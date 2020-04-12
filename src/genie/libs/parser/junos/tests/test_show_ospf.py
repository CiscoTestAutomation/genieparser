
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
                                               ShowOspfDatabase,
                                               ShowOspfDatabaseSummary)


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

class TestShowOspfDatabase(unittest.TestCase):
    """ Unit tests for:
            * show ospf3 neighbor extensive
    """

    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show ospf database 

            OSPF database, Area 0.0.0.8
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len 
        Router   3.3.3.3          3.3.3.3          0x80004d2d    61  0x22 0xa127 2496
        Router   5.5.5.5          5.5.5.5          0x800019d7  1469  0x22 0xa1c   60
        Router   27.86.198.239    27.86.198.239    0x80000442   622  0x22 0x95bf  96
        Router   59.128.2.250     59.128.2.250     0x8000205a   736  0x22 0x26f6 144
        Router   59.128.2.251     59.128.2.251     0x80001dde   567  0x22 0x1022 108
        Router   106.162.196.241  106.162.196.241  0x800004a4    35  0x22 0x1055 144
        Router   106.187.14.240   106.187.14.240   0x80001bc1  2732  0x22 0x3a76 144
        Router   106.187.14.241   106.187.14.241   0x80001f67  1468  0x22 0x81fa 120
        Router  *111.87.5.252     111.87.5.252     0x80001b9e  1608  0x22 0x1e2  120
        Router   111.87.5.253     111.87.5.253     0x80001b04  1689  0x22 0xe230 108
        Router   202.239.165.119  202.239.165.119  0x800019de   928  0x22 0xc6a6  48
        Router   202.239.165.120  202.239.165.120  0x800019ea   500  0x22 0x2747  48
        Network  202.239.165.49   106.187.14.240   0x80000499   485  0x22 0xbb30  32
        Network  202.239.165.57   106.187.14.240   0x80000498  2292  0x22 0x5f86  32
        OpaqArea 1.0.0.0          5.5.5.5          0x800019ac  1469  0x20 0xc57f  28
        OpaqArea 1.0.0.0          27.86.198.239    0x8000028c   622  0x20 0x4e06  28
        OpaqArea 1.0.0.0          106.162.196.241  0x80000fdd   521  0x20 0xe9d4  28
        OpaqArea 1.0.0.1          59.128.2.250     0x800019e5  1888  0x22 0x902f  28
        OpaqArea 1.0.0.1          59.128.2.251     0x800019c7  1664  0x22 0xd00b  28
        OpaqArea 1.0.0.1          106.187.14.240   0x80001987   334  0x22 0xde66  28
        OpaqArea 1.0.0.1          106.187.14.241   0x80001e31  1907  0x22 0x8014  28
        OpaqArea*1.0.0.1          111.87.5.252     0x80001a15   231  0x22 0xd49a  28
        OpaqArea 1.0.0.1          111.87.5.253     0x80001a0f   901  0x22 0xe48e  28
        OpaqArea 1.0.0.3          59.128.2.250     0x800013d3  2119  0x22 0x47bd 136
        OpaqArea 1.0.0.3          59.128.2.251     0x800013b5  1445  0x22 0x5fc3 136
        OpaqArea 1.0.0.3          106.187.14.240   0x8000063d  1690  0x22 0x75dc 136
        OpaqArea 1.0.0.3          106.187.14.241   0x80000c51   951  0x22 0x1721 136
        OpaqArea*1.0.0.3          111.87.5.252     0x80000321  2678  0x22 0x97cc 136
        OpaqArea 1.0.0.3          111.87.5.253     0x80000322  2500  0x22 0x71f1 136
        OpaqArea 1.0.0.4          59.128.2.250     0x8000029e  1427  0x22 0x1e4  136
        OpaqArea 1.0.0.4          59.128.2.251     0x80000299  1226  0x22 0x29c0 136
        OpaqArea 1.0.0.4          106.187.14.240   0x800003f8  1238  0x22 0xb606 136
        OpaqArea 1.0.0.4          106.187.14.241   0x800013fe  2127  0x22 0x694d 136
        OpaqArea*1.0.0.4          111.87.5.252     0x800013e8  2411  0x22 0xb804 136
        OpaqArea 1.0.0.4          111.87.5.253     0x80000f9b  2772  0x22 0x4ecf 136
        OpaqArea 1.0.0.5          59.128.2.250     0x800001b5   289  0x22 0x5e9d 136
        OpaqArea 1.0.0.5          59.128.2.251     0x800001b5   276  0x22 0xd817 136
        OpaqArea 1.0.0.5          106.187.14.240   0x80000289    33  0x22 0xdd1f 136
        OpaqArea 1.0.0.5          106.187.14.241   0x80000298  1687  0x22 0x21a9 136
        OpaqArea*1.0.0.5          111.87.5.252     0x800001bb  1312  0x22 0x79b5 136
        OpaqArea 1.0.0.5          111.87.5.253     0x800001bb  1147  0x22 0x5ec3 136
        OpaqArea 1.0.0.6          5.5.5.5          0x800019be  1469  0x20 0x629a 168
        OpaqArea 1.0.0.10         27.86.198.239    0x8000025d   622  0x20 0xcffa 132
        OpaqArea 1.0.0.10         106.162.196.241  0x8000025d   521  0x20 0x771b 132
        OpaqArea 1.0.0.11         27.86.198.239    0x8000025d   622  0x20 0xecd3 132
        OpaqArea 1.0.0.11         106.162.196.241  0x8000025d   521  0x20 0xa14f 132
        OpaqArea 1.0.0.12         27.86.198.239    0x80000163   622  0x20 0x87f8  80
        OpaqArea 1.0.8.69         106.162.196.241  0x8000003b    35  0x20 0x8150  80
        OpaqArea 1.0.8.70         106.162.196.241  0x80000151   521  0x20 0x8a2d  80
        OpaqArea 4.0.0.0          5.5.5.5          0x800019ac  1469  0x20 0x810a  52
        OpaqArea 4.0.0.0          27.86.198.239    0x8000028c   622  0x20 0x8e0f  76
        OpaqArea 4.0.0.0          59.128.2.250     0x80001a15  2810  0x22 0xbd3d  44
        OpaqArea 4.0.0.0          59.128.2.251     0x800019e4  2103  0x22 0x1b10  44
        OpaqArea 4.0.0.0          106.162.196.241  0x800003a6   521  0x20 0x2db9  76
        OpaqArea 4.0.0.0          106.187.14.240   0x8000199d  2142  0x22 0x15f1  44
        OpaqArea 4.0.0.0          106.187.14.241   0x80001e44    48  0x22 0xb2a7  44
        OpaqArea*4.0.0.0          111.87.5.252     0x80001a2a   771  0x22 0xe5ef  44
        OpaqArea 4.0.0.0          111.87.5.253     0x80001a21   410  0x22 0xf1eb  44
        OpaqArea 7.0.0.0          27.86.198.239    0x8000028c   622  0x20 0xcdab  44
        OpaqArea 7.0.0.0          106.162.196.241  0x800003a4   521  0x20 0x69c9  44
        OpaqArea 7.0.0.1          5.5.5.5          0x800019ac  1469  0x20 0x6c5a  44
        OpaqArea 7.0.0.1          59.128.2.250     0x80001fa9   736  0x22 0x7fa7  44
        OpaqArea 7.0.0.1          59.128.2.251     0x80001cfb   567  0x22 0x6ce   44
        OpaqArea 7.0.0.1          106.187.14.240   0x80001bc1  2732  0x22 0x99aa  44
        OpaqArea 7.0.0.1          106.187.14.241   0x80001f67  1468  0x22 0x6433  44
        OpaqArea*7.0.0.1          111.87.5.252     0x80001b9e  1608  0x22 0x8c7f  44
        OpaqArea 7.0.0.1          111.87.5.253     0x80001b04  1689  0x22 0xe3bf  44
        OpaqArea 8.0.0.1          59.128.2.250     0x800004f9    76  0x22 0x39a3  60
        OpaqArea 8.0.0.1          106.187.14.241   0x80000311   725  0x22 0x7002  60
        OpaqArea 8.0.0.1          111.87.5.253     0x8000030a  2230  0x22 0x6915  60
        OpaqArea 8.0.0.2          106.187.14.241   0x80000305   499  0x22 0x7271  60
        OpaqArea 8.0.0.3          106.187.14.241   0x8000029a   274  0x22 0x7248  60
        OpaqArea 8.0.0.3          111.87.5.253     0x800002db   656  0x22 0x34eb  60
        OpaqArea 8.0.0.4          111.87.5.253     0x800001bb  1960  0x22 0x31be  60
        OpaqArea 8.0.0.6          5.5.5.5          0x800019bf  1469  0x20 0x4de2  56
        OpaqArea 8.0.0.7          59.128.2.250     0x8000046b  2580  0x22 0xb9a6  48
        OpaqArea 8.0.0.7          59.128.2.251     0x800004de  1006  0x22 0x6a96  60
        OpaqArea 8.0.0.17         27.86.198.239    0x8000025d   622  0x20 0xb34a 104
        OpaqArea 8.0.0.17         106.162.196.241  0x8000025d   521  0x20 0x3e3c 104
        OpaqArea 8.0.0.18         27.86.198.239    0x8000025d   622  0x20 0xb938 104
        OpaqArea 8.0.0.18         106.162.196.241  0x8000025d   521  0x20 0x6fdb 104
        OpaqArea 8.0.0.31         59.128.2.251     0x8000029a  2542  0x22 0xe909  60
        OpaqArea 8.0.0.32         59.128.2.251     0x800001b5   787  0x22 0xe396  60
        OpaqArea 8.0.0.37         59.128.2.250     0x8000029b  1658  0x22 0xffb8  60
        OpaqArea 8.0.0.38         59.128.2.250     0x800001b5   966  0x22 0x71b3  60
        OpaqArea*8.0.0.52         111.87.5.252     0x80000308   501  0x22 0x7efa  60
        OpaqArea*8.0.0.54         111.87.5.252     0x800002dc  1042  0x22 0x1839  60
        OpaqArea*8.0.0.55         111.87.5.252     0x800001bb  1876  0x22 0x92eb  60
        OpaqArea 8.0.0.57         106.187.14.240   0x80000303  1087  0x22 0x7544  60
        OpaqArea 8.0.0.59         106.187.14.240   0x800002f4  1389  0x22 0x6d12  60
        OpaqArea 8.0.0.60         106.187.14.240   0x8000028b   937  0x22 0x4f1a  60
        OpaqArea 8.0.8.74         106.162.196.241  0x80000030    35  0x20 0xdcd1  92
        OpaqArea 8.0.8.75         106.162.196.241  0x80000151   521  0x20 0xd4b0  92
            OSPF AS SCOPE link state database
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len 
        Extern   0.0.0.0          59.128.2.251     0x800019e3  2323  0x22 0x6715  36
        Extern   0.0.0.0          106.187.14.240   0x8000039e  1991  0x22 0x9fcc  36
        Extern   1.0.0.0          202.239.165.119  0x800019b0   928  0x20 0x3bc3  36
        Extern   1.0.0.0          202.239.165.120  0x800019b1   500  0x20 0x33c9  36
        Extern   27.90.132.237    106.187.14.240   0x8000039e  1841  0x22 0xf161  36
        Extern   59.128.2.250     106.187.14.240   0x80000288  2443  0x22 0x473e  36
        Extern   59.128.2.250     106.187.14.241   0x80000298  2346  0x22 0x2153  36
        Extern   59.128.2.251     106.187.14.240   0x80000289   184  0x22 0x3b48  36
        Extern   59.128.2.251     106.187.14.241   0x80000298  1176  0x22 0x175c  36
        Extern   106.187.14.240   59.128.2.250     0x8000029a  1197  0x22 0xf88e  36
        Extern   106.187.14.240   59.128.2.251     0x800019e4  1884  0x22 0x190c  36
        Extern  *106.187.14.240   111.87.5.252     0x80001a3a  2143  0x22 0xc3fb  36
        Extern   106.187.14.241   59.128.2.250     0x80001a14  2349  0x22 0xb341  36
        Extern   106.187.14.241   59.128.2.251     0x80000299    50  0x22 0xea9b  36
        Extern   106.187.14.241   111.87.5.253     0x80000fae   164  0x22 0xeb68  36
        Extern   111.87.5.252     106.187.14.240   0x800019b0  1539  0x22 0xc372  36
        Extern   111.87.5.253     106.187.14.241   0x8000140f  2566  0x22 0x6d4   36
        Extern   202.239.164.0    106.187.14.240   0x800002da   786  0x22 0xfb51  36
        Extern   202.239.164.252  106.187.14.240   0x800002d9   636  0x22 0x19b8  36
    '''}

    golden_parsed_output = {
            
    "ospf-database-information": {
        "ospf-area-header": {
            "ospf-area": "0.0.0.8"
        },
        "ospf-database": [
            {
                "advertising-router": "3.3.3.3",
                "age": "61",
                "checksum": "0xa127",
                "lsa-id": "3.3.3.3",
                "lsa-length": "2496",
                "lsa-type": "Router",
                "options": "0x22",
                "sequence-number": "0x80004d2d"
            },
            {
                "advertising-router": "5.5.5.5",
                "age": "1469",
                "checksum": "0xa1c",
                "lsa-id": "5.5.5.5",
                "lsa-length": "60",
                "lsa-type": "Router",
                "options": "0x22",
                "sequence-number": "0x800019d7"
            },
            {
                "advertising-router": "27.86.198.239",
                "age": "622",
                "checksum": "0x95bf",
                "lsa-id": "27.86.198.239",
                "lsa-length": "96",
                "lsa-type": "Router",
                "options": "0x22",
                "sequence-number": "0x80000442"
            },
            {
                "advertising-router": "59.128.2.250",
                "age": "736",
                "checksum": "0x26f6",
                "lsa-id": "59.128.2.250",
                "lsa-length": "144",
                "lsa-type": "Router",
                "options": "0x22",
                "sequence-number": "0x8000205a"
            },
            {
                "advertising-router": "59.128.2.251",
                "age": "567",
                "checksum": "0x1022",
                "lsa-id": "59.128.2.251",
                "lsa-length": "108",
                "lsa-type": "Router",
                "options": "0x22",
                "sequence-number": "0x80001dde"
            },
            {
                "advertising-router": "106.162.196.241",
                "age": "35",
                "checksum": "0x1055",
                "lsa-id": "106.162.196.241",
                "lsa-length": "144",
                "lsa-type": "Router",
                "options": "0x22",
                "sequence-number": "0x800004a4"
            },
            {
                "advertising-router": "106.187.14.240",
                "age": "2732",
                "checksum": "0x3a76",
                "lsa-id": "106.187.14.240",
                "lsa-length": "144",
                "lsa-type": "Router",
                "options": "0x22",
                "sequence-number": "0x80001bc1"
            },
            {
                "advertising-router": "106.187.14.241",
                "age": "1468",
                "checksum": "0x81fa",
                "lsa-id": "106.187.14.241",
                "lsa-length": "120",
                "lsa-type": "Router",
                "options": "0x22",
                "sequence-number": "0x80001f67"
            },
            {
                "advertising-router": "111.87.5.252",
                "age": "1608",
                "checksum": "0x1e2",
                "lsa-id": "111.87.5.252",
                "lsa-length": "120",
                "lsa-type": "Router",
                "options": "0x22",
                "our-entry": True,
                "sequence-number": "0x80001b9e"
            },
            {
                "advertising-router": "111.87.5.253",
                "age": "1689",
                "checksum": "0xe230",
                "lsa-id": "111.87.5.253",
                "lsa-length": "108",
                "lsa-type": "Router",
                "options": "0x22",
                "sequence-number": "0x80001b04"
            },
            {
                "advertising-router": "202.239.165.119",
                "age": "928",
                "checksum": "0xc6a6",
                "lsa-id": "202.239.165.119",
                "lsa-length": "48",
                "lsa-type": "Router",
                "options": "0x22",
                "sequence-number": "0x800019de"
            },
            {
                "advertising-router": "202.239.165.120",
                "age": "500",
                "checksum": "0x2747",
                "lsa-id": "202.239.165.120",
                "lsa-length": "48",
                "lsa-type": "Router",
                "options": "0x22",
                "sequence-number": "0x800019ea"
            },
            {
                "advertising-router": "106.187.14.240",
                "age": "485",
                "checksum": "0xbb30",
                "lsa-id": "202.239.165.49",
                "lsa-length": "32",
                "lsa-type": "Network",
                "options": "0x22",
                "sequence-number": "0x80000499"
            },
            {
                "advertising-router": "106.187.14.240",
                "age": "2292",
                "checksum": "0x5f86",
                "lsa-id": "202.239.165.57",
                "lsa-length": "32",
                "lsa-type": "Network",
                "options": "0x22",
                "sequence-number": "0x80000498"
            },
            {
                "advertising-router": "5.5.5.5",
                "age": "1469",
                "checksum": "0xc57f",
                "lsa-id": "1.0.0.0",
                "lsa-length": "28",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x800019ac"
            },
            {
                "advertising-router": "27.86.198.239",
                "age": "622",
                "checksum": "0x4e06",
                "lsa-id": "1.0.0.0",
                "lsa-length": "28",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x8000028c"
            },
            {
                "advertising-router": "106.162.196.241",
                "age": "521",
                "checksum": "0xe9d4",
                "lsa-id": "1.0.0.0",
                "lsa-length": "28",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x80000fdd"
            },
            {
                "advertising-router": "59.128.2.250",
                "age": "1888",
                "checksum": "0x902f",
                "lsa-id": "1.0.0.1",
                "lsa-length": "28",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x800019e5"
            },
            {
                "advertising-router": "59.128.2.251",
                "age": "1664",
                "checksum": "0xd00b",
                "lsa-id": "1.0.0.1",
                "lsa-length": "28",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x800019c7"
            },
            {
                "advertising-router": "106.187.14.240",
                "age": "334",
                "checksum": "0xde66",
                "lsa-id": "1.0.0.1",
                "lsa-length": "28",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80001987"
            },
            {
                "advertising-router": "106.187.14.241",
                "age": "1907",
                "checksum": "0x8014",
                "lsa-id": "1.0.0.1",
                "lsa-length": "28",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80001e31"
            },
            {
                "advertising-router": "111.87.5.252",
                "age": "231",
                "checksum": "0xd49a",
                "lsa-id": "1.0.0.1",
                "lsa-length": "28",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80001a15"
            },
            {
                "advertising-router": "111.87.5.253",
                "age": "901",
                "checksum": "0xe48e",
                "lsa-id": "1.0.0.1",
                "lsa-length": "28",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80001a0f"
            },
            {
                "advertising-router": "59.128.2.250",
                "age": "2119",
                "checksum": "0x47bd",
                "lsa-id": "1.0.0.3",
                "lsa-length": "136",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x800013d3"
            },
            {
                "advertising-router": "59.128.2.251",
                "age": "1445",
                "checksum": "0x5fc3",
                "lsa-id": "1.0.0.3",
                "lsa-length": "136",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x800013b5"
            },
            {
                "advertising-router": "106.187.14.240",
                "age": "1690",
                "checksum": "0x75dc",
                "lsa-id": "1.0.0.3",
                "lsa-length": "136",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x8000063d"
            },
            {
                "advertising-router": "106.187.14.241",
                "age": "951",
                "checksum": "0x1721",
                "lsa-id": "1.0.0.3",
                "lsa-length": "136",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80000c51"
            },
            {
                "advertising-router": "111.87.5.252",
                "age": "2678",
                "checksum": "0x97cc",
                "lsa-id": "1.0.0.3",
                "lsa-length": "136",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80000321"
            },
            {
                "advertising-router": "111.87.5.253",
                "age": "2500",
                "checksum": "0x71f1",
                "lsa-id": "1.0.0.3",
                "lsa-length": "136",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80000322"
            },
            {
                "advertising-router": "59.128.2.250",
                "age": "1427",
                "checksum": "0x1e4",
                "lsa-id": "1.0.0.4",
                "lsa-length": "136",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x8000029e"
            },
            {
                "advertising-router": "59.128.2.251",
                "age": "1226",
                "checksum": "0x29c0",
                "lsa-id": "1.0.0.4",
                "lsa-length": "136",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80000299"
            },
            {
                "advertising-router": "106.187.14.240",
                "age": "1238",
                "checksum": "0xb606",
                "lsa-id": "1.0.0.4",
                "lsa-length": "136",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x800003f8"
            },
            {
                "advertising-router": "106.187.14.241",
                "age": "2127",
                "checksum": "0x694d",
                "lsa-id": "1.0.0.4",
                "lsa-length": "136",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x800013fe"
            },
            {
                "advertising-router": "111.87.5.252",
                "age": "2411",
                "checksum": "0xb804",
                "lsa-id": "1.0.0.4",
                "lsa-length": "136",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x800013e8"
            },
            {
                "advertising-router": "111.87.5.253",
                "age": "2772",
                "checksum": "0x4ecf",
                "lsa-id": "1.0.0.4",
                "lsa-length": "136",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80000f9b"
            },
            {
                "advertising-router": "59.128.2.250",
                "age": "289",
                "checksum": "0x5e9d",
                "lsa-id": "1.0.0.5",
                "lsa-length": "136",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x800001b5"
            },
            {
                "advertising-router": "59.128.2.251",
                "age": "276",
                "checksum": "0xd817",
                "lsa-id": "1.0.0.5",
                "lsa-length": "136",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x800001b5"
            },
            {
                "advertising-router": "106.187.14.240",
                "age": "33",
                "checksum": "0xdd1f",
                "lsa-id": "1.0.0.5",
                "lsa-length": "136",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80000289"
            },
            {
                "advertising-router": "106.187.14.241",
                "age": "1687",
                "checksum": "0x21a9",
                "lsa-id": "1.0.0.5",
                "lsa-length": "136",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80000298"
            },
            {
                "advertising-router": "111.87.5.252",
                "age": "1312",
                "checksum": "0x79b5",
                "lsa-id": "1.0.0.5",
                "lsa-length": "136",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x800001bb"
            },
            {
                "advertising-router": "111.87.5.253",
                "age": "1147",
                "checksum": "0x5ec3",
                "lsa-id": "1.0.0.5",
                "lsa-length": "136",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x800001bb"
            },
            {
                "advertising-router": "5.5.5.5",
                "age": "1469",
                "checksum": "0x629a",
                "lsa-id": "1.0.0.6",
                "lsa-length": "168",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x800019be"
            },
            {
                "advertising-router": "27.86.198.239",
                "age": "622",
                "checksum": "0xcffa",
                "lsa-id": "1.0.0.10",
                "lsa-length": "132",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x8000025d"
            },
            {
                "advertising-router": "106.162.196.241",
                "age": "521",
                "checksum": "0x771b",
                "lsa-id": "1.0.0.10",
                "lsa-length": "132",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x8000025d"
            },
            {
                "advertising-router": "27.86.198.239",
                "age": "622",
                "checksum": "0xecd3",
                "lsa-id": "1.0.0.11",
                "lsa-length": "132",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x8000025d"
            },
            {
                "advertising-router": "106.162.196.241",
                "age": "521",
                "checksum": "0xa14f",
                "lsa-id": "1.0.0.11",
                "lsa-length": "132",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x8000025d"
            },
            {
                "advertising-router": "27.86.198.239",
                "age": "622",
                "checksum": "0x87f8",
                "lsa-id": "1.0.0.12",
                "lsa-length": "80",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x80000163"
            },
            {
                "advertising-router": "106.162.196.241",
                "age": "35",
                "checksum": "0x8150",
                "lsa-id": "1.0.8.69",
                "lsa-length": "80",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x8000003b"
            },
            {
                "advertising-router": "106.162.196.241",
                "age": "521",
                "checksum": "0x8a2d",
                "lsa-id": "1.0.8.70",
                "lsa-length": "80",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x80000151"
            },
            {
                "advertising-router": "5.5.5.5",
                "age": "1469",
                "checksum": "0x810a",
                "lsa-id": "4.0.0.0",
                "lsa-length": "52",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x800019ac"
            },
            {
                "advertising-router": "27.86.198.239",
                "age": "622",
                "checksum": "0x8e0f",
                "lsa-id": "4.0.0.0",
                "lsa-length": "76",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x8000028c"
            },
            {
                "advertising-router": "59.128.2.250",
                "age": "2810",
                "checksum": "0xbd3d",
                "lsa-id": "4.0.0.0",
                "lsa-length": "44",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80001a15"
            },
            {
                "advertising-router": "59.128.2.251",
                "age": "2103",
                "checksum": "0x1b10",
                "lsa-id": "4.0.0.0",
                "lsa-length": "44",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x800019e4"
            },
            {
                "advertising-router": "106.162.196.241",
                "age": "521",
                "checksum": "0x2db9",
                "lsa-id": "4.0.0.0",
                "lsa-length": "76",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x800003a6"
            },
            {
                "advertising-router": "106.187.14.240",
                "age": "2142",
                "checksum": "0x15f1",
                "lsa-id": "4.0.0.0",
                "lsa-length": "44",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x8000199d"
            },
            {
                "advertising-router": "106.187.14.241",
                "age": "48",
                "checksum": "0xb2a7",
                "lsa-id": "4.0.0.0",
                "lsa-length": "44",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80001e44"
            },
            {
                "advertising-router": "111.87.5.252",
                "age": "771",
                "checksum": "0xe5ef",
                "lsa-id": "4.0.0.0",
                "lsa-length": "44",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80001a2a"
            },
            {
                "advertising-router": "111.87.5.253",
                "age": "410",
                "checksum": "0xf1eb",
                "lsa-id": "4.0.0.0",
                "lsa-length": "44",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80001a21"
            },
            {
                "advertising-router": "27.86.198.239",
                "age": "622",
                "checksum": "0xcdab",
                "lsa-id": "7.0.0.0",
                "lsa-length": "44",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x8000028c"
            },
            {
                "advertising-router": "106.162.196.241",
                "age": "521",
                "checksum": "0x69c9",
                "lsa-id": "7.0.0.0",
                "lsa-length": "44",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x800003a4"
            },
            {
                "advertising-router": "5.5.5.5",
                "age": "1469",
                "checksum": "0x6c5a",
                "lsa-id": "7.0.0.1",
                "lsa-length": "44",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x800019ac"
            },
            {
                "advertising-router": "59.128.2.250",
                "age": "736",
                "checksum": "0x7fa7",
                "lsa-id": "7.0.0.1",
                "lsa-length": "44",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80001fa9"
            },
            {
                "advertising-router": "59.128.2.251",
                "age": "567",
                "checksum": "0x6ce",
                "lsa-id": "7.0.0.1",
                "lsa-length": "44",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80001cfb"
            },
            {
                "advertising-router": "106.187.14.240",
                "age": "2732",
                "checksum": "0x99aa",
                "lsa-id": "7.0.0.1",
                "lsa-length": "44",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80001bc1"
            },
            {
                "advertising-router": "106.187.14.241",
                "age": "1468",
                "checksum": "0x6433",
                "lsa-id": "7.0.0.1",
                "lsa-length": "44",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80001f67"
            },
            {
                "advertising-router": "111.87.5.252",
                "age": "1608",
                "checksum": "0x8c7f",
                "lsa-id": "7.0.0.1",
                "lsa-length": "44",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80001b9e"
            },
            {
                "advertising-router": "111.87.5.253",
                "age": "1689",
                "checksum": "0xe3bf",
                "lsa-id": "7.0.0.1",
                "lsa-length": "44",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80001b04"
            },
            {
                "advertising-router": "59.128.2.250",
                "age": "76",
                "checksum": "0x39a3",
                "lsa-id": "8.0.0.1",
                "lsa-length": "60",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x800004f9"
            },
            {
                "advertising-router": "106.187.14.241",
                "age": "725",
                "checksum": "0x7002",
                "lsa-id": "8.0.0.1",
                "lsa-length": "60",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80000311"
            },
            {
                "advertising-router": "111.87.5.253",
                "age": "2230",
                "checksum": "0x6915",
                "lsa-id": "8.0.0.1",
                "lsa-length": "60",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x8000030a"
            },
            {
                "advertising-router": "106.187.14.241",
                "age": "499",
                "checksum": "0x7271",
                "lsa-id": "8.0.0.2",
                "lsa-length": "60",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80000305"
            },
            {
                "advertising-router": "106.187.14.241",
                "age": "274",
                "checksum": "0x7248",
                "lsa-id": "8.0.0.3",
                "lsa-length": "60",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x8000029a"
            },
            {
                "advertising-router": "111.87.5.253",
                "age": "656",
                "checksum": "0x34eb",
                "lsa-id": "8.0.0.3",
                "lsa-length": "60",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x800002db"
            },
            {
                "advertising-router": "111.87.5.253",
                "age": "1960",
                "checksum": "0x31be",
                "lsa-id": "8.0.0.4",
                "lsa-length": "60",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x800001bb"
            },
            {
                "advertising-router": "5.5.5.5",
                "age": "1469",
                "checksum": "0x4de2",
                "lsa-id": "8.0.0.6",
                "lsa-length": "56",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x800019bf"
            },
            {
                "advertising-router": "59.128.2.250",
                "age": "2580",
                "checksum": "0xb9a6",
                "lsa-id": "8.0.0.7",
                "lsa-length": "48",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x8000046b"
            },
            {
                "advertising-router": "59.128.2.251",
                "age": "1006",
                "checksum": "0x6a96",
                "lsa-id": "8.0.0.7",
                "lsa-length": "60",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x800004de"
            },
            {
                "advertising-router": "27.86.198.239",
                "age": "622",
                "checksum": "0xb34a",
                "lsa-id": "8.0.0.17",
                "lsa-length": "104",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x8000025d"
            },
            {
                "advertising-router": "106.162.196.241",
                "age": "521",
                "checksum": "0x3e3c",
                "lsa-id": "8.0.0.17",
                "lsa-length": "104",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x8000025d"
            },
            {
                "advertising-router": "27.86.198.239",
                "age": "622",
                "checksum": "0xb938",
                "lsa-id": "8.0.0.18",
                "lsa-length": "104",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x8000025d"
            },
            {
                "advertising-router": "106.162.196.241",
                "age": "521",
                "checksum": "0x6fdb",
                "lsa-id": "8.0.0.18",
                "lsa-length": "104",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x8000025d"
            },
            {
                "advertising-router": "59.128.2.251",
                "age": "2542",
                "checksum": "0xe909",
                "lsa-id": "8.0.0.31",
                "lsa-length": "60",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x8000029a"
            },
            {
                "advertising-router": "59.128.2.251",
                "age": "787",
                "checksum": "0xe396",
                "lsa-id": "8.0.0.32",
                "lsa-length": "60",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x800001b5"
            },
            {
                "advertising-router": "59.128.2.250",
                "age": "1658",
                "checksum": "0xffb8",
                "lsa-id": "8.0.0.37",
                "lsa-length": "60",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x8000029b"
            },
            {
                "advertising-router": "59.128.2.250",
                "age": "966",
                "checksum": "0x71b3",
                "lsa-id": "8.0.0.38",
                "lsa-length": "60",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x800001b5"
            },
            {
                "advertising-router": "111.87.5.252",
                "age": "501",
                "checksum": "0x7efa",
                "lsa-id": "8.0.0.52",
                "lsa-length": "60",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80000308"
            },
            {
                "advertising-router": "111.87.5.252",
                "age": "1042",
                "checksum": "0x1839",
                "lsa-id": "8.0.0.54",
                "lsa-length": "60",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x800002dc"
            },
            {
                "advertising-router": "111.87.5.252",
                "age": "1876",
                "checksum": "0x92eb",
                "lsa-id": "8.0.0.55",
                "lsa-length": "60",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x800001bb"
            },
            {
                "advertising-router": "106.187.14.240",
                "age": "1087",
                "checksum": "0x7544",
                "lsa-id": "8.0.0.57",
                "lsa-length": "60",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x80000303"
            },
            {
                "advertising-router": "106.187.14.240",
                "age": "1389",
                "checksum": "0x6d12",
                "lsa-id": "8.0.0.59",
                "lsa-length": "60",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x800002f4"
            },
            {
                "advertising-router": "106.187.14.240",
                "age": "937",
                "checksum": "0x4f1a",
                "lsa-id": "8.0.0.60",
                "lsa-length": "60",
                "lsa-type": "OpaqArea",
                "options": "0x22",
                "sequence-number": "0x8000028b"
            },
            {
                "advertising-router": "106.162.196.241",
                "age": "35",
                "checksum": "0xdcd1",
                "lsa-id": "8.0.8.74",
                "lsa-length": "92",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x80000030"
            },
            {
                "advertising-router": "106.162.196.241",
                "age": "521",
                "checksum": "0xd4b0",
                "lsa-id": "8.0.8.75",
                "lsa-length": "92",
                "lsa-type": "OpaqArea",
                "options": "0x20",
                "sequence-number": "0x80000151"
            },
            {
                "advertising-router": "59.128.2.251",
                "age": "2323",
                "checksum": "0x6715",
                "lsa-id": "0.0.0.0",
                "lsa-length": "36",
                "lsa-type": "Extern",
                "options": "0x22",
                "sequence-number": "0x800019e3"
            },
            {
                "advertising-router": "106.187.14.240",
                "age": "1991",
                "checksum": "0x9fcc",
                "lsa-id": "0.0.0.0",
                "lsa-length": "36",
                "lsa-type": "Extern",
                "options": "0x22",
                "sequence-number": "0x8000039e"
            },
            {
                "advertising-router": "202.239.165.119",
                "age": "928",
                "checksum": "0x3bc3",
                "lsa-id": "1.0.0.0",
                "lsa-length": "36",
                "lsa-type": "Extern",
                "options": "0x20",
                "sequence-number": "0x800019b0"
            },
            {
                "advertising-router": "202.239.165.120",
                "age": "500",
                "checksum": "0x33c9",
                "lsa-id": "1.0.0.0",
                "lsa-length": "36",
                "lsa-type": "Extern",
                "options": "0x20",
                "sequence-number": "0x800019b1"
            },
            {
                "advertising-router": "106.187.14.240",
                "age": "1841",
                "checksum": "0xf161",
                "lsa-id": "27.90.132.237",
                "lsa-length": "36",
                "lsa-type": "Extern",
                "options": "0x22",
                "sequence-number": "0x8000039e"
            },
            {
                "advertising-router": "106.187.14.240",
                "age": "2443",
                "checksum": "0x473e",
                "lsa-id": "59.128.2.250",
                "lsa-length": "36",
                "lsa-type": "Extern",
                "options": "0x22",
                "sequence-number": "0x80000288"
            },
            {
                "advertising-router": "106.187.14.241",
                "age": "2346",
                "checksum": "0x2153",
                "lsa-id": "59.128.2.250",
                "lsa-length": "36",
                "lsa-type": "Extern",
                "options": "0x22",
                "sequence-number": "0x80000298"
            },
            {
                "advertising-router": "106.187.14.240",
                "age": "184",
                "checksum": "0x3b48",
                "lsa-id": "59.128.2.251",
                "lsa-length": "36",
                "lsa-type": "Extern",
                "options": "0x22",
                "sequence-number": "0x80000289"
            },
            {
                "advertising-router": "106.187.14.241",
                "age": "1176",
                "checksum": "0x175c",
                "lsa-id": "59.128.2.251",
                "lsa-length": "36",
                "lsa-type": "Extern",
                "options": "0x22",
                "sequence-number": "0x80000298"
            },
            {
                "advertising-router": "59.128.2.250",
                "age": "1197",
                "checksum": "0xf88e",
                "lsa-id": "106.187.14.240",
                "lsa-length": "36",
                "lsa-type": "Extern",
                "options": "0x22",
                "sequence-number": "0x8000029a"
            },
            {
                "advertising-router": "59.128.2.251",
                "age": "1884",
                "checksum": "0x190c",
                "lsa-id": "106.187.14.240",
                "lsa-length": "36",
                "lsa-type": "Extern",
                "options": "0x22",
                "sequence-number": "0x800019e4"
            },
            {
                "advertising-router": "111.87.5.252",
                "age": "2143",
                "checksum": "0xc3fb",
                "lsa-id": "106.187.14.240",
                "lsa-length": "36",
                "lsa-type": "Extern",
                "options": "0x22",
                "our-entry": True,
                "sequence-number": "0x80001a3a"
            },
            {
                "advertising-router": "59.128.2.250",
                "age": "2349",
                "checksum": "0xb341",
                "lsa-id": "106.187.14.241",
                "lsa-length": "36",
                "lsa-type": "Extern",
                "options": "0x22",
                "sequence-number": "0x80001a14"
            },
            {
                "advertising-router": "59.128.2.251",
                "age": "50",
                "checksum": "0xea9b",
                "lsa-id": "106.187.14.241",
                "lsa-length": "36",
                "lsa-type": "Extern",
                "options": "0x22",
                "sequence-number": "0x80000299"
            },
            {
                "advertising-router": "111.87.5.253",
                "age": "164",
                "checksum": "0xeb68",
                "lsa-id": "106.187.14.241",
                "lsa-length": "36",
                "lsa-type": "Extern",
                "options": "0x22",
                "sequence-number": "0x80000fae"
            },
            {
                "advertising-router": "106.187.14.240",
                "age": "1539",
                "checksum": "0xc372",
                "lsa-id": "111.87.5.252",
                "lsa-length": "36",
                "lsa-type": "Extern",
                "options": "0x22",
                "sequence-number": "0x800019b0"
            },
            {
                "advertising-router": "106.187.14.241",
                "age": "2566",
                "checksum": "0x6d4",
                "lsa-id": "111.87.5.253",
                "lsa-length": "36",
                "lsa-type": "Extern",
                "options": "0x22",
                "sequence-number": "0x8000140f"
            },
            {
                "advertising-router": "106.187.14.240",
                "age": "786",
                "checksum": "0xfb51",
                "lsa-id": "202.239.164.0",
                "lsa-length": "36",
                "lsa-type": "Extern",
                "options": "0x22",
                "sequence-number": "0x800002da"
            },
            {
                "advertising-router": "106.187.14.240",
                "age": "636",
                "checksum": "0x19b8",
                "lsa-id": "202.239.164.252",
                "lsa-length": "36",
                "lsa-type": "Extern",
                "options": "0x22",
                "sequence-number": "0x800002d9"
            }
        ]
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

    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
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
    '''}

    golden_parsed_output = {
        "ospf-database-information": {
        "ospf-database-summary": [
            {
                "ospf-area": "0.0.0.8",
                "ospf-lsa-count": [
                    "12",
                    "2",
                    "79"
                ],
                "ospf-lsa-type": [
                    "Router",
                    "Network",
                    "OpaqArea"
                ]
            },
            {
                "@external-heading": "Externals",
                "ospf-lsa-count": "19",
                "ospf-lsa-type": "Extern"
            },
            {
                "ospf-area": [
                    "0.0.0.8",
                    "0.0.0.8",
                    "0.0.0.8",
                    "0.0.0.8",
                    "0.0.0.8"
                ],
                "ospf-intf": [
                    "ge-0/0/0.0",
                    "ge-0/0/1.0",
                    "ge-0/0/2.0",
                    "ge-0/0/3.0",
                    "lo0.0"
                ]
            }
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

if __name__ == '__main__':
    unittest.main()
