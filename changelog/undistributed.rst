* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------

* JUNOS
    * Added ShowOspfNeighborDetail for:
        * show ospf neighbor {neighbor} detail
    * Added ShowInterfacesDescriptions for:
        * show interfaces descriptions
    * Added ShowPfeRouteSummary for:
        * show pfe route summary
    * Added ShowOspfDatabaseLsaidDetail for:
        * show ospf database lsa-id {ipaddress} detail
    * Added ShowOspfDatabaseNetworkLsaidDetail for:
        * show ospf database network lsa-id {ipaddress} detail
    * Added ShowOspf3DatabaseLinkAdvertisingRouter for:
        * show ospf3 database link advertising-router {ipaddress} detail
    * Added ShowOspf3DatabaseNetworkDetail for:
        * show ospf3 database network detail

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------

* IOSXE
    * Fixed ShowBootvar to support more outputs
    * Fixed ShowDmvpn not executing the command properly on device

* NXOS
    * Updated ShowIpStaticRouteMulticast:
        * Change key 'address_family' into Optional

* LINUX
    * Fixed Ifconfig parser issues.

* JUNOS
    * Updated ShowRoute:
        * Update regex to support various outputs.
