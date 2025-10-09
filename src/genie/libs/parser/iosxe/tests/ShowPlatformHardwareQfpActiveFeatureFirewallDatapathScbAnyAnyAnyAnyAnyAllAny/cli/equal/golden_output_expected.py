expected_output = {
    "sessions": {
        "00000004": {
            "src_ip": "192.168.32.1",
            "src_port": 11001,
            "dst_ip": "192.168.132.1",
            "dst_port": 0,
            "protocol": "6",
            "protocol_desc": "tcp",
            "flags": "sc"
        },
        "00000002": {
            "src_ip": "192.168.32.1",
            "src_port": 11001,
            "dst_ip": "192.168.132.1",
            "dst_port": 21,
            "protocol": "6",
            "protocol_desc": "ftp",
            "flags": "sc"
        },
        "00000003": {
            "src_ip": "192.168.32.1",
            "src_port": 0,
            "dst_ip": "192.168.132.1",
            "dst_port": 41902,
            "protocol": "6",
            "protocol_desc": "ftp data",
            "flags": "id"
        },
        "00000000": {
            "src_ip": "10.1.1.1",
            "src_port": 10001,
            "dst_ip": "20.1.1.1",
            "dst_port": 20001,
            "protocol": "17",
            "protocol_desc": "udp",
            "flags": "sc"
        },
        "00000001": {
            "src_ip": "10.1.1.2",
            "src_port": 10001,
            "dst_ip": "20.1.1.2",
            "dst_port": 20001,
            "protocol": "17",
            "protocol_desc": "udp",
            "flags": "sc"
        }
    }
}
