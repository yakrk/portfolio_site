from django.urls import path
from . import views  # viewsにあるすべてを持ってくる


urlpatterns = [
    path('', views.commerce_top, name='commerce_top'),
    path('<int:category_id>/', views.category_top, name="category_top"),
    path('<int:category_id>/<int:product_id>/', views.product_details, name="product_details"),
    path('cart/', views.cart_top, name="cart_top"),
    path('cart/<int:cart_item_id>', views.cart_item_delete, name="cart_item_delete"),
    path('cart/completed/', views.cart_end, name="cart_end"),
    path('purchase-history/', views.purchase_history, name="purchase_history"),
    path('purchase-history/<int:purchase_id>/', views.purchase_history_details, name="purchase_history_details"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    
]
