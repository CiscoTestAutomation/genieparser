"""show_lldp.py
   supported commands:
     *  show lldp
     *  show lldp entry [<WORD>|*]
     *  show lldp interface [<WORD>]
     *  show lldp neighbors detail
     *  show lldp traffic
"""

from genie.libs.parser.iosxe.show_lldp import ShowLldp as ShowLldp_iosxe,\
                                              ShowLldpEntry as ShowLldpEntry_iosxe,\
                                              ShowLldpNeighbors as ShowLldpNeighbors_iosxe,\
                                              ShowLldpNeighborsDetail as ShowLldpNeighborsDetail_iosxe,\
                                              ShowLldpTraffic as ShowLldpTraffic_iosxe,\
                                              ShowLldpInterface as ShowLldpInterface_iosxe


class ShowLldp(ShowLldp_iosxe):
    """Parser for show lldp"""
    pass

class ShowLldpEntry(ShowLldpEntry_iosxe):
    """Parser for show lldp entry [<WORD>|*]"""
    pass

class ShowLldpNeighbors(ShowLldpNeighbors_iosxe):
    '''Parser for show lldp neighbors'''
    pass

class ShowLldpNeighborsDetail(ShowLldpNeighborsDetail_iosxe):
    '''Parser for show lldp neighbors detail'''
    pass

class ShowLldpTraffic(ShowLldpTraffic_iosxe):
    """Parser for show lldp traffic"""
    pass

class ShowLldpInterface(ShowLldpInterface_iosxe):
    """Parser for show lldp interface [<WORD>]"""
    pass
