''' show_ospf.py

NXOS parsers for the following show commands:

Completed:
    * show ip ospf
    * show ip ospf vrf <WORD>
    * show ip ospf mpls ldp interface 
    * show ip ospf mpls ldp interface vrf <WORD>
    * show ip ospf sham-links
    * show ip ospf sham-links vrf <WORD>
    * show ip ospf virtual-links
    * show ip ospf virtual-links vrf <WORD>

Pending:
    * show ip ospf interface
    * show ip ospf interface vrf <WORD>
    
    * show ip route ospf
    * show ip route ospf vrf <WORD>
    
    * show ip ospf neighbors detail
    * show ip ospf neighbors detail vrf <WORD>

    * show ip ospf database external detail
    * show ip ospf database external detail vrf <WORD>

    * show ip ospf database router detail
    * show ip ospf database router detail vrf <WORD>
    
    * show ip ospf database network detail
    * show ip ospf database network detail vrf <WORD>
    
    * show ip ospf database summary detail
    * show ip ospf database summary detail vrf <WORD>
    
    * show ip ospf database opaque-area detail
    * show ip ospf database opaque-area detail vrf <WORD>
    
    * show ip ospf database opaque-as detaill
    * show ip ospf database opaque-as detail vrf <WORD>
    
    * show ip ospf database opaque-link detail
    * show ip ospf database opaque-link detail vrf <WORD>
'''

# Python
import re

# Metaparser
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional
from parser.utils.common import Common


# ======================================
# Schema for 'show ip ospf [vrf <WORD>]'
# ======================================
class ShowIpOspfSchema(MetaParser):

    '''Schema for "show ip ospf [vrf <WORD>]" '''

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'instance': {
                            Any(): {
                                'router_id': str,
                                'instance': int,
                                Optional('nsr'): {
                                    'enable': bool
                                },
                                Optional('graceful_restart'): {
                                    Any(): {
                                        'enable': bool,
                                        'type': str,
                                        'restart_interval': int,
                                        'exist_status': str
                                    }
                                },
                                'single_tos_routes_enable': bool,
                                'opaque_lsa_enable': bool,
                                'preference': {
                                    'single_value': {
                                        'all': int,
                                    }
                                },
                                Optional('bfd'): {
                                    'enable': bool
                                },
                                'auto_cost': {
                                    'enable': bool,
                                    'reference_bandwidth': int,
                                    'bandwidth_unit': str,
                                },
                                'spf_control': {
                                    'paths': int,
                                    'throttle': {
                                        'spf': {
                                            'start': int,
                                            'hold': int,
                                            'maximum': int
                                        },
                                        'lsa': {
                                            'start': int,
                                            'hold': int,
                                            'maximum': int,
                                            Optional('minimum'): int,
                                            Optional('group_pacing'): int,
                                            Optional('external'): int,
                                            Optional('checksum'): str,
                                            Optional('opaque_as'): int,
                                            Optional('opaque_as_checksum'): str,
                                        }
                                    }
                                },
                                Optional('database_control'): {
                                    'max_lsa': int
                                },
                                Optional('stub_router'): {
                                    'always': {
                                        'always': bool
                                    }
                                },
                                'numbers': {
                                    Any(): {
                                        'number': int,
                                        'normal': int,
                                        'stub': int,
                                        'nssa': int
                                    }
                                },
                                'enable': bool,
                                'area': {
                                    Any(): {
                                        'area_type': str,
                                        'area_id': str,
                                        'existed': str,
                                        Optional('default_cost'): int,
                                        'number': {                                            
                                            'interfaces': int,
                                            'active_interfaces': int,
                                            'passive_interfaces': int,
                                            'loopback_interfaces': int
                                        },
                                        Optional('ranges'): {
                                            'prefix': str,
                                            'advertise': bool,
                                            'cost': int,
                                            'net': int,
                                        },
                                        Optional('authentication'): str,
                                        'statistics': {
                                            'spf_runs_count': int,                                            
                                            'spf_last_run_time': float,
                                            'area_scope_lsa_count': int,
                                            'area_scope_lsa_cksum_sum': str,
                                            Optional('as_nssa_translator_event_count'): int,
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


# ======================================
# Parser for 'show ip ospf [vrf <WORD>]'
# ======================================
class ShowIpOspf(ShowIpOspfSchema):

    ''' Parser for "show ip ospf [vrf <WORD>]" '''

    def cli(self, vrf=''):
        # excute command to get output
        out = self.device.execute('show ip ospf' if not vrf else
                                  'show ip ospf vrf {}'.format(vrf))
        ret_dict = {}
        sub_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Routing Process 1 with ID 2.2.2.2 VRF default
            p1 = re.compile(r'^Routing +Process +(?P<instance>\d+) +'
                             'with +ID +(?P<router_id>[\d\.]+) +'
                             'VRF +(?P<vrf>\S+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                instance = m.groupdict()['instance']
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if 'ipv4' not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family']['ipv4'] = {}
                if 'instance' not in ret_dict['vrf'][vrf]['address_family']['ipv4']:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance'] = {}
                if instance not in ret_dict['vrf'][vrf]['address_family']['ipv4']['instance']:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance'][instance] = {}
                sub_dict = ret_dict['vrf'][vrf]['address_family']['ipv4']['instance'][instance]

                # router_id
                sub_dict['router_id'] = m.groupdict()['router_id']

                # initial 
                gr_enable = None
                continue

            # Routing Process Instance Number 1
            p2 = re.compile(r'^Routing +Process +Instance +Number +(?P<instance>\d+)$')
            m = p2.match(line)
            if m:
                sub_dict['instance'] = int(m.groupdict()['instance'])
                continue

            # Stateful High Availability enabled
            p3 = re.compile(r'^Stateful +High +Availability +(?P<enable>\w+)$')
            m = p3.match(line)
            if m:
                if 'nsr' not in sub_dict:
                    sub_dict['nsr'] = {}
                sub_dict['nsr']['enable'] = True \
                    if 'enable' in m.groupdict()['enable'].lower() else False
                continue

            # Graceful-restart is configured
            p4 = re.compile(r'^Graceful\-restart +is +(?P<gr_enable>\w+)$')
            m = p4.match(line)
            if m:
                if 'graceful_restart' not in sub_dict:
                    sub_dict['graceful_restart'] = {}
                gr_enable = True \
                    if 'configured' in m.groupdict()['gr_enable'].lower() else False
                continue

            # Grace period: 60 state: Inactive 
            p5 = re.compile(r'^Grace +period: +(?P<interval>\w+) +'
                             'state: +(?P<state>\w+)$')
            m = p5.match(line)
            if m:
                if 'graceful_restart' not in sub_dict:
                    sub_dict['graceful_restart'] = {}
                restart_interval = int(m.groupdict()['interval'])
                gr_type = 'ietf'
                if gr_type not in sub_dict['graceful_restart']:
                    sub_dict['graceful_restart'][gr_type] = {}

                sub_dict['graceful_restart'][gr_type]['type'] = gr_type
                sub_dict['graceful_restart'][gr_type]['restart_interval'] = restart_interval
                if gr_enable:
                    sub_dict['graceful_restart'][gr_type]['enable'] = gr_enable
                
                continue

            # Last graceful restart exit status: None
            p6 = re.compile(r'^Last +graceful +restart +exit +status: +(?P<status>\w+)$')
            m = p6.match(line)
            if m:
                try:
                    sub_dict['graceful_restart'][gr_type]['exist_status'] = \
                        m.groupdict()['status'].lower()
                except:
                    pass
                continue

            # Supports only single TOS(TOS0) routes
            p7 = re.compile(r'^Supports +only +single +TOS\(TOS0\) +routes$')
            m = p7.match(line)
            if m:
                sub_dict['single_tos_routes_enable'] = True
                continue

            # Supports opaque LSA
            p8 = re.compile(r'^Supports +opaque +LSA$')
            m = p8.match(line)
            if m:
                sub_dict['opaque_lsa_enable'] = True
                continue

            # Administrative distance 110
            p9 = re.compile(r'^Administrative +distance +(?P<pref_all>\d+)$')
            m = p9.match(line)
            if m:
                if 'preference' not in sub_dict:
                    sub_dict['preference'] = {}
                if 'single_value' not in sub_dict['preference']:
                    sub_dict['preference']['single_value'] = {}
                sub_dict['preference']['single_value']['all'] = int(m.groupdict()['pref_all'])
                continue

            # BFD is enabled
            p10 = re.compile(r'^BFD +is +(?P<status>\w+)$')
            m = p10.match(line)
            if m:
                if 'bfd' not in sub_dict:
                    sub_dict['bfd'] = {}
                sub_dict['bfd']['enable'] = True \
                    if 'enable' in m.groupdict()['status'].lower() else False
                continue

            # Reference Bandwidth is 40000 Mbps
            p11 = re.compile(r'^Reference +Bandwidth +is +(?P<bd>\d+) +(?P<unit>\w+)$')
            m = p11.match(line)
            if m:
                if 'auto_cost' not in sub_dict:
                    sub_dict['auto_cost'] = {}
                sub_dict['auto_cost']['enable'] = True
                sub_dict['auto_cost']['reference_bandwidth'] = int(m.groupdict()['bd'])
                sub_dict['auto_cost']['bandwidth_unit'] = m.groupdict()['unit']
                continue

            # SPF throttling delay time of 200.000 msecs,
            p12 = re.compile(r'^SPF +throttling +delay +time +of +(?P<time>[\d\.]+) +msecs,$')
            m = p12.match(line)
            if m:
                start = int(m.groupdict()['time'].replace('.', ''))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'spf' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['spf'] = {}
                sub_dict['spf_control']['throttle']['spf']['start'] = start
                continue

            # SPF throttling hold time of 1000.000 msecs, 
            p13 = re.compile(r'^SPF +throttling +hold +time +of +(?P<time>[\d\.]+) +msecs,$')
            m = p13.match(line)
            if m:
                hold = int(m.groupdict()['time'].replace('.', ''))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'spf' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['spf'] = {}
                sub_dict['spf_control']['throttle']['spf']['hold'] = hold
                continue

            # SPF throttling maximum wait time of 5000.000 msecs
            p14 = re.compile(r'^SPF +throttling +maximum +wait +time +of +(?P<time>[\d\.]+) +msecs$')
            m = p14.match(line)
            if m:
                maximum = int(m.groupdict()['time'].replace('.', ''))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'spf' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['spf'] = {}
                sub_dict['spf_control']['throttle']['spf']['maximum'] = maximum
                continue

            # LSA throttling start time of 0.000 msecs,
            p15 = re.compile(r'^LSA +throttling +start +time +of +(?P<time>[\d\.]+) +msecs,$')
            m = p15.match(line)
            if m:
                start = int(m.groupdict()['time'].replace('.', ''))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'lsa' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['lsa'] = {}
                sub_dict['spf_control']['throttle']['lsa']['start'] = start
                continue

            # LSA throttling hold interval of 5000.000 msecs, 
            p16 = re.compile(r'^LSA +throttling +hold +interval +of +(?P<time>[\d\.]+) +msecs,$')
            m = p16.match(line)
            if m:
                hold = int(m.groupdict()['time'].replace('.', ''))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'lsa' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['lsa'] = {}
                sub_dict['spf_control']['throttle']['lsa']['hold'] = hold
                continue

            # LSA throttling maximum wait time of 5000.000 msecs
            p17 = re.compile(r'^LSA +throttling +maximum +wait +time +of +(?P<time>[\d\.]+) +msecs$')
            m = p17.match(line)
            if m:
                maximum = int(m.groupdict()['time'].replace('.', ''))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'lsa' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['lsa'] = {}
                sub_dict['spf_control']['throttle']['lsa']['maximum'] = maximum
                continue

            # Minimum LSA arrival 1000.000 msec
            p18 = re.compile(r'^Minimum +LSA +arrival +(?P<time>[\d\.]+) +msecs$')
            m = p18.match(line)
            if m:
                minimum = int(m.groupdict()['time'].replace('.', ''))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'lsa' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['lsa'] = {}
                sub_dict['spf_control']['throttle']['lsa']['minimum'] = minimum
                continue

            # Maximum number of non self-generated LSA allowed 123
            p19 = re.compile(r'^Maximum +number +of +non +self\-generated +'
                              'LSA +allowed +(?P<max>\d+)$')
            m = p19.match(line)
            if m:
                if 'database_control' not in sub_dict:
                    sub_dict['database_control'] = {}
                sub_dict['database_control']['max_lsa'] = int(m.groupdict()['max'])
                continue

            # Originating router LSA with maximum metric
            p19 = re.compile(r'^Originating +router +LSA +with +maximum +metric$')
            m = p19.match(line)
            if m:
                if 'stub_router' not in sub_dict:
                    sub_dict['stub_router'] = {}
                if 'always' not in sub_dict['stub_router']:
                    sub_dict['stub_router']['always'] = {}
                sub_dict['stub_router']['always']['always'] = True
                continue

            # LSA group pacing timer 10 secs
            p20 = re.compile(r'^LSA +group +pacing +timer +(?P<time>\d+) +secs$')
            m = p20.match(line)
            if m:
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'lsa' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['lsa'] = {}
                sub_dict['spf_control']['throttle']['lsa']['group_pacing'] = int(m.groupdict()['time'])
                continue

            # Maximum paths to destination 8
            p21 = re.compile(r'^Maximum paths to destination +(?P<path>\d+)$')
            m = p21.match(line)
            if m:
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                sub_dict['spf_control']['paths'] = int(m.groupdict()['path'])
                continue

            # Number of external LSAs 1, checksum sum 0x7d61
            p22 = re.compile(r'^Number +of +external +LSAs +(?P<ext_num>\d+), +'
                              'checksum +sum +(?P<chk_sum>\w+)$')
            m = p22.match(line)
            if m:
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'lsa' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['lsa'] = {}

                sub_dict['spf_control']['throttle']['lsa']['external'] = \
                    int(m.groupdict()['ext_num'])
                sub_dict['spf_control']['throttle']['lsa']['checksum'] = \
                    m.groupdict()['chk_sum']
                continue

            # Number of opaque AS LSAs 0, checksum sum 0
            p23 = re.compile(r'^Number +of +opaque +AS +LSAs +(?P<ext_num>\d+), +'
                              'checksum +sum +(?P<chk_sum>\w+)$')
            m = p23.match(line)
            if m:
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'lsa' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['lsa'] = {}

                sub_dict['spf_control']['throttle']['lsa']['opaque_as'] = \
                    int(m.groupdict()['ext_num'])
                sub_dict['spf_control']['throttle']['lsa']['opaque_as_checksum'] = \
                    m.groupdict()['chk_sum']
                continue

            # Number of areas is 1, 1 normal, 0 stub, 0 nssa
            p24 = re.compile(r'^Number +of +areas +is +(?P<num>\d+), +'
                              '(?P<normal>\d+) +normal, +'
                              '(?P<stub>\d+) +stub, +'
                              '(?P<nssa>\d+) +nssa$')
            m = p24.match(line)
            if m:
                if 'numbers' not in sub_dict:
                    sub_dict['numbers'] = {}
                if 'areas' not in sub_dict['numbers']:
                    sub_dict['numbers']['areas'] = {}
                sub_dict['numbers']['areas']['number'] = int(m.groupdict()['num'])
                sub_dict['numbers']['areas']['normal'] = int(m.groupdict()['normal'])
                sub_dict['numbers']['areas']['stub'] = int(m.groupdict()['stub'])
                sub_dict['numbers']['areas']['nssa'] = int(m.groupdict()['nssa'])
                continue

            # Number of active areas is 1, 1 normal, 0 stub, 0 nssa
            p25 = re.compile(r'^Number +of +active +areas +is +(?P<num>\d+), +'
                              '(?P<normal>\d+) +normal, +'
                              '(?P<stub>\d+) +stub, +'
                              '(?P<nssa>\d+) +nssa$')
            m = p25.match(line)
            if m:
                if 'numbers' not in sub_dict:
                    sub_dict['numbers'] = {}
                if 'active_areas' not in sub_dict['numbers']:
                    sub_dict['numbers']['active_areas'] = {}
                sub_dict['numbers']['active_areas']['number'] = int(m.groupdict()['num'])
                sub_dict['numbers']['active_areas']['normal'] = int(m.groupdict()['normal'])
                sub_dict['numbers']['active_areas']['stub'] = int(m.groupdict()['stub'])
                sub_dict['numbers']['active_areas']['nssa'] = int(m.groupdict()['nssa'])
                continue

            # Install discard route for summarized external routes.
            # Install discard route for summarized internal routes.
            p26 = re.compile(r'^Install +discard +route +for +'
                              'summarized +(?P<type>\w+) +routes.$')
            m = p26.match(line)
            if m:
                # what key
                continue

            # Area BACKBONE(0.0.0.0) 
            # Area (0.0.0.1)
            # Area BACKBONE(0.0.0.0) (Inactive)
            p27 = re.compile(r'^Area +(?P<type>\w+)?\((?P<area>[\w\.\:]+)\)'
                              '( *\((?P<status>\w+)\))?$')
            m = p27.match(line)
            if m:
                if 'area' not in sub_dict:
                    sub_dict['area'] = {}

                area = m.groupdict()['area']
                if area not in sub_dict['area']:
                    sub_dict['area'][area] = {}
                sub_dict['area'][area]['area_id'] = area

                sub_dict['area'][area]['area_type'] = 'normal'

                if m.groupdict()['status'] and  \
                  'inactive' in m.groupdict()['status'].lower():
                    sub_dict['enable'] = False
                else:
                    sub_dict['enable'] = True
                continue

            # This area is a STUB area
            p34 = re.compile(r'^This +area +is +a +(?P<type>\w+) +area$')
            m = p34.match(line)
            if m:
                sub_dict['area'][area]['area_type'] = m.groupdict()['type'].lower()
                continue

            # Generates stub default route with cost 1
            p35 = re.compile(r'^Generates +stub +default +route +with +'
                              'cost +(?P<cost>\d+)$')
            m = p35.match(line)
            if m:
                sub_dict['area'][area]['default_cost'] = int(m.groupdict()['cost'])
                continue

            #     Area has existed for 08:30:42
            p28 = re.compile(r'^Area +has +existed +for +(?P<time>[\w\.\:]+)$')
            m = p28.match(line)
            if m:
                sub_dict['area'][area]['existed'] = m.groupdict()['time']
                continue

            #     Interfaces in this area: 4 Active interfaces: 4
            p29 = re.compile(r'^Interfaces +in +this +area: +(?P<num1>\d+) +'
                              'Active +interfaces: +(?P<num2>\d+)$')
            m = p29.match(line)
            if m:
                if 'number' not in sub_dict['area'][area]:
                    sub_dict['area'][area]['number'] = {}
                sub_dict['area'][area]['number']['interfaces'] = \
                    int(m.groupdict()['num1'])
                sub_dict['area'][area]['number']['active_interfaces'] = \
                    int(m.groupdict()['num2'])
                continue

            #     Passive interfaces: 0  Loopback interfaces: 1
            p30 = re.compile(r'^Passive +interfaces: +(?P<num1>\d+) +'
                              'Loopback +interfaces: +(?P<num2>\d+)$')
            m = p30.match(line)
            if m:
                if 'number' not in sub_dict['area'][area]:
                    sub_dict['area'][area]['number'] = {}
                sub_dict['area'][area]['number']['passive_interfaces'] = \
                    int(m.groupdict()['num1'])
                sub_dict['area'][area]['number']['loopback_interfaces'] = \
                    int(m.groupdict()['num2'])
                continue

            #     No authentication available

            #     SPF calculation has run 8 times
            p31 = re.compile(r'^SPF +calculation +has +run +(?P<num1>\d+) +times$')
            m = p31.match(line)
            if m:
                if 'statistics' not in sub_dict['area'][area]:
                    sub_dict['area'][area]['statistics'] = {}
                sub_dict['area'][area]['statistics']['spf_runs_count'] = \
                    int(m.groupdict()['num1'])
                continue

            #      Last SPF ran for 0.001386s
            p32 = re.compile(r'^Last +SPF +ran +for +(?P<num1>[\d\.]+)s$')
            m = p32.match(line)
            if m:
                if 'statistics' not in sub_dict['area'][area]:
                    sub_dict['area'][area]['statistics'] = {}
                sub_dict['area'][area]['statistics']['spf_last_run_time'] = \
                    float(m.groupdict()['num1'])
                continue

            #     Area ranges are
            # 1.1.0.0/16 Active (Num nets: 1) DoNotAdvertise Cost configured 31
            # 1.1.1.0/24 Passive (Num nets: 0) Advertise Cost configured 33
            p36 = re.compile(r'^(?P<prefix>[\d\/\.]+) +'
                              '(Active|Passive) +\(Num +nets: +(?P<net>\d+)\) +'
                              '(?P<advertise>\w+) +'
                              'Cost +configured +(?P<cost>\d+)$')
            m = p36.match(line)
            if m:
                if 'ranges' not in sub_dict['area'][area]:
                    sub_dict['area'][area]['ranges'] = {}
                sub_dict['area'][area]['ranges']['prefix'] = \
                    m.groupdict()['prefix']
                sub_dict['area'][area]['ranges']['cost'] = \
                    int(m.groupdict()['cost'])
                sub_dict['area'][area]['ranges']['net'] = \
                    int(m.groupdict()['net'])
                sub_dict['area'][area]['ranges']['advertise'] = False if \
                    'donot' in m.groupdict()['advertise'].lower() else True
                continue


            #     Number of LSAs: 19, checksum sum 0x7a137
            p33 = re.compile(r'^Number +of +LSAs: +(?P<num1>\d+), +'
                              'checksum +sum +(?P<num2>\w+)$')
            m = p33.match(line)
            if m:
                if 'statistics' not in sub_dict['area'][area]:
                    sub_dict['area'][area]['statistics'] = {}
                sub_dict['area'][area]['statistics']['area_scope_lsa_count'] = \
                    int(m.groupdict()['num1'])
                sub_dict['area'][area]['statistics']\
                    ['area_scope_lsa_cksum_sum'] = m.groupdict()['num1']
                continue

        return ret_dict


# =========================================================
# Schema for 'show ip ospf mpls ldp interface [vrf <WORD>]'
# =========================================================
class ShowIpOspfMplsLdpInterfaceSchema(MetaParser):

    ''' Schema for "show ip ospf mpls ldp interface [vrf <WORD>]" '''

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'instance': {
                            Any(): {
                                'interface': {
                                    Any(): {                                    
                                        'area': str,
                                        'interface': str,
                                        'state': str,
                                        'network_type': str,
                                        'ldp': {                                                        
                                            'autoconfig': bool,
                                            'autoconfig_area_id': str,
                                            'igp_sync': bool
                                        }
                                    },
                                }
                            },
                        }
                    },
                }
            }
        }
    }


# =========================================================
# Parser for 'show ip ospf mpls ldp interface [vrf <WORD>]'
# =========================================================
class ShowIpOspfMplsLdpInterface(ShowIpOspfMplsLdpInterfaceSchema):

    ''' Parser for "show ip ospf mpls ldp interface [vrf <WORD>]" '''

    def cli(self, vrf=''):
        # excute command to get output
        out = self.device.execute('show ip ospf mpls ldp interface' if not vrf else
                                  'show ip ospf mpls ldp interface vrf {}'.format(vrf))
        ret_dict = {}
        sub_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Ethernet2/2 - Process ID 1 VRF default, area 0.0.0.0
            # SL1-0.0.0.0-22.22.22.22-11.11.11.11 - Process ID 1 VRF VRF1, area 0.0.0.1
            p1 = re.compile(r'^(?P<intf>[\w\.\-\/]+) +\- +'
                             'Process +ID +(?P<instance>\d+) +'
                             'VRF +(?P<vrf>\S+), +'
                             'area +(?P<area>[\w\.]+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                instance = m.groupdict()['instance']
                intf = m.groupdict()['intf']
                area = m.groupdict()['area']

                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if 'ipv4' not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family']['ipv4'] = {}
                if 'instance' not in ret_dict['vrf'][vrf]['address_family']['ipv4']:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance'] = {}
                if instance not in ret_dict['vrf'][vrf]['address_family']['ipv4']['instance']:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance'][instance] = {}
                if 'interface' not in ret_dict['vrf'][vrf]['address_family']['ipv4']['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance'][instance]['interface'] = {}
                if intf not in ret_dict['vrf'][vrf]['address_family']['ipv4']['instance'][instance]['interface']:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance'][instance]['interface'][intf] = {}
                sub_dict = ret_dict['vrf'][vrf]['address_family']['ipv4']['instance'][instance]['interface'][intf]

                # area
                sub_dict['area'] = area

                if 'ldp' not in sub_dict:
                    sub_dict['ldp'] = {}
                sub_dict['ldp']['autoconfig_area_id'] = area

                # interface
                sub_dict['interface'] = intf
                continue

            # LDP Autoconfig not enabled
            p2 = re.compile(r'^LDP +Autoconfig +not +enabled$')
            m = p2.match(line)
            if m:
                sub_dict['ldp']['autoconfig'] = False
                continue

            # LDP Autoconfig is enabled
            p2_1 = re.compile(r'^LDP +Autoconfig +is +enabled$')
            m = p2_1.match(line)
            if m:
                sub_dict['ldp']['autoconfig'] = True
                continue

            # LDP Sync is enabled, not required
            p3_1 = re.compile(r'^LDP +Sync +is +enabled, +not +required$')
            m = p3_1.match(line)
            if m:
                sub_dict['ldp']['igp_sync'] = True
                continue

            # LDP Sync not enabled, not required
            p3_2 = re.compile(r'^LDP +Sync +not +enabled, +not +required$')
            m = p3_2.match(line)
            if m:
                sub_dict['ldp']['igp_sync'] = False
                continue

            # State LOOPBACK, Network type LOOPBACK
            p4 = re.compile(r'^State +(?P<state>\w+), +'
                             'Network +type +(?P<type>\w+)$')
            m = p4.match(line)
            if m:
                sub_dict['state'] = m.groupdict()['state'].lower()
                sub_dict['network_type'] = m.groupdict()['type'].lower()
                continue

        return ret_dict


# ===========================================
# Superparser for:
# * 'show ip ospf sham-links [vrf <WORD>]'
# * 'show ip ospf virtual-links [vrf <WORD>]'
# ===========================================
class ShowIpOspfLinksSuperParser(MetaParser):

    ''' Parser for:
        * "show ip ospf sham-links [vrf <WORD>]"
        * "show ip ospf virtual-links [vrf <WORD>]"
    '''

    def cli(self, cmd):
        # excute command to get output
        out = self.device.execute(cmd)
        ret_dict = {}
        sub_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Virtual link VL1 to router 4.4.4.4 is up
            p1 = re.compile(r'^Virtual +link +(?P<link>\w+) +to +router +'
                             '(?P<router_id>[\w\.\:]+) +is +(?P<state>\w+)$')
            m = p1.match(line)
            if m:
                link = m.groupdict()['link']
                router_id = m.groupdict()['router_id']
                state = m.groupdict()['state']
                link_type = 'virtual_links'
                continue


            # SL1-0.0.0.0-22.22.22.22-11.11.11.11 line protocol is up
            p1_1 = re.compile(r'^(?P<link>\w+)-(?P<area>[\w\.\:]+)-'
                               '(?P<local>[\w\.\:]+)-'
                               '(?P<remote>[\w\.\:]+) +'
                               'line +protocol +is +(?P<state>\w+)$')
            m = p1_1.match(line)
            if m:
                link = m.groupdict()['link']
                backbone_area_id = m.groupdict()['area']
                local = m.groupdict()['local']
                remote = m.groupdict()['remote']
                state = m.groupdict()['state']
                link_type = 'sham_links'
                continue

            # Transit area 0.0.0.1, via interface Eth1/5, remote addr 20.3.4.4
            p2 = re.compile(r'^Transit +area +(?P<transit_area_id>[\w\.\:]+), +'
                             'via +interface +(?P<intf>[\w\.\/\-]+), +'
                             'remote +addr +(?P<remote_addr>[\w\.\:]+)$')
            m = p2.match(line)
            if m:
                transit_area_id = m.groupdict()['transit_area_id']
                intf = Common.convert_intf_name(m.groupdict()['intf'])
                remote_addr = m.groupdict()['remote_addr']
                continue

            # Unnumbered interface using IP address of Ethernet1/5 (20.3.4.3)
            # Unnumbered interface using IP address of loopback1 (22.22.22.22)
            p3 = re.compile(r'^Unnumbered +interface +using +IP +address +of +'
                             '(?P<intf>[\w\.\/\-]+) +\((?P<ip>[\w\.\:]+)\)$')
            m = p3.match(line)
            if m:
                unnumbered_interface = m.groupdict()['intf']
                ip_address = m.groupdict()['ip']
                continue

            # Process ID 1 VRF default, area 0.0.0.0
            # Process ID 1 VRF VRF1, area 0.0.0.1
            p4 = re.compile(r'^Process +ID +(?P<inst>\d+) +'
                             'VRF +(?P<vrf>\S+), +area +(?P<area>[\w\.\:]+)$')
            m = p4.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                inst = m.groupdict()['inst']
                area_id = m.groupdict()['area']

                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if 'ipv4' not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family']['ipv4'] = {}
                if 'instance' not in ret_dict['vrf'][vrf]['address_family']['ipv4']:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance'] = {}
                if inst not in ret_dict['vrf'][vrf]['address_family']['ipv4']['instance']:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance'][inst] = {}
                if 'area' not in ret_dict['vrf'][vrf]['address_family']['ipv4']['instance'][inst]:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance'][inst]['area'] = {}


                if link_type == 'virtual_links':
                    backbone_area_id = area_id
                    area_id = transit_area_id
                    key = '{0} {1}'.format(transit_area_id, router_id)
                else:
                    transit_area_id = area_id
                    key = '{0} {1}'.format(local, remote)

                if area_id not in ret_dict['vrf'][vrf]['address_family']['ipv4']['instance'][inst]['area']:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance'][inst]['area'][area_id] = {}
                if link_type not in ret_dict['vrf'][vrf]['address_family']['ipv4']['instance']\
                  [inst]['area'][area_id]:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance'][inst]\
                      ['area'][area_id][link_type] = {}

                if key not in ret_dict['vrf'][vrf]['address_family']['ipv4']['instance']\
                  [inst]['area'][area_id][link_type]:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance'][inst]\
                      ['area'][area_id][link_type][key] = {}

                sub_dict = ret_dict['vrf'][vrf]['address_family']['ipv4']['instance'][inst]\
                  ['area'][area_id][link_type][key]

                # link
                sub_dict['link'] = link

                # link
                sub_dict['link_state'] = state

                # transit_area_id
                sub_dict['transit_area_id'] = transit_area_id

                # backbone_area_id
                sub_dict['backbone_area_id'] = backbone_area_id

                try:
                    # unnumbered_interface
                    sub_dict['unnumbered_interface'] = unnumbered_interface

                    # ip_address
                    sub_dict['ip_address'] = ip_address
                except:
                    pass

                # virtual-links
                #   router_id, interface, remote_addr
                try:
                    sub_dict['router_id'] = router_id
                    sub_dict['interface'] = intf
                    sub_dict['remote_addr'] = remote_addr
                except:
                    pass

                # sham-linksl
                #   local_id, remote_id
                try:
                    sub_dict['local_id'] = local
                    sub_dict['remote_id'] = remote
                except:
                    pass

                continue

            # State P2P, Network type P2P, cost 40
            # State P2P, Network type P2P, cost 1
            p5 = re.compile(r'^State +(?P<state>\w+), +'
                             'Network +type +(?P<network_type>\w+), +'
                             'cost +(?P<cost>\d+)$')
            m = p5.match(line)
            if m:
                sub_dict['state'] = m.groupdict()['state']
                sub_dict['network_type'] = m.groupdict()['network_type']
                sub_dict['cost'] = int(m.groupdict()['cost'])
                continue

            # Index 7, Transmit delay 1 sec
            # Index 6, Transmit delay 1 sec
            p6 = re.compile(r'^Index +(?P<index>\d+), +'
                             'Transmit +delay +(?P<delay>\d+) +sec$')
            m = p6.match(line)
            if m:
                sub_dict['transmit_delay'] = int(m.groupdict()['delay'])
                sub_dict['index'] = int(m.groupdict()['index'])
                continue

            # 1 Neighbors, flooding to 1, adjacent with 1
            # 1 Neighbors, flooding to 1, adjacent with 1
            p7 = re.compile(r'^(?P<nbr_count>\d+) +Neighbors, +'
                             'flooding +to +(?P<flood>\d+), '
                             'adjacent +with +(?P<adjacent>\d+)$')
            m = p7.match(line)
            if m:
                # not sure the structure
                continue

            # Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
            # Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
            p8 = re.compile(r'^Timer +intervals: +Hello +(?P<hello>\d+), +'
                             'Dead +(?P<dead>\d+), +Wait +(?P<wait>\d+), +'
                             'Retransmit +(?P<retransmit>\d+)$')
            m = p8.match(line)
            if m:
                sub_dict['hello_interval'] = int(m.groupdict()['hello'])
                sub_dict['dead_interval'] = int(m.groupdict()['dead'])
                sub_dict['retransmit_interval'] = int(m.groupdict()['retransmit'])
                sub_dict['wait_interval'] = int(m.groupdict()['wait'])
                continue

            # Hello timer due in 00:00:05
            # Hello timer due in 00:00:02
            p9 = re.compile(r'^Hello +timer +due +in +(?P<hello_timer>[\w\.\:]+)$')
            m = p9.match(line)
            if m:
                sub_dict['hello_timer'] = m.groupdict()['hello_timer']
                continue

            # No authentication
            # Simple authentication
            # Simple authentication, using keychain test (ready)
            # Message-digest authentication, using key id 1
            p10 = re.compile(r'^(?P<auth_type>[\w\-]+) +authentication(, +'
                              'using +(?P<key_type>(key +id|keychain)) +'
                              '(?P<key>\w+)( *\((?P<status>\w+)\))?)?$')
            m = p10.match(line)
            if m:
                auth_type = m.groupdict()['auth_type'].lower()
                key_type = m.groupdict()['key_type']
                key = m.groupdict()['key']
                status = m.groupdict()['status']
                if auth_type == 'simple':
                    crypto_algorithm = 'simple'
                elif auth_type == 'message-digest':
                    crypto_algorithm = 'md5'
                else:
                    continue

                if 'authentication' not in sub_dict:
                    sub_dict['authentication'] = {}
                if 'auth_trailer_key' not in sub_dict['authentication']:
                    sub_dict['authentication']['auth_trailer_key'] = {}

                sub_dict['authentication']['auth_trailer_key']['crypto_algorithm'] = crypto_algorithm

                if key_type == 'keychain':
                    if 'auth_trailer_key_chain' not in sub_dict['authentication']:
                        sub_dict['authentication']['auth_trailer_key_chain'] = {}
                    sub_dict['authentication']['auth_trailer_key_chain']['key_chain'] = key
                    if status:
                        sub_dict['authentication']['auth_trailer_key_chain']['status'] = status
                elif key_type:
                    sub_dict['authentication']['key_id'] = key

                continue

            # Number of opaque link LSAs: 0, checksum sum 0
            # Number of opaque link LSAs: 0, checksum sum 0
            p11 = re.compile(r'^Number +of +opaque +link +LSAs: +(?P<count>\d+), +'
                              'checksum +sum +(?P<checksum>\d+)$')
            m = p11.match(line)
            if m:
                if 'statistics' not in sub_dict:
                    sub_dict['statistics'] = {}

                sub_dict['statistics']['link_scope_lsa_count'] = \
                    int(m.groupdict()['count'])
                sub_dict['statistics']['link_scope_lsa_cksum_sum'] = \
                    int(m.groupdict()['checksum'])
                continue

            # Adjacency Information
            # Adjacency Information :
            p12 = re.compile(r'^Adjacency +Information *:?$')
            m = p12.match(line)
            if m:
                continue

            #   Destination IP address: 11.11.11.11
            p13 = re.compile(r'^Destination +IP +address: +(?P<dest>[\w\.\:]+)$')
            m = p13.match(line)
            if m:
                sub_dict['destination'] = m.groupdict()['dest']
                continue

            #   Neighbor 11.11.11.11, interface address 11.11.11.11
            p14 = re.compile(r'^Neighbor +(?P<nei>[\w\.\:]+), +'
                              'interface +address +(?P<intf_ip>[\w\.\:]+)$')
            m = p14.match(line)
            if m:
                if 'neighbors' not in sub_dict:
                    sub_dict['neighbors'] = {}
                nbr_router_id = m.groupdict()['nei']
                if nbr_router_id not in sub_dict['neighbors']:
                    sub_dict['neighbors'][nbr_router_id] = {}
                sub_dict['neighbors'][nbr_router_id]['address'] = m.groupdict()['intf_ip']
                sub_dict['neighbors'][nbr_router_id]['neighbor_router_id'] = nbr_router_id
                continue

            #   Process ID 1 VRF VRF1, in area 0.0.0.1 via interface SL1-0.0.0.0-22.22.22.22
            p15 = re.compile(r'^Process +ID +(?P<inst>\d+) +VRF +(?P<vrf>\S+), +'
                              'in +area +(?P<area>[\w\.\:]+) +via +interface +'
                              '(?P<link>\w+)-(?P<backbone>[\w\.\:]+)-'
                               '(?P<local>[\w\.\:]+)$')
            m = p15.match(line)
            if m:
                sub_dict['neighbors'][nbr_router_id]['instance'] = m.groupdict()['inst']
                sub_dict['neighbors'][nbr_router_id]['area'] = m.groupdict()['area']
                sub_dict['neighbors'][nbr_router_id]['backbone_area_id'] = m.groupdict()['backbone']
                sub_dict['neighbors'][nbr_router_id]['local'] = m.groupdict()['local']
                continue

            #   -11.11.11.11
            p16 = re.compile(r'^-(?P<remote>[\w\.\:]+)$')
            m = p16.match(line)
            if m:
                sub_dict['neighbors'][nbr_router_id]['remote'] = m.groupdict()['remote']
                continue

            # State is FULL, 5 state changes, last change 00:07:51
            # State is FULL, 8 state changes, last change 08:10:01
            p17 = re.compile(r'^State +is +(?P<status>\w+), +'
                              '(?P<change>\d+) +state +changes, +'
                              'last +change +(?P<last_change>[\w\.\:]+)$')
            m = p17.match(line)
            if m:
                state = m.groupdict()['status'].lower()
                change = int(m.groupdict()['change'])
                last_change = m.groupdict()['last_change']

                if link_type == 'virtual_links':
                    nbr_router_id = router_id

                if 'neighbors' not in sub_dict:
                    sub_dict['neighbors'] = {}
                if nbr_router_id not in sub_dict['neighbors']:
                    sub_dict['neighbors'][nbr_router_id] = {}
                sub_dict['neighbors'][nbr_router_id]['neighbor_router_id'] = nbr_router_id
                sub_dict['neighbors'][nbr_router_id]['state'] = state
                if 'statistics' not in sub_dict['neighbors'][nbr_router_id]:
                    sub_dict['neighbors'][nbr_router_id]['statistics'] = {}
                sub_dict['neighbors'][nbr_router_id]['statistics']['nbr_event_count'] = change
                sub_dict['neighbors'][nbr_router_id]['last_change'] = last_change

                # virtual_links 
                #    address    
                try:
                    sub_dict['neighbors'][nbr_router_id]['address'] = remote_addr
                except:
                    pass
                continue

            # Hello options 0x32, dbd options 0x72
            # Hello options 0x32, dbd options 0x72
            p18 = re.compile(r'^Hello +options +(?P<hello>\w+), +'
                              'dbd +options +(?P<dbd>\w+)$')
            m = p18.match(line)
            if m:
                hello = m.groupdict()['hello']
                dbd = m.groupdict()['dbd']
                sub_dict['neighbors'][nbr_router_id]['hello_option'] = hello
                sub_dict['neighbors'][nbr_router_id]['dbd_option'] = dbd
                continue

            # Last non-hello packet received 00:07:49
            # Last non-hello packet received never
            p19 = re.compile(r'^Last +non\-hello +packet +received +(?P<last>[\w\.\:]+)$')
            m = p19.match(line)
            if m:
                non_hello = m.groupdict()['last']
                sub_dict['neighbors'][nbr_router_id]['last_non_hello_received'] = non_hello
                continue

            # Dead timer due in 00:00:33
            # Dead timer due in 00:00:33
            p20 = re.compile(r'^Dead +timer +due +in +(?P<dead_timer>[\w\.\:]+)$')
            m = p20.match(line)
            if m:
                sub_dict['neighbors'][nbr_router_id]['dead_timer'] = m.groupdict()['dead_timer']
                continue


        return ret_dict


# ====================================================
# Schema for 'show ip ospf virtual-links [vrf <WORD>]'
# ====================================================
class ShowIpOspfVirtualLinksSchema(MetaParser):

    ''' Schema for "show ip ospf virtual-links [vrf <WORD>]" '''

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'instance': {
                            Any(): {
                                'area': {
                                    Any(): {
                                      'virtual_links': {
                                          Any(): {
                                              'transit_area_id': str,
                                              'backbone_area_id': str,
                                              'router_id': str,
                                              'link': str,
                                              'link_state': str,
                                              Optional('unnumbered_interface'): str,
                                              Optional('ip_address'): str,
                                              'interface': str,
                                              'remote_addr': str,
                                              'hello_interval': int,
                                              'dead_interval': int,
                                              'retransmit_interval': int,
                                              'wait_interval': int,
                                              'transmit_delay': int,
                                              'index': int,
                                              Optional('authentication'): {
                                                  Optional('auth_trailer_key_chain'): {
                                                      'key_chain': str,
                                                      Optional('status'): str,
                                                  },
                                                  Optional('auth_trailer_key'): {
                                                      'crypto_algorithm': str,
                                                  },
                                                  Optional('key_id'): str,
                                              },
                                              'cost': int,
                                              'state': str,
                                              'network_type': str,
                                              'hello_timer': str,
                                              Optional('wait_timer'): int,
                                              'statistics': {
                                                  'link_scope_lsa_count': int,
                                                  'link_scope_lsa_cksum_sum': int,
                                              },
                                              'neighbors': {
                                                  Any(): {
                                                      'neighbor_router_id': str,
                                                      'address': str,
                                                      'state': str,
                                                      'dead_timer': str,
                                                      'hello_option': str,
                                                      'dbd_option': str,
                                                      'last_change': str,
                                                      'last_non_hello_received': str,
                                                      'statistics': {
                                                          'nbr_event_count': int,
                                                          Optional('nbr_retrans_qlen'): str,
                                                      }
                                                  }
                                              }
                                           }
                                        },
                                    },
                                }
                            },
                        }
                    },
                }
            }
        }
    }


# ====================================================
# Parser for 'show ip ospf virtual-links [vrf <WORD>]'
# ====================================================
class ShowIpOspfVirtualLinks(ShowIpOspfVirtualLinksSchema, ShowIpOspfLinksSuperParser):

    ''' Parser for "show ip ospf virtual-links [vrf <WORD>]" '''

    def cli(self, vrf=''):
        # excute command to get output
        cmd = 'show ip ospf virtual-links' if not vrf else \
              'show ip ospf virtual-links vrf {vrf}'.format(vrf=vrf)

        return super().cli(cmd)


# =================================================
# Schema for 'show ip ospf sham-links [vrf <WORD>]'
# =================================================
class ShowIpOspfShamLinksSchema(MetaParser):

    ''' Schema for "show ip ospf sham-links [vrf <WORD>]" '''

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'instance': {
                            Any(): {
                                'area': {
                                    Any(): {
                                      'sham_links': {
                                          Any(): {
                                              'transit_area_id': str,
                                              'backbone_area_id': str,
                                              'local_id': str,
                                              'remote_id': str,
                                              'link': str,
                                              'link_state': str,
                                              Optional('unnumbered_interface'): str,
                                              Optional('ip_address'): str,
                                              'hello_interval': int,
                                              'dead_interval': int,
                                              'retransmit_interval': int,
                                              'wait_interval': int,
                                              'transmit_delay': int,
                                              'index': int,
                                              'destination': str,
                                              Optional('authentication'): {
                                                  Optional('auth_trailer_key_chain'): {
                                                      'key_chain': str,
                                                      Optional('status'): str,
                                                  },
                                                  Optional('auth_trailer_key'): {
                                                      'crypto_algorithm': str,
                                                  },
                                                  Optional('key_id'): str,
                                              },
                                              'cost': int,
                                              'state': str,
                                              'network_type': str,
                                              'hello_timer': str,
                                              Optional('wait_timer'): int,
                                              'statistics': {
                                                  'link_scope_lsa_count': int,
                                                  'link_scope_lsa_cksum_sum': int,
                                              },
                                              Optional('neighbors'): {
                                                  Any(): {
                                                      'neighbor_router_id': str,
                                                      'address': str,
                                                      'instance': str,
                                                      'area': str,
                                                      'backbone_area_id': str,
                                                      'local': str,
                                                      'remote': str,
                                                      'state': str,
                                                      'dead_timer': str,
                                                      'hello_option': str,
                                                      'dbd_option': str,
                                                      'last_change': str,
                                                      'last_non_hello_received': str,
                                                      'statistics': {
                                                          'nbr_event_count': int,
                                                          Optional('nbr_retrans_qlen'): str,
                                                      }
                                                  }
                                              }
                                           }
                                        },
                                    },
                                }
                            },
                        }
                    },
                }
            }
        }
    }


# =================================================
# Parser for 'show ip ospf sham-links [vrf <WORD>]'
# =================================================
class ShowIpOspfShamLinks(ShowIpOspfShamLinksSchema, ShowIpOspfLinksSuperParser):

    ''' Parser for "show ip ospf sham-links [vrf <WORD>]" '''

    def cli(self, vrf=''):
        # excute command to get output
        cmd = 'show ip ospf sham-links' if not vrf else \
              'show ip ospf sham-links vrf {vrf}'.format(vrf=vrf)

        return super().cli(cmd)


# ================================================
# Schema for 'show ip ospf interface [vrf <WORD>]'
# ================================================
class ShowIpOspfInterfaceSchema(MetaParser):

    ''' Schema for "show ip ospf interface [vrf <WORD>]" '''