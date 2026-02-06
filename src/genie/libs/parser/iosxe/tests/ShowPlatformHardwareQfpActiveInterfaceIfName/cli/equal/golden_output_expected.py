expected_output = {
    'interface': {
        'Port-channel1': {
            'channel': 115,
            'interface_state': 'VALID',
            'members': ['TenGigabitEthernet3/1/0', 'TenGigabitEthernet3/1/1', 'ethernet', 'IFM'],
            'platform_interface_handle': 66,
            'protocols': {
                'ess_ac_input': {
                    'cp_handle': '0x621c7d7ec998',
                    'dp_handle': '0x40e1bb00',
                    'features': ['PPPOE_GET_SESSION', 'ESS_ENTER_SWITCHING', 'PPPOE_HANDLE_UNCLASSIFIED_SESSION', 'DEF_IF_DROP_FIA'],
                },
                'layer2_input': {
                    'cp_handle': '0x621c7d7ed9d8',
                    'dp_handle': '0x40e00100',
                    'features': ['LAYER2_INPUT_SIA', 'LAYER2_INPUT_LOOKUP_PROCESS', 'LAYER2_INPUT_GOTO_OUTPUT_FEATURE'],
                },
                'layer2_output': {
                    'cp_handle': '0x621c7d7ec858',
                    'dp_handle': '0x40e1dd00',
                    'features': ['OUTPUT_ETHER_CHNL_L2_BUNDLE_PRE_ENQ', 'LAYER2_OUTPUT_DROP_POLICY', 'LAYER2_OUTPUT_ETHER_CHANNEL_BUNDLE_ENQ', 'DEF_IF_DROP_FIA'],
                },
            },
            'qfp_interface_handle': 73,
            'rx_uidb': 262130,
            'tx_uidb': 262071,
        },
    },
}
