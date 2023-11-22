expected_output  = {
    'Entropy_target': '256 bits',
    'entropies': {
        1: {
            'entropy_bits': '256/768',
            'requests': '3',
            'source': 'CPU jitter',
            'status': 'Working',
            'type': 'Prim',
        },
        2: {
            'entropy_bits': '384/16896',
            'requests': '44',
            'source': 'ACT-2',
            'status': 'Working',
            'type': 'HW',
        },
        3: {
            'entropy_bits': '128/5888    (*)',
            'requests': '46',
            'source': 'randfill',
            'status': 'Working',
            'type': 'SW',
        },
        4: {
            'entropy_bits': '160/7360    (*)',
            'requests': '46',
            'source': 'getrandombytes',
            'status': 'Working',
            'type': 'SW',
        },
    },
    'entropy_actual_collection': '384 bits',
    'entropy_collection': '60 minutes',
    'entropy_collection_recent': '0 minutes ago',
}
