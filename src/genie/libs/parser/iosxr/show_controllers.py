''' show_controllers.py

IOSXR parsers for the following show commands:

    * show controller fia diagshell {diagshell_unit} 'l2 show' location {location}
    * show controllers coherentDSP {port}
    * show controllers optics {port}
    * show controllers fia diagshell {diagshell_unit} "diag cosq qpair egq map" location {location}
'''

# Python
import re
from genie.libs.parser.utils.common import Common

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ==========================================================================================
# Schema for 'show controller fia diagshell {diagshell_unit} 'l2 show' location {location}'
# ==========================================================================================
class ShowControllersFiaDiagshellL2showLocationSchema(MetaParser):
    '''Schema for:
        * show controller fia diagshell {diagshell_unit} 'l2 show' location {location}
    '''

    schema = {
        'nodes':
            {Any():
                {'vlan':
                    {Any():
                        {'mac': 
                            {Any():
                                {'encap_id': str,
                                'gport': str,
                                Optional('trunk'): int,
                                Optional('static'): bool
                                },
                            },
                        },
                    },
                },
            },
        }


# ==========================================================================================
# Parser for 'show controller fia diagshell {diagshell_unit} 'l2 show' location {location}'
# ==========================================================================================
class ShowControllersFiaDiagshellL2showLocation(ShowControllersFiaDiagshellL2showLocationSchema):
    '''Parser for:
        * show controller fia diagshell {diagshell_unit} 'l2 show' location {location}
    '''

    cli_command = "show controller fia diagshell {diagshell_unit} 'l2 show' location {location}"


    def cli(self, diagshell_unit=0, location='all', output=None):

        # Execute command
        if output is None:
            out = self.device.execute(self.cli_command.format(location=location,
                                        diagshell_unit=diagshell_unit))
        else:
            out = output

        # Init
        parsed_dict = {}

        # Node ID: 0/0/CPU0
        p1 = re.compile(r'^Node +ID: +(?P<node_id>(\S+))$')

        # mac=fc:00:00:ff:01:9c vlan=2544 GPORT=0x8000048 encap_id=0x2007
        # mac=fc:00:00:ff:01:03 vlan=2522 GPORT=0x9800401d Static encap_id=0xffffffff
        # mac=fc:00:00:ff:01:9c vlan=2544 GPORT=0x8000048 Trunk=0 encap_id=0x2007
        # mac=fc:00:00:ff:01:0c vlan=2524 GPORT=0xc000000 Trunk=0 Static encap_id=0x3001'
        p2 = re.compile(r'^mac\=(?P<mac>[A-Fa-f0-9:]+) +vlan=(?P<vlan>\d+)'
                         ' +GPORT\=(?P<gport>\d+|0x[A-Fa-f0-9]+)'
                         '(?: +Trunk\=(?P<trunk>\d+))?'
                         '(?: +(?P<b_static>(Static)))?'
                         ' +encap_id\=(?P<encap_id>\d+|0x[A-Fa-f0-9\']+)$')

        for line in out.splitlines():
            line = line.strip()

            # Node ID: 0/0/CPU0
            m = p1.match(line)
            if m:
                nodes_dict = parsed_dict.setdefault('nodes', {}).\
                                         setdefault(m.groupdict()['node_id'], {})
                continue

            # mac=fc:00:00:ff:01:9c vlan=2544 GPORT=0x8000048 encap_id=0x2007
            # mac=fc:00:00:ff:01:03 vlan=2522 GPORT=0x9800401d Static encap_id=0xffffffff
            # mac=fc:00:00:ff:01:9c vlan=2544 GPORT=0x8000048 Trunk=0 encap_id=0x2007
            # mac=fc:00:00:ff:01:0c vlan=2524 GPORT=0xc000000 Trunk=0 Static encap_id=0x3001'
            m = p2.match(line)
            if m:
                group = m.groupdict()
                mac_dict = nodes_dict.setdefault('vlan', {}).\
                                      setdefault(int(group['vlan']), {}).\
                                      setdefault('mac', {}).\
                                      setdefault(group['mac'], {})
                mac_dict['gport'] = group['gport']
                if group['b_static']:
                    mac_dict['static'] = bool(group['b_static'])
                if group['trunk']:
                    mac_dict['trunk'] = int(group['trunk'])
                mac_dict['encap_id'] = group['encap_id']
                continue

        return parsed_dict


# ================================================
# Schema for 'show controllers coherentDSP {port}'
# ================================================
class ShowControllersCoherentDSPSchema(MetaParser):
    '''Schema for:
        * show controllers coherentDSP {port}
    '''

    schema = {
        Any(): {
            'port': str,
            'controller_state': str,
            'inherited_secondary_state': str,
            'configured_secondary_state': str,
            'derived_state': str,
            'loopback_mode': str,
            'ber_thresholds_sf': str,
            'ber_thresholds_sd': str,
            'performance_monitoring': str,
            'alarm_info': {
                'los': int,
                'lof': int,
                'lom': int,
                'oof': int,
                'oom': int,
                'ais': int,
                'iae': int,
                'biae': int,
                'sf_ber': int,
                'sd_ber': int,
                'bdi': int,
                'tim': int,
                'fecmis_match': int,
                'fec_unc': int,
            },
            'detected_alarms': str,
            'bit_error_rate_info': {
                'prefec_ber': str,
                'postfec_ber': str,
            },
            'otu_tti': str,
            'fec_mode': str,
        },
    }


# ================================================
# Parser for 'show controllers coherentDSP {port}'
# ================================================
class ShowControllersCoherentDSP(ShowControllersCoherentDSPSchema):
    '''Parser for:
        * show controllers coherentDSP {port}
    '''

    cli_command = 'show controllers coherentDSP {port}'
    exclude = []

    def cli(self, port, output=None):

        if output is None:
            out = self.device.execute(self.cli_command.format(port=port))
        else:
            out = output

        result_dict = {}

        # Port   : CoherentDSP 0/0/1/2
        p1 = re.compile(r'^Port +: +(?P<port>[\s\S]+)$')

        # Controller State    : Up
        p2 = re.compile(r'^Controller +State +: +(?P<controller_state>\w+)$')

        # Inherited Secondary State   : Normal
        p3 = re.compile(r'^Inherited +Secondary +State +: +(?P<inherited_secondary_state>\w+)$')

        # Configured Secondary State   : Normal
        p4 = re.compile(r'^Configured +Secondary +State +: +(?P<configured_secondary_state>\w+)$')

        # Derived State      : In Service
        p5 = re.compile(r'^Derived +State +: +(?P<derived_state>[\w\s]+)$')

        # Loopback mode      : None
        p6 = re.compile(r'^Loopback +mode +: +(?P<loopback_mode>\w+)$')

        # BER Thresholds     : SF = 1.0E-5  SD = 1.0E-7
        p7 = re.compile(r'^BER +Thresholds +: SF += +(?P<sf>\S+) +SD += +(?P<sd>\S+)$')

        # Performance Monitoring    : Enable
        p8 = re.compile(r'^Performance +Monitoring +: +(?P<performance_monitoring>\w+)$')

        # Alarm Information:
        # LOS = 1 LOF = 0 LOM = 0
        p9 = re.compile(r'^LOS += +(?P<los>\d+) +LOF += +(?P<lof>\d+) +LOM += +(?P<lom>\d+)$')

        # OOF = 0 OOM = 0 AIS = 0
        p10 = re.compile(r'^OOF += +(?P<oof>\d+) +OOM += +(?P<oom>\d+) +AIS += +(?P<ais>\d+)$')

        # IAE = 0 BIAE = 0    SF_BER = 0
        p11 = re.compile(r'^IAE += +(?P<iae>\d+) +BIAE += +(?P<biae>\d+) +SF_BER += +(?P<sf_ber>\d+)$')

        # SD_BER = 0     BDI = 2 TIM = 0
        p12 = re.compile(r'^SD_BER += +(?P<sd_ber>\d+) +BDI += +(?P<bdi>\d+) +TIM += +(?P<tim>\d+)$')

        # FECMISMATCH = 0  FEC-UNC = 0
        p13 = re.compile(r'^FECMISMATCH += +(?P<fecmis_match>\d+) +FEC-UNC += +(?P<fec_unc>\d+)$')

        # Detected Alarms    : None
        p14 = re.compile(r'^Detected +Alarms +: +(?P<detected_alarms>\w+)$')

        # Bit Error Rate Information
        # PREFEC  BER        : 0.0E+00
        p15 = re.compile(r'^PREFEC +BER +: +(?P<prefec_ber>\S+)$')

        # POSTFEC BER        : 0.0E+00
        p16 = re.compile(r'^POSTFEC +BER +: +(?P<postfec_ber>\S+)$')

        # OTU TTI Received
        p17 = re.compile(r'^OTU +TTI +(?P<otu_tti>\w+)$')

        # FEC mode           : STANDARD
        p18 = re.compile(r'^FEC +mode +: +(?P<fec_mode>\w+)$')

        for line in out.splitlines():
            line = line.replace('\t', ' ').strip()
            if not line:
                continue

            # Port   : CoherentDSP 0/0/1/2
            m = p1.match(line)
            if m:
                port_num = m.groupdict()['port']
                port_dict = result_dict.setdefault(port, {})
                port_dict.update({'port': port_num})
                continue

            # Controller State    : Up
            m = p2.match(line)
            if m: 
                state = m.groupdict()['controller_state']
                port_dict.update({'controller_state': state})
                continue

            # Inherited Secondary State   : Normal
            m = p3.match(line)
            if m:
                state = m.groupdict()['inherited_secondary_state']
                port_dict.update({'inherited_secondary_state': state})
                continue

            # Configured Secondary State   : Normal
            m = p4.match(line)
            if m:
                state = m.groupdict()['configured_secondary_state']
                port_dict.update({'configured_secondary_state': state})
                continue

            # Derived State      : In Service
            m = p5.match(line)
            if m:
                state = m.groupdict()['derived_state']
                port_dict.update({'derived_state': state})
                continue

            # Loopback mode      : None
            m = p6.match(line)
            if m:
                loopback_mode = m.groupdict()['loopback_mode']
                port_dict.update({'loopback_mode': loopback_mode})
                continue

            # BER Thresholds     : SF = 1.0E-5  SD = 1.0E-7
            m = p7.match(line)
            if m:
                sf = m.groupdict()['sf']
                sd = m.groupdict()['sd']
                port_dict.update({'ber_thresholds_sf': sf})
                port_dict.update({'ber_thresholds_sd': sd})
                continue

            # Performance Monitoring    : Enable
            m = p8.match(line)
            if m:
                performance_monitoring = m.groupdict()['performance_monitoring']
                port_dict.update({'performance_monitoring': performance_monitoring})
                continue

            # Alarm Information:
            # LOS = 1 LOF = 0 LOM = 0
            m = p9.match(line)
            if m:
                group = m.groupdict() 
                alarm_dict = port_dict.setdefault('alarm_info', {})
                alarm_dict.update({k: int(v) for k, v in group.items()})
                continue

            # OOF = 0 OOM = 0 AIS = 0
            m = p10.match(line)
            if m:
                group = m.groupdict() 
                alarm_dict = port_dict.setdefault('alarm_info', {})
                alarm_dict.update({k: int(v) for k, v in group.items()})
                continue

            # IAE = 0 BIAE = 0    SF_BER = 0
            m = p11.match(line)
            if m:
                group = m.groupdict() 
                alarm_dict = port_dict.setdefault('alarm_info', {})
                alarm_dict.update({k: int(v) for k, v in group.items()})
                continue

            # SD_BER = 0     BDI = 2 TIM = 0
            m = p12.match(line)
            if m:
                group = m.groupdict() 
                alarm_dict = port_dict.setdefault('alarm_info', {})
                alarm_dict.update({k: int(v) for k, v in group.items()})
                continue

            # FECMISMATCH = 0  FEC-UNC = 0
            m = p13.match(line)
            if m:
                group = m.groupdict() 
                alarm_dict = port_dict.setdefault('alarm_info', {})
                alarm_dict.update({k: int(v) for k, v in group.items()})
                continue

            # Detected Alarms    : None
            m = p14.match(line)
            if m:
                detected_alarms = m.groupdict()['detected_alarms']
                port_dict.update({'detected_alarms': detected_alarms})
                continue

            # PREFEC  BER        : 0.0E+00
            m = p15.match(line)
            if m:
                prefec_ber = m.groupdict()['prefec_ber']
                bit_info_dict = port_dict.setdefault('bit_error_rate_info', {})
                bit_info_dict.update({'prefec_ber': prefec_ber})
                continue

            # POSTFEC BER        : 0.0E+00
            m = p16.match(line)
            if m:
                postfec_ber = m.groupdict()['postfec_ber']
                bit_info_dict = port_dict.setdefault('bit_error_rate_info', {})
                bit_info_dict.update({'postfec_ber': postfec_ber})
                continue

            # OTU TTI Received
            m = p17.match(line)
            if m:
                otu_tti = m.groupdict()['otu_tti']
                port_dict.update({'otu_tti': otu_tti})
                continue

            # FEC mode           : STANDARD
            m = p18.match(line)
            if m:
                fec_mode = m.groupdict()['fec_mode']
                port_dict.update({'fec_mode': fec_mode})
                continue

        return result_dict


# ===========================================
# Schema for 'show controllers optics {port}'
# ===========================================
class ShowControllersOpticsSchema(MetaParser):
    '''Schema for:
        * show controllers optics {port}
    '''

    schema = {
        Any(): {
            'name': str,
            'controller_state': str,
            'transport_admin_state': str,
            'laser_state': str,
            Optional('led_state'): str,
            Optional('fec_state'): str,
            'optics_status': {
                'optics_type': str,
                'wavelength': str,
                Optional('dwdm_carrier_info'): str,
                Optional('msa_itu_channel'): str,
                Optional('frequency'): str,
                Optional('alarm_status'): {
                    Optional('detected_alarms'): list,
                },
                Optional('alarm_statistics'): {
                    Optional('high_rx_pwr'): int,
                    Optional('low_rx_pwr'): int,
                    Optional('high_tx_pwr'): int,
                    Optional('low_tx_pwr'): int,
                    Optional('high_lbc'): int,
                    Optional('high_dgd'): int,
                    Optional('oor_cd'): int,
                    Optional('osnr'): int,
                    Optional('wvl_ool'): int,
                    Optional('mea'): int,
                    Optional('improper_rem'): int,
                    Optional('tc_power_prov_mismatch'): int,
                },
                Optional('los_lol_fault_status'): {
                    Optional('detected_los_lol_fault'): list,
                },
                Optional('laser_bias_current'): str,
                Optional('actual_tx_power'): str,
                Optional('rx_power'): str,
                Optional('performance_monitoring'): str,
                Optional('threshold_values'): {
                    Any() :{
                        'parameter': str,
                        'high_alarm': str,
                        'low_alarm': str,
                        'high_warning': str,
                        'low_warning': str,
                    },
                },
                Optional('lane'): {
                    Any() :{
                        'laser_bias': str,
                        'tx_power': str,
                        'rx_power': str,
                        'output_frequency': str,
                    },
                },
                Optional('lbc_high_threshold'): str,
                Optional('configured_tx_power'): str,
                Optional('configured_osnr_lower_threshold'): str,
                Optional('configured_dgd_higher_threshold'): str,
                Optional('chromatic_dispersion'): str,
                Optional('configured_cd_min'): str,
                Optional('configured_cd_max'): str,
                Optional('optical_snr'): str,
                Optional('polarization_dependent_loss'): str,
                Optional('polarization_parameters'): str,
                Optional('differential_group_delay'): str,
                Optional('temperature'): str,
                Optional('voltage'): str,
            },
            Optional('transceiver_vendor_details'): {
                Optional('form_factor'): str,
                Optional('optics_type'): str,
                Optional('name'): str,
                Optional('oui_number'): str,
                Optional('part_number'): str,
                Optional('rev_number'): str,
                Optional('serial_number'): str,
                Optional('pid'): str,
                Optional('vid'): str,
                Optional('date_code'): str,
            },
        },
    }


# ===========================================
# Parser for 'show controllers optics {port}'
# ===========================================
class ShowControllersOptics(ShowControllersOpticsSchema):
    '''Parser for:
        * show controllers optics {port}
    '''

    cli_command = 'show controllers optics {port}'
    exclude = ['laser_bias_current', 'actual_tx_power', 'rx_power', 'chromatic_dispersion']

    def cli(self, port, output=None):

        if output is None:
            out = self.device.execute(self.cli_command.format(port=port))
        else:
            out = output

        result_dict = {}

        # Controller State:  Up
        p1 = re.compile(r'^Controller +State: +(?P<controller_state>\w+)$')

        # Transport Admin State: In Service
        p2 = re.compile(r'^Transport +Admin +State: +(?P<transport_admin_state>[\w\s]+)$')

        # Laser State: On
        # Laser State: N/A 
        p3 = re.compile(r'^Laser +State: +(?P<laser_state>.+)$')

        # LED State: Green
        # LED State: Not Applicable
        p4 = re.compile(r'^LED +State: +(?P<led_state>.+)$')

        # FEC State: FEC DISABLED 
        p4_1 = re.compile(r'^FEC +State: +(?P<fec_state>.+)$')

        # Optics Type:  CFP2 DWDM
        p5 = re.compile(r'^Optics +Type: +(?P<optics_type>[\S\s]+)$')

        # DWDM carrier Info: C BAND, MSA ITU Channel=97, Frequency=191.30THz,
        # DWDM Carrier Info: Unavailable, MSA ITU Channel= Unavailable, Frequency= Unavailable , Wavelength= Unavailable
        p6 = re.compile(r'^DWDM +[Cc]arrier +Info: +(?P<dwdm_carrier_info>[\w\s]+), '
                         '+MSA +ITU +Channel *= *(?P<msa_itu_channel>[\w]+), '
                         '+Frequency *= *(?P<frequency>[\w\.]+) *,'
                         '( +Wavelength *= *(?P<wavelength>[\S\s]+))?$')

        # Wavelength=1567.133nm
        p7 = re.compile(r'^Wavelength *= *(?P<wavelength>[\S\s]+)$')

        # Detected Alarms: None
        p8 = re.compile(r'^Detected +Alarms: +(?P<detected_alarms>\w+)$')

        # Detected Alarms:
        #          LOW-RX1-PWR
        p9 = re.compile(r'^(?!-)(?P<alarm>[\w-]+)$')

        # LOS/LOL/Fault Status:
        p10 = re.compile(r'^LOS\/LOL\/Fault +Status:$')

        # Detected LOS/LOL/FAULT: RX-LOS
        p10_1 = re.compile(r'^Detected +LOS\/LOL\/FAULT: +(?P<detected_los_lol_fault>\S+)$')

        # HIGH-RX-PWR = 0            LOW-RX-PWR = 1
        p11 = re.compile(r'^HIGH-RX-PWR *= *(?P<high_rx_pwr>\d+) +LOW-RX-PWR *= *(?P<low_rx_pwr>\d+)$')

        # HIGH-TX-PWR = 0            LOW-TX-PWR = 1
        p12 = re.compile(r'^HIGH-TX-PWR *= *(?P<high_tx_pwr>\d+) +LOW-TX-PWR *= *(?P<low_tx_pwr>\d+)$')

        # HIGH-LBC = 0               HIGH-DGD = 0
        p13 = re.compile(r'^HIGH-LBC *= *(?P<high_lbc>\d+) +HIGH-DGD *= *(?P<high_dgd>\d+)$')

        # OOR-CD = 0                 OSNR = 0
        p14 = re.compile(r'^OOR-CD *= *(?P<oor_cd>\d+) +OSNR *= *(?P<osnr>\d+)$')

        # WVL-OOL = 0                MEA  = 0
        p15 = re.compile(r'^WVL-OOL *= *(?P<wvl_ool>\d+) +MEA *= *(?P<mea>\d+)$')

        # IMPROPER-REM = 0
        p16 = re.compile(r'^IMPROPER-REM *= *(?P<improper_rem>\d+)$')

        # TX-POWER-PROV-MISMATCH = 0
        p17 = re.compile(r'^TX-POWER-PROV-MISMATCH *= *(?P<tc_power_prov_mismatch>\d+)$')

        # Laser Bias Current = 0.0 mA
        p18 = re.compile(r'^Laser +Bias +Current *= *(?P<laser_bias_current>[\s\S]+)$')

        # Actual TX Power = -17.25 dBm
        # TX Power = Unavailable
        p19 = re.compile(r'^(Actual *)?TX +Power *= *(?P<actual_tx_power>[\s\S]+)$')

        # RX Power = -40.00 dBm
        p20 = re.compile(r'^RX +Power *= *(?P<rx_power>[\s\S]+)$')

        # Performance Monitoring: Enable
        p21 = re.compile(r'^Performance +Monitoring: +(?P<performance_monitoring>\w+)$')

        # Parameter                 High Alarm  Low Alarm  High Warning  Low Warning
        # ------------------------  ----------  ---------  ------------  -----------
        # Rx Power Threshold(dBm)          2.0      -13.9          -1.0         -9.9
        p22 = re.compile(r'^(?P<parameter>[\w\s(.]+\)) +(?P<high_alarm>[\w\/.-]+) '
                         r'+(?P<low_alarm>[\w\/.-]+) +(?P<high_warning>[\w\/.-]+) '
                         r'+(?P<low_warning>[\w\/.-]+)$')

        # Lane Laser Bias TX Power   RX Power    Output Frequency
        # ---- ---------- ---------- ----------  ----------------
        # 0    38.9 mA    1.42 dBm   -2.04 dBm   N/A
        p22_2 = re.compile(r'^(?P<lane>\d+) +(?P<laser_bias>[\w.-]+ +\w+) '
                           r'+(?P<tx_power>[\w.-]+ +\w+) +(?P<rx_power>[\w.-]+ +\w+) '
                           r'+(?P<output_frequency>[\S\s]+)$')

        # Temperature = 35.00 Celsius 
        p23 = re.compile(r'^Temperature *= *(?P<temperature>[\s\S]+)$')

        # Voltage = 3.26 V 
        p24 = re.compile(r'^Voltage *= *(?P<voltage>[\s\S]+)$')

        # LBC High Threshold = 98 %
        p25 = re.compile(r'^LBC +High +Threshold *= *(?P<lbc_high_threshold>[\s\S]+)$')

        # Configured Tx Power = 1.00 dBm
        p26 = re.compile(r'^Configured +Tx +Power *= *(?P<configured_tx_power>[\s\S]+)$')

        # Configured OSNR lower Threshold = 0.00 dB
        p27 = re.compile(r'^Configured +OSNR +lower +Threshold *= *(?P<configured_osnr_lower_threshold>[\s\S]+)$')

        # Configured DGD Higher Threshold = 180.00 ps
        p28 = re.compile(r'^Configured +DGD +Higher +Threshold *= *(?P<configured_dgd_higher_threshold>[\s\S]+)$')

        # Chromatic Dispersion 5 ps/nm
        p29 = re.compile(r'^Chromatic +Dispersion +(?P<chromatic_dispersion>[\s\S]+)$')

        # Configured CD-MIN -10000 ps/nm  CD-MAX 16000 ps/nm
        p30 = re.compile(r'^Configured CD-MIN +(?P<configured_cd_min>[\s\S]+) +CD-MAX +(?P<configured_cd_max>[\s\S]+)$')

        # Optical Signal to Noise Ratio = 27.00 dB
        p31 = re.compile(r'^Optical +Signal +to +Noise +Ratio *= *(?P<optical_snr>[\s\S]+)$')

        # Polarization Dependent Loss = 0.00 dB
        p32 = re.compile(r'^Polarization +Dependent +Loss *= *(?P<polarization_dependent_loss>[\s\S]+)$')

        # Polarization parameters not supported by optics
        p32_1 = re.compile(r'^Polarization +parameters +(?P<polarization_parameters>[\s\S]+)$')

        # Differential Group Delay = 2.00 ps
        p33 = re.compile(r'^Differential +Group +Delay *= *(?P<differential_group_delay>[\s\S]+)$')

        # Form Factor            : SFP+
        p34 = re.compile(r'^Form +Factor +: +(?P<form_factor>[\S\s]+)$')

        # Optics type            : SFP+ 10G SR
        p35 = re.compile(r'^Optics +type +: +(?P<optics_type>[\S\s]+)$')

        # Name                   : CISCO-AVAGO
        p36 = re.compile(r'^Name +: +(?P<name>\S+)$')

        # OUI Number             : 00.17.6a
        p37 = re.compile(r'^OUI +Number +: +(?P<oui_number>\S+)$')

        # Part Number            : SFBR-7702SDZ-CS5
        p38 = re.compile(r'^Part +Number +: +(?P<part_number>\S+)$')

        # Rev Number             : G2.5
        p39 = re.compile(r'^Rev +Number +: +(?P<rev_number>\S+)$')

        # Serial Number          : AGD162040SP
        # Serial Number          : N/A
        p40 = re.compile(r'^Serial +Number +: +(?P<serial_number>.+)$')

        # PID                    : SFP-10G-SR
        p41 = re.compile(r'^PID +: +(?P<pid>\S+)$')

        # VID                    : V03
        p42 = re.compile(r'^VID +: +(?P<vid>\S+)$')

        # Date Code(yy/mm/dd)    : 12/05/20
        p43 = re.compile(r'^Date +Code.*: +(?P<date_code>\S+)$')

        for line in out.splitlines():
            line = line.replace('\t', ' ').strip()
            if not line:
                continue

            # Controller State:  Up
            m = p1.match(line)
            if m:
                name = 'Optics {}'.format(port)
                optics_dict = result_dict.setdefault(port, {})
                optics_dict.update({'name': name})
                
                group = m.groupdict()
                optics_dict.update({k: v for k, v in group.items()})
                continue

            # Transport Admin State: In Service
            m = p2.match(line)
            if m: 
                group = m.groupdict()
                optics_dict.update({k: v for k, v in group.items()})
                continue

            # Laser State: On
            # Laser State: N/A 
            m = p3.match(line)
            if m:
                group = m.groupdict()
                optics_dict.update({k: v for k, v in group.items()})
                continue

            # LED State: Green
            # LED State: Not Applicable 
            m = p4.match(line)
            if m:
                group = m.groupdict()
                optics_dict.update({k: v for k, v in group.items()})
                continue

            # FEC State: FEC DISABLED  
            m = p4_1.match(line)
            if m:
                group = m.groupdict()
                optics_dict.update({k: v for k, v in group.items()})
                continue

            # Optics Status
            # Optics Type:  CFP2 DWDM
            m = p5.match(line)
            if m:
                group = m.groupdict()
                status_dict = optics_dict.setdefault('optics_status', {})
                status_dict.update({k: v for k, v in group.items()})
                continue

            # DWDM carrier Info: C BAND, MSA ITU Channel=97, Frequency=191.30THz,
            m = p6.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({k: v for k, v in group.items()})
                continue

            # Wavelength=1567.133nm
            m = p7.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({k: v for k, v in group.items()})
                continue

            # Detected Alarms: None
            m = p8.match(line)
            if m:
                alarm = m.groupdict()['detected_alarms']
                alarm_status = status_dict.setdefault('alarm_status', {})
                alarms = alarm_status.setdefault('detected_alarms', [])
                if alarm.lower() != 'none':
                    alarms.append(alarm)
                continue

            # Detected Alarms:
            #          LOW-RX1-PWR
            m = p9.match(line)
            if m:
                alarm = m.groupdict()['alarm']
                alarm_status = status_dict.setdefault('alarm_status', {})
                alarms = alarm_status.setdefault('detected_alarms', [])
                alarms.append(alarm)
                continue

            # LOS/LOL/Fault Status:
            m = p10.match(line)
            if m:
                fault_dict = status_dict.setdefault('los_lol_fault_status', {})
                continue

            # Detected LOS/LOL/FAULT: RX-LOS
            m = p10_1.match(line)
            if m:
                fault = m.groupdict()['detected_los_lol_fault']
                faults = fault_dict.setdefault('detected_los_lol_fault', [])
                faults.append(fault)
                continue

            # HIGH-RX-PWR = 0            LOW-RX-PWR = 1
            m = p11.match(line)
            if m:
                group = m.groupdict()
                alarm_statistics = status_dict.setdefault('alarm_statistics', {})
                alarm_statistics.update({k: int(v) for k, v in group.items()})
                continue

            # HIGH-TX-PWR = 0            LOW-TX-PWR = 1
            m = p12.match(line)
            if m:
                group = m.groupdict()
                alarm_statistics = status_dict.setdefault('alarm_statistics', {})
                alarm_statistics.update({k: int(v) for k, v in group.items()})
                continue

            # HIGH-LBC = 0               HIGH-DGD = 0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                alarm_statistics = status_dict.setdefault('alarm_statistics', {})
                alarm_statistics.update({k: int(v) for k, v in group.items()})
                continue

            # OOR-CD = 0                 OSNR = 0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                alarm_statistics = status_dict.setdefault('alarm_statistics', {})
                alarm_statistics.update({k: int(v) for k, v in group.items()})
                continue

            # WVL-OOL = 0                MEA  = 0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                alarm_statistics = status_dict.setdefault('alarm_statistics', {})
                alarm_statistics.update({k: int(v) for k, v in group.items()})
                continue

            # IMPROPER-REM = 0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                alarm_statistics = status_dict.setdefault('alarm_statistics', {})
                alarm_statistics.update({k: int(v) for k, v in group.items()})
                continue

            # TX-POWER-PROV-MISMATCH = 0
            m = p17.match(line)
            if m:
                group = m.groupdict()
                alarm_statistics = status_dict.setdefault('alarm_statistics', {})
                alarm_statistics.update({k: int(v) for k, v in group.items()})
                continue

            # Laser Bias Current = 0.0 mA
            m = p18.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({k: v for k, v in group.items()})
                continue

            # Actual TX Power = -17.25 dBm
            # TX Power = Unavailable
            m = p19.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({k: v for k, v in group.items()})
                continue

            # RX Power = -40.00 dBm
            m = p20.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({k: v for k, v in group.items()})
                continue

            # Performance Monitoring: Enable
            m = p21.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({k: v for k, v in group.items()})
                continue

            # Parameter                 High Alarm  Low Alarm  High Warning  Low Warning
            # ------------------------  ----------  ---------  ------------  -----------
            # Rx Power Threshold(dBm)          2.0      -13.9          -1.0         -9.9
            m = p22.match(line)
            if m:
                group = m.groupdict()
                parameter = group['parameter']
                para_dict = status_dict.setdefault('threshold_values', {}).setdefault(parameter, {})
                para_dict.update({k: v for k, v in group.items()})
                continue

            # Lane Laser Bias TX Power   RX Power    Output Frequency
            # ---- ---------- ---------- ----------  ----------------
            # 0    38.9 mA    1.42 dBm   -2.04 dBm   N/A
            m = p22_2.match(line)
            if m:
                group = m.groupdict()
                lane = group.pop('lane')
                lane_dict = status_dict.setdefault('lane', {}).setdefault(lane, {})
                lane_dict.update({k: v for k, v in group.items()})
                continue

            # Temperature = 35.00 Celsius 
            m = p23.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({k: v for k, v in group.items()})
                continue

            # Voltage = 3.26 V 
            m = p24.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({k: v for k, v in group.items()})
                continue

            # LBC High Threshold = 98 %
            m = p25.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({k: v for k, v in group.items()})
                continue

            # Configured Tx Power = 1.00 dBm
            m = p26.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({k: v for k, v in group.items()})
                continue

            # Configured OSNR lower Threshold = 0.00 dB
            m = p27.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({k: v for k, v in group.items()})
                continue

            # Configured DGD Higher Threshold = 180.00 ps
            m = p28.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({k: v for k, v in group.items()})
                continue

            # Chromatic Dispersion 5 ps/nm
            m = p29.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({k: v for k, v in group.items()})
                continue

            # Configured CD-MIN -10000 ps/nm  CD-MAX 16000 ps/nm
            m = p30.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({k: v for k, v in group.items()})
                continue

            # Optical Signal to Noise Ratio = 27.00 dB
            m = p31.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({k: v for k, v in group.items()})
                continue

            # Polarization Dependent Loss = 0.00 dB
            m = p32.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({k: v for k, v in group.items()})
                continue

            # Polarization parameters not supported by optics
            m = p32_1.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({k: v for k, v in group.items()})
                continue

            # Differential Group Delay = 2.00 ps
            m = p33.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({k: v for k, v in group.items()})
                continue

            # Form Factor            : SFP+  
            m = p34.match(line)
            if m:
                group = m.groupdict()
                vendor_dict = optics_dict.setdefault('transceiver_vendor_details', {})
                vendor_dict.update({k: v for k, v in group.items()})
                continue

            # Optics type            : SFP+ 10G SR
            m = p35.match(line)
            if m:
                group = m.groupdict()
                vendor_dict.update({k: v for k, v in group.items()})
                continue

            # Name                   : CISCO-AVAGO
            m = p36.match(line)
            if m:
                group = m.groupdict()
                vendor_dict.update({k: v for k, v in group.items()})
                continue

            # OUI Number             : 00.17.6a
            m = p37.match(line)
            if m:
                group = m.groupdict()
                vendor_dict.update({k: v for k, v in group.items()})
                continue

            # Part Number            : SFBR-7702SDZ-CS5
            m = p38.match(line)
            if m:
                group = m.groupdict()
                vendor_dict.update({k: v for k, v in group.items()})
                continue

            # Rev Number             : G2.5
            m = p39.match(line)
            if m:
                group = m.groupdict()
                vendor_dict.update({k: v for k, v in group.items()})
                continue

            # Serial Number          : AGD162040SP
            # Serial Number          : N/A
            m = p40.match(line)
            if m:
                group = m.groupdict()
                vendor_dict.update({k: v for k, v in group.items()})
                continue

            # PID                    : SFP-10G-SR
            m = p41.match(line)
            if m:
                group = m.groupdict()
                vendor_dict.update({k: v for k, v in group.items()})
                continue

            # VID                    : V03
            m = p42.match(line)
            if m:
                group = m.groupdict()
                vendor_dict.update({k: v for k, v in group.items()})
                continue

            # Date Code(yy/mm/dd)    : 12/05/20
            m = p43.match(line)
            if m:
                group = m.groupdict()
                vendor_dict.update({k: v for k, v in group.items()})
                continue

        return result_dict

# ===============================================================================
# Schema for 'show controllers fia diagshell 0 "diag egr_calendars" location all'
# ===============================================================================
class ShowControllersFiaDiagshellDiagEgrCalendarsLocationSchema(MetaParser):
    schema = {
        'node_id': {
            Any(): {
                'port': {
                    Any(): {
                        'priority': str,
                        'high_calendar': int,
                        'low_calendar': int,
                        'egq_if': int,
                        'e2e_if': int,
                        'egq_port_rate': int,
                        'egq_if_rate': int,
                        'e2e_port_rate': int,
                        'e2e_if_rate': int,
                    }
                }
            }
        }
    }

# ===============================================================================
# Parser for 'show controllers fia diagshell 0 "diag egr_calendars" location all'
# ===============================================================================
class ShowControllersFiaDiagshellDiagEgrCalendarsLocation(ShowControllersFiaDiagshellDiagEgrCalendarsLocationSchema):

    cli_command = 'show controllers fia diagshell {diagshell} "diag egr_calendars" location {location}'

    def cli(self, diagshell, location, output=None):
        if not output:
            cmd = self.cli_command.format(diagshell=diagshell,
                    location=location)
            out = self.device.execute(cmd)
        else:
            out = output
        
        ret_dict = {}

        # Node ID: 0/0/CPU0
        p1 = re.compile(r'^Node +ID: +(?P<node_id>\S+)$')

        # 0  |    LOW   |       255     |        4     |   28   |    4   |      336671   |     990000  |      350000   |    1050000
        p2 = re.compile(r'^(?P<port>\d+) +\| +(?P<priority>\S+) +\| +'
                r'(?P<high_calendar>\d+) +\| +(?P<low_calendar>\d+) +\| +'
                r'(?P<egq_if>\d+) +\| +(?P<e2e_if>\d+) +\| +(?P<egq_port_rate>\d+) +\| +'
                r'(?P<egq_if_rate>\d+) +\| +(?P<e2e_port_rate>\d+) +\| +'
                r'(?P<e2e_if_rate>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Node ID: 0/0/CPU0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                node_id = group['node_id']
                node_id_dict = ret_dict.setdefault('node_id', {}). \
                    setdefault(node_id, {})
                continue
            
            # 0  |    LOW   |       255     |        4     |   28   |    4   |      336671   |     990000  |      350000   |    1050000
            m = p2.match(line)
            if m:
                group = m.groupdict()
                priority = group['priority']
                port_dict = node_id_dict.setdefault('port', {}). \
                    setdefault(int(group['port']), {})
                port_dict.update({'priority': group['priority']})
                port_dict.update({'high_calendar': int(group['high_calendar'])})
                port_dict.update({'low_calendar': int(group['low_calendar'])})
                port_dict.update({'egq_if': int(group['egq_if'])})
                port_dict.update({'e2e_if': int(group['e2e_if'])})
                port_dict.update({'egq_port_rate': int(group['egq_port_rate'])})
                port_dict.update({'egq_if_rate': int(group['egq_if_rate'])})
                port_dict.update({'e2e_port_rate': int(group['e2e_port_rate'])})
                port_dict.update({'e2e_if_rate': int(group['e2e_if_rate'])})
                continue

        return ret_dict

# =====================================================================================================
# Schema for 'show controllers npu {npu} interface {interface} instance {instance} location {location}'
# =====================================================================================================
class ShowControllersNpuInterfaceInstanceLocationSchema(MetaParser):
    schema = {
        'node_id': {
            Any(): {
                'interface': {
                    Any(): {
                        'interface_handle_hex': str,
                        'npu_number': int,
                        'npu_core': int,
                        'pp_port': int,
                        'sys_port': int,
                        'voq_base': int,
                        'flow_base': int,
                        'voq_port_type': str,
                        'port_speed': str,
                    }
                }
            }
        }
    }


# =====================================================================================================
# Parser for 'show controllers npu {npu} interface {interface} instance {instance} location {location}'
# =====================================================================================================
class ShowControllersNpuInterfaceInstanceLocation(ShowControllersNpuInterfaceInstanceLocationSchema):
    cli_command = 'show controllers npu {npu} interface {interface} instance {instance} location {location}'

    def cli(self, npu, interface, instance, location, output=None):

        ret_dict = {}

        if not output:
            cmd = self.cli_command.format(npu=npu,
                interface=interface,
                instance=instance,
                location=location
            )
            out = self.device.execute(cmd)
        else:
            out = output

        # Node ID: 0/0/CPU0
        p1 = re.compile(r'^Node +ID: +(?P<node_id>\S+)$')
        # Gi0/0/0/0    108       0   0   33    33   1024   5384 local     1G
        p2 = re.compile(r'^(?P<interface>\S+) +(?P<interface_handle_hex>[0-9a-f]+) +'
                r'(?P<npu_number>\d+) +(?P<npu_core>\d+) +(?P<pp_port>\d+) +'
                r'(?P<sys_port>\d+) +(?P<voq_base>\d+) +(?P<flow_base>\d+) +'
                r'(?P<voq_port_type>\S+) +(?P<port_speed>\S+)$')
        
        for line in out.splitlines():
            line = line.strip()

            # Node ID: 0/0/CPU0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                node_id_dict = ret_dict.setdefault('node_id', {}). \
                    setdefault(group['node_id'], {})
                continue
            
            # Gi0/0/0/0    108       0   0   33    33   1024   5384 local     1G
            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                interface = Common.convert_intf_name(interface)
                interface_handle_hex = group['interface_handle_hex']
                npu_number = int(group['npu_number'])
                npu_core = int(group['npu_core'])
                pp_port = int(group['pp_port'])
                sys_port = int(group['sys_port'])
                voq_base = int(group['voq_base'])
                flow_base = int(group['flow_base'])
                voq_port_type = group['voq_port_type']
                port_speed = group['port_speed']
                interface_dict = node_id_dict.setdefault('interface', {}). \
                    setdefault(interface, {})
                interface_dict.update({'interface_handle_hex': interface_handle_hex})
                interface_dict.update({'npu_number': npu_number})
                interface_dict.update({'npu_core': npu_core})
                interface_dict.update({'pp_port': pp_port})
                interface_dict.update({'sys_port': sys_port})
                interface_dict.update({'voq_base': voq_base})
                interface_dict.update({'flow_base': flow_base})
                interface_dict.update({'voq_port_type': voq_port_type})
                interface_dict.update({'port_speed': port_speed})
                continue
        return ret_dict

# =====================================================================================
# Schema for 'show controllers fia diagshell 0 "diag cosq qpair egq map" location all'
# =====================================================================================
class ShowControllersFiaDiagshellDiagCosqQpairEgpMapSchema(MetaParser):
    schema = {
        'node_id': {
            Any(): {
                'mapping': {
                    Any(): {
                        'port_number': {
                            Any(): {
                                'priorities': int,
                                'base_q_pair': int,
                                'ps_number': int,
                                'core': int,
                                'tm_port': int,
                            }
                        }
                    }
                }
            }
        }
    }

# =====================================================================================
# Parser for 'show controllers fia diagshell 0 "diag cosq qpair egq map" location all'
# =====================================================================================
class ShowControllersFiaDiagshellDiagCosqQpairEgpMap(ShowControllersFiaDiagshellDiagCosqQpairEgpMapSchema):
    cli_command = 'show controllers fia diagshell {unit} "diag cosq qpair egq map" location {location}'
    def cli(self, unit=0, location='all', output=None):
        
        if not output:
            cmd = self.cli_command.format(unit=unit,
                        location=location)
            out = self.device.execute(cmd)
        else:
            out = output
        
        ret_dict = {}

        # Node ID: 0/0/CPU0
        p1 = re.compile(r'^Node +ID: +(?P<node_id>\S+)$')

        # EGQ MAPPING:
        p2 = re.compile(r'^(?P<mapping>[\S ]+):$')

        # Port #  |  Priorities  |  Base Q-Pair  |   PS #  | Core | TM Port |
        # ---------|--------------|---------------|---------|------|---------|
        # 0    |       2      |      200      |    25   |   0  |     0   |
        p3 = re.compile(r'^(?P<port_number>\d+) +\| +(?P<priorities>\d+) +\| +'
                        r'(?P<base_q_pair>\d+) +\| +(?P<ps_number>\d+) +\| +'
                        r'(?P<core>\d+) +\| +(?P<tm_port>\d+) +\|$')
        
        for line in out.splitlines():
            line = line.strip()

            # Node ID: 0/0/CPU0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                node_id = group['node_id']
                node_id_dict = ret_dict.setdefault('node_id', {}). \
                    setdefault(node_id, {})
                continue
            
            # EGQ MAPPING:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                mapping_dict = node_id_dict.setdefault('mapping', {}). \
                    setdefault(group['mapping'], {})
                continue
            
            # Port #  |  Priorities  |  Base Q-Pair  |   PS #  | Core | TM Port |
            # ---------|--------------|---------------|---------|------|---------|
            # 0    |       2      |      200      |    25   |   0  |     0   |
            m = p3.match(line)
            if m:
                group =  m.groupdict()
                port_dict = mapping_dict.setdefault('port_number', {}). \
                    setdefault(int(group['port_number']), {})
                port_dict.update({'priorities': int(group['priorities'])})
                port_dict.update({'base_q_pair': int(group['base_q_pair'])})
                port_dict.update({'ps_number': int(group['ps_number'])})
                port_dict.update({'core': int(group['core'])})
                port_dict.update({'tm_port': int(group['tm_port'])})
                continue

        return ret_dict
        
# vim: ft=python ts=8 sw=4 et
