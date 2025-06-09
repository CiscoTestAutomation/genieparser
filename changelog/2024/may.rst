--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* nxos
    * Modified ShowIpArpstatisticsVrfAll
        * Added <rewritepkt>, <droppedrewritepkt> and <del_dynamic_on_static_add> optional keys to schema.
        * Updated regex pattern <p2, <p3> and <p50> to accommodate various outputs.
    * Update p5 and p6 regex to capture only system version

* iosxe
    * Modified ShowPolicyMapTypeSuperParser Parser
        * Fix p1 regex to match interface
    * Modified ShowPlatformHardwareFedQosSchedulerSdkInterface parser
        * Fix p3_1 regex and made cstse_scheduler oid optinal
    * Modified ShowTimeRange parser
        * used_in as optional schema variable
    * Modified ShowPlatformSoftwareFedQosInterfaceIngressNpdDetailed super parser
        * Fix p5 regex and added 2 optional variables
    * Modified ShowIpRouteDistributor parser
        * Added timeout variable to parse bigger output
    * Modified ShowFlowMonitor parser
        * Updated name="" in function
    * Added support for rommonboot variable
        * Modified <p6> regex to support rommonboot variable
    * Modified ShowIsisDatabaseVerboseParser
        * Parser not taking into consideration if LSPID line is split. Also added recent changes from external parser in polaris.
    * Modified fix for ShowMkaPolicy
        * Made send_secure_announcements key as optional and expanded names of Te,Fo and Gi to accomodate various outputs
    * Modified ShowIsisHostname parser
        * Modified <p2> regex to match
    * Modified ShowMacsecSummary
        * Changed <transmit_sc>, <receive_sc> from schema to Optional.
        * Updated schema to accommodate various outputs.
        * Added regex pattern <p2> and <p3> to accommodate various outputs.
    * Modified ShowIpOspf
        * Added additional unit tests
    * Modified ShowIpOspfDatabase
        * Added additional unit tests
    * Modified ShowIpOspfDatabaseRouter
        * Added additional unit tests
    * Modified ShowIpOspfInterfaceBrief
        * Added additional unit tests
    * Modified ShowSdwanServiceChainStatsDetail
        * Added <track_obj>, <tx_tracker>, <rx_tracker>, <sent>, <dropped> and <rtt> optional keys in schema.
        * Added regex pattern <p5>, <p6>, <p7>, <p8>, <p9>, <p10>, <p11>, <p12> and <p13> to accommodate various outputs.
    * Modified ShowSdmPrefer Parser
        * Added optional parameters to schema and converted some of the keys to optional
        * Added new keys to schema
        * Fixed regex p14-p23 to parse (**) values
        * Added new regex p42-p49
    * Modified fix for ShowCdpNeighbors
        * Modified regex to accomodate various outputs
    * Modified ShowIsisDatabaseVerbose Parser
        * Converted flex algorithm parsing from a set of integers to a list of integers to enable JSON serialization capabilities

* iosxr
    * Modified fix for ShowL2vpnXconnectDetail
        * Modified parser to accomodate various outputs
    * Modified ShowIsisStatistics
        * Changed average_process_time_nsec key from schema to Optional.
        * Updated regex pattern r10, r11, r12, r13, r14, r15 to accommodate various outputs.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowPlatformHardwareChassisPowerSupplyDetailSwitchAll
        * show platform hardware chassis power-supply detail switch {mode} all
        * show platform hardware chassis power-supply detail all
    * Added ShowControllersEthernetControllersPhyDetail
        * Added schema and parser for 'show controllers ethernet-controller {interface} phy detail'
    * Added TracerouteIpAddress
        * Added parser for 'traceroute {ip_address}'
    * Added ShowPlatformHardwareFedSwitchQosQueueStatsInterface
        * parser for 'show platform hardware fed active qos queue stats interface {interface}'
    * Added ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear
        * parser for 'show platform hardware fed active qos queue stats interface {interface} clear'
    * Added ShowIpMfibStatus
        * Added 'show ip mfib status' command and schema for the command.
    * Added ShowIpv6MfibStatus
        * Added 'show ipv6 mfib status' command and schema for the command.

* nxos
    * Added ShowMacSecMkaStatsIntf
        * parser for 'show macsec mka statistics interface {interface}'
    * Added ShowMacSecPolicy
        * parser for 'show macsec policy'
    * Added ShowMacSecSecyStatistics
        * parser for 'show macsec secy statistics '


