from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path("list/", views.EventListView.as_view(), name="list",),
    path("create/", views.EventCreateView.as_view(), name="create"),
    path("<int:pk>", views.EventDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.EventEditView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.delete_event, name="delete",),
    path("search", views.EventSearchView.as_view(), name="search",),
]
