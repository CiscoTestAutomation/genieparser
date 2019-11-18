
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# junos show_ospf
from genie.libs.parser.junos.show_ospf import (ShowOspfInterface,
                                               ShowOspfInterfaceBrief,
                                               ShowOspfInterfaceDetail)


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


if __name__ == '__main__':
    unittest.main()
