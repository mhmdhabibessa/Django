from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('act', views.accec),
    path('get/<id>',views.show),
]