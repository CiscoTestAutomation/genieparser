''' show_monitor.py

IOSXE parsers for the following show commands:
    * show monitor
    * show monitor session {session}
    * show monitor capture
    * show monitor event-trace crypto pki event all
    * show monitor event-trace crypto pki error all
    * show monitor event-trace crypto ikev2 event all
    * show monitor event-trace crypto all detail
    * show monitor event-trace crypto from-boot 
    * show monitor event-trace crypto from-boot {timer}

'''


# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, ListOf


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
    '''

    cli_command = ['show monitor', 'show monitor session {session}']

    def cli(self, session="", output=None):
        if output is None:
            if session:
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
                Optional('source_address'): str,
                Optional('dhcp_message_type'): str,
                Optional('message_type_boot_reply'): str,
                Optional('hardware_type'): str,
                Optional('hardware_address_length'): str,
                Optional('hops'): str,
                Optional('transaction_id'): str,
                Optional('seconds_elapsed'): str,
                Optional('bootp_flags'): str,
                Optional('client_ip_address'): str,
                Optional('your_ip_address'): str,
                Optional('next_server_ip_address'): str,
                Optional('relay_agent_ip_address'): str,
                Optional('client_mac_address'): str,
                Optional('client_hardware_address_padding'): str,
                Optional('server_host_name'): str,
                Optional('boot_file_name'): str,
                Optional('magic_cookie'): str,
                Optional('dhcp_option_53_message_type'): str,
                Optional('dhcp_option_53_length'): int,
                Optional('dhcp_option_53_dhcp'): str,
                Optional('dhcp_option_61_client_identifier'): str,
                Optional('dhcp_option_61_length'): int,
                Optional('dhcp_option_61_hardware_type'): str,
                Optional('dhcp_option_61_client_mac_address'): str,
                Optional('dhcp_option_12_host_name'): str,
                Optional('dhcp_option_12_length'): int,
                Optional('dhcp_option_12_host_name_value'): str,
                Optional('dhcp_option_255_end'): str,
                Optional('dhcp_option_255_option_end'): int,
                Optional('dhcp_padding'): str,
                Optional('dhcp'): str,
                Optional('option'): str,
                Optional('option_end'): str,
                Optional('padding'): str,
                Optional('message_type'): str,
                Optional('host_name'): str,
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
        if number:
            number = int(number)
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

        # DHCP Option: (53) DHCP Message Type (Discover)
        p9 = re.compile(r'^Option: +\(53\) +DHCP +Message +Type +\((?P<dhcp_option_53_message_type>[\w]+)\)$')

        # DHCP Option Length: 1
        p10 = re.compile(r'^Length: +(?P<dhcp_option_53_length>\d+)$')

        # DHCP: Discover (1)
        p11 = re.compile(r'^DHCP: +(?P<dhcp_option_53_dhcp>[\w]+) +\((?P<dhcp_option_53_dhcp_value>\d+)\)$')

        # DHCP Option: (61) Client identifier
        p12 = re.compile(r'^Option: +\(61\) +Client +identifier$')

        # DHCP Option Length: 7
        p13 = re.compile(r'^Length: +(?P<dhcp_option_61_length>\d+)$')

        # Hardware type: Ethernet (0x01)
        p14 = re.compile(r'^Hardware +type: +(?P<dhcp_option_61_hardware_type>[\w]+) +\((?P<dhcp_option_61_hardware_type_value>[\w]+)\)$')

        # Client MAC address: 54:00:04:de:91:23 (54:00:04:de:91:23)
        p15 = re.compile(r'^Client +MAC +address: +(?P<dhcp_option_61_client_mac_address>[\w\:]+) +\((?P<dhcp_option_61_client_mac_address_value>[\w\:]+)\)$')

        # DHCP Option: (12) Host Name
        p16 = re.compile(r'^Option: +\(12\) +Host +Name$')

        # DHCP Option Length: 11
        p17 = re.compile(r'^Length: +(?P<dhcp_option_12_length>\d+)$')

        # Host Name: Tesgine2000
        p18 = re.compile(r'^Host +Name: +(?P<dhcp_option_12_host_name_value>[\w]+)$')

        # DHCP Option: (255) End
        p19 = re.compile(r'^Option: +\(255\) +End$')

        # Option End: 255
        p20 = re.compile(r'^Option +End: +(?P<dhcp_option_255_option_end>\d+)$')

        # Padding: 000000000000000000
        p21 = re.compile(r'^Padding: +(?P<dhcp_padding>[\w]+)$')

        
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

            # DHCP Option: (53) DHCP Message Type (Discover)
            m = p9.match(line)
            if m:
                group = m.groupdict()
                result_dict.update({"dhcp_option_53_message_type": group['dhcp_option_53_message_type']})
                continue

            # DHCP Option Length: 1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                result_dict.update({"dhcp_option_53_length": int(group['dhcp_option_53_length'])})
                continue

            # DHCP: Discover (1)
            m = p11.match(line)
            if m:
                group = m.groupdict()
                result_dict.update({"dhcp_option_53_dhcp": group['dhcp_option_53_dhcp']})
                continue

            # DHCP Option: (61) Client identifier
            m = p12.match(line)
            if m:
                result_dict.update({"dhcp_option_61_client_identifier": "Client identifier"})
                continue

            # DHCP Option Length: 7
            m = p13.match(line)
            if m:
                group = m.groupdict()
                result_dict.update({"dhcp_option_61_length": int(group['dhcp_option_61_length'])})
                continue

            # Hardware type: Ethernet (0x01)
            m = p14.match(line)
            if m:
                group = m.groupdict()
                result_dict.update({"dhcp_option_61_hardware_type": group['dhcp_option_61_hardware_type']})
                continue

            # Client MAC address: 54:00:04:de:91:23 (54:00:04:de:91:23)
            m = p15.match(line)
            if m:
                group = m.groupdict()
                result_dict.update({"dhcp_option_61_client_mac_address": group['dhcp_option_61_client_mac_address']})
                continue

            # DHCP Option: (12) Host Name
            m = p16.match(line)
            if m:
                result_dict.update({"dhcp_option_12_host_name": "Host Name"})
                continue

            # DHCP Option Length: 11
            m = p17.match(line)
            if m:
                group = m.groupdict()
                result_dict.update({"dhcp_option_12_length": int(group['dhcp_option_12_length'])})
                continue

            # Host Name: Tesgine2000
            m = p18.match(line)
            if m:
                group = m.groupdict()
                result_dict.update({"dhcp_option_12_host_name_value": group['dhcp_option_12_host_name_value']})
                continue

            # DHCP Option: (255) End
            m = p19.match(line)
            if m:
                result_dict.update({"dhcp_option_255_end": "End"})
                continue

            # Option End: 255
            m = p20.match(line)
            if m:
                group = m.groupdict()
                result_dict.update({"dhcp_option_255_option_end": int(group['dhcp_option_255_option_end'])})
                continue

            # Padding: 000000000000000000
            m = p21.match(line)
            if m:
                group = m.groupdict()
                result_dict.update({"dhcp_padding": group['dhcp_padding']})
                continue

        return ret_dict
    
# =========================================
# Schema for 'show monitor capture {capture_name} capture-statistics'
# =========================================
class ShowMonitorCaptureStatisticsSchema(MetaParser):

    ''' Schema for     
                    "show monitor capture <capture_name> capture-statistics" '''

    schema = {
        'capture_statistics_collected_at_software':
                {
                'capture_duration': int,
                'packets_received': int,
                'packets_dropped': int,
                'packets_oversized': int,
                'packets_errored' : int,
                'packets_sent' : int,
                'bytes_received' : int,
                'bytes_dropped' : int,
                'bytes_oversized' : int,
                'bytes_errored' : int,
                'bytes_sent' : int
                    
                },
            }

# =========================================
# Parser for 'show monitor capture {capture_name} capture-statistics'
# =========================================
class ShowMonitorCaptureStatistics(ShowMonitorCaptureStatisticsSchema):
    ''' Parser for
        "show monitor capture <capture_name> capture-statistics" '''

    cli_command = ['show monitor capture {capture_name} capture-statistics']

    def cli(self, capture_name=None, output=None):
        if output is None:
            # Execute command on device
            out = self.device.execute(self.cli_command[0].format(capture_name=capture_name))
        else:
            out = output

        # Init vars
        ret_dict = {}

        # Capture_statistics_collected_at_software
        p1 = re.compile(r'^capture\s+statistics\s+collected\s+at\s+software:$')

        # capture duration
        p2 = re.compile(r'^capture +duration +- +(?P<capture_duration>(\d+)) +seconds$')

        # Packets received
        p3 = re.compile(r'^packets +received +- +(?P<packets_received>(\d+))$')

        # Packets dropped
        p4 = re.compile(r'^packets +dropped +- +(?P<packets_dropped>(\d+))$')

        # Packets oversized
        p5 = re.compile(r'^packets +oversized +- +(?P<packets_oversized>(\d+))$')

        # Packets errored
        p6 = re.compile(r'^packets +errored +- +(?P<packets_errored>(\d+))$')

        # Packets sent
        p7 = re.compile(r'^packets +sent +- +(?P<packets_sent>(\d+))$')

        # Bytes received
        p8 = re.compile(r'^bytes +received +- +(?P<bytes_received>(\d+))$')

        # Bytes dropped
        p9 = re.compile(r'^bytes +dropped +- +(?P<bytes_dropped>(\d+))$')

        #Bytes oversized
        p10 = re.compile(r'^bytes +oversized +- +(?P<bytes_oversized>(\d+))$')

        #Bytes errored
        p11 = re.compile(r'^bytes +errored +- +(?P<bytes_errored>(\d+))$')

        #Bytes sent
        p12 = re.compile(r'^bytes +sent +- +(?P<bytes_sent>(\d+))$')
        

        for line in out.splitlines():
            line = line.strip()
            
            # Capture_statistics_collected_at_software
            m = p1.match(line)
            if m:
                group = m.groupdict()
                cap_dict = ret_dict.setdefault('capture_statistics_collected_at_software', {})      

            # Capture_duration
            m = p2.match(line)
            if m:
                group = m.groupdict()
                cap_dict.setdefault('capture_duration', int(group['capture_duration']))
                continue

            # Packets_received
            m = p3.match(line)
            if m:
                group = m.groupdict()
                cap_dict.setdefault('packets_received', int(group['packets_received']))
                continue

            # Packets_dropped
            m = p4.match(line)
            if m:
                group = m.groupdict()
                cap_dict.setdefault('packets_dropped', int(group['packets_dropped']))
                continue

            # Packets_oversized
            m = p5.match(line)
            if m:
                group = m.groupdict()
                cap_dict.setdefault('packets_oversized', int(group['packets_oversized']))
                continue

            # Packets_errored
            m = p6.match(line)
            if m:
                group = m.groupdict()
                cap_dict.setdefault('packets_errored', int(group['packets_errored']))
                continue
            
            # Packets_sent
            m = p7.match(line)
            if m:
                group = m.groupdict()
                cap_dict.setdefault('packets_sent', int(group['packets_sent']))
                continue

            # Bytes_received
            m = p8.match(line)
            if m:
                group = m.groupdict()
                cap_dict.setdefault('bytes_received', int(group['bytes_received']))
                continue

            # Bytes_dropped
            m = p9.match(line)
            if m:
                group = m.groupdict()
                cap_dict.setdefault('bytes_dropped', int(group['bytes_dropped']))
                continue

            # Bytes_oversized
            m = p10.match(line)
            if m:
                group = m.groupdict()
                cap_dict.setdefault('bytes_oversized', int(group['bytes_oversized']))
                continue

            # Bytes_errored
            m = p11.match(line)
            if m:
                group = m.groupdict()
                cap_dict.setdefault('bytes_errored', int(group['bytes_errored']))
                continue

            # Bytes_sent
            m = p12.match(line)
            if m:
                group = m.groupdict()
                cap_dict.setdefault('bytes_sent', int(group['bytes_sent']))
                continue

        return ret_dict

class ShowMonitorEventTraceDmvpnAllSchema(MetaParser):
    schema = {
        Any(): {
            Optional(Any()): {
                'event': str,
                Optional('tunnel'): str,
                Optional('target'): str,
                Optional('nbma_src'): str,
                Optional('vpn_src'): str,
                Optional('nbma_dest'): str,
                Optional('vpn_dest'): str,
                Optional('vrf'): str,
                Optional('vrf_id'): str,
                Optional('reqid'): str,
                Optional('ivl'): str,
                Optional('label'): str,
                Optional('reason'): str,
                Optional('err_code'): str,
                Optional('old'): str,
                Optional('new'): str
            },
        }
    }

class ShowMonitorEventTraceDmvpnAll(ShowMonitorEventTraceDmvpnAllSchema):
    """
    Parser for
        * 'show monitor event-trace dmvpn all'
    """

    cli_command = ['show monitor event-trace dmvpn all']

    # Defines a function to run the cli_command
    def cli(self, output=None):
        if output is None:
            # get output from device
            output = self.device.execute(self.cli_command[0])

        # initial return dictionary
        ret_dict = {}

        '''*Jun 22 06:39:28.358: NHRP-CACHE-ADD tunnel: Tu1 target: 
            192.168.10. nbma_src: 1.1.1.1 vpn_src: 192.168.10.1 nbma_dest: 
            3.3.3.1 vpn_dest: 192.168.10.3 vrf: global(0x0) label: none'''
        p0 = re.compile(r"\*(?P<time_stamp>[A-z0-9\s\d:.]+) "
            r"(?P<event>NHRP-CACHE-ADD) tunnel: (?P<tunnel>[A-z0-9]+) "
            r"target: (?P<target>[0-9.]+) nbma_src: (?P<nbma_src>[0-9.]+) "
            r"vpn_src: (?P<vpn_src>[0-9.]+) nbma_dest: (?P<nbma_dest>[0-9.]+) "
            r"vpn_dest: (?P<vpn_dest>[0-9.]+) vrf: (?P<vrf>[a-z0()]+) "
            r"label: (?P<label>[a-z]+)")

        '''*Jun 22 06:39:28.361: NHRP-NHC-UP tunnel: Tu1 NHC up nbma_src: 
            1.1.1.1 vpn_src: 192.168.10.1 nbma_dest: 3.3.3.1 vpn_dest: 
            192.168.10.3 vrf: global(0x0)'''        
        p1 = re.compile(r"\*(?P<time_stamp>[A-z0-9\s\d:.]+) "
            r"(?P<event>NHRP-NHC-UP) tunnel: (?P<tunnel>[A-z0-9]+) NHC up "
            r"nbma_src: (?P<nbma_src>[0-9.]+) vpn_src: (?P<vpn_src>[0-9.]+) "
            r"nbma_dest: (?P<nbma_dest>[0-9.]+) vpn_dest: "
            r"(?P<vpn_dest>[0-9.]+) vrf: (?P<vrf>[A-Za-z0()]+)")

        '''*Jun 22 06:39:28.362: NHRP-TUNNEL-ENDPOINT-ADD tunnel: Tu1 Added 
            tunnel endpoints nbma_dest: 3.3.3.1 vpn_dest: 192.168.10.3'''
        '''*Jul 27 07: 30: 25.534: NHRP-TUNNEL-ENDPOINT-ADD tunnel: Tu1 add/update 
            tunnel endpoints nbma_dest: 1.1.1.1 vpn_dest: 192.168.10.1'''
        p2 = re.compile(r"\*(?P<time_stamp>[A-z0-9\s\d:.]+) "
            r"(?P<event>NHRP-TUNNEL-ENDPOINT-ADD) tunnel: "
            r"(?P<tunnel>[A-z0-9]+) ([A-za-z/]+) tunnel endpoints nbma_dest: "
            r"(?P<nbma_dest>[0-9.]+) vpn_dest: (?P<vpn_dest>[0-9.]+)")

        '''*Jun 22 06:39:28.930: NHRP-NHS-UP tunnel: Tu1 NHS up nbma_src: 
            2.2.2.1 vpn_src: 192.168.10.2 nbma_dest: 1.1.1.1 vpn_dest: 
            192.168.10.1 vrf: global(0x0)'''        
        p3 = re.compile(r"\*(?P<time_stamp>[A-z0-9\s\d:.]+) "
            r"(?P<event>NHRP-NHS-UP) tunnel: (?P<tunnel>[A-z0-9]+) NHS up "
            r"nbma_src: (?P<nbma_src>[0-9.]+) vpn_src: (?P<vpn_src>[0-9.]+) "
            r"nbma_dest: (?P<nbma_dest>[0-9.]+) vpn_dest: "
            r"(?P<vpn_dest>[0-9.]+) vrf: (?P<vrf>[A-Za-z0()]+)")

        '''*Jun 22 06:51:10.254: NHRP-RECV-RES-REQ tunnel: Tu1 host with
            nbma_src: 1.1.1.1 vpn_src: 192.168.10.3 received resolution 
            request from nbma_dest: 2.2.2.1 vpn_dest: 192.168.10.2 vrf: 
            global(0x0) label: none'''        
        p4 = re.compile(r"\*(?P<time_stamp>[A-z0-9\s\d:.]+) "
            r"(?P<event>NHRP-RECV-RES-REQ) tunnel: (?P<tunnel>[A-z0-9]+) host "
            r"with nbma_src: (?P<nbma_src>[0-9.]+) vpn_src: "
            r"(?P<vpn_src>[0-9.]+) received resolution request from nbma_dest: "
            r"(?P<nbma_dest>[0-9.]+) vpn_dest: (?P<vpn_dest>[0-9.]+) vrf: "
            r"(?P<vrf>[A-Za-z0()]+) label: (?P<label>[a-z]+)")

        '''*Jun 23 12:56:43.560: NHRP-SEND-RES-REQ tunnel: Tu1 host with 
            nbma_src: 2.2.2.1 vpn_src: 192.168.10.2 send resolution request 
            to nbma_dest: 1.1.1.1 vpn_dest: 192.168.10.3 vrf: global(0x0) 
            label: none'''        
        p5 = re.compile(r"\*(?P<time_stamp>[A-z0-9\s\d:.]+) "
            r"(?P<event>NHRP-SEND-RES-REQ) tunnel: (?P<tunnel>[A-z0-9]+) host "
            r"with nbma_src: (?P<nbma_src>[0-9.]+) vpn_src: "
            r"(?P<vpn_src>[0-9.]+) send resolution request to nbma_dest: "
            r"(?P<nbma_dest>[0-9.]+) vpn_dest: (?P<vpn_dest>[0-9.]+) vrf: "
            r"(?P<vrf>[A-Za-z0()]+) label: (?P<label>[a-z]+)")

        '''*Jun 23 12:56:43.568: NHRP-RECV-RES-REPLY tunnel: Tu1 host with 
            nbma_src: 2.2.2.1 vpn_src: 192.168.10.2 received resolution reply 
            from nbma_dest: 3.3.3.1 vpn_dest: 192.168.10.3 vrf: global(0x0) 
            label: none'''        
        p6 = re.compile(r"\*(?P<time_stamp>[A-z0-9\s\d:.]+) "
            r"(?P<event>NHRP-RECV-RES-REPLY) tunnel: (?P<tunnel>[A-z0-9]+) "
            r"host with nbma_src: (?P<nbma_src>[0-9.]+) vpn_src: "
            r"(?P<vpn_src>[0-9.]+) received resolution reply from nbma_dest: "
            r"(?P<nbma_dest>[0-9.]+) vpn_dest: (?P<vpn_dest>[0-9.]+) vrf: "
            r"(?P<vrf>[A-Za-z0()]+) label: (?P<label>[a-z]+)")

        '''*Jun 23 12:56:43.712: NHRP-SEND-RES-REPLY tunnel: Tu1 host with 
            nbma_src: 3.3.3.1 vpn_src: 192.168.10.3 send resolution reply to 
            nbma_dest: 2.2.2.1 vpn_dest: 192.168.10.2 vrf: global(0x0) 
            label: illegal'''        
        p8 = re.compile(r"\*(?P<time_stamp>[A-z0-9\s\d:.]+) "
            r"(?P<event>NHRP-SEND-RES-REPLY) tunnel: (?P<tunnel>[A-z0-9]+) "
            r"host with nbma_src: (?P<nbma_src>[0-9.]+) vpn_src: "
            r"(?P<vpn_src>[0-9.]+) send resolution reply to nbma_dest: "
            r"(?P<nbma_dest>[0-9.]+) vpn_dest: (?P<vpn_dest>[0-9.]+) vrf: "
            r"(?P<vrf>[A-Za-z0()]+) label: (?P<label>[a-z]+)")

        '''*Jun 22 07:02:43.481: NHRP-RECV-PURGE-REQ tunnel: Tu1 host 
            with nbma_src: 1.1.1.1 vpn_src: 192.168.10.1 receive purge 
            request from nbma_dest: 3.3.3.1 vpn_dest: 192.168.10.3 vrf: 
            global(0x0) label: explicit-null'''        
        p9 = re.compile(r"\*(?P<time_stamp>[A-z0-9\s\d:.]+) "
            r"(?P<event>NHRP-RECV-PURGE-REQ) tunnel: (?P<tunnel>[A-z0-9]+) "
            r"host with nbma_src: (?P<nbma_src>[0-9.]+) vpn_src: "
            r"(?P<vpn_src>[0-9.]+) receive purge request from nbma_dest: "
            r"(?P<nbma_dest>[0-9.]+) vpn_dest: (?P<vpn_dest>[0-9.]+) vrf: "
            r"(?P<vrf>[A-Za-z0()]+) label: (?P<label>[a-z-]+)")

        '''*Jun 22 07:06:10.841: NHRP-SEND-PURGE-REQ tunnel: Tu1 host with 
            nbma_src: 3.3.3.1 vpn_src: 0.0.0.0 send purge request to nbma_dest: 
            UNKNOWN vpn_dest: 192.168.10.1 vrf: global(0x0) label: none'''        
        p10 = re.compile(r"\*(?P<time_stamp>[A-z0-9\s\d:.]+) "
            r"(?P<event>NHRP-SEND-PURGE-REQ) tunnel: (?P<tunnel>[A-z0-9]+) "
            r"host with nbma_src: (?P<nbma_src>[0-9.]+) vpn_src: "
            r"(?P<vpn_src>[0-9.]+) send purge request to nbma_dest: "
            r"(?P<nbma_dest>[A-Z0-9.]+) vpn_dest: (?P<vpn_dest>[0-9.]+) "
            r"vrf: (?P<vrf>[A-Za-z0()]+) label: (?P<label>[a-z]+)")

        '''NHRP-NHC-DOWN tunnel: Tu1 NHC down nbma_src: 1.1.1.1 vpn_src: 
            192.168.10.1 nbma_dest: 2.2.2.1 vpn_dest: 192.168.10.2 vrf: 
            global(0x0) reason: EXT - Tunnel Interface AdminDown'''        
        p11 = re.compile(r"\*(?P<time_stamp>[A-z0-9\s\d:.]+) "
            r"(?P<event>NHRP-NHC-DOWN) tunnel: (?P<tunnel>[A-z0-9]+) NHC down "
            r"nbma_src: (?P<nbma_src>[0-9.]+) vpn_src: (?P<vpn_src>[0-9.]+) "
            r"nbma_dest: (?P<nbma_dest>[0-9.]+) vpn_dest: "
            r"(?P<vpn_dest>[0-9.]+) vrf: (?P<vrf>[A-Za-z0()]+) reason: "
            r"(?P<reason>[A-z\s-]+)")

        '''*Jun 22 08:56:36.794: NHRP-TUNNEL-ENDPOINT-DELETE tunnel: 
            Tu1 Deleting tunnel endpoints nbma_dest: 3.3.3.1 vpn_dest: 
            192.168.10.3'''        
        p12 = re.compile(r"\*(?P<time_stamp>[A-z0-9\s\d:.]+) "
            r"(?P<event>NHRP-TUNNEL-ENDPOINT-DELETE) tunnel: "
            r"(?P<tunnel>[A-z0-9]+) Deleting tunnel endpoints nbma_dest: "
            r"(?P<nbma_dest>[0-9.]+) vpn_dest: (?P<vpn_dest>[0-9.]+)")

        '''*Jun 22 08:59:28.070: NHRP-NHS-DOWN tunnel: Tu1 NHS down 
            nbma_src: 2.2.2.1 vpn_src: 192.168.10.2 nbma_dest: 1.1.1.1 
            vpn_dest: 192.168.10.1 vrf: global(0x0) reason: NHRP - 
            Registration Failure'''
        p13 = re.compile(r"\*(?P<time_stamp>[A-z0-9\s\d:.]+) "
            r"(?P<event>NHRP-NHS-DOWN) tunnel: (?P<tunnel>[A-z0-9]+) NHS "
            r"down nbma_src: (?P<nbma_src>[0-9.]+) vpn_src: "
            r"(?P<vpn_src>[0-9.]+) nbma_dest: (?P<nbma_dest>[0-9.]+) "
            r"vpn_dest: (?P<vpn_dest>[0-9.]+) vrf: (?P<vrf>[A-Za-z0()]+) "
            r"reason: (?P<reason>[A-z\s-]+)")

        '''*Jun 22 08:59:28.071: NHRP-NHS-RECOVERY-NHS-STATE  NHS vpn_dest: 
            192.168.10.1 Tunnel1 vrf 0 cluster 0 priority 0 transitioned to 
            'expecting replies' from 'responding expecting replies'''
        '''*Jul 27 07: 30: 34.496: NHRP-NHS-RECOVERY-NHS-STATE  NHS vpn_dest: 192.168.10.1 
            Tunnel1 vrf: global(0x0) cluster 0 priority 0 transitioned to 'responding 
            expecting replies' from 'expecting replies'''
        p14 = re.compile(r"\*(?P<time_stamp>[A-z0-9\s\d:.]+) "
            r"(?P<event>NHRP-NHS-RECOVERY-NHS-STATE)  NHS vpn_dest: "
            r"(?P<vpn_dest>[0-9.]+) ([A-z0-9]+) ([a-z:]+) (?P<vrf>[A-Za-z0()]+) cluster "
            r"(?P<cluster>[0-9]+) priority (?P<priority>[0-9]+) transitioned "
            r"to ([a-z' ]+)")

        '''*Jun 22 08:59:56.133: NHRP-CTRL-PLANE-RETRANS tunnel: Tu1 
            retransmitting registration request for vpn_dest: 192.168.10.1 
            reqid 2819 retrans ivl 2 sec vrf: NONE label: explicit-null'''
        '''*Aug 14 05: 06: 47.622: NHRP-CTRL-PLANE-RETRANS tunnel: Tu1 
           retransmitting Registration Request for vpn_dest: 192.168.10.1 reqid 
           4 retrans 2 sec vrf: global (0x0) label: explicit-null'''
        p15 = re.compile(r"\*(?P<time_stamp>[A-z0-9\s\d:.]+) "
            r"(?P<event>NHRP-CTRL-PLANE-RETRANS) tunnel: "
            r"(?P<tunnel>[A-z0-9]+) retransmitting ([A-za-z]+) ([A-za-z]+) for "
            r"vpn_dest: (?P<vpn_dest>[0-9.]+) reqid (?P<reqid>[0-9]+) ([a-z ]+) "
            r"(?P<ivl>[0-9]+) sec vrf: (?P<vrf>[A-Za-z0()]+) label: "
            r"(?P<label>[a-z-]+)")

        '''*Jun 23 13:51:22.428: NHRP-NHP-DOWN tunnel: Tu1 NHP down 
            nbma_src: 2.2.2.1 vpn_src: 192.168.10.2 nbma_dest: 3.3.3.1 
            vpn_dest: 192.168.10.3 vrf: global(0x0) reason: No Reason'''
        '''*Aug 15 13: 59: 48.248: NHRP-NHP-DOWN tunnel: Tu1 NHP down nbma_src: 
            2.2.2.1 vpn_src: 192.168.10.2 nbma_dest: 3.3.3.1 vpn_dest: 192.168.10.3 
            vrf: global (0x0) reason: NHRP - Hold time expiry'''
        p18 = re.compile(r"\*(?P<time_stamp>[A-z0-9\s\d:.]+) "
            r"(?P<event>NHRP-NHP-DOWN) tunnel: (?P<tunnel>[A-z0-9]+) NHP down "
            r"nbma_src: (?P<nbma_src>[0-9.]+) vpn_src: (?P<vpn_src>[0-9.]+) "
            r"nbma_dest: (?P<nbma_dest>[0-9.]+) vpn_dest: "
            r"(?P<vpn_dest>[0-9.]+) vrf: (?P<vrf>[A-Za-z0()]+) reason: "
            r"(?P<reason>[A-z\s-]+)")

        '''*Jun 24 09:09:36.455: NHRP-CACHE-DELETE tunnel: Tu1 nbma_src: 
            1.1.1.1 vpn_src: 192.168.10.1 nbma_dest: 2.2.2.1 vpn_dest: 
            192.168.10. vrf: global(0x0) label: none reason: 
            EXT - Tunnel Interface AdminDown'''        
        p20 = re.compile(r"\*(?P<time_stamp>[A-z0-9\s\d:.]+) "
            r"(?P<event>NHRP-CACHE-DELETE) tunnel: (?P<tunnel>[A-z0-9]+) "
            r"nbma_src: (?P<nbma_src>[0-9.]+) vpn_src: (?P<vpn_src>[0-9.]+) "
            r"nbma_dest: (?P<nbma_dest>[0-9.]+) vpn_dest: "
            r"(?P<vpn_dest>[0-9.]+) vrf: (?P<vrf>[A-Za-z0()]+) label: "
            r"(?P<label>[a-z-]+) reason: (?P<reason>[A-z\s-]+)")

        '''*Jun 26 18:38:52.148: NHRP-CACHE-UPDATE tunnel: Tu1 target: 
            192.168.10. nbma_src: 2.2.2.1 vpn_src: 192.168.10.2 nbma_dest: 
            1.1.1.1 vpn_dest: 192.168.10.3 vrf: global(0x0) label: none'''        
        p21 = re.compile(r"\*(?P<time_stamp>[A-z0-9\s\d:.]+) "
            r"(?P<event>NHRP-CACHE-UPDATE) tunnel: (?P<tunnel>[A-z0-9]+) "
            r"target: (?P<target>[0-9.]+) nbma_src: (?P<nbma_src>[0-9.]+) "
            r"vpn_src: (?P<vpn_src>[0-9.]+) nbma_dest: (?P<nbma_dest>[0-9.]+) "
            r"vpn_dest: (?P<vpn_dest>[0-9.]+) vrf: (?P<vrf>[A-Za-z0()]+) label: "
            r"(?P<label>[a-z-]+)")

        '''*Jun 27 17:48:34.466: NHRP-CACHE-NBMA-NHOP-CHANGE tunnel: Tu1 
            cache address change nbma old: 1.1.1.1 -> new: 3.3.3.1'''        
        p22 = re.compile(r"\*(?P<time_stamp>[A-z0-9\s\d:.]+) "
            r"(?P<event>NHRP-CACHE-NBMA-NHOP-CHANGE) tunnel: "
            r"(?P<tunnel>[A-z0-9]+) cache address change nbma old: "
            r"(?P<old>[0-9.]+) -> new: (?P<new>[0-9.]+)")

        '''Jul  2 16:35:19.386: NHRP-RECV-PURGE-REPLY tunnel: Tu1 host with
            nbma_src: 2.2.2.1 vpn_src: 192.168.10.2 receive purge reply from 
            nbma_dest: 2.2.2.1 vpn_dest: 192.168.10.3 vrf: global(0x0) 
            label: none'''        
        p23 = re.compile(r"\*(?P<time_stamp>[A-z0-9\s\d:.]+) "
            r"(?P<event>NHRP-RECV-PURGE-REPLY) tunnel: (?P<tunnel>[A-z0-9]+) "
            r"host with nbma_src: (?P<nbma_src>[0-9.]+) vpn_src: "
            r"(?P<vpn_src>[0-9.]+) receive purge reply from nbma_dest: "
            r"(?P<nbma_dest>[0-9.]+) vpn_dest: (?P<vpn_dest>[0-9.]+) vrf: "
            r"(?P<vrf>[A-Za-z0()]+) label: (?P<label>[a-z]+)")

        '''*Jul  2 16:30:55.263: NHRP-SEND-PURGE-REPLY tunnel: Tu1  host 
            with nbma_src: 3.3.3.1 vpn_src: 192.168.10.3 send purge reply 
            to nbma_dest: 2.2.2.1 vpn_dest: 192.168.10.2 vrf: global(0x0) 
            label: illegal'''        
        p24 = re.compile(r"\*(?P<time_stamp>[A-z0-9\s\d:.]+) "
            r"(?P<event>NHRP-SEND-PURGE-REPLY) tunnel: (?P<tunnel>[A-z0-9]+)  "
            r"host with nbma_src: (?P<nbma_src>[0-9.]+) vpn_src: "
            r"(?P<vpn_src>[0-9.]+) send purge reply to nbma_dest: "
            r"(?P<nbma_dest>[0-9.]+) vpn_dest: (?P<vpn_dest>[0-9.]+) vrf: "
            r"(?P<vrf>[A-Za-z0()]+) label: (?P<label>[a-z]+)")

        for line in output.splitlines():
            line = line.strip()
            
            '''*Jun 22 06:39:28.358: NHRP-CACHE-ADD tunnel: Tu1 target: 
            192.168.10. nbma_src: 1.1.1.1 vpn_src: 192.168.10.1 nbma_dest: 
            3.3.3.1 vpn_dest: 192.168.10.3 vrf: global(0x0) label: none'''
            if m:= p0.match(line):
                groups = m.groupdict()
                dest = groups['nbma_dest'].replace(".","_")
                nhrp_cache_add = ret_dict.setdefault("nhrp_cache_add", {})
                nhrp_cache_add.update({
                    dest : {
                        'event': groups['event'],
                        'tunnel': groups['tunnel'],
                        'target': groups['target'],
                        'nbma_src': groups['nbma_src'],
                        'vpn_src': groups['vpn_src'],
                        'nbma_dest': groups['nbma_dest'],
                        'vpn_dest': groups['vpn_dest'],
                        'vrf': groups['vrf'],
                        'label': groups['label']
                    }
                })
                continue

            '''*Jun 22 06:39:28.361: NHRP-NHC-UP tunnel: Tu1 NHC up nbma_src: 
            1.1.1.1 vpn_src: 192.168.10.1 nbma_dest: 3.3.3.1 vpn_dest: 
            192.168.10.3 vrf: global(0x0)'''
            if m:= p1.match(line):
                groups = m.groupdict()
                dest = groups['nbma_dest'].replace(".","_")
                nhrp_nhc_up = ret_dict.setdefault("nhrp_nhc_up", {})
                nhrp_nhc_up.update({
                    dest : {
                        "event": groups['event'],
                        "tunnel": groups['tunnel'],
                        'nbma_src': groups['nbma_src'],
                        'vpn_src': groups['vpn_src'],
                        'nbma_dest': groups['nbma_dest'],
                        'vpn_dest': groups['vpn_dest'],
                        'vrf': groups['vrf']
                    }
                })
                continue

            '''*Jun 22 06:39:28.362: NHRP-TUNNEL-ENDPOINT-ADD tunnel: Tu1 Added 
            tunnel endpoints nbma_dest: 3.3.3.1 vpn_dest: 192.168.10.3'''
            '''*Jul 27 07: 30: 25.534: NHRP-TUNNEL-ENDPOINT-ADD tunnel: Tu1 add/update 
                tunnel endpoints nbma_dest: 3.3.3.1 vpn_dest: 192.168.10.3'''
            if m:= p2.match(line):
                groups = m.groupdict()
                dest = groups['nbma_dest'].replace(".","_")
                nhrp_tunnel_endpoint_add = ret_dict.setdefault(
                    "nhrp_tunnel_endpoint_add", {})
                nhrp_tunnel_endpoint_add.update({
                    dest : {
                        "event": groups['event'],
                        "tunnel": groups['tunnel'],
                        'nbma_dest': groups['nbma_dest'],
                        'vpn_dest': groups['vpn_dest']
                    }
                })
                continue

            '''*Jun 22 06:39:28.930: NHRP-NHS-UP tunnel: Tu1 NHS up nbma_src: 
            2.2.2.1 vpn_src: 192.168.10.2 nbma_dest: 1.1.1.1 vpn_dest: 
            192.168.10.1 vrf: global(0x0)'''
            if m:= p3.match(line):
                groups = m.groupdict()
                dest = groups['nbma_dest'].replace(".","_")
                nhrp_nhs_up = ret_dict.setdefault("nhrp_nhs_up", {})
                nhrp_nhs_up.update({
                    dest : {
                        "event": groups['event'],
                        "tunnel": groups['tunnel'],
                        'nbma_src': groups['nbma_src'],
                        'vpn_src': groups['vpn_src'],
                        'nbma_dest': groups['nbma_dest'],
                        'vpn_dest': groups['vpn_dest'],
                        'vrf': groups['vrf']
                    }
                })
                continue

            '''*Jun 22 06:51:10.254: NHRP-RECV-RES-REQ tunnel: Tu1 host with
              nbma_src: 1.1.1.1 vpn_src: 192.168.10.3 received resolution 
              request from nbma_dest: 2.2.2.1 vpn_dest: 192.168.10.2 vrf: 
              global(0x0) label: none'''
            if m:= p4.match(line):
                groups = m.groupdict()
                dest = groups['nbma_dest'].replace(".","_")
                nhrp_recv_res_req = ret_dict.setdefault(
                    "nhrp_recv_res_req", {})
                nhrp_recv_res_req.update({
                    dest : {
                        "event": groups['event'],
                        "tunnel": groups['tunnel'],
                        "nbma_src": groups['nbma_src'],
                        "vpn_src": groups['vpn_src'],
                        "nbma_dest": groups['nbma_dest'],
                        "vpn_dest": groups['vpn_dest'],
                        "vrf": groups['vrf'],
                        "label": groups['label']
                    }
                })
                continue

            '''*Jun 23 12:56:43.560: NHRP-SEND-RES-REQ tunnel: Tu1 host with 
            nbma_src: 2.2.2.1 vpn_src: 192.168.10.2 send resolution request 
            to nbma_dest: 1.1.1.1 vpn_dest: 192.168.10.3 vrf: global(0x0) 
            label: none'''
            if m:= p5.match(line):
                groups = m.groupdict()
                dest = groups['nbma_dest'].replace(".","_")
                nhrp_send_res_req = ret_dict.setdefault(
                    "nhrp_send_res_req", {})
                nhrp_send_res_req.update({
                    dest : {
                        "event": groups['event'],
                        "tunnel": groups['tunnel'],
                        "nbma_src": groups['nbma_src'],
                        "vpn_src": groups['vpn_src'],
                        "nbma_dest": groups['nbma_dest'],
                        "vpn_dest": groups['vpn_dest'],
                        "vrf": groups['vrf'],
                        "label": groups['label']
                    }
                })
                continue

            '''*Jun 23 12:56:43.568: NHRP-RECV-RES-REPLY tunnel: Tu1 host with 
            nbma_src: 2.2.2.1 vpn_src: 192.168.10.2 received resolution reply 
            from nbma_dest: 3.3.3.1 vpn_dest: 192.168.10.3 vrf: global(0x0) 
            label: none'''
            if m:= p6.match(line):
                groups = m.groupdict()
                dest = groups['nbma_dest'].replace(".","_")
                nhrp_recv_res_reply = ret_dict.setdefault(
                    "nhrp_recv_res_reply", {})
                nhrp_recv_res_reply.update({
                    dest : {
                        "event": groups['event'],
                        "tunnel": groups['tunnel'],
                        "nbma_src": groups['nbma_src'],
                        "vpn_src": groups['vpn_src'],
                        "nbma_dest": groups['nbma_dest'],
                        "vpn_dest": groups['vpn_dest'],
                        "vrf": groups['vrf'],
                        "label": groups['label']
                    }
                })
                continue

            '''*Jun 23 12:56:43.712: NHRP-SEND-RES-REPLY tunnel: Tu1 host with 
            nbma_src: 3.3.3.1 vpn_src: 192.168.10.3 send resolution reply to 
            nbma_dest: 2.2.2.1 vpn_dest: 192.168.10.2 vrf: global(0x0) 
            label: illegal'''
            if m:= p8.match(line):
                groups = m.groupdict()
                dest = groups['nbma_dest'].replace(".","_")
                nhrp_send_res_reply = ret_dict.setdefault(
                    "nhrp_send_res_reply", {})
                nhrp_send_res_reply.update({
                    dest : {
                        "event": groups['event'],
                        "tunnel": groups['tunnel'],
                        "nbma_src": groups['nbma_src'],
                        "vpn_src": groups['vpn_src'],
                        "nbma_dest": groups['nbma_dest'],
                        "vpn_dest": groups['vpn_dest'],
                        "vrf": groups['vrf'],
                        "label": groups['label']
                    }
                })
                continue

            '''*Jun 22 07:02:43.481: NHRP-RECV-PURGE-REQ tunnel: Tu1 host 
            with nbma_src: 1.1.1.1 vpn_src: 192.168.10.1 receive purge 
            request from nbma_dest: 3.3.3.1 vpn_dest: 192.168.10.3 vrf: 
            global(0x0) label: explicit-null'''
            if m:= p9.match(line):
                groups = m.groupdict()
                dest = groups['nbma_dest'].replace(".","_")
                nhrp_recv_purge_req = ret_dict.setdefault(
                    "nhrp_recv_purge_req", {})
                nhrp_recv_purge_req.update({
                    dest : {
                        "event": groups['event'],
                        "tunnel": groups['tunnel'],
                        "nbma_src": groups['nbma_src'],
                        "vpn_src": groups['vpn_src'],
                        "nbma_dest": groups['nbma_dest'],
                        "vpn_dest": groups['vpn_dest'],
                        "vrf": groups['vrf'],
                        "label": groups['label']
                    }
                })
                continue

            '''*Jun 22 07:06:10.841: NHRP-SEND-PURGE-REQ tunnel: Tu1 host with 
            nbma_src: 3.3.3.1 vpn_src: 0.0.0.0 send purge request to nbma_dest: 
            UNKNOWN vpn_dest: 192.168.10.1 vrf: global(0x0) label: none'''
            if m:= p10.match(line):
                groups = m.groupdict()
                dest = groups['nbma_dest'].replace(".","_")
                nhrp_send_purge_req = ret_dict.setdefault("nhrp_send_purge_req", {})
                nhrp_send_purge_req.update({
                    dest : {
                        "event": groups['event'],
                        "tunnel": groups['tunnel'],
                        "nbma_src": groups['nbma_src'],
                        "vpn_src": groups['vpn_src'],
                        "nbma_dest": groups['nbma_dest'],
                        "vpn_dest": groups['vpn_dest'],
                        "vrf": groups['vrf'],
                        "label": groups['label']
                    }
                })
                continue

            '''NHRP-NHC-DOWN tunnel: Tu1 NHC down nbma_src: 1.1.1.1 vpn_src: 
            192.168.10.1 nbma_dest: 2.2.2.1 vpn_dest: 192.168.10.2 vrf: 
            global(0x0) reason: EXT - Tunnel Interface AdminDown'''
            if m:= p11.match(line):
                groups = m.groupdict()
                dest = groups['nbma_dest'].replace(".","_")
                nhrp_nhc_down = ret_dict.setdefault(
                    "nhrp_nhc_down", {})
                nhrp_nhc_down.update({
                    dest : {
                        "event": groups['event'],
                        "tunnel": groups['tunnel'],
                        "nbma_src": groups['nbma_src'],
                        "vpn_src": groups['vpn_src'],
                        "nbma_dest": groups['nbma_dest'],
                        "vpn_dest": groups['vpn_dest'],
                        "vrf": groups['vrf'],
                        "reason": groups['reason']
                    }
                })
                continue

            '''*Jun 22 08:56:36.794: NHRP-TUNNEL-ENDPOINT-DELETE tunnel: 
            Tu1 Deleting tunnel endpoints nbma_dest: 3.3.3.1 vpn_dest: 
            192.168.10.3'''
            if m:= p12.match(line):
                groups = m.groupdict()
                dest = groups['nbma_dest'].replace(".","_")
                nhrp_tunnel_endpoint_delete = ret_dict.setdefault(
                    "nhrp_tunnel_endpoint_delete", {})
                nhrp_tunnel_endpoint_delete.update({
                    dest : {
                        "event": groups['event'],
                        "tunnel": groups['tunnel'],
                        "nbma_dest": groups['nbma_dest'],
                        "vpn_dest": groups['vpn_dest']
                    }
                })
                continue

            '''*Jun 22 08:59:28.070: NHRP-NHS-DOWN tunnel: Tu1 NHS down 
            nbma_src: 2.2.2.1 vpn_src: 192.168.10.2 nbma_dest: 1.1.1.1 
            vpn_dest: 192.168.10.1 vrf: global(0x0) reason: NHRP - 
            Registration Failure'''
            if m:= p13.match(line):
                groups = m.groupdict()
                dest = groups['nbma_dest'].replace(".","_")
                nhrp_nhs_down = ret_dict.setdefault(
                    "nhrp_nhs_down", {})
                nhrp_nhs_down.update({
                    dest : {
                        "event": groups['event'],
                        "tunnel": groups['tunnel'],
                        "nbma_src": groups['nbma_src'],
                        "vpn_src": groups['vpn_src'],
                        "nbma_dest": groups['nbma_dest'],
                        "vpn_dest": groups['vpn_dest'],
                        "vrf": groups['vrf']
                    }
                })
                continue

            '''*Jun 22 08:59:28.071: NHRP-NHS-RECOVERY-NHS-STATE  NHS vpn_dest: 
            192.168.10.1 Tunnel1 vrf 0 cluster 0 priority 0 transitioned to 
            'expecting replies' from 'responding expecting replies'''
            '''*Jul 27 07: 30: 34.496: NHRP-NHS-RECOVERY-NHS-STATE  NHS vpn_dest: 192.168.10.1 
            Tunnel1 vrf: global (0x0) cluster 0 priority 0 transitioned to 'responding 
            expecting replies' from 'expecting replies'''
            if m:= p14.match(line):
                groups = m.groupdict()
                dest = groups['vpn_dest'].replace(".","_")
                nhrp_nhs_recovery_nhs_state = ret_dict.setdefault(
                    "nhrp_nhs_recovery_nhs_state", {})
                nhrp_nhs_recovery_nhs_state.update({
                    dest : {
                        "event": groups['event'],
                        "vpn_dest": groups['vpn_dest']
                    }
                })
                continue

            '''*Jun 22 08:59:56.133: NHRP-CTRL-PLANE-RETRANS tunnel: Tu1 
            retransmitting registration request for vpn_dest: 192.168.10.1 
            reqid 2819 retrans ivl 2 sec vrf: NONE label: explicit-null'''
            '''*Aug 14 05: 06: 47.622: NHRP-CTRL-PLANE-RETRANS tunnel: Tu1 
           retransmitting Registration Request for vpn_dest: 192.168.10.1 reqid 
           4 retrans 2 sec vrf: global (0x0) label: explicit-null'''
            if m:= p15.match(line):
                groups = m.groupdict()
                dest = groups['vpn_dest'].replace(".","_")
                nhrp_ctrl_plane_retrance = ret_dict.setdefault(
                    "nhrp_ctrl_plane_retrance", {})
                nhrp_ctrl_plane_retrance.update({
                    dest : {
                        "event": groups['event'],
                        "tunnel": groups['tunnel'],
                        "vpn_dest": groups['vpn_dest'],
                        "vrf": groups['vrf']
                    }
                })
                continue

            '''*Jun 23 13:51:22.428: NHRP-NHP-DOWN tunnel: Tu1 NHP down 
            nbma_src: 2.2.2.1 vpn_src: 192.168.10.2 nbma_dest: 3.3.3.1 
            vpn_dest: 192.168.10.3 vrf: global(0x0) reason: No Reason'''
            if m:= p18.match(line):
                groups = m.groupdict()
                dest = groups['nbma_dest'].replace(".","_")
                nhrp_nhp_down = ret_dict.setdefault("nhrp_nhp_down", {})
                nhrp_nhp_down.update({
                    dest : {
                        "event": groups['event'],
                        "tunnel": groups['tunnel'],
                        "nbma_src": groups['nbma_src'],
                        "vpn_src": groups['vpn_src'],
                        "nbma_dest": groups['nbma_dest'],
                        "vpn_dest": groups['vpn_dest'],
                        "vrf": groups['vrf'],
                        "reason": groups['reason']
                    }
                })
                continue

            '''*Jun 24 09:09:36.455: NHRP-CACHE-DELETE tunnel: Tu1 nbma_src: 
            1.1.1.1 vpn_src: 192.168.10.1 nbma_dest: 2.2.2.1 vpn_dest: 
            192.168.10. vrf: global(0x0) label: none reason: 
            EXT - Tunnel Interface AdminDown'''
            if m:= p20.match(line):
                groups = m.groupdict()
                dest = groups['nbma_dest'].replace(".","_")
                nhrp_cache_delete = ret_dict.setdefault(
                    "nhrp_cache_delete", {})
                nhrp_cache_delete.update({
                    dest : {
                        "event": groups['event'],
                        "tunnel": groups['tunnel'],
                        "nbma_src": groups['nbma_src'],
                        "vpn_src": groups['vpn_src'],
                        "nbma_dest": groups['nbma_dest'],
                        "vpn_dest": groups['vpn_dest'],
                        "vrf": groups['vrf'],
                        "label": groups['label'],
                        "reason": groups['reason']
                    }
                })
                continue

            '''*Jun 26 18:38:52.148: NHRP-CACHE-UPDATE tunnel: Tu1 target: 
            192.168.10. nbma_src: 2.2.2.1 vpn_src: 192.168.10.2 nbma_dest: 
            1.1.1.1 vpn_dest: 192.168.10.3 vrf: global(0x0) label: none'''
            if m:= p21.match(line):
                groups = m.groupdict()
                dest = groups['nbma_dest'].replace(".","_")
                nhrp_cache_update = ret_dict.setdefault(
                    "nhrp_cache_update", {})
                nhrp_cache_update.update({
                    dest : {
                        "event": groups['event'],
                        "tunnel": groups['tunnel'],
                        "target": groups['target'],
                        "nbma_src": groups['nbma_src'],
                        "vpn_src": groups['vpn_src'],
                        "nbma_dest": groups['nbma_dest'],
                        "vpn_dest": groups['vpn_dest'],
                        "vrf": groups['vrf'],
                        "label": groups['label']
                    }
                })
                continue

            '''*Jun 27 17:48:34.466: NHRP-CACHE-NBMA-NHOP-CHANGE tunnel: Tu1 
            cache address change nbma old: 1.1.1.1 -> new: 3.3.3.1'''
            if m:= p22.match(line):
                groups = m.groupdict()
                dest = groups['old'].replace(".","_")
                nhrp_cache_nbma_nhop_change = ret_dict.setdefault(
                    "nhrp_cache_nbma_nhop_change", {})
                nhrp_cache_nbma_nhop_change.update({
                    dest : {
                        "event": groups['event'],
                        "tunnel": groups['tunnel'],
                        "old": groups['old'],
                        "new": groups['new']
                    }
                })
                continue

            '''Jul  2 16:35:19.386: NHRP-RECV-PURGE-REPLY tunnel: Tu1 host with
              nbma_src: 2.2.2.1 vpn_src: 192.168.10.2 receive purge reply from 
              nbma_dest: 2.2.2.1 vpn_dest: 192.168.10.3 vrf: global(0x0) 
              label: none'''
            if m:= p23.match(line):
                groups = m.groupdict()
                dest = groups['nbma_dest'].replace(".","_")
                nhrp_recv_purge_reply = ret_dict.setdefault(
                    "nhrp_recv_purge_reply", {})
                nhrp_recv_purge_reply.update({
                    dest : {
                        "event": groups['event'],
                        "tunnel": groups['tunnel'],
                        "nbma_src": groups['nbma_src'],
                        "vpn_src": groups['vpn_src'],
                        "nbma_dest": groups['nbma_dest'],
                        "vpn_dest": groups['vpn_dest'],
                        "vrf": groups['vrf'],
                        "label": groups['label']
                    }
                })
                continue

            '''*Jul  2 16:30:55.263: NHRP-SEND-PURGE-REPLY tunnel: Tu1  host 
            with nbma_src: 3.3.3.1 vpn_src: 192.168.10.3 send purge reply 
            to nbma_dest: 2.2.2.1 vpn_dest: 192.168.10.2 vrf: global(0x0) 
            label: illegal'''
            if m:= p24.match(line):
                groups = m.groupdict()
                dest = groups['nbma_dest'].replace(".","_")
                nhrp_send_purge_reply = ret_dict.setdefault(
                    "nhrp_send_purge_reply", {})
                nhrp_send_purge_reply.update({
                    dest : {
                        "event": groups['event'],
                        "tunnel": groups['tunnel'],
                        "nbma_src": groups['nbma_src'],
                        "vpn_src": groups['vpn_src'],
                        "nbma_dest": groups['nbma_dest'],
                        "vpn_dest": groups['vpn_dest'],
                        "vrf": groups['vrf'],
                        "label": groups['label']
                    }
                })
                continue
        return ret_dict

class ShowMonitorCaptureFileDetailedSchema(MetaParser):
    schema = {
        'dhcp_offer': {
            'client_mac_address': str,
        }
    }

class ShowMonitorCaptureFileDetailed(ShowMonitorCaptureFileDetailedSchema):
    cli_command = 'show monitor capture file flash:file1.pcap packet-number 7 detailed'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Matching patterns
        # Dynamic Host Configuration Protocol (Offer)
        p1 = re.compile(r'^Dynamic Host Configuration Protocol \(Offer\)$')

        # Client MAC address
        p2 = re.compile(r'^Client MAC address: +(?P<client_mac_address>[\w:]+)')

        dhcp_offer_section = False

        for line in output.splitlines():
            line = line.strip()

            # Dynamic Host Configuration Protocol (Offer)
            m = p1.match(line)
            if m:
                dhcp_offer_section = True
                ret_dict['dhcp_offer'] = {}
                continue

            # Client MAC address: 00:11:01:00:00:01 (00:11:01:00:00:01) within DHCP Offer section
            if dhcp_offer_section:
                m = p2.match(line)
                if m:
                    ret_dict['dhcp_offer']['client_mac_address'] = m.groupdict()['client_mac_address']
                    continue

        return ret_dict

# =================================================
#  Schema for 'show monitor event-trace crypto pki event all'
# =================================================
class ShowMonitorEventTraceCryptoPkiEventAllSchema(MetaParser):
    """Schema for `show monitor event-trace crypto pki event all`"""
    schema = {
        'event_trace': {
            'event': {
                int: {
                    'timestamp': str,
                    'event_message': str,
                }
            }
        }
    }

# =================================================
#  Parser for 'show monitor event-trace crypto pki event all'
# =================================================

class ShowMonitorEventTraceCryptoPkiEventAll(ShowMonitorEventTraceCryptoPkiEventAllSchema):
    """Parser for `show monitor event-trace crypto pki event all`"""

    cli_command = 'show monitor event-trace crypto pki event all'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}
        event_idx = 1

        # Example: 'Jun  9 13:30:43.826: Trustpoint- rootca:HTTP Server is disabled.'
        p1 = re.compile(r'^(?P<timestamp>\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2}\.\d{3}):\s*(?P<event_message>.*)$')

        # Example: '    This is a continuation line'
        p2 = re.compile(r'^\s+(?P<cont>.+)$')

        current_event = None

        for line in output.splitlines():
            line = line.rstrip()
            #Jun  9 13:30:43.826: Trustpoint- rootca:HTTP Server is disabled.
            m = p1.match(line)
            if m:
                current_event = event_idx
                event_dict = parsed_dict.setdefault('event_trace', {}).setdefault('event', {}).setdefault(current_event, {})
                event_dict['timestamp'] = m.group('timestamp')
                event_dict['event_message'] = m.group('event_message')
                event_idx += 1
                continue
            # p2: Matches lines that start with one or more spaces followed by any characters (continuation lines)
            m = p2.match(line)
            if m and current_event:
                event_dict = parsed_dict['event_trace']['event'][current_event]
                event_dict['event_message'] += '\n' + m.group('cont')
                continue

        return parsed_dict

# =================================================
#  Schema for 'show monitor event-trace crypto pki error all'
# =================================================
class ShowMonitorEventTraceCryptoPkiErrorAllSchema(MetaParser):
    """Schema for `show monitor event-trace crypto pki error all`"""
    schema = {
        'event_trace': {
            'event': {
                int: {
                    Optional('timestamp'): str,
                    Optional('event_message'): str,
                }
            }
        }
    }

# =================================================
#  Parser for 'show monitor event-trace crypto pki error all'
# =================================================
class ShowMonitorEventTraceCryptoPkiErrorAll(ShowMonitorEventTraceCryptoPkiErrorAllSchema):
    """Parser for `show monitor event-trace crypto pki error all`"""

    cli_command = 'show monitor event-trace crypto pki error all'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}
        event_idx = 1

        # Example: 'Jun  9 13:30:43.826: <event_message>'
        p1 = re.compile(r'^(?P<timestamp>\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2}\.\d{3}):\s*(?P<event_message>.*)$')

        # Example: '    This is a continuation line'
        p2 = re.compile(r'^\s+(?P<cont>.+)$')

        current_event = None

        for line in output.splitlines():
            line = line.rstrip()
            # p1: Matches a log line starting with a timestamp (e.g. 'Jun  9 13:30:43.826:') followed by an event message.
            m = p1.match(line)
            if m:
                current_event = event_idx
                event_dict = parsed_dict.setdefault('event_trace', {}).setdefault('event', {}).setdefault(current_event, {})
                event_dict['timestamp'] = m.group('timestamp')
                event_dict['event_message'] = m.group('event_message')
                event_idx += 1
                continue
            # p2: Matches lines that start with one or more spaces followed by any characters (continuation lines)
            m = p2.match(line)
            if m and current_event:
                event_dict = parsed_dict['event_trace']['event'][current_event]
                event_dict['event_message'] += '\n' + m.group('cont')
                continue

        return parsed_dict

# =================================================
#  Schema for 'show monitor event-trace crypto ikev2 event all'
# =================================================
class ShowMonitorEventTraceCryptoIkev2EventAllSchema(MetaParser):
    """Schema for `show monitor event-trace crypto ikev2 event all`"""
    schema = {
        'event_trace': {
            'events': {
                int: {
                    'timestamp': str,
                    'sa_id': int,
                    'session_id': int,
                    'remote': str,
                    'local': str,
                    'event_message': str,
                    Optional('direction'): str,
                    Optional('exchange_type'): str,
                    Optional('spi'): str,
                    Optional('ispi'): str,
                    Optional('rspi'): str,
                    Optional('ike_id_pair'): str
                }
            }
        }
    }

# =================================================
#  Parser for 'show monitor event-trace crypto ikev2 event all'
# =================================================
class ShowMonitorEventTraceCryptoIkev2EventAll(ShowMonitorEventTraceCryptoIkev2EventAllSchema):
    """Parser for `show monitor event-trace crypto ikev2 event all`"""

    cli_command = 'show monitor event-trace crypto ikev2 event all'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}
        event_idx = 1

        # Main pattern for IKEv2 event entries
        # *Apr  4 00:16:59.484: SA ID:2 SESSION ID:1 Remote: 30.1.1.2/500 Local: 30.1.1.1/500  Sending DELETE INFO message for IPsec SA [SPI: 0x28DC063C]
        p1 = re.compile(r'^\*(?P<timestamp>\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2}\.\d{3}):\s+'
                       r'SA\s+ID:(?P<sa_id>\d+)\s+'
                       r'SESSION\s+ID:(?P<session_id>\d+)\s+'
                       r'Remote:\s+(?P<remote>\S+)\s+'
                       r'Local:\s+(?P<local>\S+)\s+'
                       r'(?P<event_message>.*)$')

        # Pattern to extract direction from event message (Initiator/Responder)
        # "(I) Sending IKEv2 INFORMATIONAL Exchange REQUEST" or "(R) Received IKEv2 IKE_SA_INIT Exchange REQUEST"
        p2 = re.compile(r'^\((?P<direction>[IR])\)')

        # Pattern to extract SPI from event message (but not ISPI/RSPI)
        # "Sending DELETE INFO message for IPsec SA [SPI: 0x28DC063C]"
        p3 = re.compile(r'.*(?<!I)SPI:\s+(?P<spi>0x[0-9A-F]+)(?!\s+RSPI)')

        # Pattern to extract ISPI and RSPI from event message
        # "Sending DELETE INFO message for IKEv2 SA [ISPI: 0x52C79670608A3068 RSPI: 0x0063AAED5563FDAE]"
        p4 = re.compile(r'.*ISPI:\s+(?P<ispi>0x[0-9A-F]+)\s+RSPI:\s+(?P<rspi>0x[0-9A-F]+)')

        # Pattern to extract IKE ID pair
        # "Session with IKE ID PAIR(30.1.1.2 , 30.1.1.1) is UP"
        p5 = re.compile(r'.*IKE\s+ID\s+PAIR\((?P<ike_id_pair>[^)]+)\)')

        # Pattern to extract exchange type
        # "(I) Sending IKEv2 INFORMATIONAL Exchange REQUEST" or "(R) Received IKEv2 IKE_AUTH Exchange RESPONSE"
        p6 = re.compile(r'.*IKEv2\s+(?P<exchange_type>\w+)\s+Exchange')

        for line in output.splitlines():
            line = line.strip()

            # *Apr 4 00:16:59.484: SA ID:2 SESSION ID:1 Remote: 30.1.1.2/500 Local: 30.1.1.1/500  Sending DELETE INFO message for IPsec SA [SPI: 0x28DC063C]
            m = p1.match(line)
            if m:
                event_dict = parsed_dict.setdefault('event_trace', {}).setdefault('events', {}).setdefault(event_idx, {})

                event_dict['timestamp'] = m.group('timestamp')
                event_dict['sa_id'] = int(m.group('sa_id'))
                event_dict['session_id'] = int(m.group('session_id'))
                event_dict['remote'] = m.group('remote')
                event_dict['local'] = m.group('local')
                event_dict['event_message'] = m.group('event_message').strip()

                # Extract optional fields from event message
                event_message = event_dict['event_message']

                # Extract direction (I or R)
                m_dir = p2.match(event_message)
                if m_dir:
                    event_dict['direction'] = m_dir.group('direction')

                # Extract ISPI and RSPI first (more specific pattern)
                m_ispi_rspi = p4.match(event_message)
                if m_ispi_rspi:
                    event_dict['ispi'] = m_ispi_rspi.group('ispi')
                    event_dict['rspi'] = m_ispi_rspi.group('rspi')
                else:
                    # Only check for single SPI if no ISPI/RSPI found
                    m_spi = p3.match(event_message)
                    if m_spi:
                        event_dict['spi'] = m_spi.group('spi')

                # Extract IKE ID pair
                m_ike_id = p5.match(event_message)
                if m_ike_id:
                    event_dict['ike_id_pair'] = m_ike_id.group('ike_id_pair')

                # Extract exchange type
                m_exchange = p6.match(event_message)
                if m_exchange:
                    event_dict['exchange_type'] = m_exchange.group('exchange_type')

                event_idx += 1

        return parsed_dict


# =================================================
#  Schema for 'show monitor event-trace crypto all detail'
# =================================================
class ShowMonitorEventTraceCryptoAllDetailSchema(MetaParser):
    """Schema for `show monitor event-trace crypto all detail`"""
    schema = {
        'event_trace': {
            Optional('pki_event'): {
                Optional('events'): ListOf({
                    Optional('timestamp'): str,
                    Optional('message'): str,
                    Optional('traceback'): str,
                }),
                Optional('status'): str,
            },
            Optional('pki_internal_event'): {
                Optional('events'): ListOf({
                    Optional('timestamp'): str,
                    Optional('message'): str,
                    Optional('traceback'): str,
                }),
                Optional('status'): str,
            },
            Optional('pki_error'): {
                Optional('events'): ListOf({
                    Optional('timestamp'): str,
                    Optional('message'): str,
                    Optional('traceback'): str,
                }),
                Optional('status'): str,
            },
            Optional('ikev2_event'): {
                Optional('events'): ListOf({
                    Optional('timestamp'): str,
                    Optional('message'): str,
                    Optional('traceback'): str,
                }),
                Optional('status'): str,
            },
            Optional('ikev2_internal_event'): {
                Optional('events'): ListOf({
                    Optional('timestamp'): str,
                    Optional('message'): str,
                    Optional('traceback'): str,
                }),
                Optional('status'): str,
            },
            Optional('ikev2_error'): {
                Optional('events'): ListOf({
                    Optional('timestamp'): str,
                    Optional('message'): str,
                    Optional('traceback'): str,
                }),
                Optional('status'): str,
            },
            Optional('ikev2_exception'): {
                Optional('events'): ListOf({
                    Optional('timestamp'): str,
                    Optional('message'): str,
                    Optional('traceback'): str,
                }),
                Optional('status'): str,
            },
            Optional('ipsec_event'): {
                Optional('events'): ListOf({
                    Optional('timestamp'): str,
                    Optional('message'): str,
                    Optional('traceback'): str,
                }),
                Optional('status'): str,
            },
            Optional('ipsec_error'): {
                Optional('events'): ListOf({
                    Optional('timestamp'): str,
                    Optional('message'): str,
                    Optional('traceback'): str,
                }),
                Optional('status'): str,
            },
            Optional('ipsec_exception'): {
                Optional('events'): ListOf({
                    Optional('timestamp'): str,
                    Optional('message'): str,
                    Optional('traceback'): str,
                }),
                Optional('status'): str,
                'interrupt_context_allocation_count': int,
            },
        }
    }

# =================================================
#  Parser for 'show monitor event-trace crypto all detail'
# =================================================
class ShowMonitorEventTraceCryptoAllDetail(ShowMonitorEventTraceCryptoAllDetailSchema):
    """Parser for `show monitor event-trace crypto all detail`"""

    cli_command = 'show monitor event-trace crypto all detail'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}
        current_section = None
        current_events = []

        # pki_event:
        p1 = re.compile(r'^(?P<section>\w+):\s*$')

        # *Apr  3 23:53:30.374: EST client initialized.
        p2 = re.compile(r'^\*(?P<timestamp>\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2}\.\d{3}):\s*(?P<message>.*)$')

        # -Traceback= 1#3c677f5693d4a1da4989c9342fd445a2 :AAAACD000000+B371FD8  :AAAACD000000+6CA9C90  :AAAACD000000+6CAFFD4  :AAAACD000000+802A094  :AAAACD000000+8029AEC  :AAAACD000000+7F8E788  :AAAACD000000+896EBD8
        p3 = re.compile(r'^-Traceback=\s*(?P<traceback>.*)$')

        # Tracing currently disabled, from exec command
        p4 = re.compile(r'^Tracing currently disabled, from exec command\s*$')

        # interrupt context allocation count = 0
        p5 = re.compile(r'^interrupt context allocation count = (?P<count>\d+)\s*$')

        for line in output.splitlines():
            line = line.strip()

            # pki_event:
            m1 = p1.match(line)
            if m1:
                current_section = m1.group('section')
                if current_section not in parsed_dict:
                    section_dict = parsed_dict.setdefault('event_trace', {}).setdefault(current_section, {})
                else:
                    continue

            # *Apr  3 23:53:30.374: EST client initialized.
            m2 = p2.match(line)
            if m2:
                event = {
                    'timestamp': m2.group('timestamp'),
                    'message': m2.group('message')
                }                
                if 'events' in section_dict:
                    section_dict['events'].append(event)
                else:
                    section_dict.setdefault('events', [event])    
                continue

            # -Traceback= 1#3c677f5693d4a1da4989c9342fd445a2 :AAAACD000000+B371FD8  :AAAACD000000+6CA9C90  :AAAACD000000+6CAFFD4  :AAAACD000000+802A094  :AAAACD000000+8029AEC  :AAAACD000000+7F8E788  :AAAACD000000+896EBD8
            m3 = p3.match(line)
            if m3:
                section_dict['events'][-1]['traceback'] = m3.group('traceback')
                continue

            # Tracing currently disabled, from exec command
            m4 = p4.match(line)
            if m4:
                section_dict['status'] = 'Tracing currently disabled, from exec command'
                continue

           # interrupt context allocation count = 0
            m5 = p5.match(line)
            if m5:
                section_dict['interrupt_context_allocation_count'] = int(m5.group('count'))
                continue

        return parsed_dict


# =================================================
#  Schema for 'show monitor event-trace crypto from-boot'
#  Schema for 'show monitor event-trace crypto from-boot {timer}'
# =================================================
class ShowMonitorEventTraceCryptoFromBootSchema(MetaParser):
    """Schema for :
        'show monitor event-trace crypto from-boot'
        'show monitor event-trace crypto from-boot {timer}'"""
    schema = {
        'event_trace': {
            Optional('pki_event'): {
                Optional('events'): ListOf({
                    Optional('timestamp'): str,
                    Optional('message'): str,
                    Optional('traceback'): str,
                }),
                Optional('status'): str,
            },
            Optional('pki_internal_event'): {
                Optional('events'): ListOf({
                    Optional('timestamp'): str,
                    Optional('message'): str,
                    Optional('traceback'): str,
                }),
                Optional('status'): str,
            },
            Optional('pki_error'): {
                Optional('events'): ListOf({
                    Optional('timestamp'): str,
                    Optional('message'): str,
                    Optional('traceback'): str,
                }),
                Optional('status'): str,
            },
            Optional('ikev2_event'): {
                Optional('events'): ListOf({
                    Optional('timestamp'): str,
                    Optional('message'): str,
                    Optional('traceback'): str,
                }),
                Optional('status'): str,
            },
            Optional('ikev2_internal_event'): {
                Optional('events'): ListOf({
                    Optional('timestamp'): str,
                    Optional('message'): str,
                    Optional('traceback'): str,
                }),
                Optional('status'): str,
            },
            Optional('ikev2_error'): {
                Optional('events'): ListOf({
                    Optional('timestamp'): str,
                    Optional('message'): str,
                    Optional('traceback'): str,
                }),
                Optional('status'): str,
            },
            Optional('ikev2_exception'): {
                Optional('events'): ListOf({
                    Optional('timestamp'): str,
                    Optional('message'): str,
                    Optional('traceback'): str,
                }),
                Optional('status'): str,
            },
            Optional('ipsec_event'): {
                Optional('events'): ListOf({
                    Optional('timestamp'): str,
                    Optional('message'): str,
                    Optional('traceback'): str,
                }),
                Optional('status'): str,
            },
            Optional('ipsec_error'): {
                Optional('events'): ListOf({
                    Optional('timestamp'): str,
                    Optional('message'): str,
                    Optional('traceback'): str,
                }),
                Optional('status'): str,
            },
            Optional('ipsec_exception'): {
                Optional('events'): ListOf({
                    Optional('timestamp'): str,
                    Optional('message'): str,
                    Optional('traceback'): str,
                }),
                Optional('status'): str,
                Optional('interrupt_context_allocation_count'): int,
            },
        }
    }

# =================================================
#  Parser for 'show monitor event-trace crypto from-boot'
#  Parser for 'show monitor event-trace crypto from-boot {timer}'
# =================================================
class ShowMonitorEventTraceCryptoFromBoot(ShowMonitorEventTraceCryptoFromBootSchema):
    """Parser for :
        'show monitor event-trace crypto from-boot'
        'show monitor event-trace crypto from-boot {timer}'"""

    cli_command = ['show monitor event-trace crypto from-boot',
                   'show monitor event-trace crypto from-boot {timer}']

    def cli(self, timer='', output=None):
        if output is None:
            if timer:
                cmd = self.cli_command[1].format(timer=timer)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        parsed_dict = {}
        current_section = None
        current_events = []

        # pki_event:
        p1 = re.compile(r'^(?P<section>\w+):\s*$')

        # Aug 11 09:10:26.036: SA ID:1 SESSION ID:1 Remote: 40.181.251.101/500 Local: 40.185.80.1/500  (I) Sending IKEv2 IKE_SA_INIT Exchange REQUEST
        p2 = re.compile(r'^(?P<timestamp>\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2}\.\d{3}):\s*(?P<message>.*)$')

        # -Traceback= 1#3c677f5693d4a1da4989c9342fd445a2 :AAAACD000000+B371FD8  :AAAACD000000+6CA9C90  :AAAACD000000+6CAFFD4  :AAAACD000000+802A094  :AAAACD000000+8029AEC  :AAAACD000000+7F8E788  :AAAACD000000+896EBD8
        p3 = re.compile(r'^-Traceback=\s*(?P<traceback>.*)$')

        # Tracing currently disabled, from exec command
        p4 = re.compile(r'^Tracing currently disabled, from exec command\s*$')

        # interrupt context allocation count = 0
        p5 = re.compile(r'^interrupt context allocation count = (?P<count>\d+)\s*$')

        for line in output.splitlines():
            line = line.strip()

            # pki_event:
            m1 = p1.match(line)
            if m1:
                current_section = m1.group('section')
                if current_section not in parsed_dict:
                    section_dict = parsed_dict.setdefault('event_trace', {}).setdefault(current_section, {})
                else:
                    continue

            # Aug 11 09:10:26.036: SA ID:1 SESSION ID:1 Remote: 40.181.251.101/500 Local: 40.185.80.1/500  (I) Sending IKEv2 IKE_SA_INIT Exchange REQUEST
            m2 = p2.match(line)
            if m2:
                event = {
                    'timestamp': m2.group('timestamp'),
                    'message': m2.group('message')
                }                
                if 'events' in section_dict:
                    section_dict['events'].append(event)
                else:
                    section_dict.setdefault('events', [event])    
                continue

            # -Traceback= 1#3c677f5693d4a1da4989c9342fd445a2 :AAAACD000000+B371FD8  :AAAACD000000+6CA9C90  :AAAACD000000+6CAFFD4  :AAAACD000000+802A094  :AAAACD000000+8029AEC  :AAAACD000000+7F8E788  :AAAACD000000+896EBD8
            m3 = p3.match(line)
            if m3:
                section_dict['events'][-1]['traceback'] = m3.group('traceback')
                continue

            # Tracing currently disabled, from exec command
            m4 = p4.match(line)
            if m4:
                section_dict['status'] = 'Tracing currently disabled, from exec command'
                continue

            # interrupt context allocation count = 0
            m5 = p5.match(line)
            if m5:
                section_dict['interrupt_context_allocation_count'] = int(m5.group('count'))
                continue

        return parsed_dict
