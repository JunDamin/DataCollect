from django.urls import path
from . import views

app_name = "personnel"


urlpatterns = [
    path("create/", views.PersonnelReportCreateView.as_view(), name="create"),
    path("<int:pk>", views.PersonnelReportDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.PersonnelReportEditView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.delete_personnel_report, name="delete",),
]
