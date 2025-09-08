expected_output = {
    "exit_path_table": {
        "status": "enable",
        "current_entry": 2,
        "deleted": 0,
        "max_allow": 50,
    },
    "errors": {
        12: {
            "message": "Detected an invalid IKE SPI",
            "traceback": [
                "1#9de6b87c8b70a12e54d1e886d6f158f7  :AAAACA784000+129007E0 :AAAACA784000+1294E0C0 :AAAACA784000+1294"
            ],
        },
        8: {
            "message": "A supplied parameter is incorrect",
            "traceback": [
                "1#9de6b87c8b70a12e54d1e886d6f158f7  :AAAACA784000+129007E0 :AAAACA784000+129C73FC :AAAACA784000+1290"
            ],
        },
    },
}