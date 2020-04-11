from datetime import datetime
from django import forms
from django_countries.fields import CountryField
from . import models
from users import models as user_models


class PersonnelReportCreateForm(forms.ModelForm):

    country = forms.ChoiceField(required=True)

    class Meta:
        model = models.PersonnelReport
        fields = (
            "country",
            "report_date",
        )
        widgets = {
            "report_date": forms.DateInput(attrs={"placeholder": "YYYY-MM-DD"}),
        }

    def __init__(self, user, *args, **kwargs):
        # 인자를 받기 위해서는 view에서 get_from_kwargs를 정의하고 super를 통해서 user 값을 확보해야 한다.
        super(PersonnelReportCreateForm, self).__init__(*args, **kwargs)
        if user.department:
            country_choice = (
                user.department.department_detail.filter()
                .order_by("-created")[0]
                .countries.all()
            )
            self.fields["country"].choices = (
                (i.code, i.korean) for i in country_choice
            )
        else:
            self.fields["country"].choices = (("None", "없음"),)
        self.fields["report_date"].initial = datetime.now()

    def save(self, *args, **kwargs):
        PersonnelReport = super().save(commit=False)
        return PersonnelReport


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
