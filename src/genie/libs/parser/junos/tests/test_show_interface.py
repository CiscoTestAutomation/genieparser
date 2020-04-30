import re
import unittest
from unittest.mock import Mock

from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.junos.show_interface import (ShowInterfacesTerse,
                                                    ShowInterfacesTerseMatch,
                                                    ShowInterfaces)

#############################################################################
# unitest For show interfaces terse [| match <interface>]
#############################################################################

class test_show_interfaces_terse(unittest.TestCase):
    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
         'em1': {'admin_state': 'up',
                 'enabled': True,
                 'link_state': 'up',
                 'oper_status': 'up'},
         'em1.0': {'admin_state': 'up',
                   'enabled': True,
                   'link_state': 'up',
                   'oper_status': 'up',
                   'protocol': {'inet': {'10.0.0.4/8': {'local': '10.0.0.4/8'},
                                         '172.16.64.1/2': {'local': '172.16.64.1/2'},
                                         '172.16.64.4/2': {'local': '172.16.64.4/2'}},
                                'inet6': {'fe80::250:56ff:fe82:ba52/64': {'local': 'fe80::250:56ff:fe82:ba52/64'},
                                          '2001:db8:8d82:0:a::4/64': {'local': '2001:db8:8d82:0:a::4/64'}},
                                'tnp': {'0x4': {'local': '0x4'}}}},
         'fxp0': {'admin_state': 'up',
                  'enabled': True,
                  'link_state': 'up',
                  'oper_status': 'up'},
         'fxp0.0': {'admin_state': 'up',
                    'enabled': True,
                    'link_state': 'up',
                    'oper_status': 'up',
                    'protocol': {'inet': {'172.25.192.114/24': {'local': '172.25.192.114/24'}}}},
         'ge-0/0/0': {'admin_state': 'up',
                      'enabled': True,
                      'link_state': 'up',
                      'oper_status': 'up'},
         'ge-0/0/0.0': {'admin_state': 'up',
                        'enabled': True,
                        'link_state': 'up',
                        'oper_status': 'up',
                        'protocol': {'inet': {'10.0.1.1/24': {'local': '10.0.1.1/24'}},
                                     'multiservice': {}}},
         'ge-0/0/1': {'admin_state': 'up',
                      'enabled': True,
                      'link_state': 'up',
                      'oper_status': 'up'},
         'ge-0/0/1.0': {'admin_state': 'up',
                        'enabled': True,
                        'link_state': 'up',
                        'oper_status': 'up',
                        'protocol': {'inet': {'10.0.2.1/24': {'local': '10.0.2.1/24'}},
                                     'multiservice': {}}},
         'ge-0/0/2': {'admin_state': 'up',
                      'enabled': True,
                      'link_state': 'down',
                      'oper_status': 'down'},
         'lc-0/0/0': {'admin_state': 'up',
                      'enabled': True,
                      'link_state': 'up',
                      'oper_status': 'up'},
         'lc-0/0/0.32769': {'admin_state': 'up',
                            'enabled': True,
                            'link_state': 'up',
                            'oper_status': 'up',
                            'protocol': {'vpls': {}}},
         'lo0.0': {'admin_state': 'up',
                   'enabled': True,
                   'link_state': 'up',
                   'oper_status': 'up',
                   'protocol': {'inet': {'10.1.1.1': {'local': '10.1.1.1',
                                                      'remote': '0/0'},
                                         '10.11.11.11': {'local': '10.11.11.11',
                                                         'remote': '0/0'}}}},
         'lo0.16384': {'admin_state': 'up',
                       'enabled': True,
                       'link_state': 'up',
                       'oper_status': 'up',
                       'protocol': {'inet': {'127.0.0.1': {'local': '127.0.0.1',
                                                           'remote': '0/0'}}}},
         'lo0.16385': {'admin_state': 'up',
                       'enabled': True,
                       'link_state': 'up',
                       'oper_status': 'up',
                       'protocol': {'inet': {}}},
         'pfe-0/0/0': {'admin_state': 'up',
                       'enabled': True,
                       'link_state': 'up',
                       'oper_status': 'up'},
         'pfe-0/0/0.16383': {'admin_state': 'up',
                             'enabled': True,
                             'link_state': 'up',
                             'oper_status': 'up',
                             'protocol': {'inet': {}, 'inet6': {}}},
         'pfh-0/0/0': {'admin_state': 'up',
                       'enabled': True,
                       'link_state': 'up',
                       'oper_status': 'up'},
         'pfh-0/0/0.16383': {'admin_state': 'up',
                             'enabled': True,
                             'link_state': 'up',
                             'oper_status': 'up',
                             'protocol': {'inet': {}}},
         'pfh-0/0/0.16384': {'admin_state': 'up',
                             'enabled': True,
                             'link_state': 'up',
                             'oper_status': 'up',
                             'protocol': {'inet': {}}},
    }

    golden_output = {'execute.return_value': '''
        root@junos_vmx1> show interfaces terse 
        Interface               Admin Link Proto    Local                 Remote
        ge-0/0/0                up    up
        ge-0/0/0.0              up    up   inet     10.0.1.1/24     
                                           multiservice
        lc-0/0/0                up    up
        lc-0/0/0.32769          up    up   vpls    
        pfe-0/0/0               up    up
        pfe-0/0/0.16383         up    up   inet    
                                           inet6   
        pfh-0/0/0               up    up
        pfh-0/0/0.16383         up    up   inet    
        pfh-0/0/0.16384         up    up   inet    
        ge-0/0/1                up    up
        ge-0/0/1.0              up    up   inet     10.0.2.1/24     
                                           multiservice
        ge-0/0/2                up    down
        em1                     up    up
        em1.0                   up    up   inet     10.0.0.4/8      
                                                    172.16.64.1/2     
                                                    172.16.64.4/2     
                                           inet6    fe80::250:56ff:fe82:ba52/64
                                                    2001:db8:8d82:0:a::4/64
                                           tnp      0x4  
        fxp0                    up    up
        fxp0.0                  up    up   inet     172.25.192.114/24
        lo0.0                   up    up   inet     10.1.1.1            --> 0/0
                                                    10.11.11.11         --> 0/0
        lo0.16384               up    up   inet     127.0.0.1           --> 0/0
        lo0.16385               up    up   inet  
    '''
    }

    golden_output_interface = {'execute.return_value': """
    root@junos_vmx1 > show interfaces em1.0 terse
    em1.0                   up    up   inet     10.0.0.4/8      
                                                    172.16.64.1/2     
                                                    172.16.64.4/2     
                                           inet6    fe80::250:56ff:fe82:ba52/64
                                                    2001:db8:8d82:0:a::4/64
                                           tnp      0x4 
    """}

    golden_parsed_output_interface = {
        'em1.0': {
            'admin_state': 'up',
            'enabled': True,
            'link_state': 'up',
            'oper_status': 'up',
            'protocol': {
                'inet': {
                    '10.0.0.4/8': {
                        'local': '10.0.0.4/8'
                    },
                    '172.16.64.1/2': {
                        'local': '172.16.64.1/2'
                    },
                    '172.16.64.4/2': {
                        'local': '172.16.64.4/2'
                    }
                },
                'inet6': {
                    'fe80::250:56ff:fe82:ba52/64': {
                        'local': 'fe80::250:56ff:fe82:ba52/64'
                    },
                    '2001:db8:8d82:0:a::4/64': {
                        'local': '2001:db8:8d82:0:a::4/64'
                    }
                },
                'tnp': {
                    '0x4': {
                        'local': '0x4'
                    }
                }
            }
        }
    }

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_obj = ShowInterfacesTerse(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowInterfacesTerse(device=self.device)
        parsed_output = interface_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_interface(self):
        self.device = Mock(**self.golden_output_interface)
        interface_obj = ShowInterfacesTerse(device=self.device)
        parsed_output = interface_obj.parse(interface='em1.0')
        self.assertEqual(parsed_output, self.golden_parsed_output_interface)


class test_show_interfaces_terse_match(unittest.TestCase):
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'fxp0': {'admin_state': 'up',
                 'enabled': True,
                 'link_state': 'up',
                 'oper_status': 'up'},
        'fxp0.0': {'admin_state': 'up',
                   'enabled': True,
                   'link_state': 'up',
                   'oper_status': 'up',
                   'protocol': {'inet': {'172.25.192.114/24': {'local': '172.25.192.114/24'}}}}
    }

    golden_output = {'execute.return_value': '''
        root@junos_vmx1> show interfaces terse | match fxp0 
        fxp0                    up    up
        fxp0.0                  up    up   inet     172.25.192.114/24
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_obj = ShowInterfacesTerseMatch(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            interface_obj.parse(interface='fxp0')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowInterfacesTerseMatch(device=self.device)
        parsed_output = interface_obj.parse(interface='fxp0')
        self.assertEqual(parsed_output, self.golden_parsed_output)

class TestShowInterfaces(unittest.TestCase):
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "interface-information": {
            "physical-interface": [
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "00:50:56:8d:c8:29",
                    "description": "none/100G/in/hktGCS002_ge-0/0/0",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "00:50:56:8d:c8:29",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:19 UTC (29w6d 18:56 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "local-index": "148",
                    "logical-interface": {
                        "address-family": [
                            {
                                "address-family-flags": {
                                    "ifff-no-redirects": True,
                                    "ifff-sendbcast-pkt-to-re": True
                                },
                                "address-family-name": "inet",
                                "interface-address": {
                                    "ifa-broadcast": "111.87.5.95",
                                    "ifa-destination": "111.87.5.92/30",
                                    "ifa-flags": {
                                        "ifaf-is-preferred": True,
                                        "ifaf-is-primary": True
                                    },
                                    "ifa-local": "111.87.5.93"
                                },
                                "intf-curr-cnt": "1",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "75000",
                                "mtu": "1500",
                                "new-hold-limit": "75000"
                            },
                            {
                                "address-family-flags": {
                                    "ifff-is-primary": True
                                },
                                "address-family-name": "inet6",
                                "interface-address": [
                                    {
                                        "ifa-destination": "2001:268:fb90:14::/64",
                                        "ifa-flags": {
                                            "ifaf-is-preferred": True,
                                            "ifaf-is-primary": True
                                        },
                                        "ifa-local": "2001:268:fb90:14::1"
                                    },
                                    {
                                        "ifa-destination": "fe80::/64",
                                        "ifa-flags": {
                                            "ifaf-is-preferred": True
                                        },
                                        "ifa-local": "fe80::250:56ff:fe8d:c829"
                                    }
                                ],
                                "intf-curr-cnt": "1",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "75000",
                                "mtu": "1500",
                                "new-hold-limit": "75000"
                            },
                            {
                                "address-family-flags": {
                                    "ifff-is-primary": True
                                },
                                "address-family-name": "mpls",
                                "maximum-labels": "3",
                                "mtu": "1488"
                            },
                            {
                                "address-family-flags": {
                                    "ifff-is-primary": True
                                },
                                "address-family-name": "multiservice",
                                "mtu": "Unlimited"
                            }
                        ],
                        "encapsulation": "ENET2",
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True,
                            "internal-flags": "0x4004000"
                        },
                        "local-index": "333",
                        "name": "ge-0/0/0.0",
                        "snmp-index": "606",
                        "traffic-statistics": {
                            "input-packets": "0",
                            "output-packets": "0"
                        }
                    },
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/0",
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "snmp-index": "526",
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "traffic-statistics": {
                        "input-bps": "2952",
                        "input-pps": "5",
                        "output-bps": "3080",
                        "output-pps": "3"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "local-index": "145",
                    "logical-interface": {
                        "address-family": [
                            {
                                "address-family-flags": {
                                    "ifff-is-primary": True
                                },
                                "address-family-name": "vpls",
                                "mtu": "Unlimited"
                            }
                        ],
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True
                        },
                        "local-index": "329",
                        "logical-interface-bandwidth": "0",
                        "name": "lc-0/0/0.32769",
                        "snmp-index": "520",
                        "traffic-statistics": {
                            "input-packets": "0",
                            "output-packets": "0"
                        }
                    },
                    "name": "lc-0/0/0",
                    "snmp-index": "519",
                    "speed": "800mbps"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "local-index": "147",
                    "logical-interface": {
                        "address-family": [
                            {
                                "address-family-flags": {
                                    "ifff-none": True
                                },
                                "address-family-name": "inet",
                                "intf-curr-cnt": "0",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "0",
                                "mtu": "Unlimited",
                                "new-hold-limit": "0"
                            },
                            {
                                "address-family-flags": {
                                    "ifff-none": True
                                },
                                "address-family-name": "inet6",
                                "intf-curr-cnt": "0",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "0",
                                "mtu": "Unlimited",
                                "new-hold-limit": "0"
                            }
                        ],
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True
                        },
                        "local-index": "330",
                        "logical-interface-bandwidth": "0",
                        "name": "pfe-0/0/0.16383",
                        "snmp-index": "523",
                        "traffic-statistics": {
                            "input-packets": "0",
                            "output-packets": "0"
                        }
                    },
                    "name": "pfe-0/0/0",
                    "snmp-index": "522",
                    "speed": "800mbps"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "local-index": "146",
                    "logical-interface": {
                        "address-family": [
                            {
                                "address-family-flags": {
                                    "ifff-none": True
                                },
                                "address-family-name": "inet",
                                "intf-curr-cnt": "0",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "0",
                                "mtu": "Unlimited",
                                "new-hold-limit": "0"
                            },
                            {
                                "address-family-flags": {
                                    "ifff-is-primary": True
                                },
                                "address-family-name": "inet",
                                "intf-curr-cnt": "0",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "0",
                                "mtu": "Unlimited",
                                "new-hold-limit": "0"
                            }
                        ],
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True
                        },
                        "local-index": "332",
                        "logical-interface-bandwidth": "0",
                        "name": "pfh-0/0/0.16384",
                        "snmp-index": "525",
                        "traffic-statistics": {
                            "input-packets": "0",
                            "output-packets": "0"
                        }
                    },
                    "name": "pfh-0/0/0",
                    "snmp-index": "521",
                    "speed": "800mbps"
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "00:50:56:8d:a9:6c",
                    "description": "YW7079/9.6G/BB/sjkGCS001-EC11_xe-0/1/5[SJC]_Area8_Cost100",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "00:50:56:8d:a9:6c",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:19 UTC (29w6d 18:56 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "local-index": "149",
                    "logical-interface": {
                        "address-family": [
                            {
                                "address-family-flags": {
                                    "ifff-no-redirects": True,
                                    "ifff-sendbcast-pkt-to-re": True
                                },
                                "address-family-name": "inet",
                                "interface-address": {
                                    "ifa-broadcast": "106.187.14.123",
                                    "ifa-destination": "106.187.14.120/30",
                                    "ifa-flags": {
                                        "ifaf-is-preferred": True,
                                        "ifaf-is-primary": True
                                    },
                                    "ifa-local": "106.187.14.122"
                                },
                                "intf-curr-cnt": "1",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "75000",
                                "mtu": "1500",
                                "new-hold-limit": "75000"
                            },
                            {
                                "address-family-name": "inet6",
                                "interface-address": [
                                    {
                                        "ifa-destination": "2001:268:fb8f:1f::/64",
                                        "ifa-flags": {
                                            "ifaf-is-preferred": True,
                                            "ifaf-is-primary": True
                                        },
                                        "ifa-local": "2001:268:fb8f:1f::2"
                                    },
                                    {
                                        "ifa-destination": "fe80::/64",
                                        "ifa-flags": {
                                            "ifaf-is-preferred": True
                                        },
                                        "ifa-local": "fe80::250:56ff:fe8d:a96c"
                                    }
                                ],
                                "intf-curr-cnt": "2",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "75000",
                                "mtu": "1500",
                                "new-hold-limit": "75000"
                            },
                            {
                                "address-family-name": "mpls",
                                "maximum-labels": "3",
                                "mtu": "1488"
                            },
                            {
                                "address-family-name": "multiservice",
                                "mtu": "Unlimited"
                            }
                        ],
                        "encapsulation": "ENET2",
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True,
                            "internal-flags": "0x4004000"
                        },
                        "local-index": "334",
                        "name": "ge-0/0/1.0",
                        "snmp-index": "605",
                        "traffic-statistics": {
                            "input-packets": "376821627",
                            "output-packets": "370477594"
                        }
                    },
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/1",
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "snmp-index": "527",
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "traffic-statistics": {
                        "input-bps": "3696",
                        "input-pps": "6",
                        "output-bps": "7736",
                        "output-pps": "9"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "00:50:56:8d:90:2d",
                    "description": "ve-hkgasr01_Gi2[DefaultCost1000]",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "00:50:56:8d:90:2d",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "interface-flapped": {
                        "#text": "2020-03-05 16:04:34 UTC (2w6d 12:00 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "local-index": "150",
                    "logical-interface": {
                        "address-family": [
                            {
                                "address-family-flags": {
                                    "ifff-sendbcast-pkt-to-re": True
                                },
                                "address-family-name": "inet",
                                "interface-address": {
                                    "ifa-broadcast": "27.86.198.27",
                                    "ifa-destination": "27.86.198.24/30",
                                    "ifa-flags": {
                                        "ifaf-is-preferred": True,
                                        "ifaf-is-primary": True
                                    },
                                    "ifa-local": "27.86.198.25"
                                },
                                "intf-curr-cnt": "1",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "75000",
                                "mtu": "1500",
                                "new-hold-limit": "75000"
                            },
                            {
                                "address-family-name": "mpls",
                                "maximum-labels": "3",
                                "mtu": "1488"
                            },
                            {
                                "address-family-name": "multiservice",
                                "mtu": "Unlimited"
                            }
                        ],
                        "encapsulation": "ENET2",
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True,
                            "internal-flags": "0x4004000"
                        },
                        "local-index": "336",
                        "name": "ge-0/0/2.0",
                        "snmp-index": "536",
                        "traffic-statistics": {
                            "input-packets": "210359939",
                            "output-packets": "222589463"
                        }
                    },
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/2",
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "snmp-index": "528",
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "traffic-statistics": {
                        "input-bps": "928",
                        "input-pps": "1",
                        "output-bps": "800",
                        "output-pps": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "00:50:56:8d:06:3e",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "00:50:56:8d:06:3e",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "interface-flapped": {
                        "#text": "2019-10-25 08:50:18 UTC (21w5d 19:15 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "local-index": "151",
                    "logical-interface": {
                        "address-family": [
                            {
                                "address-family-flags": {
                                    "ifff-sendbcast-pkt-to-re": True
                                },
                                "address-family-name": "inet",
                                "interface-address": {
                                    "ifa-broadcast": "100.0.0.255",
                                    "ifa-destination": "100.0.0/24",
                                    "ifa-flags": {
                                        "ifaf-is-preferred": True,
                                        "ifaf-is-primary": True
                                    },
                                    "ifa-local": "100.0.0.254"
                                },
                                "intf-curr-cnt": "1",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "75000",
                                "mtu": "1500",
                                "new-hold-limit": "75000"
                            },
                            {
                                "address-family-name": "multiservice",
                                "mtu": "Unlimited"
                            }
                        ],
                        "encapsulation": "ENET2",
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True,
                            "internal-flags": "0x4004000"
                        },
                        "local-index": "335",
                        "name": "ge-0/0/3.0",
                        "snmp-index": "537",
                        "traffic-statistics": {
                            "input-packets": "0",
                            "output-packets": "0"
                        }
                    },
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/3",
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "snmp-index": "529",
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "traffic-statistics": {
                        "input-bps": "0",
                        "input-pps": "0",
                        "output-bps": "0",
                        "output-pps": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "00:50:56:8d:b0:9a",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "00:50:56:8d:b0:9a",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-hardware-down": True,
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-down": True,
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:20 UTC (29w6d 18:55 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "local-index": "152",
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/4",
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "snmp-index": "530",
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "traffic-statistics": {
                        "input-bps": "0",
                        "input-pps": "0",
                        "output-bps": "0",
                        "output-pps": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "2c:6b:f5:18:e8:05",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "2c:6b:f5:18:e8:05",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-hardware-down": True,
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-down": True,
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:20 UTC (29w6d 18:55 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "local-index": "153",
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/5",
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "snmp-index": "531",
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "traffic-statistics": {
                        "input-bps": "0",
                        "input-pps": "0",
                        "output-bps": "0",
                        "output-pps": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "2c:6b:f5:18:e8:06",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "2c:6b:f5:18:e8:06",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-hardware-down": True,
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-down": True,
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:20 UTC (29w6d 18:55 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "local-index": "154",
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/6",
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "snmp-index": "532",
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "traffic-statistics": {
                        "input-bps": "0",
                        "input-pps": "0",
                        "output-bps": "0",
                        "output-pps": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "2c:6b:f5:18:e8:07",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "2c:6b:f5:18:e8:07",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-hardware-down": True,
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-down": True,
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:20 UTC (29w6d 18:55 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "local-index": "155",
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/7",
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "snmp-index": "533",
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "traffic-statistics": {
                        "input-bps": "0",
                        "input-pps": "0",
                        "output-bps": "0",
                        "output-pps": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "2c:6b:f5:18:e8:08",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "2c:6b:f5:18:e8:08",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-hardware-down": True,
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-down": True,
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:20 UTC (29w6d 18:55 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "local-index": "156",
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/8",
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "snmp-index": "534",
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "traffic-statistics": {
                        "input-bps": "0",
                        "input-pps": "0",
                        "output-bps": "0",
                        "output-pps": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "2c:6b:f5:18:e8:09",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "2c:6b:f5:18:e8:09",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-hardware-down": True,
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-down": True,
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:20 UTC (29w6d 18:55 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "local-index": "157",
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/9",
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "snmp-index": "535",
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "traffic-statistics": {
                        "input-bps": "0",
                        "input-pps": "0",
                        "output-bps": "0",
                        "output-pps": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "2c:6b:f5:18:e8:11",
                    "hardware-physical-address": "2c:6b:f5:18:e8:11",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Ethernet",
                    "link-type": "Full-Duplex",
                    "local-index": "129",
                    "mtu": "9192",
                    "name": "cbp0",
                    "snmp-index": "501"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Full-Duplex",
                    "local-index": "128",
                    "name": "demux0",
                    "snmp-index": "502"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "local-index": "5",
                    "name": "dsc",
                    "snmp-index": "5"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "00:50:56:8d:55:34",
                    "hardware-physical-address": "00:50:56:8d:55:34",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "interface-flapped": {
                        "#text": "2019-08-29 09:03:11 UTC (29w6d 19:02 ago)"
                    },
                    "link-level-type": "Ethernet",
                    "local-index": "65",
                    "logical-interface": {
                        "address-family": [
                            {
                                "address-family-flags": {
                                    "ifff-is-primary": True
                                },
                                "address-family-name": "inet",
                                "interface-address": [
                                    {
                                        "ifa-broadcast": "10.255.255.255",
                                        "ifa-destination": "10/8",
                                        "ifa-flags": {
                                            "ifaf-is-preferred": True
                                        },
                                        "ifa-local": "10.0.0.4"
                                    },
                                    {
                                        "ifa-broadcast": "191.255.255.255",
                                        "ifa-destination": "128/2",
                                        "ifa-flags": {
                                            "ifaf-is-preferred": True,
                                            "ifaf-kernel": True,
                                            "ifaf-preferred": True
                                        },
                                        "ifa-local": "128.0.0.1"
                                    },
                                    {
                                        "ifa-broadcast": "191.255.255.255",
                                        "ifa-destination": "128/2",
                                        "ifa-flags": {
                                            "ifaf-is-default": True,
                                            "ifaf-is-primary": True,
                                            "ifaf-primary": True
                                        },
                                        "ifa-local": "128.0.0.4"
                                    }
                                ],
                                "intf-curr-cnt": "1",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "75000",
                                "mtu": "1500",
                                "new-hold-limit": "75000"
                            },
                            {
                                "address-family-flags": {
                                    "ifff-is-primary": True
                                },
                                "address-family-name": "inet6",
                                "interface-address": [
                                    {
                                        "ifa-destination": "fe80::/64",
                                        "ifa-flags": {
                                            "ifaf-is-preferred": True
                                        },
                                        "ifa-local": "fe80::250:56ff:fe8d:5534"
                                    },
                                    {
                                        "ifa-destination": "fec0::/64",
                                        "ifa-flags": {
                                            "ifaf-is-default": True,
                                            "ifaf-is-preferred": True,
                                            "ifaf-is-primary": True
                                        },
                                        "ifa-local": "0x4"
                                    }
                                ],
                                "intf-curr-cnt": "1",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "75000",
                                "mtu": "1500",
                                "new-hold-limit": "75000"
                            },
                            {
                                "address-family-flags": {
                                    "ifff-is-primary": True,
                                    "ifff-primary": True
                                },
                                "address-family-name": "tnp",
                                "mtu": "1500"
                            }
                        ],
                        "encapsulation": "ENET2",
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True,
                            "internal-flags": "0x4000000"
                        },
                        "local-index": "3",
                        "name": "em1.0",
                        "snmp-index": "24",
                        "traffic-statistics": {
                            "input-packets": "0",
                            "output-packets": "0"
                        }
                    },
                    "mtu": "1514",
                    "name": "em1",
                    "snmp-index": "23"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "VxLAN-Tunnel-Endpoint",
                    "link-type": "Full-Duplex",
                    "local-index": "134",
                    "mtu": "Unlimited",
                    "name": "esi",
                    "snmp-index": "503",
                    "speed": "Unlimited"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Flexible-tunnel-Interface",
                    "link-type": "Full-Duplex",
                    "local-index": "136",
                    "mtu": "Unlimited",
                    "name": "fti0",
                    "snmp-index": "504",
                    "speed": "Unlimited"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Flexible-tunnel-Interface",
                    "link-type": "Full-Duplex",
                    "local-index": "137",
                    "mtu": "Unlimited",
                    "name": "fti1",
                    "snmp-index": "505",
                    "speed": "Unlimited"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Flexible-tunnel-Interface",
                    "link-type": "Full-Duplex",
                    "local-index": "138",
                    "mtu": "Unlimited",
                    "name": "fti2",
                    "snmp-index": "506",
                    "speed": "Unlimited"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Flexible-tunnel-Interface",
                    "link-type": "Full-Duplex",
                    "local-index": "139",
                    "mtu": "Unlimited",
                    "name": "fti3",
                    "snmp-index": "507",
                    "speed": "Unlimited"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Flexible-tunnel-Interface",
                    "link-type": "Full-Duplex",
                    "local-index": "140",
                    "mtu": "Unlimited",
                    "name": "fti4",
                    "snmp-index": "508",
                    "speed": "Unlimited"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Flexible-tunnel-Interface",
                    "link-type": "Full-Duplex",
                    "local-index": "141",
                    "mtu": "Unlimited",
                    "name": "fti5",
                    "snmp-index": "509",
                    "speed": "Unlimited"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Flexible-tunnel-Interface",
                    "link-type": "Full-Duplex",
                    "local-index": "142",
                    "mtu": "Unlimited",
                    "name": "fti6",
                    "snmp-index": "510",
                    "speed": "Unlimited"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Flexible-tunnel-Interface",
                    "link-type": "Full-Duplex",
                    "local-index": "143",
                    "mtu": "Unlimited",
                    "name": "fti7",
                    "snmp-index": "511",
                    "speed": "Unlimited"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "00:50:56:8d:7c:08",
                    "hardware-physical-address": "00:50:56:8d:7c:08",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "interface-flapped": {
                        "#text": "2019-08-29 09:03:11 UTC (29w6d 19:02 ago)"
                    },
                    "link-level-type": "Ethernet",
                    "local-index": "64",
                    "logical-interface": {
                        "address-family": [
                            {
                                "address-family-flags": {
                                    "ifff-is-primary": True,
                                    "ifff-sendbcast-pkt-to-re": True
                                },
                                "address-family-name": "inet",
                                "interface-address": {
                                    "ifa-broadcast": "1.0.0.255",
                                    "ifa-destination": "1.0.0/24",
                                    "ifa-flags": {
                                        "ifaf-is-preferred": True,
                                        "ifaf-is-primary": True
                                    },
                                    "ifa-local": "1.0.0.101"
                                },
                                "intf-curr-cnt": "2",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "75000",
                                "mtu": "1500",
                                "new-hold-limit": "75000"
                            }
                        ],
                        "encapsulation": "ENET2",
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True,
                            "internal-flags": "0x4000000"
                        },
                        "local-index": "4",
                        "name": "fxp0.0",
                        "snmp-index": "13",
                        "traffic-statistics": {
                            "input-packets": "0",
                            "output-packets": "0"
                        }
                    },
                    "mtu": "1514",
                    "name": "fxp0",
                    "snmp-index": "1"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "link-level-type": "GRE",
                    "local-index": "10",
                    "mtu": "Unlimited",
                    "name": "gre",
                    "snmp-index": "8",
                    "speed": "Unlimited"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "link-level-type": "IP-over-IP",
                    "local-index": "11",
                    "mtu": "Unlimited",
                    "name": "ipip",
                    "snmp-index": "9",
                    "speed": "Unlimited"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "2c:6b:f5:18:ef:f0",
                    "hardware-physical-address": "2c:6b:f5:18:ef:f0",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Ethernet",
                    "link-type": "Full-Duplex",
                    "local-index": "132",
                    "mtu": "1514",
                    "name": "irb",
                    "snmp-index": "512"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "2c:6b:f5:18:ef:c0",
                    "hardware-physical-address": "2c:6b:f5:18:ef:c0",
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Ethernet",
                    "link-type": "Full-Duplex",
                    "local-index": "144",
                    "logical-interface": {
                        "address-family": [
                            {
                                "address-family-flags": {
                                    "ifff-is-primary": True
                                },
                                "address-family-name": "inet",
                                "interface-address": {
                                    "ifa-broadcast": "191.255.255.255",
                                    "ifa-destination": "128/2",
                                    "ifa-flags": {
                                        "ifaf-is-default": True,
                                        "ifaf-is-preferred": True,
                                        "ifaf-is-primary": True,
                                        "ifaf-primary": True
                                    },
                                    "ifa-local": "128.0.0.127"
                                },
                                "intf-curr-cnt": "0",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "75000",
                                "mtu": "1514",
                                "new-hold-limit": "75000"
                            }
                        ],
                        "encapsulation": "unknown",
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True,
                            "internal-flags": "0x24004000"
                        },
                        "local-index": "325",
                        "logical-interface-bandwidth": "1Gbps",
                        "name": "jsrv.1",
                        "snmp-index": "514",
                        "traffic-statistics": {
                            "input-packets": "33920578",
                            "output-packets": "33920578"
                        }
                    },
                    "mtu": "1514",
                    "name": "jsrv",
                    "snmp-index": "513"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-loopback": True,
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "local-index": "6",
                    "logical-interface": {
                        "address-family": [
                            {
                                "address-family-flags": {
                                    "ifff-no-redirects": True,
                                    "ifff-sendbcast-pkt-to-re": True
                                },
                                "address-family-name": "inet",
                                "interface-address": {
                                    "ifa-flags": {
                                        "ifaf-is-default": True,
                                        "ifaf-is-primary": True
                                    },
                                    "ifa-local": "111.87.5.252"
                                },
                                "intf-curr-cnt": "0",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "0",
                                "mtu": "Unlimited",
                                "new-hold-limit": "0"
                            },
                            {
                                "address-family-name": "inet6",
                                "interface-address": {
                                    "ifa-flags": {
                                        "ifaf-is-default": True,
                                        "ifaf-is-primary": True
                                    },
                                    "ifa-local": "127.0.0.1"
                                },
                                "intf-curr-cnt": "0",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "0",
                                "mtu": "Unlimited",
                                "new-hold-limit": "0"
                            },
                            {
                                "address-family-name": "inet",
                                "intf-curr-cnt": "0",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "0",
                                "mtu": "Unlimited",
                                "new-hold-limit": "0"
                            },
                            {
                                "address-family-name": "inet",
                                "intf-curr-cnt": "0",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "0",
                                "mtu": "Unlimited",
                                "new-hold-limit": "0"
                            }
                        ],
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True
                        },
                        "local-index": "321",
                        "name": "lo0.16385",
                        "snmp-index": "22",
                        "traffic-statistics": {
                            "input-packets": "0",
                            "output-packets": "0"
                        }
                    },
                    "name": "lo0",
                    "snmp-index": "6"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "LSI",
                    "local-index": "4",
                    "mtu": "Unlimited",
                    "name": "lsi",
                    "snmp-index": "4",
                    "speed": "Unlimited"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "link-level-type": "GRE",
                    "local-index": "66",
                    "mtu": "Unlimited",
                    "name": "mtun",
                    "snmp-index": "12",
                    "speed": "Unlimited"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "link-level-type": "PIM-Decapsulator",
                    "local-index": "26",
                    "mtu": "Unlimited",
                    "name": "pimd",
                    "snmp-index": "11",
                    "speed": "Unlimited"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "link-level-type": "PIM-Encapsulator",
                    "local-index": "25",
                    "mtu": "Unlimited",
                    "name": "pime",
                    "snmp-index": "10",
                    "speed": "Unlimited"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "2c:6b:f5:18:ef:b0",
                    "hardware-physical-address": "2c:6b:f5:18:ef:b0",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Ethernet",
                    "link-type": "Full-Duplex",
                    "local-index": "130",
                    "mtu": "9192",
                    "name": "pip0",
                    "snmp-index": "515"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "link-level-type": "PPPoE",
                    "link-type": "Full-Duplex",
                    "local-index": "131",
                    "mtu": "1532",
                    "name": "pp0",
                    "snmp-index": "516"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Remote-BEB",
                    "link-type": "Full-Duplex",
                    "local-index": "135",
                    "mtu": "Unlimited",
                    "name": "rbeb",
                    "snmp-index": "517",
                    "speed": "Unlimited"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Interface-Specific",
                    "local-index": "12",
                    "mtu": "Unlimited",
                    "name": "tap",
                    "snmp-index": "7",
                    "speed": "Unlimited"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "VxLAN-Tunnel-Endpoint",
                    "link-type": "Full-Duplex",
                    "local-index": "133",
                    "mtu": "Unlimited",
                    "name": "vtep",
                    "snmp-index": "518",
                    "speed": "Unlimited"
                }
            ]
        }
    }

    golden_output = {'execute.return_value': '''
        show interfaces
        Physical interface: ge-0/0/0, Enabled, Physical link is Up
        Interface index: 148, SNMP ifIndex: 526
        Description: none/100G/in/hktGCS002_ge-0/0/0
        Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        Pad to minimum frame size: Disabled
        Device flags   : Present Running
        Interface flags: SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: 00:50:56:8d:c8:29, Hardware address: 00:50:56:8d:c8:29
        Last flapped   : 2019-08-29 09:09:19 UTC (29w6d 18:56 ago)
        Input rate     : 2952 bps (5 pps)
        Output rate    : 3080 bps (3 pps)
        Active alarms  : None
        Active defects : None
        PCS statistics                      Seconds
            Bit errors                             0
            Errored blocks                         0
        Ethernet FEC statistics              Errors
            FEC Corrected Errors                    0
            FEC Uncorrected Errors                  0
            FEC Corrected Errors Rate               0
            FEC Uncorrected Errors Rate             0
        Interface transmit statistics: Disabled

        Logical interface ge-0/0/0.0 (Index 333) (SNMP ifIndex 606)
            Flags: Up SNMP-Traps 0x4004000 Encapsulation: ENET2
            Input packets : 133657033
            Output packets: 129243982
            Protocol inet, MTU: 1500
            Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: No-Redirects, Sendbcast-pkt-to-re
            Addresses, Flags: Is-Preferred Is-Primary
                Destination: 111.87.5.92/30, Local: 111.87.5.93, Broadcast: 111.87.5.95
            Protocol inet6, MTU: 1500
            Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: Is-Primary
            Addresses, Flags: Is-Preferred Is-Primary
                Destination: 2001:268:fb90:14::/64, Local: 2001:268:fb90:14::1
            Addresses, Flags: Is-Preferred
                Destination: fe80::/64, Local: fe80::250:56ff:fe8d:c829
            Protocol mpls, MTU: 1488, Maximum labels: 3
            Flags: Is-Primary
            Protocol multiservice, MTU: Unlimited
            Flags: Is-Primary

        Physical interface: lc-0/0/0, Enabled, Physical link is Up
        Interface index: 145, SNMP ifIndex: 519
        Speed: 800mbps
        Device flags   : Present Running
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Logical interface lc-0/0/0.32769 (Index 329) (SNMP ifIndex 520)
            Flags: Up Encapsulation: ENET2
            Bandwidth: 0
            Input packets : 0
            Output packets: 0
            Protocol vpls, MTU: Unlimited
            Flags: Is-Primary

        Physical interface: pfe-0/0/0, Enabled, Physical link is Up
        Interface index: 147, SNMP ifIndex: 522
        Speed: 800mbps
        Device flags   : Present Running
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Logical interface pfe-0/0/0.16383 (Index 330) (SNMP ifIndex 523)
            Flags: Up SNMP-Traps Encapsulation: ENET2
            Bandwidth: 0
            Input packets : 0
            Output packets: 0
            Protocol inet, MTU: Unlimited
            Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: None
            Protocol inet6, MTU: Unlimited
            Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: None

        Physical interface: pfh-0/0/0, Enabled, Physical link is Up
        Interface index: 146, SNMP ifIndex: 521
        Speed: 800mbps
        Device flags   : Present Running
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Logical interface pfh-0/0/0.16383 (Index 331) (SNMP ifIndex 524)
            Flags: Up SNMP-Traps Encapsulation: ENET2
            Bandwidth: 0
            Input packets : 0
            Output packets: 0
            Protocol inet, MTU: Unlimited
            Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: None

        Logical interface pfh-0/0/0.16384 (Index 332) (SNMP ifIndex 525)
            Flags: Up SNMP-Traps Encapsulation: ENET2
            Bandwidth: 0
            Input packets : 0
            Output packets: 0
            Protocol inet, MTU: Unlimited
            Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: Is-Primary

        Physical interface: ge-0/0/1, Enabled, Physical link is Up
        Interface index: 149, SNMP ifIndex: 527
        Description: YW7079/9.6G/BB/sjkGCS001-EC11_xe-0/1/5[SJC]_Area8_Cost100
        Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        Pad to minimum frame size: Disabled
        Device flags   : Present Running
        Interface flags: SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: 00:50:56:8d:a9:6c, Hardware address: 00:50:56:8d:a9:6c
        Last flapped   : 2019-08-29 09:09:19 UTC (29w6d 18:56 ago)
        Input rate     : 3696 bps (6 pps)
        Output rate    : 7736 bps (9 pps)
        Active alarms  : None
        Active defects : None
        PCS statistics                      Seconds
            Bit errors                             0
            Errored blocks                         0
        Ethernet FEC statistics              Errors
            FEC Corrected Errors                    0
            FEC Uncorrected Errors                  0
            FEC Corrected Errors Rate               0
            FEC Uncorrected Errors Rate             0
        Interface transmit statistics: Disabled

        Logical interface ge-0/0/1.0 (Index 334) (SNMP ifIndex 605)
            Flags: Up SNMP-Traps 0x4004000 Encapsulation: ENET2
            Input packets : 376821627
            Output packets: 370477594
            Protocol inet, MTU: 1500
            Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: No-Redirects, Sendbcast-pkt-to-re
            Addresses, Flags: Is-Preferred Is-Primary
                Destination: 106.187.14.120/30, Local: 106.187.14.122, Broadcast: 106.187.14.123
            Protocol inet6, MTU: 1500
            Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 2, Curr new hold cnt: 0, NH drop cnt: 0
            Addresses, Flags: Is-Preferred Is-Primary
                Destination: 2001:268:fb8f:1f::/64, Local: 2001:268:fb8f:1f::2
            Addresses, Flags: Is-Preferred
                Destination: fe80::/64, Local: fe80::250:56ff:fe8d:a96c
            Protocol mpls, MTU: 1488, Maximum labels: 3
            Protocol multiservice, MTU: Unlimited

        Physical interface: ge-0/0/2, Enabled, Physical link is Up
        Interface index: 150, SNMP ifIndex: 528
        Description: ve-hkgasr01_Gi2[DefaultCost1000]
        Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        Pad to minimum frame size: Disabled
        Device flags   : Present Running
        Interface flags: SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: 00:50:56:8d:90:2d, Hardware address: 00:50:56:8d:90:2d
        Last flapped   : 2020-03-05 16:04:34 UTC (2w6d 12:00 ago)
        Input rate     : 928 bps (1 pps)
        Output rate    : 800 bps (0 pps)
        Active alarms  : None
        Active defects : None
        PCS statistics                      Seconds
            Bit errors                             0
            Errored blocks                         0
        Ethernet FEC statistics              Errors
            FEC Corrected Errors                    0
            FEC Uncorrected Errors                  0
            FEC Corrected Errors Rate               0
            FEC Uncorrected Errors Rate             0
        Interface transmit statistics: Disabled

        Logical interface ge-0/0/2.0 (Index 336) (SNMP ifIndex 536)
            Flags: Up SNMP-Traps 0x4004000 Encapsulation: ENET2
            Input packets : 210359939
            Output packets: 222589463
            Protocol inet, MTU: 1500
            Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: Sendbcast-pkt-to-re
            Addresses, Flags: Is-Preferred Is-Primary
                Destination: 27.86.198.24/30, Local: 27.86.198.25, Broadcast: 27.86.198.27
            Protocol mpls, MTU: 1488, Maximum labels: 3
            Protocol multiservice, MTU: Unlimited

        Physical interface: ge-0/0/3, Enabled, Physical link is Up
        Interface index: 151, SNMP ifIndex: 529
        Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        Pad to minimum frame size: Disabled
        Device flags   : Present Running
        Interface flags: SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: 00:50:56:8d:06:3e, Hardware address: 00:50:56:8d:06:3e
        Last flapped   : 2019-10-25 08:50:18 UTC (21w5d 19:15 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Active alarms  : None
        Active defects : None
        PCS statistics                      Seconds
            Bit errors                             0
            Errored blocks                         0
        Ethernet FEC statistics              Errors
            FEC Corrected Errors                    0
            FEC Uncorrected Errors                  0
            FEC Corrected Errors Rate               0
            FEC Uncorrected Errors Rate             0
        Interface transmit statistics: Disabled

        Logical interface ge-0/0/3.0 (Index 335) (SNMP ifIndex 537)
            Flags: Up SNMP-Traps 0x4004000 Encapsulation: ENET2
            Input packets : 14609
            Output packets: 17416
            Protocol inet, MTU: 1500
            Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: Sendbcast-pkt-to-re
            Addresses, Flags: Is-Preferred Is-Primary
                Destination: 100.0.0/24, Local: 100.0.0.254, Broadcast: 100.0.0.255
            Protocol multiservice, MTU: Unlimited

        Physical interface: ge-0/0/4, Enabled, Physical link is Down
        Interface index: 152, SNMP ifIndex: 530
        Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        Pad to minimum frame size: Disabled
        Device flags   : Present Running Down
        Interface flags: Hardware-Down SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: 00:50:56:8d:b0:9a, Hardware address: 00:50:56:8d:b0:9a
        Last flapped   : 2019-08-29 09:09:20 UTC (29w6d 18:55 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Active alarms  : LINK
        Active defects : LINK
        PCS statistics                      Seconds
            Bit errors                             0
            Errored blocks                         0
        Ethernet FEC statistics              Errors
            FEC Corrected Errors                    0
            FEC Uncorrected Errors                  0
            FEC Corrected Errors Rate               0
            FEC Uncorrected Errors Rate             0
        Interface transmit statistics: Disabled

        Physical interface: ge-0/0/5, Enabled, Physical link is Down
        Interface index: 153, SNMP ifIndex: 531
        Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        Pad to minimum frame size: Disabled
        Device flags   : Present Running Down
        Interface flags: Hardware-Down SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: 2c:6b:f5:18:e8:05, Hardware address: 2c:6b:f5:18:e8:05
        Last flapped   : 2019-08-29 09:09:20 UTC (29w6d 18:55 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Active alarms  : LINK
        Active defects : LINK
        PCS statistics                      Seconds
            Bit errors                             0
            Errored blocks                         0
        Ethernet FEC statistics              Errors
            FEC Corrected Errors                    0
            FEC Uncorrected Errors                  0
            FEC Corrected Errors Rate               0
            FEC Uncorrected Errors Rate             0
        Interface transmit statistics: Disabled

        Physical interface: ge-0/0/6, Enabled, Physical link is Down
        Interface index: 154, SNMP ifIndex: 532
        Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        Pad to minimum frame size: Disabled
        Device flags   : Present Running Down
        Interface flags: Hardware-Down SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: 2c:6b:f5:18:e8:06, Hardware address: 2c:6b:f5:18:e8:06
        Last flapped   : 2019-08-29 09:09:20 UTC (29w6d 18:55 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Active alarms  : LINK
        Active defects : LINK
        PCS statistics                      Seconds
            Bit errors                             0
            Errored blocks                         0
        Ethernet FEC statistics              Errors
            FEC Corrected Errors                    0
            FEC Uncorrected Errors                  0
            FEC Corrected Errors Rate               0
            FEC Uncorrected Errors Rate             0
        Interface transmit statistics: Disabled

        Physical interface: ge-0/0/7, Enabled, Physical link is Down
        Interface index: 155, SNMP ifIndex: 533
        Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        Pad to minimum frame size: Disabled
        Device flags   : Present Running Down
        Interface flags: Hardware-Down SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: 2c:6b:f5:18:e8:07, Hardware address: 2c:6b:f5:18:e8:07
        Last flapped   : 2019-08-29 09:09:20 UTC (29w6d 18:55 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Active alarms  : LINK
        Active defects : LINK
        PCS statistics                      Seconds
            Bit errors                             0
            Errored blocks                         0
        Ethernet FEC statistics              Errors
            FEC Corrected Errors                    0
            FEC Uncorrected Errors                  0
            FEC Corrected Errors Rate               0
            FEC Uncorrected Errors Rate             0
        Interface transmit statistics: Disabled

        Physical interface: ge-0/0/8, Enabled, Physical link is Down
        Interface index: 156, SNMP ifIndex: 534
        Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        Pad to minimum frame size: Disabled
        Device flags   : Present Running Down
        Interface flags: Hardware-Down SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: 2c:6b:f5:18:e8:08, Hardware address: 2c:6b:f5:18:e8:08
        Last flapped   : 2019-08-29 09:09:20 UTC (29w6d 18:55 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Active alarms  : LINK
        Active defects : LINK
        PCS statistics                      Seconds
            Bit errors                             0
            Errored blocks                         0
        Ethernet FEC statistics              Errors
            FEC Corrected Errors                    0
            FEC Uncorrected Errors                  0
            FEC Corrected Errors Rate               0
            FEC Uncorrected Errors Rate             0
        Interface transmit statistics: Disabled

        Physical interface: ge-0/0/9, Enabled, Physical link is Down
        Interface index: 157, SNMP ifIndex: 535
        Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        Pad to minimum frame size: Disabled
        Device flags   : Present Running Down
        Interface flags: Hardware-Down SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: 2c:6b:f5:18:e8:09, Hardware address: 2c:6b:f5:18:e8:09
        Last flapped   : 2019-08-29 09:09:20 UTC (29w6d 18:55 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Active alarms  : LINK
        Active defects : LINK
        PCS statistics                      Seconds
            Bit errors                             0
            Errored blocks                         0
        Ethernet FEC statistics              Errors
            FEC Corrected Errors                    0
            FEC Uncorrected Errors                  0
            FEC Corrected Errors Rate               0
            FEC Uncorrected Errors Rate             0
        Interface transmit statistics: Disabled

        Physical interface: cbp0, Enabled, Physical link is Up
        Interface index: 129, SNMP ifIndex: 501
        Type: Ethernet, Link-level type: Ethernet, MTU: 9192
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Current address: 2c:6b:f5:18:e8:11, Hardware address: 2c:6b:f5:18:e8:11
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: demux0, Enabled, Physical link is Up
        Interface index: 128, SNMP ifIndex: 502
        Type: Software-Pseudo, MTU: 9192, Clocking: 1
        Device flags   : Present Running
        Interface flags: Point-To-Point SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: dsc, Enabled, Physical link is Up
        Interface index: 5, SNMP ifIndex: 5
        Type: Software-Pseudo, MTU: Unlimited
        Device flags   : Present Running
        Interface flags: Point-To-Point SNMP-Traps
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: em1, Enabled, Physical link is Up
        Interface index: 65, SNMP ifIndex: 23
        Type: Ethernet, Link-level type: Ethernet, MTU: 1514
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Current address: 00:50:56:8d:55:34, Hardware address: 00:50:56:8d:55:34
        Last flapped   : 2019-08-29 09:03:11 UTC (29w6d 19:02 ago)
            Input packets : 0
            Output packets: 0

        Logical interface em1.0 (Index 3) (SNMP ifIndex 24)
            Flags: Up SNMP-Traps 0x4000000 Encapsulation: ENET2
            Input packets : 724625563
            Output packets: 793953088
            Protocol inet, MTU: 1500
            Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: Is-Primary
            Addresses, Flags: Is-Preferred
                Destination: 10/8, Local: 10.0.0.4, Broadcast: 10.255.255.255
            Addresses, Flags: Preferred Kernel Is-Preferred
                Destination: 128/2, Local: 128.0.0.1, Broadcast: 191.255.255.255
            Addresses, Flags: Primary Is-Default Is-Primary
                Destination: 128/2, Local: 128.0.0.4, Broadcast: 191.255.255.255
            Protocol inet6, MTU: 1500
            Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: Is-Primary
            Addresses, Flags: Is-Preferred
                Destination: fe80::/64, Local: fe80::250:56ff:fe8d:5534
            Addresses, Flags: Is-Default Is-Preferred Is-Primary
                Destination: fec0::/64, Local: fec0::a:0:0:4
            Protocol tnp, MTU: 1500
            Flags: Primary, Is-Primary
            Addresses
                Local: 0x4

        Physical interface: esi, Enabled, Physical link is Up
        Interface index: 134, SNMP ifIndex: 503
        Type: Software-Pseudo, Link-level type: VxLAN-Tunnel-Endpoint, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: fti0, Enabled, Physical link is Up
        Interface index: 136, SNMP ifIndex: 504
        Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: fti1, Enabled, Physical link is Up
        Interface index: 137, SNMP ifIndex: 505
        Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: fti2, Enabled, Physical link is Up
        Interface index: 138, SNMP ifIndex: 506
        Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: fti3, Enabled, Physical link is Up
        Interface index: 139, SNMP ifIndex: 507
        Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: fti4, Enabled, Physical link is Up
        Interface index: 140, SNMP ifIndex: 508
        Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: fti5, Enabled, Physical link is Up
        Interface index: 141, SNMP ifIndex: 509
        Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: fti6, Enabled, Physical link is Up
        Interface index: 142, SNMP ifIndex: 510
        Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: fti7, Enabled, Physical link is Up
        Interface index: 143, SNMP ifIndex: 511
        Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: fxp0, Enabled, Physical link is Up
        Interface index: 64, SNMP ifIndex: 1
        Type: Ethernet, Link-level type: Ethernet, MTU: 1514
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Current address: 00:50:56:8d:7c:08, Hardware address: 00:50:56:8d:7c:08
        Last flapped   : 2019-08-29 09:03:11 UTC (29w6d 19:02 ago)
            Input packets : 0
            Output packets: 0

        Logical interface fxp0.0 (Index 4) (SNMP ifIndex 13)
            Flags: Up SNMP-Traps 0x4000000 Encapsulation: ENET2
            Input packets : 563129
            Output packets: 805208
            Protocol inet, MTU: 1500
            Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 2, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: Sendbcast-pkt-to-re, Is-Primary
            Addresses, Flags: Is-Preferred Is-Primary
                Destination: 1.0.0/24, Local: 1.0.0.101, Broadcast: 1.0.0.255

        Physical interface: gre, Enabled, Physical link is Up
        Interface index: 10, SNMP ifIndex: 8
        Type: GRE, Link-level type: GRE, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: Point-To-Point SNMP-Traps
            Input packets : 0
            Output packets: 0

        Physical interface: ipip, Enabled, Physical link is Up
        Interface index: 11, SNMP ifIndex: 9
        Type: IPIP, Link-level type: IP-over-IP, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
            Input packets : 0
            Output packets: 0

        Physical interface: irb, Enabled, Physical link is Up
        Interface index: 132, SNMP ifIndex: 512
        Type: Ethernet, Link-level type: Ethernet, MTU: 1514
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Current address: 2c:6b:f5:18:ef:f0, Hardware address: 2c:6b:f5:18:ef:f0
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: jsrv, Enabled, Physical link is Up
        Interface index: 144, SNMP ifIndex: 513
        Type: Ethernet, Link-level type: Ethernet, MTU: 1514
        Device flags   : Present Running
        Link type      : Full-Duplex
        Link flags     : None
        Current address: 2c:6b:f5:18:ef:c0, Hardware address: 2c:6b:f5:18:ef:c0
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Logical interface jsrv.1 (Index 325) (SNMP ifIndex 514)
            Flags: Up 0x24004000 Encapsulation: unknown
            Bandwidth: 1Gbps
            Routing Instance: None Bridging Domain: None
            Input packets : 0
            Output packets: 0
            Protocol inet, MTU: 1514
            Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: Is-Primary
            Addresses, Flags: Primary Is-Default Is-Preferred Is-Primary
                Destination: 128/2, Local: 128.0.0.127, Broadcast: 191.255.255.255

        Physical interface: lo0, Enabled, Physical link is Up
        Interface index: 6, SNMP ifIndex: 6
        Type: Loopback, MTU: Unlimited
        Device flags   : Present Running Loopback
        Interface flags: SNMP-Traps
        Link flags     : None
        Last flapped   : Never
            Input packets : 33920578
            Output packets: 33920578

        Logical interface lo0.0 (Index 320) (SNMP ifIndex 16)
            Flags: SNMP-Traps Encapsulation: Unspecified
            Input packets : 83
            Output packets: 83
            Protocol inet, MTU: Unlimited
            Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: No-Redirects, Sendbcast-pkt-to-re
            Addresses, Flags: Is-Default Is-Primary
                Local: 111.87.5.252
            Protocol inet6, MTU: Unlimited
            Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
            Addresses, Flags: Is-Default Is-Primary
                Local: 2001:268:fb90::b
                Local: fe80::250:560f:fc8d:7c08

        Logical interface lo0.16384 (Index 322) (SNMP ifIndex 21)
            Flags: SNMP-Traps Encapsulation: Unspecified
            Input packets : 0
            Output packets: 0
            Protocol inet, MTU: Unlimited
            Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
            Addresses
                Local: 127.0.0.1

        Logical interface lo0.16385 (Index 321) (SNMP ifIndex 22)
            Flags: SNMP-Traps Encapsulation: Unspecified
            Input packets : 33920495
            Output packets: 33920495
            Protocol inet, MTU: Unlimited
            Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0

        Physical interface: lsi, Enabled, Physical link is Up
        Interface index: 4, SNMP ifIndex: 4
        Type: Software-Pseudo, Link-level type: LSI, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: mtun, Enabled, Physical link is Up
        Interface index: 66, SNMP ifIndex: 12
        Type: Multicast-GRE, Link-level type: GRE, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
            Input packets : 0
            Output packets: 0

        Physical interface: pimd, Enabled, Physical link is Up
        Interface index: 26, SNMP ifIndex: 11
        Type: PIMD, Link-level type: PIM-Decapsulator, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
            Input packets : 0
            Output packets: 0

        Physical interface: pime, Enabled, Physical link is Up
        Interface index: 25, SNMP ifIndex: 10
        Type: PIME, Link-level type: PIM-Encapsulator, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
            Input packets : 0
            Output packets: 0

        Physical interface: pip0, Enabled, Physical link is Up
        Interface index: 130, SNMP ifIndex: 515
        Type: Ethernet, Link-level type: Ethernet, MTU: 9192
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Current address: 2c:6b:f5:18:ef:b0, Hardware address: 2c:6b:f5:18:ef:b0
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: pp0, Enabled, Physical link is Up
        Interface index: 131, SNMP ifIndex: 516
        Type: PPPoE, Link-level type: PPPoE, MTU: 1532
        Device flags   : Present Running
        Interface flags: Point-To-Point SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None

        Physical interface: rbeb, Enabled, Physical link is Up
        Interface index: 135, SNMP ifIndex: 517
        Type: Software-Pseudo, Link-level type: Remote-BEB, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: tap, Enabled, Physical link is Up
        Interface index: 12, SNMP ifIndex: 7
        Type: Software-Pseudo, Link-level type: Interface-Specific, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: vtep, Enabled, Physical link is Up
        Interface index: 133, SNMP ifIndex: 518
        Type: Software-Pseudo, Link-level type: VxLAN-Tunnel-Endpoint, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_obj = ShowInterfaces(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowInterfaces(device=self.device)
        parsed_output = interface_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()

# vim: ft=python et sw=4