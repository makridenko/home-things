# -*- coding: utf-8 -*-

import graphene

from .house import Query as HouseQuery
from .house import Mutation as HouseMutation

from .room import Query as RoomQuery
from .room import Mutation as RoomMutation

from .place import Query as PlaceQuery
from .place import Mutation as PlaceMutation

from .thing import Query as ThingQuery
from .thing import Mutation as ThingMutation


class Query(
    HouseQuery,
    RoomQuery,
    PlaceQuery,
    ThingQuery,
    graphene.ObjectType,
):
    pass


class Mutation(
    HouseMutation,
    RoomMutation,
    PlaceMutation,
    ThingMutation,
    graphene.ObjectType,
):
    pass
