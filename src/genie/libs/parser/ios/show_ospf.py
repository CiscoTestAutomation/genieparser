''' show_ospf.py

IOS parsers for the following show commands:
    * show ip ospf
    * show ip ospf interface
    * show ip ospf sham-links
    * show ip ospf virtual-links
    * show ip ospf neighbor detail
    * show ip ospf database router
    * show ip ospf database network
    * show ip ospf database summary
    * show ip ospf database external
    * show ip ospf database opaque-area
    * show ip ospf mpls ldp interface
    * show ip ospf mpls traffic-eng link
'''

# Python
import re

from netaddr import IPAddress, IPNetwork

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

from genie.libs.parser.iosxe.show_ospf import  ShowIpOspfInterface as ShowIpOspfInterface_iosxe,\
                                               ShowIpOspfDatabaseRouter as ShowIpOspfDatabaseRouter_iosxe,\
                                               ShowIpOspfDatabaseExternal as ShowIpOspfDatabaseExternal_iosxe,\
                                               ShowIpOspfDatabaseNetwork as ShowIpOspfDatabaseNetwork_iosxe,\
                                               ShowIpOspfDatabaseSummary as ShowIpOspfDatabaseSummary_iosxe,\
                                               ShowIpOspfDatabaseOpaqueArea as ShowIpOspfDatabaseOpaqueArea_iosxe,\
                                               ShowIpOspf as ShowIpOspf_iosxe,\
                                               ShowIpOspfMplsLdpInterface as ShowIpOspfMplsLdpInterface_iosxe,\
                                               ShowIpOspfMplsTrafficEngLink as ShowIpOspfMplsTrafficEngLink_iosxe,\
                                               ShowIpOspfNeighborDetail as ShowIpOspfNeighborDetail_iosxe,\
                                               ShowIpOspfVirtualLinks as ShowIpOspfVirtualLinks_iosxe,\
                                               ShowIpOspfShamLinks as ShowIpOspfShamLinks_iosxe


class ShowIpOspf(ShowIpOspf_iosxe):

    ''' Parser for "show ip ospf" '''
    pass

class ShowIpOspfInterface(ShowIpOspfInterface_iosxe):

    ''' Parser for "show ip ospf interface" '''
    pass

# ====================================
# Parser for 'show ip ospf sham-links'
# ====================================
class ShowIpOspfShamLinks(ShowIpOspfShamLinks_iosxe):

    ''' Parser for 'show ip ospf sham-links' '''
    pass

# =======================================
# Parser for 'show ip ospf virtual-links'
# =======================================
class ShowIpOspfVirtualLinks(ShowIpOspfVirtualLinks_iosxe):

    pass


class ShowIpOspfNeighborDetail(ShowIpOspfNeighborDetail_iosxe):

    ''' Parser for "show ip ospf neighbor detail" '''
    pass

class ShowIpOspfDatabaseRouter(ShowIpOspfDatabaseRouter_iosxe):

    ''' Parser for "show ip ospf database router" '''
    pass

class ShowIpOspfDatabaseExternal(ShowIpOspfDatabaseExternal_iosxe):

    ''' Parser for "show ip ospf database external" '''
    pass

class ShowIpOspfDatabaseNetwork(ShowIpOspfDatabaseNetwork_iosxe):

    ''' Parser for "show ip ospf database network" '''
    pass

class ShowIpOspfDatabaseSummary(ShowIpOspfDatabaseSummary_iosxe):

    ''' Parser for "show ip ospf database summary" '''
    pass


class ShowIpOspfDatabaseOpaqueArea(ShowIpOspfDatabaseOpaqueArea_iosxe):

    ''' Parser for "show ip ospf database opaque-area" '''
    pass


class ShowIpOspfMplsLdpInterface(ShowIpOspfMplsLdpInterface_iosxe):

    ''' Parser for "show ip ospf mpls ldp interface" '''
    pass


class ShowIpOspfMplsTrafficEngLink(ShowIpOspfMplsTrafficEngLink_iosxe):

    ''' Parser for "show ip ospf mpls traffic-eng link" '''
    pass
