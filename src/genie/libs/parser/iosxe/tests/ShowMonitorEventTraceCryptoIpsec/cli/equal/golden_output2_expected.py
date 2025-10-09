expected_output ={
  "events": [
    {
      "timestamp": "Apr  4 00:10:51.829",
      "event_type": "IPSEC-EVENT:IPSEC-DELETE-SA",
      "message": "sa delete : (sa) sa_dest = 30.1.1.1, sa_proto = 50, sa_spi = 0xB820B40F(3089150991), sa_trans = esp-aes esp-sha-hmac , sa_conn_id = 2021, sa_lifetime(k/sec) = (4608000/3600)",
      "details": {
        "sa_action": "delete",
        "sa_dest": "30.1.1.1",
        "sa_proto": 50,
        "sa_spi": "0xB820B40F(3089150991)",
        "sa_trans": "esp-aes esp-sha-hmac",
        "sa_conn_id": 2021,
        "sa_lifetime_k": 4608000,
        "sa_lifetime_sec": 3600
      }
    },
    {
      "timestamp": "Apr  4 00:10:51.829",
      "event_type": "IPSEC-EVENT:IPSEC-DELETE-SA",
      "message": "sa delete : (sa),  loc: 30.1.1.1, rem: 30.1.1.2, l_proxy: 0.0.0.0/0/256, r_proxy: 0.0.0.0/0/256",
      "details": {
        "sa_action": "delete",
        "loc": "30.1.1.1",
        "rem": "30.1.1.2",
        "l_proxy": "0.0.0.0/0/256",
        "r_proxy": "0.0.0.0/0/256"
      }
    },
    {
      "timestamp": "Apr  4 00:10:51.829",
      "event_type": "IPSEC-EVENT:IPSEC-DELETE-SA",
      "message": "sa delete : (sa) sa_dest = 30.1.1.2, sa_proto = 50, sa_spi = 0xF070E037(4033929271), sa_trans = esp-aes esp-sha-hmac , sa_conn_id = 2022, sa_lifetime(k/sec) = (4608000/3600)",
      "details": {
        "sa_action": "delete",
        "sa_dest": "30.1.1.2",
        "sa_proto": 50,
        "sa_spi": "0xF070E037(4033929271)",
        "sa_trans": "esp-aes esp-sha-hmac",
        "sa_conn_id": 2022,
        "sa_lifetime_k": 4608000,
        "sa_lifetime_sec": 3600
      }
    },
    {
      "timestamp": "Apr  4 00:10:51.829",
      "event_type": "IPSEC-EVENT:IPSEC-DELETE-SA",
      "message": "sa delete : (sa),  loc: 30.1.1.1, rem: 30.1.1.2, l_proxy: 0.0.0.0/0/256, r_proxy: 0.0.0.0/0/256",
      "details": {
        "sa_action": "delete",
        "loc": "30.1.1.1",
        "rem": "30.1.1.2",
        "l_proxy": "0.0.0.0/0/256",
        "r_proxy": "0.0.0.0/0/256"
      }
    },
    {
      "timestamp": "Apr  4 00:10:51.829",
      "event_type": "IPSEC-EVENT:IPSEC-DELETE-SA",
      "message": "SESSION ID:0, sa delete : (sa) sa_dest = 30.1.1.1, sa_proto = 50, sa_spi = 0xB820B40F(3089150991), sa_trans = esp-aes esp-sha-hmac , sa_conn_id = 2021, sa_lifetime(k/sec) = (4608000/3600)",
      "details": {
        "session_id": 0,
        "sa_action": "delete",
        "sa_dest": "30.1.1.1",
        "sa_proto": 50,
        "sa_spi": "0xB820B40F(3089150991)",
        "sa_trans": "esp-aes esp-sha-hmac",
        "sa_conn_id": 2021,
        "sa_lifetime_k": 4608000,
        "sa_lifetime_sec": 3600
      }
    },
    {
      "timestamp": "Apr  4 00:10:51.829",
      "event_type": "IPSEC-EVENT:IPSEC-DELETE-SA",
      "message": "SESSION ID:0, sa delete : (sa),  loc: 30.1.1.1, rem: 30.1.1.2, l_proxy: 0.0.0.0/0/256, r_proxy: 0.0.0.0/0/256",
      "details": {
        "session_id": 0,
        "sa_action": "delete",
        "loc": "30.1.1.1",
        "rem": "30.1.1.2",
        "l_proxy": "0.0.0.0/0/256",
        "r_proxy": "0.0.0.0/0/256"
      }
    },
    {
      "timestamp": "Apr  4 00:10:51.829",
      "event_type": "IPSEC-EVENT:IPSEC-DELETE-SA",
      "message": "SESSION ID:0, sa delete : (sa) sa_dest = 30.1.1.2, sa_proto = 50, sa_spi = 0xF070E037(4033929271), sa_trans = esp-aes esp-sha-hmac , sa_conn_id = 2022, sa_lifetime(k/sec) = (4608000/3600)",
      "details": {
        "session_id": 0,
        "sa_action": "delete",
        "sa_dest": "30.1.1.2",
        "sa_proto": 50,
        "sa_spi": "0xF070E037(4033929271)",
        "sa_trans": "esp-aes esp-sha-hmac",
        "sa_conn_id": 2022,
        "sa_lifetime_k": 4608000,
        "sa_lifetime_sec": 3600
      }
    },
    {
      "timestamp": "Apr  4 00:10:51.829",
      "event_type": "IPSEC-EVENT:IPSEC-DELETE-SA",
      "message": "SESSION ID:0, sa delete : (sa),  loc: 30.1.1.1, rem: 30.1.1.2, l_proxy: 0.0.0.0/0/256, r_proxy: 0.0.0.0/0/256",
      "details": {
        "session_id": 0,
        "sa_action": "delete",
        "loc": "30.1.1.1",
        "rem": "30.1.1.2",
        "l_proxy": "0.0.0.0/0/256",
        "r_proxy": "0.0.0.0/0/256"
      }
    },
    {
      "timestamp": "Apr  4 00:10:51.829",
      "event_type": "IPSEC-EVENT:IPSEC-SEND-KMI",
      "message": "SESSION ID:0, KMI Sent: IPSEC key engine->Crypto IKMP:KEY_ENG_NOTIFY_DECR_COUNT",
      "details": {
        "session_id": 0,
        "kmi_direction": "Sent",
        "kmi_source": "IPSEC key engine",
        "kmi_destination": "Crypto IKMP",
        "kmi_type": "KEY_ENG_NOTIFY_DECR_COUNT"
      }
    },
    {
      "timestamp": "Apr  4 00:10:51.829",
      "event_type": "IPSEC-EVENT:IPSEC-SEND-KMI",
      "message": "SESSION ID:0, KMI Sent: IPSEC key engine->Crypto IKMP:KEY_ENG_DELETE_SAS, loc: 30.1.1.1, rem: 30.1.1.2, port loc/rem: 0/500, prot: DOI-3",
      "details": {
        "session_id": 0,
        "kmi_direction": "Sent",
        "kmi_source": "IPSEC key engine",
        "kmi_destination": "Crypto IKMP",
        "kmi_type": "KEY_ENG_DELETE_SAS",
        "loc": "30.1.1.1",
        "rem": "30.1.1.2",
        "port_loc": 0,
        "port_rem": 500,
        "prot": "DOI-3"
      }
    },
    {
      "timestamp": "Apr  4 00:10:52.173",
      "event_type": "IPSEC-EVENT:IPSEC-RECV-KMI",
      "message": "SESSION ID:0, KMI Received: Crypto IKMP->IPSEC key engine:KEY_MGR_SESSION_CLOSED, loc: 30.1.1.1, rem: 30.1.1.2, port loc/rem: 500/500",
      "details": {
        "session_id": 0,
        "kmi_direction": "Received",
        "kmi_source": "Crypto IKMP",
        "kmi_destination": "IPSEC key engine",
        "kmi_type": "KEY_MGR_SESSION_CLOSED",
        "loc": "30.1.1.1",
        "rem": "30.1.1.2",
        "port_loc": 500,
        "port_rem": 500
      }
    },
    {
      "timestamp": "Apr  4 00:10:52.793",
      "event_type": "IPSEC-EVENT:IPSEC-SEND-KMI",
      "message": "SESSION ID:0, KMI Sent: IPSEC key engine->Crypto IKMP:KEY_ENG_REQUEST_SAS, loc: 30.1.1.1, rem: 30.1.1.2, l_proxy: 0.0.0.0/0/256, r_proxy: 0.0.0.0/0/256",
      "details": {
        "session_id": 0,
        "kmi_direction": "Sent",
        "kmi_source": "IPSEC key engine",
        "kmi_destination": "Crypto IKMP",
        "kmi_type": "KEY_ENG_REQUEST_SAS",
        "loc": "30.1.1.1",
        "rem": "30.1.1.2",
        "l_proxy": "0.0.0.0/0/256",
        "r_proxy": "0.0.0.0/0/256"
      }
    },
    {
      "timestamp": "Apr  4 00:10:52.813",
      "event_type": "IPSEC-EVENT:IPSEC-RECV-KMI",
      "message": "SESSION ID:0, KMI Received: Crypto IKMP->IPSEC key engine:KEY_MGR_CREATE_IPSEC_SAS, loc: 30.1.1.1, rem: 30.1.1.2, l_proxy: 0.0.0.0/500/256, r_proxy: 0.0.0.0/500/256",
      "details": {
        "session_id": 0,
        "kmi_direction": "Received",
        "kmi_source": "Crypto IKMP",
        "kmi_destination": "IPSEC key engine",
        "kmi_type": "KEY_MGR_CREATE_IPSEC_SAS",
        "loc": "30.1.1.1",
        "rem": "30.1.1.2",
        "l_proxy": "0.0.0.0/500/256",
        "r_proxy": "0.0.0.0/500/256"
      }
    },
    {
      "timestamp": "Apr  4 00:10:52.813",
      "event_type": "IPSEC-EVENT:IPSEC-SEND-KMI",
      "message": "SESSION ID:0, KMI Sent: IPSEC key engine->Crypto IKMP:KEY_ENG_NOTIFY_QOS_GROUP, loc: UNKNOWN, rem: UNKNOWN, port loc/rem: 0/0, prot: 0",
      "details": {
        "session_id": 0,
        "kmi_direction": "Sent",
        "kmi_source": "IPSEC key engine",
        "kmi_destination": "Crypto IKMP",
        "kmi_type": "KEY_ENG_NOTIFY_QOS_GROUP",
        "loc": "UNKNOWN",
        "rem": "UNKNOWN",
        "port_loc": 0,
        "port_rem": 0,
        "prot": "0"
      }
    },
    {
      "timestamp": "Apr  4 00:10:52.813",
      "event_type": "IPSEC-EVENT:IPSEC-SEND-KMI",
      "message": "SESSION ID:0, KMI Sent: IPSEC key engine->Crypto IKMP:KEY_ENG_NOTIFY_INTF",
      "details": {
        "session_id": 0,
        "kmi_direction": "Sent",
        "kmi_source": "IPSEC key engine",
        "kmi_destination": "Crypto IKMP",
        "kmi_type": "KEY_ENG_NOTIFY_INTF"
      }
    },
    {
      "timestamp": "Apr  4 00:10:52.813",
      "event_type": "IPSEC-EVENT:IPSEC-CREATE-SA",
      "message": "SESSION ID:0, sa create : (sa) sa_dest= 30.1.1.1, sa_proto= 50, sa_spi= 0xC5C89787(3318257543), sa_trans= esp-aes esp-sha-hmac , sa_conn_id= 2023, sa_lifetime(k/sec)= (4608000/3600)",
      "details": {
        "session_id": 0,
        "sa_action": "create",
        "sa_dest": "30.1.1.1",
        "sa_proto": 50,
        "sa_spi": "0xC5C89787(3318257543)",
        "sa_trans": "esp-aes esp-sha-hmac",
        "sa_conn_id": 2023,
        "sa_lifetime_k": 4608000,
        "sa_lifetime_sec": 3600
      }
    },
    {
      "timestamp": "Apr  4 00:10:52.814",
      "event_type": "IPSEC-EVENT:IPSEC-CREATE-SA",
      "message": "SESSION ID:0, sa create : (sa),  loc: 30.1.1.1, rem: 30.1.1.2, l_proxy: 0.0.0.0/0/256, r_proxy: 0.0.0.0/0/256",
      "details": {
        "session_id": 0,
        "sa_action": "create",
        "loc": "30.1.1.1",
        "rem": "30.1.1.2",
        "l_proxy": "0.0.0.0/0/256",
        "r_proxy": "0.0.0.0/0/256"
      }
    },
    {
      "timestamp": "Apr  4 00:10:52.814",
      "event_type": "IPSEC-EVENT:IPSEC-CREATE-SA",
      "message": "SESSION ID:0, sa create : (sa) sa_dest= 30.1.1.2, sa_proto= 50, sa_spi= 0xFE24CD35(4263824693), sa_trans= esp-aes esp-sha-hmac , sa_conn_id= 2024, sa_lifetime(k/sec)= (4608000/3600)",
      "details": {
        "session_id": 0,
        "sa_action": "create",
        "sa_dest": "30.1.1.2",
        "sa_proto": 50,
        "sa_spi": "0xFE24CD35(4263824693)",
        "sa_trans": "esp-aes esp-sha-hmac",
        "sa_conn_id": 2024,
        "sa_lifetime_k": 4608000,
        "sa_lifetime_sec": 3600
      }
    },
    {
      "timestamp": "Apr  4 00:10:52.814",
      "event_type": "IPSEC-EVENT:IPSEC-CREATE-SA",
      "message": "SESSION ID:0, sa create : (sa),  loc: 30.1.1.1, rem: 30.1.1.2, l_proxy: 0.0.0.0/0/256, r_proxy: 0.0.0.0/0/256",
      "details": {
        "session_id": 0,
        "sa_action": "create",
        "loc": "30.1.1.1",
        "rem": "30.1.1.2",
        "l_proxy": "0.0.0.0/0/256",
        "r_proxy": "0.0.0.0/0/256"
      }
    },
    {
      "timestamp": "Apr  4 00:10:52.822",
      "event_type": "IPSEC-EVENT:IPSEC-SEND-KMI",
      "message": "SESSION ID:0, KMI Sent: IPSEC key engine->Crypto IKMP:KEY_ENG_NOTIFY_INCR_COUNT",
      "details": {
        "session_id": 0,
        "kmi_direction": "Sent",
        "kmi_source": "IPSEC key engine",
        "kmi_destination": "Crypto IKMP",
        "kmi_type": "KEY_ENG_NOTIFY_INCR_COUNT"
      }
    },
    {
      "timestamp": "Apr  4 00:10:52.902",
      "event_type": "IPSEC-EVENT:IPSEC-RECV-KMI",
      "message": "SESSION ID:0, KMI Received: Crypto IKMP->IPSEC key engine:KEY_MGR_DELETE_SAS, loc: 30.1.1.1, rem: 30.1.1.2, port loc/rem: 0/500, prot: DOI-3",
      "details": {
        "session_id": 0,
        "kmi_direction": "Received",
        "kmi_source": "Crypto IKMP",
        "kmi_destination": "IPSEC key engine",
        "kmi_type": "KEY_MGR_DELETE_SAS",
        "loc": "30.1.1.1",
        "rem": "30.1.1.2",
        "port_loc": 0,
        "port_rem": 500,
        "prot": "DOI-3"
      }
    },
    {
      "timestamp": "Apr  4 00:10:52.902",
      "event_type": "IPSEC-EVENT:IPSEC-DELETE-SA",
      "message": "SESSION ID:0, sa delete : (sa) sa_dest = 30.1.1.1, sa_proto = 50, sa_spi = 0xC5C89787(3318257543), sa_trans = esp-aes esp-sha-hmac , sa_conn_id = 2023, sa_lifetime(k/sec) = (4608000/3600)",
      "details": {
        "session_id": 0,
        "sa_action": "delete",
        "sa_dest": "30.1.1.1",
        "sa_proto": 50,
        "sa_spi": "0xC5C89787(3318257543)",
        "sa_trans": "esp-aes esp-sha-hmac",
        "sa_conn_id": 2023,
        "sa_lifetime_k": 4608000,
        "sa_lifetime_sec": 3600
      }
    },
    {
      "timestamp": "Apr  4 00:10:52.902",
      "event_type": "IPSEC-EVENT:IPSEC-DELETE-SA",
      "message": "SESSION ID:0, sa delete : (sa),  loc: 30.1.1.1, rem: 30.1.1.2, l_proxy: 0.0.0.0/0/256, r_proxy: 0.0.0.0/0/256",
      "details": {
        "session_id": 0,
        "sa_action": "delete",
        "loc": "30.1.1.1",
        "rem": "30.1.1.2",
        "l_proxy": "0.0.0.0/0/256",
        "r_proxy": "0.0.0.0/0/256"
      }
    },
    {
      "timestamp": "Apr  4 00:10:52.902",
      "event_type": "IPSEC-EVENT:IPSEC-DELETE-SA",
      "message": "SESSION ID:0, sa delete : (sa) sa_dest = 30.1.1.2, sa_proto = 50, sa_spi = 0xFE24CD35(4263824693), sa_trans = esp-aes esp-sha-hmac , sa_conn_id = 2024, sa_lifetime(k/sec) = (4608000/3600)",
      "details": {
        "session_id": 0,
        "sa_action": "delete",
        "sa_dest": "30.1.1.2",
        "sa_proto": 50,
        "sa_spi": "0xFE24CD35(4263824693)",
        "sa_trans": "esp-aes esp-sha-hmac",
        "sa_conn_id": 2024,
        "sa_lifetime_k": 4608000,
        "sa_lifetime_sec": 3600
      }
    },
    {
      "timestamp": "Apr  4 00:10:52.902",
      "event_type": "IPSEC-EVENT:IPSEC-DELETE-SA",
      "message": "SESSION ID:0, sa delete : (sa),  loc: 30.1.1.1, rem: 30.1.1.2, l_proxy: 0.0.0.0/0/256, r_proxy: 0.0.0.0/0/256",
      "details": {
        "session_id": 0,
        "sa_action": "delete",
        "loc": "30.1.1.1",
        "rem": "30.1.1.2",
        "l_proxy": "0.0.0.0/0/256",
        "r_proxy": "0.0.0.0/0/256"
      }
    },
    {
      "timestamp": "Apr  4 00:10:52.902",
      "event_type": "IPSEC-EVENT:IPSEC-SEND-KMI",
      "message": "SESSION ID:0, KMI Sent: IPSEC key engine->Crypto IKMP:KEY_ENG_NOTIFY_DECR_COUNT",
      "details": {
        "session_id": 0,
        "kmi_direction": "Sent",
        "kmi_source": "IPSEC key engine",
        "kmi_destination": "Crypto IKMP",
        "kmi_type": "KEY_ENG_NOTIFY_DECR_COUNT"
      }
    },
    {
      "timestamp": "Apr  4 00:10:52.906",
      "event_type": "IPSEC-EVENT:IPSEC-RECV-KMI",
      "message": "SESSION ID:0, KMI Received: Crypto IKMP->IPSEC key engine:KEY_MGR_SESSION_CLOSED, loc: 30.1.1.1, rem: 30.1.1.2, port loc/rem: 500/500",
      "details": {
        "session_id": 0,
        "kmi_direction": "Received",
        "kmi_source": "Crypto IKMP",
        "kmi_destination": "IPSEC key engine",
        "kmi_type": "KEY_MGR_SESSION_CLOSED",
        "loc": "30.1.1.1",
        "rem": "30.1.1.2",
        "port_loc": 500,
        "port_rem": 500
      }
    },
    {
      "timestamp": "Apr  4 00:10:53.238",
      "event_type": "IPSEC-EVENT:IPSEC-RECV-KMI",
      "message": "SESSION ID:0, KMI Received: Crypto IKMP->IPSEC key engine:KEY_MGR_CLEAR_ENDPT_SAS, loc: 30.1.1.1, rem: 30.1.1.2, port loc/rem: 500/500, prot: DOI-0",
      "details": {
        "session_id": 0,
        "kmi_direction": "Received",
        "kmi_source": "Crypto IKMP",
        "kmi_destination": "IPSEC key engine",
        "kmi_type": "KEY_MGR_CLEAR_ENDPT_SAS",
        "loc": "30.1.1.1",
        "rem": "30.1.1.2",
        "port_loc": 500,
        "port_rem": 500,
        "prot": "DOI-0"
      }
    },
    {
      "timestamp": "Apr  4 00:10:53.238",
      "event_type": "IPSEC-EVENT:IPSEC-RECV-KMI",
      "message": "SESSION ID:0, KMI Received: Crypto IKMP->IPSEC key engine:KEY_MGR_CREATE_IPSEC_SAS, loc: 30.1.1.1, rem: 30.1.1.2, l_proxy: 0.0.0.0/500/256, r_proxy: 0.0.0.0/500/256",
      "details": {
        "session_id": 0,
        "kmi_direction": "Received",
        "kmi_source": "Crypto IKMP",
        "kmi_destination": "IPSEC key engine",
        "kmi_type": "KEY_MGR_CREATE_IPSEC_SAS",
        "loc": "30.1.1.1",
        "rem": "30.1.1.2",
        "l_proxy": "0.0.0.0/500/256",
        "r_proxy": "0.0.0.0/500/256"
      }
    },
    {
      "timestamp": "Apr  4 00:10:53.238",
      "event_type": "IPSEC-EVENT:IPSEC-SEND-KMI",
      "message": "SESSION ID:0, KMI Sent: IPSEC key engine->Crypto IKMP:KEY_ENG_NOTIFY_QOS_GROUP, loc: UNKNOWN, rem: UNKNOWN, port loc/rem: 0/0, prot: 0",
      "details": {
        "session_id": 0,
        "kmi_direction": "Sent",
        "kmi_source": "IPSEC key engine",
        "kmi_destination": "Crypto IKMP",
        "kmi_type": "KEY_ENG_NOTIFY_QOS_GROUP",
        "loc": "UNKNOWN",
        "rem": "UNKNOWN",
        "port_loc": 0,
        "port_rem": 0,
        "prot": "0"
      }
    },
    {
      "timestamp": "Apr  4 00:10:53.238",
      "event_type": "IPSEC-EVENT:IPSEC-SEND-KMI",
      "message": "SESSION ID:0, KMI Sent: IPSEC key engine->Crypto IKMP:KEY_ENG_NOTIFY_INTF",
      "details": {
        "session_id": 0,
        "kmi_direction": "Sent",
        "kmi_source": "IPSEC key engine",
        "kmi_destination": "Crypto IKMP",
        "kmi_type": "KEY_ENG_NOTIFY_INTF"
      }
    },
    {
      "timestamp": "Apr  4 00:10:53.238",
      "event_type": "IPSEC-EVENT:IPSEC-CREATE-SA",
      "message": "SESSION ID:0, sa create : (sa) sa_dest= 30.1.1.1, sa_proto= 50, sa_spi= 0x3B9191B7(999395767), sa_trans= esp-aes esp-sha-hmac , sa_conn_id= 2025, sa_lifetime(k/sec)= (4608000/3600)",
      "details": {
        "session_id": 0,
        "sa_action": "create",
        "sa_dest": "30.1.1.1",
        "sa_proto": 50,
        "sa_spi": "0x3B9191B7(999395767)",
        "sa_trans": "esp-aes esp-sha-hmac",
        "sa_conn_id": 2025,
        "sa_lifetime_k": 4608000,
        "sa_lifetime_sec": 3600
      }
    },
    {
      "timestamp": "Apr  4 00:10:53.238",
      "event_type": "IPSEC-EVENT:IPSEC-CREATE-SA",
      "message": "SESSION ID:0, sa create : (sa),  loc: 30.1.1.1, rem: 30.1.1.2, l_proxy: 0.0.0.0/0/256, r_proxy: 0.0.0.0/0/256",
      "details": {
        "session_id": 0,
        "sa_action": "create",
        "loc": "30.1.1.1",
        "rem": "30.1.1.2",
        "l_proxy": "0.0.0.0/0/256",
        "r_proxy": "0.0.0.0/0/256"
      }
    },
    {
      "timestamp": "Apr  4 00:10:53.238",
      "event_type": "IPSEC-EVENT:IPSEC-CREATE-SA",
      "message": "SESSION ID:0, sa create : (sa) sa_dest= 30.1.1.2, sa_proto= 50, sa_spi= 0xDCBBB53F(3703289151), sa_trans= esp-aes esp-sha-hmac , sa_conn_id= 2026, sa_lifetime(k/sec)= (4608000/3600)",
      "details": {
        "session_id": 0,
        "sa_action": "create",
        "sa_dest": "30.1.1.2",
        "sa_proto": 50,
        "sa_spi": "0xDCBBB53F(3703289151)",
        "sa_trans": "esp-aes esp-sha-hmac",
        "sa_conn_id": 2026,
        "sa_lifetime_k": 4608000,
        "sa_lifetime_sec": 3600
      }
    },
    {
      "timestamp": "Apr  4 00:10:53.238",
      "event_type": "IPSEC-EVENT:IPSEC-CREATE-SA",
      "message": "SESSION ID:0, sa create : (sa),  loc: 30.1.1.1, rem: 30.1.1.2, l_proxy: 0.0.0.0/0/256, r_proxy: 0.0.0.0/0/256",
      "details": {
        "session_id": 0,
        "sa_action": "create",
        "loc": "30.1.1.1",
        "rem": "30.1.1.2",
        "l_proxy": "0.0.0.0/0/256",
        "r_proxy": "0.0.0.0/0/256"
      }
    },
    {
      "timestamp": "Apr  4 00:10:53.242",
      "event_type": "IPSEC-EVENT:IPSEC-SEND-KMI",
      "message": "SESSION ID:0, KMI Sent: IPSEC key engine->Crypto IKMP:KEY_ENG_NOTIFY_INCR_COUNT",
      "details": {
        "session_id": 0,
        "kmi_direction": "Sent",
        "kmi_source": "IPSEC key engine",
        "kmi_destination": "Crypto IKMP",
        "kmi_type": "KEY_ENG_NOTIFY_INCR_COUNT"
      }
    },
    {
      "timestamp": "Apr  4 00:10:53.250",
      "event_type": "IPSEC-EVENT:IPSEC-RECV-KMI",
      "message": "SESSION ID:0, KMI Received: Crypto IKMP->IPSEC key engine:KEY_MGR_SA_ENABLE_OUTBOUND, loc: 30.1.1.1, rem: 30.1.1.2, prot: 3",
      "details": {
        "session_id": 0,
        "kmi_direction": "Received",
        "kmi_source": "Crypto IKMP",
        "kmi_destination": "IPSEC key engine",
        "kmi_type": "KEY_MGR_SA_ENABLE_OUTBOUND",
        "loc": "30.1.1.1",
        "rem": "30.1.1.2",
        "prot": "3"
      }
    }
  ]
}
