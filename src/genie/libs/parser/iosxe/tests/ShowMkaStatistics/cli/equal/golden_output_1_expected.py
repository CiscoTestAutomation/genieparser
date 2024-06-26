expected_output = {
    "mka-session-totals": {
        "secured": 2,
        "fallback-secured": 0,
        "reauthentication-attempts": 0,
        "deleted-secured": 0,
        "keepalive-timeouts": 0
    },
    "ca-statistics": {
        "pairwise-caks-derived": 0,
        "pairwaise-cak-rekeys": 0,
        "group-caks-generated": 0,
        "group-caks-received": 0
    },
    "sa-statistics": {
        "saks-generated": 1,
        "saks-rekeyed": 0,
        "saks-received": 1,
        "sak-responses-received": 1
    },
    "mkpdu-statistics": {
        "mkpdu-received": {
            "distributed-sak": 1,
            "distributed-cak": 0
        },
        "mkpdus-validated-received": 501325,
        "mkpdu-transmitted": {
            "distributed-sak": 1,
            "distributed-cak": 0
        },
        "mkpdus-transmitted": 543079
    },
    "mka-error-counters": {
        "session-failures": {
            "bringup-failures": 0,
            "reauthentication-failures": 0,
            "duplicate-auth-mgr-handle": 0
        },
        "sak-failures": {
            "sak-generation": 0,
            "hash-key-generation": 0,
            "sak-encryption-wrap": 0,
            "sak-decryption-unwrap": 0,
            "sak-cipher-mismatch": 0
        },
        "ca-failures": {
            "group-sak-generation": 0,
            "group-cak-encryption-wrap": 0,
            "group-cak-decryption-unwrap": 0,
            "pairwise-cak-derivation": 0,
            "ckn-derivation": 0,
            "ick-derivation": 0,
            "kek-derivation": 0,
            "invalid-peer-macsec-capability": 0
        },
        "macsec-failures": {
            "rx-sc-creation": 0,
            "tx-sc-creation": 0,
            "rx-sa-installation": 0,
            "tx-sa-installation": 0
        }
    }
}
