# -*- coding: utf-8 -*-

from django.db import models
from django import forms


class House(models.Model):
    title = models.CharField(
        max_length=100,
        null=False
    )

    def __str__(self):
        return self.title


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = '__all__'
