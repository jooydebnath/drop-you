from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logoutuser, name='logout'),


    path('profile/', views.profile, name='profile'),
    path('profile-settings/', views.update_information, name='profile-settings'),
    path('basic-information/', views.basic_information, name='basic-information'),
    path('contact-information/', views.contact_information, name='contact-information'),


    path('drop-you/', views.dorp_you, name='drop-you'),



    path('dashboard/', views.dashboard, name='dashboard'),
]
