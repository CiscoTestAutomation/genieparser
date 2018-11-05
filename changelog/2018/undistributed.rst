* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

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
