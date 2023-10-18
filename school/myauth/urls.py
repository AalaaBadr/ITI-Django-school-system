from django.urls import path
from .views import *

urlpatterns = [
    path('login', logIn, name='login'),
    path('Logout', logout, name='logout'),
    path('register', register, name='register'),
]
