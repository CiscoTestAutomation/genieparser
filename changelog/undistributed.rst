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
    * Added ShowIsisHostnameDetail for commands:
        * show isis hostname detail
        * show isis hostname detail vrf {vrf}

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

* IOS
    * Added ShowAccessSessionInterfaceDetails for:
        * show access-session interface {interface} details

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* NXOS
    * Updated ShowRunningConfigBgp for:
        * Updated logic to support more variouos outputs

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
    * Updated ShowFabricMulticastGlobals for:
        * Added support for various device outputs
    * Updated ShowIsisInterface for:
        * update regex to support more various output
    * Updated ShowDot1xAllSummary
	    * Updated 'system_auth_control', 'version' as Optional keys
		* Added 'eap_method' as Optional key
		* Updated regex to match new values
    * Updated ShowIsisInterface for:
        * Added optional key 'passive' to schema
    * Updated ShowSpanningTreeDetail for:
        * Added support for various device outputs

* IOSXE
    * Updated ShowPolicyMapTypeSuperParser
	    * Changed key 'service_policy', 'policy_name', 'priority_level' to Optional
		* Updated regex match queue_limit
    * Updated ShowAccessLists, ShowAccessListsSummary
        * Changed protocol names 'tcp; udp; pim' of l3 into 'ipv4' or 'ipv6'
    * Updated ShowDot1xAllDetail
	    * Modified regex for eap_method
		* Updated 'system_auth_control', 'version' as Optional keys

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

* IOS
    * Updated ShowInventory for:
        * Updated logic to support more outputs

* IOSXE
    * Updated ShowBgpDetailSuperParser
        * Added keys to schema to accommodate different outputs
        * Updated regex to catch different outputs
    * Updated ShowInventory for:
        * Update one key into Optional to support more outputs

