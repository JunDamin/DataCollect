from datetime import datetime
from django import forms
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django_countries.fields import CountryField
from . import models
from users import models as user_models


class PersonnelReportCreateForm(forms.ModelForm):
    class Meta:
        model = models.PersonnelReport
        fields = ("report_date", "country")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            delete_url = reverse_lazy(
                "personnel:delete", kwargs={"pk": self.instance.pk}
            )


class PersonnelInfoCreateForm(forms.ModelForm):
    class Meta:
        model = models.PersonnelInfo
        exclude = ()


class SearchForm(forms.ModelForm):
    class Meta:
        model = models.PersonnelReport
        fields = (
            "department",
            "country",
            "report_date",
        )

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
