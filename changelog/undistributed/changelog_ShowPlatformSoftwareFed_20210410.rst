--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXE
    * Modified ShowPlatformSoftwareFed:
        * Updat regex P36 to include objid:ADJ SPECIAL:0 
        * Updat regex P25 and corresponding schema to include bwalk parameters
        * Modify regex P11 and corresponding schema to modify flags and pdflags from str to 
        * Modify regex P14 to include label_aal
        * Add blank lines and comments between regex
        * Add full syntax of commands
        * Modify capital letters to small letters in key name in Schema and parser class
        * Delete Optional Keyword in some of key names in Schema
        * Modify nobj0 and nobj1 from str to list in regex P9 and corresponding Schema 
        * Add folder based unittests

    * Delete iosxe/show_platform_software_fed.py instead content is Appended in iosxe/show_platform.py 