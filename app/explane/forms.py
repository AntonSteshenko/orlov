from django.forms import ModelForm
from django import forms
from .models import Explane

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class CreateExplaneForm(ModelForm):
    class Meta:
        model = Explane
        fields = ['employee', 'date', 'time_from', 'time_to', 'explane']
        widgets = {
            'date': DateInput(),
            'time_from': TimeInput(),
            'time_to': TimeInput(),
        }

   