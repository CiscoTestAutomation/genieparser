#!/bin/env python
import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

from genie.libs.parser.iosxr.show_lag import ShowLacpSystemId, ShowBundle, ShowBundleReasons, ShowLacp


###################################################
# unit test for show lacp system-id
####################################################
class test_show_lacp_sysid(unittest.TestCase):
    """unit test for show lacp system-id"""

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "system_priority": 100,
        "system_id_mac": "00-1b-0c-ff-6a-36"
    }

    golden_output = {'execute.return_value': '''
        RP/0/RP0/CPU0:iosxrv9000-1#show lacp system-id 
        Tue Apr  3 20:33:23.108 UTC

        Priority  MAC Address
        --------  -----------------
          0x0064  00-1b-0c-ff-6a-36
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLacpSystemId(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLacpSystemId(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


###################################################
# unit test for show bundle
####################################################
class test_show_bundle(unittest.TestCase):
    """unit test for show bundle"""

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {
        "interfaces": {
            "Bundle-Ether1": {
                "name": "Bundle-Ether1",
                "bundle_id": 1,
                "oper_status": "up",
                "local_links": {
                    "active": 2,
                    "standby": 0,
                    "configured": 2
                },
                "local_bandwidth_kbps": {
                    "effective": 2000000,
                    "available": 2000000
                },
                "mac_address": "001b.0cff.6a35",
                "mac_address_source": "Chassis pool",
                "inter_chassis_link": "No",
                "min_active_link": 1,
                "min_active_bw_kbps": 1,
                "max_active_link": 8,
                "wait_while_timer_ms": 2000,
                "load_balance": {
                    "link_order_signaling": "Not configured",
                    "hash_type": "Default",
                    "locality_threshold": "None"
                },
                "lacp": {
                    "lacp": "Operational",
                    "flap_suppression_timer": "Off",
                    "cisco_extensions": "Disabled",
                    "non_revertive": "Disabled"
                },
                "mlacp": {
                    "mlacp": "Not configured"
                },
                "ipv4_bfd": {
                    "ipv4_bfd": "Not configured"
                },
                "ipv6_bfd": {
                    "ipv6_bfd": "Not configured"
                },
                "port": {
                    "GigabitEthernet0/0/0/0": {
                        "interface": "GigabitEthernet0/0/0/0",
                        "device": "Local",
                        "state": "Active",
                        "port_id": "0x000a, 0x0001",
                        "bw_kbps": 1000000,
                        "link_state": "Link is Active"
                    },
                    "GigabitEthernet0/0/0/1": {
                        "interface": "GigabitEthernet0/0/0/1",
                        "device": "Local",
                        "state": "Active",
                        "port_id": "0x8000, 0x0002",
                        "bw_kbps": 1000000,
                        "link_state": "Link is Active"
                    }
                }
            },
            "Bundle-Ether2": {
                "name": "Bundle-Ether2",
                "bundle_id": 2,
                "oper_status": "up",
                "local_links": {
                    "active": 2,
                    "standby": 1,
                    "configured": 3
                },
                "local_bandwidth_kbps": {
                    "effective": 2000000,
                    "available": 2000000
                },
                "mac_address": "001b.0cff.6a34",
                "mac_address_source": "Chassis pool",
                "inter_chassis_link": "No",
                "min_active_link": 2,
                "min_active_bw_kbps": 1,
                "max_active_link": 2,
                "wait_while_timer_ms": 2000,
                "load_balance": {
                    "link_order_signaling": "Not configured",
                    "hash_type": "Default",
                    "locality_threshold": "None"
                },
                "lacp": {
                    "lacp": "Operational",
                    "flap_suppression_timer": "Off",
                    "cisco_extensions": "Disabled",
                    "non_revertive": "Disabled"
                },
                "mlacp": {
                    "mlacp": "Not configured"
                },
                "ipv4_bfd": {
                    "ipv4_bfd": "Not configured"
                },
                "ipv6_bfd": {
                    "ipv6_bfd": "Not configured"
                },
                "port": {
                    "GigabitEthernet0/0/0/2": {
                        "interface": "GigabitEthernet0/0/0/2",
                        "device": "Local",
                        "state": "Standby",
                        "port_id": "0x8000, 0x0005",
                        "bw_kbps": 1000000,
                        "link_state": "Link is Standby due to maximum-active links configuration"
                    },
                    "GigabitEthernet0/0/0/3": {
                        "interface": "GigabitEthernet0/0/0/3",
                        "device": "Local",
                        "state": "Active",
                        "port_id": "0x8000, 0x0004",
                        "bw_kbps": 1000000,
                        "link_state": "Link is Active"
                    },
                    "GigabitEthernet0/0/0/4": {
                        "interface": "GigabitEthernet0/0/0/4",
                        "device": "Local",
                        "state": "Active",
                        "port_id": "0x8000, 0x0003",
                        "bw_kbps": 1000000,
                        "link_state": "Link is Active"
                    }
                }
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:iosxrv9000-1#show bundle 
        Tue Apr  3 20:30:23.603 UTC

        Bundle-Ether1
          Status:                                    Up
          Local links <active/standby/configured>:   2 / 0 / 2
          Local bandwidth <effective/available>:     2000000 (2000000) kbps
          MAC address (source):                      001b.0cff.6a35 (Chassis pool)
          Inter-chassis link:                        No
          Minimum active links / bandwidth:          1 / 1 kbps
          Maximum active links:                      8
          Wait while timer:                          2000 ms
          Load balancing:                            
            Link order signaling:                    Not configured
            Hash type:                               Default
            Locality threshold:                      None
          LACP:                                      Operational
            Flap suppression timer:                  Off
            Cisco extensions:                        Disabled
            Non-revertive:                           Disabled
          mLACP:                                     Not configured
          IPv4 BFD:                                  Not configured
          IPv6 BFD:                                  Not configured

          Port                  Device           State        Port ID         B/W, kbps
          --------------------  ---------------  -----------  --------------  ----------
          Gi0/0/0/0             Local            Active       0x000a, 0x0001     1000000
              Link is Active
          Gi0/0/0/1             Local            Active       0x8000, 0x0002     1000000
              Link is Active

        Bundle-Ether2
          Status:                                    Up
          Local links <active/standby/configured>:   2 / 1 / 3
          Local bandwidth <effective/available>:     2000000 (2000000) kbps
          MAC address (source):                      001b.0cff.6a34 (Chassis pool)
          Inter-chassis link:                        No
          Minimum active links / bandwidth:          2 / 1 kbps
          Maximum active links:                      2
          Wait while timer:                          2000 ms
          Load balancing:                            
            Link order signaling:                    Not configured
            Hash type:                               Default
            Locality threshold:                      None
          LACP:                                      Operational
            Flap suppression timer:                  Off
            Cisco extensions:                        Disabled
            Non-revertive:                           Disabled
          mLACP:                                     Not configured
          IPv4 BFD:                                  Not configured
          IPv6 BFD:                                  Not configured

          Port                  Device           State        Port ID         B/W, kbps
          --------------------  ---------------  -----------  --------------  ----------
          Gi0/0/0/2             Local            Standby      0x8000, 0x0005     1000000
              Link is Standby due to maximum-active links configuration
          Gi0/0/0/3             Local            Active       0x8000, 0x0004     1000000
              Link is Active
          Gi0/0/0/4             Local            Active       0x8000, 0x0003     1000000
              Link is Active
    '''}

    golden_parsed_output_2 = {
        "interfaces": {
            "Bundle-Ether 2": {
                "name": "Bundle-Ether 2",
                "bundle_id": 2,
                "oper_status": "up",
                "local_links": {
                    "active": 1,
                    "standby": 0,
                    "configured": 1
                },
                "local_bandwidth_kbps": {
                    "effective": 100000,
                    "available": 100000
                },
                "mac_address": "1234.43ff.3232",
                "mac_address_source": "GigabitEthernet0/0/0/1",
                "min_active_link": 1,
                "min_active_bw_kbps": 500,
                "max_active_link": 32,
                "wait_while_timer_ms": 2000,
                "load_balance": {
                    "load_balance": "Default"
                },
                "lacp": {
                    "lacp": "Operational",
                    "flap_suppression_timer": "2500 ms",
                    "cisco_extensions": "Disabled"
                },
                "mlacp": {
                    "mlacp": "Operational",
                    "iccp_group": "3",
                    "foreign_links_active": 1,
                    "foreign_links_configured": 1,
                    "switchover_type": "Revertive",
                    "recovery_delay": "300 s",
                    "maximize_threshold": "2 links"
                },
                "ipv4_bfd": {
                    "ipv4_bfd": "Not operational",
                    "state": "Off",
                    "fast_detect": "Enabled",
                    "start_timer": "Off",
                    "neighbor_unconfigured_timer": "Off",
                    "preferred_min_interval_ms": 150,
                    "preferred_multiple": 3,
                    "destination_address": "Not Configured"
                },
                "port": {
                    "GigabitEthernet0/0/0/1": {
                        "interface": "GigabitEthernet0/0/0/1",
                        "bw_kbps": 100000,
                        "device": "Local",
                        "state": "Active",
                        "port_id": "0x8000, 0x0001"
                    },
                    "MyFirstInterface": {
                        "interface": "MyFirstInterface",
                        "bw_kbps": 100000,
                        "device": "10.10.10.123",
                        "state": "Negotiating",
                        "port_id": "0x8000, 0x0032"
                    }
                }
            },
            "Bundle-Ether 3": {
                "name": "Bundle-Ether 3",
                "bundle_id": 3,
                "oper_status": "up",
                "local_links": {
                    "active": 1,
                    "standby": 0,
                    "configured": 1
                },
                "local_bandwidth_kbps": {
                    "effective": 100000,
                    "available": 100000
                },
                "mac_address": "1234.43ff.4343",
                "mac_address_source": "chassis pool",
                "min_active_link": 1,
                "min_active_bw_kbps": 500,
                "max_active_link": 32,
                "wait_while_timer_ms": 100,
                "load_balance": {
                    "link_order_signaling": "Operational",
                    "hash_type": "Src-IP"
                },
                "lacp": {
                    "lacp": "Operational",
                    "flap_suppression_timer": "120 s",
                    "cisco_extensions": "Enabled"
                },
                "mlacp": {
                    "mlacp": "Not configured"
                },
                "ipv4_bfd": {
                    "ipv4_bfd": "Not operational"
                },
                "port": {
                    "GigabitEthernet0/0/0/2": {
                        "interface": "GigabitEthernet0/0/0/2",
                        "bw_kbps": 100000,
                        "device": "Local",
                        "state": "Active",
                        "port_id": "0x8000, 0x0002"
                    }
                }
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''
        RP/0/RSP0/CPU0:router# show bundle
        Bundle-Ether 2
          Status:                                     Up
          Local links <active/standby/configured>:   1 / 0 / 1
          Local bandwidth <effective/available>:     100000 (100000) kbps
          MAC address (source):                      1234.43ff.3232 (Gi0/0/0/1)
          Minimum active links / bandwidth:          1 / 500 kbps
          Maximum active links:                      32
          Wait-while timer:                          2000 ms
          Load-balancing:                            Default
          LACP:                                      Operational
            Flap suppression timer:                  2500 ms
            Cisco extensions:                        Disabled
          mLACP:                                     Operational
            Interchassis group:                      3
            Foreign links <active/configured>:       1 / 1
            Switchover type:                         Revertive
            Recovery delay:                          300 s
            Maximize threshold:                      2 links
          IPv4 BFD:                                  Not operational
            State:                                   Off
            Fast detect:                             Enabled
            Start timer:                             Off
            Neighbor-unconfigured timer:             Off
            Preferred min interval:                  150 ms
            Preferred multiple:                      3
            Destination address:                     Not Configured

          Port                  Device          State       Port ID        B/W, kbps
          --------------------  --------------- ----------- -------------- -----------
          Gi0/0/0/1             Local           Active      0x8000, 0x0001      100000
          MyFirstInterface      10.10.10.123    Negotiating 0x8000, 0x0032      100000


        Bundle-Ether 3
          Status:                                    Up 
          Local links <active/standby/configured>:   1 / 0 / 1
          Local bandwidth <effective/available>:     100000 / 100000 kbps
          MAC address (source):                      1234.43ff.4343 (chassis pool)
          Minimum active links / bandwidth:          1 / 500 kbps
          Maximum active links:                      32 (from partner)
          Wait-while timer:                          100 ms
          Load-balancing:
            Link order signaling:                    Operational
            Hash type:                               Src-IP
          LACP:                                      Operational
            Flap suppression timer:                  120 s
            Cisco extensions:                        Enabled
          mLACP:                                     Not configured
          IPv4 BFD:                                  Not operational

          Port                  Device          State       Port ID        B/W, kbps
          --------------------  --------------- ----------- -------------- -----------
          Gi0/0/0/2             Local           Active      0x8000, 0x0002      100000

    '''}

    golden_parsed_output_3 = {
        "interfaces": {
            "Bundle-Ether1": {
                "name": "Bundle-Ether1",
                "bundle_id": 1,
                "oper_status": "up",
                "local_links": {
                    "active": 1,
                    "standby": 0,
                    "configured": 1
                },
                "local_bandwidth_kbps": {
                    "effective": 1000000,
                    "available": 1000000
                },
                "mac_address": "0000.deff.afaf",
                "mac_address_source": "Configured",
                "min_active_link": 1,
                "min_active_bw_kbps": 1,
                "max_active_link": 64,
                "wait_while_timer_ms": 100,
                "lacp": {
                    "lacp": "Operational",
                    "flap_suppression_timer": "300 ms"
                },
                "mlacp": {
                    "mlacp": "Operational",
                    "role": "Active",
                    "foreign_links_active": 0,
                    "foreign_links_configured": 1,
                    "switchover_type": "Non-revertive",
                    "recovery_delay": "300 s",
                    "maximize_threshold": "Not configured"
                },
                "ipv4_bfd": {
                    "ipv4_bfd": "Not configured"
                },
                "port": {
                    "GigabitEthernet0/0/0/0": {
                        "interface": "GigabitEthernet0/0/0/0",
                        "bw_kbps": 1000000,
                        "device": "10.81.3.2",
                        "state": "Standby",
                        "port_id": "0x8002, 0xa001",
                        "link_state": "Link is marked as Standby by mLACP peer"
                    }
                }
            }
        }
    }

    golden_output_3 = {'execute.return_value': '''
        RP/0/RSP0/CPU0:router# show bundle

        Bundle-Ether1
        Status: Up
        Local links <active/standby/configured>: 1 / 0 / 1
        Local bandwidth <effective/available>: 1000000 (1000000) kbps
        MAC address (source): 0000.deff.afaf (Configured)
        Minimum active links / bandwidth: 1 / 1 kbps
        Maximum active links: 64
        Wait while timer: 100 ms
        LACP: Operational
        Flap suppression timer: 300 ms
        mLACP: Operational
        ICCP Group: 1
        Role: Active
        Foreign links <active/configured>: 0 / 1
        Switchover type: Non-revertive
        Recovery delay: 300 s
        Maximize threshold: Not configured
        IPv4 BFD: Not configured
         
        Port Device State Port ID B/W, kbps
        -------------------- --------------- ----------- -------------- ----------
        Gi0/0/0/0 Local Active 0x8001, 0x9001 1000000
        Link is Active
        Gi0/0/0/0 10.81.3.2 Standby 0x8002, 0xa001 1000000
        Link is marked as Standby by mLACP peer
    '''}

    golden_parsed_output_4 = {
        "interfaces": {
            "Bundle-Ether1": {
                "name": "Bundle-Ether1",
                "bundle_id": 1,
                "oper_status": "mlacp hot standby",
                "local_links": {
                    "active": 0,
                    "standby": 1,
                    "configured": 1
                },
                "local_bandwidth_kbps": {
                    "effective": 0,
                    "available": 0
                },
                "mac_address": "0000.deff.afaf",
                "mac_address_source": "Configured",
                "min_active_link": 1,
                "min_active_bw_kbps": 1,
                "max_active_link": 64,
                "wait_while_timer_ms": 100,
                "lacp": {
                    "lacp": "Operational",
                    "flap_suppression_timer": "300 ms"
                },
                "mlacp": {
                    "mlacp": "Operational",
                    "role": "Standby",
                    "foreign_links_active": 1,
                    "foreign_links_configured": 1,
                    "switchover_type": "Non-revertive",
                    "recovery_delay": "300 s",
                    "maximize_threshold": "Not configured"
                },
                "ipv4_bfd": {
                    "ipv4_bfd": "Not configured"
                },
                "port": {
                    "GigabitEthernet0/0/0/0": {
                        "interface": "GigabitEthernet0/0/0/0",
                        "bw_kbps": 1000000,
                        "device": "10.81.3.2",
                        "state": "Active",
                        "port_id": "0x8002, 0xa001",
                        "link_state": "Link is Active"
                    }
                }
            }
        }
    }

    golden_output_4 = {'execute.return_value': '''
        RP/0/0/CPU0:router#show bundle
        Mon Jun 7 06:04:17.778 PDT
         
        Bundle-Ether1
        Status: mLACP hot standby
        Local links <active/standby/configured>: 0 / 1 / 1
        Local bandwidth <effective/available>: 0 (0) kbps
        MAC address (source): 0000.deff.afaf (Configured)
        Minimum active links / bandwidth: 1 / 1 kbps
        Maximum active links: 64
        Wait while timer: 100 ms
        LACP: Operational
        Flap suppression timer: 300 ms
        mLACP: Operational
        ICCP Group: 1
        Role: Standby
        Foreign links <active/configured>: 1 / 1
        Switchover type: Non-revertive
        Recovery delay: 300 s
        Maximize threshold: Not configured
        IPv4 BFD: Not configured
         
        Port Device State Port ID B/W, kbps
        -------------------- --------------- ----------- -------------- ----------
        Gi0/0/0/0 Local Standby 0x8003, 0x9001 1000000
        mLACP peer is active
        Gi0/0/0/0 10.81.3.2 Active 0x8002, 0xa001 1000000
        Link is Active
        RP/0/0/CPU0:router#
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBundle(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowBundle(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowBundle(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowBundle(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

    def test_golden_4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_4)
        obj = ShowBundle(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_4)

###################################################
# unit test for show bundle
####################################################
class test_show_bundle_reasons(unittest.TestCase):

    """unit test for 
    show bundle
    show bundle {interface} reasons
    """
    
    empty_output = {'execute.return_value': ''}
    maxDiff = None 

    golden_parsed_output1 = {
        "interfaces": {
            "Bundle-Ether12": {
                "name": "Bundle-Ether12",
                "bundle_id": 12,
                "oper_status": "up",
                "local_links": {
                    "active": 2,
                    "standby": 0,
                    "configured": 2
                },
                "local_bandwidth_kbps": {
                    "effective": 2000000,
                    "available": 2000000
                },
                "mac_address": "0006.c1ff.5574",
                "mac_address_source": "Chassis pool",
                "inter_chassis_link": "No",
                "min_active_link": 1,
                "min_active_bw_kbps": 1,
                "max_active_link": 24,
                "wait_while_timer_ms": 2000,
                "load_balance": {
                    "link_order_signaling": "Not configured",
                    "hash_type": "Default",
                    "locality_threshold": "None"
                },
                "lacp": {
                    "lacp": "Operational",
                    "flap_suppression_timer": "Off",
                    "cisco_extensions": "Disabled",
                    "non_revertive": "Disabled"
                },
                "mlacp": {
                    "mlacp": "Not configured"
                },
                "ipv4_bfd": {
                    "ipv4_bfd": "Not configured"
                },
                "ipv6_bfd": {
                    "ipv6_bfd": "Not configured"
                },
                "port": {
                    "GigabitEthernet0/0/0/2": {
                        "interface": "GigabitEthernet0/0/0/2",
                        "device": "Local",
                        "state": "Active",
                        "port_id": "0x8000, 0x0002",
                        "bw_kbps": 1000000,
                        "link_state": "Link is Active"
                    },
                    "GigabitEthernet0/0/0/3": {
                        "interface": "GigabitEthernet0/0/0/3",
                        "device": "Local",
                        "state": "Active",
                        "port_id": "0x8000, 0x0001",
                        "bw_kbps": 1000000,
                        "link_state": "Link is Active"
                    }
                }
            },
            "Bundle-Ether23": {
                "name": "Bundle-Ether23",
                "bundle_id": 23,
                "oper_status": "up",
                "local_links": {
                    "active": 1,
                    "standby": 0,
                    "configured": 2
                },
                "local_bandwidth_kbps": {
                    "effective": 1000000,
                    "available": 1000000
                },
                "mac_address": "0006.c1ff.5573",
                "mac_address_source": "Chassis pool",
                "inter_chassis_link": "No",
                "min_active_link": 1,
                "min_active_bw_kbps": 1,
                "max_active_link": 24,
                "wait_while_timer_ms": 2000,
                "load_balance": {
                    "link_order_signaling": "Not configured",
                    "hash_type": "Default",
                    "locality_threshold": "None"
                },
                "lacp": {
                    "lacp": "Operational",
                    "flap_suppression_timer": "Off",
                    "cisco_extensions": "Disabled",
                    "non_revertive": "Disabled"
                },
                "mlacp": {
                    "mlacp": "Not configured"
                },
                "ipv4_bfd": {
                    "ipv4_bfd": "Not configured"
                },
                "ipv6_bfd": {
                    "ipv6_bfd": "Not configured"
                },
                "port": {
                    "GigabitEthernet0/0/0/4": {
                        "interface": "GigabitEthernet0/0/0/4",
                        "device": "Local",
                        "state": "Configured",
                        "port_id": "0x8000, 0x0004",
                        "bw_kbps": 1000000,
                        "link_state": "Partner System ID/Key do not match that of the Selected links"
                    },
                    "GigabitEthernet0/0/0/5": {
                        "interface": "GigabitEthernet0/0/0/5",
                        "device": "Local",
                        "state": "Active",
                        "port_id": "0x8000, 0x0003",
                        "bw_kbps": 1000000,
                        "link_state": "Link is Active"
                    }
                }
            }
        }
    }

    golden_output1 = {'execute.return_value': ''' 
    RP/0/RP0/CPU0:R2_xr#show bundle reasons
    Thu Jan  2 20:40:07.953 UTC

    Bundle-Ether12
      Status:                                    Up
      Local links <active/standby/configured>:   2 / 0 / 2
      Local bandwidth <effective/available>:     2000000 (2000000) kbps
      MAC address (source):                      0006.c1ff.5574 (Chassis pool)
      Inter-chassis link:                        No
      Minimum active links / bandwidth:          1 / 1 kbps
      Maximum active links:                      24
      Wait while timer:                          2000 ms
      Load balancing:                            
        Link order signaling:                    Not configured
        Hash type:                               Default
        Locality threshold:                      None
      LACP:                                      Operational
        Flap suppression timer:                  Off
        Cisco extensions:                        Disabled
        Non-revertive:                           Disabled
      mLACP:                                     Not configured
      IPv4 BFD:                                  Not configured
      IPv6 BFD:                                  Not configured

      Port                  Device           State        Port ID         B/W, kbps
      --------------------  ---------------  -----------  --------------  ----------
      Gi0/0/0/2             Local            Active       0x8000, 0x0002     1000000
          Link is Active
      Gi0/0/0/3             Local            Active       0x8000, 0x0001     1000000
          Link is Active

    Bundle-Ether23
      Status:                                    Up
      Local links <active/standby/configured>:   1 / 0 / 2
      Local bandwidth <effective/available>:     1000000 (1000000) kbps
      MAC address (source):                      0006.c1ff.5573 (Chassis pool)
      Inter-chassis link:                        No
      Minimum active links / bandwidth:          1 / 1 kbps
      Maximum active links:                      24
      Wait while timer:                          2000 ms
      Load balancing:                            
        Link order signaling:                    Not configured
        Hash type:                               Default
        Locality threshold:                      None
      LACP:                                      Operational
        Flap suppression timer:                  Off
        Cisco extensions:                        Disabled
        Non-revertive:                           Disabled
      mLACP:                                     Not configured
      IPv4 BFD:                                  Not configured
      IPv6 BFD:                                  Not configured

      Port                  Device           State        Port ID         B/W, kbps
      --------------------  ---------------  -----------  --------------  ----------
      Gi0/0/0/4             Local            Configured   0x8000, 0x0004     1000000
          Partner System ID/Key do not match that of the Selected links
      Gi0/0/0/5             Local            Active       0x8000, 0x0003     1000000
          Link is Active
    '''
    }

    golden_parsed_output2 = {
        "interfaces": {
            "Bundle-Ether23": {
                "name": "Bundle-Ether23",
                "bundle_id": 23,
                "oper_status": "down",
                "local_links": {
                    "active": 0,
                    "standby": 0,
                    "configured": 0
                },
                "local_bandwidth_kbps": {
                    "effective": 0,
                    "available": 0
                },
                "mac_address": "000e.83ff.4444",
                "mac_address_source": "Chassis pool",
                "inter_chassis_link": "No",
                "min_active_link": 1,
                "min_active_bw_kbps": 1,
                "max_active_link": 24,
                "wait_while_timer_ms": 2000,
                "load_balance": {
                    "link_order_signaling": "Not configured",
                    "hash_type": "Default",
                    "locality_threshold": "None"
                },
                "lacp": {
                    "lacp": "Not operational",
                    "flap_suppression_timer": "Off",
                    "cisco_extensions": "Disabled",
                    "non_revertive": "Disabled"
                },
                "mlacp": {
                    "mlacp": "Not configured"
                },
                "ipv4_bfd": {
                    "ipv4_bfd": "Not configured"
                },
                "ipv6_bfd": {
                    "ipv6_bfd": "Not configured"
                },
            },
        }
    }


    golden_output2 = {'execute.return_value': '''
    [2020-01-09 18:43:58,295] +++ R2_xr: executing command 'show bundle Bundle-Ether23 reasons' +++
    show bundle Bundle-Ether23 reasons
    Thu Jan  9 23:43:50.462 UTC
    
    Bundle-Ether23
      Status:                                    Down
      Local links <active/standby/configured>:   0 / 0 / 0
      Local bandwidth <effective/available>:     0 (0) kbps
      MAC address (source):                      000e.83ff.4444 (Chassis pool)
      Inter-chassis link:                        No
      Minimum active links / bandwidth:          1 / 1 kbps
      Maximum active links:                      24
      Wait while timer:                          2000 ms
      Load balancing:
        Link order signaling:                    Not configured
        Hash type:                               Default
        Locality threshold:                      None
      LACP:                                      Not operational
        Flap suppression timer:                  Off
        Cisco extensions:                        Disabled
        Non-revertive:                           Disabled
      mLACP:                                     Not configured
      IPv4 BFD:                                  Not configured
      IPv6 BFD:                                  Not configured
    
     '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBundle(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowBundle(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)
    
    def test_golden_2(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowBundle(device=self.device)
        parsed_output = obj.parse(interface="Bundle-Ether23")
        self.assertEqual(parsed_output, self.golden_parsed_output2)



###################################################
# unit test for show lacp
####################################################
class test_show_lacp(unittest.TestCase):
    """unit test for 
    show lacp
    show lacp {interface}
    """
    
    empty_output = {'execute.return_value': ''}
    maxDiff = None 

    golden_parsed_output1 = {
        "interfaces": {
            "Bundle-Ether1": {
                "name": "Bundle-Ether1",
                "bundle_id": 1,
                "lacp_mode": "active",
                "port": {
                    "GigabitEthernet0/0/0/0": {
                        "interface": "GigabitEthernet0/0/0/0",
                        "bundle_id": 1,
                        "rate": 30,
                        "state": "ascdA---",
                        "port_id": "0x000a,0x0001",
                        "key": "0x0001",
                        "system_id": "0x0064,00-1b-0c-ff-6a-36",
                        "aggregatable": True,
                        "synchronization": "in_sync",
                        "collecting": True,
                        "distributing": True,
                        "partner": {
                            "rate": 30,
                            "state": "ascdA---",
                            "port_id": "0x000a,0x0001",
                            "key": "0x0001",
                            "system_id": "0x8000,00-0c-86-ff-c6-81",
                            "aggregatable": True,
                            "synchronization": "in_sync",
                            "collecting": True,
                            "distributing": True
                        },
                        "receive": "Current",
                        "period": "Slow",
                        "selection": "Selected",
                        "mux": "Distrib",
                        "a_churn": "None",
                        "p_churn": "None"
                    },
                    "GigabitEthernet0/0/0/1": {
                        "interface": "GigabitEthernet0/0/0/1",
                        "bundle_id": 1,
                        "rate": 30,
                        "state": "ascdA---",
                        "port_id": "0x8000,0x0002",
                        "key": "0x0001",
                        "system_id": "0x0064,00-1b-0c-ff-6a-36",
                        "aggregatable": True,
                        "synchronization": "in_sync",
                        "collecting": True,
                        "distributing": True,
                        "partner": {
                            "rate": 30,
                            "state": "ascdA---",
                            "port_id": "0x8000,0x0005",
                            "key": "0x0001",
                            "system_id": "0x8000,00-0c-86-ff-c6-81",
                            "aggregatable": True,
                            "synchronization": "in_sync",
                            "collecting": True,
                            "distributing": True
                        },
                        "receive": "Current",
                        "period": "Slow",
                        "selection": "Selected",
                        "mux": "Distrib",
                        "a_churn": "None",
                        "p_churn": "None"
                    }
                }
            },
            "Bundle-Ether2": {
                "name": "Bundle-Ether2",
                "bundle_id": 2,
                "lacp_mode": "active",
                "port": {
                    "GigabitEthernet0/0/0/2": {
                        "interface": "GigabitEthernet0/0/0/2",
                        "bundle_id": 2,
                        "rate": 30,
                        "state": "a---A---",
                        "port_id": "0x8000,0x0005",
                        "key": "0x0002",
                        "system_id": "0x0064,00-1b-0c-ff-6a-36",
                        "aggregatable": True,
                        "synchronization": "out_sync",
                        "collecting": False,
                        "distributing": False,
                        "partner": {
                            "rate": 30,
                            "state": "as--A---",
                            "port_id": "0x8000,0x0004",
                            "key": "0x0002",
                            "system_id": "0x8000,00-0c-86-ff-c6-81",
                            "aggregatable": True,
                            "synchronization": "in_sync",
                            "collecting": False,
                            "distributing": False
                        },
                        "receive": "Current",
                        "period": "Slow",
                        "selection": "Standby",
                        "mux": "Waiting",
                        "a_churn": "Churn",
                        "p_churn": "None"
                    },
                    "GigabitEthernet0/0/0/3": {
                        "interface": "GigabitEthernet0/0/0/3",
                        "bundle_id": 2,
                        "rate": 30,
                        "state": "ascdA---",
                        "port_id": "0x8000,0x0004",
                        "key": "0x0002",
                        "system_id": "0x0064,00-1b-0c-ff-6a-36",
                        "aggregatable": True,
                        "synchronization": "in_sync",
                        "collecting": True,
                        "distributing": True,
                        "partner": {
                            "rate": 30,
                            "state": "ascdA---",
                            "port_id": "0x8000,0x0003",
                            "key": "0x0002",
                            "system_id": "0x8000,00-0c-86-ff-c6-81",
                            "aggregatable": True,
                            "synchronization": "in_sync",
                            "collecting": True,
                            "distributing": True
                        },
                        "receive": "Current",
                        "period": "Slow",
                        "selection": "Selected",
                        "mux": "Distrib",
                        "a_churn": "None",
                        "p_churn": "None"
                    },
                    "GigabitEthernet0/0/0/4": {
                        "interface": "GigabitEthernet0/0/0/4",
                        "bundle_id": 2,
                        "rate": 30,
                        "state": "ascdA---",
                        "port_id": "0x8000,0x0003",
                        "key": "0x0002",
                        "system_id": "0x0064,00-1b-0c-ff-6a-36",
                        "aggregatable": True,
                        "synchronization": "in_sync",
                        "collecting": True,
                        "distributing": True,
                        "partner": {
                            "rate": 30,
                            "state": "ascdA---",
                            "port_id": "0x8000,0x0002",
                            "key": "0x0002",
                            "system_id": "0x8000,00-0c-86-ff-c6-81",
                            "aggregatable": True,
                            "synchronization": "in_sync",
                            "collecting": True,
                            "distributing": True
                        },
                        "receive": "Current",
                        "period": "Slow",
                        "selection": "Selected",
                        "mux": "Distrib",
                        "a_churn": "None",
                        "p_churn": "None"
                    }
                }
            }
        }
    }

    golden_output1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:iosxrv9000-1#show lacp
        Tue Apr  3 20:32:49.966 UTC
        State: a - Port is marked as Aggregatable.
               s - Port is Synchronized with peer.
               c - Port is marked as Collecting.
               d - Port is marked as Distributing.
               A - Device is in Active mode.
               F - Device requests PDUs from the peer at fast rate.
               D - Port is using default values for partner information.
               E - Information about partner has expired.

        Bundle-Ether1

          Port          (rate)  State    Port ID       Key    System ID
          --------------------  -------- ------------- ------ ------------------------
        Local
          Gi0/0/0/0        30s  ascdA--- 0x000a,0x0001 0x0001 0x0064,00-1b-0c-ff-6a-36
           Partner         30s  ascdA--- 0x000a,0x0001 0x0001 0x8000,00-0c-86-ff-c6-81
          Gi0/0/0/1        30s  ascdA--- 0x8000,0x0002 0x0001 0x0064,00-1b-0c-ff-6a-36
           Partner         30s  ascdA--- 0x8000,0x0005 0x0001 0x8000,00-0c-86-ff-c6-81

          Port                  Receive    Period Selection  Mux       A Churn P Churn
          --------------------  ---------- ------ ---------- --------- ------- -------
        Local
          Gi0/0/0/0             Current    Slow   Selected   Distrib   None    None   
          Gi0/0/0/1             Current    Slow   Selected   Distrib   None    None   

        Bundle-Ether2

          Port          (rate)  State    Port ID       Key    System ID
          --------------------  -------- ------------- ------ ------------------------
        Local
          Gi0/0/0/2        30s  a---A--- 0x8000,0x0005 0x0002 0x0064,00-1b-0c-ff-6a-36
           Partner         30s  as--A--- 0x8000,0x0004 0x0002 0x8000,00-0c-86-ff-c6-81
          Gi0/0/0/3        30s  ascdA--- 0x8000,0x0004 0x0002 0x0064,00-1b-0c-ff-6a-36
           Partner         30s  ascdA--- 0x8000,0x0003 0x0002 0x8000,00-0c-86-ff-c6-81
          Gi0/0/0/4        30s  ascdA--- 0x8000,0x0003 0x0002 0x0064,00-1b-0c-ff-6a-36
           Partner         30s  ascdA--- 0x8000,0x0002 0x0002 0x8000,00-0c-86-ff-c6-81

          Port                  Receive    Period Selection  Mux       A Churn P Churn
          --------------------  ---------- ------ ---------- --------- ------- -------
        Local
          Gi0/0/0/2             Current    Slow   Standby    Waiting   Churn   None   
          Gi0/0/0/3             Current    Slow   Selected   Distrib   None    None   
          Gi0/0/0/4             Current    Slow   Selected   Distrib   None    None  
        '''}

    golden_parsed_output2 =  {
        "interfaces": {
            "Bundle-Ether8": {
                "name": "Bundle-Ether8",
                "bundle_id": 8,
                "lacp_mode": "active",
                "port": {
                    "TenGigabitEthernet0/0/0/0": {
                        "interface": "TenGigabitEthernet0/0/0/0",
                        "bundle_id": 8,
                        "rate": 1,
                        "state": "ascdAF--",
                        "port_id": "0x8000,0x0002",
                        "key": "0x0008",
                        "system_id": "0x8000,40-55-39-ff-6c-0f",
                        "aggregatable": True,
                        "synchronization": "in_sync",
                        "collecting": True,
                        "distributing": True,
                        "partner": {
                            "rate": 1,
                            "state": "ascdAF--",
                            "port_id": "0x0001,0x0006",
                            "key": "0x0008",
                            "system_id": "0x0001,cc-ef-48-ff-23-0a",
                            "aggregatable": True,
                            "synchronization": "in_sync",
                            "collecting": True,
                            "distributing": True
                        },
                        "receive": "Current",
                        "period": "Fast",
                        "selection": "Selected",
                        "mux": "Distrib",
                        "a_churn": "None",
                        "p_churn": "None"
                    },
                    "TenGigabitEthernet0/1/0/0": {
                        "interface": "TenGigabitEthernet0/1/0/0",
                        "bundle_id": 8,
                        "rate": 1,
                        "state": "ascdAF--",
                        "port_id": "0x8000,0x0001",
                        "key": "0x0008",
                        "system_id": "0x8000,40-55-39-ff-6c-0f",
                        "aggregatable": True,
                        "synchronization": "in_sync",
                        "collecting": True,
                        "distributing": True,
                        "partner": {
                            "rate": 1,
                            "state": "ascdAF--",
                            "port_id": "0x8000,0x0004",
                            "key": "0x0008",
                            "system_id": "0x0001,cc-ef-48-ff-23-0a",
                            "aggregatable": True,
                            "synchronization": "in_sync",
                            "collecting": True,
                            "distributing": True
                        },
                        "receive": "Current",
                        "period": "Fast",
                        "selection": "Selected",
                        "mux": "Distrib",
                        "a_churn": "None",
                        "p_churn": "None"
                    },
                },
            },
        },
    }

    golden_output2 = {'execute.return_value': '''
        RP/0/RP0/CPU0:iosxrv9000-1#show lacp Bundle-Ether8
        Tue Apr  3 20:32:49.966 UTC
        State: a - Port is marked as Aggregatable.
               s - Port is Synchronized with peer.
               c - Port is marked as Collecting.
               d - Port is marked as Distributing.
               A - Device is in Active mode.
               F - Device requests PDUs from the peer at fast rate.
               D - Port is using default values for partner information.
               E - Information about partner has expired.

        Bundle-Ether8

          Port          (rate)  State    Port ID       Key    System ID
          --------------------  -------- ------------- ------ ------------------------
        Local
          Te0/0/0/0         1s  ascdAF-- 0x8000,0x0002 0x0008 0x8000,40-55-39-ff-6c-0f
           Partner          1s  ascdAF-- 0x0001,0x0006 0x0008 0x0001,cc-ef-48-ff-23-0a
          Te0/1/0/0         1s  ascdAF-- 0x8000,0x0001 0x0008 0x8000,40-55-39-ff-6c-0f
           Partner          1s  ascdAF-- 0x8000,0x0004 0x0008 0x0001,cc-ef-48-ff-23-0a

          Port                  Receive    Period Selection  Mux       A Churn P Churn
          --------------------  ---------- ------ ---------- --------- ------- -------
        Local
          Te0/0/0/0             Current    Fast   Selected   Distrib   None    None   
          Te0/1/0/0             Current    Fast   Selected   Distrib   None    None   

        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLacp(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowLacp(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_golden2(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowLacp(device=self.device)
        parsed_output = obj.parse(interface='Bundle-Ether8')
        self.assertEqual(parsed_output, self.golden_parsed_output2)


if __name__ == '__main__':
    unittest.main()
