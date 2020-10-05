# -*- coding: utf-8 -*-

from graphql_relay import from_global_id

from .helpers import DELETE
from .BaseMutation import BaseMutation


class BaseMutationDelete(BaseMutation):
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
        cls.action_name = DELETE

        # Call BaseMutation init method
        super(BaseMutationDelete, cls).__init_subclass_with_meta__(
            model_node=model_node,
            model_form=model_form,
            *args,
            **kwargs,
        )

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        instance = cls.model.objects.get(
            pk=from_global_id(input['id'])[1]
        )
        if instance:
            instance.delete()
            return cls(True, errors=[])
        else:
            raise Exception('Object does not exists!')
