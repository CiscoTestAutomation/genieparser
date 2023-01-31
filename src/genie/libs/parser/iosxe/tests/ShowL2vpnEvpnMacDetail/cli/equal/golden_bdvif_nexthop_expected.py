# Copyright (c) 2022 by Cisco Systems, Inc.
# All rights reserved.

expected_output={
    "evi": {
        11011: {
            "bd_id": {
                11011: {
                    "eth_tag": {
                        0: {
                            "mac_addr": {
                                "0000.0115.1112": {
                                    "sticky": False,
                                    "stale": False,
                                    "esi": "0000.0000.0000.0000.0000",
                                    "next_hops": [
                                        "V:11011 BD-VIF1500111"
                                    ],
                                    "seq_number": 0,
                                    "mac_only_present": False,
                                    "mac_dup_detection": {
                                        "status": "Timer not running"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
