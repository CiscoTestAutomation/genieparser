expected_output = {
    'port': {
        '0': {
            'port_name': 'fpe0',
            'state_information': {
                'bind_name': '0000:0b:10.0',
                'driver': 'net_e1000_igb_vf',
                'mac_address': 'f86b.d9c0.cbe0',
                'device': 'RUNNING',
                'cio': {
                    'cio_state': 'ENABLED',
                    'if_type': 0,
                    'uidb_index': 1023,
                    'module_id': 1023,
                    'flags': '0x1'
                },
                'cio_events': {
                    'enable': 2,
                    'disable': 1
                },
                'tx_drain': 'FALSE',
                'vdev_pause': 'Inactive',
                'admin_state': 'Up',
                'oper_state': 'Up (Up)',
                'link_state': {
                    'up': 1,
                    'down': 0
                },
                'events': {
                    'remove': 0,
                    'reset': 1,
                    'link_up': 0,
                    'link_down': 0,
                    'bond_del': 0,
                    'unknown': 0
                },
                'vdev_rmv_pendng': 0,
                'attach_attempts': 50
            },
            'attributes': {
                'reconfigure': 'supported',
                'rx_offload_crc_strip': 'supported',
                'rx_offload_vlan_filter': 'supported',
                'rx_vlan_tag_insert': 'needed',
                'rx_vlan_tag_swap_': 'needed',
                'mac_filter_api': 'supported',
                'mc_promisc': 'always',
                'set_mc_addr_api': 'supported',
                'pause_resume': 'supported'
            },
            'configuration': {
                'promiscuous': {
                    'admin': 'disabled',
                    'override': 'disabled',
                    'multicast': 'enabled'
                },
                'mtu_config': {
                    'mtu': 1526,
                    'cur': 1500,
                    'min': 68,
                    'max': 65535
                },
                'trans_vlan': 0,
                'map_qid_num': 0,
                'map_qid_id': 0,
                'rx_ring_size': 0,
                'tx_ring_size': 0,
                'rx_active_q_num': 1,
                'rx_total_q_num': 1,
                'rx_cio_q_num': 1,
                'rx_desc_num': {
                    'queue_0': 1024
                },
                'tx_q_num': 1,
                'tx_desc_num': {
                    'queue_0': 1024
                },
                'num_vlans': 0
            }
        }
    }
}
