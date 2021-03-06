# -*- coding: utf-8 -*-

import graphene
import django_filters
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from house.models import House
from house.forms import HouseForm
from utils.graphql import (
    BaseMutationCreate, BaseMutationUpdate, BaseMutationDelete
)


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


class HouseCreate(BaseMutationCreate):
    class Meta:
        model_node = HouseNode
        model_form = HouseForm


class HouseUpdate(BaseMutationUpdate):
    class Meta:
        model_node = HouseNode
        model_form = HouseForm


class HouseDelete(BaseMutationDelete):
    class Meta:
        model_node = HouseNode


class Query(graphene.ObjectType):
    house = relay.Node.Field(HouseNode)
    houses = DjangoFilterConnectionField(
        HouseNode,
        filterset_class=HouseFilter,
    )


class Mutation(graphene.ObjectType):
    house_create = HouseCreate.Field()
    house_update = HouseUpdate.Field()
    house_delete = HouseDelete.Field()
