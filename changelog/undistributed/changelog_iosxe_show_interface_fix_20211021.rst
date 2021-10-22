--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowIpInterface:
        * Added if statements to broadcast address logic to check for existence
          of 'ipv4' and 'address' in interface_dict
        * Allows unnumbered interfaces to pass since they report a broadcast
          address but do not have an IP address.
