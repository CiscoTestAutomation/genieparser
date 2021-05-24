--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowVersionSchema:
        * Add `air_license_level` and `next_reload_air_license_level` keys
    * Modified ShowVersion:
        * Add regex for AIR license level and type
        * Refactor license package parser implementation
