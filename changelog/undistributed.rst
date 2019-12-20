* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------

* IOSXE
    * Added ShowProcessesMemory for:
        * show processes memory
        * show processes memory | include {include}
    * Added ShowAccessSessionInterfaceDetails for:
        * show access-session interface {interface} details

* IOSXR
    * Added ShowMplsInterfaces for:
        * show mpls interfaces
        * show mpls interfaces {interface}
    * Added ShowMplsForwarding for:
        * show mpls forwarding
        * show mpls forwarding vrf {vrf}
    *Added ShowMplsLabelRange for:
        * show mpls label range
    * Added ShowIsisFRRSummary for:
        * show isis fast-reroute summary

* IOS
    * Added ShowAccessSessionInterfaceDetails for:
        * show access-session interface {interface} details
    * Added parsers for ios/cat6k:
        * show version
        * dir
        * show redundancy
        * show inventory


--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowAuthenticationSessionsInterfaceDetails
	    * Change in order of Server Policies no longer breaks parsing
    * Updated ShowClnsIsNeighborsDetail
        * Changed regex and schema to support type 'L1L2'
    * Updated ShowIsisDatabaseDetail
        * Changed schema to support more various output
<<<<<<< HEAD
    * Updated ShowInterfacesDescription
	    * Modified regex to fix parsing as per customer output
		
=======
    * Updated ShowClnsProtocol
        * Changed 'Null Tag' to 'null' 
    * Updated ShowInterfacesDescription
	    * Modified regex to fix parsing as per customer output

>>>>>>> b2aed7b96ddd7630be6c374608a53366aa5ecefa
* DNAC
    * Updated Interface for:
        * Supporting hostname in the schema
