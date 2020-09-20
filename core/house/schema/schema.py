# -*- coding: utf-8 -*-

import graphene

from .house import Query as HouseQuery
from .room import Query as RoomQuery
from .place import Query as PlaceQuery
from .thing import Query as ThingQuery


class Query(
    HouseQuery,
    RoomQuery,
    PlaceQuery,
    ThingQuery,
    graphene.ObjectType,
):
    pass
