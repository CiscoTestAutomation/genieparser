"""show_eee.py

IOSXE parsers for the following show commands:
    * 'show eee status interface <interface-id>'
    * 'show eee capabilities interface <interface-id>'
"""

from poplib import POP3_SSL_PORT
import re
import logging

from genie.libs.parser.utils.common import Common
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (And, Any, Default, Optional,
                                                Or, Schema, Use)

logger = logging.getLogger(__name__)


# ======================================================
# Parser for 'show eee status interface {interface}'
# ======================================================

class ShowEeeStatusInterfaceSchema(MetaParser):
    """Schema for show eee status interface {interface}"""

    schema = {
        'interface': {
            Any(): {
                'status': str,
                'eee_mode': str,
                'rx_lpi': str,
                'tx_lpi': str,
                'wake_error': int,
                Optional('asic_eee_status'): {
                    'rx_lpi': str,
                    'tx_lpi': str,
                    'link_fault_status': str,
                    'sync_status': str
                }
            }
        }
    }


class ShowEeeStatusInterface(ShowEeeStatusInterfaceSchema):
    """Parser for show eee status interface {interface}"""

    cli_command = 'show eee status interface {interface}'

    def cli(self, interface, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        # Te1/0/47 is up
        p0 = re.compile(r"^(?P<interface>[\w\/\.]+) is (?P<status>\w+)$")
        
        # EEE(efficient-ethernet):  Operational/Disabled/Disagreed
        p1 = re.compile(r"^EEE\(efficient-ethernet\):\s+(?P<eee_mode>.*)$")
        
        # Rx LPI Status          :  None/Low Power/Received
        # Rx LPI Status          :  Receiving LPI
        p2 = re.compile(r"^Rx\s+LPI\s+Status\s+:\s+(?P<rx_lpi>.*)$")
        
        # Tx LPI Status          :  None/Low Power/Received
        # Tx LPI Status          :  Transmitting LPI
        p3 = re.compile(r"^Tx\s+LPI\s+Status\s+:\s+(?P<tx_lpi>.*)$")

        # Wake Error Count       :  0
        p4 = re.compile(r"^Wake Error Count\s+:\s+(?P<wake_error>\d+)$")

        # ASIC EEE STATUS
        p5 = re.compile(r"^ASIC EEE STATUS$")

        # Link Fault Status      :  Link Up
        p6 = re.compile(r"^Link Fault Status\s+:\s+(?P<link_fault_status>.*)$")

        # Sync Status            :  Code group synchronization with data stream lost
        p7 = re.compile(r"^Sync Status\s+:\s+(?P<sync_status>.*)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Te1/0/47 is up
            m = p0.match(line)
            if m:
                int_dict = ret_dict.setdefault('interface', {}).setdefault(Common.convert_intf_name(m.groupdict()['interface']), {})
                int_dict['status'] = m.groupdict()['status']
                continue

            # EEE(efficient-ethernet):  Operational/Disabled/Disagreed (o/p  an be one of these states)
            m = p1.match(line)
            if m:
                int_dict['eee_mode'] = m.groupdict()['eee_mode']
                continue

            # Rx LPI Status : None/Low Power/Received
            m = p2.match(line)
            if m:
                int_dict['rx_lpi'] = m.groupdict()['rx_lpi']
                continue

            # Tx LPI Status : None/Low Power/Received
            m = p3.match(line)
            if m:
                int_dict['tx_lpi'] = m.groupdict()['tx_lpi']
                continue

            # Wake Error Count       :  0
            m = p4.match(line)
            if m:
                int_dict['wake_error'] = int(m.groupdict()['wake_error'])
                continue

            # ASIC EEE STATUS
            m = p5.match(line)
            if m:
                int_dict = int_dict.setdefault('asic_eee_status', {})
                continue

            # Link Fault Status      :  Link Up
            m = p6.match(line)
            if m:
                int_dict['link_fault_status'] = m.groupdict()['link_fault_status']
                continue

            # Sync Status            :  Code group synchronization with data stream lost
            m = p7.match(line)
            if m:
                int_dict['sync_status'] = m.groupdict()['sync_status']
                continue

        return ret_dict

# ===========================================================
# Parser for 'show eee capabilities interface {interface}'
# ===========================================================

class ShowEeeCapabilitiesInterfaceSchema(MetaParser):
    """Schema for show eee capabilities interface {interface}"""

    schema = {
        'interface': {
            Any(): {
                'eee_mode': str,
                'link_partner': str,
                'asic_interface': str,
            }
        }
    }


class ShowEeeCapabilitiesInterface(ShowEeeCapabilitiesInterfaceSchema):
    """Parser for show eee capabilities interface {interface}"""

    cli_command = 'show eee capabilities interface {interface}'

    def cli(self, interface, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        # Te1/0/47
        p0 = re.compile(r"^(?P<interface>[\w\/\.]+)$")

        # EEE(efficient-ethernet):  yes (1000T, 2G, and 5G auto)
        p1 = re.compile(r"^\s*EEE\(efficient-ethernet\):\s+(?P<eee_mode>.*)$")
        
        # Link Partner           :  not enabled
        p2 = re.compile(r"^\s*Link\s+Partner\s+:\s+(?P<link_partner>.*)$")

        # ASIC/Interface         :  EEE Incapable/None
        p3 = re.compile(r"^ASIC\/Interface\s+:\s+(?P<asic_interface>.+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Te1/0/47
            m = p0.match(line)
            if m:
                int_dict = ret_dict.setdefault('interface', {})\
                    .setdefault(Common.convert_intf_name(m.groupdict()['interface']), {})
                continue
            
            # EEE(efficient-ethernet):  yes (1000T, 2G, and 5G auto)
            m = p1.match(line)
            if m:
                int_dict['eee_mode'] = m.groupdict()['eee_mode']
                continue

            # Link Partner           :  not enabled
            m = p2.match(line)
            if m:
                int_dict['link_partner'] = m.groupdict()['link_partner']
                continue

            # ASIC/Interface         :  EEE Incapable/None
            m = p3.match(line)
            if m:
                int_dict['asic_interface'] = m.groupdict()['asic_interface']
                continue

        return ret_dict
