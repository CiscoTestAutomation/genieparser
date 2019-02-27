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
        'protocols':
            {Optional('rip'):
                {'protocol_under_dev': bool},
            Optional('eigrp'):
                {'protocol_under_dev': bool},
            Optional('ospf'):
                {'vrf': 
                    {Any(): 
                        {'address_family': 
                            {Any(): 
                                {'instance': 
                                    {Any(): 
                                        {'spf_control': 
                                            {'paths': int},
                                        'preference': 
                                            {'single_value': 
                                                {'all': int},
                                            Optional('multi_values'): 
                                                {'granularity': 
                                                    {'detail': 
                                                        {'intra_area': int,
                                                        'inter_area': int},
                                                    Optional('coarse'): 
                                                        {'internal': int}},
                                                'external': int},
                                            },
                                        'router_id': str,
                                        'outgoing_filter_list': str,
                                        'incoming_filter_list': str,
                                        'total_areas': int,
                                        'total_stub_area': int,
                                        'total_normal_area': int,
                                        'total_nssa_area': int,
                                        Optional('passive_interfaces'): list,
                                        Optional('routing_information_sources'): 
                                            {'gateway': 
                                                {Any(): 
                                                    {'distance': int,
                                                    'last_update': str},
                                                },
                                            },
                                        Optional('areas'): 
                                            {Any(): 
                                                {Optional('configured_interfaces'): list},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            Optional('application'):
                {'outgoing_filter_list': str,
                'incoming_filter_list': str,
                'maximum_path': int,
                'preference': 
                    {'single_value': 
                        {'all': int}},
                'update_frequency': int,
                'invalid': int,
                'holddown': int,
                'flushed': int,
                },
            Optional('bgp'):
                {'instance': 
                    {'default': 
                        {'bgp_id': int,
                        'vrf': 
                            {'default': 
                                {'address_family': 
                                    {'ipv4': 
                                        {'outgoing_filter_list': str,
                                        'incoming_filter_list': str,
                                        'igp_sync': bool,
                                        'automatic_route_summarization': bool,
                                        'maximum_path': int,
                                        Optional('preference'): 
                                            {'multi_values': 
                                                {'external': int,
                                                'local': int,
                                                'internal': int,
                                                },
                                            },
                                        Optional('neighbor'): 
                                            {Any(): 
                                                {'neighbor_id': str,
                                                'distance': int,
                                                'last_update': str,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            Optional('isis'):
                {'vrf': 
                    {Any(): 
                        {'address_family': 
                            {Any(): 
                                {'instance': 
                                    {Any(): 
                                        {'outgoing_filter_list': str,
                                        'incoming_filter_list': str,
                                        'redistributing': str,
                                        Optional('address_summarization'): list,
                                        'maximum_path': int,
                                        'preference': 
                                            {'single_value': 
                                                {'all': int},
                                            },
                                        Optional('configured_interfaces'): list,
                                        Optional('passive_interfaces'): list,
                                        Optional('routing_information_sources'): 
                                            {'gateway': 
                                                {Any(): 
                                                    {'distance': int,
                                                    'last_update': str,
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }



# ==============================
# Parser for 'show ip protocols'
# ==============================
class ShowIpProtocols(ShowIpProtocolsSchema):

    ''' Parser for "show ip protocols" '''

    cli_command = 'show ip protocols'

    def cli(self, output=None):

        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}
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
        # Routing Protocol is "isis banana"
        # Routing Protocol is "eigrp 1"
        p1 = re.compile(r"^Routing +Protocol +is"
                         " +\"(?P<protocol>(ospf|bgp|isis|eigrp|application))"
                         "(?: *(?P<pid>(\S+)))?\"$")

        # Outgoing update filter list for all interfaces is not set
        # Incoming update filter list for all interfaces is not set
        p2 = re.compile(r"^(?P<dir>(Outgoing|Incoming)) +update +filter +list"
                         " +for +all +interfaces +is +(?P<state>([a-zA-Z\s]+))$")

        # Router ID 1.1.1.1
        p3 = re.compile(r"^Router +ID +(?P<router_id>(\S+))$")

        # Number of areas in this router is 1. 1 normal 0 stub 0 nssa
        p4 = re.compile(r"^Number +of +areas +in +this +router +is"
                         " +(?P<areas>(\d+)). +(?P<normal>(\d+)) +normal"
                         " +(?P<stub>(\d+)) +stub +(?P<nssa>(\d+)) +nssa$")

        # Maximum path: 4
        p5 = re.compile(r"^Maximum +path: +(?P<max>(\d+))$")

        # Routing for Networks:
        p6_1 = re.compile(r"^Routing +for +Networks:$")

        # Routing on Interfaces Configured Explicitly (Area 0):
        p6_2 = re.compile(r"^Routing +on +Interfaces +Configured +Explicitly"
                         " +\(Area +(?P<area>(\d+))\)\:$")


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
        p7 = re.compile(r"^(?P<interface>(Lo.*|Gi.*|Ten.*|.*(SL|VL).*))$")


        # Gateway         Distance      Last Update
        # 3.3.3.3              110      07:33:00
        # 2.2.2.2              110      07:33:00
        # 4.4.4.4              110      00:19:15
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
        p15 = re.compile(r"^Distance: +external +(?P<external>(\d+)) +internal"
                          " +(?P<internal>(\d+)) +local +(?P<local>(\d+))$")


        # Redistributing: isis banana
        p16 = re.compile(r"^Redistributing: +(?P<redistributing>([a-zA-Z\_\s]+))$")


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
                protocol_dict = ret_dict.setdefault('protocols', {}).\
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
                    ospf_dict = protocol_dict.setdefault('vrf', {}).\
                                              setdefault(vrf, {}).\
                                              setdefault('address_family', {}).\
                                              setdefault('ipv4', {}).\
                                              setdefault('instance', {}).\
                                              setdefault(instance, {})
                elif protocol == 'bgp':
                    instance_dict = protocol_dict.setdefault('instance', {}).\
                                                  setdefault('default', {})
                    instance_dict['bgp_id'] = int(group['pid'])
                    # Set bgp_dict
                    bgp_dict = instance_dict.setdefault('vrf', {}).\
                                             setdefault('default', {}).\
                                             setdefault('address_family', {}).\
                                             setdefault('ipv4', {})
                elif protocol == 'isis':
                    # Set isis_dict
                    isis_dict = protocol_dict.setdefault('vrf', {}).\
                                              setdefault('default', {}).\
                                              setdefault('address_family', {}).\
                                              setdefault('ipv4', {}).\
                                              setdefault('instance', {}).\
                                              setdefault(instance, {})
                elif protocol == 'application':
                    application_dict = protocol_dict
                elif protocol == 'eigrp':
                    protocol_dict['protocol_under_dev'] = True
                    eigrp_dict = protocol_dict
                elif protocol == 'rip':
                    protocol_dict['protocol_under_dev'] = True
                    rip_dict = protocol_dict
                continue

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
                direction = str(group['dir']).lower() + '_' + 'filter_list'
                pdict[direction] = str(group['state']).lower()
                continue

            # Router ID 1.1.1.1
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
                ospf_area_dict = ospf_dict.setdefault('areas', {}).\
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
            # 3.3.3.3              110      07:33:00
            # 2.2.2.2              110      07:33:00
            # 4.4.4.4              110      00:19:15
            m = p8.match(line)
            if m:
                group = m.groupdict()
                gateway = str(group['gateway'])
                distance = int(group['distance'])
                last_update = str(group['last_update'])
                if routing_information:
                    if protocol == 'ospf':
                        gateway_dict = ospf_dict.\
                            setdefault('routing_information_sources', {}).\
                            setdefault('gateway', {}).setdefault(gateway, {})
                        gateway_dict['distance'] = distance
                        gateway_dict['last_update'] = last_update
                    elif protocol == 'bgp':
                        gateway_dict = bgp_dict.setdefault('neighbor', {}).\
                                                setdefault(gateway, {})
                        gateway_dict['neighbor_id'] = gateway
                        gateway_dict['distance'] = distance
                        gateway_dict['last_update'] = last_update
                    elif protocol == 'isis':
                        gateway_dict = isis_dict.\
                            setdefault('routing_information_sources', {}).\
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
                    multi_values_dict = ospf_dict.setdefault('preference', {}).\
                                                  setdefault('multi_values', {})
                    multi_values_dict['external'] = int(group['external'])
                    detail_dict = multi_values_dict.\
                                        setdefault('granularity', {}).\
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

            # Redistributing: isis banana
            m = p16.match(line)
            if m:
                if protocol == 'isis':
                    isis_dict['redistributing'] = m.groupdict()['redistributing']


        return ret_dict
