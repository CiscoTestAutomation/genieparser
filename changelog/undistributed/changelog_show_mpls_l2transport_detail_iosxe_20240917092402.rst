--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowMplsL2TransportDetail:
        * Update 'show mpls l2transport vc detail' RegEx pattern p1 to include optional "Ethernet:", to match device output "Local interface: Gi0/0/2 up, line protocol up, Ethernet:29 up"
