from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^members/([a-z0-9-]+)/$', views.detail, name='detail') #this defines the slug
]
