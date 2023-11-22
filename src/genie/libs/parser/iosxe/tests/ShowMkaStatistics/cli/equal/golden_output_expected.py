expected_output = {
    "mka-session-totals": {
        "secured": 3,
        "fallback-secured": 2,
        "reauthentication-attempts": 4,
        "deleted-secured": 2,
        "keepalive-timeouts": 0
    },
    "ca-statistics": {
        "pairwise-caks-derived": 4,
        "pairwaise-cak-rekeys": 4,
        "group-caks-generated": 0,
        "group-caks-received": 0
    },
    "sa-statistics": {
        "saks-generated": 0,
        "saks-rekeyed": 1479,
        "saks-received": 1480,
        "sak-responses-received": 0
    },
    "mkpdu-statistics": {
        "mkpdu-received": {
            "distributed-sak": 1480,
            "distributed-cak": 0
        },
        "mkpdus-validated-received": 44937,
        "mkpdu-transmitted": {
            "distributed-sak": 0,
            "distributed-cak": 0
        },
        "mkpdus-transmitted": 91067
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
        },
        "mkpdu-failures": {
            "mkpdu_tx": 0,
            "mkpdu-rx-icv-verification": 44647,
            "mkpdu-rx-fallback-icv-ver": 0,
            "mkpdu-rx-validation": 0,
            "mkpdu-rx-bad-peer-mn": 0,
            "mkpdu-rx-nonrecent-peerlist-mn": 0
        }
    }
}