expected_output = {
    "LENTRY_label": {
        18: {
            "AAL": {
                "deagg_vrf_id": 0,
                "eos0": {"adj_hdl": "0x76000024", "hw_hdl": "0x7ff7911bf758"},
                "eos1": {"adj_hdl": "0xeb000022", "hw_hdl": "0x7ff7911bf548"},
                "id": 318767109,
                "lbl": 18,
                "lspa_handle": "0",
            },
            "ADJ": {
                69: {
                    "IPv4": "93.1.1.11",
                    "adj": "0xa000001f",
                    "ifnum": "0x7c",
                    "link_type": "IP",
                    "si": "0x7ff791190278",
                },
                71: {
                    "adj": "0x53000020",
                    "ifnum": "0x7c",
                    "link_type": "MPLS",
                    "si": "0x7ff791190278",
                },
            },
            "EOS": {"flags": "()", "local_label": 0, "objid": 76, "pdflags": "0"},
            "LABEL": {
                75: {
                    "adj_handle": "0xeb000022",
                    "bwalk_cnt": 0,
                    "collapsed_oce": 0,
                    "flags": ":(POP,PHP,)",
                    "link_type": "IP",
                    "local_adj": 0,
                    "local_label": 18,
                    "modify_cnt": 1,
                    "olbl_changed": 0,
                    "outlabel": "(3, 0)",
                    "pdflags": ":(INSTALL_HW_OK,)",
                    "subwalk_cnt": 0,
                    "unsupported_recursion": 0,
                },
                78: {
                    "adj_handle": "0x76000024",
                    "bwalk_cnt": 0,
                    "collapsed_oce": 0,
                    "flags": ":(POP,PHP,)",
                    "link_type": "MPLS",
                    "local_adj": 0,
                    "local_label": 18,
                    "modify_cnt": 0,
                    "olbl_changed": 0,
                    "outlabel": "(3, 0)",
                    "pdflags": ":(INSTALL_HW_OK,)",
                    "subwalk_cnt": 0,
                    "unsupported_recursion": 0,
                },
            },
            "backwalk_cnt": 2,
            "label": 18,
            "lentry_hdl": "0x13000005",
            "modify_cnt": 1,
            "nobj": "(EOS, 76)",
        }
    }
}
