expected_output = {
    {
        "security_policy_counts": {
            "root-logical-system": {
                "security_policy": [
                    {
                        "index": "1",
                        "from-zone": "junos-global",
                        "to-zone": "junos-global",
                        "name": "GLOBAL-PERMIT-TRACE-IN",
                        "policy-hit-count": "78"
                    },
                    {
                        "index": "2",
                        "from-zone": "junos-global",
                        "to-zone": "junos-global",
                        "name": "GLOBAL-PERMIT-RADIUS-IN",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "3",
                        "from-zone": "junos-global",
                        "to-zone": "junos-global",
                        "name": "GLOBAL-PERMIT-NTP-IN",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "4",
                        "from-zone": "junos-global",
                        "to-zone": "junos-global",
                        "name": "GLOBAL-PERMIT-ICMP-IN",
                        "policy-hit-count": "3504"
                    },
                    {
                        "index": "5",
                        "from-zone": "junos-global",
                        "to-zone": "junos-global",
                        "name": "GLOBAL-PERMIT-SNMP-IN",
                        "policy-hit-count": "1"
                    },
                    {
                        "index": "6",
                        "from-zone": "junos-global",
                        "to-zone": "junos-global",
                        "name": "DEFAULT-DENY"
                    },
                    {
                        "index": "7",
                        "from-zone": "junos-global",
                        "to-zone": "junos-global",
                        "name": "GLOBAL-PERMIT-DNS-IN",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "8",
                        "from-zone": "junos-global",
                        "to-zone": "junos-global",
                        "name": "GLOBAL-PERMIT-TELEMETRY-IN",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "9",
                        "from-zone": "junos-global",
                        "to-zone": "junos-global",
                        "name": "GLOBAL-PERMIT-SSH-IN",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "10",
                        "from-zone": "junos-global",
                        "to-zone": "junos-global",
                        "name": "GLOBAL-PERMIT-KNOWN-WIDE",
                        "policy-hit-count": "337917"
                    },
                    {
                        "index": "11",
                        "from-zone": "untrust",
                        "to-zone": "TEST-STRICT",
                        "name": "STRICT-PERMIT-OPENGEAR-IN",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "12",
                        "from-zone": "untrust",
                        "to-zone": "TEST-STRICT",
                        "name": "STRICT-PERMIT-SSH-IN",
                        "policy-hit-count": "445265"
                    },
                    {
                        "index": "13",
                        "from-zone": "untrust",
                        "to-zone": "TEST-STRICT",
                        "name": "STRICT-PERMIT-SNMP-IN",
                        "policy-hit-count": "287972350"
                    },
                    {
                        "index": "14",
                        "from-zone": "untrust",
                        "to-zone": "TEST-STRICT",
                        "name": "STRICT-PERMIT-TELEMETRY-IN",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "15",
                        "from-zone": "untrust",
                        "to-zone": "TEST-STRICT",
                        "name": "STRICT-PERMIT-NETCONF-IN",
                        "policy-hit-count": "523"
                    },
                    {
                        "index": "16",
                        "from-zone": "untrust",
                        "to-zone": "TEST-STRICT",
                        "name": "STRICT-PERMIT-SSH-CORE-IN",
                        "policy-hit-count": "782267"
                    },
                    {
                        "index": "17",
                        "from-zone": "untrust",
                        "to-zone": "TEST-STRICT",
                        "name": "STRICT-PERMIT-SSH-PDUs-IN",
                        "policy-hit-count": "333"
                    },
                    {
                        "index": "18",
                        "from-zone": "untrust",
                        "to-zone": "TEST-STRICT",
                        "name": "STRICT-PERMIT-SSH-TEST-FW-IN",
                        "policy-hit-count": "91441"
                    },
                    {
                        "index": "19",
                        "from-zone": "untrust",
                        "to-zone": "TEST-STRICT",
                        "name": "STRICT-PERMIT-ICMP-IN",
                        "policy-hit-count": "24426998"
                    },
                    {
                        "index": "20",
                        "from-zone": "untrust",
                        "to-zone": "TEST-STRICT",
                        "name": "STRICT-PERMIT-TRACE-IN",
                        "policy-hit-count": "1196"
                    },
                    {
                        "index": "21",
                        "from-zone": "untrust",
                        "to-zone": "TEST-STRICT",
                        "name": "STRICT-PERMIT-RADIUS-IN",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "22",
                        "from-zone": "untrust",
                        "to-zone": "TEST-STRICT",
                        "name": "STRICT-PERMIT-NTP-IN",
                        "policy-hit-count": "117709"
                    },
                    {
                        "index": "23",
                        "from-zone": "untrust",
                        "to-zone": "TEST-STRICT",
                        "name": "STRICT-PERMIT-TEST-IPSEC-GRE-IN",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "24",
                        "from-zone": "untrust",
                        "to-zone": "TEST-STRICT",
                        "name": "STRICT-PERMIT-SSH-NSO-CORE-IN",
                        "policy-hit-count": "223809"
                    },
                    {
                        "index": "25",
                        "from-zone": "untrust",
                        "to-zone": "TEST-STRICT",
                        "name": "STRICT-PERMIT-DNS-IN",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "26",
                        "from-zone": "untrust",
                        "to-zone": "TEST-DCN",
                        "name": "DCN-PERMIT-MONITORING-IN",
                        "policy-hit-count": "475804"
                    },
                    {
                        "index": "27",
                        "from-zone": "untrust",
                        "to-zone": "TEST-DCN",
                        "name": "DCN-PERMIT-SNMP-IN",
                        "policy-hit-count": "32808"
                    },
                    {
                        "index": "28",
                        "from-zone": "untrust",
                        "to-zone": "TEST-DCN",
                        "name": "DCN-PERMIT-DNS-IN",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "29",
                        "from-zone": "untrust",
                        "to-zone": "TEST-DCN",
                        "name": "DCN-PERMIT-NTP-IN",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "30",
                        "from-zone": "untrust",
                        "to-zone": "TEST-DCN",
                        "name": "DCN-PERMIT-ICMP-IN",
                        "policy-hit-count": "1129854"
                    },
                    {
                        "index": "31",
                        "from-zone": "untrust",
                        "to-zone": "TEST-DCN",
                        "name": "DCN-PERMIT-ONE-CONTROL-IN",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "32",
                        "from-zone": "untrust",
                        "to-zone": "TEST-DCN",
                        "name": "DCN-PERMIT-MCP-IN",
                        "policy-hit-count": "5305845"
                    },
                    {
                        "index": "33",
                        "from-zone": "untrust",
                        "to-zone": "TEST-DCN",
                        "name": "DCN-PERMIT-RADIUS-IN",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "34",
                        "from-zone": "untrust",
                        "to-zone": "TEST-DCN",
                        "name": "DCN-PERMIT-PNC-IN",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "35",
                        "from-zone": "untrust",
                        "to-zone": "TEST-DCN",
                        "name": "DCN-PERMIT-TRACE-IN",
                        "policy-hit-count": "592"
                    },
                    {
                        "index": "36",
                        "from-zone": "untrust",
                        "to-zone": "TEST-DCN",
                        "name": "DCN-PERMIT-SSH-IN",
                        "policy-hit-count": "77474"
                    },
                    {
                        "index": "37",
                        "from-zone": "untrust",
                        "to-zone": "TEST-OPTICAL",
                        "name": "OPTICAL-PERMIT-KNOWN-RDP-IN",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "38",
                        "from-zone": "untrust",
                        "to-zone": "TEST-OPTICAL",
                        "name": "OPTICAL-BLOCK-RDP-IN",
                        "policy-hit-count": "7636"
                    },
                    {
                        "index": "39",
                        "from-zone": "untrust",
                        "to-zone": "TEST-OPTICAL",
                        "name": "OPTICAL-BLOCK-TELNET-IN",
                        "policy-hit-count": "51210"
                    },
                    {
                        "index": "40",
                        "from-zone": "untrust",
                        "to-zone": "TEST-OPTICAL",
                        "name": "OPTICAL-PERMIT-KNOWN-TELNET-IN",
                        "policy-hit-count": "1"
                    },
                    {
                        "index": "41",
                        "from-zone": "untrust",
                        "to-zone": "TEST-OPTICAL",
                        "name": "OPTICAL-BLOCK-IDRAC-IN",
                        "policy-hit-count": "2167"
                    },
                    {
                        "index": "42",
                        "from-zone": "untrust",
                        "to-zone": "TEST-OPTICAL",
                        "name": "OPTICAL-PERMIT-IDRAC-IN",
                        "policy-hit-count": "6528"
                    },
                    {
                        "index": "43",
                        "from-zone": "untrust",
                        "to-zone": "TEST-OPTICAL",
                        "name": "OPTICAL-BLOCK-SSH-IN",
                        "policy-hit-count": "10886"
                    },
                    {
                        "index": "44",
                        "from-zone": "untrust",
                        "to-zone": "TEST-OPTICAL",
                        "name": "OPTICAL-PERMIT-SSH-IN",
                        "policy-hit-count": "36221"
                    },
                    {
                        "index": "45",
                        "from-zone": "untrust",
                        "to-zone": "TEST-OPTICAL",
                        "name": "OPTICAL-BLOCK-OTHER-NTP-IN",
                        "policy-hit-count": "253"
                    },
                    {
                        "index": "46",
                        "from-zone": "untrust",
                        "to-zone": "TEST-OPTICAL",
                        "name": "OPTICAL-PERMIT-KNOWN-NTP-IN",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "47",
                        "from-zone": "untrust",
                        "to-zone": "TEST-OPTICAL",
                        "name": "OPTICAL-BLOCK-OTHER-DNS-IN",
                        "policy-hit-count": "10292"
                    },
                    {
                        "index": "48",
                        "from-zone": "untrust",
                        "to-zone": "TEST-OPTICAL",
                        "name": "OPTICAL-PERMIT-DNS-IN",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "49",
                        "from-zone": "TEST-STRICT",
                        "to-zone": "untrust",
                        "name": "STRICT-PERMIT-NTP-OUT",
                        "policy-hit-count": "4468672"
                    },
                    {
                        "index": "50",
                        "from-zone": "TEST-STRICT",
                        "to-zone": "untrust",
                        "name": "All_TEST-STRICT_COMMODITY-INTERNET",
                        "policy-hit-count": "14599527"
                    },
                    {
                        "index": "51",
                        "from-zone": "TEST-STRICT",
                        "to-zone": "untrust",
                        "name": "STRICT-PERMIT-SNMP-OUT",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "52",
                        "from-zone": "TEST-STRICT",
                        "to-zone": "untrust",
                        "name": "STRICT-BLOCK-SNMP-OUT",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "53",
                        "from-zone": "TEST-STRICT",
                        "to-zone": "untrust",
                        "name": "STRICT-PERMIT-TELEMETRY-OUT",
                        "policy-hit-count": "4038240"
                    },
                    {
                        "index": "54",
                        "from-zone": "TEST-STRICT",
                        "to-zone": "untrust",
                        "name": "STRICT-PERMIT-SYSLOG-OUT",
                        "policy-hit-count": "125964123"
                    },
                    {
                        "index": "55",
                        "from-zone": "TEST-STRICT",
                        "to-zone": "untrust",
                        "name": "STRICT-BLOCK-SYSLOG-OUT",
                        "policy-hit-count": "205620273"
                    },
                    {
                        "index": "56",
                        "from-zone": "TEST-STRICT",
                        "to-zone": "untrust",
                        "name": "STRICT-PERMIT-DNS-OUT",
                        "policy-hit-count": "27"
                    },
                    {
                        "index": "57",
                        "from-zone": "TEST-STRICT",
                        "to-zone": "untrust",
                        "name": "STRICT-BLOCK-DNS-OUT",
                        "policy-hit-count": "160995"
                    },
                    {
                        "index": "58",
                        "from-zone": "TEST-STRICT",
                        "to-zone": "untrust",
                        "name": "STRICT-BLOCK-NTP-OUT",
                        "policy-hit-count": "38040"
                    },
                    {
                        "index": "59",
                        "from-zone": "TEST-STRICT",
                        "to-zone": "untrust",
                        "name": "STRICT-PERMIT-RADIUS-OUT",
                        "policy-hit-count": "1699379"
                    },
                    {
                        "index": "60",
                        "from-zone": "TEST-STRICT",
                        "to-zone": "untrust",
                        "name": "STRICT-BLOCK-RADIUS-OUT",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "61",
                        "from-zone": "TEST-STRICT",
                        "to-zone": "TEST-STRICT",
                        "name": "STRICT-INTRA-ZONE-PERMIT",
                        "policy-hit-count": "118930"
                    },
                    {
                        "index": "62",
                        "from-zone": "TEST-STRICT",
                        "to-zone": "TEST-OPTICAL",
                        "name": "STRICT-TO-OPTICAL-PERMIT-TELEMETRY",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "63",
                        "from-zone": "TEST-STRICT",
                        "to-zone": "TEST-OPTICAL",
                        "name": "STRICT-TO-OPTICAL-PERMIT-ICMP",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "64",
                        "from-zone": "TEST-DCN",
                        "to-zone": "untrust",
                        "name": "DCN-PERMIT-MCP-OUT",
                        "policy-hit-count": "81375"
                    },
                    {
                        "index": "65",
                        "from-zone": "TEST-DCN",
                        "to-zone": "untrust",
                        "name": "DCN-PERMIT-WAVESERVERS-TEST-TRAPS-OUT",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "66",
                        "from-zone": "TEST-DCN",
                        "to-zone": "untrust",
                        "name": "DCN-PERMIT-RADIUS-OUT",
                        "policy-hit-count": "158601"
                    },
                    {
                        "index": "67",
                        "from-zone": "TEST-DCN",
                        "to-zone": "untrust",
                        "name": "DCN-DEFAULT-DENY-OUT",
                        "policy-hit-count": "43959"
                    },
                    {
                        "index": "68",
                        "from-zone": "TEST-DCN",
                        "to-zone": "untrust",
                        "name": "DCN-PERMIT-SYSLOG-OUT",
                        "policy-hit-count": "13650"
                    },
                    {
                        "index": "69",
                        "from-zone": "TEST-DCN",
                        "to-zone": "untrust",
                        "name": "DCN-PERMIT-NTP-OUT",
                        "policy-hit-count": "204"
                    },
                    {
                        "index": "70",
                        "from-zone": "TEST-DCN",
                        "to-zone": "TEST-DCN",
                        "name": "DCN-INTRA-ZONE-PERMIT",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "71",
                        "from-zone": "TEST-OPTICAL",
                        "to-zone": "untrust",
                        "name": "OPTICAL-DEFAULT-DENY-OUT",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "72",
                        "from-zone": "TEST-OPTICAL",
                        "to-zone": "untrust",
                        "name": "OPTICAL-PERMIT-DNS-OUT",
                        "policy-hit-count": "7552861"
                    },
                    {
                        "index": "73",
                        "from-zone": "TEST-OPTICAL",
                        "to-zone": "untrust",
                        "name": "OPTICAL-BLOCK-OTHER-NTP-OUT",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "74",
                        "from-zone": "TEST-OPTICAL",
                        "to-zone": "untrust",
                        "name": "OPTICAL-PERMIT-NTP-OUT",
                        "policy-hit-count": "1222475"
                    },
                    {
                        "index": "75",
                        "from-zone": "TEST-OPTICAL",
                        "to-zone": "untrust",
                        "name": "OPTICAL-BLOCK-OTHER-DNS-OUT",
                        "policy-hit-count": "2256"
                    },
                    {
                        "index": "76",
                        "from-zone": "TEST-OPTICAL",
                        "to-zone": "TEST-OPTICAL",
                        "name": "OPTICAL-INTRA-ZONE-PERMIT",
                        "policy-hit-count": "0"
                    }
                ],
                "total-policies": "76"
            },
            "root-logical-system2": {
                "security_policy": [
                    {
                        "index": "1",
                        "from-zone": "junos-global",
                        "to-zone": "junos-global",
                        "name": "GLOBAL-PERMIT-TRACE-IN",
                        "policy-hit-count": "78"
                    },
                    {
                        "index": "2",
                        "from-zone": "junos-global",
                        "to-zone": "junos-global",
                        "name": "GLOBAL-PERMIT-RADIUS-IN",
                        "policy-hit-count": "0"
                    },
                    {
                        "index": "3",
                        "from-zone": "junos-global",
                        "to-zone": "junos-global",
                        "name": "GLOBAL-PERMIT-NTP-IN",
                        "policy-hit-count": "0"
                    }
                ],
                "total-policies": "3"
            }
        }
    }
}