--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXR
    * Modified ShowBgpInstanceNeighborsDetailSchema:
        * Modified key 'remote_as','local_as_as_no' to Or(int, str). This captures dotted Notation ASN which is string.
    * Modified ShowBgpInstanceNeighborsDetail:
        * Modified RegEx <p3> to capture dotted Notation ASN in BGP

