''' show_hsrp.py

NXOS parsers for show commands:
    * 'show hsrp summary'
    * 'show hsrp all'
    * 'show hsrp delay'
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional


# ==============================
# Schema for 'show hsrp summary'
# ==============================
class ShowHsrpSummarySchema(MetaParser):
    
    ''' Schema for "'show hsrp summary" '''

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
            'v6_listen': int},
        'intf_total': int,
        'total_packets':{
            'tx_pass': int,
            'tx_fail': int,
            'rx_good': int},
        'pkt_unknown_groups': int,
        'total_mts_rx': int,
        }

# ==============================
# Parser for 'show hsrp summary'
# ==============================
class ShowHsrpSummary(ShowHsrpSummarySchema):
    '''Parser for show hsrp summary '''
    cli_command = 'show hsrp summary'
    exclude = [
        'total_mts_rx',
        'rx_good',
        'tx_pass',
        'pkt_unknown_groups']

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

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


# ===========================
# Schema for 'show hsrp all'
# ===========================
class ShowHsrpAllSchema(MetaParser):

    ''' Schema for 'show hsrp all' '''

    schema = {
        Any():
            {'interface': str,
            'use_bia': bool,
            'address_family':
                {Any():
                    {'version': 
                        {Any():
                            {'groups':
                                {Any():
                                    {'group_number': int,
                                    Optional('tracked_objects'):
                                        {Any():
                                            {Optional('object_name'): int,
                                            Optional('status'): str,
                                            Optional('priority_decrement'): int},
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
                                    Optional('timers'): 
                                        {Optional('hello_msec_flag'): bool,
                                        Optional('hello_msec'): int,
                                        Optional('hello_sec'): int,
                                        Optional('hold_msec_flag'): bool,
                                        Optional('hold_msec'): int,
                                        Optional('hold_sec'): int,
                                        Optional('cfged_hello_unit'): str,
                                        Optional('cfged_hello_interval'): int,
                                        Optional('cfged_hold_unit'): str,
                                        Optional('cfged_hold_interval'): int},
                                    Optional('primary_ipv4_address'): 
                                        {Optional('virtual_ip_learn'): bool,
                                        Optional('address'): str},
                                    Optional('secondary_ipv4_addresses'): 
                                        {Any():
                                            {Optional('address'): str},
                                        },
                                    Optional('link_local_ipv6_address'):
                                        {Optional('address'): str,
                                        Optional('auto_configure'): bool,
                                        },
                                    Optional('global_ipv6_addresses'):
                                        {Any():
                                            {'address': str},
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
                                    Optional('standby_mac_address'): str},
                                },
                            },
                        },
                    },
                },
            },
        }

# ===========================
# Parser for 'show hsrp all'
# ===========================
class ShowHsrpAll(ShowHsrpAllSchema):

    ''' Parser for "'show hsrp all" '''
    cli_command = 'show hsrp all'
    exclude = [
        'last_state_change',
        'standby_expire',
        'num_state_changes',
        'active_expire']

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        parsed_dict = {}
        secondary_vip_exists = False
 
        # Ethernet1/3 - Group 1 (HSRP-V1) (IPv4)
        p1 = re.compile(r'(?P<intf>(\S+)) +\- +Group +(?P<gnum>[0-9]+)'
                        ' +\(HSRP-V(?P<version>[0-9]+)\)'
                        ' +\((?P<af>(\S+))\)$')

        # Local state is Active, priority 100 (Cfged 100)
        # Local state is Active, priority 110 (Cfged 110), may preempt
        # Local state is Disabled(Virtual IP not cfged), priority 1 (Cfged 1)
        p2 = re.compile(r'Local +state +is +(?P<state>(\S+))'
                        '(?:\((?P<reason>.*)\))?'
                        ', +priority +(?P<priority>(\d+))'
                        ' +\(Cfged +(?P<cfged>(\d+))\)'
                        '(?:, +(?P<preempt>(\S+)) +preempt)?$')

        # Forwarding threshold(for vPC), lower: 0 upper: 100
        p3 = re.compile(r'Forwarding +threshold\(for +vPC\),'
                        ' +lower: +(?P<lower>(\d+))'
                        ' +upper: +(?P<upper>(\d+))$')

        # Preemption Delay (Seconds) Reload:10 Minimum:5 Sync:5
        p4 = re.compile(r'Preemption +Delay +\(Seconds\)'
                        '(?: +Reload: +(?P<reload>(\d+)))?'
                        '(?: +Minimum: +(?P<min>(\d+)))?'
                        '(?: +Sync: +(?P<sync>(\d+)))?$')

        # Hellotime 3 sec, holdtime 10 sec
        # Hellotime 999 msec (cfged 9 sec), holdtime 2999 msec (cfged 27 sec)
        p5 = re.compile(r'Hellotime +(?P<hello>(\d+)) +(?P<hello_unit>(\S+))'
                '(?: \(cfged (?P<cfged_hello>(\d+)) +(?P<cfhe_unit>(\S+)\)))?'
                ', +holdtime +(?P<hold>(\d+)) +(?P<hold_unit>(\S+))'
                '(?: +\(cfged (?P<cfged_hold>(\d+)) (?P<cfhd_unit>(\S+))\))?$')

        # Next hello sent in 2.726000 sec(s)

        # Virtual IP address is 172.16.12.254 (Cfged)
        p7 = re.compile(r'Virtual +IP +address +is +(?P<ip>(\S+))'
                         ' +\((?P<reason>(\S+))\)$')

        # Secondary Virtual IP address is 10.1.1.253
        p8 = re.compile(r'[sS]econdary +[vV]irtual +IP +address +is'
                         ' +(?P<ip>(\S+))')

        # Active router is local
        # Active router is 192.168.1.1, priority 110 expires in 2.662000 sec(s)
        p9 = re.compile(r'Active +router +is +(?P<active>(\S+))(?: *,'
                         ' +priority +(?P<priority>(\d+)) expires +in'
                         ' +(?P<expires>(\S+)) +sec\(s\))?$')

        # Standby router is 172.16.12.2 , priority 100 expires in 9.456000 sec(s)
        p10 = re.compile(r'Standby +router +is +(?P<standby>(\S+))(?: *,'
                          ' +priority +(?P<priority>(\d+)) +expires +in'
                          ' +(?P<expires>(\S+)) +sec\(s\))?$')

        # Authentication text "cisco"
        # Authentication MD5, key-string "cisco123"
        p11 = re.compile(r'Authentication +(?:(MD5, key-string)|(text))?'
                          ' +\"(?P<auth>(\S+))\"$')

        # Virtual mac address is 0000.0cff.b308 (Default MAC)
        p12 = re.compile(r'Virtual +mac +address +is +(?P<mac>(\S+))'
                          ' +\((?P<status>\S+) MAC( - (?P<use_bia>(\S+))'
                          ' +enabled)?\)$')

        # 2 state changes, last state change 03:13:06
        p13 = re.compile(r'(?P<state_changes>(\d+)) +state +changes,'
                          ' +last +state +change +(?P<last>(\S+))$')


        # Track object 1 state UP decrement 22
        p14 = re.compile(r'[tT]rack +object +(?P<tracked_object>\d+)'
                          ' +state +(?P<tracked_status>(\S+)) +decrement'
                          ' +(?P<decrement>(\d+))')

        # IP redundancy name is hsrp-Eth1/3-1 (default)
        p15 = re.compile(r'IP +redundancy +name +is +(?P<name>(\S+)) +\(default\)$')

        # Secondary VIP(s):
        p16 = re.compile(r'Secondary +VIP\(s\):$')

        # 2001:db8:7746:fa41::1
        p17 = re.compile(r'(?P<vip>(\S+))$')


        for line in out.splitlines():
            line = line.strip()

            # Ethernet1/3 - Group 1 (HSRP-V1) (IPv4)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf = group['intf']
                intf_dict = parsed_dict.setdefault(intf, {})
                intf_dict['interface'] = intf

                address_family = group['af'].lower()
                af_dict = intf_dict.setdefault('address_family', {}).\
                                      setdefault(address_family, {})

                version = int(group['version'])
                version_dict = af_dict.setdefault('version', {}).\
                                       setdefault(version, {})

                gnum = int(group['gnum'])
                groups_dict = version_dict.setdefault('groups', {}).\
                                           setdefault(gnum, {})
                groups_dict['group_number'] = gnum
                continue

            # Local state is Active, priority 100 (Cfged 100)
            # Local state is Active, priority 110 (Cfged 110), may preempt
            # Local state is Disabled(Virtual IP not cfged), priority 1 (Cfged 1)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                # Save for use when active/standby is local
                priority = int(group['priority'])
                groups_dict['priority'] = priority
                groups_dict['hsrp_router_state'] = group['state'].lower()
                groups_dict['configured_priority'] = int(group['cfged'])
                if group['reason']:
                    groups_dict['hsrp_router_state_reason'] = \
                        group['reason'].lower()
                if group['preempt']:
                    groups_dict['preempt'] = True
                continue

            # Forwarding threshold(for vPC), lower: 1 upper: 110
            m = p3.match(line)
            if m:
                group = m.groupdict()
                groups_dict['lower_fwd_threshold'] = int(group['lower'])
                groups_dict['upper_fwd_threshold'] = int(group['upper'])
                continue

            # Preemption Delay (Seconds) Reload:10 Minimum:5 Sync:5 
            m = p4.match(line)
            if m:
                group = m.groupdict()
                groups_dict['preempt_reload_delay'] = int(group['reload'])
                groups_dict['preempt_min_delay'] = int(group['min'])
                groups_dict['preempt_min_delay'] = int(group['sync'])
                continue

            # Hellotime 1 sec, holdtime 3 sec
            # Hellotime 299 msec, holdtime 2222 msec
            # Hellotime 999 msec (cfged 9 sec), holdtime 2999 msec (cfged 27 sec)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                hello_unit = group['hello_unit']
                hold_unit = group['hold_unit']

                # set timers dict
                timers_dict = groups_dict.setdefault('timers', {})                
                if hello_unit == 'sec' and hold_unit == 'sec':
                    timers_dict['hello_msec_flag'] = False
                    timers_dict['hold_msec_flag'] = False
                    timers_dict['hello_sec'] = int(group['hello'])
                    timers_dict['hold_sec']  = int(group['hold'])
                elif hello_unit == 'msec' and hold_unit == 'sec':
                    timers_dict['hello_msec_flag'] = True
                    timers_dict['hold_msec_flag'] = False
                    timers_dict['hello_msec'] = int(group['hello'])
                    timers_dict['hold_sec'] = int(group['hold'])
                elif hello_unit == 'sec' and hold_unit == 'msec':
                    timers_dict['hello_msec_flag'] = False
                    timers_dict['hold_msec_flag'] = True
                    timers_dict['hello_sec'] = int(group['hello'])
                    timers_dict['hold_msec'] = int(group['hold'])
                elif hello_unit == 'msec' and hold_unit == 'msec':
                    timers_dict['hello_msec_flag'] = True
                    timers_dict['hold_msec_flag'] = True
                    timers_dict['hello_msec'] = int(group['hello'])
                    timers_dict['hold_msec'] = int(group['hold'])

                # cfged pararms
                if group['cfged_hello']:
                    timers_dict['cfged_hello_interval'] = int(group['cfged_hello'])
                if group['cfhe_unit']:
                    timers_dict['cfged_hello_unit'] = group['cfhe_unit']
                if group['cfged_hold']:
                    timers_dict['cfged_hold_interval'] = int(group['cfged_hold'])
                if group['cfhd_unit']:
                    timers_dict['cfged_hold_unit'] = group['cfhd_unit']
                continue

            # Virtual IP address is 192.168.1.254 (Cfged)
            # Virtual IP address is 10.1.1.254 (Learnt)
            # Virtual IP address is fe80::5:73ff:fea0:14 (Auto)
            # Virtual IP address is fe80::1 (Cfged)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ip = group['ip']
                reason = group['reason']                
                if ':' in ip:
                    # IPv6 Global Address
                    if '/' in ip:
                        global_v6_dict = groups_dict.\
                                    setdefault('global_ipv6_addresses', {}).\
                                    setdefault(ip, {})
                        global_v6_dict['address'] = ip
                    else:
                        # IPv6 Link Local address
                        link_local_v6_dict = groups_dict.\
                                    setdefault('link_local_ipv6_address', {})
                        link_local_v6_dict['address'] = ip
                        if reason == 'Auto':
                            link_local_v6_dict['auto_configure'] = True
                        else:
                            link_local_v6_dict['auto_configure'] = False
                else:
                    # IPv4 Primary Address
                    primary_v4_dict = groups_dict.\
                                        setdefault('primary_ipv4_address', {})
                    primary_v4_dict['address'] = ip
                    if reason == 'Learnt':
                        primary_v4_dict['virtual_ip_learn'] = True
                    else:
                        primary_v4_dict['virtual_ip_learn'] = False
                continue

            # Secondary Virtual IP address is 10.1.1.253
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ip = group['ip']
                secondary_v4_dict = groups_dict.\
                                    setdefault('secondary_ipv4_addresses', {}).\
                                    setdefault(ip, {})
                secondary_v4_dict['address'] = ip
                continue

            # Active router is unknown
            # Active router is 192.168.1.1, priority 110 expires in 2.662000 sec(s)
            m = p9.match(line)
            if m:
                group = m.groupdict()
                role = group['active']
                groups_dict['active_router'] = role
                if group['expires']:
                    groups_dict['active_expire'] = float(group['expires'])

                # v6/v4 addresses
                if role != 'local' and role != 'unknown':
                    if ':' in role:
                        groups_dict['active_ipv6_address'] = role
                    else:
                        groups_dict['active_ip_address'] = role

                # priority
                if role == 'local':
                    try:
                        groups_dict['active_priority'] = priority
                    except Exception:
                        pass
                elif group['priority']:
                    groups_dict['active_priority'] = int(group['priority'])
                continue

            # Standby router is unknown
            # Standby router is 192.168.1.2 , priority 90 expires in 2.426000 sec(s)
            m = p10.match(line)
            if m:
                group = m.groupdict()
                role = group['standby']
                groups_dict['standby_router'] = role

                # expire
                if group['expires']:
                    groups_dict['standby_expire'] = float(group['expires'])

                # v6/v4 addresses
                if role != 'local' and role != 'unknown':
                    if ':' in role:
                        groups_dict['standby_ipv6_address'] = role
                    else:
                        groups_dict['standby_ip_address'] = role

                # priority
                if role == 'local':
                    try:
                        groups_dict['standby_priority'] = priority
                    except Exception:
                        pass
                elif group['priority']:
                    groups_dict['standby_priority'] = int(group['priority'])
                continue

            # Authentication text "cisco123"
            m = p11.match(line)
            if m:
                groups_dict['authentication'] = m.groupdict()['auth']
                continue

            # Virtual mac address is 0000.0cff.909f (Default MAC)
            m = p12.match(line)
            if m:
                group = m.groupdict()
                groups_dict['virtual_mac_address'] = group['mac']
                groups_dict['virtual_mac_address_status'] = group['status'].lower()
                if group['use_bia'] == 'use-bia':
                    intf_dict['use_bia'] = True
                else:
                    intf_dict['use_bia'] = False
                continue

            # 0 state changes, last state change never
            # 4 state changes, last state change 01:42:05
            m = p13.match(line)
            if m:
                group = m.groupdict()
                groups_dict['num_state_changes'] = int(group['state_changes'])
                groups_dict['last_state_change'] = group['last']
                continue

            # Track object 1 state UP decrement 22
            m = p14.match(line)
            if m:
                group = m.groupdict()
                tracked_object = int(group['tracked_object'])
                tobj_dict = groups_dict.setdefault('tracked_objects', {}).\
                                        setdefault(tracked_object, {})
                tobj_dict['object_name'] = tracked_object
                tobj_dict['status'] =group['tracked_status']
                tobj_dict['priority_decrement'] = int(group['decrement'])
                continue

            # IP redundancy name is hsrp-Eth4/1-0 (default)
            m = p15.match(line)
            if m:
                groups_dict['session_name'] = m.groupdict()['name']
                continue

            # Secondary VIP(s):
            m = p16.match(line)
            if m:
                secondary_vip_exists = True
                secondary_vips = []
                continue

            # 2001:db8:7746:fa41::1
            # 10.1.1.253
            m = p17.match(line)
            if m and secondary_vip_exists:
                vip = m.groupdict()['vip']
                secondary_vips.append(vip)
                groups_dict['secondary_vips'] = secondary_vips
                # fe80
                if 'fe80' not in secondary_vips:
                    mdict = groups_dict.setdefault('global_ipv6_addresses', {}).\
                                        setdefault(vip, {})
                    mdict['address'] = vip
                continue

        return parsed_dict


# ============================
# Schema for 'show hsrp delay'
# ============================
class ShowHsrpDelaySchema(MetaParser):

    ''' Schema for show hsrp delay '''

    schema = {
        Any():
            {'delay':
                {'minimum_delay': int,
                'reload_delay': int},
            },
        }

# ============================
# Parser for 'show hsrp delay'
# ============================
class ShowHsrpDelay(ShowHsrpDelaySchema):

    ''' Parser for show hsrp delay '''

    cli_command = 'show hsrp delay'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

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
