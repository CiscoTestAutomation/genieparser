expected_output = {
        "data_policy_filter": {
            'DP_HUB_LOCAL_FROM_TUNNEL': {
                'VPN1':{
                    'default_action_count': {
                        "packets": 0,
                        "bytes": 0
                    },
                    'FROM_TUNNEL_SAME_VPN_SC': {
                        "packets": 46960,
                        "bytes": 53256268
                    }
                },
                'VPN2':{
                    'default_action_count': {
                        "packets": 0,
                        "bytes": 0
                    },
                    'FROM_TUNNEL_DIFF_VPN_SC': {
                        "packets": 0,
                        "bytes": 0
                    }
                }
            },
            'DP_HUB_LOCAL_FROM_SERVICE': {
                'VPN1':{
                    'default_action_count': {
                        "packets": 430,
                        "bytes": 30020
                    },
                    'FROM_SVC_TO_BR2_SAME_VPN_SC': {
                        "packets": 1782,
                        "bytes": 124740
                    }
                },
                'VPN2':{
                    'default_action_count': {
                        "packets": 0,
                        "bytes": 0
                    },
                    'FROM_SVC_TO_BR2_DIFF_VPN_SC': {
                        "packets": 0,
                        "bytes": 0
                    }
                }
            }
        }
    }
