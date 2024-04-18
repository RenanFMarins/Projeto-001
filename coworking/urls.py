from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('coworking/<int:id>/', views.coworking),
]