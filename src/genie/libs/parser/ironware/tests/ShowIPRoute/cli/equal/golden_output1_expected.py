expected_output = {
  'total_routes': 13,
  'routes': {
    '10.200.0.12/30': {
      'network': '10.200.0.12',
      'cidr': 30,
      'via': {
        '10.254.248.10': {
          'interface': 'eth 2/2',
          'cost': '110/28',
          'type': 'O',
          'uptime': '40d0h',
          'src-vrf': '-'
        }
      }
    },
    '10.200.0.16/30': {
      'network': '10.200.0.16',
      'cidr': 30,
      'via': {
        '10.254.248.10': {
          'interface': 'eth 2/2',
          'cost': '110/194',
          'type': 'O',
          'uptime': '6d12h',
          'src-vrf': '-'
        }
      }
    },
    '10.200.0.28/30': {
      'network': '10.200.0.28',
      'cidr': 30,
      'via': {
        '10.254.248.10': {
          'interface': 'eth 2/2',
          'cost': '110/138',
          'type': 'O',
          'uptime': '40d0h',
          'src-vrf': '-'
        }
      }
    },
    '10.200.0.32/30': {
      'network': '10.200.0.32',
      'cidr': 30,
      'via': {
        '10.254.248.10': {
          'interface': 'eth 2/2',
          'cost': '110/36',
          'type': 'O',
          'uptime': '40d0h',
          'src-vrf': '-'
        }
      }
    },
    '10.200.0.56/30': {
      'network': '10.200.0.56',
      'cidr': 30,
      'via': {
        '10.254.248.10': {
          'interface': 'eth 2/2',
          'cost': '110/36',
          'type': 'O',
          'uptime': '12d4h',
          'src-vrf': '-'
        }
      }
    },
    '10.200.0.60/30': {
      'network': '10.200.0.60',
      'cidr': 30,
      'via': {
        '10.254.248.10': {
          'interface': 'eth 2/2',
          'cost': '110/38',
          'type': 'O',
          'uptime': '40d0h',
          'src-vrf': '-'
        }
      }
    },
    '10.200.0.65/32': {
      'network': '10.200.0.65',
      'cidr': 32,
      'via': {
        '10.254.248.10': {
          'interface': 'eth 2/2',
          'cost': '110/63',
          'type': 'O',
          'uptime': '40d0h',
          'src-vrf': '-'
        }
      }
    },
    '10.200.0.73/32': {
      'network': '10.200.0.73',
      'cidr': 32,
      'via': {
        '10.254.248.10': {
          'interface': 'eth 2/2',
          'cost': '110/73',
          'type': 'O',
          'uptime': '40d0h',
          'src-vrf': '-'
        }
      }
    },
    '10.200.0.80/30': {
      'network': '10.200.0.80',
      'cidr': 30,
      'via': {
        '10.254.248.10': {
          'interface': 'eth 2/2',
          'cost': '110/76',
          'type': 'O',
          'uptime': '1d1h',
          'src-vrf': '-'
        }
      }
    },
    '10.200.0.85/32': {
      'network': '10.200.0.85',
      'cidr': 32,
      'via': {
        '10.254.248.10': {
          'interface': 'eth 2/2',
          'cost': '110/27',
          'type': 'O',
          'uptime': '40d0h',
          'src-vrf': '-'
        }
      }
    },
    '200.200.200.200/32': {
      'network': '200.200.200.200',
      'cidr': 32,
      'via': {
        'DIRECT': {
          'interface': 'loopback 1',
          'cost': '0/0',
          'type': 'D',
          'uptime': '248d',
          'src-vrf': 'Unknown'
        }
      }
    },
    '1.1.1.1/32': {
      'network': '1.1.1.1',
      'cidr': 32,
      'via': {
        '10.254.251.2': {
          'interface': 'eth 5/1',
          'cost': '110/52',
          'type': 'O',
          'uptime': '15h47m',
          'src-vrf': '-'
        },
        '10.254.251.108': {
          'interface': 'eth 7/1',
          'cost': '110/52',
          'type': 'O',
          'uptime': '15h47m',
          'src-vrf': '-'
        }
      }
    },
    '2.2.2.2/32': {
      'network': '2.2.2.2',
      'cidr': 32,
      'via': {
        '10.254.251.2': {
          'interface': 'eth 5/1',
          'cost': '110/42',
          'type': 'O',
          'uptime': '15h47m',
          'src-vrf': '-'
        },
        '10.254.251.108': {
          'interface': 'eth 7/1',
          'cost': '110/42',
          'type': 'O',
          'uptime': '15h47m',
          'src-vrf': '-'
        }
      }
    }
  }
}
