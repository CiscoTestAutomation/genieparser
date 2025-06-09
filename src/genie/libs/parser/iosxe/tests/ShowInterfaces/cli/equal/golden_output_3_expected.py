expected_output = {
    "Ucse1/0/1": {
        "port_channel": {
            "port_channel_member": False
        },
        "is_deleted": False,
        "enabled": False,
        "line_protocol": "down",
        "oper_status": "down",
        "type": "UCS-E160S-M3/K9",
        "mac_address": "0045.1d12.d8b1",
        "phys_address": "0045.1d12.d8b1",
        "delay": 10,
        "mtu": 1500,
        "bandwidth": 1000000,
        "reliability": "255/255",
        "txload": "1/255",
        "rxload": "1/255",
        "encapsulations": {
            "encapsulation": "arpa"
        },
        "duplex_mode": "full",
        "port_speed": "1000mbps",
        "link_type": "force-up",
        "auto_negotiate": False,
        "media_type": "Internal",
        "flow_control": {
            "receive": False,
            "send": False
        },
        "arp_type": "arpa",
        "arp_timeout": "04:00:00",
        "last_input": "never",
        "last_output": "never",
        "output_hang": "never",
        "queues": {
            "input_queue_size": 0,
            "input_queue_max": 375,
            "input_queue_drops": 0,
            "input_queue_flushes": 0,
            "total_output_drop": 0,
            "queue_strategy": "fifo",
            "output_queue_size": 0,
            "output_queue_max": 40
        },
        "counters": {
            "rate": {
                "load_interval": 300,
                "in_rate": 0,
                "in_rate_pkts": 0,
                "out_rate": 0,
                "out_rate_pkts": 0
            },
            "last_clear": "never",
            "in_pkts": 0,
            "in_octets": 0,
            "in_no_buffer": 0,
            "in_multicast_pkts": 0,
            "in_broadcast_pkts": 0,
            "in_runts": 0,
            "in_giants": 0,
            "in_throttles": 0,
            "in_errors": 0,
            "in_crc_errors": 0,
            "in_frame": 0,
            "in_overrun": 0,
            "in_ignored": 0,
            "in_watchdog": 0,
            "in_mac_pause_frames": 0,
            "out_pkts": 0,
            "out_octets": 0,
            "out_underruns": 0,
            "out_broadcast_pkts": 0,
            "out_multicast_pkts": 0,
            "out_errors": 0,
            "out_interface_resets": 1,
            "out_collision": 0,
            "out_unknown_protocl_drops": 0,
            "out_babble": 0,
            "out_late_collision": 0,
            "out_deferred": 0,
            "out_lost_carrier": 0,
            "out_no_carrier": 0,
            "out_mac_pause_frames": 0,
            "out_buffer_failure": 0,
            "out_buffers_swapped": 0
        }
    },
    "Pseudowire1": {
        "port_channel": {
            "port_channel_member": False
        },
        "is_deleted": False,
        "enabled": True,
        "description": "pseudowire to core router",
        "mtu": 9198,
        "bandwidth": "not configured",
        "encapsulations": {
            "encapsulation": "mpls"
        },
        "peer_ip": "192.0.2.3",
        "vc_id": 1,
        "counters": {
            "in_pkts": 0,
            "in_octets": 0,
            "in_drops": 0,
            "out_pkts": 0,
            "out_octets": 0,
            "out_drops": 0
        }
    }
}
