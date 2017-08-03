''' show_hsrp.py

NXOS parsers for show commands:
    * 'show hsrp summary'
    * 'show hsrp all'

'''

# Python
import re

# Metaparser
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
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
#   Parser for 'show hsrp summary'
# ======================================

class ShowHsrpSummarySchema(MetaParser):

    schema = {'hsrp_summary':
                    {'nsf': str,
                     Optional('nsf_time'): int,
                     'global_hsrp_bfd': str,
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
                     'intf_total': int,
                     'tx_pass': int,
                     'tx_fail': int,
                     'rx_good': int,
                     'pkt_unknown_groups': int,
                     'total_mts_rx': int,
                     },
             }


class ShowHsrpSummary(ShowHsrpSummarySchema):

    def cli(self):
        cmd = 'show hsrp summary'.format()
        out = self.device.execute(cmd)
        
        # Init vars
        hsrp_summary_dict = {}
        
        
        for line in out.splitlines():
            line = line.rstrip()
            
            # Extended-hold (NSF) enabled, 10 seconds
            # Extended-hold (NSF) disabled
            p1 = re.compile(r'\s*Extended-hold +\(NSF\) +(?P<nsf>[a-zA-Z]+)'
                             '(, +(?P<nsf_time>[0-9]+) seconds)?$')
            m = p1.match(line)
            if m:
                if 'hsrp_summary' not in hsrp_summary_dict:
                    hsrp_summary_dict['hsrp_summary'] = {}
                    hsrp_summary = hsrp_summary_dict['hsrp_summary']

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
                hsrp_summary['total_groups'] = \
                    int(m.groupdict()['total_groups'])
                continue

            # Version::    V1-IPV4: 0       V2-IPV4: 3      V2-IPV6: 0
            p4 = re.compile(r'\s*Version:: +V1-IPV4: +(?P<v1_ipv4>[0-9]+)'
                             ' +V2-IPV4: +(?P<v2_ipv4>[0-9]+) +V2-IPV6:'
                             ' +(?P<v2_ipv6>[0-9]+)$')
            m = p4.match(line)
            if m:
                hsrp_summary['v1_ipv4'] = int(m.groupdict()['v1_ipv4'])
                hsrp_summary['v2_ipv4'] = int(m.groupdict()['v2_ipv4'])
                hsrp_summary['v2_ipv6'] = int(m.groupdict()['v2_ipv6'])
                continue

            # State::     Active: 0       Standby: 0       Listen: 0
            p5 = re.compile(r'\s*State:: +Active: +(?P<active>[0-9]+)'
                             ' +Standby: +(?P<standby>[0-9]+) +Listen:'
                             ' +(?P<listen>[0-9]+)$')
            m = p5.match(line)
            if m:
                hsrp_summary['active'] = int(m.groupdict()['active'])
                hsrp_summary['standby'] = int(m.groupdict()['standby'])
                hsrp_summary['listen'] = int(m.groupdict()['listen'])
                continue

            # State::  V6-Active: 0    V6-Standby: 0    V6-Listen: 0
            p6 = re.compile(r'\s*State:: +V6-Active: +(?P<v6_active>[0-9]+)'
                             ' +V6-Standby: +(?P<v6_standby>[0-9]+)'
                             ' +V6-Listen: +(?P<v6_listen>[0-9]+)$')
            m = p6.match(line)
            if m:
                hsrp_summary['v6_active'] = int(m.groupdict()['v6_active'])
                hsrp_summary['v6_standby'] = int(m.groupdict()['v6_standby'])
                hsrp_summary['v6_listen'] = int(m.groupdict()['v6_listen'])
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
                hsrp_summary['tx_pass'] = int(m.groupdict()['tx_pass'])
                hsrp_summary['tx_fail'] = int(m.groupdict()['tx_fail'])
                continue

            # Rx - Good: 0
            p9 = re.compile(r'\s*Rx +\- +Good: +(?P<rx_good>[0-9]+)$')
            m = p9.match(line)
            if m:
                hsrp_summary['rx_good'] = int(m.groupdict()['rx_good'])
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

        return hsrp_summary_dict

# ======================================
#   Parser for 'show hsrp all'       
# ======================================

class ShowHsrpAllSchema(MetaParser):
    
    schema = {'hsrp_all':
                    {'group':
                        {Any():
                            {'interface':
                                {Any():
                                    {'address_family':
                                        {Any():
                                            {'version': int,
                                             Optional('local_state'): str,
                                             Optional('priority'): int,
                                             Optional('configured_priority'): int,
                                             Optional('preempt'): bool,
                                             Optional('preempt_reload_delay'): int,
                                             Optional('preempt_min_delay'): int,
                                             Optional('preempt_sync_delay'): int,
                                             'upper_fwd_threshold': int,
                                             'lower_fwd_threshold': int,
                                             'hellotime': int,
                                             'holdtime': int,
                                             Optional('virtual_ip_address'): str,
                                             'active_router': str,
                                             'standby_router': str,
                                             'virtual_mac_addr': str,
                                             Optional('authentication_text'): str,
                                             'num_state_changes': int,
                                             'last_state_change': str,
                                             'ip_redundancy_name': str,
                                             Optional('active_priority'): int,
                                             Optional('standby_priority'): int,
                                             Optional('active_expire'): float,
                                             Optional('standby_expire'): float,
                                            }
                                        },
                                    }
                                },
                            },
                        },
                    }
                }

class ShowHsrpAll(ShowHsrpAllSchema):

    def cli(self):
        cmd = 'show hsrp all'.format()
        out = self.device.execute(cmd)
        
        # Init vars
        hsrp_all_dict = {}
        
        for line in out.splitlines():
            line = line.rstrip()

            # Ethernet4/1 - Group 0 (HSRP-V2) (IPv4)
            p1 = re.compile(r'\s*(?P<intf>[a-zA-Z0-9\/]+) +\- +Group'
                             ' +(?P<group>[0-9]+)'
                             ' +\(HSRP-V(?P<version>[0-9]+)\)'
                             ' +\((?P<af>[a-zA-Z0-9]+)\)$')
            m = p1.match(line)
            if m:
                if 'hsrp_all' not in hsrp_all_dict:
                    hsrp_all_dict['hsrp_all'] = {}
                    hsrp_all_dict['hsrp_all']['group'] = {}
                
                group = int(m.groupdict()['group'])
                if group not in hsrp_all_dict['hsrp_all']['group']:
                    hsrp_all_dict['hsrp_all']['group'][group] = {}
                    hsrp_all_dict['hsrp_all']['group'][group]['interface'] = {}

                interface = m.groupdict()['intf']
                if interface not in hsrp_all_dict['hsrp_all']['group']\
                        [group]['interface']:
                    hsrp_all_dict['hsrp_all']['group'][group]\
                        ['interface'][interface] = {}

                if 'address_family' not in hsrp_all_dict['hsrp_all']\
                    ['group'][group]['interface'][interface]:
                    hsrp_all_dict['hsrp_all']['group'][group]['interface']\
                        [interface]['address_family'] = {}

                af = m.groupdict()['af'].lower()

                if af not in hsrp_all_dict['hsrp_all']\
                    ['group'][group]['interface'][interface]['address_family']:
                    hsrp_all_dict['hsrp_all']['group'][group]\
                        ['interface'][interface]['address_family'][af] = {}

                    intf_key = hsrp_all_dict['hsrp_all']['group'][group]\
                        ['interface'][interface]['address_family'][af]

                    intf_key['version'] = int(m.groupdict()['version'])
                    continue

            # Local state is Initial(Interface Down), priority 110 \
            # (Cfged 110), may preempt
            p2 = re.compile(r'\s*Local +state +is'
                             ' +(?P<local_state>[a-zA-Z\s\(\)]+), +priority'
                             ' +(?P<priority>[0-9]+)'' +\(Cfged'
                             ' +(?P<configured_priority>[0-9]+)\)(?:,'
                             ' *(?P<preempt>[a-zA-Z]+) *preempt)?$')
            m = p2.match(line)
            if m:
                intf_key['local_state'] = m.groupdict()['local_state'].lower()
                priority = int(m.groupdict()['priority'])
                intf_key['priority'] = priority
                intf_key['configured_priority'] = \
                    int(m.groupdict()['configured_priority'])
                if m.groupdict()['preempt'] is not None:
                    intf_key['preempt'] = True
                    continue

            # Forwarding threshold(for vPC), lower: 1 upper: 110
            p3 = re.compile(r'\s*Forwarding +threshold\(for +vPC\), +lower:'
                             ' +(?P<lower_fwd_threshold>[0-9]+) +upper:'
                             ' +(?P<upper_fwd_threshold>[0-9]+)$')
            m = p3.match(line)
            if m:
                intf_key['lower_fwd_threshold'] = \
                    int(m.groupdict()['lower_fwd_threshold'])
                intf_key['upper_fwd_threshold'] = \
                    int(m.groupdict()['upper_fwd_threshold'])
                continue

            # Preemption Delay (Seconds) Reload:10 Minimum:5 Sync:5 
            p4 = re.compile(r'\s*Preemption +Delay +\(Seconds\)'
                             '(?: +Reload: *(?P<preempt_reload_delay>[0-9]+))?'
                             '(?: +Minimum: *(?P<preempt_min_delay>[0-9]+))?'
                             '(?: +Sync: *(?P<preempt_sync_delay>[0-9]+))?$')
            m = p4.match(line)
            if m:
                intf_key['preempt_reload_delay'] = \
                    int(m.groupdict()['preempt_reload_delay'])
                intf_key['preempt_min_delay'] = \
                    int(m.groupdict()['preempt_min_delay'])
                intf_key['preempt_min_delay'] = \
                    int(m.groupdict()['preempt_sync_delay'])
                continue

            # Hellotime 1 sec, holdtime 3 sec
            p5 = re.compile(r'\s*Hellotime +(?P<hellotime>[0-9]+) sec,'
                             ' +holdtime +(?P<holdtime>[0-9]+) +sec$')
            m = p5.match(line)
            if m:
                intf_key['hellotime'] = int(m.groupdict()['hellotime'])
                intf_key['holdtime'] = int(m.groupdict()['holdtime'])
                continue

            # Virtual IP address is 192.168.1.254 (Cfged)
            p6 = re.compile(r'\s*Virtual +IP +address +is'
                             ' +(?P<virtual_ip_address>[0-9\.]+) +\(Cfged\)$')
            m = p6.match(line)
            if m:
                intf_key['virtual_ip_address'] = \
                    m.groupdict()['virtual_ip_address']
                continue

            # Active router is unknown
            # Active router is 192.168.1.1, priority 110 expires in 2.662000 sec(s)
            p7 = re.compile(r'\s*Active +router +is'
                             ' +(?P<active_router>[\w\.\:]+)'
                             '( *, *priority *(?P<active_priority>\d+) expires *'
                             'in *(?P<expire>[\w\.]+) *sec\(s\))?$')
            m = p7.match(line)
            if m:
                role = m.groupdict()['active_router']
                if role == 'local':
                    try:
                        priority
                    except:
                        pass
                    else:
                        active_priority = priority
                else:
                    active_priority = m.groupdict()['active_priority']
                intf_key['active_router'] = role
                if active_priority:
                    intf_key['active_priority'] = int(active_priority)
                if m.groupdict()['expire']:
                    intf_key['active_expire'] = \
                        float(m.groupdict()['expire'])
                continue

            # Standby router is unknown
            # Standby router is 192.168.1.2 , priority 90 expires in 2.426000 sec(s)
            p8 = re.compile(r'\s*Standby +router +is'
                             ' +(?P<standby_router>[\w\.\:]+)'
                             '( *, *priority *(?P<standby_priority>\d+) expires *'
                             'in *(?P<expire>[\w\.]+) *sec\(s\))?$')
            m = p8.match(line)
            if m:
                role = m.groupdict()['standby_router']
                if role == 'local':
                    try:
                        priority
                    except:
                        pass
                    else:
                        standby_priority = priority
                else:
                    standby_priority = m.groupdict()['standby_priority']

                intf_key['standby_router'] = role
                if standby_priority:
                    intf_key['standby_priority'] = int(standby_priority)
                if m.groupdict()['expire']:
                    intf_key['standby_expire'] = \
                        float(m.groupdict()['expire'])
                continue

            # Authentication text "cisco123"
            p10 = re.compile(r'\s*Authentication *(?:MD5)?(?:,)?'
                              ' *(?:key-string)? *(?:text)?'
                              ' +\"(?P<authentication_text>[a-zA-Z0-9]+)\"$')
            m = p10.match(line)
            if m:
                intf_key['authentication_text'] = \
                    m.groupdict()['authentication_text']
                continue

            # Virtual mac address is 0000.0c9f.f000 (Default MAC)
            p9 = re.compile(r'\s*Virtual +mac +address +is'
                             ' +(?P<virtual_mac_addr>[a-zA-Z0-9\.]+)'
                             ' +\(Default MAC\)$')
            m = p9.match(line)
            if m:
                intf_key['virtual_mac_addr'] = m.groupdict()['virtual_mac_addr']
                continue

            # 0 state changes, last state change never
            # 4 state changes, last state change 01:42:05
            p11 = re.compile(r'\s*(?P<num_state_changes>[0-9]+) +state'
                              ' +changes, +last +state +change'
                              ' +(?P<last_state_change>[\w\.\:]+)$')
            m = p11.match(line)
            if m:
                intf_key['num_state_changes'] = \
                    int(m.groupdict()['num_state_changes'])
                intf_key['last_state_change'] = \
                    m.groupdict()['last_state_change']
                continue

            # IP redundancy name is hsrp-Eth4/1-0 (default)
            p11 = re.compile(r'\s*IP +redundancy +name +is'
                              ' +(?P<ip_redundancy_name>[a-zA-Z0-9\/\-]+)'
                              ' +\(default\)$')
            m = p11.match(line)
            if m:
                intf_key['ip_redundancy_name'] = \
                    m.groupdict()['ip_redundancy_name']
                continue

        return hsrp_all_dict

# vim: ft=python et sw=4
