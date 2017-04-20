''' show_hsrp.py

IOSXE parsers for show commands:
    * 'show standby all'
    * 'show standby internal'

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
#   Parser for 'show standby internal'
# ======================================

class ShowStandbyInternalSchema(MetaParser):

    schema = {'standby_internal':
                    {'hsrp_common_process_state': str,
                     'msgQ_size': int,
                     'msgQ_max_size': int,
                     'hsrp_ipv4_process_state': str,
                     'hsrp_ipv6_process_state': str,
                     'hsrp_timer_wheel_state': str,
                     'hsrp_ha_state': str,
                     'v3_to_v4_transform': str,
                     Optional('virtual_ip_hash_table'):
                        {Any():
                            {'ip': str,
                             'interface': str,
                             'group': int,
                            }},
                     Optional('mac_address_table'):
                        {Any():
                            {'interface': str,
                             'mac_address': str,
                             'group': int,
                            }},
                     },
             }


class ShowStandbyInternal(ShowStandbyInternalSchema):

    def cli(self):
        cmd = 'show standby internal'.format()
        out = self.device.execute(cmd)
        
        # Init vars
        standby_internal_dict = {}
        
        for line in out.splitlines():
            line = line.rstrip()
            
            # HSRP common process running
            p1 = re.compile(r'\s*HSRP +common +process'
                             ' +(?P<hsrp_common_process_state>[a-zA-Z]+)$')
            m = p1.match(line)
            if m:
                if 'standby_internal' not in standby_internal_dict:
                    standby_internal_dict['standby_internal'] = {}
                    stby_internal = standby_internal_dict['standby_internal']
                    stby_internal['hsrp_common_process_state'] = \
                        m.groupdict()['hsrp_common_process_state']
                    continue

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
            p7 = re.compile(r'\s*(?P<hsrp>[0-9]+) +(?P<ip>[0-9\.]+)'
                             ' +(?P<interface>[a-zA-Z0-9\/]+)'
                             ' +Grp +(?P<group>[0-9]+)$')
            m = p7.match(line)
            if m:
                hsrp = int(m.groupdict()['hsrp'])

                if 'virtual_ip_hash_table' not in stby_internal:
                    stby_internal['virtual_ip_hash_table'] = {}

                if hsrp not in stby_internal['virtual_ip_hash_table']:
                    stby_internal['virtual_ip_hash_table'][hsrp] = {}
                    stby_internal['virtual_ip_hash_table'][hsrp]['interface']\
                         = m.groupdict()['interface'].lower()
                    stby_internal['virtual_ip_hash_table'][hsrp]['ip']\
                         = m.groupdict()['ip']
                    stby_internal['virtual_ip_hash_table'][hsrp]['group']\
                         = int(m.groupdict()['group'])
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
                #import pdb ; pdb.set_trace()
                if interface == last_interface:
                    stby_internal['mac_address_table'][hsrp_number]['group']\
                         = int(m.groupdict()['group'])
                    continue

        return standby_internal_dict


# ======================================
#   Parser for 'show standby all'       
# ======================================

class ShowStandbyAllSchema(MetaParser):
    
    schema = {'standby_all':
                    {'group':
                        {Any():
                            {'interface':
                                {Any():
                                    {'state': str,
                                     Optional('version'): int,
                                     Optional('num_state_changes'): int,
                                     Optional('last_state_change'): str,
                                     Optional('track_object'): str,
                                     'virtual_ip_address': str,
                                     'active_virtual_mac_address': str,
                                     'active_mac_in_use': bool,
                                     'local_virtual_mac_address': str,
                                     'local_virtual_mac_default': str,
                                     'hellotime': int,
                                     'holdtime': int,
                                     Optional('next_hello_time'): float,
                                     Optional('authentication_text'): str,
                                     Optional('preempt'): bool,
                                     Optional('preempt_min_delay'): int,
                                     Optional('preempt_reload_delay'): int,
                                     Optional('preempt_sync_delay'): int,
                                     'active_router': str,
                                     'standby_router': str,
                                     Optional('priority'): int,
                                     Optional('default_priority'): int,
                                     Optional('configured_priority'): int,
                                     'default_group_name': str,
                                    },
                                 },
                             },
                         },
                     },
             }

class ShowStandbyAll(ShowStandbyAllSchema):

    def cli(self):
        cmd = 'show standby all'.format()
        out = self.device.execute(cmd)
        
        # Init vars
        standby_all_dict = {}
        
        for line in out.splitlines():
            line = line.rstrip()

            # Ethernet4/1 - Group 0 (version 2)
            p1 = re.compile(r'\s*(?P<intf>[a-zA-Z0-9\/]+) +\- +Group'
                             ' +(?P<group>[0-9]+)'
                             ' *(?:\(version +(?P<version>[0-9]+)\))?$')
            m = p1.match(line)
            if m:
                if 'standby_all' not in standby_all_dict:
                    standby_all_dict['standby_all'] = {}
                    standby_all_dict['standby_all']['group'] = {}
                
                group = int(m.groupdict()['group'])
                if group not in standby_all_dict['standby_all']['group']:
                    standby_all_dict['standby_all']['group'][group] = {}
                    standby_all_dict['standby_all']['group'][group]\
                        ['interface'] = {}

                interface = m.groupdict()['intf']
                if interface not in standby_all_dict['standby_all']\
                        ['group'][group]['interface']:
                    standby_all_dict['standby_all']['group'][group]\
                        ['interface'][interface] = {}
                    intf_key = standby_all_dict['standby_all']['group'][group]\
                        ['interface'][interface]
                if m.groupdict()['version'] is not None:
                    intf_key['version'] = int(m.groupdict()['version'])
                    continue

            # State is Active
            # State is Disabled
            p2 = re.compile(r'\s*State +is +(?P<state>[a-zA-Z\s\(\)]+)$')
            m = p2.match(line)
            if m:
                intf_key['state'] = m.groupdict()['state'].lower()
                continue

            # 8 state changes, last state change 1w0d
            p3 = re.compile(r'\s*(?P<num_state_changes>[0-9]+) +state'
                             ' +changes, +last +state +change'
                             ' +(?P<last_state_change>[a-zA-Z0-9]+)$')
            m = p3.match(line)
            if m:
                intf_key['num_state_changes'] = \
                    int(m.groupdict()['num_state_changes'])
                intf_key['last_state_change'] = \
                    m.groupdict()['last_state_change']
                continue

            # Track object 1 (unknown)
            p4 = re.compile(r'\s*Track +object +(?P<track_object>[0-9]+)'
                             ' +\(unknown\)$')
            m = p4.match(line)
            if m:
                intf_key['track_object'] = m.groupdict()['track_object']
                continue

            # Virtual IP address is 192.168.1.254
            # Virtual IP address is unknown
            p5 = re.compile(r'\s*Virtual +IP +address +is'
                    ' +(?P<virtual_ip_address>[a-zA-Z0-9\.]+)$')
            m = p5.match(line)
            if m:
                intf_key['virtual_ip_address'] = \
                    m.groupdict()['virtual_ip_address']
                continue

            # Active virtual MAC address is 0000.0c9f.f000 (MAC In Use)
            # Active virtual MAC address is unknown (MAC Not In Use)
            p6 = re.compile(r'\s*Active +virtual +MAC +address +is'
                             ' +(?P<active_virtual_mac_address>[a-zA-Z0-9\.]+)'
                             ' +\((?P<mac_use>[a-zA-Z\s]+)\)$')
            m = p6.match(line)
            if m:
                intf_key['active_virtual_mac_address'] = \
                    m.groupdict()['active_virtual_mac_address']
                if m.groupdict()['mac_use'] == "MAC In Use":
                    intf_key['active_mac_in_use'] = True
                else:
                    intf_key['active_mac_in_use'] = False
                    continue

            # Local virtual MAC address is 0000.0c9f.f000 (v2 default)
            p7 = re.compile(r'\s*Local +virtual +MAC +address +is'
                             ' +(?P<local_virtual_mac_address>[a-zA-Z0-9\.]+)'
                             ' +\((?P<local_virtual_mac_default>[a-zA-Z0-9]+)'
                             ' +default\)$')
            m = p7.match(line)
            if m:
                intf_key['local_virtual_mac_address'] = \
                    m.groupdict()['local_virtual_mac_address']
                intf_key['local_virtual_mac_default'] = \
                    m.groupdict()['local_virtual_mac_default']                
                continue

            # Hellotime 1 sec, holdtime 3 sec
            p8 = re.compile(r'\s*Hello +time +(?P<hellotime>[0-9]+) sec,'
                             ' +hold +time +(?P<holdtime>[0-9]+) +sec$')
            m = p8.match(line)
            if m:
                intf_key['hellotime'] = int(m.groupdict()['hellotime'])
                intf_key['holdtime'] = int(m.groupdict()['holdtime'])
                continue

            # Next hello sent in 2.848 secs
            p9 = re.compile(r'\s*Next +hello +sent +in'
                             ' +(?P<next_hello_time>[0-9\.]+) secs$')
            m = p9.match(line)
            if m:
                intf_key['next_hello_time'] = \
                    float(m.groupdict()['next_hello_time'])
                continue

            # Authentication MD5, key-string "cisco123"
            # Authentication MD5, key-chain "cisco123"
            # Authentication text "cisco123"
            # Authentication "cisco123"
            p10 = re.compile(r'\s*Authentication *(?:MD5)?(?:,)?'
                              ' *(?:key-string|key-chain)? *(?:text)?'
                              ' +\"(?P<authentication_text>[a-zA-Z0-9]+)\"$')
            m = p10.match(line)
            if m:
                intf_key['authentication_text'] = \
                    m.groupdict()['authentication_text']
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
                    intf_key['preempt'] = True
                if m.groupdict()['preempt_min_delay'] is not None:
                    intf_key['preempt_min_delay'] = \
                        int(m.groupdict()['preempt_min_delay'])
                if m.groupdict()['preempt_reload_delay'] is not None:
                    intf_key['preempt_reload_delay'] = \
                        int(m.groupdict()['preempt_reload_delay'])
                if m.groupdict()['preempt_sync_delay'] is not None:
                    intf_key['preempt_sync_delay'] = \
                        int(m.groupdict()['preempt_sync_delay'])
                    continue

            # Active router is unknown
            p12 = re.compile(r'\s*Active +router +is'
                              ' +(?P<active_router>[a-zA-Z\s]+)$')
            m = p12.match(line)
            if m:
                intf_key['active_router'] = m.groupdict()['active_router']
                continue

            # Standby router is unknown 
            p13 = re.compile(r'\s*Standby +router +is'
                              ' +(?P<standby_router>[a-zA-Z\s]+)$')
            m = p13.match(line)
            if m:
                intf_key['standby_router'] = m.groupdict()['standby_router']
                continue

            # Priority 100 (default 100)
            p14 = re.compile(r'\s*Priority +(?P<priority>[0-9]+)'
                              ' +\(default +(?P<default_priority>[0-9]+)\)$')
            m = p14.match(line)
            if m:
                intf_key['priority'] = int(m.groupdict()['priority'])
                intf_key['default_priority'] = \
                    int(m.groupdict()['default_priority'])
                continue

            # Priority 100 (configured 100)
            p15 = re.compile(r'\s*Priority +(?P<priority>[0-9]+)'
                              ' +\(configured'
                              ' +(?P<configured_priority>[0-9]+)\)$')
            m = p15.match(line)
            if m:
                intf_key['priority'] = int(m.groupdict()['priority'])
                intf_key['configured_priority'] = \
                    int(m.groupdict()['configured_priority'])
                continue

            # Group name is "hsrp-Gi1/0/1-0" (default)
            p16 = re.compile(r'\s*Group +name +is'
                              ' +\"(?P<default_group_name>[a-zA-Z0-9\/\-]+)\"'
                              ' +\(default\)$')
            m = p16.match(line)
            if m:
                intf_key['default_group_name'] = \
                    m.groupdict()['default_group_name']
                continue

        return standby_all_dict


    def yang(self):
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
                        text = gigabitethernet.tag[gigabitethernet.tag.find('}')+1:]
                        if text == 'name':
                            gig_number = gigabitethernet.text
                            interface_name = 'Gigabitethernet' + str(gig_number)
                            continue


# vim: ft=python et sw=4
