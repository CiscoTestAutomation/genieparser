
# Python
import unittest
from unittest.mock import Mock
import xml.etree.ElementTree as ET

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# YANG Parser
from genie.libs.parser.yang.bgp_openconfig_yang import BgpOpenconfigYang


# =======================================
#  Unit test for 'GET' operation on IOSXR
# =======================================

class test_yang_bgp_iosxr(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'bgp_pid': 100,
        'total_paths': 0,
        'total_prefixes': 0,
        'vrf': 
            {'default': 
                {'address_family': 
                    {'idx:l3vpn-ipv4-unicast': 
                        {'enabled': True,
                        'total_paths': 0,
                        'total_prefixes': 0},
                    'idx:l3vpn-ipv6-unicast': 
                        {'enabled': True,
                        'total_paths': 0,
                        'total_prefixes': 0}},
                'neighbor': 
                    {'10.16.2.2': 
                        {'address_family': 
                            {'idx:l3vpn-ipv4-unicast': 
                                {'active': False,
                                'enabled': True,
                                'prefixes_received': 0,
                                'prefixes_sent': 0},
                            'idx:l3vpn-ipv6-unicast': 
                                {'active': False,
                                'enabled': True,
                                'prefixes_received': 0,
                                'prefixes_sent': 0}},
                        'bgp_neighbor_counters': 
                            {'messages': 
                                {'received': 
                                    {'notifications': 0,
                                    'updates': 0},
                                'sent': 
                                    {'notifications': 0,
                                    'updates': 0}}},
                        'bgp_session_transport': 
                            {'transport': 
                                {'foreign_host': '0',
                                'foreign_port': '10.16.2.2',
                                'local_host': 'Loopback0',
                                'local_port': '0'}},
                        'graceful_restart_restart_time': 120,
                        'holdtime': 180,
                        'input_queue': 0,
                        'output_queue': 0,
                        'remote_as': 100,
                        'session_state': 'idle'},
                    '10.36.3.3': 
                        {'address_family': 
                            {'idx:l3vpn-ipv4-unicast': 
                                {'active': False,
                                'enabled': True,
                                'prefixes_received': 0,
                                'prefixes_sent': 0},
                            'idx:l3vpn-ipv6-unicast': 
                                {'active': False,
                                'enabled': True,
                                'prefixes_received': 0,
                                'prefixes_sent': 0}},
                        'bgp_neighbor_counters': 
                            {'messages': 
                                {'received': 
                                    {'notifications': 0,
                                    'updates': 0},
                                'sent': 
                                    {'notifications': 0,
                                    'updates': 0}}},
                        'bgp_session_transport': 
                            {'transport': 
                                {'foreign_host': '0',
                                'foreign_port': '10.36.3.3',
                                'local_host': 'Loopback0',
                                'local_port': '0'}},
                        'graceful_restart_restart_time': 120,
                        'holdtime': 180,
                        'input_queue': 0,
                        'output_queue': 0,
                        'remote_as': 100,
                        'session_state': 'idle'}},
                'router_id': '10.4.1.1'}}}

    class etree_holder():
        def __init__(self):
            self.data_ele = ET.fromstring('''
                 <data>
                  <bgp xmlns="http://openconfig.net/yang/bgp">
                   <global>
                    <config>
                     <as>100</as>
                     <router-id>10.4.1.1</router-id>
                    </config>
                    <state>
                     <as>100</as>
                     <router-id>10.4.1.1</router-id>
                     <total-paths>0</total-paths>
                     <total-prefixes>0</total-prefixes>
                    </state>
                    <afi-safis>
                     <afi-safi>
                      <afi-safi-name xmlns:idx="http://openconfig.net/yang/bgp-types">idx:l3vpn-ipv4-unicast</afi-safi-name>
                      <config>
                       <afi-safi-name xmlns:idx="http://openconfig.net/yang/bgp-types">idx:l3vpn-ipv4-unicast</afi-safi-name>
                       <enabled>true</enabled>
                      </config>
                      <state>
                       <afi-safi-name xmlns:idx="http://openconfig.net/yang/bgp-types">idx:l3vpn-ipv4-unicast</afi-safi-name>
                       <enabled>true</enabled>
                       <total-paths>0</total-paths>
                       <total-prefixes>0</total-prefixes>
                      </state>
                     </afi-safi>
                     <afi-safi>
                      <afi-safi-name xmlns:idx="http://openconfig.net/yang/bgp-types">idx:l3vpn-ipv6-unicast</afi-safi-name>
                      <config>
                       <afi-safi-name xmlns:idx="http://openconfig.net/yang/bgp-types">idx:l3vpn-ipv6-unicast</afi-safi-name>
                       <enabled>true</enabled>
                      </config>
                      <state>
                       <afi-safi-name xmlns:idx="http://openconfig.net/yang/bgp-types">idx:l3vpn-ipv6-unicast</afi-safi-name>
                       <enabled>true</enabled>
                       <total-paths>0</total-paths>
                       <total-prefixes>0</total-prefixes>
                      </state>
                     </afi-safi>
                    </afi-safis>
                   </global>
                   <neighbors>
                    <neighbor>
                     <neighbor-address>10.16.2.2</neighbor-address>
                     <config>
                      <neighbor-address>10.16.2.2</neighbor-address>
                      <peer-as>100</peer-as>
                     </config>
                     <state>
                      <neighbor-address>10.16.2.2</neighbor-address>
                      <peer-as>100</peer-as>
                      <queues>
                       <input>0</input>
                       <output>0</output>
                      </queues>
                      <session-state>IDLE</session-state>
                      <messages>
                       <sent>
                        <NOTIFICATION>0</NOTIFICATION>
                        <UPDATE>0</UPDATE>
                       </sent>
                       <received>
                        <NOTIFICATION>0</NOTIFICATION>
                        <UPDATE>0</UPDATE>
                       </received>
                      </messages>
                     </state>
                     <transport>
                      <config>
                       <local-address>Loopback0</local-address>
                      </config>
                      <state>
                       <local-address>Loopback0</local-address>
                       <local-port>0</local-port>
                       <remote-address>10.16.2.2</remote-address>
                       <remote-port>0</remote-port>
                      </state>
                     </transport>
                     <afi-safis>
                      <afi-safi>
                       <afi-safi-name xmlns:idx="http://openconfig.net/yang/bgp-types">idx:l3vpn-ipv4-unicast</afi-safi-name>
                       <config>
                        <afi-safi-name xmlns:idx="http://openconfig.net/yang/bgp-types">idx:l3vpn-ipv4-unicast</afi-safi-name>
                        <enabled>true</enabled>
                       </config>
                       <state>
                        <afi-safi-name xmlns:idx="http://openconfig.net/yang/bgp-types">idx:l3vpn-ipv4-unicast</afi-safi-name>
                        <enabled>true</enabled>
                        <active>false</active>
                        <prefixes>
                         <received>0</received>
                         <sent>0</sent>
                        </prefixes>
                       </state>
                      </afi-safi>
                      <afi-safi>
                       <afi-safi-name xmlns:idx="http://openconfig.net/yang/bgp-types">idx:l3vpn-ipv6-unicast</afi-safi-name>
                       <config>
                        <afi-safi-name xmlns:idx="http://openconfig.net/yang/bgp-types">idx:l3vpn-ipv6-unicast</afi-safi-name>
                        <enabled>true</enabled>
                       </config>
                       <state>
                        <afi-safi-name xmlns:idx="http://openconfig.net/yang/bgp-types">idx:l3vpn-ipv6-unicast</afi-safi-name>
                        <enabled>true</enabled>
                        <active>false</active>
                        <prefixes>
                         <received>0</received>
                         <sent>0</sent>
                        </prefixes>
                       </state>
                      </afi-safi>
                     </afi-safis>
                     <timers>
                      <state>
                       <negotiated-hold-time>180</negotiated-hold-time>
                      </state>
                     </timers>
                     <graceful-restart>
                      <state>
                       <peer-restart-time>120</peer-restart-time>
                      </state>
                     </graceful-restart>
                    </neighbor>
                    <neighbor>
                     <neighbor-address>10.36.3.3</neighbor-address>
                     <config>
                      <neighbor-address>10.36.3.3</neighbor-address>
                      <peer-as>100</peer-as>
                     </config>
                     <state>
                      <neighbor-address>10.36.3.3</neighbor-address>
                      <peer-as>100</peer-as>
                      <queues>
                       <input>0</input>
                       <output>0</output>
                      </queues>
                      <session-state>IDLE</session-state>
                      <messages>
                       <sent>
                        <NOTIFICATION>0</NOTIFICATION>
                        <UPDATE>0</UPDATE>
                       </sent>
                       <received>
                        <NOTIFICATION>0</NOTIFICATION>
                        <UPDATE>0</UPDATE>
                       </received>
                      </messages>
                     </state>
                     <transport>
                      <config>
                       <local-address>Loopback0</local-address>
                      </config>
                      <state>
                       <local-address>Loopback0</local-address>
                       <local-port>0</local-port>
                       <remote-address>10.36.3.3</remote-address>
                       <remote-port>0</remote-port>
                      </state>
                     </transport>
                     <afi-safis>
                      <afi-safi>
                       <afi-safi-name xmlns:idx="http://openconfig.net/yang/bgp-types">idx:l3vpn-ipv4-unicast</afi-safi-name>
                       <config>
                        <afi-safi-name xmlns:idx="http://openconfig.net/yang/bgp-types">idx:l3vpn-ipv4-unicast</afi-safi-name>
                        <enabled>true</enabled>
                       </config>
                       <state>
                        <afi-safi-name xmlns:idx="http://openconfig.net/yang/bgp-types">idx:l3vpn-ipv4-unicast</afi-safi-name>
                        <enabled>true</enabled>
                        <active>false</active>
                        <prefixes>
                         <received>0</received>
                         <sent>0</sent>
                        </prefixes>
                       </state>
                      </afi-safi>
                      <afi-safi>
                       <afi-safi-name xmlns:idx="http://openconfig.net/yang/bgp-types">idx:l3vpn-ipv6-unicast</afi-safi-name>
                       <config>
                        <afi-safi-name xmlns:idx="http://openconfig.net/yang/bgp-types">idx:l3vpn-ipv6-unicast</afi-safi-name>
                        <enabled>true</enabled>
                       </config>
                       <state>
                        <afi-safi-name xmlns:idx="http://openconfig.net/yang/bgp-types">idx:l3vpn-ipv6-unicast</afi-safi-name>
                        <enabled>true</enabled>
                        <active>false</active>
                        <prefixes>
                         <received>0</received>
                         <sent>0</sent>
                        </prefixes>
                       </state>
                      </afi-safi>
                     </afi-safis>
                     <timers>
                      <state>
                       <negotiated-hold-time>180</negotiated-hold-time>
                      </state>
                     </timers>
                     <graceful-restart>
                      <state>
                       <peer-restart-time>120</peer-restart-time>
                      </state>
                     </graceful-restart>
                    </neighbor>
                   </neighbors>
                  </bgp>
                 </data>
                ''')

    yang_output = etree_holder()

    def test_bgp_openconfig_yang_iosxr(self):
        self.maxDiff = None
        self.device = Mock()
        # YANG output
        self.device.get = Mock()
        self.device.get.side_effect = [self.yang_output]
        obj = BgpOpenconfigYang(device=self.device, context='yang')
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ======================================
#  Unit test for 'GET' operation on NXOS
# ======================================

class test_yang_bgp_nxos(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'bgp_pid': 333,
        'use_multiple_paths': 
            {'ebgp_max_paths': 1,
            'ibgp_max_paths': 1},
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4 label unicast': 
                        {'advertise_inactive_routes': False,
                        'ebgp_max_paths': 1,
                        'enabled': True,
                        'graceful_restart': False,
                        'ibgp_max_paths': 1},
                    'ipv4 unicast': 
                        {'advertise_inactive_routes': False,
                        'ebgp_max_paths': 1,
                        'enabled': True,
                        'graceful_restart': False,
                        'ibgp_max_paths': 1},
                    'ipv6 unicast': 
                        {'advertise_inactive_routes': False,
                        'ebgp_max_paths': 1,
                        'enabled': True,
                        'graceful_restart': False,
                        'ibgp_max_paths': 1},
                    'l3vpn ipv4 unicast': 
                        {'advertise_inactive_routes': False,
                        'ebgp_max_paths': 1,
                        'enabled': True,
                        'graceful_restart': False,
                        'ibgp_max_paths': 1},
                    'l3vpn ipv6 unicast': 
                        {'advertise_inactive_routes': False,
                        'ebgp_max_paths': 1,
                        'enabled': True,
                        'graceful_restart': False,
                        'ibgp_max_paths': 1}},
                'graceful_restart': False,
                'graceful_restart_helper_only': False,
                'graceful_restart_restart_time': 120,
                'graceful_restart_stalepath_time': 300,
                'log_neighbor_changes': True,
                'neighbor': 
                    {'10.186.101.1': 
                        {'address_family': 
                            {'ipv4 unicast': 
                                {'enabled': True,
                                'graceful_restart': False,
                                'ipv4_unicast_send_default_route': False},
                            'ipv6 unicast': 
                                {'enabled': True,
                                'graceful_restart': False},
                            'l3vpn ipv4 unicast': 
                                {'enabled': True,
                                'graceful_restart': False},
                            'l3vpn ipv6 unicast': 
                                {'enabled': True,
                                'graceful_restart': False}},
                        'allow_own_as': 0,
                        'holdtime': 180,
                        'keepalive_interval': 60,
                        'minimum_advertisement_interval': 0,
                        'bgp_session_transport': 
                            {'transport': 
                                {'foreign_host': 'unspecified',
                                'foreign_port': '10.186.101.1',
                                'local_host': '0.0.0.0',
                                'local_port': 'unspecified',
                                'passive_mode': 'false'}},
                        'description': 'None',
                        'graceful_restart': False,
                        'graceful_restart_helper_only': False,
                        'graceful_restart_restart_time': 120,
                        'graceful_restart_stalepath_time': 300,
                        'nbr_ebgp_multihop': False,
                        'nbr_ebgp_multihop_max_hop': 0,
                        'peer_group': 'None',
                        'remote_as': 333,
                        'remove_private_as': False,
                        'route_reflector_client': True,
                        'route_reflector_cluster_id': 3,
                        'send_community': 'BOTH'},
                    '10.186.102.1': 
                        {'address_family': 
                            {'ipv4 unicast': 
                                {'enabled': True,
                                'graceful_restart': False},
                            'ipv6 unicast': 
                                {'enabled': True,
                                'graceful_restart': False},
                            'l3vpn ipv4 unicast': 
                                {'enabled': True,
                                'graceful_restart': False},
                            'l3vpn ipv6 unicast': 
                                {'enabled': True,
                                'graceful_restart': False}},
                        'allow_own_as': 0,
                        'holdtime': 180,
                        'keepalive_interval': 60,
                        'minimum_advertisement_interval': 0,
                        'bgp_session_transport': 
                            {'transport': 
                                {'foreign_host': 'unspecified',
                                'foreign_port': '10.186.102.1',
                                'local_host': '0.0.0.0',
                                'local_port': 'unspecified',
                                'passive_mode': 'false'}},
                        'description': 'None',
                        'graceful_restart': False,
                        'graceful_restart_helper_only': False,
                        'graceful_restart_restart_time': 120,
                        'graceful_restart_stalepath_time': 300,
                        'nbr_ebgp_multihop': False,
                        'nbr_ebgp_multihop_max_hop': 0,
                        'peer_group': 'None',
                        'remote_as': 333,
                        'remove_private_as': False,
                        'route_reflector_client': True,
                        'route_reflector_cluster_id': 3,
                        'send_community': 'BOTH'},
                    '10.186.201.1': 
                        {'address_family': 
                            {'ipv4 unicast': 
                                {'enabled': True,
                                'graceful_restart': False,
                                'ipv4_unicast_send_default_route': False},
                            'ipv6 unicast': 
                                {'enabled': True,
                                'graceful_restart': False,
                                'ipv6_unicast_send_default_route': False},
                            'l3vpn ipv4 unicast': 
                                {'enabled': True,
                                'graceful_restart': False},
                            'l3vpn ipv6 unicast': 
                                {'enabled': True,
                                'graceful_restart': False}},
                        'allow_own_as': 0,
                        'holdtime': 180,
                        'keepalive_interval': 60,
                        'minimum_advertisement_interval': 0,
                        'bgp_session_transport': 
                            {'transport': 
                                {'foreign_host': 'unspecified',
                                'foreign_port': '10.186.201.1',
                                'local_host': '0.0.0.0',
                                'local_port': 'unspecified',
                                'passive_mode': 'false'}},
                        'description': 'None',
                        'graceful_restart': False,
                        'graceful_restart_helper_only': False,
                        'graceful_restart_restart_time': 120,
                        'graceful_restart_stalepath_time': 300,
                        'nbr_ebgp_multihop': False,
                        'nbr_ebgp_multihop_max_hop': 0,
                        'peer_group': 'None',
                        'remote_as': 888,
                        'remove_private_as': False,
                        'route_reflector_client': False,
                        'route_reflector_cluster_id': 3,
                        'send_community': 'BOTH'},
                    '10.64.4.4': 
                        {'bgp_session_transport': 
                            {'transport': 
                                {'foreign_host': 'unspecified',
                                'foreign_port': '10.64.4.4',
                                'local_host': '0.0.0.0',
                                'local_port': 'unspecified',
                                'passive_mode': 'false'}},
                        'description': 'None',
                        'graceful_restart': False,
                        'graceful_restart_helper_only': False,
                        'graceful_restart_restart_time': 120,
                        'graceful_restart_stalepath_time': 300,
                        'holdtime': 180,
                        'keepalive_interval': 60,
                        'nbr_ebgp_multihop': False,
                        'nbr_ebgp_multihop_max_hop': 0,
                        'peer_group': 'None',
                        'remove_private_as': False,
                        'route_reflector_cluster_id': 3},
                    '2001:db8:8b05::1002': 
                        {'address_family': 
                            {'ipv4 unicast': 
                                {'enabled': True,
                                'graceful_restart': False,
                                'ipv4_unicast_send_default_route': False}},
                        'allow_own_as': 0,
                        'holdtime': 180,
                        'keepalive_interval': 60,
                        'minimum_advertisement_interval': 0,
                        'bgp_session_transport': 
                            {'transport': 
                                {'foreign_host': 'unspecified',
                                'foreign_port': '2001:db8:8b05::1002',
                                'local_host': '::',
                                'local_port': 'unspecified',
                                'passive_mode': 'false'}},
                        'description': 'None',
                        'graceful_restart': False,
                        'graceful_restart_helper_only': False,
                        'graceful_restart_restart_time': 120,
                        'graceful_restart_stalepath_time': 300,
                        'nbr_ebgp_multihop': False,
                        'nbr_ebgp_multihop_max_hop': 0,
                        'peer_group': 'None',
                        'remote_as': 333,
                        'remove_private_as': False,
                        'route_reflector_client': True,
                        'route_reflector_cluster_id': 3,
                        'send_community': 'BOTH'},
                    '2001:db8:8b05::2002': 
                        {'address_family': 
                            {'ipv4 unicast': 
                                {'enabled': True,
                                'graceful_restart': False,
                                'ipv4_unicast_send_default_route': False},
                            'ipv6 unicast': 
                                {'enabled': True,
                                'graceful_restart': False,
                                'ipv6_unicast_send_default_route': False}},
                        'allow_own_as': 0,
                        'holdtime': 180,
                        'keepalive_interval': 60,
                        'minimum_advertisement_interval': 0,
                        'bgp_session_transport': 
                            {'transport': 
                                {'foreign_host': 'unspecified',
                                'foreign_port': '2001:db8:8b05::2002',
                                'local_host': '::',
                                'local_port': 'unspecified',
                                'passive_mode': 'false'}},
                        'description': 'None',
                        'graceful_restart': False,
                        'graceful_restart_helper_only': False,
                        'graceful_restart_restart_time': 120,
                        'graceful_restart_stalepath_time': 300,
                        'nbr_ebgp_multihop': False,
                        'nbr_ebgp_multihop_max_hop': 0,
                        'peer_group': 'None',
                        'remote_as': 888,
                        'remove_private_as': False,
                        'route_reflector_client': False,
                        'route_reflector_cluster_id': 3,
                        'send_community': 'BOTH'}},
                'router_id': '0.0.0.0'}}}

    class etree_holder():
        def __init__(self):
            self.data_ele = ET.fromstring('''
                <data>
                    <bgp xmlns="http://openconfig.net/yang/bgp">
                        <global>
                            <afi-safis>
                                <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                    <afi-safi-name>none</afi-safi-name>
                                    <config>
                                        <afi-safi-name>none</afi-safi-name>
                                    </config>
                                    <graceful-restart>
                                        <state>
                                            <enabled>false</enabled>
                                        </state>
                                    </graceful-restart>
                                    <state>
                                        <afi-safi-name>none</afi-safi-name>
                                        <enabled>true</enabled>
                                    </state>
                                    <route-selection-options>
                                        <config>
                                            <advertise-inactive-routes>false</advertise-inactive-routes>
                                        </config>
                                        <state>
                                            <advertise-inactive-routes>false</advertise-inactive-routes>
                                        </state>
                                    </route-selection-options>
                                    <use-multiple-paths>
                                        <ebgp>
                                            <config>
                                                <maximum-paths>1</maximum-paths>
                                            </config>
                                            <state>
                                                <maximum-paths>1</maximum-paths>
                                            </state>
                                        </ebgp>
                                        <ibgp>
                                            <config>
                                                <maximum-paths>1</maximum-paths>
                                            </config>
                                            <state>
                                                <maximum-paths>1</maximum-paths>
                                            </state>
                                        </ibgp>
                                    </use-multiple-paths>
                                </afi-safi>
                                <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                    <afi-safi-name>none</afi-safi-name>
                                    <config>
                                        <afi-safi-name>none</afi-safi-name>
                                    </config>
                                    <graceful-restart>
                                        <state>
                                            <enabled>false</enabled>
                                        </state>
                                    </graceful-restart>
                                    <state>
                                        <afi-safi-name>none</afi-safi-name>
                                        <enabled>true</enabled>
                                    </state>
                                    <route-selection-options>
                                        <config>
                                            <advertise-inactive-routes>false</advertise-inactive-routes>
                                        </config>
                                        <state>
                                            <advertise-inactive-routes>false</advertise-inactive-routes>
                                        </state>
                                    </route-selection-options>
                                    <use-multiple-paths>
                                        <ebgp>
                                            <config>
                                                <maximum-paths>1</maximum-paths>
                                            </config>
                                            <state>
                                                <maximum-paths>1</maximum-paths>
                                            </state>
                                        </ebgp>
                                        <ibgp>
                                            <config>
                                                <maximum-paths>1</maximum-paths>
                                            </config>
                                            <state>
                                                <maximum-paths>1</maximum-paths>
                                            </state>
                                        </ibgp>
                                    </use-multiple-paths>
                                </afi-safi>
                                <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                    <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                    <config>
                                        <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                    </config>
                                    <graceful-restart>
                                        <state>
                                            <enabled>false</enabled>
                                        </state>
                                    </graceful-restart>
                                    <state>
                                        <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                        <enabled>true</enabled>
                                    </state>
                                    <route-selection-options>
                                        <config>
                                            <advertise-inactive-routes>false</advertise-inactive-routes>
                                        </config>
                                        <state>
                                            <advertise-inactive-routes>false</advertise-inactive-routes>
                                        </state>
                                    </route-selection-options>
                                    <use-multiple-paths>
                                        <ebgp>
                                            <config>
                                                <maximum-paths>1</maximum-paths>
                                            </config>
                                            <state>
                                                <maximum-paths>1</maximum-paths>
                                            </state>
                                        </ebgp>
                                        <ibgp>
                                            <config>
                                                <maximum-paths>1</maximum-paths>
                                            </config>
                                            <state>
                                                <maximum-paths>1</maximum-paths>
                                            </state>
                                        </ibgp>
                                    </use-multiple-paths>
                                </afi-safi>
                                <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                    <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                    <config>
                                        <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                    </config>
                                    <graceful-restart>
                                        <state>
                                            <enabled>false</enabled>
                                        </state>
                                    </graceful-restart>
                                    <state>
                                        <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                        <enabled>true</enabled>
                                    </state>
                                    <route-selection-options>
                                        <config>
                                            <advertise-inactive-routes>false</advertise-inactive-routes>
                                        </config>
                                        <state>
                                            <advertise-inactive-routes>false</advertise-inactive-routes>
                                        </state>
                                    </route-selection-options>
                                    <use-multiple-paths>
                                        <ebgp>
                                            <config>
                                                <maximum-paths>1</maximum-paths>
                                            </config>
                                            <state>
                                                <maximum-paths>1</maximum-paths>
                                            </state>
                                        </ebgp>
                                        <ibgp>
                                            <config>
                                                <maximum-paths>1</maximum-paths>
                                            </config>
                                            <state>
                                                <maximum-paths>1</maximum-paths>
                                            </state>
                                        </ibgp>
                                    </use-multiple-paths>
                                </afi-safi>
                                <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                    <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                    <config>
                                        <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                    </config>
                                    <graceful-restart>
                                        <state>
                                            <enabled>false</enabled>
                                        </state>
                                    </graceful-restart>
                                    <state>
                                        <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                        <enabled>true</enabled>
                                    </state>
                                    <route-selection-options>
                                        <config>
                                            <advertise-inactive-routes>false</advertise-inactive-routes>
                                        </config>
                                        <state>
                                            <advertise-inactive-routes>false</advertise-inactive-routes>
                                        </state>
                                    </route-selection-options>
                                    <use-multiple-paths>
                                        <ebgp>
                                            <config>
                                                <maximum-paths>1</maximum-paths>
                                            </config>
                                            <state>
                                                <maximum-paths>1</maximum-paths>
                                            </state>
                                        </ebgp>
                                        <ibgp>
                                            <config>
                                                <maximum-paths>1</maximum-paths>
                                            </config>
                                            <state>
                                                <maximum-paths>1</maximum-paths>
                                            </state>
                                        </ibgp>
                                    </use-multiple-paths>
                                </afi-safi>
                                <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                    <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                    <config>
                                        <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                    </config>
                                    <graceful-restart>
                                        <state>
                                            <enabled>false</enabled>
                                        </state>
                                    </graceful-restart>
                                    <state>
                                        <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                        <enabled>true</enabled>
                                    </state>
                                    <route-selection-options>
                                        <config>
                                            <advertise-inactive-routes>false</advertise-inactive-routes>
                                        </config>
                                        <state>
                                            <advertise-inactive-routes>false</advertise-inactive-routes>
                                        </state>
                                    </route-selection-options>
                                    <use-multiple-paths>
                                        <ebgp>
                                            <config>
                                                <maximum-paths>1</maximum-paths>
                                            </config>
                                            <state>
                                                <maximum-paths>1</maximum-paths>
                                            </state>
                                        </ebgp>
                                        <ibgp>
                                            <config>
                                                <maximum-paths>1</maximum-paths>
                                            </config>
                                            <state>
                                                <maximum-paths>1</maximum-paths>
                                            </state>
                                        </ibgp>
                                    </use-multiple-paths>
                                </afi-safi>
                                <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                    <afi-safi-name>none</afi-safi-name>
                                    <config>
                                        <afi-safi-name>none</afi-safi-name>
                                    </config>
                                    <graceful-restart>
                                        <state>
                                            <enabled>false</enabled>
                                        </state>
                                    </graceful-restart>
                                    <state>
                                        <afi-safi-name>none</afi-safi-name>
                                        <enabled>true</enabled>
                                    </state>
                                    <route-selection-options>
                                        <config>
                                            <advertise-inactive-routes>false</advertise-inactive-routes>
                                        </config>
                                        <state>
                                            <advertise-inactive-routes>false</advertise-inactive-routes>
                                        </state>
                                    </route-selection-options>
                                    <use-multiple-paths>
                                        <ebgp>
                                            <config>
                                                <maximum-paths>1</maximum-paths>
                                            </config>
                                            <state>
                                                <maximum-paths>1</maximum-paths>
                                            </state>
                                        </ebgp>
                                        <ibgp>
                                            <config>
                                                <maximum-paths>1</maximum-paths>
                                            </config>
                                            <state>
                                                <maximum-paths>1</maximum-paths>
                                            </state>
                                        </ibgp>
                                    </use-multiple-paths>
                                </afi-safi>
                                <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                    <afi-safi-name>IPV4_LABELED_UNICAST</afi-safi-name>
                                    <config>
                                        <afi-safi-name>IPV4_LABELED_UNICAST</afi-safi-name>
                                    </config>
                                    <graceful-restart>
                                        <state>
                                            <enabled>false</enabled>
                                        </state>
                                    </graceful-restart>
                                    <state>
                                        <afi-safi-name>IPV4_LABELED_UNICAST</afi-safi-name>
                                        <enabled>true</enabled>
                                    </state>
                                    <route-selection-options>
                                        <config>
                                            <advertise-inactive-routes>false</advertise-inactive-routes>
                                        </config>
                                        <state>
                                            <advertise-inactive-routes>false</advertise-inactive-routes>
                                        </state>
                                    </route-selection-options>
                                    <use-multiple-paths>
                                        <ebgp>
                                            <config>
                                                <maximum-paths>1</maximum-paths>
                                            </config>
                                            <state>
                                                <maximum-paths>1</maximum-paths>
                                            </state>
                                        </ebgp>
                                        <ibgp>
                                            <config>
                                                <maximum-paths>1</maximum-paths>
                                            </config>
                                            <state>
                                                <maximum-paths>1</maximum-paths>
                                            </state>
                                        </ibgp>
                                    </use-multiple-paths>
                                </afi-safi>
                            </afi-safis>
                            <graceful-restart>
                                <config>
                                    <enabled>false</enabled>
                                    <helper-only>false</helper-only>
                                    <restart-time>120</restart-time>
                                    <stale-routes-time>300</stale-routes-time>
                                </config>
                                <state>
                                    <enabled>false</enabled>
                                    <helper-only>false</helper-only>
                                    <restart-time>120</restart-time>
                                    <stale-routes-time>300</stale-routes-time>
                                </state>
                            </graceful-restart>
                            <use-multiple-paths xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                <ebgp>
                                    <config>
                                        <maximum-paths>1</maximum-paths>
                                    </config>
                                    <state>
                                        <maximum-paths>1</maximum-paths>
                                    </state>
                                </ebgp>
                                <ibgp>
                                    <config>
                                        <maximum-paths>1</maximum-paths>
                                    </config>
                                    <state>
                                        <maximum-paths>1</maximum-paths>
                                    </state>
                                </ibgp>
                            </use-multiple-paths>
                            <config>
                                <as>333</as>
                                <router-id>0.0.0.0</router-id>
                            </config>
                            <state>
                                <as>333</as>
                                <router-id>0.0.0.0</router-id>
                            </state>
                        </global>
                        <neighbors>
                            <neighbor>
                                <graceful-restart>
                                    <state>
                                        <enabled>false</enabled>
                                        <helper-only>false</helper-only>
                                        <restart-time>120</restart-time>
                                        <stale-routes-time>300</stale-routes-time>
                                    </state>
                                </graceful-restart>
                                <config>
                                    <description/>
                                    <peer-as/>
                                    <remove-private-as/>
                                    <peer-group/>
                                    <neighbor-address>10.64.4.4</neighbor-address>
                                </config>
                                <ebgp-multihop>
                                    <config>
                                        <multihop-ttl>0</multihop-ttl>
                                    </config>
                                    <state>
                                        <enabled>false</enabled>
                                        <multihop-ttl>0</multihop-ttl>
                                    </state>
                                </ebgp-multihop>
                                <logging-options>
                                    <config>
                                        <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                    </config>
                                    <state>
                                        <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                    </state>
                                </logging-options>
                                <route-reflector>
                                    <config>
                                        <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                    </config>
                                    <state>
                                        <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                    </state>
                                </route-reflector>
                                <state>
                                    <description/>
                                    <peer-as/>
                                    <remove-private-as/>
                                    <peer-group/>
                                    <neighbor-address>10.64.4.4</neighbor-address>
                                </state>
                                <timers>
                                    <config>
                                        <hold-time>180</hold-time>
                                        <keepalive-interval>60</keepalive-interval>
                                    </config>
                                    <state>
                                        <hold-time>180</hold-time>
                                        <keepalive-interval>60</keepalive-interval>
                                    </state>
                                </timers>
                                <transport>
                                    <config>
                                        <passive-mode>false</passive-mode>
                                    </config>
                                    <state>
                                        <local-address>0.0.0.0</local-address>
                                        <passive-mode>false</passive-mode>
                                        <local-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</local-port>
                                        <remote-address xmlns="http://openconfig.net/yang/bgp-operational">10.64.4.4</remote-address>
                                        <remote-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</remote-port>
                                    </state>
                                </transport>
                                <neighbor-address>10.64.4.4</neighbor-address>
                            </neighbor>
                            <neighbor>
                                <afi-safis>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>none</afi-safi-name>
                                        <config>
                                            <afi-safi-name>none</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>none</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>none</afi-safi-name>
                                        <config>
                                            <afi-safi-name>none</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>none</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>none</afi-safi-name>
                                        <config>
                                            <afi-safi-name>none</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>none</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                </afi-safis>
                                <as-path-options>
                                    <config>
                                        <allow-own-as>0</allow-own-as>
                                    </config>
                                    <state>
                                        <allow-own-as>0</allow-own-as>
                                    </state>
                                </as-path-options>
                                <graceful-restart>
                                    <state>
                                        <enabled>false</enabled>
                                        <helper-only>false</helper-only>
                                        <restart-time>120</restart-time>
                                        <stale-routes-time>300</stale-routes-time>
                                    </state>
                                </graceful-restart>
                                <config>
                                    <description/>
                                    <peer-as>333</peer-as>
                                    <remove-private-as/>
                                    <send-community>BOTH</send-community>
                                    <peer-group/>
                                    <neighbor-address>10.186.102.1</neighbor-address>
                                </config>
                                <ebgp-multihop>
                                    <config>
                                        <multihop-ttl>0</multihop-ttl>
                                    </config>
                                    <state>
                                        <enabled>false</enabled>
                                        <multihop-ttl>0</multihop-ttl>
                                    </state>
                                </ebgp-multihop>
                                <logging-options>
                                    <config>
                                        <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                    </config>
                                    <state>
                                        <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                    </state>
                                </logging-options>
                                <route-reflector>
                                    <config>
                                        <route-reflector-client>true</route-reflector-client>
                                        <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                    </config>
                                    <state>
                                        <route-reflector-client>true</route-reflector-client>
                                        <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                    </state>
                                </route-reflector>
                                <state>
                                    <description/>
                                    <peer-as>333</peer-as>
                                    <remove-private-as/>
                                    <send-community>BOTH</send-community>
                                    <peer-group/>
                                    <neighbor-address>10.186.102.1</neighbor-address>
                                </state>
                                <timers>
                                    <config>
                                        <hold-time>180</hold-time>
                                        <keepalive-interval>60</keepalive-interval>
                                        <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                    </config>
                                    <state>
                                        <hold-time>180</hold-time>
                                        <keepalive-interval>60</keepalive-interval>
                                        <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                    </state>
                                </timers>
                                <transport>
                                    <config>
                                        <passive-mode>false</passive-mode>
                                    </config>
                                    <state>
                                        <local-address>0.0.0.0</local-address>
                                        <passive-mode>false</passive-mode>
                                        <local-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</local-port>
                                        <remote-address xmlns="http://openconfig.net/yang/bgp-operational">10.186.102.1</remote-address>
                                        <remote-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</remote-port>
                                    </state>
                                </transport>
                                <neighbor-address>10.186.102.1</neighbor-address>
                            </neighbor>
                            <neighbor>
                                <afi-safis>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <ipv6-unicast>
                                            <config>
                                                <send-default-route>false</send-default-route>
                                            </config>
                                            <state>
                                                <send-default-route>false</send-default-route>
                                            </state>
                                        </ipv6-unicast>
                                        <state>
                                            <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>none</afi-safi-name>
                                        <config>
                                            <afi-safi-name>none</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>none</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>none</afi-safi-name>
                                        <config>
                                            <afi-safi-name>none</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>none</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <ipv4-unicast>
                                            <config>
                                                <send-default-route>false</send-default-route>
                                            </config>
                                            <state>
                                                <send-default-route>false</send-default-route>
                                            </state>
                                        </ipv4-unicast>
                                        <state>
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                </afi-safis>
                                <as-path-options>
                                    <config>
                                        <allow-own-as>0</allow-own-as>
                                    </config>
                                    <state>
                                        <allow-own-as>0</allow-own-as>
                                    </state>
                                </as-path-options>
                                <graceful-restart>
                                    <state>
                                        <enabled>false</enabled>
                                        <helper-only>false</helper-only>
                                        <restart-time>120</restart-time>
                                        <stale-routes-time>300</stale-routes-time>
                                    </state>
                                </graceful-restart>
                                <config>
                                    <description/>
                                    <peer-as>888</peer-as>
                                    <remove-private-as/>
                                    <send-community>BOTH</send-community>
                                    <peer-group/>
                                    <neighbor-address>2001:db8:8b05::2002</neighbor-address>
                                </config>
                                <ebgp-multihop>
                                    <config>
                                        <multihop-ttl>0</multihop-ttl>
                                    </config>
                                    <state>
                                        <enabled>false</enabled>
                                        <multihop-ttl>0</multihop-ttl>
                                    </state>
                                </ebgp-multihop>
                                <logging-options>
                                    <config>
                                        <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                    </config>
                                    <state>
                                        <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                    </state>
                                </logging-options>
                                <route-reflector>
                                    <config>
                                        <route-reflector-client>false</route-reflector-client>
                                        <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                    </config>
                                    <state>
                                        <route-reflector-client>false</route-reflector-client>
                                        <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                    </state>
                                </route-reflector>
                                <state>
                                    <description/>
                                    <peer-as>888</peer-as>
                                    <remove-private-as/>
                                    <send-community>BOTH</send-community>
                                    <peer-group/>
                                    <neighbor-address>2001:db8:8b05::2002</neighbor-address>
                                </state>
                                <timers>
                                    <config>
                                        <hold-time>180</hold-time>
                                        <keepalive-interval>60</keepalive-interval>
                                        <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                    </config>
                                    <state>
                                        <hold-time>180</hold-time>
                                        <keepalive-interval>60</keepalive-interval>
                                        <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                    </state>
                                </timers>
                                <transport>
                                    <config>
                                        <passive-mode>false</passive-mode>
                                    </config>
                                    <state>
                                        <local-address>::</local-address>
                                        <passive-mode>false</passive-mode>
                                        <local-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</local-port>
                                        <remote-address xmlns="http://openconfig.net/yang/bgp-operational">2001:db8:8b05::2002</remote-address>
                                        <remote-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</remote-port>
                                    </state>
                                </transport>
                                <neighbor-address>2001:db8:8b05::2002</neighbor-address>
                            </neighbor>
                            <neighbor>
                                <afi-safis>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <ipv4-unicast>
                                            <config>
                                                <send-default-route>false</send-default-route>
                                            </config>
                                            <state>
                                                <send-default-route>false</send-default-route>
                                            </state>
                                        </ipv4-unicast>
                                        <state>
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                </afi-safis>
                                <as-path-options>
                                    <config>
                                        <allow-own-as>0</allow-own-as>
                                    </config>
                                    <state>
                                        <allow-own-as>0</allow-own-as>
                                    </state>
                                </as-path-options>
                                <graceful-restart>
                                    <state>
                                        <enabled>false</enabled>
                                        <helper-only>false</helper-only>
                                        <restart-time>120</restart-time>
                                        <stale-routes-time>300</stale-routes-time>
                                    </state>
                                </graceful-restart>
                                <config>
                                    <description/>
                                    <peer-as>333</peer-as>
                                    <remove-private-as/>
                                    <send-community>BOTH</send-community>
                                    <peer-group/>
                                    <neighbor-address>2001:db8:8b05::1002</neighbor-address>
                                </config>
                                <ebgp-multihop>
                                    <config>
                                        <multihop-ttl>0</multihop-ttl>
                                    </config>
                                    <state>
                                        <enabled>false</enabled>
                                        <multihop-ttl>0</multihop-ttl>
                                    </state>
                                </ebgp-multihop>
                                <logging-options>
                                    <config>
                                        <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                    </config>
                                    <state>
                                        <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                    </state>
                                </logging-options>
                                <route-reflector>
                                    <config>
                                        <route-reflector-client>true</route-reflector-client>
                                        <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                    </config>
                                    <state>
                                        <route-reflector-client>true</route-reflector-client>
                                        <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                    </state>
                                </route-reflector>
                                <state>
                                    <description/>
                                    <peer-as>333</peer-as>
                                    <remove-private-as/>
                                    <send-community>BOTH</send-community>
                                    <peer-group/>
                                    <neighbor-address>2001:db8:8b05::1002</neighbor-address>
                                </state>
                                <timers>
                                    <config>
                                        <hold-time>180</hold-time>
                                        <keepalive-interval>60</keepalive-interval>
                                        <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                    </config>
                                    <state>
                                        <hold-time>180</hold-time>
                                        <keepalive-interval>60</keepalive-interval>
                                        <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                    </state>
                                </timers>
                                <transport>
                                    <config>
                                        <passive-mode>false</passive-mode>
                                    </config>
                                    <state>
                                        <local-address>::</local-address>
                                        <passive-mode>false</passive-mode>
                                        <local-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</local-port>
                                        <remote-address xmlns="http://openconfig.net/yang/bgp-operational">2001:db8:8b05::1002</remote-address>
                                        <remote-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</remote-port>
                                    </state>
                                </transport>
                                <neighbor-address>2001:db8:8b05::1002</neighbor-address>
                            </neighbor>
                            <neighbor>
                                <afi-safis>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>none</afi-safi-name>
                                        <config>
                                            <afi-safi-name>none</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>none</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>none</afi-safi-name>
                                        <config>
                                            <afi-safi-name>none</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>none</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>none</afi-safi-name>
                                        <config>
                                            <afi-safi-name>none</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>none</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <ipv4-unicast>
                                            <config>
                                                <send-default-route>false</send-default-route>
                                            </config>
                                            <state>
                                                <send-default-route>false</send-default-route>
                                            </state>
                                        </ipv4-unicast>
                                        <state>
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                </afi-safis>
                                <as-path-options>
                                    <config>
                                        <allow-own-as>0</allow-own-as>
                                    </config>
                                    <state>
                                        <allow-own-as>0</allow-own-as>
                                    </state>
                                </as-path-options>
                                <graceful-restart>
                                    <state>
                                        <enabled>false</enabled>
                                        <helper-only>false</helper-only>
                                        <restart-time>120</restart-time>
                                        <stale-routes-time>300</stale-routes-time>
                                    </state>
                                </graceful-restart>
                                <config>
                                    <description/>
                                    <peer-as>333</peer-as>
                                    <remove-private-as/>
                                    <send-community>BOTH</send-community>
                                    <peer-group/>
                                    <neighbor-address>10.186.101.1</neighbor-address>
                                </config>
                                <ebgp-multihop>
                                    <config>
                                        <multihop-ttl>0</multihop-ttl>
                                    </config>
                                    <state>
                                        <enabled>false</enabled>
                                        <multihop-ttl>0</multihop-ttl>
                                    </state>
                                </ebgp-multihop>
                                <logging-options>
                                    <config>
                                        <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                    </config>
                                    <state>
                                        <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                    </state>
                                </logging-options>
                                <route-reflector>
                                    <config>
                                        <route-reflector-client>true</route-reflector-client>
                                        <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                    </config>
                                    <state>
                                        <route-reflector-client>true</route-reflector-client>
                                        <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                    </state>
                                </route-reflector>
                                <state>
                                    <description/>
                                    <peer-as>333</peer-as>
                                    <remove-private-as/>
                                    <send-community>BOTH</send-community>
                                    <peer-group/>
                                    <neighbor-address>10.186.101.1</neighbor-address>
                                </state>
                                <timers>
                                    <config>
                                        <hold-time>180</hold-time>
                                        <keepalive-interval>60</keepalive-interval>
                                        <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                    </config>
                                    <state>
                                        <hold-time>180</hold-time>
                                        <keepalive-interval>60</keepalive-interval>
                                        <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                    </state>
                                </timers>
                                <transport>
                                    <config>
                                        <passive-mode>false</passive-mode>
                                    </config>
                                    <state>
                                        <local-address>0.0.0.0</local-address>
                                        <passive-mode>false</passive-mode>
                                        <local-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</local-port>
                                        <remote-address xmlns="http://openconfig.net/yang/bgp-operational">10.186.101.1</remote-address>
                                        <remote-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</remote-port>
                                    </state>
                                </transport>
                                <neighbor-address>10.186.101.1</neighbor-address>
                            </neighbor>
                            <neighbor>
                                <afi-safis>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <ipv6-unicast>
                                            <config>
                                                <send-default-route>false</send-default-route>
                                            </config>
                                            <state>
                                                <send-default-route>false</send-default-route>
                                            </state>
                                        </ipv6-unicast>
                                        <state>
                                            <afi-safi-name>IPV6_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>L3VPN_IPV6_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>none</afi-safi-name>
                                        <config>
                                            <afi-safi-name>none</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>none</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>none</afi-safi-name>
                                        <config>
                                            <afi-safi-name>none</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>none</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>none</afi-safi-name>
                                        <config>
                                            <afi-safi-name>none</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>none</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <ipv4-unicast>
                                            <config>
                                                <send-default-route>false</send-default-route>
                                            </config>
                                            <state>
                                                <send-default-route>false</send-default-route>
                                            </state>
                                        </ipv4-unicast>
                                        <state>
                                            <afi-safi-name>IPV4_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                    <afi-safi xmlns="http://openconfig.net/yang/bgp-multiprotocol">
                                        <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                        <config>
                                            <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                        </config>
                                        <graceful-restart>
                                            <state>
                                                <enabled>false</enabled>
                                            </state>
                                        </graceful-restart>
                                        <state>
                                            <afi-safi-name>L3VPN_IPV4_UNICAST</afi-safi-name>
                                            <enabled>true</enabled>
                                        </state>
                                    </afi-safi>
                                </afi-safis>
                                <as-path-options>
                                    <config>
                                        <allow-own-as>0</allow-own-as>
                                    </config>
                                    <state>
                                        <allow-own-as>0</allow-own-as>
                                    </state>
                                </as-path-options>
                                <graceful-restart>
                                    <state>
                                        <enabled>false</enabled>
                                        <helper-only>false</helper-only>
                                        <restart-time>120</restart-time>
                                        <stale-routes-time>300</stale-routes-time>
                                    </state>
                                </graceful-restart>
                                <config>
                                    <description/>
                                    <peer-as>888</peer-as>
                                    <remove-private-as/>
                                    <send-community>BOTH</send-community>
                                    <peer-group/>
                                    <neighbor-address>10.186.201.1</neighbor-address>
                                </config>
                                <ebgp-multihop>
                                    <config>
                                        <multihop-ttl>0</multihop-ttl>
                                    </config>
                                    <state>
                                        <enabled>false</enabled>
                                        <multihop-ttl>0</multihop-ttl>
                                    </state>
                                </ebgp-multihop>
                                <logging-options>
                                    <config>
                                        <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                    </config>
                                    <state>
                                        <log-neighbor-state-changes>true</log-neighbor-state-changes>
                                    </state>
                                </logging-options>
                                <route-reflector>
                                    <config>
                                        <route-reflector-client>false</route-reflector-client>
                                        <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                    </config>
                                    <state>
                                        <route-reflector-client>false</route-reflector-client>
                                        <route-reflector-cluster-id>3</route-reflector-cluster-id>
                                    </state>
                                </route-reflector>
                                <state>
                                    <description/>
                                    <peer-as>888</peer-as>
                                    <remove-private-as/>
                                    <send-community>BOTH</send-community>
                                    <peer-group/>
                                    <neighbor-address>10.186.201.1</neighbor-address>
                                </state>
                                <timers>
                                    <config>
                                        <hold-time>180</hold-time>
                                        <keepalive-interval>60</keepalive-interval>
                                        <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                    </config>
                                    <state>
                                        <hold-time>180</hold-time>
                                        <keepalive-interval>60</keepalive-interval>
                                        <minimum-advertisement-interval>0</minimum-advertisement-interval>
                                    </state>
                                </timers>
                                <transport>
                                    <config>
                                        <passive-mode>false</passive-mode>
                                    </config>
                                    <state>
                                        <local-address>0.0.0.0</local-address>
                                        <passive-mode>false</passive-mode>
                                        <local-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</local-port>
                                        <remote-address xmlns="http://openconfig.net/yang/bgp-operational">10.186.201.1</remote-address>
                                        <remote-port xmlns="http://openconfig.net/yang/bgp-operational">unspecified</remote-port>
                                    </state>
                                </transport>
                                <neighbor-address>10.186.201.1</neighbor-address>
                            </neighbor>
                        </neighbors>
                    </bgp>
                </data>
                ''')

    yang_output = etree_holder()

    def test_bgp_openconfig_yang_nxos(self):
        self.maxDiff = None
        self.device = Mock()
        # YANG output
        self.device.get = Mock()
        self.device.get.side_effect = [self.yang_output]
        obj = BgpOpenconfigYang(device=self.device, context='yang')
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
