"""show_version.py

SONiC parsers for show commands:
    * 'show version'
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowVersionSchema(MetaParser):
    """
    Schema for
        * show version
    """
    schema = {
        'sonic_software_version': str,
        Optional('sonic_os_version'): int,
        'distribution': str,
        'kernel': str,
        'build_commit': str,
        'build_date': str,
        'built_by': str,
        'platform': str,
        'hardware_sku': str,
        'asic': str,
        'asic_count': int,
        'serial_number': str,
        'model_number': str,
        'hardware_revision': str,
        'uptime': str,
        'users': int,
        'load_average': list,
        'date': str,
        'docker_images': {
            'image_id': {
                Any(): {
                    'repository': str,
                    'tag': str,
                    'size': str
                }
            }
        }
    }


class ShowVersion(ShowVersionSchema):
    """
    Parser for
        * show version
    """
    cli_command = "show version"

    def cli(self, output: str = None) -> dict:
        if not output:
            output = self.device.execute(self.cli_command)

        # SONiC Software Version: SONiC.azure_cisco_202205.5324-dirty-20230707.044127
        p0 = re.compile(r'^SONiC Software Version: (?P<sw_version>.*)$')

        # SONiC OS Version: 11
        p1 = re.compile(r'^SONiC OS Version: (?P<os_version>\d+)$')

        # Distribution: Debian 11.7
        p2 = re.compile(r'^Distribution: (?P<distribution>.*)$')

        # Kernel: 5.10.0-18-2-amd64
        p3 = re.compile(r'^Kernel: (?P<kernel>.*)$')

        # Build commit: a2dedc96c
        p4 = re.compile(r'^Build commit: (?P<build_commit>\w+)$')

        # Build date: Fri Jul  7 14:22:57 UTC 2023
        p5 = re.compile(r'^Build date: (?P<build_date>.*)$')

        # Built by: sonicci@sonic-ci-7-lnx
        p6 = re.compile(r'^Built by: (?P<built_by>.*)$')

        # Platform: x86_64-8201_32fh_o-r0
        p7 = re.compile(r'^Platform: (?P<platform>.*)$')

        # HwSKU: 32x400Gb
        p8 = re.compile(r'^HwSKU: (?P<hwsku>[\w-]+)$')

        # ASIC: cisco-8000
        p9 = re.compile(r'^ASIC: (?P<asic>[\w-]+)$')

        # ASIC Count: 1
        p10 = re.compile(r'^ASIC Count: (?P<asic_count>\d+)$')

        # Serial Number: FOC2217FQXV
        p11 = re.compile(r'^Serial Number: (?P<serial_number>\w+)$')

        # Model Number: 8201-32FH-O
        p12 = re.compile(r'^Model Number: (?P<model_number>[\w-]+)$')

        # Hardware Revision: 0.33
        p13 = re.compile(r'^Hardware (Revision|Rev): (?P<hw_revision>[\w.]+)$')

        # Uptime: 17:07:15 up 15 min,  1 user,  load average: 0.82, 1.00, 0.90
        p14 = re.compile(r'^Uptime: (?P<uptime>.+), +(?P<users>\d+) user, +load average: (?P<load_average>.+)$')

        # Date: Thu 02 Nov 2023 17:07:15
        p15 = re.compile(r'^Date: (?P<date>.+)$')

        # REPOSITORY     TAG                                                      IMAGE ID           SIZE
        # docker-macsec  latest                                                   44ef5532977a       332MB
        # docker-snmp    azure_cisco_tortuga_202305.10234-dirty-20240326.030556   fa3b3f6e4927       359MB
        p16 = re.compile(r'^(?P<repository>[\w-]+) +(?P<tag>[\w/_/-/.]+) +(?P<image_id>\w+) +(?P<size>\w+)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # SONiC Software Version: SONiC.azure_cisco_202205.5324-dirty-20230707.044127
            m = p0.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('sonic_software_version', group['sw_version'])
                continue

            # SONiC OS Version: 11
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('sonic_os_version', int(group['os_version']))
                continue

            # Distribution: Debian 11.7
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('distribution', group['distribution'])
                continue

            # Kernel: 5.10.0-18-2-amd64
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('kernel', group['kernel'])
                continue

            # Build commit: a2dedc96c
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('build_commit', group['build_commit'])
                continue

            # Build date: Fri Jul  7 14:22:57 UTC 2023
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('build_date', group['build_date'])
                continue

            # Built by: sonicci@sonic-ci-7-lnx
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('built_by', group['built_by'])
                continue

            # Platform: x86_64-8201_32fh_o-r0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('platform', group['platform'])
                continue

            # HwSKU: 32x400Gb
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('hardware_sku', group['hwsku'])
                continue

            # ASIC: cisco-8000
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('asic', group['asic'])
                continue

            # ASIC Count: 1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('asic_count', int(group['asic_count']))
                continue

            # Serial Number: FOC2217FQXV
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('serial_number', group['serial_number'])
                continue

            # Model Number: 8201-32FH-O
            m = p12.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('model_number', group['model_number'])
                continue

            # Hardware Revision: 0.33
            m = p13.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('hardware_revision', group['hw_revision'])
                continue

            # Uptime: 17:07:15 up 15 min,  1 user,  load average: 0.82, 1.00, 0.90
            m = p14.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('uptime', group['uptime'])
                ret_dict.setdefault('users', int(group['users']))
                ret_dict.setdefault('load_average', [float(i) for i in group['load_average'].split(', ')])
                continue

            # Date: Thu 02 Nov 2023 17:07:15
            m = p15.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('date', group['date'])
                continue

            # REPOSITORY                    TAG                  IMAGE ID           SIZE
            # docker-macsec                 latest               44ef5532977a       332MB
            m = p16.match(line)
            if m:
                group = m.groupdict()
                if 'docker_images' not in ret_dict:
                    docker_image = ret_dict.setdefault('docker_images',{})
                img_id = docker_image.setdefault('image_id',{}).setdefault(group['image_id'], {})
                img_id.setdefault('repository', group['repository'])
                img_id.setdefault('tag', group['tag'])
                img_id.setdefault('size', group['size'])
                continue

        return ret_dict
