expected_output = {
    'global_isdn_switchtype': 'primary-5ess',
    'interface': {
        'Serial1/1/0:15': {
            'dsl': 0,
            'interface_isdn_switchtype': 'primary-5ess',
            'layer_1_status': 'ACTIVE',
            'layer_2_status': {
                'tei': 0,
                'ces': 1,
                'sapi': 0,
                'state': 'MULTIPLE_FRAME_ESTABLISHED',
            },
            'layer_3_status': {
                'active_layer_3_calls': 0,
            },
            'active_dsl_ccbs': 0,
            'free_channel_mask': '0x80FF7FFF',
            'number_of_l2_discards': 0,
            'l2_session_id': 9,
            'total_allocated_isdn_ccbs': 0,
        }
    }
}
