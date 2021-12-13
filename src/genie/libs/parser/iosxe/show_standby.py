"""show_standby.py

IOSXE parsers for show commands:
    * 'show standby all'
    * 'show standby internal'
    * 'show standby brief'
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ======================================
#   Schema for 'show standby internal'
# ======================================
class ShowStandbyInternalSchema(MetaParser):
    """Schema for show standby internal"""

    schema = {
        'hsrp_common_process_state': str,
        Optional('msgQ_size'): int,
        Optional('msgQ_max_size'): int,
        'hsrp_ipv4_process_state': str,
        'hsrp_ipv6_process_state': str,
        'hsrp_timer_wheel_state': str,
        Optional('hsrp_ha_state'): str,
        Optional('v3_to_v4_transform'): str,
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


# ======================================
#   Parser for 'show standby internal'
# ======================================
class ShowStandbyInternal(ShowStandbyInternalSchema):
    """Parser for show standby internal"""

    cli_command = 'show standby internal'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        # Init vars
        standby_internal_dict = {}
        
        # HSRP common process running
        p1 = re.compile(r'HSRP +common +process'
                        r' +(?P<hsrp_common_process_state>[a-zA-Z\s]+)$')

        # MsgQ size 0, max 2
        p2 = re.compile(r'MsgQ +size +(?P<msgQ_size>\d+),'
                        r' +max +(?P<msgQ_max_size>\d+)$')

        # HSRP IPv4 process running
        p3 = re.compile(r'HSRP +IPv4 +process'
                        r' +(?P<hsrp_ipv4_process_state>[a-zA-Z\s]+)$')

        # HSRP IPv6 process not running
        p4 = re.compile(r'HSRP +IPv6 +process'
                        r' +(?P<hsrp_ipv6_process_state>[a-zA-Z\s]+)$')

        # HSRP Timer wheel running
        p5 = re.compile(r'HSRP +Timer +wheel'
                        r' +(?P<hsrp_timer_wheel_state>[a-zA-Z\s]+)$')

        # HSRP HA capable, v3 to v4 transform disabled
        p6 = re.compile(r'HSRP +HA +(?P<hsrp_ha_state>[a-zA-Z\s]+),'
                        r' +v3 +to +v4 +transform'
                        r' +(?P<v3_to_v4_transform>[a-zA-Z\s]+)$')

        # HSRP virtual IP Hash Table (global)
        # 103 192.168.1.254                    Gi1/0/1    Grp 0
        # HSRP virtual IPv6 Hash Table (global)
        # 78  2001:DB8:10:1:1::254             Gi1        Grp 20
        p7 = re.compile(r'(?P<hsrp>\d+) +(?P<ip>[\w\.\:]+)'
                        r' +(?P<interface>[\w\/]+) +Grp +(?P<group>\d+)$')

        # HSRP MAC Address Table
        # 240 Gi1/0/1 0000.0cff.909f
        p8 = re.compile(r'(?P<hsrp_number>\d+)'
                        r' +(?P<interface>[\w\/]+)'
                        r' +(?P<mac_address>[\w\.]+)$')

        # HSRP MAC Address Table
        # Gi1/0/1 Grp 0
        p8_1 = re.compile(r'(?P<interface>[\w\/]+) +Grp +(?P<group>\d+)$')


        for line in out.splitlines():
            line = line.strip()

            # HSRP common process running
            m = p1.match(line)
            if m:
                stby_internal = standby_internal_dict
                stby_internal['hsrp_common_process_state'] = \
                    m.groupdict()['hsrp_common_process_state']

            # MsgQ size 0, max 2
            m = p2.match(line)
            if m:
                stby_internal['msgQ_size'] = int(m.groupdict()['msgQ_size'])
                stby_internal['msgQ_max_size'] = \
                    int(m.groupdict()['msgQ_max_size'])
                continue

            # HSRP IPv4 process running
            m = p3.match(line)
            if m:
                stby_internal['hsrp_ipv4_process_state'] = \
                    m.groupdict()['hsrp_ipv4_process_state']
                continue

            # HSRP IPv6 process not running
            m = p4.match(line)
            if m:
                stby_internal['hsrp_ipv6_process_state'] = \
                    m.groupdict()['hsrp_ipv6_process_state']
                continue

            # HSRP Timer wheel running
            m = p5.match(line)
            if m:
                stby_internal['hsrp_timer_wheel_state'] = \
                    m.groupdict()['hsrp_timer_wheel_state']
                continue

            # HSRP HA capable, v3 to v4 transform disabled
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
            # 240 Gi1/0/1 0000.0cff.909f
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

    schema = {
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


# ======================================
#   Parser for 'show standby all'
# ======================================
class ShowStandbyAll(ShowStandbyAllSchema):
    """Parser for show standby all"""

    cli_command = 'show standby all'

    exclude = ['next_hello_sent', 'last_state_change', 'standby_expires_in',
               'statistics', 'num_state_changes', 'active_expires_in']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        standby_all_dict = {}

        # Ethernet4/1 - Group 0 (version 2)
        p1 = re.compile(r'(?P<intf>[\w\/\.\-]+) +\- +Group +(?P<group>\d+)'
                        r' *(?:\(version +(?P<version>\d+)\))?$')

        # State is Active
        # State is Disabled
        # State is Init (protocol not cfgd)
        p2 = re.compile(r'[sS]tate +is +(?P<hsrp_router_state>\S+)'
                        r'( +\((?P<hsrp_router_state_reason>.+)\))?')

        # 8 state changes, last state change 1w0d
        p3 = re.compile(r'(?P<num_state_changes>\d+) +state'
                        r' +changes, +last +state +change'
                        r' +(?P<last_state_change>\w+)$')

        # Virtual IP address is 192.168.1.254
        # Virtual IP address is unknown
        # Link-Local Virtual IPv6 address is FE80::5:73FF:FEA0:14 (conf auto EUI64)
        # Link-Local Virtual IPv6 address is FE80::5:73FF:FEA0:A (impl auto EUI64)
        # Virtual IPv6 address 2001:DB8:10:1:1::254/64
        p4 = re.compile(r'(?P<v6_type>\S+)? *Virtual +(?P<address_family>\S+) '
                        r'+address( +is)? +(?P<vip>\S+) ?'
                        r'(\((?P<vip_conf>.*)\))?$')

        # Secondary virtual IP address 10.1.1.253
        p5 = re.compile(r'[sS]econdary +virtual +IP +address +'
                        r'(?P<secondary_ipv4_address>\S+)$')

        # Track object 1 (unknown)
        p6 = re.compile(r'Track +object +(?P<tracked_object>\d+)'
                        r' +\((?P<tracked_status>\S+)\)$')

        # Active virtual MAC address is 0000.0cff.909f (MAC In Use)
        # Active virtual MAC address is unknown (MAC Not In Use)
        p7 = re.compile(r'Active +virtual +MAC +address +is'
                        r' +(?P<virtual_mac_address>[\w\.]+)'
                        r' +\((?P<virtual_mac_address_mac_in_use>'
                        r'[a-zA-Z\s]+)\)$')

        # Local virtual MAC address is 0000.0cff.909f (v2 default)
        # Local virtual MAC address is 5254.00ff.afbf (bia)
        # Local virtual MAC address is aaaa.aaff.5555 (cfgd)
        p8 = re.compile(r'Local +virtual +MAC +address +is'
                        r' +(?P<local_virtual_mac_address>[\w\.]+)'
                        r' +\((?P<local_virtual_mac_address_conf>'
                        r'[\w\s]+)\)$')

        # Hellotime 1 sec, holdtime 3 sec
        # Hello time 3 sec, hold time 10 sec
        # Hello time 999 msec, hold time 10 sec
        # Hello time 999 msec, hold time 2999 msec
        # Hello time 9 sec (cfgd 999 msec), hold time 27 sec (cfgd 2999 msec)
        p9 = re.compile(r'Hello ?time +(?P<hellotime>\d+) (?P<hello_unit>\S+)'
                        r'( \(cfgd (?P<cfgd_hello_msec>\d)+ msec\))?, +hold '
                        r'?time +(?P<holdtime>\d+) +(?P<hold_unit>\S+)'
                        r'( \(cfgd (?P<cfgd_hold_msec>\d+) msec\))?$')

        # Next hello sent in 2.848 secs
        p10 = re.compile(r'Next +hello +sent +in'
                         r' +(?P<next_hello_sent>[\d\.]+) secs$')

        # Authentication MD5, key-string "cisco123"
        # Authentication MD5, key-chain "cisco123"
        # Authentication MD5, key-string
        # Authentication text "cisco123"
        # Authentication "cisco123"
        # Authentication text, string "cisco123"
        p11 = re.compile(r'[aA]uthentication +(?P<authentication_type>\w+)?'
                         r'(, +)?(key-string|key-chain|string)?( +)?'
                         r'(\"(?P<authentication>\S+)\")?$')

        # MAC refresh 222 secs (next refresh 0 secs)
        p12 = re.compile(r'MAC refresh (?P<mac_refresh>\d+) secs '
                         r'\(next refresh (?P<mac_next_refresh>\d+) secs\)$')

        # Preemption enabled, delay min 5 secs, reload 10 secs, sync 20 secs
        # Preemption enabled
        p13 = re.compile(r'Preemption +(?P<preempt>[a-zA-Z]+)(?:, +delay +min '
                         r'+(?P<preempt_min_delay>\d+) +secs,)?'
                         r'(?: +reload +(?P<preempt_reload_delay>\d+)'
                         r' +secs,)?(?: +sync'
                         r' +(?P<preempt_sync_delay>\d+) +secs)?$')

        # Active router is unknown
        p14 = re.compile(r'Active +router +is'
                         r' +(?P<active_router>[a-zA-Z\s]+)$')

        # Active router is 10.1.2.1, priority 120 (expires in 0.816 sec)
        p15 = re.compile(r'Active +router +is +(?P<active_router>\S+),'
                         r' +priority +(?P<ar_priority>\d+)'
                         r' +\(expires in (?P<active_expires_in>'
                         r'[\w\.]+) sec\)$')

        # Standby router is unknown
        # Standby router is 10.1.1.2, priority 100 (expires in 10.624 sec)
        p16 = re.compile(r'Standby +router +is +(?P<standby_router>[\w\.]+)'
                         r'(, +priority +(?P<standby_priority>\d+) +\(expires '
                         r'+in +(?P<standby_expires_in>\S+) +sec\))?')

        # Priority 100 (default 100)
        p17 = re.compile(r'Priority +(?P<priority>\d+)'
                         r' +\(default +(?P<default_priority>\d+)\)$')

        # Priority 100 (configured 100)
        p18 = re.compile(r'Priority +(?P<priority>\d+) +\(configured'
                         r' +(?P<configured_priority>\d+)\)$')

        # Group name is "hsrp-Gi1/0/1-0" (default)
        # Group name is "gandalf" (cfgd)
        # Group name is "hsrp-Gi4/10.103-100" (default)
        p19 = re.compile(r'Group +name +is +\"(?P<session_name>[\w\/\-\.]+)\"'
                         r' +(?:\(default\)|\(cfgd\))$')

        # Following "group10"
        p20 = re.compile(r'[fF]ollowing +\"(?P<follow>\S+)\"$')

        # HSRP ICMP redirects disabled
        p21 = re.compile(r'HSRP ICMP redirects disabled')

        for line in out.splitlines():
            line = line.strip()

            # Ethernet4/1 - Group 0 (version 2)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group['intf']
                group_number = int(group['group'])
                if group['version']:
                    version = int(group['version'])
                else:
                    version = 1

                interface_dict = standby_all_dict.setdefault(interface, {})
                interface_dict['interface'] = interface
                group_number_dict = {'group_number': group_number}
                continue

            # State is Active
            # State is Disabled
            # State is Init (protocol not cfgd)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                group_number_dict['hsrp_router_state'] = \
                    group['hsrp_router_state'].lower()
                if group['hsrp_router_state_reason']:
                    group_number_dict['hsrp_router_state_reason'] = \
                        group['hsrp_router_state_reason']
                continue

            # 8 state changes, last state change 1w0d
            m = p3.match(line)
            if m:
                group = m.groupdict()
                statistics_dict = group_number_dict.\
                    setdefault('statistics', {})
                statistics_dict['num_state_changes'] = \
                    int(group['num_state_changes'])
                group_number_dict['last_state_change'] = \
                    group['last_state_change']
                continue

            # Virtual IP address is 192.168.1.254
            # Virtual IP address is unknown
            # Link-Local Virtual IPv6 address is FE80::5:73FF:FEA0:14 (conf auto EUI64)
            # Link-Local Virtual IPv6 address is FE80::5:73FF:FEA0:A (impl auto EUI64)
            # Virtual IPv6 address 2001:DB8:10:1:1::254/64
            m = p4.match(line)
            if m:
                group = m.groupdict()

                if group['v6_type']:
                    v6_type = group['v6_type'].lower()

                address_family = group['address_family'].lower()

                if address_family == 'ip':
                    address_family = 'ipv4'

                vip = group['vip'].lower()

                if group['vip_conf']:
                    vip_conf = group['vip_conf'].lower()

                # create base hierarchy
                interface_dict['redirects_disable'] = False
                addr_families_dict = interface_dict.setdefault(
                    'address_family', {})
                addr_family_dict = addr_families_dict.setdefault(
                    address_family, {})
                versions_dict = addr_family_dict.setdefault('version', {})
                version_dict = versions_dict.setdefault(version, {})

                groups_dict = version_dict.setdefault('groups', {})
                groups_dict[group_number] = group_number_dict

                if vip:
                    if ':' not in vip:
                        prim_ipv4_addr_dict = group_number_dict.setdefault(
                            'primary_ipv4_address', {})
                        prim_ipv4_addr_dict['address'] = vip
                    else:
                        if 'fe80' in vip:
                            link_local_ipv6_addr_dict = \
                                group_number_dict.setdefault(
                                    'link_local_ipv6_address', {})
                            link_local_ipv6_addr_dict['address'] = vip
                            if 'conf auto eui64' in vip_conf:
                                link_local_ipv6_addr_dict['auto_configure'] = \
                                    'auto'
                        else:
                            global_ipv6_addrs_dict = group_number_dict.\
                                setdefault('global_ipv6_addresses', {})
                            vip_dict = global_ipv6_addrs_dict.\
                                setdefault(vip, {})
                            vip_dict['address'] = vip
                continue

            # Secondary virtual IP address 10.1.1.253
            m = p5.match(line)
            if m:
                group = m.groupdict()
                secondary_ipv4_address = group['secondary_ipv4_address']
                sec_ipv4_addrs_dict = group_number_dict.setdefault(
                    'secondary_ipv4_addresses', {})
                sec_ipv4_addr_dict = sec_ipv4_addrs_dict.setdefault(
                    secondary_ipv4_address, {})
                sec_ipv4_addr_dict['address'] = secondary_ipv4_address
                continue

            # Track object 1 (unknown)
            m = p6.match(line)
            if m:
                tracked_object = int(m.groupdict()['tracked_object'])
                tracked_objects_dict = group_number_dict.setdefault(
                    'tracked_objects', {})
                tracked_object_dict = tracked_objects_dict.setdefault(
                    tracked_object, {})
                tracked_object_dict['object_name'] = tracked_object
                continue

            # Active virtual MAC address is 0000.0cff.909f (MAC In Use)
            # Active virtual MAC address is unknown (MAC Not In Use)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                group_number_dict['virtual_mac_address'] = \
                    group['virtual_mac_address'].lower()
                group_number_dict['virtual_mac_address_mac_in_use'] = \
                    "MAC In Use" in group['virtual_mac_address_mac_in_use']
                continue

            # Local virtual MAC address is 0000.0cff.909f (v2 default)
            # Local virtual MAC address is 5254.00ff.afbf (bia)
            # Local virtual MAC address is aaaa.aaff.5555 (cfgd)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                group_number_dict['local_virtual_mac_address'] \
                    = group['local_virtual_mac_address']
                local_virtual_mac_address_conf \
                    = group['local_virtual_mac_address_conf']
                group_number_dict['local_virtual_mac_address_conf'] \
                    = local_virtual_mac_address_conf
                interface_dict['use_bia'] = \
                    'bia' in local_virtual_mac_address_conf
                continue

            # Hellotime 1 sec, holdtime 3 sec
            # Hello time 3 sec, hold time 10 sec
            # Hello time 999 msec, hold time 10 sec
            # Hello time 999 msec, hold time 2999 msec
            # Hello time 9 sec (cfgd 999 msec), hold time 27 sec (cfgd 2999 msec)
            m = p9.match(line)
            if m:
                group = m.groupdict()
                timers_dict = group_number_dict.setdefault('timers', {})
                hellotime = int(group['hellotime'])
                holdtime = int(group['holdtime'])
                if 'msec' in group['hello_unit']:
                    timers_dict['hello_msec_flag'] = True
                    timers_dict['hello_msec'] = hellotime
                else:
                    timers_dict['hello_msec_flag'] = False
                    timers_dict['hello_sec'] = hellotime
                if 'msec' in group['hold_unit']:
                    timers_dict['hold_msec_flag'] = True
                    timers_dict['hold_msec'] = holdtime
                else:
                    timers_dict['hold_msec_flag'] = False
                    timers_dict['hold_sec'] = holdtime
                if group['cfgd_hello_msec']:
                    timers_dict['cfgd_hello_msec'] \
                        = int(group['cfgd_hello_msec'])
                if group['cfgd_hold_msec']:
                    timers_dict['cfgd_hold_msec'] \
                        = int(group['cfgd_hold_msec'])
                continue

            # Next hello sent in 2.848 secs
            m = p10.match(line)
            if m:
                timers_dict['next_hello_sent'] = \
                    float(m.groupdict()['next_hello_sent'])
                continue

            # Authentication MD5, key-string "cisco123"
            # Authentication MD5, key-chain "cisco123"
            # Authentication MD5, key-string
            # Authentication text "cisco123"
            # Authentication "cisco123"
            # Authentication text, string "cisco123"
            m = p11.match(line)
            if m:
                group = m.groupdict()
                if group['authentication_type']:
                    group_number_dict['authentication_type'] \
                        = group['authentication_type']

                if group['authentication']:
                    group_number_dict['authentication'] \
                        = group['authentication']
                continue

            # MAC refresh 222 secs (next refresh 0 secs)
            m = p12.match(line)
            if m:
                group = m.groupdict()
                if group['mac_refresh']:
                    interface_dict['mac_refresh'] \
                        = int(group['mac_refresh'])
                if group['mac_next_refresh']:
                    interface_dict['mac_next_refresh'] \
                        = int(group['mac_next_refresh'])
                continue

            # Preemption enabled, delay min 5 secs, reload 10 secs, sync 20 secs
            # Preemption enabled
            m = p13.match(line)
            if m:
                group = m.groupdict()
                if group['preempt'] is not None:
                    group_number_dict['preempt'] = True
                if group['preempt_min_delay'] is not None:
                    group_number_dict['preempt_min_delay'] = \
                        int(group['preempt_min_delay'])
                if group['preempt_reload_delay'] is not None:
                    group_number_dict['preempt_reload_delay'] = \
                        int(group['preempt_reload_delay'])
                if group['preempt_sync_delay'] is not None:
                    group_number_dict['preempt_sync_delay'] = \
                        int(group['preempt_sync_delay'])
                continue

            # Active router is unknown
            m = p14.match(line)
            if m:
                group_number_dict['active_router'] = \
                    m.groupdict()['active_router']
                continue

            # Active router is 10.1.2.1, priority 120 (expires in 0.816 sec)
            m = p15.match(line)
            if m:
                group = m.groupdict()
                active_router = group['active_router']
                group_number_dict['active_router'] = active_router
                if 'local' not in active_router:
                    if ':' not in active_router:
                        group_number_dict['active_ip_address'] = active_router
                    else:
                        group_number_dict['active_ipv6_address'] \
                            = active_router
                group_number_dict['active_router_priority'] = \
                    int(group['ar_priority'])
                if group['active_expires_in']:
                    group_number_dict['active_expires_in'] = \
                        float(group['active_expires_in'])
                continue

            # Standby router is unknown
            # Standby router is 10.1.1.2, priority 100 (expires in 10.624 sec)
            m = p16.match(line)
            if m:
                group = m.groupdict()
                standby_router = group['standby_router']
                if group['standby_priority']:
                    group_number_dict['standby_priority'] \
                        = int(group['standby_priority'])
                if group['standby_expires_in']:
                    group_number_dict['standby_expires_in'] \
                        = float(group['standby_expires_in'])
                group_number_dict['standby_router'] = standby_router
                if 'local' not in standby_router:
                    if ':' not in standby_router:
                        group_number_dict['standby_ip_address'] = standby_router
                    else:
                        group_number_dict['standby_ipv6_address'] = standby_router
                continue

            # Priority 100 (default 100)
            m = p17.match(line)
            if m:
                group = m.groupdict()
                group_number_dict['priority'] = int(group['priority'])
                group_number_dict['default_priority'] = \
                    int(group['default_priority'])
                continue

            # Priority 100 (configured 100)
            m = p18.match(line)
            if m:
                group = m.groupdict()
                group_number_dict['priority'] = int(group['priority'])
                group_number_dict['configured_priority'] = \
                    int(group['configured_priority'])
                continue

            # Group name is "hsrp-Gi1/0/1-0" (default)
            # Group name is "gandalf" (cfgd)
            # Group name is "hsrp-Gi4/10.103-100" (default)
            m = p19.match(line)
            if m:
                group_number_dict['session_name'] = m.groupdict()['session_name']
                continue

            # Following "group10"
            m = p20.match(line)
            if m:
                group_number_dict['follow'] = m.groupdict()['follow']
                continue

            # HSRP ICMP redirects disabled
            m = p21.match(line)
            if m:
                interface_dict['redirects_disable'] = True
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


# ======================================
#   Parser for 'show standby delay'
# ======================================
class ShowStandbyDelay(ShowStandbyDelaySchema):
    """Parser for show standby delay"""

    cli_command = 'show standby delay'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        hsrp_delay_dict = {}

        # GigabitEthernet1   99      888
        p1 = re.compile(r'(?P<interface>\S+) +(?P<minimum_delay>\d+) +'
                        r'(?P<reload_delay>\d+)')

        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet1   99      888
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

# =================
# Schema for:
#  * 'show standby brief:'
# =================
class ShowStandbyBriefSchema(MetaParser):
    """Schema for show standby brief:"""
    
    schema = {
        'interface': {
            Any(): {
                'grp': int,
                'priority': int,
                Optional('is_preempt_enabled'): bool,
                'state': str,
                'active': str,
                'standby': str,
                'virtual_ip': str,
            },
        },
    }

# =================
# Parser for:
#  * 'show standby brief:'
# =================
class ShowStandbyBrief(ShowStandbyBriefSchema):
    '''Parser for show standby brief'''
    
    cli_command = 'show standby brief'

    def cli(self, output=None):
       
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}

        #Vl1309      1    110   Active  local           40.1.31.1       40.1.31.100
        #Vl500       20   100 P Active  local           100.1.50.2      100.1.50.254
        p0 = re.compile(r"^(?P<interface>\w+)\s+(?P<grp>\d+)\s+(?P<priority>\d+)\s+((?P<is_preempt_enabled>\S+)\s+)?(?P<state>\w+)\s+(?P<active>\w+)\s+(?P<standby>[\w:.]+)\s+(?P<virtual_ip>[\w:.]+)$")
        
        for line in out.splitlines():
            line = line.strip()
            
            #Vl1309      1    110   Active  local           40.1.31.1       40.1.31.100
            #Vl500       20   100 P Active  local           100.1.50.2      100.1.50.254
            m = p0.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                stby_dict = ret_dict.setdefault('interface', {}).setdefault(interface, {})
                stby_dict['grp']  = int(group['grp'])
                stby_dict['priority']  = int(group['priority'])
                if m.group('is_preempt_enabled'):
                    enable = group['is_preempt_enabled'] == 'P'
                    stby_dict['is_preempt_enabled']  = enable
                stby_dict['state']  = group['state']
                stby_dict['active']  = group['active']
                stby_dict['standby']  = group['standby']
                stby_dict['virtual_ip']  = group['virtual_ip']
                continue
           
        return ret_dict
