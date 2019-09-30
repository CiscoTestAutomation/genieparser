"""show_l2route.py

show l2route parser class

"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowL2routeTopologySchema(MetaParser):
    """Schema for:
        * 'show l2route topology'
    """
    schema = {
        Any(): {
            'topo_id': {
                Any(): {
                    'topo_name': {
                        Any(): {
                            Optional('topo_type'): str
                        }
                    }
                }
            }
        }
    }


class ShowL2routeTopology(ShowL2routeTopologySchema):
    """Parser class for show l2route topology """

    cli_command = 'show l2route topology'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Topology ID   Topology Name    Type
        # -----------   -------------    ----
        # 51             bd2              L2VRF
        # 4294967294     GLOBAL           N/A
        # 4294967295     ALL              N/A

        p = re.compile(
            r'^\s*(?P<topo_id>\d+)\s* +'
            r'(?P<topo_name>\S+)\s* +'
            r'(?:N/A|(?P<topo_type>\S+))')

        parsed_dict = {}
        counts = 0

        for line in out.splitlines():
            line = line.rstrip()

            result = p.match(line)

            if result:
                counts += 1
                group_dict = result.groupdict()

                str_topology = 'topology %d' % counts
                str_id = group_dict['topo_id']
                str_name = group_dict['topo_name']
                str_type = group_dict['topo_type']

                if str_type is None:
                    str_type = 'N/A'

                id_dict = {}
                name_dict = {}
                type_dict = {}

                id_dict['topo_id'] = {}
                name_dict['topo_name'] = {}
                type_dict['topo_type'] = {}

                type_dict['topo_type'] = str_type
                name_dict['topo_name'].setdefault(str_name, type_dict)
                id_dict['topo_id'].setdefault(str_id, name_dict)

                parsed_dict.update({str_topology: id_dict})

                continue

        return parsed_dict



class ShowL2routeEvpnMacAllSchema(MetaParser):
    """Schema for:
        * 'show l2route evpn all'
    """
    schema = {
        Any(): {
            'topo_id': {
                Any(): {
                    'mac_addr': {
                        Any(): {
                            'edt_producer': str,
                            'next_hop': str
                        }
                    }
                }
            }
        }
    }

class ShowL2routeEvpnMacAll(ShowL2routeEvpnMacAllSchema):
    """Parser class for show l2route evpn mac all"""

    cli_command = 'show l2route evpn mac all'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Topo ID  Mac Address    Producer    Next Hop(s)
        # -------- -------------- ----------- ----------------------------------------
        # 0        0012.0100.0001 L2VPN       172.16.2.89/100001/ME
        # 0        0012.0100.0002 L2VPN       172.16.2.89/100001/ME
        # 0        0012.0100.0003 L2VPN       172.16.2.89/100001/ME
        # 0        0012.0100.0004 L2VPN       172.16.2.89/100001/ME
        # 0        0012.0100.0005 L2VPN       172.16.2.89/100001/ME
        # 0        0012.0100.0006 L2VPN       172.16.2.89/100001/ME

        p = re.compile(
            r'^\s*(?P<topo_id>\d+)\s* +'
            r'(?P<mac_addr>\S+)\s* +'
            r'(?P<edt_producer>\S+)\s* +'
            r'(?P<next_hop>\S+)')

        parsed_dict = {}
        counts = 0

        for line in out.splitlines():
            line = line.rstrip()

            result = p.match(line)

            if result:
                counts += 1
                group_dict = result.groupdict()

                str_id = group_dict['topo_id']
                str_mac = group_dict['mac_addr']
                str_producer = group_dict['edt_producer']
                str_next_hop = group_dict['next_hop']

                producer_hop_dict = {}
                mac_addr_dict = {}
                id_dict = {}

                mac_addr_dict['mac_addr'] = {}
                id_dict['topo_id'] = {}

                producer_hop_dict.update({'edt_producer': str_producer})
                producer_hop_dict.update({'next_hop': str_next_hop})
                mac_addr_dict['mac_addr'].setdefault(str_mac, producer_hop_dict)
                id_dict['topo_id'].setdefault(str_id, mac_addr_dict)

                parsed_dict.update({counts: id_dict})

                continue
        return parsed_dict