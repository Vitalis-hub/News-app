from django.conf.urls import url
from . import views

urlpatterns = [
    #set the root of t
    url(r'^panel/category/list$', views.cat_list, name='cat_list'),
<<<<<<< HEAD
    url(r'^panel/category/add$', views.cat_add, name='cat_add'),
    url(r'^export/cat/csv/$', views.export_cat_csv, name='export_cat_csv'),
    url(r'^import/cat/csv/$', views.import_cat_csv, name='import_cat_csv'),
=======
     url(r'^panel/category/add$', views.cat_add, name='cat_add'),
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c

]