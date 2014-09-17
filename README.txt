crunchbase
==========

This is a Python Library for the Crunchbase 2.0 API.

API Documentation
=================

The CrunchBase API provides a RESTful interface to the data found on
CrunchBase. The response is in JSON format.

Register
~~~~~~~~

Follow the steps below to start using the CrunchBase API:

-  `Sign Up`_
-  Login & `get API key`_
-  `Browse the documentation.`_

Setup
~~~~~

::

    pip install git+git://github.com/anglinb/python-crunchbase

Up & Running
~~~~~~~~~~~~

Import Crunchbase then intialize the Crunchbase object with your api
key.

::

    from crunchbase import CrunchBase
    cb = CrunchBase('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

Here is an example of searching for an organization.

::

    cb.getOrganizations('Dropbox', page='1', order=...)

This returns the result of an organization search query in JSON format.
The keyword arguments ``(page, order, ... )`` will be translated into
GET variables and passed along with the request. Check the documentation
to find which arguments are availible for which API endpoint.

Now you are ready to perform any of the following queries against the
Crunchbase 2.0 API

::

    getOrganizations(query) #This returns result of an organization search query in JSON format.

    getOrganization(path) #This returns result of an organization search query in JSON format.

    getPeople() #This returns result of people in JSON format.

    getPerson(path) #This returns result of a single person

    getProducts() This returns result of products in JSON format.

    ... 

Check crunchbase/crunchbase.py for a list of all the of the possible
functions. These methods are in order with the ones found in the
`Crunchbase API Documentation`_.

API Usage Terms
~~~~~~~~~~~~~~~

-  `General TOS`_
-  `License: CC-BY-NC (Creative Commons Attribution-NonCommercial
   License)`_

https://developer.crunchbase.com/

Library License
~~~~~~~~~~~~~~~

`WTFPL`_

.. _Sign Up: https://developer.crunchbase.com/signup
.. _get API key: https://developer.crunchbase.com/admin
.. _Browse the documentation.: https://developer.crunchbase.com/docs
.. _Crunchbase API Documentation: https://developer.crunchbase.com/docs
.. _General TOS: http://info.crunchbase.com/docs/terms-of-service/
.. _`License: CC-BY-NC (Creative Commons Attribution-NonCommercial License)`: http://creativecommons.org/licenses/by-nc/4.0/
.. _WTFPL: http://www.wtfpl.net/