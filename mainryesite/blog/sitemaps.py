from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):

    # This can be changed to whatever is need.
    # I am using weekly, because it makes the most since.
    # For me.
    # More info found: https://docs.djangoproject.com/en/4.1/ref/contrib/sitemaps/
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated