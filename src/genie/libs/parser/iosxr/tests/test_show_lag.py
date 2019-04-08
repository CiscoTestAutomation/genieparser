#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

from genie.libs.parser.iosxr.show_lag import ShowLacpSystemId, ShowBundle, ShowLacp


###################################################
# unit test for show lacp system-id
####################################################
class test_show_lacp_sysid(unittest.TestCase):
    """unit test for show lacp system-id"""

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        RP/0/RP0/CPU0:iosxrv9000-1#show lacp system-id 
        Tue Apr  3 20:33:23.108 UTC

        Priority  MAC Address
        --------  -----------------
          0x0064  00-1b-0c-10-5a-26
    '''}

    golden_parsed_output = {
        "system_priority": 100,
        "system_id_mac": "00-1b-0c-10-5a-26"
    }

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

    golden_output = {'execute.return_value': '''
        RP/0/RP0/CPU0:iosxrv9000-1#show bundle 
        Tue Apr  3 20:30:23.603 UTC

        Bundle-Ether1
          Status:                                    Up
          Local links <active/standby/configured>:   2 / 0 / 2
          Local bandwidth <effective/available>:     2000000 (2000000) kbps
          MAC address (source):                      001b.0c10.5a25 (Chassis pool)
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
          MAC address (source):                      001b.0c10.5a24 (Chassis pool)
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

    golden_parsed_output = {
        "interfaces": {
            "Bundle-Ether1": {
                "bundle_id": 1,
                "status": "up",
                "local_links": {
                    "active": 2,
                    "standby": 0,
                    "configured": 2
                },
                "local_bandwidth": {
                    "effective": 2000000,
                    "available": 2000000
                },
                "mac_address": "001b.0c10.5a25",
                "inter_link": "No",
                "min_active_link": 1,
                "min_active_bw": 1,
                "max_active_link": 8,
                "wait_timer": 2000,
                "load_balance": {
                    "link_order_sgl": "Not configured",
                    "hash_type": "Default",
                    "local_th": "None"
                },
                "lacp": {
                    "lacp": "Operational",
                    "flap_sup_timer": "Off",
                    "cisco_ext": "Disabled",
                    "non_revert": "Disabled"
                },
                "mlacp": "Not configured",
                "ipv4_bfd": "Not configured",
                "ipv6_bfd": "Not configured",
                "port": {
                    "GigabitEthernet0/0/0/0": {
                        "interface": "GigabitEthernet0/0/0/0",
                        "device": "Local",
                        "state": "Active",
                        "port_id": "0x000a, 0x0001",
                        "bw": 1000000
                    },
                    "GigabitEthernet0/0/0/1": {
                        "interface": "GigabitEthernet0/0/0/1",
                        "device": "Local",
                        "state": "Active",
                        "port_id": "0x8000, 0x0002",
                        "bw": 1000000
                    }
                }
            },
            "Bundle-Ether2": {
                "bundle_id": 2,
                "status": "up",
                "local_links": {
                    "active": 2,
                    "standby": 1,
                    "configured": 3
                },
                "local_bandwidth": {
                    "effective": 2000000,
                    "available": 2000000
                },
                "mac_address": "001b.0c10.5a24",
                "inter_link": "No",
                "min_active_link": 2,
                "min_active_bw": 1,
                "max_active_link": 2,
                "wait_timer": 2000,
                "load_balance": {
                    "link_order_sgl": "Not configured",
                    "hash_type": "Default",
                    "local_th": "None"
                },
                "lacp": {
                    "lacp": "Operational",
                    "flap_sup_timer": "Off",
                    "cisco_ext": "Disabled",
                    "non_revert": "Disabled"
                },
                "mlacp": "Not configured",
                "ipv4_bfd": "Not configured",
                "ipv6_bfd": "Not configured",
                "port": {
                    "GigabitEthernet0/0/0/2": {
                        "interface": "GigabitEthernet0/0/0/2",
                        "device": "Local",
                        "state": "Standby",
                        "port_id": "0x8000, 0x0005",
                        "bw": 1000000
                    },
                    "GigabitEthernet0/0/0/3": {
                        "interface": "GigabitEthernet0/0/0/3",
                        "device": "Local",
                        "state": "Active",
                        "port_id": "0x8000, 0x0004",
                        "bw": 1000000
                    },
                    "GigabitEthernet0/0/0/4": {
                        "interface": "GigabitEthernet0/0/0/4",
                        "device": "Local",
                        "state": "Active",
                        "port_id": "0x8000, 0x0003",
                        "bw": 1000000
                    }
                }
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBundle(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowBundle(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


###################################################
# unit test for show lacp
####################################################
class test_show_lacp(unittest.TestCase):
    """unit test for show lacp"""

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
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
          Gi0/0/0/0        30s  ascdA--- 0x000a,0x0001 0x0001 0x0064,00-1b-0c-10-5a-26
           Partner         30s  ascdA--- 0x000a,0x0001 0x0001 0x8000,00-0c-86-5e-68-23
          Gi0/0/0/1        30s  ascdA--- 0x8000,0x0002 0x0001 0x0064,00-1b-0c-10-5a-26
           Partner         30s  ascdA--- 0x8000,0x0005 0x0001 0x8000,00-0c-86-5e-68-23

          Port                  Receive    Period Selection  Mux       A Churn P Churn
          --------------------  ---------- ------ ---------- --------- ------- -------
        Local
          Gi0/0/0/0             Current    Slow   Selected   Distrib   None    None   
          Gi0/0/0/1             Current    Slow   Selected   Distrib   None    None   

        Bundle-Ether2

          Port          (rate)  State    Port ID       Key    System ID
          --------------------  -------- ------------- ------ ------------------------
        Local
          Gi0/0/0/2        30s  a---A--- 0x8000,0x0005 0x0002 0x0064,00-1b-0c-10-5a-26
           Partner         30s  as--A--- 0x8000,0x0004 0x0002 0x8000,00-0c-86-5e-68-23
          Gi0/0/0/3        30s  ascdA--- 0x8000,0x0004 0x0002 0x0064,00-1b-0c-10-5a-26
           Partner         30s  ascdA--- 0x8000,0x0003 0x0002 0x8000,00-0c-86-5e-68-23
          Gi0/0/0/4        30s  ascdA--- 0x8000,0x0003 0x0002 0x0064,00-1b-0c-10-5a-26
           Partner         30s  ascdA--- 0x8000,0x0002 0x0002 0x8000,00-0c-86-5e-68-23

          Port                  Receive    Period Selection  Mux       A Churn P Churn
          --------------------  ---------- ------ ---------- --------- ------- -------
        Local
          Gi0/0/0/2             Current    Slow   Standby    Waiting   Churn   None   
          Gi0/0/0/3             Current    Slow   Selected   Distrib   None    None   
          Gi0/0/0/4             Current    Slow   Selected   Distrib   None    None  
        '''}

    golden_parsed_output = {
        "interfaces": {
            "Bundle-Ether1": {
                "bundle_id": 1,
                "port": {
                    "GigabitEthernet0/0/0/0": {
                        "interface": "GigabitEthernet0/0/0/0",
                        "rate": "30s",
                        "state": "ascdA---",
                        "port_id": "0x000a,0x0001",
                        "key": 1,
                        "system_priority": 100,
                        "system_id": "00-1b-0c-10-5a-26",
                        "partner": {
                            "rate": "30s",
                            "state": "ascdA---",
                            "port_id": "0x000a,0x0001",
                            "key": 1,
                            "system_priority": 32768,
                            "system_id": "00-0c-86-5e-68-23"
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
                        "rate": "30s",
                        "state": "ascdA---",
                        "port_id": "0x8000,0x0002",
                        "key": 1,
                        "system_priority": 100,
                        "system_id": "00-1b-0c-10-5a-26",
                        "partner": {
                            "rate": "30s",
                            "state": "ascdA---",
                            "port_id": "0x8000,0x0005",
                            "key": 1,
                            "system_priority": 32768,
                            "system_id": "00-0c-86-5e-68-23"
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
                "bundle_id": 2,
                "port": {
                    "GigabitEthernet0/0/0/2": {
                        "interface": "GigabitEthernet0/0/0/2",
                        "rate": "30s",
                        "state": "a---A---",
                        "port_id": "0x8000,0x0005",
                        "key": 2,
                        "system_priority": 100,
                        "system_id": "00-1b-0c-10-5a-26",
                        "partner": {
                            "rate": "30s",
                            "state": "as--A---",
                            "port_id": "0x8000,0x0004",
                            "key": 2,
                            "system_priority": 32768,
                            "system_id": "00-0c-86-5e-68-23"
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
                        "rate": "30s",
                        "state": "ascdA---",
                        "port_id": "0x8000,0x0004",
                        "key": 2,
                        "system_priority": 100,
                        "system_id": "00-1b-0c-10-5a-26",
                        "partner": {
                            "rate": "30s",
                            "state": "ascdA---",
                            "port_id": "0x8000,0x0003",
                            "key": 2,
                            "system_priority": 32768,
                            "system_id": "00-0c-86-5e-68-23"
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
                        "rate": "30s",
                        "state": "ascdA---",
                        "port_id": "0x8000,0x0003",
                        "key": 2,
                        "system_priority": 100,
                        "system_id": "00-1b-0c-10-5a-26",
                        "partner": {
                            "rate": "30s",
                            "state": "ascdA---",
                            "port_id": "0x8000,0x0002",
                            "key": 2,
                            "system_priority": 32768,
                            "system_id": "00-0c-86-5e-68-23"
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

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLacp(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLacp(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
