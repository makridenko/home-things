# -*- coding: utf-8 -*-

import json

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


class HouseTestCase(BaseModelAPITestCase):
    class Meta:
        model_form = HouseForm
        create_mutation = CREATE_MUTATION
        update_mutation = UPDATE_MUTATION
        delete_mutation = DELETE_MUTATION
