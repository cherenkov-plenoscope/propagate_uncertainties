Propagate Uncertainties
=======================
|BlackStyle|

Propagate the uncertainties of your variables in simple expressions.


Example, division
-----------------
.. code:: python

    import propagate_uncertainties as pru

    pru.divide(x=(5.0, 1.0), y=(2.0, 0.1))
    (2.5, 0.5153882032022076)


.. |BlackStyle| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black