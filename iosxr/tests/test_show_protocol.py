
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_ospf
from parser.iosxr.show_protocol import ShowProtocolsAfiAllAll


# ===========================================
#  Unit test for 'show protocols afi-all all'
# ===========================================
class test_show_protocols_afi_all_all(unittest.TestCase):

    '''Unit test for "show protocols afi-all all" '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'protocols': 
            {'bgp': 
                {'address_family': 
                    {'vpnv4 unicast': 
                        {'distance': 
                            {'external': 20,
                            'internal': 200,
                            'local': 200},
                        'neighbors': 
                            {'4.4.4.4': 
                                {'gr_enable': 'No',
                                'last_update': '00:01:28',
                                'nsr_state': 'None'}}},
                    'vpnv6 unicast': 
                        {'distance': 
                            {'external': 20,
                            'internal': 200,
                            'local': 200},
                        'neighbors': 
                            {'4.4.4.4': 
                                {'gr_enable': 'No',
                                'last_update': '00:01:28',
                                'nsr_state': 'None'}}}},
                'bgp_pid': 100,
                'graceful_restart': 
                    {'enable': False},
                'nsr': 
                    {'current_state': 'active ready',
                    'enable': True}},
            'ospf': 
                {'vrf': 
                    {'default': 
                        {'address_family': 
                            {'ipv4': 
                                {'instance': 
                                    {'1': 
                                        {'areas': 
                                            {'0.0.0.0': 
                                                {'interfaces': ['Loopback0', 'GigabitEthernet0/0/0/0', 'GigabitEthernet0/0/0/2'],
                                                'mpls': 
                                                    {'te': 
                                                        {'enable': True}}}},
                                                'nsf': False,
                                        'preference': 
                                            {'multi_values': 
                                                {'external': 114,
                                                'granularity': 
                                                    {'detail': 
                                                        {'inter_area': 113,
                                                        'intra_area': 112}}},
                                            'single_value': 
                                                {'all': 110}},
                                        'router_id': '3.3.3.3'}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/0/CPU0:R3_ospf_xr#show protocols afi-all all
        Mon Jan  8 17:45:17.553 UTC

        Routing Protocol "BGP 100"
        Non-stop routing is enabled
        Graceful restart is not enabled
        Current BGP NSR state - Active Ready
        BGP NSR state not ready: Wait for standby ready msg

        Address Family VPNv4 Unicast:
          Distance: external 20 internal 200 local 200
          Routing Information Sources:
            Neighbor          State/Last update received  NSR-State  GR-Enabled
            4.4.4.4           00:01:28                    None         No

        Address Family VPNv6 Unicast:
          Distance: external 20 internal 200 local 200
          Routing Information Sources:
            Neighbor          State/Last update received  NSR-State  GR-Enabled
            4.4.4.4           00:01:28                    None         No

        Routing Protocol OSPF 1
          Router Id: 3.3.3.3
          Distance: 110
          Distance: IntraArea 112 InterArea 113 External/NSSA 114
          Non-Stop Forwarding: Disabled
          Redistribution:
            None
          Area 0
            MPLS/TE enabled
            Loopback0
            GigabitEthernet0/0/0/0
            GigabitEthernet0/0/0/2
        '''}

    def test_show_protocols_afi_all_all_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowProtocolsAfiAllAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_protocols_afi_all_all_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowProtocolsAfiAllAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
