from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from django import forms
from .models import Schedule, Activity


from django.forms import BaseFormSet
from django.forms import formset_factory

class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ['name']

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        exclude=['schedule']




