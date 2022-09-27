--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Fix ShowLispSiteDetail to account for the instance in which port number is not available in the show output
    * Regex parser modified to account for missing port number
    * Modified ShowRunInterface
        * Changed p49 to work with 'switchport trunk allowed vlan add' feature
    * Modified ShowFlowMonitorAll
    * Modified ShowIpv6Routers parser
        * Modified ShowIpv6Routers to include VRF
    * Modified ShowPlatformSoftwareFactoryResetSecureLog
        * Added one optional key
    * Modified ShowLoggingOnboardRpActiveUptime
        * Modified p9 to match chassis type as string.There is no backward compatability to match 'chassis_type' as integer.
    * Fixed ShowPlatformFedSwitchActiveIfmMapping
        * Github issue#3888 fixed which incorrectly choose parser from C9600 due to exact match.
    * Modified ShowEnvironment
        * Added regex pattern p10,p11,p12 to match different outputs for cli "show env power"
    * Fix ShowL2vpnEvpnMacIpDetail to support additional type of interface as next-hop
    * Fixed ShowLicenseTechSupport
        * Fix the parser to support the new output from a newer sw version of the device.
    * Fixed ShowUdldNeighbor parser
        * Modified regexp to match SVL port and port_ID details as per new output change
    * Modified ShowunInterface  Added the ipv6 flow monitor in/output data in the script
    * Fixed ShowSystemMtu
        * Parser for show system mtu
    * Modified ShowMacAddressTable
    * Modified ShowPlatformFedActiveIfmMapping
        * Modified "Optional('IFG_ID') str,

* nxos
    * Fix ShowUsers regex patterns to accommodate additional outputs.

* cheetah
    * Fix ShowCapwapClientRcb to handle optional keyword


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxr
    * Added ShowBgpNeighborsAdvertisedCount
        * show bgp {address-family} neighbors {neighbor} advertised-count
    * Added ShowRcmdServer
        * show rcmd server
    * Added ShowRcmdIsisEventSpf
        * show rcmd isis {isis} event spf
    * Added ShowRcmdIsisEventPrefix
        * show rcmd isis {isis} event prefix
    * Added ShowRcmdIsisEventStatisticsPrefix
        * show rcmd isis {isis} event statistics prefix
    * Added ShowRcmdIsisEventIpfrr
        * show rcmd isis {isis} event ip-frr
    * Added ShowRcmdLdpEventRemotelfa
        * show rcmd ldp event remote-lfa
    * Added ShowRcmdLdpEventSession
        * show rcmd ldp event session

* iosxe
    * Added ShowCtsPolicyServerStatistics
        * show cts policy-server statistics all
        * show cts policy-server statistics active
        * show cts policy-server statistics name <server_name>
    * Added ShowCtsPolicyServerDetails
        * show cts policy-server details all
        * show cts policy-server details active
        * show cts policy-server details name <server_name>
    * Added ShowInterfacesStatusModule
        * added new parser for cli ' ShowInterfacesStatusModule '
    * Modified ShowPlatformhardwarefedactiveTcamUtilization
        * parser for platform hardware fed active Tcam utilization details
        * parser for platform hardware fed  switch active Tcam utilization details
    * Modified ShowProcessesMemorySchema
        * processor_pool changed as a optional
    * Added ShowPlatformSoftwareFedActiveAclSgacl
        * show platform software fed active acl sgacl cell all
        * show platform software fed {switch} active acl sgacl cell all
    * Added ShowFpBdMac
        * show platform software bridge-domain Fp active <bd_id> mac-table
        * show platform software bridge-domain Fp active <bd_id> mac-table <mac_address>
    * Added ShowFpEncapOce
        * show platform software evpn Fp active encap-oce index <oce_index> detail
    * Added ShowFQDNPacketStatistics
        * added new parser for cli "show fqdn packet statistics"
    * Added ShowAccessSessionBrief parser
        * Added ShowAccessSessionBrief parser
    * Added ShowFQDNDatabase
        * added new parser for cli "show fqdn database"
    * Added ShowPlatformSoftwareFedSwitchActiveAclUsage
        * added new parser for cli "show paltform software fed switch active acl usage"


