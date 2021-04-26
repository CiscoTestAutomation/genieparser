expected_output = {
        "vrf": {
            'default': {  # VRF information, if no, assign "default"
                "address_family": {
                    'ipv4': {  # IPv4 as initial value
                        "instance": {
                            'mpls1': {  # here is ospf name
                                "interfaces": {
                                    'Loopback0': {
                                        "name": 'Loopback0',
                                        "enable": True,
                                        "line_protocol": True,
                                        "ip_address": '25.97.1.1/32',
                                        "demand_circuit": False,
                                        "process_id": 'mpls1',
                                        "router_id": '25.97.1.1',
                                        "interface_type": 'LOOPBACK',
                                        "area": '0',
                                        "bfd": {
                                            "enable": False,
                                        },
                                        "label_stack": {
                                            "primary_label": '0',
                                            "backup_label": '0',
                                            "srte_label": '0',
                                        },
                                        "sid": '0',
                                        "strict_spf_sid": '0',
                                        "cost": 1,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }