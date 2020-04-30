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
    * Added ShowLogFilename for:
        * show log {filename}
    * Added ShowVersionDetail for:
        * show version detail
    * Added ShowVersionInvokeOnAllRoutingEngines for:
        * show version invoke-on all-routing-engines
    * Added ShowVersionDetailNoForarding for:
        * show version detail no-forwarding


--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------

* IOSXE
    * Fixed ShowDmvpn not executing the command properly on device

* NXOS
    * Updated ShowIpStaticRouteMulticast:
        * Change key 'address_family' into Optional

