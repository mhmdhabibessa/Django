from django.urls import path, include
urlpatterns = [
    path('', include('orm_app.urls')),]