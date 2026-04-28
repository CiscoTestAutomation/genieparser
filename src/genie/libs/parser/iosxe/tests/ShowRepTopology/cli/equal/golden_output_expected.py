expected_output = {
    'segment': {
        1: {
            'interfaces': {
                'GigabitEthernet1/0/1': {
                    'bridge': 'C9200_DUT',
                              'edge': 'Pri*',
                              'port': 'GigabitEthernet1/0/1',
                              'role': 'Open'},
                'GigabitEthernet1/0/2': {
                              'bridge': 'C9200_DUT',
                              'edge': 'Sec*',
                              'port': 'GigabitEthernet1/0/2',
                              'role': 'Alt'
                }
            }
        },
        3: {
            'interfaces': {
                'GigabitEthernet1/0/3': {
                    'bridge': 'C9200_DUT',
                    'edge': 'Pri*',
                    'port': 'GigabitEthernet1/0/3',
                    'role': 'Alt'
                },
                'GigabitEthernet1/0/4': {
                    'bridge': 'C9200_DUT',
                    'edge': 'Sec*',
                    'port': 'GigabitEthernet1/0/4',
                    'role': 'Open'
                }
            }
        }
    }
}