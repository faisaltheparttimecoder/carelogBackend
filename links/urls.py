from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from links import views

urlpatterns = [

    # Api URL, for the main category page
    url(r'^api/category/$', views.CategoryList.as_view()),

    # Api URL, for the links page for a particular ID.
    url(r'^api/category/(?P<pk>[0-9]+)/$', views.CategoryDetails.as_view()),

    # Api URL, for the main link page
    url(r'^api/links/$', views.LinksList.as_view()),

    # Api URL, for the links page for a particular ID.
    url(r'^api/links/(?P<pk>[0-9]+)/$', views.LinksDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)