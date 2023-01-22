from ast import Not
from multiprocessing import context
from django.contrib.auth.models import auth,User
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from . forms import Myform,Loginform
from . models import Log_in
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def Index(request):
    return render(request,'login_app/index.html')
def Sign_up(request):
    
    context={}
    form = Myform(request.POST or None)
    
    context["form"]=form
    if form.is_valid():       
        form.save()
        return HttpResponseRedirect('/')
    return render(request,'login_app/sign_up.html',context)
    
def User_login(request):
    form=Loginform(request.POST)
    context={}
    context["form"]=form
    
    if request.method=='POST':
        
        # if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            details=Log_in.objects.all()

            if Log_in.objects.filter(username=username).exists():
                if Log_in.objects.filter(password=password).exists():
                    return HttpResponse("ok")
                else:
                    return HttpResponse("not ok")   

            else:
                return HttpResponse("not ok")        
            
            # print(username)
            # user =authenticate(request,username= username,password=password)
            # print(user)
            # if user is not None:
            #     login(request, user)
            #     return redirect('/')
            #     # return HttpResponse("find the user")
            # else:
            #     messages.info(request,'invalid')  
            #     # return HttpResponse("wrong")
       
    
    return render(request,"login_app/login.html",context)
