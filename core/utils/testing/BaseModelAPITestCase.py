# -*- coding: utf-8 -*-

import json

from .helpers import random_title


class BaseModelAPITestCase:
    class Meta:
        abstract = True

    GRAPHQL_URL = '/api/'

    model_form = None

    create_mutation = None
    update_mutation = None
    delete_mutation = None

    def __init__(self, *args, **kwargs):
        self.model_form = kwargs.get('model_form', None)
        self.model = self.model_form._meta.model

        self.model_name = self.model.__name__
        self.model_name_low = self.model_name.lower()

        self.fields = self.model_form().fields

        self.create_mutation = kwargs.get('create_mutation', None)
        self.update_mutation = kwargs.get('update_mutation', None)
        self.delete_mutation = kwargs.get('delete_mutation', None)

        self.assertResponseNoErrors = kwargs.get('assertResponseNoErrors', None)

    def get_model_data_from_content(self, content, action):
        data = content['data']
        return data[f'{self.model_name_low}{action}'][f'{self.model_name_low}']

    def test_create(self):
        input_data = {}
        for name, field in self.fields:
            input_data.update({name: random_title()})
        
        response = self.query(
            self.create_mutation, 
            input_data=input_data
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        model_data = self.get_model_data_from_content(content, 'Create')

        for name, field in self.fields:
            self.assertEqual(input_data[name], model_data[name])

    def test_update(self):
        pass

    def test_delete(self):
        pass