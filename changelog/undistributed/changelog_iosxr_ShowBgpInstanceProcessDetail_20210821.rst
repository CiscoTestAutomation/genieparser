--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXR
    * Modified ShowBgpInstanceProcessDetailSchema:
        * Modified key 'as_number' to Or(int, str). This captures dotted Notation ASN which is string.
    * Modified ShowBgpInstanceProcessDetail:
        * Modified RegEx <p4> to capture dotted Notation ASN in BGP

