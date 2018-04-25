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
            Optional('isis'):
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
                                                    'last_update': str,
                                                    },
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
            },
        }


# ==============================
# Parser for 'show ip protocols'
# ==============================
class ShowIpProtocols(ShowIpProtocolsSchema):

    ''' Parser for "show ip protocols" '''

    def cli(self):

        # Execute command on device
        out = self.device.execute('show ip protocols')

        # Init vars
        ret_dict = {}
        af = 'ipv4' # this is ospf - always ipv4
        protocol = None
        routing_interfaces = None
        passive_interfaces = None

        for line in out.splitlines():
            line = line.strip()

            # Routing Protocol is "ospf 1"
            p1_1 = re.compile(r'^Routing +Protocol +is +\"ospf +(?P<pid>(\S+))\"$')
            m = p1_1.match(line)
            if m:
                instance = str(m.groupdict()['pid'])
                protocol = 'ospf'

                # Get VRF information based on OSPF instance
                cmd = 'show running-config | section router ospf {}'.format(instance)
                out = self.device.execute(cmd)

                for line in out.splitlines():
                    line = line.rstrip()

                    # Skip the show command line so as to not match
                    if re.search('show', line):
                        continue

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

                # Build dictionary
                if 'protocols' not in ret_dict:
                    ret_dict['protocols'] = {}
                if 'ospf' not in ret_dict['protocols']:
                    ret_dict['protocols']['ospf'] = {}
                if 'vrf' not in ret_dict['protocols']['ospf']:
                    ret_dict['protocols']['ospf']['vrf'] = {}
                if vrf not in ret_dict['protocols']['ospf']['vrf']:
                    ret_dict['protocols']['ospf']['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['protocols']['ospf']['vrf']\
                        [vrf]:
                    ret_dict['protocols']['ospf']['vrf'][vrf]\
                        ['address_family'] = {}
                if af not in ret_dict['protocols']['ospf']['vrf'][vrf]\
                        ['address_family']:
                    ret_dict['protocols']['ospf']['vrf'][vrf]['address_family']\
                        [af] = {}
                if 'instance' not in ret_dict['protocols']['ospf']['vrf'][vrf]\
                        ['address_family'][af]:
                    ret_dict['protocols']['ospf']['vrf'][vrf]['address_family']\
                        [af]['instance'] = {}
                if instance not in ret_dict['protocols']['ospf']['vrf'][vrf]\
                        ['address_family'][af]['instance']:
                    ret_dict['protocols']['ospf']['vrf'][vrf]['address_family']\
                        [af]['instance'][instance] = {}
                # Set ospf_dict
                ospf_dict = ret_dict['protocols']['ospf']['vrf'][vrf]\
                                ['address_family'][af]['instance'][instance]
                continue

            # Routing Protocol is "application"
            p1_2 = re.compile(r'^Routing +Protocol +is +\"application\"$')
            m = p1_2.match(line)
            if m:
                protocol = 'application'
                # Build dictionary
                if 'protocols' not in ret_dict:
                    ret_dict['protocols'] = {}
                if 'application' not in ret_dict['protocols']:
                    ret_dict['protocols']['application'] = {}
                app_dict = ret_dict['protocols']['application']
                continue

            # Routing Protocol is "bgp 100"
            p1_3 = re.compile(r'^Routing +Protocol +is +\"bgp +(?P<pid>(\d+))\"$')
            m = p1_3.match(line)
            if m:
                protocol = 'bgp'
                # Build dictionary
                if 'protocols' not in ret_dict:
                    ret_dict['protocols'] = {}
                if 'bgp' not in ret_dict['protocols']:
                    ret_dict['protocols']['bgp'] = {}
                if 'instance' not in ret_dict['protocols']['bgp']:
                    ret_dict['protocols']['bgp']['instance'] = {}
                if 'default' not in ret_dict['protocols']['bgp']['instance']:
                    ret_dict['protocols']['bgp']['instance']['default'] = {}
                ret_dict['protocols']['bgp']['instance']['default']['bgp_id'] = \
                    int(m.groupdict()['pid'])
                if 'vrf' not in ret_dict['protocols']['bgp']['instance']\
                        ['default']:
                    ret_dict['protocols']['bgp']['instance']['default']\
                        ['vrf'] = {}
                if 'default' not in ret_dict['protocols']['bgp']['instance']\
                        ['default']['vrf']:
                    ret_dict['protocols']['bgp']['instance']['default']['vrf']\
                        ['default'] = {}
                if 'address_family' not in ret_dict['protocols']['bgp']\
                        ['instance']['default']['vrf']['default']:
                    ret_dict['protocols']['bgp']['instance']['default']['vrf']\
                        ['default']['address_family'] = {}
                if 'ipv4' not in ret_dict['protocols']['bgp']['instance']\
                        ['default']['vrf']['default']['address_family']:
                    ret_dict['protocols']['bgp']['instance']['default']['vrf']\
                        ['default']['address_family']['ipv4'] = {}
                bgp_dict = ret_dict['protocols']['bgp']['instance']['default']\
                            ['vrf']['default']['address_family']['ipv4']
                continue

            # Routing Protocol is "isis"
            p1_4 = re.compile(r'^Routing +Protocol +is +\"isis\"$')
            m = p1_4.match(line)
            if m:
                protocol = 'isis'
                # Build dictionary
                if 'protocols' not in ret_dict:
                    ret_dict['protocols'] = {}
                if 'isis' not in ret_dict['protocols']:
                    ret_dict['protocols']['isis'] = {}
                    ret_dict['protocols']['isis']['protocol_under_dev'] = True
                isis_dict = ret_dict['protocols']['isis']
                continue

            # Routing Protocol is "eigrp 1"
            p1_5 = re.compile(r'^Routing +Protocol +is +\"eigrp +(?P<pid>(\d+))\"$')
            m = p1_5.match(line)
            if m:
                protocol = 'eigrp'
                # Build dictionary
                if 'protocols' not in ret_dict:
                    ret_dict['protocols'] = {}
                if 'eigrp' not in ret_dict['protocols']:
                    ret_dict['protocols']['eigrp'] = {}
                    ret_dict['protocols']['eigrp']['protocol_under_dev'] = True
                eigrp_dict = ret_dict['protocols']['eigrp']
                continue

            # Routing Protocol is "rip"
            p1_6 = re.compile(r'^Routing +Protocol +is +\"rip\"$')
            m = p1_6.match(line)
            if m:
                protocol = 'rip'
                # Build dictionary
                if 'protocols' not in ret_dict:
                    ret_dict['protocols'] = {}
                if 'rip' not in ret_dict['protocols']:
                    ret_dict['protocols']['rip'] = {}
                    ret_dict['protocols']['rip']['protocol_under_dev'] = True
                rip_dict = ret_dict['protocols']['rip']
                continue

            # Outgoing update filter list for all interfaces is not set
            # Incoming update filter list for all interfaces is not set
            p2 = re.compile(r'^(?P<dir>(Outgoing|Incoming)) +update +filter'
                             ' +list +for +all +interfaces +is'
                             ' +(?P<state>([a-zA-Z\s]+))$')
            m = p2.match(line)
            if m:
                direction = str(m.groupdict()['dir']).lower()
                direction = direction + '_' + 'filter_list'
                if protocol == 'ospf':
                    pdict = ospf_dict
                elif protocol == 'application':
                    pdict = app_dict
                elif protocol == 'bgp':
                    pdict = bgp_dict
                else:
                    continue
                pdict[direction] = str(m.groupdict()['state']).lower()
                continue
            
            # Router ID 1.1.1.1
            p3 = re.compile(r'^Router +ID +(?P<router_id>(\S+))$')
            m = p3.match(line)
            if m:
                ospf_dict['router_id'] = str(m.groupdict()['router_id'])
                continue

            # Number of areas in this router is 1. 1 normal 0 stub 0 nssa
            p4 = re.compile(r'^Number +of +areas +in +this +router +is'
                             ' +(?P<areas>(\d+)). +(?P<normal>(\d+)) +normal'
                             ' +(?P<stub>(\d+)) +stub +(?P<nssa>(\d+)) +nssa$')
            m = p4.match(line)
            if m:
                ospf_dict['total_areas'] = int(m.groupdict()['areas'])
                ospf_dict['total_normal_area'] = int(m.groupdict()['normal'])
                ospf_dict['total_stub_area'] = int(m.groupdict()['stub'])
                ospf_dict['total_nssa_area'] = int(m.groupdict()['nssa'])
                continue

            # Maximum path: 4
            p5 = re.compile(r'^Maximum +path: +(?P<max>(\d+))$')
            m = p5.match(line)
            if m:
                if protocol == 'ospf':
                    if 'spf_control' not in ospf_dict:
                        ospf_dict['spf_control'] = {}
                    ospf_dict['spf_control']['paths'] = int(m.groupdict()['max'])
                elif protocol == 'application':
                    app_dict['maximum_path'] = int(m.groupdict()['max'])
                elif protocol == 'bgp':
                    bgp_dict['maximum_path'] = int(m.groupdict()['max'])
                continue

            # Routing for Networks:
            # Routing on Interfaces Configured Explicitly (Area 0):
            p6_1 = re.compile(r'^Routing +on +Interfaces +Configured +Explicitly'
                             ' +\(Area +(?P<area>(\d+))\)\:$')
            m = p6_1.match(line)
            if m:
                area = str(IPAddress(str(m.groupdict()['area'])))
                if 'areas' not in ospf_dict:
                    ospf_dict['areas'] = {}
                if area not in ospf_dict['areas']:
                    ospf_dict['areas'][area] = {}
                routing_interfaces = []
                continue

            # Passive Interface(s):
            p6_2 = re.compile(r'^Passive +Interface\(s\):$')
            m = p6_2.match(line)
            if m:
                passive_interfaces = []
                continue

            # Loopback0
            # GigabitEthernet2
            # GigabitEthernet1
            p7 = re.compile(r'^(?P<interface>(Lo.*|Gi.*|.*(SL|VL).*))$')
            m = p7.match(line)
            if m:
                if routing_interfaces is not None:
                    routing_interfaces.append(str(m.groupdict()['interface']))
                    ospf_dict['areas'][area]['configured_interfaces'] = routing_interfaces
                elif passive_interfaces is not None:
                    passive_interfaces.append(str(m.groupdict()['interface']))
                    ospf_dict['passive_interfaces'] = passive_interfaces
                continue

            # Routing Information Sources:
            # Gateway         Distance      Last Update
            # 3.3.3.3              110      07:33:00
            # 2.2.2.2              110      07:33:00
            # 4.4.4.4              110      00:19:15
            p8 = re.compile(r'^(?P<gateway>([0-9\.]+)) +(?P<distance>(\d+))'
                             ' +(?P<last_update>([0-9\:]+))$')
            m = p8.match(line)
            if m:
                gateway = str(m.groupdict()['gateway'])
                distance = int(m.groupdict()['distance'])
                last_update = str(m.groupdict()['last_update'])
                if protocol == 'ospf':
                    if 'routing_information_sources' not in ospf_dict:
                        ospf_dict['routing_information_sources'] = {}
                    if 'gateway' not in ospf_dict['routing_information_sources']:
                        ospf_dict['routing_information_sources']['gateway'] = {}
                    if gateway not in ospf_dict['routing_information_sources']\
                            ['gateway']:
                        ospf_dict['routing_information_sources']['gateway']\
                            [gateway] = {}
                    ospf_dict['routing_information_sources']['gateway'][gateway]\
                        ['distance'] = distance
                    ospf_dict['routing_information_sources']['gateway'][gateway]\
                        ['last_update'] = last_update
                elif protocol == 'bgp':
                    if 'neighbor' not in bgp_dict:
                        bgp_dict['neighbor'] = {}
                    if gateway not in bgp_dict['neighbor']:
                        bgp_dict['neighbor'][gateway] = {}
                    bgp_dict['neighbor'][gateway]['neighbor_id'] = gateway
                    bgp_dict['neighbor'][gateway]['distance'] = distance
                    bgp_dict['neighbor'][gateway]['last_update'] = last_update
                continue
            
            # Distance: (default is 110)
            p10 = re.compile(r'^Distance: +\(default +is +(?P<num>(\d+))\)$')
            m = p10.match(line)
            if m:
                if protocol == 'ospf':
                    if 'preference' not in ospf_dict:
                        ospf_dict['preference'] = {}
                    if 'single_value' not in ospf_dict['preference']:
                        ospf_dict['preference']['single_value'] = {}
                    ospf_dict['preference']['single_value']['all'] = \
                        int(m.groupdict()['num'])
                elif protocol == 'application':
                    if 'preference' not in app_dict:
                        app_dict['preference'] = {}
                    if 'single_value' not in app_dict['preference']:
                        app_dict['preference']['single_value'] = {}
                    app_dict['preference']['single_value']['all'] = \
                        int(m.groupdict()['num'])
                continue

            # Distance: intra-area 112 inter-area 113 external 114
            p11 = re.compile(r'^Distance: +intra-area +(?P<intra>(\d+))'
                             ' +inter-area +(?P<inter>(\d+)) +external'
                             ' +(?P<external>(\d+))$')
            m = p11.match(line)
            if m:
                if protocol == 'ospf':
                    if 'preference' not in ospf_dict:
                        ospf_dict['preference'] = {}
                    if 'multi_values' not in ospf_dict['preference']:
                        ospf_dict['preference']['multi_values'] = {}
                    if 'granularity' not in ospf_dict['preference']\
                            ['multi_values']:
                        ospf_dict['preference']['multi_values']\
                            ['granularity'] = {}
                    if 'detail' not in ospf_dict['preference']['multi_values']\
                            ['granularity']:
                        ospf_dict['preference']['multi_values']['granularity']\
                            ['detail'] = {}
                    ospf_dict['preference']['multi_values']['granularity']\
                        ['detail']['intra_area'] = int(m.groupdict()['intra'])
                    ospf_dict['preference']['multi_values']['granularity']\
                        ['detail']['inter_area'] = int(m.groupdict()['inter'])
                    ospf_dict['preference']['multi_values']['external'] = \
                        int(m.groupdict()['external'])
                continue

            # Sending updates every 0 seconds
            p12 = re.compile(r'^Sending +updates +every +(?P<update>(\d+))'
                              ' +seconds$')
            m = p12.match(line)
            if m:
                if protocol == 'application':
                    app_dict['update_frequency'] = int(m.groupdict()['update'])
                    continue

            # Invalid after 0 seconds, hold down 0, flushed after 0
            p13 = re.compile(r'^Invalid +after +(?P<invalid>(\d+)) +seconds,'
                              ' +hold +down +(?P<holddown>(\d+)), +flushed'
                              ' +after +(?P<flushed>(\d+))$')
            m = p13.match(line)
            if m:
                if protocol == 'application':
                    app_dict['invalid'] = int(m.groupdict()['invalid'])
                    app_dict['holddown'] = int(m.groupdict()['holddown'])
                    app_dict['flushed'] = int(m.groupdict()['flushed'])
                    continue

            # IGP synchronization is disabled
            p13 = re.compile(r'^IGP +synchronization +is'
                              ' +(?P<igp>(enabled|disabled))$')
            m = p13.match(line)
            if m:
                if 'enabled' in m.groupdict()['igp']:
                    bgp_dict['igp_sync'] = True
                else:
                    bgp_dict['igp_sync'] = False
            
            # Automatic route summarization is disabled
            p14 = re.compile(r'^Automatic +route +summarization +is'
                              ' +(?P<route>(enabled|disabled))$')
            m = p14.match(line)
            if m:
                if 'enabled' in m.groupdict()['route']:
                    bgp_dict['automatic_route_summarization'] = True
                else:
                    bgp_dict['automatic_route_summarization'] = False

            # Distance: external 20 internal 200 local 200
            p15 = re.compile(r'^Distance: +external +(?P<external>(\d+))'
                              ' +internal +(?P<internal>(\d+)) +local'
                              ' +(?P<local>(\d+))$')
            m = p15.match(line)
            if m:
                if 'preference' not in bgp_dict:
                    bgp_dict['preference'] = {}
                if 'multi_values' not in bgp_dict['preference']:
                    bgp_dict['preference']['multi_values'] = {}
                bgp_dict['preference']['multi_values']['external'] = \
                    int(m.groupdict()['external'])
                bgp_dict['preference']['multi_values']['internal'] = \
                    int(m.groupdict()['internal'])
                bgp_dict['preference']['multi_values']['local'] = \
                    int(m.groupdict()['local'])
                continue

        return ret_dict