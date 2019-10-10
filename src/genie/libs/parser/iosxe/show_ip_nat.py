"""show_ip_nat.py
    supported commands:
        * show ip nat translations
        * show ip nat translations verbose
        * show ip nat statistics
"""

# Python
import re
import random

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowIpNatTranslationsSchema(MetaParser):
    """ Schema for the commands:
            * show ip nat translations
            * show ip nat translations verbose
    """

    schema = {
        'nat_translations': {
            'index': {
                Any(): {  # 1, 2 ,3, ...
                    'protocol': str,
                    Optional('inside_global'): str,
                    Optional('inside_local'): str,
                    Optional('outside_local'): str,
                    Optional('outside_global'): str,
                    Optional('details'): {
                        'create': str,
                        'use': str,
                        'timeout': str,
                        'map_id_in': int,
                        'mac_address': str,
                        'input_idb': str,
                        'entry_id': str,
                        'use_count': int
                    }
                },
            },
            'number_of_translations': int
        }
    }

class ShowIpNatTranslations(ShowIpNatTranslationsSchema):
    """
        * show ip nat translations
        * show ip nat translations verbose
    """

    cli_command = ['show ip nat translation', 'show ip nat translations verbose']

    def cli(self, option=None, output=None):
        
        if option:
            cmd = self.cli_command[1].format(option="verbose")
        
        if not option:
            cmd = self.cli_command[0]

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        # udp  10.5.5.1:1025          192.0.2.1:4000 --- ---
        # udp  10.5.5.1:1024          192.0.2.3:4000 --- ---
        # udp  10.5.5.1:1026          192.0.2.2:4000 --- ---
        # --- 171.69.233.209     192.168.1.95 --- ---
        # --- 171.69.233.210     192.168.1.89 --- ---
        # udp 171.69.233.209:1220  192.168.1.95:1220  171.69.2.132:53    171.69.2.132:53
        # tcp 171.69.233.209:11012 192.168.1.89:11012 171.69.1.220:23    171.69.1.220:23
        # tcp 171.69.233.209:1067  192.168.1.95:1067  171.69.1.161:23    171.69.1.161:23
        p1 = re.compile(r'^(?P<protocol>-+|udp|tcp) +(?P<inside_global>\S+) '
                         '+(?P<inside_local>\S+) +(?P<outside_local>\S+) +(?P<outside_global>\S+)$')
        
        # create: 02/15/12 11:38:01, use: 02/15/12 11:39:02, timeout: 00:00:00
        p2 = re.compile(r'^create: +(?P<create>[\S ]+), +use: +(?P<use>[\S ]+), +timeout: +(?P<timeout>\S+)$')

        # Map-Id(In): 1
        p3 = re.compile(r'^Map-Id\(In\): +(?P<map_id_in>\d+)$')

        # Mac-Address: 0000.0000.0000    Input-IDB: TenGigabitEthernet1/1/0
        p4 = re.compile(r'^Mac-Address: +(?P<mac_address>\S+) +Input-IDB: +(?P<input_idb>\S+)$')

        #entry-id: 0x0, use_count:1
        p5 = re.compile(r'^entry-id: +(?P<entry_id>\S+), +use_count:+(?P<use_count>\d+)$')

        # Total number of translations: 3
        p6 = re.compile(r'^Total +number +of +translations: +(?P<number_of_translations>\d+)$')

        # initialize variables
        ret_dict = {}
        index = 1

        for line in out.splitlines():
            line = line.strip()

            # udp  10.5.5.1:1025          192.0.2.1:4000 --- ---
            # udp  10.5.5.1:1024          192.0.2.3:4000 --- ---
            # udp  10.5.5.1:1026          192.0.2.2:4000 --- ---
            # --- 171.69.233.209     192.168.1.95 --- ---
            # --- 171.69.233.210     192.168.1.89 --- ---
            # udp 171.69.233.209:1220  192.168.1.95:1220  171.69.2.132:53    171.69.2.132:53
            # tcp 171.69.233.209:11012 192.168.1.89:11012 171.69.1.220:23    171.69.1.220:23
            # tcp 171.69.233.209:1067  192.168.1.95:1067  171.69.1.161:23    171.69.1.161:23
            m = p1.match(line)
            if m:
                group = m.groupdict()
                #import pdb;pdb.set_trace()
                protocol_dict = ret_dict.setdefault('nat_translations', {}).setdefault('index', {}).setdefault(index, {})
                protocol_dict.update({'protocol': group['protocol']})
                protocol_dict.update({'inside_global': group['inside_global']})
                protocol_dict.update({'inside_local': group['inside_local']})
                protocol_dict.update({'outside_global': group['outside_global']})
                protocol_dict.update({'outside_local': group['outside_local']})

                index += 1

                continue
            
            # create: 02/15/12 11:38:01, use: 02/15/12 11:39:02, timeout: 00:00:00
            m = p2.match(line)
            if m:
                group = m.groupdict()
                details_dict = protocol_dict.setdefault('details', {})
                details_dict.update({'create': group['create']})
                details_dict.update({'use': group['use']})
                details_dict.update({'timeout': group['timeout']})

                continue
            
            # Map-Id(In): 1
            m = p3.match(line)
            if m:
                details_dict.update({'map_id_in': int(m.groupdict()['map_id_in'])})

                continue

            # Mac-Address: 0000.0000.0000    Input-IDB: TenGigabitEthernet1/1/0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                details_dict.update({'mac_address': group['mac_address']})
                details_dict.update({'input_idb': group['input_idb']})

                continue
            
            # entry-id: 0x0, use_count:1
            m = p5.match(line)
            if m:
                group = m.groupdict()

                details_dict.update({'entry_id': group['entry_id']})
                details_dict.update({'use_count': int(group['use_count'])})

                continue
            
            # Total number of translations: 3
            m = p6.match(line)
            if m:
                #import pdb;pdb.set_trace()
                total_dict = ret_dict.setdefault('nat_translations', {})
                total_dict.update({'number_of_translations': int(m.groupdict()['number_of_translations'])})

                continue

        return ret_dict


class ShowIpNatStatisticsSchema(MetaParser):
    """ Schema for command:
            * show ip nat statistics
    """

    schema = {
        'total_active_translations': {
            'total_translations': int,
            'static': int,
            'dynamic': int,
            'extended': int,
        },
        'outside_interfaces': [],
        'inside_interfaces': [],
        'hits': int,
        'misses': int,
        Optional('cef_translated_pkts'): int,
        Optional('cef_punted_pkts'): int,
        Optional('expired_translations'): int,
        Optional('dynamic_mappings'): {
            Any(): {  # 'Inside source'
                'id': int,
                'access_list': str,
                'pool': str,
                'refcount': int,
                Optional('pool'): {
                    Any(): {  # mypool serial0/0 FastEthernet1/0
                    'netmask': str,
                    'start': str,
                    'end': str,
                    'type': str,
                    'total': str,
                    'allocated': str,
                    'missed': str
                    }
                }
            }
        },
        Optional('nat_limit_statistics'): {
            'max_entry': str,
            'used': int,
            'missed': int
        },
        Optional('pool_stats_drop'): int,
        Optional('mapping_stats_drop'): int,
        Optional('port_block_alloc_fail'): int,
        Optional('ip_alias_add_fail'): int,
        Optional('limit_entry_add_fail'): int,
        Optional('queued_packets'): int
    }

class ShowIpNatStatistics(ShowIpNatStatisticsSchema):
    """
        * show ip nat statistics
    """

    cli_command = ['show ip nat statistics']

    def cli(self, output=None):

        cmd = self.cli_command

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        # Total active translations: 0 (0 static, 0 dynamic 0 extended)
        p1 = re.compile(r'^Total +active +translations: +(?P<total_translations>\d+) '
                        '+\((?P<static>\d+) +static\, +(?P<dynamic>\d+) '
                        '+dynamic\; +(?P<extended>\d+) +extended\)$')

        # Outside interfaces
        # Inside interfaces
        p2 = re.compile(r'^(?P<in_out_interfaces>Outside|Inside) +interfaces\:$')

        # TenGigabitEthernet1/0/0, TenGigabitEthernet1/1/0, TenGigabitEthernet1/2/0, TenGigabitEthernet1/3/0
        # FastEthernet0/0
        p3 = re.compile(r'^(?P<direction_interfaces>[\w\d\/\d\/\d\,\s]+)$')

        parsed_dict = {}
        on_the_outside = False
        on_the_inside = False

        for line in out.splitlines():
            line = line.strip()

            # Total active translations: 0 (0 static, 0 dynamic 0 extended)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                total_active_dict = parsed_dict.setdefault(
                    'total_active_translations', {})
                total_active_dict['total_translations'] = group['total_translations']
                total_active_dict['static'] = int(group['static'])
                total_active_dict['dynamic'] = int(group['static'])
                total_active_dict['extended'] = int(group['extended'])
            
                continue
            # Outside interfaces
            # Inside interfaces
            m = p2.match(line)

            # TenGigabitEthernet1/0/0, TenGigabitEthernet1/1/0, TenGigabitEthernet1/2/0, TenGigabitEthernet1/3/0
            # FastEthernet0/0
            m_1 = p3.match(line)
            if m or m_1:
                if m:
                    group = m.groupdict()
                    if group['in_out_interfaces'] == 'Outside' or on_the_outside:
                        outside_interface = group['in_out_interfaces']
                        on_the_outside = True
                        on_the_inside = False
                    else:
                        inside_interface = group['in_out_interfaces']
                        on_the_inside = True  
                        on_the_outside = False       
                else:
                    group_m1 = m_1.groupdict()
                    # import pdb;pdb.set_trace()
                    if on_the_outside:
                        outside_list = group_m1['direction_interfaces'].split()
                        for item in len(outside_list):
                            parsed_dict['outside_interfaces'] += group_m1['direction_interfaces']
                        import pprint
                        pprint.pprint (outside_list)

                    elif on_the_inside:
                        inside_list = group_m1['direction_interfaces'].split()
                        for item in len(outside_list):
                            parsed_dict['inside_interfaces'] += group_m1['direction_interfaces']
                            print(item)
                        import pprint
                        pprint.pprint (inside_list)

                continue
                    
                

                    

                    

