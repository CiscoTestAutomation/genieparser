""" show_rf-profile.py

AireOS parser for the following command:
    * 'show rf-profile summary'
    'show rf-profile details {rf-profile}'

"""

from multiprocessing import connection
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# ======================
# Schema for:
#  * 'show rf-profile summary'
# ======================
class ShowRfProfileSummarySchema(MetaParser):
    """Schema for show rf-profile summary."""

    schema = {
        "rf_profiles_count": int,
        "rf_profiles": {
            str: {
                "rf_profile_name": str,
                "band": str,
                "description": str,
                "status": str,
                "applied": str
            }
        }
    }

# ====================
# Parser for:
#  * 'show rf-profile summary'
# ====================
class ShowRfProfileSummary(ShowRfProfileSummarySchema):
    """Parser for show rf-profile summary"""

    cli_command = 'show rf-profile summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        rf_profile_summary_dict = {}

        #Number of RF Profiles............................ 12
        #
        #Out Of Box State................................. Disabled
        #
        #Out Of Box Persistence........................... Disabled
        #
        #RF Profile Name                    Band     Description                          11n-client-only     Applied  
        #---------------------------------  -------  -----------------------------------  ------------------  ----------
        #Data-AC                            5 GHz    <none>                               disable             Yes       
        #Data-BG                            2.4 GHz  <none>                               disable             Yes       
        #High-Client-Density-802.11a        5 GHz    <none>                               disable             No  

        #Number of RF Profiles............................ 12
        rf_profile_count_capture = re.compile(r"^Number\sof\sRF\sProfiles\.+\s(?P<rf_profiles_count>\d+)$")

        #Data-BG                            2.4 GHz  <none>                               disable             Yes 
        rf_profile_info_capture = re.compile(r"^(?P<rf_profile_name>\S+)\s+(?P<band>\S+\s+\S+)\s+<(?P<description>\S+)>\s+(?P<status>\S+)\s+(?P<applied>\S+)$")

        remove_lines = ('Out Of', 'RF Profile', '----')   

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

        rf_profile_data = {}

        for line in out_filter:
            #Number of RF Profiles............................ 12
            if rf_profile_count_capture.match(line):
                rf_profile_count_capture_match = rf_profile_count_capture.match(line)
                groups = rf_profile_count_capture_match.groupdict()
                rf_profiles_count = int(groups['rf_profiles_count'])
                rf_profile_summary_dict['rf_profiles_count'] = rf_profiles_count
            #Data-BG                            2.4 GHz  <none>                               disable             Yes 
            elif  rf_profile_info_capture.match(line):
                rf_profile_info_capture_match = rf_profile_info_capture.match(line)
                groups = rf_profile_info_capture_match.groupdict()
                rf_profile_name = ''
                for k,v in groups.items():
                    if k == 'rf_profile_name':
                        rf_profile_name = v
                    v = v.strip()
                    if not rf_profile_summary_dict.get('rf_profiles', {}):
                        rf_profile_summary_dict['rf_profiles'] = {}
                    rf_profile_summary_dict['rf_profiles'][rf_profile_name] = {}
                    rf_profile_data.update({k: v})
                rf_profile_summary_dict['rf_profiles'][rf_profile_name].update(rf_profile_data)
                rf_profile_data = {}
                continue

        return rf_profile_summary_dict 

# ======================
# Schema for:
#  * 'show rf-profile details {rf-profile}'
# ======================
class ShowRfProfileDetailsSchema(MetaParser):
    """Schema for show rf-profile details {rf-profile}"""

    schema = {
        "rf_profile_details": {
            str: {
                'min_transmit_power': str,
                'max_transmit_power': str,
                'operational_rates': {
                    str: {
                        Optional('802.11b/g_1m_rate'): str,
                        Optional('802.11b/g_2m_rate'): str,
                        Optional('802.11b/g_5.5m_rate'): str,
                        Optional('802.11b/g_11m_rate'): str,
                        Optional('802.11a_6m_rate'): str,
                        Optional('802.11g_6m_rate'): str,
                        Optional('802.11a_9m_rate'): str,
                        Optional('802.11g_9m_rate'): str,
                        Optional('802.11a_12m_rate'): str,
                        Optional('802.11g_12m_rate'): str,
                        Optional('802.11a_18m_rate'): str,
                        Optional('802.11g_18m_rate'): str,
                        Optional('802.11a_24m_rate'): str,
                        Optional('802.11g_24m_rate'): str,
                        Optional('802.11a_36m_rate'): str,
                        Optional('802.11g_36m_rate'): str,
                        Optional('802.11a_48m_rate'): str,
                        Optional('802.11g_48m_rate'): str,
                        Optional('802.11a_54m_rate'): str,
                        Optional('802.11g_54m_rate'): str,
                    }
                }
            }
        }
    }
# ======================
# Parser for:
#  * 'show rf-profile details {rf-profile}'
# ======================

class ShowRfProfileDetails(ShowRfProfileDetailsSchema):
    """Parser for show rf-profile details {rf-profile}"""

    cli_command = 'show rf-profile details {rf_profile}'

    def cli(self, rf_profile="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(rf_profile=rf_profile))
        else:
            output = output
        
        rf_profile_details_dict = {}

        #Description...................................... <none>
        #AP Group Name.................................... AP-Group-LAB
        #Radio policy..................................... 5 GHz
        #11n-client-only.................................. disabled
        #Transmit Power Threshold v1...................... -70 dBm
        #Transmit Power Threshold v2...................... -67 dBm
        #Min Transmit Power............................... 11 dBm
        #Max Transmit Power............................... 17 dBm
        #802.11a Operational Rates
        #802.11a 6M Rate.............................. Disabled
        #802.11a 9M Rate.............................. Disabled
        #802.11a 12M Rate............................. Disabled
        #802.11a 18M Rate............................. Disabled
        #802.11a 24M Rate............................. Mandatory
        #802.11a 36M Rate............................. Supported
        #802.11a 48M Rate............................. Supported
        #802.11a 54M Rate............................. Supported

        p1 = re.compile(r"^Min\sTransmit\sPower\.+\s(?P<min_power>.*)")
        p2 = re.compile(r"^Max\sTransmit\sPower\.+\s(?P<max_power>.*)")
        p3 = re.compile(r"^(?P<band_type>.*)\sOperational\sRates")
        p4 = re.compile(r"^802.11a\s6M\sRate\.+\s(?P<a6m_rate>\S+)")
        p5 = re.compile(r"^802.11a\s9M\sRate\.+\s(?P<a9m_rate>\S+)")
        p6 = re.compile(r"^802.11a\s12M\sRate\.+\s(?P<a12m_rate>\S+)")
        p7 = re.compile(r"^802.11a\s18M\sRate\.+\s(?P<a18m_rate>\S+)")
        p8 = re.compile(r"^802.11a\s24M\sRate\.+\s(?P<a24m_rate>\S+)")
        p9 = re.compile(r"^802.11a\s36M\sRate\.+\s(?P<a36m_rate>\S+)")
        p10 = re.compile(r"^802.11a\s48M\sRate\.+\s(?P<a48m_rate>\S+)")
        p11 = re.compile(r"^802.11a\s54M\sRate\.+\s(?P<a54m_rate>\S+)")
        p12 = re.compile(r"^802.11b\/g\s1M\sRate\.+\s(?P<bg_1m_rate>\S+)")
        p13 = re.compile(r"^802.11b\/g\s2M\sRate\.+\s(?P<bg_2m_rate>\S+)")
        p14 = re.compile(r"^802.11b\/g\s55M\sRate\.+\s(?P<bg_55m_rate>\S+)")
        p15 = re.compile(r"^802.11b\/g\s11M\sRate\.+\s(?P<bg_11m_rate>\S+)")
        p16 = re.compile(r"^802.11g\s6M\sRate\.+\s(?P<g6m_rate>\S+)")
        p17 = re.compile(r"^802.11g\s9M\sRate\.+\s(?P<g9m_rate>\S+)")
        p18 = re.compile(r"^802.11g\s12M\sRate\.+\s(?P<g12m_rate>\S+)")
        p19 = re.compile(r"^802.11g\s18M\sRate\.+\s(?P<g18m_rate>\S+)")
        p20 = re.compile(r"^802.11g\s24M\sRate\.+\s(?P<g24m_rate>\S+)")
        p21 = re.compile(r"^802.11g\s36M\sRate\.+\s(?P<g36m_rate>\S+)")
        p22 = re.compile(r"^802.11g\s48M\sRate\.+\s(?P<g48m_rate>\S+)")
        p23 = re.compile(r"^802.11g\s54M\sRate\.+\s(?P<g54m_rate>\S+)")

        for line in output.splitlines():
            line = line.strip()

            if p1.match(line):
                match = p1.match(line)
                groups = match.groupdict()
                min_transmit_power = groups['min_power']
                if not rf_profile_details_dict.get('rf_profile_details', {}):
                    rf_profile_details_dict['rf_profile_details'] = {}
                rf_profile_details_dict['rf_profile_details'].update({rf_profile: {}})
                rf_profile_details_dict['rf_profile_details'][rf_profile].update({"min_transmit_power": min_transmit_power})
                continue
            elif p2.match(line):
                match = p2.match(line)
                groups = match.groupdict()
                max_transmit_power = groups['max_power']
                rf_profile_details_dict['rf_profile_details'][rf_profile].update({"max_transmit_power": max_transmit_power})
                continue
            elif p3.match(line):
                match = p3.match(line)
                groups = match.groupdict()
                band = groups['band_type']
                if not rf_profile_details_dict['rf_profile_details'][rf_profile].get('operational_rates', {}):
                    rf_profile_details_dict['rf_profile_details'][rf_profile]['operational_rates'] = {}
                rf_profile_details_dict['rf_profile_details'][rf_profile]['operational_rates'].update({band: {}})
                continue
            elif p4.match(line):
                match = p4.match(line)
                rf_profile_details_dict['rf_profile_details'][rf_profile]['operational_rates'][band].update({"802.11a_6m_rate": match.group("a6m_rate")})
                continue
            elif p5.match(line):
                match = p5.match(line)
                rf_profile_details_dict['rf_profile_details'][rf_profile]['operational_rates'][band].update({"802.11a_9m_rate": match.group("a9m_rate")})
                continue
            elif p6.match(line):
                match = p6.match(line)
                rf_profile_details_dict['rf_profile_details'][rf_profile]['operational_rates'][band].update({"802.11a_12m_rate": match.group("a12m_rate")})
                continue
            elif p7.match(line):
                match = p7.match(line)
                rf_profile_details_dict['rf_profile_details'][rf_profile]['operational_rates'][band].update({"802.11a_18m_rate": match.group("a18m_rate")})
                continue
            elif p8.match(line):
                match = p8.match(line)
                rf_profile_details_dict['rf_profile_details'][rf_profile]['operational_rates'][band].update({"802.11a_24m_rate": match.group("a24m_rate")})
                continue
            elif p9.match(line):
                match = p9.match(line)
                rf_profile_details_dict['rf_profile_details'][rf_profile]['operational_rates'][band].update({"802.11a_36m_rate": match.group("a36m_rate")})
                continue
            elif p10.match(line):
                match = p10.match(line)
                rf_profile_details_dict['rf_profile_details'][rf_profile]['operational_rates'][band].update({"802.11a_48m_rate": match.group("a48m_rate")})
                continue
            elif p11.match(line):
                match = p11.match(line)
                rf_profile_details_dict['rf_profile_details'][rf_profile]['operational_rates'][band].update({"802.11a_54m_rate": match.group("a54m_rate")})
                continue
            elif p12.match(line):
                match = p12.match(line)
                rf_profile_details_dict['rf_profile_details'][rf_profile]['operational_rates'][band].update({"802.11b/g_1m_rate": match.group("bg_1m_rate")})
                continue
            elif p13.match(line):
                match = p13.match(line)
                rf_profile_details_dict['rf_profile_details'][rf_profile]['operational_rates'][band].update({"802.11b/g_2m_rate": match.group("bg_2m_rate")})
                continue
            elif p14.match(line):
                match = p14.match(line)
                rf_profile_details_dict['rf_profile_details'][rf_profile]['operational_rates'][band].update({"802.11b/g_5.5m_rate": match.group("bg_55m_rate")})
                continue
            elif p15.match(line):
                match = p15.match(line)
                rf_profile_details_dict['rf_profile_details'][rf_profile]['operational_rates'][band].update({"802.11b/g_11m_rate": match.group("bg_11m_rate")})
                continue
            elif p16.match(line):
                match = p16.match(line)
                rf_profile_details_dict['rf_profile_details'][rf_profile]['operational_rates'][band].update({"802.11g_6m_rate": match.group("g6m_rate")})
                continue
            elif p17.match(line):
                match = p17.match(line)
                rf_profile_details_dict['rf_profile_details'][rf_profile]['operational_rates'][band].update({"802.11g_9m_rate": match.group("g9m_rate")})
                continue
            elif p18.match(line):
                match = p18.match(line)
                rf_profile_details_dict['rf_profile_details'][rf_profile]['operational_rates'][band].update({"802.11g_12m_rate": match.group("g12m_rate")})
                continue
            elif p19.match(line):
                match = p19.match(line)
                rf_profile_details_dict['rf_profile_details'][rf_profile]['operational_rates'][band].update({"802.11g_18m_rate": match.group("g18m_rate")})
                continue
            elif p20.match(line):
                match = p20.match(line)
                rf_profile_details_dict['rf_profile_details'][rf_profile]['operational_rates'][band].update({"802.11g_24m_rate": match.group("g24m_rate")})
                continue
            elif p21.match(line):
                match = p21.match(line)
                rf_profile_details_dict['rf_profile_details'][rf_profile]['operational_rates'][band].update({"802.11g_36m_rate": match.group("g36m_rate")})
                continue
            elif p22.match(line):
                match = p22.match(line)
                rf_profile_details_dict['rf_profile_details'][rf_profile]['operational_rates'][band].update({"802.11g_48m_rate": match.group("g48m_rate")})
                continue
            elif p23.match(line):
                match = p23.match(line)
                rf_profile_details_dict['rf_profile_details'][rf_profile]['operational_rates'][band].update({"802.11g_54m_rate": match.group("g54m_rate")})
                continue

        return rf_profile_details_dict

