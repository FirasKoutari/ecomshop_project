from django.urls import path
from . import views

urlpatterns = [
    path('detail/', views.detail, name='detail'),
    path('shop/',views.shop ,name='shop'),
    # ... other patterns ...
]