* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------


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
    * Updated ShowPolicyMapTypeSuperParser
	    * Changed key 'service_policy', 'policy_name', 'priority_level' to Optional
		* Updated regex match queue_limit
    * Updated ShowAccessLists, ShowAccessListsSummary
        * Changed protocol names 'tcp; udp; pim' of l3 into 'ipv4' or 'ipv6'
