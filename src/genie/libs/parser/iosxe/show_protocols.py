''' show_protocols.py

IOSXE parsers for the following show commands:
    * show ip protocols
'''

# Python
import re
import xmltodict
from netaddr import IPAddress

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional
from genie.libs.parser.utils.common import Common


# ==============================
# Schema for 'show ip protocols'
# ==============================
class ShowIpProtocolsSchema(MetaParser):

    ''' Schema for "show ip protocols" '''

    schema = {
        'protocols': {
            Optional('rip'): {
                'vrf': {
                    Any(): {
                        'address_family': {
                            Any(): {
                                Optional('instance'): {
                                    Any(): {
                                        'distance': int,
                                        'maximum_paths': int,
                                        Optional('output_delay'): int,
                                        'send_version': Or(int, str),
                                        'receive_version': Or(int, str),
                                        Optional('automatic_network_summarization_in_effect'): bool,
                                        'outgoing_update_filterlist': {
                                            'outgoing_update_filterlist': str,
                                            Optional('interfaces'): {
                                                Any(): {
                                                    'filter': str,
                                                    'per_user': bool,
                                                    'default': str,
                                                }
                                            },
                                        },
                                        'incoming_update_filterlist': {
                                            'incoming_update_filterlist': str,
                                            Optional('interfaces'): {
                                                Any(): {
                                                    'filter': str,
                                                    'per_user': bool,
                                                    'default': str,
                                                }
                                            },
                                        },
                                        Optional('incoming_route_metric'): {
                                            'added': str,
                                            'list': str,
                                        },
                                        Optional('network'): list,
                                        Optional('default_redistribution_metric'): int,
                                        'redistribute': {
                                            Any(): {
                                                Optional(Any()): {
                                                    Optional('metric'): int,
                                                    Optional('route_policy'): int,
                                                    Optional('route_type'): str,
                                                },
                                                Optional('metric'): int,
                                                Optional('route_policy'): int,
                                            }
                                        },
                                        Optional('timers'): {
                                            'update_interval': int,
                                            'next_update': int,
                                            'invalid_interval': int,
                                            'holddown_interval': int,
                                            'flush_interval': int,
                                        },
                                        Optional('interfaces'): {
                                            Any(): {
                                                Optional('neighbors'): {
                                                    Any(): {
                                                        Optional('address'): str
                                                    }
                                                },
                                                Optional('summary_address'): {
                                                    Any(): {
                                                        Optional('metric'): str
                                                    }
                                                },
                                                Optional('filtered_per_user'): int,
                                                Optional('default_set'): bool,
                                                Optional('passive'): bool,
                                                'send_version': str,
                                                'receive_version': str,
                                                'triggered_rip': str,
                                                'key_chain': str,
                                            }
                                        },
                                        Optional('neighbors'): {
                                            Any(): {
                                                'last_update': str, 
                                                'distance': int
                                            }
                                        },
                                    }
                                }
                            }
                        }
                    }
                }
            },
            Optional('eigrp'): {
                'protocol_under_dev': bool
            },
            Optional('ospf'): {
                'vrf': {
                    Any(): {
                        'address_family': {
                            Any(): {
                                'instance': {
                                    Any(): {
                                        'spf_control': {
                                            'paths': int
                                        },
                                        Optional('network'): {
                                            Any(): {
                                                'netmask': str,
                                                'area': str,
                                            }
                                        },
                                        'preference': {
                                            'single_value': {
                                                'all': int
                                            },
                                            Optional('multi_values'): {
                                                'granularity': {
                                                    'detail': {
                                                        'intra_area': int,
                                                        'inter_area': int,
                                                    },
                                                    Optional('coarse'): {
                                                        'internal': int
                                                    },
                                                },
                                                'external': int,
                                            },
                                        },
                                        'router_id': str,
                                        Optional('outgoing_filter_list'): str,
                                        Optional('incoming_filter_list'): str,
                                        'total_areas': int,
                                        'total_stub_area': int,
                                        'total_normal_area': int,
                                        'total_nssa_area': int,
                                        Optional('passive_interfaces'): list,
                                        Optional('routing_information_sources'): {
                                            'gateway': {
                                                Any(): {
                                                    'distance': int, 
                                                    'last_update': str
                                                }
                                            }
                                        },
                                        Optional('areas'): {
                                            Any(): {
                                                Optional('configured_interfaces'): list
                                            }
                                        },
                                    }
                                }
                            }
                        }
                    }
                }
            },
            Optional('application'): {
                'outgoing_filter_list': str,
                'incoming_filter_list': str,
                'maximum_path': int,
                'preference': {
                    'single_value': {
                        'all': int
                    }
                },
                'update_frequency': int,
                'invalid': int,
                'holddown': int,
                'flushed': int,
            },
            Optional('bgp'): {
                'instance': {
                    'default': {
                        'bgp_id': int,
                        'vrf': {
                            'default': {
                                'address_family': {
                                    'ipv4': {
                                        Optional('outgoing_filter_list'): str,
                                        Optional('incoming_filter_list'): str,
                                        'igp_sync': bool,
                                        'automatic_route_summarization': bool,
                                        Optional('maximum_path'): int,
                                        Optional('preference'): {
                                            'multi_values': {
                                                'external': int,
                                                'local': int,
                                                'internal': int,
                                            }
                                        },
                                        Optional('neighbors'): {
                                            Any(): {
                                                Optional('route_map'): str,
                                            }
                                        },
                                        Optional('routing_information_sources'): {
                                            Any(): {
                                                'neighbor_id': str,
                                                'distance': int,
                                                'last_update': str,
                                            }
                                        },
                                        Optional('timers'): {
                                            'update_interval': int,
                                            'next_update': int,
                                        },
                                    }
                                }
                            }
                        },
                    }
                }
            },
            Optional('isis'): {
                'vrf': {
                    Any(): {
                        'address_family': {
                            Any(): {
                                'instance': {
                                    Any(): {
                                        'outgoing_filter_list': str,
                                        'incoming_filter_list': str,
                                        Optional('redistributing'): str,
                                        Optional('address_summarization'): list,
                                        Optional('maximum_path'): int,
                                        'preference': {
                                            'single_value': {
                                                'all': int
                                            }
                                        },
                                        Optional('configured_interfaces'): list,
                                        Optional('passive_interfaces'): list,
                                        Optional('routing_information_sources'): {
                                            'gateway': {
                                                Any(): {
                                                    'distance': int, 
                                                    'last_update': str
                                                }
                                            }
                                        },
                                    }
                                }
                            }
                        }
                    }
                }
            },
        }
    }

# ==============================
# Parser for 'show ip protocols'
# ==============================
class ShowIpProtocols(ShowIpProtocolsSchema):

    ''' Parser for "show ip protocols" '''

    cli_command = ['show ip protocols',
                  'show ip protocols vrf {vrf}']
    exclude = ['last_update', ' network' , 'next_update']

    def cli(self, vrf="" ,cmd="", output=None):
        if output is None:
            if not cmd :
                if vrf:
                    cmd = self.cli_command[1].format(vrf=vrf)
                else:
                    cmd = self.cli_command[0]
            # get output from device
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}

        if not vrf:
            vrf = "default"
        protocol = None
        # Routing for Networks:
        routing_networks = False
        routing_network_intfs = []
        # Routing on Interfaces Configured Explicitly
        routing_on_interfaces = False
        routing_on_interfaces_intfs = []
        # Routing Information Sources:
        routing_information = False
        routing_info_gateways = []
        # Passive Interface(s):
        passive_interfaces = False
        passive_intfs = []

        # Routing Protocol is "ospf 1"
        # Routing Protocol is "application"
        # Routing Protocol is "bgp 100"
        # Routing Protocol is "isis"
        # Routing Protocol is "isis banana"
        # Routing Protocol is "eigrp 1"
        p1 = re.compile(r"^Routing +Protocol +is"
                        r" +\"(?P<protocol>(ospf|bgp|isis|eigrp|application|rip))"
                        r"(?: *(?P<pid>(\S+)))?\"$")

        # Outgoing update filter list for all interfaces is not set
        # Incoming update filter list for all interfaces is not set
        p2 = re.compile(r"^(?P<dir>(Outgoing|Incoming)) +update +filter +list"
                        r" +for +all +interfaces +is +(?P<state>([a-zA-Z\s]+))$")

        # Router ID 10.4.1.1
        p3 = re.compile(r"^Router +ID +(?P<router_id>(\S+))$")

        # Number of areas in this router is 1. 1 normal 0 stub 0 nssa
        p4 = re.compile(r"^Number +of +areas +in +this +router +is"
                        r" +(?P<areas>(\d+)). +(?P<normal>(\d+)) +normal"
                        r" +(?P<stub>(\d+)) +stub +(?P<nssa>(\d+)) +nssa$")

        # Maximum path: 4
        p5 = re.compile(r"^Maximum +path: +(?P<max>(\d+))$")

        # Routing for Networks:
        p6_1 = re.compile(r"^Routing +for +Networks:$")

        # Routing on Interfaces Configured Explicitly (Area 0):
        p6_2 = re.compile(r"^Routing +on +Interfaces +Configured +Explicitly"
                          r" +\(Area +(?P<area>[\d\.]+)\)\:$")

        # Routing Information Sources:
        p6_3 = re.compile(r"^Routing +Information +Sources:$")

        # Passive Interface(s):
        p6_4 = re.compile(r"^Passive +Interface\(s\):$")

        # Address Summarization:
        p6_5 = re.compile(r"^Address +Summarization:$")

        # Loopback0
        # GigabitEthernet2
        # GigabitEthernet1
        # TenGigabitEthernet0/0/26
        # Serial0
        # VoIP-Null0
        p7 = re.compile(r"^(?P<interface>(Lo\S*|Gi\S*|Ten\S*|\S*(SL|VL)\S*|Se\S*|VoIP\S*))$")

        # Gateway         Distance      Last Update
        # 10.36.3.3            110      07:33:00
        # 10.16.2.2            110      07:33:00
        # 10.64.4.4            110      00:19:15
        p8 = re.compile(r"^(?P<gateway>([0-9\.]+)) +(?P<distance>(\d+))"
                         " +(?P<last_update>([a-zA-Z0-9\:\.]+))$")

        # Distance: (default is 110)
        p9 = re.compile(r"^Distance: +\(default +is +(?P<num>(\d+))\)$")

        # Distance: intra-area 112 inter-area 113 external 114
        p10 = re.compile(r"^Distance: +intra-area +(?P<intra>(\d+)) +inter-area"
                          " +(?P<inter>(\d+)) +external +(?P<external>(\d+))$")

        # Sending updates every 0 seconds
        p11 = re.compile(r"^Sending +updates +every +(?P<update>(\d+)) +seconds$")

        # Invalid after 0 seconds, hold down 0, flushed after 0
        p12 = re.compile(r"^Invalid +after +(?P<invalid>(\d+)) +seconds, +hold"
                          " +down +(?P<holddown>(\d+)), +flushed +after"
                          " +(?P<flushed>(\d+))$")

        # IGP synchronization is disabled
        p13 = re.compile(r"^IGP +synchronization +is +(?P<igp>(enabled|disabled))$")

        # Automatic route summarization is disabled
        p14 = re.compile(r"^Automatic +route +summarization +is"
                          " +(?P<route>(enabled|disabled))$")

        # Distance: external 20 internal 200 local 200
        # Distance:external 20 internal 200 local 200
        p15 = re.compile(r"^Distance: *external +(?P<external>(\d+)) +internal"
                          " +(?P<internal>(\d+)) +local +(?P<local>(\d+))$")


        # Redistributing: isis banana
        p16 = re.compile(r"^Redistributing: +(?P<redistributing>([a-zA-Z\_\s]+))$")

        # 10.0.0.84 0.0.0.3 area 11
        # 10.0.0.88 0.0.0.3 area 11
        # 192.168.0.10 0.0.0.0 area 11
        p17 = re.compile(r'(?P<address>[\d\.]+)\s+(?P<mask>[\d\.]+)\s+area\s+(?P<area>[\d\.]+)')

        passive_interface_flag = False
        routing_network_flag = False
        neighbors_flag = False

        # Routing Protocol is "rip"
        p100 = re.compile(r'^\s*Routing Protocol +is +\"(?P<protocol>[\w]+)\"$')

        # Output delay 50 milliseconds between packets
        p102 = re.compile(r'^\s*Output +delay +(?P<output_delay>[\d]+) +milliseconds +between +packets$')

        # Outgoing update filter list for all interfaces is not set
        # Outgoing update filter list for all interfaces is 150
        p103 = re.compile(
            r'^\s*Outgoing +update +filter +list +for all +interfaces +is +(?P<outgoing_update_filterlist>[\S\s]+)$')

        # Incoming update filter list for all interfaces is not set
        # Incoming update filter list for all interfaces is 100
        p104 = re.compile(
            r'^\s*Incoming +update +filter +list +for all +interfaces +is +(?P<incoming_update_filterlist>[\S\s]+)$')

        # GigabitEthernet3.100 filtered by 130 (per-user), default is not set
        p104_1 = re.compile(
            r'^\s*(?P<interface>\S+) +filtered +by +(?P<filter>\d+)( +\((?P<per_user>\S+)\))?,'
            ' +default +is +(?P<default>[\w\s]+)$')
        # Incoming routes will have 10 added to metric if on list 21
        p105 = re.compile(r'^\s*Incoming +routes +will +have +(?P<added>\S+) +added +to +metric'
                          ' +if +on +list +(?P<list>\S+)$')

        # Sending updates every 10 seconds, next due in 8 seconds
        p106 = re.compile(
            r'^\s*Sending +updates every +(?P<update_interval>\d+) +seconds, +next +due +in (?P<next_update>\d+) +(seconds|sec)$')

        # Invalid after 21 seconds, hold down 22, flushed after 23
        p107 = re.compile(
            r'^\s*Invalid +after +(?P<invalid_interval>\d+) +seconds, +hold +down +(?P<holddown_interval>\d+)'
            ', +flushed +after +(?P<flush_interval>\d+)$')

        # Default redistribution metric is 3
        p108 = re.compile(r'^\s*Default +redistribution +metric +is +(?P<default_redistribution_metric>\d+)$')

        # Redistributing: connected, static, rip
        # Redistributing:connected, static
        p109 = re.compile(r'^\s*Redistributing: *(?P<Redistributing>[\w\,\s]+)$')

        # Neighbor(s):
        p110 = re.compile(r'^\s*Neighbor\(s\):$')

        # 172.16.121.101                                        ACCEPT_SCI_RICHEMONT
        # 192.168.1.176                                         INTERNET_EDGE_IN
        # 192.168.1.177                                         INTERNET_EDGE_IN
        # 192.168.0.9
        p111 = re.compile(r'(?P<neighbor>[\d\.]+)\s*(?P<route_map>[\w]+)?')

        # Default version control: send version 2, receive version 2
        p112 = re.compile(r'^\s*Default +version +control: +send +version +(?P<send_version>\d+)'
                          ', receive version +(?P<receive_version>\d+)$')

        # Default version control: send version 1, receive any version
        p112_1 = re.compile(r'^\s*Default +version +control: +send +version +(?P<send_version>\d+)'
                          ', receive +(?P<receive_version>\w+) version$')

        #   Interface                           Send  Recv  Triggered RIP  Key-chain
        #   GigabitEthernet3.100                2     2          No        1
        #   GigabitEthernet3.100                1 2   2          No        none
        p113 = re.compile(r'^\s*(?P<interface>[\S]+) +(?P<send>\d( \d)?)'
                          ' +(?P<receive>\d( \d)?)?'
                          ' +(?P<triggered_rip>\S+) +(?P<key_chain>\S+)$')

        # Automatic network summarization is not in effect
        # Automatic network summarization is in effect
        p114 = re.compile(
            r'^\s*Automatic +network +summarization +is( +(?P<automatic_network_summarization>\S+))? +in +effect$')

        # Address Summarization:
        p115 = re.compile(r'^\s*Address +Summarization:$')

        #   172.16.0.0/17 for GigabitEthernet3.100
        p116 = re.compile(r'^\s*(?P<prefix>[\d\.\/]+) +for +(?P<interface>[\w\.]+)$')

        # Maximum path: 4
        p117 = re.compile(r'^\s*Maximum +path: +(?P<maximum_path>\d+)$')

        # Routing for Networks:
        p118 = re.compile(r'^\s*Routing +for +Networks:$')

        #   10.0.0.0
        p119 = re.compile(r'^\s*(?P<network>[\d\.]+)$')

        # Passive Interface(s):
        p120 = re.compile(r'^\s*Passive +Interface\(s\):$')

        #   GigabitEthernet2.100
        p121 = re.compile(r'^\s*(?P<passive_interface>[\w\.]+)$')

        # Routing Information Sources:
        p122 = re.compile(r'^\s*Routing +Information +Sources:$')

        #   Gateway         Distance      Last Update
        #   10.1.2.2             120      00:00:04
        p123 = re.compile(r'^\s*(?P<gateway>[\d\.]+) +(?P<distance>\d+) +(?P<last_update>[\w\:]+)$')

        # Distance: (default is 120)
        p124 = re.compile(r'^\s*Distance: +\(default +is +(?P<distance>\d+)\)$')

        network_list = []

        for line in out.splitlines():
            line = line.strip()

            # Routing Protocol is "ospf 1"
            # Routing Protocol is "application"
            # Routing Protocol is "bgp 100"
            # Routing Protocol is "isis banana"
            # Routing Protocol is "eigrp 1"
            m = p1.match(line)
            if m:
                group = m.groupdict()
                protocol = group['protocol']
                if group['pid']:
                    instance = str(m.groupdict()['pid'])

                # Set protocol dict
                protocol_dict = ret_dict.setdefault('protocols', {}). \
                    setdefault(protocol, {})

                if protocol == 'ospf':
                    # Get VRF information based on OSPF instance
                    out = self.device.execute("show running-config | section "
                                              "router ospf {}".format(instance))
                    # Parse for VRF
                    for line in out.splitlines():
                        line = line.strip()
                        # router ospf 1
                        # router ospf 2 vrf VRF1
                        p = re.search('router +ospf +(?P<instance>(\S+))'
                                      '(?: +vrf +(?P<vrf>(\S+)))?', line)
                        if p:
                            p_instance = str(p.groupdict()['instance'])
                            if p_instance == instance:
                                if p.groupdict()['vrf']:
                                    vrf = str(p.groupdict()['vrf'])
                                    break
                                else:
                                    vrf = 'default'
                                    break

                    # Set ospf_dict
                    ospf_dict = protocol_dict.setdefault('vrf', {}). \
                        setdefault(vrf, {}). \
                        setdefault('address_family', {}). \
                        setdefault('ipv4', {}). \
                        setdefault('instance', {}). \
                        setdefault(instance, {})
                elif protocol == 'bgp':
                    instance_dict = protocol_dict.setdefault('instance', {}). \
                        setdefault('default', {})
                    instance_dict['bgp_id'] = int(group['pid'])
                    # Set bgp_dict
                    bgp_dict = instance_dict.setdefault('vrf', {}). \
                        setdefault('default', {}). \
                        setdefault('address_family', {}). \
                        setdefault('ipv4', {})
                elif protocol == 'isis':
                    # Set isis_dict
                    if not group['pid']:
                        instance = 'default'
                    if not vrf:
                        vrf = "default"
                    isis_dict = protocol_dict.setdefault('vrf', {}). \
                        setdefault(vrf, {}). \
                        setdefault('address_family', {}). \
                        setdefault('ipv4', {}). \
                        setdefault('instance', {}). \
                        setdefault(instance, {})
                elif protocol == 'application':
                    application_dict = protocol_dict
                elif protocol == 'eigrp':
                    protocol_dict['protocol_under_dev'] = True
                    eigrp_dict = protocol_dict
                elif protocol == 'rip':
                    address_family = 'ipv4'
                    rip_dict = ret_dict.setdefault('protocols', {}).\
                                            setdefault('rip', {}).\
                                            setdefault('vrf',{}).\
                                            setdefault(vrf, {}).\
                                            setdefault('address_family', {}). \
                                            setdefault(address_family, {}).\
                                            setdefault('instance', {}).\
                                            setdefault(protocol, {})
                    continue

            if protocol == 'rip':
                # Output delay 50 milliseconds between packets
                m = p102.match(line)
                if m:
                    group = m.groupdict()
                    rip_dict.update({'output_delay': int(group['output_delay'])})
                    continue

                # Outgoing update filter list for all interfaces is not set
                # Outgoing update filter list for all interfaces is 150
                m = p103.match(line)
                if m:
                    outgoing_flag = True
                    incoming_flag = False
                    group = m.groupdict()
                    outgoing_dict = rip_dict.setdefault('outgoing_update_filterlist', {})
                    outgoing_dict.update({'outgoing_update_filterlist': group['outgoing_update_filterlist']})
                    continue

                # Incoming update filter list for all interfaces is 100
                m = p104.match(line)
                if m:
                    incoming_flag = True
                    outgoing_flag = False
                    group = m.groupdict()
                    incoming_dict = rip_dict.setdefault('incoming_update_filterlist', {})
                    incoming_dict.update({k: v for k, v in group.items() if v})
                    continue

                # GigabitEthernet3.100 filtered by 130 (per-user), default is not set
                m = p104_1.match(line)
                if m:
                    if outgoing_flag:
                        temp_dict = outgoing_dict
                    if incoming_flag:
                        temp_dict = incoming_dict

                    group = m.groupdict()
                    interface_out_dict = temp_dict.setdefault('interfaces', {}).setdefault(group['interface'],
                                                                                           {})
                    interface_out_dict.update({"filter": group['filter']})
                    if group['per_user']:
                        if 'per-user' in group['per_user']:
                            per_user = True
                        else:
                            per_user = False
                    else:
                        per_user = False

                    interface_out_dict.update({"per_user": per_user})
                    interface_out_dict.update({"default": group['default']})
                    continue

                # Incoming routes will have 10 added to metric if on list 21
                m = p105.match(line)
                if m:
                    group = m.groupdict()
                    incoming_route_dict = rip_dict.setdefault('incoming_route_metric', {})
                    incoming_route_dict.update({k: v for k, v in group.items() if v})
                    continue

                # Sending updates every 10 seconds, next due in 8 seconds
                m = p106.match(line)
                if m:
                    group = m.groupdict()
                    timers_dict = rip_dict.setdefault('timers', {})
                    timers_dict.update({'update_interval': int(group['update_interval'])})
                    timers_dict.update({'next_update': int(group['next_update'])})
                    continue

                # Invalid after 21 seconds, hold down 22, flushed after 23
                m = p107.match(line)
                if m:
                    group = m.groupdict()
                    if 'timers' not in rip_dict:
                        timers_dict = rip_dict.setdefault('timers', {})
                    timers_dict.update({'invalid_interval': int(group['invalid_interval'])})
                    timers_dict.update({'holddown_interval': int(group['holddown_interval'])})
                    timers_dict.update({'flush_interval': int(group['flush_interval'])})
                    continue

                # Default redistribution metric is 3
                m = p108.match(line)
                if m:
                    group = m.groupdict()
                    rip_dict.update(
                        {'default_redistribution_metric': int(group['default_redistribution_metric'])})
                    continue

                # Redistributing: connected, static, rip
                m = p109.match(line)
                if m:
                    group = m.groupdict()
                    redistributes = group['Redistributing'].split(',')
                    redistribute_dict = rip_dict.setdefault('redistribute', {})
                    for key in redistributes:
                        redistribute_dict.setdefault(key.strip(), {})
                    continue

                m = p112.match(line)
                if m:
                    group = m.groupdict()
                    rip_dict.update({k: int(v) for k, v in group.items() if v})
                    continue

                m = p112_1.match(line)
                if m:
                    group = m.groupdict()
                    rip_dict.update({k: v for k, v in group.items() if v})
                    continue

                # Automatic network summarization is not in effect
                # Automatic network summarization is in effect
                m = p114.match(line)
                if m:
                    group = m.groupdict()
                    if group['automatic_network_summarization']:
                        automatic_network_summarization = False
                    else:
                        automatic_network_summarization = True
                    rip_dict.update(
                        {'automatic_network_summarization_in_effect': automatic_network_summarization})
                    continue

                # Interface                           Send  Recv  Triggered RIP  Key-chain
                #   GigabitEthernet3.100                2     2          No        1
                m = p113.match(line)
                if m:
                    group = m.groupdict()
                    interface_dict = rip_dict.setdefault('interfaces', {}).setdefault(group['interface'], {})
                    send = group['send']
                    receive = group['receive']

                    interface_dict.update({'send_version': send})
                    interface_dict.update({'receive_version': receive})
                    interface_dict.update({'triggered_rip': group['triggered_rip'].lower()})
                    interface_dict.update({'key_chain': group['key_chain']})
                    continue

                # 172.16.0.0/17 for GigabitEthernet3.100
                m = p116.match(line)
                if m:
                    group = m.groupdict()
                    summary_dict = interface_dict.setdefault('summary_address', {})
                    summary_dict.setdefault(group['prefix'], {})
                    continue

                # Maximum path: 4
                m = p117.match(line)
                if m:
                    group = m.groupdict()
                    rip_dict.update({'maximum_paths': int(group['maximum_path'])})
                    continue

                # Routing for Networks:
                m = p118.match(line)
                if m:
                    routing_network_flag = True
                    continue

                # 10.0.0.0
                m = p119.match(line)
                if m:
                    if routing_network_flag:
                        group = m.groupdict()
                        network_list.append(group['network'])
                        rip_dict.update({'network': list(set(network_list))})
                    continue

                # Passive Interface(s):
                m = p120.match(line)
                if m:
                    passive_interface_flag = True
                    routing_network_flag = False
                    continue

                # GigabitEthernet2.100
                m = p121.match(line)
                if m:
                    if passive_interface_flag == True:
                        group = m.groupdict()
                        interface_dict.update({'passive': True})
                    continue

                # Routing Information Sources:
                m = p122.match(line)
                if m:
                    passive_interface_flag = False
                    routing_network_flag = False
                    continue

                # Gateway         Distance      Last Update
                #   10.1.2.2             120      00:00:04
                m = p123.match(line)
                if m:
                    group = m.groupdict()
                    neighbor_dict = rip_dict.setdefault('neighbors', {}).setdefault(group['gateway'], {})
                    neighbor_dict.update({'last_update': group['last_update']})
                    neighbor_dict.update({'distance': int(group['distance'])})
                    continue

                # Distance: (default is 120)
                m = p124.match(line)
                if m:
                    group = m.groupdict()
                    rip_dict.update({'distance': int(group['distance'])})
                    continue
            else:
                # Outgoing update filter list for all interfaces is not set
                # Incoming update filter list for all interfaces is not set
                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    if protocol == 'ospf':
                        pdict = ospf_dict
                    elif protocol == 'isis':
                        pdict = isis_dict
                    elif protocol == 'application':
                        pdict = application_dict
                    elif protocol == 'bgp':
                        pdict = bgp_dict
                    else:
                        continue
                    direction = str(group['dir']).lower() + '_' + 'filter_list'
                    pdict[direction] = str(group['state']).lower()
                    continue

                # Router ID 10.4.1.1
                m = p3.match(line)
                if m:
                    ospf_dict['router_id'] = str(m.groupdict()['router_id'])
                    continue

                # Number of areas in this router is 1. 1 normal 0 stub 0 nssa
                m = p4.match(line)
                if m:
                    group = m.groupdict()
                    ospf_dict['total_areas'] = int(group['areas'])
                    ospf_dict['total_normal_area'] = int(group['normal'])
                    ospf_dict['total_stub_area'] = int(group['stub'])
                    ospf_dict['total_nssa_area'] = int(group['nssa'])
                    continue

                # Maximum path: 4
                m = p5.match(line)
                if m:
                    group = m.groupdict()
                    if protocol == 'ospf':
                        if 'spf_control' not in ospf_dict:
                            ospf_dict['spf_control'] = {}
                        ospf_dict['spf_control']['paths'] = int(group['max'])
                    elif protocol == 'application':
                        application_dict['maximum_path'] = int(group['max'])
                    elif protocol == 'bgp':
                        bgp_dict['maximum_path'] = int(group['max'])
                    elif protocol == 'isis':
                        isis_dict['maximum_path'] = int(group['max'])
                    continue

                # Routing for Networks:
                m = p6_1.match(line)
                if m:
                    # Routing for Networks:
                    routing_networks = True
                    routing_network_intfs = []
                    # Routing on Interfaces Configured Explicitly
                    routing_on_interfaces = False
                    routing_on_interfaces_intfs = []
                    # Routing Information Sources:
                    routing_information = False
                    routing_info_gateways = []
                    # Passive Interface(s):
                    passive_interfaces = False
                    passive_intfs = []
                    # Address Summarization:
                    address_summarization = False
                    address_summarization_intfs = []
                    continue

                # Routing on Interfaces Configured Explicitly (Area 0):
                m = p6_2.match(line)
                if m:
                    area = str(IPAddress(str(m.groupdict()['area'])))
                    ospf_area_dict = ospf_dict.setdefault('areas', {}). \
                        setdefault(area, {})
                    # Routing for Networks:
                    routing_networks = False
                    routing_network_intfs = []
                    # Routing on Interfaces Configured Explicitly
                    routing_on_interfaces = True
                    routing_on_interfaces_intfs = []
                    # Routing Information Sources:
                    routing_information = False
                    routing_info_gateways = []
                    # Passive Interface(s):
                    passive_interfaces = False
                    passive_intfs = []
                    # Address Summarization:
                    address_summarization = False
                    address_summarization_intfs = []
                    continue

                # Routing Information Sources:
                m = p6_3.match(line)
                if m:
                    # Routing for Networks:
                    routing_networks = False
                    routing_network_intfs = []
                    # Routing on Interfaces Configured Explicitly
                    routing_on_interfaces = False
                    routing_on_interfaces_intfs = []
                    # Routing Information Sources:
                    routing_information = True
                    routing_info_gateways = []
                    # Passive Interface(s):
                    passive_interfaces = False
                    passive_intfs = []
                    # Address Summarization:
                    address_summarization = False
                    address_summarization_intfs = []
                    continue

                # Passive Interface(s):
                m = p6_4.match(line)
                if m:
                    # Routing for Networks:
                    routing_networks = False
                    routing_network_intfs = []
                    # Routing on Interfaces Configured Explicitly
                    routing_on_interfaces = False
                    routing_on_interfaces_intfs = []
                    # Routing Information Sources:
                    routing_information = False
                    routing_info_gateways = []
                    # Passive Interface(s):
                    passive_interfaces = True
                    passive_intfs = []
                    # Address Summarization:
                    address_summarization = False
                    address_summarization_intfs = []
                    continue

                # Address Summarization:
                m = p6_5.match(line)
                if m:
                    # Routing for Networks:
                    routing_networks = False
                    routing_network_intfs = []
                    # Routing on Interfaces Configured Explicitly
                    routing_on_interfaces = False
                    routing_on_interfaces_intfs = []
                    # Routing Information Sources:
                    routing_information = False
                    routing_info_gateways = []
                    # Passive Interface(s):
                    passive_interfaces = True
                    passive_intfs = []
                    # Address Summarization:
                    address_summarization = True
                    address_summarization_intfs = []
                    continue

                # Loopback0
                # GigabitEthernet2
                # GigabitEthernet1
                m = p7.match(line)
                if m:
                    if routing_networks:
                        routing_network_intfs.append(str(m.groupdict()['interface']))
                        if protocol == 'ospf':
                            ospf_dict['areas'][area]['configured_interfaces'] = routing_network_intfs
                        elif protocol == 'isis':
                            isis_dict['configured_interfaces'] = routing_network_intfs
                    elif routing_on_interfaces:
                        routing_on_interfaces_intfs.append(str(m.groupdict()['interface']))
                        if protocol == 'ospf':
                            ospf_dict['areas'][area]['configured_interfaces'] = routing_on_interfaces_intfs
                    elif passive_interfaces:
                        passive_intfs.append(str(m.groupdict()['interface']))
                        if protocol == 'ospf':
                            ospf_dict['passive_interfaces'] = passive_intfs
                        elif protocol == 'isis':
                            isis_dict['passive_interfaces'] = passive_intfs
                    elif address_summarization:
                        address_summarization_intfs.append(str(m.groupdict()['interface']))
                        if protocol == 'isis':
                            isis_dict['address_summarization'] = address_summarization_intfs
                    continue

                # Gateway         Distance      Last Update
                # 10.36.3.3            110      07:33:00
                # 10.16.2.2            110      07:33:00
                # 10.64.4.4            110      00:19:15
                m = p8.match(line)
                if m:
                    group = m.groupdict()
                    gateway = str(group['gateway'])
                    distance = int(group['distance'])
                    last_update = str(group['last_update'])
                    if routing_information:
                        if protocol == 'ospf':
                            gateway_dict = ospf_dict. \
                                setdefault('routing_information_sources', {}). \
                                setdefault('gateway', {}).setdefault(gateway, {})
                            gateway_dict['distance'] = distance
                            gateway_dict['last_update'] = last_update
                        elif protocol == 'bgp':
                            gateway_dict = bgp_dict.setdefault('routing_information_sources', {}). \
                                setdefault(gateway, {})
                            gateway_dict['neighbor_id'] = gateway
                            gateway_dict['distance'] = distance
                            gateway_dict['last_update'] = last_update
                        elif protocol == 'isis':
                            gateway_dict = isis_dict. \
                                setdefault('routing_information_sources', {}). \
                                setdefault('gateway', {}).setdefault(gateway, {})

                            gateway_dict['distance'] = distance
                            gateway_dict['last_update'] = last_update

                    continue

                # Distance: (default is 110)
                m = p9.match(line)
                if m:
                    if protocol == 'ospf':
                        pdict = ospf_dict
                    elif protocol == 'application':
                        pdict = application_dict
                    elif protocol == 'isis':
                        pdict = isis_dict
                    else:
                        continue
                    # Set values
                    pref_dict = pdict.setdefault('preference', {})
                    single_value_dict = pref_dict.setdefault('single_value', {})
                    single_value_dict['all'] = int(m.groupdict()['num'])
                    continue

                # Distance: intra-area 112 inter-area 113 external 114
                m = p10.match(line)
                if m:
                    group = m.groupdict()
                    if protocol == 'ospf':
                        multi_values_dict = ospf_dict.setdefault('preference', {}). \
                            setdefault('multi_values', {})
                        multi_values_dict['external'] = int(group['external'])
                        detail_dict = multi_values_dict. \
                            setdefault('granularity', {}). \
                            setdefault('detail', {})
                        detail_dict['intra_area'] = int(group['intra'])
                        detail_dict['inter_area'] = int(group['inter'])
                    continue

                # Sending updates every 0 seconds
                m = p11.match(line)
                if m:
                    if protocol == 'application':
                        application_dict['update_frequency'] = \
                            int(m.groupdict()['update'])
                    continue

                # Invalid after 0 seconds, hold down 0, flushed after 0
                m = p12.match(line)
                if m:
                    group = m.groupdict()
                    if protocol == 'application':
                        application_dict['invalid'] = int(group['invalid'])
                        application_dict['holddown'] = int(group['holddown'])
                        application_dict['flushed'] = int(group['flushed'])
                    continue

                # IGP synchronization is disabled
                m = p13.match(line)
                if m:
                    if 'enabled' in m.groupdict()['igp']:
                        bgp_dict['igp_sync'] = True
                    else:
                        bgp_dict['igp_sync'] = False

                # Automatic route summarization is disabled
                m = p14.match(line)
                if m:
                    if 'enabled' in m.groupdict()['route']:
                        bgp_dict['automatic_route_summarization'] = True
                    else:
                        bgp_dict['automatic_route_summarization'] = False

                # Distance: external 20 internal 200 local 200
                m = p15.match(line)
                if m:
                    group = m.groupdict()
                    if protocol == 'bgp':
                        multi_values_dict = bgp_dict.setdefault('preference', {}).setdefault('multi_values', {})
                        multi_values_dict['external'] = int(group['external'])
                        multi_values_dict['internal'] = int(group['internal'])
                        multi_values_dict['local'] = int(group['local'])
                    continue

                # Sending updates every 60 seconds, next due in 0 sec
                m = p106.match(line)
                if m:
                    group = m.groupdict()
                    timers_dict = bgp_dict.setdefault('timers', {})
                    timers_dict.update({'update_interval': int(group['update_interval'])})
                    timers_dict.update({'next_update': int(group['next_update'])})
                    continue

                
                # Redistributing: isis banana
                m = p16.match(line)
                if m:
                    if protocol == 'isis':
                        isis_dict['redistributing'] = m.groupdict()['redistributing']
                    continue

                # 10.0.0.84 0.0.0.3 area 11
                # 10.0.0.88 0.0.0.3 area 11
                # 192.168.0.10 0.0.0.0 area 11
                m = p17.match(line)
                if m:
                    group = m.groupdict()
                    address = group['address']
                    mask = group['mask']
                    area = group['area']
                    ospf_network_dict = ospf_dict\
                        .setdefault('network', {})\
                        .setdefault(address, {})
                    ospf_network_dict['netmask'] = mask
                    ospf_network_dict['area'] = area

                    continue

                # Neighbor(s):
                m = p110.match(line)
                if m:
                    neighbors_flag = True

                    continue

                
                # 172.16.121.101                                        ACCEPT_SCI_RICHEMONT
                # 192.168.1.176                                         INTERNET_EDGE_IN
                # 192.168.1.177                                         INTERNET_EDGE_IN
                # 192.168.0.9
                m = p111.match(line)
                if m:
                    if neighbors_flag:
                        group = m.groupdict()
                        neighbor = group['neighbor']
                        route_map = group['route_map']
                        if protocol == 'bgp':
                            bgp_neighbor_dict = bgp_dict\
                                .setdefault('neighbors', {})\
                                .setdefault(neighbor, {})
                            if route_map:
                                bgp_neighbor_dict['route_map'] = route_map
                    continue

        return ret_dict




# ====================================================
#  parser for show ip route
# ====================================================
class ShowIpProtocolsSectionRip(ShowIpProtocols):
    """Parser for :
       show ip protocols | sec rip
       show ip protocols vrf {vrf} | sec rip
       """

    cli_command = ["show ip protocols | sec rip", "show ip protocols vrf {vrf} | sec rip"]
    exclude = ['network','next_update']

    def cli(self, vrf="", cmd ="",output=None):
        if vrf:
            cmd = self.cli_command[1].format(vrf=vrf)
        else:
            cmd = self.cli_command[0]

        return super().cli(cmd=cmd, vrf=vrf,output=output)

# ====================================================
#  schema for show ipv6 protocols | sec rip
# ====================================================
class ShowIpv6ProtocolsSectionRipSchema(MetaParser):
    """Schema for
            show ipv6 protocols | sec rip
            show ipv6 protocols vrf {vrf} | sec rip"""
    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        Optional('instance'): {
                            Any(): {
                                Optional('redistribute'): {
                                    Any(): {
                                        Optional('metric'): int,
                                        Optional('route_policy'): str,
                                    },
                                },
                                Optional('interfaces'): {
                                    Any():{},
                                },
                            },
                        },
                    },
                },
            },
        }
    }


# ======================================================
#  parser for show ipv6 protocols | sec rip
# =======================================================
class ShowIpv6ProtocolsSectionRip(ShowIpv6ProtocolsSectionRipSchema):
    """Parser for :
           show ipv6 protocols | sec rip
           show ipv6 protocols vrf {vrf} | sec rip
           """

    cli_command = ["show ipv6 protocols | sec rip", "show ipv6 protocols vrf {vrf} | sec rip"]

    def cli(self, vrf="", output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                vrf = 'default'
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        address_family= "ipv6"

        #IPv6 Routing Protocol is "rip ripng"
        p1 = re.compile(r'^\s*IPv6 +Routing +Protocol +is +\"(?P<protocol>[\w\s]+)\"$')

        # Interfaces:
        p2 = re.compile(r'^\s*Interfaces$')

        #   GigabitEthernet3.200
        p3 = re.compile(r'^\s*(?P<interface>[\w\.\/]+)$')

        # Redistribution:
        #   Redistributing protocol connected with metric 3
        #   Redistributing protocol connected with transparent metric 3
        p4 = re.compile(r'^\s*Redistributing +protocol +(?P<redistribute>\w+) +with( +transparent)? +metric( +(?P<metric>\d+))?$')
        #   Redistributing protocol static with transparent metric route-map static-to-rip
        p5 = re.compile(
            r'^\s*Redistributing +protocol +(?P<redistribute>\w+) +with +transparent +metric( +route-map +(?P<route_policy>[\w\-]+))?$')

        result_dict = {}

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # Routing Protocol is "rip ripng"
            m = p1.match(line)
            if m:
                group = m.groupdict()
                protocol = group['protocol']
                rip_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('address_family',{}). \
                    setdefault(address_family, {}).setdefault('instance', {}).setdefault(protocol, {})
                continue

            #   GigabitEthernet2.100
            m = p3.match(line)
            if m:
                group = m.groupdict()
                rip_dict.setdefault('interfaces', {}).setdefault(group['interface'], {})
                continue

            # Redistributing protocol connected with metric 3
            m = p4.match(line)
            if m:
                group = m.groupdict()
                redistribute = group['redistribute']
                redistribute_dict = rip_dict.setdefault('redistribute', {}).setdefault(redistribute, {})

                if group['metric']:
                    redistribute_dict.update({'metric': int(group['metric'])})
                continue
            # Redistributing protocol static with transparent metric route-map static-to-rip
            m = p5.match(line)
            if m:
                group = m.groupdict()
                redistribute = group['redistribute']

                redistribute_dict = rip_dict.setdefault('redistribute', {}).setdefault(redistribute, {})
                redistribute_dict.update({'route_policy': group['route_policy']})
                continue

        return result_dict


# ==============================
# Schema for 'show ipv6 protocols'
# ==============================
class ShowIpv6ProtocolsSchema(MetaParser):

    ''' Schema for "show ip protocols" '''

    schema = {
        'protocols': {
            Optional('rip'): {
                'vrf': {
                    Any(): {
                        'address_family': {
                            Any(): {
                                Optional('instance'): {
                                    Any(): {
                                        Optional('network'): list,
                                        'redistribute': {
                                            Any(): {
                                                Any(): {
                                                    Optional('metric'): int,
                                                    Optional('route_policy'): str,
                                                    Optional('include_connected'): bool,
                                                },
                                                Optional('metric'): int,
                                                Optional('route_policy'): str,
                                                Optional('include_connected'): bool,
                                            }
                                        },
                                        Optional('timers'): {
                                            'update_interval': int,
                                            'next_update': int,
                                            'invalid_interval': int,
                                            'holddown_interval': int,
                                            'flush_interval': int,
                                        },
                                        Optional('configured_interfaces'): list,
                                        Optional('neighbors'): {
                                            Any(): {
                                                'last_update': str,
                                                'distance': int
                                            }
                                        },
                                    }
                                }
                            }
                        }
                    }
                }
            },
            Optional('eigrp'): {
                'vrf': {
                    Any(): {
                        'address_family': {
                            Any(): {
                                'eigrp_instance': {
                                    Any(): {
                                        'router_id': str,
                                        'eigrp_id': int,
                                        Optional('name'): str,
                                        'named_mode': bool,
                                        Optional('passive_interfaces'): list,
                                        'metric_weight': {
                                            'k1': int,
                                            'k2': int,
                                            'k3': int,
                                            'k4': int,
                                            'k5': int,
                                            Optional('k6'): int,
                                        },
                                        Optional('topology'): {
                                            Any(): {
                                                'active_timer': int,
                                                'distance_internal': int,
                                                'distance_external': int,
                                                'max_path': int,
                                                'max_hopcount': int,
                                                'max_variance': int
                                            }
                                        },
                                        Optional('configured_interfaces'): list,
                                        'redistribute': {
                                            Any(): {
                                                Any(): {
                                                    Optional('metric'): int,
                                                    Optional('route_policy'): str,
                                                    Optional('include_connected'): bool,
                                                },
                                                Optional('metric'): int,
                                                Optional('route_policy'): str,
                                                Optional('include_connected'): bool,
                                            }
                                        },
                                    }
                                }
                            }
                        }
                    }
                }
            },
            Optional('ospf'): {
                'vrf': {
                    Any(): {
                        'address_family': {
                            Any(): {
                                'instance': {
                                    Any(): {
                                        Optional('network'): {
                                            Any(): {
                                                'netmask': str,
                                                'area': str,
                                            }
                                        },
                                        'router_id': str,
                                        'total_stub_area': int,
                                        'total_normal_area': int,
                                        'total_nssa_area': int,
                                        Optional('passive_interfaces'): list,
                                        Optional('routing_information_sources'): {
                                            'gateway': {
                                                Any(): {
                                                    'distance': int,
                                                    'last_update': str
                                                }
                                            }
                                        },
                                        Optional('areas'): {
                                            Any(): {
                                                Optional('configured_interfaces'): list
                                            }
                                        },
                                        'redistribute': {
                                            Any(): {
                                                Any(): {
                                                    Optional('metric'): int,
                                                    Optional('route_policy'): str,
                                                    Optional('include_connected'): bool,
                                                },
                                                Optional('metric'): int,
                                                Optional('route_policy'): str,
                                                Optional('include_connected'): bool,
                                            }
                                        },
                                    }
                                }
                            }
                        }
                    }
                }
            },
            Optional('bgp'): {
                'instance': {
                    'default': {
                        'bgp_id': int,
                        'vrf': {
                            'default': {
                                'address_family': {
                                    'ipv6': {
                                        'igp_sync': bool,
                                        Optional('preference'): {
                                            'multi_values': {
                                                'external': int,
                                                'local': int,
                                                'internal': int,
                                            }
                                        },
                                        Optional('neighbors'): {
                                            Any(): {
                                                Optional('route_map'): str,
                                            }
                                        },
                                        'redistribute': {
                                            Any(): {
                                                Any(): {
                                                    Optional('metric'): int,
                                                    Optional('route_policy'): str,
                                                    Optional('include_connected'): bool,
                                                },
                                                Optional('metric'): int,
                                                Optional('route_policy'): str,
                                                Optional('include_connected'): bool,
                                            }
                                        },
                                        Optional('routing_information_sources'): {
                                            Any(): {
                                                'neighbor_id': str,
                                                'distance': int,
                                                'last_update': str,
                                            }
                                        },
                                        Optional('timers'): {
                                            'update_interval': int,
                                            'next_update': int,
                                        },
                                    }
                                }
                            }
                        },
                    }
                }
            },
            Optional('isis'): {
                'vrf': {
                    Any(): {
                        'address_family': {
                            Any(): {
                                'instance': {
                                    Any(): {
                                        Optional('redistributing'): str,
                                        Optional('address_summarization'): list,
                                        'preference': {
                                            'single_value': {
                                                'all': int
                                            }
                                        },
                                        Optional('configured_interfaces'): list,
                                        Optional('passive_interfaces'): list,
                                        Optional('routing_information_sources'): {
                                            'gateway': {
                                                Any(): {
                                                    'distance': int,
                                                    'last_update': str
                                                }
                                            }
                                        },
                                    }
                                }
                            }
                        }
                    }
                }
            },
        }
    }


# ==============================
# Parser for 'show ipv6 protocols'
# ==============================
class ShowIpv6Protocols(ShowIpv6ProtocolsSchema):

    ''' Parser for "show ip protocols" '''

    cli_command = [
        'show ipv6 protocols',
        'show ipv6 protocols vrf {vrf}'
    ]

    exclude = ['last_update', ' network', 'next_update']

    def cli(self, vrf="", cmd="", output=None):
        if output is None:
            if not cmd:
                if vrf:
                    cmd = self.cli_command[1].format(vrf=vrf)
                else:
                    cmd = self.cli_command[0]
            # get output from device
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}

        if not vrf:
            vrf = "default"
        protocol = None
        # Routing for Networks:
        routing_networks = False
        routing_network_intfs = []
        # Routing on Interfaces Configured Explicitly
        routing_on_interfaces = False
        routing_on_interfaces_intfs = []
        # Routing Information Sources:
        routing_information = False
        routing_info_gateways = []
        # Passive Interface(s):
        passive_interfaces = False
        passive_intfs = []

        # IPv6 Routing Protocol is "ospf 1"
        # IPv6 Routing Protocol is "bgp 100"
        # IPv6 Routing Protocol is "isis"
        # IPv6 Routing Protocol is "isis banana"
        # IPv6 Routing Protocol is "eigrp 1"
        p1 = re.compile(r"^IPv6 Routing +Protocol +is"
                        r" +\"(?P<protocol>(ospf|bgp|isis|eigrp|rip))"
                        r"(?: *(?P<pid>(\S+)))?\"$")

        # Outgoing update filter list for all interfaces is not set
        # Incoming update filter list for all interfaces is not set
        p2 = re.compile(r"^(?P<dir>(Outgoing|Incoming)) +update +filter +list"
                        r" +for +all +interfaces +is +(?P<state>([a-zA-Z\s]+))$")

        # Router ID 10.4.1.1
        p3 = re.compile(r"^Router +ID +(?P<router_id>(\S+))$")

        # Number of areas: 1 normal, 0 stub, 0 nssa
        p4 = re.compile(r"^Number +of +areas:"
                        r" +(?P<normal>(\d+)) +normal,"
                        r" +(?P<stub>(\d+)) +stub, +(?P<nssa>(\d+)) +nssa$")

        # EIGRP-IPv6 VR(pyats) Address-Family Protocol for AS(20)
        # EIGRP-IPv6 Protocol for AS(20)
        p5 = re.compile(
            r'^EIGRP\-(?P<address_family>IPv4|IPv6)\s+(VR\((?P<name>\w+)\)\s+Address\-Family\s+)?'
            'Protocol\s+for\s+AS\(\s*(?P<as_num>[\S]+)\)\s*(?:VRF\((?P<vrf>\S+)\))?$'
        )

        # Routing for Networks:
        p6_1 = re.compile(r"^Routing +for +Networks:$")

        # Interfaces (Area 0):
        # Interfaces:
        p6_2 = re.compile(
            r"^Interfaces"
            r"( +\(Area +(?P<area>[\d\.]+)\))?\:$"
        )

        # Routing Information Sources:
        p6_3 = re.compile(r"^Routing +Information +Sources:$")

        # Passive Interface(s):
        p6_4 = re.compile(r"^Passive +Interface\(s\):$")

        # Address Summarization:
        p6_5 = re.compile(r"^Address +Summarization:$")

        # Loopback0
        # GigabitEthernet2
        # GigabitEthernet1
        # TenGigabitEthernet0/0/26
        # Serial0
        # VoIP-Null0
        p7 = re.compile(
            r'^(?P<interface>(Lo\S*|Gi\S*|Ten\S*|\S*(SL|VL)\S*|Se\S*|VoIP\S*|Vlan\S*|Po\S*))'
            '( +\((?P<passive>passive)\))?$'
        )

        # Gateway         Distance      Last Update
        # 10.36.3.3            110      07:33:00
        # 10.16.2.2            110      07:33:00
        # 10.64.4.4            110      00:19:15
        p8 = re.compile(r"^(?P<gateway>([0-9\.]+)) +(?P<distance>(\d+))"
                         " +(?P<last_update>([a-zA-Z0-9\:\.]+))$")
        # Metric weight K1=1, K2=0, K3=1, K4=0, K5=0 K6=0
        # Metric weight K1=1, K2=0, K3=1, K4=0, K5=0
        p9 = re.compile(
            r'^Metric +weight +K1=(?P<k1>\d+), +K2=(?P<k2>\d+), +K3=(?P<k3>\d+), +K4=(?P<k4>\d+),'
            ' +K5=(?P<k5>\d+)( +K6=(?P<k6>\d+))?$'
        )

        # Router ID 10.4.1.1
        p10 = re.compile(r"^Router\-ID: +(?P<router_id>(\S+))$")

        # Topology : 0 (base)
        p11 = re.compile(r'^Topology +:\s+(?P<topology_id>\d+)')

        # Active Timer: 3 min
        p11_1 = re.compile(r'^Active +Timer:\s+(?P<active_timer>\d+) +min$')

        # Distance: internal 90 external 170
        p11_2 = re.compile(r'^Distance:\s+internal\s+(?P<internal>\d+)\s+external\s+(?P<external>\d+)$')

        #  Maximum path: 16
        p11_3 = re.compile(r'^Maximum +path:\s+(?P<max_path>\d+)$')

        # Maximum hopcount 100
        p11_4 = re.compile(r'^Maximum +hopcount\s+(?P<max_hop>\d+)$')

        # Maximum metric variance 1
        p11_5 = re.compile(r'^Maximum +metric +variance\s+(?P<max_variance>\d+)$')

        # IGP synchronization is disabled
        p12 = re.compile(r"^IGP +synchronization +is +(?P<igp>(enabled|disabled))$")

        # Automatic route summarization is disabled
        p13 = re.compile(r"^Automatic +route +summarization +is"
                          " +(?P<route>(enabled|disabled))$")

        # Distance: external 20 internal 200 local 200
        # Distance:external 20 internal 200 local 200
        p14 = re.compile(
            r"^Distance: *external +(?P<external>(\d+)) +internal"
            r" +(?P<internal>(\d+)) +local +(?P<local>(\d+))$"
        )

        # Redistributing: isis banana
        p15 = re.compile(r"^Redistributing: +(?P<redistributing>([a-zA-Z\_\s]+))$")

        # 10.0.0.84 0.0.0.3 area 11
        # 10.0.0.88 0.0.0.3 area 11
        # 192.168.0.10 0.0.0.0 area 11
        p16 = re.compile(r'(?P<address>[\d\.]+)\s+(?P<mask>[\d\.]+)\s+area\s+(?P<area>[\d\.]+)')

        passive_interface_flag = False
        routing_network_flag = False
        neighbors_flag = False

        # Sending updates every 10 seconds, next due in 8 seconds
        p17 = re.compile(
            r'^\s*Sending +updates every +(?P<update_interval>\d+) +seconds, +next +due +in (?P<next_update>\d+) +(seconds|sec)$')

        # Redistributing protocol ospf 1 with metric 5 (internal, external 1 & 2, nssa-external 1 & 2) include-connected
        # Redistributing protocol bgp 65003 with metric 4 route-map test
        # Redistributing protocol eigrp 10 with metric 4 include-connected
        p18 = re.compile(
            r'^\s*Redistributing +protocol +(?P<redistribute>\w+)( +(?P<instance>[A-Za-z0-9]+))?( +with( +transparent)?'
            r' +metric( +(?P<metric>\d+))?)?( +\([A-Za-z0-9\-,&\s]+\))?( +route-map +(?P<route_policy>[\w\-]+))?'
            r'( +(?P<include_connected>include\-connected))?$'
        )

        # Neighbor(s):
        p19 = re.compile(r'^\s*Neighbor\(s\):$')

        # 172.16.121.101                                        ACCEPT_SCI_RICHEMONT
        # 192.168.1.176                                         INTERNET_EDGE_IN
        # 192.168.1.177                                         INTERNET_EDGE_IN
        # 192.168.0.9
        p20 = re.compile(r'(?P<neighbor>[\d\.\:\w]+)\s*(?P<route_map>[\w]+)?')

        network_list = []

        for line in out.splitlines():
            line = line.strip()

            # IPv6 Routing Protocol is "ospf 1"
            # IPv6 Routing Protocol is "bgp 100"
            # IPv6 Routing Protocol is "isis"
            # IPv6 Routing Protocol is "isis banana"
            # IPv6 Routing Protocol is "eigrp 1"
            m = p1.match(line)
            if m:
                group = m.groupdict()
                protocol = group['protocol']
                if group['pid']:
                    instance = str(m.groupdict()['pid'])

                # Set protocol dict
                protocol_dict = ret_dict.setdefault('protocols', {}). \
                    setdefault(protocol, {})

                if protocol == 'ospf':
                    # Get VRF information based on OSPF instance
                    out = self.device.execute("show running-config | section "
                                              "router ospf {}".format(instance))
                    # Parse for VRF
                    for line in out.splitlines():
                        line = line.strip()
                        # router ospf 1
                        # router ospf 2 vrf VRF1
                        p = re.search('router +ospf +(?P<instance>(\S+))'
                                      '(?: +vrf +(?P<vrf>(\S+)))?', line)
                        if p:
                            p_instance = str(p.groupdict()['instance'])
                            if p_instance == instance:
                                if p.groupdict()['vrf']:
                                    vrf = str(p.groupdict()['vrf'])
                                    break
                                else:
                                    vrf = 'default'
                                    break

                    # Set ospf_dict
                    ospf_dict = protocol_dict.setdefault('vrf', {}). \
                        setdefault(vrf, {}). \
                        setdefault('address_family', {}). \
                        setdefault('ipv6', {}). \
                        setdefault('instance', {}). \
                        setdefault(instance, {})
                    redistribute_dict = ospf_dict.setdefault('redistribute', {})
                elif protocol == 'bgp':
                    instance_dict = protocol_dict.setdefault('instance', {}). \
                        setdefault('default', {})
                    instance_dict['bgp_id'] = int(group['pid'])
                    # Set bgp_dict
                    bgp_dict = instance_dict.setdefault('vrf', {}). \
                        setdefault('default', {}). \
                        setdefault('address_family', {}). \
                        setdefault('ipv6', {})
                    redistribute_dict = bgp_dict.setdefault('redistribute', {})
                elif protocol == 'isis':
                    # Set isis_dict
                    if not group['pid']:
                        instance = 'default'
                    if not vrf:
                        vrf = "default"
                    isis_dict = protocol_dict.setdefault('vrf', {}). \
                        setdefault(vrf, {}). \
                        setdefault('address_family', {}). \
                        setdefault('ipv6', {}). \
                        setdefault('instance', {}). \
                        setdefault(instance, {})
                elif protocol == 'rip':
                    address_family = 'ipv6'
                    rip_dict = ret_dict.setdefault('protocols', {}).\
                                            setdefault('rip', {}).\
                                            setdefault('vrf', {}).\
                                            setdefault(vrf, {}).\
                                            setdefault('address_family', {}). \
                                            setdefault(address_family, {}).\
                                            setdefault('instance', {}).\
                                            setdefault(instance, {})
                    redistribute_dict = rip_dict.setdefault('redistribute', {})
                    continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                if 'vrf' in group and group['vrf']:
                    vrf = group['vrf']
                else:
                    vrf = 'default'
                eigrp_name = group.get('name', '')
                if eigrp_name:
                    instance = eigrp_name
                else:
                    instance = group['as_num']
                eigrp_dict = protocol_dict.setdefault(
                    'vrf', {}
                ).setdefault(
                    vrf, {}
                ).setdefault(
                    'address_family', {}
                ).setdefault(
                    group['address_family'].lower(), {}
                ).setdefault(
                    'eigrp_instance', {}
                ).setdefault(
                    instance, {}
                )
                if eigrp_name:
                    eigrp_dict.update({'name': eigrp_name})
                eigrp_dict.update({'named_mode': True if eigrp_name else False})
                eigrp_dict.update({'eigrp_id': int(group['as_num'])})
                redistribute_dict = eigrp_dict.setdefault('redistribute', {})
                continue

            # Redistributing protocol ospf 1 with metric 5 (internal, external 1 & 2, nssa-external 1 & 2) include-connected
            # Redistributing protocol bgp 65003 with metric 4 route-map test
            # Redistributing protocol eigrp 10 with metric 4 include-connected
            m = p18.match(line)
            if m:
                group = m.groupdict()
                source_proto_dict = redistribute_dict.setdefault(group['redistribute'], {})
                redistribute_instance = group.get('instance', '')
                if redistribute_instance:
                    source_proto_instance_dict = source_proto_dict.setdefault(redistribute_instance, {})
                    if group['metric']:
                        source_proto_instance_dict.update({'metric': int(group['metric'])})
                    if group['route_policy']:
                        source_proto_instance_dict.update({'route_policy': group['route_policy']})
                    source_proto_instance_dict.update({
                        'include_connected': True if group['include_connected'] else False
                    })
                else:
                    if group['metric']:
                        source_proto_dict.update({'metric': int(group['metric'])})
                    if group['route_policy']:
                        source_proto_dict.update({'route_policy': group['route_policy']})
                    source_proto_dict.update({
                        'include_connected': True if group['include_connected'] else False
                    })
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                if protocol == 'ospf':
                    pdict = ospf_dict
                elif protocol == 'isis':
                    pdict = isis_dict
                elif protocol == 'bgp':
                    pdict = bgp_dict
                else:
                    continue
                direction = str(group['dir']).lower() + '_' + 'filter_list'
                pdict[direction] = str(group['state']).lower()
                continue

            # Router ID 10.4.1.1
            m = p3.match(line)
            if m:
                ospf_dict['router_id'] = str(m.groupdict()['router_id'])
                continue

            # Number of areas: 1 normal, 0 stub, 0 nssa
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ospf_dict['total_normal_area'] = int(group['normal'])
                ospf_dict['total_stub_area'] = int(group['stub'])
                ospf_dict['total_nssa_area'] = int(group['nssa'])
                continue

            # Routing for Networks:
            m = p6_1.match(line)
            address_summarization = False
            if m:
                # Routing for Networks:
                routing_networks = True
                routing_network_intfs = []
                # Routing on Interfaces Configured Explicitly
                routing_on_interfaces = False
                routing_on_interfaces_intfs = []
                # Routing Information Sources:
                routing_information = False
                routing_info_gateways = []
                # Passive Interface(s):
                passive_interfaces = False
                passive_intfs = []
                # Address Summarization:
                address_summarization = False
                address_summarization_intfs = []
                continue

            # Interfaces (Area 0):
            # Interfaces :
            m = p6_2.match(line)
            if m:
                if m.groupdict()['area']:
                    area = int(m.groupdict()['area'])
                    ospf_area_dict = ospf_dict.setdefault(
                        'areas', {}
                    ).setdefault(area, {})
                # Routing for Networks:
                routing_networks = False
                routing_network_intfs = []
                # Routing on Interfaces Configured Explicitly
                routing_on_interfaces = True
                routing_on_interfaces_intfs = []
                # Routing Information Sources:
                routing_information = False
                routing_info_gateways = []
                # Passive Interface(s):
                passive_interfaces = False
                passive_intfs = []
                # Address Summarization:
                address_summarization = False
                address_summarization_intfs = []
                continue

            # Routing Information Sources:
            m = p6_3.match(line)
            if m:
                # Routing for Networks:
                routing_networks = False
                routing_network_intfs = []
                # Routing on Interfaces Configured Explicitly
                routing_on_interfaces = False
                routing_on_interfaces_intfs = []
                # Routing Information Sources:
                routing_information = True
                routing_info_gateways = []
                # Passive Interface(s):
                passive_interfaces = False
                passive_intfs = []
                # Address Summarization:
                address_summarization = False
                address_summarization_intfs = []
                continue

            # Passive Interface(s):
            m = p6_4.match(line)
            if m:
                # Routing for Networks:
                routing_networks = False
                routing_network_intfs = []
                # Routing on Interfaces Configured Explicitly
                routing_on_interfaces = False
                routing_on_interfaces_intfs = []
                # Routing Information Sources:
                routing_information = False
                routing_info_gateways = []
                # Passive Interface(s):
                passive_interfaces = True
                passive_intfs = []
                # Address Summarization:
                address_summarization = False
                address_summarization_intfs = []
                continue

            # Address Summarization:
            m = p6_5.match(line)
            if m:
                # Routing for Networks:
                routing_networks = False
                routing_network_intfs = []
                # Routing on Interfaces Configured Explicitly
                routing_on_interfaces = False
                routing_on_interfaces_intfs = []
                # Routing Information Sources:
                routing_information = False
                routing_info_gateways = []
                # Passive Interface(s):
                passive_interfaces = True
                passive_intfs = []
                # Address Summarization:
                address_summarization = True
                address_summarization_intfs = []
                continue

            # Loopback0
            # GigabitEthernet2
            # GigabitEthernet1
            m = p7.match(line)
            if m:
                if routing_networks:
                    group = m.groupdict()
                    routing_network_intfs.append(str(group['interface']))
                    if protocol == 'ospf':
                        ospf_dict['areas'][area]['configured_interfaces'] = routing_network_intfs
                    elif protocol == 'isis':
                        isis_dict['configured_interfaces'] = routing_network_intfs
                    elif protocol == 'rip':
                        rip_dict['configured_interfaces'] = routing_network_intfs
                elif routing_on_interfaces:
                    group = m.groupdict()
                    routing_on_interfaces_intfs.append(str(group['interface']))
                    is_passiv_intf = group.get('passive', '')
                    if is_passiv_intf:
                        passive_intfs.append(str(group['interface']))
                    if protocol == 'ospf':
                        ospf_dict['areas'][area]['configured_interfaces'] = routing_on_interfaces_intfs
                    elif protocol == 'rip':
                        rip_dict['configured_interfaces'] = routing_on_interfaces_intfs
                    elif protocol == 'eigrp':
                        eigrp_dict['configured_interfaces'] = routing_on_interfaces_intfs
                        if is_passiv_intf:
                            eigrp_dict['passive_interfaces'] = passive_intfs
                elif passive_interfaces:
                    passive_intfs.append(str(m.groupdict()['interface']))
                    if protocol == 'ospf':
                        ospf_dict['passive_interfaces'] = passive_intfs
                    elif protocol == 'isis':
                        isis_dict['passive_interfaces'] = passive_intfs
                elif address_summarization:
                    address_summarization_intfs.append(str(m.groupdict()['interface']))
                    if protocol == 'isis':
                        isis_dict['address_summarization'] = address_summarization_intfs
                continue

            # Gateway         Distance      Last Update
            # 10.36.3.3            110      07:33:00
            # 10.16.2.2            110      07:33:00
            # 10.64.4.4            110      00:19:15
            m = p8.match(line)
            if m:
                group = m.groupdict()
                gateway = str(group['gateway'])
                distance = int(group['distance'])
                last_update = str(group['last_update'])
                if routing_information:
                    if protocol == 'ospf':
                        gateway_dict = ospf_dict. \
                            setdefault('routing_information_sources', {}). \
                            setdefault('gateway', {}).setdefault(gateway, {})
                        gateway_dict['distance'] = distance
                        gateway_dict['last_update'] = last_update
                    elif protocol == 'bgp':
                        gateway_dict = bgp_dict.setdefault('routing_information_sources', {}). \
                            setdefault(gateway, {})
                        gateway_dict['neighbor_id'] = gateway
                        gateway_dict['distance'] = distance
                        gateway_dict['last_update'] = last_update
                    elif protocol == 'isis':
                        gateway_dict = isis_dict. \
                            setdefault('routing_information_sources', {}). \
                            setdefault('gateway', {}).setdefault(gateway, {})

                        gateway_dict['distance'] = distance
                        gateway_dict['last_update'] = last_update

                continue

            # Metric weight K1=1, K2=0, K3=1, K4=0, K5=0 K6=0
            # Metric weight K1=1, K2=0, K3=1, K4=0, K5=0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                metric_weight = {
                    'k1': int(group['k1']),
                    'k2': int(group['k2']),
                    'k3': int(group['k3']),
                    'k4': int(group['k4']),
                    'k5': int(group['k5'])
                }
                k6 = group.get('k6', '')
                if k6:
                    metric_weight['k6'] = int(k6)
                eigrp_dict.update({'metric_weight': metric_weight})
                continue

            # Router ID 10.4.1.1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                if protocol == 'eigrp':
                    eigrp_dict.update({'router_id': group['router_id']})
                continue

            # Topology : 0 (base)
            m = p11.match(line)
            if m:
                group = m.groupdict()
                eigrp_topology = eigrp_dict.setdefault(
                    'topology', {}
                ).setdefault(
                    group['topology_id'], {}
                )
                continue

            # Active Timer: 3 min
            m = p11_1.match(line)
            if m:
                if protocol == 'eigrp':
                    group = m.groupdict()
                    eigrp_topology.update({'active_timer': int(group['active_timer'])})
                continue

            # Distance: internal 90 external 170
            m = p11_2.match(line)
            if m:
                group = m.groupdict()
                if protocol == 'eigrp':
                    eigrp_topology.update({'distance_internal': int(group['internal'])})
                    eigrp_topology.update({'distance_external': int(group['external'])})
                continue

            # Maximum path: 16
            m = p11_3.match(line)
            if m:
                group = m.groupdict()
                if protocol == 'eigrp':
                    eigrp_topology.update({'max_path': int(group['max_path'])})
                continue

            #  Maximum hopcount 100
            m = p11_4.match(line)
            if m:
                group = m.groupdict()
                if protocol == 'eigrp':
                    eigrp_topology.update({'max_hopcount': int(group['max_hop'])})
                continue

            m = p11_5.match(line)
            if m:
                group = m.groupdict()
                eigrp_topology.update({'max_variance': int(group['max_variance'])})

            # IGP synchronization is disabled
            m = p12.match(line)
            if m:
                if 'enabled' in m.groupdict()['igp']:
                    bgp_dict['igp_sync'] = True
                else:
                    bgp_dict['igp_sync'] = False

            # Automatic route summarization is disabled
            m = p13.match(line)
            if m:
                if 'enabled' in m.groupdict()['route']:
                    bgp_dict['automatic_route_summarization'] = True
                else:
                    bgp_dict['automatic_route_summarization'] = False

            # Distance: external 20 internal 200 local 200
            m = p14.match(line)
            if m:
                group = m.groupdict()
                if protocol == 'bgp':
                    multi_values_dict = bgp_dict.setdefault('preference', {}).setdefault('multi_values', {})
                    multi_values_dict['external'] = int(group['external'])
                    multi_values_dict['internal'] = int(group['internal'])
                    multi_values_dict['local'] = int(group['local'])
                continue

            # Sending updates every 60 seconds, next due in 0 sec
            m = p17.match(line)
            if m:
                group = m.groupdict()
                timers_dict = bgp_dict.setdefault('timers', {})
                timers_dict.update({'update_interval': int(group['update_interval'])})
                timers_dict.update({'next_update': int(group['next_update'])})
                continue

            # Redistributing: isis banana
            m = p15.match(line)
            if m:
                if protocol == 'isis':
                    isis_dict['redistributing'] = m.groupdict()['redistributing']
                continue

            # 10.0.0.84 0.0.0.3 area 11
            # 10.0.0.88 0.0.0.3 area 11
            # 192.168.0.10 0.0.0.0 area 11
            m = p16.match(line)
            if m:
                group = m.groupdict()
                address = group['address']
                mask = group['mask']
                area = group['area']
                ospf_network_dict = ospf_dict\
                    .setdefault('network', {})\
                    .setdefault(address, {})
                ospf_network_dict['netmask'] = mask
                ospf_network_dict['area'] = area

                continue

            # Neighbor(s):
            m = p19.match(line)
            if m:
                neighbors_flag = True

                continue

            # 172.16.121.101                                        ACCEPT_SCI_RICHEMONT
            # 192.168.1.176                                         INTERNET_EDGE_IN
            # 192.168.1.177                                         INTERNET_EDGE_IN
            # 192.168.0.9
            m = p20.match(line)
            if m:
                if neighbors_flag:
                    group = m.groupdict()
                    try:
                        neighbor = IPAddress(group['neighbor'])
                    except:
                        continue
                    neighbor = group['neighbor']
                    route_map = group['route_map']
                    if protocol == 'bgp':
                        bgp_neighbor_dict = bgp_dict\
                            .setdefault('neighbors', {})\
                            .setdefault(neighbor, {})
                        if route_map:
                            bgp_neighbor_dict['route_map'] = route_map
                continue

        return ret_dict
