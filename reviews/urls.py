from django.conf.urls import url

import reviews.views as reviews_views

urlpatterns = [
    url(r'vote/up', reviews_views.vote_review_up, name='vote_up'),
    url(r'vote/down', reviews_views.vote_review_down, name='vote_down'),
    url(r'post', reviews_views.post_review, name='post'),
]
