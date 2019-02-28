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

    cli_command = 'show ip protocols'

    def cli(self, output=None):

        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

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



# ====================================================
#  schema for show ip protocols | sec rip
# ====================================================
class ShowIpProtocolsSectionRipSchema(MetaParser):
    """Schema for show ip protocols | sec rip"""
    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        Optional('instance'): {
                            Any(): {
                                Optional('default_metric'): int,
                                Optional('distance'): int,
                                Optional('triggered_update_threshold'): int,
                                Optional('maximum_paths'): int,
                                Optional('output_delay'): int,
                                Optional('offset_list'): int,
                                Optional('send_version'): int,
                                Optional('receive_version'): int,
                                Optional('automatic_network_summarization_in_effect'): bool,
                                Optional('outgoing_update_filterlist'):{
                                    Optional('outgoing_update_filterlist') :str,
                                    Optional('interfaces'):{
                                        Any():{
                                            'filter': str,
                                            'per_user': bool,
                                            'default': str,
                                        },
                                    },
                                },
                                Optional('incoming_update_filterlist'): {
                                    Optional('incoming_update_filterlist'): str,
                                    Optional('interfaces'): {
                                        Any(): {
                                            'filter': str,
                                            'per_user': bool,
                                            'default': str,
                                        },
                                    },
                                },
                                Optional('incoming_route_metric'): {
                                    'added': str,
                                    'list': str,
                                },
                                Optional('network'): list,
                                Optional('default_redistribution_metric'): int,
                                Optional('redistribute'): {
                                    Any(): {
                                        Optional(Any()): {
                                            Optional('metric'): int,
                                            Optional('route_policy'): int,
                                            Optional('route_type'): str,
                                        },
                                        Optional('metric'): int,
                                        Optional('route_policy'): int,
                                    },
                                },
                                Optional('timers'):{
                                    Optional('update_interval'): int,
                                    Optional('next_update'): int,
                                    Optional('invalid_interval'): int,
                                    Optional('holddown_interval'): int,
                                    Optional('flush_interval'): int,
                                },
                                Optional('interfaces'): {
                                    Any(): {
                                        Optional('neighbors'):{
                                            Any(): {
                                                Optional('address'): str,
                                                },
                                            },
                                        Optional('summary_address'): {
                                            Any(): {
                                                Optional('metric'): str,
                                            },
                                        },
                                        Optional('filtered_per_user'): int,
                                        Optional('default_set'): bool,
                                        Optional('passive'): bool,
                                        Optional('send_version'): str,
                                        Optional('receive_version'): str,
                                        Optional('triggered_rip'): str,
                                        Optional('key_chain'): str,
                                    },
                                },
                                Optional('neighbors'): {
                                    Any():{
                                         Optional('last_update'): str,
                                         Optional('distance'): int,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }
    }


# ====================================================
#  parser for show ip route
# ====================================================
class ShowIpProtocolsSectionRip(ShowIpProtocolsSectionRipSchema):
    """Parser for :
       show ip protocols | sec rip
       show ip protocols vrf {vrf} | sec rip
       """

    cli_command = ["show ip protocols | sec rip","show ip protocols vrf {vrf} | sec rip"]

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

        address_family = "ipv4"
        passive_interface_flag = False
        routing_network_flag = False

        # Routing Protocol is "rip"
        p1 = re.compile(r'^\s*Routing Protocol +is +\"(?P<protocol>[\w]+)\"$')

        # Output delay 50 milliseconds between packets
        p2 = re.compile(r'^\s*Output +delay +(?P<output_delay>[\d]+) +milliseconds +between +packets$')

        # Outgoing update filter list for all interfaces is not set
        # Outgoing update filter list for all interfaces is 150
        p3 = re.compile(r'^\s*Outgoing +update +filter +list +for all +interfaces +is +(?P<outgoing_update_filterlist>[\S\s]+)$')

        # Incoming update filter list for all interfaces is not set
        # Incoming update filter list for all interfaces is 100
        p4 = re.compile(r'^\s*Incoming +update +filter +list +for all +interfaces +is +(?P<incoming_update_filterlist>[\S\s]+)$')

        # GigabitEthernet3.100 filtered by 130 (per-user), default is not set
        p4_1 = re.compile(
            r'^\s*(?P<interface>\S+) +filtered +by +(?P<filter>\d+)( +\((?P<per_user>\S+)\))?,'
            ' +default +is +(?P<default>[\w\s]+)$')
        # Incoming routes will have 10 added to metric if on list 21
        p5 = re.compile(r'^\s*Incoming +routes +will +have +(?P<added>\S+) +added +to +metric'
                         ' +if +on +list +(?P<list>\S+)$')

        # Sending updates every 10 seconds, next due in 8 seconds
        p6 = re.compile(r'^\s*Sending +updates every +(?P<update_interval>\d+) +seconds, +next +due +in (?P<next_update>\d+) +seconds$')

        # Invalid after 21 seconds, hold down 22, flushed after 23
        p7 = re.compile(r'^\s*Invalid +after +(?P<invalid_interval>\d+) +seconds, +hold +down +(?P<holddown_interval>\d+)'
                        ', +flushed +after +(?P<flush_interval>\d+)$')

        # Default redistribution metric is 3
        p8 = re.compile(r'^\s*Default redistribution metric is +(?P<default_redistribution_metric>\d+)$')

        # Redistributing: connected, static, rip
        p9 = re.compile(r'^\s*Redistributing: +(?P<Redistributing>[\w\,\s]+)$')

        # Neighbor(s):
        p10 = re.compile(r'^\s*Neighbor\(s\):$')

        #   10.1.2.2
        p11 = re.compile(r'^\s*(?P<neighbor>[\d\.]+)$')

        # Default version control: send version 2, receive version 2
        p12 = re.compile(r'^\s*Default +version +control: +send +version +(?P<send_version>\d+)'
                         ', receive version +(?P<receive_version>\d+)$')

        #   Interface                           Send  Recv  Triggered RIP  Key-chain
        #   GigabitEthernet3.100                2     2          No        1
        #   GigabitEthernet3.100                1 2   2          No        none
        p13 = re.compile(r'^\s*(?P<interface>[\S]+) +(?P<send>\d( \d)?)'
                         ' +(?P<receive>\d( \d)?)?'
                         ' +(?P<triggered_rip>\S+) +(?P<key_chain>\S+)$')

        # Automatic network summarization is not in effect
        # Automatic network summarization is in effect
        p14 = re.compile(r'^\s*Automatic +network +summarization +is( +(?P<automatic_network_summarization>not)+)? +in +effect$')

        # Address Summarization:
        p15 = re.compile(r'^\s*Address +Summarization:$')

        #   172.16.0.0/17 for GigabitEthernet3.100
        p16 = re.compile(r'^\s*(?P<prefix>[\d\.\/]+) +for +(?P<interface>[\w\.]+)$')

        # Maximum path: 4
        p17 = re.compile(r'^\s*Maximum +path: +(?P<maximum_path>\d+)$')

        # Routing for Networks:
        p18 = re.compile(r'^\s*Routing +for +Networks:$')

        #   10.0.0.0
        p19 = re.compile(r'^\s*(?P<network>[\d\.]+)$')

        # Passive Interface(s):
        p20 = re.compile(r'^\s*Passive +Interface\(s\):$')

        #   GigabitEthernet2.100
        p21 = re.compile(r'^\s*(?P<passive_interface>[\w\.]+)$')

        # Routing Information Sources:
        p22 = re.compile(r'^\s*Routing +Information +Sources:$')

        #   Gateway         Distance      Last Update
        #   10.1.2.2             120      00:00:04
        p23 = re.compile(r'^\s*(?P<gateway>[\d\.]+) +(?P<distance>\d+) +(?P<last_update>[\w\:]+)$')

        # Distance: (default is 120)
        p24 = re.compile(r'^\s*Distance: +\(default +is +(?P<distance>\d+)\)$')

        result_dict = {}
        network_list = []

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # Routing Protocol is "rip"
            m = p1.match(line)
            if m:
                group = m.groupdict()
                protocol = group['protocol']
                rip_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('address_family',{}). \
                    setdefault(address_family, {}).setdefault('instance', {}).setdefault(protocol, {})
                continue

            # Output delay 50 milliseconds between packets
            m = p2.match(line)
            if m:
                group = m.groupdict()
                rip_dict.update({'output_delay': int(group['output_delay'])})
                continue

            # Outgoing update filter list for all interfaces is not set
            # Outgoing update filter list for all interfaces is 150
            m = p3.match(line)
            if m:
                outgoing_flag = True
                incoming_flag = False
                group = m.groupdict()
                outgoing_dict = rip_dict.setdefault('outgoing_update_filterlist',{})
                outgoing_dict.update({'outgoing_update_filterlist': group['outgoing_update_filterlist']})
                continue

            # Incoming update filter list for all interfaces is 100
            m = p4.match(line)
            if m:
                incoming_flag=True
                outgoing_flag = False
                group = m.groupdict()
                incoming_dict = rip_dict.setdefault('incoming_update_filterlist',{})
                incoming_dict.update({k: v for k, v in group.items() if v})
                continue

            # GigabitEthernet3.100 filtered by 130 (per-user), default is not set
            m = p4_1.match(line)
            if m:
                if outgoing_flag:
                    temp_dict = outgoing_dict
                if incoming_flag:
                     temp_dict = incoming_dict

                group = m.groupdict()
                interface_out_dict = temp_dict.setdefault('interfaces', {}).setdefault(group['interface'], {})
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
            m = p5.match(line)
            if m:
                group = m.groupdict()
                incoming_route_dict = rip_dict.setdefault('incoming_route_metric', {})
                incoming_route_dict.update({k: v for k, v in group.items() if v})
                continue

            # Sending updates every 10 seconds, next due in 8 seconds
            m = p6.match(line)
            if m:
                group = m.groupdict()
                timers_dict = rip_dict.setdefault('timers', {})
                timers_dict.update({'update_interval': int(group['update_interval'])})
                timers_dict.update({'next_update': int(group['next_update'])})
                continue

            # Invalid after 21 seconds, hold down 22, flushed after 23
            m = p7.match(line)
            if m:
                group = m.groupdict()
                if 'timers' not in rip_dict:
                    timers_dict = rip_dict.setdefault('timers', {})
                timers_dict.update({'invalid_interval': int(group['invalid_interval'])})
                timers_dict.update({'holddown_interval': int(group['holddown_interval'])})
                timers_dict.update({'flush_interval': int(group['flush_interval'])})
                continue

            # Default redistribution metric is 3
            m = p8.match(line)
            if m:
                group = m.groupdict()
                rip_dict.update({'default_redistribution_metric': int(group['default_redistribution_metric'])})
                continue

            # Redistributing: connected, static, rip
            m = p9.match(line)
            if m:
                group = m.groupdict()
                redistributes = group['Redistributing'].split(',')
                redistribute_dict = rip_dict.setdefault('redistribute', {})
                for key in redistributes:
                    redistribute_dict.setdefault(key.strip(),{})
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                rip_dict.update({k: int(v) for k, v in group.items() if v })
                continue

            # Automatic network summarization is not in effect
            # Automatic network summarization is in effect
            m = p14.match(line)
            if m:
                group = m.groupdict()
                if group['automatic_network_summarization']:
                    automatic_network_summarization = False
                else:
                    automatic_network_summarization = True
                rip_dict.update({'automatic_network_summarization_in_effect': automatic_network_summarization})
                continue

            #   Interface                           Send  Recv  Triggered RIP  Key-chain
            #   GigabitEthernet3.100                2     2          No        1
            m = p13.match(line)
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
            m = p16.match(line)
            if m:
                group = m.groupdict()
                summary_dict = interface_dict.setdefault('summary_address', {})
                summary_dict.setdefault(group['prefix'],{})
                continue

            # Maximum path: 4
            m = p17.match(line)
            if m:
                group = m.groupdict()
                rip_dict.update({'maximum_paths': int(group['maximum_path'])})
                continue

            #  Routing for Networks:
            m = p18.match(line)
            if m:
                routing_network_flag = True
                continue

            # 10.0.0.0
            m = p19.match(line)
            if m:
                if routing_network_flag:
                    group = m.groupdict()
                    network_list.append(group['network'])
                    rip_dict.update({'network': list(set(network_list))})
                continue

            # Passive Interface(s):
            m = p20.match(line)
            if m:
                passive_interface_flag = True
                routing_network_flag = False
                continue

            #   GigabitEthernet2.100
            m = p21.match(line)
            if m:
                if passive_interface_flag == True:
                    group = m.groupdict()
                    interface_dict.update({'passive': True})
                continue

            # Routing Information Sources:
            m = p22.match(line)
            if m:
                passive_interface_flag = False
                routing_network_flag = False
                continue

            #   Gateway         Distance      Last Update
            #   10.1.2.2             120      00:00:04
            m = p23.match(line)
            if m:
                group = m.groupdict()
                neighbor_dict = rip_dict.setdefault('neighbors',{}).setdefault(group['gateway'],{})
                neighbor_dict.update({'last_update': group['last_update']})
                neighbor_dict.update({'distance': int(group['distance'])})
                continue

            # Distance: (default is 120)
            m = p24.match(line)
            if m:
                group = m.groupdict()
                rip_dict.update({'distance': int(group['distance'])})
                continue

        return result_dict

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
