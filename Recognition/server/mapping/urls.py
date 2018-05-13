from django.urls import path

from server.mapping import views

urlpatterns = [
    path('photo', views.photo, name='photo'),
]
