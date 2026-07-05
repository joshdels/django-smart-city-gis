from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home_view(request):
    context = {"user": request.user}

    return render(request, "index.html", context)

