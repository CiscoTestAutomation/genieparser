--------------------------------------------------------------------------------
                                      Fix
--------------------------------------------------------------------------------

* IOSXR
    * Modified ShowPlatform for `ASR-9903` with `IOS-XR v7.8.2`:
        * Updated regex pattern <p1> to accommodate various outputs:
            * Changed whitespace before <plim> to use \s+ (was a single space) for variable spacing.
            * Made <config_state> optional by wrapping it in a non-capturing group.
        * Ensures lines without a "Config state" column are parsed (e.g., `0/0/1             A9903-20HG-PEC             OK`).