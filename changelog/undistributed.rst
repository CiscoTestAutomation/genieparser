* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* JUNOS
    * Added ShowLDPSession
        * show ldp session
--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* JUNOS
    * Updated ShowOspfDatabaseAdvertisingRouterSelfDetail
        * Added more keys to the schema, in order to support output of ShowOspfDatabaseLsaidDetail
    * Updated ShowSystemUsers
        * Regex issues resolved
* IOSXE
    * Updated ShowCdpNeighbors
        * Modified regex to support different output
    * Updated ShowCdpNeighborsDetail
        * Modified regex to support different output
    * Updated ShowIpInterface
        * Enhanced parser and added optional values

* NXOS
    * Updated ShowIpRoute
        * Enhanced parser

* IOSXR
    * Updated ShowOspfVrfAllInclusiveDatabaseOpaqueArea
        * Enhanced parser
    * Updated ShowIsisSpfLogDetail:
        * Added more regex patterns to support various outputs.
    * Updated ShowIsisInterface:
        * Modified to support default as instance name
