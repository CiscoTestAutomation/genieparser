"""  show_clns.py
   supported commands:
        *  show clns interface
        *  show clns interface <interface>
        *  show clns protocol
        *  show clns neighbor detail
        *  show clns is-neighbor detail
        *  show clns traffic
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                               Any, \
                                               Optional

from genie.libs.parser.utils.common import Common

class ShowClnsInterfaceSchema(MetaParser):
    """Schema for show clns interface,
                  show clns interface {interface}"""

    schema = {

    }

class ShowClnsInterface(ShowClnsInterfaceSchema):
    """Parser for show clns interface
                  show clns interface {interface}"""

    cli_command = ['show clns interface {interface}','show clns interface']

    def cli(self,interface="",output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[0].format(interface=interface)
            else:
                cmd = self.cli_command[1]

            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        result_dict = {}
        feature_flag = False

        # GigabitEthernet1 is up, line protocol is up
        # TokenRing 0 is administratively down, line protocol is down
        p1 = re.compile(r'^(?P<interface>[\S\s]+)is +(?P<status>[\w\s]+), +line +protocol +is +(?P<line_protocol>\w+)$')
        #   CLNS protocol processing disabled
        p2 = re.compile(r'^CLNS +protocol +processing +disabled$')
        #   Checksums enabled, MTU 1497, Encapsulation SAP
        p3 = re.compile(r'^Checksums +(?P<checksum>\w+), +MTU +(?P<mtu>\d+), +Encapsulation +(?P<encapsulation>\w+)$')
        #   ERPDUs enabled, min. interval 10 msec.
        p4 = re.compile(r'^ERPDUs +(?P<erpdus>\w+), +min. +interval +(?P<min_interval>\d+) +msec.$')
        #   CLNS fast switching enabled
        #   CLNS SSE switching disabled
        p5 = re.compile(r'^CLNS +(?P<fast_sse>\w+) +switching +(?P<switching_status>\w+)$')
        #   DEC compatibility mode OFF for this interface
        p6 = re.compile(r'^DEC +compatibility +mode +(?P<dec_compatibilty_mod>\w+) +for +this +interface$')
        #   Next ESH/ISH in 20 seconds
        p7 = re.compile(r'^Next +ESH/ISH +in +(?P<next_esh_ish>\d+) +seconds$')
        #   Routing Protocol: IS-IS (test)
        p8 = re.compile(r'^Routing +Protocol: +(?P<routing_protocol>[\S]+) +\((?P<process_id>\w+)\)$')
        #     Circuit Type: level-1-2
        p9 = re.compile(r'^Circuit +Type: +(?P<circut_type>\S+)$')
        #     Interface number 0x1, local circuit ID 0x1
        p10 = re.compile(r'^Interface +number +(?P<interface_number>\w+), +local +circuit +ID +(?P<loacl_circut>\w+)$')
        #     Neighbor Extended Local Circuit ID: 0x0
        p11 = re.compile(r'^Neighbor +Extended +Local +Circuit +ID: +(?P<neighbor_extended_local_circute_id>\w+)$')
        #     Level-1 Metric: 10, Priority: 64, Circuit ID: R2.01
        p12 = re.compile(r'^(?P<level>\S+) +Metric: +(?P<level_metric>\d+), Priority: +(?P<priority>\d+), Circuit ID: +(?P<curcuit_id>\S+)$')
        #     DR ID: R2.01
        p13 = re.compile(r'^DR +ID: +(?P<dr_id>\S+)$')
        #     Level-1 IPv6 Metric: 10
        p14 = re.compile(r'^(?P<level>\S+) +IPv6 +Metric: +(?P<level_ipv6_metric>\d+)$')
        #     Number of active level-1 adjacencies: 1
        p15 = re.compile(r'^Number +of +active +(?P<level>\S+) +adjacencies: +(?P<adjacencies>\d+)$')
        #     Next IS-IS LAN Level-1 Hello in 1 seconds
        p16 = re.compile(r'^Next +IS\-IS +LAN (?P<level>\S+) +Hello +in +(?P<level_hello>\d+) +(milli)?seconds$')
        #     Next IS-IS LAN Level-2 Hello in 645 milliseconds

        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet1 is up, line protocol is up
            m = p1.match(line)
            if m:
                group = m.groupdict()
                clns_dict = result_dict.setdefault('interfaces', {}).setdefault(group['interface'], {})
                clns_dict.update({'line_protocol': group['line_protocol']})
                continue

            #   CLNS protocol processing disabled
            m = p2.match(line)
            if m:
                clns_dict.update({'clns_protocol_processing_enabled': False})
                continue

            #   Checksums enabled, MTU 1497, Encapsulation SAP
            m = p3.match(line)
            if m:
                group = m.groupdict()
                clns_dict.update({'checksum': True if 'enabled' in group['checksum'] else False})
                clns_dict.update({'mtu': int(group['mtu'])})
                clns_dict.update({'encapsulation': group['encapsulation']})
                continue

            #   ERPDUs enabled, min. interval 10 msec.
            m = p4.match(line)
            if m:
                group = m.groupdict()
                clns_dict.update({'erpdus': True if 'enabled' in group['erpdus'] else False})
                clns_dict.update({'min_interval_msec': int(group['min_interval'])})
                continue

            #   CLNS fast switching enabled
            #   CLNS SSE switching disabled
            m = p5.match(line)
            if m:
                group = m.groupdict()
                clns_dict.update({'{}_switching'.format(fast_sse): True if 'enabled' in group['switching_status'] else False})
                continue

            #   DEC compatibility mode OFF for this interface
            m = p6.match(line)
            if m:
                group = m.groupdict()
                clns_dict.update({'dec_compatibilty_mod': group['dec_compatibilty_mod']})
                continue

            #   Next ESH/ISH in 20 seconds
            m = p7.match(line)
            if m:
                group = m.groupdict()
                clns_dict.update({'next_esh_ish': int(group['next_esh_ish'])})
                continue

            # Routing Protocol: IS-IS (test)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                instance_id = group['process_id']
                isis_dict = clns_dict.setdefault('routing_protocol',{}).setdefault(group['routing_protocol'],{})
                continue

            #     Circuit Type: level-1-2
            m = p9.match(line)
            if m:
                group = m.groupdict()
                clns_dict.update({'routing_protocol': group['routing_protocol']})
                clns_dict.update({'level_type': group['circut_type']})
                continue

            #     Interface number 0x1, local circuit ID 0x1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                isis_dict.update({'interface_name': group['interface_number']})
                isis_dict.update({'loacl_circut_id': group['loacl_circut']})
                continue

            #     Neighbor Extended Local Circuit ID: 0x0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                isis_dict.update({'neighbor_extended_local_circut_id': group['neighbor_extended_local_circute_id']})
                continue

            #     Level-1 Metric: 10, Priority: 64, Circuit ID: R2.01
            m = p12.match(line)
            if m:
                group = m.groupdict()
                level = group['level']
                if 'level-1' in level:
                    flag_level_1 = True
                    flag_level_2 = False

                if 'level-2' in level:
                    flag_level_2 = True
                    flag_level_1 = False

                level_dict = isis_dict.setdefault(level,{})
                level_dict.update({'metric': group['level_metric'])
                level_dict.update({'priority': group['priority'])
                level_dict.update({'circuit_id': group['circuit_id'])
                continue

            #     DR ID: R2.01
            m = p13.match(line)
            if m:
                group = m.groupdict()
                if flag_level_1:
                    level_dict = isis_dict_dict.setdefault('level_1', {})
                if flag_level_2:
                    level_dict = isis_dict_dict.setdefault('level_2', {})

                level_dict.update({'dr_id': group['dr_id'])
                continue

            #     Level-1 IPv6 Metric: 10
            m = p14.match(line)
            if m:
                group = m.groupdict()
                level_dict.update({'ipv6_metric': int(group['level_ipv6_metric'])
                continue

            #     Number of active level-1 adjacencies: 1
            m = p15.match(line)
            if m:
                group = m.groupdict()
                level_dict.update({'ipv6_metric': int(group['level_ipv6_metric'])
                continue

            # Next IS-IS LAN Level-1 Hello in 1 seconds
            m = p15.match(line)
            if m:
                group = m.groupdict()
                level_dict.update({'hello_interval': int(group['level_hello'])
                continue


        return result_dict


class ShowClnsProtocolSchema(MetaParser):
    """Schema for show clns protocol"""

    schema = {

    }

class ShowClnsProtocol(ShowClnsProtocolSchema):
    """Parser for show clns protocol"""

    cli_command = 'show clns protocol'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        result_dict = {}
        # IS-IS Router: VRF1 (0x10001)
        p1 = re.compile(r'^\s*IS-IS Router: +(?P<tag_process>\w+) +\((?P<tag>\w+)\)$')
        # System Id: 2222.2222.2222.00  IS-Type: level-1-2
        p2 = re.compile(r'^\s*System Id: +(?P<sytem_id>[\w\.\+) +IS\-Type: +(?P<is_type>[\w\-]+)$')
        # Manual area address(es):
        p3 = re.compile(r'^\s*Manual +area +address\(es\):$')
        # 49.0001
        p4 = re.compile(r'^\s*(?P<area_address>[\d\.]+)$')
        # Routing for area address(es):
        p5 = re.compile(r'^\s*Routing +for +area +address\(es\):$')
        # Interfaces supported by IS-IS:
        p6 = re.compile(r'^\s*Interfaces +supported +by +IS\-IS:$')
        # GigabitEthernet4 - IP - IPv6
        # Loopback1 - IP - IPv6
        p7 = re.compile(r'^\s*(?P<interface>^[A-Z][\S]+) \- +(?P<topology>[\w\-\s]+)$')
        # Redistribute:
        p8 = re.compile(r'^\s*Redistribute:$')
        #   static (on by default)
        p9 = re.compile(r'^(?P<space>\s{4})(?P<redistribute>[a-z\s\(\)]+)$')
        # Distance for L2 CLNS routes: 110
        p10 = re.compile(r'^\s*Distance +for +L2 +CLNS +routes: +(?P<distance>\d+)$')
        # RRR level: none
        p11 = re.compile(r'^\s*RRR +level: +(?P<rrr_level>\w+)$')
        # Generate narrow metrics: none
        p12 = re.compile(r'^\s*Generate +narrow +metrics: +(?P<generate_narrow_metric>\S+)$')
        # Accept narrow metrics:   none
        p15 = re.compile(r'^\s*Accept +narrow +metrics: +(?P<accept_narrow_metric>\S+)$')
        # Generate wide metrics:   level-1-2
        p14 = re.compile(r'^\s*Generate +wide +metrics: +(?P<generate_wide_metric>\S+)$')
        # Accept wide metrics:     level-1-2
        p15 = re.compile(r'^\s*Accept +wide +metrics: +(?P<accept_wide_metric>\S+)$')

        for line in out.splitlines():
            line = line.rstrip()


            m = p1.match(line)
            if m:
                group = m.groupdict()
                continue

            return result_dict


class ShowClnsNeighborsDetailSchema(MetaParser):
    """Schema for show clns neighbors detail"""

    schema = {

    }

class ShowClnsNeighborsDetail(ShowClnsNeighborsDetailSchema):
    """Parser for show clns neighbors detail"""

    cli_command = 'show clns neighbors detail'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        result_dict = {}

        # Tag VRF1:
        p1 = re.compile(r'^Tag +(?P<tag>\S+):$')
        # System Id       Interface     SNPA                State  Holdtime  Type Protocol
        # R7              Gi4           5e00.c006.0007      Up     26        L2   M-ISIS
        p2 = re.compile(r'^(?P<system_id>[\w\.] +(?P<interface>\S+) +(?P<snpa>[\w\.]+)'
                        ' +(?P<state>\w+) +(?P<holdtime>\d+) +(?P<type>\w+) +(?P<protocol>[\w\-]+)$')
        #   Area Address(es): 49.0002
        p3 = re.compile(r'^Area +Address(es): +(?P<area_address>\S+)$')
        #   IP Address(es):  20.2.7.7*
        p4 = re.compile(r'^IP +Address(es): +(?P<ip_address>\S+)$')
        #   IPv6 Address(es): FE80::5C00:C0FF:FE06:7
        p5 = re.compile(r'^IPv6 +Address(es): +(?P<ipv6_address>\S+)$')
        #   Uptime: 00:23:58
        p6 = re.compile(r'^Uptime: +(?P<uptime>[\w\:]+)$')
        #   NSF capable
        p7 = re.compile(r'^NSF +(?P<nfs>\w+)$')
        #   Topology: IPv4, IPv6
        p8 = re.compile(r'^Topology: +(?P<topology>[\S\s]+)$')
        #   Interface name: GigabitEthernet4
        p9 = re.compile(r'^Interface +name: +(?P<interface>\S+)$')
        
        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                continue

            return result_dict


class ShowClnsIsNeighborsDetailSchema(MetaParser):
    """Schema for show clns is-neighbors detail"""

    schema = {

    }

class ShowClnsIsNeighborsDetail(ShowClnsIsNeighborsDetailSchema):
    """Parser for show clns is-neighbors detail"""

    cli_command = 'show clns is-neighbors detail'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        result_dict = {}

        # Tag VRF1:
        p1 = re.compile(r'^Tag +(?P<process_tag>\S+):$')
        # System Id       Interface     State  Type Priority  Circuit Id         Format
        # R7              Gi4           Up     L2   64        R2.01              Phase V
        p2 = re.compile(r'^(?P<system_id>[\w\.] +(?P<interface>\S+) +(?P<state>\w+)'
                        ' +(?P<type>\w+) +(?P<priority>\d+) +(?P<circut_id>[\w\.]+) +(?P<format>[\S\s]+)$')
        #   Area Address(es): 49.0002
        p3 = re.compile(r'^Area +Address(es): +(?P<area_address>\S+)$')
        #   IP Address(es):  20.2.7.7*
        p4 = re.compile(r'^IP +Address(es): +(?P<ip_address>\S+)$')
        #   IPv6 Address(es): FE80::5C00:C0FF:FE06:7
        p5 = re.compile(r'^IPv6 +Address(es): +(?P<ipv6_address>\S+)$')
        #   Uptime: 00:24:24
        p6 = re.compile(r'^Uptime: +(?P<uptime>[\w\:]+)$')
        #   NSF capable
        p7 = re.compile(r'^NSF +(?P<nfs>\w+)$')
        #   Topology: IPv4, IPv6
        p8 = re.compile(r'^Topology: +(?P<topology>[\S\s]+)$')
        #   Interface name: GigabitEthernet4
        p9 = re.compile(r'^Interface +name: +(?P<interface>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                continue

            return result_dict


class ShowClnsTrafficSchema(MetaParser):
    """Schema for show clns traffic"""

    schema = {

    }

class ShowClnsTraffic(ShowClnsTrafficSchema):
    """Parser for show clns traffic"""

    cli_command = 'show clns traffic'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        result_dict = {}

        # CLNS:  Time since last clear: never
        p1 = re.compile(r'^CLNS:  +Time +since +last +clear: (?P<last_clear>\w+)$')
        # CLNS & ESIS Output: 168, Input: 4021
        p2 = re.compile(r'^CLNS \& +ESIS +Output: +(?P<clns_output>\d+) +(?P<clns_input>\d+)$')
        # Dropped Protocol not enabled on interface: 0
        p3 = re.compile(r'^Dropped Protocol not enabled on interface: +(?P<dropped_protocol>\d+)$')
        # CLNS Local: 0, Forward: 0
        p4 = re.compile(r'^CLNS +Local: +(?P<clns_local>\d+), Forward: +(?P<clns_forward>\d+)$')
        # CLNS Discards:
        p5 = re.compile(r'CLNS +Discards:$')
        #   Hdr Syntax: 0, Checksum: 0, Lifetime: 0, Output cngstn: 0
        p6 = re.compile(r'^Hdr +Syntax: +(?P<hdr_syntax>\d+), +Checksum: +(?P<checksum>\d+),'
                        ' +Lifetime: +(?P<lifetime>\d+), +Output +cngstn: +(?P<output_cngtn>\d+)$')
        #   No Route: 0, Discard Route: 0, Dst Unreachable 0, Encaps. Failed: 0
        p7 = re.compile(r'^No +Route: +(?P<no_route>\d+), +Discard +Route: +(?P<discard_route>\d+),'
                        ' +Dst +Unreachable: +(?P<dst_unreachable>\d+), +Encaps. +Failed: +(?P<encaps_failed>\d+)$')
        #   NLP Unknown: 0, Not an IS: 0
        p8 = re.compile(r'^NLP +Unknown: +(?P<nlp_unknown>\d+), +Not +an +IS: +(?P<not_an_is>\d+)$')
        # CLNS Options: Packets 0, total 0 , bad 0, GQOS 0, cngstn exprncd 0
        p9 = re.compile(r'^CLNS +Options: +Packets +(?P<packet>\d+), +total +(?P<total>\d+),'
                        ' +bad +(?P<bad>\d+), +GQOS +(?P<gqos>\d+) +cngstn +exprncd +(?P<cngstn_exprncd>\d+)$')
        # CLNS Segments:  Segmented: 0, Failed: 0
        p10 = re.compile(r'^CLNS +Segments:  +Segmented: +(?P<segmented>\d+), +Failed: +(?P<failed>\d+)$')
        # CLNS Broadcasts: sent: 0, rcvd: 0
        p11 = re.compile(r'^CLNS +Broadcasts: sent: +(?P<sent>\d+), +rcvd: +(?P<rcvd>\d+)$')
        # Echos: Rcvd 0 requests, 0 replies
        p12 = re.compile(r'^Echos: +Rcvd +(?P<rcvd>\d+) +requests, +(?P<replied>\d+) +replies$')
        #       Sent 0 requests, 0 replies
        p13 = re.compile(r'^Sent +(?P<sent>\d+) +requests, +(?P<replied>\d+) +replies$')
        # ESIS(sent/rcvd): ESHs: 0/0, ISHs: 168/0, RDs: 0/0, QCF: 0/0
        p14 = re.compile(r'^ESIS\(sent\/rcvd\): +ESHs: +(?P<esh_sent>\d+)/(?P<esh_rcvd>\d+),'
                         ' +(?P<ish_sent>\d+)/(?P<ish_rcvd>\d+),'
                         ' +(?P<rd_sent>\d+)/(?P<rd_rcvd>\d+), +(?P<qcf_sent>\d+)/(?P<qcf_rcvd>\d+)$')
        # Tunneling (sent/rcvd): IP: 0/0, IPv6: 0/0
        p15 = re.compile(r'^Tunneling +\(sent\/rcvd\): +IP: +(?P<ip_sent>\d+)/(?P<ip_rcvd>\d+),'
                         ' +(?P<ish_sent>\d+)/(?P<ish_rcvd>\d+),'
                         ' +(?P<rd_sent>\d+)/(?P<rd_rcvd>\d+), +(?P<qcf_sent>\d+)/(?P<qcf_rcvd>\d+)$')
        # Tunneling dropped (rcvd) IP/IPV6:  0
        p16 = re.compile(r'^Tunneling +dropped +\(rcvd\) +IP\/IPV6:  +(?P<tunneling_dropped>\d+)$')
        # ISO-IGRP: Querys (sent/rcvd): 0/0 Updates (sent/rcvd): 0/0
        p17 = re.compile(r'^ISO-IGRP: +Querys +\(sent\/rcvd\): (?P<query_sent>\d+)/(?P<query_rcvd>\d+),'
                         ' +Updates +(?P<update_sent>\d+)/(?P<update_rcvd>\d+)$')
        # ISO-IGRP: Router Hellos: (sent/rcvd): 0/0
        p18 = re.compile(r'^ISO-IGRP: +Router +Hellos: +\(sent\/rcvd\): +(?P<hello_sent>\d+)\/+(?P<hello_rcvd>\d+)$')
        # ISO-IGRP Syntax Errors: 0
        p18 = re.compile(r'^ISO-IGRP: +Router +Hellos: +\(sent\/rcvd\): +(?P<hello_sent>\d+)\/+(?P<hello_rcvd>\d+)$')


        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet1 is up, line protocol is up
            m = p1.match(line)
            if m:
                group = m.groupdict()

                continue

            return result_dict
