
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# junos show_ospf
from genie.libs.parser.junos.show_ospf import (ShowOspfInterface,
                                               ShowOspfInterfaceBrief,
                                               ShowOspfInterfaceDetail,
                                               ShowOspfNeighbor,
                                               ShowOspfDatabaseAdvertisingRouterSelfDetail,
                                               ShowOspfInterfaceExtensive)


class test_show_ospf_interface(unittest.TestCase):
    """ Unit tests for:
            * show ospf interface
            * show ospf interface {interface}
    """

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
    show ospf interface
    Interface           State   Area            DR ID           BDR ID          Nbrs
    ge-0/0/0.0          PtToPt  0.0.0.1         0.0.0.0         0.0.0.0            1
    ge-0/0/1.0          PtToPt  0.0.0.1         0.0.0.0         0.0.0.0            1
    '''}

    golden_parsed_output = {
        'instance': {
            'master': {
                'areas': {
                    '0.0.0.1': {
                        'interfaces': {
                            'ge-0/0/0.0': {
                                'state': 'PtToPt',
                                'dr_id': '0.0.0.0',
                                'bdr_id': '0.0.0.0',
                                'nbrs_count': 1
                            },
                            'ge-0/0/1.0': {
                                'state': 'PtToPt',
                                'dr_id': '0.0.0.0',
                                'bdr_id': '0.0.0.0',
                                'nbrs_count': 1
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_interface = {'execute.return_value': '''
        show ospf interface ge-0/0/1.0
        Interface           State   Area            DR ID           BDR ID          Nbrs
        ge-0/0/1.0          PtToPt  0.0.0.1         0.0.0.0         0.0.0.0            1
        '''}

    golden_parsed_output_interface = {
        'instance': {
            'master': {
                'areas': {
                    '0.0.0.1': {
                        'interfaces': {
                            'ge-0/0/1.0': {
                                'state': 'PtToPt',
                                'dr_id': '0.0.0.0',
                                'bdr_id': '0.0.0.0',
                                'nbrs_count': 1
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_instance = {'execute.return_value': '''
        show ospf interface instance master
        Interface           State   Area            DR ID           BDR ID          Nbrs
        ge-0/0/0.0          PtToPt  0.0.0.1         0.0.0.0         0.0.0.0            1
        ge-0/0/1.0          PtToPt  0.0.0.1         0.0.0.0         0.0.0.0            1
        '''}

    golden_parsed_output_instance = {
        'instance': {
            'master': {
                'areas': {
                    '0.0.0.1': {
                        'interfaces': {
                            'ge-0/0/0.0': {
                                'state': 'PtToPt',
                                'dr_id': '0.0.0.0',
                                'bdr_id': '0.0.0.0',
                                'nbrs_count': 1
                            },
                            'ge-0/0/1.0': {
                                'state': 'PtToPt',
                                'dr_id': '0.0.0.0',
                                'bdr_id': '0.0.0.0',
                                'nbrs_count': 1
                            }
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
        parsed_output = obj.parse(interface='ge-0/0/1.0')
        self.assertEqual(parsed_output, self.golden_parsed_output_interface)

    def test_show_ospf_interface_instance(self):
        self.device = Mock(**self.golden_output_instance)
        obj = ShowOspfInterface(device=self.device)
        parsed_output = obj.parse(instance='master')
        self.assertEqual(parsed_output, self.golden_parsed_output_instance)


class test_show_ospf_interface_brief(unittest.TestCase):
    """ Unit tests for:
            * show ospf interface brief
            * show ospf interface brief instance {instance}
            * show ospf interface {interface} brief
    """

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
    show ospf interface brief
    Interface           State   Area            DR ID           BDR ID          Nbrs
    ge-0/0/2.0          BDR     0.0.0.1         10.16.2.2         10.64.4.4            5
    '''}

    golden_parsed_output = {
        'instance': {
            'master': {
                'areas': {
                    '0.0.0.1': {
                        'interfaces': {
                            'ge-0/0/2.0': {
                                'state': 'BDR',
                                'dr_id': '10.16.2.2',
                                'bdr_id': '10.64.4.4',
                                'nbrs_count': 5,
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output_master = {'execute.return_value': '''
    show ospf interface brief instance master
    Interface           State   Area            DR ID           BDR ID          Nbrs
    ge-0/0/4.0          BDR     0.0.0.4         10.64.4.4         192.168.10.22    2
    ge-0/0/5.0          BDR     0.0.0.4         10.16.2.2         10.16.2.2          3
    ge-0/0/6.0          DR      0.0.0.4         10.64.4.4         192.168.10.22    4
    lo1.0               DR      0.0.0.4         10.16.2.2         0.0.0.0          0
    '''}

    golden_parsed_output_master = {
    'instance': {
        'master': {
            'areas': {
                '0.0.0.4': {
                    'interfaces': {
                        'ge-0/0/4.0': {
                            'state': 'BDR',
                            'dr_id': '10.64.4.4',
                            'bdr_id': '192.168.10.22',
                            'nbrs_count': 2,
                            },
                        'ge-0/0/5.0': {
                            'state': 'BDR',
                            'dr_id': '10.16.2.2',
                            'bdr_id': '10.16.2.2',
                            'nbrs_count': 3,
                            },
                        'ge-0/0/6.0': {
                            'state': 'DR',
                            'dr_id': '10.64.4.4',
                            'bdr_id': '192.168.10.22',
                            'nbrs_count': 4,
                            },
                        'lo1.0': {
                            'state': 'DR',
                            'dr_id': '10.16.2.2',
                            'bdr_id': '0.0.0.0',
                            'nbrs_count': 0,
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output_interface = {'execute.return_value': '''
    show ospf interface ge-0/0/4.0 brief
    Interface           State   Area            DR ID           BDR ID          Nbrs
    ge-0/0/4.0          PtToPt  0.0.0.1         10.16.2.1         10.64.2.4            1
    '''}

    golden_parsed_output_interface = {
        'instance': {
            'master': {
                'areas': {
                    '0.0.0.1': {
                        'interfaces': {
                            'ge-0/0/4.0': {
                                'state': 'PtToPt',
                                'dr_id': '10.16.2.1',
                                'bdr_id': '10.64.2.4',
                                'nbrs_count': 1,
                            },
                        },
                    },
                },
            },
        },
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
        parsed_output = obj.parse(instance='master')
        self.assertEqual(parsed_output, self.golden_parsed_output_master)

    def test_show_ospf_interface_interface_brief(self):
        self.device = Mock(**self.golden_output_interface)
        obj = ShowOspfInterfaceBrief(device=self.device)
        parsed_output = obj.parse(interface='ge-0/0/4.0')
        self.assertEqual(parsed_output, self.golden_parsed_output_interface)


class test_show_ospf_interface_detail(unittest.TestCase):
    """ Unit tests for:
            * show ospf interface detail
            * show ospf interface {interface} detail
    """

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
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
    '''}

    golden_parsed_output = {
        'instance': {
            'master': {
                'areas': {
                    '0.0.0.1': {
                        'interfaces': {
                            'ge-0/0/0.0': {
                                'state': 'PtToPt',
                                'dr_id': '0.0.0.0',
                                'bdr_id': '0.0.0.0',
                                'nbrs_count': 1,
                                'type': 'P2P',
                                'address': '172.16.94.1',
                                'mask': '255.255.255.0',
                                'mtu': 500,
                                'cost': 50,
                                'adj_count': 1,
                                'hello': 10,
                                'dead': 20,
                                'rexmit': 10,
                                'ospf_stub_type': 'Not Stub',
                                'authentication_type': 'None',
                                'ospf_interface': {
                                    'protection_type': 'Post Convergence',
                                    'tilfa': {
                                        'prot_link': 'Enabled',
                                        'prot_fate': 'No',
                                        'prot_srlg': 'No',
                                        'prot_node': 50
                                    },
                                    'topology': {
                                        'default': {
                                            'id': 0,
                                            'metric': 50
                                        }
                                    }
                                }
                            },
                            'ge-0/0/1.0': {
                                'state': 'PtToPt',
                                'dr_id': '0.0.0.0',
                                'bdr_id': '0.0.0.0',
                                'nbrs_count': 1,
                                'type': 'P2P',
                                'address': '172.16.94.1',
                                'mask': '255.255.255.0',
                                'mtu': 500,
                                'cost': 100,
                                'adj_count': 1,
                                'hello': 10,
                                'dead': 10,
                                'rexmit': 5,
                                'ospf_stub_type': 'Not Stub',
                                'authentication_type': 'None',
                                'ospf_interface': {
                                    'protection_type': 'Post Convergence',
                                    'tilfa': {
                                        'prot_link': 'Enabled',
                                        'prot_fate': 'No',
                                        'prot_srlg': 'No',
                                        'prot_node': 100
                                    },
                                    'topology': {
                                        'default': {
                                            'id': 0,
                                            'metric': 100
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_interface = {'execute.return_value': '''
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
    '''}

    golden_parsed_output_interface = {
        'instance': {
            'master': {
                'areas': {
                    '0.0.0.1': {
                        'interfaces': {
                            'ge-0/0/1.0': {
                                'state': 'PtToPt',
                                'dr_id': '0.0.0.0',
                                'bdr_id': '0.0.0.0',
                                'nbrs_count': 1,
                                'type': 'P2P',
                                'address': '172.16.94.1',
                                'mask': '255.255.255.0',
                                'mtu': 500,
                                'cost': 100,
                                'adj_count': 1,
                                'hello': 10,
                                'dead': 10,
                                'rexmit': 5,
                                'ospf_stub_type': 'Not Stub',
                                'authentication_type': 'None',
                                'ospf_interface': {
                                    'protection_type': 'Post Convergence',
                                    'tilfa': {
                                        'prot_link': 'Enabled',
                                        'prot_fate': 'No',
                                        'prot_srlg': 'No',
                                        'prot_node': 100
                                    },
                                    'topology': {
                                        'default': {
                                            'id': 0,
                                            'metric': 100
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_instance = {'execute.return_value': '''
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
        '''}

    golden_parsed_output_instance = {
        'instance': {
            'master': {
                'areas': {
                    '0.0.0.1': {
                        'interfaces': {
                            'ge-0/0/0.0': {
                                'state': 'PtToPt',
                                'dr_id': '0.0.0.0',
                                'bdr_id': '0.0.0.0',
                                'nbrs_count': 1,
                                'type': 'P2P',
                                'address': '172.16.94.1',
                                'mask': '255.255.255.0',
                                'mtu': 500,
                                'cost': 50,
                                'adj_count': 1,
                                'hello': 10,
                                'dead': 20,
                                'rexmit': 10,
                                'ospf_stub_type': 'Not Stub',
                                'authentication_type': 'None',
                                'ospf_interface': {
                                    'protection_type': 'Post Convergence',
                                    'tilfa': {
                                        'prot_link': 'Enabled',
                                        'prot_fate': 'No',
                                        'prot_srlg': 'No',
                                        'prot_node': 50
                                    },
                                    'topology': {
                                        'default': {
                                            'id': 0,
                                            'metric': 50
                                        }
                                    }
                                }
                            },
                            'ge-0/0/1.0': {
                                'state': 'PtToPt',
                                'dr_id': '0.0.0.0',
                                'bdr_id': '0.0.0.0',
                                'nbrs_count': 1,
                                'type': 'P2P',
                                'address': '172.16.94.1',
                                'mask': '255.255.255.0',
                                'mtu': 500,
                                'cost': 100,
                                'adj_count': 1,
                                'hello': 10,
                                'dead': 10,
                                'rexmit': 5,
                                'ospf_stub_type': 'Not Stub',
                                'authentication_type': 'None',
                                'ospf_interface': {
                                    'protection_type': 'Post Convergence',
                                    'tilfa': {
                                        'prot_link': 'Enabled',
                                        'prot_fate': 'No',
                                        'prot_srlg': 'No',
                                        'prot_node': 100
                                    },
                                    'topology': {
                                        'default': {
                                            'id': 0,
                                            'metric': 100
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_interface_instance = {'execute.return_value': '''
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
        '''}

    golden_parsed_output_interface_instance = {
        'instance': {
            'master': {
                'areas': {
                    '0.0.0.1': {
                        'interfaces': {
                            'ge-0/0/1.0': {
                                'state': 'PtToPt',
                                'dr_id': '0.0.0.0',
                                'bdr_id': '0.0.0.0',
                                'nbrs_count': 1,
                                'type': 'P2P',
                                'address': '172.16.94.1',
                                'mask': '255.255.255.0',
                                'mtu': 500,
                                'cost': 100,
                                'adj_count': 1,
                                'hello': 10,
                                'dead': 10,
                                'rexmit': 5,
                                'ospf_stub_type': 'Not Stub',
                                'authentication_type': 'None',
                                'ospf_interface': {
                                    'protection_type': 'Post Convergence',
                                    'tilfa': {
                                        'prot_link': 'Enabled',
                                        'prot_fate': 'No',
                                        'prot_srlg': 'No',
                                        'prot_node': 100
                                    },
                                    'topology': {
                                        'default': {
                                            'id': 0,
                                            'metric': 100
                                        }
                                    }
                                }
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
        parsed_output = obj.parse(interface='ge-0/0/1.0')
        self.assertEqual(parsed_output, self.golden_parsed_output_interface)

    def test_show_ospf_interface_detail_instance(self):
        self.device = Mock(**self.golden_output_instance)
        obj = ShowOspfInterfaceDetail(device=self.device)
        parsed_output = obj.parse(instance='master')
        self.assertEqual(parsed_output, self.golden_parsed_output_instance)

    def test_show_ospf_interface_detail_interface_instance(self):
        self.device = Mock(**self.golden_output_interface_instance)
        obj = ShowOspfInterfaceDetail(device=self.device)
        parsed_output = obj.parse(interface='ge-0/0/1.0', instance='master')
        self.assertEqual(parsed_output, self.golden_parsed_output_interface_instance)

class TestShowOspfNeighbor(unittest.TestCase):
    """ Unit tests for:
            * show ospf neighbor
    """

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show ospf neighbor
        Address          Interface              State     ID               Pri  Dead
        10.189.5.94      ge-0/0/0.0             Full      10.189.5.253     128    32
        10.169.14.121   ge-0/0/1.0             Full      10.169.14.240   128    33
        10.19.198.26     ge-0/0/2.0             Full      10.19.198.239      1    33
        '''}

    golden_parsed_output = {
        'ospf-neighbor-information': {
            'ospf-neighbor': [
                {
                    'neighbor-address': '10.189.5.94',
                    'interface-name': 'ge-0/0/0.0',
                    'ospf-neighbor-state': 'Full',
                    'neighbor-id': '10.189.5.253',
                    'neighbor-priority': '128',
                    'activity-timer': '32'},
                {
                    'neighbor-address': '10.169.14.121',
                    'interface-name': 'ge-0/0/1.0',
                    'ospf-neighbor-state': 'Full',
                    'neighbor-id': '10.169.14.240',
                    'neighbor-priority': '128',
                    'activity-timer': '33'},
                {
                    'neighbor-address': '10.19.198.26',
                    'interface-name': 'ge-0/0/2.0',
                    'ospf-neighbor-state': 'Full',
                    'neighbor-id': '10.19.198.239',
                    'neighbor-priority': '1', 'activity-timer': '33'
                }],
        },
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

class TestShowOspfDatabaseAdvertisingRouterSelfDetail(unittest.TestCase):

    maxDiff = None

    device = Device(name="test-device")

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
            show ospf database advertising-router self detail

            OSPF database, Area 0.0.0.8
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
        Router  *111.87.5.252     111.87.5.252     0x80001b9e  1801  0x22 0x1e2  120
        bits 0x2, link count 8
        id 111.87.5.253, data 111.87.5.93, Type PointToPoint (1)
            Topology count: 0, Default metric: 5
        id 111.87.5.92, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 5
        id 106.187.14.240, data 106.187.14.122, Type PointToPoint (1)
            Topology count: 0, Default metric: 100
        id 106.187.14.120, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 100
        id 27.86.198.239, data 27.86.198.25, Type PointToPoint (1)
            Topology count: 0, Default metric: 1000
        id 27.86.198.24, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 1000
        id 100.0.0.0, data 255.255.255.0, Type Stub (3)
            Topology count: 0, Default metric: 100
        id 111.87.5.252, data 255.255.255.255, Type Stub (3)
            Topology count: 0, Default metric: 0
        Topology default (ID 0)
            Type: PointToPoint, Node ID: 27.86.198.239
            Metric: 1000, Bidirectional
            Type: PointToPoint, Node ID: 106.187.14.240
            Metric: 100, Bidirectional
            Type: PointToPoint, Node ID: 111.87.5.253
            Metric: 5, Bidirectional
        OpaqArea*1.0.0.1          111.87.5.252     0x80001a15   424  0x22 0xd49a  28
        Opaque LSA
        RtrAddr (1), length 4:
            111.87.5.252
        OpaqArea*1.0.0.3          111.87.5.252     0x80000322   153  0x22 0x95cd 136
        Opaque LSA
        Link (2), length 112:
            Linktype (1), length 1:
            1
            LinkID (2), length 4:
            111.87.5.253
            LocIfAdr (3), length 4:
            111.87.5.93
            RemIfAdr (4), length 4:
            111.87.5.94
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
        OpaqArea*1.0.0.4          111.87.5.252     0x800013e8  2604  0x22 0xb804 136
        Opaque LSA
        Link (2), length 112:
            Linktype (1), length 1:
            1
            LinkID (2), length 4:
            106.187.14.240
            LocIfAdr (3), length 4:
            106.187.14.122
            RemIfAdr (4), length 4:
            106.187.14.121
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
        OpaqArea*1.0.0.5          111.87.5.252     0x800001bb  1505  0x22 0x79b5 136
        Opaque LSA
        Link (2), length 112:
            Linktype (1), length 1:
            1
            LinkID (2), length 4:
            27.86.198.239
            LocIfAdr (3), length 4:
            27.86.198.25
            RemIfAdr (4), length 4:
            27.86.198.26
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
        OpaqArea*4.0.0.0          111.87.5.252     0x80001a2a   964  0x22 0xe5ef  44
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
        OpaqArea*7.0.0.1          111.87.5.252     0x80001b9e  1801  0x22 0x8c7f  44
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
                111.87.5.252
            Prefix Sid (2), length 8:
            Flags (1), length 1:
                0x00
            MT ID (2), length 1:
                0
            Algorithm (3), length 1:
                0
            SID (4), length 4:
                71
        OpaqArea*8.0.0.52         111.87.5.252     0x80000308   694  0x22 0x7efa  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            106.187.14.240
            Link Data (3), length 4:
            106.187.14.122
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
        OpaqArea*8.0.0.54         111.87.5.252     0x800002dc  1235  0x22 0x1839  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            111.87.5.253
            Link Data (3), length 4:
            111.87.5.93
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
        OpaqArea*8.0.0.55         111.87.5.252     0x800001bb  2069  0x22 0x92eb  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            27.86.198.239
            Link Data (3), length 4:
            27.86.198.25
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
        Extern  *106.187.14.240   111.87.5.252     0x80001a3a  2336  0x22 0xc3fb  36
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
                    "advertising-router": "111.87.5.252",
                    "age": "1801",
                    "checksum": "0x1e2",
                    "lsa-id": "111.87.5.252",
                    "lsa-length": "120",
                    "lsa-type": "Router",
                    "options": "0x22",
                    "ospf-router-lsa": {
                        "bits": "0x2",
                        "link-count": "8",
                        "ospf-link": [
                            {
                                "link-data": "111.87.5.93",
                                "link-id": "111.87.5.253",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "5",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "111.87.5.93",
                                "link-id": "111.87.5.253",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "5",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "111.87.5.92",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "5",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "111.87.5.92",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "5",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "106.187.14.122",
                                "link-id": "106.187.14.240",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "100",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "106.187.14.122",
                                "link-id": "106.187.14.240",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "100",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "106.187.14.120",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "100",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "106.187.14.120",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "100",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "27.86.198.25",
                                "link-id": "27.86.198.239",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "27.86.198.25",
                                "link-id": "27.86.198.239",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "27.86.198.24",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "27.86.198.24",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1000",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.0",
                                "link-id": "100.0.0.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "100",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.0",
                                "link-id": "100.0.0.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "100",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "111.87.5.252",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "0",
                                "ospf-topology-count": "0",
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "111.87.5.252",
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
                                    "ospf-lsa-topology-link-node-id": "27.86.198.239",
                                    "ospf-lsa-topology-link-state": "Bidirectional",
                                },
                                {
                                    "link-type-name": "PointToPoint",
                                    "ospf-lsa-topology-link-metric": "100",
                                    "ospf-lsa-topology-link-node-id": "106.187.14.240",
                                    "ospf-lsa-topology-link-state": "Bidirectional",
                                },
                                {
                                    "link-type-name": "PointToPoint",
                                    "ospf-lsa-topology-link-metric": "5",
                                    "ospf-lsa-topology-link-node-id": "111.87.5.253",
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
                    "advertising-router": "111.87.5.252",
                    "age": "424",
                    "checksum": "0xd49a",
                    "lsa-id": "1.0.0.1",
                    "lsa-length": "28",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "tlv-block": {
                            "formatted-tlv-data": "111.87.5.252",
                            "tlv-length": "4",
                            "tlv-type-name": "RtrAddr",
                            "tlv-type-value": "1",
                        }
                    },
                    "our-entry": True,
                    "sequence-number": "0x80001a15",
                },
                {
                    "advertising-router": "111.87.5.252",
                    "age": "153",
                    "checksum": "0x95cd",
                    "lsa-id": "1.0.0.3",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "111.87.5.253",
                                "111.87.5.93",
                                "111.87.5.94",
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
                                "Local " "333, " "Remote " "0",
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
                    "advertising-router": "111.87.5.252",
                    "age": "2604",
                    "checksum": "0xb804",
                    "lsa-id": "1.0.0.4",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "106.187.14.240",
                                "106.187.14.122",
                                "106.187.14.121",
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
                                "Local " "334, " "Remote " "0",
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
                    "advertising-router": "111.87.5.252",
                    "age": "1505",
                    "checksum": "0x79b5",
                    "lsa-id": "1.0.0.5",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "27.86.198.239",
                                "27.86.198.25",
                                "27.86.198.26",
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
                                "Local " "336, " "Remote " "0",
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
                    "advertising-router": "111.87.5.252",
                    "age": "964",
                    "checksum": "0xe5ef",
                    "lsa-id": "4.0.0.0",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": ["0", "8000", "16000"],
                            "tlv-length": ["1", "12", "3", "3", "3"],
                            "tlv-type-name": [
                                "Algo",
                                "SID/Label " "Range",
                                "Range " "Size",
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
                    "advertising-router": "111.87.5.252",
                    "age": "1801",
                    "checksum": "0x8c7f",
                    "lsa-id": "7.0.0.1",
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
                                "111.87.5.252",
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
                                "Route " "Type",
                                "Prefix " "Length",
                                "AF",
                                "Flags",
                                "Prefix",
                                "Prefix " "Sid",
                                "Flags",
                                "MT " "ID",
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
                            "tlv-type-name": "Extended " "Prefix",
                            "tlv-type-value": "1",
                        },
                    },
                    "our-entry": True,
                    "sequence-number": "0x80001b9e",
                },
                {
                    "advertising-router": "111.87.5.252",
                    "age": "694",
                    "checksum": "0x7efa",
                    "lsa-id": "8.0.0.52",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "106.187.14.240",
                                "106.187.14.122",
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
                                "Link " "Type",
                                "Link " "Id",
                                "Link " "Data",
                                "Adjacency " "Sid",
                                "Flags",
                                "MT " "ID",
                                "Weight",
                                "Label",
                                "Adjacency " "Sid",
                                "Flags",
                                "MT " "ID",
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
                            "tlv-type-name": "Extended " "Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "our-entry": True,
                    "sequence-number": "0x80000308",
                },
                {
                    "advertising-router": "111.87.5.252",
                    "age": "1235",
                    "checksum": "0x1839",
                    "lsa-id": "8.0.0.54",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "111.87.5.253",
                                "111.87.5.93",
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
                                "Link " "Type",
                                "Link " "Id",
                                "Link " "Data",
                                "Adjacency " "Sid",
                                "Flags",
                                "MT " "ID",
                                "Weight",
                                "Label",
                                "Adjacency " "Sid",
                                "Flags",
                                "MT " "ID",
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
                            "tlv-type-name": "Extended " "Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "our-entry": True,
                    "sequence-number": "0x800002dc",
                },
                {
                    "advertising-router": "111.87.5.252",
                    "age": "2069",
                    "checksum": "0x92eb",
                    "lsa-id": "8.0.0.55",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "27.86.198.239",
                                "27.86.198.25",
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
                                "Link " "Type",
                                "Link " "Id",
                                "Link " "Data",
                                "Adjacency " "Sid",
                                "Flags",
                                "MT " "ID",
                                "Weight",
                                "Label",
                                "Adjacency " "Sid",
                                "Flags",
                                "MT " "ID",
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
                            "tlv-type-name": "Extended " "Link",
                            "tlv-type-value": "1",
                        },
                    },
                    "our-entry": True,
                    "sequence-number": "0x800001bb",
                },
                {
                    "advertising-router": "111.87.5.252",
                    "age": "2336",
                    "checksum": "0xc3fb",
                    "lsa-id": "106.187.14.240",
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

class TestShowOspfInterfaceExtensive(unittest.TestCase):
    """ Unit tests for:
            * show ospf neighbor
    """

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
                show ospf interface extensive
        Interface           State   Area            DR ID           BDR ID          Nbrs
        ge-0/0/0.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
        Type: P2P, Address: 111.87.5.93, Mask: 255.255.255.252, MTU: 1500, Cost: 5
        Adj count: 1
        Hello: 10, Dead: 40, ReXmit: 5, Not Stub
        Auth type: None
        Protection type: Post Convergence
        Post convergence protection: Enabled, Fate sharing: No, SRLG: No, Node cost: 100
        Topology default (ID 0) -> Cost: 5
        ge-0/0/1.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
        Type: P2P, Address: 106.187.14.122, Mask: 255.255.255.252, MTU: 1500, Cost: 100
        Adj count: 1
        Hello: 10, Dead: 40, ReXmit: 5, Not Stub
        Auth type: None
        Protection type: Post Convergence
        Post convergence protection: Enabled, Fate sharing: No, SRLG: No, Node cost: 100
        Topology default (ID 0) -> Cost: 100
        ge-0/0/2.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
        Type: P2P, Address: 27.86.198.25, Mask: 255.255.255.252, MTU: 1500, Cost: 1000
        Adj count: 1
        Hello: 10, Dead: 40, ReXmit: 5, Not Stub
        Auth type: None
        Protection type: Post Convergence
        Post convergence protection: Enabled, Fate sharing: No, SRLG: No, Node cost: 100
        Topology default (ID 0) -> Cost: 1000
        ge-0/0/3.0          DRother 0.0.0.8         0.0.0.0         0.0.0.0            0
        Type: LAN, Address: 100.0.0.254, Mask: 255.255.255.0, MTU: 1500, Cost: 100
        Adj count: 0, Passive
        Hello: 10, Dead: 40, ReXmit: 5, Not Stub
        Auth type: None
        Protection type: None
        Topology default (ID 0) -> Passive, Cost: 100
        lo0.0               DR      0.0.0.8         111.87.5.252    0.0.0.0            0
        Type: LAN, Address: 111.87.5.252, Mask: 255.255.255.255, MTU: 65535, Cost: 0
        DR addr: 111.87.5.252, Priority: 128
        Adj count: 0
        Hello: 10, Dead: 40, ReXmit: 5, Not Stub
        Auth type: None
        Protection type: None
        Topology default (ID 0) -> Cost: 0
        '''}

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
                    "interface-address": "111.87.5.93",
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
                        "ospf-topology-name": "default"
                    },
                    "ospf-stub-type": "Not Stub",
                    "retransmit-interval": "5"
                },
                {
                    "address-mask": "255.255.255.252",
                    "adj-count": "1",
                    "authentication-type": "None",
                    "bdr-id": "0.0.0.0",
                    "dead-interval": "40",
                    "dr-id": "0.0.0.0",
                    "hello-interval": "10",
                    "interface-address": "106.187.14.122",
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
                        "ospf-topology-name": "default"
                    },
                    "ospf-stub-type": "Not Stub",
                    "retransmit-interval": "5"
                },
                {
                    "address-mask": "255.255.255.252",
                    "adj-count": "1",
                    "authentication-type": "None",
                    "bdr-id": "0.0.0.0",
                    "dead-interval": "40",
                    "dr-id": "0.0.0.0",
                    "hello-interval": "10",
                    "interface-address": "27.86.198.25",
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
                        "ospf-topology-name": "default"
                    },
                    "ospf-stub-type": "Not Stub",
                    "retransmit-interval": "5"
                },
                {
                    "address-mask": "255.255.255.0",
                    "adj-count": "0",
                    "authentication-type": "None",
                    "bdr-id": "0.0.0.0",
                    "dead-interval": "40",
                    "dr-id": "0.0.0.0",
                    "hello-interval": "10",
                    "interface-address": "100.0.0.254",
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
                        "ospf-topology-passive": True
                    },
                    "ospf-stub-type": "Not Stub",
                    "passive": "Passive",
                    "retransmit-interval": "5"
                },
                {
                    "address-mask": "255.255.255.255",
                    "adj-count": "0",
                    "authentication-type": "None",
                    "bdr-id": "0.0.0.0",
                    "dead-interval": "40",
                    "dr-address": "111.87.5.252",
                    "dr-id": "111.87.5.252",
                    "hello-interval": "10",
                    "interface-address": "111.87.5.252",
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
                        "ospf-topology-name": "default"
                    },
                    "ospf-stub-type": "Not Stub",
                    "retransmit-interval": "5",
                    "router-priority": "128"
                }
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

if __name__ == '__main__':
    unittest.main()
