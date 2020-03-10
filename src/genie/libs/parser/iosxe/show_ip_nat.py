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
from genie.metaparser.util.schemaengine import (Schema,
                                                Any,
                                                Optional,
                                                Or,
                                                And,
                                                Default,
                                                Use)

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowIpNatTranslationsSchema(MetaParser):
    """ Schema for the commands:
            * show ip nat translations
            * show ip nat translations verbose
            * show ip nat translations vrf {vrf}
            * show ip nat translations vrf {vrf} verbose
    """

    schema = {
        'vrf': {
            Any(): {  # name of vrf
                'index': {  
                    Any(): {  # 1, 2 ,3, ...
                        'protocol': str,
                        Optional('inside_global'): str,
                        Optional('inside_local'): str,
                        Optional('outside_local'): str,
                        Optional('outside_global'): str,
                        Optional('group_id'): int,
                        Optional('time_left'): str,
                        Optional('details'): {
                            'create': str,
                            'use': str,
                            'timeout': str,
                            'map_id_in': int,
                            'mac_address': str,
                            'input_idb': str,
                            'entry_id': str,
                            'use_count': int,
                        }
                    },
                },
            },
            Optional('number_of_translations'): int
        }
    }


class ShowIpNatTranslations(ShowIpNatTranslationsSchema):
    """
        * show ip nat translations
        * show ip nat translations verbose
        * show ip nat translations vrf {vrf}
        * show ip nat translations vrf {vrf} verbose
    """

    cli_command = ['show ip nat translations',
                   'show ip nat translations verbose',
                   'show ip nat translations vrf {vrf}',
                   'show ip nat translations vrf {vrf} verbose']

    def cli(self, vrf=None, option=None, output=None):
        if output is None:
            if option and vrf is None:
                cmd = self.cli_command[1].format(verbose=option)
            elif option and vrf:
                cmd = self.cli_command[3].format(vrf=vrf, verbose=option)
            elif vrf and option is None:
                cmd = self.cli_command[2].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]

            out = self.device.execute(cmd)
        else:
            out = output

        # udp  10.5.5.1:1025          192.0.2.1:4000 --- ---
        # udp  10.5.5.1:1024          192.0.2.3:4000 --- ---
        # udp  10.5.5.1:1026          192.0.2.2:4000 --- ---
        # --- 172.16.94.209     192.168.1.95 --- ---
        # --- 172.16.94.210     192.168.1.89 --- ---
        # udp 172.16.94.209:1220  192.168.1.95:1220  172.16.169.132:53    172.16.169.132:53
        # tcp 172.16.94.209:11012 192.168.1.89:11012 172.16.196.220:23    172.16.196.220:23
        # tcp 172.16.94.209:1067  192.168.1.95:1067  172.16.196.161:23    172.16.196.161:23
        # icmp 10.10.140.200:66      10.10.40.100:66       10.10.140.110:66      10.10.140.110:66
        # any ---                ---                10.1.0.2          10.144.0.2
        p1 = re.compile(r'^(?P<protocol>-+|udp|tcp|icmp|any) +(?P<inside_global>\S+) '
                        r'+(?P<inside_local>\S+) +(?P<outside_local>\S+) '
                        r'+(?P<outside_global>\S+)$')
        
        # create: 02/15/12 11:38:01, use: 02/15/12 11:39:02, timeout: 00:00:00
        # create 04/09/11 10:51:48, use 04/09/11 10:52:31, timeout: 00:01:00
        p2 = re.compile(r'^create(?:\:)? +(?P<create>[\S ]+), '
                        r'+use(?:\:)? +(?P<use>[\S ]+), +timeout(?:\:)? '
                        r'+(?P<timeout>\S+)$')

        # IOS-XE: 
        # Map-Id(In): 1
        # IOS: 
        # Map-Id(In):1, Mac-Address: 0000.0000.0000 Input-IDB: GigabitEthernet0/3/1
        p3 = re.compile(r'^Map\-Id\(In\)[\:|\s]+(?P<map_id_in>\d+)(?:[\,|\s]'
                        r'+Mac\-Address\: +(?P<mac_address>\S+) +Input\-IDB\: '
                        r'+(?P<input_idb>\S+))?$')

        # IOS-XE: Mac-Address: 0000.0000.0000    Input-IDB: TenGigabitEthernet1/1/0
        p4 = re.compile(r'^Mac-Address: +(?P<mac_address>\S+) +Input-IDB: '
                        r'+(?P<input_idb>\S+)$')

        # entry-id: 0x0, use_count:1
        p5 = re.compile(r'^entry-id: +(?P<entry_id>\S+), '
                        r'+use_count:+(?P<use_count>\d+)$')

        # Total number of translations: 3
        p6 = re.compile(r'^Total +number +of +translations: '
                        r'+(?P<number_of_translations>\d+)$')
        
        # Group_id:0   vrf: genie
        p7 = re.compile(r'^Group_id\:(?P<group_id>\d+) +vrf\: +(?P<vrf_name>\S+)$')

        # Format(H:M:S) Time-left :0:0:-1
        p8 = re.compile(r'^Format\S+ +Time\-left +\:(?P<time_left>\S+)$')

        # initialize variables
        ret_dict = {}
        index_dict = {}
        tmp_dict = {}
        index = 1
        m8_index = 1
        vrf_name = ''
        vrf_flag = False

        for line in out.splitlines():
            line = line.strip()

            # udp  10.5.5.1:1025          192.0.2.1:4000 --- ---
            # udp  10.5.5.1:1024          192.0.2.3:4000 --- ---
            # udp  10.5.5.1:1026          192.0.2.2:4000 --- ---
            # --- 172.16.94.209     192.168.1.95 --- ---
            # --- 172.16.94.210     192.168.1.89 --- ---
            # udp 172.16.94.209:1220  192.168.1.95:1220  172.16.169.132:53    172.16.169.132:53
            # tcp 172.16.94.209:11012 192.168.1.89:11012 172.16.196.220:23    172.16.196.220:23
            # tcp 172.16.94.209:1067  192.168.1.95:1067  172.16.196.161:23    172.16.196.161:23
            # any ---                ---                10.1.0.2          10.144.0.2
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                if 'vrf' in ret_dict:
                    if vrf_flag:
                        protocol_dict = index_dict.setdefault(index, {})
                        protocol_dict.update(group)
                        
                    elif vrf_flag == False and index >= 2:
                        default_dict = vrf_dict.setdefault('default', {})
                        index_dict = default_dict.setdefault('index', {})
                        protocol_dict = index_dict.setdefault(index, {})
                        protocol_dict.update(group)
                        
                        if tmp_dict:
                            default_dict = vrf_dict.setdefault('default', {})
                            index_dict = default_dict.setdefault('index', {})
                            protocol_dict = index_dict.setdefault(index, {})
                            vrf_dict['default']['index'].update(tmp_dict)
                            tmp_dict.clear()

                else:
                    vrf_dict = ret_dict.setdefault('vrf', {})

                    itemp_dict = tmp_dict.setdefault(index, {})

                    itemp_dict.update(group)
                    
                    protocol_dict = index_dict.setdefault(index, {})
                    
                index += 1

                continue
            
            # create: 02/15/12 11:38:01, use: 02/15/12 11:39:02, timeout: 00:00:00
            # create 04/09/11 10:51:48, use 04/09/11 10:52:31, timeout: 00:01:00
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                if protocol_dict:
                    details_dict = protocol_dict.setdefault('details', {})
                    details_dict.update(group)
                        
                else:
                    tmp_details_dict = tmp_dict[1].setdefault('details', {})
                    tmp_details_dict.update(group)

                continue
            
            # IOS-XE: 
            # Map-Id(In): 1
            # IOS: 
            # Map-Id(In):1, Mac-Address: 0000.0000.0000 Input-IDB: GigabitEthernet0/3/1
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()

                if protocol_dict:
                    details_dict.update({'map_id_in': int(group['map_id_in'])})

                    if group['mac_address']:
                        details_dict.update({'mac_address': group['mac_address']})
                    
                    if group['input_idb']:
                        details_dict.update({'input_idb': group['input_idb']})

                else:
                    tmp_details_dict.update(
                        {'mac_address': group['mac_address']})
                    tmp_details_dict.update({'input_idb': group['input_idb']})
                    tmp_details_dict.update(
                        {'map_id_in': int(group['map_id_in'])})

                continue

            # IOS-XE: 
            # Mac-Address: 0000.0000.0000    Input-IDB: TenGigabitEthernet1/1/0
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()

                if protocol_dict:
                    details_dict.update(group)
                else:
                    tmp_details_dict.update(group)

                continue
            
            # entry-id: 0x0, use_count:1
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                if protocol_dict:
                    details_dict.update({'entry_id': group['entry_id']})
                    details_dict.update({'use_count': int(group['use_count'])})

                else:
                    tmp_details_dict.update({'entry_id': group['entry_id']})
                    tmp_details_dict.update(
                        {'use_count': int(group['use_count'])})

                if tmp_dict:
                    default_dict = vrf_dict.setdefault('default', {})
                    index_dict = default_dict.setdefault('index', {})
                    protocol_dict = index_dict.setdefault(index, {})   
                    vrf_dict['default']['index'].update(tmp_dict)
                    tmp_dict.clear()

                continue
            
            # Total number of translations: 3
            m6 = p6.match(line)
            if m6:

                anumber = int(m6.groupdict()['number_of_translations'])
                total_dict = ret_dict.setdefault('vrf', {})
                total_dict.update({'number_of_translations': anumber})

                continue

            # Group_id:0   vrf: genie
            m7 = p7.match(line)
            if m7:
                group = m7.groupdict()
                vrf_name = group['vrf_name']
                if tmp_dict:
                    vrf_name_dict = vrf_dict.setdefault(group['vrf_name'], {})
                    index_dict = vrf_name_dict.setdefault('index', {})
                    tmp_dict[1].update({'group_id': int(group['group_id'])})
                    vrf_flag = True

                else:
                    protocol_dict.update({'group_id': int(group['group_id'])})
                
                continue

            # Format(H:M:S) Time-left :0:0:-1
            m8 = p8.match(line)
            if m8:
                time_left = m8.groupdict()['time_left']
                if tmp_dict:
                    m8_dict = vrf_name_dict.setdefault('index', {})
                    tmp_dict[1].update({'time_left': time_left})
                    vrf_dict[vrf_name]['index'].update(tmp_dict)
                    tmp_dict.clear()
                else:
                    protocol_dict.update({'time_left': time_left})

                continue

        return ret_dict


class ShowIpNatStatisticsSchema(MetaParser):
    """ Schema for command:
            * show ip nat statistics
    """

    schema = {
        'active_translations': {
            'total': int,
            'static': int,
            'dynamic': int,
            'extended': int,
        },
        'interfaces': {
            Optional('outside'): list,
            Optional('inside'): list,
        },
        'hits': int,
        'misses': int,
        Optional('dynamic_mappings'): {
            Any(): {  # 'Inside source'
                'id': {
                    Any(): {  # 0, 1, 2 or 1, 2, 3
                        Optional('match'): str,  # 'access-list 1 pool poo1'
                        Optional('access_list'): str,
                        Optional('route_map'): str,
                        Optional('refcount'): int,
                        Optional('interface'): str,
                        Optional('pool'): {
                            Any(): {  # mypool test-pool
                                'netmask': str,
                                'start': str,
                                'end': str,
                                'type': str,
                                'total_addresses': int,
                                'allocated': int,
                                'allocated_percentage': int,
                                'misses': int,
                                Optional('addr_hash'): int,
                                Optional('average_len'): int,
                                Optional('chains'): str,
                                Optional('id'): int,
                            }
                        }
                    }
                }
            }
        },
        Optional('nat_limit_statistics'): {
            'max_entry': {
                'max_allowed': int,
                'used': int,
                'missed': int,
            }
        },
        Optional('cef_translated_pkts'): int,
        Optional('in_to_out_drops'): int,
        Optional('out_to_in_drops'): int,
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
        Optional('total_doors'): int,
        Optional('appl_doors'): int,
        Optional('normal_doors'): int,
    }
    

class ShowIpNatStatistics(ShowIpNatStatisticsSchema):
    """
        * show ip nat statistics
    """
    # Mapping for integers variables
    INT_MAPPING = {
        'Hits': 'hits',
        'Misses': 'misses',
        'CEF Translated packets': 'cef_translated_pkts',
        'Expired translations': 'expired_translations',
        'Pool stats drop': 'pool_stats_drop',
        'Port block alloc fail': 'port_block_alloc_fail',
        'IP alias add fail': 'ip_alias_add_fail',
        'Limit entry add fail': 'limit_entry_add_fail',
        'Queued Packets': 'queued_pkts',
        'Peak translations': 'peak_translations',
        'CEF Punted packets': 'cef_punted_pkts',
        'Mapping stats drop': 'mapping_stats_drop',
        'In-to-out drops': 'in_to_out_drops',
        'Out-to-in drops': 'out_to_in_drops',
        'Total doors': 'total_doors',
        'Appl doors': 'appl_doors',
        'Normal doors': 'normal_doors',
    }
    
    # Mapping for string variables
    STR_MAPPING = {
        'occurred': 'occurred',
    }

    cli_command = ['show ip nat statistics']

    def cli(self, output=None):

        out = output or self.device.execute(self.cli_command)

        # Total active translations: 0 (0 static, 0 dynamic 0 extended)
        # IOS
        # Total translations: 2 (0 static, 2 dynamic; 0 extended)
        p1 = re.compile(r'^Total(?: +active)? +translations: '
                        r'+(?P<total_translations>\d+) +\((?P<static>\d+) '
                        r'+static\, +(?P<dynamic>\d+) +dynamic\; '
                        r'+(?P<extended>\d+) +extended\)$')

        # Outside interfaces:
        # Inside interfaces:
        # IOS
        # Outside interfaces: Serial0
        # Inside interfaces: Ethernet1
        p2 = re.compile(r'^(?P<in_out_interfaces>Outside|Inside) '
                        r'+interfaces\:(?: +(?P<direction_interfaces>\S+))?$')

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
        # In-to-out drops: 0  Out-to-in drops: 0
        p4 = re.compile(r'^(?P<name_1>[\w|\s|\-]+)\: +(?P<number_1>\w+)'
                        r'(?:[\,|\s*]+(?P<name_2>[\w|\s|\-]+)(?:\:|\s*)? '
                        r'+(?P<number_2>\S+)(?: +ago)?)?$')

        # Dynamic mappings:
        p5 = re.compile(r'^(?P<dynamic>\w+) +mappings\:$')
        
        # -- Inside Source
        p6 = re.compile(r'^\-\- +(?P<source>\S+) +Source$')

        # [Id: 1] access-list 102 pool mypool refcount 3
        # access-list 1 pool net-208 refcount 2
        # [Id: 1] access-list 25 interface FastEthernet1/0 refcount 0
        # [Id: 3] access-list 99 interface Serial0/0 refcount 1
        # [Id: 1] access-list test-robot pool test-robot refcount 0
        # [Id: 3] access-list 99 interface Serial0/0 refcount 1
        # [Id: 1] route-map NAT-MAP pool inside-pool refcount 6
        # [Id: 0] route-map STATIC-MAP
        p7 = re.compile(r'^(?:\[Id\: +(?P<id>\d+)\] )?(?P<access_method>'
                        r'access\-+list|route\-map) +(?P<access_list>[\w\-]+)'
                        r'(?: +(?P<method>pool|interface) +(?P<pool>[\w\/-]+) '
                        r'+refcount +(?P<refcount>\d+))?$')

        # pool mypool: netmask 255.255.255.0
        # pool inside-pool: id 1, netmask 255.255.255.0
        p8 = re.compile(r'^pool +(?P<pool>\S+)\:(?: +(id +(?P<id>\d+))\,)?'
                        r'(?:( +netmask +(?P<netmask>[\d+\.]+))?)$')

        # start 10.5.5.1 end 10.5.5.5
        p9 = re.compile(r'^start +(?P<start>[\d\.]+) +end +(?P<end>[\d\.]+)$')

        # type generic, total addresses 5, allocated 1 (20%), misses 0
        # type generic, total addresses 1, allocated 0 (0%), misses 0
        p10 = re.compile(r'^type +(?P<type>\w+)\, +total +addresses '
                          r'+(?P<total_addresses>\d+)\, +allocated '
                          r'+(?P<allocated>\d+) +\((?P<allocated_percentage>\d+)'
                          r'+\%\)\, +misses +(?P<misses>\d+)$')
                           
        # max entry: max allowed 2147483647, used 3, missed 0
        p11 = re.compile(r'^max +entry\: +max +allowed +(?P<max_allowed>\d+)\, '
                        r'+used +(?P<used>\d+)\, +missed +(?P<missed>\d+)$')
        
        # longest chain in pool: pool1's addr-hash: 0, average len 0,chains 0/256
        # longest chain in pool: test-pool1's addr-hash: 0, average len 0,chains 0/256
        p12 = re.compile(r'^longest +chain +in +pool\: +(?P<pool_name>\S+)\'s '
                        r'+addr\-hash\: +(?P<addr_hash>\d+)\, +average +len '
                        r'(?P<average_len>\d+)\,+chains +(?P<chains>\S+)$')

        parsed_dict = {}
        index = 1
        on_the_outside = False
        on_the_inside = False

        for line in out.splitlines():
            line = line.strip()

            # Total active translations: 0 (0 static, 0 dynamic 0 extended)
            # IOS
            # Total translations: 2 (0 static, 2 dynamic; 0 extended)
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                active_dict = parsed_dict.setdefault('active_translations', {})
                active_dict['total'] = int(group['total_translations'])
                active_dict['static'] = int(group['static'])
                active_dict['dynamic'] = int(group['dynamic'])
                active_dict['extended'] = int(group['extended'])

                continue

            # Outside interfaces:
            # Inside interfaces:
            # IOS
            # Outside interfaces: Serial0
            # Inside interfaces: Ethernet1
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                intf_dict = parsed_dict.setdefault('interfaces', {})
                if group['in_out_interfaces'] == 'Outside':
                    on_the_outside = True
                    on_the_inside = False

                    if group['direction_interfaces']:
                        outside_list = group['direction_interfaces'].split()
                        olist = []
                        for item in outside_list:
                            olist.append(item)

                        if 'outside' in intf_dict:
                            intf_dict['outside'] += olist
                        else:
                            intf_dict['outside'] = olist
                else:
                    on_the_inside = True
                    on_the_outside = False

                    if group['direction_interfaces']:
                        inside_list = group['direction_interfaces'].split()
                        ilist = []
                        for item in inside_list:
                            ilist.append(item)

                        if 'inside' in intf_dict:
                            intf_dict['inside'] += ilist
                        else:
                            intf_dict['inside'] = ilist
                continue

            # TenGigabitEthernet1/0/0, TenGigabitEthernet1/1/0, TenGigabitEthernet1/2/0, TenGigabitEthernet1/3/0
            # FastEthernet0/0
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()

                if on_the_outside:
                    outside_list = group['direction_interfaces'].split()
                    olist = []
                    for item in outside_list:
                        olist.append(item)
                    
                    if 'outside' in intf_dict:
                        intf_dict['outside'] += olist
                    else:
                        intf_dict['outside'] = olist

                elif on_the_inside:
                    inside_list = group['direction_interfaces'].split()
                    ilist = []
                    for item in inside_list:
                        ilist.append(item)

                    if 'inside' in intf_dict:
                        intf_dict['inside'] += ilist
                    else:
                        intf_dict['inside'] = ilist

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
            # In-to-out drops: 0  Out-to-in drops: 0
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                if group['name_1']:
                    if self.INT_MAPPING.get(group['name_1']):
                        name_1 = self.INT_MAPPING.get(group['name_1'])
                        parsed_dict[name_1] = int(group['number_1'])
                    else:
                        name_1 = self.STR_MAPPING.get(group['name_1'])
                        parsed_dict[name_1] = int(group['number_1'])

                if group['name_2']:
                    if self.INT_MAPPING.get(group['name_2']):
                        name_2 = self.INT_MAPPING.get(group['name_2'])
                        parsed_dict[name_2] = int(group['number_2'])
                    else:
                        name_2 = self.STR_MAPPING.get(group['name_2'])
                        parsed_dict[name_2] = group['number_2']

                continue

            # Dynamic mappings:
            m5 = p5.match(line)
            if m5:
                dynamic_dict = parsed_dict.setdefault('dynamic_mappings', {})
                continue

            # -- Inside Source
            m6 = p6.match(line)
            if m6:
                source = m6.groupdict()['source'].lower() + '_source'
                source_dict = dynamic_dict.setdefault(source, {})
                continue

            # [Id: 1] access-list 102 pool mypool refcount 3
            # access-list 1 pool net-208 refcount 2
            # [Id: 1] access-list 25 interface FastEthernet1/0 refcount 0
            # [Id: 3] access-list 99 interface Serial0/0 refcount 1
            # [Id: 1] access-list test-robot pool test-robot refcount 0
            # [Id: 3] access-list 99 interface Serial0/0 refcount 1
            # [Id: 1] route-map NAT-MAP pool inside-pool refcount 6
            # [Id: 0] route-map STATIC-MAP
            m7 = p7.match(line)
            if m7:
                group = m7.groupdict()

                access_name1 = group['access_method'] + ' ' + group['access_list']

                if group['method'] and group['pool']:
                    access_name2 = group['method'] + ' ' + group['pool']
                    access_name = access_name1 + ' ' + access_name2
                else:
                    access_name = access_name1

                if group['id']:
                    id_dict = source_dict.setdefault('id', {})
                    name_dict = id_dict.setdefault(int(group['id']), {})
                else:
                    id_dict = source_dict.setdefault('id', {})
                    name_dict = id_dict.setdefault(index, {})
                    index += 1

                name_dict.update({'match': access_name})
                if 'access-list' == group['access_method']:
                    name_dict.update({'access_list': group['access_list']})
                
                elif 'route-map' == group['access_method']:
                    name_dict.update({'route_map': group['access_list']})

                if group['method'] == 'interface':
                    name_dict.update({'interface': group['pool']})

                elif group['method'] == 'pool':
                    pool_dict = name_dict.setdefault('pool', {})

                if group['refcount']:
                    name_dict.update({'refcount': int(group['refcount'])})

                continue
            
            # pool mypool: netmask 255.255.255.0
            # pool inside-pool: id 1, netmask 255.255.255.0
            m8 = p8.match(line)
            if m8:
                group = m8.groupdict()
                mypool_dict = pool_dict.setdefault(group['pool'], {})
                mypool_dict.update({'netmask': group['netmask']})

                if group['id']:
                    mypool_dict.update({'id': int(group['id'])})
                
                continue
            # start 10.5.5.1 end 10.5.5.5
            m9 = p9.match(line)

            if m9:
                group = m9.groupdict()

                mypool_dict.update({'start': group['start']})
                mypool_dict.update({'end': group['end']})

                continue

            # type generic, total addresses 5, allocated 1 (20 %), misses 0
            # type generic, total addresses 1, allocated 0 (0 % ), misses 0
            m10 = p10.match(line)

            if m10:
                group = m10.groupdict()
                mypool_dict.update({'type': group['type']})
                mypool_dict.update(
                    {'total_addresses': int(group['total_addresses'])})
                mypool_dict.update({'allocated': int(group['allocated'])})
                mypool_dict.update(
                    {'allocated_percentage': int(group['allocated_percentage'])})
                mypool_dict.update({'misses': int(group['misses'])})

                continue
                
            # max entry: max allowed 2147483647, used 3, missed 0
            m11 = p11.match(line)
            if m11:
                group = m11.groupdict()

                max_dict = parsed_dict.setdefault('nat_limit_statistics', {})
                nat_limit_dict = max_dict.setdefault('max_entry', {})
                nat_limit_dict.update({'max_allowed': int(group['max_allowed'])})
                nat_limit_dict.update({'used': int(group['used'])})
                nat_limit_dict.update({'missed': int(group['missed'])})

                continue

            # longest chain in pool: pool1's addr-hash: 0, average len 0,chains 0/256
            # longest chain in pool: test-pool1's addr-hash: 0, average len 0,chains 0/256
            m12 = p12.match(line)
            if m12:
                group = m12.groupdict()

                mypool_dict.update({'addr_hash': int(group['addr_hash'])})
                mypool_dict.update({'average_len': int(group['average_len'])})
                mypool_dict.update({'chains': group['chains']})

                continue
        
        return parsed_dict
