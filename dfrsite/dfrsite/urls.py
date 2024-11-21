# urls.py

from django.contrib import admin
from django.urls import path

from wb_api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', ProductViewSet.as_view(({'get': 'list'})), name='product-list'),  # GET request to list products
    path('api/v1/products/add/', ProductCreateAPIView.as_view(), name='product-add'),  # POST request for adding a product
    path('api/v1/products/form/', ProductFormView.as_view(), name='product-form'),  # Form for sending requests
]