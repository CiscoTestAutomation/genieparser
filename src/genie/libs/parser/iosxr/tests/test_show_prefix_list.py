# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Parser
from genie.libs.parser.iosxr.show_prefix_list import ShowRplPrefixSet

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# ===================================
# Unit test for 'show rpl prefix-set'
# ===================================

class test_show_rpl_prefix_set(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'prefix_set_name': {
            'test': {
                'prefix_set_name': 'test',
                'protocol': 'ipv4',
                'prefixes': {
                    '10.205.0.0/8 8..8': {
                        'prefix': '10.205.0.0/8',
                        'masklength_range': '8..8'
                    },
                    '10.205.0.0/8 8..16': {
                        'prefix': '10.205.0.0/8',
                        'masklength_range': '8..16'
                    },
                    '10.21.0.0/8 8..16': {
                        'prefix': '10.21.0.0/8',
                        'masklength_range': '8..16'
                    },
                    '10.94.0.0/8 24..32': {
                        'prefix': '10.94.0.0/8',
                        'masklength_range': '24..32'
                    },
                    '10.169.0.0/8 16..24': {
                        'prefix': '10.169.0.0/8',
                        'masklength_range': '16..24'
                    }
                }
            },
            'test6': {
                'prefix_set_name': 'test6',
                'protocol': 'ipv6',
                'prefixes': {
                    '2001:db8:1::/64 64..64': {
                        'prefix': '2001:db8:1::/64',
                        'masklength_range': '64..64'
                    },
                    '2001:db8:2::/64 65..128': {
                        'prefix': '2001:db8:2::/64',
                        'masklength_range': '65..128'
                    },
                    '2001:db8:3::/64 64..128': {
                        'prefix': '2001:db8:3::/64',
                        'masklength_range': '64..128'
                    },
                    '2001:db8:4::/64 65..98': {
                        'prefix': '2001:db8:4::/64',
                        'masklength_range': '65..98'
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        Thu Jul 20 12:07:25.163 EDT
        Listing for all Prefix Set objects

        prefix-set test
             10.205.0.0/8,
             10.205.0.0/8 le 16,
             10.21.0.0/8 le 16,
             10.94.0.0/8 ge 24,
             10.169.0.0/8 ge 16 le 24
        end-set
        !
        prefix-set test6
            2001:db8:1::/64,
             2001:db8:2::/64 ge 65,
             2001:db8:3::/64 le 128,
             2001:db8:4::/64 ge 65 le 98
        end-set
        !
    '''}

    golden_parsed_output_2 = {
        'prefix_set_name': {
            'test': {
                'prefix_set_name': 'test',
                'protocol': 'ipv4',
                'prefixes': {
                    '10.205.0.0/8 8..8': {
                        'prefix': '10.205.0.0/8',
                        'masklength_range': '8..8'
                    },
                    '10.205.0.0/8 8..16': {
                        'prefix': '10.205.0.0/8',
                        'masklength_range': '8..16'
                    },
                    '10.21.0.0/8 8..16': {
                        'prefix': '10.21.0.0/8',
                        'masklength_range': '8..16'
                    },
                    '10.94.0.0/8 24..32': {
                        'prefix': '10.94.0.0/8',
                        'masklength_range': '24..32'
                    },
                    '10.169.0.0/8 16..24': {
                        'prefix': '10.169.0.0/8',
                        'masklength_range': '16..24'
                    }
                }
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''\
        prefix-set test
             10.205.0.0/8,
             10.205.0.0/8 le 16,
             10.21.0.0/8 le 16,
             10.94.0.0/8 ge 24,
             10.169.0.0/8 ge 16 le 24
        end-set
    '''}

    device_output = {'execute.return_value': '''
+++ bl1-tatooine: executing command 'show rpl prefix-set' +++
show rpl prefix-set

Mon Oct  7 16:22:51.776 EDT
Listing for all Prefix Set objects

prefix-set PFX-AS577-MGMT
  1.1.1.0/24,
  1.1.2.0/24,
  1.1.3.0/24
end-set
!
prefix-set VPNe-Loopbacks
  12.12.12.12/20 eq 32,
  6.6.6.6/24 eq 32,
  8.8.8.8/24 eq 32,
  9.9.9.0/24 eq 32,
  6.3.5.0/24 eq 32,
  6.8.6.0/24 eq 32
end-set
!
RP/0/RSP0/CPU0:bl1-tatooine#

    '''}
    parsed_output = {
        'prefix_set_name': {
            'PFX-AS577-MGMT': {
                'prefix_set_name': 'PFX-AS577-MGMT',
                'prefixes': {
                    '1.1.1.0/24 24..24': {
                        'masklength_range': '24..24',
                        'prefix': '1.1.1.0/24',
                    },
                    '1.1.2.0/24 24..24': {
                        'masklength_range': '24..24',
                        'prefix': '1.1.2.0/24',
                    },
                    '1.1.3.0/24 24..24': {
                        'masklength_range': '24..24',
                        'prefix': '1.1.3.0/24',
                    },
                },
                'protocol': 'ipv4',
            },
            'VPNe-Loopbacks': {
                'prefix_set_name': 'VPNe-Loopbacks',
                'prefixes': {
                    '12.12.12.12/20 32..32': {
                        'masklength_range': '32..32',
                        'prefix': '12.12.12.12/20',
                    },
                    '6.3.5.0/24 32..32': {
                        'masklength_range': '32..32',
                        'prefix': '6.3.5.0/24',
                    },
                    '6.6.6.6/24 32..32': {
                        'masklength_range': '32..32',
                        'prefix': '6.6.6.6/24',
                    },
                    '6.8.6.0/24 32..32': {
                        'masklength_range': '32..32',
                        'prefix': '6.8.6.0/24',
                    },
                    '8.8.8.8/24 32..32': {
                        'masklength_range': '32..32',
                        'prefix': '8.8.8.8/24',
                    },
                    '9.9.9.0/24 32..32': {
                        'masklength_range': '32..32',
                        'prefix': '9.9.9.0/24',
                    },
                },
                'protocol': 'ipv4',
            },
        },
    }
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowRplPrefixSet(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_default(self):
        self.device = Mock(**self.golden_output)
        obj = ShowRplPrefixSet(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_name(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowRplPrefixSet(device=self.device)
        parsed_output = obj.parse(name='test')
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

    def test_2(self):
        self.device = Mock(**self.device_output)
        obj = ShowRplPrefixSet(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.parsed_output)

if __name__ == '__main__':
    unittest.main()
