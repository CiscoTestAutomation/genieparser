''' show_dlep.py

IOSXE parsers for the following show commands:

    * 'show dlep neighbor'
    * 'show dlep neighbors {interface}'
    * 'show dlep clients'
    * 'show dlep clients {interface}'
    * 'show dlep counters'
    * 'show dlep config {interface}'

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
                Optional('dlep_server'): {
                    'ip_address': str,
                    'udp_port': int,
                    'udp_socket': int,
                },
                Optional('dlep_local'): {
                    'ip_address': str,
                    'udp_port': int,
                    'udp_socket': int
                },
                Optional('sid'): {
                    Any(): {
                        'mac_address': str,
                        'addresses': {
                            'ipv4': str,
                            'ipv6_ll': str,
                            Optional('associated_interface'): str
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
        p1 = re.compile(r'^DLEP\s+Neighbors\s+for\s+Interface\s+(?P<interface>[\w\d/\.-]+)$')

        # DLEP Server IP=9.9.9.31:11131 Sock=0
        p2 = re.compile(r'^DLEP\s+Server\s+IP=(?P<dlep_server_ip>[\d\.]+):(?P<u_port>\d+)\s+Sock=(?P<sock>\d+)$')

        # DLEP Local IP=9.9.9.11:11111 Sock=0
        p3 = re.compile(r'^DLEP\s+Local\s+IP=(?P<dlep_local_ip>[\d\.]+):(?P<u_port>\d+)\s+Sock=(?P<sock>\d+)$')

        # SID=2151  MAC_Address=000c.299b.a9d2
        p4 = re.compile(r'^SID=(?P<sid>\d+)\s+(Remote\s+End-point\s+)?MAC_Address=(?P<mac_address>[\w\d\.]+)$')

        # IPv4 : 9.9.9.21  IPv6 LL : FE80::20C:29FF:FE9B:A9D2
        # DLEP Remote IP : 9.9.9.1 DLEP Remote IPv6 LL : FE80::20C:29FF:FED4:B578
        p5 = re.compile(r'^(DLEP\s+Remote\s+)?IP(v4)?\s+:\s+(?P<ipv4_address>[\d\.]+)\s+(DLEP\s+Remote\s+)?IPv6\s+LL\s+:\s+(?P<link_local_address>[\w:]+)$')

        # Associated virtual access interface : Virtual-Access2
        p6 = re.compile(r'^Associated\s+virtual\s+access\s+interface\s+:\s+(?P<interface>[\w\d/\.-]+)$')

        # RLQ RX Metric : 100
        p7 = re.compile(r'^RLQ\s+RX\s+Metric\s+:\s+(?P<rlq_rx_metric>\d+)$')

        # RLQ TX Metric : 100
        p8 = re.compile(r'^RLQ\s+TX\s+Metric\s+:\s+(?P<rlq_tx_metric>\d+)$')

        #   CDR RX Metric : 100000000 bps
        p9 = re.compile(r'^CDR\s+RX\s+Metric\s+:\s+(?P<cdr_rx_metric>\d+)\s+bps$')

        #   CDR TX Metric : 100000000 bps
        p10 = re.compile(r'^CDR\s+TX\s+Metric\s+:\s+(?P<cdr_tx_metric>\d+)\s+bps$')

        #   MDR RX Metric : 100000000 bps
        p11 = re.compile(r'^MDR\s+RX\s+Metric\s+:\s+(?P<mdr_rx_metric>\d+)\s+bps$')

        #   MDR TX Metric : 100000000 bps
        p12 = re.compile(r'^MDR\s+TX\s+Metric\s+:\s+(?P<mdr_tx_metric>\d+)\s+bps$')

        #   Resources Metric : 100
        p13 = re.compile(r'^Resources\s+Metric\s+:\s+(?P<resources_metric>\d+)$')

        #   MTU Metric : 1500
        p14 = re.compile(r'^MTU\s+Metric\s+:\s+(?P<mtu_metric>\d+)$')

        #   Latency Metric : 250 microseconds
        p15 = re.compile(r'^Latency\s+Metric\s+:\s+(?P<latency>\d+)\s+microseconds$')


        for lines in out.splitlines():
            line = lines.strip()

            # DLEP Neighbors for Interface GigabitEthernet2
            m = p1.match(line)
            if m:
                intf = m.groupdict()['interface']
                ret_dict.setdefault('interface', {})
                interface_dict = ret_dict['interface'].setdefault(intf, {})

            # DLEP Server IP=9.9.9.31:11131 Sock=0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface_dict.setdefault('dlep_server', {})
                interface_dict['dlep_server']['ip_address'] = group['dlep_server_ip']
                interface_dict['dlep_server']['udp_port'] = int(group['u_port'])
                interface_dict['dlep_server']['udp_socket'] = int(group['sock'])

            # DLEP Local IP=9.9.9.11:11111 Sock=0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                interface_dict.setdefault('dlep_local', {})
                interface_dict['dlep_local']['ip_address'] = group['dlep_local_ip']
                interface_dict['dlep_local']['udp_port'] = int(group['u_port'])
                interface_dict['dlep_local']['udp_socket'] = int(group['sock'])

            # SID=2151  MAC_Address=000c.299b.a9d2
            m = p4.match(line)
            if m:
                group = m.groupdict()
                session_dict = interface_dict.setdefault('sid', {})
                session_dict = session_dict.setdefault(int(group['sid']), {})
                session_dict['mac_address'] = group['mac_address']

            # IPv4 : 9.9.9.21  IPv6 LL : FE80::20C:29FF:FE9B:A9D2
            # DLEP Remote IP : 9.9.9.1 DLEP Remote IPv6 LL : FE80::20C:29FF:FED4:B578
            m = p5.match(line)
            if m:
                group = m.groupdict()
                session_dict.setdefault('addresses', {})
                session_dict['addresses']['ipv4'] = group['ipv4_address']
                session_dict['addresses']['ipv6_ll'] = group['link_local_address']

            # Associated virtual access interface : Virtual-Access2
            m = p6.match(line)
            if m:
                group = m.groupdict()
                session_dict.setdefault('addresses', {})
                session_dict['addresses']['associated_interface'] = \
                    group['interface']

            #   RLQ RX Metric : 100
            m = p7.match(line)
            if m:
                supported_metrics_dict = \
                    session_dict.setdefault('supported_metrics', {})
                supported_metrics_dict['rlq_rx_metric'] = \
                    int(m.groupdict()['rlq_rx_metric'])

            #   RLQ TX Metric : 100
            m = p8.match(line)
            if m:
                supported_metrics_dict = \
                    session_dict.setdefault('supported_metrics', {})
                supported_metrics_dict['rlq_tx_metric'] = \
                    int(m.groupdict()['rlq_tx_metric'])

            #   CDR RX Metric : 100000000 bps
            m = p9.match(line)
            if m:
                supported_metrics_dict = \
                    session_dict.setdefault('supported_metrics', {})
                supported_metrics_dict['cdr_rx_metric_in_bps'] = \
                    int(m.groupdict()['cdr_rx_metric'])

            #   CDR TX Metric : 100000000 bps
            m = p10.match(line)
            if m:
                supported_metrics_dict = \
                    session_dict.setdefault('supported_metrics', {})
                supported_metrics_dict['cdr_tx_metric_in_bps'] = \
                    int(m.groupdict()['cdr_tx_metric'])

            #   MDR RX Metric : 100000000 bps
            m = p11.match(line)
            if m:
                supported_metrics_dict = \
                    session_dict.setdefault('supported_metrics', {})
                supported_metrics_dict['mdr_rx_metric_in_bps'] = \
                    int(m.groupdict()['mdr_rx_metric'])

            #   MDR TX Metric : 100000000 bps
            m = p12.match(line)
            if m:
                supported_metrics_dict = \
                    session_dict.setdefault('supported_metrics', {})
                supported_metrics_dict['mdr_tx_metric_in_bps'] = \
                    int(m.groupdict()['mdr_tx_metric'])

            #   Resources Metric : 100
            m = p13.match(line)
            if m:
                supported_metrics_dict = \
                    session_dict.setdefault('supported_metrics', {})
                supported_metrics_dict['resources_metric'] = \
                    int(m.groupdict()['resources_metric'])

            #   MTU Metric : 1500
            m = p14.match(line)
            if m:
                supported_metrics_dict = \
                    session_dict.setdefault('supported_metrics', {})
                supported_metrics_dict['mtu_metric'] = \
                    int(m.groupdict()['mtu_metric'])

            #   Latency Metric : 250 microseconds
            m = p15.match(line)
            if m:
                supported_metrics_dict = \
                    session_dict.setdefault('supported_metrics', {})
                supported_metrics_dict['latency_metric_in_microseconds'] = \
                    int(m.groupdict()['latency'])

        return ret_dict


class ShowDlepClientsSchema(MetaParser):
    """Schema for 'show dlep clients' or 'show dlep clients {interface}' """

    schema = {
        'interface': {
            Any(): {
                Optional('dlep_server'): {
                    'ip_address': str,
                    'udp_port': int,
                    'udp_socket': int,
                },
                Optional('dlep_local_radio'): {
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
                },
                Optional('dlep_client'): {
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
        p1 = re.compile(r'^DLEP\s+Clients\s+for\s+Interface\s+(?P<interface>[\w\d/\.-]+)$')

        # DLEP Server IP=9.9.9.21:11121 Sock=0
        p2 = re.compile(r'^DLEP\s+(Local|Server)\s+IP=(?P<ip>[\d\.]+):(?P<u_port>\d+)\s+Sock=(?P<sock>\d+)$')

        # DLEP Local Radio IP=9.9.9.12:859 TCP Socket fd=1
        p3_1 = re.compile(
            r'^DLEP\s+Local\s+Radio\s+IP=(?P<ip>[\d\.]+):(?P<t_port>\d+)\s+TCP\s+Socket\s+fd=(?P<fd>\d+)$')

        # DLEP Client IP=9.9.9.22:860 TCP Socket fd=1
        p3_2 = re.compile(
            r'^DLEP\s+Client\s+IP=(?P<ip>[\d\.]+):(?P<t_port>\d+)\s+TCP\s+Socket\s+fd=(?P<fd>\d+)$')

        #  Peer ID=4, Virtual template=2
        p4 = re.compile(r'^Peer\s+ID=(?P<peer_id>\d+),\s+Virtual\s+template=(?P<virtual_template>\d+)$')

        #  Description: DLEP_Radio_RT3
        p5 = re.compile(r'^Description:\s+(?P<description>\S+)$')

        #   Heartbeat=5000, Dead Interval=10000, Terminate ACK=20000
        p7 = re.compile(r'^Heartbeat=(?P<heartbeat>\d+),\s+Dead\s+Interval=(?P<dead_interval>\d+),\s+Terminate\s+ACK=(?P<terminate_ack>\d+)$')

        #   Activity timeout=0, Neighbor Down ACK=10
        p9 = re.compile(r'^Activity\s+timeout=(?P<activity_timeout>\d+),\s+Neighbor\s+Down\s+ACK=(?P<neighbor_down_ack>\d+)$')

        #   Link Resources Metric : 100
        p11 = re.compile(r'^Link\s+Resources\s+Metric\s+:\s+(?P<resources>\d+)$')

        #   Link MTU Metric : 100
        p11_1 = re.compile(r'^Link\s+MTU\s+Metric\s+:\s+(?P<mtu>\d+)$')

        #   Link Latency Metric : 250 microseconds
        p12 = re.compile(r'^Link\s+Latency\s+Metric\s+:\s+(?P<latency>\d+)\s+microseconds$')

        #   Link RLQ RX Metric : 100
        p13 = re.compile(r'^Link\s+RLQ\s+RX\s+Metric\s+:\s+(?P<rlq_rx>\d+)$')

        #   Link RLQ TX Metric : 100
        p13_1 = re.compile(r'^Link\s+RLQ\s+TX\s+Metric\s+:\s+(?P<rlq_tx>\d+)$')

        #   Link CDR RX Metric : 100000000 bps
        p14 = re.compile(r'^Link\s+CDR\s+RX\s+Metric\s+:\s+(?P<cdr_rx>\d+)\s+bps$')

        #   Link CDR TX Metric : 100000000 bps
        p15 = re.compile(r'^Link\s+CDR\s+TX\s+Metric\s+:\s+(?P<cdr_tx>\d+)\s+bps$')

        #   Link MDR RX Metric : 100000000 bps
        p16 = re.compile(r'^Link\s+MDR\s+RX\s+Metric\s+:\s+(?P<mdr_rx>\d+)\s+bps$')

        #   Link MDR TX Metric : 100000000 bps
        p17 = re.compile(r'^Link\s+MDR\s+TX\s+Metric\s+:\s+(?P<mdr_tx>\d+)\s+bps$')


        for lines in out.splitlines():
            line = lines.strip()

            # DLEP Clients for Interface GigabitEthernet2
            m = p1.match(line)
            if m:
                intf = m.groupdict()['interface']
                ret_dict.setdefault('interface', {})
                interface_dict = ret_dict['interface'].setdefault(intf, {})

            # DLEP Server IP=9.9.9.21:11121 Sock=0
            m = p2.match(line)
            if m:
                interface_dict.setdefault('dlep_server', {})
                interface_dict['dlep_server']['ip_address'] = \
                    m.groupdict()['ip']
                interface_dict['dlep_server']['udp_port'] = \
                    int(m.groupdict()['u_port'])
                interface_dict['dlep_server']['udp_socket'] = \
                    int(m.groupdict()['sock'])

            # DLEP Local Radio IP=9.9.9.12:859 TCP Socket fd=1
            m = p3_1.match(line)
            if m:
                client_dict = interface_dict.setdefault('dlep_local_radio', {})
                client_dict['ip_address'] = m.groupdict()['ip']
                client_dict['tcp_port'] = int(m.groupdict()['t_port'])
                client_dict['tcp_socket_fd'] = int(m.groupdict()['fd'])

            # DLEP Client IP=9.9.9.22:860 TCP Socket fd=1
            m = p3_2.match(line)
            if m:
                client_dict = interface_dict.setdefault('dlep_client', {})
                client_dict['ip_address'] = m.groupdict()['ip']
                client_dict['tcp_port'] = int(m.groupdict()['t_port'])
                client_dict['tcp_socket_fd'] = int(m.groupdict()['fd'])

            #  Peer ID=4, Virtual template=2
            m = p4.match(line)
            if m:
                client_dict['peer_id'] = int(m.groupdict()['peer_id'])
                client_dict['virtual_template'] = \
                    int(m.groupdict()['virtual_template'])

            #  Description: DLEP_Radio_RT3
            m = p5.match(line)
            if m:
                client_dict['description'] = m.groupdict()['description']

            #   Heartbeat=5000, Dead Interval=10000, Terminate ACK=20000
            m = p7.match(line)
            if m:
                client_dict.setdefault('peer_timers_in_milliseconds', {})
                client_dict['peer_timers_in_milliseconds']['heartbeat'] = \
                    int(m.groupdict()['heartbeat'])
                client_dict['peer_timers_in_milliseconds']['dead_interval'] = \
                    int(m.groupdict()['dead_interval'])
                client_dict['peer_timers_in_milliseconds']['terminate_ack'] = \
                    int(m.groupdict()['terminate_ack'])

            #   Activity timeout=0, Neighbor Down ACK=10
            m = p9.match(line)
            if m:
                client_dict.setdefault('neighbour_timers_in_seconds', {})
                client_dict['neighbour_timers_in_seconds']['activity_timeout'] = \
                    int(m.groupdict()['activity_timeout'])
                client_dict['neighbour_timers_in_seconds']['neighbor_down_ack'] = \
                    int(m.groupdict()['neighbor_down_ack'])

            #   Link Resources Metric : 100
            m = p11.match(line)
            if m:
                supported_metrics_dict = \
                    client_dict.setdefault('supported_metrics', {})
                supported_metrics_dict['link_resources_metric'] = \
                    int(m.groupdict()['resources'])

            #   Link MTU Metric : 100
            m = p11_1.match(line)
            if m:
                supported_metrics_dict = \
                    client_dict.setdefault('supported_metrics', {})
                supported_metrics_dict['link_mtu_metric'] = \
                    int(m.groupdict()['mtu'])

            #   Link Latency Metric : 250 microseconds
            m = p12.match(line)
            if m:
                supported_metrics_dict = \
                    client_dict.setdefault('supported_metrics', {})
                supported_metrics_dict['link_latency_metric_in_microseconds'] = \
                    int(m.groupdict()['latency'])

            #   Link RLQ RX Metric : 100
            m = p13.match(line)
            if m:
                supported_metrics_dict = \
                    client_dict.setdefault('supported_metrics', {})
                supported_metrics_dict['link_rlq_rx_metric'] = \
                    int(m.groupdict()['rlq_rx'])

            #   Link RLQ TX Metric : 100
            m = p13_1.match(line)
            if m:
                supported_metrics_dict = \
                    client_dict.setdefault('supported_metrics', {})
                supported_metrics_dict['link_rlq_tx_metric'] = \
                    int(m.groupdict()['rlq_tx'])

            #   Link CDR RX Metric : 100000000 bps
            m = p14.match(line)
            if m:
                supported_metrics_dict = \
                    client_dict.setdefault('supported_metrics', {})
                supported_metrics_dict['link_cdr_rx_metric_in_bps'] = \
                    int(m.groupdict()['cdr_rx'])

            #   Link CDR TX Metric : 100000000 bps
            m = p15.match(line)
            if m:
                supported_metrics_dict = \
                    client_dict.setdefault('supported_metrics', {})
                supported_metrics_dict['link_cdr_tx_metric_in_bps'] = \
                    int(m.groupdict()['cdr_tx'])

            #   Link MDR RX Metric : 100000000 bps
            m = p16.match(line)
            if m:
                supported_metrics_dict = \
                    client_dict.setdefault('supported_metrics', {})
                supported_metrics_dict['link_mdr_rx_metric_in_bps'] = \
                    int(m.groupdict()['mdr_rx'])

            #   Link MDR TX Metric : 100000000 bps
            m = p17.match(line)
            if m:
                supported_metrics_dict = \
                    client_dict.setdefault('supported_metrics', {})
                supported_metrics_dict['link_mdr_tx_metric_in_bps'] = \
                    int(m.groupdict()['mdr_tx'])

        return ret_dict


class ShowDlepCountersSchema(MetaParser):
    """ Schema for 'show dlep counters' """
    
    schema = {
        Any(): {
            'dlep_version': str, 
            'dlep_local_ip': str, 
            'dlepv5_tcp_port': str, 
            'peer_counters': {

                'rx_peer_discovery': int, 
                'tx_peer_offer': int,
                'rx_peer_offer': int, 
                'tx_peer_discovery': int, 
                'rx_peer_init': int, 
                'tx_peer_init_ack': int, 
                'rx_peer_init_ack': int, 
                'tx_peer_init': int, 
                'rx_heartbeat': int, 
                'tx_heartbeat': int, 
                'rx_peer_terminate': int, 
                'tx_peer_terminate_ack': int, 
                'rx_peer_terminate_ack': int, 
                'tx_peer_terminate': int
            }, 
            'neighbor_counters': {

                'rx_neighbor_up': int, 
                'tx_neighbor_up_ack': int, 
                'rx_metric': int, 
                'rx_neighbor_down': int, 
                'tx_neighbor_down_ack': int, 
                'rx_neighbor_down_ack': int, 
                'tx_neighbor_down': int
            }, 
            'exception_counters': {

                'rx_invalid_message': int, 
                'rx_unknown_message': int, 
                'pre-existing_neighbor': int, 
                'neighbor_resource_error': int, 
                'neighbor_not_found': int, 
                'neighbor_msg_peer_not_up': int
            }, 
            'timer_counters': {

                'peer_heartbeat_timer': int, 
                'peer_terminate_ack_timer': int, 
                'neighbor_terminate_ack_timer': int, 
                'neighbor_activity_timer': int, 
                'radio_connect_timer': int
            }
        }, 
            'single_timer_wheel_manet_infra_wheel': {

                'granularity_msec': int, 
                'wheel_size': int, 
                'spoke_index': int, 
                'tick_count': int, 
                'flags': str, 
                'active_timers': int, 
                'high_water_mark': int, 
                'started_timers': int, 
                'restarted_timers': int, 
                'cancelled_timers': int, 
                'expired_timers': int, 
                'long_timers': int, 
                'long_timer_revs': int, 
                'timer_suspends': int
            }
    }


class ShowDlepCounters(ShowDlepCountersSchema):
    """
    Parser for 'show dlep counters' 
    """

    cli_command = "show dlep counters"

    
    def cli(self,output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        # DLEP Counters for Interface 
        
        # DLEP Counters for TenGigabitEthernet0/0/0
        p1 = re.compile(r'^(?P<counter_title1>\w+\s+\w+\s+\w+\s+)(?P<val1>\w+\/\d\/\d(\.\d+)?)$')
        # DLEP Version = RFC 8175 
        p2 = re.compile(r'^(?P<counter_title2>DLEP.*)=(?P<val2>.*)$')
        # Peer Counters:  
        p3 = re.compile(r'^(?P<counter_title3>\w+\s\w+):$')
        # RX Peer Discovery     0      TX Peer Offer             0 
        p4 = re.compile(r'^(?P<counter_title4>\w+\W?\w+\s+(\w+\s+){1,5})(?P<val3>\d+)\s+(?P<counter_title5>\w+\s+(\w+\s+){1,5})?(?P<val4>\d+)?$')
        # Peer Heartbeat Timer         369
        p5 = re.compile(r'^(?P<counter_title6>\w+\s+(\w+\s+){1,4})(?P<val5>\d+)$')
        # Single Timer Wheel "Manet Infra Wheel"
        p6 = re.compile(r'^(?P<counter_title7>\w+\s+(\w+\s+){1,4}"(\w+\s?){1,4})"$')
        # Wheel size       = 4096
        p7 = re.compile(r'^(?P<counter_title8>(\w+\s+){1,4})=(?P<val6>\s+\d+\s?(\w+){0,1})$')
          
        for lines in output.splitlines():
            line = lines.strip()
            # DLEP Counters for TenGigabitEthernet0/0/0
            m = p1.match(line)
            if m:
                title1 = m.groupdict()['counter_title1'].strip().lower().replace(" ", "_")
                par1 = m.groupdict()['val1'].strip()
                interf = title1 + "_" + par1
                ret_dict.setdefault(interf, {})
                continue
                  
            # DLEP Version = RFC 8175
            m = p2.match(line)
            if m:
                title2 = m.groupdict()['counter_title2'].strip().lower().replace(" ", "_")
                par2 = m.groupdict()['val2'].strip()
                ret_dict[interf][title2] = par2
                continue
           
            # Peer Counters:       
            m = p3.match(line)
            if m:
                title3 = m.groupdict()['counter_title3'].strip().lower().replace(" ", "_")
                ret_dict[interf].setdefault(title3, {})
                continue
            
            # RX Peer Discovery     0      TX Peer Offer             0      
            m = p4.match(line)
            if m:
                title4 = m.groupdict()['counter_title4'].strip().lower().replace(" ", "_")
                par4 = m.groupdict()['val3'].strip()
                ret_dict[interf][title3][title4] = int(par4)
                title5 = m.groupdict()['counter_title5'].strip().lower().replace(" ", "_")
                par5 = m.groupdict()['val4'].strip()
                ret_dict[interf][title3][title5] = int(par5)
                continue
            
            # Peer Heartbeat Timer         369      	  
            m = p5.match(line)
            if m:
                title6 = m.groupdict()['counter_title6'].strip().lower().replace(" ", "_")
                par6 = m.groupdict()['val5'].strip()
                ret_dict[interf][title3][title6] = int(par6)
                continue
            
            # Parses (Single Timer Wheel "Manet Infra Wheel") as header   
            m = p6.match(line)
            if m:
                title7 = m.groupdict()['counter_title7'].strip().lower().replace(" ", "_").replace("\"", "")
                ret_dict.setdefault(title7, {})
                continue
            
            # Wheel size       = 4096      
            m = p7.match(line)
            if m:
                title8 = m.groupdict()['counter_title8'].strip().lower().replace(" ", "_")
                par8 = m.groupdict()['val6'].strip()
                if "granularity" == title8:
                    title8 = title8 + "_msec"
                    par8 = par8.split(' ')[0]
                if par8.isnumeric():
                    par8 = int(par8)
                ret_dict[title7][title8] = par8
                continue

        return ret_dict
                  

class ShowDlepConfigInterfaceSchema(MetaParser):
    """Schema for 'show dlep config {interface}'"""

    schema = {
        'version': str,
        'local_ip': str,
        'tcp_port': int,
        'virtual_template': int,
        'timers': {
            'missed_heartbeat_threshold': int,
            'peer_terminate_ack_timeout': int,
            'heartbeat_interval': int,
            'discovery_interval': int,
            'session_ack_timeout': int,
            'neighbor_activity_timeout': int,
            'neighbor_down_ack_timeout': int
        }
    }


class ShowDlepConfigInterface(ShowDlepConfigInterfaceSchema):
    """
    Parser for 'show dlep config {interface}'
    """

    cli_command = 'show dlep config {interface}'

    def cli(self, interface=None, output=None):
        if output is None:
            cmd = self.cli_command.format(interface=interface)
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        # DLEP Version = RFC 8175
        p1 = re.compile(r'^DLEP Version = (?P<version>.*)$')

        # DLEP Local IP=9.9.9.151:55113
        p2 = re.compile(r'^DLEP Local IP=(?P<local_ip>.*)$')

        # DLEPv27 TCP Port = 55114
        p3 = re.compile(r'^DLEPv27 TCP Port = (?P<tcp_port>.*)$')

        # Virtual template=1
        p4 = re.compile(r'^Virtual template=(?P<virtual_template>.*)$')

        # Missed heartbeat threshold=2, Peer Terminate ACK timeout=10
        p5 = re.compile(r'^Missed heartbeat threshold=(?P<missed_heartbeat_threshold>[0-9]+), Peer Terminate ACK timeout=(?P<peer_terminate_ack_timeout>[0-9]+)$')

        # Heartbeat interval=5, Discovery interval =5, Session Ack timeout=10
        p6 = re.compile(r'^Heartbeat interval=(?P<heartbeat_interval>[0-9]+), Discovery interval =(?P<discovery_interval>[0-9]+), Session Ack timeout=(?P<session_ack_timeout>[0-9]+)$')

        # Neighbor activity timeout=0, Neighbor Down ACK timeout=10
        p7 = re.compile(r'^Neighbor activity timeout=(?P<neighbor_activity_timeout>[0-9]+), Neighbor Down ACK timeout=(?P<neighbor_down_ack_timeout>[0-9]+)$')

        for line_raw in out.splitlines():
            line = line_raw.strip()

            # DLEP Version = RFC 8175
            m = p1.match(line)
            if m:
                ret_dict['version'] = m.groupdict()['version']
                continue

            # DLEP Local IP=9.9.9.151:55113
            m = p2.match(line)
            if m:
                ret_dict['local_ip'] = m.groupdict()['local_ip']
                continue

            # DLEPv27 TCP Port = 55114
            m = p3.match(line)
            if m:
                ret_dict['tcp_port'] = int(m.groupdict()['tcp_port'])
                continue

            # Virtual template=1
            m = p4.match(line)
            if m:
                ret_dict['virtual_template'] = int(m.groupdict()['virtual_template'])
                continue

            # Missed heartbeat threshold=2, Peer Terminate ACK timeout=10
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.setdefault('timers', {})
                ret_dict['timers']['missed_heartbeat_threshold'] = int(groups['missed_heartbeat_threshold'])
                ret_dict['timers']['peer_terminate_ack_timeout'] = int(groups['peer_terminate_ack_timeout'])
                continue

            # Heartbeat interval=5, Discovery interval =5, Session Ack timeout=10
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.setdefault('timers', {})
                ret_dict['timers']['heartbeat_interval'] = int(groups['heartbeat_interval'])
                ret_dict['timers']['discovery_interval'] = int(groups['discovery_interval'])
                ret_dict['timers']['session_ack_timeout'] = int(groups['session_ack_timeout'])
                continue

            # Neighbor activity timeout=0, Neighbor Down ACK timeout=10
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.setdefault('timers', {})
                ret_dict['timers']['neighbor_activity_timeout'] = int(groups['neighbor_activity_timeout'])
                ret_dict['timers']['neighbor_down_ack_timeout'] = int(groups['neighbor_down_ack_timeout'])
                continue

        return ret_dict


class ShowDlepCountersSchema(MetaParser):
    """ Schema for 'show dlep counters' """
    
    schema = {
        Any(): {
            'dlep_version': str, 
            'dlep_local_ip': str, 
            'dlepv5_tcp_port': str, 
            'peer_counters': {

                'rx_peer_discovery': int, 
                'tx_peer_offer': int,
                'rx_peer_offer': int, 
                'tx_peer_discovery': int, 
                'rx_peer_init': int, 
                'tx_peer_init_ack': int, 
                'rx_peer_init_ack': int, 
                'tx_peer_init': int, 
                'rx_heartbeat': int, 
                'tx_heartbeat': int, 
                'rx_peer_terminate': int, 
                'tx_peer_terminate_ack': int, 
                'rx_peer_terminate_ack': int, 
                'tx_peer_terminate': int
            }, 
            'neighbor_counters': {

                'rx_neighbor_up': int, 
                'tx_neighbor_up_ack': int, 
                'rx_metric': int, 
                'rx_neighbor_down': int, 
                'tx_neighbor_down_ack': int, 
                'rx_neighbor_down_ack': int, 
                'tx_neighbor_down': int
            }, 
            'exception_counters': {

                'rx_invalid_message': int, 
                'rx_unknown_message': int, 
                'pre-existing_neighbor': int, 
                'neighbor_resource_error': int, 
                'neighbor_not_found': int, 
                'neighbor_msg_peer_not_up': int
            }, 
            'timer_counters': {

                'peer_heartbeat_timer': int, 
                'peer_terminate_ack_timer': int, 
                'neighbor_terminate_ack_timer': int, 
                'neighbor_activity_timer': int, 
                'radio_connect_timer': int
            }
        }, 
            'single_timer_wheel_manet_infra_wheel': {

                'granularity_msec': int, 
                'wheel_size': int, 
                'spoke_index': int, 
                'tick_count': int, 
                'flags': str, 
                'active_timers': int, 
                'high_water_mark': int, 
                'started_timers': int, 
                'restarted_timers': int, 
                'cancelled_timers': int, 
                'expired_timers': int, 
                'long_timers': int, 
                'long_timer_revs': int, 
                'timer_suspends': int
            }
    }


class ShowDlepCounters(ShowDlepCountersSchema):
    """
    Parser for 'show dlep counters' 
    """

    cli_command = "show dlep counters"

    
    def cli(self,output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        # DLEP Counters for Interface 
        
        # DLEP Counters for TenGigabitEthernet0/0/0
        p1 = re.compile(r'^(?P<counter_title1>\w+\s+\w+\s+\w+\s+)(?P<val1>\w+\/\d\/\d(\.\d+)?)$')
        # DLEP Version = RFC 8175 
        p2 = re.compile(r'^(?P<counter_title2>DLEP.*)=(?P<val2>.*)$')
        # Peer Counters:  
        p3 = re.compile(r'^(?P<counter_title3>\w+\s\w+):$')
        # RX Peer Discovery     0      TX Peer Offer             0 
        p4 = re.compile(r'^(?P<counter_title4>\w+\W?\w+\s+(\w+\s+){1,5})(?P<val3>\d+)\s+(?P<counter_title5>\w+\s+(\w+\s+){1,5})?(?P<val4>\d+)?$')
        # Peer Heartbeat Timer         369
        p5 = re.compile(r'^(?P<counter_title6>\w+\s+(\w+\s+){1,4})(?P<val5>\d+)$')
        # Single Timer Wheel "Manet Infra Wheel"
        p6 = re.compile(r'^(?P<counter_title7>\w+\s+(\w+\s+){1,4}"(\w+\s?){1,4})"$')
        # Wheel size       = 4096
        p7 = re.compile(r'^(?P<counter_title8>(\w+\s+){1,4})=(?P<val6>\s+\d+\s?(\w+){0,1})$')
          
        for lines in output.splitlines():
            line = lines.strip()
            # DLEP Counters for TenGigabitEthernet0/0/0
            m = p1.match(line)
            if m:
                title1 = m.groupdict()['counter_title1'].strip().lower().replace(" ", "_")
                par1 = m.groupdict()['val1'].strip()
                interf = title1 + "_" + par1
                ret_dict.setdefault(interf, {})
                continue
                  
            # DLEP Version = RFC 8175
            m = p2.match(line)
            if m:
                title2 = m.groupdict()['counter_title2'].strip().lower().replace(" ", "_")
                par2 = m.groupdict()['val2'].strip()
                ret_dict[interf][title2] = par2
                continue
           
            # Peer Counters:       
            m = p3.match(line)
            if m:
                title3 = m.groupdict()['counter_title3'].strip().lower().replace(" ", "_")
                ret_dict[interf].setdefault(title3, {})
                continue
            
            # RX Peer Discovery     0      TX Peer Offer             0      
            m = p4.match(line)
            if m:
                title4 = m.groupdict()['counter_title4'].strip().lower().replace(" ", "_")
                par4 = m.groupdict()['val3'].strip()
                ret_dict[interf][title3][title4] = int(par4)
                title5 = m.groupdict()['counter_title5'].strip().lower().replace(" ", "_")
                par5 = m.groupdict()['val4'].strip()
                ret_dict[interf][title3][title5] = int(par5)
                continue
            
            # Peer Heartbeat Timer         369      	  
            m = p5.match(line)
            if m:
                title6 = m.groupdict()['counter_title6'].strip().lower().replace(" ", "_")
                par6 = m.groupdict()['val5'].strip()
                ret_dict[interf][title3][title6] = int(par6)
                continue
            
            # Parses (Single Timer Wheel "Manet Infra Wheel") as header   
            m = p6.match(line)
            if m:
                title7 = m.groupdict()['counter_title7'].strip().lower().replace(" ", "_").replace("\"", "")
                ret_dict.setdefault(title7, {})
                continue
            
            # Wheel size       = 4096      
            m = p7.match(line)
            if m:
                title8 = m.groupdict()['counter_title8'].strip().lower().replace(" ", "_")
                par8 = m.groupdict()['val6'].strip()
                if "granularity" == title8:
                    title8 = title8 + "_msec"
                    par8 = par8.split(' ')[0]
                if par8.isnumeric():
                    par8 = int(par8)
                ret_dict[title7][title8] = par8
                continue

        return ret_dict
                  

class ShowDlepConfigInterfaceSchema(MetaParser):
    """Schema for 'show dlep config {interface}'"""

    schema = {
        'version': str,
        'local_ip': str,
        'tcp_port': int,
        'virtual_template': int,
        'timers': {
            'missed_heartbeat_threshold': int,
            'peer_terminate_ack_timeout': int,
            'heartbeat_interval': int,
            'discovery_interval': int,
            'session_ack_timeout': int,
            'neighbor_activity_timeout': int,
            'neighbor_down_ack_timeout': int
        }
    }


class ShowDlepConfigInterface(ShowDlepConfigInterfaceSchema):
    """
    Parser for 'show dlep config {interface}'
    """

    cli_command = 'show dlep config {interface}'

    def cli(self, interface=None, output=None):
        if output is None:
            cmd = self.cli_command.format(interface=interface)
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        # DLEP Version = RFC 8175
        p1 = re.compile(r'^DLEP Version = (?P<version>.*)$')

        # DLEP Local IP=9.9.9.151:55113
        p2 = re.compile(r'^DLEP Local IP=(?P<local_ip>.*)$')

        # DLEPv27 TCP Port = 55114
        p3 = re.compile(r'^DLEPv27 TCP Port = (?P<tcp_port>.*)$')

        # Virtual template=1
        p4 = re.compile(r'^Virtual template=(?P<virtual_template>.*)$')

        # Missed heartbeat threshold=2, Peer Terminate ACK timeout=10
        p5 = re.compile(r'^Missed heartbeat threshold=(?P<missed_heartbeat_threshold>[0-9]+), Peer Terminate ACK timeout=(?P<peer_terminate_ack_timeout>[0-9]+)$')

        # Heartbeat interval=5, Discovery interval =5, Session Ack timeout=10
        p6 = re.compile(r'^Heartbeat interval=(?P<heartbeat_interval>[0-9]+), Discovery interval =(?P<discovery_interval>[0-9]+), Session Ack timeout=(?P<session_ack_timeout>[0-9]+)$')

        # Neighbor activity timeout=0, Neighbor Down ACK timeout=10
        p7 = re.compile(r'^Neighbor activity timeout=(?P<neighbor_activity_timeout>[0-9]+), Neighbor Down ACK timeout=(?P<neighbor_down_ack_timeout>[0-9]+)$')

        for line_raw in out.splitlines():
            line = line_raw.strip()

            # DLEP Version = RFC 8175
            m = p1.match(line)
            if m:
                ret_dict['version'] = m.groupdict()['version']
                continue

            # DLEP Local IP=9.9.9.151:55113
            m = p2.match(line)
            if m:
                ret_dict['local_ip'] = m.groupdict()['local_ip']
                continue

            # DLEPv27 TCP Port = 55114
            m = p3.match(line)
            if m:
                ret_dict['tcp_port'] = int(m.groupdict()['tcp_port'])
                continue

            # Virtual template=1
            m = p4.match(line)
            if m:
                ret_dict['virtual_template'] = int(m.groupdict()['virtual_template'])
                continue

            # Missed heartbeat threshold=2, Peer Terminate ACK timeout=10
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.setdefault('timers', {})
                ret_dict['timers']['missed_heartbeat_threshold'] = int(groups['missed_heartbeat_threshold'])
                ret_dict['timers']['peer_terminate_ack_timeout'] = int(groups['peer_terminate_ack_timeout'])
                continue

            # Heartbeat interval=5, Discovery interval =5, Session Ack timeout=10
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.setdefault('timers', {})
                ret_dict['timers']['heartbeat_interval'] = int(groups['heartbeat_interval'])
                ret_dict['timers']['discovery_interval'] = int(groups['discovery_interval'])
                ret_dict['timers']['session_ack_timeout'] = int(groups['session_ack_timeout'])
                continue

            # Neighbor activity timeout=0, Neighbor Down ACK timeout=10
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.setdefault('timers', {})
                ret_dict['timers']['neighbor_activity_timeout'] = int(groups['neighbor_activity_timeout'])
                ret_dict['timers']['neighbor_down_ack_timeout'] = int(groups['neighbor_down_ack_timeout'])
                continue

        return ret_dict
