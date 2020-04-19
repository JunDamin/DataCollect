import pandas as pd
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
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.db import transaction
from django_countries import countries
from users import mixins as user_mixins
from . import models, forms
from data import models as data_models
from data import plotly_graph as plot
from personnel import models as personnel_models


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
        try:
            print(self.request.user.department.latest_report)
            self.request.user.department.latest_report.latest_report_id = None
            self.request.user.department.latest_report.save()
        except ObjectDoesNotExist:
            pass
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
    model = models.PersonnelReport
    ordering = "pk"
    context_object_name = "personnel_report"
    template_name = "personnel/personnel_list.html"
    paginate_by = 24
    paginate_orphans = 5
    ordering = ['-created']


class PersonnelReportSummaryView(ListView):
    model = data_models.Department
    ordering = "pk"
    context_object_name = "departments"
    template_name = "personnel/personnel_summary.html"

    def get_data_frame(self):

        # read query
        df = pd.DataFrame(
            list(
                data_models.Department.objects.exclude(
                    latest_report__id=None
                ).values_list(
                    "latest_report__country__code",
                    "latest_report__country__korean",
                    *[
                        "latest_report__" + i
                        for i in personnel_models.PersonnelReport.TOTAL_LIST
                    ]
                )
            ),
            columns=["code", "country"] + personnel_models.PersonnelReport.TOTAL_LIST,
        )
        # data processing
        df["total"] = df.sum(axis=1)
        df["location_code"] = df["code"].apply(countries.alpha3)
        return df

    def get_context_data(self, **kwargs):
        context = super(PersonnelReportSummaryView, self).get_context_data(**kwargs)
        df = self.get_data_frame()
        context["plot"] = plot.plot_personnel(df)
        context["df"] = df.to_html()
        return context
