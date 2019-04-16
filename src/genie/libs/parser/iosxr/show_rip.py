"""show_rip.py

IOSXR parser for the following show commands:
    * show rip
    * show rip vrf {vrf}
    * show rip database
    * show rip vrf {vrf} database
    * show rip interface
    * show rip vrf {vrf} interface
    * show rip statistics
    * show rip vrf {vrf} statistics
"""

# Python
import re

# MetaParser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# ======================================
# Schema for:
#    show rip interface
#    show rip vrf {vrf} interface
# ======================================
class ShowRipInterfaceSchema(MetaParser):
    """Schema for:
        show rip interface
        show rip vrf {vrf} interface"""

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'instance': {
                            Any(): {
                                'interfaces': {
                                    Any(): {
                                        'authentication': {
                                            'auth_key_chain': {
                                                'key_chain': str
                                            },
                                            'auth_key': {
                                                'crypto_algorithm': str
                                            }
                                        },
                                        'cost': int,
                                        Optional('neighbors'): {
                                            Any(): {
                                                'address': str
                                            }
                                        },
                                        'out_of_memory_state': str,
                                        'broadcast_for_v2': bool,
                                        'accept_metric_0': bool,
                                        'receive_versions': int,
                                        'send_versions': int,
                                        'interface_state': str,
                                        'address': str,
                                        'passive': bool,
                                        'split_horizon': bool,
                                        'poison_reverse': bool,
                                        'socket_set': {
                                            'multicast_group': bool,
                                            'lpts_filter': bool
                                        },
                                        'statistics': {
                                            Optional('discontinuity_time'): int,
                                            Optional('bad_packets_rcvd'): int,
                                            Optional('bad_routes_rcvd'): int,
                                            'updates_sent': int
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


# ======================================
# Parser for:
#    show rip interface
#    show rip vrf {vrf} interface
# ======================================
class ShowRipInterface(ShowRipInterfaceSchema):
    """Parser for:
        show rip interface
        show rip vrf {vrf} interface"""

    cli_commands = ['show rip interface', 'show rip vrf {vrf} interface']

    def cli(self, vrf=None, output=None):
        if output is None:
            if not vrf:
                out = self.device.execute(self.cli_commands[0])
            else:
                out = self.device.execute(self.cli_commands[1].format(vrf=vrf))
        else:
            out = output

        # ==============
        # Compiled Regex
        # ==============
        # GigabitEthernet0/0/0/0.100
        p1 = re.compile(r'^(?P<interface>\w+[\d/]+\.\d+)$')
        # Rip enabled?:               Passive
        # Out-of-memory state:        Normal
        # Broadcast for V2:           No
        # Accept Metric 0:           No
        # Send versions:              2
        # Receive versions:           2
        # Interface state:            Up
        # IP address:                 10.1.2.1/24
        # Metric Cost:                0
        # Split horizon:              Enabled
        # Poison Reverse:             Disabled
        p2 = re.compile(r'^(?P<parameter>[\w\s\-\?]+):\s+(?P<value>[\w\./\s]+)$')
        # 10.1.2.2
        p3 = re.compile(r'^(?P<peer_address>[\d\.]+)$')
        # uptime (sec): 2    version: 2
        # packets discarded: 0    routes discarded: 4733
        p4 = re.compile(r'^(?P<parameter1>[\w\s\(\)]+): +(?P<value1>\d+)\s+'
                        r'(?P<parameter2>[\w\s]+): +(?P<value2>\d+)$')

        ret_dict = {}

        if out:
            interfaces_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('address_family', {}). \
                                       setdefault(None, {}).setdefault('instance', {}).setdefault('rip', {}). \
                                       setdefault('interfaces', {})

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                # Reset dictionaries for parsing of new interface
                auth_dict = None 
                neighbors_dict = None
                socket_set_dict = None
                statistics_dict = None
                
                groups = m.groupdict()
                interface_dict = interfaces_dict.setdefault(groups['interface'], {})
                continue

            if 'Socket set options' in line:
                if not socket_set_dict:
                    socket_set_dict = interface_dict.setdefault('socket_set', {})
                continue

            m = p2.match(line)
            if m:
                groups = m.groupdict()
                parameter = groups['parameter']
                value = groups['value']

                # !START COMMENT BLOCK
                # These if blocks are used for ops model specific parameters
                if 'Rip enabled?' in parameter:
                    value = True if value in ['Yes', 'Passive'] else False
                    interface_dict.update({'passive': value})
                    continue
                
                if 'Authentication' in parameter:
                    if not auth_dict:
                        auth_dict = interface_dict.setdefault('authentication', {})
                    
                    if 'Authentication mode' in parameter:
                        auth_key_dict = auth_dict.setdefault('auth_key', {})
                        auth_key_dict.update({'crypto_algorithm': value})
                    
                    if 'Authentication keychain' in parameter:
                        auth_key_chain_dict = auth_dict.setdefault('auth_key_chain', {})
                        auth_key_chain_dict.update({'key_chain': value})

                    continue

                if 'Metric Cost' in parameter:
                    interface_dict.update({'cost': int(value)})
                    continue

                if 'IP address' in parameter:
                    interface_dict.update({'address': value})
                    continue
                
                if 'Joined multicast group' in parameter:
                    socket_set_dict.update({'multicast_group': True if 'Yes' in value else False})
                    continue
                
                if 'LPTS filter set' in parameter:
                    socket_set_dict.update({'lpts_filter': True if 'Yes' in value else False})
                    continue
                
                if 'packets received' in parameter:
                    if not statistics_dict:
                        statistics_dict = interface_dict.setdefault('statistics', {})

                    statistics_dict.update({'updates_sent': int(value)})
                    continue
                # !END COMMENT BLOCK

                parameter = re.sub(r'[ -]', '_', parameter).lower()
                if parameter in ['broadcast_for_v2', 'accept_metric_0', 
                                    'split_horizon', 'poison_reverse']:
                    value = True if value in ['Yes', 'Enabled'] else False
                    interface_dict.update({parameter: value})
                    continue
                
                if parameter in ['receive_versions', 'send_versions']:
                    interface_dict.update({parameter: int(value)})
                    continue

                interface_dict.update({parameter: value})
                continue

            m = p3.match(line)
            if m:
                groups = m.groupdict()

                if not neighbors_dict:
                    neighbors_dict = interface_dict.setdefault('neighbors', {})

                neighbor_dict = neighbors_dict.setdefault(groups['peer_address'], {})
                neighbor_dict.update({'address': groups['peer_address']})
                continue

            m = p4.match(line)
            if m:
                groups = m.groupdict()
                
                if 'uptime' in groups['parameter1']:
                    parameter1 = 'discontinuity_time'
                elif 'packets' in groups['parameter1']:
                    parameter1 = 'bad_packets_rcvd'

                statistics_dict.update({parameter1: int(groups['value1'])})

                if 'routes' in groups['parameter2']:
                    parameter2 = 'bad_routes_rcvd'
                    statistics_dict.update({parameter2: int(groups['value2'])})
                    
        return ret_dict