expected_output = {
  'total_routes': 13,
  'vrf': {
    'default': {
      'routes': {
        '10.200.0.12/30': {
          'network': '10.200.0.12',
          'netmask': 30,
          'via': {
            '10.254.248.10': {
              'interface': 'eth 2/2',
              'cost': '110/28',
              'type': 'O',
              'uptime': '40d0h',
              'src-vrf': 'local'
            }
          }
        },
        '10.200.0.16/30': {
          'network': '10.200.0.16',
          'netmask': 30,
          'via': {
            '10.254.248.10': {
              'interface': 'eth 2/2',
              'cost': '110/194',
              'type': 'O',
              'uptime': '6d12h',
              'src-vrf': 'local'
            }
          }
        },
        '10.200.0.28/30': {
          'network': '10.200.0.28',
          'netmask': 30,
          'via': {
            '10.254.248.10': {
              'interface': 'eth 2/2',
              'cost': '110/138',
              'type': 'O',
              'uptime': '40d0h',
              'src-vrf': 'local'
            }
          }
        },
        '10.200.0.32/30': {
          'network': '10.200.0.32',
          'netmask': 30,
          'via': {
            '10.254.248.10': {
              'interface': 'eth 2/2',
              'cost': '110/36',
              'type': 'O',
              'uptime': '40d0h',
              'src-vrf': 'local'
            }
          }
        },
        '10.200.0.56/30': {
          'network': '10.200.0.56',
          'netmask': 30,
          'via': {
            '10.254.248.10': {
              'interface': 'eth 2/2',
              'cost': '110/36',
              'type': 'O',
              'uptime': '12d4h',
              'src-vrf': 'local'
            }
          }
        },
        '10.200.0.60/30': {
          'network': '10.200.0.60',
          'netmask': 30,
          'via': {
            '10.254.248.10': {
              'interface': 'eth 2/2',
              'cost': '110/38',
              'type': 'O',
              'uptime': '40d0h',
              'src-vrf': 'local'
            }
          }
        },
        '10.200.0.65/32': {
          'network': '10.200.0.65',
          'netmask': 32,
          'via': {
            '10.254.248.10': {
              'interface': 'eth 2/2',
              'cost': '110/63',
              'type': 'O',
              'uptime': '40d0h',
              'src-vrf': 'local'
            }
          }
        },
        '10.200.0.73/32': {
          'network': '10.200.0.73',
          'netmask': 32,
          'via': {
            '10.254.248.10': {
              'interface': 'eth 2/2',
              'cost': '110/73',
              'type': 'O',
              'uptime': '40d0h',
              'src-vrf': 'local'
            }
          }
        },
        '10.200.0.80/30': {
          'network': '10.200.0.80',
          'netmask': 30,
          'via': {
            '10.254.248.10': {
              'interface': 'eth 2/2',
              'cost': '110/76',
              'type': 'O',
              'uptime': '1d1h',
              'src-vrf': 'local'
            }
          }
        },
        '10.200.0.85/32': {
          'network': '10.200.0.85',
          'netmask': 32,
          'via': {
            '10.254.248.10': {
              'interface': 'eth 2/2',
              'cost': '110/27',
              'type': 'O',
              'uptime': '40d0h',
              'src-vrf': 'local'
            }
          }
        },
        '192.168.195.200/32': {
          'network': '192.168.195.200',
          'netmask': 32,
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
        '10.4.1.1/32': {
          'network': '10.4.1.1',
          'netmask': 32,
          'via': {
            '10.254.251.2': {
              'interface': 'eth 5/1',
              'cost': '110/52',
              'type': 'O',
              'uptime': '15h47m',
              'src-vrf': 'local'
            },
            '10.254.251.108': {
              'interface': 'eth 7/1',
              'cost': '110/52',
              'type': 'O',
              'uptime': '15h47m',
              'src-vrf': 'local'
            }
          }
        },
        '10.16.2.2/32': {
          'network': '10.16.2.2',
          'netmask': 32,
          'via': {
            '10.254.251.2': {
              'interface': 'eth 5/1',
              'cost': '110/42',
              'type': 'O',
              'uptime': '15h47m',
              'src-vrf': 'local'
            },
            '10.254.251.108': {
              'interface': 'eth 7/1',
              'cost': '110/42',
              'type': 'O',
              'uptime': '15h47m',
              'src-vrf': 'local'
            }
          }
        }
      }
    }
  }
}
