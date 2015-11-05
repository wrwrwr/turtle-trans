"""
Some common utilities.
"""


def translate_methods(cls, translations):
    """
    Creates aliases for method names.
    """
    for method, aliases in translations.items():
        func = getattr(cls, method)
        for alias in aliases:
            setattr(cls, alias, func)
