expected_output = {
    "GigabitEthernet0/0/0": {
        "port_channel": {
            "port_channel_member": False
        },
        "is_deleted": False,
        "enabled": True,
        "line_protocol": "up",
        "oper_status": "up",
        "type": "BUILT-IN-2T+6X1GE",
        "mac_address": "cc16.7e85.0e02",
        "phys_address": "cc16.7e85.0e02",
        "ipv4": {
            "152.22.242.102/26": {
                "ip": "152.22.242.102",
                "prefix_length": "26"
            }
        },
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
        "link_type": "auto",
        "auto_negotiate": True,
        "media_type": "T",
        "flow_control": {
            "receive": True,
            "send": True
        },
        "arp_type": "arpa",
        "arp_timeout": "04:00:00",
        "last_input": "00:00:00",
        "last_output": "00:00:02",
        "output_hang": "never",
        "queues": {
            "input_queue_size": 0,
            "input_queue_max": 375,
            "input_queue_drops": 0,
            "input_queue_flushes": 0,
            "total_output_drop": 128035,
            "queue_strategy": "Class-based",
            "output_queue_size": 0,
            "output_queue_max": 40
        },
        "counters": {
            "rate": {
                "load_interval": 30,
                "in_rate": 28000,
                "in_rate_pkts": 29,
                "out_rate": 50000,
                "out_rate_pkts": 17
            },
            "last_clear": "never",
            "in_pkts": 11059827,
            "in_octets": 1600856154,
            "in_no_buffer": 0,
            "in_multicast_pkts": 232903,
            "in_broadcast_pkts": 5157390,
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
            "out_pkts": 7598063,
            "out_octets": 2854756614,
            "out_underruns": 0,
            "out_broadcast_pkts": 1297,
            "out_multicast_pkts": 0,
            "out_errors": 0,
            "out_interface_resets": 2,
            "out_collision": 0,
            "out_unknown_protocl_drops": 556,
            "out_babble": 0,
            "out_late_collision": 0,
            "out_deferred": 0,
            "out_lost_carrier": 0,
            "out_no_carrier": 0,
            "out_mac_pause_frames": 0,
            "out_buffer_failure": 0,
            "out_buffers_swapped": 0
        },
        "carrier_transitions": 3
    }
}
