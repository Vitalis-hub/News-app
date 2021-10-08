from django.conf.urls import url
from . import views

<<<<<<< HEAD

=======
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
urlpatterns = [
    #set the root of t
    url(r'^$', views.home, name='home'),
    url(r'^inner_page/$', views.inner_page, name='inner_page'),
    url(r'^panel/$', views.panel, name='panel'),
    url(r'^login/$', views.mylogin ,name='mylogin'),
<<<<<<< HEAD
    url(r'^login/register/$', views.register, name='register'),
=======
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
    url(r'^logout/$', views.mylogout ,name='mylogout'),
    url(r'^panel/setting/$', views.site_setting ,name='site_setting'),
    url(r'^panel/about/setting/$', views.about_setting ,name='about_setting'),
    url(r'^contact/$', views.contact, name='contact'),
<<<<<<< HEAD
    url(r'^panel/change/pass/$', views.change_pass ,name='change_pass'),
    url(r'^panel/answer/comments/(?P<pk>d+)/$', views.answer_cm ,name='answer_cm'),
    url(r'^show/data/$', views.show_data ,name='show_data'),

=======
     url(r'^panel/change/pass/$', views.change_pass ,name='change_pass'),
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
]