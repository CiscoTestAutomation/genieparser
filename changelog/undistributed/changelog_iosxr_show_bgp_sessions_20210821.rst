--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXR
    * Modified ShowBgpSessionsSchema:
        * Modified key 'as_number' to Or(int, str). This captures dotted Notation ASN which is string.
    * Modified ShowBgpSessions:
        * Modified RegEx <p1>,<p1_2> to capture dotted Notation ASN in BGP

