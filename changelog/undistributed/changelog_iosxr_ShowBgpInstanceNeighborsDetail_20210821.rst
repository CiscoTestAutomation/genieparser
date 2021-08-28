--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXR
    * Modified ShowBgpInstanceNeighborsDetailSchema:
        * Modified key 'remote_as','local_as_as_no' to capture dotted Notation.
    * Modified ShowBgpInstanceNeighborsDetail:
        * Modified RegEx <p3> to capture dotted Notation ASN in BGP

