from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('welcom', views.welcom),
    path('register',views.register),
    path('logout',views.log_out),
    path('page_one',views.page_one),
    path('add_book',views.add_book),


    ]
