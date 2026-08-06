expected_output = {
    'asic': {
        '0': {
            'rewritedata': {
                'BDA': {
                    'allocated': 0,
                    'free': 64,
                },
                'BSA': {
                    'allocated': 0,
                    'free': 4,
                },
                'DCI_UDP_DEST_PORT': {
                    'allocated': 0,
                    'free': 4,
                },
                'DECAP_DF_BIT': {
                    'allocated': 0,
                    'free': 8,
                },
                'ERSPAN_IPV6_TOS_LSB': {
                    'allocated': 0,
                    'free': 8,
                },
                'ERSPAN_IPV6_TOS_MSB': {
                    'allocated': 0,
                    'free': 8,
                },
                'ERSPAN_SESSION_ID': {
                    'allocated': 0,
                    'free': 8,
                },
                'ERSPAN_SESSION_ID_LS8': {
                    'allocated': 0,
                    'free': 8,
                },
                'GRE_HEADER': {
                    'allocated': 0,
                    'free': 684,
                },
                'GRE_KEY': {
                    'allocated': 0,
                    'free': 684,
                },
                'INSSEC_DEST_RLOC_IPv4_ADDR': {
                    'allocated': 1,
                    'free': 255,
                },
                'IPSEC_DEST_RLOC_IPV6': {
                    'allocated': 0,
                    'free': 256,
                },
                'IPV4_GRE_TUNNEL_DEST_IP_ADDR': {
                    'allocated': 0,
                    'free': 1024,
                },
                'IPV4_TUNNEL_DEST_IP_ADDR': {
                    'allocated': 0,
                    'free': 256,
                },
                'IPV4_TUNNEL_SRC_IP_ADDR': {
                    'allocated': 0,
                    'free': 16,
                },
                'IPV6_FLOW_ID': {
                    'allocated': 0,
                    'free': 4,
                },
                'IPV6_TUNNEL_DEST_IP_ADDR': {
                    'allocated': 0,
                    'free': 4,
                },
                'IPV6_TUNNEL_GRE_DEST_IP_ADDR': {
                    'allocated': 0,
                    'free': 256,
                },
                'IPV6_TUNNEL_SRC_IP_ADDR': {
                    'allocated': 0,
                    'free': 4,
                },
                'LAWFUL_INTERCEPT_IPv4_MD_ADDR': {
                    'allocated': 0,
                    'free': 20,
                },
                'LAWFUL_INTERCEPT_IPv4_SRC_ADD': {
                    'allocated': 0,
                    'free': 10,
                },
                'LAWFUL_INTERCEPT_IPv4_TOS': {
                    'allocated': 0,
                    'free': 20,
                },
                'LAWFUL_INTERCEPT_MD_DST_PORT': {
                    'allocated': 0,
                    'free': 100,
                },
                'LAWFUL_INTERCEPT_MD_IDENTIFIER': {
                    'allocated': 0,
                    'free': 100,
                },
                'LAWFUL_INTERCEPT_MD_SRC_PORT': {
                    'allocated': 0,
                    'free': 100,
                },
                'LOCAL_SEGMENT_IDS': {
                    'allocated': 0,
                    'free': 16,
                },
                'LVX_DEST_RLOC_IPV6': {
                    'allocated': 0,
                    'free': 1024,
                },
                'LVX_DEST_RLOC_IPv4_ADDR': {
                    'allocated': 0,
                    'free': 2048,
                },
                'LVX_HEADER_FIRST_16_BITS': {
                    'allocated': 0,
                    'free': 16,
                },
                'LVX_HEADER_LAST_8_BITS': {
                    'allocated': 0,
                    'free': 4,
                },
                'LVX_INNER_DEST_MAC_ADDR': {
                    'allocated': 0,
                    'free': 16,
                },
                'LVX_L3_LEAK_INST_ID_BYTE': {
                    'allocated': 0,
                    'free': 1500,
                },
                'LVX_MPLS_PEER_ID_TABLE_LSB': {
                    'allocated': 0,
                    'free': 2048,
                },
                'LVX_MPLS_PEER_ID_TABLE_MSB': {
                    'allocated': 0,
                    'free': 2048,
                },
                'LVX_SGT_IN_NONCE_MASK': {
                    'allocated': 0,
                    'free': 4,
                },
                'LVX_SOURCE_RLOC_IPV6': {
                    'allocated': 0,
                    'free': 130,
                },
                'LVX_SOURCE_RLOC_IPv4_ADDR': {
                    'allocated': 1,
                    'free': 129,
                },
                'LVX_TTL_PROP_MASK': {
                    'allocated': 1,
                    'free': 3,
                },
                'LVX_UDP_DEST_PORT': {
                    'allocated': 0,
                    'free': 4,
                },
                'MPLS_LABEL_TABLE': {
                    'allocated': 0,
                    'free': 16384,
                },
                'NAT_DST_PORT_UNICAST': {
                    'allocated': 0,
                    'free': 8192,
                },
                'NAT_L3_DEST_IPV4': {
                    'allocated': 0,
                    'free': 7168,
                },
                'NAT_L3_DEST_IPV6_LSB': {
                    'allocated': 0,
                    'free': 1,
                },
                'NAT_L3_DEST_IPV6_MSB': {
                    'allocated': 0,
                    'free': 1024,
                },
                'NAT_L3_SRC_IPV4': {
                    'allocated': 0,
                    'free': 8192,
                },
                'NAT_SRC_PORT_UNICAST': {
                    'allocated': 0,
                    'free': 8192,
                },
                'PHF_EGRESS_destMacAddress': {
                    'allocated': 3,
                    'free': 31997,
                },
                'SECURITY_ASSOCIATION_TABLE': {
                    'allocated': 1,
                    'free': 1023,
                },
                'UDP_ENCAP_DEST_PORT': {
                    'allocated': 0,
                    'free': 256,
                },
                'UDP_ENCAP_SRC_PORT': {
                    'allocated': 0,
                    'free': 256,
                },
                'WAN_MACSEC_FIRST_2_BYTES_TABLE': {
                    'allocated': 0,
                    'free': 16,
                },
                'WAN_MACSEC_PN_FIELD_TABLE': {
                    'allocated': 0,
                    'free': 16,
                },
                'WAN_MACSEC_REDIRECT_INDEX_TABLE': {
                    'allocated': 0,
                    'free': 512,
                },
                'WCCP2_DATA': {
                    'allocated': 0,
                    'free': 678,
                },
                'ipTtlTable': {
                    'allocated': 0,
                    'free': 16,
                },
            },
        },
    },
}
