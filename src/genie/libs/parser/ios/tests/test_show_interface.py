#!/bin/env python

import sys
import unittest
from unittest.mock import Mock
from unittest.mock import patch
from textwrap import dedent

ats_mock = Mock()
with patch.dict('sys.modules',
        {'pyats' : ats_mock}, autospec=True):
    import genie.parsergen
    from genie.parsergen import oper_fill
    from genie.parsergen import oper_check
    from genie.parsergen import oper_fill_tabular

import xml.etree.ElementTree as ET

from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.ios.show_interface import \
                                        ShowIpInterfaceBriefPipeVlan,\
                                        ShowInterfaces, ShowIpInterface,\
                                        ShowIpv6Interface, \
                                        ShowInterfacesAccounting, \
                                        ShowIpInterfaceBriefPipeIp, \
                                        ShowInterfacesCounters, \
                                        ShowInterfacesSwitchport, \
                                        ShowInterfacesTrunk, \
                                        ShowInterfacesStats,\
                                        ShowInterfacesDescription, \
                                        ShowInterfacesStatus


class TestShowInterfaceParsergen(unittest.TestCase):

    def test_tabular_parser(self):
        self.showCommandOutput='''
            R1#show ip interface brief 
            Interface              IP-Address      OK? Method Status                Protocol
            GigabitEthernet0/0     10.1.10.20      YES NVRAM  up                    up      
            GigabitEthernet1/0/1   unassigned      YES unset  up                    up         
            GigabitEthernet1/0/10  unassigned      YES unset  down                  down      
            '''

        self.outputDict = {'GigabitEthernet0/0': {'IP-Address': '10.1.10.20',
                                                  'Interface': 'GigabitEthernet0/0',
                                                  'Method': 'NVRAM',
                                                  'OK?': 'YES',
                                                  'Protocol': 'up',
                                                  'Status': 'up'},
                           'GigabitEthernet1/0/1': {'IP-Address': 'unassigned',
                                                    'Interface': 'GigabitEthernet1/0/1',
                                                    'Method': 'unset',
                                                    'OK?': 'YES',
                                                    'Protocol': 'up',
                                                    'Status': 'up'},
                           'GigabitEthernet1/0/10': {'IP-Address': 'unassigned',
                                                     'Interface': 'GigabitEthernet1/0/10',
                                                     'Method': 'unset',
                                                     'OK?': 'YES',
                                                     'Protocol': 'down',
                                                     'Status': 'down'}}

        # Define how device stub will behave when accessed by production parser.
        device_kwargs = {'is_connected.return_value':True,
                         'execute.return_value':dedent(self.showCommandOutput)}
        device1 = Mock(**device_kwargs)
        device1.name='router3'

        result = genie.parsergen.oper_fill_tabular(device=device1,
                                             show_command="show ip interface brief",
                                             refresh_cache=True,
                                             header_fields=
                                                 [ "Interface",
                                                   "IP-Address",
                                                   "OK\?",
                                                   "Method",
                                                   "Status",
                                                   "Protocol" ],
                                             label_fields=
                                                 [ "Interface",
                                                   "IP-Address",
                                                   "OK?",
                                                   "Method",
                                                   "Status",
                                                   "Protocol" ],
                                             index=[0])

        self.assertEqual(result.entries, self.outputDict)
        args, kwargs = device1.execute.call_args
        self.assertTrue('show ip interface brief' in args,
            msg='The expected command was not sent to the router')


#############################################################################
# unitest For Show ip interface
#############################################################################
class TestShowIpInterface(unittest.TestCase):
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value':
    '''
        Embedded-Service-Engine0/0 is administratively down, line protocol is down
          Internet protocol processing disabled
        GigabitEthernet0/0 is up, line protocol is up
          Internet protocol processing disabled
        GigabitEthernet0/0.100 is up, line protocol is up
          Internet address is 10.1.1.10/24
          Broadcast address is 255.255.255.255
          Address determined by non-volatile memory
          MTU is 1500 bytes
          Helper addresses are 10.1.2.129
                               10.1.3.129
          Directed broadcast forwarding is disabled
          Multicast reserved groups joined: 224.0.0.1 224.0.0.2 224.0.0.22 224.0.0.13
              224.0.0.5 224.0.0.6
          Outgoing access list is not set
          Inbound  access list is not set
          Proxy ARP is enabled
          Local Proxy ARP is disabled
          Security level is default
          Split horizon is enabled
          ICMP redirects are never sent
          ICMP unreachables are never sent
          ICMP mask replies are never sent
          IP fast switching is enabled
          IP fast switching on the same interface is enabled
          IP Flow switching is disabled
          IP CEF switching is enabled
          IP CEF switching turbo vector
          IP multicast fast switching is enabled
          IP multicast distributed fast switching is disabled
          IP route-cache flags are Fast, CEF
          Router Discovery is disabled
          IP output packet accounting is disabled
          IP access violation accounting is disabled
          TCP/IP header compression is disabled
          RTP/IP header compression is disabled
          Policy routing is enabled, using route map TRAFFIC_GRE_TUNNEL
          Network address translation is disabled
          BGP Policy Mapping is disabled
          Input features: Input-Flexible-NetFlow, Policy Routing, WCCP, MCI Check
          Output features: CCE Post NAT Classification, Stateful IPS (CCE), Firewall (NAT), Firewall (inspect), MFIB Adjacency, Post-Input-Flexible-NetFlow, Output-Flexible-NetFlow
          IPv4 WCCP Redirect outbound is disabled
          IPv4 WCCP Redirect inbound is enabled
          IPv4 WCCP Redirect exclude is disabled
        GigabitEthernet0/0.101 is up, line protocol is up
          Internet address is 10.1.98.10/24
          Broadcast address is 255.255.255.255
          Address determined by non-volatile memory
          MTU is 1500 bytes
          Helper addresses are 10.1.2.129
                               10.1.3.129
          Directed broadcast forwarding is disabled
          Multicast reserved groups joined: 224.0.0.5 224.0.0.6
          Outgoing access list is not set
          Inbound  access list is not set
          Proxy ARP is enabled
          Local Proxy ARP is disabled
          Security level is default
          Split horizon is enabled
          ICMP redirects are never sent
          ICMP unreachables are never sent
          ICMP mask replies are never sent
          IP fast switching is enabled
          IP fast switching on the same interface is enabled
          IP Flow switching is disabled
          IP CEF switching is enabled
          IP CEF switching turbo vector
          IP multicast fast switching is enabled
          IP multicast distributed fast switching is disabled
          IP route-cache flags are Fast, CEF
          Router Discovery is disabled
          IP output packet accounting is disabled
          IP access violation accounting is disabled
          TCP/IP header compression is disabled
          RTP/IP header compression is disabled
          Policy routing is disabled
          Network address translation is disabled
          BGP Policy Mapping is disabled
          Input features: Input-Flexible-NetFlow, WCCP, MCI Check
          Output features: CCE Post NAT Classification, Stateful IPS (CCE), Firewall (NAT), Firewall (inspect), Post-Input-Flexible-NetFlow, Output-Flexible-NetFlow
          IPv4 WCCP Redirect outbound is disabled
          IPv4 WCCP Redirect inbound is enabled
          IPv4 WCCP Redirect exclude is disabled
        GigabitEthernet0/0.300 is up, line protocol is up
          Internet address is 10.6.100.10/25
          Broadcast address is 255.255.255.255
          Address determined by non-volatile memory
          MTU is 1500 bytes
          Helper addresses are 10.1.2.129
                               10.1.3.129
          Directed broadcast forwarding is disabled
          Multicast reserved groups joined: 224.0.0.5 224.0.0.6
          Outgoing access list is not set
          Inbound  access list is not set
          Proxy ARP is enabled
          Local Proxy ARP is disabled
          Security level is default
          Split horizon is enabled
          ICMP redirects are never sent
          ICMP unreachables are never sent
          ICMP mask replies are never sent
          IP fast switching is enabled
          IP fast switching on the same interface is enabled
          IP Flow switching is disabled
          IP CEF switching is enabled
          IP CEF switching turbo vector
          IP multicast fast switching is enabled
          IP multicast distributed fast switching is disabled
          IP route-cache flags are Fast, CEF
          Router Discovery is disabled
          IP output packet accounting is disabled
          IP access violation accounting is disabled
          TCP/IP header compression is disabled
          RTP/IP header compression is disabled
          Policy routing is enabled, using route map TRAFFIC_GRE_TUNNEL
          Network address translation is disabled
          BGP Policy Mapping is disabled
          Input features: Input-Flexible-NetFlow, Policy Routing, WCCP, MCI Check
          Output features: CCE Post NAT Classification, Stateful IPS (CCE), Firewall (NAT), Firewall (inspect), Post-Input-Flexible-NetFlow, Output-Flexible-NetFlow
          IPv4 WCCP Redirect outbound is disabled
          IPv4 WCCP Redirect inbound is enabled
          IPv4 WCCP Redirect exclude is disabled
        GigabitEthernet0/0.308 is up, line protocol is up
          Internet address is 10.5.101.129/25
          Broadcast address is 255.255.255.255
          Address determined by non-volatile memory
          MTU is 1500 bytes
          Helper addresses are 10.1.2.129
                               10.1.3.129
          Directed broadcast forwarding is disabled
          Multicast reserved groups joined: 224.0.0.5 224.0.0.6
          Outgoing access list is not set
          Inbound  access list is not set
          Proxy ARP is enabled
          Local Proxy ARP is disabled
          Security level is default
          Split horizon is enabled
          ICMP redirects are always sent
          ICMP unreachables are always sent
          ICMP mask replies are never sent
          IP fast switching is enabled
          IP fast switching on the same interface is enabled
          IP Flow switching is disabled
          IP CEF switching is enabled
          IP CEF switching turbo vector
          IP multicast fast switching is enabled
          IP multicast distributed fast switching is disabled
          IP route-cache flags are Fast, CEF
          Router Discovery is disabled
          IP output packet accounting is disabled
          IP access violation accounting is disabled
          TCP/IP header compression is disabled
          RTP/IP header compression is disabled
          Policy routing is disabled
          Network address translation is disabled
          BGP Policy Mapping is disabled
          Input features: Input-Flexible-NetFlow, MCI Check
          Output features: CCE Post NAT Classification, Stateful IPS (CCE), Firewall (NAT), Firewall (inspect), Post-Input-Flexible-NetFlow, Output-Flexible-NetFlow
          IPv4 WCCP Redirect outbound is disabled
          IPv4 WCCP Redirect inbound is disabled
          IPv4 WCCP Redirect exclude is disabled
        GigabitEthernet0/0.324 is up, line protocol is up
          Internet address is 10.2.100.129/25
          Broadcast address is 255.255.255.255
          Address determined by non-volatile memory
          MTU is 1500 bytes
          Helper addresses are 10.160.124.129
                               10.160.125.129
          Directed broadcast forwarding is disabled
          Multicast reserved groups joined: 224.0.0.5 224.0.0.6
          Outgoing access list is not set
          Inbound  access list is not set
          Proxy ARP is enabled
          Local Proxy ARP is disabled
          Security level is default
          Split horizon is enabled
          ICMP redirects are never sent
          ICMP unreachables are never sent
          ICMP mask replies are never sent
          IP fast switching is enabled
          IP fast switching on the same interface is enabled
          IP Flow switching is disabled
          IP CEF switching is enabled
          IP CEF switching turbo vector
          IP multicast fast switching is enabled
          IP multicast distributed fast switching is disabled
          IP route-cache flags are Fast, CEF
          Router Discovery is disabled
          IP output packet accounting is disabled
          IP access violation accounting is disabled
          TCP/IP header compression is disabled
          RTP/IP header compression is disabled
          Policy routing is enabled, using route map TRAFFIC_GRE_TUNNEL
          Network address translation is disabled
          BGP Policy Mapping is disabled
          Input features: Input-Flexible-NetFlow, Policy Routing, MCI Check
          Output features: CCE Post NAT Classification, Stateful IPS (CCE), Firewall (NAT), Firewall (inspect), Post-Input-Flexible-NetFlow, Output-Flexible-NetFlow
          IPv4 WCCP Redirect outbound is disabled
          IPv4 WCCP Redirect inbound is disabled
          IPv4 WCCP Redirect exclude is disabled
        GigabitEthernet0/0.398 is up, line protocol is up
          Internet address is 10.8.10.10/25
          Broadcast address is 255.255.255.255
          Address determined by non-volatile memory
          MTU is 1500 bytes
          Helper address is not set
          Directed broadcast forwarding is disabled
          Multicast reserved groups joined: 224.0.0.5 224.0.0.6
          Outgoing access list is not set
          Inbound  access list is not set
          Proxy ARP is enabled
          Local Proxy ARP is disabled
          Security level is default
          Split horizon is enabled
          ICMP redirects are always sent
          ICMP unreachables are always sent
          ICMP mask replies are never sent
          IP fast switching is enabled
          IP fast switching on the same interface is enabled
          IP Flow switching is disabled
          IP CEF switching is enabled
          IP CEF switching turbo vector
          IP multicast fast switching is enabled
          IP multicast distributed fast switching is disabled
          IP route-cache flags are Fast, CEF
          Router Discovery is disabled
          IP output packet accounting is disabled
          IP access violation accounting is disabled
          TCP/IP header compression is disabled
          RTP/IP header compression is disabled
          Policy routing is disabled
          Network address translation is disabled
          BGP Policy Mapping is disabled
          Input features: Input-Flexible-NetFlow, MCI Check
          Output features: CCE Post NAT Classification, Stateful IPS (CCE), Firewall (NAT), Firewall (inspect), Post-Input-Flexible-NetFlow, Output-Flexible-NetFlow
          IPv4 WCCP Redirect outbound is disabled
          IPv4 WCCP Redirect inbound is disabled
          IPv4 WCCP Redirect exclude is disabled
        ISM0/0 is up, line protocol is up
          Interface is unnumbered. Using address of GigabitEthernet0/0.101 (10.1.98.10)
          Broadcast address is 255.255.255.255
          MTU is 1500 bytes
          Helper address is not set
          Directed broadcast forwarding is disabled
          Multicast reserved groups joined: 224.0.0.5
          Outgoing access list is not set
          Inbound  access list is not set
          Proxy ARP is enabled
          Local Proxy ARP is disabled
          Security level is default
          Split horizon is enabled
          ICMP redirects are always sent
          ICMP unreachables are always sent
          ICMP mask replies are never sent
          IP fast switching is enabled
          IP fast switching on the same interface is disabled
          IP Flow switching is disabled
          IP CEF switching is enabled
          IP CEF switching turbo vector
          IP multicast fast switching is enabled
          IP multicast distributed fast switching is disabled
          IP route-cache flags are Fast, CEF
          Router Discovery is disabled
          IP output packet accounting is disabled
          IP access violation accounting is disabled
          TCP/IP header compression is disabled
          RTP/IP header compression is disabled
          Policy routing is disabled
          Network address translation is disabled
          BGP Policy Mapping is disabled
          Input features: MCI Check
          Output features: CCE Post NAT Classification, Stateful IPS (CCE), Firewall (NAT), Firewall (inspect), Post-Input-Flexible-NetFlow
          IPv4 WCCP Redirect outbound is disabled
          IPv4 WCCP Redirect inbound is disabled
          IPv4 WCCP Redirect exclude is disabled
        GigabitEthernet0/1 is down, line protocol is down
          Internet protocol processing disabled
        GigabitEthernet0/2 is up, line protocol is up
          Internet address is 10.205.34.178/29
          Broadcast address is 255.255.255.255
          Address determined by non-volatile memory
          MTU is 1500 bytes
          Helper address is not set
          Directed broadcast forwarding is disabled
          Outgoing access list is not set
          Inbound  access list is SecureInternet-IPSEC
          Proxy ARP is disabled
          Local Proxy ARP is disabled
          Security level is default
          Split horizon is enabled
          ICMP redirects are never sent
          ICMP unreachables are never sent
          ICMP mask replies are never sent
          IP fast switching is enabled
          IP fast switching on the same interface is disabled
          IP Flow switching is disabled
          IP CEF switching is enabled
          IP CEF switching turbo vector
          IP multicast fast switching is enabled
          IP multicast distributed fast switching is disabled
          IP route-cache flags are Fast, CEF
          Router Discovery is disabled
          IP output packet accounting is disabled
          IP access violation accounting is disabled
          TCP/IP header compression is disabled
          RTP/IP header compression is disabled
          Policy routing is disabled
          Network address translation is disabled
          BGP Policy Mapping is disabled
          Input features: Common Flow Table, Stateful Inspection On Cypher Text, Input-Flexible-NetFlow, Stateless IN IPS (Atomic), Access List, IPSec input classification, Common Flow Table Post VPN, Stateful Inspection On Clear Text, Post Crypto IPS Atomic, MCI Check
          Output features: Common Flow Table, Stateful Inspection, IPSec output classification, CCE Post NAT Classification, Stateful IPS (CCE), Firewall (NAT), Firewall (inspect), IPSec: to crypto engine, Post-encryption output features, Post-Input-Flexible-NetFlow, Output-Flexible-NetFlow
          IPv4 WCCP Redirect outbound is disabled
          IPv4 WCCP Redirect inbound is disabled
          IPv4 WCCP Redirect exclude is disabled
          Outgoing inspection rule is VSO_FW
          Inbound IPS rule is CUSTOMER_AUDIT
        ISM0/1 is up, line protocol is up
          Internet protocol processing disabled
        SM1/0 is up, line protocol is up
          Internet address is 10.1.99.10/24
          Broadcast address is 255.255.255.255
          Address determined by non-volatile memory
          MTU is 1500 bytes
          Helper address is not set
          Directed broadcast forwarding is disabled
          Multicast reserved groups joined: 224.0.0.5 224.0.0.6
          Outgoing access list is not set
          Inbound  access list is not set
          Proxy ARP is enabled
          Local Proxy ARP is disabled
          Security level is default
          Split horizon is enabled
          ICMP redirects are always sent
          ICMP unreachables are always sent
          ICMP mask replies are never sent
          IP fast switching is enabled
          IP fast switching on the same interface is disabled
          IP Flow switching is disabled
          IP CEF switching is enabled
          IP CEF switching turbo vector
          IP multicast fast switching is enabled
          IP multicast distributed fast switching is disabled
          IP route-cache flags are Fast, CEF
          Router Discovery is disabled
          IP output packet accounting is disabled
          IP access violation accounting is disabled
          TCP/IP header compression is disabled
          RTP/IP header compression is disabled
          Policy routing is disabled
          Network address translation is disabled
          BGP Policy Mapping is disabled
          Input features: Input-Flexible-NetFlow, MCI Check
          Output features: CCE Post NAT Classification, Stateful IPS (CCE), Firewall (NAT), Firewall (inspect), Post-Input-Flexible-NetFlow, Output-Flexible-NetFlow
          IPv4 WCCP Redirect outbound is disabled
          IPv4 WCCP Redirect inbound is disabled
          IPv4 WCCP Redirect exclude is enabled
        SM1/1 is up, line protocol is up
          Internet protocol processing disabled
        Async0/1/0 is down, line protocol is down
          Internet protocol processing disabled
        Loopback0 is up, line protocol is up
          Internet address is 10.38.2.9/32
          Broadcast address is 255.255.255.255
          Address determined by non-volatile memory
          MTU is 1514 bytes
          Helper address is not set
          Directed broadcast forwarding is disabled
          Multicast reserved groups joined: 224.0.0.5
          Outgoing access list is not set
          Inbound  access list is not set
          Proxy ARP is enabled
          Local Proxy ARP is disabled
          Security level is default
          Split horizon is enabled
          ICMP redirects are always sent
          ICMP unreachables are always sent
          ICMP mask replies are never sent
          IP fast switching is enabled
          IP fast switching on the same interface is disabled
          IP Flow switching is disabled
          IP CEF switching is enabled
          IP CEF switching turbo vector
          IP Null turbo vector
          IP multicast fast switching is enabled
          IP multicast distributed fast switching is disabled
          IP route-cache flags are Fast, CEF
          Router Discovery is disabled
          IP output packet accounting is disabled
          IP access violation accounting is disabled
          TCP/IP header compression is disabled
          RTP/IP header compression is disabled
          Policy routing is disabled
          Network address translation is disabled
          BGP Policy Mapping is disabled
          Input features: MCI Check
          Output features: CCE Post NAT Classification, Stateful IPS (CCE), Firewall (NAT), Firewall (inspect), Post-Input-Flexible-NetFlow
          IPv4 WCCP Redirect outbound is disabled
          IPv4 WCCP Redirect inbound is disabled
          IPv4 WCCP Redirect exclude is disabled
        Loopback1 is up, line protocol is up
          Internet address is 172.16.219.118/32
          Broadcast address is 255.255.255.255
          Address determined by non-volatile memory
          MTU is 1514 bytes
          Helper address is not set
          Directed broadcast forwarding is disabled
          Outgoing access list is not set
          Inbound  access list is not set
          Proxy ARP is enabled
          Local Proxy ARP is disabled
          Security level is default
          Split horizon is enabled
          ICMP redirects are always sent
          ICMP unreachables are always sent
          ICMP mask replies are never sent
          IP fast switching is enabled
          IP fast switching on the same interface is disabled
          IP Flow switching is disabled
          IP CEF switching is enabled
          IP CEF switching turbo vector
          IP Null turbo vector
          IP multicast fast switching is enabled
          IP multicast distributed fast switching is disabled
          IP route-cache flags are Fast, CEF
          Router Discovery is disabled
          IP output packet accounting is disabled
          IP access violation accounting is disabled
          TCP/IP header compression is disabled
          RTP/IP header compression is disabled
          Policy routing is disabled
          Network address translation is disabled
          BGP Policy Mapping is disabled
          Input features: MCI Check
          Output features: CCE Post NAT Classification, Stateful IPS (CCE), Firewall (NAT), Firewall (inspect), Post-Input-Flexible-NetFlow
          IPv4 WCCP Redirect outbound is disabled
          IPv4 WCCP Redirect inbound is disabled
          IPv4 WCCP Redirect exclude is disabled
        NVI0 is up, line protocol is up
          Interface is unnumbered. Using address of ISM0/0 (0.0.0.0)
          Broadcast address is 255.255.255.255
          MTU is 1514 bytes
          Helper address is not set
          Directed broadcast forwarding is disabled
          Outgoing access list is not set
          Inbound  access list is not set
          Proxy ARP is enabled
          Local Proxy ARP is disabled
          Security level is default
          Split horizon is enabled
          ICMP redirects are always sent
          ICMP unreachables are always sent
          ICMP mask replies are never sent
          IP fast switching is disabled
          IP fast switching on the same interface is disabled
          IP Flow switching is disabled
          IP CEF switching is disabled
          IP Null turbo vector
          IP Null turbo vector
          IP multicast fast switching is enabled
          IP multicast distributed fast switching is disabled
          IP route-cache flags are Fast, CEF
          Router Discovery is disabled
          IP output packet accounting is disabled
          IP access violation accounting is disabled
          TCP/IP header compression is disabled
          RTP/IP header compression is disabled
          Policy routing is disabled
          Network address translation is disabled
          BGP Policy Mapping is disabled
          Input features: MCI Check
          Output features: Post-routing NAT NVI Output, CCE Post NAT Classification, Stateful IPS (CCE), Firewall (NAT), Firewall (inspect), Post-Input-Flexible-NetFlow
          IPv4 WCCP Redirect outbound is disabled
          IPv4 WCCP Redirect inbound is disabled
          IPv4 WCCP Redirect exclude is disabled
        Tunnel20 is up, line protocol is up
          Internet address is 10.145.24.118/30
          Broadcast address is 255.255.255.255
          Address determined by non-volatile memory
          MTU is 1420 bytes
          Helper address is not set
          Directed broadcast forwarding is disabled
          Multicast reserved groups joined: 224.0.0.1 224.0.0.2 224.0.0.22 224.0.0.13
          Outgoing access list is not set
          Inbound  access list is not set
          Proxy ARP is enabled
          Local Proxy ARP is disabled
          Security level is default
          Split horizon is enabled
          ICMP redirects are always sent
          ICMP unreachables are always sent
          ICMP mask replies are never sent
          IP fast switching is enabled
          IP fast switching on the same interface is disabled
          IP Flow switching is disabled
          IP CEF switching is enabled
          IP CEF switching turbo vector
          IP Null turbo vector
          IP multicast fast switching is enabled
          IP multicast distributed fast switching is disabled
          IP route-cache flags are Fast, CEF
          Router Discovery is disabled
          IP output packet accounting is disabled
          IP access violation accounting is disabled
          TCP/IP header compression is disabled
          RTP/IP header compression is disabled
          Policy routing is disabled
          Network address translation is disabled
          BGP Policy Mapping is disabled
          Input features: Input-Flexible-NetFlow, WCCP, MCI Check, TCP Adjust MSS
          Output features: CCE Post NAT Classification, Stateful IPS (CCE), Firewall (NAT), Firewall (inspect), TCP Adjust MSS, Post-Input-Flexible-NetFlow, Output-Flexible-NetFlow
          IPv4 WCCP Redirect outbound is disabled
          IPv4 WCCP Redirect inbound is enabled
          IPv4 WCCP Redirect exclude is disabled
        Vlan1 is up, line protocol is up
          Internet protocol processing disabled

    '''
    }
    golden_parsed_output = {
    "Embedded-Service-Engine0/0": {
        "enabled": False,
        "oper_status": "down"
    },
    "GigabitEthernet0/0": {
        "enabled": True,
        "oper_status": "up"
    },
    "GigabitEthernet0/0.100": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.1.1.10/24": {
                "ip": "10.1.1.10",
                "prefix_length": "24",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1500,
        "helper_address": [
            "10.1.2.129",
            "10.1.3.129"
        ],
        "directed_broadcast_forwarding": False,
        "multicast_groups": [
            "224.0.0.1",
            "224.0.0.13",
            "224.0.0.2",
            "224.0.0.22",
            "224.0.0.5",
            "224.0.0.6"
        ],
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "never sent",
            "unreachables": "never sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": True,
            "redirect_exclude": False
        }
    },
    "GigabitEthernet0/0.101": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.1.98.10/24": {
                "ip": "10.1.98.10",
                "prefix_length": "24",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1500,
        "helper_address": [
            "10.1.2.129",
            "10.1.3.129"
        ],
        "directed_broadcast_forwarding": False,
        "multicast_groups": [
            "224.0.0.5",
            "224.0.0.6"
        ],
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "never sent",
            "unreachables": "never sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "policy_routing": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": True,
            "redirect_exclude": False
        }
    },
    "GigabitEthernet0/0.300": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.6.100.10/25": {
                "ip": "10.6.100.10",
                "prefix_length": "25",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1500,
        "helper_address": [
            "10.1.2.129",
            "10.1.3.129"
        ],
        "directed_broadcast_forwarding": False,
        "multicast_groups": [
            "224.0.0.5",
            "224.0.0.6"
        ],
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "never sent",
            "unreachables": "never sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": True,
            "redirect_exclude": False
        }
    },
    "GigabitEthernet0/0.308": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.5.101.129/25": {
                "ip": "10.5.101.129",
                "prefix_length": "25",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1500,
        "helper_address": [
            "10.1.2.129",
            "10.1.3.129"
        ],
        "directed_broadcast_forwarding": False,
        "multicast_groups": [
            "224.0.0.5",
            "224.0.0.6"
        ],
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "always sent",
            "unreachables": "always sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "policy_routing": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": False,
            "redirect_exclude": False
        }
    },
    "GigabitEthernet0/0.324": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.2.100.129/25": {
                "ip": "10.2.100.129",
                "prefix_length": "25",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1500,
        "helper_address": [
            "10.160.124.129",
            "10.160.125.129"
        ],
        "directed_broadcast_forwarding": False,
        "multicast_groups": [
            "224.0.0.5",
            "224.0.0.6"
        ],
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "never sent",
            "unreachables": "never sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": False,
            "redirect_exclude": False
        }
    },
    "GigabitEthernet0/0.398": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.8.10.10/25": {
                "ip": "10.8.10.10",
                "prefix_length": "25",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1500,
        "directed_broadcast_forwarding": False,
        "multicast_groups": [
            "224.0.0.5",
            "224.0.0.6"
        ],
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "always sent",
            "unreachables": "always sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "policy_routing": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": False,
            "redirect_exclude": False
        }
    },
    "ISM0/0": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.1.98.10": {
                "ip": "10.1.98.10",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "mtu": 1500,
        "directed_broadcast_forwarding": False,
        "multicast_groups": [
            "224.0.0.5"
        ],
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "always sent",
            "unreachables": "always sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "policy_routing": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "input_features": [
            "MCI Check"
        ],
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": False,
            "redirect_exclude": False
        }
    },
    "GigabitEthernet0/1": {
        "enabled": True,
        "oper_status": "down"
    },
    "GigabitEthernet0/2": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.205.34.178/29": {
                "ip": "10.205.34.178",
                "prefix_length": "29",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1500,
        "directed_broadcast_forwarding": False,
        "proxy_arp": False,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "never sent",
            "unreachables": "never sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "policy_routing": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": False,
            "redirect_exclude": False
        }
    },
    "ISM0/1": {
        "enabled": True,
        "oper_status": "up"
    },
    "SM1/0": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.1.99.10/24": {
                "ip": "10.1.99.10",
                "prefix_length": "24",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1500,
        "directed_broadcast_forwarding": False,
        "multicast_groups": [
            "224.0.0.5",
            "224.0.0.6"
        ],
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "always sent",
            "unreachables": "always sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "policy_routing": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": False,
            "redirect_exclude": True
        }
    },
    "SM1/1": {
        "enabled": True,
        "oper_status": "up"
    },
    "Async0/1/0": {
        "enabled": True,
        "oper_status": "down"
    },
    "Loopback0": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.38.2.9/32": {
                "ip": "10.38.2.9",
                "prefix_length": "32",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1514,
        "directed_broadcast_forwarding": False,
        "multicast_groups": [
            "224.0.0.5"
        ],
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "always sent",
            "unreachables": "always sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_null_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "policy_routing": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "input_features": [
            "MCI Check"
        ],
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": False,
            "redirect_exclude": False
        }
    },
    "Loopback1": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "172.16.219.118/32": {
                "ip": "172.16.219.118",
                "prefix_length": "32",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1514,
        "directed_broadcast_forwarding": False,
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "always sent",
            "unreachables": "always sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_null_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "policy_routing": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "input_features": [
            "MCI Check"
        ],
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": False,
            "redirect_exclude": False
        }
    },
    "NVI0": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "0.0.0.0": {
                "ip": "0.0.0.0",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "mtu": 1514,
        "directed_broadcast_forwarding": False,
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "always sent",
            "unreachables": "always sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": False,
        "ip_flow_switching": False,
        "ip_cef_switching": False,
        "ip_null_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "policy_routing": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "input_features": [
            "MCI Check"
        ],
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": False,
            "redirect_exclude": False
        }
    },
    "Tunnel20": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.145.24.118/30": {
                "ip": "10.145.24.118",
                "prefix_length": "30",
                "secondary": False,
                "broadcast_address": "255.255.255.255"
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1420,
        "directed_broadcast_forwarding": False,
        "multicast_groups": [
            "224.0.0.1",
            "224.0.0.13",
            "224.0.0.2",
            "224.0.0.22"
        ],
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "always sent",
            "unreachables": "always sent",
            "mask_replies": "never sent"
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_null_turbo_vector": True,
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": [
            "CEF",
            "Fast"
        ],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "policy_routing": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": True,
            "redirect_exclude": False
        }
    },
    "Vlan1": {
        "enabled": True,
        "oper_status": "up"
    }
}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        interface_obj = ShowIpInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowIpInterface(device=self.device)
        parsed_output = interface_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()