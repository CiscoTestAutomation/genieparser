"""  show_mpls.py
   supported commands:
        *  show mpls ldp neighbor
        *  show mpls ldp neighbor vrf <vrf>
        *  show mpls ldp neighbor detail
        *  show mpls ldp neighbor vrf <vrf> detail
        *  show mpls ldp bindings
        *  show mpls ldp bindings all
        *  show mpls ldp bindings all detail
        *  show mpls ldp capabilities
        *  show mpls ldp capabilities all
        *  show mpls ldp discovery
        *  show mpls ldp discovery detail
        *  show mpls ldp discovery all
        *  show mpls ldp discovery all detail
        *  show mpls ldp discovery vrf <vrf>
        *  show mpls ldp discovery vrf <vrf> detail
        *  show mpls ldp igp sync
        *  show mpls ldp igp sync all
        *  show mpls ldp igp sync interface <interface>
        *  show mpls ldp igp sync vrf <vrf>
        *  show mpls ldp statistics
       	*  show mpls ldp parameters
       	*  show mpls forwarding-table
        *  show mpls forwarding-table detail
        *  show mpls forwarding-table vrf <vrf>
        *  show mpls forwarding-table vrf <vrf> detail
        *  show mpls interfaces
        *  show mpls interfaces <interface>
        *  show mpls interfaces <interface> detail
        *  show mpls interfaces detail
        *  show mpls l2transport vc detail
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional
from genie.libs.parser.utils.common import Common

# import iosxe parser
from genie.libs.parser.iosxe.show_mpls import ShowMplsLdpParameters as ShowMplsLdpParameters_iosxe,\
                                              ShowMplsLdpNsrStatistics as ShowMplsLdpNsrStatistics_iosxe,\
                                              ShowMplsLdpNeighbor as ShowMplsLdpNeighbor_iosxe,\
                                              ShowMplsLdpNeighborDetail as ShowMplsLdpNeighborDetail_iosxe,\
                                              ShowMplsLdpBindings as ShowMplsLdpBindings_iosxe,\
                                              ShowMplsLdpCapabilities as ShowMplsLdpCapabilities_iosxe,\
                                              ShowMplsLdpDiscovery as ShowMplsLdpDiscovery_iosxe,\
                                              ShowMplsLdpIgpSync as ShowMplsLdpIgpSync_iosxe,\
                                              ShowMplsForwardingTable as ShowMplsForwardingTable_iosxe,\
                                              ShowMplsInterface as ShowMplsInterface_iosxe,\
                                              ShowMplsL2TransportDetail as ShowMplsL2TransportDetail_iosxe, \
                                              ShowMplsL2TransportVC as ShowMplsL2TransportVC_iosxe


class ShowMplsLdpParameters(ShowMplsLdpParameters_iosxe):
    """Parser for show mpls ldp parameters"""
    pass


class ShowMplsLdpNsrStatistics(ShowMplsLdpNsrStatistics_iosxe):
    """Parser for show mpls ldp nsr statistics"""
    pass


class ShowMplsLdpNeighbor(ShowMplsLdpNeighbor_iosxe):
    """Parser for 
        show mpls ldp neighbor,
        show mpls ldp neighbor vrf <vrf>"""
    pass


class ShowMplsLdpNeighborDetail(ShowMplsLdpNeighborDetail_iosxe):
    """Parser for 
        show mpls ldp neighbor detail,
        show mpls ldp neighbor vrf <vrf> detail"""
    pass


class ShowMplsLdpBindings(ShowMplsLdpBindings_iosxe):
    """Parser for 
        show mpls ldp bindings
        show mpls ldp bindings vrf <vrf>
        show mpls ldp bindings all
        show mpls ldp bindings all detail
    """
    pass


class ShowMplsLdpCapabilities(ShowMplsLdpCapabilities_iosxe):
    """Parser for 
        show mpls ldp capabilities
        show mpls ldp capabilities all
    """
    pass


class ShowMplsLdpDiscovery(ShowMplsLdpDiscovery_iosxe):
    """Parser for 
        show mpls ldp discovery
        show mpls ldp discovery all
        show mpls ldp discovery all detail
        show mpls ldp discovery detail
        show mpls ldp discovery vrf <vrf>
        show mpls ldp discovery vrf <vrf> detail
    """
    pass


class ShowMplsLdpIgpSync(ShowMplsLdpIgpSync_iosxe):
    """Parser for 
        show mpls ldp igp sync
        show mpls ldp igp sync all
        show mpls ldp igp sync interface <interface>
        show mpls ldp igp sync vrf <vrf>
    """
    pass


class ShowMplsForwardingTable(ShowMplsForwardingTable_iosxe):
    """Parser for
        show mpls forwarding-table
        show mpls forwarding-table detail
        show mpls forwarding-table vrf <vrf>
        show mpls forwarding-table vrf <vrf> detail"""
    pass


class ShowMplsInterface(ShowMplsInterface_iosxe):
    """Parser for
        show mpls interfaces
        show mpls interfaces all
        show mpls interfaces vrf <vrf>
        show mpls interfaces <interface>
        show mpls interfaces <interface> detail
        show mpls interfaces detail"""
    pass


# ================================================
#   Show mpls l2transport vc detail
# ================================================
class ShowMplsL2TransportDetail(ShowMplsL2TransportDetail_iosxe):
    """
    Parser for show mpls l2transport vc detail
    """
    pass

# ================================================
#   Show mpls l2transport vc
# ================================================
class ShowMplsL2TransportVC(ShowMplsL2TransportVC_iosxe):
    """
    Parser for show mpls l2transport vc
    """
    pass