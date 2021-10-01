

expected_output = {
    'sdr_id': {
        0: {
            'dsdrsc_node': '0/RSP0/CPU0',
            'dsdrsc_partner_node': '0/RSP1/CPU0',
            'mac_address': 'a80c.0dff.0b76',
            'membership': {
                '0/0/CPU0': {
                    'node_status': 'IOS XR RUN',
                    'partner_name': 'NONE',
                    'red_state': 'Not-known',
                    'type': 'LC'},
                '0/RSP0/CPU0': {
                    'node_status': 'IOS XR RUN',
                    'partner_name': '0/RSP1/CPU0',
                    'red_state': 'Primary',
                    'type': 'RP'},
                '0/RSP1/CPU0': {
                    'node_status': 'IOS XR RUN',
                    'partner_name': '0/RSP0/CPU0',
                    'red_state': 'Backup',
                    'type': 'RP'}},
            'primary_node1': '0/RSP0/CPU0',
            'primary_node2': '0/RSP1/CPU0',
            'sdr_name': 'Owner'}}}
