from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from products import views

urlpatterns = [

    # Api URL, for the main product page
    url(r'^api/products/$', views.ProductsList.as_view()),

    # Api URL, for the product page with a given ID.
    url(r'^api/products/(?P<pk>[0-9]+)/$', views.ProductsListDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)