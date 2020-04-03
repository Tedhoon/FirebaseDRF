from firebase_admin import auth
from account.models import FirebaseUser


class FirebaseBackend:
    def authenticate(self, request, uid=None):
        try:
            auth.get_user(uid)
            return MyUser.objects.get(uid=uid)
        except FirebaseUser.DoesNotExist:
            return FirebaseUser.objects.create(uid=uid)
        except (auth.AuthError, ValueError):
            return None
        
        # django 내부에서 uuid를 생성하지 않고
        # firebase에서 제공하는 uid를 통해서 User의 primarykey처럼 사용한다.


# python manage.py shell
# >> from DjangoFirebase.backends import *
# >> FirebaseBackend.authenticate()