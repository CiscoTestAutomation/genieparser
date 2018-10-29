#! /bin/env python

'''Setup file for Libs

See:
    https://packaging.python.org/en/latest/distributing.html
'''

import os
import re
import sys

from setuptools import setup, find_packages

_INTERNAL_SUPPORT = 'asg-genie-support@cisco.com'
_EXTERNAL_SUPPORT = 'pyats-support-ext@cisco.com'

_INTERNAL_LICENSE = 'Cisco Systems, Inc. Cisco Confidential',
_EXTERNAL_LICENSE = 'Apache 2.0'

_INTERNAL_URL = 'http://wwwin-genie.cisco.com/'
_EXTERNAL_URL = 'https://developer.cisco.com/site/pyats/'

DEVNET_CMDLINE_OPT = '--devnet'
devnet = False
if DEVNET_CMDLINE_OPT in sys.argv:
    # avoiding argparse complexity :o
    sys.argv.remove(DEVNET_CMDLINE_OPT)
    devnet = True

# pyats support mailer
SUPPORT = _EXTERNAL_SUPPORT if devnet else _INTERNAL_SUPPORT

# license statement
LICENSE = _EXTERNAL_LICENSE if devnet else _INTERNAL_LICENSE

# project url
URL = _EXTERNAL_URL if devnet else _INTERNAL_URL

def read(*paths):
    '''read and return txt content of file'''
    with open(os.path.join(*paths)) as fp:
        return fp.read()

def find_version(*paths):
    '''reads a file and returns the defined __version__ value'''
    version_match = re.search(r"^__version__ ?= ?['\"]([^'\"]*)['\"]",
                              read(*paths), re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

def build_version_range(version):
    '''
    for any given version, return the major.minor version requirement range
    eg: for version '3.4.7', return '>=3.4.0, <3.5.0'
    '''
    req_ver = version.split('.')
    version_range = '>= %s.%s.0, < %s.%s.0' % \
        (req_ver[0], req_ver[1], req_ver[0], int(req_ver[1])+1)

    return version_range

def version_info(*paths):
    '''returns the result of find_version() and build_version_range() tuple'''

    version = find_version(*paths)
    return version, build_version_range(version)

# compute version range
version, version_range = version_info('src', 'genie', 'libs', 'parser', '__init__.py')

# generate package dependencies
install_requires = ['xmltodict']


# launch setup
setup(
    name = 'genie.libs.parser',
    version = version,

    # descriptions
    description = 'Genie libs Parser: Genie Parser Libraries',
    long_description = read('DESCRIPTION.rst'),

    # the project's main homepage.
    url = URL,

    # author details
    author = 'Cisco Systems Inc.',
    author_email = SUPPORT,

    # project licensing
    license = LICENSE,

    # see https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Telecommunications Industry',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    # project keywords
    keywords = 'genie pyats test automation',

    # uses namespace package
    namespace_packages = ['genie', 'genie.libs'],

    # project packages
    packages = find_packages(where = 'src'),

    # project directory
    package_dir = {
        '': 'src',
    },

    # additional package data files that goes into the package itself
    package_data = {
    },

    # console entry point
    entry_points = {
    },

    # package dependencies
    install_requires = install_requires,

    # any additional groups of dependencies.
    # install using: $ pip install -e .[dev]
    extras_require = {
        'dev': ['coverage',
                'restview',
                'Sphinx',
                'sphinxcontrib-napoleon',
                'sphinx-rtd-theme'],
    },

    # external modules
    ext_modules = [],

    # any data files placed outside this package.
    # See: http://docs.python.org/3.4/distutils/setupscript.html
    # format:
    #   [('target', ['list', 'of', 'files'])]
    # where target is sys.prefix/<target>
    data_files = [],

    # non zip-safe (never tested it)
    zip_safe = False,
)
