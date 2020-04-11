from datetime import datetime
from django import forms
from django_countries.fields import CountryField
from . import models
from users import models as user_models


class PredictionCreateForm(forms.ModelForm):

    country = forms.ChoiceField(required=True)

    class Meta:
        model = models.Prediction
        fields = (
            "country",
            "report_date",
            "risk_type",
            "risk_level",
            "description",
            "action",
        )
        widgets = {
            "report_date": forms.DateInput(attrs={"placeholder": "YYYY-MM-DD"}),
            "description": forms.Textarea(attrs={"placeholder": "안전전망"}),
            "action": forms.Textarea(attrs={"placeholder": "조치사항"}),
        }

    def __init__(self, user, *args, **kwargs):
        # 인자를 받기 위해서는 view에서 get_from_kwargs를 정의하고 super를 통해서 user 값을 확보해야 한다.
        super(PredictionCreateForm, self).__init__(*args, **kwargs)
        if user.employment:
            country_choice = (
                user.employment.employment_detail.filter()
                .order_by("-created")[0]
                .countries.all()
            )
        else:
            country_choice = (None, None)
        self.fields["country"].choices = ((i.code, i.korean) for i in country_choice)
        self.fields["report_date"].initial = datetime.now()

    def save(self, *args, **kwargs):
        prediction = super().save(commit=False)
        return prediction


class SearchForm(forms.ModelForm):
    class Meta:
        model = models.Prediction
        fields = (
            "country",
            "risk_type",
            "risk_level",
            "description",
            "action",
        )

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
