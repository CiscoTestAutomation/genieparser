Genie Parser Component
======================

Genie is both a library framework and a test harness that facilitates rapid
development, encourage re-usable and simplify writing test automation. Genie bundled with
the modular architecture of pyATS framework accelerates and simplifies test
automation leveraging all the perks of the Python programming language in an
object-orienting fashion.

pyATS is an end-to-end testing ecosystem, specializing in data-driven and
reusable testing, and engineered to be suitable for Agile, rapid development
iterations. Extensible by design, pyATS enables developers start with small,
simple and linear test cases, and scale towards large, complex and asynchronous
test suites.

Genie was initially developed internally in Cisco, and is now available to the
general public starting early 2018 through `Cisco DevNet`_. Visit the Genie
home page at

    https://developer.cisco.com/site/pyats/

.. _Cisco DevNet: https://developer.cisco.com/


Parser Package
--------------

This is a sub-component of Genie that parse the device output into structured
datastructure.

Requirements
------------

Genie currently supports Python 3.4+ on Linux & Mac systems. Windows platforms
are not yet supported.

Quick Start
-----------

.. code-block:: console

    # install genie as a whole
    $ pip install genie.metaparser

    # to upgrade this package manually
    $ pip install --upgrade genie.libs.parser

    # to install alpha/beta versions, add --pre
    $ pip install --pre genie.libs.parser


For more information on setting up your Python development environment,
such as creating virtual environment and installing ``pip`` on your system, 
please refer to `Virtual Environment and Packages`_ in Python tutorials.

.. _Virtual Environment and Packages: https://docs.python.org/3/tutorial/venv.html
