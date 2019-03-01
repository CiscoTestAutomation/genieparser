| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 19.0.0        |

--------------------------------------------------------------------------------
                                    SYSTEM
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowClock for 'show clock'

--------------------------------------------------------------------------------
                                    SESSION
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowLine for 'show line'
    * Add ShowUsers for 'show users'

--------------------------------------------------------------------------------
                                    ARP
--------------------------------------------------------------------------------
* NXOS
    * Fixed ShowIpArpstatisticsVrfAll for 'show ip arp statistics'

--------------------------------------------------------------------------------
                                    PLATFORM
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowProcessesCpuPlatform for 'show processes cpu platform'
    * Add ShowProcessesCpu for 'show processes cpu'
    * Enhanced ShowProcessesCpuSorted for 'show processes cpu sorted'
    * Add ShowEnvironmentAll for 'show environment all' - ASR1K
    * Add ShowEnvironment for 'show environment'

* NXOS
    * Fixed ShowInstallActive for 'show install active'

--------------------------------------------------------------------------------
                                    NTP
--------------------------------------------------------------------------------
* IOSXE
    * Add ShowNtpAssociationsDetailSchema for 'show ntp associations detail'


| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 3.1.17        |

--------------------------------------------------------------------------------
                                    FEATURE
--------------------------------------------------------------------------------
* Added the new `get_parser` feature

--------------------------------------------------------------------------------
                                    BGP
--------------------------------------------------------------------------------
* IOSXE
    * Fixed ShowBgpAllDetail and ShowBgpAllNeighbors in IOSXE to cover all types of vrf(s) and next_hop(s)

--------------------------------------------------------------------------------
                                    NTP
--------------------------------------------------------------------------------
* IOSXR
    * Add ShowRunningConfigNtp for 'show running-config ntp'

--------------------------------------------------------------------------------
                                    INTERFACE
--------------------------------------------------------------------------------
* NXOS
  * Fixed show_interface - ShowInterfaceSwitchport

* IOSXR
  * Fixed parser 'show interface detail' to support non utf8 characters

--------------------------------------------------------------------------------
                                    OSPF
--------------------------------------------------------------------------------
* NXOS
    * Fixed ShowIpOspfInterface and ShowIpOspfDatabaseOpaqueAreaDetail to cover N7K output differences

--------------------------------------------------------------------------------
                                    HSRP
--------------------------------------------------------------------------------
* NXOS
    * Fixed ShowHsrpAll to cover N7K output differences