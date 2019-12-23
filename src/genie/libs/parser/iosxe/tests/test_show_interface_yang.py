#!/bin/env python

import unittest
from unittest.mock import Mock

import xml.etree.ElementTree as ET

from pyats.topology import Device

from genie.ops.base import Context

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.iosxe.show_interface import ShowIpInterfaceBriefPipeVlan, \
                                                   ShowInterfacesSwitchport


class test_show_interface_brief_pipe_vlan_yang(unittest.TestCase):

    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    golden_parsed_output = {'interface': {'Vlan1': {'vlan_id': {'1': {'ip_address': 'unassigned'}}},
                                          'Vlan100': {'vlan_id': {'100': {'ip_address': '192.168.234.1'}}}}}

    class etree_holder():
      def __init__(self):
        self.data = ET.fromstring('''
          <data>
            <native xmlns="http://cisco.com/ns/yang/ned/ios">
              <interface>
                <Vlan>
                  <name>1</name>
                  <ip>
                    <no-address>
                      <address>false</address>
                    </no-address>
                  </ip>
                  <shutdown/>
                </Vlan>
                <Vlan>
                  <name>100</name>
                  <ip>
                    <address>
                      <primary>
                        <address>192.168.234.1</address>
                        <mask>255.255.255.0</mask>
                      </primary>
                    </address>
                  </ip>
                  <ipv6>
                    <address>
                      <prefix-list>
                        <prefix>2001::12:30/128</prefix>
                      </prefix-list>
                    </address>
                  </ipv6>
                </Vlan>
              </interface>
            </native>
          </data>
        ''')
    
    golden_output = {'get.return_value': etree_holder()}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        intf_obj = ShowIpInterfaceBriefPipeVlan(device=self.device)
        intf_obj.context = Context.yang.value.split()
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    empty_parsed_output = {'interface': {}}

    class empty_etree_holder():
      def __init__(self):
        self.data = ET.fromstring('''
          <data>
            <native xmlns="http://cisco.com/ns/yang/ned/ios">
              <interface>
                <Vlan>
                </Vlan>
              </interface>
            </native>
          </data>
        ''')

    empty_output = {'get.return_value': empty_etree_holder()}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        intf_obj = ShowIpInterfaceBriefPipeVlan(device=self.device1)
        intf_obj.context = Context.yang.value.split()
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output,self.empty_parsed_output)

# There is Not Yang output for show interface switchport
"""
class test_show_interfaces_switchport_yang(unittest.TestCase):

    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'interface': {'Gigabitethernet0/0': {},
               'Gigabitethernet1/0/1': {},
               'Gigabitethernet1/0/10': {'switchport_mode': {'access': {'vlan_id': {'400': {}}}}},
               'Gigabitethernet1/0/11': {},
               'Gigabitethernet1/0/12': {},
               'Gigabitethernet1/0/13': {},
               'Gigabitethernet1/0/14': {},
               'Gigabitethernet1/0/15': {},
               'Gigabitethernet1/0/16': {},
               'Gigabitethernet1/0/17': {},
               'Gigabitethernet1/0/18': {},
               'Gigabitethernet1/0/19': {},
               'Gigabitethernet1/0/2': {'switchport_mode': {'trunk': {'vlan_id': {'300': {}}}}},
               'Gigabitethernet1/0/20': {},
               'Gigabitethernet1/0/21': {},
               'Gigabitethernet1/0/22': {},
               'Gigabitethernet1/0/23': {},
               'Gigabitethernet1/0/24': {},
               'Gigabitethernet1/0/3': {'switchport_mode': {'trunk': {'vlan_id': {'300': {'allowed_vlans': '400'}}}}},
               'Gigabitethernet1/0/4': {},
               'Gigabitethernet1/0/5': {'switchport_mode': {'trunk': {}}},
               'Gigabitethernet1/0/6': {},
               'Gigabitethernet1/0/7': {},
               'Gigabitethernet1/0/8': {},
               'Gigabitethernet1/0/9': {},
               'Gigabitethernet1/1/1': {},
               'Gigabitethernet1/1/2': {},
               'Gigabitethernet1/1/3': {},
               'Gigabitethernet1/1/4': {},
               'Gigabitethernet2/0/1': {},
               'Gigabitethernet2/0/10': {},
               'Gigabitethernet2/0/11': {},
               'Gigabitethernet2/0/12': {},
               'Gigabitethernet2/0/13': {},
               'Gigabitethernet2/0/14': {},
               'Gigabitethernet2/0/15': {'switchport_mode': {'access': {'vlan_id': {'400': {}}}}},
               'Gigabitethernet2/0/16': {},
               'Gigabitethernet2/0/17': {},
               'Gigabitethernet2/0/18': {},
               'Gigabitethernet2/0/19': {},
               'Gigabitethernet2/0/2': {},
               'Gigabitethernet2/0/20': {},
               'Gigabitethernet2/0/21': {},
               'Gigabitethernet2/0/22': {},
               'Gigabitethernet2/0/23': {},
               'Gigabitethernet2/0/24': {},
               'Gigabitethernet2/0/3': {},
               'Gigabitethernet2/0/4': {},
               'Gigabitethernet2/0/5': {},
               'Gigabitethernet2/0/6': {},
               'Gigabitethernet2/0/7': {},
               'Gigabitethernet2/0/8': {},
               'Gigabitethernet2/0/9': {},
               'Gigabitethernet2/1/1': {},
               'Gigabitethernet2/1/2': {},
               'Gigabitethernet2/1/3': {},
               'Gigabitethernet2/1/4': {},
               'Gigabitethernet3/0/1': {},
               'Gigabitethernet3/0/10': {},
               'Gigabitethernet3/0/11': {},
               'Gigabitethernet3/0/12': {},
               'Gigabitethernet3/0/13': {},
               'Gigabitethernet3/0/14': {},
               'Gigabitethernet3/0/15': {},
               'Gigabitethernet3/0/16': {},
               'Gigabitethernet3/0/17': {},
               'Gigabitethernet3/0/18': {},
               'Gigabitethernet3/0/19': {},
               'Gigabitethernet3/0/2': {},
               'Gigabitethernet3/0/20': {},
               'Gigabitethernet3/0/21': {},
               'Gigabitethernet3/0/22': {},
               'Gigabitethernet3/0/23': {},
               'Gigabitethernet3/0/24': {},
               'Gigabitethernet3/0/3': {},
               'Gigabitethernet3/0/4': {},
               'Gigabitethernet3/0/5': {},
               'Gigabitethernet3/0/6': {},
               'Gigabitethernet3/0/7': {},
               'Gigabitethernet3/0/8': {},
               'Gigabitethernet3/0/9': {},
               'Gigabitethernet3/1/1': {},
               'Gigabitethernet3/1/2': {},
               'Gigabitethernet3/1/3': {},
               'Gigabitethernet3/1/4': {},
               'Gigabitethernet4/0/1': {},
               'Gigabitethernet4/0/10': {},
               'Gigabitethernet4/0/11': {},
               'Gigabitethernet4/0/12': {},
               'Gigabitethernet4/0/13': {},
               'Gigabitethernet4/0/14': {},
               'Gigabitethernet4/0/15': {},
               'Gigabitethernet4/0/16': {},
               'Gigabitethernet4/0/17': {},
               'Gigabitethernet4/0/18': {},
               'Gigabitethernet4/0/19': {},
               'Gigabitethernet4/0/2': {},
               'Gigabitethernet4/0/20': {},
               'Gigabitethernet4/0/21': {},
               'Gigabitethernet4/0/22': {},
               'Gigabitethernet4/0/23': {},
               'Gigabitethernet4/0/24': {},
               'Gigabitethernet4/0/3': {},
               'Gigabitethernet4/0/4': {},
               'Gigabitethernet4/0/5': {},
               'Gigabitethernet4/0/6': {},
               'Gigabitethernet4/0/7': {},
               'Gigabitethernet4/0/8': {},
               'Gigabitethernet4/0/9': {},
               'Gigabitethernet4/1/1': {},
               'Gigabitethernet4/1/2': {},
               'Gigabitethernet4/1/3': {},
               'Gigabitethernet4/1/4': {},
               'Gigabitethernet5/0/1': {},
               'Gigabitethernet5/0/10': {},
               'Gigabitethernet5/0/11': {},
               'Gigabitethernet5/0/12': {},
               'Gigabitethernet5/0/13': {},
               'Gigabitethernet5/0/14': {},
               'Gigabitethernet5/0/15': {},
               'Gigabitethernet5/0/16': {},
               'Gigabitethernet5/0/17': {},
               'Gigabitethernet5/0/18': {},
               'Gigabitethernet5/0/19': {},
               'Gigabitethernet5/0/2': {},
               'Gigabitethernet5/0/20': {},
               'Gigabitethernet5/0/21': {},
               'Gigabitethernet5/0/22': {},
               'Gigabitethernet5/0/23': {},
               'Gigabitethernet5/0/24': {},
               'Gigabitethernet5/0/3': {},
               'Gigabitethernet5/0/4': {},
               'Gigabitethernet5/0/5': {},
               'Gigabitethernet5/0/6': {},
               'Gigabitethernet5/0/7': {},
               'Gigabitethernet5/0/8': {},
               'Gigabitethernet5/0/9': {},
               'Gigabitethernet5/1/1': {},
               'Gigabitethernet5/1/2': {},
               'Gigabitethernet5/1/3': {},
               'Gigabitethernet5/1/4': {}}
}

    class etree_holder():
      def __init__(self):
        self.data = ET.fromstring('''
          <data>
            <native xmlns="http://cisco.com/ns/yang/ned/ios">
              <interface>
                <GigabitEthernet>
                  <name>0/0</name>
                  <negotiation>
                    <auto>true</auto>
                  </negotiation>
                  <vrf>
                    <forwarding>Mgmt-vrf</forwarding>
                  </vrf>
                  <ip>
                    <address>
                      <primary>
                        <address>10.1.10.20</address>
                        <mask>255.255.255.0</mask>
                      </primary>
                    </address>
                  </ip>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/1</name>
                  <switchport-conf>
                    <switchport>false</switchport>
                  </switchport-conf>
                  <ip>
                    <no-address>
                      <address>false</address>
                    </no-address>
                  </ip>
                  <standby>
                    <standby-list>
                      <group-number>5</group-number>
                      <priority>110</priority>
                    </standby-list>
                  </standby>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/10</name>
                  <switchport>
                    <access>
                      <vlan>
                        <vlan>400</vlan>
                      </vlan>
                    </access>
                    <mode>
                      <access/>
                    </mode>
                  </switchport>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/11</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/12</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/13</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/14</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/15</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/16</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/17</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/18</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/19</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/2</name>
                  <switchport>
                    <access>
                      <vlan>
                        <vlan>2</vlan>
                      </vlan>
                    </access>
                    <trunk>
                      <native>
                        <vlan>300</vlan>
                      </native>
                    </trunk>
                  </switchport>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/20</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/21</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/22</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/23</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/24</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/3</name>
                  <switchport>
                    <access>
                      <vlan>
                        <vlan>300</vlan>
                      </vlan>
                    </access>
                    <mode>
                      <trunk/>
                    </mode>
                    <trunk>
                      <allowed>
                        <vlan>
                          <vlans>400</vlans>
                        </vlan>
                      </allowed>
                    </trunk>
                  </switchport>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/4</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/5</name>
                  <switchport>
                    <mode>
                      <trunk/>
                    </mode>
                    <trunk>
                      <allowed>
                        <vlan>
                          <vlans>200,201</vlans>
                        </vlan>
                      </allowed>
                    </trunk>
                  </switchport>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/6</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/7</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/8</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/0/9</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/1/1</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/1/2</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/1/3</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>1/1/4</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/1</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/10</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/11</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/12</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/13</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/14</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/15</name>
                  <switchport>
                    <access>
                      <vlan>
                        <vlan>400</vlan>
                      </vlan>
                    </access>
                    <mode>
                      <access/>
                    </mode>
                  </switchport>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/16</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/17</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/18</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/19</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/2</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/20</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/21</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/22</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/23</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/24</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/3</name>
                  <switchport-conf>
                    <switchport>false</switchport>
                  </switchport-conf>
                  <ip>
                    <no-address>
                      <address>false</address>
                    </no-address>
                  </ip>
                  <standby>
                    <delay>
                      <minimum>5</minimum>
                    </delay>
                    <standby-list>
                      <group-number>0</group-number>
                      <name>helsinki</name>
                    </standby-list>
                    <standby-list>
                      <group-number>1</group-number>
                      <preempt>
                        <delay>
                          <minimum>10</minimum>
                        </delay>
                      </preempt>
                    </standby-list>
                    <standby-list>
                      <group-number>10</group-number>
                      <preempt/>
                    </standby-list>
                  </standby>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/4</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/5</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/6</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/7</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/8</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/0/9</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/1/1</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/1/2</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/1/3</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>2/1/4</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/1</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/10</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/11</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/12</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/13</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/14</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/15</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/16</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/17</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/18</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/19</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/2</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/20</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/21</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/22</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/23</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/24</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/3</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/4</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/5</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/6</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/7</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/8</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/0/9</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/1/1</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/1/2</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/1/3</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>3/1/4</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/1</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/10</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/11</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/12</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/13</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/14</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/15</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/16</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/17</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/18</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/19</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/2</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/20</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/21</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/22</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/23</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/24</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/3</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/4</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/5</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/6</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/7</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/8</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/0/9</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/1/1</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/1/2</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/1/3</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>4/1/4</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/1</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/10</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/11</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/12</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/13</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/14</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/15</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/16</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/17</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/18</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/19</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/2</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/20</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/21</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/22</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/23</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/24</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/3</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/4</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/5</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/6</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/7</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/8</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/0/9</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/1/1</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/1/2</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/1/3</name>
                </GigabitEthernet>
                <GigabitEthernet>
                  <name>5/1/4</name>
                </GigabitEthernet>
              </interface>
            </native>
          </data>
        ''')

    golden_output = {'get.return_value': etree_holder()}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        intf_obj = ShowInterfacesSwitchport(device=self.device)
        intf_obj.context = Context.yang.value
        parsed_output = intf_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    empty_parsed_output = {'interface': {}}

    class empty_etree_holder():
      def __init__(self):
        self.data = ET.fromstring('''
          <data>
            <native xmlns="http://cisco.com/ns/yang/ned/ios">
              <interface>
                <GigabitEthernet>
                </GigabitEthernet>
              </interface>
            </native>
          </data>
        ''')

    empty_output = {'get.return_value': empty_etree_holder()}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        intf_obj = ShowInterfacesSwitchport(device=self.device1)
        intf_obj.context = Context.yang.value
        parsed_output = intf_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.empty_parsed_output)
"""
if __name__ == '__main__':
    unittest.main()