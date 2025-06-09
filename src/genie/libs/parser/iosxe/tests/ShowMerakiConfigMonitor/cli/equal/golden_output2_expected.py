expected_output = {
    'current_state': "Ready",
    'instances': {
        1: {
            'config_change_time': "2025-04-02 08:03:05",
            'xpaths_seen': 1,
            'xpaths': {
                1: {
                    'path': "/ios:native/ios:interface/ios:GigabitEthernet[ios:name='0/0']/ios-eth:negotiation/ios-eth:auto",
                    'operation': "Delete"
                },
            }
        },
        2: {
            'config_change_time': "2025-04-01 22:22:38",
            'xpaths_seen': 2,
            'xpaths': {
                1: {
                    'path': "/ios:native/ios:interface/ios:GigabitEthernet[ios:name='0/0']/ios-eth:negotiation/ios-eth:auto",
                    'operation': "Delete"
                },
                2: {
                    'path': "/ios:native/ios:interface/ios:GigabitEthernet[ios:name='3/0/1']",
                    'operation': "Create"
                },
            },
        }
    }
}
