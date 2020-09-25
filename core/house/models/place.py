# -*- coding: utf-8 -*-

from django.db import models


class Place(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
    )

    room = models.ForeignKey(
        'house.Room',
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.room}/{self.title}'
