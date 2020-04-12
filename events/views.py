from django.http import Http404
from django.views.generic import ListView, DetailView, View, UpdateView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from users import mixins as user_mixins
from . import models, forms


class EventCreateView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.EventCreateForm
    template_name = "events/event_create.html"

    def get_form_kwargs(self):
        kwargs = super(EventCreateView, self).get_form_kwargs()
        user = self.request.user
        kwargs["user"] = user
        return kwargs

    def form_valid(self, form):
        event = form.save()
        event.author = self.request.user
        event.department = self.request.user.department
        if event.is_single:
            event.end_date = event.start_date
        event.save()
        return redirect(reverse("events:detail", kwargs={"pk": event.pk}))


class EventDetailView(DetailView):
    model = models.Event


class EventEditView(UpdateView):
    model = models.Event
    template_name = "events/event_edit.html"
    fields = (
        "title",
        "country",
        "event_type",
        "start_date",
        "end_date",
        "description",
    )

    def get_object(self, queryset=None):
        event = super().get_object(queryset=queryset)
        if event.author.pk != self.request.user.pk:
            raise Http404()

        return event


@login_required
def delete_event(request, pk):
    user = request.user
    try:
        event = models.Event.objects.get(pk=pk)
        if event.author.pk != user.pk:
            messages.error(request, "Can't delete that Event")
        else:
            models.Event.objects.filter(pk=pk).delete()
            messages.success(request, "Event Deleted")
        return redirect((reverse("core:home")))
    except models.Event.DoesNotExist:
        return redirect((reverse("core:home")))


class EventListView(ListView):

    model = models.Event
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "events"


class EventSearchView(View):
    def get(self, request):

        form = forms.SearchForm(request.GET)

        if form.is_valid():

            title = form.cleaned_data.get("title")
            country = form.cleaned_data.get("country")
            event_type = form.cleaned_data.get("event_type")

            filter_args = {}

            if title:
                filter_args["title__contains"] = title

            if country:
                filter_args["country"] = country

            if event_type:
                filter_args["event_type"] = event_type

            qs = models.Event.objects.filter(**filter_args).order_by("-created")

            paginator = Paginator(qs, 10, orphans=5)

            page = request.GET.get("page", 1)

            event = paginator.get_page(page)

            return render(
                request, "events/search.html", {"form": form, "event": event},
            )

        else:

            form = forms.SearchForm()

            return render(request, "events/search.html", {"form": form})
