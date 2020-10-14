# -*- coding: utf-8 -*-

import json

from graphene_django.utils.testing import GraphQLTestCase

from .helpers import random_title


class BaseModelAPITestCase(GraphQLTestCase):
    GRAPHQL_URL = '/api/'

    @classmethod
    def setUpClass(cls):
        super(BaseModelAPITestCase, cls).setUpClass()
        cls.abstract = True

        if hasattr(cls, 'Meta'):
            cls.model_form = cls.Meta.model_form

            cls.fields = cls.model_form().fields.items()
            cls.model_name = cls.model_form._meta.model.__name__
            cls.model_name_low = cls.model_name.lower()

            cls.create_mutation = cls.Meta.create_mutation
            cls.update_mutation = cls.Meta.update_mutation
            cls.delete_mutation = cls.Meta.delete_mutation

            cls.abstract = False

    def get_model_data_from_content(self, content, action):
        """
        Gets dict from reponse content.

        args:
            content (Dict): Response Content dictionary.
            action (String): Name of action

        returns data (Dict): Model data dict.
        """

        data = content['data']
        if action == 'Delete':
            return data[f'{self.model_name_low}{action}']
        return data[f'{self.model_name_low}{action}'][f'{self.model_name_low}']

    def create_model(self):
        """
        Creates model via create mutation;

        returns response (django.http.response.HttpResponse), input_data (Dict)
        """

        input_data = {}

        # Fill input data with random generation data
        for name, field in self.fields:
            input_data.update({name: random_title()})

        # Get response via query
        response = self.query(
            self.create_mutation,
            input_data=input_data,
        )

        return response, input_data

    def test_create(self):
        """ Test for model create """

        # Run if current class not abstract class
        if not self.abstract:
            # Try to create object
            response, input_data = self.create_model()
            # Check if response status is 200
            self.assertResponseNoErrors(response)

            # Load json from response content
            content = json.loads(response.content)
            # Get model fields data
            model_data = self.get_model_data_from_content(content, 'Create')

            # Check if every field has correct data
            for name, field in self.fields:
                self.assertEqual(input_data[name], model_data[name])

    def test_update(self):
        """ Test for model update """

        # Run if current class not abstract class
        if not self.abstract:
            # Try to create object
            response, input_data = self.create_model()

            # Load json from response content
            content = json.loads(response.content)
            # Get model fields data
            model_data = self.get_model_data_from_content(content, 'Create')

            # Get id for model update
            model_id = model_data['id']
            # Add id to input data_dict
            input_data.update({'id': model_id})

            # Update fields with random data
            for name, field in self.fields:
                input_data.update({name: random_title()})

            # Try to update model
            response = self.query(
                self.update_mutation,
                input_data=input_data,
            )
            # Check if response status is 200
            self.assertResponseNoErrors(response)

            # Load json from response content
            content = json.loads(response.content)
            # Get model fields data
            model_data = self.get_model_data_from_content(content, 'Update')

            # Check if all fields was updated
            for name, field in self.fields:
                self.assertEqual(input_data[name], model_data[name])

            # Check if id is correct
            self.assertEqual(input_data['id'], model_id)

    def test_delete(self):
        """ Test for model delete """

        # Run if current class not abstract class
        if not self.abstract:
            # Try to create object
            response, input_data = self.create_model()

            # Load json from response content
            content = json.loads(response.content)
            # Get model fields data
            model_data = self.get_model_data_from_content(content, 'Create')
            # Get id for model delete
            model_id = model_data['id']

            # Add id to input data_dict
            input_data = {'id': model_id}

            # Try to update model
            response = self.query(
                self.delete_mutation,
                input_data=input_data,
            )
            # Check if response status is 200
            self.assertResponseNoErrors(response)

            # Load json from response content
            content = json.loads(response.content)
            # Get model fields data
            model_data = self.get_model_data_from_content(content, 'Delete')

            # Check if model was deleted
            self.assertEqual(True, model_data['result'])
