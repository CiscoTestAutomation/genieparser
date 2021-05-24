""" show_bfd.py
    supports commands:
        * show bfd session
        * show bfd session destination {ip_address} detail
        * show bfd ipv6 session destination {ip_address} detail
        * show bfd session destination {ip_address}
        * show bfd ipv6 session destination {ip_address}
"""

# Python
import re
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common

# =============================================
# Parser for 'show bfd session'
# =============================================


class ShowBfdSessionSchema(MetaParser):
    schema = {
        'interface': {
            Any(): {
                'dest_ip_address': {
                    Any(): {
                        Optional('echo_total_msec'): int,
                        Optional('echo_multiplier'): int,
                        Optional('echo_msec'): int,
                        Optional('async_total_msec'): int,
                        Optional('async_multiplier'): int,
                        Optional('async_msec'): int,
                        'state': str,
                        'hardware': str,
                        'npu': str,
                        Optional('dampening'): str,
                    }
                }
            }
        }
    }

class ShowBfdSession(ShowBfdSessionSchema):
    """ Parser for show bfd session"""

    cli_command = 'show bfd session'

    def cli(self, output=None):
        """parsing mechanism: cli
        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        """
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}
        
        #Gi0/0/0/36.52       10.129.196.34   450ms(150ms*3)   6s(2s*3)         UP
        p1 = re.compile(
            r'^(?P<intf>\S+) +(?P<dest>\d+\.\d+\.\d+\.\d+) +(?P<echo_total_msec>\d+\w+)\((?P<echo_msec>\d+\w+)\*(?P<echo_multiplier>\d+)\) +(?P<async_total_msec>\d+\w+)\((?P<async_msec>\d+\w+)\*(?P<async_multiplier>\d+)\) +(?P<state>\S+)')
        
        #Gi0/0/0/26.110      10.0.221.98     0s               0s               DOWN DAMP
        p2 = re.compile(
            r'^(?P<intf>\S+) +(?P<dest>\d+\.\d+\.\d+\.\d+) +(?P<echo_total_msec>\d+\w+) +(?P<async_total_msec>\d+\w+) +(?P<state>\S+) ?(?P<damp>\S+)?')
        
        #BE300               172.16.253.53   n/a              n/a              UP
        p3 = re.compile(
            r'^(?P<intf>\S+) +(?P<dest>\d+\.\d+\.\d+\.\d+) +(?P<echo_total_msec>\w+\/\w+) +(?P<async_total_msec>\w+\/\w+) +(?P<state>\S+) ?(?P<damp>\S+)?')
        
        #                                                             No    n/a
        p4 = re.compile(
            r'(?P<hw>[No|Yes]+) +(?P<npu>\S+)')

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            #Gi0/0/0/36.52       10.129.196.34   450ms(150ms*3)   6s(2s*3)         UP
            m = p1.match(line)

            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group['intf'])
                destaddress = group['dest']
                bfd_dict = result_dict.setdefault('interface',{}).setdefault(interface,{}).setdefault('dest_ip_address',{}).setdefault(destaddress,{})
                if group['echo_total_msec'] and re.findall(r'\d+ms',group['echo_total_msec']) != []:
                    group['echo_total_msec'] = group['echo_total_msec'].rstrip('ms')
                    bfd_dict.update({'echo_total_msec': int(group['echo_total_msec'])})
                else:
                    group['echo_total_msec'] = int(group['echo_total_msec'].rstrip('s'))*1000
                    bfd_dict.update({'echo_total_msec': int(group['echo_total_msec'])})
                if group['echo_msec'] and re.findall(r'\d+ms',group['echo_msec']) != []:
                    group['echo_msec'] = group['echo_msec'].rstrip('ms')
                    bfd_dict.update({'echo_msec': int(group['echo_msec'])})
                else:
                    group['echo_msec'] = int(group['echo_msec'].rstrip('s'))*1000
                    bfd_dict.update({'echo_msec': int(group['echo_msec'])})
                bfd_dict.update({'echo_multiplier': int(group['echo_multiplier'])})
                if group['async_total_msec'] and re.findall(r'\d+ms',group['async_total_msec']) != []:
                    group['async_total_msec'] = group['async_total_msec'].rstrip('ms')
                    bfd_dict.update({'async_total_msec': int(group['async_total_msec'])})
                else:
                    group['async_total_msec'] = int(group['async_total_msec'].rstrip('s'))*1000
                    bfd_dict.update({'async_total_msec': int(group['async_total_msec'])})
                if group['async_msec'] and re.findall(r'\d+ms',group['async_msec']) != []:
                    group['async_msec'] = group['async_msec'].rstrip('ms')
                    bfd_dict.update({'async_msec': int(group['async_msec'])})
                else:
                    group['async_msec'] = int(group['async_msec'].rstrip('s'))*1000
                    bfd_dict.update({'async_msec': int(group['async_msec'])})
                bfd_dict.update({'async_multiplier': int(group['async_multiplier'])})
                bfd_dict.update({'state': group['state']})

            #Gi0/0/0/26.110      10.0.221.98     0s               0s               DOWN DAMP
            m = p2.match(line)

            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group['intf'])
                destaddress = group['dest']
                bfd_dict = result_dict.setdefault('interface',{}).setdefault(interface,{}).setdefault('dest_ip_address',{}).setdefault(destaddress,{})
                if group['echo_total_msec'] and re.findall(r'\d+ms',group['echo_total_msec']) != []:
                    group['echo_total_msec'] = group['echo_total_msec'].rstrip('ms')
                    bfd_dict.update({'echo_total_msec': int(group['echo_total_msec'])})
                else:
                    group['echo_total_msec'] = int(group['echo_total_msec'].rstrip('s'))*1000
                    bfd_dict.update({'echo_total_msec': int(group['echo_total_msec'])})
                if group['async_total_msec'] and re.findall(r'\d+ms',group['async_total_msec']) != []:
                    group['async_total_msec'] = group['async_total_msec'].rstrip('ms')
                    bfd_dict.update({'async_total_msec': int(group['async_total_msec'])})
                else:
                    group['async_total_msec'] = int(group['async_total_msec'].rstrip('s'))*1000
                    bfd_dict.update({'async_total_msec': int(group['async_total_msec'])})
                bfd_dict.update({'state': group['state']})
                if group['damp']:
                    bfd_dict.update({'dampening': group['damp']})

            #BE300               172.16.253.53   n/a              n/a              UP
            m = p3.match(line)

            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group['intf'])
                destaddress = group['dest']
                bfd_dict = result_dict.setdefault('interface',{}).setdefault(interface,{}).setdefault('dest_ip_address',{}).setdefault(destaddress,{})
                bfd_dict.update({'state': group['state']})
                if group['damp']:
                    bfd_dict.update({'dampening': group['damp']})

            #                                                             No    n/a
            m = p4.match(line)

            if m:
                group = m.groupdict()
                bfd_dict.update({'hardware': group['hw']})
                bfd_dict.update({'npu': group['npu']})
                continue

        return result_dict



# ==================================================
# Parser for 'show bfd session destination details'
# ==================================================

class ShowBfdSessionDestinationDetailsSchema(MetaParser):

    """ 
        Schema for the following show commands:
            * show bfd session destination {ip_address} detail
            *show bfd ipv6 session destination {ip_address} detail
    """

    schema = {
        'src': {
            Any():{
                'dest':{
                    Any():{
                        'interface': str,
        		        'location': str,
        		        'session':{
        		        	'state': str,
        		        	'duration': str,
        		        	'num_of_times_up': int,
        		        	'type': str,
        		        	'owner_info':{
        		        		Any():{
        		        			'desired_interval_ms': int,
        		        			'desired_multiplier': int,
        		        			'adjusted_interval_ms': int,
        		        			'adjusted_multiplier': int,
        		        		}
        		        	}
        		        },
        		        Any():{
        		        	'version': int,
        		        	'desired_tx_interval_ms': int,
        		        	'required_rx_interval_ms': int,
        		        	'required_echo_rx_interval_ms': int,
        		        	'multiplier': int,
        		        	'diag': str,
        		        	Optional('my_discr'): int,
        		        	Optional('your_discr'): int,
        		        	Optional('state'): str,
        		        	Optional(Any()): int,
        		        },
        		        'timer_vals':{
        		        	'local_async_tx_interval_ms': int,
        		        	'remote_async_tx_interval_ms': int,
        		        	'desired_echo_tx_interval_ms': int,
        		        	'local_echo_tax_interval_ms': int,
        		        	Optional('echo_detection_time_ms'): int,
        		        	Optional('async_detection_time_ms'): int,
        		        },
        		        'local_stats': {
        		        	'latency_of_echo_packets':{
        		        		'num_of_packets': int,
        		        		'min_ms':int,
        		        		'max_ms': int,
                                'avg_ms': int,
        		        		},
        		        	Any(): {
        		        		Any(): {
        		        			'num_intervals': int,
        		        			'min_ms': int,
        		        			'max_ms': int,
        		        			'avg_ms': int,
        		        			Optional('last_packet_transmitted_ms_ago'): int,
        		        			Optional('last_packet_received_ms_ago'): int,
        		        		},
        		        	}
                        }
                    }       
        		}
        	}
        }
    }

class ShowBfdSessionDestinationDetails(ShowBfdSessionDestinationDetailsSchema):

    """
    Parser for the following show commands:
        * show bfd session destination {ip_address} detail
        * show bfd ipv6 session destination {ip_address} detail
    """

    cli_command = ['show bfd session destination {ip_address} detail',
                   'show bfd {ipv6} session destination {ip_address} detail']

    def cli(self, ip_address, ipv6='', output=None):
        
        if output is None:
            if ipv6:
                out = self.device.execute(
                           self.cli_command[1].format(ipv6=ipv6, ip_address=ip_address))
            else:
                out = self.device.execute(
                           self.cli_command[0].format(ip_address=ip_address))
        else:
            out = output

        result_dict = {}

        # I/f: GigabitEthernet0/0/0/0, Location: 0/0/CPU0
        p1 = re.compile(r'I/f: +(?P<interface>[\S\s]+), '
                        r'+Location: +(?P<location>[\S\s]+)')

        # Dest: 10.4.1.1
        p2 = re.compile(r'Dest: +(?P<dest>[\S\s]+)')

        # Src: 10.4.1.2
        p3 = re.compile(r'Src: +(?P<src>[\S\s]+)')

        #  State: UP for 0d:0h:5m:50s, number of times UP: 1
        p4 = re.compile(r'State: +(?P<state>UP|DOWN|Up|Down|up|down)'
                        r' +for +(?P<duration>[\S\s]+),'
                        r' +number +of +times +UP: +(?P<num_of_times_up>[\d]+)')

        #  Session type: PR/V4/SH
        p5 = re.compile(r'Session +type: +(?P<type>[\S\s]+)')

        # Received parameters:
        # Transmitted parameters:
        p6 = re.compile(r'(?P<param>Received|Transmitted) +parameters')

        #  Version: 1, desired tx interval: 500 ms, required rx interval: 500 ms
        p7 = re.compile(r'Version: +(?P<version>\d+),'
                        r' +desired +tx +interval:'
                        r' +(?P<tx_interval>\d+) +(?P<tx_interval_unit>\w+),'
                        r' +required +rx +interval: +(?P<rx_interval>\d+)'
                        r' +(?P<rx_interval_unit>\w+)')

        #  Required echo rx interval: 0 ms, multiplier: 6, diag: None
        p8 = re.compile(r'Required echo rx interval:'
                        r' +(?P<echo_rx_interval>\d+)'
                        r' +(?P<echo_rx_interval_unit>[\w]+),'
                        r' +multiplier: (?P<multiplier>\d+),'
                        r' +diag: +(?P<diag>[\S\s]+)')

        # My discr: 18, your discr: 2148532226, state UP, D/F/P/C/A: 0/0/0/1/0
        p9 = re.compile(r'My +discr: +(?P<my_discr>\d+), +your +discr:'
                        r' +(?P<your_discr>\d+), +state +(?P<state>(ADMIN +)?(UP|DOWN)),'
                        r' +D\/F\/P\/C\/A: +(?P<d_f_p_c_a>[\d\/]+)')
        
        # Timer Values:
        p10 = re.compile(r'Timer +Values:')

        # Local negotiated async tx interval: 500 ms
        p11 = re.compile(r'Local +negotiated +async +tx +interval:'
                         r' +(?P<tx_interval>\d+) +(?P<tx_interval_unit>[\w]+)')

        # Remote negotiated async tx interval: 500 ms
        p12 = re.compile(r'Remote +negotiated +async +tx +interval:'
                         r' +(?P<tx_interval>\d+) +(?P<tx_interval_unit>[\w]+)')
        
        # Desired echo tx interval: 500 ms, local negotiated echo tx interval: 0 ms
        p13 = re.compile(r'Desired +echo +tx +interval:'
                         r' +(?P<echo_tx>\d+) +(?P<echo_tx_unit>\w+),'
                         r' +local +negotiated +echo +tx +interval:'
                         r' +(?P<local_echo_tx>\d+) +(?P<local_echo_tx_unit>\w+)')

        # Echo detection time: 0 ms(0 ms*6), async detection time: 3 s(500 ms*6)
        p14 = re.compile(r'Echo +detection +time:'
                         r' +(?P<echo_time>\d+) +(?P<echo_time_unit>\w+)(\([\S\s]+\))?,'
                         r' +async +detection +time:'
                         r' +(?P<async_time>\d+) +(?P<async_time_unit>\w+)(\([\S\s]+\))?')
        
        # Local Stats:
        p15 = re.compile(r'Local +Stats:')

        #  Intervals between async packets:
        #  Intervals between echo packets:
        p16 = re.compile(r'Intervals +between +(?P<packet_type>async|echo) packets:')

        #   Tx: Number of intervals=100, min=1 ms, max=500 ms, avg=229 ms
        #   Rx: Number of intervals=100, min=490 ms, max=513 ms, avg=500 ms
        p17 = re.compile(r'(?P<rx_tx>Tx|Rx): +Number +of +intervals=(?P<num_intervals>\d+),'
                         r' +min=(?P<min>\d+) +(?P<min_unit>\w+),'
                         r' +max=(?P<max>\d+) +(?P<max_unit>\w+),'
                         r' +avg=(?P<avg>\d+) +(?P<avg_unit>\w+)')

        #       Last packet transmitted 48 ms ago
        #       Last packet received 304 ms ago
        #       Last packet transmitted 0 s ago
        #       Last packet received 0 s ago
        p18 = re.compile(r'Last +packet +(?P<packet_direction>transmitted|received) +(?P<packet>\d+)'
                         r' +(?P<packet_unit>\w+) +ago')

        # Latency of echo packets (time between tx and rx):
        p19 = re.compile(r'Latency +of +echo +packets +\(time +between +tx +and +rx\):')

        #   Number of packets: 0, min=0 ms, max=0 ms, avg=0 ms 
        p20 = re.compile(r'Number +of +packets: +(?P<num_packets>\d+),'
                         r' +min=(?P<min>\d+) +(?P<min_unit>\w+),'
                         r' +max=(?P<max>\d+) +(?P<max_unit>\w+),'
                         r' +avg=(?P<avg>\d+) +(?P<avg_unit>\w+)')

        # Session owner information:
        p21 = re.compile(r'Session +owner +information:')

        #   ipv4_static          500 ms     6          500 ms     6
        p22 = re.compile(r'(?P<client>[\S\s]+)'
                         r' +(?P<desired_interval>\d+)'
                         r' +(?P<desired_interval_unit>\w+)'
                         r' +(?P<desired_multiplier>\d+)'
                         r' +(?P<adjusted_interval>\d+)'
                         r' +(?P<adjusted_interval_unit>\w+)'
                         r' +(?P<adjusted_multiplier>\d+)')

        dfpca_dict = {'d': 'demand_bit',
                      'f': 'final_bit',
                      'p': 'poll_bit',
                      'c': 'control_bit',
                      'a': 'authentication_bit'}

        for line in out.splitlines():
            line = line.strip()
            # I/f: GigabitEthernet0/0/0/0, Location: 0/0/CPU0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                location = group['location']

                continue

            # Dest: 10.4.1.1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                dest = group['dest']
                continue

            # Src: 10.4.1.2
            m = p3.match(line)
            if m:
                group = m.groupdict()
                dest_dict = result_dict.setdefault('src', {})\
                                       .setdefault(group['src'], {})\
                                       .setdefault('dest', {})\
                                       .setdefault(dest, {})
                dest_dict.update({'interface': interface,
                                  'location': location})
                continue

            #  State: UP for 0d:0h:5m:50s, number of times UP: 1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                session_dict = dest_dict.setdefault('session', {})
                session_dict.update({'state': group['state'],
                                     'duration': group['duration'],
                                     'num_of_times_up': int(group['num_of_times_up'])})
                continue

            #  Session type: PR/V4/SH
            m = p5.match(line)
            if m:
                group = m.groupdict()
                session_dict.update({'type': group['type']})
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                params_dict = dest_dict.setdefault(
                                '{}_parameters'.format(group['param'].lower()), {})
                continue

            #  Version: 1, desired tx interval: 500 ms, required rx interval: 500 ms
            m = p7.match(line)
            if m:
                group = m.groupdict()
                tx_interval = int(group['tx_interval'])
                if group['tx_interval_unit'] == 's':
                    tx_interval*=1000

                rx_interval= int(group['rx_interval'])
                if group['rx_interval_unit'] == 's':
                    rx_interval*=1000

                params_dict.update({'version': int(group['version']),
                                    'desired_tx_interval_ms': tx_interval,
                                    'required_rx_interval_ms': rx_interval,
                                    })
                continue

            #  Required echo rx interval: 0 ms, multiplier: 6, diag: None
            m = p8.match(line)
            if m:
                group = m.groupdict()
                rx_interval = int(group['echo_rx_interval'])
                if group['echo_rx_interval_unit'] == 's':
                    rx_interval *=1000
                params_dict.update({'required_echo_rx_interval_ms': rx_interval,
                                    'multiplier': int(group['multiplier']),
                                    'diag': group['diag'],
                                    })
                continue

            # My discr: 18, your discr: 2148532226, state UP, D/F/P/C/A: 0/0/0/1/0
            m = p9.match(line)
            if m:

                group = m.groupdict()
                if group.get('d_f_p_c_a'):
                    dfpca_list = group['d_f_p_c_a'].split('/')
                    dfpca_dict_with_value = dict(zip(dfpca_dict.values(), dfpca_list))
                    for key, value in dfpca_dict_with_value.items():
                        params_dict.update({key: int(value)})

                params_dict.update({'my_discr': int(group['my_discr']),
                                    'your_discr':int(group['your_discr']),
                                    'state': group['state']
                                    })
                continue


            # Timer Values:
            m = p10.match(line)
            if m:
                timer_dict = dest_dict.setdefault('timer_vals', {})
                continue

            # Local negotiated async tx interval: 500 ms
            m = p11.match(line)
            if m:
                group = m.groupdict()
                tx_interval = int(group['tx_interval'])
                if group['tx_interval_unit'] == 's':
                    tx_interval*=1000
                timer_dict.update({'local_async_tx_interval_ms': tx_interval})
                continue

            # Remote negotiated async tx interval: 500 ms
            m = p12.match(line)
            if m:
                group = m.groupdict()
                tx_interval = int(group['tx_interval'])
                if group['tx_interval_unit'] == 's':
                    tx_interval*=1000
                timer_dict.update({'remote_async_tx_interval_ms': tx_interval})
                continue

            # Desired echo tx interval: 500 ms, local negotiated echo tx interval: 0 ms
            m = p13.match(line)
            if m:
                group = m.groupdict()
                echo_tx = int(group['echo_tx'])
                if group['echo_tx_unit'] == 's':
                    echo_tx *= 1000

                local_echo_tx = int(group['local_echo_tx'])
                if group['local_echo_tx_unit'] == 's':
                    local_echo_tx *=1000

                timer_dict.update({'desired_echo_tx_interval_ms': echo_tx,
                                   'local_echo_tax_interval_ms': local_echo_tx})
                continue

            # Echo detection time: 0 ms(0 ms*6), async detection time: 3 s(500 ms*6)
            m = p14.match(line)
            if m:
                group = m.groupdict()
                echo_time = int(group['echo_time'])
                if group['echo_time_unit'] == 's':
                    echo_time *= 1000
                
                async_time = int(group['async_time'])
                if group['async_time_unit'] == 's':
                    async_time *= 1000
                timer_dict.update({'echo_detection_time_ms': echo_time,
                                   'async_detection_time_ms': async_time})
                continue

            # Local Stats:
            m = p15.match(line)
            if m:
                local_dict = dest_dict.setdefault('local_stats', {})
                continue

            #  Intervals between async packets:
            #  Intervals between echo packets:
            m = p16.match(line)
            if m:
                group = m.groupdict()
                interval_dict = local_dict.setdefault('interval_{}_packets'.
                                                      format(group['packet_type']), {})
                continue

            #   Tx: Number of intervals=100, min=1 ms, max=500 ms, avg=229 ms
            #   Rx: Number of intervals=100, min=490 ms, max=513 ms, avg=500 ms
            m = p17.match(line)
            if m:
                group = m.groupdict()
                rx_tx_dict = interval_dict.setdefault(group['rx_tx'], {})
                min_ = int(group['min'])*1000 if group['min_unit'] == 's' else int(group['min'])
                max_ = int(group['max'])*1000 if group['max_unit'] == 's' else int(group['max'])
                avg_ = int(group['avg'])*1000 if group['avg_unit'] == 's' else int(group['avg'])

                rx_tx_dict.update({'num_intervals': int(group['num_intervals']),
                                   'min_ms': min_,
                                   'max_ms': max_,
                                   'avg_ms': avg_})
                continue

            #       Last packet transmitted 48 ms ago
            #       Last packet received 304 ms ago
            #       Last packet transmitted 0 s ago
            #       Last packet received 0 s ago
            m = p18.match(line)
            if m:
                group = m.groupdict()
                direction = group['packet_direction']
                packet = int(group['packet'])
                if group['packet_unit'] == 's':
                    packet*=1000

                rx_tx_dict.update({'last_packet_{}_ms_ago'.format(direction): packet})
                continue

            # Latency of echo packets (time between tx and rx):
            m = p19.match(line)
            if m:
                group = m.groupdict()
                latency_dict = local_dict.setdefault('latency_of_echo_packets', {})
                continue

            #   Number of packets: 0, min=0 ms, max=0 ms, avg=0 ms 
            m = p20.match(line)
            if m:
                group = m.groupdict()
                min_ = int(group['min'])*1000 if group['min_unit'] == 's' else int(group['min'])
                max_ = int(group['max'])*1000 if group['max_unit'] == 's' else int(group['max'])
                avg_ = int(group['avg'])*1000 if group['avg_unit'] == 's' else int(group['avg'])

                latency_dict.update({'num_of_packets': int(group['num_packets']),
                                     'min_ms': min_,
                                     'max_ms': max_,
                                     'avg_ms': avg_})
                continue

            # Session owner information:
            m = p21.match(line)
            if m:
                group = m.groupdict()
                owner_dict = session_dict.setdefault('owner_info', {})
                continue

            m = p22.match(line)
            if m:
                group = m.groupdict()
                client_dict = owner_dict.setdefault(group['client'].strip(), {})

                desired_interval = int(group['desired_interval'])
                if group['desired_interval_unit'] == 's':
                    desired_interval*=1000
                client_dict.update({'desired_interval_ms': desired_interval,
                                   'desired_multiplier': int(group['desired_multiplier'])
                                   })

                adjusted_interval = int(group['adjusted_interval'])
                if group['adjusted_interval_unit'] == 's':
                    adjusted_interval*=1000
                client_dict.update({'adjusted_interval_ms': adjusted_interval,
                                    'adjusted_multiplier': int(group['adjusted_multiplier'])
                })
                continue
            

        return result_dict

class ShowBfdSessionDestinationSchema(MetaParser):

    """ 
        Schema for the following show commands:
            * show bfd session destination {ip_address}
            * show bfd ipv6 session destination {ip_address}
    """

    schema = {
        'dest':{
            Any():{
                'interface': str,
                Optional('session'):{
                    'state': str,
                },
                Optional('hardware'): str,
                Optional('npu'): str,
                'timer_vals':{
                    'async_detection_time': str,
                    'async_detection_time_ms': int,
                    Optional('async_detection_interval_ms'): int,
                    Optional('async_detection_multiplier'): int,
                    'echo_detection_time': str,
                    'echo_detection_time_ms': int,
                    Optional('echo_detection_interval_ms'): int,
                    Optional('echo_detection_multiplier'): int,
                },
            }       
        }
    }

class ShowBfdSessionDestination(ShowBfdSessionDestinationSchema):
    """
    Parser for the following show commands:
        * show bfd session destination {ip_address}
        * show bfd ipv6 session destination {ip_address}
    """

    cli_command = ['show bfd session destination {ip_address}',
                   'show bfd {ipv6} session destination {ip_address}']

    def cli(self, ip_address, ipv6='', output=None):
        
        if output is None:
            if ipv6:
                out = self.device.execute(
                           self.cli_command[1].format(ipv6=ipv6, ip_address=ip_address))
            else:
                out = self.device.execute(
                           self.cli_command[0].format(ip_address=ip_address))
        else:
            out = output

        ret_dict = {}
        
        # Gi0/0/0/0           2001:10::1 
        p1 = re.compile(r'^(((?P<hardware>(No|Yes)) +(?P<npu>\S+))|(?P<interface>\S+) +(?P<dest>[\w\:\/]+))$')

        # Te0/0/2/2           10.0.0.1        0s(0s*0)         450ms(150ms*3)   UP
        # Gi0/0/0/0           10.0.0.1        0s               12s              DOWN
        p2 = re.compile(r'^(((?P<hardware>(No|Yes)) +(?P<npu>\S+))|((?P<interface>\S+) +(?P<dest>\S+))) +'
            r'(?P<echo_detection_time>(?P<echo_time>\d+) *(?P<echo_time_unit>\w+)(\((?P<echo_detection_interval_ms>\d+)[\w ]+\*(?P<echo_detection_multiplier>\d+)\))?) +'
            r'(?P<async_detection_time>(?P<async_time>\d+) *(?P<async_time_unit>\w+)(\((?P<async_detection_interval_ms>\d+)[\w ]+\*(?P<async_detection_multiplier>\d+)\))?) +'
            r'(?P<state>\S+)$')


        for line in out.splitlines():
            line = line.strip()

            # Gi0/0/0/0           2001:10::1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf = group.get('interface', None)
                ip_address = group.get('dest', None)
                if intf and ip_address:
                    dest_dict = ret_dict.setdefault('dest', {}). \
                        setdefault(ip_address, {})
                    dest_dict.update({'interface': intf})

                hardware = group.get('hardware', None)
                npu = group.get('npu', None)
                if hardware and npu:
                    dest_dict.update({'hardware': hardware})
                    dest_dict.update({'npu': npu})

                continue
            
            # Te0/0/2/2           10.0.0.1        0s(0s*0)         450ms(150ms*3)   UP
            m = p2.match(line)
            if m:
                group = m.groupdict()
                intf = group.get('interface', None)
                ip_address = group.get('dest', None)
                echo_detection_time = group['echo_detection_time']
                async_detection_time = group['async_detection_time']
                echo_detection_interval_ms = group['echo_detection_interval_ms']
                echo_detection_multiplier = group['echo_detection_multiplier']
                async_detection_interval_ms = group['async_detection_interval_ms']
                async_detection_multiplier = group['async_detection_multiplier']
                
                state = group['state']
                
                if intf and ip_address:
                    dest_dict = ret_dict.setdefault('dest', {}). \
                        setdefault(ip_address, {})
                    dest_dict.update({'interface': intf})
                
                hardware = group.get('hardware', None)
                npu = group.get('npu', None)
                if hardware and npu:
                    dest_dict.update({'hardware': hardware})
                    dest_dict.update({'npu': npu})

                timer_vals_dict = dest_dict.setdefault('timer_vals', {})
                timer_vals_dict.update({'echo_detection_time': echo_detection_time})
                if echo_detection_interval_ms:
                    timer_vals_dict.update({'echo_detection_interval_ms': int(echo_detection_interval_ms)})
                if echo_detection_multiplier:
                    timer_vals_dict.update({'echo_detection_multiplier': int(echo_detection_multiplier)})

                timer_vals_dict.update({'async_detection_time': async_detection_time})
                if async_detection_interval_ms:
                    timer_vals_dict.update({'async_detection_interval_ms': int(async_detection_interval_ms)})
                if async_detection_multiplier:
                    timer_vals_dict.update({'async_detection_multiplier': int(async_detection_multiplier)})

                session_dict = dest_dict.setdefault('session', {})
                session_dict.update({'state': state})

                echo_time = int(group['echo_time'])
                if group['echo_time_unit'] == 's':
                    echo_time *= 1000
                
                async_time = int(group['async_time'])
                if group['async_time_unit'] == 's':
                    async_time *= 1000
                timer_vals_dict.update({'echo_detection_time_ms': echo_time,
                                   'async_detection_time_ms': async_time})
                continue
        
        return ret_dict
