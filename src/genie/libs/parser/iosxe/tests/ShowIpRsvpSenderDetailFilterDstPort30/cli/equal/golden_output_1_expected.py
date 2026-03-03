expected_output = {
 "sessions": {
  "1": {
   "name": "rsvp",
   "details": {}
  },
  "7": {
   "name": "te-p2p-lsp",
   "path": {
    "tunnel_destination": "100.1.1.2",
    "tunnel_id": 30,
    "ext_tunnel_id": "100.1.1.3",
    "tunnel_sender": "100.1.1.3",
    "lsp_id": 40,
    "path_refreshes": {
     "sent": {
      "nhop": "10.1.1.5",
      "outgoing_interface": "FiveGigabitEthernet0/0/2"
     }
    },
    "session_attributes": {
     "setup_priority": 2,
     "holding_priority": 2,
     "flags": {
      "hex": "0x7",
      "local_protection_desired": True,
      "label_recording": True,
      "se_style": True
     },
     "session_name": "rt3_t30"
    },
    "ero": {
     "incoming": [
      {
       "address": "100.1.1.3",
       "type": "Strict IPv4 Prefix",
       "bytes": 8,
       "prefix_length": 32
      },
      {
       "address": "10.1.1.6",
       "type": "Strict IPv4 Prefix",
       "bytes": 8,
       "prefix_length": 32
      },
      {
       "address": "10.1.1.5",
       "type": "Strict IPv4 Prefix",
       "bytes": 8,
       "prefix_length": 32
      },
      {
       "address": "100.1.1.2",
       "type": "Strict IPv4 Prefix",
       "bytes": 8,
       "prefix_length": 32
      }
     ],
     "outgoing": [
      {
       "address": "10.1.1.5",
       "type": "Strict IPv4 Prefix",
       "bytes": 8,
       "prefix_length": 32
      },
      {
       "address": "100.1.1.2",
       "type": "Strict IPv4 Prefix",
       "bytes": 8,
       "prefix_length": 32
      }
     ]
    },
    "traffic_parameters": {
     "rate": "158K bits/sec",
     "max_burst": "1K bytes",
     "min_policed_unit_bytes": 0,
     "max_packet_size_bytes": 2147483647
    },
    "fast_reroute": {
     "inbound_frr": "Not active",
     "outbound_frr": "Ready -- backup tunnel selected",
     "backup_tunnel": {
      "name": "Tu31",
      "label": 3
     },
     "backup_sender_template": {
      "tunnel_sender": "10.1.1.9",
      "lsp_id": 40
     },
     "backup_filterspec": {
      "tunnel_sender": "10.1.1.9",
      "lsp_id": 40
     }
    },
    "path_id_handle": "FC000428",
    "incoming_policy": {
     "status": "Accepted",
     "policy_sources": [
      "MPLS/TE"
     ]
    },
    "status": "Proxied",
    "output_interface": "FiveGigabitEthernet0/0/2",
    "output_policy_status": "Forwarding",
    "output_handle": "7D000405",
    "output_policy_sources": [
     "MPLS/TE"
    ]
   }
  }
 }
}