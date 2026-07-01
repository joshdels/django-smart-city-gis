from datetime import timedelta

from django.shortcuts import redirect, render
from django.utils import timezone

from .models import Guest


def homepage(request):
    return render(request, "homepage.html")


def inquiry_page(request):
    return render(request, "inquiry.html")

def inquiry_form(request):
    return render(request, "form/contact.html")


def send_public_form(request):
    if request.method == "POST":
        email = request.POST["email"]

        cooldown = Guest.objects.filter(
            email=email,
            created_at__gte=timezone.now() - timedelta(hours=24),
        ).exists()

        if cooldown:
            return render(
                request,
                "form/contact.html",
                {"error": "You have already submitted an inquiry within the last 24 hours"},
            )

        Guest.objects.create(
            organization=request.POST.get("organization") or "Individual",
            name=request.POST["name"],
            email=email,
            inquiry=request.POST["inquiry"],
            phone=request.POST["phone"],
        )

        return render(request, "form/contact_success.html", {"email": email})

