from django.shortcuts import render
from .models import *
# Create your views here.
# define register view template

def RegisterPage(request):
    return render(request, 'app/register.html')


def UserRegister(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']


# first we will validate that user already exits

        user = User.objects.filter(Email=email)

        if user:
            message = "User already exist"
            return render(request,"app/register.html", {'msg':message})
        else:
            if password == cpassword:
                
                newuser = User.objects.create(Firstname=fname, Lastname=lname, Email=email, Contact=contact, Password=password )
                
                message = "user register successfully"
                return render(request, "app/login.html", {'msg':message})   
            else:
                message = "password and conform password doesn't match"

                return render(request,"app/register.html", {'msg':message})
            


# Login view

def LoginPage(request):
    return render(request, "app/login.html")  

# user login 

def LoginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password'] 


   # checking email id for database

        user = User.objects.get(Email=email)

        if user:
            if user.Password == password:
                # we are getting user data in session
                request.session['Firstname'] = user.Firstname
                request.session['Lastname']  = user.Lastname  
                request.session['Email'] = user.Email 

                return render(request,'app/home.html')

            else:
                message="Password Doesn't match"
                return render(request, "app/login.thml",{'msg':message})
            
        else:
            message = "User doesn't Exit"
            return render(request, "app/register.html",{'msg':message})

