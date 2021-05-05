
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

class ShowVersionSchema(MetaParser):
    schema = {
        'version': {
            'product': str,
            'os_build': str,
            'os_edition': str,
            'os_kernel': str
            },
        }

class ShowVersion(ShowVersionSchema):

    cli_command = ['show version all']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}

        if out == '':
            return result_dict

        result_dict = {
            'version': {
                'product': '',
                'os_build': '',
                'os_kernel': '',
                'os_edition': '',
                }
            }

        ''' Sample Output
        gw-a> show version all
        Product version Check Point Gaia R80.40
        OS build 294
        OS kernel version 3.10.0-957.21.3cpx86_64
        OS edition 64-bit
        '''

        p_version = re.compile(r'^Product version Check Point Gaia (?P<version>.*)$')
        p_build = re.compile(r'^OS build (?P<build>.*)$')
        p_kernel = re.compile(r'^OS kernel version (?P<kernel>.*)$')
        p_edition = re.compile(r'^OS edition (?P<edition>.*)$')

        for line in out.splitlines():
            line = line.strip()

            # Product version Check Point Gaia R80.40
            m = p_version.match(line)
            if m:
                version = m.groupdict()['version']
                result_dict['version']['product'] = version
                continue

            # OS build 294
            m = p_build.match(line)
            if m:
                build = m.groupdict()['build']
                result_dict['version']['os_build'] = build
                continue

            # OS kernel version 3.10.0-957.21.3cpx86_64
            m = p_kernel.match(line)
            if m:
                kernel = m.groupdict()['kernel']
                result_dict['version']['os_kernel'] = kernel
                continue

            # OS edition 64-bit
            m = p_edition.match(line)
            if m:
                edition = m.groupdict()['edition']
                result_dict['version']['os_edition'] = edition
                continue

        return result_dict
