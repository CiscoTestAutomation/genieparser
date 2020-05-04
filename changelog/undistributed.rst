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
