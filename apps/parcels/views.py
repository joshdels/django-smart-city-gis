from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Parcels, Owner, Boundary


@login_required
def home_view(request):
    context = {"user": request.user}

    return render(request, "index.html", context)
