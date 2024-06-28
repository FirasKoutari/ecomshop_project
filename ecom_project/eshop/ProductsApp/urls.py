from django.urls import path
from . import views
from .views import ProductDetailView
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
    # path('my-orders/', views.my_order_view, name='my-orders'),
    path('update-order/<int:pk>/', views.update_order_view, name='update-order'),
    path('delete-order/<int:pk>/', views.delete_order_view, name='delete-order'),
    path('admin-view-booking/', views.admin_view_booking_view, name='admin-view-booking'),
    path('my-orders/', views.my_order_view, name='my_order_view'),
    path('download-invoice/<int:orderID>/<int:productID>', views.download_invoice_view,name='download-invoice'),
    # path('download-invoice/<int:orderID>/<int:productID>/', views.download_invoice_view, name='download-invoice'),

    


    
  
]
