from django.contrib import admin
from custom_auth_system.models import UserProfile


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserAdmin)
