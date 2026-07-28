from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        # Yaha apne saare page names daalo (jo urls.py mein 'name=' hai)
        return ['home', 'handle', 'play', 'music', 'Social', 'online', 'art', 'emdr', 'cbt', 'contact', 'about', 'explore', 'form', 'onlineform', 'offlineform']

    def location(self, item):
        return reverse(item)