expected_output = {
    'event_trace': {
        'events': {
            1: {
                'timestamp': 'Apr  4 00:16:59.484',
                'sa_id': 2,
                'session_id': 1,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': 'Sending DELETE INFO message for IPsec SA [SPI: 0x28DC063C]',
                'spi': '0x28DC063C'
            },
            2: {
                'timestamp': 'Apr  4 00:16:59.484',
                'sa_id': 2,
                'session_id': 1,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': '(I) Sending IKEv2 INFORMATIONAL Exchange REQUEST',
                'direction': 'I',
                'exchange_type': 'INFORMATIONAL'
            },
            3: {
                'timestamp': 'Apr  4 00:16:59.484',
                'sa_id': 2,
                'session_id': 1,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': '(I) IKEv2 INFORMATIONAL Exchange Contains: DELETE',
                'direction': 'I',
                'exchange_type': 'INFORMATIONAL'
            },
            4: {
                'timestamp': 'Apr  4 00:16:59.484',
                'sa_id': 2,
                'session_id': 1,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': 'Sending DELETE INFO message for IKEv2 SA [ISPI: 0x52C79670608A3068 RSPI: 0x0063AAED5563FDAE]',
                'ispi': '0x52C79670608A3068',
                'rspi': '0x0063AAED5563FDAE'
            },
            5: {
                'timestamp': 'Apr  4 00:16:59.484',
                'sa_id': 2,
                'session_id': 1,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': '(I) Sending IKEv2 INFORMATIONAL Exchange REQUEST',
                'direction': 'I',
                'exchange_type': 'INFORMATIONAL'
            },
            6: {
                'timestamp': 'Apr  4 00:16:59.484',
                'sa_id': 2,
                'session_id': 1,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': '(I) IKEv2 INFORMATIONAL Exchange Contains: DELETE',
                'direction': 'I',
                'exchange_type': 'INFORMATIONAL'
            },
            7: {
                'timestamp': 'Apr  4 00:16:59.484',
                'sa_id': 2,
                'session_id': 1,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': '(I) Received IKEv2 INFORMATIONAL Exchange RESPONSE',
                'direction': 'I',
                'exchange_type': 'INFORMATIONAL'
            },
            8: {
                'timestamp': 'Apr  4 00:16:59.484',
                'sa_id': 2,
                'session_id': 1,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': '(I) IKEv2 INFORMATIONAL Exchange Contains: DELETE',
                'direction': 'I',
                'exchange_type': 'INFORMATIONAL'
            },
            9: {
                'timestamp': 'Apr  4 00:17:00.424',
                'sa_id': 1,
                'session_id': 2,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': '(I) Sending IKEv2 IKE_SA_INIT Exchange REQUEST',
                'direction': 'I',
                'exchange_type': 'IKE_SA_INIT'
            },
            10: {
                'timestamp': 'Apr  4 00:17:00.432',
                'sa_id': 1,
                'session_id': 2,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': '(I) Received IKEv2 IKE_SA_INIT Exchange RESPONSE',
                'direction': 'I',
                'exchange_type': 'IKE_SA_INIT'
            },
            11: {
                'timestamp': 'Apr  4 00:17:00.436',
                'sa_id': 1,
                'session_id': 2,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': 'Completed SA init exchange'
            },
            12: {
                'timestamp': 'Apr  4 00:17:00.436',
                'sa_id': 1,
                'session_id': 2,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': '(I) Sending IKEv2 IKE_AUTH Exchange REQUEST',
                'direction': 'I',
                'exchange_type': 'IKE_AUTH'
            },
            13: {
                'timestamp': 'Apr  4 00:17:00.436',
                'sa_id': 1,
                'session_id': 2,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': '(I) Received IKEv2 IKE_AUTH Exchange RESPONSE',
                'direction': 'I',
                'exchange_type': 'IKE_AUTH'
            },
            14: {
                'timestamp': 'Apr  4 00:17:00.436',
                'sa_id': 1,
                'session_id': 2,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': 'Session with IKE ID PAIR(30.1.1.2 , 30.1.1.1) is UP',
                'ike_id_pair': '30.1.1.2 , 30.1.1.1'
            },
            15: {
                'timestamp': 'Apr  4 00:17:00.596',
                'sa_id': 1,
                'session_id': 2,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': '(R) Received IKEv2 INFORMATIONAL Exchange REQUEST',
                'direction': 'R',
                'exchange_type': 'INFORMATIONAL'
            },
            16: {
                'timestamp': 'Apr  4 00:17:00.596',
                'sa_id': 1,
                'session_id': 2,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': '(R) IKEv2 INFORMATIONAL Exchange Contains: DELETE',
                'direction': 'R',
                'exchange_type': 'INFORMATIONAL'
            },
            17: {
                'timestamp': 'Apr  4 00:17:00.596',
                'sa_id': 1,
                'session_id': 2,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': '(R) Sending IKEv2 INFORMATIONAL Exchange RESPONSE',
                'direction': 'R',
                'exchange_type': 'INFORMATIONAL'
            },
            18: {
                'timestamp': 'Apr  4 00:17:00.596',
                'sa_id': 1,
                'session_id': 2,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': '(R) IKEv2 INFORMATIONAL Exchange Contains: DELETE',
                'direction': 'R',
                'exchange_type': 'INFORMATIONAL'
            },
            19: {
                'timestamp': 'Apr  4 00:17:00.600',
                'sa_id': 1,
                'session_id': 2,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': 'Processing DELETE INFO message for IPsec SA [SPI: 0x335DA6C6]',
                'spi': '0x335DA6C6'
            },
            20: {
                'timestamp': 'Apr  4 00:17:00.600',
                'sa_id': 1,
                'session_id': 2,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': '(R) Received IKEv2 INFORMATIONAL Exchange REQUEST',
                'direction': 'R',
                'exchange_type': 'INFORMATIONAL'
            },
            21: {
                'timestamp': 'Apr  4 00:17:00.600',
                'sa_id': 1,
                'session_id': 2,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': '(R) IKEv2 INFORMATIONAL Exchange Contains: NOTIFY',
                'direction': 'R',
                'exchange_type': 'INFORMATIONAL'
            },
            22: {
                'timestamp': 'Apr  4 00:17:00.600',
                'sa_id': 1,
                'session_id': 2,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': '(R) IKEv2 INFORMATIONAL Exchange Contains: DELETE',
                'direction': 'R',
                'exchange_type': 'INFORMATIONAL'
            },
            23: {
                'timestamp': 'Apr  4 00:17:00.600',
                'sa_id': 1,
                'session_id': 2,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': '(R) Sending IKEv2 INFORMATIONAL Exchange RESPONSE',
                'direction': 'R',
                'exchange_type': 'INFORMATIONAL'
            },
            24: {
                'timestamp': 'Apr  4 00:17:00.600',
                'sa_id': 1,
                'session_id': 2,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': 'Processing DELETE INFO message for IKEv2 SA [ISPI: 0xD4821BB75E54AE19 RSPI: 0x6CED320C3A8B8B2F]',
                'ispi': '0xD4821BB75E54AE19',
                'rspi': '0x6CED320C3A8B8B2F'
            },
            25: {
                'timestamp': 'Apr  4 00:17:00.840',
                'sa_id': 1,
                'session_id': 3,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': '(R) Received IKEv2 IKE_SA_INIT Exchange REQUEST',
                'direction': 'R',
                'exchange_type': 'IKE_SA_INIT'
            },
            26: {
                'timestamp': 'Apr  4 00:17:00.848',
                'sa_id': 1,
                'session_id': 3,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': '(R) Sending IKEv2 IKE_SA_INIT Exchange RESPONSE',
                'direction': 'R',
                'exchange_type': 'IKE_SA_INIT'
            },
            27: {
                'timestamp': 'Apr  4 00:17:00.848',
                'sa_id': 1,
                'session_id': 3,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': 'Completed SA init exchange'
            },
            28: {
                'timestamp': 'Apr  4 00:17:00.848',
                'sa_id': 1,
                'session_id': 3,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': '(R) Received IKEv2 IKE_AUTH Exchange REQUEST',
                'direction': 'R',
                'exchange_type': 'IKE_AUTH'
            },
            29: {
                'timestamp': 'Apr  4 00:17:00.852',
                'sa_id': 1,
                'session_id': 3,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': '(R) Sending IKEv2 IKE_AUTH Exchange RESPONSE',
                'direction': 'R',
                'exchange_type': 'IKE_AUTH'
            },
            30: {
                'timestamp': 'Apr  4 00:17:00.852',
                'sa_id': 1,
                'session_id': 3,
                'remote': '30.1.1.2/500',
                'local': '30.1.1.1/500',
                'event_message': 'Session with IKE ID PAIR(30.1.1.2 , 30.1.1.1) is UP',
                'ike_id_pair': '30.1.1.2 , 30.1.1.1'
            }
        }
    }
}
