expected_output = {
    'isis': {
        '1': {
            'process_id': '1',
            'routes_found': False
        },
        '10': {
            'process_id': '10',
            'routes_found': True,
            'level': {
                '2': {
                    'lspid': {
                        'P-9001-1.00-00': {
                            'lspid': 'P-9001-1.00-00',
                            'lsp_seq_num': '* 0x000007f7  ',
                            'lsp_checksum': '0x54eb',
                            'lsp_holdtime': '533',
                            'rcvd': '*',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0
                        }
                    },
                    'total_level': 2,
                    'total_lsp_count': 1,
                    'local_level': 2,
                    'local_lsp_count': 1
                }
            }
        },
        '99': {
            'process_id': '99',
            'routes_found': True,
            'level': {
                '1': {
                    'lspid': {
                        'P-9001-1.00-00': {
                            'lspid': 'P-9001-1.00-00',
                            'lsp_seq_num': '* 0x0000038f  ',
                            'lsp_checksum': '0xfcf3',
                            'lsp_holdtime': '1106',
                            'rcvd': '*',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0
                        }
                    },
                    'total_level': 1,
                    'total_lsp_count': 1,
                    'local_level': 1,
                    'local_lsp_count': 1
                }
            }
        }
    }
}
