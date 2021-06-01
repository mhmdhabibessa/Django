from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index),
    path('reg', views.regestration),
    path('log', views.login),
    path('welcome', views.welcome),
    path('add_thro',views.add_thro),
    path('logout', views.logout),
    path('show',views.show),
  
]

