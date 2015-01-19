#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


class Resource(object):

    def __init__(self, uri):
        self._uri = uri
        self._client = requests.api

    def __repr__(self):
        return '<Resource %s>' % self._uri

    def __unicode__(self):
        return self._uri

    __str__ = __unicode__

    def __getitem__(self, key):
        uri = self._uri.rstrip('/')
        return self.__class__('%s/%s' % (uri, key))

    __getattr__ = __getitem__

    def request(self, method, **kwargs):
        return self._client.request(method, self._uri, **kwargs)

    def get(self, **kwargs):
        return self.request('get', **kwargs)

    def post(self, **kwargs):
        return self.request('post', **kwargs)

    def put(self, **kwargs):
        return self.request('put', **kwargs)

    def patch(self, **kwargs):
        return self.request('patch', **kwargs)

    def delete(self, **kwargs):
        return self.request('delete', **kwargs)
