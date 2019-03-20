''' show_l2vpn.py

IOSXE parsers for the following show commands:

    * show bridge-domain
    * show bridge-domain <WORD>
    * show bridge-domain | count <WORD>
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
            # import pdb; pdb.set_trace()

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