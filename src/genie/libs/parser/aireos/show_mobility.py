""" show_mobility.py

AireOS parser for the following command:
    * 'show mobility'

"""

from queue import PriorityQueue
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# ======================
# Schema for:
#  * 'show mobility summary'
# ======================

class ShowMobilitySummarySchema(MetaParser):
    """Schema for show mobility summary"""

    schema = {
        "mobility_summary": {
            "mobility_domain": str,
            "group_name": {
                str: {
                    "mac_address": str,
                    "ip_address": str,
                    "status": str,
                }
            }
        }
    }
# ======================
# Parser for:
#  * 'show mobility summary'
# ======================

class ShowMobilitySummary(ShowMobilitySummarySchema):
    """Parser for show wlan summary"""

    cli_command = 'show mobility summary'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        mobility_summary_dict = {}

        #Mobility Protocol Port........................... 16666
        #Default Mobility Domain.......................... Centralized-Corp
        #Multicast Mode .................................. Disabled
        #DTLS Mode ....................................... Disabled
        #Mobility Domain ID for 802.11r................... 0xf04f
        #Mobility Keepalive Interval...................... 10
        #Mobility Keepalive Count......................... 3
        #Mobility Group Members Configured................ 4
        #Mobility Control Message DSCP Value.............. 0
        #Mobility Use Profile Name........................ Disabled

        #Controllers configured in the Mobility Group
        #MAC Address        IP Address                                       Group Name                        Multicast IP                                     Status
        #00:27:e3:32:04:eb  172.23.89.99                                     Centralized-Corp                  0.0.0.0                                          Up

        #Mobility Protocol Port........................... 16666
        mobility_protocol_port_capture = re.compile(r"^Mobility\s+Protocol\s+Port\.+ +(?P<protocol_port>\d+)$")
        #Default Mobility Domain.......................... Centralized-Corp
        mobility_domain_capture = re.compile(r"^Default\s+Mobility\s+Domain\.+ +(?P<mobility_domain>\S+)$")
        #Multicast Mode .................................. Disabled
        mobility_header_capture = re.compile(r"^Controllers\s+configured\s+in\s+the\s+Mobility\s+Group$")
        #00:27:e3:32:04:eb  172.23.89.99                                     Centralized-Corp                  0.0.0.0                                          Up
        mobility_info_capture = re.compile(r"^(?P<mac_address>\S+)\s+(?P<ip_address>\S+)\s+(?P<group_name>\S+)\s+(?P<multicast_ip>\S+)\s+(?P<status>\S+)$")
        #Mobility Group Members Configured................ 4
        mobility_members_capture = re.compile(r"^Mobility\s+Group\s+Members\s+Configured\.+ (?P<number>\d+)$")
        #Mobility Use Profile Name........................ Disabled
        mobility_use_name_capture = re.compile(r"^Mobility\s+Use\s+Profile\s+Name\.+ (?P<use>\S+)$")
        
        for line in out.splitlines():
            line = line.strip()
            #Default Mobility Domain.......................... Centralized-Corp
            if mobility_domain_capture.match(line):
                mobility_domain_capture_match = mobility_domain_capture.match(line)
                groups = mobility_domain_capture_match.groupdict()
                if not mobility_summary_dict.get('mobility_summary',{}):
                    mobility_summary_dict['mobility_summary'] = {}
                mobility_domain = groups['mobility_domain']
                mobility_summary_dict['mobility_summary']['mobility_domain'] = mobility_domain
                continue
            #Mobility Group Members Configured................ 4
            elif mobility_members_capture.match(line):
                mobility_members_capture_match = mobility_members_capture.match(line)
                groups = mobility_members_capture_match.groupdict()
                continue
            #Mobility Use Profile Name........................ Disabled
            elif mobility_use_name_capture.match(line):
                mobility_use_name_capture_match = mobility_use_name_capture.match(line)
                groups = mobility_use_name_capture_match.groupdict()
                continue
            #00:27:e3:32:04:eb  172.23.89.99                                     Centralized-Corp                  0.0.0.0                                          Up
            elif mobility_info_capture.match(line):
                mobility_info_capture_match = mobility_info_capture.match(line)
                groups = mobility_info_capture_match.groupdict()
                group_name = groups['group_name']
                mac_address = groups['mac_address']
                ip_address = groups['ip_address']
                status = groups['status']
                if not mobility_summary_dict['mobility_summary'].get('group_name', {}):
                    mobility_summary_dict['mobility_summary']['group_name'] = {}
                mobility_summary_dict['mobility_summary']['group_name'][group_name] = {}
                mobility_summary_dict['mobility_summary']['group_name'][group_name].update({'mac_address': mac_address})
                mobility_summary_dict['mobility_summary']['group_name'][group_name].update({'ip_address': ip_address})
                mobility_summary_dict['mobility_summary']['group_name'][group_name].update({'status': status})
                continue
        
        return mobility_summary_dict


# ======================
# Schema for:
#  * 'show mobility anchor'
# ======================

class ShowMobilityAnchorSchema(MetaParser):
    """Schema for show mobility anchor"""

    schema = {
        "mobility_anchor": {
            "wlan_id": {
                int: {
                    "ip_address": str,
                    "status": str,
                    "priority": int
                }
            }
        }
    }

# ======================
# Parser for:
#  * 'show mobility anchor'
# ======================

class ShowMobilityAnchor(ShowMobilityAnchorSchema):
    """Parser for show mobility anchor"""

    cli_command = 'show mobility anchor'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        mobility_anchor_dict = {}

        #Mobility Anchor Export List
        #
        #Priority number,0=Local Anchor Priority. 1=Highest priority and 3=Lowest priority(default). 
        #
        #WLAN ID     IP Address            Status                            Priority
        # -------     ---------------       ------                            --------
        # 1           172.23.89.35          Control and Data Path Down          1                                    
        #1           172.23.89.99          Up                                  2                                    
        #101          172.23.89.35          Control and Data Path Down          1                                    
        #101          172.23.89.99          Up                                  2                                    
        #106          172.23.89.99          Up                                  3                                    
        #122          172.23.89.35          Control and Data Path Down          3                                    
        #
        #GLAN ID     IP Address            Status

        #101          172.23.89.35          Control and Data Path Down          1 
        anchor_info_capture = re.compile(r"^(?P<wlan_id>\d+)\s+(?P<ip_address>\S+)\s+(?P<status>.*)(?P<priority>\d)$")

        mobility_anchor_data = {}

        for line in out.splitlines():
            line = line.strip()
            #101          172.23.89.35          Control and Data Path Down          1 
            if line.startswith('Mobility'):
                continue
            elif line.startswith('Priority'):
                continue
            elif line.startswith('WLAN ID'):
                continue
            elif line.startswith('GLAN ID'):
                continue
            if anchor_info_capture.match(line):
                anchor_info_capture_match = anchor_info_capture.match(line)
                groups = anchor_info_capture_match.groupdict()
                wlan_id = int(groups['wlan_id'])
                ip_address = groups['ip_address']
                status = groups['status']
                priority = int(groups['priority'])
                if not mobility_anchor_dict.get('mobility_anchor', {}):
                    mobility_anchor_dict['mobility_anchor'] = {}
                    if not mobility_anchor_dict['mobility_anchor'].get('wlan_id', {}):
                        mobility_anchor_dict['mobility_anchor']['wlan_id'] = {}
                mobility_anchor_dict['mobility_anchor']['wlan_id'][wlan_id] = {}
                mobility_anchor_dict['mobility_anchor']['wlan_id'][wlan_id].update({'ip_address': ip_address})
                mobility_anchor_dict['mobility_anchor']['wlan_id'][wlan_id].update({'status': status})
                mobility_anchor_dict['mobility_anchor']['wlan_id'][wlan_id].update({'priority': priority})
                continue

        
        return mobility_anchor_dict
                    



