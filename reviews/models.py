from __future__ import unicode_literals

from django.db import models
from places.models import Place
from custom_auth_system.models import UserProfile


class Review(models.Model):
    def __str__(self):
        return '{0} ({1})'.format(self.title, self.place.title)

    title = models.CharField(max_length=256)
    text = models.TextField()
    rating = models.IntegerField(blank=True, default=0)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subreviews')
    place = models.ForeignKey(Place, null=True, blank=True, related_name='reviews')
    user = models.ForeignKey(UserProfile, null=False, blank=False, related_name='reviews')
    date_created = models.DateTimeField(auto_now=True)

    def vote_up(self):
        self.rating += 1
        self.save()

    def vote_down(self):
        self.rating -= 1
        self.save()


class ReviewCategory(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=64)
    review = models.ForeignKey('Review', null=True, blank=True, related_name='categories')
