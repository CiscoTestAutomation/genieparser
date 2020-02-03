"""show_l2route.py

show l2route topology
show l2route evpn mac all
show l2route evpn mac-ip all

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

        for line in out.splitlines():
            line = line.strip()

            result = p.match(line)

            if result:
                group_dict = result.groupdict()
                single_dict = AutoTree()

                str_type = group_dict['topo_type']
                if str_type is None:
                    str_type = 'N/A'

                single_dict[group_dict['topo_id']
                            ]['topo_name'][group_dict['topo_name']]['topo_type'] = str_type

                parsed_dict.setdefault('topo_id', {}).update(single_dict)

            continue

        return parsed_dict


class ShowL2routeEvpnMacAllSchema(MetaParser):
    """Schema for:
        * 'show l2route evpn mac all'
    """
    schema = {
        'topo_id': {
            Any(): {
                'mac_address': {
                    Any(): {
                        'producer': str,
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
        # 0        0012.01ff.0001 L2VPN       172.16.2.89/100001/ME
        # 0        0012.01ff.0002 L2VPN       172.16.2.89/100001/ME
        # 0        0012.01ff.0003 L2VPN       172.16.2.89/100001/ME
        # 0        0012.01ff.0004 L2VPN       172.16.2.89/100001/ME
        # 0        0012.01ff.0005 L2VPN       172.16.2.89/100001/ME
        # 0        0012.01ff.0006 L2VPN       172.16.2.89/100001/ME

        p = re.compile(r'^(?P<topo_id>\d+) +'
                       r'(?P<mac_address>\S+) +'
                       r'(?P<producer>\S+) +'
                       r'(?P<next_hop>\S+)')

        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            result = p.match(line)

            if result:
                group_dict = result.groupdict()

                mac_address_dict_in = AutoTree()
                mac_address_dict_in[group_dict['mac_address']
                                    ]['producer'] = group_dict['producer']
                mac_address_dict_in[group_dict['mac_address']
                                    ]['next_hop'] = group_dict['next_hop']

                parsed_dict.setdefault(
                    'topo_id',
                    {}).setdefault(
                    group_dict['topo_id'],
                    {}).setdefault(
                    'mac_address',
                    {}).update(mac_address_dict_in)

                continue
        return parsed_dict


class ShowL2routeEvpnMacIpAllSchema(MetaParser):
    """Schema for:
        * 'show l2route evpn mac-ip all'
    """
    schema = {
        'topo_id': {
            Any(): {
                'mac_address': {
                    Any(): {
                        'ip_address': {
                            Any(): {
                                'producer': str,
                                'next_hop': str
                            }
                        }
                    }
                }
            }
        }
    }


class ShowL2routeEvpnMacIpAll(ShowL2routeEvpnMacIpAllSchema):
    """Parser class for show l2route evpn mac-ip all"""

    cli_command = 'show l2route evpn mac-ip all'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Topo ID  Mac Address    IP Address      Producer    Next Hop(s)
        # -------- -------------- --------------- ----------- -----------------
        # 0        0001.00ff.0307 10.1.0.250    LOCAL       N/A
        # 0        0001.00ff.0307 2001:db8::250   LOCAL       N/A
        # 0        0aaa.0bff.bbbb 10.1.0.3      LOCAL       N/A
        # 0        0aaa.0bff.bbbc 10.1.0.4      LOCAL       N/A
        # 0        fc00.00ff.0107 192.168.166.3   L2VPN  Bundle-Ether1.0
        # 0        fc00.00ff.0109 192.168.49.3    L2VPN  68101/I/ME

        p = re.compile(r'^(?P<topo_id>\d+) +'
                       r'(?P<mac_address>\S+) +'
                       r'(?P<ip_address>\S+) +'
                       r'(?P<producer>\S+) +'
                       r'(?P<next_hop>\S+)')

        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            result = p.match(line)

            if result:

                group_dict = result.groupdict()
                ip_address_dict_in = AutoTree()

                next_hop = group_dict['next_hop']
                if next_hop is None:
                    next_hop = 'N/A'

                ip_address_dict_in[group_dict['ip_address']
                                   ]['producer'] = group_dict['producer']
                ip_address_dict_in[group_dict['ip_address']
                                   ]['next_hop'] = next_hop

           

                parsed_dict.setdefault(
                    'topo_id',
                    {}).setdefault(
                    group_dict['topo_id'],
                    {}).setdefault(
                    'mac_address',
                    {}).setdefault(
                    group_dict['mac_address'],
                    {}).setdefault('ip_address', {}).update(ip_address_dict_in)
                continue

        return parsed_dict
