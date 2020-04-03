from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

class FirebaseUserManager(BaseUserManager):    
    use_in_migrations = True    

    def create_user(self, email, nickname, password=None):                
        # if not email :            
        #     raise ValueError('must have user email')        
        user = self.model(            
            email = self.normalize_email(email),            
            nickname = nickname        
        )        
        user.set_password(password)        
        user.save(using=self._db)        
        return user     
    def create_superuser(self, email, nickname,password ):        
        user = self.create_user(            
            email = self.normalize_email(email),            
            nickname = nickname,            
            password=password        
        )        
        user.is_admin = True        
        user.is_superuser = True        
        user.is_staff = True        
        user.save(using=self._db)        
        return user 



class FirebaseUser(AbstractBaseUser):
    class Meta:
        db_table = 'users'
        verbose_name = '유저'
        verbose_name_plural = '유저들'

    objects = FirebaseUserManager()

    uid = models.CharField(
        primary_key=True,
        unique=True,
        max_length=100,
        verbose_name='유저 UID (Firebase 에서 자동 생성)'
    )
    last_login = models.DateTimeField(auto_now=True, verbose_name='최근 로그인 일자')
    is_active = models.BooleanField(default=True, verbose_name='활성화 여부')
    is_admin = models.BooleanField(default=False, verbose_name='관리자 여부')

    USERNAME_FIELD = 'uid'

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_active

    def has_module_perms(self, app_label):
        return self.is_active