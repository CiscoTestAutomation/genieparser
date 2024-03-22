"""show_vrrp.py

IOSXR parser for the following show commands:
    * 'show vrrp summary'
    * 'show vrrp {interface} detail'
    * 'show vrrp {interface} {group_number} detail'
    * 'show vrrp statistics'
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ======================================
#   Schema for 'show vrrp summary'
# ======================================
class ShowVrrpSummarySchema(MetaParser):
    """Schema for show vrrp summary"""

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
                'num_intf': int,
                'intf_up': int,
                'intf_down': int,
                'vritual_addresses_total': int,
                'virtual_addresses_active': int,
                'virtual_addresses_inactive': int,
                'num_bfd_sessions': int,
                'bfd_sessions_up': int,
                'bfd_sessions_down': int,
                'bfd_sessions_inactive': int,
            },
            'num_tracked_objects': int,
            'tracked_objects_up': int,
            'tracked_objects_down': int,
        }
    }


# ======================================
#   Parser for 'show vrrp summary'
# ======================================
class ShowVrrpSummary(ShowVrrpSummarySchema):
    """Parser for show vrrp summary"""

    cli_command = 'show vrrp summary'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # ALL            2      0     2         0      0     0
        p1 = re.compile(r'(?P<state_name>^[a-zA-Z]+)'
                        r' +(?P<v4_sessions>\d+) +(?P<v4_slaves>\d+)'
                        r' +(?P<v4_total>\d+) +(?P<v6_sessions>\d+)'
                        r' +(?P<v6_slaves>\d+) +(?P<v6_total>\d+)$')

        # 2    VRRP IPv4 interfaces    (1    up, 1    down)
        p2 = re.compile(r'(?P<num_intf>^\d+) +VRRP +IPv4 +interfaces'
                        r' +\(+(?P<intf_up>\d+) +up,'
                        r' +(?P<intf_down>\d+) +down\)$')

        # 0    VRRP IPv6 interfaces    (0    up, 0    down)
        p3 = re.compile(r'(?P<num_intf>^\d+) +VRRP +IPv6 +interfaces'
                        r' +\(+(?P<intf_up>\d+) +up,'
                        r' +(?P<intf_down>\d+) +down\)$')

        # 2    Virtual IPv4 addresses  (1    active, 1    inactive)
        p4 = re.compile(r'(?P<num_addresses>^\d+) +Virtual +IPv4'
                        r' +addresses +\((?P<active>\d+) +active,'
                        r' +(?P<inactive>\d+) +inactive\)$')

        # 0    Virtual IPv6 addresses  (0    active, 0    inactive)
        p5 = re.compile(r'(?P<num_addresses>^\d+) +Virtual +IPv6'
                        r' +addresses +\((?P<active>\d+) +active,'
                        r' +(?P<inactive>\d+) +inactive\)$')

        # 3    Tracked Objects    (1    up, 2    down)
        p6 = re.compile(r'\s*(?P<num_tracked_objects>^\d+) +Tracked'
                        r' +Objects +\((?P<tracked_objects_up>\d+) +up,'
                        r' +(?P<tracked_objects_down>\d+) +down\)$')

        # 0   IPv4 BFD sessions      (0    up, 0    down, 0    inactive)
        p7 = re.compile(r'\s*(?P<num_bfd_sessions>^\d+) +IPv4 +BFD +sessions'
                        r' +\((?P<bfd_sessions_up>\d+) +up,'
                        r' +(?P<bfd_sessions_down>\d+) +down,'
                        r' +(?P<bfd_sessions_inactive>\d+) +inactive\)$')

        # 0   IPv6 BFD sessions      (0    up, 0    down, 0    inactive)
        p8 = re.compile(r'\s*(?P<num_bfd_sessions>^\d+) +IPv6 +BFD +sessions'
                        r' +\((?P<bfd_sessions_up>\d+) +up,'
                        r' +(?P<bfd_sessions_down>\d+) +down,'
                        r' +(?P<bfd_sessions_inactive>\d+) +inactive\)$')

        # MASTER (owner)    0      0     0        0      0     0
        p9 = re.compile(
            r'(?P<state_name>^[a-zA-Z]+) +(?P<sub_name>\([a-zA-Z]+\))'
            r' +(?P<v4_sessions>\d+) +(?P<v4_slaves>\d+) +(?P<v4_total>\d+)'
            r'  +(?P<v6_sessions>\d+) +(?P<v6_slaves>\d+) +(?P<v6_total>\d+)')

        for line in out.splitlines():
            line = line.strip()

            # ALL            2      0     2         0      0     0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                if 'address_family' not in parsed_dict:
                    address_family_dict = parsed_dict.setdefault(
                        'address_family', {})
                    v4_dict = address_family_dict.setdefault('ipv4', {})
                    v4_state_dict = v4_dict.setdefault('state', {})
                    v6_dict = address_family_dict.setdefault('ipv6', {})
                    v6_state_dict = v6_dict.setdefault('state', {})

                v4_state_dict_new = v4_state_dict.setdefault(
                    (group['state_name'].lower()), {})
                v6_state_dict_new = v6_state_dict.setdefault(
                    (group['state_name'].lower()), {})
                v4_state_dict_new['sessions'] = int(group['v4_sessions'])
                v4_state_dict_new['slaves'] = int(group['v4_slaves'])
                v4_state_dict_new['total'] = int(group['v4_total'])
                v6_state_dict_new['sessions'] = int(group['v6_sessions'])
                v6_state_dict_new['slaves'] = int(group['v6_slaves'])
                v6_state_dict_new['total'] = int(group['v6_total'])
                continue

            # 2    VRRP IPv4 interfaces    (1    up, 1    down)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                v4_dict['num_intf'] = int(group['num_intf'])
                v4_dict['intf_up'] = int(group['intf_up'])
                v4_dict['intf_down'] = int(group['intf_down'])
                continue

            # 0    VRRP IPv6 interfaces    (0    up, 0    down)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                v6_dict['num_intf'] = int(group['num_intf'])
                v6_dict['intf_up'] = int(group['intf_up'])
                v6_dict['intf_down'] = int(group['intf_down'])
                continue

            # 2    Virtual IPv4 addresses  (1    active, 1    inactive)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                v4_dict['vritual_addresses_total'] = int(
                    group['num_addresses'])
                v4_dict['virtual_addresses_active'] = int(group['active'])
                v4_dict['virtual_addresses_inactive'] = int(group['inactive'])
                continue

            # 0    Virtual IPv6 addresses  (0    active, 0    inactive)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                v6_dict['vritual_addresses_total'] = int(
                    group['num_addresses'])
                v6_dict['virtual_addresses_active'] = int(group['active'])
                v6_dict['virtual_addresses_inactive'] = int(group['inactive'])
                continue

            # 3    Tracked Objects    (1    up, 2    down)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                address_family_dict['num_tracked_objects'] = int(
                    group['num_tracked_objects'])
                address_family_dict['tracked_objects_up'] = int(
                    group['tracked_objects_up'])
                address_family_dict['tracked_objects_down'] = int(
                    group['tracked_objects_down'])
                continue

            # 0   IPv4 BFD sessions      (0    up, 0    down, 0    inactive)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                v4_dict['num_bfd_sessions'] = int(group['num_bfd_sessions'])
                v4_dict['bfd_sessions_up'] = int(group['bfd_sessions_up'])
                v4_dict['bfd_sessions_down'] = int(group['bfd_sessions_down'])
                v4_dict['bfd_sessions_inactive'] = int(
                    group['bfd_sessions_inactive'])
                continue

            # 0   IPv6 BFD sessions      (0    up, 0    down, 0    inactive)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                v6_dict['num_bfd_sessions'] = int(group['num_bfd_sessions'])
                v6_dict['bfd_sessions_up'] = int(group['bfd_sessions_up'])
                v6_dict['bfd_sessions_down'] = int(group['bfd_sessions_down'])
                v6_dict['bfd_sessions_inactive'] = int(
                    group['bfd_sessions_inactive'])
                continue

            # MASTER (owner)    0      0     0        0      0     0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                v4_state_name = group['state_name'] + group['sub_name']
                v4_state_dict_new = v4_state_dict.setdefault(
                    v4_state_name.lower(), {})
                v6_state_name = group['state_name'] + group['sub_name']
                v6_state_dict_new = v6_state_dict.setdefault(
                    v6_state_name.lower(), {})
                v4_state_dict_new['sessions'] = int(group['v4_sessions'])
                v4_state_dict_new['slaves'] = int(group['v4_slaves'])
                v4_state_dict_new['total'] = int(group['v4_total'])
                v6_state_dict_new['sessions'] = int(group['v6_sessions'])
                v6_state_dict_new['slaves'] = int(group['v6_slaves'])
                v6_state_dict_new['total'] = int(group['v6_total'])
                continue
        return parsed_dict


# ======================================
#   Schema for 'show vrrp detail'
# ======================================
class ShowVrrpDetailSchema(MetaParser):
    """Schema for show vrrp detail"""

    schema = {
        'interface': {
            Any(): {
                'address_family': {
                    Any(): {
                        'vrid': {
                            Any(): {
                                Optional('bfd'): {
                                    'bfd_state': str,
                                    Optional('bfd_interval'): int,
                                    Optional('bfd_multiplier'): int,
                                    Optional('remote_ip'): str,
                                },
                                Optional('tracked'): {
                                    'up_count': int,
                                    'total_count': int,
                                    'decrement_priority': int,
                                    'tracked_objects': {
                                        Any(): {
                                            'object_name': str,
                                            'object_state': str,
                                            'object_decrement': int,
                                        }
                                    },
                                },
                                'router_state': str,
                                Optional('version'): int,
                                Optional('last_resign_received'): str,
                                Optional('last_resign_sent'): str,
                                Optional('last_coup_received'): str,
                                Optional('last_coup_sent'): str,
                                Optional('num_state_changes'): int,
                                Optional('last_state_change'): str,
                                Optional('master_router_ip'): str,
                                Optional('master_router_priority'): str,
                                Optional('virtual_mac_address'): str,
                                Optional('mac_state'): str,
                                Optional('virtual_ip_address'): str,
                                Optional('advertise_time'): str,
                                Optional('advertise_time_force'): str,
                                Optional('master_down_time'): str,
                                Optional('minimum_delay'): int,
                                Optional('reload_delay'): int,
                                Optional('current_priority'): int,
                                Optional('configured_priority'): int,
                                Optional('may_preempt'): bool,
                                Optional('preempt_minimum_delay'): int,
                                Optional('secondary_virtual_ip'): str,
                                Optional('master_name'): str,
                                Optional('number_of_slave'): int,
                                Optional('slave_to'): str,
                                Optional('authentication_string'): str,
                                Optional('master_router_ip'): str,
                                Optional('master_router_priority'): str,								
                            }
                        },
                    }
                },
            }
        }
    }


# ======================================
#   Parser for 'show vrrp detail'
# ======================================
class ShowVrrpDetail(ShowVrrpDetailSchema):
    """Parser for show vrrp detail"""

    cli_command = [
        'show vrrp detail', 'show vrrp {interface} detail',
        'show vrrp {interface} {group_number} detail',
        'show vrrp {address_family} {interface} {group_number} detail'
    ]

    def cli(self,
            output=None,
            address_family='',
            interface=None,
            group_number=None):

        if output is None:
            if interface and not group_number and not address_family:
                cmd = self.cli_command[1].format(interface=interface)
            elif interface and group_number and not address_family:
                cmd = self.cli_command[2].format(interface=interface,
                                                 group_number=group_number)
            elif interface and group_number and address_family:
                cmd = self.cli_command[3].format(address_family=address_family,\
                          interface=interface,group_number=group_number)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        parsed_dict = {}

        # GigabitEthernet0/2/0/1 - IPv4 vrID 100
        p1 = re.compile(r'(?P<interface>^[\w\/\.-]+)'
                        r' +\- +(?P<address_family>\w+)'
                        r' +vrID +(?P<vrid>\d+)$')

        # State is Backup
        p2 = re.compile(r'^State +is +(?P<router_state>[a-zA-Z]+)')

        # 1 state changes, last state change 03:50:23
        p3 = re.compile(r'(?P<num_state_changes>^\d+) +state +changes,'
                        r' +last +state +change +(?P<last_state_change>[\w\:]+)$')

        # Last resign sent: Never
        p4 = re.compile(r'^Last +resign +sent:'
                        r' +(?P<last_resign_sent>[\S ]+)$')

        # Last resign received: Never
        p5 = re.compile(r'^Last +resign +received:'
                        r' +(?P<last_resign_received>[\S ]+)$')

        # Virtual IP address is 10.1.1.1
        p6 = re.compile(r'^Virtual +IP +address'
                        r' +is +(?P<virtual_ip_address>[\w\:\.]+)$')

        # Virtual MAC address is 0000.5E00.0101, state is stored
        p7 = re.compile(r'^Virtual +MAC +address +is'
                        r' +(?P<virtual_mac_address>[\w\.]+),'
                        r' +state +is +(?P<mac_state>[a-zA-Z ]+)$')

        # Master router is 10.1.1.2, priority 254
        p8 = re.compile(r'^Master +router +is +(?P<master_router_ip>\S+)(,'
                        r' +priority +(?P<master_router_priority>\d+))?$')

        # Version is 3
        p9 = re.compile(r'^Version +is +(?P<version>\d+)$')

        # Advertise time 0.100 secs (forced)
        p10 = re.compile(r'^Advertise +time +(?P<advertise_time>[\d\.]+)'
                         r' +secs( +(?P<advertise_time_force>\(forced\)))?$')

        # Master Down Timer 12.031 (3 x 4 + (2 x 4/256))
        p11 = re.compile(r'^Master +Down +Timer +(?P<master_down_time>[\d\.]+)')

        # Minimum delay 2 sec, reload delay 10 sec
        p12 = re.compile(r'^Minimum +delay +(?P<minimum_delay>\d+)'
                         r' +sec, +reload +delay +(?P<reload_delay>\d+) +sec$')

        # Current priority 254
        p13 = re.compile(r'^Current +priority +(?P<current_priority>\d+)')

        # Configured priority 100, may preempt
        p14 = re.compile(r'^Configured +priority'
                         r' +(?P<configured_priority>\d+)'
                         r'(, (?P<may_preempt>may preempt))?')

        # minimum delay 0 secs
        p15 = re.compile(r'^minimum +delay (?P<preempt_minimum_delay>\d+) +secs$')

        # BFD enabled: state inactive, interval 15 ms multiplier 3 remote IP 151.1.0.2
        p16 = re.compile(r'^BFD +enabled: +state (?P<bfd_state>[a-zA-Z]+),'
                         r' +interval +(?P<bfd_interval>\d+) +ms +multiplier'
                         r' +(?P<bfd_multiplier>\d+) +remote IP'
                         r' +(?P<remote_ip>\S+)$')

        # Tracked items: 1/1 up: 0 decrement
        p17 = re.compile(r'^Tracked +items: +(?P<up_count>\d+)\/(?P<total_count>\d+) +up:'
                         r' +(?P<decrement_priority>\d+) +decrement$')
			
        #Object name                State     Decrement
        #GigabitEthernet0/0/0/2        Up            30
        p18 = re.compile(r'(?P<object_name>^\S+) +(?P<object_state>Down|Up) +(?P<object_decrement>\d+)')

        # Secondary Virtual IP address is 12::1
        p19 = re.compile(r'^Secondary +Virtual +IP +address'
                         r' +is +(?P<secondary_virtual_ip>[\w\:\.]+)$')
						 
        #Label masterv6 (1 slaves)
        p20 = re.compile(r'^Label +(?P<lname>(\w+)) +\((?P<lnumber>(\d+)) +(?P<lstatus>(\w+)\))')

        #Slave to masterv6
        p21 = re.compile(r'^Slave +to +(?P<sname>(\w+))$')
	
        #Authentication enabled, string cisco
        p22 = re.compile(r'^Authentication +(?P<auth_status>enabled), +string +(?P<auth_string>(\S+))$')

        # Master router is IP Address owner (12.0.0.2), priority 255
        p23 = re.compile(r'^Master +router +is +IP +Address owner +\((?P<master_router_ip>\S+)\)(,'
                         r' +priority +(?P<master_router_priority>\d+))?$')

        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet0/2/0/1 - IPv4 vrID 100
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface'].lower()
                intf_dict = parsed_dict.setdefault('interface', {})\
                                       .setdefault(interface, {})
                af_dict = intf_dict.setdefault('address_family', {})\
                                   .setdefault((group['address_family'].lower()), {})
                vrf_dict = af_dict.setdefault('vrid', {})\
                                  .setdefault((group['vrid']), {})
                continue

            # State is Backup
            m = p2.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['router_state'] = group['router_state']
                continue

            # 1 state changes, last state change 03:50:23
            m = p3.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['num_state_changes'] = int(group['num_state_changes'])
                vrf_dict['last_state_change'] = group['last_state_change']
                continue

            # Last resign sent: Never
            m = p4.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['last_resign_sent'] = group['last_resign_sent']
                continue

            # Last resign received: Never
            m = p5.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['last_resign_received'] = group['last_resign_received']
                continue

            # Virtual IP address is 10.1.1.1
            m = p6.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['virtual_ip_address'] = group['virtual_ip_address']
                continue

            # Virtual MAC address is 0000.5E00.0101, state is stored
            m = p7.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['virtual_mac_address'] = group['virtual_mac_address']
                vrf_dict['mac_state'] = group['mac_state']
                continue

            # Master router is 10.1.1.2, priority 254
            m = p8.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['master_router_ip'] = group['master_router_ip']
                if group['master_router_priority']:
                    vrf_dict['master_router_priority'] = group['master_router_priority']
                continue

            # Version is 3
            m = p9.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['version'] = int(group['version'])
                continue

            # Advertise time 0.100 secs (forced)
            m = p10.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['advertise_time'] = group['advertise_time']
                if group['advertise_time_force']:
                    vrf_dict['advertise_time_force'] = '10'
                continue

            # Master Down Timer 12.031 (3 x 4 + (2 x 4/256))
            m = p11.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['master_down_time'] = group['master_down_time']
                continue

            # Minimum delay 2 sec, reload delay 10 sec
            m = p12.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['minimum_delay'] = int(group['minimum_delay'])
                vrf_dict['reload_delay'] = int(group['reload_delay'])
                continue

            # Current priority 254
            m = p13.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['current_priority'] = int(group['current_priority'])
                continue

            # Configured priority 100, may preempt
            m = p14.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['configured_priority'] = int(group['configured_priority'])
                if group['may_preempt']:
                    vrf_dict['may_preempt'] = True
                else:
                    vrf_dict['may_preempt'] = False
                continue

            # minimum delay 0 secs
            m = p15.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['preempt_minimum_delay'] = int(group['preempt_minimum_delay'])
                continue

            # BFD enabled: state inactive, interval 15 ms multiplier 3 remote IP 151.1.0.2
            m = p16.match(line)
            if m:
                group = m.groupdict()
                bfd_dict = vrf_dict.setdefault('bfd', {})
                bfd_dict['bfd_state'] = group['bfd_state']
                bfd_dict['bfd_interval'] = int(group['bfd_interval'])
                bfd_dict['bfd_multiplier'] = int(group['bfd_multiplier'])
                bfd_dict['remote_ip'] = group['remote_ip']
                continue

            # Tracked items: 1/1 up: 0 decrement
            m = p17.match(line)
            if m:
                group = m.groupdict()
                track_dict = vrf_dict.setdefault('tracked', {})
                track_dict['up_count'] = int(group['up_count'])
                track_dict['total_count'] = int(group['total_count'])
                track_dict['decrement_priority'] = int(group['decrement_priority'])
                continue

            # Object name                State     Decrement
            # GigabitEthernet0/0/0/2        Up            30
            m = p18.match(line)
            if m:
                group = m.groupdict()
                trackobj_dict = track_dict.setdefault('tracked_objects', {})\
                                          .setdefault((group['object_name'].lower()), {})
                trackobj_dict['object_name'] = group['object_name']
                trackobj_dict['object_state'] = group['object_state']
                trackobj_dict['object_decrement'] = int(group['object_decrement'])
                continue

            # Secondary Virtual IP address is 12::1
            m = p19.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['secondary_virtual_ip'] = group['secondary_virtual_ip']
                continue

            # Label masterv6 (1 slaves)				
            m = p20.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['master_name'] = group['lname']
                vrf_dict['number_of_slave'] = int(group['lnumber'])
                continue
				
            # Slave to masterv6
            m = p21.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['slave_to'] = group['sname']
                continue

            # Authentication enabled, string cisco
            m = p22.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['authentication_string'] = group['auth_string']
                continue

            # Master router is IP Address owner (12.0.0.2), priority 255
            m = p23.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['master_router_ip'] = group['master_router_ip']
                if group['master_router_priority']:
                    vrf_dict['master_router_priority'] = group['master_router_priority']
                continue
				
        return parsed_dict


class ShowVrrpStatisticsSchema(MetaParser):
    """Schema for show vrrp statistics"""

    schema = {
        'vrrp': {
            Any(): {
                Optional('invalid_packets'): {
                    'invalid_checksum': int,
                    'unknown_unsupported_versions': int,
                    'invalid_vrid': int,
                    'too_short': int,
                },
                'protocol': {
                    'transitions_to_master': int,
                },
                'packets': {
                    'total_received': int,
                    'adverts_sent': int,
                    'bad_ttl': int,
                    'short_packets': int,
                    'failed_authentication': int,
                    'unknown_authentication': int,
                    'conflicting_authentication': int,
                    'unknown_type_field': int,
                    'conflicting_advertise_time': int,
                    'conflicting_addresses': int,
                    'received_with_zero_priority': int,
                    'sent_with_zero_priority': int,
                },
            }
        }
    }


class ShowVrrpStatistics(ShowVrrpStatisticsSchema):
    """Parser for show vrrp statistics"""

    cli_command = [
        'show vrrp statistics', 'show vrrp {interface} statistics',
        'show vrrp {interface} {group_number} statistics'
    ]

    def cli(self, interface=None, group_number=None, output=None):

        if output is None:
            if interface and not group_number:
                cmd = self.cli_command[1].format(interface=interface)
            elif interface and group_number:
                cmd = self.cli_command[2].format(interface=interface,
                                                 group_number=group_number)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # Invalid packets:
        p0 = re.compile(r'Invalid +(?P<invalid_packets>packets):')

        # Invalid checksum: 0
        p1 = re.compile(r'Invalid +checksum: +(?P<invalid_checksum>\d+)')

        # Unknown/unsupported versions: 0
        p2 = re.compile(
            r'Unknown\/unsupported +versions: +(?P<unknown_unsupported_versions>\d+)'
        )

        # Invalid vrID: 42
        p3 = re.compile(r'Invalid +vrID: +(?P<invalid_vrid>\d+)')

        #  Too short:  0
        p4 = re.compile(r'Too +short: +(?P<too_short>\d+)')

        # Protocol:
        p5 = re.compile(r'Protocol:')

        # Transitions to Master 5
        p6 = re.compile(
            r'Transitions +to +Master +(?P<transitions_to_master>\d+)')

        # Packets:
        p7 = re.compile(r'Packets:')

        # Total received: 87209
        p8 = re.compile(r'Total +received: +(?P<total_received>\d+)')

        # Adverts sent: 344811478
        p9 = re.compile(r'Adverts sent: +(?P<adverts_sent>\d+)')

        # Bad TTL: 0
        p10 = re.compile(r'Bad TTL: +(?P<bad_ttl>\d+)')

        # Short Packets: 0
        p11 = re.compile(r'Short +Packets: +(?P<short_packets>\d+)')

        # Failed authentication: 0
        p12 = re.compile(
            r'Failed authentication: +(?P<failed_authentication>\d+)')

        # Unknown authentication: 0
        p13 = re.compile(r'Unknown +authentication:'
                         r' +(?P<unknown_authentication>\d+)')

        # Conflicting authentication: 0
        p14 = re.compile(r'Conflicting +authentication:'
                         r' +(?P<conflicting_authentication>\d+)')

        # Unknown Type field: 0
        p15 = re.compile(r'Unknown +Type +field: +(?P<unknown_type_field>\d+)')

        # Conflicting Advertise time: 0
        p16 = re.compile(r'Conflicting +Advertise +time:'
                         r' +(?P<conflicting_advertise_time>\d+)')

        # Conflicting Addresses: 0
        p17 = re.compile(r'Conflicting +Addresses:'
                         r' +(?P<conflicting_addresses>\d+)')

        # Received with zero priority: 0
        p18 = re.compile(r'Received +with +zero +priority:'
                         r' +(?P<received_with_zero_priority>\d+)')

        # Sent with zero priority: 6
        p19 = re.compile(r'Sent +with +zero +priority:'
                         r' +(?P<sent_with_zero_priority>\d+)')

        parsed_dict = {}

        for line in out.splitlines():

            line = line.strip()

            # Invalid packets:
            m = p0.match(line)
            if m:
                group = m.groupdict()
                statistics_dict = parsed_dict.setdefault('vrrp', {})\
                                             .setdefault('statistics', {})
                invalid_packets_dict = statistics_dict.setdefault(
                    'invalid_packets', {})
                continue

            # Invalid checksum: 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                invalid_packets_dict['invalid_checksum'] = int(
                    group['invalid_checksum'])
                continue

            # Unknown/unsupported versions: 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                invalid_packets_dict['unknown_unsupported_versions'] = \
                                int(group['unknown_unsupported_versions'])
                continue

            # Invalid vrID: 42
            m = p3.match(line)
            if m:
                group = m.groupdict()
                invalid_packets_dict['invalid_vrid'] = int(
                    group['invalid_vrid'])
                continue

            #  Too short:  0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                invalid_packets_dict['too_short'] = int(group['too_short'])
                continue

            # Protocol:
            m = p5.match(line)
            if m:
                if 'vrrp' not in parsed_dict:
                    statistics_dict = parsed_dict.setdefault('vrrp', {}) \
                                                 .setdefault('statistics', {})
                protocol_dict = statistics_dict.setdefault('protocol', {})
                continue

            # Transitions to Master 5
            m = p6.match(line)
            if m:
                group = m.groupdict()
                protocol_dict['transitions_to_master'] = \
                                int(group['transitions_to_master'])
                continue

            # Packets:
            m = p7.match(line)
            if m:
                packets_dict = statistics_dict.setdefault('packets', {})
                continue

            # Total received: 87209
            m = p8.match(line)
            if m:
                group = m.groupdict()
                packets_dict['total_received'] = int(group['total_received'])
                continue

            # Adverts sent: 344811478
            m = p9.match(line)
            if m:
                group = m.groupdict()
                packets_dict['adverts_sent'] = int(group['adverts_sent'])
                continue

            # Bad TTL: 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                packets_dict['bad_ttl'] = int(group['bad_ttl'])
                continue

            # Short Packets: 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                packets_dict['short_packets'] = int(group['short_packets'])
                continue

            # Failed authentication: 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                packets_dict['failed_authentication'] = int(
                    group['failed_authentication'])
                continue

            # Unknown authentication: 0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                packets_dict['unknown_authentication'] = int(
                    group['unknown_authentication'])
                continue

            # Conflicting authentication: 0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                packets_dict['conflicting_authentication'] = int(
                    group['conflicting_authentication'])
                continue

            # Unknown Type field: 0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                packets_dict['unknown_type_field'] = int(
                    group['unknown_type_field'])
                continue

            # Conflicting Advertise time: 0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                packets_dict['conflicting_advertise_time'] = int(
                    group['conflicting_advertise_time'])
                continue

            # Conflicting Addresses: 0
            m = p17.match(line)
            if m:
                group = m.groupdict()
                packets_dict['conflicting_addresses'] = int(
                    group['conflicting_addresses'])
                continue

            # Received with zero priority: 0
            m = p18.match(line)
            if m:
                group = m.groupdict()
                packets_dict['received_with_zero_priority'] = int(
                    group['received_with_zero_priority'])
                continue

            # Sent with zero priority: 6
            m = p19.match(line)
            if m:
                group = m.groupdict()
                packets_dict['sent_with_zero_priority'] = int(
                    group['sent_with_zero_priority'])
                continue

        return parsed_dict
