# -*- coding: utf-8 -*-

import graphene
from house.schema import Query as HouseQuery
from house.schema import Mutation as HouseMutation


class Query(
    HouseQuery,
    graphene.ObjectType
):
    pass


class Mutation(
    HouseMutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
)
