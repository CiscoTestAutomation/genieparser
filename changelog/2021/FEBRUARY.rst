--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* IOSXR
    * Added Showbfdsessiondestination
        * Show Bfd Session Destination {Ip_Address}
        * Show Bfd Ipv6 Session Destination {Ip_Address}
    * Added Showmplsldpdiscovery
        * Show Mpls Ldp Discovery
        * Show Mpls Ldp Discovery Detail
        * Show Mpls Ldp Afi-All Discovery
        * Show Mpls Ldp Discovery <Ldp>
        * Show Mpls Ldp Vrf <Vrf> Discovery
        * Show Mpls Ldp Vrf <Vrf> Discovery Detail
    * Added Showmribevpnbucketdb
        * Parser For Show Mrib Evpn Bucket-Db
    * Modified Show_Pim.Py
        * Added Show Pim Topology Summary
        * Added Show Pim Vrf <Vrf> Topology Summary
    * Added Showrouteallsummary
        * Show Route Afi-All Safi-All Summary
        * Show Route Vrf All Afi-All Safi-All Summary
        * Show Route Vrf <Vrf> Afi-All Safi-All Summary

* IOSXE
    * Added 'Show Track' Parser
        * Added Schema And Parser To Iosxe/Show_Track.Py
        * Added Test Files In Iosxe/Tests/Showtrack Test Directory
    * Added Showipslasummary
        * Show Ip Sla Summary
    * Added Class Showipeigrpinterfaces
        * Added Parser For "Show Ip Eigrp Interfaces"
    * Added Class Showipeigrpinterfacesschema
        * Added Schema For Showipeigrpinterfaces Class ("Show Ip Eigrp Interfaces")
    * Added Parser For Show Flow Monitor Sdwan_Flow_Monitor Statistics Command
    * Showsdwanbfdhistory
        * Added Parser For Show Sdwan Bfd History Command
    * Added Parser For Show Sdwan Appqoe Aoim-Statistics
        * Showsdwanappqoeaoimstatistics
    * Added Showswitchstackportssummary
        * 'Show Switch Stack-Ports Summary'
    * Added ShowIpNbarVersion
        * 'show ip nbar version'

* IRONWARE
    * Initial Creation Of Ironware Parsers
    * Added Parsers
        * Show Interfaces Brief
        * Show Ip Interfaces
        * Show Media <Interface>
        * Show Mpls Lsp
        * Show Mpls Vll <Vll>
        * Show Mpls Vll-Local <Vll>
        * Show Mpls Ldp Neighbor
        * Show Optic <Slot>
        * Show Ip Ospf Neighbor
        * Show Ip Ospf Interface Brief
        * Show Ip Route
        * Show Ip Route Summary

* NXOS
    * Added Showeigrptopologyschema
    * Added Showeigrptopologysuperparser
    * Added Showipv4Eigrptopology
    * Added Showipv6Eigrptopology
        * For 'Show Ip Eigrp Topology'
        * For 'Show Ipv6 Eigrp Topology'

* IOS
    * Added Showinventory For Asr901
        * To Support Asr901 Output


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* IOSXE
    * Modified Showspanningtreedetail
        * Optional Interface Issue For Spanning Tree Output
    * Modified Showenvironmentall
        * Handling For Tab Characters In Output
    * Modified Showplatform
        * Enhanced Regex And Logic To Parse Various Outputs.
    * Updated Showinterfaces
        * Made Several Keys Optional
    * Modified Showauthenticationsessions
        * Show Authentication Sessions - Allow N/A As Method
    * Modified Showbgpsummarysuperparser
        * Update Code To Convert As-Colon To As-Plain For Bgp-Id
    * Modified Showbootvar
        * To Make 'Configuration_Register' Optional
    * Patch Showmplsldpdiscovery
    * Updated Showaccesslists
        * Added `Acl_Type` To Distinguish Standard, Extended Or Ipv6
    * Modified Showswitchstackportssummary
        * 'Show Switch Stack-Ports Summary'
    * Modified Showswitchstackportssummary
    * Changed Neighbor, Link_Changes_Count From Schema To Int (Was String).
    * Added Cli/Empty/Empty_Output_Ouput.Txt
    * Updated Cli/Equal/Golden_Output1_Output.* For Integer Change Above

* NXOS
    * Modified Showinterface
        * Handling For "(Sfp Checksum Error)" And "(No Operational Members)"
    * Modify Showipinterfacevrfall
        * Fix Regex
    * Modified Showrunningconfignvoverlay
        * Fixed Regex To Support More Output
    * Removed Showsysteminternall2Fwdermac Class
        * Removed For Duplicated
    * Updated Showcdpneighborsdetail
        * Support Various Outputs

* JUNOS
    * Modified Showipv6Neighborsschema
        * Made Key Optional
    * Modified Showroutetable
        * Made Keys Optional
        * Fixed Regex
    * Modified Showinterfaces
        * Added Optional Key Ifff-User-Mtu
    * Modified Showinterfaces
        * Made Key Cos-Queue-Configuration Optional
    * Modified Pingmplsrsvp
        * Updated Code To Sopport Different Output
    * Updated Showospf3Interfaceextensive
        * Updated Regex P4 To Captured Varied Output
    * Updated Showospf3Interfaceextensive
        * Updated Regex To Capture Capture Bdr Addr
    * Updated Showtaskreplication
        * To Support Various Outputs
    * Updated Showlogfilename
        * Removed Unneeded Output As Logging Lines
    * Updated Showlogfilenamematchexcept
        * Removed Unneeded Output As Logging Lines

* IOS
    * Modified Showinventory
        * Enhanced Logic To Parse Various Outputs.

* IOSXR
    * Modify Showarpdetail
        * Change Regex To Capture Bundle-Ether Interfaces
    * Modified Showrunningconfigbgp
        * Update Code To Convert As-Colon To As-Plain For Bgp-Id
    * Modified Showbgpinstancesummary
        * Update Regex To Support Vrf Name In Lowercase
    * Update Showplatform
        * Fixed To Run Unittests Successfully
    * Updated Showlogging
        * Fixed To Collect Logs With Include Option

