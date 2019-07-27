# -*- coding: utf-8 -*-
"""setuptools mock for tox."""

from setuptools import find_packages
from setuptools import setup


setup(
    name='cco.plone5',
    version='1.0',
    description='Plone 5 configuration + extensions',
    long_description='',
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 5.2',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    ],
    keywords='Python Plone',
    author='cyberconcepts.org team',
    author_email='team@cyberconcepts.org',
    url='https://github.com/cyberconcepts/cco.plone5',
    license='GPL version 2',
    zip_safe=False,
    install_requires=[],
    extras_require={},
    entry_points="""""",
)
