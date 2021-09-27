expected_output={
  "lsm_id": {
    "21": {
      "fec_root": "5.5.5.5",
      "lsm_id": 21,
      "opaque_decoded": {
        "mdt_data": 0,
        "rd": "3001:1",
        "type": "mdt"
      },
      "opaque_length": 11,
      "opaque_length_type": "bytes",
      "opaque_value": "02 000B 0030010000000100000000",
      "replication_client": {
        "vrf3001": {
          "interface": "Lspvif1",
          "path_set_id": 22,
          "rpf_id": "*",
          "uptime": "1d05h"
        }
      },
      "rnr_lsm_id": 22,
      "type": "MP2MP",
      "upstream_client": {
        "2.2.2.2:0": {
          "expires": "Never",
          "interface": "Port-channel20",
          "local_label": 27,
          "next_hop": "104.1.1.2",
          "out_label": 24,
          "path_set_id": 21,
          "state": "Active"
        }
      },
      "uptime": "1d05h"
    }
  }
}
