expected_output = {
    "forwarding-table-information": {
        "route-table": [
            {
                "address-family": "Internet",
                "enabled-protocols": "Bridging,",
                "route-table-summary": [
                    {"route-count": "918", "route-table-type": "user"},
                    {"route-count": "5", "route-table-type": "perm"},
                    {"route-count": "11", "route-table-type": "intf"},
                    {"route-count": "21", "route-table-type": "dest"},
                ],
                "table-name": "default.inet",
            },
            {
                "address-family": "Internet",
                "enabled-protocols": "Bridging,",
                "route-table-summary": [
                    {"route-count": "5", "route-table-type": "perm"}
                ],
                "table-name": "__pfe_private__.inet",
            },
            {
                "address-family": "Internet",
                "enabled-protocols": "Bridging,",
                "route-table-summary": [
                    {"route-count": "5", "route-table-type": "perm"},
                    {"route-count": "2", "route-table-type": "intf"},
                    {"route-count": "3", "route-table-type": "dest"},
                ],
                "table-name": "__juniper_services__.inet",
            },
            {
                "address-family": "Internet",
                "enabled-protocols": "Bridging, Dual VLAN,",
                "route-table-summary": [
                    {"route-count": "5", "route-table-type": "perm"}
                ],
                "table-name": "__master.anon__.inet",
            },
            {
                "address-family": "ISO",
                "enabled-protocols": "Bridging,",
                "route-table-summary": [
                    {"route-count": "1", "route-table-type": "perm"}
                ],
                "table-name": "default.iso",
            },
            {
                "address-family": "ISO",
                "enabled-protocols": "Bridging, Dual VLAN,",
                "route-table-summary": [
                    {"route-count": "1", "route-table-type": "perm"}
                ],
                "table-name": "__master.anon__.iso",
            },
            {
                "address-family": "Internet6",
                "enabled-protocols": "Bridging,",
                "route-table-summary": [
                    {"route-count": "14", "route-table-type": "user"},
                    {"route-count": "6", "route-table-type": "perm"},
                    {"route-count": "18", "route-table-type": "intf"},
                    {"route-count": "7", "route-table-type": "dest"},
                ],
                "table-name": "default.inet6",
            },
            {
                "address-family": "Internet6",
                "enabled-protocols": "Bridging, Dual VLAN,",
                "route-table-summary": [
                    {"route-count": "6", "route-table-type": "perm"}
                ],
                "table-name": "__master.anon__.inet6",
            },
            {
                "address-family": "MPLS",
                "route-table-summary": [
                    {"route-count": "44", "route-table-type": "user"},
                    {"route-count": "1", "route-table-type": "perm"},
                ],
                "table-name": "default.mpls",
            },
            {
                "address-family": "MPLS",
                "enabled-protocols": "Bridging, Single VLAN, Dual VLAN,",
                "route-table-summary": [
                    {"route-count": "1", "route-table-type": "perm"}
                ],
                "table-name": "__mpls-oam__.mpls",
            },
            {
                "address-family": "VPLS",
                "route-table-summary": [
                    {"route-count": "1", "route-table-type": "perm"}
                ],
                "table-name": "default-switch.bridge",
            },
            {
                "address-family": "DHCP Snooping",
                "route-table-summary": [
                    {"route-count": "1", "route-table-type": "perm"}
                ],
                "table-name": "default.dhcp-snooping",
            },
        ]
    }
}
