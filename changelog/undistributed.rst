* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* JUNOS
    * Added ShowBgpNeighbor for:
        * show bgp neighbor
    * Added ShowLDPOverview
        * show ldp overview
    * Added ShowOspfDatabaseAdvertisingRouterExtensive for:
        * show ospf database advertising-router {ipaddress} extensive

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* JUNOS
    * Fixed ShowBgpNeighbor:
        * Updated few keys into Optional.
* IOS
    * Fixed ShowNtpConfig:
        * Added prefered key
* IOSXE
    * Fixed ShowNtpConfig:
        * Added prefered key
