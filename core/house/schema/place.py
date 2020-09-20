# -*- coding: utf-8 -*-

import graphene
import django_filters
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from house.models import Place, PlaceForm
from utils.graphql import BaseMutationCreate


class PlaceFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Place
        fields = ['title']


class PlaceNode(DjangoObjectType):
    class Meta:
        model = Place
        interfaces = (
            relay.Node,
        )


class PlaceCreate(BaseMutationCreate):
    class Meta:
        model_node = PlaceNode
        model_form = PlaceForm
        room = 'house.Room'


class Query(graphene.ObjectType):
    place = relay.Node.Field(PlaceNode)
    places = DjangoFilterConnectionField(
        PlaceNode,
        filterset_class=PlaceFilter,
    )


class Mutation(graphene.ObjectType):
    place_create = PlaceCreate.Field()
