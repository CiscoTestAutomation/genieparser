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
        # SONiC OS Version: 11
        # Distribution: Debian 11.7
        # Kernel: 5.10.0-18-2-amd64
        # Build commit: a2dedc96c
        # Build date: Fri Jul  7 14:22:57 UTC 2023
        # Built by: sonicci@sonic-ci-7-lnx
        #
        # Platform: x86_64-8201_32fh_o-r0
        # HwSKU: 32x400Gb
        # ASIC: cisco-8000
        # ASIC Count: 1
        # Serial Number: FOC2217FQXV
        # Model Number: 8201-32FH-O
        # Hardware Revision: 0.33
        # Uptime: 17:07:15 up 15 min,  1 user,  load average: 0.82, 1.00, 0.90
        # Date: Thu 02 Nov 2023 17:07:15
        p1 = re.compile(r'^(?P<key>.+): +(?P<value>.+)')
        # Uptime: 17:07:15 up 15 min,  1 user,  load average: 0.82, 1.00, 0.90
        p1_1 = re.compile(r'^Uptime: (?P<uptime>.+), +(?P<users>\d+) user, +load average: (?P<load_average>.+)$')

        # REPOSITORY                    TAG                  IMAGE ID           SIZE
        # docker-macsec                 latest               44ef5532977a       332MB
        p2 = re.compile(r'^(?P<repository>\S+) +(?P<tag>\S+) +(?P<image_id>\w+) +(?P<size>\S+)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Distribution: Debian 11.7
            # Kernel: 5.10.0-18-2-amd64
            if m := p1.match(line):
                key = m.groupdict()['key']
                if 'uptime:' in key.lower():
                    # Uptime: 17:07:15 up 15 min,  1 user,  load average: 0.82, 1.00, 0.90
                    if m := p1_1.match(line):
                        group = m.groupdict()
                        ret_dict.update({
                            'uptime': group['uptime'],
                            'users': int(group['users']),
                            'load_average': [float(i) for i in group['load_average'].split(', ')]
                        })
                        continue
                else:
                    key = key.lower().replace(' ', '_')
                try:
                    value = int(m.groupdict()['value'])
                except ValueError:
                    value = m.groupdict()['value']

                if key == 'hwsku':
                    ret_dict.update({'hardware_sku': value})
                elif key == 'hardware_rev':
                    ret_dict.update({'hardware_revision': value})
                else:
                    ret_dict.update({key: value})
                continue

            # docker-macsec                 latest               44ef5532977a       332MB
            if m := p2.match(line):
                docker_dict = ret_dict.setdefault('docker_images', {}).setdefault('image_id', {}). \
                    setdefault(m.groupdict()['image_id'], {})
                docker_dict.update({
                    'repository': m.groupdict()['repository'],
                    'tag': m.groupdict()['tag'],
                    'size': m.groupdict()['size']
                })
                continue
        return ret_dict
