# -*- coding: utf-8 -*-

import json

from graphene_django.utils.testing import GraphQLTestCase

from utils.testing.helpers import random_title
from utils.testing import BaseModelAPITestCase

from house.forms import HouseForm


CREATE_MUTATION = '''
mutation houseCreate($input: HouseCreateInput!) {
    houseCreate(input: $input) {
        house {
            id
            title
        }
    }
}
'''

UPDATE_MUTATION = '''
mutation houseUpdate($input: HouseUpdateInput!) {
    houseUpdate(input: $input) {
        house {
            id
            title
        }
    }
}
'''

DELETE_MUTATION = '''
mutation houseDelete($input: HouseDeleteInput!) {
    houseDelete(input: $input) {
        result
    }
}
'''
