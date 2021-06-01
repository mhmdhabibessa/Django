from django.urls import path     
from . import views
urlpatterns = [
    path('home',views.page),
    path('shows',views.tabels),
    # path('shows/news', views.news),
    path('create',views.add),
    path('data',views.home),
    path('tabels',views.tabels),
    # path('shows_tab',views.shows_tab),
    path('shows/<int:id>',views.show_tow),
    path('shows/<int:id>/edit',views.edit),
    path('go_back',views.go_back),
    path('delete/<int:id>',views.delete),
    path('shows/<int:id>/edit',views.update),


    # path('edit',views.edit),
    ]