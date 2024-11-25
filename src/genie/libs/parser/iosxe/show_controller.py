''' show_controller.py

IOSXE parsers for the following show commands:

    * 'show controller VDSL {interface}'
    * 'show controller ethernet-controller {interface}'
    * 'show controller ethernet-controller'
'''

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use
# import parser utils
from genie.libs.parser.utils.common import Common


class ShowControllerVDSLSchema(MetaParser):
    """Schema for show controller VDSL {interface}"""

    schema = {
        'controller_vdsl': str,
        'daemon_status': str,
        Any(): {
            'chip_vendor': {
                Optional('chip_vendor_id'): str,
                Optional('chip_vendor_specific'): str,
                Optional('chip_vendor_country'): str,
            },
            'modem_vendor': {
                Optional('modem_vendor_id'): str,
                Optional('modem_vendor_specific'): str,
                Optional('modem_vendor_country'): str,
                Optional('modem_version_near'): str,
            },
            Optional('trellis'): str,
            Optional('serial_number_far'): str,
            Optional('sra'): str,
            Optional('sra_count'): int,
            Optional('bit_swap'): str,
            Optional('bit_swap_count'): str,
            Optional('line_attenuation'): str,
            Optional('signal_attenuation'): str,
            Optional('noise_margin'): str,
            Optional('attainable_rate'): str,
            Optional('actual_power'): str,
            Any(): {
                Optional('line_attenuation(db)'): str,
                Optional('signal_attenuation(db)'): str,
                Optional('noise_margin(db)'): str,
                Optional('speed_(kbps)'): str,
                Optional('sra_previous_speed'): str,
                Optional('previous_speed'): str,
                Optional('total_cells'): str,
                Optional('user_cells'): str,
                Optional('reed_solomon_ec'): str,
                Optional('crc_errors'): str,
                Optional('header_errors'): str,
                Optional('interleave_(ms)'): str,
                Optional('actual_inp'): str,
            },
            Optional('total_fecc'): int,
            Optional('total_es'): int,
            Optional('total_ses'): int,
            Optional('total_loss'): int,
            Optional('total_uas'): int,
            Optional('total_lprs'): int,
            Optional('total_lofs'): int,
            Optional('total_lols'): int,
        },
        Optional('serial_number_near'): str,
        Optional('modem_version_far'): str,        
        Optional('modem_status'): str,
        Optional('dsl_config_mode'): str,
        Optional('tc_mode'): str,
        Optional('selftest_result'): str,
        Optional('delt_configuration'): str,
        Optional('delt_state'): str,
        Optional('failed_full_inits'): int,
        Optional('short_inits'): int,
        Optional('failed_short_inits'): int,
        Optional('modem_fw_version'): str,
        Optional('modem_phy_version'): str,
        Optional('modem_phy_source'): str,
        Optional('training_log'): str,
        Optional('training_log_filename'): str,
        Optional('trained_mode'): str,
    }

class ShowControllerVDSL(ShowControllerVDSLSchema):
    """
    Parser for show controller VDSL {interface}
    """

    cli_command = 'show controller VDSL {interface}'

    def cli(self, interface='', output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(interface=interface))
        else:
            out = output

        ctrl_dict = {}

        # Controller VDSL 0/2/0 is UP
        p1 = re.compile(r'^[Cc]on\w+\s(?P<ctrl>\w+\s\S+)\s+\w+\s+(?P<state>\w+)$')

        # Daemon Status: UP
        p2 = re.compile(r'^(?P<param>Dae\w+\s+\w+):\s+(?P<vl>\w+)$')

        # Serial Number Near: FGL223491WW C1127X-8 17.7.20210
        # Modem Version Near: 17.7.2021 0524: 03251
        p2_1 = re.compile(r'^(?P<param>Serial\s+Number\s+Near):\s+(?P<vl>.+)$')

        # Modem Version Near: 17.7.20210524: 03251
        # Modem Version Far: 0x544d
        p2_2 = re.compile(r'^(?P<param>Modem\s+Version\s+Far):\s+(?P<vl>.+)$')

        # Modem Status: TC Sync(Showtime!)
        p2_3 = re.compile(r'^(?P<param>Modem\s+Status):\s+(?P<vl>.+)$')
        
        # DSL Config Mode: ADSL2 +
        p2_4 = re.compile(r'^(?P<param>DSL\s+\w+\s+\w+):\s+(?P<vl>.+)$')

        # Trained Mode: G.992.5 (ADSL2 +) Annex A
        p2_5 = re.compile(r'^(?P<param>Tr\w+\s+\w+):\s+(?P<vl>.+)$')

        # TC Mode: ATM
        p2_6 = re.compile(r'^(?P<param>TC\s+\w+):\s+(?P<vl>.+)$')

        # Selftest Result: 0x00
        p2_7 = re.compile(r'^(?P<param>Se\w+\s+\w+):\s+(?P<vl>.+)$')

        # Short inits: 0
        p2_8 = re.compile(r'^(?P<param>Sh\w+\s+\w+):\s+(?P<vl>.+)$')

        # DELT configuration: disabled
        # DELT state: not running
        p2_9 = re.compile(r'^(?P<param>DELT\s+\w+):\s+(?P<vl>.+)$')

        # Failed full inits: 0
        # Failed short inits: 0
        p2_10 = re.compile(r'^(?P<param>Failed\s+\w+\s+\w+):\s+(?P<vl>.+)$')

        # Modem FW Version: 4.14L.04
        p2_11 = re.compile(r'^(?P<param>Modem\s+FW+\s+\w+):\s+(?P<vl>.+)$')

        # Modem PHY Version: A2pv6F039x8.d26d
        # Modem PHY Source: System
        p2_12 = re.compile(r'^(?P<param>Modem\s+PHY+\s+\w+):\s+(?P<vl>.+)$')

        # SRA count: 0    0
        # Total FECC: 799014    23383
        # Total ES: 0       2
        # Total SES: 0      0
        # Total LOSS: 0     0
        # Total UAS: 46     46
        # Total LPRS: 0     0
        # Total LOFS: 0     0
        # Total LOLS: 0     0
        p3 = re.compile(r'^(?P<param>\w+\s+\w+):\s+(?P<xtr>\d+)\s+(?P<xtc>\d+)$')

        # Bit swap: enabled     enabled
        p3_1 = re.compile(r'^(?P<param>\w+\s+\w+):\s+(?P<xtr>[enabled|disable]+)\s+(?P<xtc>\w+)$')

        # Bit swap count: 18    3
        p3_2 = re.compile(r'^(?P<param>\w+\s+\w+\s+\w+):\s+(?P<xtr>\d+)\s+(?P<xtc>\d+)$')

        # Line Attenuation: 4.0 dB      2.2 dB
        # Signal Attenuation: 2.9 dB     0.0 dB
        # Noise Margin: 9.4 dB    5.8 dB
        p3_3 = re.compile(r'^(?P<param>\w+\s+\w+):\s+(?P<xtr>\d+.\d\s+dB)\s+(?P<xtc>\d+.\d\s+dB)$')

        # Actual Power: 19.1 dBm     12.1 dBm
        p3_4 = re.compile(r'^(?P<param>\w+\s+\w+):\s+(?P<xtr>\d+.\d\s+dBm)\s+(?P<xtc>.+)$')

        # Trellis: ON     ON
        # SRA: enabled    enabled
        p3_5 = re.compile(r'^(?P<param>\w+):\s+(?P<xtr>\w+)\s+(?P<xtc>\w+)$')

        # Attainable Rate: 23708 kbits/s       1351 kbits/s
        p3_6 = re.compile(r'^(?P<param>\w+\s+\w+):\s+(?P<xtr>\d+\s+\S+)\s+(?P<xtc>\d+\s+\S+)$')

        # Chip Vendor ID: 'BDCM'                   'BDCM'
        # Chip Vendor Specific: 0x0000        0x544D
        # Chip Vendor Country: 0xB500         0xB500
        # Modem Vendor ID: 'CSCO'                   'BDCM'
        # Modem Vendor Specific: 0x4602       0x544D
        # Modem Vendor Country: 0xB500        0xB500
        # Serial Number Near: FGL223491WW C1127X - 8 17.7.20210
        p3_7 = re.compile(r'^(?P<param>\w+\s+\w+\s+\w+):\s+(?P<xtr>\S+)\s+(?P<xtc>\S+.+)$')

        # Per Band Status: D1  D2  D3  U0  U1  U2  U3
        # Line Attenuation(dB): 0.9    2.4 2.4 N / A   2.0 1.1 N / A
        # Signal  Attenuation(dB): 0.9    2.4 2.4  N / A   1.5 0.6 N / A
        # Noise Margin(dB): 19.1    18.6    18.6    N / A   5.7 5.6 N / A
        p4 = re.compile(r'^(?P<param>\w+\s+\w+\(dB\)):\s+(?P<d1>\d+.\d+)\s+(?P<d2>\d+.\d+)\s+(?P<d3>\d+.\d+)\s+\S+\s+(?P<u1>\d+.\d+)\s+(?P<u2>\d+.\d+)\s+(?P<u3>\S+)$')

        # Training Log: Stopped
        p5 = re.compile(r'^(?P<param>\w+\s+\w+)\s+:\s+(?P<state>\S+)$')

        # Training Log Filename: flash:vdsllog.bin
        p6 = re.compile(r'^(?P<param>\w+\s+\w+\s+\w+)\s+:\s+(?P<state>\S+)$')

        # DS Channel1    DS Channel0    US Channel1    US Channel0
        # Previous Speed: NA   0   NA  0
        # Total Cells: NA   145385538   NA  7799369
        # User Cells: NA   8598306 NA  447068
        # CRC Errors: NA  0   NA  3
        # Header Errors: NA  0   NA  1
        # Actual INP: NA 0.00    NA  0.00
        p7 = re.compile(r'^(?P<param>\w+\s\w+):\s+(?P<d_ch1>[\w\d.]+)\s+(?P<d_ch0>[\d.]+)\s+(?P<u_ch1>[\w\d.]+)\s+(?P<u_ch0>[\d.]+)$')

        # Speed (kbps): NA 23756   NA  1283
        # Interleave (ms): NA  0.08    NA  0.49
        p7_1 = re.compile(r'^(?P<param>\w+\s\(\w+\)):\s+(?P<d_ch1>[\w\d.]+)\s+(?P<d_ch0>[\d.]+)\s+(?P<u_ch1>[\w\d.]+)\s+(?P<u_ch0>[\d.]+)$')

        # SRA Previous Speed: NA   0   NA  0
        p7_2 = re.compile(r'^(?P<param>\w+\s\w+\s+\w+):\s+(?P<d_ch1>[\w\d.]+)\s+(?P<d_ch0>[\d.]+)\s+(?P<u_ch1>[\w\d.]+)\s+(?P<u_ch0>[\d.]+)$')

        # Reed - Solomon EC: NA  0   NA  0
        p7_3 = re.compile(r'^(?P<param>\w+-\w+\s+\w+):\s+(?P<d_ch1>[\w\d.]+)\s+(?P<d_ch0>[\d.]+)\s+(?P<u_ch1>[\w\d.]+)\s+(?P<u_ch0>[\d.]+)$')

        for lines in out.splitlines():
            line = lines.strip()

            # Controller VDSL 0/2/0 is UP
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ctrl_dict['controller_vdsl'] = group['state']

            # Daemon Status: UP
            m = p2.match(line)
            if m:
                group = m.groupdict()
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = group['vl']

            # Serial Number Near: FGL223491WW C1127X-8 17.7.20210
            # Modem Version Near: 17.7.2021 0524: 03251\
            
            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = group['vl']

            m = p2_2.match(line)
            if m:
                group = m.groupdict()
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = group['vl']

            # Modem Status: TC Sync(Showtime!)
            m = p2_3.match(line)
            if m:
                group = m.groupdict()
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = group['vl']

            # DSL Config Mode: ADSL2 +
            m = p2_4.match(line)
            if m:
                group = m.groupdict()
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = group['vl']

            # Trained Mode: G.992.5 (ADSL2 +) Annex A
            m = p2_5.match(line)
            if m:
                group = m.groupdict()
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = group['vl']

            # TC Mode: ATM
            m = p2_6.match(line)
            if m:
                group = m.groupdict()
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = group['vl']

            # Selftest Result: 0x00
            m = p2_7.match(line)
            if m:
                group = m.groupdict()
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = group['vl']

            # Short inits: 0
            m = p2_8.match(line)
            if m:
                group = m.groupdict()
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = int(group['vl'])

            # DELT configuration: disabled
            # DELT state: not running
            m = p2_9.match(line)
            if m:
                group = m.groupdict()
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = group['vl']

            # Failed full inits: 0
            # Failed short inits: 0
            m = p2_10.match(line)
            if m:
                group = m.groupdict()
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = int(group['vl'])

            # Modem FW Version: 4.14L.04
            m = p2_11.match(line)
            if m:
                group = m.groupdict()
                param = re.sub(' +', ' ', group['param'].lower()).replace(" ", "_")
                ctrl_dict[param] = group['vl']

            # Modem PHY Version: A2pv6F039x8.d26d
            # Modem PHY Source: System
            m = p2_12.match(line)
            if m:
                group = m.groupdict()
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = group['vl']

            # SRA count: 0    0
            # Total FECC: 799014    23383
            # Total ES: 0       2
            # Total SES: 0      0
            # Total LOSS: 0     0
            # Total UAS: 46     46
            # Total LPRS: 0     0
            # Total LOFS: 0     0
            # Total LOLS: 0     0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ctrl_dict.setdefault('xtu_r_ds', {})
                ctrl_dict.setdefault('xtu_c_us', {})
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict['xtu_r_ds'][param] = int(group['xtr'])
                ctrl_dict['xtu_c_us'][param] = int(group['xtc'])

            # Bit swap: enabled     enabled
            m = p3_1.match(line)
            if m:
                group = m.groupdict()
                ctrl_dict.setdefault('xtu_r_ds', {})
                ctrl_dict.setdefault('xtu_c_us', {})
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict['xtu_r_ds'][param] = group['xtr']
                ctrl_dict['xtu_c_us'][param] = group['xtc']

            # Bit swap count: 18    3
            m = p3_2.match(line)
            if m:
                group = m.groupdict()
                ctrl_dict.setdefault('xtu_r_ds', {})
                ctrl_dict.setdefault('xtu_c_us', {})
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict['xtu_r_ds'][param] = group['xtr']
                ctrl_dict['xtu_c_us'][param] = group['xtc']

            # Line Attenuation: 4.0 dB      2.2 dB
            # Signal Attenuation: 2.9 dB     0.0 dB
            # Noise Margin: 9.4 dB    5.8 dB
            m = p3_3.match(line)
            if m:
                group = m.groupdict()
                ctrl_dict.setdefault('xtu_r_ds', {})
                ctrl_dict.setdefault('xtu_c_us', {})
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict['xtu_r_ds'][param] = group['xtr']
                ctrl_dict['xtu_c_us'][param] = group['xtc']

            # Actual Power: 19.1 dBm     12.1 dBm
            m = p3_4.match(line)
            if m:
                group = m.groupdict()
                ctrl_dict.setdefault('xtu_r_ds', {})
                ctrl_dict.setdefault('xtu_c_us', {})
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict['xtu_r_ds'][param] = group['xtr']
                ctrl_dict['xtu_c_us'][param] = group['xtc']

            # Trellis: ON     ON
            # SRA: enabled    enabled
            m = p3_5.match(line)
            if m:
                group = m.groupdict()
                ctrl_dict.setdefault('xtu_r_ds', {})
                ctrl_dict.setdefault('xtu_c_us', {})
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict['xtu_r_ds'][param] = group['xtr']
                ctrl_dict['xtu_c_us'][param] = group['xtc']

            # Attainable Rate: 23708 kbits/s       1351 kbits/s
            m = p3_6.match(line)
            if m:
                group = m.groupdict()
                ctrl_dict.setdefault('xtu_r_ds', {})
                ctrl_dict.setdefault('xtu_c_us', {})
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict['xtu_r_ds'][param] = group['xtr']
                ctrl_dict['xtu_c_us'][param] = group['xtc']

            # Chip Vendor ID: 'BDCM'                   'BDCM'
            # Chip Vendor Specific: 0x0000        0x544D
            # Chip Vendor Country: 0xB500         0xB500
            # Modem Vendor ID: 'CSCO'                   'BDCM'
            # Modem Vendor Specific: 0x4602       0x544D
            # Modem Vendor Country: 0xB500        0xB500
            # Serial Number Near: FGL223491WW C1127X - 8 17.7.20210
            m = p3_7.match(line)
            if m:
                group = m.groupdict()
                ctrl_dict.setdefault('xtu_r_ds', {})
                ctrl_dict.setdefault('xtu_c_us', {})
                param = m.groupdict()['param']
                xtr_val = m.groupdict()['xtr']
                xtc_val = m.groupdict()['xtc']
                param_v = group['param']
                param = group['param'].lower().replace(" ", "_")
                if param_v == 'Per Band Status':
                    continue
                elif param_v == 'SRA Previous Speed':
                    continue
                elif param_v == 'Serial Number Near':
                    continue
                elif 'chip' in param:
                    ctrl_dict['xtu_r_ds'].setdefault('chip_vendor',{})
                    ctrl_dict['xtu_c_us'].setdefault('chip_vendor',{})
                    ctrl_dict['xtu_r_ds']['chip_vendor'][param] = group['xtr']
                    ctrl_dict['xtu_c_us']['chip_vendor'][param] = group['xtc']
                elif 'modem' in param:
                    ctrl_dict['xtu_r_ds'].setdefault('modem_vendor',{})
                    ctrl_dict['xtu_c_us'].setdefault('modem_vendor',{})
                    ctrl_dict['xtu_r_ds']['modem_vendor'][param] = group['xtr']
                    ctrl_dict['xtu_c_us']['modem_vendor'][param] = group['xtc']
                else:
                    ctrl_dict['xtu_r_ds'][param] = group['xtr']
                    ctrl_dict['xtu_c_us'][param] = group['xtc']

            # Per Band Status: D1  D2  D3  U0  U1  U2  U3
            # Line Attenuation(dB): 0.9    2.4 2.4 N / A   2.0 1.1 N / A
            # Signal  Attenuation(dB): 0.9    2.4 2.4  N / A   1.5 0.6 N / A
            # Noise Margin(dB): 19.1    18.6    18.6    N / A   5.7 5.6 N / A
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ctrl_dict.setdefault('xtu_r_ds', {})
                ctrl_dict.setdefault('xtu_c_us', {})
                ctrl_dict['xtu_r_ds'].setdefault('d1',{})
                ctrl_dict['xtu_r_ds'].setdefault('d2', {})
                ctrl_dict['xtu_r_ds'].setdefault('d3', {})
                ctrl_dict['xtu_c_us'].setdefault('u1', {})
                ctrl_dict['xtu_c_us'].setdefault('u2', {})
                ctrl_dict['xtu_c_us'].setdefault('u3', {})
                par = group['param'].lower().replace(" ", "_")
                ctrl_dict['xtu_r_ds']['d1'][par] = group['d1']
                ctrl_dict['xtu_r_ds']['d2'][par] = group['d2']
                ctrl_dict['xtu_r_ds']['d3'][par] = group['d3']
                ctrl_dict['xtu_c_us']['u1'][par] = group['u1']
                ctrl_dict['xtu_c_us']['u2'][par] = group['u2']
                ctrl_dict['xtu_c_us']['u3'][par] = group['u3']

            # Training Log: Stopped
            m = p5.match(line)
            if m:
                group = m.groupdict()
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = group['state']

            # Training Log Filename: flash:vdsllog.bin
            m = p6.match(line)
            if m:
                group = m.groupdict()
                param.lower().replace(" ", "_")
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = group['state']

            # DS Channel1    DS Channel0    US Channel1    US Channel0
            # Previous Speed: NA   0   NA  0
            # Total Cells: NA   145385538   NA  7799369
            # User Cells: NA   8598306 NA  447068
            # CRC Errors: NA  0   NA  3
            # Header Errors: NA  0   NA  1
            # Actual INP: NA 0.00    NA  0.00
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ctrl_dict.setdefault('xtu_r_ds', {})
                ctrl_dict.setdefault('xtu_c_us', {})
                ctrl_dict['xtu_r_ds'].setdefault('ds_channel1', {})
                ctrl_dict['xtu_r_ds'].setdefault('ds_channel0', {})
                ctrl_dict['xtu_c_us'].setdefault('us_channel1', {})
                ctrl_dict['xtu_c_us'].setdefault('us_channel0', {})
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict['xtu_r_ds']['ds_channel1'][param] = group['d_ch1']
                ctrl_dict['xtu_r_ds']['ds_channel0'][param] = group['d_ch0']
                ctrl_dict['xtu_c_us']['us_channel1'][param] = group['u_ch1']
                ctrl_dict['xtu_c_us']['us_channel0'][param] = group['u_ch0']

            # Speed (kbps): NA 23756   NA  1283
            # Interleave (ms): NA  0.08    NA  0.49
            m = p7_1.match(line)
            if m:
                group = m.groupdict()
                ctrl_dict.setdefault('xtu_r_ds', {})
                ctrl_dict.setdefault('xtu_c_us', {})
                ctrl_dict['xtu_r_ds'].setdefault('ds_channel1', {})
                ctrl_dict['xtu_r_ds'].setdefault('ds_channel0', {})
                ctrl_dict['xtu_c_us'].setdefault('us_channel1', {})
                ctrl_dict['xtu_c_us'].setdefault('us_channel0', {})
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict['xtu_r_ds']['ds_channel1'][param] = group['d_ch1']
                ctrl_dict['xtu_r_ds']['ds_channel0'][param] = group['d_ch0']
                ctrl_dict['xtu_c_us']['us_channel1'][param] = group['u_ch1']
                ctrl_dict['xtu_c_us']['us_channel0'][param] = group['u_ch0']

            # SRA Previous Speed: NA   0   NA  0
            m = p7_2.match(line)
            if m:
                group = m.groupdict()
                ctrl_dict.setdefault('xtu_r_ds', {})
                ctrl_dict.setdefault('xtu_c_us', {})
                ctrl_dict['xtu_r_ds'].setdefault('ds_channel1', {})
                ctrl_dict['xtu_r_ds'].setdefault('ds_channel0', {})
                ctrl_dict['xtu_c_us'].setdefault('us_channel1', {})
                ctrl_dict['xtu_c_us'].setdefault('us_channel0', {})
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict['xtu_r_ds']['ds_channel1'][param] = group['d_ch1']
                ctrl_dict['xtu_r_ds']['ds_channel0'][param] = group['d_ch0']
                ctrl_dict['xtu_c_us']['us_channel1'][param] = group['u_ch1']
                ctrl_dict['xtu_c_us']['us_channel0'][param] = group['u_ch0']

            # Reed - Solomon EC: NA  0   NA  0
            m = p7_3.match(line)
            if m:
                group = m.groupdict()
                ctrl_dict.setdefault('xtu_r_ds', {})
                ctrl_dict.setdefault('xtu_c_us', {})
                ctrl_dict['xtu_r_ds'].setdefault('ds_channel1', {})
                ctrl_dict['xtu_r_ds'].setdefault('ds_channel0', {})
                ctrl_dict['xtu_c_us'].setdefault('us_channel1', {})
                ctrl_dict['xtu_c_us'].setdefault('us_channel0', {})
                param_1 = group['param'].lower().replace(" ", "_")
                param = param_1.replace("-","_")
                ctrl_dict['xtu_r_ds']['ds_channel1'][param] = group['d_ch1']
                ctrl_dict['xtu_r_ds']['ds_channel0'][param] = group['d_ch0']
                ctrl_dict['xtu_c_us']['us_channel1'][param] = group['u_ch1']
                ctrl_dict['xtu_c_us']['us_channel0'][param] = group['u_ch0']

        return ctrl_dict

class ShowControllersSchema(MetaParser):
    """Schema for "show controllers" """
    schema = {
        "interfaces": {
            Any(): {
                'input_packet_count': int,
                'input_bytes_count': int,
                'input_mcast_pkts': int,
                'input_bcast_pkts': int,
                'input_crc_errors': int,
                'input_overruns': int,
                'runt_packets': int,
                'giant_packets': int,
                'input_pause_frames': int,
                'output_packet_count': int,
                'output_bytes_count': int,
                'output_mcast_pkts': int,
                'output_bcast_pkts': int,
                'output_underruns': int,
                'output_pause_frames': int
            }
        }
    }

# =============================================
# Parser for 'show controllers'
# =============================================

class ShowControllers(ShowControllersSchema):
    """ parser for "show controllers" """

    cli_command = "show controllers"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        config_dict = {}

        # GigabitEthernet 0/0/0 Cumulative Statistics:
        p1 = re.compile(r"^(?P<interfaces>[A-Za-z]+\s+\d[/]+\d[/]+\d)")

        # Input packet count             7628882
        p2 = re.compile(r"^Input\spacket count\s+(?P<input_packet_count>\d+)")

        # Input bytes count              1370799013
        p3 = re.compile(r"^Input\sbytes count\s+(?P<input_bytes_count>\d+)")

        # Input mcast packets            7193
        p4 = re.compile(r"^Input\smcast packets\s+(?P<input_mcast_pkts>\d+)")

        # Input bcast packets            1
        p5 = re.compile(r"^Input\sbcast packets\s+(?P<input_bcast_pkts>\d+)")

        # Input CRC errors               0
        p6 = re.compile(r"^Input\sCRC errors\s+(?P<input_crc_errors>\d+)")

        # Input overruns                 3
        p7 = re.compile(r"^Input\soverruns\s+(?P<input_overruns>\d+)")

        # Runt packets                   0
        p8 = re.compile(r"^Runt\spackets\s+(?P<runt_packets>\d+)")

        # Giant packets                  0
        p9 = re.compile(r"^Giant\spackets\s+(?P<giant_packets>\d+)")

        # Input pause frames             0
        p10 = re.compile(r"^Input\spause frames\s+(?P<input_pause_frames>\d+)")

        # Output packet count            4546146635
        p11 = re.compile(r"^Output\spacket count\s+(?P<output_packet_count>\d+)")

        # Output bytes count             2537511523512
        p12 = re.compile(r"^Output\sbytes count\s+(?P<output_bytes_count>\d+)")

        # Output mcast packets           7189
        p13 = re.compile(r"^Output\smcast packets\s+(?P<output_mcast_pkts>\d+)")

        # Output bcast packets           112
        p14 = re.compile(r"^Output\sbcast packets\s+(?P<output_bcast_pkts>\d+)")

        # Output underruns               0
        p15 = re.compile(r"^Output\sunderruns\s+(?P<output_underruns>\d+)")

        # Output pause frames            0
        p16 = re.compile(r"^Output\spause frames\s+(?P<output_pause_frames>\s+\d+)")

        for line in output.splitlines():

            # GigabitEthernet 0/0/0 Cumulative Statistics:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interfaces = group["interfaces"]
                interfaces_dict = config_dict.setdefault('interfaces', {}).setdefault(interfaces, {})

            # Input packet count             7628882
            m = p2.match(line)
            if m:
                group = m.groupdict()
                input_packet_count = int(group["input_packet_count"])
                interfaces_dict['input_packet_count'] = input_packet_count

            # Input bytes count              1370799013
            m = p3.match(line)
            if m:
                group = m.groupdict()
                input_bytes_count = int(group["input_bytes_count"])
                interfaces_dict['input_bytes_count'] = input_bytes_count

            # Input mcast packets            7193
            m = p4.match(line)
            if m:
                group = m.groupdict()
                input_mcast_pkts = int(group["input_mcast_pkts"])
                interfaces_dict['input_mcast_pkts'] = input_mcast_pkts

            # Input bcast packets            1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                input_bcast_pkts = int(group["input_bcast_pkts"])
                interfaces_dict['input_bcast_pkts'] = input_bcast_pkts

            # Input CRC errors               0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                input_crc_errors = int(group["input_crc_errors"])
                interfaces_dict['input_crc_errors'] = input_crc_errors

            # Input overruns                 3
            m = p7.match(line)
            if m:
                group = m.groupdict()
                input_overruns = int(group["input_overruns"])
                interfaces_dict['input_overruns'] = input_overruns

            # Runt packets                   0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                runt_packets = int(group["runt_packets"])
                interfaces_dict['runt_packets'] = runt_packets

            # Giant packets                  0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                giant_packets = int(group["giant_packets"])
                interfaces_dict['giant_packets'] = giant_packets

            # Input pause frames             0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                input_pause_frames = int(group["input_pause_frames"])
                interfaces_dict['input_pause_frames'] = input_pause_frames

            # Output packet count            4546146635
            m = p11.match(line)
            if m:
                group = m.groupdict()
                output_packet_count = int(group["output_packet_count"])
                interfaces_dict['output_packet_count'] = output_packet_count

            # Output bytes count             2537511523512
            m = p12.match(line)
            if m:
                group = m.groupdict()
                output_bytes_count = int(group["output_bytes_count"])
                interfaces_dict['output_bytes_count'] = output_bytes_count

            # Output mcast packets           7189
            m = p13.match(line)
            if m:
                group = m.groupdict()
                output_mcast_pkts = int(group["output_mcast_pkts"])
                interfaces_dict['output_mcast_pkts'] = output_mcast_pkts

            # Output bcast packets           112
            m = p14.match(line)
            if m:
                group = m.groupdict()
                output_bcast_pkts = int(group["output_bcast_pkts"])
                interfaces_dict['output_bcast_pkts'] = output_bcast_pkts

            # Output underruns               0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                output_underruns = int(group["output_underruns"])
                interfaces_dict['output_underruns'] = output_underruns

            # Output pause frames            0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                output_pause_frames = int(group["output_pause_frames"])
                interfaces_dict['output_pause_frames'] = output_pause_frames

        return config_dict
    

class ShowControllerEthernetControllerSchema(MetaParser):
    """Schema for show controller ethernet-controller {interface}"""

    schema = {
        'interface': {
            Any(): {
                'last_updated': str,
                'transmit': {
                    Any(): int
                },
                'receive': {
                    Any(): int
                }
            }
        }

    }


class ShowControllerEthernetController(ShowControllerEthernetControllerSchema):
    """Parser for show controller ethernet-controller {interface}"""

    cli_command = ['show controllers ethernet-controller', 
        'show controllers ethernet-controller {interface}']

    def cli(self, interface=None, output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)
        
        # Transmit                  GigabitEthernet1/0/3          Receive 
        p1 = re.compile(r'^Transmit\s+(?P<interface>[\w\/]+)\s+Receive$')

        # 32199124 Total bytes                     1608886 Total bytes              
        # 78979 Unicast frames                        2 Unicast frames           
        # 5054660 Unicast bytes                       136 Unicast bytes 
        p2 = re.compile(r'^(?P<transmit_value>\d+)\s+(?P<transmit_key_string>[\w\s\>\(\)]+(frame[s]*|bytes|dropped|truncated|successful))\s+(?P<receive_value>\d+)\s+(?P<receive_key_string>[\w\s\>\(\)]+)$')

        # 0 Gold frames successful   
        # 0 1 collision frames  
        p3 = re.compile(r'^(?P<transmit_value>\d+)\s+(?P<transmit_key_string>[\w\s\>\(\)]+)$')
        
        # LAST UPDATE 561 msecs AGO
        p4 = re.compile(r'^LAST UPDATE (?P<last_updated>[\w\s]+) AGO$')
        
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Transmit                  GigabitEthernet1/0/3          Receive 
            m = p1.match(line)
            if m:
                interface = Common.convert_intf_name(m.groupdict()['interface'])
                int_dict = ret_dict.setdefault('interface', {}).setdefault(interface, {})
                continue
            
            # 32199124 Total bytes                     1608886 Total bytes              
            # 78979 Unicast frames                        2 Unicast frames           
            # 5054660 Unicast bytes                       136 Unicast bytes
            m = p2.match(line)
            if m:
                trans_dict = int_dict.setdefault('transmit', {})
                receive_dict = int_dict.setdefault('receive', {})
                transmit_key_string = m.groupdict()['transmit_key_string'].strip().replace(' ', '_').lower()
                receive_key_string = m.groupdict()['receive_key_string'].strip().replace(' ', '_').lower()
                trans_dict.setdefault(transmit_key_string, int(m.groupdict()['transmit_value']))
                receive_dict.setdefault(receive_key_string, int(m.groupdict()['receive_value']))
                continue
            
            # 0 Gold frames successful   
            # 0 1 collision frames 
            m = p3.match(line)
            if m:
                transmit_key_string = m.groupdict()['transmit_key_string'].replace(' ', '_').lower()
                int_dict.setdefault('transmit', {}).setdefault(transmit_key_string, int(m.groupdict()['transmit_value']))
                continue
        
            # LAST UPDATE 561 msecs AGO
            m = p4.match(line)
            if m:
                int_dict.setdefault('last_updated', m.groupdict()['last_updated'])
        
        return ret_dict
class ShowControllersEthernetControllerSchema(MetaParser):
    """
        Schema for show controllers ethernet-controller {interface}
    """

    schema = {
        'interface': {
            Any() : {
                'transmit': {
                    Any() : int
                },
                'receive': {
                    Any() : int
                },
                'last_update_msecs': int 
            }
        }
    }


class ShowControllersEthernetController(ShowControllersEthernetControllerSchema):
    """
        parser for show controllers ethernet-controller {interface}
    """

    cli_command = ['show controllers ethernet-controller', 'show controllers ethernet-controller {interface}']

    def cli(self, interface=None, output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]

            output = self.device.execute(cmd)

        # Transmit                  GigabitEthernet1/0/1          Receive   
        p1 = re.compile(r'^Transmit\s+(?P<interface>[\w\/\d\.]+)\s+Receive$')

        # 0 Total bytes                           0 Total bytes              
        # 0 Unicast frames                        0 Unicast frames       
        p2 = re.compile(r'^(?P<transmit_value>\d+)\s+(?P<transmit_key_name>.+)\s\s+'
                r'(?P<receive_value>\d+)\s+(?P<receive_key_name>.+)$')

        # 0 4 collision frames 
        p3 = re.compile(r'^(?P<transmit_value>\d+)\s+(?P<transmit_key_name>.+)$')

        # LAST UPDATE 65017966 msecs AGO
        p4 = re.compile(r'^LAST UPDATE (?P<last_update_msecs>\d+) msecs AGO$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Transmit                  GigabitEthernet1/0/1          Receive 
            m = p1.match(line)
            if m:
                int_dict = ret_dict.setdefault('interface', {}).setdefault(\
                    Common.convert_intf_name(m.groupdict()['interface']), {})
                transmit_dict = int_dict.setdefault('transmit', {})
                receive_dict = int_dict.setdefault('receive', {})
                continue

            # 0 Total bytes                           0 Total bytes              
            # 0 Unicast frames                        0 Unicast frames 
            m = p2.match(line)
            if m:
                groupdict = m.groupdict()
                transmit_key_name = groupdict['transmit_key_name'].strip().lower().\
                    replace(' ', '_').replace('>', 'greater').replace('(', '').replace(')', '')
                transmit_dict[transmit_key_name] = int(groupdict['transmit_value'])
                receive_key_name = groupdict['receive_key_name'].strip().lower().\
                    replace(' ', '_').replace('>', 'greater').replace('(', '').replace(')', '')
                receive_dict[receive_key_name] = int(groupdict['receive_value'])
                continue

            # 0 4 collision frames 
            m = p3.match(line)
            if m:
                groupdict = m.groupdict()
                transmit_key_name = groupdict['transmit_key_name'].strip().lower().\
                    replace(' ', '_').replace('>', 'greater').replace('(', '').replace(')', '')
                transmit_dict[transmit_key_name] = int(groupdict['transmit_value'])
                continue

            # LAST UPDATE 65017966 msecs AGO
            m = p4.match(line)
            if m:
                int_dict['last_update_msecs'] = int(m.groupdict()['last_update_msecs'])

        return ret_dict


# =============================================
# Parser for 'show controller vdsl {interface} local'
# =============================================

class ShowControllerVDSLlocalSchema(MetaParser):
    """Schema for show controller VDSL {interface} local"""

    schema = {
        'sfp_vendor_pid': str,
        'sfp_vendor_sn': str,
        'firmware_embedded_in_ios-xe': str,
        'running_firmware_version': str,
        'management_link': str,
        'dsl_status': str,
        'dumping_internal_info': str,
        'dying_gasp': str,
        'dumping_delt_info': str,
        
    }

class ShowControllerVDSLlocal(ShowControllerVDSLlocalSchema):
    """
    Parser for show controller VDSL {interface} local
    """

    cli_command = 'show controller VDSL {interface} local'

    def cli(self, interface=None, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(interface=interface))
        else:
            out = output

        
        
        #SFP Vendor PID:                 SFPV5311TR
        p1 = re.compile(r'^(?P<param>\w*\s*\w*\s*PID):\s+(?P<vl>.+)')
        
        #SFP Vendor SN:                  MET211611AC
        p2 = re.compile(r'^(?P<param>\w*\s*\w*\s*SN):\s+(?P<vl>.+)')
        
        #Firmware embedded in IOS-XE:    1_62_8463
        p3 = re.compile(r'^(?P<param>\w*\s*\w*\s*\w*\s*IOS-XE):\s+(?P<vl>.+)')
        
        #Running Firmware Version:       1_62_8463
        p4 = re.compile(r'^(?P<param>\w*\s*\w*\s*Version\s*):\s+(?P<vl>.+)')
        
        #Management Link:                up
        p5 = re.compile(r'^(?P<param>\w*\s*Link\s*):\s+(?P<state>.+)')
        
        #DSL Status:                     showtime
        p6 = re.compile(r'^(?P<param>DSL\s*\w*):\s+(?P<state>\w+)')
        
        #Dumping internal info:          idle
        p7 = re.compile(r'^(?P<param>\w*\s*internal\s*\w*\s*):\s+(?P<state>\w+)')
        
        #Dying Gasp:                     disarmed
        p8 = re.compile(r'^(?P<param>\w*\s*Gasp):\s+(?P<state>\w+)')
        
        #Dumping DELT info:              idle
        p9 = re.compile(r'^(?P<param>\w*\s*DELT\s*\w*\s*):\s+(?P<state>\w+)')
        
        ctrl_dict = {}
       
        for lines in out.splitlines():
            line = lines.strip()

            #SFP Vendor PID:                 SFPV5311TR
            m = p1.match(line)
            if m:
                group = m.groupdict()
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = group['vl']
                continue

            #SFP Vendor SN:                  MET211611AC
            m = p2.match(line)
            if m:
                group = m.groupdict()
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = group['vl']
                continue

            #Firmware embedded in IOS-XE:    1_62_8463
            m = p3.match(line)
            if m:
                group = m.groupdict()
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = group['vl']
                continue
                
            
            # Running Firmware Version:       1_62_8463
            m = p4.match(line)
            if m:
                group = m.groupdict()
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = group['vl']
                continue
                

            #Management Link:                up
            m = p5.match(line)
            if m:
                group = m.groupdict()
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = group['state']
                continue
            # DSL Status:                     showtime
            m = p6.match(line)
            if m:
                group = m.groupdict()
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = group['state']
                continue
                
            #Dumping internal info:          idle    
            m = p7.match(line)
            if m:
                group = m.groupdict()
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = group['state']
                continue

            #Dying Gasp:                     disarmed
            m = p8.match(line)
            if m:
                group = m.groupdict()
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = group['state']
                continue
               
            #Dumping DELT info:              idle
            m = p9.match(line)
            if m:
                group = m.groupdict()
                param = group['param'].lower().replace(" ", "_")
                ctrl_dict[param] = group['state']
                continue

        return ctrl_dict
        
class ShowControllersEthernetControllersPhyDetailSchema(MetaParser):

    """ Schema for:
        * show controllers ethernet-controller {interface} phy detail
    """
    schema = {
        'interface': str,
        'if_id': str,
        Optional('phy_registers'): {
            Any():
                {
                    'register_number': str,
                    'hex_bit_value': str,
                    'register_name': str,
                    'bits': str
                }
            }
        }


class ShowControllersEthernetControllersPhyDetail(ShowControllersEthernetControllersPhyDetailSchema):
    """
    Parser for :
        * show controllers ethernet-controller {interface} phy detail
    """

    cli_command = 'show controllers ethernet-controller {interface} phy detail'

    def cli(self, interface='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        parsed_dict = {}
        registers_dict = {}
        reg_index = 0  # Registers ID could be the same, hence abstraction iterator is needed

        # --------------------------------------------------------------
        # Regex patterns
        # --------------------------------------------------------------
        # Gi1/0/1 (if_id: 75)
        int_reg = re.compile(r'(?P<interface>[a-zA-Z]+\d+(?:\/\d+)+)\s\(if_id\:\s(?P<if_id>\d+)\)')

        #  0000 : 1140                  Control Register :  0001 0001 0100 0000
        #  0001 : 796d                    Control STATUS :  0111 1001 0110 1101
        registers_reg = re.compile(
            r'(?P<register_number>\S{4})\s\:\s(?P<hex_bit_value>\S{4})\s+(?P<register_name>.*)\s\:\s+(?P<bits>.*)')

        # --------------------------------------------------------------
        # Build the parsed output
        # --------------------------------------------------------------
        for line in output.splitlines():
            line = line.strip()

            # Gi1/0/1 (if_id: 75)
            int_name = int_reg.match(line)
            if int_name:
                group = int_name.groupdict()
                for key in group.keys():
                    if group[key]:
                        parsed_dict[key] = group[key]
                continue

            #  0000 : 1140                  Control Register :  0001 0001 0100 0000
            #  0001 : 796d                    Control STATUS :  0111 1001 0110 1101
            register_line = registers_reg.match(line)
            if register_line:
                group = register_line.groupdict()
                registers_dict[str(reg_index)] = {'register_number': group['register_number'],
                                                  'hex_bit_value': group['hex_bit_value'],
                                                  'register_name': group['register_name'],
                                                  'bits': group['bits'].replace(' ', '')}
                reg_index += 1
                continue
        if registers_dict:
            parsed_dict['phy_registers'] = registers_dict
        return parsed_dict




class ShowControllerEthernetControllerLinkstatusSchema(MetaParser):
    """Schema for show  platform  hardware fed  switch  active  npu  slot  1  port 23 link_status"""

    schema = {
        'interface':{
            'interface_name': str,
            'if_id': int,
        },
        'mac_link_status':{
            'mpp_port_details': {
                    Any():Or(int,str),
            },
            'autoneg_details':{
                    Any():Or(int,str),
            },
            'autoneg_status': {
                    Any():Or(int,str),
            },
            'mib_counters': {
                    Any(): int,
            },
        },
        'port': int,
        'cmd': str,
        'rc': str,
        'rsn': str,
        'phy_link_status':{
            'phy_configuration':{
                    Any():Or(int,str),
            },
            'phy_status':{
                    Any():Or(int,str),
            },
        },
 }



class ShowControllerEthernetControllerLinkstatus(ShowControllerEthernetControllerLinkstatusSchema):
    """
    ShowPlatformSoftwareCpmSwitchActiveB0CountersInterfaceIsis
    """

    cli_command = 'show controllers ethernet-controller {interface} link-status'

    def cli(self, interface, output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        ret_dict = {}

        #Gi1/0/5 (if_id: 1036)
        p0 = re.compile(r'^(?P<name>\S+) +\(if\_id\: +(?P<if_id>\d+)\)$')

        #******* MAC LINK STATUS ************
        p1 = re.compile(r'^\*+\s*MAC +LINK +STATUS\s*\*+$')

        #MPP PORT DETAILS
        p2 =  re.compile(r'^MPP +PORT +DETAILS$')

        #link_state: 1 pcs_status: 0  high_ber: 0
        p3 = re.compile(r'^link_state\: +(?P<link_state>\d+) +pcs_status\: +(?P<pcs_status>\d+) +high_ber\: +(?P<high_ber>\d+)$')

        #get_state = LINK_UP
        p4 = re.compile(r'^get_state +\= +(?P<get_state>.*)$')

        # Autoneg Details
        p5 = re.compile(r'^Autoneg +Details$')

        #Autoneg Status
        p6 = re.compile(r'^Autoneg +Status$')

        #MIB counters
        p7 = re.compile(r'^MIB +counters$')

        #Genral - Speed:         speed_gbps1
        p8 = re.compile(r'^(?P<key>[\s*\w]+.*)\: +(?P<value>[\S\s]+.*)$')

        #Port = 22 cmd = (port_diag unit 0 port 22 slot 0) rc = 0x0 rsn = success
        p9 = re.compile(r'^Port +\= +(?P<port>\d+) +cmd +\= +\((?P<cmd>[\s*\w]+)\) +rc +\= +(?P<rc>\w+) +rsn +\= +(?P<rsn>\w+)$')

        #PHY LINK STATUS
        p10 = re.compile(r'^\*+\s*PHY +LINK +STATUS\s*\*+$')

        #Phy Configuration :
        p11 = re.compile(r'^Phy +Configuration +\:$')

        #Phy Status :
        p12 = re.compile(r'^Phy +Status +\:$')

        for line in output.splitlines():
            line = line.strip()


            #Gi1/0/5 (if_id: 1036)
            m = p0.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('interface', {})
                root_dict['interface_name'] = group['name']
                root_dict['if_id'] = int(group['if_id'])
                continue


            #******* MAC LINK STATUS ************
            m = p1.match(line)
            if m:
                root_dict =  ret_dict.setdefault('mac_link_status', {})
                continue

            #MPP PORT DETAILS
            m = p2.match(line)
            if m:
                root_dict =  ret_dict.setdefault('mac_link_status', {}).setdefault('mpp_port_details', {})
                continue


            ##link_state: 1 pcs_status: 0  high_ber: 0'
            m = p3.match(line)
            if m:
                group = m.groupdict()
                root_dict['link_state'] = int(group['link_state'])
                root_dict['pcs_status'] = int(group['pcs_status'])
                root_dict['high_ber'] = int(group['high_ber'])
                continue

            #get_state = LINK_UP
            m = p4.match(line)
            if m:
                group = m.groupdict()
                root_dict['get_state'] = group['get_state'].strip()
                continue

            #Autoneg Details
            m = p5.match(line)
            if m:
                root_dict = ret_dict.setdefault('mac_link_status', {}).setdefault('autoneg_details', {})
                continue

            #Autoneg Status
            m = p6.match(line)
            if m:
                root_dict = ret_dict.setdefault('mac_link_status', {}).setdefault('autoneg_status', {})
                continue

            #MIB counters
            m = p7.match(line)
            if m:
                root_dict = ret_dict.setdefault('mac_link_status', {}).setdefault('mib_counters', {})
                continue


            #Genral - Speed:         speed_gbps1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].strip().lower().replace(":","").replace("-",'_').replace(" ",'_')
                if group['value'].isdigit():
                    root_dict.update({key: int(group['value'])})
                else:
                    root_dict.update({key: group['value']})
                continue

            #Port = 3 cmd = (port_diag unit 0 port 3 slot 0) rc = 0x0 rsn = success
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict['port'] = int(group['port'])
                ret_dict['cmd'] = group['cmd']
                ret_dict['rc'] = group['rc']
                ret_dict['rsn'] = group['rsn']
                continue

            #******* PHY LINK STATUS ************
            m = p10.match(line)
            if m:
                root_dict = ret_dict.setdefault('phy_link_status', {})
                continue

            #Phy Configuration :
            m = p11.match(line)
            if m:
                root_dict =  ret_dict.setdefault('phy_link_status', {}).setdefault('phy_configuration', {})
                continue

            #Phy Status :
            m = p12.match(line)
            if m:
                root_dict = ret_dict.setdefault('phy_link_status', {}).setdefault('phy_status', {})
                continue

        return ret_dict



class ShowControllerEthernetControllerLinkstatusSchema(MetaParser):
    """Schema for show  platform  hardware fed  switch  active  npu  slot  1  port 23 link_status"""

    schema = {
        'interface':{
            'interface_name': str,
            'if_id': int,
        },
        'mac_link_status':{
            'mpp_port_details': {
                    Any():Or(int,str),
            },
            'autoneg_details':{
                    Any():Or(int,str),
            },
            'autoneg_status': {
                    Any():Or(int,str),
            },
            'mib_counters': {
                    Any(): int,
            },
        },
        'port': int,
        'cmd': str,
        'rc': str,
        'rsn': str,
        'phy_link_status':{
            'phy_configuration':{
                    Any():Or(int,str),
            },
            'phy_status':{
                    Any():Or(int,str),
            },
        },
 }



class ShowControllerEthernetControllerLinkstatus(ShowControllerEthernetControllerLinkstatusSchema):
    """
    ShowPlatformSoftwareCpmSwitchActiveB0CountersInterfaceIsis
    """

    cli_command = 'show controllers ethernet-controller {interface} link-status'

    def cli(self, interface, output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        ret_dict = {}

        #Gi1/0/5 (if_id: 1036)
        p0 = re.compile(r'^(?P<name>\S+) +\(if\_id\: +(?P<if_id>\d+)\)$')

        #******* MAC LINK STATUS ************
        p1 = re.compile(r'^\*+\s*MAC +LINK +STATUS\s*\*+$')

        #MPP PORT DETAILS
        p2 =  re.compile(r'^MPP +PORT +DETAILS$')

        #link_state: 1 pcs_status: 0  high_ber: 0
        p3 = re.compile(r'^link_state\: +(?P<link_state>\d+) +pcs_status\: +(?P<pcs_status>\d+) +high_ber\: +(?P<high_ber>\d+)$')

        #get_state = LINK_UP
        p4 = re.compile(r'^get_state +\= +(?P<get_state>.*)$')

        # Autoneg Details
        p5 = re.compile(r'^Autoneg +Details$')

        #Autoneg Status
        p6 = re.compile(r'^Autoneg +Status$')

        #MIB counters
        p7 = re.compile(r'^MIB +counters$')

        #Genral - Speed:         speed_gbps1
        p8 = re.compile(r'^(?P<key>[\s*\w]+.*)\: +(?P<value>[\S\s]+.*)$')

        #Port = 22 cmd = (port_diag unit 0 port 22 slot 0) rc = 0x0 rsn = success
        p9 = re.compile(r'^Port +\= +(?P<port>\d+) +cmd +\= +\((?P<cmd>[\s*\w]+)\) +rc +\= +(?P<rc>\w+) +rsn +\= +(?P<rsn>\w+)$')

        #PHY LINK STATUS
        p10 = re.compile(r'^\*+\s*PHY +LINK +STATUS\s*\*+$')

        #Phy Configuration :
        p11 = re.compile(r'^Phy +Configuration +\:$')

        #Phy Status :
        p12 = re.compile(r'^Phy +Status +\:$')

        for line in output.splitlines():
            line = line.strip()


            #Gi1/0/5 (if_id: 1036)
            m = p0.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('interface', {})
                root_dict['interface_name'] = group['name']
                root_dict['if_id'] = int(group['if_id'])
                continue


            #******* MAC LINK STATUS ************
            m = p1.match(line)
            if m:
                root_dict =  ret_dict.setdefault('mac_link_status', {})
                continue

            #MPP PORT DETAILS
            m = p2.match(line)
            if m:
                root_dict =  ret_dict.setdefault('mac_link_status', {}).setdefault('mpp_port_details', {})
                continue


            ##link_state: 1 pcs_status: 0  high_ber: 0'
            m = p3.match(line)
            if m:
                group = m.groupdict()
                root_dict['link_state'] = int(group['link_state'])
                root_dict['pcs_status'] = int(group['pcs_status'])
                root_dict['high_ber'] = int(group['high_ber'])
                continue

            #get_state = LINK_UP
            m = p4.match(line)
            if m:
                group = m.groupdict()
                root_dict['get_state'] = group['get_state'].strip()
                continue

            #Autoneg Details
            m = p5.match(line)
            if m:
                root_dict = ret_dict.setdefault('mac_link_status', {}).setdefault('autoneg_details', {})
                continue

            #Autoneg Status
            m = p6.match(line)
            if m:
                root_dict = ret_dict.setdefault('mac_link_status', {}).setdefault('autoneg_status', {})
                continue

            #MIB counters
            m = p7.match(line)
            if m:
                root_dict = ret_dict.setdefault('mac_link_status', {}).setdefault('mib_counters', {})
                continue


            #Genral - Speed:         speed_gbps1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].strip().lower().replace(":","").replace("-",'_').replace(" ",'_')
                if group['value'].isdigit():
                    root_dict.update({key: int(group['value'])})
                else:
                    root_dict.update({key: group['value']})
                continue

            #Port = 3 cmd = (port_diag unit 0 port 3 slot 0) rc = 0x0 rsn = success
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict['port'] = int(group['port'])
                ret_dict['cmd'] = group['cmd']
                ret_dict['rc'] = group['rc']
                ret_dict['rsn'] = group['rsn']
                continue

            #******* PHY LINK STATUS ************
            m = p10.match(line)
            if m:
                root_dict = ret_dict.setdefault('phy_link_status', {})
                continue

            #Phy Configuration :
            m = p11.match(line)
            if m:
                root_dict =  ret_dict.setdefault('phy_link_status', {}).setdefault('phy_configuration', {})
                continue

            #Phy Status :
            m = p12.match(line)
            if m:
                root_dict = ret_dict.setdefault('phy_link_status', {}).setdefault('phy_status', {})
                continue

        return ret_dict
        

       
class ShowControllersEthernetControllerPortInfoSchema(MetaParser):
    """
    Schema for 'show controllers ethernet-controller tenGigabitEthernet {interface} port-info'
    """
    schema = {
        'interface': str,
        'if_id': int,
        'port_context_information': {
            'lpn': int,
            'asic_num': int,
            'asic_port': int,
            'is_init': int,
            'context_name': str,
            'is_disabled': int,
            'is_bc_inserted': int,
            'is_bc_forced': int,
            'is_qsa_module': int,
            'admin_link_state': int,
            'default_speed': int,
            'duplex': int,
            'speed': int,
            'max_speed': int,
            'flowcontrol': int,
            'fec_mode': int,
            'poll_link_status': int,
        }
    }


class ShowControllersEthernetControllerPortInfo(ShowControllersEthernetControllerPortInfoSchema):
    """Parser for 'show controllers ethernet-controller {interface} port-info'"""
    
    cli_command = 'show controllers ethernet-controller {interface} port-info'
    
    def cli(self, interface, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))
        else:
            output = output
        
        ret_dict = {}
        
        # Te1/0/13 (if_id: 1043)
        p1 = re.compile(r'^(?P<interface>\S+) +\(if_id\: +(?P<if_id>\d+)\)$')
        
        # Port Context Information
        p2  = re.compile(r'^Port +Context +Information$')
        
        # Lpn ........................ [13]
        p3 = re.compile(r'^Lpn\s+\.+\s+\[(?P<lpn>\d+)\]$')
        
        # AsicNum .................... [1]
        p4 = re.compile(r'^AsicNum\s+\.+\s+\[(?P<asic_num>\d+)\]$')
        
        # AsicPort ................... [-604733568]
        p5 = re.compile(r'AsicPort\s+\.+\s+\[(?P<asic_port>\-*\d+)\]$')
        
        # IsInit ..................... [1]
        p6 = re.compile(r'^IsInit\s+\.+\s+\[(?P<is_init>\d+)\]$')
        
        # ContextName ................ [Te1/0/13]
        p7 = re.compile(r'^ContextName\s+\.+\s+\[(?P<context_name>\S+)\]$')
        
        # IsDisabled ................. [0]
        p8 = re.compile(r'^IsDisabled\s+\.+\s+\[(?P<is_disabled>\d+)\]$')
        
        # IsBc Inserted .............. [0]
        p9 = re.compile(r'^IsBc Inserted\s+\.+\s+\[(?P<is_bc_inserted>\d+)\]$')
        
        # IsBc Forced ................ [0]
        p10 = re.compile(r'^IsBc Forced\s+\.+\s+\[(?P<is_bc_forced>\d+)\]$')
        
        # IsQsa Module ............... [0]
        p11 = re.compile(r'^IsQsa Module\s+\.+\s+\[(?P<is_qsa_module>\d+)\]$')
        
        # Admin link state ........... [1]
        p12 = re.compile(r'^Admin link state\s+\.+\s+\[(?P<admin_link_state>\d+)\]$')
        
        # default_speed .............. [10000000]
        p13 = re.compile(r'^default_speed\s+\.+\s+\[(?P<default_speed>\d+)\]$')
        
        # duplex ..................... [2]
        p14 = re.compile(r'^duplex\s+\.+\s+\[(?P<duplex>\d+)\]$')
        
        # speed ...................... [1000000]
        p15 = re.compile(r'^speed\s+\.+\s+\[(?P<speed>\d+)\]$')
        
        # max speed .................. [10000000]
        p16 = re.compile(r'^max speed\s+\.+\s+\[(?P<max_speed>\d+)\]$')
        
        # Flowcontrol ................ [2]
        p17 = re.compile(r'^Flowcontrol\s+\.+\s+\[(?P<flowcontrol>\d+)\]$')
        
        # fec mode ................... [0]
        p18 = re.compile(r'^fec mode\s+\.+\s+\[(?P<fec_mode>\d+)\]$')
        
        # Poll link status ........... [1]
        p19 = re.compile(r'^Poll link status\s+\.+\s+\[(?P<poll_link_status>\d+)\]$')
        
        for line in output.splitlines():
            line = line.strip()
            
            # Te1/0/13 (if_id: 1043)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface_name =  Common.convert_intf_name(group['interface'])
                ret_dict['interface'] = interface_name
                ret_dict['if_id'] = int(group['if_id'])                
                continue
            
            #Port Context Information
            m = p2.match(line)
            if m:
                curr_dict = ret_dict.setdefault('port_context_information', {})
                continue 
            
            #Lpn ........................ [13]
            m = p3.match(line)
            if m:
                group = m.groupdict()
                curr_dict['lpn'] = int(group['lpn'])
                continue
            
            # AsicNum .................... [1]
            m = p4.match(line)
            if m:
                group = m.groupdict()
                curr_dict['asic_num'] = int(group['asic_num'])
                continue
            
            # AsicPort ................... [-604733568]
            m = p5.match(line)
            if m:
                group = m.groupdict()
                curr_dict['asic_port'] = int(group['asic_port'])
                continue
            
            # IsInit ..................... [1]
            m = p6.match(line)
            if m:
                group = m.groupdict()
                curr_dict['is_init'] = int(group['is_init'])
                continue
                
            # ContextName ................ [Te1/0/13]    
            m = p7.match(line)
            if m:
                group = m.groupdict()
                curr_dict['context_name'] = group['context_name']
                continue
                
            # IsDisabled ................. [0]    
            m = p8.match(line)
            if m:
                group = m.groupdict()
                curr_dict['is_disabled'] = int(group['is_disabled'])
                continue
                
            # IsBc Inserted .............. [0]    
            m = p9.match(line)
            if m:
                group = m.groupdict()
                curr_dict['is_bc_inserted'] = int(group['is_bc_inserted'])
                continue            
            
            # IsBc Forced ................ [0]
            m = p10.match(line)
            if m:
                group = m.groupdict()
                curr_dict['is_bc_forced'] = int(group['is_bc_forced'])
                continue
            
            # IsQsa Module ............... [0]
            m = p11.match(line)
            if m:
                group = m.groupdict()
                curr_dict['is_qsa_module'] = int(group['is_qsa_module'])
                continue
            
            # Admin link state ........... [1]
            m = p12.match(line)
            if m:
                group = m.groupdict()
                curr_dict['admin_link_state'] = int(group['admin_link_state'])
                continue
            
            # default_speed .............. [10000000]
            m = p13.match(line)
            if m:
                group = m.groupdict()
                curr_dict['default_speed'] = int(group['default_speed'])
                continue
            
            # duplex ..................... [2]  
            m = p14.match(line)
            if m:
                group = m.groupdict()
                curr_dict['duplex'] = int(group['duplex'])
                continue
            
            # speed ...................... [1000000] 
            m = p15.match(line)
            if m:
                group = m.groupdict()
                curr_dict['speed'] = int(group['speed'])
                continue
            
            # max speed .................. [10000000]  
            m = p16.match(line)
            if m:
                group = m.groupdict()
                curr_dict['max_speed'] = int(group['max_speed'])
                continue
            
            # Flowcontrol ................ [2]
            m = p17.match(line)
            if m:
                group = m.groupdict()
                curr_dict['flowcontrol'] = int(group['flowcontrol'])
                continue
            
            # fec mode ................... [0] 
            m = p18.match(line)            
            if m:
                group = m.groupdict()
                curr_dict['fec_mode'] = int(group['fec_mode'])
                continue
            
            # Poll link status ........... [1] 
            m = p19.match(line)
            if m:
                group = m.groupdict()
                curr_dict['poll_link_status'] = int(group['poll_link_status'])
                continue
        
        return ret_dict
        
class ShowControllerEthernetControllerInterfaceMacSchema(MetaParser):
    """Schema for show  platform  hardware fed  switch  active  npu  slot  1  port 23 link_status"""
    
    schema = {
        'npu_pdsf_procagent_get_eye_common':str,
        'mpp_port_detai1': {
            Any(): {
                'mac_state_histogram': {
                    Any(): Or(int,str),
                },
                'mac_port_config': {
                   Any(): Or(int,str),
                },                    
                'mac_port_status': {
                    Any(): Or(int,str),
                },
                'mib_counters': {
                    Any(): Or(int,str),
                },     
                Optional('state_transition_history'): {
                    Any():{
                       'state': str,
                       'timestamp': str,
                    },    
                },    
            },
        },
        'multiport_detail': {
            Any(): {
                'device_info': {
                    Any(): str,
                },
                'mac_state_histogram':{
                    Any(): Or(int,str),
                    'serdes_0': {
                        Any(): Or(int,str),
                    },
                },
                'mac_port_config': {
                    Any(): Or(int,str),
                    'serdes_info': {
                        Any(): Or(int,str),
                    },
                },
                'mac_port_status': {
                    'am_lock': {
                        Any(): str,
                    },    
                    Any(): Or(int,str),
                    'mac_pcs_lane_mapping': {
                        Any(): Or(int,str),
                    },
                },                    
                'mac_port_soft_state': {
                    Any(): Or(int,str),
                },
                'mib_counters': {
                    Any(): Or(int,str),
                    Optional('tx_mac_tc_fc_frames_ok'): {
                        Any(): Or(int,str),
                    },
                    Optional('tx_xoff_state_duration'): {
                        Any(): Or(int,str),
                    },
                    Optional('rx_mac_tc_fc_frames_ok'): {
                        Any(): Or(int,str),
                    },
                    Optional('rx_xoff_state_duration'): {
                        Any(): Or(int,str),
                    },                 
                },
                'test_mode': {
                    Any(): Or(int,str),
                },
                'state_transition_history': {
                    Any():{
                       'state': str,
                       'timestamp': str,
                    },    
                },
                'serdes_parameters': {
                    'index_0': {
                        Any(): Or(int,str),
                    },
                },
                'serdes_config':{
                    'serdes_settings': {
                        'rx_settings': {
                            Any(): Or(int,str),
                            'targ_shadow':{
                                Any(): Or(int,str),
                            }    
                        },
                        'tx_settings': {
                            Any(): Or(int,str),
                            'tx_fir': {
                                Any(): Or(int,str),
                            },    
                        },
                        'flow_chart_settings': {
                            Any(): Or(int,str),
                        },
                    },    
                },
                'serdes_status':{
                    'firmware_version': {
                        Any(): str,
                    },
                    'rx_status': {
                        Any(): Or(int,str),
                        'firs': {
                            Any(): Or(int,str),
                        }    
                    },
                    'fw_rx_status': {
                        Any(): Or(int,str),
                    },
                    'fir_shadow': {
                        Any(): Or(int,str),
                    },    
                },    
                'eye_capture':{
                    'veye_data': {
                        Any(): Or(int,str),
                        'veye_values': {
                            Any(): Or(int,str),
                        },   
                    },
                },
                'reg_dump':{
                    'quad_reg':{
                        Any(): Or(int,str),
                    },
                    'p_reg':{
                        Any(): Or(int,str),
                    },
                    's_reg':{
                        Any(): Or(int,str),
                    },
                    'rxdtop':{
                        Any(): Or(int,str),
                    },
                    'txdtop':{
                        Any(): Or(int,str),
                    },
                    'autoneg':{
                        Any(): Or(int,str),
                    },
                    'linktraining':{
                        Any(): Or(int,str),
                    },
                    'rx_sts':{
                        Any():Or(int,str),
                    },
                    'an_debug_1':{
                        Any(): Or(int,str),
                    },
                    'an_debug_2':{
                        Any(): Or(int,str),
                    },
                    'lt_debug_1':{
                        Any(): Or(int,str),
                    },
                    'lt_debug_2':{
                        Any(): Or(int,str),
                    },
                },    
            },
        },
        'mac_port_link_down': {
            Any():{
                Any(): Or(int,str),
                'rx_deskew_fifo_overflow_count': {
                    Any(): Or(int,str),
                },
                'rx_pma_sig_ok_loss_interrupt_register_count': {
                    Any(): Or(int,str),
                },  
            },        
        },
        'mac_port_link_error': { 
            Any(): {
                Any(): Or(int,str),  
            },
        },
        'mac_port_link_debounce': {
            Any(): {
                Any(): Or(int,str), 
            },    
        }, 
        'port': int,
        Optional('slot'): int,
        'cmd': str,
        'rc': str,
        Optional('rsn'): str, 
        Optional('reason'): str,               
    }
         
    

class ShowControllerEthernetControllerInterfaceMac(ShowControllerEthernetControllerInterfaceMacSchema):
    """
    ShowControllerEthernetControllerInterfaceMac
    """
    
    cli_command = 'show controllers ethernet-controller {interface} mac'        

    def cli(self, interface, output=None): 

        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))         

        ret_dict = {} 
        
        #npu_pdsf_procagent_get_eye_common : asic inst 0 port 14 link 32 command 8
        p1 = re.compile(r'^npu_pdsf_procagent_get_eye_common\s*\: +(?P<npu_pdsf_procagent_get_eye_common>[\S\s]+.*)$')
        
        
        #"mpp_port_0_0_36:7": {
        p2  =  re.compile(r'^\"(?P<key>mpp_port_\d+_\d+_\d+\:\d+)\"\:\s*\{$')        
       
        #"mac_state_histogram": {
        p2_1  =  re.compile(r'^\"mac_state_histogram\"\:\s*\{$')        
       
        #"mac_port_status": { 
        p2_2 = re.compile(r'^\"mac_port_status\"\:\s*\{$')
        
        #"mib_counters": {
        p2_3 = re.compile(r'^\"mib_counters\"\:\s*\{$')
        
        #"tx_mac_tc_fc_frames_ok": [ 
        p2_3_1 = re.compile(r'^\"tx_mac_tc_fc_frames_ok\"\:\s*\[$')
        
        #"tx_xoff_state_duration": [
        p2_3_2 = re.compile(r'^\"tx_xoff_state_duration\"\:\s*\[$')
        
        #"rx_mac_tc_fc_frames_ok": [
        p2_3_3 = re.compile(r'^\"rx_mac_tc_fc_frames_ok\"\:\s*\[$')
        
        #"rx_xoff_state_duration": [
        p2_3_4 = re.compile(r'^\"rx_xoff_state_duration\"\:\s*\[$')
        
        #"multiport_phy_0_0_36": { 
        p3 = re.compile(r'^\"(?P<key>multiport_phy_\d+_\d+_\d+)\"\: +\{$')
        
        #"device_info": {
        p3_1 = re.compile(r'^\"device_info\"\:\s*\{$')
        
        # "serdes_0": { 
        p3_1_1 = re.compile(r'^\"serdes_\d+\"\:\s*\{$')        
        
        #"mac_port_config": {
        p3_2 =  re.compile(r'^\"mac_port_config\"\:\s*\{$')
        
        #"serdes_info_36": { 
        p3_2_1 = re.compile(r'^\"serdes_info_\d+\"\:\s*\{$')        
       
        #am_lock": [ 
        p3_3_1 = re.compile(r'^\"am_lock\"\:\s*\[$')        
       
        #"mac_pcs_lane_mapping": [ 
        p3_3_2 =  re.compile(r'^\"mac_pcs_lane_mapping\"\:\s*\[$') 
        
        #"mac_port_soft_state": {
        p3_4  = re.compile(r'^\"mac_port_soft_state\"\:\s*\{$')
        
        #"test_mode": {
        p3_5 = re.compile(r'^\"test_mode\"\:\s*\{$')        
        
        #"state_transition_history": [ 
        p3_6 = re.compile(r'^\"state_transition_history\"\:\s*\[$')
        
        #"serdes_parameters": {
        p3_7 = re.compile(r'^\"serdes_parameters\"\:\s*\{$')
        
        #"index_0": {
        p3_7_1 = re.compile(r'^\"index_0\"\:\s*\{$')
        
        #"serdes_config": {
        p3_8 = re.compile(r'^\"serdes_config\"\:\s*\{$')
        
        #"serdes_settings": [ 
        p3_8_1 = re.compile(r'^\"serdes_settings\"\:\s*\[$')
        
        #"rx_settings": { 
        p3_8_1_1 = re.compile(r'^\"rx_settings\"\:\s*\{$')
        
        #"targ_shadow": [ 
        p3_8_1_1_1 =  re.compile(r'^\"targ_shadow\"\:\s*\[$')
        
        #"tx_settings": {
        p3_8_1_2  =  re.compile(r'^\"tx_settings\"\:\s*\{$')
        
        #"tx_fir": [
        p3_8_1_2_1 = re.compile(r'^\"tx_fir\"\:\s*\[$')
        
        #"flow_chart_settings": { 
        p3_8_1_3 =  re.compile(r'^\"flow_chart_settings\"\:\s*\{$')
        
        #"serdes_status": {
        p3_9 = re.compile(r'^\"serdes_status\"\:\s*\{$')
        
        #"Firmware_Version": { 
        p3_9_1 =  re.compile(r'^\"Firmware_Version\"\:\s*\{$')
        
        #"rx_status": [
        p3_9_2 = re.compile(r'^\"rx_status\"\:\s*\[$')
        
        #"firs": [
        p3_9_2_1 = re.compile(r'^\"firs\":\s*\[$')
        
        #"fw_rx_status": [
        p3_9_3 = re.compile(r'^\"fw_rx_status\"\:\s*\[$')
        
        # "fir_shadow": [ 
        p3_9_4 =  re.compile(r'^\"fir_shadow\"\:\s*\[$')
        
        #"eye_capture": {
        p3_10 = re.compile (r'^\"eye_capture\"\:\s*\{$')
        
        #"veye_data": [
        p3_10_1 = re.compile(r'^\"veye_data\"\:\s*\[$')
        
        #"veye_values": [
        p3_10_1_1 = re.compile(r'^\"veye_values\"\:\s*\[$')
        
        #"reg_dump": {
        p3_11 = re.compile(r'^\"reg_dump\"\:\s*\{$')
        
        #"Quad_Reg": [
        p3_11_1 = re.compile(r'^\"Quad_Reg\"\:\s*\[$')        

        #"P_Reg": [ 
        p3_11_2 = re.compile(r'^\"P_Reg\"\:\s*\[$')
        
        #"S_reg": [
        p3_11_3 = re.compile(r'^\"S_reg\"\:\s*\[$')
        
        #"RXDTOP": [
        p3_11_4 = re.compile(r'^\"RXDTOP\"\:\s*\[$')
        
        #"TXDTOP": [
        p3_11_5 = re.compile(r'^\"TXDTOP\"\:\s*\[$')
        
        #"AutoNeg": [
        p3_11_6 = re.compile(r'^\"AutoNeg\"\:\s*\[$')
        
        #"LinkTraining": [
        p3_11_7 = re.compile(r'^\"LinkTraining\"\:\s*\[$')
        
        #"RX_STS": [
        p3_11_8 = re.compile(r'^\"RX_STS\"\:\s*\[$')
        
        #"an_debug_1": [
        p3_11_9 = re.compile(r'^\"an_debug_1\"\:\s*\[$')
        
        #""an_debug_2": [
        p3_11_10 = re.compile(r'^\"an_debug_2\"\:\s*\[$')
        
        #"lt_debug_1": [
        p3_11_11 = re.compile(r'^\"lt_debug_1\"\:\s*\[$')
        
        #"lt_debug_2": [
        p3_11_12 = re.compile(r'^\"lt_debug_2\"\:\s*\[$')
        
        #"mac_port_0_0_36.link_down_histogram": {
        p4= re.compile(r'^\"(?P<key>mac_port_\d+_\d+_\d+\.link_down_histogram)\"\:\s*\{$')        
        
        #"rx_deskew_fifo_overflow_count": [
        p4_1 = re.compile(r'^\"rx_deskew_fifo_overflow_count\"\:\s*\[$')
        
        #"rx_pma_sig_ok_loss_interrupt_register_count": [ 
        p4_2 = re.compile(r'^\"rx_pma_sig_ok_loss_interrupt_register_count\"\:\s*\[$')
        
        #"mac_port_0_0_36.link_error_histogram": {
        p5 =  re.compile(r'^\"(?P<key>mac_port_\d+_\d+_\d+\.link_error_histogram)\"\:\s*\{$')
        
        #"mac_port_0_0_36.link_debounce_state": {
        p6 = re.compile(r'^\"(?P<key>mac_port_\d+_\d+_\d+.link_debounce_state)\"\:\s*\{$')
        
        # Port = 40 Slot = 1 cmd = () rc = 0x16 reason = (null)
        p7 = re.compile(r'^Port +\= +(?P<port>\d+) +Slot +\= +(?P<slot>\d+) +cmd +\= +(?P<cmd>\([\s*\S]*\)) +rc +\= +(?P<rc>\w+) +reason(?P<reason>.*)$')
        
        # Port = 39 cmd = (prbs_stop unit 0 port 39 slot 1 serdes_level 1 polynomial 31) rc = 0x0 rsn = success
        p7_1 = re.compile(r'^Port +\= +(?P<port>\d+) +cmd +\= +(?P<cmd>\([\s*\S]*\)) +rc +\= +(?P<rc>\w+) +rsn +\= +(?P<rsn>.*)$')
               
        
        # "PRE_INIT": 0,
        p8 = re.compile(r'^\"(?P<key>\w+)\"\:\s*(?P<value>.*)$')        
        
        #false 
        p8_1 = re.compile(r'^(?P<value>\w+)$')
        
        #0
        p8_2 =  re.compile(r'^(?P<value>[-]?\d+)$')
        
        #64,
        p8_3 = re.compile(r'^(?P<value>[-]?\d+)\,$')
        
        #], 
        p8_4 =  re.compile(r'^\]\,$')
        
         #], 
        p8_5 =  re.compile(r'^\]$')
        
        cnt = index_flag = stat_cnt = 0
        
        for line in output.splitlines():
            line = line.strip() 
            
            #npu_pdsf_procagent_get_eye_common : asic inst 0 port 14 link 32 command 8
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['npu_pdsf_procagent_get_eye_common'] =  group['npu_pdsf_procagent_get_eye_common']
                continue
                
            #"mpp_port_0_0_36:7": {    
            m = p2.match(line)
            if m:
                group = m.groupdict()
                port  =  group['key']
                curr_dict = ret_dict.setdefault('mpp_port_detai1', {}).setdefault(group['key'], {})
                continue
                
            #"mac_state_histogram": {
            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                if  ret_dict.get('multiport_detail'):
                    curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mac_state_histogram', {})
                else:    
                    curr_dict =  ret_dict.setdefault('mpp_port_detai1', {}).setdefault(port, {}).setdefault('mac_state_histogram', {})                
                continue
                
            #"mac_port_status": { 
            m = p2_2.match(line)
            if m:
                group = m.groupdict()
                if  ret_dict.get('multiport_detail'):
                    curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mac_port_status', {})
                else:    
                    curr_dict =  ret_dict.setdefault('mpp_port_detai1', {}).setdefault(port, {}).setdefault('mac_port_status', {})                
                continue
            
            #"mib_counters": {
            m = p2_3.match(line)
            if m:
                group = m.groupdict()
                if  ret_dict.get('multiport_detail'):
                    curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mib_counters', {})
                else:    
                    curr_dict = ret_dict.setdefault('mpp_port_detai1', {}).setdefault(port, {}).setdefault('mib_counters', {})                
                continue
            
            #"tx_mac_tc_fc_frames_ok": [     
            m = p2_3_1.match(line)
            if m:
                index_flag  =  1
                group = m.groupdict()
                handle_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mib_counters', {})
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mib_counters', {}).setdefault('tx_mac_tc_fc_frames_ok', {})
                continue   

            #"tx_xoff_state_duration": [
            m = p2_3_2.match(line)
            if m:
                index_flag  =  1
                group = m.groupdict()
                handle_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mib_counters', {})
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mib_counters', {}).setdefault('tx_xoff_state_duration', {})
                continue 
                
            #"rx_mac_tc_fc_frames_ok": [
            m = p2_3_3.match(line)
            if m:
                index_flag  =  1
                group = m.groupdict()
                handle_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mib_counters', {})
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mib_counters', {}).setdefault('rx_mac_tc_fc_frames_ok', {})
                continue     
                
            #"rx_xoff_state_duration": [    
            m = p2_3_4.match(line)
            if m:
                index_flag  =  1
                group = m.groupdict()
                handle_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mib_counters', {})
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mib_counters', {}).setdefault('rx_xoff_state_duration', {})
                continue
            
            #"multiport_phy_0_0_36": { 
            m = p3.match(line)
            if m:
                group = m.groupdict()
                port  =  group['key']
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {})
                continue
                
            #"device_info": {
            m = p3_1.match(line)
            if  m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('device_info', {})
                continue
                
            # "serdes_0": { 
            m = p3_1_1.match(line)
            if m:
                group = m.groupdict()
                curr_dict = curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mac_state_histogram', {}).setdefault('serdes_0', {})
                continue
                
            #"mac_port_config": {
            m = p3_2.match(line)
            if m:
                group = m.groupdict()
                if  ret_dict.get('multiport_detail'):                    
                    curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mac_port_config', {})
                else:
                    curr_dict = ret_dict.setdefault('mpp_port_detai1', {}).setdefault(port, {}).setdefault('mac_port_config', {})
                continue
                
            #"serdes_info_36": {
            m = p3_2_1.match(line)
            if  m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mac_port_config', {}).setdefault('serdes_info', {})
                continue
                
            #am_lock": [
            m = p3_3_1.match(line)
            if m:
                index_flag  =  1
                group = m.groupdict()
                handle_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mac_port_status', {})
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mac_port_status', {}).setdefault('am_lock', {})
                continue
                
            #"mac_pcs_lane_mapping": [
            m = p3_3_2.match(line)
            if m:
                index_flag = 1
                group = m.groupdict()
                handle_dict  = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mac_port_status', {})
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mac_port_status', {}).setdefault('mac_pcs_lane_mapping', {})
                continue
                
            #"mac_port_soft_state": {
            m = p3_4.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('mac_port_soft_state', {})
                continue
                
            #"test_mode": {
            m = p3_5.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('test_mode', {})
                continue
                
            #"state_transition_history": [
            m = p3_6.match(line)
            if m:
                group = m.groupdict()   
                index_flag = 1
                if  ret_dict.get('multiport_detail'):                    
                    curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('state_transition_history', {})
                else:
                    curr_dict = ret_dict.setdefault('mpp_port_detai1', {}).setdefault(port, {}).setdefault('state_transition_history', {})
                handle_dict  =  curr_dict 
                continue
                
            #"serdes_parameters": {
            m = p3_7.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_parameters', {})
                continue
                
            #"index_0": {
            m = p3_7_1.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_parameters', {}).setdefault('index_0', {})
                continue
            
            #"serdes_config": {
            m = p3_8.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_config', {})
                continue
                
            #"serdes_settings": [
            m = p3_8_1.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_config', {}).setdefault('serdes_settings', {})                
                continue
                
            #"rx_settings": { 
            m = p3_8_1_1.match(line)
            if  m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_config', {}).setdefault('serdes_settings', {}).setdefault('rx_settings', {})                
                continue
                
            #"targ_shadow": [
            m = p3_8_1_1_1.match(line)    
            if  m:
                group = m.groupdict()
                index_flag = 1
                handle_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_config', {}).setdefault('serdes_settings', {}).setdefault('rx_settings', {})
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_config', {}).setdefault('serdes_settings', {}).setdefault('rx_settings', {}).setdefault('targ_shadow', {})
                continue    
                
            #"tx_settings": {
            m = p3_8_1_2.match(line)
            if  m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_config', {}).setdefault('serdes_settings', {}).setdefault('tx_settings', {})                
                continue
                
            #"tx_fir": [
            m = p3_8_1_2_1.match(line)
            if  m:
                group = m.groupdict()
                index_flag = 1
                handle_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_config', {}).setdefault('serdes_settings', {}).setdefault('tx_settings', {})
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_config', {}).setdefault('serdes_settings', {}).setdefault('tx_settings', {}).setdefault('tx_fir', {})                
                continue
                
            #"flow_chart_settings": {
            m = p3_8_1_3.match(line)
            if  m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_config', {}).setdefault('serdes_settings', {}).setdefault('flow_chart_settings', {}) 
                continue
                
            #"serdes_status": {
            m = p3_9.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_status', {})
                continue
            
            #"Firmware_Version": { 
            m = p3_9_1.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_status', {}).setdefault('firmware_version', {})                
                continue
                
            #"rx_status": [
            m = p3_9_2.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_status', {}).setdefault('rx_status', {})                
                continue
                
            #"firs": [
            m = p3_9_2_1.match(line)
            if m:
                group = m.groupdict()
                index_flag = 1
                handle_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_status', {}).setdefault('rx_status', {})
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_status', {}).setdefault('rx_status', {}).setdefault('firs',{})                
                continue
               
            #"fw_rx_status": [
            m = p3_9_3.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_status', {}).setdefault('fw_rx_status', {})                
                continue   
            
            # "fir_shadow": [ 
            m = p3_9_4.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('serdes_status', {}).setdefault('fir_shadow', {})                
                continue  
            
            #"eye_capture": {
            m = p3_10.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('eye_capture', {})                
                continue  
            
            #"veye_data": [
            m = p3_10_1.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('eye_capture', {}).setdefault('veye_data',{})                
                continue  
            
            #"veye_values": [
            m = p3_10_1_1.match(line)
            if m:
                group = m.groupdict()
                index_flag = 1
                handle_dict  = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('eye_capture', {}).setdefault('veye_data',{})
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('eye_capture', {}).setdefault('veye_data',{}).setdefault('veye_values', {})                
                continue  
                
            #"reg_dump": {
            m = p3_11.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {})                
                continue  
             
            #"Quad_Reg": [
            m = p3_11_1.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('quad_reg',{})                
                continue
            
            #"P_Reg": [ 
            m = p3_11_2.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('p_reg',{})                
                continue
            
            #"S_reg": [
            m = p3_11_3.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('s_reg',{})                
                continue 

            #"RXDTOP": [
            m = p3_11_4.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('rxdtop',{})                
                continue
            
            #"TXDTOP": [
            m = p3_11_5.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('txdtop',{})                
                continue
            
            #"AutoNeg": [
            m = p3_11_6.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('autoneg',{})                
                continue
                
            #"LinkTraining": [
            m = p3_11_7.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('linktraining',{})                
                continue

            #"RX_STS": [
            m = p3_11_8.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('rx_sts',{})                
                continue
                
            #"an_debug_1": [
            m = p3_11_9.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('an_debug_1',{})                
                continue
                
            #""an_debug_2": [
            m = p3_11_10.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('an_debug_2',{})                
                continue
                
            #"lt_debug_1": [
            m = p3_11_11.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('lt_debug_1',{})                
                continue
                
            #"lt_debug_2": [
            m = p3_11_12.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('multiport_detail', {}).setdefault(port, {}).setdefault('reg_dump', {}).setdefault('lt_debug_2',{})                
                continue
                
            #"mac_port_0_0_36.link_down_histogram": {   
            m = p4.match(line)
            if  m:
                group = m.groupdict()
                port = group['key']
                curr_dict = ret_dict.setdefault('mac_port_link_down', {}).setdefault(group['key'], {})                
                continue 
                
            #"rx_deskew_fifo_overflow_count": [
            m = p4_1.match(line)
            if  m:
                group = m.groupdict()
                index_flag = 1
                handle_dict = ret_dict.setdefault('mac_port_link_down', {}).setdefault(port, {})
                curr_dict = ret_dict.setdefault('mac_port_link_down', {}).setdefault(port, {}).setdefault('rx_deskew_fifo_overflow_count',{})               
                continue 
                
            #"rx_pma_sig_ok_loss_interrupt_register_count": [ 
            m = p4_2.match(line)
            if  m:
                group = m.groupdict()
                index_flag = 1
                handle_dict = ret_dict.setdefault('mac_port_link_down', {}).setdefault(port, {})
                curr_dict = ret_dict.setdefault('mac_port_link_down', {}).setdefault(port, {}).setdefault('rx_pma_sig_ok_loss_interrupt_register_count',{})               
                continue 
            
            #"mac_port_0_0_36.link_error_histogram": {
            m = p5.match(line)
            if  m:
                group = m.groupdict()
                port = group['key']
                curr_dict = ret_dict.setdefault('mac_port_link_error', {}).setdefault(group['key'], {})                
                continue  
                
            #"mac_port_0_0_36.link_debounce_state": {
            m = p6.match(line)
            if  m:
                group = m.groupdict()
                port = group['key']
                curr_dict = ret_dict.setdefault('mac_port_link_debounce', {}).setdefault(group['key'], {})                
                continue

            # Port = 40 Slot = 1 cmd = () rc = 0x16 reason = (null)
            m = p7.match(line)
            if  m:
                group = m.groupdict()
                ret_dict['port'] = int(group['port'])
                ret_dict['slot'] = int(group['slot'])                
                ret_dict['cmd'] = group['cmd']
                ret_dict['rc'] = group['rc']
                ret_dict['reason'] = group['reason']
                continue
            
            # Port = 39 cmd = (prbs_stop unit 0 port 39 slot 1 serdes_level 1 polynomial 31) rc = 0x0 rsn = success
            m = p7_1.match(line)
            if  m:
                group = m.groupdict()
                ret_dict['port'] = int(group['port'])                
                ret_dict['cmd'] = group['cmd']
                ret_dict['rc'] = group['rc']
                ret_dict['rsn'] = group['rsn']
                continue
            
            # "PRE_INIT": 0,
            m = p8.match(line)            
            if m:
                group = m.groupdict()
                if  group['value'] == '{' or  group['value'] == '[':
                    continue
                elif group['key'] == 'new_state':
                    stat_cnt = stat_cnt + 1
                    curr_dict = curr_dict.setdefault(stat_cnt,{})                    
                    curr_dict.update({'state': group['value']})
                    continue
                elif group['key'] == 'timestamp':
                    curr_dict.update({'timestamp': group['value']})
                    curr_dict = handle_dict
                    continue
                else:
                    group['key'] = group['key'].lower()
                    group['value'] = group['value'].strip(',').strip('"')
                    try:
                        group['value'] = int(group['value'])
                    except:
                        #If it is a word, do not convert it to int.
                        pass     
                    curr_dict.update({group['key']: group['value']})
                    continue
                    
            #false 
            m = p8_1.match(line)            
            if  m:
                group = m.groupdict()
                cnt  = cnt + 1
                key = cnt
                curr_dict.update({key: group['value']})
                continue
            
            #64,   
            m = p8_3.match(line)
            if m:
                group = m.groupdict()
                cnt  = cnt + 1
                key  = cnt 
                curr_dict.update({key: group['value']})
                continue
                
            #], 
            m = p8_4.match(line)                             
            if  m:                
                if  index_flag == 1:
                    curr_dict  = handle_dict
                    index_flag = 0   
                    cnt = 0
                continue
                
            #], 
            m = p8_5.match(line)                             
            if  m:                
                if  index_flag == 1:
                    curr_dict  = handle_dict
                    index_flag = 0   
                    cnt = 0
                    stat_cnt  =0
                continue    
          
        return ret_dict               
                  
        

