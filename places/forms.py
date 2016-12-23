from django import forms


class PlacesFiltersForm(forms.Form):
    category_eat = forms.BooleanField()
    category_nightlife = forms.BooleanField()
    category_sights = forms.BooleanField()
    category_shop = forms.BooleanField()
    category_culture = forms.BooleanField()
    category_fun = forms.BooleanField()
    category_sport = forms.BooleanField()
    category_relax = forms.BooleanField()
    category_saved = forms.BooleanField()
    budget_range = forms.IntegerField(min_value=1, max_value=5)
    style_range = forms.IntegerField(min_value=1, max_value=5)
    adventure_range = forms.IntegerField(min_value=1, max_value=5)
    landscape_range = forms.IntegerField(min_value=1, max_value=3)
    must_see_range = forms.IntegerField(min_value=1, max_value=5)
    energy_range = forms.IntegerField(min_value=1, max_value=5)
