''' show_eigrp.py
IOSXE parsers for the following commands

    * 'show ip eigrp neighbors'
    * 'show ip eigrp vrf <vrf> neighbors'
    * 'show ipv6 eigrp neighbors'
    * 'show ipv6 eigrp vrf <vrf> neighbors'
    * 'show ip eigrp neighbors detail'
    * 'show ip eigrp vrf <vrf> neighbors detail'
    * 'show ipv6 eigrp neighbors detail'
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
        * 'show ipv6 eigrp vrf <vrf> neighbors'
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

        # EIGRP-IPv6 VR(test) Address-Family Neighbors for AS(100)
        # EIGRP-IPv4 VR(test) Address-Family Neighbors for AS(100) VRF(VRF1)
        r2 = re.compile('^EIGRP\-(?P<address_family>IPv4|IPv6)\s* '
                        'VR\s*\((?P<name>\S+)\) Address-Family Neighbors\s'
                        '*for \w+\(\s*(?P<as_num>\d+)\)\s*'
                        '(?:VRF\((?P<vrf>\S+)\))?$')

        # When VRF is not on the same line as r1 and r2
        # VRF(VRF1)
        r3 = re.compile(r'^VRF\((?P<vrf>\S+)\)$')

        # H   Address      Interface  Hold  Uptime    SRTT   RTO    Q   Seq
        #                             (sec)           (ms)          Cnt Num
        # 0   10.1.1.2     Gi0/0      13    00:00:03  1996   5000   0   5
        # 2   10.1.1.9     Gi0/0      14    00:02:24  206    5000   0   5
        # 1   10.1.2.3     Gi0/1      11    00:20:39  2202   5000   0   5
        r4 = re.compile(r'^(?P<peer_handle>\d+) +'
                        '(?P<nbr_address>\S+) +'
                        '(?P<eigrp_interface>[A-Za-z]+\s*[\.\d\/]+) +'
                        '(?P<hold>\d+) +(?P<uptime>\S+) +'
                        '(?P<srtt>\d+) +'
                        '(?P<rto>\d+) +'
                        '(?P<q_cnt>\d+) +'
                        '(?P<last_seq_number>\d+)$')
        # H   Address                 Interface       Hold Uptime   SRTT   RTO  Q  Seq
        #                                             (sec)         (ms)       Cnt Num
        # 1   Link Local Address:     Gi0/0/0/1.90      12 01:36:14   11   200  0  28
        r5 = re.compile(r'^(?P<peer_handle>\d+) +Link\-local\s+address: +'
                        '(?P<eigrp_interface>[A-Za-z]+\s*[\d\/\.]+) +'
                        '(?P<hold>\d+) +(?P<uptime>\S+) +(?P<srtt>\d+) +'
                        '(?P<rto>\d+) +(?P<q_cnt>\d+) +'
                        '(?P<last_seq_number>\d+)$')

        # fe80::5c00:ff:fe02:7
        # fe80::5c00:ff:fe02:7
        r6 = re.compile(r'^(?P<nbr_address>\S+:\S*:\S*:\S*:\S*:\S+)$')

        parsed_dict = {}
        eigrp_instance = ''
        name = ''
        named_mode = False    

        # Get output
        out = output

        for line in out.splitlines():
            line = line.strip()

            # EIGRP-IPv4 Neighbors for AS(1100) VRF(VRF1)
            result = r1.match(line)
            if result:

                group = result.groupdict()
                name = group.get('name', '')
                vrf = group['vrf']
                address_family = group['address_family'].lower()
                eigrp_instance = group['as_num']

            # EIGRP-IPv6 VR(test) Address-Family Neighbors for AS(100)
            # EIGRP-IPv4 VR(test) Address-Family Neighbors for AS(100) VRF(VRF1)
            result = r2.match(line)
            if result:

                group = result.groupdict()

                name = group['name']
                vrf = group['vrf']
                address_family = group['address_family'].lower()
                eigrp_instance = group['as_num']

                continue

            # VRF(VRF1)
            result = r3.match(line)
            if result:
                group = result.groupdict()
                vrf = group['vrf']
                continue

            # H   Address      Interface  Hold  Uptime    SRTT   RTO    Q   Seq
            #                             (sec)           (ms)          Cnt Num
            # 0   10.1.1.2     Gi0/0      13    00:00:03  1996   5000   0   5
            # 2   10.1.1.9     Gi0/0      14    00:02:24  206    5000   0   5
            # 1   10.1.2.3     Gi0/1      11    00:20:39  2202   5000   0   5
            result = r4.match(line)

            if result:

                group = result.groupdict()

                if not vrf:
                    vrf = 'default'

                if not eigrp_instance:
                    eigrp_instance = ''

                if not name:
                    named_mode = False
                else:
                    named_mode = True

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

            # 1   Link Local Address:     Gi0/0/0/1.90      12 01:36:14   11   200  0  28
            result = r5.match(line)            
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
            result = r6.match(line)
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

                if not name:
                    named_mode = False
                else:
                    named_mode = True

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
        * 'show ipv6 eigrp neighbors detail'        
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
                                            'prefixes': int,
                                            'topology_ids_from_peer': int, 
                                            'topology_advert_to_peer': str}, },
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
# Super parser for:
#       'show ip eigrp neighbors detail'
#       'show ip eigrp vrf <vrf> neighbors detail'
#       'show ipv6 eigrp neighbors detail'
# ===========================================
class ShowIpEigrpNeighborsDetailSuperParser(ShowIpEigrpNeighborsDetailSchema):

    def cli(self, vrf='', output=None):

        # EIGRP-IPv4 VR(foo) Address-Family Neighbors for AS(1)
        # EIGRP-IPv4 VR(foo) Address-Family Neighbors for AS(1) VRF(VRF1)
        r1 = re.compile(r'EIGRP\-(?P<address_family>IPv4|IPv6)\s+VR'
                        '\((?P<name>\w+)\)\s+Address\-Family\s*Neighbors'
                        '\s*for \w*\(\s*(?P<as_num>[\S]+)\)\s*'
                        '(?:VRF\((?P<vrf>\S+)\))?')

        # EIGRP-IPv4 Neighbors for AS(100)
        # EIGRP-IPv4 Neighbors for AS(100) VRF(VRF1)
        r2 = re.compile(r'EIGRP\-(?P<address_family>IPv4|IPv6)\s*'
                        'Neighbors\s*for \w+\(\s*(?P<as_num>\d+)\)\s*'
                        '(?:VRF\((?P<vrf>\S+)\))?')

        # H     Address     Interface   Hold    Uptime   SRTT   RTO     Q       Seq
        #                               (sec)                   (ms)    Cnt     Num
        # 0     10.1.2.1    Et1/0       11      00:02:31 12     200     0       6
        # 1     10.1.2.3    Gi0/1       11      00:20:39 2202   5000    0       5
        r3 = re.compile(r'^(?P<peer_handle>\d+) +'
                        '(?P<nbr_address>\S+) +'
                        '(?P<eigrp_interface>[A-Za-z]+\s*[\.\d\/]+) +'
                        '(?P<hold>\d+) +(?P<uptime>\S+) +'
                        '(?P<srtt>\d+) +'
                        '(?P<rto>\d+) +'
                        '(?P<q_cnt>\d+) +'
                        '(?P<last_seq_number>\d+)$')

        # 1   Link-local address:     Gi3.90                   11 01:30:32   10   100  0  29
        r4 = re.compile(r'^(?P<peer_handle>\d+) +Link\-local\s+address: +'
                        '(?P<eigrp_interface>[A-Za-z]+\s*[\d\/\.]+) +'
                        '(?P<hold>\d+) +(?P<uptime>\S+) +(?P<srtt>\d+) +'
                        '(?P<rto>\d+) +(?P<q_cnt>\d+) +'
                        '(?P<last_seq_number>\d+)$')
        # fe80::5c00:ff:fe02:7
        # fe80::5c00:ff:fe02:7
        r5 = re.compile(r'^(?P<nbr_address>\S+)$')

        # Version 8.0/2.0, Retrans: 0, Retries: 0, Prefixes: 1
        # Version 5.1/3.0, Retrans: 2, Retries: 0, Prefixes: 1
        # Version 23.0/2.0, Retrans: 0, Retries: 0
        r6 = re.compile(r'Version\s*'
                        '(?P<os_majorver>\d+)\.(?P<os_minorver>\d+)\/'
                        '(?P<tlv_majorrev>\d+)\.(?P<tlv_minorrev>\d+), +'
                        'Retrans\s*:\s*(?P<retransmit_count>\d+)\, +'
                        'Retries\s*:\s*(?P<retry_count>\d+)\,* *'
                        '(?:Prefixes\s*:\s*(?P<prefixes>\d+))?')

        # Topology-ids from peer - 0
        r7 = re.compile(r'Topology\-ids\s+from\s+peer\s+\-\s+'
                        '(?P<topology_ids_from_peer>\d+)')

        #  Topologies advertised to peer:   base
        r8 = re.compile(r'Topologies\s+advertised\s+to\s+peer:\s*'
                        '(?P<topology_advert_to_peer>\w+)')

        parsed_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # EIGRP-IPv4 VR(foo) Address-Family Neighbors for AS(1)
            # EIGRP-IPv4 VR(foo) Address-Family Neighbors for AS(1) VRF(VRF1)
            result = r1.match(line)

            if result:

                group = result.groupdict()

                name = group.get('name', '')
                named_mode = True if name else False
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

                eigrp_instance_dict['name'] = name
                eigrp_instance_dict['named_mode'] = named_mode

                continue

            # EIGRP-IPv4 Neighbors for AS(100)
            # EIGRP-IPv4 Neighbors for AS(100) VRF(VRF1)
            result = r2.match(line)
            if result:

                group = result.groupdict()

                name = group.get('name', '')
                named_mode = True if name else False

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

                eigrp_instance_dict['name'] = name
                eigrp_instance_dict['named_mode'] = named_mode

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
                ip_dict['topology_advert_to_peer'] = ''
                continue

            # 1   Link-local address:     Gi3.90      11 01:30:32   10   100  0  29
            result = r4.match(line)
            if result:
                group = result.groupdict()

                if not vrf:
                    vrf = 'default'                

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
            result = r5.match(line)
            if result:
                group = result.groupdict()

                nbr_address = group['nbr_address']

                ip_dict = parsed_dict\
                    .setdefault('eigrp_instance', {})\
                    .setdefault(as_num, {})\
                    .setdefault('vrf', {})\
                    .setdefault(vrf, {})\
                    .setdefault('address_family', {})\
                    .setdefault(address_family, {})\
                    .setdefault('eigrp_interface', {})\
                    .setdefault(eigrp_interface, {})\
                    .setdefault('eigrp_nbr', {}).setdefault(nbr_address, {})

                ip_dict['peer_handle'] = peer_handle
                ip_dict['hold'] = hold
                ip_dict['uptime'] = uptime
                ip_dict['srtt'] = srtt
                ip_dict['rto'] = rto
                ip_dict['q_cnt'] = q_cnt
                ip_dict['last_seq_number'] = last_seq_number
                ip_dict['topology_advert_to_peer'] = ''

                continue

            # Version 8.0/2.0, Retrans: 0, Retries: 0, Prefixes: 1
            result = r6.match(line)
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
            result = r7.match(line)
            if result:
                group = result.groupdict()

                ip_dict['topology_ids_from_peer'] = \
                    int(group['topology_ids_from_peer'])
                continue

            # Topologies advertised to peer:   base
            result = r8.match(line)
            if result:
                group = result.groupdict()

                ip_dict['topology_advert_to_peer'] = \
                    group['topology_advert_to_peer']

                continue

        return parsed_dict


class ShowIpEigrpNeighborsDetail(ShowIpEigrpNeighborsDetailSuperParser,
                                 ShowIpEigrpNeighborsDetailSchema):
    
    # Parser for:
    #   'show ip eigrp neighbors detail'
    #   'show ip eigrp vrf <vrf> neighbors detail'

    cli_command = ['show ip eigrp vrf {vrf} neighbors detail',
                   'show ip eigrp neighbors detail',]

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
            show_output = self.device.execute(cmd)

        else:
            show_output = output

        return super().cli(output=show_output, vrf=vrf)

class ShowIpv6EigrpNeighborsDetail(ShowIpEigrpNeighborsDetailSuperParser,
                                   ShowIpEigrpNeighborsDetailSchema):

    # Parser for:
    #   'show ipv6 eigrp neighbors detail'    

    cli_command = 'show ipv6 eigrp neighbors detail'

    def cli(self, output=None):
        if output is None:            
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output

        return super().cli(output=show_output, vrf='default')
