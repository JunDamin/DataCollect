from django.urls import path
from data import views as data_views

app_name = "core"

urlpatterns = [
    path("", data_views.HomeView.as_view(), name="home"),
]
