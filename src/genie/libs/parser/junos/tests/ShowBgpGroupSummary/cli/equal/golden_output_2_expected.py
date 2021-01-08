expected_output = {
    'bgp-information': {
        'bgp-peer': [{'peer-address': '20.0.0.2', 'peer-as': '3', 'input-messages': '2', 'output-messages': '3', 'route-queue-count': '0', 'flap-count': '1', 'elapsed-time': {'#text': '9'}, 'peer-state': '0/0/0/0              0/0/0/0'}, {'peer-address': '2001:20::2', 'peer-as': '3', 'input-messages': '2', 'output-messages': '3', 'route-queue-count': '0', 'flap-count': '1', 'elapsed-time': {'#text': '5'}, 'peer-state': 'Establ', 'bgp-rib': [{'name': 'inet6.0', 'active-prefix-count': '0', 'received-prefix-count': '0', 'accepted-prefix-count': '0', 'suppressed-prefix-count': '0'}]}],
        'bgp-rib': [{'name': 'inet.0', 'total-prefix-count': '0', 'active-prefix-count': '0', 'suppressed-prefix-count': '0', 'history-prefix-count': '0', 'damped-prefix-count': '0', 'pending-prefix-count': '0'}, {'name': 'inet6.0', 'total-prefix-count': '0', 'active-prefix-count': '0', 'suppressed-prefix-count': '0', 'history-prefix-count': '0', 'damped-prefix-count': '0', 'pending-prefix-count': '0'}],
        'down-peer-count': '0',
        'group-count': '2',
        'peer-count': '2',
    },
}
				