from django.conf.urls import url
from . import views

urlpatterns = [

    # Products URL..
    url(r'^product/$', views.products, name="products"),

    # Security URL with args..
    url(r'^product/(?P<product_id>\d+)/$', views.products, name="productsWithOptions"),

]