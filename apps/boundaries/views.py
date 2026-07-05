from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize

from .models import Boundary


@login_required
def city_geoboundaries(request):
    """Returns barangay boundaries after filtering a city/municipal name"""

    city_name = request.GET.get("city_name")
    city_code = request.GET.get("city_code")

    if not city_code and not city_name:
        return JsonResponse(
            {"error": "Provide a parameter either city_code or city_name"}, status=(400)
        )

    queryset = Boundary.objects.all()

    if city_code:
        queryset = queryset.filter(city_code=city_code)
    elif city_name:
        queryset = queryset.filter(city_name=city_name)

    geojson = serialize(
        "geojson",
        queryset,
        geometry_field="geom",
        fields=("barangay_name", "barangay_code", "city_name"),
    )

    return HttpResponse(
        geojson,
        content_type="application/json",
    )


@login_required
def regions(request):
    data = (
        Boundary.objects.values_list("region_name", "region_code")
        .distinct()
        .order_by("region_code")
    )

    return JsonResponse(list(data), safe=False)


@login_required
def provinces(request):
    """Returns provinces name list with optional filters"""

    region_name = request.GET.get("region_name")
    region_code = request.GET.get("region_code")

    queryset = Boundary.objects.all()

    if region_code:
        queryset = queryset.filter(region_code=region_code)
    elif region_name:
        queryset = queryset.filter(region_name=region_name)

    data = (
        queryset.values_list("province_name", "province_code")
        .distinct()
        .order_by("province_name")
    )

    return JsonResponse(list(data), safe=False)


@login_required
def cities(request):
    """Returns cities name list with optional filters"""

    province_code = request.GET.get("province_code")
    province_name = request.GET.get("province_name")

    queryset = Boundary.objects.all()

    if province_code:
        queryset = queryset.filter(province_code=province_code)
    elif province_name:
        queryset = queryset.filter(province_name=province_name)

    data = (
        queryset.values_list(
            "city_name",
            "city_code",
        )
        .distinct()
        .order_by("city_name")
    )

    return JsonResponse(list(data), safe=False)


@login_required
def barangays(request):
    """Returns cities name list with optional filters"""

    city_code = request.GET.get("city_code")
    city_name = request.GET.get("city_name")

    queryset = Boundary.objects.all()

    if city_code:
        queryset = queryset.filter(city_code=city_code)
    elif city_name:
        queryset = queryset.filter(city_name=city_name)

    data = (
        queryset.values_list(
            "barangay_name",
            "barangay_code",
        )
        .distinct()
        .order_by("barangay_name")
    )

    return JsonResponse(list(data), safe=False)
