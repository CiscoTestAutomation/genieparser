expected_output = {
            'tracker_name': {
                'group-udp-tcp-10001': {
                    'element_trackers_name': 'tcp-10002, udp-10002',
                    'status': 'UP(UP OR UP)',
                    'rtt_in_msec': '1, 1',
                    'probe_id': '7, 8'
                },
                'group2': {
                    'element_trackers_name': 'track1, track2',
                    'status': 'UP(UP OR UP)',
                    'rtt_in_msec': '14, 14',
                    'probe_id': '201, 202'
                },
                'group3': {
                    'element_trackers_name': 'track1, track2',
                    'status': 'DOWN(DOWN OR DOWN)',
                    'rtt_in_msec': 'Timeout, Timeout',
                    'probe_id': '0, 0'
                }
            }
        }
