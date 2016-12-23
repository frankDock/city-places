from django.shortcuts import render_to_response, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django_ajax.decorators import ajax

from custom_auth_system.models import UserProfile
from places.models import Place

range_to_int_mapping_5 = {
    "1": (0, 20),
    "2": (20, 40),
    "3": (40, 60),
    "4": (60, 80),
    "5": (80, 100),
}

range_to_int_mapping_3 = {
    "1": (0, 33),
    "2": (33, 66),
    "3": (99, 100),
}


def show_places_page(request):
    places = Place.random(10)
    context = {'places': places}
    return render(request, 'places/places-page.html', context=context)


@ajax
def vote_place_up(request):
    place_id = request.GET.get('place_id')
    place = Place.objects.get(id=place_id)
    place.vote_up()
    resp = {'result': place.positive_votes, 'total': place.total_votes()}
    return resp


@ajax
def vote_place_down(request):
    place_id = request.GET.get('place_id')
    place = Place.objects.get(id=place_id)
    place.vote_down()
    resp = {'result': place.negative_votes, 'total': place.total_votes()}
    return resp


def get_place_directions(request, place_id):
    pass


@ajax
def get_place_by_id(request):
    place_id = request.GET.get('place_id')
    place = Place.objects.get(id=place_id)
    context = {'place': place,
               'reviews': place.reviews.all(),
               'reviews_len': len(place.reviews.all()),
               'images': place.images.all()}
    return render(request, 'places/info.html', context=context)


@ajax
def save_place_to_profile(request):
    if request.method == "POST":
        place_id = request.POST.get('place_id')
        place = Place.objects.get(id=place_id)
        user = UserProfile.objects.get(user_id=request.user)
        user.saved_places.add(place)
        user.save()
        return {'result': True}


@ajax
def remove_place_from_profile(request):
    if request.method == "POST":
        place_id = request.POST.get('place_id')
        place = Place.objects.get(id=place_id)
        user = UserProfile.objects.get(user_id=request.user)
        user.saved_places.remove(place)
        user.save()
        return {'result': True}


@csrf_exempt
def apply_places_filter(request):
    if request.method == "POST":
        query_dict = request.POST

        budget_value = query_dict.get('budget-range')
        style_value = query_dict.get('style-range')
        adventure_value = query_dict.get('adventure-range')
        landscape_value = query_dict.get('landscape-range')
        must_see_value = query_dict.get('must-see-range')
        energy_value = query_dict.get('energy-range')
        tags = [x.lower() for x in query_dict.getlist('tags')]
        categories_names = [('eat-option', 'Eat'),
                            ('nightlife-option', 'Nightlife'),
                            ('sights-option', 'Sights'),
                            ('shop-option', 'Shop'),
                            ('culture-option', 'Culture'),
                            ('fun-option', 'Fun'),
                            ('sport-option', 'Sport'),
                            ('relax-option', 'Relax'),
                            ('saved-option', 'Saved')]
        selected_categories = []
        for k in categories_names:
            if query_dict.get(k[0]):
                selected_categories.append(k[1])

        places = Place.objects.filter(budget__range=range_to_int_mapping_5[budget_value],
                                      style__range=range_to_int_mapping_5[style_value],
                                      adventure__range=range_to_int_mapping_5[adventure_value],
                                      landscape__range=range_to_int_mapping_3[landscape_value],
                                      must_see__range=range_to_int_mapping_5[must_see_value],
                                      energy__range=range_to_int_mapping_5[energy_value],
                                      categories__category__in=selected_categories).distinct()

        result_places = []
        for place in places:
            r = check_tags(place, tags)
            if r:
                result_places.append(r)

        context = {'places': result_places}

        return render(request, 'places/places-page.html', context=context)

    return render(request, "places/places-page.html")


def check_tags(place, tags):
    if not tags:
        return place

    place_tags = [x.name.lower() for x in place.tags.all()]
    for tag in tags:
        if not tag.lower() in place_tags:
            return None

    return place


def search_by_tag(search_query, place):
    place_tags = [x.name.lower() for x in place.tags.all()]
    for tag in place_tags:
        if tag in search_query.lower():
            return place
    return None


def search_places(request):
    if request.method == "POST":
        search_query = request.POST.get('search_query')
        search_query = search_query.lower()
        result_places = Place.objects.filter(title__icontains=search_query).distinct()
        if not result_places:
            places = Place.objects.all()
            result_places = []
            for place in places:
                r = search_by_tag(search_query, place)
                if r:
                    result_places.append(r)
        context = {'places': result_places}

        return render(request, 'places/places-page.html', context=context)
    else:
        return redirect('places.index')
