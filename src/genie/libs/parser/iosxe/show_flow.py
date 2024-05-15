''' show_flow.py

IOSXE parsers for the following show commands:
    * show flow monitor {name} cache format table
    * show flow exporter statistics
    * show flow exporter {exporter} statistics
    * show flow monitor {flow_monitor_name} statistics
    * show flow monitor
    * show flow monitor sdwan_flow_monitor cache filter interface input <> ipv4 source address <>
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, ListOf, Optional, And, Default, Use

# Common
from genie.libs.parser.utils.common import Common

# =========================================================
# Schema for 'show flow monitor {name} cache format table'
# =========================================================
class ShowFlowMonitorSchema(MetaParser):
    ''' Schema for "show flow monitor {name} cache format table" '''

    schema = {
        'cache_type': str,
        'cache_size': int,
        'current_entries': int,
        Optional('high_water_mark'): int,
        'flows_added': int,
        'flows_aged': int,
        Optional('ipv4_src_addr'): {
            Any(): {
                'ipv4_dst_addr': {
                    Any(): {
                        'index': {
                            Any(): {
                                'trns_src_port': int,
                                'trns_dst_port': int,
                                'ip_tos': str,
                                'ip_port': int,
                                'bytes_long': int,
                                'pkts_long': int,
                            }
                        }
                    }
                }
            }
        }
    }

# =========================================================
# Parser for 'show flow monitor {name} cache format table'
# =========================================================
class ShowFlowMonitor(ShowFlowMonitorSchema):
    ''' Parser for
      "show flow monitor {name} cache format table"
    '''

    cli_command = 'show flow monitor {name} cache format table'

    def cli(self, name, output=None):
        if output is None:
            cmd = self.cli_command.format(name=name)
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}
        dst_addr_index = {}

        # Cache type:                               Normal (Platform cache)
        p1 = re.compile(r'^Cache +type: +(?P<cache_type>[\S\s]+)$')

        # Cache size:                                   16
        p2 = re.compile(r'^Cache +size: +(?P<cache_size>\d+)$')

        # Current entries:                               1
        p3 = re.compile(r'^Current +entries: +(?P<current_entries>\d+)$')

        # High Watermark:                                1
        p4 = re.compile(r'^High +Watermark: +(?P<high_water_mark>\d+)$')

        # Flows added:                                   1
        p5 = re.compile(r'^Flows +added: +(?P<flows_added>\d+)$')

        # Flows aged:                                   0
        p6 = re.compile(r'^Flows +aged: +(?P<flows_aged>\d+)$')

        # 10.4.1.10         10.4.10.1                    0              0  0xC0         89                   100                     1
        p7 = re.compile(r'^(?P<ipv4_src_addr>\S+) +(?P<ipv4_dst_addr>\S+) +'
                        '(?P<trns_src_port>\d+) +(?P<trns_dst_port>\d+) +'
                        '(?P<ip_tos>\S+) +(?P<ip_port>\d+) +(?P<bytes_long>\d+) +'
                        '(?P<pkts_long>\d+)$')
        for line in out.splitlines():

            line = line.strip()

            # Cache type:                               Normal (Platform cache)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'cache_type': group['cache_type']})
                continue

            # Cache size:                                   16
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'cache_size': int(group['cache_size'])})
                continue

            # Current entries:                               1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'current_entries': int(group['current_entries'])})
                continue

            # High Watermark:                                1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'high_water_mark': int(group['high_water_mark'])})
                continue

            # Flows added:                                   1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'flows_added': int(group['flows_added'])})
                continue

            # Flows aged:                                   0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'flows_aged': int(group['flows_aged'])})
                continue

            # 10.4.1.10         10.4.10.1                    0              0  0xC0         89                   100                     1
            m = p7.match(line)
            if m:
                group = m.groupdict()

                index = dst_addr_index.get(group['ipv4_dst_addr'], 0) + 1

                ipv4_dst_addr_dict = ret_dict.setdefault('ipv4_src_addr', {}).\
                    setdefault(group['ipv4_src_addr'], {}).\
                    setdefault('ipv4_dst_addr', {}).\
                    setdefault(group['ipv4_dst_addr'], {}).\
                    setdefault('index', {}).\
                    setdefault(index, {})

                ipv4_dst_addr_dict.update({'trns_src_port': int(group['trns_src_port'])})
                ipv4_dst_addr_dict.update({'trns_dst_port': int(group['trns_dst_port'])})
                ipv4_dst_addr_dict.update({'ip_tos': group['ip_tos']})
                ipv4_dst_addr_dict.update({'ip_port': int(group['ip_port'])})
                ipv4_dst_addr_dict.update({'bytes_long': int(group['bytes_long'])})
                ipv4_dst_addr_dict.update({'pkts_long': int(group['pkts_long'])})

                dst_addr_index.update({group['ipv4_dst_addr']: index})

                continue

        return ret_dict


# =========================================================
# Schema for 'show flow monitor {name} cache'
# =========================================================
class ShowFlowMonitorCacheSchema(MetaParser):
    ''' Schema for
        "show flow monitor {name} cache"
        "show flow monitor {name} cache format record"
    '''

    schema = {
        'cache_type': str,
        'cache_size': int,
        'current_entries': int,
        Optional('high_water_mark'): int,
        'flows_added': int,
        'flows_aged': {
            'total': int,
            Optional('active_timeout_secs'): int,
            Optional('active_timeout'): int,
            Optional('inactive_timeout_secs'): int,
            Optional('inactive_timeout'): int,
            Optional('event_aged'): int,
            Optional('watermark_aged'): int,
            Optional('emergency_aged'): int,
        },
        Optional('entries'): {
            Any(): {
                Optional('ip_vrf_id_input'): str,
                Optional('ipv4_src_addr'): str,
                Optional('ipv4_dst_addr'): str,
                Optional('intf_input'): str,
                Optional('intf_output'): str,
                Optional('pkts'): int,
                Optional('ipv6_src_addr'): str,
                Optional('ipv6_dst_addr'): str,
                Optional('trns_src_port'): int,
                Optional('trns_dst_port'): int,
                Optional('flow_direction'): str,
                Optional('vxlan_vni_id'): str,
                Optional('vxlan_vtep_input'): str,
                Optional('vxlan_vtep_output'): str,
                Optional('ip_protocol'): int,
                Optional('ip_tos'): str,
                Optional('ipv4_nxt_hop'): str,
                Optional('ipv4_src_mask'): str,
                Optional('ipv4_dst_mask'): str,
                Optional('tcp_flags'): str,
                Optional('counter_bytes'): int,
                Optional('counter_pkts_long'): int,
                Optional('timestamp_abs_first'): str,
                Optional('timestamp_abs_last'): str,
                Optional('fw_fw_event'): int,
                Optional('datalink_ethertype'): str,
                Optional('datalink_vlan_input'): str,
                Optional('datalink_mac_src_input'): str,
                Optional('datalink_mac_dst_input'): str,
                Optional('interface_input'): str,
            },
        },
        Optional('proto_entries'): {
            Any(): {
                'ip_src_addr': str,
                'ip_dst_addr': str,
                'src_port': int,
                'dst_port': int,
                'ip_port': int,
            }
        },
    }

# =========================================================
# Parser for 'show flow monitor {name} cache'
# =========================================================
class ShowFlowMonitorCache(ShowFlowMonitorCacheSchema):
    ''' Parser for
        "show flow monitor {name} cache"
        "show flow monitor {name} cache filter ipv4 {address_direction1} address {address1} ipv4 {address_direction2} address {address2}"
    '''

    cli_command = [
        'show flow monitor {name} cache',
        'show flow monitor {name} cache filter ipv4 {address_direction1} address {address1} ipv4 {address_direction2} address {address2}'
        ]

    def cli(self, name, address_direction1=None,address1=None,address_direction2=None,address2=None,target='active',output=None):
        if output is None:
            if address_direction1 and address1 and address_direction2 and address2:
                cmd = self.cli_command[1].format(name=name, address_direction1=address_direction1, address_direction2=address_direction2, address1=address1, address2=address2)
                output = self.device.execute(cmd,target=target)
            else:                
                output = self.device.execute(self.cli_command[0].format(name=name))

        # Init vars
        ret_dict = {}
        index = 0

        # Cache type:                               Normal (Platform cache)
        p1 = re.compile(r'^Cache +type: +(?P<cache_type>[\S\s]+)$')

        # Cache size:                                   16
        p2 = re.compile(r'^Cache +size: +(?P<cache_size>\d+)$')

        # Current entries:                               1
        p3 = re.compile(r'^Current +entries: +(?P<current_entries>\d+)$')

        # High Watermark:                                1
        p4 = re.compile(r'^High +Watermark: +(?P<high_water_mark>\d+)$')

        # Flows added:                                   1
        p5 = re.compile(r'^Flows +added: +(?P<flows_added>\d+)$')

        # Flows aged:                                   0
        p6 = re.compile(r'^Flows +aged: +(?P<flows_aged>\d+)$')

        # - Inactive timeout    (    15 secs)         15
        # - Event aged                                 0
        # - Watermark aged                             6
        # - Emergency aged                             0
        p7 = re.compile(r'^- +(?P<key>[\S\s]+?)( +\( +(?P<secs>\d+) +secs\))? +(?P<value>\d+)$')

        # 0   (DEFAULT)   192.168.189.254    192.168.189.253    Null   Te0/0/0.1003     2
        p8 = re.compile(r'^(?P<ip_vrf_id_input>\d+ +\(\S+\)) +(?P<ipv4_src_addr>\S+) '
                        r'+(?P<ipv4_dst_addr>\S+) +(?P<intf_input>\S+) '
                        r'+(?P<intf_output>\S+) +(?P<pkts>\d+)$')

        # 30.1.1.6         224.0.0.5                    0              0       89
        p8_1 = re.compile(r'^(?P<ip_src_addr>\S+) +(?P<ip_dst_addr>\S+) +(?P<src_port>\d+) +(?P<dst_port>\d+) +(?P<ip_port>\d+)$')

        # IP VRF ID INPUT:           0          (DEFAULT)
        p9 = re.compile(r'^IP VRF ID INPUT: +(?P<id>[\S\s]+)$')

        # IPV4 SOURCE ADDRESS:       192.168.189.254
        p10 = re.compile(r'^IPV4 SOURCE ADDRESS: +(?P<src>\S+)$')

        # IPV4 DESTINATION ADDRESS:  192.168.189.253
        p11 = re.compile(r'^IPV4 DESTINATION ADDRESS: +(?P<dst>\S+)$')

        # interface input:           Null
        p12 = re.compile(r'^interface input: +(?P<input>\S+)$')

        # interface output:          Te0/0/0.1003
        p13 = re.compile(r'^interface output: +(?P<output>\S+)$')

        # counter packets:           3
        p14 = re.compile(r'^counter packets: +(?P<pkts>\d+)$')

        # IPV6 SOURCE ADDRESS:       BBBB:172:51:15::11
        p15 = re.compile(r'^IPV6 SOURCE ADDRESS: +(?P<ipv6_src_addr>\S+)$')

        # IPV6 DESTINATION ADDRESS:  BBBB:172:51:15::111
        p16 = re.compile(r'^IPV6 DESTINATION ADDRESS: +(?P<ipv6_dst_addr>\S+)$')

        # TRNS SOURCE PORT:          0
        p17 = re.compile(r'^TRNS SOURCE PORT: +(?P<trns_src_port>\d+)$')

        # TRNS DESTINATION PORT:     0
        p18 = re.compile(r'^TRNS DESTINATION PORT: +(?P<trns_dst_port>\d+)$')

        # FLOW DIRECTION:            Input
        p19 = re.compile(r'^FLOW DIRECTION: +(?P<flow_direction>\S+)$')

        # VXLAN VXLAN VNID:          20015
        p20 = re.compile(r'^VXLAN VXLAN VNID: +(?P<vxlan_vni_id>\S+)$')

        # VXLAN VXLAN VTEP INPUT:    172.11.1.22
        p21 = re.compile(r'^VXLAN VXLAN VTEP INPUT: +(?P<vxlan_vtep_input>\S+)$')

        # VXLAN VXLAN VTEP OUTPUT:   172.11.1.1
        p22 = re.compile(r'^VXLAN VXLAN VTEP OUTPUT: +(?P<vxlan_vtep_output>\S+)$')

        # IP PROTOCOL:               1
        p23 = re.compile(r'^IP PROTOCOL: +(?P<ip_protocol>\d+)$')

        # ipv4 next hop address:     0.0.0.0
        p24 = re.compile(r'^ipv4 next hop address: +(?P<ipv4_nxt_hop>\S+)$')

        # ipv4 source mask:          /0
        p25 = re.compile(r'^ipv4 source mask: +(?P<ipv4_src_mask>\S+)$')

        # ipv4 destination mask:     /0
        p26 = re.compile(r'^ipv4 destination mask: +(?P<ipv4_dst_mask>\S+)$')

        # tcp flags:                 0x00
        p27 = re.compile(r'^tcp flags: +(?P<tcp_flags>\S+)$')

        # counter bytes long:        192
        p28 = re.compile(r'^counter bytes long: +(?P<counter_bytes>\d+)$')

        # counter packets long:      3
        p29 = re.compile(r'^counter packets long: +(?P<counter_pkts_long>\S+)$')

        # timestamp abs first:       07:50:06.900
        p30 = re.compile(r'^timestamp abs first: +(?P<timestamp_abs_first>\S+)$')

        # timestamp abs last:        07:50:58.900
        p31 = re.compile(r'^timestamp abs last: +(?P<timestamp_abs_last>\S+)$')

        # IP TOS:                     0x14
        p32 = re.compile(r'^IP TOS:\s+(?P<ip_tos>\S+)$')

        #fw fw event:                 1
        p33 = re.compile(r'^fw fw event: +(?P<fw_fw_event>\S+)$')

        #DATALINK ETHERTYPE:                      0xFFFF
        p34 = re.compile(r'^DATALINK ETHERTYPE:\s+(?P<datalink_ethertype>[\w\s]+)$')

        # DATALINK VLAN INPUT:                     0
        p35 = re.compile(r'^DATALINK VLAN INPUT:\s+(?P<datalink_vlan_input>[\w\s]+)$')
        
        # DATALINK MAC SOURCE ADDRESS INPUT:       0011.0000.0010
        p36 = re.compile(r'^DATALINK MAC SOURCE ADDRESS INPUT:\s+(?P<datalink_mac_src_input>[\w\s\.]+)$')

        # DATALINK MAC DESTINATION ADDRESS INPUT:       0011.0000.0010
        p37 = re.compile(r'^DATALINK MAC DESTINATION ADDRESS INPUT:\s+(?P<datalink_mac_dst_input>[\w\s\.]+)$')

        # INTERFACE INPUT:                         Po31
        p38 = re.compile(r'^INTERFACE INPUT:\s+(?P<interface_input>[\w\.\/]+)$')

        # entry_dict intializes on p8 or p9 condition
        # but some output doesn't match these conditions.
        # this variable checks the entry_dict created
        entry_dict_created = False

        for line in output.splitlines():
            line = line.strip()

            # Cache type:                               Normal (Platform cache)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'cache_type': group['cache_type']})
                continue

            # Cache size:                                   16
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'cache_size': int(group['cache_size'])})
                continue

            # Current entries:                               1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'current_entries': int(group['current_entries'])})
                continue

            # High Watermark:                                1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'high_water_mark': int(group['high_water_mark'])})
                continue

            # Flows added:                                   1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'flows_added': int(group['flows_added'])})
                continue

            # Flows aged:                                   0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                aged_dict = ret_dict.setdefault('flows_aged', {})
                aged_dict.update({'total': int(group['flows_aged'])})
                continue

            # - Inactive timeout    (    15 secs)         15
            m = p7.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].lower().replace(' ', '_')
                aged_dict.update({key: int(group['value'])})

                secs = group['secs']
                if secs:
                    aged_dict.update({key + '_secs': int(secs)})
                continue

            # 0   (DEFAULT)   192.168.189.254    192.168.189.253    Null   Te0/0/0.1003     2
            m = p8.match(line)
            if m:
                index += 1
                group = m.groupdict()
                entry_dict = ret_dict.setdefault('entries', {}).setdefault(index, {})

                entry_dict.update({'ip_vrf_id_input': group['ip_vrf_id_input']})
                entry_dict.update({'ipv4_src_addr': group['ipv4_src_addr']})
                entry_dict.update({'ipv4_dst_addr': group['ipv4_dst_addr']})
                entry_dict.update({'intf_input': Common.convert_intf_name(group['intf_input'])})
                entry_dict.update({'intf_output': Common.convert_intf_name(group['intf_output'])})
                entry_dict.update({'pkts': int(group['pkts'])})
                entry_dict_created = True
                continue

            # 30.1.1.6         224.0.0.5                    0              0       89
            m = p8_1.match(line)
            if m:
                index += 1
                group = m.groupdict()
                entry_dict = ret_dict.setdefault('proto_entries', {}).setdefault(index, {})
                entry_dict.update({'ip_src_addr': group['ip_src_addr']})
                entry_dict.update({'ip_dst_addr': group['ip_dst_addr']})
                entry_dict.update({'src_port': int(group['src_port'])})
                entry_dict.update({'dst_port': int(group['dst_port'])})
                entry_dict.update({'ip_port': int(group['ip_port'])})
                entry_dict_created = True
                continue

            # IP VRF ID INPUT:           0          (DEFAULT)
            m = p9.match(line)
            if m:
                index += 1
                group = m.groupdict()
                entry_dict = ret_dict.setdefault('entries', {}).setdefault(index, {})
                entry_dict.update({'ip_vrf_id_input': group['id']})
                entry_dict_created = True
                continue

            # IPV4 SOURCE ADDRESS:       192.168.189.254
            m = p10.match(line)
            if m:
                group = m.groupdict()

                if not entry_dict_created:
                    index += 1
                    entry_dict = ret_dict.setdefault('entries', {}).setdefault(
                        index, {})

                entry_dict.update({'ipv4_src_addr': group['src']})

                continue

            # IPV4 DESTINATION ADDRESS:  192.168.189.253
            m = p11.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'ipv4_dst_addr': group['dst']})
                continue

            # interface input:           Null
            m = p12.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'intf_input': Common.convert_intf_name(group['input'])})
                continue

            # interface output:          Te0/0/0.1003
            m = p13.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'intf_output': Common.convert_intf_name(group['output'])})
                continue

            # counter packets:           3
            m = p14.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'pkts': int(group['pkts'])})
                continue

            # IPV6 SOURCE ADDRESS:  BBBB:172:51:15::11
            m = p15.match(line)
            if m:
                group = m.groupdict()

                if not entry_dict_created:
                    index += 1
                    entry_dict = ret_dict.setdefault('entries', {}).setdefault(
                        index, {})

                entry_dict.update({'ipv6_src_addr': group['ipv6_src_addr']})
                continue

            # IPV6 DESTINATION ADDRESS:  BBBB:172:51:15::111
            m = p16.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'ipv6_dst_addr': group['ipv6_dst_addr']})
                continue

            # TRNS SOURCE PORT:          1
            m = p17.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'trns_src_port': int(group['trns_src_port'])})
                continue

            # TRNS DESTINATION PORT:     100
            m = p18.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'trns_dst_port': int(group['trns_dst_port'])})
                continue

            # FLOW DIRECTION:            Input
            m = p19.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'flow_direction': group['flow_direction']})
                continue

            # VXLAN VXLAN VNID:          20015
            m = p20.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'vxlan_vni_id': group['vxlan_vni_id']})
                continue

            # VXLAN VXLAN VTEP INPUT:    172.11.1.2
            m = p21.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'vxlan_vtep_input': group['vxlan_vtep_input']})
                continue

            # VXLAN VXLAN VTEP OUTPUT:   172.11.1.1
            m = p22.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'vxlan_vtep_output': group['vxlan_vtep_output']})
                continue

            # IP PROTOCOL:               6
            m = p23.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'ip_protocol': int(group['ip_protocol'])})
                continue

            # ipv4 next hop address:     0.0.0.0
            m = p24.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'ipv4_nxt_hop': group['ipv4_nxt_hop']})
                continue

            # ipv4 source mask:          /0
            m = p25.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'ipv4_src_mask': group['ipv4_src_mask']})
                continue

            # ipv4 destination mask:     /0
            m = p26.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'ipv4_dst_mask': group['ipv4_dst_mask']})
                continue

            # tcp flags:                 0x00
            m = p27.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'tcp_flags': group['tcp_flags']})
                continue

            # counter bytes long:        4991616
            m = p28.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'counter_bytes': int(group['counter_bytes'])})
                continue

            # counter packets long:      38997
            m = p29.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'counter_pkts_long': int(group['counter_pkts_long'])})
                continue

            # timestamp abs first:       07:49:20.900
            m = p30.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'timestamp_abs_first': group['timestamp_abs_first']})
                continue

            # timestamp abs last:        07:51:29.900
            m = p31.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'timestamp_abs_last': group['timestamp_abs_last']})
                continue
            
            # IP TOS:                     0x14
            m = p32.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'ip_tos': group['ip_tos']})
                continue

            #fw fw event:                 1
            m = p33.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'fw_fw_event': int(group['fw_fw_event'])})
                continue

            #DATALINK ETHERTYPE:                      0xFFFF
            m = p34.match(line)
            if m:        
                group = m.groupdict()
                index += 1
                entry_dict = ret_dict.setdefault('entries', {}).setdefault(index, {})      
                entry_dict.update({'datalink_ethertype': group['datalink_ethertype']})
                entry_dict_created = True
                continue
                            
            # DATALINK VLAN INPUT:                     0
            m = p35.match(line)
            if m:
                group = m.groupdict()
                entry_dict = ret_dict.setdefault('entries', {}).setdefault(index, {})       
                entry_dict.update({'datalink_vlan_input': group['datalink_vlan_input']})
                entry_dict_created = True
                continue
        
            # DATALINK MAC SOURCE ADDRESS INPUT:       0011.0000.0010
            m = p36.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'datalink_mac_src_input': group['datalink_mac_src_input']})
                continue

            # DATALINK MAC DESTINATION ADDRESS INPUT:       0011.0000.0010
            m = p37.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'datalink_mac_dst_input': group['datalink_mac_dst_input']})
                continue

            # INTERFACE INPUT:                         Po31
            m = p38.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({'interface_input': group['interface_input']})
                continue

        return ret_dict

class ShowFlowMonitorCacheRecord(ShowFlowMonitorCache):
    ''' Parser for
        "show flow monitor {name} cache format record"
    '''

    cli_command = 'show flow monitor {name} cache format record'

    def cli(self, name, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(name=name))
        else:
            out = output

        return super().cli(name=name, output=out)


class ShowFlowExporterStatisticsSchema(MetaParser):
    """ Schema for:
            * show flow exporter statistics
            * show flow exporter {exporter} statistics
    """
    schema = {
        'flow_exporter': {
            Any(): {
                'pkt_send_stats': {
                    'last_cleared': str,
                    Optional(Any()): int
                },
                'client_send_stats': {
                    Any(): {
                        'records_added': {
                            'total': int,
                            Optional('sent'): int,
                            Optional('failed'): int
                        },
                        'bytes_added': {
                            'total': int,
                            Optional('sent'): int,
                            Optional('failed'): int
                        }
                    }
                }
            }
        }
    }


class ShowFlowExporterStatistics(ShowFlowExporterStatisticsSchema):
    """ Parser for:
            * show flow exporter statistics
            * show flow exporter {exporter} statistics
    """

    cli_command = ["show flow exporter statistics",
                   "show flow exporter {exporter} statistics"]

    def cli(self, exporter=None, output=None):

        if not output:
            if not exporter:
                output = self.device.execute(self.cli_command[0])
            else:
                output = self.device.execute(self.cli_command[1].format(exporter=exporter))

        # Flow Exporter test
        p1 = re.compile(r"^Flow +Exporter +(?P<exporter>\S+):$")

        # Packet send statistics (last cleared 00:10:10 ago):
        p2 = re.compile(r"^Packet +send +statistics +\(last +cleared +(?P<last_cleared>[\d:]+) +ago\):$")

        # Successfully sent:         10                     (1000 bytes)
        # No FIB:                    10                     (1000 bytes)
        # Adjacency failure:         10                     (1000 bytes)
        # Enqueued to process level: 10                     (1000 bytes)
        # Enqueueing failed:         10                     (1000 bytes)
        # IPC failed:                10                     (1000 bytes)
        # Output failed:             10                     (1000 bytes)
        # Fragmentation failed:      10                     (1000 bytes)
        # Encap fixup failed:        10                     (1000 bytes)
        # CEF not enabled:           10                     (1000 bytes)
        # Reason not given:          10                     (1000 bytes)
        # Rate limited:              10                     (1000 bytes)
        # No destination address:    10                     (1000 bytes)
        p3 = re.compile(r"^(?P<statistic>[\w\s]+): +(?P<pkts>\d+) +\((?P<bytes>\d+) +bytes\)$")

        # Client: client_name
        p4 = re.compile(r"^Client: +(?P<client>[\S\s]+)$")

        # Records added:             10
        p5 = re.compile(r"^Records +added: +(?P<total>\d+)$")

        # Bytes added:               10
        p6 = re.compile(r"^Bytes +added: +(?P<total>\d+)$")

        # - sent:                20
        p7 = re.compile(r"^- +sent: +(?P<sent>\d+)$")

        # - failed to send:      30
        p8 = re.compile(r"^- +failed +to +send: +(?P<failed>\d+)$")

        records_flag = False
        bytes_flag = False
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Flow Exporter test
            m = p1.match(line)
            if m:
                exporter_dict = ret_dict.setdefault('flow_exporter', {})\
                                        .setdefault(m.groupdict()['exporter'], {})
                continue

            # Packet send statistics (last cleared 00:10:10 ago):
            m = p2.match(line)
            if m:
                pkt_stats_dict = exporter_dict.setdefault('pkt_send_stats', {})
                pkt_stats_dict.update({'last_cleared': m.groupdict()['last_cleared']})
                continue

            # Successfully sent:         10                     (1000 bytes)
            # No FIB:                    10                     (1000 bytes)
            # Adjacency failure:         10                     (1000 bytes)
            # Enqueued to process level: 10                     (1000 bytes)
            # Enqueueing failed:         10                     (1000 bytes)
            # IPC failed:                10                     (1000 bytes)
            # Output failed:             10                     (1000 bytes)
            # Fragmentation failed:      10                     (1000 bytes)
            # Encap fixup failed:        10                     (1000 bytes)
            # CEF not enabled:           10                     (1000 bytes)
            # Reason not given:          10                     (1000 bytes)
            # Rate limited:              10                     (1000 bytes)
            # No destination address:    10                     (1000 bytes)
            m = p3.match(line)
            if m:
                key = re.sub(' ', '_', m.groupdict()['statistic']).lower()
                bytes_key = '{key}_bytes'.format(key=key)
                pkt_stats_dict.update({key: int(m.groupdict()['pkts'])})
                pkt_stats_dict.update({bytes_key: int(m.groupdict()['bytes'])})
                continue

            # Client: client_name
            m = p4.match(line)
            if m:
                client_dict = exporter_dict.setdefault('client_send_stats', {})\
                                           .setdefault(m.groupdict()['client'], {})
                continue

            # Records added:             10
            m = p5.match(line)
            if m:
                records_flag = True
                bytes_flag = False

                records_dict = client_dict.setdefault('records_added', {})
                records_dict.update({'total': int(m.groupdict()['total'])})
                continue

            # Bytes added:               10
            m = p6.match(line)
            if m:
                records_flag = False
                bytes_flag = True

                bytes_dict = client_dict.setdefault('bytes_added', {})
                bytes_dict.update({'total': int(m.groupdict()['total'])})
                continue

            # - sent:                20
            m = p7.match(line)
            if m:
                if records_flag:
                    records_dict.update({'sent': int(m.groupdict()['sent'])})
                elif bytes_flag:
                    bytes_dict.update({'sent': int(m.groupdict()['sent'])})
                continue

            # - failed to send:      30
            m = p8.match(line)
            if m:
                if records_flag:
                    records_dict.update({'failed': int(m.groupdict()['failed'])})
                elif bytes_flag:
                    bytes_dict.update({'failed': int(m.groupdict()['failed'])})

        return ret_dict


class ShowFlowMonitorSdwanFlowMonitorStatisticsSchema(MetaParser):
    ''' Schema for show flow monitor sdwan_flow_monitor statistics'''
    schema = {
        "cache_type": str,
        "cache_size": int,
        "current_entries": int,
        Optional("high_watermark"): int,
        "flows_added": int,
        "flows_aged":{
                    "total_flows_aged" : int,
                    Optional("active_timeout_secs"): int,
                    Optional("active_time"): int,
                    Optional("inactive_timeout_secs"):int,
                    Optional("inactive_time"):int
                }
            }


class ShowFlowMonitorSdwanFlowMonitorStatistics(ShowFlowMonitorSdwanFlowMonitorStatisticsSchema):

    """ Parser for "show flow monitor sdwan_flow_monitor statistics" """

    cli_command = "show flow monitor {flow_monitor_name} statistics"

    def cli(self,flow_monitor_name='',output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(flow_monitor_name=flow_monitor_name))
        else:
            out = output

        #Cache type: Normal (Platform cache)
        p1=re.compile(r'Cache+\s+type+\:+\s+(?P<cache_type>[\w\W\s()]+)')

        #Cache size: 200000
        p2=re.compile(r'Cache+\s+size+\:+\s+(?P<cache_size>\d+)')

        #Current entries: 12534
        p3=re.compile(r'Current+\s+entries+\:+\s+(?P<current_entries>\d+)')

        #High Watermark: 16030
        p4=re.compile(r'High+\s+Watermark+\:+\s+(?P<high_watermark>\d+)')

        #Flows added: 197808242
        p5=re.compile(r'Flows+\s+added+\:+\s+(?P<flows_added>\d+)')

        #Flows aged: 197795708
        p6=re.compile(r'Flows+\s+aged+\:+\s+(?P<flows_aged>\d+)')

        #- Active timeout ( 60 secs) 11897289
        p7=re.compile(r'\-+\s+Active+\s+timeout+\s+\(+\s+(?P<active_time_secs>\d+)+\s+secs+\)+\s+(?P<active_time>\d+)')

        #- Inactive timeout ( 10 secs) 185898419
        p8=re.compile(r'\-+\s+Inactive+\s+timeout+\s+\(+\s+(?P<inactive_time_secs>\d+)+\s+secs+\)+\s+(?P<inactive_time>\d+)')


        parsed_dict={}
        check_flag=0

        for line in out.splitlines():
            line = line.strip()
            m1= p1.match(line)
            if m1:
                #{'cache_type':'Normal (Platform cache)'}
                groups=m1.groupdict()
                parsed_dict['cache_type']=groups['cache_type']

            m2= p2.match(line)
            if m2:
                #{'cache_size':'200000'}
                groups=m2.groupdict()
                parsed_dict['cache_size']=int(groups['cache_size'])

            m3= p3.match(line)
            if m3:
                #{'current_entries':'12534'}
                groups=m3.groupdict()
                parsed_dict['current_entries']=int(groups['current_entries'])

            m4= p4.match(line)
            if m4:
                #{'high_watermark':'16030}
                groups=m4.groupdict()
                parsed_dict['high_watermark']=int(groups['high_watermark'])

            m5= p5.match(line)
            if m5:
                #{'flows_added':'197808242'}
                groups=m5.groupdict()
                parsed_dict['flows_added']=int(groups['flows_added'])

            m6= p6.match(line)
            if m6:
                #{'flows_aged':'1997795708'}
                parsed_dict['flows_aged']={}
                cur_dict=parsed_dict['flows_aged']
                groups=m6.groupdict()
                cur_dict['total_flows_aged']=int(groups['flows_aged'])

            m7=p7.match(line)
            if m7:
                #{'active_time_secs':'60','active_time':'11897289'}
                groups=m7.groupdict()
                cur_dict['active_timeout_secs']= int(groups['active_time_secs'])
                cur_dict['active_time']= int(groups['active_time'])

            m8=p8.match(line)
            if m8:
                #{'inactive_time_secs':'10','inactive_time':'185898419'}
                groups=m8.groupdict()
                cur_dict['inactive_timeout_secs']= int(groups['inactive_time_secs'])
                cur_dict['inactive_time']= int(groups['inactive_time'])

        return parsed_dict

# =================================================
# Schema for:
#   * 'show flow monitor all'
# ==================================================

class ShowFlowMonitorAllSchema(MetaParser):
    schema = {
        'flow_monitor_name': {
            Any(): {
                'description': str,
                'record_name': str,
                Optional('exporter_name'): str,
                'cache': {
                    'type': str,
                    'status': str,
                    'size': int,
                    'inactive_timeout': int,
                    'active_timeout': int,
                }
            },
        }
    }

# ===================================
# Parser for:
#   * 'show flow monitor all'
# ===================================

class ShowFlowMonitorAll(ShowFlowMonitorAllSchema):
    cli_command = 'show flow monitor all'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Flow Monitor v4_mon_sgt-output:
        p1 = re.compile(r'^Flow\sMonitor\s(?P<flow_monitor_name>[\w\-]+)\:$')

        # Description:       User defined
        p2 = re.compile(r'^Description:\s+(?P<description>[\w\s\.]+)$')

        # Flow Record:       v4-rec_sgt-output
        p3 = re.compile(r'^Flow\sRecord:\s+(?P<record_name>[\S\s]+)$')

        # Flow Exporter:     StealthWatch_Exporter
        p4 = re.compile(r'^Flow\sExporter:\s+(?P<exporter_name>\S+)$')

        # Cache
        p5 = re.compile(r'^(?P<cache>Cache)\:$')

        # Type:                 normal (Platform cache)
        p6 = re.compile(r'^Type:\s+(?P<type>.*)$')

        # Status:               not allocated
        p7 = re.compile(r'^Status:\s+(?P<status>[\w\s]+)$')

        # Size:                 10000 entries
        p8 = re.compile(r'^Size:\s+(?P<size>\d+)\sentries$')

        # Inactive Timeout:     15 secs
        p9 = re.compile(r'^Inactive\sTimeout:\s+(?P<inactive_timeout>\d+)\ssecs$')

        # Active Timeout:       60 secs
        p10 = re.compile(r'^Active\sTimeout:\s+(?P<active_timeout>\d+)\ssecs$')

        for line in out.splitlines():
            line = line.strip()

            # Flow Monitor v4_mon_sgt-output:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                flow_monitor_name = group['flow_monitor_name']
                flow_dict = ret_dict.setdefault('flow_monitor_name', {}).setdefault(flow_monitor_name, {})
                continue

            # Description:       User defined
            m = p2.match(line)
            if m:
                group = m.groupdict()
                flow_dict['description'] = group['description']
                continue

            # Flow Record:       v4-rec_sgt-output
            m = p3.match(line)
            if m:
                group = m.groupdict()
                flow_dict['record_name'] = group['record_name']
                continue

            # Flow Exporter:     StealthWatch_Exporter
            m = p4.match(line)
            if m:
                group = m.groupdict()
                flow_dict['exporter_name'] = group['exporter_name']
                continue

            # Cache
            m = p5.match(line)
            if m:
                group = m.groupdict()
                cache_dict = flow_dict.setdefault('cache', {})
                continue

            # Type:                 normal (Platform cache)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                cache_dict['type'] = group['type']
                continue

            # Status:               not allocated
            m = p7.match(line)
            if m:
                group = m.groupdict()
                cache_dict['status'] = group['status']
                continue

            # Size:                 10000 entries
            m = p8.match(line)
            if m:
                group = m.groupdict()
                cache_dict['size'] = int(group['size'])
                continue

            # Inactive Timeout:     15 secs
            m = p9.match(line)
            if m:
                group = m.groupdict()
                cache_dict['inactive_timeout'] = int(group['inactive_timeout'])
                continue

            # Active Timeout:       60 secs
            m = p10.match(line)
            if m:
                group = m.groupdict()
                cache_dict['active_timeout'] = int(group['active_timeout'])
                continue

        return ret_dict


class ShowFlowExporterSchema(MetaParser):
    schema = {
        'flow_exporter_name': {
            Any(): {
                'description': str,
                'export_protocol': str,
                'transport_config': {
                    'destination_type': str,
                    'destination_ip_address': str,
                    'source_ip_address': str,
                    'transport_protocol': str,
                    'destination_port': int,
                    'source_port': int,
                    'dscp': str,
                    'ttl': int,
                    'output_features': str,
                }
            }
        }
    }


class ShowFlowExporter(ShowFlowExporterSchema):
    cli_command = 'show flow exporter'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Flow Exporter StealthWatch_Exporter:
        p1 = re.compile(r'^Flow\sExporter\s(?P<flow_exporter_name>\S+)\:$')

        # Description:              Export NetFlow to StealthWatch
        p2 = re.compile(r'^Description:\s+(?P<description>[\S\s]+)$')

        # Export protocol:          NetFlow Version 9
        p3 = re.compile(r'^Export\sprotocol:\s+(?P<export_protocol>[\S\s]+)$')

        # Transport Configuration:
        p4 = re.compile(r'^(?P<transport_config>(Transport Configuration:))$')

        # Destination type:       IP
        p5 = re.compile(r'^Destination\stype:\s+(?P<destination_type>\S+)$')

        # Destination IP address: 19.1.1.19
        p6 = re.compile(r'^Destination\sIP\saddress:\s+(?P<destination_ip_address>\S+)$')

        # Source IP address:      29.29.1.1
        p7 = re.compile(r'^Source\sIP\saddress:\s+(?P<source_ip_address>\S+)$')

        # Transport Protocol:     UDP
        p8 = re.compile(r'^Transport\sProtocol:\s+(?P<transport_protocol>\S+)$')

        # Destination Port:       2055
        p9 = re.compile(r'^Destination\sPort:\s+(?P<destination_port>\d+)$')

        # Source Port:            49165
        p10 = re.compile(r'^Source\sPort:\s+(?P<source_port>\d+)$')

        # DSCP:                   0x0
        p11 = re.compile(r'^DSCP:\s+(?P<dscp>\S+)$')

        # TTL:                    255
        p12 = re.compile(r'^TTL:\s+(?P<ttl>\d+)$')

        # Output Features:        Used
        p13 = re.compile(r'^Output\sFeatures:\s+(?P<output_features>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # Flow Exporter StealthWatch_Exporter:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                if 'flow_exporter_name' not in ret_dict:
                    flow_exp_name = ret_dict.setdefault('flow_exporter_name', {})
                flow_exporter_name = group['flow_exporter_name']
                flow_dict = flow_exp_name.setdefault(flow_exporter_name, {})
                continue

            # Description:              Export NetFlow to StealthWatch
            m = p2.match(line)
            if m:
                group = m.groupdict()
                flow_dict['description'] = group['description']
                continue

            # Export protocol:          NetFlow Version 9
            m = p3.match(line)
            if m:
                group = m.groupdict()
                flow_dict['export_protocol'] = group['export_protocol']
                continue

            # Transport Configuration:
            m = p4.match(line)
            if m:
                group = m.groupdict()
                transport_config = flow_dict.setdefault('transport_config', {})
                continue

            # Destination type:       IP
            m = p5.match(line)
            if m:
                group = m.groupdict()
                transport_config['destination_type'] = group['destination_type']
                continue

            # Destination IP address: 19.1.1.19
            m = p6.match(line)
            if m:
                group = m.groupdict()
                transport_config['destination_ip_address'] = group['destination_ip_address']
                continue

            # Source IP address:      29.29.1.1
            m = p7.match(line)
            if m:
                group = m.groupdict()
                transport_config['source_ip_address'] = group['source_ip_address']
                continue

            # Transport Protocol:     UDP
            m = p8.match(line)
            if m:
                group = m.groupdict()
                transport_config['transport_protocol'] = group['transport_protocol']
                continue

            # Destination Port:       2055
            m = p9.match(line)
            if m:
                group = m.groupdict()
                transport_config['destination_port'] = int(group['destination_port'])
                continue

            # Source Port:            49165
            m = p10.match(line)
            if m:
                group = m.groupdict()
                transport_config['source_port'] = int(group['source_port'])
                continue

            # DSCP:                   0x0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                transport_config['dscp'] = group['dscp']
                continue

            # TTL:                    255
            m = p12.match(line)
            if m:
                group = m.groupdict()
                transport_config['ttl'] = int(group['ttl'])
                continue

            # Output Features:        Used
            m = p13.match(line)
            if m:
                group = m.groupdict()
                transport_config['output_features'] = group['output_features']
                continue
        return ret_dict


class ShowFlowRecordSchema(MetaParser):
    schema = {
        'flow_record_name': {
            Any(): {
                'description': str,
                'no_of_users': int,
                'total_field_space': int,
                'fields': {
                    Optional('match_list'): ListOf(str),
                    Optional('collect_list'): ListOf(str),

                }
            }
        }
    }


class ShowFlowRecord(ShowFlowRecordSchema):

    cli_command= 'show flow record'

    def cli(self,output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        #flow record wireless avc basic:
        p1 = re.compile(r'^flow\srecord\s(?P<flow_record_name>.*):$')

        #Description:        Basic IPv4 Wireless AVC template
        p2 = re.compile(r'^Description:\s+(?P<description>.*)$')

        #No. of users:       0
        p3 = re.compile(r'^No\.\sof\susers\:\s+(?P<no_of_users>\d)$')

        #Total field space:  78 bytes
        p4 = re.compile(r'^Total\sfield\sspace\:\s+(?P<total_field_space>\d+)\sbytes$')

        #Fields:
        p5 = re.compile(r'^(?P<fields>Fields\:)$')

        #match ipv4 protocol
        #match ipv4 source address
        #match ipv4 destination address
        #match transport source-port
        #match transport destination-port
        p6 = re.compile(r'^match\s(?P<match_list>.*)$')

        #collect counter bytes long
        #collect counter packets long
        #collect wireless ap mac address
        #collect wireless client mac address
        p7 = re.compile(r'^collect\s(?P<collect_list>.*)$')

        ret_dict = {}
        match_filed_list = []
        collect_field_list = []

        for line in output.splitlines():
            line = line.strip()

            #flow record wireless avc basic:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                flow_record_name = group['flow_record_name']
                flow_dict = ret_dict.setdefault('flow_record_name', {}).setdefault(flow_record_name, {})
                continue

            ##Description:        Basic IPv4 Wireless AVC template
            m = p2.match(line)
            if m:
                group = m.groupdict()
                flow_dict['description'] = group['description']
                continue

            ##No. of users:       0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                flow_dict['no_of_users'] = int(group['no_of_users'])
                continue

            #Total field space:  49 bytes
            m = p4.match(line)
            if m:
                group = m.groupdict()
                flow_dict['total_field_space'] = int(group['total_field_space'])
                continue

            ##Fields:
            m = p5.match(line)
            if m:
                group = m.groupdict()
                fields_dict = flow_dict.setdefault('fields', {})
                continue

            #match ipv4 protocol
            #match ipv4 source address
            #match ipv4 destination address
            #match transport source-port
            #match transport destination-port
            m = p6.match(line)
            if m:
                group = m.groupdict()
                match_filed = group['match_list']
                match_filed_list = fields_dict.setdefault('match_list', [])
                match_filed_list.append(match_filed)
                continue

            #collect counter bytes long
            #collect counter packets long
            #collect wireless ap mac address
            #collect wireless client mac address
            m = p7.match(line)
            if m:
                group = m.groupdict()
                collect_field = group['collect_list']
                collect_field_list = fields_dict.setdefault('collect_list', [])
                collect_field_list.append(collect_field)
                continue

        return ret_dict


class ShowRunningConfigFlowExporterSchema(MetaParser):
    schema = {
        'flow_exporter_name': {
            Any(): {
                Optional('description'): str,
                Optional('destination'): str,
                Optional('source'): str,
                Optional('dscp'): int,
                Optional('ttl'): int,
                Optional('transport_protocol'): str,
                Optional('transport_protocol_port'): int,
                Optional('export_protocol'): str,
                Optional('options'): ListOf(str),
                Optional('match_counter_packets_long_gt'): int
            }
        }
    }


class ShowRunningConfigFlowExporter(ShowRunningConfigFlowExporterSchema):

    cli_command = 'show running-config flow exporter'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        #flow exporter export_prime1_nf10
        p1 = re.compile(r'flow\s+exporter\s+(?P<flow_exporter_name>.*)$')

        #description test_expoter
        p2 = re.compile(r'description\s+(?P<description>.*)$')

        #destination 10.5.28.112
        p3 = re.compile(r'destination\s+(?P<destination>\S+)$')

        #source Loopback0
        p4 = re.compile(r'source\s+(?P<source>.*)$')

        #dscp 5
        p5 = re.compile(r'dscp\s+(?P<dscp>\d+)$')

        #ttl 64
        p6 = re.compile(r'ttl\s+(?P<ttl>\d+)$')

        #transport udp 555
        p7 = re.compile(r'transport\s+(?P<transport_protocol>\S+)\s+(?P<transport_protocol_port>\d+)$')

        #export-protocol ipfix
        p8 = re.compile(r'export-protocol\s+(?P<export_protocol>\S+)$')

        #option interface-table timeout 10
        #option vrf-table timeout 10
        #option sampler-table
        #option application-table timeout 10
        #option application-attributes timeout 10
        p9 = re.compile(r'option\s+(?P<options>.*)$')

        #match counter packets long gt 128
        p10 = re.compile(r'match\s+counter\s+packets\s+long\s+gt\s+(?P<match_counter_packets_long_gt>\d+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #flow exporter export_prime1_nf10
            m = p1.match(line)
            if m:
                group = m.groupdict()
                flow_exporter_name = group['flow_exporter_name']
                flow_dict = ret_dict.setdefault('flow_exporter_name', {}).setdefault(flow_exporter_name, {})
                continue

            #description test_expoter
            m = p2.match(line)
            if m:
                group = m.groupdict()
                flow_dict['description'] = group['description']
                continue

            #destination 10.5.28.112
            m = p3.match(line)
            if m:
                group = m.groupdict()
                flow_dict['destination'] = group['destination']
                continue

            #source Loopback0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                flow_dict['source'] = group['source']
                continue

            #dscp 5
            m = p5.match(line)
            if m:
                group = m.groupdict()
                flow_dict['dscp'] = int(group['dscp'])
                continue

            #ttl 64
            m = p6.match(line)
            if m:
                group = m.groupdict()
                flow_dict['ttl'] = int(group['ttl'])
                continue

            #transport udp 555
            m = p7.match(line)
            if m:
                group = m.groupdict()
                flow_dict['transport_protocol'] = group['transport_protocol']
                flow_dict['transport_protocol_port'] = int(group['transport_protocol_port'])
                continue

            #export-protocol ipfix
            m = p8.match(line)
            if m:
                group = m.groupdict()
                flow_dict['export_protocol'] = group['export_protocol']
                continue

            #option interface-table timeout 10
            #option vrf-table timeout 10
            #option sampler-table
            m = p9.match(line)
            if m:
                group = m.groupdict()
                option = group['options']
                flow_dict.setdefault('options', []).append(option)
                continue

            #match counter packets long gt 128
            m = p10.match(line)
            if m:
                group = m.groupdict()
                flow_dict['match_counter_packets_long_gt'] = int(group['match_counter_packets_long_gt'])
                continue

        return ret_dict


class ShowRunningConfigFlowRecordSchema(MetaParser):
    schema = {
        'flow_record': {
            Any(): {
                Optional('match_list'): ListOf(str),
                Optional('collect_list'): ListOf(str),
            }
        }
    }

class ShowRunningConfigFlowRecord(ShowRunningConfigFlowRecordSchema):

    cli_command = 'show running-config flow record'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # flow record record_l2_in
        p1 = re.compile(r'^flow\srecord\s(?P<flow_record>.*)$')

        # match datalink ethertype
        # match datalink vlan input
        # match datalink mac source address input
        # match datalink mac destination address input
        p2 = re.compile(r'^match\s(?P<match_list>.*)$')

        # collect counter bytes long
        # collect counter packets long
        # collect timestamp absolute first
        p3 = re.compile(r'^collect\s(?P<collect_list>.*)$')

        ret_dict = {}

        for line in output.splitlines():

            line = line.strip()

            # flow record record_l2_in
            m = p1.match(line)

            if m:
                group = m.groupdict()
                flow_record_name = group['flow_record']
                flow_dict = ret_dict.setdefault('flow_record', {}).setdefault(flow_record_name, {})
                continue

            # match datalink ethertype
            # match datalink vlan input
            # match datalink mac source address input
            # match datalink mac destination address input
            m = p2.match(line)

            if m:
                group = m.groupdict()
                match_list = group['match_list']
                match_filed_list = flow_dict.setdefault('match_list', [])
                match_filed_list.append(match_list)
                continue

            # collect counter bytes long
            # collect counter packets long
            # collect timestamp absolute first
            m = p3.match(line)

            if m:
                group = m.groupdict()
                collect_list = group['collect_list']
                collect_field_list = flow_dict.setdefault('collect_list', [])
                collect_field_list.append(collect_list)
                continue

        return ret_dict

# =================================================
# Schema for:
#   * 'show flow monitor Check'
# ==================================================

class ShowFlowMonitorCheckSchema(MetaParser):
    schema = {
        'flow_monitor_name': {
            Any(): {
                'description': str,
                'record_name': str,
                Optional('exporter_name'): str,
                'cache': {
                    'type': str,
                    'status': str,
                    'size': int,
                    'inactive_timeout': int,
                    'active_timeout': int,
                }
            },
        }
    }

# ===================================
# Parser for:
#   * 'show flow monitor check'
# ===================================

class ShowFlowMonitorCheck(ShowFlowMonitorCheckSchema):
    cli_command = 'show flow monitor'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Flow Monitor v4_mon_sgt-output:
        p1 = re.compile(r'^Flow\sMonitor\s(?P<flow_monitor_name>[\w\-]+)\:$')

        # Description:       User defined
        p2 = re.compile(r'^Description:\s+(?P<description>[\w\s\.]+)$')

        # Flow Record:       v4-rec_sgt-output
        p3 = re.compile(r'^Flow\sRecord:\s+(?P<record_name>[\S\s]+)$')

        # Flow Exporter:     StealthWatch_Exporter
        p4 = re.compile(r'^Flow\sExporter:\s+(?P<exporter_name>\S+)$')

        # Cache
        p5 = re.compile(r'^(?P<cache>Cache)\:$')

        # Type:                 normal (Platform cache)
        p6 = re.compile(r'^Type:\s+(?P<type>.*)$')

        # Status:               not allocated
        p7 = re.compile(r'^Status:\s+(?P<status>[\w\s]+)$')

        # Size:                 10000 entries
        p8 = re.compile(r'^Size:\s+(?P<size>\d+)\sentries$')

        # Inactive Timeout:     15 secs
        p9 = re.compile(r'^Inactive\sTimeout:\s+(?P<inactive_timeout>\d+)\ssecs$')

        # Active Timeout:       60 secs
        p10 = re.compile(r'^Active\sTimeout:\s+(?P<active_timeout>\d+)\ssecs$')

        for line in out.splitlines():
            line = line.strip()

            # Flow Monitor v4_mon_sgt-output:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                flow_monitor_name = group['flow_monitor_name']
                flow_dict = ret_dict.setdefault('flow_monitor_name', {}).setdefault(flow_monitor_name, {})
                continue

            # Description:       User defined
            m = p2.match(line)
            if m:
                group = m.groupdict()
                flow_dict['description'] = group['description']
                continue

            # Flow Record:       v4-rec_sgt-output
            m = p3.match(line)
            if m:
                group = m.groupdict()
                flow_dict['record_name'] = group['record_name']
                continue

            # Flow Exporter:     StealthWatch_Exporter
            m = p4.match(line)
            if m:
                group = m.groupdict()
                flow_dict['exporter_name'] = group['exporter_name']
                continue

            # Cache
            m = p5.match(line)
            if m:
                group = m.groupdict()
                cache_dict = flow_dict.setdefault('cache', {})
                continue

            # Type:                 normal (Platform cache)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                cache_dict['type'] = group['type']
                continue

            # Status:               not allocated
            m = p7.match(line)
            if m:
                group = m.groupdict()
                cache_dict['status'] = group['status']
                continue

            # Size:                 10000 entries
            m = p8.match(line)
            if m:
                group = m.groupdict()
                cache_dict['size'] = int(group['size'])
                continue

            # Inactive Timeout:     15 secs
            m = p9.match(line)
            if m:
                group = m.groupdict()
                cache_dict['inactive_timeout'] = int(group['inactive_timeout'])
                continue

            # Active Timeout:       60 secs
            m = p10.match(line)
            if m:
                group = m.groupdict()
                cache_dict['active_timeout'] = int(group['active_timeout'])
                continue

        return ret_dict

# =================================================================================================================================
# Schema for 'show flow monitor {name} cache filter {int_type} {direction} {interface_name} sort highest {int_type} {direction} {top}'
# =================================================================================================================================
class ShowFlowMonitorCacheFilterInterfaceSchema(MetaParser):
    ''' Schema for "show flow monitor {name} cache filter {int_type} {direction} {interface_name} sort highest {int_type} {direction} {top}" '''

    schema = {
        "processed_flow": int,
        "matched_flow": int,
        "aggregated_flow": int,
        "showing_flow": str,
        Optional("ipv4_source_address"): ListOf(str),
        Optional("ipv4_dest_address"): ListOf(str),
        Optional("trans_source_port"): ListOf(str),
        Optional("trans_dest_port"): ListOf(str),
        Optional("interface_output"): ListOf(str),
        Optional("interface_input_val") : ListOf(str),
        "ip_version": ListOf(str),
        "ip_protocol": ListOf(str),
        Optional("ip_ttl"): ListOf(str),
        Optional("interface_input"): ListOf(str),
        Optional("interface_output_val"): ListOf(str),
        "counter_packets_long": ListOf(str),
        "timestamp_abs_first": ListOf(str),
        "timestamp_abs_last": ListOf(str),
        "counter_bytes_layers_long": ListOf(str),
        Optional("ip_tos"): ListOf(str),
        Optional("ipv6_source_address"): ListOf(str),
        Optional("ipv6_dest_address"): ListOf(str)
    }

# ===================================================================================================================================
# Parser for 'show flow monitor {name} cache filter {int_type} {direction} {interface_name} sort highest {int_type} {direction} {top}'
# ===================================================================================================================================
class ShowFlowMonitorCacheFilterInterface(ShowFlowMonitorCacheFilterInterfaceSchema):
    ''' Parser for
      "show flow monitor {name} cache filter {int_type} {direction} {interface_name} sort highest {int_type} {direction} {top}"
    '''

    cli_command = 'show flow monitor {name} cache filter {int_type} {direction} {interface_name} sort highest {other_int_type} {other_direction} {top}'

    def cli(self, name, int_type, direction, interface_name, top, output=None):
        if output is None:
            cmd = self.cli_command.format(name=name, int_type=int_type, direction=direction, interface_name=interface_name, other_int_type=int_type, other_direction=direction, top=top)
            output = self.device.execute(cmd)
            out = output
        else:
            out = output

        # Init vars
        ret_dict = {}

        # Processed 1032 flows
        p1 = re.compile(r'^Processed (?P<processed_flow>[\d]+) flows$')

        # Matched 479 flows
        p2 = re.compile(r'^Matched (?P<matched_flow>[\d]+) flows$')

        # Aggregated to 479 flows
        p3 = re.compile(r'^Aggregated to (?P<aggregated_flow>[\d]+) flows$')

        # Showing the top 2 flows
        p4 = re.compile(r'^Showing the (?P<showing_flow>[\w\ ]+) flows$')

        # IPV4 SOURCE ADDRESS:        11.11.19.1
        p5 = re.compile(r'^IPV4 SOURCE ADDRESS:        (?P<ipv4_source_address>[\w\.]+)$')

        # IPV4 DESTINATION ADDRESS:   224.0.0.6
        p6 = re.compile(r'^IPV4 DESTINATION ADDRESS:   (?P<ipv4_dest_address>[\w\.]+)$')

        # INTERFACE OUTPUT:           Gi1/0/13
        p7 = re.compile(r'^INTERFACE OUTPUT:           (?P<interface_output>[\w\/]+)$')

        # IP VERSION:                 4
        p8 = re.compile(r'^IP VERSION:                 (?P<ip_version>[\d]+)$')

        # IP PROTOCOL:                89
        p9 = re.compile(r'^IP PROTOCOL:                (?P<ip_protocol>[\d]+)$')

        # IP TTL:                     1
        p10 = re.compile(r'^IP TTL:                     (?P<ip_ttl>[\d]+)$')

        # interface input:            Null
        p11 = re.compile(r'^interface input:            (?P<interface_input>[\w\/]+)$')

        # counter packets long:       3
        p12 = re.compile(r'^counter packets long:       (?P<counter_packets_long>[\d]+)$')

        # timestamp abs first:        17:36:52.000
        p13 = re.compile(r'^timestamp abs first:        (?P<timestamp_abs_first>[\d\:\.]+)$')

        # timestamp abs last:         17:36:53.000
        p14 = re.compile(r'^timestamp abs last:         (?P<timestamp_abs_last>[\d\:\.]+)$')

        # counter bytes layer2 long:  2550
        p15 = re.compile(r'^counter bytes layer2 long:  (?P<counter_bytes_layers_long>[\d]+)$')

        # TRNS SOURCE PORT:           0
        p16 = re.compile(r'^TRNS SOURCE PORT:           (?P<trans_source_port>[\d]+)$')

        # TRNS DESTINATION PORT:      0
        p17 = re.compile(r'^TRNS DESTINATION PORT:      (?P<trans_dest_port>[\d]+)$')

        # INTERFACE INPUT:            Gi1/0/13
        p18 = re.compile(r'^INTERFACE INPUT:            (?P<interface_input_val>[\w\/]+)$')

        # interface output:           Null
        p19 = re.compile(r'^interface output:           (?P<interface_output_val>[\w\/]+)$')

        # IP TOS:                     0x00
        p20 = re.compile(r'^IP TOS:                     (?P<ip_tos>[\w\/]+)$')

        # IPV6 SOURCE ADDRESS:        4100:1:7:33::1
        p21 = re.compile(r'^IPV6 SOURCE ADDRESS:        (?P<ipv6_source_address>[\w\:]+)$')

        # IPV6 DESTINATION ADDRESS:   21:28:1::2
        p22 = re.compile(r'^IPV6 DESTINATION ADDRESS:   (?P<ipv6_dest_address>[\w\:]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Processed 1032 flows
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'processed_flow': int(group['processed_flow'])})
                continue

            # Matched 479 flows
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'matched_flow': int(group['matched_flow'])})
                continue

            # Aggregated to 479 flows
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'aggregated_flow': int(group['aggregated_flow'])})
                continue

            # Showing the top 2 flows
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'showing_flow': group['showing_flow']})
                continue

            # IPV4 SOURCE ADDRESS:        11.11.19.1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ipv4_source_addr_dict = ret_dict.setdefault('ipv4_source_address', [])
                ipv4_source_addr_dict.append(group['ipv4_source_address'])
                continue

            # IPV4 DESTINATION ADDRESS:   224.0.0.6
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ipv4_dest_address = ret_dict.setdefault('ipv4_dest_address', [])
                ipv4_dest_address.append(group['ipv4_dest_address'])
                continue

            # INTERFACE OUTPUT:           Gi1/0/13
            m = p7.match(line)
            if m:
                group = m.groupdict()
                interface_output = ret_dict.setdefault('interface_output', [])
                interface_output.append(group['interface_output'])
                continue
            
            # IP VERSION:                 4
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ip_version = ret_dict.setdefault('ip_version', [])
                ip_version.append(group['ip_version'])
                continue
            
            # IP PROTOCOL:                89
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ip_protocol = ret_dict.setdefault('ip_protocol', [])
                ip_protocol.append(group['ip_protocol'])
                continue
            
            # IP TTL:                     1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ip_ttl = ret_dict.setdefault('ip_ttl', [])
                ip_ttl.append(group['ip_ttl'])
                continue
            
            # interface input:            Null
            m = p11.match(line)
            if m:
                group = m.groupdict()
                interface_input = ret_dict.setdefault('interface_input', [])
                interface_input.append(group['interface_input'])
                continue
            
            # counter packets long:       3
            m = p12.match(line)
            if m:
                group = m.groupdict()
                counter_packets_long = ret_dict.setdefault('counter_packets_long', [])
                counter_packets_long.append(group['counter_packets_long'])
                continue
            
            # timestamp abs first:        17:36:52.000
            m = p13.match(line)
            if m:
                group = m.groupdict()
                timestamp_abs_first = ret_dict.setdefault('timestamp_abs_first', [])
                timestamp_abs_first.append(group['timestamp_abs_first'])
                continue
            
            # timestamp abs last:         17:36:53.000
            m = p14.match(line)
            if m:
                group = m.groupdict()
                timestamp_abs_last = ret_dict.setdefault('timestamp_abs_last', [])
                timestamp_abs_last.append(group['timestamp_abs_last'])
                continue

            # counter bytes layer2 long:  2550
            m = p15.match(line)
            if m:
                group = m.groupdict()
                counter_bytes_layers_long = ret_dict.setdefault('counter_bytes_layers_long', [])
                counter_bytes_layers_long.append(group['counter_bytes_layers_long'])
                continue
            
            # TRNS SOURCE PORT:           0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                trans_source_port = ret_dict.setdefault('trans_source_port', [])
                trans_source_port.append(group['trans_source_port'])
                continue
            
            # TRNS DESTINATION PORT:      0
            m = p17.match(line)
            if m:
                group = m.groupdict()
                trans_dest_port = ret_dict.setdefault('trans_dest_port', [])
                trans_dest_port.append(group['trans_dest_port'])
                continue
            
            # INTERFACE INPUT:            Gi1/0/13
            m = p18.match(line)
            if m:
                group = m.groupdict()
                interface_input_val = ret_dict.setdefault('interface_input_val', [])
                interface_input_val.append(group['interface_input_val'])
                continue
            
            # interface output:           Null
            m = p19.match(line)
            if m:
                group = m.groupdict()
                interface_output_val = ret_dict.setdefault('interface_output_val', [])
                interface_output_val.append(group['interface_output_val'])
                continue

            # IP TOS:                     0x00
            m = p20.match(line)
            if m:
                group = m.groupdict()
                ip_tos = ret_dict.setdefault('ip_tos', [])
                ip_tos.append(group['ip_tos'])
                continue
            
            # IPV6 SOURCE ADDRESS:        4100:1:7:33::1
            m = p21.match(line)
            if m:
                group = m.groupdict()
                ipv6_source_address = ret_dict.setdefault('ipv6_source_address', [])
                ipv6_source_address.append(group['ipv6_source_address'])
                continue
            
            # IPV6 DESTINATION ADDRESS:   21:28:1::2
            m = p22.match(line)
            if m:
                group = m.groupdict()
                ipv6_dest_address = ret_dict.setdefault('ipv6_dest_address', [])
                ipv6_dest_address.append(group['ipv6_dest_address'])
                continue
            
        return ret_dict

# ====================================================================================================================================
# Schema for 'show flow monitor {name} cache filter interface {direction} {interface_name} ipv4 {address_direction} address {address}'
# ====================================================================================================================================
class ShowFlowMonitorCacheFilterInterfaceIPv4Schema(MetaParser):
    ''' Schema for "show flow monitor {name} cache filter interface {direction} {interface_name} ipv4 {address_direction} address {address}" '''

    schema = {
    	'cache_type': str,
    	'cache_size': str,
    	'current_entries':str,
    	'high_watermark': str,
    	'flows_added': str,
    	'flows_not_added': str,
    	'flows_aged': str,
    	'flows' : {
    		Any() : { # index
				'ipv4_source_address': str,
				'ipv4_destination_address': str,
				'source_port': str,
				'destination_port': str,
				'vpn_id': str,
				'ip_protocol': str,
				'tcp_flags': str,
				'interface_input': str,
				'interface_output': str,
				'counter_bytes_long': str,
				'counter_packets_long': str,
				'timestamp_abs_first': str,
				'timestamp_abs_last': str,
				'flow_end_reason': str,
				'connection_initiator': str,
				'interface_overlay_session_id_input': str,
				'interface_overlay_session_id_output': str,
				'connection_connection_id_long': str,
				'drop_cause_id': str,
				'counter_bytes_drop_long': str,
				'sdwan_sla_not_met': str,
				'sdwan_preferred_color_not_met': str,
				'sdwan_queue_id': str,
				'counter_packets_drop_long': str,
				'ip_tos': str,
				'ip_dscp': str,
				'ip_dscp_output': str,
				'application_name': str,
			}
    	}
	}

# ====================================================================================================================================
# Parser for 'show flow monitor {name} cache filter interface {direction} {interface_name} ipv4 {address_direction} address {address}'
# ====================================================================================================================================
class ShowFlowMonitorCacheFilterInterfaceIPv4(ShowFlowMonitorCacheFilterInterfaceIPv4Schema):
    ''' Parser for
      "show flow monitor {name} cache filter interface {direction} {interface_name} ipv4 {address_direction} address {address}"
    '''

    cli_command = 'show flow monitor {name} cache filter interface {direction} {interface_name} ipv4 {address_direction} address {address}'

    def cli(self, name='', direction='', interface_name='', address_direction='', address='', output=None):
        if output is None:
            cmd = self.cli_command.format(name=name, direction=direction, interface_name=interface_name, address_direction=address_direction, address=address)
            output = self.device.execute(cmd)
            out = output
        else:
            out = output

        # Init vars
        ret_dict = {}
        index = 0

        #  Cache type:                               Normal (Platform cache)
        p1_1 = re.compile(r'^\s*Cache\s+type:\s+(?P<cache_type>.*)$')

        #  Cache size:                              1000000
        p1_2 = re.compile(r'^\s*Cache\s+size:\s+(?P<cache_size>\d+)$')
        
        #  Current entries:                               5
        p1_3 = re.compile(r'^\s*Current\s+entries:\s+(?P<current_entries>\d+)$')

        #  High Watermark:                          1003094
        p1_4 = re.compile(r'^\s*High\s+Watermark:\s+(?P<high_watermark>\d+)$')

        #  Flows added:                          2470340673
        p1_5 = re.compile(r'^\s*Flows\s+added:\s+(?P<flows_added>\d+)$')

        #  Flows not added:                      26936258373
        p1_6 = re.compile(r'^\s*Flows\s+not\s+added:\s+(?P<flows_not_added>\d+)$')

        #  Flows aged:                           2470340668
        p1_7 = re.compile(r'^\s*Flows\s+aged:\s+(?P<flows_aged>\d+)$')

        #IPV4 SOURCE ADDRESS:                  121.0.5.2
        p2_1 = re.compile(r'^\s*IPV4\s+SOURCE\s+ADDRESS\s*:\s+(?P<ipv4_source_address>[\d\.]+)$')

        #IPV4 DESTINATION ADDRESS:             106.0.5.2
        p2_2 = re.compile(r'^\s*IPV4\s+DESTINATION\s+ADDRESS\s*:\s+(?P<ipv4_destination_address>[\d\.]+)$')

        #TRNS SOURCE PORT:                     1025
        p2_3 = re.compile(r'^\s*TRNS\s+SOURCE\s+PORT\s*:\s+(?P<source_port>\d+)$')

        #TRNS DESTINATION PORT:                63
        p2_4 = re.compile(r'^\s*TRNS\s+DESTINATION\s+PORT\s*:\s+(?P<destination_port>\d+)$')

        #IP VPN ID:                            5
        p2_5 = re.compile(r'^\s*IP\s+VPN\s+ID\s*:\s+(?P<vpn_id>\d+)$')

        #IP PROTOCOL:                          17
        p2_6 = re.compile(r'^\s*IP\s+PROTOCOL\s*:\s+(?P<ip_protocol>\d+)$')

        #tcp flags:                            0x18
        p2_7 = re.compile(r'^\s*tcp\s+flags\s*:\s+(?P<tcp_flags>.*)$')

        #interface input:                      Hu0/1/2.5
        p2_8 = re.compile(r'^\s*interface\s+input\s*:\s+(?P<interface_input>.*)$')

        #interface output:                     Hu0/1/0.3
        p2_9 = re.compile(r'^\s*interface\s+output\s*:\s+(?P<interface_output>.*)$')

        #counter bytes long:                   24686856
        p2_10 = re.compile(r'^\s*counter\s+bytes\s+long\s*:\s+(?P<counter_bytes_long>\d+)$')

        #counter packets long:                 62620
        p2_11 = re.compile(r'^\s*counter\s+packets\s+long\s*:\s+(?P<counter_packets_long>\d+)$')

        #timestamp abs first:                  15:53:01.433
        p2_12 = re.compile(r'^\s*timestamp\s+abs\s+first\s*:\s+(?P<timestamp_abs_first>[\d\:\.]+)$')

        #timestamp abs last:                   15:53:05.612
        p2_13 = re.compile(r'^\s*timestamp\s+abs\s+last\s*:\s+(?P<timestamp_abs_last>[\d\:\.]+)$')

        #flow end reason:                      Not determined
        p2_14 = re.compile(r'^\s*flow\s+end\s+reason\s*:\s+(?P<flow_end_reason>.*)$')

        #connection initiator:                 Initiator
        p2_15 = re.compile(r'^\s*connection\s+initiator\s*:\s+(?P<connection_initiator>.*)$')

        #interface overlay session id input:   0
        p2_16 = re.compile(r'^\s*interface\s+overlay\s+session\s+id\s+input\s*:\s+(?P<interface_overlay_session_id_input>\d+)$')

        #interface overlay session id output:  42
        p2_17 = re.compile(r'^\s*interface\s+overlay\s+session\s+id\s+output\s*:\s+(?P<interface_overlay_session_id_output>\d+)$')

        #connection connection id long:        0x9288A0F00018F2AD
        p2_18 = re.compile(r'^\s*connection\s+connection\s+id\s+long\s*:\s+(?P<connection_connection_id_long>.*)$')

        #drop cause id:                        0
        p2_19 = re.compile(r'^\s*drop\s+cause\s+id\s*:\s+(?P<drop_cause_id>\d+)$')

        #counter bytes drop long:              0
        p2_20 = re.compile(r'^\s*counter\s+bytes\s+drop\s+long\s*:\s+(?P<counter_bytes_drop_long>\d+)$')

        #sdwan sla not met :                   0
        p2_21 = re.compile(r'^\s*sdwan\s+sla\s+not\s+met\s*:\s+(?P<sdwan_sla_not_met>\d+)$')

        #sdwan preferred color not met :       0
        p2_22 = re.compile(r'^\s*sdwan\s+preferred\s+color\s+not\s+met\s*:\s+(?P<sdwan_preferred_color_not_met>\d+)$')

        #sdwan queue id :                      2
        p2_23 = re.compile(r'^\s*sdwan\s+queue\s+id\s*:\s+(?P<sdwan_queue_id>\d+)$')

        #counter packets drop long:            0
        p2_24 = re.compile(r'^\s*counter\s+packets\s+drop\s+long\s*:\s+(?P<counter_packets_drop_long>\d+)$')

        #ip tos:                               0x00
        p2_25 = re.compile(r'^\s*ip\s+tos\s*:\s+(?P<ip_tos>.*)$')

        #ip dscp:                              0x00
        p2_26 = re.compile(r'^\s*ip\s+dscp\s*:\s+(?P<ip_dscp>.*)$')

        #ip dscp output:                       0x00
        p2_27 = re.compile(r'^\s*ip\s+dscp\s+output\s*:\s+(?P<ip_dscp_output>.*)$')

        #application name:                     layer7 unknown
        p2_28 = re.compile(r'^\s*application\s+name\s*:\s+(?P<application_name>.*)$')


        for line in output.splitlines():

            #  Cache type:                               Normal (Platform cache)
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['cache_type'] = group['cache_type']

            #  Cache size:                              1000000
            m = p1_2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['cache_size'] = group['cache_size']

            #  Current entries:                               5
            m = p1_3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['current_entries'] = group['current_entries']

            #  High Watermark:                          1003094
            m = p1_4.match(line)
            if m:
                group = m.groupdict()
                ret_dict['high_watermark'] = group['high_watermark']

            #  Flows added:                          2470340673
            m = p1_5.match(line)
            if m:
                group = m.groupdict()
                ret_dict['flows_added'] = group['flows_added']

            #  Flows not added:                      26936258373
            m = p1_6.match(line)
            if m:
                group = m.groupdict()
                ret_dict['flows_not_added'] = group['flows_not_added']

            #  Flows aged:                           2470340668
            m = p1_7.match(line)
            if m:
                group = m.groupdict()
                ret_dict['flows_aged'] = group['flows_aged']

            #IPV4 SOURCE ADDRESS:                  121.0.5.2
            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                index += 1
                flow_dict = ret_dict.setdefault('flows', {}).setdefault(index, {})
                flow_dict['ipv4_source_address'] = group['ipv4_source_address']

            #IPV4 DESTINATION ADDRESS:             106.0.5.2
            m = p2_2.match(line)
            if m:
                group = m.groupdict()
                flow_dict['ipv4_destination_address'] = group['ipv4_destination_address']

            #TRNS SOURCE PORT:                     1025
            m = p2_3.match(line)
            if m:
                group = m.groupdict()
                flow_dict['source_port'] = group['source_port']

            #TRNS DESTINATION PORT:                63
            m = p2_4.match(line)
            if m:
                group = m.groupdict()
                flow_dict['destination_port'] = group['destination_port']

            #IP VPN ID:                            5
            m = p2_5.match(line)
            if m:
                group = m.groupdict()
                flow_dict['vpn_id'] = group['vpn_id']

            #IP PROTOCOL:                          17
            m = p2_6.match(line)
            if m:
                group = m.groupdict()
                flow_dict['ip_protocol'] = group['ip_protocol']
                
            #tcp flags:                            0x18
            m = p2_7.match(line)
            if m:
                group = m.groupdict()
                flow_dict['tcp_flags'] = group['tcp_flags']

            #interface input:                      Hu0/1/2.5
            m = p2_8.match(line)
            if m:
                group = m.groupdict()
                flow_dict['interface_input'] = group['interface_input']

            #interface output:                     Hu0/1/0.3
            m = p2_9.match(line)
            if m:
                group = m.groupdict()
                flow_dict['interface_output'] = group['interface_output']

            #counter bytes long:                   24686856
            m = p2_10.match(line)
            if m:
                group = m.groupdict()
                flow_dict['counter_bytes_long'] = group['counter_bytes_long']

            #counter packets long:                 62620
            m = p2_11.match(line)
            if m:
                group = m.groupdict()
                flow_dict['counter_packets_long'] = group['counter_packets_long']

            #timestamp abs first:                  15:53:01.433
            m = p2_12.match(line)
            if m:
                group = m.groupdict()
                flow_dict['timestamp_abs_first'] = group['timestamp_abs_first']

            #timestamp abs last:                   15:53:05.612
            m = p2_13.match(line)
            if m:
                group = m.groupdict()
                flow_dict['timestamp_abs_last'] = group['timestamp_abs_last']

            #flow end reason:                      Not determined
            m = p2_14.match(line)
            if m:
                group = m.groupdict()
                flow_dict['flow_end_reason'] = group['flow_end_reason']

            #connection initiator:                 Initiator
            m = p2_15.match(line)
            if m:
                group = m.groupdict()
                flow_dict['connection_initiator'] = group['connection_initiator']

            #interface overlay session id input:   0
            m = p2_16.match(line)
            if m:
                group = m.groupdict()
                flow_dict['interface_overlay_session_id_input'] = group['interface_overlay_session_id_input']

            #interface overlay session id output:  42
            m = p2_17.match(line)
            if m:
                group = m.groupdict()
                flow_dict['interface_overlay_session_id_output'] = group['interface_overlay_session_id_output']

            #connection connection id long:        0x9288A0F00018F2AD
            m = p2_18.match(line)
            if m:
                group = m.groupdict()
                flow_dict['connection_connection_id_long'] = group['connection_connection_id_long']

            #drop cause id:                        0
            m = p2_19.match(line)
            if m:
                group = m.groupdict()
                flow_dict['drop_cause_id'] = group['drop_cause_id']

            #counter bytes drop long:              0
            m = p2_20.match(line)
            if m:
                group = m.groupdict()
                flow_dict['counter_bytes_drop_long'] = group['counter_bytes_drop_long']

            #sdwan sla not met :                   0
            m = p2_21.match(line)
            if m:
                group = m.groupdict()
                flow_dict['sdwan_sla_not_met'] = group['sdwan_sla_not_met']

            #sdwan preferred color not met :       0
            m = p2_22.match(line)
            if m:
                group = m.groupdict()
                flow_dict['sdwan_preferred_color_not_met'] = group['sdwan_preferred_color_not_met']

            #sdwan queue id :                      2
            m = p2_23.match(line)
            if m:
                group = m.groupdict()
                flow_dict['sdwan_queue_id'] = group['sdwan_queue_id']

            #counter packets drop long:            0
            m = p2_24.match(line)
            if m:
                group = m.groupdict()
                flow_dict['counter_packets_drop_long'] = group['counter_packets_drop_long']

            #ip tos:                               0x00
            m = p2_25.match(line)
            if m:
                group = m.groupdict()
                flow_dict['ip_tos'] = group['ip_tos']

            #ip dscp:                              0x00
            m = p2_26.match(line)
            if m:
                group = m.groupdict()
                flow_dict['ip_dscp'] = group['ip_dscp']

            #ip dscp output:                       0x00
            m = p2_27.match(line)
            if m:
                group = m.groupdict()
                flow_dict['ip_dscp_output'] = group['ip_dscp_output']

            #application name:                     layer7 unknown
            m = p2_28.match(line)
            if m:
                group = m.groupdict()
                flow_dict['application_name'] = group['application_name']

        return ret_dict
