expected_output = {
    "security_policy_counts": {
        "root-logical-system": {
            "security_policy": [
                {
                    "index": "1",
                    "from_zone": "junos-global",
                    "to_zone": "junos-global",
                    "name": "GLOBAL-PERMIT-TRACE-IN",
                    "policy_hit_count": "78"
                },
                {
                    "index": "2",
                    "from_zone": "junos-global",
                    "to_zone": "junos-global",
                    "name": "GLOBAL-PERMIT-RADIUS-IN",
                    "policy_hit_count": "0"
                },
                {
                    "index": "3",
                    "from_zone": "junos-global",
                    "to_zone": "junos-global",
                    "name": "GLOBAL-PERMIT-NTP-IN",
                    "policy_hit_count": "0"
                },
                {
                    "index": "4",
                    "from_zone": "junos-global",
                    "to_zone": "junos-global",
                    "name": "GLOBAL-PERMIT-ICMP-IN",
                    "policy_hit_count": "3504"
                },
                {
                    "index": "5",
                    "from_zone": "junos-global",
                    "to_zone": "junos-global",
                    "name": "GLOBAL-PERMIT-SNMP-IN",
                    "policy_hit_count": "1"
                },
                {
                    "index": "6",
                    "from_zone": "junos-global",
                    "to_zone": "junos-global",
                    "name": "DEFAULT-DENY",
                    "policy_hit_count": "4567302"
                },
                {
                    "index": "7",
                    "from_zone": "junos-global",
                    "to_zone": "junos-global",
                    "name": "GLOBAL-PERMIT-DNS-IN",
                    "policy_hit_count": "0"
                },
                {
                    "index": "8",
                    "from_zone": "junos-global",
                    "to_zone": "junos-global",
                    "name": "GLOBAL-PERMIT-TELEMETRY-IN",
                    "policy_hit_count": "0"
                },
                {
                    "index": "9",
                    "from_zone": "junos-global",
                    "to_zone": "junos-global",
                    "name": "GLOBAL-PERMIT-SSH-IN",
                    "policy_hit_count": "0"
                },
                {
                    "index": "10",
                    "from_zone": "junos-global",
                    "to_zone": "junos-global",
                    "name": "GLOBAL-PERMIT-KNOWN-WIDE",
                    "policy_hit_count": "337917"
                },
                {
                    "index": "11",
                    "from_zone": "untrust",
                    "to_zone": "TEST-STRICT",
                    "name": "STRICT-PERMIT-OPENGEAR-IN",
                    "policy_hit_count": "0"
                },
                {
                    "index": "12",
                    "from_zone": "untrust",
                    "to_zone": "TEST-STRICT",
                    "name": "STRICT-PERMIT-SSH-IN",
                    "policy_hit_count": "445265"
                },
                {
                    "index": "13",
                    "from_zone": "untrust",
                    "to_zone": "TEST-STRICT",
                    "name": "STRICT-PERMIT-SNMP-IN",
                    "policy_hit_count": "287972350"
                },
                {
                    "index": "14",
                    "from_zone": "untrust",
                    "to_zone": "TEST-STRICT",
                    "name": "STRICT-PERMIT-TELEMETRY-IN",
                    "policy_hit_count": "0"
                },
                {
                    "index": "15",
                    "from_zone": "untrust",
                    "to_zone": "TEST-STRICT",
                    "name": "STRICT-PERMIT-NETCONF-IN",
                    "policy_hit_count": "523"
                },
                {
                    "index": "16",
                    "from_zone": "untrust",
                    "to_zone": "TEST-STRICT",
                    "name": "STRICT-PERMIT-SSH-CORE-IN",
                    "policy_hit_count": "782267"
                },
                {
                    "index": "17",
                    "from_zone": "untrust",
                    "to_zone": "TEST-STRICT",
                    "name": "STRICT-PERMIT-SSH-PDUs-IN",
                    "policy_hit_count": "333"
                },
                {
                    "index": "18",
                    "from_zone": "untrust",
                    "to_zone": "TEST-STRICT",
                    "name": "STRICT-PERMIT-SSH-TEST-FW-IN",
                    "policy_hit_count": "91441"
                },
                {
                    "index": "19",
                    "from_zone": "untrust",
                    "to_zone": "TEST-STRICT",
                    "name": "STRICT-PERMIT-ICMP-IN",
                    "policy_hit_count": "24426998"
                },
                {
                    "index": "20",
                    "from_zone": "untrust",
                    "to_zone": "TEST-STRICT",
                    "name": "STRICT-PERMIT-TRACE-IN",
                    "policy_hit_count": "1196"
                },
                {
                    "index": "21",
                    "from_zone": "untrust",
                    "to_zone": "TEST-STRICT",
                    "name": "STRICT-PERMIT-RADIUS-IN",
                    "policy_hit_count": "0"
                },
                {
                    "index": "22",
                    "from_zone": "untrust",
                    "to_zone": "TEST-STRICT",
                    "name": "STRICT-PERMIT-NTP-IN",
                    "policy_hit_count": "117709"
                },
                {
                    "index": "23",
                    "from_zone": "untrust",
                    "to_zone": "TEST-STRICT",
                    "name": "STRICT-PERMIT-TEST-IPSEC-GRE-IN",
                    "policy_hit_count": "0"
                },
                {
                    "index": "24",
                    "from_zone": "untrust",
                    "to_zone": "TEST-STRICT",
                    "name": "STRICT-PERMIT-SSH-NSO-CORE-IN",
                    "policy_hit_count": "223809"
                },
                {
                    "index": "25",
                    "from_zone": "untrust",
                    "to_zone": "TEST-STRICT",
                    "name": "STRICT-PERMIT-DNS-IN",
                    "policy_hit_count": "0"
                },
                {
                    "index": "26",
                    "from_zone": "untrust",
                    "to_zone": "TEST-DCN",
                    "name": "DCN-PERMIT-MONITORING-IN",
                    "policy_hit_count": "475804"
                },
                {
                    "index": "27",
                    "from_zone": "untrust",
                    "to_zone": "TEST-DCN",
                    "name": "DCN-PERMIT-SNMP-IN",
                    "policy_hit_count": "32808"
                },
                {
                    "index": "28",
                    "from_zone": "untrust",
                    "to_zone": "TEST-DCN",
                    "name": "DCN-PERMIT-DNS-IN",
                    "policy_hit_count": "0"
                },
                {
                    "index": "29",
                    "from_zone": "untrust",
                    "to_zone": "TEST-DCN",
                    "name": "DCN-PERMIT-NTP-IN",
                    "policy_hit_count": "0"
                },
                {
                    "index": "30",
                    "from_zone": "untrust",
                    "to_zone": "TEST-DCN",
                    "name": "DCN-PERMIT-ICMP-IN",
                    "policy_hit_count": "1129854"
                },
                {
                    "index": "31",
                    "from_zone": "untrust",
                    "to_zone": "TEST-DCN",
                    "name": "DCN-PERMIT-ONE-CONTROL-IN",
                    "policy_hit_count": "0"
                },
                {
                    "index": "32",
                    "from_zone": "untrust",
                    "to_zone": "TEST-DCN",
                    "name": "DCN-PERMIT-MCP-IN",
                    "policy_hit_count": "5305845"
                },
                {
                    "index": "33",
                    "from_zone": "untrust",
                    "to_zone": "TEST-DCN",
                    "name": "DCN-PERMIT-RADIUS-IN",
                    "policy_hit_count": "0"
                },
                {
                    "index": "34",
                    "from_zone": "untrust",
                    "to_zone": "TEST-DCN",
                    "name": "DCN-PERMIT-PNC-IN",
                    "policy_hit_count": "0"
                },
                {
                    "index": "35",
                    "from_zone": "untrust",
                    "to_zone": "TEST-DCN",
                    "name": "DCN-PERMIT-TRACE-IN",
                    "policy_hit_count": "592"
                },
                {
                    "index": "36",
                    "from_zone": "untrust",
                    "to_zone": "TEST-DCN",
                    "name": "DCN-PERMIT-SSH-IN",
                    "policy_hit_count": "77474"
                },
                {
                    "index": "37",
                    "from_zone": "untrust",
                    "to_zone": "TEST-OPTICAL",
                    "name": "OPTICAL-PERMIT-KNOWN-RDP-IN",
                    "policy_hit_count": "0"
                },
                {
                    "index": "38",
                    "from_zone": "untrust",
                    "to_zone": "TEST-OPTICAL",
                    "name": "OPTICAL-BLOCK-RDP-IN",
                    "policy_hit_count": "7636"
                },
                {
                    "index": "39",
                    "from_zone": "untrust",
                    "to_zone": "TEST-OPTICAL",
                    "name": "OPTICAL-BLOCK-TELNET-IN",
                    "policy_hit_count": "51210"
                },
                {
                    "index": "40",
                    "from_zone": "untrust",
                    "to_zone": "TEST-OPTICAL",
                    "name": "OPTICAL-PERMIT-KNOWN-TELNET-IN",
                    "policy_hit_count": "1"
                },
                {
                    "index": "41",
                    "from_zone": "untrust",
                    "to_zone": "TEST-OPTICAL",
                    "name": "OPTICAL-BLOCK-IDRAC-IN",
                    "policy_hit_count": "2167"
                },
                {
                    "index": "42",
                    "from_zone": "untrust",
                    "to_zone": "TEST-OPTICAL",
                    "name": "OPTICAL-PERMIT-IDRAC-IN",
                    "policy_hit_count": "6528"
                },
                {
                    "index": "43",
                    "from_zone": "untrust",
                    "to_zone": "TEST-OPTICAL",
                    "name": "OPTICAL-BLOCK-SSH-IN",
                    "policy_hit_count": "10886"
                },
                {
                    "index": "44",
                    "from_zone": "untrust",
                    "to_zone": "TEST-OPTICAL",
                    "name": "OPTICAL-PERMIT-SSH-IN",
                    "policy_hit_count": "36221"
                },
                {
                    "index": "45",
                    "from_zone": "untrust",
                    "to_zone": "TEST-OPTICAL",
                    "name": "OPTICAL-BLOCK-OTHER-NTP-IN",
                    "policy_hit_count": "253"
                },
                {
                    "index": "46",
                    "from_zone": "untrust",
                    "to_zone": "TEST-OPTICAL",
                    "name": "OPTICAL-PERMIT-KNOWN-NTP-IN",
                    "policy_hit_count": "0"
                },
                {
                    "index": "47",
                    "from_zone": "untrust",
                    "to_zone": "TEST-OPTICAL",
                    "name": "OPTICAL-BLOCK-OTHER-DNS-IN",
                    "policy_hit_count": "10292"
                },
                {
                    "index": "48",
                    "from_zone": "untrust",
                    "to_zone": "TEST-OPTICAL",
                    "name": "OPTICAL-PERMIT-DNS-IN",
                    "policy_hit_count": "0"
                },
                {
                    "index": "49",
                    "from_zone": "TEST-STRICT",
                    "to_zone": "untrust",
                    "name": "STRICT-PERMIT-NTP-OUT",
                    "policy_hit_count": "4468672"
                },
                {
                    "index": "50",
                    "from_zone": "TEST-STRICT",
                    "to_zone": "untrust",
                    "name": "All_TEST-STRICT_COMMODITY-INTERNET",
                    "policy_hit_count": "14599527"
                },
                {
                    "index": "51",
                    "from_zone": "TEST-STRICT",
                    "to_zone": "untrust",
                    "name": "STRICT-PERMIT-SNMP-OUT",
                    "policy_hit_count": "0"
                },
                {
                    "index": "52",
                    "from_zone": "TEST-STRICT",
                    "to_zone": "untrust",
                    "name": "STRICT-BLOCK-SNMP-OUT",
                    "policy_hit_count": "0"
                },
                {
                    "index": "53",
                    "from_zone": "TEST-STRICT",
                    "to_zone": "untrust",
                    "name": "STRICT-PERMIT-TELEMETRY-OUT",
                    "policy_hit_count": "4038240"
                },
                {
                    "index": "54",
                    "from_zone": "TEST-STRICT",
                    "to_zone": "untrust",
                    "name": "STRICT-PERMIT-SYSLOG-OUT",
                    "policy_hit_count": "125964123"
                },
                {
                    "index": "55",
                    "from_zone": "TEST-STRICT",
                    "to_zone": "untrust",
                    "name": "STRICT-BLOCK-SYSLOG-OUT",
                    "policy_hit_count": "205620273"
                },
                {
                    "index": "56",
                    "from_zone": "TEST-STRICT",
                    "to_zone": "untrust",
                    "name": "STRICT-PERMIT-DNS-OUT",
                    "policy_hit_count": "27"
                },
                {
                    "index": "57",
                    "from_zone": "TEST-STRICT",
                    "to_zone": "untrust",
                    "name": "STRICT-BLOCK-DNS-OUT",
                    "policy_hit_count": "160995"
                },
                {
                    "index": "58",
                    "from_zone": "TEST-STRICT",
                    "to_zone": "untrust",
                    "name": "STRICT-BLOCK-NTP-OUT",
                    "policy_hit_count": "38040"
                },
                {
                    "index": "59",
                    "from_zone": "TEST-STRICT",
                    "to_zone": "untrust",
                    "name": "STRICT-PERMIT-RADIUS-OUT",
                    "policy_hit_count": "1699379"
                },
                {
                    "index": "60",
                    "from_zone": "TEST-STRICT",
                    "to_zone": "untrust",
                    "name": "STRICT-BLOCK-RADIUS-OUT",
                    "policy_hit_count": "0"
                },
                {
                    "index": "61",
                    "from_zone": "TEST-STRICT",
                    "to_zone": "TEST-STRICT",
                    "name": "STRICT-INTRA-ZONE-PERMIT",
                    "policy_hit_count": "118930"
                },
                {
                    "index": "62",
                    "from_zone": "TEST-STRICT",
                    "to_zone": "TEST-OPTICAL",
                    "name": "STRICT-TO-OPTICAL-PERMIT-TELEMETRY",
                    "policy_hit_count": "0"
                },
                {
                    "index": "63",
                    "from_zone": "TEST-STRICT",
                    "to_zone": "TEST-OPTICAL",
                    "name": "STRICT-TO-OPTICAL-PERMIT-ICMP",
                    "policy_hit_count": "0"
                },
                {
                    "index": "64",
                    "from_zone": "TEST-DCN",
                    "to_zone": "untrust",
                    "name": "DCN-PERMIT-MCP-OUT",
                    "policy_hit_count": "81375"
                },
                {
                    "index": "65",
                    "from_zone": "TEST-DCN",
                    "to_zone": "untrust",
                    "name": "DCN-PERMIT-WAVESERVERS-TEST-TRAPS-OUT",
                    "policy_hit_count": "0"
                },
                {
                    "index": "66",
                    "from_zone": "TEST-DCN",
                    "to_zone": "untrust",
                    "name": "DCN-PERMIT-RADIUS-OUT",
                    "policy_hit_count": "158601"
                },
                {
                    "index": "67",
                    "from_zone": "TEST-DCN",
                    "to_zone": "untrust",
                    "name": "DCN-DEFAULT-DENY-OUT",
                    "policy_hit_count": "43959"
                },
                {
                    "index": "68",
                    "from_zone": "TEST-DCN",
                    "to_zone": "untrust",
                    "name": "DCN-PERMIT-SYSLOG-OUT",
                    "policy_hit_count": "13650"
                },
                {
                    "index": "69",
                    "from_zone": "TEST-DCN",
                    "to_zone": "untrust",
                    "name": "DCN-PERMIT-NTP-OUT",
                    "policy_hit_count": "204"
                },
                {
                    "index": "70",
                    "from_zone": "TEST-DCN",
                    "to_zone": "TEST-DCN",
                    "name": "DCN-INTRA-ZONE-PERMIT",
                    "policy_hit_count": "0"
                },
                {
                    "index": "71",
                    "from_zone": "TEST-OPTICAL",
                    "to_zone": "untrust",
                    "name": "OPTICAL-DEFAULT-DENY-OUT",
                    "policy_hit_count": "0"
                },
                {
                    "index": "72",
                    "from_zone": "TEST-OPTICAL",
                    "to_zone": "untrust",
                    "name": "OPTICAL-PERMIT-DNS-OUT",
                    "policy_hit_count": "7552861"
                },
                {
                    "index": "73",
                    "from_zone": "TEST-OPTICAL",
                    "to_zone": "untrust",
                    "name": "OPTICAL-BLOCK-OTHER-NTP-OUT",
                    "policy_hit_count": "0"
                },
                {
                    "index": "74",
                    "from_zone": "TEST-OPTICAL",
                    "to_zone": "untrust",
                    "name": "OPTICAL-PERMIT-NTP-OUT",
                    "policy_hit_count": "1222475"
                },
                {
                    "index": "75",
                    "from_zone": "TEST-OPTICAL",
                    "to_zone": "untrust",
                    "name": "OPTICAL-BLOCK-OTHER-DNS-OUT",
                    "policy_hit_count": "2256"
                },
                {
                    "index": "76",
                    "from_zone": "TEST-OPTICAL",
                    "to_zone": "TEST-OPTICAL",
                    "name": "OPTICAL-INTRA-ZONE-PERMIT",
                    "policy_hit_count": "0"
                }
            ],
            "total_policies": "76"
        },
        "root-logical-system2": {
            "security_policy": [
                {
                    "index": "1",
                    "from_zone": "junos-global",
                    "to_zone": "junos-global",
                    "name": "GLOBAL-PERMIT-TRACE-IN",
                    "policy_hit_count": "78"
                },
                {
                    "index": "2",
                    "from_zone": "junos-global",
                    "to_zone": "junos-global",
                    "name": "GLOBAL-PERMIT-RADIUS-IN",
                    "policy_hit_count": "0"
                },
                {
                    "index": "3",
                    "from_zone": "junos-global",
                    "to_zone": "junos-global",
                    "name": "GLOBAL-PERMIT-NTP-IN",
                    "policy_hit_count": "0"
                }
            ],
            "total_policies": "3"
        }
    }
}
