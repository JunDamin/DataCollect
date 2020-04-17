import pandas as pd
from django.http import Http404
from django.views.generic import ListView, DetailView, View, UpdateView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django_countries import countries
from users import mixins as user_mixins
from data import models as data_models
from . import models, forms
from data import plotly_graph as plot


class PredictionCreateView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.PredictionCreateForm
    template_name = "prediction/prediction_create.html"

    def get_form_kwargs(self):
        kwargs = super(PredictionCreateView, self).get_form_kwargs()
        user = self.request.user
        kwargs["user"] = user
        return kwargs

    def form_valid(self, form):
        prediction = form.save()
        prediction.author = self.request.user
        prediction.department = self.request.user.department
        try:
            print(self.request.user.department.latest_prediction)
            self.request.user.department.latest_prediction.latest_prediction_id = None
            self.request.user.department.latest_prediction.save()
        except ObjectDoesNotExist:
            pass
        prediction.latest_prediction = self.request.user.department
        prediction.save()
        return redirect(reverse("prediction:detail", kwargs={"pk": prediction.pk}))


class PredictionDetailView(DetailView):
    model = models.Prediction


class predictionEditView(UpdateView):
    model = models.Prediction
    template_name = "prediction/prediction_edit.html"
    fields = ("country", "risk_type", "risk_level", "description", "action")

    def get_object(self, queryset=None):
        prediction = super().get_object(queryset=queryset)
        if prediction.author.pk != self.request.user.pk:
            raise Http404()

        return prediction


@login_required
def delete_prediction(request, pk):
    user = request.user
    try:
        prediction = models.Prediction.objects.get(pk=pk)
        if prediction.author.pk != user.pk:
            messages.error(request, "Can't delete that prediction")
        else:
            models.Prediction.objects.filter(pk=pk).delete()
            messages.success(request, "Prediction Deleted")
        return redirect((reverse("core:home")))
    except models.Prediction.DoesNotExist:
        return redirect((reverse("core:home")))


class PredictionSearchView(View):
    def get(self, request):

        form = forms.SearchForm(request.GET)

        if form.is_valid():

            country = form.cleaned_data.get("country")
            risk_type = form.cleaned_data.get("risk_type")
            risk_level = form.cleaned_data.get("risk_level")
            description = form.cleaned_data.get("description")
            action = form.cleaned_data.get("action")

            filter_args = {}

            if description:
                filter_args["description__contains"] = description

            if action:
                filter_args["action__contains"] = action

            if country:
                filter_args["country"] = country

            if risk_type:
                filter_args["risk_type"] = risk_type

            if risk_level:
                filter_args["risk_level"] = risk_level

            qs = models.Prediction.objects.filter(**filter_args).order_by("-created")

            paginator = Paginator(qs, 10, orphans=5)

            page = request.GET.get("page", 1)

            prediction = paginator.get_page(page)

            return render(
                request,
                "prediction/search.html",
                {"form": form, "prediction": prediction},
            )

        else:

            form = forms.SearchForm()

            return render(request, "prediction/search.html", {"form": form})


class PredictionListView(ListView):
    model = data_models.Department
    ordering = "pk"
    context_object_name = "departments"
    template_name = "prediction/prediction_list.html"

    def get_data_frame(self):

        # read query
        df = pd.DataFrame(
            list(
                data_models.Department.objects.exclude(
                    latest_prediction__id=None
                ).values_list(
                    "latest_prediction__country__code",
                    "latest_prediction__country__korean",
                    "latest_prediction__risk_type__name",
                    "latest_prediction__risk_level__name",
                )
            ),
            columns=["code", "country", "risk_type", "risk_level"],
        )
        # data processing
        df["location_situation"] = df["risk_type"] + " | " + df["country"]
        df["location_code"] = df["code"].apply(countries.alpha3)
        return df

    def get_context_data(self, **kwargs):
        context = super(PredictionListView, self).get_context_data(**kwargs)
        df = self.get_data_frame()
        context["plot"] = plot.plot_prediction(df)
        context["df"] = df.to_html()
        return context
