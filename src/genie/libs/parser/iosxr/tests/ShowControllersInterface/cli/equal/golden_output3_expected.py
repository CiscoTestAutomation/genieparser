expected_output = {
    'interface': {
        'HundredGigE0/8/0/6': {
            'state': {
                'administrative_state': 'disabled',
                'operational_state': 'Down (Reason: Link is shutdown)',
                'led_state': 'Off'
            },
            'phy': {
                'media_type': 'Not known',
                'no_optics_present': True,
                'statistics': {
                    'fec': {
                        'corrected_codeword_count': 0,
                        'uncorrected_codeword_count': 0
                    }
                }
            },
            'mac_address_information': {
                'operational_address': 'fc58.9a12.dc58',
                'burnt_in_address': 'fc58.9a12.dc58'
            },
            'autonegotiation': 'Autonegotiation disabled.',
            'priority_flow_control': {
                'total_rx_pfc_frames': 0,
                'total_tx_pfc_frames': 0,
                'total_rx_dropped_data_frames': 0,
                'cos': {
                    0: {'status': 'off', 'rx_pfc_frames': 0, 'tx_pfc_frames': 0},
                    1: {'status': 'off', 'rx_pfc_frames': 0, 'tx_pfc_frames': 0},
                    2: {'status': 'off', 'rx_pfc_frames': 0, 'tx_pfc_frames': 0},
                    3: {'status': 'off', 'rx_pfc_frames': 0, 'tx_pfc_frames': 0},
                    4: {'status': 'off', 'rx_pfc_frames': 0, 'tx_pfc_frames': 0},
                    5: {'status': 'off', 'rx_pfc_frames': 0, 'tx_pfc_frames': 0},
                    6: {'status': 'off', 'rx_pfc_frames': 0, 'tx_pfc_frames': 0},
                    7: {'status': 'off', 'rx_pfc_frames': 0, 'tx_pfc_frames': 0}
                }
            },
            'operational_values': {
                'speed': '100Gbps',
                'duplex': 'Full Duplex',
                'flowcontrol': 'None',
                'priority_flow_control': 'None',
                'loopback': 'None (or external)',
                'mtu': 1514,
                'mru': 1518,
                'forward_error_correction': 'Not Configured'
            }
        }
    }
}
