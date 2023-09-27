from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('gamein', views.gamein, name='gamein'),
    path('gameout', views.gameout, name='gameout'),
    path('update', views.update, name='update'),
    path('load', views.load, name='load'),
    path('save', views.save, name='save'),
    path('delete', views.delete, name='delete'),
]
