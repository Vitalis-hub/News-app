from django.conf.urls import url
from . import views

urlpatterns = [
    #set the url for the site
    url(r'^newsletter/add/$', views.news_letter, name='news_letter'),
    url(r'^panel/newsletter/emails/$', views.news_emails, name='news_emails'),
    url(r'^panel/newsletter/phones/$', views.news_phones, name='news_phones'),
    url(r'^panel/newsletter/del/(?P<pk>\d+)/(?P<name>\d+)/$', views.news_txt_del, name='news_txt_del'),
    url(r'^send/email/$', views.send_email, name='send_email'),
     url(r'^check/checklist/$', views.check_mychecklist, name='check_mychecklist'),
]