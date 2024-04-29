from django.urls import path

from . import views
app_name = 'coworkings'

urlpatterns = [
    path('', views.home, name="home"),
    path('coworking/category/<int:category_id>/', views.category,
         name="category"),
    path('coworking/<int:id>/', views.coworking, name="coworking"),
]
