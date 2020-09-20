# -*- coding: utf-8 -*-

import graphene
import django_filters
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from house.models import Room


class RoomFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Room
        fields = ['title']


class RoomNode(DjangoObjectType):
    class Meta:
        model = Room
        interfaces = (
            relay.Node,
        )


class Query(graphene.ObjectType):
    room = relay.Node.Field(RoomNode)
    rooms = DjangoFilterConnectionField(
        RoomNode,
        filterset_class=RoomFilter,
    )
