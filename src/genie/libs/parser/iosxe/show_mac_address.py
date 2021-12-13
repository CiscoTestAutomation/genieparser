''' show_mac_address.py

IOSXE parsers for the following show commands:
    * show mac address-table dynamic address {mac_address}
    * show mac address-table dynamic vlan {vlan_id}
'''
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
    Any, \
    Optional, \
    Or, \
    And, \
    Default, \
    Use

# import parser utils
from genie.libs.parser.utils.common import Common



# ==============================================
# Parser for 'show mac address-table dynamic address {mac_address} and show mac address-table dynamic vlan {vlan_id}'
# ==============================================

class ShowMacAddressTableDynamicSchema(MetaParser):
    """Schema for show mac address-table dynamic address {mac_address}
                  show mac address-table dynamic vlan {vlan_id}
    """
    schema = {
               'ports': {
                   Any(): {
                       'mac-address': str,
                       'port': str,
                       'type': str,
                       'vlan-id': int},
               }

    }


class ShowMacAddressTableDynamic(ShowMacAddressTableDynamicSchema):
    """Parser for show mac address-table dynamic address {mac_address}
                  show mac address-table dynamic vlan {vlan_id}
    """

    cli_command = ['show mac address-table dynamic address {mac_address}', 'show mac address-table dynamic vlan {vlan_id}']
    def cli(self, mac_address=None, vlan_id=None, output=None):
        if mac_address:
            cmd = self.cli_command[0].format(mac_address=mac_address)
        else:
            cmd = self.cli_command[1].format(vlan_id=vlan_id)

        if output is None:
            # get output from device
            out = self.device.execute(cmd)
        else:
            out = output
        # initial return dictionary
        vlan_dict = {}
        p1 = re.compile(r'(?P<vlan_id>\d+) +'
                    '(?P<mac>([a-zA-Z0-9]+\.){2}[a-zA-Z0-9]+) +'
                    '(?P<type>\w+) +'
                    '(?P<port>\S+)')

        port_count = 1
        for line in out.splitlines():
            line = line.strip()
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                ports = vlan_dict.setdefault('ports', {})
                port_dict = ports.setdefault(port_count, {})
                port_dict['vlan-id'] = int(group['vlan_id'])
                port_dict['mac-address'] = group['mac']
                port_dict['type'] = group['type']
                port_dict['port'] = group['port']
                port_count+=1
        return(vlan_dict)
# =============================================
# Schema for 'show mac address-table count summary'
# =============================================
class ShowMacAddressTableCountSummarySchema(MetaParser):
    """ Schema for
        * show mac address-table count summary
    """
    schema = {
        'Total_dynamic_address_count': int,
        'Total_static_address_count': int,
        'Total_mac_address' : int,
        'Total_mac_address_space' : int
    }
# ==========================================================
#  Parser for 'show mac address-table count summary'
# ==========================================================

class ShowMacAddressTableCountSummary(ShowMacAddressTableCountSummarySchema):
    """ Parser for
        * show mac address-table count summary
    """
    cli_command = 'show mac address-table count summary'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        #Total Dynamic Address Count  : 15
        p1 = re.compile(r'Total\s+Dynamic\s+Address\s+Count\s+:\s+(?P<dynamic_count>\d+)')
        #Total Static  Address Count  : 0
        p2 = re.compile(r'Total\s+Static\s+Address\s+Count\s+:\s+(?P<static_count>\d+)')
        #Total Mac Address In Use     : 15
        p3 = re.compile(r'Total\s+Mac\s+Address\s+In\s+Use\s+:\s+(?P<total_mac>\d+)')
        #Total Mac Address Space Available: 65521
        p4 = re.compile(r'Total\s+Mac\s+Address\s+Space\s+Available:\s+(?P<total_mac_space>\d+)')
        for line in output.splitlines():
            line = line.strip()
            #Total Dynamic Address Count  : 15
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                ret_dict["Total_dynamic_address_count"] = int(group["dynamic_count"])
            #Total Static  Address Count  : 0
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                ret_dict["Total_static_address_count"] = int(group["static_count"])
            #Total Mac Address In Use     : 15
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                ret_dict["Total_mac_address"] = int(group["total_mac"])

            #Total Mac Address Space Available: 65521
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                ret_dict["Total_mac_address_space"] = int(group["total_mac_space"])

        return ret_dict

