from django.shortcuts import render, HttpResponse, redirect
from .models import Crud
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.decorators.cache import never_cache


@never_cache
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('myadmin')
        else:
            messages.warning(request, 'Username or Password incorrect!!')
    return render (request, 'login.html')



@never_cache
def MyadminPage(request): 
      
    if 'search' in request.GET:
        search=request.GET['search']
        details=Crud.objects.filter(username__icontains=search)
    else:
        details=Crud.objects.all()
    return render(request,'myadmin.html',{'mymembers': details})


@never_cache
def HomePage(request):
    return render (request, 'myadmin.html')


@never_cache
def LogoutPage(request):
    logout(request)
    return redirect('login')

@never_cache
def UserSignup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Passwords not matching")
        else:
            foo_instance = Crud.objects.create(username=uname,email=email,password=pass1)
            foo_instance.save()
            return redirect('userlogin')
    return render (request, 'usersignup.html')

@never_cache            
def UserLogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=Crud.objects.filter(username=username,password=pass1).count()
        if user==1:
            return render(request,'userhome.html')
        else:
            messages.warning(request, 'Username or Password incorrect!!')
    return render (request, 'userlogin.html')

@never_cache
def UserHome(request):
    return render (request, 'userhome.html')

@never_cache
def UserLogout(request):
    logout(request)
    return redirect('userlogin')

@never_cache
def update_user(request):
    uid=request.GET["uid"]
    data=Crud.objects.get(id=uid)
    return render(request,"userupdate.html",{'data':data})

@never_cache
def update(request):
    id=request.POST['uid']
    add_username = request.POST['username']
    add_email=request.POST['email']
    add_password = request.POST['password1']
    Crud.objects.filter(id=id).update(username=add_username,email=add_email,password=add_password)
    return redirect('myadmin')

@never_cache
def udelete(request):
    uid=request.GET['uid']
    Crud.objects.filter(id=uid).delete()
    return redirect('myadmin')

@never_cache
def adminadduser(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Passwords not matching")
        else:
            foo_instance = Crud.objects.create(username=uname,email=email,password=pass1)
            foo_instance.save()
            return redirect('myadmin')
    return render (request, 'adminadduser.html')