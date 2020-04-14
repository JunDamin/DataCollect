from django.urls import path
from prediction import views as prediction_views

app_name = "core"

urlpatterns = [
    path("", prediction_views.PredictionListView.as_view(), name="home"),
]
