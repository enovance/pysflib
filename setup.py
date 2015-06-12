#!/usr/bin/env python
#
# Copyright (C) 2014 eNovance SAS <licensing@enovance.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

try:
    import multiprocessing  # noqa
except:
    pass


INSTALL_REQUIRES = ['nose',
                    'mock',
                    'requests>=2.4.1',
                    'python-redmine',
                    'pyyaml',
                    'six',
                    'pygerrit>=0.2.9']


DEP_LINKS = []

VERSION = '0.1.1'

setup(
    name='pysflib',
    version=VERSION,
    description=('a python library to interact with '
                 'a software factory instance'),
    author='Software Factory',
    author_email='softwarefactory@enovance.com',
    install_requires=INSTALL_REQUIRES,
    dependency_links=DEP_LINKS,
    test_suite='nose.collector',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=['ez_setup']),
    url='http://softwarefactory.enovance.com/r/gitweb?p=pysflib.git;a=summary',
    download_url='https://github.com/enovance/pysflib/tarball/%s' % VERSION,
    keywords=['software factory', 'CI', 'continuous integration'],
)
