from django.urls import path
from . import views

urlpatterns = [path("map", views.map_dashboard, name="map_dashboard")]
