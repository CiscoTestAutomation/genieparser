
# Metaparser
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Optional, ListOf

# pyATS
from pyats.utils.exceptions import SchemaTypeError

class ShowSoftwareAuthenticityKeysSchema(MetaParser):
    """Schema for show software authenticity keys"""
    schema = {
        'public_key': {
            int: {
                'key_type': str,
                'key_type_note': str,
                'key_algorithm': str,
                'modulus_size': int,
                'modulus': str,
                'exponent_size': int,
                'exponent': int,
                'key_version': str,
                'product_name': str
            }
        }
    }

class ShowSoftwareAuthenticityKeys(ShowSoftwareAuthenticityKeysSchema):
    """Parser for show software authenticity keys"""

    cli_command = 'show software authenticity keys'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        ret_dict = {}
        current_dict = None
        
        # Public Key #1 Information
        p1 = re.compile(r'^Public Key #(?P<key_number>\d+) Information$')

        # Key Type                  : Production  (Primary)                                                                                   
        p2 = re.compile(
            r'^Key Type +: (?P<key_type>\w+) +\((?P<key_type_note>\w+)\)$'
        )
        
        # Public Key Algorithm : RSA
        p3 = re.compile(r'^Public Key Algorithm : (?P<key_algorithm>\w+)$')

        # Modulus (512 bytes)   : 
        p4 = re.compile(
            r'^Modulus \((?P<modulus_size>\d+) bytes\) +: *$'
        )

        # d8:1f:8e:b1:49:7c:bd:83:20:5f:25:43:d9:32:5a:b5:
        p5 = re.compile(
            r'^(?P<modulus>[0-9a-f:]+|[0-9a-f:]+[0-9a-f])$'
        )

        # Exponent (4 bytes)   : 10001
        p6 = re.compile(
            r'^Exponent \((?P<exponent_size>\d+) bytes\) +: (?P<exponent>\d+)$'
        )

        # Key Version          : A
        p7 = re.compile(r'^Key Version +: (?P<key_version>\w+)$')

        # Product Name         : IOS-XE
        p8 = re.compile(r'^Product Name +: (?P<product_name>.*)$')

        for line in output.splitlines():
            line = line.strip()

            # Public Key #1 Information
            if p1.match(line):
                key_number = int(p1.match(line).group(1))
                current_dict = ret_dict.setdefault('public_key', {}).setdefault(
                    key_number, {}
                )
                continue

            # Key Type                  : Production  (Primary)
            match = p2.match(line)
            if match:
                group = match.groupdict()
                key_type = group['key_type']
                key_type_note = group['key_type_note']
                current_dict['key_type'] = key_type
                current_dict['key_type_note'] = key_type_note
                continue

            # Public Key Algorithm : RSA
            match = p3.match(line)
            if match:
                group = match.groupdict()
                key_algorithm = group['key_algorithm']
                current_dict['key_algorithm'] = key_algorithm
                continue

            # Modulus (512 bytes)   : 
            match = p4.match(line)
            if match:
                group = match.groupdict()
                modulus_size = int(group['modulus_size'])
                current_dict['modulus_size'] = modulus_size
                continue

            # d8:1f:8e:b1:49:7c:bd:83:20:5f:25:43:d9:32:5a:b5:
            match = p5.match(line)
            if match:
                group = match.groupdict()
                modulus = group['modulus']
                current_dict.setdefault('modulus', '')
                current_dict['modulus'] += modulus
                continue

            # Exponent (4 bytes)   : 10001
            match = p6.match(line)
            if match:
                group = match.groupdict()
                exponent_size = int(group['exponent_size'])
                exponent = int(group['exponent'])
                current_dict['exponent_size'] = exponent_size
                current_dict['exponent'] = exponent
                continue

            # Key Version          : A
            match = p7.match(line)
            if match:
                group = match.groupdict()
                key_version = group['key_version']
                current_dict['key_version'] = key_version
                continue

            # Product Name         : IOS-XE
            match = p8.match(line)
            if match:
                group = match.groupdict()
                product_name = group['product_name']
                current_dict['product_name'] = product_name
                continue

        return ret_dict