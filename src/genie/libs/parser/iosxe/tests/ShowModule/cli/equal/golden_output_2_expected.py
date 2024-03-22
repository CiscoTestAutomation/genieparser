expected_output = {
  'switches': {
    1: {
      'module': {
        1: {
          'ports': 38,
          'card_type': 'Cisco Catalyst 9500X-28C8D Switch',
          'model': 'C9500X-28C8D',
          'serial': 'FDO24460AE5',
          'mac_address': '40B5.C1FF.EE00 to 40B5.C1FF.EE25',
          'hw': '0.2',
          'fw': '17.9.1r',
          'sw': 'BLD_POLARIS_DEV_LA',
          'status': 'ok',
          'redundancy_role': 'active',
          'operating_redundancy_mode': 'sso',
          'configured_redundancy_mode': 'sso'
        }
      }
    },
    2: {
      'module': {
        1: {
          'ports': 38,
          'card_type': 'Cisco Catalyst 9500X-28C8D Switch',
          'model': 'C9500X-28C8D',
          'serial': 'FDO25130VEC',
          'mac_address': 'F87A.4137.BE00 to F87A.4137.BE25',
          'hw': '0.2',
          'fw': '17.9.1r',
          'sw': 'BLD_POLARIS_DEV_LA',
          'status': 'ok',
          'redundancy_role': 'standby',
          'operating_redundancy_mode': 'sso',
          'configured_redundancy_mode': 'sso'
        }
      }
    }
  },
  'chassis': {
    1: {
      'number_of_mac_address': 512,
      'chassis_mac_address_lower_range': '40b5.c1ff.ee00',
      'chassis_mac_address_upper_range': '40b5.c1ff.efff'
    },
    2: {
      'number_of_mac_address': 512,
      'chassis_mac_address_lower_range': 'f87a.4137.be00',
      'chassis_mac_address_upper_range': 'f87a.4137.bfff'
    }
  }
}
