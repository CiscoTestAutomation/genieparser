* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------

* JUNOS
    * Added ShowLogFilename for:
        * show log {filename}
* JUNOS
    * Added ShowOspfNeighborDetail for:
        * show ospf neighbor {neighbor} detail
    * Added ShowBgpNeighbor for:
        * show bgp neighbor

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* NXOS
    * Updated ShowIpStaticRouteMulticast:
        * Change key 'address_family' into Optional

