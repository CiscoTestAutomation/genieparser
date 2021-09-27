expected_output={
  "lsm_id": {
    "1": {
      "fec_root": "1.1.1.1",
      "lsm_id": 1,
      "opaque_decoded": {
        "mdt_data": "0x00010000",
        "rd": 65536,
        "type": "gid"
      },
      "opaque_length": 4,
      "opaque_length_type": "bytes",
      "opaque_value": "01 0004 00010000",
      "replication_client": {
        "2.2.2.2:0": {
          "interface": "Port-channel20",
          "local_label": "None",
          "next_hop": "104.1.1.2",
          "out_label": 35,
          "path_set_id": "None",
          "uptime": "00:00:42"
        },
        "vrf3001": {
          "interface": "Lspvif6",
          "path_set_id": "None",
          "rpf_id": "*",
          "uptime": "00:00:45"
        }
      },
      "type": "P2MP",
      "upstream_client": {
        "None": {
          "expires": "N/A",
          "path_set_id": 1
        }
      },
      "uptime": "00:00:45"
    },
    "2": {
      "fec_root": "1.1.1.1",
      "lsm_id": 2,
      "opaque_decoded": {
        "mdt_data": "0x0001FFFF",
        "rd": 131071,
        "type": "gid"
      },
      "opaque_length": 4,
      "opaque_length_type": "bytes",
      "opaque_value": "01 0004 0001FFFF",
      "replication_client": {
        "2.2.2.2:0": {
          "interface": "Port-channel20",
          "local_label": "None",
          "next_hop": "104.1.1.2",
          "out_label": 31,
          "path_set_id": "None",
          "uptime": "00:00:41"
        },
        "vrf3001": {
          "interface": "Lspvif6",
          "path_set_id": "None",
          "rpf_id": "*",
          "uptime": "00:00:41"
        }
      },
      "type": "P2MP",
      "upstream_client": {
        "None": {
          "expires": "N/A",
          "path_set_id": 2
        }
      },
      "uptime": "00:00:41"
    }
  }
}
