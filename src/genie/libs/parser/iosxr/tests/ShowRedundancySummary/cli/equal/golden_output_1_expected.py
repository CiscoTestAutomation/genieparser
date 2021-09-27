

expected_output = {
    "redundancy_communication": True,
    'node': {
        '0/RSP0/CPU0(A)': {
            'node_detail': 'Node Not Ready, NSR: Not '
                           'Configured',
            'standby_node': '0/RSP1/CPU0(S)',
            'type': 'active'},
        '0/RSP0/CPU0(P)': {
            'backup_node': '0/RSP1/CPU0(B)',
            'node_detail': 'Proc Group Not Ready, NSR: '
                           'Ready',
            'standby_node': '0/RSP1/CPU0(B)',
            'type': 'primary'}}}
