
# Metaparser
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Optional, ListOf

# pyATS
from pyats.utils.exceptions import SchemaTypeError

class ShowSoftwareAuthenticityRunningSchema(MetaParser):
    """Schema for show software authenticity"""
    schema = {
        'package': {
            str: {
                'image_type': str,
                'signer_information': {
                    'common_name': str,
                    'organization_unit': str,
                    'organization_name': str
                },
                'certificate_serial_number': str,
                'hash_algorithm': str,
                'signature_algorithm': str,
                'key_version': str,
                'verifier_information': {
                    'verifier_name': str,
                    'verifier_version': str
                }
            }
        },
        Optional('system_image'): {
            'image_type': str,
            'signer_information': {
                'common_name': str,
                'organization_unit': str,
                'organization_name': str
            },
            'certificate_serial_number': str,
            'hash_algorithm': str,
            'signature_algorithm': str,
            'key_version': str,
            'verifier_information': {
                'verifier_name': str,
                'verifier_version': str
            }
        },
        Optional('rommon'): {
            'image_type': str,
            'signer_information': {
                'common_name': str,
                'organization_unit': str,
                'organization_name': str
            },
            'certificate_serial_number': str,
            'hash_algorithm': str,
            'signature_algorithm': str,
            'key_version': str,
            'verifier_information': {
                'verifier_name': str,
                'verifier_version': str
            }
        },
        Optional('microloader'): {
            'image_type': str,
            'signer_information': {
                'common_name': str,
                'organization_name': str
            },
            'certificate_serial_number': str,
            'hash_algorithm': str,
            'verifier_information': {
                'verifier_name': str,
                'verifier_version': str
            }
        }
    }

class ShowSoftwareAuthenticityRunning(ShowSoftwareAuthenticityRunningSchema):
    """Parser for show software authenticity"""

    cli_command = 'show software authenticity running'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        ret_dict = {}
        current_dict = None
        
        #PACKAGE cat9k-rpbase.BLD_POLARIS_DEV_LATEST_20240415_003241.SSA.pkg
        p1 = re.compile(r'^PACKAGE (?P<package_name>.+)$')
        
        #SYSTEM IMAGE
        p2 = re.compile(r'^SYSTEM IMAGE$')
        
        #ROMMON
        p3 = re.compile(r'^ROMMON$')
        
        # Microloader
        p4 = re.compile(r'^Microloader$')
        
        #General- Common Name           : CiscoSystems
        p5 = re.compile(r'^(?P<key>[\w\s]+): (?P<value>.+)$')
        
        for line in output.splitlines():
            line = line.strip()
            
            #PACKAGE
            if p1.match(line):
                package_name = p1.match(line).group(1)
                current_dict = ret_dict.setdefault('package', {}).setdefault(package_name, {})
                continue

            #SYSTEM IMAGE
            if p2.match(line):
                current_dict = ret_dict.setdefault('system_image', {})
                continue
            
            #ROMMON
            if p3.match(line):
                current_dict = ret_dict.setdefault('rommon', {})
                continue
                
            #Microloader
            if p4.match(line):
                current_dict = ret_dict.setdefault('microloader', {})
                continue

            #General- Common Name           : CiscoSystems
            match = p5.match(line)
            if match:
                group = match.groupdict()
                key = group['key'].strip().lower().replace(' ', '_')
                value = group['value'].strip()
                if key == 'image_type':
                    current_dict[key] = value 
                elif key=='common_name' or key=='organization_unit' or key=='organization_name':
                    current_dict.setdefault('signer_information', {})[key] = value
                elif key=='verifier_name' or key=='verifier_version':
                    current_dict.setdefault('verifier_information', {})[key] = value
                else:
                    current_dict[key] = value
                continue

        return ret_dict
