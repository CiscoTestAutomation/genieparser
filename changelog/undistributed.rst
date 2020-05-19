* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* LINUX
    * Added ShowControllersNpuInterfaceInstanceLocation for:
        * show controllers npu {npu} interface {interface} instance {instance} location {location}
    * Added ShowControllersFiaDiagshellDiagEgrCalendarsLocation for:
        * show controllers fia diagshell {diagshell} "diag egr_calendars" location {location} 
    * Added ShowControllersFiaDiagshellDiagCosqQpairEgpMap for:
        * show controllers fia diagshell 0 "diag cosq qpair egq map" location all
    * Added ShowInstallSummary for 
        * show install summary
    * Added route
    * Added netstat -rn


* JUNOS
    * Added ShowOspfNeighborDetail for:
        * show ospf neighbor {neighbor} detail.
    * Added ShowInterfacesDescriptions for:
        * show interfaces descriptions
    * Added ShowPfeRouteSummary for:
        * show pfe route summary
    * Added ShowInterfaces for:
        * show interfaces
    * Added ShowInterfacesExtensive for:
        * show interfaces extensive
        * show interfaces extensive {interface}
    * Added ShowInterfacesExtensiveNoForwarding for:
        * show interfaces extensive no-forwarding
    * Added ShowOspfDatabaseLsaidDetail for:
        * show ospf database lsa-id {ipaddress} detail
    * Added ShowOspfDatabaseNetworkLsaidDetail for:
        * show ospf database network lsa-id {ipaddress} detail
    * Added ShowOspf3DatabaseLinkAdvertisingRouter for:
        * show ospf3 database link advertising-router {ipaddress} detail
    * Added ShowOspf3DatabaseNetworkDetail for:
        * show ospf3 database network detail

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
    * Update ShowCdpNeighborsDetail:
        * Modified regex to parse interface and port_id like FastEthernet0/0.1 and Serial0/0/0:1
    * Updated ShowInterfacesSwitchport:
        * Fixed the order of conditional statements, now the parser can parse the device output correctly
    * Updated ShowAccessLists:
        * Fixed a typo in code.
    * Update ShowVtpStatus:
        * Changed the following keys into Optional: 'maximum_vlans' and 'md5_digest'.
    * Update ShowLldpEntry:
        * Fixed regex for chassis id, now also supports ':' and '-'.
        * Fixed regex for description, now also supports messages like '{"SN":"SN-NR","Owner":"OWNER"}'.
        * Fixed regex for management addresses, now also supports IPv6 addresses.
        * Changed the following keys into Optional for 'med_information': 'f/w_revision', 'power_source', 'power_priority', 'wattage' and 'capabilities'.
    * Update ShowCdpNeighborsDetail:
        * Fixed regex for platform, now also supports ':'.
    * Update ShowVlan:
        * Fixed regex for vlan name, now also supports multiple white spaces.
        * Added regex for toking ring table.
        * Added the following keys: 'token_ring', 'are_hops', 'ste_hops' and 'backup_crf'.

* NXOS
    * Updated ShowIpStaticRouteMulticast:
        * Change key 'address_family' into Optional
    * Updated ShowRunInterface:
        * Add regex to support various sample outputs
    * Updated ShowInterfaceStatus:
        * Fix a regex pattern to support various outputs
    * Updated ShowInterface
        * Added regex to support interfaces down for SFP Not Inserted
        * Added regex to support interfaces down for ErrDisabled
        * Added regex to support interfaces down due to being suspended (LACP)

* IOSXR
    * Updated ShowBgpSessions:
        * Added regex to support various outputs
    * Updated ShowBgpInstanceNeighborsDetail:
        * Updated regex to support various outputs
    * Updated ShowLldpNeighborsDetail:
        * Updated regex to support various outputs

* LINUX
    * Fixed Ifconfig parser issues.

* JUNOS
    * Updated ShowRoute:
        * Update regex to support various outputs.
    * Updated ShowRouteProtocolExtensive:
        * Update key 'validation-state' as Optional

    * Update ShowRouteProtocolExtensive for:
        * show route {route} extensive
        * show route extensive
        * show route extensive {destination}


* IOS 
    * Updated ShowIpArp
        * Added argument 'output' into super().cli()
* ASA
    * Updated ShowRoute:
        * Fixed the logic for overlapping prefixes.
        * Fixed the OSPF protocol mappings.
        * Parser optimization for dynamic routing protocols (EIGRP, OSPF, BGP, etc)
