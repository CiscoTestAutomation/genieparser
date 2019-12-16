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
    * Updated ShowPolicyMapTypeSuperParser
	    * Changed key 'service_policy', 'policy_name', 'priority_level' to Optional
		* Updated regex match queue_limit
    * Updated ShowAccessLists, ShowAccessListsSummary
        * Changed protocol names 'tcp; udp; pim' of l3 into 'ipv4' or 'ipv6'
    * Updated ShowDot1xAllDetail
	    * Modified regex for eap_method
		* Updated 'system_auth_control', 'version' as Optional keys
    * Updated ShowLispServiceMapCache, ShowLispServiceDatabase
        * EID-table default no longer breaks parsing
    * Updated ShowClnsIsNeighborsDetail
        * Changed regex and schema to support type 'L1L2'
    * Updated ShowIsisDatabaseDetail
        * Changed schema to support more various output

* IOSXR
    * Updated ShowRouteIpv4 for:
        * Updated schema to support more ouput
        * Removed ShowRouteIpDistributor, ShowRouteIpWord class
    * Updated ShowRouteIpv6 for:
        * Updated schema to support more ouput
        * Removed ShowRouteIpv6Distributor, ShowRouteIpv6Word class
    * Updated ShowAuthenticationSessionsInterfaceDetails
	    * Change in order of Server Policies no longer breaks parsing
* DNAC
    * Updated Interface for:
        * Supporting hostname in the schema