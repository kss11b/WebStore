from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^load_product/(?P<id>\d+)$', views.load_product)
 ]
