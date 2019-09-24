* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                Interface
--------------------------------------------------------------------------------
* IOSXE
<<<<<<< HEAD
    * Added ShowFlowMonitor for:
        * show flow monitor {name} cache format table
    * Added ShowFlowExporterStatistics for:
        * show flow exporter statistics
        * show flow exporter {exporter} statistics

--------------------------------------------------------------------------------
                                ROUTING
--------------------------------------------------------------------------------
* IOSXE
    * Update ShowIpCef
        * update regex to support outgoing_label_backup and outgoing_label_info
    * Update ShowIpRoute regex to support more varied output
* IOSXR
    * Updated ShowRouteIpv4:
        * Matching more routes
        * Optimized parser moving regex compilation out of for loop

--------------------------------------------------------------------------------
                                INVENTORY
--------------------------------------------------------------------------------
* IOS
    * Updated ShowInventory:
        * Matching more slots

--------------------------------------------------------------------------------
                                Spanning-tree
--------------------------------------------------------------------------------
* NXOS
    * Updated ShowSpanningTreeSummary to:
        * regex to accommodate different formats
        * changed some fields in schema to Optional
    * Updated ShowSpanningTreeDetail to:
        * updated regex to accommodate more formats
        * add support for rstp
        * changed some fields in schema to Optional
* IOSXE
    * Updated ShowSpanningTreeSummary:
        * Changed some schema keywords to Optional
        * Refined regex for various formats

--------------------------------------------------------------------------------
                                ARP
--------------------------------------------------------------------------------
* IOSXR
    * Updated ShowArpTrafficDetail to parse drop_adj key from output
* IOSXE
    * Updated ShowIpTraffic schema for more varied outputs

--------------------------------------------------------------------------------
                                VTP
--------------------------------------------------------------------------------
* IOSXE:
    * Updated ShowVtpStatusSchema to:
        * Changed schema keywords to Optional

--------------------------------------------------------------------------------
                                IPV6
--------------------------------------------------------------------------------
* NXOS
    * Updated ShowIpv6NdInterfaceVrfAll to parse more varied output

--------------------------------------------------------------------------------
                                MLD
--------------------------------------------------------------------------------
* IOSXR
    * Updated ShowMldGroupsDetail to support empty output

--------------------------------------------------------------------------------
                                lldp
--------------------------------------------------------------------------------
* IOS
    * Updated ShowLlpdEntry to:
        * Updated regex to accommodate more formats

--------------------------------------------------------------------------------
                                platform vm
--------------------------------------------------------------------------------
* IOSXR
    * Updated ShowPlatformVm to:
        * Updated regex to accommodate different formats from the outputs

--------------------------------------------------------------------------------
                                platform
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowEnvironmentAll for more varied outputs
    * Updated ShowSwitchDetail for more varied outputs
    * Updated ShowPlatformHardware for more varied outputs
    * Updated ShowPlatformSoftwareStatusControl for more varied outputs

--------------------------------------------------------------------------------
                                LAG
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowEtherChannelLoadBalancing schema for more varied outputs

--------------------------------------------------------------------------------
                                MCAST
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowIpMulticast schema for more varied outputs

--------------------------------------------------------------------------------
                                RPL
--------------------------------------------------------------------------------
* IOSXR
    * Updated ShowRplRoutePolicy:
        * Updated passing command in device.parse()

--------------------------------------------------------------------------------
                                VXLAN
--------------------------------------------------------------------------------
* NXOS
    * Updated ShowRunningConfigNvOverlay for more varied output

--------------------------------------------------------------------------------
                                Routing
--------------------------------------------------------------------------------
* IOSXE:
    * Updated ShowIpRouteWord:
        * Updated regex for various formats
        * Added fields to schema
        * Changed fields in schema to Optional
        * Added regex for additional outputs

--------------------------------------------------------------------------------
                                Ethernet
--------------------------------------------------------------------------------
* IOSXR  
    * Added ShowEthernetCfmMeps for:
        * show ethernet cfm peer meps
=======
    * Update ShowIpv6Neighbors
        * Add command 'show ipv6 neighbors {interface}'
>>>>>>> dev
* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                Interface
--------------------------------------------------------------------------------
* IOSXE
    * Update ShowIpv6Neighbors
        * Add command 'show ipv6 neighbors {interface}'

--------------------------------------------------------------------------------
                                Ethernet
--------------------------------------------------------------------------------
* IOSXR  
    * Added ShowEthernetCfmMeps for:
        * show ethernet cfm peer meps