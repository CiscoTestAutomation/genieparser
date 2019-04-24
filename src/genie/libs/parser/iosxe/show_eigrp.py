''' show_eigrp.py
IOSXE parsers for the following commands

    * 'show ip eigrp neighbors'
    * 'show ip eigrp vrf <vrf> neighbors'
    * 'show ipv6 eigrp neighbors'
    * 'show ipv6 eigrp vrf <vrf> neighbors'
    * 'show ip eigrp neighbors detail'
    * 'show ip eigrp vrf <vrf> neighbors detail'
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any

# Libs
from genie.libs.parser.utils.common import Common


class ShowEigrpNeighborsSchema(MetaParser):
    ''' Schema for:
        * 'show ip eigrp neighbors'
        * 'show ip eigrp vrf <vrf> neighbors'
        * 'show ipv6 eigrp neighbors'
        * 'show ipv6 eigrp vrf <vrf> neighbors
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


# ====================================
# Parser for 'show ip eigrp neighbors'
#            'show ip eigrp vrf <vrf> neighbors'
#            'show ipv6 eigrp neighbors'
#            'show ipv6 eigrp vrf <vrf> neighbors'
# ====================================
class ShowEigrpNeighborsSuperParser(ShowEigrpNeighborsSchema):

    def cli(self, address_family='', vrf='', output=None):

        # EIGRP-IPv4 Neighbors for AS(1100) VRF(VRF1)
        r1 = re.compile(r'^EIGRP\-(?P<address_family>IPv4|IPv6)\s'
            '*Neighbors\s*for \w+\(\s*(?P<as_num>\d+)\)\s*(?:VRF\((?P<vrf>\S+)\))?$')

        # H   Address      Interface  Hold  Uptime    SRTT   RTO    Q   Seq
        #                             (sec)           (ms)          Cnt Num
        # 0   10.1.1.2     Gi0/0      13    00:00:03  1996   5000   0   5
        # 2   10.1.1.9     Gi0/0      14    00:02:24  206    5000   0   5
        # 1   10.1.2.3     Gi0/1      11    00:20:39  2202   5000   0   5
        r2 = re.compile(r'^(?P<peer_handle>\d+) +'
                        '(?P<nbr_address>\S+) +'
                        '(?P<eigrp_interface>[A-Za-z]+\s*[\d\/]+) +'
                        '(?P<hold>\d+) +(?P<uptime>\S+) +'
                        '(?P<srtt>\d+) +'
                        '(?P<rto>\d+) +'
                        '(?P<q_cnt>\d+) +'
                        '(?P<last_seq_number>\d+)$')

        parsed_dict = {}
        eigrp_instance = ''

        # Get output
        out = output

        for line in out.splitlines():
            line = line.strip()

            result = r1.match(line)

            if result:
                vrf = result.group('vrf')
                address_family = result.group('address_family').lower()
                eigrp_instance = result.group('as_num')

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
                ip_dict['srtt'] = float(group['srtt'])
                ip_dict['rto'] = int(group['rto'])
                ip_dict['q_cnt'] = int(group['q_cnt'])
                ip_dict['last_seq_number'] = int(group['last_seq_number'])

        return parsed_dict


# ===============================================
# Parser for:
#   * 'show ip eigrp vrf {vrf} neighbors'
#   * 'show ip eigrp neighbors'
# ===============================================
class ShowIpEigrpNeighbors(ShowEigrpNeighborsSuperParser, ShowEigrpNeighborsSchema):

    cli_command = ['show ip eigrp vrf {vrf} neighbors',
                   'show ip eigrp neighbors',]

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
            show_output = self.device.execute(cmd)

        else:
            show_output = output

        return super().cli(output=show_output, address_family='ipv4', vrf=vrf)


# ===============================================
# Parser for:
#   * 'show ipv6 eigrp vrf {vrf} neighbors'
#   * 'show ipv6 eigrp neighbors'
# ===============================================
class ShowIpv6EigrpNeighbors(ShowEigrpNeighborsSuperParser, ShowEigrpNeighborsSchema):

    cli_command = ['show ipv6 eigrp vrf {vrf} neighbors',
                   'show ipv6 eigrp neighbors',]

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
            show_output = self.device.execute(cmd)

        else:
            show_output = output

        return super().cli(output=show_output, address_family='ipv6', vrf=vrf)


class ShowIpEigrpNeighborsDetailSchema(MetaParser):
    ''' Schema for
        * 'show ip eigrp neighbors detail'
        * 'show ip eigrp vrf <vrf> neighbors detail'
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
                                            'topology_ids_from_peer': int, }, },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# ===========================================
# Parser for:
#       'show ip eigrp neighbors detail'
#       'show ip eigrp vrf <vrf> neighbors detail'
# ===========================================
class ShowIpEigrpNeighborsDetail(ShowIpEigrpNeighborsDetailSchema):

    cli_command = ['show ip eigrp neighbors detail',
                   'show ip eigrp vrf {vrf} neighbors detail']

    def cli(self, vrf='', output=None):

        if output is None:
            if vrf:
                out = self.device.execute(self.cli_command[1]).format(vrf=vrf)
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # EIGRP-IPv4 VR(foo) Address-Family Neighbors for AS(1)
        # EIGRP-IPv4 VR(foo) Address-Family Neighbors for AS(1) VRF(VRF1)
        r1 = re.compile(r'EIGRP\-(?P<address_family>IPv4|IPv6)[\w \-\(\)]+ +'
                        'Address-Family\s*Neighbors\s*for '
                        '\w*\(\s*(?P<as_num>[\S]+)\)\s*(?:VRF\((?P<vrf>\S+)\))?')

        # EIGRP-IPv4 Neighbors for AS(100)
        # EIGRP-IPv4 Neighbors for AS(100) VRF(VRF1)
        r2 = re.compile(r'EIGRP\-(?P<address_family>IPv4|IPv6)\s*'
            'Neighbors\s*for \w+\(\s*(?P<as_num>\d+)\)\s*(?:VRF\((?P<vrf>\S+)\))?')

        # H     Address     Interface   Hold    Uptime   SRTT   RTO     Q       Seq
        #                               (sec)                   (ms)    Cnt     Num
        # 0     10.1.2.1    Et1/0       11      00:02:31 12     200     0       6
        # 1     10.1.2.3    Gi0/1       11      00:20:39 2202   5000    0       5
        r3 = re.compile(r'^(?P<peer_handle>\d+) +'
                        '(?P<nbr_address>\S+) +'
                        '(?P<eigrp_interface>[A-Za-z]+\s*[\d\/]+) +'
                        '(?P<hold>\d+) +(?P<uptime>\S+) +'
                        '(?P<srtt>\d+) +'
                        '(?P<rto>\d+) +'
                        '(?P<q_cnt>\d+) +'
                        '(?P<last_seq_number>\d+)$')

        # Version 8.0/2.0, Retrans: 0, Retries: 0, Prefixes: 1
        # Version 5.1/3.0, Retrans: 2, Retries: 0, Prefixes: 1
        # Version 23.0/2.0, Retrans: 0, Retries: 0
        r4 = re.compile(r'Version\s*'
                        '(?P<os_majorver>\d+)\.(?P<os_minorver>\d+)\/'
                        '(?P<tlv_majorrev>\d+)\.(?P<tlv_minorrev>\d+), +'
                        'Retrans\s*:\s*(?P<retransmit_count>\d+)\, +'
                        'Retries\s*:\s*(?P<retry_count>\d+)\,* *'
                        '(?:Prefixes\s*:\s*(?P<prefixes>\d+))?')

        # Topology-ids from peer - 0
        r5 = re.compile(r'Topology\-ids\s+from\s+peer\s+\-\s+'
                        '(?P<topology_ids_from_peer>\d+)')

        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # EIGRP-IPv4 VR(foo) Address-Family Neighbors for AS(1)
            # EIGRP-IPv4 VR(foo) Address-Family Neighbors for AS(1) VRF(VRF1)
            result = r1.match(line)

            if result:

                group = result.groupdict()

                address_family = group['address_family'].lower()
                as_num = group['as_num']
                vrf = group['vrf'] if group['vrf'] else 'default'

                # eigrp_instance_dict is used when matching r3
                eigrp_instance_dict = parsed_dict\
                    .setdefault('eigrp_instance', {})\
                    .setdefault(as_num, {})\
                    .setdefault('vrf', {})\
                    .setdefault(vrf, {})\
                    .setdefault('address_family', {})\
                    .setdefault(address_family, {})

                continue

            # EIGRP-IPv4 Neighbors for AS(100)
            # EIGRP-IPv4 Neighbors for AS(100) VRF(VRF1)
            result = r2.match(line)
            if result:

                group = result.groupdict()

                address_family = group['address_family'].lower()
                as_num = group['as_num']
                vrf = group['vrf'] if group['vrf'] else 'default'

                # eigrp_instance_dict is used when matching r3
                eigrp_instance_dict = parsed_dict\
                    .setdefault('eigrp_instance', {})\
                    .setdefault(as_num, {})\
                    .setdefault('vrf', {})\
                    .setdefault(vrf, {})\
                    .setdefault('address_family', {})\
                    .setdefault(address_family, {})

                continue

            # H     Address     Interface   Hold    Uptime   SRTT   RTO     Q       Seq
            #                               (sec)                   (ms)    Cnt     Num
            # 0     10.1.2.1    Et1/0       11      00:02:31 12     200     0       6
            result = r3.match(line)
            if result:

                group = result.groupdict()

                eigrp_interface = Common.convert_intf_name\
                    (intf=group['eigrp_interface'])

                nbr_address = group['nbr_address']

                ip_dict = eigrp_instance_dict\
                    .setdefault('eigrp_interface', {})\
                    .setdefault(eigrp_interface, {})\
                    .setdefault('eigrp_nbr', {})\
                    .setdefault(nbr_address, {})

                # dict for current IP Address
                # ip_dict is also used in r5
                ip_dict['peer_handle'] = int(group['peer_handle'])
                ip_dict['hold'] = int(group['hold'])
                ip_dict['uptime'] = group['uptime']
                ip_dict['srtt'] = float(group['srtt'])
                ip_dict['rto'] = int(group['rto'])
                ip_dict['q_cnt'] = int(group['q_cnt'])
                ip_dict['last_seq_number'] = \
                    int(group['last_seq_number'])

                continue

            # Version 8.0/2.0, Retrans: 0, Retries: 0, Prefixes: 1
            result = r4.match(line)
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

                prefixes = group['prefixes']

                ip_dict['prefixes'] = int(prefixes) if prefixes else 0

                continue

            # Topology-ids from peer - 0
            result = r5.match(line)
            if result:
                group = result.groupdict()

                ip_dict['topology_ids_from_peer'] = \
                    int(group['topology_ids_from_peer'])
                continue

        return parsed_dict
