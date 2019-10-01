"""show_l2route.py

show l2route topology
show l2route evpn mac all

"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class AutoTree(dict):
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value


class ShowL2routeTopologySchema(MetaParser):
    """Schema for:
        * 'show l2route topology'
    """
    schema = {
        Any(): {
            Any(): {
                'topo_name': {
                    Any(): {
                        Optional('topo_type'): str
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

        p = re.compile(r'^(?P<topo_id>\d+) +'
                       r'(?P<topo_name>\S+) +'
                       r'(?P<topo_type>\S+)')

        parsed_dict = {}
        counts = 0

        for line in out.splitlines():
            line = line.strip()

            result = p.match(line)

            if result:
                counts += 1
                group_dict = result.groupdict()
                single_dict = AutoTree()

                str_type = group_dict['topo_type']

                if str_type is None:
                    str_type = 'N/A'

                single_dict['topo_id %d' % counts][group_dict['topo_id']
                                                   ]['topo_name'][group_dict['topo_name']]['topo_type'] = str_type

                parsed_dict.update(single_dict)

            continue

        return parsed_dict


class ShowL2routeEvpnMacAllSchema(MetaParser):
    """Schema for:
        * 'show l2route evpn all'
    """
    schema = {
        Any(): {
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


class ShowL2routeEvpnMacAll(ShowL2routeEvpnMacAllSchema):
    """Parser class for show l2route evpn mac all"""

    cli_command = 'show l2route evpn mac all'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Topo ID  Mac Address    Producer    Next Hop(s)
        # -------- -------------- ----------- ---------------------------------
        # 0        0012.0100.0001 L2VPN       172.16.2.89/100001/ME
        # 0        0012.0100.0002 L2VPN       172.16.2.89/100001/ME
        # 0        0012.0100.0003 L2VPN       172.16.2.89/100001/ME
        # 0        0012.0100.0004 L2VPN       172.16.2.89/100001/ME
        # 0        0012.0100.0005 L2VPN       172.16.2.89/100001/ME
        # 0        0012.0100.0006 L2VPN       172.16.2.89/100001/ME

        p = re.compile(r'^(?P<topo_id>\d+) +'
                       r'(?P<mac_addr>\S+) +'
                       r'(?P<edt_producer>\S+) +'
                       r'(?P<next_hop>\S+)')

        parsed_dict = {}
        counts = 0

        for line in out.splitlines():
            line = line.strip()

            result = p.match(line)

            if result:
                counts += 1
                group_dict = result.groupdict()
                single_dict = AutoTree()

                single_dict['topo_id %d' % counts][group_dict['topo_id']
                                                   ]['mac_addr'][group_dict['mac_addr']]['edt_producer'] = group_dict['edt_producer']

                single_dict['topo_id %d' % counts][group_dict['topo_id']
                                                   ]['mac_addr'][group_dict['mac_addr']]['next_hop'] = group_dict['next_hop']

                parsed_dict.update(single_dict)

                continue
        return parsed_dict
