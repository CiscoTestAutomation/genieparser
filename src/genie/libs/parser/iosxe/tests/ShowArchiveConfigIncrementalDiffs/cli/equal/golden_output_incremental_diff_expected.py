expected_output = {
    "list_of_commands": [
        "ip subnet-zero",
        "ip cef",
        "ip name-server 10.4.4.4",
        "voice dnis-map1",
        "dnis 111",
        "interface FastEthernet1/0",
        "no ip address",
        "no ip route-cache",
        "no ip mroute-cache",
        "shutdown",
        "duplex half",
        "ip default-gateway 10.5.5.5",
        "ip classless",
        "access-list 110 deny    ip any host 10.1.1.1",
        "access-list 110 deny    ip any host 10.1.1.2",
        "access-list 110 deny    ip any host 10.1.1.3",
        "snmp-server community private RW",
    ]
}
