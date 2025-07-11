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