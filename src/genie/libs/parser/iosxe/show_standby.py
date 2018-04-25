"""show_hsrp.py

IOSXE parsers for show commands:
    * 'show standby all'
    * 'show standby internal'
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
#   Parser for 'show standby internal'
# ======================================

class ShowStandbyInternalSchema(MetaParser):
    """Schema for show standby internal"""
    schema = \
            {
                'hsrp_common_process_state': str,
                Optional('msgQ_size'): int,
                Optional('msgQ_max_size'): int,
                'hsrp_ipv4_process_state': str,
                'hsrp_ipv6_process_state': str,
                'hsrp_timer_wheel_state': str,
                'hsrp_ha_state': str,
                'v3_to_v4_transform': str,
                Optional('virtual_ip_hash_table'): {
                    Any(): {
                        Any(): {
                            'ip': str,
                            'interface': str,
                            'group': int,
                        }
                    }
                },
                Optional('mac_address_table'): {
                    Any(): {
                        'interface': str,
                        'mac_address': str,
                        'group': int,
                    }
                }
            }


class ShowStandbyInternal(ShowStandbyInternalSchema):
    """Parser for show standby internal"""

    def cli(self):
        cmd = 'show standby internal'.format()
        out = self.device.execute(cmd)
        
        # Init vars
        standby_internal_dict = {}
        
        for line in out.splitlines():
            line = line.rstrip()
            
            # HSRP common process running
            p1 = re.compile(r'\s*HSRP +common +process'
                             ' +(?P<hsrp_common_process_state>[a-zA-Z\s]+)$')
            m = p1.match(line)
            if m:
                stby_internal = standby_internal_dict
                stby_internal['hsrp_common_process_state'] = \
                    m.groupdict()['hsrp_common_process_state']

            # MsgQ size 0, max 2
            p2 = re.compile(r'\s*MsgQ +size +(?P<msgQ_size>[0-9]+),'
                             ' +max +(?P<msgQ_max_size>[0-9]+)$')
            m = p2.match(line)
            if m:
                stby_internal['msgQ_size'] = int(m.groupdict()['msgQ_size'])
                stby_internal['msgQ_max_size'] = \
                    int(m.groupdict()['msgQ_max_size'])
                continue

            # HSRP IPv4 process running
            p3 = re.compile(r'\s*HSRP +IPv4 +process'
                             ' +(?P<hsrp_ipv4_process_state>[a-zA-Z\s]+)$')
            m = p3.match(line)
            if m:
                stby_internal['hsrp_ipv4_process_state'] = \
                    m.groupdict()['hsrp_ipv4_process_state']
                continue

            # HSRP IPv6 process not running
            p4 = re.compile(r'\s*HSRP +IPv6 +process'
                             ' +(?P<hsrp_ipv6_process_state>[a-zA-Z\s]+)$')
            m = p4.match(line)
            if m:
                stby_internal['hsrp_ipv6_process_state'] = \
                    m.groupdict()['hsrp_ipv6_process_state']
                continue

            # HSRP Timer wheel running
            p5 = re.compile(r'\s*HSRP +Timer +wheel'
                             ' +(?P<hsrp_timer_wheel_state>[a-zA-Z\s]+)$')
            m = p5.match(line)
            if m:
                stby_internal['hsrp_timer_wheel_state'] = \
                    m.groupdict()['hsrp_timer_wheel_state']
                continue

            # HSRP HA capable, v3 to v4 transform disabled
            p6 = re.compile(r'\s*HSRP +HA +(?P<hsrp_ha_state>[a-zA-Z\s]+),'
                             ' +v3 +to +v4 +transform'
                             ' +(?P<v3_to_v4_transform>[a-zA-Z\s]+)$')
            m = p6.match(line)
            if m:
                stby_internal['hsrp_ha_state'] = m.groupdict()['hsrp_ha_state']
                stby_internal['v3_to_v4_transform'] = \
                    m.groupdict()['v3_to_v4_transform']
                continue

            # HSRP virtual IP Hash Table (global)
            # 103 192.168.1.254                    Gi1/0/1    Grp 0
            # HSRP virtual IPv6 Hash Table (global)
            # 78  2001:DB8:10:1:1::254             Gi1        Grp 20
            p7 = re.compile(r'\s*(?P<hsrp>[0-9]+) +(?P<ip>[0-9a-zA-Z\.\:]+)'
                             ' +(?P<interface>[a-zA-Z0-9\/]+)'
                             ' +Grp +(?P<group>[0-9]+)$')
            m = p7.match(line)
            if m:
                hsrp = int(m.groupdict()['hsrp'])

                if 'virtual_ip_hash_table' not in stby_internal:
                    stby_internal['virtual_ip_hash_table'] = {}

                if ':' not in m.groupdict()['ip']:
                    protocol = 'ipv4'
                else:
                    protocol = 'ipv6'
                if protocol not in stby_internal['virtual_ip_hash_table']:
                    stby_internal['virtual_ip_hash_table'][protocol] = {}

                if hsrp not in stby_internal['virtual_ip_hash_table']:
                    stby_internal['virtual_ip_hash_table'][protocol][hsrp] = {}
                    stby_internal['virtual_ip_hash_table'][protocol][hsrp]\
                        ['interface'] = m.groupdict()['interface'].lower()
                    stby_internal['virtual_ip_hash_table'][protocol][hsrp]\
                        ['ip']= m.groupdict()['ip']
                    stby_internal['virtual_ip_hash_table'][protocol][hsrp]\
                        ['group']= int(m.groupdict()['group'])
                    continue

            # HSRP MAC Address Table
            # 240 Gi1/0/1 0000.0c9f.f000
            p8 = re.compile(r'\s*(?P<hsrp_number>[0-9]+)'
                             ' +(?P<interface>[a-zA-Z0-9\/]+)'
                             ' +(?P<mac_address>[a-zA-Z0-9\.]+)$')
            m = p8.match(line)
            if m:
                # Save last interface
                last_interface = m.groupdict()['interface'].lower()
                hsrp_number = int(m.groupdict()['hsrp_number'])

                if 'mac_address_table' not in stby_internal:
                    stby_internal['mac_address_table'] = {}

                if hsrp_number not in stby_internal['mac_address_table']:
                    stby_internal['mac_address_table'][hsrp_number] = {}
                    stby_internal['mac_address_table'][hsrp_number]\
                        ['interface'] = m.groupdict()['interface'].lower()
                    stby_internal['mac_address_table'][hsrp_number]\
                        ['mac_address'] = m.groupdict()['mac_address']
                    continue

            # HSRP MAC Address Table
            # Gi1/0/1 Grp 0
            p8_1 = re.compile(r'\s*(?P<interface>[a-zA-Z0-9\/]+)'
                               ' +Grp +(?P<group>[0-9]+)$')
            m = p8_1.match(line)
            if m:
                interface = m.groupdict()['interface'].lower()
                if interface == last_interface:
                    stby_internal['mac_address_table'][hsrp_number]['group']\
                         = int(m.groupdict()['group'])
                    continue

        return standby_internal_dict


# ======================================
#   Schema for 'show standby all'
# ======================================

class ShowStandbyAllSchema(MetaParser):
    """Schema for show standby all"""
    schema = \
    {
        Any(): {
            Optional('use_bia'): bool,
            Optional('redirects_disable'): bool,
            Optional('interface'): str,
            Optional('mac_refresh'): int,
            Optional('mac_next_refresh'): int,
            'address_family': {
                Any(): {
                    'version': {
                        Any(): {
                            'groups': {
                                Any(): {
                                    'group_number': int,
                                    Optional('follow'): str,
                                    Optional('hsrp_router_state'): str,
                                    Optional('hsrp_router_state_reason'): str,
                                    Optional('last_state_change'): str,
                                    Optional('authentication'): str,
                                    Optional('authentication_type'): str,
                                    Optional('tracked_objects'): {
                                        Optional(Any()): {
                                            Optional('object_name'): int,
                                        }
                                    },
                                    Optional('timers'): {
                                        Optional('hello_msec_flag'): bool,
                                        Optional('hello_msec'): int,
                                        Optional('hello_sec'): int,
                                        Optional('hold_msec_flag'): bool,
                                        Optional('hold_msec'): int,
                                        Optional('hold_sec'): int,
                                        Optional('cfgd_hello_msec'): int,
                                        Optional('cfgd_hold_msec'): int,
                                        Optional('next_hello_sent'): float,
                                    },
                                    Optional('primary_ipv4_address'): {
                                        'address': str,
                                    },
                                    Optional('secondary_ipv4_addresses'): {
                                        Any(): {
                                            'address': str,
                                        }
                                    },
                                    Optional('link_local_ipv6_address'): {
                                        Optional('address'): str,
                                        Optional('auto_configure'): str,
                                    },
                                    Optional('global_ipv6_addresses'): {
                                        Any(): {
                                            'address': str,
                                        }
                                    },
                                    Optional('priority'): int,
                                    Optional('preempt'): bool,
                                    Optional('preempt_min_delay'): int,
                                    Optional('preempt_reload_delay'): int,
                                    Optional('preempt_sync_delay'): int,
                                    Optional('statistics'): {
                                        Optional('num_state_changes'): int,
                                    },
                                    Optional('active_router_priority'): int,
                                    Optional('active_ip_address'): str,
                                    Optional('active_ipv6_address'): str,
                                    Optional('active_expires_in'): float,
                                    Optional('default_priority'): int,
                                    Optional('configured_priority'): int,
                                    Optional('session_name'): str,
                                    Optional('active_mac_address'): str,
                                    Optional('active_mac_in_use'): bool,
                                    Optional('local_virtual_mac_address'): str,
                                    Optional('local_virtual_mac_default'): str,
                                    Optional('active_router'): str,
                                    Optional('standby_router'): str,
                                    Optional('standby_ip_address'): str,
                                    Optional('standby_ipv6_address'): str,
                                    Optional('virtual_mac_address_mac_in_use'): bool,
                                    Optional('local_virtual_mac_address_conf'): str,
                                    Optional('virtual_mac_address'): str,
                                    Optional('slave_group_number'): int,
                                    Optional('standby_priority'): int,
                                    Optional('standby_expires_in'): float,
                                }
                            },
                            Optional('slave_groups'): {
                                Any(): {
                                    'group_number': int,
                                    Optional('follow'): str,
                                    Optional('hsrp_router_state'): str,
                                    Optional('hsrp_router_state_reason'): str,
                                    Optional('last_state_change'): str,
                                    Optional('authentication'): str,
                                    Optional('authentication_type'): str,
                                    Optional('tracked_objects'): {
                                        Optional(Any()): {
                                            Optional('object_name'): int,
                                        }
                                    },
                                    Optional('timers'): {
                                        Optional('hello_msec_flag'): bool,
                                        Optional('hello_msec'): int,
                                        Optional('hello_sec'): int,
                                        Optional('hold_msec_flag'): bool,
                                        Optional('hold_msec'): int,
                                        Optional('hold_sec'): int,
                                        Optional('cfgd_hello_msec'): int,
                                        Optional('cfgd_hold_msec'): int,
                                        Optional('next_hello_sent'): float,
                                    },
                                    Optional('primary_ipv4_address'): {
                                        'address': str,
                                    },
                                    Optional('secondary_ipv4_addresses'): {
                                        Any(): {
                                            'address': str,
                                        }
                                    },
                                    Optional('link_local_ipv6_address'): {
                                        Optional('address'): str,
                                        Optional('auto_configure'): str,
                                    },
                                    Optional('global_ipv6_addresses'): {
                                        Any(): {
                                            'address': str,
                                        }
                                    },
                                    Optional('priority'): int,
                                    Optional('preempt'): bool,
                                    Optional('preempt_min_delay'): int,
                                    Optional('preempt_reload_delay'): int,
                                    Optional('preempt_sync_delay'): int,
                                    Optional('statistics'): {
                                        Optional('num_state_changes'): int,
                                    },
                                    Optional('active_router_priority'): int,
                                    Optional('active_ip_address'): str,
                                    Optional('active_ipv6_address'): str,
                                    Optional('active_expires_in'): float,
                                    Optional('default_priority'): int,
                                    Optional('configured_priority'): int,
                                    Optional('session_name'): str,
                                    Optional('active_mac_address'): str,
                                    Optional('active_mac_in_use'): bool,
                                    Optional('local_virtual_mac_address'): str,
                                    Optional('local_virtual_mac_default'): str,
                                    Optional('active_router'): str,
                                    Optional('standby_router'): str,
                                    Optional('standby_ip_address'): str,
                                    Optional('standby_ipv6_address'): str,
                                    Optional('virtual_mac_address_mac_in_use'): bool,
                                    Optional('local_virtual_mac_address_conf'): str,
                                    Optional('virtual_mac_address'): str,
                                    Optional('slave_group_number'): int,
                                    Optional('standby_priority'): int,
                                    Optional('standby_expires_in'): float,
                                }
                            }
                        }
                    }
                }
            }
        }   
    }

class ShowStandbyAll(ShowStandbyAllSchema):
    """Parser for show standby all
    parser class - implements detail parsing mechanisms for cli,yang output.
    """
    # *************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def cli(self):
        """Cli result for show standby all """
        cmd = 'show standby all'.format()
        out = self.device.execute(cmd)
        
        # Init vars
        standby_all_dict = {}
        group_key = {}
        
        for line in out.splitlines():
            line = line.rstrip()

            # Ethernet4/1 - Group 0 (version 2)
            p1 = re.compile(r'\s*(?P<intf>[a-zA-Z0-9\/]+) +\- +Group'
                             ' +(?P<group>[0-9]+)'
                             ' *(?:\(version +(?P<version>[0-9]+)\))?$')
            m = p1.match(line)
            if m:
                num_state_changes = last_state_change = None
                interface = m.groupdict()['intf']
                group_number = int(m.groupdict()['group'])
                if m.groupdict()['version']:
                    version = int(m.groupdict()['version'])
                else:
                    version = 1
                continue

            # State is Active
            # State is Disabled
            # State is Init (protocol not cfgd)
            p2 = re.compile(r'\s*[sS]tate +is +(?P<hsrp_router_state>\S+)'
                '( +\((?P<hsrp_router_state_reason>.+)\))?')
            m = p2.match(line)
            if m:
                hsrp_router_state = m.groupdict()['hsrp_router_state'].lower()
                if m.groupdict()['hsrp_router_state_reason']:
                    hsrp_router_state_reason = \
                        m.groupdict()['hsrp_router_state_reason']
                continue

            # 8 state changes, last state change 1w0d
            p3 = re.compile(r'\s*(?P<num_state_changes>[0-9]+) +state'
                             ' +changes, +last +state +change'
                             ' +(?P<last_state_change>[a-zA-Z0-9]+)$')
            m = p3.match(line)
            if m:
                num_state_changes = int(m.groupdict()['num_state_changes'])
                last_state_change = m.groupdict()['last_state_change']
                continue

            # Virtual IP address is 192.168.1.254
            # Virtual IP address is unknown
            # Link-Local Virtual IPv6 address is FE80::5:73FF:FEA0:14 (conf auto EUI64)
            # Link-Local Virtual IPv6 address is FE80::5:73FF:FEA0:A (impl auto EUI64)
            # Virtual IPv6 address 2001:DB8:10:1:1::254/64
            p5 = re.compile(r'\s*(?P<v6_type>\S+)? *Virtual +'
                '(?P<address_family>\S+) +address( +is)? +(?P<vip>\S+) ?'
                '(\((?P<vip_conf>.*)\))?$')
            m = p5.match(line)
            if m:
                if m.groupdict()['v6_type']:
                    v6_type = m.groupdict()['v6_type'].lower()
                address_family = m.groupdict()['address_family'].lower()
                if address_family == 'ip':
                    address_family = 'ipv4'
                vip = m.groupdict()['vip'].lower()
                if m.groupdict()['vip_conf']:
                    vip_conf = m.groupdict()['vip_conf'].lower()

                # create base hierarchy.
                if interface not in standby_all_dict:
                    standby_all_dict[interface] = {}
                    standby_all_dict[interface]['redirects_disable'] = False
                    standby_all_dict[interface]['interface'] = interface
                if 'address_family' not in standby_all_dict[interface]:
                    standby_all_dict[interface]['address_family'] = {}
                if address_family not in standby_all_dict[interface]\
                    ['address_family']:
                    standby_all_dict[interface]['address_family']\
                        [address_family] = {}
                if 'version' not in standby_all_dict[interface]\
                    ['address_family'][address_family]:
                    standby_all_dict[interface]['address_family']\
                        [address_family]['version'] = {}
                if version not in standby_all_dict[interface]\
                    ['address_family'][address_family]['version']:
                    standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version] = {}
                if 'groups' not in standby_all_dict[interface]\
                    ['address_family'][address_family]['version'][version]:
                    standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version]['groups'] = {}
                if group_number not in standby_all_dict[interface]\
                    ['address_family'][address_family]['version']\
                    [version]['groups']:
                    standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version]['groups']\
                        [group_number] = {}
                    group_key = {}

                # create hierarchy under group
                group_key['group_number'] = group_number

                if hsrp_router_state:
                    group_key['hsrp_router_state'] = hsrp_router_state
                if 'hsrp_router_state_reason' in locals():
                    group_key['hsrp_router_state_reason'] = \
                        hsrp_router_state_reason
                if num_state_changes:
                    if 'statistics' not in group_key:
                        group_key['statistics'] = {}
                    group_key['statistics']['num_state_changes'] = \
                        num_state_changes
                if last_state_change:
                    group_key['last_state_change'] = last_state_change

                if vip:
                    if ':' not in vip:
                        if 'primary_ipv4_address' not in group_key:
                            group_key['primary_ipv4_address'] = {}
                        group_key['primary_ipv4_address']['address'] = vip
                    else:
                        if 'fe80' in vip:
                            if 'link_local_ipv6_address' not in group_key:
                                group_key['link_local_ipv6_address'] = {}
                            group_key['link_local_ipv6_address']['address'] = \
                                vip
                            if 'conf auto eui64' in vip_conf:
                                group_key['link_local_ipv6_address']\
                                    ['auto_configure'] = 'auto'
                        else:
                            if 'global_ipv6_addresses' not in group_key:
                                group_key['global_ipv6_addresses'] = {}
                            if vip not in group_key['global_ipv6_addresses']:
                                group_key['global_ipv6_addresses'][vip] = {}
                            group_key['global_ipv6_addresses'][vip]\
                                ['address'] = vip

                continue

            # Secondary virtual IP address 10.1.1.253
            p4 = re.compile(r'\s*[sS]econdary +virtual +IP +address +'
                '(?P<secondary_ipv4_address>\S+)$')
            m = p4.match(line)
            if m:
                if 'secondary_ipv4_addresses' not in group_key:
                    group_key['secondary_ipv4_addresses'] = {}
                secondary_ipv4_address = m.groupdict()['secondary_ipv4_address']
                if secondary_ipv4_address not in group_key:
                    group_key['secondary_ipv4_addresses']\
                        [secondary_ipv4_address] = {}
                group_key['secondary_ipv4_addresses'][secondary_ipv4_address]\
                    ['address'] = secondary_ipv4_address

            # Track object 1 (unknown)
            p4 = re.compile(r'\s*Track +object +(?P<tracked_object>[0-9]+)'
                             ' +\((?P<tracked_status>\S+)\)$')
            m = p4.match(line)
            if m:
                tracked_object = int(m.groupdict()['tracked_object'])
                if 'tracked_objects' not in group_key:
                    group_key['tracked_objects'] = {}
                if tracked_object not in group_key['tracked_objects']:
                    group_key['tracked_objects'][tracked_object] = {}
                group_key['tracked_objects'][tracked_object]['object_name'] \
                    = tracked_object
                continue

            # Active virtual MAC address is 0000.0c9f.f000 (MAC In Use)
            # Active virtual MAC address is unknown (MAC Not In Use)
            p6 = re.compile(r'\s*Active +virtual +MAC +address +is'
                             ' +(?P<virtual_mac_address>[a-zA-Z0-9\.]+)'
                             ' +\((?P<virtual_mac_address_mac_in_use>'
                             '[a-zA-Z\s]+)\)$')
            m = p6.match(line)
            if m:
                group_key['virtual_mac_address'] = m.groupdict()\
                    ['virtual_mac_address'].lower()
                if "MAC In Use" in m.groupdict()\
                    ['virtual_mac_address_mac_in_use']:
                    group_key['virtual_mac_address_mac_in_use'] = True
                else:
                    group_key['virtual_mac_address_mac_in_use'] = False
                continue

            # Local virtual MAC address is 0000.0c9f.f000 (v2 default)
            # Local virtual MAC address is 5254.00a7.0818 (bia)
            # Local virtual MAC address is aaaa.aaaa.aaaa (cfgd)
            p7 = re.compile(r'\s*Local +virtual +MAC +address +is'
                             ' +(?P<local_virtual_mac_address>[a-zA-Z0-9\.]+)'
                             ' +\((?P<local_virtual_mac_address_conf>'
                             '[a-zA-Z0-9\s]+)\)$')
            m = p7.match(line)
            if m:
                group_key['local_virtual_mac_address'] \
                    = m.groupdict()['local_virtual_mac_address']
                local_virtual_mac_address_conf \
                    = m.groupdict()['local_virtual_mac_address_conf']
                group_key['local_virtual_mac_address_conf'] \
                    = local_virtual_mac_address_conf
                if 'bia' in local_virtual_mac_address_conf:
                    standby_all_dict[interface]['use_bia'] = True
                else:
                    standby_all_dict[interface]['use_bia'] = False
                continue

            # Hellotime 1 sec, holdtime 3 sec
            # Hello time 3 sec, hold time 10 sec
            # Hello time 999 msec, hold time 10 sec
            # Hello time 999 msec, hold time 2999 msec
            # Hello time 9 sec (cfgd 999 msec), hold time 27 sec (cfgd 2999 msec)
            p8 = re.compile(r'\s*Hello ?time +(?P<hellotime>[0-9]+) '
                '(?P<hello_unit>\S+)( \(cfgd (?P<cfgd_hello_msec>\d)+ msec\))?'
                ', +hold ?time +(?P<holdtime>[0-9]+) +(?P<hold_unit>\S+)'
                '( \(cfgd (?P<cfgd_hold_msec>\d+) msec\))?$')
            m = p8.match(line)
            if m:
                if 'timers' not in group_key:
                    group_key['timers'] = {}
                hellotime = int(m.groupdict()['hellotime'])
                holdtime = int(m.groupdict()['holdtime'])
                if 'msec' in m.groupdict()['hello_unit']:
                    group_key['timers']['hello_msec_flag'] = True
                    group_key['timers']['hello_msec'] = hellotime
                else:
                    group_key['timers']['hello_msec_flag'] = False
                    group_key['timers']['hello_sec'] = hellotime
                if 'msec' in m.groupdict()['hold_unit']:
                    group_key['timers']['hold_msec_flag'] = True
                    group_key['timers']['hold_msec'] = holdtime
                else:
                    group_key['timers']['hold_msec_flag'] = False
                    group_key['timers']['hold_sec'] = holdtime
                if m.groupdict()['cfgd_hello_msec']:
                    group_key['timers']['cfgd_hello_msec'] \
                        = int(m.groupdict()['cfgd_hello_msec'])
                if m.groupdict()['cfgd_hold_msec']:
                    group_key['timers']['cfgd_hold_msec'] \
                        = int(m.groupdict()['cfgd_hold_msec'])
                continue

            # Next hello sent in 2.848 secs
            p9 = re.compile(r'\s*Next +hello +sent +in'
                             ' +(?P<next_hello_sent>[0-9\.]+) secs$')
            m = p9.match(line)
            if m:
                group_key['timers']['next_hello_sent'] = \
                    float(m.groupdict()['next_hello_sent'])
                continue

            # Authentication MD5, key-string "cisco123"
            # Authentication MD5, key-chain "cisco123"
            # Authentication text "cisco123"
            # Authentication "cisco123"
            # Authentication text, string "cisco123"
            p10 = re.compile(r'\s*[aA]uthentication +(?P<authentication_type>'
                '[a-zA-Z0-9]+)?(, +)?(key-string|key-chain|string)?( +)?'
                '\"(?P<authentication>\S+)\"$')
            m = p10.match(line)
            if m:
                group_key['authentication'] = m.groupdict()['authentication']
                group_key['authentication_type'] \
                    = m.groupdict()['authentication_type']
                continue

            # MAC refresh 222 secs (next refresh 0 secs)
            p10 = re.compile(r'\s*MAC refresh (?P<mac_refresh>\d+) secs '
                '\(next refresh (?P<mac_next_refresh>\d+) secs\)$')
            m = p10.match(line)
            if m:
                if m.groupdict()['mac_refresh']:
                    standby_all_dict[interface]['mac_refresh'] \
                        = int(m.groupdict()['mac_refresh'])
                if m.groupdict()['mac_next_refresh']:
                    standby_all_dict[interface]['mac_next_refresh'] \
                        = int(m.groupdict()['mac_next_refresh'])
                continue

            # Preemption enabled, delay min 5 secs, reload 10 secs, sync 20 secs
            # Preemption enabled
            p11 = re.compile(r'\s*Preemption +(?P<preempt>[a-zA-Z]+)(?:, +delay'
                              ' +min +(?P<preempt_min_delay>[0-9]+) +secs,)?'
                              '(?: +reload +(?P<preempt_reload_delay>[0-9]+)'
                              ' +secs,)?(?: +sync'
                              ' +(?P<preempt_sync_delay>[0-9]+) +secs)?$')
            m = p11.match(line)
            if m:
                if m.groupdict()['preempt'] is not None:
                    group_key['preempt'] = True
                if m.groupdict()['preempt_min_delay'] is not None:
                    group_key['preempt_min_delay'] = \
                        int(m.groupdict()['preempt_min_delay'])
                if m.groupdict()['preempt_reload_delay'] is not None:
                    group_key['preempt_reload_delay'] = \
                        int(m.groupdict()['preempt_reload_delay'])
                if m.groupdict()['preempt_sync_delay'] is not None:
                    group_key['preempt_sync_delay'] = \
                        int(m.groupdict()['preempt_sync_delay'])
                continue

            # Active router is unknown
            p12 = re.compile(r'\s*Active +router +is'
                              ' +(?P<active_router>[a-zA-Z\s]+)$')
            m = p12.match(line)
            if m:
                group_key['active_router'] = m.groupdict()['active_router']
                continue

            # Active router is 10.1.2.1, priority 120 (expires in 0.816 sec)
            p12_1 = re.compile(r'\s*Active +router +is'
                              ' +(?P<active_router>\S+),'
                              ' +priority +(?P<ar_priority>[0-9]+)'
                              ' +\(expires in (?P<active_expires_in>'
                              '[a-zA-Z0-9\.\s]+) sec\)$')
            m = p12_1.match(line)
            if m:
                active_router = m.groupdict()['active_router']
                group_key['active_router'] = active_router
                if 'local' not in active_router:
                    if ':' not in active_router:
                        group_key['active_ip_address'] = active_router
                    else:
                        group_key['active_ipv6_address'] = active_router
                group_key['active_router_priority'] = \
                    int(m.groupdict()['ar_priority'])
                if m.groupdict()['active_expires_in']:
                    group_key['active_expires_in'] = \
                        float(m.groupdict()['active_expires_in'])
                continue

            # Standby router is unknown 
            # Standby router is 10.1.1.2, priority 100 (expires in 10.624 sec)
            p13 = re.compile(r'\s*Standby +router +is +(?P<standby_router>'
                              '[a-zA-Z0-9\.]+)(, +priority +'
                              '(?P<standby_priority>\d+) +\(expires +in +'
                              '(?P<standby_expires_in>\S+) +sec\))?')
            m = p13.match(line)
            if m:
                standby_router = m.groupdict()['standby_router']
                if m.groupdict()['standby_priority']:
                    group_key['standby_priority'] \
                        = int(m.groupdict()['standby_priority'])
                if m.groupdict()['standby_expires_in']:
                    group_key['standby_expires_in'] \
                        = float(m.groupdict()['standby_expires_in'])
                group_key['standby_router'] = standby_router
                if 'local' not in standby_router:
                    if ':' not in standby_router:
                        group_key['standby_ip_address'] = standby_router
                    else:
                        group_key['standby_ipv6_address'] = standby_router
                continue

            # Priority 100 (default 100)
            p14 = re.compile(r'\s*Priority +(?P<priority>[0-9]+)'
                              ' +\(default +(?P<default_priority>[0-9]+)\)$')
            m = p14.match(line)
            if m:
                group_key['priority'] = int(m.groupdict()['priority'])
                group_key['default_priority'] = \
                    int(m.groupdict()['default_priority'])
                continue

            # Priority 100 (configured 100)
            p15 = re.compile(r'\s*Priority +(?P<priority>[0-9]+)'
                              ' +\(configured'
                              ' +(?P<configured_priority>[0-9]+)\)$')
            m = p15.match(line)
            if m:
                group_key['priority'] = int(m.groupdict()['priority'])
                group_key['configured_priority'] = \
                    int(m.groupdict()['configured_priority'])
                if 'follow' in group_key:
                    if 'slave_groups' not in standby_all_dict[interface]\
                        ['address_family'][address_family]['version'][version]:
                        standby_all_dict[interface]['address_family']\
                            [address_family]['version'][version]\
                            ['slave_groups'] = {}
                    if group_key['group_number'] not in standby_all_dict\
                        [interface]['address_family'][address_family]\
                        ['version'][version]['slave_groups']:
                        standby_all_dict[interface]['address_family']\
                            [address_family]['version'][version]\
                            ['slave_groups'][group_key['group_number']] = {}
                    standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version]['slave_groups']\
                        [group_key['group_number']] = group_key
                    standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version]['slave_groups']\
                        [group_key['group_number']]['slave_group_number'] \
                        = group_key['group_number']
                    if standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version]['groups']\
                        [group_key['group_number']]:
                        del standby_all_dict[interface]['address_family']\
                            [address_family]['version'][version]['groups']\
                            [group_key['group_number']]
                else:
                    standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version]['groups']\
                        [group_number] = group_key
                continue

            # Group name is "hsrp-Gi1/0/1-0" (default)
            p16 = re.compile(r'\s*Group +name +is'
                              ' +\"(?P<session_name>[a-zA-Z0-9\/\-]+)\"'
                              ' +\(default\)$')
            m = p16.match(line)
            if m:
                group_key['session_name'] = m.groupdict()['session_name']
                if 'follow' in group_key:
                    if 'slave_groups' not in standby_all_dict[interface]\
                        ['address_family'][address_family]['version'][version]:
                        standby_all_dict[interface]['address_family']\
                            [address_family]['version'][version]\
                            ['slave_groups'] = {}
                    if group_key['group_number'] not in standby_all_dict\
                        [interface]['address_family'][address_family]\
                        ['version'][version]['slave_groups']:
                        standby_all_dict[interface]['address_family']\
                            [address_family]['version'][version]\
                            ['slave_groups'][group_key['group_number']] = {}
                    standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version]['slave_groups']\
                        [group_key['group_number']] = group_key
                    standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version]['slave_groups']\
                        [group_key['group_number']]['slave_group_number'] \
                        = group_key['group_number']
                    if standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version]['groups']\
                        [group_key['group_number']]:
                        del standby_all_dict[interface]['address_family']\
                            [address_family]['version'][version]['groups']\
                            [group_key['group_number']]
                else:
                    standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version]['groups']\
                        [group_number] = group_key
                continue
            
            # Group name is "gandalf" (cfgd)
            p16 = re.compile(r'\s*Group +name +is'
                              ' +\"(?P<session_name>[a-zA-Z0-9\/\-]+)\"'
                              ' +\(cfgd\)$')
            m = p16.match(line)
            if m:
                group_key['session_name'] = \
                    m.groupdict()['session_name']
                if 'follow' in group_key:
                    if 'slave_groups' not in standby_all_dict[interface]\
                        ['address_family'][address_family]['version'][version]:
                        standby_all_dict[interface]['address_family']\
                            [address_family]['version'][version]\
                            ['slave_groups'] = {}
                    if group_key['group_number'] not in standby_all_dict\
                        [interface]['address_family'][address_family]\
                        ['version'][version]['slave_groups']:
                        standby_all_dict[interface]['address_family']\
                            [address_family]['version'][version]\
                            ['slave_groups'][group_key['group_number']] = {}
                    standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version]['slave_groups']\
                        [group_key['group_number']] = group_key
                    standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version]['slave_groups']\
                        [group_key['group_number']]['slave_group_number'] \
                        = group_key['group_number']
                    if standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version]['groups']\
                        [group_key['group_number']]:
                        del standby_all_dict[interface]['address_family']\
                            [address_family]['version'][version]['groups']\
                            [group_key['group_number']]
                else:
                    standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version]['groups']\
                        [group_number] = group_key
                continue

            # Following "group10"
            p17 = re.compile(r'\s*[fF]ollowing +\"(?P<follow>\S+)\"$')
            m = p17.match(line)
            if m:
                group_key['follow'] = m.groupdict()['follow']
                if 'follow' in group_key:
                    if 'slave_groups' not in standby_all_dict[interface]\
                        ['address_family'][address_family]['version'][version]:
                        standby_all_dict[interface]['address_family']\
                            [address_family]['version'][version]\
                            ['slave_groups'] = {}
                    if group_key['group_number'] not in standby_all_dict\
                        [interface]['address_family'][address_family]\
                        ['version'][version]['slave_groups']:
                        standby_all_dict[interface]['address_family']\
                            [address_family]['version'][version]\
                            ['slave_groups'][group_key['group_number']] = {}
                    standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version]['slave_groups']\
                        [group_key['group_number']] = group_key
                    standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version]['slave_groups']\
                        [group_key['group_number']]['slave_group_number'] \
                        = group_key['group_number']
                    if standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version]['groups']\
                        [group_key['group_number']]:
                        del standby_all_dict[interface]['address_family']\
                            [address_family]['version'][version]['groups']\
                            [group_key['group_number']]
                else:
                    standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version]['groups']\
                        [group_number] = group_key
                continue            

            # HSRP ICMP redirects disabled
            p17 = re.compile(r'HSRP ICMP redirects disabled')
            m = p17.match(line)
            if m:
                standby_all_dict[interface]['redirects_disable'] = True
                if 'follow' in group_key:
                    if 'slave_groups' not in standby_all_dict[interface]\
                        ['address_family'][address_family]['version'][version]:
                        standby_all_dict[interface]['address_family']\
                            [address_family]['version'][version]\
                            ['slave_groups'] = {}
                    if group_key['group_number'] not in standby_all_dict\
                        [interface]['address_family'][address_family]\
                        ['version'][version]['slave_groups']:
                        standby_all_dict[interface]['address_family']\
                            [address_family]['version'][version]\
                            ['slave_groups'][group_key['group_number']] = {}
                    standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version]['slave_groups']\
                        [group_key['group_number']] = group_key
                    standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version]['slave_groups']\
                        [group_key['group_number']]['slave_group_number'] \
                        = group_key['group_number']
                    if standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version]['groups']\
                        [group_key['group_number']]:
                        del standby_all_dict[interface]['address_family']\
                            [address_family]['version'][version]['groups']\
                            [group_key['group_number']]
                else:
                    standby_all_dict[interface]['address_family']\
                        [address_family]['version'][version]['groups']\
                        [group_number] = group_key
                continue

        return standby_all_dict


    def yang(self):
        """Yang result for show standby all"""
        ret = {}
        cmd = '''<native><interface><GigabitEthernet/></interface></native>'''
        output = self.device.get(('subtree', cmd))

        for data in output.data:
            for native in data:
                for interface in native:
                    gig_number = None
                    interface_name = None
                    for gigabitethernet in interface:
                        # Remove the namespace
                        text = gigabitethernet.tag\
                            [gigabitethernet.tag.find('}')+1:]
                        if text == 'name':
                            gig_number = gigabitethernet.text
                            interface_name = 'Gigabitethernet' + str(gig_number)
                            continue

# ======================================
#   Schema for 'show standby delay'
# ======================================

class ShowStandbyDelaySchema(MetaParser):
    """Schema for show standby delay"""
    schema = {
                Any(): {
                    'delay': {
                        'minimum_delay': int,
                        'reload_delay': int,
                    }
                }
             }

class ShowStandbyDelay(ShowStandbyDelaySchema):
    """Parser for show standby delay"""
    def cli(self):
        cmd = 'show standby delay'
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
