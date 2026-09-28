expected_output = {
    'acl_entries': {
        'priority': {
            0: {
                'counter_oid': 1523,
                'dport': 67,
                'hit_count': 0,
                'protocol': 17,
                'sport': 68,
            },
            3: {
                'counter_oid': 1526,
                'dport': 547,
                'hit_count': 40,
                'protocol': 17,
                'sport': 546,
            },
            7: {
                'counter_oid': 1530,
                'hit_count': 30,
                'icmp_v6_type': 134,
            },
            20015: {
                'counter_oid': 2592,
                'hit_count': 0,
                'ipv6_sip': '2001:db8:100:1::',
                'ipv6_sip_mask': 'ffff:ffff:ffff:ffff::',
                'ssp': 52,
                'vlan': 200,
            },
            20016: {
                'drop': 'true',
                'hit_count': 0,
                'ipv4_sip': '0.0.0.0',
                'ipv4_sip_mask': '255.255.255.255',
                'vlan': 0,
            },
            50015: {
                'counter_oid': 2591,
                'drop': 'true',
                'hit_count': 4,
                'ssp': 52,
            },
        },
    },
}
