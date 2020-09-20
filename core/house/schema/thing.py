# -*- coding: utf-8 -*-

import graphene
import django_filters
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from house.models import Thing, ThingForm
from utils.graphql import BaseMutationCreate


class ThingFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Thing
        fields = ['title']


class ThingNode(DjangoObjectType):
    class Meta:
        model = Thing
        interfaces = (
            relay.Node,
        )


class ThingCreate(BaseMutationCreate):
    class Meta:
        model_node = ThingNode
        model_form = ThingForm
        place = 'house.Place'


class Query(graphene.ObjectType):
    thing = relay.Node.Field(ThingNode)
    things = DjangoFilterConnectionField(
        ThingNode,
        filterset_class=ThingFilter,
    )


class Mutation(graphene.ObjectType):
    thing_create = ThingCreate.Field()
