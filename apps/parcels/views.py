from django.shortcuts import render, get_object_or_404
from .models import Parcels, Owner, Boundary


def home_view(request):
    context = {"username": "Alex"}

    return render(request, "index.html", context)
