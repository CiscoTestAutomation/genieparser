"""
Module:
    genie.libs.parser.ironware.show_optic

Author:
    James Di Trapani <james@ditrapani.com.au> - https://github.com/jamesditrapani

Description:
    Optical parsers for IronWare devices

Parsers:
    * show optic <slot>
"""

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

__author__ = 'James Di Trapani <james@ditrapani.com.au>'


# ======================================================
# Schema for 'show optic'
# ======================================================
class ShowOpticSchema(MetaParser):
    """Schema for show interfaces brief wide"""
    schema = {
        'interfaces': {
            Any(): {
                'temperature': {
                    'value': Or(float, str),
                    Optional('alarm'): str
                },
                'tx': {
                    'value': Or(float, str),
                    Optional('alarm'): str
                },
                'rx': {
                    'value': Or(float, str),
                    Optional('alarm'): str
                },
                'tx_bias_current': {
                    'value': Or(float, str),
                    Optional('alarm'): str
                }
            }
        }
    }


# ====================================================
#  parser for 'show optic'
# ====================================================
class ShowOptic(ShowOpticSchema):
    """
    Parser for show optic <slot> on Ironware devices
    """
    cli_command = 'show optic {slot}'

    """
    Port  Temperature   Tx Power     Rx Power     Tx Bias Current
    +----+-----------+-------------+------------+----------------+
    1/1   31.3789 C  -040.0000 dBm -040.0000 dBm    0.000 mA
        Normal      Low-Alarm      Low-Alarm     Low-Warn
    1/2   34.4335 C  -006.3507 dBm -006.7243 dBm   14.650 mA
        Normal       Normal           Normal      Normal
    1/3   38.9765 C  -006.9572 dBm -007.6980 dBm   20.800 mA
        Normal       Normal           Normal      Normal
    1/4   38.9492 C  -006.2324 dBm -007.1760 dBm   27.468 mA
        Normal       Normal           Normal      Normal
    1/5   50.5156 C  -005.8720 dBm -008.0106 dBm   41.800 mA
        Normal       Normal           Normal      Normal
    1/6   43.1718 C  -006.5403 dBm -004.4696 dBm   23.100 mA
        Normal       Normal        High-Warn      Normal
    """

    def cli(self, slot, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(slot=slot))
        else:
            out = output

        result_dict = {}

        # 1/1   31.3789 C  -040.0000 dBm -040.0000 dBm    0.000 mA
        p1 = re.compile(r'(^(?P<port>\d+\/\d+)\s+'
                        r'(?P<temp>\d+.\d+|N\/A)(\sC|)\s+'
                        r'(?P<tx>[-]?\d+.\d+|N\/A|NONE)(\s+dBm|'
                        r'\s+dBm\/\s*\d+\s+uW|)\s+'
                        r'(?P<rx>[-]?\d+.\d+|N\/A|NONE)(\s+dBm|'
                        r'\s+dBm\/\s*\d+\s+uW|)\s+'
                        r'(?P<tbc>[-]?\d+.\d+|N\/A)(\s+mA|))')

        # Normal      Low-Alarm      Low-Alarm     Low-Warn
        p2 = re.compile(r'(^(?P<temp>Normal|Low-Alarm|Low-Warn|'
                        r'High-Warn|High-Alarm)\s+'
                        r'(?P<tx>Normal|Low-Alarm|Low-Warn|'
                        r'High-Warn|High-Alarm)\s+'
                        r'(?P<rx>Normal|Low-Alarm|Low-Warn|'
                        r'High-Warn|High-Alarm)\s+'
                        r'(?P<tbc>Normal|Low-Alarm|Low-Warn|'
                        r'High-Warn|High-Alarm))')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                if 'interfaces' not in result_dict:
                    interfaces_dict = result_dict.setdefault('interfaces', {})

                port = 'ethernet{0}'.format(m.groupdict()['port'])

                temp = m.groupdict()['temp']
                tx = m.groupdict()['tx']
                rx = m.groupdict()['rx']
                tbc = m.groupdict()['tbc']

                int_dict = interfaces_dict[port] = {
                    'temperature': {
                        'value': self.can_float(temp)
                    },
                    'tx': {
                        'value': self.can_float(tx)
                    },
                    'rx': {
                        'value': self.can_float(rx)
                    },
                    'tx_bias_current': {
                        'value': self.can_float(tbc)
                    }
                }
                continue

            m = p2.match(line)
            if m:
                temp = m.groupdict()['temp']
                rx = m.groupdict()['rx']
                tx = m.groupdict()['tx']
                tbc = m.groupdict()['tbc']

                interfaces_dict[port]['temperature']['alarm'] = temp
                interfaces_dict[port]['rx']['alarm'] = rx
                interfaces_dict[port]['tx']['alarm'] = tx
                interfaces_dict[port]['tx_bias_current']['alarm'] = tbc
                continue

        return result_dict

    def can_float(self, val):
        try:
            val = float(val)
            return val
        except ValueError:
            return val
