"""
IOSXE C9300 parsers for the following show commands:
    * show idprom
"""

# Python
import re
import logging
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

# ============================
#  Schema for 'show idprom interface <interface>'
# ============================

class ShowIdpromInterfaceSchema(MetaParser):
    """Schema for show idprom interface {interface}"""
    schema = {
        'sfp_info': {
            'vendor_name': str,
            'cisco_part_number': str,
            'vendor_revision': str,
            'serial_number': str,
            'product_identifier': str,
            'connector_type': str,
        }
    }

# ============================
#  Parser for 'show idprom interface <interface>'
# ============================

class ShowIdpromInterface(ShowIdpromInterfaceSchema):
    """Parser for show idprom interface <interface>"""

    cli_command = [
        'show idprom interface {interface}'
    ]

    def cli(self, interface, output=None):
        if output is None:
            cmd = self.cli_command[0].format(interface=interface)
            output = self.device.execute(cmd)

        ret_dict = {}

        # General SFP Information
        p1 = re.compile(
            r'^General SFP Information$')

        # Vendor Name           :   CISCO-EXCELIGHT
        p2 = re.compile(
            r'^Vendor +Name\s+:\s+(?P<vendor_name>.*)$')

        # Vendor Part Number    :   SPP5101SR-C1 
        p3 = re.compile(
            r'^Vendor +Part +Number\s+:\s+(?P<part_number>.*)$')

        # Vendor Revision       :   0x41 0x20 0x20 0x20
        p4 = re.compile(
            r'^Vendor +Revision\s+\:\s+(?P<vendor_revision>[0-9a-fA-Fx ]+)$')

        # Vendor Serial Number  :   ECL1249000S 
        p5 = re.compile(
            r'^Vendor +Serial +Number\s+:\s+(?P<serial_number>.*)$')

        # Identifier            :   SFP/SFP+
        p6 = re.compile(
            r'^Identifier\s+:\s+(?P<product_identifier>.*)$')

        # Connector             :   LC connector
        p7 = re.compile(
            r'^Connector\s+:\s+(?P<connector_type>[\w\s]+)$')

        for line in output.splitlines():
            line = line.strip()

            # General SFP Information
            m = p1.match(line)
            if m:
                sfp_info_dict = ret_dict.setdefault('sfp_info',{})

            # Vendor Name           :   CISCO-EXCELIGHT
            m = p2.match(line)
            if m:
                sfp_info_dict['vendor_name'] = m.groupdict()['vendor_name']
                continue

            # Vendor Part Number    :   SPP5101SR-C1 
            m = p3.match(line)
            if m:
                sfp_info_dict['cisco_part_number'] = m.groupdict()['part_number']
                continue

            # Vendor Revision       :   0x41 0x20 0x20 0x20
            m = p4.match(line)
            if m:
                sfp_info_dict['vendor_revision'] = m.groupdict()['vendor_revision']
                continue

            # Vendor Serial Number  :   ECL1249000S 
            m = p5.match(line)
            if m:
                sfp_info_dict['serial_number'] = m.groupdict()['serial_number']
                continue

            # Identifier            :   SFP/SFP+
            m = p6.match(line)
            if m:
                sfp_info_dict['product_identifier'] = m.groupdict()['product_identifier']
                continue

            # Connector             :   LC connector
            m = p7.match(line)
            if m:
                sfp_info_dict['connector_type'] = m.groupdict()['connector_type']
                continue

        return ret_dict