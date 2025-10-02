expected_output = {
    "event_trace": {
        "pki_event": {
            "events": [
                {
                    "timestamp": "Apr  3 23:53:30.374",
                    "message": "EST client initialized.",
                },
                {
                    "timestamp": "Apr  3 23:53:50.585",
                    "message": "EST client process started.",
                },
                {
                    "timestamp": "Apr  3 23:56:35.210",
                    "message": "Running configuration saved to NVRAM",
                },
            ]
        },
        "pki_internal_event": {
            "status": "Tracing currently disabled, from exec command"
        },
        "pki_error": {
            "events": [
                {
                    "timestamp": "Apr  3 23:53:50.581",
                    "message": "PKI timers have not been initialized due to non-authoritative system clock. Ensure system clock is configured/updated.",
                    "traceback": "1#3c677f5693d4a1da4989c9342fd445a2 :AAAACD000000+B371FD8  :AAAACD000000+6CA9C90  :AAAACD000000+6CAFFD4  :AAAACD000000+802A094  :AAAACD000000+8029AEC  :AAAACD000000+7F8E788  :AAAACD000000+896EBD8",
                }
            ]
        },
        "ikev2_event": {
            "status": "Tracing currently disabled, from exec command"
        },
        "ikev2_internal_event": {},
        "ikev2_error": {},
        "ikev2_exception": {},
        "ipsec_event": {
            "status": "Tracing currently disabled, from exec command"
        },
        "ipsec_error": {},
        "ipsec_exception": {
            "interrupt_context_allocation_count": 0
        },
    }
}