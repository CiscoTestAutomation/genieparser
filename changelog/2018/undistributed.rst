* Please follow the template we introduced in OCTOBER.md file.
* Every parser need to be added under the corresponding feature.


--------------------------------------------------------------------------------
                                ROUTING
--------------------------------------------------------------------------------

* NXOS
    * parser fix for 'show ip|ipv6 route vrf all' on output 
      '*via 172.16.0.1, Eth1/1, [110/81], 3w6d, ospf-Underlay, intra' which ospf is not a number

--------------------------------------------------------------------------------
                                INTERFACE
--------------------------------------------------------------------------------
* IOSXE
    * remove duplicated ShowEtherchannelSummary parser from 
      iosxe show_interface.py, keep the one in shwo_lag.py, and combine two structures

* IOSXR
    * fix parser schema for ShowInterfaceBrief to hve key 'ethernet' as optional

* IOS
    * Added parsers for below commands:
        * show interfaces
        * show ip interface brief
        * show ip interface brief | include Vlan
        * show ip interface brief | include <WROD>
        * show ip interface
        * show ipv6 interface
        * show interfaces accounting
        * show interfaces <interface> accounting

--------------------------------------------------------------------------------
                                PLATFORM
--------------------------------------------------------------------------------
* IOSXE
    * fix regexp for 'show version' to support more output to get version information

--------------------------------------------------------------------------------
                                OSPF
--------------------------------------------------------------------------------
* IOSXR
    * fix regexp to support area output as non-digit id
