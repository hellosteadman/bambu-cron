#!/usr/bin/env python
from setuptools import setup
from os import path

setup(
    name = 'bambu-cron',
    version = '2.0',
    description = 'A simple scheduling system that lets you define jobs that get performed at various intervals. Use a virtual "poor man\'s cron" or a single Django management command to run the jobs.',
    author = 'Steadman',
    author_email = 'mark@steadman.io',
    url = 'https://github.com/iamsteadman/bambu-cron',
    long_description = open(path.join(path.dirname(__file__), 'README')).read(),
    install_requires = ['Django>=1.4'],
    packages = [
        'bambu_cron',
        'bambu_cron.migrations',
        'bambu_cron.management',
        'bambu_cron.management.commands'
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django'
    ]
)