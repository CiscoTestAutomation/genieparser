--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* JUNOS
    * Added Showppmtransmissionsprotocolbfddetail
        * Show Ppm Transmissions Protocol Bfd Detail
    * Added Showchassisfabricsummary
    * Added Showchassisfabricplane
    * Added Showservicesaccountingaggregationtemplate
        * Show Services Accounting Aggregation Template Template-Name {Name} Extensive
    * Added Showservicesaccountingusage
        * Show Services Accounting Usage
    * Added Showservicesaccountingerrors
        * Show Services Accounting Errors
    * Added Showservicesaccountingflow
        * Show Services Accounting Flow
    * Added Showservicesaccountingmemory
        * Show Services Accounting Memory
    * Added Showservicesaccountingstatus
        * Show Services Accounting Status
    * Fixed Showbgpsummaryinstance
        * Show Bgp Summary Instance {Instance}
    * Modified Showinterfacesdescriptions
        * Added A Command Show Interfaces Descriptions {Interface}
    * Added Showchassisenvironment
        * Show Chassis Environment
    * Added Showchassisalarms
        * Show Chassis Alarms
    * Added Showddosprotectionstatistics
        * Show Ddos-Protection Statistics
    * Added Showchassispicfpcslotpicslot
    * Updated Traceroutenoresolve
        * Added Command 'Traceroute {Ipaddress} Source {Ipaddress2} No-Resolve'
    * Added Showlogfilename
        * Show Log {Filename} | Match {Match}
        * Show Log {Filename} | Match {Match} | Except {Except_}
    * Added Showinterfacesinterfacedetail
        * Show Interfaces {Interface} Detail
    * Added Showlacpstatisticsinterfacesinterface
        * Show Lacp Statistics Interfaces {Interface}
    * Added Showbfdsessionaddressextensive
        * Show Bfd Session Address {Ipaddress} Extensive
    * Added Showconfigurationsystemntp
        * Show Configuration System Ntp
    * Updated Showinterfaces
        * Added Show Interfaces {Interface}
    * Added Showospfneighborname
    * Added Showospf3Neighborname
    * Added Showinterfacesdiagnosticsoptics
        * Show Interfaces Diagnostics Optics {Interface}
        * Show Interfaces Diagnostics Optics
    * Added Showospfrouteprefix
        * Show Ospf Route {Prefix}
    * Added Showospf3Routeprefix
        * Show Ospf3 Route {Prefix}
    * Added Showrouteinstancename
        * Show Route Instance {Name}
    * Added Showvdcresourcedetail
        * Optional Output Support Added

* NXOS
    * Aci
        * Added Acidiagfnvread For
            * Acidiag Fnvread
        * Added Showfirmwareupgradestatus For
            * Show Firmware Upgrade Status
            * Show Firmware Upgrade Status Switch-Group {Switch_Group}
        * Added Showfirmwareupgradestatuscontrollergroup For
            * Show Firmware Upgrade Status Controller-Group
        * Added Showfirmwarerepository For
            * Show Firmware Repository
    * Aci
        * Removed Acidiagfnvread (Moved To Os=Apic)
            * Acidiag Fnvread
        * Removed Showfirmwareupgradestatus (Moved To Os=Apic)
            * Show Firmware Upgrade Status
            * Show Firmware Upgrade Status Switch-Group {Switch_Group}
        * Removed Showfirmwareupgradestatuscontrollergroup (Moved To Os=Apic)
            * Show Firmware Upgrade Status Controller-Group
        * Removed Showfirmwarerepository (Moved To Os=Apic)
            * Show Firmware Repository
    * Added Showforwardingipv4
        * 'Show Forwarding Ipv4'
        * 'Show Forwarding Ipv4 Vrf {Vrf}'
    * Added Showvdcresourcedetail
        * Show Vdc Resource Detail
        * Show Vdc Resource {Resource} Detail

* IOSXE
    * Ping
        * For 'Ping {Address} Source {Source} Repeat {Repeat}'
    * Added Showvrrp
        * For 'Show Vrrp'
    * Added Show Ip Ospf Neighbor Detail__
        * So It Would Work Without Device Output As Well
    * C9200
        * Added Showenvironmentall For
            * Show Environment All
    * C9400
        * Added Showenvironmentall
            * Show Environment All
            * Show Environment All | Include <Include>
        * Added Showenvironment
            * Show Environment
            * Show Environment | Include <Include>
    * Added Showaptagsummary
        * Show Ap Tag Summary
    * Added Showavcsdserviceinfosummary
        * Show Avc Sd-Service Info Summary
    * Added Showchassisrmi
        * Show Chassis Rmi
    * Added Showctsapsgtinfo
        * Show Cts Ap Sgt Info
    * Added Showctswirelessprofilepolicy
        * Show Cts Wireless Profile Policy
    * Added Showdevicetrackingdatabaseinterface
        * Show Device-Tracking Database Interface {Interface}
    * Showipospfinterface2
        * Show Ip Ospf Interface__
            * Added So It Works Offline
    * Showipospfmplstrafficenglink2
        * Show Ip Ospf Mpls Traffic-Eng Link__
            * Added So It Works Offline
    * Showipospfshamlinks2
        * Show Ip Ospf Sham Link__
            * Added So It Works Offline
    * Showipospfvirtuallinks2
        * Show Ip Ospf Virtual Link__
            * Added So It Works Offline
    * Added Showlispeidtablevrfipv4Database
        * Show Lisp Eid-Table Vrf Ipv4 Database
    * Added Showlispeidtablevrfuseripv4Mapcache
        * Show Lisp Eid-Table Vrf User Ipv4 Map-Cache
    * Added Showlispinstanceidethernetserver
        * Show Lisp Instance-Id Ethernet Server
    * Added Showsdwanpolicyipv6Accesslistassociations
        * Show Sdwan Policy Ipv6 Access-List-Associations
    * Added Showsdwanpolicyaccesslistassociations
        * Show Sdwan Policy Access-List-Associations
    * Added Showsdwanpolicyaccesslistcounters
        * Show Sdwan Policy Access-List-Counters
    * Added Showsdwanpolicyipv6Accesslistcounters
        * Show Sdwan Policy Ipv6 Access-List-Counters
    * Added Showsnmp
        * Show Snmp
    * Added Showtelemetryinternalconnection
        * Show Telemetry Internal Connection
    * Added Showtenantsummary
        * Show Tenant-Summary
    * Added Showtenantompsummary
        * Show Tenant {Tenant_Name} Omp Summary
    * Added Showtenantomppeers
        * Show Tenant {Tenant_Name} Omp Peers
    * Added Showtenantomproutesadvertised
        * Show Tenant {Tenant_Name} Omp Routes Advertised
        * Show Tenant {Tenant_Name} Omp Routes Vpn {Vpnid} Advertised
    * Added Showwirelessclientmacdetail
        * Show Wireless Client Mac Detail
    * Added Showwirelessfabricvnidmapping
        * Show Wireless Fabric Vnid Mapping
    * Added Showwirelessstatsclientdeletereasons
        * Show Wireless Stats Client Delete Reasons
    * Added Showwirelessstatsclientdetail
        * Show Wireless Stats Client Detail
    * Added Showwlanidclientstats
        * Show Wlan Id Client Stats

* IOSXR
    * Ping
        * For 'Ping {Address} Source {Source} Repeat {Repeat}'
    * Added Showbfdsessiondestinationdetails
        * Supports Show Bfd Session Destination {Ip_Address} Details
        * Supports Show Bfd Ipv6 Session Destination {Ip_Address} Details
    * Added Showipv6Interface
    * Added Showbfdsession
        * Show Bfd Session
    * Modified Show_Mfib.Py
        * Added Show Mfib Platform Evpn Bucket Location {Location}

* APIC
    * Added Acidiagfnvread (From Os=Nxos, Platform=Aci)
        * Acidiag Fnvread
    * Added Showfirmwareupgradestatus (From Os=Nxos, Platform=Aci)
        * Show Firmware Upgrade Status
        * Show Firmware Upgrade Status Switch-Group {Switch_Group}
    * Added Showfirmwareupgradestatuscontrollergroup (From Os=Nxos, Platform=Aci)
        * Show Firmware Upgrade Status Controller-Group
    * Added Showfirmwarerepository (From Os=Nxos, Platform=Aci)
        * Show Firmware Repository

* COMMON
    * Added Local Parser Extension Support For Devat

* SROS
    * Added Showservicesapusing
        * Show Service Sap-Using


--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* JUNOS
    * Fixed Showbfdsessiondetail
        * Cli Command Should Be 'Show Bfd Session Address {Ipaddress} Detail'
    * Modified Showospfneighbor
        * Fixed Cli_Command Error
    * Added Showddosprotectionprotocol
        * Show Ddos-Protection Protocols {Protocol}
    * Fixed Showroutetable
        * Updated Regex To Support More Output
    * Modified Showchassisfabricsummary
        * Updated P1 Regex To Consider Wider Variety
    * Showinterfaces
        * Enhanced Regex For Input Error Counter
    * Showsnmpstatistics
        * Made Snmp-Performance-Statistics Optional
    * Showntpassociations
        * Fixed Regex For Remote Field
    * Showinterfacesschema
        * Made Keys Optional
    * Showlacpinterfacesinterface
        * Fixed Regex
    * Showinterfacesextensive
        * Fixed Regex
    * Showsystemuptime
        * Fixed Regex
    * Modified Showbfdsessiondetail
        * To Cover More Output Pattern
    * Modified Showospfrouteprefix
        * Changed Ospf-Next-Hop In Schema From Dict To List To Support Multiple Nexthops
    * Modified Showopsf3Routeprefix
        * Changed Ospf-Next-Hop In Schema From Dict To List To Support Multiple Nexthops
    * Modified Showchassisenvironmentcomponent
        * Fixed To Parse Description To Cover Vary Outputs
    * Modified Showddosprotectionprotocol
        * To Cover More Output Pattern
    * Modified Showinterfaces
        * Fixed To Parse Description To Cover Vary Outputs
    * Modified Showinterfaces
        * To Cover More Output Pattern
    * Updated Showbgpsummary
        * Handled Regex To Support Various Output
    * Updated Showchassisenvironmentcomponent
        * Power Regex Updated
    * Modified Showchassisfpc
        * Made Keys Optional
    * Modified Showospfneighborinstanceall
        * Made Keys Optional
    * Modified Showospf3Neighborinstanceall
        * Made Keys Optional
    * Modified Showroutesummary
        * Made As-Number Key Optional
    * Updated Ping
        * Added Command 'Ping {Addr} Source {Source} Size {Size} Do-Not-Fragment Count {Count}'
    * Modified Showbgpsummary
        * Changed 'Bgp-Thread-Mode' To Optional.
        * Updated Regex Pattern <P5> To Accommodate Various Outputs.
    * Updated Ping
        * Modified The If-Condition To Handle Cases Properly.
    * Updated Showddosprotectionstatistics
        * Changed A Few Keys Into Optional
    * Showchassishardware
        * Updated Parser To Support Various Outputs
    * Showchassisenvironment
        * Updated Regex Pattern P1 To Support Various Outputs
    * Showlogfilename
        * Added One Edge Unit Test
    * Modified Showchassisalarms
        * Updated The Schema
    * Showlogfilename
        * Added 'Except {Except_Show_Log}' To Command 'Show Log {Filename} | Except {Except_Show_Log} | Match {Match}'
    * Showtaskreplication
        * Added Two Optional Keys Task-Protocol-Replication-Name And Task-Protocol-Replication-State
    * Modified Ping
        * Added A New Command 'Ping {Addr} Size {Size} Count {Count} Do-Not-Fragment'
    * Modified Traceroutenoresolve
        * Updated Regex Pattern <P1> To Accommodate Various Outputs.
    * Modified Showbfdsession
        * To Support Various Outputs
    * Modified Showinterfaces
        * Updated Unittests For Parser In This Class
    * Modified Showinterfacesextensive
        * Updated Unittests For Parsers In This Class
    * Modified Showbgpsummary
        * Fixed Ut Failures
    * Modified Showinterfaces
        * Added Regex Check
    * Modified Showospf3Routenetworkextensive
        * Updated Regex Patterns P2 And P3 To Capture Varied Device Output
    * Modified Ping
        * Added Command 'Ping {Addr} Source {Source} Size {Size} Count {Count} Tos {Tos} Rapid'
    * Showrouteprotocolextensiveipaddress
        * Enhanced Code To Consider Varied Device Output
    * Modified Showrouteprotocolextensive
        * Made Line Match Code Less Likely To Break
    * Modified Showrouteprotocolextensive
        * Enhanced Code To Capture Cluster List With Variations Of Device Output
    * Modified Showrouteprotocolextensive
        * Updated Code To Handle Different Device Output
    * Modified Showservicesaccountingaggregation
        * Updated Code To Handle A Variety Of Output
    * Updated Showinterfacesterse
        * To Support Various Outputs
    * Updated Showroutetable
        * To Support Various Outputs
    * Modified Showospf3Databaseextensive
        * Made Regex More Specific To Avoid False Positives
    * Modified Showchassisfabricsummary
        * Made Show Command Lower Case
    * Modified Showchassisfabricplane
        * Made Show Command Lower Case

* IOSXE
    * Modified Showcdpneighborsdetail
        * Updated Code To Handle Scenario Where There Is No Device_Id
    * Test
        * Updated Unittests To Have Correct Output
    * Modified Showcdpneighbors
        * Updated P5 Regex To Handle Scenario Where Platform Is Vmware Es
    * Fixed Ios Show Ip Route/Show Ipv6 Route Parsers
        * Show Ip Route
        * Show Ip Route Vrf <Vrf>
        * Show Ipv6 Route
        * Show Ipv6 Route Vrf <Vrf>
        * Show Ip Route <Hostname Or A.B.C.D>
        * Show Ip Route Vrf <Vrf> <Hostname Or A.B.C.D>
        * Show Ipv6 Route <Hostname Or Abcd>
        * Show Ipv6 Route Vrf <Vrf> <Hostname Or Abcd>
    * Modified Showaptagsummary
        * To Fix An Issue Where 'Number_Of_Aps'
    * Fixed Showisisneighbors
        * Show Isis Neighbors
    * Modified Showspanningtreedetail Regex P18
        * To Cover More Output Pattern
    * C9300
        * Fixed Showenvironmentall P7 To Parse More Output Patterns
    * Modified Showlispeidtablevrfipv4Database To Parse More Various Output
    * Updated Showruninterface
        * Modified Regex Pattern P3 To Support Various Outputs
    * Modified Showruninterface
        * Added Optional Key 'Shutdown'
    * Modified Monitorinterfacetraffic
        * Changed Key 'Monitor-Time' Into Optional
    * Showinterfaces
        * Added A Unit Test
    * Modified Showaccesslistssummary
        * Fixed To Support Various Outputs
    * Modified Showaccesslists
        * Fixed An Issue In P_Ip_Acl Where The Address Of The Destination
        * Fixed An Issue In P_Ip_Acl Where The Destination Port Was Being
    * Modified Golden_Output_Output.Txt
        * Additional Access-List 'Test33' That Includes Two Entries That Would
    * Modified Golden_Output_Expected.Py
        * Matched Correct Output.
    * Modified Showcdpneighbors
        * Change Device_Id, Local_Interface, And Hold_Time Into Optional Keys
        * Enhanced Regex To Capture Values With A '.'
    * Modified Showcdpneighbors
        * Show Cdp Neighbors
            * Updated All Regex Patterns To Accommodate Various Outputs.
    * Modified Showcdpneighborsdetail
        * Added Double Quote (") Character To The Regex For `Platform`.
    * C8200
        * Updated Showplatform To Cover C8200 Output Patterns
    * Modified Showroutemapall
        * Added Regex Pattern <P26> To Accommodate Various Outputs And Fixed Location Of Match_Tag_List In Schema
    * Modified Showswitchschema
        * Made Key Optional
    * Modified Showplatform
        * Show Platform Regex Update
        * Allow For Missing Serial Number In C9500
    * Modified Showinterface
        * Show Interface Regex Update
        * Fix Single Ip Helper Address
        * Add Test For Signle Ip Helper Adddress
    * Modified Showctssxpconnectionsbrief
        * To Cover More Output Pattern

* IOSXR
    * Pep8 Formatting For Show_Evn.Py
    * Showevpnevidetail
        * Fix Output Reference To 'Out'
    * Showevpnethernetsegment
        * Fix Pattern Matches And Missing Initial Values
    * Fixed Showplatform
        * Show Platform
        * Updated Regex Pattern <P1> To Accommodate Various Outputs.
        * Modified Regex For Variable <Parse_Subslot> And <Parse_Lc> To Include Slots From [0-9].
    * Modified Showbgpinstanceallallschema
        * Made Key Optional
    * Showinterfaces
        * Made Key 'Type' Optional
    * Modified Showl2Vpnxconnectdetailschema
        * Additional Keys For Backup Pw
    * Modified Showl2Vpnxconnectdetail
        * Update Backup_Pw Logic
    * Modified Showbgpinstancesschema
        * Switched Key From Int To Or(Int, Str)
    * Modified Showbgpinstances
    * Modified Showbgpinstancesummaryschema
        * Switched Keys From Int To Or(Int, Str)
    * Modified Showbgpinstancesummary
    * Modified Showbfdsessiondestinationdetails
        * Fixed Wrong Command
    * Fixed Showipinterfacebrief Regex For More Vrf Pattern

* NXOS
    * Modified Showmodule
        * Updated Regex Pattern To Handle Parenthesis Inmodule Type Name
    * Modified Showippoute
        * Updated Code To Parse Address Families Properly In Case Of Offline Output
    * Fixed Showinterfaces To Cover More Output Patterns
    * Fixed Showipinterfacevrfall To Cover More Patterns
    * Modified Showbgpl2Vpnevpn Regex P6
        * To Cover More Output Pattern
    * Updated Shownvemultisitedcilinks P1 Regex To Parse Port-Channel Interface
    * Updated Shownvemultisitefabriclinks P1 Regex To Parse Port-Channel Interface
    * Modified Showipinterface
        * Fixed Issue To Parse Inbound/Outbound Access-List
    * Modified Showbgpl2Vpnevpnneighbors Class
        * Added Regex To Accommodate More Output
    * Showntppeerstatus
        * Enhanced To Receive Various Forms Of Input
    * Modified Showplatform
        * Fix For Show Version

* IOS
    * Cat6K
        * Fixed Showversion To Cover More Output Patterns
    * Modified Showvtpstatus
        * Made Keys Optional

* UTILS
    * Fixed The Issue That Double-Quotation(") Was Missed At Last Of Show Command

* TESTS
    * Modified Ci_Folder_Parsing.Py
        * Included -F Flag To Display Only Failed Tests
        * Can Now Run Job Using Pyats Run Job Folder_Parsing_Job.Py
        * If -V Is Included, The Show Commands Output Will Be Included


