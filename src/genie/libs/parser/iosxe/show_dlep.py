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
