from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize

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
