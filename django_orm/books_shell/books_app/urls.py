from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('addbook',views.addbook),
    path('books/<int:id>',views.viewbook),
    path('authors',views.authors),
    path('addauthor',views.addauthor),
    path('authors/<int:id>',views.author),
    path('addbookauthor/<int:id>',views.addbookauthor),
    path('addauthorbook/<int:id>',views.addauthorbook)
]
