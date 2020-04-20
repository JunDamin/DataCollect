from django.urls import path
from . import views

app_name = "prediction"

urlpatterns = [
    path("", views.PredictionListView.as_view(), name="list",),
    path("summary/", views.PredictionSummaryView.as_view(), name="summary",),
    path("create/", views.PredictionCreateView.as_view(), name="create"),
    path("<int:pk>", views.PredictionDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.predictionEditView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.delete_prediction, name="delete",),
    path("search", views.PredictionSearchView.as_view(), name="search",),
    path("graph", views.update_graph, name="update-graph",),
]
