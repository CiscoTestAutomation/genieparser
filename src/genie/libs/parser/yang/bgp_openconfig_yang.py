''' bgp_openconfig_yang.py

Parser for:
    * BGP Openconfig YANG Model 'GET' Operation Parser
'''

# Python
import re
import xml.etree.ElementTree as ET

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use


# =========================================
# Parser for BGP Openconfig YANG 'GET' OPER
# =========================================

class BgpOpenconfigYangSchema(MetaParser):
    schema = {
        'bgp_pid': int,
        Optional('total_paths'): int,
        Optional('total_prefixes'): int,
        Optional('use_multiple_paths'): 
            {'ebgp_max_paths': int,
             'ibgp_max_paths': int,
            },
        'vrf': 
            {Any(): 
                {'router_id': str,
                 Optional('graceful_restart'): bool,
                 Optional('graceful_restart_helper_only'): bool,
                 Optional('graceful_restart_restart_time'): int,
                 Optional('graceful_restart_stalepath_time'): int,
                 Optional('log_neighbor_changes'): bool,
                 Optional('neighbor'): 
                    {Any(): 
                        {Optional('description'): str,
                         Optional('remote_as'): int,
                         Optional('remove_private_as'): bool,
                         Optional('peer_group'): str,
                         Optional('send_community'): str,
                         Optional('input_queue'): int,
                         Optional('output_queue'): int,
                         Optional('session_state'): str,
                         Optional('bgp_neighbor_counters'): 
                            {'messages': 
                                {Optional('sent'): 
                                    {Optional('updates'): int,
                                     Optional('notifications'): int,
                                    },
                                 Optional('received'): 
                                    {Optional('updates'): int,
                                     Optional('notifications'): int,
                                    },
                                },
                            },
                         Optional('nbr_ebgp_multihop'): bool,
                         Optional('nbr_ebgp_multihop_max_hop'): int,
                         Optional('graceful_restart'): bool,
                         Optional('graceful_restart_helper_only'): bool,
                         Optional('graceful_restart_restart_time'): int,
                         Optional('graceful_restart_stalepath_time'): int,
                         Optional('allow_own_as'): int,
                         Optional('holdtime'): int,
                         Optional('keepalive_interval'): int,
                         Optional('minimum_advertisement_interval'): int,
                         Optional('route_reflector_client'): bool,
                         Optional('route_reflector_cluster_id'): int,
                         Optional('bgp_session_transport'):
                            {'transport': 
                                {Optional('local_port'): str,
                                 Optional('local_host'): str,
                                 Optional('foreign_port'): str,
                                 Optional('foreign_host'): str,
                                 Optional('passive_mode'): str,
                                },
                            },
                         Optional('address_family'): 
                            {Any(): 
                                {Optional('enabled'): bool,
                                 Optional('graceful_restart'): bool,
                                 Optional('ipv4_unicast_send_default_route'): bool,
                                 Optional('ipv6_unicast_send_default_route'): bool,
                                 Optional('prefixes_received'): int,
                                 Optional('prefixes_sent'): int,
                                 Optional('active'): bool,
                                },
                            },
                        },
                    },
                 Optional('address_family'): 
                    {Any(): 
                        {'enabled': bool,
                         Optional('graceful_restart'): bool,
                         Optional('advertise_inactive_routes'): bool,
                         Optional('ebgp_max_paths'): int,
                         Optional('ibgp_max_paths'): int,
                         Optional('total_paths'): int,
                         Optional('total_prefixes'): int,
                        },
                    },
                },
            },
        }

class BgpOpenconfigYang(BgpOpenconfigYangSchema):

    def yang(self, **kwargs):
        
        parsed_dict = {}
        cmd = '''
            <bgp xmlns="http://openconfig.net/yang/bgp">
            </bgp>
        '''

        # Execute RPC and get response
        reply = self.device.get(('subtree', cmd))

        # Get ETree rpc-reply
        output = reply.data_ele
        
        # Get string rpc-reply
        #string_output = reply.data_xml

        for bgp in output:
            for top_level_key in bgp:
                top_level_key_name = top_level_key.tag[top_level_key.tag.find('}')+1:]
                
                # global
                if top_level_key_name == 'global':
                    for global_key in top_level_key:
                        global_key_name = global_key.tag[global_key.tag.find('}')+1:]
                    
                        # 'state'
                        if global_key_name == 'state':
                            for state_key in global_key:
                                state_key_name = state_key.tag[state_key.tag.find('}')+1:]
                                # as
                                if state_key_name == 'as':
                                    parsed_dict['bgp_pid'] = int(state_key.text)
                                # router-id
                                if state_key_name == 'router-id':
                                    if 'vrf' not in parsed_dict:
                                        parsed_dict['vrf'] = {}
                                    if 'default' not in parsed_dict['vrf']:
                                        parsed_dict['vrf']['default'] = {}
                                    parsed_dict['vrf']['default']['router_id'] = state_key.text
                                # total-paths
                                if state_key_name == 'total-paths':
                                    parsed_dict['total_paths'] = int(state_key.text)
                                # total-prefixes
                                if state_key_name == 'total-prefixes':
                                    parsed_dict['total_prefixes'] = int(state_key.text)
                        
                        # 'graceful-restart'
                        if global_key_name == 'graceful-restart':
                            for gr_key in global_key:
                                gr_key_name = gr_key.tag[gr_key.tag.find('}')+1:]
                                if gr_key_name == 'state':
                                    if 'vrf' not in parsed_dict:
                                        parsed_dict['vrf'] = {}
                                    if 'default' not in parsed_dict['vrf']:
                                        parsed_dict['vrf']['default'] = {}
                                    for gr_state_key in gr_key:
                                        gr_state_key_name = gr_state_key.tag[gr_state_key.tag.find('}')+1:]
                                        # enabled
                                        if gr_state_key_name == 'enabled':
                                            if gr_state_key.text == 'false':
                                                parsed_dict['vrf']['default']['graceful_restart'] = False
                                            elif gr_state_key.text == 'true':
                                                parsed_dict['vrf']['default']['graceful_restart'] = True
                                        # helper-only
                                        if gr_state_key_name == 'helper-only':
                                            if gr_state_key.text == 'false':
                                                parsed_dict['vrf']['default']['graceful_restart_helper_only'] = False
                                            elif gr_state_key.text == 'true':
                                                parsed_dict['vrf']['default']['graceful_restart_helper_only'] = True
                                        # restart-time
                                        if gr_state_key_name == 'restart-time':
                                            parsed_dict['vrf']['default']['graceful_restart_restart_time'] = int(gr_state_key.text)
                                        # stale-routes-time
                                        if gr_state_key_name == 'stale-routes-time':
                                            parsed_dict['vrf']['default']['graceful_restart_stalepath_time'] = int(gr_state_key.text)

                        # 'use-multiple-paths'
                        if global_key_name == 'use-multiple-paths':
                            for multiple_path_key in global_key:
                                multiple_path_key_name = multiple_path_key.tag[multiple_path_key.tag.find('}')+1:]
                                if 'use_multiple_paths' not in parsed_dict:
                                    parsed_dict['use_multiple_paths'] = {}
                                if multiple_path_key_name == 'ebgp':
                                    for ebgp_key in multiple_path_key:
                                        ebgp_key_name = ebgp_key.tag[ebgp_key.tag.find('}')+1:]
                                        if ebgp_key_name == 'state':
                                            for ebgp_state_key in ebgp_key:
                                                ebgp_state_key_name = ebgp_state_key.tag[ebgp_state_key.tag.find('}')+1:]
                                                if ebgp_state_key_name == 'maximum-paths':
                                                    parsed_dict['use_multiple_paths']['ebgp_max_paths'] = int(ebgp_state_key.text)
                                if multiple_path_key_name == 'ibgp':
                                    for ibgp_key in multiple_path_key:
                                        ibgp_key_name = ibgp_key.tag[ibgp_key.tag.find('}')+1:]
                                        if ibgp_key_name == 'state':
                                            for ibgp_state_key in ibgp_key:
                                                ibgp_state_key_name = ibgp_state_key.tag[ibgp_state_key.tag.find('}')+1:]
                                                if ibgp_state_key_name == 'maximum-paths':
                                                    parsed_dict['use_multiple_paths']['ibgp_max_paths'] = int(ibgp_state_key.text)

                        # 'afi-safis'
                        if global_key_name == 'afi-safis':
                            if 'vrf' not in parsed_dict:
                                parsed_dict['vrf'] = {}
                            if 'default' not in  parsed_dict['vrf']:
                                parsed_dict['vrf']['default'] = {}
                            if 'address_family' not in parsed_dict['vrf']['default']:
                                parsed_dict['vrf']['default']['address_family'] = {}
                            for safis_key in global_key:
                                safis_key_name = safis_key.tag[safis_key.tag.find('}')+1:]
                                if safis_key_name == 'afi-safi':
                                    for safi_key in safis_key:
                                        safi_key_name = safi_key.tag[safi_key.tag.find('}')+1:]
                                        
                                        # afi-safi-name
                                        if safi_key_name == 'afi-safi-name':
                                            address_family = str(safi_key.text).lower()
                                            address_family = address_family.replace("_", " ")
                                            address_family = address_family.replace("labeled", "label")
                                            if address_family not in parsed_dict['vrf']['default']['address_family'] and\
                                               address_family != 'none':
                                                parsed_dict['vrf']['default']['address_family'][address_family] = {}
                                        
                                        # state
                                        if safi_key_name == 'state' and address_family != 'none':
                                            for state_key in safi_key:
                                                state_key_name = state_key.tag[state_key.tag.find('}')+1:]
                                                # enabled
                                                if state_key_name == 'enabled':
                                                    if state_key.text == 'true':
                                                        parsed_dict['vrf']['default']['address_family'][address_family]['enabled'] = True
                                                    else:
                                                        parsed_dict['vrf']['default']['address_family'][address_family]['enabled'] = False
                                                # total-paths
                                                if state_key_name == 'total-paths':
                                                    parsed_dict['vrf']['default']['address_family'][address_family]['total_paths'] = int(state_key.text)
                                                # total-prefixes
                                                if state_key_name == 'total-prefixes':
                                                    parsed_dict['vrf']['default']['address_family'][address_family]['total_prefixes'] = int(state_key.text)
                                        
                                        # graceful_restart
                                        if safi_key_name == 'graceful-restart' and address_family != 'none':
                                            for gr_key in safi_key:
                                                gr_key_name = gr_key.tag[gr_key.tag.find('}')+1:]
                                                if gr_key_name == 'state':
                                                    for gr_state_key in gr_key:
                                                        gr_state_key_name = gr_state_key.tag[gr_state_key.tag.find('}')+1:]
                                                        if gr_state_key_name == 'enabled':
                                                            if gr_state_key.text == 'true':
                                                                parsed_dict['vrf']['default']['address_family'][address_family]['graceful_restart'] = True
                                                            else:
                                                                parsed_dict['vrf']['default']['address_family'][address_family]['graceful_restart'] = False

                                        # route-selection-options
                                        if safi_key_name == 'route-selection-options' and address_family != 'none':
                                            for rso_key in safi_key:
                                                rso_key_name = rso_key.tag[rso_key.tag.find('}')+1:]
                                                if rso_key_name == 'state':
                                                    for rso_key_state_key in rso_key:
                                                        rso_state_key_name = rso_key_state_key.tag[rso_key_state_key.tag.find('}')+1:]
                                                        if rso_state_key_name == 'advertise-inactive-routes':
                                                            if rso_key_state_key.text == 'true':
                                                                parsed_dict['vrf']['default']['address_family'][address_family]['advertise_inactive_routes'] = True
                                                            else:
                                                                parsed_dict['vrf']['default']['address_family'][address_family]['advertise_inactive_routes'] = False

                                        # use-multiple-paths
                                        if safi_key_name == 'use-multiple-paths' and address_family != 'none':
                                            for ump_key in safi_key:
                                                ump_key_name = ump_key.tag[ump_key.tag.find('}')+1:]
                                                if ump_key_name == 'ebgp':
                                                    for ebgp_key in ump_key:
                                                        ebgp_key_name = ebgp_key.tag[ebgp_key.tag.find('}')+1:]
                                                        if ebgp_key_name == 'state':
                                                            for ebgp_state_key in ebgp_key:
                                                                ebgp_state_key_name = ebgp_state_key.tag[ebgp_state_key.tag.find('}')+1:]
                                                                if ebgp_state_key_name == 'maximum-paths':
                                                                    parsed_dict['vrf']['default']['address_family'][address_family]['ebgp_max_paths'] = int(ebgp_state_key.text)
                                                if ump_key_name == 'ibgp':
                                                    for ibgp_key in ump_key:
                                                        ibgp_key_name = ibgp_key.tag[ibgp_key.tag.find('}')+1:]
                                                        if ibgp_key_name == 'state':
                                                            for ibgp_state_key in ibgp_key:
                                                                ibgp_state_key_name = ibgp_state_key.tag[ibgp_state_key.tag.find('}')+1:]
                                                                if ibgp_state_key_name == 'maximum-paths':
                                                                    parsed_dict['vrf']['default']['address_family'][address_family]['ibgp_max_paths'] = int(ibgp_state_key.text)

                # neighbors
                if top_level_key_name == 'neighbors':
                    for neighbor in top_level_key:
                        neighbor_name  = neighbor.tag[neighbor.tag.find('}')+1:]
                        if neighbor_name == 'neighbor':
                            # Initialize values for this neighbor
                            neighbor_name = None
                            nbr_state_dict = {}
                            nbr_transport_dict = {}
                            nbr_timers_dict = {}
                            nbr_gr_dict = {}
                            nbr_ebgp_dict = {}
                            nbr_as_path_dict = {}
                            nbr_rr_dict = {}
                            nbr_safis_dict = {}
                            for neighbor_key in neighbor:
                                # Get key name
                                neighbor_key_name = neighbor_key.tag[neighbor_key.tag.find('}')+1:]
                                
                                # Tag: neighbor-address
                                if neighbor_key_name == 'neighbor-address':
                                    neighbor_name = neighbor_key.text
                                    # Create neighbor key
                                    if 'neighbor' not in parsed_dict['vrf']['default']:
                                        parsed_dict['vrf']['default']['neighbor'] = {}
                                    if neighbor_name not in parsed_dict['vrf']['default']['neighbor']:
                                        parsed_dict['vrf']['default']['neighbor'][neighbor_name] = {}

                                # Tag: state
                                if neighbor_key_name == 'state':
                                    for state_key in neighbor_key:
                                        state_key_name = state_key.tag[state_key.tag.find('}')+1:]
                                        # description
                                        if state_key_name == 'description':
                                            nbr_state_dict['description'] = str(state_key.text)
                                        # peer-as
                                        if state_key_name == 'peer-as':
                                            if state_key.text is not None and state_key.text != 'none':
                                                nbr_state_dict['remote_as'] = int(state_key.text)
                                        # peer-group
                                        if state_key_name == 'peer-group':
                                            nbr_state_dict['peer_group'] = str(state_key.text)
                                        # remove-private-as
                                        if state_key_name == 'remove-private-as':
                                            if state_key.text == 'true':
                                                nbr_state_dict['remove_private_as'] = True
                                            else:
                                                nbr_state_dict['remove_private_as'] = False
                                        # send-community
                                        if state_key_name == 'send-community':
                                            nbr_state_dict['send_community'] = str(state_key.text)
                                        # queues
                                        if state_key_name == 'queues':
                                            for queue_key in state_key:
                                                queue_key_name = queue_key.tag[queue_key.tag.find('}')+1:]
                                                # input
                                                if queue_key_name == 'input':
                                                    nbr_state_dict['input_queue'] = int(queue_key.text)
                                                # output
                                                if queue_key_name == 'output':
                                                    nbr_state_dict['output_queue'] = int(queue_key.text)
                                        # session-state
                                        if state_key_name == 'session-state':
                                            nbr_state_dict['session_state'] = str(state_key.text).lower()
                                        # messages
                                        if state_key_name == 'messages':
                                            if 'bgp_neighbor_counters' not in nbr_state_dict:
                                                nbr_state_dict['bgp_neighbor_counters'] = {}
                                            if 'messages' not in nbr_state_dict['bgp_neighbor_counters']:
                                                nbr_state_dict['bgp_neighbor_counters']['messages'] = {}
                                            for messages_key in state_key:
                                                messages_key_name = messages_key.tag[messages_key.tag.find('}')+1:]
                                                # sent
                                                if messages_key_name == 'sent':
                                                    for sent_key in messages_key:
                                                        sent_key_name = sent_key.tag[sent_key.tag.find('}')+1:]
                                                        # NOTIFICATION
                                                        if sent_key_name == 'NOTIFICATION':
                                                            if 'sent' not in nbr_state_dict['bgp_neighbor_counters']['messages']:
                                                                nbr_state_dict['bgp_neighbor_counters']['messages']['sent'] = {}
                                                            if sent_key.text is not None:
                                                                nbr_state_dict['bgp_neighbor_counters']['messages']['sent']['notifications'] = int(sent_key.text)
                                                        # UPDATES
                                                        if sent_key_name == 'UPDATE':
                                                            if 'sent' not in nbr_state_dict['bgp_neighbor_counters']['messages']:
                                                                nbr_state_dict['bgp_neighbor_counters']['messages']['sent'] = {}
                                                            if sent_key.text is not None:
                                                                nbr_state_dict['bgp_neighbor_counters']['messages']['sent']['updates'] = int(sent_key.text)
                                                # received
                                                if messages_key_name == 'received':
                                                    for received_key in messages_key:
                                                        received_key_name = received_key.tag[received_key.tag.find('}')+1:]
                                                        # NOTIFICATION
                                                        if received_key_name == 'NOTIFICATION':
                                                            if 'received' not in nbr_state_dict['bgp_neighbor_counters']['messages']:
                                                                nbr_state_dict['bgp_neighbor_counters']['messages']['received'] = {}
                                                            if received_key.text is not None:
                                                                nbr_state_dict['bgp_neighbor_counters']['messages']['received']['notifications'] = int(received_key.text)
                                                        # UPDATES
                                                        if received_key_name == 'UPDATE':
                                                            if 'received' not in nbr_state_dict['bgp_neighbor_counters']['messages']:
                                                                nbr_state_dict['bgp_neighbor_counters']['messages']['received'] = {}
                                                            if received_key.text is not None:
                                                                nbr_state_dict['bgp_neighbor_counters']['messages']['received']['updates'] = int(received_key.text)

                                # Tag: transport
                                if neighbor_key_name == 'transport':
                                    for transport_key in neighbor_key:
                                        transport_key_name = transport_key.tag[transport_key.tag.find('}')+1:]
                                        if transport_key_name == 'state':
                                            for transport_state_key in transport_key:
                                                transport_state_key_name = transport_state_key.tag[transport_state_key.tag.find('}')+1:]
                                                # local-address
                                                if transport_state_key_name == 'local-address':
                                                    nbr_transport_dict['local_host'] = transport_state_key.text
                                                # passive-mode
                                                if transport_state_key_name == 'passive-mode':
                                                    nbr_transport_dict['passive_mode'] = transport_state_key.text
                                                # local-port
                                                if transport_state_key_name == 'local-port':
                                                    nbr_transport_dict['local_port'] = transport_state_key.text
                                                # remote-address
                                                if transport_state_key_name == 'remote-address':
                                                    nbr_transport_dict['foreign_port'] = transport_state_key.text
                                                # remote-port
                                                if transport_state_key_name == 'remote-port':
                                                    nbr_transport_dict['foreign_host'] = transport_state_key.text

                                # Tag: timers
                                if neighbor_key_name == 'timers':
                                    for timers_key in neighbor_key:
                                        timers_key_name = timers_key.tag[timers_key.tag.find('}')+1:]
                                        if timers_key_name == 'state':
                                            
                                            for timers_state_key in timers_key:
                                                timers_state_key_name = timers_state_key.tag[timers_state_key.tag.find('}')+1:]
                                                # hold-time
                                                if timers_state_key_name == 'hold-time':
                                                    nbr_timers_dict['holdtime'] = int(timers_state_key.text)
                                                # keepalive-interval
                                                if timers_state_key_name == 'keepalive-interval':
                                                    nbr_timers_dict['keepalive_interval'] = int(timers_state_key.text)
                                                # minimum-advertisement-interval
                                                if timers_state_key_name == 'minimum-advertisement-interval':
                                                    nbr_timers_dict['minimum_advertisement_interval'] = int(timers_state_key.text)
                                                # negotiated-hold-time
                                                if timers_state_key_name == 'negotiated-hold-time':
                                                    nbr_timers_dict['holdtime'] = int(timers_state_key.text)

                                # Tag: 'graceful-restart'
                                if neighbor_key_name == 'graceful-restart':
                                    for gr_key in neighbor_key:
                                        gr_key_name = gr_key.tag[gr_key.tag.find('}')+1:]
                                        if gr_key_name == 'state':
                                            for gr_state_key in gr_key:
                                                gr_state_key_name = gr_state_key.tag[gr_state_key.tag.find('}')+1:]
                                                # enabled
                                                if gr_state_key_name == 'enabled':
                                                    if gr_state_key.text == 'false':
                                                        nbr_gr_dict['graceful_restart'] = False
                                                    elif gr_state_key.text == 'true':
                                                        nbr_gr_dict['graceful_restart'] = True
                                                # helper-only
                                                if gr_state_key_name == 'helper-only':
                                                    if gr_state_key.text == 'false':
                                                        nbr_gr_dict['graceful_restart_helper_only'] = False
                                                    elif gr_state_key.text == 'true':
                                                        nbr_gr_dict['graceful_restart_helper_only'] = True
                                                # restart-time
                                                if gr_state_key_name == 'restart-time':
                                                    nbr_gr_dict['graceful_restart_restart_time'] = int(gr_state_key.text)
                                                # stale-routes-time
                                                if gr_state_key_name == 'stale-routes-time':
                                                    nbr_gr_dict['graceful_restart_stalepath_time'] = int(gr_state_key.text)
                                                # peer-restart-time
                                                if gr_state_key_name == 'peer-restart-time':
                                                    nbr_gr_dict['graceful_restart_restart_time'] = int(gr_state_key.text)

                                # Tag: ebgp-multihop
                                if neighbor_key_name == 'ebgp-multihop':
                                    for ebgp_key in neighbor_key:
                                        ebgp_key_name = ebgp_key.tag[ebgp_key.tag.find('}')+1:]
                                        if ebgp_key_name == 'state':
                                            for ebgp_state_key in ebgp_key:
                                                ebgp_state_key_name = ebgp_state_key.tag[ebgp_state_key.tag.find('}')+1:]
                                                if ebgp_state_key_name == 'enabled':
                                                    if ebgp_state_key.text == 'true':
                                                        nbr_ebgp_dict['nbr_ebgp_multihop'] = True
                                                    else:
                                                        nbr_ebgp_dict['nbr_ebgp_multihop'] = False
                                                if ebgp_state_key_name == 'multihop-ttl':
                                                    nbr_ebgp_dict['nbr_ebgp_multihop_max_hop'] = int(ebgp_state_key.text)

                                # Tag: as-path-options
                                if neighbor_key_name == 'as-path-options':
                                    for as_path_key in neighbor_key:
                                        as_path_key_name = as_path_key.tag[as_path_key.tag.find('}')+1:]
                                        if as_path_key_name == 'state':
                                            for as_path_state_key in as_path_key:
                                                as_path_state_key_name = as_path_state_key.tag[as_path_state_key.tag.find('}')+1:]
                                                if as_path_state_key_name == 'allow-own-as':
                                                    nbr_as_path_dict['allow_own_as'] = int(as_path_state_key.text)

                                # Tag: route-reflector
                                if neighbor_key_name == 'route-reflector':
                                    for rr_key in neighbor_key:
                                        rr_key_name = rr_key.tag[rr_key.tag.find('}')+1:]
                                        if rr_key_name == 'state':
                                            for rr_state_key in rr_key:
                                                rr_state_key_name = rr_state_key.tag[rr_state_key.tag.find('}')+1:]
                                                if rr_state_key_name == 'route-reflector-client':
                                                    if rr_state_key.text == 'true':
                                                        nbr_rr_dict['route_reflector_client'] = True
                                                    elif rr_state_key.text == 'false':
                                                        nbr_rr_dict['route_reflector_client'] = False
                                                if rr_state_key_name == 'route-reflector-cluster-id':
                                                    nbr_rr_dict['route_reflector_cluster_id'] = int(rr_state_key.text)

                                # Tag: logging
                                if neighbor_key_name == 'logging-options':
                                    for logging_key in neighbor_key:
                                        logging_key_name = logging_key.tag[logging_key.tag.find('}')+1:]
                                        if logging_key_name == 'state':
                                            logging_dict = {}
                                            for logging_state_key in logging_key:
                                                logging_state_key_name = logging_state_key.tag[logging_state_key.tag.find('}')+1:]
                                                if logging_state_key_name == 'log-neighbor-state-changes':
                                                    if logging_state_key.text == 'true':
                                                        logging_dict['log_neighbor_changes'] = True
                                                    else:
                                                        logging_dict['log_neighbor_changes'] = False
                                    # Add to main vrf dict
                                    if 'vrf' not in parsed_dict:
                                        parsed_dict['vrf'] = {}
                                    if 'default' not in parsed_dict['vrf']:
                                        parsed_dict['vrf']['default'] = {}
                                    parsed_dict['vrf']['default']['log_neighbor_changes'] = logging_dict['log_neighbor_changes']

                                # Tag: afi-safis
                                if neighbor_key_name == 'afi-safis':
                                    for safis_key in neighbor_key:
                                        safis_key_name = safis_key.tag[safis_key.tag.find('}')+1:]
                                        if safis_key_name == 'afi-safi':
                                            for safi_key in safis_key:
                                                safi_key_name = safi_key.tag[safi_key.tag.find('}')+1:]
                                                
                                                # afi-safi-name
                                                if safi_key_name == 'afi-safi-name':
                                                    address_family = str(safi_key.text).lower()
                                                    address_family = address_family.replace("_", " ")
                                                    if 'address_family' not in nbr_safis_dict:
                                                        nbr_safis_dict['address_family'] = {}
                                                    if address_family not in nbr_safis_dict['address_family'] and\
                                                       address_family != 'none':
                                                        nbr_safis_dict['address_family'][address_family] = {}
                                                
                                                # state
                                                if safi_key_name == 'state' and address_family != 'none':
                                                    for state_key in safi_key:
                                                        state_key_name = state_key.tag[state_key.tag.find('}')+1:]
                                                        # enabled
                                                        if state_key_name == 'enabled':
                                                            if state_key.text == 'true':
                                                                nbr_safis_dict['address_family'][address_family]['enabled'] = True
                                                            else:
                                                                nbr_safis_dict['address_family'][address_family]['enabled'] = False
                                                        # active
                                                        if state_key_name == 'active':
                                                            if state_key.text == 'true':
                                                                nbr_safis_dict['address_family'][address_family]['active'] = True
                                                            else:
                                                                nbr_safis_dict['address_family'][address_family]['active'] = False
                                                        # prefixes
                                                        if state_key_name == 'prefixes':
                                                            for prefix_key in state_key:
                                                                prefix_key_name = prefix_key.tag[prefix_key.tag.find('}')+1:]
                                                                # received
                                                                if prefix_key_name == 'received':
                                                                    nbr_safis_dict['address_family'][address_family]['prefixes_received'] = int(prefix_key.text)
                                                                # sent
                                                                if prefix_key_name == 'sent':
                                                                    nbr_safis_dict['address_family'][address_family]['prefixes_sent'] = int(prefix_key.text)
                                                
                                                # graceful_restart
                                                if safi_key_name == 'graceful-restart' and address_family != 'none':
                                                    for gr_key in safi_key:
                                                        gr_key_name = gr_key.tag[gr_key.tag.find('}')+1:]
                                                        # state
                                                        if gr_key_name == 'state':
                                                            for gr_state_key in gr_key:
                                                                gr_state_key_name = gr_state_key.tag[gr_state_key.tag.find('}')+1:]
                                                                # enabled
                                                                if gr_state_key_name == 'enabled':
                                                                    if gr_state_key.text == 'true':
                                                                        nbr_safis_dict['address_family'][address_family]['graceful_restart'] = True
                                                                    else:
                                                                        nbr_safis_dict['address_family'][address_family]['graceful_restart'] = False

                                                # ipv6-unicast
                                                if safi_key_name == 'ipv6-unicast' and address_family != 'none':
                                                    for ipv6_key in safi_key:
                                                        ipv6_key_name = ipv6_key.tag[ipv6_key.tag.find('}')+1:]
                                                        # state
                                                        if ipv6_key_name == 'state':
                                                            for ipv6_state_key in ipv6_key:
                                                                ipv6_state_key_name = ipv6_state_key.tag[ipv6_state_key.tag.find('}')+1:]
                                                                # send-default-route
                                                                if ipv6_state_key_name == 'send-default-route':
                                                                    if ipv6_state_key.text == 'true':
                                                                        nbr_safis_dict['address_family'][address_family]['ipv6_unicast_send_default_route'] = True
                                                                    else:
                                                                        nbr_safis_dict['address_family'][address_family]['ipv6_unicast_send_default_route'] = False

                                                # ipv4-unicast
                                                if safi_key_name == 'ipv4-unicast' and address_family != 'none':
                                                    for ipv4_key in safi_key:
                                                        ipv4_key_name = ipv4_key.tag[ipv4_key.tag.find('}')+1:]
                                                        # state
                                                        if ipv4_key_name == 'state':
                                                            for ipv4_state_key in ipv4_key:
                                                                ipv4_state_key_name = ipv4_state_key.tag[ipv4_state_key.tag.find('}')+1:]
                                                                # send-default-route
                                                                if ipv4_state_key_name == 'send-default-route':
                                                                    if ipv4_state_key.text == 'true':
                                                                        nbr_safis_dict['address_family'][address_family]['ipv4_unicast_send_default_route'] = True
                                                                    else:
                                                                        nbr_safis_dict['address_family'][address_family]['ipv4_unicast_send_default_route'] = False
                                                                        continue

                                # Set all tag values to main dictionary
                                if neighbor_name is not None:
                                    
                                    # Set state tag values
                                    if nbr_state_dict:
                                        for key in nbr_state_dict:
                                            parsed_dict['vrf']['default']['neighbor'][neighbor_name][key] = nbr_state_dict[key]

                                    # Set timers tag values
                                    if nbr_timers_dict:
                                        for key in nbr_timers_dict:
                                            parsed_dict['vrf']['default']['neighbor'][neighbor_name][key] = nbr_timers_dict[key]

                                    # Set graceful-restart tag values
                                    if nbr_gr_dict:
                                        for key in nbr_gr_dict:
                                            parsed_dict['vrf']['default']['neighbor'][neighbor_name][key] = nbr_gr_dict[key]

                                    # Set ebgp-multihop tag values
                                    if nbr_ebgp_dict:
                                        for key in nbr_ebgp_dict:
                                            parsed_dict['vrf']['default']['neighbor'][neighbor_name][key] = nbr_ebgp_dict[key]

                                    # Set as-path-options tag values
                                    if nbr_as_path_dict:
                                        for key in nbr_as_path_dict:
                                            parsed_dict['vrf']['default']['neighbor'][neighbor_name][key] = nbr_as_path_dict[key]

                                    # Set route-reflector tag values
                                    if nbr_rr_dict:
                                        for key in nbr_rr_dict:
                                            parsed_dict['vrf']['default']['neighbor'][neighbor_name][key] = nbr_rr_dict[key]

                                    # Set transport tag values
                                    if nbr_transport_dict:
                                        if 'bgp_session_transport' not in parsed_dict['vrf']['default']['neighbor'][neighbor_name]:
                                            parsed_dict['vrf']['default']['neighbor'][neighbor_name]['bgp_session_transport'] = {}
                                        if 'transport' not in parsed_dict['vrf']['default']['neighbor'][neighbor_name]['bgp_session_transport']:
                                            parsed_dict['vrf']['default']['neighbor'][neighbor_name]['bgp_session_transport']['transport'] = {}
                                        parsed_dict['vrf']['default']['neighbor'][neighbor_name]['bgp_session_transport']['transport'] = nbr_transport_dict

                                    # Set address-family (safi-afi) tag values
                                    if nbr_safis_dict:
                                        if 'address_family' in nbr_safis_dict:
                                            if 'address_family' not in parsed_dict['vrf']['default']['neighbor'][neighbor_name]:
                                                parsed_dict['vrf']['default']['neighbor'][neighbor_name]['address_family'] = {}
                                                parsed_dict['vrf']['default']['neighbor'][neighbor_name]['address_family'] = nbr_safis_dict['address_family']

        return parsed_dict