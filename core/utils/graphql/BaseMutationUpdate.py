# -*- coding: utf-8 -*-

from .BaseMutation import BaseMutation

from .helpers import UPDATE


class BaseMutationUpdate(BaseMutation):
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
        cls.action_name = UPDATE

        # Call BaseMutation init method
        super(BaseMutationUpdate, cls).__init_subclass_with_meta__(
            model_node=model_node,
            model_form=model_form,
            *args,
            **kwargs,
        )
