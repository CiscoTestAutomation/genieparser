"""show_platform.py

    IOS parsers for the following show commands for ASR901:

    * show inventory

"""
# python
import re

# genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
    Any, Optional

from genie.libs.parser.iosxe.show_platform import \
    ShowInventorySchema as ShowInventorySchema_iosxe


class ShowInventory(ShowInventorySchema_iosxe):
    """
    Parser for:
        * show inventory
    """
    cli_command = 'show inventory'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Init vars
        parsed_output = {}
        chassis_dir = {}
        rp_dir = {}
        other_dir = {}

        # NAME: "GigabitEthernet 0/10", DESCR: "1000BASE-BX10D SFP"
        p1 = re.compile(r'NAME\:\s*\"(?P<name>\S+\s+(?P<subslot>\d+\/\d+)?)\"\,\s*DESCR:\s*\"(?P<description>.+)\"')

        # NAME: "A901-12C-F-D Chassis", DESCR: "A901-12C-F-D Chassis"
        p1_1 = re.compile(r'NAME\:\s*\"(?P<name>.+(?P<subslot>\d+\/\d+)?)\"\,\s*DESCR:\s*\"(?P<description>.+)\"')

        # PID: A901-12C-F-D      , VID: V01 , SN: CAT9991U99B
        p2 = re.compile(r'PID:\s*(?P<pid>.+)\s*\,\s*VID:\s*(?P<vid>.*)\,\s*SN:\s*(?P<sn>.+)')

        for line in output.splitlines():
            line = line.strip()

            # NAME: "GigabitEthernet 0/10", DESCR: "1000BASE-BX10D SFP"
            m = p1.match(line)
            if m:
                group = m.groupdict()

                name = group['name']
                descr = group['description']
                subslot = group['subslot']
                continue

            # NAME: "A901-12C-F-D Chassis", DESCR: "A901-12C-F-D Chassis"
            m = p1_1.match(line)
            if m:
                group = m.groupdict()

                name = group['name']
                descr = group['description']
                subslot = ''
                continue

            # PID: A901-12C-F-D      , VID: V01 , SN: CAT9991U99B
            m = p2.match(line)
            if m:
                group = m.groupdict()

                pid = group['pid'].strip()
                vid = group.get('vid', '')
                sn = group['sn']

                if 'Chassis' in name:
                    main_dir = {}
                    main_dir = chassis_dir.setdefault('main', {}).setdefault(
                        'chassis', {}).setdefault('name', {})
                    main_dir['descr'] = descr
                    main_dir['name'] = name
                    main_dir['pid'] = pid
                    main_dir['sn'] = sn
                    main_dir['vid'] = vid
                    parsed_output.update(chassis_dir)

                    rp_slot_dir = {}
                    slot_dir = parsed_output.setdefault('slot', {})
                    rp_slot_dir = slot_dir.setdefault("0", {}).setdefault('rp', {}).setdefault(name, {})
                    rp_slot_dir['descr'] = descr
                    rp_slot_dir['name'] = name
                    rp_slot_dir['pid'] = pid
                    rp_slot_dir['sn'] = sn
                    rp_slot_dir['vid'] = vid

                elif 'GLC' in pid and subslot:
                    rp_subslot_dir = {}
                    rp_subslot_dir = rp_slot_dir.setdefault('subslot', {}).setdefault(subslot, {}).setdefault(name, {})
                    rp_subslot_dir['descr'] = descr
                    rp_subslot_dir['name'] = name
                    rp_subslot_dir['pid'] = pid
                    rp_subslot_dir['sn'] = sn
                    rp_subslot_dir['vid'] = vid

                else:
                    other_slot_dir = {}
                    other_slot_dir = slot_dir.setdefault(name, {}).setdefault('other', {}).setdefault(name, {})
                    other_slot_dir['descr'] = descr
                    other_slot_dir['name'] = name
                    other_slot_dir['pid'] = pid
                    other_slot_dir['sn'] = sn
                    other_slot_dir['vid'] = vid

        return parsed_output
