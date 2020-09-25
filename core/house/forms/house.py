# -*- coding: utf-8 -*-

from django.forms import ModelForm

from house.models import House


class HouseForm(ModelForm):
    class Meta:
        model = House
        fields = '__all__'
