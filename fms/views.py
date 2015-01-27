from django.shortcuts import render
from django.contrib.auth import logout

# Create your views here.

def index(request):
    logout(request)
    return render(request,'fms/index.html',{})