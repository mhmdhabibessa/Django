from django.urls import path     
from . import views
urlpatterns = [
path("blogs", views.index),
path("", views.root),
path("blogs/new", views.new) ,
path('blogs/create', views.create),
path('blogs/<number>',views.show),
path('blogs/<number>/edit',views.edit),
path('blogs/<number>/delete',views.destroy)

 
 
]
