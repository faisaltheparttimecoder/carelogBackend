from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from timeline import views

urlpatterns = [

    # Api URL, for the main timeline page
    url(r'^api/customer/timeline/$', views.TimelineList.as_view()),
    url(r'^api/customer/timeline/(?P<pk>[0-9]+)/$', views.TimelineDetails.as_view()),

    # Api URL, for the main timeline category page
    url(r'^api/customer/timeline_category/$', views.TimelineCategoryList.as_view()),

    # Api URL, for the main timeline page
    url(r'^api/customer/timeline_details/$', views.TimelineDetailList.as_view()),
    url(r'^api/customer/timeline_details/(?P<pk>[0-9]+)/$', views.TimelineDetailDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)