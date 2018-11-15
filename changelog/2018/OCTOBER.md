
| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 3.1.0         |
| ``genie.libs.parser``   | 3.1.1         |
| ``genie.libs.parser``   | 3.1.2         |


# V3.1.0
--------------------------------------------------------------------------------
                                LISP
--------------------------------------------------------------------------------

* IOSXE
    * show lisp session
    * show lisp platform
    * show lisp all extranet 'extranet' instance-id 'instance_id'
    * show lisp all instance-id 'instance_id' dynamic-eid detail
    * show lisp all service ipv4
    * show lisp all service ipv6
    * show lisp all service ethernet
    * show lisp all instance-id 'instance_id' ipv4
    * show lisp all instance-id 'instance_id' ipv6
    * show lisp all instance-id 'instance_id' ethernet
    * show lisp all instance-id 'instance_id' ipv4 map-cache
    * show lisp all instance-id 'instance_id' ipv6 map-cache
    * show lisp all instance-id 'instance_id' ethernet map-cache
    * show lisp all instance-id 'instance_id' ipv4 server rloc members
    * show lisp all instance-id 'instance_id' ipv6 server rloc members
    * show lisp all instance-id 'instance_id' ethernet server rloc members
    * show lisp all instance-id 'instance_id' ipv4 smr
    * show lisp all instance-id 'instance_id' ipv6 smr
    * show lisp all instance-id 'instance_id' ethernet smr
    * show lisp all service ipv4 summary
    * show lisp all service ipv6 summary
    * show lisp all service ethernet summary
    * show lisp all instance-id 'instance_id' ipv4 database
    * show lisp all instance-id 'instance_id' ipv6 database
    * show lisp all instance-id 'instance_id' ethernet database
    * show lisp all instance-id 'instance_id' ipv4 server summary
    * show lisp all instance-id 'instance_id' ipv6 server summary
    * show lisp all instance-id 'instance_id' ethernet server summary
    * show lisp all instance-id 'instance_id' ipv4 server detail internal
    * show lisp all instance-id 'instance_id' ipv6 server detail internal
    * show lisp all instance-id 'instance_id' ethernet server detail internal
    * show lisp all instance-id 'instance_id' ipv4 statistics
    * show lisp all instance-id 'instance_id' ipv6 statistics
    * show lisp all instance-id 'instance_id' ethernet statistics

--------------------------------------------------------------------------------
                                PIM
--------------------------------------------------------------------------------

* NXOS:
    * show running-config pim '| sec vrf | inc "pip string"'

--------------------------------------------------------------------------------
                                MSDP
--------------------------------------------------------------------------------

* NXOS
    * show ip msdp peer vrf 'vrf'
    * show ip msdp sa-cache detail vrf 'vrf'
    * show ip msdp policy statistics sa-policy 'address' in 'vrf "vrf"'
    * show ip msdp policy statistics sa-policy 'address' out 'vrf "vrf"'
    * show ip msdp summary
    * show ip msdp summary vrf all
    * show ip msdp summary vrf 'vrf'
    * show running-config msdp '| sec vrf | inc "pip string"'

--------------------------------------------------------------------------------
                                TRM
--------------------------------------------------------------------------------

* NXOS
    - ShowFabricMulticastGlobals
    - ShowFabricMulticastIpSaAdRoute
    - ShowFabricMulticastIpL2Mroute
    - ShowForwardingDistributionMulticastRoute
    - ShowBgpIpMvpnRouteType
    - ShowBgpIpMvpnSaadDetail
    - ShowBgpL2vpnEvpn
    - ShowBgpIpMvpn

--------------------------------------------------------------------------------
                                BGP
--------------------------------------------------------------------------------

* Fixed the following parsers for BGP (NXOS):
    - ShowBgpVrfAllAllNextHopDatabase

# V3.1.1
--------------------------------------------------------------------------------
                                OSPF
--------------------------------------------------------------------------------

* Fixed the following parsers for OSPF (NXOS):
    - ShowIpOspfMplsLdpInterface

--------------------------------------------------------------------------------
                                PLATFORM
--------------------------------------------------------------------------------

* Fixed the following parsers for PLATFORM (IOSXR):
    - ShowInventory


--------------------------------------------------------------------------------
                                ROUTING
--------------------------------------------------------------------------------

* NXOS
    * parser fix for 'show ip|ipv6 route vrf all' on output
      '*via 172.16.0.1, Eth1/1, [110/81], 3w6d, ospf-Underlay, intra' which ospf is not a number


# V3.1.2

* Enhanced CES Monitor