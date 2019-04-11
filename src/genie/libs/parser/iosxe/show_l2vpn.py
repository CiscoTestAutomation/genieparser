''' show_l2vpn.py

IOSXE parsers for the following show commands:

    * show bridge-domain
    * show bridge-domain <BD_ID>
    * show bridge-domain | count <WORD>
    * show ethernet service instance detail
    * show ethernet service instance interface <interface> detail
    * show l2vpn vfi
    * show l2vpn service all
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
                'member_ports': list,
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
        #    -   000C.29F8.5078 forward static_r  0    OCE_PTR:0xe8e5dda0
        p6 = re.compile(r'^(?P<member_port>[\w\d\-\/\s\.:]+)( +\(.*\))?$')

        #    AED MAC address    Policy  Tag       Age  Pseudoport
        #    0   0000.A000.0027 forward dynamic   3142 Port-channel1.EFP2051
        #    0   0000.A000.00F2 forward dynamic   3438 GigabitEthernet0/0/3.EFP3051
        #    -   000C.29F8.5078 forward static_r  0    OCE_PTR:0xe8e5dda0
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
    """Schema for show ethernet service instance detail
                  show ethernet service instance interface <interface> detail
    """

    schema = {
        'service_instance': {
            Any(): {
                Optional('type'): str,
                Optional('description'): str,
                'associated_interface': str,
                Optional('associated_evc'): str,
                Optional('l2protocol_drop'): bool,
                Optional('ce_vlans'): str,
                Optional('encapsulation'): str,
                Optional('rewrite'): str,
                Optional('control_policy'): str,
                Optional('intiators'): str,
                Optional('dot1q_tunnel_ethertype'): str,
                'state': str,
                'efp_statistics': {
                    'pkts_in': int,
                    'pkts_out': int,
                    'bytes_in': int,
                    'bytes_out': int,
                }
            },
        }
    }


class ShowEthernetServiceInstanceDetail(ShowEthernetServiceInstanceDetailSchema):
    """Parser for show ethernet service instance detail
                  show ethernet service instance interface <interface> detail
    """

    cli_command = ['show ethernet service instance detail', 'show ethernet service instance interface {interface} detail']

    def cli(self, interface=None, output=None):
        if output is None:
            if interface:
                cli = self.cli_command[1].format(interface=interface)
            else:
                cli = self.cli_command[0]
            out = self.device.execute(cli)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # Service Instance ID: 2051
        p1 = re.compile(r'^Service +Instance +ID: +(?P<service_id>\d+)$')

        # Service Instance Type: Static
        # Service instance type: L2Context
        p2 = re.compile(r'^Service +(i|I)nstance +(t|T)ype: +(?P<service_instance_type>\S+)$')

        # Description: xxx
        p3 = re.compile(r'^Description: +(?P<description>\S+)$')

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

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                service_id = int(group['service_id'])
                final_dict = ret_dict.setdefault('service_instance', {}).\
                    setdefault(service_id, {})
                final_dict['l2protocol_drop'] = False
                final_dict['ce_vlans'] = ''
                final_dict['associated_evc'] = ''
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                final_dict['type'] = group['service_instance_type']
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                final_dict['description'] = group['description']
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                final_dict['associated_interface'] = group['associated_interface']
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                final_dict['associated_evc'] = group['associated_evc']
                continue

            m = p6.match(line)
            if m:
                final_dict['l2protocol_drop'] = True
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                final_dict['ce_vlans'] = group['vlans']
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                final_dict['encapsulation'] = group['encapsulation']
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                final_dict['rewrite'] = group['rewrite']
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                final_dict['dot1q_tunnel_ethertype'] = group['dot1q_tunnel_ethertype']
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                final_dict['state'] = group['state']
                continue

            m = p12.match(line)
            if m:
                final_dict.setdefault('efp_statistics', {})
                continue

            m = p13.match(line)
            if m:
                group = m.groupdict()
                final_dict['efp_statistics'].update({k: \
                    int(v) for k, v in group.items()})
                continue

            m = p14.match(line)
            if m:
                group = m.groupdict()
                final_dict['intiators'] = group['intiators']
                continue

            m = p15.match(line)
            if m:
                group = m.groupdict()
                final_dict['control_policy'] = group['control_policy']
                continue

        return ret_dict


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
            },
        }
    }


class ShowEthernetServiceInstanceStats(ShowEthernetServiceInstanceStatsSchema):
    """Parser for show ethernet service instance stats
                  show ethernet service instance interface <interface> stats
    """

    cli_command = ['show ethernet service instance stats', 'show ethernet service instance interface {interface} stats']

    def cli(self, interface=None, output=None):
        cli = self.cli_command
        if output is None:
            if interface:
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
        p1 = re.compile(r'^System +maximum +number +of +service +instances: +(?P<max_num_of_service_instances>\d+)$')

        # Service Instance 2051, Interface GigabitEthernet0/0/3
        p2 = re.compile(r'^Service +Instance +(?P<service_instance>\d+), Interface +(?P<interface>\S+)$')

        #    Pkts In   Bytes In   Pkts Out  Bytes Out
        #          0          0          0          0
        p3 = re.compile(r'^(?P<pkts_in>\d+) +(?P<bytes_in>\d+) +(?P<pkts_out>\d+) +(?P<bytes_out>\d+)$')

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
# Parser for 'show l2vpn service all'
# ===================================
class ShowL2vpnServiceAllSchema(MetaParser):
    """Schema for show l2vpn service all
    """

    schema = {
        'vpls_name': {
            Any(): {
                'state': str,
                'interface': {
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


class ShowL2vpnServiceAll(ShowL2vpnServiceAllSchema):
    """Parser for show l2vpn service all
    """

    cli_command = 'show l2vpn service all'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # Legend: St=State    XC St=State in the L2VPN Service      Prio=Priority
        #         UP=Up       DN=Down            AD=Admin Down      IA=Inactive
        #         SB=Standby  HS=Hot Standby     RV=Recovering      NH=No Hardware
        #         m=manually selected

        #   Interface          Group       Encapsulation                   Prio  St  XC St
        #   ---------          -----       -------------                   ----  --  -----
        # VPLS name: VPLS-2051, State: UP
        # XC name: serviceWire1, State: UP
        # VPWS name: Gi1/1/1-1001, State: UP
        p1 = re.compile(r'^[\w]+ +name: +(?P<name>[\w\d\-\/]+), +State: +(?P<state>\w+)$')

        #   pw100214           core_pw     1:2051(MPLS)                    0     UP  UP  
        #   pw100001                       VPLS-2051(VFI)                  0     UP  UP   
        #   Eth2/1:20          access_conn EVC 55                  0     UP  UP
        #   Pw2                core        MPLS 10.144.6.6:200        1     SB  IA
        p2 = re.compile(r'^(?P<pw_intf>\S+)( +(?P<group>\S+))? +(?P<encapsulation>\S+(\s{1})?\S+(\s{1}\S+)?)'
                         ' +(?P<priority>\d+) +(?P<intf_state>\w+) +(?P<state_in_l2vpn_service>\w+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                vpls_name = group['name']
                final_dict = ret_dict.setdefault('vpls_name', {}).setdefault(
                    vpls_name, {})
                final_dict['state'] = group['state']
                continue

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

        return ret_dict