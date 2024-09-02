expected_output = {
   "nhrp_cache_add":{
      "1_1_1_1":{
         "event":"NHRP-CACHE-ADD",
         "tunnel":"Tu1",
         "target":"192.168.10.",
         "nbma_src":"2.2.2.1",
         "vpn_src":"192.168.10.2",
         "nbma_dest":"1.1.1.1",
         "vpn_dest":"192.168.10.3",
         "vrf":"global(0x0)",
         "label":"none"
      },
      "2_2_2_1":{
         "event":"NHRP-CACHE-ADD",
         "tunnel":"Tu1",
         "target":"192.168.10.",
         "nbma_src":"3.3.3.1",
         "vpn_src":"192.168.10.3",
         "nbma_dest":"2.2.2.1",
         "vpn_dest":"192.168.10.2",
         "vrf":"global(0x0)",
         "label":"none"
      },
      "3_3_3_1":{
         "event":"NHRP-CACHE-ADD",
         "tunnel":"Tu1",
         "target":"192.168.10.",
         "nbma_src":"1.1.1.1",
         "vpn_src":"192.168.10.1",
         "nbma_dest":"3.3.3.1",
         "vpn_dest":"192.168.10.3",
         "vrf":"global(0x0)",
         "label":"none"
      }
   },
   "nhrp_nhc_up":{
      "2_2_2_1":{
         "event":"NHRP-NHC-UP",
         "tunnel":"Tu1",
         "nbma_src":"1.1.1.1",
         "vpn_src":"192.168.10.1",
         "nbma_dest":"2.2.2.1",
         "vpn_dest":"192.168.10.2",
         "vrf":"global(0x0)"
      },
      "3_3_3_1":{
         "event":"NHRP-NHC-UP",
         "tunnel":"Tu1",
         "nbma_src":"1.1.1.1",
         "vpn_src":"192.168.10.1",
         "nbma_dest":"3.3.3.1",
         "vpn_dest":"192.168.10.3",
         "vrf":"global(0x0)"
      }
   },
   "nhrp_tunnel_endpoint_add":{
      "2_2_2_1":{
         "event":"NHRP-TUNNEL-ENDPOINT-ADD",
         "tunnel":"Tu1",
         "nbma_dest":"2.2.2.1",
         "vpn_dest":"192.168.10.2"
      },
      "3_3_3_1":{
         "event":"NHRP-TUNNEL-ENDPOINT-ADD",
         "tunnel":"Tu1",
         "nbma_dest":"3.3.3.1",
         "vpn_dest":"192.168.10.3"
      },
      '1_1_1_1': {
         'event': 'NHRP-TUNNEL-ENDPOINT-ADD',
         'nbma_dest': '1.1.1.1',
         'tunnel': 'Tu1',
         'vpn_dest': '192.168.10.3',
      },
   },
   "nhrp_nhs_up":{
      "1_1_1_1":{
         "event":"NHRP-NHS-UP",
         "tunnel":"Tu1",
         "nbma_src":"3.3.3.1",
         "vpn_src":"192.168.10.3",
         "nbma_dest":"1.1.1.1",
         "vpn_dest":"192.168.10.1",
         "vrf":"global(0x0)"
      }
   },
   "nhrp_recv_res_req":{
      "2_2_2_1":{
         "event":"NHRP-RECV-RES-REQ",
         "tunnel":"Tu1",
         "nbma_src":"3.3.3.1",
         "vpn_src":"192.168.10.3",
         "nbma_dest":"2.2.2.1",
         "vpn_dest":"192.168.10.2",
         "vrf":"global(0x0)",
         "label":"none"
      }
   },
   "nhrp_send_res_req":{
      "1_1_1_1":{
         "event":"NHRP-SEND-RES-REQ",
         "tunnel":"Tu1",
         "nbma_src":"2.2.2.1",
         "vpn_src":"192.168.10.2",
         "nbma_dest":"1.1.1.1",
         "vpn_dest":"192.168.10.3",
         "vrf":"global(0x0)",
         "label":"none"
      }
   },
   "nhrp_recv_res_reply":{
      "3_3_3_1":{
         "event":"NHRP-RECV-RES-REPLY",
         "tunnel":"Tu1",
         "nbma_src":"2.2.2.1",
         "vpn_src":"192.168.10.2",
         "nbma_dest":"3.3.3.1",
         "vpn_dest":"192.168.10.3",
         "vrf":"global(0x0)",
         "label":"none"
      }
   },
   "nhrp_send_res_reply":{
      "2_2_2_1":{
         "event":"NHRP-SEND-RES-REPLY",
         "tunnel":"Tu1",
         "nbma_src":"3.3.3.1",
         "vpn_src":"192.168.10.3",
         "nbma_dest":"2.2.2.1",
         "vpn_dest":"192.168.10.2",
         "vrf":"global(0x0)",
         "label":"illegal"
      }
   },
   "nhrp_recv_purge_req":{
      '2_2_2_1': {
         'event': 'NHRP-RECV-PURGE-REQ',
         'label': 'explicit-null',
         'nbma_dest': '2.2.2.1',
         'nbma_src': '1.1.1.1',
         'tunnel': 'Tu1',
         'vpn_dest': '192.168.10.2',
         'vpn_src': '192.168.10.1',
         'vrf': 'global(0x0)',
        },
      "3_3_3_1":{
         "event":"NHRP-RECV-PURGE-REQ",
         "tunnel":"Tu1",
         "nbma_src":"1.1.1.1",
         "vpn_src":"192.168.10.2",
         "nbma_dest":"3.3.3.1",
         "vpn_dest":"192.168.10.3",
         "vrf":"global(0x0)",
         "label":"explicit-null"
      }
   },
   "nhrp_send_purge_req":{
      "UNKNOWN":{
         "event":"NHRP-SEND-PURGE-REQ",
         "tunnel":"Tu1",
         "nbma_src":"3.3.3.1",
         "vpn_src":"192.168.10.3",
         "nbma_dest":"UNKNOWN",
         "vpn_dest":"192.168.10.2",
         "vrf":"global(0x0)",
         "label":"none"
      }
   },
   "nhrp_nhc_down":{
      "2_2_2_1":{
         "event":"NHRP-NHC-DOWN",
         "tunnel":"Tu1",
         "nbma_src":"1.1.1.1",
         "vpn_src":"192.168.10.1",
         "nbma_dest":"2.2.2.1",
         "vpn_dest":"192.168.10.2",
         "vrf":"global(0x0)",
         "reason":"EXT - Tunnel Interface AdminDown"
      },
      "3_3_3_1":{
         "event":"NHRP-NHC-DOWN",
         "tunnel":"Tu1",
         "nbma_src":"1.1.1.1",
         "vpn_src":"192.168.10.1",
         "nbma_dest":"3.3.3.1",
         "vpn_dest":"192.168.10.3",
         "vrf":"global(0x0)",
         "reason":"EXT - Tunnel Interface AdminDown"
      }
   },
   "nhrp_tunnel_endpoint_delete":{
      "2_2_2_1":{
         "event":"NHRP-TUNNEL-ENDPOINT-DELETE",
         "tunnel":"Tu1",
         "nbma_dest":"2.2.2.1",
         "vpn_dest":"192.168.10.2"
      },
      "3_3_3_1":{
         "event":"NHRP-TUNNEL-ENDPOINT-DELETE",
         "tunnel":"Tu1",
         "nbma_dest":"3.3.3.1",
         "vpn_dest":"192.168.10.3"
      },
      '1_1_1_1': {
         'event': 'NHRP-TUNNEL-ENDPOINT-DELETE',
         'nbma_dest': '1.1.1.1',
         'tunnel': 'Tu1',
         'vpn_dest': '192.168.10.1',
      },
   },
   "nhrp_nhs_down":{
      "1_1_1_1":{
         "event":"NHRP-NHS-DOWN",
         "tunnel":"Tu1",
         "nbma_src":"3.3.3.1",
         "vpn_src":"192.168.10.3",
         "nbma_dest":"1.1.1.1",
         "vpn_dest":"192.168.10.1",
         "vrf":"global(0x0)"
      }
   },
   "nhrp_ctrl_plane_retrance":{
      "192_168_10_1":{
         "event":"NHRP-CTRL-PLANE-RETRANS",
         "tunnel":"Tu1",
         "vpn_dest":"192.168.10.1",
         "vrf":"NONE"
      }
   },
   "nhrp_nhs_recovery_nhs_state":{
      "192_168_10_1":{
         "event":"NHRP-NHS-RECOVERY-NHS-STATE",
         "vpn_dest":"192.168.10.1"
      }
   },
   "nhrp_nhp_down":{
      '1_1_1_1': {
        'event': 'NHRP-NHP-DOWN',
        'tunnel': 'Tu1',
        'nbma_dest': '1.1.1.1',
        'nbma_src': '3.3.3.1',
        'reason': 'EXT ',
        'vpn_dest': '192.168.10.1',
        'vpn_src': '192.168.10.3',
        'vrf': 'global(0x0)'
      },
      "3_3_3_1":{
         "event":"NHRP-NHP-DOWN",
         "tunnel":"Tu1",
         "nbma_src":"2.2.2.1",
         "vpn_src":"192.168.10.2",
         "nbma_dest":"3.3.3.1",
         "vpn_dest":"192.168.10.3",
         "vrf":"global(0x0)",
         "reason":"No Reason"
      },
      "2_2_2_1":{
         "event":"NHRP-NHP-DOWN",
         "tunnel":"Tu1",
         "nbma_src":"3.3.3.1",
         "vpn_src":"192.168.10.3",
         "nbma_dest":"2.2.2.1",
         "vpn_dest":"192.168.10.2",
         "vrf":"global(0x0)",
         "reason":"No Reason"
      }

   },
   "nhrp_cache_update":{
      "1_1_1_1":{
         "event":"NHRP-CACHE-UPDATE",
         "tunnel":"Tu1",
         "target":"192.168.10.",
         "nbma_src":"2.2.2.1",
         "vpn_src":"192.168.10.2",
         "nbma_dest":"1.1.1.1",
         "vpn_dest":"192.168.10.3",
         "vrf":"global(0x0)",
         "label":"none"
      },
      '2_2_2_1': {
         'event': 'NHRP-CACHE-UPDATE',
         'label': 'none',
         'nbma_dest': '2.2.2.1',
         'nbma_src': '1.1.1.1',
         'target': '192.168.10.',
         'tunnel': 'Tu1',
         'vpn_dest': '192.168.10.2',
         'vpn_src': '192.168.10.1',
         'vrf': 'global(0x0)',
        },
      "3_3_3_1":{
         "event":"NHRP-CACHE-UPDATE",
         "tunnel":"Tu1",
         "target":"192.168.10.",
         "nbma_src":"1.1.1.1",
         "vpn_src":"192.168.10.1",
         "nbma_dest":"3.3.3.1",
         "vpn_dest":"192.168.10.3",
         "vrf":"global(0x0)",
         "label":"none"
      }
   },
   "nhrp_tunnel_endpoint_add":{
      "2_2_2_1":{
         "event":"NHRP-TUNNEL-ENDPOINT-ADD",
         "tunnel":"Tu1",
         "nbma_dest":"2.2.2.1",
         "vpn_dest":"192.168.10.2"
      },
      "3_3_3_1":{
         "event":"NHRP-TUNNEL-ENDPOINT-ADD",
         "tunnel":"Tu1",
         "nbma_dest":"3.3.3.1",
         "vpn_dest":"192.168.10.3"
      },
      "1_1_1_1":{
         "event":"NHRP-TUNNEL-ENDPOINT-ADD",
         "tunnel":"Tu1",
         "nbma_dest":"1.1.1.1",
         "vpn_dest":"192.168.10.3"
      }
   },
   'nhrp_cache_nbma_nhop_change': {
      '1_1_1_1': {
         'event': 'NHRP-CACHE-NBMA-NHOP-CHANGE',
         'new': '3.3.3.1',
         'old': '1.1.1.1',
         'tunnel': 'Tu1',
      },
   },
   'nhrp_cache_delete': {
      '1_1_1_1': {
         'event': 'NHRP-CACHE-DELETE',
         'label': 'none',
         'nbma_dest': '1.1.1.1',
         'nbma_src': '3.3.3.1',
         'reason': 'EXT - Admin action ',
         'tunnel': 'Tu1',
         'vpn_dest': '192.168.10.',
         'vpn_src': '0.0.0.0',
         'vrf': 'global(0x0)',
        },
      '2_2_2_1': {
         'event': 'NHRP-CACHE-DELETE',
         'label': 'none',
         'nbma_dest': '2.2.2.1',
         'nbma_src': '3.3.3.1',
         'reason': 'No Reason',
         'tunnel': 'Tu1',
         'vpn_dest': '192.168.10.',
         'vpn_src': '192.168.10.3',
         'vrf': 'global(0x0)',
        },
      '3_3_3_1': {
         'event': 'NHRP-CACHE-DELETE',
         'label': 'none',
         'nbma_dest': '3.3.3.1',
         'nbma_src': '3.3.3.1',
         'reason': 'No Reason',
         'tunnel': 'Tu1',
         'vpn_dest': '192.168.10.',
         'vpn_src': '192.168.10.3',
         'vrf': 'global(0x0)',
        }
   }
}