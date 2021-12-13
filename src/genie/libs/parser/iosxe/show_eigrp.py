''' show_eigrp.py
IOSXE parsers for the following commands

    * 'show ip eigrp neighbors'
    * 'show ip eigrp vrf <vrf> neighbors'
    * 'show ipv6 eigrp neighbors'
    * 'show ipv6 eigrp vrf <vrf> neighbors'
    * 'show ip eigrp neighbors detail'
    * 'show ip eigrp vrf <vrf> neighbors detail'
    * 'show ipv6 eigrp neighbors detail'
    * 'show ip eigrp interfaces'
    * 'show ipv6 eigrp interfaces'
    * 'show ipv6 eigrp interfaces detail'
    * 'show ip eigrp interfaces detail'
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

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
    exclude = ['uptime' , 'hold']

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
    exclude = ['hold' , 'uptime']

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
                            Optional('eigrp_interface'): {
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

        # When VRF is alone in a line
        # VRF(VRF1)
        r2_1 = re.compile(r'VRF\((?P<vrf>\w+)\)')


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
        r5 = re.compile(r'^(?P<nbr_address>\S+:\S*:\S*:\S*:\S*:\S+)$')

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

            # VRF(VRF1)
            result = r2_1.match(line)
            if result:
                group = result.groupdict()
                vrf = group['vrf'] if group['vrf'] else 'default'

                eigrp_instance_dict = parsed_dict\
                    .setdefault('eigrp_instance', {})\
                    .setdefault(as_num, {})\
                    .setdefault('vrf', {})\
                    .setdefault(vrf, {})\
                    .setdefault('address_family', {})\
                    .setdefault(address_family, {})

                eigrp_instance_dict['name'] = name
                eigrp_instance_dict['named_mode'] = named_mode


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
    exclude = ['uptime', 'hold']

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
    exclude = ['hold' , 'uptime']

    def cli(self, output=None):
        if output is None:            
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output

        return super().cli(output=show_output, vrf='default')


class ShowEigrpInterfacesSchema(MetaParser):

    ''' Schema for
        * "show ip eigrp interfaces"
        * "show ip eigrp vrf <vrf> interfaces"
    '''

# These are the key-value pairs to add to the parsed dictionary
    schema = {
            'vrf':
                {Any():
                     {'eigrp_instance':
                          {Any():
                               {'address_family':
                                    {Any(): {
                                        Optional('name'): str,
                                        'named_mode': bool,
                                        'interface':
                                              {Any():
                                                   {'peers': int,
                                                    'xmit_q_unreliable': int,
                                                    'xmit_q_reliable': int,
                                                    'peer_q_unreliable': int,
                                                    'peer_q_reliable': int,
                                                    'mean_srtt': int,
                                                    'pacing_time_unreliable': int,
                                                    'pacing_time_reliable': int,
                                                    'mcast_flow_timer': int,
                                                    'pend_routes': int,
                                                    Optional('hello_interval'): int,
                                                    Optional('hold_time'): int,
                                                    Optional('split_horizon_enabled'): bool,
                                                    Optional('packetized_sent'): int,
                                                    Optional('packetized_expedited'): int,
                                                    Optional('hello_sent'): int,
                                                    Optional('hello_expedited'): int,
                                                    Optional('unreliable_mcasts'): int,
                                                    Optional('reliable_mcasts'): int,
                                                    Optional('unreliable_ucasts'): int,
                                                    Optional('reliable_ucasts'): int,
                                                    Optional('mcast_exceptions'): int,
                                                    Optional('cr_packets'): int,
                                                    Optional('acks_suppressed'): int,
                                                    Optional('retransmissions_sent'): int,
                                                    Optional('out_of_sequence_rcvd'): int,
                                                    Optional('topology_ids_on_interface'): int,
                                                    Optional('authentication_mode'): str,
                                                    Optional('key_chain'): str,
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
#       'show ip eigrp interfaces detail'
#       'show ip eigrp vrf <vrf> interfaces detail'
#       'show ipv6 eigrp interfaces detail'
#       'show ipv6 eigrp interfaces'
#       'show ip eigrp interfaces'
# ===========================================
class ShowEigrpInterfacesSuperParser(ShowEigrpInterfacesSchema):

    # Defines a function to run the cli_command
    def cli(self, vrf='', output=None):
        out = output

        # Initializes the Python dictionary variable
        parsed_dict = {}

        # Defines the regex for the first line of device output. Example is:
        # EIGRP-IPv4 Interfaces for AS(1)
        # EIGRP-IPv6 VR(cisco) Address-Family Interfaces for AS(20)
        p1 = re.compile(
            r'EIGRP\-(?P<address_family>IPv4|IPv6)\s+(VR\((?P<name>\w+)\)\s+Address\-Family\s+)?'
            r'Interfaces\s+for\s+AS\(\s*(?P<auto_sys>[\S]+)\)\s*(?:VRF\((?P<vrf>\S+)\))?$'
        )

        # VRF(1)
        p1_2 = re.compile(r"VRF\((?P<vrf>\S+)\)")

        # Defines the regex for the second line of device output. Example is:
        # Xmit Queue   PeerQ        Mean   Pacing Time   Multicast    Pending
        p2 = re.compile(r'Xmit +Queue +PeerQ +Mean +Pacing +Time +Multicast +Pending$')

        # Defines the regex for the third line of device output. Example is:
        # Interface              Peers  Un/Reliable  Un/Reliable  SRTT   Un/Reliable   Flow Timer   Routes
        p3 = re.compile(r'Interface +Peers +Un/Reliable +Un/Reliable +SRTT +Un/Reliable +Flow +Timer +Routes$')

        # Defines the regex for the fourth, and repeating, lines of device output. Example is:
        # Gi1                      1        0/0       0/0          20       0/0           84           0
        p4 = re.compile(
            r'(?P<interface>(\S+\d)) +(?P<peers>(\d+)) +(?P<xmit_q_unreliable>(\d+))/(?P<xmit_q_reliable>(\d+))'
            r' +(?P<peer_q_unreliable>(\d+))/(?P<peer_q_reliable>(\d+)) +(?P<mean_srtt>(\d+))'
            r' +(?P<pacing_t_unreliable>(\d+))/(?P<pacing_t_reliable>(\d+)) +(?P<mcast_flow_timer>(\d+))'
            r' +(?P<pend_routes>(\d+))$'
        )

        # Hello-interval is 5, Hold-time is 15
        p5 = re.compile(r'^Hello\-interval +is\s+(?P<hello_interval>\d+), +Hold\-time +is\s(?P<hold_time>\d+)$')

        # Split-horizon is enabled
        p6 = re.compile(r'^Split-horizon is (?P<state>\w+)$')

        # Packetized sent/expedited: 0/0
        p7 = re.compile(r'^Packetized +sent\/expedited:\s+(?P<sent>\d+)\/(?P<expedited>\d+)$')

        # Hello's sent/expedited: 597/1
        p8 = re.compile(r"^Hello's +sent\/expedited:\s+(?P<sent>\d+)\/(?P<expedited>\d+)$")

        #  Un/reliable mcasts: 0/0  Un/reliable ucasts: 0/0
        p9 = re.compile(
            r'^Un\/reliable +mcasts:\s+(?P<unreliable_mcast>\d+)\/(?P<reliable_mcast>\d+)\s+'
            r'Un\/reliable +ucasts: (?P<unreliable_ucast>\d+)\/(?P<reliable_ucast>\d+)$'
        )
        # Mcast exceptions: 0  CR packets: 0  ACKs suppressed: 0
        p10 = re.compile(
            r'^Mcast +exceptions:\s+(?P<mcast_exception>\d+)  +CR +packets:\s+'
            r'(?P<cr_packets>\d+) +ACKs +suppressed:\s+(?P<ack_suppressed>\d+)$'
        )
        #   Retransmissions sent: 0  Out-of-sequence rcvd: 0
        p11 = re.compile(
            r'^Retransmissions +sent:\s+(?P<retransmission_sent>\d+)  +Out\-of\-sequence +rcvd:\s+'
            r'(?P<out_of_sequence_rcvd>\d+)$'
        )

        #   Authentication mode is not set
        #   Authentication mode is md5,  key-chain is "test"
        p12 = re.compile(
            r'^Authentication +mode +is\s+(?P<authentication>[A-Za-z0-9\-]+|not set)'
            r'(, +key\-chain +is\s+(")?(?P<key_chain>not set|[A-Za-z0-9\-]+))?(")?'
        )

        # Defines the "for" loop, to pattern match each line of output
        for line in out.splitlines():
            line = line.strip()

            # Processes the matched patterns for the first line of output
            # EIGRP-IPv4 Interfaces for AS(1)
            # EIGRP-IPv6 VR(cisco) Address-Family Interfaces for AS(20)
            m = p1.match(line)

            if m:
                group = m.groupdict()
                auto_sys = group['auto_sys']
                instance_dict = parsed_dict.setdefault('vrf', {}). \
                    setdefault('default', {}).setdefault('eigrp_instance', {}). \
                    setdefault(auto_sys, {}).setdefault('address_family', {}). \
                    setdefault(group['address_family'].lower(), {})
                if group['name']:
                    instance_dict.update({'name': group['name']})
                    instance_dict.update({'named_mode': True if group['name'] else False})
                else:
                    instance_dict.update({'named_mode': False})
                    

                continue

            # VRF(1)
            m = p1_2.match(line)
            if m:
                group = m.groupdict()
                parsed_dict_copy = parsed_dict['vrf']['default'].copy()
                parsed_dict['vrf'] = {group['vrf']: parsed_dict_copy}
                continue

            # Processes the matched patterns for the second line of output
            # Xmit Queue   PeerQ        Mean   Pacing Time   Multicast    Pending
            m = p2.match(line)
            if m:
                continue

            # Processes the matched patterns for the third line of output
            # Interface              Peers  Un/Reliable  Un/Reliable  SRTT   Un/Reliable   Flow Timer   Routes
            m = p3.match(line)
            if m:
                continue

            # Processes the matched patterns for the fourth, and repeating, lines of output
            #  Gi1                      1        0/0       0/0          20       0/0           84           0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                interface_short = group['interface']
                interface_long = Common.convert_intf_name(interface_short)
                int_dict = instance_dict.setdefault('interface', {}).setdefault(interface_long, {})
                int_dict['peers'] = int(group['peers'])
                int_dict['xmit_q_unreliable'] = int(group['xmit_q_unreliable'])
                int_dict['xmit_q_reliable'] = int(group['xmit_q_reliable'])
                int_dict['peer_q_unreliable'] = int(group['peer_q_unreliable'])
                int_dict['peer_q_reliable'] = int(group['peer_q_reliable'])
                int_dict['mean_srtt'] = int(group['mean_srtt'])
                int_dict['pacing_time_unreliable'] = int(group['pacing_t_unreliable'])
                int_dict['pacing_time_reliable'] = int(group['pacing_t_reliable'])
                int_dict['mcast_flow_timer'] = int(group['mcast_flow_timer'])
                int_dict['pend_routes'] = int(group['pend_routes'])
                continue

            # Hello-interval is 5, Hold-time is 15
            m = p5.match(line)
            if m:
                group = m.groupdict()
                int_dict.update({'hello_interval': int(group['hello_interval'])})
                int_dict.update({'hold_time': int(group['hold_time'])})
                continue

            # Split-horizon is enabled
            m = p6.match(line)
            if m:
                group = m.groupdict()
                if group['state'] == 'enabled':
                    split_horizon_state = True
                else:
                    split_horizon_state = False
                int_dict.update({'split_horizon_enabled': split_horizon_state})
                continue

            # Packetized sent/expedited: 0/0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                int_dict.update({'packetized_sent': int(group['sent'])})
                int_dict.update({'packetized_expedited': int(group['expedited'])})
                continue

            # Hello's sent/expedited: 597/1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                int_dict.update({'hello_sent': int(group['sent'])})
                int_dict.update({'hello_expedited': int(group['expedited'])})
                continue

            #  Un/reliable mcasts: 0/0  Un/reliable ucasts: 0/0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                int_dict.update({'unreliable_mcasts': int(group['unreliable_mcast'])})
                int_dict.update({'reliable_mcasts': int(group['reliable_mcast'])})
                int_dict.update({'unreliable_ucasts': int(group['unreliable_ucast'])})
                int_dict.update({'reliable_ucasts': int(group['reliable_ucast'])})
                continue

            # Mcast exceptions: 0  CR packets: 0  ACKs suppressed: 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                int_dict.update({'mcast_exceptions': int(group['mcast_exception'])})
                int_dict.update({'cr_packets': int(group['cr_packets'])})
                int_dict.update({'acks_suppressed': int(group['ack_suppressed'])})
                continue

            #   Retransmissions sent: 0  Out-of-sequence rcvd: 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                int_dict.update({'retransmissions_sent': int(group['retransmission_sent'])})
                int_dict.update({'out_of_sequence_rcvd': int(group['out_of_sequence_rcvd'])})
                continue

            #   Authentication mode is not set
            #   Authentication mode is md5,  key-chain is "test"
            m = p12.match(line)
            if m:
                group = m.groupdict()
                if group['authentication'] != 'not':
                    int_dict.update({'authentication_mode': group['authentication']})
                    if group['key_chain'] != 'not':
                        int_dict.update({'key_chain': group['key_chain']})
                continue

        return parsed_dict


class ShowIpEigrpTopologySchema(MetaParser):
    ''' Schema for:
        * 'show ip eigrp topology'
        * 'show ip eigrp vrf <vrf> topology'
        * 'show ipv6 eigrp topology'
        * 'show ipv6 eigrp vrf <vrf> topology'
    '''

    schema = {
        'eigrp_instance': {
            Any(): {
                'vrf': {
                    Any(): {
                        'address_family': {
                            Any(): {
                                'eigrp_id': {
                                    Any(): {
                                        'eigrp_routes': {
                                            Any(): {
                                                'route_code': str,
                                                'route_type': str,
                                                'route': str,
                                                'successor_count': int,
                                                'FD': int,
                                                'known_via': str,
                                                Optional('outgoing_interface'): str,
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

class ShowEigrpTopologySuperParser(ShowIpEigrpTopologySchema):
    '''Parser for:
    show ip eigrp topology
    show ip eigrp vrf <vrf> topology
    show ipv6 eigrp topology
    show ipv6 eigrp vrf <vrf topology>
    '''

    def cli(self, address_family='', vrf='', output=None):
        route_code_dict = {}
        # Codes: P - Passive, A - Active, U - Update, Q - Query, R - Reply,
        # r - reply Status, s - sia Status
        route_code_dict['Passive'] = ['P']
        route_code_dict['Active'] = ['A']
        route_code_dict['Update'] = ['U']
        route_code_dict['Query'] = ['Q']
        route_code_dict['Reply'] = ['R']
        route_code_dict['reply_Status'] = ['r']
        route_code_dict['sia_Status'] = ['s']

        # EIGRP-IPv4 Topology Table for AS(10)/ID(10.169.0.2)
        # EIGRP-IPv4 Topology Table for AS(10)/ID(10.169.0.2) VRF(red)
        # EIGRP-IPv4 VR(test) Topology Table for AS(100)/ID(10.114.254.5)
        r1 = re.compile(r'^EIGRP\-(?P<address_family>IPv4|IPv6)\s*(VR\((?P<process_name>\w+)\))?\s*'
                        r'Topology\s*Table\s*for\s*\w+\(\s*(?P<as_num>\d+)\)\/\w+\(\s*(?P<eigrp_id>\S+)\)'
                        r'\s*(?:VRF\((?P<vrf>\S+)\))?$')

        # Topology(base) TID(0) VRF(1)
        r1_2 = re.compile(r'(Topology\((?P<topology_base>\w+)\)\s+TID\((?P<topology_id>\d+)\)\s+)\s*(?:VRF\((?P<vrf>\S+)\))$')

        # IPv6-EIGRP Topology Table for AS(1)/ID(2001:0DB8:10::/64)
        # IPv6-EIGRP Topology Table for AS(1)/ID(2001:0DB8:10::/64) VRF(red)
        r2 = re.compile(r'^(?P<address_family>IPv4|IPv6)\-EIGRP\s*'
        'Topology\s*Table\s*for\s*\w+\(\s*(?P<as_num>\d+)\)\/\w+\(\s*(?P<eigrp_id>\S+)\)\s*'
        '(?:VRF\((?P<vrf>\S+)\))?$')

        # P 10.169.0.0/16, 1 successors, FD is 2816
        # P 10.36.3.3/32, 1 successors, FD is 130816
        # P 10.4.1.1/32, 1 successors, FD is 2816, tag is 900
        # P 2001:0DB8:3::/64, 1 successors, FD is 281600
        r3 = re.compile(r'^(?P<code>[\w\*]+)\s*(?P<network>\S+),\s*'
        '(?P<successor_count>[\d])\s*successors,\s*FD\s*is\s*(?P<fd>[\d]+)?,'
        '?( +tag\s*is\s*(?P<tag>[\S]+))?$')

        # via Connected, GigabitEthernet0/0/0
        # via 10.169.0.1 (130816/128256), GigabitEthernet0/0/0
        # via +Redistributed (2816/0)
        # via Connected, Ethernet1/0
        r4 = re.compile(r'^\s*via\s*[+]?(?P<known_via>[\S]+).,*? *\(?(?P<route_preference>[\d\/]+)?\)?,?( +(?P<interface>[\S]+))?$')

        parsed_dict = {}
        eigrp_instance = vrf = as_num = eigrp_id = ''

        # Get output
        out = output

        for line in out.splitlines():
            line = line.strip()
            
            # EIGRP-IPv4 Topology Table for AS(10)/ID(10.169.0.2)
            # EIGRP-IPv4 Topology Table for AS(10)/ID(10.169.0.2) VRF(red)
            # EIGRP-IPv4 VR(test) Topology Table for AS(100)/ID(10.114.254.5)
            result = r1.match(line)
            if result:
                address_family = result.groupdict()['address_family']
                as_num = result.groupdict()['as_num']
                eigrp_id = result.groupdict()['eigrp_id']

                if result.groupdict()['vrf']:
                    vrf = result.groupdict()['vrf']
                else:
                    vrf = 'default'
                continue

            # Topology(base) TID(0) VRF(1)
            result = r1_2.match(line)
            if result:
                if result.groupdict()['vrf']:
                    vrf = result.groupdict()['vrf']
                else:
                    vrf = 'default'
                continue

            # IPv6-EIGRP Topology Table for AS(1)/ID(2001:0DB8:10::/64)
            # IPv6-EIGRP Topology Table for AS(1)/ID(2001:0DB8:10::/64) VRF(red)
            result = r2.match(line)
            if result:
                address_family = result.groupdict()['address_family']
                as_num = result.groupdict()['as_num']
                eigrp_id = result.groupdict()['eigrp_id']

                if result.groupdict()['vrf']:
                    vrf = result.groupdict()['vrf']
                else:
                    vrf = 'default'
                continue

            # P 10.169.0.0/16, 1 successors, FD is 2816
            # P 10.36.3.3/32, 1 successors, FD is 130816
            # P 10.4.1.1/32, 1 successors, FD is 2816, tag is 900
            # P 2001:0DB8:3::/64, 1 successors, FD is 281600
            result = r3.match(line)
            if result:
                route_prefix = result.groupdict()['network']

                route_dict = parsed_dict\
                    .setdefault('eigrp_instance', {})\
                    .setdefault(as_num, {})\
                    .setdefault('vrf', {})\
                    .setdefault(vrf, {})\
                    .setdefault('address_family', {})\
                    .setdefault(address_family, {})\
                    .setdefault('eigrp_id', {})\
                    .setdefault(eigrp_id, {})\
                    .setdefault('eigrp_routes', {})\
                    .setdefault(route_prefix, {})
                
                route_code = result.groupdict()['code'].strip()
                successor_count = int(result.groupdict()['successor_count'])
                fd = int(result.groupdict()['fd'])
                for key, value in route_code_dict.items():
                    if route_code in value:
                        route_type = key
                
                route_dict['route_code'] = route_code
                route_dict['successor_count'] = successor_count
                route_dict['FD'] = fd
                route_dict['route_type'] = route_type
                route_dict['route'] = route_prefix
                continue
            
            # via Connected, GigabitEthernet0/0/0
            # via 10.169.0.1 (130816/128256), GigabitEthernet0/0/0
            # via +Redistributed (2816/0)
            # via Connected, Ethernet1/0
            result = r4.match(line)
            if result:
                known_via = result.groupdict()['known_via']
                if result.groupdict()['interface']:
                    outgoing_interface = result.groupdict()['interface']
                    route_dict['outgoing_interface'] = outgoing_interface

                route_dict['known_via'] = known_via
                continue


        return parsed_dict


class ShowIpEigrpInterfaces(ShowEigrpInterfacesSuperParser, ShowEigrpInterfacesSchema):

    '''
    Parser for:
        "show ip eigrp interfaces"
        "show ip eigrp vrf <vrf> interfaces"
    '''

    cli_command = ['show ip eigrp vrf {vrf} interfaces',
                    'show ip eigrp interfaces']

    # Defines a function to run the cli_command
    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        return super().cli(output=out, vrf=vrf)


class ShowIpv6EigrpInterfaces(ShowEigrpInterfacesSuperParser, ShowEigrpInterfacesSchema):

    ''' Parser for "show ipv6 eigrp interfaces"'''

    cli_command = 'show ipv6 eigrp interfaces'

    # Defines a function to run the cli_command
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return super().cli(output=out)


class ShowIpEigrpInterfacesDetail(ShowEigrpInterfacesSuperParser, ShowEigrpInterfacesSchema):

    ''' Parser for "show ip eigrp interfaces detail"'''

    cli_command = 'show ip eigrp interfaces detail'

    # Defines a function to run the cli_command
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return super().cli(output=out)


class ShowIpv6EigrpInterfacesDetail(ShowEigrpInterfacesSuperParser, ShowEigrpInterfacesSchema):

    ''' Parser for "show ipv6 eigrp interfaces detail"'''

    cli_command = 'show ipv6 eigrp interfaces detail'

    # Defines a function to run the cli_command
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return super().cli(output=out)


# ===============================================
# Parser for:
#   * 'show ip eigrp vrf {vrf} topology'
#   * 'show ip eigrp topology'
# ===============================================
class ShowIpEigrpTopology(ShowEigrpTopologySuperParser, ShowIpEigrpTopologySchema):
    cli_command = ['show ip eigrp vrf {vrf} topology',
                    'show ip eigrp topology',]

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
            
            output = self.device.execute(cmd)
        
        return super().cli(output=output, address_family='ipv4', vrf=vrf)


# ===============================================
# Parser for:
#   * 'show ipv6 eigrp vrf {vrf} neighbors'
#   * 'show ipv6 eigrp neighbors'
# ===============================================
class ShowIpv6EigrpTopology(ShowEigrpTopologySuperParser, ShowIpEigrpTopologySchema):
    cli_command = ['show ipv6 eigrp vrf {vrf} topology',
                    'show ipv6 eigrp topology',]

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]

            output = self.device.execute(cmd)
        
        return super().cli(output=output, address_family='ipv4', vrf=vrf)
