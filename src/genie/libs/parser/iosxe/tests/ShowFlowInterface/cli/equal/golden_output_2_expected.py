expected_output = {
    'interface': {
        'FiftyGigE1/0/36': {
            'fnf': {
                'datalink_monitor_in': {
                    'direction': {
                        'Input': {
                            'traffic': {
                                'type': 'datalink', 
                                'sampler': 'sampler_random'
                            }
                        }
                    }
                }
            }
        }, 
        'Port-channel10': {
            'fnf': {
                'datalink_monitor_in': {
                    'direction': {
                        'Input': {
                            'traffic': {
                                'type': 'datalink', 
                                'sampler': 'sampler_random'
                            }
                        }
                    }
                }
            }
        }
    }
}