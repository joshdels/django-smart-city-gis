from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render

from .models import Parcels, Owner, Boundary


@login_required
def home_view(request):
    context = {"user": request.user}

    return render(request, "index.html", context)


@login_required
def upload_boundaries(request):
    # to fix this for tax boundaries
    if not request.user.is_staff:
        return HttpResponseForbidden("You do not have permission")

    if request.method == "POST":
        file = request.FILES.get("boundary_file")

        if not file:
            error = "No File Uploaded"

        else:
            error = "File received successfully"

    return render(request, "upload_boundaries.html", {"error": error})


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


def regions(request):
    data = (
        Boundary.objects.values_list("region_name", flat=True)
        .distinct()
        .order_by("region_code")
    )

    return JsonResponse(list(data), safe=False)


def provinces(request):
    data = (
        Boundary.objects.values_list("province_name", flat=True)
        .distinct()
        .order_by("province_name")
    )

    return JsonResponse(list(data), safe=False)


def cities(request):
    data = (
        Boundary.objects.values_list("city_name", flat=True)
        .distinct()
        .order_by("city_name")
    )

    return JsonResponse(list(data), safe=False)


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
