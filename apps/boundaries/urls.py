from django.urls import path
from . import views

urlpatterns = [
    path("boundaries", views.geographic_boundaries),
    path("regions", views.regions),
    path("provinces", views.provinces),
    path("cities", views.cities),
    path("barangays", views.barangays)
]

