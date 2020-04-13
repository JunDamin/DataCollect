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

    def __init__(self, user, *args, **kwargs):
        super(PersonnelReportCreateForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            delete_url = reverse_lazy(
                "personnel:delete", kwargs={"pk": self.instance.pk}
            )
        self.fields["report_date"].initial = datetime.now()
        if user.department:
            country_choices = (
                user.department.department_detail.filter()
                .order_by("-created")[0]
                .countries.all()
            )
            self.fields["country"].choices = [
                (i.code, i.korean) for i in country_choices
            ]
        else:
            self.fields["country"].choices = (("None", "없음"),)


class PersonnelInfoCreateForm(forms.ModelForm):
    class Meta:
        model = models.PersonnelInfo
        fields = ("personnel_type", "number")


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
