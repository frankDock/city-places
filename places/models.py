from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager


class Place(models.Model):
    def __unicode__(self):
        return u'{0}'.format(self.title)

    main_image = models.ImageField(verbose_name='Main image', blank=True, null=True, upload_to='places/main_images',
                                   default='places/main_images/placeholder.jpg')
    title = models.CharField(max_length=256, verbose_name='Place title', blank=False, null=False)
    address = models.CharField(max_length=256, verbose_name='Place address', blank=False, null=False)
    categories = models.ManyToManyField('Category', blank=False, verbose_name='Place categories')
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='Place tags', related_name='place')
    phone = models.CharField(max_length=64, blank=True, null=False, default='')
    budget = models.IntegerField(blank=False, null=False, default=0)
    style = models.IntegerField(blank=False, null=False, default=0)
    adventure = models.IntegerField(blank=False, null=False, default=0)
    landscape = models.IntegerField(blank=False, null=False, default=0)
    must_see = models.IntegerField(blank=False, null=False, default=0)
    energy = models.IntegerField(blank=False, null=False, default=0)
    rating = models.IntegerField(verbose_name='Rating of a place', default=0, null=False)
    positive_votes = models.IntegerField(verbose_name='Number of positive votes',
                                         default=0)
    negative_votes = models.IntegerField(verbose_name='Number of negative votes',
                                         default=0)
    images = models.ManyToManyField('PlaceImage', verbose_name='Place images', related_name='place', blank=True)

    @classmethod
    def random(cls, quantity=1):
        result = list()

        for i in range(quantity):
            result.append(cls.objects.order_by('?').first())

        return result

    def vote_up(self):
        self.rating += 1
        self.positive_votes += 1
        self.save()

    def vote_down(self):
        self.rating -= 1
        self.negative_votes += 1
        self.save()

    def total_votes(self):
        return self.positive_votes + self.negative_votes


class PlaceImage(models.Model):
    def __unicode__(self):
        return u'{0}'.format(self.description)

    class Meta:
        verbose_name = "Place image"
        verbose_name_plural = "Place images"

    image = models.ImageField(verbose_name='Image for place', upload_to='places_images')
    description = models.CharField(max_length=64)


class Category(models.Model):
    def __unicode__(self):
        return u'{0}'.format(self.category)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=64, unique=True)


class Tag(models.Model):
    def __unicode__(self):
        return u'{0} ({1})'.format(self.name, self.place.title)

    name = models.CharField(verbose_name='Tag name', max_length=64)
    rating = models.IntegerField(verbose_name='Tag rating', blank=False, null=False, default=0)

