# **************************************************
# test file test_show_bgp.py
#
# Python
import unittest
from unittest.mock import Mock
# Ats
from ats.topology import Device
# Metaparser
from metaparser.util.exceptions import SchemaEmptyParserError
# nxos show_bgp
from parser.nxos.show_bgp import ShowBgpVrfAllAllDampeningParameters


class TestShowBgpVrfAllAllDampeningParameters(unittest.TestCase):
    ''' unittest for "show bgp vrf all all dampening parameters"
    '''
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'vrf':
                            {'VRF1':
                             {'address_family':
                              {'ipv4 unicast':
                               {'dampening': 'True',
                                'dampening_route_map': 'dampening1',
                                'dampening_half_life_time': '45',
                                'dampening_reuse_time': '10000',
                                'dampening_suppress_time': '20000',
                                'dampening_max_suppress_time': '255',
                                'dampening_max_suppress_penalty': '507968'},
                               'ipv6 unicast':
                               {'dampening': 'True',
                                'dampening_route_map': 'dampening2',
                                'dampening_half_life_time': '45',
                                'dampening_reuse_time': '9999',
                                'dampening_suppress_time': '19999',
                                'dampening_max_suppress_time': '255',
                                'dampening_max_suppress_penalty': '507917'}}},
                             'default':
                             {'address_family':
                              {'ipv4 unicast':
                               {'dampening': 'True',
                                'dampening_half_life_time': '45',
                                'dampening_reuse_time': '1111',
                                'dampening_suppress_time': '2222',
                                'dampening_max_suppress_time': '255',
                                'dampening_max_suppress_penalty': '56435'},
                              'vpnv4 unicast':
                               {'dampening': 'True',
                                'route_distinguisher':
                                 {'1:100':
                                  {'rd_vrf': 'vpn1',
                                   'dampening_half_life_time': '1 mins',
                                   'dampening_reuse_time': '10',
                                   'dampening_suppress_time': '30',
                                   'dampening_max_suppress_time': '2 mins',
                                   'dampening_max_suppress_penalty': '40'}}}}}}}

    golden_output = {'execute.return_value': '''
Route Flap Dampening Parameters for VRF VRF1 Address family IPv4 Unicast:

Dampening policy configured: dampening1

Half-life time                 : 45
Suppress penalty               : 20000
Reuse penalty                  : 10000
Max suppress time              : 255
Max suppress penalty           : 507968

Route Flap Dampening Parameters for VRF VRF1 Address family IPv6 Unicast:

Dampening policy configured: dampening2

Half-life time                 : 45
Suppress penalty               : 19999
Reuse penalty                  : 9999
Max suppress time              : 255
Max suppress penalty           : 507917

Route Flap Dampening Parameters for VRF default Address family IPv4 Unicast:

Configured values in use:

Half-life time                 : 45
Suppress penalty               : 2222
Reuse penalty                  : 1111
Max suppress time              : 255
Max suppress penalty           : 56435

Route Flap Dampening Parameters for VRF default Address family VPNv4 Unicast:
Route Distinguisher: 1:100    (VRF vpn1)

Configured values in use:

Half-life time                 : 1 mins
Suppress penalty               : 30
Reuse penalty                  : 10
Max suppress time              : 2 mins
Max suppress penalty           : 40


'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        bgp_obj = ShowBgpVrfAllAllDampeningParameters(device=self.device)
        parsed_output = bgp_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_obj = ShowBgpVrfAllAllDampeningParameters(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_obj.parse()


if __name__ == '__main__':
    unittest.main()
