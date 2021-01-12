expected_output = {
    'ddos-protocols-information': {
        'ddos-protocol-group': {
            'ddos-protocol': {
                'ddos-basic-parameters': {
                    'policer-bandwidth': '20000',
                    'policer-burst': '20000',
                    'policer-enable': 'Yes',
                    'policer-time-recover': '300',
                },
                'ddos-flow-detection': {
                    'detect-time': '3',
                    'detection-mode': 'Automatic',
                    'flow-aggregation-level-states': {
                        'ifd-bandwidth': '20000',
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
                'ddos-instance': [{'protocol-states-locale': 'Routing Engine', 'ddos-instance-statistics': {'packet-received': '0', 'packet-arrival-rate': '0', 'packet-dropped': '0', 'packet-arrival-rate-max': '0'}, 'ddos-instance-parameters': {'policer-bandwidth': '20000', 'policer-burst': '20000', 'policer-enable': 'enabled'}}],
                'ddos-system-statistics': {
                    'packet-arrival-rate': '0',
                    'packet-arrival-rate-max': '0',
                    'packet-dropped': '0',
                    'packet-received': '0',
                },
                'packet-type': 'aggregate',
                'packet-type-description': 'Aggregate for all arp traffic',
            },
            'group-name': 'ARP',
        },
        'flows-cumulative': '0',
        'flows-current': '0',
        'mod-packet-types': '0',
        'packet-types-in-violation': '0',
        'packet-types-rcvd-packets': '0',
        'total-packet-types': '1',
    },
}
				