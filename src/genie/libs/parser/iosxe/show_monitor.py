''' show_monitor.py

IOSXE parsers for the following show commands:
    * show monitor
    * show monitor session all
    * show monitor capture

'''


# Python
import re
import xmltodict
from netaddr import IPAddress, IPNetwork

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, And, Default, Use

# import parser utils
from genie.libs.parser.utils.common import Common


# =========================================
# Schema for 'show monitor'
# =========================================
class ShowMonitorSchema(MetaParser):

    ''' Schema for "show monitor" '''

    schema = {
        'session':
            {Any():
                 {'type':str,
                  'status':str,
                  Optional('source_ports'):
                      {Any(): str,
                      },
                  Optional('destination_ports'): str,
                  Optional('destination_ip_address'): str,
                  Optional('destination_erspan_id'): str,
                  Optional('origin_ip_address'): str,
                  Optional('source_erspan_id'): str,
                  Optional('source_ip_address'): str,
                  'mtu': int,
                  },
            },
        }


# =========================================
# Parser for 'show monitor'
# =========================================
class ShowMonitor(ShowMonitorSchema):
    ''' Parser for
      "show monitor"
      "show monitor session all"
    '''

    cli_command = ['show monitor', 'show monitor session {session}']

    def cli(self, session="", output=None):
        if output is None:
            if session:
                cmd = self.cli_command[-1].format(session=session)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}

        # Session 1
        p1 = re.compile('Session +(?P<session>(\d+))')

        # Type                   : ERSPAN Source Session
        p2 = re.compile('^Type +: +(?P<type>([a-zA-Z\s]+))$')

        # Status                 : Admin Enabled
        p3 = re.compile('^Status +: +(?P<status>([a-zA-Z\s]+))$')

        # Source Ports           :
        p4_1 = re.compile('^Source +Ports +:$')

        #    TX Only            : Gi0/1/4
        #    Both               : Gi0/1/4
        p4_2 = re.compile('(?P<key>(TX Only|Both)) *: +(?P<intf>(\S+))$')

        # Destination IP Address : 172.18.197.254
        p5 = re.compile('^Destination +IP +Address +: +(?P<destination_ip_address>([0-9\.\:]+))$')

        # MTU                    : 1464
        p6 = re.compile('^MTU +: +(?P<mtu>([0-9]+))$')

        # Destination ERSPAN ID  : 1
        p7 = re.compile('^Destination +ERSPAN +ID +: +(?P<destination_erspan_Id>([0-9]+))$')

        # Origin IP Address      : 172.18.197.254
        p8 = re.compile('^Origin +IP +Address +: +(?P<origin_ip_address>([0-9\.\:]+))$')

        # Destination Ports      : Gi0/1/6 Gi0/1/2
        p9 = re.compile('^Destination +Ports +: +(?P<destination_ports>([a-zA-Z0-9\/\s]+))$')

        # Source IP Address      : 172.18.197.254
        p10 = re.compile('^Source +IP +Address +: +(?P<source_ip_address>([0-9\.\:]+))$')

        # Source ERSPAN ID       : 1
        p11 = re.compile('^Source +ERSPAN +ID +: +(?P<source_erspan_Id>([0-9]+))$')

        for line in out.splitlines():
            line = line.strip()

            # Session 1
            m = p1.match(line)
            if m:
                session = m.groupdict()['session']
                session_dict = ret_dict.setdefault('session', {}).setdefault(session, {})
                continue

            # Type                   : ERSPAN Source Session
            m = p2.match(line)
            if m:
                session_dict['type'] = str(m.groupdict()['type'])
                continue

            # Status                 : Admin Enabled
            m = p3.match(line)
            if m:
                session_dict['status'] = str(m.groupdict()['status'])
                continue

            # Source Ports           :
            m = p4_1.match(line)
            if m:
                src_ports_dict = session_dict.setdefault('source_ports', {})
                continue

            #    TX Only            : Gi0/1/4
            #    Both               : Gi0/1/4
            m = p4_2.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].lower().replace(" ", "_")
                # Set keys
                src_ports_dict[key] = group['intf']
                continue

            # Destination IP Address : 172.18.197.254
            m = p5.match(line)
            if m:
                session_dict['destination_ip_address'] = str(m.groupdict()['destination_ip_address'])
                continue

            # MTU                    : 1464
            m = p6.match(line)
            if m:
                session_dict['mtu'] = int(m.groupdict()['mtu'])
                continue

            # Destination ERSPAN ID  : 1
            m = p7.match(line)
            if m:
                session_dict['destination_erspan_id'] = str(m.groupdict()['destination_erspan_Id'])
                continue

            # Origin IP Address      : 172.18.197.254
            m = p8.match(line)
            if m:
                session_dict['origin_ip_address'] = str(m.groupdict()['origin_ip_address'])
                continue

            # Destination Ports      : Gi0/1/6 Gi0/1/2
            m = p9.match(line)
            if m:
                session_dict['destination_ports'] = str(m.groupdict()['destination_ports'])
                continue
            # Source IP Address      : 172.18.197.254
            m = p10.match(line)
            if m:
                session_dict['source_ip_address'] = str(m.groupdict()['source_ip_address'])
                continue

            # Source ERSPAN ID       : 1
            m = p11.match(line)
            if m:
                session_dict['source_erspan_id'] = str(m.groupdict()['source_erspan_Id'])
                continue

        return ret_dict


# =========================================
# Schema for 'show monitor capture'
# =========================================
class ShowMonitorCaptureSchema(MetaParser):

    ''' Schema for "show monitor capture" '''

    schema = {
        'status_information':
            {Any():
                {'target_type':
                    {'interface': str,
                     'direction': str,
                     'status': str
                    },
                'filter_details': str,
                'buffer_details':
                    {'buffer_type': str,
                     'buffer_size': int
                    },
                'limit_details':
                    {'packets_number': int,
                     'packets_capture_duaration': int,
                     'packets_size': int,
                     'maximum_packets_number': int,
                     'packet_sampling_rate': int
                    },
                },
            },
        }


# =========================================
# Parser for 'show monitor capture'
# =========================================
class ShowMonitorCapture(ShowMonitorCaptureSchema):
    ''' Parser for
      "show monitor capture"
    '''

    cli_command = 'show monitor capture'

    def cli(self, output=None):
        if output is None:
            # Execute command on device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}

        # Status Information for Capture CAPTURE
        # Status Information for Capture NTP
        p1 = re.compile(r'^Status +Information +for +Capture +(?P<status_information>(\w+))$')

        # Target Type:
        p2 = re.compile(r'^Target +Type:+$')

        # Interface: Control Plane, Direction : both
        # Interface: GigabitEthernet0/0/0, Direction: both
        p3 = re.compile(r'^Interface: +(?P<interface>([\w\s\/]+)), +Direction *:+ (?P<direction>(\w+))$')

        # Status : Inactive
        p4 = re.compile(r'^Status +: +(?P<status>(\w+))$')

        #Capture all packets
        p5 = re.compile(r'^(?P<filter_details>([\w\s]+))$')

        # Buffer Details:
        p6 = re.compile(r'^Buffer +Details:+$')

        # Buffer Type: LINEAR (default)
        p7 = re.compile(r'^Buffer +Type: +(?P<buffer_type>(\w+))')

        # Buffer Size (in MB): 10
        p8 = re.compile(r'^Buffer +Size +\(in MB\): +(?P<buffer_size>(\d+))$')

        # Limit Details:
        p9 = re.compile(r'^Limit +Details:+$')

        # Number of Packets to capture: 0 (no limit)
        p10 = re.compile(r'^Number +of +Packets +to +capture: +(?P<packets_number>(\d+))')

        # Packet Capture duration: 0 (no limit)
        p11 = re.compile(r'^Packet +Capture +duration: +(?P<packets_capture_duaration>(\d+))')

        # Packet Size to capture: 0 (no limit)
        p12 = re.compile(r'^Packet +Size +to +capture: +(?P<packets_size>(\d+))')

        # Maximum number of packets to capture per second: 1000
        p13 = re.compile(r'^Maximum +number +of +packets +to +capture +per +second: +(?P<maximum_packets_number>(\d+))$')

        # Packet sampling rate: 0 (no sampling)
        p14 = re.compile(r'^Packet +sampling +rate: +(?P<packet_sampling_rate>(\d+))')

        for line in out.splitlines():
            line = line.strip()

            # Status Information for Capture CAPTURE
            # Status Information for Capture NTP
            m = p1.match(line)
            if m:
                status_information = m.groupdict()['status_information']
                status_dict = ret_dict.setdefault('status_information', {}).setdefault(status_information, {})
                continue

            # Target Type:
            m = p2.match(line)
            if m:
                target_type_dict = status_dict.setdefault('target_type',{})
                continue

            # Interface: Control Plane, Direction : both
            # Interface: GigabitEthernet0/0/0, Direction: both
            m = p3.match(line)
            if m:
                target_type_dict['interface'] = str(m.groupdict()['interface'])
                target_type_dict['direction'] = str(m.groupdict()['direction'])
                continue

            # Status : Active
            m = p4.match(line)
            if m:
                target_type_dict['status'] = str(m.groupdict()['status'])
                continue

            # Filter Details:
            # Capture all packets
            m = p5.match(line)
            if m:
                status_dict['filter_details']=str(m.groupdict()['filter_details'])
                continue

            # Buffer Details:
            m = p6.match(line)
            if m:
                buffer_dict = status_dict.setdefault('buffer_details',{})
                continue

            # Buffer Type: LINEAR (default)
            m = p7.match(line)
            if m:
                buffer_dict['buffer_type'] = str(m.groupdict()['buffer_type'])
                continue

            # Buffer Size (in MB): 10
            m = p8.match(line)
            if m:
                buffer_dict['buffer_size'] = int(m.groupdict()['buffer_size'])
                continue

            # Limit Details:
            m = p9.match(line)
            if m:
                limit_dict = status_dict.setdefault('limit_details', {})
                continue

            # Number of Packets to capture: 0 (no limit)
            m = p10.match(line)
            if m:
                limit_dict['packets_number'] = int(m.groupdict()['packets_number'])
                continue

            # Packet Capture duration: 0 (no limit)
            m = p11.match(line)
            if m:
                limit_dict['packets_capture_duaration'] = int(m.groupdict()['packets_capture_duaration'])
                continue

            # Packet Size to capture: 0 (no limit)
            m = p12.match(line)
            if m:
                limit_dict['packets_size'] = int(m.groupdict()['packets_size'])
                continue

            # Maximum number of packets to capture per second: 1000
            m = p13.match(line)
            if m:
                limit_dict['maximum_packets_number'] = int(m.groupdict()['maximum_packets_number'])
                continue

            # Packet sampling rate: 0 (no sampling)
            m = p14.match(line)
            if m:
                limit_dict['packet_sampling_rate'] = int(m.groupdict()['packet_sampling_rate'])
                continue


        return ret_dict
