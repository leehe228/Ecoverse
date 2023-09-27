from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.upload, name='upload'),
    path('update', views.update, name='update'),
    path('delete', views.delete, name='delete'),
]
