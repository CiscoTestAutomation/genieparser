expected_output = {
  'link': {
    1: {
      'protocol': 'ISIS L1',
      'identifier': '0x0',
      'local_node_descriptor': {
        'as_number': 50,
        'bgp_identifier': '0.0.0.0',
        'iso_node_id': '1111.1111.1111'
      },
      'remote_node_descriptor': {
        'as_number': 50,
        'bgp_identifier': '0.0.0.0',
        'iso_node_id': '2222.2222.2222.01'
      },
      'link_descriptor': {},
      'internal_flag': '0x0',
      'action': 'Update',
      'merged_link_attr': {
        'metric': 28
      }
    },
    2: {
      'protocol': 'ISIS L1',
      'identifier': '0x0',
      'local_node_descriptor': {
        'as_number': 50,
        'bgp_identifier': '0.0.0.0',
        'iso_node_id': '2222.2222.2222'
      },
      'remote_node_descriptor': {
        'as_number': 50,
        'bgp_identifier': '0.0.0.0',
        'iso_node_id': '2222.2222.2222.01'
      },
      'link_descriptor': {},
      'internal_flag': '0x0',
      'action': 'Update',
      'merged_link_attr': {
        'metric': 10
      }
    },
    3: {
      'protocol': 'ISIS L1',
      'identifier': '0x0',
      'local_node_descriptor': {
        'as_number': 50,
        'bgp_identifier': '0.0.0.0',
        'iso_node_id': '2222.2222.2222.01'
      },
      'remote_node_descriptor': {
        'as_number': 50,
        'bgp_identifier': '0.0.0.0',
        'iso_node_id': '1111.1111.1111'
      },
      'link_descriptor': {},
      'internal_flag': '0x0',
      'action': 'Update',
      'merged_link_attr': {
        'metric': 0
      }
    },
    4: {
      'protocol': 'ISIS L1',
      'identifier': '0x0',
      'local_node_descriptor': {
        'as_number': 50,
        'bgp_identifier': '0.0.0.0',
        'iso_node_id': '2222.2222.2222.01'
      },
      'remote_node_descriptor': {
        'as_number': 50,
        'bgp_identifier': '0.0.0.0',
        'iso_node_id': '2222.2222.2222'
      },
      'link_descriptor': {},
      'internal_flag': '0x0',
      'action': 'Update',
      'merged_link_attr': {
        'metric': 0
      }
    }
  }
}
