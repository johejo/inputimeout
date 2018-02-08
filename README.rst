inputimeout
===========

.. image:: https://img.shields.io/pypi/v/inputimeout.svg   :target: https://pypi.python.org/pypi/inputimeout
.. image:: https://img.shields.io/github/license/mashape/apistatus.svg   :target: https://raw.githubusercontent.com/johejo/inputimeout/master/LICENSE

Description
-----------

Multi platform standard input with timeout

Install
-------

.. code:: bash

    $ pip install inputimeout

Usage
-----

.. code:: python

    from inputimeout import inputimeout, TimeoutOccurred
    try:
        something = inputimeout(prompt='>>', timeout=5)
    except TimeoutOccurred:
        something = 'something'
    print(something)

License
-------

MIT
