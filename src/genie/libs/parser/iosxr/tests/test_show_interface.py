import re
import unittest
from unittest.mock import Mock

from pyats.topology import Device

from genie.metaparser.util.exceptions import (SchemaEmptyParserError,
                                              SchemaMissingKeyError)

from genie.libs.parser.iosxr.show_interface import (ShowInterfacesDetail,
                                                    ShowVlanInterface,
                                                    ShowIpv4VrfAllInterface,
                                                    ShowIpv6VrfAllInterface,
                                                    ShowEthernetTags,
                                                    ShowInterfacesAccounting,
                                                    ShowIpInterfaceBrief,
                                                    ShowIpv4InterfaceBrief,
                                                    ShowInterfaces,
                                                    ShowInterfacesDescription,
                                                    ShowIpv6Interface)


#############################################################################
# unitest For show ethernet tags
#############################################################################

class test_show_ethernet_tags(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "GigabitEthernet0/0/0/0.511": {
              "rewrite_num_of_tags_push": 0,
              "status": "up",
              "rewrite_num_of_tags_pop": 1,
              "mtu": 1518,
              "outer_vlan": ".1Q:511",
              "vlan_id": "511"
         },
         "GigabitEthernet0/0/0/0.510": {
              "rewrite_num_of_tags_push": 0,
              "status": "up",
              "rewrite_num_of_tags_pop": 1,
              "mtu": 1518,
              "outer_vlan": ".1Q:510",
              "vlan_id": "510"
         },
         "GigabitEthernet0/0/0/0.503": {
              "rewrite_num_of_tags_push": 0,
              "status": "up",
              "rewrite_num_of_tags_pop": 1,
              "mtu": 1518,
              "outer_vlan": ".1Q:503",
              "vlan_id": "503"
         },
         "GigabitEthernet0/0/0/0.501": {
              "rewrite_num_of_tags_push": 0,
              "status": "up",
              "rewrite_num_of_tags_pop": 1,
              "mtu": 1518,
              "outer_vlan": ".1Q:501",
              "vlan_id": "501"
         },
         "GigabitEthernet0/0/0/0.502": {
              "rewrite_num_of_tags_push": 0,
              "status": "up",
              "rewrite_num_of_tags_pop": 1,
              "mtu": 1518,
              "outer_vlan": ".1Q:502",
              "vlan_id": "502"
         },
         "GigabitEthernet0/0/0/0.504": {
              "rewrite_num_of_tags_push": 0,
              "status": "up",
              "rewrite_num_of_tags_pop": 1,
              "mtu": 1518,
              "outer_vlan": ".1Q:504",
              "vlan_id": "504"
         },
         "GigabitEthernet0/0/0/0.505": {
              "rewrite_num_of_tags_push": 0,
              "status": "up",
              "rewrite_num_of_tags_pop": 1,
              "mtu": 1518,
              "outer_vlan": ".1Q:505",
              "vlan_id": "505"
         },
         "GigabitEthernet0/0/0/1.501": {
              "rewrite_num_of_tags_push": 0,
              "status": "up",
              "rewrite_num_of_tags_pop": 1,
              "mtu": 1518,
              "outer_vlan": ".1Q:501",
              "vlan_id": "501"
         }

    }
    golden_parsed_interface_output = {
        "GigabitEthernet0/0/0/1.501": {
            "rewrite_num_of_tags_push": 0,
            "status": "up",
            "rewrite_num_of_tags_pop": 1,
            "mtu": 1518,
            "outer_vlan": ".1Q:501",
            "vlan_id": "501"
        }
    }

    golden_output = {'execute.return_value': '''
        St:    AD - Administratively Down, Dn - Down, Up - Up
        Ly:    L2 - Switched layer 2 service, L3 = Terminated layer 3 service,
        Xtra   C - Match on Cos, E  - Match on Ethertype, M - Match on source MAC
        -,+:   Ingress rewrite operation; number of tags to pop and push respectively

        Interface               St  MTU  Ly Outer            Inner            Xtra -,+
        Gi0/0/0/0.501           Up  1518 L3 .1Q:501          -                -    1 0
        Gi0/0/0/0.502           Up  1518 L3 .1Q:502          -                -    1 0
        Gi0/0/0/0.503           Up  1518 L3 .1Q:503          -                -    1 0
        Gi0/0/0/0.504           Up  1518 L3 .1Q:504          -                -    1 0
        Gi0/0/0/0.505           Up  1518 L3 .1Q:505          -                -    1 0
        Gi0/0/0/0.510           Up  1518 L3 .1Q:510          -                -    1 0
        Gi0/0/0/0.511           Up  1518 L3 .1Q:511          -                -    1 0
        Gi0/0/0/1.501           Up  1518 L3 .1Q:501          -                -    1 0


    '''}
    golden_interface_output={'execute.return_value': '''
        St:    AD - Administratively Down, Dn - Down, Up - Up
        Ly:    L2 - Switched layer 2 service, L3 = Terminated layer 3 service,
        Xtra   C - Match on Cos, E  - Match on Ethertype, M - Match on source MAC
        -,+:   Ingress rewrite operation; number of tags to pop and push respectively

        Interface               St  MTU  Ly Outer            Inner            Xtra -,+
        Gi0/0/0/1.501           Up  1518 L3 .1Q:501          -                -    1 0
    '''}


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowEthernetTags(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowEthernetTags(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_custom(self):
        self.device = Mock(**self.golden_output)
        obj = ShowEthernetTags(device=self.device)
        parsed_output = obj.parse(interface='Gi0/0/0/1.501')
        self.assertEqual(parsed_output,self.golden_parsed_output)



if __name__ == '__main__':
    unittest.main()

