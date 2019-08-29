#!/usr/bin/env python
from setuptools import find_packages, setup


setup(
    name='digitalocean_omg',
    description='Digitalocean OMG wrapper',
    author='Asyncy',
    author_email='noreply@asyncy.com',
    license='MIT',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click>=7.0',
        'python-digitalocean>=1.14.0'
    ],
    entry_points="""
        [console_scripts]
        digitalocean_omg=digitalocean_omg.App:App.main
    """
)
