from django.urls import path

from . import views

urlpatterns = [
    path("<int:uhealth_id>" , views.index , name = "index") ,
    #path("logout" , views.logout_view , name = "logout") ,
    path("home" , views.home , name = "home") ,
    path("signup" , views.signup , name = "signup") , 
    path("login" , views.login_view , name = "login")
]