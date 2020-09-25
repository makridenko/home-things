# -*- coding: utf-8 -*-

from django.forms import ModelForm

from house.models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
