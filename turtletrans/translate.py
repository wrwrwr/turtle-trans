"""
Some common utilities.
"""
from turtle import Turtle


def turtle_subclass(name):
    """
    Creates a subclass of Turtle with the given name.
    """
    return type(name, (Turtle,), {})


def translate_methods(cls, translations):
    """
    Creates aliases for method names.
    """
    for method, aliases in translations.items():
        func = getattr(cls, method)
        for alias in aliases:
            setattr(cls, alias, func)
