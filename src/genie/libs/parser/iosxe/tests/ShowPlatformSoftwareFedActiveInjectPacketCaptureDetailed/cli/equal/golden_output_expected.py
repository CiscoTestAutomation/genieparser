expected_output = {
    "inject_packet_capture": "disabled",
  "buffer_wrapping": "disabled",
  "total_captured": 1,
  "capture_capacity": 4096,
  "capture_filter": "\"udp.port == 9995\"",
  "inject_packet_number": {
    "1": {
      "interface": {
        "pal": {
          "iifd": "0x00000000]"
        }
      },
      "metadata": {
        "cause": "2 [QFP destination lookup],",
        "sub_cause": "1",
        "q_no": "0",
        "linktype": "MCP_LINK_TYPE_IP [1]"
      },
      "ether_hdr_1": {
        "dest_mac": "3c57.3104.6a00,",
        "src_mac": "3c57.3104.6a00"
      },
      "ether_hdr_2": {
        "ether_type": "0x0800 (IPv4)"
      },
      "ipv4_hdr_1": {
        "dest_ip": "111.0.0.2,",
        "src_ip": "111.0.0.1"
      },
      "ipv4_hdr_2": {
        "packet_len": "188",
        "ttl": "255",
        "protocol": "17 (UDP)"
      },
      "udp_hdr": {
        "dest_port": "9995",
        "src_port": "49572"
      },
      "doppler_frame_descriptor": {
        "fdformat": "0x3",
        "system_ttl": "0x8",
        "fdtype": "0x1",
        "span_session_map": "0",
        "qoslabel": "0x81",
        "fpe_first_header_type": "0"
      }
    }
  }
}

