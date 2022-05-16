Propagate Uncertainties
=======================
|BlackStyle|

Propagate the uncertainties of your variables in simple expressions.
Both value and absolute uncertainty of a variable are stored in a ``tuple()``.

.. code:: python

    C_value = 42.0
    C_absolute_uncertainty = 1.337
    C = tuple(C_value, C_absolute_uncertainty)


Example, division
-----------------
.. code:: python

    import propagate_uncertainties as pru

    pru.divide(x=(5.0, 1.0), y=(2.0, 0.1))
    (2.5, 0.5153882032022076)


.. |BlackStyle| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black