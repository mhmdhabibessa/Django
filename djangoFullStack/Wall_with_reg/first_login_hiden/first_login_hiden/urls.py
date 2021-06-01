from django.urls import path, include           # import include
# from django.contrib import admin              # comment out, or just delete
urlpatterns = [
    path('', include('start_my_app.urls')),
    path('login', include('start_my_app.urls')),

]