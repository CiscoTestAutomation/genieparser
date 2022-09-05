expected_output = {
    'drops': {
        'IN_V4_PKT_HIT_INVALID_SA': {
            'drop_type': 1,
            'packets': 0
        },
        'IN_CLEAR_US_V4_PSTATE_SB_FAILED': {
            'drop_type': 2,
            'packets': 0
        },
        'IN_US_V4_PKT_FOUND_IPSEC_NOT_ENABLED': {
            'drop_type': 3,
            'packets': 0
        },
        'IN_US_V4_PKT_SA_NOT_FOUND_SPI': {
            'drop_type': 4,
            'packets': 0
        },
        'IN_TUNNEL_US_V4_PKT_IPSEC_NO_KEEP': {
            'drop_type': 5,
            'packets': 1
        },
        'IN_TRANS_CL_V4_PKT_FAILED_POLICY': {
            'drop_type': 6,
            'packets': 0
        },
        'IN_TRANS_V4_IPSEC_PKT_NOT_FOUND_SPI': {
            'drop_type': 7,
            'packets': 0
        },
        'IN_US_CL_V4_PKT_FAILED_POLICY': {
            'drop_type': 8,
            'packets': 0
        },
        'IN_V6_PKT_HIT_INVALID_SA': {
            'drop_type': 9,
            'packets': 0
        },
        'IN_CLEAR_US_V6_PSTATE_SB_FAILED': {
            'drop_type': 10,
            'packets': 0
        },
        'IN_US_V6_PKT_FOUND_IPSEC_NOT_ENABLED': {
            'drop_type': 11,
            'packets': 0
        },
        'IN_US_V6_PKT_SA_NOT_FOUND_SPI': {
            'drop_type': 12,
            'packets': 0
        },
        'IN_TUNNEL_US_V6_PKT_IPSEC_NOT_KEEP': {
            'drop_type': 13,
            'packets': 0
        },
        'IN_TRANS_V6_PKT_FAILED_POLICY': {
            'drop_type': 14,
            'packets': 0
        },
        'IN_US_CL_V6_PKT_FAILED_POLICY': {
            'drop_type': 15,
            'packets': 0
        },
        'IN_CPP_FAIL_NOTIF_SA_SOFT_EXPIRY': {
            'drop_type': 17,
            'packets': 0
        },
        'IN_CD_SW_IPSEC_HARD_EXPIRY': {
            'drop_type': 18,
            'packets': 0
        },
        'IN_CD_SW_IPSEC_ANTI_REPLAY_FAIL': {
            'drop_type': 19,
            'packets': 0
        },
        'IN_UNEXP_CD_SW_IPSEC_EXCEPTION': {
            'drop_type': 20,
            'packets': 0
        },
        'IN_TBASED_ANTI_REPLAY_FAIL': {
            'drop_type': 21,
            'packets': 0
        },
        'IN_PKT_HEADPAD_LEN_ERR': {
            'drop_type': 23,
            'packets': 0
        },
        'IN_PKT_PSTATE_TOO_BIG': {
            'drop_type': 24,
            'packets': 0
        },
        'IN_INFRA_V4_PKT_LEN_TOO_BIG': {
            'drop_type': 25,
            'packets': 0
        },
        'IN_INFRA_V6_PKT_LEN_TOO_BIG': {
            'drop_type': 26,
            'packets': 0
        },
        'IN_PSTATE_CHUNK_MEM_NOT_INIT': {
            'drop_type': 27,
            'packets': 0
        },
        'IN_PSTATE_CHUNK_ALLOC_FAIL': {
            'drop_type': 28,
            'packets': 0
        },
        'IN_SETTING_WRONG_L2_HDR': {
            'drop_type': 29,
            'packets': 0
        },
        'IN_V4_POST_INPUT_POLICY_FAIL': {
            'drop_type': 30,
            'packets': 0
        },
        'IN_V6_POST_INPUT_POLICY_FAIL': {
            'drop_type': 31,
            'packets': 0
        },
        'OUT_V4_PKT_HIT_INVALID_SA': {
            'drop_type': 32,
            'packets': 0
        },
        'OUT_V4_PKT_HIT_IKE_START_SP': {
            'drop_type': 33,
            'packets': 0
        },
        'OUT_V4_PKT_HIT_TED_START_SP': {
            'drop_type': 34,
            'packets': 0
        },
        'OUT_V4_PKT_HIT_DENY_DROP_SP': {
            'drop_type': 35,
            'packets': 0
        },
        'OUT_V4_PKT_HIT_UNKNOWN_TCAM': {
            'drop_type': 36,
            'packets': 0
        },
        'OUT_V6_PKT_HIT_INVALID_SA': {
            'drop_type': 37,
            'packets': 0
        },
        'OUT_V6_PKT_HIT_IKE_START_SP': {
            'drop_type': 38,
            'packets': 0
        },
        'OUT_V6_PKT_HIT_TED_START_SP': {
            'drop_type': 39,
            'packets': 0
        },
        'OUT_V6_PKT_HIT_DENY_DROP_SP': {
            'drop_type': 40,
            'packets': 0
        },
        'OUT_V6_PKT_HIT_UNKNOWN_TCAM': {
            'drop_type': 41,
            'packets': 0
        },
        'OUT_CPP_FAIL_NOTIF_SA_SOFT_EXPIRY': {
            'drop_type': 43,
            'packets': 0
        },
        'OUT_CD_SW_IPSEC_HARD_EXPIRY': {
            'drop_type': 44,
            'packets': 0
        },
        'OUT_UNEXP_CD_SW_IPSEC_EXCEPTION': {
            'drop_type': 45,
            'packets': 0
        },
        'OUT_CD_SW_IPSEC_DETECT_SEQ_OVEFLOW': {
            'drop_type': 46,
            'packets': 0
        },
        'OUT_CANNOT_FRAG_DF_SET_PKT': {
            'drop_type': 48,
            'packets': 0
        },
        'OUT_PKT_HEADPAD_LEN_ERR': {
            'drop_type': 49,
            'packets': 0
        },
        'OUT_PKT_PSTATE_TOO_BIG': {
            'drop_type': 50,
            'packets': 0
        },
        'OUT_INFRA_V4_PKT_LEN_TOO_BIG': {
            'drop_type': 51,
            'packets': 0
        },
        'OUT_INFRA_V6_PKT_LEN_TOO_BIG': {
            'drop_type': 52,
            'packets': 0
        },
        'OUT_PSTATE_CHUNK_MEM_NOT_INIT': {
            'drop_type': 53,
            'packets': 0
        },
        'OUT_PSTATE_CHUNK_ALLOC_FAIL': {
            'drop_type': 54,
            'packets': 0
        },
        'OUT_SETTING_WRONG_L2_HDR': {
            'drop_type': 55,
            'packets': 0
        },
        'OUT_V4_POST_OUTPUT_POLICY_FAIL': {
            'drop_type': 56,
            'packets': 0
        },
        'OUT_V6_POST_OUTPUT_POLICY_FAIL': {
            'drop_type': 57,
            'packets': 0
        },
        'MPASS_RESTORE_FAIL': {
            'drop_type': 59,
            'packets': 0
        },
        'CRYPTO_DEVICE_IPSEC_STOP': {
            'drop_type': 60,
            'packets': 0
        },
        'OUT_V4_TX_PKT_ADJ_FAIL': {
            'drop_type': 61,
            'packets': 0
        },
        'IN_CD_SW_IPSEC_MAC_EXCEPTION': {
            'drop_type': 62,
            'packets': 0
        },
        'IN_NAT_DEMUX_FAIL': {
            'drop_type': 63,
            'packets': 0
        },
        'OUT_NAT_DEMUX_FAIL': {
            'drop_type': 64,
            'packets': 0
        },
        'IN_CD_SW_IPSEC_NH_MISMATCH': {
            'drop_type': 65,
            'packets': 0
        },
        'CD_SW_IPSEC_PKT_HIT_INVALID_SA': {
            'drop_type': 68,
            'packets': 0
        },
        'IN_PKT_MDATA_ERR': {
            'drop_type': 69,
            'packets': 0
        },
        'IN_V4_PKT_FRAG_ERR': {
            'drop_type': 70,
            'packets': 0
        },
        'IN_PKT_IPVER_INVALID': {
            'drop_type': 89,
            'packets': 0
        },
        'IN_PKT_CERM_DROP': {
            'drop_type': 108,
            'packets': 0
        },
        'OUT_PKT_CERM_DROP': {
            'drop_type': 109,
            'packets': 0
        },
        'PKT_BUFFER_UNAVAILABLE': {
            'drop_type': 110,
            'packets': 0
        },
        'OUT_IPV4_SA_NOT_FOUND': {
            'drop_type': 111,
            'packets': 0
        },
        'OUT_IPV6_SA_NOT_FOUND': {
            'drop_type': 112,
            'packets': 0
        },
        'IN_IPD3P_ANTI_REPLAY_FAIL': {
            'drop_type': 113,
            'packets': 0
        },
        'IN_CRYPTO_THRPUT_POLICY_DROP': {
            'drop_type': 114,
            'packets': 0
        },
        'OUT_CRYPTO_THRPUT_POLICY_DROP': {
            'drop_type': 115,
            'packets': 0
        },
        'CD_IN_PKT_OUT_OF_WINDOW': {
            'drop_type': 116,
            'packets': 0
        }
    }
}
