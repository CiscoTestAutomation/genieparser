'''show_platform.py

JunOS parsers for the following show commands:
    * show ppm transmissions protocol bfd detail
'''

# Python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, \
                    Optional, Use


# ===========================
# Schema for:
#   * 'show ppm transmissions protocol bfd detail'
# ===========================
class ShowPPMTransmissionsProtocolBfdDetailSchema(MetaParser):
    ''' Schema for:
        * 'show ppm transmissions protocol bfd detail'
    '''
    '''
    schema = {
    "ppm-transmissions": {
        "transmission-data": [{
            "protocol": str,
            "transmission-destination": str,
            "transmission-distributed": str,
            Optional("transmission-host"): str,
            "transmission-interface-index": str,
            "transmission-interval": str,
            "transmission-pfe-addr": str,
            "transmission-pfe-handle": str
            }]
        }
    }
    '''

    def validate_transmission_data(value):
        if not isinstance(value, list):
            raise SchemaError('transmission data is not a list')

        transmission_data = Schema({
            "protocol": str,
            "transmission-destination": str,
            "transmission-distributed": str,
            Optional("transmission-host"): str,
            "transmission-interface-index": str,
            "transmission-interval": str,
            "transmission-pfe-addr": str,
            "transmission-pfe-handle": str
        })

        for item in value:
            transmission_data.validate(item)
        return value

    schema = {
        "ppm-transmissions": {
            "transmission-data": Use(validate_transmission_data)
        }
    }



# ===========================
# Parser for:
#   * 'show ppm transmissions protocol bfd detail'
# ===========================
class ShowPPMTransmissionsProtocolBfdDetail(ShowPPMTransmissionsProtocolBfdDetailSchema):
    ''' Parser for:
        * 'show ppm transmissions protocol bfd detail'
    '''

    cli_command = 'show ppm transmissions protocol bfd detail'

    def cli(self, output=None):

        # Execute command
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init
        ret_dict = {}

        # Destination: 27.85.194.102, Protocol: BFD, Transmission interval: 300
        p1 = re.compile(r'^Destination: +(?P<transmission_destination>[\d\.]+), '
                        r'+Protocol: +(?P<protocol>\S+), Transmission +interval: '
                        r'+(?P<transmission_interval>\d+)$')

        # Distributed: TRUE, Distribution handle: 6918, Distribution address: fpc9
        p2 = re.compile(r'^Distributed: +(?P<transmission_distributed>\S+), '
                        r'+Distribution +handle: +(?P<transmission_pfe_handle>\d+), '
                        r'Distribution +address: +(?P<transmission_pfe_addr>\S+)$')

        # IFL-index: 783
        p3 = re.compile(r'^IFL-index: +(?P<transmission_interface_index>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Destination: 27.85.194.102, Protocol: BFD, Transmission interval: 300
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ppm_transmissions = ret_dict.setdefault('ppm-transmissions', {}). \
                    setdefault('transmission-data', [])
                
                transmission_data_dict = {}

                for key, value in group.items():
                    key = key.replace('_', '-')
                    transmission_data_dict[key] = value

                ppm_transmissions.append(transmission_data_dict)
                continue

            # Distributed: TRUE, Distribution handle: 6918, Distribution address: fpc9
            m = p2.match(line)
            if m:
                group = m.groupdict()
                for key, value in group.items():
                    key = key.replace('_', '-')
                    transmission_data_dict.update({key:value})
                continue

            # IFL-index: 783
            m = p3.match(line)
            if m:
                group = m.groupdict()
                for key, value in group.items():
                    key = key.replace('_', '-')
                    transmission_data_dict.update({key:value})
                continue
            
        return ret_dict