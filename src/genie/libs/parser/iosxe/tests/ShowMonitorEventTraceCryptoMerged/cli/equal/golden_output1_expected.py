expected_output= {
    "events": [
      {
        "timestamp": "Apr  3 23:53:30.376",
        "event_type": "pki_event",
        "message": "EST client initialized."
      },
      {
        "timestamp": "Apr  3 23:53:50.584",
        "event_type": "pki_error",
        "message": "PKI timers have not been initialized due to non-authoritative system clock. Ensure system clock is configured/updated.",
        "traceback": "1#3c677f5693d4a1da4989c9342fd445a2 :AAAACD000000+B371FD8  :AAAACD000000+6CA9C90  :AAAACD000000+6CAFFD4  :AAAACD000000+802A094  :AAAACD000000+8029AEC  :AAAACD000000+7F8E788  :AAAACD000000+896EBD8"
      },
      {
        "timestamp": "Apr  3 23:53:50.588",
        "event_type": "pki_event",
        "message": "EST client process started."
      },
      {
        "timestamp": "Apr  3 23:56:35.212",
        "event_type": "pki_event",
        "message": "Running configuration saved to NVRAM"
      }
    ]
}
