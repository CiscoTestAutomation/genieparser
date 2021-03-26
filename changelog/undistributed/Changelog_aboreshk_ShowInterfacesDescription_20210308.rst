--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXR
    * Modified ShowInterfacesDescription:
        * Update regex p2 - description - to accommodate spaces for 'show interfaces description'.
    * Modified ShowEthernetTags:
        * Removed cli_command from ShowEthernetTags in 'show_ethernet.py'
        * Migrated unitest For 'show ethernet tags' to new style unittests 'ShowEthernetTags' folder
        * Removed 'src/genie/libs/parser/iosxr/tests/test_show_ethernet_yang.py'
        * Removed 'src/genie/libs/parser/iosxr/tests/test_show_interface.py' since all unittests in this file have been migrated to new unittests folder
				
* JUNOS
    * Modified ShowInterfacesDescriptions:
        * Update regex p2 - description - to accommodate spaces for 'show interfaces descriptions'.
        * Add folder based unittests.
