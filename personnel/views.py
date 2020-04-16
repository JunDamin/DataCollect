from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View, UpdateView, CreateView
from django.views.generic.edit import FormView, ModelFormMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.db import transaction
from users import mixins as user_mixins
from . import models, forms
from data import models as data_models


class PersonnelReportCreateView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.PersonnelCreateForm
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
        personnel.latest_report = self.request.user.department
        personnel.save()
        return redirect(reverse("personnel:detail", kwargs={"pk": personnel.pk}))


class PersonnelReportDetailView(DetailView):
    model = models.PersonnelReport


class PersonnelReportEditView(UpdateView):
    model = models.PersonnelReport
    template_name = "personnel/personnel_edit.html"
    fields = (
        "report_date",
        "country",
        "koica",
        "koica_admin",
        "v_codi",
        "p_codi",
        "yp",
        "local_v",
        "local_p",
        "koica_v",
        "advisor",
        "kmco",
        "global_doctor",
        "etc_v",
        "project_koica",
        "project_etc",
        "description",
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


class PersonnelReportListView(ListView):
    model = data_models.Department
    ordering = "pk"
    context_object_name = "departments"
    template_name = "personnel/personnel_list.html"
