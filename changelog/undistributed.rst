* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                MPLS
--------------------------------------------------------------------------------
* IOSXE
    * Update ShowMplsForwardingTable
        * Add command 'show mpls forwarding-table {prefix}'

--------------------------------------------------------------------------------
                                Segment Routing
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowSegmentRoutingMplsConnectedPrefixSidMapLocal for:
        'show segment-routing mpls connected-prefix-sid-map local ipv4'
        'show segment-routing mpls connected-prefix-sid-map local ipv6'

--------------------------------------------------------------------------------
                                BGP
--------------------------------------------------------------------------------
* IOSXR
    * Updated ShowBgpL2vpnEvpn for:
        added a schema and unittest, and updated based on the schema
