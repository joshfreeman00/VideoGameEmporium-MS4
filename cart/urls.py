from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_cart, name='display_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
]
