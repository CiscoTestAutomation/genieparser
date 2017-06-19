''' show_bgp.py

NXOS parsers for the following show commands:
    * 'show bgp process vrf all'
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
        'bgp_tag': str,
        'bgp_protocol_state': str,
        'bgp_memory_state': str,
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
                    },
                },
            },
        },
    }

class ShowBgpProcessVrfAll(ShowBgpProcessVrfAllSchema):

    '''Parser for show bgp process vrf all'''

    def cli(self):
        cmd = 'show bgp process vrf all'
        out = self.device.execute(cmd)
        
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

            # BGP Memory State               : OK
            p5 = re.compile(r'^\s*BGP +Memory +State *:'
                             ' +(?P<memory_state>[a-zA-Z]+)$')
            m = p5.match(line)
            if m:
                parsed_dict['bgp_memory_state'] = \
                    str(m.groupdict()['memory_state']).lower()
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
                parsed_dict['vrf'][vrf_name]['address_family'][address_family]\
                    ['table_id'] = m.groupdict()['table_id']
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

        return parsed_dict


# =========================================
# Parser for 'show bgp peer-session <WORD>'
# =========================================

class ShowBgpPeerSessionSchema(MetaParser):
    
    '''Schema for show bgp peer-session <WORD>'''

    schema = {
        'peer_session': 
            {Any(): 
                {'shutdown': bool,
                 'update_source': str,
                 'description': str,
                 'password': bool,
                 'ebgp_multihop_enable': bool,
                 'ebgp_multihop_limit': int,
                 'disable_connectivity_check': bool,
                 'suppress_capabilities': bool,
                 'transport_connection_mode': str,
                 'holdtime': int,
                 'keepalive': int,
                 'remote_as': bool,
                 'local_as': bool,
                 'bfd': bool,
                 'inherited_vrf_default': str,
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
                                {'next_hop': 
                                    {Any(): 
                                        {Optional('status_codes'): str,
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

                # Check if the prefix exists
                if prefix not in af_dict[address_family]['prefixes']:
                    af_dict[address_family]['prefixes'][prefix] = {}
                
                # Check if next_hop top level key exists
                if 'next_hop' not in af_dict[address_family]['prefixes']\
                    [prefix]:
                    af_dict[address_family]['prefixes'][prefix]\
                        ['next_hop'] = {}

                # Check if current prefix details are on next line
                if next_hop == 'None':
                    data_on_nextline = True
                    continue

                # Check if next_hop exists
                if next_hop not in af_dict[address_family]['prefixes']\
                    [prefix]['next_hop']:
                    af_dict[address_family]['prefixes'][prefix]\
                        ['next_hop'][next_hop] = {}
                    nh_dict = af_dict[address_family]['prefixes']\
                        [prefix]['next_hop'][next_hop]
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

                # Check if next_hop exists
                if next_hop not in af_dict[address_family]['prefixes']\
                    [prefix]['next_hop']:
                    af_dict[address_family]['prefixes'][prefix]\
                        ['next_hop'][next_hop] = {}
                    nh_dict = af_dict[address_family]['prefixes']\
                        [prefix]['next_hop'][next_hop]
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
                                        {Optional('next_hop'):
                                            {Optional(Any()):
                                                {Optional('status_codes'): str,
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
                
                # Check if next_hop top level key exists
                if 'next_hop' not in af_dict['advertised'][prefix]:
                    af_dict['advertised'][prefix]['next_hop'] = {}

                # Check if current prefix details are on next line
                if next_hop == 'None':
                    data_on_nextline = True
                    continue

                # Check if next_hop exists
                if next_hop not in af_dict['advertised'][prefix]['next_hop']:
                    af_dict['advertised'][prefix]['next_hop'][next_hop] = {}
                    nh_dict = af_dict['advertised'][prefix]['next_hop'][next_hop]
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

                # Check if next_hop exists
                if next_hop not in af_dict['advertised'][prefix]['next_hop']:
                    af_dict['advertised'][prefix]['next_hop'][next_hop] = {}
                    nh_dict = af_dict['advertised'][prefix]['next_hop'][next_hop]
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
                                        {Optional('next_hop'):
                                            {Optional(Any()):
                                                {Optional('status_codes'): str,
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
    
    '''Parser for show bgp vrf all all neighbors 21.0.0.2 routes'''

    def cli(self, vrf, neighbor):
        cmd  = 'show bgp vrf {vrf} all neighbors {neighbor} routes'.format(vrf=vrf, neighbor=neighbor)
        out = self.device.execute(cmd)

        # Init vars
        route_dict = {}
        data_on_nextline =  False

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
                
                # Check if next_hop top level key exists
                if 'next_hop' not in af_dict['routes'][prefix]:
                    af_dict['routes'][prefix]['next_hop'] = {}

                # Check if current prefix details are on next line
                if next_hop == 'None':
                    data_on_nextline = True
                    continue

                # Check if next_hop exists
                if next_hop not in af_dict['routes'][prefix]['next_hop']:
                    af_dict['routes'][prefix]['next_hop'][next_hop] = {}
                    nh_dict = af_dict['routes'][prefix]['next_hop'][next_hop]
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

                # Check if next_hop exists
                if next_hop not in af_dict['routes'][prefix]['next_hop']:
                    af_dict['routes'][prefix]['next_hop'][next_hop] = {}
                    nh_dict = af_dict['routes'][prefix]['next_hop'][next_hop]
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
                                        {Optional('next_hop'):
                                            {Optional(Any()):
                                                {Optional('status_codes'): str,
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
                
                # Check if next_hop top level key exists
                if 'next_hop' not in af_dict['received_routes'][prefix]:
                    af_dict['received_routes'][prefix]['next_hop'] = {}

                # Check if current prefix details are on next line
                if next_hop == 'None':
                    data_on_nextline = True
                    continue

                # Check if next_hop exists
                if next_hop not in af_dict['received_routes'][prefix]['next_hop']:
                    af_dict['received_routes'][prefix]['next_hop'][next_hop] = {}
                    nh_dict = af_dict['received_routes'][prefix]['next_hop'][next_hop]
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

                # Check if next_hop exists
                if next_hop not in af_dict['received_routes'][prefix]['next_hop']:
                    af_dict['received_routes'][prefix]['next_hop'][next_hop] = {}
                    nh_dict = af_dict['received_routes'][prefix]['next_hop'][next_hop]
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

# vim: ft=python et sw=4
