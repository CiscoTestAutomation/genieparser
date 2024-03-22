''' show_l2vpn.py

IOSXE parsers for the following show commands:

    * show bridge-domain
    * show bridge-domain <BD_ID>
    * show bridge-domain | count <WORD>
    * show ethernet service instance detail
    * show ethernet service instance interface <interface> detail
    * show l2vpn vfi
    * show l2vpn vfi name {name} detail
    * show vfi name {name}
    * show l2vpn service all
    * show l2vpn service interface {interface}
    * show l2vpn service name {name}
    * show l2vpn service xconnect all
    * show l2vpn service xconnect interface {interface}
    * show l2vpn service xconnect name {name}
    * show ethernet service instance
    * show ethernet service instance id {service_instance_id} interface {interface} detail
    * show ethernet service instance id {service_instance_id} interface {interface} stats
    * show l2vpn atom preferred-path
    * show l2vpn evpn ethernet-segment detail
    * show l2vpn evpn ethernet-segment interface {interface} detail
    * show l2vpn evpn ethernet-segment
    * show l2vpn evpn mac
    * show l2vpn evpn mac address {mac_addr}
    * show l2vpn evpn mac address {mac_addr} detail
    * show l2vpn evpn mac bridge-domain {bd_id}
    * show l2vpn evpn mac bridge-domain {bd_id} address {mac_addr}
    * show l2vpn evpn mac bridge-domain {bd_id} address {mac_addr} detail
    * show l2vpn evpn mac bridge-domain {bd_id} detail
    * show l2vpn evpn mac bridge-domain {bd_id} duplicate
    * show l2vpn evpn mac bridge-domain {bd_id} duplicate detail
    * show l2vpn evpn mac bridge-domain {bd_id} duplicate summary
    * show l2vpn evpn mac bridge-domain {bd_id} local
    * show l2vpn evpn mac bridge-domain {bd_id} local detail
    * show l2vpn evpn mac bridge-domain {bd_id} local summary
    * show l2vpn evpn mac bridge-domain {bd_id} remote
    * show l2vpn evpn mac bridge-domain {bd_id} remote detail
    * show l2vpn evpn mac bridge-domain {bd_id} remote summary
    * show l2vpn evpn mac bridge-domain {bd_id} summary
    * show l2vpn evpn mac detail
    * show l2vpn evpn mac duplicate
    * show l2vpn evpn mac duplicate detail
    * show l2vpn evpn mac duplicate summary
    * show l2vpn evpn mac evi {evi_id}
    * show l2vpn evpn mac evi {evi_id} address {mac_addr}
    * show l2vpn evpn mac evi {evi_id} address {mac_addr} detail
    * show l2vpn evpn mac evi {evi_id} detail
    * show l2vpn evpn mac evi {evi_id} duplicate
    * show l2vpn evpn mac evi {evi_id} duplicate detail
    * show l2vpn evpn mac evi {evi_id} duplicate summary
    * show l2vpn evpn mac evi {evi_id} local
    * show l2vpn evpn mac evi {evi_id} local detail
    * show l2vpn evpn mac evi {evi_id} local summary
    * show l2vpn evpn mac evi {evi_id} remote
    * show l2vpn evpn mac evi {evi_id} remote detail
    * show l2vpn evpn mac evi {evi_id} remote summary
    * show l2vpn evpn mac evi {evi_id} summary
    * show l2vpn evpn mac local
    * show l2vpn evpn mac local detail
    * show l2vpn evpn mac local summary
    * show l2vpn evpn mac remote
    * show l2vpn evpn mac remote detail
    * show l2vpn evpn mac remote summary
    * show l2vpn evpn mac summary
    * show l2vpn evpn mac ip
    * show l2vpn evpn mac ip address {ipv4_addr}
    * show l2vpn evpn mac ip address {ipv4_addr} detail
    * show l2vpn evpn mac ip address {ipv6_addr}
    * show l2vpn evpn mac ip address {ipv6_addr} detail
    * show l2vpn evpn mac ip bridge-domain {bd_id}
    * show l2vpn evpn mac ip bridge-domain {bd_id} address {ipv4_addr}
    * show l2vpn evpn mac ip bridge-domain {bd_id} address {ipv4_addr}  detail
    * show l2vpn evpn mac ip bridge-domain {bd_id} address {ipv6_addr}
    * show l2vpn evpn mac ip bridge-domain {bd_id} address {ipv6_addr} detail
    * show l2vpn evpn mac ip bridge-domain {bd_id} detail
    * show l2vpn evpn mac ip bridge-domain {bd_id} duplicate
    * show l2vpn evpn mac ip bridge-domain {bd_id} duplicate detail
    * show l2vpn evpn mac ip bridge-domain {bd_id} duplicate summary
    * show l2vpn evpn mac ip bridge-domain {bd_id} local
    * show l2vpn evpn mac ip bridge-domain {bd_id} local detail
    * show l2vpn evpn mac ip bridge-domain {bd_id} local summary
    * show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr}
    * show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ipv4_addr}
    * show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ipv4_addr} detail
    * show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ipv6_addr}
    * show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ipv6_addr} detail
    * show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} detail
    * show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} summary
    * show l2vpn evpn mac ip bridge-domain {bd_id} remote
    * show l2vpn evpn mac ip bridge-domain {bd_id} remote detail
    * show l2vpn evpn mac ip bridge-domain {bd_id} remote summary
    * show l2vpn evpn mac ip bridge-domain {bd_id} summary
    * show l2vpn evpn mac ip detail
    * show l2vpn evpn mac ip duplicate
    * show l2vpn evpn mac ip duplicate detail
    * show l2vpn evpn mac ip duplicate summary
    * show l2vpn evpn mac ip evi {evi_id}
    * show l2vpn evpn mac ip evi {evi_id} address {ipv4_addr}
    * show l2vpn evpn mac ip evi {evi_id} address {ipv4_addr} detail
    * show l2vpn evpn mac ip evi {evi_id} address {ipv6_addr}
    * show l2vpn evpn mac ip evi {evi_id} address {ipv6_addr} detail
    * show l2vpn evpn mac ip evi {evi_id} detail
    * show l2vpn evpn mac ip evi {evi_id} duplicate
    * show l2vpn evpn mac ip evi {evi_id} duplicate detail
    * show l2vpn evpn mac ip evi {evi_id} duplicate summary
    * show l2vpn evpn mac ip evi {evi_id} local
    * show l2vpn evpn mac ip evi {evi_id} local detail
    * show l2vpn evpn mac ip evi {evi_id} local summary
    * show l2vpn evpn mac ip evi {evi_id} mac {mac_addr}
    * show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ipv4_addr}
    * show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ipv4_addr} detail
    * show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ipv6_addr}
    * show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ipv6_addr} detail
    * show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} detail
    * show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} summary
    * show l2vpn evpn mac ip evi {evi_id} remote
    * show l2vpn evpn mac ip evi {evi_id} remote detail
    * show l2vpn evpn mac ip evi {evi_id} remote summary
    * show l2vpn evpn mac ip evi {evi_id} summary
    * show l2vpn evpn mac ip local
    * show l2vpn evpn mac ip local detail
    * show l2vpn evpn mac ip local summary
    * show l2vpn evpn mac ip mac {mac_addr}
    * show l2vpn evpn mac ip mac {mac_addr} address {ipv4_addr}
    * show l2vpn evpn mac ip mac {mac_addr} address {ipv4_addr} detail
    * show l2vpn evpn mac ip mac {mac_addr} address {ipv6_addr}
    * show l2vpn evpn mac ip mac {mac_addr} address {ipv6_addr} detail
    * show l2vpn evpn mac ip mac {mac_addr} detail
    * show l2vpn evpn mac ip mac {mac_addr} summary
    * show l2vpn evpn mac ip remote
    * show l2vpn evpn mac ip remote detail
    * show l2vpn evpn mac ip remote summary
    * show l2vpn evpn mac ip summary
    * show storm-control
    * show storm-control {interface}
    * show l2vpn evpn mac vlan {vlan_id}
    * show l2vpn evpn mac vlan {vlan_id} address {mac_addr}
    * show l2vpn evpn mac vlan {vlan_id} duplicate
    * show l2vpn evpn mac vlan {vlan_id} local
    * show l2vpn evpn mac vlan {vlan_id} remote
    * show l2vpn evpn mac ip vlan {vlan_id}
    * show l2vpn evpn mac ip vlan {vlan_id} address {ipv4_addr}
    * show l2vpn evpn mac ip vlan {vlan_id} address {ipv6_addr}
    * show l2vpn evpn mac ip vlan {vlan_id} duplicate
    * show l2vpn evpn mac ip vlan {vlan_id} local
    * show l2vpn evpn mac ip vlan {vlan_id} mac {mac_addr}
    * show l2vpn evpn mac ip vlan {vlan_id} mac {mac_addr} address {ipv4_addr}
    * show l2vpn evpn mac ip vlan {vlan_id} mac {mac_addr} address {ipv6_addr}
    * show l2vpn evpn mac ip vlan {vlan_id} remote
    * show l2vpn evpn default-gateway detail
    * show l2vpn evpn default-gateway summary
    * show l2vpn evpn default-gateway evi <evi_id> detail
    * show l2vpn evpn default-gateway evi <evi_id> summary
    * show l2vpn evpn default-gateway bridge-domain {bd_id} detail
    * show l2vpn evpn default-gateway bridge-domain {bd_id} summary
    * show l2vpn evpn default-gateway vlan <vlan_id> detail
    * show l2vpn evpn default-gateway vlan <vlan_id> summary
    * show l2vpn evpn peers vxlan detail
    * show l2vpn evpn peers vxlan address <peer_addr> detail
    * show l2vpn evpn peers vxlan global detail
    * show l2vpn evpn peers vxlan global address <peer_addr> detail
    * show l2vpn evpn peers vxlan vni <vni_id> detail
    * show l2vpn evpn peers vxlan vni <vni_id> address <peer_addr> detail
    * show l2vpn evpn peers vxlan interface <nve_interface> detail
    * show l2vpn evpn peers vxlan interface <nve_interface> address <peer_addr> detail
    * show l2vpn evpn summary
    * show l2vpn evpn evi detail
    * show l2vpn evpn evi <evi> detail
    * show l2vpn evpn multicast local
    * show l2vpn evpn multicast remote
    * show l2vpn evpn capabilities
    * show running-config | section l2vpn evpn
    * show l2vpn evpn vpws vc id detail
    * show l2vpn evpn vpws vc id <vc_id> detail
    * show l2vpn evpn vpws vc preferred-path
    * show l2vpn evpn default-gateway

Copyright (c) 2021 by Cisco Systems, Inc.
All rights reserved.
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use
from genie.parsergen import oper_fill_tabular
# import parser utils
from genie.libs.parser.utils.common import Common

# ====================================
# Parser for 'show bridge-domain'
# ====================================
class ShowBridgeDomainSchema(MetaParser):
    """Schema for show bridge-domain
                  show bridge-domain <BD_ID>
                  show bridge-domain | count <WORD>"""

    schema = {
        Optional('lines_match_regexp'): int,
        Optional('bridge_domain'): {
            Any(): {
                'number_of_ports_in_all': int,
                'bd_domain_id': int,
                'aging_timer': int,
                'state': str,
                'mac_learning_state': str,
                Optional('member_ports'): list,
                Any(): {
                    Any(): {
                        'num_of_ports': str,
                        'interfaces': list,
                    },
                },
                Optional('mac_table'): {
                    Any(): {
                        'pseudoport': str,
                        'mac_address': {
                            Any(): {
                                'mac_address': str,
                                'aed': int,
                                'policy': str,
                                'tag': str,
                                'age': int,
                            },
                        }
                    },
                }
            },
        }
    }


class ShowBridgeDomain(ShowBridgeDomainSchema):
    """Parser for show bridge-domain
                  show bridge-domain <BD_ID>
                  show bridge-domain | count <WORD>"""

    cli_command = ['show bridge-domain', 'show bridge-domain {bd_id}', 'show bridge-domain | count {word}']

    def cli(self, bd_id=None, word=None, output=None):
        cli = self.cli_command
        if output is None:
            if bd_id:
                cli = self.cli_command[1].format(bd_id=bd_id)
            elif word:
                cli = self.cli_command[2].format(word=word)
            else:
                cli = self.cli_command[0]
            out = self.device.execute(cli)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # Bridge-domain 2051 (2 ports in all)
        p1 = re.compile(r'^Bridge-domain +(?P<bridge_domain>\d+) +\((?P<number_of_ports_in_all>\d+) +ports +in +all\)$')

        # State: UP                    Mac learning: Enabled
        p2 = re.compile(r'^State: +(?P<state>\w+) +Mac +learning: +(?P<mac_learning_state>\w+)$')

        # Aging-Timer: 3600 second(s)
        p3 = re.compile(r'^Aging-Timer: +(?P<aging_timer>\d+) +second\(s\)$')

        # Load for five secs: 10%/1%; one minute: 11%; five minutes: 12%
        p4 = re.compile(r'^Load +for.*$')

        # Time source is NTP, 19:54:46.940 EST Wed Nov 2 2016
        p4_1 = re.compile(r'^Time +source.*$')

        # AED MAC address    Policy  Tag       Age  Pseudoport
        p4_2 = re.compile(r'^AED +MAC +address +Policy +Tag +Age +Pseudoport$')

        # 1 ports belonging to split-horizon group 0
        p5 = re.compile(r'^(?P<num_of_ports>\d+) +ports +belonging +to +(?P<port_belonging_group>[\w\-\d]+) +group +(?P<group_number>\d+)$')

        #     vfi VPLS-2051 neighbor 10.120.202.64 2051
        #     Port-channel1 service instance 2051 (split-horizon)
        #     GigabitEthernet0/0/3 service instance 3051 (split-horizon)
        #    -   000C.29FF.4971 forward static_r  0    OCE_PTR:0xe8e5dda0
        p6 = re.compile(r'^(?P<member_port>[\w\d\-\/\s\.:]+)( +\(.*\))?$')

        #    AED MAC address    Policy  Tag       Age  Pseudoport
        #    0   0000.A0FF.0027 forward dynamic   3142 Port-channel1.EFP2051
        #    0   0000.A0FF.00F2 forward dynamic   3438 GigabitEthernet0/0/3.EFP3051
        #    -   000C.29FF.4971 forward static_r  0    OCE_PTR:0xe8e5dda0
        p7 = re.compile(r'^(?P<aed>[\d-]+) +(?P<mac_address>[\w\d\.]+) +(?P<policy>\w+) +(?P<tag>\w+)'
                         ' +(?P<age>\d+) +(?P<pseudoport>[\w\d\-\.\/:]+)$')

        # Number of lines which match regexp = 32000
        p8 = re.compile(r'^Number +of +lines +which +match +regexp += +(?P<lines_match_regexp>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                bridge_domain = int(group['bridge_domain'])
                member_port_list = []
                final_dict = ret_dict.setdefault('bridge_domain', {}).\
                    setdefault(bridge_domain, {})
                final_dict['number_of_ports_in_all'] = int(
                    group['number_of_ports_in_all'])
                final_dict['bd_domain_id'] = int(group['bridge_domain'])
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                final_dict.update({k:v for k, v in group.items()})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                final_dict.update({k:int(v) for k, v in group.items()})
                continue

            m = p4.match(line)
            if m:
                continue

            m = p4_1.match(line)
            if m:
                continue

            m = p4_2.match(line)
            if m:
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                num_of_ports = group['num_of_ports']
                port_belonging_group = group['port_belonging_group']+'_group'
                group_number = group['group_number']
                final_dict.setdefault(port_belonging_group, {})
                final_dict[port_belonging_group].setdefault(group_number, {})
                final_dict[port_belonging_group][group_number]['num_of_ports'] = num_of_ports
                ret_dict['interfaces'] = []
                continue

            m = p6.match(line)
            if m:
                m_2 = p7.match(line)
                if m_2:
                    group = m_2.groupdict()
                    pseudoport = group['pseudoport']
                    mac_address = group['mac_address']
                    final_dict.setdefault('mac_table', {}).setdefault(
                        pseudoport, {}).setdefault(
                            'mac_address', {}).setdefault(mac_address, {})
                    final_dict['mac_table'][pseudoport]['pseudoport'] = pseudoport
                    final_dict['mac_table'][pseudoport]['mac_address']\
                        [mac_address]['mac_address'] = mac_address
                    final_dict['mac_table'][pseudoport]['mac_address']\
                        [mac_address]['aed'] = 0 if group['aed'] == '-' else int(group['aed'])
                    final_dict['mac_table'][pseudoport]['mac_address']\
                        [mac_address]['policy'] = group['policy']
                    final_dict['mac_table'][pseudoport]['mac_address']\
                        [mac_address]['tag'] = group['tag']
                    final_dict['mac_table'][pseudoport]['mac_address']\
                        [mac_address]['age'] = int(group['age'])
                    continue

                group = m.groupdict()
                if 'interfaces' in ret_dict and port_belonging_group in final_dict:
                    ret_dict['interfaces'].append(group['member_port'])
                    final_dict[port_belonging_group][group_number]\
                        ['interfaces'] = ret_dict['interfaces']
                member_port_list.append(group['member_port'])
                final_dict['member_ports'] = member_port_list
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict['lines_match_regexp'] = int(group['lines_match_regexp'])
                continue

        if 'interfaces' in ret_dict:
            del ret_dict['interfaces']

        return ret_dict


# ==================================================
# Parser for 'show ethernet service instance detail'
# ==================================================
class ShowEthernetServiceInstanceDetailSchema(MetaParser):
    """Schema for show ethernet service instance
                  show ethernet service instance detail
                  show ethernet service instance interface <interface> detail
    """

    schema = {
        'service_instance': {
            Any(): {
                'interfaces': {
                    Any(): {
                        Optional('type'): str,
                        Optional('description'): str,
                        Optional('associated_evc'): str,
                        Optional('l2protocol_drop'): bool,
                        Optional('ce_vlans'): str,
                        Optional('encapsulation'): str,
                        Optional('rewrite'): str,
                        Optional('control_policy'): str,
                        Optional('intiators'): str,
                        Optional('dot1q_tunnel_ethertype'): str,
                        Optional('state'): str,
                        Optional('efp_statistics'): {
                            'pkts_in': int,
                            'pkts_out': int,
                            'bytes_in': int,
                            'bytes_out': int,
                        },
                        Optional('micro_block_type'): {
                            Any(): {
                                Any(): Any()
                            }
                        },
                        Optional('l2_acl'): {
                            Optional('inbound'): str,
                            Optional('permit_count'): int,
                            Optional('deny_count'): int,
                        },
                    }
                }
            },
        }
    }

class ShowEthernetServiceInstanceDetail(ShowEthernetServiceInstanceDetailSchema):
    """Parser for show ethernet service instance detail
                  show ethernet service instance interface <interface> detail
                  show ethernet service instance id {service_instance_id} interface {interface} detail
    """

    cli_command = [
        'show ethernet service instance detail', 
        'show ethernet service instance interface {interface} detail',
        'show ethernet service instance id {service_instance_id} interface {interface} detail']

    def cli(self, service_instance_id=None, interface=None, output=None):
        if output is None:
            if service_instance_id and interface:
                cli = self.cli_command[2].format(service_instance_id=service_instance_id, 
                    interface=interface)
            elif interface:
                cli = self.cli_command[1].format(interface=interface)
            else:
                cli = self.cli_command[0]
            out = self.device.execute(cli)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}
        sub_dict = {}
        final_dict = {}
        # initial regexp pattern
        # Service Instance ID: 2051
        p1 = re.compile(r'^Service +Instance +ID: +(?P<service_id>\d+)$')

        # Service Instance Type: Static
        # Service instance type: L2Context
        p2 = re.compile(r'^Service +(i|I)nstance +(t|T)ype: +(?P<service_instance_type>\S+)$')

        # Description: xxx
        # Description: Fiber Connexion to XXX-111-1111
        p3 = re.compile(r'^Description: +(?P<description>[\S\s]+)$')

        # Associated Interface: GigabitEthernet0/0/3
        p4 = re.compile(r'^Associated +Interface: +(?P<associated_interface>[\w\d\-\.\/]+)$')

        # Associated EVC: 
        p5 = re.compile(r'^Associated +EVC: +(?P<associated_evc>\S+)$')

        # L2protocol drop
        p6 = re.compile(r'^L2protocol +drop$')

        # CE-Vlans: 10-20                                                                        
        p7 = re.compile(r'^CE-Vlans: +(?P<vlans>\S+)$')

        # Encapsulation: dot1q 2051 vlan protocol type 0x8100
        p8 = re.compile(r'^Encapsulation: +(?P<encapsulation>[\S\s]+)$')

        # Rewrite: egress tag translate 1-to-1 dot1q 2051 vlan-type 0x8100
        p9 = re.compile(r'^Rewrite: +(?P<rewrite>[\S\s]+)$')

        # Interface Dot1q Tunnel Ethertype: 0x8100
        p10 = re.compile(r'^Interface Dot1q Tunnel Ethertype: +(?P<dot1q_tunnel_ethertype>\S+)$')

        # State: Up
        p11 = re.compile(r'^State: +(?P<state>\w+)$')

        # EFP Statistics:
        p12 = re.compile(r'^EFP Statistics:$')

        #    Pkts In   Bytes In   Pkts Out  Bytes Out
        #          0          0          0          0
        p13 = re.compile(r'^(?P<pkts_in>\d+) +(?P<bytes_in>\d+) +(?P<pkts_out>\d+) +(?P<bytes_out>\d+)$')

        # Intiators: unclassified vlan
        p14 = re.compile(r'^Intiators: +(?P<intiators>[\S\s]+)$')

        # Control policy: ABC
        p15 = re.compile(r'^Control +policy: +(?P<control_policy>[\S\s]+)$')

        # 1   Static GigabitEthernet0/0/3       Up
        p16 = re.compile(r'^(?P<service_id>\d+) +(?P<service_instance_type>\w+) +'
            '(?P<associated_interface>\S+) +(?P<state>\w+)( +(?P<vlans>\S+))?$')

        # Microblock type: Storm-Control
        p17 = re.compile(r'^Microblock +type: +(?P<micro_block_type>[\S ]+)$')

        # storm-control unicast cir 8001
        # storm-control broadcast cir 8001
        # storm-control multicast cir 8001
        p18 = re.compile(r'^(?P<key>storm-control +\S+ +\S+) +(?P<val>\d+)$')

        # Load for five secs: 2%/0%; one minute: 5%; five minutes: 4%
        p19 = re.compile(r'^Load +for +\w+ +\w+: [\S ]+$')

        # L2 ACL (inbound): test-acl
        p20 = re.compile(r'^L2 +ACL +\((?P<key>\w+)\): +(?P<val>\S+)$')
        
        # L2 ACL permit count: 10255
        # L2 ACL deny count: 53
        p21 = re.compile(r'^L2 +ACL +(?P<key>(permit|deny) +count): +(?P<val>\d+)$')
        
        # Bridge-domain: 12-1900
        # L2 Multicast GID: 9
        p22 = re.compile(r'^(?P<key>[\S+ ]+): +(?P<val>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            
            # Service Instance ID: 2051
            m = p1.match(line)
            if m:
                sub_dict = {}
                group = m.groupdict()
                service_instance_id = int(group['service_id'])
                continue
            
            # Service Instance Type: Static
            # Service instance type: L2Context
            m = p2.match(line)
            if m:
                group = m.groupdict()
                sub_dict['type'] = group['service_instance_type']
                continue

            # Description: xxx
            m = p3.match(line)
            if m:
                group = m.groupdict()
                sub_dict['description'] = group['description']
                continue

            # Associated Interface: GigabitEthernet0/0/3
            m = p4.match(line)
            if m:
                group = m.groupdict()
                final_dict = ret_dict.setdefault('service_instance', {}).\
                    setdefault(service_instance_id, {}).\
                    setdefault('interfaces', {}).\
                    setdefault(group['associated_interface'], sub_dict)
                continue

            # Associated EVC: 
            m = p5.match(line)
            if m:
                group = m.groupdict()
                sub_dict['associated_evc'] = group['associated_evc']
                continue

            # L2protocol drop
            m = p6.match(line)
            if m:
                sub_dict['l2protocol_drop'] = True
                continue

            # CE-Vlans: 10-20
            m = p7.match(line)
            if m:
                group = m.groupdict()
                sub_dict['ce_vlans'] = group['vlans']
                continue

            # Encapsulation: dot1q 2051 vlan protocol type 0x8100
            m = p8.match(line)
            if m:
                group = m.groupdict()
                sub_dict['encapsulation'] = group['encapsulation']
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                sub_dict['rewrite'] = group['rewrite']
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                sub_dict['dot1q_tunnel_ethertype'] = group['dot1q_tunnel_ethertype']
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                sub_dict['state'] = group['state']
                continue

            m = p12.match(line)
            if m:
                sub_dict.setdefault('efp_statistics', {})
                continue

            m = p13.match(line)
            if m:
                group = m.groupdict()
                sub_dict['efp_statistics'].update({k: \
                    int(v) for k, v in group.items()})
                continue

            m = p14.match(line)
            if m:
                group = m.groupdict()
                sub_dict['intiators'] = group['intiators']
                continue

            m = p15.match(line)
            if m:
                group = m.groupdict()
                sub_dict['control_policy'] = group['control_policy']
                continue

            # 1   Static GigabitEthernet0/0/3       Up
            m = p16.match(line)
            if m:
                group = m.groupdict()
                service_instance_id = int(group['service_id'])
                
                final_dict = ret_dict.setdefault('service_instance', {}).\
                    setdefault(service_instance_id, {}).\
                    setdefault('interfaces', {}).\
                    setdefault(group['associated_interface'], sub_dict)
                sub_dict['state'] = group['state']
                sub_dict['type'] = group['service_instance_type']
                if group['vlans']:
                    sub_dict['ce_vlans'] = group['vlans'] 

                continue
            
            # Microblock type: Storm-Control
            m = p17.match(line)
            if m:
                if not final_dict:
                    final_dict = ret_dict.setdefault('service_instance', {}).\
                        setdefault(service_instance_id, {}).\
                        setdefault('interfaces', {}).\
                        setdefault(interface, sub_dict)

                group = m.groupdict()
                micro_block_type = group['micro_block_type']
                micro_block_dict = sub_dict.setdefault('micro_block_type', {}).\
                    setdefault(micro_block_type, {})
                continue
            
            # storm-control unicast cir 8001
            m = p18.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].lower().replace(' ', '_').\
                    replace('-', '_')
                storm_control_list =  micro_block_dict.\
                    setdefault(key, group['val'])
                continue

            # Load for five secs: 2%/0%; one minute: 5%; five minutes: 4%
            m = p19.match(line)
            if m:
                continue
            
            # L2 ACL (inbound): test-acl
            m = p20.match(line)
            if m:
                group = m.groupdict()
                sub_dict.setdefault('l2_acl', {}).\
                    setdefault(group['key'], group['val'])
                continue

            # L2 ACL permit count: 10255
            # L2 ACL deny count: 53
            m = p21.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].lower().replace(' ', '_').\
                    replace('-', '_')
                sub_dict.setdefault('l2_acl', {}).\
                    setdefault(key, int(group['val']))
                continue

            # Bridge-domain: 12-1900
            # L2 Multicast GID: 9
            m = p22.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].lower().replace(' ', '_').\
                    replace('-', '_')
                val = group['val']
                try:
                    micro_block_dict.update({key : int(val)})
                except ValueError:
                    micro_block_dict.update({key : val})
                continue

        return ret_dict

class ShowEthernetServiceInstance(ShowEthernetServiceInstanceDetail):
    """Parser for show ethernet service instance
    """
    cli_command = 'show ethernet service instance'
    def cli(self, interface=None, output=None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output
        return super().cli(output=show_output)

# =================================================
# Parser for 'show ethernet service instance stats'
# =================================================
class ShowEthernetServiceInstanceStatsSchema(MetaParser):
    """Schema for show ethernet service instance stats
                  show ethernet service instance interface <interface> stats
    """

    schema = {
        Optional('max_num_of_service_instances'): int,
        Optional('service_instance'): {
            Any(): {
                'interface': str,
                'pkts_in': int,
                'pkts_out': int,
                'bytes_in': int,
                'bytes_out': int,
                Optional('storm_control_discard_pkts'): {
                    'broadcast': {
                        Any(): int
                    },
                    'multicast': {
                        Any(): int
                    },
                    'unknown_unicast': {
                        Any(): int
                    }
                }
            },
        }
    }


class ShowEthernetServiceInstanceStats(ShowEthernetServiceInstanceStatsSchema):
    """Parser for show ethernet service instance stats
                  show ethernet service instance interface <interface> stats
                  show ethernet service instance id {service_instance_id} interface {interface} stats
    """

    cli_command = ['show ethernet service instance stats', 
        'show ethernet service instance interface {interface} stats',
        'show ethernet service instance id {service_instance_id} interface {interface} stats']

    def cli(self, service_instance_id=None, interface=None, output=None):
        cli = self.cli_command
        if output is None:
            if service_instance_id and interface:
                cli = self.cli_command[2].format(
                    service_instance_id=service_instance_id,
                    interface=interface)
            elif interface:
                cli = self.cli_command[1].format(interface=interface)
            else:
                cli = self.cli_command[0]
            out = self.device.execute(cli)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # System maximum number of service instances: 32768
        p1 = re.compile(r'^\S+ +maximum +number +of +service +instances: +(?P<max_num_of_service_instances>\d+)$')

        # Service Instance 2051, Interface GigabitEthernet0/0/3
        p2 = re.compile(r'^Service +Instance +(?P<service_instance>\d+), Interface +(?P<interface>\S+)$')

        #    Pkts In   Bytes In   Pkts Out  Bytes Out
        #          0          0          0          0
        p3 = re.compile(r'^(?P<pkts_in>\d+) +(?P<bytes_in>\d+) +(?P<pkts_out>\d+) +(?P<bytes_out>\d+)$')
        
        # default:0            default:0            default:0           
        # cos 0:0              cos 0:0              cos 0:0  
        p4 = re.compile(r'^(?P<broadcast_key>(default)|(\w+ +\d+)):(?P<broadcast_value>\d+) +'
                '(?P<multicast_key>(default)|(\w+ +\d+)):(?P<multicast_value>\d+) +'
                '(?P<unknown_unicast_key>(default)|(\w+ +\d+)):(?P<unknown_unicast_value>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['max_num_of_service_instances'] = int(group['max_num_of_service_instances'])
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                service_id = int(group['service_instance'])
                final_dict = ret_dict.setdefault('service_instance', {}).\
                    setdefault(service_id, {})
                final_dict['interface'] = group['interface']
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                final_dict.update({k: int(v) for k, v in group.items()})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                broadcast = final_dict.setdefault('storm_control_discard_pkts', {}).\
                    setdefault('broadcast', {})
                broadcast.update({group['broadcast_key']: int(group['broadcast_value'])})

                multicast = final_dict.setdefault('storm_control_discard_pkts', {}).\
                    setdefault('multicast', {})
                multicast.update({group['multicast_key']: int(group['multicast_value'])})

                unknown_unicast = final_dict.setdefault('storm_control_discard_pkts', {}).\
                    setdefault('unknown_unicast', {})
                unknown_unicast.update({group['unknown_unicast_key']: int(group['unknown_unicast_value'])})

        return ret_dict


# ===================================================
# Parser for 'show ethernet service instance summary'
# ===================================================
class ShowEthernetServiceInstanceSummarySchema(MetaParser):
    """Schema for show ethernet service instance summary
    """

    schema = {
        Any(): {
            Any(): {
                'total': int,
                'up': int,
                'admin_do': int,
                'down': int,
                'error_di': int,
                'unknown': int,
                'deleted': int,
                'bd_adm_do': int,
            },
        },
    }


class ShowEthernetServiceInstanceSummary(ShowEthernetServiceInstanceSummarySchema):
    """Parser for show ethernet service instance summary
    """

    cli_command = 'show ethernet service instance summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # System summary
        p1 = re.compile(r'^System +summary$')
 
        # Associated interface: GigabitEthernet0/0/3
        # Associated interface: Port-channel1
        p2 = re.compile(r'^Associated +interface: +(?P<interface>[\w\d\/\.\-]+)$')

        #             Total       Up  AdminDo     Down  ErrorDi  Unknown  Deleted  BdAdmDo  
        # bdomain         0        0        0        0        0        0        0        0  
        # xconnect        0        0        0        0        0        0        0        0  
        # local sw        0        0        0        0        0        0        0        0  
        # other         201      201        0        0        0        0        0        0  
        # all           201      201        0        0        0        0        0        0  
        p3 = re.compile(r'^(?P<service>[\w\s\d]+) +(?P<total>\d+) +(?P<up>\d+)'
                         ' +(?P<admin_do>\d+) +(?P<down>\d+) +(?P<error_di>\d+)'
                         ' +(?P<unknown>\d+) +(?P<deleted>\d+) +(?P<bd_adm_do>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                header = 'system_summary'
                ret_dict.setdefault(header, {})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                header = group['interface']
                ret_dict.setdefault(header, {})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                service = group.pop('service').strip()
                ret_dict[header].setdefault(service, {})
                ret_dict[header][service].update({k: int(v) for k, v in group.items()})
                continue

        return ret_dict


# ===========================
# Parser for 'show l2vpn vfi'
# ===========================
class ShowL2vpnVfiSchema(MetaParser):
    """Schema for show l2vpn vfi
    """

    schema = {
        'vfi': {
            Any(): {
                'bd_vfi_name': str,
                Optional('bridge_group'): str,
                'state': str,
                Optional('type'): str,
                'signaling': str,
                'vpn_id': int,
                Optional('ve_id'): int,
                Optional('vpls_id'): str,
                Optional('ve_range'): int,
                Optional('rd'): str,
                Optional('rt'): list,
                'bridge_domain': {
                    Any(): {
                        Optional('pseudo_port_interface'): str,
                        Optional('attachment_circuits'): {
                            Optional(Any()): {
                                'name': str,
                            }
                        },
                        'vfi': {
                            Any(): {
                                'pw_id': {
                                    Any(): {
                                        Optional('local_label'): int,
                                        Optional('ve_id'): int,
                                        Optional('vc_id'): int,
                                        Optional('remote_label'): int,
                                        Optional('split_horizon'): bool,
                                        Optional('discovered_router_id'): str,
                                        Optional('next_hop'): str,
                                    },
                                }
                            },
                        }
                    },
                }
            },
        }
    }


class ShowL2vpnVfi(ShowL2vpnVfiSchema):
    """Parser for show l2vpn vfi
    """

    cli_command = 'show l2vpn vfi'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # Legend: RT=Route-target, S=Split-horizon, Y=Yes, N=No

        # VFI name: VPLS-2051, state: up, type: multipoint, signaling: BGP
        # VFI name: serviceCore1, State: UP, Signaling Protocol: LDP
        p1 = re.compile(r'^VFI +name: +(?P<vfi>[\w\d\-]+), +[S|s]tate:'
                         ' +(?P<state>\w+)(, type: +(?P<type>\w+))?,'
                         ' +[S|s]ignaling( Protocol)?: +(?P<signaling>\w+)$')

        #   VPN ID: 2051, VE-ID: 2, VE-SIZE: 10
        #   VPN ID: 2000
        p2 = re.compile(r'^VPN +ID: +(?P<vpn_id>\d+)(, +VE-ID: +(?P<ve_id>\d+),'
                         ' VE-SIZE: +(?P<ve_range>\d+))?$')

        #   VPN ID: 100, VPLS-ID: 9:10, Bridge-domain vlan: 100
        p2_1 = re.compile(r'^VPN +ID: +(?P<vpn_id>\d+), +VPLS-ID: +(?P<vpls_id>\S+),'
                         ' Bridge-domain +vlan: +(?P<bridge_domain_vlan>\d+)$')

        #   RD: 65109:2051, RT: 65109:2051, 65109:2051,
        #   RD: 9:10, RT: 10.10.10.10:150
        p3 = re.compile(r'^RD: +(?P<rd>[\d\:]+), +RT: +(?P<rt>[\S\s]+)$')

        #   Bridge-Domain 2051 attachment circuits:
        p4 = re.compile(r'^Bridge-Domain +(?P<bd_id>\d+)'
                         ' +attachment +circuits:( +(?P<attachment_circuits>[\S\s]+))?$')

        #   Pseudo-port interface: pseudowire100001
        p5 = re.compile(r'^Pseudo-port +[I|i]nterface: +(?P<pseudo_port_interface>\S+)$')

        #   Interface          Peer Address    VE-ID  Local Label  Remote Label    S
        #   pseudowire100202   10.120.202.64    1      16           327810          Y
        p6 = re.compile(r'^(?P<pw_intf>\S+) +(?P<pw_peer_id>[\d\.]+)'
                         ' +(?P<ve_id>\d+) +(?P<local_label>\d+) +(?P<remote_label>\d+) +(?P<split_horizon>\w+)$')

        # Interface          Peer Address     VC ID        S
        # pseudowire3        10.64.4.4        14           Y
        # pseudowire2        10.36.3.3        13           Y
        # pseudowire1        10.16.2.2        12           Y
        p6_1 = re.compile(r'^(?P<pw_intf>\S+) +(?P<pw_peer_id>[\d\.]+)'
                         ' +(?P<vc_id>\d+) +(?P<split_horizon>\w+)$')

        # Interface    Peer Address    VC ID      Discovered Router ID   Next Hop
        # Pw2000       10.0.0.1        10         10.0.0.1               10.0.0.1
        # Pw2001       10.0.0.2        10         10.1.1.2               10.0.0.2
        # Pw2002       10.0.0.3        10         10.1.1.3               10.0.0.3
        # Pw5          10.0.0.4        10         -                      10.0.0.4
        p6_2 = re.compile(r'^(?P<pw_intf>\S+) +(?P<pw_peer_id>[\d\.]+)'
                         ' +(?P<vc_id>\d+) +(?P<discovered_router_id>[\d\.\-]+) +(?P<next_hop>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                vfi = group['vfi']
                final_dict = ret_dict.setdefault('vfi', {}).setdefault(vfi, {})
                final_dict['bd_vfi_name'] = vfi
                final_dict['state'] = group['state']
                if group['type']:
                    final_dict['type'] = group['type']
                final_dict['signaling'] = group['signaling']
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                final_dict['vpn_id'] = int(group['vpn_id'])
                if group['ve_id']:
                    final_dict['ve_id'] = int(group['ve_id'])
                if group['ve_range']:
                    final_dict['ve_range'] = int(group['ve_range'])
                continue

            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                final_dict['vpn_id'] = int(group['vpn_id'])
                final_dict['vpls_id'] = group['vpls_id']
                new_final_dict = final_dict.setdefault('bridge_domain', {}).\
                    setdefault(int(group['bridge_domain_vlan']), {})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                final_dict['rd'] = group['rd']
                final_dict['rt'] = [x.strip() for x in group['rt'].split(',') if x]
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                bd_id = group['bd_id']
                if 'bridge_domain' not in final_dict:
                    final_dict.setdefault('bridge_domain', {})
                if bd_id not in final_dict['bridge_domain']:
                    new_final_dict = final_dict['bridge_domain'].setdefault(bd_id, {})
                new_final_dict.setdefault('attachment_circuits', {})
                if group['attachment_circuits']:
                    new_final_dict['attachment_circuits'].setdefault(
                        group['attachment_circuits'], {})
                    new_final_dict['attachment_circuits']\
                        [group['attachment_circuits']]['name'] = \
                            group['attachment_circuits']
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                new_final_dict['pseudo_port_interface'] = \
                    group['pseudo_port_interface']
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                pw_peer_id = group['pw_peer_id']
                pw_intf = group['pw_intf']
                pw_final_dict = new_final_dict.setdefault('vfi', {}).\
                    setdefault(pw_peer_id, {}).setdefault('pw_id', {}).\
                        setdefault(pw_intf, {})
                pw_final_dict['local_label'] = \
                    int(group['local_label'])
                pw_final_dict['ve_id'] = \
                    int(group['ve_id'])
                pw_final_dict['remote_label'] = \
                    int(group['remote_label'])
                if 'Y' in group['split_horizon'] or \
                    'y' in group['split_horizon']:
                    pw_final_dict['split_horizon'] = \
                        True
                else:
                    pw_final_dict['split_horizon'] = \
                        False
                continue

            m = p6_1.match(line)
            if m:
                group = m.groupdict()
                pw_peer_id = group['pw_peer_id']
                pw_intf = group['pw_intf']
                pw_final_dict = new_final_dict.setdefault('vfi', {}).\
                    setdefault(pw_peer_id, {}).setdefault('pw_id', {}).\
                        setdefault(pw_intf, {})
                pw_final_dict['vc_id'] = \
                    int(group['vc_id'])
                if 'Y' in group['split_horizon'] or \
                    'y' in group['split_horizon']:
                    pw_final_dict['split_horizon'] = \
                        True
                else:
                    pw_final_dict['split_horizon'] = \
                        False
                continue

            m = p6_2.match(line)
            if m:
                group = m.groupdict()
                pw_peer_id = group['pw_peer_id']
                pw_intf = group['pw_intf']
                pw_final_dict = new_final_dict.setdefault('vfi', {}).\
                    setdefault(pw_peer_id, {}).setdefault('pw_id', {}).\
                        setdefault(pw_intf, {})
                pw_final_dict['vc_id'] = \
                    int(group['vc_id'])
                pw_final_dict['discovered_router_id'] = \
                    group['discovered_router_id']
                pw_final_dict['next_hop'] = \
                    group['next_hop']
                continue

        return ret_dict

# ===================================
# Schema for 'show l2vpn service all'
# ===================================
class ShowL2vpnServiceAllSchema(MetaParser):
    """Schema for show l2vpn service all
                  show l2vpn service interface {interface}
                  show l2vpn service name {name}
                  show l2vpn service xconnect all
                  show l2vpn service xconnect interface {interface}
                  show l2vpn service xconnect name {name}
    """

    schema = {
        'vpls_name': {
            Any(): {
                'state': str,
               Optional('description'): str,
                Optional('interface'): {
                    Any(): {
                        Optional('group'): str,
                        'encapsulation': str,
                        'priority': int,
                        'state': str,
                        'state_in_l2vpn_service': str,
                    },
                }
            },
        }
    }

# ===================================
# Parser for 'show l2vpn service all'
# ===================================
class ShowL2vpnServiceAll(ShowL2vpnServiceAllSchema):
    """Parser for  show l2vpn service all
                   show l2vpn service interface {interface}
                   show l2vpn service name {name}
                   show l2vpn service xconnect all
                   show l2vpn service xconnect interface {interface}
                   show l2vpn service xconnect name {name}
     """

    cli_command = [
                  'show l2vpn service all',
                  'show l2vpn service interface {interface}',
                  'show l2vpn service name {name}',
                  'show l2vpn service {xconnect} all',
                  'show l2vpn service {xconnect} interface {interface}',
                  'show l2vpn service {xconnect} name {name}'
    ]

    def cli(self, interface=None, name=None, xconnect=None, output=None):
        if output is None:
            if xconnect and interface:
                cli_cmd = self.cli_command[4].format(xconnect=xconnect, interface=interface)
            elif xconnect and name:
                cli_cmd = self.cli_command[5].format(xconnect=xconnect, name=name)
            elif xconnect:
                cli_cmd = self.cli_command[3].format(xconnect=xconnect)
            elif interface:
                cli_cmd = self.cli_command[1].format(interface=interface)
            elif name:
                cli_cmd = self.cli_command[2].format(name=name)
            else:
                cli_cmd = self.cli_command[0]
            out = self.device.execute(cli_cmd)
        else:
            out = output

        if not out:
            return

        # initial return dictionary
        ret_dict = {}

        # VPLS name: VPLS-2051, State: UP
        # XC name: serviceWire1, State: UP
        # VPWS name: Gi1/1/1-1001, State: UP
        # VPWS name: Gi3-SI:2842, State: UP
        p1 = re.compile(r'^\w+ +name: +(?P<name>[\w\d\-\/:]+), +State: +(?P<state>\w+)$')

        #   pw100214           core_pw     1:2051(MPLS)                    0     UP  UP
        #   pw100001                       VPLS-2051(VFI)                  0     UP  UP
        #   Eth2/1:20          access_conn EVC 55                  0     UP  UP
        #   Pw2                core        MPLS 10.144.6.6:200        1     SB  IA
        #   Te0/1/3                        Te0/1/3:1900(Eth VLAN)          0     UP  UP
        p2 = re.compile(r'^(?P<pw_intf>\S+)( +(?P<group>\S+))? +(?P<encapsulation>\S+(?:\s\S+|\(.+\))) +(?P<priority>\d+) +(?P<intf_state>\w+) +(?P<state_in_l2vpn_service>[\w\-]+)$')

        #   Description: none
        #   Description: Any_String
        p3 = re.compile(r'^\s*Description:\s+(?P<description>\S+)')

        for line in out.splitlines():
            line = line.strip()

            # VPLS name: VPLS-2051, State: UP
            # XC name: serviceWire1, State: UP
            # VPWS name: Gi1/1/1-1001, State: UP
            # VPWS name: Gi3-SI:2842, State: UP
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vpls_name = group['name']
                final_dict = ret_dict.setdefault('vpls_name', {}).setdefault(
                    vpls_name, {})
                final_dict['state'] = group['state']
                continue

            #   pw100214           core_pw     1:2051(MPLS)                    0     UP  UP
            #   pw100001                       VPLS-2051(VFI)                  0     UP  UP
            #   Eth2/1:20          access_conn EVC 55                  0     UP  UP
            #   Pw2                core        MPLS 10.144.6.6:200        1     SB  IA
            m = p2.match(line)
            if m:
                group = m.groupdict()
                pw_intf = group['pw_intf']
                final_dict.setdefault('interface', {}).setdefault(pw_intf, {})
                if group['group']:
                    final_dict['interface'][pw_intf]['group'] = group['group']
                final_dict['interface'][pw_intf]['encapsulation'] = \
                    group['encapsulation'].strip()
                final_dict['interface'][pw_intf]['priority'] = int(
                    group['priority'])
                final_dict['interface'][pw_intf]['state'] = \
                    group['intf_state']
                final_dict['interface'][pw_intf]['state_in_l2vpn_service'] = \
                    group['state_in_l2vpn_service']
                continue

            #   Description: none
            #   Description: Any_String
            m = p3.match(line)
            if m:
                final_dict['description'] = m.groupdict()['description']
                continue

        return ret_dict

# ===================================
# Parser for 'show l2vpn vfi name {name} detail'
# ===================================
class ShowL2vpnVfiNameDetailSchema(MetaParser):
    """Schema for show l2vpn vfi name {name} detail
    """

    schema = {
        'bridge-domain': int,
        'interfaces': {
            Any(): {
                'peer-address': str,
                's': str,
                'vc-id': int
             }
        },
        'pseudo-port-intf': str,
        'signaling': str,
        'state': str,
        'type': str,
        'vfi-name': str,
        'vpn-id': int
    }


class ShowL2vpnVfiNameDetail(ShowL2vpnVfiNameDetailSchema):
    """Parser for show l2vpn vfi name {name} detail
    """

    cli_command = 'show l2vpn vfi name {name} detail'

    def cli(self, name=None, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(name=name))
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        #VFI name: vpls, state: up, type: multipoint, signaling: LDP
        p1 = re.compile(r'VFI name: +(?P<vfi_name>\w+)\, +'
                    'state: +(?P<state>\w+)\, +'
                    'type: +(?P<type>\w+)\, +'
                    'signaling: +(?P<signaling>\w+)')

        #VPN ID: 1000
        p2 = re.compile(r'VPN ID: +(?P<vpn_id>\d+)')

        #Bridge-Domain 1000 attachment circuits:
        p3 = re.compile(r'Bridge-Domain +(?P<bridge_domain>\d+)')

        #Pseudo-port interface: pseudowire100007
        p4 = re.compile(r'Pseudo-port interface\: +(?P<pseudo_port_intf>\S+)')

        #pseudowire22       192.168.255.3    1000         Y
        p5 = re.compile(r'(?P<interface>\S+) +'
                    '(?P<addr>([0-9]+\.){3}[0-9]+) +'
                    '(?P<vc_id>\d+) +'
                    '(?P<s>\w)')

        for line in out.splitlines():
            line = line.strip()
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                ret_dict.update({
                    'vfi-name': group['vfi_name'],
                    'state': group['state'],
                    'type': group['type'],
                    'signaling': group['signaling']
                })
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                ret_dict.update({'vpn-id': int(group['vpn_id'])})
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                ret_dict.update({'bridge-domain': int(group['bridge_domain'])})

            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                ret_dict.update({'pseudo-port-intf': group['pseudo_port_intf']})

            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                interface_dict = ret_dict.setdefault('interfaces', {})
                interface = interface_dict.setdefault(group['interface'], {})
                interface.update({
                    'peer-address': group['addr'],
                    'vc-id': int(group['vc_id']),
                    's': group['s']
                })

        return ret_dict


# ===================================
# Parser for 'show vfi name {name}'
# ===================================
class ShowVfiNameSchema(MetaParser):
    """Schema for show vfi name {name}
   """

    schema = {
        'bridge-domain': int,
        'peers': {
            Any(): {
                'peer-address': str,
                's': str,
                'vc-id': int
             }
        },
        'signaling': str,
        'state': str,
        'type': str,
        'vfi-name': str,
        'vpn-id': int
    }


class ShowVfiName(ShowVfiNameSchema):
    """Parser for show vfi name {name}
    """

    cli_command = 'show vfi name {name}'

    def cli(self, name=None, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(name=name))
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        #VFI name: vpls, state: up, type: multipoint, signaling: LDP
        p1 = re.compile(r'VFI name: +(?P<vfi_name>\w+)\, +'
                    'state: +(?P<state>\w+)\, +'
                    'type: +(?P<type>\w+)\, +'
                    'signaling: +(?P<signaling>\w+)')

        #VPN ID: 1000
        p2 = re.compile(r'VPN ID: +(?P<vpn_id>\d+)')

        #Bridge-Domain 1000 attachment circuits:
        p3 = re.compile(r'Bridge-Domain +(?P<bridge_domain>\d+)')

        #192.168.255.3    1000         Y
        p4 = re.compile(r'(?P<addr>([0-9]+\.){3}[0-9]+) +'
                    '(?P<vc_id>\d+) +'
                    '(?P<s>\w)')

        peer_count=1
        for line in out.splitlines():
            line = line.strip()
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                ret_dict.update({
                    'vfi-name': group['vfi_name'],
                    'state': group['state'],
                    'type': group['type'],
                    'signaling': group['signaling']
                })
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                ret_dict.update({'vpn-id': int(group['vpn_id'])})
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                ret_dict.update({'bridge-domain': int(group['bridge_domain'])})

            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                peer_dict = ret_dict.setdefault('peers', {})
                peer = peer_dict.setdefault(peer_count, {})
                peer.update({
                    'peer-address': group['addr'],
                    'vc-id': int(group['vc_id']),
                    's': group['s']
                })
                peer_count+=1

        return ret_dict

# ============================================
# Schema for 'show l2vpn evpn ethernet-segment detail'
# ============================================
class ShowL2vpnEvpnEthernetSegmentDetailSchema(MetaParser):
    """ Schema for show l2vpn evpn ethernet-segment detail
                   show l2vpn evpn ethernet-segment interface {interface} detail
    """

    schema = {
        Any(): {
            'interface': list,
            'redundancy_mode': str,
            'df_wait_time': int,
            'split_horizon_label': int,
            'state': str,
            'encap_type': str,
            'ordinal': Or(int, str),
            'core_isolation': str,
            Optional('rd'): {
                Any (): {
                    'export_rt': list,
                },
            },
            'forwarder_list': list,
        }
    }


# ==================================================
# Parser for 'show l2vpn evpn ethernet-segment detail'
# ==================================================
class ShowL2vpnEvpnEthernetSegmentDetail(ShowL2vpnEvpnEthernetSegmentDetailSchema):
    """ Parser for: show l2vpn evpn ethernet-segment detail
                    show l2vpn evpn ethernet-segment interface {interface} detail
    """

    cli_command = [
           'show l2vpn evpn ethernet-segment interface {interface} detail',
           'show l2vpn evpn ethernet-segment detail'
                  ]

    def cli(self, interface=None, output=None):

        if output is None:
            # Execute command
            if interface:
                cli_cmd = self.cli_command[0].format(interface=interface)
            else:
                cli_cmd = self.cli_command[1]
            cli_output = self.device.execute(cli_cmd)
        else:
            cli_output = output

        # EVPN Ethernet Segment ID: 03AA.BB00.0000.0200.0001
        p1 = re.compile(r'^EVPN +Ethernet +Segment +ID: +(?P<eth_seg>[0-9a-fA-F\.]+)$')

        # Interface:              Po1
        # Interface:              pw100002 pw100003 pw100005 pw100006
        p2 = re.compile(r'^Interface: +(?P<intf>.*)$')

        # Redundancy mode:        all-active
        p3 = re.compile(r'^Redundancy +mode: +(?P<redundancy_mode>[a-z\-]+)$')

        # DF election wait time:  3 seconds
        p4 = re.compile(r'^DF +election +wait +time: +(?P<df_time>[0-9]+) +seconds$')

        # Split Horizon label:    16 
        p5 = re.compile(r'^Split +Horizon +label: +(?P<sh_label>\d+)$')

        # State:                  Ready
        # State:                  Port Down
        p6 = re.compile(r'^State: +(?P<state>[\w\(\): ]+)$')

        # Encapsulation:          mpls
        p7 = re.compile(r'^Encapsulation: +(?P<encap_type>\w+)$')

        # Ordinal:                1
        # Ordinal:                Not available
        p8 = re.compile(r'^Ordinal: +(?P<ordinal>[\d\w ]+)$')

        # Core Isolation:         No
        # Core Isolation:         Yes (error disable)
        p9 = re.compile(r'^Core +Isolation: +(?P<core_iso>[\w\(\) ]+)$')

        # RD:                     4.4.4.3:1
        # RD:                     Not set
        p10 = re.compile(r'^RD: +(?P<rd>[0-9\.:\w ]+)$')

        # Export-RTs:           100:2
        p11 = re.compile(r'^Export-RTs: +(?P<export_rt>[0-9: ]+)$')

        #                       1:12 1:13 1:14 1:21 1:22 
        p11_1 = re.compile(r'^(?P<export_rt>[0-9: ]+)$')

        # Forwarder List:         3.3.3.3 4.4.4.3
        # Forwarder List:         
        p12 = re.compile(r'^Forwarder +List: *(?P<fwd>[0-9\. ]*)$')

        parser_dict = {}

        if not cli_output:
            return

        export_rts_multiline = False

        for line in cli_output.splitlines():
            line = line.strip()

            #EVPN Ethernet Segment ID: 03AA.BB00.0000.0200.0001
            m = p1.match(line)
            if m:
                group = m.groupdict()
                eth_seg = parser_dict.setdefault(group['eth_seg'], {}) 
                continue

            #  Interface:              Po1
            #  Interface:              pw100002 pw100003 pw100005 pw100006
            m = p2.match(line)
            if m:
                group = m.groupdict()
                intf = group['intf']
                intf_list = eth_seg.setdefault('interface', [])
                for item in intf.split():
                    intf_list.append(Common.convert_intf_name(item))
                continue

            #  Redundancy mode:        all-active
            m = p3.match(line)
            if m:
                group = m.groupdict()
                eth_seg.update({'redundancy_mode': group['redundancy_mode']})
                continue

            #  DF election wait time:  3 seconds
            m = p4.match(line)
            if m:
                group = m.groupdict()
                eth_seg.update({'df_wait_time': int(group['df_time'])})
                continue

            #  Split Horizon label:    16
            m = p5.match(line)
            if m:
                group = m.groupdict()
                eth_seg.update({'split_horizon_label': int(group['sh_label'])})
                continue
            #  State:                  Ready
            #  State:                  Port Down
            m = p6.match(line)
            if m:
                group = m.groupdict()
                eth_seg.update({'state': group['state']})
                continue
            #  Encapsulation:          mpls
            m = p7.match(line)
            if m:
                group = m.groupdict()
                eth_seg.update({'encap_type': group['encap_type']})
                continue
            #  Ordinal:                1
            #  Ordinal:                Not available
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ordinal = group['ordinal']
                if ordinal.isnumeric():
                    ordinal = int(ordinal)
                eth_seg.update({'ordinal': ordinal})
                continue
            #  Core Isolation:         No
            #  Core Isolation:         Yes (error disable)
            m = p9.match(line)
            if m:
                group = m.groupdict()
                eth_seg.update({'core_isolation': group['core_iso']})
                continue
            #  RD:                     4.4.4.3:1
            #  RD:                     Not set
            m = p10.match(line)
            if m:
                group = m.groupdict()
                rd = group['rd']
                rt_dict = eth_seg.setdefault('rd', {}).setdefault(rd, {})
                continue

            #    Export-RTs:           100:2
            m = p11.match(line)
            if m:
                export_rts_multiline = True
                group = m.groupdict()
                export_rt = group['export_rt']
                export_rt_list = rt_dict.setdefault('export_rt', [])
                for item in export_rt.split():
                    export_rt_list.append(item)
                continue
            elif export_rts_multiline:
                #                       1:12 1:13 1:14 1:21 1:22 
                m = p11_1.match(line)
                if m:
                    group = m.groupdict()
                    export_rt = group['export_rt']
                    for item in export_rt.split():
                        export_rt_list.append(item)

            #  Forwarder List:         3.3.3.3 4.4.4.3
            #  Forwarder List:         
            m = p12.match(line)
            if m:
                export_rts_multiline = False
                group = m.groupdict()
                fwd = group['fwd']
                fwd_list = eth_seg.setdefault('forwarder_list', [])
                if fwd:
                    for item in fwd.split():
                        fwd_list.append(item) 
                continue

        return parser_dict

# ============================================
# Schema for 'show l2vpn evpn ethernet-segment'
# ============================================
class ShowL2vpnEvpnEthernetSegmentSchema(MetaParser):
    """ Schema for show l2vpn evpn ethernet-segment
    """

    schema = {
        'esi': {
            Any(): {
                'port': str,
                'redundancy_mode': str,
                'df_wait_time': int,
                'split_horizon_label': int,
            }
        }
    }

# ==================================================
# Parser for 'show l2vpn evpn ethernet-segment'
# ==================================================
class ShowL2vpnEvpnEthernetSegment(ShowL2vpnEvpnEthernetSegmentSchema):
    """ Parser for: show l2vpn evpn ethernet-segment """

    cli_command = 'show l2vpn evpn ethernet-segment'

    def cli(self, output=None):

        parsed_dict = {}

        if output is None:
            # Execute command
            cli_output = self.device.execute(self.cli_command)
        else:
            cli_output = output

        #03AA.AABB.BBCC.CC00.0001 Et0/2      single-active   3       16
        p1 = re.compile(r'^(?P<esi>(\w+\.\w+\.\w+\.\w+\.\w+)) +(?P<port>\S+) +(?P<redundancy_mode>\S+) +(?P<df_time>\S+) +(?P<sh_label>\S+)$')
        parser_dict = {}

        if not cli_output:
            return

        for line in cli_output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                esi = parser_dict.setdefault('esi', {})
                eth_seg = esi.setdefault(group['esi'], {}) 
                eth_seg.update({
                    'port': Common.convert_intf_name(group['port']),
                    'redundancy_mode': group['redundancy_mode'],
                    'df_wait_time': int(group['df_time']),
                    'split_horizon_label': int(group['sh_label'])
                })
                continue

        return parser_dict


# =================================
# Schema for 'show l2vpn evpn mac'
# =================================
class ShowL2vpnEvpnMacSchema(MetaParser):
    """ Schema for show l2vpn evpn mac
                   show l2vpn evpn mac address {mac_addr}
                   show l2vpn evpn mac bridge-domain {bd_id}
                   show l2vpn evpn mac bridge-domain {bd_id} address {mac_addr}
                   show l2vpn evpn mac bridge-domain {bd_id} duplicate
                   show l2vpn evpn mac bridge-domain {bd_id} local
                   show l2vpn evpn mac bridge-domain {bd_id} remote
                   show l2vpn evpn mac duplicate
                   show l2vpn evpn mac evi {evi_id}
                   show l2vpn evpn mac evi {evi_id} address {mac_addr}
                   show l2vpn evpn mac evi {evi_id} duplicate
                   show l2vpn evpn mac evi {evi_id} local
                   show l2vpn evpn mac evi {evi_id} remote
                   show l2vpn evpn mac local
                   show l2vpn evpn mac remote
                   show l2vpn evpn mac vlan {vlan_id}
                   show l2vpn evpn mac vlan {vlan_id} address {mac_addr}
                   show l2vpn evpn mac vlan {vlan_id} duplicate
                   show l2vpn evpn mac vlan {vlan_id} {local}
                   show l2vpn evpn mac vlan {vlan_id} {remote}
    """

    schema = {
        'evi': {
            Any(): {
                'bd_id': {
                    Any(): {
                        'eth_tag': {
                            Any() : {
                                'mac_addr':{
                                    Any(): {
                                        'esi': str,
                                        'next_hops': list
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


# =================================
# Parser for 'show l2vpn evpn mac'
# =================================
class ShowL2vpnEvpnMac(ShowL2vpnEvpnMacSchema):
    """ Parser for show l2vpn evpn mac
                   show l2vpn evpn mac address {mac_addr}
                   show l2vpn evpn mac bridge-domain {bd_id}
                   show l2vpn evpn mac bridge-domain {bd_id} address {mac_addr}
                   show l2vpn evpn mac bridge-domain {bd_id} duplicate
                   show l2vpn evpn mac bridge-domain {bd_id} local
                   show l2vpn evpn mac bridge-domain {bd_id} remote
                   show l2vpn evpn mac duplicate
                   show l2vpn evpn mac evi {evi_id}
                   show l2vpn evpn mac evi {evi_id} address {mac_addr}
                   show l2vpn evpn mac evi {evi_id} duplicate
                   show l2vpn evpn mac evi {evi_id} local
                   show l2vpn evpn mac evi {evi_id} remote
                   show l2vpn evpn mac local
                   show l2vpn evpn mac remote
                   show l2vpn evpn mac vlan {vlan_id}
                   show l2vpn evpn mac vlan {vlan_id} address {mac_addr}
                   show l2vpn evpn mac vlan {vlan_id} duplicate
                   show l2vpn evpn mac vlan {vlan_id} {local}
                   show l2vpn evpn mac vlan {vlan_id} {remote}
    """

    cli_command = ['show l2vpn evpn mac',
                   'show l2vpn evpn mac address {mac_addr}',
                   'show l2vpn evpn mac {mac_type}',
                   'show l2vpn evpn mac bridge-domain {bd_id}',
                   'show l2vpn evpn mac bridge-domain {bd_id} address {mac_addr}',
                   'show l2vpn evpn mac bridge-domain {bd_id} {mac_type}',
                   'show l2vpn evpn mac evi {evi_id}',
                   'show l2vpn evpn mac evi {evi_id} address {mac_addr}',
                   'show l2vpn evpn mac evi {evi_id} {mac_type}',
                   'show l2vpn evpn mac vlan {vlan_id}',
                   'show l2vpn evpn mac vlan {vlan_id} address {mac_addr}',
                   'show l2vpn evpn mac vlan {vlan_id} duplicate',
                   'show l2vpn evpn mac vlan {vlan_id} {local}',
                   'show l2vpn evpn mac vlan {vlan_id} {remote}'
    ]

    def cli(self, output=None, mac_addr=None, mac_type=None, bd_id=None, 
            evi_id=None, vlan_id=None, local=None, remote=None):
        if not output:
            # Only these CLI options for mac_type are supported.
            if mac_type and mac_type != 'local' and mac_type != 'remote' and mac_type != 'duplicate':
                raise Exception("Unsupported mac_type {}".format(mac_type))

            cli_cmd = 'show l2vpn evpn mac'

            if bd_id:
                cli_cmd += ' bridge-domain {bd_id}'.format(bd_id=bd_id)
            elif evi_id:
                cli_cmd += ' evi {evi_id}'.format(evi_id=evi_id)
            elif vlan_id:
                cli_cmd += ' vlan {vlan_id}'.format(vlan_id=vlan_id)
                if local:
                    cli_cmd += ' local'
                elif remote:
                    cli_cmd += ' remote'

            if mac_type:
                cli_cmd += ' {mac_type}'.format(mac_type=mac_type)
            elif mac_addr:
                cli_cmd += ' address {mac_addr}'.format(mac_addr=mac_addr)

            cli_output = self.device.execute(cli_cmd)
        else:
            cli_output = output

        if not cli_output:
            return {}

        # Case 1 - BD header
        #
        # MAC Address    EVI   BD    ESI                      Ether Tag  Next Hop(s)
        # -------------- ----- ----- ------------------------ ---------- ---------------
        # aabb.0011.0001 1     11    0000.0000.0000.0000.0000 0          Et1/0:11
        # aabb.0011.0021 1     11    0000.0000.0000.0000.0000 0          Duplicate
        # aabb.0012.0002 2     12    0000.0000.0000.0000.0000 0          2.2.2.1
        #
        # Case 2 - VLAN header
        #
        # MAC Address    EVI   VLAN  ESI                      Ether Tag  Next Hop(s)
        # -------------- ----- ----- ------------------------ ---------- ---------------
        # aabb.0011.0002 1     11    0000.0000.0000.0000.0000 0          2.2.2.1
        #
        # Case 3 - Multiple Next Hops
        #
        # MAC Address    EVI   BD    ESI                      Ether Tag  Next Hop(s)
        # -------------- ----- ----- ------------------------ ---------- ---------------
        # aabb.0012.0002 2     12    0000.0000.0000.0000.0000 0          2.2.2.1
        # aabb.cc02.2800 2     12    03AA.BB00.0000.0200.0001 0          3.3.3.1
        # aabb.cc82.2800 2     12    03AA.BB00.0000.0200.0001 0          Et1/0:12
        #                                                                3.3.3.1
        p1 = re.compile(r'^MAC Address\s+EVI\s+(BD|VLAN)\s+ESI\s+Ether Tag\s+Next Hop\(s\)$')
        p2 = re.compile(r'^(?P<mac>[0-9a-fA-F\.]+)\s+(?P<evi>\d+)\s+(?P<bd_id>\d+)\s+(?P<esi>[0-9a-fA-F\.]+)\s+(?P<eth_tag>\d+)\s+(?P<next_hop>.+)$')
        p3 = re.compile(r'^(?P<next_hop>.+)$')

        parser_dict = {}

        header_validated = False
        next_hops = None
        for line in cli_output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Sanity check the header appears in the expected order.
            m = p1.match(line)
            if m:
                header_validated = True
                continue

            # aabb.0011.0001 1     11    0000.0000.0000.0000.0000 0          Et1/0:11
            m = p2.match(line)
            if m:
                group = m.groupdict()
                evi_dict = parser_dict.setdefault('evi', {})
                evis = evi_dict.setdefault(int(group['evi']), {})

                bd_id_dict = evis.setdefault('bd_id', {})
                bd_ids = bd_id_dict.setdefault(int(group['bd_id']), {})

                eth_tag_dict = bd_ids.setdefault( 'eth_tag', {})
                eth_tags = eth_tag_dict.setdefault( int(group['eth_tag']), {})

                mac_addr_dict = eth_tags.setdefault('mac_addr', {})
                mac_vals = mac_addr_dict.setdefault(group['mac'], {})

                mac_vals.update({
                    'esi': group['esi']
                })
                next_hops = mac_vals.setdefault('next_hops', [])
                next_hops.append(group['next_hop'])
                continue

            #                                                                3.3.3.1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                if next_hops:
                    next_hops.append(group['next_hop'])
                continue

        if not header_validated:
            return {}

        return parser_dict


# ========================================
# Schema for 'show l2vpn evpn mac detail'
# ========================================
class ShowL2vpnEvpnMacDetailSchema(MetaParser):
    """ Schema for show l2vpn evpn mac address {mac_addr} detail
                   show l2vpn evpn mac bridge-domain {bd_id} address {mac_addr} detail
                   show l2vpn evpn mac bridge-domain {bd_id} detail
                   show l2vpn evpn mac bridge-domain {bd_id} duplicate detail
                   show l2vpn evpn mac bridge-domain {bd_id} local detail
                   show l2vpn evpn mac bridge-domain {bd_id} remote detail
                   show l2vpn evpn mac detail
                   show l2vpn evpn mac duplicate detail
                   show l2vpn evpn mac evi {evi_id} address {mac_addr} detail
                   show l2vpn evpn mac evi {evi_id} detail
                   show l2vpn evpn mac evi {evi_id} duplicate detail
                   show l2vpn evpn mac evi {evi_id} local detail
                   show l2vpn evpn mac evi {evi_id} remote detail
                   show l2vpn evpn mac local detail
                   show l2vpn evpn mac remote detail
    """

    schema = {
        'evi': {
            Any(): {
                'bd_id': {
                    Any(): {
                        'eth_tag': {
                            Any(): {
                                'mac_addr': {
                                    Any(): {
                                        'sticky': bool,
                                        'stale': bool,
                                        'esi': str,
                                        'next_hops': list,
                                        Optional('local_addr'): str,
                                        'seq_number': int,
                                        'mac_only_present': bool,
                                        'mac_dup_detection': {
                                            'status': str,
                                            Optional('moves_count'): int,
                                            Optional('moves_limit'): int,
                                            Optional('expiry_time'): str,
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


# ========================================
# Parser for 'show l2vpn evpn mac detail'
# ========================================
class ShowL2vpnEvpnMacDetail(ShowL2vpnEvpnMacDetailSchema):
    """ Parser for show l2vpn evpn mac address {mac_addr} detail
                   show l2vpn evpn mac bridge-domain {bd_id} address {mac_addr} detail
                   show l2vpn evpn mac bridge-domain {bd_id} detail
                   show l2vpn evpn mac bridge-domain {bd_id} duplicate detail
                   show l2vpn evpn mac bridge-domain {bd_id} local detail
                   show l2vpn evpn mac bridge-domain {bd_id} remote detail
                   show l2vpn evpn mac detail
                   show l2vpn evpn mac duplicate detail
                   show l2vpn evpn mac evi {evi_id} address {mac_addr} detail
                   show l2vpn evpn mac evi {evi_id} detail
                   show l2vpn evpn mac evi {evi_id} duplicate detail
                   show l2vpn evpn mac evi {evi_id} local detail
                   show l2vpn evpn mac evi {evi_id} remote detail
                   show l2vpn evpn mac local detail
                   show l2vpn evpn mac remote detail
    """

    cli_command = ['show l2vpn evpn mac detail',
                   'show l2vpn evpn mac address {mac_addr} detail',
                   'show l2vpn evpn mac {mac_type} detail',
                   'show l2vpn evpn mac bridge-domain {bd_id} detail',
                   'show l2vpn evpn mac bridge-domain {bd_id} address {mac_addr} detail',
                   'show l2vpn evpn mac bridge-domain {bd_id} {mac_type} detail',
                   'show l2vpn evpn mac evi {evi_id} detail',
                   'show l2vpn evpn mac evi {evi_id} address {mac_addr} detail',
                   'show l2vpn evpn mac evi {evi_id} {mac_type} detail',
    ]

    def cli(self, output=None, mac_addr=None, mac_type=None, bd_id=None, evi_id=None):
        if not output:
            # Only these CLI options for mac_type are supported.
            if mac_type and mac_type != 'local' and mac_type != 'remote' and mac_type != 'duplicate':
                raise Exception("Unsupported mac_type {}".format(mac_type))

            cli_cmd = 'show l2vpn evpn mac'

            if bd_id:
                cli_cmd += ' bridge-domain {bd_id}'.format(bd_id=bd_id)
            elif evi_id:
                cli_cmd += ' evi {evi_id}'.format(evi_id=evi_id)

            if mac_type:
                cli_cmd += ' {mac_type}'.format(mac_type=mac_type)
            elif mac_addr:
                cli_cmd += ' address {mac_addr}'.format(mac_addr=mac_addr)

            cli_cmd += ' detail'

            cli_output = self.device.execute(cli_cmd)
        else:
            cli_output = output

        if not cli_output:
            return {}

        # MAC Address:                aabb.0011.0020
        # MAC Address:                aabb.0012.0002, sticky
        # MAC Address:                aabb.0012.0002 (stale)
        # MAC Address:                aabb.0012.0002, sticky (stale)
        p1 = re.compile(r'^MAC Address:\s+(?P<mac>[0-9a-fA-F\.]+)(,?\s+(?P<mac_status>[\w\s\(\)]+))?$')

        # EVPN Instance:              2
        p2 = re.compile(r'^EVPN Instance:\s+(?P<evi>\d+)$')

        # Bridge Domain:              11
        # Vlan:                       11
        p3 = re.compile(r'^(Bridge Domain|Vlan):\s+(?P<bd_id>\d+)$')

        # Ethernet Segment:           03AA.BB00.0000.0200.0001
        p4 = re.compile(r'^Ethernet Segment:\s+(?P<esi>[0-9a-fA-F\.]+)$')

        # Ethernet Tag ID:            0
        p5 = re.compile(r'^Ethernet Tag ID:\s+(?P<eth_tag>\d+)$')

        # Next Hop(s):                L:17 Ethernet1/0 service instance 12
        # Next Hop(s):                V:1000111 BD-VIF1112
        p6 = re.compile(r'^Next Hop\(s\):\s+(?P<next_hop>[\w\/\s\.:-]+)$')
        #                             L:17 3.3.3.1
        #                             L:17 5.5.5.1
        #                             V:1000111 BD-VIF1112
        p7 = re.compile(r'^(?P<next_hop>[\w\/\s\.:-]+)$')

        # Local Address:              4.4.4.1
        p8 = re.compile(r'^Local Address:\s+(?P<local_addr>[a-zA-Z0-9\.:]+)$')

        # Sequence Number:            0
        p9 = re.compile(r'^Sequence Number:\s+(?P<seq_number>\d+)$')

        # MAC only present:           Yes
        p10 = re.compile(r'^MAC only present:\s+(?P<mac_only_present>(Yes|No))$')

        # MAC Duplication Detection:  Timer not running
        # MAC Duplication Detection:  MAC moves 3, limit 5
        #                             Timer expires in 09:56:34
        # MAC Duplication Detection:  Duplicate MAC address detected
        p11 = re.compile(r'^MAC Duplication Detection:\s+(?P<mac_dup_status>[\w\d\s,]+)$')
        p12 = re.compile(r'^MAC moves (?P<moves_count>\d+), limit (?P<moves_limit>\d+)$')
        p13 = re.compile(r'^Timer expires in (?P<expiry_time>[\d:]+)$')

        parser_dict = {}

        for line in cli_output.splitlines():
            line = line.strip()
            if not line:
                continue

            # MAC Address:                aabb.0011.0020
            # MAC Address:                aabb.0012.0002, sticky
            # MAC Address:                aabb.0012.0002 (stale)
            # MAC Address:                aabb.0012.0002, sticky (stale)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                mac_addr_value = group['mac']
                sticky = False
                stale = False
                if group['mac_status']:
                    sticky = 'sticky' in group['mac_status']
                    stale = 'stale' in group['mac_status']
                continue

            # EVPN Instance:              2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                evi_dict = parser_dict.setdefault( 'evi', {})
                evis = evi_dict.setdefault( int(group['evi']), {} )

                continue

            # Bridge Domain:              11
            # Vlan:                       11
            m = p3.match(line)
            if m:
                group = m.groupdict()
                bd_id_dict = evis.setdefault( 'bd_id', {} )
                bd_ids = bd_id_dict.setdefault( int(group['bd_id']), {} )

                continue

            # Ethernet Segment:           03AA.BB00.0000.0200.0001
            m = p4.match(line)
            if m:
                group = m.groupdict()
                esi_value = group['esi']
                continue

            # Ethernet Tag ID:            0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                # mac_vals.update({'eth_tag': int(group['eth_tag'])})
                eth_tag_dict = bd_ids.setdefault( 'eth_tag', {})
                eth_tags = eth_tag_dict.setdefault( int(group['eth_tag']), {} )

                mac_addr_dict = eth_tags.setdefault('mac_addr', {})
                mac_vals = mac_addr_dict.setdefault(mac_addr_value, {})

                mac_vals.update({
                    'sticky': sticky,
                    'stale': stale,
                    'esi': esi_value
                })
                continue

            # Next Hop(s):                L:17 Ethernet1/0 service instance 12
            m = p6.match(line)
            if m:
                group = m.groupdict()
                next_hops = mac_vals.setdefault('next_hops', [])
                next_hops.append(group['next_hop'])
                continue

            # Local Address:              4.4.4.1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                mac_vals.update({'local_addr': group['local_addr']})
                continue

            # Sequence Number:            0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                mac_vals.update({'seq_number': int(group['seq_number'])})
                continue

            # MAC only present:           Yes
            m = p10.match(line)
            if m:
                group = m.groupdict()
                mac_only_present = True if group['mac_only_present'] == 'Yes' else False
                mac_vals.update({'mac_only_present': mac_only_present})
                continue

            # MAC Duplication Detection:  Timer not running
            # MAC Duplication Detection:  MAC moves 3, limit 5
            # MAC Duplication Detection:  Duplicate MAC address detected
            m = p11.match(line)
            if m:
                group = m.groupdict()
                mac_dup_status = group['mac_dup_status']
                mac_dup_vals = mac_vals.setdefault('mac_dup_detection', {})
                mac_dup_vals.update({'status': mac_dup_status})

                m = p12.match(mac_dup_status)
                if m:
                    group = m.groupdict()
                    mac_dup_vals.update({
                        'moves_count': int(group['moves_count']),
                        'moves_limit': int(group['moves_limit']),
                    })
                continue

            #                             Timer expires in 09:56:34
            m = p13.match(line)
            if m:
                group = m.groupdict()
                mac_dup_vals.update({'expiry_time': group['expiry_time']})
                continue

            # Check this pattern last as it can match other fields.
            #                             L:17 5.5.5.1
            m = p7.match(line)
            if m:
                group = m.groupdict()
                next_hops.append(group['next_hop'])
                continue

        return parser_dict


# =========================================
# Schema for 'show l2vpn evpn mac summary'
# =========================================
class ShowL2vpnEvpnMacSummarySchema(MetaParser):
    """ Schema for show l2vpn evpn mac bridge-domain {bd_id} duplicate summary
                   show l2vpn evpn mac bridge-domain {bd_id} local summary
                   show l2vpn evpn mac bridge-domain {bd_id} remote summary
                   show l2vpn evpn mac bridge-domain {bd_id} summary
                   show l2vpn evpn mac duplicate summary
                   show l2vpn evpn mac evi {evi_id} duplicate summary
                   show l2vpn evpn mac evi {evi_id} local summary
                   show l2vpn evpn mac evi {evi_id} remote summary
                   show l2vpn evpn mac evi {evi_id} summary
                   show l2vpn evpn mac local summary
                   show l2vpn evpn mac remote summary
                   show l2vpn evpn mac summary
    """

    schema = {
        'evi': {
            int: {
                'bd_id': {
                    int: {
                        'eth_tag': {
                            int: {
                                Optional('remote_count'): int,
                                Optional('local_count'): int,
                                Optional('dup_count'): int,
                            },
                        },
                    },
                },
            },
        },
        Optional('total'): {
            Optional('remote_count'): int,
            Optional('local_count'): int,
            Optional('dup_count'): int,
        }
    }


# =========================================
# Parser for 'show l2vpn evpn mac summary'
# =========================================
class ShowL2vpnEvpnMacSummary(ShowL2vpnEvpnMacSummarySchema):
    """ Parser for show l2vpn evpn mac bridge-domain {bd_id} duplicate summary
                   show l2vpn evpn mac bridge-domain {bd_id} local summary
                   show l2vpn evpn mac bridge-domain {bd_id} remote summary
                   show l2vpn evpn mac bridge-domain {bd_id} summary
                   show l2vpn evpn mac duplicate summary
                   show l2vpn evpn mac evi {evi_id} duplicate summary
                   show l2vpn evpn mac evi {evi_id} local summary
                   show l2vpn evpn mac evi {evi_id} remote summary
                   show l2vpn evpn mac evi {evi_id} summary
                   show l2vpn evpn mac local summary
                   show l2vpn evpn mac remote summary
                   show l2vpn evpn mac summary
    """

    cli_command = ['show l2vpn evpn mac summary',
                   'show l2vpn evpn mac {mac_type} summary',
                   'show l2vpn evpn mac bridge-domain {bd_id} summary',
                   'show l2vpn evpn mac bridge-domain {bd_id} {mac_type} summary',
                   'show l2vpn evpn mac evi {evi_id} summary',
                   'show l2vpn evpn mac evi {evi_id} {mac_type} summary',
    ]

    def cli(self, output=None, mac_type=None, bd_id=None, evi_id=None):
        if not output:
            # Only these CLI options for mac_type are supported.
            if mac_type and mac_type != 'local' and mac_type != 'remote' and mac_type != 'duplicate':
                raise Exception("Unsupported mac_type {}".format(mac_type))

            cli_cmd = 'show l2vpn evpn mac'

            if bd_id:
                cli_cmd += ' bridge-domain {bd_id}'.format(bd_id=bd_id)
            elif evi_id:
                cli_cmd += ' evi {evi_id}'.format(evi_id=evi_id)

            if mac_type:
                cli_cmd += ' {mac_type}'.format(mac_type=mac_type)

            cli_cmd += ' summary'

            cli_output = self.device.execute(cli_cmd)
        else:
            cli_output = output

        if not cli_output:
            return {}

        # PE1#show l2vpn evpn mac bridge-domain 11 duplicate summary
        # EVI   BD    Ether Tag  Dup MAC    
        # ----- ----- ---------- ---------- 
        # 1     11    0          1         
        #
        # PE1#show l2vpn evpn mac bridge-domain 11 summary
        # EVI   BD    Ether Tag  Remote MAC Local MAC  Dup MAC
        # ----- ----- ---------- ---------- ---------- ----------
        # 1     11    0          4          6          1
        #
        # PE1#show l2vpn evpn mac remote summary
        # EVI   BD    Ether Tag  Remote MAC 
        # ----- ----- ---------- ---------- 
        # 1     11    0          4         
        # 2     12    0          2         
        #
        # Total                  6
        #
        # PE1#show l2vpn evpn mac summary
        # EVI   BD    Ether Tag  Remote MAC Local MAC  Dup MAC
        # ----- ----- ---------- ---------- ---------- ----------
        # 1     11    0          4          6          1
        # 2     12    0          2          2          0
        #
        # Total                  6          8          1
        #
        # VTEP1#show l2vpn evpn mac summary
        # EVI   VLAN  Ether Tag  Remote MAC Local MAC  Dup MAC
        # ----- ----- ---------- ---------- ---------- ----------
        # 1     11    0          1          0          0
        # 2     12    0          0          0          0
        #
        # Total                  1          0          0
        p1 = re.compile(r'^EVI\s+(BD|VLAN)\s+Ether Tag\s+Remote MAC\s+Local MAC\s+Dup MAC$')
        p2 = re.compile(r'^EVI\s+(BD|VLAN)\s+Ether Tag\s+Remote MAC$')
        p3 = re.compile(r'^EVI\s+(BD|VLAN)\s+Ether Tag\s+Local MAC$')
        p4 = re.compile(r'^EVI\s+(BD|VLAN)\s+Ether Tag\s+Dup MAC$')
        p5 = re.compile(r'^(?P<evi>\d+)\s+(?P<bd_id>\d+)\s+(?P<eth_tag>\d+)\s+(?P<remote_count>\d+)\s+(?P<local_count>\d+)\s+(?P<dup_count>\d+)$')
        p6 = re.compile(r'^(?P<evi>\d+)\s+(?P<bd_id>\d+)\s+(?P<eth_tag>\d+)\s+(?P<count>\d+)$')
        p7 = re.compile(r'^Total\s+(?P<remote_count>\d+)\s+(?P<local_count>\d+)\s+(?P<dup_count>\d+)$')
        p8 = re.compile(r'^Total\s+(?P<count>\d+)$')

        parser_dict = {}

        table_mac_types = None
        for line in cli_output.splitlines():
            line = line.strip()
            if not line:
                continue

            # EVI   BD    Ether Tag  Remote MAC Local MAC  Dup MAC
            m = p1.match(line)
            if m:
                table_mac_types = 'All'
                continue

            # EVI   BD    Ether Tag  Remote MAC 
            m = p2.match(line)
            if m:
                table_mac_types = 'Remote'
                continue

            # EVI   BD    Ether Tag  Local MAC  
            m = p3.match(line)
            if m:
                table_mac_types = 'Local'
                continue

            # EVI   BD    Ether Tag  Dup MAC    
            m = p4.match(line)
            if m:
                table_mac_types = 'Dup'
                continue

            # 1     11    0          4          6          1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                evi_dict = parser_dict.setdefault('evi', {})
                evi_vals = evi_dict.setdefault(int(group['evi']), {})
                bd_id_dict = evi_vals.setdefault('bd_id', {})
                bd_vals = bd_id_dict.setdefault(int(group['bd_id']), {})
                eth_tag_dict = bd_vals.setdefault('eth_tag', {})
                eth_tag_vals = eth_tag_dict.setdefault(int(group['eth_tag']), {})
                if table_mac_types == 'All':
                    eth_tag_vals.update({
                        'remote_count': int(group['remote_count']),
                        'local_count': int(group['local_count']),
                        'dup_count': int(group['dup_count']),
                    })
                continue

            # 1     11    0          4         
            m = p6.match(line)
            if m:
                group = m.groupdict()
                evi_dict = parser_dict.setdefault('evi', {})
                evi_vals = evi_dict.setdefault(int(group['evi']), {})
                bd_id_dict = evi_vals.setdefault('bd_id', {})
                bd_vals = bd_id_dict.setdefault(int(group['bd_id']), {})
                eth_tag_dict = bd_vals.setdefault('eth_tag', {})
                eth_tag_vals = eth_tag_dict.setdefault(int(group['eth_tag']), {})
                if table_mac_types == 'Remote':
                    eth_tag_vals.update({
                        'remote_count': int(group['count']),
                    })
                elif table_mac_types == 'Local':
                    eth_tag_vals.update({
                        'local_count': int(group['count']),
                    })
                elif table_mac_types == 'Dup':
                    eth_tag_vals.update({
                        'dup_count': int(group['count']),
                    })
                continue

            # Total                  6          8          1
            m = p7.match(line)
            if m:
                group = m.groupdict()
                total_vals = parser_dict.setdefault('total', {})
                if table_mac_types == 'All':
                    total_vals.update({
                        'remote_count': int(group['remote_count']),
                        'local_count': int(group['local_count']),
                        'dup_count': int(group['dup_count']),
                    })
                continue

            # Total                  6
            m = p8.match(line)
            if m:
                group = m.groupdict()
                total_vals = parser_dict.setdefault('total', {})
                if table_mac_types == 'Remote':
                    total_vals.update({
                        'remote_count': int(group['count']),
                    })
                elif table_mac_types == 'Local':
                    total_vals.update({
                        'local_count': int(group['count']),
                    })
                elif table_mac_types == 'Dup':
                    total_vals.update({
                        'dup_count': int(group['count']),
                    })
                continue

        # Header must be invalid if this was never set.
        if not table_mac_types:
            return {}

        return parser_dict


# ====================================
# Schema for 'show l2vpn evpn mac ip'
# ====================================
class ShowL2vpnEvpnMacIpSchema(MetaParser):
    """ Schema for show l2vpn evpn mac ip
                   show l2vpn evpn mac ip address {ipv4_addr}
                   show l2vpn evpn mac ip address {ipv6_addr}
                   show l2vpn evpn mac ip bridge-domain {bd_id}
                   show l2vpn evpn mac ip bridge-domain {bd_id} address {ipv4_addr}
                   show l2vpn evpn mac ip bridge-domain {bd_id} address {ipv6_addr}
                   show l2vpn evpn mac ip bridge-domain {bd_id} duplicate
                   show l2vpn evpn mac ip bridge-domain {bd_id} local
                   show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr}
                   show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ipv4_addr}
                   show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ipv6_addr}
                   show l2vpn evpn mac ip bridge-domain {bd_id} remote
                   show l2vpn evpn mac ip duplicate
                   show l2vpn evpn mac ip evi {evi_id}
                   show l2vpn evpn mac ip evi {evi_id} address {ipv4_addr}
                   show l2vpn evpn mac ip evi {evi_id} address {ipv6_addr}
                   show l2vpn evpn mac ip evi {evi_id} duplicate
                   show l2vpn evpn mac ip evi {evi_id} local
                   show l2vpn evpn mac ip evi {evi_id} mac {mac_addr}
                   show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ipv4_addr}
                   show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ipv6_addr}
                   show l2vpn evpn mac ip evi {evi_id} remote
                   show l2vpn evpn mac ip local
                   show l2vpn evpn mac ip mac {mac_addr}
                   show l2vpn evpn mac ip mac {mac_addr} address {ipv4_addr}
                   show l2vpn evpn mac ip mac {mac_addr} address {ipv6_addr}
                   show l2vpn evpn mac ip remote
                   show l2vpn evpn mac ip vlan {vlan_id}
                   show l2vpn evpn mac ip vlan {vlan_id} address {ipv4_addr}
                   show l2vpn evpn mac ip vlan {vlan_id} address {ipv6_addr}
                   show l2vpn evpn mac ip vlan {vlan_id} duplicate
                   show l2vpn evpn mac ip vlan {vlan_id} local
                   show l2vpn evpn mac ip vlan {vlan_id} mac {mac_addr}
                   show l2vpn evpn mac ip vlan {vlan_id} mac {mac_addr} address {ipv4_addr}
                   show l2vpn evpn mac ip vlan {vlan_id} mac {mac_addr} address {ipv6_addr}
                   show l2vpn evpn mac ip vlan {vlan_id} remote
    """

    schema = {
        'evi': {
            Any(): {
                'bd_id': {
                    Any(): {
                        'ip_addr': {
                            Any(): {
                                'mac_addr': {
                                    Any(): {
                                        'next_hops': list
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


# ====================================
# Parser for 'show l2vpn evpn mac ip'
# ====================================
class ShowL2vpnEvpnMacIp(ShowL2vpnEvpnMacIpSchema):
    """ Parser for show l2vpn evpn mac ip
                   show l2vpn evpn mac ip address {ipv4_addr}
                   show l2vpn evpn mac ip address {ipv6_addr}
                   show l2vpn evpn mac ip bridge-domain {bd_id}
                   show l2vpn evpn mac ip bridge-domain {bd_id} address {ipv4_addr}
                   show l2vpn evpn mac ip bridge-domain {bd_id} address {ipv6_addr}
                   show l2vpn evpn mac ip bridge-domain {bd_id} duplicate
                   show l2vpn evpn mac ip bridge-domain {bd_id} local
                   show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr}
                   show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ipv4_addr}
                   show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ipv6_addr}
                   show l2vpn evpn mac ip bridge-domain {bd_id} remote
                   show l2vpn evpn mac ip duplicate
                   show l2vpn evpn mac ip evi {evi_id}
                   show l2vpn evpn mac ip evi {evi_id} address {ipv4_addr}
                   show l2vpn evpn mac ip evi {evi_id} address {ipv6_addr}
                   show l2vpn evpn mac ip evi {evi_id} duplicate
                   show l2vpn evpn mac ip evi {evi_id} local
                   show l2vpn evpn mac ip evi {evi_id} mac {mac_addr}
                   show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ipv4_addr}
                   show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ipv6_addr}
                   show l2vpn evpn mac ip evi {evi_id} remote
                   show l2vpn evpn mac ip local
                   show l2vpn evpn mac ip mac {mac_addr}
                   show l2vpn evpn mac ip mac {mac_addr} address {ipv4_addr}
                   show l2vpn evpn mac ip mac {mac_addr} address {ipv6_addr}
                   show l2vpn evpn mac ip remote
                   show l2vpn evpn mac ip vlan {vlan_id}
                   show l2vpn evpn mac ip vlan {vlan_id} address {ipv4_addr}
                   show l2vpn evpn mac ip vlan {vlan_id} address {ipv6_addr}
                   show l2vpn evpn mac ip vlan {vlan_id} duplicate
                   show l2vpn evpn mac ip vlan {vlan_id} local
                   show l2vpn evpn mac ip vlan {vlan_id} mac {mac_addr}
                   show l2vpn evpn mac ip vlan {vlan_id} mac {mac_addr} address {ipv4_addr}
                   show l2vpn evpn mac ip vlan {vlan_id} mac {mac_addr} address {ipv6_addr}
                   show l2vpn evpn mac ip vlan {vlan_id} remote
    """

    cli_command = ['show l2vpn evpn mac ip',
                    'show l2vpn evpn mac ip address {ip_addr}',
                    'show l2vpn evpn mac ip {mac_ip_type}',
                    'show l2vpn evpn mac ip mac {mac_addr}',
                    'show l2vpn evpn mac ip mac {mac_addr} address {ip_addr}',
                    'show l2vpn evpn mac ip bridge-domain {bd_id}',
                    'show l2vpn evpn mac ip bridge-domain {bd_id} address {ip_addr}',
                    'show l2vpn evpn mac ip bridge-domain {bd_id} {mac_ip_type}',
                    'show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr}',
                    'show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ip_addr}',
                    'show l2vpn evpn mac ip evi {evi_id}',
                    'show l2vpn evpn mac ip evi {evi_id} address {ip_addr}',
                    'show l2vpn evpn mac ip evi {evi_id} {mac_ip_type}',
                    'show l2vpn evpn mac ip evi {evi_id} mac {mac_addr}',
                    'show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ip_addr}',
                    'show l2vpn evpn mac ip vlan {vlan_id}',
                    'show l2vpn evpn mac ip vlan {vlan_id} address {ip_addr}',
                    'show l2vpn evpn mac ip vlan {vlan_id} {mac_ip_type}',
                    'show l2vpn evpn mac ip vlan {vlan_id} mac {mac_addr}',
                    'show l2vpn evpn mac ip vlan {vlan_id} mac {mac_addr} address {ip_addr}',
     ]

    def cli(self, output=None, mac_addr=None, mac_ip_type=None, bd_id=None, evi_id=None, ip_addr=None, vlan_id=None):
        if not output:
            # Only these CLI options for mac_ip_type are supported.
            if mac_ip_type and mac_ip_type != 'local' and mac_ip_type != 'remote' and mac_ip_type != 'duplicate':
                raise Exception("Unsupported mac_ip_type {}".format(mac_ip_type))
            
            cli_cmd = 'show l2vpn evpn mac ip'

            if bd_id:
                cli_cmd += ' bridge-domain {bd_id}'.format(bd_id=bd_id)
            elif evi_id:
                cli_cmd += ' evi {evi_id}'.format(evi_id=evi_id)
            elif vlan_id:
                cli_cmd += ' vlan {vlan_id}'.format(vlan_id=vlan_id)

            if mac_ip_type:
                cli_cmd += ' {mac_ip_type}'.format(mac_ip_type=mac_ip_type)
            elif mac_addr:
                cli_cmd += ' mac {mac_addr}'.format(mac_addr=mac_addr)
                if ip_addr:
                    cli_cmd += ' address {ip_addr}'.format(ip_addr=ip_addr)
            elif ip_addr:
                cli_cmd += ' address {ip_addr}'.format(ip_addr=ip_addr)

            cli_output = self.device.execute(cli_cmd)
        else:
            cli_output = output

        if not cli_output:
            return {}

        # Case 1 - BD header
        #
        # IP Address                EVI   BD    MAC Address    Next Hop(s)
        # ------------------------- ----- ----- -------------- -------------------------
        # 192.168.11.11             1     11    aabb.0011.0001 Et1/0:11
        # 2001:11::20               1     11    aabb.0011.0021 Duplicate
        # 2001:12::11               2     12    aabb.0012.0002 2.2.2.1
        #
        # Case 2 - VLAN header
        #
        # IP Address                EVI   VLAN  MAC Address    Next Hop(s)
        # ------------------------- ----- ----- -------------- -------------------------
        # 192.168.11.12             1     11    aabb.0011.0002 2.2.2.1
        # 2001:11::12               1     11    aabb.0011.0002 2.2.2.1
        #
        # Case 3 - Multiple Next Hops
        #
        # IP Address                EVI   BD    MAC Address    Next Hop(s)
        # ------------------------- ----- ----- -------------- -------------------------
        # 192.168.12.3              2     12    aabb.cc82.2800 Et1/0:12
        #                                                      3.3.3.1
        #                                                      5.5.5.1
        # 2001:12::3                2     12    aabb.cc82.2800 Et1/0:12
        #                                                      3.3.3.1
        #                                                      5.5.5.1
        #
        # Case 4 - Duplicate IP
        #
        # IP Address                EVI   BD    MAC Address    Next Hop(s)
        # ------------------------- ----- ----- -------------- -------------------------
        # 192.168.11.21             1     11    Duplicate      Et1/0:11
        p1 = re.compile(r'^IP Address\s+EVI\s+(BD|VLAN)\s+MAC Address\s+Next Hop\(s\)$')
        p2 = re.compile(r'^(?P<ip>[0-9a-fA-F\.:]+)\s+(?P<evi>\d+)\s+(?P<bd_id>\d+)\s+(?P<mac>[\d\w\.]+)\s+(?P<next_hop>.+)$')
        p3 = re.compile(r'^(?P<next_hop>.+)$')

        parser_dict = {}

        header_validated = False
        next_hops = None
        for line in cli_output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Sanity check the header appears in the expected order.
            m = p1.match(line)
            if m:
                header_validated = True
                continue

            # 192.168.12.3              2     12    aabb.cc82.2800 Et1/0:12
            m = p2.match(line)
            if m:
                group = m.groupdict()
                evi_dict = parser_dict.setdefault('evi', {})
                evis = evi_dict.setdefault(int(group['evi']), {})

                bd_id_dict = evis.setdefault('bd_id', {})
                bd_ids = bd_id_dict.setdefault(int(group['bd_id']), {})

                ip_addr_dict = bd_ids.setdefault('ip_addr', {})
                ip_vals = ip_addr_dict.setdefault(group['ip'], {})

                mac_addr_dict = ip_vals.setdefault( 'mac_addr', {})
                mac_addrs = mac_addr_dict.setdefault( group['mac'], {})

                next_hops = mac_addrs.setdefault('next_hops', [])
                next_hops.append(group['next_hop'])
                continue

            #                                                      3.3.3.1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                if next_hops:
                    next_hops.append(group['next_hop'])
                continue

        if not header_validated:
            return {}

        return parser_dict


# ===========================================
# Schema for 'show l2vpn evpn mac ip detail'
# ===========================================
class ShowL2vpnEvpnMacIpDetailSchema(MetaParser):
    """ Schema for show l2vpn evpn mac ip address {ipv4_addr} detail
                   show l2vpn evpn mac ip address {ipv6_addr} detail
                   show l2vpn evpn mac ip bridge-domain {bd_id} address {ipv4_addr}  detail
                   show l2vpn evpn mac ip bridge-domain {bd_id} address {ipv6_addr} detail
                   show l2vpn evpn mac ip bridge-domain {bd_id} detail
                   show l2vpn evpn mac ip bridge-domain {bd_id} duplicate detail
                   show l2vpn evpn mac ip bridge-domain {bd_id} local detail
                   show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ipv4_addr} detail
                   show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ipv6_addr} detail
                   show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} detail
                   show l2vpn evpn mac ip bridge-domain {bd_id} remote detail
                   show l2vpn evpn mac ip detail
                   show l2vpn evpn mac ip duplicate detail
                   show l2vpn evpn mac ip evi {evi_id} address {ipv4_addr} detail
                   show l2vpn evpn mac ip evi {evi_id} address {ipv6_addr} detail
                   show l2vpn evpn mac ip evi {evi_id} detail
                   show l2vpn evpn mac ip evi {evi_id} duplicate detail
                   show l2vpn evpn mac ip evi {evi_id} local detail
                   show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ipv4_addr} detail
                   show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ipv6_addr} detail
                   show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} detail
                   show l2vpn evpn mac ip evi {evi_id} remote detail
                   show l2vpn evpn mac ip local detail
                   show l2vpn evpn mac ip mac {mac_addr} address {ipv4_addr} detail
                   show l2vpn evpn mac ip mac {mac_addr} address {ipv6_addr} detail
                   show l2vpn evpn mac ip mac {mac_addr} detail
                   show l2vpn evpn mac ip remote detail
    """

    schema = {
        'evi': {
            Any(): {
                'bd_id': {
                    Any(): {
                        'eth_tag': {
                            Any(): {
                                'ip_addr': {
                                    Any(): {
                                        'mac_addr': {
                                            Any(): {
                                                'stale': bool,
                                                'esi': str,
                                                'next_hops': list,
                                                Optional('local_addr'): str,
                                                'seq_number': int,
                                                'ip_dup_detection': {
                                                    'status': str,
                                                    Optional('moves_count'): int,
                                                    Optional('moves_limit'): int,
                                                    Optional('expiry_time'): str,
                                                },
                                                Optional('last_local_mac_sent'): str,
                                                Optional('last_local_mac_learned'): str,
                                                Optional('last_remote_mac_received'): str,
                                                'label2_included': str,
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


# ===========================================
# Parser for 'show l2vpn evpn mac ip detail'
# ===========================================
class ShowL2vpnEvpnMacIpDetail(ShowL2vpnEvpnMacIpDetailSchema):
    """ Parser for show l2vpn evpn mac ip address {ipv4_addr} detail
                   show l2vpn evpn mac ip address {ipv6_addr} detail
                   show l2vpn evpn mac ip bridge-domain {bd_id} address {ipv4_addr}  detail
                   show l2vpn evpn mac ip bridge-domain {bd_id} address {ipv6_addr} detail
                   show l2vpn evpn mac ip bridge-domain {bd_id} detail
                   show l2vpn evpn mac ip bridge-domain {bd_id} duplicate detail
                   show l2vpn evpn mac ip bridge-domain {bd_id} local detail
                   show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ipv4_addr} detail
                   show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ipv6_addr} detail
                   show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} detail
                   show l2vpn evpn mac ip bridge-domain {bd_id} remote detail
                   show l2vpn evpn mac ip detail
                   show l2vpn evpn mac ip duplicate detail
                   show l2vpn evpn mac ip evi {evi_id} address {ipv4_addr} detail
                   show l2vpn evpn mac ip evi {evi_id} address {ipv6_addr} detail
                   show l2vpn evpn mac ip evi {evi_id} detail
                   show l2vpn evpn mac ip evi {evi_id} duplicate detail
                   show l2vpn evpn mac ip evi {evi_id} local detail
                   show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ipv4_addr} detail
                   show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ipv6_addr} detail
                   show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} detail
                   show l2vpn evpn mac ip evi {evi_id} remote detail
                   show l2vpn evpn mac ip local detail
                   show l2vpn evpn mac ip mac {mac_addr} address {ipv4_addr} detail
                   show l2vpn evpn mac ip mac {mac_addr} address {ipv6_addr} detail
                   show l2vpn evpn mac ip mac {mac_addr} detail
                   show l2vpn evpn mac ip remote detail
    """

    cli_command = ['show l2vpn evpn mac ip detail',
                    'show l2vpn evpn mac ip address {ip_addr} detail',
                    'show l2vpn evpn mac ip {mac_ip_type} detail',
                    'show l2vpn evpn mac ip mac {mac_addr} detail',
                    'show l2vpn evpn mac ip mac {mac_addr} address {ip_addr} detail',
                    'show l2vpn evpn mac ip bridge-domain {bd_id} detail',
                    'show l2vpn evpn mac ip bridge-domain {bd_id} address {ip_addr} detail',
                    'show l2vpn evpn mac ip bridge-domain {bd_id} {mac_ip_type} detail',
                    'show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} detail',
                    'show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ip_addr} detail',
                    'show l2vpn evpn mac ip evi {evi_id} detail',
                    'show l2vpn evpn mac ip evi {evi_id} address {ip_addr} detail',
                    'show l2vpn evpn mac ip evi {evi_id} {mac_ip_type} detail',
                    'show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} detail',
                    'show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ip_addr} detail',
     ]

    def cli(self, output=None, mac_addr=None, mac_ip_type=None, bd_id=None, evi_id=None, ip_addr=None):
        if not output:
            # Only these CLI options for mac_ip_type are supported.
            if mac_ip_type and mac_ip_type != 'local' and mac_ip_type != 'remote' and mac_ip_type != 'duplicate':
                raise Exception("Unsupported mac_ip_type {}".format(mac_ip_type))

            cli_cmd = 'show l2vpn evpn mac ip'

            if bd_id:
                cli_cmd += ' bridge-domain {bd_id}'.format(bd_id=bd_id)
            elif evi_id:
                cli_cmd += ' evi {evi_id}'.format(evi_id=evi_id)

            if mac_ip_type:
                cli_cmd += ' {mac_ip_type}'.format(mac_ip_type=mac_ip_type)
            elif mac_addr:
                cli_cmd += ' mac {mac_addr}'.format(mac_addr=mac_addr)
                if ip_addr:
                    cli_cmd += ' address {ip_addr}'.format(ip_addr=ip_addr)
            elif ip_addr:
                cli_cmd += ' address {ip_addr}'.format(ip_addr=ip_addr)

            cli_cmd += ' detail'

            cli_output = self.device.execute(cli_cmd)
        else:
            cli_output = output

        if not cli_output:
            return {}

        # IP Address:                192.168.11.21
        # IP Address:                2001:12::3
        # IP Address:                FE80::A8BB:FF:FE12:2 (stale)
        p1 = re.compile(r'^IP Address:\s+(?P<ip>[0-9a-fA-F\.:]+)(\s+(?P<ip_status>[\w\s\(\)]+))?$')

        # EVPN Instance:             1
        p2 = re.compile(r'^EVPN Instance:\s+(?P<evi>\d+)$')

        # Bridge Domain:             11
        # Vlan:                      11
        p3 = re.compile(r'^(Bridge Domain|Vlan):\s+(?P<bd_id>\d+)$')

        # MAC Address:               aabb.0012.0002
        p4 = re.compile(r'^MAC Address:\s+(?P<mac>[0-9a-fA-F\.]+)$')

        # Ethernet Segment:          03AA.BB00.0000.0200.0001
        p5 = re.compile(r'^Ethernet Segment:\s+(?P<esi>[0-9a-fA-F\.]+)$')

        # Ethernet Tag ID:           0
        p6 = re.compile(r'^Ethernet Tag ID:\s+(?P<eth_tag>\d+)$')

        # Next Hop(s):               L:17 Ethernet1/0 service instance 12
        #                            L:17 3.3.3.1
        #                            L:17 5.5.5.1
        p7 = re.compile(r'^Next Hop\(s\):\s+(?P<next_hop>[\w\/\s\.:-]+)$')
        p8 = re.compile(r'^(?P<next_hop>[\w\/\s\.:-]+)$')

        # Local Address:             4.4.4.1
        p9 = re.compile(r'^Local Address:\s+(?P<local_addr>[a-zA-Z0-9\.:]+)$')

        # Sequence Number:           0
        p10 = re.compile(r'^Sequence Number:\s+(?P<seq_number>\d+)$')

        # IP Duplication Detection:  Timer not running
        # IP Duplication Detection:  IP moves 4, limit 5
        #                            Timer expires in 09:19:15
        # IP Duplication Detection:  Duplicate IP address detected
        p11 = re.compile(r'^IP Duplication Detection:\s+(?P<ip_dup_status>[\w\d\s,]+)$')
        p12 = re.compile(r'^IP moves (?P<moves_count>\d+), limit (?P<moves_limit>\d+)$')
        p13 = re.compile(r'^Timer expires in (?P<expiry_time>[\d:]+)$')

        # Last Local MAC sent:       aabb.0011.0022
        p14 = re.compile(r'^Last Local MAC sent:\s+(?P<last_local_mac_sent>[0-9a-fA-F\.]+)$')

        # Last Local MAC learned:    aabb.0011.0022
        p15 = re.compile(r'^Last Local MAC learned:\s+(?P<last_local_mac_learned>[0-9a-fA-F\.]+)$')

        # Last Remote MAC received:  aabb.0011.0022
        p16 = re.compile(r'^Last Remote MAC received:\s+(?P<last_remote_mac_received>[0-9a-fA-F\.]+)$')

        # Label2 included:           No
        p17 = re.compile(r'^Label2 included:\s+(?P<label2_included>(Yes|No))$')

        parser_dict = {}

        for line in cli_output.splitlines():
            line = line.strip()
            if not line:
                continue

            # IP Address:                192.168.11.21
            # IP Address:                2001:12::3
            # IP Address:                FE80::A8BB:FF:FE12:2 (stale)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ip_addr_value = group['ip']
                stale = False
                if group['ip_status']:
                    stale = 'stale' in group['ip_status']
                continue

            # EVPN Instance:             1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                evi_dict = parser_dict.setdefault( 'evi', {})
                evis = evi_dict.setdefault( int(group['evi']), {})
                continue

            # Bridge Domain:             11
            # Vlan:                      11
            m = p3.match(line)
            if m:
                group = m.groupdict()
                bd_id_dict = evis.setdefault('bd_id', {})
                bd_ids = bd_id_dict.setdefault( int(group['bd_id']), {})
                continue

            # MAC Address:               aabb.0012.0002
            m = p4.match(line)
            if m:
                group = m.groupdict()
                mac_addr_value = group['mac']
                continue

            # Ethernet Segment:          03AA.BB00.0000.0200.0001
            m = p5.match(line)
            if m:
                group = m.groupdict()
                esi_value = group['esi']
                continue

            # Ethernet Tag ID:           0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                eth_tag_dict = bd_ids.setdefault('eth_tag', {})
                eth_tags = eth_tag_dict.setdefault( int(group['eth_tag']), {})

                ip_addr_dict = eth_tags.setdefault('ip_addr', {})
                ip_vals = ip_addr_dict.setdefault(ip_addr_value, {})

                mac_addr_dict = ip_vals.setdefault( 'mac_addr', {})
                mac_addrs = mac_addr_dict.setdefault( mac_addr_value, {})
                mac_addrs.update({
                    'stale': stale,
                    'esi': esi_value
                })
                continue

            # Next Hop(s):               L:17 Ethernet1/0 service instance 12
            m = p7.match(line)
            if m:
                group = m.groupdict()
                next_hops = mac_addrs.setdefault('next_hops', [])
                next_hops.append(group['next_hop'])
                continue

            # Local Address:             4.4.4.1
            m = p9.match(line)
            if m:
                group = m.groupdict()
                mac_addrs.update({'local_addr': group['local_addr']})
                continue

            # Sequence Number:           0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                mac_addrs.update({'seq_number': int(group['seq_number'])})
                continue

            # IP Duplication Detection:  Timer not running
            # IP Duplication Detection:  IP moves 4, limit 5
            # IP Duplication Detection:  Duplicate IP address detected
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ip_dup_status = group['ip_dup_status']
                ip_dup_vals = mac_addrs.setdefault('ip_dup_detection', {})
                ip_dup_vals.update({'status': ip_dup_status})

                m = p12.match(ip_dup_status)
                if m:
                    group = m.groupdict()
                    ip_dup_vals.update({
                        'moves_count': int(group['moves_count']),
                        'moves_limit': int(group['moves_limit']),
                    })
                continue

            #                            Timer expires in 09:19:15
            m = p13.match(line)
            if m:
                group = m.groupdict()
                ip_dup_vals.update({'expiry_time': group['expiry_time']})
                continue

            # Last Local MAC sent:       aabb.0011.0022
            m = p14.match(line)
            if m:
                group = m.groupdict()
                mac_addrs.update({'last_local_mac_sent': group['last_local_mac_sent']})
                continue

            # Last Local MAC learned:    aabb.0011.0022
            m = p15.match(line)
            if m:
                group = m.groupdict()
                mac_addrs.update({'last_local_mac_learned': group['last_local_mac_learned']})
                continue

            # Last Remote MAC received:  aabb.0011.0022
            m = p16.match(line)
            if m:
                group = m.groupdict()
                mac_addrs.update({'last_remote_mac_received': group['last_remote_mac_received']})
                continue

            # MAC only present:           Yes
            m = p17.match(line)
            if m:
                group = m.groupdict()
                mac_addrs.update({'label2_included': group['label2_included']})
                continue

            # Check this pattern last as it can match other fields.
            #                            L:17 5.5.5.1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                next_hops.append(group['next_hop'])
                continue

        return parser_dict


# ============================================
# Schema for 'show l2vpn evpn mac ip summary'
# ============================================
class ShowL2vpnEvpnMacIpSummarySchema(MetaParser):
    """ Schema for show l2vpn evpn mac ip bridge-domain {bd_id} duplicate summary
                   show l2vpn evpn mac ip bridge-domain {bd_id} local summary
                   show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} summary
                   show l2vpn evpn mac ip bridge-domain {bd_id} remote summary
                   show l2vpn evpn mac ip bridge-domain {bd_id} summary
                   show l2vpn evpn mac ip duplicate summary
                   show l2vpn evpn mac ip evi {evi_id} duplicate summary
                   show l2vpn evpn mac ip evi {evi_id} local summary
                   show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} summary
                   show l2vpn evpn mac ip evi {evi_id} remote summary
                   show l2vpn evpn mac ip evi {evi_id} summary
                   show l2vpn evpn mac ip local summary
                   show l2vpn evpn mac ip mac {mac_addr} summary
                   show l2vpn evpn mac ip remote summary
                   show l2vpn evpn mac ip summary
    """

    schema = {
        'evi': {
            int: {
                'bd_id': {
                    int: {
                        'eth_tag': {
                            int: {
                                Optional('remote_count'): int,
                                Optional('local_count'): int,
                                Optional('dup_count'): int,
                            },
                        },
                    },
                },
            },
        },
        Optional('total'): {
            Optional('remote_count'): int,
            Optional('local_count'): int,
            Optional('dup_count'): int,
        }
    }


# ============================================
# Parser for 'show l2vpn evpn mac ip summary'
# ============================================
class ShowL2vpnEvpnMacIpSummary(ShowL2vpnEvpnMacIpSummarySchema):
    """ Parser for show l2vpn evpn mac ip bridge-domain {bd_id} duplicate summary
                   show l2vpn evpn mac ip bridge-domain {bd_id} local summary
                   show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} summary
                   show l2vpn evpn mac ip bridge-domain {bd_id} remote summary
                   show l2vpn evpn mac ip bridge-domain {bd_id} summary
                   show l2vpn evpn mac ip duplicate summary
                   show l2vpn evpn mac ip evi {evi_id} duplicate summary
                   show l2vpn evpn mac ip evi {evi_id} local summary
                   show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} summary
                   show l2vpn evpn mac ip evi {evi_id} remote summary
                   show l2vpn evpn mac ip evi {evi_id} summary
                   show l2vpn evpn mac ip local summary
                   show l2vpn evpn mac ip mac {mac_addr} summary
                   show l2vpn evpn mac ip remote summary
                   show l2vpn evpn mac ip summary
    """

    cli_command = ['show l2vpn evpn mac ip summary',
                    'show l2vpn evpn mac ip {mac_ip_type} summary',
                    'show l2vpn evpn mac ip mac {mac_addr} summary',
                    'show l2vpn evpn mac ip bridge-domain {bd_id} summary',
                    'show l2vpn evpn mac ip bridge-domain {bd_id} {mac_ip_type} summary',
                    'show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} summary',
                    'show l2vpn evpn mac ip evi {evi_id} summary',
                    'show l2vpn evpn mac ip evi {evi_id} {mac_ip_type} summary',
                    'show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} summary',
     ]

    def cli(self, output=None, mac_ip_type=None, bd_id=None, evi_id=None, mac_addr=None):
        if not output:
            # Only these CLI options for mac_ip_type are supported.
            if mac_ip_type and mac_ip_type != 'local' and mac_ip_type != 'remote' and mac_ip_type != 'duplicate':
                raise Exception("Unsupported mac_ip_type {}".format(mac_ip_type))

            cli_cmd = 'show l2vpn evpn mac ip'

            if bd_id:
                cli_cmd += ' bridge-domain {bd_id}'.format(bd_id=bd_id)
            elif evi_id:
                cli_cmd += ' evi {evi_id}'.format(evi_id=evi_id)

            if mac_ip_type:
                cli_cmd += ' {mac_ip_type}'.format(mac_ip_type=mac_ip_type)
            elif mac_addr:
                cli_cmd += ' mac {mac_addr}'.format(mac_addr=mac_addr)

            cli_cmd += ' summary'

            cli_output = self.device.execute(cli_cmd)
        else:
            cli_output = output

        if not cli_output:
            return {}

        # PE1#show l2vpn evpn mac ip bridge-domain 11 duplicate summary
        # EVI   BD    Ether Tag  Dup IP     
        # ----- ----- ---------- ---------- 
        # 1     11    0          1         
        #
        # PE1#show l2vpn evpn mac ip bridge-domain 11 summary
        # EVI   BD    Ether Tag  Remote IP  Local IP   Dup IP
        # ----- ----- ---------- ---------- ---------- ----------
        # 1     11    0          4          5          1
        #
        # PE1#show l2vpn evpn mac ip evi 1 remote summary
        # EVI   BD    Ether Tag  Remote IP  
        # ----- ----- ---------- ---------- 
        # 1     11    0          4         
        #
        # Total                  4
        #
        # PE1#show l2vpn evpn mac ip summary
        # EVI   BD    Ether Tag  Remote IP  Local IP   Dup IP
        # ----- ----- ---------- ---------- ---------- ----------
        # 1     11    0          4          5          1
        # 2     12    0          2          2          0
        #
        # Total                  6          7          1
        #
        # VTEP1#show l2vpn evpn mac ip summary
        # EVI   VLAN  Ether Tag  Remote IP  Local IP   Dup IP
        # ----- ----- ---------- ---------- ---------- ----------
        # 1     11    0          2          0          0
        # 2     12    0          0          0          0
        #
        # Total                  2          0          0
        p1 = re.compile(r'^EVI\s+(BD|VLAN)\s+Ether Tag\s+Remote IP\s+Local IP\s+Dup IP$')
        p2 = re.compile(r'^EVI\s+(BD|VLAN)\s+Ether Tag\s+Remote IP$')
        p3 = re.compile(r'^EVI\s+(BD|VLAN)\s+Ether Tag\s+Local IP$')
        p4 = re.compile(r'^EVI\s+(BD|VLAN)\s+Ether Tag\s+Dup IP$')
        p5 = re.compile(r'^(?P<evi>\d+)\s+(?P<bd_id>\d+)\s+(?P<eth_tag>\d+)\s+(?P<remote_count>\d+)\s+(?P<local_count>\d+)\s+(?P<dup_count>\d+)$')
        p6 = re.compile(r'^(?P<evi>\d+)\s+(?P<bd_id>\d+)\s+(?P<eth_tag>\d+)\s+(?P<count>\d+)$')
        p7 = re.compile(r'^Total\s+(?P<remote_count>\d+)\s+(?P<local_count>\d+)\s+(?P<dup_count>\d+)$')
        p8 = re.compile(r'^Total\s+(?P<count>\d+)$')

        parser_dict = {}

        table_mac_ip_types = None
        for line in cli_output.splitlines():
            line = line.strip()
            if not line:
                continue

            # EVI   BD    Ether Tag  Remote MAC Local MAC  Dup MAC
            m = p1.match(line)
            if m:
                table_mac_ip_types = 'All'
                continue

            # EVI   BD    Ether Tag  Remote MAC 
            m = p2.match(line)
            if m:
                table_mac_ip_types = 'Remote'
                continue

            # EVI   BD    Ether Tag  Local MAC  
            m = p3.match(line)
            if m:
                table_mac_ip_types = 'Local'
                continue

            # EVI   BD    Ether Tag  Dup MAC    
            m = p4.match(line)
            if m:
                table_mac_ip_types = 'Dup'
                continue

            # 1     11    0          4          5          1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                evi_dict = parser_dict.setdefault('evi', {})
                evi_vals = evi_dict.setdefault(int(group['evi']), {})
                bd_id_dict = evi_vals.setdefault('bd_id', {})
                bd_vals = bd_id_dict.setdefault(int(group['bd_id']), {})
                eth_tag_dict = bd_vals.setdefault('eth_tag', {})
                eth_tag_vals = eth_tag_dict.setdefault(int(group['eth_tag']), {})
                if table_mac_ip_types == 'All':
                    eth_tag_vals.update({
                        'remote_count': int(group['remote_count']),
                        'local_count': int(group['local_count']),
                        'dup_count': int(group['dup_count']),
                    })
                continue

            # 1     11    0          1         
            m = p6.match(line)
            if m:
                group = m.groupdict()
                evi_dict = parser_dict.setdefault('evi', {})
                evi_vals = evi_dict.setdefault(int(group['evi']), {})
                bd_id_dict = evi_vals.setdefault('bd_id', {})
                bd_vals = bd_id_dict.setdefault(int(group['bd_id']), {})
                eth_tag_dict = bd_vals.setdefault('eth_tag', {})
                eth_tag_vals = eth_tag_dict.setdefault(int(group['eth_tag']), {})
                if table_mac_ip_types == 'Remote':
                    eth_tag_vals.update({
                        'remote_count': int(group['count']),
                    })
                elif table_mac_ip_types == 'Local':
                    eth_tag_vals.update({
                        'local_count': int(group['count']),
                    })
                elif table_mac_ip_types == 'Dup':
                    eth_tag_vals.update({
                        'dup_count': int(group['count']),
                    })
                continue

            # Total                  6          7          1
            m = p7.match(line)
            if m:
                group = m.groupdict()
                total_vals = parser_dict.setdefault('total', {})
                if table_mac_ip_types == 'All':
                    total_vals.update({
                        'remote_count': int(group['remote_count']),
                        'local_count': int(group['local_count']),
                        'dup_count': int(group['dup_count']),
                    })
                continue

            # Total                  4
            m = p8.match(line)
            if m:
                group = m.groupdict()
                total_vals = parser_dict.setdefault('total', {})
                if table_mac_ip_types == 'Remote':
                    total_vals.update({
                        'remote_count': int(group['count']),
                    })
                elif table_mac_ip_types == 'Local':
                    total_vals.update({
                        'local_count': int(group['count']),
                    })
                elif table_mac_ip_types == 'Dup':
                    total_vals.update({
                        'dup_count': int(group['count']),
                    })
                continue

        # Header must be invalid if this was never set.
        if not table_mac_ip_types:
            return {}

        return parser_dict

# ===========================================
# Schema for 'show storm-control {interface}'
# ===========================================
class ShowStormControlSchema(MetaParser):
    ''' Schema for
        show storm-control
        show storm-control {interface}
    '''

    schema = {
        'traffic_type': {
            Any(): {
                Optional('interfaces'): {
                    Any(): {
                        'interface': str,
                        'state': str,
                        'upper': Or(str, float),
                        'lower': Or(str, float),
                        'current': Or(str, float),
                        'action': str
                    }
                },
                Optional('interface'): str,
                Optional('state'): str,
                Optional('upper'): Or(str, float),
                Optional('lower'): Or(str, float),
                Optional('current'): Or(str, float),
                Optional('action'): str
            },
        }
    }


# ===========================================
# Parser for 'show storm-control {interface}'
# ===========================================
class ShowStormControl(ShowStormControlSchema):
    ''' Parser for
        show storm-control
        show storm-control {interface}
    '''
    cli_command = ['show storm-control',
                   'show storm-control {interface}']

    def cli(self, interface=None, output=None):
        if output is None:
            if interface:
                output = self.device.execute(
                    self.cli_command[1].format(interface=interface))
            else:
                output = self.device.execute(self.cli_command[0])

        ret_dict = {}

        # Te1/0/3         Forwarding           5.00%        1.00%          2.00%    Shutdown     B
        # Te1/0/3         Forwarding           5.00%        1.00%          3.00%    Shutdown     M
        # Gi0/2/0         Link Down            0.70%        0.70%          0.00%    Shutdown     B
        # Gi1/0/3         Forwarding           1k pps       1k pps         0 pps        None     U
        # Gi1/0/3         Forwarding           950 pps      950 pps        0 pps        None    UU
        p1 = re.compile(
            r'^(?P<interface>(\S+))\s+(?P<state>([A-Za-z]+\s?[A-Za-z]+))\s+(?P<upper>[\d\w\.]+)\s?(%|pps|bps)\s+(?P<lower>[\d\w\.]+)\s?(%|pps|bps)\s+(?P<current>[\d\w\.]+)\s?(%|pps|bps)\s+(?P<action>\S+)\s+(?P<type>\S+)')

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            # Te1/0/3         Forwarding           5.00%        1.00%          2.00%    Shutdown     B
            # Te1/0/3         Forwarding           5.00%        1.00%          3.00%    Shutdown     M
            # Gi0/2/0         Link Down            0.70%        0.70%          0.00%    Shutdown     B
            # Gi1/0/3         Forwarding           1k pps       1k pps         0 pps        None     U
            # Gi1/0/3         Forwarding           950 pps      950 pps        0 pps        None    UU
            if m:
                group = m.groupdict()
                traffic_type = str(group['type'])
                if not interface:
                    intf = group['interface']
                    control_dict = ret_dict.setdefault(
                        'traffic_type', {}).setdefault(
                        traffic_type, {}).setdefault(
                        'interfaces', {}).setdefault(intf, {})
                else:
                    control_dict = ret_dict.setdefault(
                        'traffic_type', {}).setdefault(traffic_type, {})

                control_dict['interface'] = str(group['interface'])
                control_dict['state'] = str(group['state'])

                try:
                    control_dict['upper'] = float(group['upper'])
                except ValueError:
                    control_dict['upper'] = str(group['upper'])

                try:
                    control_dict['lower'] = float(group['lower'])
                except ValueError:
                    control_dict['lower'] = str(group['lower'])

                try:
                    control_dict['current'] = float(group['current'])
                except ValueError:
                    control_dict['current'] = str(group['current'])

                control_dict['action'] = str(group['action'])
                continue

        return ret_dict


# ===============================================
# Schema for 'show l2vpn evpn peers vxlan detail'
# ===============================================
class ShowL2vpnEvpnPeersVxlanDetailSchema(MetaParser):
    """ Schema for show l2vpn evpn peers vxlan detail
                   show l2vpn evpn peers vxlan address <peer_addr> detail
                   show l2vpn evpn peers vxlan global detail
                   show l2vpn evpn peers vxlan global address <peer_addr> detail
                   show l2vpn evpn peers vxlan vni <vni_id> detail
                   show l2vpn evpn peers vxlan vni <vni_id> address <peer_addr> detail
                   show l2vpn evpn peers vxlan interface <nve_interface> detail
                   show l2vpn evpn peers vxlan interface <nve_interface> address <peer_addr> detail
    """

    schema = {
        'peer_address': {
            Any(): {
                'peer_vni': {
                    Any(): {
                        'local_vni': str,
                        'interface': str,
                        'up_time': str,
                        Optional('number_of_routes'): {
                            Optional('ead_per_evi'): int,
                            Optional('mac'): int,
                            Optional('mac_ip'): int,
                            Optional('imet'): int,
                            Optional('es'): int,
                            Optional('ead_per_es'): int,
                            Optional('total'): int,
                        }
                    },
                },
            },
        },
    }


# ===============================================
# Parser for 'show l2vpn evpn peers vxlan detail'
# ===============================================
class ShowL2vpnEvpnPeersVxlanDetail(ShowL2vpnEvpnPeersVxlanDetailSchema):
    """ Parser for show l2vpn evpn peers vxlan detail
                   show l2vpn evpn peers vxlan address <peer_addr> detail
                   show l2vpn evpn peers vxlan global detail
                   show l2vpn evpn peers vxlan global address <peer_addr> detail
                   show l2vpn evpn peers vxlan vni <vni_id> detail
                   show l2vpn evpn peers vxlan vni <vni_id> address <peer_addr> detail
                   show l2vpn evpn peers vxlan interface <nve_interface> detail
                   show l2vpn evpn peers vxlan interface <nve_interface> address <peer_addr> detail
    """

    cli_command = ['show l2vpn evpn peers vxlan detail',
                   'show l2vpn evpn peers vxlan address {peer_addr} detail',
                   'show l2vpn evpn peers vxlan global detail',
                   'show l2vpn evpn peers vxlan global address {peer_addr} detail',
                   'show l2vpn evpn peers vxlan vni {vni_id} detail',
                   'show l2vpn evpn peers vxlan vni {vni_id} address {peer_addr} detail',
                   'show l2vpn evpn peers vxlan interface {nve_interface} detail',
                   'show l2vpn evpn peers vxlan interface {nve_interface} address {peer_addr} detail']

    def cli(self, peer_addr=None, vni_id=None, nve_intf=None, glob=None, output=None):

        # Init vars
        parsed_dict = {}

        if output is None:
            # Execute command
            if glob and peer_addr:
                output = self.device.execute(
                    self.cli_command[3].format(peer_addr=peer_addr))
            elif glob:
                output = self.device.execute(self.cli_command[2])
            elif nve_intf and peer_addr:
                output = self.device.execute(
                    self.cli_command[7].format(nve_interface=nve_intf, peer_addr=peer_addr))
            elif nve_intf:
                output = self.device.execute(
                    self.cli_command[6].format(nve_interface=nve_intf))
            elif vni_id and peer_addr:
                output = self.device.execute(
                    self.cli_command[5].format(vni_id=vni_id, peer_addr=peer_addr))
            elif vni_id:
                output = self.device.execute(
                    self.cli_command[4].format(vni_id=vni_id))
            elif peer_addr:
                output = self.device.execute(
                    self.cli_command[1].format(peer_addr=peer_addr))
            else:
                output = self.device.execute(self.cli_command[0])

        # Interface:        nve1
        # Interface:        Global
        p1 = re.compile(r'^Interface:\s+(?P<name>\w*)$')

        # Local VNI:        20011
        # Local VNI:        N/A
        p2 = re.compile(r'^Local VNI:\s+((?P<vni>\d+)|N/A)$')

        # Peer VNI:         20011
        # Peer VNI:         N/A
        p3 = re.compile(r'^Peer VNI:\s+((?P<vni>\d+)|N/A)$')

        # Peer IP Address:  11.11.11.2
        p4 = re.compile(r'^Peer IP Address:\s+(?P<address>[0-9a-fA-F\.:]+)$')

        # UP time:          1w6d
        # UP time:          00:15:49
        p5 = re.compile(r'^UP time:\s+(?P<time>[\w:]*)$')

        # Number of routes
        p6 = re.compile(r'^Number of routes$')

        # EAD per-EVI:    0
        p7 = re.compile(r'^EAD per-EVI:\s+(?P<routes>\d+)$')

        # MAC:            1
        p8 = re.compile(r'^MAC:\s+(?P<routes>\d+)$')

        # MAC/IP:         0
        p9 = re.compile(r'^MAC/IP:\s+(?P<routes>\d+)$')

        # IMET:           1
        p10 = re.compile(r'^IMET:\s+(?P<routes>\d+)$')

        # Total:          1
        p11 = re.compile(r'^Total:\s+(?P<routes>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Interface:        nve1
            # Interface:        Global
            m = p1.match(line)
            if m:
                interface = str(m.groupdict()['name'])
                continue

            # Local VNI:        20011
            # Local VNI:        N/A
            m = p2.match(line)
            if m:
                if m.groupdict()['vni']:
                    local_vni = str(m.groupdict()['vni'])
                else:
                    local_vni = 'N/A'
                continue

            # Peer VNI:         20011
            # Peer VNI:         N/A
            m = p3.match(line)
            if m:
                if m.groupdict()['vni']:
                    peer_vni = str(m.groupdict()['vni'])
                else:
                    peer_vni = 'N/A'
                continue

            # Peer IP Address:  11.11.11.2
            m = p4.match(line)
            if m:
                peer_address = str(m.groupdict()['address'])
                peer_dict = parsed_dict.setdefault('peer_address', {}).\
                                        setdefault(peer_address, {})
                peer_vni_dict = peer_dict.setdefault('peer_vni', {}).\
                                          setdefault(peer_vni, {})
                peer_vni_dict['local_vni'] = local_vni
                peer_vni_dict['interface'] = interface
                continue

            # UP time:          1w6d
            m = p5.match(line)
            if m:
                peer_vni_dict['up_time'] = str(m.groupdict()['time'])
                continue

            # Number of routes
            m = p6.match(line)
            if m:
                routes_dict = peer_vni_dict.setdefault('number_of_routes', {})
                continue

            # EAD per-EVI:    0
            m = p7.match(line)
            if m:
                routes_dict['ead_per_evi'] = int(m.groupdict()['routes'])
                continue

            # MAC:            1
            m = p8.match(line)
            if m:
                routes_dict['mac'] = int(m.groupdict()['routes'])
                continue

            # MAC/IP:         0
            m = p9.match(line)
            if m:
                routes_dict['mac_ip'] = int(m.groupdict()['routes'])
                continue

            # IMET:           1
            m = p10.match(line)
            if m:
                routes_dict['imet'] = int(m.groupdict()['routes'])
                continue

            # Total:          1
            m = p11.match(line)
            if m:
                routes_dict['total'] = int(m.groupdict()['routes'])
                continue

        return parsed_dict


# ===================================================
# Schema for 'show l2vpn evpn default-gateway detail'
# ===================================================
class ShowL2vpnEvpnDefaultGatewayDetailSchema(MetaParser):
    """ Schema for show l2vpn evpn default-gateway detail
                   show l2vpn evpn default-gateway evi <evi_id> detail
                   show l2vpn evpn default-gateway bridge-domain {bd_id} detail
                   show l2vpn evpn default-gateway vlan <vlan_id> detail
    """

    schema = {
        'evi': {
            Any(): {
                'bd_id': {
                    Any(): {
                        'dg_addr': {
                            Any(): {
                                'source': {
                                    Any(): {
                                        Optional('eth_tag'): int,
                                        'mac_addr': str,
                                        'valid': bool,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# ===================================================
# Parser for 'show l2vpn evpn default-gateway detail'
# ===================================================
class ShowL2vpnEvpnDefaultGatewayDetail(ShowL2vpnEvpnDefaultGatewayDetailSchema):
    """ Parser for show l2vpn evpn default-gateway detail
                   show l2vpn evpn default-gateway evi <evi_id> detail
                   show l2vpn evpn default-gateway bridge-domain {bd_id} detail
                   show l2vpn evpn default-gateway vlan <vlan_id> detail
    """

    cli_command = ['show l2vpn evpn default-gateway detail',
                   'show l2vpn evpn default-gateway evi {evi_id} detail',
                   'show l2vpn evpn default-gateway bridge-domain {bd_id} detail',
                   'show l2vpn evpn default-gateway vlan {vlan_id} detail']

    def cli(self, evi_id=None, bd_id=None, vlan_id=None, output=None):

        # Init vars
        parsed_dict = {}
        valid = True

        if output is None:
            # Execute command
            if evi_id:
                output = self.device.execute(
                    self.cli_command[1].format(evi_id=evi_id))
            elif bd_id:
                output = self.device.execute(
                    self.cli_command[2].format(bd_id=bd_id))
            elif vlan_id:
                output = self.device.execute(
                    self.cli_command[3].format(vlan_id=vlan_id))
            else:
                output = self.device.execute(self.cli_command[0])

        # Default Gateway Address:   10.3.1.254 (invalid)
        p0 = re.compile(r'^Default Gateway Address:\s+(?P<address>[0-9a-fA-F\.:]+)\s+\(invalid\)$')

        # Default Gateway Address:   10.3.1.254
        p1 = re.compile(r'^Default Gateway Address:\s+(?P<address>[0-9a-fA-F\.:]+)$')

        # EVPN Instance:             103
        p2 = re.compile(r'^EVPN Instance:\s+(?P<evi>\d+)$')

        # Vlan:                      103
        # Bridge Domain:             103
        p3 = re.compile(r'^(Vlan|Bridge Domain):\s+(?P<bd_id>\d+)$')

        # MAC Address:               549f.c6f4.53bf
        p4 = re.compile(r'^MAC Address:\s+(?P<mac>[0-9a-fA-F\.]+)$')

        # Ethernet Tag ID:           0
        p5 = re.compile(r'^Ethernet Tag ID:\s+(?P<etag>\d+)$')

        # Source:                    V:2000103 Vlan103
        # Source:                    V:2000103 20.0.101.1
        p6 = re.compile(r'^Source:\s+(?P<source>[\w\.\: ]+)$')

        for line in output.splitlines():
            line = line.strip()

            # Default Gateway Address:   10.3.1.254 (invalid)
            m = p0.match(line)
            if m:
                dg_address = str(m.groupdict()['address'])
                valid = False
                continue

            # Default Gateway Address:   10.3.1.254
            m = p1.match(line)
            if m:
                dg_address = str(m.groupdict()['address'])
                continue

            # EVPN Instance:             103
            m = p2.match(line)
            if m:
                evi = int(m.groupdict()['evi'])
                evi_dict = parsed_dict.setdefault('evi', {}).\
                                       setdefault(evi, {})
                continue

            # Vlan:                      103
            # Bridge Domain:             103
            m = p3.match(line)
            if m:
                bd_id = int(m.groupdict()['bd_id'])
                bd_dict = evi_dict.setdefault('bd_id', {}).\
                                   setdefault(bd_id, {})
                dg_dict = bd_dict.setdefault('dg_addr', {}).\
                                  setdefault(dg_address, {})
                continue

            # MAC Address:               549f.c6f4.53bf
            m = p4.match(line)
            if m:
                mac_address = str(m.groupdict()['mac'])
                continue

            # Ethernet Tag ID:           0
            m = p5.match(line)
            if m:
                eth_tag = int(m.groupdict()['etag'])
                continue

            # Source:                    V:2000103 Vlan103
            # Source:                    V:2000103 20.0.101.1
            m = p6.match(line)
            if m:
                source = str(m.groupdict()['source'])
                source_dict = dg_dict.setdefault('source', {}).\
                                      setdefault(source, {})
                source_dict['mac_addr'] = mac_address
                source_dict['eth_tag'] = eth_tag
                source_dict['valid'] = valid
                continue

        return parsed_dict


class ShowL2vpnEvpnDefaultGateway(ShowL2vpnEvpnDefaultGatewayDetailSchema):
    """ 
        Parser for show l2vpn evpn default-gateway
    """

    cli_command = 'show l2vpn evpn default-gateway'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Y   192.168.1.201             1     201   a0f8.4910.bccc Vl201
        p1 = re.compile(r'^(?P<valid>\w+)\s+(?P<dg_addr>\S+)\s+(?P<evi>\d+)\s+(?P<vlan>\d+)\s+(?P<mac_addr>\S+)\s+(?P<source>\S+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Y   192.168.1.201             1     201   a0f8.4910.bccc Vl201
            m = p1.match(line)
            if m:
                reg_dict = m.groupdict()
                source_dict = ret_dict.setdefault('evi', {}).setdefault(reg_dict['evi'], {}).setdefault('bd_id', {}).setdefault(reg_dict['vlan'], {}).setdefault('dg_addr', {}).setdefault(reg_dict['dg_addr'], {}).setdefault('source', {}).setdefault(reg_dict['source'], {})
                source_dict['mac_addr'] = reg_dict['mac_addr']
                source_dict['valid'] = reg_dict['valid'] == 'Y'
                continue

        return ret_dict


# ====================================================
# Schema for 'show l2vpn evpn default-gateway summary'
# ====================================================
class ShowL2vpnEvpnDefaultGatewaySummarySchema(MetaParser):
    """ Schema for show l2vpn evpn default-gateway summary
                   show l2vpn evpn default-gateway evi <evi_id> summary
                   show l2vpn evpn default-gateway bridge-domain {bd_id} summary
                   show l2vpn evpn default-gateway vlan <vlan_id> summary
    """

    schema = {
        'evi': {
            int: {
                'bd_id': {
                    int: {
                        'eth_tag': int,
                        'remote_dg': int,
                        'local_dg': int,
                    },
                },
            },
        },
        Optional('total'): {
            Optional('remote_dg'): int,
            Optional('local_dg'): int,
        }
    }


# ====================================================
# Parser for 'show l2vpn evpn default-gateway summary'
# ====================================================
class ShowL2vpnEvpnDefaultGatewaySummary(ShowL2vpnEvpnDefaultGatewaySummarySchema):
    """ Parser for show l2vpn evpn default-gateway summary
                   show l2vpn evpn default-gateway evi <evi_id> summary
                   show l2vpn evpn default-gateway bridge-domain {bd_id} summary
                   show l2vpn evpn default-gateway vlan <vlan_id> summary
    """

    cli_command = ['show l2vpn evpn default-gateway summary',
                   'show l2vpn evpn default-gateway evi {evi_id} summary',
                   'show l2vpn evpn default-gateway bridge-domain {bd_id} summary',
                   'show l2vpn evpn default-gateway vlan {vlan_id} summary']

    def cli(self, evi_id=None, bd_id=None, vlan_id=None, output=None):

        # Init vars
        parsed_dict = {}

        if output is None:
            # Execute command
            if evi_id:
                output = self.device.execute(
                    self.cli_command[1].format(evi_id=evi_id))
            elif bd_id:
                output = self.device.execute(
                    self.cli_command[2].format(bd_id=bd_id))
            elif vlan_id:
                output = self.device.execute(
                    self.cli_command[3].format(vlan_id=vlan_id))
            else:
                output = self.device.execute(self.cli_command[0])

        # 103   103   0          4          4
        p1 = re.compile(r'^(?P<evi>\d+)\s+(?P<bd_id>\d+)\s+(?P<eth_tag>\d+)\s+(?P<remote_dg>\d+)\s+(?P<local_dg>\d+)$')

        # Total                  4          4
        p2 = re.compile(r'^Total\s+(?P<remote_dg>\d+)\s+(?P<local_dg>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # 103   103   0          4          4
            m = p1.match(line)
            if m:
                group = m.groupdict()
                evi_dict = parsed_dict.setdefault('evi', {}).\
                                       setdefault(int(group['evi']), {})
                bd_dict = evi_dict.setdefault('bd_id', {}).\
                                      setdefault(int(group['bd_id']), {})
                bd_dict['eth_tag'] = int(group['eth_tag'])
                bd_dict['remote_dg'] = int(group['remote_dg'])
                bd_dict['local_dg'] = int(group['local_dg'])
                continue

            # Total                  4          4
            m = p2.match(line)
            if m:
                group = m.groupdict()
                total_vals = parsed_dict.setdefault('total', {})
                total_vals['remote_dg'] = int(group['remote_dg'])
                total_vals['local_dg'] = int(group['local_dg'])
                continue

        return parsed_dict


# ============================================
# Schema for 'show l2vpn atom preferred-path'
# ============================================
class ShowL2vpnAtomPreferredPathSchema(MetaParser):
    """ Schema for show l2vpn atom preferred-path """
    schema = {
        'vc_id': {
            Any(): {  # id of vc
                'peer_id': {
                    Any(): {  # id of peer
                        Optional('bandwidth'): {
                            'total': int,
                            'available': int,
                            'reserved': int
                        },
                        'interface': str,
                    }
                 }
            }
        }
    }

# ==================================================
# Parser for 'show l2vpn atom preferred-path'
# ==================================================
class ShowL2vpnAtomPreferredPath(ShowL2vpnAtomPreferredPathSchema):
    """ Parser for: show l2vpn atom preferred-path """

    cli_command = 'show l2vpn atom preferred-path'

    def cli(self, output=None):

        # initial return dictionary
        ret_dict = {}

        if output is None:
            # Execute command
            output = self.device.execute(self.cli_command)

        # Tunnel interface    Bandwidth Tot/Avail/Resv         Peer ID         VC ID
        # ------------------- -------------------------------- --------------- ----------
        # Tunnel1             500/100/400                      1.1.1.1         1
        # Tunnel65536                                          20.20.20.20     2

        p1 = re.compile(r'^(?P<interface>\S+) +(?:(?P<total_bandwidth>\d+)\/(?P<avail_bandwidth>\d+)'
                         '\/(?P<reserved_bandwidth>\d+))? +(?P<peer_id>[\d.]+) +(?P<vc_id>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                vc_id = group['vc_id']
                peer_id = group['peer_id']

                peer_id_dict = ret_dict.\
                    setdefault('vc_id', {}).\
                    setdefault(vc_id, {}).\
                    setdefault('peer_id', {}).\
                    setdefault(peer_id, {})

                peer_id_dict.update({'interface': group['interface']})

                if group['total_bandwidth'] and \
                   group['avail_bandwidth'] and \
                   group['reserved_bandwidth']:
                    bandwidth_dict = peer_id_dict.setdefault('bandwidth', {})
                    bandwidth_dict.update({
                        'total': int(group['total_bandwidth']),
                        'available': int(group['avail_bandwidth']),
                        'reserved': int(group['reserved_bandwidth'])
                    })

        return ret_dict

# ============================================
# Schema for 'show l2vpn evpn summary'
# ============================================
class ShowL2vpnEvpnSummarySchema(MetaParser):
    """ Schema for show l2vpn evpn summary """
    schema = {
        'evis': {
            'total': int,
            Optional('vlan_aware'): int,
            Optional('vlan_based'): int,
            Optional('vlan_bundle'): int,
        },
        'router_id': str,
        'glb_rep_type': str,
        'bgp': {
            'asn': int,
            'evpn_af_configured': bool,
        },
        'mac_addresses': {
            'local': int,
            'remote': int,
            'duplicate': int,
            'total': int,
        },
        'mac_dup': {
            'seconds': int,
            'limit': int,
        },
        Optional('bridge_domains'): int,
        Optional('label_alloc_mode'): str,
        Optional('arp_flood_suppression'): bool,
        Optional('dhcp_flood_suppression'): bool,
        Optional('core_connected'): bool,
        Optional('ip_dup'): {
            'seconds': int,
            'limit': int,
        },
        Optional('ip_addresses'): {
            'local': int,
            'remote': int,
            'duplicate': int,
            'total': int,
        },
        Optional('adv_def_gateway'): bool,
        Optional('def_gateway_addresses'): {
            'local': int,
            'remote': int,
            'total': int,
        },
        Optional('max_rt_per_ead_es'): int,
        Optional('mh_aliasing'): bool,
        Optional('glb_ip_local_learn'): bool,
        Optional('ip_local_learn_limit'): {
            'ipv4': int,
            'ipv6': int,
        },
        Optional('ip_local_learn_timer'): {
            'down': int,
            'poll': int,
            'reachable': int,
            'stale': int,
        },
        Optional('auto_rt'): str,
        Optional('adv_mcast'): bool,
    }

# ==================================================
# Parser for 'show l2vpn evpn summary'
# ==================================================
class ShowL2vpnEvpnSummary(ShowL2vpnEvpnSummarySchema):
    """ Parser for show l2vpn evpn summary """

    cli_command = 'show l2vpn evpn summary'

    def cli(self, output=None):

        # Init vars
        parsed_dict = {}
        mac_address = False
        ip_address = False
        dg_address = False
        ip_limits = False
        ip_timers = False

        if output is None:
            # Execute command
            output = self.device.execute(self.cli_command)


        # EVPN Instances (excluding point-to-point): 1
        p1 = re.compile(r'^EVPN Instances \(excluding point-to-point\):'
                        r'\s+(?P<evis>\d+)$')

        # VLAN Aware:   1
        p2 = re.compile(r'^VLAN Aware:\s+(?P<evis>\d+)$')

        # VLAN Based:   1
        p3 = re.compile(r'^VLAN Based:\s+(?P<evis>\d+)$')

        # VLAN Bundle:   1
        p4 = re.compile(r'^VLAN Bundle:\s+(?P<evis>\d+)$')

        # Vlans: 1
        # Bridge Domains: 10
        p5 = re.compile(r'^(Vlans|Bridge Domains): (?P<bds>\d+)$')

        # BGP: ASN 1, address-family l2vpn evpn configured
        p6 = re.compile(r'^BGP: ASN (?P<asn>\d+), '
                        r'address-family l2vpn evpn (?P<af>[\w ]+)$')

        # Router ID: 20.20.20.20
        p7 = re.compile(r'^Router ID:\s+(?P<id>[0-9a-fA-F\.:]+)$')

        # Label Allocation Mode: Per-BD
        p8 = re.compile(r'^Label Allocation Mode:\s+(?P<mode>[\w\-]+)$')

        # Global Replication Type: Static
        p9 = re.compile(r'^Global Replication Type:\s+(?P<type>[\w\- ]+)$')

        # ARP/ND Flooding Suppression: Enabled
        p10 = re.compile(r'^ARP\/ND Flooding Suppression:\s+(?P<enable>\w+)$')

        # DHCP Relay Flooding Suppression: Disabled
        p11 = re.compile(r'^DHCP Relay Flooding Suppression:'
                         r'\s+(?P<enable>\w+)$')

        # Connectivity to Core: UP
        p12 = re.compile(r'^Connectivity to Core:\s+(?P<status>\w+)$')

        # MAC Duplication: seconds 10 limit 100
        p13 = re.compile(r'^MAC Duplication: seconds (?P<seconds>\d+) '
                         r'limit (?P<limit>\d+)$')

        # MAC Addresses: 25
        p14 = re.compile(r'^MAC Addresses:\s+(?P<total>\d+)$')

        # IP Duplication: seconds 180 limit 5
        p15 = re.compile(r'^IP Duplication: seconds (?P<seconds>\d+) '
                         r'limit (?P<limit>\d+)$')

        # IP Addresses: 14
        p16 = re.compile(r'^IP Addresses:\s+(?P<total>\d+)$')

        # Advertise Default Gateway: No
        p17 = re.compile(r'^Advertise Default Gateway:\s+(?P<enable>\w+)$')

        # Default Gateway Addresses: 1
        p18 = re.compile(r'^Default Gateway Addresses:\s+(?P<total>\d+)$')

        # Local:     11
        p19 = re.compile(r'^Local:\s+(?P<local>\d+)$')

        # Remote:    12
        p20 = re.compile(r'^Remote:\s+(?P<remote>\d+)$')

        # Duplicate: 2
        p21 = re.compile(r'^Duplicate:\s+(?P<duplicate>\d+)$')

        # Maximum number of Route Targets per EAD-ES route: 200
        p22 = re.compile(r'^Maximum number of Route Targets '
                         r'per EAD-ES route: (?P<rts>\d+)$')

        # Multi-home aliasing: Enabled
        p23 = re.compile(r'^Multi-home aliasing:\s+(?P<enable>\w+)$')

        # Global IP Local Learn: Enabled
        p24 = re.compile(r'^Global IP Local Learn:\s+(?P<enable>[\w ]+)$')

        # IP local learning limits
        p25 = re.compile(r'^IP local learning limits$')

        # IPv4: 4 addresses per-MAC
        p26 = re.compile(r'^IPv4: (?P<ipv4>\d+) addresses per-MAC$')

        # IPv6: 12 addresses per-MAC
        p27 = re.compile(r'^IPv6: (?P<ipv6>\d+) addresses per-MAC$')

        # IP local learning timers
        p28 = re.compile(r'^IP local learning timers$')

        # Down:      10 minutes
        p29 = re.compile(r'^Down:\s+(?P<down>\d+) minutes$')

        # Poll:      1 minutes
        p30 = re.compile(r'^Poll:\s+(?P<poll>\d+) minutes$')

        # Reachable: 5 minutes
        p31 = re.compile(r'^Reachable:\s+(?P<reachable>\d+) minutes$')

        # Stale:     30 minutes
        p32 = re.compile(r'^Stale:\s+(?P<stale>\d+) minutes$')

        # Auto route-target: evi-id based
        p33 = re.compile(r'^Auto route-target:\s+(?P<type>[\w\- ]+)$')

        # Advertise Multicast: Yes
        p34 = re.compile(r'^Advertise Multicast:\s+(?P<enable>\w+)$')

        for line in output.splitlines():
            line = line.strip()

            # EVPN Instances (excluding point-to-point): 1
            m = p1.match(line)
            if m:
                evis_dict = parsed_dict.setdefault('evis', {})
                evis_dict['total'] = int(m.groupdict()['evis'])
                continue

            # VLAN Aware:   1
            m = p2.match(line)
            if m:
                evis_dict['vlan_aware'] = int(m.groupdict()['evis'])
                continue

            # VLAN Based:   1
            m = p3.match(line)
            if m:
                evis_dict['vlan_based'] = int(m.groupdict()['evis'])
                continue

            # VLAN Bundle:   1
            m = p4.match(line)
            if m:
                evis_dict['vlan_bundle'] = int(m.groupdict()['evis'])
                continue

            # Vlans: 1
            # Bridge Domains: 10
            m = p5.match(line)
            if m:
                parsed_dict['bridge_domains'] = int(m.groupdict()['bds'])
                continue

            # BGP: ASN 1, address-family l2vpn evpn configured
            m = p6.match(line)
            if m:
                bgp_dict = parsed_dict.setdefault('bgp', {})
                bgp_dict['asn'] = int(m.groupdict()['asn'])
                if m.groupdict()['af'] == 'configured':
                    bgp_dict['evpn_af_configured'] = True
                else:
                    bgp_dict['evpn_af_configured'] = False
                continue

            # Router ID: 20.20.20.20
            m = p7.match(line)
            if m:
                parsed_dict['router_id'] = str(m.groupdict()['id'])
                continue

            # Label Allocation Mode: Per-BD
            m = p8.match(line)
            if m:
                parsed_dict['label_alloc_mode'] = str(m.groupdict()['mode'])
                continue

            # Global Replication Type: Static
            m = p9.match(line)
            if m:
                parsed_dict['glb_rep_type'] = str(m.groupdict()['type'])
                continue

            # ARP/ND Flooding Suppression: Enabled
            m = p10.match(line)
            if m:
                if m.groupdict()['enable'].lower() == 'enabled':
                    parsed_dict['arp_flood_suppression'] = True
                else:
                    parsed_dict['arp_flood_suppression'] = False
                continue

            # DHCP Relay Flooding Suppression: Disabled
            m = p11.match(line)
            if m:
                if m.groupdict()['enable'].lower() == 'enabled':
                    parsed_dict['dhcp_flood_suppression'] = True
                else:
                    parsed_dict['dhcp_flood_suppression'] = False
                continue

            # Connectivity to Core: UP
            m = p12.match(line)
            if m:
                if m.groupdict()['status'].lower() == 'up':
                    parsed_dict['core_connected'] = True
                else:
                    parsed_dict['core_connected'] = False
                continue

            # MAC Duplication: seconds 10 limit 100
            m = p13.match(line)
            if m:
                mac_dup_dict = parsed_dict.setdefault('mac_dup', {})
                mac_dup_dict['seconds'] = int(m.groupdict()['seconds'])
                mac_dup_dict['limit'] = int(m.groupdict()['limit'])
                continue

            # MAC Addresses: 25
            m = p14.match(line)
            if m:
                mac_address = True
                mac_addr_dict = parsed_dict.setdefault('mac_addresses', {})
                mac_addr_dict['total'] = int(m.groupdict()['total'])
                continue

            # IP Duplication: seconds 180 limit 5
            m = p15.match(line)
            if m:
                ip_dup_dict = parsed_dict.setdefault('ip_dup', {})
                ip_dup_dict['seconds'] = int(m.groupdict()['seconds'])
                ip_dup_dict['limit'] = int(m.groupdict()['limit'])
                continue

            # IP Addresses: 14
            m = p16.match(line)
            if m:
                ip_address = True
                ip_addr_dict = parsed_dict.setdefault('ip_addresses', {})
                ip_addr_dict['total'] = int(m.groupdict()['total'])
                continue

            # Advertise Default Gateway: No
            m = p17.match(line)
            if m:
                if m.groupdict()['enable'].lower() == 'yes':
                    parsed_dict['adv_def_gateway'] = True
                else:
                    parsed_dict['adv_def_gateway'] = False
                continue

            # Default Gateway Addresses: 1
            m = p18.match(line)
            if m:
                dg_address = True
                dg_addr_dict = parsed_dict.setdefault('def_gateway_addresses',
                                                      {})
                dg_addr_dict['total'] = int(m.groupdict()['total'])
                continue

            # Local:     11
            m = p19.match(line)
            if m:
                if dg_address:
                    dg_addr_dict['local'] = int(m.groupdict()['local'])
                elif ip_address:
                    ip_addr_dict['local'] = int(m.groupdict()['local'])
                elif mac_address:
                    mac_addr_dict['local'] = int(m.groupdict()['local'])
                continue

            # Remote:    12
            m = p20.match(line)
            if m:
                if dg_address:
                    dg_addr_dict['remote'] = int(m.groupdict()['remote'])
                elif ip_address:
                    ip_addr_dict['remote'] = int(m.groupdict()['remote'])
                elif mac_address:
                    mac_addr_dict['remote'] = int(m.groupdict()['remote'])
                continue

            # Duplicate: 2
            m = p21.match(line)
            if m:
                dup = m.groupdict()['duplicate']
                if ip_address:
                    ip_addr_dict['duplicate'] = int(dup)
                elif mac_address:
                    mac_addr_dict['duplicate'] = int(dup)
                continue

            # Maximum number of Route Targets per EAD-ES route: 200
            m = p22.match(line)
            if m:
                parsed_dict['max_rt_per_ead_es'] = int(m.groupdict()['rts'])
                continue

            # Multi-home aliasing: Enabled
            m = p23.match(line)
            if m:
                if m.groupdict()['enable'].lower() == 'enabled':
                    parsed_dict['mh_aliasing'] = True
                else:
                    parsed_dict['mh_aliasing'] = False
                continue

            # Global IP Local Learn: Enabled
            m = p24.match(line)
            if m:
                if m.groupdict()['enable'].lower() == 'enabled':
                    parsed_dict['glb_ip_local_learn'] = True
                else:
                    parsed_dict['glb_ip_local_learn'] = False
                continue

            # IP local learning limits
            m = p25.match(line)
            if m:
                ip_limits = True
                ip_limit_dict = parsed_dict.setdefault('ip_local_learn_limit',
                                                       {})
                continue

            # IPv4: 4 addresses per-MAC
            m = p26.match(line)
            if m and ip_limits:
                ip_limit_dict['ipv4'] = int(m.groupdict()['ipv4'])
                continue

            # IPv6: 12 addresses per-MAC
            m = p27.match(line)
            if m and ip_limits:
                ip_limit_dict['ipv6'] = int(m.groupdict()['ipv6'])
                continue

            # IP local learning timers
            m = p28.match(line)
            if m:
                ip_timers = True
                ip_timer_dict = parsed_dict.setdefault('ip_local_learn_timer',
                                                       {})
                continue

            # Down:      10 minutes
            m = p29.match(line)
            if m and ip_timers:
                ip_timer_dict['down'] = int(m.groupdict()['down'])
                continue

            # Poll:      1 minutes
            m = p30.match(line)
            if m and ip_timers:
                ip_timer_dict['poll'] = int(m.groupdict()['poll'])
                continue

            # Reachable: 5 minutes
            m = p31.match(line)
            if m and ip_timers:
                ip_timer_dict['reachable'] = int(m.groupdict()['reachable'])
                continue

            # Stale:     30 minutes
            m = p32.match(line)
            if m and ip_timers:
                ip_timer_dict['stale'] = int(m.groupdict()['stale'])
                continue

            # Auto route-target: evi-id based
            m = p33.match(line)
            if m:
                parsed_dict['auto_rt'] = str(m.groupdict()['type'])
                continue

            # Advertise Multicast: Yes
            m = p34.match(line)
            if m:
                if m.groupdict()['enable'].lower() == 'yes':
                    parsed_dict['adv_mcast'] = True
                else:
                    parsed_dict['adv_mcast'] = False
                continue

        return parsed_dict

# ============================================
# Schema for 'show l2vpn evpn evi detail'
# ============================================
class ShowL2vpnEvpnEviDetailSchema(MetaParser):
    """ Schema for show l2vpn evpn evi detail """

    schema = {
        Any(): {
            'evi_type': str,
            'encap_type': str,
            'state': str,
            Optional('rd'): str,
            Optional('rd_type'): str,
            Optional('import_rt'): str,
            Optional('export_rt'): str,
            Optional('per_evi_label'): str,
            Optional('replication_type'): str,
            Optional('re_orig_rt5'): bool,
            Optional('ip_local_learn'): bool,
            Optional('adv_def_gateway'): bool,
            Optional('adv_mcast'): bool,
            Optional('bridge_domain'): {
                Any(): {
                    'etag': int,
                    'state': str,
                    Optional('flood_suppress'): bool,
                    Optional('core_if'): str,
                    Optional('access_if'): str,
                    Optional('nve_if'): str,
                    Optional('rmac'): str,
                    Optional('core_vlan'): int,
                    Optional('l2vni'): int,
                    Optional('l3vni'): int,
                    Optional('vtep_ip'): str,
                    Optional('vtep_ip_sec'): str,
                    Optional('mcast_ip'): str,
                    Optional('vrf'): str,
                    Optional('ipv4_irb'): bool,
                    Optional('ipv6_irb'): bool,
                    Optional('bum_label'): int,
                    Optional('per_bd_label'): int,
                    Optional('bdi_label'): int,
                    Optional('pseudo_port'): {
                        Any(): {
                            Optional('mac_routes'): int,
                            Optional('mac_ip_routes'): int,
                            Optional('per_ce_label'): int,
                            Optional('df_state'): str,
                            Optional('access_vfi'): str,
                            Optional('peer'): str,
                            Optional('vc'): int,
                            Optional('esi'): str,
                        },
                    },
                    Optional('peer'): {
                        Any(): {
                            'mac_routes': int,
                            'mac_ip_routes': int,
                            'imet_routes': int,
                            'ead_routes': int,
                        },
                    },
                },
            },
        },
    }


# ==================================================
# Parser for 'show l2vpn evpn evi detail'
# ==================================================
class ShowL2vpnEvpnEviDetail(ShowL2vpnEvpnEviDetailSchema):
    """ Parser for show l2vpn evpn evi detail """

    cli_command = ['show l2vpn evpn evi detail',
                   'show l2vpn evpn evi {evi} detail']

    def cli(self, evi=None, output=None):

        # Init vars
        parsed_dict = {}

        if output is None:
            # Execute command
            if evi:
                output = self.device.execute(
                    self.cli_command[1].format(evi=evi))
            else:
                output = self.device.execute(self.cli_command[0])
  

        # EVPN instance:       1 (VLAN Based)
        p1 = re.compile(r'^EVPN instance:\s+(?P<evi>\d+)\s+\((?P<type>.*)\)$')

        # RD:                20.20.20.20:1 (auto)
        p2 = re.compile(r'^RD:\s+(?P<rd>[0-9a-fA-F\.:]+)\s+\((?P<type>\w+)\)$')

        # Import-RTs:        1:1
        # Import-RTs:        1:100 995:95 997:97 998:98 999:99
        p3 = re.compile(r'^Import-RTs:\s+(?P<rt>[\d:\s]+)')

        # Export-RTs:        1:1
        # Export-RTs:        1:100 995:95 997:97 998:98 999:99
        p4 = re.compile(r'^Export-RTs:\s+(?P<rt>[\d:\s]+)')

        # Per-EVI Label:     none
        p5 = re.compile(r'^Per-EVI Label:\s+(?P<label>\d+|none)$')

        # State:             Established
        # State:             No BGP, Incomplete
        p6 = re.compile(r'^State:\s+(?P<state>[\w\s,]+)$')

        # Replication Type:  Static (global)
        p7 = re.compile(r'^Replication Type:\s+(?P<type>[\w\-\s]+)')

        # Encapsulation:     vxlan
        p8 = re.compile(r'^Encapsulation:\s+(?P<enctype>\w+)')

        # IP Local Learn:    Enabled (global)
        p9 = re.compile(r'^IP Local Learn:\s+(?P<enable>[\w\s]+)')

        # Adv. Def. Gateway: Disabled (global)
        p10 = re.compile(r'^Adv. Def. Gateway:\s+(?P<enable>\w+)')

        # Re-originate RT5:  Disabled
        p11 = re.compile(r'^Re-originate RT5:\s+(?P<enable>\w+)')

        # Adv. Multicast:    Enabled (global)
        p12 = re.compile(r'^Adv. Multicast:\s+(?P<enable>\w+)')

        # Vlan:              100
        # Bridge Domain:     1
        p13 = re.compile(r'^(Vlan|Bridge Domain):\s+(?P<bd_id>\d+)$')

        # Ethernet-Tag:    0
        p14 = re.compile(r'^Ethernet-Tag:\s+(?P<etag>\d+)$')

        # Flood Suppress:  Attached
        p15 = re.compile(r'^Flood Suppress:\s+(?P<attach>\w+)$')

        # Core If:         Vlan500
        p16 = re.compile(r'^Core If:\s+(?P<name>\w*)$')

        # Access If:       Vlan100
        p17 = re.compile(r'^Access If:\s+(?P<name>\w*)$')

        # NVE If:          nve1
        p18 = re.compile(r'^NVE If:\s+(?P<name>\w+)$')

        # RMAC:            0000.0000.0000
        p19 = re.compile(r'^RMAC:\s+(?P<mac>[A-Fa-f0-9:\.]+)$')

        # Core Vlan:       0
        p20 = re.compile(r'^Core Vlan:\s+(?P<vlan>\d+)$')

        # L2 VNI:          10000
        p21 = re.compile(r'^L2 VNI:\s+(?P<vni>\d+)$')

        # L3 VNI:          0
        p22 = re.compile(r'^L3 VNI:\s+(?P<vni>\d+)$')

        # VTEP IP:         1.20.20.20
        p23 = re.compile(r'^VTEP IP:\s+(?P<addr>UNKNOWN|[A-Fa-f0-9:\.]+)$')

        # MCAST IP:        227.0.0.1
        p24 = re.compile(r'^MCAST IP:\s+(?P<addr>UNKNOWN|[A-Fa-f0-9:\.]+)')

        # VRF:             Red
        p25 = re.compile(r'^VRF:\s+(?P<vrf>\w*)$')

        # IPv4 IRB:        Enabled (Asymmetric)
        p26 = re.compile(r'^IPv4 IRB:\s+(?P<enable>\w+)')

        # IPv6 IRB:        Disabled
        p27 = re.compile(r'^IPv6 IRB:\s+(?P<enable>\w+)')

        # BUM Label:       1002
        p28 = re.compile(r'^BUM Label:\s+((?P<label>\d+)|none)$')

        # Per-BD Label:    1003
        p29 = re.compile(r'^Per-BD Label:\s+((?P<label>\d+)|none)$')

        # BDI Label:       none
        p30 = re.compile(r'^BDI Label:\s+((?P<label>\d+)|none)$')

        # Pseudoports:
        p31 = re.compile(r'^Pseudoports( \(Labels\))?:$')

        # Ethernet0/1 service instance 1
        # Ethernet0/3 service instance 1 (DF state: PE-to-CE BUM blocked)
        p32 = re.compile(r'^(?P<pp_name>[\w\/\.\-]+ service instance \d+)'
                         r'( \(((?P<label>\d+)|none)\))?'
                         r'( \(DF state: (?P<state>[\w\- ]+)\))?$')

        # pseudowire100002 (Access VFI VFI10: Peer 5.5.5.5, VC 10)
        # pseudowire100003 (Access PW: Peer 5.5.5.5, VC 10) (DF state: blocked)
        p33 = re.compile(
            r'^(?P<pp_name>pseudowire\d+)'
            r' \((((Access )?VFI (?P<access_vfi>\w+))|(Access PW)):'
            r' ((Peer (?P<addr>[A-Fa-f0-9:\.]+), VC (?P<vc>\d+))'
            r'|(no peer info))\)'
            r'( \(((?P<label>\d+)|none)\))?'
            r'( \(DF state: (?P<state>[\w\-\s]+)\))?$')

        # Routes: 1 MAC, 1 MAC/IP
        p34 = re.compile(r'^Routes:\s+(?P<mac>\d+) MAC,'
                         r'\s+(?P<mac_ip>\d+) MAC\/IP$')

        # Peers:
        p35 = re.compile(r'^Peers:$')

        # 15.15.15.15
        p36 = re.compile(r'^(?P<addr>[A-Fa-f0-9:\.]+)$')

        # Routes: 0 MAC, 0 MAC/IP, 1 IMET, 1 EAD
        p37 = re.compile(r'^Routes:\s+(?P<mac>\d+) MAC,'
                         r'\s+(?P<mac_ip>\d+) MAC\/IP,'
                         r'\s+(?P<imet>\d+) IMET,'
                         r'\s+(?P<ead>\d+) EAD$')

        # Sec. VTEP IP:    1.1.1.2
        p38 = re.compile(r'^Sec\. VTEP IP:\s+(?P<addr>UNKNOWN|[A-Fa-f\d:.]+)$')

        # ESI: 0000.0000.0000.0000.0001
        p39 = re.compile(r'^ESI:\s+(?P<esi>[0-9a-fA-F\.]+)$')

        for line in output.splitlines():
            line = line.strip()

            # EVPN instance:       1 (VLAN Based)
            m = p1.match(line)
            if m:
                bd_id = None
                pseudoport = None
                peer = None
                pp_section = False
                peer_section = False
                evi = m.groupdict()['evi']
                evi_dict = parsed_dict.setdefault(evi, {})
                evi_dict['evi_type'] = str(m.groupdict()['type'])
                continue

            # RD:                20.20.20.20:1 (auto)
            m = p2.match(line)
            if m:
                evi_dict['rd'] = str(m.groupdict()['rd'])
                evi_dict['rd_type'] = str(m.groupdict()['type'])
                continue

            # Import-RTs:        1:1
            m = p3.match(line)
            if m:
                evi_dict['import_rt'] = str(m.groupdict()['rt'])
                continue

            # Export-RTs:        1:1
            m = p4.match(line)
            if m:
                evi_dict['export_rt'] = str(m.groupdict()['rt'])
                continue

            # Per-EVI Label:     none
            m = p5.match(line)
            if m:
                evi_dict['per_evi_label'] = str(m.groupdict()['label'])
                continue

            # State:             Established
            m = p6.match(line)
            if m:
                state = str(m.groupdict()['state'])
                if bd_id is None:
                    evi_dict['state'] = state
                else:
                    parsed_dict[evi]['bridge_domain'][bd_id]['state'] = state
                continue

            # Replication Type:  Static (global)
            m = p7.match(line)
            if m:
                rep_type = m.groupdict()['type'].rstrip()
                evi_dict['replication_type'] = str(rep_type)
                continue

            # Encapsulation:     vxlan
            m = p8.match(line)
            if m:
                evi_dict['encap_type'] = str(m.groupdict()['enctype'])
                continue

            # IP Local Learn:    Enabled (global)
            m = p9.match(line)
            if m:
                ip_local = m.groupdict()['enable'].rstrip().lower()
                if ip_local == 'enabled' or ip_local == 'enable':
                    evi_dict['ip_local_learn'] = True
                else:
                    evi_dict['ip_local_learn'] = False
                continue

            # Adv. Def. Gateway: Disabled (global)
            m = p10.match(line)
            if m:
                if m.groupdict()['enable'].lower() == 'enabled':
                    evi_dict['adv_def_gateway'] = True
                else:
                    evi_dict['adv_def_gateway'] = False
                continue

            # Re-originate RT5:  Disabled
            m = p11.match(line)
            if m:
                if m.groupdict()['enable'].lower() == 'enabled':
                    evi_dict['re_orig_rt5'] = True
                else:
                    evi_dict['re_orig_rt5'] = False
                continue

            # Adv. Multicast:    Enabled (global)
            m = p12.match(line)
            if m:
                if m.groupdict()['enable'].lower() == 'enabled':
                    evi_dict['adv_mcast'] = True
                else:
                    evi_dict['adv_mcast'] = False
                continue

            # Vlan:              100
            # Bridge Domain:     1
            m = p13.match(line)
            if m:
                pseudoport = None
                peer = None
                pp_section = False
                peer_section = False
                bd_id = m.groupdict()['bd_id']
                bd_dict = evi_dict.setdefault(
                    'bridge_domain', {}).setdefault(bd_id, {})
                continue

            # Ethernet-Tag:    0
            m = p14.match(line)
            if m:
                bd_dict['etag'] = int(m.groupdict()['etag'])
                continue

            # Flood Suppress:  Attached
            m = p15.match(line)
            if m:
                if m.groupdict()['attach'].lower() == 'attached':
                    bd_dict['flood_suppress'] = True
                else:
                    bd_dict['flood_suppress'] = False
                continue

            # Core If:         Vlan500
            m = p16.match(line)
            if m:
                bd_dict['core_if'] = str(m.groupdict()['name'])
                continue

            # Access If:       Vlan100
            m = p17.match(line)
            if m:
                bd_dict['access_if'] = str(m.groupdict()['name'])
                continue

            # NVE If:          nve1
            m = p18.match(line)
            if m:
                bd_dict['nve_if'] = str(m.groupdict()['name'])
                continue

            # RMAC:            0000.0000.0000
            m = p19.match(line)
            if m:
                bd_dict['rmac'] = str(m.groupdict()['mac'])
                continue

            # Core Vlan:       0
            m = p20.match(line)
            if m:
                bd_dict['core_vlan'] = int(m.groupdict()['vlan'])
                continue

            # L2 VNI:          10000
            m = p21.match(line)
            if m:
                bd_dict['l2vni'] = int(m.groupdict()['vni'])
                continue

            # L3 VNI:          0
            m = p22.match(line)
            if m:
                bd_dict['l3vni'] = int(m.groupdict()['vni'])
                continue

            # VTEP IP:         1.20.20.20
            m = p23.match(line)
            if m:
                bd_dict['vtep_ip'] = str(m.groupdict()['addr'])
                continue

            # Sec. VTEP IP:    1.1.1.2
            m = p38.match(line)
            if m:
                bd_dict['vtep_ip_sec'] = str(m.groupdict()['addr'])
                continue

            # MCAST IP:        227.0.0.1
            m = p24.match(line)
            if m:
                bd_dict['mcast_ip'] = str(m.groupdict()['addr'])
                continue

            # VRF:             Red
            m = p25.match(line)
            if m:
                bd_dict['vrf'] = str(m.groupdict()['vrf'])
                continue

            # IPv4 IRB:        Enabled (Asymmetric)
            m = p26.match(line)
            if m:
                if m.groupdict()['enable'].lower() == 'enabled':
                    bd_dict['ipv4_irb'] = True
                else:
                    bd_dict['ipv4_irb'] = False
                continue

            # IPv6 IRB:        Disabled
            m = p27.match(line)
            if m:
                if m.groupdict()['enable'].lower() == 'enabled':
                    bd_dict['ipv6_irb'] = True
                else:
                    bd_dict['ipv6_irb'] = False
                continue

            # BUM Label:       1002
            m = p28.match(line)
            if m:
                if m.groupdict()['label']:
                    bd_dict['bum_label'] = int(m.groupdict()['label'])
                continue

            # Per-BD Label:    1003
            m = p29.match(line)
            if m:
                if m.groupdict()['label']:
                    bd_dict['per_bd_label'] = int(m.groupdict()['label'])
                continue

            # BDI Label:       none
            m = p30.match(line)
            if m:
                if m.groupdict()['label']:
                    bd_dict['bdi_label'] = int(m.groupdict()['label'])
                continue

            # Pseudoports:
            m = p31.match(line)
            if m:
                peer = None
                pp_section = True
                pp_dict = bd_dict.setdefault('pseudo_port', {})
                continue

            # Ethernet0/1 service instance 1
            # Ethernet0/3 service instance 1 (DF state: PE-to-CE BUM blocked)
            m = p32.match(line)
            if m and pp_section:
                pseudoport = str(m.groupdict()['pp_name'])
                if pseudoport not in pp_dict:
                    pp_dict[pseudoport] = {}
                if m.groupdict()['label']:
                    pp_dict[pseudoport]['per_ce_label'] = int(
                        m.groupdict()['label'])
                if m.groupdict()['state']:
                    pp_dict[pseudoport]['df_state'] = str(
                        m.groupdict()['state'])
                continue

            # pseudowire100002 (Access VFI VFI10: Peer 5.5.5.5, VC 10)
            # pseudowire100003 (Access PW: Peer 5.5.5.5, VC 10) (DF state: blocked)
            m = p33.match(line)
            if m and pp_section:
                pseudoport = str(m.groupdict()['pp_name'])
                if pseudoport not in pp_dict:
                    pp_dict[pseudoport] = {}
                if m.groupdict()['access_vfi']:
                    pp_dict[pseudoport]['access_vfi'] = str(
                        m.groupdict()['access_vfi'])
                if m.groupdict()['addr']:
                    pp_dict[pseudoport]['peer'] = str(m.groupdict()['addr'])
                if m.groupdict()['vc']:
                    pp_dict[pseudoport]['vc'] = int(m.groupdict()['vc'])
                if m.groupdict()['label']:
                    pp_dict[pseudoport]['per_ce_label'] = int(
                        m.groupdict()['label'])
                if m.groupdict()['state']:
                    pp_dict[pseudoport]['df_state'] = str(
                        m.groupdict()['state'])
                continue

            # Routes: 1 MAC, 1 MAC/IP
            m = p34.match(line)
            if m and pseudoport is not None:
                macs = m.groupdict()['mac']
                macips = m.groupdict()['mac_ip']
                pp_dict[pseudoport]['mac_routes'] = int(macs)
                pp_dict[pseudoport]['mac_ip_routes'] = int(macips)
                continue

            # ESI: 0000.0000.0000.0000.0001
            m = p39.match(line)
            if m and pseudoport is not None:
                esi = m.groupdict()['esi']
                pp_dict[pseudoport]['esi'] = str(esi)
                continue

            # Peers:
            m = p35.match(line)
            if m:
                pseudoport = None
                peer_section = True
                pp_section = False
                peer_dict = bd_dict.setdefault('peer', {})
                continue

            # 15.15.15.15
            m = p36.match(line)
            if m and peer_section and peer is None:
                peer = str(m.groupdict()['addr'])
                if peer not in peer_dict:
                    peer_dict[peer] = {}
                continue

            # Routes: 0 MAC, 0 MAC/IP, 1 IMET, 1 EAD
            m = p37.match(line)
            if m and peer is not None:
                peer_dict[peer]['mac_routes'] = int(m.groupdict()['mac'])
                peer_dict[peer]['mac_ip_routes'] = int(m.groupdict()['mac_ip'])
                peer_dict[peer]['imet_routes'] = int(m.groupdict()['imet'])
                peer_dict[peer]['ead_routes'] = int(m.groupdict()['ead'])
                peer = None
                continue

        return parsed_dict

# ============================================
# Schema for 'show l2vpn evpn multicast local'
# ============================================
class ShowL2vpnEvpnMcastLocalSchema(MetaParser):
    """ Schema for show l2vpn evpn multicast local """
    schema = {
        Any(): {
            Any(): {
                Any(): {
                    Any(): {
                        'evi': str,
                        'vlan': str,
                        'interface': str,
                        'src_grp': str,
                        'version': str,
                        'filter_mode': str,
                    },
                },
            },
        },
    }


# ==================================================
# Parser for 'show l2vpn evpn multicast local'
# ==================================================
class ShowL2vpnEvpnMcastLocal(ShowL2vpnEvpnMcastLocalSchema):
    """ Parser for show l2vpn evpn multicast local """

    cli_command = 'show l2vpn evpn multicast local'

    def cli(self, output=None):

        # Init vars
        parsed_dict = {}

        if output is None:
            # Execute command
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output

        parsed_dict = oper_fill_tabular(
            header_fields=["EVI", "VLAN", "Interface",
                           "Version", "Filter", "\(Source, Group\)"],
            label_fields=['evi', 'vlan', 'interface', 'version',
                          'filter_mode', 'src_grp'],
            index=[0, 1, 2, 5],
            device_output=show_output,
            device_os='iosxe'
        ).entries

        return parsed_dict

# ============================================
# Schema for 'show l2vpn evpn multicast remote'
# ============================================
class ShowL2vpnEvpnMcastRemoteSchema(MetaParser):
    """ Schema for show l2vpn evpn multicast remote """
    schema = {
        Any(): {
            Any(): {
                Any(): {
                    Any(): {
                        'evi': str,
                        'vlan': str,
                        'originator': str,
                        'src_grp': str,
                        'version': str,
                        'filter_mode': str,
                    },
                },
            },
        },
    }


# ==================================================
# Parser for 'show l2vpn evpn multicast remote'
# ==================================================
class ShowL2vpnEvpnMcastRemote(ShowL2vpnEvpnMcastRemoteSchema):
    """ Parser for: show l2vpn evpn multicast remote """

    cli_command = 'show l2vpn evpn multicast remote'

    def cli(self, output=None):

        # Init vars
        parsed_dict = {}

        if output is None:
            # Execute command
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output

        parsed_dict = oper_fill_tabular(
            header_fields=["EVI", "VLAN", "Originator",
                           "Version", "Filter", "\(Source, Group\)"],
            label_fields=['evi', 'vlan', 'originator', 'version',
                          'filter_mode', 'src_grp'],
            index=[0, 1, 2, 5],
            device_output=show_output,
            device_os='iosxe'
        ).entries

        return parsed_dict

# =====================================================
# Schema for 'show l2vpn evpn capabilities'
# =====================================================
class ShowL2vpnEvpnCapSchema(MetaParser):
    """Schema for show l2vpn evpn capabilities"""

    schema = {
        'vlanbased_evi': bool,
        'vlanbundle_evi': bool,
        'vlanaware_evi': bool,
        'ingress_rep': bool,
        'p2mp_rep': bool,
        'mp2mp_rep': bool,
        'static_rep': bool,
        'perbd_label': bool,
        'perce_label': bool,
        'perevi_label': bool,
        'floodsp_ar': bool,
        'floodsp_dhcprelay': bool,
        'vlan_config_mode': bool,
        'mpls_encap': bool,
        'vxlan_encap': bool,
        'mh_aliasing': bool,
        'vpls_stitching': bool,
        'vpls_seamless': bool,
        'mh_red_aa': bool,
        'mn_red_sa': bool,
        'es_old_config': bool,
        'ip_local_learn': bool,
        'vpls_stitch_dh_sa': bool,
        'l2trm_ipv4': bool,
        'l2trm_ipv6': bool,
        'l2trm_srcg_fwd': bool,
        'vpws_prefered_path_srte': bool,
    }


# =====================================================
# Parser for 'show l2vpn evpn capabilities'
# =====================================================
class ShowL2vpnEvpnCap(ShowL2vpnEvpnCapSchema):
    """Parser for show l2vpn evpn capabilities"""

    cli_command = 'show l2vpn evpn capabilities'

    def cli(self, output=None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output

        # initial return dictionary
        parsed_dict = {}

        # EVPN Platform Capabilities
        p0 = re.compile(r'^EVPN Platform Capabilities$')
        # VLAN-based EVPN Instance: supported
        p1 = re.compile(r'^VLAN-based EVPN Instance: supported$')
        # VLAN-bundle EVPN Instance: supported
        p2 = re.compile(r'^VLAN-bundle EVPN Instance: supported$')
        # VLAN-aware EVPN Instance: supported
        p3 = re.compile(r'^VLAN-aware EVPN Instance: supported$')
        # Ingress replication type: supported
        p4 = re.compile(r'^Ingress replication type: supported$')
        # Point-to-multipoint replication type: supported
        p5 = re.compile(r'^Point-to-multipoint replication type: supported$')
        # Multipoint-to-multipoint replication type: supported
        p6 = re.compile(r'^Multipoint-to-multipoint '
                        r'replication type: supported$')
        # Static replication type: supported
        p7 = re.compile(r'^Static replication type: supported$')
        # Per-BD MPLS label allocation mode: supported
        p8 = re.compile(r'^Per-BD MPLS label allocation mode: supported$')
        # Per-CE MPLS label allocation mode: supported
        p9 = re.compile(r'^Per-CE MPLS label allocation mode: supported$')
        # Per-EVI MPLS label allocation mode: supported
        p10 = re.compile(r'^Per-EVI MPLS label allocation mode: supported$')
        # Address resolution flooding suppression: supported
        p11 = re.compile(r'^Address resolution flooding '
                         r'suppression: supported$')
        # DHCP Relay flooding suppression: supported
        p12 = re.compile(r'^DHCP Relay flooding suppression: supported$')
        # VLAN configuration mode: supported
        p13 = re.compile(r'^VLAN configuration mode: supported$')
        # MPLS encapsulation: supported
        p14 = re.compile(r'^MPLS encapsulation: supported$')
        # VxLAN encapsulation: supported
        p15 = re.compile(r'^VxLAN encapsulation: supported$')
        # Multi-homing aliasing: supported
        p16 = re.compile(r'^Multi-homing aliasing: supported$')
        # VPLS stitching: supported
        p17 = re.compile(r'^VPLS stitching: supported$')
        # VPLS seamless integration: supported
        p18 = re.compile(r'^VPLS seamless integration: supported$')
        # Multi-homing all active redundancy mode: supported
        p19 = re.compile(r'^Multi-homing all active '
                         r'redundancy mode: supported$')
        # Multi-homing single active redundancy mode: supported
        p20 = re.compile(r'^Multi-homing single active '
                         r'redundancy mode: supported$')
        # Ethernet Segment old config model: supported
        p21 = re.compile(r'^Ethernet Segment old config model: supported$')
        # IP local learning: supported
        p22 = re.compile(r'^IP local learning: supported$')
        # VPLS stitching single-active dual-homing: supported
        p23 = re.compile(r'^VPLS stitching single-active '
                         r'dual-homing: supported$')
        # Layer 2 Tenant Routed Multicast IPv4: supported
        p24 = re.compile(r'^Layer 2 Tenant Routed Multicast IPv4: supported$')
        # Layer 2 Tenant Routed Multicast IPv6: supported
        p25 = re.compile(r'^Layer 2 Tenant Routed Multicast IPv6: supported$')
        # Layer 2 multicast source specific forwarding: supported
        p26 = re.compile(r'^Layer 2 multicast source specific '
                         r'forwarding: supported$')
        # VPWS Preferred Path SRTE Policy: supported
        p27 = re.compile(r'^VPWS Preferred Path SRTE Policy: supported$')

        for line in show_output.splitlines():
            line = line.strip()

            # EVPN Platform Capabilities
            m = p0.match(line)
            if m:
                parsed_dict['vlanbased_evi'] = False
                parsed_dict['vlanbundle_evi'] = False
                parsed_dict['vlanaware_evi'] = False
                parsed_dict['ingress_rep'] = False
                parsed_dict['p2mp_rep'] = False
                parsed_dict['mp2mp_rep'] = False
                parsed_dict['static_rep'] = False
                parsed_dict['perbd_label'] = False
                parsed_dict['perce_label'] = False
                parsed_dict['perevi_label'] = False
                parsed_dict['floodsp_ar'] = False
                parsed_dict['floodsp_dhcprelay'] = False
                parsed_dict['vlan_config_mode'] = False
                parsed_dict['mpls_encap'] = False
                parsed_dict['vxlan_encap'] = False
                parsed_dict['mh_aliasing'] = False
                parsed_dict['vpls_stitching'] = False
                parsed_dict['vpls_seamless'] = False
                parsed_dict['mh_red_aa'] = False
                parsed_dict['mn_red_sa'] = False
                parsed_dict['es_old_config'] = False
                parsed_dict['ip_local_learn'] = False
                parsed_dict['vpls_stitch_dh_sa'] = False
                parsed_dict['l2trm_ipv4'] = False
                parsed_dict['l2trm_ipv6'] = False
                parsed_dict['l2trm_srcg_fwd'] = False
                parsed_dict['vpws_prefered_path_srte'] = False
                continue

            # VLAN-based EVPN Instance: supported
            m = p1.match(line)
            if m:
                parsed_dict['vlanbased_evi'] = True
                continue

            # VLAN-bundle EVPN Instance: supported
            m = p2.match(line)
            if m:
                parsed_dict['vlanbundle_evi'] = True
                continue

            # VLAN-aware EVPN Instance: supported
            m = p3.match(line)
            if m:
                parsed_dict['vlanaware_evi'] = True
                continue

            # Ingress replication type: supported
            m = p4.match(line)
            if m:
                parsed_dict['ingress_rep'] = True
                continue

            # Point-to-multipoint replication type: supported
            m = p5.match(line)
            if m:
                parsed_dict['p2mp_rep'] = True
                continue

            # Multipoint-to-multipoint replication type: supported
            m = p6.match(line)
            if m:
                parsed_dict['mp2mp_rep'] = True
                continue

            # Static replication type: supported
            m = p7.match(line)
            if m:
                parsed_dict['static_rep'] = True
                continue

            # Per-BD MPLS label allocation mode: supported
            m = p8.match(line)
            if m:
                parsed_dict['perbd_label'] = True
                continue

            # Per-CE MPLS label allocation mode: supported
            m = p9.match(line)
            if m:
                parsed_dict['perce_label'] = True
                continue

            # Per-EVI MPLS label allocation mode: supported
            m = p10.match(line)
            if m:
                parsed_dict['perevi_label'] = True
                continue

            # Address resolution flooding suppression: supported
            m = p11.match(line)
            if m:
                parsed_dict['floodsp_ar'] = True
                continue

            # DHCP Relay flooding suppression: supported
            m = p12.match(line)
            if m:
                parsed_dict['floodsp_dhcprelay'] = True
                continue

            # VLAN configuration mode: supported
            m = p13.match(line)
            if m:
                parsed_dict['vlan_config_mode'] = True
                continue

            # MPLS encapsulation: supported
            m = p14.match(line)
            if m:
                parsed_dict['mpls_encap'] = True
                continue

            # VxLAN encapsulation: supported
            m = p15.match(line)
            if m:
                parsed_dict['vxlan_encap'] = True
                continue

            # Multi-homing aliasing: supported
            m = p16.match(line)
            if m:
                parsed_dict['mh_aliasing'] = True
                continue

            # VPLS stitching: supported
            m = p17.match(line)
            if m:
                parsed_dict['vpls_stitching'] = True
                continue

            # VPLS seamless integration: supported
            m = p18.match(line)
            if m:
                parsed_dict['vpls_seamless'] = True
                continue

            # Multi-homing all active redundancy mode: supported
            m = p19.match(line)
            if m:
                parsed_dict['mh_red_aa'] = True
                continue

            # Multi-homing single active redundancy mode: supported
            m = p20.match(line)
            if m:
                parsed_dict['mn_red_sa'] = True
                continue

            # Ethernet Segment old config model: supported
            m = p21.match(line)
            if m:
                parsed_dict['es_old_config'] = True
                continue

            # IP local learning: supported
            m = p22.match(line)
            if m:
                parsed_dict['ip_local_learn'] = True
                continue

            # VPLS stitching single-active dual-homing: supported
            m = p23.match(line)
            if m:
                parsed_dict['vpls_stitch_dh_sa'] = True
                continue

            # Layer 2 Tenant Routed Multicast IPv4: supported
            m = p24.match(line)
            if m:
                parsed_dict['l2trm_ipv4'] = True
                continue

            # Layer 2 Tenant Routed Multicast IPv6: supported
            m = p25.match(line)
            if m:
                parsed_dict['l2trm_ipv6'] = True
                continue

            # Layer 2 multicast source specific forwarding: supported
            m = p26.match(line)
            if m:
                parsed_dict['l2trm_srcg_fwd'] = True
                continue

            # VPWS Preferred Path SRTE Policy: supported
            m = p27.match(line)
            if m:
                parsed_dict['vpws_prefered_path_srte'] = True
                continue

        return parsed_dict

# =====================================================
# Schema for 'show running-config | section l2vpn evpn'
# =====================================================
class ShowRunSectionL2vpnEvpnSchema(MetaParser):
    """Schema for show running-config | section l2vpn evpn"""

    schema = {
        'floodsup_ar_disable': bool,
        'floodsup_dhcprelay_disable': bool,
        'mh_alias_disable': bool,
        'dgw_advertise': bool,
        'mcast_advertise': bool,
        Optional('reptype'): str,
        Optional('evis'): {
            Any(): {
                'srvinst': str,
                'dgw_advertise': bool,
                'mcast_advertise': bool,
                Optional('encaptype'): str,
                Optional('reptype'): str,
            },
        },
    }


# =====================================================
# Parser for 'show running-config | section l2vpn evpn'
# =====================================================
class ShowRunSectionL2vpnEvpn(ShowRunSectionL2vpnEvpnSchema):
    """Parser for show running-config | section l2vpn evpn """

    cli_command = 'show running-config | section l2vpn evpn'

    def cli(self, output=None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output

        # initial return dictionary
        parsed_dict = {}

        # l2vpn evpn
        p1 = re.compile(r'^l2vpn evpn$')

        # l2vpn evpn instance 2 vlan-based
        p2 = re.compile(r'^l2vpn evpn instance '
                        r'(?P<evi>\d+) (?P<srvinst>[\w-]+)$')

        # replication-type ingress
        p3 = re.compile(r'^replication-type (?P<reptype>\w+)$')

        # flooding-suppression address-resolution disable
        p4 = re.compile(r'^flooding-suppression address-resolution disable$')

        # multihoming aliasing disable
        p5 = re.compile(r'^multihoming aliasing disable$')

        # default-gateway advertise
        p6 = re.compile(r'^default-gateway advertise$')

        # multicast advertise
        p7 = re.compile(r'^multicast advertise$')

        # encapsulation vxlan
        p8 = re.compile(r'^encapsulation (?P<encaptype>\w+)$')

        # default-gateway advertise enable/disable
        p9 = re.compile(r'^default-gateway advertise (?P<dgadv>\w+)$')

        # multicast advertise enable/disable
        p10 = re.compile(r'^multicast advertise (?P<mcadv>\w+)$')

        # flooding-suppression dhcp-relay disable
        p11 = re.compile(r'^flooding-suppression dhcp-relay disable$')

        floodsup_ar_disable = False
        floodsup_dhcprelay_disable = False
        mh_alias_disable = False
        dgw_adver = False
        mcast_adver = False

        set_evi = False
        for line in show_output.splitlines():
            line = line.strip()

            # l2vpn evpn
            m = p1.match(line)
            if m:
                parsed_dict['floodsup_ar_disable'] = floodsup_ar_disable
                parsed_dict['floodsup_dhcprelay_disable'] = floodsup_dhcprelay_disable
                parsed_dict['mh_alias_disable'] = mh_alias_disable
                parsed_dict['dgw_advertise'] = dgw_adver
                parsed_dict['mcast_advertise'] = mcast_adver
                continue

            # l2vpn evpn instance 2 vlan-based
            m = p2.match(line)
            if m:
                evis_dict = parsed_dict.setdefault('evis', {})
                evi = m.groupdict()['evi']
                evi_dict = evis_dict.setdefault(evi, {})
                evi_dict['srvinst'] = str(m.groupdict()['srvinst'])
                evi_dict['dgw_advertise'] = dgw_adver
                evi_dict['mcast_advertise'] = mcast_adver
                if 'reptype' in parsed_dict:
                    evi_dict['reptype'] = parsed_dict['reptype']
                set_evi = True
                continue

            # replication-type ingress
            m = p3.match(line)
            if m:
                if set_evi:
                    evi_dict['reptype'] = str(m.groupdict()['reptype'])
                else:
                    parsed_dict['reptype'] = str(m.groupdict()['reptype'])
                continue

            # flooding-suppression address-resolution disable
            m = p4.match(line)
            if m:
                parsed_dict['floodsup_ar_disable'] = True
                continue

            # flooding-suppression dhcp-relay disable
            m = p11.match(line)
            if m:
                parsed_dict['floodsup_dhcprelay_disable'] = True
                continue

            # multihoming aliasing disable
            m = p5.match(line)
            if m:
                parsed_dict['mh_alias_disable'] = True
                continue

            # default-gateway advertise
            m = p6.match(line)
            if m:
                parsed_dict['dgw_advertise'] = True
                dgw_adver = True
                continue

            # multicast advertise
            m = p7.match(line)
            if m:
                parsed_dict['mcast_advertise'] = True
                mcast_adver = True
                continue

            # encapsulation vxlan
            m = p8.match(line)
            if m:
                if set_evi:
                    evi_dict['encaptype'] = str(m.groupdict()['encaptype'])
                continue

            # default-gateway advertise enable/disable
            m = p9.match(line)
            if m:
                if set_evi:
                    if 'enable' == str(m.groupdict()['dgadv']):
                        evi_dict['dgw_advertise'] = True
                    elif 'disable' == str(m.groupdict()['dgadv']):
                        evi_dict['dgw_advertise'] = False
                continue

            # multicast advertise enable/disable
            m = p10.match(line)
            if m:
                if set_evi:
                    if 'enable' == str(m.groupdict()['mcadv']):
                        evi_dict['mcast_advertise'] = True
                    elif 'disable' == str(m.groupdict()['mcadv']):
                        evi_dict['mcast_advertise'] = False
                continue

        return parsed_dict

# ============================================
# Schema for 'show l2vpn evpn vpws vc id detail'
# ============================================
class ShowL2vpnEvpnVpwsVcSchema(MetaParser):
    """ Schema for show l2vpn evpn vpws vc id detail """

    schema = {
            'vc_name': str,
            'vc_state': str,
            'evi': int,
            Optional('source'): int,
            Optional('target'): int,
            Optional('local_label'): int,
            Optional('remote_label'): int,
            Optional('next_hop'): str,
            Optional('access_if'): str,
            Optional('access_if_state'): str,
            Optional('access_member_state'): str,
            Optional('output_if'): str,
            Optional('output_label_stack'): str,
            Optional('preferred_path'): str,
            Optional('default_path'): str,
            Optional('rx_pak'): int,
            Optional('tx_pak'): int,
    }


# ==================================================
# Parser for 'show l2vpn evpn vpws vc id detail'
# ==================================================
class ShowL2vpnEvpnVpwsVc(ShowL2vpnEvpnVpwsVcSchema):
    """ Parser for: show l2vpn evpn vpws vc id {vc_id} detail """

    cli_command = 'show l2vpn evpn vpws vc id {vc_id} detail'

    def cli(self, vc_id=None, output=None):

        # Init vars
        parsed_dict = {}

        if output is None:
            # Execute command
            if vc_id:
                show_output = self.device.execute(self.cli_command.format(vc_id=vc_id))
            else:
                show_output = None
        else:
            show_output = output


        # EVPN name: vc100, state: up, type: point-to-point
        p1 = re.compile(r'^EVPN name:\s+(?P<vc_name>[^,]+), state:\s+(?P<vc_state>[^,]+), type:\s+point-to-point$')

        # EVPN ID: 100
        p2 = re.compile(r'^EVPN ID:\s+(?P<evi>\d+)$')

        # VPWS Service Instance ID: Source 1, Target 2
        p3 = re.compile(r'^\s*VPWS Service Instance ID:\s+Source\s+(?P<source>\d+), Target\s+(?P<target>\d+)$')

        # Labels: Local 18, Remote 16
        p4 = re.compile(r'^\s*Labels:\s+Local\s+(?P<local_label>\d+), Remote\s+(?P<remote_label>\d+)$')

        # Next Hop Address: 20.20.20.20
        p5 = re.compile(r'^\s*Next Hop Address:\s+(?P<next_hop>[A-Fa-f0-9:\.]+)$')

        # Associated member interface Et1/2 up, Et1/2 status is up
        p6 = re.compile(r'^\s*Associated member interface\s+(?P<access_if>\S+)\s+(?P<access_member_state>[^,]+)(\S+\s+){4}(?P<access_if_state>.*)$')

        # Output interface: Tu65536, imposed label stack {24321 16}
        p7 = re.compile(r'^\s*Output interface:\s+(?P<output_if>.*), imposed label stack {(?P<output_label_stack>[^}]+)')

        # Preferred path:   active
        p8 = re.compile(r'^\s*Preferred path:\s+(?P<preferred_path>.*)$')

        # Default path: ready
        p9 = re.compile(r'^\s*Default path:\s+(?P<default_path>.*)$')

        # Rx Counters
        # 0 input transit packets, 0 bytes
        p10 = re.compile(r'^\s*(?P<rx_pak>\S+)\s+input transit packets')
        # 0 drops

        # Tx Counters
        # 0 output transit packets, 0 bytes
        p11 = re.compile(r'^\s*(?P<tx_pak>\S+)\s+output transit packets')
        # 0 drops

        for line in show_output.splitlines():
            line = line.strip()

            # EVPN name: vc100, state: up, type: point-to-point
            m = p1.match(line)
            if m:
                parsed_dict['vc_name'] = str(m.groupdict()['vc_name'])
                parsed_dict['vc_state'] = str(m.groupdict()['vc_state'])
                continue

            # EVPN ID: 100
            m = p2.match(line)
            if m:
                parsed_dict['evi'] = int(m.groupdict()['evi'])
                continue

            # VPWS Service Instance ID: Source 1, Target 2
            m = p3.match(line)
            if m:
                parsed_dict['source'] = int(m.groupdict()['source'])
                parsed_dict['target'] = int(m.groupdict()['target'])
                continue

            # Labels: Local 18, Remote 16
            m = p4.match(line)
            if m:
                parsed_dict['local_label'] = int(m.groupdict()['local_label'])
                parsed_dict['remote_label'] = int(m.groupdict()['remote_label'])
                continue

            # Next Hop Address: 20.20.20.20
            m = p5.match(line)
            if m:
                parsed_dict['next_hop'] = str(m.groupdict()['next_hop'])
                continue

            # Associated member interface Et1/2 up, Et1/2 status is up
            m = p6.match(line)
            if m:
                parsed_dict['access_if'] = str(m.groupdict()['access_if'])
                parsed_dict['access_if_state'] = str(m.groupdict()['access_if_state'])
                parsed_dict['access_member_state'] = str(m.groupdict()['access_member_state'])
                continue

            # Output interface: Tu65536, imposed label stack {24321 16}
            m = p7.match(line)
            if m:
                parsed_dict['output_if'] = str(m.groupdict()['output_if'])
                parsed_dict['output_label_stack'] = str(m.groupdict()['output_label_stack'])
                continue

            # Preferred path:   active
            m = p8.match(line)
            if m:
                parsed_dict['preferred_path'] = str(m.groupdict()['preferred_path'])
                continue

            # Default path: ready
            m = p9.match(line)
            if m:
                parsed_dict['default_path'] = str(m.groupdict()['default_path'])
                continue

            # Rx Counters
            # 0 input transit packets, 0 bytes
            m = p10.match(line)
            if m:
                parsed_dict['rx_pak'] = int(m.groupdict()['rx_pak'])
                continue

            # Tx Counters
            # 0 output transit packets, 0 bytes
            m = p11.match(line)
            if m:
                parsed_dict['tx_pak'] = int(m.groupdict()['tx_pak'])
                continue

        return parsed_dict

# ============================================
# Schema for 'show l2vpn evpn vpws vc preferred-path'
# ============================================
class ShowL2vpnEvpnVpwsVcPreferredPathSchema(MetaParser):
    """ Schema for show l2vpn evpn vpws vc preferred-path """
    schema = {
        Any(): {
                    'Tunnel': str,
                    'EVPN ID': str,
                    'Source': str,
                    'Target': str,
                    'Name': str,
                    'Status': str,
                },
    }


# ==================================================
# Parser for 'show l2vpn evpn vpws vc preferred-path'
# ==================================================
class ShowL2vpnEvpnVpwsVcPreferredPath(ShowL2vpnEvpnVpwsVcPreferredPathSchema):
    """ Parser for: show l2vpn evpn vpws vc preferred-path """

    cli_command = 'show l2vpn evpn vpws vc preferred-path'

    def cli(self, output=None):

        # Init vars
        parsed_dict = {}

        if output is None:
            # Execute command
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output

        if show_output:
            parsed_dict = oper_fill_tabular(header_fields=["Tunnel", "EVPN ID", "Source", "Target", "Name", "Status"],
                                            device_output=show_output,
                                            device_os='iosxe', index=[1]).entries
        return parsed_dict


# ============================================
# Schema for 'show l2vpn atom vc'
# ============================================
class ShowL2vpnAtomVcSchema(MetaParser):
    """Schema for show l2vpn atom vc"""

    schema = {
        'name': {
            Any(): {
                'interface': {
                    Any(): {
                        'peer_id': str,
                        'vc_id': int,
                        'type': str,
                        'status': str                        
                    }
                }
            }
        }
    }

# ======================================================
# Parser for 'show l2vpn atom vc '
# ======================================================
class ShowL2vpnAtomVc(ShowL2vpnAtomVcSchema):
    """Parser for show l2vpn atom vc"""
    
    cli_command = 'show l2vpn atom vc'
    
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Interface Peer ID        VC ID      Type   Name                     Status
        p1 = re.compile(r"^(?P<interface>[\w\d]+)\s+(?P<peer_id>[\d\:\.]+)\s+(?P<vc_id>\d+)\s+(?P<type>\w+)\s+(?P<name>[\w\d]+)\s+(?P<status>\w+)$")

        for line in output.splitlines():
            line = line.rstrip()

            # Interface Peer ID        VC ID      Type   Name                     Status
            m = p1.match(line)
            if m:
                name = m.groupdict()['name']
                key_chain_dict = ret_dict.setdefault('name', {}).setdefault(name, {})
                key_name = Common.convert_intf_name(m.groupdict()['interface'])
                process_dict = key_chain_dict.setdefault('interface', {}).setdefault(key_name, {})
                process_dict['peer_id']=m.groupdict()['peer_id']
                process_dict['status']=m.groupdict()['status']
                process_dict['vc_id']=int(m.groupdict()['vc_id'])
                process_dict['type']=m.groupdict()['type']
                continue

        return ret_dict
