''' show_eigrp.py
IOSXR parser for the following commands

    * 'show eigrp ipv4 neighbors'
    * 'show eigrp ipv4 vrf {vrf} neighbors'

    * 'show eigrp ipv6 neighbors'
    * 'show eigrp ipv6 vrf {vrf} neighbors'

    * 'show eigrp ipv4 neighbors detail'
    * 'show eigrp ipv4 vrf {vrf} neighbors detail'

    * 'show eigrp ipv6 neighbors detail'
    * 'show eigrp ipv6 vrf {vrf} neighbors detail'
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
        * 'show eigrp ipv4 neighbors'
        * 'show eigrp ipv4 vrf {vrf} neighbors'

        * 'show eigrp ipv6 neighbors'
        * 'show eigrp ipv6 vrf {vrf} neighbors'
    '''

    schema = {
        'eigrp_instance': {
            Any(): {
                'vrf': {
                    Any(): {
                        'address_family': {
                            Any(): {
                                'name': str,
                                'named_mode': bool,
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


# =======================================
# Parser for:
#   'show eigrp ipv4 neighbors'
#   'show eigrp ipv4 vrf {vrf} neighbors'
#   'show eigrp ipv6 neighbors'
#   'show eigrp ipv6 vrf {vrf} neighbors'
# =======================================
class ShowEigrpNeighborsSuperParser(ShowEigrpNeighborsSchema):

    def cli(self, vrf='', output=None):

        # IPv4-EIGRP VR(test) Neighbors for AS(100) VRF default
        # IPv4-EIGRP VR(test) Neighbors for AS(100) VRF VRF1
        # IPv6-EIGRP VR(test) Neighbors for AS(100) VRF default
        # IPv6-EIGRP VR(test) Neighbors for AS(100) VRF VRF1
        r1 = re.compile(r'^(?P<address_family>IPv4|IPv6)\-EIGRP\s+'
                        '(?:VR\(?(?P<name>\S+)\))?\s*Neighbors\s*for\s*'
                        'AS\(\s*(?P<as_num>\d+)\)\s*VRF\s*(?P<vrf>\S+)$')

        # H   Address                 Interface       Hold Uptime   SRTT   RTO  Q  Seq
        #                                             (sec)         (ms)       Cnt Num
        # 1   10.23.90.3              Gi0/0/0/1.90      13 01:41:56   13   200  0  23
        # 0   10.12.90.1              Gi0/0/0/0.90      14 02:55:10    1   200  0  17
        # 1   10.23.90.3              Gi0/0/0/1.390     12 01:40:17    4   200  0  15
        # 0   10.12.90.1              Gi0/0/0/0.390     12 02:52:31  816  4896  0  8
        r2 = re.compile(r'^(?P<peer_handle>\d+) +'
                        '(?P<nbr_address>\S+) +'
                        '(?P<eigrp_interface>[A-Za-z]+\s*[\d\/\.]+) +'
                        '(?P<hold>\d+) +(?P<uptime>\S+) +'
                        '(?P<srtt>\d+) +'
                        '(?P<rto>\d+) +'
                        '(?P<q_cnt>\d+) +'
                        '(?P<last_seq_number>\d+)$')

        # H   Address                 Interface       Hold Uptime   SRTT   RTO  Q  Seq
        #                                             (sec)         (ms)       Cnt Num
        # 1   Link Local Address:     Gi0/0/0/1.90      12 01:36:14   11   200  0  28
        r3 = re.compile(r'^(?P<peer_handle>\d+) +Link\s+Local\s+Address: +'
                        '(?P<eigrp_interface>[A-Za-z]+\s*[\d\/\.]+) +'
                        '(?P<hold>\d+) +(?P<uptime>\S+) +(?P<srtt>\d+) +'
                        '(?P<rto>\d+) +(?P<q_cnt>\d+) +'
                        '(?P<last_seq_number>\d+)$')

        # fe80::5c00:ff:fe02:7
        # fe80::5c00:ff:fe02:7
        r4 = re.compile(r'^(?P<nbr_address>\S+)$')

        parsed_dict = {}

        for line in output.splitlines():

            line = line.strip()

            # IPv4-EIGRP VR(test) Neighbors for AS(100) VRF default
            # IPv4-EIGRP VR(test) Neighbors for AS(100) VRF VRF1
            # IPv6-EIGRP VR(test) Neighbors for AS(100) VRF default
            # IPv6-EIGRP VR(test) Neighbors for AS(100) VRF VRF1
            result = r1.match(line)
            if result:
                group = result.groupdict()

                name = group['name']
                named_mode = True if name else False
                address_family = group['address_family'].lower()
                eigrp_instance = group['as_num']
                vrf = group['vrf']
                continue

            # 1   10.23.90.3              Gi0/0/0/1.90      13 01:41:56   13   200  0  23
            # 0   10.12.90.1              Gi0/0/0/0.90      14 02:55:10    1   200  0  17
            # 1   10.23.90.3              Gi0/0/0/1.390     12 01:40:17    4   200  0  15
            # 0   10.12.90.1              Gi0/0/0/0.390     12 02:52:31  816  4896  0  8
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

                address_family_dict = parsed_dict\
                    .setdefault('eigrp_instance', {})\
                    .setdefault(eigrp_instance, {})\
                    .setdefault('vrf', {})\
                    .setdefault(vrf, {})\
                    .setdefault('address_family', {})\
                    .setdefault(address_family, {})

                address_family_dict['name'] = name
                address_family_dict['named_mode'] = named_mode

                ip_dict = address_family_dict.setdefault('eigrp_interface', {})\
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

            # 1   Link Local Address:     Gi0/0/0/1.90      12 01:36:14   11   200  0  28
            # 0   Link Local Address:     Gi0/0/0/0.90      11 02:30:16    1   200  0  23
            result = r3.match(line)
            if result:

                group = result.groupdict()

                if not vrf:
                    vrf = 'default'

                if not eigrp_instance:
                    eigrp_instance = ''

                eigrp_interface = Common.convert_intf_name\
                    (intf=group['eigrp_interface'])

                peer_handle = int(group['peer_handle'])
                hold = int(group['hold'])
                uptime = group['uptime']
                srtt = float(group['srtt'])/1000
                rto = int(group['rto'])
                q_cnt = int(group['q_cnt'])
                last_seq_number = int(group['last_seq_number'])
                continue

            # fe80::5c00:ff:fe02:7
            # fe80::5c00:ff:fe02:7
            result = r4.match(line)
            if result:

                group = result.groupdict()

                nbr_address = group['nbr_address']

                address_family_dict = parsed_dict\
                    .setdefault('eigrp_instance', {})\
                    .setdefault(eigrp_instance, {})\
                    .setdefault('vrf', {})\
                    .setdefault(vrf, {})\
                    .setdefault('address_family', {})\
                    .setdefault(address_family, {})

                address_family_dict['name'] = name
                address_family_dict['named_mode'] = named_mode

                ip_dict = address_family_dict.setdefault('eigrp_interface', {})\
                    .setdefault(eigrp_interface, {})\
                    .setdefault('eigrp_nbr', {}).setdefault(nbr_address, {})

                ip_dict['peer_handle'] = peer_handle
                ip_dict['hold'] = hold
                ip_dict['uptime'] = uptime
                ip_dict['srtt'] = srtt
                ip_dict['rto'] = rto
                ip_dict['q_cnt'] = q_cnt
                ip_dict['last_seq_number'] = last_seq_number

                continue

        return parsed_dict


class ShowEigrpIpv4Neighbors(ShowEigrpNeighborsSuperParser,
                             ShowEigrpNeighborsSchema):
    cli_command = ['show eigrp ipv4 vrf {vrf} neighbors',
                   'show eigrp ipv4 neighbors']
    exclude = ['dead_time', 'hold']

    def cli(self, vrf='all', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]

            show_output = self.device.execute(cmd)

        else:
            show_output = output

        return super().cli(output=show_output, vrf=vrf)


class ShowEigrpIpv6Neighbors(ShowEigrpNeighborsSuperParser,
                             ShowEigrpNeighborsSchema):
    cli_command = ['show eigrp ipv6 vrf {vrf} neighbors',
                   'show eigrp ipv6 neighbors']
    exclude = ['hold']

    def cli(self, vrf='all', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]

            show_output = self.device.execute(cmd)

        else:
            show_output = output

        return super().cli(output=show_output, vrf=vrf)


class ShowEigrpNeighborsDetailSchema(MetaParser):
    ''' Schema for
        * 'show eigrp ipv4 neighbors detail'
        * 'show eigrp ipv4 vrf {vrf} neighbors detail'
        * 'show eigrp ipv6 neighbors detail'
        * 'show eigrp ipv6 vrf {vrf} neighbors detail'
    '''

    schema = {
        'eigrp_instance': {
            Any(): {
                'vrf': {
                    Any(): {
                        'address_family': {
                            Any(): {
                                'name': str,
                                'named_mode': bool,
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
                                                'bfd': str,
                                                'prefixes': int, }, },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            }


# ================================================
# Parser fpr
#   'show eigrp ipv4 neighbors detail'
#   'show eigrp ipv4 vrf {vrf} neighbors detail'
#   'show eigrp ipv6 neighbors detail'
#   'show eigrp ipv6 vrf {vrf} neighbors detail'
# ================================================
class ShowEigrpNeighborsDetailSuperParser(ShowEigrpNeighborsDetailSchema):

    def cli(self, vrf='', output=None):

        # IPv4-EIGRP VR(test) Neighbors for AS(100) VRF VRF1
        # IPv4-EIGRP VR(test) Neighbors for AS(100) VRF default
        # IPv6-EIGRP VR(test) Neighbors for AS(100) VRF default
        # IPv6-EIGRP VR(test) Neighbors for AS(100) VRF VRF1
        r1 = re.compile(r'^(?P<address_family>IPv4|IPv6)\-EIGRP\s+'
                        '(?:VR\(?(?P<name>\S+)\))?\s*Neighbors\s*for\s*'
                        'AS\(\s*(?P<as_num>\d+)\)\s*VRF\s*(?P<vrf>\S+)$')

        # 1   10.23.90.3              Gi0/0/0/1.90      11 01:43:15   13   200  0  23
        # 1   10.23.90.3              Gi0/0/0/1.390     14 01:41:47    4   200  0  15
        # 0   10.12.90.1              Gi0/0/0/0.390     13 02:54:01  816  4896  0  8
        r2 = re.compile(r'^(?P<peer_handle>\d+) +'
                        '(?P<nbr_address>\S+) +'
                        '(?P<eigrp_interface>[A-Za-z]+\s*[\d\/\.]+) +'
                        '(?P<hold>\d+) +(?P<uptime>\S+) +'
                        '(?P<srtt>\d+) +'
                        '(?P<rto>\d+) +'
                        '(?P<q_cnt>\d+) +'
                        '(?P<last_seq_number>\d+)$')

        # 1   Link Local Address:     Gi0/0/0/1.390     11 01:42:44    9   200  0  14
        # 0   Link Local Address:     Gi0/0/0/0.390     12 02:31:47    4   200  0  9
        r3 = re.compile(r'^(?P<peer_handle>\d+) +Link\s+Local\s+Address: +'
                        '(?P<eigrp_interface>[A-Za-z]+\s*[\d\/\.]+) +'
                        '(?P<hold>\d+) +(?P<uptime>\S+) +(?P<srtt>\d+) +'
                        '(?P<rto>\d+) +(?P<q_cnt>\d+) +'
                        '(?P<last_seq_number>\d+)$')

        # fe80::5c00:ff:fe02:7
        # fe80::5c00:ff:fe02:7
        r4 = re.compile(r'^(?P<nbr_address>\S+)$')

        # Version 23.0/2.0, Retrans: 1, Retries: 0, Prefixes: 6
        # Version 8.0/1.2, Retrans: 1, Retries: 0, Prefixes: 5
        r5 = re.compile(r'Version\s*'
                        '(?P<os_majorver>\d+)\.(?P<os_minorver>\d+)\/'
                        '(?P<tlv_majorrev>\d+)\.(?P<tlv_minorrev>\d+), +'
                        'Retrans\s*:\s*(?P<retransmit_count>\d+)\, +'
                        'Retries\s*:\s*(?P<retry_count>\d+)\,* *'
                        '(?:Prefixes\s*:\s*(?P<prefixes>\d+))?')

        # BFD disabled
        r6 = re.compile(r'^BFD\s+(?P<bfd>\w+)$')

        parsed_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # IPv4-EIGRP VR(test) Neighbors for AS(100) VRF VRF1
            # IPv4-EIGRP VR(test) Neighbors for AS(100) VRF default
            # IPv6-EIGRP VR(test) Neighbors for AS(100) VRF default
            # IPv6-EIGRP VR(test) Neighbors for AS(100) VRF VRF1
            result = r1.match(line)
            if result:
                group = result.groupdict()

                name = group['name']
                named_mode = True if name else False
                address_family = group['address_family'].lower()
                eigrp_instance = group['as_num']
                vrf = group['vrf']
                continue

            # 1   10.23.90.3              Gi0/0/0/1.90      11 01:43:15   13   200  0  23
            # 1   10.23.90.3              Gi0/0/0/1.390     14 01:41:47    4   200  0  15
            # 0   10.12.90.1              Gi0/0/0/0.390     13 02:54:01  816  4896  0  8
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

                address_family_dict = parsed_dict\
                    .setdefault('eigrp_instance', {})\
                    .setdefault(eigrp_instance, {})\
                    .setdefault('vrf', {})\
                    .setdefault(vrf, {})\
                    .setdefault('address_family', {})\
                    .setdefault(address_family, {})

                address_family_dict['name'] = name
                address_family_dict['named_mode'] = named_mode

                ip_dict = address_family_dict.setdefault('eigrp_interface', {})\
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

            # 1   Link Local Address:     Gi0/0/0/1.390     11 01:42:44    9   200  0  14
            # 0   Link Local Address:     Gi0/0/0/0.390     12 02:31:47    4   200  0  9
            result = r3.match(line)
            if result:

                group = result.groupdict()

                if not vrf:
                    vrf = 'default'

                if not eigrp_instance:
                    eigrp_instance = ''

                eigrp_interface = Common.convert_intf_name\
                    (intf=group['eigrp_interface'])

                peer_handle = int(group['peer_handle'])
                hold = int(group['hold'])
                uptime = group['uptime']
                srtt = float(group['srtt'])/1000
                rto = int(group['rto'])
                q_cnt = int(group['q_cnt'])
                last_seq_number = int(group['last_seq_number'])
                continue

            # fe80::5c00:ff:fe02:7
            # fe80::5c00:ff:fe02:7
            result = r4.match(line)
            if result:

                group = result.groupdict()

                nbr_address = group['nbr_address']

                address_family_dict = parsed_dict\
                    .setdefault('eigrp_instance', {})\
                    .setdefault(eigrp_instance, {})\
                    .setdefault('vrf', {})\
                    .setdefault(vrf, {})\
                    .setdefault('address_family', {})\
                    .setdefault(address_family, {})

                address_family_dict['name'] = name
                address_family_dict['named_mode'] = named_mode

                ip_dict = address_family_dict.setdefault('eigrp_interface', {})\
                    .setdefault(eigrp_interface, {})\
                    .setdefault('eigrp_nbr', {}).setdefault(nbr_address, {})

                ip_dict['peer_handle'] = peer_handle
                ip_dict['hold'] = hold
                ip_dict['uptime'] = uptime
                ip_dict['srtt'] = srtt
                ip_dict['rto'] = rto
                ip_dict['q_cnt'] = q_cnt
                ip_dict['last_seq_number'] = last_seq_number

                continue

            # Version 23.0/2.0, Retrans: 1, Retries: 0, Prefixes: 6
            # Version 8.0/1.2, Retrans: 1, Retries: 0, Prefixes: 5
            result = r5.match(line)
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

            # BFD disabled
            result = r6.match(line)
            if result:

                group = result.groupdict()

                ip_dict['bfd'] = group['bfd']

        return parsed_dict


class ShowEigrpIpv4NeighborsDetail(ShowEigrpNeighborsDetailSuperParser,
                                   ShowEigrpNeighborsDetailSchema):

    cli_command = ['show eigrp ipv4 vrf {vrf} neighbors detail',
                   'show eigrp ipv4 neighbors detail', ]
    exclude = ['hold']

    def cli(self, vrf='all', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]

            show_output = self.device.execute(cmd)

        else:
            show_output = output

        return super().cli(output=show_output, vrf=vrf)


class ShowEigrpIpv6NeighborsDetail(ShowEigrpNeighborsDetailSuperParser,
                                   ShowEigrpNeighborsDetailSchema):
    cli_command = ['show eigrp ipv6 vrf {vrf} neighbors detail', 
                   'show eigrp ipv6 neighbors detail', ]
    exclude = ['hold']

    def cli(self, vrf='all', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]

            show_output = self.device.execute(cmd)

        else:
            show_output = output

        return super().cli(output=show_output, vrf=vrf)
