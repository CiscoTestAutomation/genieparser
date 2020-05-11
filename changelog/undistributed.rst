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
    * Updated ShowAccessLists:
        * Fixed a typo in code.
    * Update ShowLldpEntry:
        * Fixed regex for chassis id, now also supports ':' and '-'.
        * Fixed regex for description, now also supports messages like '{"SN":"SN-NR","Owner":"OWNER"}'.
        * Fixed regex for management addresses, now also supports IPv6 addresses.
        * Changed the following keys into Optional for 'med_information': 'f/w_revision', 'power_source', 'power_priority', 'wattage' and 'capabilities'.

* NXOS
    * Updated ShowIpStaticRouteMulticast:
        * Change key 'address_family' into Optional
    * Updated ShowRunInterface:
        * Add regex to support various sample outputs
    * Updated ShowInterface
        * Added regex to support interfaces down for SFP Not Inserted
        * Added regex to support interfaces down for ErrDisabled
        * Added regex to support interfaces down due to being suspended (LACP)

* IOSXR
    * Updated ShowBgpSessions:
        * Added regex to support various outputs
    
* LINUX
    * Fixed Ifconfig parser issues.

* JUNOS
    * Updated ShowRoute:
        * Update regex to support various outputs.

* IOS 
    * Updated ShowIpArp
        * Added argument 'output' into super().cli()
                