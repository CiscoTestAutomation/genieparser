"""show_install.py
   supported commands:
     *  show install summary
     *  show install rollback
     *  show install rollbackId
     *  show install state
     *  show install package SMU/subpkg
"""

# Python
import re
import random

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Schema,
                                                Any,
                                                Optional)

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowInstallSummarySchema(MetaParser):
    """Schema for show install summary"""
    schema = {
        'location': {
            Any(): {
                'pkg_state': {
                    Any(): {
                        'type': str,
                        'state': str,
                        'filename_version': str,
                    }
                },
                'auto_abort_timer': str,
                Optional('time_before_rollback'): str,
            },
        },
    }

class ShowInstallSummary(ShowInstallSummarySchema):
    """Parser for show install summary"""

    cli_command = 'show install summary'

    def cli(self, output=None):
        if output is None:
            # get output from device
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        ret_dict = {}
        index = 0
        # initial regexp pattern
        # [ R0 ] Installed Package(s) Information:
        p1 = re.compile(r'^\[ +(?P<location>[\S ]+)\] +Installed Package'
                        r'\(s\) +Information:$')
        # SMU   U    bootflash:utah.bm.smu.may15.bin
        # IMG   C    10.69.1.0.66982
        p2 = re.compile(r'^(?P<type>\S+) + (?P<state>\w) +(?P<filename_version>\S+)$')
        
        # Auto abort timer: active on install_activate, time before rollback - 01:49:42
        p3 = re.compile(r'^Auto +abort +timer: +(?P<auto_abort_timer>[\S ]+), +'
                        r'time +before +rollback +\- +(?P<time_before_rollback>\S+)$')

        # Auto abort timer: active on install_activate
        p4 = re.compile(r'^Auto +abort +timer: +(?P<auto_abort_timer>[\S ]+)$')

        for line in output.splitlines():
            line = line.strip()
            
            # [ R0 ] Installed Package(s) Information:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                location = group['location'].strip()
                location_dict = ret_dict.setdefault('location', {}). \
                    setdefault(location, {})
                continue

            # SMU   U    bootflash:utah.bm.smu.may15.bin
            # IMG   C    10.69.1.0.66982
            m = p2.match(line)
            if m:
                group = m.groupdict()
                index += 1
                install_dict = location_dict.setdefault('pkg_state', {}). \
                    setdefault(index, {})
                install_dict.update({'type': group['type']})
                install_dict.update({'state': group['state']})
                install_dict.update({'filename_version': group['filename_version']})
                continue
            
            # Auto abort timer: active on install_activate, time before rollback - 01:49:42
            m = p3.match(line)
            if m:
                group = m.groupdict()
                location_dict.update({'auto_abort_timer': group['auto_abort_timer']})
                time_before_rollback = group.get('time_before_rollback', None)
                if time_before_rollback:
                    location_dict.update({'time_before_rollback': time_before_rollback})
                continue
            
            # Auto abort timer: active on install_activate
            m = p4.match(line)
            if m:
                group = m.groupdict()
                location_dict.update({'auto_abort_timer': group['auto_abort_timer']})
                continue

        return ret_dict


class ShowInstallRollbackSchema(MetaParser):
    """Schema for show install rollback"""
    schema = {
        'install_rollback': {
            Any(): {
                    'id': int,
                    'label': str,
                    'description': str,
                },
            },
        }


class ShowInstallRollback(ShowInstallRollbackSchema):
    """Parser for show install rollback"""

    cli_command = 'show install rollback'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        ret_dict = {}
        index = 0
        # 5       No_Label                         No Description
        p1 = re.compile(r'^(?P<id>\d+)\s*(?P<label>(\S+ ){1,})\s{2,}(?P<description>.*)$')

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                index += 1
                group = m.groupdict()
                rollback_dict = ret_dict.setdefault('install_rollback', {}).setdefault(index, {})
                rollback_dict.update({'id': int(group['id'])})
                rollback_dict.update({'label': group['label'].strip()})
                rollback_dict.update({'description': group['description']})
                continue

        return ret_dict


class ShowInstallRollbackIdSchema(MetaParser):
    """Schema for show install rollback id <id>"""
    schema = {
        'id': {
            Any(): {
                'label': str,
                'description': str,
                'date': str,
                'time': str,
                'reload_required': str,
                Optional('type'): {
                    Any(): {
                        'state': str,
                        'filename_version': str
                    }
                }
            },
        },
    }


class ShowInstallRollbackId(ShowInstallRollbackIdSchema):
    """Parser for show install rollback id"""

    cli_command = 'show install rollback id {rollback_id}'

    def cli(self, rollback_id='', output=None):
        if output is None:
            # get output from device
            output = self.device.execute(self.cli_command.format(rollback_id=rollback_id))

        # initial return dictionary
        ret_dict = {}

        # Rollback id - 5 (Created on 2021-10-21 16:34:06.000000000 +0000)
        p1 = re.compile(r'Rollback\s*id\s*-\s*(?P<rollback_id>\d+)\s*\('
                        r'Created\s*on\s*(?P<date>\d*-\d*-\d*)\s*'
                        r'(?P<time>\d*:\d*:\d*.\d*)')

        # Label: No Label
        p2 = re.compile(r'Label:\s*(?P<label>.*)')

        # Description: No Description
        p3 = re.compile(r'Description:\s*(?P<description>.*)')

        # Reload required: NO
        p4 = re.compile(r'Reload\s*required:\s*(?P<reload_required>.*)')

        # IMG   C    17.08.01.0.148528 |
        # SMU   C    /flash1/user/cat9k_iosxe.2021-10-06_22.52_shidogra.53.CSCxx12353.SSA.smu.bin
        p5 = re.compile(r'^(?P<type>\S+) + (?P<state>\w) +(?P<filename_version>\S+)$')

        for line in output.splitlines():
            line = line.strip()
            
            m = p1.match(line)
            if m:
                group = m.groupdict()
                rollback_dict = ret_dict.setdefault('id', {}). \
                    setdefault(int(group['rollback_id']), {})
                rollback_dict.update({'date': group['date']})
                rollback_dict.update({'time': group['time']})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                rollback_dict.update({'label': group['label']})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                rollback_dict.update({'description': group['description']})
                continue
            
            m = p4.match(line)
            if m:
                group = m.groupdict()
                rollback_dict.update({'reload_required': group['reload_required']})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                install_dict = rollback_dict.setdefault('type', {}). \
                    setdefault(group['type'], {})
                install_dict.update({'state': group['state']})
                install_dict.update({'filename_version': group['filename_version']})
                continue

        return ret_dict


class ShowInstallStateSchema(MetaParser):
    """Schema for show install state"""
    schema = {
        'location': {
            Any(): {
                Optional('pkg_state'): {
                    Any(): {
                        'type': str,
                        'state': str,
                        'filename_version': str,
                    }
                },
                Optional('auto_abort_timer'): str,
            },
        },
    }


class ShowInstallState(ShowInstallStateSchema):
    """Parser for show install state"""

    cli_command = ['show install {state}']

    def cli(self, state="", output=None):
        if output is None:
            # get output from device
            output = self.device.execute(self.cli_command[0].format(state=state))

        # initial return dictionary
        ret_dict = {}
        index = 0
        # initial regexp pattern
        # [ R0 ] Installed Package(s) Information:
        p1 = re.compile(r'^\[ +(?P<location>[\S ]+)\]+\s+\w+ Package\(s\) +Information:$')
        # SMU   U    bootflash:utah.bm.smu.may15.bin
        # IMG   C    10.69.1.0.66982
        p2 = re.compile(r'^(?P<type>\S+) + (?P<state>\w) +(?P<filename_version>\S+)$')

        # Auto abort timer: active on install_activate
        p4 = re.compile(r'^Auto +abort +timer: +(?P<auto_abort_timer>[\S ]+)$')

        for line in output.splitlines():
            line = line.strip()

            # [ R0 ] Installed Package(s) Information:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                location = group['location'].strip()
                location_dict = ret_dict.setdefault('location', {}). \
                    setdefault(location, {})
                continue

            # SMU   U    bootflash:utah.bm.smu.may15.bin
            # IMG   C    10.69.1.0.66982
            m = p2.match(line)
            if m:
                group = m.groupdict()
                index += 1
                install_dict = location_dict.setdefault('pkg_state', {}). \
                    setdefault(index, {})
                install_dict.update({'type': group['type']})
                install_dict.update({'state': group['state']})
                install_dict.update({'filename_version': group['filename_version']})
                continue

            # Auto abort timer: active on install_activate
            m = p4.match(line)
            if m:
                group = m.groupdict()
                location_dict.update({'auto_abort_timer': group['auto_abort_timer']})
                continue

        return ret_dict


class ShowInstallPackageSMUSchema(MetaParser):
    """Schema for show install state"""
    schema = {
        'package': {
            'name': str,
            'version': str,
            'platform': str,
            'package_type': str,
            Optional('defect_id'): str,
            'package_state': str,
            Optional('supersedes_list'): str,
            Optional('smu_fixes_list'): str,
            'smu_id': int,
            'smu_type': str,
            'smu_compatible_with_version': str,
            Optional('smu_impact'): {
                'package': str,
                'size': int,
                'raw_SHA1_sum': str,
                'header_size': str,
                'package_type': int,
                'package_flags': int,
                'header_version': int,
                'internal_pkg_info': {
                    'name': str,
                    'build_time': str,
                    'release_date': str,
                    'boot_architecture': str,
                    'route_processor': str,
                    'user': str,
                    'package_name': str,
                    'build': str,
                    Optional('card_types'): str,
                },
            },
        },
    }


class ShowInstallPackageSMU(ShowInstallPackageSMUSchema):
    """Parser for show install package SMU/subpkg"""

    cli_command = 'show install package {file_path}'

    def cli(self, file_path="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(file_path=file_path))

        # initial return dictionary
        ret_dict = {}

        # Name: C9800-SW-iosxe-wlc.BLD_POLARIS_DEV_LATEST_20211206_041312_V17_8_0_26.SSA.bin
        p1 = re.compile(r'^Name: +(?P<file_name>.*bin$)')

        # Version: 17.08.01.0.150818.1638769329..Cupertino
        p2 = re.compile(r'Version: +(?P<version>.*$)')

        # Platform: CAT9K
        p3 = re.compile(r'Platform: +(?P<platform>.*$)')

        # Package Type: PKG
        p4 = re.compile(r'Package Type: +(?P<package_type>.*$)')

        # Defect ID: CSCvq24042
        p5 = re.compile(r'Defect ID: +(?P<defect_id>.*$)')

        # Package State: Not Installed
        p6 = re.compile(r'Package State: +(?P<package_state>.*$)')

        # Supersedes List:
        p7 = re.compile(r'Supersedes List: +(?P<supersedes_list>.*$)')

        # SMU Fixes List:
        p8 = re.compile(r'SMU Fixes List: +(?P<smu_fixes_list>.*$)')

        # SMU ID: 1000
        p9 = re.compile(r'SMU ID: +(?P<smu_id>.*$)')

        # SMU Type: reload
        p10 = re.compile(r'SMU Type: +(?P<smu_type>.*$)')

        # SMU Compatible with Version: 17.08.01.0.150818
        p11 = re.compile(r'SMU Compatible with Version: +(?P<smu_compatilble_version>.*$)')

        # SMUImpact:
        # Package: cat9k-wlc.BLD_POLARIS_DEV_LATEST_20211206_041312_V17_8_0_26.SSA.pkg
        p12 = re.compile(r'Package: +(?P<package>.*$)')

        # Size: 657171504
        p13 = re.compile(r'Size: +(?P<size>.*$)')

        # Raw disk-file SHA1sum:
        #  4e739aa1b7f4705bbce4ddddf4afab969ce0a7f0
        p14 = re.compile(r'^Raw disk-file SHA1sum:$')
        p30 = re.compile(r'(^\s*\w+$)')

        # Header size: 1072 bytes
        p15 = re.compile(r'Header size: +(?P<header_size>.*$)')

        # Package type: 0
        p16 = re.compile(r'Package type: +(?P<package_type>.*$)')

        # Package flags: 0
        p17 = re.compile(r'Package flags: +(?P<package_flags>.*$)')

        # Header version: 3
        p18 = re.compile(r'Header version: +(?P<header_version>.*$)')

        # Internal package information:
        # Name: rp_wlc
        p19 = re.compile(r'Name: +(?P<package_name>.*$)')

        # BuildTime: 2021-12-05_21.42
        p20 = re.compile(r'BuildTime: +(?P<build_time>.*$)')

        # ReleaseDate: 2021-12-06_04.53
        p21 = re.compile(r'ReleaseDate: +(?P<release_date>.*$)')

        # BootArchitecture: none
        p22 = re.compile(r'BootArchitecture: +(?P<boot_architecture>.*$)')

        # RouteProcessor: cat9k
        p23 = re.compile(r'RouteProcessor: +(?P<route_processor>.*$)')

        # Platform: CAT9K  ---> same regex ------ can we exclude?
        # p24 = re.compile(r'Platform: +(?P<platform>.*$)')

        # User: mcpre
        p25 = re.compile(r'User: +(?P<user>.*$)')

        # PackageName: wlc
        p26 = re.compile(r'PackageName: +(?P<package_name>.*$)')

        # Build: BLD_POLARIS_DEV_LATEST_20211206_041312_V17_8_0_26
        p27 = re.compile(r'Build: +(?P<build>.*$)')

        p28= re.compile(r'CardTypes: +(?P<card_types>.*$)')

        # k = out.splitlines()
        istr = iter(output.splitlines())
        for line in istr:
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                install_pkg = ret_dict.setdefault('package', {})
                install_pkg.update({'name': group['file_name']})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                install_pkg = ret_dict.setdefault('package', {})
                install_pkg.update({'version': group['version']})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                install_pkg = ret_dict.setdefault('package', {})
                install_pkg.update({'platform': group['platform']})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                install_pkg = ret_dict.setdefault('package', {})
                install_pkg.update({'package_type': group['package_type']})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                install_pkg = ret_dict.setdefault('package', {})
                install_pkg.update({'defect_id': group['defect_id']})
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                install_pkg = ret_dict.setdefault('package', {})
                install_pkg.update({'package_state': group['package_state']})
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                install_pkg = ret_dict.setdefault('package', {})
                install_pkg.update({'supersedes_list': group['supersedes_list']})
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                install_pkg = ret_dict.setdefault('package', {})
                install_pkg.update({'smu_fixes_list': group['smu_fixes_list']})
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                install_pkg = ret_dict.setdefault('package', {})
                install_pkg.update({'smu_id': int(group['smu_id'])})
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                install_pkg = ret_dict.setdefault('package', {})
                install_pkg.update({'smu_type': group['smu_type']})
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                install_pkg = ret_dict.setdefault('package', {})
                install_pkg.update({'smu_compatible_with_version': group['smu_compatilble_version']})
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                impact = install_pkg.setdefault('smu_impact', {})
                impact.update({'package': group['package']})
                continue

            m = p13.match(line)
            if m:
                group = m.groupdict()
                impact = install_pkg.setdefault('smu_impact', {})
                impact.update({'size': int(group['size'])})
                continue

            m = p14.match(line)
            if m:
                group = m.groupdict()
                impact = install_pkg.setdefault('smu_impact', {})
                next_line = next(istr)
                m1 = p30.match(next_line.strip())
                if m1:
                    impact.update({'raw_SHA1_sum': m1.group(1)})
                # impact.update({'raw_SHA1_sum': str(k[k.index(line)+1])})
                continue

            m = p15.match(line)
            if m:
                group = m.groupdict()
                impact = install_pkg.setdefault('smu_impact', {})
                impact.update({'header_size': group['header_size']})
                continue

            m = p16.match(line)
            if m:
                group = m.groupdict()
                impact = install_pkg.setdefault('smu_impact', {})
                impact.update({'package_type': int(group['package_type'])})
                continue

            m = p17.match(line)
            if m:
                group = m.groupdict()
                impact = install_pkg.setdefault('smu_impact', {})
                impact.update({'package_flags': int(group['package_flags'])})
                continue

            m = p18.match(line)
            if m:
                group = m.groupdict()
                impact = install_pkg.setdefault('smu_impact', {})
                impact.update({'header_version': int(group['header_version'])})
                continue

            m = p19.match(line)
            if m:
                group = m.groupdict()
                impact_info = impact.setdefault('internal_pkg_info', {})
                impact_info.update({'name': group['package_name']})
                continue

            m = p20.match(line)
            if m:
                group = m.groupdict()
                impact_info = impact.setdefault('internal_pkg_info', {})
                impact_info.update({'build_time': group['build_time']})
                continue

            m = p21.match(line)
            if m:
                group = m.groupdict()
                impact_info = impact.setdefault('internal_pkg_info', {})
                impact_info.update({'release_date': group['release_date']})
                continue

            m = p22.match(line)
            if m:
                group = m.groupdict()
                impact_info = impact.setdefault('internal_pkg_info', {})
                impact_info.update({'boot_architecture': group['boot_architecture']})
                continue

            m = p23.match(line)
            if m:
                group = m.groupdict()
                impact_info = impact.setdefault('internal_pkg_info', {})
                impact_info.update({'route_processor': group['route_processor']})
                continue

            m = p25.match(line)
            if m:
                group = m.groupdict()
                impact_info = impact.setdefault('internal_pkg_info', {})
                impact_info.update({'user': group['user']})
                continue

            m = p26.match(line)
            if m:
                group = m.groupdict()
                impact_info = impact.setdefault('internal_pkg_info', {})
                impact_info.update({'package_name': group['package_name']})
                continue

            m = p27.match(line)
            if m:
                group = m.groupdict()
                impact_info = impact.setdefault('internal_pkg_info', {})
                impact_info.update({'build': group['build']})
                continue

            m = p28.match(line)
            if m:
                group = m.groupdict()
                impact_info = impact.setdefault('internal_pkg_info', {})
                impact_info.update({'card_types': group['card_types']})
                continue

        return ret_dict
