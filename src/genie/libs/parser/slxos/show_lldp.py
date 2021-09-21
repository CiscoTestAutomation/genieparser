"""
Author:
    Fabio Pessoa Nunes (https://www.linkedin.com/in/fpessoanunes/)

show_lldp.py

SLXOS parsers for the following show commands:
    * show lldp neighbor

Schemas based on SLX's YANG models
"""

import re
import xml.etree.ElementTree as ET

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =================================================
# Schema for:
#   * 'show lldp neighbor'
# ==================================================
class ShowLldpNeighborsSchema(MetaParser):
    ''' Schema for "show lldp neighbor" '''
    schema = {
        'total_entries': int,
        Optional('interfaces'): {
            Any(): {
                'local_interface_name': str,
                'neighbors': {
                    Any(): {
                        'remote_chassis_id': str,
                        'remote_interface_name': str,
                        Optional('remote_system_name'): str
                    }
                }
            }
        }
    }


# ===================================
# Parser for:
#   * 'show lldp neighbor'
# ===================================
class ShowLldpNeighbors(ShowLldpNeighborsSchema):
    ''' Parser for "show lldp neighbor" '''

    cli_command = ['show lldp neighbors']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        lldp_dict = {}

        # Total no. of Records: 3
        p1 = re.compile(
            r'[\s\S]*Total\s+no.\s+of\s+Records:\s+(?P<entry>\d+)$')

        # Local Port    Dead Interval  Remaining Life  Remote Port ID                    Remote Port Descr                 Chassis ID       Tx           Rx           System Name
        # Eth 0/8       120            107             Ethernet 0/1                      U_                                d884.66ea.fe14   382863       77092        SLX
        # Eth 0/44      120            97              71                                                                  0004.96a3.4b5d   1950327      299888       switch-01
        # Eth 0/45      120            97              72                                                                  0004.96a3.4b5d   1950327      299888       switch-01
        p2 = re.compile(
            r'^(?P<local_port>[\w\/\.\-\:]+(?:\s[\w\/\.\-\:]+|()))\s+'
            r'(?P<dead_interval>\d+)\s+\d+\s+'
            r'(?P<remote_port>[\w\/\.\-\:]+(?:\s[\w\/\.\-\:]+|())).*'
            r'(?P<remote_chassis_id>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})\s+\d+\s+\d+'
            r'(?:|\s+(?P<remote_chassis_name>\S*)|())$')

        for line in out.splitlines():
            line = line.strip()

            # Total entries displayed: 4
            m = p1.match(line)
            if m:
                lldp_dict['total_entries'] = int(m.groupdict()['entry'])
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()

                interfaces = lldp_dict.setdefault('interfaces', {})

                if 'Eth ' in group['local_port']:
                    intf_local = group['local_port'].replace('Eth ', 'Ethernet ')
                else:
                    intf_local = group['local_port']

                if intf_local not in interfaces.keys():
                    interface = interfaces.setdefault(intf_local, {})
                    interface['local_interface_name'] = intf_local
                    neighbors = interface.setdefault('neighbors', {})
                else:
                    neighbors = interfaces[intf_local]['neighbors']

                neighbor = neighbors.setdefault(group['remote_port'], {})
                neighbor['remote_chassis_id'] = group['remote_chassis_id']
                neighbor['remote_interface_name'] = group['remote_port']
                if group['remote_chassis_name'] is not None:
                    neighbor['remote_system_name'] = group['remote_chassis_name']
            continue

        return lldp_dict

    def yang(self):
        rpc_request = """
            <get-lldp-neighbor-detail xmlns="urn:brocade.com:mgmt:brocade-lldp-ext">
            </get-lldp-neighbor-detail>
        """
        rpc_request_more = """
            <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <get-lldp-neighbor-detail xmlns="urn:brocade.com:mgmt:brocade-lldp-ext">
            <last-rcvd-ifindex>%s</last-rcvd-ifindex>
            </get-lldp-neighbor-detail>
            </rpc>
        """
        lldp_dict = {}
        last_rcvd_ifindex = None
        has_more = True
        while has_more:
            has_more = False
            if last_rcvd_ifindex is None:
                output = ET.fromstring(self.device.request(rpc_request))
            else:
                output = ET.fromstring(self.device.request(rpc_request_more % last_rcvd_ifindex))
            for elem in output:
                if elem.tag == '{urn:brocade.com:mgmt:brocade-lldp-ext}lldp-neighbor-detail':
                    for iter in elem:
                        if iter.tag == '{urn:brocade.com:mgmt:brocade-lldp-ext}local-interface-name':
                            if 'Eth ' in iter.text:
                                intf_local = iter.text.replace('Eth ', 'Ethernet ')
                            else:
                                intf_local = iter.text
                            interfaces = lldp_dict.setdefault('interfaces', {})
                            interface = interfaces.setdefault(intf_local, {})
                            interface['local_interface_name'] = intf_local
                        elif iter.tag == '{urn:brocade.com:mgmt:brocade-lldp-ext}remote-interface-name':
                            neighbor = interface.setdefault('neighbors', {}).setdefault(iter.text, {})
                            neighbor['remote_interface_name'] = iter.text
                        elif iter.tag == '{urn:brocade.com:mgmt:brocade-lldp-ext}remote-chassis-id':
                            neighbor['remote_chassis_id'] = iter.text
                        elif iter.tag == '{urn:brocade.com:mgmt:brocade-lldp-ext}remote-system-name':
                            neighbor['remote_system_name'] = iter.text
                        elif iter.tag == '{urn:brocade.com:mgmt:brocade-lldp-ext}local-interface-ifindex':
                            last_rcvd_ifindex = iter.text
                    lldp_dict.setdefault('total_entries', 0)
                    lldp_dict['total_entries'] += 1
                elif elem.tag == '{urn:brocade.com:mgmt:brocade-lldp-ext}has-more':
                    if elem.text == 'true':
                        has_more = True
                lldp_dict.setdefault('total_entries', 0)
        return lldp_dict
