from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.Login, name='login'),
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
    path('home/', views.Home, name='home'),
    path('logout/', views.Logout, name='logout')
]
