from django import template
from ..models import Post
from django.db.models import Count

# Required by django template library.
# see more here: https://docs.djangoproject.com/en/4.1/howto/custom-template-tags/
register = template.Library()

@register.simple_tag
def total_posts():
    """ Just a simple demo to return all post published. """
    return Post.published.count()
    
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    """ Returns a list of latest post to lastest_posts html file.
        Can be used anywhere by calling the latest_posts html file."""
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

@register.simple_tag
def most_commented_posts(count=5):
    """ Gets the 5 most commented on posts. """
    return Post.published.annotate(
                total_comments=Count('comments')
    ).order_by('-total_comments')[:count]