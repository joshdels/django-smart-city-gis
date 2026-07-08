from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def map_dashboard(request):
    return render(request, "parcel-map.html")
