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
        'session': {
            Any(): {
                'type':str,
                Optional('status'):str,
                Optional('source_ports'): {
                    Any(): str,
                },
                Optional('source_subinterfaces'): {
                    Any(): str,
                },
                Optional('source_vlans'): {
                    Any():str,
                },
                Optional('source_efps'): {
                    Any():str,
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
        #    RX Only            : 20
        #    RX Only            : Twe2/0/3
        p4_2 = re.compile(r'(?P<key>(TX Only|Both|RX Only)) *: +(?P<src_val>(\S+))$')

        # Source Subinterfaces:
        p5_1 = re.compile(r'^Source +Subinterfaces\s*:$')

        # Source VLANs           :
        p6_1 = re.compile(r'^Source +VLANs +:$')

        # Filter Access-Group: 100
        p7 = re.compile(r'^Filter +Access-Group: +(?P<filter_access_group>(\d+))$')

        # Destination Ports      : Gi0/1/6 Gi0/1/2
        # Destination Ports        : Po24,Po26,Po28,Po30,Po32,Po34,Po36,Po38,Po40,Po46-50
        p8 = re.compile(r'^Destination +Ports +: +(?P<destination_ports>([\w\/\s\-\,\.]+))$')

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

        # Source EFPs           :
        p17 = re.compile(r'^Source +EFPs +:$')

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
                tx_rx_dict = session_dict.setdefault('source_ports', {})
                continue

            # TX Only            : Gi0/1/4
            # Both               : Gi0/1/4
            # RX Only              : Twe2/0/3
            m = p4_2.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].lower().replace(" ", "_")
                # Set keys
                tx_rx_dict[key] = group['src_val']
                continue

            # Source Subinterfaces:
            m = p5_1.match(line)
            if m:
                tx_rx_dict = session_dict.setdefault('source_subinterfaces', {})
                continue

            # Source VLANs           :
            m = p6_1.match(line)
            if m:
                tx_rx_dict = session_dict.setdefault('source_vlans', {})
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

            # Source EFPs              :
            m = p17.match(line)
            if m:
                tx_rx_dict = session_dict.setdefault('source_efps', {})
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


#=================================================
# Schema for 'monitor capture {capture_name} stop'
#=================================================

class MonitorCaptureStopSchema(MetaParser):
    schema = {
        'capture_duration': int,
        'packets_received': int,
        'packets_dropped': int,
        'packets_oversized': int,
        Optional('bytes_dropped_in_asic'): int,
        'stopped_capture_name': str
    }

#=================================================
# Parser for 'monitor capture {capture_name} stop'
#=================================================

class MonitorCaptureStop(MonitorCaptureStopSchema):

    cli_command = 'monitor capture {capture_name} stop'

    def cli(self, capture_name=None, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(capture_name=capture_name))

        # Capture duration - 56 seconds
        p1 = re.compile(r'Capture\sduration\s\-\s+(?P<capture_duration>\d+)\s+seconds')

        # Packets received - 0
        p2 = re.compile(r'Packets\sreceived\s+\-\s+(?P<packets_received>\d+)')

        # Packets dropped - 0
        p3 = re.compile(r'Packets\sdropped\s+\-\s+(?P<packets_dropped>\d+)')

        # Packets oversized - 0
        p4 = re.compile(r'Packets\soversized\s+\-\s+(?P<packets_oversized>\d+)')

        # Bytes dropped in asic - 0
        p5 = re.compile(r'Bytes\sdropped\sin\sasic\s+\-\s+(?P<bytes_dropped_in_asic>\d+)')

        # Stopped capture point : cap1
        p6 = re.compile(r'Stopped\scapture\spoint\s\:\s+(?P<stopped_capture_name>\S+)')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Capture duration - 56 seconds
            m = p1.match(line)
            if m:
                capture_duration = m.groupdict()['capture_duration']
                ret_dict.update({'capture_duration': int(capture_duration)})
                continue

            # Packets received - 0
            m = p2.match(line)
            if m:
                packets_received = m.groupdict()['packets_received']
                ret_dict.update({'packets_received': int(packets_received)})
                continue

            # Packets dropped - 0
            m = p3.match(line)
            if m:
                packets_dropped = m.groupdict()['packets_dropped']
                ret_dict.update({'packets_dropped': int(packets_dropped)})
                continue

            # Packets oversized - 0
            m = p4.match(line)
            if m:
                packets_oversized = m.groupdict()['packets_oversized']
                ret_dict.update({'packets_oversized': int(packets_oversized)})
                continue

            # Bytes dropped in asic - 0
            m = p5.match(line)
            if m:
                bytes_dropped_in_asic = m.groupdict()['bytes_dropped_in_asic']
                ret_dict.update({'bytes_dropped_in_asic': int(bytes_dropped_in_asic)})
                continue

            # Stopped capture point : cap1
            m = p6.match(line)
            if m:
                stopped_capture_name = m.groupdict()['stopped_capture_name']
                ret_dict.update({'stopped_capture_name': stopped_capture_name})
                continue

        return ret_dict

#=================================================
# Schema for 'show monitor capture {capture_name} buffer'
#=================================================

class ShowMonitorCaptureBufferSchema(MetaParser):
    schema = {

        'capture': {
            int: {
                'time': str,
                'scr_mac_address': str,
                'dst_mac_address': str,
                'protocol': str,
                'packet_size': int,
                'data': str,
            },
        }
    }

#=================================================
# Parser for 'show monitor capture {capture_name} buffer'
#=================================================

class ShowMonitorCaptureBuffer(ShowMonitorCaptureBufferSchema):

    cli_command = ['show monitor capture {capture_name} buffer', 'show monitor capture file {path}']

    def cli(self, capture_name="", path="", output=None):
        if output is None:
            if capture_name:
                output = self.device.execute(self.cli_command[0].format(capture_name=capture_name),timeout=180)
            else:
                output = self.device.execute(self.cli_command[1].format(path=path),timeout=180)

        # 1   0.000000 f4:db:e6:5b:97:04 -> 01:80:c2:00:00:00 STP 60 RST. Root = 32768/805/6c:b2:ae:49:6a:40  Cost = 0  Port = 0x8185
        # 2   2.999988     10.1.1.2 -> 233.252.252.127 IPv4 96 Fragmented IP protocol (proto=UDP 17, off=1480, ID=93f1)
        p1 = re.compile(r'^(?P<pck_no>\d+) +(?P<time>[\d\.]+) +(?P<scr_mac_address>[\da-f\:\.]+) +-> +(?P<dst_mac_address>[\da-f\:\.]+) +(?P<protocol>[\w]+) +(?P<packet_size>[0-9]+) +(?P<data>.*)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            # Capture duration - 56 seconds
            m = p1.match(line)
            if m:
                group = m.groupdict()
                pck_no = group.pop('pck_no')
                capture = ret_dict.setdefault('capture', {}).setdefault(int(pck_no), {})
                capture.update({k: v for k, v in group.items() if "packet_size" != k })
                capture.update({"packet_size":int(group['packet_size'])})
                continue
        return ret_dict

# ======================================================
# Schema for 'show monitor capture buffer detailed '
# ======================================================
class ShowMonitorCaptureBufferDetailedSchema(MetaParser):
    schema = {
        'framenumber': {
            Any():{
                Optional('source_ipv4'): str,
                Optional('destination_ipv4'): str, 
                Optional('source_eth'): str, 
                Optional('destination_eth'): str,
                Optional('interface_id'): str,
                Optional('interface_name'): str,
                Optional('encapsulation_type'): str,
                Optional('arrival_time'): str,
                Optional('time_shift_for_this_packet'): str,
                Optional('epoch_time'): str,
                Optional('time_delta_from_previous_captured_frame'): str,
                Optional('time_delta_from_previous_displayed_frame'): str,
                Optional('time_since_reference_or_first_frame'): str,
                Optional('frame_number'): str,
                Optional('frame_length'): str,
                Optional('capture_length'): str,
                Optional('frame_is_marked'): str,
                Optional('frame_is_ignored'): str,
                Optional('protocols_in_frame'): str,
                Optional('type'): str,
                Optional('sgt'): str,
                Optional('destination'): str,
                Optional('source'): str,
                Optional('address'): str,
                Optional('options'): str,
                Optional('version'): str,
                Optional('total_length'): str,
                Optional('identification'): str,
                Optional('flags'): str,
                Optional('fragment_offset'): str,
                Optional('time_to_live'): str,
                Optional('protocol'): str,
                Optional('header_checksum'): str,
                Optional('header_checksum_status'): str,
                Optional('length'): str,
                Optional('time_since_previous_frame'): str,
                Optional('time_since_first_frame'): str,
                Optional('reserved'): str,
                Optional('stream_index'): str,
                Optional('checksum'): str, 
                Optional('source_port'): str, 
                Optional('group_policy_id'): str, 
                Optional('destination_port'): str, 
                Optional('checksum_status'): str,
                Optional('tcp_segment_len'): str,
                Optional('sequence_number'): str,
                Optional('next_sequence_number'): str,
                Optional('acknowledgment_number'): str,
                Optional('window_size_value'): str,
                Optional('calculated_window_size'): str,
                Optional('window_size_scaling_factor'): str,
                Optional('urgent_pointer'): str,
                Optional('bytes_in_flight'): str,
                Optional('bytes_sent_since_last_psh_flag'): str,
                Optional('severity_level'): str,
                Optional('group'): str,
                Optional('the_rto_for_this_segment_was'): str,
                Optional('rto_based_on_delta_from_frame'): str,
                Optional('time_since_first_frame_in_this_tcp_stream'): str,
                Optional('time_since_previous_frame_in_this_tcp_stream'): str,
                Optional('tcp_source_port'): int,
                Optional('tcp_destination_port'): int,
                Optional('tcp_seq_num'): int,
                Optional('tcp_len'): int,
                Optional('udp_source_port'): int,
                Optional('udp_destination_port'): int,
                Optional('next_header'): str,
                Optional('hop_limit'): str,
                Optional('payload_length'): str,
                Optional('source_ipv6'): str,
                Optional('destination_ipv6'): str,
                Optional('vxlan_id'): int,
                Optional('dscp_value'): int,
                Optional('packet_identifier'): str,
                Optional('authenticator'): str,
                Optional('vendor_id'): str,
                Optional('code'): str,
                Optional('destination_address'): str,
                Optional('source_address'): str
            }
        }
    }

# ======================================================
# Parser for 'show monitor capture buffer detailed '
# ======================================================
class ShowMonitorCaptureBufferDetailed(ShowMonitorCaptureBufferDetailedSchema):
    """Parser for 'show monitor capture buffer detailed"""
    cli_command = ['show monitor capture {capture_name} buffer detailed',
                    'show monitor capture {capture_name} buffer display-filter "{filter_criteria}" detailed',
                    'show monitor capture file {path} packet-number {number} detailed']
    
    def cli(self, capture_name="", filter_criteria="",path="", number="", output=None):
        if output is None:
            # Build the command
            if filter_criteria:
                cmd = self.cli_command[1].format(capture_name=capture_name, filter_criteria=filter_criteria)
            elif path and number:
                cmd = self.cli_command[2].format(path=path, number=number)                
            else:
                cmd = self.cli_command[0].format(capture_name=capture_name)
            # Execute the command
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # Frame 1: 1496 bytes on wire (11968 bits), 80 bytes captured (640 bits) on interface /tmp/epc_ws/wif_to_ts_pipe, id 0
        p0 =re.compile(r'^Frame (?P<frame_num>\d+): +(?P<frame_value>[\w\s\(\)\,\/]+)$')

        # Frame Number: 1
        p1 = re.compile(r'^(?P<pattern>[a-zA-Z \[]+): +(?P<value>[\w\s\(\)\:\,\.\/\]\[]+)$')
        
        # Internet Protocol Version 4, Src: 49.1.1.2, Dst: 91.4.1.1
        p2 = re.compile(r'^Internet Protocol Version 4, Src:+\s+(?P<source_ipv4>[\d\.]+)+, Dst:+\s+(?P<destination_ipv4>[\.\d]+)$')

        # Ethernet II, Src: fa:88:8e:78:00:02 (fa:88:8e:78:00:02), Dst: 00:a7:42:86:06:bf (00:a7:42:86:06:bf)
        p3=re.compile(r'^Ethernet II, Src:+\s+(?P<source_eth>[\:\w\)\( ]+)+, Dst:+\s+(?P<destination_eth>[\:\w\(\) ]+)$')

        # Transmission Control Protocol, Src Port: 0, Dst Port: 0, Seq: 1, Len: 942
        p4 = re.compile(r'^Transmission Control Protocol, Src Port:+\s+(?P<tcp_source_port>[\d]+)+, Dst Port:+\s+(?P<tcp_destination_port>[\d]+)+, Seq:+\s+(?P<tcp_seq_num>[\d]+)+, Len:+\s+(?P<tcp_len>[\d]+)$')

        # User Datagram Protocol, Src Port: 65473, Dst Port: 4789
        p5 = re.compile(r'^User Datagram Protocol, Src Port:+\s+(?P<udp_source_port>[\d]+)+, Dst Port:+\s+(?P<udp_destination_port>[\d]+)$')

        # Internet Protocol Version 6, Src: 2000:10::10, Dst: 2000:14::20
        p6 = re.compile(r'^Internet Protocol Version 6, Src:+\s+(?P<source_ipv6>[\d\:]+)+, Dst:+\s+(?P<destination_ipv6>[\:\d]+)$')
        
        # VXLAN Network Identifier (VNI): 50000
        p7 = re.compile(r'^VXLAN +Network +Identifier +\(VNI+\): +(?P<vxlan_id>(\d+))$')

        #     1010 00.. = Differentiated Services Codepoint: Class Selector 5 (40)
        p8 = re.compile(r'^[\S\s]+\s+= Differentiated Services Codepoint: [\s\S]+ \((?P<dscp_value>\d+)\)$')

        # loop to split lines of output
        for line in output.splitlines():
            line = line.strip()

            # Frame 1: 1496 bytes on wire (11968 bits), 80 bytes captured (640 bits) on interface /tmp/epc_ws/wif_to_ts_pipe, id 0
            m = p0.match(line)
            if m:
                groups = m.groupdict()
                framenumber = int(groups["frame_num"])
                result_dict = ret_dict.setdefault('framenumber', {}).setdefault(framenumber, {})
                continue

            # Frame Number: 1
            # Capture Length: 80 bytes (640 bits)
            # [Frame is marked: False]
            # Encapsulation type: Ethernet [1]
            m = p1.match(line)
            if m:
                group = m.groupdict()
                scrubbed = (group['pattern'].strip()).replace(' ', '_').replace('[', '')
                result_dict.update({scrubbed.lower(): (group['value'].replace(']', '').replace('[', ''))})
                continue
            
            # Internet Protocol Version 4, Src: 49.1.1.2, Dst: 91.4.1.1
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                result_dict.update({
                    "source_ipv4":groups['source_ipv4'],
                    "destination_ipv4":groups['destination_ipv4']
                    })
                continue

            # Ethernet II, Src: fa:88:8e:78:00:02 (fa:88:8e:78:00:02), Dst: 00:a7:42:86:06:bf (00:a7:42:86:06:bf)
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                result_dict.update({
                    "source_eth":groups['source_eth'],
                    "destination_eth":groups['destination_eth']
                    })
                continue

            # Transmission Control Protocol, Src Port: 0, Dst Port: 0, Seq: 1, Len: 942
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                result_dict.update({
                    "tcp_source_port":int(groups['tcp_source_port']),
                    "tcp_destination_port":int(groups['tcp_destination_port']),
                    "tcp_seq_num":int(groups['tcp_seq_num']),
                    "tcp_len":int(groups['tcp_len'])
                    })
                continue

            # User Datagram Protocol, Src Port: 65473, Dst Port: 4789
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                result_dict.update({
                    "udp_source_port":int(groups['udp_source_port']),
                    "udp_destination_port":int(groups['udp_destination_port'])
                    })
                continue

            # Internet Protocol Version 6, Src: 2000:10::10, Dst: 2000:14::20
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                result_dict.update({
                    "source_ipv6":groups['source_ipv6'],
                    "destination_ipv6":groups['destination_ipv6']
                    })
                continue

            # VXLAN Network Identifier (VNI): 50000
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                result_dict.update({"vxlan_id":int(groups['vxlan_id'])})
                continue
            
            # 1010 00.. = Differentiated Services Codepoint: Class Selector 5 (40)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                result_dict.update({"dscp_value":int(group['dscp_value'])})
                continue

        return ret_dict