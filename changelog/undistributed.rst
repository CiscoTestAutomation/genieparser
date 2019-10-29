* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowMyShowCommand for commands;
        * 'My show command'

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* IOSXR
    * Enhanced ShowBgpInstanceNeighborsReceivedRoutes;
        * Updated code to support various outputs
        * Added unittest corresponding to the new supported output
    * Enhanced ShowBgpInstanceSummary;
        * Updated code to support various outputs
        * Added unittest corresponding to the new supported output

--------------------------------------------------------------------------------
                                Protocols
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowIpProtocols tu sopport more outputs
--------------------------------------------------------------------------------
                                Interface
--------------------------------------------------------------------------------
* NXOS
    * Fixed regex to accommodate various outputs
* IOSXE
    * Fixed regex to accommodate more outputs
    
* IOSXE
    * Fixed parser ShowRunSectionIsis to support missing ISIS name outputs

--------------------------------------------------------------------------------
                                Interface
--------------------------------------------------------------------------------
* IOSXE
    * ShowInterfaces
        * Fixed regex to accommodate more outputs formats

--------------------------------------------------------------------------------
                                   VDC 
--------------------------------------------------------------------------------
* NXOS 
    * Updated ShowVdcDetailSchema to accomodate different outputs 

--------------------------------------------------------------------------------
                                Traceroute
--------------------------------------------------------------------------------
* IOSXR
    * Added Traceroute class

--------------------------------------------------------------------------------
                                ROUTING
--------------------------------------------------------------------------------
* IOSXE
    * Verified customer outputs
    * Added field to schema advertised_by

--------------------------------------------------------------------------------
                                ACL
--------------------------------------------------------------------------------
* IOSXE
    * ShowAccessLists
        * Updated regex to capture more outputs

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* NXOS
    * ShowIpOspf
        * Added missing keys to schema
        * Added regex to capture more outputs
