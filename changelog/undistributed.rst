* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowMyShowCommand for commands;
        * 'My show command'

* IOSXR
    * Added ShowMsdpPeer, ShowMsdpContext, ShowMsdpSummary, ShowMsdpSaCache, ShowMsdpStatisticsPeer for commands:
        * 'show msdp peer'
        * 'show msdp vrf {vrf} peer'
        * 'show msdp context'
        * 'show msdp vrf {vrf} context'
        * 'show msdp summary'
        * 'show msdp vrf {vrf} summary'
        * 'show msdp sa-cache'
        * 'show msdp vrf {vrf} sa-cache'
        * 'show msdp statistics peer'
        * 'show msdp vrf {vrf} statistics peer'
--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXE
    * Enhanced ShowFix;
        * Updated my code
        * Fixed bad code i wrote before

