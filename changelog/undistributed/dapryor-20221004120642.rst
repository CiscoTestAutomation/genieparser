--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIpInterface
        * Fixed bug where first line of the command is the output and the hostname contains an IP.
            This would cause the multicast reserved groups section to fail due to uninitialized variables
        * Improved Multicast reserved groups parsing when the IPs span multiple lines
