expected_output = {
    'interface': {
        'HundredGigE5/0/15': {
            'fnf': {
                'DreamLine-Monitor': {
                    'direction': {
                        'Input': {
                            'traffic': {
                                'sampler': 'Netflow-Sample',
                                'type': 'ip'
                            }
                        }
                    }
                },
                'FlowMonitor-1': {
                    'direction': {
                        'Output': {
                            'traffic': {
                                'sampler': 'Netflow-Sample',
                                'type': 'ip'
                            }
                        }
                    }
                }
            }
        }
    }
}