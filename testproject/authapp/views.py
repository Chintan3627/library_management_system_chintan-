from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
# from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate
# from

# from 
# Create your views here.


def home(request):
    return render(request,'index.html')

def LogoutView(request):
    logout(request)
    return redirect('home')

def registration_page(request):
    if request.method != "POST":
        return render(request, 'registration.html')
    else:
        stetus = registration(request)
        if stetus.status_code == 200:
            messages.success(request, 'suuces fully rgister you can login')
            return redirect('home')
        else:
            messages.error(request,'somthing is not righ please try again')
            return render(request, 'registration.html')

def login_page(request):
    if request.method == "POST":
        # import pdb; pdb.set_trace()
        status = login_view(request)
        if status.status_code == 200:
            messages.success(request, 'suucesfully login')
            return redirect('home')
        else:
            messages.success(request, 'Please provied valied username or password')
            return render(request,'login.html')
    return render(request,'login.html')


@api_view(['POST'])
def registration(request):
    # import  pdb; pdb.set_trace()
    try:
        user = LibararyUser.objects.create_user(
                username= request.data['username'],
                  password= request.data['password'],
                  user_type=request.data['user_type'],
                  phone_number=request.data['phone_number'],
                  first_name=request.data['first_name'],
                  last_name=request.data['last_name'],
                  email = request.data["email"],
                  is_active = True
                  )
        return Response(status=200)
    except Exception as e:
        
        return Response(status=400)
    
@api_view(['POST'])      
def login_view(request):
    username_ = request.data['username']
    password_ = request.data['password']
    user = authenticate(username=username_, password=password_)
    if user:
        login(request, user)
        return Response(status=200) 
    else:
        return Response(status=200) 

