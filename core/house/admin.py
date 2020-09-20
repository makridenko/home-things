# -*- coding: utf-8 -*-

from django.contrib import admin

from house.models import (
    House,
    Room,
    Place,
    Thing,
)


admin.site.register(House)
admin.site.register(Room)
admin.site.register(Place)
admin.site.register(Thing)
