"""show_ip_nat.py
    supported commands:
        * show ip nat translations
        * show ip nat translations verbose
        * show ip nat statistics
"""

# Python
import re
import random

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Schema,
                                                Any,
                                                Optional,
                                                Or,
                                                And,
                                                Default,
                                                Use)

# import parser utils
from genie.libs.parser.utils.common import Common

from genie.libs.parser.iosxe.show_ip import (ShowIpNatTranslations 
                                                as ShowIpNatTranslationsIosxe,
                                                ShowIpNatStatistics 
                                                as ShowIpNatStatisticsIosxe)


class ShowIpNatTranslations(ShowIpNatTranslationsIosxe):
    """
        * show ip nat translations
        * show ip nat translations verbose
    """

    pass


class ShowIpNatStatistics(ShowIpNatStatisticsIosxe):
    """ Schema for command:
            * show ip nat statistics
    """

    pass


# =======================================
# Schema for 'show ip device tracking all'
# =======================================
class ShowIpDeviceTrackingAllSchema(MetaParser):
    """ 
    Schema for 'show ip device tracking all'
    """

    schema = {
        'state': str,
        'probe_count': int,
        'probe_interval': int,
        'delay_interval': int,
        'total_numb_if_enabled': int,
        'devices': {
            Any(): {
                'mac_address': str,
                'vlan': int,
                'interface': str,
                'state': str,
                Optional('source'): str,
                Optional('probe_timeout'): int,
            }
        }
    }


# =========================================
# Parser for 'show ip device tracking all
# =========================================
class ShowIpDeviceTrackingAll(ShowIpDeviceTrackingAllSchema):
    """
    Parser for 'show ip device tracking all'
    """
    cli_command = 'show ip device tracking all'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}
        # Global IP Device Tracking for clients = Enabled
        p1 = re.compile(r".*=\s(Enabled|Disabled)")
        
        # Global IP Device Tracking Probe Count = 3
        # Global IP Device Tracking Probe Interval = 30
        # Global IP Device Tracking Probe Delay Interval = 0
        p2 = re.compile(r".*=\s(\d+)")
        
        # EXAMPLE (Note: some devices do not have probe-timeout and sources)
        # -----------------------------------------------------------------------------------------------
        #   IP Address    MAC Address   Vlan  Interface           Probe-Timeout      State    Source
        # -----------------------------------------------------------------------------------------------
        #   192.168.178.218 b437.6c25.f929 30   GigabitEthernet0/8     30              ACTIVE   ARP
        p3 = re.compile(
            r"(?P<ip>\b25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b)\s+(?P<mac>([a-fA-F0-9]{4}\.){2}[a-fA-F0-9]{4})\s+(?P<vlan>\d+)\s+(?P<int>\S+)\s+(?P<probe>\d+)?\s+(?P<state>\S+)(\s+)?(?P<source>\S+)?")
        # Total number interfaces enabled: 8
        p4 = re.compile(
            r"(Total number interfaces enabled:)\s(?P<numb>\d+)")

        for line in out.splitlines():
            line = line.strip()
            m1 = p1.match(line)
            
            if m1:
                parsed_dict['state'] = m1.group(1)
                continue

            m2 = p2.match(line)
            if m2:
                if 'Probe Count' in line:
                    parsed_dict['probe_count'] = int(m2.group(1))
                elif 'Probe Interval' in line:
                    parsed_dict['probe_interval'] = int(m2.group(1))
                elif 'Probe Delay Interval' in line:
                    parsed_dict['delay_interval'] = int(m2.group(1))
                continue

            m3 = p3.match(line)
            if m3:
                parsed_dict.setdefault('devices', {}).setdefault(m3.group("ip"),{})
                parsed_dict['devices'][m3.group("ip")] = {}
                parsed_dict['devices'][m3.group("ip")]['interface'] = m3.group("int")
                parsed_dict['devices'][m3.group("ip")]['mac_address'] = m3.group("mac")
                parsed_dict['devices'][m3.group("ip")]['vlan'] = int(m3.group("vlan"))
                parsed_dict['devices'][m3.group("ip")]['state'] = m3.group("state")
                
                # some devices do not have source and probe attribute
                if m3.groupdict().get("source") is not None:
                    parsed_dict['devices'][m3.group("ip")]['source'] = m3.group("source")
                
                if m3.groupdict().get("probe") is not None:
                    parsed_dict['devices'][m3.group("ip")]['probe_timeout'] = int(m3.group("probe"))
                continue

            m4 = p4.match(line)
            if m4:
                parsed_dict['total_numb_if_enabled'] = int(m4.group("numb"))
                continue
        return parsed_dict