import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.nxos.show_pim import ShowIpPimInterface,\
                                 ShowIpv6PimVrfAllDetail,\
                                 ShowIpPimRp,\
                                 ShowIpPimPolicyStaticticsRegisterPolicy,\
                                 ShowIpPimGroupRange,\
                                 ShowIpPimVrfDetail,\
                                 ShowIpPimNeighbor,\
                                 ShowIpv6PimGroupRange,\
                                 ShowIpPimRoute,\
                                 ShowIpv6PimNeighbor,\
                                 ShowIpv6PimRoute,\
                                 ShowIpPimDf,\
                                 ShowIpv6PimDf,\
                                 ShowIpv6PimRp,\
                                 ShowIpv6PimInterface, \
                                 ShowRunningConfigPim


# ============================================
# Parser for 'show ipv6 pim interface'
# ============================================
class test_show_ipv6_pim_interface(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_v6_pim_interface_1 = {
        'vrf':{
            'default':{
                'interfaces':{
                    'Ethernet2/1':{
                        'address_family':{
                            'ipv6':{
                                'oper_status': 'up',
                                'link_status': 'up',
                                'admin_status': 'up',
                                'address': ['2001:db8:1:5::1/64'],
                                'dr_address': 'fe80::5054:ff:fe89:740c' ,
                                'dr_priority': 1,
                                'neighbor_count': 0,
                                'hello_interval': 30,
                                'hello_expiration': '00:00:13',
                                'neighbor_holdtime': 105,
                                'configured_dr_priority': 1,
                                'bsr_border': False,
                                'genid': '0x25f72e3c',
                                'hello_md5_ah_authentication': 'disabled',
                                'bfd': {
                                    'enable': False,
                                },
                               'sm': {
                                    'passive': False,
                                },
                               'auto_enabled': False,
                               'statistics': {
                                    'last_reset': 'never',
                                    'general': {
                                        'hellos': '240/0',
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
                    'Ethernet2/5':{
                        'address_family': {
                            'ipv6': {
                                'oper_status': 'up',
                                'link_status': 'up',
                                'admin_status': 'up',
                                'address': ['2001:db8:1:2::1/64','2001:db8:1:2::2/64'],
                                'dr_address': 'fe80::5054:ff:fe89:740c',
                                'dr_priority': 1,
                                'neighbor_count': 0,
                                'hello_interval': 30,
                                'hello_expiration': '00:00:07',
                                'neighbor_holdtime': 105,
                                'configured_dr_priority': 1,
                                'bsr_border': False,
                                'genid': '0x30a2ad71',
                                'hello_md5_ah_authentication': 'disabled',
                                'bfd': {
                                    'enable': False,
                                },
                                'sm': {
                                    'passive': False,
                                },
                                'auto_enabled': False,
                                'statistics': {
                                    'last_reset': 'never',
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
            'VRF1':{
                'interfaces': {
                    'Ethernet2/2': {
                        'address_family': {
                            'ipv6': {
                                'oper_status': 'up',
                                'link_status': 'up',
                                'admin_status': 'up',
                                'address': ['2001:db8:11:33::11/64'],
                                'dr_address': 'fe80::5054:ff:fe89:740c',
                                'dr_priority': 166,
                                'neighbor_count': 1,
                                'hello_interval': 67,
                                'hello_expiration': '00:00:34',
                                'neighbor_holdtime': 236,
                                'configured_dr_priority': 166,
                                'bsr_border': True,
                                'genid': '0x08f0f420',
                                'hello_md5_ah_authentication': 'disabled',
                                'neighbor_filter': 'v6neighbor-policy',
                                'jp_inbound_policy': 'v6jp-policy',
                                'jp_outbound_policy': 'v6jp-policy',
                                'bfd': {
                                    'enable': False,
                                },
                                'sm': {
                                    'passive': False,
                                },
                                'auto_enabled': False,
                                'statistics': {
                                    'last_reset': 'never',
                                    'general': {
                                        'hellos': '274/477',
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

    golden_output_v6_pim_interface_1 = {'execute.return_value': '''
R1#show ipv6 pim interface vrf all
PIM6 Interface Status for VRF "default"
Ethernet2/1, Interface status: protocol-up/link-up/admin-up
  IPv6 address:
    2001:db8:1:5::1/64 [VALID]
  PIM6 DR: fe80::5054:ff:fe89:740c, DR's priority: 1
  PIM6 neighbor count: 0
  PIM6 hello interval: 30 secs, next hello sent in: 00:00:13
  PIM6 neighbor holdtime: 105 secs
  PIM6 configured DR priority: 1
  PIM6 border interface: no
  PIM6 GenID sent in Hellos: 0x25f72e3c
  PIM6 Hello MD5-AH Authentication: disabled
  PIM6 Neighbor policy: none configured
  PIM6 Join-Prune inbound policy: none configured
  PIM6 Join-Prune outbound policy: none configured
  PIM passive interface: no
  PIM Auto Enabled: no
  PIM6 BFD enabled: no
  PIM6 Interface Statistics, last reset: never
    General (sent/received):
      Hellos: 240/0, JPs: 0/0, Asserts: 0/0
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
Ethernet2/5, Interface status: protocol-up/link-up/admin-up
  IPv6 address:
    2001:db8:1:2::1/64 [VALID]
    2001:db8:1:2::2/64 [VALID]
  PIM6 DR: fe80::5054:ff:fe89:740c, DR's priority: 1
  PIM6 neighbor count: 0
  PIM6 hello interval: 30 secs, next hello sent in: 00:00:07
  PIM6 neighbor holdtime: 105 secs
  PIM6 configured DR priority: 1
  PIM6 border interface: no
  PIM6 GenID sent in Hellos: 0x30a2ad71
  PIM6 Hello MD5-AH Authentication: disabled
  PIM6 Neighbor policy: none configured
  PIM6 Join-Prune inbound policy: none configured
  PIM6 Join-Prune outbound policy: none configured
  PIM passive interface: no
  PIM Auto Enabled: no
  PIM6 BFD enabled: no
  PIM6 Interface Statistics, last reset: never
    General (sent/received):
      Hellos: 489/0, JPs: 0/0, Asserts: 0/0
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

PIM6 Interface Status for VRF "VRF1"
Ethernet2/2, Interface status: protocol-up/link-up/admin-up
  IPv6 address:
    2001:db8:11:33::11/64 [VALID]
  PIM6 DR: fe80::5054:ff:fe89:740c, DR's priority: 166
  PIM6 neighbor count: 1
  PIM6 hello interval: 67 secs (configured 66666 ms), next hello sent in: 00:00:34
  PIM6 neighbor holdtime: 236 secs
  PIM6 configured DR priority: 166
  PIM6 border interface: yes
  PIM6 GenID sent in Hellos: 0x08f0f420
  PIM6 Hello MD5-AH Authentication: disabled
  PIM6 Neighbor policy: v6neighbor-policy
  PIM6 Join-Prune inbound policy: v6jp-policy
  PIM6 Join-Prune outbound policy: v6jp-policy
  PIM passive interface: no
  PIM Auto Enabled: no
  PIM6 BFD enabled: no
  PIM6 Interface Statistics, last reset: never
    General (sent/received):
      Hellos: 274/477, JPs: 0/0, Asserts: 0/0
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

    golden_parsed_output_v6_pim_interface_2 = {
        "vrf": {
            "VRF1": {
                "interfaces": {
                    "Ethernet1/1.11": {
                        "address_family": {
                            "ipv6": {
                                "oper_status": "up",
                                "link_status": "up",
                                "admin_status": "up",
                                "address": ["2001:10:3:5::5/64", " Errors:"],
                                "dr_address": "fe80::282:eaff:feed:1b08",
                                "dr_priority": 1,
                                "neighbor_count": 1,
                                "hello_interval": 30,
                                "hello_expiration": "00:00:08",
                                "neighbor_holdtime": 105,
                                "configured_dr_priority": 1,
                                "dr_delay": 3,
                                "bsr_border": False,
                                "genid": "0x2a5b3d03",
                                "hello_md5_ah_authentication": "disabled",
                                "jp_interval": 1,
                                "jp_next_sending": 0,
                                "bfd": {"enable": False},
                                "sm": {"passive": False},
                                "auto_enabled": False,
                                "statistics": {
                                    "general": {
                                        "hellos": "29/29",
                                        "jps": "3/0",
                                        "asserts": "0/0",
                                        "graft_acks": "0/0",
                                        "grafts": "0/0",
                                        "df_offers": "0/0",
                                        "df_backoffs": "0/0",
                                        "df_passes": "0/0",
                                        "df_winners": "0/0",
                                    },
                                    "last_reset": "never",
                                    "errors": {
                                        "checksum": 0,
                                        "invalid_df_subtypes": 0,
                                        "invalid_packet_types": 0,
                                        "authentication_failed": 0,
                                        "packet_length_errors": 0,
                                        "bad_version_packets": 0,
                                        "packets_from_self": 0,
                                        "packets_from_non_neighbors": 0,
                                        "packets_received_on_passiveinterface": 0,
                                        "jps_received_on_rpf_interface": 0,
                                        "joins_received_with_no_rp": 0,
                                        "joins_received_with_wrong_rp": 0,
                                        "joins_received_with_bidir_groups": 0,
                                        "joins_received_with_ssm_groups": 0,
                                        "jps_filtered_by_inbound_policy": 0,
                                        "jps_filtered_by_outbound_policy": 0,
                                    },
                                },
                            }
                        }
                    },
                    "Ethernet1/2.11": {
                        "address_family": {
                            "ipv6": {
                                "oper_status": "up",
                                "link_status": "up",
                                "admin_status": "up",
                                "dr_address": "fe80::282:94ff:fe2d:1b08",
                                "dr_priority": 1,
                                "configured_dr_priority": 1,
                                "dr_delay": 3,
                                "neighbor_count": 0,
                                "hello_interval": 30,
                                "hello_expiration": "00:00:17",
                                "neighbor_holdtime": 105,
                                "bsr_border": False,
                                "genid": "0x30aaaac9",
                                "hello_md5_ah_authentication": "disabled",
                                "jp_interval": 1,
                                "jp_next_sending": 0,
                                "bfd": {"enable": False},
                                "sm": {"passive": False},
                                "auto_enabled": False,
                                "statistics": {
                                    "general": {
                                        "hellos": "28/0",
                                        "jps": "0/0",
                                        "asserts": "0/0",
                                        "df_offers": "0/0",
                                        "graft_acks": "0/0",
                                        "grafts": "0/0",
                                        "df_backoffs": "0/0",
                                        "df_passes": "0/0",
                                        "df_winners": "0/0",
                                    },
                                    "last_reset": "never",
                                    "errors": {
                                        "checksum": 0,
                                        "invalid_df_subtypes": 0,
                                        "invalid_packet_types": 0,
                                        "authentication_failed": 0,
                                        "packet_length_errors": 0,
                                        "bad_version_packets": 0,
                                        "packets_from_self": 0,
                                        "packets_from_non_neighbors": 0,
                                        "packets_received_on_passiveinterface": 0,
                                        "jps_received_on_rpf_interface": 0,
                                        "joins_received_with_bidir_groups": 0,
                                        "joins_received_with_no_rp": 0,
                                        "joins_received_with_ssm_groups": 0,
                                        "joins_received_with_wrong_rp": 0,
                                        "jps_filtered_by_inbound_policy": 0,
                                        "jps_filtered_by_outbound_policy": 0,
                                    },
                                },
                                "address": ["2001:20:5:5::5/64", " Errors:"],
                            }
                        }
                    },
                    "Ethernet1/3.11": {
                        "address_family": {
                            "ipv6": {
                                "oper_status": "up",
                                "link_status": "up",
                                "admin_status": "up",
                                "dr_address": "fe80::282:94ff:fe2d:1b08",
                                "dr_priority": 1,
                                "configured_dr_priority": 1,
                                "dr_delay": 3,
                                "neighbor_count": 1,
                                "hello_interval": 30,
                                "hello_expiration": "00:00:24",
                                "neighbor_holdtime": 105,
                                "bsr_border": False,
                                "genid": "0x1c0ede6c",
                                "hello_md5_ah_authentication": "disabled",
                                "jp_interval": 1,
                                "jp_next_sending": 0,
                                "bfd": {"enable": False},
                                "sm": {"passive": False},
                                "auto_enabled": False,
                                "statistics": {
                                    "general": {
                                        "hellos": "29/28",
                                        "jps": "16/0",
                                        "asserts": "0/0",
                                        "df_offers": "0/0",
                                        "graft_acks": "0/0",
                                        "grafts": "0/0",
                                        "df_backoffs": "0/0",
                                        "df_passes": "0/0",
                                        "df_winners": "0/0",
                                    },
                                    "last_reset": "never",
                                    "errors": {
                                        "checksum": 0,
                                        "invalid_df_subtypes": 0,
                                        "invalid_packet_types": 0,
                                        "authentication_failed": 0,
                                        "packet_length_errors": 0,
                                        "bad_version_packets": 0,
                                        "packets_from_self": 0,
                                        "packets_from_non_neighbors": 0,
                                        "packets_received_on_passiveinterface": 0,
                                        "jps_received_on_rpf_interface": 0,
                                        "joins_received_with_bidir_groups": 0,
                                        "joins_received_with_no_rp": 0,
                                        "joins_received_with_ssm_groups": 0,
                                        "joins_received_with_wrong_rp": 0,
                                        "jps_filtered_by_inbound_policy": 0,
                                        "jps_filtered_by_outbound_policy": 0,
                                    },
                                },
                                "address": ["2001:10:4:5::5/64", " Errors:"],
                            }
                        }
                    },
                    "loopback11": {
                        "address_family": {
                            "ipv6": {
                                "oper_status": "up",
                                "link_status": "up",
                                "admin_status": "up",
                                "dr_address": "fe80::250:56ff:fe82:942d",
                                "dr_priority": 1,
                                "configured_dr_priority": 1,
                                "dr_delay": 3,
                                "neighbor_count": 0,
                                "hello_interval": 30,
                                "hello_expiration": "00:00:18",
                                "neighbor_holdtime": 105,
                                "bsr_border": False,
                                "genid": "0x1c0aa317",
                                "hello_md5_ah_authentication": "disabled",
                                "jp_interval": 1,
                                "jp_next_sending": 0,
                                "bfd": {"enable": False},
                                "sm": {"passive": False},
                                "auto_enabled": False,
                                "statistics": {
                                    "general": {
                                        "hellos": "29/0",
                                        "jps": "0/0",
                                        "asserts": "0/0",
                                        "df_offers": "0/0",
                                        "graft_acks": "0/0",
                                        "grafts": "0/0",
                                        "df_backoffs": "0/0",
                                        "df_passes": "0/0",
                                        "df_winners": "0/0",
                                    },
                                    "last_reset": "never",
                                    "errors": {
                                        "checksum": 0,
                                        "invalid_df_subtypes": 0,
                                        "invalid_packet_types": 0,
                                        "authentication_failed": 0,
                                        "packet_length_errors": 0,
                                        "bad_version_packets": 0,
                                        "packets_from_self": 0,
                                        "packets_from_non_neighbors": 0,
                                        "packets_received_on_passiveinterface": 0,
                                        "jps_received_on_rpf_interface": 0,
                                        "joins_received_with_bidir_groups": 0,
                                        "joins_received_with_no_rp": 0,
                                        "joins_received_with_ssm_groups": 0,
                                        "joins_received_with_wrong_rp": 0,
                                        "jps_filtered_by_inbound_policy": 0,
                                        "jps_filtered_by_outbound_policy": 0,
                                    },
                                },
                                "address": ["2001:5:5:5::5/128", " Errors:"],
                            }
                        }
                    },
                }
            },
            "default": {
                "interfaces": {
                    "Ethernet1/1.10": {
                        "address_family": {
                            "ipv6": {
                                "oper_status": "up",
                                "link_status": "up",
                                "admin_status": "up",
                                "address": ["2001:10:3:5::5/64", " Errors:"],
                                "dr_address": "fe80::282:eaff:feed:1b08",
                                "dr_priority": 1,
                                "neighbor_count": 1,
                                "hello_interval": 30,
                                "hello_expiration": "00:00:09",
                                "neighbor_holdtime": 105,
                                "configured_dr_priority": 1,
                                "dr_delay": 3,
                                "bsr_border": False,
                                "genid": "0x0e0ec63f",
                                "hello_md5_ah_authentication": "disabled",
                                "jp_interval": 1,
                                "jp_next_sending": 0,
                                "bfd": {"enable": False},
                                "sm": {"passive": False},
                                "auto_enabled": False,
                                "statistics": {
                                    "general": {
                                        "hellos": "29/29",
                                        "jps": "3/0",
                                        "asserts": "0/0",
                                        "graft_acks": "0/0",
                                        "grafts": "0/0",
                                        "df_offers": "0/0",
                                        "df_backoffs": "0/0",
                                        "df_passes": "0/0",
                                        "df_winners": "0/0",
                                    },
                                    "last_reset": "never",
                                    "errors": {
                                        "checksum": 0,
                                        "invalid_df_subtypes": 0,
                                        "invalid_packet_types": 0,
                                        "authentication_failed": 0,
                                        "packet_length_errors": 0,
                                        "bad_version_packets": 0,
                                        "packets_from_self": 0,
                                        "packets_from_non_neighbors": 0,
                                        "packets_received_on_passiveinterface": 0,
                                        "jps_received_on_rpf_interface": 0,
                                        "joins_received_with_no_rp": 0,
                                        "joins_received_with_wrong_rp": 0,
                                        "joins_received_with_bidir_groups": 0,
                                        "joins_received_with_ssm_groups": 0,
                                        "jps_filtered_by_inbound_policy": 0,
                                        "jps_filtered_by_outbound_policy": 0,
                                    },
                                },
                            }
                        }
                    },
                    "Ethernet1/2.10": {
                        "address_family": {
                            "ipv6": {
                                "oper_status": "up",
                                "link_status": "up",
                                "admin_status": "up",
                                "dr_address": "fe80::282:94ff:fe2d:1b08",
                                "dr_priority": 1,
                                "configured_dr_priority": 1,
                                "dr_delay": 3,
                                "neighbor_count": 0,
                                "hello_interval": 30,
                                "hello_expiration": "00:00:18",
                                "neighbor_holdtime": 105,
                                "bsr_border": False,
                                "genid": "0x0f5cdda1",
                                "hello_md5_ah_authentication": "disabled",
                                "jp_interval": 1,
                                "jp_next_sending": 0,
                                "bfd": {"enable": False},
                                "sm": {"passive": False},
                                "auto_enabled": False,
                                "statistics": {
                                    "general": {
                                        "hellos": "28/0",
                                        "jps": "0/0",
                                        "asserts": "0/0",
                                        "df_offers": "0/0",
                                        "graft_acks": "0/0",
                                        "grafts": "0/0",
                                        "df_backoffs": "0/0",
                                        "df_passes": "0/0",
                                        "df_winners": "0/0",
                                    },
                                    "last_reset": "never",
                                    "errors": {
                                        "checksum": 0,
                                        "invalid_df_subtypes": 0,
                                        "invalid_packet_types": 0,
                                        "authentication_failed": 0,
                                        "packet_length_errors": 0,
                                        "bad_version_packets": 0,
                                        "packets_from_self": 0,
                                        "packets_from_non_neighbors": 0,
                                        "packets_received_on_passiveinterface": 0,
                                        "jps_received_on_rpf_interface": 0,
                                        "joins_received_with_bidir_groups": 0,
                                        "joins_received_with_no_rp": 0,
                                        "joins_received_with_ssm_groups": 0,
                                        "joins_received_with_wrong_rp": 0,
                                        "jps_filtered_by_inbound_policy": 0,
                                        "jps_filtered_by_outbound_policy": 0,
                                    },
                                },
                                "address": ["2001:20:5:5::5/64", " Errors:"],
                            }
                        }
                    },
                    "Ethernet1/3.10": {
                        "address_family": {
                            "ipv6": {
                                "oper_status": "up",
                                "link_status": "up",
                                "admin_status": "up",
                                "dr_address": "fe80::282:94ff:fe2d:1b08",
                                "dr_priority": 1,
                                "configured_dr_priority": 1,
                                "dr_delay": 3,
                                "neighbor_count": 1,
                                "hello_interval": 30,
                                "hello_expiration": "00:00:12",
                                "neighbor_holdtime": 105,
                                "bsr_border": False,
                                "genid": "0x01ea02dd",
                                "hello_md5_ah_authentication": "disabled",
                                "jp_interval": 1,
                                "jp_next_sending": 0,
                                "bfd": {"enable": False},
                                "sm": {"passive": False},
                                "auto_enabled": False,
                                "statistics": {
                                    "general": {
                                        "hellos": "29/28",
                                        "jps": "16/0",
                                        "asserts": "0/0",
                                        "df_offers": "0/0",
                                        "graft_acks": "0/0",
                                        "grafts": "0/0",
                                        "df_backoffs": "0/0",
                                        "df_passes": "0/0",
                                        "df_winners": "0/0",
                                    },
                                    "last_reset": "never",
                                    "errors": {
                                        "checksum": 0,
                                        "invalid_df_subtypes": 0,
                                        "invalid_packet_types": 0,
                                        "authentication_failed": 0,
                                        "packet_length_errors": 0,
                                        "bad_version_packets": 0,
                                        "packets_from_self": 0,
                                        "packets_from_non_neighbors": 0,
                                        "packets_received_on_passiveinterface": 0,
                                        "jps_received_on_rpf_interface": 0,
                                        "joins_received_with_bidir_groups": 0,
                                        "joins_received_with_no_rp": 0,
                                        "joins_received_with_ssm_groups": 0,
                                        "joins_received_with_wrong_rp": 0,
                                        "jps_filtered_by_inbound_policy": 0,
                                        "jps_filtered_by_outbound_policy": 0,
                                    },
                                },
                                "address": ["2001:10:4:5::5/64", " Errors:"],
                            }
                        }
                    },
                    "loopback0": {
                        "address_family": {
                            "ipv6": {
                                "oper_status": "up",
                                "link_status": "up",
                                "admin_status": "up",
                                "dr_address": "fe80::250:56ff:fe82:942d",
                                "dr_priority": 1,
                                "configured_dr_priority": 1,
                                "dr_delay": 3,
                                "neighbor_count": 0,
                                "hello_interval": 30,
                                "hello_expiration": "00:00:16",
                                "neighbor_holdtime": 105,
                                "bsr_border": False,
                                "genid": "0x0cb530a6",
                                "hello_md5_ah_authentication": "disabled",
                                "jp_interval": 1,
                                "jp_next_sending": 0,
                                "bfd": {"enable": False},
                                "sm": {"passive": False},
                                "auto_enabled": False,
                                "statistics": {
                                    "general": {
                                        "hellos": "29/0",
                                        "jps": "0/0",
                                        "asserts": "0/0",
                                        "df_offers": "0/0",
                                        "graft_acks": "0/0",
                                        "grafts": "0/0",
                                        "df_backoffs": "0/0",
                                        "df_passes": "0/0",
                                        "df_winners": "0/0",
                                    },
                                    "last_reset": "never",
                                    "errors": {
                                        "checksum": 0,
                                        "invalid_df_subtypes": 0,
                                        "invalid_packet_types": 0,
                                        "authentication_failed": 0,
                                        "packet_length_errors": 0,
                                        "bad_version_packets": 0,
                                        "packets_from_self": 0,
                                        "packets_from_non_neighbors": 0,
                                        "packets_received_on_passiveinterface": 0,
                                        "jps_received_on_rpf_interface": 0,
                                        "joins_received_with_bidir_groups": 0,
                                        "joins_received_with_no_rp": 0,
                                        "joins_received_with_ssm_groups": 0,
                                        "joins_received_with_wrong_rp": 0,
                                        "jps_filtered_by_inbound_policy": 0,
                                        "jps_filtered_by_outbound_policy": 0,
                                    },
                                },
                                "address": ["2001:5:5:5::5/128", " Errors:"],
                            }
                        }
                    },
                }
            },
        }
    }


    golden_output_v6_pim_interface_2 = {'execute.return_value': '''
        R1#show ipv6 pim interface vrf all
        PIM Interface Status for VRF "VRF1"
        Ethernet1/1.11, Interface status: protocol-up/link-up/admin-up
          IPv6 address: 
            2001:10:3:5::5/64 [VALID]
          PIM DR: fe80::282:eaff:feed:1b08, DR's priority: 1
          PIM neighbor count: 1
          PIM hello interval: 30 secs, next hello sent in: 00:00:08
          PIM neighbor holdtime: 105 secs
          PIM configured DR priority: 1
          PIM configured DR delay: 3 secs
          PIM border interface: no
          PIM GenID sent in Hellos: 0x2a5b3d03
          PIM Hello MD5-AH Authentication: disabled
          PIM Neighbor policy: none configured
          PIM Join-Prune inbound policy: none configured
          PIM Join-Prune outbound policy: none configured
          PIM Join-Prune interval: 1 minutes
          PIM Join-Prune next sending: 0 minutes
          PIM BFD enabled: no
          PIM passive interface: no
          PIM Auto Enabled: no
          PIM vPC-peer neighbor: 0::
          PIM Interface Statistics, last reset: never
            General (sent/received):
              Hellos: 29/29 (early: 0), JPs: 3/0, Asserts: 0/0
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
        Ethernet1/2.11, Interface status: protocol-up/link-up/admin-up
          IPv6 address: 
            2001:20:5:5::5/64 [VALID]
          PIM DR: fe80::282:94ff:fe2d:1b08, DR's priority: 1
          PIM neighbor count: 0
          PIM hello interval: 30 secs, next hello sent in: 00:00:17
          PIM neighbor holdtime: 105 secs
          PIM configured DR priority: 1
          PIM configured DR delay: 3 secs
          PIM border interface: no
          PIM GenID sent in Hellos: 0x30aaaac9
          PIM Hello MD5-AH Authentication: disabled
          PIM Neighbor policy: none configured
          PIM Join-Prune inbound policy: none configured
          PIM Join-Prune outbound policy: none configured
          PIM Join-Prune interval: 1 minutes
          PIM Join-Prune next sending: 0 minutes
          PIM BFD enabled: no
          PIM passive interface: no
          PIM Auto Enabled: no
          PIM vPC-peer neighbor: 0::
          PIM Interface Statistics, last reset: never
            General (sent/received):
              Hellos: 28/0 (early: 0), JPs: 0/0, Asserts: 0/0
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
        Ethernet1/3.11, Interface status: protocol-up/link-up/admin-up
          IPv6 address: 
            2001:10:4:5::5/64 [VALID]
          PIM DR: fe80::282:94ff:fe2d:1b08, DR's priority: 1
          PIM neighbor count: 1
          PIM hello interval: 30 secs, next hello sent in: 00:00:24
          PIM neighbor holdtime: 105 secs
          PIM configured DR priority: 1
          PIM configured DR delay: 3 secs
          PIM border interface: no
          PIM GenID sent in Hellos: 0x1c0ede6c
          PIM Hello MD5-AH Authentication: disabled
          PIM Neighbor policy: none configured
          PIM Join-Prune inbound policy: none configured
          PIM Join-Prune outbound policy: none configured
          PIM Join-Prune interval: 1 minutes
          PIM Join-Prune next sending: 0 minutes
          PIM BFD enabled: no
          PIM passive interface: no
          PIM Auto Enabled: no
          PIM vPC-peer neighbor: 0::
          PIM Interface Statistics, last reset: never
            General (sent/received):
              Hellos: 29/28 (early: 0), JPs: 16/0, Asserts: 0/0
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
        loopback11, Interface status: protocol-up/link-up/admin-up
          IPv6 address: 
            2001:5:5:5::5/128 [VALID]
          PIM DR: fe80::250:56ff:fe82:942d, DR's priority: 1
          PIM neighbor count: 0
          PIM hello interval: 30 secs, next hello sent in: 00:00:18
          PIM neighbor holdtime: 105 secs
          PIM configured DR priority: 1
          PIM configured DR delay: 3 secs
          PIM border interface: no
          PIM GenID sent in Hellos: 0x1c0aa317
          PIM Hello MD5-AH Authentication: disabled
          PIM Neighbor policy: none configured
          PIM Join-Prune inbound policy: none configured
          PIM Join-Prune outbound policy: none configured
          PIM Join-Prune interval: 1 minutes
          PIM Join-Prune next sending: 0 minutes
          PIM BFD enabled: no
          PIM passive interface: no
          PIM Auto Enabled: no
          PIM vPC-peer neighbor: 0::
          PIM Interface Statistics, last reset: never
            General (sent/received):
              Hellos: 29/0 (early: 0), JPs: 0/0, Asserts: 0/0
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
        Ethernet1/1.10, Interface status: protocol-up/link-up/admin-up
          IPv6 address: 
            2001:10:3:5::5/64 [VALID]
          PIM DR: fe80::282:eaff:feed:1b08, DR's priority: 1
          PIM neighbor count: 1
          PIM hello interval: 30 secs, next hello sent in: 00:00:09
          PIM neighbor holdtime: 105 secs
          PIM configured DR priority: 1
          PIM configured DR delay: 3 secs
          PIM border interface: no
          PIM GenID sent in Hellos: 0x0e0ec63f
          PIM Hello MD5-AH Authentication: disabled
          PIM Neighbor policy: none configured
          PIM Join-Prune inbound policy: none configured
          PIM Join-Prune outbound policy: none configured
          PIM Join-Prune interval: 1 minutes
          PIM Join-Prune next sending: 0 minutes
          PIM BFD enabled: no
          PIM passive interface: no
          PIM Auto Enabled: no
          PIM vPC-peer neighbor: 0::
          PIM Interface Statistics, last reset: never
            General (sent/received):
              Hellos: 29/29 (early: 0), JPs: 3/0, Asserts: 0/0
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
        Ethernet1/2.10, Interface status: protocol-up/link-up/admin-up
          IPv6 address: 
            2001:20:5:5::5/64 [VALID]
          PIM DR: fe80::282:94ff:fe2d:1b08, DR's priority: 1
          PIM neighbor count: 0
          PIM hello interval: 30 secs, next hello sent in: 00:00:18
          PIM neighbor holdtime: 105 secs
          PIM configured DR priority: 1
          PIM configured DR delay: 3 secs
          PIM border interface: no
          PIM GenID sent in Hellos: 0x0f5cdda1
          PIM Hello MD5-AH Authentication: disabled
          PIM Neighbor policy: none configured
          PIM Join-Prune inbound policy: none configured
          PIM Join-Prune outbound policy: none configured
          PIM Join-Prune interval: 1 minutes
          PIM Join-Prune next sending: 0 minutes
          PIM BFD enabled: no
          PIM passive interface: no
          PIM Auto Enabled: no
          PIM vPC-peer neighbor: 0::
          PIM Interface Statistics, last reset: never
            General (sent/received):
              Hellos: 28/0 (early: 0), JPs: 0/0, Asserts: 0/0
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
        Ethernet1/3.10, Interface status: protocol-up/link-up/admin-up
          IPv6 address: 
            2001:10:4:5::5/64 [VALID]
          PIM DR: fe80::282:94ff:fe2d:1b08, DR's priority: 1
          PIM neighbor count: 1
          PIM hello interval: 30 secs, next hello sent in: 00:00:12
          PIM neighbor holdtime: 105 secs
          PIM configured DR priority: 1
          PIM configured DR delay: 3 secs
          PIM border interface: no
          PIM GenID sent in Hellos: 0x01ea02dd
          PIM Hello MD5-AH Authentication: disabled
          PIM Neighbor policy: none configured
          PIM Join-Prune inbound policy: none configured
          PIM Join-Prune outbound policy: none configured
          PIM Join-Prune interval: 1 minutes
          PIM Join-Prune next sending: 0 minutes
          PIM BFD enabled: no
          PIM passive interface: no
          PIM Auto Enabled: no
          PIM vPC-peer neighbor: 0::
          PIM Interface Statistics, last reset: never
            General (sent/received):
              Hellos: 29/28 (early: 0), JPs: 16/0, Asserts: 0/0
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
        loopback0, Interface status: protocol-up/link-up/admin-up
          IPv6 address: 
            2001:5:5:5::5/128 [VALID]
          PIM DR: fe80::250:56ff:fe82:942d, DR's priority: 1
          PIM neighbor count: 0
          PIM hello interval: 30 secs, next hello sent in: 00:00:16
          PIM neighbor holdtime: 105 secs
          PIM configured DR priority: 1
          PIM configured DR delay: 3 secs
          PIM border interface: no
          PIM GenID sent in Hellos: 0x0cb530a6
          PIM Hello MD5-AH Authentication: disabled
          PIM Neighbor policy: none configured
          PIM Join-Prune inbound policy: none configured
          PIM Join-Prune outbound policy: none configured
          PIM Join-Prune interval: 1 minutes
          PIM Join-Prune next sending: 0 minutes
          PIM BFD enabled: no
          PIM passive interface: no
          PIM Auto Enabled: no
          PIM vPC-peer neighbor: 0::
          PIM Interface Statistics, last reset: never
            General (sent/received):
              Hellos: 29/0 (early: 0), JPs: 0/0, Asserts: 0/0
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
        obj = ShowIpv6PimInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_pim_interface(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_v6_pim_interface_1)
        obj = ShowIpv6PimInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_v6_pim_interface_1)

    def test_golden_pim_interface_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_v6_pim_interface_2)
        obj = ShowIpv6PimInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_v6_pim_interface_2)



# ============================================
# Parser for 'show ipv6 pim rp vrf all'
# ============================================
class test_show_ipv6_pim_rp_vrf_all(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_rp_1 = {
        "vrf": {
            "VRF1": {
                 "address_family": {
                      "ipv6": {
                           "rp": {
                                "rp_list": {
                                     "2001:db8:1:1::1 SM bootstrap": {
                                          "df_ordinal": 0,
                                          "info_source_address": "2001:db8:1:1::1",
                                          "info_source_type": "bootstrap",
                                          "mode": "SM",
                                          "group_ranges": "ff05::1/8",
                                          "expiration": "00:02:20",
                                          "priority": 192,
                                          "up_time": "03:29:13",
                                          "address": "2001:db8:1:1::1"
                                     }
                                },
                                "rp_mappings": {
                                     "ff05::1/8 2001:db8:1:1::1 bootstrap": {
                                          "group": "ff05::1/8",
                                          "rp_address": "2001:db8:1:1::1",
                                          "expiration": "00:02:20",
                                          "protocol": "bootstrap",
                                          "up_time": "03:29:13"
                                     }
                                },
                                "bsr": {
                                     "bsr_address": {
                                          "2001:db8:1:1::1": {
                                               "mode": "SM",
                                               "policy": "ff05::1/8",
                                               "priority": 192,
                                               "address": "2001:db8:1:1::1"
                                          }
                                     },
                                     "bsr": {
                                          "priority": 99,
                                          "hash_mask_length": 128,
                                          "expires": "00:01:37",
                                          "address": "2001:db8:1:1::1",
                                          "up_time": "00:09:14"
                                     },
                                     "bsr_candidate": {
                                          "hash_mask_length": 128,
                                          "priority": 99,
                                          "address": "2001:db8:1:1::1"
                                     },
                                     "rp": {
                                          "rp_address": "2001:db8:1:1::1",
                                          "group_policy": "ff05::1/8",
                                          "up_time": "03:29:13"
                                     },
                                     "rp_candidate_next_advertisement": "00:02:20"
                                }
                           },
                           "sm": {
                                "asm": {
                                     "anycast_rp": {
                                          "2001:db8:111:111::111 2001:db8:3:4::5": {
                                               "anycast_address": "2001:db8:111:111::111"
                                          },
                                          "2001:db8:111:111::111 2001:db8:1:2::2": {
                                               "anycast_address": "2001:db8:111:111::111"
                                          }
                                     }
                                }
                           }
                      }
                 }
            },
            "default": {
                 "address_family": {
                      "ipv6": {
                           "rp": {
                                "rp_list": {
                                     "2001:db8:1:1::1 SM bootstrap": {
                                          "df_ordinal": 0,
                                          "info_source_address": "2001:db8:1:1::1",
                                          "info_source_type": "bootstrap",
                                          "mode": "SM",
                                          "group_ranges": "ff05::1/8",
                                          "expiration": "00:02:20",
                                          "priority": 192,
                                          "up_time": "03:29:13",
                                          "address": "2001:db8:1:1::1"
                                     },
                                     "2001:db8:504::1 SM static": {
                                          "expiration": "0.000000",
                                          "info_source_type": "static",
                                          "mode": "SM",
                                          "group_ranges": "ff1e::3002/128 ff1e::3001/128",
                                          "df_ordinal": 0,
                                          "up_time": "00:00:02",
                                          "address": "2001:db8:504::1"
                                     },
                                     "2001:db8:12:12::12 BIDIR static": {
                                          "expiration": "0.000000",
                                          "info_source_type": "static",
                                          "mode": "BIDIR",
                                          "group_ranges": "ff08::/16",
                                          "df_ordinal": 7,
                                          "up_time": "00:58:17",
                                          "address": "2001:db8:12:12::12"
                                     },
                                     "2001:db8:111:111::111 SM static": {
                                          "expiration": "0.000000",
                                          "info_source_type": "static",
                                          "mode": "SM",
                                          "group_ranges": "ff09::/16",
                                          "df_ordinal": 0,
                                          "up_time": "00:00:52",
                                          "address": "2001:db8:111:111::111"
                                     }
                                },
                                "rp_mappings": {
                                     "ff09::/16 2001:db8:111:111::111 static": {
                                          "group": "ff09::/16",
                                          "rp_address": "2001:db8:111:111::111",
                                          "expiration": "0.000000",
                                          "protocol": "static",
                                          "up_time": "00:00:52"
                                     },
                                     "ff05::1/8 2001:db8:1:1::1 bootstrap": {
                                          "group": "ff05::1/8",
                                          "rp_address": "2001:db8:1:1::1",
                                          "expiration": "00:02:20",
                                          "protocol": "bootstrap",
                                          "up_time": "03:29:13"
                                     },
                                     "ff08::/16 2001:db8:12:12::12 static": {
                                          "group": "ff08::/16",
                                          "rp_address": "2001:db8:12:12::12",
                                          "expiration": "0.000000",
                                          "protocol": "static",
                                          "up_time": "00:58:17"
                                     },
                                     "ff1e::3002/128 ff1e::3001/128 2001:db8:504::1 static": {
                                          "group": "ff1e::3002/128 ff1e::3001/128",
                                          "rp_address": "2001:db8:504::1",
                                          "expiration": "0.000000",
                                          "protocol": "static",
                                          "up_time": "00:00:02"
                                     }
                                },
                                "static_rp": {
                                     "2001:db8:111:111::111": {
                                          "sm": {
                                               "policy_name": "ff09::/16"
                                          }
                                     },
                                     "2001:db8:504::1": {
                                          "sm": {
                                               "route_map": "PIM6-STATIC-RP",
                                               "policy_name": "ff1e::3002/128 ff1e::3001/128"
                                          }
                                     },
                                     "2001:db8:12:12::12": {
                                          "bidir": {
                                               "policy_name": "ff08::/16"
                                          }
                                     }
                                },
                                "bsr": {
                                     "bsr_address": {
                                          "2001:db8:1:1::1": {
                                               "mode": "SM",
                                               "policy": "ff05::1/8",
                                               "priority": 192,
                                               "address": "2001:db8:1:1::1"
                                          }
                                     },
                                     "bsr": {
                                          "hash_mask_length": 128,
                                          "priority": 99,
                                          "address": "2001:db8:1:1::1"
                                     },
                                     "bsr_candidate": {
                                          "hash_mask_length": 128,
                                          "priority": 99,
                                          "address": "2001:db8:1:1::1"
                                     },
                                     "rp": {
                                          "rp_address": "2001:db8:1:1::1",
                                          "group_policy": "ff05::1/8",
                                          "up_time": "03:29:13"
                                     },
                                     "bsr_next_bootstrap": "00:00:15",
                                     "rp_candidate_next_advertisement": "00:02:20"
                                }
                           },
                           "sm": {
                                "asm": {
                                     "anycast_rp": {
                                          "2001:db8:111:111::111 2001:db8:3:4::5": {
                                               "anycast_address": "2001:db8:111:111::111"
                                          },
                                          "2001:db8:111:111::111 2001:db8:1:2::2": {
                                               "anycast_address": "2001:db8:111:111::111"
                                          }
                                     }
                                }
                           }
                      }
                 }
            }
       }
    }
    golden_output_rp_1 = {'execute.return_value': '''
        R1# show ipv6 pim rp vrf all
        PIM6 RP Status Information for VRF "default"
        BSR: 2001:db8:1:1::1*, next Bootstrap message in: 00:00:15,
              priority: 99, hash-length: 128
        Auto-RP disabled
        BSR RP Candidate policy: None
        BSR RP policy: None
        Auto-RP Announce policy: None
        Auto-RP Discovery policy: None

        Anycast-RP 2001:db8:111:111::111 members:
          2001:db8:1:2::2  2001:db8:3:4::5

        RP: 2001:db8:1:1::1*, (0), uptime: 03:29:13, expires: 00:02:20,
         priority: 192, RP-source: 2001:db8:1:1::1 (B), group ranges:
              ff05::1/8
        RP: 2001:db8:12:12::12, (7), uptime: 00:58:17, expires: 0.000000,
         priority: 0, RP-source: (local), group ranges:
              ff08::/16 (bidir)
        RP: 2001:db8:111:111::111, (0), uptime: 00:00:52, expires: 0.000000,
         priority: 0, RP-source: (local), group ranges:
              ff09::/16
        RP: 2001:db8:504::1, (0), uptime: 00:00:02, expires: 0.000000,
         priority: 0, RP-source: (local), group-map: PIM6-STATIC-RP, group ranges:
              ff1e::3002/128 ff1e::3001/128

        PIM6 RP Status Information for VRF "VRF1"
        BSR: 2001:db8:1:1::1, uptime: 00:09:14, expires: 00:01:37,
              priority: 99, hash-length: 128
        Auto-RP disabled
        BSR RP Candidate policy: None
        BSR RP policy: None
        Auto-RP Announce policy: None
        Auto-RP Discovery policy: None

        Anycast-RP 2001:db8:111:111::111 members:
          2001:db8:1:2::2  2001:db8:3:4::5

        RP: 2001:db8:1:1::1*, (0), uptime: 03:29:13, expires: 00:02:20,
         priority: 192, RP-source: 2001:db8:1:1::1 (B), group ranges:
              ff05::1/8
    '''}


    golden_output_rp_2 = {'execute.return_value': '''
        R2_nx# show ipv6 pim rp vrf all
        PIM6 RP Status Information for VRF "default"
        BSR: Not Operational
        Auto-RP disabled
        BSR RP Candidate policy: None
        BSR RP policy: None
        Auto-RP Announce policy: None
        Auto-RP Discovery policy: None
        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6PimRp(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_ip_pim_rp_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_rp_1)
        obj = ShowIpv6PimRp(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output_rp_1)


    def test_golden_ip_pim_rp_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_rp_2)
        obj = ShowIpv6PimRp(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='all')


# ============================================
# Parser for 'show ipv6 pim df vrf all'
# ============================================
class test_show_ipv6_pim_df(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_v6_df_vrf_1 = {
        'vrf':{
            'default':
                {
                'address_family':
                    {'ipv6':
                        {
                        'rp':{
                            'bidir':{
                                'interface_df_election':{
                                    '2001:db8:1:1::1 Ethernet2/1':{
                                        'address': '2001:db8:1:1::1',
                                        'interface_name': 'Ethernet2/1',
                                        'metric_pref': 0,
                                        'metric': 0,
                                        'group_range': 'ff09::/16',
                                        'df_address': 'fe80::5054:ff:fe89:740c',
                                        'interface_state': 'win',
                                        'winner_metric_pref': 0,
                                        'winner_metric': 0,
                                        'df_uptime': '00:00:48',
                                        'df_ordinal': 8,

                                    },
                                    '2001:db8:1:1::1 Ethernet2/5': {
                                        'address': '2001:db8:1:1::1',
                                        'interface_name': 'Ethernet2/5',
                                        'metric_pref': 0,
                                        'metric': 0,
                                        'group_range': 'ff09::/16',
                                        'df_address': 'fe80::5054:ff:fe89:740c',
                                        'interface_state': 'win',
                                        'winner_metric_pref': 0,
                                        'winner_metric': 0,
                                        'df_uptime': '00:00:48',
                                        'df_ordinal': 8,

                                    },
                                    '2001:db8:1:1::1 Loopback0': {
                                        'address': '2001:db8:1:1::1',
                                        'interface_name': 'Loopback0',
                                        'metric_pref': 0,
                                        'metric': 0,
                                        'group_range': 'ff09::/16',
                                        'df_address': '0::',
                                        'interface_state': 'lose',
                                        'winner_metric_pref': 0,
                                        'winner_metric': 0,
                                        'df_uptime': '00:00:48',
                                        'df_ordinal': 8,

                                    },
                                    '2001:db8:12:12::12 Ethernet2/1': {
                                        'address': '2001:db8:12:12::12',
                                        'interface_name': 'Ethernet2/1',
                                        'metric_pref': -1,
                                        'metric': -1,
                                        'group_range': 'ff08::/16',
                                        'df_address': '0::',
                                        'interface_state': 'lose',
                                        'winner_metric_pref': -1,
                                        'winner_metric': -1,
                                        'df_uptime': '00:01:27',
                                        'df_ordinal': 7,
                                    },
                                    '2001:db8:12:12::12 Ethernet2/5': {
                                        'address': '2001:db8:12:12::12',
                                        'interface_name': 'Ethernet2/5',
                                        'metric_pref': -1,
                                        'metric': -1,
                                        'group_range': 'ff08::/16',
                                        'df_address': '0::',
                                        'interface_state': 'lose',
                                        'winner_metric_pref': -1,
                                        'winner_metric': -1,
                                        'df_uptime': '00:01:27',
                                        'df_ordinal': 7,
                                    },
                                    '2001:db8:12:12::12 Loopback0': {
                                        'address': '2001:db8:12:12::12',
                                        'interface_name': 'Loopback0',
                                        'metric_pref': -1,
                                        'metric': -1,
                                        'group_range': 'ff08::/16',
                                        'df_address': '0::',
                                        'interface_state': 'lose',
                                        'winner_metric_pref': -1,
                                        'winner_metric': -1,
                                        'df_uptime': '00:01:27',
                                        'df_ordinal': 7,
                                    },

                               },
                            },
                        },
                    },
                },
            },
        },
    }
    golden_output_vrf_df_1 = {'execute.return_value': '''
        R1# show ipv6 pim df vrf all
        Bidir-PIM6 Designated Forwarder Information for VRF "default"

        RP Address (ordinal)   RP Metric       Group Range
        2001:db8:1:1::1 (8)
                               [0/0]           ff09::/16

          Interface     DF Address                 DF State DF Metric  DF Uptime
          Eth2/1        fe80::5054:ff:fe89:740c    Winner   [0/0]      00:00:48
          Eth2/5        fe80::5054:ff:fe89:740c    Winner   [0/0]      00:00:48
          Lo0           0::                        Lose     [0/0]      00:00:48

        RP Address (ordinal)   RP Metric       Group Range
        2001:db8:12:12::12 (7)
                               [-1/-1]         ff08::/16

          Interface     DF Address                 DF State DF Metric  DF Uptime
          Eth2/1        0::                        Lose     [-1/-1]    00:01:27
          Eth2/5        0::                        Lose     [-1/-1]    00:01:27
          Lo0           0::                        Lose     [-1/-1]    00:01:27


        Bidir-PIM6 Designated Forwarder Information for VRF "VRF1"


    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6PimDf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_df_vrf_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_vrf_df_1)
        obj = ShowIpv6PimDf(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_v6_df_vrf_1)


# ============================================
# Parser for 'show ip pim df vrf all'
# ============================================
class test_show_ip_pim_df(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_df_vrf_1 = {
        'vrf':{
            'default':
                {
                'address_family':
                    {'ipv4':
                        {
                        'rp':{
                            'bidir':{
                                'interface_df_election':{
                                    '10.16.2.2 Loopback0':{
                                        'address': '10.16.2.2',
                                        'interface_name': 'Loopback0',
                                        'df_bits': '00000002 (1)',
                                        'metric_pref': 0,
                                        'metric': 0,
                                        'group_range': '224.128.0.0/9',
                                        'df_address': '10.4.1.1',
                                        'interface_state': 'win',
                                        'winner_metric_pref': 0,
                                        'winner_metric': 0,
                                        'df_uptime': '00:28:14',
                                        'df_ordinal': 2,

                                    },
                                    '10.16.2.2 Ethernet2/2': {
                                        'address': '10.16.2.2',
                                        'interface_name': 'Ethernet2/2',
                                        'df_bits': '00000002 (1)',
                                        'metric_pref': 0,
                                        'metric': 0,
                                        'group_range': '224.128.0.0/9',
                                        'df_address': '10.2.0.2',
                                        'interface_state': 'lose',
                                        'winner_metric_pref': 0,
                                        'winner_metric': 0,
                                        'df_uptime': '00:28:14',
                                        'df_ordinal': 2,
                                        'is_rpf': True,

                                    },
                               },
                            },
                        },
                    },
                },
            },
            'VRF1':
                {
                'address_family':
                    {'ipv4':
                        {
                        'rp': {
                            'bidir': {
                                'interface_df_election': {
                                    '10.66.12.12 Loopback1': {
                                        'address': '10.66.12.12',
                                        'interface_name': 'Loopback1',
                                        'df_bits': '00000002 (1)',
                                        'metric_pref': 0,
                                        'metric': 0,
                                        'group_range': '224.128.0.0/9',
                                        'df_address': '10.4.1.1',
                                        'interface_state': 'win',
                                        'winner_metric_pref': 0,
                                        'winner_metric': 0,
                                        'df_uptime': '02:28:14',
                                        'df_ordinal': 3,

                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }
    golden_output_vrf_df_1 = {'execute.return_value': '''
        R1# show ip pim df vrf all
        Bidir-PIM Designated Forwarder Information for VRF "default"
        RP Address (ordinal)   DF-bits          RP Metric  Group Range
        10.16.2.2 (2)            00000002 (1)     [0/0]      224.128.0.0/9

          Interface            DF Address       DF State   DF Metric    DF Uptime
          Loopback0            10.4.1.1          Winner     [0/0]        00:28:14
          Ethernet2/2                 10.2.0.2         Lose       [0/0]        00:28:14  (RPF)

        Bidir-PIM Designated Forwarder Information for VRF "VRF1"
        RP Address (ordinal)   DF-bits          RP Metric  Group Range
        10.66.12.12 (3)            00000002 (1)     [0/0]      224.128.0.0/9

          Interface            DF Address       DF State   DF Metric    DF Uptime
          Loopback1            10.4.1.1          Winner     [0/0]        02:28:14

    '''}

    golden_output_vrf_df_2= {'execute.return_value': '''
            R1# show ip pim df vrf all
            Bidir-PIM Designated Forwarder Information for VRF "default"

            '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpPimDf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_df_vrf_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_vrf_df_1)
        obj = ShowIpPimDf(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_df_vrf_1)

    def test_golden_df_vrf_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_vrf_df_2)
        obj = ShowIpPimDf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ============================================
# Parser for 'show ipv6 pim route vrf all'
# ============================================
class test_show_ipv6_pim_route(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_v6_route_1 = {
        'vrf':{
            'VRF1':
                {
                'address_family':
                    {'ipv6':
                         {
                         'topology_tree_info': {
                                'ff30::/12 * True': {
                                    'group': 'ff30::/12',
                                    'source_address': '*',
                                    'is_rpt': True,
                                    'expiration': '00:00:27',
                                    'incoming_interface': 'Null',
                                    'rpf_neighbor': '0::',
                                    'jp_holdtime_roundup': 3,
                                    'oif': '00000000',
                                    'oif_count': 0,
                                    'oif_timeout_count': 0,
                                    'oif_timeout': '00000000',
                                    'immediate': '00000000',
                                    'immediate_count': 0,
                                    'immediate_timeout_count': 0,
                                    'immediate_timeout': '00000000',
                                    'timeout_interval': 3,
                                    'route_fabric_owned': False,
                                },
                         },
                    },
                },
            },
            'default':
                {
                'address_family':
                    {'ipv6':
                         {
                         'topology_tree_info': {
                                'ff08::/16 * True': {
                                    'group': 'ff08::/16',
                                    'source_address': '*',
                                    'is_rpt': True,
                                    'rp_bit': True,
                                    'expiration': '00:02:31',
                                    'incoming_interface': 'Null',
                                    'rpf_neighbor': '0::',
                                    'jp_holdtime_roundup': 3,
                                    'oif': '00000000',
                                    'oif_count': 0,
                                    'oif_timeout_count': 0,
                                    'oif_timeout': '00000000',
                                    'timeout_interval': 2,
                                    'mode': 'bidir',
                                    'rp_address': '2001:db8:12:12::12',
                                    'route_fabric_owned': False,
                                    },
                                'ff30::/12 * True': {
                                    'group': 'ff30::/12',
                                    'source_address': '*',
                                    'is_rpt': True,
                                    'expiration': '00:02:31',
                                    'incoming_interface': 'Null0',
                                    'rpf_neighbor': '0::',
                                    'jp_holdtime_roundup': 3,
                                    'oif': '00000000',
                                    'oif_count': 0,
                                    'oif_timeout_count': 0,
                                    'oif_timeout': '00000000',
                                    'timeout_interval': 3,
                                    'route_fabric_owned': False,
                                    'immediate': '00000000',
                                    'immediate_count': 0,
                                    'immediate_timeout_count': 0,
                                    'immediate_timeout': '00000000',
                                 },
                         },
                    },
                },
            },
        },
    }
    golden_output_v6_route_1 = {'execute.return_value': '''
    R1# show ipv6 pim route vrf all
    PIM6 Routing Table for VRF "default" - 2 entries

    (*, ff08::/16), RP 2001:db8:12:12::12, bidir, expires 00:02:31 Route Fabric owned : FALSE, RP-bit
      Incoming interface: Null, RPF nbr 0::
      Oif-list: (0) 00000000, timeout-list: (0) 00000000
      Timeout-interval: 2, JP-holdtime round-up: 3

    (*, ff30::/12), expires 00:02:31 Route Fabric owned : FALSE
      Incoming interface: Null0, RPF nbr 0::
      Oif-list:       (0) 00000000, timeout-list: (0) 00000000
      Immediate-list: (0) 00000000, timeout-list: (0) 00000000
      Timeout-interval: 3, JP-holdtime round-up: 3


    PIM6 Routing Table for VRF "VRF1" - 1 entries

    (*, ff30::/12), expires 00:00:27 Route Fabric owned : FALSE
      Incoming interface: Null, RPF nbr 0::
      Oif-list:       (0) 00000000, timeout-list: (0) 00000000
      Immediate-list: (0) 00000000, timeout-list: (0) 00000000
      Timeout-interval: 3, JP-holdtime round-up: 3
    '''}


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6PimRoute(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_ipv6_pim_route_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_v6_route_1)
        obj = ShowIpv6PimRoute(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_v6_route_1)


# ============================================
# Parser for 'show ipv6 pim neighbor'
# ============================================
class test_show_ipv6_pim_neighbor(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output_ipv6_neighbor_1 = {
        'vrf':{
            'VRF1':
                {
                'interfaces':{
                    'Ethernet2/2':{
                        'address_family':{
                            'ipv6':{
                                'neighbors':{
                                   'fe80::5054:ff:fe5b:aa80':{
                                       'bfd_status': False,
                                       'expiration': '00:01:28',
                                       'dr_priority': 1,
                                       'up_time': '07:31:36',
                                       'interface': 'Ethernet2/2',
                                       'bidir_capable': True,
                                       'ecmp_redirect_capable': False

                                    },
                                    'secondary_address':['2001:db8:11:33::33','2001:db8:1:3::3']
                                },
                            },
                        },

                    },
                },
            },
            'default':
                {
                    'interfaces': {
                        'Ethernet2/4': {
                            'address_family': {
                                'ipv6': {
                                    'neighbors': {
                                        'fe80::5054:ff:fec2:b74f': {
                                            'bfd_status': False,
                                            'expiration': '00:01:21',
                                            'dr_priority': 1,
                                            'up_time': '6d19h',
                                            'interface': 'Ethernet2/4',
                                            'bidir_capable': True,
                                            'ecmp_redirect_capable': False

                                        },
                                        'secondary_address': ['2001:10:1:2::2']
                                    },
                                },
                            },

                        },
                    },
                },
        },
    }

    golden_output_ipv6_neighbor_1 = {'execute.return_value': '''
    PIM6 Neighbor Status for VRF "default"
    Neighbor Address              Interface   Uptime    Expires   DR   Bidir-  BFD
                                                                  Pri  Capable State

    fe80::5054:ff:fec2:b74f       Eth2/4      6d19h     00:01:21  1    yes     n/a
      Secondary addresses:
        2001:10:1:2::2

    PIM6 Neighbor Status for VRF "VRF1"
    Neighbor Address              Interface   Uptime    Expires   DR   Bidir-  BFD
                                                                  Pri  Capable State
    fe80::5054:ff:fe5b:aa80       Eth2/2      07:31:36  00:01:28  1    yes     n/a
      Secondary addresses:
        2001:db8:11:33::33
        2001:db8:1:3::3

    '''}


    golden_output_ipv6_neighbor_2 = {'execute.return_value': '''
    R1# show ip pim neighbor vrf all
    PIM6 Neighbor Status for VRF "VRF1"
    Neighbor        Interface            Uptime    Expires   DR       Bidir-  BFD
                                                             Priority Capable State
        '''}

    golden_parsed_output_ipv6_neighbor_3 = {
        'vrf': {
            'default':
                {
                    'interfaces': {
                        'Ethernet2/4': {
                            'address_family': {
                                'ipv6': {
                                    'neighbors': {
                                        'fe80::5054:ff:fec2:b74f': {
                                            'bfd_status': False,
                                            'expiration': '00:01:21',
                                            'dr_priority': 1,
                                            'up_time': '6d19h',
                                            'interface': 'Ethernet2/4',
                                            'bidir_capable': True,
                                            'ecmp_redirect_capable': False

                                        },
                                        'secondary_address': ['2001:10:1:2::2']
                                    },
                                },
                            },

                        },
                    },
                },
            },
        }

    golden_output_ipv6_neighbor_3 = {'execute.return_value': '''
        PIM6 Neighbor Status for VRF "default"
        Neighbor Address              Interface   Uptime    Expires   DR   Bidir-  BFD
                                                                      Pri  Capable State

        fe80::5054:ff:fec2:b74f       Eth2/4      6d19h     00:01:21  1    yes     n/a
          Secondary addresses:
            2001:10:1:2::2

        '''}

    golden_parsed_output_ipv6_neighbor_4 = {
        "vrf": {
            "VRF1": {
                "interfaces": {
                    "Ethernet1/1.11": {
                        "address_family": {
                            "ipv6": {
                                "neighbors": {
                                    "fe80::282:eaff:feed:1b08": {
                                        "bfd_status": False,
                                        "expiration": "00:01:37",
                                        "dr_priority": 1,
                                        "up_time": "00:12:53",
                                        "interface": "Ethernet1/1.11",
                                        "bidir_capable": True,
                                        "ecmp_redirect_capable": False ,
                                    },
                                    "secondary_address": [
                                        "2001:10:3:5::3",
                                        "2001:10:4:5::4",
                                    ],
                                }
                            }
                        }
                    },
                    "Ethernet1/3.11": {
                        "address_family": {
                            "ipv6": {
                                "neighbors": {
                                    "fe80::282:85ff:fe4e:1b08": {
                                        "bfd_status": False,
                                        "expiration": "00:01:29",
                                        "dr_priority": 1,
                                        "up_time": "00:12:59",
                                        "interface": "Ethernet1/3.11",
                                        "bidir_capable": True,
                                        "ecmp_redirect_capable": False,
                                    },
                                    "secondary_address": [
                                        "2001:10:3:5::3",
                                        "2001:10:4:5::4",
                                    ],
                                }
                            }
                        }
                    },
                }
            },
            "default": {
                "interfaces": {
                    "Ethernet1/1.10": {
                        "address_family": {
                            "ipv6": {
                                "neighbors": {
                                    "fe80::282:eaff:feed:1b08": {
                                        "bfd_status": False,
                                        "expiration": "00:01:38",
                                        "dr_priority": 1,
                                        "up_time": "00:12:53",
                                        "interface": "Ethernet1/1.10",
                                        "bidir_capable": True,
                                        "ecmp_redirect_capable": False,
                                    },
                                    "secondary_address": [
                                        "2001:10:3:5::3",
                                        "2001:10:4:5::4",
                                    ],
                                }
                            }
                        }
                    },
                    "Ethernet1/3.10": {
                        "address_family": {
                            "ipv6": {
                                "neighbors": {
                                    "fe80::282:85ff:fe4e:1b08": {
                                        "bfd_status": False,
                                        "expiration": "00:01:35",
                                        "dr_priority": 1,
                                        "up_time": "00:12:59",
                                        "interface": "Ethernet1/3.10",
                                        "bidir_capable": True,
                                        "ecmp_redirect_capable": False,
                                    },
                                    "secondary_address": [
                                        "2001:10:3:5::3",
                                        "2001:10:4:5::4",
                                    ],
                                }
                            }
                        }
                    },
                }
            },
        }
    }

    golden_output_ipv6_neighbor_4 = {'execute.return_value': '''
        #show ipv6 pim neighbor vrf all

        PIM Neighbor Status for VRF "VRF1"
        Neighbor                     Interface            Uptime    Expires   DR       Bidir-  BFD     ECMP Redirect
                                                                              Priority Capable State   Capable
        fe80::282:eaff:feed:1b08     Ethernet1/1.11       00:12:53  00:01:37  1        yes     n/a     no
           Secondary addresses:
            2001:10:3:5::3
        fe80::282:85ff:fe4e:1b08     Ethernet1/3.11       00:12:59  00:01:29  1        yes     n/a     no
           Secondary addresses:
            2001:10:4:5::4

        PIM Neighbor Status for VRF "default"
        Neighbor                     Interface            Uptime    Expires   DR       Bidir-  BFD     ECMP Redirect
                                                                              Priority Capable State   Capable
        fe80::282:eaff:feed:1b08     Ethernet1/1.10       00:12:53  00:01:38  1        yes     n/a     no
           Secondary addresses:
            2001:10:3:5::3
        fe80::282:85ff:fe4e:1b08     Ethernet1/3.10       00:12:59  00:01:35  1        yes     n/a     no
           Secondary addresses:
            2001:10:4:5::4

    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6PimNeighbor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_ip_pim_neighbor_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_ipv6_neighbor_1)
        obj = ShowIpv6PimNeighbor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_ipv6_neighbor_1)

    def test_golden_ip_pim_neighbor_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_ipv6_neighbor_2)
        obj = ShowIpv6PimNeighbor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_ip_pim_neighbor_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_ipv6_neighbor_3)
        obj = ShowIpv6PimNeighbor(device=self.device)
        parsed_output = obj.parse(vrf='default')
        self.assertEqual(parsed_output, self.golden_parsed_output_ipv6_neighbor_3)

    def test_golden_ip_pim_neighbor_4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_ipv6_neighbor_4)
        obj = ShowIpv6PimNeighbor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_ipv6_neighbor_4)


# ============================================
# unittest  for 'show ip pim route'
# ============================================
class test_show_ip_pim_route(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_route_1 = {
        'vrf':{
            'VRF1':
                {
                'address_family':
                    {'ipv4':
                         {
                         'topology_tree_info': {
                                '232.0.0.0/8 * True': {
                                    'group': '232.0.0.0/8',
                                    'source_address': '*',
                                    'is_rpt': True,
                                    'expiration': '00:00:01',
                                    'incoming_interface': 'Null',
                                    'rpf_neighbor': '0.0.0.0',
                                    'jp_holdtime_roundup': 3,
                                    'oif': '00000000',
                                    'oif_count': 0,
                                    'oif_timeout_count': 0,
                                    'oif_timeout': '00000000',
                                    'immediate': '00000000',
                                    'immediate_count': 0,
                                    'immediate_timeout_count': 0,
                                    'immediate_timeout': '00000000',
                                    'timeout_interval': 3,
                                    'sgr_prune_count': 0,
                                    'sgr_prune': '00000000',
                                },
                         },
                    },
                },
            },
            'default':
                {
                'address_family':
                    {'ipv4':
                         {
                         'topology_tree_info': {
                                '231.0.0.1/24 * True': {
                                    'group': '231.0.0.1/24',
                                    'source_address': '*',
                                    'is_rpt': True,
                                    'expiration': '00:00:01',
                                    'incoming_interface': 'Null0',
                                    'rpf_neighbor': '0.0.0.0',
                                    'jp_holdtime_roundup': 3,
                                    'oif': '00000000',
                                    'oif_count': 0,
                                    'oif_timeout_count': 0,
                                    'oif_timeout': '00000000',
                                    'immediate': '00000000',
                                    'immediate_count': 0,
                                    'immediate_timeout_count': 0,
                                    'immediate_timeout': '00000000',
                                    'timeout_interval': 3,
                                    'sgr_prune_count': 0,
                                    'sgr_prune': '00000000',
                                    },
                                '233.0.0.0/24 * True': {
                                    'group': '233.0.0.0/24',
                                    'source_address': '*',
                                    'is_rpt': True,
                                    'rp_bit': True,
                                    'expiration': '00:01:58',
                                    'incoming_interface': 'Null',
                                    'rpf_neighbor': '0.0.0.0',
                                    'rp_address':'10.66.12.12',
                                    'mode':'bidir',
                                    'jp_holdtime_roundup': 3,
                                    'oif': '00000000',
                                    'oif_count': 0,
                                    'oif_timeout_count': 0,
                                    'oif_timeout': '00000000',
                                    'timeout_interval': 2,
                                    },
                                '238.0.0.0/24 * True': {
                                    'group': '238.0.0.0/24',
                                    'source_address': '*',
                                    'is_rpt': True,
                                    'rp_bit': True,
                                    'mode': 'bidir',
                                    'expiration': '00:01:58',
                                    'incoming_interface': 'loopback0',
                                    'rpf_neighbor': '10.4.1.1',
                                    'rp_address': '10.4.1.1',
                                    'jp_holdtime_roundup': 3,
                                    'oif': '00000000',
                                    'oif_count': 0,
                                    'oif_timeout_count': 0,
                                    'oif_timeout': '00000000',
                                    'timeout_interval': 2,
                             },
                         },
                    },
                },
            },
        },
    }
    golden_output_route_1 = {'execute.return_value': '''
    R1# show ip pim route vrf all
    PIM Routing Table for VRF "VRF1" - 1 entries

    (*, 232.0.0.0/8), expires 0.000000 (00:00:01)
      Incoming interface: Null, RPF nbr 0.0.0.0
      Oif-list:       (0) 00000000, timeout-list: (0) 00000000
      Immediate-list: (0) 00000000, timeout-list: (0) 00000000
      Sgr-prune-list: (0) 00000000
      Timeout-interval: 3, JP-holdtime round-up: 3


    PIM Routing Table for VRF "default" - 3 entries

    (*, 231.0.0.1/24), expires 0.000000 (00:00:01)
      Incoming interface: Null0, RPF nbr 0.0.0.0
      Oif-list:       (0) 00000000, timeout-list: (0) 00000000
      Immediate-list: (0) 00000000, timeout-list: (0) 00000000
      Sgr-prune-list: (0) 00000000
      Timeout-interval: 3, JP-holdtime round-up: 3

    (*, 233.0.0.0/24), RP 10.66.12.12, bidir, expires 00:01:58, RP-bit
      Incoming interface: Null, RPF nbr 0.0.0.0
      Oif-list: (0) 00000000, timeout-list: (0) 00000000
      Timeout-interval: 2, JP-holdtime round-up: 3

    (*, 238.0.0.0/24), RP 10.4.1.1*, bidir, expires 00:01:58, RP-bit
      Incoming interface: loopback0, RPF nbr 10.4.1.1
      Oif-list: (0) 00000000, timeout-list: (0) 00000000
      Timeout-interval: 2, JP-holdtime round-up: 3
    '''}


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpPimRoute(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_ip_pim_route_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_route_1)
        obj = ShowIpPimRoute(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_route_1)


# ============================================
# Parser for 'show ipv6 pim group-range vrf all'
# ============================================
class test_show_ipv6_pim_group_range(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_group_range_1 = {
        'vrf':{
            'default':
                {
                'address_family':{
                    'ipv6':{
                        'sm':{
                            'ssm':{
                               'ff3x::/32':{
                                   'mode': 'ssm',
                                    },
                                },
                            'asm':{
                                'ff05::1/8': {
                                'mode': 'asm',
                                'rp_address': '2001:db8:1:1::1',
                                    },
                                },
                            },
                        },
                    },
                },
            'VRF1':{
                'address_family': {
                    'ipv6': {
                        'sm': {
                            'ssm': {
                                'ff3x::/32': {
                                    'mode': 'ssm',
                                },
                            },
                        },
                    },
                },
            },
        },
    }
    golden_output_group_range_1 = {'execute.return_value': '''
        R1# show ipv6 pim group-range vrf all
        PIM6 Group-Range Configuration for VRF "default"
        Group-range               Mode      RP-address          Shared-tree-only range
        ff3x::/32                 SSM       -                   -
        ff05::1/8                 ASM       2001:db8:1:1::1

        PIM6 Group-Range Configuration for VRF "VRF1"
        Group-range               Mode      RP-address          Shared-tree-only range
        ff3x::/32                 SSM       -
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6PimGroupRange(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_ip_pim_group_range_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_group_range_1)
        obj = ShowIpv6PimGroupRange(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_group_range_1)


# ============================================
# Parser for 'show ip pim neighbor vrf all'
# ============================================
class test_show_ip_pim_neighbor(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_neighbor_1 = {
        'vrf':{
            'VRF1':
                {
                'interfaces':{
                    'Ethernet2/2':{
                        'address_family':{
                            'ipv4':{
                                'neighbors':{
                                   '10.11.33.33':{
                                       'bfd_status': False,
                                       'expiration': '00:01:25',
                                       'dr_priority': 1,
                                       'up_time': '07:31:30',
                                       'interface': 'Ethernet2/2',
                                       'bidir_capable': True,

                                    },
                                    '10.11.33.43': {
                                        'bfd_status': False,
                                        'expiration': '00:01:25',
                                        'dr_priority': 1,
                                        'up_time': '07:31:30',
                                        'interface': 'Ethernet2/2',
                                        'bidir_capable': True,

                                    },
                                },
                            },
                        },

                    },
                },
            },
        },
    }

    golden_output_neighbor_1 = {'execute.return_value': '''
    R1# show ip pim neighbor vrf all
    PIM Neighbor Status for VRF "VRF1"
    Neighbor        Interface            Uptime    Expires   DR       Bidir-  BFD
                                                             Priority Capable State
    10.11.33.33     Ethernet2/2          07:31:30  00:01:25  1        yes     n/a
    10.11.33.43     Ethernet2/2          07:31:30  00:01:25  1        yes     n/a

    PIM Neighbor Status for VRF "default"
    Neighbor        Interface            Uptime    Expires   DR       Bidir-  BFD
                                                         Priority Capable State
    '''}


    golden_output_neighbor_2 = {'execute.return_value': '''
    R1# show ip pim neighbor vrf all
    PIM Neighbor Status for VRF "VRF1"
    Neighbor        Interface            Uptime    Expires   DR       Bidir-  BFD
                                                             Priority Capable State

    PIM Neighbor Status for VRF "default"
    Neighbor        Interface            Uptime    Expires   DR       Bidir-  BFD
                                                         Priority Capable State
        '''}

    golden_parsed_output_neighbor_3 = {
        'vrf': {
            'VRF1':
                {
                    'interfaces': {
                        'Ethernet2/2': {
                            'address_family': {
                                'ipv4': {
                                    'neighbors': {
                                        '10.11.33.33': {
                                            'bfd_status': False,
                                            'expiration': '00:01:25',
                                            'dr_priority': 1,
                                            'up_time': '07:31:30',
                                            'interface': 'Ethernet2/2',
                                            'bidir_capable': True,

                                        },
                                    },
                                },
                            },

                        },
                    },
                },
        },
    }

    golden_output_neighbor_3 = {'execute.return_value': '''
        R1# show ip pim neighbor vrf VRF1
        PIM Neighbor Status for VRF "VRF1"
        Neighbor        Interface            Uptime    Expires   DR       Bidir-  BFD
                                                                 Priority Capable State
        10.11.33.33     Ethernet2/2          07:31:30  00:01:25  1        yes     n/a

        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpPimNeighbor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_ip_pim_neighbor_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_neighbor_1)
        obj = ShowIpPimNeighbor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_neighbor_1)

    def test_golden_ip_pim_neighbor_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_neighbor_2)
        obj = ShowIpPimNeighbor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_ip_pim_neighbor_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_neighbor_3)
        obj = ShowIpPimNeighbor(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_neighbor_3)


# ============================================
# Parser for 'show ip pim vrf all detail'
# ============================================

class test_show_ip_pim_vrf_detail(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_vrf_detail_1 = {
        'vrf':{
            'default':
                {
                'address_family':
                    {'ipv4':
                        {
                        'sm':{
                            'asm':{
                                'register_source': 'loopback0',
                                'register_source_address': '10.4.1.1',
                                'sg_expiry_timer': {
                                    'sg_list': 'sg-expiry-timer-sg-list',
                                    'infinity': True,
                                    'sg_expiry_timer_configured': True,
                                    'config_version': 1,
                                    'active_version': 1,
                                },
                            },
                        },
                        'vrf_id': 1,
                        'table_id': '0x00000001',
                        'interface_count': 3,
                        'bfd': {
                            'enable': False,
                        },
                        'mvpn': {
                            'enable': False,
                        },
                        'pre_build_spt': 'disabled',
                        'cli_vrf_done': True,
                        'cibtype_auto_enabled': True,
                        'vxlan_vni_id': 0,
                        },
                    },
                },
            'VRF1':
                {
                'address_family':
                    {'ipv4':
                        {
                        'sm': {
                            'asm': {
                                'register_source': 'loopback1',
                                'register_source_address': '10.229.11.11',
                                'sg_expiry_timer': {
                                    'sg_expiry_timer': 1200,
                                    'sg_expiry_timer_configured': True,
                                    'config_version': 1,
                                    'active_version': 1,
                                },
                            },
                        },
                        'vrf_id': 3,
                        'table_id': '0x00000003',
                        'interface_count': 3,
                        'bfd': {
                            'enable': False,
                        },
                        'mvpn': {
                            'enable': False,
                        },

                        'pre_build_spt': 'disabled',
                        'cli_vrf_done': True,
                        'cibtype_auto_enabled': True,
                        'vxlan_vni_id': 0,
                    },
                },
            },
        },
    }
    golden_output_vrf_detail_1 = {'execute.return_value': '''
        R1# show ip pim vrf all detail
        PIM Enabled VRFs
        VRF Name              VRF      Table       Interface  BFD        MVPN
                              ID       ID          Count      Enabled    Enabled
        default               1        0x00000001  3          no          no
          State Limit: None
          Register Rate Limit: none
          Register source  interface : loopback0 address : 10.4.1.1
          Shared tree ranges: none
          (S,G)-expiry timer: configured, infinity
            (S,G)-list policy: sg-expiry-timer-sg-list
            (S,G)-expiry timer config version 1, active version 1

          Pre-build SPT for all (S,G)s in VRF: disabled
          CLI vrf done: TRUE
          PIM cibtype Auto Enabled: yes
          PIM VxLAN VNI ID: 0
        VRF1                  3        0x00000003  3          no          no
          State Limit: None
          Register Rate Limit: none
          Register source  interface : loopback1 address : 10.229.11.11
          Shared tree ranges: none
          (S,G)-expiry timer: configured, 1200 secs
            (S,G)-list policy: none
            (S,G)-expiry timer config version 1, active version 1

          Pre-build SPT for all (S,G)s in VRF: disabled
          CLI vrf done: TRUE
          PIM cibtype Auto Enabled: yes
          PIM VxLAN VNI ID: 0
    '''}

    golden_output_vrf_detail_2 = {'execute.return_value': '''
            R1# show ip pim vrf all detail
            PIM Enabled VRFs
            %S DDDD
        '''}

    golden_parsed_output_vrf_detail_3 = {
    "vrf": {

        "VRF1": {
            "address_family": {
                "ipv4": {
                    "pre_build_spt": "disabled",
                    "vxlan_vni_id": 0,
                    "vrf_id": 3,
                    "mvpn": {
                        "enable": False
                    },
                    "sm": {
                        "asm": {
                            "sg_expiry_timer": {
                                "active_version": 0,
                                "config_version": 0
                            }
                        }
                    },
                    "interface_count": 1,
                    "bfd": {
                        "enable": False
                    },
                    "cli_vrf_done": True,
                    "table_id": "0x00000003",
                    "cibtype_auto_enabled": True
                }
            }
        },
        "VRF2": {
            "address_family": {
                "ipv4": {
                    "pre_build_spt": "disabled",
                    "vxlan_vni_id": 0,
                    "vrf_id": 4,
                    "mvpn": {
                        "enable": False
                    },
                    "sm": {
                        "asm": {
                            "sg_expiry_timer": {
                                "active_version": 0,
                                "config_version": 0
                            }
                        }
                    },
                    "interface_count": 1,
                    "bfd": {
                        "enable": False
                    },
                    "cli_vrf_done": True,
                    "table_id": "0x00000004",
                    "cibtype_auto_enabled": True
                }
            }
        },
        "default": {
            "address_family": {
                "ipv4": {
                    "pre_build_spt": "disabled",
                    "vxlan_vni_id": 0,
                    "vrf_id": 1,
                    "mvpn": {
                        "enable": False
                    },
                    "sm": {
                        "asm": {
                            "register_source": "Ethernet4/1",
                            "sg_expiry_timer": {
                                "active_version": 1,
                                "sg_expiry_timer": 1200,
                                "sg_expiry_timer_configured": True,
                                "config_version": 1
                            },
                            "register_source_address": "0.0.0.0"
                        }
                    },
                    "interface_count": 4,
                    "bfd": {
                        "enable": False
                    },
                    "cli_vrf_done": True,
                    "table_id": "0x00000001",
                    "cibtype_auto_enabled": True
                }
            }
        }
      }
    }

    golden_output_vrf_detail_3 ={'execute.return_value':'''
R1_nx# show ip pim vrf all detail
PIM Enabled VRFs
VRF Name              VRF      Table       Interface  BFD        MVPN
                      ID       ID          Count      Enabled    Enabled
default               1        0x00000001  4          no          no
  State Limit: None
  Register Rate Limit: none
  Register source  interface : Ethernet4/1 address : 0.0.0.0
  Shared tree ranges: none
  (S,G)-expiry timer: configured, 1200 secs
    (S,G)-list policy: none
    (S,G)-expiry timer config version 1, active version 1

  Pre-build SPT for all (S,G)s in VRF: disabled
  CLI vrf done: TRUE
  PIM cibtype Auto Enabled: yes
  PIM VxLAN VNI ID: 0
VRF1                  3        0x00000003  1          no          no
  State Limit: None
  Register Rate Limit: none
  Register source  interface : none
  Shared tree ranges: none
  (S,G)-expiry timer: not configured
    (S,G)-list policy: none
    (S,G)-expiry timer config version 0, active version 0

  Pre-build SPT for all (S,G)s in VRF: disabled
  CLI vrf done: TRUE
  PIM cibtype Auto Enabled: yes
  PIM VxLAN VNI ID: 0
VRF2                  4        0x00000004  1          no          no
  State Limit: None
  Register Rate Limit: none
  Register source  interface : none
  Shared tree ranges: none
  (S,G)-expiry timer: not configured
    (S,G)-list policy: none
    (S,G)-expiry timer config version 0, active version 0

  Pre-build SPT for all (S,G)s in VRF: disabled
  CLI vrf done: TRUE
  PIM cibtype Auto Enabled: yes
  PIM VxLAN VNI ID: 0
    '''}
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpPimVrfDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_detail_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_vrf_detail_1)
        obj = ShowIpPimVrfDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_vrf_detail_1)

    def test_golden_vrf_detail_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_vrf_detail_2)
        obj = ShowIpPimVrfDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_detail_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_vrf_detail_3)
        obj = ShowIpPimVrfDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_vrf_detail_3)

# ============================================
# Unit test for 'show ip pim group-range'
# ============================================
class test_show_ip_pim_group_range(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_group_range_1 = {
        'vrf':{
            'VRF1':
                {
                'address_family':{
                    'ipv4':{
                        'sm':{
                            'ssm':{
                               '232.0.0.0/8':{
                                   'action': 'accept',
                                   'mode': 'ssm',
                                   'range': 'local',
                                },
                            },
                            'asm':{
                                '224.0.0.0/4': {
                                    'mode': 'asm',
                                    'rp_address': '10.21.33.33',
                                },
                            },
                        },
                    },
                },
            },
            'default':{
                'address_family': {
                    'ipv4': {
                        'sm': {
                            'ssm': {
                                '232.0.0.0/8': {
                                    'action': 'accept',
                                    'mode': 'ssm',
                                    'range': 'local',
                                },
                            },
                            'asm':{
                                '224.0.0.0/4': {
                                    'mode': 'asm',
                                    'rp_address': '10.16.2.2',
                                },
                                '224.0.0.0/5': {
                                    'mode': 'asm',
                                    'rp_address': '10.1.5.1',
                                },
                            },
                        },
                    },
                },
            },
        },
    }
    golden_output_group_range_1 = {'execute.return_value': '''
    R1# show ip pim group-range vrf all
    PIM Group-Range Configuration for VRF "VRF1"
    Group-range        Action    Mode      RP-address       Shared-tree-only range
    232.0.0.0/8        Accept    SSM       -                -         Local
    224.0.0.0/4        -         ASM       10.21.33.33      -

    PIM Group-Range Configuration for VRF "default"
    Group-range        Action    Mode      RP-address       Shared-tree-only range
    232.0.0.0/8        Accept    SSM       -                -         Local
    224.0.0.0/4        -         ASM       10.16.2.2          -
    224.0.0.0/5        -         ASM       10.1.5.1         -
    '''}


    golden_output_group_range_2 = {'execute.return_value': '''
    R1_nx# show ip pim group-range vrf VRF3
    PIM VRF "VRF3" does not exist
    R1_nx# E
    '''}
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpPimGroupRange(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_ip_pim_group_range_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_group_range_1)
        obj = ShowIpPimGroupRange(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_group_range_1)

    def test_golden_ip_pim_group_range_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_group_range_2)
        obj = ShowIpPimGroupRange(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()



# ===============================================================
# unittest  for 'show ip pim policy statictics register-policy vrf all '
# ================================================================
class test_show_ip_pim_statictics_registery_policy(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_statictics_1 = {
        'vrf': {
            'VRF1':
                {
                'address_family':
                    {'ipv4':{
                        'sm': {
                            'asm': {
                                'accept_register': 'pim_register_vrf',
                                'register_policy': {
                                    'pim_register_vrf': {
                                        'match ip multicast group 239.2.2.2/32': {
                                            'compare_count': 0,
                                            'match_count': 0,
                                            },
                                        'total_accept_count': 0,
                                        'total_reject_count': 0,
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            'default':
                {
                'address_family':
                    {'ipv4':
                        {
                        'sm':{
                            'asm':{
                                'accept_register': 'pim_register_p',
                                'register_policy':{
                                    'pim_register_p':{
                                            'ip prefix-list pim_register_p seq 5 permit 239.3.3.3/32':{
                                                  'match_count':0,
                                            },
                                            'total_accept_count':0,
                                            'total_reject_count':0,
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            }

    golden_output_statictics_1 = {'execute.return_value': '''
        R1_nx# sh run | egrep '^vrf|register-policy'
        ip pim register-policy pim_register_p
        ipv6 pim register-policy testv6
        vrf context VRF1
          ip pim register-policy pim_register_vrf
        vrf context VRF2
        vrf context management

        R1_nx# show ip pim policy statistics register-policy vrf all
        C: No. of comparisions, M: No. of matches

        route-map pim_register_vrf permit 10
          match ip multicast group 239.2.2.2/32                      C: 0      M: 0

        Total accept count for policy: 0
        Total reject count for policy: 0


        C: No. of comparisions, M: No. of matches

        ip prefix-list pim_register_p seq 5 permit 239.3.3.3/32      M: 0

        Total accept count for policy: 0
        Total reject count for policy: 0

        '''}



    golden_output_statictics_1 = {'execute.return_value': '''
            R1_nx# sh run | egrep '^vrf|register-policy'
            ip pim register-policy pim_register_p
            ipv6 pim register-policy testv6
            vrf context VRF1
              ip pim register-policy pim_register_vrf
            vrf context VRF2
            vrf context management

            R1_nx# show ip pim policy statistics register-policy vrf all
            C: No. of comparisions, M: No. of matches

            route-map pim_register_vrf permit 10
              match ip multicast group 239.2.2.2/32                      C: 0      M: 0

            Total accept count for policy: 0
            Total reject count for policy: 0


            C: No. of comparisions, M: No. of matches

            ip prefix-list pim_register_p seq 5 permit 239.3.3.3/32      M: 0

            Total accept count for policy: 0
            Total reject count for policy: 0

            '''}
    golden_parsed_output_statictics_2 = {
        'vrf': {
            'VRF1':
                {
                    'address_family':
                        {'ipv4': {
                            'sm': {
                                'asm': {
                                    'accept_register': 'pim_register_vrf',
                                    'register_policy': {
                                        'pim_register_vrf': {
                                            'match ip multicast group 239.2.2.2/32': {
                                                'compare_count': 0,
                                                'match_count': 0,
                                            },
                                            'total_accept_count': 0,
                                            'total_reject_count': 0,
                                        },
                                    },
                                },
                            },
                        },
                        },
                },
        },
    }
    golden_output_statictics_2 = {'execute.return_value': '''
            R1_nx# sh run | egrep '^vrf|register-policy'
            ip pim register-policy pim_register_p
            ipv6 pim register-policy testv6
            vrf context VRF1
              ip pim register-policy pim_register_vrf
            vrf context VRF2
            vrf context management

            R1_nx# show ip pim policy statistics register-policy vrf VRF1
            C: No. of comparisions, M: No. of matches

            route-map pim_register_vrf permit 10
              match ip multicast group 239.2.2.2/32                      C: 0      M: 0

            Total accept count for policy: 0
            Total reject count for policy: 0

            '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpPimPolicyStaticticsRegisterPolicy(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_statistics_register_policy_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_statictics_1)
        obj = ShowIpPimPolicyStaticticsRegisterPolicy(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_statictics_1)

    def test_golden_statistics_register_policy_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_statictics_2)
        obj = ShowIpPimPolicyStaticticsRegisterPolicy(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_statictics_2)


# ============================================
# Parser for 'show ip pim rp'
# Parser for 'show ip pim rp vrf <word>'
# ============================================
class test_show_ip_pim_rp(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_rp_1 = {
        "vrf": {
            "default": {
                 "address_family": {
                      "ipv4": {
                           "rp": {
                                "autorp": {
                                     "address": "10.1.5.1",
                                     "bsr_next_discovery": "00:00:42"
                                },
                                "static_rp": {
                                     "10.111.111.111": {
                                          "sm": {
                                               "policy_name": "224.0.0.0/4"
                                          }
                                     },
                                     "10.16.2.2": {
                                          "sm": {
                                               "policy_name": "224.0.0.0/4"
                                          }
                                     },
                                     "10.66.12.12": {
                                          "bidir": {
                                               "policy_name": "233.0.0.0/24"
                                          }
                                     }
                                },
                                "rp_list": {
                                     "10.111.111.111 SM static": {
                                          "mode": "SM",
                                          "group_ranges": "224.0.0.0/4",
                                          "df_ordinal": 0,
                                          "expiration": "never",
                                          "up_time": "00:01:06",
                                          "address": "10.111.111.111",
                                          "info_source_type": "static"
                                     },
                                     "10.16.2.2 SM static": {
                                          "mode": "SM",
                                          "group_ranges": "224.0.0.0/4",
                                          "df_ordinal": 0,
                                          "expiration": "never",
                                          "up_time": "03:52:52",
                                          "address": "10.16.2.2",
                                          "info_source_type": "static"
                                     },
                                     "10.66.12.12 BIDIR static": {
                                          "mode": "BIDIR",
                                          "group_ranges": "233.0.0.0/24",
                                          "df_ordinal": 1,
                                          "expiration": "never",
                                          "up_time": "00:00:54",
                                          "address": "10.66.12.12",
                                          "info_source_type": "static"
                                     },
                                     "10.1.5.1 SM bootstrap": {
                                          "mode": "SM",
                                          "group_ranges": "224.0.0.0/5",
                                          "df_ordinal": 0,
                                          "expiration": "00:02:05",
                                          "up_time": "01:56:07",
                                          "priority": 92,
                                          "address": "10.1.5.1",
                                          "info_source_address": "10.1.5.1",
                                          "info_source_type": "bootstrap"
                                     }
                                },
                                "rp_mappings": {
                                     "224.0.0.0/4 10.16.2.2 static": {
                                          "group": "224.0.0.0/4",
                                          "protocol": "static",
                                          "rp_address": "10.16.2.2",
                                          "up_time": "03:52:52",
                                          "expiration": "never"
                                     },
                                     "224.0.0.0/4 10.111.111.111 static": {
                                          "group": "224.0.0.0/4",
                                          "protocol": "static",
                                          "rp_address": "10.111.111.111",
                                          "up_time": "00:01:06",
                                          "expiration": "never"
                                     },
                                     "224.0.0.0/5 10.1.5.1 bootstrap": {
                                          "group": "224.0.0.0/5",
                                          "protocol": "bootstrap",
                                          "rp_address": "10.1.5.1",
                                          "up_time": "01:56:07",
                                          "expiration": "00:02:05"
                                     },
                                     "233.0.0.0/24 10.66.12.12 static": {
                                          "group": "233.0.0.0/24",
                                          "protocol": "static",
                                          "rp_address": "10.66.12.12",
                                          "up_time": "00:00:54",
                                          "expiration": "never"
                                     }
                                },
                                "bsr": {
                                     "bsr_candidate": {
                                          "hash_mask_length": 30,
                                          "priority": 111,
                                          "address": "10.1.5.1"
                                     },
                                     "rp": {
                                          "up_time": "01:56:07",
                                          "rp_address": "10.1.5.1",
                                          "group_policy": "224.0.0.0/5"
                                     },
                                     "bsr_next_bootstrap": "00:00:01",
                                     'rp_candidate_next_advertisement': '00:02:05',
                                     "bsr_address": {
                                          "10.1.5.1": {
                                               "mode": "SM",
                                               "priority": 92,
                                               "address": "10.1.5.1",
                                               "policy": "224.0.0.0/5"
                                          }
                                     },
                                     "bsr": {
                                          "hash_mask_length": 30,
                                          "priority": 111,
                                          "address": "10.1.5.1"
                                     }
                                }
                           },
                           "sm": {
                                "asm": {
                                     "anycast_rp": {
                                          "10.111.111.111 10.1.5.1": {
                                               "anycast_address": "10.111.111.111"
                                          },
                                          "10.111.111.111 10.1.2.1": {
                                               "anycast_address": "10.111.111.111"
                                          }
                                     }
                                }
                           }
                      }
                 }
            },
            "VRF1": {
                 "address_family": {
                      "ipv4": {
                           "rp": {
                                "autorp": {
                                     "send_rp_announce": {
                                          "rp_source": "192.168.64.2",
                                          "bidir": True,
                                          "scope": 0,
                                          "group_list": "226.0.0.0/8",
                                          "group": "226.0.0.0"
                                     },
                                     "address": "10.229.11.11",
                                     "bsr_next_discovery": "00:00:15"
                                },
                                "static_rp": {
                                     "10.21.33.33": {
                                          "sm": {
                                               "policy_name": "224.0.0.0/4"
                                          }
                                     }
                                },
                                "rp_list": {
                                     "192.168.64.2 BIDIR autorp": {
                                          "mode": "BIDIR",
                                          "group_ranges": "226.0.0.0/8",
                                          "df_ordinal": 0,
                                          "expiration": "00:02:24",
                                          "up_time": "04:30:45",
                                          "priority": 255,
                                          "address": "192.168.64.2",
                                          "info_source_address": "192.168.64.2",
                                          "info_source_type": "autorp"
                                     },
                                     "10.21.33.33 SM static": {
                                          "mode": "SM",
                                          "group_ranges": "224.0.0.0/4",
                                          "df_ordinal": 0,
                                          "expiration": "never",
                                          "up_time": "03:52:52",
                                          "address": "10.21.33.33",
                                          "info_source_type": "static"
                                     }
                                },
                                "rp_mappings": {
                                     "224.0.0.0/4 10.21.33.33 static": {
                                          "group": "224.0.0.0/4",
                                          "protocol": "static",
                                          "rp_address": "10.21.33.33",
                                          "up_time": "03:52:52",
                                          "expiration": "never"
                                     },
                                     "226.0.0.0/8 192.168.64.2 autorp": {
                                          "group": "226.0.0.0/8",
                                          "protocol": "autorp",
                                          "rp_address": "192.168.64.2",
                                          "up_time": "04:30:45",
                                          "expiration": "00:02:24"
                                     }
                                }
                           }
                      }
                 }
            }
       }

    }
    golden_output_rp_1 = {'execute.return_value': '''
        R1# show ip pim rp vrf all
        PIM RP Status Information for VRF "VRF1"
        BSR: Not Operational
        Auto-RP RPA: 10.229.11.11*, next Discovery message in: 00:00:15
        BSR RP Candidate policy: None
        BSR RP policy: None
        Auto-RP Announce policy: None
        Auto-RP Discovery policy: None

        RP: 10.21.33.33, (0), 
          uptime: 03:52:52  priority: 0,
          RP-source: (local),
          group ranges:
              224.0.0.0/4, expires: never
        RP: 192.168.64.2, (0), 
          uptime: 04:30:45   priority: 255, 
          RP-source: 192.168.64.2 (A),
          group ranges:
            226.0.0.0/8   (bidir)  ,  expires: 00:02:24 (A)

        PIM RP Status Information for VRF "VRF2"
        BSR disabled
        Auto-RP disabled
        BSR RP Candidate policy: None
        BSR RP policy: None
        Auto-RP Announce policy: None
        Auto-RP Discovery policy: None

        PIM RP Status Information for VRF "default"
        BSR: 10.1.5.1*, next Bootstrap message in: 00:00:01,
             priority: 111, hash-length: 30
        Auto-RP RPA: 10.1.5.1*, next Discovery message in: 00:00:42
        BSR RP Candidate policy: None
        BSR RP policy: None
        Auto-RP Announce policy: None
        Auto-RP Discovery policy: None

        Anycast-RP 10.111.111.111 members:
          10.1.2.1*  10.1.5.1*

        RP: 10.16.2.2, (0), uptime: 03:52:52, expires: never,
          priority: 0, RP-source: (local), group ranges:
              224.0.0.0/4
        RP: 10.1.5.1*, (0), uptime: 01:56:07, expires: 00:02:05,
          priority: 92, RP-source: 10.1.5.1 (B), group ranges:
              224.0.0.0/5
        RP: 10.66.12.12, (1), uptime: 00:00:54, expires: never,
          priority: 0, RP-source: (local), group ranges:
              233.0.0.0/24  (bidir)
        RP: 10.111.111.111, (0), uptime: 00:01:06, expires: never,
          priority: 0, RP-source: (local), group ranges:
              224.0.0.0/4
    '''}


    golden_output_rp_2 = {'execute.return_value': '''
        R2_nx# show ip pim rp vrf all
        PIM RP Status Information for VRF "default"
        BSR: Not Operational
        Auto-RP disabled
        BSR RP Candidate policy: None
        BSR RP policy: None
        Auto-RP Announce policy: None
        Auto-RP Discovery policy: None

        '''}


    golden_output_rp_3 = {'execute.return_value': '''
        R1_nx# show ip pim rp vrf all
        PIM RP Status Information for VRF "VRF1"
        BSR: 10.1.5.5, uptime: 18:04:20, expires: 00:01:50,
             priority: 0, hash-length: 0
        Auto-RP disabled
        BSR RP Candidate policy: None
        BSR RP policy: None
        Auto-RP Announce policy: None
        Auto-RP Discovery policy: None

        RP: 10.1.5.1*, (0), uptime: 18:04:19, expires: 00:02:10,
          priority: 5, RP-source: 10.1.5.5 (B), group ranges:
              239.0.0.0/24
        RP: 10.1.5.5, (0), uptime: 18:07:42, expires: never,
          priority: 0, RP-source: (local), group ranges:
              224.0.0.0/4

        PIM RP Status Information for VRF "VRF2"
        BSR disabled
        Auto-RP disabled
        BSR RP Candidate policy: None
        BSR RP policy: None
        Auto-RP Announce policy: None
        Auto-RP Discovery policy: None


        PIM RP Status Information for VRF "default"
        BSR: 10.4.1.1*, next Bootstrap message in: 00:00:42,
             priority: 64, hash-length: 30
        Auto-RP disabled
        BSR RP Candidate policy: None
        BSR RP policy: None
        Auto-RP Announce policy: None
        Auto-RP Discovery policy: None

        RP: 10.16.2.2, (0), uptime: 18:05:36, expires: 00:02:18,
          priority: 10, RP-source: 10.16.2.2 (B), group ranges:
              239.0.0.0/24
        RP: 10.36.3.3, (0), uptime: 18:07:42, expires: 00:01:50 (B),
          priority: 5, RP-source: 10.36.3.3 (B), (local), group ranges:
              239.0.0.0/24   224.0.0.0/4
    '''

}

    golden_parsed_output_rp_3 = {
        "vrf": {
            "default": {
                 "address_family": {
                      "ipv4": {
                           "rp": {
                                "bsr": {
                                     "bsr": {
                                          "hash_mask_length": 30,
                                          "priority": 64,
                                          "address": "10.4.1.1"
                                     },
                                     "bsr_next_bootstrap": "00:00:42",
                                     'rp_candidate_next_advertisement': '00:02:18',
                                     "bsr_address": {
                                          "10.16.2.2": {
                                               "priority": 10,
                                               "address": "10.16.2.2",
                                               "mode": "SM",
                                               "policy": "239.0.0.0/24"
                                          }
                                     },
                                     "rp": {
                                          "group_policy": "239.0.0.0/24",
                                          "up_time": "18:05:36",
                                          "rp_address": "10.16.2.2"
                                     },
                                     "bsr_candidate": {
                                          "hash_mask_length": 30,
                                          "priority": 64,
                                          "address": "10.4.1.1"
                                     }
                                },
                                "rp_mappings": {
                                     "239.0.0.0/24 10.16.2.2 bootstrap": {
                                          "protocol": "bootstrap",
                                          "expiration": "00:02:18",
                                          "group": "239.0.0.0/24",
                                          "up_time": "18:05:36",
                                          "rp_address": "10.16.2.2"
                                     }
                                },
                                "rp_list": {
                                     "10.16.2.2 SM bootstrap": {
                                          "info_source_address": "10.16.2.2",
                                          "priority": 10,
                                          "address": "10.16.2.2",
                                          "mode": "SM",
                                          "group_ranges": "239.0.0.0/24",
                                          "df_ordinal": 0,
                                          "expiration": "00:02:18",
                                          "up_time": "18:05:36",
                                          "info_source_type": "bootstrap"
                                     }
                                }
                           }
                      }
                 }
            },
            "VRF1": {
                 "address_family": {
                      "ipv4": {
                           "rp": {
                                "bsr": {
                                     "bsr": {
                                          "hash_mask_length": 0,
                                          "priority": 0,
                                          "address": "10.1.5.5",
                                          "up_time": "18:04:20",
                                          "expires": "00:01:50"
                                     },
                                     "bsr_address": {
                                          "10.1.5.5": {
                                               "priority": 5,
                                               "address": "10.1.5.5",
                                               "mode": "SM",
                                               "policy": "239.0.0.0/24"
                                          }
                                     },
                                     "rp": {
                                          "group_policy": "239.0.0.0/24",
                                          "up_time": "18:04:19",
                                          "rp_address": "10.1.5.5"
                                     },
                                     "bsr_candidate": {
                                          "hash_mask_length": 0,
                                          "priority": 0,
                                          "address": "10.1.5.5"
                                     },
                                     'rp_candidate_next_advertisement': '00:02:10'
                                },
                                "rp_mappings": {
                                     "239.0.0.0/24 10.1.5.1 bootstrap": {
                                          "protocol": "bootstrap",
                                          "expiration": "00:02:10",
                                          "group": "239.0.0.0/24",
                                          "up_time": "18:04:19",
                                          "rp_address": "10.1.5.1"
                                     },
                                     "224.0.0.0/4 10.1.5.5 static": {
                                          "protocol": "static",
                                          "expiration": "never",
                                          "group": "224.0.0.0/4",
                                          "up_time": "18:07:42",
                                          "rp_address": "10.1.5.5"
                                     }
                                },
                                "rp_list": {
                                     "10.1.5.5 SM static": {
                                          "address": "10.1.5.5",
                                          "mode": "SM",
                                          "group_ranges": "224.0.0.0/4",
                                          "df_ordinal": 0,
                                          "expiration": "never",
                                          "up_time": "18:07:42",
                                          "info_source_type": "static"
                                     },
                                     "10.1.5.1 SM bootstrap": {
                                          "info_source_address": "10.1.5.5",
                                          "priority": 5,
                                          "address": "10.1.5.1",
                                          "mode": "SM",
                                          "group_ranges": "239.0.0.0/24",
                                          "df_ordinal": 0,
                                          "expiration": "00:02:10",
                                          "up_time": "18:04:19",
                                          "info_source_type": "bootstrap"
                                     }
                                },
                                "static_rp": {
                                     "10.1.5.5": {
                                          "sm": {
                                               "policy_name": "224.0.0.0/4"
                                          }
                                     }
                                }
                           }
                      }
                 }
            }
       }
    }


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpPimRp(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_ip_pim_rp_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_rp_1)
        obj = ShowIpPimRp(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output_rp_1)


    def test_golden_ip_pim_rp_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_rp_2)
        obj = ShowIpPimRp(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_ip_pim_rp_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_rp_3)
        obj = ShowIpPimRp(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output_rp_3)


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
                                'oper_status': 'up',
                                'link_status': 'up',
                                'admin_status': 'up',
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
                                'jp_interval': 60,
                                'jp_next_sending': 60,
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
                                'oper_status': 'up',
                                'link_status': 'up',
                                'admin_status': 'up',
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
                                'jp_interval': 60,
                                'jp_next_sending': 60,
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
                                'oper_status': 'up',
                                'link_status': 'up',
                                'admin_status': 'up',
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
                                'jp_interval': 60,
                                'jp_next_sending': 60,
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


# ============================================
# Parser for 'show running-config pim'
# Parser for 'show running-config pim6'
# ============================================
outputs = {}

def mapper(key):
    return outputs[key]

class test_show_running_config_pim_pim6(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    parsed_output = {
        "feature_pim6": True,
        "vrf": {
             "VRF1": {
                  "address_family": {
                       "ipv4": {
                            "rp": {
                                 "bsr": {
                                      "loopback10": {
                                           "interface": "loopback10",
                                           "route_map": "filtera"
                                      }
                                 },
                                 "autorp": {
                                      "send_rp_discovery": {
                                           "interface": "loopback11"
                                      },
                                      "send_rp_announce": {
                                           "group_list": "236.0.0.0/8",
                                           "interface": "loopback11"
                                      }
                                 }
                            }
                       }
                  }
             },
             "default": {
                  "address_family": {
                       "ipv4": {
                            "rp": {
                                 "bsr": {
                                      "Ethernet1/1": {
                                           "interface": "Ethernet1/1",
                                           "priority": 10,
                                           "policy": "239.0.0.0/24",
                                           "interval": 60,
                                           "mode": "bidir"
                                      }
                                 },
                                 "autorp": {
                                      "send_rp_discovery": {
                                           "interface": "loopback0"
                                      },
                                      "send_rp_announce": {
                                           "group_list": "236.0.0.0/8",
                                           "interface": "loopback0"
                                      }
                                 }
                            }
                       }
                  }
             }
        },
        "feature_pim": True
    }

    parsed_output_v4 = {
        "vrf": {
             "VRF1": {
                  "address_family": {
                       "ipv4": {
                            "rp": {
                                 "bsr": {
                                      "loopback10": {
                                           "interface": "loopback10",
                                           "route_map": "filtera"
                                      }
                                 },
                                 "autorp": {
                                      "send_rp_discovery": {
                                           "interface": "loopback11"
                                      },
                                      "send_rp_announce": {
                                           "group_list": "236.0.0.0/8",
                                           "interface": "loopback11"
                                      }
                                 }
                            }
                       }
                  }
             },
             "default": {
                  "address_family": {
                       "ipv4": {
                            "rp": {
                                 "bsr": {
                                      "Ethernet1/1": {
                                           "interface": "Ethernet1/1",
                                           "priority": 10,
                                           "policy": "239.0.0.0/24",
                                           "interval": 60,
                                           "mode": "bidir"
                                      }
                                 },
                                 "autorp": {
                                      "send_rp_discovery": {
                                           "interface": "loopback0"
                                      },
                                      "send_rp_announce": {
                                           "group_list": "236.0.0.0/8",
                                           "interface": "loopback0"
                                      }
                                 }
                            }
                       }
                  }
             }
        },
        "feature_pim": True
    }
    parsed_output_v6 = {
        'feature_pim6': True, 'vrf': {'VRF1': {}, 'default': {}}
    }
    parsed_output_default_attr = {
        'vrf': {'default': {'address_family': {'ipv4': {'rp': {'autorp': {'send_rp_announce': {'group_list': '236.0.0.0/8',
                                                                                              'interface': 'loopback0'}}}}}}}
    }
    parsed_output_non_default_attr = {
        'vrf': {'VRF1': {'address_family': {'ipv4': {'rp': {'autorp': {'send_rp_announce': {'group_list': '236.0.0.0/8',
                                                                                              'interface': 'loopback11'}}}}}}}
    }

    golden_output_v4 = {'execute.return_value': '''
        N95_2_R2# show run pim

!Command: show running-config pim
!Time: Wed Aug 15 15:47:22 2018

version 7.0(3)I7(3)
feature pim

ip pim send-rp-announce loopback0 group-list 236.0.0.0/8
ip pim send-rp-discovery loopback0
ip pim rp-candidate Ethernet1/1 group-list 239.0.0.0/24 priority 10 interval 60 bidir

vrf context VRF1
  ip pim send-rp-announce loopback11 group-list 236.0.0.0/8
  ip pim send-rp-discovery loopback11
  ip pim rp-candidate loopback10 route-map filtera
    '''}

    golden_output_v6 = {'execute.return_value': '''
        N95_2_R2# show run pim6

!Command: show running-config pim6
!Time: Tue Aug 14 18:32:21 2018

version 7.0(3)I7(3)
feature pim6

ipv6 pim rp-address 2001:6:6:6::6 group-list fff0::/12
ipv6 pim ssm range ff30::/12

vrf context VRF1
  ipv6 pim rp-address 2001:6:6:6::6 group-list fff0::/12
  ipv6 pim ssm range ff30::/12
    '''}

    golden_output_default_attr = {'execute.return_value': '''
        N95_2_R2# show run pim | section '^i' | inc send-rp-announce
ip pim send-rp-announce loopback0 group-list 236.0.0.0/8
    '''}

    golden_output_non_default_attr = {'execute.return_value': '''
        N95_2_R2# show running-config pim | sec VRF1 | inc send-rp-announce
  ip pim send-rp-announce loopback11 group-list 236.0.0.0/8
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6PimVrfAllDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

        
    def test_golden_all(self):
        self.maxDiff = None
        # Mock device output
        outputs['show running-config pim'] = self.golden_output_v4['execute.return_value']
        outputs['show running-config pim6'] = self.golden_output_v6['execute.return_value']
        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        obj = ShowRunningConfigPim(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output)

    def test_golden_pim(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_v4)
        obj = ShowRunningConfigPim(device=self.device)
        parsed_output = obj.parse(address_family='ipv4')
        self.assertEqual(parsed_output, self.parsed_output_v4)

    def test_golden_pim6(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_v6)
        obj = ShowRunningConfigPim(device=self.device)
        parsed_output = obj.parse(address_family='ipv6')
        self.assertEqual(parsed_output, self.parsed_output_v6)

    def test_golden_vrf_default_attr(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_default_attr)
        obj = ShowRunningConfigPim(device=self.device)
        parsed_output = obj.parse(address_family='ipv4', vrf='default', pip_str='send-rp-announce')
        self.assertEqual(parsed_output, self.parsed_output_default_attr)

    def test_golden_vrf_non_default_attr(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_non_default_attr)
        obj = ShowRunningConfigPim(device=self.device)
        parsed_output = obj.parse(address_family='ipv4', vrf='VRF1', pip_str='send-rp-announce')
        self.assertEqual(parsed_output, self.parsed_output_non_default_attr)

if __name__ == '__main__':
    unittest.main()