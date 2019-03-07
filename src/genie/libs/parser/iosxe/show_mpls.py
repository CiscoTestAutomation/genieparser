"""  show_ldp.py
   supported commands:
        *  show mpls ldp neighbor
        *  show mpls ldp neighbor vrf <vrf>
        *  show mpls ldp neighbor detail
        *  show mpls ldp bindings
        *  show mpls ldp bindings all
        *  show mpls ldp bindings all detail
        *  show mpls ldp capabilities
        *  show mpls ldp capabilities all
        *  show mpls ldp discovery
        *  show mpls ldp discovery detail
        *  show mpls ldp discovery all
        *  show mpls ldp discovery all detail
        *  show mpls ldp discovery vrf <vrf>
        *  show mpls ldp discovery vrf <vrf> detail
        *  show mpls ldp igp sync
        *  show mpls ldp igp sync all
        *  show mpls ldp igp sync interface <interface>
        *  show mpls ldp igp sync vrf <vrf>
        *  show mpls ldp statistics
       	*  show mpls ldp parameters
"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                               Any, \
                                               Optional


class ShowMplsLdpNeighborSchema(MetaParser):
    """Schema for show mpls ldp neighbor"""
    schema = {
        'vrf': {
            Any(): {
                'neighbor': {
                    Any(): {
                        'local_ldp': str,
                        'tcp_connection': list,
                        'state': str,
                        'msg_sent': int,
                        'msg_rcvd': int,
                        'downstream': bool,
                        Optional('last_tib_rev_sent'): int,
                        Optional('password'): str,
                        'uptime': str,
                        Optional('peer_holdtime_ms'): str,
                        Optional('ka_interval_ms'): str,
                        Optional('peer_state'): str,
                        'ldp_source': {
                            'interface': str,
                            'src_ip_address': str,
                            Optional('holdtime_ms'): int,
                            Optional('hello_interval_ms'): int,
                        },
                        'address_bound': list,
                        Optional('capabilities_sent'): {
                            'iccp_type': str,
                            'maj_version': int,
                            'min_version': int,
                            'dynamic_anouncement': str,
                            'mldp_point_to_multipoint': str,
                            'mldp_multipoint_to_multipoint': str,
                            'typed_wildcard': str,

                        },
                        Optional('nsr'): str,
                        Optional('capabilities_received'): {
                            Optional('iccp_type'): str,
                            Optional('maj_version'): int,
                            Optional('min_version'): int,
                            Optional('dynamic_anouncement'): str,
                            Optional('mldp_point_to_multipoint'): str,
                            Optional('mldp_multipoint_to_multipoint'): str,
                            Optional('typed_wildcard'): str,

                        },
                    },
                }
            }
        },
    }


class ShowMplsLdpNeighbor(ShowMplsLdpNeighborSchema):
    """Parser for show mpls ldp neighbor,
                  show mpls ldp neighbor vrf <vrf>"""

    cli_command = ['show mpls ldp neighbor', 'show mpls ldp neighbor vrf {vrf}']

    def cli(self, vrf="",cmd="",output=None):
        if output is None:
            if not cmd:
                if vrf:
                    cmd = self.cli_command[1].format(vrf=vrf)
                else:
                    cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        if not vrf:
            vrf = 'default'

        # initial return dictionary
        result_dict = {}
        address_bound_flag = False
        received_flag = False
        sent_flag = False

        # Peer LDP Ident: 106.162.197.252:0; Local LDP Ident 106.162.197.254:0
        p1 = re.compile(r'^Peer +LDP +Ident: +(?P<peer_ldp>\S+); +Local +LDP +Ident +(?P<local_ldp>\S+)$')

        #     TCP connection: 106.162.197.252.646 - 106.162.197.254.20170
        p2 = re.compile(r'^TCP +connection: +(?P<tcp_connection>[\S\s]+)$')

        #     State: Oper; Msgs sent/rcvd: 824/825; Downstream
        #     State: Oper; Msgs sent/rcvd: 824/825; Downstream; Last TIB rev sent 4103
        p3 = re.compile(r'^State: +(?P<state>\w+); +Msgs +sent\/rcvd: +(?P<msg_sent>\d+)\/(?P<msg_rcvd>\d+);'
                                ' +(?P<downstream>\w+)(; +Last +TIB +rev +sent +(?P<last_tib_rev_sent>\d+))?$')

        #  Up time: 04:26:14
        #  Up time: 3d21h; UID: 4; Peer Id 0
        p4 = re.compile(r'^Up +time: +(?P<up_time>[\w\:]+)(; +UID: (?P<uid>\d+); +Peer +Id +(?P<peer_id>\d+))?$')

        #     LDP discovery sources:
        #       GigabitEthernet0/0/0, Src IP addr: 106.162.197.93
        p5 = re.compile(r'^(?P<interface>[\S]+)(,|;) +Src +IP +addr: +(?P<src_ip_address>[\d\.]+)$')

        #       holdtime: 15000 ms, hello interval: 5000 ms
        p5_1 = re.compile(r'^holdtime: +(?P<holdtime>\d+) +ms, +hello +interval: +(?P<hello_interval>\d+) +ms$')

        #     Addresses bound to peer LDP Ident:
        p6 = re.compile(r'^Addresses +bound +to +peer +LDP +Ident:$')

        #       106.162.197.252 27.93.202.49    106.162.197.101 113.146.190.254
        p7 = re.compile(r'^(?P<address_bound_peer_ldp>[\d\.\s]+)$')

        # Peer holdtime: 180000 ms; KA interval: 60000 ms; Peer state: estab
        p8 = re.compile(r'^Peer +holdtime: +(?P<peer_holdtime>\d+) +ms, +KA +interval: +(?P<ka_interval>\d+) +ms;'
                         ' +Peer +state +(?P<peer_state>\S+)$')

        # Password: not required, none, in use
        p9 = re.compile(r'^Password: +(?P<password>[\S\s]+)$')

        #NSR: Not Ready
        p10 = re.compile(r'^NSR: +(?P<nsr>[\S\s]+)$')

        # Capabilities Sent:
        p11 = re.compile(r'^Capabilities +Sent:$')

        #   [ICCP (type 0x0405) MajVer 1 MinVer 0]
        p12 = re.compile(r'^\[ICCP \(type +(?P<type>\w+)\) +MajVer +(?P<maj_ver>\d+) +MinVer +(?P<min_ver>\d+)\]$')

        #   [Dynamic Announcement (0x0506)]
        p13 = re.compile(r'^\[Dynamic +Announcement \((?P<dynamic_anouncement>\w+)\)\]$')

        #   [mLDP Point-to-Multipoint (0x0508)]
        p14 = re.compile(r'^\[mLDP +Point\-to\-Multipoint \((?P<mldp_point_to_multipoint>\w+)\)\]$')
        #   [mLDP Multipoint-to-Multipoint (0x0509)]
        p15 = re.compile(r'^\[mLDP +Multipoint\-to\-Multipoint \((?P<mldp_multipoint_to_multipoint>\w+)\)\]$')
        #   [Typed Wildcard (0x050B)]
        p16 = re.compile(r'^\[Typed +Wildcard \((?P<typed_wildcard>\w+)\)\]$')

        # Capabilities Received:
        p17 = re.compile(r'^Capabilities +Received:$')
        #   [None]
        p18 = re.compile(r'^\[None\]$')

        for line in out.splitlines():
            line = line.strip()
            # Peer LDP Ident: 106.162.197.252:0; Local LDP Ident 106.162.197.254:0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                address_bound_flag = False
                peer_dict = result_dict.setdefault('vrf', {}).\
                                        setdefault(vrf,{}).\
                                        setdefault('neighbor',{}).\
                                        setdefault(group['peer_ldp'] ,{})
                peer_dict.update({'local_ldp':group['local_ldp']})
                continue

            # TCP connection: 106.162.197.252.646 - 106.162.197.254.20170
            m = p2.match(line)
            if m:
                group = m.groupdict()
                tcpconnection = group['tcp_connection']
                if '-' in tcpconnection:
                    tcp_connection = [x.strip() for x in tcpconnection.split("-")]
                else:
                    tcp_connection = list(tcpconnection)

                peer_dict.update({'tcp_connection': tcp_connection})
                continue

            # State: Oper; Msgs sent/rcvd: 824/825; Downstream
            # State: Oper; Msgs sent/rcvd: 824/825; Downstream; Last TIB rev sent 4103
            m = p3.match(line)
            if m:
                group = m.groupdict()
                peer_dict.update({'state': group['state'].lower()})
                peer_dict.update({'msg_sent': int(group['msg_sent'])})
                peer_dict.update({'msg_rcvd': int(group['msg_rcvd'])})
                peer_dict.update({'downstream': True if 'downstream' in group['downstream'].lower() else False})
                if group['last_tib_rev_sent']:
                    peer_dict.update({'last_tib_rev_sent': int(group['last_tib_rev_sent'])})
                continue

            # Up time: 04:26:14
            m = p4.match(line)
            if m:
                group = m.groupdict()
                peer_dict.update({'uptime': group['up_time']})
                continue

            #  GigabitEthernet0/0/0, Src IP addr: 106.162.197.93
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ldp_source_dict = peer_dict.setdefault('ldp_source',{})
                ldp_source_dict.update({'interface': group['interface']})
                ldp_source_dict.update({'src_ip_address': group['src_ip_address']})
                continue

            # holdtime: 15000 ms, hello interval: 5000 ms
            m = p5_1.match(line)
            if m:
                group = m.groupdict()
                ldp_source_dict.update({'holdtime_ms': int(group['holdtime'])})
                ldp_source_dict.update({'hello_interval_ms': int(group['hello_interval'])})
                continue

            #  Addresses bound to peer LDP Ident:
            m = p6.match(line)
            if m:
                address_bound_flag = True
                continue

            #  106.162.197.252 27.93.202.49    106.162.197.101 113.146.190.254
            m = p7.match(line)
            if m:
                group = m.groupdict()
                address_bound_list = group['address_bound_peer_ldp'].split()
                if address_bound_flag:
                    if 'address_bound' not in peer_dict:
                        peer_dict.update({'address_bound': address_bound_list})
                    else:
                        peer_dict['address_bound'].extend(address_bound_list)
                continue

            # Peer holdtime: 180000 ms; KA interval: 60000 ms; Peer state: estab
            m = p8.match(line)
            if m:
                group = m.groupdict()
                peer_dict.update({'peer_holdtime_ms': int(group['peer_holdtime'])})
                peer_dict.update({'ka_interval_ms': int(group['ka_interval'])})
                peer_dict.update({'peer_state': group['peer_state']})
                continue

            # Password: not required, none, in use
            m = p9.match(line)
            if m:
                group = m.groupdict()
                peer_dict.update({'password': group['password']})
                continue

            # NSR: Not Ready
            m = p10.match(line)
            if m:
                group = m.groupdict()
                peer_dict.update({'nsr': group['nsr']})
                continue

            # Capabilities Sent:
            m = p11.match(line)
            if m:
                received_flag = False
                sent_flag = True
                temp_dict = peer_dict.setdefault('capabilities_sent', {})
                continue

            #   [ICCP (type 0x0405) MajVer 1 MinVer 0]
            m = p12.match(line)
            if m:
                group = m.groupdict()
                temp_dict.update({'iccp_type': group['type']})
                temp_dict.update({'maj_version': int(group['maj_ver'])})
                temp_dict.update({'min_version': int(group['min_ver'])})

                continue

            #   [Dynamic Announcement (0x0506)]
            m = p13.match(line)
            if m:
                group = m.groupdict()
                temp_dict.update({'dynamic_anouncement': group['dynamic_anouncement']})
                continue

            #   [mLDP Point-to-Multipoint (0x0508)]
            m = p14.match(line)
            if m:
                group = m.groupdict()
                temp_dict.update({'mldp_point_to_multipoint': group['mldp_point_to_multipoint']})
                continue

            #   [mLDP Multipoint-to-Multipoint (0x0509)]
            m = p15.match(line)
            if m:
                group = m.groupdict()
                temp_dict.update({'mldp_multipoint_to_multipoint': group['mldp_multipoint_to_multipoint']})
                continue

            #   [Typed Wildcard (0x050B)]
            m = p16.match(line)
            if m:
                group = m.groupdict()
                temp_dict.update({'typed_wildcard': group['typed_wildcard']})
                continue

            # Capabilities Received:
            m = p17.match(line)
            if m:
                received_flag = True
                sent_flag = False
                temp_dict = peer_dict.setdefault('capabilities_received', {})
                continue

            # [None]
            m = p18.match(line)
            if m:
                if received_flag:
                    peer_dict.pop('capabilities_received')
                if sent_flag:
                    peer_dict.pop('capabilities_sent')
                continue

        return result_dict


class ShowMplsLdpNeighborDetail(ShowMplsLdpNeighbor):
    """Parser for show mpls ldp neighbor detail,
                  show mpls ldp neighbor vrf <vrf> detail"""

    cli_command = ['show mpls ldp neighbor detail', 'show mpls ldp neighbor vrf {vrf} detail']

    def cli(self, vrf="", cmd ="",output=None):
        return super().cli(cmd=self.cli_command,vrf=vrf,output=output)