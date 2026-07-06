from django.shortcuts import render


def map_dashboard(request):
    return render(request, "parcel-map.html")
