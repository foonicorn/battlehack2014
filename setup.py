#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup


# TODO: Create proper readme and history
readme = ''
history = ''

setup(
    name='battlehack',
    version='0.1.0',
    description='',
    long_description=readme + '\n\n' + history,
    author='Battle Hack 2014',
    author_email='',
    url='https://gitlab.moccu.com/moccu/battlehack-2014',
    packages=find_packages('src', exclude=['tests']),
    package_dir={'': 'src'},
    include_package_data=True,
    tests_require=[],
    install_requires=[],
    dependency_links=[],
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)