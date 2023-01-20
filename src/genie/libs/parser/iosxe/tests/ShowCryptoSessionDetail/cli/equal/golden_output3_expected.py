expected_output= {
  "interface": {
    "1": {
      "interface": "Tunnel3111",
      "peer": {
        "192.168.1.1": {
          "port": {
            "500": {
              "desc": "none",
              "fvrf": "none",
              "ipsec_flow": {
                "permit ip 100.75.0.0/255.255.255.192 192.168.25.0/255.255.255.0": {
                  "active_sas": 0,
                  "inbound_life_kb": "0",
                  "inbound_life_secs": "0",
                  "inbound_pkts_decrypted": 0,
                  "inbound_pkts_drop": 0,
                  "origin": "crypto map",
                  "outbound_life_kb": "0",
                  "outbound_life_secs": "0",
                  "outbound_pkts_drop": 0,
                  "outbound_pkts_encrypted": 0
                },
                "permit ip 100.75.0.0/255.255.255.192 192.168.25.0/255.255.255.128": {
                  "active_sas": 0,
                  "inbound_life_kb": "0",
                  "inbound_life_secs": "0",
                  "inbound_pkts_decrypted": 0,
                  "inbound_pkts_drop": 0,
                  "origin": "crypto map",
                  "outbound_life_kb": "0",
                  "outbound_life_secs": "0",
                  "outbound_pkts_drop": 0,
                  "outbound_pkts_encrypted": 0
                },
                "permit ip 100.75.0.0/255.255.255.192 192.168.26.0/255.255.255.0": {
                  "active_sas": 0,
                  "inbound_life_kb": "0",
                  "inbound_life_secs": "0",
                  "inbound_pkts_decrypted": 0,
                  "inbound_pkts_drop": 0,
                  "origin": "crypto map",
                  "outbound_life_kb": "0",
                  "outbound_life_secs": "0",
                  "outbound_pkts_drop": 0,
                  "outbound_pkts_encrypted": 0
                },
                "permit ip host 100.74.10.1 192.168.25.0/255.255.255.0": {
                  "active_sas": 0,
                  "inbound_life_kb": "0",
                  "inbound_life_secs": "0",
                  "inbound_pkts_decrypted": 0,
                  "inbound_pkts_drop": 0,
                  "origin": "crypto map",
                  "outbound_life_kb": "0",
                  "outbound_life_secs": "0",
                  "outbound_pkts_drop": 0,
                  "outbound_pkts_encrypted": 0
                },
                "permit ip host 100.74.10.1 192.168.25.0/255.255.255.128": {
                  "active_sas": 0,
                  "inbound_life_kb": "0",
                  "inbound_life_secs": "0",
                  "inbound_pkts_decrypted": 0,
                  "inbound_pkts_drop": 0,
                  "origin": "crypto map",
                  "outbound_life_kb": "0",
                  "outbound_life_secs": "0",
                  "outbound_pkts_drop": 0,
                  "outbound_pkts_encrypted": 0
                },
                "permit ip host 100.74.10.1 192.168.26.0/255.255.255.0": {
                  "active_sas": 0,
                  "inbound_life_kb": "0",
                  "inbound_life_secs": "0",
                  "inbound_pkts_decrypted": 0,
                  "inbound_pkts_drop": 0,
                  "origin": "crypto map",
                  "outbound_life_kb": "0",
                  "outbound_life_secs": "0",
                  "outbound_pkts_drop": 0,
                  "outbound_pkts_encrypted": 0
                }
              },
              "ivrf": "inner",
              "phase1_id": "(none)"
            }
          }
        }
      },
      "session_status": "DOWN"
    },
    "2": {
      "interface": "Tunnel3111",
      "peer": {
        "192.168.1.1": {
          "port": {
            "500": {
              "desc": "none",
              "fvrf": "none",
              "ike_sa": {
                "1": {
                  "capabilities": "none",
                  "conn_id": "0",
                  "lifetime": "0",
                  "local": "94.140.184.80",
                  "local_port": "500",
                  "remote": "192.168.1.1",
                  "remote_port": "500",
                  "sa_status": "Inactive",
                  "session_id": "0",
                  "version": "IKEv1"
                },
                "2": {
                  "capabilities": "none",
                  "conn_id": "0",
                  "lifetime": "0",
                  "local": "94.140.184.80",
                  "local_port": "500",
                  "remote": "192.168.1.1",
                  "remote_port": "500",
                  "sa_status": "Inactive",
                  "session_id": "0",
                  "version": "IKEv1"
                }
              },
              "ivrf": "none",
              "phase1_id": "(none)"
            }
          }
        }
      },
      "profile": "ISAKMP-inner-LOC_A",
      "session_status": "DOWN-NEGOTIATING"
    }
  }
}