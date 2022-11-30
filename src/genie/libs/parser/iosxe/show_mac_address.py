''' show_mac_address.py

IOSXE parsers for the following show commands:
    * show mac address-table dynamic address {mac_address}
    * show mac address-table dynamic vlan {vlan_id}
    * show mac address-table count
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

# =============================================
# Schema for 'show mac address-table count vlan {vlan_id}'
# =============================================
class ShowMacAddressTableCountVlanSchema(MetaParser):
    """ Schema for
        * show mac address-table count vlan {vlan_id}
    """
    schema = {
        'Total_dynamic_address_count': int,
        'Total_static_address_count': int,
        'Total_mac_address_in_use' : int,
        'Total_mac_address_space' : int
    }
# ==========================================================
#  Parser for 'show mac address-table count vlan {vlan_id}'
# ==========================================================

class ShowMacAddressTableCountVlan(ShowMacAddressTableCountVlanSchema):
    """ Parser for
        * show mac address-table count vlan {vlan_id}
    """
    cli_command = 'show mac address-table count vlan {vlan_id}'

    def cli(self, vlan_id, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(vlan_id=vlan_id))
        ret_dict = {}
        #Dynamic Address Count  : 15
        p1 = re.compile(r'^Dynamic\s+Address\s+Count\s+:\s+(?P<dynamic_count>\d+)$')
        #Static  Address Count  : 0
        p2 = re.compile(r'^Static\s+Address\s+Count\s+:\s+(?P<static_count>\d+)$')
        #Total Mac Address In Use     : 15
        p3 = re.compile(r'^Total\s+Mac\s+Addresses\s+:\s+(?P<mac>\d+)$')
        #Total Mac Address Space Available: 65521
        p4 = re.compile(r'^Total\s+Mac\s+Address\s+Space\s+Available:\s+(?P<total_mac_space>\d+)$')
        for line in output.splitlines():
            line = line.strip()
            #Total Dynamic Address Count  : 15
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                ret_dict["Total_dynamic_address_count"] = int(group["dynamic_count"])
                continue
            #Total Static  Address Count  : 0
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                ret_dict["Total_static_address_count"] = int(group["static_count"])
                continue
            #Total Mac Address In Use     : 15
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                ret_dict["Total_mac_address_in_use"] = int(group["mac"])
                continue
            #Total Mac Address Space Available: 65521
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                ret_dict["Total_mac_address_space"] = int(group["total_mac_space"])
                continue
        return ret_dict


# ======================================================
# Parser for 'show mac address-table count '
# ======================================================

class ShowMacAddressTableCountSchema(MetaParser):
    """Schema for show mac address-table count"""

    schema = {
        'vlan': {
            Any(): {
                'static_address_count': int,
                'dynamic_address_count': int,
                'total_mac_address': int
            },
        },
        'total_dynamic_address_count': int,
        'total_static_address_count': int,
        'total_mac_address_in_use': int,
        'total_mac_address_space': int,
    }

class ShowMacAddressTableCount(ShowMacAddressTableCountSchema):
    """Parser for show mac address-table count"""

    cli_command = 'show mac address-table count'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Mac Entries for Vlan 1:
        p1 = re.compile(r"^Mac\s+Entries\s+for\s+Vlan\s+(?P<vlan>\d+):$")
        # Static  Address Count  : 1
        p1_1 = re.compile(r"^Static\s+Address\s+Count\s+:\s+(?P<static_address_count>\d+)$")
        # Dynamic Address Count  : 8
        p2 = re.compile(r"^Dynamic\s+Address\s+Count\s+:\s+(?P<dynamic_address_count>\d+)$")
        # Total Mac Addresses    : 9
        p3 = re.compile(r"^Total\s+Mac\s+Addresses\s+:\s+(?P<total_mac_address>\d+)$")
        # Total Dynamic Address Count  : 32776
        p4 = re.compile(r"^Total\s+Dynamic\s+Address\s+Count\s+:\s+(?P<total_dynamic_address_count>\d+)$")
        # Total Static  Address Count  : 2
        p5 = re.compile(r"^Total\s+Static\s+Address\s+Count\s+:\s+(?P<total_static_address_count>\d+)$")
        # Total Mac Address In Use     : 32778
        p6 = re.compile(r"^Total\s+Mac\s+Address\s+In\s+Use\s+:\s+(?P<total_mac_address_in_use>\d+)$")
        # Total Mac Address Space Available: 98294
        p7 = re.compile(r"^Total\s+Mac\s+Address\s+Space\s+Available:\s+(?P<total_mac_address_space>\d+)$")

        ret_dict = {}

        for line in output.splitlines():

            # Mac Entries for Vlan 1:
            match_obj = p1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                vlan_var = dict_val['vlan']
                vlan_dict = ret_dict.setdefault('vlan', {}).setdefault(vlan_var, {})
                continue

            # Static  Address Count  : 1
            match_obj = p1_1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                vlan_dict['static_address_count'] = int(dict_val['static_address_count'])
                continue

            # Dynamic Address Count  : 8
            match_obj = p2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                vlan_dict['dynamic_address_count'] = int(dict_val['dynamic_address_count'])
                continue

            # Total Mac Addresses    : 9
            match_obj = p3.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                vlan_dict['total_mac_address'] = int(dict_val['total_mac_address'])
                continue

            # Total Dynamic Address Count  : 32776
            match_obj = p4.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                ret_dict['total_dynamic_address_count'] = int(dict_val['total_dynamic_address_count'])
                continue

            # Total Static  Address Count  : 2
            match_obj = p5.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                ret_dict['total_static_address_count'] = int(dict_val['total_static_address_count'])
                continue

            # Total Mac Address In Use     : 32778
            match_obj = p6.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                ret_dict['total_mac_address_in_use'] = int(dict_val['total_mac_address_in_use'])
                continue

            # Total Mac Address Space Available: 98294
            match_obj = p7.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                ret_dict['total_mac_address_space'] = int(dict_val['total_mac_address_space'])
                continue

        return ret_dict
