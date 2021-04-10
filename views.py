from django.contrib.auth import authenticate , login , logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Userdata

# Create your views here.

def home(request) :
    return render(request , "users/home_page.html")

def signup(request) :
    if request.method == "POST" :
        userdata = Userdata()
        userdata.first_name = request.POST["fname"]
        userdata.last_name = request.POST["lname"]
        userdata.aadhar_number = request.POST["aadhar_no"]
        userdata.address = request.POST["address"]
        userdata.gender = request.POST["gender"]
        userdata.date_of_birth = request.POST["dob"]
        userdata.mediclaim_number = request.POST["mediclaim"]
        userdata.phone_number = request.POST["phone_number"]
        userdata.email_address = request.POST["email"]
        userdata.user_name = request.POST["username"]
        userdata.password = request.POST["user_password"]
        userdata.save()
        return HttpResponseRedirect(reverse("login"))
    return render(request , "users/signup.html")

def login_view(request) :
    if request.method == "POST" :
        g_username = request.POST["l_username"]
        g_password = request.POST["l_password"]
        if Userdata.objects.get(user_name = g_username) :
            if Userdata.objects.get(user_name = g_username).password == g_password :
                #user = authenticate(request , username = g_username , password = g_password)
                #login(request , user)
                #u = Userdata.objects.get(user_name = g_username)
                return HttpResponseRedirect(reverse("index" , args = (Userdata.objects.get(user_name = g_username).health_id)))
        else :
            return render(request , "users/login.html" , {
                "message" : "Invalid credentials."
            })
    return render(request , "users/login.html")

def index(request , uhealth_id) :
    return render(request , "users/index.html" , {
        "User" : Userdata.objects.get(pk = uhealth_id)
    })
    


