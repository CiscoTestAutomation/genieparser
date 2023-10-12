'''show_cable_tdr_interface.py
IOSXE parser for the following show command
	* show cable tdr interface {interface}
    * show cable-diagnostics tdr interface {interface}
    * show cable rpd
    * show cable rpd {rpd_mac_or_ip}
    * show cable rpd ipv6
    * show cable rpd {rpd_mac} ipv6
    * show cable rpd {rpd_ip} ipv6
    * show cable rpd {tengig_core_interface} ipv6
    * show cable rpd slot {lc_slot_number}  ipv6
    * show cable rpd {rpd_mac_or_ip} spectrum-capture-capabilities
    * show cable modem
    * show cable modem {cm_ipv4_or_ipv6_or_mac}
    * show cable modem rpd {rpd_ipv4_or_ipv6_or_mac}
    * show cable modem rpd id {rpd_mac}
    * show cable modem rpd name {rpd_name}
    * show cable modem cable {cable_interface}
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, ListOf, \
        Optional, And, Default, Use

# import parser utils
from genie.libs.parser.utils.common import Common

# =================================================
# Schema for:
#   * 'show cable tdr interface {interface}'
# ==================================================
class ShowCableTdrIntSchema(MetaParser):
    schema = {
        Any(): {
            'interface': str,
            'speed': str,
            'date': str,
            'time': str,
            'pairs': {
                Any() : {
                    'length': int,
                    'tolerance': int,
                    'remote_pair': str,
                    'status': str,
               }
           }
        }
    }

class ShowCableTdrInterface(ShowCableTdrIntSchema):
    """
    Parser for:
            show cable tdr interface {interface}
    """

    cli_command = 'show cable tdr interface {interface}'

    def cli(self, interface=None, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        # initial return dictionary
        tdr_dict = {}

        # TDR test last run on: January 09 16:19:29
        p1 = re.compile(r'^TDR +test +last +run +on: +(?P<date>\w+ \d+) +(?P<time>\d+:\d+:\d+)$')

        # Gi1/0/1   auto  Pair A     0    +/- 1  meters N/A         Open
        p2 = re.compile(r'^(?P<interface>\w\w\d\/\d\/\d+)\s+(?P<speed>auto|100M|1000M|2500M)'
                '\s+Pair (?P<local_pair>A)     (?P<pair_length>\d+)\s+\+\/\- (?P<pair_tolerance>\d+)\s+meters '
                '(?P<pair_remote>N\/A|Pair A|Pair B|Pair C|Pair D)\s+(?P<pair_status>.*$)')

        #                 Pair B     1    +/- 1  meters N/A         Open
        #                 Pair C     0    +/- 1  meters N/A         Open
        #                 Pair D     1    +/- 1  meters N/A         Open
        p3 = re.compile(r'Pair +(?P<local_pair>B|C|D)\s+(?P<pair_length>\d+)\s+\+\/\- (?P<pair_tolerance>\d+)\s+meters'
                ' +(?P<pair_remote>N\/A|Pair A|Pair B|Pair C|Pair D)\s+(?P<pair_status>.*$)')

        for line in output.splitlines():
            line = line.strip()

            # TDR test last run on: January 09 16:19:29
            m = p1.match(line)
            if m:
                date_performed = m.groupdict()['date']
                time_performed = m.groupdict()['time']
                continue

            # Gi1/0/1   auto  Pair A     0    +/- 1  meters N/A         Open
            m = p2.match(line)
            if m:
                interface = m.groupdict()['interface']
                group = m.groupdict()
                tdr_dict[interface] = {}
                tdr_dict[interface]['interface'] = m.groupdict()['interface']
                tdr_dict[interface]['speed'] = m.groupdict()['speed']

                tdr_dict[interface]['date'] = date_performed
                tdr_dict[interface]['time'] = time_performed

                tdr_dict[interface].setdefault('pairs', {})

                pair = m.groupdict()['local_pair']
                tdr_dict[interface]['pairs'][pair] = {}
                tdr_dict[interface]['pairs'][pair]['length'] = int(m.groupdict()['pair_length'])
                tdr_dict[interface]['pairs'][pair]['tolerance'] = int(m.groupdict()['pair_tolerance'])
                tdr_dict[interface]['pairs'][pair]['remote_pair'] = m.groupdict()['pair_remote']
                tdr_dict[interface]['pairs'][pair]['status'] = m.groupdict()['pair_status']
                continue

            #                 Pair B     1    +/- 1  meters N/A         Open
            #                 Pair C     0    +/- 1  meters N/A         Open
            #                 Pair D     1    +/- 1  meters N/A         Open
            m = p3.match(line)
            if m:
                pair = m.groupdict()['local_pair']
                tdr_dict[interface]['pairs'][pair] = {}
                tdr_dict[interface]['pairs'][pair]['length'] = int(m.groupdict()['pair_length'])
                tdr_dict[interface]['pairs'][pair]['tolerance'] = int(m.groupdict()['pair_tolerance'])
                tdr_dict[interface]['pairs'][pair]['remote_pair'] = m.groupdict()['pair_remote']
                tdr_dict[interface]['pairs'][pair]['status'] = m.groupdict()['pair_status']
                continue

        return(tdr_dict)


class ShowCableDiagnosticsTdrIntSchema(MetaParser):
    """Schema show cable-diagnostics tdr interface {interface}"""
    schema = {
        'interface': {
            Any(): {
                'speed': str,
                Optional('date'): str,
                Optional('time'): str,
                'pairs': {
                    Any() : {
                        'length': str,
                        'tolerance': str,
                        'remote_pair': str,
                        'status': str,
                    }
                }
            }
        }
    }


class ShowCableDiagnosticsTdrInt(ShowCableDiagnosticsTdrIntSchema):
    """Parser for show cable-diagnostics tdr interface {interface}"""

    cli_command = 'show cable-diagnostics tdr interface {interface}'

    def cli(self, interface=None, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        # TDR test last run on: January 09 16:19:29
        p1 = re.compile(r'^TDR +test +last +run +on: +(?P<date>\w+ \d+) +(?P<time>\d+:\d+:\d+)$')

        # Gi1/0/1   auto  Pair A     0    +/- 1  meters N/A         Open
        # Gi2/7 0Mbps 1-2 46 +/-1m Unknown Open
        # Gi1/0/1     1000M Pair A     N/A                N/A         Not Completed
        p2 = re.compile(r'^(?P<interface>[\w\/]+)\s+(?P<speed>\d+(auto|Mbps|M))((\s+)|(\s+\w+\s+))'
                        r'(?P<local_pair>([\d\-]+)|A)\s+(?P<length>\d+|N/A)((\s+\+\/\-|\s)(?P<tolerance>\w+|))'
                        r'\s+(?P<remote_pair>N/A|\w+)\s+(?P<status>.*$)')

        #   Pair B     N/A                N/A         Not Completed      
        #   Pair C     N/A                N/A         Not Completed      
        #   Pair D     N/A                N/A         Not Completed 
        # 3-6 45 +/-1m Unknown Open 
        p3 = re.compile(r'((\w+\s+)|)(?P<local_pair>((\w)|(\d\-\d)))\s+(?P<length>\d+|N/A)((\s+\+\/\-|\s)(?P<tolerance>\w+|))'
            r'\s+(?P<remote_pair>N/A|\w+)\s+(?P<status>.*$)')

        # initial return dictionary
        ret_dict = {}

        # Added flag to check wheather p1 pattern is executing or not. If p1 regex. match any line flag will change to True.
        flag = False
        for line in output.splitlines():
            line = line.strip()

            # TDR test last run on: January 09 16:19:29
            m = p1.match(line)
            if m:
                # If condition satisfied flag will True.
                flag = True
                group = m.groupdict()
                continue

            # Gi1/0/1   auto  Pair A     0    +/- 1  meters N/A         Open
            m = p2.match(line)
            if m:
                output = m.groupdict()
                int_dict = ret_dict.setdefault('interface', {}).setdefault(output['interface'], {})
                int_dict['speed'] = output['speed']
                # If flag True then it will add date and time in int_dict.
                if flag:
                    int_dict['date'] = group['date']
                    int_dict['time'] = group['time']
                pairs = int_dict.setdefault('pairs', {})
                pair_dict = pairs.setdefault(output['local_pair'], {})
                pair_dict['length'] = output['length']
                pair_dict['tolerance'] = output['tolerance']
                pair_dict['remote_pair'] = output['remote_pair']
                pair_dict['status'] = output['status']
                continue

            #   Pair D     N/A                N/A         Not Completed  
            m = p3.match(line)
            if m:
                output = m.groupdict()
                local_pair = output['local_pair']
                del output['local_pair']
                pairs.setdefault(local_pair, output)
                continue

        return ret_dict

# =================================================
# Schema for:
#   * 'show cable rpd'
#   * 'show cable rpd {rpd_mac}'
# ==================================================

class ShowCableRpdSchema(MetaParser):
    """ Schema for "show cable rpd" """

    schema = {
        'mac_address': {
            Any(): {
                'ip_address': str,
                'interface': str,
                'state': str,
                'role': str,
                'ha': str,
                'auth': str,
                'name': str,
            }
        }
    }

# ========================================
# Parser for 'show cable rpd'
# Parser for 'show cable rpd {rpd_mac}'
# ========================================

class ShowCableRpd(ShowCableRpdSchema):
    """ Parser for
      "show cable rpd"
      "show cable rpd {rpd_mac_or_ip}"
    """

    cli_command = ['show cable rpd',
                   'show cable rpd {rpd_mac_or_ip}']

    def cli(self, rpd_mac_or_ip='', output=None):
        if output is None:
            if rpd_mac_or_ip:
                cmd = self.cli_command[1].format(rpd_mac_or_ip=rpd_mac_or_ip)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)
        else:
            output = output

        # Init vars
        ret_dict = {}

        # 70b3.1791.4266  ---              Te1/1/0   online       Pri  Act N/A  LC9_RPD0_3x6_RACK4
        p1 = re.compile(r'^(?P<rpd_mac>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})\s+'
                        r'(?P<ip_address>-{3}|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                        r'(?P<interface>Te\d(\/\d{1,2}){2})\s+'
                        r'(?P<state>(\S)+)\s+(?P<role>(\S)+)\s+'
                        r'(?P<ha>(\S)+)\s+(?P<auth>(\S)+)\s+(?P<name>(\S){1,80}$)')

        for line in output.splitlines():
            line = line.strip()

            # 70b3.1791.4266  ---              Te1/1/0   online       Pri  Act N/A  LC9_RPD0_3x6_RACK4
            m = p1.match(line)
            if m:
                rpd_mac = m.groupdict()['rpd_mac']
                if 'mac_address' not in ret_dict:
                    ret_dict['mac_address'] = {}
                ret_dict['mac_address'][rpd_mac] = {}
                ret_dict['mac_address'][rpd_mac]['ip_address'] = m.groupdict()['ip_address']
                ret_dict['mac_address'][rpd_mac]['interface'] = m.groupdict()['interface']
                ret_dict['mac_address'][rpd_mac]['state'] = m.groupdict()['state']
                ret_dict['mac_address'][rpd_mac]['role'] = m.groupdict()['role']
                ret_dict['mac_address'][rpd_mac]['ha'] = m.groupdict()['ha']
                ret_dict['mac_address'][rpd_mac]['auth'] = m.groupdict()['auth']
                ret_dict['mac_address'][rpd_mac]['name'] = m.groupdict()['name']
                continue

        return ret_dict


# =================================================
# Schema for:
#   * 'show cable rpd ipv6'
#   * 'show cable rpd {rpd_mac} ipv6'
#   * 'show cable rpd {rpd_ip} ipv6'
#   * 'show cable rpd {tengig_core_interface} ipv6'
#   * 'show cable rpd slot {lc_slot_number}  ipv6'
# ==================================================


class ShowCableRpdIpv6Schema(MetaParser):
    """ Schema for
        "show cable rpd ipv6"
        "show cable rpd {rpd_mac} ipv6"
        "show cable rpd {rpd_ip} ipv6"
        "show cable rpd {tengig_core_interface} ipv6"
        "show cable rpd slot {lc_slot_number} ipv6"
    """

    schema = {
        'mac_address': {
            Any(): {
                'ipv6_address': str,
                'interface': str,
                'state': str,
                'role': str,
                'ha': str,
                'auth': str,
            }
        }
    }

# ========================================
# Parser for 'show cable rpd ipv6'
# Parser for 'show cable rpd {rpd_mac} ipv6'
# Parser for 'show cable rpd {rpd_ip} ipv6'
# Parser for 'show cable rpd {tengig_core_interface} ipv6'
# Parser for 'show cable rpd slot {lc_slot_number}  ipv6'
# ========================================

class ShowCableRpdIpv6(ShowCableRpdIpv6Schema):
    """
    Parser for
        "show cable rpd ipv6"
        "show cable rpd {rpd_mac} ipv6"
        "show cable rpd {rpd_ip} ipv6"
        "show cable rpd {tengig_core_interface} ipv6"
        "show cable rpd slot {lc_slot_number} ipv6"
    """

    cli_command = ['show cable rpd ipv6',
                   'show cable rpd {argument} ipv6',
                   'show cable rpd slot {lc_slot_number} ipv6']

    def cli(self, argument='',lc_slot_number='', output=None):
        if output is None:
            if lc_slot_number:
                cmd = self.cli_command[2].format(lc_slot_number=lc_slot_number)
            elif argument:
                cmd = self.cli_command[1].format(argument=argument)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # Init vars
        ret_dict = {}

        # 70b3.1791.4266  Te1/1/0   online       Pri  Act N/A  2002::C096:103
        p1 = re.compile(r'^(?P<rpd_mac>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})\s+'
                        r'(?P<interface>Te\d(\/\d{1,2}){2})\s+'
                        r'(?P<state>(\S)+)\s+(?P<role>(\S)+)\s+'
                        r'(?P<ha>(\S)+)\s+(?P<auth>(\S)+)\s+(?P<ipv6_address>-{3}|[a-fA-F\d\:]+$)')

        for line in output.splitlines():
            line = line.strip()

            # 70b3.1791.4266  Te1/1/0   online       Pri  Act N/A  2002::C096:103
            m = p1.match(line)
            if m:
                rpd_mac = m.groupdict()['rpd_mac']
                if 'mac_address' not in ret_dict:
                    ret_dict['mac_address'] = {}
                ret_dict['mac_address'][rpd_mac] = {}
                ret_dict['mac_address'][rpd_mac]['interface'] = m.groupdict()['interface']
                ret_dict['mac_address'][rpd_mac]['state'] = m.groupdict()['state']
                ret_dict['mac_address'][rpd_mac]['role'] = m.groupdict()['role']
                ret_dict['mac_address'][rpd_mac]['ha'] = m.groupdict()['ha']
                ret_dict['mac_address'][rpd_mac]['auth'] = m.groupdict()['auth']
                ret_dict['mac_address'][rpd_mac]['ipv6_address'] = m.groupdict()['ipv6_address']
                continue
        return ret_dict


# =================================================
# Schema for:
#   * 'show cable rpd {rpd_mac_or_ip} spectrum-capture-capabilities'
# ==================================================

class ShowCableRpdSpectrumCaptureCapabilitiesSchema(MetaParser):
    """ Schema for "show cable rpd {rpd_mac_or_ip} spectrum-capture-capabilities" """

    schema = {
        'mac_address': str,
        'num_sac': int,
        'sac_index': int,
        'sac_description': str,
        'max_capture_span_in_hz': int,
        'min_capture_freq_in_hz': int,
        'max_capture_freq_in_hz': int,
        'supported_trigger_modes': ListOf(str),
        'supported_output_formats': ListOf(str),
        'supported_window_formats': ListOf(str),
        'supports_averaging': bool,
        'supported_aggregation_method': str,
        'supports_spectrum_qualification': bool,
        'max_num_bins': int,
        'min_num_bins': int,
        'min_repeat_period_in_us': int,
        'supported_trigger_channel_type': ListOf(str),
        'pw_type': ListOf(str),
        'lowest_capture_port': int,
        'highest_capture_port': int,
        'supported_scanning_capture': bool,
        'min_scanning_repeat_period_in_ms': int,
    }


# ========================================
# Parser for 'show cable rpd {rpd_mac_or_ip} spectrum-capture-capabilities'
# ========================================

class ShowCableRpdSpectrumCaptureCapabilities(ShowCableRpdSpectrumCaptureCapabilitiesSchema):
    """ Parser for
      "show cable rpd {rpd_mac_or_ip} spectrum-capture-capabilities"
    """

    cli_command = ['show cable rpd {rpd_mac_or_ip} spectrum-capture-capabilities']

    def cli(self, rpd_mac_or_ip='', output=None):
        if output is None:
            cmd = self.cli_command[0].format(rpd_mac_or_ip=rpd_mac_or_ip)
            output = self.device.execute(cmd)
        else:
            output = output

        # Init vars
        ret_dict = {}

        # RPD ID                         : 70b3.1791.423c
        p1 = re.compile(r'^RPD\sID\s+:\s(?P<rpd_mac>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}$)')

        # NumSacs                        : 1
        p2 = re.compile(r'^NumSacs\s+:\s(?P<num_sac>\d+$)')

        # SacIndex                       : 0
        p3 = re.compile(r'^SacIndex\s+:\s(?P<sac_index>\d+$)')

        # SacDescription                 : Wideband Spectrum Analysis Circuit, frequency range 0-204.8 MHz
        p4 = re.compile(r'^SacDescription\s+:\s(?P<sac_description>.*$)')

        # MaxCaptureSpan                 : 409600000 Hz
        p5 = re.compile(r'^MaxCaptureSpan\s+:\s(?P<max_capture_span_in_hz>\d+)\sHz$')

        # MinimumCaptureFrequency        : 0 Hz
        p6 = re.compile(r'^MinimumCaptureFrequency\s+:\s(?P<min_capture_freq_in_hz>\d+)\sHz$')

        # MaximumCaptureFrequency        : 409600000 Hz
        p7 = re.compile(r'^MaximumCaptureFrequency\s+:\s(?P<max_capture_freq_in_hz>\d+)\sHz$')

        # SupportedTriggerModes          : |freeRunning|
        p8 = re.compile(r'^SupportedTriggerModes\s+:\s(?P<supported_trigger_modes>\S+)$')

        # SupportedOutputFormats         : |timeIQ|fftPower|fftIQ|fftAmplitude|
        p9 = re.compile(r'^SupportedOutputFormats\s+:\s(?P<supported_output_formats>\S+)$')

        # SupportedWindowFormats         : |hann|blackmanHarris|hamming|
        p10 = re.compile(r'^SupportedWindowFormats\s+:\s(?P<supported_window_formats>\S+)$')

        # SupportsAveraging              : Support
        p11 = re.compile(r'^SupportsAveraging\s+:\s(?P<supports_averaging>(Not Support|Support)$)')

        # SupportedAggregationMethods    : None
        p12 = re.compile(r'^SupportedAggregationMethods\s+:\s(?P<supported_aggregation_method>.*$)')

        # SupportsSpectrumQualification  : Not Support
        p13 = re.compile(r'^SupportsSpectrumQualification\s+:\s'
                         r'(?P<supports_spectrum_qualification>(Not Support|Support)$)')

        # MaxNumBins                     : 4096
        p14 = re.compile(r'^MaxNumBins\s+:\s(?P<max_num_bins>\d+$)')

        # MinNumBins                     : 256
        p15 = re.compile(r'^MinNumBins\s+:\s(?P<min_num_bins>\d+$)')

        # MinRepeatPeriod                : 25000 us
        p16 = re.compile(r'^MinRepeatPeriod\s+:\s(?P<min_repeat_period_in_us>\d+)\sus$')

        # SupportedTrigChanTypes         : |SC-QAM|OFDMA|
        p17 = re.compile(r'^SupportedTrigChanTypes\s+:\s(?P<supported_trigger_channel_type>\S+)$')

        # PwType                         : |PNM PW|
        p18 = re.compile(r'^PwType\s+:\s(?P<pw_type>.*$)')

        # LowestCapturePort              : 0
        p19 = re.compile(r'^LowestCapturePort\s+:\s(?P<lowest_capture_port>\d+$)')

        # HighestCapturePort             : 1
        p20 = re.compile(r'^HighestCapturePort\s+:\s(?P<highest_capture_port>\d+$)')

        # SupportsScanningCapture        : Not Support
        p21 = re.compile(r'^SupportsScanningCapture\s+:\s(?P<supported_scanning_capture>(Not Support|Support)$)')

        # MinScanningRepeatPeriod        : 0 ms
        p22 = re.compile(r'^MinScanningRepeatPeriod\s+:\s(?P<min_scanning_repeat_period_in_ms>\d+)\sms$')


        for line in output.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                ret_dict['mac_address'] = m.groupdict()['rpd_mac']
                continue

            m = p2.match(line)
            if m:
                ret_dict['num_sac'] = int(m.groupdict()['num_sac'])
                continue

            m = p3.match(line)
            if m:
                ret_dict['sac_index'] = int(m.groupdict()['sac_index'])
                continue

            m = p4.match(line)
            if m:
                ret_dict['sac_description'] = m.groupdict()['sac_description']
                continue

            m = p5.match(line)
            if m:
                ret_dict['max_capture_span_in_hz'] = int(m.groupdict()['max_capture_span_in_hz'])
                continue

            m = p6.match(line)
            if m:
                ret_dict['min_capture_freq_in_hz'] = int(m.groupdict()['min_capture_freq_in_hz'])
                continue

            m = p7.match(line)
            if m:
                ret_dict['max_capture_freq_in_hz'] = int(m.groupdict()['max_capture_freq_in_hz'])
                continue

            m = p8.match(line)
            if m:
                ret_dict['supported_trigger_modes'] = m.groupdict()['supported_trigger_modes'].strip('|').split('|')
                continue

            m = p9.match(line)
            if m:
                ret_dict['supported_output_formats'] = m.groupdict()['supported_output_formats'].strip('|').split('|')
                continue

            m = p10.match(line)
            if m:
                ret_dict['supported_window_formats'] = m.groupdict()['supported_window_formats'].strip('|').split('|')
                continue

            m = p11.match(line)
            if m:
                if m.groupdict()['supports_averaging'] == "Support":
                    ret_dict['supports_averaging'] = True
                else:
                    ret_dict['supports_averaging'] = False
                continue

            m = p12.match(line)
            if m:
                ret_dict['supported_aggregation_method'] = m.groupdict()['supported_aggregation_method']
                continue

            m = p13.match(line)
            if m:
                if m.groupdict()['supports_spectrum_qualification'] == "Support":
                    ret_dict['supports_spectrum_qualification'] = True
                else:
                    ret_dict['supports_spectrum_qualification'] = False
                continue

            m = p14.match(line)
            if m:
                ret_dict['max_num_bins'] = int(m.groupdict()['max_num_bins'])
                continue

            m = p15.match(line)
            if m:
                ret_dict['min_num_bins'] = int(m.groupdict()['min_num_bins'])
                continue

            m = p16.match(line)
            if m:
                ret_dict['min_repeat_period_in_us'] = int(m.groupdict()['min_repeat_period_in_us'])
                continue

            m = p17.match(line)
            if m:
                ret_dict['supported_trigger_channel_type'] = \
                    m.groupdict()['supported_trigger_channel_type'].strip('|').split('|')
                continue

            m = p18.match(line)
            if m:
                ret_dict['pw_type'] = m.groupdict()['pw_type'].strip('|').split('|')
                continue

            m = p19.match(line)
            if m:
                ret_dict['lowest_capture_port'] = int(m.groupdict()['lowest_capture_port'])
                continue

            m = p20.match(line)
            if m:
                ret_dict['highest_capture_port'] = int(m.groupdict()['highest_capture_port'])
                continue

            m = p21.match(line)
            if m:
                if m.groupdict()['supported_scanning_capture'] == "Support":
                    ret_dict['supported_scanning_capture'] = True
                else:
                    ret_dict['supported_scanning_capture'] = False
                continue

            m = p22.match(line)
            if m:
                ret_dict['min_scanning_repeat_period_in_ms'] = int(m.groupdict()['min_scanning_repeat_period_in_ms'])
                continue

        return ret_dict


# =================================================
# Schema for:
# * show cable modem
# * show cable modem {cm_ipv4_or_ipv6_or_mac}
# * show cable modem rpd {rpd_ipv4_or_ipv6_or_mac}
# * show cable modem rpd id {rpd_mac}
# * show cable modem rpd name {rpd_name}
# * show cable modem cable {cable_interface}
# ==================================================

class ShowCableModemSchema(MetaParser):
    """ Schema for
        "show cable modem"
        "show cable modem {cm_ipv4_or_ipv6_or_mac}"
        "show cable modem rpd {rpd_ipv4_or_ipv6_or_mac}"
        "show cable modem rpd id {rpd_mac}"
        "show cable modem rpd name {rpd_name}"
        "show cable modem cable {cable_interface}"
    """

    schema = {
        'mac_address': {
            Any(): {
                'ipv4_address': str,
                'interface': str,
                'mac_state': str,
                'primary_sid': str,
                'rx_power': str,
                'timing_offset': str,
                'num_cpe': str,
                'dip': str,
                Optional('dev_class'): str,

            }
        }
    }


# ========================================
# Parser for
# * show cable modem
# * show cable modem {cm_ipv4_or_ipv6_or_mac}
# * show cable modem rpd {rpd_ipv4_or_ipv6_or_mac}
# * show cable modem rpd id {rpd_mac}
# * show cable modem rpd name {rpd_name}
# * show cable modem cable {cable_interface}
# ========================================

class ShowCableModem(ShowCableModemSchema):
    """
    Parser for
        "show cable modem"
        "show cable modem {cm_ipv4_or_ipv6_or_mac}"
    """

    cli_command = ['show cable modem',
                   'show cable modem {cm_ipv4_or_ipv6_or_mac}']

    def cli(self, cm_ipv4_or_ipv6_or_mac='', output=None):
        if output is None:
            if cm_ipv4_or_ipv6_or_mac:
                cmd = self.cli_command[1].format(cm_ipv4_or_ipv6_or_mac=cm_ipv4_or_ipv6_or_mac)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # Init vars
        ret_dict = {}

        # 9058.515c.a3c0 101.115.1.18    C1/0/0/UB     w-online(pt)      1     10.00  416    0   N
        p1 = re.compile(r'^(?P<cm_mac>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})\s+'
                        r'(?P<ip_address>-{3}|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                        r'(?P<interface>C\d(\/\d{1,2}){2}\/UB)\s+(?P<state>(\S)+)\s+'
                        r'(?P<sid>(\d)+)\s+(?P<rx_power>(\S)+)\s+(?P<timing_offset>(\S)+)\s+'
                        r'(?P<num_cpe>(\d){1,5})\s+(?P<dip>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # 9058.515c.a3c0 101.115.1.18    C1/0/0/UB     w-online(pt)      1     10.00  416    0   N
            m = p1.match(line)
            if m:
                cm_mac = m.groupdict()['cm_mac']
                cm_mac_dict = ret_dict.setdefault('mac_address', {}).setdefault(cm_mac, {})
                cm_mac_dict.update({
                    'ipv4_address': m.groupdict()['ip_address'],
                    'interface': m.groupdict()['interface'],
                    'mac_state': m.groupdict()['state'],
                    'primary_sid': m.groupdict()['sid'],
                    'rx_power': m.groupdict()['rx_power'],
                    'timing_offset': m.groupdict()['timing_offset'],
                    'num_cpe': m.groupdict()['num_cpe'],
                    'dip': m.groupdict()['dip']
                })
                continue
        return ret_dict


class ShowCableModemCable(ShowCableModemSchema):
    """
    Parser for
        "show cable modem cable {cable_interface}"
    """

    cli_command = ['show cable modem cable {cable_interface}']

    def cli(self, cable_interface, output=None):
        if output is None:
            cmd = self.cli_command[0].format(cable_interface=cable_interface)
            output = self.device.execute(cmd)

        # Init vars
        ret_dict = {}

        # 9058.515c.a3c0 101.115.1.18    C1/0/0/UB     w-online(pt)      1     10.00  416    0   N
        p1 = re.compile(r'^(?P<cm_mac>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})\s+'
                        r'(?P<ip_address>-{3}|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                        r'(?P<interface>C\d(\/\d{1,2}){2}\/UB)\s+(?P<state>(\S)+)\s+'
                        r'(?P<sid>(\d)+)\s+(?P<rx_power>(\S)+)\s+(?P<timing_offset>(\S)+)\s+'
                        r'(?P<num_cpe>(\d){1,5})\s+(?P<dip>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # 9058.515c.a3c0 101.115.1.18    C1/0/0/UB     w-online(pt)      1     10.00  416    0   N
            m = p1.match(line)
            if m:
                cm_mac = m.groupdict()['cm_mac']
                cm_mac_dict = ret_dict.setdefault('mac_address', {}).setdefault(cm_mac, {})
                cm_mac_dict.update({
                    'ipv4_address': m.groupdict()['ip_address'],
                    'interface': m.groupdict()['interface'],
                    'mac_state': m.groupdict()['state'],
                    'primary_sid': m.groupdict()['sid'],
                    'rx_power': m.groupdict()['rx_power'],
                    'timing_offset': m.groupdict()['timing_offset'],
                    'num_cpe': m.groupdict()['num_cpe'],
                    'dip': m.groupdict()['dip']
                })
                continue
        return ret_dict


class ShowCableModemRpd(ShowCableModemSchema):
    """
    Parser for
        "show cable modem rpd {rpd_ipv4_or_ipv6_or_mac}"
    """

    cli_command = ['show cable modem rpd {rpd_ipv4_or_ipv6_or_mac}']

    def cli(self, rpd_ipv4_or_ipv6_or_mac, output=None):
        if output is None:
            cmd = self.cli_command[0].format(rpd_ipv4_or_ipv6_or_mac=rpd_ipv4_or_ipv6_or_mac)
            output = self.device.execute(cmd)

        # Init vars
        ret_dict = {}

        # 9058.515c.a3c0 101.115.1.18    C1/0/0/UB     w-online(pt)      1     10.00  416    0   N CM
        p1 = re.compile(r'^(?P<cm_mac>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})\s+'
                        r'(?P<ip_address>-{3}|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                        r'(?P<interface>C\d(\/\d{1,2}){2}\/UB)\s+(?P<state>(\S)+)\s+'
                        r'(?P<sid>(\d)+)\s+(?P<rx_power>(\S)+)\s+(?P<timing_offset>(\S)+)\s+'
                        r'(?P<num_cpe>(\d){1,5})\s+(?P<dip>\S+)\s+(?P<dev_class>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # 9058.515c.c978 101.115.1.12    C9/0/1/UB     w-online(pt)      1     10.00  470    0   N CM
            m = p1.match(line)
            if m:
                cm_mac = m.groupdict()['cm_mac']
                cm_mac_dict = ret_dict.setdefault('mac_address', {}).setdefault(cm_mac, {})
                cm_mac_dict.update({
                    'ipv4_address': m.groupdict()['ip_address'],
                    'interface': m.groupdict()['interface'],
                    'mac_state': m.groupdict()['state'],
                    'primary_sid': m.groupdict()['sid'],
                    'rx_power': m.groupdict()['rx_power'],
                    'timing_offset': m.groupdict()['timing_offset'],
                    'num_cpe': m.groupdict()['num_cpe'],
                    'dip': m.groupdict()['dip'],
                    'dev_class': m.groupdict()['dev_class']
                })
                continue
        return ret_dict


class ShowCableModemRpdId(ShowCableModemSchema):
    """
    Parser for
        "show cable modem rpd id {rpd_mac}"
    """

    cli_command = ['show cable modem rpd id {rpd_mac}']

    def cli(self, rpd_mac, output=None):
        if output is None:
            cmd = self.cli_command[0].format(rpd_mac=rpd_mac)
            output = self.device.execute(cmd)

        # Init vars
        ret_dict = {}

        # 9058.515c.a3c0 101.115.1.18    C1/0/0/UB     w-online(pt)      1     10.00  416    0   N CM
        p1 = re.compile(r'^(?P<cm_mac>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})\s+'
                        r'(?P<ip_address>-{3}|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                        r'(?P<interface>C\d(\/\d{1,2}){2}\/UB)\s+(?P<state>(\S)+)\s+'
                        r'(?P<sid>(\d)+)\s+(?P<rx_power>(\S)+)\s+(?P<timing_offset>(\S)+)\s+'
                        r'(?P<num_cpe>(\d){1,5})\s+(?P<dip>\S+)\s+(?P<dev_class>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # 9058.515c.c978 101.115.1.12    C9/0/1/UB     w-online(pt)      1     10.00  470    0   N CM
            m = p1.match(line)
            if m:
                cm_mac = m.groupdict()['cm_mac']
                cm_mac_dict = ret_dict.setdefault('mac_address', {}).setdefault(cm_mac, {})
                cm_mac_dict.update({
                    'ipv4_address': m.groupdict()['ip_address'],
                    'interface': m.groupdict()['interface'],
                    'mac_state': m.groupdict()['state'],
                    'primary_sid': m.groupdict()['sid'],
                    'rx_power': m.groupdict()['rx_power'],
                    'timing_offset': m.groupdict()['timing_offset'],
                    'num_cpe': m.groupdict()['num_cpe'],
                    'dip': m.groupdict()['dip'],
                    'dev_class': m.groupdict()['dev_class']
                })
                continue
        return ret_dict


class ShowCableModemRpdName(ShowCableModemSchema):
    """
    Parser for
        "show cable modem rpd name {rpd_name}"
    """

    cli_command = ['show cable modem rpd name {rpd_name}']

    def cli(self, rpd_name, output=None):
        if output is None:
            cmd = self.cli_command[0].format(rpd_name=rpd_name)
            output = self.device.execute(cmd)

        # Init vars
        ret_dict = {}

        # 9058.515c.a3c0 101.115.1.18    C1/0/0/UB     w-online(pt)      1     10.00  416    0   N CM
        p1 = re.compile(r'^(?P<cm_mac>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})\s+'
                        r'(?P<ip_address>-{3}|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                        r'(?P<interface>C\d(\/\d{1,2}){2}\/UB)\s+(?P<state>(\S)+)\s+'
                        r'(?P<sid>(\d)+)\s+(?P<rx_power>(\S)+)\s+(?P<timing_offset>(\S)+)\s+'
                        r'(?P<num_cpe>(\d){1,5})\s+(?P<dip>\S+)\s+(?P<dev_class>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # 9058.515c.c978 101.115.1.12    C9/0/1/UB     w-online(pt)      1     10.00  470    0   N CM
            m = p1.match(line)
            if m:
                cm_mac = m.groupdict()['cm_mac']
                cm_mac_dict = ret_dict.setdefault('mac_address', {}).setdefault(cm_mac, {})
                cm_mac_dict.update({
                    'ipv4_address': m.groupdict()['ip_address'],
                    'interface': m.groupdict()['interface'],
                    'mac_state': m.groupdict()['state'],
                    'primary_sid': m.groupdict()['sid'],
                    'rx_power': m.groupdict()['rx_power'],
                    'timing_offset': m.groupdict()['timing_offset'],
                    'num_cpe': m.groupdict()['num_cpe'],
                    'dip': m.groupdict()['dip'],
                    'dev_class': m.groupdict()['dev_class']
                })
                continue
        return ret_dict
