expected_output = {
    "LENTRY_label": {
        22: {
            "AAL": {
                "deagg_vrf_id": 0,
                "eos0": {"adj_hdl": "0x83000039", "hw_hdl": "0x7f02737c6628"},
                "eos1": {"adj_hdl": "0x3d000038", "hw_hdl": "0x7f02737c6478"},
                "id": 3724541962,
                "lbl": 22,
                "lspa_handle": "0",
            },
            "ADJ": {
                137: {
                    "IPv4": "172.16.25.2",
                    "adj": "0x63000036",
                    "ifnum": "0x36",
                    "link_type": "IP",
                    "si": "0x7f02737a2348",
                },
                139: {
                    "adj": "0x5c000037",
                    "ifnum": "0x36",
                    "link_type": "MPLS",
                    "si": "0x7f02737a2348",
                },
            },
            "EOS": {"flags": "()", "local_label": 0, "objid": 142, "pdflags": "0"},
            "LABEL": {
                141: {
                    "adj_handle": "0x3d000038",
                    "bwalk_cnt": 0,
                    "collapsed_oce": 0,
                    "flags": "0x18:(POP,PHP,)",
                    "link_type": "IP",
                    "local_adj": 0,
                    "local_label": 22,
                    "modify_cnt": 1,
                    "olbl_changed": 0,
                    "outlabel": "(3, 0)",
                    "pdflags": "0:(INSTALL_HW_OK,)",
                    "subwalk_cnt": 0,
                    "unsupported_recursion": 0,
                },
                143: {
                    "adj_handle": "0x83000039",
                    "bwalk_cnt": 0,
                    "collapsed_oce": 0,
                    "flags": "0x18:(POP,PHP,)",
                    "link_type": "MPLS",
                    "local_adj": 0,
                    "local_label": 22,
                    "modify_cnt": 0,
                    "olbl_changed": 0,
                    "outlabel": "(3, 0)",
                    "pdflags": "0:(INSTALL_HW_OK,)",
                    "subwalk_cnt": 0,
                    "unsupported_recursion": 0,
                },
            },
            "backwalk_cnt": 2,
            "label": 22,
            "lentry_hdl": "0xde00000a",
            "modify_cnt": 1,
            "nobj": "(EOS, 142)",
        }
    }
}
