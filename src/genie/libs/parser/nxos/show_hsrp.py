"""show_hsrp.py

NXOS parsers for show commands:
    * 'show hsrp summary'
    * 'show hsrp all'
    * 'show hsrp delay'
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use


def regexp(expression):
    def match(value):
        if re.match(expression,value):
            return value
        else:
            raise TypeError("Value '%s' doesnt match regex '%s'"
                              %(value,expression))
    return match


# ======================================
#   Schema for 'show hsrp summary'
# ======================================

class ShowHsrpSummarySchema(MetaParser):
    """Schema for show hsrp summary"""
    schema = {
                'nsf': str,
                 Optional('nsf_time'): int,
                 'global_hsrp_bfd': str,
                 'stats': {
                    'total_groups': int,
                    'v1_ipv4': int,
                    'v2_ipv4': int,
                    'v2_ipv6': int,
                    'active': int,
                    'standby': int,
                    'listen': int,
                    'v6_active': int,
                    'v6_standby': int,
                    'v6_listen': int,
                 },
                 'intf_total': int,
                 'total_packets':{
                    'tx_pass': int,
                    'tx_fail': int,
                    'rx_good': int,
                 },
                 'pkt_unknown_groups': int,
                 'total_mts_rx': int,
             }

class ShowHsrpSummary(ShowHsrpSummarySchema):
    """Parser for show hsrp summary"""
    def cli(self):
        cmd = 'show hsrp summary'
        out = self.device.execute(cmd)
        
        # Init vars
        hsrp_summary = {}
        
        
        for line in out.splitlines():
            line = line.rstrip()
            
            # Extended-hold (NSF) enabled, 10 seconds
            # Extended-hold (NSF) disabled
            p1 = re.compile(r'\s*Extended-hold +\(NSF\) +(?P<nsf>[a-zA-Z]+)'
                             '(, +(?P<nsf_time>[0-9]+) seconds)?$')
            m = p1.match(line)
            if m:
                hsrp_summary['nsf'] = m.groupdict()['nsf']
                if m.groupdict()['nsf_time']:
                    hsrp_summary['nsf_time'] = int(m.groupdict()['nsf_time'])
                continue

            # Global HSRP-BFD enabled
            p2 = re.compile(r'\s*Global +HSRP-BFD'
                             ' +(?P<global_hsrp_bfd>[a-zA-Z]+)$')
            m = p2.match(line)
            if m:
                hsrp_summary['global_hsrp_bfd'] = \
                    m.groupdict()['global_hsrp_bfd']
                continue

            # Total Groups: 3
            p3 = re.compile(r'\s*Total +Groups: +(?P<total_groups>[0-9]+)$')
            m = p3.match(line)
            if m:
                if 'stats' not in hsrp_summary:
                    hsrp_summary['stats'] = {}
                hsrp_summary['stats']['total_groups'] = \
                    int(m.groupdict()['total_groups'])
                continue

            # Version::    V1-IPV4: 0       V2-IPV4: 3      V2-IPV6: 0
            p4 = re.compile(r'\s*Version:: +V1-IPV4: +(?P<v1_ipv4>[0-9]+)'
                             ' +V2-IPV4: +(?P<v2_ipv4>[0-9]+) +V2-IPV6:'
                             ' +(?P<v2_ipv6>[0-9]+)$')
            m = p4.match(line)
            if m:
                hsrp_summary['stats']['v1_ipv4'] = int(m.groupdict()['v1_ipv4'])
                hsrp_summary['stats']['v2_ipv4'] = int(m.groupdict()['v2_ipv4'])
                hsrp_summary['stats']['v2_ipv6'] = int(m.groupdict()['v2_ipv6'])
                continue

            # State::     Active: 0       Standby: 0       Listen: 0
            p5 = re.compile(r'\s*State:: +Active: +(?P<active>[0-9]+)'
                             ' +Standby: +(?P<standby>[0-9]+) +Listen:'
                             ' +(?P<listen>[0-9]+)$')
            m = p5.match(line)
            if m:
                hsrp_summary['stats']['active'] = int(m.groupdict()['active'])
                hsrp_summary['stats']['standby'] = int(m.groupdict()['standby'])
                hsrp_summary['stats']['listen'] = int(m.groupdict()['listen'])
                continue

            # State::  V6-Active: 0    V6-Standby: 0    V6-Listen: 0
            p6 = re.compile(r'\s*State:: +V6-Active: +(?P<v6_active>[0-9]+)'
                             ' +V6-Standby: +(?P<v6_standby>[0-9]+)'
                             ' +V6-Listen: +(?P<v6_listen>[0-9]+)$')
            m = p6.match(line)
            if m:
                hsrp_summary['stats']['v6_active'] \
                    = int(m.groupdict()['v6_active'])
                hsrp_summary['stats']['v6_standby'] \
                    = int(m.groupdict()['v6_standby'])
                hsrp_summary['stats']['v6_listen'] \
                    = int(m.groupdict()['v6_listen'])
                continue

            # Total HSRP Enabled interfaces: 1
            p7 = re.compile(r'\s*Total +HSRP +Enabled +interfaces:'
                             ' +(?P<intf_total>[0-9]+)$')
            m = p7.match(line)
            if m:
                hsrp_summary['intf_total'] = int(m.groupdict()['intf_total'])
                continue

            # Tx - Pass: 0       Fail: 0
            p8 = re.compile(r'\s*Tx +\- +Pass: +(?P<tx_pass>[0-9]+) +Fail:'
                             ' +(?P<tx_fail>[0-9]+)$')
            m = p8.match(line)
            if m:
                if 'total_packets' not in hsrp_summary:
                    hsrp_summary['total_packets'] = {}
                hsrp_summary['total_packets']['tx_pass'] \
                    = int(m.groupdict()['tx_pass'])
                hsrp_summary['total_packets']['tx_fail'] \
                    = int(m.groupdict()['tx_fail'])
                continue

            # Rx - Good: 0
            p9 = re.compile(r'\s*Rx +\- +Good: +(?P<rx_good>[0-9]+)$')
            m = p9.match(line)
            if m:
                hsrp_summary['total_packets']['rx_good'] \
                    = int(m.groupdict()['rx_good'])
                continue

            # Packet for unknown groups: 0
            p10 = re.compile(r'\s*Packet +for +unknown +groups:'
                              ' +(?P<pkt_unknown_groups>[0-9]+)$')
            m = p10.match(line)
            if m:
                hsrp_summary['pkt_unknown_groups'] = \
                    int(m.groupdict()['pkt_unknown_groups'])
                continue

            # Total MTS: Rx: 85
            p11 = re.compile(r'\s*Total +MTS: +Rx: +(?P<total_mts_rx>[0-9]+)$')
            m = p11.match(line)
            if m:
                hsrp_summary['total_mts_rx'] = \
                    int(m.groupdict()['total_mts_rx'])
                continue

        return hsrp_summary

# ======================================
#   Schema for 'show hsrp all'
# ======================================

class ShowHsrpAllSchema(MetaParser):
    """Schema for show hsrp all"""
    schema = {
        Any(): {
            'address_family': {
                Any(): {
                    'version': {
                        Any(): {
                            'groups': {
                                Any(): {
                                    'group_number': int,
                                    Optional('tracked_objects'): {
                                        Optional(Any()): {
                                            Optional('object_name'): int,
                                            Optional('status'): str,
                                            Optional('priority_decrement'): int,
                                        }
                                    },
                                    Optional('hsrp_router_state'): str,
                                    Optional('hsrp_router_state_reason'): str,
                                    Optional('priority'): int,
                                    Optional('configured_priority'): int,
                                    Optional('preempt'): bool,
                                    Optional('preempt_reload_delay'): int,
                                    Optional('preempt_min_delay'): int,
                                    Optional('preempt_sync_delay'): int,
                                    'upper_fwd_threshold': int,
                                    'lower_fwd_threshold': int,
                                    Optional('timers'): {
                                        Optional('hello_msec_flag'): bool,
                                        Optional('hello_msec'): int,
                                        Optional('hello_sec'): int,
                                        Optional('hold_msec_flag'): bool,
                                        Optional('hold_msec'): int,
                                        Optional('hold_sec'): int,
                                        Optional('cfged_hello_unit'): str,
                                        Optional('cfged_hello_interval'): int,
                                        Optional('cfged_hold_unit'): str,
                                        Optional('cfged_hold_interval'): int,
                                    },
                                    Optional('primary_ipv4_address'): {
                                        Optional('virtual_ip_learn'): bool,
                                        Optional('address'): str,
                                    },
                                    Optional('secondary_ipv4_addresses'): {
                                        Optional(Any()): {
                                            Optional('address'): str,
                                        }
                                    },
                                    Optional('link_local_ipv6_address'): {
                                        Optional('address'): str,
                                        Optional('auto_configure'): bool,
                                    },
                                    Optional('global_ipv6_addresses'): {
                                        Optional(Any()): {
                                            'address': str,
                                        }
                                    },
                                    'active_router': str,
                                    'standby_router': str,
                                    'virtual_mac_address': str,
                                    'virtual_mac_address_status': str,
                                    Optional('authentication'): str,
                                    'num_state_changes': int,
                                    'last_state_change': str,
                                    Optional('session_name'): str,
                                    Optional('active_priority'): int,
                                    Optional('standby_priority'): int,
                                    Optional('active_expire'): float,
                                    Optional('standby_expire'): float,
                                    Optional('secondary_vips'): list,
                                    Optional('active_ip_address'): str,
                                    Optional('active_ipv6_address'): str,
                                    Optional('active_mac_address'): str,
                                    Optional('standby_ip_address'): str,
                                    Optional('standby_ipv6_address'): str,
                                    Optional('standby_mac_address'): str,
                                }
                            },
                            Optional('slave_groups'): {
                                Optional(Any()): {
                                    Optional('group_number'): int,
                                    Optional('tracked_objects'): {
                                        Optional(Any()): {
                                            Optional('object_name'): int,
                                            Optional('status'): str,
                                            Optional('priority_decrement'): int,
                                        }
                                    },
                                    Optional('hsrp_router_state'): str,
                                    Optional('hsrp_router_state_reason'): str,
                                    Optional('priority'): int,
                                    Optional('configured_priority'): int,
                                    Optional('preempt'): bool,
                                    Optional('preempt_reload_delay'): int,
                                    Optional('preempt_min_delay'): int,
                                    Optional('preempt_sync_delay'): int,
                                    Optional('upper_fwd_threshold'): int,
                                    Optional('lower_fwd_threshold'): int,
                                    Optional('timers'): {
                                        Optional('hello_msec_flag'): bool,
                                        Optional('hello_msec'): int,
                                        Optional('hello_sec'): int,
                                        Optional('hold_msec_flag'): bool,
                                        Optional('hold_msec'): int,
                                        Optional('hold_sec'): int,
                                        Optional('cfged_hello_unit'): str,
                                        Optional('cfged_hello_interval'): int,
                                        Optional('cfged_hold_unit'): str,
                                        Optional('cfged_hold_interval'): int,
                                    },
                                    Optional('primary_ipv4_address'): {
                                        Optional('virtual_ip_learn'): bool,
                                        Optional('address'): str,
                                    },
                                    Optional('secondary_ipv4_addresses'): {
                                        Optional(Any()): {
                                            Optional('address'): str,
                                        }
                                    },
                                    Optional('link_local_ipv6_address'): {
                                        Optional('address'): str,
                                        Optional('auto_configure'): bool,
                                    },
                                    Optional('global_ipv6_addresses'): {
                                        Optional(Any()): {
                                            Optional('address'): str,
                                        }
                                    },
                                    Optional('active_router'): str,
                                    Optional('standby_router'): str,
                                    Optional('virtual_mac_address'): str,
                                    Optional('virtual_mac_address_status'): str,
                                    Optional('authentication'): str,
                                    Optional('num_state_changes'): int,
                                    Optional('last_state_change'): str,
                                    Optional('session_name'): str,
                                    Optional('active_priority'): int,
                                    Optional('standby_priority'): int,
                                    Optional('active_expire'): float,
                                    Optional('standby_expire'): float,
                                    Optional('secondary_vips'): list,
                                    Optional('active_ip_address'): str,
                                    Optional('active_ipv6_address'): str,
                                    Optional('active_mac_address'): str,
                                    Optional('standby_ip_address'): str,
                                    Optional('standby_ipv6_address'): str,
                                    Optional('standby_mac_address'): str,
                                    Optional('follow'): str,
                                }
                            }
                        }
                    },
                },
            },
            'interface': str,
            'use_bia': bool,
        },
    }

class ShowHsrpAll(ShowHsrpAllSchema):
    """Parser for show hsrp all"""
    def cli(self):
        cmd = 'show hsrp all'
        out = self.device.execute(cmd)
        
        # Init vars
        hsrp_all_dict = {}
        secondary_vip_exists = False
        follow = None
        group_key = {}
        flag = False
        
        for line in out.splitlines():
            line = line.rstrip()

            # check for slave_groups
            if line == '' and flag == True:
                if group_key:
                    if follow:
                        if 'slave_groups' not in hsrp_all_dict[interface]\
                            ['address_family'][address_family]['version']\
                            [version]:
                            hsrp_all_dict[interface]['address_family']\
                                [address_family]['version'][version]\
                                ['slave_groups'] = {}
                        if group_number not in hsrp_all_dict[interface]\
                            ['address_family'][address_family]['version']\
                            [version]['slave_groups']:
                            hsrp_all_dict[interface]['address_family']\
                                [address_family]['version'][version]\
                                ['slave_groups'][group_number] = {}
                        hsrp_all_dict[interface]['address_family']\
                            [address_family]['version'][version]\
                            ['slave_groups'][group_number].update(group_key)
                        hsrp_all_dict[interface]['address_family']\
                            [address_family]['version'][version]\
                            ['slave_groups'][group_number]['follow'] = follow
                        del hsrp_all_dict[interface]['address_family']\
                            [address_family]['version'][version]['groups']\
                            [group_number]
                        follow = None
                        flag = False
                    else:
                        hsrp_all_dict[interface]['address_family']\
                            [address_family]['version'][version]['groups']\
                            [group_number].update(group_key)
                        group_key = {}
                        flag = False

            # Ethernet4/1 - Group 0 (HSRP-V2) (IPv4)
            p1 = re.compile(r'\s*(?P<interface>[a-zA-Z0-9\/]+) +\- +Group'
                             ' +(?P<group_number>[0-9]+)'
                             ' +\(HSRP-V(?P<version>[0-9]+)\)'
                             ' +\((?P<address_family>[a-zA-Z0-9]+)\)$')
            m = p1.match(line)
            if m:
                flag = True
                interface = m.groupdict()['interface']
                if interface not in hsrp_all_dict:
                    hsrp_all_dict[interface] = {}
                    hsrp_all_dict[interface]['interface'] = interface

                if 'address_family' not in hsrp_all_dict[interface]:
                    hsrp_all_dict[interface]['address_family'] = {}
                address_family = m.groupdict()['address_family'].lower()
                if address_family not in hsrp_all_dict[interface]\
                    ['address_family']:
                    hsrp_all_dict[interface]['address_family']\
                        [address_family] = {}

                if 'version' not in hsrp_all_dict[interface]['address_family']\
                    [address_family]:
                    hsrp_all_dict[interface]['address_family'][address_family]\
                        ['version'] = {}
                version = int(m.groupdict()['version'])
                if version not in hsrp_all_dict[interface]['address_family']\
                    [address_family]['version']:
                    hsrp_all_dict[interface]['address_family'][address_family]\
                        ['version'][version] = {}

                if 'groups' not in hsrp_all_dict[interface]['address_family']\
                    [address_family]['version'][version]:
                    hsrp_all_dict[interface]['address_family'][address_family]\
                        ['version'][version]['groups'] = {}

                group_number = int(m.groupdict()['group_number'])
                if group_number not in hsrp_all_dict[interface]\
                    ['address_family'][address_family]['version'][version]\
                    ['groups']:
                    hsrp_all_dict[interface]['address_family'][address_family]\
                        ['version'][version]['groups'][group_number] = {}
                    group_key['group_number'] = group_number

                    # reset secondary flag
                    secondary_vip_exists = False
                    continue

            p2 = re.compile(r'\s*Local +state +is'
                             ' +(?P<hsrp_router_state>\S+)'
                             '(\((?P<hsrp_router_state_reason>.+)\))?, '
                             '+priority +(?P<priority>[0-9]+)'' +\(Cfged'
                             ' +(?P<configured_priority>[0-9]+)\)(?:,'
                             ' *(?P<preempt>[a-zA-Z]+) *preempt)?$')
            m = p2.match(line)
            if m:
                group_key['hsrp_router_state'] \
                    = m.groupdict()['hsrp_router_state'].lower()
                if m.groupdict()['hsrp_router_state_reason']:
                    group_key['hsrp_router_state_reason'] \
                        = m.groupdict()['hsrp_router_state_reason'].lower()
                priority = int(m.groupdict()['priority'])
                group_key['priority'] = priority
                group_key['configured_priority'] = \
                    int(m.groupdict()['configured_priority'])
                if m.groupdict()['preempt'] is not None:
                    group_key['preempt'] = True
                    continue

            # Forwarding threshold(for vPC), lower: 1 upper: 110
            p3 = re.compile(r'\s*Forwarding +threshold\(for +vPC\), +lower:'
                             ' +(?P<lower_fwd_threshold>[0-9]+) +upper:'
                             ' +(?P<upper_fwd_threshold>[0-9]+)$')
            m = p3.match(line)
            if m:
                group_key['lower_fwd_threshold'] = \
                    int(m.groupdict()['lower_fwd_threshold'])
                group_key['upper_fwd_threshold'] = \
                    int(m.groupdict()['upper_fwd_threshold'])
                continue

            # Preemption Delay (Seconds) Reload:10 Minimum:5 Sync:5 
            p4 = re.compile(r'\s*Preemption +Delay +\(Seconds\)'
                             '(?: +Reload: *(?P<preempt_reload_delay>[0-9]+))?'
                             '(?: +Minimum: *(?P<preempt_min_delay>[0-9]+))?'
                             '(?: +Sync: *(?P<preempt_sync_delay>[0-9]+))?$')
            m = p4.match(line)
            if m:
                group_key['preempt_reload_delay'] = \
                    int(m.groupdict()['preempt_reload_delay'])
                group_key['preempt_min_delay'] = \
                    int(m.groupdict()['preempt_min_delay'])
                group_key['preempt_min_delay'] = \
                    int(m.groupdict()['preempt_sync_delay'])
                continue

            # Hellotime 1 sec, holdtime 3 sec
            # Hellotime 299 msec, holdtime 2222 msec
            # Hellotime 999 msec (cfged 9 sec), holdtime 2999 msec (cfged 27 sec)
            p5 = re.compile(r'\s*Hellotime +(?P<hello>[0-9]+) '
                '(?P<hello_unit>\S+)( \(cfged (?P<cfged_hello>\d+) '
                '(?P<cfged_hello_unit>\S+)\))?, +holdtime +(?P<hold>[0-9]+) +'
                '(?P<hold_unit>\S+)( \(cfged (?P<cfged_hold>\d+) '
                '(?P<cfged_hold_unit>\S+)\))?$')
            m = p5.match(line)
            if m:
                if 'timers' not in group_key:
                    group_key['timers'] = {}
                hello_unit = m.groupdict()['hello_unit']
                hold_unit = m.groupdict()['hold_unit']
                if hello_unit == 'sec' and hold_unit == 'sec':
                    group_key['timers']['hello_msec_flag'] = False
                    group_key['timers']['hold_msec_flag'] = False
                    group_key['timers']['hello_sec'] \
                        = int(m.groupdict()['hello'])
                    group_key['timers']['hold_sec'] \
                        = int(m.groupdict()['hold'])
                elif hello_unit == 'msec' and hold_unit == 'sec':
                    group_key['timers']['hello_msec_flag'] = True
                    group_key['timers']['hold_msec_flag'] = False
                    group_key['timers']['hello_msec'] \
                        = int(m.groupdict()['hello'])
                    group_key['timers']['hold_sec'] \
                        = int(m.groupdict()['hold'])
                elif hello_unit == 'sec' and hold_unit == 'msec':
                    group_key['timers']['hello_msec_flag'] = False
                    group_key['timers']['hold_msec_flag'] = True
                    group_key['timers']['hello_sec'] \
                        = int(m.groupdict()['hello'])
                    group_key['timers']['hold_msec'] \
                        = int(m.groupdict()['hold'])
                elif hello_unit == 'msec' and hold_unit == 'msec':
                    group_key['timers']['hello_msec_flag'] = True
                    group_key['timers']['hold_msec_flag'] = True
                    group_key['timers']['hello_msec'] \
                        = int(m.groupdict()['hello'])
                    group_key['timers']['hold_msec'] \
                        = int(m.groupdict()['hold'])
                if m.groupdict()['cfged_hello']:
                    group_key['timers']['cfged_hello_interval'] \
                        = int(m.groupdict()['cfged_hello'])
                if m.groupdict()['cfged_hello_unit']:
                    group_key['timers']['cfged_hello_unit'] \
                        = m.groupdict()['cfged_hello_unit']
                if m.groupdict()['cfged_hold']:
                    group_key['timers']['cfged_hold_interval'] \
                        = int(m.groupdict()['cfged_hold'])
                if m.groupdict()['cfged_hold_unit']:
                    group_key['timers']['cfged_hold_unit'] \
                        = m.groupdict()['cfged_hold_unit']

                continue

            # Virtual IP address is 192.168.1.254 (Cfged)
            # Virtual IP address is 10.1.1.254 (Learnt)
            # Virtual IP address is fe80::5:73ff:fea0:14 (Auto)
            # Virtual IP address is fe80::1 (Cfged)
            p6 = re.compile(r'\s*Virtual +IP +address +is'
                             ' +(?P<virtual_ip_address>[\w\:\.]+) +'
                             '\((?P<vip_status>\S+)\)$')
            m = p6.match(line)
            if m:
                virtual_ip_address = m.groupdict()['virtual_ip_address']
                vip_status = m.groupdict()['vip_status']                
                if ':' in virtual_ip_address:
                    # IPv6 Global Address
                    if '/' in virtual_ip_address:
                            if 'global_ipv6_addresses' not in group_key:
                                group_key['global_ipv6_addresses'] = {}
                                if virtual_ip_address not in group_key\
                                    ['global_ipv6_addresses']:
                                    group_key['global_ipv6_addresses']\
                                        [virtual_ip_address] = {}
                                group_key['global_ipv6_addresses']\
                                    [virtual_ip_address]['address'] \
                                    = virtual_ip_address
                    else:
                        # IPv6 Link Local address
                        if 'link_local_ipv6_address' not in group_key:
                            group_key['link_local_ipv6_address'] = {}
                        group_key['link_local_ipv6_address']['address'] \
                            = virtual_ip_address
                        if vip_status == 'Auto':
                            group_key['link_local_ipv6_address']\
                                ['auto_configure'] = True
                        else:
                            group_key['link_local_ipv6_address']\
                                ['auto_configure'] = False
                else:
                    if 'primary_ipv4_address' not in group_key:
                        group_key['primary_ipv4_address'] = {}
                    group_key['primary_ipv4_address']['address'] \
                        = virtual_ip_address
                    if vip_status == 'Learnt':
                        group_key['primary_ipv4_address']['virtual_ip_learn'] \
                            = True
                    else:
                        group_key['primary_ipv4_address']['virtual_ip_learn'] \
                            = False
                continue

            # Secondary Virtual IP address is 10.1.1.253
            p6 = re.compile(r'\s*[sS]econdary +[vV]irtual +IP +address +is +'
                '(?P<secondary_ipv4_address>\S+)')
            m = p6.match(line)
            if m:
                if 'secondary_ipv4_addresses' not in group_key:
                    group_key['secondary_ipv4_addresses'] = {}
                secondary_ipv4_address = m.groupdict()['secondary_ipv4_address']
                if secondary_ipv4_address not in group_key\
                    ['secondary_ipv4_addresses']:
                    group_key['secondary_ipv4_addresses']\
                        [secondary_ipv4_address] = {}
                group_key['secondary_ipv4_addresses'][secondary_ipv4_address]\
                    ['address'] = secondary_ipv4_address


            # Active router is unknown
            # Active router is 192.168.1.1, priority 110 expires in 2.662000 sec(s)
            p7 = re.compile(r'\s*Active +router +is'
                             ' +(?P<active_router>[\w\.\:]+)'
                             '( *, *priority *(?P<active_priority>\d+) '
                             'expires *in *(?P<expire>[\w\.]+) *sec\(s\))?$')
            m = p7.match(line)
            if m:
                role = m.groupdict()['active_router']
                if role == 'local':
                    try:
                        priority
                    except Exception:
                        pass
                    else:
                        active_priority = priority
                else:
                    active_priority = m.groupdict()['active_priority']
                group_key['active_router'] = role
                if active_priority:
                    group_key['active_priority'] = int(active_priority)
                if m.groupdict()['expire']:
                    group_key['active_expire'] = \
                        float(m.groupdict()['expire'])
                if role != 'local' and role != 'unknown':
                    if ':' in role:
                        group_key['active_ipv6_address'] = role
                    else:
                        group_key['active_ip_address'] = role
                continue

            # Standby router is unknown
            # Standby router is 192.168.1.2 , priority 90 expires in 2.426000 sec(s)
            p8 = re.compile(r'\s*Standby +router +is'
                             ' +(?P<standby_router>[\w\.\:]+)'
                             '( *, *priority *(?P<standby_priority>\d+) '
                             'expires *in *(?P<expire>[\w\.]+) *sec\(s\))?$')
            m = p8.match(line)
            if m:
                role = m.groupdict()['standby_router']
                if role == 'local':
                    try:
                        priority
                    except Exception:
                        pass
                    else:
                        standby_priority = priority
                else:
                    standby_priority = m.groupdict()['standby_priority']

                group_key['standby_router'] = role
                if standby_priority:
                    group_key['standby_priority'] = int(standby_priority)
                if m.groupdict()['expire']:
                    group_key['standby_expire'] = \
                        float(m.groupdict()['expire'])
                if role != 'local' and role != 'unknown':
                    if ':' in role:
                        group_key['standby_ipv6_address'] = role
                    else:
                        group_key['standby_ip_address'] = role
                continue

            # Authentication text "cisco123"
            p10 = re.compile(r'\s*Authentication *(?:MD5)?(?:,)?'
                              ' *(?:key-string)? *(?:text)?'
                              ' +\"(?P<authentication>[a-zA-Z0-9]+)\"$')
            m = p10.match(line)
            if m:
                group_key['authentication'] = \
                    m.groupdict()['authentication']
                continue

            # Virtual mac address is 0000.0c9f.f000 (Default MAC)
            p9 = re.compile(r'\s*Virtual +mac +address +is'
                             ' +(?P<virtual_mac_address>[a-zA-Z0-9\.]+)'
                             ' +\((?P<virtual_mac_address_status>\S+) MAC'
                             '( - (?P<use_bia>\S+) enabled)?\)$')
            m = p9.match(line)
            if m:
                group_key['virtual_mac_address'] \
                    = m.groupdict()['virtual_mac_address']
                group_key['virtual_mac_address_status'] \
                    = m.groupdict()['virtual_mac_address_status'].lower()
                if m.groupdict()['use_bia'] == 'use-bia':
                    hsrp_all_dict[interface]['use_bia'] = True
                else:
                    hsrp_all_dict[interface]['use_bia'] = False
                continue

            # 0 state changes, last state change never
            # 4 state changes, last state change 01:42:05
            p11 = re.compile(r'\s*(?P<num_state_changes>[0-9]+) +state'
                              ' +changes, +last +state +change'
                              ' +(?P<last_state_change>[\w\.\:]+)$')
            m = p11.match(line)
            if m:
                group_key['num_state_changes'] = \
                    int(m.groupdict()['num_state_changes'])
                group_key['last_state_change'] = \
                    m.groupdict()['last_state_change']
                continue

            # Track object 1 state UP decrement 22
            p11 = re.compile(r'\s*[tT]rack +object +(?P<tracked_object>\d+)'
                ' +state +(?P<tracked_status>\S+) +decrement'
                ' +(?P<tracked_object_priority_decrement>\d+)')
            m = p11.match(line)

            if m:
                if 'tracked_objects' not in group_key:
                    group_key['tracked_objects'] = {}
                tracked_object = int(m.groupdict()['tracked_object'])
                if tracked_object not in group_key['tracked_objects']:
                    group_key['tracked_objects'][tracked_object] = {}
                group_key['tracked_objects'][tracked_object]['object_name'] =\
                 tracked_object
                group_key['tracked_objects'][tracked_object]\
                ['status'] = m.groupdict()['tracked_status']
                group_key['tracked_objects'][tracked_object]\
                ['priority_decrement'] =\
                 int(m.groupdict()['tracked_object_priority_decrement'])

            # IP redundancy name is hsrp-Eth4/1-0 (default)
            p11 = re.compile(r'\s*IP +redundancy +name +is'
                              ' +(?P<session_name>[a-zA-Z0-9\/\-]+)'
                              ' +\(default\)$')
            m = p11.match(line)
            if m:
                group_key['session_name'] = \
                    m.groupdict()['session_name']
                continue

            # Secondary VIP(s):
            p12 = re.compile(r'\s*Secondary +VIP\(s\):$')
            m = p12.match(line)
            if m:
                secondary_vip_exists = True
                continue

            # 192:168::1
            # 10.1.1.253
            p13 = re.compile(r'\s*(?P<secondary_vips>[\w\:\.]+)+$')
            m = p13.match(line)
            if m and secondary_vip_exists:
                if 'secondary_vips' not in group_key:
                    group_key['secondary_vips'] = []
                secondary_vips = m.groupdict()['secondary_vips']
                group_key['secondary_vips'].append(secondary_vips)
                if 'fe80' not in secondary_vips:
                    if 'global_ipv6_addresses' not in group_key:
                        group_key['global_ipv6_addresses'] = {}
                    if secondary_vips not in group_key['global_ipv6_addresses']:
                        group_key['global_ipv6_addresses'][secondary_vips] = {}
                    group_key['global_ipv6_addresses'][secondary_vips]\
                        ['address'] = secondary_vips

                continue

            # Slave to master: group10 
            p14 = re.compile(r'\s*[sS]lave to master: (?P<follow>\S+)')
            m = p14.match(line)
            if m:
                follow = m.groupdict()['follow']
                continue

        return hsrp_all_dict

# ======================================
#   Schema for 'show hsrp delay'
# ======================================

class ShowHsrpDelaySchema(MetaParser):
    """Schema for show hsrp delay"""
    schema = {
                Any(): {
                    'delay': {
                        'minimum_delay': int,
                        'reload_delay': int,
                    }
                }
             }

class ShowHsrpDelay(ShowHsrpDelaySchema):
    """Parser for show hsrp delay"""
    def cli(self):
        cmd = 'show hsrp delay'
        out = self.device.execute(cmd)

        # Init vars
        hsrp_delay_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # Interface          Minimum Reload
            # (no need to parse above because it's just header)

            # GigabitEthernet1   99      888
            p1 = re.compile(r'\s*(?P<interface>\S+) +(?P<minimum_delay>\d+) +'
                '(?P<reload_delay>\d+)')
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                if interface not in hsrp_delay_dict:
                    hsrp_delay_dict[interface] = {}
                if 'delay' not in hsrp_delay_dict[interface]:
                    hsrp_delay_dict[interface]['delay'] = {}
                hsrp_delay_dict[interface]['delay']['minimum_delay'] \
                    = int(m.groupdict()['minimum_delay'])
                hsrp_delay_dict[interface]['delay']['reload_delay'] \
                    = int(m.groupdict()['reload_delay'])

        return hsrp_delay_dict

# vim: ft=python et sw=4
