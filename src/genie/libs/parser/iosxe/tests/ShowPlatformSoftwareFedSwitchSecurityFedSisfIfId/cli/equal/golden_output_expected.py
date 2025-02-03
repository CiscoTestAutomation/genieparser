expected_output={
  'fed_sisf_port_data': {
    'interface': {
      'interface_id': {
        1035: {
          'interface_name': 'GigabitEthernet1/0/4',
          'interface_oid': 1090,
          'target_port': 'TRUE',
          'sisf_enable': 'TRUE',
          'interface_local': 'TRUE',
          'asic_local': '0x1',
          'etherchannel_member': 'FALSE',
          'interface_active': 'TRUE',
          'internal_error': 'None',
          'low_level_error': 'None',
          'etherchannel': 'FALSE',
          'etherchannel_id': 0,
          'reference_count': 0,
          'num_oids_programmed': 1,
          'num_oids_on_asic': '0x1',
          'no_acl_diagnostic': 0,
          'invalid_acl_diagnostic': 0,
          'redundant_active_diagnostic': 0,
          'redundant_deactivate_diagnostic': 0,
          'asic_specific': {
            'acl_info': {
              'oid': 557,
              'on_asic': 0,
              'positions': {
                0: {
                  'protocol': 'UDP',
                  'src_port': 547,
                  'dst_port': 0,
                  'action': 'PUNT',
                  'counter_oid': 558
                },
                1: {
                  'protocol': 'UDP',
                  'src_port': 0,
                  'dst_port': 547,
                  'action': 'PUNT',
                  'counter_oid': 559
                },
                2: {
                  'protocol': 'UDP',
                  'src_port': 0,
                  'dst_port': 546,
                  'action': 'PUNT',
                  'counter_oid': 560
                },
                3: {
                  'protocol': 'ICMPv6',
                  'message_type': 'Neighbor Solicitation',
                  'code': 0,
                  'action': 'PUNT',
                  'counter_oid': 561
                },
                4: {
                  'protocol': 'ICMPv6',
                  'message_type': 'Neighbor Advertisement',
                  'code': 0,
                  'action': 'PUNT',
                  'counter_oid': 562
                },
                5: {
                  'protocol': 'ICMPv6',
                  'message_type': 'Router Solicitation',
                  'code': 0,
                  'action': 'PUNT',
                  'counter_oid': 563
                },
                6: {
                  'protocol': 'ICMPv6',
                  'message_type': 'Router Advertisement',
                  'code': 0,
                  'action': 'PUNT',
                  'counter_oid': 564
                },
                7: {
                  'protocol': 'ICMPv6',
                  'message_type': 'Redirect Message',
                  'code': 0,
                  'action': 'PUNT',
                  'counter_oid': 565
                },
                8: {
                  'protocol': 'ICMPv6',
                  'message_type': 'Duplicate Address Request',
                  'code': 0,
                  'action': 'PUNT',
                  'counter_oid': 566
                },
                9: {
                  'protocol': 'ICMPv6',
                  'message_type': 'Duplicate Address Confirmation',
                  'code': 0,
                  'action': 'PUNT',
                  'counter_oid': 567
                }
              }
            }
          }
        },
        1044: {
          'interface_name': 'GigabitEthernet1/0/13',
          'interface_oid': 0,
          'target_port': 'TRUE',
          'sisf_enable': 'FALSE',
          'interface_local': 'TRUE',
          'asic_local': '0x1',
          'etherchannel_member': 'TRUE',
          'programmed_status': 'Not programmed',
          'interface_active': 'TRUE',
          'internal_error': 'None',
          'low_level_error': 'None',
          'etherchannel': 'FALSE',
          'etherchannel_id': 1169,
          'reference_count': 0,
          'num_oids_programmed': 0,
          'num_oids_on_asic': '0x0',
          'no_acl_diagnostic': 0,
          'invalid_acl_diagnostic': 0,
          'redundant_active_diagnostic': 0,
          'redundant_deactivate_diagnostic': 0
        },
        1169: {
          'interface_name': 'Port-channel128',
          'interface_oid': 2090,
          'target_port': 'TRUE',
          'sisf_enable': 'TRUE',
          'interface_local': 'TRUE',
          'asic_local': '0x1',
          'etherchannel_member': 'FALSE',
          'interface_active': 'TRUE',
          'internal_error': 'None',
          'low_level_error': 'None',
          'etherchannel': 'TRUE',
          'etherchannel_id': 0,
          'reference_count': 1,
          'num_oids_programmed': 1,
          'num_oids_on_asic': '0x1',
          'no_acl_diagnostic': 0,
          'invalid_acl_diagnostic': 0,
          'redundant_active_diagnostic': 0,
          'redundant_deactivate_diagnostic': 0,
          'asic_specific': {
            'acl_info': {
              'oid': 557,
              'on_asic': 0,
              'positions': {
                0: {
                  'protocol': 'UDP',
                  'src_port': 547,
                  'dst_port': 0,
                  'action': 'PUNT',
                  'counter_oid': 558
                },
                1: {
                  'protocol': 'UDP',
                  'src_port': 0,
                  'dst_port': 547,
                  'action': 'PUNT',
                  'counter_oid': 559
                },
                2: {
                  'protocol': 'UDP',
                  'src_port': 0,
                  'dst_port': 546,
                  'action': 'PUNT',
                  'counter_oid': 560
                },
                3: {
                  'protocol': 'ICMPv6',
                  'message_type': 'Neighbor Solicitation',
                  'code': 0,
                  'action': 'PUNT',
                  'counter_oid': 561
                },
                4: {
                  'protocol': 'ICMPv6',
                  'message_type': 'Neighbor Advertisement',
                  'code': 0,
                  'action': 'PUNT',
                  'counter_oid': 562
                },
                5: {
                  'protocol': 'ICMPv6',
                  'message_type': 'Router Solicitation',
                  'code': 0,
                  'action': 'PUNT',
                  'counter_oid': 563
                },
                6: {
                  'protocol': 'ICMPv6',
                  'message_type': 'Router Advertisement',
                  'code': 0,
                  'action': 'PUNT',
                  'counter_oid': 564
                },
                7: {
                  'protocol': 'ICMPv6',
                  'message_type': 'Redirect Message',
                  'code': 0,
                  'action': 'PUNT',
                  'counter_oid': 565
                },
                8: {
                  'protocol': 'ICMPv6',
                  'message_type': 'Duplicate Address Request',
                  'code': 0,
                  'action': 'PUNT',
                  'counter_oid': 566
                },
                9: {
                  'protocol': 'ICMPv6',
                  'message_type': 'Duplicate Address Confirmation',
                  'code': 0,
                  'action': 'PUNT',
                  'counter_oid': 567
                }
              }
            }
          }
        }
      }
    }
  }
}
