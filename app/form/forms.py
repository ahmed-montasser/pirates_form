from django.forms import Form, ModelForm
from django import forms
from .models import FormApplierModel


class TimeSlotForm(Form):
    time = forms.TimeField(required=True, input_formats="%H:%M:%S")
    date = forms.DateField(required=True, input_formats="%Y-%m-%d")
    capacity = forms.IntegerField(min_value=1, required=True)


class ApplicantsForm(ModelForm):
    class Meta:
        model = FormApplierModel
        fields = [
            "first_name",
            "last_name",
            "email",
            "mobile_number",
            "first_preference",
            "second_preference",
            "is_interviewed",
        ]
