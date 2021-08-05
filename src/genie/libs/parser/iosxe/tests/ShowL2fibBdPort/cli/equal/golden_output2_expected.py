expected_output = {
    'Et0/1:11': {
        'type': 'BD_PORT',
        'is_pathlist': False,
        'port': 'Et0/1:11'
    },
    '[IR]20011:2.2.2.2': {
        'type':'VXLAN_REP',
        'is_pathlist': True,
        'pathlist': {
            'id': '1190',
            'path_count': '1',
            'type': 'VXLAN_REP',
            'description': '[IR]20011:2.2.2.2'
        }
    },
    '[IR]20011:3.3.3.2': {
        'type':'VXLAN_REP',
        'is_pathlist': True,
        'pathlist': {
            'id': '1183',
            'path_count': '1',
            'type': 'VXLAN_REP',
            'description': '[IR]20011:3.3.3.2'
        }
    }
}