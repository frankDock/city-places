"""elleday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

import custom_auth_system.views as custom_auth_system_views
import static_pages.views as static_pages_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^places/', include('places.urls', namespace='places')),
    url(r'^reviews/', include('reviews.urls', namespace='reviews')),
    url(r'^$', static_pages_views.homepage, name='homepage'),
    url(r'^contact$', static_pages_views.contact, name='contact'),
    url(r'^company$', static_pages_views.company, name='company'),
    url(r'^logout/', custom_auth_system_views.logout_user, name='logout')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
