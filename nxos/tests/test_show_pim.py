import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from parser.nxos.show_pim import ShowIpPimInterface,\
                                 ShowIpv6PimVrfAllDetail\


# ============================================
# Parser for 'show ip pim interface'
# ============================================
class test_show_ip_pim_interface(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_pim_interface_1 = {
        'vrf':{
            'VRF1':{
                'interfaces':{
                    'Ethernet2/2':{
                        'address_family':{
                            'ipv4':{
                                'oper_status': 'protocol-up/link-up/admin-up',
                                'address': ['10.11.33.11'],
                                'ip_subnet': '10.11.33.0/24',
                                'dr_address': '10.11.33.11' ,
                                'dr_priority': 144,
                                'neighbor_count': 1,
                                'hello_interval': 45,
                                'hello_expiration': '00:00:05',
                                'neighbor_holdtime': 159,
                                'configured_dr_priority': 144,
                                'dr_delay': 3 ,
                                'bsr_border': True,
                                'genid': '0x26fae674',
                                'hello_md5_ah_authentication': 'disabled',
                                'neighbor_filter': 'v4neighbor-policy',
                                'jp_inbound_policy': 'v4jp-policy',
                                'jp_outbound_policy': 'v4jp-policy',
                                'jp_interval': 1,
                                'jp_next_sending': 1,
                                'bfd': {
                                    'enable': False,
                                },
                               'sm': {
                                    'passive': False,
                                },
                               'vpc_svi': False,
                               'auto_enabled': False,
                               'statistics': {
                                    'general': {
                                        'hellos': '360/474',
                                        'jps': '0/0',
                                        'asserts': '0/0',
                                        'grafts': '0/0',
                                        'graft_acks': '0/0',
                                        'df_offers': '0/0',
                                        'df_winners': '0/0',
                                        'df_backoffs': '0/0',
                                        'df_passes': '0/0',
                                    },
                                    'errors': {
                                        'checksum': 0,
                                        'invalid_packet_types': 0,
                                        'invalid_df_subtypes': 0,
                                        'authentication_failed': 0,
                                        'packet_length_errors': 0,
                                        'bad_version_packets': 0,
                                        'packets_from_self': 0,
                                        'packets_from_non_neighbors': 0,
                                        'packets_received_on_passiveinterface': 0,
                                        'jps_received_on_rpf_interface': 0,
                                        'joins_received_with_no_rp': 0,
                                        'joins_received_with_wrong_rp': 0,
                                        'joins_received_with_ssm_groups': 0,
                                        'joins_received_with_bidir_groups': 0,
                                        'jps_filtered_by_inbound_policy': 0,
                                        'jps_filtered_by_outbound_policy': 0,
                                    },
                                },
                            },
                        },
                    },
                    'Ethernet2/3':{
                        'address_family': {
                            'ipv4': {
                                'oper_status': 'protocol-up/link-up/admin-up',
                                'address': ['10.11.66.11'],
                                'ip_subnet': '10.11.66.0/24',
                                'dr_address': '10.11.66.11',
                                'dr_priority': 1,
                                'neighbor_count': 0,
                                'hello_interval': 30,
                                'hello_expiration': '00:00:14',
                                'neighbor_holdtime': 105,
                                'configured_dr_priority': 1,
                                'dr_delay': 3,
                                'bsr_border': False,
                                'genid': '0x2737c18b',
                                'hello_md5_ah_authentication': 'disabled',
                                'neighbor_filter': 'none configured',
                                'jp_inbound_policy': 'none configured',
                                'jp_outbound_policy': 'none configured',
                                'jp_interval': 1,
                                'jp_next_sending': 1,
                                'bfd': {
                                    'enable': False,
                                },
                                'sm': {
                                    'passive': False,
                                },
                                'vpc_svi': False,
                                'auto_enabled': False,
                                'statistics': {
                                    'general': {
                                        'hellos': '489/0',
                                        'jps': '0/0',
                                        'asserts': '0/0',
                                        'grafts': '0/0',
                                        'graft_acks': '0/0',
                                        'df_offers': '0/0',
                                        'df_winners': '0/0',
                                        'df_backoffs': '0/0',
                                        'df_passes': '0/0',
                                    },
                                    'errors': {
                                        'checksum': 0,
                                        'invalid_packet_types': 0,
                                        'invalid_df_subtypes': 0,
                                        'authentication_failed': 0,
                                        'packet_length_errors': 0,
                                        'bad_version_packets': 0,
                                        'packets_from_self': 0,
                                        'packets_from_non_neighbors': 0,
                                        'packets_received_on_passiveinterface': 0,
                                        'jps_received_on_rpf_interface': 0,
                                        'joins_received_with_no_rp': 0,
                                        'joins_received_with_wrong_rp': 0,
                                        'joins_received_with_ssm_groups': 0,
                                        'joins_received_with_bidir_groups': 0,
                                        'jps_filtered_by_inbound_policy': 0,
                                        'jps_filtered_by_outbound_policy': 0,
                                    },
                                },
                            },
                            },
                        },
                    },
                },
            'default':{
                'interfaces': {
                    'Ethernet2/1': {
                        'address_family': {
                            'ipv4': {
                                'oper_status': 'protocol-up/link-up/admin-up',
                                'address': ['10.1.5.1'],
                                'ip_subnet': '10.1.5.0/24',
                                'dr_address': '10.1.5.1',
                                'dr_priority': 1,
                                'neighbor_count': 0,
                                'hello_interval': 30,
                                'hello_expiration': '00:00:13',
                                'neighbor_holdtime': 105,
                                'configured_dr_priority': 1,
                                'dr_delay': 3,
                                'bsr_border': False,
                                'genid': '0x3148ed16',
                                'hello_md5_ah_authentication': 'disabled',
                                'neighbor_filter': 'none configured',
                                'jp_inbound_policy': 'none configured',
                                'jp_outbound_policy': 'none configured',
                                'jp_interval': 1,
                                'jp_next_sending': 1,
                                'bfd': {
                                    'enable': False,
                                },
                                'sm': {
                                    'passive': False,
                                },
                                'vpc_svi': False,
                                'auto_enabled': False,
                                'statistics': {
                                    'general': {
                                        'hellos': '243/0',
                                        'jps': '0/0',
                                        'asserts': '0/0',
                                        'grafts': '0/0',
                                        'graft_acks': '0/0',
                                        'df_offers': '0/0',
                                        'df_winners': '0/0',
                                        'df_backoffs': '0/0',
                                        'df_passes': '0/0',
                                    },
                                    'errors': {
                                        'checksum': 0,
                                        'invalid_packet_types': 0,
                                        'invalid_df_subtypes': 0,
                                        'authentication_failed': 0,
                                        'packet_length_errors': 0,
                                        'bad_version_packets': 0,
                                        'packets_from_self': 0,
                                        'packets_from_non_neighbors': 0,
                                        'packets_received_on_passiveinterface': 0,
                                        'jps_received_on_rpf_interface': 0,
                                        'joins_received_with_no_rp': 0,
                                        'joins_received_with_wrong_rp': 0,
                                        'joins_received_with_ssm_groups': 0,
                                        'joins_received_with_bidir_groups': 0,
                                        'jps_filtered_by_inbound_policy': 0,
                                        'jps_filtered_by_outbound_policy': 0,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }
    }

    golden_output_pim_interface_1 = {'execute.return_value': '''
    R1# show ip pim interface vrf all
        PIM Interface Status for VRF "VRF1"
        Ethernet2/2, Interface status: protocol-up/link-up/admin-up
          IP address: 10.11.33.11, IP subnet: 10.11.33.0/24
          PIM DR: 10.11.33.11, DR's priority: 144
          PIM neighbor count: 1
          PIM hello interval: 45 secs (configured 44444 ms), next hello sent in: 00:00:05
          PIM neighbor holdtime: 159 secs
          PIM configured DR priority: 144
          PIM configured DR delay: 3 secs
          PIM border interface: yes
          PIM GenID sent in Hellos: 0x26fae674
          PIM Hello MD5-AH Authentication: disabled
          PIM Neighbor policy: v4neighbor-policy
          PIM Join-Prune inbound policy: v4jp-policy
          PIM Join-Prune outbound policy: v4jp-policy
          PIM Join-Prune interval: 1 minutes
          PIM Join-Prune next sending: 1 minutes
          PIM BFD enabled: no
          PIM passive interface: no
          PIM VPC SVI: no
          PIM Auto Enabled: no
          PIM Interface Statistics, last reset: never
            General (sent/received):
              Hellos: 360/474 (early: 0), JPs: 0/0, Asserts: 0/0
              Grafts: 0/0, Graft-Acks: 0/0
              DF-Offers: 0/0, DF-Winners: 0/0, DF-Backoffs: 0/0, DF-Passes: 0/0
            Errors:
              Checksum errors: 0, Invalid packet types/DF subtypes: 0/0
              Authentication failed: 0
              Packet length errors: 0, Bad version packets: 0, Packets from self: 0
              Packets from non-neighbors: 0
                  Packets received on passiveinterface: 0
              JPs received on RPF-interface: 0
              (*,G) Joins received with no/wrong RP: 0/0
              (*,G)/(S,G) JPs received for SSM/Bidir groups: 0/0
              JPs filtered by inbound policy: 0
              JPs filtered by outbound policy: 0
        Ethernet2/3, Interface status: protocol-up/link-up/admin-up
          IP address: 10.11.66.11, IP subnet: 10.11.66.0/24
          PIM DR: 10.11.66.11, DR's priority: 1
          PIM neighbor count: 0
          PIM hello interval: 30 secs, next hello sent in: 00:00:14
          PIM neighbor holdtime: 105 secs
          PIM configured DR priority: 1
          PIM configured DR delay: 3 secs
          PIM border interface: no
          PIM GenID sent in Hellos: 0x2737c18b
          PIM Hello MD5-AH Authentication: disabled
          PIM Neighbor policy: none configured
          PIM Join-Prune inbound policy: none configured
          PIM Join-Prune outbound policy: none configured
          PIM Join-Prune interval: 1 minutes
          PIM Join-Prune next sending: 1 minutes
          PIM BFD enabled: no
          PIM passive interface: no
          PIM VPC SVI: no
          PIM Auto Enabled: no
          PIM Interface Statistics, last reset: never
            General (sent/received):
              Hellos: 489/0 (early: 0), JPs: 0/0, Asserts: 0/0
              Grafts: 0/0, Graft-Acks: 0/0
              DF-Offers: 0/0, DF-Winners: 0/0, DF-Backoffs: 0/0, DF-Passes: 0/0
            Errors:
              Checksum errors: 0, Invalid packet types/DF subtypes: 0/0
              Authentication failed: 0
              Packet length errors: 0, Bad version packets: 0, Packets from self: 0
              Packets from non-neighbors: 0
                  Packets received on passiveinterface: 0
              JPs received on RPF-interface: 0
              (*,G) Joins received with no/wrong RP: 0/0
              (*,G)/(S,G) JPs received for SSM/Bidir groups: 0/0
              JPs filtered by inbound policy: 0
              JPs filtered by outbound policy: 0

        PIM Interface Status for VRF "default"
        Ethernet2/1, Interface status: protocol-up/link-up/admin-up
          IP address: 10.1.5.1, IP subnet: 10.1.5.0/24
          PIM DR: 10.1.5.1, DR's priority: 1
          PIM neighbor count: 0
          PIM hello interval: 30 secs, next hello sent in: 00:00:13
          PIM neighbor holdtime: 105 secs
          PIM configured DR priority: 1
          PIM configured DR delay: 3 secs
          PIM border interface: no
          PIM GenID sent in Hellos: 0x3148ed16
          PIM Hello MD5-AH Authentication: disabled
          PIM Neighbor policy: none configured
          PIM Join-Prune inbound policy: none configured
          PIM Join-Prune outbound policy: none configured
          PIM Join-Prune interval: 1 minutes
          PIM Join-Prune next sending: 1 minutes
          PIM BFD enabled: no
          PIM passive interface: no
          PIM VPC SVI: no
          PIM Auto Enabled: no
          PIM Interface Statistics, last reset: never
            General (sent/received):
              Hellos: 243/0 (early: 0), JPs: 0/0, Asserts: 0/0
              Grafts: 0/0, Graft-Acks: 0/0
              DF-Offers: 0/0, DF-Winners: 0/0, DF-Backoffs: 0/0, DF-Passes: 0/0
            Errors:
              Checksum errors: 0, Invalid packet types/DF subtypes: 0/0
              Authentication failed: 0
              Packet length errors: 0, Bad version packets: 0, Packets from self: 0
              Packets from non-neighbors: 0
                  Packets received on passiveinterface: 0
              JPs received on RPF-interface: 0
              (*,G) Joins received with no/wrong RP: 0/0
              (*,G)/(S,G) JPs received for SSM/Bidir groups: 0/0
              JPs filtered by inbound policy: 0
              JPs filtered by outbound policy: 0

    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpPimInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_pim_interface(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_pim_interface_1)
        obj = ShowIpPimInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_pim_interface_1)


# ============================================
# Parser for 'show ipv6 pim vrf all detail'
# ============================================
class test_show_ipv6_pim_vrf_all_detail(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_v6_vrf_detail_1 = {
        'vrf':{
            'default':
                {
                'address_family':
                    {'ipv6':
                        {
                        'vrf_id': 1,
                        'table_id': '0x80000001',
                        'interface_count': 3,
                        'bfd': {
                            'enable': False,
                        },

                        'state_limit': 'none',
                        'register_rate_limit': 'none',
                        'shared_tree_route_map':'v6spt-threshold-group-list',
                        },
                    },
                },
            'VRF1':
                {
                'address_family':
                    {'ipv6':
                        {
                        'vrf_id': 3,
                        'table_id': '0x80000003',
                        'interface_count': 3,
                        'bfd': {
                            'enable': False,
                        },

                        'state_limit': 'none',
                        'register_rate_limit': 'none',
                        'shared_tree_ranges': 'none',
                    },
                },
            },
        },
    }
    golden_output_vrf_v6_detail_1 = {'execute.return_value': '''
        R1# show ipv6 pim vrf all detail
        PIM6 Enabled VRFs
        VRF Name              VRF      Table       Interface  BFD
                              ID       ID          Count      Enabled
        default               1        0x80000001  3          no
          State Limit: None
          Register Rate Limit: none
          Shared tree route-map: v6spt-threshold-group-list
                 route-ranges:

        VRF1                  3        0x80000003  3          no
          State Limit: None
          Register Rate Limit: none
          Shared tree ranges: none
    '''}

    golden_output_vrf_v6_detail_2 = {'execute.return_value': '''
            R1# show ip pim vrf all detail
            PIM6 Enabled VRFs
            %S DDDD
        '''}
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6PimVrfAllDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_v6_vrf_detail_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_vrf_v6_detail_1)
        obj = ShowIpv6PimVrfAllDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_v6_vrf_detail_1)

    def test_golden_v6_vrf_detail_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_vrf_v6_detail_2)
        obj = ShowIpv6PimVrfAllDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

if __name__ == '__main__':
    unittest.main()