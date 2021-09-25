from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/read/', adminapp.users, name='users'),
    path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('users/create/<int:pk>/', adminapp.user_delete, name='user_delete'),

    path('categories/create/', adminapp.category_create, name='category_create'),
    path('categories/read/', adminapp.categories, name='categories'),
    path('categories/update/<int:pk>/', adminapp.category_update, name='category_update'),
    path('categories/create/<int:pk>/', adminapp.category_delete, name='category_delete'),

    path('products/create/<int:pk>/', adminapp.product_create, name='product_create'),
    path('products/read/<int:pk>', adminapp.products, name='products'),
    path('products/read/category/<int:pk>/', adminapp.product_read, name='product_read'),
    path('products/update/<int:pk>/', adminapp.product_update, name='product_update'),
    path('products/create/<int:pk>/', adminapp.product_delete, name='product_delete'),
]