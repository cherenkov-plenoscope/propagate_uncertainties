Propagate Uncertainties
=======================
|BlackStyle|

Propagate the uncertainties of your variables in simple expressions.

Example, division
-----------------
.. code:: python

    import propagate_uncertainties as pu

    pu.divide(x=5.0, x_au=1.0, y=2.0, y_au=0.1)
    (2.5, 0.5153882032022076)


.. |BlackStyle| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black