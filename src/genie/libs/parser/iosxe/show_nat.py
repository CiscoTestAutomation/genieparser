'''show_nat.py

IOSXE parser for the following show commands:
   * show nat64 translations
   * show nat64 translations entry-type bind {bind_type}
   * show nat64 translations {pro_port_type} {pro_port}
   * show nat64 translations {ip_type} {address_type} {address}
   * show nat64 translations time created {time_stamp}
   * show nat64 translations entry-type {session}
   * show nat64 translations {verbose}
   * show nat64 pools
   * show nat64 pools {routes}
   * show nat64 pools hsl-id {hsl_id}
   * show nat64 pools hsl-id {hsl_id} {routes}
   * show nat64 pools name {pool_name}
   * show nat64 pools name {pool_name} {routes}
   * show nat64 pools range {pool_start_ip} {upper_range} 
   * show nat64 pools range {pool_start_ip} {upper_range} {routes}
   * show nat64 prefix stateful global
   * show nat64 prefix stateful interfaces,
   * show nat64 prefix stateful interfaces prefix {prefix}
   * show ipv6 nd ra nat64-prefix
   * show nat64 translations vrf {vrf_name}
   * show nat64 prefix stateful static-routes prefix {prefix} vrf {vrf_name}
   * show ip nat redundancy
   * show nat66 statistics
   * show nat66 nd
   * show nat66 prefix
'''
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, ListOf

class ShowNat64TranslationsSchema(MetaParser):
    """Schema for show nat64 translations"""

    schema = {
        'index':{
            Any():{
                'proto': str,
                'original_ipv4': str,                             
                'translated_ipv6': str,
                'translated_ipv4': str,
                'original_ipv6': str,
                Optional('created'): str,
                Optional('last_used'): str,
                Optional('timeout'): int,
                Optional('left'): str,
                Optional('use_count'): int,
                Optional('id'): int,
                Optional('parent_id'): str,
                Optional('config_id'): int                        
            },  
        },
        'total_no_of_translations': int
    }
      
class ShowNat64Translations(ShowNat64TranslationsSchema):
    """
    show nat64 translations
    show nat64 translations entry-type bind {all/static/dynamic}
    show nat64 translations {protocol/port} {tcp/udp/icmp/port_number}
    show nat64 translations {v4/v6} {original/translated} {Ipv4 adddress/Ipv6 address}
    show nat64 translations time created {time_stamp}
    show nat64 translations entry-type {session}
    show nat64 translations {verbose}
    show nat64 translations vrf {vrf_name}
    """

    cli_command = [
                    'show nat64 translations',
                    'show nat64 translations entry-type bind {bind_type}',
                    'show nat64 translations {pro_port_type} {pro_port}',
                    'show nat64 translations {ip_type} {address_type} {address}',
                    'show nat64 translations time created {time_stamp}',
                    'show nat64 translations entry-type {session}',
                    'show nat64 translations {verbose}',
                    'show nat64 translations vrf {vrf_name}'                   
                  ]
    
    def cli(self, 
            bind_type="", 
            pro_port_type="", 
            pro_port="", 
            ip_type="", 
            address_type="", 
            address="", 
            time_stamp="",  
            session="", 
            verbose="", 
            vrf_name="",
            output=None):
        
        if output is None:
            if bind_type:  
                cmd = self.cli_command[1].format(bind_type=bind_type)
            elif pro_port_type:
                cmd = self.cli_command[2].format(pro_port_type=pro_port_type,pro_port=pro_port)
            elif ip_type:
                cmd = self.cli_command[3].format(ip_type=ip_type,address_type=address_type,address=address)
            elif time_stamp:
                cmd = self.cli_command[4].format(time_stamp=time_stamp)
            elif session:
                cmd = self.cli_command[5].format(session=session)
            elif verbose:
                cmd = self.cli_command[6].format(verbose=verbose)
            elif vrf_name:
                cmd = self.cli_command[7].format(vrf_name=vrf_name)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        ret_dict = {}
        
        index = 1
        index_dict = {}

        # Proto Original IPv4   Translated IPv4
        # icmp  1.1.1.2:0       [1001::101:102]:0
        p1 = re.compile(r'^(?P<proto>\S+)\s+(?P<original_ipv4>\S+)\s+(?P<translated_ipv4>\S+)$')
        
        # Translated IPv6 Original IPv6
        # 5.5.5.5:0  [2009::2]:0
        p2 = re.compile(r'^(?P<translated_ipv6>\S+)\s+(?P<original_ipv6>\S+)$')
        
        # created: 3 Jun 2022 16:23:45, last-used: 3 Jun 2022 16:23:45,
        p3 = re.compile(r"^created+: +(?P<created>(.*))\, +last-used+: +(?P<last_used>(.*))$")
        
        # timeout: 300000, left 00:00:02,
        p4 = re.compile(r"^timeout+: +(?P<timeout>\d+)\, +left +(?P<left>(.*))$")
        
        #use_count: 0, id: 44, parent-id(src/dst): 18/27
        p5 = re.compile(r"^use_count+: +(?P<use_count>\d+)\, +id+: +(?P<id>\d+)\,"
                        r" +parent-id\(src/dst\)+: +(?P<parent_id>\d+/\d+)$")
        # use_count: 1, config-id: 18
        p6 = re.compile(r"^use_count+: +(?P<use_count>\d+)\, +config-id+: +(?P<config_id>\d+)$")
        
        # Total number of translations: 3
        p7 = re.compile(r'^Total number of translations+: +(?P<total_no_of_translations>\d+)$')
      
        for line in output.splitlines(): 
            line = line.strip()   
            
            # Proto Original IPv4   Translated IPv4
            # icmp  1.1.1.2:0       [1001::101:102]:0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                index_dict = ret_dict.setdefault('index', {}).setdefault(index,{})
                index_dict['proto'] = group['proto']
                index_dict['original_ipv4'] = group['original_ipv4']
                index_dict['translated_ipv4'] = group['translated_ipv4']
                continue
            
            # Translated IPv6 Original IPv6
            # 5.5.5.5:0  [2009::2]:0     
            m = p2.match(line)
            if m:
                group = m.groupdict()
                index_dict['translated_ipv6'] = group['translated_ipv6']
                index_dict['original_ipv6'] = group['original_ipv6']
                index += 1
                continue
                
            # created: 3 Jun 2022 16:23:45, last-used: 3 Jun 2022 16:23:45,
            m = p3.match(line)
            if m:
                index_dict['created'] = m.groupdict()['created']
                index_dict['last_used'] = m.groupdict()['last_used']
                continue
            
            # timeout: 300000, left 00:00:02,
            m = p4.match(line)
            if m:
                index_dict['timeout'] = int(m.groupdict()['timeout'])
                index_dict['left'] = m.groupdict()['left']
                continue
            
            #use_count: 0, id: 44, parent-id(src/dst): 18/27
            m = p5.match(line)
            if m:
                index_dict['use_count'] = int(m.groupdict()['use_count'])
                index_dict['id'] = int(m.groupdict()['id'])
                index_dict['parent_id'] = m.groupdict()['parent_id']
                continue
            
            # use_count: 1, config-id: 18
            m = p6.match(line)
            if m:
                index_dict['use_count'] = int(m.groupdict()['use_count'])
                index_dict['config_id'] = int(m.groupdict()['config_id'])
                continue
                            
            # Total number of translations: 3
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict['total_no_of_translations'] = int(group['total_no_of_translations'])
                continue
     
        return ret_dict
              
class ShowNat64TimeoutsSchema(MetaParser):
    """show nat64 timeouts"""

    schema = {
        'nat64_timeout': {
            Any(): {
                'cli_cfg': str,
                'seconds': int,
                'uses_all': str
            },
        }
    }

class ShowNat64Timeouts(ShowNat64TimeoutsSchema):
    """ Parser for
       show nat64 timeouts
    """

    cli_command = 'show nat64 timeouts'
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        ret_dict = {}
        
        # Seconds CLI Cfg Uses 'All'
        p1 = re.compile(r'^Seconds +CLI +(?P<cfg>(\w+)) +Uses \'All\'$')
        
        # all flows 
        # udp
        # tcp
        # tcp-transient
        # icmp
        # bind
        p2 = re.compile(r'^(?P<all_flows>(\D+))$')
        
        # 86400 FALSE FALSE
        # 300 FALSE TRUE
        # 7200 FALSE TRUE
        # 240 FALSE FALSE
        # 60 FALSE TRUE
        # 3600 FALSE TRUE
        p3 = re.compile(r'(?P<seconds>(\d+)) +(?P<cli_cfg>(\w+)) +(?P<uses_all>(\w+))')
        
        for line in output.splitlines():
            line = line.strip()
            
            # Seconds CLI Cfg Uses 'All'
            m = p1.match(line)
            if m:
                group = m.groupdict()
                local_dict = ret_dict.setdefault('nat64_timeout', {})
                continue
            
            # all flows 
            # udp
            # tcp
            # tcp-transient
            # icmp
            # bind
            m = p2.match(line)
            if m:
                group = m.groupdict()
                nat_dict = local_dict.setdefault(group['all_flows'], {})
                continue
            
            # 86400 FALSE FALSE
            # 300 FALSE TRUE
            # 7200 FALSE TRUE
            # 240 FALSE FALSE
            # 60 FALSE TRUE
            # 3600 FALSE TRUE
            m = p3.match(line)
            if m:
                group = m.groupdict()
                nat_dict['seconds'] = int(group['seconds'])
                nat_dict['cli_cfg'] = group['cli_cfg']
                nat_dict['uses_all'] = group['uses_all']
                continue
            
        return ret_dict

class ShowNat64StatisticsSchema(MetaParser):
    """show nat64 statistics"""
    
    schema = {
        'nat64_stats': {
            Optional('active_sessions'): int,
            Optional('active_translations'): {
                'dynamic': int,
                'extended': int,
                'static': int,
                'total_translations': int
            },
            Optional('dynamic_mapping_statistics'): {
                'access_list': {
                    Any(): {
                        'pool': {
                            Any(): {
                                'allocated': int,
                                'end_ip': str,
                                'nat64_pool_name': str,
                                'packet_count': int,
                                'percent': int,
                                'start_ip': str,
                                'total_address': int
                            }
                        },
                        'refcount': int
                    }
                }
            },
            Optional('expired_sessions'): int,
            Optional('global_statistics'): {
                'prefix': {
                    Any(): {
                        'packets_dropped': int,
                        'packets_translated': {
                            'v4_to_v6': int,
                            'v6_to_v4': int
                        },
                        Optional('prefix_vrf_name'): str
                    }
                }
            },
            Optional('hits_misses'): {
                'hit_pkts': int, 
                'miss_pkts': int
            },
            Optional('interface_statistics'): {
                Any(): {
                    'stateful_prefix': {
                        Any(): {
                            'packets_dropped': int,
                            'packets_translated': {
                                'v4_to_v6': int,
                                'v6_to_v4': int
                            }
                    },
                    'ipv4': str,
                    'ipv6': str
                    }
                }
            },
            Optional('nat64_enabled_interfaces'): int,
            Optional('number_of_packets'): {
                'cef_punted_pkts': int,
                'cef_translated_pkts': int,
                'dropped_pkts': int,
                Optional('hits_misses'): {
                    'hit_pkts': int,
                    'miss_pkts': int
                }
            }
        }
    }
       
class ShowNat64Statistics(ShowNat64StatisticsSchema):
    """ Parser for
       show nat64 statistics
       show nat64 statistics <global>
       show nat64 statistics mapping <dynamic>
       show nat64 statistics mapping dynamic acl <acl_name>
       show nat64 statistics mapping dynamic pool <pool_name>
       show nat64 statistics interface <interface_name>
    """

    cli_command = [
                    'show nat64 statistics',
                    'show nat64 statistics {global_cmd}',
                    'show nat64 statistics mapping {dynamic}',
                    'show nat64 statistics mapping dynamic acl {acl_name}',
                    'show nat64 statistics mapping dynamic pool {pool_name}',
                    'show nat64 statistics interface {interface_name}'
                  ]

    def cli(self, global_cmd="", dynamic="", acl_name="", pool_name="", interface_name="", output=None):

        if output is None:
            if global_cmd:
                cmd = self.cli_command[1].format(global_cmd=global_cmd)
            elif dynamic:
                cmd = self.cli_command[2].format(dynamic=dynamic)
            elif acl_name:
                cmd = self.cli_command[3].format(acl_name=acl_name)
            elif pool_name:
                cmd = self.cli_command[4].format(pool_name=pool_name)
            elif interface_name:
                cmd = self.cli_command[5].format(interface_name=interface_name)            
            else:
                cmd = self.cli_command[0]
                
            output = self.device.execute(cmd)

        ret_dict = {}
        nat64_dict = {}
        v4v6_dict = {}
        int_dict = {}
        pd_dict = {}
        cef_dict = {}
        state_dict = {}
        
        # Number of NAT64 enabled interfaces: 4
        p1 = re.compile(r'^Number of NAT64 enabled interfaces\: +(?P<nat64_enabled_interfaces>(\d+))')
        
        # Packets translated (IPv4 -> IPv6): 5
        p2 = re.compile(r'^Packets translated \(IPv4 \-\> IPv6\)\: +(?P<v4_to_v6>(\d+)$)')
        
        # Packets translated (IPv6 -> IPv4): 131495
        p3 = re.compile(r'^Packets translated \(IPv6 \-\> IPv4\)\: +(?P<v6_to_v4>(\d+)$)')
        
        # Prefix: 64:FF9B::/96
        p4 = re.compile(r'^Prefix\: +(?P<prefix>(\S+))$')
        
        # Prefix: 2002:1::/96 - vrf nat64_vrf
        p44 = re.compile(r'^Prefix\: +(?P<prefix>(\S+)) \- +vrf+ (?P<prefix_vrf_name>\S+)$')
        
        # Packets dropped: 0
        p5 = re.compile(r'^Packets +dropped+\: +(?P<packets_dropped>\d+)')
        
        # TenGigabitEthernet5/0/12 (IPv4 not configured, IPv6 not configured):
        p6 = re.compile(r'^(?P<interface>(\S+)) +\(IPv4 (?P<ipv4>(\D+)), +IPv6 (?P<ipv6>(\D+))+\)\:')
        
        # Stateful Prefix: 2010:1::/96
        p7 = re.compile(r'^Stateful Prefix\: +(?P<stateful_prefix>(\S+))')
        
        # Total active translations: 2(1 static, 1 dynamic,1 extended)
        # Total active translations: 12(10 static, 1 dynamic,1 extended)
        p8 = re.compile(
            r'^Total active translations+\: +(?P<total_translations>(\d+))\(+(?P<static>(\d+)) +static, +(?P<dynamic>(\d+)) +dynamic,+(?P<extended>(\d+)) +extended')
        
        # Active sessions: 0
        p9 = re.compile(r'^Active sessions\: +(?P<active_sessions>(\d+))')
        
        # Number of expired entries: 0
        p10 = re.compile(r'^Number of expired entries\: +(?P<expired_sessions>(\d+))')
        
        # Hits: 0 Misses: 0
        p11 = re.compile(r'^Hits+\: +(?P<hit_pkts>(\d+))+\s+Misses+\: +(?P<miss_pkts>(\d+))')
        
        # access-list nat64_acl1 pool nat64_v4_pool refcount 0
        p12 = re.compile(r'access-list +(?P<access_list>(\S+)) +pool +(?P<nat64_pool>(\S+)) +refcount +(?P<refcount>(\d+))')
        
        # pool nat64_v4_pool:
        p13 = re.compile(r'pool +(?P<nat64_pool_name>(\S+))\:')
        
        # start 10.0.0.2 end 10.0.0.255
        p14 = re.compile(r'^start (?P<start_ip>([0-9]{1,3}.){3}([0-9]{1,3})) +end +(?P<end_ip>([0-9]{1,3}.){3}([0-9]{1,3}))')
        
        # total addresses 254, allocated 0 (0%)
        p15 = re.compile(
            r'^total addresses +(?P<total_address>(\d+)), +allocated +(?P<allocated>(\d+)) +\(+(?P<percent>(\d+))+\%\)')
        
        # address exhaustion packet count 0
        p16 = re.compile(r'address exhaustion packet count +(?P<packet_count>(\d+))')
        
        # CEF Translated: 0 CEF Punted packets: 0
        p17 = re.compile(r'^CEF +Translated+\: +(?P<cef_translated_pkts>\d+) +CEF Punted packets+\: +(?P<cef_punted_pkts>\d+)')
        
        # Dropped: 3461156
        p18 = re.compile(r'^Dropped+\: +(?P<dropped_pkts>\d+)')
        
        for line in output.splitlines():
            line = line.strip()
        
            # Number of NAT64 enabled interfaces: 4
            m = p1.match(line)
            if m:
                group = m.groupdict()
                nat64_dict = ret_dict.setdefault('nat64_stats', {})
                hit_miss_dict = nat64_dict.setdefault('hits_misses', {})
                nat64_dict['nat64_enabled_interfaces'] = int(group['nat64_enabled_interfaces'])
                continue
        
            # Packets translated (IPv4 -> IPv6): 5
            m = p2.match(line)
            if m:
                group = m.groupdict()
                v4v6_dict['v4_to_v6'] = int(group['v4_to_v6'])
                continue
        
            # Packets translated (IPv6 -> IPv4): 131495
            m = p3.match(line)
            if m:
                group = m.groupdict()
                v4v6_dict['v6_to_v4'] = int(group['v6_to_v4'])
                continue
        
            # Prefix: 64:FF9B::/96
            m = p4.match(line)
            if m:
                group = m.groupdict()
                nat64_dict = ret_dict.setdefault('nat64_stats', {})
                global_dict = nat64_dict.setdefault('global_statistics', {})
                pre_dict = global_dict.setdefault('prefix', {})
                prefix_dict = pre_dict.setdefault(group['prefix'], {})
                v4v6_dict = prefix_dict.setdefault('packets_translated', {})
                continue
                
            # Prefix: 2002:1::/96 - vrf nat64_vrf
            m = p44.match(line)
            if m:
                group = m.groupdict()
                nat64_dict = ret_dict.setdefault('nat64_stats', {})
                global_dict = nat64_dict.setdefault('global_statistics', {})
                pre_dict = global_dict.setdefault('prefix', {})
                prefix_dict = pre_dict.setdefault(group['prefix'], {})
                v4v6_dict = prefix_dict.setdefault('packets_translated', {})
                prefix_dict['prefix_vrf_name'] = group['prefix_vrf_name']
                continue
        
            # Packets dropped: 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                if 'interface_statistics' not in nat64_dict.keys():
                    prefix_dict['packets_dropped'] = int(group['packets_dropped'])
                    continue
                else:
                    state_dict['packets_dropped'] = int(group['packets_dropped'])
                    continue
        
            # TenGigabitEthernet5/0/12 (IPv4 not configured, IPv6 not configured):
            m = p6.match(line)
            if m:
                group = m.groupdict()
                nat64_dict = ret_dict.setdefault('nat64_stats', {})
                interface_dict = nat64_dict.setdefault('interface_statistics', {})
                int_dict = interface_dict.setdefault(str(group['interface']), {})
                stateful_dict = int_dict.setdefault('stateful_prefix', {})
                stateful_dict['ipv4'] = str(group['ipv4'])
                stateful_dict['ipv6'] = str(group['ipv6'])
                continue
        
            # Stateful Prefix: 2010:1::/96
            m = p7.match(line)
            if m:
                group = m.groupdict()
                state_dict = stateful_dict.setdefault(group['stateful_prefix'], {})
                v4v6_dict = state_dict.setdefault('packets_translated', {})
                continue
        
            # Total active translations: 2(1 static, 1 dynamic,1 extended)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                nat64_dict = ret_dict.setdefault('nat64_stats', {})
                trans_dict = nat64_dict.setdefault('active_translations', {})
                trans_dict['total_translations'] = int(group['total_translations'])
                trans_dict['static'] = int(group['static'])
                trans_dict['dynamic'] = int(group['dynamic'])
                trans_dict['extended'] = int(group['extended'])
                continue
        
            # Active sessions: 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                nat64_dict['active_sessions'] = int(group['active_sessions'])
                continue
        
            # Number of expired entries: 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                nat64_dict['expired_sessions'] = int(group['expired_sessions'])
                continue
        
            # Hits: 0 Misses: 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                hit_miss_dict['hit_pkts'] = int(group['hit_pkts'])
                hit_miss_dict['miss_pkts'] = int(group['miss_pkts'])
                continue
        
            # access-list nat64_acl1 pool nat64_v4_pool refcount 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                nat64_dict = ret_dict.setdefault('nat64_stats', {})
                dyn_dict = nat64_dict.setdefault('dynamic_mapping_statistics', {})
                dyn_acl_dict = dyn_dict.setdefault('access_list', {})
                dynamic_dict = dyn_acl_dict.setdefault(group['access_list'], {})
                dynamic_pool = dynamic_dict.setdefault('pool', {})
                dyn_pool_dict = dynamic_pool.setdefault(group['nat64_pool'], {})
                dynamic_dict['refcount'] = int(group['refcount'])
                continue
        
            # pool nat64_v4_pool:
            m = p13.match(line)
            if m:
                group = m.groupdict()
                dyn_pool_dict['nat64_pool_name'] = group['nat64_pool_name']
                continue
        
            # start 10.0.0.2 end 10.0.0.255
            m = p14.match(line)
            if m:
                group = m.groupdict()
                dyn_pool_dict['start_ip'] = group['start_ip']
                dyn_pool_dict['end_ip'] = group['end_ip']
                continue
        
            # total addresses 254, allocated 0 (0%)
            m = p15.match(line)
            if m:
                group = m.groupdict()
                dyn_pool_dict['total_address'] = int(group['total_address'])
                dyn_pool_dict['allocated'] = int(group['allocated'])
                dyn_pool_dict['percent'] = int(group['percent'])
                continue
        
            # address exhaustion packet count 0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                dyn_pool_dict['packet_count'] = int(group['packet_count'])
                continue
        
            # CEF Translated: 0 CEF Punted packets: 0
            m = p17.match(line)
            if m:
                group = m.groupdict()
                cef_dict = nat64_dict.setdefault('number_of_packets', {})
                cef_dict['cef_translated_pkts'] = int(group['cef_translated_pkts'])
                cef_dict['cef_punted_pkts'] = int(group['cef_punted_pkts'])
                hit_miss_dict = cef_dict.setdefault('hits_misses', {})
                continue
        
            # Dropped: 3461156
            m = p18.match(line)
            if m:
                group = m.groupdict()
                cef_dict['dropped_pkts'] = int(group['dropped_pkts'])
                continue
                   
        return ret_dict

class ShowNat64MappingsStaticAddressesSchema(MetaParser):
    """show nat64 mappings static addresses"""
    
    schema = {
        'nat64_mappings': {
            'address': {
                Any(): {
                    'direction': str,
                    'ref_count': int
                }
            }
        }
    }
     
class ShowNat64MappingsStaticAddresses(ShowNat64MappingsStaticAddressesSchema):
    """ Parser for
       show nat64 mappings static addresses
       show nat64 mappings static addresses <ip_address>
       show nat64 mappings static addresses <ipv6_address>
    """

    cli_command = [
                    'show nat64 mappings static addresses',
                    'show nat64 mappings static addresses {ip_address}',
                    'show nat64 mappings static addresses {ipv6_address}'
                  ]

    def cli(self,  ip_address="", ipv6_address="", output=None):

        if output is None:
            if ip_address:
                cmd = self.cli_command[1].format(ip_address=ip_address)
            elif ipv6_address:
                cmd = self.cli_command[2].format(ipv6_address=ipv6_address) 
            else:
                cmd = self.cli_command[0]
                
            output = self.device.execute(cmd)

        ret_dict = {}
    
        # 5.5.5.5
        p1 = re.compile(r'(?P<address>([[0-9]+[:|.]+.*))')
    
        # v6v4      1
        # v6v4      16
        p2 = re.compile(r'(?P<direction>(\S+)) +(?P<ref_count>(\d+))')
        for line in output.splitlines():
            line = line.strip()
    
            # # 5.5.5.5
            m = p1.match(line)
            if m:
                group = m.groupdict()
                domain_dict = ret_dict.setdefault('nat64_mappings', {})
                local_dict = domain_dict.setdefault('address', {})
                nested_dict = local_dict.setdefault(group['address'], {})
                continue
    
            # v6v4      1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                nested_dict['direction'] = group['direction']
                nested_dict['ref_count'] = int(group['ref_count'])
    
                continue
    
        return ret_dict

class ShowNat64MappingsDynamicSchema(MetaParser):
    """show nat64 mappings dynamic"""
    
    schema = {
        'dynamic_mappings': {
            'access_list': {
                Any(): {
                    'dir_id': int,
                    'direction': str,
                    'flags': str,
                    'mapping_id': int,
                    'null': str,
                    'pool': str,
                    'rg_id': int
                }
            },
            Optional('no_of_mappings'): int
        }
    }
     
class ShowNat64MappingsDynamic(ShowNat64MappingsDynamicSchema):
    """ Parser for
       show nat64 mappings dynamic
       show nat64 mappings dynamic id <number>
       show nat64 mappings dynamic list <access_list_name>
       show nat64 mappings dynamic pool <pool_name>
    """

    cli_command = [
                    'show nat64 mappings dynamic',
                    'show nat64 mappings dynamic id {number}',
                    'show nat64 mappings dynamic list {access_list_name}',
                    'show nat64 mappings dynamic pool {pool_name}'
                  ]

    def cli(self, number="", access_list_name="", pool_name="", output=None):

        if output is None:
            if number:
                cmd = self.cli_command[1].format(number=number)
            elif access_list_name:
                cmd = self.cli_command[2].format(access_list_name=access_list_name) 
            elif pool_name:
                cmd = self.cli_command[3].format(pool_name=pool_name)
            else:
                cmd = self.cli_command[0]
                
            output = self.device.execute(cmd)

        ret_dict = {}
        domain_dict = ret_dict.setdefault('dynamic_mappings', {})
        pool_dict = {}
        
        # Dynamic mappings configured: 2
        p1 = re.compile(r'^Dynamic mappings configured\: +(?P<no_of_mappings>(\d+))')
        
        # Direction ID      ACL
        # v6v4      1       acl_1                            NULL
        # v6v4      27       acl_1                            NULL
        p2 = re.compile(r'(?P<direction>(\w+)) +(?P<dir_id>(\d+)) +(?P<acl>(\w+)) +(?P<null>(\w+))')
        
        # Pool                             Flags
        # n64_pool                         0x00000000 0.0.0.0 (none)
        p3 = re.compile(r'(?P<pool>(\S+)) .* +(?P<flags>([0-9x0-9]+ .* +\(none\)))')
        
        # RG ID Mapping ID
        # 0     0
        # RG ID Mapping ID
        # 11     12
        p4 = re.compile(r'(?P<rg_id>(\d+)) +(?P<mapping_id>(\d+))')
        
        for line in output.splitlines():
            line = line.strip()
            
            # Dynamic mappings configured: 2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                domain_dict = ret_dict.setdefault('dynamic_mappings', {})
                domain_dict['no_of_mappings'] = int(group['no_of_mappings'])
                continue
            
            # Direction ID      ACL
            # v6v4      1       acl_1                            NULL
            m = p2.match(line)
            if m:
                group = m.groupdict()
                acl_dict = domain_dict.setdefault('access_list', {})
                pool_dict = acl_dict.setdefault(group['acl'], {})
                pool_dict['direction'] = group['direction']
                pool_dict['dir_id'] = int(group['dir_id'])
                pool_dict['null'] = group['null']
                continue
            
            # Pool                             Flags
            # n64_pool                         0x00000000 0.0.0.0 (none)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                pool_dict['pool'] = group['pool']
                pool_dict['flags'] = group['flags']
                continue
            
            # RG ID Mapping ID
            # 0     0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                pool_dict['rg_id'] = int(group['rg_id'])
                pool_dict['mapping_id'] = int(group['mapping_id'])
                continue
            
        return ret_dict

class ShowNat64StatisticsPrefixStatefulSchema(MetaParser):
    """show nat64 statistics prefix stateful <ipv6>/<prefix_length>"""

    schema = {
        'nat64_statistics': {
            'stateful_prefix': {
                Any(): {
                    'packets_dropped': int,
                    'packets_translated': {
                        'v4_to_v6': int,
                        'v6_to_v4': int
                    }
                }
            }
        }
    }

class ShowNat64StatisticsPrefixStateful(ShowNat64StatisticsPrefixStatefulSchema):
    """ Parser for
       show nat64 statistics prefix stateful <ipv6>/<prefix_length>
    """

    cli_command = [
                    'show nat64 statistics prefix stateful {ipv6_prefix}',
                  ]

    def cli(self, ipv6_prefix="", output=None):

        if output is None:
            if ipv6_prefix:
                cmd = self.cli_command[0].format(ipv6_prefix=ipv6_prefix)
                
        output = self.device.execute(cmd)

    
        ret_dict = {}
        
        # Stateful Prefix: 1001::/96
        p1 = re.compile(r'^Stateful Prefix\: +(?P<stateful_prefix>(\S+))')
        
        # Packets translated (IPv4 -> IPv6): 0
        p2 = re.compile(r'^Packets translated \(IPv4 \-\> IPv6\)\: +(?P<v4_to_v6>(\d+)$)')
        
        # Packets translated (IPv6 -> IPv4): 0
        p3 = re.compile(r'^Packets translated \(IPv6 \-\> IPv4\)\: +(?P<v6_to_v4>(\d+)$)')

        # Packets dropped: 0
        p4 = re.compile(r'^Packets +dropped+\: +(?P<packets_dropped>\d+)')
        
        for line in output.splitlines():
            line = line.strip()
        
            # Stateful Prefix: 1001::/96
            m = p1.match(line)
            if m:
                group = m.groupdict()
                nat_dict = ret_dict.setdefault('nat64_statistics', {})
                stat_dict = nat_dict.setdefault('stateful_prefix', {})
                prefix_dict = stat_dict.setdefault(group['stateful_prefix'], {})
                continue
            
            # Packets translated (IPv4 -> IPv6): 5
            m = p2.match(line)
            if m:
                group = m.groupdict()
                trans_dict = prefix_dict.setdefault('packets_translated', {})
                trans_dict['v4_to_v6'] = int(group['v4_to_v6'])
                continue
            
            # Packets translated (IPv6 -> IPv4): 131495
            m = p3.match(line)
            if m:
                group = m.groupdict()
                trans_dict['v6_to_v4'] = int(group['v6_to_v4'])
                continue
        
            # Packets dropped: 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                prefix_dict['packets_dropped'] = int(group['packets_dropped'])
                continue
                
        return ret_dict

class ShowNat64MappingsStaticSchema(MetaParser):
    """show nat64 mappings static"""
    
    schema = {
        'static_mappings': {
            'index': {
                Any(): {
                    'address': str,
                    'direction': str,
                    'is_valid': str,
                    'mapping_id': int,
                    'non_key_address': str,
                    'protocol': str,
                    'rg_id': int
                }
            },
            'no_of_mappings': int
        }
    }
     
class ShowNat64MappingsStatic(ShowNat64MappingsStaticSchema):
    """ Parser for
           show nat64 mappings static
    """

    cli_command = 'show nat64 mappings static'
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        pool_dict = {}
        index = 1
        index_dict = {}
        
        # Static mappings configured: 1
        p1 = re.compile(r'^Static mappings configured\: +(?P<no_of_mappings>(\d+))')
        
        # Direction Protocol Address (Port, if any)
        # v6v4 --- 2009::2
        p2 = re.compile(r'(?P<direction>(\w+)) +(?P<protocol>(\S+)) +(?P<address>([0-9:].*).*)')
        
        # Non-key Address (Port, if any)
        # 1.1.1.2 (100)
        p3 = re.compile(r'(?P<non_key_address>(\d.+ .*\)))')
        
        # Non-key Address (Port, if any)
        # 2.2.2.2
        p4 = re.compile(r'(?P<non_key_address>([0-9]{1,3}.){3}([0-9]{1,3}))')
        
        # RG ID Mapping ID
        # 0     0          FALSE
        # RG ID Mapping ID
        # 11     12          FALSE
        p5 = re.compile(r'(?P<rg_id>(\d+)) +(?P<mapping_id>(\d+)) +(?P<is_valid>(\w+))')
        
        for line in output.splitlines():
            line = line.strip()
            
            # Dynamic mappings configured: 2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                domain_dict = ret_dict.setdefault('static_mappings', {})
                domain_dict['no_of_mappings'] = int(group['no_of_mappings'])
                continue
        
            # Direction Protocol Address (Port, if any)
            # v6v4 --- 2009::2            
            m = p2.match(line)
            if m:
                group = m.groupdict()
                pool_dict = domain_dict.setdefault('index', {}).setdefault(index, {})
                pool_dict['direction'] = group['direction']
                pool_dict['protocol'] = group['protocol']
                pool_dict['address'] = group['address']
                index = index + 1
                continue
            
            # Non-key Address (Port, if any)
            # 1.1.1.2 (100)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                pool_dict['non_key_address'] = group['non_key_address']
                continue

            # Non-key Address (Port, if any)
            # 2.2.2.2
            m = p4.match(line)
            if m:
                group = m.groupdict()
                pool_dict['non_key_address'] = group['non_key_address']
                continue

            # RG ID Mapping ID
            # 0     0            
            m = p5.match(line)
            if m:
                group = m.groupdict()
                pool_dict['rg_id'] = int(group['rg_id'])
                pool_dict['mapping_id'] = int(group['mapping_id'])
                pool_dict['is_valid'] = group['is_valid']
                continue
                
        return ret_dict
        
class ShowNat64PoolsSchema(MetaParser):
    """Schema for show nat64 pools"""

    schema = {
        Optional('pools_configured'): int,
        Any():{
            Any():{
                'index':{
                    Any():{
                        'protocol': str,
                        'hsl_id': int,
                        'name': str,
                        'is_single': str,
                        'range': str,
                        Optional('ranges'): str,
                        Any():{
                            Optional('static_routes_range'): int,
                            Optional('static_routes'): list
                        }
                    }
                }
            }   
        }    
    }
    
class ShowNat64Pools(ShowNat64PoolsSchema):
    """
    show nat64 pools
    show nat64 pools {routes}
    show nat64 pools hsl-id {hsl_id}
    show nat64 pools hsl-id {hsl_id} {routes}
    show nat64 pools name {pool_name}
    show nat64 pools name {pool_name} {routes}
    show nat64 pools range {pool_start_ip} {upper_range} 
    show nat64 pools range {pool_start_ip} {upper_range} {routes}
    
    """
    cli_command = [
                    'show nat64 pools',
                    'show nat64 pools {routes}',
                    'show nat64 pools hsl-id {hsl_id}',
                    'show nat64 pools hsl-id {hsl_id} {routes}',
                    'show nat64 pools name {pool_name}',
                    'show nat64 pools name {pool_name} {routes}',
                    'show nat64 pools range {pool_start_ip} {upper_range}',
                    'show nat64 pools range {pool_start_ip} {upper_range} {routes}'                    
                  ]
    
    def cli(self, 
            routes="", 
            hsl_id="", 
            pool_name="", 
            pool_start_ip="", 
            upper_range="",            
            output=None):
                        
            if output is None:            
                if routes:
                    if hsl_id:
                        cmd = self.cli_command[3].format(hsl_id=hsl_id,routes=routes)
                    elif pool_name:
                        cmd = self.cli_command[5].format(pool_name=pool_name,routes=routes)
                    elif pool_start_ip and upper_range:
                        cmd = self.cli_command[7].format(pool_start_ip=pool_start_ip,upper_range=upper_range,routes=routes)
                    else:
                        cmd = self.cli_command[1].format(routes=routes)
                else:
                    if hsl_id:
                        cmd = self.cli_command[2].format(hsl_id=hsl_id)
                    elif pool_name:
                        cmd = self.cli_command[4].format(pool_name=pool_name)
                    elif pool_start_ip and upper_range:
                        cmd = self.cli_command[6].format(pool_start_ip=pool_start_ip,upper_range=upper_range)
                    else:
                        cmd = self.cli_command[0]
                output = self.device.execute(cmd)
    
            ret_dict = {}

            index = 1
            index_dict = {}
            
            # Pools configured: 2
            p0 = re.compile(r'^Pools configured+: +(?P<pools_configured>\d+)$')
            
            # Protocol HSL ID     Name
            # IPv4     1          n64_pool
            p1 = re.compile(r'^(?P<protocol>\S+) +(?P<hsl_id>\d+) +(?P<name>\S+)$')
            
            # Is Single        Range
            # TRUE            (135.0.0.1 - 135.0.0.100)
            p2 = re.compile(r'^(?P<is_single>\w+) +(?P<range>\(+[\d.\s -]+\))$')
            
            # Ranges
            # 135.0.0.1 - 135.0.0.100
            p3 = re.compile(r'^(?P<ranges>[\d.\s -]+)$')
            
            # Static Routes for Range: 9
            p4 = re.compile(r'^Static Routes for Range+: +(?P<static_routes_range>\d+)$')
            
            # Static Routes 135.0.0.1/32
            p5 = re.compile(r'^(?P<static_routes>[\d./]+)$')
            
            for line in output.splitlines():
                line = line.strip()
                
                # Pools configured: 2
                m = p0.match(line)
                if m:
                    group = m.groupdict()
                    ret_dict['pools_configured'] = int(group['pools_configured'])
                    continue
    
                # Protocol HSL ID     Name
                # IPv4     1          n64_pool
                m = p1.match(line)
                if m:
                    group = m.groupdict()
                    protocol = group['protocol']
                    protocol = ret_dict.setdefault('protocol', {}).setdefault(protocol, {})
                    index_dict = protocol.setdefault('index', {}).setdefault(index, {})
                    index_dict['protocol'] = group['protocol']
                    index_dict['hsl_id'] = int(group['hsl_id'])
                    index_dict['name'] = group['name']
                    index += 1
                    continue
    
                # Is Single        Range
                # TRUE            (135.0.0.1 - 135.0.0.100)
                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    index_dict['is_single'] = group['is_single']
                    index_dict['range'] = group['range']
                    continue
    
                # Ranges
                # 135.0.0.1 - 135.0.0.100
                m = p3.match(line)
                if m:
                    group = m.groupdict()
                    index_dict['ranges'] = group['ranges']
                    continue
    
                # Static Routes for Range: 9
                m= p4.match(line)
                if m:
                    group = m.groupdict()
                    static_dict = index_dict.setdefault('static_routes_dict', {})
                    static_dict['static_routes_range'] = int(group['static_routes_range'])
                    continue
                    
                # Static Routes 135.0.0.1/32
                m = p5.match(line)
                if m:
                    group = m.groupdict()
                    static_route_dict = static_dict.setdefault('static_routes', [])
                    static_route_dict.append(group['static_routes'])
                    continue
                  
            return ret_dict
        
class ShowNat64PrefixStatefulGlobalSchema(MetaParser):
    """Schema for show nat64 prefix stateful global"""

    schema = {
        'validation': str,
        'prefix': str,
        Optional('prefix_vrf_name'): str,
        Any():{
            'index':{
                Any():{
                    'interface': str,
                    Optional('int_vrf_name'): str
                }
            }
        }   
    }
    
class ShowNat64PrefixStatefulGlobal(ShowNat64PrefixStatefulGlobalSchema):
    """
    show nat64 prefix stateful global
    """

    cli_command = 'show nat64 prefix stateful global'                    
    
    def cli(self, output=None):
        
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        
        index =  1

        # Global Stateful Prefix: is valid, 1001::/96
        p1 = re.compile(r'^Global Stateful Prefix+: is +(?P<validation>(\w+))\, +(?P<prefix>(.*))$')
        
        # Global Stateful Prefix: is not valid
        p2 = re.compile(r'^Global Stateful Prefix+: is +(?P<validation>[\w ]+)$')
        
        # 2002:1::/96 - vrf nat64_vrf
        p22 = re.compile(r'(?P<prefix>[\w\:\.]+[\/]+[\d]+) \- +vrf+ (?P<prefix_vrf_name>\S+)$')
        
        # IFs Using Global Prefix
        # Twe1/0/3
        # Twe1/0/19
        # Twe2/0/9
        p3 = re.compile(r'^(?P<interface>\S+)$')
        
        # IFs Using Global Prefix
        # Te2/2/0/19 - vrf nat64_vrf
        p33 = re.compile(r'^(?P<interface>\S+) \- +vrf+ (?P<int_vrf_name>\S+)$')
        
        for line in output.splitlines():
            line = line.strip()
        
            # Global Stateful Prefix: is valid, 1001::/96
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["validation"] = group["validation"]
                ret_dict["prefix"] = group["prefix"]
                continue
                
            # Global Stateful Prefix: is not valid
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict["validation"] = group["validation"]
                continue
            
            # 2002:1::/96 - vrf nat64_vrf    
            m = p22.match(line)
            if m:
                group = m.groupdict()
                ret_dict["prefix"] = group["prefix"]
                ret_dict["prefix_vrf_name"] = group["prefix_vrf_name"]
                continue
        
            # IFs Using Global Prefix
            # Twe1/0/3
            # Twe1/0/19
            # Twe2/0/9
            m = p3.match(line)
            if m:
                group = m.groupdict()
                prefix_global = ret_dict.setdefault('prefix_global', {})
                index_dict = prefix_global.setdefault('index', {}).setdefault(index,{})
                index_dict['interface'] = group['interface']
                index += 1
                continue
            
            # IFs Using Global Prefix
            # Te2/2/0/19 - vrf nat64_vrf   
            m = p33.match(line)
            if m:
                group = m.groupdict()
                prefix_global = ret_dict.setdefault('prefix_global', {})
                index_dict = prefix_global.setdefault('index', {}).setdefault(index, {})
                index_dict['interface'] = group['interface']
                index_dict['int_vrf_name'] = group['int_vrf_name']
                index += 1
                continue

        return ret_dict
        
class ShowNat64PrefixStatefulInterfacesSchema(MetaParser):
    """Schema for  show nat64 prefix stateful interfaces"""

    schema = {
        Any():{
            'index':{
                Any():{
                    'interface': str,
                    'nat64_enabled': str,
                    'global': str,
                    'prefix': str
                }
            }
        }   
    }
    
class ShowNat64PrefixStatefulInterfaces(ShowNat64PrefixStatefulInterfacesSchema):
    """
    show nat64 prefix stateful interfaces,
    show nat64 prefix stateful interfaces prefix {prefix}
    """

    cli_command = [
                   'show nat64 prefix stateful interfaces',
                   'show nat64 prefix stateful interfaces prefix {prefix}'
                  ]                 
    
    def cli(self, prefix="", output=None):
        
        if output is None:
            if prefix:
                cmd = self.cli_command[1].format(prefix=prefix)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        ret_dict = {}        
        index =  1
        
        # Interface
        # TwentyFiveGigE1/0/19
        p1 = re.compile(r'^(?P<interface>\S+)$')
        
        #  NAT64 Enabled Global Prefix
        #  TRUE          TRUE   1001::/96
        p2 = re.compile(r'^(?P<nat64_enabled>\S+) + (?P<global>\S+) + (?P<prefix>\S+)$')
        
        for line in output.splitlines():
            line = line.strip()

            # Interface
            # TwentyFiveGigE1/0/19
            m = p1.match(line)
            if m:
                group = m.groupdict()
                prefix_interfaces = ret_dict.setdefault('prefix_interfaces', {})
                index_dict = prefix_interfaces.setdefault('index', {}).setdefault(index,{})
                index_dict['interface'] = group['interface']
                continue
                
            #  NAT64 Enabled Global Prefix
            #  TRUE          TRUE   1001::/96
            m = p2.match(line)
            if m:
                group = m.groupdict()
                index_dict['nat64_enabled'] = group['nat64_enabled']
                index_dict['global'] = group['global']
                index_dict['prefix'] = group['prefix']
                index += 1
                continue
       
        return ret_dict
                
class ShowNat64PrefixStatefulStaticRoutesSchema(MetaParser):
    """Schema for  show nat64 prefix stateful static-routes"""

    schema = {
        Any():{
            'index':{
                Any():{
                    'nat64_prefix': str,
                    'static_route_ref_count': int,
                    Optional('vrf_name'): str
                }
            }
        }   
    }
    
class ShowNat64PrefixStatefulStaticRoutes(ShowNat64PrefixStatefulStaticRoutesSchema):
    """
    show nat64 prefix stateful static-routes,
    show nat64 prefix stateful static-routes prefix {prefix}
    show nat64 prefix stateful static-routes prefix {prefix} vrf {vrf_name}
    """

    cli_command = [
                   'show nat64 prefix stateful static-routes',
                   'show nat64 prefix stateful static-routes prefix {prefix}',
                   'show nat64 prefix stateful static-routes prefix {prefix} vrf {vrf_name}'
                  ]                 
    
    def cli(self, prefix="", vrf_name="", output=None):
        
        if output is None:
            if vrf_name and prefix:
                cmd = self.cli_command[2].format(prefix=prefix,vrf_name=vrf_name)
            elif prefix:
                cmd = self.cli_command[1].format(prefix=prefix)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        ret_dict = {}        
        index =  1        
        index_dict = {}
        
        # NAT64 Prefix
        # 1001::/96
        p1 = re.compile(r'^(?P<nat64_prefix>[\w\:\.]+[\/]+[\d]+)$')
        
        # NAT64 Prefix
        # VRF
        # 2002:1::/96 vrf vrf1
        p11 = re.compile(r'^(?P<nat64_prefix>[\w\:\.]+[\/]+[\d]+)+ vrf +(?P<vrf_name>\S+)$')

        # Static Route Ref-Count
        # 1
        p2 = re.compile(r'^(?P<static_route_ref_count>\d+)$')
        
        for line in output.splitlines():
            line = line.strip()

            # NAT64 Prefix
            # 1001::/96
            m = p1.match(line)
            if m:
                group = m.groupdict()
                prefix_static_routes = ret_dict.setdefault('prefix_static_routes', {})
                index_dict = prefix_static_routes.setdefault('index', {}).setdefault(index,{})
                index_dict['nat64_prefix'] = group['nat64_prefix']
                continue
                
            # NAT64 Prefix
            # VRF
            # 2002:1::/96 vrf vrf1
            m = p11.match(line)
            if m:
                group = m.groupdict()
                prefix_static_routes = ret_dict.setdefault('prefix_static_routes', {})
                index_dict = prefix_static_routes.setdefault('index', {}).setdefault(index,{})
                index_dict['nat64_prefix'] = group['nat64_prefix']
                index_dict['vrf_name'] = group['vrf_name']
                continue
                
            # Static Route Ref-Count
            # 1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                index_dict['static_route_ref_count'] = int(group['static_route_ref_count'])
                index += 1
                continue
         
        return ret_dict
        
        
class ShowIpv6NdRaPrefixSchema(MetaParser):
    """Schema for  show ipv6 nd ra nat64-prefix"""

    schema = {
            'index':{
                Any():{
                    'prefix': str,
                    'prefix_length': str,
                    'time': int,
                    'interface': str
                }
            }  
    }
    
class ShowIpv6NdRaPrefix(ShowIpv6NdRaPrefixSchema):
    """
    show ipv6 nd ra nat64-prefix
    """

    cli_command = 'show ipv6 nd ra nat64-prefix'                 
    
    def cli(self, output=None):
        
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}        
        index = 1
        
        # 5000::/32 100  GigabitEthernet29
        p1 = re.compile(r'^(?P<prefix>[\w\:\.]+)\s+(?P<prefix_length>[\/]+[\d]+)\s+(?P<time>\d+)\s+(?P<interface>\S+)$')
        
        for line in output.splitlines():
            line = line.strip()

            # 5000::/32 100  GigabitEthernet29
            m = p1.match(line)
            if m:
                group = m.groupdict()
                index_dict = ret_dict.setdefault('index', {}).setdefault(index, {})
                index_dict['prefix'] = group['prefix']
                index_dict['prefix_length'] = group['prefix_length']
                index_dict['time'] = int(group['time'])
                index_dict['interface'] = group['interface']
                index += 1
                continue
                
        return ret_dict  


class ShowIpNatRedundancySchema(MetaParser):
    """ Schema for 'show ip nat redundancy' """

    schema = {
        "ip": {
            Any(): {
                "name" : str,
                "id": str,
                "use_count": str,
            },
        },
    }

class ShowIpNatRedundancy(ShowIpNatRedundancySchema):
    """ parser for 'show ip nat redundancy' """

    cli_command = "show ip nat redundancy"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output = output
        
        ret_dict = {}
        ip_dict = {}
        
        # 201.201.1.200 hsrp_lan_201         0         1
        p1 = re.compile(r'^\s*(?P<ip>[\>\d\.]+)\s+(?P<name>\w+)\s+(?P<id>\d+)\s+(?P<use_count>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # 201.201.1.200 hsrp_lan_201         0         1
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ip_dict = ret_dict.setdefault('ip', {})
                ip = groups['ip']
                ip_info = ip_dict.setdefault(ip, {})
                ip_info['name'] = groups['name']
                ip_info['id'] = groups['id']
                ip_info['use_count'] = groups['use_count']
                continue

        return ret_dict

class ShowNat66StatisticsSchema(MetaParser):
    """ Schema for 'show nat66 statistics' """

    schema = {
        "nat66_statistics": {
            "global_stats": {
                Optional("enable_count"): int,
                "packets_translated": {
                    "in_to_out": int,
                    "out_to_in": int,
                },
            },
        },
    }


class ShowNat66Statistics(ShowNat66StatisticsSchema):
    """ parser for 'show nat66 statistics' """
    cli_command = "show nat66 statistics"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = dict()
        global_stats_dict = dict()
        # NAT66 Statistics
        p0 = re.compile(r'^NAT66 +Statistics$')
        # Global Stats: enable count 4 or Global Stats:
        p1 = re.compile(r'^Global +Stats: +enable +count +(?P<enable_count>\d+)$')
        # Packets translated (In -> Out)
        #     : 25
        # Packets translated (Out -> In)
        #     : 20
        p2_1 = re.compile(r'^Packets +translated +\(In +\-\> +Out\)$')
        p2_2 = re.compile(r'^Packets +translated +\(Out +\-\> +In\)$')
        p2_3 = re.compile(r'^: +(?P<nat66_pkt_count>\d+)$')
        for line in output.splitlines():
            line = line.strip()
            # NAT66 Statistics
            m = p0.match(line)
            if m:
                global_stats_dict = ret_dict.setdefault('nat66_statistics', {}).setdefault('global_stats', {})
                continue
            # Global Stats: enable count 4
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                global_stats_dict['enable_count'] = int(groups['enable_count'])
                continue
            #    Packets translated (In -> Out)
            #        : 25
            m = p2_1.match(line)
            if m:
                packets_translated_dict = global_stats_dict.setdefault('packets_translated', {})
                in_to_out_flag = True
                continue
            # Packets translated (Out -> In)
            #     : 20
            m = p2_2.match(line)
            if m:
                in_to_out_flag = False
                continue

            m = p2_3.match(line)
            if m:
                groups = m.groupdict()
                if in_to_out_flag:
                    packets_translated_dict['in_to_out'] = int(groups['nat66_pkt_count'])
                else:
                    packets_translated_dict['out_to_in'] = int(groups['nat66_pkt_count'])
                continue
        return ret_dict


class ShowNat66PrefixSchema(MetaParser):
    """ Schema for 'show nat66 prefix' """

    schema = {
        "nat66_prefix": {
            "prefixes_configured": int,
            "ra_prefixes_configured": int,
            "nat66_prefixes": {
                Any(): {
                    "id": int,
                    "inside": str,
                    "outside": str,
                    Optional("vrf"): str,
                },
            },
        },
    }


class ShowNat66Prefix(ShowNat66PrefixSchema):
    """ parser for 'show nat66 prefix' """
    cli_command = "show nat66 prefix"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = dict()
        nat66_prefixes_dict = dict()
        # Prefixes configured: 3
        p1 = re.compile(r'^Prefixes +configured: +(?P<prefixes_configured>\d+)$')
        # RA Prefixes configured: 0
        p2 = re.compile(r'^RA +Prefixes +configured: +(?P<ra_prefixes_configured>\d+)$')
        # Id: 1          Inside FD62:1B53:AFFB:1201::/112 Outside 2001:4888:AFFB:1201::/112
        p3_1 = re.compile(r'^Id: +(?P<id>\d+) +Inside +(?P<inside>[\w\:\/]+) +Outside +(?P<outside>[\w\:\/]+)$')
        # Id: 1          Inside FD62:1B53:AFFB:1201::/112 Outside 2001:4888:AFFB:1201::/112 vrf MPN1201
        p3_2 = re.compile(r'^Id: +(?P<id>\d+) +Inside +(?P<inside>[\w\:\/]+) +Outside +(?P<outside>[\w\:\/]+)( +vrf +(?P<vrf>\S+))?$')

        for line in output.splitlines():
            line = line.strip()
            # Prefixes configured: 3
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                nat66_prefixes_dict = ret_dict.setdefault('nat66_prefix', {})
                nat66_prefixes_dict['prefixes_configured'] = int(groups['prefixes_configured'])
                continue
            # RA Prefixes configured: 0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                nat66_prefixes_dict['ra_prefixes_configured'] = int(groups['ra_prefixes_configured'])
                continue
            # Id: 1          Inside FD62:1B53:AFFB:1201::/112 Outside 2001:4888:AFFB:1201::/112
            m = p3_1.match(line)
            if m:
                groups = m.groupdict()
                nat66_prefix_dict = nat66_prefixes_dict.setdefault('nat66_prefixes', {}).setdefault(groups['id'], {})
                nat66_prefix_dict['id'] = int(groups['id'])
                nat66_prefix_dict['inside'] = groups['inside']
                nat66_prefix_dict['outside'] = groups['outside']
                continue
            # Id: 1          Inside FD62:1B53:AFFB:1201::/112 Outside 2001:4888:AFFB:1201::/112 vrf MPN1201
            m = p3_2.match(line)
            if m:
                groups = m.groupdict()
                nat66_prefix_dict = nat66_prefixes_dict.setdefault('nat66_prefixes', {}).setdefault(groups['id'], {})
                nat66_prefix_dict['id'] = int(groups['id'])
                nat66_prefix_dict['inside'] = groups['inside']
                nat66_prefix_dict['outside'] = groups['outside']
                nat66_prefix_dict['vrf'] = groups['vrf']
                continue
        return ret_dict


class ShowNat66NdSchema(MetaParser):
    """ Schema for 'show nat66 nd' """

    schema = {
        "nat66_nd": {
            Optional("nd_prefix_db"): ListOf(str),
            Optional("ipv6_nd_entries"): ListOf(str),
            Optional("nat66_nd_disabled"): bool,
        },
    }


class ShowNat66Nd(ShowNat66NdSchema):
    """ parser for 'show nat66 nd' """
    cli_command = "show nat66 nd"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = dict()
        nd_prefix_db_list = []
        ipv6_nd_entries_list = []
        disable_flag = False
        # ND Prefix DB:
        # 2001:4888:AFFB:1201::/112
        p1 = re.compile(r'^(?P<nd_prefix_db>[\w\:\/]+)$')
        # IPv6 ND Entries:
        # 2001:4888:AFFB:1201::1
        p2 = re.compile(r'^(?P<ipv6_nd_entries>[\w\:]+)$')
        # NAT66 neighbor discovery is not enabled.
        p3 = re.compile(r'^NAT66 +neighbor +discovery +is +not +enabled.$')


        for line in output.splitlines():
            line = line.strip()
            # IPv6 ND Entries:
            # 2001:4888:AFFB:1201::1
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                ipv6_nd_entries_list.append(groups['ipv6_nd_entries'])
                continue
            # ND Prefix DB:
            # 2001:4888:AFFB:1201::/112
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                nd_prefix_db_list.append(groups['nd_prefix_db'])
                continue
            # NAT66 neighbor discovery is not enabled.
            m = p3.match(line)
            if m:
                disable_flag = True
        if nd_prefix_db_list:
            ret_dict.setdefault('nat66_nd', {}).setdefault('nd_prefix_db', nd_prefix_db_list)
        if ipv6_nd_entries_list:
            ret_dict.setdefault('nat66_nd', {}).setdefault('ipv6_nd_entries', ipv6_nd_entries_list)
        if disable_flag:
            ret_dict.setdefault('nat66_nd', {}).setdefault('nat66_nd_disabled', disable_flag)
        return ret_dict


class ShowPlatformSoftwareFedSwitchActiveNatAclSchema(MetaParser):
    """
    Schema for show platform software fed switch active nat acl
    """
    schema = {
        'index':{
            Any():{
              'type': str,                          
              'protocol': str,
              'src_port': str,
              'dst_port': str, 
              'src_addr': str, 
              'dst_addr': str,                           
            },
        },
        'ace_count': int,
        'oid': str,   
    }
class ShowPlatformSoftwareFedSwitchActiveNatAcl(ShowPlatformSoftwareFedSwitchActiveNatAclSchema):
    """
    show platform software fed switch active nat acl
    """

    cli_command = ['show platform software fed {switch} {mode} nat acl',
                   'show platform software fed active nat acl']           

    def cli(self, switch=None, mode=None, output=None):

        if output is None:
            if switch and mode:
                cmd = self.cli_command[0].format(switch=switch, mode=mode)
            else:
                cmd = self.cli_command[1]
            output = self.device.execute(cmd)

        ret_dict = {}
        index = 1
        index_dict = {}
        #  Type | Protocol | Src Port | Dst Port |        Src Addr |        Dst Addr |
        # ----------------------------------------------------------------------------
        #  SNAT |      any |        - |        - |        12.0.0.0 |         0.0.0.0 |
        #  DNAT |      any |        - |        - |         0.0.0.0 |        36.0.0.2 |
        p0 = re.compile(r'^(?P<type>\S+)\s+\|+\s+(?P<protocol>\S+)\s+\|+\s+(?P<src_port>\S+)\s+\|+\s+(?P<dst_port>\S+)\s+\|+\s+(?P<src_addr>[\d\.]+)\s+\|+\s+(?P<dst_addr>[\d\.]+)\s+\|$')

        # Ace Count : 2
        p1 = re.compile(r'^Ace Count +: +(?P<ace_count>\d+)$')

        # Oid       : 1082
        p2 = re.compile(r'^Oid +: +(?P<oid>\S+)$')

        for line in output.splitlines(): 
            line = line.strip()   

            #  Type | Protocol | Src Port | Dst Port |        Src Addr |        Dst Addr |
            # ----------------------------------------------------------------------------
            #  SNAT |      any |        - |        - |        12.0.0.0 |         0.0.0.0 |
            #  DNAT |      any |        - |        - |         0.0.0.0 |        36.0.0.2 |
            m = p0.match(line)
            if m:
                group = m.groupdict()
                index_dict = ret_dict.setdefault('index', {}).setdefault(index,{})
                index_dict['type'] = group['type']
                index_dict['protocol'] = group['protocol']
                index_dict['src_port'] = group['src_port']
                index_dict['dst_port'] = group['dst_port']
                index_dict['src_addr'] = group['src_addr']
                index_dict['dst_addr'] = group['dst_addr']
                index += 1
                continue
            # Ace Count : 2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['ace_count'] = int(group['ace_count'])
                continue
            # Oid       : 1082
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['oid'] = group['oid']
                continue

        return ret_dict

class ShowPlatformSoftwareFedSwitchActiveNatFlowsSchema(MetaParser):
    """
    Schema for show platform software fed switch active nat flows
    """
    schema = {
        'index':{
            Any():{
              'flow_id': str,                          
              'vrf': str,
              'protocol': str,
              'il_ip_port': str, 
              'ig_ip_port': str, 
              'ol_ip_port': str,  
              'og_ip_port': str,                          
            },
        },
        'no_of_flows': int,  
    }
class ShowPlatformSoftwareFedSwitchActiveNatFlows(ShowPlatformSoftwareFedSwitchActiveNatFlowsSchema):
    """
    show platform software fed switch active nat flows
    """

    cli_command = ['show platform software fed {switch} {mode} nat flows',
                   'show platform software fed active nat flows']     

    def cli(self, switch=None, mode=None, output=None):

        if output is None:
            if switch and mode:
                cmd = self.cli_command[0].format(switch=switch, mode=mode)
            else:
                cmd = self.cli_command[1]
            output = self.device.execute(cmd)

        ret_dict = {}
        index = 1
        index_dict = {}
        #              Flow ID |   VRF | Protocol |          IL_IP : Port |          IG_IP : Port |          OL_IP : Port |          OG_IP : Port |
        # ------------------------------------------------------------------------------------------------------------------------------------------
        #                  0xa |     0 |      tcp |        12.0.0.2:60    |        36.0.0.2:60    |        22.0.0.2:60    |        22.0.0.2:60    |
        #                  0xb |     0 |      udp |        12.0.0.2:63    |        36.0.0.2:63    |        22.0.0.2:63    |        22.0.0.2:63    |
        p0 = re.compile(r'^(?P<flow_id>\w+)\s+\|+\s+(?P<vrf>\d+)\s+\|+\s+(?P<protocol>\S+)\s+\|\s+(?P<il_ip_port>[\d\.\:]+)\s+\|\s+(?P<ig_ip_port>[\d\.\:]+)\s+\|\s+(?P<ol_ip_port>[\d\.\:]+)\s+\|\s+(?P<og_ip_port>[\d\.\:]+)\s+\|$')

        # Number of Flows : 2
        p1 = re.compile(r'^Number of Flows +: +(?P<no_of_flows>\d+)$')

        for line in output.splitlines(): 
            line = line.strip()   

            #              Flow ID |   VRF | Protocol |          IL_IP : Port |          IG_IP : Port |          OL_IP : Port |          OG_IP : Port |
            # ------------------------------------------------------------------------------------------------------------------------------------------
            #                  0xa |     0 |      tcp |        12.0.0.2:60    |        36.0.0.2:60    |        22.0.0.2:60    |        22.0.0.2:60    |
            #                  0xb |     0 |      udp |        12.0.0.2:63    |        36.0.0.2:63    |        22.0.0.2:63    |        22.0.0.2:63    |
            m = p0.match(line)
            if m:
                group = m.groupdict()
                index_dict = ret_dict.setdefault('index', {}).setdefault(index,{})
                index_dict['flow_id'] = group['flow_id']
                index_dict['vrf'] = group['vrf']
                index_dict['protocol'] = group['protocol']
                index_dict['il_ip_port'] = group['il_ip_port']
                index_dict['ig_ip_port'] = group['ig_ip_port']
                index_dict['ol_ip_port'] = group['ol_ip_port']
                index_dict['og_ip_port'] = group['og_ip_port']
                index += 1
                continue
            # Number of Flows : 2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['no_of_flows'] = int(group['no_of_flows'])
                continue
        return ret_dict