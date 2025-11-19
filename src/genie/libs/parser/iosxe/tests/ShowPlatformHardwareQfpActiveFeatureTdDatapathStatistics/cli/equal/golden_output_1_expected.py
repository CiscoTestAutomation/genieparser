expected_output = {
    'events_errors': {
        'hex_limit': 0,
        'invalid_opt': 0,
        'invalid_sync': 0,
        'invalid_tx': 0,
        'mem_err': 0,
        'pa_err': 0,
        'pkt_err': 0,
        'punt_err': 0,
        'tcp_fixup_drop': 0,
        'tcp_flag_noack': 0,
        'tcp_invalid_rx': 0,
    },
    'pool_usage': {
        'buf_size_alloc': {
            'alloc': 0,
            'free': 0,
        },
        'pkt_buf_alloc': {
            'alloc': 0,
            'fail': 0,
            'free': 0,
        },
        'vtcp_info_alloc': {
            'alloc': 2,
            'fail': 0,
            'free': 0,
        },
    },
    'receive': {
        'alg_proc_csum': 0,
        'dup_ack': 2,
        'lisp_seg': 0,
        'off_csum': 0,
        'out_of_order': 0,
        'overlap': 0,
        'retrans': 0,
    },
    'send': {
        'hold_rst': 0,
        'rst': 0,
        'rx_ack': 0,
        'tx_hold_rexmit': 0,
        'tx_rexmit': 0,
        'tx_seg': 0,
    },
}