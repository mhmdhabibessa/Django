from django.urls import path
from . import views


urlpatterns = [
    path('', views.root),
    path('login', views.login),
    path('register', views.register),
    path('logout',views.logout),
    path('thoughts',views.thoughts),
    path('add_thought',views.add_thought),
    path('thoughts/<int:id>', views.details),
    path('thoughts/like/<int:id>', views.like),
    path('thoughts/unlike/<int:id>', views.unlike),
    path('thoughts/delete/<int:id>', views.delete),

]