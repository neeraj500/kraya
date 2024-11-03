from django.contrib import admin
from django.urls import path

from core.views import frontpage, shop
from product.views import product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
]
