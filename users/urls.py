from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
        path('', include('django.contrib.auth.urls')), # включает пути login, logout 
        path('register/', views.register, name='register'), # регистрация
        ]
