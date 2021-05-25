May 2021
========

May 25th - Genie v21.5
----------------------

+-----------------------------------+-------------------------------+
| Module                            | Version                       |
+===================================+===============================+
| ``genie``                         | 21.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.health``             | 21.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.clean``              | 21.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.conf``               | 21.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.filetransferutils``  | 21.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.ops``                | 21.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.parser``             | 21.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.robot``              | 21.5                          |
+-----------------------------------+-------------------------------+
| ``genie.libs.sdk``                | 21.5                          |
+-----------------------------------+-------------------------------+
| ``genie.telemetry``               | 21.5                          |
+-----------------------------------+-------------------------------+
| ``genie.trafficgen``              | 21.5                          |
+-----------------------------------+-------------------------------+

Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    pip install --upgrade ats[full] # For internal user
    pip install --upgrade pyats[full] # For DevNet user

If you have pyATS installed, you can use:

.. code-block:: bash

    pyats version update

Changelogs
^^^^^^^^^^

genie
"""""
--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* json
    * Fix 'make json' implementation to the GitHub URL is using the correct path

* harness
    * Datafile content order is preserved during loading.
    * Default execution order of triggers and verifications is no longer alphabetical. It is now as provided in the yaml file.


genie.libs.health
"""""""""""""""""

--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* health
    * Modified internal functions
        * To support 'run_condition' in yaml and 'testscript' variables for device check
    * Modified internal functions
        * To support Markup '%VARIABLES{}' for 'health_sections'/'health_uids'/'health_groups'

genie.libs.clean
""""""""""""""""

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* com
    * Modified copy_to_device
        * So the stage continues even if a file cannot be deleted when freeing up disk space.
    * Modified Device Recovery
        * To respect current result in case device recovery did nothing

* iosxe
    * Modified install_image stage dialogs so clean can enter 'y' at the reload prompt

* ioxe
    * Modified clean stage 'install_image'
        * Updated execute error pattern
    * Modified clean stage 'install_package'
        * Updated execute error pattern

* apic clean
    * Modified fabric_upgrade stage to upgrade only if needed
    * Added copy_to_device stage for APIC and included disk space check and cleanup if needed

* filetransferutils
    * Modified APIC plugin, added deletefile implementation

* sdk
    * Added new APIs for APIC

genie.libs.conf
"""""""""""""""

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos conf
    * Modified Vlan class
        * Fix vn_segment_id config

genie.libs.filetransferutils
""""""""""""""""""""""""""""

No changes.

genie.libs.ops
""""""""""""""

No changes.

genie.libs.parser
"""""""""""""""""

--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxr
    * Added ShowOspfDatabase
        * show ospf database
        * show ospf {process_id} database
    * Added ShowOspfv3InterfaceSchema
    * Added ShowOspfv3Interface
        * show ospfv3 interface
    * Added ShowOspfv3Database
        * show ospfv3 database
        * show ospfv3 {process_id} database
    * Added ShowOspfv3VrfAllInclusiveNeighborDetail
        * show ospfv3 vrf all-inclusive neighbor detail
    * Added ShowOspfv3Neighbor
        * show ospfv3 neighbor
        * show ospfv3 {process} neighbor
        * show ospfv3 vrf {vrf} neighbor
        * folder based unittests

* iosxe
    * Added ShowIpEigrpTopology
        * Added parser for "show ip eigrp topology" & "show ip eigrp vrf {vrf} topology"
        * Added 4 regexp, r1, r2, r3, r4 to ShowEigrpTopologySuperparser
        * Added folder based unittests
    * Added ShowIpv6EigrpTopology
        * Added parser for "show ipv6 eigrp topology" & "show ipv6 eigrp vrf {vrf} topology"
        * Added 4 regexp, r1, r2, r3, r4 to ShowEigrpTopologySuperparser
        * Added folder based unittests
    * Added ShowIpNbarVersion

* apic
    * Added parsers for 'fnvread', 'df' and 'ls' commands

* linux
    * Added parsers for 'ls' commands

* add show command 'show ip nbar version'

* add folder based unittests


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowIpRouteSummary
        * Update p1 regex to capture output related to spacing for 'show ip route summary'
        * Add folder based unittests
    * Modified ShowInterfaces
        * Updated regex pattern p1 and p1_1 to accommodate various outputs.
        * Add folderbased unittest.
    * Modified ShowIpInterface
        * Updated regex pattern p1 and to accommodate various outputs.
        * Add folderbased unittest.
    * Modified ShowIpv6Interface
        * Updated regex pattern p1 and to accommodate various outputs.
        * Add folderbased unittest.
    * Modified ShowPlatformSoftwareStatusControl
        * Fixed regex
    * Modified ShowBgpNeighborSuperParser
        * Update regex <p22> to properly match Current Prefixes
    * Modified ShowApDot115GhzSummary
        * Update schema to accept optional mode field
    * Modified ShowInventory
        * Add regex p1_8 to accept additional NAMES for 'show inventory' command
        * Update logic to include missing NAMES if they exists
        * Add folder based unittests
    * ShowRouteMapAll
        * Updated show route-map regex's to allow special characters in places where they should be allowed
        * Update test to cover more of the regex's and to include match_community_list key
    * Modified ShowInterfacesAccounting
        * to support various output
    * Modified ShowVersionSchema
        * Add `air_license_level` and `next_reload_air_license_level` keys
    * Modified ShowVersion
        * Add regex for AIR license level and type
        * Refactor license package parser implementation
    * Modified ShowInterface class
        * Normalize interface name
    * Modified ShowStandbyAll
        * Refactor parser so that it commits data to standby_all_dict after parsing all lines
        * Fix group name regex so that it works with subinterfaces

* viptela
    * Modified ShowOmpPeers
        * updated regex pattern p1 to accommodate full-length site id strings
        * updated folderbased unittest
        * this updates IOSXE ShowSdwanOmpPeers

* iosxr
    * Modified ShowL2vpnBridgeDomainBrief
        * Class now parses its own output instead of calling and returning another class' output verbatim.
        * This is helpful because the Brief version of the command outputs in a different format.
    * Added ShowL2vpnBridgeDomainSchema
        * Schema needed to support modifications to ShowL2vpnBridgeDomainBrief
    * Modified Ping
        * Changed pattern p4 to work with IP addresses that cannot be pinged
        * Added unittest

* nxos
    * Modified ShowInterfaceStatus
        * to support various output
    * Modified ShowCdpNeighborsDetail
        * Fixed issue with parser that affected Jupyter notebooks

* update logic to include mode field when it exist in the cli output

* update regex p1 to include tx_pwr field with or without star
    * Add folder based unittests

* ios
    * ShowRouteMapAll
        * Update test to include match_community_list key
    * Show Boot command now uses the IOSXE 'show boot' parser instead of IOSXE 'show bootvar'

* nxos
    * Modified ShowInterfaceBrief
        * Updated regex p4 to remove false positives
        * Updated schema to not require an ethernet interface

genie.libs.robot
""""""""""""""""

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* robot
    * Fixed testbed loading
    * Deprecated 'use genie testbed' keyword

genie.libs.sdk
""""""""""""""

--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * Modified delete_unprotected_files API
        * Added allow_failure argument to silently allow file deletion to fail
    * Modified restore_running_config
        * Update Unicon reply dialog pattern for restore_running_config

* iosxe
    * Modified delete_unprotected_files API
        * Added allow_failure argument to silently allow file deletion to fail
    * Modified restore_running_config
        * Update Unicon reply dialog pattern for restore_running_config

* com
    * Modified free_up_disk_space API
        * Added allow_deletion_failure argument to silently allow file deletion to fail

* blitz
    * Modified 'add_result_as_extra' decolator for pyATS Health Check
        * Fixed multi process issue with loop and parallel
    * Check if NETCONF subsccribe operation RPC message contains lxml objects.

* ios
    * Modified restore_running_config
        * Update Unicon reply dialog pattern for restore_running_config


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* ios
    * Added 'get_boot_variables' API for IOS

* iosxe
    * Fixed unconfigconfigOspf
        * Fixed Verify_unconfig in unconfigconfigOspf to handle empty parser exception which happens when there is only one OSPF instance configured
        * Method handles empty parser exception and now looks for OSPF ID in list of OSPF IDs in parsed output
    * Added VRF argument to 'configure_ntp_server' API

* common api
    * Added 'arithmetic_operations' API to calculate operands.

* utils
    * added new API 'get_bool'
        * simple API to return boolean result against value such as string, integer, dict, list and so on
    * added new API 'get_testcase_name'
        * to get testcase name from 'runtime' object

* blitz
    * added support to evaluate just value without operator
        * 'if $VARIABLES{test}' will return boolean result based on content of test. no operator required. if variable is not ready/initialized, it will be treated as 'None'

genie.telemetry
"""""""""""""""

No changes.

genie.trafficgen
""""""""""""""""

