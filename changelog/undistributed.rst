* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------

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
    * Added ShowIpBgpRegexp:
        * show ip bgp regexp ^$ 
    * Moved ShowBootvar to iosxe folder
    * Added ShowInterfaceStatus for:
        * show interface status

* IOSXE
    * Added ShowProcessesMemory for:
        * show processes memory
        * show processes memory | include {include}
    * Added ShowAccessSessionInterfaceDetails for:
        * show access-session interface {interface} details
    * Added ShowIpBgpRegexp for:
        * show ip bgp regexp ^$ 
    * Added ShowBootvar for:
        * 'show bootvar'
    * Added ShowInterfaceStatus for:
        * show interface status

* IOSXR
    * Added ShowMplsInterfaces for:
        * show mpls interfaces
        * show mpls interfaces {interface}
    * Added ShowMplsForwarding for:
        * show mpls forwarding
        * show mpls forwarding vrf {vrf}
    * Added ShowMplsLabelRange for:
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
        * show ssh history

* SROS
    * Added ShowSystemNtpAll for:
        * show system ntp all
    * Added ShowRouterIsisAdjacency for:
        * show router isis adjacency
    * Added ShowRouterIsisAdjacencyDetail for:
        * show router isis adjacency detail

* LINUX
    * Added Ps for:
        * ps -ef
        * ps -ef | grep {grep}

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------

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
    * Updated ShowUsers:
        * Changed regex to support various outputs.
    * Updated ShowProcessesCpuHistory
        * Fixed warnings for python3.8
    * Updated ShowUsers
        * Fixed warnings for python3.8

* IOSXR
    * Updated ShowRouteIpv4:
        * Changed regex to support some VRF values such as 'L:111'
    * Updated ShowRouteIpv4:
        * Changed regex to support some VRF values such as 'L:111'
    * Updated ShowLacp
        * Change in order to parse show lacp {interface}.
    * Updated ShowBundle
        * Change in order to parse show bundle {interface} reasons 
    * Updating symbolic link to platform specific unittests
    * Updated ShowRouteIpv4
        * Added and updated regex
        * Added unittest
    * Updated and removed regex to accommodate outputs
    * Added new unittest 
    * Updated and added regex to accommodate more outputs
    * Added new output to unittest
    * Updated regex to accommodate more outputs
    * Added extra key to schema
    * Added new unittest

* NXOS
    * Updated ShowVpc:
        * Supporting parser for vpc+ outputs
    * Updated ShowNveVniIngressReplication
        * Added regex 
        * Added new unittest
    * Updated ShowIpCefInternal
	    * Update schema and regex to support more various output

* DNAC
    * Updated Interface for:
        * Supporting hostname in the schema
