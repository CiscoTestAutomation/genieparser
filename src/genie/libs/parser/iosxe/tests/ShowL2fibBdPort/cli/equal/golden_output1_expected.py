expected_output = {
    'Et0/2:12': {
        'type': 'BD_PORT',
        'is_pathlist': False,
        'port': 'Et0/2:12'
    },
    '[IR]20012:2.2.2.2': {
        'type':'VXLAN_REP',
        'is_pathlist': True,
        'pathlist': {
            'id': '1191',
            'path_count': '1',
            'type': 'VXLAN_REP',
            'description': '[IR]20012:2.2.2.2'
        }
    },
    '[IR]20012:3.3.3.2': {
        'type':'VXLAN_REP',
        'is_pathlist': True,
        'pathlist': {
            'id': '1184',
            'path_count': '1',
            'type': 'VXLAN_REP',
            'description': '[IR]20012:3.3.3.2'
        }
    }
}