'''show_romvar.py
IOSXE revision 1 parsers for the following commands:
    * show romvar
    * show romvar switch <switch_number>
'''

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional
from genie.libs.parser.iosxe.show_romvar import ShowRomvar as ShowRomvarDefault


class ShowRomvarSchema(MetaParser):
    """Schema for show romvar."""

    schema = {
        'rommon_variables': {
            'active': {
                Optional('ps1'): str,
                Optional('switch_number'): int,
                Optional('mcp_startup_traceflags'): str,
                Optional('license_active_level'): str,
                Optional('license_boot_level'): str,
                Optional('stack'): str,
                Optional('boot'): list,
                Optional('switch_priority'): int,
                Optional('chassis_ha_local_ip'): str,
                Optional('chassis_ha_remote_ip'): str,
                Optional('chassis_ha_local_mask'): str,
                Optional('ret_2_rts'): str,
                Optional('rmi_interface'): str,
                Optional('rmi_local_ip'): str,
                Optional('rmi_remote_ip'): str,
                Optional('bsi'): int,
                Optional('ret_2_rcalts'): str,
                Optional('random_num'): int,
                Optional('thrput'): str,
                Optional('config_file'): str,
                Optional('debug_conf'): str,
                Optional('bootldr'): str,
                Optional('crashinfo'): str,
                Optional('no_console'): int,
                Optional('boot_device_mode'): str,
                Optional('boardid'): int,
                Optional('mac_addr'): str,
                Optional('manual_boot'): str,
                Optional('model_num'): str,
                Optional('model_revision_num'): str,
                Optional('motherboard_assembly_num'): str,
                Optional('motherboard_revision_num'): str,
                Optional('motherboard_serial_num'): str,
                Optional('rommon_autoboot_attempt'): int,
                Optional('system_serial_num'): str,
                Optional('version_id'): str,
                Optional('device_managed_mode'): str,
                Optional('default_gateway'): str,
                Optional('ip_address'): str,
                Optional('tftp_server'): str,
                Optional('subnet_mask'): str,
                Optional('abnormal_reset_count'): int,
                Optional('boot_loader_upgrade_disable'): str,
                Optional('real_mgmte_dev'): str,
                Optional('sr_mgmt_vrf'): str,
                Optional('boot_param'): str,
                Optional('boot_param_bkp'): str,
                Optional('switch_ignore_startup_config'): int,
            },
            Optional('standby'): {
                Optional('ps1'): str,
                Optional('switch_number'): int,
                Optional('mcp_startup_traceflags'): str,
                Optional('license_active_level'): str,
                Optional('license_boot_level'): str,
                Optional('stack'): str,
                Optional('boot'): list,
                Optional('switch_priority'): int,
                Optional('chassis_ha_local_ip'): str,
                Optional('chassis_ha_remote_ip'): str,
                Optional('chassis_ha_local_mask'): str,
                Optional('ret_2_rts'): str,
                Optional('rmi_interface'): str,
                Optional('rmi_local_ip'): str,
                Optional('rmi_remote_ip'): str,
                Optional('bsi'): int,
                Optional('ret_2_rcalts'): str,
                Optional('random_num'): int,
                Optional('thrput'): str,
                Optional('config_file'): str,
                Optional('debug_conf'): str,
                Optional('bootldr'): str,
                Optional('crashinfo'): str,
                Optional('no_console'): int,
                Optional('boot_device_mode'): str,
                Optional('boardid'): int,
                Optional('mac_addr'): str,
                Optional('manual_boot'): str,
                Optional('model_num'): str,
                Optional('model_revision_num'): str,
                Optional('motherboard_assembly_num'): str,
                Optional('motherboard_revision_num'): str,
                Optional('motherboard_serial_num'): str,
                Optional('rommon_autoboot_attempt'): int,
                Optional('system_serial_num'): str,
                Optional('version_id'): str,
                Optional('device_managed_mode'): str,
                Optional('default_gateway'): str,
                Optional('ip_address'): str,
                Optional('tftp_server'): str,
                Optional('subnet_mask'): str,
                Optional('abnormal_reset_count'): int,
                Optional('boot_loader_upgrade_disable'): str,
                Optional('real_mgmte_dev'): str,
                Optional('sr_mgmt_vrf'): str,
                Optional('boot_param'): str,
                Optional('boot_param_bkp'): str,
                Optional('switch_ignore_startup_config'): int,
            },
        },
    }


class ShowRomvar(ShowRomvarSchema):
    """Parser for show romvar"""

    cli_command = ['show romvar',
                   'show romvar switch {switch_number}']

    def cli(self, switch_number=None, output=None):
        if output is None:
            if not switch_number:
                output = self.device.execute(self.cli_command[0])
            else:
                output = self.device.execute(
                    self.cli_command[1].format(
                        switch_number=switch_number,
                    )
                )

        ret_dict = {}
        parser = ShowRomvarDefault(device=self.device)

        for role, section_output in self._split_role_sections(output).items():
            parsed_section = parser.cli(output=section_output)
            rommon_variables = parsed_section.get('rommon_variables', {})
            if rommon_variables:
                ret_dict.setdefault(
                    'rommon_variables', {}
                )[role] = rommon_variables

        return ret_dict

    @staticmethod
    def _split_role_sections(output):
        sections = {}
        role = None

        # Active
        # ======
        role_header = re.compile(r'^(?P<role>Active|Standby)\s*$', re.I)

        # ROMMON variables for Active Switch
        # ROMMON variables for Standby
        romvar_role_header = re.compile(
            r'^ROMMON\s+variables\s+for\s+(?P<role>Active|Standby)\b.*$', re.I)

        for line in output.splitlines():
            stripped_line = line.strip()

            match = role_header.match(stripped_line)
            if match:
                role = match.group('role').lower()
                sections.setdefault(role, [])
                continue

            match = romvar_role_header.match(stripped_line)
            if match:
                role = match.group('role').lower()
                sections.setdefault(role, []).append('ROMMON variables:')
                continue

            if role:
                sections[role].append(line)

        if not sections:
            sections['active'] = output.splitlines()

        return {role: '\n'.join(lines) for role, lines in sections.items()}
