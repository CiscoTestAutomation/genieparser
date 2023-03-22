

expected_output = {
    'instance': {
        'default': {
            'vrf': {
                'default': {
                    'vrf_name_out': 'default',
                    'vrf_router_id': '192.168.4.11',
                    'vrf_local_as': 100,
                    'address_family': {
                        'l2vpn evpn': {
                            'tableversion': 155,
                            'configuredpeers': 2,
                            'capablepeers': 2,
                            'totalnetworks': 32,
                            'totalpaths': 32,
                            'memoryused': 5708,
                            'numberattrs': 20,
                            'bytesattrs': 3200,
                            'numberpaths': 0,
                            'bytespaths': 0,
                            'numbercommunities': 1,
                            'bytescommunities': 32,
                            'numberclusterlist': 3,
                            'bytesclusterlist': 12,
                            'dampening': 'disabled',
                            'neighbor': {
                                '172.16.205.8': {
                                    'neighbor': '172.16.205.8',
                                    'version': 4,
                                    'msgrecvd': 130,
                                    'msgsent': 139,
                                    'neighbortableversion': 155,
                                    'inq': 0,
                                    'outq': 0,
                                    'remoteas': 200,
                                    'time': '02:05:01',
                                    'state': 'established',
                                    'prefixreceived': 0,
                                },
                                '192.168.234.1':{
                                    'neighbor': '192.168.234.1',
                                    'version': 4,
                                    'msgrecvd': 182,
                                    'msgsent': 128,
                                    'neighbortableversion': 155,
                                    'inq': 0,
                                    'outq': 0,
                                    'remoteas': 100,
                                    'time': '01:42:47',
                                    'state': 'established',
                                    'prefixreceived': 12,
                                },
                                '90:90:90::3': {
                                    'neighbor': '90:90:90::3',
                                    'version': 4,
                                    'msgrecvd': 200,
                                    'msgsent': 300,
                                    'neighbortableversion': 400,
                                    'inq': 0,
                                    'outq': 0,
                                    'remoteas': 500,
                                    'time': '03:52:17',
                                    'state': 'established',
                                    'prefixreceived': 1200,
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
