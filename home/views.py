from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login

#password for test user-Tan1shq@2003 ,arabialibaba:alibaba@1234

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html') 

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        #check if user has entered correct credentials
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            print("I am in user if condition")
            # A backend authenticated the credentials
            login(request,user)
            return redirect(dashboard)    
        else:
            print("I am in Else condition")
            # No backend authenticated the credentials
            return render(request,'login.html') 
    
    return render(request,'login.html') 

def logoutUser(request):
    logout(request)
    return redirect("/login") 

def dashboard(request):
    print(request)
    print("I am in dashboard view function")
    return render(request, 'dashboard.html')
