"""show_platform.py

NXOS parser class for below commands:
       show version
        show processes cpu
        show processes cpu | include <include>
        show processes memory
        show processes memory | include <include>
        show cores
"""
import re

try:
    from pyats import tcl
except Exception:
    pass

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or, And, Default, Use


def regexp(expression):
    def match(value):
        if re.match(expression,value):
            return value
        else:
            raise TypeError("Value '%s' doesnt match regex '%s'"
                              %(value, expression))
    return match


class ShowVersionSchema(MetaParser):
    """Schema for show version"""

    schema = {'platform':
                  {Optional('name'): str,
                   Optional('reason'): str,
                   Optional('system_version'): str,
                   Optional('os'): str,
                   'hardware':
                      {Optional('bootflash'): str,
                       Optional('slot0'): str,
                       Optional('chassis'): str,
                       Optional('rp'): str,
                       Optional('cpu'): Or(str, None),
                       Optional('device_name'): str,
                       Optional('memory'): str,
                       Optional('model'): str,
                       Optional('processor_board_id'): str,
                       Optional('slots'): str},
                  'kernel_uptime':
                      {Optional('days'): int,
                       Optional('hours'): int,
                       Optional('minutes'): int,
                       Optional('seconds'): int},
                  'software':
                      {Optional('bios_version'): str,
                       Optional('bios_compile_time'): str,
                       Optional('kickstart_version'): str,
                       Optional('kickstart_compile_time'): str,
                       Optional('kickstart_image_file'): str,
                       Optional('system_version'): str,
                       Optional('system_compile_time'): str,
                       Optional('system_image_file'): str}
                  }
              }

class ShowVersion(ShowVersionSchema):
    """Parser for :
        show version
        parser class implements detail parsing mechanisms for cli, xml and yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).
    cli_command = 'show version'
    exclude = [
        'seconds',
        'minutes',
        'hours',
        'days',
        'essor_board_id',
        'reason']

    def cli(self,output=None):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        version_dict = {}

        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Cisco +(?P<platform>[a-zA-Z]+) +Operating +System +\((?P<os>[A-Z\-]+)\)? +Software$')
            m = p1.match(line)
            if m:
                name = str(m.groupdict()['platform'])
                os = str(m.groupdict()['os'])

                if 'platform' not in version_dict:
                    version_dict['platform'] = {}
                if 'name' not in version_dict['platform']:
                    version_dict['platform']['name'] = name
                if 'os' not in version_dict['platform']:
                    version_dict['platform']['os'] = os
                continue

            p2 = re.compile(r'^\s*Software$')
            m = p2.match(line)
            if m:

                if 'software' not in version_dict['platform']:
                    version_dict['platform']['software'] = {}
                continue

            p3 = re.compile(r'^\s*BIOS: +version +(?P<bios_version>[0-9\.]+)?$')
            m = p3.match(line)
            if m:

                bios_version = str(m.groupdict()['bios_version'])

                if 'bios_version' not in version_dict['platform']['software']:
                    version_dict['platform']['software']['bios_version'] = bios_version
                continue

            p4 = re.compile(r'^\s*kickstart: +version +(?P<kickstart_version>[\w\.\(\)\[\]\s]+)$')
            m = p4.match(line)
            if m:
                kickstart_version = str(m.groupdict()['kickstart_version'])

                if 'kickstart_version' not in version_dict['platform']['software']:
                    version_dict['platform']['software']['kickstart_version'] = kickstart_version
                continue

            p5 = re.compile(r'^\s*system: +version +(?P<system_version>[\w\.\(\)\[\]\s]+)$')
            m = p5.match(line)
            if m:
                system_version = str(m.groupdict()['system_version'])

                if 'system_version' not in version_dict['platform']['software']:
                    version_dict['platform']['software']['system_version'] = system_version
                continue

            p6 = re.compile(r'^\s*NXOS: +version +(?P<system_version>[A-Za-z0-9\.\(\)\[\]\s]+)$')
            m = p6.match(line)
            if m:
                system_version = str(m.groupdict()['system_version'])

                if 'system_version' not in version_dict['platform']['software']:
                    version_dict['platform']['software']['system_version'] = system_version
                continue

            p7 = re.compile(r'^\s*BIOS +compile +time: +(?P<bios_compile_time>[0-9\/]+)?$')
            m = p7.match(line)
            if m:
                bios_compile_time = str(m.groupdict()['bios_compile_time'])

                if 'bios_compile_time' not in version_dict['platform']['software']:
                    version_dict['platform']['software']['bios_compile_time'] = bios_compile_time
                continue

            p8 = re.compile(r'^\s*kickstart +image +file +is: +(?P<kickstart_image_file>[\w\:\/\-\.]+)$')
            m = p8.match(line)
            if m:
                kickstart_image_file = str(m.groupdict()['kickstart_image_file'])

                if 'kickstart_image_file' not in version_dict['platform']['software']:
                    version_dict['platform']['software']['kickstart_image_file'] = kickstart_image_file
                continue

            p9 = re.compile(r'^\s*kickstart +compile +time: +(?P<kickstart_compile_time>[0-9\/\s\:\[\]]+)$')
            m = p9.match(line)
            if m:
                kickstart_compile_time = str(m.groupdict()['kickstart_compile_time'])

                if 'kickstart_compile_time' not in version_dict['platform']['software']:
                    version_dict['platform']['software']['kickstart_compile_time'] = kickstart_compile_time
                continue

            p10 = re.compile(r'^\s*system +image +file +is: +(?P<system_image_file>[\w\:\/\-\.]+)$')
            m = p10.match(line)
            if m:
                system_image_file = str(m.groupdict()['system_image_file'])

                if 'system_image_file' not in version_dict['platform']['software']:
                    version_dict['platform']['software']['system_image_file'] = system_image_file
                continue

            p11 = re.compile(r'^\s*system +compile +time: +(?P<system_compile_time>[0-9\/\s\:\[\]]+)$')
            m = p11.match(line)
            if m:
                system_compile_time = str(m.groupdict()['system_compile_time'])

                if 'system_compile_time' not in version_dict['platform']['software']:
                    version_dict['platform']['software']['system_compile_time'] = system_compile_time
                continue

            p12 = re.compile(r'^\s*NXOS +image +file +is: +(?P<system_image_file>[\w\:\/\-\.]+)$')
            m = p12.match(line)
            if m:
                system_image_file = str(m.groupdict()['system_image_file'])

                if 'system_image_file' not in version_dict['platform']['software']:
                    version_dict['platform']['software']['system_image_file'] = system_image_file
                continue

            p13 = re.compile(r'^\s*NXOS +compile +time: +(?P<system_compile_time>[0-9\/\s\:\[\]]+)$')
            m = p13.match(line)
            if m:
                system_compile_time = str(m.groupdict()['system_compile_time'])

                if 'system_compile_time' not in version_dict['platform']['software']:
                    version_dict['platform']['software']['system_compile_time'] = system_compile_time
                continue

            p14 = re.compile(r'^\s*Hardware$')
            m = p14.match(line)
            if m:

                if 'hardware' not in version_dict['platform']:
                    version_dict['platform']['hardware'] = {}
                continue

            # cisco NX-OSv chassis
            # cisco Nexus7000 C7009 (9 Slot) Chassis ("Supervisor Module-2")
            # cisco Nexus 5596 Chassis ("O2 48X10GE/Modular Supervisor")
            # cisco N9K-C93180YC-EX ("supervisor")
            p15 = re.compile(r'^\s*cisco +(?P<model>[a-zA-Z0-9\-\s]+)'
            #r'( +\((?P<slot>[0-9]+) Slot\))?( +[C|c]hassis)?( +\(\"(?P<rp>'
            r'( +\((?P<slot>[0-9]+) Slot\))?( +[C|c]hassis)( +\(\"(?P<rp>'
            #r'( +\((?P<slot>[0-9]+) Slot\))? +[C|c]hassis( +\(\"(?P<rp>'
            r'[a-zA-Z0-9\s\-\/\+]+)\"\))?(\s)?$')
            m = p15.match(line)
            if m:
                model = chassis = str(m.groupdict()['model'])
                slot = str(m.groupdict()['slot'])
                rp = str(m.groupdict()['rp'])

                if 'model' not in version_dict['platform']['hardware']:
                    version_dict['platform']['hardware']['model'] = model
                    version_dict['platform']['hardware']['chassis'] = chassis

                if 'slots' not in version_dict['platform']['hardware']:
                    version_dict['platform']['hardware']['slots'] = slot

                if 'rp' not in version_dict['platform']['hardware']:
                    version_dict['platform']['hardware']['rp'] = rp
                continue


            # Intel(R) Xeon(R) CPU         with 32938744 kB of memory.
            # Intel(R) Core(TM) i3- CPU @ 2.50GHz with 12345678 kB of memory.
            # Intel(R) Celeron(R) M CPU with 2073416 kB of memory.
            p16 = re.compile(r'^(?P<cpu>.*) +with +(?P<memory>[0-9a-zA-Z\s]+) +of +memory\.$')
            m = p16.match(line)
            if m:

                cpu = str(m.groupdict()['cpu']).strip()
                memory = str(m.groupdict()['memory'])

                if cpu == ' ':
                    cpu = None

                if 'cpu' not in version_dict['platform']['hardware']:
                    version_dict['platform']['hardware']['cpu'] = cpu

                if 'memory' not in version_dict['platform']['hardware']:
                    version_dict['platform']['hardware']['memory'] = memory

                continue

            p17 = re.compile(r'^\s*Processor +Board +ID +(?P<processor_board_id>[A-Z0-9]+)$')
            m = p17.match(line)
            if m:

                processor_board_id = str(m.groupdict()['processor_board_id'])

                if 'processor_board_id' not in version_dict['platform']['hardware']:
                    version_dict['platform']['hardware']['processor_board_id'] = processor_board_id

                continue

            p18 = re.compile(r'^\s*Device name: +(?P<device_name>[a-zA-Z0-9\-\_]+)$')
            m = p18.match(line)
            if m:

                device_name = str(m.groupdict()['device_name'])

                if 'device_name' not in version_dict['platform']['hardware']:
                    version_dict['platform']['hardware']['device_name'] = device_name

                continue

            p19 = re.compile(r'^\s*bootflash: +(?P<bootflash>[a-zA-Z0-9\s]+)$')
            m = p19.match(line)
            if m:

                bootflash = str(m.groupdict()['bootflash'])

                if 'bootflash' not in version_dict['platform']['hardware']:
                    version_dict['platform']['hardware']['bootflash'] = bootflash

                continue

            p20 = re.compile(r'^\s*slot0: +(?P<slot0>[a-zA-Z0-9\s]+) +\(expansion flash\)$')
            m = p20.match(line)
            if m:

                slot0 = str(m.groupdict()['slot0'])

                if 'slot0' not in version_dict['platform']['hardware']:
                    version_dict['platform']['hardware']['slot0'] = slot0

                continue

            p21 = re.compile(r'^\s*Kernel +uptime +is +(?P<days>[0-9]+) +day\(s\), +(?P<hours>[0-9]+) +hour\(s\), +(?P<minutes>[0-9]+) +minute\(s\), +(?P<seconds>[0-9]+) +second\(s\)$')
            m = p21.match(line)
            if m:

                if 'kernel_uptime' not in version_dict['platform']:
                    version_dict['platform']['kernel_uptime'] = {}

                days = int(m.groupdict()['days'])
                hours = int(m.groupdict()['hours'])
                minutes = int(m.groupdict()['minutes'])
                seconds = int(m.groupdict()['seconds'])

                if 'days' not in version_dict['platform']['kernel_uptime']:
                    version_dict['platform']['kernel_uptime']['days'] = days

                if 'hours' not in version_dict['platform']['kernel_uptime']:
                    version_dict['platform']['kernel_uptime']['hours'] = hours

                if 'minutes' not in version_dict['platform']['kernel_uptime']:
                    version_dict['platform']['kernel_uptime']['minutes'] = minutes

                if 'seconds' not in version_dict['platform']['kernel_uptime']:
                    version_dict['platform']['kernel_uptime']['seconds'] = seconds

                continue

            p22 = re.compile(r'^\s*Reason: +(?P<reason>[a-zA-Z0-9\s-]+)$')
            m = p22.match(line)
            if m:

                reason = str(m.groupdict()['reason'])

                if 'reason' not in version_dict['platform']:
                    version_dict['platform']['reason'] = reason

                continue

            p23 = re.compile(r'^\s*System version: +(?P<system_version>[0-9\(\)\.]+)?$')
            m = p23.match(line)
            if m:

                system_version = str(m.groupdict()['system_version'])

                if 'system_version' not in version_dict['platform']:
                    version_dict['platform']['system_version'] = system_version

                continue

        return version_dict

class ShowInventorySchema(MetaParser):
    """Schema for show inventory"""
    schema = {'name':
                {Any():
                    {'description': str,
                     'slot': str,
                     Optional('pid'): str,
                     Optional('vid'): str,
                     Optional('serial_number'): str}
                },
            }


class ShowInventory(ShowInventorySchema):
    """Parser for show inventory"""

    cli_command = 'show inventory'

    def cli(self,output=None):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        inventory_dict = {}

        # NAME: "Chassis", DESCR: "NX-OSv Chassis"
        # NAME: "Slot 38",  DESCR: "Nexus7700 C7706 (6 Slot) Chassis Fan Module"
        # NAME: "FEX 106 Module 1",  DESCR: "Fabric Extender Module: 48x1GE, 4x10GE Supervisor"
        p1 = re.compile(r'^NAME: +\"(?P<name>[\S\s]+)\", +DESCR: +\"(?P<description>[\S\s]+)\"$')

        p1_1 = re.compile(r'^Slot +(?P<slot>\d+)$')

        # PID: N9K-NXOSV , VID: , SN: 92XXRQ9UCZS
        # PID: N9K-C9300-FAN2 , VID: V01 , SN: N/A
        # PID: N2K-C2248-FAN       ,  VID: N/A ,  SN: N/A
        p2 = re.compile(r'^PID: +(?P<pid>[\S]*) +, +VID: +(?P<vid>[\S]*) *, +SN: *(?P<serial_number>[\S]*)?$')

        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                name = m.groupdict()['name']
                description = m.groupdict()['description']
                item_dict = inventory_dict.setdefault('name', {}).setdefault(name, {})
                item_dict.update({'description': description})

                m1 = p1_1.match(name)
                if m1:
                    slot = m1.groupdict()['slot']
                else:
                    slot = 'None'

                item_dict.update({'slot': slot})
                continue

            m = p2.match(line)
            if m:
                if m.groupdict()['pid']:
                    item_dict['pid'] = m.groupdict()['pid']
                if m.groupdict()['vid']:
                    item_dict['vid'] = m.groupdict()['vid']
                if m.groupdict()['serial_number']:
                    item_dict['serial_number'] = m.groupdict()['serial_number']
                continue

        return inventory_dict


class ShowInstallActiveSchema(MetaParser):
    """Schema for show install active"""
    schema = {'boot_images':
                {Optional('kickstart_image'): str,
                 Optional('system_image'): str},
              Optional('active_packages'):
                {Any():
                  {Optional('active_package_name'): str}
                },
              }


class ShowInstallActive(ShowInstallActiveSchema):
    """Parser for show install active"""

    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).
    cli_command = 'show install active'

    def cli(self, output=None):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        active_dict = {}
        active_package = False

        active_package_module_number = 0

        p1 = re.compile(r'^\s*(?P<boot_images>[a-zA-Z\s]+):$')
        p2 = re.compile(r'^\s*Kickstart Image: +(?P<kickstart_image>[a-zA-z0-9\:\/\-\.]+)$')
        p3 = re.compile(r'^\s*System Image: +(?P<system_image>[a-zA-z0-9\:\/\-\.]+)$')
        p4 = re.compile(r'^\s*Active Packages:$')
        p5 = re.compile(r'^\s*Active Packages on Module #(?P<module_number>[0-9]+):$')
        p6 = re.compile(r'^\s*(?P<active_package_name>[a-zA-z0-9\-\.]+)$')

        for line in out.splitlines():
            line = line.rstrip()

            m = p1.match(line)
            if m:
                if 'boot_images' not in active_dict:
                    active_dict['boot_images'] = {}
                    continue


            m = p2.match(line)
            if m:
                active_dict['boot_images']['kickstart_image'] = m.groupdict()['kickstart_image']
                continue


            m = p3.match(line)
            if m:
                active_dict['boot_images']['system_image'] = m.groupdict()['system_image']
                continue

            m = p4.match(line)
            if m:
                active_package = True
                if 'active_packages' not in active_dict:
                    active_dict['active_packages'] = {}
                continue

            m = p5.match(line)
            if m:
                active_package = True
                active_package_module_number = m.groupdict()['module_number']
                if 'active_packages' not in active_dict:
                    active_dict['active_packages'] = {}
                continue

            m = p6.match(line)
            if m and active_package:
                module_number = 'active_package_module_' + str(active_package_module_number)
                if module_number not in active_dict['active_packages']:
                    active_dict['active_packages'][module_number] = {}
                active_dict['active_packages'][module_number]['active_package_name'] = m.groupdict()['active_package_name']
                active_package = False
                continue

        return active_dict


# =====================================
# Schema for 'show redundancy status'
# =====================================

class ShowRedundancyStatusSchema(MetaParser):
    """Schema for:
        show redundancy status
        show system redundancy status"""

    schema = {'redundancy_mode':
                  {'administrative': str,
                   'operational': str},
              Any():
                  {'redundancy_state': str,
                   Optional('supervisor_state'): str,
                   Optional('internal_state'):str},
              Optional('system_start_time'): str,
              Optional('system_uptime'): str,
              Optional('kernel_uptime'): str,
              Optional('active_supervisor_time'): str}


class ShowRedundancyStatus(ShowRedundancyStatusSchema):
    """Parser for show redundancy status"""
    cli_command = 'show redundancy status'
    exclude = [
        'active_supervisor_time',
        'kernel_uptime',
        'system_uptime']

    def cli(self, cmd='',output=None):
        if not cmd:
            cmd = self.cli_command

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        redundancy_dict = {}
        sup_number = None
        for line in out.splitlines():
            line = line.rstrip()
            line = line.replace('\t', '  ')
            p1 = re.compile(r'^\s*Redundancy mode$')
            m = p1.match(line)
            if m:
                if 'redundancy_mode' not in redundancy_dict:
                    redundancy_dict['redundancy_mode'] = {}
                continue

            # Redundancy information not available for this platform
            p1 = re.compile(r'^\s*Redundancy +information +not +available +for +this +platform$')
            m = p1.match(line)
            if m:
                if 'redundancy_mode' not in redundancy_dict:
                    redundancy_dict['redundancy_mode'] = {}
                    redundancy_dict['redundancy_mode']['administrative'] = 'none'
                    redundancy_dict['redundancy_mode']['operational'] = 'none'
                continue

            p2 = re.compile(r'^\s*administrative: +(?P<administrative>[a-zA-z\s]+)$')
            m = p2.match(line)
            if m:
                redundancy_dict['redundancy_mode']['administrative'] = m.groupdict()['administrative']
                continue

            p3 = re.compile(r'^\s*operational: +(?P<operational>[a-zA-z\s]+)$')
            m = p3.match(line)
            if m:
                redundancy_dict['redundancy_mode']['operational'] = m.groupdict()['operational']
                continue

            p4 = re.compile(r'^\s*(This|Other) +supervisor +\(sup-(?P<sup_num>\d+)\)$')
            m = p4.match(line)
            if m:
                sup_num = m.groupdict()['sup_num']
                key = 'supervisor_{}'.format(sup_num)
                if key not in redundancy_dict:
                    redundancy_dict[key] = {}
                continue

            p6 = re.compile(r'^\s*Redundancy state: +(?P<redundancy_state>[a-zA-z\W\s]+)$')
            m = p6.match(line)
            if m:
                redundancy_dict[key]['redundancy_state'] = m.groupdict()['redundancy_state']

            p7 = re.compile(r'^\s*Supervisor state: +(?P<supervisor_state>[a-zA-z\s]+)$')
            m = p7.match(line)
            if m:
                redundancy_dict[key]['supervisor_state'] = m.groupdict()['supervisor_state']

            p8 = re.compile(r'^\s*Internal state: +(?P<internal_state>[a-zA-z\s]+)$')
            m = p8.match(line)
            if m:
                redundancy_dict[key]['internal_state'] = m.groupdict()['internal_state']

            p9 = re.compile(r'^\s*System start time: +(?P<system_start_time>[a-zA-z0-9\:\s]+)$')
            m = p9.match(line)
            if m:
                redundancy_dict['system_start_time'] = m.groupdict()['system_start_time']
                continue

            p10 = re.compile(r'^\s*System uptime: +(?P<system_uptime>[a-zA-z0-9\:\,\s]+)$')
            m = p10.match(line)
            if m:
                redundancy_dict['system_uptime'] = m.groupdict()['system_uptime']
                continue

            p11 = re.compile(r'^\s*Kernel uptime: +(?P<kernel_uptime>[a-zA-z0-9\:\,\s]+)$')
            m = p11.match(line)
            if m:
                redundancy_dict['kernel_uptime'] = m.groupdict()['kernel_uptime']
                continue

            p12 = re.compile(r'^\s*Active supervisor uptime: +(?P<active_supervisor_time>[a-zA-z0-9\:\,\s]+)$')
            m = p12.match(line)
            if m:
                redundancy_dict['active_supervisor_time'] = m.groupdict()['active_supervisor_time']
                continue

        return redundancy_dict


# ==========================================
# Parser for 'show system redundancy status'
# ==========================================
class ShowSystemRedundancyStatus(ShowRedundancyStatus):
    """Parser for show system redundancy status"""

    def cli(self,output=None):
        cmd = 'show system redundancy status'
        return super().cli(cmd=cmd,output=output)


class ShowBootSchema(MetaParser):
    """Schema for show boot"""

    schema = {'current_boot_variable':
                  {Optional('sup_number'):
                      {Any():
                          {Optional('kickstart_variable'): str,
                           Optional('system_variable'): str,
                           Optional('boot_poap'):str}
                      },
                  Optional('kickstart_variable'): str,
                  Optional('system_variable'): str,
                  Optional('boot_poap'):str},
              'next_reload_boot_variable':
                  {Optional('sup_number'):
                      {Any():
                          {Optional('kickstart_variable'): str,
                           Optional('system_variable'): str,
                           Optional('boot_poap'):str}
                      },
                  Optional('kickstart_variable'): str,
                  Optional('system_variable'): str,
                  Optional('boot_poap'):str}
              }

class ShowBoot(ShowBootSchema):
    """Parser for show boot"""

    cli_command = 'show boot'

    def cli(self,output=None):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        boot_dict = {}
        boot_variable = None
        sup_number = None
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Current Boot Variables:$')
            m = p1.match(line)
            if m:
                boot_variable = 'current'
                if 'current_boot_variable' not in boot_dict:
                    boot_dict['current_boot_variable'] = {}
                continue

            p2 = re.compile(r'^\s*Boot Variables on next reload:$')
            m = p2.match(line)
            if m:
                boot_variable = 'next'
                if 'next_reload_boot_variable' not in boot_dict:
                    boot_dict['next_reload_boot_variable'] = {}
                continue

            p3 = re.compile(r'^\s*sup-1$')
            m = p3.match(line)
            if m:
                sup_number = 'sup-1'
                if boot_variable == 'current':
                    if 'sup_number' not in boot_dict['current_boot_variable']:
                        boot_dict['current_boot_variable']['sup_number'] = {}
                    if 'sup-1' not in boot_dict['current_boot_variable']['sup_number']:
                        boot_dict['current_boot_variable']['sup_number']['sup-1'] = {}
                elif boot_variable == 'next':
                    if 'sup_number' not in boot_dict['next_reload_boot_variable']:
                        boot_dict['next_reload_boot_variable']['sup_number'] = {}
                    if 'sup-1' not in boot_dict['next_reload_boot_variable']['sup_number']:
                        boot_dict['next_reload_boot_variable']['sup_number']['sup-1'] = {}
                continue

            p4 = re.compile(r'^\s*sup-2$')
            m = p4.match(line)
            if m:
                sup_number = 'sup-2'
                if boot_variable == 'current':
                    if 'sup_number' not in boot_dict['current_boot_variable']:
                        boot_dict['current_boot_variable']['sup_number'] = {}
                    if 'sup-2' not in boot_dict['current_boot_variable']['sup_number']:
                        boot_dict['current_boot_variable']['sup_number']['sup-2'] = {}
                elif boot_variable == 'next':
                    if 'sup_number' not in boot_dict['next_reload_boot_variable']:
                        boot_dict['next_reload_boot_variable']['sup_number'] = {}
                    if 'sup-2' not in boot_dict['next_reload_boot_variable']['sup_number']:
                        boot_dict['next_reload_boot_variable']['sup_number']['sup-2'] = {}
                continue


            p5 = re.compile(r'^\s*kickstart variable = +(?P<kickstart_variable>[a-zA-z0-9\:\-\.\/\s]+)$')
            m = p5.match(line)
            if m:
                if boot_variable == 'current':
                    if sup_number:
                        if sup_number == 'sup-1':
                            boot_dict['current_boot_variable']['sup_number']['sup-1']['kickstart_variable'] = m.groupdict()['kickstart_variable']
                        elif sup_number == 'sup-2':
                            boot_dict['current_boot_variable']['sup_number']['sup-2']['kickstart_variable'] = m.groupdict()['kickstart_variable']
                    else:
                        boot_dict['current_boot_variable']['kickstart_variable'] = m.groupdict()['kickstart_variable']
                elif boot_variable == 'next':
                    if sup_number:
                        if sup_number == 'sup-1':
                            boot_dict['next_reload_boot_variable']['sup_number']['sup-1']['kickstart_variable'] = m.groupdict()['kickstart_variable']
                        elif sup_number == 'sup-2':
                            boot_dict['next_reload_boot_variable']['sup_number']['sup-2']['kickstart_variable'] = m.groupdict()['kickstart_variable']
                    else:
                        boot_dict['next_reload_boot_variable']['kickstart_variable'] = m.groupdict()['kickstart_variable']
                continue

            p6 = re.compile(r'^\s*system variable = +(?P<system_variable>[a-zA-z0-9\:\-\.\/\s]+)$')
            m = p6.match(line)
            if m:
                if boot_variable == 'current':
                    if sup_number:
                        if sup_number == 'sup-1':
                            boot_dict['current_boot_variable']['sup_number']['sup-1']['system_variable'] = m.groupdict()['system_variable']
                        elif sup_number == 'sup-2':
                            boot_dict['current_boot_variable']['sup_number']['sup-2']['system_variable'] = m.groupdict()['system_variable']
                    else:
                        boot_dict['current_boot_variable']['system_variable'] = m.groupdict()['system_variable']
                elif boot_variable == 'next':
                    if sup_number:
                        if sup_number == 'sup-1':
                            boot_dict['next_reload_boot_variable']['sup_number']['sup-1']['system_variable'] = m.groupdict()['system_variable']
                        elif sup_number == 'sup-2':
                            boot_dict['next_reload_boot_variable']['sup_number']['sup-2']['system_variable'] = m.groupdict()['system_variable']
                    else:
                        boot_dict['next_reload_boot_variable']['system_variable'] = m.groupdict()['system_variable']
                continue


            # NXOS variable = bootflash:/ISSUCleanGolden.system.gbin
            p5_1 = re.compile(r'^\s*NXOS +variable += +(?P<image>[a-zA-z0-9\:\-\.\/\s]+)$')
            m = p5_1.match(line)
            if m:
                if boot_variable == 'current':
                    if sup_number:
                        if sup_number == 'sup-1':
                            boot_dict['current_boot_variable']['sup_number']['sup-1']['system_variable'] = m.groupdict()['image']
                        elif sup_number == 'sup-2':
                            boot_dict['current_boot_variable']['sup_number']['sup-2']['system_variable'] = m.groupdict()['image']
                    else:
                        boot_dict['current_boot_variable']['system_variable'] = m.groupdict()['image']
                elif boot_variable == 'next':
                    if sup_number:
                        if sup_number == 'sup-1':
                            boot_dict['next_reload_boot_variable']['sup_number']['sup-1']['system_variable'] = m.groupdict()['image']
                        elif sup_number == 'sup-2':
                            boot_dict['next_reload_boot_variable']['sup_number']['sup-2']['system_variable'] = m.groupdict()['image']
                    else:
                        boot_dict['next_reload_boot_variable']['system_variable'] = m.groupdict()['image']
                continue

            p7 = re.compile(r'^\s*Boot POAP +(?P<boot_poap>[a-zA-z]+)$')
            m = p7.match(line)
            if m:
                if boot_variable == 'current':
                    if sup_number:
                        if sup_number == 'sup-1':
                            boot_dict['current_boot_variable']['sup_number']['sup-1']['boot_poap'] = m.groupdict()['boot_poap']
                        elif sup_number == 'sup-2':
                            boot_dict['current_boot_variable']['sup_number']['sup-2']['boot_poap'] = m.groupdict()['boot_poap']
                    else:
                        boot_dict['current_boot_variable']['boot_poap'] = m.groupdict()['boot_poap']
                elif boot_variable == 'next':
                    if sup_number:
                        if sup_number == 'sup-1':
                            boot_dict['next_reload_boot_variable']['sup_number']['sup-1']['boot_poap'] = m.groupdict()['boot_poap']
                        elif sup_number == 'sup-2':
                            boot_dict['next_reload_boot_variable']['sup_number']['sup-2']['boot_poap'] = m.groupdict()['boot_poap']
                    else:
                        boot_dict['next_reload_boot_variable']['boot_poap'] = m.groupdict()['boot_poap']
                continue

        return boot_dict

class ShowModuleSchema(MetaParser):
    """Schema for show module"""
    schema = {'slot':
                  {'rp':
                    {Any():
                      {Any():
                        {'ports': str,
                         'slot': str,
                         Optional('model'): str,
                         'status': str,
                         Optional('software'): str,
                         Optional('hardware'): str,
                         Optional('mac_address'): str,
                         Optional('serial_number'): str,
                         Optional('online_diag_status'): str,
                         Optional('slot/world_wide_name'): str}
                      },
                    },
                   Optional('lc'):
                    {Optional(Any()):
                      {Optional(Any()):
                        {Optional('ports'): str,
                         'slot': str,
                         Optional('model'): str,
                         Optional('status'): str,
                         Optional('software'): str,
                         Optional('hardware'): str,
                         Optional('mac_address'): str,
                         Optional('serial_number'): str,
                         Optional('online_diag_status'): str,
                         Optional('slot/world_wide_name'): str}
                      },
                    }
                  },
              Optional('xbar'):
                  {Optional(Any()):
                      {Optional('ports'): str,
                       'slot': str,
                       Optional('module_type'): str,
                       Optional('model'): str,
                       Optional('status'): str,
                       Optional('software'): str,
                       Optional('hardware'): str,
                       Optional('mac_address'): str,
                       Optional('serial_number'): str}
                  },
              }

class ShowModule(ShowModuleSchema):
    """Parser for show module"""

    cli_command = 'show module'

    def cli(self,output=None):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        module_dict = {}
        table_header = None
        header_type = None
        rp_list = []
        map_dic = {}
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Mod.*$')
            m = p1.match(line)
            if m:
                table_header = 'slot'
                if 'slot' not in module_dict:
                    module_dict['slot'] = {}
                continue

            p2 = re.compile(r'^\s*Xbar.*$')
            m = p2.match(line)
            if m:
                table_header = 'xbar'
                if 'xbar' not in module_dict:
                    module_dict['xbar'] = {}
                continue

            p3 = re.compile(r'^\s*(?P<number>[0-9]+) +(?P<ports>[0-9]+) +(?P<module_type>[a-zA-Z0-9\/\-\s\+\(\)]+) +(?P<model>\S+) +(?P<status>[a-zA-Z\-\s]+) *\*?$')
            p3_1 = re.compile(r'^\s*(?P<number>[0-9]+) +(?P<ports>[0-9]+) +(?P<module_type>[a-zA-Z0-9\/\-\s\+]+) +(?P<status>[a-zA-Z\-\s]+) *\*?$')
            m = p3.match(line)
            m1 = p3_1.match(line)
            m = m if m else m1
            if m:
                header_number = m.groupdict()['number']
                module_type = m.groupdict()['module_type']
                if 'Supervisor' in module_type:
                    header_type = 'rp'
                    if header_type not in module_dict['slot']:
                        module_dict['slot'][header_type] = {}
                    rp_list.append(header_number)
                    rp_name =  m.groupdict()['module_type'].strip()
                    map_dic[header_number] = rp_name
                else:
                    header_type = 'lc'
                    if header_type not in module_dict['slot']:
                        module_dict['slot'][header_type] = {}
                    lc_name =  m.groupdict()['module_type'].strip()
                    map_dic[header_number] = lc_name
                if table_header == 'slot':
                    if header_number in rp_list:
                        if header_number not in module_dict['slot']['rp']:
                            module_dict['slot']['rp'][header_number] = {}
                        if rp_name not in module_dict['slot']['rp'][header_number]:
                            module_dict['slot']['rp'][header_number][rp_name] = {'slot': header_number}
                        module_dict['slot']['rp'][header_number][rp_name]['ports'] = m.groupdict()['ports'].strip()
                        if m.groupdict()['model']:
                            module_dict['slot']['rp'][header_number][rp_name]['model'] = m.groupdict()['model'].strip()
                        module_dict['slot']['rp'][header_number][rp_name]['status'] = m.groupdict()['status'].strip()
                    else:
                        if header_number not in module_dict['slot']['lc']:
                            module_dict['slot']['lc'][header_number] = {}
                        if lc_name not in module_dict['slot']['lc'][header_number]:
                            module_dict['slot']['lc'][header_number][lc_name] = {'slot': header_number}
                        module_dict['slot']['lc'][header_number][lc_name]['ports'] = m.groupdict()['ports'].strip()
                        if m.groupdict()['model']:
                            module_dict['slot']['lc'][header_number][lc_name]['model'] = m.groupdict()['model'].strip()
                        module_dict['slot']['lc'][header_number][lc_name]['status'] = m.groupdict()['status'].strip()
                elif table_header == 'xbar':
                    if header_number not in module_dict['xbar']:
                        module_dict['xbar'][header_number] = {'slot': header_number}
                    module_dict['xbar'][header_number]['ports'] = m.groupdict()['ports'].strip()
                    module_dict['xbar'][header_number]['module_type'] = m.groupdict()['module_type'].strip()
                    if m.groupdict()['model']:
                        module_dict['xbar'][header_number]['model'] = m.groupdict()['model'].strip()
                    module_dict['xbar'][header_number]['status'] = m.groupdict()['status'].strip()
                continue

            p4 = re.compile(r'^\s*(?P<number>[0-9]+) +(?P<software>[A-Z0-9\(\)\.]+) +(?P<hardware>[0-9\.]+)( +)?(?P<world_wide_name>[\w\-]+)?$')
            m = p4.match(line)
            if m:
                header_number = m.groupdict()['number']
                world_wide_name = m.groupdict()['world_wide_name']
                if table_header == 'slot':
                    if header_number in rp_list:
                        rp_name = map_dic[header_number]
                        module_dict['slot']['rp'][header_number][rp_name]['software'] = m.groupdict()['software'].strip()
                        module_dict['slot']['rp'][header_number][rp_name]['hardware'] = m.groupdict()['hardware'].strip()
                    else:
                        lc_name = map_dic[header_number]
                        module_dict['slot']['lc'][header_number][lc_name]['software'] = m.groupdict()['software'].strip()
                        module_dict['slot']['lc'][header_number][lc_name]['hardware'] = m.groupdict()['hardware'].strip()
                    if world_wide_name:
                        if header_number in rp_list:
                            module_dict['slot']['rp'][header_number][rp_name]['slot/world_wide_name'] = m.groupdict()['world_wide_name'].strip()
                        else:
                            module_dict['slot']['lc'][header_number][lc_name]['slot/world_wide_name'] = m.groupdict()['world_wide_name'].strip()
                elif table_header == 'xbar':
                    module_dict['xbar'][header_number]['software'] = m.groupdict()['software'].strip()
                    module_dict['xbar'][header_number]['hardware'] = m.groupdict()['hardware'].strip()
                    if world_wide_name:
                        module_dict['xbar'][header_number]['slot/world_wide_name'] = m.groupdict()['world_wide_name']
                continue

            p5 = re.compile(r'^\s*(?P<number>[0-9]+) +(?P<mac_address>[a-zA-Z0-9\.\-\s]+) +(?P<serial_number>[A-Z0-9]+)$')
            m = p5.match(line)
            if m:
                header_number = m.groupdict()['number']
                if table_header == 'slot':
                    if header_number in rp_list:
                        rp_name = map_dic[header_number]
                        module_dict['slot']['rp'][header_number][rp_name]['mac_address'] = m.groupdict()['mac_address'].strip()
                        module_dict['slot']['rp'][header_number][rp_name]['serial_number'] = m.groupdict()['serial_number'].strip()
                    else:
                        lc_name = map_dic[header_number]
                        module_dict['slot']['lc'][header_number][lc_name]['mac_address'] = m.groupdict()['mac_address'].strip()
                        module_dict['slot']['lc'][header_number][lc_name]['serial_number'] = m.groupdict()['serial_number'].strip()
                elif table_header == 'xbar':
                    module_dict['xbar'][header_number]['mac_address'] = m.groupdict()['mac_address'].strip()
                    module_dict['xbar'][header_number]['serial_number'] = m.groupdict()['serial_number'].strip()
                continue

            p6 = re.compile(r'^\s*(?P<number>[0-9]+) +(?P<online_diag_status>[a-zA-Z]+)$')
            m = p6.match(line)
            if m:
                header_number = m.groupdict()['number']
                if header_number in rp_list:
                    rp_name = map_dic[header_number]
                    module_dict['slot']['rp'][header_number][rp_name]['online_diag_status'] = m.groupdict()['online_diag_status'].strip()
                else:
                    lc_name = map_dic[header_number]
                    module_dict['slot']['lc'][header_number][lc_name]['online_diag_status'] = m.groupdict()['online_diag_status'].strip()
                continue

        # The case of n9k virtual device where no module was showing "supervisor" in the module type
        if 'slot' in module_dict:
            if 'rp' not in module_dict['slot'].keys():
                for key in module_dict['slot']['lc'].keys():
                    rp_key = key
                    break
                module_dict['slot']['rp'] = {}
                module_dict['slot']['rp'][rp_key] = module_dict['slot']['lc'][rp_key]
                del module_dict['slot']['lc'][rp_key]

        return module_dict

class DirSchema(MetaParser):
    """Schema for dir"""
    schema = {'disk_used_space': str,
              'disk_free_space': str,
              'disk_total_space': str,
              'dir': str,
              Optional('files'):
                  {Any():
                      {'size': str,
                       'date': str,
                       'time': str}
                  },
              }

class Dir(DirSchema):
    """Parser for dir"""

    cli_command = ['dir', 'dir {directory}']
    exclude = [
        'date',
        'size',
        'time',
        'disk_free_space',
        'disk_used_space']

    def cli(self, directory='', output=None):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        if output is None:
            if directory:
                out = self.device.execute(self.cli_command[1].format(directory=directory))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        dir_dict = {}
        file = None
        disk_type = None
        date = None
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*(?P<size>[0-9]+) +(?P<month>[a-zA-Z]+) +(?P<day>[0-9]+) +(?P<time>[0-9\:]+) +(?P<year>[0-9]+) +(?P<file>[a-zA-Z0-9\.\/\_\-\+]+)$')
            m = p1.match(line)
            if m:
                file = m.groupdict()['file']
                date = m.groupdict()['month'].strip() + ' ' + m.groupdict()['day'].strip() + ' ' + m.groupdict()['year'].strip()
                if 'files' not in dir_dict:
                    dir_dict['files'] = {}
                dir_dict['files'][file] = {}
                dir_dict['files'][file]['size'] = m.groupdict()['size']
                dir_dict['files'][file]['time'] = m.groupdict()['time']
                dir_dict['files'][file]['date'] = date
                continue

            p2 = re.compile(r'^\s*(?P<disk_space>[0-9]+) bytes +(?P<type>[a-z]+)$')
            m = p2.match(line)
            if m:
                disk_type = m.groupdict()['type']
                if disk_type == 'used':
                    dir_dict['disk_used_space'] = m.groupdict()['disk_space']
                if disk_type == 'free':
                    dir_dict['disk_free_space'] = m.groupdict()['disk_space']
                if disk_type == 'total':
                    dir_dict['disk_total_space'] = m.groupdict()['disk_space']
                continue

            p3 = re.compile(r'^\s*Usage +for +(?P<directory_name>[a-z\:]+).*$')
            m = p3.match(line)
            if m:
                dir_dict['dir'] = m.groupdict()['directory_name']
                continue

        return dir_dict

class ShowVdcDetailSchema(MetaParser):
    """Schema for show vdc detail"""
    schema = {'vdc':
                {Any():
                  {'name': str,
                  'state': str,
                  'mac_address': str,
                  'ha_policy': str,
                  'dual_sup_ha_policy': str,
                  'boot_order': str,
                  Optional('cpu_share'): str,
                  Optional('cpu_share_percentage'): str,
                  'create_time': str,
                  Optional('reload_count'): str,
                  Optional('uptime'): str,
                  'restart_count': str,
                  Optional('restart_time'): str,
                  'type': str,
                  'supported_linecards': str}
                },
            }

class ShowVdcDetail(ShowVdcDetailSchema):
    """Parser for show vdc detail"""

    cli_command = 'show vdc detail'
    exclude = [
        'uptime']

    def cli(self,output=None):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        vdc_dict = {}
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Switchwide +mode +is +.*$')
            m = p1.match(line)
            if m:
                continue

            p2 = re.compile(r'^\s*vdc +id: +(?P<id>[0-9]+)$')
            m = p2.match(line)
            if m:
                identity = m.groupdict()['id']
                if 'vdc' not in vdc_dict:
                    vdc_dict['vdc'] = {}
                if identity not in vdc_dict['vdc']:
                    vdc_dict['vdc'][identity] = {}
                continue

            p2 = re.compile(r'^\s*vdc +name: +(?P<name>\S+)$')
            m = p2.match(line)
            if m:
                vdc_dict['vdc'][identity]['name'] = m.groupdict()['name']
                continue

            p3 = re.compile(r'^\s*vdc +state: +(?P<state>[a-z]+)$')
            m = p3.match(line)
            if m:
                vdc_dict['vdc'][identity]['state'] = m.groupdict()['state']
                continue

            p4 = re.compile(r'^\s*vdc +mac +address: +(?P<mac>[a-z0-9\:]+)$')
            m = p4.match(line)
            if m:
                vdc_dict['vdc'][identity]['mac_address'] = m.groupdict()['mac']
                continue

            p5 = re.compile(r'^\s*vdc +ha +policy: +(?P<policy>[A-Z]+)$')
            m = p5.match(line)
            if m:
                vdc_dict['vdc'][identity]['ha_policy'] = m.groupdict()['policy']
                continue

            p6 = re.compile(r'^\s*vdc +dual-sup +ha +policy: +(?P<dual_policy>[A-Z]+)$')
            m = p6.match(line)
            if m:
                vdc_dict['vdc'][identity]['dual_sup_ha_policy'] = m.groupdict()['dual_policy']
                continue

            p7 = re.compile(r'^\s*vdc +boot +Order: +(?P<boot_order>[0-9]+)$')
            m = p7.match(line)
            if m:
                vdc_dict['vdc'][identity]['boot_order'] = m.groupdict()['boot_order']
                continue

            p8 = re.compile(r'^\s*CPU +Share: +(?P<cpu_share>[0-9]+)$')
            m = p8.match(line)
            if m:
                vdc_dict['vdc'][identity]['cpu_share'] = m.groupdict()['cpu_share']
                continue

            p9 = re.compile(r'^\s*CPU +Share +Percentage: +(?P<cpu_share_percentage>[0-9\%]+)$')
            m = p9.match(line)
            if m:
                vdc_dict['vdc'][identity]['cpu_share_percentage'] = m.groupdict()['cpu_share_percentage']
                continue

            p10 = re.compile(r'^\s*vdc +create +time: +(?P<vdc_create_time>[a-zA-Z0-9\:\s]+)$')
            m = p10.match(line)
            if m:
                vdc_dict['vdc'][identity]['create_time'] = m.groupdict()['vdc_create_time']
                continue

            p11 = re.compile(r'^\s*vdc +reload +count: +(?P<reload_count>[0-9]+)$')
            m = p11.match(line)
            if m:
                vdc_dict['vdc'][identity]['reload_count'] = m.groupdict()['reload_count']
                continue

            p12 = re.compile(r'^\s*vdc +uptime: +(?P<uptime>[a-z0-9\(\)\s\,]+)$')
            m = p12.match(line)
            if m:
                vdc_dict['vdc'][identity]['uptime'] = m.groupdict()['uptime']
                continue

            p13 = re.compile(r'^\s*vdc +restart +count: +(?P<count>[0-9]+)$')
            m = p13.match(line)
            if m:
                vdc_dict['vdc'][identity]['restart_count'] = m.groupdict()['count']
                continue

            p14 = re.compile(r'^\s*vdc +restart +time: +(?P<restart_time>[a-zA-Z0-9\:\s]+)$')
            m = p14.match(line)
            if m:
                vdc_dict['vdc'][identity]['restart_time'] = m.groupdict()['restart_time']
                continue

            p15 = re.compile(r'^\s*vdc +type: +(?P<type>[a-zA-Z]+)$')
            m = p15.match(line)
            if m:
                if 'vdc' not in vdc_dict:
                    vdc_dict['vdc'] = {}
                vdc_dict['vdc'][identity]['type'] = m.groupdict()['type']
                continue

            p16 = re.compile(r'^\s*vdc +supported +linecards: +(?P<linecards>[a-zA-Z0-9\s]+)$')
            m = p16.match(line)
            if m:
                if 'vdc' not in vdc_dict:
                    vdc_dict['vdc'] = {}
                vdc_dict['vdc'][identity]['supported_linecards'] = m.groupdict()['linecards']
                continue

        return vdc_dict

class ShowVdcCurrentSchema(MetaParser):
    '''Schema for:
        * show vdc current-vdc
    '''

    schema = {
        'current_vdc':
            {'id': str,
            'name': str,
            }
        }

class ShowVdcCurrent(ShowVdcCurrentSchema):
    '''Parser for:
        * show vdc current-vdc
    '''

    cli_command = 'show vdc current-vdc'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init
        ret_dict = {}

        # Current vdc is 1 - N95_1
        p1 = re.compile(r'^Current +vdc +is +(?P<id>\d+) *- *(?P<name>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # Current vdc is 1 - N95_1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                curr_vdc_dict = ret_dict.setdefault('current_vdc', {})
                curr_vdc_dict['id'] = group['id']
                curr_vdc_dict['name'] = group['name']
                continue

        return ret_dict

class ShowVdcMembershipStatusSchema(MetaParser):
    """Schema for show vdc membership status"""
    schema = {'virtual_device':
                {Any():
                    {'membership':
                        {Any():
                            {Any():
                                {'vd_ms_status': str,
                                 'vd_ms_type': str}
                            },
                        },
                    }
                },
            }

class ShowVdcMembershipStatus(ShowVdcMembershipStatusSchema):
    """Parser for show vdc membership status"""

    cli_command = 'show vdc membership status'

    def cli(self,output=None):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        member_status_vdc_dict = {}
        port_type = None
        port_number = None
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Flags : b - breakout port$')
            m = p1.match(line)
            if m:
                continue

            p2 = re.compile(r'^\s*vdc_id: +(?P<id>[0-9]+) +vdc_name: +(?P<name>\S+) +interfaces:$')
            m = p2.match(line)
            if m:
                identity = m.groupdict()['id']
                vdc_name = m.groupdict()['name']
                if 'virtual_device' not in member_status_vdc_dict:
                    member_status_vdc_dict['virtual_device'] = {}
                if identity not in member_status_vdc_dict['virtual_device']:
                    member_status_vdc_dict['virtual_device'][identity] = {}
                if 'membership' not in member_status_vdc_dict['virtual_device'][identity]:
                    member_status_vdc_dict['virtual_device'][identity]['membership'] = {}
                if vdc_name not in member_status_vdc_dict['virtual_device'][identity]['membership']:
                    member_status_vdc_dict['virtual_device'][identity]['membership'][vdc_name] = {}
                continue

            p3 = re.compile(r'^\s*Port +Status$')
            m = p3.match(line)
            if m:
                continue

            p4 = re.compile(r'^\s*(?P<port_type>[a-zA-Z]+)(?P<port_number>[0-9a-z/\\(\)]+) +(?P<status>[A-Z]+)$')
            m = p4.match(line)
            if m:
                port_type = m.groupdict()['port_type']
                port_number = m.groupdict()['port_number']
                port = port_type+port_number
                if port not in member_status_vdc_dict['virtual_device'][identity]['membership'][vdc_name]:
                    member_status_vdc_dict['virtual_device'][identity]['membership'][vdc_name][port] = {}
                status = m.groupdict()['status']
                if 'Eth' in port_type:
                    port_type = 'Ethernet'
                member_status_vdc_dict['virtual_device'][identity]['membership'][vdc_name][port]['vd_ms_status'] = status
                member_status_vdc_dict['virtual_device'][identity]['membership'][vdc_name][port]['vd_ms_type'] = port_type
                continue

        return member_status_vdc_dict


class ShowProcessesMemorySchema(MetaParser):
    """Schema for show processes memory
                  show processes memory | include <WORD>
    """

    schema = {
        'pid': {
            Any(): {
                'index': {
                    Any(): {
                        'pid': int,
                        'mem_alloc': int,
                        'mem_limit': int,
                        'mem_used': int,
                        'stack_base_ptr': str,
                        'process': str,
                    }
                }
            }
        },
        Optional('all_mem_alloc'): int,
    }


class ShowProcessesMemory(ShowProcessesMemorySchema):
    """Schema for show processes memory
                  show processes memory | include <WORD>
    """

    cli_command = [
        'show processes memory', 'show processes memory | include {include}'
    ]

    def cli(self, include=None, output=None):

        ret_dict = {}
        pid_index = {}

        if not output:
            if include:
                cmd = self.cli_command[1].format(include=include)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        #  8178  45387776  4294967295  1029939200  ffc31360/ffc311a0  bgp
        p1 = re.compile(
            r'^(\s+)?(?P<pid>\d+)\s+(?P<mem_alloc>\d+)\s+(?P<mem_limit>\d+)\s+(?P<mem_used>\d+)\s+(?P<stack_base_ptr>\S+)\s+(?P<process>\S+)'
        )

        # All processes: MemAlloc = 4693938176
        p2 = re.compile(
            r'^(\s+)?All\s+processes:\s+MemAlloc\s+=\s+(?P<all_mem_alloc>\d+)')

        for line in out.splitlines():
            line = line.strip()

            #  8178  45387776  4294967295  1029939200  ffc31360/ffc311a0  bgp
            m = p1.match(line)
            if m:
                group = m.groupdict()
                pid = int(group['pid'])
                index = pid_index.get(pid, 0) + 1
                pid_dict = ret_dict.setdefault('pid', {}). \
                    setdefault(pid, {}). \
                    setdefault('index', {}). \
                    setdefault(index, {})

                pid_index.update({pid: index})
                pid_dict.update({
                    k: int(v) if v.isdigit() else v
                    for k, v in group.items() if v is not None
                })
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'all_mem_alloc': int(group['all_mem_alloc'])})

        return ret_dict


class ShowProcessesCpuSchema(MetaParser):
    """Schema for show processes cpu
                  show processes cpu | include <WORD>
    """

    schema = {
        Optional('five_sec_cpu_interrupts'): int,
        Optional('five_sec_cpu_total'): int,
        Optional('one_min_cpu'): int,
        Optional('five_min_cpu'): int,
        Optional('user_percent'): float,
        Optional('kernel_percent'): float,
        Optional('idle_percent'): float,
        Optional('index'): {
            Any(): {
                'pid': int,
                'runtime_ms': int,
                'invoked': int,
                'usecs': int,
                'one_sec': float,
                'process': str,
            }
        }
    }


class ShowProcessesCpu(ShowProcessesCpuSchema):
    """Schema for show processes cpu
                  show processes cpu | include <WORD>
    """

    cli_command = [
        'show processes cpu', 'show processes cpu | include {include}'
    ]

    def cli(self, include='', output=None):

        if output is None:
            if include:
                out = self.device.execute(
                    self.cli_command[1].format(include=include))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # initial return dictionary
        ret_dict = {}
        index = 0

        #   958          810       728      0   2.95%  nginx
        p1 = re.compile(
            r'^(\s+)?(?P<pid>\d+)\s+(?P<runtime_ms>\d+)\s+(?P<invoked>\d+)\s+(?P<usecs>\d+)\s+(?P<one_sec>\d+\.\d+)%\s+(?P<process>\S+)'
        )

        # CPU util  :    2.07% user,   29.01% kernel,   68.91% idle
        p2 = re.compile(
            r'^(\s+)?CPU\s+util\s+:\s+(?P<user_percent>\d+\.\d+)%\s+user,\s+(?P<kernel_percent>\d+\.\d+)%\s+kernel,\s+(?P<idle_percent>\d+\.\d+)%\s+idle'
        )

        # CPU utilization for five seconds: 18%/7%; one minute: 20%; five minutes: 20%
        p3 = re.compile(
            r'^(\s+)?CPU\s+utilization\s+for\s+five\s+seconds:\s+(?P<five_sec_cpu_total>\d+)%/(?P<five_sec_cpu_interrupts>\d+)%;\s+one\s+minute:\s+(?P<one_min_cpu>\d+)%;\s+five\s+minutes:\s+(?P<five_min_cpu>\d+)%'
        )

        for line in out.splitlines():
            line = line.strip()

            #   958          810       728      0   2.95%  nginx
            m = p1.match(line)
            if m:
                group = m.groupdict()
                index += 1
                sort_dict = ret_dict.setdefault('index',
                                                {}).setdefault(index, {})
                sort_dict['process'] = group['process']
                sort_dict.update({
                    k: int(v)
                    for k, v in group.items()
                    if k in ['pid', 'runtime_ms', 'invoked', 'usecs']
                })
                sort_dict.update({
                    k: float(v)
                    for k, v in group.items() if k in ['one_sec']
                })
                continue

            # CPU util  :    2.07% user,   29.01% kernel,   68.91% idle
            m = p2.match(line)
            if m:
                ret_dict.update(
                    {k: float(v)
                     for k, v in m.groupdict().items()})
                continue

            # CPU utilization for five seconds: 18%/7%; one minute: 20%; five minutes: 20%
            m = p3.match(line)
            if m:
                ret_dict.update({k: int(v) for k, v in m.groupdict().items()})
                continue

        return ret_dict


class ShowCoresSchema(MetaParser):
    """Schema for show cores"""

    schema = {
        'date': {
            str: {
                'pid': {
                    int: {
                        'vdc': int,
                        'module': int,
                        'instance': int,
                        'process_name': str,
                    }
                }
            }
        }
    }


class ShowCores(ShowCoresSchema):
    """Schema for show cores"""

    cli_command = 'show cores'

    def cli(self, output=None):

        out = self.device.execute(
            self.cli_command) if output is None else output
        # initial return dictionary
        ret_dict = {}

        # 1    27      1         bgp              8083      2020-08-16 16:16:25
        p1 = re.compile(
            r'^(\s+)?(?P<vdc>\d+)\s+(?P<module>\d+)\s+(?P<instance>\d+)\s+(?P<process_name>\S+)\s+(?P<pid>\d+)\s+(?P<date>.*)'
        )

        for line in out.splitlines():
            line = line.strip()

            # 1    27      1         bgp              8083      2020-08-16 16:16:25
            m = p1.match(line)
            if m:
                group = m.groupdict()
                date = group.pop('date')
                pid = int(group.pop('pid'))

                pid_dict = ret_dict.setdefault('date', {}).setdefault(date, {}).setdefault('pid', {}).setdefault(pid, {})

                for key, value in group.items():
                  try:
                    value = int(value)
                  except:
                    pass

                  pid_dict.update({key: value})

        return ret_dict
