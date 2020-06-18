from firebase_admin import auth
from account.models import FirebaseUser


class FirebaseBackend:
    def authenticate(self, email=None, password=None, uid=None):
        try:
            auth.get_user(uid)
            return FirebaseUser.objects.get(uid=uid)
        except FirebaseUser.DoesNotExist:
            return FirebaseUser.objects.create(email=email, password=password, uid=uid)
        # except (auth.AuthError, ValueError):
        except:
            print("인증실패!!")
            return None
        
        # django 내부에서 uid를 생성하지 않고
        # firebase에서 제공하는 uid를 통해서 User의 Pk로 사용한다.


# python manage.py shell
# >> from DjangoFirebase.backends import *
# >> Users = FirebaseBackend()
# >> Users.authenticate(email = "gt0305@likelion.org", nickname = "me", password = "1")