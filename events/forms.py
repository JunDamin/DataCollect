from datetime import datetime
from django import forms
from django_countries.fields import CountryField
from . import models
from users import models as user_models


class EventCreateForm(forms.ModelForm):

    country = forms.ChoiceField(required=True)

    class Meta:
        model = models.Event
        fields = (
            "title",
            "country",
            "event_type",
            "start_date",
            "end_date",
            "description",
        )
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "제목"}),
            "start_date": forms.DateInput(attrs={"placeholder": "YYYY-MM-DD"}),
            "end_date": forms.DateInput(attrs={"placeholder": "YYYY-MM-DD"}),
            "description": forms.Textarea(attrs={"placeholder": "세부내역"}),
        }

    def __init__(self, user, *args, **kwargs):
        # 인자를 받기 위해서는 view에서 get_from_kwargs를 정의하고 super를 통해서 user 값을 확보해야 한다.
        super(EventCreateForm, self).__init__(*args, **kwargs)
        if user.department:
            country_choice = (
                user.department.department_detail.filter()
                .order_by("-created")[0]
                .countries.all()
            )
        else:
            country_choice = (None, None)
        self.fields["country"].choices = ((i.code, i.korean) for i in country_choice)
        self.fields["start_date"].initial = datetime.now()
        self.fields["end_date"].initial = datetime.now()

    def save(self, *args, **kwargs):
        event = super().save(commit=False)
        return event


class SearchForm(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = (
            "title",
            "country",
            "event_type",
            "description",
        )

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
