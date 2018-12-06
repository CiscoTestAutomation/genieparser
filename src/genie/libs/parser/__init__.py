'''
    Module:
        genie.libs.parser

    Description:
        This is the library sub-component of Genie for `genie.metaparser`.

'''

# metadata
__version__ = '3.1.9'
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


# try to record usage statistics
#  - only internal cisco users will have stats.CesMonitor module
#  - below code does nothing for DevNet users -  we DO NOT track usage stats
#    for PyPI/public/customer users
try:
    # new internal cisco-only pkg since devnet release
    from ats.cisco.stats import CesMonitor
except Exception:
    try:
        # legacy pyats version, stats was inside utils module
        from ats.utils.stats import CesMonitor
    except Exception:
        CesMonitor = None

finally:
    if CesMonitor is not None:
        # CesMonitor exists -> this is an internal cisco user
        CesMonitor(action = __name__, application='Genie').post()
        CesMonitor(action = __name__, application='pyATS Packages').post()
