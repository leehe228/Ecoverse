from django.urls import path
from . import views

urlpatterns = [
    path('update', views.update, name='update'),
    path('eat', views.eat, name='eat'),
    path('suf', views.suf, name='suf'),
]
