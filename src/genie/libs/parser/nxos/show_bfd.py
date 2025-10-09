'''show_bfd.py
NXOS parser for the following show commands
    * show bfd ipv4 neighbors
    * show bfd ipv4 neighbors vrf {vrf}
    * show bfd ipv4 {ipv4_address} neighbors vrf {vrf}
    * show bfd ipv6 neighbors
    * show bfd ipv6 neighbors vrf {vrf}
    * show bfd ipv6 {ipv6_address} neighbors vrf {vrf}
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Optional, Any, Or

# parser utils
from genie.libs.parser.utils.common import Common


class ShowBfdSessionSchema(MetaParser):
    """
    Schema for the following show commands:
        * show bfd ipv4 neighbors
        * show bfd ipv4 neighbors vrf {vrf}
        * show bfd ipv4 {ipv4_address} neighbors vrf {vrf}
        * show bfd ipv6 neighbors
        * show bfd ipv6 neighbors vrf {vrf}
        * show bfd ipv6 {ipv6_address} neighbors vrf {vrf}
    """
    schema = {
        'vrf': {
            Any(): {
                'our_address': {
                    Any(): {
                        'neighbor_address': {
                            Any(): {
                                Optional('ld_rd'): str,
                                Optional('rh_rs'): str,
                                Optional('holdown_timer'): str,
                                Optional('holdown_timer_multiplier'): int,
                                Optional('state'): str,
                                Optional('interface'): str,
                                Optional('vrf'): str,
                                Optional('type'): str,
                            }
                        }
                    }
                }
            }
        }
    }

# ==============================================================
# Parser for the following show commands:
# 	* 'show bfd ipv4 neighbors'
# ==============================================================


class ShowBfdIpv4Session(ShowBfdSessionSchema):
    """ Parser for the following commands:
        * show bfd ipv4 neighbors
        * show bfd ipv4 neighbors vrf {vrf}
        * show bfd ipv4 {ipv4_address} neighbors vrf {vrf}

        OurAddr         NeighAddr       LD/RD                 RH/RS           Holdown(mult)     State       Int                   Vrf                              Type
        32.1.5.2        32.1.5.3        1090519042/1090519063 Up              4741(3)           Up          Po123.5               vxlan-1003                       SH
        32.1.6.2        32.1.6.3        1090519043/1090519064 Up              4741(3)           Up          Po123.6               vxlan-1003                       SH
        32.1.7.2        32.1.7.3        1090519044/1090519065 Up              4741(3)           Up          Po123.7               vxlan-1003                       SH
        11.11.2.1       11.11.5.1       1090519055/1090520660 Up              516(3)            Up          Lo13                  vxlan-1005                       MH
        11.11.2.1       11.11.6.1       1090519380/1090519696 Up              662(3)            Up          Lo12                  vxlan-1004                       MH
        node02#
    """

    cli_command = ['show bfd ipv4 neighbors',
                   'show bfd ipv4 neighbors vrf {vrf}',
                   'show bfd ipv4 {ipv4_address} neighbors vrf {vrf}']

    def cli(self, vrf='', ipv4_address=None, output=None):
        if output is None:
            # execute command to get output
            if vrf:
                if ipv4_address:
                    out = self.device.execute(self.cli_command[2].format(
                        vrf=vrf, ipv4_address=ipv4_address))
                else:
                    out = self.device.execute(
                        self.cli_command[1].format(vrf=vrf))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # initial variables
        ret_dict = {}

        # regex pattern for
        # 10.10.12.1      10.10.12.2      1090519053/1090519042 Up              6000(3)           Up          Eth1/35               default                          SH       N/A
        p1 = re.compile(
            r'^(?P<our_address>[\w\.\:]+)\s+'
            r'(?P<our_neighbor>[\w\.\:]+)\s+'
            r'(?P<ld_rd>\d+\/\d+)\s+(?P<rh_rs>\w+)\s+'
            r'(?P<holdown_timer>N\/A|\d+)\((?P<holdown_timer_multiplier>\d+)\)\s+'
            r'(?P<state>\S+)\s+(?P<interface>\S+)\s+(?P<vrf>\S+)\s+(?P<type>\S+).+?$')

        for line in out.splitlines():
            line = line.strip()

        # match line for p1
        # 10.10.12.1      10.10.12.2      1090519053/1090519042 Up              6000(3)           Up          Eth1/35               default                          SH       N/A
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf = ret_dict.setdefault('vrf', {}). \
                    setdefault(group['vrf'], {})
                our_address = vrf.setdefault(
                    'our_address', {}).setdefault(group['our_address'], {})
                our_neighbor = our_address.setdefault(
                    'neighbor_address', {}).setdefault(group['our_neighbor'], {})
                our_neighbor.update({'ld_rd': group['ld_rd'],
                                     'rh_rs': group['rh_rs'],
                                     'holdown_timer': group['holdown_timer'],
                                     'holdown_timer_multiplier': int(group['holdown_timer_multiplier']),
                                     'state': group['state'],
                                     'vrf': group['vrf'],
                                     'type': group['type'],
                                     'interface': Common.convert_intf_name(group['interface'])})
                continue
        return ret_dict


class ShowBfdIpv6Session(ShowBfdSessionSchema):
    """ Parser for the following commands:
        * show bfd ipv6 neighbors
        * show bfd ipv6 neighbors vrf {vrf}
        * show bfd ipv6 {ipv6_address} neighbors vrf {vrf}

        OurAddr                          NeighAddr
        LD/RD                 RH/RS           Holdown(mult)     State       Int                   Vrf                              Type
        32:1:7::2                        32:1:7::3
        1090519041/1090519061 Up              5917(3)           Up          Po123.7               vxlan-1003                       SH
        32:1:5::2                        32:1:5::3
        1090519045/1090519071 Up              5917(3)           Up          Po123.5               vxlan-1003                       SH
        32:1:6::2                        32:1:6::3
        1090519046/1090519078 Up              5917(3)           Up          Po123.6               vxlan-1003                       SH
        11:11:2::1                       11:11:6::1
        1090519053/1090519050 Up              648(3)            Up          Lo12                  vxlan-1004                       MH
        11:11:2::1                       11:11:5::1
        1090519056/1090520662 Up              523(3)            Up          Lo13                  vxlan-1005                       MH
        node02#
    """

    cli_command = ['show bfd ipv6 neighbors',
                   'show bfd ipv6 neighbors vrf {vrf}',
                   'show bfd ipv6 {ipv6_address} neighbors vrf {vrf}']

    def cli(self, vrf='', ipv6_address=None, output=None):
        if output is None:
            # execute command to get output
            if vrf:
                if ipv6_address:
                    out = self.device.execute(self.cli_command[2].format(
                        vrf=vrf, ipv6_address=ipv6_address))
                else:
                    out = self.device.execute(
                        self.cli_command[1].format(vrf=vrf))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # initial variables
        ret_dict = {}

        # regex pattern for
        # 2001:db8:12::1                   2001:db8:12::2
        p1 = re.compile(r'^(?P<our_address>[0-9A-Fa-f]+:[0-9A-Fa-f:]+)\s+(?P<our_neighbor>'
                        r'[0-9A-Fa-f]+:[0-9A-Fa-f:]+)$')

        # 1090519054/1090519043 Up              6000(3)           Up          Eth1/35               default                          SH
        p2 = re.compile(r'^(?P<ld_rd>\d+\/\d+)\s+(?P<rh_rs>\w+)\s+(?P<holdown_timer>N\/A|\d+)\((?P<holdown_timer_multiplier>\d+)\)\s+(?P<state>\S+)\s+(?P<interface>\S+)\s+(?P<vrf>\S+)\s+(?P<type>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            # match line for p1
            # 2001:db8:12::1                   2001:db8:12::2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                our_address = group['our_address']
                our_neighbor = group['our_neighbor']
                continue
            # match line for p2
            # 1090519054/1090519043 Up              6000(3)           Up          Eth1/35               default
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if group['vrf']:
                    vrf = ret_dict.setdefault('vrf', {}). \
                        setdefault(group['vrf'], {})
                    our_address = vrf.setdefault(
                        'our_address', {}).setdefault(our_address, {})
                    our_neighbor = our_address.setdefault(
                        'neighbor_address', {}).setdefault(our_neighbor, {})
                    our_neighbor.update({'ld_rd': group['ld_rd'],
                                         'rh_rs': group['rh_rs'],
                                         'holdown_timer': group['holdown_timer'],
                                         'holdown_timer_multiplier': int(group['holdown_timer_multiplier']),
                                         'state': group['state'],
                                         'vrf': group['vrf'],
                                         'type': group['type'],
                                         'interface': Common.convert_intf_name(group['interface'])})
                continue
        return ret_dict


class ShowBfdNeighbor(ShowBfdSessionSchema):
    """ Parser for the following commands:
        * show bfd neighbor
    """

    cli_command = ['show bfd neighbor']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # initial variables
        ret_dict = {}

        # regex pattern for
        # OurAddr         NeighAddr       LD/RD                 RH/RS           Holdown(mult)     State       Int               Vrf                       Type
        # 21.1.1.1        21.1.1.2        1090519041/1090519041 Up              1271181547(3)     Up          Eth1/17/1         default                   SH
        # *22.1.1.1        22.1.1.2        1090519042/1090519042 Up              1271183236(3)     Up          Eth1/17/2.5       default                   SH
        p1 = re.compile(r'^(\*)?(?P<our_address>[\w\.\:]+)\s+(?P<our_neighbor>[\w\.\:]+)' \
                        r'\s+(?P<ld_rd>\d+\/\d+)\s+(?P<rh_rs>\S+)\s+(?P<holdown_timer>\d+)' \
                        r'(\s+)?\((?P<holdown_timer_multiplier>\d+)(\s+)?\)\s+(?P<state>\w+)\s+' \
                        r'(?P<interface>[\w\/\.]+)(\s+(?P<vrf>[\w]+)\s+(?P<type>[\w]+))?$')
        for line in out.splitlines():
            line = line.strip()

            # match line for p1
            # 21.1.1.1        21.1.1.2        1090519041/1090519041 Up              1271181547(3)     Up          Eth1/17/1         default                   SH
            # *22.1.1.1        22.1.1.2        1090519042/1090519042 Up              1271183236(3)     Up          Eth1/17/2.5       default                   SH
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf = ret_dict.setdefault('vrf', {}). \
                    setdefault(group['vrf'], {})
                our_address = vrf.setdefault(
                    'our_address', {}).setdefault(group['our_address'], {})
                our_neighbor = our_address.setdefault(
                    'neighbor_address', {}).setdefault(group['our_neighbor'], {})
                our_neighbor.update({'ld_rd': group['ld_rd'],
                                     'rh_rs': group['rh_rs'],
                                     'holdown_timer': group['holdown_timer'],
                                     'holdown_timer_multiplier': int(group['holdown_timer_multiplier']),
                                     'state': group['state'],
                                     'vrf': group['vrf'],
                                     'type': group['type'],
                                     'interface': Common.convert_intf_name(group['interface'])})
                continue

        return ret_dict


class ShowBfdNeighborDetailSchema(MetaParser):

    """
    Schema for the following show commands:
        * show bfd neighbor detail
    """

    schema = {
        'our_address': {
            Any(): {
                'neighbor_address': {
                    Any(): {
                        'ld_rd': str,
                        'rh_rs': str,
                        'holdown_timer': Or(int, str),
                        'holdown_timer_multiplier': int,
                        'state': str,
                        'interface': str,
                        'session': {
                            'state': str,
                            'echo_function': bool,
                        },
                        Optional('session_host'): str,
                        Optional('local_diag'): int,
                        Optional('demand_mode'): int,
                        Optional('poll_bit'): int,
                        Optional('authenticate'): str,
                        Optional('min_tx_interface'): int,
                        Optional('min_rx_interface'): int,
                        Optional('multiplier'): int,
                        Optional('received_min_rx_int'): int,
                        Optional('received_multiplier'): int,
                        Optional('holddown'): int,
                        Optional('holddown_hits'): int,
                        Optional('hello'): int,
                        Optional('hello_hits'): int,
                        Optional('rx'): {
                            'count': int,
                            'min_int_ms': int,
                            'max_int_ms': int,
                            'avg_int_ms': int,
                            'last_ms_ago': int
                        },
                        Optional('tx'): {
                            'count': int,
                            'min_int_ms': int,
                            'max_int_ms': int,
                            'avg_int_ms': int,
                            'last_ms_ago': int
                        },
                        Optional('uptime'): {
                            'days': int,
                            'hrs': int,
                            'mins': int,
                            'secs': int
                        },
                        'last_packet': {
                            'version': int,
                            'diagnostic': int,
                            'state_bit': str,
                            'demand_bit': int,
                            'poll_bit': int,
                            'final_bit': int,
                            'multiplier': int,
                            'length': int,
                            'my_discr': int,
                            'your_discr': int,
                            'min_tx_int': int,
                            'min_rx_int': int,
                        },
                        'hosting_lc': {
                            'lc': int,
                            'down_reason': str,
                            'hosted': str,
                            'offloaded': str,
                        },
                        'registered_protocols': str,
                    }
                }
            }
        }
    }	


class ShowBfdNeighborDetail(ShowBfdNeighborDetailSchema):

    """ Parser for the following commands:
            * 'show bfd neighbor detail'
            * 'show bfd neighbor interface <interface> detail
    """
    cli_command = ['show bfd neighbor detail', 'show bfd neighbor interface {interface} detail']
    def cli(self, interface=None, output=None):
        if output is None:
            if interface:
                out = self.device.execute(self.cli_command[1].format(interface=interface))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output
            
        ret_dict = {}
        # 21.1.1.1        21.1.1.2        1090519041/1090519041 Up              1271180418(3)     Up          Eth1/17/1         default                   SH
        p1 = re.compile(r'^(\*)?(?P<our_address>[\w\.\:]+)\s+(?P<our_neighbor>[\w\.\:]+)\s+(?P<ld_rd>\d+\/\d+)\s+'\
                        r'(?P<rh_rs>\S+)\s+(?P<holdown_timer>(\d+)?(\w\/\w)?)(\s+)?\((?P<holdown_timer_multiplier>\d+)'\
                        r'(\s+)?\)\s+(?P<state>\w+)\s+(?P<interface>[\w\/\.]+)(\s+(?P<vrf>[\w]+)\s+(?P<type>[\w]+))?$')

        # Session state is Up and not using echo function
        # Session state is Up and not using echo functioax/avg: 0/1691/46 last: 36 ms ago
        p2 = re.compile(r'^\s*Session +state +is +(?P<state>\S+) +and +not '\
                        r'+using +echo +((\w+)?(\/)?(\w+)?(\:)?(\/)?( )?)+')

        # Session state is Up and using echo function with 50 ms interval  
        p2_1 = re.compile(r'^\s*Session +state +is +(?P<state>\S+) +and +using +echo '\
                          r'+function +with +(?P<echo>\d+) +ms+ interval')

        # Session type: Singlehop
        p3 = re.compile(r'^\s*Session\s+type:\s+(?P<session_host>\S+)$')

        # Local Diag: 0, Demand mode: 0, Poll bit: 0, Authentication: None
        p4 = re.compile(r'^\s*Local +Diag: +(?P<local_diag>\d+), +Demand '\
                        r'+mode: +(?P<demand_mode>\d+), +Poll +bit: +(?P<poll_bit>\d+)(, +Authentication: +(?P<authenticate>[\w]+))?$')

        # MinTxInt: 50000 us, MinRxInt: 50000 us, Multiplier: 3
        p5 = re.compile(r'^\s*MinTxInt:\s+(?P<min_tx_interface>\d+) +us,\s+MinRxInt:\s+'\
                        r'(?P<min_rx_interface>\d+) +us,\s+Multiplier:\s+(?P<multiplier>\d+)$')

        # Received MinRxInt: 50000 us, Received Multiplier: 3
        p6 = re.compile(r'^\s*Received +MinRxInt:\s+'\
                        r'(?P<received_min_rx_interface>\d+) +us,\s+'\
                        r'Received\s+Multiplier:\s+(?P<received_multiplier>\d+)$')

        # Holdown (hits): 0 ms (0), Hello (hits): 50 ms (2703)
        p7 = re.compile(r'^\s*Hold(d)?own +\(hits\): '\
                        r'+(?P<holddown>\d+)( ms )?\((?P<holddown_hits>\d+)\), '\
                        r'+Hello +\(hits\): +(?P<hello>\d+)( ms )?\((?P<hello_hits>\d+)\)$')

        # Rx Count: 2703, Rx Interval (ms) min/max/avg: 0/2185/879 last: 129901 ms ago
        p8 = re.compile(r'^\s*Rx +Count: +(?P<count>\d+), +Rx +'\
                        r'Interval +\(ms\) +min\/max\/avg: +(?P<min_int_ms>\d+)'\
                        r'\/(?P<max_int_ms>\d+)\/(?P<avg_int_ms>\d+) +'\
                        r'last: +(?P<last_ms_ago>\d+) +ms +ago$')

        # Tx Count: 2703, Tx Interval (ms) min/max/avg: 0/0/0 last: 0 ms ago
        p9 = re.compile(r'^\s*Tx +Count: +(?P<count>\d+), +Tx +Interval +'\
                        r'\(ms\) +min\/max\/avg: +(?P<min_int_ms>\d+)\/(?P<max_int_ms>\d+)'\
                        r'\/(?P<avg_int_ms>\d+) +last: +(?P<last_ms_ago>\d+) +ms +ago$')

        # Registered protocols:  ospf
        p10 = re.compile(r'^\s*Registered +protocols: +(?P<registered_protocols>[\w]+)$')

        # Uptime: 0 days 0 hrs 2 mins 11 secs
        p11 = re.compile(r'^\s*Uptime: +(?P<days>\S+)\s+days\s+(?P<hrs>[\d]+)\s+hrs\s+(?P<mins>[\d]+)\s+mins\s+(?P<secs>[\d]+)\s+secs$')

        # Last packet: Version: 1
        p12 = re.compile(r'^\s*Last\s+packet:\s+Version:\s+(?P<version>\d+)'\
                        r'\s+\-\s+Diagnostic:\s+(?P<diagnostic>\d+)$')

        #              State bit: Up             - Demand bit: 0
        p13 = re.compile(r'^\s*State +bit: +(?P<state_bit>\S+)\s+\-\s+'\
                         r'Demand +bit:\s+(?P<demand_bit>\d+)$')

        #              Poll bit: 0               - Final bit: 0
        p14 = re.compile(r'^\s*Poll\s+bit:\s+(?P<poll_bit>\d+)\s+\-\s+'\
                         r'Final\s+bit:\s+(?P<final_bit>\d+)$')

        #              C bit : 1
        p15 = re.compile(r'^\s*C +bit: +(?P<c_bit>\d+)$')

        #              Multiplier: 3             - Length: 24
        p16 = re.compile(r'^\s*Multiplier: +(?P<multiplier>\d+)\s+\-\s+'\
                         r'Length:\s+(?P<length>\d+)$')

        #              My Discr.: 1090519041     - Your Discr.: 1090519041
        p17 = re.compile(r'^\s*My +Discr\.: +(?P<my_discr>\d+)\s+\-\s+'\
                         r'Your +Discr\.:\s+(?P<your_discr>\d+)')

        #              Min tx interval: 50000    - Min rx interval: 50000
        p18 = re.compile(r'^\s*Min +tx +interval: +(?P<min_tx_interval>\d+)'\
                         r'\s+\-\s+Min +rx +interval:\s+(?P<min_rx_interval>\d+)$')

        # Hosting LC: 1, Down reason: None, Reason not-hosted: None, Offloaded: Yes
        p19 = re.compile(r'^\s*Hosting +LC: +(?P<lc>[\d]+), '\
                        r'+Down +reason: +(?P<down_reason>[\w ]+), +Reason +not-hosted: '\
                        r'+(?P<hosted>[\w]+), Offloaded: +(?P<offloaded>[\w]+)$')

        for line in out.splitlines():
            line = line.strip()

            # 21.1.1.1        21.1.1.2        1090519041/1090519041 Up              1271180418(3)     Up          Eth1/17/1         default                   SH
            m = p1.match(line)
            if m:
                group = m.groupdict()
                our_address = group['our_address']
                our_address = ret_dict.setdefault('our_address', {}). \
                    setdefault(group['our_address'], {})
                our_neighbor = our_address.setdefault('neighbor_address', \
                    {}).setdefault(group['our_neighbor'], {})
                our_neighbor.update({'ld_rd' : group['ld_rd']})
                our_neighbor.update({'rh_rs' : group['rh_rs']})
                if group['holdown_timer'] is int :
                    our_neighbor.update({'holdown_timer' : \
                    int(group['holdown_timer'])})
                else:
                    our_neighbor.update({'holdown_timer' : \
                    (group['holdown_timer'])})
                our_neighbor.update({'holdown_timer_multiplier' : \
                    int(group['holdown_timer_multiplier'])})
                our_neighbor.update({'state' : group['state']})
                our_neighbor.update({'interface' : \
                    Common.convert_intf_name(group['interface'])})
                continue

            # Session state is Up and not using echo function
            m = p2.match(line)
            if m:
                group = m.groupdict()
                session = our_neighbor.setdefault('session', {})
                session.update({'state' : group['state']})
                session.update({'echo_function' : False})
                continue
            
            # Session state is Up and using echo function with 50 ms interval
            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                session = our_neighbor.setdefault('session', {})
                session.update({'state' : group['state']})
                session.update({'echo_function' : True})
                continue
            
            # Session type: Singlehop
            m = p3.match(line)
            if m:
                group = m.groupdict()
                our_neighbor.update({'session_host' : group['session_host']})
                continue

            # Local Diag: 0, Demand mode: 0, Poll bit: 0, Authentication: None
            m = p4.match(line)
            if m:
                group = m.groupdict()
                our_neighbor.update({'local_diag': int(group['local_diag'])})
                our_neighbor.update({'demand_mode': int(group['demand_mode'])})
                our_neighbor.update({'poll_bit': int(group['poll_bit'])})
                our_neighbor.update({'authenticate': group['authenticate']})
                continue

            # MinTxInt: 50000 us, MinRxInt: 50000 us, Multiplier: 3
            m = p5.match(line)
            if m:
                group = m.groupdict()
                our_neighbor.update({'min_tx_interface': int(group['min_tx_interface'])})
                our_neighbor.update({'min_rx_interface': int(group['min_rx_interface'])})
                our_neighbor.update({'multiplier': int(group['multiplier'])})
                continue

            # Received MinRxInt: 50000 us, Received Multiplier: 3
            m = p6.match(line)
            if m:
                group = m.groupdict()
                our_neighbor.update({'received_min_rx_int' : \
                    int(group['received_min_rx_interface'])})
                our_neighbor.update({'received_multiplier' : \
                    int(group['received_multiplier'])})
                continue

            # Holdown (hits): 0 ms (0), Hello (hits): 50 ms (2703)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                our_neighbor.update({k: int(v) for k, v in group.items()})
                continue

            # Rx Count: 2703, Rx Interval (ms) min/max/avg: 0/2185/879 last: 129901 ms ago
            m = p8.match(line)
            if m:
                group = m.groupdict()
                rx = our_neighbor.setdefault('rx', {})
                rx.update({k: int(v) for k, v in group.items()})
                continue 

            # Tx Count: 2703, Tx Interval (ms) min/max/avg: 0/0/0 last: 0 ms ago
            m = p9.match(line)
            if m:
                group = m.groupdict()
                tx = our_neighbor.setdefault('tx', {})
                tx.update({k: int(v) for k, v in group.items()})
                continue

            # Registered protocols:  ospf
            m = p10.match(line)
            if m:
                group = m.groupdict()
                our_neighbor.update({'registered_protocols' : group['registered_protocols']})
                continue
            
            # Uptime: 0 days 0 hrs 2 mins 11 secs
            m = p11.match(line)
            if m:
                group = m.groupdict()
                date = our_neighbor.setdefault('uptime', {})
                date.update({'days' : int(group['days'])})
                date.update({'hrs' : int(group['hrs'])})
                date.update({'mins' : int(group['mins'])})
                date.update({'secs' : int(group['secs'])})
                continue

            # Last packet: Version: 1
            m = p12.match(line)
            if m:
                group = m.groupdict()
                last_packet = our_neighbor.setdefault('last_packet', {})
                last_packet.update({'version' : int(group['version'])})
                last_packet.update({'diagnostic' : int(group['diagnostic'])})
                continue

            #              State bit: Up             - Demand bit: 0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                last_packet.update({'state_bit' : group['state_bit']})
                last_packet.update({'demand_bit' : int(group['demand_bit'])})
                continue

            #              Poll bit: 0               - Final bit: 0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                last_packet.update({'poll_bit' : int(group['poll_bit'])})
                last_packet.update({'final_bit' : int(group['final_bit'])})
                continue

            #              C bit : 1
            m = p15.match(line)
            if m:
                group = m.groupdict()
                last_packet.update({'c_bit' : int(group['c_bit'])})
                continue

            #              Multiplier: 3             - Length: 24
            m = p16.match(line)
            if m:
                group = m.groupdict()
                last_packet.update({'multiplier' : int(group['multiplier'])})
                last_packet.update({'length' : int(group['length'])})
                continue
            
            #              My Discr.: 1090519041     - Your Discr.: 1090519041
            m = p17.match(line)
            if m:
                group = m.groupdict()
                last_packet.update({'my_discr' : int(group['my_discr'])})
                last_packet.update({'your_discr' : int(group['your_discr'])})
                continue

            #              Min tx interval: 50000    - Min rx interval: 50000
            m = p18.match(line)
            if m:
                group = m.groupdict()
                last_packet.update({'min_tx_int' : 
                    int(group['min_tx_interval'])})
                last_packet.update({'min_rx_int' : 
                    int(group['min_rx_interval'])})
                continue
            
            # Hosting LC: 1, Down reason: None, Reason not-hosted: None, Offloaded: Yes
            m = p19.match(line)
            if m:
                group = m.groupdict()
                host = our_neighbor.setdefault('hosting_lc', {})
                host.update({'lc' : int(group['lc'])})
                host.update({'down_reason' : group['down_reason']})
                host.update({'hosted' : group['hosted']})
                host.update({'offloaded' : group['offloaded']})
                continue

        return ret_dict
