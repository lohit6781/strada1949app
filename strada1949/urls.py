from django.contrib import admin
from django.urls import path
from strada1949 import views

urlpatterns = [
    path('', views.home, name='Default'),
    path('home/', views.home, name='Home'),
    path('products/<str:category>', views.products, name='Products'),
    path('collection/<str:collection_url>', views.collections, name='Collections'),
    path('product/<str:product_id>', views.productView, name='ProductView'),
    path('cart/', views.cart, name='Cart'),
    path('redirect/', views.redirection, name='Redirection'),
    path('terms-of-service/', views.termsConditions, name='TermsAndCondition'),
    path('test/', views.test, name='test'),
    path('success/', views.success, name='success'),
    path('failure/', views.failure, name='failure'),
    path('del/', views.deleteSession, name='del'),
]

handler404 = 'strada1949.views.handler404'
handler500 = 'strada1949.views.handler500'