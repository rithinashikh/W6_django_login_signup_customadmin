from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.UserSignup, name='usersignup'),
    path('myadmin/', views.MyadminPage, name='myadmin'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('userlogin/', views.UserLogin, name='userlogin'),
    path('userhome/', views.UserHome, name='userhome'),
    path('userlogout/', views.UserLogout, name='userlogout'),
    path('update_user/',views.update_user,name="update_user"),
    path('update/',views.update,name="update"),
    path('udelete/',views.udelete, name="udelete"),
    path('adminadduser/',views.adminadduser, name="adminadduser"),

]
