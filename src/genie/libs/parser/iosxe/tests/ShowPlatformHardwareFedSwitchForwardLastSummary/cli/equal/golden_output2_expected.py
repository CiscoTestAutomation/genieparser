expected_output = {
    "input_packet": {
        "ethernet": {
            "dst": "6c:8b:d3:69:14:bf",
            "src": "f8:b7:e2:4e:cd:ea",
            "type": "0x8100"
        },
        "dot1q": {
            "prio": 0,
            "id": 0,
            "vlan": 239,
            "type": "0x800"
        },
        "ip": {
            "version": 4,
            "ihl": 5,
            "tos": "0x0",
            "len": 100,
            "id": 12224,
            "flags": "",
            "frag": 0,
            "ttl": 254,
            "proto": "icmp",
            "chksum": "0xc20d",
            "src": "100.1.1.1",
            "dst": "100.1.1.200",
            "options": ""
        },
        "icmp": {
            "type": "echo-request",
            "code": 0,
            "chksum": "0xcccd",
            "id": "0x12",
            "seq": "0xbfa"
        },
        "raw": {
            "load": "00 00 00 00 3E E8 66 88 AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD AB CD"
        }
    },
    "ingress": {
        "port": "TwentyFiveGigE1/0/24",
        "global_port_number": 24,
        "local_port_number": 24,
        "asic_port_number": 15,
        "asic_instance": 1,
        "vlan": 239,
        "mapped_vlan_id": 254,
        "stp_instance": 253,
        "block_forward": 0,
        "block_learn": 0,
        "l3_interface": {
            "id": 38,
            "ipv4_routing": "enabled",
            "ipv6_routing": "enabled",
            "vrf_id": 0
        },
        "adjacency": {
            "station_index": "117    [SI_CPUQ_FORUS_TRAFFIC]",
            "destination_index": 24120,
            "rewrite_index": 1,
            "replication_bit_map": "0x8    ['coreCpu']"
        }
    },
    "decision": {
        "destination_index": "24120  [DI_CPUQ_FORUS_TRAFFIC]",
        "rewrite_index": "1      [RI_CPU]",
        "dest_mod_index": "0      [IGR_FIXED_DMI_NULL_VALUE]",
        "cpu_map_index": "0      [CMI_NULL]",
        "forwarding_mode": "3      [Other or Tunnel]",
        "replication_bit_map": [
            "coreCpu"
        ],
        "winner": "L3FWDIPV4 LOOKUP",
        "qos_label": 1,
        "sgt": 0,
        "dgtid": 0
    }
}