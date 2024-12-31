from django.urls import path
from . import views

urlpatterns = [
    path('', views.commission_list, name='commission_list'),
    path('<int:pk>/', views.commission_detail, name='commission_detail'),
    path('add/', views.add_commission, name='add_commission'),
    path('<int:pk>/edit/', views.edit_commission, name='edit_commission'),
    path('<int:pk>/delete/', views.delete_commission, name='delete_commission'),
]