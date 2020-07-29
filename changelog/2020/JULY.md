| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |    20.7       |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* JUNOS
    * Added ShowTedDatabaseIpAddress
        * show ted database {ipaddress}
    * Created ShowMPLSLSPNameDetail
        * show mpls lsp name {name} detail
    * Created ShowMPLSLSPNameExtensive
        * show mpls lsp name {name} extensive
    * Show Ospf3 Route Network Extensive
        * Created ShowOspf3RouteNetworkExtensive
    * Added ShowBFDSesssion
        * show bfd session
    * Added ShowBFDSesssionDetail
        * show bfd session {ipaddress} detail
    * Added ShowLDPSession
        * show ldp session
    * Added ShowClassOfService
        * show class-of-service interface {interface}
    * Added ShowRouteForwardingTableLabel
        * show route forwarding-table label {label}
    * Added ShowRSVPSession
        * show rsvp session
    * Added ShowRSVPNeighbor
        * show rsvp neighbor
    * Added ShowLdpDatabaseSessionIpaddress
        * show ldp database session ipaddress
    * Added ShowLdpNeighbor
        * show ldp neighbor
    * Added ShowRSVPNeighborDetail
        * show rsvp neighbor detail
    * Added ShowOspfDatabaseOpaqueArea
        * show ospf database opaque-area
    * Added ShowLDPInterface
        * show ldp interface {interface}
    * Added ShowLDPInterfaceDetail
        * show ldp interface {interface} detail
    * Added PingMplsRsvp
        * ping mpls rsvp {rspv}
    * Added TracerouteNoResolve
        * traceroute {ipaddress} no-resolve
    * Added Ping
        * ping {addr} ttl {ttl} count {count} wait {wait}
* IOSXE
    * Added ShowLicense
        * show license
    * Added ShowPlatformHardwareQfpActiveFeatureAppqoe
        * show platform hardware qfp active feature appqoe stats all

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------
* JUNOS
    * Updated ShowOspfDatabaseAdvertisingRouterSelfDetail
        * Added more keys to the schema, in order to support output of ShowOspfDatabaseLsaidDetail
        * ospf-lsa-topology now optional
    * Updated ShowSystemUsers
        * Regex issues resolved
    * Updated ShowOspfOverview
        * Optional key issue resolved
    * Updated ShowInterfaceExtensive
        * No longer breaks on use and previously unused data is now used
    * Updated ShowOspfDatabaseExtensiveSchema
        * Optional key issue resolved
    * Updated ShowOspf3DatabaseExtensiveSchema
        * Optional key issue resolved
    * Updated ShowOspfVrfAllInclusive
        * key error resolved
    * Updated ShowOspfDatabaseLsaidDetail
        * Resolved issue where empty output would cause error
        * ospf-lsa-topology now optional
    * Updated ShowOspf3DatabaseExtensive
        * Missing key issue resolved
        * show ospf3 database advertising-router {address} extensive
        * show ospf3 database {lsa_type} advertising-router {address} extensive
    * Updated ShowOspf3Database
        * List ospf-area
    * Updated ShowOspfDatabaseExtensiveSchema
        * Modified ShowOspfDatabaseExtensiveSchema to have optional keys
        * Missing key added
    * Updated ShowOspf3Overview
        * Missing key added
    * Updated ShowSystemUptime
        * Fixed optional key error, improved regex, and fixed return results
    * Updated ShowInterfaces
        * Optional key issue resolved
        * Regex modified to support more output
        * 'show interfaces extensive {interface}' changed to 'show interfaces {interface} extensive'
    * Updated TracerouteNoResolve
        * Change key 'hops' into Optional
* IOSXE
    * Updated ShowCdpNeighbors
        * Modified regex to support different output
    * Updated ShowCdpNeighborsDetail
        * Modified regex to support different output
    * Updated ShowIpInterface
        * Enhanced parser and added optional values
    * Updated ShowSegmentRoutingTrafficEngPolicy
        * Enhanced the schema to support updated outputs
    * Updated ShowPlatformIntegrity
        * to pretty print the rpc reply for netconf
    * Updated ShowVersion
        * Enhanced parser
    * Updated ShowProcessesMemory
        * Modified schema to support different output

* NXOS
    * Updated ShowIpRoute
        * Enhanced parser

* IOSXR
    * Updated ShowOspfVrfAllInclusiveDatabaseOpaqueArea
        * Enhanced parser
    * Updated ShowIsisSpfLogDetail:
        * Added more regex patterns to support various outputs.
    * Updated ShowIsisInterface:
        * Modified to support default as instance name
    * Updated ShowInterfaces:
        * Added more regex patterns to support various outputs.

