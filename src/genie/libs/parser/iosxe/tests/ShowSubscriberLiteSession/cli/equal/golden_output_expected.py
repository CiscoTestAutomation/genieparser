expected_output = {
    "total_sessions" : 1,
    "lite_sessions" : {
        1: {
            "src_ip" : "100.0.0.10",
            "vrf" : "Default",
            "s_vrf":"Default",
            "interface":"Te1/0/3.100",
            "pbhk":"0.0.0.0:0" },
        2: {
            "src_ip" : "100.0.0.11",
            "vrf" : "Default",
            "s_vrf":"Default",
            "interface":"Te1/0/3.200",
            "pbhk":"0.0.0.0:0"
        }
    }
}

