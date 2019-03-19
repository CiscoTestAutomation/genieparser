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
                'vpls': str,
                'neighbor': str,
                'no_of_ports_belongs': str,
                'port_belonging_group': str,
                'group_number': str,
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

    cli_command = 'show bridge-domain'

    def cli(self, keyword=None, count=False, output=None):
        cli = self.cli_command
        if output is None:
            if keyword:
                if count:
                    cli = cli + ' | count'
                cli = cli + ' {keyword}'.format(keyword=keyword)
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

        #     vfi VPLS-2051 neighbor 27.93.202.64 2051
        p4 = re.compile(r'^vfi +(?P<vpls>[\d\w\-]+) +neighbor (?P<neighbor>[\d\.]+) +(\d+)$')

        # # 1 ports belonging to split-horizon group 0
        p5 = re.compile(r'^(?P<no_of_ports_belongs>[\w\-\d]+) +ports +belonging +to +(?P<port_belonging_group>[\w\-\d]+) +group +(?P<group_number>\d+)$')

        #     Port-channel1 service instance 2051 (split-horizon)
        #     GigabitEthernet0/0/3 service instance 3051 (split-horizon)
        p6 = re.compile(r'^(?P<member_port>[\w\d\-\/]+) +service +instance +(\d+) +\(.*\)$')

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
                group = m.groupdict()
                final_dict.update({k:v for k, v in group.items()})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                final_dict.update({k:v for k, v in group.items()})
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                member_port_list.append(group['member_port'])
                final_dict['member_ports'] = member_port_list
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                pseudoport = group['pseudoport']
                mac_address = group['mac_address']
                final_dict.setdefault('mac_table', {}).setdefault(
                    pseudoport, {}).setdefault('mac_address', {}).setdefault(mac_address, {})
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

            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict['lines_match_regexp'] = int(group['lines_match_regexp'])
                continue

        return ret_dict