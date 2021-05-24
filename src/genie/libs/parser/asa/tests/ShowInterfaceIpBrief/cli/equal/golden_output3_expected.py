expected_output = {
    "interfaces": {
        "Control0/0": {
            "ipv4": {"127.0.1.1": {"ip": "127.0.1.1"}},
            "check": "YES",
            "method": "CONFIG",
            "link_status": "up",
            "line_protocol": "up",
        },
        "GigabitEthernet0/0": {
            "ipv4": {"192.168.16.226": {"ip": "192.168.16.226"}},
            "check": "YES",
            "method": "CONFIG",
            "link_status": "up",
            "line_protocol": "up",
        },
        "GigabitEthernet0/1": {
            "ipv4": {"unnumbered": {"unnumbered_intf_ref": "unassigned"}},
            "check": "YES",
            "method": "unset",
            "link_status": "admin down",
            "line_protocol": "down",
        },
        "GigabitEthernet0/2": {
            "ipv4": {"10.1.1.50": {"ip": "10.1.1.50"}},
            "check": "YES",
            "method": "manual",
            "link_status": "admin down",
            "line_protocol": "down",
        },
        "GigabitEthernet0/3": {
            "ipv4": {"192.168.2.6": {"ip": "192.168.2.6"}},
            "check": "YES",
            "method": "DHCP",
            "link_status": "admin down",
            "line_protocol": "down",
        },
        "Management0/0": {
            "ipv4": {"192.168.145.3": {"ip": "192.168.145.3"}},
            "check": "YES",
            "method": "CONFIG",
            "link_status": "up",
        },
    }
}
