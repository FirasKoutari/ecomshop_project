from django.urls import path
from . import views
from .views import ProductDetailView,add_to_cart_view
# In your urls.py file
from .views import category_product_list_view
    


urlpatterns = [
    path('detail/', views.detail, name='detail'),
    path('shop/',views.shop ,name='shop'),
    path('category/<int:cid>/',category_product_list_view ,name='category'),
    # path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    # path('add-to-cart/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),

    # path('add_to_cart_view/<int:pk>/', add_to_cart_view, name='add_to_cart_view'),
    # ... other patterns ...
]
