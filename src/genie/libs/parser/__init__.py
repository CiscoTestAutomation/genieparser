'''
    Module:
        genie.libs.parser

    Description:
        This is the library sub-component of Genie for `genie.metaparser`.

'''

# metadata
__version__ = '21.12'
__author__ = 'Cisco Systems Inc.'
__contact__ = ['pyats-support@cisco.com', 'pyats-support-ext@cisco.com']
__copyright__ = 'Copyright (c) 2018, Cisco Systems Inc.'

from .base import tcl_invoke_ats_cmd,\
                  tcl_package_require_caas,\
                  tcl_package_require_caas_parsers,\
                  tcl_invoke_caas_abstract_parser,\
                  CaasMetaParser

from genie import abstract
abstract.declare_package(__name__)


