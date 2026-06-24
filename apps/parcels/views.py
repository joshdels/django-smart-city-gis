from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
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
