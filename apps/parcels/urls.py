from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("api/boundaries", views.geographic_boundaries),
    path("api/regions", views.regions),
    path("api/provinces", views.provinces),
    path("api/cities", views.cities),
    path("api/barangays", views.barangays)
]

