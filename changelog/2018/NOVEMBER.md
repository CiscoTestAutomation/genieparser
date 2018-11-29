| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 3.1.8         |

--------------------------------------------------------------------------------
                                NTP
--------------------------------------------------------------------------------

* Enhancements for the following IOSXE & IOS parsers;
    * ShowNtpAssociations
    * ShowNtpStatus
    * ShowNtpConfig


| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 3.1.7         |

--------------------------------------------------------------------------------
                                NTP
--------------------------------------------------------------------------------
* Junos
    * Add ShowNtpAssociations for 'show ntp associations'
    * Add ShowNtpStatus for 'show ntp status'
    * Add ShowConfigurationSystemNtpSet for 'show configuration system ntp | display set'

* IOSXE
    * Add ShowNtpAssociations for 'show ntp associations'
    * Add ShowNtpStatus for 'show ntp status'
    * Add ShowNtpConfig for 'show ntp config'

* IOS
    * Add ShowNtpAssociations for 'show ntp associations'
    * Add ShowNtpStatus for 'show ntp status'
    * Add ShowNtpConfig for 'show ntp config'

--------------------------------------------------------------------------------
                                INTERFACE
--------------------------------------------------------------------------------
* Junos
    * Add ShowInterfacesTerse for 'show interfaces terse'
      and 'show interfaces terse | match "intf_name"'


--------------------------------------------------------------------------------
                                TRM
--------------------------------------------------------------------------------
* NXOS
   * Update "fabric_l2_mroute" to be optional in ShowFabricMulticastIpL2MrouteSchema    


| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 3.1.6         |

--------------------------------------------------------------------------------
                                VRF
--------------------------------------------------------------------------------
* IOS
    * Add parser:
        * ShowVrfDetail


| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 3.1.5         |

--------------------------------------------------------------------------------
                                INTERFACE
--------------------------------------------------------------------------------

* NXOS
    * Fix for ShowInterfaceSwitchport on different output for key admin_priv_vlan_trunk_private_vlans

* IOS
    * Added parsers for below commands:
        * show interfaces
        * show ip interface brief
        * show ip interface brief | include Vlan
        * show ip interface brief | include \<WORD\>
        * show ip interface
        * show ipv6 interface
        * show interfaces accounting
        * show interfaces \<interface\> accounting

--------------------------------------------------------------------------------
                                LAG
--------------------------------------------------------------------------------

* NXOS
    * Fix for IOSXE ShowPagpNeighbor to replace '\t' to 0 or more spaces ' *'

--------------------------------------------------------------------------------
                                TRM
--------------------------------------------------------------------------------

* NXOS
    * Added below parsers :
      * ShowFabricMulticastGlobals
      * ShowFabricMulticastIpSaAdRoute
      * ShowFabricMulticastIpL2Mroute
      * ShowForwardingDistributionMulticastRoute
      * ShowBgpIpMvpnRouteType
      * ShowBgpIpMvpnSaadDetail
      * ShowBgpL2vpnEvpn
      * ShowBgpIpMvpn

--------------------------------------------------------------------------------
                                PLATFORM
--------------------------------------------------------------------------------

* IOS
    * Added parsers for below comands:
        * show version
        * dir
        * show redundancy
        * show inventory
        * show bootvar
        * show processes cpu sorted
        * show processes cpu sorted \<1min|5min|5sec\>
        * show processes cpu sorted | include \<WORD\>
        * show processes cpu sorted \<1min|5min|5sec> | include \<WORD\>

* NXOS
    * Updated parsers:
        * ShowInventory

--------------------------------------------------------------------------------
                                ROUTING
--------------------------------------------------------------------------------

* NXOS
    * Updated parsers:
        * ShowIpRoute

--------------------------------------------------------------------------------
                                BGP
--------------------------------------------------------------------------------

* NXOS
    * Updated parsers:
        * ShowBgpVrfAllAllSummary

# V3.1.4

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 3.1.4         |

--------------------------------------------------------------------------------
                                NTP
--------------------------------------------------------------------------------
* NXOS
    * Add ShowNtpPeerStatus for 'show ntp peer-status'
    * Add ShowNtpPeers for 'show ntp peers'



# V3.1.3

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 3.1.3         |

--------------------------------------------------------------------------------
                                ROUTING
--------------------------------------------------------------------------------

* NXOS
    * parser fix for 'show ip|ipv6 route vrf all' on output 
      '*via 172.16.0.1, Eth1/1, [110/81], 3w6d, ospf-Underlay, intra'
      which ospf is not a number
--------------------------------------------------------------------------------
                                INTERFACE
--------------------------------------------------------------------------------

* IOSXE
    * remove duplicated ShowEtherchannelSummary parser from 
      iosxe show_interface.py, keep the one in shwo_lag.py, and combine two structures

* IOSXR
    * fix parser schema for ShowInterfaceBrief to have key 'ethernet' as optional
--------------------------------------------------------------------------------
                                PLATFORM
--------------------------------------------------------------------------------

* IOSXE
    * fix regexp for 'show version' to support more output to get version information
* IOSXR
    * Add new key 'full_slot' for ShowPlatorm to parse out the full slot name
    * Fix Dir parser with different output
--------------------------------------------------------------------------------
                                OSPF
--------------------------------------------------------------------------------

* IOSXR
    * fix regexp to support area output as non-digit id
* NXOS
    * updated parser schema for ShowIpOspfMplsLdpInterface to
      support 'required' and 'achieved' as optional
--------------------------------------------------------------------------------
                                IMGP
--------------------------------------------------------------------------------

* NXOS
    * Convert interface name to standard style (Loopback, Ethernet,etc.) for 
      ShowIpIgmpGroups
--------------------------------------------------------------------------------
                                MLD
--------------------------------------------------------------------------------

* NXOS
    * Convert interface name to standard style (Loopback, Ethernet,etc.) for 
      ShowIpv6MldGroups
