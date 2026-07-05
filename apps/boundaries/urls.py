from django.urls import path
from . import views

urlpatterns = [
    path("city_geoboundaries", views.city_geoboundaries, name="city_geoboundaries"),
    path("regions_lists", views.regions, name="regions_lists"),
    path("provinces_lists", views.provinces, name="provinces_lists"),
    path("cities_lists", views.cities, name="cities_lists"),
    path("barangays_lists", views.barangays, name="barangays_lists")
]

