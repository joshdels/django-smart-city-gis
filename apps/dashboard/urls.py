from django.urls import path
from . import views

urlpatterns = [
  path("parcel-map", views.map_dashboard, name="parcel_dashboard"),
  path("parcel-detail/<int:id>", views.parcel_detail, name="parcel-detail")
]
