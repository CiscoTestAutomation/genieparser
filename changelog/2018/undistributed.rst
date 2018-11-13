* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.


| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                INTERFACE
--------------------------------------------------------------------------------
* NXOS
    * Fix for ShowInterfaceSwitchport on different output for key admin_priv_vlan_trunk_private_vlans

--------------------------------------------------------------------------------
                                LAG
--------------------------------------------------------------------------------
* NXOS
    * Fix for IOSXE ShowPagpNeighbor to replace '\t' to 0 or more spaces ' *'

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
        * show processes cpu sorted <1min|5min|5sec>
        * show processes cpu sorted | include <WORD>
        * show processes cpu sorted <1min|5min|5sec> | include <WORD>
