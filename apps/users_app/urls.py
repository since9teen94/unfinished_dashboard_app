from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('register', views.register, name='register'),
    path('success', views.success, name='success'),
    path('success/user', views.user_page, name='user_page'),
    path('logout', views.logout, name='logout'),
    path('create/message', views.post_message, name='post_message'),
    path('delete/message', views.delete_message, name='delete_message'),
    path('edit/message', views.edit_message, name='edit_message'),
    path('comment/message', views.comment_message, name='comment_message'),
]