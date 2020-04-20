from django.urls import path
from . import views

app_name = "data"

urlpatterns = [
    path("my_department", views.get_my_departemnt, name="my-department",),
]
