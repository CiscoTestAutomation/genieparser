"""
Author:
    Fabio Pessoa Nunes (https://www.linkedin.com/in/fpessoanunes/)

show_version.py

SLXOS parsers for the following show commands:
    * show version

Schemas based on SLX's YANG models
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =================================================
# Schema for:
#   * 'show version'
# ==================================================
class ShowVersionSchema(MetaParser):
    """Schema for show version"""

    schema = {
        'version': {
            'firmware_ver': str,
            'build_time': str,
            'install_time': str,
            'system_uptime': str,
            Optional('primary_ver'): str,
            Optional('secondary_ver'): str,
            Optional('slot'): {
                Any(): {
                    'name': str,
                    'status': str,
                    'primary_ver': str,
                    'secondary_ver': str
                }
            }
        }
    }


# ===================================
# Parser for:
#   * 'show version'
# ===================================
class ShowVersion(ShowVersionSchema):
    ''' Parser for "show version" '''

    cli_command = ['show version']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        ver_dict = {}
        result_dict = {}

        # Firmware name:      18r.1.00h
        p0 = re.compile(r'^Firmware name:\s+(?P<firmware_ver>.+)\s*$')

        # Build Time:         08:13:43 Apr  7, 2021
        p1 = re.compile(r'^Build Time:\s+(?P<build_time>.+)\s*$')

        # Install Time:       07:14:32 Jun  1, 2021
        p2 = re.compile(r'^Install Time:\s+(?P<install_time>.+)\s*$')

        # System Uptime:   93days 5hrs 32mins 10secs
        p3 = re.compile(r'^System Uptime:\s+(?P<system_uptime>.*)$')

        # M1      SLX-OS  18r.1.00h                                          ACTIVE*
        #                 18r.1.00h
        # SLX-OS   20.2.2a
        p4 = re.compile(
            r'^(?P<slot>[A-Z0-9]+[\/[0-9]+]?)?\s*SLX-OS\s+'
            r'(?P<primary_ver>\d+\w?\.\d+\.\d+\S*)\s*'
            r'(?P<status>[a-zA-Z]+)?\*?\s*$')
        
        # 20.2.2a
        p5 = re.compile(r'^\s*(?P<secondary_ver>\d+\w?\.\d+\.\d+[a-z]*)\s*$')

        for line in out.splitlines():
            line = line.strip()

            # Firmware name:      18r.1.00h
            m = p0.match(line)
            if m:
                firmware_ver = m.groupdict()['firmware_ver']
                if 'version' not in ver_dict:
                    result_dict = ver_dict.setdefault('version', {})
                result_dict['firmware_ver'] = firmware_ver
                continue

            # Build Time:         08:13:43 Apr  7, 2021
            m = p1.match(line)
            if m:
                build_time = m.groupdict()['build_time']
                result_dict['build_time'] = build_time
                continue

            # Install Time:       07:14:32 Jun  1, 2021
            m = p2.match(line)
            if m:
                install_time = m.groupdict()['install_time']
                result_dict['install_time'] = install_time
                continue

            # System Uptime:   93days 5hrs 32mins 10secs
            m = p3.match(line)
            if m:
                system_uptime = m.groupdict()['system_uptime']
                result_dict['system_uptime'] = system_uptime
                continue

            # M1      SLX-OS  18r.1.00h                                          ACTIVE*
            #                 18r.1.00h
            # SLX-OS   20.2.2a
            m = p4.match(line)
            if m:
                if m.groupdict()['slot'] is not None:
                    slot = m.groupdict()['slot']
                    primary_ver = m.groupdict()['primary_ver']
                    status = m.groupdict()['status']
                    if 'slot' not in result_dict:
                        result_dict['slot'] = {}
                    result_dict['slot'][slot] = {}
                    slot_dict = result_dict['slot'][slot]
                    slot_dict['name'] = slot
                    slot_dict['primary_ver'] = primary_ver
                    slot_dict['status'] = status
                else:
                    slot = None
                    primary_ver = m.groupdict()['primary_ver']
                    result_dict['primary_ver'] = primary_ver
                continue
            
            # 20.2.2a
            m = p5.match(line)
            if m:
                secondary_ver = m.groupdict()['secondary_ver']
                if slot is None:
                    result_dict['secondary_ver'] = secondary_ver
                else:
                    slot_dict['secondary_ver'] = secondary_ver
                    slot = None
                continue

        return ver_dict
