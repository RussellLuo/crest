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

    # GET http://example.com/api
    api.get()

Get a resource within the API:

    users = api.users

    # GET http://example.com/api/users
    users.get()

    # GET http://example.com/api/users?name=russell
    users.get(params={'name': 'russell'})

    # POST http://example.com/api/users (payload: {"name": "russell"})
    users.post(json={'name': 'russell'})

    # GET http://example.com/api/users/1
    users[1].get()

    # PATCH http://example.com/api/users/1 (payload: {"name": "russell"})
    users[1].patch(json={'name': 'russell'})

Get a sub resource of `users`:

    operations = users[1].operations

    # GET http://example.com/api/users/1/operations
    operations.get()

    # GET http://example.com/api/users/1/operations/1
    operations[1].get()


Thanks
------

`Crest` is based on kennethreitz's [requests][1], and is inspired by adnam's [resources][2]. Thank you guys!


[1]: https://github.com/kennethreitz/requests
[2]: https://github.com/adnam/resources
