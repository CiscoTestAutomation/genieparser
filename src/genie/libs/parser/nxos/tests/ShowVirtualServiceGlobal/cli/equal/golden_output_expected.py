

expected_output = {
    'version': '1.10',
    'virtual_services': {
        'installed': 1,
        'activated': 1,
    },
    'machine_types': {
        'supported': ['LXC'],
        'disabled': ['KVM'],
    },
    'resource_limits': {
        'cpus_per_service': 1,
        'cpu': {
            'quota': 20,
            'committed': 1,
            'available': 19,
        },
        'memory': {
            'quota': 3840,
            'committed': 500,
            'available': 3340,
        },
        'bootflash': {
            'quota': 8192,
            'committed': 1000,
            'available': 7192,
        },
    },
}
