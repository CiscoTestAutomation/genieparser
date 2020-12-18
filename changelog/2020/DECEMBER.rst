--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* IOSXE
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
    * Modified Showplatform
        * Show Platform Regex Update
        * Allow For Missing Serial Number In C9500
    * Modified Showinterface
        * Show Interface Regex Update
        * Fix Single Ip Helper Address
        * Add Test For Signle Ip Helper Adddress
    * Modified Showspanningtreedetail Regex P18
        * To Cover More Output Pattern
    * Fixed Showisisneighbors
        * Show Isis Neighbors
    * Modified Showcdpneighborsdetail
        * Updated Code To Handle Scenario Where There Is No Device_Id
    * C8200
        * Updated Showplatform To Cover C8200 Output Patterns
    * C9300
        * Fixed Showenvironmentall P7 To Parse More Output Patterns
    * Test
        * Updated Unittests To Have Correct Output
    * Modified Showcdpneighbors
        * Show Cdp Neighbors
            * Updated All Regex Patterns To Accommodate Various Outputs.
    * Modified Showswitchschema
        * Made Key Optional
    * Modified Showaptagsummary
        * To Fix An Issue Where 'Number_Of_Aps'
    * Updated Showruninterface
        * Modified Regex Pattern P3 To Support Various Outputs
    * Modified Showroutemapall
        * Added Regex Pattern <P26> To Accommodate Various Outputs And Fixed Location Of Match_Tag_List In Schema

* JUNOS
    * Modified Showospf3Routenetworkextensive
        * Updated Regex Patterns P2 And P3 To Capture Varied Device Output
    * Updated Ping
        * Added Command 'Ping {Addr} Source {Source} Size {Size} Do-Not-Fragment Count {Count}'
    * Modified Traceroutenoresolve
        * Updated Regex Pattern <P1> To Accommodate Various Outputs.
    * Modified Ping
        * Added Command 'Ping {Addr} Source {Source} Size {Size} Count {Count} Tos {Tos} Rapid'
    * Modified Showrouteprotocolextensive
        * Updated Code To Handle Different Device Output
    * Modified Showrouteprotocolextensive
        * Enhanced Code To Capture Cluster List With Variations Of Device Output
    * Modified Showinterfaces
        * To Cover More Output Pattern
    * Modified Showchassisfabricsummary
        * Made Show Command Lower Case
    * Modified Showchassisfabricplane
        * Made Show Command Lower Case
    * Modified Showrouteprotocolextensive
        * Made Line Match Code Less Likely To Break
    * Modified Showchassisfpc
        * Made Keys Optional
    * Modified Showbgpsummary
        * Changed 'Bgp-Thread-Mode' To Optional.
        * Updated Regex Pattern <P5> To Accommodate Various Outputs.
    * Modified Showospf3Databaseextensive
        * Made Regex More Specific To Avoid False Positives
    * Showrouteprotocolextensiveipaddress
        * Enhanced Code To Consider Varied Device Output
    * Showinterfaces
        * Enhanced Regex For Input Error Counter
    * Showsnmpstatistics
        * Made Snmp-Performance-Statistics Optional
    * Showntpassociations
        * Fixed Regex For Remote Field
    * Updated Ping
        * Modified The If-Condition To Handle Cases Properly.
    * Modified Showinterfaces
        * Added Regex Check
    * Modified Showroutesummary
        * Made As-Number Key Optional
    * Modified Showospfneighborinstanceall
        * Made Keys Optional
    * Modified Showospf3Neighborinstanceall
        * Made Keys Optional

* IOS
    * Modified Showvtpstatus
        * Made Keys Optional
    * Cat6K
        * Fixed Showversion To Cover More Output Patterns

* IOSXR
    * Fixed Showplatform
        * Show Platform
        * Updated Regex Pattern <P1> To Accommodate Various Outputs.
        * Modified Regex For Variable <Parse_Subslot> And <Parse_Lc> To Include Slots From [0-9].
    * Modified Showbgpinstanceallallschema
        * Made Key Optional
    * Showinterfaces
        * Made Key 'Type' Optional
    * Modified Show_Mfib.Py
        * Added Show Mfib Platform Evpn Bucket Location {Location}
    * Modified Showbgpinstancesschema
        * Switched Key From Int To Or(Int, Str)
    * Modified Showbgpinstances
    * Modified Showbgpinstancesummaryschema
        * Switched Keys From Int To Or(Int, Str)
    * Modified Showbgpinstancesummary

* NXOS
    * Showntppeerstatus
        * Enhanced To Receive Various Forms Of Input
    * Modified Showplatform
        * Fix For Show Version
    * Updated Shownvemultisitedcilinks P1 Regex To Parse Port-Channel Interface
    * Updated Shownvemultisitefabriclinks P1 Regex To Parse Port-Channel Interface
    * Modified Showbgpl2Vpnevpn Regex P6
        * To Cover More Output Pattern
    * Modified Showbgpl2Vpnevpnneighbors Class
        * Added Regex To Accommodate More Output
    * Fixed Showipinterfacevrfall To Cover More Patterns

* TESTS
    * Modified Ci_Folder_Parsing.Py
        * Included -F Flag To Display Only Failed Tests
        * Can Now Run Job Using Pyats Run Job Folder_Parsing_Job.Py
        * If -V Is Included, The Show Commands Output Will Be Included


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* IOSXE
    * Added Showtenantsummary
        * Show Tenant-Summary
    * Added Showtenantompsummary
        * Show Tenant {Tenant_Name} Omp Summary
    * Added Showtenantomppeers
        * Show Tenant {Tenant_Name} Omp Peers
    * Added Showtenantomproutesadvertised
        * Show Tenant {Tenant_Name} Omp Routes Advertised
        * Show Tenant {Tenant_Name} Omp Routes Vpn {Vpnid} Advertised
    * Added Showdevicetrackingdatabaseinterface
        * Show Device-Tracking Database Interface {Interface}
    * Added Showctsapsgtinfo
        * Show Cts Ap Sgt Info
    * Added Showtelemetryinternalconnection
        * Show Telemetry Internal Connection
    * Added Showwlanidclientstats
        * Show Wlan Id Client Stats
    * Added Showwirelessclientmacdetail
        * Show Wireless Client Mac Detail
    * Added Show Ip Ospf Neighbor Detail__
        * So It Would Work Without Device Output As Well
    * Added Showaptagsummary
        * Show Ap Tag Summary
    * Added Showvrrp
        * For 'Show Vrrp'
    * Added Showlispeidtablevrfuseripv4Mapcache
        * Show Lisp Eid-Table Vrf User Ipv4 Map-Cache
    * Showipospfmplstrafficenglink2
        * Show Ip Ospf Mpls Traffic-Eng Link__
            * Added So It Works Offline
    * Showipospfshamlinks2
        * Show Ip Ospf Sham Link__
            * Added So It Works Offline
    * Added Showwirelessstatsclientdetail
        * Show Wireless Stats Client Detail
    * Added Showavcsdserviceinfosummary
        * Show Avc Sd-Service Info Summary
    * Added Showctswirelessprofilepolicy
        * Show Cts Wireless Profile Policy
    * Added Showwirelessfabricvnidmapping
        * Show Wireless Fabric Vnid Mapping
    * Added Showwirelessstatsclientdeletereasons
        * Show Wireless Stats Client Delete Reasons
    * Added Showlispinstanceidethernetserver
        * Show Lisp Instance-Id Ethernet Server
    * Added Showchassisrmi
        * Show Chassis Rmi
    * Added Showsnmp
        * Show Snmp
    * Showipospfvirtuallinks2
        * Show Ip Ospf Virtual Link__
            * Added So It Works Offline
    * Added Showsdwanpolicyipv6Accesslistassociations
        * Show Sdwan Policy Ipv6 Access-List-Associations
    * Added Showsdwanpolicyaccesslistassociations
        * Show Sdwan Policy Access-List-Associations
    * Added Showsdwanpolicyaccesslistcounters
        * Show Sdwan Policy Access-List-Counters
    * Added Showsdwanpolicyipv6Accesslistcounters
        * Show Sdwan Policy Ipv6 Access-List-Counters
    * Added Showlispeidtablevrfipv4Database
        * Show Lisp Eid-Table Vrf Ipv4 Database
    * Showipospfinterface2
        * Show Ip Ospf Interface__
            * Added So It Works Offline

* JUNOS
    * Added Showchassisenvironment
        * Show Chassis Environment
    * Updated Traceroutenoresolve
        * Added Command 'Traceroute {Ipaddress} Source {Ipaddress2} No-Resolve'
    * Added Showddosprotectionstatistics
        * Show Ddos-Protection Statistics
    * Modified Showinterfacesdescriptions
        * Added A Command Show Interfaces Descriptions {Interface}
    * Added Showconfigurationsystemntp
        * Show Configuration System Ntp
    * Added Showchassisalarms
        * Show Chassis Alarms
    * Added Showospfrouteprefix
        * Show Ospf Route {Prefix}
    * Added Showospf3Routeprefix
        * Show Ospf3 Route {Prefix}
    * Added Showchassisfabricsummary
    * Added Showchassisfabricplane

* IOSXR
    * Added Showbfdsession
        * Show Bfd Session

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
    * Added Showforwardingipv4
        * 'Show Forwarding Ipv4'
        * 'Show Forwarding Ipv4 Vrf {Vrf}'
    * Added Showvdcresourcedetail
        * Show Vdc Resource Detail
        * Show Vdc Resource {Resource} Detail

* SROS
    * Added Showservicesapusing
        * Show Service Sap-Using


