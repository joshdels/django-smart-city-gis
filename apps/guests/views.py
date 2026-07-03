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
    if request.method != "POST":
        return redirect("inquiry")

    email = request.POST["email"]

    cooldown = Guest.objects.filter(
        email=email,
        created_at__gte=timezone.now() - timedelta(hours=24),
    ).exists()

    if cooldown:
        return render(
            request,
            "inquiry.html",
            {
                "error": "You have already submitted an inquiry within the last 24 hours.",
                "name": request.POST.get("name", ""),
                "organization": request.POST.get("organization", ""),
                "email": email,
                "phone": request.POST.get("phone", ""),
                "inquiry": request.POST.get("inquiry", ""),
            },
        )

    Guest.objects.create(
        organization=request.POST.get("organization") or "Individual",
        name=request.POST["name"],
        email=email,
        inquiry=request.POST["inquiry"],
        phone=request.POST["phone"],
    )

    request.session["submitted_email"] = email
    return redirect("inquiry_success")


def inquiry_success(request):
    email = request.session.pop("submitted_email", None)

    if not email:
        return redirect("inquiry")

    return render(
        request,
        "contact_success.html",
        {"email": email},
    )

# temp for testing
def test(request):
    return render(request, "404.html")