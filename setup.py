#!/usr/bin/env python

from setuptools import setup

setup(
    name='turtle-trans',
    version='0.0.1',
    packages=('turtletrans',),
    tests_require=('pytest', 'pytest-flake8', 'pytest-isort', 'pytest-readme',
                   'flake8-print', 'flake8-todo', 'pep8-naming'),

    description="Localization of the standard turtle module.",
    long_description=open('README.rst').read(),
    author="Wojciech Ruszczewski",
    author_email="python@wr.waw.pl",
    url="http://github.org/wrwrwr/turtle-trans",
    license="MIT",
    classifiers=(
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Education",
        "Topic :: Education :: Computer Aided Instruction (CAI)",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.4",
    ),
)
