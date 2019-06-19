import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.asa.show_context import ShowContext, \
                                               ShowContextDetail

# ============================================
# unit test for 'show context'
# =============================================
class test_show_context(unittest.TestCase):
    '''
       unit test for show context
    '''
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
 
    golden_parsed_output = {
        'pod1': {
            'candidate_default': False,
            'class': 'default',
            'mode': 'Routed',
            'url': 'disk0:/pod-context/pod1',
            'interfaces': {
                'Vlan100': {
                    'interface': 'Vlan100'
                },
                'Vlan200': {
                    'interface': 'Vlan200'
                }
            }
        },
        'pod2': {
            'candidate_default': False,
            'class': '111',
            'mode': 'Routed',
            'url': 'disk0:/pod-context/pod2',
            'interfaces': {
                'Vlan300': {
                    'interface': 'Vlan300'
                },
                'Vlan400': {
                    'interface': 'Vlan400'
                }
            }
        },
        'admin': {
            'candidate_default': True,
            'class': 'default',
            'mode': 'Routed',
            'url': 'disk0:/pod-context/admin.cfg',
            'interfaces': {
                'Vlan1000': {
                    'interface': 'Vlan1000'
                },
                'Vlan1001': {
                    'interface': 'Vlan1001'
                },
                'Vlan1030': {
                    'interface': 'Vlan1030'
                },
                'Vlan1031': {
                    'interface': 'Vlan1031'
                },
                'Vlan1050': {
                    'interface': 'Vlan1050'
                },
                'Vlan1051': {
                    'interface': 'Vlan1051'
                },
                'Vlan1082': {
                    'interface': 'Vlan1082'
                },
                'Vlan1083': {
                    'interface': 'Vlan1083'
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''       
        pod1             default              Vlan100,Vlan200      Routed       disk0:/pod-context/pod1
        pod2             111                  Vlan300,Vlan400      Routed       disk0:/pod-context/pod2
        *admin            default              Vlan1000,Vlan1001,   Routed       disk0:/pod-context/admin.cfg
                                                Vlan1030,Vlan1031,
                                                Vlan1050,Vlan1051,
                                                Vlan1082,Vlan1083...
          '''}

    def test_empty_1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowContext(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj_context = ShowContext(device=self.device)
        parsed_output = obj_context.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

# ============================================
# unit test for 'show context detail'
# =============================================
class test_show_context_detail(unittest.TestCase):
    '''
       unit test for show context detail
    '''
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
 
    golden_parsed_output = {
        'pod1': {
            'context_created': True,
            'id': 2,
            'flags': '0x00000112',
            'class': 'default',
            'url': 'disk0:/pod-context/pod1',
            'interfaces': {
                'real_interfaces': {
                    'Vlan100': {
                        'real_interface': 'Vlan100'
                    },
                    'Vlan200': {
                        'real_interface': 'Vlan200'
                    },
                },
                'mapped_interfaces': {
                    'Vlan100': {
                        'mapped_interface': 'Vlan100'
                    },
                    'Vlan200': {
                        'mapped_interface': 'Vlan200'
                    }
                }
            }
        },
        'null': {
            'context_created': False,
            'id': 4,
            'flags': '0x00000114',
            'class': 'default'
        },
        'admin': {
            'context_created': True,
            'id': 1,
            'flags': '0x00000111',
            'class': 'default',
            'url': 'disk0:/pod-context/admin.cfg',
            'interfaces': {
                'real_interfaces': {
                    'Vlan1000': {
                        'real_interface': 'Vlan1000'
                    },
                    'Vlan1001': {
                        'real_interface': 'Vlan1001'
                    },
                    'Vlan1030': {
                        'real_interface': 'Vlan1030'
                    },
                    'Vlan1031': {
                        'real_interface': 'Vlan1031'
                    },
                    'Vlan1032': {
                        'real_interface': 'Vlan1032'
                    },
                    'Vlan993': {
                        'real_interface': 'Vlan993'
                    },
                    'Vlan994': {
                        'real_interface': 'Vlan994'
                    },
                    'Vlan995': {
                        'real_interface': 'Vlan995'
                    },
                    'Vlan996': {
                        'real_interface': 'Vlan996'
                    },
                    'Vlan997': {
                        'real_interface': 'Vlan997'
                    },
                    'Vlan998': {
                        'real_interface': 'Vlan998'
                    },
                    'Vlan999': {
                        'real_interface': 'Vlan999'
                    }
                }
            }
        },
        'pod3': {
            'context_created': True,
            'id': 3,
            'flags': '0x00000113',
            'class': 'default',
            'url': 'disk0:/pod-context/pod3',
            'interfaces': {
                'real_interfaces': {
                    'Vlan303': {
                        'real_interface': 'Vlan303'
                    },
                    'Vlan603': {
                        'real_interface': 'Vlan603'
                    },
                },
                'mapped_interfaces': {
                    'Vlan303': {
                        'mapped_interface': 'Vlan303'
                    },
                    'Vlan603': {
                        'mapped_interface': 'Vlan603'
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''       
        Context "pod1", has been created
          Config URL: disk0:/pod-context/pod1
          Real Interfaces: Vlan100, Vlan200
          Mapped Interfaces: Vlan100, Vlan200
          Class: default, Flags: 0x00000112, ID: 2

        Context "null", is a system resource
          Config URL: ... null ...
          Real Interfaces:
          Mapped Interfaces:
          Class: default, Flags: 0x00000114, ID: 4

        Context "admin", has been created
          Config URL: disk0:/pod-context/admin.cfg
          Real Interfaces: Vlan1000, Vlan1001, Vlan1030, Vlan1031, Vlan1032,
            Vlan993, Vlan994, Vlan995, Vlan996, Vlan997, Vlan998, Vlan999
            Class: default, Flags: 0x00000111, ID: 1

        Context "pod3", has been created
          Config URL: disk0:/pod-context/pod3
          Real Interfaces: Vlan303, Vlan603
          Mapped Interfaces: Vlan303, Vlan603
          Class: default, Flags: 0x00000113, ID: 3
          '''}

    def test_empty_1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowContextDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj_context_detail = ShowContextDetail(device=self.device)
        parsed_output = obj_context_detail.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()