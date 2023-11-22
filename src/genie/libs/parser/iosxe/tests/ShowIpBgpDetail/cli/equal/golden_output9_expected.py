expected_output = {
    'instance': {
        'default': {
            'vrf': {
                'red': {
                    'address_family': {
                        'vpnv4': {
                            'prefixes': {
                                '11.11.11.11/32': {
                                    'table_version': '37',
                                    'available_path': '1',
                                    'best_path': '1',
                                    'paths': '1 available, best #1, table red',
                                    'index': {
                                        1: {
                                            'binding_sid': {
                                                'color': '7',
                                                'sid': '18',
                                                'state': 'UP'
                                            },
                                            'next_hop': '4.4.4.4',
                                            'gateway': '7.7.7.9',
                                            'originator': '8.8.8.9',
                                            'next_hop_igp_metric': '20',
                                            'next_hop_via': 'default',
                                            'update_group': 8,
                                            'localpref': 100,
                                            'metric': 0,
                                            'origin_codes': '?',
                                            'status_codes': '*>',
                                            'refresh_epoch': 6,
                                            'route_info': '1',
                                            'imported_path_from': '1:1:11.11.11.11/32 (global)',
                                            'ext_community': 'SoO:2:2 RT:1:1 RT:1:2 RT:1:3 RT:1:4 RT:1:5 RT:1:6 RT:1:7 RT:1:8 RT:1:9 RT:1:10 RT:1:11 RT:1:12 RT:1:13 RT:1:14 RT:1:15 RT:1:16 RT:1:17 RT:1:18 RT:1:19 RT:1:20 RT:1:21 RT:1:22 RT:1:23 RT:1:24 RT:1:25 RT:1:26 RT:1:27 RT:1:28 RT:1:29 RT:1:30 RT:1:31 RT:1:32 RT:1:33 RT:1:34 RT:1:35 RT:1:36 RT:1:37 RT:1:38 RT:1:39 RT:1:40 RT:1:41 RT:1:42 RT:1:43 RT:1:44 RT:1:45 RT:1:46 RT:1:47 RT:1:48 RT:1:49 RT:1:50 RT:1:51 RT:1:52 RT:1:53 RT:1:54 RT:1:55 RT:1:56 RT:1:57 RT:1:58 RT:1:59 RT:1:60 RT:1:61 RT:1:62 RT:1:63 RT:1:64 RT:1:65 RT:1:66 RT:1:67 RT:1:68 RT:1:69 RT:1:70 RT:1:71 RT:1:72 RT:1:73 RT:1:74 RT:1:75 RT:1:76 RT:1:77 RT:1:78 RT:1:79 RT:1:80 RT:1:81 RT:1:82 RT:1:83 RT:1:84 RT:1:85 RT:1:86 RT:1:87 RT:1:88 RT:1:89 RT:1:90 RT:1:91 RT:1:92 RT:1:93 RT:1:94 RT:1:95 RT:1:96 RT:1:97 RT:1:98 RT:1:99 RT:1:100 RT:2:1 RT:2:2 RT:2:3 RT:2:4 RT:2:5 RT:2:6 RT:2:7 RT:2:8 RT:2:9 RT:2:10 RT:2:11 RT:2:12 RT:2:13 RT:2:14 RT:2:15 RT:2:16 RT:2:17 RT:2:18 RT:2:19 RT:2:20 RT:2:21 RT:2:22 RT:2:23 RT:2:24 RT:2:25 RT:2:26 RT:2:27 RT:2:28 RT:2:29 RT:2:30 RT:2:31 RT:2:32 RT:2:33 RT:2:34 RT:2:35 RT:2:36 RT:2:37 RT:2:38 RT:2:39 RT:2:40 RT:2:41 RT:2:42 RT:2:43 RT:2:44 RT:2:45 RT:2:46 RT:2:47 RT:2:48 RT:2:49 RT:2:50 RT:2:51 RT:2:52 RT:2:53 RT:2:54 RT:2:55 RT:2:56 RT:2:57 RT:2:58 RT:2:59 RT:2:60 RT:2:61 RT:2:62 RT:2:63 RT:2:64 RT:2:65 RT:2:66 RT:2:67 RT:2:68 RT:2:69 RT:2:70 RT:2:71 RT:2:72 RT:2:73 RT:2:74 RT:2:75 RT:2:76 RT:2:77 RT:2:78 RT:2:79 RT:2:80 RT:2:81 RT:2:82 RT:2:83 RT:2:84 RT:2:85 RT:2:86 RT:2:87 RT:2:88 RT:2:89 RT:2:90 RT:2:91 RT:2:92 RT:2:93 RT:2:94 RT:2:95 RT:2:96 RT:2:97 RT:2:98 RT:2:99 RT:2:100 RT:3:1 RT:3:2 RT:3:3 RT:3:4 RT:3:5 RT:3:6 RT:3:7 RT:3:8 RT:3:9 RT:3:10 RT:3:11 RT:3:12 RT:3:13 RT:3:14 RT:3:15 RT:3:16 RT:3:17 RT:3:18 RT:3:19 RT:3:20 RT:3:21 RT:3:22 RT:3:23 RT:3:24 RT:3:25 RT:3:26 RT:3:27 RT:3:28 RT:3:29 RT:3:30 RT:3:31 RT:3:32 RT:3:33 RT:3:34 RT:3:35 RT:3:36 RT:3:37 RT:3:38 RT:3:39 RT:3:40 RT:3:41 RT:3:42 RT:3:43 RT:3:44 RT:3:45 RT:3:46 RT:3:47 RT:3:48 RT:3:49 RT:3:50 RT:3:51 RT:3:52 RT:3:53 RT:3:54 RT:3:55 RT:3:56 RT:3:57 RT:3:58 RT:3:59 RT:3:60 RT:3:61 RT:3:62 RT:3:63 RT:3:64 RT:3:65 RT:3:66 RT:3:67 RT:3:68 RT:3:69 RT:3:70 RT:3:71 RT:3:72 RT:3:73 RT:3:74 RT:3:75 RT:3:76 RT:3:77 RT:3:78 RT:3:79 RT:3:80 RT:3:81 RT:3:82 RT:3:83 RT:3:84 RT:3:85 RT:3:86 RT:3:87 RT:3:88 RT:3:89 RT:3:90 RT:3:91 RT:3:92 RT:3:93 RT:3:94 RT:3:95 RT:3:96 RT:3:97 RT:3:98 RT:3:99 RT:3:100 RT:4:1 RT:4:2 RT:4:3 RT:4:4 RT:4:5 RT:4:6 RT:4:7 RT:4:8 RT:4:9 RT:4:10 RT:4:11 RT:4:12 RT:4:13 RT:4:14 RT:4:15 RT:4:16 RT:4:17 RT:4:18 RT:4:19 RT:4:20 RT:4:21 RT:4:22 RT:4:23 RT:4:24 RT:4:25 RT:4:26 RT:4:27 RT:4:28 RT:4:29 RT:4:30 RT:4:31 RT:4:32 RT:4:33 RT:4:34 RT:4:35 RT:4:36 RT:4:37 RT:4:38 RT:4:39 RT:4:40 RT:4:41 RT:4:42 RT:4:43 RT:4:44 RT:4:45 RT:4:46 RT:4:47 RT:4:48 RT:4:49 RT:4:50 RT:4:51 RT:4:52 RT:4:53 RT:4:54 RT:4:55 RT:4:56 RT:4:57 RT:4:58 RT:4:59 RT:4:60 RT:4:61 RT:4:62 RT:4:63 RT:4:64 RT:4:65 RT:4:66 RT:4:67 RT:4:68 RT:4:69 RT:4:70 RT:4:71 RT:4:72 RT:4:73 RT:4:74 RT:4:75 RT:4:76 RT:4:77 RT:4:78 RT:4:79 RT:4:80 RT:4:81 RT:4:82 RT:4:83 RT:4:84 RT:4:85 RT:4:86 RT:4:87 RT:4:88 RT:4:89 RT:4:90 RT:4:91 RT:4:92 RT:4:93 RT:4:94 RT:4:95 RT:4:96 RT:4:97 RT:4:98 RT:4:99 RT:4:100 RT:5:1 RT:5:2 RT:5:3 RT:5:4 RT:5:5 RT:5:6 RT:5:7 RT:5:8 RT:5:9 RT:5:10 RT:5:11 RT:5:12 RT:5:13 RT:5:14 RT:5:15 RT:5:16 RT:5:17 RT:5:18 RT:5:19 RT:5:20 RT:5:21 RT:5:22 RT:5:23 RT:5:24 RT:5:25 RT:5:26 RT:5:27 RT:5:28 RT:5:29 RT:5:30 RT:5:31 RT:5:32 RT:5:33 RT:5:34 RT:5:35 RT:5:36 RT:5:37 RT:5:38 RT:5:39 RT:5:40 RT:5:41 RT:5:42 RT:5:43 RT:5:44 RT:5:45 RT:5:46 RT:5:47 RT:5:48 RT:5:49 RT:5:50 Color:1 Color:2 Color:3 Color:4 Color:5 Color:6 Color:7',
                                            'cluster_list': '8.8.8.9',
                                            'mpls_labels': {
                                                'in': 'nolabel',
                                                'out': '23'
                                            },
                                            'recipient_pathid': '0',
                                            'transfer_pathid': '0x0'
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
