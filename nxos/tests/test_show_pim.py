import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from parser.nxos.show_pim import ShowIpv6PimVrfAllDetail\







# ============================================
# Parser for 'show ipv6 pim vrf all detail'
# ============================================
class test_show_ipv6_pim_vrf_all_detail(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_v6_vrf_detail_1 = {
        'vrf':{
            'default':
                {
                'address_family':
                    {'ipv6':
                        {
                        'vrf_id': 1,
                        'table_id': '0x80000001',
                        'interface_count': 3,
                        'bfd': {
                            'enable': False,
                        },

                        'state_limit': 'none',
                        'register_rate_limit': 'none',
                        'shared_tree_route_map':'v6spt-threshold-group-list',
                        },
                    },
                },
            'VRF1':
                {
                'address_family':
                    {'ipv6':
                        {
                        'vrf_id': 3,
                        'table_id': '0x80000003',
                        'interface_count': 3,
                        'bfd': {
                            'enable': False,
                        },

                        'state_limit': 'none',
                        'register_rate_limit': 'none',
                        'shared_tree_ranges': 'none',
                    },
                },
            },
        },
    }
    golden_output_vrf_v6_detail_1 = {'execute.return_value': '''
        R1# show ipv6 pim vrf all detail
        PIM6 Enabled VRFs
        VRF Name              VRF      Table       Interface  BFD
                              ID       ID          Count      Enabled
        default               1        0x80000001  3          no
          State Limit: None
          Register Rate Limit: none
          Shared tree route-map: v6spt-threshold-group-list
                 route-ranges:

        VRF1                  3        0x80000003  3          no
          State Limit: None
          Register Rate Limit: none
          Shared tree ranges: none
    '''}

    golden_output_vrf_v6_detail_2 = {'execute.return_value': '''
            R1# show ip pim vrf all detail
            PIM6 Enabled VRFs
            %S DDDD
        '''}
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6PimVrfAllDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_v6_vrf_detail_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_vrf_v6_detail_1)
        obj = ShowIpv6PimVrfAllDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_v6_vrf_detail_1)

    def test_golden_v6_vrf_detail_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_vrf_v6_detail_2)
        obj = ShowIpv6PimVrfAllDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

if __name__ == '__main__':
    unittest.main()