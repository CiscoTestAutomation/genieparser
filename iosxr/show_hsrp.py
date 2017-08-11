''' show_hsrp.py

IOSXR parsers for show commands:
    * 'show hsrp summary'
    * 'show hsrp detail'

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
                    {'address_family':
                        {Any():
                            {'state':
                                {Any():
                                    {'sessions': int,
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
                     },
             }


class ShowHsrpSummary(ShowHsrpSummarySchema):

    def cli(self):
        cmd = 'show hsrp summary'.format()
        out = self.device.execute(cmd)
        
        # Init vars
        hsrp_summary_dict = {}
        ipv4_set = False
        ipv6_set = False
        
        for line in out.splitlines():
            line = line.rstrip()
            
            # ALL            2      0     2         0      0     0
            p1 = re.compile(r'\s*(?P<state_name>[a-zA-Z]+)'
                             ' +(?P<v4_sessions>[0-9]+) +(?P<v4_slaves>[0-9]+)'
                             ' +(?P<v4_total>[0-9]+) +(?P<v6_sessions>[0-9]+)'
                             ' +(?P<v6_slaves>[0-9]+) +(?P<v6_total>[0-9]+)$')
            m = p1.match(line)
            if m:
                if 'hsrp_summary' not in hsrp_summary_dict:
                    hsrp_summary_dict['hsrp_summary'] = {}
                    hsrp_summary_dict['hsrp_summary']['address_family'] = {}
                    hsrp_summary_dict['hsrp_summary']['address_family']\
                        ['ipv4'] = {}
                    ipv4 = hsrp_summary_dict['hsrp_summary']['address_family']\
                        ['ipv4']
                    hsrp_summary_dict['hsrp_summary']['address_family']\
                        ['ipv6'] = {}
                    ipv6 = hsrp_summary_dict['hsrp_summary']['address_family']\
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
            p2 = re.compile(r'\s*(?P<num_intf>[0-9]+) +HSRP +IPv4 +interfaces'
                             ' +\(+(?P<intf_up>[0-9]+) +up,'
                             ' +(?P<intf_down>[0-9]+) +down\)$')
            m = p2.match(line)
            if m:
                if ipv4_set:
                    ipv4['intf_total'] = int(m.groupdict()['num_intf'])
                    ipv4['intf_up'] = int(m.groupdict()['intf_up'])
                    ipv4['intf_down'] = int(m.groupdict()['intf_down'])
                    continue

            # 0    HSRP IPv6 interfaces    (0    up, 0    down)
            p3 = re.compile(r'\s*(?P<num_intf>[0-9]+) +HSRP +IPv6 +interfaces'
                             ' +\(+(?P<intf_up>[0-9]+) +up,'
                             ' +(?P<intf_down>[0-9]+) +down\)$')
            m = p3.match(line)
            if m:
                if ipv6_set:
                    ipv6['intf_total'] = int(m.groupdict()['num_intf'])
                    ipv6['intf_up'] = int(m.groupdict()['intf_up'])
                    ipv6['intf_down'] = int(m.groupdict()['intf_down'])
                    continue

            # 2    Virtual IPv4 addresses  (1    active, 1    inactive)
            p4 = re.compile(r'\s*(?P<num_addresses>[0-9]+) +Virtual +IPv4'
                             ' +addresses +\((?P<active>[0-9]+) +active,'
                             ' +(?P<inactive>[0-9]+) +inactive\)$')
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
            p5 = re.compile(r'\s*(?P<num_addresses>[0-9]+) +Virtual +IPv6'
                             ' +addresses +\((?P<active>[0-9]+) +active,'
                             ' +(?P<inactive>[0-9]+) +inactive\)$')
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
            p6 = re.compile(r'\s*(?P<num_tracked_objects>[0-9]+) +Tracked'
                             ' +Objects +\((?P<tracked_objects_up>[0-9]+) +up,'
                             ' +(?P<tracked_objects_down>[0-9]+) +down\)$')
            m = p6.match(line)
            if m:
                hsrp_summary_dict['hsrp_summary']['num_tracked_objects'] = \
                    int(m.groupdict()['num_tracked_objects'])
                hsrp_summary_dict['hsrp_summary']['tracked_objects_up'] = \
                    int(m.groupdict()['tracked_objects_up'])
                hsrp_summary_dict['hsrp_summary']['tracked_objects_down'] = \
                    int(m.groupdict()['tracked_objects_down'])
                continue

            # 0    BFD sessions       (0    up, 0    down, 0    inactive)
            p7 = re.compile(r'\s*(?P<num_bfd_sessions>[0-9]+) +BFD +sessions'
                             ' +\((?P<bfd_sessions_up>[0-9]+) +up,'
                             ' +(?P<bfd_sessions_down>[0-9]+) +down,'
                             ' +(?P<bfd_sessions_inactive>[0-9]+) +inactive\)$')
            m = p7.match(line)
            if m:
                hsrp_summary_dict['hsrp_summary']['num_bfd_sessions'] = \
                    int(m.groupdict()['num_bfd_sessions'])
                hsrp_summary_dict['hsrp_summary']['bfd_sessions_up'] = \
                    int(m.groupdict()['bfd_sessions_up'])
                hsrp_summary_dict['hsrp_summary']['bfd_sessions_down'] = \
                    int(m.groupdict()['bfd_sessions_down'])
                hsrp_summary_dict['hsrp_summary']['bfd_sessions_inactive'] = \
                    int(m.groupdict()['bfd_sessions_inactive'])
                continue

        return hsrp_summary_dict


# ======================================
#   Parser for 'show hsrp detail'       
# ======================================

class ShowHsrpDetailSchema(MetaParser):
    
    schema = {'hsrp_detail':
                    {'group':
                        {Any():
                            {'interface':
                                {Any():
                                    {'address_family':
                                        {Any():
                                             {'version': int,
                                             Optional('local_state'): str,
                                             Optional('priority'): int,
                                             Optional('preempt'): bool,
                                             Optional('preempt_delay'): int,
                                             'hellotime': int,
                                             'holdtime': int,
                                             Optional('config_hellotime'): int,
                                             Optional('config_holdtime'): int,
                                             Optional('active_priority'): int,
                                             Optional('standby_priority'): int,
                                             Optional('active_expire'): str,
                                             Optional('standby_expire'): str,
                                             'min_delay': int,
                                             'reload_delay': int,
                                             'ip_address': str,
                                             'active_router': str,
                                             'standby_router': str,
                                             'standby_virtual_mac_addr': str,
                                             'standby_state': str,
                                             Optional('authentication_text'): str,
                                             'num_state_changes': int,
                                             'last_state_change': str,
                                             'last_coup_sent': str,
                                             'last_coup_received': str,
                                             'last_resign_sent': str,
                                             'last_resign_received': str,
                                             Optional('track_objects'):
                                                {Optional('num_tracked_objects'): int,
                                                 Optional('num_tracked_objects_up'): int,
                                                 Any():
                                                        {Optional('priority_decrement'): int},
                                                 },
                                            },
                                        },
                                    }
                                 },
                             },
                         },
                     },
                }

class ShowHsrpDetail(ShowHsrpDetailSchema):

    def cli(self):
        cmd = 'show hsrp detail'.format()
        out = self.device.execute(cmd)
        
        # Init vars
        hsrp_detail_dict = {}
        
        for line in out.splitlines():
            line = line.rstrip()

            # GigabitEthernet0/0/0/1 - IPv4 Group 5 (version 1)
            p1 = re.compile(r'\s*(?P<intf>[a-zA-Z0-9\/\.]+)'
                             ' +\- +(?P<af>[a-zA-Z0-9]+)'
                             ' +Group +(?P<group>[0-9]+)'
                             ' +\(version +(?P<version>[0-9]+)\)$')
            m = p1.match(line)
            if m:
                if 'hsrp_detail' not in hsrp_detail_dict:
                    hsrp_detail_dict['hsrp_detail'] = {}
                    hsrp_detail_dict['hsrp_detail']['group'] = {}
                
                group = int(m.groupdict()['group'])
                interface = m.groupdict()['intf']

                if group not in hsrp_detail_dict['hsrp_detail']['group']:
                    hsrp_detail_dict['hsrp_detail']['group'][group] = {}
                    hsrp_detail_dict['hsrp_detail']['group'][group]\
                        ['interface'] = {}
                
                if interface not in hsrp_detail_dict['hsrp_detail']['group']\
                        [group]['interface']:
                    hsrp_detail_dict['hsrp_detail']['group'][group]\
                        ['interface'][interface] = {}

                if 'address_family' not in hsrp_detail_dict['hsrp_detail']\
                    ['group'][group]['interface'][interface]:
                    hsrp_detail_dict['hsrp_detail']['group'][group]['interface']\
                        [interface]['address_family'] = {}

                af = m.groupdict()['af'].lower()

                if af not in hsrp_detail_dict['hsrp_detail']\
                    ['group'][group]['interface'][interface]['address_family']:
                    hsrp_detail_dict['hsrp_detail']['group'][group]\
                        ['interface'][interface]['address_family'][af] = {}

                    intf_key = hsrp_detail_dict['hsrp_detail']['group'][group]\
                        ['interface'][interface]['address_family'][af]
                        
                    intf_key['version'] = int(m.groupdict()['version'])
                    continue

            # Local state is Active, priority 110, may preempt
            p2 = re.compile(r'\s*Local +state +is +(?P<local_state>[a-zA-Z]+),'
                             ' +priority +(?P<priority>[0-9]+),'
                             ' +(?P<preempt>[a-zA-Z]+) preempt$')
            m = p2.match(line)
            if m:
                intf_key['local_state'] = m.groupdict()['local_state'].lower()
                priority = int(m.groupdict()['priority'])
                intf_key['priority'] = priority
                if m.groupdict()['preempt'] is not None:
                    intf_key['preempt'] = True
                    continue

            # Preemption delay for at least 10 secs
            p3 = re.compile(r'\s*Preemption +delay +for +at +least'
                             ' +(?P<preempt_delay>[0-9]+) +secs$')
            m = p3.match(line)
            if m:
                intf_key['preempt_delay'] = int(m.groupdict()['preempt_delay'])
                continue

            # Hellotime 1000 msec holdtime 3000 msec
            p4 = re.compile(r'\s*Hellotime +(?P<hellotime>[0-9]+) +msec'
                             ' +holdtime +(?P<holdtime>[0-9]+) +msec$')
            m = p4.match(line)
            if m:
                intf_key['hellotime'] = int(m.groupdict()['hellotime'])
                intf_key['holdtime'] = int(m.groupdict()['holdtime'])
                continue

            # Configured hellotime 1000 msec holdtime 3000 msec
            p5 = re.compile(r'\s*Configured +hellotime'
                             ' +(?P<config_hellotime>[0-9]+) msec +holdtime'
                             ' +(?P<config_holdtime>[0-9]+) +msec$')
            m = p5.match(line)
            if m:
                intf_key['config_hellotime'] = \
                    int(m.groupdict()['config_hellotime'])
                intf_key['config_holdtime'] = \
                    int(m.groupdict()['config_holdtime'])
                continue

            # Minimum delay 5 sec, reload delay 10 sec
            p6 = re.compile(r'\s*Minimum +delay +(?P<min_delay>[0-9]+) +sec,'
                             ' +reload +delay +(?P<reload_delay>[0-9]+) +sec$')
            m = p6.match(line)
            if m:
                intf_key['min_delay'] = int(m.groupdict()['min_delay'])
                intf_key['reload_delay'] = int(m.groupdict()['reload_delay'])
                continue

            # Hot standby IP address is 192.168.1.254 configured
            # Hot standby IP address is fe80::205:73ff:fea0:1 configured
            p7 = re.compile(r'\s*Hot +standby +IP +address +is'
                             ' +(?P<ip_address>[\w\:\.]+) +configured$')
            m = p7.match(line)
            if m:
                intf_key['ip_address'] = m.groupdict()['ip_address']
                continue

            # Active router is 
            # Active router is 192.168.1.2 expires in 00:00:02
            p8 = re.compile(r'\s*Active +router +is'
                             ' +(?P<active_router>([\w\:\.]+)(, *[\w\.\:]+)?)'
                             '( *(expired|expires +in +(?P<expire>[\w\:\.]+)))?$')
            m = p8.match(line)
            if m:
                role = m.groupdict()['active_router']
                if role == 'local':
                    try:
                        priority
                    except:
                        pass
                    else:
                        intf_key['active_priority'] = int(priority)

                intf_key['active_router'] = role
                    
                if m.groupdict()['expire']:
                    intf_key['active_expire'] = m.groupdict()['expire']
                continue

            # Standby router is unknown expired
            # Standby router is 192.168.1.2 expires in 00:00:02
            # Standby router is fe80::5000:1cff:fe0a:1, 5200.1c0a.0001 expires in 00:00:02
            p9 = re.compile(r'\s*Standby +router +is'
                             ' +(?P<standby_router>([\w\:\.]+)(, *[\w\.\:]+)?)'
                             '( *(expired|expires +in +(?P<expire>[\w\:\.]+)))?$')
            m = p9.match(line)
            if m:
                role = m.groupdict()['standby_router']
                if role == 'local':
                    try:
                        priority
                    except:
                        pass
                    else:
                        intf_key['standby_priority'] = int(priority)

                intf_key['standby_router'] = role
                    
                if m.groupdict()['expire']:
                    intf_key['standby_expire'] = m.groupdict()['expire']
                continue

            # Standby virtual mac address is 0000.0c07.ac05, state is active
            p10 = re.compile(r'\s*Standby +virtual +mac +address +is'
                              ' +(?P<standby_virtual_mac_addr>[a-zA-Z0-9\.]+),'
                              ' +state +is +(?P<standby_state>[a-zA-Z ]+)$')
            m = p10.match(line)
            if m:
                intf_key['standby_virtual_mac_addr'] = \
                    m.groupdict()['standby_virtual_mac_addr']
                intf_key['standby_state'] = m.groupdict()['standby_state']
                continue

            # Authentication text, string "cisco123"
            p11 = re.compile(r'\s*Authentication +text, +string'
                              ' +\"(?P<authentication_text>[a-zA-Z0-9]+)\"$')
            m = p11.match(line)
            if m:
                intf_key['authentication_text'] = \
                    m.groupdict()['authentication_text']
                continue

            # 4 state changes, last state change 2d03h
            # 2 state changes, last state change 01:18:43
            p12 = re.compile(r'\s*(?P<num_state_changes>[0-9]+) +state'
                              ' +changes, +last +state +change'
                              ' +(?P<last_state_change>[a-zA-Z0-9\:\.]+)$')
            m = p12.match(line)
            if m:
                intf_key['num_state_changes'] = \
                    int(m.groupdict()['num_state_changes'])
                intf_key['last_state_change'] = \
                    m.groupdict()['last_state_change']
                continue

            # Last coup sent:       Never
            # Last coup sent:       Aug 11 08:26:25.272 UTC
            p13 = re.compile(r'\s*Last +coup +sent:'
                              ' +(?P<last_coup_sent>[\w\s\:\.]+)$')
            m = p13.match(line)
            if m:
                intf_key['last_coup_sent'] = m.groupdict()['last_coup_sent']
                continue

            # Last coup received:   Never
            p14 = re.compile(r'\s*Last +coup +received:'
                              ' +(?P<last_coup_received>[\w\s\:\.]+)$')
            m = p14.match(line)
            if m:
                intf_key['last_coup_received'] = \
                    m.groupdict()['last_coup_received']
                continue

            # Last resign sent:     Never
            p15 = re.compile(r'\s*Last +resign +sent:'
                              ' +(?P<last_resign_sent>[\w\s\:\.]+)$')
            m = p15.match(line)
            if m:
                intf_key['last_resign_sent'] = m.groupdict()['last_resign_sent']
                continue

            # Last resign received: Never
            # Last resign received: Aug 11 08:26:25.272 UTC
            p16 = re.compile(r'\s*Last +resign +received:'
                              ' +(?P<last_resign_received>[\w\s\:\.]+)$')
            m = p16.match(line)
            if m:
                intf_key['last_resign_received'] = \
                    m.groupdict()['last_resign_received']
                continue

            # Tracking states for 1 object, 1 up:
            # Tracking states for 1 objects, 1 up:
            p17 = re.compile(r'\s*Tracking +states +for'
                              ' +(?P<num_tracked_objects>[0-9]+) +object(?:s)?,'
                              ' +(?P<num_tracked_objects_up>[0-9]+) up:$')
            m = p17.match(line)
            if m:
                track_found = True
                intf_key['track_objects'] = {}
                intf_key['track_objects']['num_tracked_objects'] = \
                    int(m.groupdict()['num_tracked_objects'])
                intf_key['track_objects']['num_tracked_objects_up'] = \
                    int(m.groupdict()['num_tracked_objects_up'])
                continue

            # Up   banana               Priority decrement: 20
            # Down   apple               Priority decrement: 50
            p18 = re.compile(r'\s*(Up|Down)'
                              ' +(?P<track_object_name>[a-zA-Z0-9]+) +Priority'
                              ' +decrement: +(?P<priority_decrement>[0-9]+)$')
            m = p18.match(line)
            if m:
                if track_found:
                    track_object_name = m.groupdict()['track_object_name']
                    if track_object_name not in intf_key['track_objects']:
                        intf_key['track_objects'][track_object_name] = {}
                        intf_key['track_objects'][track_object_name]\
                            ['priority_decrement'] = \
                            int(m.groupdict()['priority_decrement'])
                        continue

        return hsrp_detail_dict

# vim: ft=python et sw=4
