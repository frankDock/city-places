from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

from places.models import Place


class UserProfile(models.Model):
    def __unicode__(self):
        return u'@{0} ({1})'.format(self.user_id.username, self.status)

    user_id = models.OneToOneField(User, verbose_name='User object', unique=True, related_name='profile')
    profile_photo = models.ImageField(verbose_name='Profile photo', width_field=333, height_field=333, blank=True,
                                      upload_to='users/profile_photos')
    location = models.CharField(max_length=64, verbose_name='User location', default='')
    status = models.CharField(max_length=64, verbose_name='User status', default='User')
    saved_places = models.ManyToManyField(Place, verbose_name='Saved places', blank=True)
    followers = models.ManyToManyField('self', verbose_name='User followers', blank=True)
    following = models.ManyToManyField('self', verbose_name='User following', blank=True)

    @classmethod
    def get_by_id(cls, user_id):
        return User.objects.get(id=user_id)