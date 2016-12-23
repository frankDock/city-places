import json

from django_ajax.decorators import ajax

from places.models import Place
from reviews.models import Review, ReviewCategory
from custom_auth_system.models import UserProfile


@ajax
def post_review(request):
    categories_mapping = {
        "review-category-general": "General",
        "review-category-atmosphere": "Atmosphere",
        "review-category-food": "Food",
        "review-category-prices": "Prices"
    }

    json_data = json.loads(request.POST.get('data'))
    data = dict()
    for j in json_data:
        data[j['name']] = j['value']

    review = Review(user_id=request.user.id)
    review.save()
    for value in data:
        if value in categories_mapping:
            category = ReviewCategory(name=categories_mapping[value], review=review)
            category.save()
            review.categories.add(category)

    place_id = request.POST.get('place_id')
    review.place = Place.objects.get(id=place_id)
    review.text = data['review-text']
    review.save()


@ajax
def vote_review_up(request):
    review_id = request.POST.get('review_id')
    review = Review.objects.get(id=review_id)
    review.vote_up()
    return {'result': review.rating}


@ajax
def vote_review_down(request):
    review_id = request.POST.get('review_id')
    review = Review.objects.get(id=review_id)
    review.vote_down()
    return {'result': review.rating}
