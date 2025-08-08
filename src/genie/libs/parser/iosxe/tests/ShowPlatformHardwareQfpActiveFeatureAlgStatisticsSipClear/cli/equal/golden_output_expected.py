expected_output = {
    'sip_info_pool_used_chunk_entries_number': 1,
    'receive': {
        'register': {
            'count': 0,
            '200_ok': 0
        },
        'invite': {
            'count': 1,
            '200_ok': 0,
            'rexmit_invite': 1
        },
        'update': {
            'count': 0,
            '200_ok': 0
        },
        'bye': {
            'count': 0,
            '200_ok': 0
        },
        'subscribe': {
            'count': 0,
            '200_ok': 0
        },
        'refer': {
            'count': 0,
            '200_ok': 0
        },
        'prack': {
            'count': 0,
            '200_ok': 0
        },
        'trying': 0,
        'ringing': 0,
        'ack': 0,
        'info': 0,
        'cancel': 0,
        'sess_prog': 0,
        'message': 0,
        'notify': 0,
        'publish': 0,
        'options': 0,
        '1xx': 0,
        '2xx': 0,
        'other_req': 0,
        'other_ok': 0,
        '3xx_6xx': 0
    },
    'events': {
        'null_dport': 0,
        'media_port_zero': 0,
        'malform_media': 0,
        'no_content_length': 0,
        'cr_trunk_chnls': 1,
        'del_trunk_chnls': 0,
        'start_trunk_timer': 1,
        'restart_trunk_timer': 0,
        'stop_trunk_timer': 0,
        'trunk_timer_timeout': 0,
        'cr_dbl_entry': 0,
        'del_dbl_entry': 0,
        'cr_dbl_cfg_entry': 0,
        'del_dbl_cfg_entry': 0,
        'start_dbl_trig_tmr': 0,
        'restart_dbl_trig_tmr': 0,
        'stop_dbl_trig_tmr': 0,
        'dbl_trig_timeout': 0,
        'start_dbl_blk_tmr': 0,
        'restart_dbl_blk_tmr': 0,
        'stop_dbl_blk_tmr': 0,
        'dbl_blk_tmr_timeout': 0,
        'start_dbl_idle_tmr': 0,
        'restart_dbl_idle_tmr': 0,
        'stop_dbl_idle_tmr': 0,
        'dbl_idle_tmr_timeout': 0,
        'media_addr_zero': 0,
        'need_more_data': 0,
        'sip_pkt_alloc': 2,
        'sip_pkt_free': 2,
        'sip_msg_alloc': 0,
        'sip_msg_free': 0
    },
    'errors': {
        'create_token_err': 0,
        'add_portlist_err': 0,
        'invalid_offset': 0,
        'invalid_pktlen': 0,
        'free_magic': 0,
        'double_free': 0,
        'sess_retmem_failed': 0,
        'sess_malloc_failed': 0,
        'pkt_retmem_failed': 0,
        'pkt_malloc_failed': 0,
        'msg_retmem_failed': 0,
        'msg_malloc_failed': 0,
        'bad_format': 0,
        'invalid_proto': 0,
        'add_alg_state_fail': 0,
        'no_call_id': 0,
        'parse_sip_hdr_fail': 0,
        'parse_sdp_fail': 0,
        'error_new_chnl': 0,
        'huge_size': 0,
        'create_failed': 0,
        'not_sip_msg': 0
    },
    'writeback_errors': {
        'offset_err': 0,
        'pa_err': 0,
        'no_info': 0
    },
    'dos_errors': {
        'dbl_retmem_failed': 0,
        'dbl_malloc_failed': 0,
        'dblcfg_retm_failed': 0,
        'dblcfg_malloc_failed': 0,
        'session_wlock_ovflw': 0,
        'global_wlock_ovflw': 0,
        'blacklisted': 0
    },
    'sip_alg_counters_cleared': 'SIP ALG counters cleared after display.'
}
