#!/bin/env python

import unittest
from unittest.mock import Mock

from pyats.topology import Device

from genie.ops.base import Context

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.slxos.show_lldp import ShowLldpNeighbors


class test_show_lldp_neighbors_yang(unittest.TestCase):

    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    golden_parsed_output = {
        "interfaces": {
            "Ethernet 0/2": {
                "local_interface_name": "Ethernet 0/2",
                "neighbors": {
                    "Bundle-Ether1": {
                        "remote_chassis_id": "94ae.f095.f4d9",
                        "remote_interface_name": "Bundle-Ether1",
                        "remote_system_name": "lab-ncs5501-pe1",
                    }
                },
            },
            "Ethernet 0/43": {
                "local_interface_name": "Ethernet 0/43",
                "neighbors": {
                    "000a.f741.5d92": {
                        "remote_chassis_id": "000a.f741.5d92",
                        "remote_interface_name": "000a.f741.5d92",
                        "remote_system_name": "trafficgen-server",
                    }
                },
            },
            "Ethernet 0/44": {
                "local_interface_name": "Ethernet 0/44",
                "neighbors": {
                    "000a.f741.5d90": {
                        "remote_chassis_id": "000a.f741.5d90",
                        "remote_interface_name": "000a.f741.5d90",
                        "remote_system_name": "trafficgen-server",
                    }
                },
            },
            "Ethernet 0/46": {
                "local_interface_name": "Ethernet 0/46",
                "neighbors": {
                    "90b1.1c08.a4a3": {
                        "remote_chassis_id": "90b1.1c08.a4a3",
                        "remote_interface_name": "90b1.1c08.a4a3",
                    }
                },
            },
            "Ethernet 0/47": {
                "local_interface_name": "Ethernet 0/47",
                "neighbors": {
                    "90b1.1c08.a4a5": {
                        "remote_chassis_id": "90b1.1c08.a4a5",
                        "remote_interface_name": "90b1.1c08.a4a5",
                    }
                },
            },
            "Ethernet 0/5": {
                "local_interface_name": "Ethernet 0/5",
                "neighbors": {
                    "Bundle-Ether1": {
                        "remote_chassis_id": "94ae.f09c.94d9",
                        "remote_interface_name": "Bundle-Ether1",
                        "remote_system_name": "lab-ncs5501-pe2",
                    }
                },
            },
            "Ethernet 0/50": {
                "local_interface_name": "Ethernet 0/50",
                "neighbors": {
                    "HundredGigE0/0/0/32": {
                        "remote_chassis_id": "94ae.f07b.c0d9",
                        "remote_interface_name": "HundredGigE0/0/0/32",
                        "remote_system_name": "lab-ncs5502-p1",
                    }
                },
            },
            "Ethernet 0/51": {
                "local_interface_name": "Ethernet 0/51",
                "neighbors": {
                    "HundredGigE0/0/1/0": {
                        "remote_chassis_id": "94ae.f095.f4d9",
                        "remote_interface_name": "HundredGigE0/0/1/0",
                        "remote_system_name": "lab-ncs5501-pe1",
                    }
                },
            },
            "Ethernet 0/52": {
                "local_interface_name": "Ethernet 0/52",
                "neighbors": {
                    "HundredGigE0/0/1/1": {
                        "remote_chassis_id": "94ae.f095.f4d9",
                        "remote_interface_name": "HundredGigE0/0/1/1",
                        "remote_system_name": "lab-ncs5501-pe1",
                    }
                },
            },
        },
        "total_entries": 9,
    }

    golden_raw_output = '''
      <rpc-reply message-id="urn:uuid:81e136a3-a5ac-4e0d-9a2e-5cef686c4f73" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
        <lldp-neighbor-detail xmlns="urn:brocade.com:mgmt:brocade-lldp-ext">
          <local-interface-name>Eth 0/2</local-interface-name>
          <local-interface-ifindex>201342976</local-interface-ifindex>
          <local-interface-mac>609c.9fde.2f1a</local-interface-mac>
          <remote-interface-name>Bundle-Ether1</remote-interface-name>
          <remote-interface-mac>94ae.f095.f4dd</remote-interface-mac>
          <dead-interval>120</dead-interval>
          <remaining-life>91</remaining-life>
          <remote-chassis-id>94ae.f095.f4d9</remote-chassis-id>
          <lldp-pdu-transmitted>51417</lldp-pdu-transmitted>
          <lldp-pdu-received>51673</lldp-pdu-received>
          <remote-port-description>Connection to CE</remote-port-description>
          <remote-system-name>lab-ncs5501-pe1</remote-system-name>
          <remote-system-description> 7.4.1.30I, NCS-5500</remote-system-description>
        </lldp-neighbor-detail>
        <lldp-neighbor-detail xmlns="urn:brocade.com:mgmt:brocade-lldp-ext">
          <local-interface-name>Eth 0/5</local-interface-name>
          <local-interface-ifindex>201367552</local-interface-ifindex>
          <local-interface-mac>609c.9fde.2f1d</local-interface-mac>
          <remote-interface-name>Bundle-Ether1</remote-interface-name>
          <remote-interface-mac>94ae.f09c.94dd</remote-interface-mac>
          <dead-interval>120</dead-interval>
          <remaining-life>104</remaining-life>
          <remote-chassis-id>94ae.f09c.94d9</remote-chassis-id>
          <lldp-pdu-transmitted>51417</lldp-pdu-transmitted>
          <lldp-pdu-received>51673</lldp-pdu-received>
          <remote-port-description>Connection to CE</remote-port-description>
          <remote-system-name>lab-ncs5501-pe2</remote-system-name>
          <remote-system-description> 7.4.1.30I, NCS-5500</remote-system-description>
        </lldp-neighbor-detail>
        <lldp-neighbor-detail xmlns="urn:brocade.com:mgmt:brocade-lldp-ext">
          <local-interface-name>Eth 0/43</local-interface-name>
          <local-interface-ifindex>201678848</local-interface-ifindex>
          <local-interface-mac>609c.9fde.2f43</local-interface-mac>
          <remote-interface-name>000a.f741.5d92</remote-interface-name>
          <remote-interface-mac>000a.f741.5d92</remote-interface-mac>
          <dead-interval>120</dead-interval>
          <remaining-life>95</remaining-life>
          <remote-chassis-id>000a.f741.5d92</remote-chassis-id>
          <lldp-pdu-transmitted>154255</lldp-pdu-transmitted>
          <lldp-pdu-received>257089</lldp-pdu-received>
          <remote-port-description>p1p2</remote-port-description>
          <remote-system-name>trafficgen-server</remote-system-name>
          <remote-system-description>Ubuntu 14.04.5 LTS Linux 4.4.0-31-generic #50~14.0</remote-system-description>
        </lldp-neighbor-detail>
        <lldp-neighbor-detail xmlns="urn:brocade.com:mgmt:brocade-lldp-ext">
          <local-interface-name>Eth 0/44</local-interface-name>
          <local-interface-ifindex>201687040</local-interface-ifindex>
          <local-interface-mac>609c.9fde.2f44</local-interface-mac>
          <remote-interface-name>000a.f741.5d90</remote-interface-name>
          <remote-interface-mac>000a.f741.5d90</remote-interface-mac>
          <dead-interval>120</dead-interval>
          <remaining-life>96</remaining-life>
          <remote-chassis-id>000a.f741.5d90</remote-chassis-id>
          <lldp-pdu-transmitted>154255</lldp-pdu-transmitted>
          <lldp-pdu-received>257089</lldp-pdu-received>
          <remote-port-description>p1p1</remote-port-description>
          <remote-system-name>trafficgen-server</remote-system-name>
          <remote-system-description>Ubuntu 14.04.5 LTS Linux 4.4.0-31-generic #50~14.0</remote-system-description>
        </lldp-neighbor-detail>
        <lldp-neighbor-detail xmlns="urn:brocade.com:mgmt:brocade-lldp-ext">
          <local-interface-name>Eth 0/46</local-interface-name>
          <local-interface-ifindex>201703424</local-interface-ifindex>
          <local-interface-mac>609c.9fde.2f46</local-interface-mac>
          <remote-interface-name>90b1.1c08.a4a3</remote-interface-name>
          <remote-interface-mac>90b1.1c08.a4a3</remote-interface-mac>
          <dead-interval>120</dead-interval>
          <remaining-life>116</remaining-life>
          <remote-chassis-id>90b1.1c08.a4a3</remote-chassis-id>
          <lldp-pdu-transmitted>51417</lldp-pdu-transmitted>
          <lldp-pdu-received>50910</lldp-pdu-received>
        </lldp-neighbor-detail>
        <lldp-neighbor-detail xmlns="urn:brocade.com:mgmt:brocade-lldp-ext">
          <local-interface-name>Eth 0/47</local-interface-name>
          <local-interface-ifindex>201711616</local-interface-ifindex>
          <local-interface-mac>609c.9fde.2f47</local-interface-mac>
          <remote-interface-name>90b1.1c08.a4a5</remote-interface-name>
          <remote-interface-mac>90b1.1c08.a4a5</remote-interface-mac>
          <dead-interval>120</dead-interval>
          <remaining-life>117</remaining-life>
          <remote-chassis-id>90b1.1c08.a4a5</remote-chassis-id>
          <lldp-pdu-transmitted>51417</lldp-pdu-transmitted>
          <lldp-pdu-received>50910</lldp-pdu-received>
        </lldp-neighbor-detail>
        <lldp-neighbor-detail xmlns="urn:brocade.com:mgmt:brocade-lldp-ext">
          <local-interface-name>Eth 0/50</local-interface-name>
          <local-interface-ifindex>201736448</local-interface-ifindex>
          <local-interface-mac>609c.9fde.2f4a</local-interface-mac>
          <remote-interface-name>HundredGigE0/0/0/32</remote-interface-name>
          <remote-interface-mac>94ae.f07b.c080</remote-interface-mac>
          <dead-interval>120</dead-interval>
          <remaining-life>101</remaining-life>
          <remote-chassis-id>94ae.f07b.c0d9</remote-chassis-id>
          <lldp-pdu-transmitted>51417</lldp-pdu-transmitted>
          <lldp-pdu-received>51674</lldp-pdu-received>
          <remote-port-description>P</remote-port-description>
          <remote-system-name>lab-ncs5502-p1</remote-system-name>
          <remote-system-description> 7.1.2, NCS-5500</remote-system-description>
        </lldp-neighbor-detail>
        <lldp-neighbor-detail xmlns="urn:brocade.com:mgmt:brocade-lldp-ext">
          <local-interface-name>Eth 0/51</local-interface-name>
          <local-interface-ifindex>201744640</local-interface-ifindex>
          <local-interface-mac>609c.9fde.2f4b</local-interface-mac>
          <remote-interface-name>HundredGigE0/0/1/0</remote-interface-name>
          <remote-interface-mac>94ae.f095.f4c0</remote-interface-mac>
          <dead-interval>120</dead-interval>
          <remaining-life>99</remaining-life>
          <remote-chassis-id>94ae.f095.f4d9</remote-chassis-id>
          <lldp-pdu-transmitted>51417</lldp-pdu-transmitted>
          <lldp-pdu-received>51674</lldp-pdu-received>
          <remote-port-description>P</remote-port-description>
          <remote-system-name>lab-ncs5501-pe1</remote-system-name>
          <remote-system-description> 7.4.1.30I, NCS-5500</remote-system-description>
        </lldp-neighbor-detail>
        <lldp-neighbor-detail xmlns="urn:brocade.com:mgmt:brocade-lldp-ext">
          <local-interface-name>Eth 0/52</local-interface-name>
          <local-interface-ifindex>201752832</local-interface-ifindex>
          <local-interface-mac>609c.9fde.2f4c</local-interface-mac>
          <remote-interface-name>HundredGigE0/0/1/1</remote-interface-name>
          <remote-interface-mac>94ae.f095.f4c4</remote-interface-mac>
          <dead-interval>120</dead-interval>
          <remaining-life>108</remaining-life>
          <remote-chassis-id>94ae.f095.f4d9</remote-chassis-id>
          <lldp-pdu-transmitted>58638</lldp-pdu-transmitted>
          <lldp-pdu-received>32</lldp-pdu-received>
          <remote-port-description>P</remote-port-description>
          <remote-system-name>lab-ncs5501-pe1</remote-system-name>
          <remote-system-description> 7.4.1.30I, NCS-5500</remote-system-description>
        </lldp-neighbor-detail>
        <has-more xmlns="urn:brocade.com:mgmt:brocade-lldp-ext">false</has-more>
      </rpc-reply>
    '''
    golden_output = {'request.return_value': golden_raw_output}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        intf_obj = ShowLldpNeighbors(device=self.device)
        intf_obj.context = Context.yang.value.split()
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    empty_parsed_output = {'total_entries': 0}

    empty_raw_output = '''
      <rpc-reply message-id="urn:uuid:ac7a6b74-7b8a-4f02-9708-39478e94e491" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
        <has-more xmlns="urn:brocade.com:mgmt:brocade-lldp-ext">false</has-more>
      </rpc-reply>
    '''
    empty_output = {'request.return_value': empty_raw_output}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        intf_obj = ShowLldpNeighbors(device=self.device1)
        intf_obj.context = Context.yang.value.split()
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output, self.empty_parsed_output)


if __name__ == '__main__':
    unittest.main()
