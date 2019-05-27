* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                   interface
--------------------------------------------------------------------------------
* NXOS
    * Updated ShowInterface
        * added show interface {interface} to support custom interface
    * Updated ShowIpInterfaceVrfAll
        * added show ip interface vrf {vrf},
                show ip interface {intf} vrf all,
                show ip interface {intf} vrf {vrf} to support custom interface and vrf
    * Updated ShowVrfAllInterface
        * added show vrf {vrf} interface {interface},
                show vrf {vrf} interface,
                show vrf all interface {interface} to support custom interface and vrf
    * Updated ShowInterfaceSwitchport
        * added show interface {interface} switchport to support custom interface
    * Updated ShowIpv6InterfaceVrfAll
        * added show ipv6 interface vrf {vrf},
                show ipv6 interface {intf} vrf all,
                show ipv6 interface {intf} vrf {vrf} to support custom interface and vrf

--------------------------------------------------------------------------------
                                   Routing
--------------------------------------------------------------------------------
* NXOS
    * Updated ShowRoutingVrfAll
        * added show routing vrf {vrf} to support custom vrf
    * Updated ShowRoutingIpv6VrfAll
        * added show ipv6 routing vrf {vrf} to support custom vrf