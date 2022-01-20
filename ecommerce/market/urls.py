from django.urls import path

from . import views

app_name = 'market'

urlpatterns = [
    path('', views.myProducts, name='myProducts'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
]