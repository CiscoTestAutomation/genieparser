
# Python
import unittest
from unittest.mock import Mock
import xml.etree.ElementTree as ET

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_bgp
from parser.iosxr.show_bgp import ShowPlacementProgramAll,\
                                  ShowBgpInstanceAfGroupConfiguration,\
                                  ShowBgpInstanceSessionGroupConfiguration,\
                                  ShowBgpInstanceProcessDetail,\
                                  ShowBgpInstanceNeighborsDetail,\
                                  ShowBgpInstanceNeighborsAdvertisedRoutes,\
                                  ShowBgpInstanceNeighborsReceivedRoutes,\
                                  ShowBgpInstanceNeighborsRoutes,\
                                  ShowBgpInstanceSummary


# ==========================================
# Unit test for 'show placement program all'
# ==========================================

class test_show_placement_program_all(unittest.TestCase):
    
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'program': 
            {'rcp_fs':
                {'instance':
                    {'default':
                        {'active': '0/0/CPU0',
                        'active_state': 'RUNNING',
                        'group': 'central-services',
                        'jid': '1168',
                        'standby': 'NONE',
                        'standby_state': 'NOT_SPAWNED'}}},
            'ospf': 
                {'instance':
                    {'1':
                        {'active': '0/0/CPU0',
                        'active_state': 'RUNNING',
                        'group': 'v4-routing',
                        'jid': '1018',
                        'standby': 'NONE',
                        'standby_state': 'NOT_SPAWNED'}}},
            'bgp': 
                {'instance':
                    {'default':
                        {'active': '0/0/CPU0',
                        'active_state': 'RUNNING',
                        'group': 'v4-routing',
                        'jid': '1018',
                        'standby': 'NONE',
                        'standby_state': 'NOT_SPAWNED'}}},
            'statsd_manager_g': 
                {'instance':
                    {'default':
                        {'active': '0/0/CPU0',
                        'active_state': 'RUNNING',
                        'group': 'netmgmt',
                        'jid': '1141',
                        'standby': 'NONE',
                        'standby_state': 'NOT_SPAWNED'}}},
            'pim': 
                {'instance':
                    {'default':
                        {'active': '0/0/CPU0',
                        'active_state': 'RUNNING',
                        'group': 'mcast-routing',
                        'jid': '1158',
                        'standby': 'NONE',
                        'standby_state': 'NOT_SPAWNED'}}},
            'ipv6_local': 
                {'instance':
                    {'default':
                        {'active': '0/0/CPU0',
                        'active_state': 'RUNNING',
                        'group': 'v6-routing',
                        'jid': '1156',
                        'standby': 'NONE',
                        'standby_state': 'NOT_SPAWNED'}}}
            }
        }
    
    golden_output = {'execute.return_value': '''
            
            Display program related information. This is the program information corresponding to this LR as
            perceived by the placement daemon.
            ------------------------------------------------------------------------------------------------------------------------------------------
                               Process Information
            ------------------------------------------------------------------------------------------------------------------------------------------
            Program                                 Group               jid  Active         Active-state             Standby        Standby-state  
            ------------------------------------------------------------------------------------------------------------------------------------------
            rcp_fs                                  central-services    1168 0/0/CPU0       RUNNING                  NONE           NOT_SPAWNED    
            ospf(1)                                 v4-routing          1018 0/0/CPU0       RUNNING                  NONE           NOT_SPAWNED    
            bgp(default)                            v4-routing          1018 0/0/CPU0       RUNNING                  NONE           NOT_SPAWNED
            statsd_manager_g                        netmgmt             1141 0/0/CPU0       RUNNING                  NONE           NOT_SPAWNED    
            pim                                     mcast-routing       1158 0/0/CPU0       RUNNING                  NONE           NOT_SPAWNED    
            ipv6_local                              v6-routing          1156 0/0/CPU0       RUNNING                  NONE           NOT_SPAWNED    
      '''}


    golden_parsed_output1 = {
        'program': 
            {'auto_ip_ring': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                       'active_state': 'RUNNING',
                                                       'group': 'central-services',
                                                       'jid': '1156',
                                                       'standby': '0/RSP0/CPU0',
                                                       'standby_state': 'RUNNING'}}},
             'bfd': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                              'active_state': 'RUNNING',
                                              'group': 'central-services',
                                              'jid': '1158',
                                              'standby': '0/RSP0/CPU0',
                                              'standby_state': 'RUNNING'}}},
             'bgp': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                              'active_state': 'RUNNING',
                                              'group': 'v4-routing',
                                              'jid': '1051',
                                              'standby': '0/RSP0/CPU0',
                                              'standby_state': 'RUNNING'},
                                  'test': {'active': '0/RSP1/CPU0',
                                           'active_state': 'RUNNING',
                                           'group': 'Group_10_bgp2',
                                           'jid': '1052',
                                           'standby': '0/RSP0/CPU0',
                                           'standby_state': 'RUNNING'},
                                  'test1': {'active': '0/RSP1/CPU0',
                                            'active_state': 'RUNNING',
                                            'group': 'Group_5_bgp3',
                                            'jid': '1053',
                                            'standby': '0/RSP0/CPU0',
                                            'standby_state': 'RUNNING'},
                                  'test2': {'active': '0/RSP1/CPU0',
                                            'active_state': 'RUNNING',
                                            'group': 'Group_5_bgp4',
                                            'jid': '1054',
                                            'standby': '0/RSP0/CPU0',
                                            'standby_state': 'RUNNING'}}},
             'bgp_epe': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                  'active_state': 'RUNNING',
                                                  'group': 'v4-routing',
                                                  'jid': '1159',
                                                  'standby': '0/RSP0/CPU0',
                                                  'standby_state': 'RUNNING'}}},
             'bpm': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                              'active_state': 'RUNNING',
                                              'group': 'v4-routing',
                                              'jid': '1066',
                                              'standby': '0/RSP0/CPU0',
                                              'standby_state': 'RUNNING'}}},
             'bundlemgr_distrib': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                            'active_state': 'RUNNING',
                                                            'group': 'central-services',
                                                            'jid': '1157',
                                                            'standby': '0/RSP0/CPU0',
                                                            'standby_state': 'RUNNING'}}},
             'domain_services': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                          'active_state': 'RUNNING',
                                                          'group': 'central-services',
                                                          'jid': '1160',
                                                          'standby': '0/RSP0/CPU0',
                                                          'standby_state': 'RUNNING'}}},
             'es_acl_mgr': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                     'active_state': 'RUNNING',
                                                     'group': 'central-services',
                                                     'jid': '1169',
                                                     'standby': '0/RSP0/CPU0',
                                                     'standby_state': 'RUNNING'}}},
             'eth_gl_cfg': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                     'active_state': 'RUNNING',
                                                     'group': 'central-services',
                                                     'jid': '1151',
                                                     'standby': '0/RSP0/CPU0',
                                                     'standby_state': 'RUNNING'}}},
             'ethernet_stats_controller_edm': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                                        'active_state': 'RUNNING',
                                                                        'group': 'central-services',
                                                                        'jid': '1161',
                                                                        'standby': '0/RSP0/CPU0',
                                                                        'standby_state': 'RUNNING'}}},
             'ftp_fs': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                 'active_state': 'RUNNING',
                                                 'group': 'central-services',
                                                 'jid': '1162',
                                                 'standby': '0/RSP0/CPU0',
                                                 'standby_state': 'RUNNING'}}},
             'icpe_satmgr': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                      'active_state': 'RUNNING',
                                                      'group': 'central-services',
                                                      'jid': '1163',
                                                      'standby': '0/RSP0/CPU0',
                                                      'standby_state': 'RUNNING'}}},
             'igmp': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                               'active_state': 'RUNNING',
                                               'group': 'mcast-routing',
                                               'jid': '1208',
                                               'standby': '0/RSP0/CPU0',
                                               'standby_state': 'RUNNING'}}},
             'intf_mgbl': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                    'active_state': 'RUNNING',
                                                    'group': 'central-services',
                                                    'jid': '1143',
                                                    'standby': '0/RSP0/CPU0',
                                                    'standby_state': 'RUNNING'}}},
             'ipv4_connected': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                         'active_state': 'RUNNING',
                                                         'group': 'v4-routing',
                                                         'jid': '1152',
                                                         'standby': '0/RSP0/CPU0',
                                                         'standby_state': 'RUNNING'}}},
             'ipv4_local': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                     'active_state': 'RUNNING',
                                                     'group': 'v4-routing',
                                                     'jid': '1153',
                                                     'standby': '0/RSP0/CPU0',
                                                     'standby_state': 'RUNNING'}}},
             'ipv4_mfwd_ma': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                       'active_state': 'RUNNING',
                                                       'group': 'mcast-routing',
                                                       'jid': '1204',
                                                       'standby': '0/RSP0/CPU0',
                                                       'standby_state': 'RUNNING'}}},
             'ipv4_mpa': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                   'active_state': 'RUNNING',
                                                   'group': 'central-services',
                                                   'jid': '1149',
                                                   'standby': '0/RSP0/CPU0',
                                                   'standby_state': 'RUNNING'}}},
             'ipv4_rib': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                   'active_state': 'RUNNING',
                                                   'group': 'v4-routing',
                                                   'jid': '1146',
                                                   'standby': '0/RSP0/CPU0',
                                                   'standby_state': 'RUNNING'}}},
             'ipv4_rump': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                    'active_state': 'RUNNING',
                                                    'group': 'v4-routing',
                                                    'jid': '1167',
                                                    'standby': '0/RSP0/CPU0',
                                                    'standby_state': 'RUNNING'}}},
             'ipv4_static': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                      'active_state': 'RUNNING',
                                                      'group': 'v4-routing',
                                                      'jid': '1043',
                                                      'standby': '0/RSP0/CPU0',
                                                      'standby_state': 'RUNNING'}}},
             'ipv6_connected': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                         'active_state': 'RUNNING',
                                                         'group': 'v6-routing',
                                                         'jid': '1154',
                                                         'standby': '0/RSP0/CPU0',
                                                         'standby_state': 'RUNNING'}}},
             'ipv6_local': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                     'active_state': 'RUNNING',
                                                     'group': 'v6-routing',
                                                     'jid': '1155',
                                                     'standby': '0/RSP0/CPU0',
                                                     'standby_state': 'RUNNING'}}},
             'ipv6_mfwd_ma': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                       'active_state': 'RUNNING',
                                                       'group': 'mcast-routing',
                                                       'jid': '1205',
                                                       'standby': '0/RSP0/CPU0',
                                                       'standby_state': 'RUNNING'}}},
             'ipv6_mpa': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                   'active_state': 'RUNNING',
                                                   'group': 'central-services',
                                                   'jid': '1150',
                                                   'standby': '0/RSP0/CPU0',
                                                   'standby_state': 'RUNNING'}}},
             'ipv6_rib': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                   'active_state': 'RUNNING',
                                                   'group': 'v6-routing',
                                                   'jid': '1147',
                                                   'standby': '0/RSP0/CPU0',
                                                   'standby_state': 'RUNNING'}}},
             'ipv6_rump': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                    'active_state': 'RUNNING',
                                                    'group': 'v6-routing',
                                                    'jid': '1168',
                                                    'standby': '0/RSP0/CPU0',
                                                    'standby_state': 'RUNNING'}}},
             'l2tp_mgr': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                   'active_state': 'RUNNING',
                                                   'group': 'v4-routing',
                                                   'jid': '1176',
                                                   'standby': '0/RSP0/CPU0',
                                                   'standby_state': 'RUNNING'}}},
             'l2vpn_mgr': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                    'active_state': 'RUNNING',
                                                    'group': 'v4-routing',
                                                    'jid': '1175',
                                                    'standby': '0/RSP0/CPU0',
                                                    'standby_state': 'RUNNING'}}},
             'mld': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                              'active_state': 'RUNNING',
                                              'group': 'mcast-routing',
                                              'jid': '1209',
                                              'standby': '0/RSP0/CPU0',
                                              'standby_state': 'RUNNING'}}},
             'mpls_ldp': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                   'active_state': 'RUNNING',
                                                   'group': 'v4-routing',
                                                   'jid': '1199',
                                                   'standby': '0/RSP0/CPU0',
                                                   'standby_state': 'RUNNING'}}},
             'mpls_static': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                      'active_state': 'RUNNING',
                                                      'group': 'v4-routing',
                                                      'jid': '1142',
                                                      'standby': '0/RSP0/CPU0',
                                                      'standby_state': 'RUNNING'}}},
             'mrib': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                               'active_state': 'RUNNING',
                                               'group': 'mcast-routing',
                                               'jid': '1206',
                                               'standby': '0/RSP0/CPU0',
                                               'standby_state': 'RUNNING'}}},
             'mrib6': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                'active_state': 'RUNNING',
                                                'group': 'mcast-routing',
                                                'jid': '1207',
                                                'standby': '0/RSP0/CPU0',
                                                'standby_state': 'RUNNING'}}},
             'netconf': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                  'active_state': 'RUNNING',
                                                  'group': 'central-services',
                                                  'jid': '1189',
                                                  'standby': '0/RSP0/CPU0',
                                                  'standby_state': 'RUNNING'}}},
             'nfmgr': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                'active_state': 'RUNNING',
                                                'group': 'central-services',
                                                'jid': '1145',
                                                'standby': '0/RSP0/CPU0',
                                                'standby_state': 'RUNNING'}}},
             'ospf': {'instance': {'1': {'active': '0/RSP1/CPU0',
                                         'active_state': 'RUNNING',
                                         'group': 'v4-routing',
                                         'jid': '1018',
                                         'standby': '0/RSP0/CPU0',
                                         'standby_state': 'RUNNING'}}},
             'ospf_uv': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                  'active_state': 'RUNNING',
                                                  'group': 'v4-routing',
                                                  'jid': '1114',
                                                  'standby': '0/RSP0/CPU0',
                                                  'standby_state': 'RUNNING'}}},
             'pbr_ma': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                 'active_state': 'RUNNING',
                                                 'group': 'central-services',
                                                 'jid': '1171',
                                                 'standby': '0/RSP0/CPU0',
                                                 'standby_state': 'RUNNING'}}},
             'pim': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                              'active_state': 'RUNNING',
                                              'group': 'mcast-routing',
                                              'jid': '1210',
                                              'standby': '0/RSP0/CPU0',
                                              'standby_state': 'RUNNING'}}},
             'pim6': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                               'active_state': 'RUNNING',
                                               'group': 'mcast-routing',
                                               'jid': '1211',
                                               'standby': '0/RSP0/CPU0',
                                               'standby_state': 'RUNNING'}}},
             'policy_repository': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                            'active_state': 'RUNNING',
                                                            'group': 'v4-routing',
                                                            'jid': '1148',
                                                            'standby': '0/RSP0/CPU0',
                                                            'standby_state': 'RUNNING'}}},
             'python_process_manager': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                                 'active_state': 'RUNNING',
                                                                 'group': 'central-services',
                                                                 'jid': '1164',
                                                                 'standby': '0/RSP0/CPU0',
                                                                 'standby_state': 'RUNNING'}}},
             'qos_ma': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                 'active_state': 'RUNNING',
                                                 'group': 'central-services',
                                                 'jid': '1172',
                                                 'standby': '0/RSP0/CPU0',
                                                 'standby_state': 'RUNNING'}}},
             'rcp_fs': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                 'active_state': 'RUNNING',
                                                 'group': 'central-services',
                                                 'jid': '1165',
                                                 'standby': '0/RSP0/CPU0',
                                                 'standby_state': 'RUNNING'}}},
             'rt_check_mgr': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                       'active_state': 'RUNNING',
                                                       'group': 'v4-routing',
                                                       'jid': '1170',
                                                       'standby': '0/RSP0/CPU0',
                                                       'standby_state': 'RUNNING'}}},
             'schema_server': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                        'active_state': 'RUNNING',
                                                        'group': 'central-services',
                                                        'jid': '1177',
                                                        'standby': '0/RSP0/CPU0',
                                                        'standby_state': 'RUNNING'}}},
             'snmppingd': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                    'active_state': 'RUNNING',
                                                    'group': 'central-services',
                                                    'jid': '1195',
                                                    'standby': '0/RSP0/CPU0',
                                                    'standby_state': 'RUNNING'}}},
             'spa_cfg_hlpr': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                       'active_state': 'RUNNING',
                                                       'group': 'central-services',
                                                       'jid': '1130',
                                                       'standby': '0/RSP0/CPU0',
                                                       'standby_state': 'RUNNING'}}},
             'ssh_conf_verifier': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                            'active_state': 'RUNNING',
                                                            'group': 'central-services',
                                                            'jid': '1183',
                                                            'standby': '0/RSP0/CPU0',
                                                            'standby_state': 'RUNNING'}}},
             'ssh_server': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                     'active_state': 'RUNNING',
                                                     'group': 'central-services',
                                                     'jid': '1184',
                                                     'standby': '0/RSP0/CPU0',
                                                     'standby_state': 'RUNNING'}}},
             'statsd_manager_g': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                           'active_state': 'RUNNING',
                                                           'group': 'netmgmt',
                                                           'jid': '1144',
                                                           'standby': '0/RSP0/CPU0',
                                                           'standby_state': 'RUNNING'}}},
             'telemetry_encoder': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                            'active_state': 'RUNNING',
                                                            'group': 'central-services',
                                                            'jid': '1194',
                                                            'standby': '0/RSP0/CPU0',
                                                            'standby_state': 'RUNNING'}}},
             'tty_verifyd': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                      'active_state': 'RUNNING',
                                                      'group': 'central-services',
                                                      'jid': '1166',
                                                      'standby': '0/RSP0/CPU0',
                                                      'standby_state': 'RUNNING'}}},
             'vservice_mgr': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                       'active_state': 'RUNNING',
                                                       'group': 'central-services',
                                                       'jid': '1173',
                                                       'standby': '0/RSP0/CPU0',
                                                       'standby_state': 'RUNNING'}}},
             'wanphy_proc': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                      'active_state': 'RUNNING',
                                                      'group': 'central-services',
                                                      'jid': '1178',
                                                      'standby': '0/RSP0/CPU0',
                                                      'standby_state': 'RUNNING'}}},
             'xtc_agent': {'instance': {'default': {'active': '0/RSP1/CPU0',
                                                    'active_state': 'RUNNING',
                                                    'group': 'central-services',
                                                    'jid': '1174',
                                                    'standby': '0/RSP0/CPU0',
                                                    'standby_state': 'RUNNING'}}}}}

    golden_output1 = {'execute.return_value': '''

        Mon Jul 17 18:58:33.074 PDT
        Display program related information. This is the program information corresponding to this LR as
        perceived by the placement daemon.
        ------------------------------------------------------------------------------------------------------------------------------------------
                           Process Information
        ------------------------------------------------------------------------------------------------------------------------------------------
        Program                                 Group               jid  Active         Active-state             Standby        Standby-state  
        ------------------------------------------------------------------------------------------------------------------------------------------
        schema_server                           central-services    1177 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        vservice_mgr                            central-services    1173 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        ipv4_mpa                                central-services    1149 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        qos_ma                                  central-services    1172 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        icpe_satmgr                             central-services    1163 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        eth_gl_cfg                              central-services    1151 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        rcp_fs                                  central-services    1165 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        ssh_server                              central-services    1184 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        es_acl_mgr                              central-services    1169 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        snmppingd                               central-services    1195 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        xtc_agent                               central-services    1174 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        ftp_fs                                  central-services    1162 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        ipv6_mpa                                central-services    1150 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        telemetry_encoder                       central-services    1194 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        bfd                                     central-services    1158 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        ethernet_stats_controller_edm           central-services    1161 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        tty_verifyd                             central-services    1166 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        spa_cfg_hlpr                            central-services    1130 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        auto_ip_ring                            central-services    1156 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        nfmgr                                   central-services    1145 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        bundlemgr_distrib                       central-services    1157 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        netconf                                 central-services    1189 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        intf_mgbl                               central-services    1143 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        domain_services                         central-services    1160 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        python_process_manager                  central-services    1164 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        wanphy_proc                             central-services    1178 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        ssh_conf_verifier                       central-services    1183 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        pbr_ma                                  central-services    1171 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        rt_check_mgr                            v4-routing          1170 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        ipv4_rib                                v4-routing          1146 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        l2vpn_mgr                               v4-routing          1175 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        ipv4_connected                          v4-routing          1152 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        ospf(1)                                 v4-routing          1018 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        l2tp_mgr                                v4-routing          1176 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        bgp_epe                                 v4-routing          1159 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        ospf_uv                                 v4-routing          1114 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        bpm                                     v4-routing          1066 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        ipv4_rump                               v4-routing          1167 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        ipv4_static                             v4-routing          1043 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        mpls_ldp                                v4-routing          1199 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        bgp(default)                            v4-routing          1051 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        policy_repository                       v4-routing          1148 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        mpls_static                             v4-routing          1142 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        ipv4_local                              v4-routing          1153 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        statsd_manager_g                        netmgmt             1144 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        igmp                                    mcast-routing       1208 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        mrib                                    mcast-routing       1206 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        ipv4_mfwd_ma                            mcast-routing       1204 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        pim6                                    mcast-routing       1211 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        ipv6_mfwd_ma                            mcast-routing       1205 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        mld                                     mcast-routing       1209 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        pim                                     mcast-routing       1210 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        mrib6                                   mcast-routing       1207 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        ipv6_rib                                v6-routing          1147 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        ipv6_connected                          v6-routing          1154 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        ipv6_local                              v6-routing          1155 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        ipv6_rump                               v6-routing          1168 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        bgp(test)                               Group_10_bgp2       1052 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        bgp(test1)                              Group_5_bgp3        1053 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        bgp(test2)                              Group_5_bgp4        1054 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING        
        ------------------------------------------------------------------------------------------------------------------------------------------
        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        placement_program_all_obj = ShowPlacementProgramAll(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = placement_program_all_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        placement_program_all_obj = ShowPlacementProgramAll(device=self.device)
        parsed_output = placement_program_all_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        placement_program_all_obj = ShowPlacementProgramAll(device=self.device)
        parsed_output = placement_program_all_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output1)


# ======================================================================
# Unit test for 'show bgp instance <WORD> af-group <WORD> configuration'
# ======================================================================

class test_show_bgp_instance_af_group_configuration(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        "instance": {
            "default": {
                "pp_name": {
                    "af_group": {
                        "address_family": "ipv4 unicast",
                        "default_originate": True,
                        "default_originate_route_map": "allpass",
                        "max_prefix_no": 429,
                        "max_prefix_threshold": 75,
                        "max_prefix_restart": 35,
                        "next_hop_self": True,
                        "route_map_name_in": "allpass",
                        "route_map_name_out": "allpass",
                        "route_reflector_client": True,
                        "send_community": "both",
                        "send_comm_ebgp": True,
                        "send_ext_comm_ebgp": True,
                        "soo": "100:1",
                        "soft_reconfiguration": "inbound always",
                        "allowas_in_as_number": 10,
                        "allowas_in": True,
                        "as_override": True
                    }
                }
            }
        }

    }

    golden_output = {'execute.return_value': '''

    Fri Jul 14 16:30:21.081 EDT
    Building configuration...    
    router bgp 100 af-group af_group address-family ipv4 unicast 

        Wed Jul 12 15:42:07.027 EDT
    af-group af_group address-family IPv4 Unicast
      default-originate policy allpass            []
      maximum-prefix 429 75 35                    []
      next-hop-self                               []
      policy allpass in                           []
      policy allpass out                          []
      route-reflector-client                      []
      send-community-ebgp                         []
      send-extended-community-ebgp                []
      site-of-origin 100:1                        []
      soft-reconfiguration inbound always         []
      allowas-in 10                               []
      as-override                                 []

        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowBgpInstanceAfGroupConfiguration(device=self.device1)
        self.maxDiff = None
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpInstanceAfGroupConfiguration(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ===========================================================================
# Unit test for 'show bgp instance <WORD> session-group <WORD> configuration'
# ===========================================================================

class test_show_bgp_instance_session_group_configuration(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "instance": {
            "default": {
                "peer_session": {
                    "SG": {
                        "remote_as": 333,
                        "fall_over_bfd": True,
                        "password_text": "094F471A1A0A464058",
                        "holdtime": 30,
                        "transport_connection_mode": "active-only",
                        "ebgp_multihop_max_hop": 254,
                        "local_replace_as": True,
                        "ps_minimum_holdtime": 3,
                        "keepalive_interval": 10,
                        "shutdown": True,
                        "local_dual_as": True,
                        "local_no_prepend": True,
                        "ebgp_multihop_enable": True,
                        "suppress_four_byte_as_capability": True,
                        "local_as_as_no": 200,
                        "description": "SG_group",
                        "update_source": 'loopback0',
                        "disable_connected_check": True}}}}}

    golden_output = {'execute.return_value': '''
        Fri Jul 14 17:50:40.461 EDT
        Building configuration...
        router bgp 100 session-group SG 

        Thu Jul 13 12:28:48.673 EDT
        session-group SG
         remote-as 333                              []
         description SG_group                       []
         ebgp-multihop 254                          []
         local-as 200 no-prepend replace-as dual-as []
         password encrypted 094F471A1A0A464058      []
         shutdown                                   []
         timers 10 30 3                             []
         update-source Loopback0                    []
         suppress-4byteas                           []
         session-open-mode active-only              []
         bfd fast-detect                            []
         ignore-connected                           []
        '''}

    golden_parsed_output1 = {
        'instance': 
            {'default': 
                {'peer_session': 
                    {'SG': 
                        {'description': 'LALALALLA',
                        'ebgp_multihop_enable': True,
                        'ebgp_multihop_max_hop': 255,
                        'fall_over_bfd': True,
                        'local_as_as_no': 10,
                        'local_no_prepend': True}}},
            'test': 
                {'peer_session': 
                    {'LALALALLA': 
                        {'description': 'LALALALLA',
                        'ebgp_multihop_enable': True,
                        'ebgp_multihop_max_hop': 255,
                        'fall_over_bfd': True,
                        'local_as_as_no': 10,
                        'local_no_prepend': True},
                    'abcd': 
                        {'description': 'LALALALLA',
                        'ebgp_multihop_enable': True,
                        'ebgp_multihop_max_hop': 255,
                        'fall_over_bfd': True,
                        'local_as_as_no': 10,
                        'local_no_prepend': True},
                    'efddd': 
                        {'description': 'LALALALLA',
                        'ebgp_multihop_enable': True,
                        'ebgp_multihop_max_hop': 255,
                        'fall_over_bfd': True,
                        'local_as_as_no': 10,
                        'local_no_prepend': True}}}}}

    golden_output1 = {'execute.return_value': '''
        router bgp 333 instance test session-group abcd
        router bgp 333 instance test session-group abcd bfd fast-detect
        router bgp 333 instance test session-group abcd description LALALALLA
        router bgp 333 instance test session-group efddd
        router bgp 333 instance test session-group efddd bfd fast-detect
        router bgp 333 instance test session-group efddd ebgp-multihop 255
        router bgp 333 instance test session-group efddd local-as 10 no-prepend
        router bgp 333 instance test neighbor 1.1.1.1 use session-group LALALALLA
        router bgp 100 session-group SG
        router bgp 100 session-group SG description SG

        RP/0/RSP1/CPU0:PE1#show bgp instance default session-group SG configuration
        Thu Jul 20 09:02:18.537 PDT
        session-group SG
         description SG  []

        RP/0/RSP1/CPU0:PE1#show bgp instance test session-group abcd configuration 
        Thu Jul 20 09:02:48.738 PDT
        session-group abcd
         description LALALALLA []
         bfd fast-detect       []

        RP/0/RSP1/CPU0:PE1#show bgp instance test session-group efddd configuration 
        Thu Jul 20 09:03:10.702 PDT
        session-group efddd
         ebgp-multihop 255      []
         local-as 10 no-prepend []
         bfd fast-detect        []
        
        RP/0/RSP1/CPU0:PE1#show bgp instance test session-group LALALALLA configuration 
        Thu Jul 20 09:03:41.151 PDT
        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowBgpInstanceSessionGroupConfiguration(device=self.device1)
        self.maxDiff = None
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpInstanceSessionGroupConfiguration(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowBgpInstanceSessionGroupConfiguration(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output1)


# ============================================================
# Unit test for 'show bgp instance all vrf all process detail'
# ============================================================
class test_show_bgp_instance_all_vrf_all_process_detail(unittest.TestCase):
    
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "instance": {
            "default": {
               "vrf": {
                    "a": {
                         "operation_mode": "STANDALONE",
                         "generic_scan_interval": 60,
                         "received_notifications": 0,
                         "default_value_for_bmp_buffer_size": 307,
                         "default_local_preference": 100,
                         "pool": {
                              "300": {
                                   "free": 0,
                                   "alloc": 1
                              },
                              "4500": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "20000": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "200": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "1200": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "600": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "5000": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "400": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "500": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "4000": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "2200": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "700": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "800": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "900": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "3300": {
                                   "free": 0,
                                   "alloc": 0
                              }
                         },
                         "sent_notifications": 0,
                         "fast_external_fallover": True,
                         "node": "node0_0_CPU0",
                         "non_stop_routing": True,
                         "max_limit_for_bmp_buffer_size": 409,
                         "att": {
                              "ppmp_attr": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "bmp_paths": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "paths": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "tunnel_encap_attr": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "route_reflector_entries": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "pmsi_tunnel_attr": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "ribrnh_tunnel_attr": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "attributes": {
                                   "memory_used": 152,
                                   "number": 1
                              },
                              "extended_communities": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "nexthop_entries": {
                                   "memory_used": 7600,
                                   "number": 19
                              },
                              "as_paths": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "bmp_prefixes": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "communities": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "pe_distinguisher_labels": {
                                   "memory_used": 0,
                                   "number": 0
                              }
                         },
                         "as_system_number_format": "ASPLAIN",
                         "active_cluster_id": "10",
                         "message_logging_pool_summary": {
                              "4500": {
                                   "free": 0,
                                   "alloc": 0
                              }
                         },
                         "update_delay": 120,
                         "platform_rlimit_max": 2147483648,
                         "bgp_speaker_process": 0,
                         "address_family": {
                              "ipv4 unicast ": {
                                   "nexthop_resolution_minimum_prefix_length": "0 (not configured)",
                                   "rib_table_prefix_limit_ver": "0",
                                   "state": "read only mode",
                                   "dynamic_med_timer": "Not Running",
                                   "table_version_synced_to_rib": "1",
                                   "soft_reconfig_entries": "0",
                                   "rib_table_prefix_limit_reached": "no",
                                   "dynamic_med_periodic_timer": "Not Running",
                                   "prefix_scanned_per_segment": "100000",
                                   "table_version_acked_by_rib": "0",
                                   "permanent_network": "unconfigured",
                                   "label_retention_timer_value": "5 mins",
                                   "dynamic_med_int": "10 minutes",
                                   "dynamic_med": True,
                                   "table_state": "inactive",
                                   "chunk_elememt_size": "3",
                                   "num_of_scan_segments": "0",
                                   "main_table_version": "1",
                                   "remote_local": {
                                        "prefixes": {
                                             "allocated": 0,
                                             "freed": 0
                                        }
                                   },
                                   "table_bit_field_size": "1 ",
                                   "dampening": False,
                                   "attribute_download": "Disabled",
                                   "rib_has_not_converged": "version 0",
                                   "prefixes_path": {
                                        "prefixes": {
                                             "number": 0,
                                             "mem_used": 0
                                        }
                                   },
                                   "scan_interval": "60",
                                   "bgp_table_version": "1",
                                   "current_vrf": "a ",
                                   "total_prefixes_scanned": "0"
                              }
                         },
                         "current_limit_for_bmp_buffer_size": 307,
                         "default_cluster_id": "10",
                         "received_updates": 0,
                         "current_utilization_of_bmp_buffer_limit": 0,
                         "sent_updates": 0,
                         "router_id": "4.4.4.4",
                         "bmp_pool_summary": {
                              "300": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "4500": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "20000": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "10000": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "200": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "100": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "6500": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "8500": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "400": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "600": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "2200": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "1200": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "500": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "4000": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "3300": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "5500": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "700": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "800": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "900": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "7500": {
                                   "free": 0,
                                   "alloc": 0
                              }
                         },
                         "as_number": 100,
                         "restart_count": 1,
                         "vrf_info": {
                              "non-default": {
                                   "nbrs_estab": 0,
                                   "total": 3,
                                   "cfg": 2
                              },
                              "default": {
                                   "nbrs_estab": 0,
                                   "total": 1,
                                   "cfg": 1
                              }
                         },
                         "neighbor_logging": True,
                         "default_keepalive": 60,
                         "enforce_first_as_enabled": True
                    },
                    "VRF1": {
                         "operation_mode": "STANDALONE",
                         "generic_scan_interval": 60,
                         "received_notifications": 0,
                         "default_local_preference": 100,
                         "pool": {
                              "300": {
                                   "free": 0,
                                   "alloc": 1
                              },
                              "4500": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "20000": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "200": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "1200": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "600": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "5000": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "400": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "500": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "4000": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "2200": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "700": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "800": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "900": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "3300": {
                                   "free": 0,
                                   "alloc": 0
                              }
                         },
                         "sent_notifications": 0,
                         "fast_external_fallover": True,
                         "node": "node0_0_CPU0",
                         "non_stop_routing": True,
                         "max_limit_for_bmp_buffer_size": 409,
                         "att": {
                              "ribrnh_tunnel_attr": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "attributes": {
                                   "memory_used": 152,
                                   "number": 1
                              },
                              "extended_communities": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "nexthop_entries": {
                                   "memory_used": 7600,
                                   "number": 19
                              },
                              "as_paths": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "communities": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "route_reflector_entries": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "tunnel_encap_attr": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "ppmp_attr": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "pe_distinguisher_labels": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "pmsi_tunnel_attr": {
                                   "memory_used": 0,
                                   "number": 0
                              }
                         },
                         "as_system_number_format": "ASPLAIN",
                         "active_cluster_id": "10",
                         "message_logging_pool_summary": {
                              "4500": {
                                   "free": 0,
                                   "alloc": 0
                              }
                         },
                         "update_delay": 120,
                         "platform_rlimit_max": 2147483648,
                         "default_cluster_id": "10",
                         "bgp_speaker_process": 0,
                         "current_limit_for_bmp_buffer_size": 307,
                         "default_value_for_bmp_buffer_size": 307,
                         "received_updates": 0,
                         "current_utilization_of_bmp_buffer_limit": 0,
                         "sent_updates": 0,
                         "router_id": "4.4.4.4",
                         "bmp_pool_summary": {
                              "300": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "4500": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "20000": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "10000": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "200": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "100": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "6500": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "8500": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "400": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "600": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "2200": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "1200": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "500": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "4000": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "3300": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "5500": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "700": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "800": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "900": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "7500": {
                                   "free": 0,
                                   "alloc": 0
                              }
                         },
                         "as_number": 100,
                         "restart_count": 1,
                         "vrf_info": {
                              "non-default": {
                                   "nbrs_estab": 0,
                                   "total": 3,
                                   "cfg": 2
                              },
                              "default": {
                                   "nbrs_estab": 0,
                                   "total": 1,
                                   "cfg": 1
                              }
                         },
                         "neighbor_logging": True,
                         "default_keepalive": 60,
                         "enforce_first_as_enabled": True
                    },
                    "vrf1": {
                         "operation_mode": "STANDALONE",
                         "generic_scan_interval": 60,
                         "received_notifications": 0,
                         "default_local_preference": 100,
                         "pool": {
                              "300": {
                                   "free": 0,
                                   "alloc": 1
                              },
                              "4500": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "20000": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "200": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "1200": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "600": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "5000": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "400": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "500": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "4000": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "2200": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "700": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "800": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "900": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "3300": {
                                   "free": 0,
                                   "alloc": 0
                              }
                         },
                         "sent_notifications": 0,
                         "fast_external_fallover": True,
                         "node": "node0_0_CPU0",
                         "non_stop_routing": True,
                         "max_limit_for_bmp_buffer_size": 409,
                         "att": {
                              "ribrnh_tunnel_attr": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "attributes": {
                                   "memory_used": 152,
                                   "number": 1
                              },
                              "extended_communities": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "nexthop_entries": {
                                   "memory_used": 7600,
                                   "number": 19
                              },
                              "as_paths": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "communities": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "route_reflector_entries": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "tunnel_encap_attr": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "ppmp_attr": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "pe_distinguisher_labels": {
                                   "memory_used": 0,
                                   "number": 0
                              },
                              "pmsi_tunnel_attr": {
                                   "memory_used": 0,
                                   "number": 0
                              }
                         },
                         "as_system_number_format": "ASPLAIN",
                         "active_cluster_id": "10",
                         "message_logging_pool_summary": {
                              "4500": {
                                   "free": 0,
                                   "alloc": 0
                              }
                         },
                         "update_delay": 120,
                         "platform_rlimit_max": 2147483648,
                         "default_cluster_id": "10",
                         "bgp_speaker_process": 0,
                         "current_limit_for_bmp_buffer_size": 307,
                         "default_value_for_bmp_buffer_size": 307,
                         "received_updates": 0,
                         "current_utilization_of_bmp_buffer_limit": 0,
                         "sent_updates": 0,
                         "router_id": "4.4.4.4",
                         "bmp_pool_summary": {
                              "300": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "4500": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "20000": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "10000": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "200": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "100": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "6500": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "8500": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "400": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "600": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "2200": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "1200": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "500": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "4000": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "3300": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "5500": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "700": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "800": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "900": {
                                   "free": 0,
                                   "alloc": 0
                              },
                              "7500": {
                                   "free": 0,
                                   "alloc": 0
                              }
                         },
                         "as_number": 100,
                         "restart_count": 1,
                         "vrf_info": {
                              "non-default": {
                                   "nbrs_estab": 0,
                                   "total": 3,
                                   "cfg": 2
                              },
                              "default": {
                                   "nbrs_estab": 0,
                                   "total": 1,
                                   "cfg": 1
                              }
                         },
                         "neighbor_logging": True,
                         "default_keepalive": 60,
                         "enforce_first_as_enabled": True
                    }
                }
            },
            "test": {}
        }
    }
    golden_output = {'execute.return_value': '''

        Wed Jul 12 16:37:22.420 EDT

        BGP instance 0: 'default'
        =========================

        VRF: a
        ------

        BGP Process Information: VRF a (Inactive)
        BGP Route Distinguisher: 100:1

        BGP is operating in STANDALONE mode
        Autonomous System number format: ASPLAIN
        Autonomous System: 100
        Router ID: 4.4.4.4
        Default Cluster ID: 10 (manually configured)
        Active Cluster IDs:  10
        Fast external fallover enabled
        Platform RLIMIT max: 2147483648 bytes
        Maximum limit for BMP buffer size: 409 MB
        Default value for BMP buffer size: 307 MB
        Current limit for BMP buffer size: 307 MB
        Current utilization of BMP buffer limit: 0 B
        Neighbor logging is enabled
        Enforce first AS enabled
        iBGP to IGP redistribution enabled
        Default local preference: 100
        Default keepalive: 60
        Non-stop routing is enabled
        Update delay: 120
        Generic scan interval: 60

        BGP Speaker process: 0, Node: node0_0_CPU0
        Restart count: 1
                                   Total           Nbrs Estab/Cfg
        Default VRFs:              1               0/1
        Non-Default VRFs:          3               0/2
        This VRF:                                  0/2

                                   Sent            Received
        Updates:                   0               0               
        Notifications:             0               0               

                                   Number          Memory Used
        Attributes:                1               152             
        AS Paths:                  0               0               
        Communities:               0               0               
        Extended communities:      0               0               
        PMSI Tunnel attr:          0               0               
        RIBRNH Tunnel attr:        0               0               
        PPMP attr:                 0               0               
        Tunnel Encap attr:         0               0               
        PE distinguisher labels:   0               0               
        Route Reflector Entries:   0               0               
        Nexthop Entries:           19              7600            

                                   Alloc           Free          
        Pool 200:                  0               0             
        Pool 300:                  1               0             
        Pool 400:                  0               0             
        Pool 500:                  0               0             
        Pool 600:                  0               0             
        Pool 700:                  0               0             
        Pool 800:                  0               0             
        Pool 900:                  0               0             
        Pool 1200:                 0               0             
        Pool 2200:                 0               0             
        Pool 3300:                 0               0             
        Pool 4000:                 0               0             
        Pool 4500:                 0               0             
        Pool 5000:                 0               0             
        Pool 20000:                0               0             

        Message logging pool summary:
                                   Alloc           Free          
        Pool 100:                  0               0             
        Pool 200:                  0               0             
        Pool 500:                  0               0             
        Pool 2200:                 0               0             
        Pool 4500:                 0               0             

        BMP pool summary:
                                   Alloc           Free          
        Pool 100:                  0               0             
        Pool 200:                  0               0             
        Pool 300:                  0               0             
        Pool 400:                  0               0             
        Pool 500:                  0               0             
        Pool 600:                  0               0             
        Pool 700:                  0               0             
        Pool 800:                  0               0             
        Pool 900:                  0               0             
        Pool 1200:                 0               0             
        Pool 2200:                 0               0             
        Pool 3300:                 0               0             
        Pool 4000:                 0               0             
        Pool 4500:                 0               0             
        Pool 5500:                 0               0             
        Pool 6500:                 0               0             
        Pool 7500:                 0               0             
        Pool 8500:                 0               0             
        Pool 10000:                0               0             
        Pool 20000:                0               0             

        VRF a Address family: IPv4 Unicast (Table inactive)
        Dampening is not enabled
        Client reflection is not enabled in global config
        Dynamic MED is Disabled
        Dynamic MED interval : 10 minutes
        Dynamic MED Timer : Not Running
        Dynamic MED Periodic Timer : Not Running
        Scan interval: 60
        Total prefixes scanned: 0
        Prefixes scanned per segment: 100000
        Number of scan segments: 0
        Nexthop resolution minimum prefix-length: 0 (not configured)
        Main Table Version: 1
        Table version synced to RIB: 1
        Table version acked by RIB: 0
        IGP notification: IGPs notified
        RIB has not converged: version 0
        RIB table prefix-limit reached ?  [No], version 0
        Permanent Network Unconfigured

        State: Read Only mode.
        BGP Table Version: 1
        Attribute download: Disabled
        Label retention timer value 5 mins
        Soft Reconfig Entries: 0
        Table bit-field size : 1 Chunk element size : 3

                           Last 8 Triggers       Ver         Tbl Ver     Trig TID  

        Label Thread       Total triggers: 0

        Import Thread      Total triggers: 0

        RIB Thread         Total triggers: 0

        Update Thread      Total triggers: 0

                                   Allocated       Freed         
        Prefixes:                  0               0             
        Paths:                     0               0             
        Path-elems:                0               0             

                                   Number          Mem Used      
        Prefixes:                  0               0             
        Paths:                     0               0             
        Path-elems:                0               0             
        BMP Prefixes:              0               0             
        BMP Paths:                 0               0             


        VRF: VRF1
        ---------

        BGP Process Information: VRF VRF1 (Inactive)
        BGP Route Distinguisher: 100:2

        BGP is operating in STANDALONE mode
        Autonomous System number format: ASPLAIN
        Autonomous System: 100
        Router ID: 4.4.4.4
        Default Cluster ID: 10 (manually configured)
        Active Cluster IDs:  10
        Fast external fallover enabled
        Platform RLIMIT max: 2147483648 bytes
        Maximum limit for BMP buffer size: 409 MB
        Default value for BMP buffer size: 307 MB
        Current limit for BMP buffer size: 307 MB
        Current utilization of BMP buffer limit: 0 B
        Neighbor logging is enabled
        Enforce first AS enabled
        iBGP to IGP redistribution enabled
        Default local preference: 100
        Default keepalive: 60
        Non-stop routing is enabled
        Update delay: 120
        Generic scan interval: 60

        BGP Speaker process: 0, Node: node0_0_CPU0
        Restart count: 1
                                   Total           Nbrs Estab/Cfg
        Default VRFs:              1               0/1
        Non-Default VRFs:          3               0/2
        This VRF:                                  0/0

                                   Sent            Received
        Updates:                   0               0               
        Notifications:             0               0               

                                   Number          Memory Used
        Attributes:                1               152             
        AS Paths:                  0               0               
        Communities:               0               0               
        Extended communities:      0               0               
        PMSI Tunnel attr:          0               0               
        RIBRNH Tunnel attr:        0               0               
        PPMP attr:                 0               0               
        Tunnel Encap attr:         0               0               
        PE distinguisher labels:   0               0               
        Route Reflector Entries:   0               0               
        Nexthop Entries:           19              7600            

                                   Alloc           Free          
        Pool 200:                  0               0             
        Pool 300:                  1               0             
        Pool 400:                  0               0             
        Pool 500:                  0               0             
        Pool 600:                  0               0             
        Pool 700:                  0               0             
        Pool 800:                  0               0             
        Pool 900:                  0               0             
        Pool 1200:                 0               0             
        Pool 2200:                 0               0             
        Pool 3300:                 0               0             
        Pool 4000:                 0               0             
        Pool 4500:                 0               0             
        Pool 5000:                 0               0             
        Pool 20000:                0               0             

        Message logging pool summary:
                                   Alloc           Free          
        Pool 100:                  0               0             
        Pool 200:                  0               0             
        Pool 500:                  0               0             
        Pool 2200:                 0               0             
        Pool 4500:                 0               0             

        BMP pool summary:
                                   Alloc           Free          
        Pool 100:                  0               0             
        Pool 200:                  0               0             
        Pool 300:                  0               0             
        Pool 400:                  0               0             
        Pool 500:                  0               0             
        Pool 600:                  0               0             
        Pool 700:                  0               0             
        Pool 800:                  0               0             
        Pool 900:                  0               0             
        Pool 1200:                 0               0             
        Pool 2200:                 0               0             
        Pool 3300:                 0               0             
        Pool 4000:                 0               0             
        Pool 4500:                 0               0             
        Pool 5500:                 0               0             
        Pool 6500:                 0               0             
        Pool 7500:                 0               0             
        Pool 8500:                 0               0             
        Pool 10000:                0               0             
        Pool 20000:                0               0             

        VRF: vrf1
        ---------

        BGP Process Information: VRF vrf1 (Inactive)
        BGP Route Distinguisher: 100:3

        BGP is operating in STANDALONE mode
        Autonomous System number format: ASPLAIN
        Autonomous System: 100
        Router ID: 4.4.4.4
        Default Cluster ID: 10 (manually configured)
        Active Cluster IDs:  10
        Fast external fallover enabled
        Platform RLIMIT max: 2147483648 bytes
        Maximum limit for BMP buffer size: 409 MB
        Default value for BMP buffer size: 307 MB
        Current limit for BMP buffer size: 307 MB
        Current utilization of BMP buffer limit: 0 B
        Neighbor logging is enabled
        Enforce first AS enabled
        iBGP to IGP redistribution enabled
        Default local preference: 100
        Default keepalive: 60
        Non-stop routing is enabled
        Update delay: 120
        Generic scan interval: 60

        BGP Speaker process: 0, Node: node0_0_CPU0
        Restart count: 1
                                   Total           Nbrs Estab/Cfg
        Default VRFs:              1               0/1
        Non-Default VRFs:          3               0/2
        This VRF:                                  0/0

                                   Sent            Received
        Updates:                   0               0               
        Notifications:             0               0               

                                   Number          Memory Used
        Attributes:                1               152             
        AS Paths:                  0               0               
        Communities:               0               0               
        Extended communities:      0               0               
        PMSI Tunnel attr:          0               0               
        RIBRNH Tunnel attr:        0               0               
        PPMP attr:                 0               0               
        Tunnel Encap attr:         0               0               
        PE distinguisher labels:   0               0               
        Route Reflector Entries:   0               0               
        Nexthop Entries:           19              7600            

                                   Alloc           Free          
        Pool 200:                  0               0             
        Pool 300:                  1               0             
        Pool 400:                  0               0             
        Pool 500:                  0               0             
        Pool 600:                  0               0             
        Pool 700:                  0               0             
        Pool 800:                  0               0             
        Pool 900:                  0               0             
        Pool 1200:                 0               0             
        Pool 2200:                 0               0             
        Pool 3300:                 0               0             
        Pool 4000:                 0               0             
        Pool 4500:                 0               0             
        Pool 5000:                 0               0             
        Pool 20000:                0               0             

        Message logging pool summary:
                                   Alloc           Free          
        Pool 100:                  0               0             
        Pool 200:                  0               0             
        Pool 500:                  0               0             
        Pool 2200:                 0               0             
        Pool 4500:                 0               0             

        BMP pool summary:
                                   Alloc           Free          
        Pool 100:                  0               0             
        Pool 200:                  0               0             
        Pool 300:                  0               0             
        Pool 400:                  0               0             
        Pool 500:                  0               0             
        Pool 600:                  0               0             
        Pool 700:                  0               0             
        Pool 800:                  0               0             
        Pool 900:                  0               0             
        Pool 1200:                 0               0             
        Pool 2200:                 0               0             
        Pool 3300:                 0               0             
        Pool 4000:                 0               0             
        Pool 4500:                 0               0             
        Pool 5500:                 0               0             
        Pool 6500:                 0               0             
        Pool 7500:                 0               0             
        Pool 8500:                 0               0             
        Pool 10000:                0               0             
        Pool 20000:                0               0             


        BGP instance 1: 'test'
        ======================
        % None of the requested address families are configured for instance 'test'(28591)         

    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpInstanceProcessDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf_type='vrf')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpInstanceProcessDetail(device=self.device)
        parsed_output = obj.parse(vrf_type='vrf')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ============================================================
# Unit test for 'show bgp instance all all all process detail'
# ============================================================
class test_show_bgp_instance_all_all_all_process_detail(unittest.TestCase):
    
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "instance": {
            "default": {
                "vrf": {
                    "default": {
                        "active_cluster_id": "1.1.1.1",
                        "router_id": "1.1.1.1",
                        "current_limit_for_bmp_buffer_size": 307,
                        "generic_scan_interval": 60,
                        "bgp_speaker_process": 0,
                        "sent_notifications": 1,
                        "fast_external_fallover": True,
                        "default_cluster_id": "1.1.1.1",
                        "non_stop_routing": True,
                        "att": {
                            "total_rds": {
                               "number": 4,
                               "memory_used": 320
                            },
                            "attributes": {
                               "number": 6,
                               "memory_used": 912
                            },
                            "local_paths": {
                               "number": 30,
                               "memory_used": 2640
                            },
                            "pmsi_tunnel_attr": {
                               "number": 0,
                               "memory_used": 0
                            },
                            "local_rds": {
                               "number": 2,
                               "memory_used": 160
                            },
                            "as_paths": {
                               "number": 6,
                               "memory_used": 480
                            },
                            "communities": {
                               "number": 0,
                               "memory_used": 0
                            },
                            "extended_communities": {
                               "number": 6,
                               "memory_used": 480
                            },
                            "nexthop_entries": {
                               "number": 32,
                               "memory_used": 12800
                            },
                            "route_reflector_entries": {
                               "number": 4,
                               "memory_used": 320
                            },
                            "pe_distinguisher_labels": {
                               "number": 0,
                               "memory_used": 0
                            },
                            "tunnel_encap_attr": {
                               "number": 0,
                               "memory_used": 0
                            },
                            "remote_paths": {
                               "number": 20,
                               "memory_used": 1760
                            },
                            "local_prefixes": {
                               "number": 30,
                               "memory_used": 3210
                            },
                            "remote_rds": {
                               "number": 2,
                               "memory_used": 160
                            },
                            "ppmp_attr": {
                               "number": 0,
                               "memory_used": 0
                            },
                            "ribrnh_tunnel_attr": {
                               "number": 0,
                               "memory_used": 0
                            },
                            "total_prefixes": {
                               "number": 40,
                               "memory_used": 4280
                            },
                            "total_paths": {
                               "number": 50,
                               "memory_used": 4400
                            },
                            "imported_paths": {
                               "number": 25,
                               "memory_used": 2200
                            }
                        },
                        "received_notifications": 0,
                        "node": "node0_0_CPU0",
                        "default_value_for_bmp_buffer_size": 307,
                        "current_utilization_of_bmp_buffer_limit": 0,
                        "as_number": 100,
                        "as_system_number_format": "ASPLAIN",
                        "platform_rlimit_max": 2147483648,
                        "bmp_pool_summary": {
                            "8500": {
                               "free": 0,
                               "alloc": 0
                            },
                            "5500": {
                               "free": 0,
                               "alloc": 0
                            },
                            "10000": {
                               "free": 0,
                               "alloc": 0
                            },
                            "20000": {
                               "free": 0,
                               "alloc": 0
                            },
                            "900": {
                               "free": 0,
                               "alloc": 0
                            },
                            "3300": {
                               "free": 0,
                               "alloc": 0
                            },
                            "4500": {
                               "free": 0,
                               "alloc": 0
                            },
                            "400": {
                               "free": 0,
                               "alloc": 0
                            },
                            "300": {
                               "free": 0,
                               "alloc": 0
                            },
                            "600": {
                               "free": 0,
                               "alloc": 0
                            },
                            "800": {
                               "free": 0,
                               "alloc": 0
                            },
                            "200": {
                               "free": 0,
                               "alloc": 0
                            },
                            "700": {
                               "free": 0,
                               "alloc": 0
                            },
                            "500": {
                               "free": 0,
                               "alloc": 0
                            },
                            "1200": {
                               "free": 0,
                               "alloc": 0
                            },
                            "100": {
                               "free": 0,
                               "alloc": 0
                            },
                            "6500": {
                               "free": 0,
                               "alloc": 0
                            },
                            "7500": {
                               "free": 0,
                               "alloc": 0
                            },
                            "4000": {
                               "free": 0,
                               "alloc": 0
                            },
                            "2200": {
                               "free": 0,
                               "alloc": 0
                            }
                        },
                        "update_delay": 120,
                        "default_keepalive": 60,
                        "max_limit_for_bmp_buffer_size": 409,
                        "message_logging_pool_summary": {
                            "4500": {
                               "free": 0,
                               "alloc": 0
                            }
                        },
                        "vrf_info": {
                            "default": {
                               "cfg": 2,
                               "total": 1,
                               "nbrs_estab": 2
                            },
                            "non-default": {
                               "cfg": 4,
                               "total": 2,
                               "nbrs_estab": 4
                            }
                        },
                        "enforce_first_as_enabled": True,
                        "received_updates": 24,
                        "operation_mode": "STANDALONE",
                        "neighbor_logging": True,
                        "restart_count": 1,
                        "sent_updates": 14,
                        "address_family": {
                            "vpnv6 unicast": {
                               "dynamic_med_timer": "Not Running",
                               "table_version_synced_to_rib": "43",
                               "dynamic_med_periodic_timer": "Not Running",
                               "label_retention_timer_value": "5 mins",
                               "total_prefixes_scanned": "40",
                               "dynamic_med_int": "10 minutes",
                               "attribute_download": "Disabled",
                               "permanent_network": "unconfigured",
                               "rib_table_prefix_limit_reached": "no",
                               "bgp_table_version": "43",
                               "table_version_acked_by_rib": "0",
                               "prefix_scanned_per_segment": "100000",
                               "nexthop_resolution_minimum_prefix_length": "0 (not configured)",
                               "num_of_scan_segments": "1",
                               "main_table_version": "43",
                               "remote_local": {
                                    "remote prefixes": {
                                         "freed": 0,
                                         "allocated": 10
                                    }
                               },
                               "client_reflection": True,
                               "chunk_elememt_size": "3",
                               "scan_interval": "60",
                               "table_bit_field_size": "1 ",
                               "prefixes_path": {
                                    "remote prefixes": {
                                         "mem_used": 1040,
                                         "number": 10
                                    }
                               },
                               "dynamic_med": True,
                               "rib_has_not_converged": "version 0",
                               "dampening": False,
                               "thread": {
                                    "update thread": {
                                         "triggers": {
                                              "Jun 28 19:10:16.427": {
                                                   "trig_tid": 8,
                                                   "ver": 43,
                                                   "tbl_ver": 43
                                              }
                                         }
                                    },
                                    "import thread": {
                                         "triggers": {
                                              "Jun 28 19:10:16.427": {
                                                   "trig_tid": 3,
                                                   "ver": 43,
                                                   "tbl_ver": 43
                                              }
                                         }
                                    },
                                    "label thread": {
                                         "triggers": {
                                              "Jun 28 19:10:16.427": {
                                                   "trig_tid": 3,
                                                   "ver": 43,
                                                   "tbl_ver": 43
                                              }
                                         }
                                    },
                                    "rib thread": {
                                         "triggers": {
                                              "Jun 28 18:29:34.604": {
                                                   "trig_tid": 8,
                                                   "ver": 33,
                                                   "tbl_ver": 43
                                              }
                                         }
                                    }
                               },
                               "rib_table_prefix_limit_ver": "0",
                               "state": "normal mode",
                               "soft_reconfig_entries": "0"
                          },
                          "vpnv4 unicast": {
                               "dynamic_med_timer": "Not Running",
                               "table_version_synced_to_rib": "43",
                               "dynamic_med_periodic_timer": "Not Running",
                               "label_retention_timer_value": "5 mins",
                               "total_prefixes_scanned": "40",
                               "dynamic_med_int": "10 minutes",
                               "attribute_download": "Disabled",
                               "permanent_network": "unconfigured",
                               "rib_table_prefix_limit_reached": "no",
                               "bgp_table_version": "43",
                               "table_version_acked_by_rib": "0",
                               "prefix_scanned_per_segment": "100000",
                               "nexthop_resolution_minimum_prefix_length": "0 (not configured)",
                               "num_of_scan_segments": "1",
                               "main_table_version": "43",
                               "remote_local": {
                                    "remote prefixes": {
                                         "freed": 0,
                                         "allocated": 10
                                    }
                               },
                               "client_reflection": True,
                               "chunk_elememt_size": "3",
                               "scan_interval": "60",
                               "table_bit_field_size": "1 ",
                               "prefixes_path": {
                                    "remote prefixes": {
                                         "mem_used": 920,
                                         "number": 10
                                    }
                               },
                               "dynamic_med": True,
                               "rib_has_not_converged": "version 0",
                               "dampening": False,
                               "thread": {
                                    "update thread": {
                                         "triggers": {
                                              "Jun 28 19:10:16.427": {
                                                   "trig_tid": 8,
                                                   "ver": 43,
                                                   "tbl_ver": 43
                                              }
                                         }
                                    },
                                    "import thread": {
                                         "triggers": {
                                              "Jun 28 19:10:16.427": {
                                                   "trig_tid": 3,
                                                   "ver": 43,
                                                   "tbl_ver": 43
                                              }
                                         }
                                    },
                                    "label thread": {
                                         "triggers": {
                                              "Jun 28 19:10:16.427": {
                                                   "trig_tid": 3,
                                                   "ver": 43,
                                                   "tbl_ver": 43
                                              }
                                         }
                                    },
                                    "rib thread": {
                                         "triggers": {
                                              "Jun 28 18:29:29.595": {
                                                   "trig_tid": 8,
                                                   "ver": 33,
                                                   "tbl_ver": 43
                                              }
                                         }
                                    }
                               },
                               "rib_table_prefix_limit_ver": "0",
                               "state": "normal mode",
                               "soft_reconfig_entries": "0"
                          }
                        },
                        "default_local_preference": 100,
                        "pool": {
                          "20000": {
                               "free": 0,
                               "alloc": 0
                          },
                          "900": {
                               "free": 0,
                               "alloc": 0
                          },
                          "3300": {
                               "free": 0,
                               "alloc": 0
                          },
                          "4500": {
                               "free": 0,
                               "alloc": 0
                          },
                          "400": {
                               "free": 6,
                               "alloc": 6
                          },
                          "300": {
                               "free": 310,
                               "alloc": 311
                          },
                          "600": {
                               "free": 12,
                               "alloc": 12
                          },
                          "800": {
                               "free": 0,
                               "alloc": 0
                          },
                          "5000": {
                               "free": 0,
                               "alloc": 0
                          },
                          "200": {
                               "free": 0,
                               "alloc": 0
                          },
                          "700": {
                               "free": 2,
                               "alloc": 2
                          },
                          "500": {
                               "free": 20,
                               "alloc": 20
                          },
                          "1200": {
                               "free": 0,
                               "alloc": 0
                          },
                          "4000": {
                               "free": 0,
                               "alloc": 0
                          },
                          "2200": {
                               "free": 0,
                               "alloc": 0}}}}}}
    }

    golden_output = {'execute.return_value': '''
        Wed Jun 28 19:11:16.033 UTC

        BGP instance 0: 'default'
        =========================

        BGP Process Information: 
        BGP is operating in STANDALONE mode
        Autonomous System number format: ASPLAIN
        Autonomous System: 100
        Router ID: 1.1.1.1 (manually configured)
        Default Cluster ID: 1.1.1.1
        Active Cluster IDs:  1.1.1.1
        Fast external fallover enabled
        Platform RLIMIT max: 2147483648 bytes
        Maximum limit for BMP buffer size: 409 MB
        Default value for BMP buffer size: 307 MB
        Current limit for BMP buffer size: 307 MB
        Current utilization of BMP buffer limit: 0 B
        Neighbor logging is enabled
        Enforce first AS enabled
        Default local preference: 100
        Default keepalive: 60
        Non-stop routing is enabled
        Update delay: 120
        Generic scan interval: 60

        BGP Speaker process: 0, Node: node0_0_CPU0
        Restart count: 1
                                   Total           Nbrs Estab/Cfg
        Default VRFs:              1               2/2
        Non-Default VRFs:          2               4/4

                                   Sent            Received
        Updates:                   14              24              
        Notifications:             1               0               

                                   Number          Memory Used
        Attributes:                6               912             
        AS Paths:                  6               480             
        Communities:               0               0               
        Extended communities:      6               480             
        PMSI Tunnel attr:          0               0               
        RIBRNH Tunnel attr:        0               0               
        PPMP attr:                 0               0               
        Tunnel Encap attr:         0               0               
        PE distinguisher labels:   0               0               
        Route Reflector Entries:   4               320             
        Nexthop Entries:           32              12800           

                                   Alloc           Free          
        Pool 200:                  0               0             
        Pool 300:                  311             310           
        Pool 400:                  6               6             
        Pool 500:                  20              20            
        Pool 600:                  12              12            
        Pool 700:                  2               2             
        Pool 800:                  0               0             
        Pool 900:                  0               0             
        Pool 1200:                 0               0             
        Pool 2200:                 0               0             
        Pool 3300:                 0               0             
        Pool 4000:                 0               0             
        Pool 4500:                 0               0             
        Pool 5000:                 0               0             
        Pool 20000:                0               0             

        Message logging pool summary:
                                   Alloc           Free          
        Pool 100:                  19              10            
        Pool 200:                  11              1             
        Pool 500:                  19              12            
        Pool 2200:                 0               0             
        Pool 4500:                 0               0             

        BMP pool summary:
                                   Alloc           Free          
        Pool 100:                  0               0             
        Pool 200:                  0               0             
        Pool 300:                  0               0             
        Pool 400:                  0               0             
        Pool 500:                  0               0             
        Pool 600:                  0               0             
        Pool 700:                  0               0             
        Pool 800:                  0               0             
        Pool 900:                  0               0             
        Pool 1200:                 0               0             
        Pool 2200:                 0               0             
        Pool 3300:                 0               0             
        Pool 4000:                 0               0             
        Pool 4500:                 0               0             
        Pool 5500:                 0               0             
        Pool 6500:                 0               0             
        Pool 7500:                 0               0             
        Pool 8500:                 0               0             
        Pool 10000:                0               0             
        Pool 20000:                0               0             

        Address family: VPNv4 Unicast
        Dampening is not enabled
        Client reflection is enabled in global config
        Dynamic MED is Disabled
        Dynamic MED interval : 10 minutes
        Dynamic MED Timer : Not Running
        Dynamic MED Periodic Timer : Not Running
        Scan interval: 60
        Total prefixes scanned: 40
        Prefixes scanned per segment: 100000
        Number of scan segments: 1
        Nexthop resolution minimum prefix-length: 0 (not configured)
        Main Table Version: 43
        Table version synced to RIB: 43
        Table version acked by RIB: 0
        RIB has not converged: version 0
        RIB table prefix-limit reached ?  [No], version 0
        Permanent Network Unconfigured

        State: Normal mode.
        BGP Table Version: 43
        Attribute download: Disabled
        Label retention timer value 5 mins
        Soft Reconfig Entries: 0
        Table bit-field size : 1 Chunk element size : 3

                           Last 8 Triggers       Ver         Tbl Ver     Trig TID  

        Label Thread       Jun 28 19:10:16.427   43          43          3         
                           Jun 28 19:10:16.417   43          43          3         
                           Jun 28 19:09:29.680   43          43          3         
                           Jun 28 19:09:29.670   43          43          3         
                           Jun 28 18:29:34.604   43          43          3         
                           Jun 28 18:29:29.595   33          43          4         
                           Jun 28 18:29:29.595   33          38          3         
                           Jun 28 18:24:52.694   33          33          3         
                           Total triggers: 15

        Import Thread      Jun 28 19:10:16.427   43          43          3         
                           Jun 28 19:10:16.417   43          43          3         
                           Jun 28 19:09:29.680   43          43          3         
                           Jun 28 19:09:29.670   43          43          3         
                           Jun 28 18:29:34.604   43          43          3         
                           Jun 28 18:29:29.595   43          43          8         
                           Jun 28 18:29:29.595   38          43          4         
                           Jun 28 18:29:29.595   33          38          3         
                           Total triggers: 16

        RIB Thread         Jun 28 18:29:29.595   33          43          8         
                           Jun 28 18:29:29.595   33          43          4         
                           Jun 28 18:24:26.135   13          33          4         
                           Jun 28 18:24:26.135   13          33          8         
                           Jun 28 18:24:26.135   13          33          4         
                           Jun 28 18:24:21.656   11          13          4         
                           Jun 28 18:21:26.418   1           11          8         
                           Jun 28 18:21:26.418   1           11          6         
                           Total triggers: 8

        Update Thread      Jun 28 19:10:16.427   43          43          8         
                           Jun 28 19:10:16.417   43          43          8         
                           Jun 28 19:09:29.680   43          43          8         
                           Jun 28 19:09:29.670   43          43          8         
                           Jun 28 18:29:34.604   43          43          8         
                           Jun 28 18:29:29.605   43          43          18        
                           Jun 28 18:29:29.595   33          43          8         
                           Jun 28 18:24:52.694   33          33          8         
                           Total triggers: 17

                              Allocated       Freed         
        Remote Prefixes:      10              0             
        Remote Paths:         20              0             
        Remote Path-elems:    10              0             

        Local Prefixes:       30              0             
        Local Paths:          30              0             

                              Number          Mem Used      
        Remote Prefixes:      10              920           
        Remote Paths:         20              1760          
        Remote Path-elems:    10              630           
        Remote RDs:           2               160           

        Local Prefixes:       30              2850          
        Local Paths:          30              2640          
        Local RDs:            2               160           

        Total Prefixes:       40              3800          
        Total Paths:          50              4400          
        Total Path-elems:     40              4400          
        Imported Paths:       25              2200          
        Total RDs:            4               320           


        Address family: VPNv6 Unicast
        Dampening is not enabled
        Client reflection is enabled in global config
        Dynamic MED is Disabled
        Dynamic MED interval : 10 minutes
        Dynamic MED Timer : Not Running
        Dynamic MED Periodic Timer : Not Running
        Scan interval: 60
        Total prefixes scanned: 40
        Prefixes scanned per segment: 100000
        Number of scan segments: 1
        Nexthop resolution minimum prefix-length: 0 (not configured)
        Main Table Version: 43
        Table version synced to RIB: 43
        Table version acked by RIB: 0
        RIB has not converged: version 0
        RIB table prefix-limit reached ?  [No], version 0
        Permanent Network Unconfigured

        State: Normal mode.
        BGP Table Version: 43
        Attribute download: Disabled
        Label retention timer value 5 mins
        Soft Reconfig Entries: 0
        Table bit-field size : 1 Chunk element size : 3

                           Last 8 Triggers       Ver         Tbl Ver     Trig TID  

        Label Thread       Jun 28 19:10:16.427   43          43          3         
                           Jun 28 19:10:16.417   43          43          3         
                           Jun 28 19:09:29.680   43          43          3         
                           Jun 28 19:09:29.670   43          43          3         
                           Jun 28 18:29:34.604   33          43          4         
                           Jun 28 18:29:34.604   33          38          3         
                           Jun 28 18:29:29.595   33          33          3         
                           Jun 28 18:24:52.694   33          33          3         
                           Total triggers: 15

        Import Thread      Jun 28 19:10:16.427   43          43          3         
                           Jun 28 19:10:16.417   43          43          3         
                           Jun 28 19:09:29.680   43          43          3         
                           Jun 28 19:09:29.670   43          43          3         
                           Jun 28 18:29:34.604   43          43          8         
                           Jun 28 18:29:34.604   38          43          4         
                           Jun 28 18:29:34.604   33          38          3         
                           Jun 28 18:29:29.595   33          33          3         
                           Total triggers: 16

        RIB Thread         Jun 28 18:29:34.604   33          43          8         
                           Jun 28 18:29:34.604   33          43          4         
                           Jun 28 18:24:26.135   13          33          4         
                           Jun 28 18:24:26.135   13          33          4         
                           Jun 28 18:24:21.656   11          13          8         
                           Jun 28 18:21:26.428   1           11          8         
                           Jun 28 18:21:26.418   1           11          6         
                           Total triggers: 7

        Update Thread      Jun 28 19:10:16.427   43          43          8         
                           Jun 28 19:10:16.417   43          43          8         
                           Jun 28 19:09:29.680   43          43          8         
                           Jun 28 19:09:29.670   43          43          8         
                           Jun 28 18:29:34.604   43          43          19        
                           Jun 28 18:29:34.604   33          43          8         
                           Jun 28 18:29:29.595   33          33          8         
                           Jun 28 18:24:52.694   33          33          8         
                           Total triggers: 17

                              Allocated       Freed         
        Remote Prefixes:      10              0             
        Remote Paths:         20              0             
        Remote Path-elems:    10              0             

        Local Prefixes:       30              0             
        Local Paths:          30              0             

                              Number          Mem Used      
        Remote Prefixes:      10              1040          
        Remote Paths:         20              1760          
        Remote Path-elems:    10              630           
        Remote RDs:           2               160           

        Local Prefixes:       30              3210          
        Local Paths:          30              2640          
        Local RDs:            2               160           

        Total Prefixes:       40              4280          
        Total Paths:          50              4400          
        Total Path-elems:     40              4400          
        Imported Paths:       25              2200          
        Total RDs:            4               320
    '''}

    golden_parsed_output1 = {
        'instance': 
            {'default': 
                {'vrf': 
                    {'default': 
                        {'active_cluster_id': '1.1.1.1',
                        'address_family': 
                            {'vpnv4 unicast': 
                                {'attribute_download': 'Disabled',
                                'bgp_table_version': '7',
                                'chunk_elememt_size': '3',
                                'client_reflection': True,
                                'dampening': False,
                                'dynamic_med': True,
                                'dynamic_med_int': '10 '
                                              'minutes',
                                'dynamic_med_periodic_timer': 'Not '
                                                         'Running',
                                'dynamic_med_timer': 'Not '
                                                'Running',
                                'label_retention_timer_value': '5 '
                                                          'mins',
                                'main_table_version': '7',
                                'nexthop_resolution_minimum_prefix_length': '0 '
                                                                       '(not '
                                                                       'configured)',
                                'num_of_scan_segments': '1',
                                'permanent_network': 'unconfigured',
                                'prefix_scanned_per_segment': '100000',
                                'prefixes_path': {'remote prefixes': {'mem_used': 0,
                                                                 'number': 0}},
                                'remote_local': {'remote prefixes': {'allocated': 0,
                                                                'freed': 0}},
                                'rib_has_not_converged': 'version '
                                                    '0',
                                'rib_table_prefix_limit_reached': 'no',
                                'rib_table_prefix_limit_ver': '0',
                                'scan_interval': '60',
                                'soft_reconfig_entries': '0',
                                'state': 'normal '
                                    'mode',
                                'table_bit_field_size': '1 ',
                                'table_version_acked_by_rib': '0',
                                'table_version_synced_to_rib': '7',
                                'total_prefixes_scanned': '0'},
                            'vpnv6 unicast': 
                                {'attribute_download': 'Disabled',
                                'bgp_table_version': '7',
                                'chunk_elememt_size': '3',
                                'client_reflection': True,
                                'dampening': False,
                                'dynamic_med': True,
                                'dynamic_med_int': '10 '
                                                  'minutes',
                                'dynamic_med_periodic_timer': 'Not '
                                                             'Running',
                                'dynamic_med_timer': 'Not '
                                                    'Running',
                                'label_retention_timer_value': '5 '
                                                              'mins',
                                'main_table_version': '7',
                                'nexthop_resolution_minimum_prefix_length': '0 '
                                                                           '(not '
                                                                           'configured)',
                                'num_of_scan_segments': '1',
                                'permanent_network': 'unconfigured',
                                'prefix_scanned_per_segment': '100000',
                                'prefixes_path': {'remote prefixes': {'mem_used': 0,
                                                                     'number': 0}},
                                'remote_local': {'remote prefixes': {'allocated': 0,
                                                                    'freed': 0}},
                                'rib_has_not_converged': 'version '
                                                        '0',
                                'rib_table_prefix_limit_reached': 'no',
                                'rib_table_prefix_limit_ver': '0',
                                'scan_interval': '60',
                                'soft_reconfig_entries': '0',
                                'state': 'normal '
                                        'mode',
                                'table_bit_field_size': '1 ',
                                'table_version_acked_by_rib': '0',
                                'table_version_synced_to_rib': '7',
                                'total_prefixes_scanned': '0'}},
                        'as_number': 100,
                        'as_system_number_format': 'ASPLAIN',
                        'att': 
                            {'as_paths': {'memory_used': 0,
                                           'number': 0},
                              'attributes': {'memory_used': 0,
                                             'number': 0},
                              'communities': {'memory_used': 0,
                                              'number': 0},
                              'extended_communities': {'memory_used': 0,
                                                       'number': 0},
                              'imported_paths': {'memory_used': 0,
                                                 'number': 0},
                              'large_communities': {'memory_used': 0,
                                                    'number': 0},
                              'local_paths': {'memory_used': 0,
                                              'number': 0},
                              'local_prefixes': {'memory_used': 0,
                                                 'number': 0},
                              'local_rds': {'memory_used': 160,
                                            'number': 2},
                              'nexthop_entries': {'memory_used': 10400,
                                                  'number': 26},
                              'pe_distinguisher_labels': {'memory_used': 0,
                                                          'number': 0},
                              'pmsi_tunnel_attr': {'memory_used': 0,
                                                   'number': 0},
                              'ppmp_attr': {'memory_used': 0,
                                            'number': 0},
                              'remote_paths': {'memory_used': 0,
                                               'number': 0},
                              'remote_rds': {'memory_used': 0,
                                             'number': 0},
                              'ribrnh_tunnel_attr': {'memory_used': 0,
                                                     'number': 0},
                              'route_reflector_entries': {'memory_used': 0,
                                                          'number': 0},
                              'total_paths': {'memory_used': 0,
                                              'number': 0},
                              'total_prefixes': {'memory_used': 0,
                                                 'number': 0},
                              'total_rds': {'memory_used': 160,
                                            'number': 2},
                              'tunnel_encap_attr': {'memory_used': 0,
                                                    'number': 0}},
                        'bgp_speaker_process': 0,
                        'bmp_pool_summary': {'100': {'alloc': 0,
                                                   'free': 0},
                                           '10000': {'alloc': 0,
                                                     'free': 0},
                                           '1200': {'alloc': 0,
                                                    'free': 0},
                                           '200': {'alloc': 0,
                                                   'free': 0},
                                           '20000': {'alloc': 0,
                                                     'free': 0},
                                           '2200': {'alloc': 0,
                                                    'free': 0},
                                           '300': {'alloc': 0,
                                                   'free': 0},
                                           '3300': {'alloc': 0,
                                                    'free': 0},
                                           '400': {'alloc': 0,
                                                   'free': 0},
                                           '4000': {'alloc': 0,
                                                    'free': 0},
                                           '4500': {'alloc': 0,
                                                    'free': 0},
                                           '500': {'alloc': 0,
                                                   'free': 0},
                                           '5500': {'alloc': 0,
                                                    'free': 0},
                                           '600': {'alloc': 0,
                                                   'free': 0},
                                           '6500': {'alloc': 0,
                                                    'free': 0},
                                           '700': {'alloc': 0,
                                                   'free': 0},
                                           '7500': {'alloc': 0,
                                                    'free': 0},
                                           '800': {'alloc': 0,
                                                   'free': 0},
                                           '8500': {'alloc': 0,
                                                    'free': 0},
                                           '900': {'alloc': 0,
                                                   'free': 0}},
                        'current_limit_for_bmp_buffer_size': 326,
                        'current_utilization_of_bmp_buffer_limit': 0,
                        'default_cluster_id': '1.1.1.1',
                        'default_keepalive': 60,
                        'default_local_preference': 100,
                        'default_value_for_bmp_buffer_size': 326,
                        'enforce_first_as_enabled': True,
                        'fast_external_fallover': True,
                        'generic_scan_interval': 60,
                        'max_limit_for_bmp_buffer_size': 435,
                        'message_logging_pool_summary': {'4500': {'alloc': 0,
                                                                'free': 0}},
                        'neighbor_logging': True,
                        'node': 'node0_RSP1_CPU0',
                        'non_stop_routing': True,
                        'operation_mode': 'STANDALONE',
                        'platform_rlimit_max': 2281701376,
                        'pool': {'1200': {'alloc': 0,
                                        'free': 0},
                               '200': {'alloc': 0,
                                       'free': 0},
                               '20000': {'alloc': 0,
                                         'free': 0},
                               '2200': {'alloc': 0,
                                        'free': 0},
                               '300': {'alloc': 1,
                                       'free': 0},
                               '3300': {'alloc': 0,
                                        'free': 0},
                               '400': {'alloc': 0,
                                       'free': 0},
                               '4000': {'alloc': 0,
                                        'free': 0},
                               '4500': {'alloc': 0,
                                        'free': 0},
                               '500': {'alloc': 0,
                                       'free': 0},
                               '5000': {'alloc': 0,
                                        'free': 0},
                               '600': {'alloc': 0,
                                       'free': 0},
                               '700': {'alloc': 0,
                                       'free': 0},
                               '800': {'alloc': 0,
                                       'free': 0},
                               '900': {'alloc': 0,
                                       'free': 0}},
                        'received_notifications': 0,
                        'received_updates': 0,
                        'restart_count': 1,
                        'router_id': '1.1.1.1',
                        'sent_notifications': 0,
                        'sent_updates': 0,
                        'update_delay': 120,
                        'vrf_info': {'default': {'cfg': 2,
                                               'nbrs_estab': 0,
                                               'total': 1},
                                   'non-default': {'cfg': 4,
                                                   'nbrs_estab': 0,
                                                   'total': 2}}}}},
            'test': 
                {'vrf': 
                    {'default': {}}},
            'test1': 
                {'vrf': 
                    {'default': {}}},
            'test2': 
                {'vrf': 
                    {'default': {}}}}}

    golden_output1 = {'execute.return_value': '''
        BGP instance 0: 'default'
        =========================

        BGP Process Information: 
        BGP is operating in STANDALONE mode
        Autonomous System number format: ASPLAIN
        Autonomous System: 100
        Router ID: 1.1.1.1 (manually configured)
        Default Cluster ID: 1.1.1.1
        Active Cluster IDs:  1.1.1.1
        Fast external fallover enabled
        Platform RLIMIT max: 2281701376 bytes
        Maximum limit for BMP buffer size: 435 MB
        Default value for BMP buffer size: 326 MB
        Current limit for BMP buffer size: 326 MB
        Current utilization of BMP buffer limit: 0 B
        Neighbor logging is enabled
        Enforce first AS enabled
        Default local preference: 100
        Default keepalive: 60
        Non-stop routing is enabled
        Update delay: 120
        Generic scan interval: 60

        BGP Speaker process: 0, Node: node0_RSP1_CPU0
        Restart count: 1
                                   Total           Nbrs Estab/Cfg
        Default VRFs:              1               0/2
        Non-Default VRFs:          2               0/4

                                   Sent            Received
        Updates:                   0               0               
        Notifications:             0               0               

                                   Number          Memory Used
        Attributes:                0               0               
        AS Paths:                  0               0               
        Communities:               0               0               
        Large Communities:         0               0               
        Extended communities:      0               0               
        PMSI Tunnel attr:          0               0               
        RIBRNH Tunnel attr:        0               0               
        PPMP attr:                 0               0               
        Tunnel Encap attr:         0               0               
        PE distinguisher labels:   0               0               
        Route Reflector Entries:   0               0               
        Nexthop Entries:           26              10400           

                                   Alloc           Free          
        Pool 200:                  0               0             
        Pool 300:                  1               0             
        Pool 400:                  0               0             
        Pool 500:                  0               0             
        Pool 600:                  0               0             
        Pool 700:                  0               0             
        Pool 800:                  0               0             
        Pool 900:                  0               0             
        Pool 1200:                 0               0             
        Pool 2200:                 0               0             
        Pool 3300:                 0               0             
        Pool 4000:                 0               0             
        Pool 4500:                 0               0             
        Pool 5000:                 0               0             
        Pool 20000:                0               0             

        Message logging pool summary:
                                   Alloc           Free          
        Pool 100:                  0               0             
        Pool 200:                  0               0             
        Pool 500:                  0               0             
        Pool 2200:                 0               0             
        Pool 4500:                 0               0             

        BMP pool summary:
                                   Alloc           Free          
        Pool 100:                  0               0             
        Pool 200:                  0               0             
        Pool 300:                  0               0             
        Pool 400:                  0               0             
        Pool 500:                  0               0             
        Pool 600:                  0               0             
        Pool 700:                  0               0             
        Pool 800:                  0               0             
        Pool 900:                  0               0             
        Pool 1200:                 0               0             
        Pool 2200:                 0               0             
        Pool 3300:                 0               0             
        Pool 4000:                 0               0             
        Pool 4500:                 0               0             
        Pool 5500:                 0               0             
        Pool 6500:                 0               0             
        Pool 7500:                 0               0             
        Pool 8500:                 0               0             
        Pool 10000:                0               0             
        Pool 20000:                0               0             

        Address family: VPNv4 Unicast
        Dampening is not enabled
        Client reflection is enabled in global config
        Dynamic MED is Disabled
        Dynamic MED interval : 10 minutes
        Dynamic MED Timer : Not Running
        Dynamic MED Periodic Timer : Not Running
        Scan interval: 60
        Total prefixes scanned: 0
        Prefixes scanned per segment: 100000
        Number of scan segments: 1
        Nexthop resolution minimum prefix-length: 0 (not configured)
        Main Table Version: 7
        Table version synced to RIB: 7
        Table version acked by RIB: 0
        RIB has not converged: version 0
        RIB table prefix-limit reached ?  [No], version 0
        Permanent Network Unconfigured

        State: Normal mode.
        BGP Table Version: 7
        Attribute download: Disabled
        Label retention timer value 5 mins
        Soft Reconfig Entries: 0
        Table bit-field size : 1 Chunk element size : 3
        Maximum supported label-stack depth:
           For IPv4 Nexthop: 0
           For IPv6 Nexthop: 0

                           Last 8 Triggers       Ver         Tbl Ver     Trig TID  

        Label Thread       Jul  6 11:42:04.367   7           7           3         
                           Jul  6 11:42:01.371   5           6           9         
                           Jul  6 11:42:01.370   5           5           18        
                           Jul  6 11:42:01.367   0           5           4         
                           Total triggers: 4

        Import Thread      Jul  6 11:42:04.367   7           7           3         
                           Jul  6 11:42:01.371   5           6           9         
                           Jul  6 11:42:01.370   5           5           18        
                           Jul  6 11:42:01.366   0           5           18        
                           Total triggers: 4

        RIB Thread         Jul  6 11:42:01.371   5           7           8         
                           Jul  6 11:42:01.370   5           5           8         
                           Jul  6 11:42:01.367   1           5           8         
                           Jul  6 11:42:01.366   1           5           6         
                           Total triggers: 4

        Update Thread      Jul  6 11:42:04.367   7           7           8         
                           Jul  6 11:42:01.371   7           7           18        
                           Jul  6 11:42:01.371   5           7           9         
                           Jul  6 11:42:01.370   5           5           8         
                           Jul  6 11:42:01.370   5           5           18        
                           Total triggers: 5

                              Allocated       Freed         
        Remote Prefixes:      0               0             
        Remote Paths:         0               0             
        Remote Path-elems:    0               0             

        Local Prefixes:       0               0             
        Local Paths:          0               0             

                              Number          Mem Used      
        Remote Prefixes:      0               0             
        Remote Paths:         0               0             
        Remote Path-elems:    0               0             
        Remote RDs:           0               0             

        Local Prefixes:       0               0             
        Local Paths:          0               0             
        Local RDs:            2               160           

        Total Prefixes:       0               0             
        Total Paths:          0               0             
        Total Path-elems:     0               0             
        Imported Paths:       0               0             
        Total RDs:            2               160           


        Address family: VPNv6 Unicast
        Dampening is not enabled
        Client reflection is enabled in global config
        Dynamic MED is Disabled
        Dynamic MED interval : 10 minutes
        Dynamic MED Timer : Not Running
        Dynamic MED Periodic Timer : Not Running
        Scan interval: 60
        Total prefixes scanned: 0
        Prefixes scanned per segment: 100000
        Number of scan segments: 1
        Nexthop resolution minimum prefix-length: 0 (not configured)
        Main Table Version: 7
        Table version synced to RIB: 7
        Table version acked by RIB: 0
        RIB has not converged: version 0
        RIB table prefix-limit reached ?  [No], version 0
        Permanent Network Unconfigured

        State: Normal mode.
        BGP Table Version: 7
        Attribute download: Disabled
        Label retention timer value 5 mins
        Soft Reconfig Entries: 0
        Table bit-field size : 1 Chunk element size : 3
        Maximum supported label-stack depth:
           For IPv4 Nexthop: 0
           For IPv6 Nexthop: 0

                           Last 8 Triggers       Ver         Tbl Ver     Trig TID  

        Label Thread       Jul  6 11:42:04.367   7           7           3         
                           Jul  6 11:42:01.373   5           6           9         
                           Jul  6 11:42:01.371   5           5           19        
                           Jul  6 11:42:01.367   0           5           4         
                           Total triggers: 4

        Import Thread      Jul  6 11:42:04.367   7           7           3         
                           Jul  6 11:42:01.373   5           6           9         
                           Jul  6 11:42:01.371   5           5           19        
                           Jul  6 11:42:01.367   0           5           19        
                           Total triggers: 4

        RIB Thread         Jul  6 11:42:01.373   5           7           4         
                           Jul  6 11:42:01.371   5           5           8         
                           Jul  6 11:42:01.367   1           5           8         
                           Jul  6 11:42:01.367   1           5           6         
                           Total triggers: 4

        Update Thread      Jul  6 11:42:04.367   7           7           8         
                           Jul  6 11:42:01.373   7           7           19        
                           Jul  6 11:42:01.373   5           7           8         
                           Jul  6 11:42:01.373   5           7           9         
                           Jul  6 11:42:01.371   5           5           8         
                           Jul  6 11:42:01.371   5           5           19        
                           Total triggers: 6

                              Allocated       Freed         
        Remote Prefixes:      0               0             
        Remote Paths:         0               0             
        Remote Path-elems:    0               0             

        Local Prefixes:       0               0             
        Local Paths:          0               0             

                              Number          Mem Used      
        Remote Prefixes:      0               0             
        Remote Paths:         0               0             
        Remote Path-elems:    0               0             
        Remote RDs:           0               0             

        Local Prefixes:       0               0             
        Local Paths:          0               0             
        Local RDs:            2               160           

        Total Prefixes:       0               0             
        Total Paths:          0               0             
        Total Path-elems:     0               0             
        Imported Paths:       0               0             
        Total RDs:            2               160           



        BGP instance 1: 'test'
        ======================
        % None of the requested address families are configured for instance 'test'(29193)

        BGP instance 2: 'test1'
        =======================
        % None of the requested address families are configured for instance 'test1'(29193)

        BGP instance 3: 'test2'
        =======================
        % None of the requested address families are configured for instance 'test2'(29193)
        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpInstanceProcessDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf_type='all')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpInstanceProcessDetail(device=self.device)
        parsed_output = obj.parse(vrf_type='all')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowBgpInstanceProcessDetail(device=self.device)
        parsed_output = obj.parse(vrf_type='all')
        self.assertEqual(parsed_output,self.golden_parsed_output1)

# ==============================================================
# Unit test for 'show bgp instance all all all neighbors detail'
# ==============================================================

class test_show_bgp_instance_all_all_all_neighbors_detail(unittest.TestCase):

    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "instance": {
          "default": {
               "vrf": {
                    "default": {
                         "neighbor": {
                              "2.2.2.2": {
                                   "link_state": "internal link",
                                   "last_ka_expiry_before_second_last": "00:00:00",
                                   "inbound_message": "3",
                                   "bgp_session_transport": {
                                        "connection": {
                                             "last_reset": "00:00:00",
                                             "state": "established",
                                             "connections_established": 1,
                                             "connections_dropped": 0
                                        },
                                        "transport": {
                                             "local_host": "1.1.1.1",
                                             "if_handle": "0x00000000",
                                             "foreign_port": "179",
                                             "foreign_host": "2.2.2.2",
                                             "local_port": "46663"
                                        }
                                   },
                                   "last_ka_error_ka_not_sent": "00:00:00",
                                   "min_acceptable_hold_time": 3,
                                   "router_id": "2.2.2.2",
                                   "last_write_written": 0,
                                   "second_last_write_before_attempted": 0,
                                   "last_ka_start_before_second_last": "00:00:00",
                                   "remote_as": 100,
                                   "bgp_negotiated_keepalive_timers": {
                                        "keepalive_interval": 60,
                                        "hold_time": 180
                                   },
                                   "last_write_pulse_rcvd": "Jun 28 19:03:35.294 ",
                                   "written": 19,
                                   "message_stats_output_queue": 0,
                                   "second_attempted": 19,
                                   "message_stats_input_queue": 0,
                                   "last_ka_expiry_before_reset": "00:00:00",
                                   "last_write_pulse_rcvd_before_reset": "00:00:00",
                                   "second_written": 19,
                                   "last_write_before_reset": "00:00:00",
                                   "attempted": 19,
                                   "second_last_write": "00:01:23",
                                   "last_ka_error_before_reset": "00:00:00",
                                   "bgp_neighbor_counters": {
                                        "messages": {
                                             "sent": {
                                                  "keepalives": 43,
                                                  "opens": 1,
                                                  "updates": 4,
                                                  "notifications": 0,
                                             },
                                             "received": {
                                                  "keepalives": 44,
                                                  "opens": 1,
                                                  "updates": 6,
                                                  "notifications": 0,
                                             }
                                        }
                                   },
                                   "last_write_thread_event_before_reset": "00:00:00",
                                   "last_write_attempted": 0,
                                   "precedence": "internet",
                                   "configured_hold_time": 180,
                                   "keepalive": 60,
                                   "local_as_as_no": 100,
                                   "last_read": "00:00:32",
                                   "second_last_write_before_written": 0,
                                   "minimum_time_between_adv_runs": 0,
                                   "multiprotocol_capability": "received",
                                   "address_family": {
                                        "vpnv4 unicast": {
                                             "last_synced_ack_version": 0,
                                             "last_ack_version": 43,
                                             "cummulative_no_prefixes_denied": 0,
                                             "refresh_request_status": "No Refresh request being processed",
                                             "prefix_suppressed": 0,
                                             "route_refresh_request_received": 0,
                                             "maximum_prefixes_allowed": 2097152,
                                             "neighbor_version": 43,
                                             "maximum_prefix_restart": 0,
                                             "eor_status": "was received during read-only mode",
                                             "best_paths": 10,
                                             "outstanding_version_objects_max": 1,
                                             "exact_no_prefixes_denied": 0,
                                             "prefix_withdrawn": 0,
                                             "outstanding_version_objects_current": 0,
                                             "route_refresh_request_sent": 0,
                                             "accepted_prefixes": 10,
                                             "maximum_prefix_threshold": "75%",
                                             "filter_group": "0.2",
                                             "maximum_prefix_warning_only": True,
                                             "update_group": "0.2",
                                             "additional_paths_operation": "None",
                                             "prefix_advertised": 5
                                        },
                                        "vpnv6 unicast": {
                                             "last_synced_ack_version": 0,
                                             "last_ack_version": 43,
                                             "cummulative_no_prefixes_denied": 0,
                                             "refresh_request_status": "No Refresh request being processed",
                                             "prefix_suppressed": 0,
                                             "route_refresh_request_received": 0,
                                             "maximum_prefixes_allowed": 1048576,
                                             "neighbor_version": 43,
                                             "maximum_prefix_restart": 0,
                                             "eor_status": "was received during read-only mode",
                                             "best_paths": 10,
                                             "outstanding_version_objects_max": 1,
                                             "exact_no_prefixes_denied": 0,
                                             "prefix_withdrawn": 0,
                                             "outstanding_version_objects_current": 0,
                                             "route_refresh_request_sent": 0,
                                             "accepted_prefixes": 10,
                                             "maximum_prefix_threshold": "75%",
                                             "filter_group": "0.2",
                                             "maximum_prefix_warning_only": True,
                                             "update_group": "0.2",
                                             "additional_paths_operation": "None",
                                             "prefix_advertised": 5
                                        }
                                   },
                                   "non_stop_routing": "enabled",
                                   "last_write": "00:00:23",
                                   "nsr_state": "None",
                                   "tcp_initial_sync_done": "---",
                                   "last_full_not_set_pulse_count": 93,
                                   "tcp_initial_sync": "---",
                                   "outbound_message": "3",
                                   "bgp_negotiated_capabilities": {
                                        "four_octets_asn": "advertised received",
                                        "vpnv6_unicast": "advertised received",
                                        "route_refresh": "advertised received",
                                        "vpnv4_unicast": "advertised received"
                                   },
                                   "last_write_thread_event_second_last": "00:00:00",
                                   "second_last_write_before_reset": "00:00:00",
                                   "last_ka_start_before_reset": "00:00:00",
                                   "last_read_before_reset": "00:00:00",
                                   "session_state": "established",
                                   "up_time": "00:42:33",
                              },
                              "3.3.3.3": {
                                   "link_state": "internal link",
                                   "last_ka_expiry_before_second_last": "00:00:00",
                                   "inbound_message": "3",
                                   "bgp_session_transport": {
                                        "connection": {
                                             "last_reset": "00:00:00",
                                             "state": "established",
                                             "connections_established": 1,
                                             "connections_dropped": 0
                                        },
                                        "transport": {
                                             "local_host": "1.1.1.1",
                                             "if_handle": "0x00000000",
                                             "foreign_port": "179",
                                             "foreign_host": "3.3.3.3",
                                             "local_port": "54707",
                                        }
                                   },
                                   "last_ka_error_ka_not_sent": "00:00:00",
                                   "min_acceptable_hold_time": 3,
                                   "router_id": "3.3.3.3",
                                   "last_write_written": 0,
                                   "second_last_write_before_attempted": 0,
                                   "last_ka_start_before_second_last": "00:00:00",
                                   "remote_as": 100,
                                   "bgp_negotiated_keepalive_timers": {
                                        "keepalive_interval": 60,
                                        "hold_time": 180
                                   },
                                   "last_write_pulse_rcvd": "Jun 28 19:03:52.763 ",
                                   "written": 19,
                                   "message_stats_output_queue": 0,
                                   "second_attempted": 19,
                                   "message_stats_input_queue": 0,
                                   "last_ka_expiry_before_reset": "00:00:00",
                                   "last_write_pulse_rcvd_before_reset": "00:00:00",
                                   "second_written": 19,
                                   "last_write_before_reset": "00:00:00",
                                   "attempted": 19,
                                   "second_last_write": "00:01:23",
                                   "last_ka_error_before_reset": "00:00:00",
                                   "bgp_neighbor_counters": {
                                        "messages": {
                                             "sent": {
                                                  "keepalives": 40,
                                                  "opens": 1,
                                                  "updates": 4,
                                                  "notifications": 0,
                                             },
                                             "received": {
                                                  "keepalives": 41,
                                                  "opens": 1,
                                                  "updates": 6,
                                                  "notifications": 0,
                                             }
                                        }
                                   },
                                   "last_write_thread_event_before_reset": "00:00:00",
                                   "last_write_attempted": 0,
                                   "precedence": "internet",
                                   "configured_hold_time": 180,
                                   "keepalive": 60,
                                   "local_as_as_no": 100,
                                   "last_read": "00:00:06",
                                   "second_last_write_before_written": 0,
                                   "minimum_time_between_adv_runs": 0,
                                   "multiprotocol_capability": "received",
                                   "address_family": {
                                        "vpnv4 unicast": {
                                             "last_synced_ack_version": 0,
                                             "last_ack_version": 43,
                                             "cummulative_no_prefixes_denied": 0,
                                             "refresh_request_status": "No Refresh request being processed",
                                             "prefix_suppressed": 0,
                                             "route_refresh_request_received": 0,
                                             "maximum_prefixes_allowed": 2097152,
                                             "neighbor_version": 43,
                                             "maximum_prefix_restart": 0,
                                             "eor_status": "was not received during read-only mode",
                                             "best_paths": 0,
                                             "outstanding_version_objects_max": 1,
                                             "exact_no_prefixes_denied": 0,
                                             "prefix_withdrawn": 0,
                                             "outstanding_version_objects_current": 0,
                                             "route_refresh_request_sent": 0,
                                             "accepted_prefixes": 10,
                                             "maximum_prefix_threshold": "75%",
                                             "filter_group": "0.2",
                                             "maximum_prefix_warning_only": True,
                                             "update_group": "0.2",
                                             "additional_paths_operation": "None",
                                             "prefix_advertised": 5
                                        },
                                        "vpnv6 unicast": {
                                             "last_synced_ack_version": 0,
                                             "last_ack_version": 43,
                                             "cummulative_no_prefixes_denied": 0,
                                             "refresh_request_status": "No Refresh request being processed",
                                             "prefix_suppressed": 0,
                                             "route_refresh_request_received": 0,
                                             "maximum_prefixes_allowed": 1048576,
                                             "neighbor_version": 43,
                                             "maximum_prefix_restart": 0,
                                             "eor_status": "was not received during read-only mode",
                                             "best_paths": 0,
                                             "outstanding_version_objects_max": 1,
                                             "exact_no_prefixes_denied": 0,
                                             "prefix_withdrawn": 0,
                                             "outstanding_version_objects_current": 0,
                                             "route_refresh_request_sent": 0,
                                             "accepted_prefixes": 10,
                                             "maximum_prefix_threshold": "75%",
                                             "filter_group": "0.2",
                                             "maximum_prefix_warning_only": True,
                                             "update_group": "0.2",
                                             "additional_paths_operation": "None",
                                             "prefix_advertised": 5
                                        }
                                   },
                                   "non_stop_routing": "enabled",
                                   "last_write": "00:00:23",
                                   "nsr_state": "None",
                                   "tcp_initial_sync_done": "---",
                                   "last_full_not_set_pulse_count": 88,
                                   "tcp_initial_sync": "---",
                                   "outbound_message": "3",
                                   "bgp_negotiated_capabilities": {
                                        "four_octets_asn": "advertised received",
                                        "vpnv6_unicast": "advertised received",
                                        "route_refresh": "advertised received",
                                        "vpnv4_unicast": "advertised received"
                                   },
                                   "last_write_thread_event_second_last": "00:00:00",
                                   "second_last_write_before_reset": "00:00:00",
                                   "last_ka_start_before_reset": "00:00:00",
                                   "last_read_before_reset": "00:00:00",
                                   "session_state": "established",
                                   "up_time": "00:39:07",
                                }
                            }
                        }
                    }
                }
            }
        }

    golden_output = {'execute.return_value': '''
           
        BGP instance 0: 'default'
        =========================

        BGP neighbor is 2.2.2.2
         Remote AS 100, local AS 100, internal link
         Remote router ID 2.2.2.2
          BGP state = Established, up for 00:42:33
          NSR State: None
          Last read 00:00:32, Last read before reset 00:00:00
          Hold time is 180, keepalive interval is 60 seconds
          Configured hold time: 180, keepalive: 60, min acceptable hold time: 3
          Last write 00:00:23, attempted 19, written 19
          Second last write 00:01:23, attempted 19, written 19
          Last write before reset 00:00:00, attempted 0, written 0
          Second last write before reset 00:00:00, attempted 0, written 0
          Last write pulse rcvd  Jun 28 19:03:35.294 last full not set pulse count 93
          Last write pulse rcvd before reset 00:00:00
          Socket not armed for io, armed for read, armed for write
          Last write thread event before reset 00:00:00, second last 00:00:00
          Last KA expiry before reset 00:00:00, second last 00:00:00
          Last KA error before reset 00:00:00, KA not sent 00:00:00
          Last KA start before reset 00:00:00, second last 00:00:00
          Precedence: internet
          Non-stop routing is enabled
          Entered Neighbor NSR TCP mode:
            TCP Initial Sync :              ---                
            TCP Initial Sync Phase Two :    ---                
            TCP Initial Sync Done :         ---                
          Multi-protocol capability received
          Neighbor capabilities:            Adv         Rcvd
            Route refresh:                  Yes         Yes
            4-byte AS:                      Yes         Yes
            Address family VPNv4 Unicast:   Yes         Yes
            Address family VPNv6 Unicast:   Yes         Yes
          Message stats:
            InQ depth: 0, OutQ depth: 0
                            Last_Sent               Sent  Last_Rcvd               Rcvd
            Open:           Jun 28 18:21:24.198        1  Jun 28 18:21:24.208        1
            Notification:   ---                        0  ---                        0
            Update:         Jun 28 18:29:34.624        4  Jun 28 18:21:26.218        6
            Keepalive:      Jun 28 19:03:35.164       43  Jun 28 19:03:26.445       44
            Route_Refresh:  ---                        0  ---                        0
            Total:                                    48                            51
          Minimum time between advertisement runs is 0 secs
          Inbound message logging enabled, 3 messages buffered
          Outbound message logging enabled, 3 messages buffered

         For Address Family: VPNv4 Unicast
          BGP neighbor version 43
          Update group: 0.2 Filter-group: 0.2  No Refresh request being processed
            Graceful Restart capability received
              Remote Restart time is 120 seconds
              Neighbor did not preserve the forwarding state during latest restart
          Route refresh request: received 0, sent 0
          10 accepted prefixes, 10 are bestpaths
          Exact no. of prefixes denied : 0.
          Cumulative no. of prefixes denied: 0. 
          Prefix advertised 5, suppressed 0, withdrawn 0
          Maximum prefixes allowed 2097152
          Threshold for warning message 75%, restart interval 0 min
          AIGP is enabled
          An EoR was received during read-only mode
          Last ack version 43, Last synced ack version 0
          Outstanding version objects: current 0, max 1
          Additional-paths operation: None
          Send Multicast Attributes

         For Address Family: VPNv6 Unicast
          BGP neighbor version 43
          Update group: 0.2 Filter-group: 0.2  No Refresh request being processed
            Graceful Restart capability received
              Remote Restart time is 120 seconds
              Neighbor did not preserve the forwarding state during latest restart
          Route refresh request: received 0, sent 0
          10 accepted prefixes, 10 are bestpaths
          Exact no. of prefixes denied : 0.
          Cumulative no. of prefixes denied: 0. 
          Prefix advertised 5, suppressed 0, withdrawn 0
          Maximum prefixes allowed 1048576
          Threshold for warning message 75%, restart interval 0 min
          AIGP is enabled
          An EoR was received during read-only mode
          Last ack version 43, Last synced ack version 0
          Outstanding version objects: current 0, max 1
          Additional-paths operation: None
          Send Multicast Attributes

          Connections established 1; dropped 0
          Local host: 1.1.1.1, Local port: 46663, IF Handle: 0x00000000
          Foreign host: 2.2.2.2, Foreign port: 179
          Last reset 00:00:00

        BGP neighbor is 3.3.3.3
         Remote AS 100, local AS 100, internal link
         Remote router ID 3.3.3.3
          BGP state = Established, up for 00:39:07
          NSR State: None
          Last read 00:00:06, Last read before reset 00:00:00
          Hold time is 180, keepalive interval is 60 seconds
          Configured hold time: 180, keepalive: 60, min acceptable hold time: 3
          Last write 00:00:23, attempted 19, written 19
          Second last write 00:01:23, attempted 19, written 19
          Last write before reset 00:00:00, attempted 0, written 0
          Second last write before reset 00:00:00, attempted 0, written 0
          Last write pulse rcvd  Jun 28 19:03:52.763 last full not set pulse count 88
          Last write pulse rcvd before reset 00:00:00
          Socket not armed for io, armed for read, armed for write
          Last write thread event before reset 00:00:00, second last 00:00:00
          Last KA expiry before reset 00:00:00, second last 00:00:00
          Last KA error before reset 00:00:00, KA not sent 00:00:00
          Last KA start before reset 00:00:00, second last 00:00:00
          Precedence: internet
          Non-stop routing is enabled
          Entered Neighbor NSR TCP mode:
            TCP Initial Sync :              ---                
            TCP Initial Sync Phase Two :    ---                
            TCP Initial Sync Done :         ---                
          Multi-protocol capability received
          Neighbor capabilities:            Adv         Rcvd
            Route refresh:                  Yes         Yes
            4-byte AS:                      Yes         Yes
            Address family VPNv4 Unicast:   Yes         Yes
            Address family VPNv6 Unicast:   Yes         Yes
          Message stats:
            InQ depth: 0, OutQ depth: 0
                            Last_Sent               Sent  Last_Rcvd               Rcvd
            Open:           Jun 28 18:24:51.194        1  Jun 28 18:24:51.204        1
            Notification:   ---                        0  ---                        0
            Update:         Jun 28 18:29:34.624        4  Jun 28 18:24:52.664        6
            Keepalive:      Jun 28 19:03:35.164       40  Jun 28 19:03:52.763       41
            Route_Refresh:  ---                        0  ---                        0
            Total:                                    45                            48
          Minimum time between advertisement runs is 0 secs
          Inbound message logging enabled, 3 messages buffered
          Outbound message logging enabled, 3 messages buffered

         For Address Family: VPNv4 Unicast
          BGP neighbor version 43
          Update group: 0.2 Filter-group: 0.2  No Refresh request being processed
            Graceful Restart capability received
              Remote Restart time is 120 seconds
              Neighbor did not preserve the forwarding state during latest restart
          Route refresh request: received 0, sent 0
          10 accepted prefixes, 0 are bestpaths
          Exact no. of prefixes denied : 0.
          Cumulative no. of prefixes denied: 0. 
          Prefix advertised 5, suppressed 0, withdrawn 0
          Maximum prefixes allowed 2097152
          Threshold for warning message 75%, restart interval 0 min
          AIGP is enabled
          An EoR was not received during read-only mode
          Last ack version 43, Last synced ack version 0
          Outstanding version objects: current 0, max 1
          Additional-paths operation: None
          Send Multicast Attributes

         For Address Family: VPNv6 Unicast
          BGP neighbor version 43
          Update group: 0.2 Filter-group: 0.2  No Refresh request being processed
            Graceful Restart capability received
              Remote Restart time is 120 seconds
              Neighbor did not preserve the forwarding state during latest restart
          Route refresh request: received 0, sent 0
          10 accepted prefixes, 0 are bestpaths
          Exact no. of prefixes denied : 0.
          Cumulative no. of prefixes denied: 0. 
          Prefix advertised 5, suppressed 0, withdrawn 0
          Maximum prefixes allowed 1048576
          Threshold for warning message 75%, restart interval 0 min
          AIGP is enabled
          An EoR was not received during read-only mode
          Last ack version 43, Last synced ack version 0
          Outstanding version objects: current 0, max 1
          Additional-paths operation: None
          Send Multicast Attributes

          Connections established 1; dropped 0
          Local host: 1.1.1.1, Local port: 54707, IF Handle: 0x00000000
          Foreign host: 3.3.3.3, Foreign port: 179
          Last reset 00:00:00
            '''}


    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_instance_neighbors_detail_obj = ShowBgpInstanceNeighborsDetail(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_instance_neighbors_detail_obj.parse(vrf_type='all')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        bgp_instance_neighbors_detail_obj = ShowBgpInstanceNeighborsDetail(device=self.device)
        parsed_output = bgp_instance_neighbors_detail_obj.parse(vrf_type='all')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ==============================================================
# Unit test for 'show bgp instance all vrf all neighbors detail'
# ==============================================================

class test_show_bgp_instance_all_vrf_all_neighbors_detail(unittest.TestCase):

    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "instance": {
            "default": {
                "vrf": {
                    "VRF1": {
                        "neighbor": {
                            "2001:db8:1:5::5": {
                                "router_id": "10.1.5.1",
                                "local_as_as_no": 100,
                                "bgp_negotiated_capabilities": {
                                    "ipv6_unicast": "advertised received",
                                    "four_octets_asn": "advertised ",
                                    "route_refresh": "advertised "
                                },
                                "last_write_pulse_rcvd": "Jun 28 19:17:44.716 ",
                                "bgp_negotiated_keepalive_timers": {
                                    "hold_time": 180,
                                    "keepalive_interval": 60
                                },
                                "tcp_initial_sync": "---",
                                "last_full_not_set_pulse_count": 112,
                                "bgp_session_transport": {
                                    "connection": {
                                        "state": "established",
                                       "last_reset": "00:00:00",
                                        "connections_established": 1,
                                        "connections_dropped": 0
                                    },
                                    "transport": {
                                        "foreign_host": "2001:db8:1:5::5",
                                        "local_port": "179",
                                        "if_handle": "0x00000060",
                                        "local_host": "2001:db8:1:5::1",
                                        "foreign_port": "11014",
                                    }
                                },
                                "inbound_message": "3",
                                "keepalive": 60,
                                "minimum_time_between_adv_runs": 0,
                                "last_write": "00:00:38",
                                "enforcing_first_as": "enabled",
                                "second_attempted": 19,
                                "last_ka_start_before_second_last": "00:00:00",
                                "message_stats_input_queue": 0,
                                "address_family": {
                                    "ipv6 unicast": {
                                        "outstanding_version_objects_current": 0,
                                        "outstanding_version_objects_max": 1,
                                        "cummulative_no_by_orf_policy": 0,
                                        "policy_for_incoming_adv": "all-pass",
                                        "last_synced_ack_version": 0,
                                        "last_ack_version": 43,
                                        "best_paths": 0,
                                        "cummulative_no_prefixes_denied": 5,
                                        "maximum_prefixes_allowed": 524288,
                                        "cummulative_no_no_policy": 5,
                                        "eor_status": "was not received during read-only mode",
                                        "maximum_prefix_warning_only": True,
                                        "cummulative_no_by_policy": 0,
                                        "refresh_request_status": "No Refresh request being processed",
                                        "maximum_prefix_restart": 0,
                                        "additional_routes_local_label": "Unicast SAFI",
                                        "route_refresh_request_received": 0,
                                        "maximum_prefix_threshold": "75%",
                                        "update_group": "0.2",
                                        "neighbor_version": 43,
                                        "filter_group": "0.2",
                                        "exact_no_prefixes_denied": 0,
                                        "prefix_advertised": 10,
                                        "additional_paths_operation": "None",
                                        "prefix_withdrawn": 0,
                                        "prefix_suppressed": 0,
                                        "route_refresh_request_sent": 0,
                                        "accepted_prefixes": 0,
                                        "cummulative_no_failed_rt_match": 0,
                                        "policy_for_outgoing_adv": "all-pass"
                                    }
                                },
                                "second_last_write_before_written": 0,
                                "last_ka_error_ka_not_sent": "00:00:00",
                                "last_write_written": 0,
                                "written": 19,
                                "precedence": "internet",
                                "nsr_state": "None",
                                "second_last_write_before_attempted": 0,
                                "last_read_before_reset": "00:00:00",
                                "multiprotocol_capability": "received",
                                "second_written": 19,
                                "link_state": "external link",
                                "configured_hold_time": 180,
                                "last_write_pulse_rcvd_before_reset": "00:00:00",
                                "last_ka_error_before_reset": "00:00:00",
                                "second_last_write": "00:01:38",
                                "non_stop_routing": "enabled",
                                "attempted": 19,
                                "second_last_write_before_reset": "00:00:00",
                                "last_ka_expiry_before_second_last": "00:00:00",
                                "last_write_before_reset": "00:00:00",
                                "outbound_message": "3",
                                "last_write_attempted": 0,
                                "message_stats_output_queue": 0,
                                "remote_as": 200,
                                "last_write_thread_event_second_last": "00:00:00",
                                "last_write_thread_event_before_reset": "00:00:00",
                                "last_ka_start_before_reset": "00:00:00",
                                "min_acceptable_hold_time": 3,
                                "tcp_initial_sync_done": "---",
                                "last_read": "00:00:42",
                                "last_ka_expiry_before_reset": "00:00:00",
                                "session_state": "established",
                                "up_time": "00:53:45",
                                "bgp_neighbor_counters": {
                                    "messages": {
                                        "received": {
                                            "opens": 1,
                                            "keepalives": 54,
                                            "notifications": 0,
                                            "updates": 1,
                                        },
                                        "sent": {
                                            "opens": 1,
                                            "keepalives": 55,
                                            "notifications": 0,
                                            "updates": 3,
                                        }
                                    }
                                }
                            },
                            "10.1.5.5": {
                                "router_id": "10.1.5.5",
                                "local_as_as_no": 100,
                                "bgp_negotiated_capabilities": {
                                    "ipv4_unicast": "advertised received",
                                    "four_octets_asn": "advertised ",
                                    "route_refresh": "advertised "
                                },
                                "last_write_pulse_rcvd": "Jun 28 19:17:44.716 ",
                                "bgp_negotiated_keepalive_timers": {
                                    "hold_time": 180,
                                    "keepalive_interval": 60
                                },
                                "tcp_initial_sync": "---",
                                "last_full_not_set_pulse_count": 113,
                                "bgp_session_transport": {
                                    "connection": {
                                        "state": "established",
                                        "last_reset": "00:00:00",
                                        "connections_established": 1,
                                        "connections_dropped": 0
                                    },
                                    "transport": {
                                        "foreign_host": "10.1.5.5",
                                        "local_port": "179",
                                        "if_handle": "0x00000060",
                                        "local_host": "10.1.5.1",
                                        "foreign_port": "11052",
                                    }
                                },
                                "inbound_message": "3",
                                "keepalive": 60,
                                "minimum_time_between_adv_runs": 0,
                                "last_write": "00:00:38",
                                "enforcing_first_as": "enabled",
                                "second_attempted": 19,
                                "last_ka_start_before_second_last": "00:00:00",
                                "message_stats_input_queue": 0,
                                "address_family": {
                                    "ipv4 unicast": {
                                        "outstanding_version_objects_current": 0,
                                        "outstanding_version_objects_max": 1,
                                        "cummulative_no_by_orf_policy": 0,
                                        "policy_for_incoming_adv": "all-pass",
                                        "last_synced_ack_version": 0,
                                        "last_ack_version": 43,
                                        "best_paths": 0,
                                        "cummulative_no_prefixes_denied": 5,
                                        "maximum_prefixes_allowed": 1048576,
                                        "cummulative_no_no_policy": 5,
                                        "eor_status": "was not received during read-only mode",
                                        "maximum_prefix_warning_only": True,
                                        "cummulative_no_by_policy": 0,
                                        "refresh_request_status": "No Refresh request being processed",
                                        "maximum_prefix_restart": 0,
                                        "additional_routes_local_label": "Unicast SAFI",
                                        "route_refresh_request_received": 0,
                                        "maximum_prefix_threshold": "75%",
                                        "update_group": "0.2",
                                        "neighbor_version": 43,
                                        "filter_group": "0.2",
                                        "exact_no_prefixes_denied": 0,
                                        "prefix_advertised": 10,
                                        "additional_paths_operation": "None",
                                        "prefix_withdrawn": 0,
                                        "prefix_suppressed": 0,
                                        "route_refresh_request_sent": 0,
                                        "accepted_prefixes": 0,
                                        "cummulative_no_failed_rt_match": 0,
                                        "policy_for_outgoing_adv": "all-pass"
                                    }
                                },
                                "second_last_write_before_written": 0,
                                "last_ka_error_ka_not_sent": "00:00:00",
                                "last_write_written": 0,
                                "written": 19,
                                "precedence": "internet",
                                "nsr_state": "None",
                                "second_last_write_before_attempted": 0,
                                "last_read_before_reset": "00:00:00",
                                "multiprotocol_capability": "not received",
                                "second_written": 19,
                                "link_state": "external link",
                                "configured_hold_time": 180,
                                "last_write_pulse_rcvd_before_reset": "00:00:00",
                                "last_ka_error_before_reset": "00:00:00",
                                "second_last_write": "00:01:38",
                                "non_stop_routing": "enabled",
                                "attempted": 19,
                                "second_last_write_before_reset": "00:00:00",
                                "last_ka_expiry_before_second_last": "00:00:00",
                                "last_write_before_reset": "00:00:00",
                                "outbound_message": "3",
                                "last_write_attempted": 0,
                                "message_stats_output_queue": 0,
                                "remote_as": 200,
                                "last_write_thread_event_second_last": "00:00:00",
                                "last_write_thread_event_before_reset": "00:00:00",
                                "last_ka_start_before_reset": "00:00:00",
                                "min_acceptable_hold_time": 3,
                                "tcp_initial_sync_done": "---",
                                "last_read": "00:00:51",
                                "last_ka_expiry_before_reset": "00:00:00",
                                "session_state": "established",
                                "up_time": "00:53:54",
                                "bgp_neighbor_counters": {
                                    "messages": {
                                        "received": {
                                            "opens": 1,
                                            "keepalives": 54,
                                            "notifications": 0,
                                            "updates": 1,
                                        },
                                        "sent": {
                                            "opens": 1,
                                            "keepalives": 55,
                                            "notifications": 0,
                                            "updates": 2,
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "VRF2": {
                        "neighbor": {
                            "2001:db8:20:1:5::5": {
                                "router_id": "20.1.5.1",
                                "local_as_as_no": 100,
                                "bgp_negotiated_capabilities": {
                                    "ipv6_unicast": "advertised received",
                                    "four_octets_asn": "advertised ",
                                    "route_refresh": "advertised "
                                },
                                "last_write_pulse_rcvd": "Jun 28 19:17:40.237 ",
                                "bgp_negotiated_keepalive_timers": {
                                    "hold_time": 180,
                                    "keepalive_interval": 60
                                },
                                "tcp_initial_sync": "---",
                                "last_full_not_set_pulse_count": 102,
                                "bgp_session_transport": {
                                    "connection": {
                                        "state": "established",
                                        "last_reset": "00:00:00",
                                        "connections_established": 1,
                                        "connections_dropped": 0
                                    },
                                    "transport": {
                                        "foreign_host": "2001:db8:20:1:5::5",
                                        "local_port": "179",
                                        "if_handle": "0x00000080",
                                        "local_host": "2001:db8:20:1:5::1",
                                        "foreign_port": "11013",
                                    }
                                },
                                "inbound_message": "3",
                                "keepalive": 60,
                                "minimum_time_between_adv_runs": 0,
                                "last_write": "00:00:43",
                                "enforcing_first_as": "enabled",
                                "second_attempted": 19,
                                "last_ka_start_before_second_last": "00:00:00",
                                "message_stats_input_queue": 0,
                                "address_family": {
                                    "ipv6 unicast": {
                                        "outstanding_version_objects_current": 0,
                                        "outstanding_version_objects_max": 1,
                                        "additional_routes_local_label": "Unicast SAFI",
                                        "last_synced_ack_version": 0,
                                        "last_ack_version": 43,
                                        "best_paths": 5,
                                        "cummulative_no_prefixes_denied": 0,
                                        "maximum_prefixes_allowed": 524288,
                                        "eor_status": "was not received during read-only mode",
                                        "maximum_prefix_warning_only": True,
                                        "additional_paths_operation": "None",
                                        "maximum_prefix_restart": 0,
                                        "policy_for_incoming_adv": "all-pass",
                                        "route_refresh_request_received": 0,
                                        "accepted_prefixes": 5,
                                        "update_group": "0.1",
                                        "neighbor_version": 43,
                                        "filter_group": "0.1",
                                        "exact_no_prefixes_denied": 0,
                                        "prefix_advertised": 10,
                                        "prefix_withdrawn": 0,
                                        "prefix_suppressed": 0,
                                        "route_refresh_request_sent": 0,
                                        "maximum_prefix_threshold": "75%",
                                        "policy_for_outgoing_adv": "all-pass",
                                        "refresh_request_status": "No Refresh request being processed"
                                    }
                                },
                                "second_last_write_before_written": 0,
                                "last_ka_error_ka_not_sent": "00:00:00",
                                "last_write_written": 0,
                                "written": 19,
                                "precedence": "internet",
                                "nsr_state": "None",
                                "second_last_write_before_attempted": 0,
                                "last_read_before_reset": "00:00:00",
                                "multiprotocol_capability": "received",
                                "second_written": 19,
                                "link_state": "external link",
                                "configured_hold_time": 180,
                                "last_write_pulse_rcvd_before_reset": "00:00:00",
                                "last_ka_error_before_reset": "00:00:00",
                                "second_last_write": "00:01:43",
                                "non_stop_routing": "enabled",
                                "attempted": 19,
                                "second_last_write_before_reset": "00:00:00",
                                "last_ka_expiry_before_second_last": "00:00:00",
                                "last_write_before_reset": "00:00:00",
                                "outbound_message": "3",
                                "last_write_attempted": 0,
                                "message_stats_output_queue": 0,
                                "remote_as": 200,
                                "last_write_thread_event_second_last": "00:00:00",
                                "last_write_thread_event_before_reset": "00:00:00",
                                "last_ka_start_before_reset": "00:00:00",
                                "min_acceptable_hold_time": 3,
                                "tcp_initial_sync_done": "---",
                                "last_read": "00:00:46",
                                "last_ka_expiry_before_reset": "00:00:00",
                                "session_state": "established",
                                "up_time": "00:48:49",
                                "bgp_neighbor_counters": {
                                    "messages": {
                                        "received": {
                                            "opens": 1,
                                            "keepalives": 49,
                                            "notifications": 0,
                                            "updates": 1,
                                        },
                                        "sent": {
                                            "opens": 1,
                                            "keepalives": 49,
                                            "notifications": 0,
                                            "updates": 3,
                                        }
                                    }
                                }
                            },
                            "20.1.5.5": {
                                "router_id": "20.1.5.5",
                                "local_as_as_no": 100,
                                "bgp_negotiated_capabilities": {
                                    "ipv4_unicast": "advertised received",
                                    "four_octets_asn": "advertised ",
                                    "route_refresh": "advertised "
                                },
                                "last_write_pulse_rcvd": "Jun 28 19:17:40.237 ",
                                "bgp_negotiated_keepalive_timers": {
                                    "hold_time": 180,
                                    "keepalive_interval": 60
                                },
                                "tcp_initial_sync": "---",
                                "last_full_not_set_pulse_count": 102,
                                "bgp_session_transport": {
                                    "connection": {
                                        "state": "established",
                                        "last_reset": "00:00:00",
                                        "connections_established": 1,
                                        "connections_dropped": 0
                                    },
                                    "transport": {
                                        "foreign_host": "20.1.5.5",
                                        "local_port": "179",
                                        "if_handle": "0x00000080",
                                        "local_host": "20.1.5.1",
                                        "foreign_port": "11099",
                                    }
                                },
                                "inbound_message": "3",
                                "keepalive": 60,
                                "minimum_time_between_adv_runs": 0,
                                "last_write": "00:00:43",
                                "enforcing_first_as": "enabled",
                                "second_attempted": 19,
                                "last_ka_start_before_second_last": "00:00:00",
                                "message_stats_input_queue": 0,
                                "address_family": {
                                    "ipv4 unicast": {
                                        "outstanding_version_objects_current": 0,
                                        "outstanding_version_objects_max": 1,
                                        "additional_routes_local_label": "Unicast SAFI",
                                        "last_synced_ack_version": 0,
                                        "last_ack_version": 43,
                                        "best_paths": 5,
                                        "cummulative_no_prefixes_denied": 0,
                                        "maximum_prefixes_allowed": 495,
                                        "eor_status": "was not received during read-only mode",
                                        "maximum_prefix_warning_only": True,
                                        "additional_paths_operation": "None",
                                        "maximum_prefix_restart": 0,
                                        "policy_for_incoming_adv": "all-pass",
                                        "route_refresh_request_received": 0,
                                        "accepted_prefixes": 5,
                                        "update_group": "0.1",
                                        "neighbor_version": 43,
                                        "filter_group": "0.1",
                                        "exact_no_prefixes_denied": 0,
                                        "prefix_advertised": 10,
                                        "prefix_withdrawn": 0,
                                        "prefix_suppressed": 0,
                                        "route_refresh_request_sent": 0,
                                        "maximum_prefix_threshold": "75%",
                                        "policy_for_outgoing_adv": "all-pass",
                                        "refresh_request_status": "No Refresh request being processed"
                                    }
                                },
                                "second_last_write_before_written": 0,
                                "last_ka_error_ka_not_sent": "00:00:00",
                                "last_write_written": 0,
                                "written": 19,
                                "precedence": "internet",
                                "nsr_state": "None",
                                "second_last_write_before_attempted": 0,
                                "last_read_before_reset": "00:00:00",
                                "multiprotocol_capability": "not received",
                                "second_written": 19,
                                "link_state": "external link",
                                "configured_hold_time": 180,
                                "last_write_pulse_rcvd_before_reset": "00:00:00",
                                "last_ka_error_before_reset": "00:00:00",
                                "second_last_write": "00:01:43",
                                "non_stop_routing": "enabled",
                                "attempted": 19,
                                "second_last_write_before_reset": "00:00:00",
                                "last_ka_expiry_before_second_last": "00:00:00",
                                "last_write_before_reset": "00:00:00",
                                "outbound_message": "3",
                                "last_write_attempted": 0,
                                "message_stats_output_queue": 0,
                                "remote_as": 200,
                                "last_write_thread_event_second_last": "00:00:00",
                                "last_write_thread_event_before_reset": "00:00:00",
                                "last_ka_start_before_reset": "00:00:00",
                                "min_acceptable_hold_time": 3,
                                "tcp_initial_sync_done": "---",
                                "last_read": "00:00:51",
                                "last_ka_expiry_before_reset": "00:00:00",
                                "session_state": "established",
                                "up_time": "00:48:54",
                                "bgp_neighbor_counters": {
                                    "messages": {
                                         "received": {
                                              "opens": 1,
                                              "keepalives": 49,
                                              "notifications": 0,
                                              "updates": 1,
                                         },
                                         "sent": {
                                              "opens": 1,
                                              "keepalives": 50,
                                              "notifications": 0,
                                              "updates": 2,
                                         }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''
        Wed Jun 28 19:18:23.304 UTC

        BGP instance 0: 'default'
        =========================

        VRF: VRF1
        ---------

        BGP neighbor is 10.1.5.5, vrf VRF1
         Remote AS 200, local AS 100, external link
         Remote router ID 10.1.5.5
          BGP state = Established, up for 00:53:54
          NSR State: None
          Last read 00:00:51, Last read before reset 00:00:00
          Hold time is 180, keepalive interval is 60 seconds
          Configured hold time: 180, keepalive: 60, min acceptable hold time: 3
          Last write 00:00:38, attempted 19, written 19
          Second last write 00:01:38, attempted 19, written 19
          Last write before reset 00:00:00, attempted 0, written 0
          Second last write before reset 00:00:00, attempted 0, written 0
          Last write pulse rcvd  Jun 28 19:17:44.716 last full not set pulse count 113
          Last write pulse rcvd before reset 00:00:00
          Socket not armed for io, armed for read, armed for write
          Last write thread event before reset 00:00:00, second last 00:00:00
          Last KA expiry before reset 00:00:00, second last 00:00:00
          Last KA error before reset 00:00:00, KA not sent 00:00:00
          Last KA start before reset 00:00:00, second last 00:00:00
          Precedence: internet
          Non-stop routing is enabled
          Entered Neighbor NSR TCP mode:
            TCP Initial Sync :              ---                
            TCP Initial Sync Phase Two :    ---                
            TCP Initial Sync Done :         ---                
          Enforcing first AS is enabled
          Multi-protocol capability not received
          Neighbor capabilities:            Adv         Rcvd
            Route refresh:                  Yes         No
            4-byte AS:                      Yes         No
            Address family IPv4 Unicast:    Yes         Yes
          Message stats:
            InQ depth: 0, OutQ depth: 0
                            Last_Sent               Sent  Last_Rcvd               Rcvd
            Open:           Jun 28 18:24:28.875        1  Jun 28 18:24:28.875        1
            Notification:   ---                        0  ---                        0
            Update:         Jun 28 18:28:43.838        2  Jun 28 18:24:29.135        1
            Keepalive:      Jun 28 19:17:44.616       55  Jun 28 19:17:31.987       54
            Route_Refresh:  ---                        0  ---                        0
            Total:                                    58                            56
          Minimum time between advertisement runs is 0 secs
          Inbound message logging enabled, 3 messages buffered
          Outbound message logging enabled, 3 messages buffered

         For Address Family: IPv4 Unicast
          BGP neighbor version 43
          Update group: 0.2 Filter-group: 0.2  No Refresh request being processed
          Route refresh request: received 0, sent 0
          Policy for incoming advertisements is all-pass
          Policy for outgoing advertisements is all-pass
          0 accepted prefixes, 0 are bestpaths
          Exact no. of prefixes denied : 0.
          Cumulative no. of prefixes denied: 5. 
            No policy: 5, Failed RT match: 0
            By ORF policy: 0, By policy: 0
          Prefix advertised 10, suppressed 0, withdrawn 0
          Maximum prefixes allowed 1048576
          Threshold for warning message 75%, restart interval 0 min
          An EoR was not received during read-only mode
          Last ack version 43, Last synced ack version 0
          Outstanding version objects: current 0, max 1
          Additional-paths operation: None
          Advertise routes with local-label via Unicast SAFI

          Connections established 1; dropped 0
          Local host: 10.1.5.1, Local port: 179, IF Handle: 0x00000060
          Foreign host: 10.1.5.5, Foreign port: 11052
          Last reset 00:00:00

        BGP neighbor is 2001:db8:1:5::5, vrf VRF1
         Remote AS 200, local AS 100, external link
         Remote router ID 10.1.5.1
          BGP state = Established, up for 00:53:45
          NSR State: None
          Last read 00:00:42, Last read before reset 00:00:00
          Hold time is 180, keepalive interval is 60 seconds
          Configured hold time: 180, keepalive: 60, min acceptable hold time: 3
          Last write 00:00:38, attempted 19, written 19
          Second last write 00:01:38, attempted 19, written 19
          Last write before reset 00:00:00, attempted 0, written 0
          Second last write before reset 00:00:00, attempted 0, written 0
          Last write pulse rcvd  Jun 28 19:17:44.716 last full not set pulse count 112
          Last write pulse rcvd before reset 00:00:00
          Socket not armed for io, armed for read, armed for write
          Last write thread event before reset 00:00:00, second last 00:00:00
          Last KA expiry before reset 00:00:00, second last 00:00:00
          Last KA error before reset 00:00:00, KA not sent 00:00:00
          Last KA start before reset 00:00:00, second last 00:00:00
          Precedence: internet
          Non-stop routing is enabled
          Entered Neighbor NSR TCP mode:
            TCP Initial Sync :              ---                
            TCP Initial Sync Phase Two :    ---                
            TCP Initial Sync Done :         ---                
          Enforcing first AS is enabled
          Multi-protocol capability received
          Neighbor capabilities:            Adv         Rcvd
            Route refresh:                  Yes         No
            4-byte AS:                      Yes         No
            Address family IPv6 Unicast:    Yes         Yes
          Message stats:
            InQ depth: 0, OutQ depth: 0
                            Last_Sent               Sent  Last_Rcvd               Rcvd
            Open:           Jun 28 18:24:37.875        1  Jun 28 18:24:37.875        1
            Notification:   ---                        0  ---                        0
            Update:         Jun 28 18:28:43.838        3  Jun 28 18:24:38.135        1
            Keepalive:      Jun 28 19:17:44.616       55  Jun 28 19:17:41.026       54
            Route_Refresh:  ---                        0  ---                        0
            Total:                                    59                            56
          Minimum time between advertisement runs is 0 secs
          Inbound message logging enabled, 3 messages buffered
          Outbound message logging enabled, 3 messages buffered

         For Address Family: IPv6 Unicast
          BGP neighbor version 43
          Update group: 0.2 Filter-group: 0.2  No Refresh request being processed
          Route refresh request: received 0, sent 0
          Policy for incoming advertisements is all-pass
          Policy for outgoing advertisements is all-pass
          0 accepted prefixes, 0 are bestpaths
          Exact no. of prefixes denied : 0.
          Cumulative no. of prefixes denied: 5. 
            No policy: 5, Failed RT match: 0
            By ORF policy: 0, By policy: 0
          Prefix advertised 10, suppressed 0, withdrawn 0
          Maximum prefixes allowed 524288
          Threshold for warning message 75%, restart interval 0 min
          An EoR was not received during read-only mode
          Last ack version 43, Last synced ack version 0
          Outstanding version objects: current 0, max 1
          Additional-paths operation: None
          Advertise routes with local-label via Unicast SAFI

          Connections established 1; dropped 0
          Local host: 2001:db8:1:5::1, Local port: 179, IF Handle: 0x00000060
          Foreign host: 2001:db8:1:5::5, Foreign port: 11014
          Last reset 00:00:00

        VRF: VRF2
        ---------

        BGP neighbor is 20.1.5.5, vrf VRF2
         Remote AS 200, local AS 100, external link
         Remote router ID 20.1.5.5
          BGP state = Established, up for 00:48:54
          NSR State: None
          Last read 00:00:51, Last read before reset 00:00:00
          Hold time is 180, keepalive interval is 60 seconds
          Configured hold time: 180, keepalive: 60, min acceptable hold time: 3
          Last write 00:00:43, attempted 19, written 19
          Second last write 00:01:43, attempted 19, written 19
          Last write before reset 00:00:00, attempted 0, written 0
          Second last write before reset 00:00:00, attempted 0, written 0
          Last write pulse rcvd  Jun 28 19:17:40.237 last full not set pulse count 102
          Last write pulse rcvd before reset 00:00:00
          Socket not armed for io, armed for read, armed for write
          Last write thread event before reset 00:00:00, second last 00:00:00
          Last KA expiry before reset 00:00:00, second last 00:00:00
          Last KA error before reset 00:00:00, KA not sent 00:00:00
          Last KA start before reset 00:00:00, second last 00:00:00
          Precedence: internet
          Non-stop routing is enabled
          Entered Neighbor NSR TCP mode:
            TCP Initial Sync :              ---                
            TCP Initial Sync Phase Two :    ---                
            TCP Initial Sync Done :         ---                
          Enforcing first AS is enabled
          Multi-protocol capability not received
          Neighbor capabilities:            Adv         Rcvd
            Route refresh:                  Yes         No
            4-byte AS:                      Yes         No
            Address family IPv4 Unicast:    Yes         Yes
          Message stats:
            InQ depth: 0, OutQ depth: 0
                            Last_Sent               Sent  Last_Rcvd               Rcvd
            Open:           Jun 28 18:29:29.345        1  Jun 28 18:29:29.345        1
            Notification:   ---                        0  ---                        0
            Update:         Jun 28 18:29:39.374        2  Jun 28 18:29:29.595        1
            Keepalive:      Jun 28 19:17:40.137       50  Jun 28 19:17:31.987       49
            Route_Refresh:  ---                        0  ---                        0
            Total:                                    53                            51
          Minimum time between advertisement runs is 0 secs
          Inbound message logging enabled, 3 messages buffered
          Outbound message logging enabled, 3 messages buffered

         For Address Family: IPv4 Unicast
          BGP neighbor version 43
          Update group: 0.1 Filter-group: 0.1  No Refresh request being processed
          Route refresh request: received 0, sent 0
          Policy for incoming advertisements is all-pass
          Policy for outgoing advertisements is all-pass
          5 accepted prefixes, 5 are bestpaths
          Exact no. of prefixes denied : 0.
          Cumulative no. of prefixes denied: 0. 
          Prefix advertised 10, suppressed 0, withdrawn 0
          Maximum prefixes allowed 495
          Threshold for warning message 75%, restart interval 0 min
          An EoR was not received during read-only mode
          Last ack version 43, Last synced ack version 0
          Outstanding version objects: current 0, max 1
          Additional-paths operation: None
          Advertise routes with local-label via Unicast SAFI

          Connections established 1; dropped 0
          Local host: 20.1.5.1, Local port: 179, IF Handle: 0x00000080
          Foreign host: 20.1.5.5, Foreign port: 11099
          Last reset 00:00:00

        BGP neighbor is 2001:db8:20:1:5::5, vrf VRF2
         Remote AS 200, local AS 100, external link
         Remote router ID 20.1.5.1
          BGP state = Established, up for 00:48:49
          NSR State: None
          Last read 00:00:46, Last read before reset 00:00:00
          Hold time is 180, keepalive interval is 60 seconds
          Configured hold time: 180, keepalive: 60, min acceptable hold time: 3
          Last write 00:00:43, attempted 19, written 19
          Second last write 00:01:43, attempted 19, written 19
          Last write before reset 00:00:00, attempted 0, written 0
          Second last write before reset 00:00:00, attempted 0, written 0
          Last write pulse rcvd  Jun 28 19:17:40.237 last full not set pulse count 102
          Last write pulse rcvd before reset 00:00:00
          Socket not armed for io, armed for read, armed for write
          Last write thread event before reset 00:00:00, second last 00:00:00
          Last KA expiry before reset 00:00:00, second last 00:00:00
          Last KA error before reset 00:00:00, KA not sent 00:00:00
          Last KA start before reset 00:00:00, second last 00:00:00
          Precedence: internet
          Non-stop routing is enabled
          Entered Neighbor NSR TCP mode:
            TCP Initial Sync :              ---                
            TCP Initial Sync Phase Two :    ---                
            TCP Initial Sync Done :         ---                
          Enforcing first AS is enabled
          Multi-protocol capability received
          Neighbor capabilities:            Adv         Rcvd
            Route refresh:                  Yes         No
            4-byte AS:                      Yes         No
            Address family IPv6 Unicast:    Yes         Yes
          Message stats:
            InQ depth: 0, OutQ depth: 0
                            Last_Sent               Sent  Last_Rcvd               Rcvd
            Open:           Jun 28 18:29:34.344        1  Jun 28 18:29:34.344        1
            Notification:   ---                        0  ---                        0
            Update:         Jun 28 18:29:39.374        3  Jun 28 18:29:34.604        1
            Keepalive:      Jun 28 19:17:40.137       49  Jun 28 19:17:37.007       49
            Route_Refresh:  ---                        0  ---                        0
            Total:                                    53                            51
          Minimum time between advertisement runs is 0 secs
          Inbound message logging enabled, 3 messages buffered
          Outbound message logging enabled, 3 messages buffered

         For Address Family: IPv6 Unicast
          BGP neighbor version 43
          Update group: 0.1 Filter-group: 0.1  No Refresh request being processed
          Route refresh request: received 0, sent 0
          Policy for incoming advertisements is all-pass
          Policy for outgoing advertisements is all-pass
          5 accepted prefixes, 5 are bestpaths
          Exact no. of prefixes denied : 0.
          Cumulative no. of prefixes denied: 0. 
          Prefix advertised 10, suppressed 0, withdrawn 0
          Maximum prefixes allowed 524288
          Threshold for warning message 75%, restart interval 0 min
          An EoR was not received during read-only mode
          Last ack version 43, Last synced ack version 0
          Outstanding version objects: current 0, max 1
          Additional-paths operation: None
          Advertise routes with local-label via Unicast SAFI

          Connections established 1; dropped 0
          Local host: 2001:db8:20:1:5::1, Local port: 179, IF Handle: 0x00000080
          Foreign host: 2001:db8:20:1:5::5, Foreign port: 11013
          Last reset 00:00:00
        
            '''}


    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_instance_neighbors_detail_obj = ShowBgpInstanceNeighborsDetail(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_instance_neighbors_detail_obj.parse(vrf_type='vrf')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        bgp_instance_neighbors_detail_obj = ShowBgpInstanceNeighborsDetail(device=self.device)
        parsed_output = bgp_instance_neighbors_detail_obj.parse(vrf_type='vrf')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ================================================================================
# Unit test for 'show bgp instance all vrf all neighbors <WORD> advertised-routes'
# ================================================================================

class test_show_bgp_instance_all_vrf_all_neighbors_advertised_routes(unittest.TestCase):
        
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output =  {
        "instance": {
            "default": {
                "vrf": {
                    "VRF2": {
                        "address_family": {
                            "ipv4 unicast RD 200:2": {
                                "advertised": {
                                    "prefix": {
                                        "46.2.2.0/24": {
                                            "index": {
                                                1: {
                                                    "froms": "2.2.2.2",
                                                    "next_hop": "20.1.5.1",
                                                    "asn": 100,
                                                    "origin_code": "e",
                                                    "path": "400 33299 51178 47751 {27016}"}}},
                                        "46.1.1.0/24": {
                                            "index": {
                                                1: {
                                                    "froms": "2.2.2.2",
                                                    "next_hop": "20.1.5.1",
                                                    "asn": 100,
                                                    "origin_code": "e",
                                                    "path": "300 33299 51178 47751 {27016}"}}},
                                        "46.1.5.0/24": {
                                            "index": {
                                                1: {
                                                    "froms": "2.2.2.2",
                                                    "next_hop": "20.1.5.1",
                                                    "asn": 100,
                                                    "origin_code": "e",
                                                    "path": "300 33299 51178 47751 {27016}"}}},
                                        "46.1.4.0/24": {
                                            "index": {
                                                1: {
                                                    "froms": "2.2.2.2",
                                                    "next_hop": "20.1.5.1",
                                                    "asn": 100,
                                                    "origin_code": "e",
                                                    "path": "300 33299 51178 47751 {27016}"
                                        }}}}},
                                "processed_prefixes": "4",
                                "route_distinguisher": "200:2",
                                "processed_paths": "4",
                                "default_vrf": "VRF2"}}},
                    "VRF1": {}
                    }
                }
            }
        }



    golden_output = {'execute.return_value': '''
    
     Neighbor not found

    BGP instance 0: 'default'
    =========================

    VRF: VRF1
    ---------

    VRF: VRF2
    ---------
    Network            Next Hop        From            AS Path
    Route Distinguisher: 200:2 (default for vrf VRF2)
    46.1.1.0/24        20.1.5.1        2.2.2.2         100 300 33299 51178 47751 {27016}e
    46.1.4.0/24        20.1.5.1        2.2.2.2         100 300 33299 51178 47751 {27016}e
    46.1.5.0/24        20.1.5.1        2.2.2.2         100 300 33299 51178 47751 {27016}e
    46.2.2.0/24        20.1.5.1        2.2.2.2         100 400 33299 51178 47751 {27016}e

    Processed 4 prefixes, 4 paths

        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_instance_all_vrf_all_neighbors_advertised_routes_obj = ShowBgpInstanceNeighborsAdvertisedRoutes(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_instance_all_vrf_all_neighbors_advertised_routes_obj.parse(neighbor='20.1.5.5', vrf='vrf')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        bgp_instance_all_vrf_all_neighbors_advertised_routes_obj = ShowBgpInstanceNeighborsAdvertisedRoutes(device=self.device)
        parsed_output = bgp_instance_all_vrf_all_neighbors_advertised_routes_obj.parse(neighbor='20.1.5.5', vrf='vrf')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ================================================================================
# Unit test for 'show bgp instance all all all neighbors <WORD> advertised-routes'
# ================================================================================

class test_show_bgp_instance_all_all_all_neighbors_advertised_routes(unittest.TestCase):
        
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output =  {
        "instance": {
            "default": {
                "vrf": {
                    "default": {
                        "address_family": {
                            "vpnv4 unicast RD 200:2": {
                                "processed_paths": "2",
                                "processed_prefixes": "2",
                                "advertised": {
                                    "prefix": {
                                        "15.1.2.0/24": {
                                            "index": {
                                                1: {
                                                    "froms": "20.1.5.5",
                                                    "path": "33299 51178 47751 {27016}",
                                                    "asn": 200,
                                                    "next_hop": "1.1.1.1",
                                                    "origin_code": "e"
                                                }
                                            }
                                        },
                                        "15.1.1.0/24": {
                                            "index": {
                                                1: {
                                                    "froms": "20.1.5.5",
                                                    "path": "33299 51178 47751 {27016}",
                                                    "asn": 200,
                                                    "next_hop": "1.1.1.1",
                                                    "origin_code": "e"
                                                }
                                            }
                                        }
                                    }
                                },
                                "default_vrf": "default",
                                "route_distinguisher": "200:2"
                            },
                            "vpnv6 unicast RD 200:2": {
                                "processed_paths": "2",
                                "processed_prefixes": "2",
                                "advertised": {
                                    "prefix": {
                                        "615:11:11::/64": {
                                            "index": {
                                                1: {
                                                    "froms": "2001:db8:20:1:5::5",
                                                    "path": "33299 51178 47751 {27017}",
                                                    "asn": 200,
                                                    "next_hop": "1.1.1.1",
                                                    "origin_code": "e"
                                                }
                                            }
                                        },
                                        "615:11:11:1::/64": {
                                            "index": {
                                                1: {
                                                    "froms": "2001:db8:20:1:5::5",
                                                    "path": "33299 51178 47751 {27016}",
                                                    "asn": 200,
                                                    "next_hop": "1.1.1.1",
                                                    "origin_code": "e"
                                                }
                                            }
                                        }
                                    }
                                },
                                "default_vrf": "default",
                                "route_distinguisher": "200:2"
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''

         BGP instance 0: 'default'
        =========================

        Address Family: VPNv4 Unicast
        -----------------------------

        Network            Next Hop        From            AS  Path
        Route Distinguisher: 200:2
        15.1.1.0/24        1.1.1.1         20.1.5.5        200 33299 51178 47751 {27016}e
        15.1.2.0/24        1.1.1.1         20.1.5.5        200 33299 51178 47751 {27016}e

        Processed 2 prefixes, 2 paths

        Address Family: VPNv6 Unicast
        -----------------------------

        Network            Next Hop        From            AS  Path
        Route Distinguisher: 200:2
        615:11:11::/64     1.1.1.1         2001:db8:20:1:5::5
                                                           200 33299 51178 47751 {27017}e
        615:11:11:1::/64   1.1.1.1         2001:db8:20:1:5::5
                                                           200 33299 51178 47751 {27016}e

        Processed 2 prefixes, 2 paths
        '''}
    
    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowBgpInstanceNeighborsAdvertisedRoutes(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(neighbor='3.3.3.3', vrf='all')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpInstanceNeighborsAdvertisedRoutes(device=self.device)
        parsed_output = obj.parse(neighbor='3.3.3.3', vrf='all')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ==============================================================================
# Unit test for 'show bgp instance all vrf all neighbors <WORD> received-routes'
# ==============================================================================

class test_show_bgp_instance_all_vrf_all_neighbors_received_routes(unittest.TestCase):
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output =   {
        "instance": {
           "default": {
                "vrf": {
                    "vrf2": {
                        "address_family": {
                            "ipv4 unicast RD 200:2": {
                                "non_stop_routing": True,
                                "vrf_id": "0x60000002",
                                "processed_prefixes": 2,
                                "table_state": "Active",
                                "state": "Active",
                                "processed_paths": 2,
                                "table_id": "0xe0000011",
                                "nsr_initial_initsync_version": "11 (Reached)",
                                "tbl_ver": 63,
                                "received": {
                                    "prefix": {
                                        "15.1.1.0/24": {
                                            "index": {
                                                1: {
                                                    "next_hop": "20.1.5.5",
                                                    "origin_codes": "e",
                                                    "metric": "2219",
                                                    "path": "200 33299 51178 47751 {27016}",
                                                    "weight": "0",
                                                    "status_codes": "*"
                                                }
                                            }
                                        },
                                        "15.1.2.0/24": {
                                            "index": {
                                                1: {
                                                    "next_hop": "20.1.5.5",
                                                    "origin_codes": "e",
                                                    "metric": "2219",
                                                    "path": "200 33299 51178 47751 {27016}",
                                                    "weight": "0",
                                                    "status_codes": "*"
                                                }}}}},
                               "local_as": 100,
                               "route_identifier": "11.11.11.11",
                               "rd_version": 63,
                               "nsr_issu_sync_group_versions": "0/0"
                            }}}}}}}



    golden_output = {'execute.return_value': '''
        Wed Jun 28 19:20:50.783 UTC
        % Neighbor not found

        BGP instance 0: 'default'
        =========================

        VRF: VRF1
        ---------

        VRF: VRF2
        ---------
        BGP VRF VRF2, state: Active
        BGP Route Distinguisher: 200:2
        VRF ID: 0x60000002
        BGP router identifier 11.11.11.11, local AS number 100
        Non-stop routing is enabled
        BGP table state: Active
        Table ID: 0xe0000011   RD version: 63
        BGP main routing table version 63
        BGP NSR Initial initsync version 11 (Reached)
        BGP NSR/ISSU Sync-Group versions 0/0

        Status codes: s suppressed, d damped, h history, * valid, > best
                      i - internal, r RIB-failure, S stale, N Nexthop-discard
        Origin codes: i - IGP, e - EGP, ? - incomplete
           Network            Next Hop            Metric LocPrf Weight Path
        Route Distinguisher: 200:2 (default for vrf VRF2)
        *  15.1.1.0/24        20.1.5.5              2219             0 200 33299 51178 47751 {27016} e
        *  15.1.2.0/24        20.1.5.5              2219             0 200 33299 51178 47751 {27016} e

        Processed 2 prefixes, 2 paths
        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowBgpInstanceNeighborsReceivedRoutes(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='vrf',neighbor='20.1.5.5')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpInstanceNeighborsReceivedRoutes(device=self.device)
        parsed_output = obj.parse(vrf='vrf',neighbor='20.1.5.5')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ==============================================================================
# Unit test for 'show bgp instance all all all neighbors <WORD> received-routes'
# ==============================================================================

class test_show_bgp_instance_all_all_all_neighbors_received_routes(unittest.TestCase):
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output =  {
        "instance": {
            "default": {
                "vrf": {
                    "default": {
                        "address_family": {
                            "vpnv4 unicast RD 300:1": {
                                "nsr_initial_initsync_version": "11 (Reached)",
                                "route_identifier": "1.1.1.1",
                                "non_stop_routing": True,
                                "nsr_issu_sync_group_versions": "0/0",
                                "received": {
                                    "prefix": {
                                        "46.1.1.0/24": {
                                            "index": {
                                                1: {
                                                    "metric": "2219",
                                                    "locprf": "100",
                                                    "path": "300 33299 51178 47751 {27016}",
                                                    "weight": "0",
                                                    "origin_codes": "e",
                                                    "status_codes": "*i",
                                                    "next_hop": "4.4.4.4"
                                                }}}}},
                                "generic_scan_interval": 60,
                                "local_as": 100,
                                "rd_version": 0,
                                "tbl_ver": 43,
                                "table_id": "0x0",
                                "table_state": "Active",
                                "scan_interval": 60
                            },
                            "vpnv6 unicast RD 300:1": {
                                "nsr_initial_initsync_version": "11 (Reached)",
                                "route_identifier": "1.1.1.1",
                                "non_stop_routing": True,
                                "nsr_issu_sync_group_versions": "0/0",
                                "received": {
                                    "prefix": {
                                        "646:11:11::/64": {
                                            "index": {
                                                1: {
                                                    "metric": "2219",
                                                    "locprf": "100",
                                                    "path": "300 33299 51178 47751 {27016}",
                                                    "weight": "0",
                                                    "origin_codes": "e",
                                                    "status_codes": "*i",
                                                    "next_hop": "4.4.4.4"
                                                   }
                                              }
                                        },
                                        "646:11:11:4::/64": {
                                            "index": {
                                                1: {
                                                    "metric": "2219",
                                                    "locprf": "100",
                                                    "path": "300 33299 51178 47751 {27016}",
                                                    "weight": "0",
                                                    "origin_codes": "e",
                                                    "status_codes": "*i",
                                                    "next_hop": "4.4.4.4"
                                                   }}}}},
                                "generic_scan_interval": 60,
                                "local_as": 100,
                                "rd_version": 0,
                                "tbl_ver": 43,
                                "table_id": "0x0",
                                "table_state": "Active",
                                "scan_interval": 60
                            },
                            "vpnv6 unicast RD 400:1": {
                                "nsr_initial_initsync_version": "11 (Reached)",
                                "route_identifier": "1.1.1.1",
                                "non_stop_routing": True,
                                "nsr_issu_sync_group_versions": "0/0",
                                "received": {
                                    "prefix": {
                                        "646:22:22:1::/64": {
                                            "index": {
                                                1: {
                                                    "metric": "2219",
                                                    "locprf": "100",
                                                    "path": "400 33299 51178 47751 {27016}",
                                                    "weight": "0",
                                                    "origin_codes": "e",
                                                    "status_codes": "*i",
                                                    "next_hop": "4.4.4.4"}}},
                                        "646:22:22::/64": {
                                            "index": {
                                                1: {
                                                    "metric": "2219",
                                                    "locprf": "100",
                                                    "path": "400 33299 51178 47751 {27016}",
                                                    "weight": "0",
                                                    "origin_codes": "e",
                                                    "status_codes": "*i",
                                                    "next_hop": "4.4.4.4"
                                                   }}}}},
                                "generic_scan_interval": 60,
                                "processed_paths": 10,
                                "rd_version": 0,
                                "tbl_ver": 43,
                                "table_id": "0x0",
                                "table_state": "Active",
                                "processed_prefixes": 10,
                                "local_as": 100,
                                "scan_interval": 60
                            },
                            "vpnv4 unicast RD 400:1": {
                                "nsr_initial_initsync_version": "11 (Reached)",
                                "route_identifier": "1.1.1.1",
                                "non_stop_routing": True,
                                "nsr_issu_sync_group_versions": "0/0",
                                "received": {
                                    "prefix": {
                                        "46.2.2.0/24": {
                                            "index": {
                                                1: {
                                                    "metric": "2219",
                                                    "locprf": "100",
                                                    "path": "400 33299 51178 47751 {27016}",
                                                    "weight": "0",
                                                    "origin_codes": "e",
                                                    "status_codes": "*i",
                                                    "next_hop": "4.4.4.4"}}}}},
                                "generic_scan_interval": 60,
                                "processed_paths": 10,
                                "rd_version": 0,
                                "tbl_ver": 43,
                                "table_id": "0x0",
                                "table_state": "Active",
                                "processed_prefixes": 10,
                                "local_as": 100,
                                "scan_interval": 60}}}}}}}



    golden_output = {'execute.return_value': '''
        BGP instance 0: 'default'
        =========================

        Address Family: VPNv4 Unicast
        -----------------------------

        BGP router identifier 1.1.1.1, local AS number 100
        BGP generic scan interval 60 secs
        Non-stop routing is enabled
        BGP table state: Active
        Table ID: 0x0   RD version: 0
        BGP main routing table version 43
        BGP NSR Initial initsync version 11 (Reached)
        BGP NSR/ISSU Sync-Group versions 0/0
        BGP scan interval 60 secs

        Status codes: s suppressed, d damped, h history, * valid, > best
                      i - internal, r RIB-failure, S stale, N Nexthop-discard
        Origin codes: i - IGP, e - EGP, ? - incomplete
           Network            Next Hop            Metric LocPrf Weight Path
        Route Distinguisher: 300:1
        * i46.1.1.0/24        4.4.4.4               2219    100      0 300 33299 51178 47751 {27016} e
        Route Distinguisher: 400:1
        * i46.2.2.0/24        4.4.4.4               2219    100      0 400 33299 51178 47751 {27016} e

        Processed 10 prefixes, 10 paths

        Address Family: VPNv6 Unicast
        -----------------------------

        BGP router identifier 1.1.1.1, local AS number 100
        BGP generic scan interval 60 secs
        Non-stop routing is enabled
        BGP table state: Active
        Table ID: 0x0   RD version: 0
        BGP main routing table version 43
        BGP NSR Initial initsync version 11 (Reached)
        BGP NSR/ISSU Sync-Group versions 0/0
        BGP scan interval 60 secs

        Status codes: s suppressed, d damped, h history, * valid, > best
                      i - internal, r RIB-failure, S stale, N Nexthop-discard
        Origin codes: i - IGP, e - EGP, ? - incomplete
           Network            Next Hop            Metric LocPrf Weight Path
        Route Distinguisher: 300:1
        * i646:11:11::/64     4.4.4.4               2219    100      0 300 33299 51178 47751 {27016} e
        * i646:11:11:4::/64   4.4.4.4               2219    100      0 300 33299 51178 47751 {27016} e
        Route Distinguisher: 400:1
        * i646:22:22::/64     4.4.4.4               2219    100      0 400 33299 51178 47751 {27016} e
        * i646:22:22:1::/64   4.4.4.4               2219    100      0 400 33299 51178 47751 {27016} e

        Processed 10 prefixes, 10 paths


        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowBgpInstanceNeighborsReceivedRoutes(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='all',neighbor='20.1.5.5')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpInstanceNeighborsReceivedRoutes(device=self.device)
        parsed_output = obj.parse(vrf='all',neighbor='20.1.5.5')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# =====================================================================
# Unit test for 'show bgp instance all vrf all neighbors <WORD> routes'
# =====================================================================

class test_show_bgp_instance_all_vrf_all_neighbors_routes(unittest.TestCase):
    
    dev = Device(name='Device')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        "instance": {
            "default": {
                "vrf": {
                    "vrf2": {
                        "address_family": {
                            "ipv4 unicast RD 200:2": {
                                "nsr_initial_initsync_version": "11 (Reached)",
                                "route_identifier": "11.11.11.11",
                                "non_stop_routing": True,
                                "processed_prefixes": 2,
                                "vrf_id": "0x60000002",
                                "table_id": "0xe0000011",
                                "local_as": 100,
                                "tbl_ver": 63,
                                "processed_paths": 2,
                                "nsr_issu_sync_group_versions": "0/0",
                                "table_state": "Active",
                                "routes": {
                                    "prefix": {
                                        "15.1.1.0/24": {
                                            "index": {
                                                1: {
                                                    "path": "200 33299 51178 47751 {27016}",
                                                    "next_hop": "20.1.5.5",
                                                    "status_codes": "*>",
                                                    "weight": "0",
                                                    "metric": "2219",
                                                    "origin_codes": "e"
                                                }
                                            }
                                        },
                                        "15.1.2.0/24": {
                                            "index": {
                                                1: {
                                                    "path": "200 33299 51178 47751 {27016}",
                                                    "next_hop": "20.1.5.5",
                                                    "status_codes": "*>",
                                                    "weight": "0",
                                                    "metric": "2219",
                                                    "origin_codes": "e"
                                                }
                                            }
                                        }
                                    }
                                },
                                "state": "Active",
                                "rd_version": 63}}}}}}}

    golden_output = {'execute.return_value': '''
    
     Neighbor not found

    BGP instance 0: 'default'
    =========================

    VRF: VRF1
    ---------

    VRF: VRF2
    ---------
    BGP VRF VRF2, state: Active
    BGP Route Distinguisher: 200:2
    VRF ID: 0x60000002
    BGP router identifier 11.11.11.11, local AS number 100
    Non-stop routing is enabled
    BGP table state: Active
    Table ID: 0xe0000011   RD version: 63
    BGP main routing table version 63
    BGP NSR Initial initsync version 11 (Reached)
    BGP NSR/ISSU Sync-Group versions 0/0

    Status codes: s suppressed, d damped, h history, * valid, > best
                  i - internal, r RIB-failure, S stale, N Nexthop-discard
    Origin codes: i - IGP, e - EGP, ? - incomplete
       Network            Next Hop            Metric LocPrf Weight Path
    Route Distinguisher: 200:2 (default for vrf VRF2)
    *> 15.1.1.0/24        20.1.5.5              2219             0 200 33299 51178 47751 {27016} e
    *> 15.1.2.0/24        20.1.5.5              2219             0 200 33299 51178 47751 {27016} e
    
    Processed 2 prefixes, 2 paths

        '''}

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowBgpInstanceNeighborsRoutes(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(neighbor='20.1.5.5', vrf='vrf')

    def test_golden(self):
        self.dev = Mock(**self.golden_output)
        obj = ShowBgpInstanceNeighborsRoutes(device=self.dev)
        parsed_output = obj.parse(neighbor='20.1.5.5', vrf='vrf')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# =====================================================================
# Unit test for 'show bgp instance all all all neighbors <WORD> routes'
# =====================================================================

class test_show_bgp_instance_all_all_all_neighbors_routes(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
       "instance": {
          "default": {
               "vrf": {
                    "default": {
                         "address_family": {
                              "vpnv4 unicast RD 400:1": {
                                   "rd_version": 0,
                                   "route_identifier": "1.1.1.1",
                                   "routes": {
                                        "prefix": {
                                             "46.2.2.0/24": {
                                                  "index": {
                                                       1: {
                                                            "path": "400 33299 51178 47751 {27016}",
                                                            "status_codes": "*i",
                                                            "locprf": "100",
                                                            "weight": "0",
                                                            "next_hop": "4.4.4.4",
                                                            "metric": "2219",
                                                            "origin_codes": "e"
                                                       }
                                                  }
                                             }
                                        }
                                   },
                                   "non_stop_routing": True,
                                   "scan_interval": 60,
                                   "tbl_ver": 43,
                                   "nsr_issu_sync_group_versions": "0/0",
                                   "local_as": 100,
                                   "nsr_initial_initsync_version": "11 (Reached)",
                                   "table_id": "0x0",
                                   "table_state": "Active",
                                   "processed_prefixes": 2,
                                   "generic_scan_interval": 60,
                                   "processed_paths": 2
                              },
                              "vpnv6 unicast RD 400:1": {
                                   "rd_version": 0,
                                   "route_identifier": "1.1.1.1",
                                   "routes": {
                                        "prefix": {
                                             "646:22:22::/64": {
                                                  "index": {
                                                       1: {
                                                            "path": "400 33299 51178 47751 {27016}",
                                                            "status_codes": "*i",
                                                            "locprf": "100",
                                                            "weight": "0",
                                                            "next_hop": "4.4.4.4",
                                                            "metric": "2219",
                                                            "origin_codes": "e"
                                                       }
                                                  }
                                             }
                                        }
                                   },
                                   "non_stop_routing": True,
                                   "scan_interval": 60,
                                   "tbl_ver": 43,
                                   "nsr_issu_sync_group_versions": "0/0",
                                   "local_as": 100,
                                   "nsr_initial_initsync_version": "11 (Reached)",
                                   "table_id": "0x0",
                                   "table_state": "Active",
                                   "processed_prefixes": 3,
                                   "generic_scan_interval": 60,
                                   "processed_paths": 3
                              },
                              "vpnv4 unicast RD 300:1": {
                                   "rd_version": 0,
                                   "route_identifier": "1.1.1.1",
                                   "routes": {
                                        "prefix": {
                                             "46.1.1.0/24": {
                                                  "index": {
                                                       1: {
                                                            "path": "300 33299 51178 47751 {27016}",
                                                            "status_codes": "*i",
                                                            "locprf": "100",
                                                            "weight": "0",
                                                            "next_hop": "4.4.4.4",
                                                            "metric": "2219",
                                                            "origin_codes": "e"
                                                       }
                                                  }
                                             }
                                        }
                                   },
                                   "non_stop_routing": True,
                                   "scan_interval": 60,
                                   "tbl_ver": 43,
                                   "nsr_issu_sync_group_versions": "0/0",
                                   "local_as": 100,
                                   "nsr_initial_initsync_version": "11 (Reached)",
                                   "table_id": "0x0",
                                   "table_state": "Active",
                                   "generic_scan_interval": 60
                              },
                              "vpnv6 unicast RD 300:1": {
                                   "rd_version": 0,
                                   "route_identifier": "1.1.1.1",
                                   "routes": {
                                        "prefix": {
                                             "646:11:11::/64": {
                                                  "index": {
                                                       1: {
                                                            "path": "300 33299 51178 47751 {27016}",
                                                            "status_codes": "*i",
                                                            "locprf": "100",
                                                            "weight": "0",
                                                            "next_hop": "4.4.4.4",
                                                            "metric": "2219",
                                                            "origin_codes": "e"
                                                       }
                                                  }
                                             },
                                             "646:11:11:1::/64": {
                                                  "index": {
                                                       1: {
                                                            "path": "300 33299 51178 47751 {27016}",
                                                            "status_codes": "*i",
                                                            "locprf": "100",
                                                            "weight": "0",
                                                            "next_hop": "4.4.4.4",
                                                            "metric": "2219",
                                                            "origin_codes": "e"
                                                       }
                                                  }
                                             }
                                        }
                                   },
                                   "non_stop_routing": True,
                                   "scan_interval": 60,
                                   "tbl_ver": 43,
                                   "nsr_issu_sync_group_versions": "0/0",
                                   "local_as": 100,
                                   "nsr_initial_initsync_version": "11 (Reached)",
                                   "table_id": "0x0",
                                   "table_state": "Active",
                                   "generic_scan_interval": 60
                              }
                         }
                    }
               }
          }
     }
    }

    golden_output = {'execute.return_value': '''
        BGP instance 0: 'default'
        =========================

        Address Family: VPNv4 Unicast
        -----------------------------

        BGP router identifier 1.1.1.1, local AS number 100
        BGP generic scan interval 60 secs
        Non-stop routing is enabled
        BGP table state: Active
        Table ID: 0x0   RD version: 0
        BGP main routing table version 43
        BGP NSR Initial initsync version 11 (Reached)
        BGP NSR/ISSU Sync-Group versions 0/0
        BGP scan interval 60 secs

        Status codes: s suppressed, d damped, h history, * valid, > best
                      i - internal, r RIB-failure, S stale, N Nexthop-discard
        Origin codes: i - IGP, e - EGP, ? - incomplete
           Network            Next Hop            Metric LocPrf Weight Path
        Route Distinguisher: 300:1
        * i46.1.1.0/24        4.4.4.4               2219    100      0 300 33299 51178 47751 {27016} e
        
        Route Distinguisher: 400:1
        * i46.2.2.0/24        4.4.4.4               2219    100      0 400 33299 51178 47751 {27016} e
        

        Processed 2 prefixes, 2 paths

        Address Family: VPNv6 Unicast
        -----------------------------

        BGP router identifier 1.1.1.1, local AS number 100
        BGP generic scan interval 60 secs
        Non-stop routing is enabled
        BGP table state: Active
        Table ID: 0x0   RD version: 0
        BGP main routing table version 43
        BGP NSR Initial initsync version 11 (Reached)
        BGP NSR/ISSU Sync-Group versions 0/0
        BGP scan interval 60 secs

        Status codes: s suppressed, d damped, h history, * valid, > best
                      i - internal, r RIB-failure, S stale, N Nexthop-discard
        Origin codes: i - IGP, e - EGP, ? - incomplete
           Network            Next Hop            Metric LocPrf Weight Path
        Route Distinguisher: 300:1
        * i646:11:11::/64     4.4.4.4               2219    100      0 300 33299 51178 47751 {27016} e
        * i646:11:11:1::/64   4.4.4.4               2219    100      0 300 33299 51178 47751 {27016} e
        Route Distinguisher: 400:1
        * i646:22:22::/64     4.4.4.4               2219    100      0 400 33299 51178 47751 {27016} e
        

        Processed 3 prefixes, 3 paths


        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowBgpInstanceNeighborsRoutes(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(neighbor='3.3.3.3', vrf='all')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpInstanceNeighborsRoutes(device=self.device)
        parsed_output = obj.parse(neighbor='3.3.3.3', vrf='all')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


# =====================================================
# Unit test for 'show bgp instance all all all summary'
# =====================================================

class test_show_bgp_instance_all_all_all_summary(unittest.TestCase):
    
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "instance": {
            "default": {
                "vrf": {
                    "default": {
                        "neighbor": {
                            "2.2.2.2": {
                                "remote_as": 100,
                                "address_family": {
                                    "vpnv4 unicast": {
                                        "msg_rcvd": 59,
                                        "output_queue": 0,
                                        "state_pfxrcd": '10',
                                        "spk": 0,
                                        "up_down": "00:50:38",
                                        "tbl_ver": 43,
                                        "msg_sent": 56,
                                        "input_queue": 0},
                                    "vpnv6 unicast": {
                                        "msg_rcvd": 59,
                                        "output_queue": 0,
                                        "state_pfxrcd": '10',
                                        "spk": 0,
                                        "up_down": "00:50:38",
                                        "tbl_ver": 43,
                                        "msg_sent": 56,
                                        "input_queue": 0}}},
                            "3.3.3.3": {
                                "remote_as": 100,
                                "address_family": {
                                    "vpnv4 unicast": {
                                        "msg_rcvd": 68,
                                        "output_queue": 0,
                                        "state_pfxrcd": '10',
                                        "spk": 0,
                                        "up_down": "00:47:11",
                                        "tbl_ver": 43,
                                        "msg_sent": 58,
                                        "input_queue": 0},
                                    "vpnv6 unicast": {
                                        "msg_rcvd": 68,
                                        "output_queue": 0,
                                        "state_pfxrcd": '10',
                                        "spk": 0,
                                        "up_down": "00:47:11",
                                        "tbl_ver": 43,
                                        "msg_sent": 58,
                                        "input_queue": 0}}}},
                        "address_family": {
                            "vpnv4 unicast": {
                                "non_stop_routing": "enabled",
                                "table_id": "0x0",
                                "nsr_initial_init_ver_status": "Reached",
                                "operation_mode": "STANDALONE ",
                                "bgp_table_version": 43,
                                "router_id": "1.1.1.1",
                                "nsr_issu_sync_group_versions": "0/0",
                                "local_as": 100,
                                "nsr_initial_initsync_version": 11,
                                "process": {
                                    "Speaker": {
                                        "rcvtblver": 43,
                                        "labelver": 43,
                                        "sendtblver": 43,
                                        "brib_rib": 43,
                                        "standbyver": 0,
                                        "importver": 43}},
                                "generic_scan_interval": 60,
                                "table_state": "Active",
                                "rd_version": 0},
                            "vpnv6 unicast": {
                                "non_stop_routing": "enabled",
                                "table_id": "0x0",
                                "nsr_initial_init_ver_status": "Reached",
                                "operation_mode": "STANDALONE ",
                                "bgp_table_version": 43,
                                "router_id": "1.1.1.1",
                                "nsr_issu_sync_group_versions": "0/0",
                                "local_as": 100,
                                "nsr_initial_initsync_version": 11,
                                "process": {
                                    "Speaker": {
                                        "rcvtblver": 43,
                                        "labelver": 43,
                                        "sendtblver": 43,
                                        "brib_rib": 43,
                                        "standbyver": 0,
                                        "importver": 43}},
                                "generic_scan_interval": 60,
                                "table_state": "Active",
                                "rd_version": 0}}}}}}}

    golden_output = {'execute.return_value': '''
    
        BGP instance 0: 'default'
        =========================

        Address Family: VPNv4 Unicast
        -----------------------------

        BGP router identifier 1.1.1.1, local AS number 100
        BGP generic scan interval 60 secs
        Non-stop routing is enabled
        BGP table state: Active
        Table ID: 0x0   RD version: 0
        BGP main routing table version 43
        BGP NSR Initial initsync version 11 (Reached)
        BGP NSR/ISSU Sync-Group versions 0/0
        BGP scan interval 60 secs

        BGP is operating in STANDALONE mode.


        Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
        Speaker              43         43         43         43          43           0

        Neighbor        Spk    AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
        2.2.2.2           0   100      59      56       43    0    0 00:50:38         10
        3.3.3.3           0   100      68      58       43    0    0 00:47:11         10


        Address Family: VPNv6 Unicast
        -----------------------------

        BGP router identifier 1.1.1.1, local AS number 100
        BGP generic scan interval 60 secs
        Non-stop routing is enabled
        BGP table state: Active
        Table ID: 0x0   RD version: 0
        BGP main routing table version 43
        BGP NSR Initial initsync version 11 (Reached)
        BGP NSR/ISSU Sync-Group versions 0/0
        BGP scan interval 60 secs

        BGP is operating in STANDALONE mode.


        Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
        Speaker              43         43         43         43          43           0

        Neighbor        Spk    AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
        2.2.2.2           0   100      59      56       43    0    0 00:50:38         10
        3.3.3.3           0   100      68      58       43    0    0 00:47:11         10
        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_instance_summary_obj = ShowBgpInstanceSummary(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_instance_summary_obj.parse(vrf_type='all')

    def test_golden(self):
       self.maxDiff = None
       self.device = Mock(**self.golden_output)
       bgp_instance_summary_obj = ShowBgpInstanceSummary(device=self.device)
       parsed_output = bgp_instance_summary_obj.parse(vrf_type='all')
       self.assertEqual(parsed_output,self.golden_parsed_output)


# =====================================================
# Unit test for 'show bgp instance all vrf all summary'
# =====================================================

class test_show_bgp_instance_all_vrf_all_summary(unittest.TestCase):
    
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "instance": {
            "default": {
                "vrf": {
                    "vrf2": {
                        "neighbor": {
                            "20.1.5.5": {
                                "remote_as": 200,
                                "address_family": {
                                    "ipv4 unicast RD 200:2": {
                                        "tbl_ver": 63,
                                        "msg_rcvd": 58,
                                        "msg_sent": 62,
                                        "route_distinguisher": "200:2",
                                        "spk": 0,
                                        "up_down": "00:01:12",
                                        "state_pfxrcd": '5',
                                        "output_queue": 0,
                                        "input_queue": 0}}}},
                        "address_family": {
                            "ipv4 unicast RD 200:2": {
                                "local_as": 100,
                                "operation_mode": "STANDALONE ",
                                "table_id": "0xe0000011",
                                "vrf_state": "active",
                                "route_distinguisher": "200:2",
                                "bgp_table_version": 63,
                                "nsr_initial_initsync_version": 11,
                                "table_state": "Active",
                                "vrf_id": "0x60000002",
                                "router_id": "11.11.11.11",
                                "bgp_vrf": "vrf2",
                                "non_stop_routing": "enabled",
                                "nsr_issu_sync_group_versions": "0/0",
                                "nsr_initial_init_ver_status": "Reached",
                                "process": {
                                    "Speaker": {
                                        "importver": 63,
                                        "labelver": 63,
                                        "standbyver": 0,
                                        "rcvtblver": 63,
                                        "brib_rib": 63,
                                        "sendtblver": 63}},
                                "rd_version": 63}}},
                    "vrf1": {
                        "neighbor": {
                            "10.1.5.5": {
                                "remote_as": 200,
                                "address_family": {
                                    "ipv4 unicast RD 200:1": {
                                        "tbl_ver": 63,
                                        "msg_rcvd": 60,
                                        "msg_sent": 62,
                                        "route_distinguisher": "200:1",
                                        "spk": 0,
                                        "up_down": "00:57:32",
                                        "state_pfxrcd": '0',
                                        "output_queue": 0,
                                        "input_queue": 0}}}},
                        "address_family": {
                            "ipv4 unicast RD 200:1": {
                                "local_as": 100,
                                "operation_mode": "STANDALONE ",
                                "table_id": "0xe0000010",
                                "vrf_state": "active",
                                "route_distinguisher": "200:1",
                                "bgp_table_version": 63,
                                "nsr_initial_initsync_version": 11,
                                "table_state": "Active",
                                "vrf_id": "0x60000001",
                                "router_id": "11.11.11.11",
                                "bgp_vrf": "vrf1",
                                "non_stop_routing": "enabled",
                                "nsr_issu_sync_group_versions": "0/0",
                                "nsr_initial_init_ver_status": "Reached",
                                "process": {
                                    "Speaker": {
                                        "importver": 63,
                                        "labelver": 63,
                                        "standbyver": 0,
                                        "rcvtblver": 63,
                                        "brib_rib": 63,
                                        "sendtblver": 63}},
                                "rd_version": 63}}}}}}}

    golden_output = {'execute.return_value': '''
        BGP instance 0: 'default'
        =========================

        VRF: VRF1
        ---------
        BGP VRF VRF1, state: Active
        BGP Route Distinguisher: 200:1
        VRF ID: 0x60000001
        BGP router identifier 11.11.11.11, local AS number 100
        Non-stop routing is enabled
        BGP table state: Active
        Table ID: 0xe0000010   RD version: 63
        BGP main routing table version 63
        BGP NSR Initial initsync version 11 (Reached)
        BGP NSR/ISSU Sync-Group versions 0/0

        BGP is operating in STANDALONE mode.


        Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
        Speaker              63         63         63         63          63           0

        Neighbor        Spk    AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
        10.1.5.5          0   200      60      62       63    0    0 00:57:32          0


        VRF: VRF2
        ---------
        BGP VRF VRF2, state: Active
        BGP Route Distinguisher: 200:2
        VRF ID: 0x60000002
        BGP router identifier 11.11.11.11, local AS number 100
        Non-stop routing is enabled
        BGP table state: Active
        Table ID: 0xe0000011   RD version: 63
        BGP main routing table version 63
        BGP NSR Initial initsync version 11 (Reached)
        BGP NSR/ISSU Sync-Group versions 0/0

        BGP is operating in STANDALONE mode.


        Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
        Speaker              63         63         63         63          63           0

        Neighbor        Spk    AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
        20.1.5.5          0   200      58      62       63    0    0 00:01:12          5
        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_instance_summary_obj = ShowBgpInstanceSummary(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_instance_summary_obj.parse(vrf_type='vrf')

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        bgp_instance_summary_obj = ShowBgpInstanceSummary(device=self.device)
        parsed_output = bgp_instance_summary_obj.parse(vrf_type='vrf')
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
