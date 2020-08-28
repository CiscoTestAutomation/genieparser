# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# junos show_ospf
from genie.libs.parser.junos.show_ospf import (
    ShowOspfInterface,
    ShowOspfInterfaceBrief,
    ShowOspfInterfaceDetail,
    ShowOspfNeighbor,
    ShowOspfDatabase,
    ShowOspfDatabaseOpaqueArea,
    ShowOspfDatabaseSummary,
    ShowOspfDatabaseExternalExtensive,
    ShowOspfOverview,
    ShowOspfOverviewExtensive,
    ShowOspfDatabaseAdvertisingRouterSelfDetail,
    ShowOspfDatabaseExtensive,
    ShowOspfNeighborExtensive,
    ShowOspfInterfaceExtensive,
    ShowOspfNeighborDetail,
    ShowOspfDatabaseNetworkLsaidDetail,
    ShowOspfDatabaseLsaidDetail,
    ShowOspfRouteBrief,
    ShowOspfRouteDetail,
    ShowOspfRouteNetworkExtensive,
    ShowOspfDatabaseAdvertisingRouterExtensive,
)

class TestShowOspfDatabaseOpaqueArea(unittest.TestCase):
    """ Unit tests for:
            * show ospf database opaque-area
    """
    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}
    
    maxDiff = None

    golden_output = {
        "execute.return_value": """
            show ospf database opaque-area
            OSPF database, Area 0.0.0.8
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
        OpaqArea 10.1.0.1          10.49.194.125    0x80000002   359  0x22 0x6f5d  28
        OpaqArea 10.1.0.1          10.49.194.127    0x80000002   595  0x22 0x7751  28
        OpaqArea*10.1.0.1          10.34.2.250     0x80000003   227  0x22 0xa11a  28
        OpaqArea 10.1.0.1          10.34.3.252     0x80000002   754  0x22 0xad09  28
        OpaqArea 10.1.0.1          10.169.14.240   0x80000002  2210  0x22 0x35ae  28
        OpaqArea 10.1.0.3          10.49.194.125    0x80000001  1168  0x22 0x27f4 136
        OpaqArea 10.1.0.3          10.49.194.127    0x80000001  1441  0x22 0xa27  136
        OpaqArea*10.1.0.3          10.34.2.250     0x80000002   934  0x22 0x2ac3 136
        OpaqArea 10.1.0.3          10.34.3.252     0x80000001  1815  0x22 0x90dd 136
        OpaqArea 10.1.0.3          10.169.14.240   0x80000002   597  0x22 0x5697 136
        OpaqArea*10.1.0.4          10.34.2.250     0x80000001  1814  0x22 0xb7b3 136
        OpaqArea 10.1.0.4          10.34.3.252     0x80000001  1167  0x22 0x412  136
        OpaqArea 10.1.0.4          10.169.14.240   0x80000001  1440  0x22 0x58d5 136
        """
    }
    
    golden_parsed_output = {
        "ospf-database-information": {
            "ospf-area-header": {
                "ospf-area": "0.0.0.8"
            },
            "ospf-database": [
                {
                    "advertising-router": "10.49.194.125",
                    "age": "359",
                    "checksum": "0x6f5d",
                    "lsa-id": "10.1.0.1",
                    "lsa-length": "28",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80000002"
                },
                {
                    "advertising-router": "10.49.194.127",
                    "age": "595",
                    "checksum": "0x7751",
                    "lsa-id": "10.1.0.1",
                    "lsa-length": "28",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80000002"
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "227",
                    "checksum": "0xa11a",
                    "lsa-id": "10.1.0.1",
                    "lsa-length": "28",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "our-entry": True,
                    "sequence-number": "0x80000003"
                },
                {
                    "advertising-router": "10.34.3.252",
                    "age": "754",
                    "checksum": "0xad09",
                    "lsa-id": "10.1.0.1",
                    "lsa-length": "28",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80000002"
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "2210",
                    "checksum": "0x35ae",
                    "lsa-id": "10.1.0.1",
                    "lsa-length": "28",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80000002"
                },
                {
                    "advertising-router": "10.49.194.125",
                    "age": "1168",
                    "checksum": "0x27f4",
                    "lsa-id": "10.1.0.3",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80000001"
                },
                {
                    "advertising-router": "10.49.194.127",
                    "age": "1441",
                    "checksum": "0xa27",
                    "lsa-id": "10.1.0.3",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80000001"
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "934",
                    "checksum": "0x2ac3",
                    "lsa-id": "10.1.0.3",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "our-entry": True,
                    "sequence-number": "0x80000002"
                },
                {
                    "advertising-router": "10.34.3.252",
                    "age": "1815",
                    "checksum": "0x90dd",
                    "lsa-id": "10.1.0.3",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80000001"
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "597",
                    "checksum": "0x5697",
                    "lsa-id": "10.1.0.3",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80000002"
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "1814",
                    "checksum": "0xb7b3",
                    "lsa-id": "10.1.0.4",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "our-entry": True,
                    "sequence-number": "0x80000001"
                },
                {
                    "advertising-router": "10.34.3.252",
                    "age": "1167",
                    "checksum": "0x412",
                    "lsa-id": "10.1.0.4",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80000001"
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "1440",
                    "checksum": "0x58d5",
                    "lsa-id": "10.1.0.4",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80000001"
                }
            ]
        }
    }

    def test_show_ospf_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspfDatabaseOpaqueArea(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()
    
    def test_show_ospf_database_opaque_area(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspfDatabaseOpaqueArea(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)
    
class test_show_ospf_interface(unittest.TestCase):
    """ Unit tests for:
            * show ospf interface
            * show ospf interface {interface}
    """

    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
    show ospf interface
    Interface           State   Area            DR ID           BDR ID          Nbrs
    ge-0/0/0.0          PtToPt  0.0.0.1         0.0.0.0         0.0.0.0            1
    ge-0/0/1.0          PtToPt  0.0.0.1         0.0.0.0         0.0.0.0            1
    """
    }

    golden_parsed_output = {
        "instance": {
            "master": {
                "areas": {
                    "0.0.0.1": {
                        "interfaces": {
                            "ge-0/0/0.0": {
                                "state": "PtToPt",
                                "dr_id": "0.0.0.0",
                                "bdr_id": "0.0.0.0",
                                "nbrs_count": 1,
                            },
                            "ge-0/0/1.0": {
                                "state": "PtToPt",
                                "dr_id": "0.0.0.0",
                                "bdr_id": "0.0.0.0",
                                "nbrs_count": 1,
                            },
                        }
                    }
                }
            }
        }
    }

    golden_output_interface = {
        "execute.return_value": """
        show ospf interface ge-0/0/1.0
        Interface           State   Area            DR ID           BDR ID          Nbrs
        ge-0/0/1.0          PtToPt  0.0.0.1         0.0.0.0         0.0.0.0            1
        """
    }

    golden_parsed_output_interface = {
        "instance": {
            "master": {
                "areas": {
                    "0.0.0.1": {
                        "interfaces": {
                            "ge-0/0/1.0": {
                                "state": "PtToPt",
                                "dr_id": "0.0.0.0",
                                "bdr_id": "0.0.0.0",
                                "nbrs_count": 1,
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_instance = {
        "execute.return_value": """
        show ospf interface instance master
        Interface           State   Area            DR ID           BDR ID          Nbrs
        ge-0/0/0.0          PtToPt  0.0.0.1         0.0.0.0         0.0.0.0            1
        ge-0/0/1.0          PtToPt  0.0.0.1         0.0.0.0         0.0.0.0            1
        """
    }

    golden_parsed_output_instance = {
        "instance": {
            "master": {
                "areas": {
                    "0.0.0.1": {
                        "interfaces": {
                            "ge-0/0/0.0": {
                                "state": "PtToPt",
                                "dr_id": "0.0.0.0",
                                "bdr_id": "0.0.0.0",
                                "nbrs_count": 1,
                            },
                            "ge-0/0/1.0": {
                                "state": "PtToPt",
                                "dr_id": "0.0.0.0",
                                "bdr_id": "0.0.0.0",
                                "nbrs_count": 1,
                            },
                        }
                    }
                }
            }
        }
    }

    def test_show_ospf_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspfInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_show_ospf_interface(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspfInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_ospf_interface_interface(self):
        self.device = Mock(**self.golden_output_interface)
        obj = ShowOspfInterface(device=self.device)
        parsed_output = obj.parse(interface="ge-0/0/1.0")
        self.assertEqual(parsed_output, self.golden_parsed_output_interface)

    def test_show_ospf_interface_instance(self):
        self.device = Mock(**self.golden_output_instance)
        obj = ShowOspfInterface(device=self.device)
        parsed_output = obj.parse(instance="master")
        self.assertEqual(parsed_output, self.golden_parsed_output_instance)


class test_show_ospf_interface_brief(unittest.TestCase):
    """ Unit tests for:
            * show ospf interface brief
            * show ospf interface brief instance {instance}
            * show ospf interface {interface} brief
    """

    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
    show ospf interface brief
    Interface           State   Area            DR ID           BDR ID          Nbrs
    ge-0/0/2.0          BDR     0.0.0.1         10.16.2.2         10.64.4.4            5
    """
    }

    golden_parsed_output = {
        "instance": {
            "master": {
                "areas": {
                    "0.0.0.1": {
                        "interfaces": {
                            "ge-0/0/2.0": {
                                "state": "BDR",
                                "dr_id": "10.16.2.2",
                                "bdr_id": "10.64.4.4",
                                "nbrs_count": 5,
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_master = {
        "execute.return_value": """
    show ospf interface brief instance master
    Interface           State   Area            DR ID           BDR ID          Nbrs
    ge-0/0/4.0          BDR     0.0.0.4         10.64.4.4         192.168.10.22    2
    ge-0/0/5.0          BDR     0.0.0.4         10.16.2.2         10.16.2.2          3
    ge-0/0/6.0          DR      0.0.0.4         10.64.4.4         192.168.10.22    4
    lo1.0               DR      0.0.0.4         10.16.2.2         0.0.0.0          0
    """
    }

    golden_parsed_output_master = {
        "instance": {
            "master": {
                "areas": {
                    "0.0.0.4": {
                        "interfaces": {
                            "ge-0/0/4.0": {
                                "state": "BDR",
                                "dr_id": "10.64.4.4",
                                "bdr_id": "192.168.10.22",
                                "nbrs_count": 2,
                            },
                            "ge-0/0/5.0": {
                                "state": "BDR",
                                "dr_id": "10.16.2.2",
                                "bdr_id": "10.16.2.2",
                                "nbrs_count": 3,
                            },
                            "ge-0/0/6.0": {
                                "state": "DR",
                                "dr_id": "10.64.4.4",
                                "bdr_id": "192.168.10.22",
                                "nbrs_count": 4,
                            },
                            "lo1.0": {
                                "state": "DR",
                                "dr_id": "10.16.2.2",
                                "bdr_id": "0.0.0.0",
                                "nbrs_count": 0,
                            },
                        }
                    }
                }
            }
        }
    }

    golden_output_interface = {
        "execute.return_value": """
    show ospf interface ge-0/0/4.0 brief
    Interface           State   Area            DR ID           BDR ID          Nbrs
    ge-0/0/4.0          PtToPt  0.0.0.1         10.16.2.1         10.64.2.4            1
    """
    }

    golden_parsed_output_interface = {
        "instance": {
            "master": {
                "areas": {
                    "0.0.0.1": {
                        "interfaces": {
                            "ge-0/0/4.0": {
                                "state": "PtToPt",
                                "dr_id": "10.16.2.1",
                                "bdr_id": "10.64.2.4",
                                "nbrs_count": 1,
                            }
                        }
                    }
                }
            }
        }
    }

    def test_show_ospf_interface_brief_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspfInterfaceBrief(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_show_ospf_interface_brief(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspfInterfaceBrief(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_ospf_interface_brief_instance_master(self):
        self.device = Mock(**self.golden_output_master)
        obj = ShowOspfInterfaceBrief(device=self.device)
        parsed_output = obj.parse(instance="master")
        self.assertEqual(parsed_output, self.golden_parsed_output_master)

    def test_show_ospf_interface_interface_brief(self):
        self.device = Mock(**self.golden_output_interface)
        obj = ShowOspfInterfaceBrief(device=self.device)
        parsed_output = obj.parse(interface="ge-0/0/4.0")
        self.assertEqual(parsed_output, self.golden_parsed_output_interface)


class test_show_ospf_interface_detail(unittest.TestCase):
    """ Unit tests for:
            * show ospf interface detail
            * show ospf interface {interface} detail
    """

    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
    show ospf interface detail
    Interface           State   Area            DR ID           BDR ID          Nbrs
    ge-0/0/0.0          PtToPt  0.0.0.1         0.0.0.0         0.0.0.0            1
      Type: P2P, Address: 172.16.94.1, Mask: 255.255.255.0, MTU: 500, Cost: 50
      Adj count: 1
      Hello: 10, Dead: 20, ReXmit: 10, Not Stub
      Auth type: None
      Protection type: Post Convergence
      Post convergence protection: Enabled, Fate sharing: No, SRLG: No, Node cost: 50
      Topology default (ID 0) -> Cost: 50
    ge-0/0/1.0          PtToPt  0.0.0.1         0.0.0.0         0.0.0.0            1
      Type: P2P, Address: 172.16.94.1, Mask: 255.255.255.0, MTU: 500, Cost: 100
      Adj count: 1
      Hello: 10, Dead: 10, ReXmit: 5, Not Stub
      Auth type: None
      Protection type: Post Convergence
      Post convergence protection: Enabled, Fate sharing: No, SRLG: No, Node cost: 100
      Topology default (ID 0) -> Cost: 100
    """
    }

    golden_parsed_output = {
        "instance": {
            "master": {
                "areas": {
                    "0.0.0.1": {
                        "interfaces": {
                            "ge-0/0/0.0": {
                                "state": "PtToPt",
                                "dr_id": "0.0.0.0",
                                "bdr_id": "0.0.0.0",
                                "nbrs_count": 1,
                                "type": "P2P",
                                "address": "172.16.94.1",
                                "mask": "255.255.255.0",
                                "mtu": 500,
                                "cost": 50,
                                "adj_count": 1,
                                "hello": 10,
                                "dead": 20,
                                "rexmit": 10,
                                "ospf_stub_type": "Not Stub",
                                "authentication_type": "None",
                                "ospf_interface": {
                                    "protection_type": "Post Convergence",
                                    "tilfa": {
                                        "prot_link": "Enabled",
                                        "prot_fate": "No",
                                        "prot_srlg": "No",
                                        "prot_node": 50,
                                    },
                                    "topology": {"default": {"id": 0, "metric": 50}},
                                },
                            },
                            "ge-0/0/1.0": {
                                "state": "PtToPt",
                                "dr_id": "0.0.0.0",
                                "bdr_id": "0.0.0.0",
                                "nbrs_count": 1,
                                "type": "P2P",
                                "address": "172.16.94.1",
                                "mask": "255.255.255.0",
                                "mtu": 500,
                                "cost": 100,
                                "adj_count": 1,
                                "hello": 10,
                                "dead": 10,
                                "rexmit": 5,
                                "ospf_stub_type": "Not Stub",
                                "authentication_type": "None",
                                "ospf_interface": {
                                    "protection_type": "Post Convergence",
                                    "tilfa": {
                                        "prot_link": "Enabled",
                                        "prot_fate": "No",
                                        "prot_srlg": "No",
                                        "prot_node": 100,
                                    },
                                    "topology": {"default": {"id": 0, "metric": 100}},
                                },
                            },
                        }
                    }
                }
            }
        }
    }

    golden_output_interface = {
        "execute.return_value": """
    show ospf interface ge-0/0/1.0 detail
    Interface           State   Area            DR ID           BDR ID          Nbrs
    ge-0/0/1.0          PtToPt  0.0.0.1         0.0.0.0         0.0.0.0            1
      Type: P2P, Address: 172.16.94.1, Mask: 255.255.255.0, MTU: 500, Cost: 100
      Adj count: 1
      Hello: 10, Dead: 10, ReXmit: 5, Not Stub
      Auth type: None
      Protection type: Post Convergence
      Post convergence protection: Enabled, Fate sharing: No, SRLG: No, Node cost: 100
      Topology default (ID 0) -> Cost: 100
    """
    }

    golden_parsed_output_interface = {
        "instance": {
            "master": {
                "areas": {
                    "0.0.0.1": {
                        "interfaces": {
                            "ge-0/0/1.0": {
                                "state": "PtToPt",
                                "dr_id": "0.0.0.0",
                                "bdr_id": "0.0.0.0",
                                "nbrs_count": 1,
                                "type": "P2P",
                                "address": "172.16.94.1",
                                "mask": "255.255.255.0",
                                "mtu": 500,
                                "cost": 100,
                                "adj_count": 1,
                                "hello": 10,
                                "dead": 10,
                                "rexmit": 5,
                                "ospf_stub_type": "Not Stub",
                                "authentication_type": "None",
                                "ospf_interface": {
                                    "protection_type": "Post Convergence",
                                    "tilfa": {
                                        "prot_link": "Enabled",
                                        "prot_fate": "No",
                                        "prot_srlg": "No",
                                        "prot_node": 100,
                                    },
                                    "topology": {"default": {"id": 0, "metric": 100}},
                                },
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_instance = {
        "execute.return_value": """
        show ospf interface detail instance master
        Interface           State   Area            DR ID           BDR ID          Nbrs
        ge-0/0/0.0          PtToPt  0.0.0.1         0.0.0.0         0.0.0.0            1
          Type: P2P, Address: 172.16.94.1, Mask: 255.255.255.0, MTU: 500, Cost: 50
          Adj count: 1
          Hello: 10, Dead: 20, ReXmit: 10, Not Stub
          Auth type: None
          Protection type: Post Convergence
          Post convergence protection: Enabled, Fate sharing: No, SRLG: No, Node cost: 50
          Topology default (ID 0) -> Cost: 50
        ge-0/0/1.0          PtToPt  0.0.0.1         0.0.0.0         0.0.0.0            1
          Type: P2P, Address: 172.16.94.1, Mask: 255.255.255.0, MTU: 500, Cost: 100
          Adj count: 1
          Hello: 10, Dead: 10, ReXmit: 5, Not Stub
          Auth type: None
          Protection type: Post Convergence
          Post convergence protection: Enabled, Fate sharing: No, SRLG: No, Node cost: 100
          Topology default (ID 0) -> Cost: 100
        """
    }

    golden_parsed_output_instance = {
        "instance": {
            "master": {
                "areas": {
                    "0.0.0.1": {
                        "interfaces": {
                            "ge-0/0/0.0": {
                                "state": "PtToPt",
                                "dr_id": "0.0.0.0",
                                "bdr_id": "0.0.0.0",
                                "nbrs_count": 1,
                                "type": "P2P",
                                "address": "172.16.94.1",
                                "mask": "255.255.255.0",
                                "mtu": 500,
                                "cost": 50,
                                "adj_count": 1,
                                "hello": 10,
                                "dead": 20,
                                "rexmit": 10,
                                "ospf_stub_type": "Not Stub",
                                "authentication_type": "None",
                                "ospf_interface": {
                                    "protection_type": "Post Convergence",
                                    "tilfa": {
                                        "prot_link": "Enabled",
                                        "prot_fate": "No",
                                        "prot_srlg": "No",
                                        "prot_node": 50,
                                    },
                                    "topology": {"default": {"id": 0, "metric": 50}},
                                },
                            },
                            "ge-0/0/1.0": {
                                "state": "PtToPt",
                                "dr_id": "0.0.0.0",
                                "bdr_id": "0.0.0.0",
                                "nbrs_count": 1,
                                "type": "P2P",
                                "address": "172.16.94.1",
                                "mask": "255.255.255.0",
                                "mtu": 500,
                                "cost": 100,
                                "adj_count": 1,
                                "hello": 10,
                                "dead": 10,
                                "rexmit": 5,
                                "ospf_stub_type": "Not Stub",
                                "authentication_type": "None",
                                "ospf_interface": {
                                    "protection_type": "Post Convergence",
                                    "tilfa": {
                                        "prot_link": "Enabled",
                                        "prot_fate": "No",
                                        "prot_srlg": "No",
                                        "prot_node": 100,
                                    },
                                    "topology": {"default": {"id": 0, "metric": 100}},
                                },
                            },
                        }
                    }
                }
            }
        }
    }

    golden_output_interface_instance = {
        "execute.return_value": """
        show ospf interface ge-0/0/1.0 detail instance master
        Interface           State   Area            DR ID           BDR ID          Nbrs
        ge-0/0/1.0          PtToPt  0.0.0.1         0.0.0.0         0.0.0.0            1
          Type: P2P, Address: 172.16.94.1, Mask: 255.255.255.0, MTU: 500, Cost: 100
          Adj count: 1
          Hello: 10, Dead: 10, ReXmit: 5, Not Stub
          Auth type: None
          Protection type: Post Convergence
          Post convergence protection: Enabled, Fate sharing: No, SRLG: No, Node cost: 100
          Topology default (ID 0) -> Cost: 100
        """
    }

    golden_parsed_output_interface_instance = {
        "instance": {
            "master": {
                "areas": {
                    "0.0.0.1": {
                        "interfaces": {
                            "ge-0/0/1.0": {
                                "state": "PtToPt",
                                "dr_id": "0.0.0.0",
                                "bdr_id": "0.0.0.0",
                                "nbrs_count": 1,
                                "type": "P2P",
                                "address": "172.16.94.1",
                                "mask": "255.255.255.0",
                                "mtu": 500,
                                "cost": 100,
                                "adj_count": 1,
                                "hello": 10,
                                "dead": 10,
                                "rexmit": 5,
                                "ospf_stub_type": "Not Stub",
                                "authentication_type": "None",
                                "ospf_interface": {
                                    "protection_type": "Post Convergence",
                                    "tilfa": {
                                        "prot_link": "Enabled",
                                        "prot_fate": "No",
                                        "prot_srlg": "No",
                                        "prot_node": 100,
                                    },
                                    "topology": {"default": {"id": 0, "metric": 100}},
                                },
                            }
                        }
                    }
                }
            }
        }
    }

    def test_show_ospf_interface_detail_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspfInterfaceDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_show_ospf_interface_detail(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspfInterfaceDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_ospf_interface_interface_detail(self):
        self.device = Mock(**self.golden_output_interface)
        obj = ShowOspfInterfaceDetail(device=self.device)
        parsed_output = obj.parse(interface="ge-0/0/1.0")
        self.assertEqual(parsed_output, self.golden_parsed_output_interface)

    def test_show_ospf_interface_detail_instance(self):
        self.device = Mock(**self.golden_output_instance)
        obj = ShowOspfInterfaceDetail(device=self.device)
        parsed_output = obj.parse(instance="master")
        self.assertEqual(parsed_output, self.golden_parsed_output_instance)

    def test_show_ospf_interface_detail_interface_instance(self):
        self.device = Mock(**self.golden_output_interface_instance)
        obj = ShowOspfInterfaceDetail(device=self.device)
        parsed_output = obj.parse(interface="ge-0/0/1.0", instance="master")
        self.assertEqual(parsed_output, self.golden_parsed_output_interface_instance)


class TestShowOspfNeighbor(unittest.TestCase):
    """ Unit tests for:
            * show ospf neighbor
    """

    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
        show ospf neighbor
        Address          Interface              State     ID               Pri  Dead
        10.189.5.94      ge-0/0/0.0             Full      10.189.5.253     128    32
        10.169.14.121   ge-0/0/1.0             Full      10.169.14.240   128    33
        10.19.198.26     ge-0/0/2.0             Full      10.19.198.239      1    33
        """
    }

    golden_parsed_output = {
        "ospf-neighbor-information": {
            "ospf-neighbor": [
                {
                    "neighbor-address": "10.189.5.94",
                    "interface-name": "ge-0/0/0.0",
                    "ospf-neighbor-state": "Full",
                    "neighbor-id": "10.189.5.253",
                    "neighbor-priority": "128",
                    "activity-timer": "32",
                },
                {
                    "neighbor-address": "10.169.14.121",
                    "interface-name": "ge-0/0/1.0",
                    "ospf-neighbor-state": "Full",
                    "neighbor-id": "10.169.14.240",
                    "neighbor-priority": "128",
                    "activity-timer": "33",
                },
                {
                    "neighbor-address": "10.19.198.26",
                    "interface-name": "ge-0/0/2.0",
                    "ospf-neighbor-state": "Full",
                    "neighbor-id": "10.19.198.239",
                    "neighbor-priority": "1",
                    "activity-timer": "33",
                },
            ]
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspfNeighbor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspfNeighbor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowOspfDatabase(unittest.TestCase):
    """ Unit tests for:
            * show ospf database
    """

    device = Device(name="aDevice")
    maxDiff = None

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
        show ospf database

            OSPF database, Area 0.0.0.8
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
        Router   10.36.3.3          10.36.3.3          0x80004d2d    61  0x22 0xa127 2496
        Router   10.100.5.5          10.100.5.5          0x800019d7  1469  0x22 0xa1c   60
        Router   10.19.198.239    10.19.198.239    0x80000442   622  0x22 0x95bf  96
        Router   10.34.2.250     10.34.2.250     0x8000205a   736  0x22 0x26f6 144
        Router   10.34.2.251     10.34.2.251     0x80001dde   567  0x22 0x1022 108
        Router   10.169.196.241  10.169.196.241  0x800004a4    35  0x22 0x1055 144
        Router   10.169.14.240   10.169.14.240   0x80001bc1  2732  0x22 0x3a76 144
        Router   10.169.14.241   10.169.14.241   0x80001f67  1468  0x22 0x81fa 120
        Router  *10.189.5.252     10.189.5.252     0x80001b9e  1608  0x22 0x1e2  120
        Router   10.189.5.253     10.189.5.253     0x80001b04  1689  0x22 0xe230 108
        Router   192.168.36.119  192.168.36.119  0x800019de   928  0x22 0xc6a6  48
        Router   192.168.36.120  192.168.36.120  0x800019ea   500  0x22 0x2747  48
        Network  192.168.36.49   10.169.14.240   0x80000499   485  0x22 0xbb30  32
        Network  192.168.36.57   10.169.14.240   0x80000498  2292  0x22 0x5f86  32
        OpaqArea 10.1.0.0          10.100.5.5          0x800019ac  1469  0x20 0xc57f  28
        OpaqArea 10.1.0.0          10.19.198.239    0x8000028c   622  0x20 0x4e06  28
        OpaqArea 10.1.0.0          10.169.196.241  0x80000fdd   521  0x20 0xe9d4  28
        OpaqArea 10.1.0.1          10.34.2.250     0x800019e5  1888  0x22 0x902f  28
        OpaqArea 10.1.0.1          10.34.2.251     0x800019c7  1664  0x22 0xd00b  28
        OpaqArea 10.1.0.1          10.169.14.240   0x80001987   334  0x22 0xde66  28
        OpaqArea 10.1.0.1          10.169.14.241   0x80001e31  1907  0x22 0x8014  28
        OpaqArea*10.1.0.1          10.189.5.252     0x80001a15   231  0x22 0xd49a  28
        OpaqArea 10.1.0.1          10.189.5.253     0x80001a0f   901  0x22 0xe48e  28
        OpaqArea 10.1.0.3          10.34.2.250     0x800013d3  2119  0x22 0x47bd 136
        OpaqArea 10.1.0.3          10.34.2.251     0x800013b5  1445  0x22 0x5fc3 136
        OpaqArea 10.1.0.3          10.169.14.240   0x8000063d  1690  0x22 0x75dc 136
        OpaqArea 10.1.0.3          10.169.14.241   0x80000c51   951  0x22 0x1721 136
        OpaqArea*10.1.0.3          10.189.5.252     0x80000321  2678  0x22 0x97cc 136
        OpaqArea 10.1.0.3          10.189.5.253     0x80000322  2500  0x22 0x71f1 136
        OpaqArea 10.1.0.4          10.34.2.250     0x8000029e  1427  0x22 0x1e4  136
        OpaqArea 10.1.0.4          10.34.2.251     0x80000299  1226  0x22 0x29c0 136
        OpaqArea 10.1.0.4          10.169.14.240   0x800003f8  1238  0x22 0xb606 136
        OpaqArea 10.1.0.4          10.169.14.241   0x800013fe  2127  0x22 0x694d 136
        OpaqArea*10.1.0.4          10.189.5.252     0x800013e8  2411  0x22 0xb804 136
        OpaqArea 10.1.0.4          10.189.5.253     0x80000f9b  2772  0x22 0x4ecf 136
        OpaqArea 10.1.0.5          10.34.2.250     0x800001b5   289  0x22 0x5e9d 136
        OpaqArea 10.1.0.5          10.34.2.251     0x800001b5   276  0x22 0xd817 136
        OpaqArea 10.1.0.5          10.169.14.240   0x80000289    33  0x22 0xdd1f 136
        OpaqArea 10.1.0.5          10.169.14.241   0x80000298  1687  0x22 0x21a9 136
        OpaqArea*10.1.0.5          10.189.5.252     0x800001bb  1312  0x22 0x79b5 136
        OpaqArea 10.1.0.5          10.189.5.253     0x800001bb  1147  0x22 0x5ec3 136
        OpaqArea 10.1.0.6          10.100.5.5          0x800019be  1469  0x20 0x629a 168
        OpaqArea 10.1.0.10         10.19.198.239    0x8000025d   622  0x20 0xcffa 132
        OpaqArea 10.1.0.10         10.169.196.241  0x8000025d   521  0x20 0x771b 132
        OpaqArea 10.1.0.11         10.19.198.239    0x8000025d   622  0x20 0xecd3 132
        OpaqArea 10.1.0.11         10.169.196.241  0x8000025d   521  0x20 0xa14f 132
        OpaqArea 10.1.0.12         10.19.198.239    0x80000163   622  0x20 0x87f8  80
        OpaqArea 10.1.8.69         10.169.196.241  0x8000003b    35  0x20 0x8150  80
        OpaqArea 10.1.8.70         10.169.196.241  0x80000151   521  0x20 0x8a2d  80
        OpaqArea 10.16.0.0          10.100.5.5          0x800019ac  1469  0x20 0x810a  52
        OpaqArea 10.16.0.0          10.19.198.239    0x8000028c   622  0x20 0x8e0f  76
        OpaqArea 10.16.0.0          10.34.2.250     0x80001a15  2810  0x22 0xbd3d  44
        OpaqArea 10.16.0.0          10.34.2.251     0x800019e4  2103  0x22 0x1b10  44
        OpaqArea 10.16.0.0          10.169.196.241  0x800003a6   521  0x20 0x2db9  76
        OpaqArea 10.16.0.0          10.169.14.240   0x8000199d  2142  0x22 0x15f1  44
        OpaqArea 10.16.0.0          10.169.14.241   0x80001e44    48  0x22 0xb2a7  44
        OpaqArea*10.16.0.0          10.189.5.252     0x80001a2a   771  0x22 0xe5ef  44
        OpaqArea 10.16.0.0          10.189.5.253     0x80001a21   410  0x22 0xf1eb  44
        OpaqArea 10.49.0.0          10.19.198.239    0x8000028c   622  0x20 0xcdab  44
        OpaqArea 10.49.0.0          10.169.196.241  0x800003a4   521  0x20 0x69c9  44
        OpaqArea 10.49.0.1          10.100.5.5          0x800019ac  1469  0x20 0x6c5a  44
        OpaqArea 10.49.0.1          10.34.2.250     0x80001fa9   736  0x22 0x7fa7  44
        OpaqArea 10.49.0.1          10.34.2.251     0x80001cfb   567  0x22 0x6ce   44
        OpaqArea 10.49.0.1          10.169.14.240   0x80001bc1  2732  0x22 0x99aa  44
        OpaqArea 10.49.0.1          10.169.14.241   0x80001f67  1468  0x22 0x6433  44
        OpaqArea*10.49.0.1          10.189.5.252     0x80001b9e  1608  0x22 0x8c7f  44
        OpaqArea 10.49.0.1          10.189.5.253     0x80001b04  1689  0x22 0xe3bf  44
        OpaqArea 10.64.0.1          10.34.2.250     0x800004f9    76  0x22 0x39a3  60
        OpaqArea 10.64.0.1          10.169.14.241   0x80000311   725  0x22 0x7002  60
        OpaqArea 10.64.0.1          10.189.5.253     0x8000030a  2230  0x22 0x6915  60
        OpaqArea 10.64.0.2          10.169.14.241   0x80000305   499  0x22 0x7271  60
        OpaqArea 10.64.0.3          10.169.14.241   0x8000029a   274  0x22 0x7248  60
        OpaqArea 10.64.0.3          10.189.5.253     0x800002db   656  0x22 0x34eb  60
        OpaqArea 10.64.0.4          10.189.5.253     0x800001bb  1960  0x22 0x31be  60
        OpaqArea 10.64.0.6          10.100.5.5          0x800019bf  1469  0x20 0x4de2  56
        OpaqArea 10.64.0.7          10.34.2.250     0x8000046b  2580  0x22 0xb9a6  48
        OpaqArea 10.64.0.7          10.34.2.251     0x800004de  1006  0x22 0x6a96  60
        OpaqArea 10.64.0.17         10.19.198.239    0x8000025d   622  0x20 0xb34a 104
        OpaqArea 10.64.0.17         10.169.196.241  0x8000025d   521  0x20 0x3e3c 104
        OpaqArea 10.64.0.18         10.19.198.239    0x8000025d   622  0x20 0xb938 104
        OpaqArea 10.64.0.18         10.169.196.241  0x8000025d   521  0x20 0x6fdb 104
        OpaqArea 10.64.0.31         10.34.2.251     0x8000029a  2542  0x22 0xe909  60
        OpaqArea 10.64.0.32         10.34.2.251     0x800001b5   787  0x22 0xe396  60
        OpaqArea 10.64.0.37         10.34.2.250     0x8000029b  1658  0x22 0xffb8  60
        OpaqArea 10.64.0.38         10.34.2.250     0x800001b5   966  0x22 0x71b3  60
        OpaqArea*10.64.0.52         10.189.5.252     0x80000308   501  0x22 0x7efa  60
        OpaqArea*10.64.0.54         10.189.5.252     0x800002dc  1042  0x22 0x1839  60
        OpaqArea*10.64.0.55         10.189.5.252     0x800001bb  1876  0x22 0x92eb  60
        OpaqArea 10.64.0.57         10.169.14.240   0x80000303  1087  0x22 0x7544  60
        OpaqArea 10.64.0.59         10.169.14.240   0x800002f4  1389  0x22 0x6d12  60
        OpaqArea 10.64.0.60         10.169.14.240   0x8000028b   937  0x22 0x4f1a  60
        OpaqArea 10.64.8.74         10.169.196.241  0x80000030    35  0x20 0xdcd1  92
        OpaqArea 10.64.8.75         10.169.196.241  0x80000151   521  0x20 0xd4b0  92
            OSPF AS SCOPE link state database
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
        Extern   0.0.0.0          10.34.2.251     0x800019e3  2323  0x22 0x6715  36
        Extern   0.0.0.0          10.169.14.240   0x8000039e  1991  0x22 0x9fcc  36
        Extern   10.1.0.0          192.168.36.119  0x800019b0   928  0x20 0x3bc3  36
        Extern   10.1.0.0          192.168.36.120  0x800019b1   500  0x20 0x33c9  36
        Extern   10.174.132.237    10.169.14.240   0x8000039e  1841  0x22 0xf161  36
        Extern   10.34.2.250     10.169.14.240   0x80000288  2443  0x22 0x473e  36
        Extern   10.34.2.250     10.169.14.241   0x80000298  2346  0x22 0x2153  36
        Extern   10.34.2.251     10.169.14.240   0x80000289   184  0x22 0x3b48  36
        Extern   10.34.2.251     10.169.14.241   0x80000298  1176  0x22 0x175c  36
        Extern   10.169.14.240   10.34.2.250     0x8000029a  1197  0x22 0xf88e  36
        Extern   10.169.14.240   10.34.2.251     0x800019e4  1884  0x22 0x190c  36
        Extern  *10.169.14.240   10.189.5.252     0x80001a3a  2143  0x22 0xc3fb  36
        Extern   10.169.14.241   10.34.2.250     0x80001a14  2349  0x22 0xb341  36
        Extern   10.169.14.241   10.34.2.251     0x80000299    50  0x22 0xea9b  36
        Extern   10.169.14.241   10.189.5.253     0x80000fae   164  0x22 0xeb68  36
        Extern   10.189.5.252     10.169.14.240   0x800019b0  1539  0x22 0xc372  36
        Extern   10.189.5.253     10.169.14.241   0x8000140f  2566  0x22 0x6d4   36
        Extern   192.168.100.0    10.169.14.240   0x800002da   786  0x22 0xfb51  36
        Extern   192.168.100.252  10.169.14.240   0x800002d9   636  0x22 0x19b8  36
    """
    }

    golden_parsed_output = {
        "ospf-database-information": {
            "ospf-area-header": {"ospf-area": "0.0.0.8"},
            "ospf-database": [
                {
                    "advertising-router": "10.36.3.3",
                    "age": "61",
                    "checksum": "0xa127",
                    "lsa-id": "10.36.3.3",
                    "lsa-length": "2496",
                    "lsa-type": "Router",
                    "options": "0x22",
                    "sequence-number": "0x80004d2d",
                },
                {
                    "advertising-router": "10.100.5.5",
                    "age": "1469",
                    "checksum": "0xa1c",
                    "lsa-id": "10.100.5.5",
                    "lsa-length": "60",
                    "lsa-type": "Router",
                    "options": "0x22",
                    "sequence-number": "0x800019d7",
                },
                {
                    "advertising-router": "10.19.198.239",
                    "age": "622",
                    "checksum": "0x95bf",
                    "lsa-id": "10.19.198.239",
                    "lsa-length": "96",
                    "lsa-type": "Router",
                    "options": "0x22",
                    "sequence-number": "0x80000442",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "736",
                    "checksum": "0x26f6",
                    "lsa-id": "10.34.2.250",
                    "lsa-length": "144",
                    "lsa-type": "Router",
                    "options": "0x22",
                    "sequence-number": "0x8000205a",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "567",
                    "checksum": "0x1022",
                    "lsa-id": "10.34.2.251",
                    "lsa-length": "108",
                    "lsa-type": "Router",
                    "options": "0x22",
                    "sequence-number": "0x80001dde",
                },
                {
                    "advertising-router": "10.169.196.241",
                    "age": "35",
                    "checksum": "0x1055",
                    "lsa-id": "10.169.196.241",
                    "lsa-length": "144",
                    "lsa-type": "Router",
                    "options": "0x22",
                    "sequence-number": "0x800004a4",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "2732",
                    "checksum": "0x3a76",
                    "lsa-id": "10.169.14.240",
                    "lsa-length": "144",
                    "lsa-type": "Router",
                    "options": "0x22",
                    "sequence-number": "0x80001bc1",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "1468",
                    "checksum": "0x81fa",
                    "lsa-id": "10.169.14.241",
                    "lsa-length": "120",
                    "lsa-type": "Router",
                    "options": "0x22",
                    "sequence-number": "0x80001f67",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "1608",
                    "checksum": "0x1e2",
                    "lsa-id": "10.189.5.252",
                    "lsa-length": "120",
                    "lsa-type": "Router",
                    "options": "0x22",
                    "our-entry": True,
                    "sequence-number": "0x80001b9e",
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "1689",
                    "checksum": "0xe230",
                    "lsa-id": "10.189.5.253",
                    "lsa-length": "108",
                    "lsa-type": "Router",
                    "options": "0x22",
                    "sequence-number": "0x80001b04",
                },
                {
                    "advertising-router": "192.168.36.119",
                    "age": "928",
                    "checksum": "0xc6a6",
                    "lsa-id": "192.168.36.119",
                    "lsa-length": "48",
                    "lsa-type": "Router",
                    "options": "0x22",
                    "sequence-number": "0x800019de",
                },
                {
                    "advertising-router": "192.168.36.120",
                    "age": "500",
                    "checksum": "0x2747",
                    "lsa-id": "192.168.36.120",
                    "lsa-length": "48",
                    "lsa-type": "Router",
                    "options": "0x22",
                    "sequence-number": "0x800019ea",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "485",
                    "checksum": "0xbb30",
                    "lsa-id": "192.168.36.49",
                    "lsa-length": "32",
                    "lsa-type": "Network",
                    "options": "0x22",
                    "sequence-number": "0x80000499",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "2292",
                    "checksum": "0x5f86",
                    "lsa-id": "192.168.36.57",
                    "lsa-length": "32",
                    "lsa-type": "Network",
                    "options": "0x22",
                    "sequence-number": "0x80000498",
                },
                {
                    "advertising-router": "10.100.5.5",
                    "age": "1469",
                    "checksum": "0xc57f",
                    "lsa-id": "10.1.0.0",
                    "lsa-length": "28",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x800019ac",
                },
                {
                    "advertising-router": "10.19.198.239",
                    "age": "622",
                    "checksum": "0x4e06",
                    "lsa-id": "10.1.0.0",
                    "lsa-length": "28",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x8000028c",
                },
                {
                    "advertising-router": "10.169.196.241",
                    "age": "521",
                    "checksum": "0xe9d4",
                    "lsa-id": "10.1.0.0",
                    "lsa-length": "28",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x80000fdd",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "1888",
                    "checksum": "0x902f",
                    "lsa-id": "10.1.0.1",
                    "lsa-length": "28",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x800019e5",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "1664",
                    "checksum": "0xd00b",
                    "lsa-id": "10.1.0.1",
                    "lsa-length": "28",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x800019c7",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "334",
                    "checksum": "0xde66",
                    "lsa-id": "10.1.0.1",
                    "lsa-length": "28",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80001987",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "1907",
                    "checksum": "0x8014",
                    "lsa-id": "10.1.0.1",
                    "lsa-length": "28",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80001e31",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "231",
                    "checksum": "0xd49a",
                    "lsa-id": "10.1.0.1",
                    "lsa-length": "28",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "our-entry": True,
                    "sequence-number": "0x80001a15",
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "901",
                    "checksum": "0xe48e",
                    "lsa-id": "10.1.0.1",
                    "lsa-length": "28",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80001a0f",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "2119",
                    "checksum": "0x47bd",
                    "lsa-id": "10.1.0.3",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x800013d3",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "1445",
                    "checksum": "0x5fc3",
                    "lsa-id": "10.1.0.3",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x800013b5",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "1690",
                    "checksum": "0x75dc",
                    "lsa-id": "10.1.0.3",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x8000063d",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "951",
                    "checksum": "0x1721",
                    "lsa-id": "10.1.0.3",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80000c51",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "2678",
                    "checksum": "0x97cc",
                    "lsa-id": "10.1.0.3",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "our-entry": True,
                    "sequence-number": "0x80000321",
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "2500",
                    "checksum": "0x71f1",
                    "lsa-id": "10.1.0.3",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80000322",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "1427",
                    "checksum": "0x1e4",
                    "lsa-id": "10.1.0.4",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x8000029e",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "1226",
                    "checksum": "0x29c0",
                    "lsa-id": "10.1.0.4",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80000299",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "1238",
                    "checksum": "0xb606",
                    "lsa-id": "10.1.0.4",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x800003f8",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "2127",
                    "checksum": "0x694d",
                    "lsa-id": "10.1.0.4",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x800013fe",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "2411",
                    "checksum": "0xb804",
                    "lsa-id": "10.1.0.4",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "our-entry": True,
                    "sequence-number": "0x800013e8",
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "2772",
                    "checksum": "0x4ecf",
                    "lsa-id": "10.1.0.4",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80000f9b",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "289",
                    "checksum": "0x5e9d",
                    "lsa-id": "10.1.0.5",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x800001b5",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "276",
                    "checksum": "0xd817",
                    "lsa-id": "10.1.0.5",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x800001b5",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "33",
                    "checksum": "0xdd1f",
                    "lsa-id": "10.1.0.5",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80000289",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "1687",
                    "checksum": "0x21a9",
                    "lsa-id": "10.1.0.5",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80000298",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "1312",
                    "checksum": "0x79b5",
                    "lsa-id": "10.1.0.5",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "our-entry": True,
                    "sequence-number": "0x800001bb",
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "1147",
                    "checksum": "0x5ec3",
                    "lsa-id": "10.1.0.5",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x800001bb",
                },
                {
                    "advertising-router": "10.100.5.5",
                    "age": "1469",
                    "checksum": "0x629a",
                    "lsa-id": "10.1.0.6",
                    "lsa-length": "168",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x800019be",
                },
                {
                    "advertising-router": "10.19.198.239",
                    "age": "622",
                    "checksum": "0xcffa",
                    "lsa-id": "10.1.0.10",
                    "lsa-length": "132",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x8000025d",
                },
                {
                    "advertising-router": "10.169.196.241",
                    "age": "521",
                    "checksum": "0x771b",
                    "lsa-id": "10.1.0.10",
                    "lsa-length": "132",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x8000025d",
                },
                {
                    "advertising-router": "10.19.198.239",
                    "age": "622",
                    "checksum": "0xecd3",
                    "lsa-id": "10.1.0.11",
                    "lsa-length": "132",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x8000025d",
                },
                {
                    "advertising-router": "10.169.196.241",
                    "age": "521",
                    "checksum": "0xa14f",
                    "lsa-id": "10.1.0.11",
                    "lsa-length": "132",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x8000025d",
                },
                {
                    "advertising-router": "10.19.198.239",
                    "age": "622",
                    "checksum": "0x87f8",
                    "lsa-id": "10.1.0.12",
                    "lsa-length": "80",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x80000163",
                },
                {
                    "advertising-router": "10.169.196.241",
                    "age": "35",
                    "checksum": "0x8150",
                    "lsa-id": "10.1.8.69",
                    "lsa-length": "80",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x8000003b",
                },
                {
                    "advertising-router": "10.169.196.241",
                    "age": "521",
                    "checksum": "0x8a2d",
                    "lsa-id": "10.1.8.70",
                    "lsa-length": "80",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x80000151",
                },
                {
                    "advertising-router": "10.100.5.5",
                    "age": "1469",
                    "checksum": "0x810a",
                    "lsa-id": "10.16.0.0",
                    "lsa-length": "52",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x800019ac",
                },
                {
                    "advertising-router": "10.19.198.239",
                    "age": "622",
                    "checksum": "0x8e0f",
                    "lsa-id": "10.16.0.0",
                    "lsa-length": "76",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x8000028c",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "2810",
                    "checksum": "0xbd3d",
                    "lsa-id": "10.16.0.0",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80001a15",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "2103",
                    "checksum": "0x1b10",
                    "lsa-id": "10.16.0.0",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x800019e4",
                },
                {
                    "advertising-router": "10.169.196.241",
                    "age": "521",
                    "checksum": "0x2db9",
                    "lsa-id": "10.16.0.0",
                    "lsa-length": "76",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x800003a6",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "2142",
                    "checksum": "0x15f1",
                    "lsa-id": "10.16.0.0",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x8000199d",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "48",
                    "checksum": "0xb2a7",
                    "lsa-id": "10.16.0.0",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80001e44",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "771",
                    "checksum": "0xe5ef",
                    "lsa-id": "10.16.0.0",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "our-entry": True,
                    "sequence-number": "0x80001a2a",
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "410",
                    "checksum": "0xf1eb",
                    "lsa-id": "10.16.0.0",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80001a21",
                },
                {
                    "advertising-router": "10.19.198.239",
                    "age": "622",
                    "checksum": "0xcdab",
                    "lsa-id": "10.49.0.0",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x8000028c",
                },
                {
                    "advertising-router": "10.169.196.241",
                    "age": "521",
                    "checksum": "0x69c9",
                    "lsa-id": "10.49.0.0",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x800003a4",
                },
                {
                    "advertising-router": "10.100.5.5",
                    "age": "1469",
                    "checksum": "0x6c5a",
                    "lsa-id": "10.49.0.1",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x800019ac",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "736",
                    "checksum": "0x7fa7",
                    "lsa-id": "10.49.0.1",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80001fa9",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "567",
                    "checksum": "0x6ce",
                    "lsa-id": "10.49.0.1",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80001cfb",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "2732",
                    "checksum": "0x99aa",
                    "lsa-id": "10.49.0.1",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80001bc1",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "1468",
                    "checksum": "0x6433",
                    "lsa-id": "10.49.0.1",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80001f67",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "1608",
                    "checksum": "0x8c7f",
                    "lsa-id": "10.49.0.1",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "our-entry": True,
                    "sequence-number": "0x80001b9e",
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "1689",
                    "checksum": "0xe3bf",
                    "lsa-id": "10.49.0.1",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80001b04",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "76",
                    "checksum": "0x39a3",
                    "lsa-id": "10.64.0.1",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x800004f9",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "725",
                    "checksum": "0x7002",
                    "lsa-id": "10.64.0.1",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80000311",
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "2230",
                    "checksum": "0x6915",
                    "lsa-id": "10.64.0.1",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x8000030a",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "499",
                    "checksum": "0x7271",
                    "lsa-id": "10.64.0.2",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80000305",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "274",
                    "checksum": "0x7248",
                    "lsa-id": "10.64.0.3",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x8000029a",
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "656",
                    "checksum": "0x34eb",
                    "lsa-id": "10.64.0.3",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x800002db",
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "1960",
                    "checksum": "0x31be",
                    "lsa-id": "10.64.0.4",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x800001bb",
                },
                {
                    "advertising-router": "10.100.5.5",
                    "age": "1469",
                    "checksum": "0x4de2",
                    "lsa-id": "10.64.0.6",
                    "lsa-length": "56",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x800019bf",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "2580",
                    "checksum": "0xb9a6",
                    "lsa-id": "10.64.0.7",
                    "lsa-length": "48",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x8000046b",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "1006",
                    "checksum": "0x6a96",
                    "lsa-id": "10.64.0.7",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x800004de",
                },
                {
                    "advertising-router": "10.19.198.239",
                    "age": "622",
                    "checksum": "0xb34a",
                    "lsa-id": "10.64.0.17",
                    "lsa-length": "104",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x8000025d",
                },
                {
                    "advertising-router": "10.169.196.241",
                    "age": "521",
                    "checksum": "0x3e3c",
                    "lsa-id": "10.64.0.17",
                    "lsa-length": "104",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x8000025d",
                },
                {
                    "advertising-router": "10.19.198.239",
                    "age": "622",
                    "checksum": "0xb938",
                    "lsa-id": "10.64.0.18",
                    "lsa-length": "104",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x8000025d",
                },
                {
                    "advertising-router": "10.169.196.241",
                    "age": "521",
                    "checksum": "0x6fdb",
                    "lsa-id": "10.64.0.18",
                    "lsa-length": "104",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x8000025d",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "2542",
                    "checksum": "0xe909",
                    "lsa-id": "10.64.0.31",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x8000029a",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "787",
                    "checksum": "0xe396",
                    "lsa-id": "10.64.0.32",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x800001b5",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "1658",
                    "checksum": "0xffb8",
                    "lsa-id": "10.64.0.37",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x8000029b",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "966",
                    "checksum": "0x71b3",
                    "lsa-id": "10.64.0.38",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x800001b5",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "501",
                    "checksum": "0x7efa",
                    "lsa-id": "10.64.0.52",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "our-entry": True,
                    "sequence-number": "0x80000308",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "1042",
                    "checksum": "0x1839",
                    "lsa-id": "10.64.0.54",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "our-entry": True,
                    "sequence-number": "0x800002dc",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "1876",
                    "checksum": "0x92eb",
                    "lsa-id": "10.64.0.55",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "our-entry": True,
                    "sequence-number": "0x800001bb",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "1087",
                    "checksum": "0x7544",
                    "lsa-id": "10.64.0.57",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x80000303",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "1389",
                    "checksum": "0x6d12",
                    "lsa-id": "10.64.0.59",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x800002f4",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "937",
                    "checksum": "0x4f1a",
                    "lsa-id": "10.64.0.60",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "sequence-number": "0x8000028b",
                },
                {
                    "advertising-router": "10.169.196.241",
                    "age": "35",
                    "checksum": "0xdcd1",
                    "lsa-id": "10.64.8.74",
                    "lsa-length": "92",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x80000030",
                },
                {
                    "advertising-router": "10.169.196.241",
                    "age": "521",
                    "checksum": "0xd4b0",
                    "lsa-id": "10.64.8.75",
                    "lsa-length": "92",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "sequence-number": "0x80000151",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "2323",
                    "checksum": "0x6715",
                    "lsa-id": "0.0.0.0",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "sequence-number": "0x800019e3",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "1991",
                    "checksum": "0x9fcc",
                    "lsa-id": "0.0.0.0",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "sequence-number": "0x8000039e",
                },
                {
                    "advertising-router": "192.168.36.119",
                    "age": "928",
                    "checksum": "0x3bc3",
                    "lsa-id": "10.1.0.0",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x20",
                    "sequence-number": "0x800019b0",
                },
                {
                    "advertising-router": "192.168.36.120",
                    "age": "500",
                    "checksum": "0x33c9",
                    "lsa-id": "10.1.0.0",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x20",
                    "sequence-number": "0x800019b1",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "1841",
                    "checksum": "0xf161",
                    "lsa-id": "10.174.132.237",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "sequence-number": "0x8000039e",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "2443",
                    "checksum": "0x473e",
                    "lsa-id": "10.34.2.250",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "sequence-number": "0x80000288",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "2346",
                    "checksum": "0x2153",
                    "lsa-id": "10.34.2.250",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "sequence-number": "0x80000298",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "184",
                    "checksum": "0x3b48",
                    "lsa-id": "10.34.2.251",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "sequence-number": "0x80000289",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "1176",
                    "checksum": "0x175c",
                    "lsa-id": "10.34.2.251",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "sequence-number": "0x80000298",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "1197",
                    "checksum": "0xf88e",
                    "lsa-id": "10.169.14.240",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "sequence-number": "0x8000029a",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "1884",
                    "checksum": "0x190c",
                    "lsa-id": "10.169.14.240",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "sequence-number": "0x800019e4",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "2143",
                    "checksum": "0xc3fb",
                    "lsa-id": "10.169.14.240",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "our-entry": True,
                    "sequence-number": "0x80001a3a",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "2349",
                    "checksum": "0xb341",
                    "lsa-id": "10.169.14.241",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "sequence-number": "0x80001a14",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "50",
                    "checksum": "0xea9b",
                    "lsa-id": "10.169.14.241",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "sequence-number": "0x80000299",
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "164",
                    "checksum": "0xeb68",
                    "lsa-id": "10.169.14.241",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "sequence-number": "0x80000fae",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "1539",
                    "checksum": "0xc372",
                    "lsa-id": "10.189.5.252",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "sequence-number": "0x800019b0",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "2566",
                    "checksum": "0x6d4",
                    "lsa-id": "10.189.5.253",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "sequence-number": "0x8000140f",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "786",
                    "checksum": "0xfb51",
                    "lsa-id": "192.168.100.0",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "sequence-number": "0x800002da",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "636",
                    "checksum": "0x19b8",
                    "lsa-id": "192.168.100.252",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "sequence-number": "0x800002d9",
                },
            ],
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspfDatabase(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspfDatabase(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowOspfDatabaseSummary(unittest.TestCase):
    """ Unit tests for:
            * show ospf database summary
    """

    device = Device(name="aDevice")
    maxDiff = None
    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
        show ospf database summary
            Area 0.0.0.8:
               12 Router LSAs
               2 Network LSAs
               79 OpaqArea LSAs
            Externals:
               19 Extern LSAs
            Interface ge-0/0/0.0:
            Area 0.0.0.8:
            Interface ge-0/0/1.0:
            Area 0.0.0.8:
            Interface ge-0/0/2.0:
            Area 0.0.0.8:
            Interface ge-0/0/3.0:
            Area 0.0.0.8:
            Interface lo0.0:
            Area 0.0.0.8:
    """
    }

    golden_parsed_output = {
        "ospf-database-information": {
            "ospf-database-summary": [
                {
                    "ospf-area": "0.0.0.8",
                    "ospf-lsa-count": ["12", "2", "79"],
                    "ospf-lsa-type": ["Router", "Network", "OpaqArea"],
                },
                {
                    "@external-heading": "Externals",
                    "ospf-lsa-count": "19",
                    "ospf-lsa-type": "Extern",
                },
                {
                    "ospf-area": [
                        "0.0.0.8",
                        "0.0.0.8",
                        "0.0.0.8",
                        "0.0.0.8",
                        "0.0.0.8",
                    ],
                    "ospf-intf": [
                        "ge-0/0/0.0",
                        "ge-0/0/1.0",
                        "ge-0/0/2.0",
                        "ge-0/0/3.0",
                        "lo0.0",
                    ],
                },
            ]
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspfDatabaseSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspfDatabaseSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowOspfDatabaseExternalExtensive(unittest.TestCase):
    """ Unit tests for:
            * show ospf database external extensive
    """

    device = Device(name="aDevice")
    maxDiff = None
    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
        show ospf database external extensive
            OSPF AS SCOPE link state database
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
        Extern   0.0.0.0          10.34.2.251     0x800019e3  2728  0x22 0x6715  36
        mask 0.0.0.0
        Topology default (ID 0)
            Type: 1, Metric: 1, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
        Aging timer 00:14:32
        Installed 00:45:19 ago, expires in 00:14:32, sent 00:45:17 ago
        Last changed 30w0d 01:34:30 ago, Change count: 1
        Extern   0.0.0.0          10.169.14.240   0x8000039e  2396  0x22 0x9fcc  36
        mask 0.0.0.0
        Topology default (ID 0)
            Type: 1, Metric: 1, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
        Aging timer 00:20:03
        Installed 00:39:53 ago, expires in 00:20:04, sent 00:39:51 ago
        Last changed 4w2d 05:48:46 ago, Change count: 1
        Extern   10.1.0.0          192.168.36.119  0x800019b0  1333  0x20 0x3bc3  36
        mask 255.255.255.0
        Topology default (ID 0)
            Type: 2, Metric: 20, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
        Aging timer 00:37:47
        Installed 00:22:09 ago, expires in 00:37:47, sent 00:22:07 ago
        Last changed 21w6d 00:06:09 ago, Change count: 1
        Extern   10.1.0.0          192.168.36.120  0x800019b1   905  0x20 0x33c9  36
        mask 255.255.255.0
        Topology default (ID 0)
            Type: 2, Metric: 20, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
        Aging timer 00:44:55
        Installed 00:15:01 ago, expires in 00:44:55, sent 00:14:59 ago
        Last changed 21w6d 00:06:37 ago, Change count: 1
        Extern   10.174.132.237    10.169.14.240   0x8000039e  2246  0x22 0xf161  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
        Aging timer 00:22:34
        Installed 00:37:23 ago, expires in 00:22:34, sent 00:37:21 ago
        Last changed 4w2d 05:48:43 ago, Change count: 1
        Extern   10.34.2.250     10.169.14.240   0x80000288  2848  0x22 0x473e  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 10.166.34.12
        Aging timer 00:12:32
        Installed 00:47:25 ago, expires in 00:12:32, sent 00:47:23 ago
        Last changed 3w0d 08:51:45 ago, Change count: 1
        Extern   10.34.2.250     10.169.14.241   0x80000298  2751  0x22 0x2153  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 10.166.34.12
        Aging timer 00:14:09
        Installed 00:45:45 ago, expires in 00:14:09, sent 00:45:43 ago
        Last changed 3w0d 08:11:45 ago, Change count: 1
        Extern   10.34.2.251     10.169.14.240   0x80000289   589  0x22 0x3b48  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 10.166.34.12
        Aging timer 00:50:11
        Installed 00:09:46 ago, expires in 00:50:11, sent 00:09:44 ago
        Last changed 3w0d 08:51:50 ago, Change count: 1
        Extern   10.34.2.251     10.169.14.241   0x80000298  1581  0x22 0x175c  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 10.166.34.12
        Aging timer 00:33:38
        Installed 00:26:15 ago, expires in 00:33:39, sent 00:26:13 ago
        Last changed 3w0d 08:11:40 ago, Change count: 1
        Extern   10.169.14.240   10.34.2.250     0x8000029a  1602  0x22 0xf88e  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
        Aging timer 00:33:18
        Installed 00:26:36 ago, expires in 00:33:18, sent 00:26:34 ago
        Last changed 3w0d 08:51:43 ago, Change count: 1
        Extern   10.169.14.240   10.34.2.251     0x800019e4  2289  0x22 0x190c  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
        Aging timer 00:21:51
        Installed 00:38:00 ago, expires in 00:21:51, sent 00:37:59 ago
        Last changed 30w0d 01:34:30 ago, Change count: 1
        Extern  *10.169.14.240   10.189.5.252     0x80001a3a  2548  0x22 0xc3fb  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
        Gen timer 00:02:55
        Aging timer 00:17:31
        Installed 00:42:28 ago, expires in 00:17:32, sent 00:42:26 ago
        Last changed 3w3d 07:34:17 ago, Change count: 25, Ours
        Extern   10.169.14.241   10.34.2.250     0x80001a14  2754  0x22 0xb341  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
        Aging timer 00:14:05
        Installed 00:45:48 ago, expires in 00:14:06, sent 00:45:46 ago
        Last changed 30w0d 01:05:04 ago, Change count: 1
        Extern   10.169.14.241   10.34.2.251     0x80000299   455  0x22 0xea9b  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
        Aging timer 00:52:25
        Installed 00:07:27 ago, expires in 00:52:25, sent 00:07:25 ago
        Last changed 3w0d 08:11:38 ago, Change count: 1
        Extern   10.169.14.241   10.189.5.253     0x80000fae   569  0x22 0xeb68  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
        Aging timer 00:50:31
        Installed 00:09:26 ago, expires in 00:50:31, sent 00:09:24 ago
        Last changed 3w3d 07:33:47 ago, Change count: 31
        Extern   10.189.5.252     10.169.14.240   0x800019b0  1944  0x22 0xc372  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 10.166.34.12
        Aging timer 00:27:35
        Installed 00:32:21 ago, expires in 00:27:36, sent 00:32:19 ago
        Last changed 3w3d 07:33:50 ago, Change count: 3
        Extern   10.189.5.253     10.169.14.241   0x80001410   227  0x22 0x4d5   36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 10.166.34.12
        Aging timer 00:56:12
        Installed 00:03:41 ago, expires in 00:56:13, sent 00:03:39 ago
        Last changed 3w3d 07:24:57 ago, Change count: 17
        Extern   192.168.100.0    10.169.14.240   0x800002da  1191  0x22 0xfb51  36
        mask 255.255.255.128
        Topology default (ID 0)
            Type: 1, Metric: 31900, Fwd addr: 0.0.0.0, Tag: 10.76.212.52
        Aging timer 00:40:08
        Installed 00:19:48 ago, expires in 00:40:09, sent 00:19:46 ago
        Last changed 2w6d 19:00:07 ago, Change count: 75
        Extern   192.168.100.252  10.169.14.240   0x800002d9  1041  0x22 0x19b8  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 31900, Fwd addr: 0.0.0.0, Tag: 10.76.212.52
        Aging timer 00:42:39
        Installed 00:17:18 ago, expires in 00:42:39, sent 00:17:16 ago
        Last changed 2w6d 19:00:07 ago, Change count: 75
    """
    }

    golden_parsed_output = {
        "ospf-database-information": {
            "ospf-database": [
                {
                    "@external-heading": "OSPF AS SCOPE link state database",
                    "@heading": "Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len",
                    "advertising-router": "10.34.2.251",
                    "age": "2728",
                    "checksum": "0x6715",
                    "lsa-id": "0.0.0.0",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:14:32"},
                        "expiration-time": {"#text": "00:14:32"},
                        "installation-time": {"#text": "00:45:19"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "30w0d 01:34:30"},
                        "send-time": {"#text": "00:45:17"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "0.0.0.0",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "1",
                            "ospf-topology-name": "default",
                            "tag": "0.0.0.0",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x800019e3",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "2396",
                    "checksum": "0x9fcc",
                    "lsa-id": "0.0.0.0",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:20:03"},
                        "expiration-time": {"#text": "00:20:04"},
                        "installation-time": {"#text": "00:39:53"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "4w2d 05:48:46"},
                        "send-time": {"#text": "00:39:51"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "0.0.0.0",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "1",
                            "ospf-topology-name": "default",
                            "tag": "0.0.0.0",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x8000039e",
                },
                {
                    "advertising-router": "192.168.36.119",
                    "age": "1333",
                    "checksum": "0x3bc3",
                    "lsa-id": "10.1.0.0",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x20",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:37:47"},
                        "expiration-time": {"#text": "00:37:47"},
                        "installation-time": {"#text": "00:22:09"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "21w6d 00:06:09"},
                        "send-time": {"#text": "00:22:07"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.0",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "20",
                            "ospf-topology-name": "default",
                            "tag": "0.0.0.0",
                            "type-value": "2",
                        },
                    },
                    "sequence-number": "0x800019b0",
                },
                {
                    "advertising-router": "192.168.36.120",
                    "age": "905",
                    "checksum": "0x33c9",
                    "lsa-id": "10.1.0.0",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x20",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:44:55"},
                        "expiration-time": {"#text": "00:44:55"},
                        "installation-time": {"#text": "00:15:01"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "21w6d 00:06:37"},
                        "send-time": {"#text": "00:14:59"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.0",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "20",
                            "ospf-topology-name": "default",
                            "tag": "0.0.0.0",
                            "type-value": "2",
                        },
                    },
                    "sequence-number": "0x800019b1",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "2246",
                    "checksum": "0xf161",
                    "lsa-id": "10.174.132.237",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:22:34"},
                        "expiration-time": {"#text": "00:22:34"},
                        "installation-time": {"#text": "00:37:23"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "4w2d 05:48:43"},
                        "send-time": {"#text": "00:37:21"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "50",
                            "ospf-topology-name": "default",
                            "tag": "0.0.0.0",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x8000039e",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "2848",
                    "checksum": "0x473e",
                    "lsa-id": "10.34.2.250",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:12:32"},
                        "expiration-time": {"#text": "00:12:32"},
                        "installation-time": {"#text": "00:47:25"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "3w0d 08:51:45"},
                        "send-time": {"#text": "00:47:23"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "50",
                            "ospf-topology-name": "default",
                            "tag": "10.166.34.12",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x80000288",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "2751",
                    "checksum": "0x2153",
                    "lsa-id": "10.34.2.250",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:14:09"},
                        "expiration-time": {"#text": "00:14:09"},
                        "installation-time": {"#text": "00:45:45"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "3w0d 08:11:45"},
                        "send-time": {"#text": "00:45:43"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "50",
                            "ospf-topology-name": "default",
                            "tag": "10.166.34.12",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x80000298",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "589",
                    "checksum": "0x3b48",
                    "lsa-id": "10.34.2.251",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:50:11"},
                        "expiration-time": {"#text": "00:50:11"},
                        "installation-time": {"#text": "00:09:46"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "3w0d 08:51:50"},
                        "send-time": {"#text": "00:09:44"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "50",
                            "ospf-topology-name": "default",
                            "tag": "10.166.34.12",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x80000289",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "1581",
                    "checksum": "0x175c",
                    "lsa-id": "10.34.2.251",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:33:38"},
                        "expiration-time": {"#text": "00:33:39"},
                        "installation-time": {"#text": "00:26:15"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "3w0d 08:11:40"},
                        "send-time": {"#text": "00:26:13"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "50",
                            "ospf-topology-name": "default",
                            "tag": "10.166.34.12",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x80000298",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "1602",
                    "checksum": "0xf88e",
                    "lsa-id": "10.169.14.240",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:33:18"},
                        "expiration-time": {"#text": "00:33:18"},
                        "installation-time": {"#text": "00:26:36"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "3w0d 08:51:43"},
                        "send-time": {"#text": "00:26:34"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "50",
                            "ospf-topology-name": "default",
                            "tag": "0.0.0.0",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x8000029a",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "2289",
                    "checksum": "0x190c",
                    "lsa-id": "10.169.14.240",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:21:51"},
                        "expiration-time": {"#text": "00:21:51"},
                        "installation-time": {"#text": "00:38:00"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "30w0d 01:34:30"},
                        "send-time": {"#text": "00:37:59"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "50",
                            "ospf-topology-name": "default",
                            "tag": "0.0.0.0",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x800019e4",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "2754",
                    "checksum": "0xb341",
                    "lsa-id": "10.169.14.241",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:14:05"},
                        "expiration-time": {"#text": "00:14:06"},
                        "installation-time": {"#text": "00:45:48"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "30w0d 01:05:04"},
                        "send-time": {"#text": "00:45:46"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "50",
                            "ospf-topology-name": "default",
                            "tag": "0.0.0.0",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x80001a14",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "455",
                    "checksum": "0xea9b",
                    "lsa-id": "10.169.14.241",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:52:25"},
                        "expiration-time": {"#text": "00:52:25"},
                        "installation-time": {"#text": "00:07:27"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "3w0d 08:11:38"},
                        "send-time": {"#text": "00:07:25"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "50",
                            "ospf-topology-name": "default",
                            "tag": "0.0.0.0",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x80000299",
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "569",
                    "checksum": "0xeb68",
                    "lsa-id": "10.169.14.241",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:50:31"},
                        "expiration-time": {"#text": "00:50:31"},
                        "installation-time": {"#text": "00:09:26"},
                        "lsa-change-count": "31",
                        "lsa-changed-time": {"#text": "3w3d 07:33:47"},
                        "send-time": {"#text": "00:09:24"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "50",
                            "ospf-topology-name": "default",
                            "tag": "0.0.0.0",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x80000fae",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "1944",
                    "checksum": "0xc372",
                    "lsa-id": "10.189.5.252",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:27:35"},
                        "expiration-time": {"#text": "00:27:36"},
                        "installation-time": {"#text": "00:32:21"},
                        "lsa-change-count": "3",
                        "lsa-changed-time": {"#text": "3w3d 07:33:50"},
                        "send-time": {"#text": "00:32:19"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "50",
                            "ospf-topology-name": "default",
                            "tag": "10.166.34.12",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x800019b0",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "227",
                    "checksum": "0x4d5",
                    "lsa-id": "10.189.5.253",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:56:12"},
                        "expiration-time": {"#text": "00:56:13"},
                        "installation-time": {"#text": "00:03:41"},
                        "lsa-change-count": "17",
                        "lsa-changed-time": {"#text": "3w3d 07:24:57"},
                        "send-time": {"#text": "00:03:39"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "50",
                            "ospf-topology-name": "default",
                            "tag": "10.166.34.12",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x80001410",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "1191",
                    "checksum": "0xfb51",
                    "lsa-id": "192.168.100.0",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:40:08"},
                        "expiration-time": {"#text": "00:40:09"},
                        "installation-time": {"#text": "00:19:48"},
                        "lsa-change-count": "75",
                        "lsa-changed-time": {"#text": "2w6d 19:00:07"},
                        "send-time": {"#text": "00:19:46"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.128",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "31900",
                            "ospf-topology-name": "default",
                            "tag": "10.76.212.52",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x800002da",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "1041",
                    "checksum": "0x19b8",
                    "lsa-id": "192.168.100.252",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:42:39"},
                        "expiration-time": {"#text": "00:42:39"},
                        "installation-time": {"#text": "00:17:18"},
                        "lsa-change-count": "75",
                        "lsa-changed-time": {"#text": "2w6d 19:00:07"},
                        "send-time": {"#text": "00:17:16"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "31900",
                            "ospf-topology-name": "default",
                            "tag": "10.76.212.52",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x800002d9",
                },
            ]
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspfDatabaseExternalExtensive(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspfDatabaseExternalExtensive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowOspfOverview(unittest.TestCase):
    """ Unit tests for:
            * show ospf overview
    """

    device = Device(name="aDevice")
    maxDiff = None

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
        show ospf overview
        Instance: master
            Router ID: 10.189.5.252
            Route table index: 0
            Configured overload, expires in 14 seconds
            AS boundary router
            LSA refresh time: 50 minutes
            Traffic engineering
            SPRING: Enabled
                SRGB Config Range :
                SRGB Start-Label : 16000, SRGB Index-Range : 8000
                SRGB Block Allocation: Success
                SRGB Start Index : 16000, SRGB Size : 8000, Label-Range: [ 16000, 23999 ]
                Node Segments: Enabled
                Ipv4 Index : 71
            Post Convergence Backup: Enabled
                Max labels: 3, Max spf: 100, Max Ecmp Backup: 1
            Area: 0.0.0.8
                Stub type: Not Stub
                Authentication Type: None
                Area border routers: 0, AS boundary routers: 7
                Neighbors
                Up (in full state): 3
            Topology: default (ID 0)
                Prefix export count: 1
                Full SPF runs: 173416
                SPF delay: 0.200000 sec, SPF holddown: 2 sec, SPF rapid runs: 3
                Backup SPF: Not Needed
    """
    }

    golden_parsed_output = {
        "ospf-overview-information": {
            "ospf-overview": {
                "instance-name": "master",
                "ospf-area-overview": {
                    "authentication-type": "None",
                    "ospf-abr-count": "0",
                    "ospf-area": "0.0.0.8",
                    "ospf-asbr-count": "7",
                    "ospf-nbr-overview": {"ospf-nbr-up-count": "3"},
                    "ospf-stub-type": "Not Stub",
                },
                "ospf-lsa-refresh-time": "50",
                "ospf-route-table-index": "0",
                'ospf-configured-overload-remaining-time': '14',
                "ospf-router-id": "10.189.5.252",
                "ospf-spring-overview": {
                    "ospf-node-segment": {"ospf-node-segment-ipv4-index": "71"},
                    "ospf-node-segment-enabled": "Enabled",
                    "ospf-spring-enabled": "Enabled",
                    "ospf-srgb-allocation": "Success",
                    "ospf-srgb-block": {
                        "ospf-srgb-first-label": "16000",
                        "ospf-srgb-last-label": "23999",
                        "ospf-srgb-size": "8000",
                        "ospf-srgb-start-index": "16000",
                    },
                    "ospf-srgb-config": {
                        "ospf-srgb-config-block-header": "SRGB Config Range",
                        "ospf-srgb-index-range": "8000",
                        "ospf-srgb-start-label": "16000",
                    },
                },
                "ospf-tilfa-overview": {
                    "ospf-tilfa-ecmp-backup": "1",
                    "ospf-tilfa-enabled": "Enabled",
                    "ospf-tilfa-max-labels": "3",
                    "ospf-tilfa-max-spf": "100",
                },
                "ospf-topology-overview": {
                    "ospf-backup-spf-status": "Not Needed",
                    "ospf-full-spf-count": "173416",
                    "ospf-prefix-export-count": "1",
                    "ospf-spf-delay": "0.200000",
                    "ospf-spf-holddown": "2",
                    "ospf-spf-rapid-runs": "3",
                    "ospf-topology-id": "0",
                    "ospf-topology-name": "default",
                },
            }
        }
    }

    golden_output2 = {
        "execute.return_value": """
            show ospf overview

            Instance: master

            Router ID: 10.1.0.102

            Route table index: 0

            LSA refresh time: 50 minutes

            Post Convergence Backup: Disabled

            Area: 0.0.0.0

                Stub type: Not Stub

                Authentication Type: None

                Area border routers: 0, AS boundary routers: 0

                Neighbors

                Up (in full state): 0

            Topology: default (ID 0)

                Prefix export count: 0

                Full SPF runs: 2

                SPF delay: 0.200000 sec, SPF holddown: 5 sec, SPF rapid runs: 3

                Backup SPF: Not Needed
        """
    }

    golden_parsed_output2 = {
        "ospf-overview-information": {
            "ospf-overview": {
                "instance-name": "master",
                "ospf-area-overview": {
                    "authentication-type": "None",
                    "ospf-abr-count": "0",
                    "ospf-area": "0.0.0.0",
                    "ospf-asbr-count": "0",
                    "ospf-nbr-overview": {"ospf-nbr-up-count": "0"},
                    "ospf-stub-type": "Not Stub",
                },
                "ospf-lsa-refresh-time": "50",
                "ospf-route-table-index": "0",
                "ospf-router-id": "10.1.0.102",
                "ospf-topology-overview": {
                    "ospf-backup-spf-status": "Not Needed",
                    "ospf-full-spf-count": "2",
                    "ospf-prefix-export-count": "0",
                    "ospf-spf-delay": "0.200000",
                    "ospf-spf-holddown": "5",
                    "ospf-spf-rapid-runs": "3",
                    "ospf-topology-id": "0",
                    "ospf-topology-name": "default",
                },
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspfOverview(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspfOverview(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden2(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowOspfOverview(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)


class TestShowOspfOverviewExtensive(unittest.TestCase):
    """ Unit tests for:
            * show ospf overview extensive
    """

    device = Device(name="aDevice")
    maxDiff = None

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
        show ospf overview extensive
        Instance: master
            Router ID: 10.189.5.252
            Route table index: 0
            AS boundary router
            LSA refresh time: 50 minutes
            Traffic engineering
            SPRING: Enabled
                SRGB Config Range :
                SRGB Start-Label : 16000, SRGB Index-Range : 8000
                SRGB Block Allocation: Success
                SRGB Start Index : 16000, SRGB Size : 8000, Label-Range: [ 16000, 23999 ]
                Node Segments: Enabled
                Ipv4 Index : 71
            Post Convergence Backup: Enabled
                Max labels: 3, Max spf: 100, Max Ecmp Backup: 1
            Area: 0.0.0.8
                Stub type: Not Stub
                Authentication Type: None
                Area border routers: 0, AS boundary routers: 7
                Neighbors
                Up (in full state): 3
            Topology: default (ID 0)
                Prefix export count: 1
                Full SPF runs: 173416
                SPF delay: 0.200000 sec, SPF holddown: 2 sec, SPF rapid runs: 3
                Backup SPF: Not Needed
    """
    }

    golden_parsed_output = {
        "ospf-overview-information": {
            "ospf-overview": {
                "instance-name": "master",
                "ospf-area-overview": {
                    "authentication-type": "None",
                    "ospf-abr-count": "0",
                    "ospf-area": "0.0.0.8",
                    "ospf-asbr-count": "7",
                    "ospf-nbr-overview": {"ospf-nbr-up-count": "3"},
                    "ospf-stub-type": "Not Stub",
                },
                "ospf-lsa-refresh-time": "50",
                "ospf-route-table-index": "0",
                "ospf-router-id": "10.189.5.252",
                "ospf-spring-overview": {
                    "ospf-node-segment": {"ospf-node-segment-ipv4-index": "71"},
                    "ospf-node-segment-enabled": "Enabled",
                    "ospf-spring-enabled": "Enabled",
                    "ospf-srgb-allocation": "Success",
                    "ospf-srgb-block": {
                        "ospf-srgb-first-label": "16000",
                        "ospf-srgb-last-label": "23999",
                        "ospf-srgb-size": "8000",
                        "ospf-srgb-start-index": "16000",
                    },
                    "ospf-srgb-config": {
                        "ospf-srgb-config-block-header": "SRGB Config Range",
                        "ospf-srgb-index-range": "8000",
                        "ospf-srgb-start-label": "16000",
                    },
                },
                "ospf-tilfa-overview": {
                    "ospf-tilfa-ecmp-backup": "1",
                    "ospf-tilfa-enabled": "Enabled",
                    "ospf-tilfa-max-labels": "3",
                    "ospf-tilfa-max-spf": "100",
                },
                "ospf-topology-overview": {
                    "ospf-backup-spf-status": "Not Needed",
                    "ospf-full-spf-count": "173416",
                    "ospf-prefix-export-count": "1",
                    "ospf-spf-delay": "0.200000",
                    "ospf-spf-holddown": "2",
                    "ospf-spf-rapid-runs": "3",
                    "ospf-topology-id": "0",
                    "ospf-topology-name": "default",
                },
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspfOverviewExtensive(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspfOverviewExtensive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowOspfDatabaseAdvertisingRouterSelfDetail(unittest.TestCase):

    maxDiff = None

    device = Device(name="test-device")

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
            show ospf database advertising-router self detail

            OSPF database, Area 0.0.0.8
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
        Router  *10.189.5.252     10.189.5.252     0x80001b9e  1801  0x22 0x1e2  120
        bits 0x2, link count 8
        id 10.189.5.253, data 10.189.5.93, Type PointToPoint (1)
            Topology count: 0, Default metric: 5
        id 10.189.5.92, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 5
        id 10.169.14.240, data 10.169.14.122, Type PointToPoint (1)
            Topology count: 0, Default metric: 100
        id 10.169.14.120, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 100
        id 10.19.198.239, data 10.19.198.25, Type PointToPoint (1)
            Topology count: 0, Default metric: 1000
        id 10.19.198.24, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 1000
        id 10.55.0.0, data 255.255.255.0, Type Stub (3)
            Topology count: 0, Default metric: 100
        id 10.189.5.252, data 255.255.255.255, Type Stub (3)
            Topology count: 0, Default metric: 0
        Topology default (ID 0)
            Type: PointToPoint, Node ID: 10.19.198.239
            Metric: 1000, Bidirectional
            Type: PointToPoint, Node ID: 10.169.14.240
            Metric: 100, Bidirectional
            Type: PointToPoint, Node ID: 10.189.5.253
            Metric: 5, Bidirectional
        OpaqArea*10.1.0.1          10.189.5.252     0x80001a15   424  0x22 0xd49a  28
        Opaque LSA
        RtrAddr (1), length 4:
            10.189.5.252
        OpaqArea*10.1.0.3          10.189.5.252     0x80000322   153  0x22 0x95cd 136
        Opaque LSA
        Link (2), length 112:
            Linktype (1), length 1:
            1
            LinkID (2), length 4:
            10.189.5.253
            LocIfAdr (3), length 4:
            10.189.5.93
            RemIfAdr (4), length 4:
            10.189.5.94
            TEMetric (5), length 4:
            5
            MaxBW (6), length 4:
            1000Mbps
            MaxRsvBW (7), length 4:
            1000Mbps
            UnRsvBW (8), length 32:
                Priority 0, 1000Mbps
                Priority 1, 1000Mbps
                Priority 2, 1000Mbps
                Priority 3, 1000Mbps
                Priority 4, 1000Mbps
                Priority 5, 1000Mbps
                Priority 6, 1000Mbps
                Priority 7, 1000Mbps
            LinkLocalRemoteIdentifier (11), length 8:
            Local 333, Remote 0
            Color (9), length 4:
            0
        OpaqArea*10.1.0.4          10.189.5.252     0x800013e8  2604  0x22 0xb804 136
        Opaque LSA
        Link (2), length 112:
            Linktype (1), length 1:
            1
            LinkID (2), length 4:
            10.169.14.240
            LocIfAdr (3), length 4:
            10.169.14.122
            RemIfAdr (4), length 4:
            10.169.14.121
            TEMetric (5), length 4:
            100
            MaxBW (6), length 4:
            1000Mbps
            MaxRsvBW (7), length 4:
            1000Mbps
            UnRsvBW (8), length 32:
                Priority 0, 1000Mbps
                Priority 1, 1000Mbps
                Priority 2, 1000Mbps
                Priority 3, 1000Mbps
                Priority 4, 1000Mbps
                Priority 5, 1000Mbps
                Priority 6, 1000Mbps
                Priority 7, 1000Mbps
            LinkLocalRemoteIdentifier (11), length 8:
            Local 334, Remote 0
            Color (9), length 4:
            10
        OpaqArea*10.1.0.5          10.189.5.252     0x800001bb  1505  0x22 0x79b5 136
        Opaque LSA
        Link (2), length 112:
            Linktype (1), length 1:
            1
            LinkID (2), length 4:
            10.19.198.239
            LocIfAdr (3), length 4:
            10.19.198.25
            RemIfAdr (4), length 4:
            10.19.198.26
            TEMetric (5), length 4:
            1000
            MaxBW (6), length 4:
            1000Mbps
            MaxRsvBW (7), length 4:
            1000Mbps
            UnRsvBW (8), length 32:
                Priority 0, 1000Mbps
                Priority 1, 1000Mbps
                Priority 2, 1000Mbps
                Priority 3, 1000Mbps
                Priority 4, 1000Mbps
                Priority 5, 1000Mbps
                Priority 6, 1000Mbps
                Priority 7, 1000Mbps
            LinkLocalRemoteIdentifier (11), length 8:
            Local 336, Remote 0
            Color (9), length 4:
            2
        OpaqArea*10.16.0.0          10.189.5.252     0x80001a2a   964  0x22 0xe5ef  44
        Opaque LSA
        SR-Algorithm (8), length 1:
            Algo (1), length 1:
                0
        SID/Label Range (9), length 12:
            Range Size (1), length 3:
                8000
            SID/Label (1), length 3:
            Label (1), length 3:
                16000
        OpaqArea*10.49.0.1          10.189.5.252     0x80001b9e  1801  0x22 0x8c7f  44
        Opaque LSA
        Extended Prefix (1), length 20:
            Route Type (1), length 1:
                1
            Prefix Length (2), length 1:
                32
            AF (3), length 1:
                0
            Flags (4),  length 1:
                0x40
            Prefix (5), length 32:
                10.189.5.252
            Prefix Sid (2), length 8:
            Flags (1), length 1:
                0x00
            MT ID (2), length 1:
                0
            Algorithm (3), length 1:
                0
            SID (4), length 4:
                71
        OpaqArea*10.64.0.52         10.189.5.252     0x80000308   694  0x22 0x7efa  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.169.14.240
            Link Data (3), length 4:
            10.169.14.122
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                2567
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                2568
        OpaqArea*10.64.0.54         10.189.5.252     0x800002dc  1235  0x22 0x1839  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.189.5.253
            Link Data (3), length 4:
            10.189.5.93
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                28985
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                28986
        OpaqArea*10.64.0.55         10.189.5.252     0x800001bb  2069  0x22 0x92eb  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.19.198.239
            Link Data (3), length 4:
            10.19.198.25
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                167966
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                167967
            OSPF AS SCOPE link state database
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
        Extern  *10.169.14.240   10.189.5.252     0x80001a3a  2336  0x22 0xc3fb  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 0.0.0.0

    """
    }

    golden_parsed_output = {
        "ospf-database-information": {
            "ospf-area-header": {"ospf-area": "0.0.0.8"},
            "ospf-database": [
                {
                    "advertising-router": "10.189.5.252",
                    "age": "1801",
                    "checksum": "0x1e2",
                    "lsa-id": "10.189.5.252",
                    "lsa-length": "120",
                    "lsa-type": "Router",
                    "options": "0x22",
                    "ospf-router-lsa": {
                        "bits": "0x2",
                        "link-count": "8",
                        "ospf-link": [
                            {
                                "link-data": "10.189.5.93",
                                "link-id": "10.189.5.253",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "5",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.189.5.93",
                                "link-id": "10.189.5.253",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "5",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.189.5.92",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "5",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.189.5.92",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "5",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.169.14.122",
                                "link-id": "10.169.14.240",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "100",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.169.14.122",
                                "link-id": "10.169.14.240",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "100",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.169.14.120",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "100",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.169.14.120",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "100",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.19.198.25",
                                "link-id": "10.19.198.239",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.19.198.25",
                                "link-id": "10.19.198.239",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.19.198.24",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.19.198.24",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.0",
                                "link-id": "10.55.0.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "100",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.0",
                                "link-id": "10.55.0.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "100",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "10.189.5.252",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "0",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "10.189.5.252",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "0",
                                "ospf-topology-count": "0",
                            },
                        ],
                        "ospf-lsa-topology": {
                            "ospf-lsa-topology-link": [
                                {
                                    "link-type-name": "PointToPoint",
                                    "ospf-lsa-topology-link-metric": "1000",
                                    "ospf-lsa-topology-link-node-id": "10.19.198.239",
                                    "ospf-lsa-topology-link-state": "Bidirectional",
                                },
                                {
                                    "link-type-name": "PointToPoint",
                                    "ospf-lsa-topology-link-metric": "100",
                                    "ospf-lsa-topology-link-node-id": "10.169.14.240",
                                    "ospf-lsa-topology-link-state": "Bidirectional",
                                },
                                {
                                    "link-type-name": "PointToPoint",
                                    "ospf-lsa-topology-link-metric": "5",
                                    "ospf-lsa-topology-link-node-id": "10.189.5.253",
                                    "ospf-lsa-topology-link-state": "Bidirectional",
                                },
                            ],
                            "ospf-topology-id": "0",
                            "ospf-topology-name": "default",
                        },
                    },
                    "our-entry": True,
                    "sequence-number": "0x80001b9e",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "424",
                    "checksum": "0xd49a",
                    "lsa-id": "10.1.0.1",
                    "lsa-length": "28",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "tlv-block": {
                            "formatted-tlv-data": "10.189.5.252",
                            "tlv-length": "4",
                            "tlv-type-name": "RtrAddr",
                            "tlv-type-value": "1",
                        }
                    },
                    "our-entry": True,
                    "sequence-number": "0x80001a15",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "153",
                    "checksum": "0x95cd",
                    "lsa-id": "10.1.0.3",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.189.5.253",
                                "10.189.5.93",
                                "10.189.5.94",
                                "5",
                                "1000Mbps",
                                "1000Mbps",
                                "Priority "
                                "0, "
                                "1000Mbps\n"
                                "Priority "
                                "1, "
                                "1000Mbps\n"
                                "Priority "
                                "2, "
                                "1000Mbps\n"
                                "Priority "
                                "3, "
                                "1000Mbps\n"
                                "Priority "
                                "4, "
                                "1000Mbps\n"
                                "Priority "
                                "5, "
                                "1000Mbps\n"
                                "Priority "
                                "6, "
                                "1000Mbps\n"
                                "Priority "
                                "7, "
                                "1000Mbps\n",
                                "Local 333, Remote 0",
                                "0",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "32",
                                "8",
                                "4",
                            ],
                            "tlv-type-name": [
                                "Linktype",
                                "LinkID",
                                "LocIfAdr",
                                "RemIfAdr",
                                "TEMetric",
                                "MaxBW",
                                "MaxRsvBW",
                                "UnRsvBW",
                                "LinkLocalRemoteIdentifier",
                                "Color",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "6",
                                "7",
                                "8",
                                "11",
                                "9",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "112",
                            "tlv-type-name": "Link",
                            "tlv-type-value": "2",
                        },
                    },
                    "our-entry": True,
                    "sequence-number": "0x80000322",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "2604",
                    "checksum": "0xb804",
                    "lsa-id": "10.1.0.4",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.169.14.240",
                                "10.169.14.122",
                                "10.169.14.121",
                                "100",
                                "1000Mbps",
                                "1000Mbps",
                                "Priority "
                                "0, "
                                "1000Mbps\n"
                                "Priority "
                                "1, "
                                "1000Mbps\n"
                                "Priority "
                                "2, "
                                "1000Mbps\n"
                                "Priority "
                                "3, "
                                "1000Mbps\n"
                                "Priority "
                                "4, "
                                "1000Mbps\n"
                                "Priority "
                                "5, "
                                "1000Mbps\n"
                                "Priority "
                                "6, "
                                "1000Mbps\n"
                                "Priority "
                                "7, "
                                "1000Mbps\n",
                                "Local 334, Remote 0",
                                "10",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "32",
                                "8",
                                "4",
                            ],
                            "tlv-type-name": [
                                "Linktype",
                                "LinkID",
                                "LocIfAdr",
                                "RemIfAdr",
                                "TEMetric",
                                "MaxBW",
                                "MaxRsvBW",
                                "UnRsvBW",
                                "LinkLocalRemoteIdentifier",
                                "Color",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "6",
                                "7",
                                "8",
                                "11",
                                "9",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "112",
                            "tlv-type-name": "Link",
                            "tlv-type-value": "2",
                        },
                    },
                    "our-entry": True,
                    "sequence-number": "0x800013e8",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "1505",
                    "checksum": "0x79b5",
                    "lsa-id": "10.1.0.5",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.19.198.239",
                                "10.19.198.25",
                                "10.19.198.26",
                                "1000",
                                "1000Mbps",
                                "1000Mbps",
                                "Priority "
                                "0, "
                                "1000Mbps\n"
                                "Priority "
                                "1, "
                                "1000Mbps\n"
                                "Priority "
                                "2, "
                                "1000Mbps\n"
                                "Priority "
                                "3, "
                                "1000Mbps\n"
                                "Priority "
                                "4, "
                                "1000Mbps\n"
                                "Priority "
                                "5, "
                                "1000Mbps\n"
                                "Priority "
                                "6, "
                                "1000Mbps\n"
                                "Priority "
                                "7, "
                                "1000Mbps\n",
                                "Local 336, Remote 0",
                                "2",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "32",
                                "8",
                                "4",
                            ],
                            "tlv-type-name": [
                                "Linktype",
                                "LinkID",
                                "LocIfAdr",
                                "RemIfAdr",
                                "TEMetric",
                                "MaxBW",
                                "MaxRsvBW",
                                "UnRsvBW",
                                "LinkLocalRemoteIdentifier",
                                "Color",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "6",
                                "7",
                                "8",
                                "11",
                                "9",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "112",
                            "tlv-type-name": "Link",
                            "tlv-type-value": "2",
                        },
                    },
                    "our-entry": True,
                    "sequence-number": "0x800001bb",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "964",
                    "checksum": "0xe5ef",
                    "lsa-id": "10.16.0.0",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": ["0", "8000", "16000"],
                            "tlv-length": ["1", "12", "3", "3", "3"],
                            "tlv-type-name": [
                                "Algo",
                                "SID/Label Range",
                                "Range Size",
                                "SID/Label",
                                "Label",
                            ],
                            "tlv-type-value": ["1", "9", "1", "1", "1"],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "1",
                            "tlv-type-name": "SR-Algorithm",
                            "tlv-type-value": "8",
                        },
                    },
                    "our-entry": True,
                    "sequence-number": "0x80001a2a",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "1801",
                    "checksum": "0x8c7f",
                    "lsa-id": "10.49.0.1",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "32",
                                "0",
                                "0x40",
                                "10.189.5.252",
                                "0x00",
                                "0",
                                "0",
                                "71",
                            ],
                            "tlv-length": [
                                "1",
                                "1",
                                "1",
                                "1",
                                "32",
                                "8",
                                "1",
                                "1",
                                "1",
                                "4",
                            ],
                            "tlv-type-name": [
                                "Route Type",
                                "Prefix Length",
                                "AF",
                                "Flags",
                                "Prefix",
                                "Prefix Sid",
                                "Flags",
                                "MT ID",
                                "Algorithm",
                                "SID",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "20",
                            "tlv-type-name": "Extended Prefix",
                            "tlv-type-value": "1",
                        },
                    },
                    "our-entry": True,
                    "sequence-number": "0x80001b9e",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "694",
                    "checksum": "0x7efa",
                    "lsa-id": "10.64.0.52",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.169.14.240",
                                "10.169.14.122",
                                "0xe0",
                                "0",
                                "0",
                                "2567",
                                "0x60",
                                "0",
                                "0",
                                "2568",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "our-entry": True,
                    "sequence-number": "0x80000308",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "1235",
                    "checksum": "0x1839",
                    "lsa-id": "10.64.0.54",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.189.5.253",
                                "10.189.5.93",
                                "0xe0",
                                "0",
                                "0",
                                "28985",
                                "0x60",
                                "0",
                                "0",
                                "28986",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "our-entry": True,
                    "sequence-number": "0x800002dc",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "2069",
                    "checksum": "0x92eb",
                    "lsa-id": "10.64.0.55",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.19.198.239",
                                "10.19.198.25",
                                "0xe0",
                                "0",
                                "0",
                                "167966",
                                "0x60",
                                "0",
                                "0",
                                "167967",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "our-entry": True,
                    "sequence-number": "0x800001bb",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "2336",
                    "checksum": "0xc3fb",
                    "lsa-id": "10.169.14.240",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "50",
                            "ospf-topology-name": "default",
                            "tag": "0.0.0.0",
                            "type-value": "1",
                        },
                    },
                    "our-entry": True,
                    "sequence-number": "0x80001a3a",
                },
            ],
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspfDatabaseAdvertisingRouterSelfDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspfDatabaseAdvertisingRouterSelfDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowOspfDatabaseExtensive(unittest.TestCase):

    maxDiff = None

    device = Device(name="test-device")

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
        show ospf database extensive

            OSPF database, Area 0.0.0.8
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
        Router   10.36.3.3          10.36.3.3          0x80004d2d   352  0x22 0xa127 2496
        bits 0x0, link count 206
        id 10.36.3.3, data 255.255.255.255, Type Stub (3)
            Topology count: 0, Default metric: 1
        id 192.168.220.0, data 255.255.255.255, Type Stub (3)
            Topology count: 0, Default metric: 1
        id 192.168.220.4, data 255.255.255.255, Type Stub (3)
            Topology count: 0, Default metric: 1
        id 192.168.220.1, data 255.255.255.255, Type Stub (3)
            Topology count: 0, Default metric: 1
        id 192.168.220.2, data 255.255.255.255, Type Stub (3)
            Topology count: 0, Default metric: 1
        id 192.168.220.3, data 255.255.255.255, Type Stub (3)
            Topology count: 0, Default metric: 1
        id 10.169.196.241, data 192.168.111.1, Type PointToPoint (1)
            Topology count: 0, Default metric: 1
        id 192.168.111.0, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 1
        id 10.169.196.241, data 192.168.4.1, Type PointToPoint (1)
            Topology count: 0, Default metric: 1
        id 192.168.4.0, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 1
        Topology default (ID 0)
            Type: PointToPoint, Node ID: 10.169.196.241
            Metric: 1, Bidirectional
        Aging timer 00:54:08
        Installed 00:05:44 ago, expires in 00:54:08, sent 00:05:42 ago
        Last changed 1d 02:16:03 ago, Change count: 69
        Router   10.100.5.5          10.100.5.5          0x800019d7  1760  0x22 0xa1c   60
        bits 0x0, link count 3
        id 10.100.5.5, data 255.255.255.255, Type Stub (3)
            Topology count: 0, Default metric: 1
        id 10.34.2.250, data 10.16.0.2, Type PointToPoint (1)
            Topology count: 0, Default metric: 1
        id 10.16.0.0, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 1
        Topology default (ID 0)
            Type: PointToPoint, Node ID: 10.34.2.250
            Metric: 1, Bidirectional
        Aging timer 00:30:40
        Installed 00:29:13 ago, expires in 00:30:40, sent 00:29:11 ago
        Last changed 4w6d 19:31:25 ago, Change count: 38
        Router   10.19.198.239    10.19.198.239    0x80000442   913  0x22 0x95bf  96
        bits 0x0, link count 6
        id 10.19.198.239, data 255.255.255.255, Type Stub (3)
            Topology count: 0, Default metric: 1
        id 10.189.5.253, data 10.19.198.30, Type PointToPoint (1)
            Topology count: 0, Default metric: 1000
        id 10.19.198.28, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 1000
        id 10.189.5.252, data 10.19.198.26, Type PointToPoint (1)
            Topology count: 0, Default metric: 1000
        id 10.19.198.24, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 1000
        id 10.15.0.0, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 1
        Topology default (ID 0)
            Type: PointToPoint, Node ID: 10.189.5.252
            Metric: 1000, Bidirectional
            Type: PointToPoint, Node ID: 10.189.5.253
            Metric: 1000, Bidirectional
        Aging timer 00:44:47
        Installed 00:15:12 ago, expires in 00:44:47, sent 00:15:10 ago
        Last changed 1w0d 19:55:00 ago, Change count: 45
        Router   10.34.2.250     10.34.2.250     0x8000205a  1027  0x22 0x26f6 144
        bits 0x2, link count 10
        id 10.34.2.251, data 10.34.2.201, Type PointToPoint (1)
            Topology count: 0, Default metric: 5
        id 10.34.2.200, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 5
        id 10.169.14.240, data 10.169.14.158, Type PointToPoint (1)
            Topology count: 0, Default metric: 100
        id 10.169.14.156, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 100
        id 10.169.196.241, data 10.169.196.213, Type PointToPoint (1)
            Topology count: 0, Default metric: 1000
        id 10.169.196.212, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 1000
        id 10.100.5.5, data 10.16.0.1, Type PointToPoint (1)
            Topology count: 0, Default metric: 1000
        id 10.16.0.0, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 1000
        id 192.168.220.0, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 1000
        id 10.34.2.250, data 255.255.255.255, Type Stub (3)
            Topology count: 0, Default metric: 0
        Topology default (ID 0)
            Type: PointToPoint, Node ID: 10.100.5.5
            Metric: 1000, Bidirectional
            Type: PointToPoint, Node ID: 10.169.196.241
            Metric: 1000, Bidirectional
            Type: PointToPoint, Node ID: 10.169.14.240
            Metric: 100, Bidirectional
            Type: PointToPoint, Node ID: 10.34.2.251
            Metric: 5, Bidirectional
        Aging timer 00:42:53
        Installed 00:17:01 ago, expires in 00:42:53, sent 00:16:59 ago
        Last changed 2w0d 00:51:24 ago, Change count: 1911
        Router   10.34.2.251     10.34.2.251     0x80001dde   858  0x22 0x1022 108
        bits 0x2, link count 7
        id 10.34.2.250, data 10.34.2.202, Type PointToPoint (1)
            Topology count: 0, Default metric: 5
        id 10.34.2.200, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 5
        id 10.169.14.241, data 10.169.14.34, Type PointToPoint (1)
            Topology count: 0, Default metric: 120
        id 10.169.14.32, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 120
        id 10.169.196.241, data 10.169.196.217, Type PointToPoint (1)
            Topology count: 0, Default metric: 1000
        id 10.169.196.216, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 1000
        id 10.34.2.251, data 255.255.255.255, Type Stub (3)
            Topology count: 0, Default metric: 0
        Topology default (ID 0)
            Type: PointToPoint, Node ID: 10.169.196.241
            Metric: 1000, Bidirectional
            Type: PointToPoint, Node ID: 10.169.14.241
            Metric: 120, Bidirectional
            Type: PointToPoint, Node ID: 10.34.2.250
            Metric: 5, Bidirectional
        Aging timer 00:45:42
        Installed 00:14:09 ago, expires in 00:45:42, sent 00:14:07 ago
        Last changed 2w0d 00:51:22 ago, Change count: 1258
        OpaqArea 10.1.0.4          10.34.2.250     0x8000029e  1718  0x22 0x1e4  136
        Opaque LSA
        Link (2), length 112:
            Linktype (1), length 1:
            1
            LinkID (2), length 4:
            10.169.14.240
            LocIfAdr (3), length 4:
            10.169.14.158
            RemIfAdr (4), length 4:
            10.169.14.157
            TEMetric (5), length 4:
            100
            MaxBW (6), length 4:
            1000Mbps
            MaxRsvBW (7), length 4:
            1000Mbps
            UnRsvBW (8), length 32:
                Priority 0, 1000Mbps
                Priority 1, 1000Mbps
                Priority 2, 1000Mbps
                Priority 3, 1000Mbps
                Priority 4, 1000Mbps
                Priority 5, 1000Mbps
                Priority 6, 1000Mbps
                Priority 7, 1000Mbps
            LinkLocalRemoteIdentifier (11), length 8:
            Local 334, Remote 0
            Color (9), length 4:
            4
        Aging timer 00:31:21
        Installed 00:28:32 ago, expires in 00:31:22, sent 00:28:30 ago
        Last changed 3w0d 08:18:02 ago, Change count: 5
        OpaqArea 10.1.0.4          10.34.2.251     0x80000299  1517  0x22 0x29c0 136
        Opaque LSA
        Link (2), length 112:
            Linktype (1), length 1:
            1
            LinkID (2), length 4:
            10.169.14.241
            LocIfAdr (3), length 4:
            10.169.14.34
            RemIfAdr (4), length 4:
            10.169.14.33
            TEMetric (5), length 4:
            90
            MaxBW (6), length 4:
            1000Mbps
            MaxRsvBW (7), length 4:
            1000Mbps
            UnRsvBW (8), length 32:
                Priority 0, 1000Mbps
                Priority 1, 1000Mbps
                Priority 2, 1000Mbps
                Priority 3, 1000Mbps
                Priority 4, 1000Mbps
                Priority 5, 1000Mbps
                Priority 6, 1000Mbps
                Priority 7, 1000Mbps
            LinkLocalRemoteIdentifier (11), length 8:
            Local 334, Remote 0
            Color (9), length 4:
            6
        Aging timer 00:34:43
        Installed 00:25:08 ago, expires in 00:34:43, sent 00:25:06 ago
        Last changed 3w0d 08:09:50 ago, Change count: 1
        OpaqArea 10.1.0.4          10.169.14.240   0x800003f8  1529  0x22 0xb606 136
        Opaque LSA
        Link (2), length 112:
            Linktype (1), length 1:
            1
            LinkID (2), length 4:
            10.189.5.252
            LocIfAdr (3), length 4:
            10.169.14.121
            RemIfAdr (4), length 4:
            10.169.14.122
            TEMetric (5), length 4:
            100
            MaxBW (6), length 4:
            1000Mbps
            MaxRsvBW (7), length 4:
            1000Mbps
            UnRsvBW (8), length 32:
                Priority 0, 1000Mbps
                Priority 1, 1000Mbps
                Priority 2, 1000Mbps
                Priority 3, 1000Mbps
                Priority 4, 1000Mbps
                Priority 5, 1000Mbps
                Priority 6, 1000Mbps
                Priority 7, 1000Mbps
            LinkLocalRemoteIdentifier (11), length 8:
            Local 334, Remote 0
            Color (9), length 4:
            10
        Aging timer 00:34:31
        Installed 00:25:26 ago, expires in 00:34:31, sent 00:25:24 ago
        Last changed 3w3d 07:23:05 ago, Change count: 6
        OpaqArea 10.1.0.4          10.169.14.241   0x800013fe  2418  0x22 0x694d 136
        Opaque LSA
        Link (2), length 112:
            Linktype (1), length 1:
            1
            LinkID (2), length 4:
            10.189.5.253
            LocIfAdr (3), length 4:
            10.169.14.129
            RemIfAdr (4), length 4:
            10.169.14.130
            TEMetric (5), length 4:
            70
            MaxBW (6), length 4:
            1000Mbps
            MaxRsvBW (7), length 4:
            1000Mbps
            UnRsvBW (8), length 32:
                Priority 0, 1000Mbps
                Priority 1, 1000Mbps
                Priority 2, 1000Mbps
                Priority 3, 1000Mbps
                Priority 4, 1000Mbps
                Priority 5, 1000Mbps
                Priority 6, 1000Mbps
                Priority 7, 1000Mbps
            LinkLocalRemoteIdentifier (11), length 8:
            Local 334, Remote 0
            Color (9), length 4:
            6
        Aging timer 00:19:42
        Installed 00:40:12 ago, expires in 00:19:42, sent 00:40:10 ago
        Last changed 3w3d 07:23:04 ago, Change count: 35
        OpaqArea*10.1.0.4          10.189.5.252     0x800013e8  2702  0x22 0xb804 136
        Opaque LSA
        Link (2), length 112:
            Linktype (1), length 1:
            1
            LinkID (2), length 4:
            10.169.14.240
            LocIfAdr (3), length 4:
            10.169.14.122
            RemIfAdr (4), length 4:
            10.169.14.121
            TEMetric (5), length 4:
            100
            MaxBW (6), length 4:
            1000Mbps
            MaxRsvBW (7), length 4:
            1000Mbps
            UnRsvBW (8), length 32:
                Priority 0, 1000Mbps
                Priority 1, 1000Mbps
                Priority 2, 1000Mbps
                Priority 3, 1000Mbps
                Priority 4, 1000Mbps
                Priority 5, 1000Mbps
                Priority 6, 1000Mbps
                Priority 7, 1000Mbps
            LinkLocalRemoteIdentifier (11), length 8:
            Local 334, Remote 0
            Color (9), length 4:
            10
        Gen timer 00:00:19
        Aging timer 00:14:58
        Installed 00:45:02 ago, expires in 00:14:58, sent 00:45:00 ago
        Last changed 3w3d 07:23:03 ago, Change count: 3, Ours, TE Link ID: 2147483652
        OpaqArea 10.1.0.4          10.189.5.253     0x80000f9c   209  0x22 0x4cd0 136
        Opaque LSA
        Link (2), length 112:
            Linktype (1), length 1:
            1
            LinkID (2), length 4:
            10.169.14.241
            LocIfAdr (3), length 4:
            10.169.14.130
            RemIfAdr (4), length 4:
            10.169.14.129
            TEMetric (5), length 4:
            70
            MaxBW (6), length 4:
            1000Mbps
            MaxRsvBW (7), length 4:
            1000Mbps
            UnRsvBW (8), length 32:
                Priority 0, 1000Mbps
                Priority 1, 1000Mbps
                Priority 2, 1000Mbps
                Priority 3, 1000Mbps
                Priority 4, 1000Mbps
                Priority 5, 1000Mbps
                Priority 6, 1000Mbps
                Priority 7, 1000Mbps
            LinkLocalRemoteIdentifier (11), length 8:
            Local 334, Remote 0
            Color (9), length 4:
            6
        Aging timer 00:56:31
        Installed 00:03:26 ago, expires in 00:56:31, sent 00:03:24 ago
        Last changed 3w3d 07:23:04 ago, Change count: 15
        OpaqArea 10.1.0.5          10.34.2.250     0x800001b5   580  0x22 0x5e9d 136
        Opaque LSA
        Link (2), length 112:
            Linktype (1), length 1:
            1
            LinkID (2), length 4:
            10.169.196.241
            LocIfAdr (3), length 4:
            10.169.196.213
            RemIfAdr (4), length 4:
            10.169.196.214
            TEMetric (5), length 4:
            1000
            MaxBW (6), length 4:
            1000Mbps
            MaxRsvBW (7), length 4:
            1000Mbps
            UnRsvBW (8), length 32:
                Priority 0, 1000Mbps
                Priority 1, 1000Mbps
                Priority 2, 1000Mbps
                Priority 3, 1000Mbps
                Priority 4, 1000Mbps
                Priority 5, 1000Mbps
                Priority 6, 1000Mbps
                Priority 7, 1000Mbps
            LinkLocalRemoteIdentifier (11), length 8:
            Local 337, Remote 0
            Color (9), length 4:
            2
        Aging timer 00:50:20
        Installed 00:09:34 ago, expires in 00:50:20, sent 00:09:32 ago
        Last changed 2w0d 00:51:24 ago, Change count: 1
        OpaqArea 10.49.0.1          10.100.5.5          0x800019ac  1760  0x20 0x6c5a  44
        Opaque LSA
        Extended Prefix (1), length 20:
            Route Type (1), length 1:
                1
            Prefix Length (2), length 1:
                32
            AF (3), length 1:
                0
            Flags (4),  length 1:
                0x40
            Prefix (5), length 32:
                10.100.5.5
            Prefix Sid (2), length 8:
            Flags (1), length 1:
                0x00
            MT ID (2), length 1:
                0
            Algorithm (3), length 1:
                0
            SID (4), length 4:
                1000
        Aging timer 00:30:40
        Installed 00:29:13 ago, expires in 00:30:40, sent 00:29:11 ago
        Last changed 21w5d 22:48:11 ago, Change count: 1
        OpaqArea 10.49.0.1          10.34.2.250     0x80001fa9  1027  0x22 0x7fa7  44
        Opaque LSA
        Extended Prefix (1), length 20:
            Route Type (1), length 1:
                1
            Prefix Length (2), length 1:
                32
            AF (3), length 1:
                0
            Flags (4),  length 1:
                0x40
            Prefix (5), length 32:
                10.34.2.250
            Prefix Sid (2), length 8:
            Flags (1), length 1:
                0x00
            MT ID (2), length 1:
                0
            Algorithm (3), length 1:
                0
            SID (4), length 4:
                61
        Aging timer 00:42:53
        Installed 00:17:01 ago, expires in 00:42:53, sent 00:16:59 ago
        Last changed 30w0d 01:32:34 ago, Change count: 1
        OpaqArea 10.49.0.1          10.34.2.251     0x80001cfb   858  0x22 0x6ce   44
        Opaque LSA
        Extended Prefix (1), length 20:
            Route Type (1), length 1:
                1
            Prefix Length (2), length 1:
                32
            AF (3), length 1:
                0
            Flags (4),  length 1:
                0x40
            Prefix (5), length 32:
                10.34.2.251
            Prefix Sid (2), length 8:
            Flags (1), length 1:
                0x00
            MT ID (2), length 1:
                0
            Algorithm (3), length 1:
                0
            SID (4), length 4:
                62
        Aging timer 00:45:42
        Installed 00:14:09 ago, expires in 00:45:42, sent 00:14:07 ago
        Last changed 30w0d 01:32:36 ago, Change count: 1
        OpaqArea 10.49.0.1          10.169.14.240   0x80001bc2   173  0x22 0x97ab  44
        Opaque LSA
        Extended Prefix (1), length 20:
            Route Type (1), length 1:
                1
            Prefix Length (2), length 1:
                32
            AF (3), length 1:
                0
            Flags (4),  length 1:
                0x40
            Prefix (5), length 32:
                10.169.14.240
            Prefix Sid (2), length 8:
            Flags (1), length 1:
                0x00
            MT ID (2), length 1:
                0
            Algorithm (3), length 1:
                0
            SID (4), length 4:
                51
        Aging timer 00:57:06
        Installed 00:02:50 ago, expires in 00:57:07, sent 00:02:48 ago
        Last changed 30w0d 01:32:37 ago, Change count: 1
        OpaqArea 10.49.0.1          10.169.14.241   0x80001f67  1759  0x22 0x6433  44
        Opaque LSA
        Extended Prefix (1), length 20:
            Route Type (1), length 1:
                1
            Prefix Length (2), length 1:
                32
            AF (3), length 1:
                0
            Flags (4),  length 1:
                0x40
            Prefix (5), length 32:
                10.169.14.241
            Prefix Sid (2), length 8:
            Flags (1), length 1:
                0x00
            MT ID (2), length 1:
                0
            Algorithm (3), length 1:
                0
            SID (4), length 4:
                52
        Aging timer 00:30:41
        Installed 00:29:13 ago, expires in 00:30:41, sent 00:29:11 ago
        Last changed 30w0d 01:32:36 ago, Change count: 1
        OpaqArea*10.49.0.1          10.189.5.252     0x80001b9e  1899  0x22 0x8c7f  44
        Opaque LSA
        Extended Prefix (1), length 20:
            Route Type (1), length 1:
                1
            Prefix Length (2), length 1:
                32
            AF (3), length 1:
                0
            Flags (4),  length 1:
                0x40
            Prefix (5), length 32:
                10.189.5.252
            Prefix Sid (2), length 8:
            Flags (1), length 1:
                0x00
            MT ID (2), length 1:
                0
            Algorithm (3), length 1:
                0
            SID (4), length 4:
                71
        Gen timer 00:18:20
        Aging timer 00:28:20
        Installed 00:31:39 ago, expires in 00:28:21, sent 00:31:37 ago
        Last changed 30w0d 01:46:13 ago, Change count: 1, Ours, TE Link ID: 0
        OpaqArea 10.49.0.1          10.189.5.253     0x80001b04  1980  0x22 0xe3bf  44
        Opaque LSA
        Extended Prefix (1), length 20:
            Route Type (1), length 1:
                1
            Prefix Length (2), length 1:
                32
            AF (3), length 1:
                0
            Flags (4),  length 1:
                0x40
            Prefix (5), length 32:
                10.189.5.253
            Prefix Sid (2), length 8:
            Flags (1), length 1:
                0x00
            MT ID (2), length 1:
                0
            Algorithm (3), length 1:
                0
            SID (4), length 4:
                72
        Aging timer 00:26:59
        Installed 00:32:57 ago, expires in 00:27:00, sent 00:32:55 ago
        Last changed 30w0d 01:32:43 ago, Change count: 1
        OpaqArea 10.64.0.1          10.34.2.250     0x800004f9   367  0x22 0x39a3  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.34.2.251
            Link Data (3), length 4:
            10.34.2.201
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                142149
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                142150
        Aging timer 00:53:53
        Installed 00:06:01 ago, expires in 00:53:53, sent 00:05:59 ago
        Last changed 2w0d 00:50:30 ago, Change count: 285
        OpaqArea 10.64.0.1          10.169.14.241   0x80000311  1016  0x22 0x7002  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.169.14.240
            Link Data (3), length 4:
            10.169.14.18
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                37408
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                37409
        Aging timer 00:43:04
        Installed 00:16:50 ago, expires in 00:43:04, sent 00:16:48 ago
        Last changed 2w6d 19:46:47 ago, Change count: 50
        OpaqArea 10.64.0.1          10.189.5.253     0x8000030a  2521  0x22 0x6915  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.169.14.241
            Link Data (3), length 4:
            10.169.14.130
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                1912
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                1913
        Aging timer 00:17:59
        Installed 00:41:58 ago, expires in 00:17:59, sent 00:41:56 ago
        Last changed 2w6d 20:01:45 ago, Change count: 31
        OpaqArea 10.64.0.2          10.169.14.241   0x80000305   790  0x22 0x7271  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.189.5.253
            Link Data (3), length 4:
            10.169.14.129
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                1647
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                1648
        Aging timer 00:46:49
        Installed 00:13:04 ago, expires in 00:46:50, sent 00:13:02 ago
        Last changed 2w6d 18:58:08 ago, Change count: 47
        OpaqArea 10.64.0.3          10.169.14.241   0x8000029a   565  0x22 0x7248  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.34.2.251
            Link Data (3), length 4:
            10.169.14.33
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                1649
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                1650
        Aging timer 00:50:35
        Installed 00:09:19 ago, expires in 00:50:35, sent 00:09:17 ago
        Last changed 2w6d 18:14:24 ago, Change count: 7
        OpaqArea 10.64.0.3          10.189.5.253     0x800002db   947  0x22 0x34eb  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.189.5.252
            Link Data (3), length 4:
            10.189.5.94
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                13988
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                13989
        Aging timer 00:44:13
        Installed 00:15:44 ago, expires in 00:44:13, sent 00:15:42 ago
        Last changed 2w0d 00:43:19 ago, Change count: 17
        OpaqArea 10.64.0.4          10.189.5.253     0x800001bb  2251  0x22 0x31be  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.19.198.239
            Link Data (3), length 4:
            10.19.198.29
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                102794
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                102795
        Aging timer 00:22:29
        Installed 00:37:28 ago, expires in 00:22:29, sent 00:37:26 ago
        Last changed 2w0d 00:51:02 ago, Change count: 1
        OpaqArea 10.64.0.6          10.100.5.5          0x800019bf  1760  0x20 0x4de2  56
        Opaque LSA
        Extended Link (1), length 32:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.34.2.250
            Link Data (3), length 4:
            10.16.0.2
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                24000
            Invalid (32768), length 4:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                24000
        Aging timer 00:30:40
        Installed 00:29:13 ago, expires in 00:30:40, sent 00:29:11 ago
        Last changed 21w5d 22:48:11 ago, Change count: 1
        OpaqArea 10.64.0.7          10.34.2.250     0x8000046b  2871  0x22 0xb9a6  48
        Opaque LSA
        Extended Link (1), length 24:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.100.5.5
            Link Data (3), length 4:
            10.16.0.1
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                207722
        Aging timer 00:12:09
        Installed 00:47:45 ago, expires in 00:12:09, sent 00:47:43 ago
        Last changed 2w0d 00:42:10 ago, Change count: 123
        OpaqArea 10.64.0.7          10.34.2.251     0x800004de  1297  0x22 0x6a96  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.34.2.250
            Link Data (3), length 4:
            10.34.2.202
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                112778
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                112779
        Aging timer 00:38:23
        Installed 00:21:28 ago, expires in 00:38:23, sent 00:21:26 ago
        Last changed 2w6d 19:46:37 ago, Change count: 243
        OpaqArea 10.64.0.17         10.19.198.239    0x8000025d   913  0x20 0xb34a 104
        Opaque LSA
        Extended Link (1), length 80:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.189.5.252
            Link Data (3), length 4:
            10.19.198.26
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                1730
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                1729
            Invalid (8), length 4:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                1729
            Invalid (32768), length 4:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                1729
            Invalid (9), length 8:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                1729
            Invalid (32769), length 12:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                1729
        Aging timer 00:44:47
        Installed 00:15:12 ago, expires in 00:44:47, sent 00:15:10 ago
        Last changed 2w0d 00:51:03 ago, Change count: 2
        OpaqArea 10.64.0.17         10.169.196.241  0x8000025d   812  0x20 0x3e3c 104
        Opaque LSA
        Extended Link (1), length 80:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.34.2.250
            Link Data (3), length 4:
            10.169.196.214
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                223815
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                223843
            Invalid (8), length 4:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                223843
            Invalid (32768), length 4:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                223843
            Invalid (9), length 8:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                223843
            Invalid (32769), length 12:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                223843
        Aging timer 00:46:27
        Installed 00:13:25 ago, expires in 00:46:28, sent 00:13:23 ago
        Last changed 2w0d 00:51:24 ago, Change count: 2
        OpaqArea 10.64.0.18         10.19.198.239    0x8000025d   913  0x20 0xb938 104
        Opaque LSA
        Extended Link (1), length 80:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.189.5.253
            Link Data (3), length 4:
            10.19.198.30
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                1728
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                1727
            Invalid (8), length 4:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                1727
            Invalid (32768), length 4:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                1727
            Invalid (9), length 8:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                1727
            Invalid (32769), length 12:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                1727
        Aging timer 00:44:47
        Installed 00:15:12 ago, expires in 00:44:47, sent 00:15:10 ago
        Last changed 2w0d 00:51:02 ago, Change count: 2
        OpaqArea 10.64.0.18         10.169.196.241  0x8000025d   812  0x20 0x6fdb 104
        Opaque LSA
        Extended Link (1), length 80:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.34.2.251
            Link Data (3), length 4:
            10.169.196.218
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                223844
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                223845
            Invalid (8), length 4:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                223845
            Invalid (32768), length 4:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                223845
            Invalid (9), length 8:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                223845
            Invalid (32769), length 12:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                223845
        Aging timer 00:46:27
        Installed 00:13:25 ago, expires in 00:46:28, sent 00:13:23 ago
        Last changed 2w0d 00:51:22 ago, Change count: 2
        OpaqArea 10.64.0.31         10.34.2.251     0x8000029b   114  0x22 0xe70a  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.169.14.241
            Link Data (3), length 4:
            10.169.14.34
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                15022
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                15023
        Aging timer 00:58:06
        Installed 00:01:47 ago, expires in 00:58:06, sent 00:01:45 ago
        Last changed 2w0d 00:43:41 ago, Change count: 8
        OpaqArea 10.64.0.32         10.34.2.251     0x800001b5  1078  0x22 0xe396  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.169.196.241
            Link Data (3), length 4:
            10.169.196.217
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                259074
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                259075
        Aging timer 00:42:02
        Installed 00:17:50 ago, expires in 00:42:02, sent 00:17:48 ago
        Last changed 2w0d 00:51:22 ago, Change count: 1
        OpaqArea 10.64.0.37         10.34.2.250     0x8000029b  1949  0x22 0xffb8  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.169.14.240
            Link Data (3), length 4:
            10.169.14.158
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                143642
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                143643
        Aging timer 00:27:31
        Installed 00:32:23 ago, expires in 00:27:31, sent 00:32:21 ago
        Last changed 2w0d 00:27:01 ago, Change count: 7
        OpaqArea 10.64.0.38         10.34.2.250     0x800001b5  1257  0x22 0x71b3  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.169.196.241
            Link Data (3), length 4:
            10.169.196.213
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                358249
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                358250
        Aging timer 00:39:02
        Installed 00:20:51 ago, expires in 00:39:03, sent 00:20:49 ago
        Last changed 2w0d 00:51:24 ago, Change count: 1
        OpaqArea*10.64.0.52         10.189.5.252     0x80000308   792  0x22 0x7efa  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.169.14.240
            Link Data (3), length 4:
            10.169.14.122
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                2567
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                2568
        Gen timer 00:36:39
        Aging timer 00:46:48
        Installed 00:13:12 ago, expires in 00:46:48, sent 00:13:10 ago
        Last changed 2w0d 00:37:11 ago, Change count: 25, Ours, TE Link ID: 0
        OpaqArea*10.64.0.54         10.189.5.252     0x800002dc  1333  0x22 0x1839  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.189.5.253
            Link Data (3), length 4:
            10.189.5.93
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                28985
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                28986
        Gen timer 00:27:30
        Aging timer 00:37:47
        Installed 00:22:13 ago, expires in 00:37:47, sent 00:22:11 ago
        Last changed 2w0d 00:46:13 ago, Change count: 26, Ours, TE Link ID: 0
        OpaqArea*10.64.0.55         10.189.5.252     0x800001bb  2167  0x22 0x92eb  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.19.198.239
            Link Data (3), length 4:
            10.19.198.25
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                167966
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                167967
        Gen timer 00:09:20
        Aging timer 00:23:53
        Installed 00:36:07 ago, expires in 00:23:53, sent 00:36:05 ago
        Last changed 2w0d 00:51:03 ago, Change count: 1, Ours, TE Link ID: 0
        OpaqArea 10.64.0.57         10.169.14.240   0x80000303  1378  0x22 0x7544  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.169.14.241
            Link Data (3), length 4:
            10.169.14.17
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                379383
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                379384
        Aging timer 00:37:01
        Installed 00:22:55 ago, expires in 00:37:02, sent 00:22:53 ago
        Last changed 2w6d 19:46:52 ago, Change count: 57
        OpaqArea 10.64.0.59         10.169.14.240   0x800002f4  1680  0x22 0x6d12  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.189.5.252
            Link Data (3), length 4:
            10.169.14.121
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                25
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                26
        Aging timer 00:32:00
        Installed 00:27:57 ago, expires in 00:32:00, sent 00:27:55 ago
        Last changed 3w1d 08:43:52 ago, Change count: 52
        OpaqArea 10.64.0.60         10.169.14.240   0x8000028b  1228  0x22 0x4f1a  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.34.2.250
            Link Data (3), length 4:
            10.169.14.157
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                207596
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                207597
        Aging timer 00:39:32
        Installed 00:20:25 ago, expires in 00:39:32, sent 00:20:23 ago
        Last changed 2w6d 18:58:13 ago, Change count: 6
        OpaqArea 10.64.8.74         10.169.196.241  0x80000030   326  0x20 0xdcd1  92
        Opaque LSA
        Extended Link (1), length 68:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            10.36.3.3
            Link Data (3), length 4:
            192.168.111.2
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                223852
            Invalid (8), length 4:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                223852
            Invalid (32768), length 4:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                223852
            Invalid (9), length 8:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                223852
            Invalid (32769), length 12:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                223852
        Aging timer 00:54:34
        Installed 00:05:21 ago, expires in 00:54:34, sent 00:05:19 ago
        Last changed 1d 02:16:03 ago, Change count: 1
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
        Extern   0.0.0.0          10.34.2.251     0x800019e3  2614  0x22 0x6715  36
        mask 0.0.0.0
        Topology default (ID 0)
            Type: 1, Metric: 1, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
        Aging timer 00:16:26
        Installed 00:43:25 ago, expires in 00:16:26, sent 00:43:23 ago
        Last changed 30w0d 01:32:36 ago, Change count: 1
        Extern   0.0.0.0          10.169.14.240   0x8000039e  2282  0x22 0x9fcc  36
        mask 0.0.0.0
        Topology default (ID 0)
            Type: 1, Metric: 1, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
        Aging timer 00:21:57
        Installed 00:37:59 ago, expires in 00:21:58, sent 00:37:57 ago
        Last changed 4w2d 05:46:52 ago, Change count: 1
        Extern   10.1.0.0          192.168.36.119  0x800019b0  1219  0x20 0x3bc3  36
        mask 255.255.255.0
        Topology default (ID 0)
            Type: 2, Metric: 20, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
        Aging timer 00:39:41
        Installed 00:20:15 ago, expires in 00:39:41, sent 00:20:13 ago
        Last changed 21w6d 00:04:15 ago, Change count: 1
        Extern   10.1.0.0          192.168.36.120  0x800019b1   791  0x20 0x33c9  36
        mask 255.255.255.0
        Topology default (ID 0)
            Type: 2, Metric: 20, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
        Aging timer 00:46:49
        Installed 00:13:07 ago, expires in 00:46:49, sent 00:13:05 ago
        Last changed 21w6d 00:04:43 ago, Change count: 1
        Extern   10.174.132.237    10.169.14.240   0x8000039e  2132  0x22 0xf161  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
        Aging timer 00:24:28
        Installed 00:35:29 ago, expires in 00:24:28, sent 00:35:27 ago
        Last changed 4w2d 05:46:49 ago, Change count: 1
        Extern   10.34.2.250     10.169.14.240   0x80000288  2734  0x22 0x473e  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 10.166.34.12
        Aging timer 00:14:26
        Installed 00:45:31 ago, expires in 00:14:26, sent 00:45:29 ago
        Last changed 3w0d 08:49:51 ago, Change count: 1
        Extern   10.34.2.250     10.169.14.241   0x80000298  2637  0x22 0x2153  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 10.166.34.12
        Aging timer 00:16:03
        Installed 00:43:51 ago, expires in 00:16:03, sent 00:43:49 ago
        Last changed 3w0d 08:09:51 ago, Change count: 1
        Extern   10.34.2.251     10.169.14.240   0x80000289   475  0x22 0x3b48  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 10.166.34.12
        Aging timer 00:52:05
        Installed 00:07:52 ago, expires in 00:52:05, sent 00:07:50 ago
        Last changed 3w0d 08:49:56 ago, Change count: 1
        Extern   192.168.100.0    10.169.14.240   0x800002da  1077  0x22 0xfb51  36
        mask 255.255.255.128
        Topology default (ID 0)
            Type: 1, Metric: 31900, Fwd addr: 0.0.0.0, Tag: 10.76.212.52
        Aging timer 00:42:03
        Installed 00:17:54 ago, expires in 00:42:03, sent 00:17:52 ago
        Last changed 2w6d 18:58:13 ago, Change count: 75
        Extern   192.168.100.252  10.169.14.240   0x800002d9   927  0x22 0x19b8  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 31900, Fwd addr: 0.0.0.0, Tag: 10.76.212.52
        Aging timer 00:44:33
        Installed 00:15:24 ago, expires in 00:44:33, sent 00:15:22 ago
        Last changed 2w6d 18:58:13 ago, Change count: 75
    """
    }
    golden_output_1 = {
        "execute.return_value": """
        show ospf database advertising-router 10.34.2.250 extensive
            OSPF database, Area 0.0.0.8
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
        Router   10.34.2.250     10.34.2.250     0x80000003  1107  0x22 0x29f7  60
        bits 0x0, link count 3
        id 10.169.14.240, data 10.169.14.158, Type PointToPoint (1)
            Topology count: 0, Default metric: 1
        id 10.169.14.156, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 1
        id 10.34.2.250, data 255.255.255.255, Type Stub (3)
            Topology count: 0, Default metric: 0
        Topology default (ID 0)
            Type: PointToPoint, Node ID: 10.169.14.240
            Metric: 1, Bidirectional
        Aging timer 00:41:32
        Installed 00:18:24 ago, expires in 00:41:33
        Last changed 00:18:53 ago, Change count: 2
        """
    }
    golden_parsed_output = {
        "ospf-database-information": {
            "ospf-area-header": {"ospf-area": "0.0.0.8"},
            "ospf-database": [
                {
                    "advertising-router": "10.36.3.3",
                    "age": "352",
                    "checksum": "0xa127",
                    "lsa-id": "10.36.3.3",
                    "lsa-length": "2496",
                    "lsa-type": "Router",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:54:08"},
                        "expiration-time": {"#text": "00:54:08"},
                        "installation-time": {"#text": "00:05:44"},
                        "lsa-change-count": "69",
                        "lsa-changed-time": {"#text": "1d 02:16:03"},
                        "send-time": {"#text": "00:05:42"},
                    },
                    "ospf-router-lsa": {
                        "bits": "0x0",
                        "link-count": "206",
                        "ospf-link": [
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "10.36.3.3",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "10.36.3.3",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "192.168.220.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "192.168.220.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "192.168.220.4",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "192.168.220.4",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "192.168.220.1",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "192.168.220.1",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "192.168.220.2",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "192.168.220.2",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "192.168.220.3",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "192.168.220.3",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "192.168.111.1",
                                "link-id": "10.169.196.241",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "192.168.111.1",
                                "link-id": "10.169.196.241",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "192.168.111.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "192.168.111.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "192.168.4.1",
                                "link-id": "10.169.196.241",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "192.168.4.1",
                                "link-id": "10.169.196.241",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "192.168.4.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "192.168.4.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                        ],
                        "ospf-lsa-topology": {
                            "ospf-lsa-topology-link": [
                                {
                                    "link-type-name": "PointToPoint",
                                    "ospf-lsa-topology-link-metric": "1",
                                    "ospf-lsa-topology-link-node-id": "10.169.196.241",
                                    "ospf-lsa-topology-link-state": "Bidirectional",
                                }
                            ],
                            "ospf-topology-id": "0",
                            "ospf-topology-name": "default",
                        },
                    },
                    "sequence-number": "0x80004d2d",
                },
                {
                    "advertising-router": "10.100.5.5",
                    "age": "1760",
                    "checksum": "0xa1c",
                    "lsa-id": "10.100.5.5",
                    "lsa-length": "60",
                    "lsa-type": "Router",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:30:40"},
                        "expiration-time": {"#text": "00:30:40"},
                        "installation-time": {"#text": "00:29:13"},
                        "lsa-change-count": "38",
                        "lsa-changed-time": {"#text": "4w6d 19:31:25"},
                        "send-time": {"#text": "00:29:11"},
                    },
                    "ospf-router-lsa": {
                        "bits": "0x0",
                        "link-count": "3",
                        "ospf-link": [
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "10.100.5.5",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "10.100.5.5",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.16.0.2",
                                "link-id": "10.34.2.250",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.16.0.2",
                                "link-id": "10.34.2.250",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.16.0.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.16.0.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                        ],
                        "ospf-lsa-topology": {
                            "ospf-lsa-topology-link": [
                                {
                                    "link-type-name": "PointToPoint",
                                    "ospf-lsa-topology-link-metric": "1",
                                    "ospf-lsa-topology-link-node-id": "10.34.2.250",
                                    "ospf-lsa-topology-link-state": "Bidirectional",
                                }
                            ],
                            "ospf-topology-id": "0",
                            "ospf-topology-name": "default",
                        },
                    },
                    "sequence-number": "0x800019d7",
                },
                {
                    "advertising-router": "10.19.198.239",
                    "age": "913",
                    "checksum": "0x95bf",
                    "lsa-id": "10.19.198.239",
                    "lsa-length": "96",
                    "lsa-type": "Router",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:44:47"},
                        "expiration-time": {"#text": "00:44:47"},
                        "installation-time": {"#text": "00:15:12"},
                        "lsa-change-count": "45",
                        "lsa-changed-time": {"#text": "1w0d 19:55:00"},
                        "send-time": {"#text": "00:15:10"},
                    },
                    "ospf-router-lsa": {
                        "bits": "0x0",
                        "link-count": "6",
                        "ospf-link": [
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "10.19.198.239",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "10.19.198.239",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.19.198.30",
                                "link-id": "10.189.5.253",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.19.198.30",
                                "link-id": "10.189.5.253",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.19.198.28",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.19.198.28",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.19.198.26",
                                "link-id": "10.189.5.252",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.19.198.26",
                                "link-id": "10.189.5.252",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.19.198.24",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.19.198.24",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.15.0.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.15.0.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                        ],
                        "ospf-lsa-topology": {
                            "ospf-lsa-topology-link": [
                                {
                                    "link-type-name": "PointToPoint",
                                    "ospf-lsa-topology-link-metric": "1000",
                                    "ospf-lsa-topology-link-node-id": "10.189.5.252",
                                    "ospf-lsa-topology-link-state": "Bidirectional",
                                },
                                {
                                    "link-type-name": "PointToPoint",
                                    "ospf-lsa-topology-link-metric": "1000",
                                    "ospf-lsa-topology-link-node-id": "10.189.5.253",
                                    "ospf-lsa-topology-link-state": "Bidirectional",
                                },
                            ],
                            "ospf-topology-id": "0",
                            "ospf-topology-name": "default",
                        },
                    },
                    "sequence-number": "0x80000442",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "1027",
                    "checksum": "0x26f6",
                    "lsa-id": "10.34.2.250",
                    "lsa-length": "144",
                    "lsa-type": "Router",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:42:53"},
                        "expiration-time": {"#text": "00:42:53"},
                        "installation-time": {"#text": "00:17:01"},
                        "lsa-change-count": "1911",
                        "lsa-changed-time": {"#text": "2w0d 00:51:24"},
                        "send-time": {"#text": "00:16:59"},
                    },
                    "ospf-router-lsa": {
                        "bits": "0x2",
                        "link-count": "10",
                        "ospf-link": [
                            {
                                "link-data": "10.34.2.201",
                                "link-id": "10.34.2.251",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "5",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.34.2.201",
                                "link-id": "10.34.2.251",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "5",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.34.2.200",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "5",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.34.2.200",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "5",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.169.14.158",
                                "link-id": "10.169.14.240",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "100",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.169.14.158",
                                "link-id": "10.169.14.240",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "100",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.169.14.156",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "100",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.169.14.156",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "100",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.169.196.213",
                                "link-id": "10.169.196.241",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.169.196.213",
                                "link-id": "10.169.196.241",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.169.196.212",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.169.196.212",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.16.0.1",
                                "link-id": "10.100.5.5",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.16.0.1",
                                "link-id": "10.100.5.5",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.16.0.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.16.0.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "192.168.220.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "192.168.220.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "10.34.2.250",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "0",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "10.34.2.250",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "0",
                                "ospf-topology-count": "0",
                            },
                        ],
                        "ospf-lsa-topology": {
                            "ospf-lsa-topology-link": [
                                {
                                    "link-type-name": "PointToPoint",
                                    "ospf-lsa-topology-link-metric": "1000",
                                    "ospf-lsa-topology-link-node-id": "10.100.5.5",
                                    "ospf-lsa-topology-link-state": "Bidirectional",
                                },
                                {
                                    "link-type-name": "PointToPoint",
                                    "ospf-lsa-topology-link-metric": "1000",
                                    "ospf-lsa-topology-link-node-id": "10.169.196.241",
                                    "ospf-lsa-topology-link-state": "Bidirectional",
                                },
                                {
                                    "link-type-name": "PointToPoint",
                                    "ospf-lsa-topology-link-metric": "100",
                                    "ospf-lsa-topology-link-node-id": "10.169.14.240",
                                    "ospf-lsa-topology-link-state": "Bidirectional",
                                },
                                {
                                    "link-type-name": "PointToPoint",
                                    "ospf-lsa-topology-link-metric": "5",
                                    "ospf-lsa-topology-link-node-id": "10.34.2.251",
                                    "ospf-lsa-topology-link-state": "Bidirectional",
                                },
                            ],
                            "ospf-topology-id": "0",
                            "ospf-topology-name": "default",
                        },
                    },
                    "sequence-number": "0x8000205a",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "858",
                    "checksum": "0x1022",
                    "lsa-id": "10.34.2.251",
                    "lsa-length": "108",
                    "lsa-type": "Router",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:45:42"},
                        "expiration-time": {"#text": "00:45:42"},
                        "installation-time": {"#text": "00:14:09"},
                        "lsa-change-count": "1258",
                        "lsa-changed-time": {"#text": "2w0d 00:51:22"},
                        "send-time": {"#text": "00:14:07"},
                    },
                    "ospf-router-lsa": {
                        "bits": "0x2",
                        "link-count": "7",
                        "ospf-link": [
                            {
                                "link-data": "10.34.2.202",
                                "link-id": "10.34.2.250",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "5",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.34.2.202",
                                "link-id": "10.34.2.250",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "5",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.34.2.200",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "5",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.34.2.200",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "5",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.169.14.34",
                                "link-id": "10.169.14.241",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "120",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.169.14.34",
                                "link-id": "10.169.14.241",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "120",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.169.14.32",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "120",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.169.14.32",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "120",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.169.196.217",
                                "link-id": "10.169.196.241",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.169.196.217",
                                "link-id": "10.169.196.241",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.169.196.216",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.169.196.216",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "10.34.2.251",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "0",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "10.34.2.251",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "0",
                                "ospf-topology-count": "0",
                            },
                        ],
                        "ospf-lsa-topology": {
                            "ospf-lsa-topology-link": [
                                {
                                    "link-type-name": "PointToPoint",
                                    "ospf-lsa-topology-link-metric": "1000",
                                    "ospf-lsa-topology-link-node-id": "10.169.196.241",
                                    "ospf-lsa-topology-link-state": "Bidirectional",
                                },
                                {
                                    "link-type-name": "PointToPoint",
                                    "ospf-lsa-topology-link-metric": "120",
                                    "ospf-lsa-topology-link-node-id": "10.169.14.241",
                                    "ospf-lsa-topology-link-state": "Bidirectional",
                                },
                                {
                                    "link-type-name": "PointToPoint",
                                    "ospf-lsa-topology-link-metric": "5",
                                    "ospf-lsa-topology-link-node-id": "10.34.2.250",
                                    "ospf-lsa-topology-link-state": "Bidirectional",
                                },
                            ],
                            "ospf-topology-id": "0",
                            "ospf-topology-name": "default",
                        },
                    },
                    "sequence-number": "0x80001dde",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "1718",
                    "checksum": "0x1e4",
                    "lsa-id": "10.1.0.4",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:31:21"},
                        "expiration-time": {"#text": "00:31:22"},
                        "installation-time": {"#text": "00:28:32"},
                        "lsa-change-count": "5",
                        "lsa-changed-time": {"#text": "3w0d 08:18:02"},
                        "send-time": {"#text": "00:28:30"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.169.14.240",
                                "10.169.14.158",
                                "10.169.14.157",
                                "100",
                                "1000Mbps",
                                "1000Mbps",
                                "Priority "
                                "0, "
                                "1000Mbps\n"
                                "Priority "
                                "1, "
                                "1000Mbps\n"
                                "Priority "
                                "2, "
                                "1000Mbps\n"
                                "Priority "
                                "3, "
                                "1000Mbps\n"
                                "Priority "
                                "4, "
                                "1000Mbps\n"
                                "Priority "
                                "5, "
                                "1000Mbps\n"
                                "Priority "
                                "6, "
                                "1000Mbps\n"
                                "Priority "
                                "7, "
                                "1000Mbps\n",
                                "Local 334, Remote 0",
                                "4",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "32",
                                "8",
                                "4",
                            ],
                            "tlv-type-name": [
                                "Linktype",
                                "LinkID",
                                "LocIfAdr",
                                "RemIfAdr",
                                "TEMetric",
                                "MaxBW",
                                "MaxRsvBW",
                                "UnRsvBW",
                                "LinkLocalRemoteIdentifier",
                                "Color",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "6",
                                "7",
                                "8",
                                "11",
                                "9",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "112",
                            "tlv-type-name": "Link",
                            "tlv-type-value": "2",
                        },
                    },
                    "sequence-number": "0x8000029e",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "1517",
                    "checksum": "0x29c0",
                    "lsa-id": "10.1.0.4",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:34:43"},
                        "expiration-time": {"#text": "00:34:43"},
                        "installation-time": {"#text": "00:25:08"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "3w0d 08:09:50"},
                        "send-time": {"#text": "00:25:06"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.169.14.241",
                                "10.169.14.34",
                                "10.169.14.33",
                                "90",
                                "1000Mbps",
                                "1000Mbps",
                                "Priority "
                                "0, "
                                "1000Mbps\n"
                                "Priority "
                                "1, "
                                "1000Mbps\n"
                                "Priority "
                                "2, "
                                "1000Mbps\n"
                                "Priority "
                                "3, "
                                "1000Mbps\n"
                                "Priority "
                                "4, "
                                "1000Mbps\n"
                                "Priority "
                                "5, "
                                "1000Mbps\n"
                                "Priority "
                                "6, "
                                "1000Mbps\n"
                                "Priority "
                                "7, "
                                "1000Mbps\n",
                                "Local 334, Remote 0",
                                "6",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "32",
                                "8",
                                "4",
                            ],
                            "tlv-type-name": [
                                "Linktype",
                                "LinkID",
                                "LocIfAdr",
                                "RemIfAdr",
                                "TEMetric",
                                "MaxBW",
                                "MaxRsvBW",
                                "UnRsvBW",
                                "LinkLocalRemoteIdentifier",
                                "Color",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "6",
                                "7",
                                "8",
                                "11",
                                "9",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "112",
                            "tlv-type-name": "Link",
                            "tlv-type-value": "2",
                        },
                    },
                    "sequence-number": "0x80000299",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "1529",
                    "checksum": "0xb606",
                    "lsa-id": "10.1.0.4",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:34:31"},
                        "expiration-time": {"#text": "00:34:31"},
                        "installation-time": {"#text": "00:25:26"},
                        "lsa-change-count": "6",
                        "lsa-changed-time": {"#text": "3w3d 07:23:05"},
                        "send-time": {"#text": "00:25:24"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.189.5.252",
                                "10.169.14.121",
                                "10.169.14.122",
                                "100",
                                "1000Mbps",
                                "1000Mbps",
                                "Priority "
                                "0, "
                                "1000Mbps\n"
                                "Priority "
                                "1, "
                                "1000Mbps\n"
                                "Priority "
                                "2, "
                                "1000Mbps\n"
                                "Priority "
                                "3, "
                                "1000Mbps\n"
                                "Priority "
                                "4, "
                                "1000Mbps\n"
                                "Priority "
                                "5, "
                                "1000Mbps\n"
                                "Priority "
                                "6, "
                                "1000Mbps\n"
                                "Priority "
                                "7, "
                                "1000Mbps\n",
                                "Local 334, Remote 0",
                                "10",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "32",
                                "8",
                                "4",
                            ],
                            "tlv-type-name": [
                                "Linktype",
                                "LinkID",
                                "LocIfAdr",
                                "RemIfAdr",
                                "TEMetric",
                                "MaxBW",
                                "MaxRsvBW",
                                "UnRsvBW",
                                "LinkLocalRemoteIdentifier",
                                "Color",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "6",
                                "7",
                                "8",
                                "11",
                                "9",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "112",
                            "tlv-type-name": "Link",
                            "tlv-type-value": "2",
                        },
                    },
                    "sequence-number": "0x800003f8",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "2418",
                    "checksum": "0x694d",
                    "lsa-id": "10.1.0.4",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:19:42"},
                        "expiration-time": {"#text": "00:19:42"},
                        "installation-time": {"#text": "00:40:12"},
                        "lsa-change-count": "35",
                        "lsa-changed-time": {"#text": "3w3d 07:23:04"},
                        "send-time": {"#text": "00:40:10"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.189.5.253",
                                "10.169.14.129",
                                "10.169.14.130",
                                "70",
                                "1000Mbps",
                                "1000Mbps",
                                "Priority "
                                "0, "
                                "1000Mbps\n"
                                "Priority "
                                "1, "
                                "1000Mbps\n"
                                "Priority "
                                "2, "
                                "1000Mbps\n"
                                "Priority "
                                "3, "
                                "1000Mbps\n"
                                "Priority "
                                "4, "
                                "1000Mbps\n"
                                "Priority "
                                "5, "
                                "1000Mbps\n"
                                "Priority "
                                "6, "
                                "1000Mbps\n"
                                "Priority "
                                "7, "
                                "1000Mbps\n",
                                "Local 334, Remote 0",
                                "6",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "32",
                                "8",
                                "4",
                            ],
                            "tlv-type-name": [
                                "Linktype",
                                "LinkID",
                                "LocIfAdr",
                                "RemIfAdr",
                                "TEMetric",
                                "MaxBW",
                                "MaxRsvBW",
                                "UnRsvBW",
                                "LinkLocalRemoteIdentifier",
                                "Color",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "6",
                                "7",
                                "8",
                                "11",
                                "9",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "112",
                            "tlv-type-name": "Link",
                            "tlv-type-value": "2",
                        },
                    },
                    "sequence-number": "0x800013fe",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "2702",
                    "checksum": "0xb804",
                    "lsa-id": "10.1.0.4",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:14:58"},
                        "expiration-time": {"#text": "00:14:58"},
                        "generation-timer": {"#text": "00:00:19"},
                        "installation-time": {"#text": "00:45:02"},
                        "lsa-change-count": "3",
                        "lsa-changed-time": {"#text": "3w3d 07:23:03"},
                        "send-time": {"#text": "00:45:00"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.169.14.240",
                                "10.169.14.122",
                                "10.169.14.121",
                                "100",
                                "1000Mbps",
                                "1000Mbps",
                                "Priority "
                                "0, "
                                "1000Mbps\n"
                                "Priority "
                                "1, "
                                "1000Mbps\n"
                                "Priority "
                                "2, "
                                "1000Mbps\n"
                                "Priority "
                                "3, "
                                "1000Mbps\n"
                                "Priority "
                                "4, "
                                "1000Mbps\n"
                                "Priority "
                                "5, "
                                "1000Mbps\n"
                                "Priority "
                                "6, "
                                "1000Mbps\n"
                                "Priority "
                                "7, "
                                "1000Mbps\n",
                                "Local 334, Remote 0",
                                "10",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "32",
                                "8",
                                "4",
                            ],
                            "tlv-type-name": [
                                "Linktype",
                                "LinkID",
                                "LocIfAdr",
                                "RemIfAdr",
                                "TEMetric",
                                "MaxBW",
                                "MaxRsvBW",
                                "UnRsvBW",
                                "LinkLocalRemoteIdentifier",
                                "Color",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "6",
                                "7",
                                "8",
                                "11",
                                "9",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "112",
                            "tlv-type-name": "Link",
                            "tlv-type-value": "2",
                        },
                    },
                    "our-entry": True,
                    "sequence-number": "0x800013e8",
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "209",
                    "checksum": "0x4cd0",
                    "lsa-id": "10.1.0.4",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:56:31"},
                        "expiration-time": {"#text": "00:56:31"},
                        "installation-time": {"#text": "00:03:26"},
                        "lsa-change-count": "15",
                        "lsa-changed-time": {"#text": "3w3d 07:23:04"},
                        "send-time": {"#text": "00:03:24"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.169.14.241",
                                "10.169.14.130",
                                "10.169.14.129",
                                "70",
                                "1000Mbps",
                                "1000Mbps",
                                "Priority "
                                "0, "
                                "1000Mbps\n"
                                "Priority "
                                "1, "
                                "1000Mbps\n"
                                "Priority "
                                "2, "
                                "1000Mbps\n"
                                "Priority "
                                "3, "
                                "1000Mbps\n"
                                "Priority "
                                "4, "
                                "1000Mbps\n"
                                "Priority "
                                "5, "
                                "1000Mbps\n"
                                "Priority "
                                "6, "
                                "1000Mbps\n"
                                "Priority "
                                "7, "
                                "1000Mbps\n",
                                "Local 334, Remote 0",
                                "6",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "32",
                                "8",
                                "4",
                            ],
                            "tlv-type-name": [
                                "Linktype",
                                "LinkID",
                                "LocIfAdr",
                                "RemIfAdr",
                                "TEMetric",
                                "MaxBW",
                                "MaxRsvBW",
                                "UnRsvBW",
                                "LinkLocalRemoteIdentifier",
                                "Color",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "6",
                                "7",
                                "8",
                                "11",
                                "9",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "112",
                            "tlv-type-name": "Link",
                            "tlv-type-value": "2",
                        },
                    },
                    "sequence-number": "0x80000f9c",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "580",
                    "checksum": "0x5e9d",
                    "lsa-id": "10.1.0.5",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:50:20"},
                        "expiration-time": {"#text": "00:50:20"},
                        "installation-time": {"#text": "00:09:34"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "2w0d 00:51:24"},
                        "send-time": {"#text": "00:09:32"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.169.196.241",
                                "10.169.196.213",
                                "10.169.196.214",
                                "1000",
                                "1000Mbps",
                                "1000Mbps",
                                "Priority "
                                "0, "
                                "1000Mbps\n"
                                "Priority "
                                "1, "
                                "1000Mbps\n"
                                "Priority "
                                "2, "
                                "1000Mbps\n"
                                "Priority "
                                "3, "
                                "1000Mbps\n"
                                "Priority "
                                "4, "
                                "1000Mbps\n"
                                "Priority "
                                "5, "
                                "1000Mbps\n"
                                "Priority "
                                "6, "
                                "1000Mbps\n"
                                "Priority "
                                "7, "
                                "1000Mbps\n",
                                "Local 337, Remote 0",
                                "2",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "32",
                                "8",
                                "4",
                            ],
                            "tlv-type-name": [
                                "Linktype",
                                "LinkID",
                                "LocIfAdr",
                                "RemIfAdr",
                                "TEMetric",
                                "MaxBW",
                                "MaxRsvBW",
                                "UnRsvBW",
                                "LinkLocalRemoteIdentifier",
                                "Color",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "6",
                                "7",
                                "8",
                                "11",
                                "9",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "112",
                            "tlv-type-name": "Link",
                            "tlv-type-value": "2",
                        },
                    },
                    "sequence-number": "0x800001b5",
                },
                {
                    "advertising-router": "10.100.5.5",
                    "age": "1760",
                    "checksum": "0x6c5a",
                    "lsa-id": "10.49.0.1",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:30:40"},
                        "expiration-time": {"#text": "00:30:40"},
                        "installation-time": {"#text": "00:29:13"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "21w5d 22:48:11"},
                        "send-time": {"#text": "00:29:11"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "32",
                                "0",
                                "0x40",
                                "10.100.5.5",
                                "0x00",
                                "0",
                                "0",
                                "1000",
                            ],
                            "tlv-length": [
                                "1",
                                "1",
                                "1",
                                "1",
                                "32",
                                "8",
                                "1",
                                "1",
                                "1",
                                "4",
                            ],
                            "tlv-type-name": [
                                "Route Type",
                                "Prefix Length",
                                "AF",
                                "Flags",
                                "Prefix",
                                "Prefix Sid",
                                "Flags",
                                "MT ID",
                                "Algorithm",
                                "SID",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "20",
                            "tlv-type-name": "Extended Prefix",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x800019ac",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "1027",
                    "checksum": "0x7fa7",
                    "lsa-id": "10.49.0.1",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:42:53"},
                        "expiration-time": {"#text": "00:42:53"},
                        "installation-time": {"#text": "00:17:01"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "30w0d 01:32:34"},
                        "send-time": {"#text": "00:16:59"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "32",
                                "0",
                                "0x40",
                                "10.34.2.250",
                                "0x00",
                                "0",
                                "0",
                                "61",
                            ],
                            "tlv-length": [
                                "1",
                                "1",
                                "1",
                                "1",
                                "32",
                                "8",
                                "1",
                                "1",
                                "1",
                                "4",
                            ],
                            "tlv-type-name": [
                                "Route Type",
                                "Prefix Length",
                                "AF",
                                "Flags",
                                "Prefix",
                                "Prefix Sid",
                                "Flags",
                                "MT ID",
                                "Algorithm",
                                "SID",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "20",
                            "tlv-type-name": "Extended Prefix",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x80001fa9",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "858",
                    "checksum": "0x6ce",
                    "lsa-id": "10.49.0.1",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:45:42"},
                        "expiration-time": {"#text": "00:45:42"},
                        "installation-time": {"#text": "00:14:09"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "30w0d 01:32:36"},
                        "send-time": {"#text": "00:14:07"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "32",
                                "0",
                                "0x40",
                                "10.34.2.251",
                                "0x00",
                                "0",
                                "0",
                                "62",
                            ],
                            "tlv-length": [
                                "1",
                                "1",
                                "1",
                                "1",
                                "32",
                                "8",
                                "1",
                                "1",
                                "1",
                                "4",
                            ],
                            "tlv-type-name": [
                                "Route Type",
                                "Prefix Length",
                                "AF",
                                "Flags",
                                "Prefix",
                                "Prefix Sid",
                                "Flags",
                                "MT ID",
                                "Algorithm",
                                "SID",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "20",
                            "tlv-type-name": "Extended Prefix",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x80001cfb",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "173",
                    "checksum": "0x97ab",
                    "lsa-id": "10.49.0.1",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:57:06"},
                        "expiration-time": {"#text": "00:57:07"},
                        "installation-time": {"#text": "00:02:50"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "30w0d 01:32:37"},
                        "send-time": {"#text": "00:02:48"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "32",
                                "0",
                                "0x40",
                                "10.169.14.240",
                                "0x00",
                                "0",
                                "0",
                                "51",
                            ],
                            "tlv-length": [
                                "1",
                                "1",
                                "1",
                                "1",
                                "32",
                                "8",
                                "1",
                                "1",
                                "1",
                                "4",
                            ],
                            "tlv-type-name": [
                                "Route Type",
                                "Prefix Length",
                                "AF",
                                "Flags",
                                "Prefix",
                                "Prefix Sid",
                                "Flags",
                                "MT ID",
                                "Algorithm",
                                "SID",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "20",
                            "tlv-type-name": "Extended Prefix",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x80001bc2",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "1759",
                    "checksum": "0x6433",
                    "lsa-id": "10.49.0.1",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:30:41"},
                        "expiration-time": {"#text": "00:30:41"},
                        "installation-time": {"#text": "00:29:13"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "30w0d 01:32:36"},
                        "send-time": {"#text": "00:29:11"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "32",
                                "0",
                                "0x40",
                                "10.169.14.241",
                                "0x00",
                                "0",
                                "0",
                                "52",
                            ],
                            "tlv-length": [
                                "1",
                                "1",
                                "1",
                                "1",
                                "32",
                                "8",
                                "1",
                                "1",
                                "1",
                                "4",
                            ],
                            "tlv-type-name": [
                                "Route Type",
                                "Prefix Length",
                                "AF",
                                "Flags",
                                "Prefix",
                                "Prefix Sid",
                                "Flags",
                                "MT ID",
                                "Algorithm",
                                "SID",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "20",
                            "tlv-type-name": "Extended Prefix",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x80001f67",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "1899",
                    "checksum": "0x8c7f",
                    "lsa-id": "10.49.0.1",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:28:20"},
                        "expiration-time": {"#text": "00:28:21"},
                        "generation-timer": {"#text": "00:18:20"},
                        "installation-time": {"#text": "00:31:39"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "30w0d 01:46:13"},
                        "send-time": {"#text": "00:31:37"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "32",
                                "0",
                                "0x40",
                                "10.189.5.252",
                                "0x00",
                                "0",
                                "0",
                                "71",
                            ],
                            "tlv-length": [
                                "1",
                                "1",
                                "1",
                                "1",
                                "32",
                                "8",
                                "1",
                                "1",
                                "1",
                                "4",
                            ],
                            "tlv-type-name": [
                                "Route Type",
                                "Prefix Length",
                                "AF",
                                "Flags",
                                "Prefix",
                                "Prefix Sid",
                                "Flags",
                                "MT ID",
                                "Algorithm",
                                "SID",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "20",
                            "tlv-type-name": "Extended Prefix",
                            "tlv-type-value": "1",
                        },
                    },
                    "our-entry": True,
                    "sequence-number": "0x80001b9e",
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "1980",
                    "checksum": "0xe3bf",
                    "lsa-id": "10.49.0.1",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:26:59"},
                        "expiration-time": {"#text": "00:27:00"},
                        "installation-time": {"#text": "00:32:57"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "30w0d 01:32:43"},
                        "send-time": {"#text": "00:32:55"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "32",
                                "0",
                                "0x40",
                                "10.189.5.253",
                                "0x00",
                                "0",
                                "0",
                                "72",
                            ],
                            "tlv-length": [
                                "1",
                                "1",
                                "1",
                                "1",
                                "32",
                                "8",
                                "1",
                                "1",
                                "1",
                                "4",
                            ],
                            "tlv-type-name": [
                                "Route Type",
                                "Prefix Length",
                                "AF",
                                "Flags",
                                "Prefix",
                                "Prefix Sid",
                                "Flags",
                                "MT ID",
                                "Algorithm",
                                "SID",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "20",
                            "tlv-type-name": "Extended Prefix",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x80001b04",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "367",
                    "checksum": "0x39a3",
                    "lsa-id": "10.64.0.1",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:53:53"},
                        "expiration-time": {"#text": "00:53:53"},
                        "installation-time": {"#text": "00:06:01"},
                        "lsa-change-count": "285",
                        "lsa-changed-time": {"#text": "2w0d 00:50:30"},
                        "send-time": {"#text": "00:05:59"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.34.2.251",
                                "10.34.2.201",
                                "0xe0",
                                "0",
                                "0",
                                "142149",
                                "0x60",
                                "0",
                                "0",
                                "142150",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x800004f9",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "1016",
                    "checksum": "0x7002",
                    "lsa-id": "10.64.0.1",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:43:04"},
                        "expiration-time": {"#text": "00:43:04"},
                        "installation-time": {"#text": "00:16:50"},
                        "lsa-change-count": "50",
                        "lsa-changed-time": {"#text": "2w6d 19:46:47"},
                        "send-time": {"#text": "00:16:48"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.169.14.240",
                                "10.169.14.18",
                                "0xe0",
                                "0",
                                "0",
                                "37408",
                                "0x60",
                                "0",
                                "0",
                                "37409",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x80000311",
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "2521",
                    "checksum": "0x6915",
                    "lsa-id": "10.64.0.1",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:17:59"},
                        "expiration-time": {"#text": "00:17:59"},
                        "installation-time": {"#text": "00:41:58"},
                        "lsa-change-count": "31",
                        "lsa-changed-time": {"#text": "2w6d 20:01:45"},
                        "send-time": {"#text": "00:41:56"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.169.14.241",
                                "10.169.14.130",
                                "0xe0",
                                "0",
                                "0",
                                "1912",
                                "0x60",
                                "0",
                                "0",
                                "1913",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x8000030a",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "790",
                    "checksum": "0x7271",
                    "lsa-id": "10.64.0.2",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:46:49"},
                        "expiration-time": {"#text": "00:46:50"},
                        "installation-time": {"#text": "00:13:04"},
                        "lsa-change-count": "47",
                        "lsa-changed-time": {"#text": "2w6d 18:58:08"},
                        "send-time": {"#text": "00:13:02"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.189.5.253",
                                "10.169.14.129",
                                "0xe0",
                                "0",
                                "0",
                                "1647",
                                "0x60",
                                "0",
                                "0",
                                "1648",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x80000305",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "565",
                    "checksum": "0x7248",
                    "lsa-id": "10.64.0.3",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:50:35"},
                        "expiration-time": {"#text": "00:50:35"},
                        "installation-time": {"#text": "00:09:19"},
                        "lsa-change-count": "7",
                        "lsa-changed-time": {"#text": "2w6d 18:14:24"},
                        "send-time": {"#text": "00:09:17"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.34.2.251",
                                "10.169.14.33",
                                "0xe0",
                                "0",
                                "0",
                                "1649",
                                "0x60",
                                "0",
                                "0",
                                "1650",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x8000029a",
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "947",
                    "checksum": "0x34eb",
                    "lsa-id": "10.64.0.3",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:44:13"},
                        "expiration-time": {"#text": "00:44:13"},
                        "installation-time": {"#text": "00:15:44"},
                        "lsa-change-count": "17",
                        "lsa-changed-time": {"#text": "2w0d 00:43:19"},
                        "send-time": {"#text": "00:15:42"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.189.5.252",
                                "10.189.5.94",
                                "0xe0",
                                "0",
                                "0",
                                "13988",
                                "0x60",
                                "0",
                                "0",
                                "13989",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x800002db",
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "2251",
                    "checksum": "0x31be",
                    "lsa-id": "10.64.0.4",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:22:29"},
                        "expiration-time": {"#text": "00:22:29"},
                        "installation-time": {"#text": "00:37:28"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "2w0d 00:51:02"},
                        "send-time": {"#text": "00:37:26"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.19.198.239",
                                "10.19.198.29",
                                "0xe0",
                                "0",
                                "0",
                                "102794",
                                "0x60",
                                "0",
                                "0",
                                "102795",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x800001bb",
                },
                {
                    "advertising-router": "10.100.5.5",
                    "age": "1760",
                    "checksum": "0x4de2",
                    "lsa-id": "10.64.0.6",
                    "lsa-length": "56",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:30:40"},
                        "expiration-time": {"#text": "00:30:40"},
                        "installation-time": {"#text": "00:29:13"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "21w5d 22:48:11"},
                        "send-time": {"#text": "00:29:11"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.34.2.250",
                                "10.16.0.2",
                                "0x60",
                                "0",
                                "0",
                                "24000",
                                "0x60",
                                "0",
                                "0",
                                "24000",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "4",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Invalid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "32768",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "32",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x800019bf",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "2871",
                    "checksum": "0xb9a6",
                    "lsa-id": "10.64.0.7",
                    "lsa-length": "48",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:12:09"},
                        "expiration-time": {"#text": "00:12:09"},
                        "installation-time": {"#text": "00:47:45"},
                        "lsa-change-count": "123",
                        "lsa-changed-time": {"#text": "2w0d 00:42:10"},
                        "send-time": {"#text": "00:47:43"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.100.5.5",
                                "10.16.0.1",
                                "0xe0",
                                "0",
                                "0",
                                "207722",
                            ],
                            "tlv-length": ["1", "4", "4", "7", "1", "1", "1", "3"],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": ["1", "2", "3", "2", "1", "2", "3", "4"],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "24",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x8000046b",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "1297",
                    "checksum": "0x6a96",
                    "lsa-id": "10.64.0.7",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:38:23"},
                        "expiration-time": {"#text": "00:38:23"},
                        "installation-time": {"#text": "00:21:28"},
                        "lsa-change-count": "243",
                        "lsa-changed-time": {"#text": "2w6d 19:46:37"},
                        "send-time": {"#text": "00:21:26"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.34.2.250",
                                "10.34.2.202",
                                "0xe0",
                                "0",
                                "0",
                                "112778",
                                "0x60",
                                "0",
                                "0",
                                "112779",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x800004de",
                },
                {
                    "advertising-router": "10.19.198.239",
                    "age": "913",
                    "checksum": "0xb34a",
                    "lsa-id": "10.64.0.17",
                    "lsa-length": "104",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:44:47"},
                        "expiration-time": {"#text": "00:44:47"},
                        "installation-time": {"#text": "00:15:12"},
                        "lsa-change-count": "2",
                        "lsa-changed-time": {"#text": "2w0d 00:51:03"},
                        "send-time": {"#text": "00:15:10"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.189.5.252",
                                "10.19.198.26",
                                "0x60",
                                "0",
                                "0",
                                "1730",
                                "0xe0",
                                "0",
                                "0",
                                "1729",
                                "0xe0",
                                "0",
                                "0",
                                "1729",
                                "0xe0",
                                "0",
                                "0",
                                "1729",
                                "0xe0",
                                "0",
                                "0",
                                "1729",
                                "0xe0",
                                "0",
                                "0",
                                "1729",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "4",
                                "1",
                                "1",
                                "1",
                                "3",
                                "4",
                                "1",
                                "1",
                                "1",
                                "3",
                                "8",
                                "1",
                                "1",
                                "1",
                                "3",
                                "12",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Invalid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Invalid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Invalid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Invalid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "8",
                                "1",
                                "2",
                                "3",
                                "4",
                                "32768",
                                "1",
                                "2",
                                "3",
                                "4",
                                "9",
                                "1",
                                "2",
                                "3",
                                "4",
                                "32769",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "80",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x8000025d",
                },
                {
                    "advertising-router": "10.169.196.241",
                    "age": "812",
                    "checksum": "0x3e3c",
                    "lsa-id": "10.64.0.17",
                    "lsa-length": "104",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:46:27"},
                        "expiration-time": {"#text": "00:46:28"},
                        "installation-time": {"#text": "00:13:25"},
                        "lsa-change-count": "2",
                        "lsa-changed-time": {"#text": "2w0d 00:51:24"},
                        "send-time": {"#text": "00:13:23"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.34.2.250",
                                "10.169.196.214",
                                "0x60",
                                "0",
                                "0",
                                "223815",
                                "0xe0",
                                "0",
                                "0",
                                "223843",
                                "0xe0",
                                "0",
                                "0",
                                "223843",
                                "0xe0",
                                "0",
                                "0",
                                "223843",
                                "0xe0",
                                "0",
                                "0",
                                "223843",
                                "0xe0",
                                "0",
                                "0",
                                "223843",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "4",
                                "1",
                                "1",
                                "1",
                                "3",
                                "4",
                                "1",
                                "1",
                                "1",
                                "3",
                                "8",
                                "1",
                                "1",
                                "1",
                                "3",
                                "12",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Invalid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Invalid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Invalid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Invalid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "8",
                                "1",
                                "2",
                                "3",
                                "4",
                                "32768",
                                "1",
                                "2",
                                "3",
                                "4",
                                "9",
                                "1",
                                "2",
                                "3",
                                "4",
                                "32769",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "80",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x8000025d",
                },
                {
                    "advertising-router": "10.19.198.239",
                    "age": "913",
                    "checksum": "0xb938",
                    "lsa-id": "10.64.0.18",
                    "lsa-length": "104",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:44:47"},
                        "expiration-time": {"#text": "00:44:47"},
                        "installation-time": {"#text": "00:15:12"},
                        "lsa-change-count": "2",
                        "lsa-changed-time": {"#text": "2w0d 00:51:02"},
                        "send-time": {"#text": "00:15:10"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.189.5.253",
                                "10.19.198.30",
                                "0x60",
                                "0",
                                "0",
                                "1728",
                                "0xe0",
                                "0",
                                "0",
                                "1727",
                                "0xe0",
                                "0",
                                "0",
                                "1727",
                                "0xe0",
                                "0",
                                "0",
                                "1727",
                                "0xe0",
                                "0",
                                "0",
                                "1727",
                                "0xe0",
                                "0",
                                "0",
                                "1727",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "4",
                                "1",
                                "1",
                                "1",
                                "3",
                                "4",
                                "1",
                                "1",
                                "1",
                                "3",
                                "8",
                                "1",
                                "1",
                                "1",
                                "3",
                                "12",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Invalid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Invalid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Invalid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Invalid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "8",
                                "1",
                                "2",
                                "3",
                                "4",
                                "32768",
                                "1",
                                "2",
                                "3",
                                "4",
                                "9",
                                "1",
                                "2",
                                "3",
                                "4",
                                "32769",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "80",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x8000025d",
                },
                {
                    "advertising-router": "10.169.196.241",
                    "age": "812",
                    "checksum": "0x6fdb",
                    "lsa-id": "10.64.0.18",
                    "lsa-length": "104",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:46:27"},
                        "expiration-time": {"#text": "00:46:28"},
                        "installation-time": {"#text": "00:13:25"},
                        "lsa-change-count": "2",
                        "lsa-changed-time": {"#text": "2w0d 00:51:22"},
                        "send-time": {"#text": "00:13:23"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.34.2.251",
                                "10.169.196.218",
                                "0x60",
                                "0",
                                "0",
                                "223844",
                                "0xe0",
                                "0",
                                "0",
                                "223845",
                                "0xe0",
                                "0",
                                "0",
                                "223845",
                                "0xe0",
                                "0",
                                "0",
                                "223845",
                                "0xe0",
                                "0",
                                "0",
                                "223845",
                                "0xe0",
                                "0",
                                "0",
                                "223845",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "4",
                                "1",
                                "1",
                                "1",
                                "3",
                                "4",
                                "1",
                                "1",
                                "1",
                                "3",
                                "8",
                                "1",
                                "1",
                                "1",
                                "3",
                                "12",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Invalid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Invalid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Invalid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Invalid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "8",
                                "1",
                                "2",
                                "3",
                                "4",
                                "32768",
                                "1",
                                "2",
                                "3",
                                "4",
                                "9",
                                "1",
                                "2",
                                "3",
                                "4",
                                "32769",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "80",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x8000025d",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "114",
                    "checksum": "0xe70a",
                    "lsa-id": "10.64.0.31",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:58:06"},
                        "expiration-time": {"#text": "00:58:06"},
                        "installation-time": {"#text": "00:01:47"},
                        "lsa-change-count": "8",
                        "lsa-changed-time": {"#text": "2w0d 00:43:41"},
                        "send-time": {"#text": "00:01:45"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.169.14.241",
                                "10.169.14.34",
                                "0xe0",
                                "0",
                                "0",
                                "15022",
                                "0x60",
                                "0",
                                "0",
                                "15023",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x8000029b",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "1078",
                    "checksum": "0xe396",
                    "lsa-id": "10.64.0.32",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:42:02"},
                        "expiration-time": {"#text": "00:42:02"},
                        "installation-time": {"#text": "00:17:50"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "2w0d 00:51:22"},
                        "send-time": {"#text": "00:17:48"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.169.196.241",
                                "10.169.196.217",
                                "0xe0",
                                "0",
                                "0",
                                "259074",
                                "0x60",
                                "0",
                                "0",
                                "259075",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x800001b5",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "1949",
                    "checksum": "0xffb8",
                    "lsa-id": "10.64.0.37",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:27:31"},
                        "expiration-time": {"#text": "00:27:31"},
                        "installation-time": {"#text": "00:32:23"},
                        "lsa-change-count": "7",
                        "lsa-changed-time": {"#text": "2w0d 00:27:01"},
                        "send-time": {"#text": "00:32:21"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.169.14.240",
                                "10.169.14.158",
                                "0xe0",
                                "0",
                                "0",
                                "143642",
                                "0x60",
                                "0",
                                "0",
                                "143643",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x8000029b",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "1257",
                    "checksum": "0x71b3",
                    "lsa-id": "10.64.0.38",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:39:02"},
                        "expiration-time": {"#text": "00:39:03"},
                        "installation-time": {"#text": "00:20:51"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "2w0d 00:51:24"},
                        "send-time": {"#text": "00:20:49"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.169.196.241",
                                "10.169.196.213",
                                "0xe0",
                                "0",
                                "0",
                                "358249",
                                "0x60",
                                "0",
                                "0",
                                "358250",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x800001b5",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "792",
                    "checksum": "0x7efa",
                    "lsa-id": "10.64.0.52",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:46:48"},
                        "expiration-time": {"#text": "00:46:48"},
                        "generation-timer": {"#text": "00:36:39"},
                        "installation-time": {"#text": "00:13:12"},
                        "lsa-change-count": "25",
                        "lsa-changed-time": {"#text": "2w0d 00:37:11"},
                        "send-time": {"#text": "00:13:10"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.169.14.240",
                                "10.169.14.122",
                                "0xe0",
                                "0",
                                "0",
                                "2567",
                                "0x60",
                                "0",
                                "0",
                                "2568",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "our-entry": True,
                    "sequence-number": "0x80000308",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "1333",
                    "checksum": "0x1839",
                    "lsa-id": "10.64.0.54",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:37:47"},
                        "expiration-time": {"#text": "00:37:47"},
                        "generation-timer": {"#text": "00:27:30"},
                        "installation-time": {"#text": "00:22:13"},
                        "lsa-change-count": "26",
                        "lsa-changed-time": {"#text": "2w0d 00:46:13"},
                        "send-time": {"#text": "00:22:11"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.189.5.253",
                                "10.189.5.93",
                                "0xe0",
                                "0",
                                "0",
                                "28985",
                                "0x60",
                                "0",
                                "0",
                                "28986",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "our-entry": True,
                    "sequence-number": "0x800002dc",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "2167",
                    "checksum": "0x92eb",
                    "lsa-id": "10.64.0.55",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:23:53"},
                        "expiration-time": {"#text": "00:23:53"},
                        "generation-timer": {"#text": "00:09:20"},
                        "installation-time": {"#text": "00:36:07"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "2w0d 00:51:03"},
                        "send-time": {"#text": "00:36:05"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.19.198.239",
                                "10.19.198.25",
                                "0xe0",
                                "0",
                                "0",
                                "167966",
                                "0x60",
                                "0",
                                "0",
                                "167967",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "our-entry": True,
                    "sequence-number": "0x800001bb",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "1378",
                    "checksum": "0x7544",
                    "lsa-id": "10.64.0.57",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:37:01"},
                        "expiration-time": {"#text": "00:37:02"},
                        "installation-time": {"#text": "00:22:55"},
                        "lsa-change-count": "57",
                        "lsa-changed-time": {"#text": "2w6d 19:46:52"},
                        "send-time": {"#text": "00:22:53"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.169.14.241",
                                "10.169.14.17",
                                "0xe0",
                                "0",
                                "0",
                                "379383",
                                "0x60",
                                "0",
                                "0",
                                "379384",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x80000303",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "1680",
                    "checksum": "0x6d12",
                    "lsa-id": "10.64.0.59",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:32:00"},
                        "expiration-time": {"#text": "00:32:00"},
                        "installation-time": {"#text": "00:27:57"},
                        "lsa-change-count": "52",
                        "lsa-changed-time": {"#text": "3w1d 08:43:52"},
                        "send-time": {"#text": "00:27:55"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.189.5.252",
                                "10.169.14.121",
                                "0xe0",
                                "0",
                                "0",
                                "25",
                                "0x60",
                                "0",
                                "0",
                                "26",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x800002f4",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "1228",
                    "checksum": "0x4f1a",
                    "lsa-id": "10.64.0.60",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:39:32"},
                        "expiration-time": {"#text": "00:39:32"},
                        "installation-time": {"#text": "00:20:25"},
                        "lsa-change-count": "6",
                        "lsa-changed-time": {"#text": "2w6d 18:58:13"},
                        "send-time": {"#text": "00:20:23"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.34.2.250",
                                "10.169.14.157",
                                "0xe0",
                                "0",
                                "0",
                                "207596",
                                "0x60",
                                "0",
                                "0",
                                "207597",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x8000028b",
                },
                {
                    "advertising-router": "10.169.196.241",
                    "age": "326",
                    "checksum": "0xdcd1",
                    "lsa-id": "10.64.8.74",
                    "lsa-length": "92",
                    "lsa-type": "OpaqArea",
                    "options": "0x20",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:54:34"},
                        "expiration-time": {"#text": "00:54:34"},
                        "installation-time": {"#text": "00:05:21"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "1d 02:16:03"},
                        "send-time": {"#text": "00:05:19"},
                    },
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "10.36.3.3",
                                "192.168.111.2",
                                "0x60",
                                "0",
                                "0",
                                "223852",
                                "0x60",
                                "0",
                                "0",
                                "223852",
                                "0x60",
                                "0",
                                "0",
                                "223852",
                                "0x60",
                                "0",
                                "0",
                                "223852",
                                "0x60",
                                "0",
                                "0",
                                "223852",
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "7",
                                "1",
                                "1",
                                "1",
                                "3",
                                "4",
                                "1",
                                "1",
                                "1",
                                "3",
                                "4",
                                "1",
                                "1",
                                "1",
                                "3",
                                "8",
                                "1",
                                "1",
                                "1",
                                "3",
                                "12",
                                "1",
                                "1",
                                "1",
                                "3",
                            ],
                            "tlv-type-name": [
                                "Link Type",
                                "Link Id",
                                "Link Data",
                                "Adjacency Sid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Invalid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Invalid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Invalid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                                "Invalid",
                                "Flags",
                                "MT ID",
                                "Weight",
                                "Label",
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "2",
                                "1",
                                "2",
                                "3",
                                "4",
                                "8",
                                "1",
                                "2",
                                "3",
                                "4",
                                "32768",
                                "1",
                                "2",
                                "3",
                                "4",
                                "9",
                                "1",
                                "2",
                                "3",
                                "4",
                                "32769",
                                "1",
                                "2",
                                "3",
                                "4",
                            ],
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "68",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "sequence-number": "0x80000030",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "2614",
                    "checksum": "0x6715",
                    "lsa-id": "0.0.0.0",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:16:26"},
                        "expiration-time": {"#text": "00:16:26"},
                        "installation-time": {"#text": "00:43:25"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "30w0d 01:32:36"},
                        "send-time": {"#text": "00:43:23"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "0.0.0.0",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "1",
                            "ospf-topology-name": "default",
                            "tag": "0.0.0.0",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x800019e3",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "2282",
                    "checksum": "0x9fcc",
                    "lsa-id": "0.0.0.0",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:21:57"},
                        "expiration-time": {"#text": "00:21:58"},
                        "installation-time": {"#text": "00:37:59"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "4w2d 05:46:52"},
                        "send-time": {"#text": "00:37:57"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "0.0.0.0",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "1",
                            "ospf-topology-name": "default",
                            "tag": "0.0.0.0",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x8000039e",
                },
                {
                    "advertising-router": "192.168.36.119",
                    "age": "1219",
                    "checksum": "0x3bc3",
                    "lsa-id": "10.1.0.0",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x20",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:39:41"},
                        "expiration-time": {"#text": "00:39:41"},
                        "installation-time": {"#text": "00:20:15"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "21w6d 00:04:15"},
                        "send-time": {"#text": "00:20:13"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.0",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "20",
                            "ospf-topology-name": "default",
                            "tag": "0.0.0.0",
                            "type-value": "2",
                        },
                    },
                    "sequence-number": "0x800019b0",
                },
                {
                    "advertising-router": "192.168.36.120",
                    "age": "791",
                    "checksum": "0x33c9",
                    "lsa-id": "10.1.0.0",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x20",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:46:49"},
                        "expiration-time": {"#text": "00:46:49"},
                        "installation-time": {"#text": "00:13:07"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "21w6d 00:04:43"},
                        "send-time": {"#text": "00:13:05"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.0",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "20",
                            "ospf-topology-name": "default",
                            "tag": "0.0.0.0",
                            "type-value": "2",
                        },
                    },
                    "sequence-number": "0x800019b1",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "2132",
                    "checksum": "0xf161",
                    "lsa-id": "10.174.132.237",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:24:28"},
                        "expiration-time": {"#text": "00:24:28"},
                        "installation-time": {"#text": "00:35:29"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "4w2d 05:46:49"},
                        "send-time": {"#text": "00:35:27"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "50",
                            "ospf-topology-name": "default",
                            "tag": "0.0.0.0",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x8000039e",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "2734",
                    "checksum": "0x473e",
                    "lsa-id": "10.34.2.250",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:14:26"},
                        "expiration-time": {"#text": "00:14:26"},
                        "installation-time": {"#text": "00:45:31"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "3w0d 08:49:51"},
                        "send-time": {"#text": "00:45:29"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "50",
                            "ospf-topology-name": "default",
                            "tag": "10.166.34.12",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x80000288",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "2637",
                    "checksum": "0x2153",
                    "lsa-id": "10.34.2.250",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:16:03"},
                        "expiration-time": {"#text": "00:16:03"},
                        "installation-time": {"#text": "00:43:51"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "3w0d 08:09:51"},
                        "send-time": {"#text": "00:43:49"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "50",
                            "ospf-topology-name": "default",
                            "tag": "10.166.34.12",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x80000298",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "475",
                    "checksum": "0x3b48",
                    "lsa-id": "10.34.2.251",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:52:05"},
                        "expiration-time": {"#text": "00:52:05"},
                        "installation-time": {"#text": "00:07:52"},
                        "lsa-change-count": "1",
                        "lsa-changed-time": {"#text": "3w0d 08:49:56"},
                        "send-time": {"#text": "00:07:50"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "50",
                            "ospf-topology-name": "default",
                            "tag": "10.166.34.12",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x80000289",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "1077",
                    "checksum": "0xfb51",
                    "lsa-id": "192.168.100.0",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:42:03"},
                        "expiration-time": {"#text": "00:42:03"},
                        "installation-time": {"#text": "00:17:54"},
                        "lsa-change-count": "75",
                        "lsa-changed-time": {"#text": "2w6d 18:58:13"},
                        "send-time": {"#text": "00:17:52"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.128",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "31900",
                            "ospf-topology-name": "default",
                            "tag": "10.76.212.52",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x800002da",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "927",
                    "checksum": "0x19b8",
                    "lsa-id": "192.168.100.252",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:44:33"},
                        "expiration-time": {"#text": "00:44:33"},
                        "installation-time": {"#text": "00:15:24"},
                        "lsa-change-count": "75",
                        "lsa-changed-time": {"#text": "2w6d 18:58:13"},
                        "send-time": {"#text": "00:15:22"},
                    },
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "31900",
                            "ospf-topology-name": "default",
                            "tag": "10.76.212.52",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x800002d9",
                },
            ],
        }
    }
    golden_parsed_output_1 = {
        "ospf-database-information": {
            "ospf-area-header": {"ospf-area": "0.0.0.8"},
            "ospf-database": [
                {
                    "advertising-router": "10.34.2.250",
                    "age": "1107",
                    "checksum": "0x29f7",
                    "lsa-id": "10.34.2.250",
                    "lsa-length": "60",
                    "lsa-type": "Router",
                    "options": "0x22",
                    "ospf-database-extensive": {
                        "aging-timer": {"#text": "00:41:32"},
                        "expiration-time": {"#text": "00:41:33"},
                        "installation-time": {"#text": "00:18:24"},
                        "lsa-change-count": "2",
                        "lsa-changed-time": {"#text": "00:18:53"},
                    },
                    "ospf-router-lsa": {
                        "bits": "0x0",
                        "link-count": "3",
                        "ospf-link": [
                            {
                                "link-data": "10.169.14.158",
                                "link-id": "10.169.14.240",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.169.14.158",
                                "link-id": "10.169.14.240",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.169.14.156",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.169.14.156",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "10.34.2.250",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "0",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "10.34.2.250",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "0",
                                "ospf-topology-count": "0",
                            },
                        ],
                        "ospf-lsa-topology": {
                            "ospf-lsa-topology-link": [
                                {
                                    "link-type-name": "PointToPoint",
                                    "ospf-lsa-topology-link-metric": "1",
                                    "ospf-lsa-topology-link-node-id": "10.169.14.240",
                                    "ospf-lsa-topology-link-state": "Bidirectional",
                                }
                            ],
                            "ospf-topology-id": "0",
                            "ospf-topology-name": "default",
                        },
                    },
                    "sequence-number": "0x80000003",
                },
            ],
        }
    }


    golden_output_2={
        "execute.return_value": """
        show ospf database extensive 
            OSPF database, Area 0.0.0.0
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len 
        Router   1.1.1.1          1.1.1.1          0x80000005    14  0x22 0x9f32  48
        bits 0x2, link count 2
        id 30.0.0.2, data 30.0.0.1, Type Transit (2)
            Topology count: 0, Default metric: 1
        id 1.1.1.1, data 255.255.255.255, Type Stub (3)
            Topology count: 0, Default metric: 0
        Topology default (ID 0)
            Type: Transit, Node ID: 30.0.0.2
            Metric: 1, Bidirectional
        Aging timer 00:59:46
        Installed 00:00:11 ago, expires in 00:59:46
        Last changed 00:00:11 ago, Change count: 3
        Router  *3.3.3.3          3.3.3.3          0x80000003    99  0x22 0xb705  48
        bits 0x0, link count 2
        id 30.0.0.2, data 30.0.0.2, Type Transit (2)
            Topology count: 0, Default metric: 1
        id 3.3.3.3, data 255.255.255.255, Type Stub (3)
            Topology count: 0, Default metric: 0
        Topology default (ID 0)
            Type: Transit, Node ID: 30.0.0.2
            Metric: 1, Bidirectional
        Gen timer 00:48:21
        Aging timer 00:58:21
        Installed 00:01:39 ago, expires in 00:58:21, sent 00:01:37 ago
        Last changed 00:01:39 ago, Change count: 2, Ours
        Network *30.0.0.2         3.3.3.3          0x80000001   104  0x22 0x42bb  32
        mask 255.255.255.0
        attached router 3.3.3.3
        attached router 1.1.1.1
        Topology default (ID 0)
            Type: Transit, Node ID: 1.1.1.1
            Metric: 0, Bidirectional
            Type: Transit, Node ID: 3.3.3.3
            Metric: 0, Bidirectional
        Gen timer 00:48:16
        Aging timer 00:58:16
        Installed 00:01:44 ago, expires in 00:58:16, sent 00:01:42 ago
        Last changed 00:01:44 ago, Change count: 1, Ours
            OSPF AS SCOPE link state database
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len 
        Extern   11.11.11.11      1.1.1.1          0x80000001    14  0x22 0xe69b  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 2, Metric: 0, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
        Aging timer 00:59:46
        Installed 00:00:11 ago, expires in 00:59:46
        Last changed 00:00:11 ago, Change count: 1
  """
    }

    golden_parsed_output_2 = {
        "ospf-database-information": {
        "ospf-area-header": {
            "ospf-area": "0.0.0.0"
        },
        "ospf-database": [
            {
                "advertising-router": "1.1.1.1",
                "age": "14",
                "checksum": "0x9f32",
                "lsa-id": "1.1.1.1",
                "lsa-length": "48",
                "lsa-type": "Router",
                "options": "0x22",
                "ospf-database-extensive": {
                    "aging-timer": {
                        "#text": "00:59:46"
                    },
                    "expiration-time": {
                        "#text": "00:59:46"
                    },
                    "installation-time": {
                        "#text": "00:00:11"
                    },
                    "lsa-change-count": "3",
                    "lsa-changed-time": {
                        "#text": "00:00:11"
                    }
                },
                "ospf-router-lsa": {
                    "bits": "0x2",
                    "link-count": "2",
                    "ospf-link": [
                        {
                            "link-data": "30.0.0.1",
                            "link-id": "30.0.0.2",
                            "link-type-name": "Transit",
                            "link-type-value": "2",
                            "metric": "1",
                            "ospf-topology-count": "0"
                        },
                        {
                            "link-data": "30.0.0.1",
                            "link-id": "30.0.0.2",
                            "link-type-name": "Transit",
                            "link-type-value": "2",
                            "metric": "1",
                            "ospf-topology-count": "0"
                        },
                        {
                            "link-data": "255.255.255.255",
                            "link-id": "1.1.1.1",
                            "link-type-name": "Stub",
                            "link-type-value": "3",
                            "metric": "0",
                            "ospf-topology-count": "0"
                        },
                        {
                            "link-data": "255.255.255.255",
                            "link-id": "1.1.1.1",
                            "link-type-name": "Stub",
                            "link-type-value": "3",
                            "metric": "0",
                            "ospf-topology-count": "0"
                        }
                    ],
                    "ospf-lsa-topology": {
                        "ospf-lsa-topology-link": [
                            {
                                "link-type-name": "Transit",
                                "ospf-lsa-topology-link-metric": "1",
                                "ospf-lsa-topology-link-node-id": "30.0.0.2",
                                "ospf-lsa-topology-link-state": "Bidirectional"
                            }
                        ],
                        "ospf-topology-id": "0",
                        "ospf-topology-name": "default"
                    }
                },
                "sequence-number": "0x80000005"
            },
            {
                "advertising-router": "3.3.3.3",
                "age": "99",
                "checksum": "0xb705",
                "lsa-id": "3.3.3.3",
                "lsa-length": "48",
                "lsa-type": "Router",
                "options": "0x22",
                "ospf-database-extensive": {
                    "aging-timer": {
                        "#text": "00:58:21"
                    },
                    "expiration-time": {
                        "#text": "00:58:21"
                    },
                    "generation-timer": {
                        "#text": "00:48:21"
                    },
                    "installation-time": {
                        "#text": "00:01:39"
                    },
                    "send-time": {
                        "#text": "00:01:37"
                    }
                },
                "ospf-router-lsa": {
                    "bits": "0x0",
                    "link-count": "2",
                    "ospf-link": [
                        {
                            "link-data": "30.0.0.2",
                            "link-id": "30.0.0.2",
                            "link-type-name": "Transit",
                            "link-type-value": "2",
                            "metric": "1",
                            "ospf-topology-count": "0"
                        },
                        {
                            "link-data": "30.0.0.2",
                            "link-id": "30.0.0.2",
                            "link-type-name": "Transit",
                            "link-type-value": "2",
                            "metric": "1",
                            "ospf-topology-count": "0"
                        },
                        {
                            "link-data": "255.255.255.255",
                            "link-id": "3.3.3.3",
                            "link-type-name": "Stub",
                            "link-type-value": "3",
                            "metric": "0",
                            "ospf-topology-count": "0"
                        },
                        {
                            "link-data": "255.255.255.255",
                            "link-id": "3.3.3.3",
                            "link-type-name": "Stub",
                            "link-type-value": "3",
                            "metric": "0",
                            "ospf-topology-count": "0"
                        }
                    ],
                    "ospf-lsa-topology": {
                        "ospf-lsa-topology-link": [
                            {
                                "link-type-name": "Transit",
                                "ospf-lsa-topology-link-metric": "1",
                                "ospf-lsa-topology-link-node-id": "30.0.0.2",
                                "ospf-lsa-topology-link-state": "Bidirectional"
                            }
                        ],
                        "ospf-topology-id": "0",
                        "ospf-topology-name": "default"
                    }
                },
                "our-entry": True,
                "sequence-number": "0x80000003"
            },
            {
                "advertising-router": "3.3.3.3",
                "age": "104",
                "checksum": "0x42bb",
                "lsa-id": "30.0.0.2",
                "lsa-length": "32",
                "lsa-type": "Network",
                "options": "0x22",
                "ospf-database-extensive": {
                    "aging-timer": {
                        "#text": "00:58:16"
                    },
                    "expiration-time": {
                        "#text": "00:58:16"
                    },
                    "generation-timer": {
                        "#text": "00:48:16"
                    },
                    "installation-time": {
                        "#text": "00:01:44"
                    },
                    "send-time": {
                        "#text": "00:01:42"
                    }
                },
                "ospf-network-lsa": {
                    "address-mask": "255.255.255.0",
                    "attached-router": [
                        "3.3.3.3",
                        "1.1.1.1"
                    ],
                    "ospf-lsa-topology": {
                        "ospf-lsa-topology-link": [
                            {
                                "link-type-name": "Transit",
                                "ospf-lsa-topology-link-metric": "0",
                                "ospf-lsa-topology-link-node-id": "1.1.1.1",
                                "ospf-lsa-topology-link-state": "Bidirectional"
                            },
                            {
                                "link-type-name": "Transit",
                                "ospf-lsa-topology-link-metric": "0",
                                "ospf-lsa-topology-link-node-id": "3.3.3.3",
                                "ospf-lsa-topology-link-state": "Bidirectional"
                            }
                        ],
                        "ospf-topology-id": "0",
                        "ospf-topology-name": "default"
                    }
                },
                "our-entry": True,
                "sequence-number": "0x80000001"
            },
            {
                "advertising-router": "1.1.1.1",
                "age": "14",
                "checksum": "0xe69b",
                "lsa-id": "11.11.11.11",
                "lsa-length": "36",
                "lsa-type": "Extern",
                "options": "0x22",
                "ospf-database-extensive": {
                    "aging-timer": {
                        "#text": "00:59:46"
                    },
                    "expiration-time": {
                        "#text": "00:59:46"
                    },
                    "installation-time": {
                        "#text": "00:00:11"
                    },
                    "lsa-change-count": "1",
                    "lsa-changed-time": {
                        "#text": "00:00:11"
                    }
                },
                "ospf-external-lsa": {
                    "address-mask": "255.255.255.255",
                    "ospf-external-lsa-topology": {
                        "forward-address": "0.0.0.0",
                        "ospf-topology-id": "0",
                        "ospf-topology-metric": "0",
                        "ospf-topology-name": "default",
                        "tag": "0.0.0.0",
                        "type-value": "2"
                    }
                },
                "sequence-number": "0x80000001"
            }
        ]
    }
    }


    golden_output_3 = {"execute.return_value": """
        show ospf database netsummary extensive

            OSPF database, Area 0.0.0.0
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
        Summary *1.2.0.0          1.1.1.1          0x80000005  2388  0x22 0x48e8  28
        mask 255.255.255.0
        Topology default (ID 0) -> Metric: 1
        Gen timer 00:10:10
        Aging timer 00:20:12
        Installed 00:39:48 ago, expires in 00:20:12
        Last changed 02:12:22 ago, Change count: 1, Ours
        Summary *2.2.2.2          1.1.1.1          0x80000003  1890  0x22 0x1519  28
        mask 255.255.255.255
        Topology default (ID 0) -> Metric: 1
        Gen timer 00:18:30
        Aging timer 00:28:30
        Installed 00:31:30 ago, expires in 00:28:30
        Last changed 02:11:30 ago, Change count: 1, Ours

            OSPF database, Area 0.0.0.1
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
        Summary *1.1.1.1          1.1.1.1          0x80000005  1389  0x22 0x35fb  28
        mask 255.255.255.255
        Topology default (ID 0) -> Metric: 0
        Gen timer 00:26:50
        Aging timer 00:36:50
        Installed 00:23:09 ago, expires in 00:36:51, sent 00:23:07 ago
        Last changed 02:12:22 ago, Change count: 1, Ours
        Summary *11.11.11.11      1.1.1.1          0x80000005   890  0x22 0x67a1  28
        mask 255.255.255.255
        Topology default (ID 0) -> Metric: 0
        Gen timer 00:35:10
        Aging timer 00:45:10
        Installed 00:14:50 ago, expires in 00:45:10, sent 00:14:47 ago
        Last changed 02:12:22 ago, Change count: 1, Ours
    """}

    golden_parsed_output_3 = {
        'ospf-database-information': {
            'ospf-area-header': {
            'ospf-area': '0.0.0.1'
            },
            'ospf-database': [{
            'lsa-type': 'Summary',
            'lsa-id': '1.2.0.0',
            'advertising-router': '1.1.1.1',
            'sequence-number': '0x80000005',
            'age': '2388',
            'options': '0x22',
            'checksum': '0x48e8',
            'lsa-length': '28',
            'our-entry': True,
            'ospf-summary-lsa': {
                'address-mask': '255.255.255.0',
                'ospf-summary-lsa-topology': {
                'ospf-topology-name': 'default',
                'ospf-topology-id': '0',
                'ospf-topology-metric': '1'
                }
            },
            'ospf-database-extensive': {
                'generation-timer': {
                '#text': '00:10:10'
                },
                'aging-timer': {
                '#text': '00:20:12'
                },
                'installation-time': {
                    '#text': '00:39:48'
                },
                'expiration-time': {
                    '#text': '00:20:12'
                }
            }
            }, {
            'lsa-type': 'Summary',
            'lsa-id': '2.2.2.2',
            'advertising-router': '1.1.1.1',
            'sequence-number': '0x80000003',
            'age': '1890',
            'options': '0x22',
            'checksum': '0x1519',
            'lsa-length': '28',
            'our-entry': True,
            'ospf-summary-lsa': {
                'address-mask': '255.255.255.255',
                'ospf-summary-lsa-topology': {
                'ospf-topology-name': 'default',
                'ospf-topology-id': '0',
                'ospf-topology-metric': '1'
                }
            },
            'ospf-database-extensive': {
                'generation-timer': {
                '#text': '00:18:30'
                },
                'aging-timer': {
                '#text': '00:28:30'
                },
                'generation-timer': {
                    '#text': '00:18:30'
                },
                'installation-time': {
                    '#text': '00:31:30'
                },
                'expiration-time': {
                    '#text': '00:28:30'
                }
            }
            }, {
            'lsa-type': 'Summary',
            'lsa-id': '1.1.1.1',
            'advertising-router': '1.1.1.1',
            'sequence-number': '0x80000005',
            'age': '1389',
            'options': '0x22',
            'checksum': '0x35fb',
            'lsa-length': '28',
            'our-entry': True,
            'ospf-summary-lsa': {
                'address-mask': '255.255.255.255',
                'ospf-summary-lsa-topology': {
                'ospf-topology-name': 'default',
                'ospf-topology-id': '0',
                'ospf-topology-metric': '0'
                }
            },
            'ospf-database-extensive': {
                'generation-timer': {
                '#text': '00:26:50'
                },
                'aging-timer': {
                '#text': '00:36:50'
                },
                'expiration-time': {
                '#text': '00:36:51'
                },
                'installation-time': {
                '#text': '00:23:09'
                },
                'send-time': {
                '#text': '00:23:07'
                }
            }
            }, {
            'lsa-type': 'Summary',
            'lsa-id': '11.11.11.11',
            'advertising-router': '1.1.1.1',
            'sequence-number': '0x80000005',
            'age': '890',
            'options': '0x22',
            'checksum': '0x67a1',
            'lsa-length': '28',
            'our-entry': True,
            'ospf-summary-lsa': {
                'address-mask': '255.255.255.255',
                'ospf-summary-lsa-topology': {
                'ospf-topology-name': 'default',
                'ospf-topology-id': '0',
                'ospf-topology-metric': '0'
                }
            },
            'ospf-database-extensive': {
                'generation-timer': {
                '#text': '00:35:10'
                },
                'aging-timer': {
                '#text': '00:45:10'
                },
                'expiration-time': {
                '#text': '00:45:10'
                },
                'installation-time': {
                '#text': '00:14:50'
                },
                'send-time': {
                '#text': '00:14:47'
                }
            }
            }]
        }
        }

    golden_output_4 = {"execute.return_value": """
        show ospf database extensive

            OSPF database, Area 0.0.0.0
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
        Router  *1.1.1.1          1.1.1.1          0x80000005   271  0x22 0xb233  48
        bits 0x1, link count 2
        id 1.1.1.1, data 255.255.255.255, Type Stub (3)
            Topology count: 0, Default metric: 0
        id 11.11.11.11, data 255.255.255.255, Type Stub (3)
            Topology count: 0, Default metric: 0
        Gen timer 00:45:29
        Aging timer 00:55:29
        Installed 00:04:31 ago, expires in 00:55:29
        Last changed 02:10:28 ago, Change count: 1, Ours
        Summary *1.2.0.0          1.1.1.1          0x80000005  2269  0x22 0x48e8  28
        mask 255.255.255.0
        Topology default (ID 0) -> Metric: 1
        Gen timer 00:12:08
        Aging timer 00:22:10
        Installed 00:37:49 ago, expires in 00:22:11
        Last changed 02:10:23 ago, Change count: 1, Ours
        Summary *2.2.2.2          1.1.1.1          0x80000003  1771  0x22 0x1519  28
        mask 255.255.255.255
        Topology default (ID 0) -> Metric: 1
        Gen timer 00:20:28
        Aging timer 00:30:28
        Installed 00:29:31 ago, expires in 00:30:29
        Last changed 02:09:31 ago, Change count: 1, Ours

            OSPF database, Area 0.0.0.1
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
        Router  *1.1.1.1          1.1.1.1          0x80000006  2768  0x22 0xf427  36
        bits 0x1, link count 1
        id 1.2.0.2, data 1.2.0.1, Type Transit (2)
            Topology count: 0, Default metric: 1
        Topology default (ID 0)
            Type: Transit, Node ID: 1.2.0.2
            Metric: 1, Bidirectional
        Gen timer 00:03:48
        Aging timer 00:13:52
        Installed 00:46:08 ago, expires in 00:13:52, sent 00:46:06 ago
        Last changed 02:09:36 ago, Change count: 2, Ours
        Router   2.2.2.2          2.2.2.2          0x80000005  1777  0x22 0xc933  48
        bits 0x0, link count 2
        id 1.2.0.2, data 1.2.0.2, Type Transit (2)
            Topology count: 0, Default metric: 1
        id 2.2.2.2, data 255.255.255.255, Type Stub (3)
            Topology count: 0, Default metric: 0
        Topology default (ID 0)
            Type: Transit, Node ID: 1.2.0.2
            Metric: 1, Bidirectional
        Aging timer 00:30:22
        Installed 00:29:34 ago, expires in 00:30:23
        Last changed 02:09:34 ago, Change count: 2
        Network  1.2.0.2          2.2.2.2          0x80000003  1782  0x22 0x9c82  32
        mask 255.255.255.0
        attached router 2.2.2.2
        attached router 1.1.1.1
        Topology default (ID 0)
            Type: Transit, Node ID: 1.1.1.1
            Metric: 0, Bidirectional
            Type: Transit, Node ID: 2.2.2.2
            Metric: 0, Bidirectional
        Aging timer 00:30:17
        Installed 00:29:39 ago, expires in 00:30:18
        Last changed 02:09:39 ago, Change count: 1
        Summary *1.1.1.1          1.1.1.1          0x80000005  1270  0x22 0x35fb  28
        mask 255.255.255.255
        Topology default (ID 0) -> Metric: 0
        Gen timer 00:28:48
        Aging timer 00:38:49
        Installed 00:21:10 ago, expires in 00:38:50, sent 00:21:08 ago
        Last changed 02:10:23 ago, Change count: 1, Ours
        Summary *11.11.11.11      1.1.1.1          0x80000005   771  0x22 0x67a1  28
        mask 255.255.255.255
        Topology default (ID 0) -> Metric: 0
        Gen timer 00:37:08
        Aging timer 00:47:09
        Installed 00:12:51 ago, expires in 00:47:09, sent 00:12:48 ago
        Last changed 02:10:23 ago, Change count: 1, Ours
    """}

    golden_parsed_output_4 = {
        'ospf-database-information': {
            'ospf-area-header': {
            'ospf-area': '0.0.0.1'
            },
            'ospf-database': [{
            'lsa-type': 'Router',
            'lsa-id': '1.1.1.1',
            'advertising-router': '1.1.1.1',
            'sequence-number': '0x80000005',
            'age': '271',
            'options': '0x22',
            'checksum': '0xb233',
            'lsa-length': '48',
            'our-entry': True,
            'ospf-router-lsa': {
                'bits': '0x1',
                'link-count': '2',
                'ospf-link': [{
                'link-id': '1.1.1.1',
                'link-data': '255.255.255.255',
                'link-type-name': 'Stub',
                'link-type-value': '3',
                'ospf-topology-count': '0',
                'metric': '0'
                }, {
                'link-id': '1.1.1.1',
                'link-data': '255.255.255.255',
                'link-type-name': 'Stub',
                'link-type-value': '3',
                'ospf-topology-count': '0',
                'metric': '0'
                }, {
                'link-id': '11.11.11.11',
                'link-data': '255.255.255.255',
                'link-type-name': 'Stub',
                'link-type-value': '3',
                'ospf-topology-count': '0',
                'metric': '0'
                }, {
                'link-id': '11.11.11.11',
                'link-data': '255.255.255.255',
                'link-type-name': 'Stub',
                'link-type-value': '3',
                'ospf-topology-count': '0',
                'metric': '0'
                }]
            },
            'ospf-database-extensive': {
                'generation-timer': {
                '#text': '00:45:29'
                },
                'aging-timer': {
                '#text': '00:55:29'
                },
                'expiration-time': {
                    '#text': '00:55:29'
                },
                'installation-time': {
                    '#text': '00:04:31'
                }
            }
            }, {
            'lsa-type': 'Summary',
            'lsa-id': '1.2.0.0',
            'advertising-router': '1.1.1.1',
            'sequence-number': '0x80000005',
            'age': '2269',
            'options': '0x22',
            'checksum': '0x48e8',
            'lsa-length': '28',
            'our-entry': True,
            'ospf-summary-lsa': {
                'address-mask': '255.255.255.0',
                'ospf-summary-lsa-topology': {
                'ospf-topology-name': 'default',
                'ospf-topology-id': '0',
                'ospf-topology-metric': '1'
                }
            },
            'ospf-database-extensive': {
                'generation-timer': {
                '#text': '00:12:08'
                },
                'aging-timer': {
                '#text': '00:22:10'
                },
                'expiration-time': {
                    '#text': '00:22:11'
                },
                'installation-time': {
                    '#text': '00:37:49'
                },
            }
            }, {
            'lsa-type': 'Summary',
            'lsa-id': '2.2.2.2',
            'advertising-router': '1.1.1.1',
            'sequence-number': '0x80000003',
            'age': '1771',
            'options': '0x22',
            'checksum': '0x1519',
            'lsa-length': '28',
            'our-entry': True,
            'ospf-summary-lsa': {
                'address-mask': '255.255.255.255',
                'ospf-summary-lsa-topology': {
                'ospf-topology-name': 'default',
                'ospf-topology-id': '0',
                'ospf-topology-metric': '1'
                }
            },
            'ospf-database-extensive': {
                'generation-timer': {
                '#text': '00:20:28'
                },
                'aging-timer': {
                '#text': '00:30:28'
                },
                'expiration-time': {
                    '#text': '00:30:29'
                },
                'installation-time': {
                    '#text': '00:29:31'
                },
            }
            }, {
            'lsa-type': 'Router',
            'lsa-id': '1.1.1.1',
            'advertising-router': '1.1.1.1',
            'sequence-number': '0x80000006',
            'age': '2768',
            'options': '0x22',
            'checksum': '0xf427',
            'lsa-length': '36',
            'our-entry': True,
            'ospf-router-lsa': {
                'bits': '0x1',
                'link-count': '1',
                'ospf-link': [{
                'link-id': '1.2.0.2',
                'link-data': '1.2.0.1',
                'link-type-name': 'Transit',
                'link-type-value': '2',
                'ospf-topology-count': '0',
                'metric': '1'
                }, {
                'link-id': '1.2.0.2',
                'link-data': '1.2.0.1',
                'link-type-name': 'Transit',
                'link-type-value': '2',
                'ospf-topology-count': '0',
                'metric': '1'
                }],
                'ospf-lsa-topology': {
                'ospf-topology-name': 'default',
                'ospf-topology-id': '0',
                'ospf-lsa-topology-link': [{
                    'link-type-name': 'Transit',
                    'ospf-lsa-topology-link-node-id': '1.2.0.2',
                    'ospf-lsa-topology-link-metric': '1',
                    'ospf-lsa-topology-link-state': 'Bidirectional'
                }]
                }
            },
            'ospf-database-extensive': {
                'generation-timer': {
                '#text': '00:03:48'
                },
                'aging-timer': {
                '#text': '00:13:52'
                },
                'expiration-time': {
                '#text': '00:13:52'
                },
                'installation-time': {
                '#text': '00:46:08'
                },
                'send-time': {
                '#text': '00:46:06'
                }
            }
            }, {
            'lsa-type': 'Router',
            'lsa-id': '2.2.2.2',
            'advertising-router': '2.2.2.2',
            'sequence-number': '0x80000005',
            'age': '1777',
            'options': '0x22',
            'checksum': '0xc933',
            'lsa-length': '48',
            'ospf-router-lsa': {
                'bits': '0x0',
                'link-count': '2',
                'ospf-link': [{
                'link-id': '1.2.0.2',
                'link-data': '1.2.0.2',
                'link-type-name': 'Transit',
                'link-type-value': '2',
                'ospf-topology-count': '0',
                'metric': '1'
                }, {
                'link-id': '1.2.0.2',
                'link-data': '1.2.0.2',
                'link-type-name': 'Transit',
                'link-type-value': '2',
                'ospf-topology-count': '0',
                'metric': '1'
                }, {
                'link-id': '2.2.2.2',
                'link-data': '255.255.255.255',
                'link-type-name': 'Stub',
                'link-type-value': '3',
                'ospf-topology-count': '0',
                'metric': '0'
                }, {
                'link-id': '2.2.2.2',
                'link-data': '255.255.255.255',
                'link-type-name': 'Stub',
                'link-type-value': '3',
                'ospf-topology-count': '0',
                'metric': '0'
                }],
                'ospf-lsa-topology': {
                'ospf-topology-name': 'default',
                'ospf-topology-id': '0',
                'ospf-lsa-topology-link': [{
                    'link-type-name': 'Transit',
                    'ospf-lsa-topology-link-node-id': '1.2.0.2',
                    'ospf-lsa-topology-link-metric': '1',
                    'ospf-lsa-topology-link-state': 'Bidirectional'
                }]
                }
            },
            'ospf-database-extensive': {
                'aging-timer': {
                '#text': '00:30:22'
                },
                'lsa-changed-time': {
                '#text': '02:09:34'
                },
                'expiration-time': {
                    '#text': '00:30:23'
                },
                'installation-time': {
                    '#text': '00:29:34'
                },
                'lsa-change-count': '2'
            }
            }, {
            'lsa-type': 'Network',
            'lsa-id': '1.2.0.2',
            'advertising-router': '2.2.2.2',
            'sequence-number': '0x80000003',
            'age': '1782',
            'options': '0x22',
            'checksum': '0x9c82',
            'lsa-length': '32',
            'ospf-network-lsa': {
                'address-mask': '255.255.255.0',
                'attached-router': ['2.2.2.2', '1.1.1.1'],
                'ospf-lsa-topology': {
                'ospf-topology-name': 'default',
                'ospf-topology-id': '0',
                'ospf-lsa-topology-link': [{
                    'link-type-name': 'Transit',
                    'ospf-lsa-topology-link-node-id': '1.1.1.1',
                    'ospf-lsa-topology-link-metric': '0',
                    'ospf-lsa-topology-link-state': 'Bidirectional'
                }, {
                    'link-type-name': 'Transit',
                    'ospf-lsa-topology-link-node-id': '2.2.2.2',
                    'ospf-lsa-topology-link-metric': '0',
                    'ospf-lsa-topology-link-state': 'Bidirectional'
                }]
                }
            },
            'ospf-database-extensive': {
                'aging-timer': {
                '#text': '00:30:17'
                },
                'lsa-changed-time': {
                '#text': '02:09:39'
                },
                'expiration-time': {
                    '#text': '00:30:18'
                },
                'installation-time': {
                    '#text': '00:29:39'
                },
                'lsa-change-count': '1'
            }
            }, {
            'lsa-type': 'Summary',
            'lsa-id': '1.1.1.1',
            'advertising-router': '1.1.1.1',
            'sequence-number': '0x80000005',
            'age': '1270',
            'options': '0x22',
            'checksum': '0x35fb',
            'lsa-length': '28',
            'our-entry': True,
            'ospf-summary-lsa': {
                'address-mask': '255.255.255.255',
                'ospf-summary-lsa-topology': {
                'ospf-topology-name': 'default',
                'ospf-topology-id': '0',
                'ospf-topology-metric': '0'
                }
            },
            'ospf-database-extensive': {
                'generation-timer': {
                '#text': '00:28:48'
                },
                'aging-timer': {
                '#text': '00:38:49'
                },
                'expiration-time': {
                '#text': '00:38:50'
                },
                'installation-time': {
                '#text': '00:21:10'
                },
                'send-time': {
                '#text': '00:21:08'
                }
            }
            }, {
            'lsa-type': 'Summary',
            'lsa-id': '11.11.11.11',
            'advertising-router': '1.1.1.1',
            'sequence-number': '0x80000005',
            'age': '771',
            'options': '0x22',
            'checksum': '0x67a1',
            'lsa-length': '28',
            'our-entry': True,
            'ospf-summary-lsa': {
                'address-mask': '255.255.255.255',
                'ospf-summary-lsa-topology': {
                'ospf-topology-name': 'default',
                'ospf-topology-id': '0',
                'ospf-topology-metric': '0'
                }
            },
            'ospf-database-extensive': {
                'generation-timer': {
                '#text': '00:37:08'
                },
                'aging-timer': {
                '#text': '00:47:09'
                },
                'expiration-time': {
                '#text': '00:47:09'
                },
                'installation-time': {
                '#text': '00:12:51'
                },
                'send-time': {
                '#text': '00:12:48'
                }
            }
            }]
        }
        }

    def test_empty(self):
        pass
        self.device = Mock(**self.empty_output)
        obj = ShowOspfDatabaseExtensive(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        pass
        self.device = Mock(**self.golden_output)
        obj = ShowOspfDatabaseExtensive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowOspfDatabaseAdvertisingRouterExtensive(device=self.device)
        parsed_output = obj.parse(ipaddress='10.34.2.250')
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowOspfDatabaseExtensive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.device = Mock(**self.golden_output_3)
        obj = ShowOspfDatabaseExtensive(device=self.device)
        parsed_output = obj.parse(data_type='netsummary')
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

    def test_golden_4(self):
        self.device = Mock(**self.golden_output_4)
        obj = ShowOspfDatabaseExtensive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_4)


class TestShowOspfNeighborExtensive(unittest.TestCase):
    """ Unit tests for:
            * show ospf neighbor extensive
    """

    device = Device(name="aDevice")

    maxDiff = None

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
        show ospf neighbor extensive
        Address          Interface              State     ID               Pri  Dead
        10.189.5.94      ge-0/0/0.0             Full      10.189.5.253     128    39
        Area 0.0.0.8, opt 0x52, DR 0.0.0.0, BDR 0.0.0.0
        Up 3w0d 16:50:35, adjacent 3w0d 16:50:35
        SPRING Adjacency Labels:

            Label       Flags       Adj-Sid-Type

            28985       BVL         Protected

            28986       VL          UnProtected

        Topology default (ID 0) -> Bidirectional
        10.169.14.121   ge-0/0/1.0             Full      10.169.14.240   128    31
        Area 0.0.0.8, opt 0x52, DR 0.0.0.0, BDR 0.0.0.0
        Up 3w2d 03:12:20, adjacent 3w2d 03:12:15
        SPRING Adjacency Labels:

            Label       Flags       Adj-Sid-Type

            2567        BVL         Protected

            2568        VL          UnProtected

        Topology default (ID 0) -> Bidirectional
        10.19.198.26     ge-0/0/2.0             Full      10.19.198.239      1    39
        Area 0.0.0.8, opt 0x52, DR 0.0.0.0, BDR 0.0.0.0
        Up 1w5d 20:40:14, adjacent 1w5d 20:40:14
        SPRING Adjacency Labels:

            Label       Flags       Adj-Sid-Type

            167966      BVL         Protected

            167967      VL          UnProtected

        Topology default (ID 0) -> Bidirectional
    """
    }

    golden_parsed_output = {
        "ospf-neighbor-information": {
            "ospf-neighbor": [
                {
                    "activity-timer": "39",
                    "adj-sid-list": {
                        "spring-adjacency-labels": [
                            {
                                "adj-sid-type": "Protected",
                                "flags": "BVL",
                                "label": "28985",
                            },
                            {
                                "adj-sid-type": "UnProtected",
                                "flags": "VL",
                                "label": "28986",
                            },
                        ]
                    },
                    "bdr-address": "0.0.0.0",
                    "dr-address": "0.0.0.0",
                    "interface-name": "ge-0/0/0.0",
                    "neighbor-address": "10.189.5.94",
                    "neighbor-adjacency-time": {"#text": "3w0d 16:50:35"},
                    "neighbor-id": "10.189.5.253",
                    "neighbor-priority": "128",
                    "neighbor-up-time": {"#text": "3w0d 16:50:35"},
                    "options": "0x52",
                    "ospf-area": "0.0.0.8",
                    "ospf-neighbor-state": "Full",
                    "ospf-neighbor-topology": {
                        "ospf-neighbor-topology-state": "Bidirectional",
                        "ospf-topology-id": "0",
                        "ospf-topology-name": "default",
                    },
                },
                {
                    "activity-timer": "31",
                    "adj-sid-list": {
                        "spring-adjacency-labels": [
                            {
                                "adj-sid-type": "Protected",
                                "flags": "BVL",
                                "label": "2567",
                            },
                            {
                                "adj-sid-type": "UnProtected",
                                "flags": "VL",
                                "label": "2568",
                            },
                        ]
                    },
                    "bdr-address": "0.0.0.0",
                    "dr-address": "0.0.0.0",
                    "interface-name": "ge-0/0/1.0",
                    "neighbor-address": "10.169.14.121",
                    "neighbor-adjacency-time": {"#text": "3w2d 03:12:15"},
                    "neighbor-id": "10.169.14.240",
                    "neighbor-priority": "128",
                    "neighbor-up-time": {"#text": "3w2d 03:12:20"},
                    "options": "0x52",
                    "ospf-area": "0.0.0.8",
                    "ospf-neighbor-state": "Full",
                    "ospf-neighbor-topology": {
                        "ospf-neighbor-topology-state": "Bidirectional",
                        "ospf-topology-id": "0",
                        "ospf-topology-name": "default",
                    },
                },
                {
                    "activity-timer": "39",
                    "adj-sid-list": {
                        "spring-adjacency-labels": [
                            {
                                "adj-sid-type": "Protected",
                                "flags": "BVL",
                                "label": "167966",
                            },
                            {
                                "adj-sid-type": "UnProtected",
                                "flags": "VL",
                                "label": "167967",
                            },
                        ]
                    },
                    "bdr-address": "0.0.0.0",
                    "dr-address": "0.0.0.0",
                    "interface-name": "ge-0/0/2.0",
                    "neighbor-address": "10.19.198.26",
                    "neighbor-adjacency-time": {"#text": "1w5d 20:40:14"},
                    "neighbor-id": "10.19.198.239",
                    "neighbor-priority": "1",
                    "neighbor-up-time": {"#text": "1w5d 20:40:14"},
                    "options": "0x52",
                    "ospf-area": "0.0.0.8",
                    "ospf-neighbor-state": "Full",
                    "ospf-neighbor-topology": {
                        "ospf-neighbor-topology-state": "Bidirectional",
                        "ospf-topology-id": "0",
                        "ospf-topology-name": "default",
                    },
                },
            ]
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspfNeighborExtensive(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspfNeighborExtensive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowOspfInterfaceExtensive(unittest.TestCase):
    """ Unit tests for:
            * show ospf interface extensive
    """

    maxDiff = None

    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
                show ospf interface extensive
        Interface           State   Area            DR ID           BDR ID          Nbrs
        ge-0/0/0.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
        Type: P2P, Address: 10.189.5.93, Mask: 255.255.255.252, MTU: 1500, Cost: 5
        Adj count: 1
        Hello: 10, Dead: 40, ReXmit: 5, Not Stub
        Auth type: None
        Protection type: Post Convergence
        Post convergence protection: Enabled, Fate sharing: No, SRLG: No, Node cost: 100
        Topology default (ID 0) -> Cost: 5
        ge-0/0/1.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
        Type: P2P, Address: 10.169.14.122, Mask: 255.255.255.252, MTU: 1500, Cost: 100
        Adj count: 1
        Hello: 10, Dead: 40, ReXmit: 5, Not Stub
        Auth type: None
        Protection type: Post Convergence
        Post convergence protection: Enabled, Fate sharing: No, SRLG: No, Node cost: 100
        Topology default (ID 0) -> Cost: 100
        ge-0/0/2.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
        Type: P2P, Address: 10.19.198.25, Mask: 255.255.255.252, MTU: 1500, Cost: 1000
        Adj count: 1
        Hello: 10, Dead: 40, ReXmit: 5, Not Stub
        Auth type: None
        Protection type: Post Convergence
        Post convergence protection: Enabled, Fate sharing: No, SRLG: No, Node cost: 100
        Topology default (ID 0) -> Cost: 1000
        ge-0/0/3.0          DRother 0.0.0.8         0.0.0.0         0.0.0.0            0
        Type: LAN, Address: 10.55.0.254, Mask: 255.255.255.0, MTU: 1500, Cost: 100
        Adj count: 0, Passive
        Hello: 10, Dead: 40, ReXmit: 5, Not Stub
        Auth type: None
        Protection type: None
        Topology default (ID 0) -> Passive, Cost: 100
        lo0.0               DR      0.0.0.8         10.189.5.252    0.0.0.0            0
        Type: LAN, Address: 10.189.5.252, Mask: 255.255.255.255, MTU: 65535, Cost: 0
        DR addr: 10.189.5.252, Priority: 128
        Adj count: 0
        Hello: 10, Dead: 40, ReXmit: 5, Not Stub
        Auth type: None
        Protection type: None
        Topology default (ID 0) -> Cost: 0
        """
    }

    golden_parsed_output = {
        "ospf-interface-information": {
            "ospf-interface": [
                {
                    "address-mask": "255.255.255.252",
                    "adj-count": "1",
                    "authentication-type": "None",
                    "bdr-id": "0.0.0.0",
                    "dead-interval": "40",
                    "dr-id": "0.0.0.0",
                    "hello-interval": "10",
                    "interface-address": "10.189.5.93",
                    "interface-cost": "5",
                    "interface-name": "ge-0/0/0.0",
                    "interface-type": "P2P",
                    "mtu": "1500",
                    "neighbor-count": "1",
                    "ospf-area": "0.0.0.8",
                    "ospf-interface-protection-type": "Post Convergence",
                    "ospf-interface-state": "PtToPt",
                    "ospf-interface-tilfa-prot-fate": "No",
                    "ospf-interface-tilfa-prot-link": "Enabled",
                    "ospf-interface-tilfa-prot-node": "100",
                    "ospf-interface-tilfa-prot-srlg": "No",
                    "ospf-interface-topology": {
                        "ospf-topology-id": "0",
                        "ospf-topology-metric": "5",
                        "ospf-topology-name": "default",
                    },
                    "ospf-stub-type": "Not Stub",
                    "retransmit-interval": "5",
                },
                {
                    "address-mask": "255.255.255.252",
                    "adj-count": "1",
                    "authentication-type": "None",
                    "bdr-id": "0.0.0.0",
                    "dead-interval": "40",
                    "dr-id": "0.0.0.0",
                    "hello-interval": "10",
                    "interface-address": "10.169.14.122",
                    "interface-cost": "100",
                    "interface-name": "ge-0/0/1.0",
                    "interface-type": "P2P",
                    "mtu": "1500",
                    "neighbor-count": "1",
                    "ospf-area": "0.0.0.8",
                    "ospf-interface-protection-type": "Post Convergence",
                    "ospf-interface-state": "PtToPt",
                    "ospf-interface-tilfa-prot-fate": "No",
                    "ospf-interface-tilfa-prot-link": "Enabled",
                    "ospf-interface-tilfa-prot-node": "100",
                    "ospf-interface-tilfa-prot-srlg": "No",
                    "ospf-interface-topology": {
                        "ospf-topology-id": "0",
                        "ospf-topology-metric": "100",
                        "ospf-topology-name": "default",
                    },
                    "ospf-stub-type": "Not Stub",
                    "retransmit-interval": "5",
                },
                {
                    "address-mask": "255.255.255.252",
                    "adj-count": "1",
                    "authentication-type": "None",
                    "bdr-id": "0.0.0.0",
                    "dead-interval": "40",
                    "dr-id": "0.0.0.0",
                    "hello-interval": "10",
                    "interface-address": "10.19.198.25",
                    "interface-cost": "1000",
                    "interface-name": "ge-0/0/2.0",
                    "interface-type": "P2P",
                    "mtu": "1500",
                    "neighbor-count": "1",
                    "ospf-area": "0.0.0.8",
                    "ospf-interface-protection-type": "Post Convergence",
                    "ospf-interface-state": "PtToPt",
                    "ospf-interface-tilfa-prot-fate": "No",
                    "ospf-interface-tilfa-prot-link": "Enabled",
                    "ospf-interface-tilfa-prot-node": "100",
                    "ospf-interface-tilfa-prot-srlg": "No",
                    "ospf-interface-topology": {
                        "ospf-topology-id": "0",
                        "ospf-topology-metric": "1000",
                        "ospf-topology-name": "default",
                    },
                    "ospf-stub-type": "Not Stub",
                    "retransmit-interval": "5",
                },
                {
                    "address-mask": "255.255.255.0",
                    "adj-count": "0",
                    "authentication-type": "None",
                    "bdr-id": "0.0.0.0",
                    "dead-interval": "40",
                    "dr-id": "0.0.0.0",
                    "hello-interval": "10",
                    "interface-address": "10.55.0.254",
                    "interface-cost": "100",
                    "interface-name": "ge-0/0/3.0",
                    "interface-type": "LAN",
                    "mtu": "1500",
                    "neighbor-count": "0",
                    "ospf-area": "0.0.0.8",
                    "ospf-interface-protection-type": "None",
                    "ospf-interface-state": "DRother",
                    "ospf-interface-topology": {
                        "ospf-topology-id": "0",
                        "ospf-topology-metric": "100",
                        "ospf-topology-name": "default",
                        "ospf-topology-passive": True,
                    },
                    "ospf-stub-type": "Not Stub",
                    "passive": "Passive",
                    "retransmit-interval": "5",
                },
                {
                    "address-mask": "255.255.255.255",
                    "adj-count": "0",
                    "authentication-type": "None",
                    "bdr-id": "0.0.0.0",
                    "dead-interval": "40",
                    "dr-address": "10.189.5.252",
                    "dr-id": "10.189.5.252",
                    "hello-interval": "10",
                    "interface-address": "10.189.5.252",
                    "interface-cost": "0",
                    "interface-name": "lo0.0",
                    "interface-type": "LAN",
                    "mtu": "65535",
                    "neighbor-count": "0",
                    "ospf-area": "0.0.0.8",
                    "ospf-interface-protection-type": "None",
                    "ospf-interface-state": "DR",
                    "ospf-interface-topology": {
                        "ospf-topology-id": "0",
                        "ospf-topology-metric": "0",
                        "ospf-topology-name": "default",
                    },
                    "ospf-stub-type": "Not Stub",
                    "retransmit-interval": "5",
                    "router-priority": "128",
                },
            ]
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspfInterfaceExtensive(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspfInterfaceExtensive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowOspfNeighborDetail(unittest.TestCase):
    """ Unit tests for:
            * show ospf neighbor detail
    """

    device = Device(name="aDevice")

    maxDiff = None

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
        show ospf neighbor detail
        Address          Interface              State     ID               Pri  Dead
        10.189.5.94      ge-0/0/0.0             Full      10.189.5.253     128    39
        Area 0.0.0.8, opt 0x52, DR 0.0.0.0, BDR 0.0.0.0
        Up 3w0d 16:50:35, adjacent 3w0d 16:50:35
        SPRING Adjacency Labels:

            Label       Flags       Adj-Sid-Type

            28985       BVL         Protected

            28986       VL          UnProtected

        Topology default (ID 0) -> Bidirectional
        10.169.14.121   ge-0/0/1.0             Full      10.169.14.240   128    31
        Area 0.0.0.8, opt 0x52, DR 0.0.0.0, BDR 0.0.0.0
        Up 3w2d 03:12:20, adjacent 3w2d 03:12:15
        SPRING Adjacency Labels:

            Label       Flags       Adj-Sid-Type

            2567        BVL         Protected

            2568        VL          UnProtected

        Topology default (ID 0) -> Bidirectional
        10.19.198.26     ge-0/0/2.0             Full      10.19.198.239      1    39
        Area 0.0.0.8, opt 0x52, DR 0.0.0.0, BDR 0.0.0.0
        Up 1w5d 20:40:14, adjacent 1w5d 20:40:14
        SPRING Adjacency Labels:

            Label       Flags       Adj-Sid-Type

            167966      BVL         Protected

            167967      VL          UnProtected

        Topology default (ID 0) -> Bidirectional
    """
    }

    golden_parsed_output = {
        "ospf-neighbor-information": {
            "ospf-neighbor": [
                {
                    "activity-timer": "39",
                    "adj-sid-list": {
                        "spring-adjacency-labels": [
                            {
                                "adj-sid-type": "Protected",
                                "flags": "BVL",
                                "label": "28985",
                            },
                            {
                                "adj-sid-type": "UnProtected",
                                "flags": "VL",
                                "label": "28986",
                            },
                        ]
                    },
                    "bdr-address": "0.0.0.0",
                    "dr-address": "0.0.0.0",
                    "interface-name": "ge-0/0/0.0",
                    "neighbor-address": "10.189.5.94",
                    "neighbor-adjacency-time": {"#text": "3w0d 16:50:35"},
                    "neighbor-id": "10.189.5.253",
                    "neighbor-priority": "128",
                    "neighbor-up-time": {"#text": "3w0d 16:50:35"},
                    "options": "0x52",
                    "ospf-area": "0.0.0.8",
                    "ospf-neighbor-state": "Full",
                    "ospf-neighbor-topology": {
                        "ospf-neighbor-topology-state": "Bidirectional",
                        "ospf-topology-id": "0",
                        "ospf-topology-name": "default",
                    },
                },
                {
                    "activity-timer": "31",
                    "adj-sid-list": {
                        "spring-adjacency-labels": [
                            {
                                "adj-sid-type": "Protected",
                                "flags": "BVL",
                                "label": "2567",
                            },
                            {
                                "adj-sid-type": "UnProtected",
                                "flags": "VL",
                                "label": "2568",
                            },
                        ]
                    },
                    "bdr-address": "0.0.0.0",
                    "dr-address": "0.0.0.0",
                    "interface-name": "ge-0/0/1.0",
                    "neighbor-address": "10.169.14.121",
                    "neighbor-adjacency-time": {"#text": "3w2d 03:12:15"},
                    "neighbor-id": "10.169.14.240",
                    "neighbor-priority": "128",
                    "neighbor-up-time": {"#text": "3w2d 03:12:20"},
                    "options": "0x52",
                    "ospf-area": "0.0.0.8",
                    "ospf-neighbor-state": "Full",
                    "ospf-neighbor-topology": {
                        "ospf-neighbor-topology-state": "Bidirectional",
                        "ospf-topology-id": "0",
                        "ospf-topology-name": "default",
                    },
                },
                {
                    "activity-timer": "39",
                    "adj-sid-list": {
                        "spring-adjacency-labels": [
                            {
                                "adj-sid-type": "Protected",
                                "flags": "BVL",
                                "label": "167966",
                            },
                            {
                                "adj-sid-type": "UnProtected",
                                "flags": "VL",
                                "label": "167967",
                            },
                        ]
                    },
                    "bdr-address": "0.0.0.0",
                    "dr-address": "0.0.0.0",
                    "interface-name": "ge-0/0/2.0",
                    "neighbor-address": "10.19.198.26",
                    "neighbor-adjacency-time": {"#text": "1w5d 20:40:14"},
                    "neighbor-id": "10.19.198.239",
                    "neighbor-priority": "1",
                    "neighbor-up-time": {"#text": "1w5d 20:40:14"},
                    "options": "0x52",
                    "ospf-area": "0.0.0.8",
                    "ospf-neighbor-state": "Full",
                    "ospf-neighbor-topology": {
                        "ospf-neighbor-topology-state": "Bidirectional",
                        "ospf-topology-id": "0",
                        "ospf-topology-name": "default",
                    },
                },
            ]
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspfNeighborDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspfNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_ospf_neighbor_instance_detail(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspfNeighborDetail(device=self.device)
        parsed_output = obj.parse(neighbor="10.189.5.94")
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowOspfRouteBrief(unittest.TestCase):
    """ Unit tests for:
            * show ospf route brief
    """

    maxDiff = None

    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
        show ospf route brief
        Topology default Route Table:

        Prefix             Path  Route      NH       Metric NextHop       Nexthop
                        Type  Type       Type            Interface     Address/LSP
        10.36.3.3            Intra Router     IP         1201 ge-0/0/1.0    10.169.14.121
        10.100.5.5            Intra Router     IP         1200 ge-0/0/1.0    10.169.14.121
        10.19.198.239      Intra Router     IP         1000 ge-0/0/2.0    10.19.198.26
        10.34.2.250       Intra AS BR      IP          200 ge-0/0/1.0    10.169.14.121
        10.34.2.251       Intra AS BR      IP          205 ge-0/0/1.0    10.169.14.121
        10.169.196.241    Intra Router     IP         1200 ge-0/0/1.0    10.169.14.121
        10.169.14.240     Intra AS BR      IP          100 ge-0/0/1.0    10.169.14.121
        10.169.14.241     Intra AS BR      IP          105 ge-0/0/1.0    10.169.14.121
        10.189.5.253       Intra AS BR      IP            5 ge-0/0/0.0    10.189.5.94
        192.168.36.119    Intra AS BR      IP        10100 ge-0/0/1.0    10.169.14.121
        192.168.36.120    Intra AS BR      IP        10100 ge-0/0/1.0    10.169.14.121
        0.0.0.0/0          Ext1  Network    IP          101 ge-0/0/1.0    10.169.14.121
        10.1.0.0/24         Ext2  Network    IP           20 ge-0/0/1.0    10.169.14.121
        10.36.3.3/32         Intra Network    IP         1202 ge-0/0/1.0    10.169.14.121
        10.16.0.0/30         Intra Network    IP         1200 ge-0/0/1.0    10.169.14.121
        10.100.5.5/32         Intra Network    IP         1201 ge-0/0/1.0    10.169.14.121
        10.100.5.5/32         Intra Network    Spring     1201 ge-0/0/1.0    10.169.14.121
                                            Bkup SPRING     ge-0/0/0.0    10.189.5.94
        10.19.198.24/30    Intra Network    IP         1000 ge-0/0/2.0
        10.19.198.28/30    Intra Network    IP         1005 ge-0/0/0.0    10.189.5.94
        10.19.198.239/32   Intra Network    IP         1001 ge-0/0/2.0    10.19.198.26
        10.19.198.239/32   Intra Network    Spring     1001 ge-0/0/2.0    10.19.198.26
                                            Bkup SPRING     ge-0/0/0.0    10.189.5.94
        10.174.132.237/32   Ext1  Network    IP          150 ge-0/0/1.0    10.169.14.121
        10.34.2.200/30    Intra Network    IP          205 ge-0/0/1.0    10.169.14.121
        10.34.2.250/32    Intra Network    IP          200 ge-0/0/1.0    10.169.14.121
        10.34.2.250/32    Intra Network    Spring      200 ge-0/0/1.0    10.169.14.121
        10.34.2.251/32    Intra Network    IP          205 ge-0/0/1.0    10.169.14.121
        10.34.2.251/32    Intra Network    Spring      205 ge-0/0/1.0    10.169.14.121
        10.15.0.0/30        Intra Network    IP         1001 ge-0/0/2.0    10.19.198.26
        10.64.0.0/30        Intra Network    IP         1201 ge-0/0/1.0    10.169.14.121
        10.55.0.0/24       Intra Network    IP          100 ge-0/0/3.0
        10.169.196.212/30 Intra Network    IP         1200 ge-0/0/1.0    10.169.14.121
        10.169.196.216/30 Intra Network    IP         1205 ge-0/0/1.0    10.169.14.121
        10.169.196.241/32 Intra Network    IP         1201 ge-0/0/1.0    10.169.14.121
        10.169.196.241/32 Intra Network    Spring     1201 ge-0/0/1.0    10.169.14.121
                                            Bkup SPRING     ge-0/0/0.0    10.189.5.94
        10.169.14.16/30   Intra Network    IP          105 ge-0/0/1.0    10.169.14.121
        10.169.14.32/30   Intra Network    IP          225 ge-0/0/1.0    10.169.14.121
        10.169.14.120/30  Intra Network    IP          100 ge-0/0/1.0
        10.169.14.128/30  Intra Network    IP          125 ge-0/0/0.0    10.189.5.94
        10.169.14.156/30  Intra Network    IP          200 ge-0/0/1.0    10.169.14.121
        10.169.14.240/32  Intra Network    IP          100 ge-0/0/1.0    10.169.14.121
        10.169.14.240/32  Intra Network    Spring      100 ge-0/0/1.0    10.169.14.121
                                            Bkup SPRING     ge-0/0/0.0    10.189.5.94
        10.169.14.241/32  Intra Network    IP          105 ge-0/0/1.0    10.169.14.121
        10.169.14.241/32  Intra Network    Spring      105 ge-0/0/1.0    10.169.14.121
        10.169.14.242/32  Intra Network    IP          100 ge-0/0/1.0    10.169.14.121
        10.169.14.243/32  Intra Network    IP          105 ge-0/0/1.0    10.169.14.121
        10.189.5.92/30     Intra Network    IP            5 ge-0/0/0.0
        10.189.5.252/32    Intra Network    IP            0 lo0.0
        10.189.5.252/32    Intra Network    Spring        0 lo0.0
        10.189.5.253/32    Intra Network    IP            5 ge-0/0/0.0    10.189.5.94
        10.189.5.253/32    Intra Network    Spring        5 ge-0/0/0.0    10.189.5.94
        192.168.220.0/30       Intra Network    IP         1200 ge-0/0/1.0    10.169.14.121
        192.168.36.119/32 Intra Network    IP        10101 ge-0/0/1.0    10.169.14.121
        192.168.36.120/32 Intra Network    IP        10101 ge-0/0/1.0    10.169.14.121
        2567               Intra Network    Mpls          0 ge-0/0/1.0    10.169.14.121
                                            Bkup MPLS       ge-0/0/0.0    10.189.5.94
        2567 (S=0)         Intra Network    Mpls          0 ge-0/0/1.0    10.169.14.121
                                            Bkup MPLS       ge-0/0/0.0    10.189.5.94
        2568               Intra Network    Mpls          0 ge-0/0/1.0    10.169.14.121
        2568 (S=0)         Intra Network    Mpls          0 ge-0/0/1.0    10.169.14.121
        167966             Intra Network    Mpls          0 ge-0/0/2.0    10.19.198.26
                                            Bkup MPLS       ge-0/0/0.0    10.189.5.94
        167966 (S=0)       Intra Network    Mpls          0 ge-0/0/2.0    10.19.198.26
                                            Bkup MPLS       ge-0/0/0.0    10.189.5.94
        167967             Intra Network    Mpls          0 ge-0/0/2.0    10.19.198.26
        167967 (S=0)       Intra Network    Mpls          0 ge-0/0/2.0    10.19.198.26
        28985              Intra Network    Mpls          0 ge-0/0/0.0    10.189.5.94
        28985 (S=0)        Intra Network    Mpls          0 ge-0/0/0.0    10.189.5.94
        28986              Intra Network    Mpls          0 ge-0/0/0.0    10.189.5.94
        28986 (S=0)        Intra Network    Mpls          0 ge-0/0/0.0    10.189.5.94
        17000              Intra Network    Mpls       1201 ge-0/0/1.0    10.169.14.121
                                            Bkup MPLS       ge-0/0/0.0    10.189.5.94
        16051              Intra Network    Mpls        100 ge-0/0/1.0    10.169.14.121
                                            Bkup MPLS       ge-0/0/0.0    10.189.5.94
        16051 (S=0)        Intra Network    Mpls        100 ge-0/0/1.0    10.169.14.121
                                            Bkup MPLS       ge-0/0/0.0    10.189.5.94
        16052              Intra Network    Mpls        105 ge-0/0/1.0    10.169.14.121
        16061              Intra Network    Mpls        200 ge-0/0/1.0    10.169.14.121
        16062              Intra Network    Mpls        205 ge-0/0/1.0    10.169.14.121
        16063              Intra Network    Mpls       1201 ge-0/0/1.0    10.169.14.121
                                            Bkup MPLS       ge-0/0/0.0    10.189.5.94
        16072              Intra Network    Mpls          5 ge-0/0/0.0    10.189.5.94
        16073              Intra Network    Mpls       1001 ge-0/0/2.0    10.19.198.26
                                            Bkup MPLS       ge-0/0/0.0    10.189.5.94
        16073 (S=0)        Intra Network    Mpls       1001 ge-0/0/2.0    10.19.198.26
                                            Bkup MPLS       ge-0/0/0.0    10.189.5.94
    """
    }

    golden_parsed_output = {
        "ospf-route-information": {
            "ospf-topology-route-table": {
                "ospf-route": [
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.36.3.3",
                                "interface-cost": "1201",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Router",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.100.5.5",
                                "interface-cost": "1200",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Router",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.19.198.239",
                                "interface-cost": "1000",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.19.198.26"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Router",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.34.2.250",
                                "interface-cost": "200",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "AS BR",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.34.2.251",
                                "interface-cost": "205",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "AS BR",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.169.196.241",
                                "interface-cost": "1200",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Router",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.169.14.240",
                                "interface-cost": "100",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "AS BR",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.169.14.241",
                                "interface-cost": "105",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "AS BR",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.189.5.253",
                                "interface-cost": "5",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.189.5.94"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "AS BR",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "192.168.36.119",
                                "interface-cost": "10100",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "AS BR",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "192.168.36.120",
                                "interface-cost": "10100",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "AS BR",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "0.0.0.0/0",
                                "interface-cost": "101",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Ext1",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.1.0.0/24",
                                "interface-cost": "20",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Ext2",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.36.3.3/32",
                                "interface-cost": "1202",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.16.0.0/30",
                                "interface-cost": "1200",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.100.5.5/32",
                                "interface-cost": "1201",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            },
                            {
                                "address-prefix": "10.100.5.5/32",
                                "interface-cost": "1201",
                                "next-hop-type": "Spring",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup SPRING",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            },
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.19.198.24/30",
                                "interface-cost": "1000",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-name": {"interface-name": "ge-0/0/2.0"}
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.19.198.28/30",
                                "interface-cost": "1005",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.189.5.94"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.19.198.239/32",
                                "interface-cost": "1001",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.19.198.26"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            },
                            {
                                "address-prefix": "10.19.198.239/32",
                                "interface-cost": "1001",
                                "next-hop-type": "Spring",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup SPRING",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.19.198.26"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            },
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.174.132.237/32",
                                "interface-cost": "150",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Ext1",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.34.2.200/30",
                                "interface-cost": "205",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.34.2.250/32",
                                "interface-cost": "200",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            },
                            {
                                "address-prefix": "10.34.2.250/32",
                                "interface-cost": "200",
                                "next-hop-type": "Spring",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            },
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.34.2.251/32",
                                "interface-cost": "205",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            },
                            {
                                "address-prefix": "10.34.2.251/32",
                                "interface-cost": "205",
                                "next-hop-type": "Spring",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            },
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.15.0.0/30",
                                "interface-cost": "1001",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.19.198.26"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.64.0.0/30",
                                "interface-cost": "1201",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.55.0.0/24",
                                "interface-cost": "100",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-name": {"interface-name": "ge-0/0/3.0"}
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.169.196.212/30",
                                "interface-cost": "1200",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.169.196.216/30",
                                "interface-cost": "1205",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.169.196.241/32",
                                "interface-cost": "1201",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            },
                            {
                                "address-prefix": "10.169.196.241/32",
                                "interface-cost": "1201",
                                "next-hop-type": "Spring",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup SPRING",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            },
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.169.14.16/30",
                                "interface-cost": "105",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.169.14.32/30",
                                "interface-cost": "225",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.169.14.120/30",
                                "interface-cost": "100",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"}
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.169.14.128/30",
                                "interface-cost": "125",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.189.5.94"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.169.14.156/30",
                                "interface-cost": "200",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.169.14.240/32",
                                "interface-cost": "100",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            },
                            {
                                "address-prefix": "10.169.14.240/32",
                                "interface-cost": "100",
                                "next-hop-type": "Spring",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup SPRING",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            },
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.169.14.241/32",
                                "interface-cost": "105",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            },
                            {
                                "address-prefix": "10.169.14.241/32",
                                "interface-cost": "105",
                                "next-hop-type": "Spring",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            },
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.169.14.242/32",
                                "interface-cost": "100",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.169.14.243/32",
                                "interface-cost": "105",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.189.5.92/30",
                                "interface-cost": "5",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-name": {"interface-name": "ge-0/0/0.0"}
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.189.5.252/32",
                                "interface-cost": "0",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-name": {"interface-name": "lo0.0"}
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            },
                            {
                                "address-prefix": "10.189.5.252/32",
                                "interface-cost": "0",
                                "next-hop-type": "Spring",
                                "ospf-next-hop": {
                                    "next-hop-name": {"interface-name": "lo0.0"}
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            },
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.189.5.253/32",
                                "interface-cost": "5",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.189.5.94"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            },
                            {
                                "address-prefix": "10.189.5.253/32",
                                "interface-cost": "5",
                                "next-hop-type": "Spring",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.189.5.94"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            },
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "192.168.220.0/30",
                                "interface-cost": "1200",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "192.168.36.119/32",
                                "interface-cost": "10101",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "192.168.36.120/32",
                                "interface-cost": "10101",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "2567",
                                "interface-cost": "0",
                                "next-hop-type": "Mpls",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup MPLS",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "2567 (S=0)",
                                "interface-cost": "0",
                                "next-hop-type": "Mpls",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup MPLS",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "2568",
                                "interface-cost": "0",
                                "next-hop-type": "Mpls",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "2568 (S=0)",
                                "interface-cost": "0",
                                "next-hop-type": "Mpls",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "167966",
                                "interface-cost": "0",
                                "next-hop-type": "Mpls",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup MPLS",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.19.198.26"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "167966 (S=0)",
                                "interface-cost": "0",
                                "next-hop-type": "Mpls",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup MPLS",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.19.198.26"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "167967",
                                "interface-cost": "0",
                                "next-hop-type": "Mpls",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.19.198.26"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "167967 (S=0)",
                                "interface-cost": "0",
                                "next-hop-type": "Mpls",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.19.198.26"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "28985",
                                "interface-cost": "0",
                                "next-hop-type": "Mpls",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.189.5.94"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "28985 (S=0)",
                                "interface-cost": "0",
                                "next-hop-type": "Mpls",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.189.5.94"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "28986",
                                "interface-cost": "0",
                                "next-hop-type": "Mpls",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.189.5.94"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "28986 (S=0)",
                                "interface-cost": "0",
                                "next-hop-type": "Mpls",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.189.5.94"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "17000",
                                "interface-cost": "1201",
                                "next-hop-type": "Mpls",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup MPLS",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "16051",
                                "interface-cost": "100",
                                "next-hop-type": "Mpls",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup MPLS",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "16051 (S=0)",
                                "interface-cost": "100",
                                "next-hop-type": "Mpls",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup MPLS",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "16052",
                                "interface-cost": "105",
                                "next-hop-type": "Mpls",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "16061",
                                "interface-cost": "200",
                                "next-hop-type": "Mpls",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "16062",
                                "interface-cost": "205",
                                "next-hop-type": "Mpls",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "16063",
                                "interface-cost": "1201",
                                "next-hop-type": "Mpls",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup MPLS",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "16072",
                                "interface-cost": "5",
                                "next-hop-type": "Mpls",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.189.5.94"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "16073",
                                "interface-cost": "1001",
                                "next-hop-type": "Mpls",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup MPLS",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.19.198.26"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "16073 (S=0)",
                                "interface-cost": "1001",
                                "next-hop-type": "Mpls",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup MPLS",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.19.198.26"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                ]
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspfRouteBrief(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspfRouteBrief(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowOspfRouteDetail(unittest.TestCase):
    """ Unit tests for:
            * show ospf route detail
    """

    maxDiff = None

    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
        show ospf route detail
        Topology default Route Table:

        Prefix             Path  Route      NH       Metric NextHop       Nexthop
                        Type  Type       Type            Interface     Address/LSP
        10.36.3.3            Intra Router     IP         1201 ge-0/0/1.0    10.169.14.121
        area 0.0.0.8, origin 10.36.3.3, optional-capability 0x0
        10.100.5.5            Intra Router     IP         1200 ge-0/0/1.0    10.169.14.121
        area 0.0.0.8, origin 10.100.5.5, optional-capability 0x0
        10.19.198.239      Intra Router     IP         1000 ge-0/0/2.0    10.19.198.26
        area 0.0.0.8, origin 10.19.198.239, optional-capability 0x0
        10.34.2.250       Intra AS BR      IP          200 ge-0/0/1.0    10.169.14.121
        area 0.0.0.8, origin 10.34.2.250, optional-capability 0x2
        10.34.2.251       Intra AS BR      IP          205 ge-0/0/1.0    10.169.14.121
        area 0.0.0.8, origin 10.34.2.251, optional-capability 0x2
        10.169.196.241    Intra Router     IP         1200 ge-0/0/1.0    10.169.14.121
        area 0.0.0.8, origin 10.169.196.241, optional-capability 0x0
        10.169.14.240     Intra AS BR      IP          100 ge-0/0/1.0    10.169.14.121
        area 0.0.0.8, origin 10.169.14.240, optional-capability 0x2
        10.100.5.5/32         Intra Network    Spring     1201 ge-0/0/1.0    10.169.14.121
                                            Bkup SPRING     ge-0/0/0.0    10.189.5.94
        area 0.0.0.8, origin 10.100.5.5, priority medium
        10.19.198.24/30    Intra Network    IP         1000 ge-0/0/2.0
        area 0.0.0.8, origin 10.189.5.252, priority low
        10.19.198.28/30    Intra Network    IP         1005 ge-0/0/0.0    10.189.5.94
        area 0.0.0.8, origin 10.189.5.253, priority medium
        10.19.198.239/32   Intra Network    IP         1001 ge-0/0/2.0    10.19.198.26
        area 0.0.0.8, origin 10.19.198.239, priority medium
        10.19.198.239/32   Intra Network    Spring     1001 ge-0/0/2.0    10.19.198.26
                                            Bkup SPRING     ge-0/0/0.0    10.189.5.94
        area 0.0.0.8, origin 10.19.198.239, priority medium
        192.168.100.252/32 Ext1  Network    IP        32000 ge-0/0/1.0    10.169.14.121
        area 0.0.0.0, origin 10.169.14.240, priority medium
        192.168.36.48/30  Intra Network    IP        10100 ge-0/0/1.0    10.169.14.121
        area 0.0.0.8, origin 10.169.14.240, priority medium
        192.168.36.56/30  Intra Network    IP        10100 ge-0/0/1.0    10.169.14.121
        area 0.0.0.8, origin 10.169.14.240, priority medium
        192.168.36.119/32 Intra Network    IP        10101 ge-0/0/1.0    10.169.14.121
        area 0.0.0.8, origin 192.168.36.119, priority medium
        192.168.36.120/32 Intra Network    IP        10101 ge-0/0/1.0    10.169.14.121
        area 0.0.0.8, origin 192.168.36.120, priority medium
        2567               Intra Network    Mpls          0 ge-0/0/1.0    10.169.14.121
                                            Bkup MPLS       ge-0/0/0.0    10.189.5.94
        area 0.0.0.8, origin 10.189.5.252, priority medium
        2567 (S=0)         Intra Network    Mpls          0 ge-0/0/1.0    10.169.14.121
                                            Bkup MPLS       ge-0/0/0.0    10.189.5.94
        area 0.0.0.8, origin 10.189.5.252, priority medium
        2568               Intra Network    Mpls          0 ge-0/0/1.0    10.169.14.121
        area 0.0.0.8, origin 10.189.5.252, priority medium
        2568 (S=0)         Intra Network    Mpls          0 ge-0/0/1.0    10.169.14.121
        area 0.0.0.8, origin 10.189.5.252, priority medium
        167966             Intra Network    Mpls          0 ge-0/0/2.0    10.19.198.26
                                            Bkup MPLS       ge-0/0/0.0    10.189.5.94
        area 0.0.0.8, origin 10.189.5.252, priority medium
        167966 (S=0)       Intra Network    Mpls          0 ge-0/0/2.0    10.19.198.26
                                            Bkup MPLS       ge-0/0/0.0    10.189.5.94
        area 0.0.0.8, origin 10.189.5.252, priority medium
        167967             Intra Network    Mpls          0 ge-0/0/2.0    10.19.198.26
        area 0.0.0.8, origin 10.189.5.252, priority medium
        167967 (S=0)       Intra Network    Mpls          0 ge-0/0/2.0    10.19.198.26
        area 0.0.0.8, origin 10.189.5.252, priority medium
        16051 (S=0)        Intra Network    Mpls        100 ge-0/0/1.0    10.169.14.121
                                            Bkup MPLS       ge-0/0/0.0    10.189.5.94
        area 0.0.0.8, origin 10.169.14.240, priority medium
        16052              Intra Network    Mpls        105 ge-0/0/1.0    10.169.14.121
        area 0.0.0.8, origin 10.169.14.241, priority medium
        16061              Intra Network    Mpls        200 ge-0/0/1.0    10.169.14.121
        area 0.0.0.8, origin 10.34.2.250, priority medium
        16062              Intra Network    Mpls        205 ge-0/0/1.0    10.169.14.121
        area 0.0.0.8, origin 10.34.2.251, priority medium
        16063              Intra Network    Mpls       1201 ge-0/0/1.0    10.169.14.121
                                            Bkup MPLS       ge-0/0/0.0    10.189.5.94
        area 0.0.0.8, origin 10.169.196.241, priority medium
        16072              Intra Network    Mpls          5 ge-0/0/0.0    10.189.5.94
        area 0.0.0.8, origin 10.189.5.253, priority medium
        16073              Intra Network    Mpls       1001 ge-0/0/2.0    10.19.198.26
                                            Bkup MPLS       ge-0/0/0.0    10.189.5.94
        area 0.0.0.8, origin 10.19.198.239, priority medium
        16073 (S=0)        Intra Network    Mpls       1001 ge-0/0/2.0    10.19.198.26
                                            Bkup MPLS       ge-0/0/0.0    10.189.5.94
        area 0.0.0.8, origin 10.19.198.239, priority medium
                                            Bkup MPLS       ge-0/0/0.0    10.189.5.94
    """
    }

    golden_parsed_output = {
        "ospf-route-information": {
            "ospf-topology-route-table": {
                "ospf-route": [
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.36.3.3",
                                "interface-cost": "1201",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Router",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.100.5.5",
                                "interface-cost": "1200",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Router",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.19.198.239",
                                "interface-cost": "1000",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.19.198.26"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Router",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.34.2.250",
                                "interface-cost": "200",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "AS BR",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.34.2.251",
                                "interface-cost": "205",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "AS BR",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.169.196.241",
                                "interface-cost": "1200",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Router",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.169.14.240",
                                "interface-cost": "100",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "AS BR",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.100.5.5/32",
                                "interface-cost": "1201",
                                "next-hop-type": "Spring",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup SPRING",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.19.198.24/30",
                                "interface-cost": "1000",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-name": {"interface-name": "ge-0/0/2.0"}
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.19.198.28/30",
                                "interface-cost": "1005",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.189.5.94"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "10.19.198.239/32",
                                "interface-cost": "1001",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.19.198.26"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            },
                            {
                                "address-prefix": "10.19.198.239/32",
                                "interface-cost": "1001",
                                "next-hop-type": "Spring",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup SPRING",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.19.198.26"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            },
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "192.168.100.252/32",
                                "interface-cost": "32000",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Ext1",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "192.168.36.48/30",
                                "interface-cost": "10100",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "192.168.36.56/30",
                                "interface-cost": "10100",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "192.168.36.119/32",
                                "interface-cost": "10101",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "192.168.36.120/32",
                                "interface-cost": "10101",
                                "next-hop-type": "IP",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "2567",
                                "interface-cost": "0",
                                "next-hop-type": "Mpls",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup MPLS",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "2567 (S=0)",
                                "interface-cost": "0",
                                "next-hop-type": "Mpls",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup MPLS",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "2568",
                                "interface-cost": "0",
                                "next-hop-type": "Mpls",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "2568 (S=0)",
                                "interface-cost": "0",
                                "next-hop-type": "Mpls",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "167966",
                                "interface-cost": "0",
                                "next-hop-type": "Mpls",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup MPLS",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.19.198.26"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "167966 (S=0)",
                                "interface-cost": "0",
                                "next-hop-type": "Mpls",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup MPLS",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.19.198.26"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "167967",
                                "interface-cost": "0",
                                "next-hop-type": "Mpls",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.19.198.26"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "167967 (S=0)",
                                "interface-cost": "0",
                                "next-hop-type": "Mpls",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.19.198.26"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "16051 (S=0)",
                                "interface-cost": "100",
                                "next-hop-type": "Mpls",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup MPLS",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "16052",
                                "interface-cost": "105",
                                "next-hop-type": "Mpls",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "16061",
                                "interface-cost": "200",
                                "next-hop-type": "Mpls",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "16062",
                                "interface-cost": "205",
                                "next-hop-type": "Mpls",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "16063",
                                "interface-cost": "1201",
                                "next-hop-type": "Mpls",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup MPLS",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.169.14.121"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/1.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "16072",
                                "interface-cost": "5",
                                "next-hop-type": "Mpls",
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.189.5.94"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/0.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "16073",
                                "interface-cost": "1001",
                                "next-hop-type": "Mpls",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup MPLS",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.19.198.26"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                    {
                        "ospf-route-entry": [
                            {
                                "address-prefix": "16073 (S=0)",
                                "interface-cost": "1001",
                                "next-hop-type": "Mpls",
                                "ospf-backup-next-hop": {
                                    "ospf-backup-next-hop-address": "10.189.5.94",
                                    "ospf-backup-next-hop-interface": "ge-0/0/0.0",
                                    "ospf-backup-next-hop-type": "Bkup MPLS",
                                },
                                "ospf-next-hop": {
                                    "next-hop-address": {
                                        "interface-address": "10.19.198.26"
                                    },
                                    "next-hop-name": {"interface-name": "ge-0/0/2.0"},
                                },
                                "route-path-type": "Intra",
                                "route-type": "Network",
                            }
                        ]
                    },
                ]
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspfRouteDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspfRouteDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowOspfDatabaseNetworkLsaidDetail(unittest.TestCase):
    """ Unit tests for:
            * show ospf database network lsa-id {ipaddress} detail
    """

    device = Device(name="aDevice")

    maxDiff = None

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
        show ospf database network lsa-id 10.69.197.1 detail

        OSPF database, Area 192.168.76.0
      Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
    Network *10.69.197.1    192.168.219.235   0x80000026  1730  0x22 0x1b56  36
    mask 255.255.255.128
    attached router 192.168.219.235
    attached router 10.69.198.249
    attached router 192.168.219.236
    Topology default (ID 0)
        Type: Transit, Node ID: 192.168.219.236
          Metric: 0, Bidirectional
        Type: Transit, Node ID: 10.69.198.249
          Metric: 0, Bidirectional
        Type: Transit, Node ID: 192.168.219.235
          Metric: 0, Bidirectional
    """
    }

    golden_parsed_output = {
        "ospf-database-information": {
            "ospf-area-header": {"ospf-area": "192.168.76.0"},
            "ospf-database": {
                "@heading": "Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len",
                "advertising-router": "192.168.219.235",
                "age": "1730",
                "checksum": "0x1b56",
                "lsa-id": "10.69.197.1",
                "lsa-length": "36",
                "lsa-type": "Network",
                "options": "0x22",
                "ospf-network-lsa": {
                    "address-mask": "255.255.255.128",
                    "attached-router": [
                        "192.168.219.235",
                        "10.69.198.249",
                        "192.168.219.236",
                    ],
                    "ospf-lsa-topology": {
                        "ospf-lsa-topology-link": [
                            {
                                "link-type-name": "Transit",
                                "ospf-lsa-topology-link-metric": "0",
                                "ospf-lsa-topology-link-node-id": "192.168.219.236",
                                "ospf-lsa-topology-link-state": "Bidirectional",
                            },
                            {
                                "link-type-name": "Transit",
                                "ospf-lsa-topology-link-metric": "0",
                                "ospf-lsa-topology-link-node-id": "10.69.198.249",
                                "ospf-lsa-topology-link-state": "Bidirectional",
                            },
                            {
                                "link-type-name": "Transit",
                                "ospf-lsa-topology-link-metric": "0",
                                "ospf-lsa-topology-link-node-id": "192.168.219.235",
                                "ospf-lsa-topology-link-state": "Bidirectional",
                            },
                        ],
                        "ospf-topology-id": "default",
                        "ospf-topology-name": "default",
                    },
                },
                "our-entry": True,
                "sequence-number": "0x80000026",
            },
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspfDatabaseNetworkLsaidDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(ipaddress="10.69.197.1")

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspfDatabaseNetworkLsaidDetail(device=self.device)
        parsed_output = obj.parse(ipaddress="10.69.197.1")
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowOspfDatabaseLsaidDetail(unittest.TestCase):
    """ Unit tests for:
            * show ospf database lsa-id {ipaddress} detail
    """

    device = Device(name="aDevice")

    maxDiff = None

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
        show ospf database lsa-id 10.34.2.250 detail

        OSPF database, Area 0.0.0.8
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
        Router   10.34.2.250     10.34.2.250     0x80000048  1598  0x22 0xed79 108
        bits 0x2, link count 7
        id 10.34.2.251, data 10.34.2.201, Type PointToPoint (1)
            Topology count: 0, Default metric: 5
        id 10.34.2.200, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 5
        id 10.169.14.240, data 10.169.14.158, Type PointToPoint (1)
            Topology count: 0, Default metric: 100
        id 10.169.14.156, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 100
        id 10.16.0.0, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 1000
        id 192.168.220.0, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 1000
        id 10.34.2.250, data 255.255.255.255, Type Stub (3)
            Topology count: 0, Default metric: 0
        Topology default (ID 0)
            Type: PointToPoint, Node ID: 10.169.14.240
            Metric: 100, Bidirectional
            Type: PointToPoint, Node ID: 10.34.2.251
            Metric: 5, Bidirectional
            OSPF AS SCOPE link state database
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
        Extern   10.34.2.250     10.169.14.240   0x80000043  1075  0x22 0xd7f4  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 10.166.34.12
        Extern  *10.34.2.250     10.169.14.241   0x80000044   670  0x22 0xcffa  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 10.166.34.12
        """
    }

    golden_parsed_output = {
        "ospf-database-information": {
            "ospf-area-header": {"ospf-area": "0.0.0.8"},
            "ospf-database": [
                {
                    "advertising-router": "10.34.2.250",
                    "age": "1598",
                    "checksum": "0xed79",
                    "lsa-id": "10.34.2.250",
                    "lsa-length": "108",
                    "lsa-type": "Router",
                    "options": "0x22",
                    "ospf-router-lsa": {
                        "bits": "0x2",
                        "link-count": "7",
                        "ospf-link": [
                            {
                                "link-data": "10.34.2.201",
                                "link-id": "10.34.2.251",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "5",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.34.2.201",
                                "link-id": "10.34.2.251",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "5",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.34.2.200",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "5",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.34.2.200",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "5",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.169.14.158",
                                "link-id": "10.169.14.240",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "100",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "10.169.14.158",
                                "link-id": "10.169.14.240",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "100",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.169.14.156",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "100",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.169.14.156",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "100",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.16.0.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "10.16.0.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "192.168.220.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "192.168.220.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "10.34.2.250",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "0",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "10.34.2.250",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "0",
                                "ospf-topology-count": "0",
                            },
                        ],
                        "ospf-lsa-topology": {
                            "ospf-lsa-topology-link": [
                                {
                                    "link-type-name": "PointToPoint",
                                    "ospf-lsa-topology-link-metric": "100",
                                    "ospf-lsa-topology-link-node-id": "10.169.14.240",
                                    "ospf-lsa-topology-link-state": "Bidirectional",
                                },
                                {
                                    "link-type-name": "PointToPoint",
                                    "ospf-lsa-topology-link-metric": "5",
                                    "ospf-lsa-topology-link-node-id": "10.34.2.251",
                                    "ospf-lsa-topology-link-state": "Bidirectional",
                                },
                            ],
                            "ospf-topology-id": "0",
                            "ospf-topology-name": "default",
                        },
                    },
                    "sequence-number": "0x80000048",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "1075",
                    "checksum": "0xd7f4",
                    "lsa-id": "10.34.2.250",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "50",
                            "ospf-topology-name": "default",
                            "tag": "10.166.34.12",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x80000043",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "670",
                    "checksum": "0xcffa",
                    "lsa-id": "10.34.2.250",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "50",
                            "ospf-topology-name": "default",
                            "tag": "10.166.34.12",
                            "type-value": "1",
                        },
                    },
                    "our-entry": True,
                    "sequence-number": "0x80000044",
                },
            ],
        }
    }

    golden_output_2 = {
        "execute.return_value": """
        OSPF AS SCOPE link state database
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
        Extern   10.34.2.250     10.169.14.240   0x80000043  1075  0x22 0xd7f4  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 10.166.34.12
        Extern  *10.34.2.250     10.169.14.241   0x80000044   670  0x22 0xcffa  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 10.166.34.12
    """
    }

    golden_parsed_output_2 = {
        "ospf-database-information": {
            "ospf-database": [
                {
                    "advertising-router": "10.169.14.240",
                    "age": "1075",
                    "checksum": "0xd7f4",
                    "lsa-id": "10.34.2.250",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "50",
                            "ospf-topology-name": "default",
                            "tag": "10.166.34.12",
                            "type-value": "1",
                        },
                    },
                    "sequence-number": "0x80000043",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "670",
                    "checksum": "0xcffa",
                    "lsa-id": "10.34.2.250",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "50",
                            "ospf-topology-name": "default",
                            "tag": "10.166.34.12",
                            "type-value": "1",
                        },
                    },
                    "our-entry": True,
                    "sequence-number": "0x80000044",
                },
            ]
        }
    }

    golden_output_3 = {
        "execute.return_value": """
    show ospf database lsa-id 10.145.0.3 detail 

        OSPF database, Area 0.0.0.0
     Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len 
    Network *10.145.0.3         10.36.3.3          0x80000002    64  0x22 0x9958  36
      mask 255.255.255.0
      attached router 10.36.3.3
      attached router 10.64.4.4
      attached router 10.4.1.1
      Topology default (ID 0)
        Type: Transit, Node ID: 10.4.1.1
          Metric: 0, Bidirectional
        Type: Transit, Node ID: 10.64.4.4
          Metric: 0, Bidirectional
        Type: Transit, Node ID: 10.36.3.3
          Metric: 0, Bidirectional
    """
    }

    golden_parsed_output_3 = {
        "ospf-database-information": {
            "ospf-area-header": {"ospf-area": "0.0.0.0"},
            "ospf-database": [
                {
                    "advertising-router": "10.36.3.3",
                    "age": "64",
                    "checksum": "0x9958",
                    "lsa-id": "10.145.0.3",
                    "lsa-length": "36",
                    "lsa-type": "Network",
                    "options": "0x22",
                    "ospf-network-lsa": {
                        "address-mask": "255.255.255.0",
                        "attached-router": ["10.36.3.3", "10.64.4.4", "10.4.1.1"],
                        "ospf-lsa-topology": {
                            "ospf-lsa-topology-link": [
                                {
                                    "link-type-name": "Transit",
                                    "ospf-lsa-topology-link-metric": "0",
                                    "ospf-lsa-topology-link-node-id": "10.4.1.1",
                                    "ospf-lsa-topology-link-state": "Bidirectional",
                                },
                                {
                                    "link-type-name": "Transit",
                                    "ospf-lsa-topology-link-metric": "0",
                                    "ospf-lsa-topology-link-node-id": "10.64.4.4",
                                    "ospf-lsa-topology-link-state": "Bidirectional",
                                },
                                {
                                    "link-type-name": "Transit",
                                    "ospf-lsa-topology-link-metric": "0",
                                    "ospf-lsa-topology-link-node-id": "10.36.3.3",
                                    "ospf-lsa-topology-link-state": "Bidirectional",
                                },
                            ],
                            "ospf-topology-id": "0",
                            "ospf-topology-name": "default",
                        },
                    },
                    "our-entry": True,
                    "sequence-number": "0x80000002",
                }
            ],
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspfDatabaseLsaidDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(ipaddress="10.34.2.250")

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspfDatabaseLsaidDetail(device=self.device)
        parsed_output = obj.parse(ipaddress="10.34.2.250")

        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowOspfDatabaseLsaidDetail(device=self.device)
        parsed_output = obj.parse(ipaddress="10.34.2.250")

        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.device = Mock(**self.golden_output_3)
        obj = ShowOspfDatabaseLsaidDetail(device=self.device)
        parsed_output = obj.parse(ipaddress="10.145.0.3")
        self.assertEqual(parsed_output, self.golden_parsed_output_3)


class TestShowOspfRouteNetworkExtensive(unittest.TestCase):
    """ Unit tests for:
            * show ospf route network extensive
    """

    device = Device(name="aDevice")
    maxDiff = None

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
            show ospf route network extensive
        Topology default Route Table:

        Prefix             Path  Route      NH       Metric NextHop       Nexthop
                        Type  Type       Type            Interface     Address/LSP
        10.1.0.0/24         Ext2  Network    IP            0 ge-0/0/0.0    10.70.0.4
        area 0.0.0.0, origin 10.36.3.3, priority medium
        10.4.1.1/32         Intra Network    IP            0 lo0.0
        area 0.0.0.0, origin 10.4.1.1, priority low
        10.16.2.2/32         Intra Network    IP            1 ge-0/0/1.0    10.135.0.2
        area 0.0.0.0, origin 10.16.2.2, priority medium
        10.36.3.3/32         Intra Network    IP            2 ge-0/0/0.0    10.70.0.4
        area 0.0.0.0, origin 10.36.3.3, priority medium
        10.64.4.4/32         Intra Network    IP            1 ge-0/0/0.0    10.70.0.4
        area 0.0.0.0, origin 10.64.4.4, priority medium
        10.145.0.0/24        Ext2  Network    IP            0 ge-0/0/0.0    10.70.0.4
        area 0.0.0.0, origin 10.36.3.3, priority medium
        10.135.0.0/24        Intra Network    IP            1 ge-0/0/1.0
        area 0.0.0.0, origin 10.4.1.1, priority low
        10.70.0.0/24        Intra Network    IP            1 ge-0/0/0.0
        area 0.0.0.0, origin 10.4.1.1, priority low
        10.205.0.0/24        Intra Network    IP            2 ge-0/0/0.0    10.70.0.4
        area 0.0.0.0, origin 10.64.4.4, priority medium
    """
    }

    golden_parsed_output = {
        "ospf-route-information": {
            "ospf-topology-route-table": {
                "ospf-route": [
                    {
                        "ospf-route-entry": {
                            "address-prefix": "10.1.0.0/24",
                            "interface-cost": "0",
                            "next-hop-type": "IP",
                            "ospf-area": "0.0.0.0",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.70.0.4"
                                },
                                "next-hop-name": {
                                    "interface-name": "ge-0/0/0.0"
                                }
                            },
                            "route-origin": "10.36.3.3",
                            "route-path-type": "Ext2",
                            "route-priority": "medium",
                            "route-type": "Network",
                        }
                    },
                    {
                        "ospf-route-entry": {
                            "address-prefix": "10.4.1.1/32",
                            "interface-cost": "0",
                            "next-hop-type": "IP",
                            "ospf-area": "0.0.0.0",
                            "ospf-next-hop": {
                                "next-hop-name": {"interface-name": "lo0.0"}
                            },
                            "route-origin": "10.4.1.1",
                            "route-path-type": "Intra",
                            "route-priority": "low",
                            "route-type": "Network",
                        }
                    },
                    {
                        "ospf-route-entry": {
                            "address-prefix": "10.16.2.2/32",
                            "interface-cost": "1",
                            "next-hop-type": "IP",
                            "ospf-area": "0.0.0.0",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.135.0.2"
                                },
                                "next-hop-name": {
                                    "interface-name": "ge-0/0/1.0"
                                }
                            },
                            "route-origin": "10.16.2.2",
                            "route-path-type": "Intra",
                            "route-priority": "medium",
                            "route-type": "Network",
                        }
                    },
                    {
                        "ospf-route-entry": {
                            "address-prefix": "10.36.3.3/32",
                            "interface-cost": "2",
                            "next-hop-type": "IP",
                            "ospf-area": "0.0.0.0",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.70.0.4"
                                },
                                "next-hop-name": {
                                    "interface-name": "ge-0/0/0.0"
                                }
                            },
                            "route-origin": "10.36.3.3",
                            "route-path-type": "Intra",
                            "route-priority": "medium",
                            "route-type": "Network",
                        }
                    },
                    {
                        "ospf-route-entry": {
                            "address-prefix": "10.64.4.4/32",
                            "interface-cost": "1",
                            "next-hop-type": "IP",
                            "ospf-area": "0.0.0.0",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.70.0.4"
                                },
                                "next-hop-name": {
                                    "interface-name": "ge-0/0/0.0"
                                }
                            },
                            "route-origin": "10.64.4.4",
                            "route-path-type": "Intra",
                            "route-priority": "medium",
                            "route-type": "Network",
                        }
                    },
                    {
                        "ospf-route-entry": {
                            "address-prefix": "10.145.0.0/24",
                            "interface-cost": "0",
                            "next-hop-type": "IP",
                            "ospf-area": "0.0.0.0",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.70.0.4"
                                },
                                "next-hop-name": {
                                    "interface-name": "ge-0/0/0.0"
                                }
                            },
                            "route-origin": "10.36.3.3",
                            "route-path-type": "Ext2",
                            "route-priority": "medium",
                            "route-type": "Network",
                        }
                    },
                    {
                        "ospf-route-entry": {
                            "address-prefix": "10.135.0.0/24",
                            "interface-cost": "1",
                            "next-hop-type": "IP",
                            "ospf-area": "0.0.0.0",
                            "ospf-next-hop": {
                                "next-hop-name": {"interface-name": "ge-0/0/1.0"}
                            },
                            "route-origin": "10.4.1.1",
                            "route-path-type": "Intra",
                            "route-priority": "low",
                            "route-type": "Network",
                        }
                    },
                    {
                        "ospf-route-entry": {
                            "address-prefix": "10.70.0.0/24",
                            "interface-cost": "1",
                            "next-hop-type": "IP",
                            "ospf-area": "0.0.0.0",
                            "ospf-next-hop": {
                                "next-hop-name": {"interface-name": "ge-0/0/0.0"}
                            },
                            "route-origin": "10.4.1.1",
                            "route-path-type": "Intra",
                            "route-priority": "low",
                            "route-type": "Network",
                        }
                    },
                    {
                        "ospf-route-entry": {
                            "address-prefix": "10.205.0.0/24",
                            "interface-cost": "2",
                            "next-hop-type": "IP",
                            "ospf-area": "0.0.0.0",
                            "ospf-next-hop": {
                                "next-hop-address": {
                                    "interface-address": "10.70.0.4"
                                },
                                "next-hop-name": {
                                    "interface-name": "ge-0/0/0.0"
                                }
                            },
                            "route-origin": "10.64.4.4",
                            "route-path-type": "Intra",
                            "route-priority": "medium",
                            "route-type": "Network",
                        }
                    },
                ],
                "ospf-topology-name": "default",
            }
        }
    }

    def test_show_ospf_route_network_extensive_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspfRouteNetworkExtensive(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_show_ospf_route_network_extensive(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspfRouteNetworkExtensive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()