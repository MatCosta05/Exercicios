from . import views
from django.urls import path

app_main = "main"

urlpatterns = [
    path("", views.homepage, name="homepage"),
]