expected_output = {
  'interface': {
    'interface_name': 'Te1/0/1',
    'if_id': 1032
  },
  'mac_link_status': {
    'mpp_port_details': {
      'link_state': 1,
      'pcs_status': 0,
      'high_ber': 0,
      'get_state': 'LINK_UP'
    },
    'autoneg_status': {
      'speed': 'speed_gbps1',
      'completed': 1,
      'link_status': 1,
      'rx_state': 1,
      'tx_state': 2,
      'sw_mode': 0,
      'cached': 1,
      'serdes_base': 19,
      'mpp_port_id': 1
    },
    'mib_counters': {
      'tx_legal_frames_counter': 90046,
      'tx_legal_bytes_counter': 6720314,
      'tx_legal_frames_with_64_bytes': 87477,
      'tx_legal_frames_with_65_127_bytes': 1,
      'tx_legal_frames_with_128_255_bytes': 2,
      'tx_legal_frames_with_256_511_bytes': 2,
      'tx_legal_frames_with_512_1023_bytes': 0,
      'tx_legal_frames_with_1024_1518_bytes': 0,
      'tx_legal_frames_with_1519_2500_bytes': 0,
      'tx_legal_frames_with_2501_9000_bytes': 0,
      'tx_frames_with_crc_error': 0,
      'tx_internal_error_packets_missing_the_end_of_packet': 0,
      'tx_internal_error_under_run_packets': 0,
      'tx_legal_flow_control_packets': 0,
      'tx_out_of_band_packets_transmitted': 0,
      'tx_internal_error_out_of_band_packets_with_crc_error': 0,
      'tx_lpi_active_count': 0,
      'tx_lpi_transition_count': 0,
      'rx_legal_frames': 0,
      'rx_legal_bytes': 0,
      'rx_legal_frames_with_64_bytes': 0,
      'rx_legal_frames_with_65_127_bytes': 0,
      'rx_legal_frames_with_128_255_bytes': 0,
      'rx_legal_frames_with_256_511_bytes': 0,
      'rx_legal_frames_with_511_1023_bytes': 0,
      'rx_legal_frames_with_1024_1518_bytes': 0,
      'rx_legal_frames_with_1519_2500_bytes': 0,
      'rx_legal_frames_with_2501_9000_bytes': 0,
      'rx_received_frames_with_inverted_crc': 0,
      'rx_packets_received_with_crc_errors': 0,
      'rx_packet_received_larger_from_max_packet_size': 0,
      'rx_packet_received_smaller_from_min_packet_size': 0,
      'rx_packets_with_code_error': 0,
      'rx_legal_flow_control_packets': 0,
      'rx_out_of_band_packets_received': 0,
      'rx_packets_received_with_inverted_crc': 0,
      'rx_out_of_band_packets_with_crc_error': 0,
      'rx_out_of_band_packets_with_code_error': 0,
      'rx_lpi_active_count': 0,
      'rx_lpi_transition_count': 0
    }
  },
  'port': 1,
  'slot': 1,
  'cmd': 'port_diag unit 1 port 0 slot 0',
  'rc': '0x0',
  'rsn': 'success',
  'phy_link_status': {
    'phy_configuration': {
      'autoneg': 'Enabled',
      'duplex': 'Full',
      'loopback': 'Disabled',
      'autoneg_restart': 'Complete'
    },
    'phy_status': {
      'phy_link_status': 'LinkUp',
      'auto_neg_status': 'Completed',
      'speed': '1000M',
      'mdix_status': 'ON',
      'fr_mode': 'NFR',
      'fr_ability': 'False',
      'fr_signal_type': 'Signal IDLE during FR',
      'no_of_fr_requested': 0,
      'total_no_of_fr': 0,
      'fr_status': 'Disable',
      'tx_resolution': 'Enable',
      'timer_resolution': '30 ms',
      'extended_timer': 'Not requested',
      'fr_tx_disable': 'Not requested'
    }
  }
}
