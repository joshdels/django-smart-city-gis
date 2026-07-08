from django.shortcuts import get_object_or_404, Http404
from django.http import HttpResponse
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required

from .models import Parcel
from apps.accounts import models as accounts_model

# later naning filtering sa per users' role and code
# @login_required
# def show_municipal_parcels(request):
#     if accounts_model.User == 'Admin' or 'Editor':

#         queryset = boundary


@login_required
def show_parcels(request):
    # ill filter muna per barangays
    barangays = request.GET.getlist("barangay")

    queryset = Parcel.objects.all()

    if barangays:
        queryset = queryset.filter(barangay_name__in=barangays)

    geojson = serialize(
        "geojson",
        queryset,
        geometry_field="geom",
    )

    return HttpResponse(geojson, content_type="application/json")


@login_required
def parcel_detail(request, id):
    parcel = get_object_or_404(Parcel, id=id)

    geojson = serialize(
        "geojson",
        [parcel],
        geometry_field="geom",
    )

    return HttpResponse(geojson, content_type="application/json")
