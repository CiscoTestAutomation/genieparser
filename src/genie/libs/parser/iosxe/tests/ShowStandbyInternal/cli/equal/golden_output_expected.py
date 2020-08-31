expected_output = {
    "hsrp_common_process_state": "not running",
    "hsrp_ha_state": "capable",
    "hsrp_ipv4_process_state": "not running",
    "hsrp_ipv6_process_state": "not running",
    "hsrp_timer_wheel_state": "running",
    "mac_address_table": {
        166: {"group": 10, "interface": "gi2/0/3", "mac_address": "0000.0cff.b311"},
        169: {"group": 5, "interface": "gi1/0/1", "mac_address": "0000.0cff.b30c"},
        172: {"group": 0, "interface": "gi2/0/3", "mac_address": "0000.0cff.b307"},
        173: {"group": 1, "interface": "gi2/0/3", "mac_address": "0000.0cff.b308"},
    },
    "msgQ_max_size": 0,
    "msgQ_size": 0,
    "v3_to_v4_transform": "disabled",
    "virtual_ip_hash_table": {
        "ipv6": {78: {"group": 20, "interface": "gi1", "ip": "2001:DB8:10:1:1::254"}},
        "ipv4": {
            103: {"group": 0, "interface": "gi1/0/1", "ip": "192.168.1.254"},
            106: {"group": 10, "interface": "gi1/0/2", "ip": "192.168.2.254"},
        },
    },
}
