from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize

from .models import Boundary

#TODO 1. fix this boundaries as name first for querries later
# copy the parcels_boundaries to Boundaries_boundaries?? DB


@login_required
def geographic_boundaries(request):
    queryset = Boundary.objects.filter(city_name="Davao City")

    geojson = serialize(
        "geojson",
        queryset,
        geometry_field="geom",
        fields=("barangay_name", "city_name"),
    )

    return HttpResponse(
        geojson,
        content_type="application/json",
    )


@login_required
def regions(request):
    data = (
        Boundary.objects.values_list("region_name", flat=True)
        .distinct()
        .order_by("region_code")
    )

    return JsonResponse(list(data), safe=False)


@login_required
def provinces(request):
    data = (
        Boundary.objects.values_list("province_name", flat=True)
        .distinct()
        .order_by("province_name")
    )

    return JsonResponse(list(data), safe=False)


@login_required
def cities(request):
    data = (
        Boundary.objects.values_list("city_name", flat=True)
        .distinct()
        .order_by("city_name")
    )

    return JsonResponse(list(data), safe=False)


@login_required
def barangays(request):
    data = (
        Boundary.objects.values_list("barangay_name", flat=True)
        .distinct()
        .order_by("barangay_name")
    )

    return JsonResponse(list(data), safe=False)


def barangay_boundaries(request):
    pass


# TODO 1. Params and its address... in a form
# Also add a abstract model to assign its region and city so that the city per customer is used to filter its cities....
