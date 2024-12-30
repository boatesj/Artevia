from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('artworks/', views.artwork_list, name='artwork_list'),
    path('artworks/<int:pk>/', views.artwork_detail, name='artwork_detail'),
]
