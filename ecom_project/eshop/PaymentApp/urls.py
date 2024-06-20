from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('order_success/', views.order_success, name='order_success'),
    path('add_card/', views.add_card, name='add_card'),
    # ... other patterns ...
]
