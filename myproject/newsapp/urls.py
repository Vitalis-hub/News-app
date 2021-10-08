from django.conf.urls import url
from . import views

urlpatterns = [
    #set the root of t
    url(r'^newsapp/(?P<word>.*)/$', views.news_detail ,name='news_detail'),
    url(r'^panel/news/list/$', views.news_list ,name='news_list'),
    url(r'^panel/news/add/$', views.news_add ,name='news_add'),
    url(r'^panel/news/del/(?P<pk>\d+)/$', views.news_delete ,name='news_delete'),
    url(r'^panel/news/edit/(?P<pk>\d+)/$', views.news_edit ,name='news_edit'),
<<<<<<< HEAD
    url(r'^panel/publish/edit/(?P<pk>\d+)/$', views.news_publish ,name='news_publish'),
    url(r'^urls/(?P<pk>\d+)/$', views.news_detail_short ,name='news_detail_short'),
    url(r'^all/news/(?P<word>.*)/$', views.news_all_show, name='news_all_show'),
    url(r'^news/all/$', views.all_news, name='all_news'),
    url(r'^search/$', views.all_news_search, name='all_news_search'),
=======
    
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
]