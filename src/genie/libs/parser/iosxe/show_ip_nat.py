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
        # create 04/09/11 10:51:48, use 04/09/11 10:52:31, timeout: 00:01:00
        p2 = re.compile(r'^create(?:\:)? +(?P<create>[\S ]+), +use(?:\:)? +(?P<use>[\S ]+), +timeout(?:\:)? +(?P<timeout>\S+)$')

        # IOS-XE: Map-Id(In): 1
        # IOS: Map-Id(In):1, Mac-Address: 0000.0000.0000 Input-IDB: GigabitEthernet0/3/1
        p3 = re.compile(r'^Map\-Id\(In\)[\:|\s*]+(?P<map_id_in>\d+)(?:[\,\s*]+Mac\-Address\: '
                         '+(?P<mac_address>\S+) +Input\-IDB\: +(?P<input_idb>\S+))?$')

        # IOS-XE: Mac-Address: 0000.0000.0000    Input-IDB: TenGigabitEthernet1/1/0
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

                protocol_dict = ret_dict.setdefault('nat_translations', {}).setdefault('index', {}).setdefault(index, {})
                protocol_dict.update({'protocol': group['protocol']})
                protocol_dict.update({'inside_global': group['inside_global']})
                protocol_dict.update({'inside_local': group['inside_local']})
                protocol_dict.update({'outside_global': group['outside_global']})
                protocol_dict.update({'outside_local': group['outside_local']})

                index += 1

                continue
            
            # create: 02/15/12 11:38:01, use: 02/15/12 11:39:02, timeout: 00:00:00
            # create 04/09/11 10:51:48, use 04/09/11 10:52:31, timeout: 00:01:00
            m = p2.match(line)
            if m:
                group = m.groupdict()

                details_dict = protocol_dict.setdefault('details', {})
                details_dict.update({'create': group['create']})
                details_dict.update({'use': group['use']})
                details_dict.update({'timeout': group['timeout']})

                continue
            
            # IOS-XE: Map-Id(In): 1
            # IOS: Map-Id(In):1, Mac-Address: 0000.0000.0000 Input-IDB: GigabitEthernet0/3/1
            m = p3.match(line)
            if m:
                group = m.groupdict()

                details_dict.update({'map_id_in': int(m.groupdict()['map_id_in'])})

                if group['mac_address']:
                    details_dict.update({'mac_address': group['mac_address']})
                
                if group['input_idb']:
                    details_dict.update({'input_idb': group['input_idb']})

                continue

            # IOS-XE: Mac-Address: 0000.0000.0000    Input-IDB: TenGigabitEthernet1/1/0
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
                total_dict = ret_dict.setdefault('nat_translations', {})
                total_dict.update({'number_of_translations': int(m.groupdict()['number_of_translations'])})

                continue

        return ret_dict


class ShowIpNatStatisticsSchema(MetaParser):
    """ Schema for command:
            * show ip nat statistics
    """

    schema = {
        'active_translations': {
            Any(): { #Total active translations
                'static': int,
                'dynamic': int,
                'extended': int,
            },
            'outside_interfaces': list,
            'inside_interfaces': list,
            'hits': int,
            'misses': int,
            Optional('dynamic_mappings'): {
                Any(): {  # 'Inside source'
                    Optional('id'): int,
                    'access_list': str,
                    'refcount': int,
                    Optional('interface'): str,
                    Optional('pool'): {
                        Any(): {  # mypool test-pool
                        'netmask': str,
                        'start': str,
                        'end': str,
                        'type': str,
                        'total': str,
                        'allocated': str,
                        'misses': str,
                        Optional('addr_hash'): int,
                        Optional('average_len'): int,
                        Optional('chains'): str
                        }
                    },
                }
            },
            Optional('nat_limit_statistics'): {
                'max_allowed': int,
                'used': int,
                'missed': int,
            },
            Optional('cef_translated_pkts'): int,
            Optional('cef_punted_pkts'): int,
            Optional('expired_translations'): int,
            Optional('pool_stats_drop'): int,
            Optional('mapping_stats_drop'): int,
            Optional('port_block_alloc_fail'): int,
            Optional('ip_alias_add_fail'): int,
            Optional('limit_entry_add_fail'): int,
            Optional('queued_pkts'): int,
            Optional('peak_translations'): int,
            Optional('occurred'): str,
        }
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
        # IOS
        # Total translations: 2 (0 static, 2 dynamic; 0 extended)
        p1 = re.compile(r'^Total(?: +active)? +translations: +(?P<total_translations>\d+) '
                         '+\((?P<static>\d+) +static\, +(?P<dynamic>\d+) +dynamic\; '
                         '+(?P<extended>\d+) +extended\)$')

        # Outside interfaces:
        # Inside interfaces:
        # IOS
        # Outside interfaces: Serial0
        # Inside interfaces: Ethernet1
        p2 = re.compile(r'^(?P<in_out_interfaces>Outside|Inside) +interfaces\:(?: +(?P<direction_interfaces>\S+))?$')

        # TenGigabitEthernet1/0/0, TenGigabitEthernet1/1/0, TenGigabitEthernet1/2/0, TenGigabitEthernet1/3/0
        # FastEthernet0/0
        p3 = re.compile(r'^(?P<direction_interfaces>[\w\d\/\d\/\d\,\s]+)$')

        # Hits: 59230465  Misses: 3
        # CEF Translated packets: 0, CEF Punted packets: 0
        # Expired translations: 0
        # Pool stats drop: 0  Mapping stats drop: 0
        # Port block alloc fail: 0
        # IP alias add fail: 0
        # Limit entry add fail: 0
        # Queued Packets: 0
        # Peak translations: 8114, occurred 18:35:17 ago
        p4 = re.compile(r'^(?P<name_1>[\w|\s]+)\: +(?P<number_1>\w+)(?:[\,|\s*]'
                         '+(?P<name_2>[\w|\s]+)(?:\:|\s*)? +(?P<number_2>\S+)(?: +ago)?)?$')

        # Dynamic mappings:
        p5 = re.compile(r'^(?P<dynamic>\w+) +mappings\:$')
        
        # -- Inside Source
        p5_1 = re.compile(r'^\-\- +(?P<source>\S+) +Source$')

        # [Id: 1] access-list 102 pool mypool refcount 3
        # access-list 1 pool net-208 refcount 2
        # [Id: 1] access-list 25 interface FastEthernet1/0 refcount 0
        # [Id: 3] access-list 99 interface Serial0/0 refcount 1
        # [Id: 1] access-list test-robot pool test-robot refcount 0
        # [Id: 3] access-list 99 interface Serial0/0 refcount 1
        p6 = re.compile(r'^(?:\[Id\: +(?P<id>\d+)\] )?access\-+list '
                         '+(?P<access_list>[\w\-]+) +(?P<method>pool|interface) '
                         '+(?P<pool>[\w\/-]+) +refcount +(?P<refcount>\d+)$')

        # pool mypool: netmask 255.255.255.0
        p7 = re.compile(r'^pool +(?P<pool>[\w\/-]+)\: +netmask +(?P<netmask>[\d+\.]+)$')

        # start 10.5.5.1 end 10.5.5.5
        p7_1 = re.compile(r'^start +(?P<start>[\d\.]+) +end +(?P<end>[\d\.]+)$')

        # type generic, total addresses 5, allocated 1 (20 %), misses 0
        # type generic, total addresses 1, allocated 0 (0 % ), misses 0
        p7_2 = re.compile(r'^type +(?P<type>\w+)\, +total +addresses '
                           '+(?P<total_addresses>\d+)\, +allocated '
                           '+(?P<allocated>\d+ +\(\w+\%\))\, '
                           '+misses +(?P<misses>\d+)$')
                           
        # max entry: max allowed 2147483647, used 3, missed 0
        p8 = re.compile(r'^max +entry\: +max +allowed +(?P<max_allowed>\d+)\, '
                         '+used +(?P<used>\d+)\, +missed +(?P<missed>\d+)$')
        
        # longest chain in pool: pool1's addr-hash: 0, average len 0,chains 0/256
        # longest chain in pool: test-pool1's addr-hash: 0, average len 0,chains 0/256
        p9 = re.compile(r'^longest +chain +in +pool\: +(?P<pool_name>\S+)\'s '
                         '+addr\-hash\: +(?P<addr_hash>\d+)\, +average +len '
                         '(?P<average_len>\d+)\,+chains +(?P<chains>\S+)$')

        parsed_dict = {}
        on_the_outside = False
        on_the_inside = False

        for line in out.splitlines():
            line = line.strip()

            # Total active translations: 0 (0 static, 0 dynamic 0 extended)
            # IOS
            # Total translations: 2 (0 static, 2 dynamic; 0 extended)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                total = int(group['total_translations'])
                active_dict = parsed_dict.setdefault('active_translations', {})
                total_stats = active_dict.setdefault(total, {})
                total_stats['static'] = int(group['static'])
                total_stats['dynamic'] = int(group['dynamic'])
                total_stats['extended'] = int(group['extended'])

                continue

            # Outside interfaces:
            # Inside interfaces:
            # IOS
            # Outside interfaces: Serial0
            # Inside interfaces: Ethernet1
            m = p2.match(line)

            # TenGigabitEthernet1/0/0, TenGigabitEthernet1/1/0, TenGigabitEthernet1/2/0, TenGigabitEthernet1/3/0
            # FastEthernet0/0
            m_1 = p3.match(line)
            if m or m_1:
                if m:
                    group = m.groupdict()
                    if group['in_out_interfaces'] == 'Outside':
                        outside_interface = group['in_out_interfaces']
                        on_the_outside = True
                        on_the_inside = False

                        if group['direction_interfaces']:
                            outside_list = group['direction_interfaces'].split()
                            olist = []
                            for item in outside_list:
                                olist.append(item)

                            if 'outside_interfaces' in active_dict:
                                active_dict['outside_interfaces'] += olist
                            else:
                                active_dict['outside_interfaces'] = olist
                    else:
                        inside_interface = group['in_out_interfaces']
                        on_the_inside = True  
                        on_the_outside = False 

                        if group['direction_interfaces']:
                            inside_list = group['direction_interfaces'].split()
                            ilist = []
                            for item in inside_list:
                                ilist.append(item)

                            if 'inside_interfaces' in active_dict:
                                active_dict['inside_interfaces'] += ilist
                            else:
                                active_dict['inside_interfaces'] = ilist
    
                else:
                    group_m1 = m_1.groupdict()

                    if on_the_outside:
                        outside_list = group_m1['direction_interfaces'].split()
                        olist = []
                        for item in outside_list:
                            olist.append(item)
                        
                        if 'outside_interfaces' in active_dict:
                            active_dict['outside_interfaces'] += olist
                        else:
                            active_dict['outside_interfaces'] = olist

                    elif on_the_inside:
                        inside_list = group_m1['direction_interfaces'].split()
                        ilist = []
                        for item in inside_list:
                            ilist.append(item)

                        if 'inside_interfaces' in active_dict:
                            active_dict['inside_interfaces'] += ilist
                        else:
                            active_dict['inside_interfaces'] = ilist

                continue

            # Hits: 59230465  Misses: 3
            # CEF Translated packets: 0, CEF Punted packets: 0
            # Expired translations: 0
            # Pool stats drop: 0  Mapping stats drop: 0
            # Port block alloc fail: 0
            # IP alias add fail: 0
            # Limit entry add fail: 0
            # Queued Packets: 0
            # Peak translations: 8114, occurred 18:35:17 ago
            m = p4.match(line)
            if m:
                group = m.groupdict()

                if group['name_1']:
                    if group['name_1'] == 'Hits':
                        active_dict.setdefault(
                            'hits', int(m.groupdict()['number_1']))
                    
                    if group['name_1'] == 'CEF Translated packets':
                        active_dict.setdefault(
                            'cef_translated_pkts', int(m.groupdict()['number_1']))
                    
                    if group['name_1'] == 'Expired translations':
                        active_dict.setdefault(
                            'expired_translations', int(m.groupdict()['number_1']))
                    
                    if group['name_1'] == 'Pool stats drop':
                        active_dict.setdefault(
                            'pool_stats_drop', int(m.groupdict()['number_1']))
                    
                    if group['name_1'] == 'Port block alloc fail':
                        active_dict.setdefault(
                            'port_block_alloc_fail', int(m.groupdict()['number_1']))

                    if group['name_1'] == 'IP alias add fail':
                        active_dict.setdefault(
                            'ip_alias_add_fail', int(m.groupdict()['number_1']))
                    
                    if group['name_1'] == 'Limit entry add fail':
                        active_dict.setdefault(
                            'limit_entry_add_fail', int(m.groupdict()['number_1']))

                    if group['name_1'] == 'Queued Packets':
                        active_dict.setdefault(
                            'queued_pkts', int(m.groupdict()['number_1']))

                    if group['name_1'] == 'Peak translations':
                        active_dict.setdefault('peak_translations', int(m.groupdict()['number_1']))

                if group['name_2']:
                    
                    if group['name_2'] == 'CEF Punted packets':
                        active_dict.setdefault(
                            'cef_punted_pkts', int(m.groupdict()['number_2']))
                    
                    if group['name_2'] == 'Mapping stats drop':
                        active_dict.setdefault(
                            'mapping_stats_drop', int(m.groupdict()['number_2']))
                    
                    if group['name_2'] == 'Misses':
                        active_dict.setdefault(
                            'misses', int(m.groupdict()['number_2']))
                    
                    if group['name_2'] == 'occurred':
                        active_dict.setdefault(
                            'occurred', m.groupdict()['number_2'])

                continue

            # Dynamic mappings:
            m = p5.match(line)

            # -- Inside Source
            m_1 = p5_1.match(line)
            if m or m_1:
                if m:
                    dynamic_dict = active_dict.setdefault('dynamic_mappings', {})
                
                if m_1:
                    source = m_1.groupdict()['source'].lower() + '_source'
                    source_dict = dynamic_dict.setdefault(source, {})

                continue

            # [Id: 1] access-list 102 pool mypool refcount 3
            # access-list 1 pool net-208 refcount 2
            # [Id: 1] access-list 25 interface FastEthernet1/0 refcount 0
            # [Id: 3] access-list 99 interface Serial0/0 refcount 1
            # [Id: 1] access-list test-robot pool test-robot refcount 0
            # [Id: 3] access-list 99 interface Serial0/0 refcount 1
            m = p6.match(line)
            if m:
                group = m.groupdict()
                if group['id']:
                    source_dict.setdefault('id', int(group['id']))
                
                if group['method'] == 'interface':
                    source_dict.setdefault('interface', group['pool'])

                elif group['method'] == 'pool':
                    pool_dict = source_dict.setdefault('pool', {})

                source_dict.setdefault('access_list', group['access_list'])
                source_dict.setdefault('refcount', int(group['refcount']))

                continue
            
            # pool mypool: netmask 255.255.255.0
            m = p7.match(line)

            # start 10.5.5.1 end 10.5.5.5
            m_1 = p7_1.match(line)

            # type generic, total addresses 5, allocated 1 (20 %), misses 0
            # type generic, total addresses 1, allocated 0 (0 % ), misses 0
            m_2 = p7_2.match(line)

            if m or m_1 or m_2:

                if m:
                    group = m.groupdict()
                    mypool_dict = pool_dict.setdefault(group['pool'], {})
                    mypool_dict.setdefault('netmask', group['netmask'])

                if m_1:
                    group_m1 = m_1.groupdict()

                    mypool_dict.setdefault('start', group_m1['start'])
                    mypool_dict.setdefault('end', group_m1['end'])
                
                if m_2:
                    group_m2 = m_2.groupdict()

                    mypool_dict.setdefault('type', group_m2['type'])
                    mypool_dict.setdefault('total', group_m2['total_addresses'])
                    mypool_dict.setdefault('allocated', group_m2['allocated'])
                    mypool_dict.setdefault('misses', group_m2['misses'])

                continue
                
            # max entry: max allowed 2147483647, used 3, missed 0
            m = p8.match(line)
            if m:
                group = m.groupdict()

                nat_limit_dict = active_dict.setdefault('nat_limit_statistics', {})

                nat_limit_dict.setdefault('max_allowed', int(group['max_allowed']))
                nat_limit_dict.setdefault('used', int(group['used']))
                nat_limit_dict.setdefault('missed', int(group['missed']))

                continue

            # longest chain in pool: pool1's addr-hash: 0, average len 0,chains 0/256
            # longest chain in pool: test-pool1's addr-hash: 0, average len 0,chains 0/256
            m = p9.match(line)
            if m:
                group = m.groupdict()

                mypool_dict.setdefault('addr_hash', int(group['addr_hash']))
                mypool_dict.setdefault(
                    'average_len', int(group['average_len']))
                mypool_dict.setdefault('chains', group['chains'])

                continue

        return parsed_dict
                    
                

                    

                    

