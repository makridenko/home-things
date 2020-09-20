# -*- coding: utf-8 -*-

from graphql_relay import from_global_id
from graphene_django.types import ErrorType

from django.apps import apps

from .BaseMutation import BaseMutation


class BaseMutationCreate(BaseMutation):
    class Meta:
        abstract = True

    @classmethod
    def get_form_data(cls, **data):
        for obj in data:
            # Need to get object from id
            if hasattr(data[obj], 'keys') and 'id' in data[obj].keys():
                try:
                    fk_model = apps.get_model(cls.kwargs[obj])
                except KeyError:
                    raise Exception(f'Please provide {obj} obj')

                pk = from_global_id(data[obj]['id'])[1]
                data[obj] = fk_model.objects.get(pk=pk)

        return cls.model_form(**{'data': data})

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        form = cls.get_form_data(**input)

        if form.is_valid():
            obj = form.save()
            return cls(obj, errors=[])
        else:
            return cls(errors=ErrorType.from_errors(form.errors), **{})
