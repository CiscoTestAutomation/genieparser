--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* NX-OS
    * Modified ShowLldpNeighborsDetail:

      * If an NX-OS device is connected to an IOS-XR device the interface formats will be processed
        in a way that's compatible with IOS-XR devices, e.g. TenGigabitEthernet becomes TenGigE

* Utils
    * Modified Common.py - Common.convert_intf_name:
        * Dictionary containing interface conversions is now nested.
        * Created *generic* key as a catchall for previous code.
        * Edited logic to check if a specific operating system is mentions in the os= argument