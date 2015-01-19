Crest
=====

A simple REST client for Python.


Installation
------------

Install `Crest` with `pip`:

    $ pip install python-crest

Install development version from `GitHub`:

    $ git clone https://github.com/RussellLuo/crest.git
    $ cd crest
    $ python setup.py install


Getting Started
---------------

Create an API resource:

    from crest import Resource
    api = Resource('http://example.com/api')
    api.get()
    # GET http://example.com/api

Create resources within the API:

    users = api.users
    users.get()
    # GET http://example.com/api/users
    users[1].get()
    # GET http://example.com/api/users/1

Create a sub resource of `users`:

    operations = users[1].operations
    operations.get()
    # GET http://example.com/api/users/1/operations
    operations[1].get()
    # GET http://example.com/api/users/1/operations/1


Thanks
------

`Crest` is based on kennethreitz's [requests][1], and inspired by adnam's [resources][2]. Thank you guys!


[1]: https://github.com/kennethreitz/requests
[2]: https://github.com/adnam/resources
