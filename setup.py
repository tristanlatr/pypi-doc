#! /usr/bin/env python3
from setuptools import setup

setup(
    name                =   "pypi-doc",
    version             =   '0.1',
    description         =   "PyPI libraries doc with pydoctor",
    author              =   "Martin Fischer",
    maintainer          =   "Tristan Landes",
    packages            =   ['pypi_doc',],
    install_requires    =   [
        "pydoctor",
        "requests", 
        "toml", 
        "importlib_resources"
    ],
    python_requires=">=3.6",
    entry_points        =   {'console_scripts': ['pypi-doc = pypi_doc.build:main'],},
)
