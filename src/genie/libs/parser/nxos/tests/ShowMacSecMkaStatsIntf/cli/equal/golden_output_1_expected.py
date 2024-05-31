expected_output = {
    'Ethernet1/97/2': {
        'per_ca_mka_stats': {
            'ca_statistics': {
                'pairwise_cak_rekeys': 0
            }, 
            'sa_statistics': {
                'saks_generated': 0, 
                'saks_rekeyed': 0, 
                'saks_received': 0, 
                'sak_response_received': 0
            }, 
            'mkpdu_statistics': {
                'mkpdus_tx': 21657, 
                'mkpdu_rx_distributed_sak': 0, 
                'mkpdu_tx_distributed_sak': 0, 
                'mkpdu_valid_rx': 0
            }
        },
        'mka_stats': {
            'ca_statistics': {
                'pairwise_cak_rekeys': 0
            }, 
            'sa_statistics': {
                'saks_generated': 1, 
                'saks_rekeyed': 0, 
                'saks_received': 0, 
                'sak_response_received': 1
            }, 
            'mkpdu_statistics': {
                'mkpdus_tx': 37777, 
                'mkpdu_rx_distributed_sak': 0, 
                'mkpdu_tx_distributed_sak': 1, 
                'mkpdu_valid_rx': 16105
            }, 
            'mka_idb_stat': {
                'mkpdu_tx_success': 37777, 
                'mkpdu_tx_fail': 0, 
                'mkpdu_tx_build_fail': 0, 
                'mkpdu_no_tx_on_intf_down': 0, 
                'mkpdu_no_rx_on_intf_down': 0, 
                'mkpdu_rx_ca_not_found': 0, 
                'mkpdu_rx_error': 0, 
                'mkpdu_rx_success': 16105
            }, 
            'mkpdu_failures': {
                'mkpdu_rx_validation': 0, 
                'mkpdu_rx_bad_peer_mn': 0, 
                'mkpdu_rx_no_recent_peerlist_mn': 0, 
                'mkpdu_rxdrop_sakuse_kn_mismatch': 0, 
                'mkpdu_rxdrop_sakuse_rx_notset': 0, 
                'mkpdu_rxdrop_sakuse_key_mi_mismatch': 0, 
                'mkpdu_rxdrop_sakuse_an_not_inuse': 0, 
                'mkpdu_rxdrop_sakuse_ks_rxtx_notset': 0, 
                'mkpdu_rx_drp_pkt_eth_mismatch': 0,
                'mkpdu_rx_drp_pkt_dest_mac_mismatch': 0
            }, 
            'sak_failures': {
                'sak_gen': 0, 
                'hash_key_gen': 0, 
                'sack_ecrypt_wrap': 0, 
                'sack_decrypt_unwrap': 0
            }, 
            'ca_failures': {
                'ick_derivation': 0, 
                'kek_derivation': 0, 
                'invalid_peer_macsec_capab': 0
            }, 
            'macsec_failures': {
                'rx_sa_install': 0, 
                'tx_sa_install': 0
            }
        }
    }
}