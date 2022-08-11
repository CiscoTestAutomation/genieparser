expected_output = {
    'interfaces': {
        'mgmt0': {
            'ipv4': {
                'neighbors': {
                    '10.48.3.254': {
                        'ip': '10.48.3.254',
                        'link_layer_address': '0000.5e00.0101',
                        'age': '00:00:05',
                        'physical_interface': 'mgmt0',
                        'origin': 'dynamic'
                    }
                }
            }
        }, 
        'Ethernet1/54': {
            'ipv4': {
                'neighbors': {
                    '172.20.12.16': {
                        'ip': '172.20.12.16',
                        'link_layer_address': '10b3.d6dc.0293',
                        'age': '00:03:13',
                        'physical_interface': 'Ethernet1/54',
                        'origin': 'dynamic'
                    }
                }
            }
        },
        'Vlan3622': {
            'ipv4': {
                'neighbors': {
                    '172.20.12.18': {
                        'ip': '172.20.12.18',
                        'link_layer_address': '7c21.0e12.3627',
                        'age': '00:01:53',
                        'physical_interface': 'port-channel1000',
                        'origin': 'dynamic'
                    }
                }
            }
        },
        'port-channel1100.3623': {
            'ipv4': {
                'neighbors': {
                    '172.24.8.85': {
                        'ip': '172.24.8.85',
                        'link_layer_address': '7c21.0e12.3627',
                        'age': '00:16:58',
                        'physical_interface': 'port-channel1100.3623',
                        'origin': 'dynamic'
                    }
                }
            }
        },
        'port-channel1100.3624': {
            'ipv4': {
                'neighbors': {
                    '172.24.8.89': {
                        'ip': '172.24.8.89',
                        'link_layer_address': '7c21.0e12.3627',
                        'age': '00:17:00',
                        'physical_interface': 'port-channel1100.3624',
                        'origin': 'dynamic'
                    }
                }
            }
        },
        'Vlan240': {
            'ipv4': {
                'neighbors': {
                    '192.168.240.59': {
                        'ip': '192.168.240.59',
                        'link_layer_address': '0cc4.7aee.9c2e',
                        'age': '00:02:40',
                        'physical_interface': 'port-channel1000',
                        'origin': 'dynamic',
                        'flag': 'Adjacencies synced via CFSoE'
                    }, 
                    '192.168.240.62': {
                        'ip': '192.168.240.62',
                        'link_layer_address': 'a2b6.9300.0003',
                        'age': '00:12:56',
                        'physical_interface': 'Ethernet163/1/47',
                        'origin': 'dynamic'
                    }
                }
            }
        }
    }
}
