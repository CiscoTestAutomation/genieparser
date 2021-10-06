

expected_output = {
    "vrf": {
        "default": {
           "local_as": 0,
           "originator_id": "10.16.2.2",
           "statistics": {
                "num_of_configured_peers": 1,
                "num_of_established_peers": 1,
                "num_of_shutdown_peers": 0
           },
           "peer": {
                "10.144.6.6": {
                     "elapsed_time": "06:15:59",
                     "statistics": {
                          "num_of_sg_received": 1,
                          "last_message_received": "00:00:48"
                     },
                     "session_state": "established",
                     "address": "10.144.6.6",
                     "peer_as": 0
                }
            }
        },
    }
}
