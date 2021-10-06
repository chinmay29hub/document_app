from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
