expected_output = {
    "session": {
        "session_number": 2,
        "type": "erspan-source",
        "mode": "extended",
        "ssn_direction": "both",
        "state": "up",
        "erspan_id": 1,
        "vrf_name": "default",
        "acl_name": "acl-name not specified",
        "ip_ttl": 255,
        "ip_dscp": 0,
        "destination_ip": "9.1.1.2",
        "origin_ip": "5.5.5.5 (global)",
        "src_intf_all": "both",
        "filter_vlans": 100,
        "trace_route": False,
        "eth_type": "0x800",
        "frame_type": "IPv4",
        "dest_ip": "10.10.100.11/32",
        "src_ip": "10.10.100.21/32",
        "feature": {
            "mtu_trunc": {
                "enabled": "No"
            },
            "rate_limit_rx": {
                "enabled": "No"
            },
            "rate_limit_tx": {
                "enabled": "No"
            },
            "sampling": {
                "enabled": "No"
            },
            "mcbe": {
                "enabled": "No"
            },
            "l3_tx": {
                "enabled": "-",
                "modules_supported": [
                    1,
                    3,
                    4,
                    9
                ]
            },
            "erspan_acl": {
                "enabled": "-",
                "modules_not_supported": [
                    1,
                    3,
                    4,
                    9
                ]
            },
            "erspan_v2": {
                "enabled": "Yes",
                "modules_supported": [
                    1,
                    3,
                    4,
                    9
                ]
            },
            "simpl rb span": {
                "enabled": "Yes",
                "modules_supported": [
                    1,
                    3,
                    4,
                    9
                ]
            },
            "extended_ssn": {
                "enabled": "Yes",
                "modules_supported": [
                    1,
                    3,
                    4,
                    9
                ]
            }
        },
        "legend": {
            "mcbe": "Multicast Best Effort",
            "l3_tx": "L3 Multicast Egress SPAN",
            "exsp_x": "L3, FP, or misc"
        }
    }
}
