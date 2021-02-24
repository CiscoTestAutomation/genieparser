expected_output = {
    'ddos-protocols-information': {
        'ddos-protocol-group': {
            'ddos-protocol': {
                'ddos-basic-parameters': {
                    'policer-bandwidth': '2000',
                    'policer-burst': '10000',
                    'policer-enable': 'Yes',
                    'policer-time-recover': '300',
                },
                'ddos-flow-detection': {
                    'detect-time': '3',
                    'detection-mode': 'Automatic',
                    'flow-aggregation-level-states': {
                        'ifd-bandwidth': '2000',
                        'ifd-control-mode': 'Drop',
                        'ifd-detection-mode': 'Automatic',
                        'ifl-bandwidth': '10',
                        'ifl-control-mode': 'Drop',
                        'ifl-detection-mode': 'Automatic',
                        'sub-bandwidth': '10',
                        'sub-control-mode': 'Drop',
                        'sub-detection-mode': 'Automatic',
                    },
                    'log-flows': 'Yes',
                    'recover-time': '60',
                    'timeout-active-flows': 'No',
                    'timeout-time': '300',
                },
                'ddos-instance': [{'protocol-states-locale': 'Routing Engine', 'ddos-instance-statistics': {'packet-received': '3', 'packet-arrival-rate': '0', 'packet-dropped': '0', 'packet-arrival-rate-max': '0'}, 'ddos-instance-parameters': {'policer-bandwidth': '2000', 'policer-burst': '10000', 'policer-enable': 'enabled'}}],
                'ddos-system-statistics': {
                    'packet-arrival-rate': '0',
                    'packet-arrival-rate-max': '0',
                    'packet-dropped': '0',
                    'packet-received': '3',
                },
                'packet-type': 'host-route-v4',
                'packet-type-description': 'unclassified v4 hostbound packets',
            },
            'group-name': 'Unclassified',
        },
        'flows-cumulative': '0',
        'flows-current': '0',
    },
}
				