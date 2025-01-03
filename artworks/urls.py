from django.urls import path
from . import views

urlpatterns = [
    # Index
    path('', views.index, name='index'),
    
    # Categories
    path('categories/', views.category_list, name='category_list'),
    path('category/add/', views.add_category, name='add_category'),
    path('category/edit/<int:category_id>/', views.edit_category, name='edit_category'),
    path('category/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    
    # Artworks
    path('artworks/', views.artwork_list, name='artwork_list'),
    path('artworks/<int:pk>/', views.artwork_detail, name='artwork_detail'),
    path('artwork/add/', views.add_artwork, name='add_artwork'),
    path('artwork/edit/<int:pk>/', views.edit_artwork, name='edit_artwork'),
]
