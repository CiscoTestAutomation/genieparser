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
            }
        }
    }
