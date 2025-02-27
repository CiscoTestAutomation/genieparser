--------------------------------------------------------------------------------
                            Fix
--------------------------------------------------------------------------------
* IOSXR
    * Modified ShowVrfAllDetail:
        * Modified regex <p4_1> to capture all interface names
            * Replaced the previous regex that relied on specific interface prefixes (e.g., Gi, Bun, Ten, etc.) with a more general pattern.
        * Introduced `in_interfaces_section` flag for accurate section tracking