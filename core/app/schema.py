# -*- coding: utf-8 -*-

import graphene
from house.schema import Query as HouseQuery


class Query(
    HouseQuery,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(
    query=Query,
)