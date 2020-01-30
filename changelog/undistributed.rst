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
    * Added ShowMplsLabelTablePrivate for:
        * show mpls label table private    
    * Added ShowMplsLdpNeighbor for:
        * show mpls ldp neighbor
        * show mpls ldp neighbor {interface}
    * Added ShowMplsLdpNeighborDetail for:
        * show mpls ldp neighbor detail
        * show mpls ldp neighbor {interface} detail
    * Added ShowIsisFRRSummary for:
        * show isis fast-reroute summary
    * Added ShowBgpEgressEngineering for:
        * show bgp egress-engineering
    * Added ShowTrafficCollecterIpv4CountersPrefixDetail for:
        * show traffic-collector external-interface
        * show traffic-collector ipv4 counters prefix <prefix> detail
    * Added ShowBundleReasons for:  
        * show bundle reasons
        * show bundle {interface} reasons
    * Added ShowSsh for:
        * show ssh session details

* IOS
    * Added ShowAccessSessionInterfaceDetails for:
        * show access-session interface {interface} details
    * Added parsers for ios/cat6k:
        * show version
        * dir
        * show redundancy
        * show inventory
    * Added parsers for ios/c7600:
        * show version
        * dir
        * show redundancy
        * show inventory
        * show module

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
    * Updated ShowInterfacesDescription
	    * Modified regex to fix parsing as per customer output
		
    * Updated ShowClnsProtocol
        * Changed 'Null Tag' to 'null' 
    * Updated ShowInterfacesDescription
	    * Modified regex to fix parsing as per customer output
* IOSXR
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

* IOS
    * Updated ShowVersion for:
        * Optional key issue for ios/cat6k platform
        * Updating symbolic link to platform specific unittests
    * Updated ShowAccessLists
	    * Updated for the case of empty ttl_groups
		* Updated for udp ACL with incremented counter
		* Added support for access-lists with object-group references

* IOSXE
    * Updating symbolic link to platform specific unittests

* IOSXR
    * Updating symbolic link to platform specific unittests

* IOSXR
    * Updated and removed regex to accommodate outputs
    * Added new unittest 
    * Updated and added regex to accommodate more outputs
    * Added new output to unittest

* IOSXR
    * Updated regex to accommodate more outputs
    * Added extra key to schema
    * Added new unittest
    
