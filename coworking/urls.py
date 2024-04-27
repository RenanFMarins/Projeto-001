from django.urls import path

from . import views
pp_name = 'coworkings'

urlpatterns = [
    path('', views.home, name="coworkings-home"),
    path('coworking/<int:id>/', views.coworking, name="coworkings-coworking"),
]