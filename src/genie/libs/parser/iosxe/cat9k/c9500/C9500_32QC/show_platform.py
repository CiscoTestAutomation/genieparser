'''show_platform.py

IOSXE C9500-32QC parsers for the following show commands:
   * show platform
'''

# Python
import re
import logging
import xmltodict

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, And, Default, Use

# import parser utils
from genie.libs.parser.utils.common import Common

# ===========================
#  Schema for 'show platform'
# ===========================
class ShowPlatformSchema(MetaParser):

    """Schema for show platform"""

    schema = {
            'chassis': str,
            'slot': {
                Any(): {
                    Optional('cpld_ver'): str,
                    Optional('fw_ver'): str,
                    'insert_time': str,
                    'name': str,
                    'slot': str,
                    'state': str,
                    Optional('subslot'): {
                        Any(): {
                            'insert_time': str,
                            'name': str,
                            'state': str,
                            'subslot': str,
                        },
                    }
                },
            }
        }


# ===========================
#  Parser for 'show platform'
# ===========================
class ShowPlatform(ShowPlatformSchema):

    ''' Parser for:
        * 'show platform'
    '''

    cli_command = ['show platform']
    exclude = ['insert_time']

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        platform_dict = {}

        # Chassis type: C9500-32QC
        p0 = re.compile(r'^Chassis +type: +(?P<chassis>\S+)$')

        # Slot      Type                State                 Insert time (ago)
        # --------- ------------------- --------------------- -----------------
        # 1         C9500-32QC          ok                    1d18h
        p1 = re.compile(r'^(?P<slot>[\w\d]+) +(?P<name>\S+) +'
                         r'(?P<state>\w+(\, \w+)?) +(?P<insert_time>\S+)$')

        # Slot      Type                State                 Insert time (ago)
        # --------- ------------------- --------------------- -----------------
        #  1/0      C9500-32QC          ok                    1d18h
        p2 = re.compile(r'^(?P<slot>\S+)\/(?P<subslot>\d+) +(?P<name>\S+) +'
                         r'(?P<state>\w+(\, \w+)?) +(?P<insert_time>\S+)$')

        # Slot      CPLD Version        Firmware Version
        # --------- ------------------- ---------------------------------------
        # 1         19061022            17.1.1[FC2]
        p3 = re.compile(r'^(?P<slot>\S+) +(?P<cpld_version>\d+) +'
                         r'(?P<fireware_ver>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # Chassis type: C9500-32QC
            m = p0.match(line)
            if m:
                chassis = m.groupdict()['chassis']
                platform_dict.setdefault('chassis', chassis)
                continue

            # Slot      Type                State                 Insert time (ago)
            # --------- ------------------- --------------------- -----------------
            # 1         C9500-32QC          ok                    1d18h
            m = p1.match(line)
            if m:
                slot = m.groupdict()['slot']
                slot_dict = platform_dict.setdefault('slot', {}).setdefault(slot, {})
                slot_dict['name'] = m.groupdict()['name']
                slot_dict['state'] = m.groupdict()['state']
                slot_dict['insert_time'] = m.groupdict()['insert_time']
                slot_dict['slot'] = slot
                continue

            # Slot      Type                State                 Insert time (ago)
            # --------- ------------------- --------------------- -----------------
            #  1/0      C9500-32QC          ok                    1d18h
            m = p2.match(line)
            if m:
                slot = m.groupdict()['slot']
                subslot = m.groupdict()['subslot']
                subslot_dict = platform_dict.setdefault('slot', {}).setdefault(
                    slot, {}).setdefault('subslot', {}).setdefault(subslot, {})
                subslot_dict['name'] = m.groupdict()['name']
                subslot_dict['state'] = m.groupdict()['state']
                subslot_dict['insert_time'] = m.groupdict()['insert_time']
                subslot_dict['subslot'] = subslot
                continue

            # Slot      CPLD Version        Firmware Version
            # --------- ------------------- ---------------------------------------
            # 1         19061022            17.1.1[FC2]
            m = p3.match(line)
            if m:
                slot = m.groupdict()['slot']
                slot_dict = platform_dict.setdefault('slot', {}).setdefault(slot, {})
                slot_dict['cpld_ver'] = m.groupdict()['cpld_version']
                slot_dict['fw_ver'] = m.groupdict()['fireware_ver']
                continue

        return platform_dict
