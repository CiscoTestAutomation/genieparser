* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowIpBgpRouteDistributer for:
        * show ip bgp {route}
        * show ip bgp {address_family}

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowMplsForwardingTable:
        * Modified wrong regex
    * Updated ShowIpCef:
        * Modified regex to support SID
        * update regex and schema to support local sid
    * Updated ShowMplsForwardingTableDetail:
        * show mpls forwarding-table {route} detail
    * Updated Traceroute:
        * Updated regex to support various outputs.
        * Updated schema and regex to support AS number.
    * Updated ShowBootvar
        * Fixed crash
        * Added unittest
    * Updated ShowInterfacesStatus
        * Updated regex to support various output
    * Updated ShowNveEthernetSegment
        * Updated regex to support various output
    * Updated ShowIpInterfaceVrfAll
        * Update regex to support more various output

* NXOS
    * Updated ShowInterface
        * Update regex to cover both 'IP' and 'ip', both 'Rx' and 'RX'
        * Add if-condition to assign True to key 'enabled' when has output 'admin state is up'
    * Updated ShowIpRoute
        * Add keys into the schema, modify regex
    * Updated ShowRouting
        * Change its parent class from ShowRoutingVrfAll into ShowIpRoute

