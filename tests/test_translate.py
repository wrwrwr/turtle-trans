from turtle import Turtle

from turtletrans.translate import translate_methods, turtle_subclass


class TranslateTests:
    def test_subclass(self):
        # A new subclass with the given name should be created.
        t = turtle_subclass('T')
        assert issubclass(t, Turtle) and t != Turtle
        assert t.__name__ == 'T'

    def test_methods(self):
        # We want the localized methods only on the subclass.
        t = type('T', (Turtle,), {})
        translate_methods(t, {'forward': ('f',)})
        assert hasattr(t, 'f') and not hasattr(Turtle, 'f')
        assert getattr(t, 'f') == getattr(Turtle, 'forward')
