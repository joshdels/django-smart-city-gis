from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from apps.parcels.models import Parcel


@login_required
def map_dashboard(request):
    return render(request, "parcels-map.html")


@login_required
def parcel_detail(request, id):
    parcel = get_object_or_404(Parcel, id=id)
    context = {"parcel": parcel}

    return render(request, "parcel-detail.html", context)
