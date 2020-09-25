# -*- coding: utf-8 -*-

from django.db import models


class Thing(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
    )

    place = models.ForeignKey(
        'house.Place',
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.place}/{self.title}'
