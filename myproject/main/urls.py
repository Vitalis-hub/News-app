from django.conf.urls import url
from . import views

urlpatterns = [
    #set the root of t
    url(r'^$', views.home, name='home'),
    url(r'^inner_page/$', views.inner_page, name='inner_page'),
    url(r'^panel/$', views.panel, name='panel'),
    url(r'^login/$', views.mylogin ,name='mylogin'),
    url(r'^logout/$', views.mylogout ,name='mylogout'),
    url(r'^panel/setting/$', views.site_setting ,name='site_setting'),
    url(r'^panel/about/setting/$', views.about_setting ,name='about_setting'),
    url(r'^contact/$', views.contact, name='contact'),
     url(r'^panel/change/pass/$', views.change_pass ,name='change_pass'),
]