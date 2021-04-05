#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
from os import path
import sys

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Manjesh N",
    author_email='manjesh_n@hotmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="Used to paginate REST API Calls / Mostly on MultiThreaded API Calls",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='paginateit',
    name='paginateit',
    src_dir=path.abspath(path.dirname(__file__)),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/manjesh23/paginateit',
    version='0.0.1',
    zip_safe=False,
)

if sys.argv[1].lower().strip() == 'make':  # exec Makefile commands
    import pymake
    fpath = path.join(src_dir, 'Makefile')
    pymake.main(['-f', fpath] + sys.argv[2:])
    # Stop to avoid setup.py raising non-standard command error
    sys.exit(0)
setup(use_scm_version=True)
