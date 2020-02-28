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
    * Updating symbolic link to platform specific unittests
    * Updated ShowInterfacesStatus
        * Update regex to support various output

* IOSXR
    * Updating symbolic link to platform specific unittests
    * Updated and removed regex to accommodate outputs
    * Added new unittest 
    * Updated and added regex to accommodate more outputs
    * Added new output to unittest
    * Updated regex to accommodate more outputs
    * Added extra key to schema
    * Added new unittest

* NXOS
    * Updated ShowNveVniIngressReplication
        * Added regex 
        * Added new unittest
    * Updated ShowIpCefInternal
	    * Update schema and regex to support more various output
    * Updated ShowInterface
        * Update regex to cover both 'IP' and 'ip', both 'Rx' and 'RX'
* IOSXR:
    * Updated ShowRouteIpv4
        * Added and updated regex
        * Added unittest

* IOSXE:
    * Updated ShowBootvar
        * Fixed crash
        * Added unittest
    * Updated Traceroute:
        * Updated regex to support various outputs.
        * Updated schema and regex to support AS number.
* IOSXE
    * Updated ShowMplsForwardingTable:
        * Modified wrong regex
    * Updated ShowIpCef:
        * Modified regex to support SID
    * Updated ShowMplsForwardingTableDetail:
        * show mpls forwarding-table {route} detail
        
