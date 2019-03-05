# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='idepend',
    version='0.1.0',
    description='idepend package for Python-Guide.org',
    long_description=readme,
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    url='https://github.com/henrykironde/idepend',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

