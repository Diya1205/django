# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctor/', views.doctor_profile, name='doctor_profile'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
     path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    
]
