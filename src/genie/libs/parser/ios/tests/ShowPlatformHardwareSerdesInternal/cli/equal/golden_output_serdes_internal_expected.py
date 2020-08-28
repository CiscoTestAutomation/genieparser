expected_output = {
    "link": {
        "Encryption Processor": {
            "errors": {
                "rx_parity": 0,
                "rx_process": 0,
                "rx_schedule": 0,
                "rx_statistics": 0,
                "tx_process": 0,
                "tx_schedule": 0,
                "tx_statistics": 0,
            },
            "from": {
                "bytes": {"dropped": 0, "errored": 0, "total": 0},
                "pkts": {"dropped": 0, "errored": 0, "total": 0},
            },
            "local_rx_in_sync": True,
            "local_tx_in_sync": True,
            "remote_rx_in_sync": True,
            "remote_tx_in_sync": True,
            "to": {
                "bytes": {"dropped": 0, "total": 0},
                "pkts": {"dropped": 0, "total": 0},
            },
        },
        "Network-Processor-0": {
            "from": {"bytes": {"total": 7397920802}, "pkts": {"total": 21259012}},
            "local_rx_in_sync": True,
            "local_tx_in_sync": True,
            "to": {"bytes": {"total": 7343838083}, "pkts": {"total": 21763844}},
        },
    },
    "serdes_exception_counts": {
        "c2w": {},
        "cfg": {},
        "cilink": {
            "link": {
                "0": {"chicoEvent": 5, "msgEccError": 5, "msgTypeError": 5},
                "1": {"chicoEvent": 1, "msgEccError": 1, "msgTypeError": 1},
                "2": {"chicoEvent": 3, "msgEccError": 3, "msgTypeError": 3},
            }
        },
        "edh-hi": {},
        "edh-lo": {},
        "edm": {},
        "eqs/fc": {},
        "idh-hi": {},
        "idh-lo": {},
        "idh-shared": {},
        "ilak": {},
        "isch": {},
        "pcie": {},
        "slb": {},
        "spi link": {},
    },
}
