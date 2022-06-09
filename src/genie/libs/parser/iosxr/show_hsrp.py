""" show_hsrp.py

IOSXR parsers for show commands:
    * 'show hsrp summary'
    * 'show hsrp {interface} detail'
    * 'show hsrp {address_family} {interface} {group_number} detail'

"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
from genie.libs.parser.utils.common import Common

# ======================================
#   Schema for 'show hsrp summary'
# ======================================
class ShowHsrpSummarySchema(MetaParser):
    """Schema for show hsrp summary"""

    schema = {
        'address_family': {
            Any(): {
                'state': {
                    Any(): {
                        'sessions': int,
                        'slaves': int,
                        'total': int,
                    },
                },
                'intf_total': int,
                'intf_up': int,
                'intf_down': int,
                'vritual_addresses_total': int,
                'virtual_addresses_active': int,
                'virtual_addresses_inactive': int,
            },
        },
        'num_tracked_objects': int,
        'tracked_objects_up': int,
        'tracked_objects_down': int,
        'num_bfd_sessions': int,
        'bfd_sessions_up': int,
        'bfd_sessions_down': int,
        'bfd_sessions_inactive': int,
    }
             

# ======================================
#   Parser for 'show hsrp summary'
# ======================================
class ShowHsrpSummary(ShowHsrpSummarySchema):
    """Parser for show hsrp summary"""

    cli_command = 'show hsrp summary'

    def cli(self,output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        # Init vars
        hsrp_summary_dict = {}
        ipv4_set = False
        ipv6_set = False

        # ALL            2      0     2         0      0     0
        p1 = re.compile(r'(?P<state_name>[a-zA-Z]+)'
                        r' +(?P<v4_sessions>\d+) +(?P<v4_slaves>\d+)'
                        r' +(?P<v4_total>\d+) +(?P<v6_sessions>\d+)'
                        r' +(?P<v6_slaves>\d+) +(?P<v6_total>\d+)$')
        
        # 2    HSRP IPv4 interfaces    (1    up, 1    down)
        p2 = re.compile(r'(?P<num_intf>\d+) +HSRP +IPv4 +interfaces'
                        r' +\(+(?P<intf_up>\d+) +up,'
                        r' +(?P<intf_down>\d+) +down\)$')

        # 0    HSRP IPv6 interfaces    (0    up, 0    down)
        p3 = re.compile(r'(?P<num_intf>\d+) +HSRP +IPv6 +interfaces'
                        r' +\(+(?P<intf_up>\d+) +up,'
                        r' +(?P<intf_down>\d+) +down\)$')

        # 2    Virtual IPv4 addresses  (1    active, 1    inactive)
        p4 = re.compile(r'(?P<num_addresses>\d+) +Virtual +IPv4'
                        r' +addresses +\((?P<active>\d+) +active,'
                        r' +(?P<inactive>\d+) +inactive\)$')

        # 0    Virtual IPv6 addresses  (0    active, 0    inactive)
        p5 = re.compile(r'(?P<num_addresses>\d+) +Virtual +IPv6'
                        r' +addresses +\((?P<active>\d+) +active,'
                        r' +(?P<inactive>\d+) +inactive\)$')

        # 3    Tracked Objects    (1    up, 2    down)
        p6 = re.compile(r'\s*(?P<num_tracked_objects>\d+) +Tracked'
                        r' +Objects +\((?P<tracked_objects_up>\d+) +up,'
                        r' +(?P<tracked_objects_down>\d+) +down\)$')

        # 0    BFD sessions       (0    up, 0    down, 0    inactive)
        p7 = re.compile(r'\s*(?P<num_bfd_sessions>\d+) +BFD +sessions'
                        r' +\((?P<bfd_sessions_up>\d+) +up,'
                        r' +(?P<bfd_sessions_down>\d+) +down,'
                        r' +(?P<bfd_sessions_inactive>\d+) +inactive\)$')

        for line in out.splitlines():
            line = line.strip()
            
            # ALL            2      0     2         0      0     0
            m = p1.match(line)
            if m:
                if 'address_family' not in hsrp_summary_dict:
                    hsrp_summary_dict['address_family'] = {}
                    hsrp_summary_dict['address_family']\
                        ['ipv4'] = {}
                    ipv4 = hsrp_summary_dict['address_family']\
                        ['ipv4']
                    hsrp_summary_dict['address_family']\
                        ['ipv6'] = {}
                    ipv6 = hsrp_summary_dict['address_family']\
                        ['ipv6']
                    ipv4['state'] = {}
                    ipv6['state'] = {}

                state_name = m.groupdict()['state_name']
                v4_sessions = m.groupdict()['v4_sessions']
                v4_slaves = m.groupdict()['v4_slaves']
                v4_total = m.groupdict()['v4_total']
                v6_sessions = m.groupdict()['v6_sessions']
                v6_slaves = m.groupdict()['v6_slaves']
                v6_total = m.groupdict()['v6_total']

                if v4_sessions is not None and v6_sessions is not None:
                    ipv4_set = True
                    ipv6_set = True

                if state_name not in ipv4['state']:
                    ipv4['state'][state_name] = {}
                    ipv4['state'][state_name]['sessions'] = int(v4_sessions)
                    ipv4['state'][state_name]['slaves'] = int(v4_slaves)
                    ipv4['state'][state_name]['total'] = int(v4_total)

                if state_name not in ipv6['state']:
                    ipv6['state'][state_name] = {}
                    ipv6['state'][state_name]['sessions'] = int(v6_sessions)
                    ipv6['state'][state_name]['slaves'] = int(v6_slaves)
                    ipv6['state'][state_name]['total'] = int(v6_total)
                    continue

            # 2    HSRP IPv4 interfaces    (1    up, 1    down)
            m = p2.match(line)
            if m:
                if ipv4_set:
                    ipv4['intf_total'] = int(m.groupdict()['num_intf'])
                    ipv4['intf_up'] = int(m.groupdict()['intf_up'])
                    ipv4['intf_down'] = int(m.groupdict()['intf_down'])
                    continue

            # 0    HSRP IPv6 interfaces    (0    up, 0    down)
            m = p3.match(line)
            if m:
                if ipv6_set:
                    ipv6['intf_total'] = int(m.groupdict()['num_intf'])
                    ipv6['intf_up'] = int(m.groupdict()['intf_up'])
                    ipv6['intf_down'] = int(m.groupdict()['intf_down'])
                    continue

            # 2    Virtual IPv4 addresses  (1    active, 1    inactive)
            m = p4.match(line)
            if m:
                if ipv4_set:
                    ipv4['vritual_addresses_total'] = \
                        int(m.groupdict()['num_addresses'])
                    ipv4['virtual_addresses_active'] = \
                        int(m.groupdict()['active'])
                    ipv4['virtual_addresses_inactive'] = \
                        int(m.groupdict()['inactive'])
                    continue

            # 0    Virtual IPv6 addresses  (0    active, 0    inactive)
            m = p5.match(line)
            if m:
                if ipv6_set:
                    ipv6['vritual_addresses_total'] = \
                        int(m.groupdict()['num_addresses'])
                    ipv6['virtual_addresses_active'] = \
                        int(m.groupdict()['active'])
                    ipv6['virtual_addresses_inactive'] = \
                        int(m.groupdict()['inactive'])
                    continue

            # 3    Tracked Objects    (1    up, 2    down)
            m = p6.match(line)
            if m:
                hsrp_summary_dict['num_tracked_objects'] = \
                    int(m.groupdict()['num_tracked_objects'])
                hsrp_summary_dict['tracked_objects_up'] = \
                    int(m.groupdict()['tracked_objects_up'])
                hsrp_summary_dict['tracked_objects_down'] = \
                    int(m.groupdict()['tracked_objects_down'])
                continue

            # 0    BFD sessions       (0    up, 0    down, 0    inactive)
            m = p7.match(line)
            if m:
                hsrp_summary_dict['num_bfd_sessions'] = \
                    int(m.groupdict()['num_bfd_sessions'])
                hsrp_summary_dict['bfd_sessions_up'] = \
                    int(m.groupdict()['bfd_sessions_up'])
                hsrp_summary_dict['bfd_sessions_down'] = \
                    int(m.groupdict()['bfd_sessions_down'])
                hsrp_summary_dict['bfd_sessions_inactive'] = \
                    int(m.groupdict()['bfd_sessions_inactive'])
                continue

        return hsrp_summary_dict


# ======================================
#   Schema for 'show hsrp detail'       
# ======================================
class ShowHsrpDetailSchema(MetaParser):
    """Schema for show hsrp detail"""
    schema = {
        Any(): {
            'interface': str,
            Optional('bfd'): {
                'enabled': bool,
                'detection_multiplier': int,
                'interval': int,
            },            Optional('use_bia'): bool,
            Optional('delay'): {
                'minimum_delay': int,
                'reload_delay': int,
            },
            'redirects_disable': bool,
            'address_family': {
                Any(): {
                    'version': {
                        Any(): {
                            'groups': {
                                Any(): {
                                    Optional('bfd'): {
                                        'address': str,
                                        'interface_name': str,
                                        Optional('state'): str,
                                    },
                                    Optional('tracked_interfaces'): {
                                        Any(): {
                                            'interface_name': str,
                                            'priority_decrement': int,
                                        }
                                    },
                                    Optional('tracked_objects'): {
                                        'num_tracked_objects': int,
                                        'num_tracked_objects_up': int,
                                        Any(): {
                                            'object_name': str,
                                            'priority_decrement': int,
                                        }
                                    },
                                    'timers': {
                                        'hello_msec_flag': bool,
                                        'hello_msec': int,
                                        Optional('hello_sec'): int,
                                        'hold_msec_flag': bool,
                                        'hold_msec': int,
                                        Optional('hold_sec'): int,
                                        Optional('cfgd_hello_msec'): int,
                                        Optional('cfgd_hold_msec'): int,
                                    },
                                    Optional('primary_ipv4_address'): {
                                        'address': str,
                                    },
                                    Optional('authentication'): str,
                                    Optional('link_local_ipv6_address'): {
                                        Optional('address'): str,
                                        Optional('auto_configure'): str,
                                    },
                                    Optional('statistics'): {
                                        Optional('last_resign_received'): str,
                                        Optional('last_resign_sent'): str,
                                        Optional('last_coup_received'): str,
                                        Optional('last_coup_sent'): str,
                                        Optional('num_state_changes'): int,
                                        Optional('last_state_change'): str,
                                    },
                                    'priority': int,
                                    Optional('preempt'): bool,
                                    Optional('preempt_delay'): int,
                                    Optional('session_name'): str,
                                    Optional('num_of_slaves'): int,
                                    Optional('virtual_mac_address'): str,
                                    'group_number': int,
                                    Optional('active_router'): str,
                                    Optional('standby_router'): str,
                                    Optional('active_ip_address'): str,
                                    Optional('active_ipv6_address'): str,
                                    Optional('active_mac_address'): str,
                                    Optional('standby_ip_address'): str,
                                    Optional('standby_ipv6_address'): str,
                                    Optional('standby_mac_address'): str,
                                    Optional('active_priority'): int,
                                    Optional('standby_priority'): int,
                                    Optional('active_state'): str,
                                    Optional('standby_state'): str,
                                    Optional('active_expire'): str,
                                    Optional('standby_expire'): str,
                                    'hsrp_router_state': str,
                                }
                            },
                            Optional('slave_groups'): {
                                Any(): {
                                    'follow': str,
                                    Optional('bfd'): {
                                        'address': str,
                                        'interface_name': str,
                                    },
                                    Optional('tracked_interfaces'): {
                                        Any(): {
                                            'interface_name': str,
                                            'priority_decrement': int,
                                        }
                                    },
                                    Optional('tracked_objects'): {
                                        'num_tracked_objects': int,
                                        'num_tracked_objects_up': int,
                                        Any(): {
                                            'object_name': str,
                                            'priority_decrement': int,
                                        }
                                    },
                                    Optional('timers'): {
                                        'hello_msec_flag': bool,
                                        'hello_msec': int,
                                        Optional('hello_sec'): int,
                                        'hold_msec_flag': bool,
                                        'hold_msec': int,
                                        Optional('hold_sec'): int,
                                        Optional('cfgd_hello_msec'): int,
                                        Optional('cfgd_hold_msec'): int,
                                    },
                                    Optional('primary_ipv4_address'): {
                                        'address': str,
                                    },
                                    Optional('authentication'): str,
                                    Optional('link_local_ipv6_address'): {
                                        Optional('address'): str,
                                        Optional('auto_configure'): str,
                                    },
                                    Optional('statistics'): {
                                        Optional('last_resign_received'): str,
                                        Optional('last_resign_sent'): str,
                                        Optional('last_coup_received'): str,
                                        Optional('last_coup_sent'): str,
                                        Optional('num_state_changes'): int,
                                        Optional('last_state_change'): str,
                                    },
                                    'priority': int,
                                    Optional('preempt'): bool,
                                    Optional('preempt_delay'): int,
                                    Optional('session_name'): str,
                                    Optional('virtual_mac_address'): str,
                                    'group_number': int,
                                    Optional('active_router'): str,
                                    Optional('standby_router'): str,
                                    Optional('active_ip_address'): str,
                                    Optional('active_ipv6_address'): str,
                                    Optional('active_mac_address'): str,
                                    Optional('standby_ip_address'): str,
                                    Optional('standby_ipv6_address'): str,
                                    Optional('active_priority'): int,
                                    Optional('standby_priority'): int,
                                    Optional('active_state'): str,
                                    Optional('standby_state'): str,
                                    Optional('active_expire'): str,
                                    Optional('standby_expire'): str,
                                    'hsrp_router_state': str,
                                }
                            }
                        }
                    }
                }
            }
        }        
    }


# ======================================
#   Parser for 'show hsrp detail'       
# ======================================
class ShowHsrpDetail(ShowHsrpDetailSchema):
    """Parser for show hsrp detail"""
    """Parser for show hsrp {interface} {group_number} detail"""
    
    cli_command = [
            'show hsrp detail', 
            'show hsrp {interface} detail', 
            'show hsrp {interface} {group_number} detail', 
            'show hsrp {address_family} {interface} {group_number} detail'
    ]    
    exclude = ['last_state_change', 'standby_expire', 'active_expire', 
               'num_state_changes', 'last_coup_received', 'last_coup_sent', 
               'last_resign_received', 'last_resign_sent']

    def cli(self, output=None, address_family='', interface=None, group_number=None):
        if output is None:
            if interface and not group_number and not address_family:
                cmd = self.cli_command[1].format(interface=interface)
            elif interface and group_number and not address_family:
                cmd = self.cli_command[2].format(interface=interface,group_number=group_number)
            elif interface and group_number and  address_family:
                cmd = self.cli_command[3].format(address_family=address_family,\
                          interface=interface,group_number=group_number)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output
        
        # Init vars
        hsrp_detail_dict = {}
        
        # GigabitEthernet0/0/0/1 - IPv4 Group 5 (version 1)
        # Bundle-Ether4.1296 - IPv4 Group 1296 (version 2)
        p1 = re.compile(r'(?P<interface>[\w\/\.-]+)'
                        r' +\- +(?P<address_family>\w+)'
                        r' +Group +(?P<group_number>\d+)'
                        r' +\(version +(?P<version>\d+)\)$')

        # Label group10 (1 slaves)
        p2 = re.compile(r'[lL]abel +(?P<session_name>\S+) +'
                        r'\((?P<num_of_slaves>\d+) slaves\)')

        # Slave to group10
        p3 = re.compile(r'[sS]lave +to +(?P<follow>\S+)$')

        # Local state is Active, priority 110, may preempt
        # Local state is Init, priority 100, use bia
        # Local state is Init, priority 100, may preempt, use bia
        # Local state is Init
        p4 = re.compile(
            r'Local +state +is +(?P<hsrp_router_state>[a-zA-Z]+)'
            r'(, +priority +(?P<priority>\d+))?'
            r'(?P<preempt>, may preempt)?(?P<use_bia>, use bia)?$')

        # Preemption delay for at least 10 secs
        p5 = re.compile(r'Preemption +delay +for +at +least'
                        r' +(?P<preempt_delay>\d+) +secs$')
                    
        # Hellotime 1000 msec holdtime 3000 msec
        p6 = re.compile(r'Hellotime +(?P<hello_msec>\d+) +msec'
                        r' +holdtime +(?P<hold_msec>\d+) +msec$')

        # Configured hellotime 1000 msec holdtime 3000 msec
        p7 = re.compile(r'Configured +hellotime'
                        r' +(?P<cfgd_hello_msec>\d+) msec +holdtime'
                        r' +(?P<cfgd_hold_msec>\d+) +msec$')

        # Minimum delay 5 sec, reload delay 10 sec
        p8 = re.compile(r'Minimum +delay +(?P<minimum_delay>\d+) +sec, +'
                        r'reload +delay +(?P<reload_delay>\d+) +sec$')

        # BFD enabled (GigabitEthernet0/0/0/1, 10.1.1.1): state inactive, interval 15 ms multiplier 3
        # BFD enabled (Unknown, 0.0.0.0): state inactive, interval 0 ms multiplier 0
        p9 = re.compile(
            r'BFD enabled \((?P<bfd_interface_name>\S+), (?P<bfd_address>\S+)\)'
            r': state (?P<bfd_state>\S+), interval (?P<bfd_interval>\d+) ms '
            r'multiplier (?P<bfd_detection_multiplier>\d+)$')

        # Hot standby IP address is 192.168.1.254 configured
        # Hot standby IP address is fe80::205:73ff:fea0:1 configured
        p10 = re.compile(r'Hot +standby +IP +address +is'
                         r' +(?P<vip>[\w\:\.]+) +configured$')

        # Active router is 
        # Active router is 192.168.1.2 expires in 00:00:02
        # Active router is 192.168.1.2, priority 90 expires in 00:00:02
        p11 = re.compile(r'Active +router +is +(?P<active_router>([\w\:\.]+)'
                         r'(, *[\w\.\:]+)?)(, *priority (?P<priority>\d+))?'
                         r'( *(expired|expires +in +(?P<expire>[\w\:\.]+)))?$')

        # Standby router is unknown expired
        # Standby router is 192.168.1.2 expires in 00:00:02
        # Standby router is fe80::5000:1cff:feff:a0b, 5200.1cff.0a0b expires in 00:00:02
        p12 = re.compile(r'Standby +router +is +(?P<standby_router>([\w\:\.]+)'
                         r'(, *[\w\.\:]+)?)( *(expired|expires +in +(?P<expire>'
                         r'[\w\:\.]+)))?$')

        # Standby virtual mac address is 0000.0cff.b30c, state is active
        p13 = re.compile(r'Standby +virtual +mac +address +is'
                         r' +(?P<virtual_mac_address>[\w\.]+),'
                         r' +state +is +(?P<standby_state>[a-zA-Z ]+)$')

        # Authentication text, string "cisco123"
        p14 = re.compile(r'Authentication +text, +string'
                         r' +\"(?P<authentication>\w+)\"$')

        # 4 state changes, last state change 2d03h
        # 2 state changes, last state change 01:18:43
        p15 = re.compile(r'(?P<num_state_changes>\d+) +state'
                         r' +changes, +last +state +change'
                         r' +(?P<last_state_change>[\w\:\.]+)$')

        # Standby ICMP redirects disabled
        p16 = re.compile(r'Standby ICMP redirects disabled')

        # Last coup sent:       Never
        # Last coup sent:       Aug 11 08:26:25.272 UTC
        p17 = re.compile(r'Last +coup +sent: +(?P<last_coup_sent>[\w\s\:\.]+)$')

        # Last coup received:   Never
        p18 = re.compile(r'Last +coup +received:'
                         r' +(?P<last_coup_received>[\w\s\:\.]+)$')

        # Last resign sent:     Never
        p19 = re.compile(r'Last +resign +sent:'
                         r' +(?P<last_resign_sent>[\w\s\:\.]+)$')

        # Last resign received: Never
        # Last resign received: Aug 11 08:26:25.272 UTC
        p20 = re.compile(r'Last +resign +received:'
                         r' +(?P<last_resign_received>[\w\s\:\.]+)$')

        # Tracking states for 1 object, 1 up:
        # Tracking states for 2 objects, 1 up:
        p21 = re.compile(r'Tracking +states +for'
                         r' +(?P<num_tracked_objects>\d+) +objects?,'
                         r' +(?P<num_tracked_objects_up>\d+) up:$')

        # Up   banana               Priority decrement: 20
        # Down   apple               Priority decrement: 50
        # Up   GigabitEthernet0/0/0/1 Priority decrement: 123
        p22 = re.compile(r'(?P<tracked_status>\S+) +'
                         r'((?P<tracked_object>\w+)|'
                         r'(?P<tracked_interface>[\w\/\.\-]+)) +'
                         r'Priority +decrement: +'
                         r'(?P<tracked_object_priority_decrement>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet0/0/0/1 - IPv4 Group 5 (version 1)
            # Bundle-Ether4.1296 - IPv4 Group 1296 (version 2)
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                address_family = m.groupdict()['address_family'].lower()
                if m.groupdict()['version']:
                    version = int(m.groupdict()['version'])                    
                if m.groupdict()['group_number']:
                    group_number = int(m.groupdict()['group_number'])

                if interface not in hsrp_detail_dict:
                    hsrp_detail_dict[interface] = {}
                    hsrp_detail_dict[interface]['interface'] = interface
                if 'address_family' not in hsrp_detail_dict[interface]:
                    hsrp_detail_dict[interface]['address_family'] = {}
                if address_family not in hsrp_detail_dict[interface]\
                    ['address_family']:
                    hsrp_detail_dict[interface]['address_family']\
                        [address_family] = {}
                if 'version' not in hsrp_detail_dict[interface]\
                    ['address_family'][address_family]:
                    hsrp_detail_dict[interface]['address_family']\
                        [address_family]['version'] = {}
                if version not in hsrp_detail_dict[interface]\
                    ['address_family'][address_family]['version']:
                    hsrp_detail_dict[interface]['address_family']\
                        [address_family]['version'][version] = {}
                if 'groups' not in hsrp_detail_dict[interface]\
                    ['address_family'][address_family]['version'][version]:
                    hsrp_detail_dict[interface]['address_family']\
                        [address_family]['version'][version]['groups'] = {}
                if group_number not in hsrp_detail_dict[interface]\
                    ['address_family'][address_family]['version'][version]\
                    ['groups']:
                    hsrp_detail_dict[interface]['address_family']\
                        [address_family]['version'][version]['groups']\
                        [group_number] = {}
                    group_key = {}
                    group_key['group_number'] = group_number
                continue

            # Label group10 (1 slaves)
            m = p2.match(line)
            if m:
                group_key['session_name'] = m.groupdict()['session_name']
                group_key['num_of_slaves'] = int(m.groupdict()['num_of_slaves'])
                continue            

            # Slave to group10
            m = p3.match(line)
            if m:
                group_key['follow'] = m.groupdict()['follow']
                continue

            # Local state is Active, priority 110, may preempt
            # Local state is Init, priority 100, use bia
            # Local state is Init, priority 100, may preempt, use bia
            # Local state is Init
            m = p4.match(line)
            if m:
                group_key['hsrp_router_state'] \
                    = m.groupdict()['hsrp_router_state'].lower()
                if m.groupdict()['priority']:
                    priority = int(m.groupdict()['priority'])
                group_key['priority'] = priority
                if m.groupdict()['preempt'] is not None:
                    group_key['preempt'] = True
                if m.groupdict()['use_bia'] is not None:
                    hsrp_detail_dict[interface]['use_bia'] = True
                else:
                    hsrp_detail_dict[interface]['use_bia'] = False
                continue

            # Preemption delay for at least 10 secs
            m = p5.match(line)
            if m:
                group_key['preempt_delay'] = int(m.groupdict()['preempt_delay'])
                continue

            # Hellotime 1000 msec holdtime 3000 msec
            m = p6.match(line)
            if m:
                if 'timers' not in group_key:
                    group_key['timers'] = {}
                group_key['timers']['hello_msec'] \
                    = int(m.groupdict()['hello_msec'])
                group_key['timers']['hold_msec'] \
                    = int(m.groupdict()['hold_msec'])
                group_key['timers']['hello_msec_flag'] = True
                group_key['timers']['hold_msec_flag'] = True
                continue

            # Configured hellotime 1000 msec holdtime 3000 msec
            m = p7.match(line)
            if m:
                if 'timers' not in group_key:
                    group_key['timers'] = {}
                group_key['timers']['cfgd_hello_msec'] = \
                    int(m.groupdict()['cfgd_hello_msec'])
                group_key['timers']['cfgd_hold_msec'] = \
                    int(m.groupdict()['cfgd_hold_msec'])
                continue

            # Minimum delay 5 sec, reload delay 10 sec
            m = p8.match(line)
            if m:
                if 'delay' not in hsrp_detail_dict[interface]:
                    hsrp_detail_dict[interface]['delay'] = {}
                hsrp_detail_dict[interface]['delay']['minimum_delay'] \
                    = int(m.groupdict()['minimum_delay'])
                hsrp_detail_dict[interface]['delay']['reload_delay'] \
                    = int(m.groupdict()['reload_delay'])
                continue

            # BFD enabled (GigabitEthernet0/0/0/1, 10.1.1.1): state inactive, interval 15 ms multiplier 3
            # BFD enabled (Unknown, 0.0.0.0): state inactive, interval 0 ms multiplier 0
            m = p9.match(line)
            if m:
                if 'bfd' not in hsrp_detail_dict[interface]:
                    hsrp_detail_dict[interface]['bfd'] = {}
                hsrp_detail_dict[interface]['bfd']['enabled'] = True
                if m.groupdict()['bfd_interface_name'] != 'Unknown':
                    hsrp_detail_dict[interface]['bfd']['detection_multiplier'] \
                        = int(m.groupdict()['bfd_detection_multiplier'])
                    hsrp_detail_dict[interface]['bfd']['interval'] \
                        = int(m.groupdict()['bfd_interval'])
                    if 'bfd' not in group_key:
                        group_key['bfd'] = {}
                    group_key['bfd']['address'] = m.groupdict()['bfd_address']
                    group_key['bfd']['interface_name'] \
                        = m.groupdict()['bfd_interface_name']
                    group_key['bfd']['state'] = m.groupdict()['bfd_state']
                continue

            # Hot standby IP address is 192.168.1.254 configured
            # Hot standby IP address is fe80::205:73ff:fea0:1 configured
            m = p10.match(line)
            if m:
                vip = m.groupdict()['vip'].lower()
                if ':' not in vip:
                    if 'primary_ipv4_address' not in group_key:
                        group_key['primary_ipv4_address'] = {}
                    group_key['primary_ipv4_address']['address'] = vip
                else:
                    if 'fe80' in vip:
                        if 'link_local_ipv6_address' not in group_key:
                            group_key['link_local_ipv6_address'] = {}
                        group_key['link_local_ipv6_address']['address'] = vip
                    else:
                        if 'global_ipv6_addresses' not in group_key:
                            group_key['global_ipv6_addresses'] = {}
                        if vip not in group_key['global_ipv6_addresses']:
                            group_key['global_ipv6_addresses'][vip] = {}
                        group_key['global_ipv6_addresses'][vip]['address'] = vip
                
                continue

            # Active router is 
            # Active router is 192.168.1.2 expires in 00:00:02
            # Active router is 192.168.1.2, priority 90 expires in 00:00:02
            m = p11.match(line)
            if m:
                role = m.groupdict()['active_router']
                if role == 'local':
                    try:
                        priority
                    except Exception:
                        pass
                    else:
                        group_key['active_priority'] = int(priority)

                group_key['active_router'] = role
                if role != 'unknown' or role != 'local':
                    if ':' not in role:
                        group_key['active_ip_address'] = role
                    else:
                        group_key['active_ipv6_address'] = role
                    
                if m.groupdict()['expire']:
                    group_key['active_expire'] = m.groupdict()['expire']
                continue

            # Standby router is unknown expired
            # Standby router is 192.168.1.2 expires in 00:00:02
            # Standby router is fe80::5000:1cff:feff:a0b, 5200.1cff.0a0b expires in 00:00:02
            m = p12.match(line)
            if m:
                role = m.groupdict()['standby_router']
                if role == 'local':
                    try:
                        priority
                    except Exception:
                        pass
                    else:
                        group_key['standby_priority'] = int(priority)

                group_key['standby_router'] = role
                if role != 'unknown' or role != 'local':
                    if ':' not in role:
                        group_key['standby_ip_address'] = role
                    else:
                        group_key['standby_ipv6_address'] = role

                if m.groupdict()['expire']:
                    group_key['standby_expire'] = m.groupdict()['expire']
                continue

            # Standby virtual mac address is 0000.0cff.b30c, state is active
            m = p13.match(line)
            if m:
                group_key['virtual_mac_address'] = \
                    m.groupdict()['virtual_mac_address']
                group_key['standby_state'] = m.groupdict()['standby_state']

                # check if group belongs to slave_groups
                if 'follow' in group_key:
                    if 'slave_groups' not in hsrp_detail_dict[interface]\
                        ['address_family'][address_family]['version'][version]:
                        hsrp_detail_dict[interface]['address_family']\
                            [address_family]['version'][version]\
                            ['slave_groups'] = {}
                    if group_number not in hsrp_detail_dict[interface]\
                        ['address_family'][address_family]['version']\
                        [version]['slave_groups']:
                        hsrp_detail_dict[interface]['address_family']\
                            [address_family]['version'][version]\
                            ['slave_groups'][group_number] = {}
                    hsrp_detail_dict[interface]['address_family']\
                        [address_family]['version'][version]['slave_groups']\
                        [group_number] = group_key
                    del hsrp_detail_dict[interface]['address_family']\
                        [address_family]['version'][version]['groups']\
                        [group_number]
                continue

            # Authentication text, string "cisco123"
            m = p14.match(line)
            if m:
                group_key['authentication'] = \
                    m.groupdict()['authentication']
                continue

            # 4 state changes, last state change 2d03h
            # 2 state changes, last state change 01:18:43
            m = p15.match(line)
            if m:
                if 'statistics' not in group_key:
                    group_key['statistics'] = {}
                group_key['statistics']['num_state_changes'] = \
                    int(m.groupdict()['num_state_changes'])
                group_key['statistics']['last_state_change'] = \
                    m.groupdict()['last_state_change']
                continue

            # Standby ICMP redirects disabled
            m = p16.match(line)
            if m:
                hsrp_detail_dict[interface]['redirects_disable'] = True
                continue

            # Last coup sent:       Never
            # Last coup sent:       Aug 11 08:26:25.272 UTC
            m = p17.match(line)
            if m:
                if 'redirects_disable' not in hsrp_detail_dict[interface]:
                    hsrp_detail_dict[interface]['redirects_disable'] = False
                if 'statistics' not in group_key:
                    group_key['statistics'] = {}
                group_key['statistics']['last_coup_sent'] \
                    = m.groupdict()['last_coup_sent']
                continue

            # Last coup received:   Never
            m = p18.match(line)
            if m:
                if 'statistics' not in group_key:
                    group_key['statistics'] = {}
                group_key['statistics']['last_coup_received'] = \
                    m.groupdict()['last_coup_received']
                continue

            # Last resign sent:     Never
            m = p19.match(line)
            if m:
                if 'statistics' not in group_key:
                    group_key['statistics'] = {}
                group_key['statistics']['last_resign_sent'] \
                    = m.groupdict()['last_resign_sent']
                continue

            # Last resign received: Never
            # Last resign received: Aug 11 08:26:25.272 UTC
            m = p20.match(line)
            if m:
                if 'statistics' not in group_key:
                    group_key['statistics'] = {}
                group_key['statistics']['last_resign_received'] = \
                    m.groupdict()['last_resign_received']
                hsrp_detail_dict[interface]['address_family'][address_family]\
                    ['version'][version]['groups'][group_number] = group_key
                continue

            # Tracking states for 1 object, 1 up:
            # Tracking states for 1 objects, 1 up:
            m = p21.match(line)
            if m:
                if 'tracked_objects' not in group_key:
                    group_key['tracked_objects'] = {}
                group_key['tracked_objects']['num_tracked_objects'] = \
                    int(m.groupdict()['num_tracked_objects'])
                group_key['tracked_objects']['num_tracked_objects_up'] = \
                    int(m.groupdict()['num_tracked_objects_up'])
                hsrp_detail_dict[interface]['address_family'][address_family]\
                    ['version'][version]['groups'][group_number] = group_key
                continue

            # Up   banana               Priority decrement: 20
            # Down   apple               Priority decrement: 50
            # Up   GigabitEthernet0/0/0/1 Priority decrement: 123
            m = p22.match(line)
            if m:
                tracked_object = m.groupdict()['tracked_object']
                tracked_interface = m.groupdict()['tracked_interface']
                if tracked_object:
                    if 'tracked_objects' not in group_key:
                        group_key['tracked_objects'] = {}
                    if tracked_object not in group_key:
                        group_key['tracked_objects'][tracked_object] = {}
                    group_key['tracked_objects'][tracked_object]\
                        ['object_name'] = tracked_object
                    group_key['tracked_objects'][tracked_object]\
                        ['priority_decrement'] = int(m.groupdict()\
                        ['tracked_object_priority_decrement'])
                elif tracked_interface:
                    if 'tracked_interfaces' not in group_key:
                        group_key['tracked_interfaces'] = {}
                    if tracked_interface not in group_key['tracked_interfaces']:
                        group_key['tracked_interfaces'][tracked_interface] = {}
                    group_key['tracked_interfaces'][tracked_interface]\
                        ['interface_name'] = tracked_interface
                    group_key['tracked_interfaces'][tracked_interface]\
                        ['priority_decrement'] = int(m.groupdict()\
                        ['tracked_object_priority_decrement']) 
                hsrp_detail_dict[interface]['address_family'][address_family]\
                    ['version'][version]['groups'][group_number] = group_key

        return hsrp_detail_dict

class ShowHsrpBfdSchema(MetaParser):
    ''' Schema for commands:
        * show hsrp bfd
    '''
    schema = {
        'bfd_interface': {
            Any():{
                'groups': {
                    Any(): { 			 
                        'destination_ip': str,
                        'state': str,  
                        'interval': int,
                        'multiplier': int,
                        'hsrp_interface': str,
                        'hsrp_group':int,						
                    }
                },  					
            },
        },
    }

class ShowHsrpBfd(ShowHsrpBfdSchema):
    ''' Parser for commands:
        * show hsrp bfd
    '''
	
    cli_command = [
            'show hsrp bfd', 
            'show hsrp bfd {interface}', 
            'show hsrp bfd {interface} {destination_ip}' 
    ] 

    def cli(self, output=None, interface=None, destination_ip=None):
	
        if output is None:
            if interface and not destination_ip:
                cmd = self.cli_command[1].format(interface=interface)
            elif interface and destination_ip:
                cmd = self.cli_command[2].format(interface=interface,destination_ip=destination_ip)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # BFD Interface    Destination IP  State    Intv Mult HSRP Interface   Grp 
        # -------------    --------------  -----    ---- ---- --------------   ----
        # Gi0/0/0/5        10.1.1.3          up     15    3 Gi0/0/0/5           1
        r1 = re.compile(r'(?P<interface>\S+) +(?P<dest_address>\S+)'
                        r' +(?P<state>\S+) +(?P<interval>\d+)'                    
                        r' +(?P<multiplier>\d+)'
                        r' +(?P<hsrp_intf>\S+) +(?P<group>\S+)$')
     
        parsed_dict = {} 
			
        for line in out.splitlines():                                                
            line = line.strip()
     		
            #Gi0/0/0/5  10.1.1.3   up     15    3  Gi0/0/0/5  1 
            m = r1.match(line)
            if m:
                group = m.groupdict()
                if 'bfd_interface' not in parsed_dict:
                    intf_dict = parsed_dict.setdefault('bfd_interface', {})
                interface = Common.convert_intf_name(group['interface'])
                if interface not in intf_dict:
                    intferface_dict =  intf_dict.setdefault(interface, {})
                if 'groups' not in intferface_dict:
                    group_dict = intferface_dict.setdefault('groups', {})
                if group['group'] not in group_dict:
                    hsrp_dict = group_dict.setdefault(group['group'], {})
                   
                hsrp_dict['destination_ip'] = group['dest_address']
                hsrp_dict['state'] = group['state']
                hsrp_dict['interval'] = int(group['interval'])
                hsrp_dict['multiplier'] = int(group['multiplier'])
                hsrp_interface = Common.convert_intf_name(group['hsrp_intf'])
                hsrp_dict['hsrp_interface'] = hsrp_interface
                hsrp_dict['hsrp_group'] = int(group['group'])
                continue
				
        return parsed_dict
