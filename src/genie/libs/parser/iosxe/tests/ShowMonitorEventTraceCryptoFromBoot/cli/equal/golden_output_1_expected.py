expected_output = {
    "event_trace": {
        "pki_event": {},
        "pki_internal_event": {
            "status": "Tracing currently disabled, from exec command"
        },
        "pki_error": {},
        "ikev2_event": {
            "events": [
                {
                    "timestamp": "Aug 11 09:10:26.036",
                    "message": "SA ID:1 SESSION ID:1 Remote: 40.181.251.101/500 Local: 40.185.80.1/500  (I) Sending IKEv2 IKE_SA_INIT Exchange REQUEST",
                },
                {
                    "timestamp": "Aug 11 09:10:26.043",
                    "message": "SA ID:2 SESSION ID:2 Remote: 40.181.251.101/500 Local: 40.182.80.1/500  (I) Sending IKEv2 IKE_SA_INIT Exchange REQUEST",
                },
                {
                    "timestamp": "Aug 11 09:10:26.050",
                    "message": "SA ID:3 SESSION ID:3 Remote: 40.181.251.101/500 Local: 40.183.80.1/500  (I) Sending IKEv2 IKE_SA_INIT Exchange REQUEST",
                },
            ]
        },
        "ikev2_internal_event": {
            "events": [
                {
                    "timestamp": "Aug 11 09:10:26.035",
                    "message": "SA ID:0 SESSION ID:0    IKEV2-RECV-KMI: KMI Received: KEY_ENG_REQUEST_SAS, KMI source: IPSEC key engine, KMI dest: Crypto IKEv2, local: 40.185.80.1, remote: 40.181.251.101",
                },
                {
                    "timestamp": "Aug 11 09:10:26.036",
                    "message": "SA ID:0 SESSION ID:0    IKEV2_EVENT_QUEUE_KMI type:KEY_ENG_REQUEST_SAS",
                },
                {
                    "timestamp": "Aug 11 09:10:26.040",
                    "message": "SA ID:0 SESSION ID:0    IKEV2-RECV-KMI: KMI Received: KEY_ENG_REQUEST_SAS, KMI source: IPSEC key engine, KMI dest: Crypto IKEv2, local: 40.182.80.1, remote: 40.181.251.101",
                },
                {
                    "timestamp": "Aug 11 09:10:26.043",
                    "message": "SA ID:0 SESSION ID:0    IKEV2_EVENT_QUEUE_KMI type:KEY_ENG_REQUEST_SAS",
                },
                {
                    "timestamp": "Aug 11 09:10:26.047",
                    "message": "SA ID:0 SESSION ID:0    IKEV2-RECV-KMI: KMI Received: KEY_ENG_REQUEST_SAS, KMI source: IPSEC key engine, KMI dest: Crypto IKEv2, local: 40.183.80.1, remote: 40.181.251.101",
                },
                {
                    "timestamp": "Aug 11 09:10:26.050",
                    "message": "SA ID:0 SESSION ID:0    IKEV2_EVENT_QUEUE_KMI type:KEY_ENG_REQUEST_SAS",
                },
            ]
        },
        "ikev2_error": {},
        "ikev2_exception": {},
        "ipsec_event": {
            "events": [
                {
                    "timestamp": "Aug  8 18:17:29.901",
                    "message": "IPSEC-EVENT:IPSEC-DELETE-SA:  SESSION ID:0, sa delete : (sa) sa_dest = 418A::70:0:1, sa_proto = 50, sa_spi = 0x102(258), sa_trans = esp-gcm 256 , sa_conn_id = 2032, sa_lifetime(k/sec) = (0/809107524)",
                },
                {
                    "timestamp": "Aug  8 18:17:29.901",
                    "message": "IPSEC-EVENT:IPSEC-DELETE-SA:  SESSION ID:0, sa delete : (sa),  loc: 418A::80:0:1, rem: 418A::70:0:1, l_proxy: 418A::80:0:1/12346/256, r_proxy: 418A::70:0:1/12346/256",
                },
                {
                    "timestamp": "Aug  8 18:17:29.904",
                    "message": "IPSEC-EVENT:IPSEC-CREATE-SA:  SESSION ID:0, sa create : (sa) sa_dest= 418A::80:0:1, sa_proto= 50, sa_spi= 0x10A(266), sa_trans= esp-gcm 256 , sa_conn_id= 2037, sa_lifetime(k/sec)= (0/809107530)",
                },
            ]
        },
        "ipsec_error": {},
        "ipsec_exception": {
            "interrupt_context_allocation_count": 0
        },
    }
}