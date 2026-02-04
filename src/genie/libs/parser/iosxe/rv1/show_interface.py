"""
    show_interface.py
    IOSXE revision 1 parsers for the following show commands:
    *show interface transceiver details
    *show interface transceiver         
"""

import logging
import re
import json

from genie.metaparser import MetaParser
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or
# import parser utils
from genie.libs.parser.utils.common import Common

logger = logging.getLogger(__name__)

class ShowInterfacesTransceiverDetailSchema(MetaParser):
    """Schema for:
        show interfaces {interface} transceiver detail"""

    schema = {
        'interfaces': {
            Any(): {
                Optional('transceiver'): str,
                Optional('type'): str,
                Optional('name'): str,
                Optional('part_number'): str,

                'Temperature': Or(
                    {
                        'Value': Or(float, str),
                        Optional('Lane'): str,
                        'HighAlarmThreshold': Or(float, str),
                        'HighWarnThreshold': Or(float, str),
                        'LowWarnThreshold': Or(float, str),
                        'LowAlarmThreshold': Or(float, str)
                    },
                    {
                        Any(): {
                            'Value': Or(float, str),
                            Optional('Lane'): str,
                            'HighAlarmThreshold': Or(float, str),
                            'HighWarnThreshold': Or(float, str),
                            'LowWarnThreshold': Or(float, str),
                            'LowAlarmThreshold': Or(float, str)
                        }
                    }
                ),

                'Voltage': Or(
                    {
                        'Value': Or(float, str),
                        Optional('Lane'): str,
                        'HighAlarmThreshold': Or(float, str),
                        'HighWarnThreshold': Or(float, str),
                        'LowWarnThreshold': Or(float, str),
                        'LowAlarmThreshold': Or(float, str)
                    },
                    {
                        Any(): {
                            'Value': Or(float, str),
                            Optional('Lane'): str,
                            'HighAlarmThreshold': Or(float, str),
                            'HighWarnThreshold': Or(float, str),
                            'LowWarnThreshold': Or(float, str),
                            'LowAlarmThreshold': Or(float, str)
                        }
                    }
                ),

                'Current': Or(
                    {
                        'Value': Or(float, str),
                        Optional('Lane'): str,
                        'HighAlarmThreshold': Or(float, str),
                        'HighWarnThreshold': Or(float, str),
                        'LowWarnThreshold': Or(float, str),
                        'LowAlarmThreshold': Or(float, str)
                    },
                    {
                        Any(): {
                            'Value': Or(float, str),
                            Optional('Lane'): str,
                            'HighAlarmThreshold': Or(float, str),
                            'HighWarnThreshold': Or(float, str),
                            'LowWarnThreshold': Or(float, str),
                            'LowAlarmThreshold': Or(float, str)
                        }
                    }
                ),

                'OpticalTX': Or(
                    {
                        'Value': Or(float, str),
                        Optional('Lane'): str,
                        'HighAlarmThreshold': Or(float, str),
                        'HighWarnThreshold': Or(float, str),
                        'LowWarnThreshold': Or(float, str),
                        'LowAlarmThreshold': Or(float, str)
                    },
                    {
                        Any(): {
                            'Value': Or(float, str),
                            Optional('Lane'): str,
                            'HighAlarmThreshold': Or(float, str),
                            'HighWarnThreshold': Or(float, str),
                            'LowWarnThreshold': Or(float, str),
                            'LowAlarmThreshold': Or(float, str)
                        }
                    }
                ),

                'OpticalRX': Or(
                    {
                        'Value': Or(float, str),
                        Optional('Lane'): str,
                        'HighAlarmThreshold': Or(float, str),
                        'HighWarnThreshold': Or(float, str),
                        'LowWarnThreshold': Or(float, str),
                        'LowAlarmThreshold': Or(float, str)
                    },
                    {
                        Any(): {
                            'Value': Or(float, str),
                            Optional('Lane'): str,
                            'HighAlarmThreshold': Or(float, str),
                            'HighWarnThreshold': Or(float, str),
                            'LowWarnThreshold': Or(float, str),
                            'LowAlarmThreshold': Or(float, str)
                        }
                    }
                ),
            }
        }
    }

class ShowInterfacesTransceiverDetail(ShowInterfacesTransceiverDetailSchema):
    """parser for
            * show interfaces transceiver detail
            * show interfaces {interface} transceiver detail
        """

    cli_command = ['show interfaces {interface} transceiver detail',
                   'show interfaces transceiver detail']

    def cli(self, interface=None, output=None):
        if output is None:
            if interface:
                out = self.device.execute(self.cli_command[0].format(interface=interface))
            else:
                out = self.device.execute(self.cli_command[1])
        else:
            out = output

        # transceiver is present
        # type is 10Gbase-LR
        # name is CISCO-FINISAR
        # part number is FTLX1474D3BCL-CS
        p1 = re.compile(r'^(?P<key>[Tt]ransceiver|[Tt]ype|[Nn]ame|[Pp]art +[Nn]umber) +is +(?P<value>[\S\s]+)$')

        # Voltage            Threshold   Threshold  Threshold  Threshold
        p3_0 = re.compile(r'(?P<statistic>(Temperature|Voltage|Current|Transmit Power|Receive Power)) +Threshold +Threshold +Threshold +Threshold$')

        # Twe2/1/1     25.5                   90.0       85.0       -5.0      -10.0
        # Twe2/1/1   N/A    5.7                 50.0       40.0        2.0        1.0
        # Twe2/1/1   N/A    N/A                 50.0       40.0        2.0        1.0
        p3_1 = re.compile(
            r'^(?P<port>\S+)\s+'
            r'(?:(?P<lane>\S+)\s+)?'
            r'(?P<value>\S+)\s+'
            r'(?P<HAT>-?[\d\.NAna/]+)\s+'
            r'(?P<HWT>-?[\d\.NAna/]+)\s+'
            r'(?P<LWT>-?[\d\.NAna/]+)\s+'
            r'(?P<LAT>-?[\d\.NAna/]+)$'
        )

        result_dict = {}
        is_dict = {}
        stat = None

        for line in out.splitlines():
            line = line.strip()

            # transceiver is present
            # type is 10Gbase-LR
            # name is CISCO-FINISAR
            # part number is FTLX1474D3BCL-CS
            m = p1.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].lower().replace(' ', '_')
                value = group['value'].strip()
                is_dict[key] = value
                continue

            # Voltage            Threshold   Threshold  Threshold  Threshold
            m = p3_0.match(line)
            if m:
                stat = m.group('statistic')
                if stat == 'Transmit Power':
                    stat = 'OpticalTX'
                elif stat == 'Receive Power':
                    stat = 'OpticalRX'
                continue

            # Twe2/1/1     25.5                   90.0       85.0       -5.0      -10.0
            # Twe2/1/1   N/A    5.7                 50.0       40.0        2.0        1.0
            # Twe2/1/1   N/A    N/A                 50.0       40.0        2.0        1.0
            if stat:
                m = p3_1.match(line)
                if m:
                    groups = m.groupdict()
                    intf = Common.convert_intf_name(groups['port'])
                    intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf, {})

                    intf_dict.update(is_dict)
                    is_dict = {}

                    stat_dict = intf_dict.setdefault(stat, {})

                    lane = groups.get('lane')
                    value_dict = {
                        'Value': groups['value'],
                        'HighAlarmThreshold': float(groups['HAT']),
                        'HighWarnThreshold': float(groups['HWT']),
                        'LowWarnThreshold': float(groups['LWT']),
                        'LowAlarmThreshold': float(groups['LAT']),
                    }

                    if lane and lane.isdigit():
                        stat_dict[lane] = value_dict
                    else:
                        stat_dict['Value'] = value_dict['Value']
                        stat_dict['HighAlarmThreshold'] = value_dict['HighAlarmThreshold']
                        stat_dict['HighWarnThreshold'] = value_dict['HighWarnThreshold']
                        stat_dict['LowWarnThreshold'] = value_dict['LowWarnThreshold']
                        stat_dict['LowAlarmThreshold'] = value_dict['LowAlarmThreshold']  
        return result_dict
    
class ShowInterfacesTransceiverSchema(MetaParser):
    """Schema for:
        * show interfaces {interface} transceiver
    """

    schema = {
        'interfaces': {
            Any(): {  # interface name
                Optional('port'): str,
                Optional('temp'): str,
                Optional('voltage'): str,
                Optional('current'): str,
                Optional('opticaltx'): str,
                Optional('opticalrx'): str,
                Optional('max_power'): str,

                 Optional('transceiver'): {
                    Optional('status'): str,
                    Optional('slot'): int,
                    Optional('subslot'): int,
                    Optional('port'): int,
                },

                Optional('details'): {
                    Optional('module_temperature'): float,
                    Optional('tx_voltage'): float,
                    Optional('tx_power'): float,
                    Optional('rx_power'): float,
                },

                Optional('lanes'): {
                    Any(): {
                        Optional('tx_power'): float,
                        Optional('rx_power'): float,
                        Optional('bias_current'): float,
                    }
                },

                Optional('idprom'): {
                    Optional('description'): str,
                    Optional('transceiver_type'): str,
                    Optional('pid'): str,
                    Optional('vendor_revision'): str,
                    Optional('serial_number'): str,
                    Optional('vendor_name'): str,
                    Optional('vendor_oui'): str,
                    Optional('clei_code'): str,
                    Optional('part_number'): str,
                    Optional('device_state'): str,
                    Optional('date_code'): str,
                    Optional('connector_type'): str,
                    Optional('encoding'): str,
                    Optional('nominal_bitrate'): str,
                },
            }
        }
    }


class ShowInterfacesTransceiver(ShowInterfacesTransceiverSchema):
    """
    parser for
        * show interfaces transceiver
        * show interfaces {interface} transceiver
    """

    cli_command = ['show interfaces {interface} transceiver', 'show interfaces transceiver']

    def cli(self, interface=None, output=None):
        if output is None:
            if interface:
                out = self.device.execute(self.cli_command[0].format(interface=interface))
            else:
                out = self.device.execute(self.cli_command[1])

        else:
            out = output

        # Gi1/1      40.6       5.09       0.4     -25.2      N/A
        # Gi1/1      40.6       5.09       0.4     -25.2      -31.00    Max
        p = re.compile(r'^(?P<port>([\d\/A-Za-z]+)) +(?P<temp>([\d\.-]+)) '
                        r'+(?P<voltage>([\d\.-]+)) +(?P<current>([\d\.-]+)) '
                        r'+(?P<opticaltx>(\S+)) +(?P<opticalrx>(\S+))(\s+(?P<max_power>.*))?$')

        # The Transceiver in slot 2 subslot 0 port 0 is enabled.
        p1 = re.compile(
            r'^The Transceiver in slot (?P<slot>\d+) subslot (?P<subslot>\d+) port (?P<port>\d+) is (?P<state>\w+)\.$')

        # Module temperature                        = +22.214 C [Range: +0.000 to +70.000 C]
        p2 = re.compile(
            r'^Module temperature\s+=\s+\+?(?P<module_temperature>[\d\.]+)\s+C')

        # Transceiver Tx supply voltage             = 3.2405 Volts [Range: 3.1350 to 3.4650 Volts]
        p3 = re.compile(
            r'^Transceiver Tx supply voltage\s+=\s+(?P<tx_voltage>[\d\.]+)\s+Volts')

        # Transceiver Tx power                      =  6.1 dBm
        p4 = re.compile(
            r'^Transceiver Tx power\s+=\s+(?P<tx_power>[\d\.]+)\s+dBm')

        # Transceiver Rx optical power              =  6.5 dBm
        p5 = re.compile(
            r'^Transceiver Rx optical power\s+=\s+(?P<rx_power>[\d\.]+)\s+dBm')

        # Tx power Network Lane[00]               =  0.2 dBm (1.456 mW)  [Range:-8.4 to  2.4 dBm]
        p6 = re.compile(
            r'^Tx power Network Lane\[(?P<lane>\d+)\]\s+=\s+(?P<lane_tx_power>[\d\.]+)\s+dBm')

        # Bias Current Network Lane[00]           = 7.494 mA   [Range: 3.0 to 8.500 mA]
        p7 = re.compile(
            r'^Bias Current Network Lane\[(?P<lane>\d+)\]\s+=\s+(?P<bias_current>[\d\.]+)\s+mA')

        # Description                               = QSFP28 optics (type 134)
        p8 = re.compile(
            r'^Description\s+=\s+(?P<description>.+)$')

        # Transceiver Type:                         = QSFP 100GE SR (411)
        p9 = re.compile(
            r'^Transceiver Type:\s+=\s+(?P<transceiver_type>.+)$')

        # Product Identifier (PID)                  = QSFP-100G-SR4-S
        p10 = re.compile(
            r'^Product Identifier \(PID\)\s+=\s+(?P<pid>\S+)')

        # Vendor Revision                           = 06
        p11 = re.compile(
            r'^Vendor Revision\s+=\s+(?P<vendor_revision>\S+)')

        # Serial Number (SN)                        = AVF2304S40E
        p12 = re.compile(
            r'^Serial Number \(SN\)\s+=\s+(?P<serial_number>\S+)')

        # Vendor Name                               = CISCO-AVAGO
        p13 = re.compile(
            r'^Vendor Name\s+=\s+(?P<vendor_name>.+)$')

        # Vendor OUI (IEEE company ID)              = 00.17.6A (5994)
        p14 = re.compile(
            r'^Vendor OUI \(IEEE company ID\)\s+=\s+(?P<vendor_oui>[\w\.]+)')

        # CLEI code                                 = CMUIATKCAA
        p15 = re.compile(
            r'^CLEI code\s+=\s+(?P<clei_code>\S+)')

        # Cisco part number                         = 10-3142-03
        p16 = re.compile(
            r'^Cisco part number\s+=\s+(?P<part_number>\S+)')

        # Device State                              = Enabled.
        p17 = re.compile(
            r'^Device State\s+=\s+(?P<device_state>\w+)')

        # Date code (yy/mm/dd)                      = 19/01/27
        p18 = re.compile(
            r'^Date code \(yy/mm/dd\)\s+=\s+(?P<date_code>[\d\/]+)')

        # Connector type                            = MPO
        p19 = re.compile(
            r'^Connector type\s+=\s+(?P<connector_type>\S+)')

        # Encoding                                  = 64B66B
        p20 = re.compile(
            r'^Encoding\s+=\s+(?P<encoding>\S+)')

        # Nominal bitrate per channel               = 25GE (25500 Mbits/s)
        p21 = re.compile(
            r'^Nominal bitrate per channel\s+=\s+(?P<nominal_bitrate>.+)$')

        result_dict = {}
        for line in out.splitlines():
            line = line.strip()

            m = p.match(line)
            if m:
                group = m.groupdict()
                intf_name = Common.convert_intf_name(group['port'])
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf_name, {})
                intf_dict['port'] = intf_name
                intf_dict['temp'] = group['temp']
                intf_dict['voltage'] = group['voltage']
                intf_dict['current'] = group['current']
                intf_dict['opticaltx'] = group['opticaltx']
                intf_dict['opticalrx'] = group['opticalrx']
                if group['max_power']:
                    intf_dict['max_power'] = group['max_power']
                continue

            m = p1.match(line)
            if m and interface:
                group = m.groupdict()
                intf_name = Common.convert_intf_name(interface)
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf_name, {})
                trans_dict = intf_dict.setdefault('transceiver', {})
                trans_dict['status'] = group['state']
                trans_dict['slot'] = int(group['slot'])
                trans_dict['subslot'] = int(group['subslot'])
                trans_dict['port'] = int(group['port'])
                continue

            m = p2.match(line)
            if m and interface:
                group = m.groupdict()
                intf_name = Common.convert_intf_name(interface)
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf_name, {})
                det_dict = intf_dict.setdefault('details', {})
                det_dict['module_temperature'] = float(group['module_temperature'])
                continue

            m = p3.match(line)
            if m and interface:
                group = m.groupdict()
                intf_name = Common.convert_intf_name(interface)
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf_name, {})
                det_dict = intf_dict.setdefault('details', {})
                det_dict['tx_voltage'] = float(group['tx_voltage'])
                continue

            m = p4.match(line)
            if m and interface:
                group = m.groupdict()
                intf_name = Common.convert_intf_name(interface)
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf_name, {})
                det_dict = intf_dict.setdefault('details', {})
                det_dict['tx_power'] = float(group['tx_power'])
                continue

            m = p5.match(line)
            if m and interface:
                group = m.groupdict()
                intf_name = Common.convert_intf_name(interface)
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf_name, {})
                det_dict = intf_dict.setdefault('details', {})
                det_dict['rx_power'] = float(group['rx_power'])
                continue

            m = p6.match(line)
            if m and interface:
                group = m.groupdict()
                intf_name = Common.convert_intf_name(interface)
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf_name, {})
                lanes_dict = intf_dict.setdefault('lanes', {})
                lane_id = int(group['lane'])
                lane = lanes_dict.setdefault(lane_id, {})
                lane['tx_power'] = float(group['lane_tx_power'])
                continue

            m = p7.match(line)
            if m and interface:
                group = m.groupdict()
                intf_name = Common.convert_intf_name(interface)
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf_name, {})
                lanes_dict = intf_dict.setdefault('lanes', {})
                lane_id = int(group['lane'])
                lane = lanes_dict.setdefault(lane_id, {})
                lane['bias_current'] = float(group['bias_current'])
                continue

            m = p8.match(line)
            if m and interface:
                group = m.groupdict()
                intf_name = Common.convert_intf_name(interface)
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf_name, {})
                id_dict = intf_dict.setdefault('idprom', {})
                id_dict['description'] = group['description']
                continue

            m = p9.match(line)
            if m and interface:
                group = m.groupdict()
                intf_name = Common.convert_intf_name(interface)
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf_name, {})
                id_dict = intf_dict.setdefault('idprom', {})
                id_dict['transceiver_type'] = group['transceiver_type']
                continue

            m = p10.match(line)
            if m and interface:
                group = m.groupdict()
                intf_name = Common.convert_intf_name(interface)
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf_name, {})
                id_dict = intf_dict.setdefault('idprom', {})
                id_dict['pid'] = group['pid']
                continue

            m = p11.match(line)
            if m and interface:
                group = m.groupdict()
                intf_name = Common.convert_intf_name(interface)
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf_name, {})
                id_dict = intf_dict.setdefault('idprom', {})
                id_dict['vendor_revision'] = group['vendor_revision']
                continue

            m = p12.match(line)
            if m and interface:
                group = m.groupdict()
                intf_name = Common.convert_intf_name(interface)
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf_name, {})
                id_dict = intf_dict.setdefault('idprom', {})
                id_dict['serial_number'] = group['serial_number']
                continue

            m = p13.match(line)
            if m and interface:
                group = m.groupdict()
                intf_name = Common.convert_intf_name(interface)
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf_name, {})
                id_dict = intf_dict.setdefault('idprom', {})
                id_dict['vendor_name'] = group['vendor_name']
                continue

            m = p14.match(line)
            if m and interface:
                group = m.groupdict()
                intf_name = Common.convert_intf_name(interface)
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf_name, {})
                id_dict = intf_dict.setdefault('idprom', {})
                id_dict['vendor_oui'] = group['vendor_oui']
                continue

            m = p15.match(line)
            if m and interface:
                group = m.groupdict()
                intf_name = Common.convert_intf_name(interface)
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf_name, {})
                id_dict = intf_dict.setdefault('idprom', {})
                id_dict['clei_code'] = group['clei_code']
                continue

            m = p16.match(line)
            if m and interface:
                group = m.groupdict()
                intf_name = Common.convert_intf_name(interface)
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf_name, {})
                id_dict = intf_dict.setdefault('idprom', {})
                id_dict['part_number'] = group['part_number']
                continue

            m = p17.match(line)
            if m and interface:
                group = m.groupdict()
                intf_name = Common.convert_intf_name(interface)
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf_name, {})
                id_dict = intf_dict.setdefault('idprom', {})
                id_dict['device_state'] = group['device_state']
                continue

            m = p18.match(line)
            if m and interface:
                group = m.groupdict()
                intf_name = Common.convert_intf_name(interface)
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf_name, {})
                id_dict = intf_dict.setdefault('idprom', {})
                id_dict['date_code'] = group['date_code']
                continue

            m = p19.match(line)
            if m and interface:
                group = m.groupdict()
                intf_name = Common.convert_intf_name(interface)
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf_name, {})
                id_dict = intf_dict.setdefault('idprom', {})
                id_dict['connector_type'] = group['connector_type']
                continue

            m = p20.match(line)
            if m and interface:
                group = m.groupdict()
                intf_name = Common.convert_intf_name(interface)
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf_name, {})
                id_dict = intf_dict.setdefault('idprom', {})
                id_dict['encoding'] = group['encoding']
                continue

            m = p21.match(line)
            if m and interface:
                group = m.groupdict()
                intf_name = Common.convert_intf_name(interface)
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(intf_name, {})
                id_dict = intf_dict.setdefault('idprom', {})
                id_dict['nominal_bitrate'] = group['nominal_bitrate']
                continue

        return result_dict