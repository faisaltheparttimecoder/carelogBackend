from django.conf.urls import url
from . import views

urlpatterns = [

    # Core URL..
    url(r'^login/$', views.login, name="login"),

]