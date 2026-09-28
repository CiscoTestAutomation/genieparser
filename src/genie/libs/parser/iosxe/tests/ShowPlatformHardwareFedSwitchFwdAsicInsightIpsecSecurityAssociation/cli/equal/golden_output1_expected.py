expected_output =  {
    'security_associations': {
        'EGRESS': {
            3167388969: {
                'algorithm': 'AES_GCM_256',
                'direction': 'EGRESS',
                'encrypt_bytes': 10022320,
                'encrypt_errors': 0,
                'encrypt_pkts': 10024,
                'esn': True,
                'h_value': '0x4e7712f4ea4ab07730b272ece775322c5dbcc6b027d26da93fedc167439a34e3',
                'key': '0xa8c7aa15d54b1f15408f307505dbfd30234149ec8357e6d85fe480038a0ad6df',
                'key_extra': '0x6a89a15b0000000000000000',
                'next_pn': 10025,
                'spi': 3167388969,
            },
        },
        'INGRESS': {
            947601419: {
                'algorithm': 'AES_GCM_256',
                'anti_replay': False,
                'current_pn': 10025,
                'decrypt_bytes': 10022320,
                'decrypt_errors': 0,
                'decrypt_pkts': 10024,
                'direction': 'INGRESS',
                'errors': 0,
                'esn': True,
                'h_value': '0xdf5ea8a080f328368d1424fee30784225f50e514c6a81c03075d3e3f3db84436',
                'key': '0x211f4b9baded6823bbac229fd4cc7bf8cb892aefb03e5a6578fcf27bc6ad5caf',
                'key_extra': '0x45f0009a0000000000000000',
                'spi': 947601419,
            },
        },
    },
}
