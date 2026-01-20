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
            output = self.device.execute(self.cli_command)
        
        parsed_dict = {}
        # Global IP Device Tracking for clients = Enabled
        p1 = re.compile(r".*=\s(Enabled|Disabled)")
        
        # Global IP Device Tracking Probe Count = 3
        p2 = re.compile(r".*\sProbe\sCount\s=\s(\d+)")
        # Global IP Device Tracking Probe Interval = 30
        p3 = re.compile(r".*\sProbe\sInterval\s=\s(\d+)")
        # Global IP Device Tracking Probe Delay Interval = 0
        p4 = re.compile(r".*\sProbe\sDelay\sInterval\s=\s(\d+)")
        
        # EXAMPLE (Note: some devices do not have probe-timeout and sources)
        # -----------------------------------------------------------------------------------------------
        #   IP Address    MAC Address   Vlan  Interface           Probe-Timeout      State    Source
        # -----------------------------------------------------------------------------------------------
        #   192.168.178.218 b437.6c25.f929 30   GigabitEthernet0/8     30              ACTIVE   ARP
        p5 = re.compile(
            r"(?P<ip>\b25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b)\s+(?P<mac>([a-fA-F0-9]{4}\.){2}[a-fA-F0-9]{4})\s+(?P<vlan>\d+)\s+(?P<int>\S+)\s+(?P<probe>\d+)?\s+(?P<state>\S+)(\s+)?(?P<source>\S+)?")
        # Total number interfaces enabled: 8
        p6 = re.compile(
            r"(Total number interfaces enabled:)\s(?P<numb>\d+)")

        for line in output.splitlines():
            line = line.strip()
            # Global IP Device Tracking for clients = Enabled
            m1 = p1.match(line)
            if m1:
                parsed_dict['state'] = m1.group(1)
                continue

            # Global IP Device Tracking Probe Count = 3
            m2 = p2.match(line)
            print(line)
            if m2:
                parsed_dict['probe_count'] = int(m2.group(1))
            
            # Global IP Device Tracking Probe Interval = 30
            m3 = p3.match(line)
            print(m3)
            if m3:
                parsed_dict['probe_interval'] = int(m3.group(1))
            
            # Global IP Device Tracking Probe Delay Interval = 0
            m4 = p4.match(line)
            if m4:
                parsed_dict['delay_interval'] = int(m4.group(1))

            # EXAMPLE (Note: some devices do not have probe-timeout and sources)
            # -----------------------------------------------------------------------------------------------
            #   IP Address    MAC Address   Vlan  Interface           Probe-Timeout      State    Source
            # -----------------------------------------------------------------------------------------------
            #   192.168.178.218 b437.6c25.f929 30   GigabitEthernet0/8     30              ACTIVE   ARP
            m5 = p5.match(line)
            if m5:
                parsed_dict.setdefault('devices', {}).setdefault(m5.group("ip"),{})
                parsed_dict['devices'][m5.group("ip")] = {}
                parsed_dict['devices'][m5.group("ip")]['interface'] = m5.group("int")
                parsed_dict['devices'][m5.group("ip")]['mac_address'] = m5.group("mac")
                parsed_dict['devices'][m5.group("ip")]['vlan'] = int(m5.group("vlan"))
                parsed_dict['devices'][m5.group("ip")]['state'] = m5.group("state")
                
                # some devices do not have source and probe attribute
                if m5.groupdict().get("source") is not None:
                    parsed_dict['devices'][m5.group("ip")]['source'] = m5.group("source")
                
                if m5.groupdict().get("probe") is not None:
                    parsed_dict['devices'][m5.group("ip")]['probe_timeout'] = int(m5.group("probe"))
                continue

            m6 = p6.match(line)
            if m6:
                parsed_dict['total_numb_if_enabled'] = int(m6.group("numb"))
                continue
        print(parsed_dict)
        return parsed_dict