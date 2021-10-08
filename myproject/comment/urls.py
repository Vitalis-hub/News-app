from django.conf.urls import url
from . import views

urlpatterns = [
    #set the root of t
    url(r'^comment/add/news/(?P<pk>\d+)?$', views.news_cm_add, name='news_cm_add'),
    url(r'^comment/list/$', views.comments_list, name='comments_list'),
    url(r'^comment/del/(?P<pk>\d+)/$', views.comments_del, name='comments_del'),
    url(r'^comment/confirm/(?P<pk>\d+)/$', views.comments_confirm, name='comments_confirm'),
]