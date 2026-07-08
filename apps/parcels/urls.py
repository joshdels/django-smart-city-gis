from django.urls import path
from . import views

urlpatterns = [
    path("show-parcels/", views.show_parcels, name="show_parcels"),
]
