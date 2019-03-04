"""
IOS Parsers
"""
# genieparser
from genie.libs.parser.iosxe.show_vlan import ShowVlan as ShowVlan_iosxe, \
                                              ShowVlanMtu as ShowVlanMtu_iosxe,\
                                              ShowVlanAccessMap as ShowVlanAccessMap_iosxe,\
                                              ShowVlanRemoteSpan as ShowVlanRemoteSpan_iosxe,\
                                              ShowVlanFilter as ShowVlanFilter_iosxe


class ShowVlan(ShowVlan_iosxe):
    pass

class ShowVlanMtu(ShowVlanMtu_iosxe):
   pass


class ShowVlanAccessMap(ShowVlanAccessMap_iosxe):
    pass


class ShowVlanRemoteSpan(ShowVlanRemoteSpan_iosxe):
    pass

class ShowVlanFilter(ShowVlanFilter_iosxe):
    pass