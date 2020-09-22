# -*- coding: utf-8 -*-

import graphene
import django_filters
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from house.models import Room, RoomForm
from utils.graphql import BaseMutationCreate


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


class RoomCreate(BaseMutationCreate):
    class Meta:
        model_node = RoomNode
        model_form = RoomForm
        house = 'house.House'


class Query(graphene.ObjectType):
    room = relay.Node.Field(RoomNode)
    rooms = DjangoFilterConnectionField(
        RoomNode,
        filterset_class=RoomFilter,
    )


class Mutation(graphene.ObjectType):
    room_create = RoomCreate.Field()
