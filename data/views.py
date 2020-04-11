
from django.http import Http404
from django.views.generic import View, ListView
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from users import mixins as user_mixins
from . import models, forms

# Create your views here.


class HomeView(user_mixins.LoggedInOnlyView, ListView):

    model = models.Department
    context_object_name = "department"
