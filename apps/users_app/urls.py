from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('register', views.register, name='register'),
    path('success', views.success, name='success'),
    path('logout', views.logout, name='logout')
]