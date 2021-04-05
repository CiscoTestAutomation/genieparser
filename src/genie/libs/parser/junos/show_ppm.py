'''show_ppm.py

JunOS parsers for the following show commands:
    * show ppm transmissions protocol bfd detail
'''

# Python
import re

# Genie
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import Schema, Any, \
                    Optional, Use, ListOf


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

    schema = {
        "ppm-transmissions": {
            Optional("remote-transmissions"): str,
            Optional("total-transmissions"): str,
            "transmission-data": ListOf({
               "protocol": str,
                Optional("transmission-count"): str,
                Optional("transmission-delay-difference"): str,
                Optional("transmission-delayed"): str,
                Optional("transmission-delayed-count"): str,
                "transmission-destination": str,
                "transmission-distributed": str,
                Optional("transmission-host"): str,
                "transmission-interface-index": str,
                "transmission-interval": str,
                Optional("transmission-interval-threshold"): str,
                Optional("transmission-jitter"): str,
                Optional("transmission-largest-difference"): str,
                Optional("transmission-last-interval"): str,
                Optional("transmission-pfe-addr"): str,
                Optional("transmission-pfe-handle"): str
            })
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

        # Destination: 10.49.194.102, Protocol: BFD, Transmission interval: 300
        p1 = re.compile(r'^Destination: +(?P<transmission_destination>\S+), '
                        r'+Protocol: +(?P<protocol>\S+), Transmission +interval: '
                        r'+(?P<transmission_interval>\d+)$')

        # Distributed: TRUE, Distribution handle: 6918, Distribution address: fpc9
        p2 = re.compile(r'^Distributed: +(?P<transmission_distributed>\S+)'
                        r'(, +Distribution +handle: +(?P<transmission_pfe_handle>\d+), '
                        r'Distribution +address: +(?P<transmission_pfe_addr>\S+))?$')

        # IFL-index: 783
        p3 = re.compile(r'^IFL-index: +(?P<transmission_interface_index>\d+)$')

        # Tx Jitter: 25, Tx Delayed: FALSE, Delay Difference: 0, Last Tx Interval: 821, Tx Delayed count: 0, Tx Interval Threshold: 1250, Tx Largest Interval: 0, Tx Counter: 15891
        p4 = re.compile(r'^Tx +Jitter: +(?P<transmission_jitter>[\d\.]+), Tx +Delayed: +'
                        r'(?P<transmission_delayed>\S+), +Delay +Difference: +(?P<transmission_delay_difference>\d+), '
                        r'Last+ Tx +Interval: +(?P<transmission_last_interval>\d+), +Tx +Delayed +count: +'
                        r'(?P<transmission_delayed_count>\d+), +Tx +Interval +Threshold: +(?P<transmission_interval_threshold>\d+), '
                        r'+Tx +Largest +Interval: +(?P<transmission_largest_difference>\d+), +Tx +Counter: (?P<transmission_count>\d+)$')

        # Transmission entries: 6, Remote transmission entries: 3
        p5 = re.compile(r'^Transmission +entries: +(?P<total_transmissions>\d+), +Remote +transmission +entries: +(?P<remote_transmissions>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Destination: 10.49.194.102, Protocol: BFD, Transmission interval: 300
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ppm_transmissions = ret_dict.setdefault('ppm-transmissions', {})

                transmission_data_list = ppm_transmissions.setdefault('transmission-data', [])

                transmission_data_dict = {}

                for key, value in group.items():
                    key = key.replace('_', '-')
                    transmission_data_dict[key] = value

                transmission_data_list.append(transmission_data_dict)
                continue

            # Distributed: TRUE, Distribution handle: 6918, Distribution address: fpc9
            m = p2.match(line)
            if m:
                group = m.groupdict()
                for key, value in group.items():
                    if value != None:
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

            # Tx Jitter: 25, Tx Delayed: FALSE, Delay Difference: 0, Last Tx Interval: 821, Tx Delayed count: 0, Tx Interval Threshold: 1250, Tx Largest Interval: 0, Tx Counter: 15891
            m = p4.match(line)
            if m:
                group = m.groupdict()
                for key, value in group.items():
                    key = key.replace('_', '-')
                    transmission_data_dict.update({key:value})
                continue

            # Transmission entries: 6, Remote transmission entries: 3
            m = p5.match(line)
            if m:
                group = m.groupdict()
                for key, value in group.items():
                    key = key.replace('_', '-')
                    ppm_transmissions.update({key:value})
                continue

        return ret_dict