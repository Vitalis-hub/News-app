"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
<<<<<<< HEAD
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap
from main.sitemap import MyNewsSiteMap
from rest_framework import routers
from main import views

router = routers.DefaultRouter()
router.register(r'mynews', views.NewsViewSet)
sitemaps = {
    'news': MyNewsSiteMap(),
}
=======
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    url(r'rest/',include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap',),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

=======
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
    url(r'', include('main.urls')),
    url(r'', include('newsapp.urls')),
    url(r'', include('cat.urls')),
    url(r'', include('subcat.urls')),
    url(r'', include('contactform.urls')),
    url(r'', include('trending.urls')),
<<<<<<< HEAD
    url(r'', include('manager.urls')),
    url(r'', include('newsletter.urls')),
    url(r'', include('comment.urls')),
    url(r'', include('blacklist.urls')),

=======
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
]

if settings.DEBUG:
    #make a dynamc urll for all static files
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
