''' show_monitor.py

IOSXE parsers for the following show commands:
    * show monitor
    * show monitor session {session}
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
                  Optional('source_subinterfaces'):
                      {Any(): str,
                      },
                  Optional('source_vlans'):
                      {Any():str,
                      },
                  Optional('filter_access_group'): int,
                  Optional('destination_ports'): str,
                  Optional('destination_ip_address'): str,
                  Optional('destination_erspan_id'): str,
                  Optional('origin_ip_address'): str,
                  Optional('source_erspan_id'): str,
                  Optional('source_ip_address'): str,
                  Optional('source_rspan_vlan'): int,
                  Optional('dest_rspan_vlan'): int,
                  Optional('mtu'): int,
                  },
            },
        }


# =========================================
# Parser for 'show monitor'
# =========================================
class ShowMonitor(ShowMonitorSchema):
    ''' Parser for
      "show monitor"
      "show monitor session {session}"
      "show monitor session all"
    '''

    cli_command = ['show monitor', 'show monitor session {session}', 'show monitor session all']

    def cli(self, session="", all="", output=None):
        if output is None:
            if all:
                cmd = self.cli_command[2]
            elif session:
                cmd = self.cli_command[1].format(session=session)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}
        src_ports = False
        source_subintfs = False

        # Session 1
        p1 = re.compile(r'Session +(?P<session>(\d+))')

        # Type                   : ERSPAN Source Session
        # Type: ERSPAN Source Session
        p2 = re.compile(r'^Type *: +(?P<type>([a-zA-Z\s]+))$')

        # Status                 : Admin Enabled
        # Status: Admin Enabled
        p3 = re.compile(r'^Status *: +(?P<status>([a-zA-Z\s]+))$')

        # Source Ports           :
        p4_1 = re.compile(r'^Source +Ports +:$')

        #    TX Only            : Gi0/1/4
        #    Both               : Gi0/1/4
        p4_2 = re.compile(r'(?P<key>(TX Only|Both)) *: +(?P<src_val>(\S+))$')

        # Source Subinterfaces:
        p5_1 = re.compile(r'^Source +Subinterfaces:$')

        # Both: Gi2/2/0.100
        #p5_2 = re.compile(r'^(?P<key>(Both)) *: +(?P<val>([\w\/\.]+))$')

        # Source VLANs           :
        p6_1 = re.compile(r'^Source +VLANs +:$')

        # RX Only            : 20
        p6_2 = re.compile(r'^(?P<key>(RX Only)) *: +(?P<rx_val>(\d+))$')

        # Filter Access-Group: 100
        p7 = re.compile(r'^Filter +Access-Group: +(?P<filter_access_group>(\d+))$')

        # Destination Ports      : Gi0/1/6 Gi0/1/2
        p8 = re.compile(r'^Destination +Ports +: +(?P<destination_ports>([a-zA-Z0-9\/\s]+))$')

        # Destination IP Address : 172.18.197.254
        p9 = re.compile(r'^Destination +IP +Address +: +(?P<destination_ip_address>([0-9\.\:]+))$')

        # Destination ERSPAN ID  : 1
        p10 = re.compile(r'^Destination +ERSPAN +ID +: +(?P<destination_erspan_Id>([0-9]+))$')

        # Origin IP Address      : 172.18.197.254
        p11 = re.compile(r'^Origin +IP +Address *: +(?P<origin_ip_address>([0-9\.\:]+))$')

        # Source ERSPAN ID       : 1
        p12 = re.compile(r'^Source +ERSPAN +ID +: +(?P<source_erspan_Id>([0-9]+))$')

        # Source IP Address      : 172.18.197.254
        p13 = re.compile(r'^Source +IP +Address +: +(?P<source_ip_address>([0-9\.\:]+))$')

        # Source RSPAN VLAN : 100
        p14 = re.compile(r'^Source +RSPAN +VLAN :+ (?P<source_rspan_vlan>(\d+))$')

        # Dest RSPAN VLAN : 100
        p15 = re.compile(r'^Dest +RSPAN +VLAN :+ (?P<dest_rspan_vlan>(\d+))$')

        # MTU                    : 1464
        p16 = re.compile(r'^MTU +: +(?P<mtu>([0-9]+))$')

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
                src_ports = True
                source_subintfs = False
                continue

            #    TX Only            : Gi0/1/4
            #    Both               : Gi0/1/4
            m = p4_2.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].lower().replace(" ", "_")
                # Set keys
                if src_ports:
                    src_ports_dict[key] = group['src_val']
                elif source_subintfs:
                    source_sub_dict[key] = group['src_val']
                continue

            # Source Subinterfaces:
            m = p5_1.match(line)
            if m:
                source_sub_dict = session_dict.setdefault('source_subinterfaces', {})
                src_ports = False
                source_subintfs = True
                continue

            # Source VLANs           :
            m = p6_1.match(line)
            if m:
                source_vlan_dict = session_dict.setdefault('source_vlans', {})
                continue

            # RX Only            : 20
            m = p6_2.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].lower().replace(" ", "_")
                source_vlan_dict[key] = group['rx_val']
                continue

            # Filter Access-Group: 100
            m = p7.match(line)
            if m:
                session_dict['filter_access_group'] = int(m.groupdict()['filter_access_group'])
                continue

            # Destination Ports      : Gi0/1/6 Gi0/1/2
            m = p8.match(line)
            if m:
                session_dict['destination_ports'] = str(m.groupdict()['destination_ports'])
                continue

            # Destination IP Address : 172.18.197.254
            m = p9.match(line)
            if m:
                session_dict['destination_ip_address'] = str(m.groupdict()['destination_ip_address'])
                continue

            # Destination ERSPAN ID  : 1
            m = p10.match(line)
            if m:
                session_dict['destination_erspan_id'] = str(m.groupdict()['destination_erspan_Id'])
                continue

            # Origin IP Address      : 172.18.197.254
            m = p11.match(line)
            if m:
                session_dict['origin_ip_address'] = str(m.groupdict()['origin_ip_address'])
                continue

            # Source ERSPAN ID       : 1
            m = p12.match(line)
            if m:
                session_dict['source_erspan_id'] = str(m.groupdict()['source_erspan_Id'])
                continue

            # Source IP Address      : 172.18.197.254
            m = p13.match(line)
            if m:
                session_dict['source_ip_address'] = str(m.groupdict()['source_ip_address'])
                continue

            # Source RSPAN VLAN : 100
            m = p14.match(line)
            if m:
                session_dict['source_rspan_vlan'] = int(m.groupdict()['source_rspan_vlan'])
                continue

            # Dest RSPAN VLAN : 100
            m = p15.match(line)
            if m:
                session_dict['dest_rspan_vlan'] = int(m.groupdict()['dest_rspan_vlan'])
                continue

            # MTU                    : 1464
            m = p16.match(line)
            if m:
                session_dict['mtu'] = int(m.groupdict()['mtu'])
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
                     'status': str,
                    },
                'filter_details':
                    {'filter_details_type':str,
                      Optional('source_ip'):str,
                      Optional('destination_ip'): str,
                      Optional('protocol'): str,
                    },
                'buffer_details':
                    {'buffer_type': str,
                     Optional('buffer_size'): int,
                    },
                Optional('file_details'):
                    {Optional('file_name'): str,
                     Optional('file_size'): int,
                     Optional('file_number'): int,
                     Optional('size_of_buffer'): int
                    },
                'limit_details':
                    {'packets_number': int,
                     'packets_capture_duaration': int,
                     'packets_size': int,
                     Optional('maximum_packets_number'): int,
                     Optional('packets_per_second'): int,
                     'packet_sampling_rate': int,
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
        p2_1 = re.compile(r'^Interface: +(?P<interface>([\w\s\/]+)), +Direction *:+ (?P<direction>(\w+))$')

        # Status : Inactive
        p2_2 = re.compile(r'^Status +: +(?P<status>(\w+))$')

        # Filter Details:
        p3=re.compile(r'^Filter +Details:+$')

        # Capture all packets
        # IPv4
        p3_1 = re.compile(r'^(?P<filter_details_type>([\w\s]+))$')

        # Source IP:  any
        p3_2=re.compile(r'^Source +IP: +(?P<source_ip>(\w+))$')

        # Destination IP:  any
        p3_3 = re.compile(r'^Destination +IP: +(?P<destination_ip>(\w+))$')

        #Protocol: any
        p3_4 = re.compile(r'^Protocol: +(?P<protocol>(\w+))$')

        # Buffer Details:
        p4 = re.compile(r'^Buffer +Details:+$')

        # Buffer Type: LINEAR (default)
        p4_1 = re.compile(r'^Buffer +Type: +(?P<buffer_type>(.*))$')

        # Buffer Size (in MB): 10
        p4_2 = re.compile(r'^Buffer +Size +\(in MB\): +(?P<buffer_size>(\d+))$')

        # File Details:
        p5 = re.compile(r'^File +Details:+$')

        # Associated file name: flash:mycap.pcap
        p5_1 = re.compile(r'^Associated +file +name: +(?P<file_name>(.*))$')

        # Total size of files(in MB): 5
        p5_2 = re.compile(r'^Total +size +of +files+\(in MB\): +(?P<file_size>(\d+))$')

        # Number of files in ring: 2
        p5_3 = re.compile(r'^Number +of +files +in +ring: +(?P<file_number>(\d+))$')

        # Size of buffer(in MB): 10
        p5_4 = re.compile(r'^Size +of +buffer+\(in MB\): +(?P<size_of_buffer>(\d+))$')

        # Limit Details:
        p6 = re.compile(r'^Limit +Details:+$')

        # Number of Packets to capture: 0 (no limit)
        p6_1 = re.compile(r'^Number +of +Packets +to +capture: +(?P<packets_number>(\d+))')

        # Packet Capture duration: 0 (no limit)
        p6_2 = re.compile(r'^Packet +Capture +duration: +(?P<packets_capture_duaration>(\d+))')

        # Packet Size to capture: 0 (no limit)
        p6_3 = re.compile(r'^Packet +Size +to +capture: +(?P<packets_size>(\d+))')

        # Maximum number of packets to capture per second: 1000
        p6_4 = re.compile(r'^Maximum +number +of +packets +to +capture +per +second: +(?P<maximum_packets_number>(\d+))$')

        # Packets per second: 0 (no limit)
        p6_5=re.compile(r'Packets +per +second: +(?P<packets_per_second>(\d+))')

        # Packet sampling rate: 0 (no sampling)
        p6_6 = re.compile(r'^Packet +sampling +rate: +(?P<packet_sampling_rate>(\d+))')

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
            m = p2_1.match(line)
            if m:
                target_type_dict['interface'] = str(m.groupdict()['interface'])
                target_type_dict['direction'] = str(m.groupdict()['direction'])
                continue

            # Status : Active
            m = p2_2.match(line)
            if m:
                target_type_dict['status'] = str(m.groupdict()['status'])
                continue

            # Filter Details:
            m=p3.match(line)
            if m:
                filter_dict = status_dict.setdefault('filter_details',{})
                continue

            # Capture all packets
            m = p3_1.match(line)
            if m:
                filter_dict['filter_details_type']=str(m.groupdict()['filter_details_type'])
                continue

            # Source IP:  any
            m = p3_2.match(line)
            if m:
                filter_dict['source_ip'] = str(m.groupdict()['source_ip'])
                continue

            # Destination IP:  any
            m = p3_3.match(line)
            if m:
                filter_dict['destination_ip'] = str(m.groupdict()['destination_ip'])
                continue

            # Protocol: any
            m = p3_4.match(line)
            if m:
                filter_dict['protocol'] = str(m.groupdict()['protocol'])
                continue

            # Buffer Details:
            m = p4.match(line)
            if m:
                buffer_dict = status_dict.setdefault('buffer_details',{})
                continue

            # Buffer Type: LINEAR (default)
            m = p4_1.match(line)
            if m:
                buffer_dict['buffer_type'] = str(m.groupdict()['buffer_type'])
                continue

            # Buffer Size (in MB): 10
            m = p4_2.match(line)
            if m:
                buffer_dict['buffer_size'] = int(m.groupdict()['buffer_size'])
                continue

            # File Details:
            m = p5.match(line)
            if m:
                file_dict = status_dict.setdefault('file_details', {})
                continue

            # Associated file name: flash:mycap.pcap
            m = p5_1.match(line)
            if m:
                file_dict['file_name'] = str(m.groupdict()['file_name'])
                continue

            # Total size of files(in MB): 5
            m = p5_2.match(line)
            if m:
                file_dict['file_size'] = int(m.groupdict()['file_size'])
                continue

            # Number of files in ring: 2
            m = p5_3.match(line)
            if m:
                file_dict['file_number'] = int(m.groupdict()['file_number'])
                continue

            # Size of buffer(in MB): 10
            m = p5_4.match(line)
            if m:
                file_dict['size_of_buffer'] = int(m.groupdict()['size_of_buffer'])
                continue

            # Limit Details:
            m = p6.match(line)
            if m:
                limit_dict = status_dict.setdefault('limit_details', {})
                continue

            # Number of Packets to capture: 0 (no limit)
            m = p6_1.match(line)
            if m:
                limit_dict['packets_number'] = int(m.groupdict()['packets_number'])
                continue

            # Packet Capture duration: 0 (no limit)
            m = p6_2.match(line)
            if m:
                limit_dict['packets_capture_duaration'] = int(m.groupdict()['packets_capture_duaration'])
                continue

            # Packet Size to capture: 0 (no limit)
            m = p6_3.match(line)
            if m:
                limit_dict['packets_size'] = int(m.groupdict()['packets_size'])
                continue

            # Maximum number of packets to capture per second: 1000
            m = p6_4.match(line)
            if m:
                limit_dict['maximum_packets_number'] = int(m.groupdict()['maximum_packets_number'])
                continue

            # Packets per second: 0 (no limit)
            m = p6_5.match(line)
            if m:
                limit_dict['packets_per_second'] = int(m.groupdict()['packets_per_second'])
                continue

            # Packet sampling rate: 0 (no sampling)
            m = p6_6.match(line)
            if m:
                limit_dict['packet_sampling_rate'] = int(m.groupdict()['packet_sampling_rate'])
                continue

        return ret_dict
