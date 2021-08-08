--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXR
    * Modified ShowBgpInstanceAllAllSchema:
        * Modified key 'local_as' to Or(int, str). This captures dotted Notation ASN which is string.
    * Modified ShowBgpInstanceAllAll:
        * Modified RegEx <p6>,<p16_2>,<p16>,<m3> under <p16>, <p17> to capture dotted Notation ASN in BGP

