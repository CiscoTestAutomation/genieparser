"""
show_image_version.py
Parser for the following ArubaOS show command(s):
    * show image version
"""

# Python
import re

from genie.metaparser.util import keynames_exist

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


class ShowImageVersionSchema(MetaParser):

    ''' Schema for:
        * 'show image version'
    '''
    
    schema = {
        'partition': {
            Any(): {
                'disk': str,
                'firmware_version': str,
                'signature_type': str,
                'build_type': str,
                'build_number': int,
                'label': str,
                'built_on': str,
            },
            'default_partition': int,
        },
    }


class ShowImageVersion(ShowImageVersionSchema):
    
    '''Parser for:
        * 'show image version'
    '''
    
    cli_command = 'show image version'

    """
    ----------------------------------
    Partition               : 0:0 (/mnt/disk1)
    Software Version        : ArubaOS 8.6.0.16 (Digitally Signed SHA1/SHA256 - Production Build)
    Build number            : 82590
    Label                   : 82590
    Built on                : Thu Dec 16 13:28:34 UTC 2021
    ----------------------------------
    Partition               : 0:1 (/mnt/disk2) **Default boot**
    Software Version        : ArubaOS 8.10.0.0 LSR (Digitally Signed SHA1/SHA256 - Developer/Internal Build)
    Build number            : 0000
    Label                   : jenkins@yk-aos-preflight-ENG.0000
    Built on                : Wed Mar 9 09:41:5
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        ret_dict = {}
        partition_dict = {}

        p0 = re.compile(r'^Partition\s+:\s\d:(?P<partition>\d)\s\((?P<disk>.*)\)\s*(?P<default_partition>\*\*Default boot\*\*)?$')

        p1 = re.compile(r'^Software\s+Version\s+:\s+(?P<firmware_version>.*)\s\(Digitally\s+Signed\s+(?P<signature_type>.*)\s+-\s+(?P<build_type>.*)\s+Build\)$')

        p2 = re.compile(r'^Build\s+number\s+:\s+(?P<build_number>\d*)$')

        p3 = re.compile(r'^Label\s+:\s+(?P<label>.*)$')

        p4 = re.compile(r'^Built\s+on\s+:\s+(?P<built_on>.*)$')

        for line in out.splitlines():           
            line = line.strip()

            m = p0.match(line)
            if m:
                partition = int(m.groupdict()['partition'])
                if 'partition' not in ret_dict:
                    partition_dict = ret_dict.setdefault('partition', {})
                disk = m.groupdict()['disk']
                default_partition = m.groupdict()['default_partition']

                partition_dict[partition] = {}

                partition_dict[partition]['disk'] = disk
                if default_partition:
                    partition_dict['default_partition'] = int(partition)
                continue

            m = p1.match(line)
            if m:
                firmware_version = m.groupdict()['firmware_version']
                signature_type = m.groupdict()['signature_type']
                build_type = m.groupdict()['build_type']

                partition_dict[partition]['firmware_version'] = firmware_version
                partition_dict[partition]['signature_type'] = signature_type
                partition_dict[partition]['build_type'] = build_type
                continue

            m = p2.match(line)
            if m:
                build_number = m.groupdict()['build_number']

                partition_dict[partition]['build_number'] = int(build_number)
                continue

            m = p3.match(line)
            if m:
                label = m.groupdict()['label']

                partition_dict[partition]['label'] = label
                continue

            m = p4.match(line)
            if m:
                built_on = m.groupdict()['built_on']

                partition_dict[partition]['built_on'] = built_on
                continue

        keynames_to_check = ['partition', 'partition.default_partition']
        assert keynames_exist(ret_dict, keynames_to_check) == None

        return ret_dict

