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

* IOSXE
    * Updated ShowMacAddressTable for new commnad:
        * show mac address-table vlan {vlan}

* IOS
    * Updated ShowMacAddressTable for new commnad:
        * show mac address-table vlan {vlan}

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------

* IOSXE
    * Fixed ShowBootvar to support more outputs
    * Removed duplicate ShowBoot parser & fixed existing ShowBoot parser
    * Fixed ShowDmvpn not executing the command properly on device
    * Update ShowIpRoute:
        * Fixed regex for VRF name, now supports the '-' character in name.
    * Updated ShowInterfacesSwitchport:
        * Fixed the order of conditional statements, now the parser can parse the device output correctly
* NXOS
    * Updated ShowIpStaticRouteMulticast:
        * Change key 'address_family' into Optional
    * Updated ShowRunInterface:
        * Add regex to support various sample outputs
    * Updated ShowInterfaceStatus:
        * Fix a regex pattern to support various outputs

* IOSXR
    * Updated ShowBgpSessions:
        * Added regex to support various outputs
    * Updated ShowBgpInstanceNeighborsDetail:
        * Updated regex to support various outputs
* LINUX
    * Fixed Ifconfig parser issues.

* JUNOS
    * Updated ShowRoute:
        * Update regex to support various outputs.
    * Updated ShowRouteProtocolExtensive:
        * Update key 'validation-state' as Optional

