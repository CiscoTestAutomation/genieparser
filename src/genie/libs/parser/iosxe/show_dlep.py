''' show_dlep.py

IOSXE parsers for the following show commands:

    * 'show dlep neighbor'
    * 'show dlep neighbors {interface}'
    * 'show dlep clients'
    * 'show dlep clients {interface}'

'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use
from genie.libs.parser.utils.common import Common


# genie.parsergen
try:
    import genie.parsergen
except (ImportError, OSError):
    pass



class ShowDlepNeighborsSchema(MetaParser):
    """Schema for 'show dlep neighbors' or 'show dlep neighbors {interface}' """

    schema = {
        'interface': {
            Any(): {
                'dlep_server': {
                    'ip_address': str,
                    'udp_port': int,
                    'udp_socket': int,
                },
                'sid': {
                    'sid_id': int,
                    'mac_address': str,
                    'addresses': {
                        'ipv4': str,
                        'ipv6_ll': str,
                    },
                    'supported_metrics': {
                        'rlq_rx_metric': int,
                        'rlq_tx_metric': int,
                        'resources_metric': int,
                        'mtu_metric': int,
                        'latency_metric_in_microseconds': int,
                        'cdr_rx_metric_in_bps': int,
                        'cdr_tx_metric_in_bps': int,
                        'mdr_rx_metric_in_bps': int,
                        'mdr_tx_metric_in_bps': int
                    }
                }
            }
        }
    }


class ShowDlepNeighbors(ShowDlepNeighborsSchema):
    """
    Parser for 'show dlep neighbors' or 'show dlep neighbors {interface}'
    """

    cli_command = ['show dlep neighbors','show dlep neighbors {interface}']

    def cli(self, interface='',output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # DLEP Neighbors for Interface GigabitEthernet2
        p1 = re.compile(r'^(?P<nibor_intf>DLEP\s\w+\s\w+\sInterface)\s+(?P<int>\S+)$')

        # DLEP Server IP=9.9.9.31:11131 Sock=0
        p2 = re.compile(r'^(?P<srv>DLEP\s\w+)\sIP=(?P<ip>[\d\.]+):(?P<u_port>\d+)\s\w+=(?P<sock>\d+)$')

        # SID=2151  MAC_Address=000c.299b.a9d2
        p3 = re.compile(r'^(?P<sid>\w+)=(?P<sid_val>\d+)\s+(?P<mac>\w+)=(?P<mac_id>.+)$')

        #  IPv4 : 9.9.9.21  IPv6 LL : FE80::20C:29FF:FE9B:A9D2
        p4 = re.compile(r'^(?P<ip4>\w+\d)\s:\s(?P<ip4_val>[\d\.]+)\s+(?P<ip6>\w+\s\w+)\s:\s(?P<ip6_val>.+)$')


        # RLQ RX Metric : 100
        # RLQ TX Metric : 100
        p5 = re.compile(r'^(?P<par>RLQ\s\w+\s\w+)\s:\s(?P<val>\d+)+$')


        #   CDR RX Metric : 100000000 bps
        p6 = re.compile(r'^(?P<par>CDR\sRX\s\w+)\s:\s(?P<val>\d+)\s+\w+$')

        #   CDR TX Metric : 100000000 bps
        p7 = re.compile(r'^(?P<par>CDR\sTX\s\w+)\s:\s(?P<val>\d+)\s+\w+$')

        #   MDR RX Metric : 100000000 bps
        p8 = re.compile(r'^(?P<par>MDR\sRX\s\w+)\s:\s(?P<val>\d+)\s+\w+$')

        #   MDR TX Metric : 100000000 bps
        p9 = re.compile(r'^(?P<par>MDR\sTX\s\w+)\s:\s(?P<val>\d+)\s+\w+$')

        #   Resources Metric : 100
        #   MTU Metric : 1500
        p10 = re.compile(r'^(?P<par>\w+\s\w+)\s:\s(?P<val>\d+)$')

        #   Latency Metric : 250 microseconds
        p11 = re.compile(r'^(?P<par>\w+\s\w+)\s:\s(?P<val>\d+)\s+\w+$')


        for lines in out.splitlines():
            line = lines.strip()

            # DLEP Neighbors for Interface GigabitEthernet2
            m = p1.match(line)
            if m:
                intf = m.groupdict()['int']
                ret_dict.setdefault('interface', {})
                ret_dict['interface'].setdefault(intf, {})

            # DLEP Server IP=9.9.9.31:11131 Sock=0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                srvr = group['srv'].lower().replace(" ", "_")
                ret_dict['interface'][intf].setdefault(srvr, {})
                ret_dict['interface'][intf][srvr]['ip_address'] = group['ip']
                ret_dict['interface'][intf][srvr]['udp_port'] = int(group['u_port'])
                ret_dict['interface'][intf][srvr]['udp_socket'] = int(group['sock'])

            # SID=2151  MAC_Address=000c.299b.a9d2
            m = p3.match(line)
            if m:
                group = m.groupdict()
                sid = group['sid'].lower()
                ret_dict['interface'][intf].setdefault(sid, {})
                mac = group['mac'].lower()
                ret_dict['interface'][intf][sid]['sid_id'] = int(group['sid_val'])
                ret_dict['interface'][intf][sid][mac] = group['mac_id']

            #  IPv4 : 9.9.9.21  IPv6 LL : FE80::20C:29FF:FE9B:A9D2
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ipv4 = group['ip4'].lower()
                ipv6 = group['ip6'].lower().replace(" ", "_")
                ret_dict['interface'][intf][sid].setdefault('addresses', {})
                ret_dict['interface'][intf][sid]['addresses'][ipv4] = group['ip4_val']
                ret_dict['interface'][intf][sid]['addresses'][ipv6] = group['ip6_val']

            #   RLQ RX Metric : 100
            #   RLQ TX Metric : 100
            m = p5.match(line)
            if m:
                param = m.groupdict()['par'].lower().replace(" ", "_")
                ret_dict['interface'][intf][sid].setdefault('supported_metrics', {})
                ret_dict['interface'][intf][sid]['supported_metrics'][param] = int(m.groupdict()['val'])

            #   CDR RX Metric : 100000000 bps
            m = p6.match(line)
            if m:
                ret_dict['interface'][intf][sid]['supported_metrics']['cdr_rx_metric_in_bps'] = int(m.groupdict()['val'])

            #   CDR TX Metric : 100000000 bps
            m = p7.match(line)
            if m:
                ret_dict['interface'][intf][sid]['supported_metrics']['cdr_tx_metric_in_bps'] = int(m.groupdict()['val'])

            #   MDR RX Metric : 100000000 bps
            m = p8.match(line)
            if m:
                ret_dict['interface'][intf][sid]['supported_metrics']['mdr_rx_metric_in_bps'] = int(m.groupdict()['val'])

            #   MDR TX Metric : 100000000 bps
            m = p9.match(line)
            if m:
                ret_dict['interface'][intf][sid]['supported_metrics']['mdr_tx_metric_in_bps'] = int(m.groupdict()['val'])

            #   Resources Metric : 100
            #   MTU Metric : 1500
            m = p10.match(line)
            if m:
                param = m.groupdict()['par'].lower().replace(" ", "_")
                ret_dict['interface'][intf][sid]['supported_metrics'][param] = int(m.groupdict()['val'])

            #   Latency Metric : 250 microseconds
            m = p11.match(line)
            if m:
                ret_dict['interface'][intf][sid]['supported_metrics']['latency_metric_in_microseconds'] = int(m.groupdict()['val'])

        return ret_dict


class ShowDlepClientsSchema(MetaParser):
    """Schema for 'show dlep clients' or 'show dlep clients {interface}' """

    schema = {
        'interface': {
            Any(): {
                'dlep_server': {
                    'ip_address': str,
                    'udp_port': int,
                    'udp_socket': int,
                },
                'dlep_client': {
                    'ip_address': str,
                    'tcp_port': int,
                    'tcp_socket_fd': int,
                    'peer_id': int,
                    'virtual_template': int,
                    'description': str,
                    'peer_timers_in_milliseconds': {
                        'heartbeat': int,
                        'dead_interval': int,
                        'terminate_ack': int,
                    },
                    'neighbour_timers_in_seconds': {
                        'activity_timeout': int,
                        'neighbor_down_ack': int,
                    },
                    'supported_metrics': {
                        'link_rlq_rx_metric': int,
                        'link_rlq_tx_metric': int,
                        'link_resources_metric': int,
                        'link_mtu_metric': int,
                        'link_latency_metric_in_microseconds': int,
                        'link_cdr_rx_metric_in_bps': int,
                        'link_cdr_tx_metric_in_bps': int,
                        'link_mdr_rx_metric_in_bps': int,
                        'link_mdr_tx_metric_in_bps': int,
                    }
                }
            }
        }
    }


class ShowDlepClients(ShowDlepClientsSchema):
    """
    Parser for 'show dlep clients' or 'show dlep clients {interface}'
    """

    cli_command = ['show dlep clients','show dlep clients {interface}']

    def cli(self, interface='',output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # DLEP Clients for Interface GigabitEthernet2
        p1 = re.compile(r'^(?P<clnt_intf>DLEP\s\w+\s\w+\sInterface)\s+(?P<int>\S+)$')

        # DLEP Server IP=9.9.9.21:11121 Sock=0
        p2 = re.compile(r'^(?P<srv>DLEP\s\w+)\sIP=(?P<ip>[\d\.]+):(?P<u_port>\d+)\s\w+=(?P<sock>\d+)$')

        # DLEP Client IP=9.9.9.22:860 TCP Socket fd=1
        p3 = re.compile(
            r'^(?P<clnt>DLEP\s\w+)\sIP=(?P<ip>[\d\.]+):(?P<t_port>\d+)\s(?P<t_sock>\w+\s\w+\s\w+)=(?P<num>\d+)$')

        #  Peer ID=4, Virtual template=2
        p4 = re.compile(r'^(?P<par>\w+\s\w+)=(?P<val_1>\d+),\s+(?P<v_intf>\w+\s\w+[\s\w+])=(?P<val_2>\d+)$')

        #  Description: DLEP_Radio_RT3
        p5 = re.compile(r'^(?P<des>[Dd]esc\w+):\s+(?P<stng>\S+)$')

        #  Peer Timers (all values in milliseconds):
        p6 = re.compile(r'^[Pp]eer Ti\w+.+$')

        #   Heartbeat=5000, Dead Interval=10000, Terminate ACK=20000
        p7 = re.compile(r'^(?P<hb>\w+)=(?P<hb_val>\d+)\S+\s+(?P<d_int>\w+\s\w+)=(?P<d_val>\d+)\S+\s+(?P<t_ack>\w+\s\w+)\S(?P<t_val>\d+)$')

        #  Neighbor Timers (all values in seconds):
        p8 = re.compile(r'^[Nn]eigh\w+\s[Tt]im\w+.+$')

        #   Activity timeout=0, Neighbor Down ACK=10
        p9 = re.compile(r'^(?P<par>\w+\s\w+)=(?P<val_1>\d+),\s+(?P<nibor>\w+\s\w+\s\w+)=(?P<val_2>\d+)$')

        #  Supported Metrics:
        p10 = re.compile(r'^[Ss]upp\w+\s[Mm]etr\w+:$')

        #   Link Resources Metric : 100
        #   Link MTU Metric : 100
        p11 = re.compile(r'^(?P<par>[Ll]ink\s\w+\s\w+)\s:\s(?P<val>\d+)$')

        #   Link Latency Metric : 250 microseconds
        p12 = re.compile(r'^(?P<par>[Ll]ink\s\w+\s\w+)\s:\s(?P<val>\d+)\s+\w+$')

        #   Link RLQ RX Metric : 100
        #   Link RLQ TX Metric : 100
        p13 = re.compile(r'^(?P<par>[Ll]ink\sRLQ\s\w+\s\w+)\s:\s(?P<val>\d+)$')

        #   Link CDR RX Metric : 100000000 bps
        p14 = re.compile(r'^(?P<par>[Ll]ink\sCDR\sRX\s\w+)\s:\s(?P<val>\d+)\s+\w+$')

        #   Link CDR TX Metric : 100000000 bps
        p15 = re.compile(r'^(?P<par>[Ll]ink\sCDR\sTX\s\w+)\s:\s(?P<val>\d+)\s+\w+$')

        #   Link MDR RX Metric : 100000000 bps
        p16 = re.compile(r'^(?P<par>[Ll]ink\sMDR\sRX\s\w+)\s:\s(?P<val>\d+)\s+\w+$')

        #   Link MDR TX Metric : 100000000 bps
        p17 = re.compile(r'^(?P<par>[Ll]ink\sMDR\sTX\s\w+)\s:\s(?P<val>\d+)\s+\w+$')


        for lines in out.splitlines():
            line = lines.strip()

            # DLEP Clients for Interface GigabitEthernet2
            m = p1.match(line)
            if m:
                intf = m.groupdict()['int']
                ret_dict.setdefault('interface', {})
                ret_dict['interface'].setdefault(intf, {})

            # DLEP Server IP=9.9.9.21:11121 Sock=0
            m = p2.match(line)
            if m:
                srvr = m.groupdict()['srv'].lower().replace(" ", "_")
                ret_dict['interface'][intf].setdefault(srvr, {})
                ret_dict['interface'][intf][srvr]['ip_address'] = m.groupdict()['ip']
                ret_dict['interface'][intf][srvr]['udp_port'] = int(m.groupdict()['u_port'])
                ret_dict['interface'][intf][srvr]['udp_socket'] = int(m.groupdict()['sock'])

            # DLEP Client IP=9.9.9.22:860 TCP Socket fd=1
            m = p3.match(line)
            if m:
                clint = m.groupdict()['clnt'].lower().replace(" ", "_")
                tcp_sock = m.groupdict()['t_sock'].lower().replace(" ", "_")
                ret_dict['interface'][intf].setdefault(clint, {})
                ret_dict['interface'][intf][clint]['ip_address'] = m.groupdict()['ip']
                ret_dict['interface'][intf][clint]['tcp_port'] = int(m.groupdict()['t_port'])
                ret_dict['interface'][intf][clint][tcp_sock] = int(m.groupdict()['num'])

            #  Peer ID=4, Virtual template=2
            m = p4.match(line)
            if m:
                par_1 = m.groupdict()['par'].lower().replace(" ", "_")
                val_1 = m.groupdict()['val_1']
                par_2 = m.groupdict()['v_intf'].lower().replace(" ", "_")
                val_2 = m.groupdict()['val_2']
                ret_dict['interface'][intf][clint][par_1] = int(m.groupdict()['val_1'])
                ret_dict['interface'][intf][clint][par_2] = int(m.groupdict()['val_2'])

            #  Description: DLEP_Radio_RT3
            m = p5.match(line)
            if m:
                descr = m.groupdict()['des'].lower().replace(" ", "_")
                ret_dict['interface'][intf][clint][descr] = m.groupdict()['stng']

            #  Peer Timers (all values in milliseconds):
            m = p6.match(line)
            if m:
                ret_dict['interface'][intf][clint].setdefault('peer_timers_in_milliseconds', {})

            #   Heartbeat=5000, Dead Interval=10000, Terminate ACK=20000
            m = p7.match(line)
            if m:
                h_beat = m.groupdict()['hb'].lower().replace(" ", "_")
                d_inter = m.groupdict()['d_int'].lower().replace(" ", "_")
                term_ack = m.groupdict()['t_ack'].lower().replace(" ", "_")
                ret_dict['interface'][intf][clint]['peer_timers_in_milliseconds'][h_beat] = int(m.groupdict()['hb_val'])
                ret_dict['interface'][intf][clint]['peer_timers_in_milliseconds'][d_inter] = int(m.groupdict()['d_val'])
                ret_dict['interface'][intf][clint]['peer_timers_in_milliseconds'][term_ack] = int(m.groupdict()['t_val'])

            #  Neighbor Timers (all values in seconds):
            m = p8.match(line)
            if m:
                ret_dict['interface'][intf][clint].setdefault('neighbour_timers_in_seconds', {})

            #   Activity timeout=0, Neighbor Down ACK=10
            m = p9.match(line)
            if m:
                par_1 = m.groupdict()['par'].lower().replace(" ", "_")
                par_2 = m.groupdict()['nibor'].lower().replace(" ", "_")
                ret_dict['interface'][intf][clint]['neighbour_timers_in_seconds'][par_1] = int(m.groupdict()['val_1'])
                ret_dict['interface'][intf][clint]['neighbour_timers_in_seconds'][par_2] = int(m.groupdict()['val_2'])

            #  Supported Metrics:
            m = p10.match(line)
            if m:
                ret_dict['interface'][intf][clint].setdefault('supported_metrics', {})

            #   Link Resources Metric : 100
            #   Link MTU Metric : 100
            m = p11.match(line)
            if m:
                param = m.groupdict()['par'].lower().replace(" ", "_")
                ret_dict['interface'][intf][clint]['supported_metrics'][param] = int(m.groupdict()['val'])

            #   Link Latency Metric : 250 microseconds
            m = p12.match(line)
            if m:
                ret_dict['interface'][intf][clint]['supported_metrics']['link_latency_metric_in_microseconds'] = int(m.groupdict()['val'])

            #   Link RLQ RX Metric : 100
            #   Link RLQ TX Metric : 100
            m = p13.match(line)
            if m:
                param = m.groupdict()['par'].lower().replace(" ", "_")
                ret_dict['interface'][intf][clint]['supported_metrics'][param] = int(m.groupdict()['val'])

            #   Link CDR RX Metric : 100000000 bps
            m = p14.match(line)
            if m:
                ret_dict['interface'][intf][clint]['supported_metrics']['link_cdr_rx_metric_in_bps'] = int(m.groupdict()['val'])

            #   Link CDR TX Metric : 100000000 bps
            m = p15.match(line)
            if m:
                ret_dict['interface'][intf][clint]['supported_metrics']['link_cdr_tx_metric_in_bps'] = int(m.groupdict()['val'])

            #   Link MDR RX Metric : 100000000 bps
            m = p16.match(line)
            if m:
                ret_dict['interface'][intf][clint]['supported_metrics']['link_mdr_rx_metric_in_bps'] = int(m.groupdict()['val'])

            #   Link MDR TX Metric : 100000000 bps
            m = p17.match(line)
            if m:
                ret_dict['interface'][intf][clint]['supported_metrics']['link_mdr_tx_metric_in_bps'] = int(m.groupdict()['val'])
        
        return ret_dict
