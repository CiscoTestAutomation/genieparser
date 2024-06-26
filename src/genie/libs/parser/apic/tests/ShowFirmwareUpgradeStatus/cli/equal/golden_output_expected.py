expected_output = {
        'node': {
            1: {
                'pod': 1,
                'current_firmware': 'apic-4.2(4o)',
                'status': 'success',
                'upgrade_progress_percentage': 100
            },
            101: {
                'pod': 1,
                'current_firmware': 'unknown',
                'target_firmware': 'unknown',
                'status': 'node unreachable'
            },
            102: {
                'pod': 1,
                'current_firmware': 'n9000-14.2(4q)',
                'status': 'not scheduled',
                'upgrade_progress_percentage': 0
            },
            201: {
                'pod': 1,
                'current_firmware': 'unknown',
                'target_firmware': 'unknown',
                'status': 'node unreachable'
            }
        }
    }