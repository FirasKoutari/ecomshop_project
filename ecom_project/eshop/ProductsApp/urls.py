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
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('add_review/<int:product_id>/', views.add_review, name='add_review'),
    path('shop1/', views.products_view, name='shop_products_view'),
    # path('shop/', views.filter, name='shop_filter'),  # Utilisation de 'filter' pour la vue
    path('shop/filter/', views.shop_filter, name='shop_filter'),  


    
  
]
