''' show_module.py
IOSXE parsers for the following show commands:

    * 'show module'
'''

import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use


log = logging.getLogger(__name__)


class ShowModuleSchema(MetaParser):
    """Schema for show module"""
    schema = {
        Optional('chassis_type'): str,
        Or('switch', 'module'): Or(
            {
                Any(): {
                    'module': {
                        int: {
                            'ports': int,
                            'card_type': str,
                            'model': str,
                            'serial': str,
                            Optional('mac_address'): str,
                            Optional('hw'): str,
                            Optional('fw'): str,
                            Optional('sw'): str,
                            Optional('status'): str,
                            Optional('redundancy_role'): str,
                            Optional('operating_redundancy_mode'): str,
                            Optional('configured_redundancy_mode'): str,
                        }
                    },
                }
            },
            {
                int: {
                    'ports': int,
                    'card_type': str,
                    'model': str,
                    'serial': str,
                    Optional('status'): str,
                    Optional('redundancy_role'): str,
                    Optional('operating_redundancy_mode'): str,
                    Optional('configured_redundancy_mode'): str,
                }
            },
        ),
        Optional('status'): {
            str: {
                'mac_address': str,
                'hw': str,
                'fw': str,
                'sw': str,
                'status': str,
            }
        },
        Optional('sup'): {
            Any(): {
                'operating_redundancy_mode': str,
                'configured_redundancy_mode': str,
            }
        },
        Optional('chassis'): {
            Any(): {
                'number_of_mac_address': int,
                'chassis_mac_address_lower_range': str,
                'chassis_mac_address_upper_range': str,
            }
        },
        Optional('number_of_mac_address'): int,
        Optional('chassis_mac_address_lower_range'): str,
        Optional('chassis_mac_address_upper_range'): str,
    }


class ShowModule(ShowModuleSchema):
    """Parser for show module"""

    cli_command = 'show module'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Chassis Type: C9610R
        p0 = re.compile(r'^Chassis Type: +(?P<chassis_type>\S+)$')

        # Switch Number 1
        p1 = re.compile(r'^Switch Number +(?P<switch_number>\d+)$')

        # Mod Ports Card Type                                   Model          Serial No.
        # ---+-----+--------------------------------------+--------------+--------------
        # 1   48   48-Port 10GE / 25GE                         C9600-LC-48YL    FDO24170FSK
        # 1   32   30x40/100GE + 2x40/100/400GE                C9600X-LC-32CD   FDO281001K7
        # 3   0    Blank Module                                C9610-BLANK      N/A
        p2 = re.compile(r'^(?P<mod>\d+)\s+(?P<ports>\d+)\s+(?P<card_type>.+?)\s{2,}(?P<model>\S+)\s+(?P<serial>\S+)$')

        # Mod MAC addresses                    Hw   Fw           Sw                 Status
        # ---+--------------------------------+----+------------+------------------+--------
        # 1   AC4A.67AA.CE80 to AC4A.67AA.CEFF 2.0  17.7.1r[FC3]  17.03.01           ok
        # 1   B08D.57C1.2B80 to B08D.57C1.2B9F 1.0  17.18.1r      BLD_POLARIS_DEV_LA ok
        p3 = re.compile(r'^(?P<mod>\d+)\s+(?P<mac_address>[\w\.]+ to [\w\.]+)\s+(?P<hw>[\d\.]+)\s+(?P<fw>\S+)\s+(?P<sw>\S+)\s+(?P<status>\S+)$')

        # Mod Redundancy Role     Operating Redundancy Mode Configured Redundancy Mode
        # ---+-------------------+-------------------------+---------------------------
        # 3   Standby             sso                       sso
        # 4   Active              sso                       sso
        p4 = re.compile(r'^(?P<mod>\d+)\s+(?P<redundancy_role>\S+)\s+(?P<operating_redundancy_mode>\S+)\s+(?P<configured_redundancy_mode>\S+)$')

        # Chassis 1 MAC address range: 64 addresses from 8c44.a5a8.b800 to 8c44.a5a8.b83f
        p5 = re.compile(
            r'^Chassis (?P<chassis_num>\d+) MAC address range: '
            r'(?P<number_of_mac_address>\d+) addresses from '
            r'(?P<chassis_mac_address_lower_range>\S+) to '
            r'(?P<chassis_mac_address_upper_range>\S+)$'
        )

        # Chassis MAC address range: 64 addresses from 6cb2.ae4a.5540 to 6cb2.ae4a.557f
        p6 = re.compile(
            r'^Chassis MAC address range: '
            r'(?P<number_of_mac_address>\d+) addresses from '
            r'(?P<chassis_mac_address_lower_range>\S+) to '
            r'(?P<chassis_mac_address_upper_range>\S+)$'
        )

        ret_dict = {}
        current_switch = None  

        for line in out.splitlines():
            line = line.strip()

            # Chassis Type: C9610R
            m = p0.match(line)
            if m:
                group = m.groupdict()
                ret_dict['chassis_type'] = group['chassis_type']
                continue

            # Switch Number 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                current_switch = group['switch_number']
                ret_dict.setdefault('switch', {}).setdefault(current_switch, {})
                continue

            # Mod Ports Card Type                                   Model          Serial No.
            # ---+-----+--------------------------------------+--------------+--------------
            # 1   48   48-Port 10GE / 25GE                         C9600-LC-48YL    FDO24170FSK
            m = p2.match(line)
            if m:
                group = m.groupdict()
                mod = int(group.pop('mod'))
                module_dict = ret_dict.setdefault('module', {}) if current_switch is None else \
                    ret_dict.setdefault('switch', {}).setdefault(current_switch, {}).setdefault('module', {})
                mod_entry = module_dict.setdefault(mod, {})
                mod_entry.update({k: v.strip() for k, v in group.items()})
                mod_entry['ports'] = int(group['ports'])
                continue
            
            # Mod MAC addresses                    Hw   Fw           Sw                 Status
            # ---+--------------------------------+----+------------+------------------+--------
            # 1   AC4A.67AA.CE80 to AC4A.67AA.CEFF 2.0  17.7.1r[FC3]  17.03.01           ok  
            m = p3.match(line)
            if m:
                group = m.groupdict()
                mod = int(group['mod'])
                if current_switch is not None:
                    some_dict = ret_dict.setdefault('switch', {}).setdefault(current_switch, {}) \
                        .setdefault('module', {}).setdefault(mod, {})
                else:
                    ret_dict.setdefault('module', {}).setdefault(mod, {})['status'] = group['status'].strip()
                    some_dict = ret_dict.setdefault('status', {}).setdefault(str(mod), {})

                some_dict['mac_address'] = group['mac_address'].strip()
                some_dict['hw'] = group['hw'].strip()
                some_dict['fw'] = group['fw'].strip()
                some_dict['sw'] = group['sw'].strip()
                some_dict['status'] = group['status'].strip()
                continue
            
            # Mod Redundancy Role     Operating Redundancy Mode Configured Redundancy Mode
            # 3   Standby             sso                       sso     
            m = p4.match(line)
            if m:
                group = m.groupdict()
                mod = int(group['mod'])
                redundancy_role = group['redundancy_role'].lower()
                redundancy_role_original = group['redundancy_role']
                operating_redundancy_mode = group['operating_redundancy_mode'].lower()
                configured_redundancy_mode = group['configured_redundancy_mode'].lower()
                if current_switch is not None:
                    mod_entry = ret_dict.setdefault('switch', {}).setdefault(current_switch, {}) \
                        .setdefault('module', {}).setdefault(mod, {})
                    mod_entry['redundancy_role'] = redundancy_role
                    mod_entry['operating_redundancy_mode'] = operating_redundancy_mode
                    mod_entry['configured_redundancy_mode'] = configured_redundancy_mode
                else:
                    mod_entry = ret_dict.setdefault('module', {}).setdefault(mod, {})
                    mod_entry['redundancy_role'] = redundancy_role
                    mod_entry['operating_redundancy_mode'] = operating_redundancy_mode
                    mod_entry['configured_redundancy_mode'] = configured_redundancy_mode
                    sup_dict = ret_dict.setdefault('sup', {}).setdefault(redundancy_role_original, {})
                    sup_dict['operating_redundancy_mode'] = operating_redundancy_mode
                    sup_dict['configured_redundancy_mode'] = configured_redundancy_mode
                continue

            # Chassis 1 MAC address range: 64 addresses from 6cb2.ae4a.5540 to 6cb2.ae4a.557f
            m = p5.match(line)
            if m:
                group = m.groupdict()
                chassis_dict = ret_dict.setdefault('chassis', {}).setdefault(group['chassis_num'], {})
                chassis_dict['number_of_mac_address'] = int(group['number_of_mac_address'])
                chassis_dict['chassis_mac_address_lower_range'] = group['chassis_mac_address_lower_range'].lower()
                chassis_dict['chassis_mac_address_upper_range'] = group['chassis_mac_address_upper_range'].lower()
                continue

            # Chassis MAC address range: 64 addresses from 6cb2.ae4a.5540 to 6cb2.ae4a.557f
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict['number_of_mac_address'] = int(group['number_of_mac_address'])
                ret_dict['chassis_mac_address_lower_range'] = group['chassis_mac_address_lower_range'].lower()
                ret_dict['chassis_mac_address_upper_range'] = group['chassis_mac_address_upper_range'].lower()
                continue

        return ret_dict
