# -*- coding: utf-8 -*-

from django.db import models
from django import forms


class Room(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
    )

    house = models.ForeignKey(
        'house.House',
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.house}/{self.title}'


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
