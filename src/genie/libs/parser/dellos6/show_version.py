'''
Author: Knox Hutchinson
Contact: https://dataknox.dev
https://twitter.com/data_knox
https://youtube.com/c/dataknox
'''
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

# ======================================================
# Schema for 'show version'
# ======================================================


class ShowVersionSchema(MetaParser):
    schema = {
        'version': {
            'machine_dsc': str,
            'model': str,
            'machine_type': str,
            'serial': str,
            'manufacturer': str,
            'bia': str,
            'sys_obj_id': str,
            'soc_ver': str,
            'hw_ver': str,
            'cpld_ver': str,
            'versioning': {
                'unit': str,
                'active_ver': str,
                'backup_ver': str,
                'curr_act_ver': str,
                'next_act_ver': str
            }
        }
    }


class ShowVersion(ShowVersionSchema):
    """Parser for show version on Dell PowerSwitch OS6 devices
    parser class - implements detail parsing mechanisms for cli output.
    """
    cli_command = 'show version'

    """
    Machine Description............... Dell Networking Switch
    System Model ID................... N1548
    Machine Type...................... Dell Networking N1548
    Serial Number..................... CN0V143P2829856D0183A00
    Manufacturer...................... 0xbc00
    Burned In MAC Address............. F8B1.5683.8731
    System Object ID.................. 1.3.6.1.4.1.674.10895.3065
    SOC Version....................... BCM56150_A0
    HW Version........................ 2
    CPLD Version...................... 16

    unit active      backup      current-active next-active
    ---- ----------- ----------- -------------- --------------
    1    6.3.2.4     6.2.5.3     6.3.2.4        6.3.2.4
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        ver_dict = {}
        result_dict = {}

        p0 = re.compile(r'^Machine +Description\.+\s(?P<mach_desc>.+)$')

        p1 = re.compile(r'^System +Model +ID+\.+\s(?P<sys_model_id>.+)$')

        p2 = re.compile(r'^Machine+ Type+\.+\s(?P<mach_type>.+)$')

        p3 = re.compile(r'^Serial +Number+\.+\s(?P<serial>.+)$')

        p4 = re.compile(r'^Manufacturer+\.+\s(?P<manufacturer>.+)$')

        p5 = re.compile(r'^Burned +In +MAC +Addres+\.+\s(?P<bia>.+)$')

        p6 = re.compile(r'^System +Object +ID+\.+\s(?P<sys_obj_id>.+)$')

        p7 = re.compile(r'^SOC +Version+\.+\s(?P<soc_ver>.+)$')

        p8 = re.compile(r'^HW +Version+\.+\s(?P<hw_ver>.+)$')

        p9 = re.compile(r'^CPLD +Version+\.+\s(?P<cpld_ver>.+)$')

        p10 = re.compile(
            r'^(?P<unit>\d)+\s+(?P<active_ver>\d\.\d\.\d\.\d)+\s+(?P<backup_ver>\d\.\d\.\d\.\d)+\s+(?P<curr_act_ver>\d\.\d\.\d\.\d)+\s+(?P<next_act_ver>\d\.\d\.\d\.\d)')

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                mach_desc = m.groupdict()['mach_desc']
                if 'version' not in ver_dict:
                    result_dict = ver_dict.setdefault('version', {})
                result_dict['machine_dsc'] = mach_desc
                continue

            m = p1.match(line)
            if m:
                sys_model_id = m.groupdict()['sys_model_id']
                result_dict['model'] = sys_model_id
                continue

            m = p2.match(line)
            if m:
                mach_type = m.groupdict()['mach_type']
                result_dict['machine_type'] = mach_type
                continue

            m = p3.match(line)
            if m:
                serial = m.groupdict()['serial']
                result_dict['serial'] = serial
                continue

            m = p4.match(line)
            if m:
                manufacturer = m.groupdict()['manufacturer']
                result_dict['manufacturer'] = manufacturer
                continue

            m = p5.match(line)
            if m:
                bia = m.groupdict()['bia']
                result_dict['bia'] = bia
                continue

            m = p6.match(line)
            if m:
                sys_obj_id = m.groupdict()['sys_obj_id']
                result_dict['sys_obj_id'] = sys_obj_id
                continue

            m = p7.match(line)
            if m:
                soc_ver = m.groupdict()['soc_ver']
                result_dict['soc_ver'] = soc_ver
                continue

            m = p8.match(line)
            if m:
                hw_ver = m.groupdict()['hw_ver']
                result_dict['hw_ver'] = hw_ver
                continue

            m = p9.match(line)
            if m:
                cpld_ver = m.groupdict()['cpld_ver']
                result_dict['cpld_ver'] = cpld_ver
                continue

            m = p10.match(line)
            if m:
                unit = m.groupdict()['unit']
                active_ver = m.groupdict()['active_ver']
                backup_ver = m.groupdict()['backup_ver']
                curr_act_ver = m.groupdict()['curr_act_ver']
                next_act_ver = m.groupdict()['next_act_ver']
                result_dict['versioning'] = {}
                result_dict['versioning']['unit'] = unit
                result_dict['versioning']['active_ver'] = active_ver
                result_dict['versioning']['backup_ver'] = backup_ver
                result_dict['versioning']['curr_act_ver'] = curr_act_ver
                result_dict['versioning']['next_act_ver'] = next_act_ver

        return ver_dict
