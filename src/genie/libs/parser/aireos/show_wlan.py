""" show_wlan.py

AireOS parser for the following commands:
    * 'show wlan summary'
    'show wlan {wlan_id}'
    'show wlan apgroups'

"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# ======================
# Schema for:
#  * 'show wlan summary'
# ======================
class ShowWlanSummarySchema(MetaParser):
    """Schema for show wlan summary."""

    schema = {
        "wlan_summary": {
            "wlan_count": int,
            "wlan_id": {
                int: {
                    "profile_name": str,
                    "ssid": str,
                    "status": str,
                    "interface_name": str
                }
            }
        }
    }

# ======================
# Parser for:
#  * 'show wlan summary'
# ======================

class ShowWlanSummary(ShowWlanSummarySchema):
    """Parser for show wlan summary"""

    cli_command = 'show wlan summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        wlan_summary_dict = {}

        #Number of WLANs.................................. 10 

        #WLAN ID  WLAN Profile Name / SSID                                                 Status    Interface Name        PMIPv6 Mobility
        #-------  -----------------------------------------------------------------------  --------  --------------------  ---------------
        #1        CiscoSensorProvisioning / CiscoSensorProvisioning                        Enabled   management            none        
        #101      phsa-staff / phsa-staff                                                  Enabled   management            none        
        #102      vch / vch                                                                Enabled   management            none        
        #103      vch-staff / vch-staff                                                    Enabled   phsa-lab-dec-ssid-subnet-3none

        #Number of WLANs.................................. 10 
        wlan_count_capture = re.compile(r"^Number\s+of\s+WLANs\.+ +(?P<wlan_count>\d+)$")
        #WLAN ID  WLAN Profile Name / SSID                                                 Status    Interface Name        PMIPv6 Mobility
        wlan_info_header_capture = re.compile(r"^WLAN\s+ID\s+WLAN\s+Profile\s+Name\s+\/\s+SSID\s+Status\s+Interface\s+Name\s+PMIPv6\s+Mobility$")
        #-------  -----------------------------------------------------------------------  --------  --------------------  ---------------
        delimiter_capture = re.compile(
            r"-------\s+-----------------------------------------------------------------------\s+--------\s+--------------------\s+---------------$")
        #1        CiscoSensorProvisioning / CiscoSensorProvisioning                        Enabled   management            none        
        wlan_info_capture = re.compile(
            r"^(?P<wlan_id>\d+)\s+(?P<profile_name>\S+)\s\/\s+(?P<ssid>\S+)\s+(?P<status>\S+)\s+(?P<interface_name>\S+)\s+(?P<pmipv6_mobility>\S+)")
        #103      vch-staff / vch-staff                                                    Enabled   phsa-lab-dec-ssid-subnet-3none
        wlan_info_capture_2 = re.compile(r"^(?P<wlan_id>\d+)\s+(?P<profile_name>\S+)\s\/\s+(?P<ssid>\S+)\s+(?P<status>\S+)\s+(?P<interface_name>\S+)none$")

        for line in out.splitlines():
            line = line.strip()
            #Number of WLANs.................................. 10 
            if wlan_count_capture.match(line):
                wlan_count_capture_match = wlan_count_capture.match(line)
                groups = wlan_count_capture_match.groupdict()
                if not wlan_summary_dict.get('wlan_summary', {}):
                   wlan_summary_dict['wlan_summary'] = {}
                wlan_count = int(groups['wlan_count'])
                wlan_summary_dict['wlan_summary']['wlan_count'] = wlan_count 
                continue
            #WLAN ID  WLAN Profile Name / SSID                                                 Status    Interface Name        PMIPv6 Mobility
            elif  wlan_info_header_capture.match(line):
                wlan_info_header_capture_match = wlan_info_header_capture.match(line)
                groups = wlan_info_header_capture_match.groupdict()
                continue
            #-------  -----------------------------------------------------------------------  --------  --------------------  ---------------
            elif delimiter_capture.match(line):
                delimiter_capture_match = delimiter_capture.match(line)
                groups = delimiter_capture_match.groupdict()
                continue
            #1        CiscoSensorProvisioning / CiscoSensorProvisioning                        Enabled   management            none        
            elif wlan_info_capture.match(line):
                wlan_info_capture_match = wlan_info_capture.match(line)
                groups = wlan_info_capture_match.groupdict()
                wlan_id = int(groups['wlan_id'])
                profile_name = groups['profile_name']
                ssid = groups['ssid']
                wlan_status = groups['status']
                interface_name=groups['interface_name']
                if not wlan_summary_dict['wlan_summary'].get('wlan_id', {}):
                    wlan_summary_dict['wlan_summary']['wlan_id'] = {}
                wlan_summary_dict['wlan_summary']['wlan_id'][wlan_id] = {}
                wlan_summary_dict['wlan_summary']['wlan_id'][wlan_id].update({'profile_name': profile_name})
                wlan_summary_dict['wlan_summary']['wlan_id'][wlan_id].update({'ssid': ssid})
                wlan_summary_dict['wlan_summary']['wlan_id'][wlan_id].update({'status': wlan_status})
                wlan_summary_dict['wlan_summary']['wlan_id'][wlan_id].update({'interface_name': interface_name})
                continue
            elif wlan_info_capture_2.match(line):
                wlan_info_capture_2_match = wlan_info_capture_2.match(line)
                groups = wlan_info_capture_2_match.groupdict()
                wlan_id = int(groups['wlan_id'])
                profile_name = groups['profile_name']
                ssid = groups['ssid']
                wlan_status = groups['status']
                interface_name=groups['interface_name']
                if not wlan_summary_dict['wlan_summary'].get('wlan_id', {}):
                    wlan_summary_dict['wlan_summary']['wlan_id'] = {}
                wlan_summary_dict['wlan_summary']['wlan_id'][wlan_id] = {}
                wlan_summary_dict['wlan_summary']['wlan_id'][wlan_id].update({'profile_name': profile_name})
                wlan_summary_dict['wlan_summary']['wlan_id'][wlan_id].update({'ssid': ssid})
                wlan_summary_dict['wlan_summary']['wlan_id'][wlan_id].update({'status': wlan_status})
                wlan_summary_dict['wlan_summary']['wlan_id'][wlan_id].update({'interface_name': interface_name})
                continue

        return wlan_summary_dict

# ======================
# Schema for:
#  * 'show wlan {wlan_id}'
# ======================

class ShowWlanSchema(MetaParser):
    """Schema for show wlan {wlan_id}"""

    schema = {
        "wlan_id": {
            int: {
                "wlan_identifier": int,
                "profile_name": str,
                "network_name": str,
                "status": str,
                "broadcast_ssid": str,
                "aaa_policy_override": str,
                "interface_name": str,
                "session_timeout":str,
                "exclusionlist_timeout": str,
                "user_idle_timeout": str,
                "quality_of_service": str,
                "dhcp_server": str,
                "wmm": str,
                "passive_client_feature": str,
                "Radius_servers": {
                    "authentication_server_1": str,
                    Optional("authentication_server_2"): str,
                    "accounting_server_1": str, 
                    Optional("accounting_server_2"): str},
                "80211_authentication": str,
                "802.1x": str, 
                "flexconnect_local_switching": str
            }
        }
    }

# ======================
# Parser for:
#  * 'show wlan {wlan_id}'
# ======================

class ShowWlan(ShowWlanSchema):
    """Parser for show wlan {wlan_id}"""

    cli_command = 'show wlan {wlan_id}'

    def cli(self, wlan_id="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(wlan_id=wlan_id))
        else:
            output = output
        
        wlan_dict = {}

        #WLAN Identifier.................................. 101
        #Profile Name..................................... phsa-staff
        #Network Name (SSID).............................. phsa-staff
        #Status........................................... Enabled
        #Broadcast SSID................................... Enabled
        #AAA Policy Override.............................. Enabled
        #Interface........................................ phsa-lab-kdc-dc-ssid-subnet-1
        #Session Timeout.................................. 1800 seconds
        #User Idle Timeout................................ Disabled
        #Exclusionlist Timeout............................ 180 seconds
        #Quality of Service............................... Silver
        #DHCP Server...................................... Default
        #WMM.............................................. Allowed
        #Passive Client Feature........................... Disabled
        #Radius Servers
        #Authentication................................ 172.23.89.193 1812 *
        #Authentication................................ 172.23.89.201 1812 *
        #Accounting.................................... 172.23.89.193 1813 *
        #Accounting.................................... 172.23.89.201 1813 *
        #802.11 Authentication:........................ Open System
        #802.1X........................................ Disabled
        #FlexConnect Local Switching................... Enabled

        p1 = re.compile(r"^WLAN\s+Identifier\.+\s(?P<wlan_id>\d+)$")
        p2 = re.compile(r"^Profile\s+Name\.+\s(?P<profile_name>\S+)$")
        p3 = re.compile(r"^Network\s+Name\s\(SSID\)\.+\s(?P<network_name>\S+)")
        p4 = re.compile(r"^Status\.+\s(?P<status>\S+)")
        p5 = re.compile(r"^Broadcast\sSSID\.+\s(?P<broadcast_ssid>\S+)$")
        p6 = re.compile(r"^AAA\sPolicy\sOverride\.+\s(?P<aaa_policy>\S+)$")
        p7 = re.compile(r"^Interface\.+\s(?P<interface_name>\S+)$")
        p8 = re.compile(r"^Session\sTimeout\.+\s(?P<session_timeout>.*)$")
        p9 = re.compile(r"^User\sIdle\sTimeout\.+\s(?P<user_idle_timeout>.*)$")
        p10 = re.compile(r"^Exclusionlist\sTimeout\.+\s(?P<exclusionlist_timeout>.*)$")
        p11 = re.compile(r"^Quality\sof\sService\.+\s(?P<qos>.*)$")
        p12 = re.compile(r"^DHCP\sServer\.+\s(?P<dhcp_server>.*)$")
        p13 = re.compile(r"^WMM\.+\s(?P<wmm>.*)$")
        p14 = re.compile(r"^Passive\sClient\sFeature\.+\s(?P<passive_client>.*)$")
        p15 = re.compile(r"^Radius\sServers")
        p16 = re.compile(r"^Authentication\.+\s(?P<authentication_server1>.*)$")
        p17 = re.compile(r"^Authentication\.+\s(?P<authentication_server2>\S+).1812\s\*$")
        p18 = re.compile(r"^Accounting\.+\s(?P<accounting_server1>.*)$")
        p19 = re.compile(r"^Accounting\.+\s(?P<accounting_server2>\S+).1813\s\*$")
        p20 = re.compile(r"^802.11\sAuthentication:\.+\s(?P<a80211_authentication>.*)$")
        p21 = re.compile(r"^802.1X\.+\s(?P<a802x>.*)$")
        p22 = re.compile(r"^FlexConnect\sLocal\sSwitching\.+\s(?P<flexconnect_local_switching>.*)$")
        p23 = re.compile(r"^Exclusionlist\.+\s(?P<exclusionlist>.*)$")

        for line in output.splitlines():
            line = line.strip()

            if p1.match(line):
                match = p1.match(line)
                groups = match.groupdict()
                wlan_id = int(groups['wlan_id'])
                if not wlan_dict.get('wlan_id', {}):
                    wlan_dict['wlan_id'] = {}
                wlan_dict['wlan_id'].update({wlan_id: {}})
                wlan_dict['wlan_id'][wlan_id].update({"wlan_identifier": wlan_id })
                continue
            elif p2.match(line):
                match = p2.match(line)
                wlan_dict['wlan_id'][wlan_id].update({"profile_name": match.group("profile_name") })
                continue
            elif p3.match(line):
                match = p3.match(line)
                wlan_dict['wlan_id'][wlan_id].update({"network_name": match.group("network_name") })
                continue
            elif p4.match(line):
                match = p4.match(line)
                wlan_dict['wlan_id'][wlan_id].update({"status": match.group("status") })
                continue
            elif p5.match(line):
                match = p5.match(line)
                wlan_dict['wlan_id'][wlan_id].update({"broadcast_ssid": match.group("broadcast_ssid") })
                continue
            elif p6.match(line):
                match = p6.match(line)
                wlan_dict['wlan_id'][wlan_id].update({"aaa_policy_override": match.group("aaa_policy") })
                continue
            elif p7.match(line):
                match = p7.match(line)
                wlan_dict['wlan_id'][wlan_id].update({"interface_name": match.group("interface_name") })
                continue
            elif p8.match(line):
                match = p8.match(line)
                wlan_dict['wlan_id'][wlan_id].update({"session_timeout": match.group("session_timeout") })
                continue
            elif p9.match(line):
                match = p9.match(line)
                wlan_dict['wlan_id'][wlan_id].update({"user_idle_timeout": match.group("user_idle_timeout") })
                continue
            elif p10.match(line):
                match = p10.match(line)
                wlan_dict['wlan_id'][wlan_id].update({"exclusionlist_timeout": match.group("exclusionlist_timeout") })
                continue
            elif p11.match(line):
                match = p11.match(line)
                wlan_dict['wlan_id'][wlan_id].update({"quality_of_service": match.group("qos") })
                continue
            elif p12.match(line):
                match = p12.match(line)
                wlan_dict['wlan_id'][wlan_id].update({"dhcp_server": match.group("dhcp_server") })
                continue
            elif p13.match(line):
                match = p13.match(line)
                wlan_dict['wlan_id'][wlan_id].update({"wmm": match.group("wmm") })
                continue
            elif p14.match(line):
                match = p14.match(line)
                wlan_dict['wlan_id'][wlan_id].update({"passive_client_feature": match.group("passive_client") })
                continue
            elif p15.match(line):
                match = p15.match(line)
                if not wlan_dict['wlan_id'][wlan_id].get('Radius_servers', {}):
                    wlan_dict['wlan_id'][wlan_id]['Radius_servers'] = {}
                continue
            elif p16.match(line):
                match = p16.match(line)
                wlan_dict['wlan_id'][wlan_id]['Radius_servers'] .update({"authentication_server_1": match.group("authentication_server1") })
                continue
            elif p17.match(line):
                match = p17.match(line)
                wlan_dict['wlan_id'][wlan_id]['Radius_servers'] .update({"authentication_server_2": match.group("authentication_server2") })
                continue
            elif p18.match(line):
                match = p18.match(line)
                wlan_dict['wlan_id'][wlan_id]['Radius_servers'] .update({"accounting_server_1": match.group("accounting_server1") })
                continue
            elif p19.match(line):
                match = p19.match(line)
                wlan_dict['wlan_id'][wlan_id]['Radius_servers'] .update({"accounting_server_2": match.group("accounting_server2") })
                continue
            elif p20.match(line):
                match = p20.match(line)
                wlan_dict['wlan_id'][wlan_id].update({"80211_authentication": match.group("a80211_authentication") })
                continue
            elif p21.match(line):
                match = p21.match(line)
                wlan_dict['wlan_id'][wlan_id].update({"802.1x": match.group("a802x") })
                continue
            elif p22.match(line):
                match = p22.match(line)
                wlan_dict['wlan_id'][wlan_id].update({"flexconnect_local_switching": match.group("flexconnect_local_switching") })
                continue
            elif p23.match(line):
                match = p23.match(line)
                wlan_dict['wlan_id'][wlan_id].update({"exclusionlist_timeout": match.group("exclusionlist")})
                continue

        return wlan_dict


# ======================
# Schema for:
#  * 'show wlan apgroups'
# ======================

class ShowWlanApgroupsSchema(MetaParser):
    """Schema for show wlan apgroups"""

    schema = {
        "ap_group_count": int,
        "ap_group": {
            str: {
                "site_name": str,
                "site_description": str,
                "2.4_ghz_band": str,
                "5.0_ghz_band": str,
                "wlan_id": {
                    int: {
                       "interface_name": str 
                    }
                }
            }
        }
    }

# ======================
# Parser for:
#  * 'show wlan apgroups'
# ======================

class ShowWlanApgroups(ShowWlanApgroupsSchema):
    """Parser for show wlan apgroups"""

    cli_command = 'show wlan apgroups'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        wlan_apgroup_dict = {}

        #Total Number of AP Groups........................ 4 
        #
        #Site Name........................................ AP-Group-LAB
        #Site Description................................. test
        #Venue Group Code................................. Unspecified
        #Venue Type Code.................................. Unspecified
        #
        #RF Profile
        #----------
        #2.4 GHz band..................................... Data-BG
        #5 GHz band....................................... Data-AC

        #WLAN ID          Interface          Network Admission Control          Radio Policy        OpenDnsProfile
        #-------          -----------        --------------------------         ------------         --------------
        #102             phsa-lab-cw-dc-ssid-subnet-5Disabled                          None                        None
        #131             management           Disabled                          None                        None
        #101             management           Disabled                          None                

        p1 = re.compile(r"^Total\sNumber\sof\sAP\sGroups\.+\s(?P<no_of_groups>\d+)")
        p2 = re.compile(r"^Site\sName\.+\s(?P<site_name>\S+)$")
        p3 = re.compile(r"^Site\sDescription\.+\s(?P<site_description>.*)$")
        p4 = re.compile(r"^2.4\sGHz\sband\.+\s(?P<profile_name_24>\S+)")
        p5 = re.compile(r"^5\sGHz\sband\.+\s(?P<profile_name_5>\S+)")
        p6 = re.compile(r"^(?P<wlan_id>\d+)\s+(?P<interface_name>\S+)\s+(?P<admin_control>\S+)\s+(?P<network_policy>\S+)\s+(?P<dns_profile>\S+)")

        for line in out.splitlines():
            line = line.strip()

            if p1.match(line):
                match = p1.match(line)
                groups = match.groupdict()
                ap_group_count = int(groups['no_of_groups'])
                wlan_apgroup_dict["ap_group_count"] = ap_group_count
                continue
            elif p2.match(line):
                match = p2.match(line)
                groups = match.groupdict()
                site_name = groups['site_name']
                if not wlan_apgroup_dict.get('ap_group', {}):
                    wlan_apgroup_dict['ap_group'] = {}
                wlan_apgroup_dict['ap_group'].update({site_name: {}})
                wlan_apgroup_dict['ap_group'][site_name].update({"site_name": site_name})
                continue
            elif p3.match(line):
                match = p3.match(line)
                wlan_apgroup_dict['ap_group'][site_name].update({"site_description":match.group("site_description") })
                continue
            elif p4.match(line):
                match = p4.match(line)
                wlan_apgroup_dict['ap_group'][site_name].update({"2.4_ghz_band":match.group("profile_name_24") })
                continue
            elif p5.match(line):
                match = p5.match(line)
                wlan_apgroup_dict['ap_group'][site_name].update({"5.0_ghz_band":match.group("profile_name_5") })
                continue
            elif p6.match(line):
                match = p6.match(line)
                groups = match.groupdict()
                wlan_id = int(groups['wlan_id'])
                interface_name = groups['interface_name']
                if not wlan_apgroup_dict['ap_group'][site_name].get('wlan_id', {}):
                    wlan_apgroup_dict['ap_group'][site_name]['wlan_id'] = {}
                wlan_apgroup_dict['ap_group'][site_name]['wlan_id'][wlan_id] = {}
                wlan_apgroup_dict['ap_group'][site_name]['wlan_id'][wlan_id].update({'interface_name': interface_name})
                continue

        return wlan_apgroup_dict
