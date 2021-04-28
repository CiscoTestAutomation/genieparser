--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* NXOS
    * Modified Showversion
        * Show Version
    * Modified Showforwardingipv4
        * Updated Regex Patterns P3 And, P3_1 To Accommodate Various Outputs.
    * Modified Showrunningconfignvoverlay
        * Fixed Regex To Support More Output
    * Modified Showbgppolicystatisticsparser
        * Change Xml.Getchildren To List(Item) Because Of Python 3.9 Deprecation
    * Modified Showvrf
        * Update Regex To Accommodate Reason That Are More Than One Word.
        * Added New Folder Based Unittests.
    * Modified Showlldpneighborsdetail
        * Update Regex P5 And P6 To Handle Spaces In System_Name And System_Description For 'Show Lldp Neighbors Detail' Command.
        * Converted Unittestss To New Folder Based Unittests And Add New Unittests.
    * Removed Showsysteminternall2Fwdermac Class
        * Removed For Duplicated
    * Modified Showiproute
        * Updated Regex Pattern <Next_Hop> To Accommodate Various Outputs.
    * Modified Showinterfacebrief
        * To Support Only Port-Channel Interfaces In The Output
    * Updated Showcdpneighborsdetail
        * Support Various Outputs
    * Modified Showinterface
        * Handling For "(Sfp Checksum Error)" And "(No Operational Members)"

* IOSXE
    * Modified Showspanningtreedetail
        * Optional Interface Issue For Spanning Tree Output
    * Modified Showiproute
        * Updated Src_Protocol_Dict To Contain New Key Codes Including '+', '%', 'P', '&' For Static, Connected, Bgp, Ospf, Eigrp Routes
        * Modified Regex Pattern P3 For Both Ipv4 And Ipv6 Tables To Include Above Symbols When Parsing
        * Modified Regex Pattern P3 To Include Next Hop Vrf. Before Vrf Was In Brackets And Was Being Treated As An Outgoing Interface Which Was Incorrect
        * Added Vrf Field For Next Hop In Output Dictionary Of Show Ip Route.
    * Added Parser For Show Flow Monitor Sdwan_Flow_Monitor Statistics Command
    * Patch Showmplsldpdiscovery
    * Updated Showaccesslists
        * Added `Acl_Type` To Distinguish Standard, Extended Or Ipv6
    * Modified Ping
        * Added Arguments For Ping Api
        * Updated Regex To Support Various Outputs
    * Updated Showinterfaces
        * Made Several Keys Optional
    * Modified Showbootvar
        * To Make 'Configuration_Register' Optional
    * Modified Showauthenticationsessions
        * Show Authentication Sessions - Allow N/A As Method
    * Modified Showbgp
        * Update Cli_Command To Accept 'Show Bgp {Address_Family} Unicast'.
        * Add Folder Based Unittests.
    * Modified Showplatform
        * Enhanced Regex And Logic To Parse Various Outputs.
    * Modified Showbgpsummarysuperparser
        * Update Code To Convert As-Colon To As-Plain For Bgp-Id
    * Showsdwanbfdhistory
        * Added Parser For Show Sdwan Bfd History Command
    * Added Class Showipeigrpinterfaces
        * Added Parser For "Show Ip Eigrp Interfaces"
    * Added Class Showipeigrpinterfacesschema
        * Added Schema For Showipeigrpinterfaces Class ("Show Ip Eigrp Interfaces")
    * Modified Showenvironmentall
        * Handling For Tab Characters In Output
    * Modified Showiproute
        * To Fix An Issue When Using These Parser With Ops Where The Command Variable Would Be Overwritten
    * Modified Showipv6Route
        * To Fix An Issue When Using These Parser With Ops Where The Command Variable Would Be Overwritten
    * Modified Showiprouteword
        * To Fix An Issue When Using These Parser With Ops Where The Command Variable Would Be Overwritten
    * Modified Showipv6Routeword
        * To Fix An Issue When Using These Parser With Ops Where The Command Variable Would Be Overwritten
    * Modified Showswitchstackportssummary
        * 'Show Switch Stack-Ports Summary'
    * Modified Showswitchstackportssummary
    * Changed Neighbor, Link_Changes_Count From Schema To Int (Was String).
    * Added Cli/Empty/Empty_Output_Ouput.Txt
    * Updated Cli/Equal/Golden_Output1_Output.* For Integer Change Above

* JUNOS
    * Modified Showroutetable
        * Made Keys Optional
        * Fixed Regex
    * Modified Showchassisenvironmentfpc
        * Updated P_Power Regex Pattern
        * Made Voltage Key Optional
    * Modified Showchassispower
        * Changed Some Keys To Optional.
        * Added Regex To Capture Wider Variety Of Device Output
    * Modified Showipv6Neighborsschema
        * Made Key Optional
    * Modified Showinterfaces
        * Added Optional Key Ifff-User-Mtu
    * Modified Showinterfacesdescriptions
        * Update Regex P2 - Description - To Accommodate Spaces For 'Show Interfaces Descriptions'.
        * Add Folder Based Unittests.
    * Modified Showddosprotectionprotocol
        * Accounted For Fpc Slots
    * Modified Pingmplsrsvp
        * Updated Code To Sopport Different Output
    * Updated Showinterfaces
        * Updated P2 Regex. Added ? To `(, +Generation +\S+)`
        * Added P32_1. Checks For `Addresses`
    * Modified Showchassispower
        * Changed Some Keys To Optional.
        * Added Regex To Capture Wider Variety Of Device Output
    * Modified Filelistdetailschema
    * Modified Pingschema
    * Modified Showarpnoresolveschema
    * Modified Showarpschema
    * Modified Showbgpgroupbriefschema
    * Modified Showbgpsummaryschema
    * Modified Showchassisalarmsschema
    * Modified Showchassisenvironmentcomponentschema
    * Modified Showchassisenvironmentfpcschema
    * Modified Showchassisfabricplaneschema
    * Modified Showchassisfabricsummaryschema
    * Modified Showchassisfirmwareschema
    * Modified Showchassisfpcpicstatusschema
    * Modified Showchassisfpcschema
    * Modified Showchassishardwaredetailschema
    * Modified Showchassishardwareextensiveschema
    * Modified Showchassishardwareschema
    * Modified Showchassispicfpcslotpicslotschema
    * Modified Showchassisroutingengineschema
    * Modified Showconfigurationprotocolsmplspathschema
    * Modified Showddosprotectionprotocolschema
    * Modified Showfirewalllogschema
    * Modified Showinterfacesdescriptionsschema
    * Modified Showinterfacesdiagnosticsopticsschema
    * Modified Showinterfacespolicersinterfaceschema
    * Modified Showinterfacesqueueschema
    * Modified Showinterfacesschema
    * Modified Showinterfacesstatisticsschema
    * Modified Showipv6Neighborsschema
    * Modified Showkrtqueueschema
    * Modified Showlacpinterfacesinterfaceschema
    * Modified Showlacpstatisticsinterfacesinterfaceschema
    * Modified Showldpdatabasesessionipaddressschema
    * Modified Showldpneighborschema
    * Modified Showospf3Databaseextensiveschema
    * Modified Showospf3Databaseexternalextensiveschema
    * Modified Showospf3Databaselinkadvertisingrouterschema
    * Modified Showospf3Databasenetworkdetailschema
    * Modified Showospf3Databaseschema
    * Modified Showospf3Interfaceextensiveschema
    * Modified Showospf3Interfaceschema
    * Modified Showospf3Neighborextensiveschema
    * Modified Showospf3Neighborinstanceallschema
    * Modified Showospf3Neighborschema
    * Modified Showospf3Routenetworkextensiveschema
    * Modified Showospf3Routerouteschema
    * Modified Showospfdatabaseadvertisingrouterselfdetailschema
    * Modified Showospfdatabaseextensiveschema
    * Modified Showospfdatabaseexternalextensiveschema
    * Modified Showospfdatabasenetworklsaiddetailschema
    * Modified Showospfdatabaseopaqueareaschema
    * Modified Showospfdatabaseschema
    * Modified Showospfdatabasesummaryschema
    * Modified Showospfinterfaceextensiveschema
    * Modified Showospfneighborextensiveschema
    * Modified Showospfneighborinstanceallschema
    * Modified Showospfneighborschema
    * Modified Showospfroutebriefschema
    * Modified Showospfroutenetworkextensiveschema
    * Modified Showospfrouteprefixschema
    * Modified Showospfstatisticsschema
    * Modified Showppmtransmissionsprotocolbfddetailschema
    * Modified Showpferoutesummaryschema
    * Modified Showrsvpneighbordetailschema
    * Modified Showrsvpsessionschema
    * Modified Showrouteadvertisingprotocoldetailschema
    * Modified Showrouteadvertisingprotocolschema
    * Modified Showrouteforwardingtablelabelschema
    * Modified Showrouteforwardingtablesummaryschema
    * Modified Showrouteinstancedetailschema
    * Modified Showrouteinstancenameschema
    * Modified Showrouteprotocolextensiveschema
    * Modified Showroutereceiveprotocolextensiveschema
    * Modified Showroutereceiveprotocolpeeraddressextensiveschema
    * Modified Showroutereceiveprotocolschema
    * Modified Showrouteschema
    * Modified Showroutesummaryschema
    * Modified Showroutetablelabelswitchednameschema
    * Modified Showservicesaccountingaggregationtemplateschema
    * Modified Showservicesaccountingerrorsschema
    * Modified Showservicesaccountingflowschema
    * Modified Showservicesaccountingmemoryschema
    * Modified Showservicesaccountingstatusschema
    * Modified Showservicesaccountingusageschema
    * Modified Showsnmpconfigurationschema
    * Modified Showsnmpstatisticsschema
    * Modified Showsystemcommitschema
    * Modified Showsystemconnectionsschema
    * Modified Showsystemcoredumpsschema
    * Modified Showsystemqueuesschema
    * Modified Showsystemstatisticsschema
    * Modified Showsystemstorageschema
    * Modified Showsystemusersschema
    * Modified Showteddatabaseipaddressschema
    * Modified Showversiondetailschema
    * Modified Showversioninvokeonallroutingenginesschema
    * Modified Showversionschema
    * Modified Traceroutenoresolveschema
        * Using Listof Instead Of Use
    * Modified Showservicesaccountingaggregationtemplate
        * Allowed For Multiple Entries
    * Updated Showospf3Interfaceextensive
        * Updated Regex To Capture Capture Bdr Addr
    * Modified Showinterfaces
        * Made Key Cos-Queue-Configuration Optional
    * Modified Showchassispicfpcslotpicslot
        * Fixed Uptime Regex
            * Accounted For Seconds And Second
            * Accounted For Lack Of Hours
    * Updated Showospf3Interfaceextensive
        * Updated Regex To Capture Capture Bdr Addr
    * Updated Showospf3Interfaceextensive
        * Updated Regex P4 To Captured Varied Output
    * Modified Showchassispicfpcslotpicslot
        * Fixed Uptime Regex
            * Accounted For Seconds And Second
            * Accounted For Lack Of Hours
    * Updated Showtaskreplication
        * To Support Various Outputs
    * Modified Showchassisenvironmentfpc
        * Updated P_Power Regex Pattern
        * Made Voltage Key Optional

* IOS/CAT6K, IOS/C7600, IOSXE/CAT4K, NXOS
    * Modified Showmoduleschema Class
        * Add 'Slot' Key
    * Modified Showmodule
        * Add Slot Value To Leaf

* UTILS
    * Turn The Unittest Code Into A Standalone Importable
    * Modified Common()
        * Change Xml.Getchildren To List(Item) Because Of Python 3.9 Deprecation
    * Turn The Unittest Code Into A Standalone Importable

* IOSXR
    * Modified Ping
        * Added Arguments For Ping Api
        * Updated Regex To Support Various Outputs
    * Update Showplatform
        * Fixed To Run Unittests Successfully
    * Modified Showinterfacesdescription
        * Update Regex P2 - Description - To Accommodate Spaces For 'Show Interfaces Description'.
    * Modified Showethernettags
        * Removed Cli_Command From Showethernettags In 'Show_Ethernet.Py'
        * Migrated Unitest For 'Show Ethernet Tags' To New Style Unittests 'Showethernettags' Folder
        * Removed 'Src/Genie/Libs/Parser/Iosxr/Tests/Test_Show_Ethernet_Yang.Py'
        * Removed 'Src/Genie/Libs/Parser/Iosxr/Tests/Test_Show_Interface.Py' Since All Unittests In This File Have Been Migrated To New Unittests Folder
    * Modified Showlldpentry
        * Update Regex P2 To Handle Spaces In Chassis_Id For 'Show Lldp Neighbors Detail' Command.
        * Add Folder Based Unittests.
    * Modified Showrunningconfigbgp
        * Update Code To Convert As-Colon To As-Plain For Bgp-Id
    * Modified Showbfdsession
        * Changed <Async_Msec> And <Echo_Msec> From Schema To Optional.
        * Changed Showbfdsession Folder Tests To Reflect This Change
        * Removed Showbfdsession From Parser Unittest Ignore List
    * Modified Showbgpinstancesummary
        * Update Parser To Accept Numbers And Dotted Numbers For Remote_As In P17_2.
    * Modify Showarpdetail
        * Change Regex To Capture Bundle-Ether Interfaces
    * Modified Showbgpinstancesummary
        * Update Regex To Support Vrf Name In Lowercase
    * Updated Showlogging
        * Fixed To Collect Logs With Include Option

* ASA
    * Modified Showinterfaceipbrief
        * Updated Regex Patterns <Method> And <Link_Status> To Properly Capture Device Output

* IOS
    * Modified Showinventory
        * Enhanced Logic To Parse Various Outputs.
    * Added Class Showipeigrpinterfaces
        * Added Parser For "Show Ip Eigrp Interfaces"

* IOSXE AND IOSXE/C9500
    * Modified Showversion
        * Added Label And Build_Label Keys To Schema
        * Added Xe_Version Key To Show Version Schema
        * Updated Regex Patterns P0 To Catch Xe_Version
        * Updated Regex P1/P3 To Catch Label And Build_Label
        * Update Version_Short To Match Major.Minor For Xe/9500

* IOS-XR
    * Modified Showcdpneighborsdetail
        * Updated Regex Pattern <Platform> To Accommodate Various Outputs.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* IOSXR
    * Added Following Commands For Dir
        * Dir Location {Location}
        * Dir {Directory} Location {Location}
    * Modified Show_Pim.Py
        * Added Show Pim Topology Summary
        * Added Show Pim Vrf <Vrf> Topology Summary
    * Added Showmplsldpdiscovery
        * Show Mpls Ldp Discovery
        * Show Mpls Ldp Discovery Detail
        * Show Mpls Ldp Afi-All Discovery
        * Show Mpls Ldp Discovery <Ldp>
        * Show Mpls Ldp Vrf <Vrf> Discovery
        * Show Mpls Ldp Vrf <Vrf> Discovery Detail
    * Added Showusers
        * Show User
    * Added Following Commands For Dir
        * Dir Location {Location}
        * Dir {Directory} Location {Location}
    * Added Showbfdsessiondestination
        * Show Bfd Session Destination {Ip_Address}
        * Show Bfd Ipv6 Session Destination {Ip_Address}

* IOSXE
    * Added Showsdwanzbfwstatistics
        * Show Sdwan Zbfw Zonepair-Statistics
    * Added Parser For Show Sdwan Appqoe Aoim-Statistics
        * Showsdwanappqoeaoimstatistics
    * Added Showipslasummary
        * Show Ip Sla Summary
    * Added 'Show Track' Parser
        * Added Schema And Parser To Iosxe/Show_Track.Py
        * Added Test Files In Iosxe/Tests/Showtrack Test Directory
    * Added Showswitchstackportssummary
        * 'Show Switch Stack-Ports Summary'
    * Added Showsdwanzbfwstatistics
        * Show Sdwan Zbfw Zonepair-Statistics
    * Modified Showvrrp
        * Changed Schema To Allow Track_Group To Optionally Be Nested Level With Most Other Key/Value Pairs.
            * Added Regex Pattern <Track> To Accommodate Various Outputs.
            * Added Key <Flags> Into The Schema.
    * Added Parser Capabilities And A New 'Show Vrrp All' Parser To Handle The Following Commands
        * Show Vrrp All
        * Show Vrrp Interface {Interface}
        * Show Vrrp Interface {Interface} All
        * Show Vrrp Interface {Interface} Group {Group}
        * Show Vrrp Interface {Interface} Group {Group} All
    * Added Showipnbarclassificationsocket
        * Show Ip Nbar Classification Socket-Cache <Number_Of_Sockets>

* NXOS
    * Added Showusers
        * Show User
    * Added Ping
        * Ping {Addr}
        * Ping {Addr} Source {Source} Count {Count}
    * Added Showeigrptopologyschema
    * Added Showeigrptopologysuperparser
    * Added Showipv4Eigrptopology
    * Added Showipv6Eigrptopology
        * For 'Show Ip Eigrp Topology'
        * For 'Show Ipv6 Eigrp Topology'
    * Modified Showinterfacebrief
        * Modified Parser To Accommodate Nve Related Config.
        * `Show Interface Brief Nve 1`
    * Added Showenvironment
        * For 'Show Environment'
    * Added Showenvironmentfan
        * For 'Show Environment Fan'
    * Added Showenvironmentfandetail
        * For 'Show Environment Fan Detail'
    * Added Showenvironmentpower
        * For 'Show Environment Power'
    * Added Showenvironmentpowerdetail
        * For 'Show Environment Power Detail'
    * Added Showenvironmenttemperature
        * For 'Show Environment Temperature'
        * For 'Show Environment Temperature Module {Module}'
    * Added Showinterfacecapabilities
        * For 'Show Interface Capabilities'
        * For  'Show Interface {Interface} Capabilities'
    * Added Showinterfacetransceiver
        * For 'Show Interface Transceiver'
        * For 'Show Interface {Interface} Transceiver'
    * Added Showinterfacetransceiverdetails
        * For 'Show Interface Transceiver Details'
        * For 'Show Interface {Interface} Transceiver Details'
    * Added Showinterfacefec
        * For 'Show Interface Fec'
    * Added Showinterfacehardwaremap
        * For 'Show Interface Hardware-Mappings'

* IOS
    * Added Ping
        * Ping {Addr}
        * Ping {Addr} Source {Source} Repeat {Count}
    * Added Showinventory For Asr901
        * To Support Asr901 Output

* ADDED NEW TESTS TO THE IOSXE/TESTS/SHOWVRRP FOLDER

* ADDED TESTS AND TEST FOLDER IOSXE/TESTS/SHOWVRRPALL

* ADDED TESTS AND TEST FOLDER IOSXE/TESTS/SHOWVRRPBRIEF

* ADDED TESTS AND TEST FOLDER IOSXE/TESTS/SHOWVRRPBRIEFALL

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

* ADDED SHOWROUTEALLSUMMARY
    * Show Route Afi-All Safi-All Summary
    * Show Route Vrf All Afi-All Safi-All Summary
    * Show Route Vrf <Vrf> Afi-All Safi-All Summary


