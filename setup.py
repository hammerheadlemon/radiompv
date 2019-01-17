#!/usr/bin/env python3

from setuptools import setup, find_packages
import os


def read(*names):
    values = dict()
    extensions = ['.txt', '.rst']
    for name in names:
        value = ''
        for extension in extensions:
            filename = name + extension
            if os.path.isfile(filename):
                value = open(name + extension).read()
                break
        values[name] = value
    return values


long_description = """
%(README)s

News
====

%(CHANGES)s

""" % read('README', 'CHANGES')

setup(
    name='radiompv',
    version="0.1",
    description='mpv wrapped in python - play a few BBC radio stations',
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Other Audience",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords='radio',
    author='Matthew Lemon',
    author_email='matt@matthewlemon.com',
    maintainer='Matthew Lemon',
    maintainer_email='matt@matthewlemon.com',
    url='https://github.com/hammerheadlemon/radiompv',
    license='GPLv3',
    packages=find_packages(),
    python_requires='>=3.6',
    entry_points={'console_scripts': [
        'radiompv = radiompv.radiompv:main',
    ]},
    install_requires=['requests == 2.21.0', 'beautifulsoup4 == 4.7.1', 'halo == 0.0.22'],
)
