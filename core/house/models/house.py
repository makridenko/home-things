# -*- coding: utf-8 -*-

from django.db import models


class House(models.Model):
    title = models.CharField(
        max_length=100,
        null=False
    )

    def __str__(self):
        return self.title
