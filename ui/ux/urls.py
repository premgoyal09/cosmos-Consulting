from django.contrib import admin
from django.urls import path, include

from .import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('home', views.home_view, name='home'),
    path('about', views.about, name='about'),
    path('whychoose', views.whychoose, name='whychoose'),
    path('industry', views.industry, name='industry'),
    path('contact', views.contact, name='contact'),
    path('signup/', views.signup_view, name='signup'),
    path('login', views.login_view, name='login'),
    # path('users/', views.users_view, name='users'),
    path('logout', views.logout_view, name='logout'),
]
