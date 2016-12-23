from django.conf.urls import url

import places.views as places_views

urlpatterns = [
    url(r'vote/up', places_views.vote_place_up, name='vote_up'),
    url(r'vote/down', places_views.vote_place_down, name='vote_down'),
    url(r'get', places_views.get_place_by_id, name='get_by_id'),
    url(r'save', places_views.save_place_to_profile, name='save'),
    url(r'remove', places_views.remove_place_from_profile, name='remove'),
    url(r'filter/', places_views.apply_places_filter, name='apply_filters'),
    url(r'search/', places_views.search_places, name='search'),
    url(r'', places_views.show_places_page, name='index'),
]
