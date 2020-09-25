# -*- coding: utf-8 -*-

from .BaseMutation import BaseMutation

from .helpers import CREATE


class BaseMutationCreate(BaseMutation):
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
        cls.action_name = CREATE

        # Call BaseMutation init method
        super(BaseMutationCreate, cls).__init_subclass_with_meta__(
            model_node=model_node,
            model_form=model_form,
            *args, 
            **kwargs,
        )
