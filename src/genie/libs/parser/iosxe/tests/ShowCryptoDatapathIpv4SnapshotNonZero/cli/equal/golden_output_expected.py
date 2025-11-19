expected_output = {
    'success_statistics': {
        'snapshot_timestamp': '21:34:30 PST Mar 4 2006',
        'crypto_check_input_core': {
            '2nd_round_ok': 245,
            '1st_round_ok': 118
        },
        'post_crypto_ip_encrypt': {
            'post_encrypt_ipflowok': 230
        },
        'crypto_ceal_post_encrypt_switch': {
            'post_encrypt_ipflowok_2': 230
        }
    },
    'error_statistics': {
        'snapshot_timestamp': '21:34:30 PST Mar 4 2006'
    },
    'punt_statistics': {
        'snapshot_timestamp': '21:34:30 PST Mar 4 2006',
        'crypto_ceal_post_decrypt_switch': {
            'fs_to_ps': 245
        }
    },
    'internal_statistics': {
        'snapshot_timestamp': '21:34:30 PST Mar 4 2006',
        'crypto_check_input': {
            'check_input_core_not_con': 378,
            'check_input_core_consume': 623
        },
        'crypto_check_input_core': {
            'came_back_from_ce': 245,
            'deny_pak': 15
        },
        'crypto_ipsec_les_fs': {
            'not_esp_or_ah': 1113
        },
        'post_crypto_ip_decrypt': {
            'decrypt_switch': 245
        },
        'crypto_decrypt_ipsec_sa_check': {
            'check_ident_success': 245
        },
        'crypto_ceal_post_decrypt_switch': {
            'fs': 245
        },
        'crypto_ceal_post_decrypt_fs': {
            'les_ip_turbo_fs': 245,
            'tunnel_ip_les_fs': 245
        },
        'crypto_ceal_post_decrypt_ps': {
            'proc_inline': 245
        },
        'crypto_ceal_punt_to_process_inline': {
            'coalesce': 245,
            'simple_enq': 245
        },
        'crypto_ceal_post_encrypt_switch': {
            'ps': 230
        },
        'crypto_ceal_post_encrypt_ps': {
            'ps_coalesce': 230,
            'simple_enq': 230
        },
        'crypto_engine_ps_vec': {
            'ip_encrypt': 230
        },
        'crypto_send_epa_packets': {
            'ucast_next_hop': 230,
            'ip_ps_send': 230
        }
    }
}
