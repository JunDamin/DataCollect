from django.urls import path
from . import views

app_name = "personnel"


urlpatterns = [
    path("list/", views.PersonnelListView.as_view(), name="list",),
    path("create/", views.PersonnelReportFormsetView.as_view(), name="create"),
    path("<int:pk>", views.PersonnelReportDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.PersonnelReportEditView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.delete_personnel_report, name="delete",),
]
