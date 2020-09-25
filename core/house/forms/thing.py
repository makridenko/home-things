# -*- coding: utf-8 -*-

from django.forms import ModelForm

from house.models import Thing


class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = '__all__'
