#!/usr/bin/env python3
from setuptools import setup

from bnf import __version__


def read_requirements(fh):
    return [line for line in fh.read().split('\n') if line != '']


with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as fh:
    requirements = read_requirements(fh)

with open('test_requirements.txt', 'r') as fh:
    test_requirements = read_requirements(fh)

setup(
    name='bnf',
    version=__version__,
    author='Nikita Boyarskikh',
    author_email='n02@ya.ru',
    url='https://github.com/Nikita-Boyarskikh/bnf',
    license='MIT',
    python_requires='>=3.5',
    long_description_content_type='text/markdown',
    description='Backus–Naur form parsing and analyzing python library',
    long_description=long_description,
    packages=['bnf'],
    install_requires=requirements,
    project_urls={
        'Issues': 'https://github.com/Nikita-Boyarskikh/bnf/issues/',
        'Documentation': 'https://github.com/Nikita-Boyarskikh/bnf/wiki',
        'Source Code': 'https://github.com/Nikita-Boyarskikh/bnf',
    },
    setup_requires=['pytest-runner>=4.0'],
    tests_require=test_requirements,
)
