from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render

from .models import Parcels, Owner, Boundary


@login_required
def home_view(request):
    context = {"user": request.user}

    return render(request, "index.html", context)

