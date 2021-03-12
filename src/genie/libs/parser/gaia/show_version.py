
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

class ShowVersionSchema(MetaParser):
    schema = {
        'version': {
            'os' : {
                'build': str,
                'edition': str,
                'kernel': str
            },
            'product': str
        }
    }

class ShowVersion(ShowVersionSchema):

    cli_command = ['show version all']
    
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}

        if out is '':
            return result_dict

        result_dict = {
            'version': {
                'product': '',   
                'os': {
                    'build': '',
                    'kernel': '',
                    'edition': ''
                    }
                }
            }

        p_version = re.compile(r'^Product version Check Point Gaia (?P<version>.*)$')
        p_build = re.compile(r'^OS build (?P<build>.*)$')
        p_kernel = re.compile(r'^OS kernel version (?P<kernel>.*)$')
        p_edition = re.compile(r'^OS edition (?P<edition>.*)$')

        for line in out.splitlines():
            line = line.strip()

            m = p_version.match(line)
            if m:
                version = m.groupdict()['version']
                result_dict['version']['product'] = version
                continue
            
            m = p_build.match(line)
            if m:
                build = m.groupdict()['build']
                result_dict['version']['os']['build'] = build
                continue
            
            m = p_kernel.match(line)
            if m:
                kernel = m.groupdict()['kernel']
                result_dict['version']['os']['kernel'] = kernel
                continue

            m = p_edition.match(line)
            if m:
                edition = m.groupdict()['edition']
                result_dict['version']['os']['edition'] = edition
                continue
            
        return result_dict 



    

