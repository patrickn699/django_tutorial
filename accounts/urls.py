from django.urls import path
from . import views

urlpatterns = [
   
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
'''
 path('hello/', views.hello, name='hello'),
    path('', views.root, name='index'),
    path('square/', views.squar, name='square'),
    path('squ', views.square, name='squ'),
    '''
