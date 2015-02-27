#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

description = 'A simple REST client for Python.'

install_requires = [
    'requests>=2.5.0',
],

setup(
    name='Python-Crest',
    version='0.1.6',
    author='RussellLuo',
    author_email='luopeng.he@gmail.com',
    maintainer='RussellLuo',
    maintainer_email='luopeng.he@gmail.com',
    keywords='REST, Python',
    description=description,
    long_description=description,
    license='MIT',
    packages=find_packages(),
    url='https://github.com/RussellLuo/crest',
    install_requires=install_requires,
)
