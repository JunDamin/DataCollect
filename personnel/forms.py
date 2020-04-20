from datetime import datetime
from django import forms
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django_countries.fields import CountryField
from . import models
from users import models as user_models


class PersonnelCreateForm(forms.ModelForm):
    class Meta:
        model = models.PersonnelReport
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
        widgets = {
            "report_date": forms.DateInput(attrs={"placeholder": "YYYY-MM-DD"}),
            "description": forms.Textarea(attrs={"placeholder": "참고사항"}),
        }

    def __init__(self, user, *args, **kwargs):
        # 인자를 받기 위해서는 view에서 get_from_kwargs를 정의하고 super를 통해서 user 값을 확보해야 한다.
        super(PersonnelCreateForm, self).__init__(*args, **kwargs)
        if user.department:
            country_choice = (
                user.department.department_detail.filter()
                .order_by("-created")[0]
                .countries.all()
            )
            self.fields["country"].choices = ((i.id, i.korean) for i in country_choice)
        else:
            country_choice = (None, None)
            self.fields["country"].choices = ((i.id, i.korean) for i in country_choice)
        self.fields["report_date"].initial = datetime.now()

    def save(self, *args, **kwargs):
        personnel = super().save(commit=False)
        return personnel


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
