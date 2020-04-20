from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.go_to_home, name="home"),
]
