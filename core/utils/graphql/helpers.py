# -*- coding: utf-8 -*-


def to_snake_case(string):
    """
    Changes CamelCase -> camel_case

    args:
        string (String): string to change
    """
    return ''.join([
        '_'+char.lower() if char.isupper() else char for char in string
    ]).lstrip('_')


def to_camel_case(string):
    """
    Changes snake_case -> SnakeCase

    args:
        string (String): string to change
    """
    return string.split('_')[0] + ''.join((
        w.capitalize() for w in string.split('_')[1:]
    ))
