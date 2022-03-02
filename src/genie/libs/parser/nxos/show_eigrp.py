''' show_eigrp.py
NXOS parsers for the following commands
    * 'show ip eigrp neighbors vrf <vrf>'
    * 'show ipv6 eigrp neighbors vrf <vrf>'
    * 'show ip eigrp neighbors detail vrf <vrf>'
    * 'show ipv6 eigrp neighbors detail vrf <vrf>'
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# Libs
from genie.libs.parser.utils.common import Common


class ShowEigrpNeighborsSchema(MetaParser):
    '''Schema for:
        * 'show ip eigrp neighbors vrf <vrf>'
        * 'show ipv6 eigrp neighbors vrf <vrf>'
    '''

    schema = {
        'eigrp_instance': {
            Any(): {
                'vrf': {
                    Any(): {
                        'address_family': {
                            Any(): {
                                'eigrp_interface': {
                                    Any(): {
                                        'eigrp_nbr': {
                                            Any(): {
                                                'peer_handle': int,
                                                'hold': int,
                                                'uptime': str,
                                                'q_cnt': int,
                                                'last_seq_number': int,
                                                'srtt': float,
                                                'rto': int, }, },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            }


class ShowEigrpNeighborsSuperParser(ShowEigrpNeighborsSchema):
    '''Super parser for:
        * 'show ip eigrp neighbors vrf <vrf>'
        * 'show ipv6 eigrp neighbors vrf <vrf>'
    '''

    def cli(self, vrf='', output=None):

        # IP-EIGRP neighbors for process 100 VRF default
        # IP-EIGRP neighbors for process 100 VRF VRF1
        # IPv6-EIGRP neighbors for process 100 VRF default
        # IPv6-EIGRP neighbors for process 100 VRF VRF1
        r1 = re.compile(r'^(?P<address_family>IP|IPv4|IPv6)'
                        '\-EIGRP\s+neighbors\s*for\s*process \s*'
                        '(?P<as_num>\d+)\s*VRF\s*(?P<vrf>\S+)$')

        # 1   10.13.90.1              Eth1/2.90       13   01:56:49  1    50    0   16
        # 0   10.23.90.2              Eth1/1.90       11   01:46:12  15   90    0   22
        # 0   fe80::f816:3eff:fecf:5a5b               Eth1/1.90       12   01:40:09  10   60    0   30
        # 1   fe80::f816:3eff:fe62:65af               Eth1/2.90       12   01:40:07  4    50    0   22
        r2 = re.compile(r'^(?P<peer_handle>\d+) +'
                        '(?P<nbr_address>\S+) +'
                        '(?P<eigrp_interface>[A-Za-z]+\s*[\d\/\.]+) +'
                        '(?P<hold>\d+) +(?P<uptime>\S+) +'
                        '(?P<srtt>\d+) +'
                        '(?P<rto>\d+) +'
                        '(?P<q_cnt>\d+) +'
                        '(?P<last_seq_number>\d+)$')

        parsed_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # IP-EIGRP neighbors for process 100 VRF default
            # IP-EIGRP neighbors for process 100 VRF VRF1
            # IPv6-EIGRP neighbors for process 100 VRF default
            # IPv6-EIGRP neighbors for process 100 VRF VRF1
            result = r1.match(line)

            if result:
                group = result.groupdict()

                address_family = group['address_family'].lower()
                if address_family == 'ip':
                    address_family = 'ipv4'

                eigrp_instance = group['as_num']
                vrf = group['vrf']
                continue

            # 1   10.13.90.1              Eth1/2.90       13   01:56:49  1    50    0   16
            # 0   10.23.90.2              Eth1/1.90       11   01:46:12  15   90    0   22
            # 0   fe80::f816:3eff:fecf:5a5b               Eth1/1.90       12   01:40:09  10   60    0   30
            # 1   fe80::f816:3eff:fe62:65af               Eth1/2.90       12   01:40:07  4    50    0   22
            result = r2.match(line)
            if result:

                group = result.groupdict()

                if not vrf:
                    vrf = 'default'

                if not eigrp_instance:
                    eigrp_instance = ''

                eigrp_interface = Common.convert_intf_name\
                    (intf=group['eigrp_interface'])

                nbr_address = group['nbr_address']

                ip_dict = parsed_dict\
                    .setdefault('eigrp_instance', {})\
                    .setdefault(eigrp_instance, {})\
                    .setdefault('vrf', {})\
                    .setdefault(vrf, {})\
                    .setdefault('address_family', {})\
                    .setdefault(address_family, {})\
                    .setdefault('eigrp_interface', {})\
                    .setdefault(eigrp_interface, {})\
                    .setdefault('eigrp_nbr', {}).setdefault(nbr_address, {})

                ip_dict['peer_handle'] = int(group['peer_handle'])
                ip_dict['hold'] = int(group['hold'])
                ip_dict['uptime'] = group['uptime']
                ip_dict['srtt'] = float(group['srtt'])/1000
                ip_dict['rto'] = int(group['rto'])
                ip_dict['q_cnt'] = int(group['q_cnt'])
                ip_dict['last_seq_number'] = int(group['last_seq_number'])
                continue

        return parsed_dict


class ShowIpv4EigrpNeighbors(ShowEigrpNeighborsSuperParser,
                             ShowEigrpNeighborsSchema):

    cli_command = 'show ip eigrp neighbors vrf {vrf}'

    def cli(self, vrf='all', output=None):
        if output is None:
            cmd = self.cli_command.format(vrf=vrf)

            show_output = self.device.execute(cmd)

        else:
            show_output = output

        return super().cli(output=show_output, vrf=vrf)


class ShowIpv6EigrpNeighbors(ShowEigrpNeighborsSuperParser,
                             ShowEigrpNeighborsSchema):

    cli_command = 'show ipv6 eigrp neighbors vrf {vrf}'

    def cli(self, vrf='all', output=None):
        if output is None:
            cmd = self.cli_command.format(vrf=vrf)

            show_output = self.device.execute(cmd)
        else:
            show_output = output

        return super().cli(output=show_output, vrf=vrf)


class ShowEigrpNeighborsDetailSchema(MetaParser):
    '''Schema for:
        * 'show ip eigrp neighbors detail vrf <vrf>'
        * 'show ipv6 eigrp neighbors detail vrf <vrf>'
    '''

    schema = {
        'eigrp_instance': {
            Any(): {
                'vrf': {
                    Any(): {
                        'address_family': {
                            Any(): {
                                'eigrp_interface': {
                                    Any(): {
                                        'eigrp_nbr': {
                                            Any(): {
                                                'retransmit_count': int,
                                                'retry_count': int,
                                                'last_seq_number': int,
                                                'srtt': float,
                                                'rto': int,
                                                'q_cnt': int,
                                                'peer_handle': int,
                                                'nbr_sw_ver': {
                                                    'os_majorver': int,
                                                    'os_minorver': int,
                                                    'tlv_majorrev': int,
                                                    'tlv_minorrev': int, },
                                                'hold': int,
                                                'uptime': str,
                                                'prefixes': int,
                                                'bfd_state': str, }, },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            }


class ShowEigrpNeighborsDetailSuperParser(ShowEigrpNeighborsDetailSchema):
    '''Super parser for:
        * 'show ip eigrp neighbors detail vrf <vrf>'
        * 'show ipv6 eigrp neighbors detail vrf <vrf>'
    '''

    def cli(self, vrf='', output=None):

        # IP-EIGRP neighbors for process 100 VRF default
        # IP-EIGRP neighbors for process 100 VRF VRF1
        # IPv6-EIGRP neighbors for process 100 VRF default
        # IPv6-EIGRP neighbors for process 100 VRF VRF1
        r1 = re.compile(r'^(?P<address_family>IP|IPv4|IPv6)'
                        '\-EIGRP\s+neighbors\s*for\s*process \s*'
                        '(?P<as_num>\d+)\s*VRF\s*(?P<vrf>\S+)$')

        # 1   10.13.90.1              Eth1/2.90       14   01:58:11  1    50    0   16
        # 0   10.23.90.2              Eth1/1.90       13   01:47:34  15   90    0   22
        # 0   fe80::f816:3eff:fecf:5a5b               Eth1/1.90       12   01:41:31  10   60    0   30
        # 0   fe80::f816:3eff:fecf:5a5b               Eth1/1.390      11   01:45:50  10   60    0   10
        r2 = re.compile(r'^(?P<peer_handle>\d+) +'
                        '(?P<nbr_address>\S+) +'
                        '(?P<eigrp_interface>[A-Za-z]+\s*[\d\/\.]+) +'
                        '(?P<hold>\d+) +(?P<uptime>\S+) +'
                        '(?P<srtt>\d+) +'
                        '(?P<rto>\d+) +'
                        '(?P<q_cnt>\d+) +'
                        '(?P<last_seq_number>\d+)$')

        # Version 3.3/2.0, Retrans: 1, Retries: 0, BFD state: N/A, Prefixes: 3
        # Version 3.3/2.0, Retrans: 1, Retries: 0, BFD state: N/A, Prefixes: 3
        # Version 23.0/2.0, Retrans: 1, Retries: 0, BFD state: N/A
        r3 = re.compile(r'Version\s*(?P<os_majorver>\d+)\.'
                        '(?P<os_minorver>\d+)\/(?P<tlv_majorrev>\d+)\.'
                        '(?P<tlv_minorrev>\d+), +Retrans\s*:\s*'
                        '(?P<retransmit_count>\d+)\, +Retries\s*:\s*'
                        '(?P<retry_count>\d+)\,* *BFD\s+state\:\s*'
                        '(?P<bfd_state>[\w\/]+)\,*\s*'
                        '(?:Prefixes\s*:\s*(?P<prefixes>\d+))?')

        parsed_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # IP-EIGRP neighbors for process 100 VRF default
            # IP-EIGRP neighbors for process 100 VRF VRF1
            # IPv6-EIGRP neighbors for process 100 VRF default
            # IPv6-EIGRP neighbors for process 100 VRF VRF1
            result = r1.match(line)

            if result:
                group = result.groupdict()

                address_family = group['address_family'].lower()
                if address_family == 'ip':
                    address_family = 'ipv4'
                eigrp_instance = group['as_num']
                vrf = group['vrf']
                continue

            # 1   10.13.90.1              Eth1/2.90       14   01:58:11  1    50    0   16
            # 0   10.23.90.2              Eth1/1.90       13   01:47:34  15   90    0   22
            # 0   fe80::f816:3eff:fecf:5a5b               Eth1/1.90       12   01:41:31  10   60    0   30
            # 0   fe80::f816:3eff:fecf:5a5b               Eth1/1.390      11   01:45:50  10   60    0   10
            result = r2.match(line)
            if result:

                group = result.groupdict()

                if not vrf:
                    vrf = 'default'

                if not eigrp_instance:
                    eigrp_instance = ''

                eigrp_interface = Common.convert_intf_name\
                    (intf=group['eigrp_interface'])

                nbr_address = group['nbr_address']

                ip_dict = parsed_dict\
                    .setdefault('eigrp_instance', {})\
                    .setdefault(eigrp_instance, {})\
                    .setdefault('vrf', {})\
                    .setdefault(vrf, {})\
                    .setdefault('address_family', {})\
                    .setdefault(address_family, {})\
                    .setdefault('eigrp_interface', {})\
                    .setdefault(eigrp_interface, {})\
                    .setdefault('eigrp_nbr', {}).setdefault(nbr_address, {})

                ip_dict['peer_handle'] = int(group['peer_handle'])
                ip_dict['hold'] = int(group['hold'])
                ip_dict['uptime'] = group['uptime']
                ip_dict['srtt'] = float(group['srtt'])/1000
                ip_dict['rto'] = int(group['rto'])
                ip_dict['q_cnt'] = int(group['q_cnt'])
                ip_dict['last_seq_number'] = int(group['last_seq_number'])

                continue

            # Version 3.3/2.0, Retrans: 1, Retries: 0, BFD state: N/A, Prefixes: 3
            # Version 3.3/2.0, Retrans: 1, Retries: 0, BFD state: N/A, Prefixes: 3
            # Version 23.0/2.0, Retrans: 1, Retries: 0, BFD state: N/A
            result = r3.match(line)

            if result:
                group = result.groupdict()

                sw_ver_dict = ip_dict.setdefault('nbr_sw_ver', {})

                # Version begin
                sw_ver_dict['os_majorver'] = int(group['os_majorver'])
                sw_ver_dict['os_minorver'] = int(group['os_minorver'])
                sw_ver_dict['tlv_majorrev'] = int(group['tlv_majorrev'])
                sw_ver_dict['tlv_minorrev'] = int(group['tlv_minorrev'])
                # Version end

                ip_dict['retransmit_count'] = \
                    int(group['retransmit_count'])
                ip_dict['retry_count'] = int(group['retry_count'])
                ip_dict['bfd_state'] = group['bfd_state']

                prefixes = group['prefixes']

                ip_dict['prefixes'] = int(prefixes) if prefixes else 0

                continue

        return parsed_dict


class ShowIpv4EigrpNeighborsDetail(ShowEigrpNeighborsDetailSuperParser,
                                   ShowEigrpNeighborsDetailSchema):

    cli_command = 'show ip eigrp neighbors detail vrf {vrf}'

    def cli(self, vrf='all', output=None):
        if output is None:            
            cmd = self.cli_command.format(vrf=vrf)
                
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        return super().cli(output=show_output, vrf=vrf)


class ShowIpv6EigrpNeighborsDetail(ShowEigrpNeighborsDetailSuperParser,
                                   ShowEigrpNeighborsDetailSchema):

    cli_command = 'show ipv6 eigrp neighbors detail vrf {vrf}'

    def cli(self, vrf='all', output=None):
        if output is None:
            cmd = self.cli_command.format(vrf=vrf)

            show_output = self.device.execute(cmd)
        else:
            show_output = output

        return super().cli(output=show_output, vrf=vrf)

class ShowEigrpTopologySchema(MetaParser):
    '''Schema for:
        * 'show ip eigrp topology'
        * 'show ipv6 eigrp topology'
        * 'show ip eigrp topology vrf <vrf>'
        * 'show ipv6 eigrp topology vrf <vrf>'
    '''

    schema = {
        'as': {
            int: {
                'routerid': str,
                'vrf': {
                    Any(): {
                        'address_family': {
                            Any(): {
                                'route': {
                                    Any(): {
                                        'state': str,
                                        'num_successors': int,
                                        'fd': str,
                                        'nexthops': {
                                            int: {
                                                'nexthop': str,
                                                Optional('fd'): int,
                                                Optional('rd'): int,
                                                Optional('interface'): str
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

class ShowEigrpTopologySuperParser(ShowEigrpTopologySchema):
    '''Super parser for:
        * 'show ip eigrp topology'
        * 'show ipv6 eigrp topology'
        * 'show ip eigrp topology vrf <vrf>'
        * 'show ipv6 eigrp topology vrf <vrf>'
    '''

    def cli(self, output=None):
        # IP-EIGRP Topology Table for AS(1)/ID(10.0.0.1) VRF default
        # IPv6-EIGRP Topology Table for AS(0)/ID(0.0.0.0) VRF vrf1
        r1 = re.compile(r'^(?P<address_family>IP|IPv4|IPv6)'
                        '\-EIGRP\s+Topology\s+Table\s+for\s+'
                        'AS\((?P<as_num>\d+)\)\/ID\((?P<routerid>\S+)\)'
                        '\s+VRF\s+(?P<vrf>\S+)$')

        # P 10.1.1.0/24, 1 successors, FD is 2816
        # P 2001:1::1:0/112, 1 successors, FD is 2816
        # P 10.4.1.0/24, 2 successors, FD is Inaccessible
        r2 = re.compile(r'^(?P<state>P|A|U|Q|R|r|s)\s+(?P<route>\S+),\s+'
                        '(?P<num_successors>\d+)\s+successors,'
                        '\s+FD\s+is\s+(?P<fd>(\d+)|Inaccessible)$')

        # via Connected, Ethernet1/2
        # via Rstatic (51200/0)
        # via 10.1.1.2 (3072/576), Ethernet1/2
        r3 = re.compile(r'via\s+(?P<nexthop>\S+)'
                        '(\s+\((?P<fd>\d+)\/(?P<rd>\d+)\))?'
                        '(,\s(?P<interface>\S+))?$')

        parsed_dict:dict = {}

        nexthop_count:int = 0

        # loop over all the lines
        for line in output.splitlines():
            line = line.strip()

            result = r1.match(line)
            if result:
                group:dict = result.groupdict()
                address_family = group['address_family'].lower()
                if address_family == 'ip':
                    address_family = 'ipv4'
                as_num = int(group['as_num'])
                routerid = group['routerid']
                vrf = group['vrf']
                as_dict:dict = parsed_dict \
                    .setdefault('as', {}) \
                    .setdefault(as_num, {})
                as_dict['routerid'] = routerid
                continue

            result = r2.match(line)
            if result:
                nexthop_count = 0
                group:dict = result.groupdict()

                if not vrf:
                    vrf = 'default'
                if not as_num:
                    as_num = 0
                if not routerid:
                    routerid = ''

                route:str = group['route']
                route_dict:dict = parsed_dict \
                    .setdefault('as', {}) \
                    .setdefault(as_num, {}) \
                    .setdefault('vrf', {}) \
                    .setdefault(vrf, {}) \
                    .setdefault('address_family', {}) \
                    .setdefault(address_family, {}) \
                    .setdefault('route', {}) \
                    .setdefault(route, {})
                route_dict['state'] = group['state']
                route_dict['num_successors'] = int(group['num_successors'])
                route_dict['fd'] = group['fd']

            result = r3.match(line)
            if result:
                group:dict = result.groupdict()
                nexthop_dict:dict = parsed_dict \
                    .setdefault('as', {}) \
                    .setdefault(as_num, {}) \
                    .setdefault('vrf', {}) \
                    .setdefault(vrf, {}) \
                    .setdefault('address_family', {}) \
                    .setdefault(address_family, {}) \
                    .setdefault('route', {}) \
                    .setdefault(route, {}) \
                    .setdefault('nexthops', {}) \
                    .setdefault(nexthop_count, {})
                nexthop_count = nexthop_count + 1
                nexthop_dict['nexthop'] = group['nexthop']
                for key in ('fd', 'rd') :
                    if group[key]:
                        nexthop_dict[key] = int(group[key])
                if group['interface']:
                    nexthop_dict['interface'] = group['interface']

        return parsed_dict

class ShowIpEigrpTopology(ShowEigrpTopologySuperParser, ShowEigrpTopologySchema):
    '''Parser for:
        * 'show ip eigrp topology'
        * 'show ip eigrp topology vrf <vrf>'
    '''

    cli_command = [
        'show ip eigrp topology'
        'show ip eigrp topology {vrf}'
    ]

    def cli(self, vrf=None, output=None):
        if output is None:
            if vrf is None:
                cmd = self.cli_command[0]
            else:
                cmd = self.cli_command[1].format(vrf=vrf)
            output = self.device.execute(cmd)

        return super().cli(output=output)

class ShowIpv6EigrpTopology(ShowEigrpTopologySuperParser, ShowEigrpTopologySchema):
    '''Parser for:
        * 'show ipv6 eigrp topology'
        * 'show ipv6 eigrp topology vrf <vrf>'
    '''

    cli_command = [
        'show ipv6 eigrp topology'
        'show ipv6 eigrp topology {vrf}'
    ]

    def cli(self, vrf=None, output=None):
        if output is None:
            if vrf is None:
                cmd = self.cli_command[0]
            else:
                cmd = self.cli_command[1].format(vrf=vrf)
            output = self.device.execute(cmd)

        return super().cli(output=output)
