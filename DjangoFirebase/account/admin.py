from django.contrib import admin
from .models import FirebaseUserManager,FirebaseUser

admin.site.register(FirebaseUser)

# firebase에서 db_table을 짜야함