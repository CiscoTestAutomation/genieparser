expected_output = {
        'event_trace': {
            'event': {
                1: {
                    'event_message': 'Trustpoint- client:Manual enrollment for trustpoint',
                    'timestamp': 'Jun  9 13:08:58.289',
    
            },
            10: {
                    'event_message': 'Trustpoint- client:ID Certificate will expire in 0 Days 0 hours 19 mins 59 secs at 2025-06-09T18:58:58Z.\nIssuer-name  : cn=RCA1 C=pki\nSubject-name : hostname=pki-reg4,cn=R1 C=pki\nSerial-number: 03\nAuto-Renewal : Not Enabled',
                    'timestamp': 'Jun  9 13:08:59.923',
    
            },
            11: {
                    'event_message': 'Trustpoint- client:Started shadow timer for 28304632 seconds.\nIssuer-name  : cn=RCA1 C=pki\nSubject-name : cn=RCA1 C=pki\nSerial-number: 02\nEnd-date     : 2026-06-08T18:38:51Z\nCSR Fingerprint MD5 : 0AD9955A6885213797DE145CBAB688EF\nCSR Fingerprint SHA1: 583381E9DDC3D287CC59BA96ED12AF917097D339\nCSR Fingerprint SHA2: 5DEB1BCCDE7ADB48448DAFD89996701ECDA17E30E3F3E532D6EC5B249752A195\nCSR Fingerprint (unsigned) MD5 : 5DC501B7C8E2987F4E4646B2C64F36A3\nIssuer-name  : cn=RCA1 C=pki\nSubject-name : unstructuredname=pki-reg4,cn=R1 C=pki\nSerial-number: 03\nEnd-date     : 2025-06-09T18:58:58Z\nIssuer-name  : cn=RCA1 C=pki\nSubject-name : hostname=pki-reg4,cn=R1 C=pki\nSerial-number: 03\nAuto-Renewal : Not Enabled\nNum of Unique Streams .. 1\nTotal UTF To Process ... 1\nTotal UTM To Process ... 37271\nUTM Process Filter ..... ios\nMRST Filter Rules ...... 48\nFirst UTM TimeStamp ............... 2025/06/09 15:21:24.750766751\nLast UTM TimeStamp ................ 2025/06/09 18:40:00.231755961\nUTM [Skipped / Rendered / Total] .. 37239 / 32 / 37271\nUTM [ENCODED] ..................... 32\nUTM [PLAIN TEXT] .................. 0\nUTM [DYN LIB] ..................... 0\nUTM [MODULE ID] ................... 0\nUTM [TDL TAN] ..................... 19\nUTM [APP CONTEXT] ................. 0\nUTM [MARKER] ...................... 0\nUTM [PCAP] ........................ 0\nUTM [LUID NOT FOUND] .............. 0\nUTM Level [EMERGENCY / ALERT / CRITICAL / ERROR] .. 0 / 0 / 0 / 0\nUTM Level [WARNING / NOTICE / INFO / DEBUG] ....... 2 / 30 / 0 / 0\nUTM Level [VERBOSE / NOISE / INVALID] ............. 0 / 0 / 0',
                    'timestamp': 'Jun  9 13:08:59.924',
    
            },
            2: {
                    'event_message': 'Trustpoint- client:Sending GetCACaps request with msg = GET /cgi-bin/pkiclient.exe?operation=GetCACaps&message=client HTTP/1.0',
                    'timestamp': 'Jun  9 13:08:59.351',
    
            },
            3: {
                    'event_message': 'Trustpoint- client:Capabilities received : GET NEXT CA CERT, RENEWAL, SHA1, SHA256, SHA384, SHA512,',
                    'timestamp': 'Jun  9 13:08:59.375',
    
            },
            4: {
                    'event_message': 'Trustpoint- client:\nCSR Fingerprint MD5 : 0AD9955A6885213797DE145CBAB688EF\nCSR Fingerprint SHA1: 583381E9DDC3D287CC59BA96ED12AF917097D339\nCSR Fingerprint SHA2: 5DEB1BCCDE7ADB48448DAFD89996701ECDA17E30E3F3E532D6EC5B249752A195',
                    'timestamp': 'Jun  9 13:08:59.391',
    
            },
            5: {
                    'event_message': 'Trustpoint- client:\nCSR Fingerprint (unsigned) MD5 : 5DC501B7C8E2987F4E4646B2C64F36A3',
                    'timestamp': 'Jun  9 13:08:59.391',
    
            },
            6: {
                    'event_message': 'Trustpoint- client:Client sending PKCSReq',
                    'timestamp': 'Jun  9 13:08:59.425',
    
            },
            7: {
                    'event_message': 'Trustpoint- client:Received pki message.',
                    'timestamp': 'Jun  9 13:08:59.906',
    
            },
            8: {
                    'event_message': 'Trustpoint- client:Client received CertRep - GRANTED.',
                    'timestamp': 'Jun  9 13:08:59.907',
    
            },
            9: {
                    'event_message': 'Trustpoint- client:An ID certificate has been installed under\nIssuer-name  : cn=RCA1 C=pki\nSubject-name : unstructuredname=pki-reg4,cn=R1 C=pki\nSerial-number: 03\nEnd-date     : 2025-06-09T18:58:58Z',
                    'timestamp': 'Jun  9 13:08:59.921',
    
            },
        },
    },
}