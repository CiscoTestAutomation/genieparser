#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.iosxe.show_run import ShowRunPolicyMap


class test_show_run_policy_map(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
    "policy_map": {
        "L3VPN-0_in": {
            "class": {
                "HEY_in": {
                    "police": {
                        "cir_bps": "365",
                        "pir_bps": "235",
                        "conformed": "transmit",
                        "exceeded": "drop"
                    }
                },
                "OSPF": {
                    "police": {
                        "cir_bps": "543",
                        "pir_bps": "876",
                        "conformed": "transmit",
                        "exceeded": "drop"
                    }
                },
                "class-default": {
                    "police": {
                        "cir_bps": "2565",
                        "cir_bc_bytes": "4234",
                        "conformed": "transmit",
                        "exceeded": "drop"
                    },
                    "service_policy": "child"
                }
            }
        }
    }
}

    golden_output = {'execute.return_value': '''\
    show run policy-map L3VPN-0_in
    Building configuration...

    Current configuration : 56 bytes
    !
    policy-map L3VPN-0_in
     class HEY_in
      police cir 365 pir 235 conform-action transmit  exceed-action drop
     class OSPF
      police cir 543 pir 876 conform-action transmit  exceed-action drop
     class class-default
      police cir 2565 bc 4234 conform-action transmit  exceed-action drop
       service-policy child
    !
    end
    '''
    }

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowRunPolicyMap(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(name= 'L3VPN-0_in')

    def test_golden(self):
        self.device1 = Mock(**self.golden_output)
        obj = ShowRunPolicyMap(device=self.device1)
        parsed_output = obj.parse(name= 'L3VPN-0_in')
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()