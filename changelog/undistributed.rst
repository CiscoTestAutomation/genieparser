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
    * Added ShowIpBgpRegexp for:
        * show ip bgp regexp ^$ 
    * Added ShowBootvar for:
        * 'show bootvar'

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
    * Added ShowIpBgpRegexp:
        * show ip bgp regexp ^$ 
    * Moved ShowBootvar to iosxe folder

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
* IOSXE
    * Updated ShowIpCefInternal
	    * Update schema and regex to support more various output