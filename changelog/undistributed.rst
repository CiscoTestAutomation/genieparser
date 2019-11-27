* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* NXOS
    * Added ShowIsisHostnameDetail for commands:
        * show isis hostname detail
        * show isis hostname detail vrf {vrf}

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXR
    * Updated ShowIsis
        * Updated regex to support more various output

* NXOS
    * Updated ShowAccessLists for:
        * Updated few keys' names by following ACL's Ops structure
* IOSXE
    * Updated ShowIsisHostname for:
        * Updated int to list for level key
    * Updated ShowPolicyMapTypeSuperParser
	    * Changed key 'service_policy', 'policy_name', 'priority_level' to Optional
		* Updated regex match queue_limit
