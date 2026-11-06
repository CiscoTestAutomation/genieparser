expected_output = {
    'hatseflats-1': {'networks': {
        1: {'ip': '172.16.2.0', 'subnet_mask': '255.255.255.0', 'secondary': False}},
        'dhcp_options': {}, 'dhcp_excludes': {}},
    'hatseflats-2': {'networks': {
        1: {'ip': '172.16.3.0', 'subnet_mask': '255.255.255.0',
            'secondary': False}}, 'dhcp_options': {},
        'dhcp_excludes': {}}, 'TEST-1': {'networks': {
        1: {'ip': '12.1.1.0', 'subnet_mask': '255.255.255.0', 'secondary': False},
        2: {'ip': '13.1.0.0', 'subnet_mask': '255.255.254.0', 'secondary': True}},
        'dhcp_options': {
            1: {
                'option': '150',
                'type': 'ip',
                'data': '10.1.1.100'},
            2: {
                'option': '43',
                'type': 'ip',
                'data': '12.1.1.1'}},
        'dhcp_excludes': {
            1: {
                'start': '12.1.1.10',
                'end': '12.1.1.10'},
            2: {
                'start': '12.1.1.12',
                'end': '12.1.1.114'}},
        'vrf': 'lala',
        'domain': 'nelis.nl',
        'dns_servers': [
            '10.1.1.99',
            '10.1.1.100'],
        'netbios_servers': [
            '10.1.1.101',
            '10.1.1.102']},
    'BFR-test-voice': {'networks': {
        1: {'ip': '172.19.0.0', 'subnet_mask': '255.255.0.0',
            'secondary': False}}, 'dhcp_options': {
        1: {'option': '43', 'type': 'hex',
            'data': '010a.5369.656d.656e.7300.0000.0204.0000.0258.0317.7364.6c70.3a2f.2f31.3732.2e31.372e.302e.323a.3138.3434.33ff'}},
        'dhcp_excludes': {},
        'domain': 'test-voice.local',
        'gateway': '172.19.0.254',
        'dns_servers': ['10.31.1.1', '10.31.107.253']},
    'test-company-(CGR)': {'networks': {
        1: {'ip': '10.1.10.0', 'subnet_mask': '255.255.255.0',
            'secondary': False}}, 'dhcp_options': {
        1: {'option': '150', 'type': 'ip', 'data': '139.156.73.67'}},
        'dhcp_excludes': {1: {'start': '10.1.10.2',
                              'end': '10.1.1.20'}},
        'gateway': '10.1.10.1',
        'dns_servers': ['213.162.171.133',
                        '213.162.171.134']}, 'cxbeh': {
        'networks': {1: {'ip': '10.111.10.0', 'subnet_mask': '255.255.255.0',
                         'secondary': False}},
        'dhcp_options': {1: {'option': '66', 'type': 'ascii', 'data': '"10.12.1.10"'}},
        'dhcp_excludes': {}, 'dns_servers': ['10.100.1.5'], 'domain': 'woonzorg.local',
        'gateway': '10.111.10.1', 'boot_file': 'testfile'}, 'DHCP_TEST1': {'networks': {
        1: {'ip': '10.222.0.0', 'subnet_mask': '255.255.0.0', 'secondary': False}},
        'dhcp_options': {
            1: {'option': '43',
                'type': 'hex',
                'data': '3a02.14ff'},
            2: {'option': '201',
                'type': 'ascii',
                'data': "'10.80.3.33' '40003'"},
            3: {'option': '202',
                'type': 'ip',
                'data': '10.80.3.33'}},
        'dhcp_excludes': {},
        'domain': 'corp.csu.lan',
        'dns_servers': ['10.80.2.4',
                        '10.80.2.5'],
        'gateway': '10.222.254.254',
        'lease_time': '8'}, 'Mitel': {
        'networks': {1: {'ip': '172.16.100.0', 'subnet_mask': '255.255.255.0',
                         'secondary': False}}, 'dhcp_options': {
            1: {'option': '43', 'type': 'ascii',
                'data': 'id:ipphone.mitel.com;call_srv=143.0.0.1;vlan=40;l2p=6;dscp=46;sw_tftp=143.0.0.1'}},
        'dhcp_excludes': {}, 'gateway': '172.16.100.200'}, 'SUVM1202': {'networks': {
        1: {'ip': '130.1.41.0', 'subnet_mask': '255.255.255.0', 'secondary': False}},
        'dhcp_options': {
            1: {
                'option': '186',
                'type': 'ip',
                'data': '172.24.1.2'},
            2: {
                'option': '190',
                'type': 'hex',
                'data': '01bb'},
            3: {
                'option': '161',
                'type': 'ascii',
                'data': '"172.24.1.2"'},
            4: {
                'option': '184',
                'type': 'ascii',
                'data': '"wdmserverrapport"'},
            5: {
                'option': '185',
                'type': 'ascii',
                'data': '"DellWyse"'}},
        'dhcp_excludes': {},
        'gateway': '130.1.41.253'}}