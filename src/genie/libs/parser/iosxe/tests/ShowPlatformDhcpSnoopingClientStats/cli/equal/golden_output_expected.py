expected_output = {
    "client_mac":"44AE.25D3.6006",
    "packet_trace":[
        {
            "timestamp":"2025/03/19 11:08:53.012",
            "destination_mac":"FFFF.FFFF.FFFF",
            "destination_ip":"255.255.255.255",
            "vlan":100,
            "message":"DHCPDISCOVER(B)",
            "handler_action":"PUNT:RECEIVED"
        },
        {
            "timestamp":"2025/03/19 11:08:53.012",
            "destination_mac":"FFFF.FFFF.FFFF",
            "destination_ip":"255.255.255.255",
            "vlan":100,
            "message":"DHCPDISCOVER(B)",
            "handler_action":"PUNT:TO_DHCPSN"
        },
        {
            "timestamp":"2025/03/19 11:08:53.022",
            "destination_mac":"FFFF.FFFF.FFFF",
            "destination_ip":"255.255.255.255",
            "vlan":100,
            "message":"DHCPDISCOVER(B)",
            "handler_action":"BRIDGE:RECEIVED"
        },
        {
            "timestamp":"2025/03/19 11:08:53.022",
            "destination_mac":"FFFF.FFFF.FFFF",
            "destination_ip":"255.255.255.255",
            "vlan":100,
            "message":"DHCPDISCOVER(B)",
            "handler_action":"BRIDGE:TO_INJECT"
        },
        {
            "timestamp":"2025/03/19 11:08:53.022",
            "destination_mac":"FFFF.FFFF.FFFF",
            "destination_ip":"255.255.255.255",
            "vlan":100,
            "message":"DHCPDISCOVER(B)",
            "handler_action":"L2INJECT:TO_FWD"
        },
        {
            "timestamp":"2025/03/19 11:08:53.024",
            "destination_mac":"FFFF.FFFF.FFFF",
            "destination_ip":"255.255.255.255",
            "vlan":100,
            "message":"DHCPOFFER(B)",
            "handler_action":"PUNT:RECEIVED"
        },
        {
            "timestamp":"2025/03/19 11:08:53.024",
            "destination_mac":"FFFF.FFFF.FFFF",
            "destination_ip":"255.255.255.255",
            "vlan":100,
            "message":"DHCPOFFER(B)",
            "handler_action":"PUNT:TO_DHCPSN"
        },
        {
            "timestamp":"2025/03/19 11:08:53.033",
            "destination_mac":"FFFF.FFFF.FFFF",
            "destination_ip":"255.255.255.255",
            "vlan":100,
            "message":"DHCPOFFER(B)",
            "handler_action":"PUNT:RECEIVED"
        },
        {
            "timestamp":"2025/03/19 11:08:53.033",
            "destination_mac":"FFFF.FFFF.FFFF",
            "destination_ip":"255.255.255.255",
            "vlan":100,
            "message":"DHCPOFFER(B)",
            "handler_action":"PUNT:TO_DHCPSN"
        },
        {
            "timestamp":"2025/03/19 11:08:53.061",
            "destination_mac":"FFFF.FFFF.FFFF",
            "destination_ip":"255.255.255.255",
            "vlan":100,
            "message":"DHCPREQUEST(B)",
            "handler_action":"PUNT:RECEIVED"
        },
        {
            "timestamp":"2025/03/19 11:08:53.061",
            "destination_mac":"FFFF.FFFF.FFFF",
            "destination_ip":"255.255.255.255",
            "vlan":100,
            "message":"DHCPREQUEST(B)",
            "handler_action":"PUNT:TO_DHCPSN"
        },
        {
            "timestamp":"2025/03/19 11:08:53.072",
            "destination_mac":"FFFF.FFFF.FFFF",
            "destination_ip":"255.255.255.255",
            "vlan":100,
            "message":"DHCPREQUEST(B)",
            "handler_action":"BRIDGE:RECEIVED"
        },
        {
            "timestamp":"2025/03/19 11:08:53.072",
            "destination_mac":"FFFF.FFFF.FFFF",
            "destination_ip":"255.255.255.255",
            "vlan":100,
            "message":"DHCPREQUEST(B)",
            "handler_action":"BRIDGE:TO_INJECT"
        },
        {
            "timestamp":"2025/03/19 11:08:53.072",
            "destination_mac":"FFFF.FFFF.FFFF",
            "destination_ip":"255.255.255.255",
            "vlan":100,
            "message":"DHCPREQUEST(B)",
            "handler_action":"L2INJECT:TO_FWD"
        },
        {
            "timestamp":"2025/03/19 11:08:53.074",
            "destination_mac":"FFFF.FFFF.FFFF",
            "destination_ip":"255.255.255.255",
            "vlan":100,
            "message":"DHCPACK(B)",
            "handler_action":"PUNT:RECEIVED"
        },
        {
            "timestamp":"2025/03/19 11:08:53.074",
            "destination_mac":"FFFF.FFFF.FFFF",
            "destination_ip":"255.255.255.255",
            "vlan":100,
            "message":"DHCPACK(B)",
            "handler_action":"PUNT:TO_DHCPSN"
        },
        {
            "timestamp":"2025/03/19 11:08:53.083",
            "destination_mac":"FFFF.FFFF.FFFF",
            "destination_ip":"255.255.255.255",
            "vlan":100,
            "message":"DHCPACK(B)",
            "handler_action":"PUNT:RECEIVED"
        },
        {
            "timestamp":"2025/03/19 11:08:53.083",
            "destination_mac":"FFFF.FFFF.FFFF",
            "destination_ip":"255.255.255.255",
            "vlan":100,
            "message":"DHCPACK(B)",
            "handler_action":"PUNT:TO_DHCPSN"
        }
    ]
}