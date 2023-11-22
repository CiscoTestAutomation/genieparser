""" show_install.py
NXOS parsers for the following show commands:
* 'show install all status'
"""

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ===================================
# Schema for 'show install all status'
# ===================================
class ShowInstallAllStatusSchema(MetaParser):
    """ Schema for:
       * 'show install all status'
    """

    schema = {
        'verifying_image_status': str,
        Optional('verifying_image_type'): str,
        Optional('upgrade_image'): str,
        Optional('preparing_nxos_version_info'): str,
        Optional('preparing_bios_version_info'): str,
        Optional('module_support_check'): str,
        Optional('notifying_services'): str,
        Optional('runtime_checks'): str,
        Optional('set_boot_variables'): str,
        Optional('configuration_copy'): str,
        Optional('compact_flash_and_upgrade'): str,
        Optional('compatibility_check'): {
            Any(): {
                'module': int,
                'bootable': str,
                'impact': str,
                'install_type': str,
                'reason': str

            },
        },
        Optional('image_upgrade_table'): {
            Any(): {
                'module': int,
                'image': str,
                'running_version': str,
                'new_version': str,
                'upg_required': str
            }
        },
        Optional('pre_upgrade_check_failed_code'): str,
        Optional('additional_info'): str
    }


# ====================================
# Parser for 'show install all status'
# ====================================
class ShowInstallAllStatus(ShowInstallAllStatusSchema):
    """Parser for show install all status """

    cli_command = [
        'show install all status'
    ]

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        parsed_dict = {}

        #  -- SUCCESS <Tue Sep 28 02:57:04>
        p0 = re.compile(r'^\s*--\s* (?P<status>[\s\w]+).*$')

        # Verifying image bootflash:/nxos.9.3.7.bin for boot variable "nxos".
        p1 = re.compile(r'^Verifying image bootflash.*$')

        # Verifying image type.
        p2 = re.compile(r'^Verifying image type.$')

        # Preparing "nxos" version info using image bootflash:/nxos.9.3.7.bin.
        p3 = re.compile(r'^Preparing "nxos" version info using image (?P<image>[^\n]*).*$')

        # Preparing "bios" version info using image bootflash:/nxos.9.3.7.bin.
        p4 = re.compile(r'^Preparing "bios" version info using image.*$')

        #  Performing module support checks.
        p5 = re.compile(r'^Performing module support checks.*$')

        #  Notifying services about system upgrade.
        p6 = re.compile(r'^Notifying services about system upgrade.*$')

        # Performing runtime checks.
        p7 = re.compile(r'^Performing runtime checks.*$')

        #  Setting boot variables.
        p8 = re.compile(r'^Setting boot variables.*$')

        #  Performing configuration copy.
        p9 = re.compile(r'^Performing configuration copy.*$')

        #  Refreshing compact flash and upgrading bios/loader/bootrom.
        p10 = re.compile(r'^Refreshing compact flash and upgrading bios.*$')

        # Module  bootable          Impact  Install-type  Reason
        # ------  --------  --------------  ------------  ------
        #      1       yes      disruptive          none  default upgrade is not hitless
        p11 = re.compile(
            r'^(?P<module>\d+)\s+(?P<bootable>[\w]+)\s+(?P<impact>[\w]+)\s+(?P<type>[\w-]+)\s+(?P<reason>[\w \-]+)')

        # Module       Image                  Running-Version(pri:alt)           New-Version  Upg-Required
        # ------  ----------  ----------------------------------------  --------------------  ------------
        # 1        nxos                                    9.3(7)                9.3(7)            no
        p12 = re.compile(
            r'^(?P<module>\d+)\s+(?P<image>\w+)\s+(?P<run_version>[\w.\(\/\):]+)\s+(?P<new_version>[\w.\('
            r'\/\):]+)\s+(?P<upg_req>\w+)')

        # Return code 0x437F0001 ((null)).
        # pre-upgrade check failed. Return code 0x437F0001 ((null))
        p13 = re.compile(r'^(?P<preup_fail>Return code [\w\s\(\)]+)')

        # Service "__inst_001__eigrp" in vdc 1: EIGRP  ISSU config check failed, ISSU may cause traffic disruption
        p14 = re.compile(r'^Service (?P<addinfo>(.)*)')

        out = iter(out.splitlines())
        for line in out:
            line = line.strip()

            # Verifying image bootflash:/nxos.9.3.7.bin for boot variable "nxos".
            m = p1.match(line)
            if m:
                # -- SUCCESS <Tue Sep 28 02:57:04>
                m1 = p0.match(next(out))
                parsed_dict['verifying_image_status'] = m1.groupdict()['status']
                continue

            # Verifying image type.
            m = p2.match(line)
            if m:
                # -- SUCCESS <Tue Sep 28 02:57:14>
                m2 = p0.match(next(out))
                parsed_dict['verifying_image_type'] = m2.groupdict()['status']
                continue

            # Preparing "nxos" version info using image bootflash:/nxos.9.3.7.bin.
            m = p3.match(line)
            if m:
                # -- SUCCESS <Tue Sep 28 02:57:16>
                m3 = p0.match(next(out))
                parsed_dict['upgrade_image'] = m.groupdict()['image']
                parsed_dict['preparing_nxos_version_info'] = m3.groupdict()['status']
                continue

            # Preparing "bios" version info using image bootflash:/nxos.9.3.7.bin.
            m = p4.match(line)
            if m:
                # -- SUCCESS <Tue Sep 28 02:57:19>
                m4 = p0.match(next(out))
                parsed_dict['preparing_bios_version_info'] = m4.groupdict()['status']
                continue

            # Performing module support checks.
            m = p5.match(line)
            if m:
                # -- SUCCESS <Tue Sep 28 02:58:21>
                m5 = p0.match(next(out))
                parsed_dict['module_support_check'] = m5.groupdict()['status']
                continue

            # Notifying services about system upgrade.
            m = p6.match(line)
            if m:
                # -- SUCCESS <Tue Sep 28 02:58:35>
                m6 = p0.match(next(out))
                parsed_dict['notifying_services'] = m6.groupdict()['status']
                continue

            # Performing runtime checks.
            m = p7.match(line)
            if m:
                # -- SUCCESS <Tue Sep 28 02:59:21>
                m7 = p0.match(next(out))
                parsed_dict['runtime_checks'] = m7.groupdict()['status']
                continue

            # Setting boot variables.
            m = p8.match(line)
            if m:
                # -- SUCCESS <Tue Sep 28 03:00:14>
                m8 = p0.match(next(out))
                parsed_dict['set_boot_variables'] = m8.groupdict()['status']
                continue

            # Performing configuration copy.
            m = p9.match(line)
            if m:
                # -- SUCCESS <Tue Sep 28 03:00:18>
                m9 = p0.match(next(out))
                parsed_dict['configuration_copy'] = m9.groupdict()['status']
                continue

            # Refreshing compact flash and upgrading bios/loader/bootrom.
            m = p10.match(line)
            if m:
                # Warning: please do not remove or power off the module at this time.
                m10 = p0.match(next(out))
                if m10:
                    parsed_dict['compact_flash_and_upgrade'] = m10.groupdict()['status']
                else:
                    # -- SUCCESS <Tue Sep 28 03:00:19>
                    m10 = p0.match(next(out))
                    parsed_dict['compact_flash_and_upgrade'] = m10.groupdict()['status']
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                compatibility_dict = parsed_dict.setdefault('compatibility_check', {})
                compatibility_index = len(compatibility_dict) + 1
                comp_dict = compatibility_dict.setdefault(compatibility_index, {})
                comp_dict['module'] = int(group['module'])
                comp_dict['bootable'] = group['bootable']
                comp_dict['impact'] = group['impact']
                comp_dict['install_type'] = group['type']
                comp_dict['reason'] = group['reason']
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                image_dict = parsed_dict.setdefault('image_upgrade_table', {})
                image_index = len(image_dict) + 1
                image_upgrade_dict = image_dict.setdefault(image_index, {})
                image_upgrade_dict['module'] = int(group['module'])
                image_upgrade_dict['image'] = group['image']
                image_upgrade_dict['running_version'] = group['run_version']
                image_upgrade_dict['new_version'] = group['new_version']
                image_upgrade_dict['upg_required'] = group['upg_req']
                continue

            # Return code 0x437F0001 ((null)).
            # pre-upgrade check failed. Return code 0x437F0001 ((null))
            m = p13.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['pre_upgrade_check_failed_code'] = group['preup_fail']
                continue

            # Service "__inst_001__eigrp" in vdc 1: EIGRP  ISSU config check failed, ISSU may cause traffic disruption
            m = p14.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['additional_info'] = group['addinfo']
                continue

        return parsed_dict
