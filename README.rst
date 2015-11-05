============
turtle-trans
============

Partial translation of the standard `turtle` module. For those that would like
to learn some programming before English.

Just a few methods are translated at the moment. Feel free to add more
translations and languages.

Examples
========

.. code:: python

    >>> from turtletrans.es import Tortuga

    >>> t = Tortuga()
    >>> t.adelante(100)
    >>> t.derecho(90)
    >>> t.haciaatrás(40)
    >>> t.izquierda(10)

.. code:: python

    >>> from turtletrans.pl import Żółw

    >>> ż = Żółw()
    >>> ż.naprzód(30)
    >>> ż.prawo(90)
    >>> ż.wstecz(40)
    >>> ż.lewo(10)

.. comment (not yet):

    Installation
    ============

    .. code:: bash

        pip install turtle-trans

Requires a recent version of Python (> 3).
