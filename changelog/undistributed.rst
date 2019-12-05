* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* NXOS:
    * Added ShowErrdisableRecovery for
        * show errdisable recovery
		
* IOSXE
    * Added ShowProcessesMemory for:
        * show processes memory
        * show processes memory | include {include}
    * Added ShowAccessSessionInterfaceDetails for:
        * show access-session interface {interface} details
		
* NXOS
    * Added ShowIsisHostnameDetail for commands:
        * show isis hostname detail
        * show isis hostname detail vrf {vrf}
		
* IOS
    * Added ShowAccessSessionInterfaceDetails for:
        * show access-session interface {interface} details
	
--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXR
    * Updated ShowIsis
        * Updated regex to support more various output

* NXOS
    * Updated ShowAccessLists for:
        * Updated few keys' names, one key's type by following ACL's Ops structure
    * Updated ShowIpv6MldLocalGroups for:
        * Added support for various device outputs
    * Updated ShowIpv6MldGroups for:
        * Added support for various device outputs
    * Updated ShowIsisHostname for:
        * Updated int to list for level key

* IOSXE
    * Updated ShowPolicyMapTypeSuperParser
	    * Changed key 'service_policy', 'policy_name', 'priority_level' to Optional
		* Updated regex match queue_limit
    * Updated ShowAccessLists, ShowAccessListsSummary
        * Changed protocol names 'tcp; udp; pim' of l3 into 'ipv4' or 'ipv6'

* IOSXR
    * Updated ShowRouteIpv4 for:
        * Updated schema to support more ouput
        * Removed ShowRouteIpDistributor, ShowRouteIpWord class
    * Updated ShowRouteIpv6 for:
        * Updated schema to support more ouput
        * Removed ShowRouteIpv6Distributor, ShowRouteIpv6Word class
    * Updated ShowAuthenticationSessionsInterfaceDetails
	    * Changed key 'template' to Optional
		* Added 'security_policy' and 'security_status' to 'server_policies'
		* Added a regex to match Server Policies
* IOSXE
    * Updated ShowBgpDetailSuperParser
        * Added keys to schema to accomodate different outputs
        * Updated regex to catch different outputs
