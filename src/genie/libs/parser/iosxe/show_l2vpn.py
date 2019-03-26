''' show_l2vpn.py

IOSXE parsers for the following show commands:

    * show bridge-domain
    * show bridge-domain <WORD>
    * show bridge-domain | count <WORD>
    * show ethernet service instance detail
    * show ethernet service instance interface <interface> detail
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
                  show bridge-domain <WORD>
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
                'mac_table': {
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
                  show bridge-domain <WORD>
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

        # Time source is NTP, 19:54:46.940 JST Wed Nov 2 2016
        p4_1 = re.compile(r'^Time +source.*$')

        # AED MAC address    Policy  Tag       Age  Pseudoport
        p4_2 = re.compile(r'^AED +MAC +address +Policy +Tag +Age +Pseudoport$')

        # 1 ports belonging to split-horizon group 0
        p5 = re.compile(r'^(?P<num_of_ports>\d+) +ports +belonging +to +(?P<port_belonging_group>[\w\-\d]+) +group +(?P<group_number>\d+)$')

        #     vfi VPLS-2051 neighbor 27.93.202.64 2051
        #     Port-channel1 service instance 2051 (split-horizon)
        #     GigabitEthernet0/0/3 service instance 3051 (split-horizon)
        p6 = re.compile(r'^(?P<member_port>[\w\d\-\/\s\.]+)( +\(.*\))?$')

        #    AED MAC address    Policy  Tag       Age  Pseudoport
        #    0   0000.A000.0027 forward dynamic   3142 Port-channel1.EFP2051
        #    0   0000.A000.00F2 forward dynamic   3438 GigabitEthernet0/0/3.EFP3051
        p7 = re.compile(r'^(?P<aed>\d+) +(?P<mac_address>[\w\d\.]+) +(?P<policy>\w+) +(?P<tag>\w+) +(?P<age>\d+) +(?P<pseudoport>[\w\d\-\.\/]+)$')

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
                        [mac_address]['aed'] = int(group['aed'])
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
        p3 = re.compile(r'^(?P<service>[\w\s\d]+) +(?P<total>\d+) +(?P<up>\d+) +(?P<admin_do>\d+) +(?P<down>\d+) +(?P<error_di>\d+) +(?P<unknown>\d+) +(?P<deleted>\d+) +(?P<bd_adm_do>\d+)$')

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
                service = group.pop('service')
                ret_dict[header].setdefault(service , {})
                ret_dict[header][service].update({k: int(v) for k, v in group.items()})
                continue

        return ret_dict