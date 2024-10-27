from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('',views.homepage,name="home-page"),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    
]