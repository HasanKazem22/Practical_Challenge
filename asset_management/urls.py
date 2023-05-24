from django.urls import path
from . import views

urlpatterns = [
    path('', views.AssetList, name='asset_list'),
    path('assets/create/', views.AssetCreate, name='asset_create')
]