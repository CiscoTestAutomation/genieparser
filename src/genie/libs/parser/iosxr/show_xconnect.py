"""show_xconnect.py

show xsconnect parser class

  supported commands:
   *  show l2vpn xconnect
   *  show l2vpn xconnect brief
   *  show l2vpn xconnect detail
   *  show l2vpn xconnect mp2mp detail
"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                               Any, \
                                               Optional, \
                                               Or, \
                                               And, \
                                               Default, \
                                               Use

from genie.libs.parser.base import *
from genie.libs.parser.utils.common import Common


# ======================================
# Schema for 'show l2vpn xconnect brief'
# ======================================
class ShowL2VpnXconnectBriefSchema(MetaParser):
    '''Schema for:
        * show l2vpn xconnect brief
    '''

    schema = {
        Optional('total'):
            {'up': int,
            'down': int,
            'unr': int,
            },
        Optional('locally_switching'):
            {'like_to_like':
                {Any():
                    {'up': int,
                    'down': int,
                    'unr': int,
                    },
                },
            'total':
                {'up': int,
                'down': int,
                'unr': int,
                },
            },
        Optional('atom'):
            {'like_to_like':
                {Any():
                    {'up': int,
                    'down': int,
                    'unr': int,
                    },
                },
            'total':
                {'up': int,
                'down': int,
                'unr': int,
                },
            },
        }


# ======================================
# Parser for 'show l2vpn xconnect brief'
# ======================================
class ShowL2VpnXconnectBrief(ShowL2VpnXconnectBriefSchema):
    '''Parser for:
        * show l2vpn xconnect brief
    '''

    cli_command = 'show l2vpn xconnect brief'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init
        parsed_dict = {}

        # Locally Switching
        p1 = re.compile(r'^Locally Switching$')

        # AToM
        p2 = re.compile(r'^AToM$')

        # Like-to-Like                        UP       DOWN        UNR
        p3 = re.compile(r'^Like-to-Like.*$')

        #   Invalid AC                         0          0          1
        #   EFP/Invalid AC                     0          0          1
        #   EFP                                3          0          0
        #   Total                              3          0          2
        p4 = re.compile(r'^(?P<item>([a-zA-Z\-\/\s]+)) +(?P<up>(\d+))'
                         ' +(?P<down>(\d+)) +(?P<unr>(\d+))$')

        # Total: 0 UP, 0 DOWN, 0 UNRESOLVED
        p5 = re.compile(r'^Total: +(?P<up>(\d+)) +UP, +(?P<down>(\d+)) +DOWN,'
                         ' +(?P<unr>(\d+)) +UNRESOLVED$')

        for line in out.splitlines():
            line = line.strip()

            # Locally Switching
            m = p1.match(line)
            if m:
                sub_dict = parsed_dict.setdefault('locally_switching', {})
                continue

            # AToM
            m = p2.match(line)
            if m:
                sub_dict = parsed_dict.setdefault('atom', {})
                continue

            # Like-to-Like                        UP       DOWN        UNR
            m = p3.match(line)
            if m:
                ltl_parsed = True
                continue

            #   Invalid AC                         0          0          1
            #   EFP/Invalid AC                     0          0          1
            #   EFP                                3          0          0
            #   Total                              3          0          2
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ltl = group['item'].strip().lower().replace(" ", "_").\
                                                    replace("/", "_")
                if not ltl_parsed:
                    total_dict = sub_dict.setdefault(ltl, {})
                    total_dict['up'] = int(group['up'])
                    total_dict['down'] = int(group['down'])
                    total_dict['unr'] = int(group['unr'])
                else:
                    ltl_dict = sub_dict.setdefault('like_to_like', {}).\
                                        setdefault(ltl, {})
                    ltl_dict['up'] = int(group['up'])
                    ltl_dict['down'] = int(group['down'])
                    ltl_dict['unr'] = int(group['unr'])
                    if ltl == 'total':
                        ltl_parsed = False
                continue

            # Total: 0 UP, 0 DOWN, 0 UNRESOLVED
            m = p5.match(line)
            if m:
                group = m.groupdict()
                total_dict = parsed_dict.setdefault('total', {})
                for key, value in group.items():
                    total_dict[key] = int(value)
                continue

        return parsed_dict


# ===========================================================
# Schema for:
#     *'show l2vpn xconnect detail'
#     *'show l2vpn xconnect mp2mp detail'
# ===========================================================

class ShowL2vpnXconnectDetailSchema(MetaParser):
    schema = {
        'group': {
            Any(): {
                Optional('mp2mp'): {
                    Any(): {
                        'state': str,
                        'vpn_id': int,
                        'vpn_mtu': int,
                        'l2_encapsulation': str,
                        'auto_discovery': {
                            Any(): {
                                'state': str,
                                'event_name': str,
                                'route_distinguisher': str,
                            },
                        },
                        'import_route_targets': list,
                        'export_route_targets': list,
                        'signaling_protocol': {
                            Any(): {
                                'ce_range': int,
                            }
                        }
                    }
                },
                'xc': {
                    Any(): {
                        'state': str,
                        'interworking': str,
                        Optional('local_ce_id'): int,
                        Optional('remote_ce_id'): int,
                        Optional('discovery_state'): str,
                        Optional('monitor_session'): {
                            Any(): {
                                'state': str
                            }
                        },
                        Optional('ac'):{
                            Any(): {
                                'state': str,
                                Optional('type'): str,
                                Optional('num_ranges'): int,
                                Optional('rewrite_tags'): str,
                                Optional('mtu'): int,
                                Optional('xc_id'): str,
                                Optional('interworking'): str,
                                Optional('msti'): int,
                                Optional('statistics'): {
                                    'packet_totals': {
                                        Optional('receive'): int,
                                        Optional('send'): int
                                    },
                                    'byte_totals': {
                                        Optional('receive'): int,
                                        Optional('send'): int
                                    },
                                    Optional('drops'): {
                                        Optional('illegal_vlan'): int,
                                        Optional('illegal_length'): int,
                                    },
                                },
                                Optional('vlan_ranges'): list,
                            }
                        },
                        Optional('pw'): {
                            'neighbor': {
                                Any(): {
                                    'id': {
                                        Any(): {
                                            'state': str,
                                            Optional('pw_class'): str,
                                            Optional('xc_id'): str,
                                            Optional('encapsulation'): str,
                                            Optional('auto_discovered'): str,
                                            Optional('protocol'): str,
                                            Optional('source_address'): str,
                                            Optional('lsp'): str,
                                            Optional('type'): str,
                                            Optional('control_word'): str,
                                            Optional('interworking'): str,
                                            Optional('backup_disable_delay'): int,
                                            Optional('status_tlv'): str,
                                            Optional('sequencing'): str,
                                            Optional('mpls'): {
                                                Any(): {
                                                    'local': str,
                                                    'remote': str,
                                                    Optional('local_type'): list,
                                                    Optional('remote_type'): list,
                                                }
                                            },
                                            Optional('create_time'): str,
                                            Optional('last_time_status_changed'): str,
                                            Optional('statistics'): {
                                                'packet_totals': {
                                                    Optional('receive'): int,
                                                    Optional('send'): int
                                                },
                                                'byte_totals': {
                                                    Optional('receive'): int,
                                                    Optional('send'): int
                                                }
                                            },
                                        }
                                    }
                                }
                            }
                        },
                        Optional('evpn'): {
                            'neighbor': {
                                Any(): {
                                    'id': {
                                        Any(): {
                                            'state': str,
                                            'ac_id': int,
                                            'xc_id': str,
                                            'encapsulation': str,
                                            'source_address': str,
                                            'encap_type': str,
                                            'control_word': str,
                                            'lsp': str,
                                            Optional('status_tlv'): str,
                                            Optional('sequencing'): str,
                                            'evpn': {
                                                Any(): {
                                                    'local': str,
                                                    'remote': str,
                                                    Optional('local_type'): list,
                                                    Optional('remote_type'): list,
                                                }
                                            },
                                            'create_time': str,
                                            Optional('last_time_status_changed'): str,
                                            Optional('statistics'): {
                                                'packet_totals': {
                                                    Optional('receive'): int,
                                                    Optional('send'): int
                                                },
                                                'byte_totals': {
                                                    Optional('receive'): int,
                                                    Optional('send'): int
                                                }
                                            },
                                        }
                                    }
                                }
                            }
                        },
                        Optional('backup_pw'): {
                            'neighbor': {
                                Any(): {
                                    'id': {
                                        Any(): {
                                            'state': str,
                                            'pw_class': str,
                                            'xc_id': str,
                                            'encapsulation': str,
                                            Optional('auto_discovered'): str,
                                            'protocol': str,
                                            Optional('source_address'): str,
                                            Optional('lsp'): str,
                                            Optional('type'): str,
                                            Optional('control_word'): str,
                                            Optional('interworking'): str,
                                            Optional('backup_disable_delay'): int,
                                            Optional('status_tlv'): str,
                                            Optional('sequencing'): str,
                                            'mpls': {
                                                Any(): {
                                                    'local': str,
                                                    'remote': str,
                                                    Optional('local_type'): list,
                                                    Optional('remote_type'): list,
                                                }
                                            },
                                            Optional('create_time'): str,
                                            Optional('last_time_status_changed'): str,
                                            Optional('statistics'): {
                                                'packet_totals': {
                                                    Optional('receive'): int,
                                                    Optional('send'): int
                                                },
                                                'byte_totals': {
                                                    Optional('receive'): int,
                                                    Optional('send'): int
                                                }
                                            },
                                        }
                                    }
                                }
                            }
                        },
                    },
                },
            },
        },
    }

# ===========================================================
# Parser for:
#     *'show l2vpn xconnect detail'
# ===========================================================

class ShowL2vpnXconnectDetail(ShowL2vpnXconnectDetailSchema):
    """Parser for show l2vpn xconnect detail"""

    cli_command = 'show l2vpn xconnect detail'
    def cli(self, output=None):
        out = output if output else self.device.execute(self.cli_command)
        ret_dict = {}
        current_dict = None
        pw_backup = False
        interface_found = False
        label_found = False
        # Group siva_xc, XC siva_p2p, state is down; Interworking none
        p1 = re.compile(r'^Group +(?P<group>\S+), +XC +(?P<xc>\S+), +'
            'state +is +(?P<state>\S+); +Interworking +(?P<interworking>\S+)')

        # Monitor-Session: pw-span-test, state is configured
        p2 = re.compile(r'^Monitor\-Session: +(?P<monitor_session>\S+)'
            ', +state +is +(?P<state>\S+)$')

        # AC: GigabitEthernet0/4/0/1, state is up
        # AC: GigabitEthernet0/4/0/1, state is down (Admin)
        p3 = re.compile(r'^AC: +(?P<ac>\S+), +state +is +(?P<state>[\S ]+)$')

        # Type Ethernet
        p4 = re.compile(r'^Type +(?P<type>\S+)$')

        # MTU 1500; XC ID 0x5000001; interworking none; MSTi 0
        # MTU 1500; XC ID 0x2000013; interworking none
        p5 = re.compile(r'^MTU +(?P<mtu>\d+); +XC +ID +(?P<xc_id>\S+); +'
            'interworking +(?P<interworking>\S+)(; +MSTi +(?P<msti>\d+))?$')

        # packet totals: send 98
        p6 = re.compile(r'^packet +totals: +send +(?P<send>\d+)$')
        
        # packet totals: receive 98
        p6_1 = re.compile(r'^packet +totals: +receive +(?P<receive>\d+)$')

        # packets: received 3, sent 0
        p6_2 = re.compile(r'^packets: +received +(?P<received>\d+), +sent +(?P<send>\d+)')

        # byte totals: send 20798
        p7 = re.compile(r'^byte +totals: +send +(?P<send>\d+)$')

        # byte totals: send 20798
        p7_1 = re.compile(r'^byte +totals: +receive +(?P<receive>\d+)$')

        # packets: received 3, sent 0
        p7_2 = re.compile(r'^bytes: +received +(?P<received>\d+), +sent +(?P<send>\d+)')

        # drops: illegal VLAN 0, illegal length 0
        p7_3 = re.compile(r'^drops: +illegal +VLAN +(?P<illegal_vlan>\d+), +illegal +'
            'length +(?P<illegal_length>\d+)$')

        # PW: neighbor 10.1.1.1, PW ID 1, state is down ( local ready )
        p8 = re.compile(r'^PW: +neighbor +(?P<neighbor>\S+), +PW +ID +'
            '(?P<id>\d+), state +is +(?P<state>[\S ]+)$')
        
        # EVPN: neighbor 10.154.219.82, PW ID: evi 10200, ac-id 30200, state is up ( established )
        p8_1 = re.compile(r'^EVPN: +neighbor +(?P<neighbor>\S+), +PW +ID: +'
            '(?P<pw_id>[\S ]+), +ac-id +(?P<ac_id>\d+), +state +is +(?P<state>[\S ]+)$')
        
        # PW class not set, XC ID 0x5000001
        p9 = re.compile(r'^PW +class +(?P<pw_class>[\S ]+), +XC +ID +(?P<xc_id>\S+)$')

        # Encapsulation MPLS, protocol LDP
        p10 = re.compile(r'^Encapsulation +(?P<encapsulation>\S+)(, +Auto-discovered +'
            '\((?P<auto_discovered>\S+)\))?, +protocol +(?P<protocol>\S+)$')

        # PW type Ethernet, control word enabled, interworking none
        p11 = re.compile(r'^PW +type +(?P<type>\S+), +control +word +(?P<control_word>\S+)'
            ', +interworking +(?P<interworking>\S+)$')

        # PW backup disable delay 0 sec
        p12 = re.compile(r'^PW +backup +disable +delay +(?P<backup_disable_delay>\d+) +sec$')

        # Sequencing not set
        p13 = re.compile(r'^Sequencing +(?P<sequencing>[\S ]+)$')

        # PW Status TLV in use
        p13_1 = re.compile(r'^PW +Status +TLV +(?P<status_tlv>[\S ]+)$')

        # MPLS         Local                          Remote
        # EVPN         Local                          Remote
        p14 = re.compile(r'^(?P<label_name>MPLS|EVPN) +Local +Remote$')

        # Label        30005                          unknown
        # Group ID     0x5000300                      0x0
        # VCCV CV type 0x2                            0x0
        # Avoid show commands: show l2vpn xconnect detail
        # Avoid Date and Time: Wed Sep 25 20:09:36.362 UTC
        p15 = re.compile(r'^(?!(show +l2vpn))[\S ]+$')

        # Create time: 20/11/2007 21:45:06 (00:53:31 ago)
        p16 = re.compile(r'^Create +time: +(?P<create_time>[\S ]+)$')

        # Last time status changed: 20/11/2007 22:38:14 (00:00:23 ago)
        p17 = re.compile(r'^Last +time +status +changed: +(?P<last_time_status_changed>[\S ]+)$')

        # Backup PW:
        p18 = re.compile(r'^Backup +PW:$')

        # ------------ ------------------------------ -----------------------------
        p19 = re.compile(r'^-+ +-+ +-+$')

        # (control word)                 (control word)  
        p20 = re.compile(r'^\([\S ]+\)$')

        # Backup for neighbor 10.1.1.1 PW ID 1 ( active )
        p21 = re.compile(r'^Backup( +PW)? +for +neighbor +\S+ +PW +ID +\d+( +\( +\w+ +\))?$')

        # Avoid Device name : Device#
        # Avoid Date and Time: Wed Sep 25 20:09:36.362 UTC
        p22 = re.compile(r'^(\w+ +\w+ \d+ +\S+ +\w+)|(\S+\#)$')

        # Local CE ID: 1, Remote CE ID: 2, Discovery State: Advertised
        p23 = re.compile(r'^Local +CE +ID: +(?P<local_ce_id>\d+), +Remote +CE +ID: +'
            '(?P<remote_ce_id>\d+), Discovery +State: +(?P<state>\S+)$')

        # Type VLAN; Num Ranges: 1
        p24 = re.compile(r'^Type +(?P<type>\S+); +Num +Ranges: +(?P<num_ranges>\d+)$')

        # VLAN ranges: [1, 1]
        p25 = re.compile(r'^VLAN +ranges: +\[(?P<vlan_ranges>[\S ]+)\]$')

        # Group gr1, MP2MP mp1, state: up
        p26 = re.compile(r'^Group +(?P<group_name>\S+), +MP2MP +(?P<mp2mp>\S+), +state: +(?P<state>\S+)$')

        # VPN ID: 100
        p27 = re.compile(r'^VPN +ID: +(?P<vpn_id>\d+)$')

        # VPN MTU: 1500
        p28 = re.compile(r'^VPN +MTU: +(?P<vpn_mtu>\d+)$')

        # L2 Encapsulation: VLAN
        p29 = re.compile(r'^L2 +Encapsulation: +(?P<l2_encapsulation>\S+)$')

        # Auto Discovery: BGP, state is Advertised (Service Connected)
        p30 = re.compile(r'^Auto +Discovery: +(?P<auto_discovery>\S+), +state +is +'
            '(?P<state>\S+) +\((?P<event_name>[\S ]+)\)$')

        # Route Distinguisher: (auto) 10.36.3.3:32770
        p31 = re.compile(r'^Route +Distinguisher: +(?P<route_distinguisher>[\S ]+)$')

        # Import Route Targets:
        p32 = re.compile(r'^Import +Route +Targets:$')

        # Export Route Targets:
        p33 = re.compile(r'^Export +Route +Targets:$')

        # 10.16.2.2:100
        p34 = re.compile(r'^(?P<route_target>[\d\.:]+)$')

        # Signaling protocol:BGP
        p35 = re.compile(r'^Signaling +protocol: *(?P<signaling_protocol>\S+)$')

        # CE Range:10
        p36 = re.compile(r'^CE +Range: *(?P<ce_range>\d+)$')

        # Statistics:
        p37 = re.compile(r'^Statistics:$')

        # Wed Oct  2 14:36:55.184 EDT
        p38 = re.compile(r'^[Wed|Thu|Fri|Sat|Sun|Mon|Tue]+ +'
                        '[Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec]+ +'
                        '\d{1,2} +\d{1,2}:\d{1,2}:\d{1,2}[\.]\d{1,3} +[A-Z]{3}')

        # Rewrite Tags: [] 
        p39 = re.compile(r'^Rewrite +Tags: +\[(?P<rewrite_tags>[\S ]+)?\]$')

        # XC ID 0xc0000001
        p40 = re.compile(r'^XC +ID +(?P<xc_id>\S+)$')

        # Encapsulation MPLS
        p41 = re.compile(r'^Encapsulation +(?P<encapsulation>\S+)$')

        # Source address 10.154.219.88
        p42 = re.compile(r'^Source +address +(?P<source_address>\S+)$')

        # Encap type Ethernet, control word enabled
        p43 = re.compile(r'^Encap +type +(?P<encap_type>\S+), +control +'
                            'word +(?P<control_word>\S+)$')

        # LSP : Up
        p44 = re.compile(r'^LSP +: +(?P<lsp>\S+)$')

        for line in out.splitlines():
            original_line = line
            line = line.strip()
            
            # Avoid show commands : show l2vpn xconnect detail
            # Avoid Date and Time: Wed Sep 25 20:09:36.362 UTC
            m = p22.match(line)
            if m:
                continue
            
            # Statistics:
            m = p37.match(line)
            if m:
                continue
            
            # Wed Oct  2 14:36:55.184 EDT
            m = p38.match(line)
            if m:
                continue

            # Rewrite Tags: []
            m = p39.match(line)
            if m:
                group = m.groupdict()
                current_dict.setdefault('rewrite_tags', '')
                current_dict.update({k:v.strip() for k, v in group.items() if v is not None})
                continue

            # Group siva_xc, XC siva_p2p, state is down; Interworking none
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_name = group['group']
                xc = group['xc']
                state = group['state']
                interworking = group['interworking']

                xc_dict = ret_dict.setdefault('group', {}). \
                    setdefault(group_name, {}). \
                    setdefault('xc', {}). \
                    setdefault(xc, {})

                xc_dict.update({'state': state})
                xc_dict.update({'interworking': interworking})
                label_found = False
                continue

            # Group gr1, MP2MP mp1, state: up
            m = p26.match(line)
            if m:
                group = m.groupdict()
                group_name = group['group_name']
                mp2mp = group['mp2mp']
                state = group['state']

                mp2mp_dict = ret_dict.setdefault('group', {}). \
                    setdefault(group_name, {}). \
                    setdefault('mp2mp', {}). \
                    setdefault(mp2mp, {})

                mp2mp_dict.update({'state': state})
                label_found = False
                continue
            
            # Monitor-Session: pw-span-test, state is configured
            m = p2.match(line)
            if m:
                group = m.groupdict()
                monitor_session = group['monitor_session']
                state = group['state']
                monitor_session_dict = xc_dict.setdefault('monitor_session', {}). \
                    setdefault(monitor_session, {})
                monitor_session_dict.update({'state': state})
                continue

            # AC: GigabitEthernet0/4/0/1, state is up 
            # AC: GigabitEthernet0/4/0/1, state is down (Admin)
            m = p3.match(line)
            if m:
                pw_backup = False
                group = m.groupdict()
                ac = group['ac']
                state = group['state']
                current_dict = xc_dict.setdefault('ac', {}). \
                    setdefault(ac, {})
                current_dict.update({'state': state})
                continue
            
            # Type Ethernet
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ac_type = group['type']
                current_dict.update({'type': ac_type})
                continue

            # MTU 1500; XC ID 0x5000001; interworking none; MSTi 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                mtu = int(group['mtu'])
                xc_id = group['xc_id']
                interworking = group['interworking']
                current_dict.update({'mtu': mtu})
                current_dict.update({'xc_id': xc_id})
                current_dict.update({'interworking': interworking})
                if group['msti']:
                    msti = int(group['msti'])
                    current_dict.update({'msti': msti})
                continue
            
            # packet totals: send 98
            m = p6.match(line)
            if m:
                group = m.groupdict()
                send = int(group['send'])
                current_dict.setdefault('statistics', {}). \
                    setdefault('packet_totals', {}). \
                    update({'send': send})
                continue

            # packet totals: receive 98
            m = p6_1.match(line)
            if m:
                group = m.groupdict()
                receive = int(group['receive'])
                current_dict.setdefault('statistics', {}). \
                    setdefault('packet_totals', {}). \
                    update({'receive': receive})
                continue
            
            # packets: received 3, sent 0
            m = p6_2.match(line)
            if m:
                group = m.groupdict()
                receive = int(group['received'])
                send = int(group['send'])
                packet_dict = current_dict.setdefault('statistics', {}). \
                    setdefault('packet_totals', {})
                packet_dict.update({'receive': receive})
                packet_dict.update({'send': send})
                continue

            # byte totals: send 98
            m = p7.match(line)
            if m:
                group = m.groupdict()
                send = int(group['send'])
                current_dict.setdefault('statistics', {}). \
                    setdefault('byte_totals', {}). \
                    update({'send': send})
                continue
            
            # byte totals: receive 98
            m = p7_1.match(line)
            if m:
                group = m.groupdict()
                receive = int(group['receive'])
                current_dict.setdefault('statistics', {}). \
                    setdefault('byte_totals', {}). \
                    update({'receive': receive})
                continue

            # packets: received 3, sent 0
            m = p7_2.match(line)
            if m:
                group = m.groupdict()
                receive = int(group['received'])
                send = int(group['send'])
                packet_dict = current_dict.setdefault('statistics', {}). \
                    setdefault('byte_totals', {})
                packet_dict.update({'receive': receive})
                packet_dict.update({'send': send})
                continue

            # drops: illegal VLAN 0, illegal length 0
            m = p7_3.match(line)
            if m:
                group = m.groupdict()
                vlan = int(group['illegal_vlan'])
                illegal_length = int(group['illegal_length'])
                statistics_dict = current_dict.setdefault('statistics', {})
                drop_dict = statistics_dict.setdefault('drops', {})
                drop_dict.update({'illegal_vlan': vlan})
                drop_dict.update({'illegal_length': illegal_length})
                continue

            # PW: neighbor 10.1.1.1, PW ID 1, state is down ( local ready )
            m = p8.match(line)
            if m:
                group = m.groupdict()
                neighbor = group['neighbor']
                pw_id = int(group['id'])
                state = group['state']
                if not pw_backup:
                    current_dict = xc_dict.setdefault('pw', {})
                
                current_dict = current_dict.setdefault('neighbor', {}). \
                        setdefault(neighbor, {}). \
                        setdefault('id', {}). \
                        setdefault(pw_id, {})

                current_dict.update({'state': state})
                continue

            # EVPN: neighbor 10.154.219.82, PW ID: evi 10200, ac-id 30200, state is up ( established )
            m = p8_1.match(line)
            if m:
                group = m.groupdict()
                neighbor = group['neighbor']
                pw_id = group['pw_id']
                ac_id = int(group['ac_id'])
                state = group['state']
                current_dict = xc_dict.setdefault('evpn', {})
                
                current_dict = current_dict.setdefault('neighbor', {}). \
                        setdefault(neighbor, {}). \
                        setdefault('id', {}). \
                        setdefault(pw_id, {})

                current_dict.update({'state': state})
                current_dict.update({'ac_id': ac_id})
                continue
            
            # PW class not set, XC ID 0x5000001
            m = p9.match(line)
            if m:
                group = m.groupdict()
                xc_id = group['xc_id']
                pw_class = group['pw_class']
                current_dict.update({'pw_class': pw_class})
                current_dict.update({'xc_id': xc_id})
                continue

            # Encapsulation MPLS, protocol LDP
            m = p10.match(line)
            if m:
                group = m.groupdict()
                encapsulation = group['encapsulation']
                protocol = group['protocol']
                current_dict.update({'encapsulation': encapsulation})
                current_dict.update({'protocol': protocol})
                continue
            
            # PW type Ethernet, control word enabled, interworking none
            m = p11.match(line)
            if m:
                group = m.groupdict()
                pw_type = group['type']
                control_word = group['control_word']
                interworking = group['interworking']
                current_dict.update({'type': pw_type})
                current_dict.update({'control_word': control_word})
                current_dict.update({'interworking': interworking})
                continue

            # PW backup disable delay 0 sec
            m = p12.match(line)
            if m:
                group = m.groupdict()
                backup_disable_delay = int(group['backup_disable_delay'])
                current_dict.update({'backup_disable_delay': backup_disable_delay})
                continue

            # Sequencing not set
            m = p13.match(line)
            if m:
                group = m.groupdict()
                sequencing = group['sequencing']
                current_dict.update({'sequencing': sequencing})
                continue

            # PW Status TLV in use
            m = p13_1.match(line)
            if m:
                group = m.groupdict()
                status_tlv = group['status_tlv']
                current_dict.update({'status_tlv': sequencing})
                continue

            # MPLS         Local                          Remote
            # EVPN         Local                          Remote
            m = p14.match(line)
            if m:
                group = m.groupdict()
                label_name = group['label_name'].lower()
                continue
            
            # Create time: 20/11/2007 21:45:06 (00:53:31 ago)
            m = p16.match(line)
            if m:
                group = m.groupdict()
                create_time = group['create_time']
                current_dict.update({'create_time': create_time})
                continue
            
            # Last time status changed: 20/11/2007 22:38:14 (00:00:23 ago)
            m = p17.match(line)
            if m:
                group = m.groupdict()
                last_time_status_changed = group['last_time_status_changed']
                current_dict.update({'last_time_status_changed': last_time_status_changed})
                continue
            
            # Backup PW:
            m = p18.match(line)
            if m:
                current_dict = xc_dict.setdefault('backup_pw', {})
                pw_backup = True
                interface_found = False
                continue
            
            # ------------ ------------------------------ -----------------------------
            m = p19.match(line)
            if m:
                mpls_pairs = {}
                for m in re.finditer(r'-+', original_line):
                    mpls_pairs.update({m.start(): m.end() + 1})
                label_found = not label_found
                continue

            # Backup for neighbor 10.1.1.1 PW ID 1 ( active )
            m = p21.match(line)
            if m:
                continue
            
            # Local CE ID: 1, Remote CE ID: 2, Discovery State: Advertised
            m = p23.match(line)
            if m:
                group = m.groupdict()
                local_ce_id = int(group['local_ce_id'])
                remote_ce_id = int(group['remote_ce_id'])
                discovery_state = group['state']
                xc_dict.update({'local_ce_id': local_ce_id})
                xc_dict.update({'remote_ce_id': remote_ce_id})
                xc_dict.update({'discovery_state': discovery_state})
                continue
            
            # Type VLAN; Num Ranges: 1
            m = p24.match(line)
            if m:
                group = m.groupdict()
                type_name = group['type']
                num_ranges =  int(group['num_ranges'])
                current_dict.update({'type': type_name})
                current_dict.update({'num_ranges': num_ranges})
                continue

            # VLAN ranges: [1, 1]
            m = p25.match(line)
            if m:
                group = m.groupdict()
                vlan_ranges = group['vlan_ranges'].replace(' ', '').split(',')
                current_dict.update({'vlan_ranges': vlan_ranges})
                continue
            
            # VPN ID: 100
            m = p27.match(line)
            if m:
                group = m.groupdict()
                vpn_id = int(group['vpn_id'])
                mp2mp_dict.update({'vpn_id': vpn_id})
                continue

            # VPN MTU: 1500
            m = p28.match(line)
            if m:
                group = m.groupdict()
                vpn_mtu = int(group['vpn_mtu'])
                mp2mp_dict.update({'vpn_mtu': vpn_mtu})
                continue

            # L2 Encapsulation: VLAN
            # p29 = re.compile(r'^L2 +Encapsulation: +(?P<l2_encapsulation>\S+)$')
            m = p29.match(line)
            if m:
                group = m.groupdict()
                l2_encapsulation = group['l2_encapsulation']
                mp2mp_dict.update({'l2_encapsulation': l2_encapsulation})
                continue

            # Auto Discovery: BGP, state is Advertised (Service Connected)
            m = p30.match(line)
            if m:
                group = m.groupdict()
                auto_discovery = group['auto_discovery']
                state = group['state']
                event_name = group['event_name']
                auto_discovery_dict = mp2mp_dict.setdefault('auto_discovery', {}). \
                    setdefault(auto_discovery, {})
                auto_discovery_dict.update({'state': state})
                auto_discovery_dict.update({'event_name': event_name})
                continue

            # Route Distinguisher: (auto) 10.36.3.3:32770
            # p31 = re.compile(r'^Route +Distinguisher: +(?P<route_distinguisher>[\S ]+)$')
            m = p31.match(line)
            if m:
                group = m.groupdict()
                route_distinguisher = group['route_distinguisher']
                auto_discovery_dict.update({'route_distinguisher': route_distinguisher})
                continue

            # Import Route Targets:
            m = p32.match(line)
            if m:
                route_target_list = mp2mp_dict.setdefault('import_route_targets', [])
                continue

            # Export Route Targets:
            m = p33.match(line)
            if m:
                route_target_list = mp2mp_dict.setdefault('export_route_targets', [])
                continue

            # 10.16.2.2:100
            m = p34.match(line)
            if m:
                group = m.groupdict()
                route_target = group['route_target']
                route_target_list.append(route_target)
                continue

            # Signaling protocol:BGP
            m = p35.match(line)
            if m:
                group = m.groupdict()
                signaling_protocol = group['signaling_protocol']
                signaling_protocol_dict = mp2mp_dict.setdefault('signaling_protocol', {}). \
                    setdefault(signaling_protocol, {})
                continue

            # CE Range:10
            m = p36.match(line)
            if m:
                group = m.groupdict()
                ce_range = int(group['ce_range'])
                signaling_protocol_dict.update({'ce_range': ce_range})
                continue

            # XC ID 0xc0000001
            m = p40.match(line)
            if m:
                group = m.groupdict()
                current_dict.update({'xc_id': group['xc_id']})
                continue

            # Encapsulation MPLS
            m = p41.match(line)
            if m:
                group = m.groupdict()
                current_dict.update({'encapsulation': group['encapsulation']})
                continue

            # Source address 10.154.219.88
            m = p42.match(line)
            if m:
                group = m.groupdict()
                current_dict.update({'source_address': group['source_address']})
                continue

            # Encap type Ethernet, control word enabled
            m = p43.match(line)
            if m:
                group = m.groupdict()
                current_dict.update({'encap_type': group['encap_type']})
                current_dict.update({'control_word': group['control_word']})
                continue

            # LSP : Up
            m = p44.match(line)
            if m:
                group = m.groupdict()
                current_dict.update({'lsp': group['lsp']})
                continue
            
            #              (LSP ping verification)               
            #                                             (none)
            #              (control word)                 (control word)
            #              (control word) 
            # Label        30005                          unknown
            # Group ID     0x5000300                      0x0
            # VCCV CV type 0x2                            0x0
            m = p15.match(line)
            if m:
                if label_found:
                    mpls_items = list(mpls_pairs.items())

                    # Last index of MPLS label section
                    mpls_end_index = mpls_items[0][1]

                    # Start and end index of Local section
                    local_start_index = mpls_items[1][0]
                    local_end_index = mpls_items[1][1]
                    
                    # Start and end index of Remote section
                    remote_start_index = mpls_items[2][0]
                    remote_end_index = mpls_items[2][1]

                    mpls_value = original_line[:mpls_end_index]
                    mpls_value = (original_line[:mpls_end_index].strip().
                                    replace('-', '_').
                                    replace(' ', '_').
                                    lower())
                    
                    local_value = (original_line[local_start_index:local_end_index])
                    local_value = local_value.replace('(',''). \
                                        replace(')', ''). \
                                        strip()

                    remote_value = (original_line[remote_start_index:remote_end_index])
                    remote_value = remote_value.replace('(',''). \
                                    replace(')', ''). \
                                    strip()
                    # Any thing between () brackets will be added to Local or Remote based on position
                    if ')' not in line:
                        if mpls_value == 'interface':
                            mpls_dict = current_dict.setdefault(label_name, {}). \
                                    setdefault('monitor_interface' if interface_found else mpls_value, {})
                            if not interface_found:
                                interface_found = True
                        else:
                            mpls_dict = current_dict.setdefault(label_name, {}). \
                                setdefault(mpls_value, {})
                        mpls_dict.update({'local': local_value})
                        mpls_dict.update({'remote': remote_value})
                    else:
                        local_type = mpls_dict.get('local_type', [])
                        remote_type = mpls_dict.get('remote_type', [])
                        if local_value:
                            local_type.append(local_value)
                        if remote_value:
                            remote_type.append(remote_value)
                        mpls_dict.update({'local_type': local_type})
                        mpls_dict.update({'remote_type': remote_type})
                continue
        return ret_dict

# ===========================================================
# Parser for:
#     *'show l2vpn xconnect mp2mp detail'
# ===========================================================

class ShowL2vpnXconnectMp2mpDetail(ShowL2vpnXconnectDetail):
    """Parser class for 'show l2vpn xconnect mp2mp detail' CLI."""

    cli_command = 'show l2vpn xconnect mp2mp detail'
    
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        return super().cli(output=out)

class ShowL2vpnXconnectSchema(MetaParser):
    """Schema for show l2vpn xconnect"""
    schema = {
        'groups': {
            Any(): {
                'name': {
                    Any(): {
                        'status': str,
                        'segment1': {
                            Any(): {
                                'status': str,
                                'segment2': {
                                    Any(): {
                                        'status': str,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


class ShowL2vpnXconnect(ShowL2vpnXconnectSchema):
    """Parser for show l2vpn xconnect """

    cli_command = 'show l2vpn xconnect'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}
        flag_group = True
        m3_1 = None

        # L2TPV3_V4_XC_GRP
        #           L2TPV3_P2P_1
        p1 = re.compile(r'^(?P<group>[\w\-]+)$')

        # SB = Standby, SR = Standby Ready, (PP) = Partially Programmed
        p1_1 = re.compile(r'^SB = Standby, SR = Standby Ready, \(PP\) = Partially Programmed$')

        # BL-PE-BG   G1-1-1-23-311
        p1_2 = re.compile(r'^(?P<group>\S+) +(?P<name>\S+)$')

        #               1000     DN   Gi0/0/0/5.1000    UP   10.4.1.206       1000   DN
        p2 = re.compile(r'^(?P<name>[a-zA-Z0-9]+) '
                        r'+(?P<status_group>(UP|DN|AD|UR|SB|SR|\(PP\))) '
                        r'+(?P<segment_1>.*?) ' 
                        r'+(?P<status_seg1>(UP|DN|AD|UR|SB|SR|\(PP\))) '
                        r'+(?P<segment_2>[\S ]+) '
                        r'+(?P<status_seg2>(UP|DN|AD|UR|SB|SR|\(PP\)))$')

        #                        UP   Gi0/2/0/1.2            UP       10.154.26.26     100    UP  
        p3 = re.compile(r'^(?P<status_group>(UP|DN|AD|UR|SB|SR|\(PP\))) '
                        r'+(?P<segment_1>.*?) ' 
                        r'+(?P<status_seg1>(UP|DN|AD|UR|SB|SR|\(PP\))) '
                        r'+(?P<segment_2>[\S ]+) '
                        r'+(?P<status_seg2>(UP|DN|AD|UR|SB|SR|\(PP\)))$')

        #                        UP   Gi0/2/0/1.2            UP       10.154.26.26     100  
        p3_1 = re.compile(r'^(?P<status_group>(UP|DN|AD|UR|SB|SR|\(PP\))) '
                        r'+(?P<segment_1>.*?) ' 
                        r'+(?P<status_seg1>(UP|DN|AD|UR|SB|SR|\(PP\))) '
                        r'+(?P<segment_2>[\S ]+)$')
        
        # T-0-5-0-0  UR   Te0/5/0/0              UR       10.154.219.75    4293089094
        p3_2 = re.compile(r'^(?P<name>\S+) +(?P<status_group>(UP|DN|AD|UR|SB|SR|\(PP\))) +'
                r'(?P<segment_1>.*?) +(?P<status_seg1>(UP|DN|AD|UR|SB|SR|\(PP\))) +'
                r'(?P<segment_2>[\S ]+)$')
        
        # CRS-CRS    T-0-5-0-8  UP   Te0/5/0/8              UP       10.19.196.51   9651100
        p3_3 = re.compile(r'^(?P<group>\S+) +(?P<name>\S+) +'
                r'(?P<status_group>(UP|DN|AD|UR|SB|SR|\(PP\))) +(?P<segment_1>.*?) +'
                r'(?P<status_seg1>(UP|DN|AD|UR|SB|SR|\(PP\))) +(?P<segment_2>[\S ]+)$')

        # vpws       vpws       UR   Te0/2/1/0              UR       EVPN 302,302,0.0.0.0   DN
        p3_4 = re.compile(r'^(?P<group>\S+) +(?P<name>\S+) +'
                r'(?P<status_group>(UP|DN|AD|UR|SB|SR|\(PP\))) +(?P<segment_1>.*?) +'
                r'(?P<status_seg1>(UP|DN|AD|UR|SB|SR|\(PP\))) +(?P<segment_2>[\S ]+)'
                r' +(?P<status_segment2>(UP|DN|AD|UR|SB|SR|\(PP\)))$')

        #                                                             UP  
        p4 = re.compile(r'^(?P<status_segment2>(UP|DN|AD|UR|SB|SR|\(PP\)))$')

        # UP       10.19.196.10   1152   DN
        p5 = re.compile(r'^(?P<status_seg1>(UP|DN|AD|UR|SB|SR|\(PP\)))'
                r' +(?P<segment_2>[\S ]+) +(?P<status_seg2>(UP|DN|AD|UR|SB|SR|\(PP\)))$')

        # UR   10.154.219.75    2015030201
        p6 = re.compile(r'^(?P<status_group>(UP|DN|AD|UR|SB|SR|\(PP\))) +(?P<segment_1>[\S ]+)$')

        # T-0-4-0-2  UR   10.154.219.98    4293089094
        p7 = re.compile(r'^(?P<name>\S+) +(?P<status_group>(UP|DN|AD|UR|SB|SR|\(PP\))) +'
                r'(?P<segment_1>[\S ]+)$')

        for line in out.splitlines():
            line = line.strip()
            
            if '--------' in line:
                continue

            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                segment2_dict['status'] = str(group['status_segment2'])
                flag_group = True
                continue

            m = p1.match(line)
            if m:
                if flag_group:
                    group = m.groupdict()
                    group_dict = ret_dict.setdefault('groups', {}) \
                        .setdefault(str(group['group']), {})
                    flag_group = False
                else:
                    group = m.groupdict()
                    name_dict = group_dict.setdefault('name', {}) \
                        .setdefault(str(group['group']), {})
                    flag_group = True
                continue
            
            m = p1_1.match(line)
            if m:
                continue
            
            # BL-PE-BG   G1-1-1-23-311
            m = p1_2.match(line)
            if m:
                group = m.groupdict()
                group_dict = ret_dict.setdefault('groups', {}). \
                    setdefault(group['group'], {})
                name_dict = group_dict.setdefault('name', {}) \
                        .setdefault(group['name'], {})
                continue

            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                name_dict = group_dict.setdefault('name', {}) \
                    .setdefault(str(group['name']), {})
                flag_group = True
            
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()

            if m2 or m3:
                name_dict['status'] = str(group['status_group'])
                segment1_dict = name_dict.setdefault('segment1',{}) \
                    .setdefault(Common.convert_intf_name(group['segment_1']), {})
                segment1_dict['status'] = str(group['status_seg1'])
                segment2_dict = segment1_dict.setdefault('segment2', {}) \
                    .setdefault(str(group['segment_2'].strip()), {})
                segment2_dict['status'] = str(group['status_seg2'])
                continue

            m3_1 = p3_1.match(line)
            if m3_1:
                group = m3_1.groupdict()
                name_dict['status'] = str(group['status_group'])
                segment1_dict = name_dict.setdefault('segment1',{}) \
                    .setdefault(Common.convert_intf_name(group['segment_1']), {})
                segment1_dict['status'] = str(group['status_seg1'])
                segment2_dict = segment1_dict.setdefault('segment2', {}) \
                    .setdefault(str(group['segment_2'].strip()), {})
            
            # T-0-5-0-0  UR   Te0/5/0/0              UR       10.154.219.75    4293089094
            m = p3_2.match(line)
            if m:
                group = m.groupdict()
                name_dict = group_dict.setdefault('name', {}) \
                        .setdefault(group['name'], {})
                name_dict['status'] = str(group['status_group'])
                segment1_dict = name_dict.setdefault('segment1',{}) \
                    .setdefault(Common.convert_intf_name(group['segment_1']), {})
                segment1_dict['status'] = str(group['status_seg1'])
                segment2_dict = segment1_dict.setdefault('segment2', {}) \
                    .setdefault(str(group['segment_2'].strip()), {})
                continue

            # vpws       vpws       UR   Te0/2/1/0              UR       EVPN 302,302,0.0.0.0   DN
            m = p3_4.match(line)
            if m:
                group = m.groupdict()
                group_dict = ret_dict.setdefault('groups', {}). \
                    setdefault(group['group'], {})
                name_dict = group_dict.setdefault('name', {}) \
                        .setdefault(group['name'], {})
                name_dict['status'] = str(group['status_group'])
                segment1_dict = name_dict.setdefault('segment1',{}) \
                    .setdefault(Common.convert_intf_name(group['segment_1']), {})
                segment1_dict['status'] = str(group['status_seg1'])
                segment2_dict = segment1_dict.setdefault('segment2', {}) \
                    .setdefault(str(group['segment_2'].strip()), {})
                segment2_dict['status'] = str(group['status_segment2'])
                continue

            # CRS-CRS    T-0-5-0-8  UP   Te0/5/0/8              UP       10.19.196.51   9651100
            m = p3_3.match(line)
            if m:
                group = m.groupdict()
                group_dict = ret_dict.setdefault('groups', {}). \
                    setdefault(group['group'], {})
                name_dict = group_dict.setdefault('name', {}) \
                        .setdefault(group['name'], {})
                name_dict['status'] = str(group['status_group'])
                segment1_dict = name_dict.setdefault('segment1',{}) \
                    .setdefault(Common.convert_intf_name(group['segment_1']), {})
                segment1_dict['status'] = str(group['status_seg1'])
                segment2_dict = segment1_dict.setdefault('segment2', {}) \
                    .setdefault(str(group['segment_2'].strip()), {})
                continue

            # UR       Nonexistent            UR
            m = p5.match(line)
            if m:
                group = m.groupdict()
                segment1_dict['status'] = str(group['status_seg1'])
                segment2_dict = segment1_dict.setdefault('segment2', {}) \
                    .setdefault(str(group['segment_2'].strip()), {})
                segment2_dict['status'] = str(group['status_seg2'])
                continue
            
            # UR   10.154.219.75    2015030201
            m = p6.match(line)
            if m:
                group = m.groupdict()
                name_dict['status'] = str(group['status_group'])
                segment1_dict = name_dict.setdefault('segment1',{}) \
                    .setdefault(Common.convert_intf_name(group['segment_1'].strip()), {})
                continue
            
            # T-0-4-0-2  UR   10.154.219.98    4293089094
            m = p7.match(line)
            if m:
                group = m.groupdict()
                name_dict = group_dict.setdefault('name', {}) \
                        .setdefault(group['name'], {})
                name_dict['status'] = str(group['status_group'])
                segment1_dict = name_dict.setdefault('segment1',{}) \
                    .setdefault(Common.convert_intf_name(group['segment_1'].strip()), {})
                continue
        return ret_dict

"""Schema for 'show l2vpn xconnect summary'"""
class ShowL2vpnXconnectSummarySchema(MetaParser):
    schema = {
        'number_of_groups': {
            'total': int,
        },
        'number_of_xconnects': {
            'total': int,
            'up': int,
            'down': int,
            'unresolved': int,
            'partially_programmed': int,
            'ac_pw': int,
            'ac_ac': int,
            'pw_pw': int,
            'monitor_session_pw': int,
        },
        'number_of_admin_down_segments': {
            'total': int
        },
        'number_of_mp2mp_xconnects': {
            'total': int,
            'up': int,
            'down': int,
            'advertised': int,
            'non_advertised': int,
        },
        'number_of_ce_connections': {
            'total': int,
            'advertised': int,
            'non_advertised': int
        },
        'backup_pw': {
            'configured': int,
            'up': int,
            'down': int,
            'admin_down': int,
            'unresolved': int,
            'standby': int,
            'standby_ready': int,
        },
        'backup_interface': {
            'configured': int,
            'up': int,
            'down': int,
            'admin_down': int,
            'unresolved': int,
            'standby': int,
        }
    }

class ShowL2vpnXconnectSummary(ShowL2vpnXconnectSummarySchema):
    """Parser for show l2vpn xconnect summary"""
    
    cli_command = 'show l2vpn xconnect summary'
    def cli(self, output=None):
        '''parsing mechanism: cli
        '''

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        ret_dict = {}

        # Number of groups: 0
        p1 = re.compile(r'^Number +of +groups: +(?P<number_of_groups>\d+)$')
        
        # Number of xconnects: 0
        p2 = re.compile(r'^Number +of +xconnects: +(?P<number_of_xconnects>\d+)$')

        # Up: 0  Down: 0  Unresolved: 0 Partially-programmed: 0
        p3 = re.compile(r'^Up: (?P<up>\d+) +Down: +(?P<down>\d+) +Unresolved: +'
            '(?P<unresolved>\d+) +Partially-programmed: +(?P<partially_programmed>\d+)$')

        # AC-PW: 0  AC-AC: 0  PW-PW: 0 Monitor-Session-PW: 0
        p4 = re.compile(r'^AC-PW: +(?P<ac_pw>\d+) +AC-AC: +(?P<ac_ac>\d+) +PW-PW: +'
            '(?P<pw_pw>\d+) +Monitor-Session-PW: +(?P<monitor_session_pw>\d+)$')

        # Number of Admin Down segments: 0
        p5 = re.compile(r'^Number +of +Admin +Down +segments: +'
            '(?P<number_of_admin_down_segments>\d+)$')

        # Number of MP2MP xconnects: 0
        p6 = re.compile(r'^Number +of +MP2MP +xconnects: +(?P<number_of_mp2mp_xconnects>\d+)$')
        
        # Up 0 Down 0
        p7 = re.compile(r'^Up +(?P<up>\d+) +Down +(?P<down>\d+)$')

        # Advertised: 0 Non-Advertised: 0
        p8 = re.compile(r'^Advertised: +(?P<advertised>\d+) +Non-Advertised: +'
            '(?P<non_advertised>\d+)$')

        # Number of CE Connections: 0
        p9 = re.compile(r'^Number +of +CE +Connections: +(?P<number_of_ce_connections>\d+)$')

        # Backup PW:
        p10 = re.compile(r'^Backup +PW:$')

        # Backup Interface: 
        p11 = re.compile(r'^Backup +Interface:$')
        
        # Configured   : 0
        # UP           : 0
        # Down         : 0
        # Admin Down   : 0
        # Unresolved   : 0
        # Standby      : 0
        # Standby Ready: 0
        p12 = re.compile(r'^(?P<key>[\S ]+): +(?P<value>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Number of groups: 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                number_of_groups = int(group['number_of_groups'])
                number_of_groups_dict = ret_dict.setdefault('number_of_groups', {})
                number_of_groups_dict.update({'total': number_of_groups})
                continue
            
            # # Number of xconnects: 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                number_of_xconnects = int(group['number_of_xconnects'])
                number_of_xconnects_dict = ret_dict.setdefault('number_of_xconnects', {})
                number_of_xconnects_dict.update({'total': number_of_xconnects})
                continue
            
            # Up: 0  Down: 0  Unresolved: 0 Partially-programmed: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                number_of_xconnects_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue
            
            # AC-PW: 0  AC-AC: 0  PW-PW: 0 Monitor-Session-PW: 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                number_of_xconnects_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue
            
            # Number of Admin Down segments: 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                number_of_admin_down_segments = int(group['number_of_admin_down_segments'])
                number_of_admin_down_segments_dict = ret_dict.\
                    setdefault('number_of_admin_down_segments', {})
                number_of_admin_down_segments_dict.\
                    update({'total': number_of_admin_down_segments})
                continue
            
            # Number of MP2MP xconnects: 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                number_of_mp2mp_xconnects = int(group['number_of_mp2mp_xconnects'])
                xconnects_dict = ret_dict.setdefault('number_of_mp2mp_xconnects', {})
                xconnects_dict.update({'total': number_of_mp2mp_xconnects})
                continue
            
            # Up 0 Down 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                xconnects_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue
            
            # Advertised: 0 Non-Advertised: 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                xconnects_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue
            
            # Number of CE Connections: 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                number_of_ce_connections = int(group['number_of_ce_connections'])
                xconnects_dict = ret_dict.setdefault('number_of_ce_connections', {})
                xconnects_dict.update({'total': number_of_ce_connections})
                continue
            
            # Backup PW:
            m = p10.match(line)
            if m:
                current_dict = ret_dict.setdefault('backup_pw', {})
                continue
            
            # Backup Interface:
            m = p11.match(line)
            if m:
                current_dict = ret_dict.setdefault('backup_interface', {})
                continue

            # Configured   : 0
            # UP           : 0
            # Down         : 0
            # Admin Down   : 0
            # Unresolved   : 0
            # Standby      : 0
            # Standby Ready: 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].strip().lower().replace(' ', '_')
                value = int(group['value'])
                current_dict.update({key: value})
                continue
        
        return ret_dict