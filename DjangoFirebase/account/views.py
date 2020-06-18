from django.shortcuts import render
# import pyrebase
from firebase import firebase as fb
import firebase_admin

# firebaseConfig={
#             'apiKey' : "AIzaSyB0noCCCErBRiQGrK8o0NrDVN9GSRjVOXQ",
#             'authDomain' : "fir-djangouser.firebaseapp.com",
#             'databaseURL' : "https://fir-djangouser.firebaseio.com",
#             'projectId' : "fir-djangouser",
#             'storageBucket' : "fir-djangouser.appspot.com",
#             'messagingSenderId' : "227062425443",
#             'appId' : "1:227062425443:web:23ccd4e33d1560d33d9556"
#             };

# firebase = pyrebase.initialize_app(firebaseConfig)

# auth=firebase.auth()

def signin(request):
    return render(reqeust,"index.html")
    

# Create your views here.
def index(request):
    return render(request, 'index.html')