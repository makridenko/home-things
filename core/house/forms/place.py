# -*- coding: utf-8 -*-

from django.forms import ModelForm

from house.models import Place


class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = '__all__'
