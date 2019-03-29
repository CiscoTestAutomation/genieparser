''' show_ospf.py

IOSXE parsers for the following show commands:

    * show ip ospf
    * show ip ospf interface
    * show ip ospf sham-links
    * show ip ospf virtual-links
    * show ip ospf neighbor detail
    * show ip ospf database
    * show ip ospf database router
    * show ip ospf database network
    * show ip ospf database summary
    * show ip ospf database external
    * show ip ospf database opaque-area
    * show ip ospf mpls ldp interface
    * show ip ospf mpls traffic-eng link
    * show ip ospf max-metric
    * show ip ospf traffic

'''

# Python
import re
import xmltodict
from netaddr import IPAddress, IPNetwork

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional
from genie.libs.parser.utils.common import Common


# ==================
# Schema for:
#   * 'show ip ospf'
# ==================
class ShowIpOspfSchema(MetaParser):

    ''' Schema for:
        * 'show ip ospf'
    '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {'router_id': str,
                                Optional('enable'): bool,
                                'nsr':
                                    {'enable': bool},
                                'bfd': 
                                    {'enable': bool,
                                    Optional('strict_mode'): bool},
                                Optional('domain_id_type'): str,
                                Optional('domain_id_value'): str,
                                Optional('start_time'): str,
                                Optional('nssa'): bool,
                                Optional('area_transit'): bool,
                                Optional('redistribution'): 
                                    {Optional('max_prefix'): 
                                        {Optional('num_of_prefix'): int,
                                        Optional('prefix_thld'): int,
                                        Optional('warn_only'): bool},
                                    Optional('connected'): 
                                        {'enabled': bool,
                                        Optional('subnets'): str,
                                        Optional('metric'): int},
                                    Optional('static'): 
                                        {'enabled': bool,
                                        Optional('subnets'): str,
                                        Optional('metric'): int},
                                    Optional('bgp'): 
                                        {'bgp_id': int,
                                        Optional('metric'): int,
                                        Optional('subnets'): str,
                                        Optional('nssa_only'): str,
                                        },
                                    Optional('isis'): 
                                        {'isis_pid': str,
                                        Optional('subnets'): str,
                                        Optional('metric'): int}},
                                Optional('database_control'): 
                                    {'max_lsa': int,
                                     Optional('max_lsa_current'): int,
                                     Optional('max_lsa_threshold_value'): int,
                                     Optional('max_lsa_ignore_count'): int,
                                     Optional('max_lsa_current_count'): int,
                                     Optional('max_lsa_ignore_time'): int,
                                     Optional('max_lsa_reset_time'): int,
                                     Optional('max_lsa_limit'): int,
                                     Optional('max_lsa_warning_only'): bool},
                                Optional('stub_router'):
                                    {Optional('always'): 
                                        {'always': bool,
                                        'include_stub': bool,
                                        'summary_lsa': bool,
                                        'external_lsa': bool,
                                        Optional('summary_lsa_metric'): int,
                                        Optional('external_lsa_metric'): int,
                                        Optional('state'): str},
                                    Optional('on_startup'): 
                                        {'on_startup': int,
                                        'include_stub': bool,
                                        'summary_lsa': bool,
                                        'summary_lsa_metric': int,
                                        'external_lsa': bool,
                                        'external_lsa_metric': int,
                                        'state': str},
                                    },
                                Optional('spf_control'): 
                                    {Optional('incremental_spf'): bool,
                                    'throttle': 
                                        {'spf': 
                                            {'start': int,
                                            'hold': int,
                                            'maximum': int},
                                        'lsa': 
                                            {Optional('start'): int,
                                            Optional('hold'): int,
                                            Optional('maximum'): int,
                                            Optional('arrival'): int},
                                        },
                                    },
                                Optional('auto_cost'): 
                                    {'enable': bool,
                                    'reference_bandwidth': int,
                                    'bandwidth_unit': str},
                                Optional('adjacency_stagger'): 
                                    {'initial_number': int,
                                    'maximum_number': int,
                                    Optional('no_initial_limit'): bool},
                                Optional('graceful_restart'): 
                                    {Any(): 
                                        {'enable': bool,
                                        'type': str,
                                        Optional('helper_enable'): bool,
                                        Optional('restart_interval'): int}},
                                Optional('event_log'): 
                                    {'enable': bool,
                                    Optional('max_events'): int,
                                    Optional('mode'): str,
                                    },
                                Optional('numbers'): 
                                    {Optional('external_lsa'): int,
                                    Optional('external_lsa_checksum'): str,
                                    Optional('opaque_as_lsa'): int,
                                    Optional('opaque_as_lsa_checksum'): str,
                                    Optional('dc_bitless'): int,
                                    Optional('do_not_age'): int},
                                Optional('total_areas'): int,
                                Optional('total_normal_areas'): int,
                                Optional('total_stub_areas'): int,
                                Optional('total_nssa_areas'): int,
                                Optional('total_areas_transit_capable'): int,
                                Optional('lsa_group_pacing_timer'): int,
                                Optional('interface_flood_pacing_timer'): int,
                                Optional('retransmission_pacing_timer'): int,
                                Optional('external_flood_list_length'): int,
                                Optional('db_exchange_summary_list_optimization'): bool,
                                Optional('elapsed_time'): str,
                                Optional('lls'): bool,
                                Optional('opqaue_lsa'): bool,
                                Optional('flags'): 
                                    {Optional('abr'): bool,
                                    Optional('asbr'): bool},
                                Optional('areas'): 
                                    {Any(): 
                                        {'area_id': str,
                                        'area_type': str,
                                        Optional('summary'): bool,
                                        Optional('default_cost'): int,
                                        Optional('authentication'): bool,
                                        Optional('ranges'): 
                                            {Any(): 
                                                {'prefix': str,
                                                Optional('cost'): int,
                                                'advertise': bool}},
                                        Optional('rrr_enabled'): bool,
                                        Optional('statistics'): 
                                            {Optional('spf_runs_count'): int,
                                            Optional('spf_last_executed'): str,
                                            Optional('interfaces_count'): int,
                                            Optional('loopback_count'): int,
                                            Optional('area_scope_lsa_count'): int,
                                            Optional('area_scope_lsa_cksum_sum'): str,
                                            Optional('area_scope_opaque_lsa_count'): int,
                                            Optional('area_scope_opaque_lsa_cksum_sum'): str,
                                            Optional('dcbitless_lsa_count'): int,
                                            Optional('indication_lsa_count'): int,
                                            Optional('donotage_lsa_count'): int,
                                            Optional('flood_list_length'): int,
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


# ==================
# Parser for:
#   * 'show ip ospf'
# ==================
class ShowIpOspf(ShowIpOspfSchema):

    ''' Parser for:
        * 'show ip ospf'
    '''

    cli_command = 'show ip ospf'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}
        af = 'ipv4' # this is ospf - always ipv4

        for line in out.splitlines():
            line = line.strip()

            # Routing Process "ospf 1" with ID 10.36.3.3
            # VRF VRF1 in Routing Process "ospf 1" with ID 10.36.3.3
            p1 = re.compile(r'(?:^VRF +(?P<vrf>(\S+)) +in +)?Routing +Process'
                             ' +\"(?:ospf)? +(?P<instance>([a-zA-Z0-9\s]+))\"'
                             ' +with +ID +(?P<router_id>(\S+))$')
            m = p1.match(line)
            if m:
                instance = str(m.groupdict()['instance'])
                router_id = str(m.groupdict()['router_id'])
                if m.groupdict()['vrf']:
                    vrf = str(m.groupdict()['vrf'])
                else:
                    vrf = 'default'

                # Set structure
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if af not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family'][af] = {}
                if 'instance' not in ret_dict['vrf'][vrf]['address_family'][af]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance'] = {}
                if instance not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance] = {}

                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]
                sub_dict['router_id'] = router_id
                sub_dict['enable'] = True
                # Set some default values
                if 'nsr' not in sub_dict:
                    sub_dict['nsr'] = {}
                    sub_dict['nsr']['enable'] = False
                if 'bfd' not in sub_dict:
                    sub_dict['bfd'] = {}
                    sub_dict['bfd']['enable'] = False
                continue

            # Routing Process is shutdown
            p1_1 = re.compile(r'^Routing +Process +is +shutdown$')
            m = p1_1.match(line)
            if m:
                sub_dict['enable'] = False
                continue

            # Domain ID type 0x0005, value 0.0.0.2
            p2 = re.compile(r'^Domain +ID +type +(?P<domain_id>(\S+)), +value'
                               ' +(?P<value>(\S+))$')
            m = p2.match(line)
            if m:
                sub_dict['domain_id_type'] = str(m.groupdict()['domain_id'])
                sub_dict['domain_id_value'] = str(m.groupdict()['value'])
                continue

            # Start time: 00:23:49.050, Time elapsed: 1d01h
            p3 = re.compile(r'^Start +time: +(?P<start>([0-9\:\.]+)), +Time'
                             ' +elapsed: +(?P<elapsed>(\S+))$')
            m = p3.match(line)
            if m:
                sub_dict['start_time'] = str(m.groupdict()['start'])
                sub_dict['elapsed_time'] = str(m.groupdict()['elapsed'])
                continue

            # Supports only single TOS(TOS0) routes
            p4 = re.compile(r'^Supports +only +single +TOS(TOS0) routes$')
            m = p4.match(line)
            if m:
                sub_dict['single_tos_route'] = True
                continue

            # Supports opaque LSA
            p5 = re.compile(r'^Supports +opaque +LSA$')
            m = p5.match(line)
            if m:
                sub_dict['opqaue_lsa'] = True
                continue

            # Supports Link-local Signaling (LLS)
            p6 = re.compile(r'^Supports +Link-local +Signaling +\(LLS\)$')
            m = p6.match(line)
            if m:
                sub_dict['lls'] = True
                continue

            # Supports area transit capability
            p7 = re.compile(r'^Supports +area +transit +capability$')
            m = p7.match(line)
            if m:
                sub_dict['area_transit'] = True
                continue

            # Supports NSSA (compatible with RFC 3101)
            p8 = re.compile(r'^Supports +NSSA +\(compatible +with +RFC +3101\)$')
            m = p8.match(line)
            if m:
                sub_dict['nssa'] = True
                continue

            # Supports Database Exchange Summary List Optimization (RFC 5243)
            p9 = re.compile(r'^Supports +Database +Exchange +Summary +List'
                             ' +Optimization +\(RFC +5243\)$')
            m = p9.match(line)
            if m:
                sub_dict['db_exchange_summary_list_optimization'] = True
                continue

            # Event-log disabled
            # Event-log enabled, Maximum number of events: 1000, Mode: cyclic
            p10 = re.compile(r'^Event-log +(?P<event_log>(enabled|disabled)),'
                              '(?: +Maximum +number +of +events:'
                              ' +(?P<max_events>(\d+)),'
                              ' +Mode: +(?P<mode>(\S+)))?$')
            m = p10.match(line)
            if m:
                if 'event_log' not in sub_dict:
                    sub_dict['event_log'] = {}
                if 'enabled' in m.groupdict()['event_log']:
                    sub_dict['event_log']['enable'] = True
                else:
                    sub_dict['event_log']['enable'] = False
                if m.groupdict()['max_events']:
                    sub_dict['event_log']['max_events'] = \
                        int(m.groupdict()['max_events'])
                if m.groupdict()['mode']:
                    sub_dict['event_log']['mode'] = str(m.groupdict()['mode'])
                    continue

            # It is an area border router
            # It is an autonomous system boundary router
            # It is an area border and autonomous system boundary router
            p11 = re.compile(r'^It +is +an'
                               '(?: +(?P<abr>(area border)))?'
                               '(?: +and)?'
                               '(?: +(?P<asbr>(autonomous system boundary)))?'
                               ' +router$')
            m = p11.match(line)
            if m:
                if 'flags' not in sub_dict:
                    sub_dict['flags'] = {}
                if m.groupdict()['abr']:
                    sub_dict['flags']['abr'] = True
                if m.groupdict()['asbr']:
                    sub_dict['flags']['asbr'] = True
                continue

            # Redistributing External Routes from,
            p12_1 = re.compile(r'^Redistributing +External +Routes +from,$')
            m = p12_1.match(line)
            if m:
                if 'redistribution' not in sub_dict:
                    sub_dict['redistribution'] = {}
                    continue

            # connected 
            # connected with metric mapped to 10
            # static
            # static with metric mapped to 10
            p12_2 = re.compile(r'^(?P<type>(connected|static))(?: +with +metric'
                               ' +mapped +to +(?P<metric>(\d+)))?$')
            m = p12_2.match(line)
            if m:
                the_type = str(m.groupdict()['type'])
                if the_type not in sub_dict['redistribution']:
                    sub_dict['redistribution'][the_type] = {}
                sub_dict['redistribution'][the_type]['enabled'] = True
                if m.groupdict()['metric']:
                    sub_dict['redistribution'][the_type]['metric'] = \
                        int(m.groupdict()['metric'])
                continue

            # connected, includes subnets in redistribution
            # static, includes subnets in redistribution
            # isis, includes subnets in redistribution
            p12_2_1 = re.compile(r'^(?P<type>(connected|static|isis))'
                                 ', +includes +(?P<redist>(subnets)) +in +redistribution')
            m = p12_2_1.match(line)
            if m:
                the_type = str(m.groupdict()['type'])
                if the_type not in sub_dict['redistribution']:
                    sub_dict['redistribution'][the_type] = {}
                sub_dict['redistribution'][the_type]['enabled'] = True

                sub_dict['redistribution'][the_type]['subnets'] = m.groupdict()['redist']
                continue
            # bgp 100 with metric mapped to 111
            # isis 10 with metric mapped to 3333
            # bgp 100 with metric mapped to 100, includes subnets in redistribution, nssa areas only
            # bgp 100, includes subnets in redistribution
            p12_3 = re.compile(r'^(?P<prot>(bgp|isis)) +(?P<pid>(\d+))'
                               '(?: +with +metric +mapped +to +(?P<metric>(\d+)))?'
                               '(?:, +includes +(?P<redist>(subnets)) +in +redistribution)?'
                               '(?:, +(?P<nssa>(nssa areas only)))?$')
            m = p12_3.match(line)
            if m:
                prot = str(m.groupdict()['prot'])
                if prot not in sub_dict['redistribution']:
                    sub_dict['redistribution'][prot] = {}
                if prot == 'bgp':
                    sub_dict['redistribution'][prot]['bgp_id'] = \
                        int(m.groupdict()['pid'])
                else:
                    sub_dict['redistribution'][prot]['isis_pid'] = \
                        str(m.groupdict()['pid'])
                
                # Set parsed values
                if m.groupdict()['metric']:
                    sub_dict['redistribution'][prot]['metric'] = \
                        int(m.groupdict()['metric'])
                if m.groupdict()['redist']:
                    sub_dict['redistribution'][prot]['subnets'] = \
                        str(m.groupdict()['redist'])
                if m.groupdict()['nssa']:
                    sub_dict['redistribution'][prot]['nssa_only'] = True
                continue

            # Maximum number of redistributed prefixes 4000
            # Maximum number of redistributed prefixes 3000 (warning-only)
            p12_4 = re.compile(r'^Maximum +number +of +redistributed +prefixes'
                               ' +(?P<num_prefix>(\d+))'
                               '(?: +\((?P<warn>(warning-only))\))?')
            m = p12_4.match(line)
            if m:
                if 'max_prefix' not in sub_dict['redistribution']:
                    sub_dict['redistribution']['max_prefix'] = {}
                sub_dict['redistribution']['max_prefix']['num_of_prefix'] = \
                    int(m.groupdict()['num_prefix'])
                if m.groupdict()['warn']:
                    sub_dict['redistribution']['max_prefix']['warn_only'] = True
                else:
                    sub_dict['redistribution']['max_prefix']['warn_only'] = False
                    continue

            # Threshold for warning message 70%
            p12_5 = re.compile(r'^Threshold +for +warning +message'
                               ' +(?P<thld>(\d+))\%$')
            m = p12_5.match(line)
            if m:
                if 'max_prefix' not in sub_dict['redistribution']:
                    sub_dict['redistribution']['max_prefix'] = {}
                sub_dict['redistribution']['max_prefix']['prefix_thld'] = \
                    int(m.groupdict()['thld'])
                continue

            # Router is not originating router-LSAs with maximum metric
            p13 = re.compile(r'^Router +is +not +originating +router-LSAs'
                               ' +with +maximum +metric$')
            m = p13.match(line)
            if m:
                if 'stub_router' not in sub_dict:
                    sub_dict['stub_router'] = {}
                if 'always' not in sub_dict['stub_router']:
                    sub_dict['stub_router']['always'] = {}
                # Set values
                sub_dict['stub_router']['always']['always'] = False
                sub_dict['stub_router']['always']['include_stub'] = False
                sub_dict['stub_router']['always']['summary_lsa'] = False
                sub_dict['stub_router']['always']['external_lsa'] = False
                continue

            # Originating router-LSAs with maximum metric
            p14_1 = re.compile(r'^Originating +router-LSAs +with +maximum'
                               ' +metric$')
            m = p14_1.match(line)
            if m:
                if 'stub_router' not in sub_dict:
                    sub_dict['stub_router'] = {}
                    continue

            # Condition: always State: active
            # Condition: on start-up for 5 seconds, State: inactive
            p14_2 = re.compile(r'^Condition:'
                               ' +(?P<condition>(always|on start-up))'
                               '(?: +for +(?P<seconds>(\d+)) +seconds,)?'
                               ' +State: +(?P<state>(\S+))$')
            m = p14_2.match(line)
            if m:
                condition = str(m.groupdict()['condition']).lower().replace("-", "")
                condition = condition.replace(" ", "_")
                if 'stub_router' not in sub_dict:
                    sub_dict['stub_router'] = {}
                if condition not in sub_dict['stub_router']:
                    sub_dict['stub_router'][condition] = {}
                sub_dict['stub_router'][condition]['state'] = \
                    str(m.groupdict()['state']).lower()
                # Set 'condition' key
                if condition == 'always':
                    sub_dict['stub_router'][condition][condition] = True
                else:
                    sub_dict['stub_router'][condition][condition] = \
                        int(m.groupdict()['seconds'])
                continue

            # Advertise stub links with maximum metric in router-LSAs
            p14_3 = re.compile(r'^Advertise +stub +links +with +maximum +metric'
                               ' +in +router\-LSAs$')
            m = p14_3.match(line)
            if m:
                sub_dict['stub_router'][condition]['include_stub'] = True
                continue

            # Advertise summary-LSAs with metric 16711680
            p14_4 = re.compile(r'^Advertise +summary\-LSAs +with +metric'
                               ' +(?P<metric>(\d+))$')
            m = p14_4.match(line)
            if m:
                sub_dict['stub_router'][condition]['summary_lsa'] = True
                sub_dict['stub_router'][condition]['summary_lsa_metric'] = \
                    int(m.groupdict()['metric'])
                continue

            # Advertise external-LSAs with metric 16711680
            p14_5 = re.compile(r'^^Advertise +external\-LSAs +with +metric'
                               ' +(?P<metric>(\d+))$')
            m = p14_5.match(line)
            if m:
                sub_dict['stub_router'][condition]['external_lsa'] = True
                sub_dict['stub_router'][condition]['external_lsa_metric'] = \
                    int(m.groupdict()['metric'])
                continue

            # Initial SPF schedule delay 50 msecs
            p15 = re.compile(r'^Initial +SPF +schedule +delay +(?P<time>(\S+))'
                             ' +msecs$')
            m = p15.match(line)
            if m:
                start = int(float(m.groupdict()['time']))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'spf' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['spf'] = {}
                sub_dict['spf_control']['throttle']['spf']['start'] = start
                continue

            # Minimum hold time between two consecutive SPFs 200 msecs
            p16 = re.compile(r'^Minimum +hold +time +between +two +consecutive'
                             ' +SPFs +(?P<time>(\S+)) +msecs$')
            m = p16.match(line)
            if m:
                hold = int(float(m.groupdict()['time']))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'spf' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['spf'] = {}
                sub_dict['spf_control']['throttle']['spf']['hold'] = hold
                continue

            # Maximum wait time between two consecutive SPFs 5000 msecs
            p17 = re.compile(r'^Maximum +wait +time +between +two +consecutive'
                             ' +SPFs +(?P<time>(\S+)) +msecs$')
            m = p17.match(line)
            if m:
                maximum = int(float(m.groupdict()['time']))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'spf' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['spf'] = {}
                sub_dict['spf_control']['throttle']['spf']['maximum'] = maximum
                continue

            # Initial LSA throttle delay 50 msecs
            p18 = re.compile(r'^Initial +LSA +throttle +delay +(?P<time>(\S+))'
                             ' +msecs$')
            m = p18.match(line)
            if m:
                start = int(float(m.groupdict()['time']))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'lsa' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['lsa'] = {}
                sub_dict['spf_control']['throttle']['lsa']['start'] = start
                continue

            # Minimum hold time for LSA throttle 200 msecs
            p19 = re.compile(r'^Minimum +hold +time +for +LSA +throttle'
                              ' +(?P<time>(\S+)) +msecs$')
            m = p19.match(line)
            if m:
                hold = int(float(m.groupdict()['time']))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'lsa' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['lsa'] = {}
                sub_dict['spf_control']['throttle']['lsa']['hold'] = hold
                continue

            # Maximum wait time for LSA throttle 5000 msecs
            p20 = re.compile(r'^Maximum +wait +time +for +LSA +throttle'
                              ' +(?P<time>(\S+)) +msecs$')
            m = p20.match(line)
            if m:
                maximum = int(float(m.groupdict()['time']))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'lsa' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['lsa'] = {}
                sub_dict['spf_control']['throttle']['lsa']['maximum'] = maximum
                continue

            # Minimum LSA interval 200 msecs. Minimum LSA arrival 100 msecs
            # Minimum LSA arrival 100 msecs
            p21 = re.compile(r'^Minimum +LSA +arrival'
                              ' +(?P<arrival>(\S+)) +msecs$')
            m = p21.match(line)
            if m:
                if 'lsa' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['lsa'] = {}
                sub_dict['spf_control']['throttle']['lsa']['arrival'] = \
                    int(float(m.groupdict()['arrival']))
                continue

            # Incremental-SPF disabled
            p22 = re.compile(r'^Incremental-SPF +(?P<incr>(disabled|enabled))$')
            m = p22.match(line)
            if m:
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'enabled' in m.groupdict()['incr']:
                    sub_dict['spf_control']['incremental_spf'] = True
                else:
                    sub_dict['spf_control']['incremental_spf'] = False
                    continue

            # LSA group pacing timer 240 secs
            p23 = re.compile(r'LSA +group +pacing +timer'
                              ' +(?P<pacing>(\d+)) +secs$')
            m = p23.match(line)
            if m:
                sub_dict['lsa_group_pacing_timer'] = \
                    int(float(m.groupdict()['pacing']))
                continue

            # Interface flood pacing timer 33 msecs
            p24 = re.compile(r'Interface +flood +pacing +timer'
                              ' +(?P<interface>(\d+)) +msecs$')
            m = p24.match(line)
            if m:
                sub_dict['interface_flood_pacing_timer'] = \
                    int(float(m.groupdict()['interface']))
                continue

            # Retransmission pacing timer 66 msecs
            p25 = re.compile(r'Retransmission +pacing +timer'
                              ' +(?P<retransmission>(\d+)) +msecs$')
            m = p25.match(line)
            if m:
                sub_dict['retransmission_pacing_timer'] = \
                    int(float(m.groupdict()['retransmission']))
                continue

            # EXCHANGE/LOADING adjacency limit: initial 300, process maximum 300
            p26 = re.compile(r'EXCHANGE/LOADING +adjacency +limit: +initial'
                              ' +(?P<initial>(\S+)), +process +maximum'
                              ' +(?P<maximum>(\d+))$')
            m = p26.match(line)
            if m:
                if 'adjacency_stagger' not in sub_dict:
                    sub_dict['adjacency_stagger'] = {}
                if m.groupdict()['initial'] == 'None':
                    sub_dict['adjacency_stagger']['no_initial_limit'] = True
                else:
                    sub_dict['adjacency_stagger']['initial_number'] = \
                        int(m.groupdict()['initial'])
                sub_dict['adjacency_stagger']['maximum_number'] = \
                    int(m.groupdict()['maximum'])
                continue

            # Number of external LSA 1. Checksum Sum 0x00607f
            p27 = re.compile(r'^Number +of +external +LSA +(?P<ext>(\d+))\.'
                              ' +Checksum +Sum +(?P<checksum>(\S+))$')
            m = p27.match(line)
            if m:
                if 'numbers' not in sub_dict:
                    sub_dict['numbers'] = {}
                sub_dict['numbers']['external_lsa'] = int(m.groupdict()['ext'])
                sub_dict['numbers']['external_lsa_checksum'] = \
                    str(m.groupdict()['checksum'])
                continue

            # Number of opaque AS LSA 0. Checksum Sum 00000000
            p28 = re.compile(r'^Number +of +opaque +AS +LSA +(?P<opq>(\d+))\.'
                              ' +Checksum +Sum +(?P<checksum>(\S+))$')
            m = p28.match(line)
            if m:
                if 'numbers' not in sub_dict:
                    sub_dict['numbers'] = {}
                sub_dict['numbers']['opaque_as_lsa'] = int(m.groupdict()['opq'])
                sub_dict['numbers']['opaque_as_lsa_checksum'] = \
                    str(m.groupdict()['checksum'])
                continue

            # Number of DCbitless external and opaque AS LSA 0
            p29 = re.compile(r'^Number +of +DCbitless +external +and +opaque'
                              ' +AS +LSA +(?P<num>(\d+))$')
            m = p29.match(line)
            if m:
                if 'numbers' not in sub_dict:
                    sub_dict['numbers'] = {}
                sub_dict['numbers']['dc_bitless'] = int(m.groupdict()['num'])
                continue

            # Number of DoNotAge external and opaque AS LSA 0
            p30 = re.compile(r'^Number +of +DoNotAge +external +and +opaque'
                              ' +AS +LSA +(?P<num>(\d+))$')
            m = p30.match(line)
            if m:
                if 'numbers' not in sub_dict:
                    sub_dict['numbers'] = {}
                sub_dict['numbers']['do_not_age'] = int(m.groupdict()['num'])
                continue

            # Number of areas in this router is 1. 1 normal 0 stub 0 nssa
            p31 = re.compile(r'^Number +of +areas +in +this +router +is'
                              ' +(?P<total_areas>(\d+))\. +(?P<normal>(\d+))'
                              ' +normal +(?P<stub>(\d+)) +stub +(?P<nssa>(\d+))'
                              ' +nssa$')
            m = p31.match(line)
            if m:
                sub_dict['total_areas'] = int(m.groupdict()['total_areas'])
                sub_dict['total_normal_areas'] = int(m.groupdict()['normal'])
                sub_dict['total_stub_areas'] = int(m.groupdict()['stub'])
                sub_dict['total_nssa_areas'] = int(m.groupdict()['nssa'])
                continue

            # Number of areas transit capable is 0
            p32 = re.compile(r'Number +of +areas +transit +capable +is'
                              ' +(?P<num>(\d+))$')
            m = p32.match(line)
            if m:
                sub_dict['total_areas_transit_capable'] = int(m.groupdict()['num'])
                continue

            # Maximum number of non self-generated LSA allowed 123
            p33 = re.compile(r'^Maximum +number +of +non +self-generated +LSA'
                              ' +allowed +(?P<max_lsa>(\d+))$')
            m = p33.match(line)
            if m:
                if 'database_control' not in sub_dict:
                    sub_dict['database_control'] = {}
                sub_dict['database_control']['max_lsa'] = \
                    int(m.groupdict()['max_lsa'])
                continue

            # Current number of non self-generated LSA 0
            p33_1 = re.compile(r'^Current +number +of +non +self\-generated +LSA +(?P<max_lsa_current>\d+)$')
            m = p33_1.match(line)
            if m:
                if 'database_control' not in sub_dict:
                    sub_dict['database_control'] = {}
                sub_dict['database_control']['max_lsa_current'] = \
                    int(m.groupdict()['max_lsa_current'])
                continue

            # Threshold for warning message 75%
            p33_2 = re.compile(r'^Threshold +for +warning +message +(?P<max_lsa_threshold_value>\d+)\%$')
            m = p33_2.match(line)
            if m:
                if 'database_control' not in sub_dict:
                    sub_dict['database_control'] = {}
                sub_dict['database_control']['max_lsa_threshold_value'] = \
                    int(m.groupdict()['max_lsa_threshold_value'])
                continue

            # Ignore-time 5 minutes, reset-time 10 minutes
            p33_3 = re.compile(r'^Ignore\-time +(?P<max_lsa_ignore_time>\d+) +minutes,'
                               ' +reset\-time +(?P<max_lsa_reset_time>\d+) +minutes$')
            m = p33_3.match(line)
            if m:
                if 'database_control' not in sub_dict:
                    sub_dict['database_control'] = {}
                sub_dict['database_control']['max_lsa_ignore_time'] = \
                    int(m.groupdict()['max_lsa_ignore_time']) * 60
                sub_dict['database_control']['max_lsa_reset_time'] = \
                    int(m.groupdict()['max_lsa_reset_time']) * 60
                continue

            # Ignore-count allowed 5, current ignore-count 0
            p33_4 = re.compile(r'^Ignore\-count +allowed +(?P<max_lsa_ignore_count>\d+),'
                              ' +current ignore\-count +(?P<max_lsa_current_count>\d+)$')
            m = p33_4.match(line)
            if m:
                if 'database_control' not in sub_dict:
                    sub_dict['database_control'] = {}
                sub_dict['database_control']['max_lsa_ignore_count'] = \
                    int(m.groupdict()['max_lsa_ignore_count'])
                sub_dict['database_control']['max_lsa_current_count'] = \
                    int(m.groupdict()['max_lsa_current_count'])
                continue

            # Maximum limit of redistributed prefixes 5000 (warning-only)
            p33_5 = re.compile(r'^Maximum +limit +of +redistributed +prefixes +(?P<max_lsa_limit>\d+) +\(warning\-only\)$')
            m = p33_5.match(line)
            if m:
                if 'database_control' not in sub_dict:
                    sub_dict['database_control'] = {}
                sub_dict['database_control']['max_lsa_limit'] = int(m.groupdict()['max_lsa_limit'])
                sub_dict['database_control']['max_lsa_warning_only'] = False
                continue

            # External flood list length 0
            p34 = re.compile(r'^External +flood +list +length +(?P<num>(\d+))$')
            m = p34.match(line)
            if m:
                sub_dict['external_flood_list_length'] = int(m.groupdict()['num'])
                continue

            # Non-Stop Forwarding enabled
            # IETF Non-Stop Forwarding enabled
            p35 = re.compile(r'^(?P<gr_type>(IETF|Cisco)) +Non-Stop +Forwarding'
                              ' +(?P<enable>(enabled|disabled))$')
            m = p35.match(line)
            if m:
                gr_type = str(m.groupdict()['gr_type']).lower()
                if 'enabled' in m.groupdict()['enable']:
                    enable = True
                else:
                    enable = False
                if 'graceful_restart' not in sub_dict:
                    sub_dict['graceful_restart'] = {}
                if gr_type not in sub_dict['graceful_restart']:
                    sub_dict['graceful_restart'][gr_type] = {}
                # Set keys
                sub_dict['graceful_restart'][gr_type]['enable'] = True
                sub_dict['graceful_restart'][gr_type]['type'] = gr_type

            # IETF NSF helper support enabled
            # Cisco NSF helper support enabled
            p36 = re.compile(r'^(?P<gr_type>(IETF|Cisco)) +NSF +helper +support'
                              ' +(?P<gr_helper>(enabled|disabled))$')
            m = p36.match(line)
            if m:
                gr_type = str(m.groupdict()['gr_type']).lower()
                if 'enabled' in m.groupdict()['gr_helper']:
                    gr_helper = True
                else:
                    gr_helper = False
                if 'graceful_restart' not in sub_dict:
                    sub_dict['graceful_restart'] = {}
                if gr_type not in sub_dict['graceful_restart']:
                    sub_dict['graceful_restart'][gr_type] = {}
                # Set keys
                sub_dict['graceful_restart'][gr_type]['type'] = gr_type
                sub_dict['graceful_restart'][gr_type]['helper_enable'] = gr_helper
                if 'enable' not in sub_dict['graceful_restart'][gr_type]:
                    sub_dict['graceful_restart'][gr_type]['enable'] = False
                continue

            # restart-interval limit: 11 sec
            p36_1 = re.compile(r'^restart-interval +limit *: +(?P<num>(\d+)) +sec$')
            m = p36_1.match(line)
            if m:
                sub_dict['graceful_restart'][gr_type]['restart_interval'] = \
                    int(m.groupdict()['num'])
                continue

            # Reference bandwidth unit is 100 mbps
            # Reference bandwidth unit is 4294967 mbps
            p37 = re.compile(r'^Reference +bandwidth +unit +is'
                              ' +(?P<bd>(\d+)) +(?P<unit>(mbps))$')
            m = p37.match(line)
            if m:
                bd = int(m.groupdict()['bd'])
                if 'auto_cost' not in sub_dict:
                    sub_dict['auto_cost'] = {}
                sub_dict['auto_cost']['reference_bandwidth'] = bd
                sub_dict['auto_cost']['bandwidth_unit'] = str(m.groupdict()['unit'])
                if bd == 100:
                    # This is the default - set to False
                    sub_dict['auto_cost']['enable'] = False
                else:
                    sub_dict['auto_cost']['enable'] = True
                continue

            # Area BACKBONE(0)
            # Area BACKBONE(0.0.0.0) (Inactive)
            # Area 1
            p38 = re.compile(r'^Area +(?P<area>(\S+))(?: *\((I|i)nactive\))?$')
            m = p38.match(line)
            if m:
                parsed_area = str(m.groupdict()['area'])
                n = re.match('BACKBONE\((?P<area_num>(\S+))\)', parsed_area)
                if n:
                    area = str(IPAddress(str(n.groupdict()['area_num'])))
                else:
                    area = str(IPAddress(str(m.groupdict()['area'])))

                # Create dict
                if 'areas' not in sub_dict:
                    sub_dict['areas'] = {}
                if area not in sub_dict['areas']:
                    sub_dict['areas'][area] = {}
                
                # Set default values
                sub_dict['areas'][area]['area_id'] = area
                sub_dict['areas'][area]['area_type'] = 'normal'
                continue

            # It is a stub area
            # It is a stub area, no summary LSA in this area
            # It is a NSSA area
            p39_1 = re.compile(r'^It +is +a +(?P<area_type>(\S+)) +area'
                                '(?:, +(?P<summary>(no +summary +LSA +in +this'
                                ' +area)))?$')
            m = p39_1.match(line)
            if m:
                area_type = str(m.groupdict()['area_type']).lower()
                sub_dict['areas'][area]['area_type'] = area_type
                if area_type == 'stub':
                    if m.groupdict()['summary']:
                        sub_dict['areas'][area]['summary'] = False
                    else:
                        sub_dict['areas'][area]['summary'] = True
                    continue

            # generates stub default route with cost 111
            # generates stub default route with cost 222
            p39_2 = re.compile(r'^generates +stub +default +route +with +cost'
                                ' +(?P<default_cost>(\d+))$')
            m = p39_2.match(line)
            if m:
                sub_dict['areas'][area]['default_cost'] = \
                    int(m.groupdict()['default_cost'])
                continue

            # Area ranges are
            p40_1 = re.compile(r'^Area ranges are$')
            m = p40_1.match(line)
            if m:
                if 'ranges' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['ranges'] = {}
                continue

            # 10.4.1.0/24 Passive Advertise
            # 10.4.0.0/16 Passive DoNotAdvertise 
            # 10.4.0.0/16 Active(10 - configured) Advertise
            p40_2 = re.compile(r'^(?P<prefix>([0-9\.\/]+)) +(Passive|Active)'
                                '(?:\((?P<cost>(\d+)) +\- +configured\))?'
                                ' +(?P<advertise>(Advertise|DoNotAdvertise))$')
            m = p40_2.match(line)
            if m:
                prefix = str(m.groupdict()['prefix'])
                if 'ranges' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['ranges'] = {}
                if prefix not in sub_dict['areas'][area]['ranges']:
                    sub_dict['areas'][area]['ranges'][prefix] = {}
                sub_dict['areas'][area]['ranges'][prefix]['prefix'] = prefix
                if m.groupdict()['cost']:
                    sub_dict['areas'][area]['ranges'][prefix]['cost'] = \
                        int(m.groupdict()['cost'])
                if 'Advertise' in m.groupdict()['advertise']:
                    sub_dict['areas'][area]['ranges'][prefix]['advertise'] = True
                else:
                    sub_dict['areas'][area]['ranges'][prefix]['advertise'] = False
                continue

            # Number of interfaces in this area is 3
            # Number of interfaces in this area is 3 (1 loopback)
            p41 = re.compile(r'^Number +of +interfaces +in +this +area +is'
                              ' +(?P<num_intf>(\d+))(?:'
                              ' *\((?P<loopback>(\d+)) +loopback\))?$')
            m = p41.match(line)
            if m:
                if 'areas' not in sub_dict:
                    sub_dict['areas'] = {}
                if area not in sub_dict['areas']:
                    sub_dict['areas'][area] = {}
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['interfaces_count'] =\
                    int(m.groupdict()['num_intf'])
                if m.groupdict()['loopback']:
                    sub_dict['areas'][area]['statistics']['loopback_count'] =\
                        int(m.groupdict()['loopback'])
                continue

            # Area has RRR enabled
            p42 = re.compile(r'^Area +has +RRR +enabled$')
            m = p42.match(line)
            if m:
                sub_dict['areas'][area]['rrr_enabled'] = True
                continue

            # SPF algorithm executed 26 times
            p43 = re.compile(r'^SPF +algorithm +executed +(?P<count>(\d+))'
                              ' +times$')
            m = p43.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['spf_runs_count'] = \
                    int(m.groupdict()['count'])
                continue

            # SPF algorithm last executed 00:19:54.849 ago
            p44 = re.compile(r'^SPF +algorithm +last +executed'
                              ' +(?P<last_exec>(\S+)) +ago$')
            m = p44.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['spf_last_executed'] = \
                    str(m.groupdict()['last_exec'])
                continue

            # Area has no authentication
            p45 = re.compile(r'^Area +has +no +authentication$')
            m = p45.match(line)
            if m:
                continue

            # Number of LSA 19.  Checksum Sum 0x0a2fb5
            p46 = re.compile(r'^Number +of +LSA +(?P<lsa_count>(\d+))\.'
                              ' +Checksum +Sum +(?P<checksum_sum>(\S+))$')
            m = p46.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['area_scope_lsa_count'] =\
                    int(m.groupdict()['lsa_count'])
                sub_dict['areas'][area]['statistics']\
                    ['area_scope_lsa_cksum_sum'] = \
                        str(m.groupdict()['checksum_sum'])
                continue

            # Number of opaque link LSA 0.  Checksum Sum 00000000
            p47 = re.compile(r'^Number +of opaque +link +LSA'
                              ' +(?P<opaque_count>(\d+))\. +Checksum +Sum'
                              ' +(?P<checksum_sum>(\S+))$')
            m = p47.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']\
                    ['area_scope_opaque_lsa_count'] = \
                        int(m.groupdict()['opaque_count'])
                sub_dict['areas'][area]['statistics']\
                    ['area_scope_opaque_lsa_cksum_sum'] = \
                        str(m.groupdict()['checksum_sum'])
                continue

            # Number of DCbitless LSA 5
            p48 = re.compile(r'^Number +of +DCbitless +LSA +(?P<count>(\d+))$')
            m = p48.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['dcbitless_lsa_count'] = \
                    int(m.groupdict()['count'])
                continue

            # Number of indication LSA 0
            p49 = re.compile(r'^Number +of +indication +LSA +(?P<count>(\d+))$')
            m = p49.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['indication_lsa_count'] =\
                    int(m.groupdict()['count'])
                continue

            # Number of DoNotAge LSA 0
            p50 = re.compile(r'^Number +of +DoNotAge +LSA +(?P<count>(\d+))$')
            m = p50.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['donotage_lsa_count'] = \
                    int(m.groupdict()['count'])
                continue

            # Flood list length 0
            p51 = re.compile(r'^Flood +list +length +(?P<len>(\d+))$')
            m = p51.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['flood_list_length'] = \
                    int(m.groupdict()['len'])
                continue
        
            # Non-Stop Routing enabled
            p52 = re.compile(r'^Non-Stop +Routing +(?P<nsr>(enabled))$')
            m = p52.match(line)
            if m:
                sub_dict['nsr']['enable'] = True
                continue

            # BFD is enabled in strict mode
            p53_1 = re.compile(r'^BFD +is +enabled +in +strict +mode$')
            m = p53_1.match(line)
            if m:
                if 'bfd' not in sub_dict:
                    sub_dict['bfd'] = {}
                sub_dict['bfd']['enable'] = True
                sub_dict['bfd']['strict_mode'] = True
                continue

            # BFD is enabled
            p53_2 = re.compile(r'^BFD +is +enabled$')
            m = p53_2.match(line)
            if m:
                if 'bfd' not in sub_dict:
                    sub_dict['bfd'] = {}
                sub_dict['bfd']['enable'] = True
                continue

        return ret_dict


# ============================
# Schema for:
#   * 'show ip ospf interface'
# ============================
class ShowIpOspfInterfaceSchema(MetaParser):

    ''' Schema for:
        * 'show ip ospf interface'
    '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {'areas': 
                                    {Any(): 
                                        {Optional('interfaces'): 
                                            {Any(): 
                                                {'name': str,
                                                'enable': bool,
                                                'line_protocol': bool,
                                                'ip_address': str,
                                                Optional('interface_id'): int,
                                                Optional('attached'): str,
                                                'demand_circuit': bool,
                                                'router_id': str,
                                                'interface_type': str,
                                                'bfd': 
                                                    {'enable': bool},
                                                Optional('if_cfg'): bool,
                                                Optional('cost'): int,
                                                Optional('transmit_delay'): int,
                                                Optional('state'): str,
                                                Optional('priority'): int,
                                                Optional('dr_router_id'): str,
                                                Optional('dr_ip_addr'): str,
                                                Optional('bdr_router_id'): str,
                                                Optional('bdr_ip_addr'): str,
                                                Optional('hello_interval'): int,
                                                Optional('dead_interval'): int,
                                                Optional('wait_interval'): int,
                                                Optional('retransmit_interval'): int,
                                                Optional('passive'): bool,
                                                Optional('oob_resync_timeout'): int,
                                                Optional('hello_timer'): str,
                                                Optional('index'): str,
                                                Optional('flood_queue_length'): int,
                                                Optional('next'): str,
                                                Optional('lls'): bool,
                                                Optional('last_flood_scan_length'): int,
                                                Optional('max_flood_scan_length'): int,
                                                Optional('last_flood_scan_time_msec'): int,
                                                Optional('max_flood_scan_time_msec'): int,
                                                Optional('total_dcbitless_lsa'): int,
                                                Optional('donotage_lsa'): bool,
                                                Optional('ti_lfa_protected'): bool,
                                                Optional('ipfrr_candidate'): bool,
                                                Optional('ipfrr_protected'): bool,
                                                Optional('stub_host'): bool,
                                                Optional('prefix_suppression'): bool,
                                                Optional('ttl_security'): 
                                                    {'enable': bool,
                                                    Optional('hops'): int},
                                                Optional('graceful_restart'): 
                                                    {Any(): 
                                                        {'type': str,
                                                        'helper': bool}},
                                                Optional('topology'): 
                                                    {Any(): 
                                                        {'cost': int,
                                                        'disabled': bool,
                                                        'shutdown': bool,
                                                        'name': str}},
                                                Optional('statistics'): 
                                                    {Optional('adj_nbr_count'): int,
                                                    Optional('nbr_count'): int,
                                                    Optional('num_nbrs_suppress_hello'): int,
                                                    },
                                                Optional('neighbors'): 
                                                    {Any(): 
                                                        {Optional('dr_router_id'): str,
                                                        Optional('bdr_router_id'): str,
                                                        },
                                                    },
                                                Optional('authentication'): 
                                                    {'auth_trailer_key': 
                                                        {'crypto_algorithm': str,
                                                        Optional('youngest_key_id'): int,
                                                        },
                                                    },
                                                },
                                            },
                                        Optional('virtual_links'): 
                                            {Any(): 
                                                {'name': str,
                                                'enable': bool,
                                                'line_protocol': bool,
                                                'ip_address': str,
                                                Optional('interface_id'): int,
                                                Optional('attached'): str,
                                                'demand_circuit': bool,
                                                'router_id': str,
                                                'interface_type': str,
                                                'bfd': 
                                                    {'enable': bool},
                                                Optional('if_cfg'): bool,
                                                Optional('cost'): int,
                                                Optional('transmit_delay'): int,
                                                Optional('state'): str,
                                                Optional('priority'): int,
                                                Optional('dr_router_id'): str,
                                                Optional('dr_ip_addr'): str,
                                                Optional('bdr_router_id'): str,
                                                Optional('bdr_ip_addr'): str,
                                                Optional('hello_interval'): int,
                                                Optional('dead_interval'): int,
                                                Optional('wait_interval'): int,
                                                Optional('retransmit_interval'): int,
                                                Optional('passive'): bool,
                                                Optional('oob_resync_timeout'): int,
                                                Optional('hello_timer'): str,
                                                Optional('index'): str,
                                                Optional('flood_queue_length'): int,
                                                Optional('next'): str,
                                                Optional('lls'): bool,
                                                Optional('last_flood_scan_length'): int,
                                                Optional('max_flood_scan_length'): int,
                                                Optional('last_flood_scan_time_msec'): int,
                                                Optional('max_flood_scan_time_msec'): int,
                                                Optional('total_dcbitless_lsa'): int,
                                                Optional('donotage_lsa'): bool,
                                                Optional('ti_lfa_protected'): bool,
                                                Optional('ipfrr_candidate'): bool,
                                                Optional('ipfrr_protected'): bool,
                                                Optional('stub_host'): bool,
                                                Optional('prefix_suppression'): bool,
                                                Optional('ttl_security'): 
                                                    {'enable': bool,
                                                    Optional('hops'): int},
                                                Optional('graceful_restart'): 
                                                    {Any(): 
                                                        {'type': str,
                                                        'helper': bool}},
                                                Optional('topology'): 
                                                    {Any(): 
                                                        {'cost': int,
                                                        'disabled': bool,
                                                        'shutdown': bool,
                                                        'name': str}},
                                                Optional('statistics'): 
                                                    {Optional('adj_nbr_count'): int,
                                                    Optional('nbr_count'): int,
                                                    Optional('num_nbrs_suppress_hello'): int,
                                                    },
                                                Optional('neighbors'): 
                                                    {Any(): 
                                                        {Optional('dr_router_id'): str,
                                                        Optional('bdr_router_id'): str,
                                                        },
                                                    },
                                                Optional('authentication'): 
                                                    {'auth_trailer_key': 
                                                        {'crypto_algorithm': str,
                                                        Optional('youngest_key_id'): int,
                                                        },
                                                    },
                                                },
                                            },
                                        Optional('sham_links'): 
                                            {Any(): 
                                                {'name': str,
                                                'enable': bool,
                                                'line_protocol': bool,
                                                'ip_address': str,
                                                Optional('interface_id'): int,
                                                Optional('attached'): str,
                                                'demand_circuit': bool,
                                                'router_id': str,
                                                'interface_type': str,
                                                'bfd': 
                                                    {'enable': bool},
                                                Optional('if_cfg'): bool,
                                                Optional('cost'): int,
                                                Optional('transmit_delay'): int,
                                                Optional('state'): str,
                                                Optional('priority'): int,
                                                Optional('dr_router_id'): str,
                                                Optional('dr_ip_addr'): str,
                                                Optional('bdr_router_id'): str,
                                                Optional('bdr_ip_addr'): str,
                                                Optional('hello_interval'): int,
                                                Optional('dead_interval'): int,
                                                Optional('wait_interval'): int,
                                                Optional('retransmit_interval'): int,
                                                Optional('passive'): bool,
                                                Optional('oob_resync_timeout'): int,
                                                Optional('hello_timer'): str,
                                                Optional('index'): str,
                                                Optional('flood_queue_length'): int,
                                                Optional('next'): str,
                                                Optional('lls'): bool,
                                                Optional('last_flood_scan_length'): int,
                                                Optional('max_flood_scan_length'): int,
                                                Optional('last_flood_scan_time_msec'): int,
                                                Optional('max_flood_scan_time_msec'): int,
                                                Optional('total_dcbitless_lsa'): int,
                                                Optional('donotage_lsa'): bool,
                                                Optional('ti_lfa_protected'): bool,
                                                Optional('ipfrr_candidate'): bool,
                                                Optional('ipfrr_protected'): bool,
                                                Optional('stub_host'): bool,
                                                Optional('prefix_suppression'): bool,
                                                Optional('ttl_security'): 
                                                    {'enable': bool,
                                                    Optional('hops'): int},
                                                Optional('graceful_restart'): 
                                                    {Any(): 
                                                        {'type': str,
                                                        'helper': bool}},
                                                Optional('topology'): 
                                                    {Any(): 
                                                        {'cost': int,
                                                        'disabled': bool,
                                                        'shutdown': bool,
                                                        'name': str}},
                                                Optional('statistics'): 
                                                    {Optional('adj_nbr_count'): int,
                                                    Optional('nbr_count'): int,
                                                    Optional('num_nbrs_suppress_hello'): int},
                                                Optional('neighbors'): 
                                                    {Any(): 
                                                        {Optional('dr_router_id'): str,
                                                        Optional('bdr_router_id'): str,
                                                        },
                                                    },
                                                Optional('authentication'): 
                                                    {'auth_trailer_key': 
                                                        {'crypto_algorithm': str,
                                                        Optional('youngest_key_id'): int,
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
            },
        }


# ===========================================
# Parser for:
#   * 'show ospf vrf all-inclusive interface'
# ===========================================
class ShowIpOspfInterface(ShowIpOspfInterfaceSchema):

    ''' Parser for:
        * 'show ip ospf interface'
    '''

    cli_command = 'show ip ospf interface'

    def cli(self):
        out = self.device.execute(self.cli_command)

        # Init vars
        ret_dict = {}
        af = 'ipv4' # this is ospf - always ipv4

        # Mapping dict
        bool_dict = {'up': True, 'down': False, 'unknown': False}

        for line in out.splitlines():
            line = line.strip()

            # Loopback0 is up, line protocol is up 
            # GigabitEthernet2 is up, line protocol is up
            # Port-channel2.100 is administratively down, line protocol is down
            # OSPF_SL1 is up, line protocol is up 
            # OSPF_VL3 is up, line protocol is up 
            # TenGigabitEthernet3/0/1 is up, line protocol is up (connected)
            # TenGigabitEthernet1/8 is down, line protocol is down (notconnect)
            # TenGigabitEthernet2/6.3052 is administratively down, line protocol is down (disabled)
            # TenGigabitEthernet1/15 is down, line protocol is down (err-disabled)
            p1 = re.compile(r'^(?P<interface>(\S+)) +is( +administratively)?'
                             ' +(?P<enable>(unknown|up|down)), +line +protocol'
                             ' +is +(?P<line_protocol>(up|down))'
                             '(?: +\(\S+\))?$')
            m = p1.match(line)
            if m:
                interface = str(m.groupdict()['interface'])
                enable = str(m.groupdict()['enable'])
                line_protocol = str(m.groupdict()['line_protocol'])

                # Determine if 'interface' or 'sham_link' or 'virtual_link'
                if re.search('SL', interface):
                    x = re.match('(?P<ignore>\S+)_SL(?P<num>(\d+))', interface)
                    if x:
                        intf_type = 'sham_links'
                        name = 'SL' + str(x.groupdict()['num'])
                elif re.search('VL', interface):
                    x = re.match('(?P<ignore>\S+)_VL(?P<num>(\d+))', interface)
                    if x:
                        intf_type = 'virtual_links'
                        name = 'VL' + str(x.groupdict()['num'])
                else:
                    intf_type = 'interfaces'
                    name = interface
                continue

            # Internet Address 10.4.1.1/32, Interface ID 11, Area 0
            # Internet Address 0.0.0.0/0, Area 0, Attached via Not Attached
            # Internet Address 10.229.4.4/24, Area 1, Attached via Interface Enable
            p2 = re.compile(r'^Internet +Address +(?P<address>(\S+)),'
                             '(?: +Interface +ID +(?P<intf_id>(\d+)),)?'
                             ' +Area +(?P<area>(\S+))(?:, +Attached +via'
                             ' +(?P<attach>(.*)))?$')
            m = p2.match(line)
            if m:
                ip_address = str(m.groupdict()['address'])
                area = str(IPAddress(str(m.groupdict()['area'])))
                if m.groupdict()['intf_id']:
                    intf_id = int(m.groupdict()['intf_id'])
                if m.groupdict()['attach']:
                    attached = str(m.groupdict()['attach']).lower()
                continue

            # Attached via Interface Enable
            p2_1 = re.compile(r'^Attached +via +(?P<attached>([a-zA-Z0-9\s]+))$')
            m = p2_1.match(line)
            if m:
                attached = str(m.groupdict()['attached']).lower()
                continue

            # Process ID 1, Router ID 10.64.4.4, Network Type VIRTUAL_LINK, Cost: 1
            # Process ID 2, Router ID 10.229.11.11, Network Type SHAM_LINK, Cost: 111
            # Process ID 1, Router ID 10.4.1.1, Network Type BROADCAST, Cost: 1
            p3 = re.compile(r'^Process +ID +(?P<pid>(\S+)),'
                             '(?: +VRF +(?P<vrf>(\S+)))?'
                             ' +Router +ID +(?P<router_id>(\S+)),'
                             ' +Network +Type +(?P<interface_type>(\S+)),'
                             ' +Cost: +(?P<cost>(\d+))$')
            m = p3.match(line)
            if m:
                instance = str(m.groupdict()['pid'])
                router_id = str(m.groupdict()['router_id'])
                interface_type = str(m.groupdict()['interface_type']).lower()
                interface_type = interface_type.replace("_", "-")

                # Get interface values
                if intf_type == 'interfaces':
                    intf_name = interface
                elif intf_type == 'virtual_links':
                    # Init
                    vl_addr = None
                    vl_transit_area_id = None

                    # Execute command to get virtual-link address
                    cmd = 'show ip ospf virtual-links | i {intf}'.format(intf=interface)
                    out = self.device.execute(cmd)

                    for line in out.splitlines():
                        line = line.rstrip()
                        # Virtual Link OSPF_VL0 to router 10.100.5.5 is down
                        p = re.search('Virtual +Link +(?P<intf>(\S+)) +to +router'
                                     ' +(?P<address>(\S+)) +is +(up|down)'
                                     '(?:.*)?', line)
                        if p:
                            if interface == str(p.groupdict()['intf']):
                                vl_addr = str(p.groupdict()['address'])
                                break

                    # Execute command to get virtual-link transit_area_id
                    if vl_addr is not None:
                        cmd = 'show running-config | i virtual-link | i {addr}'.format(addr=vl_addr)
                        out = self.device.execute(cmd)

                        for line in out.splitlines():
                            line = line.rstrip()
                            #  area 1 virtual-link 10.100.5.5
                            q = re.search('area +(?P<q_area>(\d+)) +virtual-link'
                                          ' +(?P<addr>(\S+))(?: +(.*))?', line)
                            if q:
                                q_addr = str(q.groupdict()['addr'])

                                # Check parameters match
                                if q_addr == vl_addr:
                                    vl_transit_area_id = str(IPAddress(str(q.groupdict()['q_area'])))
                                    break

                    if vl_transit_area_id is not None:
                        intf_name = '{} {}'.format(vl_transit_area_id, router_id)
                        area = vl_transit_area_id
                elif intf_type == 'sham_links':
                    # Init
                    sl_local_id = None
                    sl_remote_id = None

                    # Execute command to get sham-link remote_id
                    cmd = 'show ip ospf sham-links | i {intf}'.format(intf=interface)
                    out = self.device.execute(cmd)

                    for line in out.splitlines():
                        line = line.rstrip()
                        # Sham Link OSPF_SL1 to address 10.151.22.22 is up
                        p = re.search('Sham +Link +(?P<intf>(\S+)) +to +address'
                                     ' +(?P<remote>(\S+)) +is +(up|down)', line)
                        if p:
                            if interface == str(p.groupdict()['intf']):
                                sl_remote_id = str(p.groupdict()['remote'])
                                break

                    # Execute command to get sham-link local_id
                    if sl_remote_id is not None:
                        cmd = 'show running-config | i sham-link | i {remote}'.format(remote=sl_remote_id)
                        out = self.device.execute(cmd)

                        for line in out.splitlines():
                            line = line.rstrip()
                            # area 1 sham-link 10.229.11.11 10.151.22.22 cost 111 ttl-security hops 3
                            q = re.search('area +(?P<q_area>(\d+)) +sham-link'
                                          ' +(?P<local_id>(\S+))'
                                          ' +(?P<remote_id>(\S+)) +(.*)', line)
                            if q:
                                q_area = str(IPAddress(str(q.groupdict()['q_area'])))
                                q_remote_id = str(q.groupdict()['remote_id'])

                                # Check parameters match
                                if q_area == area and q_remote_id == sl_remote_id:
                                    sl_local_id = str(q.groupdict()['local_id'])
                                    break

                    # Set intf_name based on parsed values
                    if sl_local_id is not None:
                        intf_name = '{} {}'.format(sl_local_id, sl_remote_id)

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
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if af not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family'][af] = {}
                if 'instance' not in ret_dict['vrf'][vrf]['address_family'][af]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance'] = {}
                if instance not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance] = {}
                if 'areas' not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area] = {}
                if intf_type not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][intf_type] = {}
                if intf_name not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area][intf_type]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][intf_type][intf_name] = {}
                
                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]['areas'][area]\
                            [intf_type][intf_name]
                # Delete variables to avoid overwrite issues for next intf
                del area
                del intf_name
                
                # Set values found in this regex
                sub_dict['router_id'] = router_id
                sub_dict['interface_type'] = interface_type
                if m.groupdict()['cost']:
                    sub_dict['cost'] = int(m.groupdict()['cost'])

                # Set defaault keys
                sub_dict['demand_circuit'] = False
                if 'bfd' not in sub_dict:
                    sub_dict['bfd'] = {}
                sub_dict['bfd']['enable'] = False

                # Set previously parsed keys
                try:
                    sub_dict['name'] = name
                    del name
                except Exception:
                    pass
                try:
                    sub_dict['ip_address'] = ip_address
                    del ip_address
                except Exception:
                    pass
                try:
                    sub_dict['interface_id'] = intf_id
                    del intf_id
                except Exception:
                    pass
                try:
                    sub_dict['attached'] = attached
                    del attached
                except Exception:
                    pass
                try:
                    sub_dict['enable'] = bool_dict[enable]
                except Exception:
                    pass
                try:
                    sub_dict['line_protocol'] = bool_dict[line_protocol]
                except Exception:
                    pass
                continue

            # Topology-MTID    Cost    Disabled    Shutdown      Topology Name
            #             0       1          no          no               Base
            p4 = re.compile(r'^(?P<mtid>(\d+)) +(?P<topo_cost>(\d+))'
                             ' +(?P<disabled>(yes|no)) +(?P<shutdown>(yes|no))'
                             ' +(?P<topo_name>(\S+))$')
            m = p4.match(line)
            if m:
                mtid = int(m.groupdict()['mtid'])
                if 'topology' not in sub_dict:
                    sub_dict['topology'] = {}
                if mtid not in sub_dict['topology']:
                    sub_dict['topology'][mtid] = {}
                sub_dict['topology'][mtid]['cost'] = int(m.groupdict()['topo_cost'])
                sub_dict['topology'][mtid]['name'] = str(m.groupdict()['topo_name'])
                if 'yes' in m.groupdict()['disabled']:
                    sub_dict['topology'][mtid]['disabled'] = True
                else:
                    sub_dict['topology'][mtid]['disabled'] = False
                if 'yes' in m.groupdict()['shutdown']:
                    sub_dict['topology'][mtid]['shutdown'] = True
                else:
                    sub_dict['topology'][mtid]['shutdown'] = False
                    continue

            # Configured as demand circuit
            p5 = re.compile(r'^Configured as demand circuit$')
            m = p5.match(line)
            if m:
                sub_dict['demand_circuit'] = True
                continue

            # Run as demand circuit
            p6 = re.compile(r'^Run as demand circuit$')
            m = p6.match(line)
            if m:
                sub_dict['demand_circuit'] = True
                continue

            # DoNotAge LSA not allowed (Number of DCbitless LSA is 1).
            p7 = re.compile(r'^DoNotAge +LSA +not +allowed +\(Number +of'
                              ' +DCbitless +LSA +is +(?P<num>(\d+))\)\.$')
            m = p7.match(line)
            if m:
                sub_dict['donotage_lsa'] = False
                sub_dict['total_dcbitless_lsa'] = int(m.groupdict()['num'])
                continue

            # Enabled by interface config, including secondary ip addresses
            p8 = re.compile(r'^Enabled +by +interface +config, +including'
                             ' +secondary +ip +addresses$')
            m = p8.match(line)
            if m:
                sub_dict['if_cfg'] = True
                continue

            # Transmit Delay is 1 sec, State POINT_TO_POINT
            # Transmit Delay is 1 sec, State DR, Priority 1
            # Transmit Delay is 1 sec, State DR, Priority 111, BFD enabled
            p9 = re.compile(r'^Transmit +Delay is +(?P<delay>(\d+)) +sec,'
                             ' +State +(?P<state>(\S+))'
                             '(?:, +Priority +(?P<priority>(\d+)))?'
                             '(?:, +BFD +(?P<bfd>(enabled|disabled)))?$')
            m = p9.match(line)
            if m:
                sub_dict['transmit_delay'] = int(m.groupdict()['delay'])
                state = str(m.groupdict()['state']).lower()
                state = state.replace("_", "-")
                sub_dict['state'] = state
                if m.groupdict()['priority']:
                    sub_dict['priority'] = int(m.groupdict()['priority'])
                if m.groupdict()['bfd']:
                    if 'bfd' not in sub_dict:
                        sub_dict['bfd'] = {}
                    if 'enabled' in m.groupdict()['bfd']:
                        sub_dict['bfd']['enable'] = True
                    else:
                        sub_dict['bfd']['enable'] = False
                        continue

            # Designated Router (ID) 10.36.3.3, Interface address 10.2.3.3
            p10 = re.compile(r'^Designated +(R|r)outer +\(ID\)'
                             ' +(?P<dr_router_id>(\S+)), +(I|i)nterface'
                             ' +(A|a)ddress +(?P<dr_ip_addr>(\S+))$')
            m = p10.match(line)
            if m:
                sub_dict['dr_router_id'] = str(m.groupdict()['dr_router_id'])
                sub_dict['dr_ip_addr'] = str(m.groupdict()['dr_ip_addr'])
                continue

            # Backup Designated router (ID) 10.16.2.2, Interface address 10.2.3.2
            p11 = re.compile(r'^Backup +(D|d)esignated +(R|r)outer +\(ID\)'
                             ' +(?P<bdr_router_id>(\S+)), +(I|i)nterface'
                             ' +(A|a)ddress +(?P<bdr_ip_addr>(\S+))$')
            m = p11.match(line)
            if m:
                sub_dict['bdr_router_id'] = str(m.groupdict()['bdr_router_id'])
                sub_dict['bdr_ip_addr'] = str(m.groupdict()['bdr_ip_addr'])
                continue

            # Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
            p12 = re.compile(r'^Timer +intervals +configured,'
                             ' +Hello +(?P<hello>(\d+)),'
                             ' +Dead +(?P<dead>(\d+)),'
                             ' +Wait +(?P<wait>(\d+)),'
                             ' +Retransmit +(?P<retransmit>(\d+))$')
            m = p12.match(line)
            if m:
                sub_dict['hello_interval'] = int(m.groupdict()['hello'])
                sub_dict['dead_interval'] = int(m.groupdict()['dead'])
                sub_dict['wait_interval'] = int(m.groupdict()['wait'])
                sub_dict['retransmit_interval'] = int(m.groupdict()['retransmit'])
                continue

            #  oob-resync timeout 40
            p12_1 = re.compile(r'^oob-resync +timeout +(?P<oob>(\d+))$')
            m = p12_1.match(line)
            if m:
                sub_dict['oob_resync_timeout'] = int(m.groupdict()['oob'])
                continue
            
            # Hello due in 00:00:00
            p12_2 = re.compile(r'^Hello +due +in +(?P<hello_timer>(\S+))$')
            m = p12_2.match(line)
            if m:
                sub_dict['passive'] = False
                sub_dict['hello_timer'] = str(m.groupdict()['hello_timer'])
                continue

            # Supports Link-local Signaling (LLS)
            p13 = re.compile(r'^Supports +Link-local +Signaling +\(LLS\)$')
            m = p13.match(line)
            if m:
                sub_dict['lls'] = True
                continue
            
            # Cisco NSF helper support enabled
            # IETF NSF helper support enabled
            p14 = re.compile(r'^(?P<gr_type>(Cisco|IETF)) +NSF +helper +support'
                              ' +(?P<helper>(enabled|disabled))$')
            m = p14.match(line)
            if m:
                gr_type = str(m.groupdict()['gr_type']).lower()
                if 'graceful_restart' not in sub_dict:
                    sub_dict['graceful_restart'] = {}
                if gr_type not in sub_dict['graceful_restart']:
                    sub_dict['graceful_restart'][gr_type] = {}
                sub_dict['graceful_restart'][gr_type]['type'] = gr_type
                if 'enabled' in m.groupdict()['helper']:
                    sub_dict['graceful_restart'][gr_type]['helper'] = True
                else:
                    sub_dict['graceful_restart'][gr_type]['helper'] = False
                continue

            # Index 2/2, flood queue length 0
            p15 = re.compile(r'^Index +(?P<index>(\S+)),'
                               ' +flood +queue +length +(?P<length>(\d+))$')
            m = p15.match(line)
            if m:
                sub_dict['index'] = str(m.groupdict()['index'])
                sub_dict['flood_queue_length'] = int(m.groupdict()['length'])
                continue

            # Next 0(0)/0(0)
            p16 = re.compile(r'^Next +(?P<next>(\S+))$')
            m = p16.match(line)
            if m:
                sub_dict['next'] = str(m.groupdict()['next'])
                continue

            # Last flood scan length is 0, maximum is 11
            p17 = re.compile(r'^Last +flood +scan +length +is +(?P<num>(\d+)),'
                              ' +maximum +is +(?P<max>(\d+))$')
            m = p17.match(line)
            if m:
                sub_dict['last_flood_scan_length'] = int(m.groupdict()['num'])
                sub_dict['max_flood_scan_length'] = int(m.groupdict()['max'])
                continue

            # Last flood scan time is 0 msec, maximum is 1 msec
            p18 = re.compile(r'^Last +flood +scan +time +is +(?P<time1>(\d+))'
                              ' +msec, +maximum +is +(?P<time2>(\d+)) +msec$')
            m = p18.match(line)
            if m:
                sub_dict['last_flood_scan_time_msec'] = \
                    int(m.groupdict()['time1'])
                sub_dict['max_flood_scan_time_msec'] = \
                    int(m.groupdict()['time2'])
                continue

            # Neighbor Count is 1, Adjacent neighbor count is 1
            p19 = re.compile(r'^Neighbor +Count +is +(?P<nbr_count>(\d+)),'
                              ' +Adjacent +neighbor +count +is'
                              ' +(?P<adj_nbr_count>(\d+))$')
            m = p19.match(line)
            if m:
                if 'statistics' not in sub_dict:
                    sub_dict['statistics'] = {}
                sub_dict['statistics']['nbr_count'] = \
                    int(m.groupdict()['nbr_count'])
                sub_dict['statistics']['adj_nbr_count'] = \
                    int(m.groupdict()['adj_nbr_count'])
                continue

            # Adjacent with neighbor 10.16.2.2 (Backup Designated Router)
            p20_1 = re.compile(r'^Adjacent +with +neighbor +(?P<nbr>(\S+))'
                              ' +\((B|b)ackup +(D|d)esignated +(R|r)outer\)$')
            m = p20_1.match(line)
            if m:
                neighbor = str(m.groupdict()['nbr'])
                if 'neighbors' not in sub_dict:
                    sub_dict['neighbors'] = {}
                if neighbor not in sub_dict['neighbors']:
                    sub_dict['neighbors'][neighbor] = {}
                sub_dict['neighbors'][neighbor]['bdr_router_id'] = neighbor
                continue

            # Adjacent with neighbor 10.36.3.3 (Designated Router)
            p20_2 = re.compile(r'^Adjacent +with +neighbor +(?P<nbr>(\S+))'
                              ' +\((D|d)esignated +(R|r)outer\)$')
            m = p20_2.match(line)
            if m:
                neighbor = str(m.groupdict()['nbr'])
                if 'neighbors' not in sub_dict:
                    sub_dict['neighbors'] = {}
                if neighbor not in sub_dict['neighbors']:
                    sub_dict['neighbors'][neighbor] = {}
                sub_dict['neighbors'][neighbor]['dr_router_id'] = neighbor
                continue

            # Adjacent with neighbor 10.64.4.4 (Hello suppressed)
            p20_3 = re.compile(r'^Adjacent +with +neighbor +(?P<nbr>(\S+))'
                              ' +\(Hello suppressed\)$')
            m = p20_3.match(line)
            if m:
                neighbor = str(m.groupdict()['nbr'])
                if 'neighbors' not in sub_dict:
                    sub_dict['neighbors'] = {}
                if neighbor not in sub_dict['neighbors']:
                    sub_dict['neighbors'][neighbor] = {}
                continue

            # Suppress hello for 0 neighbor(s)
            p21 = re.compile(r'^Suppress +hello +for +(?P<sup>(\d+))'
                              ' +neighbor\(s\)$')
            m = p21.match(line)
            if m:
                if 'statistics' not in sub_dict:
                    sub_dict['statistics'] = {}
                sub_dict['statistics']['num_nbrs_suppress_hello'] = \
                    int(m.groupdict()['sup'])
                continue

            # Loopback interface is treated as a stub Host
            p22 = re.compile(r'^Loopback +interface +is +treated +as +a +stub'
                              ' +Host$')
            m = p22.match(line)
            if m:
                sub_dict['stub_host'] = True
                continue

            # Can be protected by per-prefix Loop-Free FastReroute
            p23 = re.compile(r'^Can +be +protected +by per-+prefix +Loop-Free'
                              ' +FastReroute$')
            m = p23.match(line)
            if m:
                sub_dict['ipfrr_protected'] = True
                continue

            # Can be used for per-prefix Loop-Free FastReroute repair paths
            p24 = re.compile(r'^Can +be +used +for +per-prefix +Loop-Free'
                              ' +FastReroute +repair +paths$')
            m = p24.match(line)
            if m:
                sub_dict['ipfrr_candidate'] = True
                continue

            # Not Protected by per-prefix TI-LFA
            p25 = re.compile(r'^Not +Protected +by +per-prefix +TI-LFA$')
            m = p25.match(line)
            if m:
                sub_dict['ti_lfa_protected'] = False
                continue

            # Prefix-suppression is enabled
            p26 = re.compile(r'^Prefix-suppression +is +(?P<ps>(enabled|disabled))$')
            m = p26.match(line)
            if m:
                if 'enabled' in m.groupdict()['ps']:
                    sub_dict['prefix_suppression'] = True
                else:
                    sub_dict['prefix_suppression'] = False

            # Strict TTL checking enabled, up to 3 hops allowed
            p27 = re.compile(r'^Strict +TTL +checking'
                             ' +(?P<strict_ttl>(enabled|disabled))'
                             '(?:, +up +to +(?P<hops>(\d+)) +hops +allowed)?$')
            m = p27.match(line)
            if m:
                if 'ttl_security' not in sub_dict:
                    sub_dict['ttl_security'] = {}
                if 'enabled' in m.groupdict()['strict_ttl']:
                    sub_dict['ttl_security']['enable'] = True
                else:
                    sub_dict['ttl_security']['enable'] = False
                if m.groupdict()['hops']:
                    sub_dict['ttl_security']['hops'] = int(m.groupdict()['hops'])
                    continue

            # Simple password authentication enabled
            p28_1 = re.compile(r'^Simple +password +authentication +enabled$')
            m = p28_1.match(line)
            if m:
                if 'authentication' not in sub_dict:
                    sub_dict['authentication'] = {}
                if 'auth_trailer_key' not in sub_dict['authentication']:
                    sub_dict['authentication']['auth_trailer_key'] = {}
                sub_dict['authentication']['auth_trailer_key']\
                    ['crypto_algorithm'] = 'simple'
                continue

            # Cryptographic authentication enabled
            p28_2 = re.compile(r'^Cryptographic +authentication +enabled$')
            m = p28_2.match(line)
            if m:
                if 'authentication' not in sub_dict:
                    sub_dict['authentication'] = {}
                if 'auth_trailer_key' not in sub_dict['authentication']:
                    sub_dict['authentication']['auth_trailer_key'] = {}
                sub_dict['authentication']['auth_trailer_key']\
                    ['crypto_algorithm'] = 'md5'
                continue

            # Youngest key id is 2
            p28_3 = re.compile(r'^Youngest +key +id +is +(?P<id>(\d+))$')
            m = p28_3.match(line)
            if m:
                if 'authentication' not in sub_dict:
                    sub_dict['authentication'] = {}
                if 'auth_trailer_key' not in sub_dict['authentication']:
                    sub_dict['authentication']['auth_trailer_key'] = {}
                sub_dict['authentication']['auth_trailer_key']\
                    ['youngest_key_id'] = int(m.groupdict()['id'])
                continue
            
            # Rollover in progress, 1 neighbor(s) using the old key(s):
            p28_4 = re.compile(r'^Rollover +in +progress, +(?P<num>(\d+))'
                                ' +neighbor(s) +using +the +old +key(s):$')
            m = p28_4.match(line)
            if m:
                continue

            # key id 1 algorithm MD5
            p28_5 = re.compile(r'^key +id +1 +algorithm +MD5$')
            m = p28_5.match(line)
            if m:
                if 'authentication' not in sub_dict:
                    sub_dict['authentication'] = {}
                if 'auth_trailer_key' not in sub_dict['authentication']:
                    sub_dict['authentication']['auth_trailer_key'] = {}
                sub_dict['authentication']['auth_trailer_key']\
                    ['crypto_algorithm'] = 'md5'
                continue

        return ret_dict


# ================================
# Super parser for:
#   * 'show ip ospf virtual-links'
#   * 'show ip ospf sham-links'
# ================================
class ShowIpOspfLinksParser(MetaParser):

    ''' Parser for:
        * 'show ip ospf virtual-links'
        * 'show ip ospf sham-links'
    '''

    def cli(self, cmd, link_type,output=None):

        assert link_type in ['virtual_links', 'sham_links']

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output
        
        # Init vars
        ret_dict = {}
        af = 'ipv4'

        # crypo_algorithm dict
        crypto_dict = {'cryptographic': 'md5', 'simple password': 'simple'}

        for line in out.splitlines():
            line = line.strip()

            # Sham Link OSPF_SL0 to address 10.151.22.22 is up
            # Virtual Link OSPF_VL0 to router 10.64.4.4 is up
            p1 = re.compile(r'^(Virtual|Sham) +Link +(?P<interface>(\S+)) +to'
                             ' +(address|router) +(?P<address>(\S+)) +is'
                             ' +(?P<link_state>(up|down))$')
            m = p1.match(line)
            if m:
                address = str(m.groupdict()['address'])
                sl_remote_id = vl_router_id = address
                interface = str(m.groupdict()['interface'])
                link_state = str(m.groupdict()['link_state'])
                instance = None
                
                # Get link name
                n = re.match('(?P<ignore>\S+)_(?P<name>(S|V)L(\d+))', interface)
                if n:
                    real_link_name = str(n.groupdict()['name'])
                else:
                    real_link_name = interface
                
                # Get OSPF process ID from 'show ip ospf interface'
                cmd = 'show ip ospf interface | section {}'.format(interface)
                out = self.device.execute(cmd)

                for line in out.splitlines():
                    line = line.rstrip()

                    # Process ID 2, Router ID 10.229.11.11, Network Type SHAM_LINK, Cost: 111
                    p = re.search('Process +ID +(?P<instance>(\S+)), +Router'
                                  ' +(.*)', line)
                    if p:
                        instance = str(p.groupdict()['instance'])
                        break

                # Get VRF information using the ospf instance
                if instance is not None:
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

                # Build dict
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if af not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family'][af] = {}
                if 'instance' not in ret_dict['vrf'][vrf]['address_family'][af]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance'] = {}
                if instance not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance] = {}
                continue


            # Area 1, source address 10.21.33.33
            # Area 1 source address 10.229.11.11
            p2 = re.compile(r'^Area +(?P<area>(\S+)),? +source +address'
                             ' +(?P<source_address>(\S+))$')
            m = p2.match(line)
            if m:
                area = str(IPAddress(str(m.groupdict()['area'])))
                source_address = str(m.groupdict()['source_address'])

                # Set link_name for sham_link
                link_name = '{} {}'.format(source_address, sl_remote_id)

                # Build dict
                if 'areas' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area] = {}
                if link_type not in  ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][link_type] = {}
                if link_name not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area][link_type]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][link_type][link_name] = {}

                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]['areas'][area]\
                            [link_type][link_name]

                # Set values
                sub_dict['transit_area_id'] = area
                sub_dict['local_id'] = source_address
                sub_dict['demand_circuit'] = False

                # Set previously parsed values
                try:
                    sub_dict['name'] = real_link_name
                    sub_dict['remote_id'] = sl_remote_id
                    sub_dict['link_state'] = link_state
                except Exception:
                    pass
                continue

            # Run as demand circuit
            p3 = re.compile(r'^Run +as +demand +circuit$')
            m = p3.match(line)
            if m:
                if link_type == 'sham_links':
                    sub_dict['demand_circuit'] = True
                else:
                    demand_circuit = True
                continue

            # DoNotAge LSA not allowed (Number of DCbitless LSA is 7).
            # DoNotAge LSA not allowed (Number of DCbitless LSA is 1). Cost of using 111 State POINT_TO_POINT,
            p4 = re.compile(r'^DoNotAge +LSA +not +allowed'
                             ' +\(Number +of +DCbitless +LSA +is +(?P<dcbitless>(\d+))\).'
                             '(?: +Cost +of +using +(?P<cost>(\d+)))?'
                             '(?: State +(?P<state>(\S+)))?$')
            m = p4.match(line)
            if m:
                dcbitless_lsa_count = int(m.groupdict()['dcbitless'])
                donotage_lsa = 'not allowed'
                if m.groupdict()['cost']:
                    cost = int(m.groupdict()['cost'])
                if m.groupdict()['state']:
                    link_state =  str(m.groupdict()['state']).lower()

                # Set values for sham_links
                if link_type == 'sham_links':
                    sub_dict['dcbitless_lsa_count'] = dcbitless_lsa_count
                    sub_dict['donotage_lsa'] = donotage_lsa
                    if m.groupdict()['cost']:
                        sub_dict['cost'] = cost
                    if m.groupdict()['state']:
                        sub_dict['state'] = link_state
                    continue

            # Transit area 1
            # Transit area 1, via interface GigabitEthernet0/1
            p5 = re.compile(r'^Transit +area +(?P<area>(\S+)),'
                             '(?: +via +interface +(?P<intf>(\S+)))?$')
            m = p5.match(line)
            if m:
                area = str(IPAddress(str(m.groupdict()['area'])))

                # Set link_name for virtual_link
                link_name = '{} {}'.format(area, vl_router_id)

                # Create dict
                if 'areas' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area] = {}
                if link_type not in  ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][link_type] = {}
                if link_name not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area][link_type]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][link_type][link_name] = {}

                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]['areas'][area]\
                            [link_type][link_name]

                # Set values
                sub_dict['transit_area_id'] = area
                sub_dict['demand_circuit'] = False
                if m.groupdict()['intf']:
                    sub_dict['interface'] = str(m.groupdict()['intf'])

                # Set previously parsed values
                try:
                    sub_dict['name'] = real_link_name
                except Exception:
                    pass
                try:
                    sub_dict['router_id'] = vl_router_id
                except Exception:
                    pass
                try:
                    sub_dict['dcbitless_lsa_count'] = dcbitless_lsa_count
                except Exception:
                    pass
                try:
                    sub_dict['donotage_lsa'] = donotage_lsa
                except Exception:
                    pass
                try:
                    sub_dict['demand_circuit'] = demand_circuit
                except Exception:
                    pass
                try:
                    sub_dict['link_state'] = link_state
                except Exception:
                    pass
                continue

            # Topology-MTID    Cost    Disabled     Shutdown      Topology Name
            #             0       1          no           no               Base
            p6 = re.compile(r'^(?P<mtid>(\d+)) +(?P<topo_cost>(\d+))'
                             ' +(?P<disabled>(yes|no)) +(?P<shutdown>(yes|no))'
                             ' +(?P<topo_name>(\S+))$')
            m = p6.match(line)
            if m:
                mtid = int(m.groupdict()['mtid'])
                if 'topology' not in sub_dict:
                    sub_dict['topology'] = {}
                if mtid not in sub_dict['topology']:
                    sub_dict['topology'][mtid] = {}
                sub_dict['topology'][mtid]['cost'] = int(m.groupdict()['topo_cost'])
                sub_dict['topology'][mtid]['name'] = str(m.groupdict()['topo_name'])
                if 'yes' in m.groupdict()['disabled']:
                    sub_dict['topology'][mtid]['disabled'] = True
                else:
                    sub_dict['topology'][mtid]['disabled'] = False
                if 'yes' in m.groupdict()['shutdown']:
                    sub_dict['topology'][mtid]['shutdown'] = True
                else:
                    sub_dict['topology'][mtid]['shutdown'] = False
                    continue
            
            # Transmit Delay is 1 sec, State POINT_TO_POINT,
            p7 = re.compile(r'^Transmit +Delay +is +(?P<transmit_delay>(\d+))'
                             ' +sec, +State +(?P<state>(\S+)),?$')
            m = p7.match(line)
            if m:
                sub_dict['transmit_delay'] = int(m.groupdict()['transmit_delay'])
                state = str(m.groupdict()['state']).lower()
                state = state.replace("_", "-")
                sub_dict['state'] = state
                continue

            # Timer intervals configured, Hello 3, Dead 13, Wait 13, Retransmit 5
            # Timer intervals configured, Hello 4, Dead 16, Wait 16, Retransmit 44
            # Timer intervals configured, Hello 10, Dead 40, Wait 40,
            p8 = re.compile(r'^Timer +intervals +configured,'
                             ' +Hello +(?P<hello>(\d+)),'
                             ' +Dead +(?P<dead>(\d+)),'
                             ' +Wait +(?P<wait>(\d+)),'
                             '(?: +Retransmit +(?P<retransmit>(\d+)))?$')
            m = p8.match(line)
            if m:
                if m.groupdict()['hello']:
                    sub_dict['hello_interval'] = int(m.groupdict()['hello'])
                if m.groupdict()['dead']:
                    sub_dict['dead_interval'] = int(m.groupdict()['dead'])
                if m.groupdict()['wait']:
                    sub_dict['wait_interval'] = int(m.groupdict()['wait'])
                if m.groupdict()['retransmit']:
                    sub_dict['retransmit_interval'] = int(m.groupdict()['retransmit'])
                continue

            # Strict TTL checking enabled, up to 3 hops allowed
            p9 = re.compile(r'^Strict +TTL +checking'
                             ' +(?P<strict_ttl>(enabled|disabled))'
                             '(?:, +up +to +(?P<hops>(\d+)) +hops +allowed)?$')
            m = p9.match(line)
            if m:
                if 'ttl_security' not in sub_dict:
                    sub_dict['ttl_security'] = {}
                if 'enabled' in m.groupdict()['strict_ttl']:
                    sub_dict['ttl_security']['enable'] = True
                else:
                    sub_dict['ttl_security']['enable'] = False
                if m.groupdict()['hops']:
                    sub_dict['ttl_security']['hops'] = int(m.groupdict()['hops'])
                    continue

            # Hello due in 00:00:03:179
            p10 = re.compile(r'^Hello +due +in +(?P<hello_timer>(\S+))$')
            m = p10.match(line)
            if m:
                sub_dict['hello_timer'] = str(m.groupdict()['hello_timer'])
                continue          
          
            # Adjacency State FULL
            p11 = re.compile(r'^Adjacency +State +(?P<adj_state>(\S+))$')
            m = p11.match(line)
            if m:
                sub_dict['adjacency_state'] = str(m.groupdict()['adj_state']).lower()
                continue

            # Index 1/2/2, retransmission queue length 0, number of retransmission 2
            p12 = re.compile(r'^Index +(?P<index>(\S+)), +retransmission +queue'
                              ' +length +(?P<length>(\d+)), +number +of'
                              ' +retransmission +(?P<retrans>(\d+))$')
            m = p12.match(line)
            if m:
                sub_dict['index'] = str(m.groupdict()['index'])
                sub_dict['retrans_qlen'] = int(m.groupdict()['length'])
                sub_dict['total_retransmission'] = int(m.groupdict()['retrans'])
                continue

            # First 0x0(0)/0x0(0)/0x0(0) Next 0x0(0)/0x0(0)/0x0(0)
            p13 = re.compile(r'^First +(?P<first>(\S+)) +Next +(?P<next>(\S+))$')
            m = p13.match(line)
            if m:
                sub_dict['first'] = str(m.groupdict()['first'])
                sub_dict['next'] = str(m.groupdict()['next'])
                continue

            # Last retransmission scan length is 1, maximum is 1
            p14 = re.compile(r'^Last +retransmission +scan +length +is'
                              ' +(?P<len>(\d+)), +maximum +is +(?P<max>(\d+))$')
            m = p14.match(line)
            if m:
                sub_dict['last_retransmission_scan_length'] = \
                    int(m.groupdict()['len'])
                sub_dict['last_retransmission_max_length'] = \
                    int(m.groupdict()['max'])
                continue

            # Last retransmission scan time is 0 msec, maximum is 0 msec
            p15 = re.compile(r'^Last +retransmission +scan +time +is'
                              ' +(?P<time>(\d+)) +msec, +maximum +is'
                              ' +(?P<max>(\d+)) +msec$')
            m = p15.match(line)
            if m:
                sub_dict['last_retransmission_scan_time'] = \
                    int(m.groupdict()['time'])
                sub_dict['last_retransmission_max_scan'] = \
                    int(m.groupdict()['max'])
                continue

        return ret_dict


# =============================
# Schema for:
#   * 'show ip ospf sham-links'
# =============================
class ShowIpOspfShamLinksSchema(MetaParser):

    ''' Schema for:
        * 'show ip ospf sham-links'
    '''

    schema = {
        'vrf':
            {Any():
                {'address_family':
                    {Any():
                        {'instance':
                            {Any():
                                {'areas':
                                    {Any():
                                        {'sham_links':
                                            {Any():
                                                {'name': str,
                                                'link_state': str,
                                                'local_id': str,
                                                'remote_id': str,
                                                'transit_area_id': str,
                                                Optional('hello_interval'): int,
                                                Optional('dead_interval'): int,
                                                Optional('wait_interval'): int,
                                                Optional('retransmit_interval'): int,
                                                Optional('transmit_delay'): int,
                                                'cost': int,
                                                'state': str,
                                                Optional('hello_timer'): str,
                                                Optional('demand_circuit'): bool,
                                                Optional('dcbitless_lsa_count'): int,
                                                Optional('donotage_lsa'): str,
                                                Optional('adjacency_state'): str,
                                                Optional('ttl_security'):
                                                    {'enable': bool,
                                                    Optional('hops'): int},
                                                    Optional('index'): str,
                                                    Optional('first'): str,
                                                    Optional('next'): str,
                                                    Optional('last_retransmission_max_length'): int,
                                                    Optional('last_retransmission_max_scan'): int,
                                                    Optional('last_retransmission_scan_length'): int,
                                                    Optional('last_retransmission_scan_time'): int,
                                                    Optional('total_retransmission'): int,
                                                    Optional('retrans_qlen'): int,
                                                    Optional('topology'):
                                                        {Any():
                                                            {'cost': int,
                                                            'disabled': bool,
                                                            'shutdown': bool,
                                                            'name': str,
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
                },
            }


# =============================
# Parser for:
#   * 'show ip ospf sham-links'
# =============================
class ShowIpOspfShamLinks(ShowIpOspfShamLinksSchema, ShowIpOspfLinksParser):

    ''' Parser for:
        * 'show ip ospf sham-links'
    '''

    cli_command = 'show ip ospf sham-links'

    def cli(self, output=None):

        return super().cli(cmd=self.cli_command, link_type='sham_links',output=output)


# ================================
# Schema for:
#   * 'show ip ospf virtual-links'
# ================================
class ShowIpOspfVirtualLinksSchema(MetaParser):

    ''' Schema for:
        * 'show ip ospf virtual-links'
    '''

    schema = {
        'vrf':
            {Any():
                {'address_family':
                    {Any():
                        {'instance':
                            {Any():
                                {'areas':
                                    {Any():
                                        {'virtual_links':
                                            {Any():
                                                {'name': str,
                                                'link_state': str,
                                                'router_id': str,
                                                'transit_area_id': str,
                                                Optional('hello_interval'): int,
                                                Optional('dead_interval'): int,
                                                Optional('wait_interval'): int,
                                                Optional('retransmit_interval'): int,
                                                'transmit_delay': int,
                                                'state': str,
                                                'demand_circuit': bool,
                                                Optional('cost'): int,
                                                Optional('hello_timer'): str,
                                                Optional('interface'): str,
                                                Optional('dcbitless_lsa_count'): int,
                                                Optional('donotage_lsa'): str,
                                                Optional('adjacency_state'): str,
                                                Optional('ttl_security'):
                                                    {'enable': bool,
                                                    Optional('hops'): int},
                                                    Optional('index'): str,
                                                    Optional('first'): str,
                                                    Optional('next'): str,
                                                    Optional('last_retransmission_max_length'): int,
                                                    Optional('last_retransmission_max_scan'): int,
                                                    Optional('last_retransmission_scan_length'): int,
                                                    Optional('last_retransmission_scan_time'): int,
                                                    Optional('total_retransmission'): int,
                                                    Optional('retrans_qlen'): int,
                                                    Optional('topology'):
                                                        {Any():
                                                            {'cost': int,
                                                            'disabled': bool,
                                                            'shutdown': bool,
                                                            'name': str,
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
                },
            }


# ================================
# Parser for:
#   * 'show ip ospf virtual-links'
# ================================
class ShowIpOspfVirtualLinks(ShowIpOspfVirtualLinksSchema, ShowIpOspfLinksParser):

    ''' Parser for:
        * 'show ip ospf virtual-links'
    '''

    cli_command = 'show ip ospf virtual-links'

    def cli(self, output=None):

        return super().cli(cmd=self.cli_command, link_type='virtual_links', output=output)


# ==================================
# Schema for:
#   * 'show ip ospf neighbor detail'
# =========================================
class ShowIpOspfNeighborDetailSchema(MetaParser):

    ''' Schema for:
        * 'show ip ospf neighbor detail'
    '''

    schema = {
        'vrf': 
            {Any():
                {'address_family':
                    {Any():
                        {'instance':
                            {Any():
                                {'areas': 
                                    {Any(): 
                                        {Optional('interfaces'): 
                                            {Any(): 
                                                {'neighbors': 
                                                    {Any(): 
                                                        {'neighbor_router_id': str,
                                                        'address': str,
                                                        'interface': str,
                                                        'priority': int,
                                                        'state': str,
                                                        'dr_ip_addr': str,
                                                        'bdr_ip_addr': str,
                                                        Optional('interface_id'): str,
                                                        Optional('hello_options'): str,
                                                        Optional('dbd_options'): str,
                                                        Optional('dead_timer'): str,
                                                        Optional('uptime'): str,
                                                        Optional('index'): str,
                                                        Optional('first'): str,
                                                        Optional('next'): str,
                                                        Optional('ls_ack_list'): str,
                                                        Optional('statistics'): 
                                                            {Optional('nbr_event_count'): int,
                                                            Optional('nbr_retrans_qlen'): int,
                                                            Optional('total_retransmission'): int,
                                                            Optional('last_retrans_scan_length'): int,
                                                            Optional('last_retrans_max_scan_length'): int,
                                                            Optional('last_retrans_scan_time_msec'): int,
                                                            Optional('last_retrans_max_scan_time_msec'): int},
                                                        },
                                                    },
                                                },
                                            },
                                        Optional('sham_links'): 
                                            {Any(): 
                                                {'neighbors': 
                                                    {Any(): 
                                                        {'neighbor_router_id': str,
                                                        'address': str,
                                                        'interface': str,
                                                        'priority': int,
                                                        'state': str,
                                                        'dr_ip_addr': str,
                                                        'bdr_ip_addr': str,
                                                        Optional('interface_id'): str,
                                                        Optional('hello_options'): str,
                                                        Optional('dbd_options'): str,
                                                        Optional('dead_timer'): str,
                                                        Optional('uptime'): str,
                                                        Optional('index'): str,
                                                        Optional('first'): str,
                                                        Optional('next'): str,
                                                        Optional('ls_ack_list'): str,
                                                        Optional('statistics'): 
                                                            {Optional('nbr_event_count'): int,
                                                            Optional('nbr_retrans_qlen'): int,
                                                            Optional('total_retransmission'): int,
                                                            Optional('last_retrans_scan_length'): int,
                                                            Optional('last_retrans_max_scan_length'): int,
                                                            Optional('last_retrans_scan_time_msec'): int,
                                                            Optional('last_retrans_max_scan_time_msec'): int},
                                                        },
                                                    },
                                                },
                                            },
                                        Optional('virtual_links'): 
                                            {Any(): 
                                                {'neighbors': 
                                                    {Any(): 
                                                        {'neighbor_router_id': str,
                                                        'address': str,
                                                        'interface': str,
                                                        'priority': int,
                                                        'state': str,
                                                        'dr_ip_addr': str,
                                                        'bdr_ip_addr': str,
                                                        Optional('interface_id'): str,
                                                        Optional('hello_options'): str,
                                                        Optional('dbd_options'): str,
                                                        Optional('dead_timer'): str,
                                                        Optional('uptime'): str,
                                                        Optional('index'): str,
                                                        Optional('first'): str,
                                                        Optional('next'): str,
                                                        Optional('ls_ack_list'): str,
                                                        Optional('statistics'): 
                                                            {Optional('nbr_event_count'): int,
                                                            Optional('nbr_retrans_qlen'): int,
                                                            Optional('total_retransmission'): int,
                                                            Optional('last_retrans_scan_length'): int,
                                                            Optional('last_retrans_max_scan_length'): int,
                                                            Optional('last_retrans_scan_time_msec'): int,
                                                            Optional('last_retrans_max_scan_time_msec'): int},
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
            },
        }


# ================================
# Parser for:
#   'show ip ospf neighbor detail'
# ================================
class ShowIpOspfNeighborDetail(ShowIpOspfNeighborDetailSchema):

    ''' Parser for:
        * 'show ip ospf neighbor detail'
    '''

    cli_command = 'show ip ospf neighbor detail'

    def cli(self, output=None):

        if output is None:
            # Execute command on device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}
        af = 'ipv4' # this is ospf - always ipv4

        for line in out.splitlines():
            line = line.strip()

            # Neighbor 10.16.2.2, interface address 10.1.2.2
            # Neighbor 192.168.111.1, interface address 192.168.70.1, interface-id 192
            # Neighbor 192.168.255.9, interface address 10.0.109.9, interface-id unknown
            p1 = re.compile(r'^Neighbor +(?P<neighbor>(\S+)), +interface'
                             ' +address +(?P<address>(\S+))'
                             '(?:, +interface-id +(?P<intf_id>(\S+)))?$')
            m = p1.match(line)
            if m:
                neighbor = str(m.groupdict()['neighbor'])
                address = str(m.groupdict()['address'])
                if m.groupdict()['intf_id']:
                    interface_id = str(m.groupdict()['intf_id'])
                continue

            # In the area 0 via interface GigabitEthernet2
            p2 = re.compile(r'^In +the +area +(?P<area>(\S+)) +via +interface'
                             ' +(?P<interface>(\S+))$')
            m = p2.match(line)
            if m:
                area = str(IPAddress(str(m.groupdict()['area'])))
                interface = str(m.groupdict()['interface'])
                instance = None
                router_id = None

                # Get OSPF process ID from 'show ip ospf interface'
                cmd = 'show ip ospf interface | section {}'.format(interface)
                out = self.device.execute(cmd)

                for line in out.splitlines():
                    line = line.rstrip()

                    # Process ID 2, Router ID 10.229.11.11, Network Type SHAM_LINK, Cost: 111
                    p = re.search('Process +ID +(?P<instance>(\S+)), +Router +ID'
                                  ' +(?P<router_id>(\S+)) +(.*)', line)
                    if p:
                        instance = str(p.groupdict()['instance'])
                        router_id = str(p.groupdict()['router_id'])
                        break

                # Get VRF information using the ospf instance
                if instance is not None:
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

                # Build dict
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if af not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family'][af] = {}
                if 'instance' not in ret_dict['vrf'][vrf]['address_family'][af]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance'] = {}
                if instance not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance] = {}

                # Determine if 'interface' or 'virtual_links' or 'sham_links'
                if re.search('VL', interface):
                    # Init
                    intf_type = 'virtual_links'
                    vl_addr = None
                    vl_transit_area_id = None

                    # Execute command to get virtual-link address
                    cmd = 'show ip ospf virtual-links | i {intf}'.format(intf=interface)
                    out = self.device.execute(cmd)

                    for line in out.splitlines():
                        line = line.rstrip()
                        # Virtual Link OSPF_VL0 to router 10.100.5.5 is down
                        p = re.search('Virtual +Link +(?P<intf>(\S+)) +to +router'
                                     ' +(?P<address>(\S+)) +is +(up|down)'
                                     '(?:.*)?', line)
                        if p:
                            if interface == str(p.groupdict()['intf']):
                                vl_addr = str(p.groupdict()['address'])
                                break

                    # Execute command to get virtual-link transit_area_id
                    if vl_addr is not None and router_id is not None:
                        cmd = 'show running-config | i virtual-link | i {addr}'.format(addr=vl_addr)
                        out = self.device.execute(cmd)

                        for line in out.splitlines():
                            line = line.rstrip()
                            #  area 1 virtual-link 10.100.5.5
                            q = re.search('area +(?P<q_area>(\d+)) +virtual-link'
                                          ' +(?P<addr>(\S+))(?: +(.*))?', line)
                            if q:
                                q_addr = str(q.groupdict()['addr'])
                                # Check parameters match
                                if q_addr == vl_addr:
                                    vl_transit_area_id = str(IPAddress(str(q.groupdict()['q_area'])))
                                    break

                    if vl_transit_area_id is not None:
                        intf_name = '{} {}'.format(vl_transit_area_id, router_id)
                        area = vl_transit_area_id
                elif re.search('SL', interface):
                    # Init
                    intf_type = 'sham_links'
                    sl_local_id = None
                    sl_remote_id = None

                    # Execute command to get sham-link remote_id
                    cmd = 'show ip ospf sham-links | i {intf}'.format(intf=interface)
                    out = self.device.execute(cmd)

                    for line in out.splitlines():
                        line = line.rstrip()
                        # Sham Link OSPF_SL1 to address 10.151.22.22 is up
                        p = re.search('Sham +Link +(?P<intf>(\S+)) +to +address'
                                     ' +(?P<remote>(\S+)) +is +(up|down)', line)
                        if p:
                            if interface == str(p.groupdict()['intf']):
                                sl_remote_id = str(p.groupdict()['remote'])
                                break

                    # Execute command to get sham-link local_id
                    if sl_remote_id is not None:
                        cmd = 'show running-config | i sham-link | i {remote}'.format(remote=sl_remote_id)
                        out = self.device.execute(cmd)

                        for line in out.splitlines():
                            line = line.rstrip()
                            # area 1 sham-link 10.229.11.11 10.151.22.22 cost 111 ttl-security hops 3
                            q = re.search('area +(?P<q_area>(\d+)) +sham-link'
                                          ' +(?P<local_id>(\S+))'
                                          ' +(?P<remote_id>(\S+)) +(.*)', line)
                            if q:
                                q_area = str(IPAddress(str(q.groupdict()['q_area'])))
                                q_remote_id = str(q.groupdict()['remote_id'])

                                # Check parameters match
                                if q_area == area and q_remote_id == sl_remote_id:
                                    sl_local_id = str(q.groupdict()['local_id'])
                                    break

                    # Set intf_name based on parsed values
                    if sl_local_id is not None:
                        intf_name = '{} {}'.format(sl_local_id, sl_remote_id)
                else:
                    # Set values for dict
                    intf_type = 'interfaces'
                    intf_name = interface

                if 'areas' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area] = {}
                if intf_type not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][intf_type] = {}
                if intf_name not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area][intf_type]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][intf_type][intf_name] = {}
                if 'neighbors' not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area][intf_type]\
                        [intf_name]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][intf_type][intf_name]\
                        ['neighbors'] = {}
                if neighbor not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area][intf_type]\
                        [intf_name]['neighbors']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][intf_type][intf_name]\
                        ['neighbors'][neighbor] = {}
                
                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]['areas'][area][intf_type]\
                            [intf_name]['neighbors'][neighbor]

                # Set values
                sub_dict['neighbor_router_id'] = neighbor
                sub_dict['interface'] = interface
                try:
                    sub_dict['address'] = address
                    del address
                except Exception:
                    pass
                try:
                    sub_dict['interface_id'] = interface_id
                    del interface_id
                except Exception:
                    pass
                continue

            # Neighbor priority is 1, State is FULL, 6 state changes
            p3 = re.compile(r'^Neighbor +priority +is +(?P<priority>(\d+)),'
                             ' +State +is +(?P<state>(\S+)),'
                             ' +(?P<num>(\d+)) +state +changes$')
            m = p3.match(line)
            if m:
                sub_dict['priority'] = int(m.groupdict()['priority'])
                state = str(m.groupdict()['state']).lower()
                state = state.replace('_', '-')
                sub_dict['state'] = state
                if 'statistics' not in sub_dict:
                    sub_dict['statistics'] = {}
                sub_dict['statistics']['nbr_event_count'] = \
                    int(m.groupdict()['num'])
                continue

            # DR is 10.2.3.3 BDR is 10.2.3.2
            p4 = re.compile(r'^DR +is +(?P<dr_ip_addr>(\S+))'
                             ' +BDR +is +(?P<bdr_ip_addr>(\S+))$')
            m = p4.match(line)
            if m:
                sub_dict['dr_ip_addr'] = str(m.groupdict()['dr_ip_addr'])
                sub_dict['bdr_ip_addr'] = str(m.groupdict()['bdr_ip_addr'])
                continue

            # Options is 0x2 in Hello (E-bit)
            p5 = re.compile(r'^Options +is +(?P<options>(\S+)) +in +Hello'
                             ' +\(E-bit\)$')
            m = p5.match(line)
            if m:
                sub_dict['hello_options'] = str(m.groupdict()['options'])
                continue

            # Options is 0x42 in DBD (E-bit, O-bit)
            # Options is 0x42 in DBD (E-bit, O-bit)
            p6 = re.compile(r'^Options +is +(?P<options>(\S+)) +in +DBD'
                             ' +\(E-bit, O-bit\)$')
            m = p6.match(line)
            if m:
                sub_dict['dbd_options'] = str(m.groupdict()['options'])
                continue

            # Dead timer due in 00:00:38
            p7 = re.compile(r'^Dead +timer +due +in +(?P<dead_timer>(\S+))$')
            m = p7.match(line)
            if m:
                sub_dict['dead_timer'] = str(m.groupdict()['dead_timer'])
                continue

            # Neighbor is up for 08:22:07
            p8 = re.compile(r'^Neighbor +is +up +for +(?P<uptime>(\S+))$')
            m = p8.match(line)
            if m:
                sub_dict['uptime'] = str(m.groupdict()['uptime'])
                continue

            # Index 1/2/2, retransmission queue length 0, number of retransmission 0
            p9 = re.compile(r'^Index +(?P<index>(\S+)) +retransmission +queue'
                             ' +length +(?P<ql>(\d+)), +number +of'
                             ' +retransmission +(?P<num_retrans>(\d+))$')
            m = p9.match(line)
            if m:
                sub_dict['index'] = str(m.groupdict()['index'])
                if 'statistics' not in sub_dict:
                    sub_dict['statistics'] = {}
                sub_dict['statistics']['nbr_retrans_qlen'] = \
                    int(m.groupdict()['ql'])
                sub_dict['statistics']['total_retransmission'] = \
                    int(m.groupdict()['num_retrans'])
                continue

            # First 0x0(0)/0x0(0)/0x0(0) Next 0x0(0)/0x0(0)/0x0(0)
            p10 = re.compile(r'^First +(?P<first>(\S+)) +Next +(?P<next>(\S+))$')
            m = p10.match(line)
            if m:
                sub_dict['first'] = str(m.groupdict()['first'])
                sub_dict['next'] = str(m.groupdict()['next'])
                continue

            # Last retransmission scan length is 0, maximum is 0
            p11 = re.compile(r'^Last +retransmission +scan +length +is'
                              ' +(?P<num1>(\d+)), +maximum +is'
                              ' +(?P<num2>(\d+))$')
            m = p11.match(line)
            if m:
                if 'statistics' not in sub_dict:
                    sub_dict['statistics'] = {}
                sub_dict['statistics']['last_retrans_scan_length'] = \
                    int(m.groupdict()['num1'])
                sub_dict['statistics']['last_retrans_max_scan_length'] = \
                    int(m.groupdict()['num2'])
                continue

            # Last retransmission scan time is 0 msec, maximum is 0 msec
            p12 = re.compile(r'^Last +retransmission +scan +time +is'
                              ' +(?P<num1>(\d+)) +msec, +maximum +is'
                              ' +(?P<num2>(\d+)) +msec$')
            m = p12.match(line)
            if m:
                if 'statistics' not in sub_dict:
                    sub_dict['statistics'] = {}
                sub_dict['statistics']['last_retrans_scan_time_msec'] = \
                    int(m.groupdict()['num1'])
                sub_dict['statistics']['last_retrans_max_scan_time_msec'] = \
                    int(m.groupdict()['num2'])
                continue

        return ret_dict


# ===========================
# Schema for:
#   * 'show ip ospf database'
# ===========================
class ShowIpOspfDatabaseSchema(MetaParser):
    
    ''' Schema for:
        * 'show ip ospf database'
    '''

    schema = {
        'vrf':
            {Any():
                {'address_family':
                    {Any():
                        {'instance':
                            {Any():
                                {Optional('areas'):
                                    {Any():
                                        {'database':
                                            {'lsa_types':
                                                {Any():
                                                    {'lsa_type': int,
                                                    'lsas':
                                                        {Any():
                                                            {'lsa_id': str,
                                                            'adv_router': str,
                                                            'ospfv2':
                                                                {'header':
                                                                    {'lsa_id': str,
                                                                    'adv_router': str,
                                                                    'age': int,
                                                                    'seq_num': str,
                                                                    'checksum': str,
                                                                    Optional('link_count'): int,
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
                        },
                    },
                },
            },
        }


# ==========================
# Parser for:
#    'show ip ospf database'
# ==========================
class ShowIpOspfDatabase(ShowIpOspfDatabaseSchema):

    ''' Parser for:
        * 'show ip ospf database'
    '''

    cli_command = 'show ip ospf database'

    def cli(self, output=None):

        if output is None:
            # Execute command on device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}
        address_family = 'ipv4'
        default_mt_id = 0

        # 1: Router
        # 2: Network Link
        # 3: Summary
        # 3: Summary Network
        # 3: Summary Net
        # 4: Summary ASB
        # 5: Type-5 AS External
        # 10: Opaque Area
        lsa_type_mapping = {
            'router': 1,
            'net': 2,
            'summary': 3,
            'summary net': 3,
            'summary asb': 4,
            'external': 5,
            'opaque': 10,
            }

        # OSPF Router with ID (172.16.1.214) (Process ID 65109)
        # OSPF Router with ID (10.36.3.3) (Process ID 1, VRF VRF1)
        p1 = re.compile(r'^OSPF +Router +with +ID +\((?P<router_id>(\S+))\)'
                         ' +\(Process +ID +(?P<instance>(\d+))'
                         '(?:, +VRF +(?P<vrf>(\S+)))?\)$')

        # Router Link States (Area 0)
        # Net Link States (Area 0)
        # Summary Net Link States (Area 8)
        # Summary ASB Link States (Area 8)
        p2 = re.compile(r'^(?P<lsa_type>([a-zA-Z\s]+)) +Link +States +\(Area'
                         ' +(?P<area>(\S+))\)$')

        # Link ID         ADV Router      Age         Seq#       Checksum Link count
        # 10.13.202.64    10.120.202.64   2794        0x80000043 0x002254 3
        # 10.1.1.2        10.169.197.253  70          0x8000003F 0x0015EF
        p3 = re.compile(r'^(?P<link_id>(\S+)) +(?P<adv_router>(\S+))'
                         ' +(?P<age>(\d+)) +(?P<seq>(\S+)) +(?P<checksum>(\S+))'
                         '(?: *(?P<link_count>(\d+)))?$')

        for line in out.splitlines():
            line = line.strip()

            # Load for five secs: 71%/0%; one minute: 11%; five minutes: 9%
            # Time source is NTP, 20:29:26.348 EST Fri Nov 11 2016

            # OSPF Router with ID (10.36.3.3) (Process ID 1, VRF VRF1)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                router_id = str(group['router_id'])
                instance = str(group['instance'])
                if group['vrf']:
                    vrf = str(group['vrf'])
                else:
                    vrf = 'default'
                # Create dict
                ospf_dict = ret_dict.setdefault('vrf', {}).\
                                     setdefault(vrf, {}).\
                                     setdefault('address_family', {}).\
                                     setdefault(address_family, {}).\
                                     setdefault('instance', {}).\
                                     setdefault(instance, {})
                continue

            # Router Link States (Area 0)
            # Net Link States (Area 0)
            # Summary Net Link States (Area 8)
            # Summary ASB Link States (Area 8)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                lsa_type_key = group['lsa_type'].lower()
                if lsa_type_key in lsa_type_mapping:
                    lsa_type = lsa_type_mapping[lsa_type_key]
                else:
                    continue

                # Set area
                if group['area']:
                    try:
                        int(group['area'])
                        area = str(IPAddress(str(group['area'])))
                    except Exception:
                        area = str(group['area'])
                else:
                    area = '0.0.0.0'

                # Create dict structure
                lsa_type_dict = ospf_dict.setdefault('areas', {}).\
                                          setdefault(area, {}).\
                                          setdefault('database', {}).\
                                          setdefault('lsa_types', {}).\
                                          setdefault(lsa_type, {})
                # Set lsa_type
                lsa_type_dict['lsa_type'] = lsa_type
                continue

            # Link ID         ADV Router      Age         Seq#       Checksum Link count
            # 10.13.202.64    10.120.202.64   2794        0x80000043 0x002254 3
            # 10.1.1.2        10.169.197.253  70          0x8000003F 0x0015EF
            m = p3.match(line)
            if m:
                group = m.groupdict()
                lsa_id = group['link_id']

                # Create dict
                lsas_dict = lsa_type_dict.setdefault('lsas', {}).\
                                          setdefault(lsa_id, {})
                lsas_dict['lsa_id'] = lsa_id
                lsas_dict['adv_router'] = group['adv_router']

                # osfpv2 dict
                ospfv2_dict = lsas_dict.setdefault('ospfv2', {}).\
                                        setdefault('header', {})
                ospfv2_dict['lsa_id'] = lsa_id
                ospfv2_dict['adv_router'] = group['adv_router']
                ospfv2_dict['age'] = int(group['age'])
                ospfv2_dict['seq_num'] = group['seq']
                ospfv2_dict['checksum'] = group['checksum']
                if group['link_count']:
                    ospfv2_dict['link_count'] = int(group['link_count'])
                continue

        return ret_dict


# =====================================
# Super parser for:
#   * 'show ip ospf database external'
#   * 'show ip ospf database network'
#   * 'show ip ospf database summary'
#   * 'show ip ospf database router'
#   * 'show ip ospf database opaque'
# =====================================
class ShowIpOspfDatabaseTypeParser(MetaParser):

    ''' Parser for:
        * 'show ip ospf database external'
        * 'show ip ospf database network'
        * 'show ip ospf database summary'
        * 'show ip ospf database router'
        * 'show ip ospf database opaque'
    '''

    def cli(self, cmd, db_type, output=None):

        assert db_type in ['external', 'network', 'summary', 'router',
                           'opaque']

        if output is None:
            # Execute command on device
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}
        af = 'ipv4'
        default_mt_id = 0

        # Router
        # Network Link
        # Summary Network
        # Opaque Area
        # Type-5 AS External
        lsa_type_mapping = {
            'router': 1,
            'network': 2,
            'summary': 3,
            'external': 5,
            'opaque': 10,
            }

        for line in out.splitlines():
            line = line.strip()

            # OSPF Router with ID (10.36.3.3) (Process ID 1)
            # OSPF Router with ID (10.36.3.3) (Process ID 1, VRF VRF1)
            p1 = re.compile(r'^OSPF +Router +with +ID +\((?P<router_id>(\S+))\)'
                             ' +\(Process +ID +(?P<instance>(\d+))'
                             '(?:, +VRF +(?P<vrf>(\S+)))?\)$')
            m = p1.match(line)
            if m:
                router_id = str(m.groupdict()['router_id'])
                instance = str(m.groupdict()['instance'])
                if m.groupdict()['vrf']:
                    vrf = str(m.groupdict()['vrf'])
                else:
                    vrf = 'default'
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if af not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family'][af] = {}
                if 'instance' not in ret_dict['vrf'][vrf]['address_family'][af]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance'] = {}
                if instance not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance] = {}
                continue

            # Router Link States (Area 0)
            # Net Link States (Area 1)
            # Summary Net Link States (Area 0.0.0.0)
            # Type-5 AS External Link States
            # Type-10 Opaque Link Area Link States (Area 0)
            p2 = re.compile(r'^(?P<lsa_type_name>(.*)) +Link +States'
                             '(?: +\(Area +(?P<area>(\S+))\))?$')
            m = p2.match(line)
            if m:
                lsa_type = lsa_type_mapping[db_type]
                
                # Set area
                if m.groupdict()['area']:
                    try:
                        int(m.groupdict()['area'])
                        area = str(IPAddress(str(m.groupdict()['area'])))
                    except Exception:
                        area = str(m.groupdict()['area'])
                else:
                    area = '0.0.0.0'

                # Create dict structure
                if 'areas' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area] = {}
                if 'database' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['database'] = {}
                if 'lsa_types' not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area]['database']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['database']['lsa_types'] = {}
                if lsa_type not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]['database']\
                        ['lsa_types']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['database']['lsa_types']\
                        [lsa_type] = {}

                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]['areas'][area]['database']\
                            ['lsa_types'][lsa_type]

                # Set lsa_type
                sub_dict['lsa_type'] = lsa_type
                continue

            # Routing Bit Set on this LSA
            p3_1 = re.compile(r'^Routing +Bit +Set +on +this +LSA$')
            m = p3_1.match(line)
            if m:
                routing_bit_enable = True
                continue

            # LS age: 1565
            p3_2 = re.compile(r'^LS +age: +(?P<age>(\d+))$')
            m = p3_2.match(line)
            if m:
                age = int(m.groupdict()['age'])
                continue

            # LS age: MAXAGE(3601)
            p3_2_1 = re.compile(r'^LS +age: +\w+\((?P<age>(\d+))\)$')
            m = p3_2_1.match(line)
            if m:
                age = int(m.groupdict()['age'])
                continue

            # Options: 0x20 (No TOS-capability, DC)
            # Options: (No TOS-capability, DC)
            p4 = re.compile(r'^Options:(?: +(?P<option>([a-zA-Z0-9]+)))?'
                            '(?: *\((?P<option_desc>(.*))\))?$')
            m = p4.match(line)
            if m:
                option = str(m.groupdict()['option'])
                option_desc = str(m.groupdict()['option_desc'])
                continue

            # LS Type: Type-5 AS-External
            p5_1 = re.compile(r'^LS +Type: +(?P<lsa_type>(.*))$')
            m = p5_1.match(line)
            if m:
                lsa_type = lsa_type_mapping[db_type]
                continue

            # Link State ID: 10.4.1.1
            # Link State ID: 10.94.44.44 (Network address)
            # Link State ID: 10.1.2.1 (Designated Router address)
            # Link State ID: 10.1.2.1 (address of Designated Router)
            p5_2 = re.compile(r'^Link +State +ID: +(?P<lsa_id>(\S+))'
                             '(?: +\(.*\))?$')
            m = p5_2.match(line)
            if m:
                lsa_id = str(m.groupdict()['lsa_id'])
                continue

            # Advertising Router: 10.64.4.4
            p6 = re.compile(r'^Advertising +Router: +(?P<adv_router>(\S+))$')
            m = p6.match(line)
            if m:
                adv_router = str(m.groupdict()['adv_router'])
                lsa = '{} {}'.format(lsa_id, adv_router)
                
                # Reset counters for this lsa
                link_tlv_counter = 0
                unknown_tlvs_counter = 0

                # Create schema structure
                if 'lsas' not in sub_dict:
                    sub_dict['lsas'] = {}
                if lsa not in sub_dict['lsas']:
                    sub_dict['lsas'][lsa] = {}
                
                # Set keys under 'lsa'
                sub_dict['lsas'][lsa]['adv_router'] = adv_router
                try:
                    sub_dict['lsas'][lsa]['lsa_id'] = lsa_id
                except Exception:
                    pass

                # Set db_dict
                if 'ospfv2' not in sub_dict['lsas'][lsa]:
                    sub_dict['lsas'][lsa]['ospfv2'] = {}
                if 'body' not in sub_dict['lsas'][lsa]['ospfv2']:
                    sub_dict['lsas'][lsa]['ospfv2']['body'] = {}
                if db_type not in sub_dict['lsas'][lsa]['ospfv2']['body']:
                    sub_dict['lsas'][lsa]['ospfv2']['body'][db_type] = {}
                db_dict = sub_dict['lsas'][lsa]['ospfv2']['body'][db_type]

                # Create 'topologies' sub_dict if 'summary' or 'database'
                if db_type in ['summary', 'external']:
                    if 'topologies' not in db_dict:
                        db_dict['topologies'] = {}
                    if default_mt_id not in db_dict['topologies']:
                        db_dict['topologies'][default_mt_id] = {}
                    db_topo_dict = db_dict['topologies'][default_mt_id]
                    db_topo_dict['mt_id'] = default_mt_id

                # Set header dict
                if 'header' not in sub_dict['lsas'][lsa]['ospfv2']:
                    sub_dict['lsas'][lsa]['ospfv2']['header'] = {}
                header_dict = sub_dict['lsas'][lsa]['ospfv2']['header']

                # Set previously parsed values
                try:
                    header_dict['routing_bit_enable'] = routing_bit_enable
                    del routing_bit_enable
                except Exception:
                    pass
                try:
                    header_dict['age'] = age
                    del age
                except Exception:
                    pass
                try:
                    header_dict['option'] = option
                    del option
                except Exception:
                    pass
                try:
                    header_dict['option_desc'] = option_desc
                    del option_desc
                except Exception:
                    pass
                try:
                    header_dict['type'] = lsa_type
                    del lsa_type
                except Exception:
                    pass
                try:
                    header_dict['lsa_id'] = lsa_id
                    del lsa_id
                except Exception:
                    pass
                try:
                    header_dict['adv_router'] = adv_router
                    del adv_router
                except Exception:
                    pass
                try:
                    header_dict['opaque_type'] = opaque_type
                    del opaque_type
                except Exception:
                    pass
                try:
                    header_dict['opaque_id'] = opaque_id
                    del opaque_id
                except Exception:
                    pass

            # LS Seq Number: 0x80000002
            p7 = re.compile(r'^LS +Seq +Number: +(?P<ls_seq_num>(\S+))$')
            m = p7.match(line)
            if m:
                header_dict['seq_num'] = str(m.groupdict()['ls_seq_num'])
                continue

            # Checksum: 0x7d61
            p8 = re.compile(r'^Checksum: +(?P<checksum>(\S+))$')
            m = p8.match(line)
            if m:
                header_dict['checksum'] = str(m.groupdict()['checksum'])
                continue

            # Length: 36
            p9 = re.compile(r'^Length: +(?P<length>(\d+))$')
            m = p9.match(line)
            if m:
                header_dict['length'] = int(m.groupdict()['length'])
                continue

            # Network Mask: /32
            p10 = re.compile(r'^Network +Mask: +\/(?P<net_mask>(\S+))$')
            m = p10.match(line)
            if m:
                dummy = '{}/{}'.format('0.0.0.0', m.groupdict()['net_mask'])
                db_dict['network_mask'] = str(IPNetwork(dummy).netmask)
                continue

            # Metric Type: 2 (Larger than any link state path)
            # Metric Type: 2 (Larger than any link state path)
            p11_1 = re.compile(r'^Metric +Type: +2 +\(.*\)$')
            m = p11_1.match(line)
            if m:
                db_topo_dict['flags'] = "E"
                continue

            # Metric Type: 1 (Comparable directly to link state metric)
            p11_2 = re.compile(r'^Metric +Type: +1 +\(.*\)$')
            m = p11_2.match(line)
            if m:
                # Do nothing
                continue

            # TOS: 0
            # TOS: 0 Metric: 1
            p12 = re.compile(r'^TOS:? +(?P<tos>(\d+))(?:(\s+|\t+)Metric(?:s)?:'
                              ' +(?P<metric>(\d+)))?$')
            m = p12.match(line)
            if m:
                if db_type == 'router':
                    if m.groupdict()['tos']:
                        db_dict['links'][link_id]['topologies'][default_mt_id]\
                                ['tos'] = int(m.groupdict()['tos'])
                    if m.groupdict()['metric']:
                        db_dict['links'][link_id]['topologies'][default_mt_id]\
                                ['metric'] = int(m.groupdict()['metric'])
                        continue
                else:
                    db_topo_dict['tos'] = int(m.groupdict()['tos'])
                    if m.groupdict()['metric']:
                        db_topo_dict['metric'] = int(m.groupdict()['metric'])
                        continue

            # Metric: 20
            p13 = re.compile(r'^Metric: +(?P<metric>(\d+))$')
            m = p13.match(line)
            if m:
                db_topo_dict['metric'] = int(m.groupdict()['metric'])
                continue

            # Forward Address: 0.0.0.0
            p14 = re.compile(r'^Forward +Address: +(?P<addr>(\S+))$')
            m = p14.match(line)
            if m:
                db_topo_dict['forwarding_address'] = str(m.groupdict()['addr'])
                continue

            # External Route Tag: 0
            p15 = re.compile(r'^External +Route +Tag: +(?P<tag>(\d+))$')
            m = p15.match(line)
            if m:
                db_topo_dict['external_route_tag'] = int(m.groupdict()['tag'])
                continue

            # Attached Router: 10.84.66.66
            p16 = re.compile(r'^Attached +Router: +(?P<att_router>(\S+))$')
            m = p16.match(line)
            if m:
                attached_router = str(m.groupdict()['att_router'])
                if 'attached_routers' not in db_dict:
                    db_dict['attached_routers'] = {}
                if attached_router not in db_dict['attached_routers']:
                    db_dict['attached_routers'][attached_router] = {}
                continue

            # Number of links: 3
            # Number of Links: 3
            p17 = re.compile(r'^Number +of +(l|L)inks *: +(?P<num>(\d+))$')
            m = p17.match(line)
            if m:
                db_dict['num_of_links'] = int(m.groupdict()['num'])
                continue

            # Link connected to: a Stub Network
            p18 = re.compile(r'^Link +connected +to: +a +(?P<type>(.*))$')
            m = p18.match(line)
            if m:
                link_type = str(m.groupdict()['type']).lower()
                continue

            # Link connected to: another Router (point-to-point)
            p18_1 = re.compile(r'^Link +connected +to: +(?P<type>(.*))$')
            m = p18_1.match(line)
            if m:
                link_type = str(m.groupdict()['type']).lower()
                continue

            # (Link ID) Network/subnet number: 10.4.1.1
            p19_1 = re.compile(r'^\(Link +ID\) +Network\/(s|S)ubnet +(n|N)umber:'
                                ' +(?P<link_id>(\S+))$')
            m = p19_1.match(line)
            if m:
                link_id = str(m.groupdict()['link_id'])

                # Create dict structures
                if 'links' not in db_dict:
                    db_dict['links'] = {}
                if link_id not in db_dict['links']:
                    db_dict['links'][link_id] = {}
                db_dict['links'][link_id]['link_id'] = link_id

                # Set previously parsed values
                try:
                    db_dict['links'][link_id]['type'] = link_type
                except Exception:
                    pass
                
                # Create topology dict under link_id
                if 'topologies' not in db_dict['links'][link_id]:
                    db_dict['links'][link_id]['topologies'] = {}
                if default_mt_id not in db_dict['links'][link_id]['topologies']:
                    db_dict['links'][link_id]['topologies'][default_mt_id] = {}
                db_dict['links'][link_id]['topologies'][default_mt_id]['mt_id'] = default_mt_id
                continue

            # (Link ID) Designated Router address: 10.166.7.6
            p19_2 = re.compile(r'^\(Link +ID\) +(D|d)esignated +(R|r)outer'
                                ' +(a|A)ddress: +(?P<link_id>(\S+))$')
            m = p19_2.match(line)
            if m:
                link_id = str(m.groupdict()['link_id'])

                # Create dict structures
                if 'links' not in db_dict:
                    db_dict['links'] = {}
                if link_id not in db_dict['links']:
                    db_dict['links'][link_id] = {}
                db_dict['links'][link_id]['link_id'] = link_id

                # Set previously parsed values
                try:
                    db_dict['links'][link_id]['type'] = link_type
                except Exception:
                    pass
                
                # Create topology dict under link_id
                if 'topologies' not in db_dict['links'][link_id]:
                    db_dict['links'][link_id]['topologies'] = {}
                if default_mt_id not in db_dict['links'][link_id]['topologies']:
                    db_dict['links'][link_id]['topologies'][default_mt_id] = {}
                db_dict['links'][link_id]['topologies'][default_mt_id]['mt_id'] = default_mt_id
                continue

            # (Link ID) Neighboring Router ID: 10.151.22.22
            p19_3 = re.compile(r'^\(Link +ID\) +(N|n)eighboring +(R|r)outer'
                                ' +(I|d)D: +(?P<link_id>(\S+))$')
            m = p19_3.match(line)
            if m:
                link_id = str(m.groupdict()['link_id'])

                # Create dict structures
                if 'links' not in db_dict:
                    db_dict['links'] = {}
                if link_id not in db_dict['links']:
                    db_dict['links'][link_id] = {}
                db_dict['links'][link_id]['link_id'] = link_id

                # Set previously parsed values
                try:
                    db_dict['links'][link_id]['type'] = link_type
                except Exception:
                    pass
                
                # Create topology dict under link_id
                if 'topologies' not in db_dict['links'][link_id]:
                    db_dict['links'][link_id]['topologies'] = {}
                if default_mt_id not in db_dict['links'][link_id]['topologies']:
                    db_dict['links'][link_id]['topologies'][default_mt_id] = {}
                db_dict['links'][link_id]['topologies'][default_mt_id]['mt_id'] = default_mt_id
                continue

            # (Link Data) Network Mask: 255.255.255.255
            p20_1 = re.compile(r'^\(Link +Data\) +Network +Mask:'
                                ' +(?P<link_data>(\S+))$')
            m = p20_1.match(line)
            if m:
                db_dict['links'][link_id]['link_data'] = \
                    str(m.groupdict()['link_data'])
                continue

            # (Link Data) Router Interface address: 10.166.7.6
            p20_2 = re.compile(r'^\(Link +Data\) +Router +Interface +address:'
                                ' +(?P<link_data>(\S+))$')
            m = p20_2.match(line)
            if m:
                db_dict['links'][link_id]['link_data'] = \
                    str(m.groupdict()['link_data'])
                continue

            # MTID 32 Metrics: 1
            p21 = re.compile(r'^MTID:? +(?P<mtid>(\d+))(\t+|\s+)(M|m)etric(s?): +(?P<metric>(\d+))$')
            m = p21.match(line)
            if m:
                mtid = int(m.groupdict()['mtid'])
                if db_type == 'router':
                    if mtid not in db_dict['links'][link_id]['topologies']:
                        db_dict['links'][link_id]['topologies'][mtid] = {}
                    db_dict['links'][link_id]['topologies'][mtid]['mt_id'] = mtid
                    db_dict['links'][link_id]['topologies'][mtid]['metric'] = \
                        int(m.groupdict()['metric'])
                elif db_type == 'summary':
                    if 'topologies' not in db_dict:
                        db_dict['topologies'] = {}
                    if mtid not in db_dict['topologies']:
                        db_dict['topologies'][mtid] = {}
                    db_topo_dict = db_dict['topologies'][mtid]
                    db_topo_dict['mt_id'] = mtid
                    db_topo_dict['metric'] = int(m.groupdict()['metric'])
                continue

            # Number of MTID metrics: 0
            p21_1 = re.compile(r'^Number +of +MTID +metrics: +(?P<num>(\d+))$')
            m = p21_1.match(line)
            if m:
                db_dict['links'][link_id]['num_mtid_metrics'] = \
                    int(m.groupdict()['num'])
                continue

            # Opaque Type: 1
            p22 = re.compile(r'^Opaque +Type: +(?P<type>(\d+))(?: +\((Traffic Engineering)\))?$')
            m = p22.match(line)
            if m:
                opaque_type = int(m.groupdict()['type'])
                continue
            
            # Opaque ID: 38
            p23 = re.compile(r'^Opaque +ID: +(?P<id>(\d+))$')
            m = p23.match(line)
            if m:
                opaque_id = int(m.groupdict()['id'])
                continue

            # Fragment number: 0
            p24 = re.compile(r'^Fragment +number *: +(?P<num>(\d+))$')
            m = p24.match(line)
            if m:
                header_dict['fragment_number'] = int(m.groupdict()['num'])
                continue

            # MPLS TE router ID : 10.4.1.1
            p25 = re.compile(r'^MPLS +TE +router +ID *: +(?P<mpls>(\S+))$')
            m = p25.match(line)
            if m:
                header_dict['mpls_te_router_id'] = str(m.groupdict()['mpls'])
                continue

            # AS Boundary Router
            p26_1 = re.compile(r'^AS +Boundary +Router$')
            m = p26_1.match(line)
            if m:
                header_dict['as_boundary_router'] = True
                continue

            # Area Border Router
            p26_2 = re.compile(r'^Area +Border +Router$')
            m = p26_2.match(line)
            if m:
                header_dict['area_border_router'] = True
                continue

            # Link connected to Broadcast network
            p27 = re.compile(r'^Link +connected +to +(?P<link>(.*))$')
            m = p27.match(line)
            if m:
                link_tlv_counter += 1
                if 'link_tlvs' not in db_dict:
                    db_dict['link_tlvs'] = {}
                if link_tlv_counter not in db_dict['link_tlvs']:
                    db_dict['link_tlvs'][link_tlv_counter] = {}

                # Set link type
                opaque_link = str(m.groupdict()['link']).lower()
                if opaque_link == 'broadcast network':
                    opaque_link_type = 2
                else:
                    opaque_link_type = 1
                db_dict['link_tlvs'][link_tlv_counter]\
                    ['link_type'] = opaque_link_type
                db_dict['link_tlvs'][link_tlv_counter]\
                    ['link_name'] = opaque_link
                
                # Set remote_if_ipv4_addrs (if needed)
                if opaque_link_type == 2:
                    if 'remote_if_ipv4_addrs' not in db_dict['link_tlvs']\
                            [link_tlv_counter]:
                        db_dict['link_tlvs'][link_tlv_counter]\
                            ['remote_if_ipv4_addrs'] = {}
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['remote_if_ipv4_addrs']['0.0.0.0'] = {}
                continue

            # Link ID : 10.1.4.4
            p28 = re.compile(r'^Link +ID *: +(?P<id>(\S+))$')
            m = p28.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]['link_id'] = \
                    str(m.groupdict()['id'])
                continue

            # Interface Address : 10.1.4.1
            p29 = re.compile(r'^Interface +Address *: +(?P<addr>(\S+))$')
            m = p29.match(line)
            if m:
                addr = str(m.groupdict()['addr'])
                if 'local_if_ipv4_addrs' not in db_dict['link_tlvs']\
                        [link_tlv_counter]:
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['local_if_ipv4_addrs'] = {}
                if addr not in db_dict['link_tlvs'][link_tlv_counter]\
                        ['local_if_ipv4_addrs']:
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['local_if_ipv4_addrs'][addr] = {}
                    continue

            # Admin Metric : 1
            p30 = re.compile(r'^Admin +Metric *: +(?P<te_metric>(\d+))$')
            m = p30.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]['te_metric'] = \
                    int(m.groupdict()['te_metric'])
                continue

            # Maximum Bandwidth : 125000000
            # Maximum bandwidth : 125000000
            p31 = re.compile(r'^Maximum +(B|b)andwidth *:'
                              ' +(?P<max_band>(\d+))$')
            m = p31.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]['max_bandwidth'] = \
                    int(m.groupdict()['max_band'])
                continue

            # Maximum reservable bandwidth : 93750000
            # Maximum reservable bandwidth global: 93750000
            p32 = re.compile(r'^Maximum +(R|r)eservable +(B|b)andwidth'
                              '(?: +global)? *: +(?P<max_res_band>(\d+))$')
            m = p32.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]\
                    ['max_reservable_bandwidth'] = \
                    int(m.groupdict()['max_res_band'])
                continue

            # Affinity Bit : 0x0
            p33 = re.compile(r'^Affinity +Bit *: +(?P<admin_group>(\S+))$')
            m = p33.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]['admin_group'] = \
                    str(m.groupdict()['admin_group'])
                continue

            # IGP Metric : 1
            p33_1 = re.compile(r'^IGP +Metric *: +(?P<igp_metric>(\d+))$')
            m = p33_1.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]['igp_metric'] = \
                    int(m.groupdict()['igp_metric'])
                continue

            # Number of Priority : 8
            p33_2 = re.compile(r'^Number +of +Priority *: +(?P<num>(\d+))$')
            m = p33_2.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]['total_priority'] = \
                    int(m.groupdict()['num'])
                continue
            
            # Priority 0 : 93750000    Priority 1 : 93750000
            p34 = re.compile(r'^Priority +(?P<num1>(\d+)) *:'
                              ' +(?P<band1>(\d+))(?: +Priority +(?P<num2>(\d+))'
                              ' *: +(?P<band2>(\d+)))?$')
            m = p34.match(line)
            if m:
                value1 = '{} {}'.format(str(m.groupdict()['num1']), str(m.groupdict()['band1']))
                value2 = '{} {}'.format(str(m.groupdict()['num2']), str(m.groupdict()['band2']))
                if 'unreserved_bandwidths' not in db_dict['link_tlvs']\
                        [link_tlv_counter]:
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths'] = {}
                if value1 not in db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths']:
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths'][value1] = {}
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths'][value1]['priority'] = \
                        int(m.groupdict()['num1'])
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths'][value1]\
                        ['unreserved_bandwidth'] = int(m.groupdict()['band1'])
                if value2 not in db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths']:
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths'][value2] = {}
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths'][value2]['priority'] = \
                            int(m.groupdict()['num2'])
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths'][value2]\
                        ['unreserved_bandwidth'] = int(m.groupdict()['band2'])
                    continue

            # Unknown Sub-TLV   :  Type = 32770, Length = 4 Value = 00 00 00 01
            p35 = re.compile(r'^Unknown +Sub-TLV *: +Type += +(?P<type>(\d+)),'
                              ' +Length += +(?P<length>(\d+))'
                              ' +Value += +(?P<value>(.*))$')
            m = p35.match(line)
            if m:
                unknown_tlvs_counter += 1
                if 'unknown_tlvs' not in db_dict['link_tlvs'][link_tlv_counter]:
                    db_dict['link_tlvs'][link_tlv_counter]['unknown_tlvs'] = {}
                if unknown_tlvs_counter not in db_dict['link_tlvs']\
                        [link_tlv_counter]['unknown_tlvs']:
                    db_dict['link_tlvs'][link_tlv_counter]['unknown_tlvs']\
                        [unknown_tlvs_counter] = {}
                db_dict['link_tlvs'][link_tlv_counter]['unknown_tlvs']\
                    [unknown_tlvs_counter]['type'] = int(m.groupdict()['type'])
                db_dict['link_tlvs'][link_tlv_counter]['unknown_tlvs']\
                    [unknown_tlvs_counter]['length'] = int(m.groupdict()['length'])
                db_dict['link_tlvs'][link_tlv_counter]['unknown_tlvs']\
                    [unknown_tlvs_counter]['value'] = str(m.groupdict()['value'])
                continue

            # Extended Administrative Group : Length: 8
            p36 = re.compile(r'^Extended +Administrative +Group *: +Length *:'
                              ' +(?P<eag_length>(\d+))$')
            m = p36.match(line)
            if m:
                if 'extended_admin_group' not in db_dict['link_tlvs']\
                        [link_tlv_counter]:
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['extended_admin_group'] = {}
                db_dict['link_tlvs'][link_tlv_counter]['extended_admin_group']\
                    ['length'] = int(m.groupdict()['eag_length'])
                continue

            # EAG[0]: 0
            p37 = re.compile(r'^EAG\[(?P<group_num>(\d+))\]: +(?P<val>(\d+))$')
            m = p37.match(line)
            if m:
                group_num = int(m.groupdict()['group_num'])
                if 'groups' not in db_dict['link_tlvs'][link_tlv_counter]\
                        ['extended_admin_group']:
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['extended_admin_group']['groups'] = {}
                if group_num not in db_dict['link_tlvs'][link_tlv_counter]\
                    ['extended_admin_group']['groups']:
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['extended_admin_group']['groups'][group_num] = {}
                db_dict['link_tlvs'][link_tlv_counter]['extended_admin_group']\
                    ['groups'][group_num]['value'] = int(m.groupdict()['val'])
                continue


        return ret_dict


# ==================================
# Schema for:
#   * 'show ip ospf database router'
# ==================================
class ShowIpOspfDatabaseRouterSchema(MetaParser):

    ''' Schema for:
        * show ip ospf database router'
    '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {Optional('areas'): 
                                    {Any(): 
                                        {'database': 
                                            {'lsa_types': 
                                                {Any(): 
                                                    {'lsa_type': int,
                                                    'lsas': 
                                                        {Any(): 
                                                            {'lsa_id': str,
                                                            'adv_router': str,
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'option': str,
                                                                    'option_desc': str,
                                                                    'lsa_id': str,
                                                                    'age': int,
                                                                    'type': int,
                                                                    'adv_router': str,
                                                                    'seq_num': str,
                                                                    'checksum': str,
                                                                    'length': int,
                                                                    Optional('routing_bit_enable'): bool,
                                                                    Optional('as_boundary_router'): bool,
                                                                    Optional('area_border_router'): bool,
                                                                    },
                                                                'body': 
                                                                    {'router': 
                                                                        {Optional('flags'): str,
                                                                        'num_of_links': int,
                                                                        Optional('links'):
                                                                            {Any(): 
                                                                                {'link_id': str,
                                                                                'link_data': str,
                                                                                'type': str,
                                                                                'num_mtid_metrics': int,
                                                                                'topologies': 
                                                                                    {Any(): 
                                                                                        {'mt_id': int,
                                                                                        Optional('metric'): int,
                                                                                        Optional('tos'): int,
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


# ==================================
# Parser for:
#   * 'show ip ospf database router'
# ==================================
class ShowIpOspfDatabaseRouter(ShowIpOspfDatabaseRouterSchema, ShowIpOspfDatabaseTypeParser):

    ''' Parser for:
        * 'show ip ospf database router'
    '''

    cli_command = 'show ip ospf database router'

    def cli(self, output=None):

        return super().cli(cmd=self.cli_command, db_type='router', output=output)


# ====================================
# Schema for:
#   * 'show ip ospf database external'
# ====================================
class ShowIpOspfDatabaseExternalSchema(MetaParser):

    ''' Schema for:
        * 'show ip ospf database external'
    '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {Optional('areas'): 
                                    {Any(): 
                                        {'database': 
                                            {'lsa_types': 
                                                {Any(): 
                                                    {'lsa_type': int,
                                                    'lsas': 
                                                        {Any(): 
                                                            {'lsa_id': str,
                                                            'adv_router': str,
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'option': str,
                                                                    'option_desc': str,
                                                                    'lsa_id': str,
                                                                    'age': int,
                                                                    'type': int,
                                                                    'adv_router': str,
                                                                    'seq_num': str,
                                                                    'checksum': str,
                                                                    'length': int,
                                                                    Optional('routing_bit_enable'): bool,
                                                                    },
                                                                'body': 
                                                                    {'external': 
                                                                        {'network_mask': str,
                                                                        'topologies': 
                                                                            {Any(): 
                                                                                {'mt_id': int,
                                                                                Optional('flags'): str,
                                                                                'metric': int,
                                                                                'forwarding_address': str,
                                                                                'external_route_tag': int},
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
                                },
                            },
                        },
                    },
                },
            },
        }


# ====================================
# Parser for:
#   * 'show ip ospf database external'
# ====================================
class ShowIpOspfDatabaseExternal(ShowIpOspfDatabaseExternalSchema, ShowIpOspfDatabaseTypeParser):

    ''' Parser for:
        * 'show ip ospf database external'
    '''

    cli_command = 'show ip ospf database external'

    def cli(self, output=None):

        return super().cli(cmd=self.cli_command, db_type='external', output=output)


# ===================================
# Schema for:
#   * 'show ip ospf database network'
# ===================================
class ShowIpOspfDatabaseNetworkSchema(MetaParser):

    ''' Schema for:
        * 'show ip ospf database network'
    '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {Optional('areas'): 
                                    {Any(): 
                                        {'database': 
                                            {'lsa_types': 
                                                {Any(): 
                                                    {'lsa_type': int,
                                                    'lsas': 
                                                        {Any(): 
                                                            {'lsa_id': str,
                                                            'adv_router': str,
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'option': str,
                                                                    'option_desc': str,
                                                                    'lsa_id': str,
                                                                    'age': int,
                                                                    'type': int,
                                                                    'adv_router': str,
                                                                    'seq_num': str,
                                                                    'checksum': str,
                                                                    'length': int,
                                                                    Optional('routing_bit_enable'): bool,
                                                                    },
                                                                'body': 
                                                                    {'network': 
                                                                        {'network_mask': str,
                                                                        'attached_routers': 
                                                                            {Any(): {},
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
                                },
                            },
                        },
                    },
                },
            },
        }


# ===================================
# Parser for:
#   * 'show ip ospf database network'
# ===================================
class ShowIpOspfDatabaseNetwork(ShowIpOspfDatabaseNetworkSchema, ShowIpOspfDatabaseTypeParser):

    ''' Parser for:
        * 'show ip ospf database network'
    '''

    cli_command = 'show ip ospf database network'

    def cli(self, output=None):

        return super().cli(cmd=self.cli_command, db_type='network', output=output)


# ===================================
# Schema for:
#   * 'show ip ospf database summary'
# ===================================
class ShowIpOspfDatabaseSummarySchema(MetaParser):

    ''' Schema for:
        * 'show ip ospf database summary'
    '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {Optional('areas'): 
                                    {Any(): 
                                        {'database': 
                                            {'lsa_types': 
                                                {Any(): 
                                                    {'lsa_type': int,
                                                    'lsas': 
                                                        {Any(): 
                                                            {'lsa_id': str,
                                                            'adv_router': str,
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'option': str,
                                                                    'option_desc': str,
                                                                    'lsa_id': str,
                                                                    'age': int,
                                                                    'type': int,
                                                                    'adv_router': str,
                                                                    'seq_num': str,
                                                                    'checksum': str,
                                                                    'length': int,
                                                                    Optional('routing_bit_enable'): bool,
                                                                    },
                                                                'body': 
                                                                    {'summary': 
                                                                        {'network_mask': str,
                                                                        'topologies': 
                                                                            {Any(): 
                                                                                {'mt_id': int,
                                                                                'metric': int},
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
                                },
                            },
                        },
                    },
                },
            },
        }


# ===================================
# Parser for:
#   * 'show ip ospf database summary'
# ===================================
class ShowIpOspfDatabaseSummary(ShowIpOspfDatabaseSummarySchema, ShowIpOspfDatabaseTypeParser):

    ''' Parser for:
        * 'show ip ospf database summary'
    '''

    cli_command = 'show ip ospf database summary'

    def cli(self, output=None):

        return super().cli(cmd=self.cli_command, db_type='summary', output=output)


# =======================================
# Schema for:
#   * 'show ip ospf database opaque-area'
# =======================================
class ShowIpOspfDatabaseOpaqueAreaSchema(MetaParser):

    ''' Schema for:
        * 'show ip ospf database opaque-area
    '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {Optional('areas'): 
                                    {Any(): 
                                        {'database': 
                                            {'lsa_types': 
                                                {Any(): 
                                                    {'lsa_type': int,
                                                    'lsas': 
                                                        {Any(): 
                                                            {'lsa_id': str,
                                                            'adv_router': str,
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'option': str,
                                                                    'option_desc': str,
                                                                    'lsa_id': str,
                                                                    'age': int,
                                                                    'type': int,
                                                                    'adv_router': str,
                                                                    'seq_num': str,
                                                                    'checksum': str,
                                                                    'length': int,
                                                                    'opaque_type': int,
                                                                    'opaque_id': int,
                                                                    'fragment_number': int,
                                                                    Optional('mpls_te_router_id'): str},
                                                                'body': 
                                                                    {'opaque': 
                                                                        {'num_of_links': int,
                                                                        Optional('link_tlvs'): 
                                                                            {Any(): 
                                                                                {'link_type': int,
                                                                                'link_name': str,
                                                                                'link_id': str,
                                                                                'te_metric': int,
                                                                                'max_bandwidth': int,
                                                                                'max_reservable_bandwidth': int,
                                                                                'admin_group': str,
                                                                                Optional('igp_metric'): int,
                                                                                Optional('total_priority'): int,
                                                                                Optional('local_if_ipv4_addrs'): 
                                                                                    {Any(): {}},
                                                                                Optional('remote_if_ipv4_addrs'): 
                                                                                    {Any(): {}},
                                                                                Optional('unreserved_bandwidths'): 
                                                                                    {Any(): 
                                                                                        {'priority': int,
                                                                                        'unreserved_bandwidth': int},
                                                                                    },
                                                                                Optional('unknown_tlvs'): 
                                                                                    {Any(): 
                                                                                        {'type': int,
                                                                                        'length': int,
                                                                                        'value': str},
                                                                                    },
                                                                                Optional('extended_admin_group'):
                                                                                    {'length': int,
                                                                                    Optional('groups'): 
                                                                                        {Any(): 
                                                                                            {'value': int,},
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


# =======================================
# Parser for:
#   * 'show ip ospf database opaque-area'
# =======================================
class ShowIpOspfDatabaseOpaqueArea(ShowIpOspfDatabaseOpaqueAreaSchema, ShowIpOspfDatabaseTypeParser):

    ''' Parser for:
        * 'show ip ospf database opaque-area'
    '''

    cli_command = 'show ip ospf database opaque-area'

    def cli(self, output=None):

        return super().cli(cmd=self.cli_command, db_type='opaque', output=output)


# =====================================
# Schema for:
#   * 'show ip ospf mpls ldp interface'
# =====================================
class ShowIpOspfMplsLdpInterfaceSchema(MetaParser):

    ''' Schema for:
        * "show ip ospf mpls ldp interface" 
    '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {'mpls': 
                                    {'ldp': 
                                        {'autoconfig': bool,
                                        'autoconfig_area_id': str,
                                        },
                                    },
                                'areas': 
                                    {Any(): 
                                        {'interfaces': 
                                            {Any(): 
                                                {'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': bool,
                                                        'autoconfig_area_id': str,
                                                        'igp_sync': bool,
                                                        'holddown_timer': bool,
                                                        'state': str,
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
            },
        }


# =====================================
# Parser for:
#   * 'show ip ospf mpls ldp interface'
# =====================================
class ShowIpOspfMplsLdpInterface(ShowIpOspfMplsLdpInterfaceSchema):

    ''' Parser for:
        * 'show ip ospf mpls ldp interface'
    '''

    cli_command = 'show ip ospf mpls ldp interface'

    def cli(self, output=None):

        if output is None:
            # Execute command on device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}
        af = 'ipv4' # this is ospf - always ipv4

        for line in out.splitlines():
            line = line.strip()

            # Loopback0
            # GigabitEthernet2
            # TenGigabitEthernet3/0/1
            # TwoGigabitEthernet
            # FiveGigabitEthernet
            # TwentyFiveGigE
            # FortyGigabitEthernet
            # HundredGigE
            # OSPF_SL1
            # OSPF_VL1
            # --extra--
            # Cellular
            # FastEthernet
            # LISP
            # Port-channel
            # Tunnel
            # VirtualPortGroup
            # Vlan
            p1 = re.compile(r'^(?P<interface>(Lo.*|.*Gig.*|.*(SL|VL).*|'
                             'Cellular.*|FastEthernet.*|LISP.*|Po.*|Tunnel.*|'
                             'VirtualPortGroup.*|Vlan.*))$')
            m = p1.match(line)
            if m:
                interface = str(m.groupdict()['interface'])
                continue

            # Process ID 1, Area 0
            # Process ID 100, Area 0.0.0.0
            # Process ID 2, VRF VRF1, Area 1
            p2 = re.compile(r'^Process +ID +(?P<instance>(\S+)),'
                             '(?: +VRF +(?P<vrf>(\S+)),)?'
                             ' +Area +(?P<area>(\S+))$')
            m = p2.match(line)
            if m:
                instance = str(m.groupdict()['instance'])
                try:
                    int(m.groupdict()['area'])
                    area = str(IPAddress(str(m.groupdict()['area'])))
                except:
                    area = m.groupdict()['area']
                if m.groupdict()['vrf']:
                    vrf = str(m.groupdict()['vrf'])
                else:
                    vrf = 'default'

                # Create dict
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if af not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family'][af] = {}
                if 'instance' not in ret_dict['vrf'][vrf]['address_family'][af]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance'] = {}
                if instance not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance] = {}
                # Create mpls dict
                if 'mpls' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['mpls'] = {}
                if 'ldp' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['mpls']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['mpls']['ldp'] = {}
                mpls_ldp_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['mpls']['ldp']
                # Set values to mpls_ldp_dict
                mpls_ldp_dict['autoconfig_area_id'] = area
                if 'areas' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area] = {}
                if 'interfaces' not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['interfaces'] = {}
                if interface not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]['interfaces']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['interfaces'][interface] = {}
                if 'mpls' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]['interfaces']\
                        [interface]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['interfaces'][interface]\
                        ['mpls'] = {}
                if 'ldp' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]['interfaces']\
                        [interface]['mpls']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['interfaces'][interface]\
                        ['mpls']['ldp'] = {}
                # Creat intf_dict
                intf_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                                ['instance'][instance]['areas'][area]\
                                ['interfaces'][interface]['mpls']['ldp']
                # Set values to intf_dict
                intf_dict['autoconfig_area_id'] = area
                continue

            # LDP is not configured through LDP autoconfig
            # LDP is configured through LDP autoconfig
            p3 = re.compile(r'^LDP +is'
                             ' +(?P<auto_config>(not configured|configured))'
                             ' +through +LDP +autoconfig$')
            m = p3.match(line)
            if m:
                if m.groupdict()['auto_config'] is 'configured':
                    intf_dict['autoconfig'] = True
                    mpls_ldp_dict['autoconfig'] = True
                else:
                    intf_dict['autoconfig'] = False
                    mpls_ldp_dict['autoconfig'] = False
                    continue
            
            # LDP-IGP Synchronization : Not required
            # LDP-IGP Synchronization : Required
            p4 = re.compile(r'^LDP-IGP +Synchronization *:'
                              ' +(?P<igp_sync>(Not required|Required))$')
            m = p4.match(line)
            if m:
                if m.groupdict()['igp_sync'] == 'Required':
                    intf_dict['igp_sync'] = True
                else:
                    intf_dict['igp_sync'] = False
                    continue

            # Holddown timer is disabled
            p5 = re.compile(r'^Holddown +timer +is (?P<val>([a-zA-Z\s]+))$')
            m = p5.match(line)
            if m:
                if 'enabled' in m.groupdict()['val']:
                    intf_dict['holddown_timer'] = True
                else:
                    intf_dict['holddown_timer'] = False
                    continue

            # Interface is up 
            p5 = re.compile(r'^Interface +is (?P<state>(up|down))$')
            m = p5.match(line)
            if m:
                intf_dict['state'] = str(m.groupdict()['state'])
                continue

        return ret_dict


# ========================================
# Schema for:
#   * 'show ip ospf mpls traffic-eng link'
# ========================================
class ShowIpOspfMplsTrafficEngLinkSchema(MetaParser):

    ''' Schema for:
        * 'show ip ospf mpls traffic-eng link'
    '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {'mpls': 
                                    {'te': 
                                        {'router_id': str},
                                    },
                                'areas': 
                                    {Any(): 
                                        {'mpls': 
                                            {'te': 
                                                {'enable': bool,
                                                Optional('total_links'): int,
                                                Optional('area_instance'): int,
                                                Optional('link_hash_bucket'):
                                                    {Any(): 
                                                        {'link_fragments': 
                                                            {Any(): 
                                                                {'link_instance': int,
                                                                'network_type': str,
                                                                'link_id': str,
                                                                'interface_address': str,
                                                                'te_admin_metric': int,
                                                                'igp_admin_metric': int,
                                                                'max_bandwidth': int,
                                                                'max_reservable_bandwidth': int,
                                                                'affinity_bit': str,
                                                                'total_priority': int,
                                                                Optional('unreserved_bandwidths'): 
                                                                    {Any(): 
                                                                        {'priority': int,
                                                                        'unreserved_bandwidth': int,
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
                            },
                        },
                    },
                },
            },
        }


# ========================================
# Parser for:
#   * 'show ip ospf mpls traffic-eng link'
# ========================================
class ShowIpOspfMplsTrafficEngLink(ShowIpOspfMplsTrafficEngLinkSchema):

    ''' Parser for:
        * 'show ip ospf mpls traffic-eng link'
    '''

    cli_command = 'show ip ospf mpls traffic-eng link'

    def cli(self, output=None):

        if output is None:
            # Execute command on device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}
        af = 'ipv4' # this is ospf - always ipv4

        for line in out.splitlines():
            line = line.strip()

            # OSPF Router with ID (10.4.1.1) (Process ID 1)
            p1 = re.compile(r'^OSPF +Router +with +ID +\((?P<router_id>(\S+))\)'
                             ' +\(Process +ID +(?P<instance>(\S+))\)$')
            m = p1.match(line)
            if m:
                router_id = str(m.groupdict()['router_id'])
                instance = str(m.groupdict()['instance'])

                # Get VRF information using the ospf instance
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

                # Create dict
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if af not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family'][af] = {}
                if 'instance' not in ret_dict['vrf'][vrf]['address_family'][af]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance'] = {}
                if instance not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance] = {}
                if 'mpls' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['mpls'] = {}
                if 'te' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['mpls']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['mpls']['te'] = {}
                ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['mpls']['te']['router_id'] = router_id
                continue

            # Area 0 has 2 MPLS TE links. Area instance is 2.
            p2 = re.compile(r'^Area +(?P<area>(\d+)) +has +(?P<links>(\d+))'
                             ' +MPLS +TE +links. +Area +instance +is'
                             ' +(?P<area_instance>(\d+))\.$')
            m = p2.match(line)
            if m:
                area = str(IPAddress(str(m.groupdict()['area'])))
                total_links = int(m.groupdict()['links'])
                area_instance = int(m.groupdict()['area_instance'])
                # Create dict
                if 'areas' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area] = {}
                if 'mpls' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['mpls'] = {}
                if 'te' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]['mpls']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['mpls']['te'] = {}
                # Set values
                ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                    [instance]['areas'][area]['mpls']['te']['enable'] = True
                ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                    [instance]['areas'][area]['mpls']['te']['total_links'] = \
                        total_links
                ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                    [instance]['areas'][area]['mpls']['te']['area_instance'] = \
                        area_instance
                continue

            # Area 1 MPLS TE not initialized
            # Area 0.0.0.0 MPLS TE not initialized
            p3 = re.compile(r'^Area +(?P<area>(\S+)) +MPLS +TE +not +initialized$')
            m = p3.match(line)
            if m:
                try:
                    int(m.groupdict()['area'])
                    area = str(IPAddress(str(m.groupdict()['area'])))
                except:
                    area = m.groupdict()['area']
                # Create dict
                if 'areas' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area] = {}
                if 'mpls' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['mpls'] = {}
                if 'te' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]['mpls']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['mpls']['te'] = {}
                # Set values
                ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                    [instance]['areas'][area]['mpls']['te']['enable'] = False
                continue

            # Links in hash bucket 8.
            p4 = re.compile(r'^Links +in +hash +bucket +(?P<hash>(\d+))\.$')
            m = p4.match(line)
            if m:
                link_hash_bucket = int(m.groupdict()['hash'])
                if 'link_hash_bucket' not in ret_dict['vrf'][vrf]\
                        ['address_family'][af]['instance'][instance]['areas']\
                        [area]['mpls']['te']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['mpls']['te']\
                        ['link_hash_bucket'] = {}
                if link_hash_bucket not in ret_dict['vrf'][vrf]\
                        ['address_family'][af]['instance'][instance]['areas']\
                        [area]['mpls']['te']['link_hash_bucket']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['mpls']['te']\
                        ['link_hash_bucket'][link_hash_bucket] = {}
                link_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                                ['instance'][instance]['areas'][area]['mpls']\
                                ['te']['link_hash_bucket'][link_hash_bucket]
                continue

            # Link is associated with fragment 2. Link instance is 2
            p5 = re.compile(r'^Link +is +associated +with +fragment'
                             ' +(?P<fragment>(\d+))\. +Link +instance +is'
                             ' +(?P<link_instance>(\d+))$')
            m = p5.match(line)
            if m:
                link_fragment = int(m.groupdict()['fragment'])
                if 'link_fragments' not in link_dict:
                    link_dict['link_fragments'] = {}
                if link_fragment not in link_dict['link_fragments']:
                    link_dict['link_fragments'][link_fragment] = {}
                sub_dict = link_dict['link_fragments'][link_fragment]
                sub_dict['link_instance'] = int(m.groupdict()['link_instance'])
                continue

            # Link connected to Broadcast network
            p6 = re.compile(r'^Link +connected +to +(?P<type>([a-zA-Z\s]+))$')
            m = p6.match(line)
            if m:
                sub_dict['network_type'] = str(m.groupdict()['type']).lower()
                continue

            # Link ID : 10.1.2.1
            p7 = re.compile(r'^Link +ID *: +(?P<link_id>(\S+))$')
            m = p7.match(line)
            if m:
                sub_dict['link_id'] = str(m.groupdict()['link_id'])
                continue

            # Interface Address : 10.1.2.1
            p8 = re.compile(r'^Interface +Address *: +(?P<addr>(\S+))$')
            m = p8.match(line)
            if m:
                sub_dict['interface_address'] = str(m.groupdict()['addr'])
                continue

            # Admin Metric te: 1 igp: 1
            p9 = re.compile(r'^Admin +Metric +te: +(?P<te>(\d+)) +igp:'
                             ' +(?P<igp>(\d+))$')
            m = p9.match(line)
            if m:
                sub_dict['te_admin_metric'] = int(m.groupdict()['te'])
                sub_dict['igp_admin_metric'] = int(m.groupdict()['igp'])
                continue

            # Maximum bandwidth : 125000000
            p9 = re.compile(r'^Maximum +(B|b)andwidth *: +(?P<mband>(\d+))$')
            m = p9.match(line)
            if m:
                sub_dict['max_bandwidth'] = int(m.groupdict()['mband'])
                continue

            # Maximum reservable bandwidth : 93750000
            p10 = re.compile(r'^Maximum +(R|r)eservable +(B|b)andwidth *:'
                              ' +(?P<res_band>(\d+))$')
            m = p10.match(line)
            if m:
                sub_dict['max_reservable_bandwidth'] = \
                    int(m.groupdict()['res_band'])
                continue

            # Affinity Bit : 0x0
            p11 = re.compile(r'^Affinity +Bit *: +(?P<admin_group>(\S+))$')
            m = p11.match(line)
            if m:
                sub_dict['affinity_bit'] = str(m.groupdict()['admin_group'])
                continue

            # Number of Priority : 8
            p12 = re.compile(r'^Number +of +Priority +: +(?P<priority>(\d+))$')
            m = p12.match(line)
            if m:
                sub_dict['total_priority'] = int(m.groupdict()['priority'])
                continue

            # Priority 0 : 93750000     Priority 1 : 93750000
            p13 = re.compile(r'^Priority +(?P<num1>(\d+)) *:'
                              ' +(?P<band1>(\d+))(?: +Priority +(?P<num2>(\d+))'
                              ' *: +(?P<band2>(\d+)))?$')
            m = p13.match(line)
            if m:
                value1 = '{} {}'.format(str(m.groupdict()['num1']), str(m.groupdict()['band1']))
                value2 = '{} {}'.format(str(m.groupdict()['num2']), str(m.groupdict()['band2']))
                if 'unreserved_bandwidths' not in sub_dict:
                    sub_dict['unreserved_bandwidths'] = {}
                if value1 not in sub_dict['unreserved_bandwidths']:
                    sub_dict['unreserved_bandwidths'][value1] = {}
                    sub_dict['unreserved_bandwidths'][value1]['priority'] =  \
                        int(m.groupdict()['num1'])
                    sub_dict['unreserved_bandwidths'][value1]\
                        ['unreserved_bandwidth'] = int(m.groupdict()['band1'])
                if value2 not in sub_dict['unreserved_bandwidths']:
                    sub_dict['unreserved_bandwidths'][value2] = {}
                    sub_dict['unreserved_bandwidths'][value2]['priority'] = \
                        int(m.groupdict()['num2'])
                    sub_dict['unreserved_bandwidths'][value2]\
                        ['unreserved_bandwidth'] = int(m.groupdict()['band2'])
                continue

        return ret_dict


# =============================
# Schema for:
#   * 'show ip ospf max-metric'
# =============================
class ShowIpOspfMaxMetricSchema(MetaParser):
    
    ''' Schema for:
        * 'show ip ospf max-metric'
    '''

    schema = {
        'vrf':
            {Any():
                {'address_family':
                    {Any():
                        {'instance':
                            {Any():
                                {'router_id': str,
                                'base_topology_mtid':
                                    {Any():
                                        {'start_time': str,
                                        'time_elapsed': str,
                                        'router_lsa_max_metric':
                                            {Any(): 
                                                {Optional('condition'): str,
                                                Optional('state'): str,
                                                Optional('advertise_lsa_metric'): int,
                                                Optional('unset_reason'): str,
                                                Optional('unset_time'): str,
                                                Optional('unset_time_elapsed'): str,
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


# =============================
# Parser for:
#   * 'show ip ospf max-metric'
# =============================
class ShowIpOspfMaxMetric(ShowIpOspfMaxMetricSchema):

    ''' Parser for:
        * 'show ip ospf max-metric'
    '''

    cli_command = 'show ip ospf max-metric'

    def cli(self, output=None):

        if output is None:
            # Execute command on device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}
        address_family = 'ipv4'

        # Load for five secs: 71%/0%; one minute: 11%; five minutes: 9%
        # Time source is NTP, 20:29:26.348 EST Fri Nov 11 2016

        # OSPF Router with ID (172.16.1.214) (Process ID 65109)
        # OSPF Router with ID (10.36.3.3) (Process ID 1, VRF VRF1)
        p1 = re.compile(r'^OSPF +Router +with +ID +\((?P<router_id>(\S+))\)'
                         ' +\(Process +ID +(?P<instance>(\d+))'
                         '(?:, +VRF +(?P<vrf>(\S+)))?\)$')

        # Base Topology (MTID 0)
        p2 = re.compile(r'^Base +Topology +\(MTID +(?P<mtid>(\d+))\)$')

        # Start time: 00:01:58.314, Time elapsed: 00:54:43.858
        p3 = re.compile(r'^Start +time: +(?P<start_time>(\S+)), +Time +elapsed:'
                         ' +(?P<time_elapsed>(\S+))$')

        # Originating router-LSAs with maximum metric
        p4_1 = re.compile(r'^Originating +router-LSAs +with +maximum +metric$')

        # Router is not originating router-LSAs with maximum metric
        p4_2 = re.compile(r'^Router +is +not +originating +router-LSAs +with'
                           ' +maximum +metric$')

        # Condition: on startup for 5 seconds, State: inactive
        p5 = re.compile(r'^Condition: +(?P<condition>(.*)), +State:'
                          ' +(?P<state>([a-zA-Z\s]+))$')

        # Advertise summary-LSAs with metric 16711680
        p6 = re.compile(r'^Advertise +summary-LSAs +with +metric'
                         ' +(?P<metric>(\d+))$')

        # Unset reason: timer expired, Originated for 5 seconds
        p7 = re.compile(r'^Unset +reason: (?P<reason>(.*))$')

        # Unset time: 00:02:03.314, Time elapsed: 00:54:38.858
        p8 = re.compile(r'^Unset +time: +(?P<time>(\S+)), +Time +elapsed:'
                         ' +(?P<elapsed>(\S+))$')

        for line in out.splitlines():
            line = line.strip()

            # OSPF Router with ID (10.36.3.3) (Process ID 1, VRF VRF1)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                router_id = str(group['router_id'])
                instance = str(group['instance'])
                if group['vrf']:
                    vrf = str(group['vrf'])
                else:
                    vrf = 'default'
                # Create dict
                ospf_dict = ret_dict.setdefault('vrf', {}).\
                                     setdefault(vrf, {}).\
                                     setdefault('address_family', {}).\
                                     setdefault(address_family, {}).\
                                     setdefault('instance', {}).\
                                     setdefault(instance, {})
                ospf_dict['router_id'] = router_id
                continue

            # Base Topology (MTID 0)
            m = p2.match(line)
            if m:
                mtid = m.groupdict()['mtid']
                mtid_dict = ospf_dict.setdefault('base_topology_mtid', {}).\
                                      setdefault(mtid, {})
                continue

            # Start time: 00:01:58.314, Time elapsed: 00:54:43.858
            m = p3.match(line)
            if m:
                group = m.groupdict()
                mtid_dict['start_time'] = group['start_time']
                mtid_dict['time_elapsed'] = group['time_elapsed']
                continue

            # Originating router-LSAs with maximum metric
            m = p4_1.match(line)
            if m:
                rtr_lsa_dict = mtid_dict.\
                                    setdefault('router_lsa_max_metric', {}).\
                                    setdefault(True, {})
                continue

            # Router is not originating router-LSAs with maximum metric
            m = p4_2.match(line)
            if m:
                rtr_lsa_dict = mtid_dict.\
                                    setdefault('router_lsa_max_metric', {}).\
                                    setdefault(False, {})
                continue

            # Condition: on startup for 5 seconds, State: inactive
            m = p5.match(line)
            if m:
                group = m.groupdict()
                rtr_lsa_dict['condition'] = group['condition']
                rtr_lsa_dict['state'] = group['state']
                continue

            # Advertise summary-LSAs with metric 16711680
            m = p6.match(line)
            if m:
                rtr_lsa_dict['advertise_lsa_metric'] = int(m.groupdict()['metric'])

            # Unset reason: timer expired, Originated for 5 seconds
            m = p7.match(line)
            if m:
                rtr_lsa_dict['unset_reason'] = m.groupdict()['reason']
                continue

            # Unset time: 00:02:03.314, Time elapsed: 00:54:38.858
            m = p8.match(line)
            if m:
                group = m.groupdict()
                rtr_lsa_dict['unset_time'] = group['time']
                rtr_lsa_dict['unset_time_elapsed'] = group['elapsed']
                continue

        return ret_dict


# ==========================
# Schema for:
#   * 'show ip ospf traffic'
# ==========================
class ShowIpOspfTrafficSchema(MetaParser):

    ''' Schema for:
        * 'show ip ospf traffic'
    '''

    schema = {
        'ospf_statistics':
            {'last_clear_traffic_counters': str,
            'rcvd':
                {'total': int,
                'checksum_errors': int,
                'hello': int,
                'database_desc': int,
                'link_state_req': int,
                'link_state_updates': int,
                'link_state_acks': int,
                },
            'sent':
                {'total': int,
                'hello': int,
                'database_desc': int,
                'link_state_req': int,
                'link_state_updates': int,
                'link_state_acks': int,
                },
            },
        'vrf':
            {Any():
                {'address_family':
                    {Any():
                        {'instance':
                            {Any():
                                {'router_id': str,
                                'ospf_queue_statistics':
                                    {'limit': 
                                        {'inputq': int,
                                        'outputq': int,
                                        'updateq': int,
                                        },
                                    'drops': 
                                        {'inputq': int,
                                        'outputq': int,
                                        'updateq': int,
                                        },
                                    'max_delay_msec': 
                                        {'inputq': int,
                                        'outputq': int,
                                        'updateq': int,
                                        },
                                    'max_size': 
                                        {'total': 
                                            {'inputq': int,
                                            'outputq': int,
                                            'updateq': int,
                                            },
                                        'invalid':
                                            {'inputq': int,
                                            'outputq': int,
                                            'updateq': int,
                                            },
                                        'hello':
                                            {'inputq': int,
                                            'outputq': int,
                                            'updateq': int,
                                            },
                                        'db_des':
                                            {'inputq': int,
                                            'outputq': int,
                                            'updateq': int,
                                            },
                                        'ls_req':
                                            {'inputq': int,
                                            'outputq': int,
                                            'updateq': int,
                                            },
                                        'ls_upd':
                                            {'inputq': int,
                                            'outputq': int,
                                            'updateq': int,
                                            },
                                        'ls_ack':
                                            {'inputq': int,
                                            'outputq': int,
                                            'updateq': int,
                                            },
                                        },
                                    'current_size': 
                                        {'total': 
                                            {'inputq': int,
                                            'outputq': int,
                                            'updateq': int,
                                            },
                                        'invalid':
                                            {'inputq': int,
                                            'outputq': int,
                                            'updateq': int,
                                            },
                                        'hello':
                                            {'inputq': int,
                                            'outputq': int,
                                            'updateq': int,
                                            },
                                        'db_des':
                                            {'inputq': int,
                                            'outputq': int,
                                            'updateq': int,
                                            },
                                        'ls_req':
                                            {'inputq': int,
                                            'outputq': int,
                                            'updateq': int,
                                            },
                                        'ls_upd':
                                            {'inputq': int,
                                            'outputq': int,
                                            'updateq': int,
                                            },
                                        'ls_ack':
                                            {'inputq': int,
                                            'outputq': int,
                                            'updateq': int,
                                            },
                                        },
                                    },
                                'interface_statistics':
                                    {'interfaces':
                                        {Any():
                                            {'last_clear_traffic_counters': str,
                                            'ospf_packets_received_sent':
                                                {'type': 
                                                    {Any():
                                                        {'packets': int,
                                                        'bytes': int,
                                                        },
                                                    },
                                                },
                                            'ospf_header_errors':
                                                {'length': int,
                                                'instance_id': int,
                                                'checksum': int,
                                                'auth_type': int,
                                                'version': int,
                                                'bad_source': int,
                                                'no_virtual_link': int,
                                                'area_mismatch': int,
                                                'no_sham_link': int,
                                                'self_originated': int,
                                                'duplicate_id': int,
                                                'hello': int,
                                                'mtu_mismatch': int,
                                                'nbr_ignored': int,
                                                'lls': int,
                                                'unknown_neighbor': int,
                                                'authentication': int,
                                                'ttl_check_fail': int,
                                                'adjacency_throttle': int,
                                                'bfd': int,
                                                'test_discard': int,
                                                },
                                            'ospf_lsa_errors':
                                                {'type': int,
                                                'length': int,
                                                'data': int,
                                                'checksum': int,
                                                },
                                            },
                                        },
                                    },
                                'summary_traffic_statistics':
                                    {'ospf_packets_received_sent': 
                                        {'type':
                                            {Any():
                                                {'packets': int,
                                                'bytes': int,
                                                },
                                            },
                                        },
                                    'ospf_header_errors':
                                        {'length': int,
                                        'instance_id': int,
                                        'checksum': int,
                                        'auth_type': int,
                                        'version': int,
                                        'bad_source': int,
                                        'no_virtual_link': int,
                                        'area_mismatch': int,
                                        'no_sham_link': int,
                                        'self_originated': int,
                                        'duplicate_id': int,
                                        'hello': int,
                                        'mtu_mismatch': int,
                                        'nbr_ignored': int,
                                        'lls': int,
                                        'unknown_neighbor': int,
                                        'authentication': int,
                                        'ttl_check_fail': int,
                                        'adjacency_throttle': int,
                                        'bfd': int,
                                        'test_discard': int,
                                        },
                                    'ospf_lsa_errors':
                                        {'type': int,
                                        'length': int,
                                        'data': int,
                                        'checksum': int,
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# ==========================
# Parser for:
#   * 'show ip ospf traffic'
# ==========================
class ShowIpOspfTraffic(ShowIpOspfTrafficSchema):

    ''' Parser for:
        * "show ip ospf traffic"
    '''

    cli_command = 'show ip ospf traffic'

    def cli(self, output=None):

        if output is None:
            # Execute command on device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}
        address_family = 'ipv4'
        received = False ; sent = False
        interface_stats = False ; summary_stats = False
        max_size_stats = False ; current_size_stats = False

        # OSPF statistics:
        p1 = re.compile(r'^OSPF +statistics:$')

        # Last clearing of OSPF traffic counters never
        # Last clearing of interface traffic counters never
        p2 = re.compile(r'^Last +clearing +of +(?P<type>(OSPF|interface)) +traffic'
                         ' +counters +(?P<last_clear>([a-zA-Z0-9\:\s]+))$')

        # Rcvd: 2112690 total, 0 checksum errors
        p3 = re.compile(r'^Rcvd: +(?P<total>(\d+)) total, +(?P<csum_errors>(\d+))'
                         ' +checksum +errors$')

        # 2024732 hello, 938 database desc, 323 link state req
        # 2381794 hello, 1176 database desc, 43 link state req
        p4 = re.compile(r'^(?P<hello>(\d+)) +hello, +(?P<db_desc>(\d+))'
                         ' +database +desc, +(?P<link_state_req>(\d+))'
                         ' +link +state +req$')

        # 11030 link state updates, 75666 link state acks
        # 92224 link state updates, 8893 link state acks
        p5 = re.compile(r'^(?P<link_state_updates>(\d+)) +link +state +updates,'
                         ' +(?P<link_state_acks>(\d+)) +link +state +acks$')

        # Sent: 2509472 total
        p6 = re.compile(r'^Sent: +(?P<total>(\d+)) +total$')


        # OSPF Router with ID (10.169.197.252) (Process ID 65109)
        # OSPF Router with ID (10.36.3.3) (Process ID 1, VRF VRF1)
        p7 = re.compile(r'^OSPF +Router +with +ID +\((?P<router_id>(\S+))\)'
                         ' +\(Process +ID +(?P<instance>(\d+))'
                         '(?:, +VRF +(?P<vrf>(\S+)))?\)$')

        # OSPF queue statistics for process ID 65109:
        p8 = re.compile(r'^OSPF +queue +statistics +for +process +ID +(?P<pid>(\d+)):$')

        #                   InputQ   UpdateQ      OutputQ
        # Limit             0        200          0
        # Drops             0          0          0
        # Max delay [msec] 49          2          2
        # Invalid           0          0          0
        # Hello             0          0          0
        # DB des            0          0          0
        # LS req            0          0          0
        # LS upd            0          0          0
        # LS ack           14         14          6
        p9_1 = re.compile(r'^(?P<item>(Limit|Drops|Max delay \[msec\]|Invalid|'
                           'Hello|DB des|LS req|LS upd|LS ack))'
                           ' +(?P<inputq>(\d+)) +(?P<updateq>(\d+))'
                           ' +(?P<outputq>(\d+))$')

        #                   InputQ   UpdateQ      OutputQ
        # Max size         14         14          6
        # Current size      0          0          0
        p9_2 = re.compile(r'^(?P<item>(Max size|Current size)) +(?P<inputq>(\d+))'
                           ' +(?P<updateq>(\d+)) +(?P<outputq>(\d+))$')

        # Interface statistics:
        p10 = re.compile(r'^Interface +statistics:$')

        # Interface GigabitEthernet0/0/6
        p11 = re.compile(r'^Interface +(?P<intf>(\S+))$')

        # OSPF packets received/sent
        # Type          Packets              Bytes
        # RX Invalid    0                    0
        # RX Hello      169281               8125472
        # RX DB des     36                   1232
        # RX LS req     20                   25080
        # RX LS upd     908                  76640
        # RX LS ack     9327                 8733808
        # RX Total      179572               16962232
        # TX Failed     0                    0
        # TX Hello      169411               13552440
        # TX DB des     40                   43560
        # TX LS req     4                    224
        # TX LS upd     12539                12553264
        # TX LS ack     899                  63396
        # TX Total      182893               26212884
        p12 = re.compile(r'^(?P<type>([a-zA-Z\s]+)) +(?P<packets>(\d+))'
                          ' +(?P<bytes>(\d+))$')

        # OSPF header errors
        p13 = re.compile(r'^OSPF +header +errors$')

        # Length 0, Instance ID 0, Checksum 0, Auth Type 0,
        p14 = re.compile(r'^Length +(?P<len>(\d+)), +Instance +ID'
                          ' +(?P<iid>(\d+)), +Checksum +(?P<csum>(\d+)),'
                          ' +Auth +Type +(?P<auth>(\d+)),?$')

        # Version 0, Bad Source 0, No Virtual Link 0,
        p15 = re.compile(r'^Version +(?P<version>(\d+)), +Bad +Source'
                          ' +(?P<bad_source>(\d+)), +No +Virtual +Link'
                          ' +(?P<no_virtual_link>(\d+)),?$')

        # Area Mismatch 0, No Sham Link 0, Self Originated 0,
        p16 = re.compile(r'^Area +Mismatch +(?P<area_mismatch>(\d+)),'
                          ' +No +Sham +Link +(?P<no_sham_link>(\d+)),'
                          ' +Self +Originated +(?P<self_originated>(\d+)),?$')

        # Duplicate ID 0, Hello 0, MTU Mismatch 0,
        p17 = re.compile(r'^Duplicate +ID +(?P<duplicate_id>(\d+)),'
                          ' +Hello +(?P<hello>(\d+)), +MTU +Mismatch'
                          ' +(?P<mtu_mismatch>(\d+)),$')

        # Nbr Ignored 0, LLS 0, Unknown Neighbor 0,
        p18 = re.compile(r'^Nbr +Ignored +(?P<nbr_ignored>(\d+)), +LLS'
                          ' +(?P<lls>(\d+)), +Unknown +Neighbor'
                          ' +(?P<unknown_neighbor>(\d+)),?$')

        # Authentication 0, TTL Check Fail 0, Adjacency Throttle 0,
        p19 = re.compile(r'^Authentication +(?P<authentication>(\d+)), +TTL'
                          ' +Check +Fail +(?P<ttl_check_fail>(\d+)), +Adjacency'
                          ' +Throttle +(?P<adjacency_throttle>(\d+)),?$')

        # BFD 0, Test discard 0
        p20 = re.compile(r'^BFD +(?P<bfd>(\d+)), +Test +discard'
                          ' +(?P<test_discard>(\d+))$')

        # OSPF LSA errors
        p21 = re.compile(r'^OSPF +LSA +errors$')

        # Type 0, Length 0, Data 0, Checksum 0
        p22 = re.compile(r'^Type +(?P<type>(\d+)), +Length +(?P<len>(\d+)),'
                          ' +Data +(?P<data>(\d+)), +Checksum +(?P<csum>(\d+))$')

        # Summary traffic statistics for process ID 65109:
        p23 = re.compile(r'^Summary +traffic +statistics +for +process +ID'
                          ' +(?P<pid>(\d+)):$')

        for line in out.splitlines():
            line = line.strip()

            # OSPF statistics:
            m = p1.match(line)
            if m:
                ospf_stats_dict = ret_dict.setdefault('ospf_statistics', {})
                continue

            # Last clearing of OSPF traffic counters never
            # Last clearing of interface traffic counters never
            m = p2.match(line)
            if m:
                if m.groupdict()['type'] == 'OSPF':
                    ospf_stats_dict['last_clear_traffic_counters'] = \
                                                m.groupdict()['last_clear']
                if m.groupdict()['type'] == 'interface':
                    intf_dict['last_clear_traffic_counters'] = \
                                                m.groupdict()['last_clear']
                continue

            # Rcvd: 2112690 total, 0 checksum errors
            m = p3.match(line)
            if m:
                group = m.groupdict()
                rcvd_dict = ospf_stats_dict.setdefault('rcvd', {})
                rcvd_dict['total'] = int(group['total'])
                rcvd_dict['checksum_errors'] = int(group['csum_errors'])
                received = True ; sent = False
                continue

            # 2024732 hello, 938 database desc, 323 link state req
            # 2381794 hello, 1176 database desc, 43 link state req
            m = p4.match(line)
            if m:
                group = m.groupdict()
                if received:
                    sdict = rcvd_dict
                elif sent:
                    sdict = sent_dict
                else:
                    continue
                sdict['hello'] = int(group['hello'])
                sdict['database_desc'] = int(group['db_desc'])
                sdict['link_state_req'] = int(group['link_state_req'])
                continue

            # 11030 link state updates, 75666 link state acks
            # 92224 link state updates, 8893 link state acks
            m = p5.match(line)
            if m:
                group = m.groupdict()
                if received:
                    sdict = rcvd_dict
                elif sent:
                    sdict = sent_dict
                else:
                    continue
                sdict['link_state_updates'] = int(group['link_state_updates'])
                sdict['link_state_acks'] = int(group['link_state_acks'])
                continue

            # Sent: 2509472 total
            m = p6.match(line)
            if m:
                group = m.groupdict()
                sent_dict = ospf_stats_dict.setdefault('sent', {})
                sent_dict['total'] = int(group['total'])
                sent = True ; received = False
                continue

            # OSPF Router with ID (10.169.197.252) (Process ID 65109)
            # OSPF Router with ID (10.36.3.3) (Process ID 1, VRF VRF1)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                router_id = str(group['router_id'])
                instance = str(group['instance'])
                if group['vrf']:
                    vrf = str(group['vrf'])
                else:
                    vrf = 'default'
                # Create dict
                ospf_dict = ret_dict.setdefault('vrf', {}).\
                                     setdefault(vrf, {}).\
                                     setdefault('address_family', {}).\
                                     setdefault(address_family, {}).\
                                     setdefault('instance', {}).\
                                     setdefault(instance, {})
                ospf_dict['router_id'] = router_id
                continue

            # OSPF queue statistics for process ID 65109:
            m = p8.match(line)
            if m:
                queue_stats_dict = ospf_dict.setdefault('ospf_queue_statistics', {})
                continue

            #                   InputQ   UpdateQ      OutputQ
            # Limit             0        200          0
            # Drops             0          0          0
            # Max delay [msec] 49          2          2
            # Invalid           0          0          0
            # Hello             0          0          0
            # DB des            0          0          0
            # LS req            0          0          0
            # LS upd            0          0          0
            # LS ack           14         14          6
            m = p9_1.match(line)
            if m:
                group = m.groupdict()
                item = group['item'].strip().lower().replace(" ", "_").\
                                    replace("[", "").replace("]", "")
                if max_size_stats:
                    tmp_dict = max_size_queue_stats_dict.setdefault(item, {})
                elif current_size_stats:
                    tmp_dict = current_size_queue_stats_dict.setdefault(item, {})
                else:
                    tmp_dict = queue_stats_dict.setdefault(item, {})
                tmp_dict['inputq'] = int(group['inputq'])
                tmp_dict['updateq'] = int(group['updateq'])
                tmp_dict['outputq'] = int(group['outputq'])
                continue

            #                   InputQ   UpdateQ      OutputQ
            # Max size         14         14          6
            # Current size      0          0          0
            m = p9_2.match(line)
            if m:
                group = m.groupdict()
                item = group['item'].strip().lower().replace(" ", "_")
                tmp_dict = queue_stats_dict.setdefault(item, {})
                if item == 'max_size':
                    max_size_stats = True
                    current_size_stats = False
                    max_size_queue_stats_dict = tmp_dict
                elif item == 'current_size':
                    current_size_stats = True
                    max_size_stats = False
                    current_size_queue_stats_dict = tmp_dict
                tmp_dict.setdefault('total', {})['inputq'] = int(group['inputq'])
                tmp_dict.setdefault('total', {})['updateq'] = int(group['updateq'])
                tmp_dict.setdefault('total', {})['outputq'] = int(group['outputq'])
                continue

            # Interface statistics:
            m = p10.match(line)
            if m:
                intf_stats_dict = ospf_dict.setdefault('interface_statistics', {})
                continue

            # Interface GigabitEthernet0/0/6
            m = p11.match(line)
            if m:
                intf = m.groupdict()['intf']
                intf_dict = intf_stats_dict.setdefault('interfaces', {}).\
                                            setdefault(intf, {})
                interface_stats = True ; summary_stats = False
                continue

            # Type          Packets              Bytes
            # RX Invalid    0                    0
            # RX Hello      169281               8125472
            # RX DB des     36                   1232
            # RX LS req     20                   25080
            # RX LS upd     908                  76640
            # RX LS ack     9327                 8733808
            # RX Total      179572               16962232
            # TX Failed     0                    0
            # TX Hello      169411               13552440
            # TX DB des     40                   43560
            # TX LS req     4                    224
            # TX LS upd     12539                12553264
            # TX LS ack     899                  63396
            # TX Total      182893               26212884
            m = p12.match(line)
            if m:
                group = m.groupdict()
                if interface_stats:
                    sdict = intf_dict
                elif summary_stats:
                    sdict = summary_stats_dict
                else:
                    continue
                item_type = group['type'].strip().lower().replace(" ", "_")
                tmp_dict = sdict.setdefault('ospf_packets_received_sent', {}).\
                            setdefault('type', {}).setdefault(item_type, {})
                tmp_dict['packets'] = int(group['packets'])
                tmp_dict['bytes'] = int(group['bytes'])
                continue

            # OSPF header errors
            m = p13.match(line)
            if m:
                group = m.groupdict()
                if interface_stats:
                    sdict = intf_dict
                elif summary_stats:
                    sdict = summary_stats_dict
                else:
                    continue
                ospf_header_errors_dict = sdict.setdefault('ospf_header_errors', {})
                continue

            # Length 0, Instance ID 0, Checksum 0, Auth Type 0,
            m = p14.match(line)
            if m:
                group = m.groupdict()
                ospf_header_errors_dict['length'] = int(group['len'])
                ospf_header_errors_dict['instance_id'] = int(group['iid'])
                ospf_header_errors_dict['checksum'] = int(group['csum'])
                ospf_header_errors_dict['auth_type'] = int(group['auth'])
                continue

            # Version 0, Bad Source 0, No Virtual Link 0,
            m = p15.match(line)
            if m:
                group = m.groupdict()
                ospf_header_errors_dict['version'] = int(group['version'])
                ospf_header_errors_dict['bad_source'] = int(group['bad_source'])
                ospf_header_errors_dict['no_virtual_link'] = int(group['no_virtual_link'])
                continue

            # Area Mismatch 0, No Sham Link 0, Self Originated 0,
            m = p16.match(line)
            if m:
                group = m.groupdict()
                ospf_header_errors_dict['area_mismatch'] = int(group['area_mismatch'])
                ospf_header_errors_dict['no_sham_link'] = int(group['no_sham_link'])
                ospf_header_errors_dict['self_originated'] = int(group['self_originated'])
                continue

            # Duplicate ID 0, Hello 0, MTU Mismatch 0,
            m = p17.match(line)
            if m:
                group = m.groupdict()
                ospf_header_errors_dict['duplicate_id'] = int(group['duplicate_id'])
                ospf_header_errors_dict['hello'] = int(group['hello'])
                ospf_header_errors_dict['mtu_mismatch'] = int(group['mtu_mismatch'])
                continue

            # Nbr Ignored 0, LLS 0, Unknown Neighbor 0,
            m = p18.match(line)
            if m:
                group = m.groupdict()
                ospf_header_errors_dict['nbr_ignored'] = int(group['nbr_ignored'])
                ospf_header_errors_dict['lls'] = int(group['lls'])
                ospf_header_errors_dict['unknown_neighbor'] = int(group['unknown_neighbor'])
                continue

            # Authentication 0, TTL Check Fail 0, Adjacency Throttle 0,
            m = p19.match(line)
            if m:
                group = m.groupdict()
                ospf_header_errors_dict['authentication'] = int(group['authentication'])
                ospf_header_errors_dict['ttl_check_fail'] = int(group['ttl_check_fail'])
                ospf_header_errors_dict['adjacency_throttle'] = int(group['adjacency_throttle'])
                continue

            # BFD 0, Test discard 0
            m = p20.match(line)
            if m:
                group = m.groupdict()
                ospf_header_errors_dict['bfd'] = int(group['bfd'])
                ospf_header_errors_dict['test_discard'] = int(group['test_discard'])
                continue

            # OSPF LSA errors
            m = p21.match(line)
            if m:
                if interface_stats:
                    sdict = intf_dict
                elif summary_stats:
                    sdict = summary_stats_dict
                else:
                    continue
                ospf_lsa_errors_dict = sdict.setdefault('ospf_lsa_errors', {})
                continue

            # Type 0, Length 0, Data 0, Checksum 0
            m = p22.match(line)
            if m:
                group = m.groupdict()
                ospf_lsa_errors_dict['type'] = int(group['type'])
                ospf_lsa_errors_dict['length'] = int(group['len'])
                ospf_lsa_errors_dict['data'] = int(group['data'])
                ospf_lsa_errors_dict['checksum'] = int(group['csum'])
                continue

            # Summary traffic statistics for process ID 65109:
            m = p23.match(line)
            if m:
                summary_stats_dict = ospf_dict.\
                                setdefault('summary_traffic_statistics', {})
                interface_stats = False ; summary_stats = True
                continue

        return ret_dict


# ===========================
# Schema for:
#   * 'show ip ospf neighbor'
# ===========================
class ShowIpOspfNeighborSchema(MetaParser):

    ''' Schema for:
        * 'show ip ospf neighbor'
    '''

    schema = {
        'interfaces':
            {Any():
                {'neighbors':
                    {Any():
                        {'priority': int,
                        'state':str,
                        'dead_time':str,
                        'address':str,
                        },
                    },
                },
            },
        }


# ===========================
# Parser for:
#   * 'show ip ospf neighbor'
# ===========================
class ShowIpOspfNeighbor(ShowIpOspfNeighborSchema):

    ''' Parser for:
        * 'show ip ospf neighbor'
    '''

    cli_command = 'show ip ospf neighbor'

    def cli(self, output=None):

        if output is None:
            # Execute command on device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}

        # Neighbor ID     Pri   State           Dead Time   Address         Interface
        # 172.16.197.253 128   FULL/DR         00:00:30    172.16.165.49  GigabitEthernet0/0/1
        
        p1=re.compile(r'^(?P<neighbor>\S+) +(?P<pri>\d+) +(?P<state>\S+) +(?P<dead_time>\S+)'
                       ' +(?P<address>\S+) +(?P<interface>\S+)$')

        for line in out.splitlines():

            line = line.strip()
            m = p1.match(line)
            if m:
                neighbor = m.groupdict()['neighbor']
                interface = m.groupdict()['interface']

                #Build Dict

                intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(interface, {})
                nbr_dict = intf_dict.setdefault('neighbors', {}).setdefault(neighbor, {})

                # Set values
                nbr_dict['priority'] = int(m.groupdict()['pri'])
                nbr_dict['state'] = str(m.groupdict()['state'])
                nbr_dict['dead_time'] = str(m.groupdict()['dead_time'])
                nbr_dict['address'] = str(m.groupdict()['address'])
                continue

        return ret_dict

