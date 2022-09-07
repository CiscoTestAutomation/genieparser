''' show_device_sensor.py

IOSXE parsers for the following show commands:
    * show device-sensor cache interface {interface}
'''

# Python

import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common

# =================
# Schema for:
#  * 'show device-sensor cache interface {interface}'
# =================

class ShowDeviceSensorSchema(MetaParser):
    """Schema for show device-sensor cache interface {interface}"""
    schema = {
        'device':{
            # device mac address
            Any(): {
                'port': {
                    Any(): {
                        'proto': {
                            # Protocol - DHCP or CDP
                            Any(): {
                                'type': {
                                    # Protocol Type - integer
                                    Any(): {  
                                        'name': str,
                                        'length': int,
                                        'value': str,
                                        'text': str,
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

# =================
# Parser for:
#  * 'show device-sensor'
# =================
class ShowDeviceSensor(ShowDeviceSensorSchema):
    '''Parser for show device-sensor cache interface {interface}     

    '''

    cli_command = ['show device-sensor cache interface {interface}']

    def cli(self, interface=None, output=None):
        if output is None:            
            if interface:
                cmd = "show device-sensor cache interface {interface}".format(interface=interface)
                output = self.device.execute(cmd)
        else:
            output = output

        # initial variables
        ret_dict = {'device': {}}

        if output:
            if "No elements found in cache" in output:
                ret_dict = {}
                return ret_dict

        # Device: 0050.56ae.de2e on port TenGigabitEthernet1/1/6
        p0 = re.compile(r'^Device: +(?P<mac>\S+) +on port (?P<port>\S+)$')

        # DHCP    60:class-identifier            10 3C 08 63 69 73 63 6F 70 6E  <.ciscopn
        p1 = re.compile(r'^(?P<protocol>\S+)\s+(?P<proto_type>\d+):(?P<name>\S+)\s+(?P<length>\d+)\s(?P<value>[0-9A-F\d ]{27})\s(?P<text>\S+)$')

        #                                           30 63 37 35 2E 62 64 30 32  0c75.bd02
        p2 = re.compile(r'^\s+(?P<value>[0-9A-F\d ]{27})\s(?P<text>\S+)$')

        for line in output.splitlines():
            line_strip = line.strip()

            m = p0.match(line)
            if m:
                mac = m.groupdict()['mac']
                mac_dict = ret_dict['device'].setdefault(mac, {})
                mac_dict['port'] = {}
                interface = m.groupdict()['port']
                port_dict = mac_dict['port'].setdefault(interface, {})
                port_dict.setdefault('proto', {})
                continue

            m = p1.match(line)
            if m:
                protocol = m.groupdict()['protocol']
                prot_dict = port_dict['proto'].setdefault(protocol, {})
                prot_dict.setdefault('type', {})
                proto_type = m.groupdict()['proto_type']
                # cast to integer
                proto_type_dict = prot_dict['type'].setdefault(int(proto_type), {})
                
                proto_type_dict['name'] = m.groupdict()['name']
                proto_type_dict['length'] = int(m.groupdict()['length'])
                # strip blankspace from the end of the string
                proto_type_dict['value'] = m.groupdict()['value'].rstrip()
                proto_type_dict['text'] = m.groupdict()['text']
                continue

            m = p2.match(line)
            if m:
                value = m.groupdict()['value']
                text = m.groupdict()['text']                
                if value:
                    # Add to existing string
                    proto_type_dict['value'] = proto_type_dict['value'] +" " +value.rstrip()
                if text:
                    # Add to existing string
                    proto_type_dict['text']+=text
                continue

        return ret_dict
# ----------------------
