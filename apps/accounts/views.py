from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model

User = get_user_model()


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("map_dashboard")

        return render(request, "login.html", {"error": "Invalid credentails"})

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(
                request, "register.html", {"error": "Username already exists"}
            )

        user = User.objects.create_user(username=username, password=password)

        login(request, user)
        return redirect("map_dashboard")

    return render(request, "register.html")
