from django.conf.urls import url
from . import views

urlpatterns = [
    #set the root of t
    url(r'^panel/category/list$', views.cat_list, name='cat_list'),
     url(r'^panel/category/add$', views.cat_add, name='cat_add'),

]