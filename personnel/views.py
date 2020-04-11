from django.http import Http404
from django.views.generic import ListView, DetailView, View, UpdateView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from users import mixins as user_mixins
from . import models, forms


class PersonnelReportCreateView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.PersonnelReportCreateForm
    template_name = "personnel/personnel_create.html"

    def get_form_kwargs(self):
        kwargs = super(PersonnelReportCreateView, self).get_form_kwargs()
        user = self.request.user
        kwargs["user"] = user
        return kwargs

    def form_valid(self, form):
        personnel = form.save()
        personnel.author = self.request.user
        personnel.department = self.request.user.department
        personnel.save()
        return redirect(reverse("personnel:detail", kwargs={"pk": personnel.pk}))


class PersonnelReportDetailView(DetailView):
    model = models.PersonnelReport
    template_name = "personnel/personnel_detail.html"
    context_object_name = "personnel"


class PersonnelReportEditView(UpdateView):
    model = models.PersonnelReport
    template_name = "personnel/personnel_edit.html"
    fields = (
        "department",
        "country",
        "report_date",
    )

    def get_object(self, queryset=None):
        personnel = super().get_object(queryset=queryset)
        if personnel.author.pk != self.request.user.pk:
            raise Http404()

        return personnel


@login_required
def delete_personnel_report(request, pk):
    user = request.user
    try:
        personnel = models.PersonnelReport.objects.get(pk=pk)
        if personnel.author.pk != user.pk:
            messages.error(request, "Can't delete that personnel")
        else:
            models.PersonnelReport.objects.filter(pk=pk).delete()
            messages.success(request, "Personnel Report Deleted")
        return redirect((reverse("core:home")))
    except models.PersonnelReport.DoesNotExist:
        return redirect((reverse("core:home")))
