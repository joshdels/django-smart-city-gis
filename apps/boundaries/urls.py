from django.urls import path
from . import views

urlpatterns = [
    path("city-geoboundaries", views.city_geoboundaries, name="city_geoboundaries"),
    path("regions-lists", views.regions, name="regions_lists"),
    path("provinces-lists", views.provinces, name="provinces_lists"),
    path("cities-lists", views.cities, name="cities_lists"),
    path("barangays-lists", views.barangays, name="barangays_lists")
]

