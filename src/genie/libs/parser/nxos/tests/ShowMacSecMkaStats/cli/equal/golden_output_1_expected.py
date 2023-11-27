expected_output = {
    'mka_global_stats': {
        'mka_session_events': {
            'secured_events': 6, 
            'del_secured_events': 6, 
            'keepalive_timeout_events': 160466
        }, 
        'ca_statistics': {
            'pairwise_cak_rekeys': 0
        }, 
        'sa_statistics': {
            'saks_generated': 6, 
            'saks_rekeyed': 0, 
            'saks_recieved': 0, 
            'sak_response_recieved': 6
        }, 
        'mkpdu_statistics': {
            'mkpdu_valid_rx': 39032, 
            'mkpdu_rx_distributed_sak': 8, 
            'mkpdu_tx_distributed_sak': 8, 
            'mkpdus_tx': 160503
        }
    }, 
    'mka_error_cnt_total': {
        'session_failures': {
            'bringup_failures': 0
        }, 
        'sak_failures': {
            'sak_gen': 0, 
            'hash_key_gen': 0, 
            'sack_ecrypt_wrap': 0, 
            'sack_decrypt_unwrap': 0, 
            'sack_cipher_mismatch': 0
        }, 
        'ca_failures': {
            'ick_derivation': 0, 
            'kek_derivation': 0, 
            'invalid_peer_macsec_capab': 0
        }, 
        'macsec_failures': {
            'rx_sa_install': 0, 
            'tx_sa_install': 0
        }, 
        'mkpdu_failures': {
            'mkpdu_tx': 0, 
            'mkpdu_rx_bad_peer_mn': 0, 
            'mkpdu_rx_no_recent_peerlist_mn': 0, 
            'mkpdu_rxdrop_sakuse_kn_mismatch': 0, 
            'mkpdu_rxdrop_sakuse_rx_notset': 0, 
            'mkpdu_rxdrop_sakuse_key_mi_mismatch': 0, 
            'mkpdu_rxdrop_sakuse_an_not_inuse': 0, 
            'mkpdu_rxdrop_sakuse_ks_rxtx_notset': 0
        }, 
        'global_stats': {
            'mkpdu_rx_invalid_ckn': 0, 
            'mkpdu_tx_pkt_build_fail': 0
        }
    }
}