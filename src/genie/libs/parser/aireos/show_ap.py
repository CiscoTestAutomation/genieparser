""" show_ap.py

AireOS parser for the following commands:
    * 'show ap summary'
    'show ap config general {ap_name}'

"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# ======================
# Schema for:
#  * 'show ap summary'
# ======================
class ShowApSummarySchema(MetaParser):
    """Schema for show ap summary."""

    schema = {
        "ap_count": int,
        "ap_name": {
            str: {
                "slots_count": int,
                "ap_model": str,
                "ethernet_mac": str,
                "location": str,
                "country": str,
                "ap_ip_address": str,
                "clients_count": int
            }
        }
    }

# ====================
# Parser for:
#  * 'show ap summary'
# ====================
class ShowApSummary(ShowApSummarySchema):
    """Parser for show ap summary"""

    cli_command = 'show ap summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        ap_summary_dict = {}
        #Number of APs.................................... 3
        #
        #Global AP User Name.............................. TELUS_AP
        #Global AP Dot1x User Name........................ Not Configured
        #Global AP Dot1x EAP Method....................... EAP-FAST
        #
        #AP Name                         Slots  AP Model              Ethernet MAC       Location              Country     IP Address       Clients  DSE Location  
        #------------------------------  -----  --------------------  -----------------  --------------------  ----------  ---------------  -------  --------------
        #PLAB-AP3802-2                   3      AIR-AP3802I-A-K9       00:27:e3:89:21:00  default location      CA          10.253.31.126    0        [0 ,0 ,0 ]
        #PLAB-AP9130-2                   3      C9130AXI-A             3c:41:0e:fe:4f:f4  default location      CA          10.253.31.5      0        [0 ,0 ,0 ]
        #PLAB-AP9120-2                   2      C9120AXI-A             a4:b4:39:2f:08:dc  default location      CA          10.253.31.3      0        [0 ,0 ,0 ]

        #Number of APs.................................... 3
        ap_count_capture = re.compile(r"^Number\s+of\s+APs\.+ +(?P<ap_count>\d+)$")

        #PLAB-AP3802-2                   3      AIR-AP3802I-A-K9       00:27:e3:89:21:00  default location      CA          10.253.31.126    0        [0 ,0 ,0 ]
        ap_info_capture = re.compile(
            r"^(?P<ap_name>\S+)\s+(?P<slots_count>\d+)\s+(?P<ap_model>\S+)\s+"
            "(?P<ethernet_mac>\S+)\s+(?P<location>.*)\s+(?P<country>\S+)\s+"
            "(?P<ap_ip_address>\d+\.\d+\.\d+\.\d+)\s+(?P<clients_count>\d+)\s+\[0 ,0 ,0 \]$")

        remove_lines = ('AP Name', '----')

        # Remove unwanted lines from raw text
        def filter_lines(raw_output, remove_lines):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            rendered_lines = []
            for clean_line in clean_lines:
                clean_line_strip = clean_line.strip()
                # Remove lines unwanted lines from list of "remove_lines"
                if not clean_line_strip.startswith(remove_lines):
                    rendered_lines.append(clean_line_strip)
            return rendered_lines  

        out_filter = filter_lines(raw_output=out, remove_lines=remove_lines)

        ap_summary_data = {}     

        for line in out_filter:
            # Number of APs: 149
            if ap_count_capture.match(line):
                ap_count_match = ap_count_capture.match(line)
                groups = ap_count_match.groupdict()
                ap_count = int(groups['ap_count'])
                ap_summary_dict['ap_count'] = ap_count         
            #PLAB-AP3802-2                   3      AIR-AP3802I-A-K9       00:27:e3:89:21:00  default location      CA          10.253.31.126    0        [0 ,0 ,0 ]
            elif ap_info_capture.match(line):
                ap_info_capture_match = ap_info_capture.match(line)
                groups = ap_info_capture_match.groupdict()
                # ap name is the key to place all the ap neighbor info
                ap_name = ''
                # Loop over all regex matches found
                for k,v in groups.items():
                    if k == 'ap_name':
                        ap_name = v
                    else:
                        if k != 'ap_model' and v.isdigit():
                            v = int(v)
                        elif str(v):
                            v = v.strip()
                        if not ap_summary_dict.get("ap_name", {}):
                            ap_summary_dict["ap_name"] = {}
                        ap_summary_dict['ap_name'][ap_name] = {}
                        ap_summary_data.update({k: v})
                ap_summary_dict['ap_name'][ap_name].update(ap_summary_data)
                ap_summary_data = {}
                continue

        return ap_summary_dict


# ======================
# Schema for:
#  * 'show ap config general [ap_name]'
# ======================

class ShowApConfigGeneralSchema(MetaParser):
    """Schema for show ap config general {ap_name}"""

    schema = {
        "ap_name": {
            str: {
                "ap_country_code": str,
                "ap_ip_address": str,
                "ap_group": str,
                "primary_cisco_switch_name": str,
                Optional("secondary_cisco_switch_name"): str,
                "primary_cisco_switch_ip_address": str,
                Optional("secondary_cisco_switch_ip_address"): str,
                "power_type":str,
                "ap_mode": str,
                "led_state": str,
                "ap_version": str,
                "ap_serial": str,
            }
        }
    }

# ======================
# Parser for:
#  * 'show ap config general {ap_name}'
# ======================

class ShowApConfigGeneral(ShowApConfigGeneralSchema):
    """Parser for show ap config general {ap_name}"""

    cli_command = 'show ap config general {ap_name}'

    def cli(self, ap_name="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(ap_name=ap_name))
        else:
            output = output

        ap_config_dict = {}

        #Cisco AP Name.................................... PLAB-AP9120-2
        #AP Country code.................................. CA - Canada
        #IP Address....................................... 10.253.31.3
        #Cisco AP Group Name.............................. AP-Group-LAB
        #Primary Cisco Switch Name........................ PLAB-CW-WLC-01
        #Primary Cisco Switch IP Address.................. 172.23.89.35
        #Secondary Cisco Switch Name...................... 
        #Secondary Cisco Switch IP Address................ Not Configured
        #AP Mode ......................................... FlexConnect
        #AP Model......................................... C9120AXI-A
        #IOS Version...................................... 8.10.162.0
        #LED State........................................ Enabled
        #Power Type/Mode.................................. PoE/Full Power
        #AP Serial Number................................. FJC242316HS

        p1 = re.compile(r"^Cisco\sAP\sName\.+\s(?P<cisco_ap_name>\S+)$")
        p2 = re.compile(r"^AP\sCountry\scode\.+\s(?P<ap_country_code>.*)$")
        p3 = re.compile(r"^IP\sAddress\.+\s(?P<ap_ip_address>\S+)$")
        p4 = re.compile (r"^Cisco\sAP\s+Group\sName.+\s(?P<ap_group>\S+)$")
        p5 = re.compile (r"^Primary\sCisco\s+Switch\sName.+\s(?P<pri_wlc_name>\S+)$")
        p6 = re.compile (r"^Primary\sCisco\s+Switch\sIP\sAddress.+\s(?P<pri_wlc_ip>\S+)$")
        p7 = re.compile (r"^Secondary\sCisco\s+Switch\sName.+\s(?P<sec_wlc_name>\S+)$")
        p8 = re.compile (r"^Secondary\sCisco\s+Switch\sIP\sAddress\.+\s+(?P<sec_wlc_ip>.*)$")
        p9 = re.compile (r"^AP\sMode\s\.+\s(?P<ap_mode>\S+)$")
        p10 = re.compile(r"^AP\sModel\s\.+\s(?P<ap_model>\S+)$")
        p11 = re.compile(r"^IOS\sVersion.+\s(?P<ap_version>\S+)$")
        p12 = re.compile(r"^LED\sState.+\s(?P<led_state>\S+)$")
        p13 = re.compile(r"^Power\sType\/Mode\.+\s(?P<power_type>.*)$")
        p14 = re.compile(r"^AP\sSerial\sNumber\.+\s(?P<ap_serial>\S+)$")

        for line in output.splitlines():
            line = line.strip()

            if p1.match(line):
                match = p1.match(line)
                groups = match.groupdict()
                ap_name = groups['cisco_ap_name']
                if not ap_config_dict.get('ap_name', {}):
                    ap_config_dict['ap_name'] = {}
                ap_config_dict['ap_name'].update({ap_name: {}})
                continue
            elif p2.match(line):
                match = p2.match(line)
                ap_config_dict['ap_name'][ap_name].update({"ap_country_code": match.group("ap_country_code")})
                continue
            elif p3.match(line):
                match = p3.match(line)
                ap_config_dict['ap_name'][ap_name].update({"ap_ip_address": match.group("ap_ip_address")})
                continue
            elif p4.match(line):
                match = p4.match(line)
                ap_config_dict['ap_name'][ap_name].update({"ap_group": match.group("ap_group")})
                continue
            elif p5.match(line):
                match = p5.match(line)
                ap_config_dict['ap_name'][ap_name].update({"primary_cisco_switch_name": match.group("pri_wlc_name")})
                continue
            elif p6.match(line):
                match = p6.match(line)
                ap_config_dict['ap_name'][ap_name].update({"primary_cisco_switch_ip_address": match.group("pri_wlc_ip")})
                continue
            elif p7.match(line):
                match = p7.match(line)
                ap_config_dict['ap_name'][ap_name].update({"secondary_cisco_switch_name": match.group("sec_wlc_name")})
                continue
            elif p8.match(line):
                match = p8.match(line)
                ap_config_dict['ap_name'][ap_name].update({"secondary_cisco_switch_ip_address": match.group("sec_wlc_ip")})
                continue
            elif p9.match(line):
                match = p9.match(line)
                ap_config_dict['ap_name'][ap_name].update({"ap_mode": match.group("ap_mode")})
                continue
            elif p10.match(line):
                match = p10.match(line)
                ap_config_dict['ap_name'][ap_name].update({"ap_model": match.group("ap_model")})
                continue
            elif p11.match(line):
                match = p11.match(line)
                ap_config_dict['ap_name'][ap_name].update({"ap_version": match.group("ap_version")})
                continue
            elif p12.match(line):
                match = p12.match(line)
                ap_config_dict['ap_name'][ap_name].update({"led_state": match.group("led_state")})
                continue
            elif p13.match(line):
                match = p13.match(line)
                ap_config_dict['ap_name'][ap_name].update({"power_type": match.group("power_type")})
                continue
            elif p14.match(line):
                match = p14.match(line)
                ap_config_dict['ap_name'][ap_name].update({"ap_serial": match.group("ap_serial")})
                continue

        return ap_config_dict


                    

















