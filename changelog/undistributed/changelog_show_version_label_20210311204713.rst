--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXE and IOSXE/C9500
    * Modified ShowVersion:
      * Added label and build_label keys to schema
      * Added xe_version key to show version schema
      * Updated regex patterns p0 to catch xe_version
      * Updated regex p1/p3 to catch label and build_label
      * Update version_short to match major.minor for XE/9500
