from django.urls import path 
from .import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('registr/', views.user_register, name='register'),
    path('logout/', views.user_register, name='logout'),
]