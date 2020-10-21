expected_output = {
    "profile_name": {
        "lizzard_Fabric_F_90c76354": {
            "wlan_id": 17,
            "ssid": "lizzard",
            "config": [
                "radio dot11a",
                "security ft",
                "security wpa akm ft dot1x",
                "security dot1x authentication-list dnac-cts-list",
                "no shutdown",
            ],
        },
        "internet_Fabric_F_522662da": {
            "wlan_id": 19,
            "ssid": "internet",
            "config": [
                "mac-filtering default",
                "no security ft adaptive",
                "no security wpa",
                "no security wpa wpa2 ciphers aes",
                "no security wpa akm dot1x",
                "no shutdown",
            ],
        },
        "lizzard_l_Fabric_F_0e98c2cd": {
            "wlan_id": 18,
            "ssid": "lizzard_2",
            "config": [
                "no broadcast-ssid",
                "radio dot11bg",
                "security dot1x authentication-list dnac-cts-list",
                "no shutdown",
            ],
        },
        "alfa_Global_F_953d5d2b": {
            "wlan_id": 17,
            "ssid": "alfa",
            "config": [
                "radio dot11a",
                "security ft over-the-ds",
                "security dot1x authentication-list dnac-cts-list",
                "no shutdown",
            ],
        },
    }
}