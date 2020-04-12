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


class PersonnelReportListView(ListView):
    model = models.PersonnelReport


class PersonnelReportFormsetView(
    user_mixins.LoggedInOnlyView, ModelFormMixin, FormView
):
    form_class = forms.PersonnelReportCreateForm
    formset_class = inlineformset_factory(
        parent_model=models.PersonnelReport,
        model=models.PersonnelInfo,
        form=forms.PersonnelInfoCreateForm,
        extra=1,
        can_order=True,
        can_delete=True,
    )
    object = None
    template_name = "personnel/personnel_formset.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "formset" not in kwargs:
            context["formset"] = self.get_formset
        return context

    def get_formset(self, **kwargs):
        kwargs.update(instance=self.object)
        return self.formset_class(**kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        formset = self.get_formset(data=self.request.POST)
        if form.is_valid() and formset.is_valid():
            return self.form_formset_valid(form, formset)
        else:
            return self.form_formset_invalid(form, formset)

    def form_formset_valid(self, form, formset):
        formset.instance = self.object = form.save()
        formset.instance.department = self.request.user.department
        form.save()
        formset.save()
        return redirect(
            reverse_lazy("personnel:detail", kwargs={"pk": formset.instance.pk})
        )

    def form_formset_invalid(self, form, formset):
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )


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
