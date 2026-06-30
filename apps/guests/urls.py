from django.urls import path
from . import views

urlpatterns = [path("", views.send_public_form, name="send_public_form")]
