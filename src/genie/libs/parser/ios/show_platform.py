"""show_platform.py

    IOS parsers for the following show commands:

    * show version
    * dir
    * show redundancy
    * show inventory
    * show bootvar
    * show processes cpu sorted
    * show processes cpu sorted <1min|5min|5sec>
    * show processes cpu sorted | include <WORD>
    * show processes cpu sorted <1min|5min|5sec> | include <WORD>
"""
# python
import re

# genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, Optional

# import iosxe parser
from genie.libs.parser.iosxe.show_platform import \
        ShowVersion as ShowVersion_iosxe, \
        Dir as Dir_iosxe, \
        ShowInventorySchema as ShowInventorySchema_iosxe, \
        ShowRedundancy as ShowRedundancy_iosxe, \
        ShowProcessesCpuSorted as ShowProcessesCpuSorted_iosxe


class ShowVersion(ShowVersion_iosxe):
    """Parser for show version
    """
    pass


class Dir(Dir_iosxe):
    """Parser for dir
    """
    pass


class ShowRedundancyIosSchema(MetaParser):
    """Schema for show redundancy """
    schema = {
                'red_sys_info': {
                    'available_system_uptime': str,
                    'switchovers_system_experienced': str,
                    'standby_failures': str,
                    'last_switchover_reason': str,
                    'hw_mode': str,
                    Optional('conf_red_mode'): str,
                    Optional('oper_red_mode'): str,
                    'maint_mode': str,
                    'communications': str,
                    Optional('communications_reason'): str,
                    },
                'slot': {
                    Any(): {
                        'curr_sw_state': str,
                        'uptime_in_curr_state': str,
                        'image_ver': str,
                        Optional('boot'): str,
                        Optional('config_file'): str,
                        Optional('bootldr'): str,
                        'config_register': str,
                    }
                }
            }


class ShowRedundancy(ShowRedundancyIosSchema, ShowRedundancy_iosxe):
    """Parser for show redundancy
    """
    pass


class ShowInventory(ShowInventorySchema_iosxe):
    """Parser for show Inventory
    """
    def cli(self):
        cmd = 'show inventory'.format()
        out = self.device.execute(cmd)
        name = descr = slot = subslot = pid = ''
        inventory_dict = {}

        # NAME: "CISCO2921/K9 chassis", DESCR: "CISCO2921/K9 chassis"
        # NAME: "IOSv", DESCR: "IOSv chassis, Hw Serial#: 1234567890, Hw Revision: 1.0"
        p1 = re.compile(r'^NAME\:\s+\"(?P<name>.*)\",\s+DESCR\:\s+\"(?P<descr>.*)\"')
        
        # IOSv
        p1_1 = re.compile(r'\w+')

        # "Switch 1"
        p1_2 = re.compile(r'\s*\S+[ t](?P<slot>[a-zA-Z]*\d+)[ /]*')

        # SPA subslot 0/0
        p1_3 = re.compile(r'SPA subslot (?P<slot>\d+)/(?P<subslot>\d+)')

        # subslot 0/0
        p1_4 = re.compile(r'\s*\S+ *\d+[ /]*(?P<subslot>\d+.*)$')

        # PID: IOSv              , VID: 1.0, SN: 9KLUMCXRGCYY7MZLRU14R
        p2 = re.compile(r'^PID: +(?P<pid>\S+) *, +VID: +(?P<vid>\S+) *, +SN: +(?P<sn>.*)$')

        for line in out.splitlines():
            line = line.strip()

            #  NAME: "IOSv", DESCR: "IOSv chassis, Hw Serial#: 1234567890, Hw Revision: 1.0"
            m = p1.match(line)
            if m:
                name = m.groupdict()['name']
                descr = m.groupdict()['descr']

                m = p1_1.match(name)
                if m:
                    slot = '1'
                    slot_dict = inventory_dict.setdefault('slot', {}).setdefault(slot, {})

                m = p1_2.match(name)
                if m:
                    slot = m.groupdict()['slot']
                    slot_dict = inventory_dict.setdefault('slot', {}).setdefault(slot, {})

                m = p1_3.match(name)
                if m:
                    slot = m.groupdict()['slot']
                    subslot = m.groupdict()['subslot']
                    slot_dict = inventory_dict.setdefault('slot', {}).setdefault(slot, {})

                if 'Power Supply Module' in name:
                    slot = name.replace('Power Supply Module ', 'P')
                    slot_dict = inventory_dict.setdefault('slot', {}).setdefault(slot, {})

                m = p1_4.match(name)
                if m:
                    subslot = m.groupdict()['subslot']
                continue

            # PID: IOSv              , VID: 1.0, SN: 9KLUMCXRGCYY7MZLRU14R
            m = p2.match(line)
            if m:
                if 'WS-C' in pid:
                    old_pid = pid
                pid = m.groupdict()['pid']
                vid = m.groupdict()['vid']
                sn = m.groupdict()['sn']
                if name:
                    if pid and ('Chassis' in name):
                        chassis_dict = inventory_dict.setdefault('main', {})\
                            .setdefault('chassis', {}).setdefault(pid, {})
                        chassis_dict.update({'name': name, 'descr': descr,
                                            'pid': pid, 'vid': vid, 'sn': sn})
                    if slot:
                        if 'WS-C' in pid or 'IOSv' in pid:
                            rp_dict = slot_dict.setdefault('rp', {}).setdefault(pid, {})
                            rp_dict.update({'name': name, 'descr': descr,
                                                'pid': pid, 'vid': vid, 'sn': sn})
                        else:
                            other_dict = slot_dict.setdefault('other', {}).setdefault(pid, {})
                            other_dict.update({'name': name, 'descr': descr,
                                                'pid': pid, 'vid': vid, 'sn': sn})
                name = descr = slot = subslot = ''
                continue

        return inventory_dict


class ShowBootvarSchema(MetaParser):
    """Schema for show bootvar"""

    schema = {Optional('current_boot_variable'): str,
              Optional('next_reload_boot_variable'): str,
              Optional('config_file'): str,
              Optional('bootldr'): str,
              Optional('active'): {
                  'configuration_register': str,
                  Optional('boot_variable'): str,
              },
              Optional('standby'): {              
                  'configuration_register': str,
                  Optional('boot_variable'): str,
              },
    }


class ShowBootvar(ShowBootvarSchema):
    """Parser for show boot"""

    def cli(self):
        cmd = 'show boot'.format()
        out = self.device.execute(cmd)
        boot_dict = {}
        boot_variable = None

        # BOOT variable = bootflash:/asr1000rpx.bin,12;
        # BOOT variable = flash:cat3k_caa-universalk9.BLD_POLARIS_DEV_LATEST_20150907_031219.bin;flash:cat3k_caa-universalk9.BLD_POLARIS_DEV_LATEST_20150828_174328.SSA.bin;flash:ISSUCleanGolden;
        p1 = re.compile(r'^BOOT +variable +=( *(?P<var>\S+);)?$')

        # Standby BOOT variable = bootflash:/asr1000rpx.bin,12;
        p2 = re.compile(r'^Standby +BOOT +variable +=( *(?P<var>\S+);)?$')

        # Configuration register is 0x2002
        p3 = re.compile(r'^Configuration +register +is +(?P<var>\w+)$')

        # Standby Configuration register is 0x2002
        p4 = re.compile(r'^Standby +Configuration +register +is +(?P<var>\w+)$')

        # CONFIG_FILE variable = 
        p5 = re.compile(r'^CONFIG_FILE +variable += +(?P<var>\S+)$')

        # BOOTLDR variable = 
        p6 = re.compile(r'^BOOTLDR +variable += +(?P<var>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # BOOT variable = disk0:s72033-adventerprisek9-mz.122-33.SRE0a-ssr-nxos-76k-1,12;            
            m = p1.match(line)
            if m:
                boot = m.groupdict()['var']
                if boot:
                    boot_dict['next_reload_boot_variable'] = boot
                    boot_dict.setdefault('active', {})['boot_variable'] = boot
                continue

            # Standby BOOT variable = bootflash:/asr1000rpx.bin,12;
            m = p2.match(line)
            if m:
                boot = m.groupdict()['var']
                if boot:
                    boot_dict.setdefault('standby', {})['boot_variable'] = boot
                continue

            # Configuration register is 0x2002
            m = p3.match(line)
            if m:
                boot_dict.setdefault('active', {})['configuration_register'] = m.groupdict()['var']
                continue

            # Standby Configuration register is 0x2002
            m = p4.match(line)
            if m:
                boot_dict.setdefault('standby', {})['configuration_register'] = m.groupdict()['var']
                continue

            # CONFIG_FILE variable = 
            m = p5.match(line)
            if m:
                if m.groupdict()['var']:
                    boot_dict.setdefault('active', {})['config_file'] = m.groupdict()['var']
                continue

            # BOOTLDR variable = 
            m = p6.match(line)
            if m:
                if m.groupdict()['var']:
                    boot_dict.setdefault('standby', {})['bootldr'] = m.groupdict()['var']
                continue
        return boot_dict


class ShowProcessesCpuSorted(ShowProcessesCpuSorted_iosxe):
    """Parser for show processes cpu sorted
                  show processes cpu sorted <1min|5min|5sec>
                  show processes cpu sorted | include <WORD>
                  show processes cpu sorted <1min|5min|5sec> | include <WORD>
    """
    pass
