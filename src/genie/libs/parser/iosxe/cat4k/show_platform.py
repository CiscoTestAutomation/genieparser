"""cat4k implementation of show_platform.py

"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


class ShowModuleSchema(MetaParser):
    """Schema for show module"""
    schema = {
        'chassis_type': str,
        'power_consumed': str,
        'mod': {
            Any(): {
                'slot': int,
                'port': int,
                'card_type': str,
                'model': str,
                'serial_number': str,
                'mac_address_from': str,
                'mac_address_to': str,
                'hw_ver': str,
                Optional('fw_ver'): str,
                Optional('sw_ver'): str,
                'status': str,
                Optional('redundancy_role'): str,
                Optional('operating_mode'): str,
                Optional('redundancy_status'): str
            }
        },
        Optional('system_failures'): {
            'power_supply': str
        }
    }


class ShowModule(ShowModuleSchema):
    """Parser for show module"""
    cli_command = 'show module'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        # Chassis Type : WS-C4507R+E
        p1 = re.compile(r'^Chassis Type +: +(?P<chassis_type>.+)$')

        # Power consumed by backplane : 40 Watts
        p2 = re.compile(r'^Power consumed by backplane +: +(?P<power_consumed>.+)$')

        # 1    48  10/100/1000BaseT Premium POE E Series  WS-X4648-RJ45V+E   ABCDE123456
        # 3     6  Sup 7L-E 10GE (SFP+), 1000BaseX (SFP)  WS-X45-SUP7L-E     QWERT987654
        p3 = re.compile(r'^(?P<mod>\d+) +(?P<port>\d+) +(?P<card_type>[\S\s]+) +(?P<model>\S+) +(?P<serial_number>\S+)$')

        # 3 555a.88ff.584c to 555a.88ff.5859 3.0 15.0(1r)SG10 03.06.07.E       Ok
        p4 = re.compile(r'^(?P<mod>\d+) +(?P<mac_address_from>[\w\.]+) +to +(?P<mac_address_to>[\w\.]+) +(?P<hw_ver>[\w\.\(\)]+) +(?P<fw_ver>[\w\.\(\)]+) +(?P<sw_ver>[\w\.\(\)]+) +(?P<status>\w+)$')

        # 1 11a1.b2ff.ee55 to 11a1.b2ff.ee61 3.1                               Ok
        p4_1 = re.compile(r'^(?P<mod>\d+) +(?P<mac_address_from>[\w\.]+) +to +(?P<mac_address_to>[\w\.]+) +(?P<hw_ver>[\w\.\(\)]+) +(?P<status>\w+)$')

        # 3   Active Supervisor   RPR                 Active
        p5 = re.compile(r'^(?P<mod>\d+) +(?P<redundancy_role>[\S\s]+) +(?P<operating_mode>\S+) +(?P<redundancy_status>\S+)$')

        # Power Supply:   bad/off (see 'show power')
        p6 = re.compile(r'^Power Supply: +(?P<power_supply>.+)$')


        for line in out.splitlines():
            line = line.strip()

            # Chassis Type : WS-C4507R+E
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'chassis_type': group['chassis_type']})
                continue

            # Power consumed by backplane : 40 Watts
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'power_consumed': group['power_consumed']})
                continue

            # 1    48  10/100/1000BaseT Premium POE E Series  WS-X4648-RJ45V+E   ABCDE123456
            # 3     6  Sup 7L-E 10GE (SFP+), 1000BaseX (SFP)  WS-X45-SUP7L-E     QWERT987654
            m = p3.match(line)
            if m:
                group = m.groupdict()
                mode_dict = ret_dict.setdefault('mod', {}).setdefault(int(group['mod']), {})
                mode_dict.update({'slot': int(group['mod'])})
                mode_dict.update({'port': int(group['port'])})
                mode_dict.update({'card_type': group['card_type'].strip()})
                mode_dict.update({'model': group['model']})
                mode_dict.update({'serial_number': group['serial_number']})
                continue

            # 3 555a.88ff.584c to 555a.88ff.5859 3.0 15.0(1r)SG10 03.06.07.E       Ok
            m = p4.match(line)
            if m:
                group = m.groupdict()
                mode_dict = ret_dict.setdefault('mod', {}).setdefault(int(group['mod']), {})
                mode_dict.update({'mac_address_from': group['mac_address_from']})
                mode_dict.update({'mac_address_to': group['mac_address_to']})
                mode_dict.update({'hw_ver': group['hw_ver']})
                mode_dict.update({'fw_ver': group['fw_ver']})
                mode_dict.update({'sw_ver': group['sw_ver']})
                mode_dict.update({'status': group['status']})
                continue

            # 1 11a1.b2ff.ee55 to 11a1.b2ff.ee61 3.1                               Ok
            m = p4_1.match(line)
            if m:
                group = m.groupdict()
                mode_dict = ret_dict.setdefault('mod', {}).setdefault(int(group['mod']), {})
                mode_dict.update({'mac_address_from': group['mac_address_from']})
                mode_dict.update({'mac_address_to': group['mac_address_to']})
                mode_dict.update({'hw_ver': group['hw_ver']})
                mode_dict.update({'status': group['status']})
                continue

            # 3   Active Supervisor   RPR                 Active
            m = p5.match(line)
            if m:
                group = m.groupdict()
                mode_dict = ret_dict.setdefault('mod', {}).setdefault(int(group['mod']), {})
                mode_dict.update({'redundancy_role': group['redundancy_role'].strip()})
                mode_dict.update({'operating_mode': group['operating_mode']})
                mode_dict.update({'redundancy_status': group['redundancy_status']})
                continue

            ## Power Supply:   bad/off (see 'show power')
            m = p6.match(line)
            if m:
                group = m.groupdict()
                system_dict = ret_dict.setdefault('system_failures', {})
                system_dict.update({'power_supply': group['power_supply']})
                continue

        return ret_dict