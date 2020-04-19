from django.urls import path
from . import views

app_name = "prediction"

urlpatterns = [
    path("summary/", views.PredictionSummaryView.as_view(), name="summary",),
    path("create/", views.PredictionCreateView.as_view(), name="create"),
    path("<int:pk>", views.PredictionDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.predictionEditView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.delete_prediction, name="delete",),
    path("search", views.PredictionSearchView.as_view(), name="search",),
]
