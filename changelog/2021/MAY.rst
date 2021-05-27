--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxr
    * Added ShowOspfDatabase
        * show ospf database
        * show ospf {process_id} database
    * Added ShowOspfv3InterfaceSchema
    * Added ShowOspfv3Interface
        * show ospfv3 interface
    * Added ShowOspfv3Database
        * show ospfv3 database
        * show ospfv3 {process_id} database
    * Added ShowOspfv3VrfAllInclusiveNeighborDetail
        * show ospfv3 vrf all-inclusive neighbor detail
    * Added ShowOspfv3Neighbor
        * show ospfv3 neighbor
        * show ospfv3 {process} neighbor
        * show ospfv3 vrf {vrf} neighbor
        * folder based unittests

* iosxe
    * Added ShowIpEigrpTopology
        * Added parser for "show ip eigrp topology" & "show ip eigrp vrf {vrf} topology"
        * Added 4 regexp, r1, r2, r3, r4 to ShowEigrpTopologySuperparser
        * Added folder based unittests
    * Added ShowIpv6EigrpTopology
        * Added parser for "show ipv6 eigrp topology" & "show ipv6 eigrp vrf {vrf} topology"
        * Added 4 regexp, r1, r2, r3, r4 to ShowEigrpTopologySuperparser
        * Added folder based unittests
    * Added ShowIpNbarVersion
        * add show command 'show ip nbar version'
        * add folder based unittests

* apic
    * Added parsers for 'fnvread', 'df' and 'ls' commands

* linux
    * Added parsers for 'ls' commands


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIpRouteSummary
        * Update p1 regex to capture output related to spacing for 'show ip route summary'
        * Add folder based unittests
    * Modified ShowInterfaces
        * Updated regex pattern p1 and p1_1 to accommodate various outputs.
        * Add folderbased unittest.
    * Modified ShowIpInterface
        * Updated regex pattern p1 and to accommodate various outputs.
        * Add folderbased unittest.
    * Modified ShowIpv6Interface
        * Updated regex pattern p1 and to accommodate various outputs.
        * Add folderbased unittest.
    * Modified ShowPlatformSoftwareStatusControl
        * Fixed regex
    * Modified ShowBgpNeighborSuperParser
        * Update regex <p22> to properly match Current Prefixes
    * Modified ShowApDot115GhzSummary
        * Update schema to accept optional mode field
            * update logic to include mode field when it exist in the cli output
            * update regex p1 to include tx_pwr field with or without star
        * Add folder based unittests
        
    * Modified ShowInventory
        * Add regex p1_8 to accept additional NAMES for 'show inventory' command
        * Update logic to include missing NAMES if they exists
        * Add folder based unittests
    * ShowRouteMapAll
        * Updated show route-map regex's to allow special characters in places where they should be allowed
        * Update test to cover more of the regex's and to include match_community_list key
    * Modified ShowInterfacesAccounting
        * to support various output
    * Modified ShowVersionSchema
        * Add `air_license_level` and `next_reload_air_license_level` keys
    * Modified ShowVersion
        * Add regex for AIR license level and type
        * Refactor license package parser implementation
    * Modified ShowInterface class
        * Normalize interface name
    * Modified ShowStandbyAll
        * Refactor parser so that it commits data to standby_all_dict after parsing all lines
        * Fix group name regex so that it works with subinterfaces

* viptela
    * Modified ShowOmpPeers
        * updated regex pattern p1 to accommodate full-length site id strings
        * updated folderbased unittest
        * this updates IOSXE ShowSdwanOmpPeers

* iosxr
    * Modified ShowL2vpnBridgeDomainBrief
        * Class now parses its own output instead of calling and returning another class' output verbatim.
        * This is helpful because the Brief version of the command outputs in a different format.
    * Added ShowL2vpnBridgeDomainSchema
        * Schema needed to support modifications to ShowL2vpnBridgeDomainBrief
    * Modified Ping
        * Changed pattern p4 to work with IP addresses that cannot be pinged
        * Added unittest

* nxos
    * Modified ShowInterfaceStatus
        * to support various output
    * Modified ShowCdpNeighborsDetail
        * Fixed issue with parser that affected Jupyter notebooks

* ios
    * ShowRouteMapAll
        * Update test to include match_community_list key
    * Show Boot command now uses the IOSXE 'show boot' parser instead of IOSXE 'show bootvar'

* nxos
    * Modified ShowInterfaceBrief
        * Updated regex p4 to remove false positives
        * Updated schema to not require an ethernet interface
