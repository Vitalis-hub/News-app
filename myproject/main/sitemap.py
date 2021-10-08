from django.contrib.sitemaps import Sitemap
from newsapp.models import Newsapp


class MyNewsSiteMap(Sitemap):

    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return Newsapp.objects.all()

    def location(self, item):
        return "/news/" + str(item)
