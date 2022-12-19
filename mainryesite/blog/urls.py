from django.urls import path
from . import views
from .feeds import LatestPostFeed

app_name = 'blog'

urlpatterns = [
   
    #def post_list
    path('', views.post_list, name='post_list'),
    
    #Class PostListView    
    #path('', views.PostListView.as_view(), name='post_list'),
   
    # Path for the post.
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
            views.post_detail,
            name='post_detail'),
   
    # Path for the blog share feature.
    path('<int:post_id>/share/',
          views.post_share, name='post_share'),
   
    # Path for comments.
    path('<int:post_id>/comment/',
          views.post_comment, name='post_comment'),
   
    # Path for list by tag
    path('tag/<slug:tag_slug>/',
         views.post_list, name='post_list_by_tag'),

      # For RSS
    path('feed/', LatestPostFeed(), name='post_feed'),  
]