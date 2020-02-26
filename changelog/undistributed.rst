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
* IOSXE
    * Updated ShowAuthenticationSessionsInterfaceDetails
	    * Change in order of Server Policies no longer breaks parsing
    * Updated ShowClnsIsNeighborsDetail
        * Changed regex and schema to support type 'L1L2'
    * Updated ShowIsisDatabaseDetail
        * Changed schema to support more various output
    * Updated ShowInterfacesDescription
	    * Modified regex to fix parsing as per customer output
    * Updated ShowVlan
        * Modified if-condition to support various output.
    * Updated ShowClnsProtocol
        * Changed 'Null Tag' to 'null' 
    * Updated ShowInterfacesDescription
	    * Modified regex to fix parsing as per customer output
    * Updated ShowVrfDetail:
        * Modified regex to support customer output
    * Updated ShowEthernetServiceInstanceDetail
        * Modified regex to support outputs
    * Updated ShowIpIgmpInterface:
        * Modified schema
    * Updated ShowIpPimInterfaceDetail:
        * Added on Optional key to schema
    * Updated ShowVersion:
        * Modified schema and parser class
    * Updated ShowAccessLists:
        * Modified regex to parse more outputs


* IOSXR
    * Updated ShowRouteIpv4:
        * Changed regex to support some VRF values such as 'L:111'

    * Updated ShowLacp
        * Change in order to parse show lacp {interface}.
    * Updated ShowBundle
        * Change in order to parse show bundle {interface} reasons 

* DNAC
    * Updated Interface for:
        * Supporting hostname in the schema
		
* NXOS
    * Updated ShowVpc:
        * Supporting parser for vpc+ outputs
    * Updated ShowIpRoute:
        * Add keys 'route_preference' and 'metric' into the schema
    * Updated ShowRouting:
        * Change its parent class into ShowIpRoute

* IOS
    * Updated ShowVersion for:
        * Optional key issue for ios/cat6k platform
        * Updating symbolic link to platform specific unittests
    * Updated ShowAccessLists
	    * Updated for the case of empty ttl_groups
		* Updated for udp ACL with incremented counter
		* Added support for access-lists with object-group references
    * Updated ShowInventory
        * Updated for various outputs

* IOSXE
    * Updating symbolic link to platform specific unittests

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
* IOSXR:
    * Updated ShowRouteIpv4
        * Added and updated regex
        * Added unittest
    * Updated ShowMplsForwardingTable:
        * Modified wrong regex
    * Updated ShowIpCef:
        * Modified regex to support SID
    * Updated ShowMplsForwardingTableDetail:
        * show mpls forwarding-table {route} detail