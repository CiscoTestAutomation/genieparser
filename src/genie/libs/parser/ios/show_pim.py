''' show_mcast.py

IOSXE parsers for the following show commands:

    * show ipv6 pim interface
    * show ipv6 pim vrf <WROD> interface 

'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


from genie.libs.parser.iosxe.show_pim import ShowIpPimInterface as ShowIpPimInterface_iosxe,\
                                             ShowIpPimBsrRouter as ShowIpPimBsrRouter_iosxe,\
                                             ShowIpPimRpMapping as ShowIpPimRpMapping_iosxe,\
                                             ShowIpPimInterfaceDetail as ShowIpPimInterfaceDetail_iosxe,\
                                             ShowIpPimInterfaceDf as ShowIpPimInterfaceDf_iosxe,\
                                             ShowPimNeighbor as ShowPimNeighbor_iosxe,\
                                             ShowIpPimNeighbor as ShowIpPimNeighbor_iosxe,\
                                             ShowIpv6PimInterface as ShowIpv6PimInterface_iosxe,\
                                             ShowIpv6PimNeighbor as ShowIpv6PimNeighbor_iosxe,\
                                             ShowIpv6PimNeighborDetail as ShowIpv6PimNeighborDetail_iosxe,\
                                             ShowIpv6PimBsrElection as ShowIpv6PimBsrElection_iosxe,\
                                             ShowIpv6PimBsrCandidateRp as ShowIpv6PimBsrCandidateRp_iosxe

class ShowIpv6PimInterface(ShowIpv6PimInterface_iosxe):
    """Parser for:
        show ipv6 pim interface
        show ipv6 pim vrf <vrf> interface"""
    pass

class ShowIpv6PimBsrElection(ShowIpv6PimBsrElection_iosxe):
    """Parser for:
        show ipv6 pim bsr election
        show ipv6 pim vrf <vrf> bsr election"""
    pass

class ShowIpv6PimBsrCandidateRp(ShowIpv6PimBsrCandidateRp_iosxe):
    """Parser for:
        show ipv6 pim bsr candidate-rp
        show ipv6 pim vrf <vrf> bsr candidate-rp"""
    pass

class ShowIpPimInterface(ShowIpPimInterface_iosxe):
    """Parser for:
            show ip pim interface
            show ip pim vrf <vrf> interface"""
    pass


class ShowIpPimBsrRouter(ShowIpPimBsrRouter_iosxe):
    '''Parser for:
        show ip pim bsr-router
        show ip pim vrf <vrf> bsr-router'''
    pass


class ShowIpPimRpMapping(ShowIpPimRpMapping_iosxe):
    ''' Parser for:
         show ip pim rp mapping
         show ip pim vrf <vrf_name> rp mapping'''
    pass


class ShowIpPimInterfaceDetail(ShowIpPimInterfaceDetail_iosxe):
    ''' Parser for:
        show ip pim Interface detail
        show ip pim vrf <vrf_name> interface detail'''
    pass

class ShowPimNeighbor(ShowPimNeighbor_iosxe):
    '''Parser for:
            show ip/ipv6 pim [vrf <WORD>] neighbor
            show ipv6 pim [vrf <word>] neighbor detail'''
    pass


class ShowIpPimNeighbor(ShowIpPimNeighbor_iosxe):
    '''Parser for show ip pim [vrf <WORD>] neighbor'''
    pass

# ==========================================================
#  parser for 'show ipv6 pim [vrf <WORD>] neighbor'
# ==========================================================
class ShowIpv6PimNeighbor(ShowIpv6PimNeighbor_iosxe):
    '''Parser for show ipv6 pim [vrf <WORD>] neighbor'''
    pass

# ==========================================================
#  parser for 'show ipv6 pim [vrf <WORD>] neighbor detail'
# ==========================================================
class ShowIpv6PimNeighborDetail(ShowIpv6PimNeighborDetail_iosxe):
    '''Parser for show ipv6 pim [vrf <WORD>] neighbor detail'''
    pass


class ShowIpPimInterfaceDf(ShowIpPimInterfaceDf_iosxe):
    '''Parser for show ip pim [vrf <WORD>] interface df'''

    pass
