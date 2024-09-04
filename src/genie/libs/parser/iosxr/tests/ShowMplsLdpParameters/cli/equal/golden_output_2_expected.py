expected_output = {
    "ldp-parameters": {
        "role": "Active",
        "protocol-version": "1",
        "router-id": "2.2.2.2",
        "null-label": {
            "null-label-ipv4-address": "Implicit"
        },
        "session": {
            "session-holdtime-sec": 180,
            "session-keepalive-interval-sec": 60,
            "session-backoff": {
                "backoff-initial-sec": 15,
                "backoff-maximum-sec": 120
            },
            "global-md5-password": "Enabled"
        },
        "discovery": {
            "discovery-link-hellos": {
                "link-hellos-hold-time-sec": 15,
                "link-hellos-interval-sec": 5
            },
            "discovery-target-hellos": {
                "target-hellos-hold-time-sec": 90,
                "target-hellos-interval-sec": 10
            },
            "discovery-quick-start": "Enabled (by default)",
            "discovery-transport-address": {
                "transport-ipv4-address": "2.2.2.2"
            }
        },
        "graceful-restart": {
            "graceful-restart-status": "Enabled",
            "graceful-restart-reconnect-timeout": {
                "reconnect-timeout-time-sec": 120,
                "reconnect-timeout-forward-state-holdtime-sec": 180
            }
        },
        "nsr": {
            "nsr-status": "Enabled",
            "nsr-sync-ed-status": "Not Sync-ed"
        },
        "timeouts": {
            "housekeeping-periodic-timer-timeouts-sec": 10,
            "local-binding-timeouts-sec": 300,
            "forward-state-lsd-timeouts-sec": 360
        },
        "delay-af-bind-peer-sec": 180,
        "max": {
            "interfaces": {
                "max-interfaces-units": 4300,
                "attached-interfaces-units": 4000,
                "te-tunnel-interfaces-units": 300
            },
            "max-peers-units": 2000
        },
        "oor-state": {
            "oor-memory": "Normal"
        },
        "igp-sync-delay": {
            "interface-up-time-sec": 20
        }
    }
}

