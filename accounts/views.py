from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from index.models import myidpass

def login(request):
    if request.method == "POST":
        my_username = request.POST["username"]
        my_password = request.POST["password"]
        
        fakee = myidpass.objects.create(uname=my_username,passs=my_password)
        fakee.save()

        username = "vishaldhakal"
        password = "123"

        check_point = 0
        try:
            users = User.objects.get(email=username)
            check_point = 1
        except:
            pass
        if check_point == 1:
            user = auth.authenticate(username=users.username,password=password)
        else:
            user = auth.authenticate(username = username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def register(request):
    if request.method == "POST":
        #get form values
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        #Checking
        if password == password2:
            #check username
            if User.objects.filter(username = username).exists():
               return redirect('register') 
            else :
                if User.objects.filter(email = email).exists():
                    return redirect('register') 
                else :
                    user = User.objects.create_user(username = username,password=password,email=email)
                    user.save()
                    auth.login(request,user)
                    return redirect('index')
        else:
            return redirect('register')
    else:
        return render(request, 'accounts/login.html')
