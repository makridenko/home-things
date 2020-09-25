# -*- coding: utf-8 -*-

import graphene
from graphene import relay
from graphene_django.forms.converter import convert_form_field
from graphene_django.types import ErrorType
from graphql_relay import from_global_id

from django.apps import apps
from django.forms import modelform_factory
from django.forms.models import ModelChoiceField

from .helpers import (
    to_camel_case, to_snake_case, CREATE, UPDATE, DELETE, gen_fk_description
)


class BaseMutation(relay.ClientIDMutation):
    model_node = None
    model_form = None
    action_name = None

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

        if not model_form and cls.action_name != DELETE:
            raise Exception('Model form is required!')

        if not model_node:
            raise Exception('Model node is required!')

        cls.model_form = model_form
        cls.model_node = model_node
        cls.model = model_node._meta.model

        cls.kwargs = kwargs
        cls.ErrorType = ErrorType

        model_input = {}

        # In delete mutation needs only id of object
        if cls.action_name == DELETE:
            model_input['id'] = graphene.ID(required=True)
        else:
            for name, field in model_form().fields.items():
                # Update mutation need non required fields, 
                # except ID! (model pk)
                if cls.action_name == UPDATE:
                    field.required = False

                # If field is FK - create obj
                if type(field) == ModelChoiceField:
                    input_obj = type(
                        to_camel_case(f'{name}_{cls.action_name}_input'),
                        (graphene.InputObjectType,),
                        {'id': graphene.ID(
                            required=True,
                            description=gen_fk_description(field),
                        )},
                    )

                    # Add obj as graphene field as Input class attr
                    model_input[name] = graphene.Field(
                        input_obj, 
                        required=field.required,
                    )
                else:
                    model_input[name] = convert_form_field(field)
        
            if cls.action_name == UPDATE:
                model_input['id'] = graphene.ID(required=True)

        # Create Input class
        cls.Input = type('Input', (object,), model_input)

        # Set attr for return
        setattr(
            cls, 
            to_snake_case(cls.model.__name__), 
            graphene.Field(cls.model_node),
        )

        # Set attr for errors
        setattr(cls, 'errors', graphene.List(cls.ErrorType))

        # Call original init method
        super(BaseMutation, cls).__init_subclass_with_meta__(*args, **kwargs)

    @classmethod
    def get_form(cls, **input):
        instance = None
        model_form = cls.model_form

        for obj in input:
            # Need to get object from id
            if hasattr(input[obj], 'keys') and 'id' in input[obj].keys():
                # Get model from model form field via queryset
                fk_model = model_form().fields[obj].queryset.model
                # TODO: need to check ModelNode
                pk = from_global_id(input[obj]['id'])[1]
                input[obj] = fk_model.objects.get(pk=pk)
        
        # Need for object update
        if 'id' in input.keys():
            # Get model instance for update via form
            instance = cls.model.objects.get(
                pk=from_global_id(input[obj])[1]
            )
            # Remove model pk
            del input['id']

            # Generate new form for update
            model_form = modelform_factory(
                cls.model, 
                form=model_form, 
                fields=[field for field in input.keys()]
            )

        return model_form(**{'data': input}, instance=instance)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        form = cls.get_form(**input)

        if form.is_valid():
            instance = form.save()
            return cls(instance, errors=[])
        else:
            return cls(errors=cls.ErrorType.from_errors(form.errors), **{})
