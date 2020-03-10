#!/bin/env python
import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError

from genie.libs.parser.nxos.aci.show_platform import ShowPlatformInternalHalPolicyRedirdst
class TestShowPlatformInternalHalPolicyRedirdst(unittest.TestCase):

    dev = Device(name='aci')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'group_id': {
            '0x224': {
                'dst_ip': '10.69.9.9/32',
                'outgoing_ifname': 'Tunnel30',
                'outgoing_l2_ifindex': '0x1801001e',
                'packets_hash': '0x29d2',
                'protocol': '0x1',
                'rewrite_mac': '00:00:00:ff:02:03',
                'rewrite_vnid': '0xf08007',
                'src_ip': '10.1.1.1/32',
            },
        },
    }

    golden_output = {'execute.return_value': '''\
        Group Id                                                 : 0x224 
        Src IP                                                    : 10.1.1.1/32 
        Dst IP                                                    : 10.69.9.9/32 
        Protocol                                                  : 0x1 

        Rewrite MAC                                               : 00:00:00:ff:02:03 
        Rewrite VNID                                              : 0xf08007 
        Outgoing L2 IfIndex                                       : 0x1801001e 
        Outgoing IfName                                           : Tunnel30 

        Packet's Hash                                             : 0x29d2 
                                    
    '''
    }

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowPlatformInternalHalPolicyRedirdst(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsered_output = obj.parse(
                group_id='548', 
                address_family='ipv4',
                src_ip='10.1.1.1',
                dst_ip='10.69.9.9',
                protocol='1')

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowPlatformInternalHalPolicyRedirdst(device=self.dev)
        parsed_output = obj.parse(
                group_id='548', 
                address_family='ipv4',
                src_ip='10.1.1.1',
                dst_ip='10.69.9.9',
                protocol='1')
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()