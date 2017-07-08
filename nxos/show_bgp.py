''' show_bgp.py

NXOS parsers for the following show commands:
    * 'show bgp process vrf all'
    * 'show bgp process vrf all | xml'
    * 'show bgp peer-session <WORD>'
    * 'show bgp peer-policy <WORD>'
    * 'show bgp peer-template <WORD>'
    * 'show bgp vrf all all'
    * 'show bgp vrf all all neighbors'
    * 'show bgp vrf all all nexthop-database'
    * 'show bgp vrf all all summary'
    * 'show bgp vrf all dampening parameters'
    * 'show bgp vrf all all neighbors <WORD> advertised-routes'
    * 'show bgp vrf all all neighbors <WORD> routes'
    * 'show bgp vrf all all neighbors <WORD> received-routes'
'''

# Python
import re
import xml.etree.ElementTree as ET

# Metaparser
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use


# =====================================
# Parser for 'show bgp process vrf all'
# =====================================

class ShowBgpProcessVrfAllSchema(MetaParser):
    
    '''Schema for show bgp process vrf all'''

    schema = {
        'bgp_pid': int,
        'bgp_protocol_started_reason': str,
        Optional('bgp_performance_mode'): str,
        'bgp_tag': str,
        'bgp_protocol_state': str,
        Optional('bgp_isolate_mode'): str,
        Optional('bgp_mmode'): str,
        'bgp_memory_state': str,
        Optional('bgp_asformat'): str,
        Optional('segment_routing_global_block'): str,
        'num_attr_entries': int,
        'hwm_attr_entries': int,
        'bytes_used': int,
        'entries_pending_delete': int,
        'hwm_entries_pending_delete': int,
        'bgp_paths_per_hwm_attr': int,
        'bgp_as_path_entries': int,
        'bytes_used_as_path_entries': int,
        Optional('vrf'): 
            {Any(): 
                {'vrf_id': str,
                 'vrf_state': str,
                 Optional('router_id'): str,
                 Optional('conf_router_id'): str,
                 Optional('confed_id'): int,
                 Optional('cluster_id'): str,
                 'num_conf_peers': int,
                 'num_pending_conf_peers': int,
                 'num_established_peers': int,
                 Optional('vrf_rd'): str,
                 Optional('address_family'): 
                    {Any(): 
                        {Optional('table_id'): str,
                         Optional('table_state'): str,
                         'peers': 
                            {Any(): 
                                {'active_peers': int,
                                 'routes': int,
                                 'paths': int,
                                 'networks': int,
                                 'aggregates': int,
                                },
                            },
                         Optional('redistribution'): 
                            {Any(): 
                                {Optional('route_map'): str,
                                },
                            },
                         Optional('export_rt_list'): str,
                         Optional('import_rt_list'): str,
                         Optional('label_mode'): str,
                         Optional('aggregate_label'): str,
                         Optional('route_reflector'): bool,
                         Optional('next_hop_trigger_delay'):
                            {'critical': int,
                             'non_critical': int,
                            },
                        Optional('import_default_map'): str,
                        Optional('import_default_prefix_limit'): int,
                        Optional('import_default_prefix_count'): int,
                        Optional('export_default_map'): str,
                        Optional('export_default_prefix_limit'): int,
                        Optional('export_default_prefix_count'): int,
                        },
                    },
                },
            },
        }

class ShowBgpProcessVrfAll(ShowBgpProcessVrfAllSchema):

    '''Parser for show bgp process vrf all'''

    def cli(self):
        out = self.device.execute('show bgp process vrf all')
        
        # Init vars
        parsed_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # BGP Process ID                 : 29474
            p1 = re.compile(r'^\s*BGP +Process +ID *: +(?P<bgp_pid>[0-9]+)$')
            m = p1.match(line)
            if m:
                parsed_dict['bgp_pid'] = int(m.groupdict()['bgp_pid'])
                continue

            # BGP Protocol Started, reason:  : configuration
            p2 = re.compile(r'^\s*BGP Protocol Started, +reason: *:'
                             ' +(?P<reason>[a-zA-Z\s]+)$')
            m = p2.match(line)
            if m:
                parsed_dict['bgp_protocol_started_reason'] = \
                    str(m.groupdict()['reason']).lower()
                continue

            # BGP Performance Mode:          : No
            p2_1 = re.compile(r'^\s*BGP +Performance +Mode *:'
                               ' +(?P<performance_mode>[a-zA-Z\s]+)$')
            m = p2_1.match(line)
            if m:
                parsed_dict['bgp_performance_mode'] = \
                    str(m.groupdict()['performance_mode'])
                continue

            # BGP Protocol Tag               : 100
            p3 = re.compile(r'^\s*BGP +Protocol +Tag *:'
                             ' +(?P<bgp_tag>[a-zA-Z0-9]+)$')
            m = p3.match(line)
            if m:
                parsed_dict['bgp_tag'] = str(m.groupdict()['bgp_tag']).lower()
                continue

            # BGP Protocol State             : Running
            p4 = re.compile(r'^\s*BGP +Protocol +State *:'
                             ' +(?P<protocol_state>[a-zA-Z]+)$')
            m = p4.match(line)
            if m:
                parsed_dict['bgp_protocol_state'] = \
                    str(m.groupdict()['protocol_state']).lower()
                continue

            # BGP Isolate Mode               : No
            p4_1 = re.compile(r'^\s*BGP +Isolate +Mode *:'
                               ' +(?P<isolate_mode>[a-zA-Z\s]+)$')
            m = p4_1.match(line)
            if m:
                parsed_dict['bgp_isolate_mode'] = \
                    str(m.groupdict()['isolate_mode'])
                continue

            # BGP MMODE                      : Initialized
            p4_3 = re.compile(r'^\s*BGP +MMODE *:'
                               ' +(?P<mmode>[a-zA-Z\s]+)$')
            m = p4_3.match(line)
            if m:
                parsed_dict['bgp_mmode'] = str(m.groupdict()['mmode'])
                continue

            # BGP Memory State               : OK
            p5 = re.compile(r'^\s*BGP +Memory +State *:'
                             ' +(?P<memory_state>[a-zA-Z]+)$')
            m = p5.match(line)
            if m:
                parsed_dict['bgp_memory_state'] = \
                    str(m.groupdict()['memory_state']).lower()
                continue

            # BGP asformat                   : asplain
            p5_1 = re.compile(r'^\s*BGP +asformat *:'
                               ' +(?P<asformat>[a-zA-Z\s]+)$')
            m = p5_1.match(line)
            if m:
                parsed_dict['bgp_asformat'] = str(m.groupdict()['asformat'])
                continue

            # Segment Routing Global Block   : 10000-25000
            p5_2 = re.compile(r'^\s*Segment +Routing +Global +Block *:'
                               ' +(?P<segment>[0-9\-]+)$')
            m = p5_2.match(line)
            if m:
                parsed_dict['segment_routing_global_block'] = \
                    str(m.groupdict()['segment'])
                continue

            # BGP attributes information
            # Number of attribute entries    : 4
            p6 = re.compile(r'^\s*Number +of +attribute +entries *:'
                             ' +(?P<num_attr_entries>[0-9]+)$')
            m = p6.match(line)
            if m:
                parsed_dict['num_attr_entries'] = \
                    int(m.groupdict()['num_attr_entries'])
                continue

            # HWM of attribute entries       : 5
            p7 = re.compile(r'^\s*HWM +of +attribute +entries *:'
                             ' +(?P<hwm_attr_entries>[0-9]+)$')
            m = p7.match(line)
            if m:
                parsed_dict['hwm_attr_entries'] = \
                    int(m.groupdict()['hwm_attr_entries'])
                continue

            # Bytes used by entries          : 368
            p8 = re.compile(r'^\s*Bytes +used +by +entries *:'
                             ' +(?P<bytes_used>[0-9]+)$')
            m = p8.match(line)
            if m:
                parsed_dict['bytes_used'] = int(m.groupdict()['bytes_used'])
                continue

            # Entries pending delete         : 0
            p9 = re.compile(r'^\s*Entries +pending +delete *:'
                             ' +(?P<entries_pending_delete>[0-9]+)$')
            m = p9.match(line)
            if m:
                parsed_dict['entries_pending_delete'] = \
                    int(m.groupdict()['entries_pending_delete'])
                continue

            # HWM of entries pending delete  : 0
            p10 = re.compile(r'^\s*HWM +of +entries +pending +delete *:'
                              ' +(?P<hwm_entries_pending_delete>[0-9]+)$')
            m = p10.match(line)
            if m:
                parsed_dict['hwm_entries_pending_delete'] = \
                    int(m.groupdict()['hwm_entries_pending_delete'])
                continue

            # BGP paths per attribute HWM    : 1
            p11 = re.compile(r'^\s*BGP +paths +per +attribute +HWM *:'
                              ' +(?P<bgp_paths_per_hwm_attr>[0-9]+)$')
            m = p11.match(line)
            if m:
                parsed_dict['bgp_paths_per_hwm_attr'] = \
                    int(m.groupdict()['bgp_paths_per_hwm_attr'])
                continue

            # BGP AS path entries            : 0
            p12 = re.compile(r'^\s*BGP +AS +path +entries *:'
                              ' +(?P<bgp_as_path_entries>[0-9]+)$')
            m = p12.match(line)
            if m:
                parsed_dict['bgp_as_path_entries'] = \
                    int(m.groupdict()['bgp_as_path_entries'])
                continue

            # Bytes used by AS path entries  : 0
            p13 = re.compile(r'^\s*Bytes +used +by +AS +path +entries *:'
                              ' +(?P<bytes_used_as_path_entries>[0-9]+)$')
            m = p13.match(line)
            if m:
                parsed_dict['bytes_used_as_path_entries'] = \
                    int(m.groupdict()['bytes_used_as_path_entries'])
                continue

            # BGP Information for VRF VRF1
            p14 = re.compile(r'^\s*BGP +Information +for +VRF'
                              ' +(?P<vrf_name>[a-zA-Z0-9]+)$')
            m = p14.match(line)
            if m:
                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                vrf_name = str(m.groupdict()['vrf_name'])
                if vrf_name not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf_name] = {}
                    continue

            # VRF Id                         : 3
            p15 = re.compile(r'^\s*VRF +Id *:'
                              ' +(?P<vrf_id>[a-zA-Z0-9]+)$')
            m = p15.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['vrf_id'] = \
                    str(m.groupdict()['vrf_id'])
                continue

            # VRF state                      : UP
            p16 = re.compile(r'^\s*VRF +state *:'
                              ' +(?P<vrf_state>[a-zA-Z]+)$')
            m = p16.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['vrf_state'] = \
                    str(m.groupdict()['vrf_state']).lower()
                continue

            # Router-ID                      : 11.11.11.11
            p17 = re.compile(r'^\s*Router-ID *:'
                              ' +(?P<router_id>[0-9\.]+)$')
            m = p17.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['router_id'] = \
                    str(m.groupdict()['router_id'])
                continue

            # Configured Router-ID           : 0.0.0.0
            p18 = re.compile(r'^\s*Configured +Router-ID *:'
                              ' +(?P<conf_router_id>[0-9\.]+)$')
            m = p18.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['conf_router_id'] = \
                    str(m.groupdict()['conf_router_id'])
                continue

            # Confed-ID                      : 0
            p19 = re.compile(r'^\s*Confed-ID *:'
                              ' +(?P<confed_id>[0-9]+)$')
            m = p19.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['confed_id'] = \
                    int(m.groupdict()['confed_id'])
                continue

            # Cluster-ID                     : 0.0.0.0
            p20 = re.compile(r'^\s*Cluster-ID *:'
                              ' +(?P<cluster_id>[0-9\.]+)$')
            m = p20.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['cluster_id'] = \
                    str(m.groupdict()['cluster_id'])
                continue

            # No. of configured peers        : 1
            p21 = re.compile(r'^\s*No. +of +configured +peers *:'
                              ' +(?P<num_conf_peers>[0-9]+)$')
            m = p21.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['num_conf_peers'] = \
                    int(m.groupdict()['num_conf_peers'])
                continue
            
            # No. of pending config peers    : 0
            p22 = re.compile(r'^\s*No. +of +pending +config +peers *:'
                              ' +(?P<num_pending_conf_peers>[0-9]+)$')
            m = p22.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['num_pending_conf_peers'] = \
                    int(m.groupdict()['num_pending_conf_peers'])
                continue
            
            # No. of established peers       : 0
            p23 = re.compile(r'^\s*No. +of +established +peers *:'
                              ' +(?P<num_established_peers>[0-9]+)$')
            m = p23.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['num_established_peers'] = \
                    int(m.groupdict()['num_established_peers'])
                continue
            
            # VRF RD                         : 100:100
            p24 = re.compile(r'^\s*VRF +RD *:'
                              ' +(?P<vrf_rd>[a-zA-Z0-9\:\s]+)$')
            m = p24.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['vrf_rd'] = \
                    str(m.groupdict()['vrf_rd']).lower()
                continue

            #     Information for address family IPv4 Unicast in VRF VRF1
            p25 = re.compile(r'^\s*Information +for +address +family'
                               ' +(?P<address_family>[a-zA-Z0-9\s]+)'
                               ' +in +VRF +(?P<vrf>[a-zA-Z0-9]+)$')
            m = p25.match(line)
            if m:
                if 'address_family' not in parsed_dict['vrf'][vrf_name]:
                    parsed_dict['vrf'][vrf_name]['address_family'] = {}

                address_family = str(m.groupdict()['address_family']).lower()
                
                vrf = str(m.groupdict()['vrf'])

                if address_family not in parsed_dict['vrf'][vrf_name]\
                    ['address_family'] and vrf == vrf_name:
                    parsed_dict['vrf'][vrf_name]['address_family']\
                        [address_family] = {}
                    continue

            #     Table Id                   : 10
            #     Table Id                   : 0x80000001
            p26 = re.compile(r'^\s*Table +Id *: +(?P<table_id>(\S+))$')
            m = p26.match(line)
            if m:
                table_id = str(m.groupdict()['table_id'])
                if '0x' in table_id:
                    parsed_dict['vrf'][vrf_name]['address_family']\
                        [address_family]['table_id'] = table_id
                else:
                    parsed_dict['vrf'][vrf_name]['address_family']\
                        [address_family]['table_id'] = '0x' + table_id
                continue
            
            #     Table state                : UP
            p27 = re.compile(r'^\s*Table +state *: +(?P<table_state>[a-zA-Z]+)$')
            m = p27.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                    ['table_state'] = str(m.groupdict()['table_state']).lower()
                continue

            #     Peers      Active-peers    Routes     Paths      Networks   Aggregates
            #     1          0               5          5          1          2      
            p28 = re.compile(r'^\s*(?P<peers>[0-9]+) +(?P<active_peers>[0-9]+)'
                              ' +(?P<routes>[0-9]+) +(?P<paths>[0-9]+)'
                              ' +(?P<networks>[0-9]+) +(?P<aggregates>[0-9]+)$')
            m = p28.match(line)
            if m:
                if 'peers' not in parsed_dict['vrf'][vrf_name]\
                    ['address_family'][address_family]:
                    parsed_dict['vrf'][vrf_name]['address_family']\
                        [address_family]['peers'] = {}

                peers = int(m.groupdict()['peers'])

                if peers not in parsed_dict['vrf'][vrf_name]['address_family']\
                    [address_family]['peers']:
                    parsed_dict['vrf'][vrf_name]['address_family']\
                        [address_family]['peers'][peers] = {}
                    parsed_dict['vrf'][vrf_name]['address_family']\
                        [address_family]['peers'][peers]['active_peers'] = \
                            int(m.groupdict()['active_peers'])
                    parsed_dict['vrf'][vrf_name]['address_family']\
                        [address_family]['peers'][peers]['routes'] = \
                            int(m.groupdict()['routes'])
                    parsed_dict['vrf'][vrf_name]['address_family']\
                        [address_family]['peers'][peers]['paths'] = \
                            int(m.groupdict()['paths'])
                    parsed_dict['vrf'][vrf_name]['address_family']\
                        [address_family]['peers'][peers]['networks'] = \
                            int(m.groupdict()['networks'])
                    parsed_dict['vrf'][vrf_name]['address_family']\
                        [address_family]['peers'][peers]['aggregates'] = \
                            int(m.groupdict()['aggregates'])
                    continue

            #     Redistribution                
            #         direct, route-map genie_redistribution
            #         static, route-map genie_redistribution
            #         eigrp, route-map test-map
            p29 = re.compile(r'^\s*(?P<name>[a-zA-Z]+),'
                              ' +route-map +(?P<route_map>[a-zA-Z\-\_]+)$')
            m = p29.match(line)
            if m:
                if 'redistribution' not in parsed_dict['vrf'][vrf_name]\
                    ['address_family'][address_family]:
                    parsed_dict['vrf'][vrf_name]['address_family']\
                        [address_family]['redistribution'] = {}

                name = str(m.groupdict()['name']).lower()

                if name not in parsed_dict['vrf'][vrf_name]['address_family']\
                    [address_family]['redistribution']:
                    parsed_dict['vrf'][vrf_name]['address_family']\
                        [address_family]['redistribution'][name] = {}
                    parsed_dict['vrf'][vrf_name]['address_family']\
                        [address_family]['redistribution'][name]\
                            ['route_map'] = str(m.groupdict()['route_map'])
                    continue
            
            #     Export RT list: 100:100
            p30 = re.compile(r'^\s*Export +RT +list *:'
                              ' +(?P<export_rt_list>[0-9\:]+)$')
            m = p30.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                    ['export_rt_list'] = str(m.groupdict()['export_rt_list'])
                continue

            #     Import RT list: 100:100
            p31 = re.compile(r'^\s*Import +RT +list *:'
                              ' +(?P<import_rt_list>[0-9\:]+)$')
            m = p31.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                    ['import_rt_list'] = str(m.groupdict()['import_rt_list'])
                continue

            #     Label mode: per-prefix
            p32 = re.compile(r'^\s*Label +mode *: +(?P<label_mode>[a-zA-Z\-]+)$')
            m = p32.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                    ['label_mode'] = str(m.groupdict()['label_mode'])
                continue

            #     Aggregate label: 492287
            p33 = re.compile(r'^\s*Aggregate +label *:'
                              ' +(?P<aggregate_label>[a-zA-Z0-9\-]+)$')
            m = p33.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                    ['aggregate_label'] = str(m.groupdict()['aggregate_label'])
                continue

            # Import default limit       : 1000
            p34 = re.compile(r'^\s*Import +default +limit *:'
                              ' +(?P<import_default_prefix_limit>[0-9]+)$')
            m = p34.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                    ['import_default_prefix_limit'] = \
                        int(m.groupdict()['import_default_prefix_limit'])
                continue

            # Import default prefix count : 3
            p35 = re.compile(r'^\s*Import +default +prefix +count *:'
                              ' +(?P<import_default_prefix_count>[0-9]+)$')
            m = p35.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                    ['import_default_prefix_count'] = \
                        int(m.groupdict()['import_default_prefix_count'])

            # Import default map         : PERMIT_ALL_RM
            p36 = re.compile(r'^\s*Import +default +map *:'
                              ' +(?P<import_default_map>[a-zA-Z0-9\_\-]+)$')
            m = p36.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                    ['import_default_map'] = \
                        str(m.groupdict()['import_default_map'])

            # Export default limit       : 1000
            p37 = re.compile(r'^\s*Export +default +limit *:'
                              ' +(?P<export_default_prefix_limit>[0-9]+)$')
            m = p37.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                    ['export_default_prefix_limit'] = \
                        int(m.groupdict()['export_default_prefix_limit'])

            # Export default prefix count : 2
            p38 = re.compile(r'^\s*Export +default +prefix +count *:'
                              ' +(?P<export_default_prefix_count>[0-9]+)$')
            m = p38.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                    ['export_default_prefix_count'] = \
                        int(m.groupdict()['export_default_prefix_count'])

            # Export default map         : PERMIT_ALL_RM
            p39 = re.compile(r'^\s*Export +default +map *:'
                              ' +(?P<export_default_map>[a-zA-Z0-9\_\-]+)$')
            m = p39.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                    ['export_default_map'] = \
                        str(m.groupdict()['export_default_map'])

            # Nexthop trigger-delay
            p40 = re.compile(r'^\s*Nexthop +trigger-delay$')
            m = p40.match(line)
            if m:
                if 'next_hop_trigger_delay' not in parsed_dict['vrf'][vrf_name]\
                    ['address_family'][address_family]:
                    parsed_dict['vrf'][vrf_name]['address_family']\
                        [address_family]['next_hop_trigger_delay'] = {}

            # critical 3000 ms
            p41 = re.compile(r'^\s*critical +(?P<critical>[0-9]+) +ms$')
            m = p41.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['address_family']\
                    [address_family]['next_hop_trigger_delay']['critical'] = \
                    int(m.groupdict()['critical'])

            # non-critical 3000 ms
            p42 = re.compile(r'^\s*non-critical +(?P<non_critical>[0-9]+) +ms$')
            m = p42.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['address_family']\
                    [address_family]['next_hop_trigger_delay']['non_critical'] = \
                        int(m.groupdict()['non_critical'])

        return parsed_dict

    def xml(self):
        out = self.device.execute('show bgp process vrf all | xml')

        etree_dict = {}
        # Remove junk characters returned by the device
        out = out.replace("]]>]]>", "")
        output = ET.fromstring(out)

        for item in output:
            for data in item:
                for show in data:
                    for bgp in show:
                        for __XML__OPT_Cmd_show_ip_bgp_session_cmd_vrf in bgp:
                            for process in __XML__OPT_Cmd_show_ip_bgp_session_cmd_vrf:
                                for __XML__OPT_Cmd_show_bgp_process_cmd_vrf in process:
                                    for __XML__OPT_Cmd_show_bgp_process_cmd___readonly__ in __XML__OPT_Cmd_show_bgp_process_cmd_vrf:
                                        for key in __XML__OPT_Cmd_show_bgp_process_cmd___readonly__:
                                            # Get key text
                                            text = key.tag[key.tag.find('}')+1:]
                                            # bgp_pid
                                            if text == 'processid':
                                                etree_dict['bgp_pid'] = int(key.text)
                                            # bgp_protocol_started_reason
                                            if text == 'protocolstartedreason':
                                                etree_dict['bgp_protocol_started_reason'] = key.text
                                            # bgp_tag
                                            if text == 'protocoltag':
                                                etree_dict['bgp_tag'] = key.text
                                            # bgp_protocol_state
                                            if text == 'protocolstate':
                                                etree_dict['bgp_protocol_state'] = str(key.text).lower()
                                            # bgp_isolate_mode
                                            if text == 'isolatemode':
                                                etree_dict['bgp_isolate_mode'] = key.text
                                            # bgp_mmode
                                            if text == 'mmode':
                                                etree_dict['bgp_mmode'] = key.text
                                            # bgp_memory_state
                                            if text == 'memorystate':
                                                etree_dict['bgp_memory_state'] = str(key.text).lower()
                                            # bgp_performance_mode
                                            if text == 'forwardingstatesaved':
                                                state = key.text
                                                if state == 'false':
                                                    etree_dict['bgp_performance_mode'] = 'No'
                                                else:
                                                    etree_dict['bgp_performance_mode'] = 'Yes'
                                            # bgp_asformat
                                            if text == 'asformat':
                                                etree_dict['bgp_asformat'] = key.text
                                            if text == 'srgbmin':
                                                srgbin = key.text
                                            if text == 'srgbmax':
                                                srgmax = key.text
                                                try:
                                                    etree_dict['segment_routing_global_block'] = srgbin + '-' + srgmax
                                                except:
                                                    pass
                                            # num_attr_entries
                                            if text == 'attributeentries':
                                                etree_dict['num_attr_entries'] = int(key.text)
                                            # hwm_attr_entries
                                            if text == 'hwmattributeentries':
                                                etree_dict['hwm_attr_entries'] = int(key.text)
                                            # bytes_used
                                            if text == 'bytesused':
                                                etree_dict['bytes_used'] = int(key.text)
                                            # entries_pending_delete
                                            if text == 'entriespendingdelete':
                                                etree_dict['entries_pending_delete'] = int(key.text)
                                            # hwm_entries_pending_delete
                                            if text == 'hwmentriespendingdelete':
                                                etree_dict['hwm_entries_pending_delete'] = int(key.text)
                                            # bgp_paths_per_hwm_attr
                                            if text == 'pathsperattribute':
                                                etree_dict['bgp_paths_per_hwm_attr'] = int(key.text)
                                            # bgp_as_path_entries
                                            if text == 'aspathentries':
                                                etree_dict['bgp_as_path_entries'] = int(key.text)
                                            # bytes_used_as_path_entries
                                            if text == 'aspathbytes':
                                                etree_dict['bytes_used_as_path_entries'] = int(key.text)
                                            
                                            if text == 'TABLE_vrf':
                                                for table_vrf in key:
                                                    for row_vrf in table_vrf:
                                                        vrf_tag = row_vrf.tag[row_vrf.tag.find('}')+1:]

                                                        # vrf
                                                        #   vrf_name
                                                        if vrf_tag == 'vrf-name-out':
                                                            vrf_name = row_vrf.text
                                                            if 'vrf' not in etree_dict:
                                                                etree_dict['vrf'] = {}
                                                            if vrf_name not in etree_dict['vrf']:
                                                                etree_dict['vrf'][vrf_name] = {}
                                                                vrf_dict = etree_dict['vrf'][vrf_name]
                                                        # vrf_id
                                                        if vrf_tag == 'vrf-id':
                                                            vrf_dict['vrf_id'] = row_vrf.text
                                                        # vrf_state
                                                        if vrf_tag == 'vrf-state':
                                                            vrf_dict['vrf_state'] = row_vrf.text
                                                        # router_id
                                                        if vrf_tag == 'vrf-router-id':
                                                            vrf_dict['router_id'] = row_vrf.text
                                                        # conf_router_id
                                                        if vrf_tag == 'vrf-cfgd-id':
                                                            vrf_dict['conf_router_id'] = row_vrf.text
                                                        # confed_id
                                                        if vrf_tag == 'vrf-confed-id':
                                                            vrf_dict['confed_id'] = int(row_vrf.text)
                                                        # cluster_id
                                                        if vrf_tag == 'vrf-cluster-id':
                                                           vrf_dict['cluster_id'] = row_vrf.text
                                                        # num_conf_peers
                                                        if vrf_tag == 'vrf-peers':
                                                            vrf_dict['num_conf_peers'] = int(row_vrf.text)
                                                        # num_pending_conf_peers
                                                        if vrf_tag == 'vrf-pending-peers':
                                                            vrf_dict['num_pending_conf_peers'] = int(row_vrf.text)
                                                        # num_established_peers
                                                        if vrf_tag == 'vrf-est-peers':
                                                            vrf_dict['num_established_peers'] = int(row_vrf.text)
                                                        # vrf_rd
                                                        if vrf_tag == 'vrf-rd':
                                                            vrf_dict['vrf_rd'] = row_vrf.text

                                                        if vrf_tag == 'TABLE_af':
                                                            for table_af in row_vrf:
                                                                for row_af in table_af:
                                                                    af_tag = row_af.tag[row_af.tag.find('}')+1:]

                                                                    # address_family
                                                                    #   address_family_name
                                                                    if af_tag == 'af-name':
                                                                        address_family_name = str(row_af.text).lower()
                                                                        if 'address_family' not in etree_dict['vrf'][vrf_name]:
                                                                            etree_dict['vrf'][vrf_name]['address_family'] = {}
                                                                        if address_family_name not in etree_dict['vrf'][vrf_name]['address_family']:
                                                                            etree_dict['vrf'][vrf_name]['address_family'][address_family_name] = {}
                                                                            af_dict = etree_dict['vrf'][vrf_name]['address_family'][address_family_name]
                                                                        # Initialize empty lists
                                                                        export_rt_list = ''
                                                                        import_rt_list = ''
                                                                    # table_id
                                                                    if af_tag == 'af-table-id':
                                                                        table_id = str(row_af.text)
                                                                        if '0x' in table_id:
                                                                            af_dict['table_id'] = table_id
                                                                        else:
                                                                            af_dict['table_id'] = '0x' + table_id
                                                                    # table_state
                                                                    if af_tag == 'af-state':
                                                                        af_dict['table_state'] = str(row_af.text).lower()
                                                                    # peers
                                                                    if af_tag == 'af-num-peers':
                                                                        peers = int(row_af.text)
                                                                        if 'peers' not in af_dict:
                                                                            af_dict['peers'] = {}
                                                                        if peers not in af_dict['peers']:
                                                                            af_dict['peers'][peers] = {}
                                                                    # active_peers
                                                                    if af_tag == 'af-num-active-peers':
                                                                        af_dict['peers'][peers]['active_peers'] = int(row_af.text)
                                                                    # routes
                                                                    if af_tag == 'af-peer-routes':
                                                                        af_dict['peers'][peers]['routes'] = int(row_af.text)
                                                                    # paths
                                                                    if af_tag == 'af-peer-paths':
                                                                        af_dict['peers'][peers]['paths'] = int(row_af.text)
                                                                    # networks
                                                                    if af_tag == 'af-peer-networks':
                                                                        af_dict['peers'][peers]['networks'] = int(row_af.text)
                                                                    # aggregates
                                                                    if af_tag == 'af-peer-aggregates':
                                                                        af_dict['peers'][peers]['aggregates'] = int(row_af.text)
                                                                    # route_reflector
                                                                    if af_tag == 'af-rr':
                                                                        if row_af.text == 'false':
                                                                            af_dict['route_reflector'] = False
                                                                        elif row_af.text == 'true':
                                                                            af_dict['route_reflector'] = True
                                                                    # next_hop_trigger_delay
                                                                    #   critical
                                                                    if af_tag == 'nexthop-trigger-delay-critical':
                                                                        if 'next_hop_trigger_delay' not in af_dict:
                                                                            af_dict['next_hop_trigger_delay'] = {}
                                                                        af_dict['next_hop_trigger_delay']['critical'] = int(row_af.text)
                                                                    # next_hop_trigger_delay
                                                                    #   non_critical
                                                                    if af_tag == 'nexthop-trigger-delay-non-critical':
                                                                        af_dict['next_hop_trigger_delay']['non_critical'] = int(row_af.text)
                                                                    # aggregate_label
                                                                    if af_tag == 'af-aggregate-label':
                                                                        af_dict['aggregate_label'] = row_af.text
                                                                    # label_mode
                                                                    if af_tag == 'af-label-mode':
                                                                        af_dict['label_mode'] = row_af.text
                                                                    # import_default_map
                                                                    if af_tag == 'importdefault_map':
                                                                        af_dict['import_default_map'] = row_af.text
                                                                    # import_default_prefix_limit
                                                                    if af_tag == 'importdefault_prefixlimit':
                                                                        af_dict['import_default_prefix_limit'] = int(row_af.text)
                                                                    # import_default_prefix_count
                                                                    if af_tag == 'importdefault_prefixcount':
                                                                        af_dict['import_default_prefix_count'] = int(row_af.text)
                                                                    # export_default_map
                                                                    if af_tag == 'exportdefault_map':
                                                                        af_dict['export_default_map'] = row_af.text
                                                                    # export_default_prefix_limit
                                                                    if af_tag == 'exportdefault_prefixlimit':
                                                                        af_dict['export_default_prefix_limit'] = int(row_af.text)
                                                                    # export_default_prefix_count
                                                                    if af_tag == 'exportdefault_prefixcount':
                                                                        af_dict['export_default_prefix_count'] = int(row_af.text)

                                                                    # TABLE_redist
                                                                    #   ROW_redist
                                                                    if af_tag == 'TABLE_redist':
                                                                        for table_redist in row_af:
                                                                            for row_redist in table_redist:
                                                                                row_redist_tag = row_redist.tag[row_redist.tag.find('}')+1:]
                                                                                # protocol
                                                                                if row_redist_tag == 'protocol':
                                                                                    protocol = row_redist.text
                                                                                    if 'redistribution' not in af_dict:
                                                                                        af_dict['redistribution'] = {}
                                                                                    if protocol not in af_dict['redistribution']:
                                                                                        af_dict['redistribution'][protocol] = {}
                                                                                # route_map
                                                                                if row_redist_tag == 'route-map':
                                                                                    af_dict['redistribution'][protocol]['route_map'] = row_redist.text

                                                                    # TABLE_evpn_export_rt
                                                                    #   ROW_evpn_export_rt
                                                                    if af_tag == 'TABLE_evpn_export_rt':
                                                                        for table_evpn_export in row_af:
                                                                            for row_export in table_evpn_export:
                                                                                row_export_tag = row_export.tag[row_export.tag.find('}')+1:]
                                                                                # export_rt_list
                                                                                if row_export_tag == 'evpn-export-rt':
                                                                                    export_rt_list = str(export_rt_list + ' ' + row_export.text).strip()
                                                                                    af_dict['export_rt_list'] = export_rt_list
                                                                    # TABLE_evpn_import_rt
                                                                    #   ROW_evpn_import_rt
                                                                    if af_tag == 'TABLE_evpn_import_rt':
                                                                        for table_evpn_import in row_af:
                                                                            for row_import in table_evpn_import:
                                                                                row_import_tag = row_import.tag[row_import.tag.find('}')+1:]
                                                                                # export_rt_list
                                                                                if row_import_tag == 'evpn-import-rt':
                                                                                    import_rt_list = str(import_rt_list + ' ' + row_import.text).strip()
                                                                                    af_dict['import_rt_list'] = import_rt_list

                                                                    # parsed all tags
                                                                    continue
                                                                                    
        return etree_dict

        
# =========================================
# Parser for 'show bgp peer-session <WORD>'
# =========================================

class ShowBgpPeerSessionSchema(MetaParser):
    
    '''Schema for show bgp peer-session <WORD>'''

    schema = {
        'peer_session': 
            {Any(): 
                {Optional('shutdown'): bool,
                 Optional('update_source'): str,
                 Optional('description'): str,
                 Optional('password'): bool,
                 Optional('ebgp_multihop_enable'): bool,
                 Optional('ebgp_multihop_limit'): int,
                 Optional('disable_connectivity_check'): bool,
                 Optional('suppress_capabilities'): bool,
                 Optional('transport_connection_mode'): str,
                 Optional('holdtime'): int,
                 Optional('keepalive'): int,
                 Optional('remote_as'): bool,
                 Optional('local_as'): bool,
                 Optional('bfd'): bool,
                 Optional('inherited_vrf_default'): str,
                },
            },
        }

class ShowBgpPeerSession(ShowBgpPeerSessionSchema):

    '''Parser for show bgp peer-session <WORD>
       Executing 'show running-config bgp | inc peer-session' to colllect
       configured peer-session names.
    '''

    def cli(self):
        
        # Execute 'show running' command to collect peer-sessions
        cmd = 'show running-config | inc peer-session'
        out = self.device.execute(cmd)
        
        # Init vars
        peer_sessions = []
        parsed_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # template peer-session PEER-SESSION
            p1 = re.compile(r'^\s*template +peer-session '
                             '+(?P<session_name>[a-zA-Z\-\_]+)$')
            m = p1.match(line)
            if m:
                # Create top level key
                if 'peer_session' not in parsed_dict:
                    parsed_dict['peer_session'] = {}
                # Get session name and save it for later
                peer_sessions.append(str(m.groupdict()['session_name']))
                continue

        if peer_sessions:
            
            # Execute bgp show command now
            for session in peer_sessions:
                
                # Create session key
                if session not in parsed_dict['peer_session']:
                    parsed_dict['peer_session'][session] = {}
                    sub_dict = parsed_dict['peer_session'][session]
                
                base_cmd = 'show bgp peer-session ' + session
                cmd = base_cmd
                out = self.device.execute(cmd)

                for line in out.splitlines():
                    line = line.rstrip()

                    # Commands configured in this template:
                    # Shutdown
                    r1 = re.compile(r'^\s*Shutdown$')
                    m = r1.match(line)
                    if m:
                        sub_dict['shutdown'] = True
                        continue
                  
                    # Update Source - interface: loopback0
                    r2 = re.compile(r'^\s*Update +Source +-'
                                     ' +(?P<update_source>[a-zA-Z0-9\:\s]+)$')
                    m = r2.match(line)
                    if m:
                        sub_dict['update_source'] = \
                            str(m.groupdict()['update_source']).lower()
                        continue
                  
                    # Description - description: PEER-SESSION
                    r3 = re.compile(r'^\s*Description +- +description *:'
                                     ' +(?P<desc>[a-zA-Z\-]+)$')
                    m = r3.match(line)
                    if m:
                        sub_dict['description'] = \
                            str(m.groupdict()['desc'])
                        continue
                  
                    # Password
                    r4 = re.compile(r'^\s*Password$')
                    m = r4.match(line)
                    if m:
                        sub_dict['password'] = True
                        continue
                  
                    # EBGP Multihop - hop limit: 255
                    r5 = re.compile(r'^\s*EBGP +Multihop +- +hop +limit *:'
                                     ' +(?P<ebgp_multihop_limit>[0-9]+)$')
                    m = r5.match(line)
                    if m:
                        sub_dict['ebgp_multihop_enable'] = True
                        sub_dict['ebgp_multihop_limit'] = \
                            int(m.groupdict()['ebgp_multihop_limit'])
                        continue
                  
                    # Disable Connectivity Check
                    r6 = re.compile(r'^\s*Disable +Connectivity +Check$')
                    m = r6.match(line)
                    if m:
                        sub_dict['disable_connectivity_check'] = True
                        continue
                    
                    # Suppress Capabilities
                    r7 = re.compile(r'^\s*Suppress +Capabilities$')
                    m = r7.match(line)
                    if m:
                        sub_dict['suppress_capabilities'] = True
                        continue
                  
                    # Passive Only
                    r8 = re.compile(r'^\s*Passive Only$')
                    m = r8.match(line)
                    if m:
                        sub_dict['transport_connection_mode'] = 'Passive'
                        continue
                  
                    # Timers - hold time: 111, keepalive: 222
                    r9 = re.compile(r'^\s*Timers +- +hold +time *:'
                                     ' +(?P<holdtime>[0-9]+), keepalive *:'
                                     ' +(?P<keepalive>[0-9]+)$')
                    m = r9.match(line)
                    if m:
                        sub_dict['holdtime'] = int(m.groupdict()['holdtime'])
                        sub_dict['keepalive'] = int(m.groupdict()['keepalive'])
                        continue
                    
                    # Remote AS
                    r10 = re.compile(r'^\s*Remote AS$')
                    m = r10.match(line)
                    if m:
                        sub_dict['remote_as'] = True
                        continue
                  
                    # Local AS
                    r11 = re.compile(r'^\s*Local AS$')
                    m = r11.match(line)
                    if m:
                        sub_dict['local_as'] = True
                        continue
                  
                    # Enable Bfd
                    r12 = re.compile(r'^\s*Enable Bfd$')
                    m = r12.match(line)
                    if m:
                        sub_dict['bfd'] = True
                        continue
                
                    # Inherited commands:
                    # Inherited by the following peers:
                    # VRF default: 2.2.2.5
                    r13 = re.compile(r'^\s*VRF +default *:'
                                     ' +(?P<vrf_default>[0-9\.]+)$')
                    m = r13.match(line)
                    if m:
                        sub_dict['inherited_vrf_default'] = \
                            str(m.groupdict()['vrf_default'])
                        continue

        # Return parsed output
        return parsed_dict


# ========================================
# Parser for 'show bgp peer-policy <WORD>'
# ========================================

class ShowBgpPeerPolicySchema(MetaParser):
    
    '''Schema for show bgp peer-policy <WORD>'''

    schema = {
        'peer_policy': 
            {Any(): 
                {Optional('send_community'): bool,
                 Optional('send_ext_community'): bool,
                 Optional('route_reflector_client'): bool,
                 Optional('route_map_name_in'): str,
                 Optional('route_map_name_out'): str,
                 Optional('maximum_prefix_max_prefix_no'): int,
                 Optional('default_originate'): bool,
                 Optional('default_originate_route_map'): str,
                 Optional('soft_reconfiguration'): bool,
                 Optional('site_of_origin'): bool,
                 Optional('allowas_in'): bool,
                 Optional('as_override'): bool,
                 Optional('inherited_vrf_default'): str,
                 Optional('next_hop_self'): bool,
                },
            },
        }

class ShowBgpPeerPolicy(ShowBgpPeerPolicySchema):

    '''Parser for show bgp peer-policy <WORD>
       Executing 'show running-config bgp | inc peer-policy' to colllect
       configured peer-policy names.
    '''

    def cli(self):
        
        # Execute 'show running' command to collect peer-sessions
        cmd = 'show running-config | inc peer-policy'
        out = self.device.execute(cmd)
        
        # Init vars
        policy_names = []
        parsed_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # template peer-policy PEER-POLICY
            p1 = re.compile(r'^\s*template +peer-policy'
                             ' +(?P<policy_name>[a-zA-Z0-9\-\_]+)$')
            m = p1.match(line)
            if m:
                # Get session name and save it for later
                policy_names.append(str(m.groupdict()['policy_name']))
                
                # Create top level key
                if 'peer_policy' not in parsed_dict:
                    parsed_dict['peer_policy'] = {}
                
                continue

        if policy_names:
            
            # Execute bgp show command now
            for policy_name in policy_names:
                
                # Create policy_name key
                if policy_name not in parsed_dict['peer_policy']:
                    parsed_dict['peer_policy'][policy_name] = {}
                    sub_dict = parsed_dict['peer_policy'][policy_name]
                
                base_cmd = 'show bgp peer-policy ' + policy_name
                cmd = base_cmd
                out = self.device.execute(cmd)

                for line in out.splitlines():
                    line = line.rstrip()

                    # Commands configured in this template:
                    # Send Community
                    r1 = re.compile(r'^\s*Send +Community$')
                    m = r1.match(line)
                    if m:
                        sub_dict['send_community'] = True
                        continue
                  
                    # Send Ext-community
                    r2 = re.compile(r'^\s*Send +Ext-community$')
                    m = r2.match(line)
                    if m:
                        sub_dict['send_ext_community'] = True
                        continue
                  
                    # Route Reflector Client
                    r3 = re.compile(r'^\s*Route +Reflector +Client$')
                    m = r3.match(line)
                    if m:
                        sub_dict['route_reflector_client'] = True
                        continue
                  
                    # Route-map Inbound - policy-name: test-map
                    r4 = re.compile(r'^\s*Route-map +Inbound +- +policy-name *:'
                                     ' +(?P<inbound_name>[a-zA-Z\-]+)$')
                    m = r4.match(line)
                    if m:
                        sub_dict['route_map_name_in'] = \
                            str(m.groupdict()['inbound_name'])
                        continue
                  
                    # Route-map Outbound - policy-name: test-map
                    r5 = re.compile(r'^\s*Route-map +Outbound +- +policy-name *:'
                                     ' +(?P<outbound_name>[a-zA-Z\-]+)$')
                    m = r5.match(line)
                    if m:
                        sub_dict['route_map_name_out'] = \
                            str(m.groupdict()['outbound_name'])
                  
                    # Maximum Prefixes - prefix limit: 300
                    r6 = re.compile(r'^\s*Maximum +Prefixes +- +prefix +limit *:'
                                     ' +(?P<max_prefix_no>[0-9]+)$')
                    m = r6.match(line)
                    if m:
                        sub_dict['maximum_prefix_max_prefix_no'] = \
                            int(m.groupdict()['max_prefix_no'])
                        continue
                    
                    # Default Originate - route-map: test
                    r7 = re.compile(r'^\s*Default +Originate(?: +- +route-map *:'
                                     ' +(?P<route_map>[a-zA-Z]+))?$')
                    m = r7.match(line)
                    if m:
                        sub_dict['default_originate'] =  True
                        sub_dict['default_originate_route_map'] = \
                            str(m.groupdict()['route_map'])
                        continue
                  
                    # Soft-Reconfig
                    r8 = re.compile(r'^\s*Soft-Reconfig$')
                    m = r8.match(line)
                    if m:
                        sub_dict['soft_reconfiguration'] = True
                        continue
                  
                    # Site-of-origin
                    r9 = re.compile(r'^\s*Site-of-origin$')
                    m = r9.match(line)
                    if m:
                        sub_dict['site_of_origin'] = True
                        continue
                    
                    # Allowas-in
                    r10 = re.compile(r'^\s*Allowas-in$')
                    m = r10.match(line)
                    if m:
                        sub_dict['allowas_in'] = True
                        continue
                  
                    # AS-override
                    r11 = re.compile(r'^\s*AS-override$')
                    m = r11.match(line)
                    if m:
                        sub_dict['as_override'] = True
                        continue
                
                    # Inherited commands:
                    # Inherited by the following peers:
                    # VRF default: 2.2.2.5
                    r12 = re.compile(r'^\s*VRF +default *:'
                                     ' +(?P<vrf_default>[0-9\.]+)$')
                    m = r12.match(line)
                    if m:
                        sub_dict['inherited_vrf_default'] = \
                            str(m.groupdict()['vrf_default'])
                        continue

                    # Nexthop Self
                    r13 = re.compile(r'^\s*Nexthop +Self$')
                    m = r13.match(line)
                    if m:
                        sub_dict['next_hop_self'] = True
                        continue

        # Return parsed output
        return parsed_dict


# ==========================================
# Parser for 'show bgp peer-template <WORD>'
# ==========================================

class ShowBgpPeerTemplateSchema(MetaParser):

    '''Schema for show bgp peer-template <WORD>'''

    schema = {
        'peer_template':
            {Any():
                {Optional('remote_as'): int,
                Optional('inherit_template'): str,
                Optional('description'): str,
                Optional('update_source'): str,
                Optional('disable_connected_check'): bool,
                Optional('bfd_live_detection'): bool,
                Optional('num_hops_bgp_peer'): int,
                Optional('tcp_md5_auth'): str,
                Optional('nbr_transport_connection_mode'): str,
                Optional('nbr_local_as_cmd'): str,
                Optional('private_as_updates'): bool,
                Optional('holdtime'): int,
                Optional('keepalive_interval'): int,
                },
            },
        }

class ShowBgpPeerTemplate(ShowBgpPeerTemplateSchema):

    '''Parser for show bgp peer-template <WORD>
       Executing 'show running-config bgp | inc peer' to colllect
       configured peer-template names.
    '''

    def cli(self):
        
        # Execute 'show running' command to collect peer templates
        cmd = 'show running-config | inc peer'
        out = self.device.execute(cmd)
        
        # Init vars
        peer_templates = []
        parsed_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # template peer PEER
            p1 = re.compile(r'^\s*template +peer'
                             ' +(?P<peer_template>[a-zA-Z0-9\-\_]+)$')
            m = p1.match(line)
            if m:
                # Get session name and save it for later
                peer_templates.append(str(m.groupdict()['peer_template']))
                
                # Create top level key
                if 'peer_template' not in parsed_dict:
                    parsed_dict['peer_template'] = {}
                continue

        if peer_templates:
            
            # Execute bgp show command now
            for peer_template in peer_templates:
                
                # Create template_names key
                if peer_template not in parsed_dict['peer_template']:
                    parsed_dict['peer_template'][peer_template] = {}
                    sub_dict = parsed_dict['peer_template'][peer_template]
                
                base_cmd = 'show bgp peer-template ' + peer_template
                cmd = base_cmd
                out = self.device.execute(cmd)

                for line in out.splitlines():
                    line = line.rstrip()

                    # BGP peer-template is PEER
                    # Remote AS 500
                    p1 = re.compile(r'^\s*Remote +AS +(?P<remote_as>[0-9]+)$')
                    m = p1.match(line)
                    if m:
                        sub_dict['remote_as'] = int(m.groupdict()['remote_as'])
                        continue

                    # Inherits session configuration from session-template PEER-SESSION
                    p2 = re.compile(r'^\s*Inherits +session +configuration'
                                     ' +from session-template'
                                     ' +(?P<inherit_template>(\S+))$')
                    m = p2.match(line)
                    if m:
                        sub_dict['inherit_template'] = \
                            str(m.groupdict()['inherit_template'])
                        continue

                    # Description: DESC
                    p3 = re.compile(r'^\s*Description *: +(?P<desc>(\S+))$')
                    m = p3.match(line)
                    if m:
                        sub_dict['description'] = str(m.groupdict()['desc'])
                        continue

                    # Using loopback1 as update source for this peer
                    p4 = re.compile(r'^\s*Using +(?P<update_source>(\S+)) +as'
                                     ' +update +source +for +this +peer$')
                    m = p4.match(line)
                    if m:
                        sub_dict['update_source'] = \
                            str(m.groupdict()['update_source'])
                        continue

                    # Connected check is disabled
                    p5 = re.compile(r'^\s*Connected check is disabled$')
                    m = p5.match(line)
                    if m:
                        sub_dict['disable_connected_check'] = True
                        continue

                    # BFD live-detection is configured
                    p6 = re.compile(r'^\s*BFD live-detection is configured$')
                    m = p6.match(line)
                    if m:
                        sub_dict['bfd_live_detection'] = True
                        continue

                    # External BGP peer might be upto 255 hops away
                    p7 = re.compile(r'^\s*External +BGP +peer +might +be +upto'
                                     ' +(?P<num_hops_bgp_peer>[0-9]+) +hops'
                                     ' +away$')
                    m = p7.match(line)
                    if m:
                        sub_dict['num_hops_bgp_peer'] = \
                            int(m.groupdict()['num_hops_bgp_peer'])
                        continue

                    # TCP MD5 authentication is enabled
                    p8 = re.compile(r'^\s*TCP +MD5 +authentication +is'
                                     ' +(?P<tcp_md5_auth>(\S+))$')
                    m = p8.match(line)
                    if m:
                        sub_dict['tcp_md5_auth'] = \
                            str(m.groupdict()['tcp_md5_auth'])
                        continue

                    # Only passive connection setup allowed
                    p9 = re.compile(r'^\s*Only +passive +connection +setup'
                                     ' +allowed$')
                    m = p9.match(line)
                    if m:
                        sub_dict['nbr_transport_connection_mode'] = 'Passive'
                        continue

                    # Neighbor local-as command not active
                    p10 = re.compile(r'^\s*Neighbor +local-as +command'
                                      ' +(?P<nbr_local_as_cmd>(\S+))$')
                    m = p10.match(line)
                    if m:
                        sub_dict['nbr_local_as_cmd'] = \
                            str(m.groupdict()['nbr_local_as_cmd'])
                        continue

                    # Private AS numbers removed from updates sent to this neighbor
                    p11 = re.compile(r'^\s*Private +AS +numbers +removed +from'
                                      ' +updates +sent +to +this +neighbor$')
                    m = p11.match(line)
                    if m:
                        sub_dict['private_as_updates'] = False
                        continue

                    # Hold time = 26, keepalive interval is 13 seconds
                    p12 = re.compile(r'^\s*Hold +time += +(?P<holdtime>[0-9]+),'
                                      ' +keepalive +interval +is'
                                      ' +(?P<keepalive_interval>[0-9]+)'
                                      ' +seconds$')
                    m = p12.match(line)
                    if m:
                        sub_dict['holdtime'] = \
                            int(m.groupdict()['holdtime'])
                        sub_dict['keepalive_interval'] = \
                            int(m.groupdict()['keepalive_interval'])
                        continue


        # Return parsed output
        return parsed_dict

# =================================
# Parser for 'show bgp vrf all all'
# =================================

class ShowBgpVrfAllAllSchema(MetaParser):
    
    '''Schema for show bgp vrf all all'''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'bgp_table_version': int,
                         'local_router_id': str,
                         Optional('route_distinguisher'): str,
                         Optional('default_vrf'): str,
                         Optional('aggregate_address_ipv4_address'): str,
                         Optional('aggregate_address_ipv4_mask'): str,
                         Optional('aggregate_address_as_set'): bool,
                         Optional('aggregate_address_summary_only'): bool,
                         Optional('v6_aggregate_address_ipv6_address'): str,
                         Optional('v6_aggregate_address_as_set'): bool,
                         Optional('v6_aggregate_address_summary_only'): bool,
                         Optional('prefixes'):
                            {Any(): 
                                {'index': 
                                    {Any(): 
                                        {'next_hop': str,
                                         Optional('status_codes'): str,
                                         Optional('path_type'): str,
                                         'metric': str,
                                         'localprf': str,
                                         'weight': str,
                                         'origin_codes': str,
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }

class ShowBgpVrfAllAll(ShowBgpVrfAllAllSchema):
    
    '''Parser for show bgp vrf all all'''

    def cli(self):
        cmd = 'show bgp vrf all all'
        out = self.device.execute(cmd)
        
        # Init vars
        parsed_dict = {}
        af_dict = {}
        data_on_nextline = False
        index = 1
        for line in out.splitlines():
            line = line.rstrip()

            # BGP routing table information for VRF VRF1, address family IPv4 Unicast
            p1 = re.compile(r'^\s*BGP +routing +table +information +for +VRF'
                             ' +(?P<vrf_name>[a-zA-Z0-9\-]+), +address +family'
                             ' +(?P<address_family>[a-zA-Z0-9\s]+)$')
            m = p1.match(line)
            if m:
                route_distinguisher = default_vrf = ''
                # Get values
                vrf = str(m.groupdict()['vrf_name'])
                address_family = str(m.groupdict()['address_family']).lower()
                continue

            # BGP table version is 35, local router ID is 11.11.11.11
            # BGP table version is 381, Local Router ID is 1.1.1.2
            p2 = re.compile(r'^\s*BGP +table +version +is'
                             ' +(?P<bgp_table_version>[0-9]+), +(L|l)ocal'
                             ' +(R|r)outer +ID +is +(?P<local_router_id>[0-9\.]+)$')
            m = p2.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                local_router_id = str(m.groupdict()['local_router_id'])
                continue

            # Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
            # Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist
            # Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath
            # Network            Next Hop         Metric   LocPrf   Weight Path

            # *>a11.0.0.0/8       0.0.0.0                  100      32768 i
            # *>i33.33.33.33/32   3.3.3.3         0        100          0 ?
            # l34.34.34.0/24      0.0.0.0                  100      32768 i
            # *>i2001::33/128     ::ffff:3.3.3.3  0        100          0 ?
            # *>l[2]:[0]:[0]:[48]:[0000.1986.6d99]:[0]:[0.0.0.0]/216
            # *>i                 21.0.0.2        0        100          0 ?
            p3 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                             '(?P<path_type>(i|e|c|l|a|r))'
                             '(?P<prefix>[a-zA-Z0-9\.\:\/\[\]]+)?'
                             '(?: *(?P<next_hop>[a-zA-Z0-9\.\:]+))?'
                             '(?: +(?P<metric>[0-9]+))?'
                             '(?: +(?P<localprf>[0-9]+) +(?P<weight>[0-9]+))?'
                             '(?: +(?P<origin_codes>(i|e|\?|\|)))?$')
            m = p3.match(line)
            if m:
                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf] = {}
                    parsed_dict['vrf'][vrf]['address_family'] = {}
                    af_dict = parsed_dict['vrf'][vrf]['address_family']
                if address_family not in af_dict:
                    af_dict[address_family] = {}

                if 'RD' in address_family:
                    af_dict[address_family]['route_distinguisher'] = route_distinguisher
                    af_dict[address_family]['default_vrf'] = default_vrf

                af_dict[address_family]['bgp_table_version'] = bgp_table_version
                af_dict[address_family]['local_router_id'] = local_router_id


                # Get keys
                status_codes = str(m.groupdict()['status_codes'])
                path_type = str(m.groupdict()['path_type'])
                last_prefix = str(m.groupdict()['prefix'])
                next_hop = str(m.groupdict()['next_hop'])
                metric = str(m.groupdict()['metric']).strip()
                localprf = str(m.groupdict()['localprf'])
                weight = str(m.groupdict()['weight'])
                origin_codes = str(m.groupdict()['origin_codes'])

                # Check prefixes top level key exists
                if 'prefixes' not in af_dict[address_family]:
                    af_dict[address_family]['prefixes'] = {}
                
                if last_prefix != 'None':
                    prefix = last_prefix
                    # if network is L2VPN EVPN, index = 0
                    if next_hop != 'None':
                        index = 1
                    else:
                        index = 0

                # Check if the prefix exists
                if prefix not in af_dict[address_family]['prefixes']:
                    af_dict[address_family]['prefixes'][prefix] = {}
                
                # Check if index top level key exists
                if 'index' not in af_dict[address_family]['prefixes']\
                    [prefix]:
                    af_dict[address_family]['prefixes'][prefix]\
                        ['index'] = {}

                # Check if current prefix details are on next line
                if next_hop == 'None':
                    data_on_nextline = True
                    continue

                # Check if index exists
                if index not in af_dict[address_family]['prefixes']\
                    [prefix]['index']:
                    af_dict[address_family]['prefixes'][prefix]\
                        ['index'][index] = {}
                    nh_dict = af_dict[address_family]['prefixes']\
                        [prefix]['index'][index]
                    nh_dict['next_hop'] = next_hop
                    nh_dict['status_codes'] = status_codes
                    nh_dict['path_type'] = path_type
                    nh_dict['metric'] = metric
                    nh_dict['localprf'] = localprf
                    nh_dict['weight'] = weight
                    nh_dict['origin_codes'] = origin_codes

                # Check if aggregate_address_ipv4_address
                if '>a' in status_codes+path_type:
                    address, mask = prefix.split("/")
                    if ':' in prefix:
                        af_dict[address_family]\
                            ['v6_aggregate_address_ipv6_address'] = prefix
                        af_dict[address_family]\
                            ['v6_aggregate_address_as_set'] = True
                        af_dict[address_family]\
                            ['v6_aggregate_address_summary_only'] = True
                    else:
                        af_dict[address_family]\
                            ['aggregate_address_ipv4_address'] = address
                        af_dict[address_family]\
                            ['aggregate_address_ipv4_mask'] = mask
                        af_dict[address_family]\
                            ['aggregate_address_as_set'] = True
                        af_dict[address_family]\
                            ['aggregate_address_summary_only'] = True
                    continue
                else:
                    # increment for multiple next-hops 
                    index += 1

            #                     0.0.0.0                  100      32768 i
            p4 = re.compile(r'^\s*(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                             '(?: +(?P<metric>[a-zA-Z0-9\s\(\)]+))?'
                             ' +(?P<localprf>[0-9]+) +(?P<weight>[0-9]+)'
                             ' +(?P<origin_codes>(i|e|\?|\|))$')
            m = p4.match(line)
            if m:
                # Get keys
                next_hop = str(m.groupdict()['next_hop'])
                metric = str(m.groupdict()['metric']).strip()
                localprf = str(m.groupdict()['localprf'])
                weight = str(m.groupdict()['weight'])
                origin_codes = str(m.groupdict()['origin_codes'])

                # increment for L2VPN EVPN prefix
                index += 1

                # Check if index exists
                if index not in af_dict[address_family]['prefixes']\
                    [prefix]['index']:
                    af_dict[address_family]['prefixes'][prefix]\
                        ['index'][index] = {}
                    nh_dict = af_dict[address_family]['prefixes']\
                        [prefix]['index'][index]
                    nh_dict['next_hop'] = next_hop
                    nh_dict['metric'] = metric
                    nh_dict['localprf'] = localprf
                    nh_dict['weight'] = weight
                    nh_dict['origin_codes'] = origin_codes
                    if data_on_nextline:
                        nh_dict['status_codes'] = status_codes
                        nh_dict['path_type'] = path_type
                        data_on_nextline = False
                        continue

            # Network            Next Hop            Metric     LocPrf     Weight Path
            # Route Distinguisher: 100:100     (VRF VRF1)
            p5 = re.compile(r'^\s*Route +Distinguisher *:'
                              ' +(?P<route_distinguisher>(\S+))'
                              ' +\(VRF +(?P<default_vrf>(\S+))\)$')
            m = p5.match(line)
            if m:
                route_distinguisher = str(m.groupdict()['route_distinguisher'])
                default_vrf = str(m.groupdict()['default_vrf'])
                if 'RD' in address_family:
                    p = re.compile(r'(?P<afname>.+\s.+) RD')
                    m = p.match(address_family)
                    if m:
                        address_family = m.groupdict()['afname'] + ' RD ' + route_distinguisher
                else:
                    address_family = address_family + ' RD ' + route_distinguisher
                continue

        return parsed_dict


# ==============================================
# Parser for 'show bgp vrf <WORD> all neighbors'
# ==============================================

class ShowBgpVrfAllNeighborsSchema(MetaParser):
    
    '''Schema for show bgp vrf <WORD> all neighbors'''

    schema = {
        'neighbor':
            {Any(): 
                {'remote_as': str,
                 Optional('local_as'): str,
                 'link': str,
                 'peer_index': int,
                 Optional('description'): str,
                 'bgp_version': int,
                 'router_id': str,
                 'session_state': str,
                 'shutdown': bool,
                 'up_time': str,
                 Optional('suppress_four_byte_as_capability'): bool,
                 Optional('retry_time'): str,
                 Optional('update_source'): str,
                 Optional('bfd_live_detection'): bool,
                 Optional('nbr_local_as_cmd'): str,
                 Optional('last_read'): str,
                 Optional('holdtime'): str,
                 Optional('keepalive_interval'): str,
                 Optional('bgp_negotiated_keepalive_timers'): 
                    {Optional('last_read'): str,
                     Optional('keepalive_interval'): str,
                     Optional('hold_time'): str,
                     Optional('last_written'): str,
                     Optional('keepalive_timer'): str,},
                 Optional('disable_connected_check'): bool,
                 Optional('inherit_peer_session'): str,
                 Optional('ebgp_multihop_max_hop'): int,
                 Optional('ebgp_multihop'): bool,
                 Optional('tcp_md5_auth'): str,
                 Optional('tcp_md5_auth_config'): str,
                 Optional('received_messages'): int,
                 Optional('received_notifications'): int,
                 Optional('received_bytes_queue'): int,
                 Optional('sent_messages'): int,
                 Optional('sent_notifications'): int,
                 Optional('sent_bytes_queue'): int,
                 Optional('bgp_session_transport'):
                    {Optional('connection'): 
                        {Optional('mode'): str,
                         Optional('last_reset'): str,
                         Optional('reset_reason'): str,
                         Optional('reset_by'): str,
                         Optional('attempts'): int,
                         Optional('established'): int,
                         Optional('dropped'): int,
                        },
                     Optional('transport'):
                        {Optional('local_port'): str,
                         Optional('local_host'): str,
                         Optional('foreign_port'): str,
                         Optional('foreign_host'): str,
                         Optional('fd'): str,
                        },
                    },
                 Optional('bgp_neighbor_counters'):
                    {Optional('messages'):
                        {Optional('sent'): 
                            {Any(): int,
                            },
                         Optional('received'):
                            {Any(): int,
                            },
                        },
                    },
                 Optional('bgp_negotiated_capabilities'): 
                    {Optional('route_refresh'): str,
                     Optional('route_refresh_old'): str,
                     Optional('vpnv4_unicast'): str,
                     Optional('vpnv6_unicast'): str,
                     Optional('graceful_restart'): str,
                     Optional('enhanced_refresh'): str,
                     Optional('multisession'): str,
                     Optional('stateful_switchover'): str,
                     Optional('dynamic_capability'): str,
                     Optional('dynamic_capability_old'): str,
                    },
                 Optional('graceful_restart_paramters'): 
                    {Optional('address_families_advertised_to_peer'): str,
                     Optional('address_families_advertised_from_peer'): str,
                     Optional('restart_time_advertised_to_peer_seconds'): int,
                     Optional('restart_time_advertised_by_peer_seconds'): int,
                     Optional('stale_time_advertised_by_peer_seconds'): int,
                    },
                 Optional('address_family'): 
                    {Any(): 
                        {Optional('bgp_table_version'): int,
                         Optional('neighbor_version'): int,
                         Optional('send_community'): bool,
                         Optional('soo'): str,
                         Optional('soft_configuration'): bool,
                         Optional('next_hop_self'): bool,
                         Optional('as_override_count'): int,
                         Optional('as_override'): bool,
                         Optional('maximum_prefix_max_prefix_no'): int,
                         Optional('route_map_name_in'): str,
                         Optional('route_map_name_out'): str,
                         Optional('nbr_af_default_originate'): bool,
                         Optional('nbr_af_default_originate_route_map'): str,
                         Optional('route_reflector_client'): bool,
                         Optional('path'): 
                            {Optional('total_entries'): int,
                             Optional('memory_usage'): int,
                             Optional('accepted_paths'): int,
                            },
                         Optional('inherit_peer_policy'):
                            {Any():
                                {Optional('inherit_peer_seq'): int,
                                },
                            },
                        },
                    },
                },
            },
        }

class ShowBgpVrfAllNeighbors(ShowBgpVrfAllNeighborsSchema):
    
    '''Parser for show bgp vrf <WORD> all neighbors'''

    def cli(self, vrf):
        cmd  = 'show bgp vrf {vrf} all neighbors'.format(vrf=vrf)
        out = self.device.execute(cmd)
        
        # Init vars
        parsed_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # BGP neighbor is 2.2.2.2,  remote AS 100, ibgp link,  Peer index 1
            # BGP neighbor is 2.2.2.5,  remote AS 200, local AS 333, ebgp link,  Peer index 2
            p1 = re.compile(r'^\s*BGP +neighbor +is +(?P<neighbor_id>[a-zA-Z0-9\.\:]+),'
                             ' +remote +AS +(?P<remote_as>[0-9]+),'
                             '(?: +local +AS +(?P<local_as>[0-9]+),)?'
                             ' +(?P<link>[a-zA-Z]+) +link, +Peer +index'
                             ' +(?P<peer_index>[0-9]+)$')
            m = p1.match(line)
            if m:
                if 'neighbor' not in parsed_dict:
                    parsed_dict['neighbor'] = {}
                neighbor_id = str(m.groupdict()['neighbor_id'])
                if neighbor_id not in parsed_dict['neighbor']:
                    parsed_dict['neighbor'][neighbor_id] = {}
                    parsed_dict['neighbor'][neighbor_id]['remote_as'] = \
                        str(m.groupdict()['remote_as'])
                    parsed_dict['neighbor'][neighbor_id]['local_as'] = \
                        str(m.groupdict()['local_as'])
                    parsed_dict['neighbor'][neighbor_id]['link'] = \
                        str(m.groupdict()['link'])
                    parsed_dict['neighbor'][neighbor_id]['peer_index'] = \
                        int(m.groupdict()['peer_index'])
                    continue

            # Description: nei_desc
            p2 = re.compile(r'^\s*Description *: +(?P<description>(\S+))$')
            m = p2.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['description'] = \
                        str(m.groupdict()['description'])
                continue

            # BGP version 4, remote router ID 2.2.2.2
            p3 = re.compile(r'^\s*BGP +version +(?P<bgp_version>[0-9]+),'
                             ' +remote +router +ID +(?P<router_id>[0-9\.]+)$')
            m = p3.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['bgp_version'] = \
                        int(m.groupdict()['bgp_version'])
                parsed_dict['neighbor'][neighbor_id]['router_id'] = \
                        str(m.groupdict()['router_id'])
                continue

            # BGP state = Established, up for 5w0d
            # BGP state = Idle, down for 4w6d, retry in 0.000000
            # BGP state = Shut (Admin), down for 5w0d
            p4 = re.compile(r'^\s*BGP +state +='
                             ' +(?P<session_state>[a-zA-Z\(\)\s]+), +(up|down)'
                             ' +for +(?P<up_time>[a-zA-Z0-9\:\.]+)'
                             '(?: *, +retry +in +(?P<retry_time>[0-9\.\:]+))?$')
            m = p4.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['session_state'] = \
                        str(m.groupdict()['session_state'])
                parsed_dict['neighbor'][neighbor_id]['up_time'] = \
                        str(m.groupdict()['up_time'])
                parsed_dict['neighbor'][neighbor_id]['retry_time'] = \
                        str(m.groupdict()['retry_time'])
                session_state = str(m.groupdict()['session_state'])
                if 'Shut' in session_state or 'shut' in session_state:
                    parsed_dict['neighbor'][neighbor_id]['shutdown'] = True
                else:
                    parsed_dict['neighbor'][neighbor_id]['shutdown'] = False
                    continue

            # Using loopback0 as update source for this peer
            p5 = re.compile(r'^\s*Using +(?P<update_source>[a-zA-Z0-9]+)'
                             ' +as +update +source +for +this +peer$')
            m = p5.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['update_source'] = \
                        str(m.groupdict()['update_source'])
                continue

            # BFD live-detection is configured
            p6 = re.compile(r'^\s*BFD live-detection is configured$')
            m = p6.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['bfd_live_detection'] = \
                    True
                continue

            # Neighbor local-as command not active
            p7 = re.compile(r'^\s*Neighbor +local-as +command'
                             ' +(?P<nbr_local_as_cmd>[a-zA-Z\s]+)$')
            m = p7.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['nbr_local_as_cmd'] = \
                        str(m.groupdict()['nbr_local_as_cmd'])
                continue

            # Last read 00:00:24, hold time = 99, keepalive interval is 33 seconds
            # Last read never, hold time = 180, keepalive interval is 60 seconds
            # Last read never, hold time = 45, keepalive interval is 15 seconds
            p8 = re.compile(r'^\s*Last +read +(?P<last_read>[a-zA-Z0-9\:]+),'
                             ' +hold +time += +(?P<holdtime>[0-9]+), +keepalive'
                             ' +interval +is +(?P<keepalive_interval>[0-9]+)'
                             ' +seconds$')
            m = p8.match(line)
            if m:
                if 'bgp_negotiated_keepalive_timers' not in \
                    parsed_dict['neighbor'][neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_negotiated_keepalive_timers'] = {}
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_keepalive_timers']['last_read'] = \
                        str(m.groupdict()['last_read'])
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_keepalive_timers']['keepalive_interval'] = \
                        str(m.groupdict()['keepalive_interval'])
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_keepalive_timers']['hold_time'] = \
                        str(m.groupdict()['holdtime'])
                continue

            # Last written 00:00:02, keepalive timer expiry due 00:00:30
            # Last written never, keepalive timer not running
            p9 = re.compile(r'^\s*Last +written'
                             ' +(?P<last_written>[a-zA-Z0-9\:]+), +keepalive'
                             ' +timer +(?P<keepalive_timer>[a-zA-Z0-9\:\s]+)$')
            m = p9.match(line)
            if m:
                if 'bgp_negotiated_keepalive_timers' not in \
                    parsed_dict['neighbor'][neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_negotiated_keepalive_timers'] = {}
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_keepalive_timers']['last_written'] = \
                        str(m.groupdict()['last_written'])
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_keepalive_timers']['keepalive_timer'] = \
                        str(m.groupdict()['keepalive_timer'])
                continue

            # Inherits session configuration from session-template PEER-SESSION
            p10 = re.compile(r'^\s*Inherits +session +configuration +from'
                            ' +session-template +(?P<template>[a-zA-Z\-\_]+)$')
            m = p10.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['inherit_peer_session'] = \
                    str(m.groupdict()['template'])
                continue

            # Connected check is disabled
            p11 = re.compile(r'^\s*Connected check is disabled$')
            m = p11.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['disable_connected_check'] = True
                continue

            # External BGP peer might be upto 255 hops away
            p12 = re.compile(r'^\s*External +BGP +peer +might +be +upto'
                             ' +(?P<ebgp_multihop_max_hop>[0-9]+) +hops +away$')
            m = p12.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['ebgp_multihop_max_hop'] = \
                    int(m.groupdict()['ebgp_multihop_max_hop'])
                parsed_dict['neighbor'][neighbor_id]['ebgp_multihop'] = True
                continue

            # TCP MD5 authentication is enabled
            p13 = re.compile(r'^\s*TCP +MD5 +authentication +is'
                              ' +(?P<tcp_md5_auth>[a-zA-Z\s]+)$')
            m = p13.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['tcp_md5_auth'] = \
                    str(m.groupdict()['tcp_md5_auth'])
                parsed_dict['neighbor'][neighbor_id]['tcp_md5_auth_config'] = \
                    str(line).strip()
                continue
            
            # Only passive connection setup allowed
            p14 = re.compile(r'^\s*Only +passive +connection +setup'
                             ' +(?P<only_passive_conn>[a-zA-Z]+)$')
            m = p14.match(line)
            if m:
                if 'bgp_session_transport' not in parsed_dict['neighbor']\
                    [neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport'] = {}
                if 'connection' not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_session_transport']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['connection'] = {}
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['connection']['mode'] = \
                    str(m.groupdict()['only_passive_conn'])
                continue

            # Received 92717 messages, 3 notifications, 0 bytes in queue
            p15 = re.compile(r'^\s*Received +(?P<received_messages>[0-9]+)'
                              ' +messages, +(?P<received_notifications>[0-9]+)'
                              ' +notifications, +(?P<received_bytes>[0-9]+)'
                              ' +bytes +in +queue$')
            m = p15.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['received_messages'] = \
                    int(m.groupdict()['received_messages'])
                parsed_dict['neighbor'][neighbor_id]['received_notifications'] = \
                    int(m.groupdict()['received_notifications'])
                parsed_dict['neighbor'][neighbor_id]['received_bytes_queue'] = \
                    int(m.groupdict()['received_bytes'])
                continue

            # Sent 92730 messages, 5 notifications, 0 bytes in queue
            p16 = re.compile(r'^\s*Sent +(?P<sent_messages>[0-9]+)'
                              ' +messages, +(?P<sent_notifications>[0-9]+)'
                              ' +notifications, +(?P<sent_bytes_queue>[0-9]+)'
                              ' +bytes +in +queue$')
            m = p16.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['sent_messages'] = \
                    int(m.groupdict()['sent_messages'])
                parsed_dict['neighbor'][neighbor_id]['sent_notifications'] = \
                    int(m.groupdict()['sent_notifications'])
                parsed_dict['neighbor'][neighbor_id]['sent_bytes_queue'] = \
                    int(m.groupdict()['sent_bytes_queue'])
                continue

            # Connections established 9, dropped 8
            p17 = re.compile(r'^\s*Connections +established'
                              ' +(?P<esablished>[0-9]+), +dropped'
                              ' +(?P<dropped>[0-9]+)$')
            m = p17.match(line)
            if m:
                if 'bgp_session_transport' not in parsed_dict['neighbor']\
                    [neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport'] = {}
                if 'connection' not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_session_transport']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['connection'] = {}
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['connection']['established'] = \
                        int(m.groupdict()['esablished'])
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['connection']['dropped'] = int(m.groupdict()['dropped'])
                continue

            # Connections attempts 0
            p17_1 = re.compile(r'^\s*Connections +attempts'
                                ' +(?P<attemps>[0-9]+)$')
            m = p17.match(line)
            if m:
                if 'bgp_session_transport' not in parsed_dict['neighbor']\
                    [neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport'] = {}
                if 'connection' not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_session_transport']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['connection'] = {}
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['connection']['attemps'] = int(m.groupdict()['attemps'])
                continue

            # Last reset by us 5w0d, due to session cleared
            # Last reset by peer 5w0d, due to session cleared
            # Last reset by us never, due to No error
            p18 = re.compile(r'^\s*Last +reset +by (?P<reset_by>[a-zA-Z]+)'
                              ' +(?P<last_reset>[a-zA-Z0-9\:\s]+), +due +to'
                              ' +(?P<reset_reason>[a-zA-Z\-\s]+)$')
            m = p18.match(line)
            if m:
                if 'bgp_session_transport' not in parsed_dict['neighbor']\
                    [neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport'] = {}
                if 'connection' not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_session_transport']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['connection'] = {}
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['connection']['last_reset'] = \
                        str(m.groupdict()['last_reset']).lower()
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['connection']['reset_reason'] = \
                        str(m.groupdict()['reset_reason']).lower()
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['connection']['reset_by'] = \
                        str(m.groupdict()['reset_by']).lower()
                continue

            # Neighbor capabilities:
            p19 = re.compile(r'^\s*Neighbor +capabilities *:$')
            m = p19.match(line)
            if m:
                if 'bgp_negotiated_capabilities' not in parsed_dict['neighbor']\
                    [neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_negotiated_capabilities'] = {}
                continue

            # Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
            p20_1 = re.compile(r'^\s*Dynamic +capability *:'
                              ' +(?P<dynamic_capability>[a-zA-Z\,\(\)\s]+)$')
            m = p20_1.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_capabilities']['dynamic_capability'] = \
                        str(m.groupdict()['dynamic_capability'])
                continue

            # Dynamic capability (old): advertised received
            p20_2 = re.compile(r'^\s*Dynamic +capability +\(old\) *:'
                              ' +(?P<dynamic_capability_old>[a-zA-Z\s]+)$')
            m = p20_2.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_capabilities']['dynamic_capability_old'] = \
                        str(m.groupdict()['dynamic_capability_old'])
                continue

            # Route refresh capability (new): advertised received
            p21_1 = re.compile(r'^\s*Route +refresh +capability +\(new\) *:'
                                ' +(?P<route_refresh>[a-zA-Z\s]+)$')
            m = p21_1.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_capabilities']['route_refresh'] = \
                        str(m.groupdict()['route_refresh'])
                continue

            # Route refresh capability (old): advertised received 
            p21_1 = re.compile(r'^\s*Route +refresh +capability +\(old\) *:'
                                ' +(?P<route_refresh_old>[a-zA-Z\s]+)$')
            m = p21_1.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_capabilities']['route_refresh_old'] = \
                        str(m.groupdict()['route_refresh_old'])
                continue

            # 4-Byte AS capability: disabled
            p22 = re.compile(r'^\s*4-Byte AS capability: disabled$')
            m = p22.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['suppress_four_byte_as_capability'] = True
                continue

            # Address family VPNv4 Unicast: advertised received
            p23 = re.compile(r'^\s*Address +family +VPNv4 +Unicast *:'
                              ' +(?P<vpnv4_unicast>[a-zA-Z\s]+)$')
            m = p23.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_capabilities']['vpnv4_unicast'] = \
                        str(m.groupdict()['vpnv4_unicast'])
                continue

            # Address family VPNv6 Unicast: advertised received 
            p24 = re.compile(r'^\s*Address +family +VPNv6 +Unicast *:'
                              ' +(?P<vpnv6_unicast>[a-zA-Z\s]+)$')
            m = p24.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_capabilities']['vpnv6_unicast'] = \
                        str(m.groupdict()['vpnv6_unicast'])
                continue


            # Graceful Restart capability: advertised received
            p25 = re.compile(r'^\s*Graceful +Restart +capability *:'
                              ' +(?P<graceful_restart>[a-zA-Z\s]+)$')
            m = p25.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_capabilities']['graceful_restart'] = \
                        str(m.groupdict()['graceful_restart'])
                continue

            # Graceful Restart Parameters:
            p26 = re.compile(r'^\s*Graceful +Restart +Parameters *:$')
            m = p26.match(line)
            if m:
                if 'graceful_restart_paramters' not in \
                    parsed_dict['neighbor'][neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['graceful_restart_paramters'] = {}
                    continue

            # Address families advertised to peer:
            # VPNv4 Unicast  VPNv6 Unicast 
            p27_1 = re.compile(r'^\s*$')
            m = p27_1.match(line)
            if m:
                continue

            # Address families received from peer:
            # VPNv4 Unicast  VPNv6 Unicast  
            p27_2 = re.compile(r'^\s*$')
            m = p27_2.match(line)
            if m:
                continue

            # Forwarding state preserved by peer for:
            # Restart time advertised to peer: 240 seconds
            p28_1 = re.compile(r'^\s*Restart +time +advertised +to +peer *:'
                                ' +(?P<time>[0-9]+) +seconds$')
            m = p28_1.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['graceful_restart_paramters']\
                        ['restart_time_advertised_to_peer_seconds'] = \
                            int(m.groupdict()['time'])
                continue

            # Restart time advertised by peer: 120 seconds
            p28_2 = re.compile(r'^\s*Restart +time +advertised +by +peer *:'
                                ' +(?P<time>[0-9]+) +seconds$')
            m = p28_2.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['graceful_restart_paramters']\
                        ['restart_time_advertised_by_peer_seconds'] = \
                            int(m.groupdict()['time'])
                continue

            # Stale time for routes advertised by peer: 600 seconds
            p28_1 = re.compile(r'^\s*Stale +time +for +routes +advertised +by'
                                ' +peer *: +(?P<time>[0-9]+) +seconds$')
            m = p28_1.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['graceful_restart_paramters']\
                        ['stale_time_advertised_by_peer_seconds'] = \
                            int(m.groupdict()['time'])
                continue

            # Message statistics:
            #                         Sent               Rcvd
            # Opens:                         9                  9  
            # Notifications:                 5                  3  
            # Updates:                      50                 38  
            # Keepalives:                92663              92661  
            # Route Refresh:                 2                  5  
            # Capability:                    1                  1  
            # Total:                     92730              92717  
            # Total bytes:             1763812            1763099  
            # Bytes in queue:                0                  0
            p30 = re.compile(r'^\s*(?P<message_stat>[a-zA-Z\s]+) *:'
                              ' +(?P<sent>[0-9]+) +(?P<received>[0-9]+)$')
            m = p30.match(line)
            if m:
                if 'bgp_neighbor_counters' not in parsed_dict['neighbor']\
                    [neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_neighbor_counters'] = {}
                if 'messages' not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_neighbor_counters']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_neighbor_counters']['messages'] = {}
                if 'sent' not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_neighbor_counters']['messages']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_neighbor_counters']['messages']['sent'] = {}
                if 'received' not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_neighbor_counters']['messages']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_neighbor_counters']['messages']['received'] = {}
                message_stat = str(m.groupdict()['message_stat']).lower()
                message_stat = message_stat.replace(" ", "_")
                sent = int(m.groupdict()['sent'])
                received = int(m.groupdict()['received'])
                if message_stat not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_neighbor_counters']['messages']['sent']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_neighbor_counters']['messages']['sent']\
                        [message_stat] = sent
                if message_stat not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_neighbor_counters']['messages']['received']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_neighbor_counters']['messages']['received']\
                        [message_stat] = received
                continue

            # For address family: VPNv4 Unicast
            p31 = re.compile(r'^\s*For +address +family *:'
                              ' +(?P<af>[a-zA-Z0-9\s]+)$')
            m = p31.match(line)
            if m:
                if 'address_family' not in  parsed_dict['neighbor'][neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]['address_family'] = {}
                address_family = str(m.groupdict()['af']).lower()
                
                if address_family not in parsed_dict['neighbor'][neighbor_id]\
                    ['address_family']:
                    parsed_dict['neighbor'][neighbor_id]['address_family']\
                        [address_family] = {}
                    continue

            # BGP table version 48, neighbor version 48
            p32 = re.compile(r'^\s*BGP +table +version'
                              ' +(?P<af_bgp_table_version>[0-9]+), +neighbor'
                              ' +version +(?P<nbr_version>[0-9]+)$')
            m = p32.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['bgp_table_version'] = \
                        int(m.groupdict()['af_bgp_table_version'])
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['neighbor_version'] = \
                        int(m.groupdict()['nbr_version'])
                continue

            # 1 accepted paths consume 48 bytes of memory
            p33 = re.compile(r'^\s*(?P<accepted_paths>[0-9]+) +accepted'
                              ' +paths +consume +(?P<bytes_consumed>[0-9]+)'
                              ' +bytes +of +memory$')
            m = p33.match(line)
            if m:
                if 'path' not in parsed_dict['neighbor'][neighbor_id]\
                    ['address_family'][address_family]:
                    parsed_dict['neighbor'][neighbor_id]['address_family']\
                        [address_family]['path'] = {}
                accepted_paths = int(m.groupdict()['accepted_paths'])
                memory_usage = int(m.groupdict()['bytes_consumed'])
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['path']['accepted_paths'] = accepted_paths
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['path']['memory_usage'] = memory_usage
                continue

            # 2 sent paths
            p34 = re.compile(r'^\s*(?P<num_sent_paths>[0-9]+) +sent +paths$')
            m = p34.match(line)
            if m:
                if 'path' not in parsed_dict['neighbor'][neighbor_id]\
                    ['address_family'][address_family]:
                    parsed_dict['neighbor'][neighbor_id]['address_family']\
                        [address_family]['path'] = {}
                total_entries = int(m.groupdict()['num_sent_paths'])
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['path']['total_entries'] = total_entries
                continue
            
            # Community attribute sent to this neighbor
            p35 = re.compile(r'^\s*Community +attribute +sent +to +this'
                              ' +neighbor$')
            m = p35.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['send_community'] = True
                continue

            # Extended community attribute sent to this neighbor
            p36 = re.compile(r'^\s*Extended +community +attribute +sent +to'
                              ' +this +neighbor$')
            m = p36.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['send_community'] = True
                continue

            # Maximum prefixes allowed 300000
            p37 = re.compile(r'^\s*Maximum +prefixes +allowed +(?P<num>[0-9]+)$')
            m = p37.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['maximum_prefix_max_prefix_no'] = \
                        int(m.groupdict()['num'])
                continue

            # Inbound route-map configured is genie_redistribution, handle obtained
            p38 = re.compile(r'^\s*Inbound +route-map +configured +is'
                              ' +(?P<route_map_name_in>(\S+)), +handle'
                              ' +obtained$')
            m = p38.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['route_map_name_in'] = \
                        str(m.groupdict()['route_map_name_in'])
                continue

            # Outbound route-map configured is genie_redistribution, handle obtained
            p39 = re.compile(r'^\s*Outbound +route-map +configured +is'
                              ' +(?P<route_map_name_out>(\S+)), +handle'
                              ' +obtained$')
            m = p39.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['route_map_name_out'] = \
                        str(m.groupdict()['route_map_name_out'])
                continue
            
            # Third-party Nexthop will not be computed.
            p40 = re.compile(r'^\s*Third-party +Nexthop +will +not +be'
                              ' +computed.$')
            m = p40.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['next_hop_self'] = False
                continue
            
            # SOO Extcommunity: SOO:100:100
            p41 = re.compile(r'^\s*SOO +Extcommunity *:'
                              ' +(?P<soo>[a-zA-Z0-9\:]+)$')
            m = p41.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['soo'] = str(m.groupdict()['soo'])
                continue

            # Inbound soft reconfiguration allowed
            p42 = re.compile(r'^\s*Inbound +soft +reconfiguration +allowed$')
            m = p42.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['soft_configuration'] = True
                continue

            # Nexthop always set to local peering address, 0.0.0.0
            p43 = re.compile(r'^\s*Nexthop +always +set +to +local +peering'
                              ' +address, +0\.0\.0\.0$')
            m = p43.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['next_hop_self'] = True
                continue

            # Allow my ASN 9 times
            p44 = re.compile(r'^\s*Allow +my +ASN +(?P<num>[0-9]+) +times$')
            m = p44.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['as_override_count'] = \
                        int(m.groupdict()['num'])
                continue

            # ASN override is enabled
            p45 = re.compile(r'^\s*ASN override is enabled$')
            m = p45.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['as_override'] = True
                continue

            # Default information originate, default not sent
            p46 = re.compile(r'^\s*Default +information +originate, +default'
                              ' +not +sent$')
            m = p46.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['nbr_af_default_originate'] = True
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['nbr_af_default_originate_route_map'] = \
                        str(line).strip()
                continue

            # Inherited policy-templates:
            # Preference    Name
            #         10    PEER-POLICY                                                 
            #         20    PEER-POLICY2
            p48 = re.compile(r'^\s*(?P<inherit_peer_seq>[0-9]+)'
                              ' +(?P<policy_name>[a-zA-Z0-9\-\_]+)$')
            m = p48.match(line)
            if m:
                policy_name = str(m.groupdict()['policy_name'])
                inherit_peer_seq = int(m.groupdict()['inherit_peer_seq'])
                if 'inherit_peer_policy' not in parsed_dict['neighbor']\
                    [neighbor_id]['address_family'][address_family]:
                    parsed_dict['neighbor'][neighbor_id]['address_family']\
                        [address_family]['inherit_peer_policy'] = {}
                if policy_name not in parsed_dict['neighbor'][neighbor_id]\
                    ['address_family'][address_family]\
                        ['inherit_peer_policy']:
                    parsed_dict['neighbor'][neighbor_id]['address_family']\
                        [address_family]['inherit_peer_policy']\
                        [policy_name] = {}
                    parsed_dict['neighbor'][neighbor_id]['address_family']\
                        [address_family]['inherit_peer_policy']\
                        [policy_name]['inherit_peer_seq'] = inherit_peer_seq
                    continue

            # Local host: 1.1.1.1, Local port: 179
            p49 = re.compile(r'^\s*Local +host *: +(?P<local_host>[0-9\.\:]+),'
                              ' +Local +port *: +(?P<local_port>[0-9]+)$')
            m = p49.match(line)
            if m:
                if 'bgp_session_transport' not in parsed_dict['neighbor']\
                    [neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport'] = {}
                if 'transport' not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_session_transport']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['transport'] = {}
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['transport']['local_host'] = \
                        str(m.groupdict()['local_host'])
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['transport']['local_port'] = \
                        str(m.groupdict()['local_port'])
                continue

            # Foreign host: 2.2.2.2, Foreign port: 4466
            p50 = re.compile(r'^\s*Foreign +host *:'
                              ' +(?P<foreign_host>[0-9\.\:]+), +Foreign'
                              ' +port *: +(?P<foreign_port>[0-9]+)$')
            m = p50.match(line)
            if m:
                if 'bgp_session_transport' not in parsed_dict['neighbor']\
                    [neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport'] = {}
                if 'transport' not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_session_transport']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['transport'] = {}
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['transport']['foreign_host'] = \
                        str(m.groupdict()['foreign_host'])
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['transport']['foreign_port'] = \
                        str(m.groupdict()['foreign_port'])
                continue
            
            # fd = 44
            p51 = re.compile(r'^\s*fd += +(?P<fd>[0-9]+)$')
            m = p51.match(line)
            if m:
                if 'bgp_session_transport' not in parsed_dict['neighbor']\
                    [neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport'] = {}
                if 'transport' not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_session_transport']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['transport'] = {}
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['transport']['fd'] = str(m.groupdict()['fd'])
                continue

            # Route reflector client
            p52 = re.compile(r'^\s*Route reflector client$')
            m = p52.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['route_reflector_client'] = True
                continue

        return parsed_dict


# ==================================================
# Parser for 'show bgp vrf all all nexthop-database'
# ==================================================

class ShowBgpVrfAllAllNextHopDatabaseSchema(MetaParser):
    
    '''Schema for show bgp vrf all all nexthop-database'''

    schema = {
        'vrf': 
            {Any():
                {'address_family':
                    {Any():
                        {'af_nexthop_trigger_enable': bool,
                         'nexthop_trigger_delay_critical': int,
                         'nexthop_trigger_delay_non_critical': int,
                         Optional('next_hop'): str,
                         Optional('refcount'): int,
                         Optional('igp_cost'): int,
                         Optional('igp_route_type'): int,
                         Optional('igp_preference'): int,
                         Optional('nexthop_type'): str,
                         Optional('nexthop_last_resolved'): str,
                         Optional('nexthop_resolved_using'): str,
                         Optional('metric_next_advertise'): str,
                         Optional('rnh_epoch'): int,
                         Optional('attached_nexthop'): str,
                         Optional('attached_nexthop_interface'): str,
                        },
                    },
                },
            },
        }

class ShowBgpVrfAllAllNextHopDatabase(ShowBgpVrfAllAllNextHopDatabaseSchema):
    
    '''Parser for show bgp vrf all all nexthop-database'''

    def cli(self):
        cmd = 'show bgp vrf all all nexthop-database'
        out = self.device.execute(cmd)
        
        # Init vars
        nh_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # Next Hop table for VRF VRF1, address family IPv4 Unicast:
            p1 = re.compile(r'^\s*Next +Hop +table +for +VRF'
                             ' +(?P<vrf_name>[a-zA-Z0-9]+), +address +family'
                             ' +(?P<af>[a-zA-Z0-9\s]+) *:$')
            m = p1.match(line)
            if m:
                if 'vrf' not in nh_dict:
                    nh_dict['vrf'] = {}
                vrf = str(m.groupdict()['vrf_name'])
                if vrf not in nh_dict['vrf']:
                    nh_dict['vrf'][vrf] = {}
                if 'address_family' not in nh_dict['vrf'][vrf]:
                    nh_dict['vrf'][vrf]['address_family'] = {}
                af = str(m.groupdict()['af']).lower()

                if af not in nh_dict['vrf'][vrf]['address_family']:
                    nh_dict['vrf'][vrf]['address_family'][af] = {}
                    af_dict = nh_dict['vrf'][vrf]['address_family'][af]
                    af_dict['af_nexthop_trigger_enable'] = True
                    continue

            # Next-hop trigger-delay(miliseconds)
            # Critical: 2222 Non-critical: 3333
            p2 = re.compile(r'^\s*Critical *:'
                             ' +(?P<nexthop_trigger_delay_critical>[0-9]+)'
                             ' +Non-critical *:'
                             ' +(?P<nexthop_trigger_delay_non_critical>[0-9]+)$')
            m = p2.match(line)
            if m:
                af_dict['nexthop_trigger_delay_critical'] = \
                    int(m.groupdict()['nexthop_trigger_delay_critical'])
                af_dict['nexthop_trigger_delay_non_critical'] = \
                    int(m.groupdict()['nexthop_trigger_delay_non_critical'])
                continue

            # Nexthop: 0.0.0.0, Refcount: 4, IGP cost: 0
            p3 = re.compile(r'^\s*Nexthop *: +(?P<nh>[a-zA-Z0-9\.\:]+),'
                             ' +Refcount *: +(?P<refcount>[0-9]+), +IGP'
                             ' +cost *: +(?P<igp_cost>[0-9]+)$')
            m = p3.match(line)
            if m:
                af_dict['next_hop'] = str(m.groupdict()['nh'])
                af_dict['refcount'] = int(m.groupdict()['refcount'])
                af_dict['igp_cost'] = int(m.groupdict()['igp_cost'])
                continue

            # IGP Route type: 0, IGP preference: 0
            p4 = re.compile(r'^\s*IGP +Route +type *:'
                             ' +(?P<igp_route_type>[0-9]+), +IGP +preference *:'
                             ' +(?P<igp_preference>[0-9]+)$')
            m = p4.match(line)
            if m:
                af_dict['igp_route_type'] = int(m.groupdict()['igp_route_type'])
                af_dict['igp_preference'] = int(m.groupdict()['igp_preference'])
                continue

            # Nexthop is not-attached local unreachable not-labeled
            # Nexthop is not-attached not-local reachable labeled
            p5 = re.compile(r'^\s*Nexthop +is +(?P<nexthop_type>[a-zA-Z\s\-]+)$')
            m = p5.match(line)
            if m:
                af_dict['nexthop_type'] = str(m.groupdict()['nexthop_type'])
                continue

            # Nexthop last resolved: never, using 0.0.0.0/0
            p6 = re.compile(r'^\s*Nexthop +last +resolved *:'
                             ' +(?P<nexthop_last_resolved>[a-zA-Z0-9\:]+),'
                             ' +using +(?P<nexthop_resolved_using>[0-9\.\/]+)$')
            m = p6.match(line)
            if m:
                af_dict['nexthop_last_resolved'] = \
                    str(m.groupdict()['nexthop_last_resolved'])
                af_dict['nexthop_resolved_using'] = \
                    str(m.groupdict()['nexthop_resolved_using'])
                continue

            # Metric next advertise: Never
            p7 = re.compile(r'^\s*Metric +next +advertise *:'
                             ' +(?P<metric_next_advertise>[a-zA-Z0-9]+)$')
            m = p7.match(line)
            if m:
                af_dict['metric_next_advertise'] = \
                    str(m.groupdict()['metric_next_advertise']).lower()
                continue

            # RNH epoch: 0
            p8 = re.compile(r'^\s*RNH +epoch *: +(?P<rnh_epoch>[0-9]+)$')
            m = p8.match(line)
            if m:
                af_dict['rnh_epoch'] = int(m.groupdict()['rnh_epoch'])
                continue

            # Attached nexthop: 10.1.3.3, Interface: Ethernet4/2
            p8 = re.compile(r'^\s*Attached +nexthop *:'
                             ' +(?P<attached_nexthop>[0-9\.\:]+), +Interface *:'
                             ' +(?P<attached_nexthop_interface>[a-zA-Z0-9\/]+)$')
            m = p8.match(line)
            if m:
                af_dict['attached_nexthop'] = \
                    str(m.groupdict()['attached_nexthop'])
                af_dict['attached_nexthop_interface'] = \
                    str(m.groupdict()['attached_nexthop_interface'])
                continue

        return nh_dict


# =========================================
# Parser for 'show bgp vrf all all summary'
# =========================================

class ShowBgpVrfAllAllSummarySchema(MetaParser):
    
    '''Schema for show bgp vrf all all summary'''

    schema = {
        'vrf':
            {Any():
                {Optional('neighbor'):
                    {Any():
                        {'address_family':
                            {Any():
                                {'v': int,
                                'as': int,
                                'msg_rcvd': int,
                                'msg_sent': int,
                                'tbl_ver': int,
                                'inq': int,
                                'outq': int,
                                'up_down': str,
                                'state_pfxrcd': str,
                                Optional('route_identifier'): str,
                                Optional('local_as'): int,
                                Optional('bgp_table_version'): int,
                                Optional('config_peers'): int,
                                Optional('capable_peers'): int,
                                Optional('prefixes'):
                                    {'total_entries': int,
                                    'memory_usage': int,
                                },
                                Optional('path'):
                                    {'total_entries': int,
                                    'memory_usage': int,
                                },
                                Optional('attribute_entries'): str,
                                Optional('as_path_entries'): str,
                                Optional('community_entries'): str,
                                Optional('clusterlist_entries'): str,
                                Optional('dampening'): bool,
                                Optional('history_paths'): int,
                                Optional('dampened_paths'): int,
                                },
                            },
                        },
                    },
                },
            },
        }

class ShowBgpVrfAllAllSummary(ShowBgpVrfAllAllSummarySchema):
    
    '''Parser for show bgp vrf all all summary'''

    def cli(self):
        cmd = 'show bgp vrf all all summary'
        out = self.device.execute(cmd)
        
        # Init vars
        sum_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # BGP summary information for VRF VRF1, address family IPv4 Unicast
            p1 = re.compile(r'^\s*BGP +summary +information +for +VRF'
                             ' +(?P<vrf_name>[a-zA-Z0-9]+), +address +family'
                             ' +(?P<address_family>[a-zA-Z0-9\s]+)$')
            m = p1.match(line)
            if m:
                # Save variables for use later
                address_family = str(m.groupdict()['address_family']).lower()
                vrf = str(m.groupdict()['vrf_name'])
                continue

            # BGP router identifier 4.4.4.4, local AS number 100
            p2 = re.compile(r'^\s*BGP +router +identifier'
                             ' +(?P<route_identifier>[0-9\.\:]+), +local +AS'
                             ' +number +(?P<local_as>[0-9]+)$')
            m = p2.match(line)
            if m:
                route_identifier = str(m.groupdict()['route_identifier'])
                local_as = int(m.groupdict()['local_as'])
                if 'vrf' not in sum_dict:
                    sum_dict['vrf'] = {}
                if vrf not in sum_dict['vrf']:
                    sum_dict['vrf'][vrf] = {}
                continue

            # BGP table version is 40, IPv4 Unicast config peers 1, capable peers 0
            p3 = re.compile(r'^\s*BGP +table +version +is'
                             ' +(?P<bgp_table_version>[0-9]+),'
                             ' +(?P<address_family>[a-zA-Z0-9\s]+) +config'
                             ' +peers +(?P<config_peers>[0-9]+), +capable'
                             ' +peers +(?P<capable_peers>[0-9]+)$')
            m = p3.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                config_peers = int(m.groupdict()['config_peers'])
                capable_peers = int(m.groupdict()['capable_peers'])
                continue

            # 5 network entries and 5 paths using 620 bytes of memory
            p4 = re.compile(r'^\s*(?P<networks>[0-9]+) +network +entries +and'
                             ' +(?P<paths>[0-9]+) +paths +using'
                             ' +(?P<bytes>[0-9]+) +bytes +of +memory$')
            m = p4.match(line)
            if m:
                num_prefix_entries = int(m.groupdict()['networks'])
                memory_usage = int(m.groupdict()['bytes'])
                num_path_entries = int(m.groupdict()['paths'])
                continue

            # BGP attribute entries [3/384], BGP AS path entries [0/0]
            p5 = re.compile(r'^\s*BGP +attribute +entries'
                             ' +(?P<attribute_entries>(\S+)), +BGP +AS +path'
                             ' +entries +(?P<as_path_entries>(\S+))$')
            m = p5.match(line)
            if m:
                attribute_entries = str(m.groupdict()['attribute_entries'])
                as_path_entries = str(m.groupdict()['as_path_entries'])
                continue

            # BGP community entries [0/0], BGP clusterlist entries [1/4]
            p6 = re.compile(r'^\s*BGP +community +entries'
                             ' +(?P<community_entries>(\S+)), +BGP +clusterlist'
                             ' +entries +(?P<clusterlist_entries>(\S+))$')
            m = p6.match(line)
            if m:
                community_entries = str(m.groupdict()['community_entries'])
                clusterlist_entries = str(m.groupdict()['clusterlist_entries'])
                continue

            # Dampening configured, 0 history paths, 0 dampened paths
            p7 = re.compile(r'^\s*Dampening +configured,'
                             ' +(?P<history_paths>[0-9]+) +history +paths,'
                             ' +(?P<dampened_paths>[0-9]+) +dampened +paths$')
            m = p7.match(line)
            if m:
                dampening = True
                history_paths = int(m.groupdict()['history_paths'])
                dampened_paths = int(m.groupdict()['dampened_paths'])
                continue

            # Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
            # 2.2.2.10        4     0       0       0        0    0    0     5w6d Idle 
            p8 = re.compile(r'^\s*(?P<neighbor>[0-9\.]+) +(?P<v>[0-9]+)'
                             ' +(?P<as>[0-9]+) +(?P<msg_rcvd>[0-9]+)'
                             ' +(?P<msg_sent>[0-9]+) +(?P<tbl_ver>[0-9]+)'
                             ' +(?P<inq>[0-9]+) +(?P<outq>[0-9]+)'
                             ' +(?P<up_down>[a-zA-Z0-9\:]+)'
                             ' +(?P<state>[a-zA-Z0-9\(\)\s]+)$')
            m = p8.match(line)
            if m:
                # Add neighbor to dictionary
                neighbor = str(m.groupdict()['neighbor'])
                if 'neighbor' not in sum_dict['vrf'][vrf]:
                    sum_dict['vrf'][vrf]['neighbor'] = {}
                if neighbor not in sum_dict['vrf'][vrf]['neighbor']:
                    sum_dict['vrf'][vrf]['neighbor'][neighbor] = {}
                    nbr_dict = sum_dict['vrf'][vrf]['neighbor'][neighbor]

                # Add address family to this neighbor
                if 'address_family' not in nbr_dict:
                    nbr_dict['address_family'] = {}
                if address_family not in nbr_dict['address_family']:
                    nbr_dict['address_family'][address_family] = {}
                    nbr_af_dict = nbr_dict['address_family'][address_family]

                # Add keys for this address_family
                nbr_af_dict['v'] = int(m.groupdict()['v'])
                nbr_af_dict['as'] = int(m.groupdict()['as'])
                nbr_af_dict['msg_rcvd'] = int(m.groupdict()['msg_rcvd'])
                nbr_af_dict['msg_sent'] = int(m.groupdict()['msg_sent'])
                nbr_af_dict['tbl_ver'] = int(m.groupdict()['tbl_ver'])
                nbr_af_dict['inq'] = int(m.groupdict()['inq'])
                nbr_af_dict['outq'] = int(m.groupdict()['outq'])
                nbr_af_dict['up_down'] = str(m.groupdict()['up_down'])
                nbr_af_dict['state_pfxrcd'] = str(m.groupdict()['state'])
                try:
                    # Assign variables
                    nbr_af_dict['route_identifier'] = route_identifier
                    nbr_af_dict['local_as'] = local_as
                    nbr_af_dict['bgp_table_version'] = bgp_table_version
                    nbr_af_dict['config_peers'] = config_peers
                    nbr_af_dict['capable_peers'] = capable_peers
                    nbr_af_dict['attribute_entries'] = attribute_entries
                    nbr_af_dict['as_path_entries'] = as_path_entries
                    nbr_af_dict['community_entries'] = community_entries
                    nbr_af_dict['clusterlist_entries'] = clusterlist_entries
                    nbr_af_dict['dampening'] = dampening
                    nbr_af_dict['history_paths'] = history_paths
                    nbr_af_dict['dampened_paths'] = dampened_paths
                    # Delete variables in preparation for next neighbor
                    del route_identifier; del local_as; del bgp_table_version;
                    del config_peers; del capable_peers; del attribute_entries;
                    del as_path_entries; del community_entries;
                    del clusterlist_entries; del dampening; del history_paths;
                    del dampened_paths
                except:
                    pass
                if num_prefix_entries:
                    nbr_af_dict['prefixes'] = {}
                    nbr_af_dict['prefixes']['total_entries'] = num_prefix_entries
                    nbr_af_dict['prefixes']['memory_usage'] = memory_usage
                if num_path_entries:
                    nbr_af_dict['path'] = {}
                    nbr_af_dict['path']['total_entries'] = num_prefix_entries
                    nbr_af_dict['path']['memory_usage'] = memory_usage
                    continue

        return sum_dict


# ==================================================
# Parser for 'show bgp vrf all dampening parameters'
# ==================================================

class ShowBgpVrfAllAllDampeningParametersSchema(MetaParser):
    
    '''Schema for 'show bgp vrf all dampening parameters'''
    
    schema = {
        'vrf':
            {Any():
                {'address_family':
                    {Any():
                        {Optional('dampening'): str,
                        Optional('dampening_route_map'): str,
                        Optional('dampening_half_life_time'): str,
                        Optional('dampening_reuse_time'): str,
                        Optional('dampening_suppress_time'): str,
                        Optional('dampening_max_suppress_time'): str,
                        Optional('dampening_max_suppress_penalty'): str,
                        Optional('route_distinguisher'):
                            {Optional(Any()):
                                {Optional('dampening'): str,
                                Optional('rd_vrf'): str,
                                Optional('dampening_route_map'): str,
                                Optional('dampening_half_life_time'): str,
                                Optional('dampening_reuse_time'): str,
                                Optional('dampening_suppress_time'): str,
                                Optional('dampening_max_suppress_time'): str,
                                Optional('dampening_max_suppress_penalty'): str,
                                },
                            },
                        },
                    },
                },
            },
        }

class ShowBgpVrfAllAllDampeningParameters(ShowBgpVrfAllAllDampeningParametersSchema):
    
    '''Parser for 'show bgp vrf all dampening parameters'''
    
    def cli(self):
        cmd = 'show bgp vrf all all dampening parameters'
        out = self.device.execute(cmd)
        bgp_dict = {}
        sub_dict = {}

        for line in out.splitlines():
            line = line.strip()
            p1 = re.compile(r'^Route +(?P<route>\w+) +Dampening +Parameters '
                             '+for +VRF +(?P<vrf>\w+) +Address +family '
                             '+(?P<af_name>[a-zA-Z0-9 ]+):$')
            m = p1.match(line)
            if m:
                if 'vrf' not in bgp_dict:
                    bgp_dict['vrf'] = {}

                vrf = m.groupdict()['vrf']
                if vrf not in bgp_dict['vrf']:
                    bgp_dict['vrf'][vrf] = {}
                    bgp_dict['vrf'][vrf]['address_family'] = {}

                af_name = m.groupdict()['af_name'].lower()
                if af_name not in bgp_dict['vrf'][vrf]['address_family']:
                    bgp_dict['vrf'][vrf]['address_family'][af_name] = {}
                    # trim the coding lines for adopting pep8
                    sub_dict = bgp_dict['vrf'][vrf]['address_family'][af_name]
                    sub_dict['dampening'] = 'True'
                continue

            p9 = re.compile(r'^Route +Distinguisher: +(?P<rd>[0-9\.:]+) +'
                             '\(VRF +(?P<rd_vrf>\w+)\)$')
            m = p9.match(line)
            if m:
                if 'route_distinguisher' not in \
                  bgp_dict['vrf'][vrf]['address_family'][af_name]:
                   bgp_dict['vrf'][vrf]['address_family']\
                     [af_name]['route_distinguisher'] = {}
                rd = m.groupdict()['rd']
                if rd and rd not in bgp_dict['vrf'][vrf]['address_family']\
                  [af_name]['route_distinguisher']:
                    sub_dict = bgp_dict['vrf'][vrf]['address_family']\
                      [af_name]['route_distinguisher'][rd] = {}

                rd_vrf = m.groupdict()['rd_vrf']
                if rd_vrf:
                    sub_dict['rd_vrf'] = rd_vrf
                continue

            p2 = re.compile(r'^Dampening +policy +configured: '
                             '+(?P<route_map>\w+)$')
            m = p2.match(line)
            if m:
                sub_dict['dampening_route_map'] = m.groupdict()['route_map']
                continue

            p3 = re.compile(r'^Half-life +time +: +'
                             '(?P<half_time>[a-zA-Z0-9 ]+)$')
            m = p3.match(line)
            if m:
                sub_dict['dampening_half_life_time'] =\
                   m.groupdict()['half_time']
                continue

            p4 = re.compile(r'^Suppress +penalty +: +'
                             '(?P<suppress_pen>[a-zA-Z0-9 ]+)$')
            m = p4.match(line)
            if m:
                sub_dict['dampening_suppress_time'] =\
                  m.groupdict()['suppress_pen']
                continue

            p5 = re.compile(r'^Reuse +penalty +: +'
                             '(?P<reuse_pen>[a-zA-Z0-9 ]+)$')
            m = p5.match(line)
            if m:
                sub_dict['dampening_reuse_time'] =\
                  m.groupdict()['reuse_pen']
                continue

            p6 = re.compile(r'^Max +suppress +time +: +'
                             '(?P<max_sup_time>[a-zA-Z0-9 ]+)$')
            m = p6.match(line)
            if m:
                sub_dict['dampening_max_suppress_time'] =\
                  m.groupdict()['max_sup_time']
                continue

            p7 = re.compile(r'^Max +suppress +penalty +: '
                             '+(?P<max_sup_pen>[a-zA-Z0-9 ]+)$')
            m = p7.match(line)
            if m:
                sub_dict['dampening_max_suppress_penalty'] =\
                  m.groupdict()['max_sup_pen']
                continue
        return bgp_dict


# ======================================================================
# Parser for 'show bgp vrf <WORD> all neighbors <WORD> advertised-routes'
# ======================================================================

class ShowBgpVrfAllNeighborsAdvertisedRoutesSchema(MetaParser):
    
    '''Schema for show bgp vrf <WORD> all neighbors <WORD> advertised-routes'''

    schema = {
        'vrf':
            {Any():
                {'neighbor':
                    {Any():
                        {'address_family':
                            {Any():
                                {'bgp_table_version': int,
                                 'local_router_id': str,
                                 Optional('route_distinguisher'): str,
                                 Optional('default_vrf'): str,
                                 Optional('advertised'): 
                                    {Optional(Any()):
                                        {Optional('index'):
                                            {Optional(Any()):
                                                {Optional('next_hop'): str,
                                                 Optional('status_codes'): str,
                                                 Optional('path_type'): str,
                                                 Optional('metric'): str,
                                                 Optional('localprf'): str,
                                                 Optional('weight'): str,
                                                 Optional('origin_codes'): str,
                                                },
                                            },
                                        },
                                    },
                                },
                            },

                        },

                    },

                },
            },
        }

class ShowBgpVrfAllNeighborsAdvertisedRoutes(ShowBgpVrfAllNeighborsAdvertisedRoutesSchema):
    
    '''Parser for show bgp vrf <WORD> all neighbors <WORD> advertised-routes'''

    def cli(self, vrf, neighbor):
        cmd  = 'show bgp vrf {vrf} all neighbors {neighbor} advertised-routes'.format(vrf=vrf, neighbor=neighbor)
        out = self.device.execute(cmd)
        
        # Init vars
        route_dict = {}
        data_on_nextline =  False
        index = 1

        bgp_table_version = local_router_id = ''

        for line in out.splitlines():
            line = line.rstrip()

            # Peer 21.0.0.2 routes for address family IPv4 Unicast:
            p1 = re.compile(r'^\s*Peer +(?P<neighbor_id>(\S+)) +routes +for'
                             ' +address +family'
                             ' +(?P<address_family>[a-zA-Z0-9\s\-]+) *:$')
            m = p1.match(line)
            if m:
                if 'vrf' not in route_dict:
                    route_dict['vrf'] = {}
                if vrf not in route_dict['vrf']:
                    route_dict['vrf'][vrf] = {}
                if 'neighbor' not in route_dict['vrf'][vrf]:
                    route_dict['vrf'][vrf]['neighbor'] = {}
                neighbor_id = str(m.groupdict()['neighbor_id'])
                if neighbor_id not in route_dict['vrf'][vrf]['neighbor']:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id] = {}
                if 'address_family' not in route_dict['vrf'][vrf]['neighbor']\
                    [neighbor_id]:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'] = {}
                address_family = str(m.groupdict()['address_family']).lower()
                continue

            # BGP table version is 25, Local Router ID is 21.0.101.1
            p2 = re.compile(r'^\s*BGP +table +version +is'
                             ' +(?P<bgp_table_version>[0-9]+), +Local +Router'
                             ' +ID +is +(?P<local_router_id>(\S+))$')
            m = p2.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                local_router_id = str(m.groupdict()['local_router_id'])
                continue

            # Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
            # Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
            # Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup
            # Network            Next Hop            Metric     LocPrf     Weight Path
            # *>l1.1.1.0/24         0.0.0.0                           100      32768 i
            # *>r1.3.1.0/24         0.0.0.0               4444        100      32768 ?
            # *>r1.3.2.0/24         0.0.0.0               4444        100      32768 ?
            p3 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                             '(?P<path_type>(i|e|c|l|a|r|I))'
                             '(?P<prefix>[a-zA-Z0-9\.\:\/\[\]]+)'
                             '(?: *(?P<next_hop>[a-zA-Z0-9\.\:]+))?'
                             '(?: +(?P<metric>[0-9]+))?'
                             '(?: +(?P<localprf>[0-9]+) +(?P<weight>[0-9]+))?'
                             '(?: +(?P<origin_codes>(i|e|\?|\&|\|)))?$')
            m = p3.match(line)
            if m:
                if address_family not in route_dict['vrf'][vrf]['neighbor']\
                    [neighbor_id]['address_family']:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'][address_family] = {}
                    af_dict = route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'][address_family] = {}

                if 'RD' in address_family:
                    af_dict['route_distinguisher'] = route_distinguisher
                    af_dict['default_vrf'] = default_vrf

                af_dict['bgp_table_version'] = bgp_table_version
                af_dict['local_router_id'] = local_router_id

                # Get keys
                status_codes = str(m.groupdict()['status_codes'])
                path_type = str(m.groupdict()['path_type'])
                prefix = str(m.groupdict()['prefix'])
                next_hop = str(m.groupdict()['next_hop'])
                metric = str(m.groupdict()['metric']).strip()
                localprf = str(m.groupdict()['localprf'])
                weight = str(m.groupdict()['weight'])
                origin_codes = str(m.groupdict()['origin_codes'])

                # Check advertised top level key exists
                if 'advertised' not in af_dict:
                    af_dict['advertised'] = {}
                
                # Check if the prefix exists
                if prefix not in af_dict['advertised']:
                    af_dict['advertised'][prefix] = {}
                
                # Check if index top level key exists
                if 'index' not in af_dict['advertised'][prefix]:
                    af_dict['advertised'][prefix]['index'] = {}

                # Check if current prefix details are on next line
                if next_hop == 'None':
                    data_on_nextline = True
                    continue

                # Check if index exists
                if index not in af_dict['advertised'][prefix]['index']:
                    af_dict['advertised'][prefix]['index'][index] = {}
                    nh_dict = af_dict['advertised'][prefix]['index'][index]
                    nh_dict['next_hop'] = next_hop
                    nh_dict['status_codes'] = status_codes
                    nh_dict['path_type'] = path_type
                    nh_dict['metric'] = metric
                    nh_dict['localprf'] = localprf
                    nh_dict['weight'] = weight
                    nh_dict['origin_codes'] = origin_codes
                    continue

            #                     0.0.0.0                  100      32768 i
            p4 = re.compile(r'^\s*(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                             '(?: +(?P<metric>[a-zA-Z0-9\s\(\)]+))?'
                             ' +(?P<localprf>[0-9]+) +(?P<weight>[0-9]+)'
                             ' +(?P<origin_codes>(i|e|\?|\|))$')
            m = p4.match(line)
            if m:
                # Get keys
                next_hop = str(m.groupdict()['next_hop'])
                metric = str(m.groupdict()['metric']).strip()
                localprf = str(m.groupdict()['localprf'])
                weight = str(m.groupdict()['weight'])
                origin_codes = str(m.groupdict()['origin_codes'])

                # Check if index exists
                if index not in af_dict['advertised'][prefix]['index']:
                    af_dict['advertised'][prefix]['index'][index] = {}
                    nh_dict = af_dict['advertised'][prefix]['index'][index]
                    nh_dict['next_hop'] = next_hop
                    nh_dict['metric'] = metric
                    nh_dict['localprf'] = localprf
                    nh_dict['weight'] = weight
                    nh_dict['origin_codes'] = origin_codes
                    if data_on_nextline:
                        nh_dict['status_codes'] = status_codes
                        nh_dict['path_type'] = path_type
                        data_on_nextline = False
                        continue

            # Network            Next Hop            Metric     LocPrf     Weight Path
            # Route Distinguisher: 100:100     (VRF VRF1)
            # Route Distinguisher: 2:100    (VRF vpn2)
            p5 = re.compile(r'^\s*Route +Distinguisher *:'
                              ' +(?P<route_distinguisher>(\S+))'
                              ' +\(VRF +(?P<default_vrf>(\S+))\)$')
            m = p5.match(line)
            if m:
                route_distinguisher = str(m.groupdict()['route_distinguisher'])
                default_vrf = str(m.groupdict()['default_vrf'])
                if 'RD' in address_family:
                    p = re.compile(r'(?P<afname>.+\s.+) RD')
                    m = p.match(address_family)
                    if m:
                        address_family = m.groupdict()['afname'] + ' RD ' + route_distinguisher
                else:
                    address_family = address_family + ' RD ' + route_distinguisher
                continue

        return route_dict


# ============================================================
# Parser for 'show bgp vrf <WORD> all neighbors <WORD> routes'
# ============================================================

class ShowBgpVrfAllNeighborsRoutesSchema(MetaParser):
    
    '''Schema for show bgp vrf <WORD> all neighbors <WORD> routes'''

    schema = {
        'vrf':
            {Any():
                {'neighbor':
                    {Any():
                        {'address_family':
                            {Any():
                                {'bgp_table_version': int,
                                 'local_router_id': str,
                                 Optional('route_distinguisher'): str,
                                 Optional('default_vrf'): str,
                                 Optional('routes'): 
                                    {Optional(Any()):
                                        {Optional('index'):
                                            {Optional(Any()):
                                                {Optional('next_hop'): str,
                                                 Optional('status_codes'): str,
                                                 Optional('path_type'): str,
                                                 Optional('metric'): str,
                                                 Optional('localprf'): str,
                                                 Optional('weight'): str,
                                                 Optional('origin_codes'): str,
                                                },
                                            },
                                        },
                                    },
                                },
                            },

                        },

                    },

                },
            },
        }

class ShowBgpVrfAllNeighborsRoutes(ShowBgpVrfAllNeighborsRoutesSchema):
    
    '''Parser for show bgp vrf <WORD> all neighbors <WORD> routes'''

    def cli(self, vrf, neighbor):
        cmd  = 'show bgp vrf {vrf} all neighbors {neighbor} routes'.format(vrf=vrf, neighbor=neighbor)
        out = self.device.execute(cmd)

        # Init vars
        route_dict = {}
        data_on_nextline =  False
        index = 1

        bgp_table_version = local_router_id = ''

        for line in out.splitlines():
            line = line.rstrip()

            # Peer 21.0.0.2 routes for address family IPv4 Unicast:
            p1 = re.compile(r'^\s*Peer +(?P<neighbor_id>(\S+)) +routes +for'
                             ' +address +family'
                             ' +(?P<address_family>[a-zA-Z0-9\s]+) *:$')
            m = p1.match(line)
            if m:
                if 'vrf' not in route_dict:
                    route_dict['vrf'] = {}
                if vrf not in route_dict['vrf']:
                    route_dict['vrf'][vrf] = {}
                if 'neighbor' not in route_dict['vrf'][vrf]:
                    route_dict['vrf'][vrf]['neighbor'] = {}
                neighbor_id = str(m.groupdict()['neighbor_id'])
                if neighbor_id not in route_dict['vrf'][vrf]['neighbor']:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id] = {}
                if 'address_family' not in route_dict['vrf'][vrf]['neighbor']\
                    [neighbor_id]:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'] = {}
                address_family = str(m.groupdict()['address_family']).lower()
                continue

            # BGP table version is 25, Local Router ID is 21.0.101.1
            p2 = re.compile(r'^\s*BGP +table +version +is'
                             ' +(?P<bgp_table_version>[0-9]+), +Local +Router'
                             ' +ID +is +(?P<local_router_id>(\S+))$')
            m = p2.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                local_router_id = str(m.groupdict()['local_router_id'])
                continue

            # Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
            # Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
            # Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup
            # Network            Next Hop            Metric     LocPrf     Weight Path
            # *>l1.1.1.0/24         0.0.0.0                           100      32768 i
            # *>r1.3.1.0/24         0.0.0.0               4444        100      32768 ?
            # *>r1.3.2.0/24         0.0.0.0               4444        100      32768 ?
            p3 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                             '(?P<path_type>(i|e|c|l|a|r|I))'
                             '(?P<prefix>[a-zA-Z0-9\.\:\/\[\]]+)'
                             '(?: *(?P<next_hop>[a-zA-Z0-9\.\:]+))?'
                             '(?: +(?P<metric>[0-9]+))?'
                             '(?: +(?P<localprf>[0-9]+) +(?P<weight>[0-9]+))?'
                             '(?: +(?P<origin_codes>(i|e|\?|\&|\|)))?$')
            m = p3.match(line)
            if m:
                if address_family not in route_dict['vrf'][vrf]['neighbor']\
                    [neighbor_id]['address_family']:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'][address_family] = {}
                    af_dict = route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'][address_family] = {}

                if 'RD' in address_family:
                    af_dict['route_distinguisher'] = route_distinguisher
                    af_dict['default_vrf'] = default_vrf

                af_dict['bgp_table_version'] = bgp_table_version
                af_dict['local_router_id'] = local_router_id

                # Get keys
                status_codes = str(m.groupdict()['status_codes'])
                path_type = str(m.groupdict()['path_type'])
                prefix = str(m.groupdict()['prefix'])
                next_hop = str(m.groupdict()['next_hop'])
                metric = str(m.groupdict()['metric']).strip()
                localprf = str(m.groupdict()['localprf'])
                weight = str(m.groupdict()['weight'])
                origin_codes = str(m.groupdict()['origin_codes'])

                # Check routes top level key exists
                if 'routes' not in af_dict:
                    af_dict['routes'] = {}
                
                # Check if the prefix exists
                if prefix not in af_dict['routes']:
                    af_dict['routes'][prefix] = {}
                
                # Check if index top level key exists
                if 'index' not in af_dict['routes'][prefix]:
                    af_dict['routes'][prefix]['index'] = {}

                # Check if current prefix details are on next line
                if next_hop == 'None':
                    data_on_nextline = True
                    continue

                # Check if index exists
                if index not in af_dict['routes'][prefix]['index']:
                    af_dict['routes'][prefix]['index'][index] = {}
                    nh_dict = af_dict['routes'][prefix]['index'][index]
                    nh_dict['next_hop'] = next_hop
                    nh_dict['status_codes'] = status_codes
                    nh_dict['path_type'] = path_type
                    nh_dict['metric'] = metric
                    nh_dict['localprf'] = localprf
                    nh_dict['weight'] = weight
                    nh_dict['origin_codes'] = origin_codes
                    continue

            #                     0.0.0.0                  100      32768 i
            p4 = re.compile(r'^\s*(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                             '(?: +(?P<metric>[a-zA-Z0-9\s\(\)]+))?'
                             ' +(?P<localprf>[0-9]+) +(?P<weight>[0-9]+)'
                             ' +(?P<origin_codes>(i|e|\?|\|))$')
            m = p4.match(line)
            if m:
                # Get keys
                next_hop = str(m.groupdict()['next_hop'])
                metric = str(m.groupdict()['metric']).strip()
                localprf = str(m.groupdict()['localprf'])
                weight = str(m.groupdict()['weight'])
                origin_codes = str(m.groupdict()['origin_codes'])

                # Check if index exists
                if index not in af_dict['routes'][prefix]['index']:
                    af_dict['routes'][prefix]['index'][index] = {}
                    nh_dict = af_dict['routes'][prefix]['index'][index]
                    nh_dict['next_hop'] = next_hop
                    nh_dict['metric'] = metric
                    nh_dict['localprf'] = localprf
                    nh_dict['weight'] = weight
                    nh_dict['origin_codes'] = origin_codes
                    if data_on_nextline:
                        nh_dict['status_codes'] = status_codes
                        nh_dict['path_type'] = path_type
                        data_on_nextline = False
                        continue

            # Network            Next Hop            Metric     LocPrf     Weight Path
            # Route Distinguisher: 100:100     (VRF VRF1)
            # Route Distinguisher: 2:100    (VRF vpn2)
            p5 = re.compile(r'^\s*Route +Distinguisher *:'
                              ' +(?P<route_distinguisher>(\S+))'
                              ' +\(VRF +(?P<default_vrf>(\S+))\)$')
            m = p5.match(line)
            if m:
                route_distinguisher = str(m.groupdict()['route_distinguisher'])
                default_vrf = str(m.groupdict()['default_vrf'])
                if 'RD' in address_family:
                    p = re.compile(r'(?P<afname>.+\s.+) RD')
                    m = p.match(address_family)
                    if m:
                        address_family = m.groupdict()['afname'] + ' RD ' + route_distinguisher
                else:
                    address_family = address_family + ' RD ' + route_distinguisher
                    str(m.groupdict()['default_vrf'])
                continue

        return route_dict


# =====================================================================
# Parser for 'show bgp vrf <WORD> all neighbors <WORD> received-routes'
# =====================================================================

class ShowBgpVrfAllNeighborsReceivedRoutesSchema(MetaParser):
    
    '''Schema for show bgp vrf <WORD> all neighbors <WORD> routes'''

    schema = {
        'vrf':
            {Any():
                {'neighbor':
                    {Any():
                        {'address_family':
                            {Any():
                                {'bgp_table_version': int,
                                 'local_router_id': str,
                                 Optional('route_distinguisher'): str,
                                 Optional('default_vrf'): str,
                                 Optional('received_routes'): 
                                    {Optional(Any()):
                                        {Optional('index'):
                                            {Optional(Any()):
                                                {Optional('next_hop'): str,
                                                 Optional('status_codes'): str,
                                                 Optional('path_type'): str,
                                                 Optional('metric'): str,
                                                 Optional('localprf'): str,
                                                 Optional('weight'): str,
                                                 Optional('origin_codes'): str,
                                                },
                                            },
                                        },
                                    },
                                },
                            },

                        },

                    },

                },
            },
        }

class ShowBgpVrfAllNeighborsReceivedRoutes(ShowBgpVrfAllNeighborsReceivedRoutesSchema):
    
    '''Parser for show bgp vrf <WORD> all neighbors <WORD> received-routes'''

    def cli(self, vrf, neighbor):
        cmd  = 'show bgp vrf {vrf} all neighbors {neighbor} received-routes'.format(vrf=vrf, neighbor=neighbor)
        out = self.device.execute(cmd)

        # Init vars
        route_dict = {}
        data_on_nextline =  False
        index = 1

        bgp_table_version = local_router_id = ''

        for line in out.splitlines():
            line = line.rstrip()

            # Peer 21.0.0.2 routes for address family IPv4 Unicast:
            p1 = re.compile(r'^\s*Peer +(?P<neighbor_id>(\S+)) +routes +for'
                             ' +address +family'
                             ' +(?P<address_family>[a-zA-Z0-9\s]+) *:$')
            m = p1.match(line)
            if m:
                if 'vrf' not in route_dict:
                    route_dict['vrf'] = {}
                if vrf not in route_dict['vrf']:
                    route_dict['vrf'][vrf] = {}
                if 'neighbor' not in route_dict['vrf'][vrf]:
                    route_dict['vrf'][vrf]['neighbor'] = {}
                neighbor_id = str(m.groupdict()['neighbor_id'])
                if neighbor_id not in route_dict['vrf'][vrf]['neighbor']:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id] = {}
                if 'address_family' not in route_dict['vrf'][vrf]['neighbor']\
                    [neighbor_id]:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'] = {}
                address_family = str(m.groupdict()['address_family']).lower()
                continue

            # BGP table version is 25, Local Router ID is 21.0.101.1
            p2 = re.compile(r'^\s*BGP +table +version +is'
                             ' +(?P<bgp_table_version>[0-9]+), +Local +Router'
                             ' +ID +is +(?P<local_router_id>(\S+))$')
            m = p2.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                local_router_id = str(m.groupdict()['local_router_id'])
                continue

            # Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
            # Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
            # Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup
            # Network            Next Hop            Metric     LocPrf     Weight Path
            # *>l1.1.1.0/24         0.0.0.0                           100      32768 i
            # *>r1.3.1.0/24         0.0.0.0               4444        100      32768 ?
            # *>r1.3.2.0/24         0.0.0.0               4444        100      32768 ?
            p3 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                             '(?P<path_type>(i|e|c|l|a|r|I))'
                             '(?P<prefix>[a-zA-Z0-9\.\:\/\[\]]+)'
                             '(?: *(?P<next_hop>[a-zA-Z0-9\.\:]+))?'
                             '(?: +(?P<metric>[0-9]+))?'
                             '(?: +(?P<localprf>[0-9]+) +(?P<weight>[0-9]+))?'
                             '(?: +(?P<origin_codes>(i|e|\?|\&|\|)))?$')
            m = p3.match(line)
            if m:
                if address_family not in route_dict['vrf'][vrf]['neighbor']\
                    [neighbor_id]['address_family']:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'][address_family] = {}
                    af_dict = route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'][address_family] = {}

                if 'RD' in address_family:
                    af_dict['route_distinguisher'] = route_distinguisher
                    af_dict['default_vrf'] = default_vrf

                af_dict['bgp_table_version'] = bgp_table_version
                af_dict['local_router_id'] = local_router_id

                # Get keys
                status_codes = str(m.groupdict()['status_codes'])
                path_type = str(m.groupdict()['path_type'])
                prefix = str(m.groupdict()['prefix'])
                next_hop = str(m.groupdict()['next_hop'])
                metric = str(m.groupdict()['metric']).strip()
                localprf = str(m.groupdict()['localprf'])
                weight = str(m.groupdict()['weight'])
                origin_codes = str(m.groupdict()['origin_codes'])

                # Check received_routes top level key exists
                if 'received_routes' not in af_dict:
                    af_dict['received_routes'] = {}
                
                # Check if the prefix exists
                if prefix not in af_dict['received_routes']:
                    af_dict['received_routes'][prefix] = {}
                
                # Check if index top level key exists
                if 'index' not in af_dict['received_routes'][prefix]:
                    af_dict['received_routes'][prefix]['index'] = {}

                # Check if current prefix details are on next line
                if next_hop == 'None':
                    data_on_nextline = True
                    continue

                # Check if index exists
                if index not in af_dict['received_routes'][prefix]['index']:
                    af_dict['received_routes'][prefix]['index'][index] = {}
                    nh_dict = af_dict['received_routes'][prefix]['index'][index]
                    nh_dict['next_hop'] = next_hop
                    nh_dict['status_codes'] = status_codes
                    nh_dict['path_type'] = path_type
                    nh_dict['metric'] = metric
                    nh_dict['localprf'] = localprf
                    nh_dict['weight'] = weight
                    nh_dict['origin_codes'] = origin_codes
                    continue

            #                     0.0.0.0                  100      32768 i
            p4 = re.compile(r'^\s*(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                             '(?: +(?P<metric>[a-zA-Z0-9\s\(\)]+))?'
                             ' +(?P<localprf>[0-9]+) +(?P<weight>[0-9]+)'
                             ' +(?P<origin_codes>(i|e|\?|\|))$')
            m = p4.match(line)
            if m:
                # Get keys
                next_hop = str(m.groupdict()['next_hop'])
                metric = str(m.groupdict()['metric']).strip()
                localprf = str(m.groupdict()['localprf'])
                weight = str(m.groupdict()['weight'])
                origin_codes = str(m.groupdict()['origin_codes'])

                # Check if index exists
                if index not in af_dict['received_routes'][prefix]['index']:
                    af_dict['received_routes'][prefix]['index'][index] = {}
                    nh_dict = af_dict['received_routes'][prefix]['index'][index]
                    nh_dict['next_hop'] = next_hop
                    nh_dict['metric'] = metric
                    nh_dict['localprf'] = localprf
                    nh_dict['weight'] = weight
                    nh_dict['origin_codes'] = origin_codes
                    if data_on_nextline:
                        nh_dict['status_codes'] = status_codes
                        nh_dict['path_type'] = path_type
                        data_on_nextline = False
                        continue

            # Network            Next Hop            Metric     LocPrf     Weight Path
            # Route Distinguisher: 100:100     (VRF VRF1)
            # Route Distinguisher: 2:100    (VRF vpn2)
            p5 = re.compile(r'^\s*Route +Distinguisher *:'
                              ' +(?P<route_distinguisher>(\S+))'
                              ' +\(VRF +(?P<default_vrf>(\S+))\)$')
            m = p5.match(line)
            if m:
                route_distinguisher = str(m.groupdict()['route_distinguisher'])
                default_vrf = str(m.groupdict()['default_vrf'])
                if 'RD' in address_family:
                    p = re.compile(r'(?P<afname>.+\s.+) RD')
                    m = p.match(address_family)
                    if m:
                        address_family = m.groupdict()['afname'] + ' RD ' + route_distinguisher
                else:
                    address_family = address_family + ' RD ' + route_distinguisher
                continue

        return route_dict


# ====================================
# Parser for 'show running-config bgp'
# ====================================

class ShowRunningConfigBgpSchema(MetaParser):

    '''Schema for show running-config bgp'''

    schema = {'bgp':
                {'bgp_id': int,
                 'protocol_shutdown': bool,
                 Optional('ps_name'):
                    {Any():
                        {'ps_fall_over_bfd': bool,
                         'ps_suppress_four_byte_as_capability': bool,
                         Optional('ps_description'): str,
                         'ps_disable_connected_check': bool,
                         'ps_ebgp_multihop': bool,
                         Optional('ps_ebgp_multihop_max_hop'): int,
                         Optional('ps_local_as_as_no'): int,
                         'ps_local_as_no_prepend': bool,
                         'ps_local_as_dual_as': bool,
                         'ps_local_as_replace_as': bool,
                         Optional('ps_password_text'): str,
                         Optional('ps_remote_as'): int,
                         'ps_shutdown': bool,
                         Optional('ps_keepalive_interval'): int,
                         Optional('ps_hodltime'): int,
                         Optional('ps_transport_connection_mode'): str,
                         Optional('ps_update_source'): str}
                    },
                 Optional('pp_name'):
                    {Any():
                        {Optional('pp_allowas_in'): bool,
                         'pp_allowas_in_as_number': int,
                         'pp_as_override': bool,
                         'pp_default_originate': bool,
                         Optional('pp_default_originate_route_map'): str,
                         Optional('pp_route_map_name_in'): str,
                         Optional('pp_route_map_name_out'): str,
                         Optional('pp_maximum_prefix_max_prefix_no'): int,
                         Optional('pp_maximum_prefix_threshold'): int,
                         Optional('pp_maximum_prefix_restart'): int,
                         Optional('pp_maximum_prefix_warning_only'): bool,
                         'pp_next_hop_self': bool,
                         'pp_route_reflector_client': bool,
                         Optional('pp_send_community'): str,
                         'pp_soft_reconfiguration': bool,
                         Optional('pp_soo'): str}
                    },
                 'vrf':
                    {Any():
                        {Optional('always_compare_med'): bool,
                         Optional('bestpath_compare_routerid'): bool,
                         Optional('bestpath_cost_community_ignore'): bool,
                         Optional('bestpath_med_missing_at_worst'): bool,
                         Optional('cluster_id'): str,
                         Optional('confederation_identifier'): int,
                         Optional('confederation_peers_as'): str,
                         'graceful_restart': bool,
                         Optional('graceful_restart_restart_time'): int,
                         Optional('graceful_restart_stalepath_time'): int,
                         'log_neighbor_changes': bool,
                         Optional('router_id'): str,
                         Optional('keepalive_interval'): int,
                         Optional('holdtime'): int,
                         'enforce_first_as': bool,
                         'fast_external_fallover': bool,
                         Optional('default_choice_ipv4_unicast'): str,
                         Optional('dynamic_med_interval'): int,
                         Optional('shutdown'): str,
                         'flush_routes': bool,
                         'isolate': bool,
                         Optional('disable_policy_batching_ipv4'): str,
                         Optional('disable_policy_batching_ipv6'): str,
                         Optional('af_name'):
                            {Any():
                                {Optional('af_dampening'): bool,
                                 Optional('af_dampening_route_map'): str,
                                 Optional('af_dampening_half_life_time'): int,
                                 Optional('af_dampening_reuse_time'): int,
                                 Optional('af_dampening_suppress_time'): int,
                                 Optional('af_dampening_max_suppress_time'): int,
                                 Optional('af_nexthop_route_map'): str,
                                 Optional('af_nexthop_trigger_enable'): bool,
                                 Optional('af_nexthop_trigger_delay_critical'): int,
                                 Optional('af_nexthop_trigger_delay_non_critical'): int,
                                 Optional('af_client_to_client_reflection'): bool,
                                 Optional('af_distance_extern_as'): int,
                                 Optional('af_distance_internal_as'): int,
                                 Optional('af_distance_local'): int,
                                 Optional('af_maximum_paths_ebgp'): int,
                                 Optional('af_maximum_paths_ibgp'): int,
                                 Optional('af_maximum_paths_eibgp'): int,
                                 Optional('af_aggregate_address_ipv4_address'): str,
                                 Optional('af_aggregate_address_ipv4_mask'): int,
                                 Optional('af_aggregate_address_as_set'): bool,
                                 Optional('af_aggregate_address_summary_only'): bool,
                                 Optional('af_network_number'): str,
                                 Optional('af_network_mask'): int,
                                 Optional('af_network_route_map'): str,
                                 Optional('af_redist_isis'): str,
                                 Optional('af_redist_isis_metric'): str,
                                 Optional('af_redist_isis_route_policy'): str,
                                 Optional('af_redist_ospf'): str,
                                 Optional('af_redist_ospf_metric'): str,
                                 Optional('af_redist_ospf_route_policy'): str,
                                 Optional('af_redist_rip'): str,
                                 Optional('af_redist_rip_metric'): str,
                                 Optional('af_redist_rip_route_policy'): str,
                                 Optional('af_redist_static'): bool,
                                 Optional('af_redist_static_metric'): str,
                                 Optional('af_redist_static_route_policy'): str,
                                 Optional('af_redist_connected'): bool,
                                 Optional('af_redist_connected_metric'): str,
                                 Optional('af_redist_connected_route_policy'): str,
                                 Optional('af_v6_aggregate_address_ipv6_address'): str,
                                 Optional('af_v6_aggregate_address_as_set'): bool,
                                 Optional('af_v6_aggregate_address_summary_only'): bool,
                                 Optional('af_v6_network_number'): str,
                                 Optional('af_v6_network_route_map'): str,
                                 Optional('af_v6_allocate_label_all'): bool,
                                 Optional('af_retain_rt_all'): bool,
                                 Optional('af_label_allocation_mode'): str}
                            },
                         Optional('neighbor_id'):
                            {Any():
                                {Optional('nbr_fall_over_bfd'): bool,
                                 Optional('nbr_suppress_four_byte_as_capability'): bool,
                                 Optional('nbr_description'): str,
                                 Optional('nbr_disable_connected_check'): bool,
                                 Optional('nbr_ebgp_multihop'): bool,
                                 Optional('nbr_ebgp_multihop_max_hop'): int,
                                 Optional('nbr_inherit_peer_session'): str,
                                 Optional('nbr_local_as_as_no'): str,
                                 Optional('nbr_local_as_no_prepend'): bool,
                                 Optional('nbr_local_as_replace_as'): bool,
                                 Optional('nbr_local_as_dual_as'): bool,
                                 Optional('nbr_remote_as'): int,
                                 Optional('nbr_remove_private_as'): bool,
                                 Optional('nbr_shutdown'): bool,
                                 Optional('nbr_keepalive_interval'): int,
                                 Optional('nbr_holdtime'): int,
                                 Optional('nbr_update_source'): str,
                                 Optional('nbr_password_text'): str,
                                 Optional('nbr_transport_connection_mode'): str,
                                 Optional('nbr_af_name'):
                                    {Any():
                                        {Optional('nbr_af_allowas_in'): bool,
                                         Optional('nbr_af_allowas_in_as_number'): int,
                                         Optional('nbr_af_inherit_peer_policy'): str,
                                         Optional('nbr_af_inherit_peer_seq'): int,
                                         Optional('nbr_af_maximum_prefix_max_prefix_no'): int,
                                         Optional('nbr_af_maximum_prefix_threshold'): int,
                                         Optional('nbr_af_maximum_prefix_restart'): int,
                                         Optional('nbr_af_maximum_prefix_warning_only'): bool,
                                         Optional('nbr_af_route_map_name_in'): str,
                                         Optional('nbr_af_route_map_name_out'): str,
                                         Optional('nbr_af_route_reflector_client'): bool,
                                         Optional('nbr_af_send_community'): str,
                                         Optional('nbr_af_soft_reconfiguration'): bool,
                                         Optional('nbr_af_next_hop_self'): bool,
                                         Optional('nbr_af_as_override'): bool,
                                         Optional('nbr_af_default_originate'): bool,
                                         Optional('nbr_af_default_originate_route_map'): str,
                                         Optional('nbr_af_soo'): str}
                                    },
                                }
                            },
                        }
                    },
                }
            }


class ShowRunningConfigBgp(ShowRunningConfigBgpSchema):

    '''Parser for show running-config bgp'''

    def cli(self):
        cmd  = 'show running-config bgp'
        out = self.device.execute(cmd)

        # Init vars
        bgp_dict = {}
        bgp_id = ''
        protocol_shutdown = False
        send_community_standard_match = 'False'
        peer_policy_send_community_standard_match = 'False'
        neighbor_id = ''
        af_name = ''
        nbr_af_name = ''
        ps_name = ''
        pp_name = ''

        for line in out.splitlines():
            line = line.rstrip()
            # router bgp 333
            p1 = re.compile(r'^\s*router +bgp +(?P<bgp_id>[0-9]+)$')
            m = p1.match(line)
            if m:
                bgp_id = int(m.groupdict()['bgp_id'])
                if 'bgp' not in bgp_dict:
                    bgp_dict['bgp'] = {}
                bgp_dict['bgp']['bgp_id'] = bgp_id
                bgp_dict['bgp']['protocol_shutdown'] = protocol_shutdown
                vrf = 'default'
                if 'vrf' not in bgp_dict['bgp']:
                    bgp_dict['bgp']['vrf'] = {}
                if vrf not in bgp_dict['bgp']['vrf']:
                    bgp_dict['bgp']['vrf'][vrf] = {}
                continue

            if bgp_id:
                #   shutdown
                p2 = re.compile(r'^\s*shutdown$')
                m = p2.match(line)
                if m:
                    bgp_dict['bgp']['protocol_shutdown'] = True
                    continue

                #   vrf vpn1
                p3 = re.compile(r'^\s*vrf +(?P<vrf>[a-z0-9]+)$')
                m = p3.match(line)
                if m:
                    # Get keys
                    vrf = str(m.groupdict()['vrf'])
                    af_name = ''
                    neighbor_id = ''
                    nbr_af_name = ''
                    if 'vrf' not in bgp_dict['bgp']:
                        bgp_dict['bgp']['vrf'] = {}
                    if vrf not in bgp_dict['bgp']['vrf']:
                        bgp_dict['bgp']['vrf'][vrf] = {}
                    continue

                if vrf:
                    #   bestpath cost-community ignore
                    #   bestpath compare-routerid
                    #   bestpath med missing-as-worst
                    #   bestpath always-compare-med
                    p4 = re.compile(r'^\s*bestpath +(?P<best_path>[a-z\-\s]+)$')
                    m = p4.match(line)
                    if m:
                        # Get keys
                        best_path = str(m.groupdict()['best_path'])
                        # Initialize variables
                        bgp_dict['bgp']['vrf'][vrf]['always_compare_med'] = \
                            False
                        bgp_dict['bgp']['vrf'][vrf]['bestpath_compare_routerid'] = \
                            False
                        bgp_dict['bgp']['vrf'][vrf]['bestpath_cost_community_ignore'] = \
                            False
                        bgp_dict['bgp']['vrf'][vrf]['bestpath_med_missing_at_worst'] = \
                            False
                        if best_path == 'cost-community ignore':
                            bgp_dict['bgp']['vrf'][vrf]['bestpath_cost_community_ignore'] = True
                        elif best_path == 'compare-routerid':
                            bgp_dict['bgp']['vrf'][vrf]['bestpath_compare_routerid'] = True
                        elif best_path == 'med missing-as-worst':
                            bgp_dict['bgp']['vrf'][vrf]['bestpath_med_missing_at_worst'] = True
                        elif best_path == 'always-compare-med':
                            bgp_dict['bgp']['vrf'][vrf]['always_compare_med'] = True
                        continue

                    #   cluster-id <cluster_id>
                    p5 = re.compile(r'^\s*cluster-id +(?P<cluster_id>[0-9\.]+)$')
                    m = p5.match(line)
                    if m:
                        bgp_dict['bgp']['vrf'][vrf]['cluster_id'] = \
                            str(m.groupdict()['cluster_id'])
                        continue

                    #   confederation identifier <confederation_identifier>
                    p6 = re.compile(r'^\s*confederation +identifier +(?P<confederation_identifier>[0-9]+)$')
                    m = p6.match(line)
                    if m:
                        bgp_dict['bgp']['vrf'][vrf]['confederation_identifier'] = \
                            int(m.groupdict()['confederation_identifier'])
                        continue

                    #   confederation peers <confederation_peers_as>
                    p7 = re.compile(r'^\s*confederation +peers +(?P<confederation_peers_as>[0-9]+)$')
                    m = p7.match(line)
                    if m:
                        bgp_dict['bgp']['vrf'][vrf]['confederation_peers_as'] = \
                            str(m.groupdict()['confederation_peers_as'])
                        continue

                    #   no graceful-restart
                    p8 = re.compile(r'^\s*no graceful-restart$')
                    m = p8.match(line)
                    if m:
                        bgp_dict['bgp']['vrf'][vrf]['graceful_restart'] = False
                        continue
                    elif 'graceful_restart' not in bgp_dict['bgp']['vrf'][vrf]:
                        bgp_dict['bgp']['vrf'][vrf]['graceful_restart'] = True

                    #   graceful-restart restart-time 121
                    #   graceful-restart stalepath-time 301
                    p9 = re.compile(r'^\s*graceful-restart'
                                     ' +(?P<graceful_restart_type>[a-z\-]+)'
                                     ' +(?P<time>[0-9]+)$')
                    m = p9.match(line)
                    if m:
                        graceful_restart_type = \
                            str(m.groupdict()['graceful_restart_type'])
                        if graceful_restart_type == 'restart-time':
                            bgp_dict['bgp']['vrf'][vrf][
                                'graceful_restart_restart_time'] = \
                                    int(m.groupdict()['time'])
                        else:
                            bgp_dict['bgp']['vrf'][vrf][
                                'graceful_restart_stalepath_time'] = \
                                    int(m.groupdict()['time'])
                        continue

                    #   log-neighbor-changes
                    p10 = re.compile(r'^\s*log-neighbor-changes$')
                    m = p10.match(line)
                    if m:
                        bgp_dict['bgp']['vrf'][vrf]['log_neighbor_changes'] = True
                        continue
                    elif 'log_neighbor_changes' not in bgp_dict['bgp']['vrf'][vrf]:
                        bgp_dict['bgp']['vrf'][vrf]['log_neighbor_changes'] = False

                    #   router-id <router-id>
                    p11 = re.compile(r'^\s*router-id +(?P<router_id>[0-9]+)$')
                    m = p11.match(line)
                    if m:
                        bgp_dict['bgp']['vrf'][vrf]['router_id'] = \
                            str(m.groupdict()['router_id'])
                        continue

                    #   timers bgp <keepalive-interval> <holdtime>
                    p12 = re.compile(r'^\s*timers +bgp +(?P<keepalive_interval>[0-9]+)'
                                      ' +(?P<holdtime>[0-9]+)$')
                    m = p12.match(line)
                    if m:
                        bgp_dict['bgp']['vrf'][vrf]['keepalive_interval'] = \
                            int(m.groupdict()['keepalive_interval'])
                        bgp_dict['bgp']['vrf'][vrf]['holdtime'] = \
                            int(m.groupdict()['holdtime'])
                        continue

                    #   no enforce-first-as
                    p13 = re.compile(r'^\s*no enforce-first-as$')
                    m = p13.match(line)
                    if m:
                        bgp_dict['bgp']['vrf'][vrf]['enforce_first_as'] = False
                        continue
                    elif 'enforce_first_as' not in bgp_dict['bgp']['vrf'][vrf]:
                        bgp_dict['bgp']['vrf'][vrf]['enforce_first_as'] = True

                    #   no fast-external-fallover
                    p14 = re.compile(r'^\s*no fast-external-fallover$')
                    m = p14.match(line)
                    if m:
                        bgp_dict['bgp']['vrf'][vrf]['fast_external_fallover'] = False
                        continue
                    elif 'fast_external_fallover' not in bgp_dict['bgp']['vrf'][vrf]:
                        bgp_dict['bgp']['vrf'][vrf]['fast_external_fallover'] = True

                    #   dynamic-med-interval 70
                    p15 = re.compile(r'^\s*dynamic-med-interval +(?P<dynamic_med_interval>[0-9]+)$')
                    m = p15.match(line)
                    if m:
                        bgp_dict['bgp']['vrf'][vrf]['dynamic_med_interval'] = \
                            int(m.groupdict()['dynamic_med_interval'])
                        continue

                    #   flush-routes
                    p16 = re.compile(r'^\s*flush-routes$')
                    m = p16.match(line)
                    if m:
                        bgp_dict['bgp']['vrf'][vrf]['flush_routes'] = True
                        continue
                    elif 'flush_routes' not in bgp_dict['bgp']['vrf'][vrf]:
                        bgp_dict['bgp']['vrf'][vrf]['flush_routes'] = False

                    #   isolate
                    p17 = re.compile(r'^\s*isolate$')
                    m = p17.match(line)
                    if m:
                        bgp_dict['bgp']['vrf'][vrf]['isolate'] = True
                        continue
                    elif 'isolate' not in bgp_dict['bgp']['vrf'][vrf]:
                        bgp_dict['bgp']['vrf'][vrf]['isolate'] = False

                    #   disable-policy-batching ipv4 prefix-list <WORD>
                    p18 = re.compile(r'^\s*disable-policy-batching ipv4 prefix-list +(?P<disable_policy_batching_ipv4>[a-zA-Z0-9]+)$')
                    m = p18.match(line)
                    if m:
                        bgp_dict['bgp']['vrf'][vrf]['disable_policy_batching_ipv4'] = \
                            str(m.groupdict()['disable_policy_batching_ipv4'])
                        continue

                    #   disable-policy-batching ipv4 prefix-list <WORD>
                    p19 = re.compile(r'^\s*disable-policy-batching ipv6 prefix-list +(?P<disable_policy_batching_ipv6>[a-zA-Z0-9]+)$')
                    m = p19.match(line)
                    if m:
                        bgp_dict['bgp']['vrf'][vrf]['disable_policy_batching_ipv6'] = \
                            str(m.groupdict()['disable_policy_batching_ipv6'])
                        continue

                    if neighbor_id == '':
                        #   address-family ipv4 multicast
                        p20 = re.compile(r'^\s*address-family +(?P<af_name>[a-z0-9\-\s]+)$')
                        m = p20.match(line)
                        if m:
                            # Get keys
                            af_name = str(m.groupdict()['af_name'])
                            if 'af_name' not in bgp_dict['bgp']['vrf'][vrf]:
                                bgp_dict['bgp']['vrf'][vrf]['af_name'] = {}
                            if af_name not in bgp_dict['bgp']['vrf'][vrf]['af_name']:
                                bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name] = {}
                            continue

                    if af_name:
                        #    dampening [ { <af_dampening_half_life_time>
                        #    <af_dampening_resuse_time> <af_dampening_suppress_time>
                        #    <af_dampening_max_suppress_time> } |
                        #    { route-map <af_dampening_route_map> } ]
                        p21 = re.compile(r'^\s*dampening '
                                          '+(?P<af_dampening_half_life_time>[0-9]+) '
                                          '+(?P<af_dampening_reuse_time>[0-9]+) '
                                          '+(?P<af_dampening_suppress_time>[0-9]+) '
                                          '+(?P<af_dampening_max_suppress_time>[0-9]+)$')
                        m = p21.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_dampening'] = \
                                True
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_dampening_half_life_time'] = \
                                int(m.groupdict()['af_dampening_half_life_time'])
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_dampening_reuse_time'] = \
                                int(m.groupdict()['af_dampening_reuse_time'])
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_dampening_suppress_time'] = \
                                int(m.groupdict()['af_dampening_suppress_time'])
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_dampening_max_suppress_time'] = \
                                int(m.groupdict()['af_dampening_max_suppress_time'])
                            continue

                        #    dampening [ { route-map <af_dampening_route_map> } ]
                        p22 = re.compile(r'^\s*dampening +route-map +(?P<af_dampening_route_map>[A-Z0-9\-\_]+)$')
                        m = p22.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_dampening'] = \
                                True
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_dampening_route_map'] = \
                                str(m.groupdict()['af_dampening_route_map'])
                            continue

                        #    nexthop route-map <af_nexthop_route_map>
                        p23 = re.compile(r'^\s*nexthop +route-map +(?P<af_nexthop_route_map>[A-Za-z0-9\-\_]+)$')
                        m = p23.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_nexthop_route_map'] = \
                                str(m.groupdict()['af_nexthop_route_map'])
                            continue

                        #     { nexthop trigger-delay critical
                        #     <af_nexthop_trigger_delay_critical> non-critical
                        #     <af_nexthop_trigger_delay_non_critical> } |
                        #     { no nexthop trigger-delay }
                        p24 = re.compile(r'^\s*nexthop +trigger-delay +critical +(?P<af_nexthop_trigger_delay_critical>[0-9]+) +non-critical +(?P<af_nexthop_trigger_delay_non_critical>[0-9]+)$')
                        m = p24.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_nexthop_trigger_enable'] = \
                                True
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_nexthop_trigger_delay_critical'] = \
                                int(m.groupdict()['af_nexthop_trigger_delay_critical'])
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_nexthop_trigger_delay_non_critical'] = \
                                int(m.groupdict()['af_nexthop_trigger_delay_non_critical'])
                            continue

                        #     {no nexthop trigger-delay }
                        p25 = re.compile(r'^\s*no nexthop trigger-delay$')
                        m = p25.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_nexthop_trigger_enable'] = \
                                False
                            continue

                        #     {no client-to-client reflection }
                        p26 = re.compile(r'^\s*no client-to-client reflection$')
                        m = p26.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_client_to_client_reflection'] = \
                                False
                            continue
                        elif 'af_client_to_client_reflection' not in bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]:
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_client_to_client_reflection'] = \
                                True

                        #    distance <af_distance_extern_as> <af_distance_internal_as> <af_distance_local> | no distance [ <af_distance_extern_as> <af_distance_internal_as> <af_distance_local> ]
                        p27 = re.compile(r'^\s*distance +(?P<af_distance_extern_as>[0-9]+) +(?P<af_distance_internal_as>[0-9]+) +(?P<af_distance_local>[0-9]+)$')
                        m = p27.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_distance_extern_as'] = \
                                int(m.groupdict()['af_distance_extern_as'])
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_distance_internal_as'] = \
                                int(m.groupdict()['af_distance_internal_as'])
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_distance_local'] = \
                                int(m.groupdict()['af_distance_local'])
                            continue

                        #    maximum-paths <af_maximum_paths_ebgp>
                        #    maximum-paths ibgp <af_maximum_paths_ibgp>
                        p28 = re.compile(r'^\s*maximum-paths( +(?P<af_maximum_paths_type>[a-z]+))? +(?P<af_maximum_paths_value>[0-9]+)$')
                        m = p28.match(line)
                        if m:
                            if m.groupdict()['af_maximum_paths_type']:
                                bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_maximum_paths_ibgp'] = \
                                    int(m.groupdict()['af_maximum_paths_value'])
                            else:
                                bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_maximum_paths_ebgp'] = \
                                    int(m.groupdict()['af_maximum_paths_value'])
                            continue

                        #    maximum-paths eibgp <af_maximum_paths_eibgp>
                        p29 = re.compile(r'^\s*maximum-paths +eibgp +(?P<af_maximum_paths_eibgp>[0-9]+)$')
                        m = p29.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_maximum_paths_eibgp'] = \
                                int(m.groupdict()['af_maximum_paths_eibgp'])
                            continue

                        #    aggregate-address <af_aggregate_address_ipv4_address>/<af_aggregate_address_ipv4_mask> [ as-set | summary-only ] +
                        #    aggregate-address <af_v6_aggregate_address_ipv6_address> [ as-set | summary-only ] +
                        p30 = re.compile(r'^\s*aggregate-address +(?P<af_aggregate_address_address>[a-z0-9\.\:]+)(\/(?P<af_aggregate_address_ipv4_mask>[0-9]+))?( +(?P<extra_line>[a-z\-\s]+))?$')
                        m = p30.match(line)
                        if m:
                            ip_address = str(m.groupdict()['af_aggregate_address_address'])
                            if '::' not in ip_address:
                                bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_aggregate_address_ipv4_address'] = \
                                    ip_address
                                bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_aggregate_address_ipv4_mask'] = \
                                    int(m.groupdict()['af_aggregate_address_ipv4_mask'])
                                if m.groupdict()['extra_line']:
                                    if m.groupdict()['extra_line'] == 'as-set':
                                        bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_aggregate_address_as_set'] = \
                                            True
                                    elif m.groupdict()['extra_line'] == 'summary-only':
                                        bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_aggregate_address_summary_only'] = \
                                            True
                                    elif m.groupdict()['extra_line'] == 'as-set summary-only':
                                        bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_aggregate_address_as_set'] = \
                                            True
                                        bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_aggregate_address_summary_only'] = \
                                            True
                            else:
                                bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_v6_aggregate_address_ipv6_address'] = \
                                    ip_address
                                if m.groupdict()['extra_line']:
                                    if m.groupdict()['extra_line'] == 'as-set':
                                        bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_v6_aggregate_address_as_set'] = \
                                            True
                                    elif m.groupdict()['extra_line'] == 'summary-only':
                                        bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_v6_aggregate_address_summary_only'] = \
                                            True
                                    elif m.groupdict()['extra_line'] == 'as-set summary-only':
                                        bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_v6_aggregate_address_as_set'] = \
                                            True
                                        bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_v6_aggregate_address_summary_only'] = \
                                            True
                            continue

                        #    network { <af_network_number> mask <af_network_mask> } [ route-map <rmap-name> ] +
                        #    network <af_v6_network_number> [ route-map <af_v6_network_route_map> ] +
                        p31 = re.compile(r'^\s*network +(?P<af_network_number>[0-9\.\:\/]+)( +mask +(?P<af_network_mask>[0-9\.]+))?( +route-map +(?P<af_network_route_map>[A-Za-z0-9\-\_]+))?$')
                        m = p31.match(line)
                        if m:
                            if m.groupdict()['af_network_mask']:
                                bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_network_number'] = \
                                    str(m.groupdict()['af_network_number'])
                                bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_network_mask'] = \
                                    str(m.groupdict()['af_network_mask'])
                                if m.groupdict()['af_network_route_map']:
                                    bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_network_route_map'] = \
                                        str(m.groupdict()['af_network_route_map'])
                            else:
                                bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_v6_network_number'] = \
                                    str(m.groupdict()['af_network_number'])
                                if m.groupdict()['af_network_route_map']:
                                    bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_v6_network_route_map'] = \
                                        str(m.groupdict()['af_network_route_map'])
                            continue

                        #    network { <af_network_number>/<ip-prefix> } [ route-map <rmap-name> ] +
                        p32 = re.compile(r'^\s*network +(?P<af_network_number>[0-9\.]+)\/(?P<af_network_mask>[0-9]+)( +route-map +(?P<af_network_route_map>[A-Za-z0-9\-\_]+))?$')
                        m = p32.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_network_number'] = \
                                str(m.groupdict()['af_network_number'])
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_network_mask'] = \
                                str(m.groupdict()['af_network_mask'])
                            if m.groupdict()['af_network_route_map']:
                                bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_network_route_map'] = \
                                    str(m.groupdict()['af_network_route_map'])
                            continue

                        #    redistribute isis <Isis.pid> route-map <route_policy>
                        p33 = re.compile(r'^\s*redistribute +isis +(?P<af_redist_isis>[0-9]+) +route-map+(?P<af_redist_isis_route_policy>[A-Za-z0-9\-\_]+)$')
                        m = p32.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_redist_isis'] = \
                                str(m.groupdict()['af_redist_isis'])
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_redist_isis_route_policy'] = \
                                str(m.groupdict()['af_redist_isis_route_policy'])
                            continue

                        #    redistribute isis <Isis.pid> route-map <route_policy>
                        p34 = re.compile(r'^\s*redistribute +isis +(?P<af_redist_isis>[0-9]+) +route-map+(?P<af_redist_isis_route_policy>[A-Za-z0-9\-\_]+)$')
                        m = p34.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_redist_isis'] = \
                                str(m.groupdict()['af_redist_isis'])
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_redist_isis_route_policy'] = \
                                str(m.groupdict()['af_redist_isis_route_policy'])
                            continue

                        #    redistribute ospf <Ospf.pid> route-map <route_policy>
                        p35 = re.compile(r'^\s*redistribute +ospf +(?P<af_redist_ospf>[0-9]+) +route-map+(?P<af_redist_ospf_route_policy>[A-Za-z0-9\-\_]+)$')
                        m = p35.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_redist_ospf'] = \
                                str(m.groupdict()['af_redist_ospf'])
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_redist_ospf_route_policy'] = \
                                str(m.groupdict()['af_redist_ospf_route_policy'])
                            continue

                        #    Redistribute rip <Rip.pid> route-map <route_policy>
                        p36 = re.compile(r'^\s*redistribute +rip +(?P<af_redist_rip>[0-9]+) +route-map +(?P<af_redist_rip_route_policy>[A-Za-z0-9\-\_]+)$')
                        m = p36.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_redist_rip'] = \
                                str(m.groupdict()['af_redist_rip'])
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_redist_rip_route_policy'] = \
                                str(m.groupdict()['af_redist_rip_route_policy'])
                            continue

                        #    redistribute static route-map <route_policy>
                        p37 = re.compile(r'^\s*redistribute +static +route-map +(?P<af_redist_static_route_policy>[A-Za-z0-9\-\_]+)$')
                        m = p37.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_redist_static'] = True
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_redist_static_route_policy'] = \
                                str(m.groupdict()['af_redist_static_route_policy'])
                            continue

                        #    redistribute direct route-map <route_policy>
                        p38 = re.compile(r'^\s*redistribute +direct +route-map +(?P<af_redist_connected_route_policy>[A-Za-z0-9\-\_]+)$')
                        m = p38.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_redist_connected'] = True
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_redist_connected_route_policy'] = \
                                str(m.groupdict()['af_redist_connected_route_policy'])
                            continue

                        #    allocate-label all
                        p39 = re.compile(r'^\s*allocate-label all$')
                        m = p39.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_v6_allocate_label_all'] = True
                            continue

                        #    retain route-target all
                        p40 = re.compile(r'^\s*retain route-target all$')
                        m = p40.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_retain_rt_all'] = True
                            continue

                        #    label-allocation-mode per-vrf
                        p41 = re.compile(r'^\s*label-allocation-mode +(?P<per_vrf>[A-Za-z0-9]+)$')
                        m = p41.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['af_name'][af_name]['af_label_allocation_mode'] = \
                                str(m.groupdict()['per_vrf'])
                            continue

                    #   neighbor <neighbor_id>
                    p42 = re.compile(r'^\s*neighbor +(?P<neighbor_id>[a-z0-9\.\:]+)$')
                    m = p42.match(line)
                    if m:
                        # Get keys
                        neighbor_id = str(m.groupdict()['neighbor_id'])
                        if 'neighbor_id' not in bgp_dict['bgp']['vrf'][vrf]:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'] = {}
                        if neighbor_id not in bgp_dict['bgp']['vrf'][vrf]['neighbor_id']:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id] = {}
                        continue

                    #   Same line of configuration can be configured under the peer session section
                    if neighbor_id:
                        #   bfd
                        p43 = re.compile(r'^\s*bfd$')
                        m = p43.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_fall_over_bfd'] = \
                                True
                            continue
                        elif 'nbr_fall_over_bfd' not in bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_fall_over_bfd'] = \
                                False

                        #   capability suppress 4-byte-as
                        p44 = re.compile(r'^\s*capability suppress 4-byte-as$')
                        m = p44.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_suppress_four_byte_as_capability'] = \
                                True
                            continue
                        elif 'nbr_suppress_four_byte_as_capability' not in bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_suppress_four_byte_as_capability'] = \
                                False

                        #   description <nbr_description>
                        p45 = re.compile(r'^\s*description +(?P<nbr_description>[A-Za-z0-9]+)$')
                        m = p45.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_description'] = \
                                str(m.groupdict()['nbr_description'])
                            continue

                        #   disable-connected-check
                        p46 = re.compile(r'^\s*disable-connected-check$')
                        m = p46.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_disable_connected_check'] = \
                                True
                            continue
                        elif 'nbr_disable_connected_check' not in bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_disable_connected_check'] = \
                                False

                        #   ebgp-multihop <nbr_ebgp_multihop_max_hop>
                        p47 = re.compile(r'^\s*ebgp-multihop +(?P<nbr_ebgp_multihop_max_hop>[0-9]+)$')
                        m = p47.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_ebgp_multihop'] = \
                                True
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_ebgp_multihop_max_hop'] = \
                                int(m.groupdict()['nbr_ebgp_multihop_max_hop'])
                            continue
                        elif 'nbr_ebgp_multihop' not in bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_ebgp_multihop'] = \
                                False

                        #   inherit peer-session <nbr_inherit_peer_session>
                        p48 = re.compile(r'^\s*inherit peer-session +(?P<nbr_inherit_peer_session>[A-Za-z0-9\-]+)$')
                        m = p48.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_inherit_peer_session'] = \
                                str(m.groupdict()['nbr_inherit_peer_session'])
                            continue

                        #    { local-as <nbr_local_as_as_no> [ no-prepend [ replace-as [ dual-as ] ] ] }
                        p49 = re.compile(r'^\s*local-as +(?P<nbr_local_as_as_no>[0-9\.]+)( +(?P<no_prepend>no-prepend)( +(?P<replace_as>replace-as)( +(?P<dual_as>dual-as))?)?)?$')
                        m = p49.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_local_as_as_no'] = \
                                str(m.groupdict()['nbr_local_as_as_no'])
                            if 'nbr_local_as_no_prepend' in m.groupdict():
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_local_as_no_prepend'] = \
                                    True
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_local_as_replace_as'] = \
                                    True
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_local_as_dual_as'] = \
                                    True
                            continue
                        elif 'nbr_local_as_no_prepend' not in bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_local_as_no_prepend'] = \
                                False
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_local_as_replace_as'] = \
                                False
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_local_as_dual_as'] = \
                                False

                        #   { remote-as <nbr_remote_as> }
                        p50 = re.compile(r'^\s*remote-as +(?P<nbr_remote_as>[0-9]+)$')
                        m = p50.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_remote_as'] = \
                                int(m.groupdict()['nbr_remote_as'])
                            continue

                        #   remove-private-as
                        p51 = re.compile(r'^\s*remove-private-as$')
                        m = p51.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_remove_private_as'] = \
                                True
                            continue
                        elif 'nbr_remove_private_as' not in bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_remove_private_as'] = \
                                False

                        #   shutdown
                        p52 = re.compile(r'^\s*shutdown$')
                        m = p52.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_shutdown'] = \
                                True
                            continue
                        elif 'nbr_shutdown' not in bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_shutdown'] = \
                                False

                        #   timers <nbr_keepalive_interval> <nbr_holdtime>
                        p53 = re.compile(r'^\s*timers +(?P<nbr_keepalive_interval>[0-9]+) +(?P<nbr_holdtime>[0-9]+)$')
                        m = p53.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_keepalive_interval'] = \
                                int(m.groupdict()['nbr_keepalive_interval'])
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_holdtime'] = \
                                int(m.groupdict()['nbr_holdtime'])
                            continue

                        #   update-source <nbr_update_source>
                        p54 = re.compile(r'^\s*update-source +(?P<nbr_update_source>[A-Za-z0-9\/\.]+)$')
                        m = p54.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_update_source'] = \
                                str(m.groupdict()['nbr_update_source'])
                            continue

                        #   password <nbr_password_text>
                        p55 = re.compile(r'^\s*password +(?P<nbr_password_text>.*)$')
                        m = p55.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_password_text'] = \
                                str(m.groupdict()['nbr_password_text'])
                            continue

                        #   transport connection-mode <nbr_transport_connection_mode>
                        p56 = re.compile(r'^\s*transport connection-mode +(?P<nbr_transport_connection_mode>[a-z]+)$')
                        m = p56.match(line)
                        if m:
                            bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_transport_connection_mode'] = \
                                str(m.groupdict()['nbr_transport_connection_mode'])
                            continue

                        #   address-family <nbr_af_name>
                        p57 = re.compile(r'^\s*address-family +(?P<nbr_af_name>[A-Za-z0-9\s\-]+)$')
                        m = p57.match(line)
                        if m:
                            nbr_af_name = str(m.groupdict()['nbr_af_name'])
                            if 'nbr_af_name' not in bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]:
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'] = {}
                            if nbr_af_name not in bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name']:
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name] = {}
                            continue

                        if nbr_af_name:
                            #   allowas-in [ <allowas-in-cnt> ]
                            p58 = re.compile(r'^\s*allowas-in( +(?P<nbr_af_allowas_in_as_number>[0-9]+))?$')
                            m = p58.match(line)
                            if m:
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_allowas_in'] = \
                                    True
                                if m.groupdict()['nbr_af_allowas_in_as_number']:
                                    bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_allowas_in_as_number'] = \
                                        int(m.groupdict()['nbr_af_allowas_in_as_number'])
                                continue
                            elif 'nbr_af_allowas_in' not in bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]:
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_allowas_in'] = \
                                    False

                            #   inherit peer-policy <nbr_af_inherit_peer_policy> <nbr_af_inherit_peer_seq>
                            p59 = re.compile(r'^\s*inherit peer-policy +(?P<nbr_af_inherit_peer_policy>[A-Za-z0-9\-]+) +(?P<nbr_af_inherit_peer_seq>[0-9]+)$')
                            m = p59.match(line)
                            if m:
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_inherit_peer_policy'] = \
                                    str(m.groupdict()['nbr_af_inherit_peer_policy'])
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_inherit_peer_seq'] = \
                                    int(m.groupdict()['nbr_af_inherit_peer_seq'])
                                continue

                            #   maximum-prefix <nbr_af_maximum_prefix_max_prefix_no> [ <nbr_af_maximum_prefix_threshold> ] [ restart <nbr_af_maximum_prefix_restart> ]
                            p60 = re.compile(r'^\s*maximum-prefix +(?P<nbr_af_maximum_prefix_max_prefix_no>[0-9]+)( +(?P<nbr_af_maximum_prefix_threshold>[0-9]+))?( +restart +(?P<nbr_af_maximum_prefix_restart>[0-9]+))?$')
                            m = p60.match(line)
                            if m:
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_maximum_prefix_max_prefix_no'] = \
                                    int(m.groupdict()['nbr_af_maximum_prefix_max_prefix_no'])
                                if m.groupdict()['nbr_af_maximum_prefix_threshold']:
                                    bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_maximum_prefix_threshold'] = \
                                        int(m.groupdict()['nbr_af_maximum_prefix_threshold'])
                                if m.groupdict()['nbr_af_maximum_prefix_restart']:
                                    bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_maximum_prefix_restart'] = \
                                        int(m.groupdict()['nbr_af_maximum_prefix_restart'])
                                continue

                            #   maximum-prefix <nbr_af_maximum_prefix_max_prefix_no> [ <nbr_af_maximum_prefix_threshold> ] [ warning-only ]
                            p61 = re.compile(r'^\s*maximum-prefix +(?P<nbr_af_maximum_prefix_max_prefix_no>[0-9]+)( +(?P<nbr_af_maximum_prefix_threshold>[0-9]+))?( +(?P<nbr_af_maximum_prefix_warning_only>warning-only))?$')
                            m = p61.match(line)
                            if m:
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_maximum_prefix_max_prefix_no'] = \
                                    int(m.groupdict()['nbr_af_maximum_prefix_max_prefix_no'])
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_maximum_prefix_threshold'] = \
                                    int(m.groupdict()['nbr_af_maximum_prefix_threshold'])
                                if m.groupdict()['nbr_af_maximum_prefix_warning_only']:
                                    bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_maximum_prefix_warning_only'] = \
                                        True
                                else:
                                    bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_maximum_prefix_warning_only'] = \
                                        False
                                continue

                            #   route-map <nbr_af_route_map_name_in> in
                            p62 = re.compile(r'^\s*route-map +(?P<nbr_af_route_map_name_in>.*) in$')
                            m = p62.match(line)
                            if m:
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_route_map_name_in'] = \
                                    str(m.groupdict()['nbr_af_route_map_name_in'])
                                continue

                            #   route-map <nbr_af_route_map_name_out> out
                            p63 = re.compile(r'^\s*route-map +(?P<nbr_af_route_map_name_out>.*) out$')
                            m = p63.match(line)
                            if m:
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_route_map_name_out'] = \
                                    str(m.groupdict()['nbr_af_route_map_name_out'])
                                continue

                            #   route-reflector-client
                            p64 = re.compile(r'^\s*route-reflector-client$')
                            m = p64.match(line)
                            if m:
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_route_reflector_client'] = \
                                    True
                                continue
                            elif 'nbr_af_route_reflector_client' not in bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]:
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_route_reflector_client'] = \
                                    False

                            #   send-community
                            p65 = re.compile(r'^\s*send-community$')
                            m = p65.match(line)
                            if m:
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_send_community'] = \
                                    'standard'
                                send_community_standard_match = 'True'
                                continue

                            #   send-community extended
                            p66 = re.compile(r'^\s*send-community +extended$')
                            m = p66.match(line)
                            if m:
                                if send_community_standard_match:
                                    bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_send_community'] = \
                                        'both'
                                else:
                                    bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_send_community'] = \
                                        'extended'
                                continue

                            #   route-reflector-client
                            p67 = re.compile(r'^\s*soft-reconfiguration inbound( +(?P<nbr_af_soft_reconfiguration_extra>.*))?$')
                            m = p67.match(line)
                            if m:
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_soft_reconfiguration'] = \
                                    True
                                continue
                            elif 'nbr_af_soft_reconfiguration' not in bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]:
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_soft_reconfiguration'] = \
                                    False

                            #   next-hop-self
                            p68 = re.compile(r'^\s*next-hop-self$')
                            m = p68.match(line)
                            if m:
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_next_hop_self'] = \
                                    True
                                continue
                            elif 'nbr_af_next_hop_self' not in bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]:
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_next_hop_self'] = \
                                    False

                            #   as-override
                            p69 = re.compile(r'^\s*as-override$')
                            m = p69.match(line)
                            if m:
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_as_override'] = \
                                    True
                                continue
                            elif 'nbr_af_as_override' not in bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]:
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_as_override'] = \
                                    False

                            #   default-originate [ route-map <nbr_af_default_originate_route_map> ]
                            p70 = re.compile(r'^\s*default-originate( +route-map +(?P<nbr_af_default_originate_route_map>.*))?$')
                            m = p70.match(line)
                            if m:
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_default_originate'] = \
                                    True
                                if m.groupdict()['nbr_af_default_originate_route_map']:
                                    bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_default_originate_route_map'] = \
                                        str(m.groupdict()['nbr_af_default_originate_route_map'])
                                continue
                            elif 'nbr_af_default_originate' not in bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]:
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_default_originate'] = \
                                    False

                            #   soo <nbr_af_soo>
                            p71 = re.compile(r'^\s*soo +(?P<nbr_af_soo>.*)$')
                            m = p71.match(line)
                            if m:
                                bgp_dict['bgp']['vrf'][vrf]['neighbor_id'][neighbor_id]['nbr_af_name'][nbr_af_name]['nbr_af_soo'] = \
                                    str(m.groupdict()['nbr_af_soo'])
                                continue

                #   template peer-session PEER-SESSION
                p72 = re.compile(r'^\s*template peer-session +(?P<ps_name>.*)$')
                m = p72.match(line)
                if m:
                    # Get keys
                    ps_name = str(m.groupdict()['ps_name'])
                    if 'ps_name' not in bgp_dict['bgp']:
                        bgp_dict['bgp']['ps_name'] = {}
                    if ps_name not in bgp_dict['bgp']['ps_name']:
                        bgp_dict['bgp']['ps_name'][ps_name] = {}
                    continue

                if ps_name:
                    #   bfd
                    p73 = re.compile(r'^\s*bfd$')
                    m = p73.match(line)
                    if m:
                        # Get keys
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_fall_over_bfd'] = True
                        continue
                    elif 'ps_fall_over_bfd' not in bgp_dict['bgp']['ps_name'][ps_name]:
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_fall_over_bfd'] = False

                    #   capability suppress 4-byte-as
                    p74 = re.compile(r'^\s*bfd$')
                    m = p74.match(line)
                    if m:
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_suppress_four_byte_as_capability'] = True
                        continue
                    elif 'ps_suppress_four_byte_as_capability' not in bgp_dict['bgp']['ps_name'][ps_name]:
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_suppress_four_byte_as_capability'] = False

                    #   description <ps_description>
                    p75 = re.compile(r'^\s*description +(?P<ps_description>.*)$')
                    m = p75.match(line)
                    if m:
                        # Get keys
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_description'] = \
                            str(m.groupdict()['ps_description'])
                        continue

                    #   disable-connected-check
                    p76 = re.compile(r'^\s*disable-connected-check$')
                    m = p76.match(line)
                    if m:
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_disable_connected_check'] = True
                        continue
                    elif 'ps_disable_connected_check' not in bgp_dict['bgp']['ps_name'][ps_name]:
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_disable_connected_check'] = False

                    #   ebgp-multihop <ps_ebgp_multihop_max_hop>
                    p77 = re.compile(r'^\s*ebgp-multihop +(?P<ps_ebgp_multihop_max_hop>[0-9]+)$$')
                    m = p77.match(line)
                    if m:
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_ebgp_multihop'] = True
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_ebgp_multihop_max_hop'] = \
                            int(m.groupdict()['ps_ebgp_multihop_max_hop'])
                        continue
                    elif 'ps_ebgp_multihop' not in bgp_dict['bgp']['ps_name'][ps_name]:
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_ebgp_multihop'] = False

                    #    { local-as <ps_local_as_as_no> [ no-prepend [ replace-as [ dual-as ] ] ] }
                    p78 = re.compile(r'^\s*local-as +(?P<ps_local_as_as_no>[0-9\.]+)( +no-prepend( +replace-as( +dual-as)?)?)?$')
                    m = p78.match(line)
                    if m:
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_local_as_as_no'] = \
                            str(m.groupdict()['ps_local_as_as_no'])
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_local_as_no_prepend'] = \
                            True
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_local_as_replace_as'] = \
                            True
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_local_as_dual_as'] = \
                            True
                        continue
                    elif 'ps_local_as_no_prepend' not in bgp_dict['bgp']['ps_name'][ps_name]:
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_local_as_no_prepend'] = \
                            False
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_local_as_replace_as'] = \
                            False
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_local_as_dual_as'] = \
                            False

                    #   password <ps_password_text>
                    p79 = re.compile(r'^\s*password +(?P<ps_password_text>.*)$')
                    m = p79.match(line)
                    if m:
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_password_text'] = \
                            str(m.groupdict()['ps_password_text'])
                        continue

                    #   { remote-as <ps_remote_as> }
                    p80 = re.compile(r'^\s*remote-as +(?P<ps_remote_as>[0-9]+)$')
                    m = p80.match(line)
                    if m:
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_remote_as'] = \
                            int(m.groupdict()['ps_remote_as'])
                        continue

                    #   shutdown
                    p81 = re.compile(r'^\s*shutdown$')
                    m = p81.match(line)
                    if m:
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_shutdown'] = \
                            True
                        continue
                    elif 'ps_shutdown' not in bgp_dict['bgp']['ps_name'][ps_name]:
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_shutdown'] = \
                            False

                    #   timers <ps_keepalive_interval> <ps_hodltime>
                    p82 = re.compile(r'^\s*timers +(?P<ps_keepalive_interval>[0-9]+) +(?P<ps_hodltime>[0-9]+)$')
                    m = p82.match(line)
                    if m:
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_keepalive_interval'] = \
                            int(m.groupdict()['ps_keepalive_interval'])
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_hodltime'] = \
                            int(m.groupdict()['ps_hodltime'])
                        continue

                    #   transport connection-mode <ps_transport_connection_mode>
                    p83 = re.compile(r'^\s*transport connection-mode +(?P<ps_transport_connection_mode>[a-z]+)$')
                    m = p83.match(line)
                    if m:
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_transport_connection_mode'] = \
                            str(m.groupdict()['ps_transport_connection_mode'])
                        continue

                    #   update-source <ps_update_source>
                    p84 = re.compile(r'^\s*update-source +(?P<ps_update_source>[A-Za-z0-9\/\.]+)$')
                    m = p54.match(line)
                    if m:
                        bgp_dict['bgp']['ps_name'][ps_name]['ps_update_source'] = \
                            str(m.groupdict()['ps_update_source'])
                        continue

                #   template peer-policy <pp_name>
                p85 = re.compile(r'^\s*template peer-session +(?P<pp_name>.*)$')
                m = p85.match(line)
                if m:
                    # Get keys
                    pp_name = str(m.groupdict()['pp_name'])
                    if 'pp_name' not in bgp_dict['bgp']:
                        bgp_dict['bgp']['pp_name'] = {}
                    if pp_name not in bgp_dict['bgp']['pp_name']:
                        bgp_dict['bgp']['pp_name'][pp_name] = {}
                    continue

                if pp_name:
                    #   allowas-in [ <allowas-in-cnt> ]
                    p86 = re.compile(r'^\s*allowas-in( +(?P<pp_allowas_in_as_number>[0-9]+))?$')
                    m = p86.match(line)
                    if m:
                        bgp_dict['bgp']['pp_name'][pp_name]['pp_allowas_in'] = \
                            True
                        if m.groupdict()['pp_allowas_in_as_number']:
                            bgp_dict['bgp']['pp_name'][pp_name]['pp_allowas_in_as_number'] = \
                                int(m.groupdict()['pp_allowas_in_as_number'])
                        continue
                    elif 'pp_allowas_in' not in bgp_dict['bgp']['pp_name'][pp_name]:
                        bgp_dict['bgp']['pp_name'][pp_name]['pp_allowas_in'] = \
                            False

                    #   as-override
                    p87 = re.compile(r'^\s*as-override$')
                    m = p87.match(line)
                    if m:
                        bgp_dict['bgp']['pp_name'][pp_name]['pp_as_override'] = \
                            True
                        continue
                    elif 'pp_as_override' not in bgp_dict['bgp']['pp_name'][pp_name]:
                        bgp_dict['bgp']['pp_name'][pp_name]['pp_as_override'] = \
                            False

                    #   default-originate [ route-map <pp_default_originate_route_map> ]
                    p88 = re.compile(r'^\s*default-originate( +route-map +(?P<pp_default_originate_route_map>.*))?$')
                    m = p88.match(line)
                    if m:
                        bgp_dict['bgp']['pp_name'][pp_name]['pp_default_originate'] = \
                            True
                        if m.groupdict()['pp_default_originate_route_map']:
                            bgp_dict['bgp']['pp_name'][pp_name]['pp_default_originate_route_map'] = \
                                str(m.groupdict()['pp_default_originate_route_map'])
                        continue
                    elif 'pp_default_originate' not in bgp_dict['bgp']['pp_name'][pp_name]:
                        bgp_dict['bgp']['pp_name'][pp_name]['pp_default_originate'] = \
                            False

                    #   route-map <pp_route_map_name_in> in
                    p89 = re.compile(r'^\s*route-map +(?P<pp_route_map_name_in>.*) in$')
                    m = p89.match(line)
                    if m:
                        bgp_dict['bgp']['pp_name'][pp_name]['pp_route_map_name_in'] = \
                            str(m.groupdict()['pp_route_map_name_in'])
                        continue

                    #   route-map <nbr_af_route_map_name_out> out
                    p90 = re.compile(r'^\s*route-map +(?P<pp_route_map_name_out>.*) out$')
                    m = p90.match(line)
                    if m:
                        bgp_dict['bgp']['pp_name'][pp_name]['pp_route_map_name_out'] = \
                            str(m.groupdict()['pp_route_map_name_out'])
                        continue

                    #    maximum-prefix <pp_maximum_prefix_max_prefix_no> [ <pp_maximum_prefix_threshold> ] [ restart <pp_maximum_prefix_restart> ]
                    p91 = re.compile(r'^\s*maximum-prefix +(?P<pp_maximum_prefix_max_prefix_no>[0-9]+)( +(?P<nbr_af_maximum_prefix_threshold>[0-9]+))?(restart +(?P<nbr_af_maximum_prefix_restart>[0-9]+))?$')
                    m = p91.match(line)
                    if m:
                        bgp_dict['bgp']['pp_name'][pp_name]['pp_maximum_prefix_max_prefix_no'] = \
                            int(m.groupdict()['pp_maximum_prefix_max_prefix_no'])
                        bgp_dict['bgp']['pp_name'][pp_name]['pp_maximum_prefix_threshold'] = \
                            int(m.groupdict()['pp_maximum_prefix_threshold'])
                        bgp_dict['bgp']['pp_name'][pp_name]['pp_maximum_prefix_restart'] = \
                            int(m.groupdict()['pp_maximum_prefix_restart'])
                        continue

                    #   maximum-prefix <pp_maximum_prefix_max_prefix_no> [ <pp_maximum_prefix_threshold> ] [ warning-only ]
                    p92 = re.compile(r'^\s*maximum-prefix +(?P<pp_maximum_prefix_max_prefix_no>[0-9]+)( +(?P<pp_maximum_prefix_threshold>[0-9]+))?( +(?P<pp_maximum_prefix_warning_only>warning-only))?$')
                    m = p92.match(line)
                    if m:
                        bgp_dict['bgp']['pp_name'][pp_name]['pp_maximum_prefix_max_prefix_no'] = \
                            int(m.groupdict()['pp_maximum_prefix_max_prefix_no'])
                        bgp_dict['bgp']['pp_name'][pp_name]['pp_maximum_prefix_threshold'] = \
                            int(m.groupdict()['pp_maximum_prefix_threshold'])
                        if m.groupdict()['pp_maximum_prefix_warning_only']:
                            bgp_dict['bgp']['pp_name'][pp_name]['pp_maximum_prefix_warning_only'] = \
                                True
                        else:
                            bgp_dict['bgp']['pp_name'][pp_name]['pp_maximum_prefix_warning_only'] = \
                                False
                        continue

                    #   next-hop-self
                    p93 = re.compile(r'^\s*next-hop-self$')
                    m = p93.match(line)
                    if m:
                        bgp_dict['bgp']['pp_name'][pp_name]['pp_next_hop_self'] = \
                            True
                        continue
                    elif 'pp_next_hop_self' not in bgp_dict['bgp']['pp_name'][pp_name]:
                        bgp_dict['bgp']['pp_name'][pp_name]['pp_next_hop_self'] = \
                            False

                    #   route-reflector-client
                    p94 = re.compile(r'^\s*route-reflector-client$')
                    m = p94.match(line)
                    if m:
                        bgp_dict['bgp']['pp_name'][pp_name]['pp_route_reflector_client'] = \
                            True
                        continue
                    elif 'pp_route_reflector_client' not in bgp_dict['bgp']['pp_name'][pp_name]:
                        bgp_dict['bgp']['pp_name'][pp_name]['pp_route_reflector_client'] = \
                            False

                    #   send-community
                    p95 = re.compile(r'^\s*send-community$')
                    m = p95.match(line)
                    if m:
                        bgp_dict['bgp']['pp_name'][pp_name]['pp_send_community'] = \
                            'standard'
                        peer_policy_send_community_standard_match = 'True'
                        continue

                    #   send-community extended
                    p96 = re.compile(r'^\s*send-community +extended$')
                    m = p96.match(line)
                    if m:
                        if peer_policy_send_community_standard_match:
                            bgp_dict['bgp']['pp_name'][pp_name]['pp_send_community'] = \
                                'both'
                        else:
                            bgp_dict['bgp']['pp_name'][pp_name]['pp_send_community'] = \
                                'extended'
                        continue

                    #   route-reflector-client
                    p97 = re.compile(r'^\s*soft-reconfiguration inbound( +(?P<nbr_af_soft_reconfiguration_extra>.*))?$')
                    m = p97.match(line)
                    if m:
                        bgp_dict['bgp']['pp_name'][pp_name]['pp_soft_reconfiguration'] = \
                            True
                        continue
                    elif 'pp_soft_reconfiguration' not in bgp_dict['bgp']['pp_name'][pp_name]:
                        bgp_dict['bgp']['pp_name'][pp_name]['pp_soft_reconfiguration'] = \
                            False

                    #   soo <pp_soo>
                    p98 = re.compile(r'^\s*soo +(?P<pp_soo>.*)$')
                    m = p98.match(line)
                    if m:
                        bgp_dict['bgp']['pp_name'][pp_name]['pp_soo'] = \
                            str(m.groupdict()['pp_soo'])
                        continue

        return bgp_dict

# vim: ft=python et sw=4
