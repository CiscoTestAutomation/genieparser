#!/bin/env python

import unittest
from unittest.mock import Mock

import xml.etree.ElementTree as ET

from pyats.topology import Device

from genie.ops.base import Context

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.slxos.show_run import ShowRunBridgeDomain, \
                                             ShowRunMacAccessList


class test_show_run_bridge_domain_yang(unittest.TestCase):

    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    golden_parsed_output = {
      "bridge-domains": {
            20: {
                "bpdu-drop-enable": True,
                "bridge-domain-id": 20,
                "bridge-domain-type": "p2mp",
                "local-switching": True,
                "logical-interfaces": {
                    "ethernet": {
                        "0/30.1": {"lif-bind-id": "Ethernet 0/30.1"},
                        "0/30.2": {"lif-bind-id": "Ethernet 0/30.2"},
                    },
                    "port-channel": {
                        "100.1": {"pc-lif-bind-id": "Port-channel 100.1"},
                        "100.2": {"pc-lif-bind-id": "Port-channel 100.2"},
                    },
                },
                "mac-address": {"withdrawal": True},
                "peers": {
                    "1.1.1.1": {
                        "lsps": {
                            "abc": {"lsp-name": "abc"},
                            "def": {"lsp-name": "def"},
                            "ed": {"lsp-name": "ed"},
                        },
                        "peer-ip": "1.1.1.1",
                    },
                    "3.3.3.3": {
                        "lsps": {
                            "1": {"lsp-name": "1"},
                            "abc": {"lsp-name": "abc"},
                            "cos": {"lsp-name": "cos"},
                        },
                        "peer-ip": "3.3.3.3",
                    },
                    "4.4.4.4": {
                        "control-word": True,
                        "cos": 4,
                        "flow-label": True,
                        "load-balance": True,
                        "lsps": {
                          "abc": {"lsp-name": "abc"},
                          "ds": {"lsp-name": "ds"}
                        },
                        "peer-ip": "4.4.4.4",
                    },
                },
                "pw-profile-name": "default",
                "statistics": True,
                "suppress-arp": {"suppress-arp-enable": True},
                "suppress-nd": {"suppress-nd-enable": True},
                "vc-id-num": 20,
            },
            30: {
                "bridge-domain-id": 30,
                "bridge-domain-type": "p2p",
                "logical-interfaces": {
                    "ethernet": {},
                    "port-channel": {
                      "1.300": {
                        "pc-lif-bind-id": "Port-channel 1.300"
                      }
                    },
                },
                "peers": {
                    "100.1.234.6": {
                        "control-word": True,
                        "cos": 1,
                        "flow-label": True,
                        "load-balance": True,
                        "peer-ip": "100.1.234.6",
                    }
                },
                "pw-profile-name": "class-fat",
                "vc-id-num": 20030,
            },
            40: {
                "bpdu-drop-enable": True,
                "bridge-domain-id": 40,
                "bridge-domain-type": "p2mp",
                "description": "test",
                "local-switching": True,
                "mac-address": {"withdrawal": True},
                "pw-profile-name": "default",
                "statistics": True,
            },
        }
    }

    class etree_holder():
        def __init__(self):
            self.data = ET.fromstring('''
            <data>
              <bridge-domain xmlns="urn:brocade.com:mgmt:brocade-bridge-domain">
                <bridge-domain-id>20</bridge-domain-id>
                <bridge-domain-type>p2mp</bridge-domain-type>
                <vc-id-num>20</vc-id-num>
                <peer>
                  <peer-ip>1.1.1.1</peer-ip>
                  <lsp>abc</lsp>
                  <lsp>def</lsp>
                  <lsp>ed</lsp>
                </peer>
                <peer>
                  <peer-ip>3.3.3.3</peer-ip>
                  <lsp>1</lsp>
                  <lsp>abc</lsp>
                  <lsp>cos</lsp>
                </peer>
                <peer>
                  <peer-ip>4.4.4.4</peer-ip>
                  <load-balance/>
                  <cos>4</cos>
                  <flow-label/>
                  <control-word/>
                  <lsp>abc</lsp>
                  <lsp>ds</lsp>
                </peer>
                <statistics/>
                <pw-profile-name>default</pw-profile-name>
                <logical-interface>
                  <ethernet>
                    <lif-bind-id>0/30.1</lif-bind-id>
                  </ethernet>
                  <ethernet>
                    <lif-bind-id>0/30.2</lif-bind-id>
                  </ethernet>
                  <port-channel>
                    <pc-lif-bind-id>100.1</pc-lif-bind-id>
                  </port-channel>
                  <port-channel>
                    <pc-lif-bind-id>100.2</pc-lif-bind-id>
                  </port-channel>
                </logical-interface>
                <bpdu-drop-enable/>
                <local-switching/>
                <mac-address>
                  <withdrawal/>
                </mac-address>
                <suppress-arp xmlns="urn:brocade.com:mgmt:brocade-arp">
                  <suppress-arp-enable/>
                </suppress-arp>
                <suppress-nd xmlns="urn:brocade.com:mgmt:brocade-ipv6-nd-ra">
                  <suppress-nd-enable/>
                </suppress-nd>
                <ip>
                  <arp-node-config xmlns="urn:brocade.com:mgmt:brocade-dai">
                    <arp>
                      <inspection>
                        <trust/>
                        <filter>
                          <acl-name>abc</acl-name>
                        </filter>
                      </inspection>
                    </arp>
                  </arp-node-config>
                  <bd-ip-igmp xmlns="urn:brocade.com:mgmt:brocade-igmp-snooping">
                    <snooping>
                      <igmps-enable/>
                    </snooping>
                  </bd-ip-igmp>
                </ip>
              </bridge-domain>
              <bridge-domain xmlns="urn:brocade.com:mgmt:brocade-bridge-domain">
                <bridge-domain-id>30</bridge-domain-id>
                <bridge-domain-type>p2p</bridge-domain-type>
                <vc-id-num>20030</vc-id-num>
                <peer>
                  <peer-ip>100.1.234.6</peer-ip>
                  <load-balance/>
                  <cos>1</cos>
                  <flow-label/>
                  <control-word/>
                </peer>
                <pw-profile-name>class-fat</pw-profile-name>
                <logical-interface>
                  <port-channel>
                    <pc-lif-bind-id>1.300</pc-lif-bind-id>
                  </port-channel>
                </logical-interface>
              </bridge-domain>
              <bridge-domain xmlns="urn:brocade.com:mgmt:brocade-bridge-domain">
                <bridge-domain-id>40</bridge-domain-id>
                <bridge-domain-type>p2mp</bridge-domain-type>
                <description>test</description>
                <statistics/>
                <pw-profile-name>default</pw-profile-name>
                <bpdu-drop-enable/>
                <local-switching/>
                <mac-address>
                  <withdrawal/>
                </mac-address>
              </bridge-domain>
            </data>
            ''')
    golden_output = {'get.return_value': etree_holder()}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        intf_obj = ShowRunBridgeDomain(device=self.device)
        intf_obj.context = Context.yang.value.split()
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    empty_parsed_output = {'bridge-domains': {}}

    class empty_etree_holder():
        def __init__(self):
            self.data = ET.fromstring('''<data/>''')
    empty_output = {'get.return_value': empty_etree_holder()}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        intf_obj = ShowRunBridgeDomain(device=self.device1)
        intf_obj.context = Context.yang.value.split()
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output, self.empty_parsed_output)


class test_show_run_bridge_domain_yang(unittest.TestCase):

    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    golden_parsed_output = {
        "mac": {
            "access-list": {
                "extended": {
                    "test-2": {
                        "name": "test-2",
                        "seqs": {
                            10: {
                                "action": "permit",
                                "dst": "any",
                                "ethertype": "arp",
                                "seq-id": 10,
                                "source": "host",
                                "srchost": "e481.84a5.e47e",
                                "vlan": "10",
                                "vlan-tag-format": "single-tagged",
                            },
                            11: {
                                "action": "permit",
                                "dst": "any",
                                "ethertype": "ipv4",
                                "seq-id": 11,
                                "source": "bbbb.bbbb.bbb0",
                                "src-mac-addr-mask": "ffff.ffff.fff0",
                                "vlan": "10",
                                "vlan-tag-format": "single-tagged",
                            },
                            12: {
                                "action": "deny",
                                "dst": "host",
                                "dsthost": "cccc.cccc.ccc0",
                                "ethertype": "ipv6",
                                "seq-id": 12,
                                "source": "any",
                                "vlan": "30",
                                "vlan-tag-format": "single-tagged",
                            },
                            13: {
                                "action": "hard-drop",
                                "dst": "cccc.cccc.cc00",
                                "dst-mac-addr-mask": "ffff.ffff.ff00",
                                "ethertype": "ipv6",
                                "seq-id": 13,
                                "source": "any",
                                "vlan": "30",
                                "vlan-tag-format": "single-tagged",
                            },
                            100: {
                                "action": "deny",
                                "dst": "any",
                                "seq-id": 100,
                                "source": "any",
                            },
                        },
                    },
                    "test3": {
                        "name": "test3",
                        "seqs": {
                            103: {
                                "action": "permit",
                                "dst": "any",
                                "ethertype": "arp",
                                "inner-vlan": "1234",
                                "outer-vlan": "200",
                                "seq-id": 103,
                                "source": "host",
                                "srchost": "abcd.abcd.abcd",
                                "vlan-tag-format": "double-tagged",
                            },
                            104: {
                                "action": "permit",
                                "dst": "any",
                                "ethertype": "ipv4",
                                "inner-vlan": "200",
                                "outer-vlan": "1234",
                                "seq-id": 104,
                                "source": "host",
                                "srchost": "abcd.abcd.abcd",
                                "vlan-tag-format": "double-tagged",
                            },
                            105: {
                                "action": "permit",
                                "dst": "any",
                                "ethertype": "ipv6",
                                "inner-vlan": "10",
                                "outer-vlan": "10",
                                "seq-id": 105,
                                "source": "host",
                                "srchost": "abcd.abcd.abcd",
                                "vlan-tag-format": "double-tagged",
                            },
                            110: {
                                "action": "permit",
                                "dst": "any",
                                "ethertype": "arp",
                                "seq-id": 110,
                                "source": "host",
                                "srchost": "abcd.abcd.abcd",
                                "vlan": "321",
                                "vlan-tag-format": "single-tagged",
                            },
                            111: {
                                "action": "permit",
                                "dst": "any",
                                "ethertype": "ipv4",
                                "seq-id": 111,
                                "source": "host",
                                "srchost": "abcd.abcd.abcd",
                                "vlan": "321",
                                "vlan-tag-format": "single-tagged",
                            },
                            112: {
                                "action": "permit",
                                "dst": "any",
                                "ethertype": "ipv6",
                                "seq-id": 112,
                                "source": "host",
                                "srchost": "abcd.abcd.abcd",
                                "vlan": "321",
                                "vlan-tag-format": "single-tagged",
                            },
                            200: {
                                "action": "permit",
                                "count": True,
                                "drop-precedence-force": 2,
                                "dst": "any",
                                "log": True,
                                "mirror": True,
                                "pcp": 1,
                                "pcp-force": 3,
                                "seq-id": 200,
                                "source": "host",
                                "srchost": "abcd.abcd.abcd",
                                "vlan": "10",
                                "vlan-tag-format": "single-tagged",
                            },
                            210: {
                                "action": "permit",
                                "dst": "any",
                                "seq-id": 210,
                                "source": "host",
                                "srchost": "abcd.abcd.abcd",
                                "vlan": "10",
                                "vlan-id-mask": "0xfff",
                                "vlan-tag-format": "single-tagged",
                            },
                            211: {
                                "action": "permit",
                                "dst": "any",
                                "ethertype": "arp",
                                "seq-id": 211,
                                "source": "host",
                                "srchost": "abcd.abcd.abcd",
                                "vlan": "10",
                                "vlan-id-mask": "0xfff",
                                "vlan-tag-format": "single-tagged",
                            },
                            610: {
                                "action": "permit",
                                "dst": "any",
                                "seq-id": 610,
                                "source": "host",
                                "srchost": "abcd.abcd.abcd",
                                "vlan": "10",
                                "vlan-tag-format": "single-tagged",
                            },
                            700: {
                                "action": "permit",
                                "drop-precedence-force": 1,
                                "dst": "any",
                                "seq-id": 700,
                                "source": "host",
                                "srchost": "abcd.abcd.abcd",
                                "vlan": "10",
                                "vlan-tag-format": "single-tagged",
                            },
                            800: {
                                "action": "permit",
                                "dst": "any",
                                "seq-id": 800,
                                "source": "host",
                                "srchost": "abcd.abcd.abcd",
                                "vlan": "1111",
                            },
                            801: {
                                "action": "permit",
                                "dst": "any",
                                "seq-id": 801,
                                "source": "host",
                                "srchost": "abcd.abcd.abcd",
                                "unknown-unicast-only": True,
                                "vlan": "1111",
                            },
                            802: {
                                "action": "permit",
                                "dst": "any",
                                "known-unicast-only": True,
                                "seq-id": 802,
                                "source": "host",
                                "srchost": "abcd.abcd.abcd",
                                "vlan": "1111",
                            },
                        },
                    },
                },
                "standard": {
                    "test-1": {
                        "name": "test-1",
                        "seqs": {
                            10: {
                                "action": "permit",
                                "count": True,
                                "seq-id": 10,
                                "source": "host",
                                "srchost": "aaaa.aaaa.aaaa",
                            },
                            20: {
                                "action": "deny",
                                "log": True,
                                "seq-id": 20,
                                "source": "aaaa.aaaa.aaa0",
                                "src-mac-addr-mask": "ffff.ffff.fff0",
                            },
                            30: {
                                "action": "hard-drop",
                                "copy-sflow": True,
                                "seq-id": 30,
                                "source": "any",
                            },
                        },
                    }
                },
            }
        }
    }

    class etree_holder():
        def __init__(self):
            self.data = ET.fromstring('''
            <data>
              <mac xmlns="urn:brocade.com:mgmt:brocade-mac-access-list">
                <access-list>
                  <standard>
                    <name>test-1</name>
                    <hide-mac-acl-std>
                      <seq>
                        <seq-id>10</seq-id>
                        <action>permit</action>
                        <source>host</source>
                        <srchost>aaaa.aaaa.aaaa</srchost>
                        <count/>
                      </seq>
                      <seq>
                        <seq-id>20</seq-id>
                        <action>deny</action>
                        <source>aaaa.aaaa.aaa0</source>
                        <src-mac-addr-mask>ffff.ffff.fff0</src-mac-addr-mask>
                        <log/>
                      </seq>
                      <seq>
                        <seq-id>30</seq-id>
                        <action>hard-drop</action>
                        <source>any</source>
                        <copy-sflow/>
                      </seq>
                    </hide-mac-acl-std>
                  </standard>
                  <extended>
                    <name>test-2</name>
                    <hide-mac-acl-ext>
                      <seq>
                        <seq-id>10</seq-id>
                        <action>permit</action>
                        <source>host</source>
                        <srchost>e481.84a5.e47e</srchost>
                        <dst>any</dst>
                        <vlan-tag-format>single-tagged</vlan-tag-format>
                        <vlan>10</vlan>
                        <ethertype>arp</ethertype>
                      </seq>
                      <seq>
                        <seq-id>11</seq-id>
                        <action>permit</action>
                        <source>bbbb.bbbb.bbb0</source>
                        <src-mac-addr-mask>ffff.ffff.fff0</src-mac-addr-mask>
                        <dst>any</dst>
                        <vlan-tag-format>single-tagged</vlan-tag-format>
                        <vlan>10</vlan>
                        <ethertype>ipv4</ethertype>
                      </seq>
                      <seq>
                        <seq-id>12</seq-id>
                        <action>deny</action>
                        <source>any</source>
                        <dst>host</dst>
                        <dsthost>cccc.cccc.ccc0</dsthost>
                        <vlan-tag-format>single-tagged</vlan-tag-format>
                        <vlan>30</vlan>
                        <ethertype>ipv6</ethertype>
                      </seq>
                      <seq>
                        <seq-id>13</seq-id>
                        <action>hard-drop</action>
                        <source>any</source>
                        <dst>cccc.cccc.cc00</dst>
                        <dst-mac-addr-mask>ffff.ffff.ff00</dst-mac-addr-mask>
                        <vlan-tag-format>single-tagged</vlan-tag-format>
                        <vlan>30</vlan>
                        <ethertype>ipv6</ethertype>
                      </seq>
                      <seq>
                        <seq-id>100</seq-id>
                        <action>deny</action>
                        <source>any</source>
                        <dst>any</dst>
                      </seq>
                    </hide-mac-acl-ext>
                  </extended>
                  <extended>
                    <name>test3</name>
                    <hide-mac-acl-ext>
                      <seq>
                        <seq-id>103</seq-id>
                        <action>permit</action>
                        <source>host</source>
                        <srchost>abcd.abcd.abcd</srchost>
                        <dst>any</dst>
                        <vlan-tag-format>double-tagged</vlan-tag-format>
                        <outer-vlan>200</outer-vlan>
                        <inner-vlan>1234</inner-vlan>
                        <ethertype>arp</ethertype>
                      </seq>
                      <seq>
                        <seq-id>104</seq-id>
                        <action>permit</action>
                        <source>host</source>
                        <srchost>abcd.abcd.abcd</srchost>
                        <dst>any</dst>
                        <vlan-tag-format>double-tagged</vlan-tag-format>
                        <outer-vlan>1234</outer-vlan>
                        <inner-vlan>200</inner-vlan>
                        <ethertype>ipv4</ethertype>
                      </seq>
                      <seq>
                        <seq-id>105</seq-id>
                        <action>permit</action>
                        <source>host</source>
                        <srchost>abcd.abcd.abcd</srchost>
                        <dst>any</dst>
                        <vlan-tag-format>double-tagged</vlan-tag-format>
                        <outer-vlan>10</outer-vlan>
                        <inner-vlan>10</inner-vlan>
                        <ethertype>ipv6</ethertype>
                      </seq>
                      <seq>
                        <seq-id>110</seq-id>
                        <action>permit</action>
                        <source>host</source>
                        <srchost>abcd.abcd.abcd</srchost>
                        <dst>any</dst>
                        <vlan-tag-format>single-tagged</vlan-tag-format>
                        <vlan>321</vlan>
                        <ethertype>arp</ethertype>
                      </seq>
                      <seq>
                        <seq-id>111</seq-id>
                        <action>permit</action>
                        <source>host</source>
                        <srchost>abcd.abcd.abcd</srchost>
                        <dst>any</dst>
                        <vlan-tag-format>single-tagged</vlan-tag-format>
                        <vlan>321</vlan>
                        <ethertype>ipv4</ethertype>
                      </seq>
                      <seq>
                        <seq-id>112</seq-id>
                        <action>permit</action>
                        <source>host</source>
                        <srchost>abcd.abcd.abcd</srchost>
                        <dst>any</dst>
                        <vlan-tag-format>single-tagged</vlan-tag-format>
                        <vlan>321</vlan>
                        <ethertype>ipv6</ethertype>
                      </seq>
                      <seq>
                        <seq-id>200</seq-id>
                        <action>permit</action>
                        <source>host</source>
                        <srchost>abcd.abcd.abcd</srchost>
                        <dst>any</dst>
                        <vlan-tag-format>single-tagged</vlan-tag-format>
                        <vlan>10</vlan>
                        <pcp>1</pcp>
                        <pcp-force>3</pcp-force>
                        <drop-precedence-force>2</drop-precedence-force>
                        <count/>
                        <log/>
                        <mirror/>
                      </seq>
                      <seq>
                        <seq-id>210</seq-id>
                        <action>permit</action>
                        <source>host</source>
                        <srchost>abcd.abcd.abcd</srchost>
                        <dst>any</dst>
                        <vlan-tag-format>single-tagged</vlan-tag-format>
                        <vlan>10</vlan>
                        <vlan-id-mask>0xfff</vlan-id-mask>
                      </seq>
                      <seq>
                        <seq-id>211</seq-id>
                        <action>permit</action>
                        <source>host</source>
                        <srchost>abcd.abcd.abcd</srchost>
                        <dst>any</dst>
                        <vlan-tag-format>single-tagged</vlan-tag-format>
                        <vlan>10</vlan>
                        <vlan-id-mask>0xfff</vlan-id-mask>
                        <ethertype>arp</ethertype>
                      </seq>
                      <seq>
                        <seq-id>610</seq-id>
                        <action>permit</action>
                        <source>host</source>
                        <srchost>abcd.abcd.abcd</srchost>
                        <dst>any</dst>
                        <vlan-tag-format>single-tagged</vlan-tag-format>
                        <vlan>10</vlan>
                      </seq>
                      <seq>
                        <seq-id>700</seq-id>
                        <action>permit</action>
                        <source>host</source>
                        <srchost>abcd.abcd.abcd</srchost>
                        <dst>any</dst>
                        <vlan-tag-format>single-tagged</vlan-tag-format>
                        <vlan>10</vlan>
                        <drop-precedence-force>1</drop-precedence-force>
                      </seq>
                      <seq>
                        <seq-id>800</seq-id>
                        <action>permit</action>
                        <source>host</source>
                        <srchost>abcd.abcd.abcd</srchost>
                        <dst>any</dst>
                        <vlan>1111</vlan>
                      </seq>
                      <seq>
                        <seq-id>801</seq-id>
                        <action>permit</action>
                        <source>host</source>
                        <srchost>abcd.abcd.abcd</srchost>
                        <dst>any</dst>
                        <vlan>1111</vlan>
                        <unknown-unicast-only/>
                      </seq>
                      <seq>
                        <seq-id>802</seq-id>
                        <action>permit</action>
                        <source>host</source>
                        <srchost>abcd.abcd.abcd</srchost>
                        <dst>any</dst>
                        <vlan>1111</vlan>
                        <known-unicast-only/>
                      </seq>
                    </hide-mac-acl-ext>
                  </extended>
                </access-list>
              </mac>
            </data>
            ''')
    golden_output = {'get.return_value': etree_holder()}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        intf_obj = ShowRunMacAccessList(device=self.device)
        intf_obj.context = Context.yang.value.split()
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    empty_parsed_output = {'mac': {'access-list': {}}}

    class empty_etree_holder():
        def __init__(self):
            self.data = ET.fromstring('''<data/>''')
    empty_output = {'get.return_value': empty_etree_holder()}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        intf_obj = ShowRunMacAccessList(device=self.device1)
        intf_obj.context = Context.yang.value.split()
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output, self.empty_parsed_output)


if __name__ == '__main__':
    unittest.main()
