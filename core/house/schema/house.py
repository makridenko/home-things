# -*- coding: utf-8 -*-

import graphene
import django_filters
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from house.models import House


class HouseFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = House
        fields = ['title']


class HouseNode(DjangoObjectType):
    class Meta:
        model = House
        interfaces = (
            relay.Node,
        )


class Query(graphene.ObjectType):
    house = relay.Node.Field(HouseNode)
    houses = DjangoFilterConnectionField(
        HouseNode,
        filterset_class=HouseFilter,
    )
