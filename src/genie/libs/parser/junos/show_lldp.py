""" show_lldp.py

JunOs parsers for the following show commands:
    * show lldp
"""

# Python
import re

# ==============================
# Schema for 'show lldp'
# ==============================
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional


class ShowLldpSchema(MetaParser):
    """ Schema for:
            * show lldp
    """

    # These are the key-value pairs to add to the parsed dictionary
    schema = {
        'lldp-global-status': str,
        'lldp-advertisement-interval': str,
        'lldp-transmit-delay-interval': str,
        'lldp-hold-time-interval': str,
        'lldp-notification-interval': str,
        'ptopo-configuration-trap-interval': str,
        'ptopo-maximum-hold-time': str,
        'lldp-med-global-status': str,
        'lldp-port-id-subtype': str,
        Optional('lldp-port-description-type'): str,
    }


# ==============================
# Parser for 'show lldp'
# ==============================


# The parser class inherits from the schema class
class ShowLldp(ShowLldpSchema):
    ''' Parser for "show lldp"'''

    cli_command = 'show lldp'
    # exclude contains fields of command output which holds random values and
    # thus can't be used for tests
    exclude = [
        'lldp-advertisement-interval', 'lldp-transmit-delay-interval',
        'lldp-hold-time-interval', 'lldp-notification-interval',
        'ptopo-configuration-trap-interval', 'ptopo-maximum-hold-time'
    ]

    # Defines a function to run the cli_command
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Initializes the Python dictionary variable
        parsed_dict = {}

        # LLDP : Disabled
        p1 = re.compile(r'^LLDP\s*:\s*(?P<lldp_global_status>\w+)$')

        # Advertisement interval    : 30 seconds
        p2 = re.compile(r'^Advertisement\s+interval\s*:\s*('
                        r'?P<lldp_advertisement_interval>\d+) +seconds?$')

        # Transmit delay            : 0 seconds
        p3 = re.compile(
            r'^Transmit\s+delay\s*:\s*(?P<lldp_transmit_delay_interval>\d+) '
            r'+seconds?$')

        # Hold timer                : 120 seconds
        p4 = re.compile(
            r'^Hold\s+timer\s*:\s*(?P<lldp_hold_time_interval>\d+) '
            r'+seconds?$')

        # Notification interval     : 5 Second(s)
        p5 = re.compile(r'^Notification\s+interval\s*:\s*('
                        r'?P<lldp_notification_interval>\d+) +Second\(s\)$')

        # Config Trap Interval      : 0 seconds
        p6 = re.compile(
            r'^Config\s+Trap\s+Interval\s*:\s*('
            r'?P<ptopo_configuration_trap_interval>\d+) +seconds?$')

        # Connection Hold timer     : 300 seconds
        p7 = re.compile(r'^Connection\s+Hold\s+timer\s*:\s*('
                        r'?P<ptopo_maximum_hold_time>\d+) +seconds?$')

        # LLDP MED                  : Disabled
        p8 = re.compile(r'^LLDP\s+MED\s*:\s*(?P<lldp_med_global_status>\w+)$')

        # Port ID TLV subtype       : locally-assigned
        p9 = re.compile(
            r'^Port\s+ID\s+TLV\s+subtype\s*:\s*(?P<lldp_port_id_subtype>['
            r'-\w\s]+)$')

        # Port Description TLV type : interface-alias (ifAlias)
        p10 = re.compile(r'^Port\s+Description\s+TLV\s+type\s*:\s*('
                         r'?P<lldp_port_description_type>[\s\S]+)$')

        for line in out.splitlines():
            line = line.strip()

            # LLDP : Disabled
            m = p1.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['lldp-global-status'] = group['lldp_global_status']
                continue

            # Advertisement interval : 30 seconds
            m = p2.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['lldp-advertisement-interval'] = \
                    group['lldp_advertisement_interval']
                continue

            # Transmit delay            : 0 seconds
            m = p3.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['lldp-transmit-delay-interval'] = \
                    group['lldp_transmit_delay_interval']
                continue

            # Hold timer                : 120 seconds
            m = p4.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['lldp-hold-time-interval'] = \
                    group['lldp_hold_time_interval']
                continue

            # Notification interval     : 5 Second(s)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['lldp-notification-interval'] = \
                    group['lldp_notification_interval']
                continue

            # Config Trap Interval      : 0 seconds
            m = p6.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['ptopo-configuration-trap-interval'] = \
                    group['ptopo_configuration_trap_interval']
                continue

            # Connection Hold timer     : 300 seconds
            m = p7.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['ptopo-maximum-hold-time'] = \
                    group['ptopo_maximum_hold_time']
                continue

            # LLDP MED                  : Disabled
            m = p8.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['lldp-med-global-status'] = \
                    group['lldp_med_global_status']
                continue

            # Port ID TLV subtype       : locally-assigned
            m = p9.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['lldp-port-id-subtype'] = \
                    group['lldp_port_id_subtype']
                continue

            # Port Description TLV type : interface-alias (ifAlias)
            m = p10.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['lldp-port-description-type'] = \
                    group['lldp_port_description_type']
                continue

        return parsed_dict
