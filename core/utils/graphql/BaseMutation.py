# -*- coding: utf-8 -*-

import graphene
from graphene import relay
from graphene_django.forms.converter import convert_form_field
from graphene_django.types import ErrorType

from django.forms.models import ModelChoiceField

from .helpers import to_camel_case, to_snake_case


class BaseMutation(relay.ClientIDMutation):
    class Meta:
        abstract = True

    @classmethod
    def __init_subclass_with_meta__(
        cls, 
        model_node=None, 
        model_form=None, 
        *args, 
        **kwargs,
    ):

        if not model_form:
            raise Exception('Model form is required!')

        if not model_node:
            raise Exception('Model node is required!')

        cls.model_form = model_form
        cls.model_node = model_node
        cls.model = model_node._meta.model
        cls.kwargs = kwargs
        model_input = {}

        for name, field in model_form().fields.items():
            # If field is FK - create obj
            if type(field) == ModelChoiceField:
                input_obj = type(
                    to_camel_case(f'{name}_input'),
                    (graphene.InputObjectType,),
                    {'id': graphene.ID(required=True)},
                )
                # Add obj as graphene field as Input class attr
                model_input[name] = graphene.Field(
                    input_obj, 
                    required=field.required,
                )
            else:
                model_input[name] = convert_form_field(field)
        
        # Create Input class
        cls.Input = type('Input', (object,), model_input)

        # Set attr for return
        setattr(
            cls, 
            to_snake_case(cls.model.__name__), 
            graphene.Field(cls.model_node),
        )

        # Set attr for errors
        setattr(cls, 'errors', graphene.List(ErrorType))

        # Call original init method
        super(BaseMutation, cls).__init_subclass_with_meta__(*args, **kwargs)