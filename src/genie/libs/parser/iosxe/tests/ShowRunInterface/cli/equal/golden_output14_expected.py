expected_output= {
    "interfaces": {
        "nve1": {
            "member_vni": {
                "20011": {
                    "ingress_replication": {
                        'enabled': True,
                        'remote_peer_ip': '1.1.1.1'
                    }
                },
                "20012": {
                    "ingress_replication": {
                        'enabled': True,
                        'remote_peer_ip': '1.1.1.2'
                    }
                },
                "20013": {
                    "mcast_group": "239.1.1.3"
                },
                "20014": {
                    "mcast_group": "239.1.1.4"
                },
            },
            "source_interface": "Loopback1"
        },
    }
}
