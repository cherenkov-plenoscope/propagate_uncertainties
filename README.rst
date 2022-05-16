Propagate Uncertainties
=======================
|BlackStyle|

Propagate the uncertainties of your variables in simple expressions.


Example, division
-----------------
.. code:: python

    import propagate_uncertainties as pru

    C, C_au = pru.divide(x(5.0, 0.3), y=(2.0, 1.0))


.. |BlackStyle| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black