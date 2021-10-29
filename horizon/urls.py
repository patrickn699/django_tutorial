from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('', views.root, name='index'),
    path('square/', views.squar, name='square'),
    path('squ', views.square, name='squ'),
]