from django.contrib import admin
from places.models import Category, Place, PlaceImage


class CategoryAdmin(admin.ModelAdmin):
    pass


class PlaceAdmin(admin.ModelAdmin):
    pass


class PlaceImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceImage, PlaceImageAdmin)
