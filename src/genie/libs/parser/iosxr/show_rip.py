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
                                                'address': str,
                                                'uptime': int,
                                                'version': int,
                                                'packets_discarded': int,
                                                'routes_discarded': int
                                            }
                                        },
                                        'out_of_memory_state': str,
                                        'broadcast_for_v2': bool,
                                        'accept_metric_0': bool,
                                        'receive_versions': int,
                                        'send_versions': int,
                                        'oper_status': str,
                                        'address': str,
                                        'passive': bool,
                                        'split_horizon': bool,
                                        'poison_reverse': bool,
                                        'socket_set': {
                                            'multicast_group': bool,
                                            'lpts_filter': bool
                                        },
                                        'statistics': {
                                            'total_packets_received': int
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

    def cli(self, vrf='', output=None):
        if output is None:
            if not vrf:
                vrf = 'default'
                out = self.device.execute(self.cli_commands[0])
            else:
                out = self.device.execute(self.cli_commands[1].format(vrf=vrf))
        else:
            out = output

        ret_dict = {}

        # GigabitEthernet0/0/0/0.100
        p1 = re.compile(r'^(?P<interface>\w+[\d/]+\.\d+)$')

        # Rip enabled?:               Passive
        p2 = re.compile(r'^Rip +enabled\?:\s+(?P<passive>\w+)$')

        # Out-of-memory state:        Normal
        p3 = re.compile(r'^Out-of-memory +state:\s+(?P<state>\w+)$')

        # Broadcast for V2:           No
        p4 = re.compile(r'^Broadcast +for +V2:\s+(?P<broadcast>\w+)$')

        # Accept Metric 0:           No
        p5 = re.compile(r'^Accept +Metric +0:\s+(?P<accept_metric>\w+)$')

        # Send versions:              2
        p6 = re.compile(r'^Send +versions:\s+(?P<version>\d+)$')

        # Receive versions:           2
        p7 = re.compile(r'^Receive +versions:\s+(?P<version>\d+)$')

        # Interface state:            Up
        p8 = re.compile(r'^Interface +state:\s+(?P<state>\w+)$')

        # IP address:                 10.1.2.1/24
        p9 = re.compile(r'^IP +address:\s+(?P<ip_address>[\d\/\.]+)$')

        # Metric Cost:                0
        p10 = re.compile(r'^Metric +Cost:\s+(?P<cost>\d+)$')

        # Split horizon:              Enabled
        p11 = re.compile(r'^Split +horizon:\s+(?P<split_horizon>\w+)$')

        # Poison Reverse:             Disabled
        p12 = re.compile(r'^Poison +Reverse:\s+(?P<poison_reverse>\w+)$')

        # Socket set options:
        p13 = re.compile(r'^Socket +set +options:$')

        # Joined multicast group:    Yes
        p14 = re.compile(r'^Joined +multicast +group:\s+(?P<joined>\w+)$')

        # LPTS filter set:           Yes
        p15 = re.compile(r'^LPTS +filter +set:\s+(?P<filter_set>\w+)$')

        # Authentication mode:        None
        p16 = re.compile(r'^Authentication +mode:\s+(?P<mode>\w+)$')

        # Authentication keychain:    Not set
        p17 = re.compile(r'^Authentication +keychain:\s+(?P<keychain>[\w\s]+)$')

        # Total packets received: 4877
        p18 = re.compile(r'^Total +packets +received:\s+(?P<packets_received>\d+)$')

        # RIP peers attached to this interface:
        p19 = re.compile(r'^RIP +peers +attached +to +this +interface:$')

        # 10.1.2.2
        p20 = re.compile(r'^(?P<peer_address>[\d\.]+)$')

        # uptime (sec): 2    version: 2
        p21 = re.compile(r'^uptime \(sec\): +(?P<uptime>\d+)\s+version: +(?P<version>\d+)$')

        # packets discarded: 0    routes discarded: 4733
        p22 = re.compile(r'packets +discarded: +(?P<packets_discarded>\d+)\s+routes +'
                        r'discarded: +(?P<routes_discarded>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet0/0/0/0.100
            m = p1.match(line)
            if m:
                if not ret_dict:
                    interfaces_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('address_family', {}). \
                                       setdefault('ipv4', {}).setdefault('instance', {}).setdefault('rip', {}). \
                                       setdefault('interfaces', {})
                
                groups = m.groupdict()
                interface_dict = interfaces_dict.setdefault(groups['interface'], {})
                continue

            # Rip enabled?:               Passive
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                passive = True if 'passive' in groups['passive'].lower() else False
                interface_dict.update({'passive': passive})
                continue

            # Out-of-memory state:        Normal
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                interface_dict.update({'out_of_memory_state': groups['state']})
                continue

            # Broadcast for V2:           No
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                broadcast = True if 'yes' in groups['broadcast'].lower() else False
                interface_dict.update({'broadcast_for_v2': broadcast})
                continue

            # Accept Metric 0:           No
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                accept_metric = True if 'yes' in groups['accept_metric'].lower() else False
                interface_dict.update({'accept_metric_0': accept_metric})
                continue

            # Send versions:              2
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                interface_dict.update({'send_versions': int(groups['version'])})
                continue

            # Receive versions:           2
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                interface_dict.update({'receive_versions': int(groups['version'])})
                continue

            # Interface state:            Up
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                interface_dict.update({'oper_status': groups['state']})
                continue

            # IP address:                 10.1.2.1/24
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                interface_dict.update({'address': groups['ip_address']})
                continue

            # Metric Cost:                0
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                interface_dict.update({'cost': int(groups['cost'])})
                continue

            # Split horizon:              Enabled
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                split_horizon = True if 'enabled' in groups['split_horizon'].lower() else False
                interface_dict.update({'split_horizon': split_horizon})
                continue

            # Poison Reverse:             Disabled
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                poison_reverse = True if 'enabled' in groups['poison_reverse'].lower() else False
                interface_dict.update({'poison_reverse': poison_reverse})
                continue

            # Socket set options:
            m = p13.match(line)
            if m:
                socket_dict = interface_dict.setdefault('socket_set', {})
                continue

            # Joined multicast group:    Yes
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                joined = True if 'yes' in groups['joined'].lower() else False
                socket_dict.update({'multicast_group': joined})
                continue

            # LPTS filter set:           Yes
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                filter_set = True if 'yes' in groups['filter_set'].lower() else False
                socket_dict.update({'lpts_filter': filter_set})
                continue

            # Authentication mode:        None
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                if 'authentication' not in interface_dict:
                    auth_dict = interface_dict.setdefault('authentication', {})
                
                auth_key_dict = auth_dict.setdefault('auth_key', {})
                auth_key_dict.update({'crypto_algorithm': groups['mode']})
                continue

            # Authentication keychain:    Not set
            m = p17.match(line)
            if m:
                groups = m.groupdict()
                if 'authentication' not in interface_dict:
                    auth_dict = interface_dict.setdefault('authentication', {})

                auth_key_chain_dict = auth_dict.setdefault('auth_key_chain', {})
                auth_key_chain_dict.update({'key_chain': groups['keychain']})
                continue

            # Total packets received: 4877
            m = p18.match(line)
            if m:
                groups = m.groupdict()
                statistics_dict = interface_dict.setdefault('statistics', {})
                statistics_dict.update({'total_packets_received': int(groups['packets_received'])})
                continue

            # RIP peers attached to this interface:
            m = p19.match(line)
            if m:
                neighbors_dict = interface_dict.setdefault('neighbors', {})
                continue

            # 10.1.2.2
            m = p20.match(line)
            if m:
                groups = m.groupdict()

                neighbor_dict = neighbors_dict.setdefault(groups['peer_address'], {})
                neighbor_dict.update({'address': groups['peer_address']})
                continue

            # uptime (sec): 2    version: 2
            m = p21.match(line)
            if m:
                groups = m.groupdict()
                neighbor_dict.update({'uptime': int(groups['uptime'])})
                neighbor_dict.update({'version': int(groups['version'])})
                continue

            # packets discarded: 0    routes discarded: 4733
            m = p22.match(line)
            if m:
                groups = m.groupdict()
                neighbor_dict.update({'packets_discarded': int(groups['packets_discarded'])})
                neighbor_dict.update({'routes_discarded': int(groups['routes_discarded'])})

        return ret_dict