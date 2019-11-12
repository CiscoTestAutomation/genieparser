''' show_ospf.py

NXOS parsers for the following show commands:
    * show ip ospf
    * show ip ospf vrf <WORD>
    * show ip ospf mpls ldp interface 
    * show ip ospf mpls ldp interface vrf <WORD>
    * show ip ospf virtual-links
    * show ip ospf virtual-links vrf <WORD>
    * show ip ospf sham-links
    * show ip ospf sham-links vrf <WORD>
    * show ip ospf interface
    * show ip ospf interface vrf <WORD>
    * show ip ospf neighbors detail
    * show ip ospf neighbors detail vrf <WORD>
    * show ip ospf database external detail
    * show ip ospf database external detail vrf <WORD>
    * show ip ospf database network detail
    * show ip ospf database network detail vrf <WORD>
    * show ip ospf database summary detail
    * show ip ospf database summary detail vrf <WORD>
    * show ip ospf database router detail
    * show ip ospf database router detail vrf <WORD>
'''

# Python
import re
from netaddr import IPNetwork

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional
from genie.libs.parser.utils.common import Common


# ======================================
# Schema for 'show ip ospf [vrf <vrf>]'
# ======================================
class ShowIpOspfSchema(MetaParser):
    """Schema for:
        show ip ospf
        show ip ospf vrf <vrf>"""

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'instance': {
                            Any(): {
                                'router_id': str,
                                'instance': int,
                                Optional('name_lookup'): bool,
                                Optional('nsr'): {
                                    'enable': bool
                                },
                                Optional('graceful_restart'):{
                                    Any(): {
                                        'enable': bool,
                                        'type': str,
                                        'restart_interval': int,
                                        'state': str,
                                        'exist_status': str
                                    },
                                },
                                Optional('single_tos_routes_enable'): bool,
                                Optional('opaque_lsa_enable'): bool,
                                Optional('this_router_is'): str,
                                Optional('preference'): {
                                    'single_value': {
                                        'all': int
                                    },
                                },
                                Optional('bfd'): {
                                    'enable': bool
                                },
                                Optional('auto_cost'): {
                                    'enable': bool,
                                    'reference_bandwidth': int,
                                    'bandwidth_unit': str
                                },
                                Optional('spf_control'): {
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
                                            Optional('numbers'): {
                                                Optional('external_lsas'): {
                                                    Optional('total'): int,
                                                    Optional('checksum'): str
                                                },
                                                Optional('opaque_as_lsas'): {
                                                    Optional('total'): int,
                                                    Optional('checksum'): str
                                                },
                                            },
                                        },
                                    },
                                },
                                Optional('numbers'): {
                                    'active_areas': {
                                        'total': int,
                                        'nssa': int,
                                        'normal': int,
                                        'stub': int
                                    },
                                    'areas': {
                                        'total': int,
                                        'nssa': int,
                                        'normal': int,
                                        'stub': int,
                                    },
                                },
                                Optional('database_control'): {
                                    'max_lsa': int
                                },
                                Optional('stub_router'): {
                                    'always': {
                                        'always': bool,
                                        Optional('include_stub'): bool,
                                        Optional('summary_lsa'): bool,
                                        Optional('external_lsa'): bool
                                    },
                                    Optional('on_startup'): {
                                        'on_startup': int,
                                        Optional('include_stub'): bool,
                                        Optional('summary_lsa'): bool,
                                        Optional('external_lsa'): bool
                                    },
                                },
                                Optional('enable'): bool,
                                Optional('discard_route_external'): bool,
                                Optional('discard_route_internal'): bool,
                                Optional('areas'): {
                                    Any(): {
                                        'area_type': str,
                                        'area_id': str,
                                        Optional('generate_nssa_default_route'): bool,
                                        Optional('summary'): bool,
                                        Optional('perform_translation'): str,
                                        Optional('existed'): str,
                                        Optional('default_cost'): int,
                                        Optional('numbers'): {
                                            'interfaces': int,
                                            'active_interfaces': int,
                                            'passive_interfaces': int,
                                            'loopback_interfaces': int
                                        },
                                        Optional('ranges'): {
                                            Any(): {
                                                'prefix': str,
                                                'advertise': bool,
                                                'cost': int,
                                                'net': int
                                            },
                                        },
                                        Optional('authentication'): str,
                                        Optional('statistics'): {
                                            'spf_runs_count': int,                                            
                                            'spf_last_run_time': float,
                                            'area_scope_lsa_count': int,
                                            'area_scope_lsa_cksum_sum': str,
                                            Optional('as_nssa_translator_event_count'): int
                                        }
                                    },
                                },
                                Optional('redistribution'): {
                                    Optional('bgp'): {
                                        'bgp_id': int,  # 'redist_bgp_id',
                                    },
                                    Optional('static'): {
                                        'enabled': bool,  # 'redist_static'
                                    }
                                },
                            },
                        },
                    },
                },
            },
        }
    }


# ======================================
# Parser for 'show ip ospf [vrf <WORD>]'
# ======================================
class ShowIpOspf(ShowIpOspfSchema):
    """Parser for:
        show ip ospf
        show ip ospf vrf <vrf>"""

    cli_command = ['show ip ospf vrf {vrf}', 'show ip ospf']
    exclude = ['existed']

    def cli(self, vrf='', output=None):
        if vrf:
            cmd = self.cli_command[0].format(vrf=vrf)
        else:
            cmd = self.cli_command[1]

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output
        
        # Init vars
        ret_dict = {}
        sub_dict = {}
        redist = False

        p1 = re.compile(r'^Routing +Process +(?P<instance>\d+) +'
                        r'with +ID +(?P<router_id>[\d\.]+) +'
                        r'VRF +(?P<vrf>\S+)$')
        p2 = re.compile(r'^Routing +Process +Instance +Number'
                        r' +(?P<instance>\d+)$')
        p3 = re.compile(r'^Stateful +High +Availability +(?P<enable>\w+)$')
        p4 = re.compile(r'^Graceful\-restart +is +(?P<gr_enable>\w+)$')
        p5 = re.compile(r'^Grace +period: +(?P<interval>\w+) +'
                        r'state: +(?P<state>\w+)$')
        p6 = re.compile(r'^Last +graceful +restart +exit +status: '
                        r'+(?P<status>\w+).*?$')
        p7 = re.compile(r'^Supports +only +single +TOS\(TOS0\) +routes$')
        p8 = re.compile(r'^Supports +opaque +LSA$')
        p9 = re.compile(r'^Administrative +distance +(?P<pref_all>\d+)$')
        p10 = re.compile(r'^BFD +is +enabled$')
        p11 = re.compile(r'^Reference +Bandwidth +is +(?P<bd>\d+)'
                         r' +(?P<unit>\w+)$')
        p12 = re.compile(r'^SPF +throttling +delay +time +of'
                         r' +(?P<time>[\d\.]+) +msecs,$')
        p13 = re.compile(r'^SPF +throttling +hold +time +of'
                         r' +(?P<time>[\d\.]+) +msecs,$')
        p14 = re.compile(r'^SPF +throttling +maximum +wait +time +of'
                         r' +(?P<time>[\d\.]+) +msecs$')
        p15 = re.compile(r'^LSA +throttling +start +time +of'
                         r' +(?P<time>[\d\.]+) +msecs,$')
        p16 = re.compile(r'^LSA +throttling +hold +interval +of'
                         r' +(?P<time>[\d\.]+) +msecs,$')
        p17 = re.compile(r'^LSA +throttling +maximum +wait +time +of'
                         r' +(?P<time>[\d\.]+) +msecs$')
        p18 = re.compile(r'^Minimum +LSA +arrival +(?P<time>[\d\.]+) +msec$')
        p19 = re.compile(r'^Maximum +number +of +non +self\-generated +'
                         r'LSA +allowed +(?P<max>\d+)$')
        p19_1 = re.compile(r'^Originating +router +LSA +with +maximum +metric$')
        p20 = re.compile(r'^LSA +group +pacing +timer +(?P<time>\d+) +secs$')
        p21 = re.compile(r'^Maximum paths to destination +(?P<path>\d+)$')
        p22 = re.compile(r'^Number +of +external +LSAs +(?P<total>\d+), +'
                         r'checksum +sum +(?P<checksum>\w+)$')
        p23 = re.compile(r'^Number +of +opaque +AS +LSAs +(?P<total>\d+),'
                         r' +checksum +sum +(?P<checksum>\w+)$')
        p24 = re.compile(r'^Number +of +areas +is +(?P<total>\d+), +'
                         r'(?P<normal>\d+) +normal, +'
                         r'(?P<stub>\d+) +stub, +'
                         r'(?P<nssa>\d+) +nssa$')
        p25 = re.compile(r'^Number +of +active +areas +is +(?P<total>\d+),'
                         r' +(?P<normal>\d+) +normal, +'
                         r'(?P<stub>\d+) +stub, +'
                         r'(?P<nssa>\d+) +nssa$')
        p26 = re.compile(r'^Install +discard +route +for +'
                         r'summarized +(?P<type>\w+) +routes.$')
        p27 = re.compile(r'^Area +(?P<type>\w+)?\((?P<area>[\w\.\:]+)\)'
                         r'( *\((?P<status>\w+)\))?$')
        p34 = re.compile(r'^This +area +is +a +(?P<type>\w+) +area$')
        p35 = re.compile(r'^Generates +stub +default +route +with +'
                         r'cost +(?P<cost>\d+)$')
        p28 = re.compile(r'^Area +has +existed +for +(?P<time>[\w\.\:]+)$')
        p29 = re.compile(r'^Interfaces +in +this +area: +(?P<num1>\d+) +'
                         r'Active +interfaces: +(?P<num2>\d+)$')
        p30 = re.compile(r'^Passive +interfaces: +(?P<num1>\d+) +'
                         r'Loopback +interfaces: +(?P<num2>\d+)$')
        p31 = re.compile(r'^SPF +calculation +has +run +(?P<num1>\d+) +times$')
        p32 = re.compile(r'^Last +SPF +ran +for +(?P<num1>[\d\.]+)s$')
        p36 = re.compile(r'^(?P<prefix>[\d\/\.]+) +'
                         r'(Active|Passive) +\(Num +nets: +(?P<net>\d+)\) +'
                         r'(?P<advertise>\w+) +'
                         r'Cost +configured +(?P<cost>\d+)$')
        p33 = re.compile(r'^Number +of +LSAs: +(?P<num1>\d+), +'
                         r'checksum +sum +(?P<num2>\w+)$')

        p37 = re.compile(r'^Redistributing +External +Routes +from$')

        p38 = re.compile(r'^(?P<redist>[\w]+)(?:-(?P<redist_id>\d+))?$')

        p39 = re.compile(r'^Name +Lookup +is +(?P<name_lookup>enabled|disabled)$')

        p40 = re.compile(r'^Summarization +is +(?P<summary>disabled)$')

        p41 = re.compile(r'^Perform +(?P<perform_translation>\S+) +LSA +translation$')

        p42 = re.compile(r'(?P<authentication>No|Message\-digest|Simple)'
                         r'(?: +password)?(?: +authentication(?: +available)?)?$')
        
        p43 = re.compile(r'^Generates +NSSA +(?P<generate_nssa>[\S\s]+)$')

        p44 = re.compile(r'^This +router +is +(?P<this_router_is>[\w\s]+)(?:\.)?$')

        for line in out.splitlines():
            line = line.strip()

            # Routing Process 1 with ID 10.16.2.2 VRF default
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
                if 'instance' not in ret_dict['vrf'][vrf]['address_family']\
                        ['ipv4']:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']\
                        ['instance'] = {}
                if instance not in ret_dict['vrf'][vrf]['address_family']\
                        ['ipv4']['instance']:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance']\
                        [instance] = {}
                sub_dict = ret_dict['vrf'][vrf]['address_family']['ipv4']\
                    ['instance'][instance]

                # router_id
                sub_dict['router_id'] = m.groupdict()['router_id']
                # instance
                sub_dict['instance'] = int(m.groupdict()['instance'])

                # initial 
                gr_enable = None
                continue

            # Routing Process Instance Number 1
            m = p2.match(line)
            if m:
                sub_dict['instance'] = int(m.groupdict()['instance'])
                continue

            # Stateful High Availability enabled
            m = p3.match(line)
            if m:
                if 'nsr' not in sub_dict:
                    sub_dict['nsr'] = {}
                sub_dict['nsr']['enable'] = True \
                    if 'enable' in m.groupdict()['enable'].lower() else False
                continue

            # Graceful-restart is configured
            m = p4.match(line)
            if m:
                if 'graceful_restart' not in sub_dict:
                    sub_dict['graceful_restart'] = {}
                gr_enable = True \
                    if 'configured' in m.groupdict()['gr_enable'].lower() else False
                continue

            # Grace period: 60 state: Inactive 
            m = p5.match(line)
            if m:
                restart_interval = int(m.groupdict()['interval'])
                state = str(m.groupdict()['state'])
                if 'graceful_restart' not in sub_dict:
                    sub_dict['graceful_restart'] = {}
                if 'ietf' not in sub_dict['graceful_restart']:
                    sub_dict['graceful_restart']['ietf'] = {}
                sub_dict['graceful_restart']['ietf']['type'] = 'ietf'
                sub_dict['graceful_restart']['ietf']['restart_interval'] = \
                    restart_interval
                sub_dict['graceful_restart']['ietf']['state'] = state
                if gr_enable:
                    sub_dict['graceful_restart']['ietf']['enable'] = gr_enable
                continue

            # Last graceful restart exit status: None
            # Last graceful restart exit status: Failed (grace period timeout)
            m = p6.match(line)
            if m:
                sub_dict['graceful_restart']['ietf']['exist_status'] = \
                    m.groupdict()['status'].lower()
                continue

            # Supports only single TOS(TOS0) routes
            m = p7.match(line)
            if m:
                sub_dict['single_tos_routes_enable'] = True
                continue

            # Supports opaque LSA
            m = p8.match(line)
            if m:
                sub_dict['opaque_lsa_enable'] = True
                continue

            # Administrative distance 110
            m = p9.match(line)
            if m:
                if 'preference' not in sub_dict:
                    sub_dict['preference'] = {}
                if 'single_value' not in sub_dict['preference']:
                    sub_dict['preference']['single_value'] = {}
                sub_dict['preference']['single_value']['all'] = \
                    int(m.groupdict()['pref_all'])
                continue

            # BFD is enabled
            m = p10.match(line)
            if m:
                if 'bfd' not in sub_dict:
                    sub_dict['bfd'] = {}
                sub_dict['bfd']['enable'] = True
                continue

            # Reference Bandwidth is 40000 Mbps
            m = p11.match(line)
            if m:
                bd = int(m.groupdict()['bd'])
                if 'auto_cost' not in sub_dict:
                    sub_dict['auto_cost'] = {}
                sub_dict['auto_cost']['reference_bandwidth'] = \
                    int(m.groupdict()['bd'])
                sub_dict['auto_cost']['bandwidth_unit'] = \
                    m.groupdict()['unit'].lower()
                if bd == 40000:
                    # This is the default - set to False
                    sub_dict['auto_cost']['enable'] = False
                else:
                    sub_dict['auto_cost']['enable'] = True
                    continue

            # SPF throttling delay time of 200.000 msecs,
            m = p12.match(line)
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

            # SPF throttling hold time of 1000.000 msecs, 
            m = p13.match(line)
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

            # SPF throttling maximum wait time of 5000.000 msecs
            m = p14.match(line)
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

            # LSA throttling start time of 0.000 msecs,
            m = p15.match(line)
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

            # LSA throttling hold interval of 5000.000 msecs, 
            m = p16.match(line)
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

            # LSA throttling maximum wait time of 5000.000 msecs
            m = p17.match(line)
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

            # Minimum LSA arrival 1000.000 msec
            m = p18.match(line)
            if m:
                minimum = int(float(m.groupdict()['time']))
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'lsa' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['lsa'] = {}
                sub_dict['spf_control']['throttle']['lsa']['minimum'] = minimum
                continue

            # Maximum number of non self-generated LSA allowed 123
            m = p19.match(line)
            if m:
                if 'database_control' not in sub_dict:
                    sub_dict['database_control'] = {}
                sub_dict['database_control']['max_lsa'] = \
                    int(m.groupdict()['max'])
                continue

            # Originating router LSA with maximum metric
            m = p19_1.match(line)
            if m:
                if 'stub_router' not in sub_dict:
                    sub_dict['stub_router'] = {}
                if 'always' not in sub_dict['stub_router']:
                    sub_dict['stub_router']['always'] = {}
                sub_dict['stub_router']['always']['always'] = True
                continue

            # LSA group pacing timer 10 secs
            m = p20.match(line)
            if m:
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'lsa' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['lsa'] = {}
                sub_dict['spf_control']['throttle']['lsa']['group_pacing'] = \
                    int(m.groupdict()['time'])
                continue

            # Maximum paths to destination 8
            m = p21.match(line)
            if m:
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                sub_dict['spf_control']['paths'] = int(m.groupdict()['path'])
                continue

            # Number of external LSAs 1, checksum sum 0x7d61
            m = p22.match(line)
            if m:
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'lsa' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['lsa'] = {}
                if 'numbers' not in sub_dict['spf_control']['throttle']['lsa']:
                    sub_dict['spf_control']['throttle']['lsa']['numbers'] = {}
                if 'external_lsas' not in sub_dict['spf_control']['throttle']\
                        ['lsa']['numbers']:
                    sub_dict['spf_control']['throttle']['lsa']['numbers']\
                        ['external_lsas'] = {}
                sub_dict['spf_control']['throttle']['lsa']['numbers']\
                    ['external_lsas']['total'] = int(m.groupdict()['total'])
                sub_dict['spf_control']['throttle']['lsa']['numbers']\
                    ['external_lsas']['checksum'] = str(m.groupdict()['checksum'])
                continue

            # Number of opaque AS LSAs 0, checksum sum 0
            m = p23.match(line)
            if m:
                if 'spf_control' not in sub_dict:
                    sub_dict['spf_control'] = {}
                if 'throttle' not in sub_dict['spf_control']:
                    sub_dict['spf_control']['throttle'] = {}
                if 'lsa' not in sub_dict['spf_control']['throttle']:
                    sub_dict['spf_control']['throttle']['lsa'] = {}
                if 'numbers' not in sub_dict['spf_control']['throttle']['lsa']:
                    sub_dict['spf_control']['throttle']['lsa']['numbers'] = {}
                if 'opaque_as_lsas' not in sub_dict['spf_control']['throttle']\
                        ['lsa']['numbers']:
                    sub_dict['spf_control']['throttle']['lsa']['numbers']\
                        ['opaque_as_lsas'] = {}
                sub_dict['spf_control']['throttle']['lsa']['numbers']\
                    ['opaque_as_lsas']['total'] = int(m.groupdict()['total'])
                sub_dict['spf_control']['throttle']['lsa']['numbers']\
                    ['opaque_as_lsas']['checksum'] = str(m.groupdict()['checksum'])
                continue

            # Number of areas is 1, 1 normal, 0 stub, 0 nssa
            m = p24.match(line)
            if m:
                if 'numbers' not in sub_dict:
                    sub_dict['numbers'] = {}
                if 'areas' not in sub_dict['numbers']:
                    sub_dict['numbers']['areas'] = {}
                sub_dict['numbers']['areas']['total'] = \
                    int(m.groupdict()['total'])
                sub_dict['numbers']['areas']['normal'] = \
                    int(m.groupdict()['normal'])
                sub_dict['numbers']['areas']['stub'] = \
                    int(m.groupdict()['stub'])
                sub_dict['numbers']['areas']['nssa'] = \
                    int(m.groupdict()['nssa'])
                continue

            # Number of active areas is 1, 1 normal, 0 stub, 0 nssa
            m = p25.match(line)
            if m:
                if 'numbers' not in sub_dict:
                    sub_dict['numbers'] = {}
                if 'active_areas' not in sub_dict['numbers']:
                    sub_dict['numbers']['active_areas'] = {}
                sub_dict['numbers']['active_areas']['total'] = \
                    int(m.groupdict()['total'])
                sub_dict['numbers']['active_areas']['normal'] = \
                    int(m.groupdict()['normal'])
                sub_dict['numbers']['active_areas']['stub'] = \
                    int(m.groupdict()['stub'])
                sub_dict['numbers']['active_areas']['nssa'] = \
                    int(m.groupdict()['nssa'])
                continue

            # Install discard route for summarized external routes.
            # Install discard route for summarized internal routes.
            m = p26.match(line)
            if m:
                sub_dict['discard_route_external'] = True
                sub_dict['discard_route_internal'] = True
                continue

            # Area BACKBONE(0.0.0.0) 
            # Area (0.0.0.1)
            # Area BACKBONE(0.0.0.0) (Inactive)
            m = p27.match(line)
            if m:
                area = m.groupdict()['area']
                if 'areas' not in sub_dict:
                    sub_dict['areas'] = {}
                if area not in sub_dict['areas']:
                    sub_dict['areas'][area] = {}
                sub_dict['areas'][area]['area_id'] = area
                sub_dict['areas'][area]['area_type'] = 'normal'
                if m.groupdict()['status'] and  \
                  'inactive' in m.groupdict()['status'].lower():
                    sub_dict['enable'] = False
                else:
                    sub_dict['enable'] = True
                continue

            # This area is a STUB area
            # This area is a NSSA area
            m = p34.match(line)
            if m:
                sub_dict['areas'][area]['area_type'] = \
                    m.groupdict()['type'].lower()
                continue

            # Generates stub default route with cost 1
            m = p35.match(line)
            if m:
                sub_dict['areas'][area]['default_cost'] = \
                    int(m.groupdict()['cost'])
                continue

            #  Area has existed for 08:30:42
            m = p28.match(line)
            if m:
                sub_dict['areas'][area]['existed'] = m.groupdict()['time']
                continue

            # Interfaces in this area: 4 Active interfaces: 4
            m = p29.match(line)
            if m:
                if 'numbers' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['numbers'] = {}
                sub_dict['areas'][area]['numbers']['interfaces'] = \
                    int(m.groupdict()['num1'])
                sub_dict['areas'][area]['numbers']['active_interfaces'] = \
                    int(m.groupdict()['num2'])
                continue

            # Passive interfaces: 0  Loopback interfaces: 1
            m = p30.match(line)
            if m:
                if 'numbers' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['numbers'] = {}
                sub_dict['areas'][area]['numbers']['passive_interfaces'] = \
                    int(m.groupdict()['num1'])
                sub_dict['areas'][area]['numbers']['loopback_interfaces'] = \
                    int(m.groupdict()['num2'])
                continue

            # SPF calculation has run 8 times
            m = p31.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['spf_runs_count'] = \
                    int(m.groupdict()['num1'])
                continue

            # Last SPF ran for 0.001386s
            m = p32.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['spf_last_run_time'] = \
                    float(m.groupdict()['num1'])
                continue

            #     Area ranges are
            # 10.4.0.0/16 Active (Num nets: 1) DoNotAdvertise Cost configured 31
            # 10.4.1.0/24 Passive (Num nets: 0) Advertise Cost configured 33
            m = p36.match(line)
            if m:
                prefix = str(m.groupdict()['prefix'])
                if 'ranges' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['ranges'] = {}
                if prefix not in sub_dict['areas'][area]['ranges']:
                    sub_dict['areas'][area]['ranges'][prefix] = {}
                sub_dict['areas'][area]['ranges'][prefix]['prefix'] = \
                    m.groupdict()['prefix']
                sub_dict['areas'][area]['ranges'][prefix]['cost'] = \
                    int(m.groupdict()['cost'])
                sub_dict['areas'][area]['ranges'][prefix]['net'] = \
                    int(m.groupdict()['net'])
                sub_dict['areas'][area]['ranges'][prefix]['advertise'] = False if\
                    'donot' in m.groupdict()['advertise'].lower() else True
                continue


            # Number of LSAs: 19, checksum sum 0x7a137
            m = p33.match(line)
            if m:
                if 'statistics' not in sub_dict['areas'][area]:
                    sub_dict['areas'][area]['statistics'] = {}
                sub_dict['areas'][area]['statistics']['area_scope_lsa_count'] = \
                    int(m.groupdict()['num1'])
                sub_dict['areas'][area]['statistics']\
                    ['area_scope_lsa_cksum_sum'] = m.groupdict()['num1']
                continue
            
            # Redistributing External Routes from
            m37 = p37.match(line)
            if m37:
                redist = True
                redist_dict = sub_dict.setdefault('redistribution', {})

                continue   
            
            # static
            # bgp-100
            m38 = p38.match(line)
            if m38:
                if redist:
                    group = m38.groupdict()
                    if group['redist'] == 'bgp':
                        bgp_dict = redist_dict.setdefault('bgp', {})
                        bgp_dict.update({'bgp_id': int(group['redist_id'])})
                    elif group['redist'] == 'static':
                        static_dict = redist_dict.setdefault('static', {})
                        static_dict.update({'enabled': True})
                continue

            # Name Lookup is enabled
            m39 = p39.match(line)
            if m39:
                group = m39.groupdict()['name_lookup']
                sub_dict['name_lookup'] = True if group == 'enabled' else False

                continue
            
            # Summarization is disabled
            m40 = p40.match(line)
            if m40:
                summary = m40.groupdict()['summary']
                status = sub_dict['areas'][area]

                status['summary'] = True if summary == 'enabled' else False

                continue

            # Perform type-7/type-5 LSA translation
            m41 = p41.match(line)
            if m41:
                translation = m41.groupdict()['perform_translation']
                sub_dict['areas'][area]['perform_translation'] = translation

                continue
            
            # Message-digest authentication
            # Simple password authentication
            # No authentication available
            m42 = p42.match(line)
            if m42:
                message = m42.groupdict()['authentication']
                auth_dict = sub_dict['areas'][area]
                if message == 'No':
                    auth_dict['authentication'] = 'none'
                else:
                    auth_dict['authentication'] = message

                continue
            # Generates NSSA default route    
            m43 = p43.match(line)
            if m43:
                route = m43.groupdict()['generate_nssa']
                route_dict = sub_dict['areas'][area]
                route_dict['generate_nssa_default_route'] = True

                continue

            # This router is an area border and autonomous system boundary.
            # This router is an area border
            # This router is an autonomous system boundary
            m44 = p44.match(line)
            if m44:
                boundary = m44.groupdict()['this_router_is']
                sub_dict['this_router_is'] = boundary

                continue
            
        return ret_dict


# =========================================================
# Schema for 'show ip ospf mpls ldp interface [vrf <WORD>]'
# =========================================================
class ShowIpOspfMplsLdpInterfaceSchema(MetaParser):
    """Schema for:
        show ip ospf mpls ldp interface
        show ip ospf mpls ldp interface vrf <vrf>"""

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {'areas' :
                                    {Any(): 
                                        {'mpls': 
                                            {'ldp': 
                                                {'autoconfig': bool,
                                                'autoconfig_area_id': str,
                                                'igp_sync': bool,
                                                 Optional('required'): bool,
                                                 Optional('achieved'): bool,
                                             },
                                            },
                                        Optional('interfaces'): 
                                            {Any(): 
                                                {'area': str,
                                                'name': str,
                                                'state': str,
                                                'interface_type': str,
                                                'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': bool,
                                                        'autoconfig_area_id': str,
                                                        'igp_sync': bool,
                                                         Optional('required'): bool,
                                                         Optional('achieved'): bool,
                                                         },
                                                    },
                                                },
                                            },
                                        Optional('virtual_links'): 
                                            {Any(): 
                                                {'area': str,
                                                'name': str,
                                                'state': str,
                                                'interface_type': str,
                                                'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': bool,
                                                        'autoconfig_area_id': str,
                                                        'igp_sync': bool,
                                                         Optional('required'): bool,
                                                         Optional('achieved'): bool,
                                                         },
                                                    },
                                                },
                                            },
                                        Optional('sham_links'): 
                                            {Any(): 
                                                {'area': str,
                                                'name': str,
                                                'state': str,
                                                'interface_type': str,
                                                'mpls': 
                                                    {'ldp': 
                                                        {'autoconfig': bool,
                                                        'autoconfig_area_id': str,
                                                        'igp_sync': bool,
                                                         Optional('required'): bool,
                                                         Optional('achieved'): bool,
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


# =========================================================
# Parser for 'show ip ospf mpls ldp interface [vrf <WORD>]'
# =========================================================
class ShowIpOspfMplsLdpInterface(ShowIpOspfMplsLdpInterfaceSchema):
    """Parser for:
        show ip ospf mpls ldp interface
        show ip ospf mpls ldp interface <interface>
        show ip ospf mpls ldp interface vrf <vrf>"""

    cli_command = ['show ip ospf mpls ldp interface vrf {vrf}',
                   'show ip ospf mpls ldp interface',
                   'show ip ospf mpls ldp interface {interface}']
    exclude = [
        'state']

    def cli(self, vrf='', interface='', output=None):
        if vrf:
            cmd = self.cli_command[0].format(vrf=vrf)
        else:
            if interface:
                cmd = self.cli_command[2].format(interface=interface)
            else:
                cmd = self.cli_command[1]

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}
        sub_dict = {}

        p1 = re.compile(r'^(?P<interface>[\w\.\-\/]+) +\- +'
                            'Process +ID +(?P<instance>\S+) +'
                            'VRF +(?P<vrf>\S+), +'
                            'area +(?P<area>[\w\.]+)$')
        p2 = re.compile(r'^LDP +Autoconfig +not +enabled$')
        p2_1 = re.compile(r'^LDP +Autoconfig +is +enabled$')
        p3_1 = re.compile(r'^LDP +Sync +is +enabled,'
                            ' +(?P<req>(is|not)) +required'
                            '(?: +and +(?P<ach>(is|not)) +achieved)?$')
        p3_2 = re.compile(r'^LDP +Sync +not +enabled, +not +required$')
        p4 = re.compile(r'^State +(?P<state>\w+), +'
                            'Network +type +(?P<type>\w+)$')
        for line in out.splitlines():
            line = line.strip()

            # Ethernet2/2 - Process ID 1 VRF default, area 0.0.0.0
            # Ethernet8/11/3 - Process ID UNDERLAY VRF default, area 0.0.0.0
            # SL1-0.0.0.0-10.151.22.22-10.229.11.11 - Process ID 1 VRF VRF1, area 0.0.0.1
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                instance = m.groupdict()['instance']
                area = m.groupdict()['area']
                interface = m.groupdict()['interface']

                # Determine if 'interface' or 'sham_link' or 'virtual_link'
                if re.search('SL', interface):
                    pattern = '(?P<link>\w+)-(?P<area_id>[\w\.\:]+)-(?P<local>[\w\.\:]+)-(?P<remote>[\w\.\:]+)'
                    n = re.match(pattern, interface)
                    link = str(n.groupdict()['link'])
                    area_id = str(n.groupdict()['area_id'])
                    local = str(n.groupdict()['local'])
                    remote = str(n.groupdict()['remote'])
                    # Set values for dict
                    intf_type = 'sham_links'
                    intf_name = local + ' ' + remote
                elif re.search('VL', interface):
                    pattern = '(?P<link>\w+)-(?P<area_id>[\w\.\:]+)-(?P<router_id>[\w\.\:]+)'
                    n = re.match(pattern, interface)
                    link = str(n.groupdict()['link'])
                    area_id = str(n.groupdict()['area_id'])
                    router_id = str(n.groupdict()['router_id'])
                    # Set values for dict
                    intf_type = 'virtual_links'
                    intf_name = area_id + ' ' + router_id
                else:
                    # Set values for dict
                    intf_type = 'interfaces'
                    intf_name = interface

                # Create dict structure
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if 'ipv4' not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family']['ipv4'] = {}
                if 'instance' not in ret_dict['vrf'][vrf]['address_family']\
                        ['ipv4']:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']\
                        ['instance'] = {}
                if instance not in ret_dict['vrf'][vrf]['address_family']\
                        ['ipv4']['instance']:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance']\
                        [instance] = {}
                if 'areas' not in ret_dict['vrf'][vrf]['address_family']['ipv4']\
                        ['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family']['ipv4']\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance']\
                        [instance]['areas'][area] = {}
                area_dict = ret_dict['vrf'][vrf]['address_family']['ipv4']\
                                ['instance'][instance]['areas'][area]
                if intf_type not in ret_dict['vrf'][vrf]['address_family']\
                        ['ipv4']['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance']\
                        [instance]['areas'][area][intf_type] = {}
                if intf_name not in ret_dict['vrf'][vrf]['address_family']\
                        ['ipv4']['instance'][instance]['areas'][area][intf_type]:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance']\
                        [instance]['areas'][area][intf_type][intf_name] = {}
                sub_dict = ret_dict['vrf'][vrf]['address_family']['ipv4']\
                            ['instance'][instance]['areas'][area]\
                            [intf_type][intf_name]

                # Set keys at area level
                if 'mpls' not in area_dict:
                    area_dict['mpls'] = {}
                if 'ldp' not in area_dict['mpls']:
                    area_dict['mpls']['ldp'] = {}
                area_dict['mpls']['ldp']['autoconfig_area_id'] = area

                # Set keys at interface level
                sub_dict['area'] = area
                sub_dict['name'] = intf_name
                if 'mpls' not in sub_dict:
                    sub_dict['mpls'] = {}
                if 'ldp' not in sub_dict['mpls']:
                    sub_dict['mpls']['ldp'] = {}
                sub_dict['mpls']['ldp']['autoconfig_area_id'] = area
                continue

            # LDP Autoconfig not enabled
            m = p2.match(line)
            if m:
                # Set at area level
                area_dict['mpls']['ldp']['autoconfig_area_id'] = area
                area_dict['mpls']['ldp']['autoconfig'] = False
                # Set at interface level
                sub_dict['mpls']['ldp']['autoconfig_area_id'] = area
                sub_dict['mpls']['ldp']['autoconfig'] = False
                continue

            # LDP Autoconfig is enabled
            m = p2_1.match(line)
            if m:
                # Set at area level
                area_dict['mpls']['ldp']['autoconfig'] = True
                # Set at interface level
                sub_dict['mpls']['ldp']['autoconfig'] = True
                continue

            # LDP Sync is enabled, is required and is achieved
            # LDP Sync is enabled, is required and not achieved
            # LDP Sync is enabled, not required
            m = p3_1.match(line)
            if m:
                # Set at area level
                area_dict['mpls']['ldp']['igp_sync'] = True
                if m.groupdict()['req']:
                    area_dict['mpls']['ldp']['required'] = True \
                        if 'is' in m.groupdict()['req'] else False
                if m.groupdict()['ach']:
                    area_dict['mpls']['ldp']['achieved'] = True \
                        if 'is' in m.groupdict()['ach'] else False

                # Set at interface level
                sub_dict['mpls']['ldp']['igp_sync'] = True
                if m.groupdict()['req']:
                    sub_dict['mpls']['ldp']['required'] = True \
                        if 'is' in m.groupdict()['req'] else False
                if m.groupdict()['ach']:
                    sub_dict['mpls']['ldp']['achieved'] = True \
                        if 'is' in m.groupdict()['ach'] else False
                continue

            # LDP Sync not enabled, not required
            m = p3_2.match(line)
            if m:
                # Set at area level
                area_dict['mpls']['ldp']['igp_sync'] = False
                area_dict['mpls']['ldp']['required'] = False
                # Set at interface level
                sub_dict['mpls']['ldp']['igp_sync'] = False
                sub_dict['mpls']['ldp']['required'] = False
                continue

            # State LOOPBACK, Network type LOOPBACK
            m = p4.match(line)
            if m:
                state = str(m.groupdict()['state']).lower()
                interface_type = str(m.groupdict()['type']).lower()
                if state == 'p2p':
                    state = 'point_to_point'
                if interface_type == 'p2p':
                    interface_type =  'point_to_point'
                sub_dict['state'] = state
                sub_dict['interface_type'] = interface_type
                continue

        return ret_dict


# =============================================
# Parser for 'show ip ospf <WORD> [vrf <WORD>]'
# =============================================
class ShowIpOspfLinksParser(MetaParser):
    """Parser for:
        show ip ospf <link_type>
        show ip ospf <link_type> vrf <vrf>"""

    def cli(self, cmd, output=None):
        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output
        
        # Init vars
        ret_dict = {}
        sub_dict = {}
        p1 = re.compile(r'^Virtual +link +(?P<link>\w+) +to +router +'
                            '(?P<router_id>[\w\.\:]+) +is +(?P<state>\w+)$')
        p1_1 = re.compile(r'^(?P<link>\w+)-(?P<area>[\w\.\:]+)-'
                            '(?P<local>[\w\.\:]+)-'
                            '(?P<remote>[\w\.\:]+) +'
                            'line +protocol +is +(?P<state>\w+)$')
        p2 = re.compile(r'^Transit +area +(?P<transit_area_id>[\w\.\:]+), +'
                            'via +interface +(?P<intf>[\w\.\/\-]+), +'
                            'remote +addr +(?P<remote_addr>[\w\.\:]+)$')
        p3 = re.compile(r'^Unnumbered +interface +using +IP +address +of +'
                            '(?P<intf>[\w\.\/\-]+) +\((?P<ip>[\w\.\:]+)\)$')
        p4 = re.compile(r'^Process +ID +(?P<inst>\d+) +'
                            'VRF +(?P<vrf>\S+), +area +(?P<area>[\w\.\:]+)$')
        p5 = re.compile(r'^State +(?P<state>\w+), +Network +type'
                            ' +(?P<interface_type>\w+), +cost +(?P<cost>\d+)$')
        p6 = re.compile(r'^Index +(?P<index>\d+), +'
                            'Transmit +delay +(?P<delay>\d+) +sec$')
        p7 = re.compile(r'^(?P<nbr_count>\d+) +Neighbors, +'
                            'flooding +to +(?P<flood>\d+), '
                            'adjacent +with +(?P<adjacent>\d+)$')
        p8 = re.compile(r'^Timer +intervals: +Hello +(?P<hello>\d+), +'
                            'Dead +(?P<dead>\d+), +Wait +(?P<wait>\d+), +'
                            'Retransmit +(?P<retransmit>\d+)$')
        p9 = re.compile(r'^Hello +timer +due +in +(?P<hello_timer>[\w\.\:]+)$')
        p10 = re.compile(r'^(?P<auth_type>[\w\-]+) +authentication(, +'
                            'using +(?P<key_type>(key +id|keychain)) +'
                            '(?P<key>\w+)( *\((?P<status>\w+)\))?)?$')
        p11 = re.compile(r'^Number +of +opaque +link +LSAs: +(?P<count>\d+),'
                            ' +checksum +sum +(?P<checksum>\d+)$')
        p12 = re.compile(r'^Adjacency +Information *:?$')
        p13 = re.compile(r'^Destination +IP +address: +(?P<dest>[\w\.\:]+)$')
        p14 = re.compile(r'^Neighbor +(?P<nei>[\w\.\:]+), +'
                            'interface +address +(?P<intf_ip>[\w\.\:]+)$')
        p15 = re.compile(r'^Process +ID +(?P<inst>\d+) +VRF +(?P<vrf>\S+), +'
                            'in +area +(?P<area>[\w\.\:]+) +via +interface +'
                            '(?P<link>\w+)-(?P<backbone>[\w\.\:]+)-'
                            '(?P<local>[\w\.\:]+)$')
        p16 = re.compile(r'^-(?P<remote>[\w\.\:]+)$')
        p17 = re.compile(r'^State +is +(?P<status>\w+), +'
                            '(?P<change>\d+) +state +changes, +'
                            'last +change +(?P<last_change>[\w\.\:]+)$')
        p18 = re.compile(r'^Hello +options +(?P<hello>\w+), +'
                            'dbd +options +(?P<dbd>\w+)$')
        p19 = re.compile(r'^Last +non\-hello +packet +received +(?P<last>[\w\.\:]+)$')
        p20 = re.compile(r'^Dead +timer +due +in +(?P<dead_timer>[\w\.\:]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Virtual link VL1 to router 10.64.4.4 is up
            m = p1.match(line)
            if m:
                link = m.groupdict()['link']
                router_id = m.groupdict()['router_id']
                state = m.groupdict()['state']
                link_type = 'virtual_links'
                continue


            # SL1-0.0.0.0-10.151.22.22-10.229.11.11 line protocol is up
            m = p1_1.match(line)
            if m:
                link = m.groupdict()['link']
                backbone_area_id = m.groupdict()['area']
                local = m.groupdict()['local']
                remote = m.groupdict()['remote']
                state = m.groupdict()['state']
                link_type = 'sham_links'
                continue

            # Transit area 0.0.0.1, via interface Eth1/5, remote addr 10.19.4.4
            m = p2.match(line)
            if m:
                transit_area_id = m.groupdict()['transit_area_id']
                intf = Common.convert_intf_name(m.groupdict()['intf'])
                remote_addr = m.groupdict()['remote_addr']
                continue

            # Unnumbered interface using IP address of Ethernet1/5 (10.19.4.3)
            # Unnumbered interface using IP address of loopback1 (10.151.22.22)
            m = p3.match(line)
            if m:
                unnumbered_interface = m.groupdict()['intf']
                ip_address = m.groupdict()['ip']
                continue

            # Process ID 1 VRF default, area 0.0.0.0
            # Process ID 1 VRF VRF1, area 0.0.0.1
            m = p4.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                inst = str(m.groupdict()['inst'])
                area_id = m.groupdict()['area']

                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if 'ipv4' not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family']['ipv4'] = {}
                if 'instance' not in ret_dict['vrf'][vrf]['address_family']\
                        ['ipv4']:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']\
                        ['instance'] = {}
                if inst not in ret_dict['vrf'][vrf]['address_family']['ipv4']\
                        ['instance']:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance']\
                        [inst] = {}
                if 'areas' not in ret_dict['vrf'][vrf]['address_family']['ipv4']\
                        ['instance'][inst]:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance']\
                        [inst]['areas'] = {}

                # Set area_id based on link_type
                if link_type == 'virtual_links':
                    backbone_area_id = area_id
                    area_id = transit_area_id
                    link_key = '{0} {1}'.format(transit_area_id, router_id)
                else:
                    transit_area_id = area_id
                    link_key = '{0} {1}'.format(local, remote)

                if area_id not in ret_dict['vrf'][vrf]['address_family']\
                        ['ipv4']['instance'][inst]['areas']:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance']\
                        [inst]['areas'][area_id] = {}
                if link_type not in ret_dict['vrf'][vrf]['address_family']\
                        ['ipv4']['instance'][inst]['areas'][area_id]:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance']\
                        [inst]['areas'][area_id][link_type] = {}
                if link_key not in ret_dict['vrf'][vrf]['address_family']\
                        ['ipv4']['instance'][inst]['areas'][area_id][link_type]:
                    ret_dict['vrf'][vrf]['address_family']['ipv4']['instance']\
                        [inst]['areas'][area_id][link_type][link_key] = {}
                sub_dict = ret_dict['vrf'][vrf]['address_family']['ipv4']\
                            ['instance'][inst]['areas'][area_id]\
                            [link_type][link_key]

                # Set previously parsed keys
                try:
                    sub_dict['name'] = link
                except Exception:
                    pass
                try:
                    sub_dict['link_state'] = state
                except Exception:
                    pass
                try:
                    sub_dict['transit_area_id'] = transit_area_id
                except Exception:
                    pass
                try:
                    sub_dict['backbone_area_id'] = backbone_area_id
                except Exception:
                    pass
                try:
                    sub_dict['unnumbered_interface'] = unnumbered_interface
                except Exception:
                    pass
                try:
                    sub_dict['unnumbered_ip_address'] = ip_address
                except Exception:
                    pass
                try:
                    sub_dict['router_id'] = router_id
                except Exception:
                    pass
                try:
                    sub_dict['interface'] = intf
                except Exception:
                    pass
                try:
                    sub_dict['remote_addr'] = remote_addr
                except Exception:
                    pass
                try:
                    sub_dict['local_id'] = local
                except Exception:
                    pass
                try:
                    sub_dict['remote_id'] = remote
                except Exception:
                    pass
                continue

            # State P2P, Network type P2P, cost 40
            # State P2P, Network type P2P, cost 1
            m = p5.match(line)
            if m:
                interface_type = str(m.groupdict()['interface_type']).lower()
                state = str(m.groupdict()['state']).lower()
                sub_dict['cost'] = int(m.groupdict()['cost'])
                if interface_type == 'p2p':
                    interface_type = 'point_to_point'
                if state == 'p2p':
                    state = 'point_to_point'
                sub_dict['interface_type'] = interface_type
                sub_dict['state'] = state
                continue

            # Index 7, Transmit delay 1 sec
            # Index 6, Transmit delay 1 sec
            m = p6.match(line)
            if m:
                sub_dict['transmit_delay'] = int(m.groupdict()['delay'])
                sub_dict['index'] = int(m.groupdict()['index'])
                continue

            # 1 Neighbors, flooding to 1, adjacent with 1
            # 1 Neighbors, flooding to 1, adjacent with 1
            m = p7.match(line)
            if m:
                sub_dict['nbr_total'] = int(m.groupdict()['nbr_count'])
                sub_dict['nbr_flood'] = int(m.groupdict()['flood'])
                sub_dict['nbr_adjs'] = int(m.groupdict()['adjacent'])
                continue

            # Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
            # Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
            m = p8.match(line)
            if m:
                sub_dict['hello_interval'] = int(m.groupdict()['hello'])
                sub_dict['dead_interval'] = int(m.groupdict()['dead'])
                sub_dict['retransmit_interval'] = int(m.groupdict()['retransmit'])
                sub_dict['wait_interval'] = int(m.groupdict()['wait'])
                continue

            # Hello timer due in 00:00:05
            # Hello timer due in 00:00:02
            m = p9.match(line)
            if m:
                sub_dict['hello_timer'] = m.groupdict()['hello_timer']
                continue

            # No authentication
            # Simple authentication
            # Simple authentication, using keychain test (ready)
            # Message-digest authentication, using key id 1
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

                sub_dict['authentication']['auth_trailer_key']\
                    ['crypto_algorithm'] = crypto_algorithm

                if key_type == 'keychain':
                    if 'auth_trailer_key_chain' not in sub_dict['authentication']:
                        sub_dict['authentication']['auth_trailer_key_chain'] = {}
                    sub_dict['authentication']['auth_trailer_key_chain']\
                        ['key_chain'] = key
                    if status:
                        sub_dict['authentication']['auth_trailer_key_chain']\
                            ['status'] = status
                elif key_type:
                    sub_dict['authentication']['key_id'] = key

                continue

            # Number of opaque link LSAs: 0, checksum sum 0
            # Number of opaque link LSAs: 0, checksum sum 0
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
            m = p12.match(line)
            if m:
                continue

            #   Destination IP address: 10.229.11.11
            m = p13.match(line)
            if m:
                sub_dict['destination'] = m.groupdict()['dest']
                continue

            #   Neighbor 10.229.11.11, interface address 10.229.11.11
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

            #   Process ID 1 VRF VRF1, in area 0.0.0.1 via interface SL1-0.0.0.0-10.151.22.22
            m = p15.match(line)
            if m:
                sub_dict['neighbors'][nbr_router_id]['instance'] = m.groupdict()['inst']
                sub_dict['neighbors'][nbr_router_id]['area'] = m.groupdict()['area']
                sub_dict['neighbors'][nbr_router_id]['backbone_area_id'] = m.groupdict()['backbone']
                sub_dict['neighbors'][nbr_router_id]['local'] = m.groupdict()['local']
                continue

            #   -10.229.11.11
            m = p16.match(line)
            if m:
                sub_dict['neighbors'][nbr_router_id]['remote'] = m.groupdict()['remote']
                continue

            # State is FULL, 5 state changes, last change 00:07:51
            # State is FULL, 8 state changes, last change 08:10:01
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
                    del remote_addr
                except Exception:
                    pass
                continue

            # Hello options 0x32, dbd options 0x72
            # Hello options 0x32, dbd options 0x72
            m = p18.match(line)
            if m:
                hello = m.groupdict()['hello']
                dbd = m.groupdict()['dbd']
                sub_dict['neighbors'][nbr_router_id]['hello_option'] = hello
                sub_dict['neighbors'][nbr_router_id]['dbd_option'] = dbd
                continue

            # Last non-hello packet received 00:07:49
            # Last non-hello packet received never
            m = p19.match(line)
            if m:
                non_hello = m.groupdict()['last']
                sub_dict['neighbors'][nbr_router_id]['last_non_hello_received'] = non_hello
                continue

            # Dead timer due in 00:00:33
            # Dead timer due in 00:00:33
            m = p20.match(line)
            if m:
                sub_dict['neighbors'][nbr_router_id]['dead_timer'] = m.groupdict()['dead_timer']
                continue


        return ret_dict


# ====================================================
# Schema for 'show ip ospf virtual-links [vrf <WORD>]'
# ====================================================
class ShowIpOspfVirtualLinksSchema(MetaParser):

    """Schema for:
        show ip ospf virtual-links
        show ip ospf virtual-links vrf <vrf>"""

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'instance': {
                            Any(): {
                                'areas': {
                                    Any(): {
                                      'virtual_links': {
                                          Any(): {
                                              'transit_area_id': str,
                                              'backbone_area_id': str,
                                              'router_id': str,
                                              'name': str,
                                              'link_state': str,
                                              Optional('unnumbered_interface'): str,
                                              Optional('unnumbered_ip_address'): str,
                                              'interface': str,
                                              'remote_addr': str,
                                              'hello_interval': int,
                                              'dead_interval': int,
                                              'retransmit_interval': int,
                                              'wait_interval': int,
                                              'transmit_delay': int,
                                              'index': int,
                                              Optional('nbr_total'): int,
                                              Optional('nbr_flood'): int,
                                              Optional('nbr_adjs'): int,
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
                                              'interface_type': str,
                                              Optional('hello_timer'): str,
                                              Optional('wait_timer'): int,
                                              'statistics': {
                                                  'link_scope_lsa_count': int,
                                                  'link_scope_lsa_cksum_sum': int,
                                              },
                                              Optional('neighbors'): {
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
class ShowIpOspfVirtualLinks(ShowIpOspfVirtualLinksSchema, ShowIpOspfLinksParser):
    """Parser for:
        show ip ospf virtual-links
        show ip ospf virtual-links vrf <vrf>"""

    cli_command = ['show ip ospf virtual-links vrf {vrf}','show ip ospf virtual-links']
    exclude = [
        'df_uptime',
        'is_rpf',
        'df_address']

    def cli(self, vrf='',output=None):
        
        if vrf:
            cmd = self.cli_command[0].format(vrf=vrf)
        else:
            cmd = self.cli_command[1]

        return super().cli(cmd,output=output)


# =================================================
# Schema for 'show ip ospf sham-links [vrf <WORD>]'
# =================================================
class ShowIpOspfShamLinksSchema(MetaParser):
    """Schema for:
        show ip ospf sham-links
        show ip ospf sham-links vrf <vrf>"""

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'instance': {
                            Any(): {
                                'areas': {
                                    Any(): {
                                      'sham_links': {
                                          Any(): {
                                              'transit_area_id': str,
                                              'backbone_area_id': str,
                                              'local_id': str,
                                              'remote_id': str,
                                              'name': str,
                                              'link_state': str,
                                              Optional('unnumbered_interface'): str,
                                              Optional('unnumbered_ip_address'): str,
                                              'hello_interval': int,
                                              'dead_interval': int,
                                              'retransmit_interval': int,
                                              'wait_interval': int,
                                              'transmit_delay': int,
                                              'index': int,
                                              Optional('nbr_total'): int,
                                              Optional('nbr_flood'): int,
                                              Optional('nbr_adjs'): int,
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
                                              'interface_type': str,
                                              Optional('hello_timer'): str,
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
class ShowIpOspfShamLinks(ShowIpOspfShamLinksSchema, ShowIpOspfLinksParser):
    """Parser for:
        show ip ospf sham-links
        show ip ospf sham-links vrf <vrf>"""

    cli_command = ['show ip ospf sham-links vrf {vrf}', 'show ip ospf sham-links']

    def cli(self, vrf='', output=None):
        if vrf:
            cmd = self.cli_command[0].format(vrf=vrf)
        else:
            cmd = self.cli_command[1]

        return super().cli(cmd,output=output)


# ================================================
# Schema for 'show ip ospf interface [vrf <WORD>]'
# ================================================
class ShowIpOspfInterfaceSchema(MetaParser):
    """Schema for:
        show ip ospf interface
        show ip ospf interface vrf <WORD>"""

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
                                                'bfd': 
                                                    {'enable': bool},
                                                'enable': bool,
                                                'line_protocol': str,
                                                'ip_address': str,
                                                'state': str,
                                                'interface_type': str,
                                                'cost': int,
                                                'index': int,
                                                'if_cfg': bool,
                                                Optional('transmit_delay'): int,
                                                Optional('passive'): bool,
                                                Optional('priority'): int,
                                                Optional('dr_router_id'): str,
                                                Optional('dr_ip_addr'): str,
                                                Optional('bdr_router_id'): str,
                                                Optional('bdr_ip_addr'): str,
                                                Optional('hello_interval'): int,
                                                Optional('dead_interval'): int,
                                                Optional('retransmit_interval'): int,
                                                Optional('wait_interval'): int,
                                                Optional('hello_timer'): str,
                                                Optional('statistics'): 
                                                    {Optional('link_scope_lsa_count'): int,
                                                    Optional('link_scope_lsa_cksum_sum'): int,
                                                    Optional('total_neighbors'): int,
                                                    Optional('num_nbrs_flooding'): int,
                                                    Optional('num_nbrs_adjacent'): int},
                                                Optional('authentication'):
                                                    {Optional('auth_trailer_key_chain'):
                                                        {Optional('key_chain'): str},
                                                    Optional('auth_trailer_key'):
                                                        {Optional('key'): str,
                                                        Optional('crypto_algorithm'): str},
                                                    },
                                                },
                                            },
                                        Optional('sham_links'): 
                                            {Any(): 
                                                {'name': str,
                                                'bfd': 
                                                    {'enable': bool},
                                                'enable': bool,
                                                'line_protocol': str,
                                                'ip_address': str,
                                                'state': str,
                                                'interface_type': str,
                                                'cost': int,
                                                'index': int,
                                                'if_cfg': bool,
                                                Optional('transmit_delay'): int,
                                                Optional('passive'): bool,
                                                Optional('priority'): int,
                                                Optional('dr_router_id'): str,
                                                Optional('dr_ip_addr'): str,
                                                Optional('bdr_router_id'): str,
                                                Optional('bdr_ip_addr'): str,
                                                Optional('hello_interval'): int,
                                                Optional('dead_interval'): int,
                                                Optional('retransmit_interval'): int,
                                                Optional('wait_interval'): int,
                                                Optional('hello_timer'): str,
                                                Optional('statistics'): 
                                                    {'link_scope_lsa_count': int,
                                                    'link_scope_lsa_cksum_sum': int,
                                                    Optional('total_neighbors'): int,
                                                    Optional('num_nbrs_flooding'): int,
                                                    Optional('num_nbrs_adjacent'): int},
                                                Optional('authentication'):
                                                    {Optional('auth_trailer_key_chain'):
                                                        {Optional('key_chain'): str},
                                                    Optional('auth_trailer_key'):
                                                        {Optional('key'): str,
                                                        Optional('crypto_algorithm'): str},
                                                    },
                                                },
                                            },
                                        Optional('virtual_links'): 
                                            {Any(): 
                                                {'name': str,
                                                'bfd': 
                                                    {'enable': bool},
                                                'backbone_area_id': str,
                                                'enable': bool,
                                                'line_protocol': str,
                                                'ip_address': str,
                                                'state': str,
                                                'interface_type': str,
                                                'cost': int,
                                                'index': int,
                                                'if_cfg': bool,
                                                Optional('transmit_delay'): int,
                                                Optional('passive'): bool,
                                                Optional('priority'): int,
                                                Optional('dr_router_id'): str,
                                                Optional('dr_ip_addr'): str,
                                                Optional('bdr_router_id'): str,
                                                Optional('bdr_ip_addr'): str,
                                                Optional('hello_interval'): int,
                                                Optional('dead_interval'): int,
                                                Optional('retransmit_interval'): int,
                                                Optional('wait_interval'): int,
                                                Optional('hello_timer'): str,
                                                Optional('statistics'): 
                                                    {'link_scope_lsa_count': int,
                                                    'link_scope_lsa_cksum_sum': int,
                                                    Optional('total_neighbors'): int,
                                                    Optional('num_nbrs_flooding'): int,
                                                    Optional('num_nbrs_adjacent'): int},
                                                Optional('authentication'):
                                                    {Optional('auth_trailer_key_chain'):
                                                        {Optional('key_chain'): str},
                                                    Optional('auth_trailer_key'):
                                                        {Optional('key'): str,
                                                        Optional('crypto_algorithm'): str},
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


# ================================================
# Parser for 'show ip ospf interface [vrf <WORD>]'
# ================================================
class ShowIpOspfInterface(ShowIpOspfInterfaceSchema):
    """Parser for:
        show ip ospf interface
        show ip ospf interface <interface>
        show ip ospf interface vrf <vrf>"""

    cli_command = ['show ip ospf interface vrf {vrf}',
                   'show ip ospf interface',
                   'show ip ospf interface {interface}']
    exclude = [
        'hello_timer',
        'bdr_ip_addr',
        'bdr_router_id',
        'dr_ip_addr',
        'dr_router_id',
        'state',
        'index']

    def cli(self, vrf='', interface='', output=None):
        if vrf:
            cmd = self.cli_command[0].format(vrf=vrf)
        else:
            if interface:
                cmd = self.cli_command[2].format(interface=interface)
            else:
                cmd = self.cli_command[1]

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}
        af = 'ipv4'

        # Mapping dict
        bool_dict = {'up': True, 'down': False}

        # Ethernet2/2 is up, line protocol is up
        # port-channel2.100 is up, line protocol is up
        p1 = re.compile(r'^(?P<intf>(\S+)) +is +(?P<enable>(up|down)),'
                         ' +line +protocol +is'
                         ' +(?P<line_protocol>(up|down))$')

        # IP address 10.2.3.2/24
        p2_1 = re.compile(r'^IP +address +(?P<ip_address>(\S+))$')

        # IP address 192.168.246.1/24, Process ID 2 VRF default, area 0.0.0.1
        p2_2 = re.compile(r'^IP +address +(?P<ip_address>(\S+)), +Process'
                               ' +ID +(?P<pid>(\S+)) +VRF +(?P<vrf>(\S+)),'
                               ' +area +(?P<area>(\S+))$')

        # Process ID 1 VRF default, area 0.0.0.0
        # Process ID UNDERLAY VRF default, area 0.0.0.0
        p2_3 = re.compile(r'^Process +ID +(?P<pid>(\S+)) +VRF'
                         ' +(?P<vrf>(\S+)), +area +(?P<area>(\S+))$')

        # Unnumbered interface using IP address of loopback1 (10.151.22.22)
        p3 = re.compile(r'^Unnumbered +interface +using +IP +address +of'
                           ' +(?P<interface>(\S+))'
                           ' +\((?P<ip_address>(\S+))\)$')

        # Enabled by interface configuration
        p4 = re.compile(r'^Enabled +by +interface +configuration$')

        # State BDR, Network type BROADCAST, cost 1
        p5 = re.compile(r'^State +(?P<state>(\S+)), +Network +type '
                         '(?P<intf_type>(\S+)), +cost +(?P<cost>(\d+))$')

        # Index 3, Transmit delay 1 sec, Router Priority 1
        p6_1 = re.compile(r'^Index +(?P<index>(\d+))(?:, +Transmit +delay'
                           ' +(?P<transmit_delay>(\d+)) +sec)?(?:, +Router'
                           ' +Priority +(?P<priority>(\d+)))?$')

        # Index 2, Passive interface
        p6_2 = re.compile(r'^Index +(?P<index>(\d+)), +Passive +interface$')

        # Designated Router ID: 10.36.3.3, address: 10.2.3.3
        p7_1 = re.compile(r'^(D|d)esignated +(R|r)outer +(ID|Id):'
                           ' (?P<router_id>(\S+)), +address:'
                           ' +(?P<ip_addr>(\S+))$')

        # Backup Designated Router ID: 10.16.2.2, address: 10.2.3.2
        p7_2 = re.compile(r'^(B|b)ackup +(D|d)esignated +(R|r)outer'
                           ' +(ID|Id): +(?P<router_id>(\S+)), +address:'
                           ' +(?P<ip_addr>(\S+))$')

        # 1 Neighbors, flooding to 1, adjacent with 1
        p8 = re.compile(r'^(?P<num_neighbors>(\d+)) +Neighbors, +flooding'
                         ' +to +(?P<flooding>(\d+)), +adjacent +with'
                         ' +(?P<adjacent>(\d+))$')

        # Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
        p9 = re.compile(r'^Timer +intervals: +Hello +(?P<hello>(\d+)),'
                         ' +Dead +(?P<dead>(\d+)), +Wait +(?P<wait>(\d+)),'
                         ' +Retransmit +(?P<retransmit>(\d+))$')

        # Hello timer due in 00:00:02
        p10 = re.compile(r'^Hello +timer +due +in +(?P<hello>(\S+))$')

        # Simple authentication
        # Simple authentication, using keychain test (ready)
        # Simple authentication, using keychain test (not ready)
        p11_1 = re.compile(r'^Simple +authentication(?:, +using +keychain'
                            ' +(?P<keychain>(\S+))'
                            ' +\((not +ready|ready)\))?$')

        # Message-digest authentication, using default key id 0
        p11_2 = re.compile(r'^Message-digest +authentication, +using'
                            ' +default key id +(?P<key>(\S+))$')

        # Number of opaque link LSAs: 0, checksum sum 0
        p12 = re.compile(r'^Number +of +opaque +link +LSAs:'
                          ' +(?P<count>(\d+)), +checksum +sum'
                          ' +(?P<checksum>(\d+))$')

        # BFD is enabled
        p13 = re.compile(r'^BFD +is +enabled$')

        for line in out.splitlines():
            line = line.strip()

            # Ethernet2/2 is up, line protocol is up
            # port-channel2.100 is up, line protocol is up
            m = p1.match(line)
            if m:
                # intf name
                interface = intf_name = str(m.groupdict()['intf'])
                # enable
                enable = str(m.groupdict()['enable'])
                # line_protocol
                line_protocol = str(m.groupdict()['line_protocol'])

                # Determine if 'interface' or 'sham_link' or 'virtual_link'
                if re.search('SL', interface):
                    pattern = '(?P<link>\w+)-(?P<area_id>[\w\.\:]+)-(?P<local>[\w\.\:]+)-(?P<remote>[\w\.\:]+)'
                    n = re.match(pattern, interface)
                    link = str(n.groupdict()['link'])
                    area_id = str(n.groupdict()['area_id'])
                    local = str(n.groupdict()['local'])
                    remote = str(n.groupdict()['remote'])
                    # Set values for dict
                    intf_type = 'sham_links'
                    intf_name = local + ' ' + remote
                elif re.search('VL', interface):
                    pattern = '(?P<link>\w+)-(?P<area_id>[\w\.\:]+)-(?P<router_id>[\w\.\:]+)'
                    n = re.match(pattern, interface)
                    link = str(n.groupdict()['link'])
                    backbone_area_id = str(n.groupdict()['area_id'])
                    router_id = str(n.groupdict()['router_id'])
                    # Set values for dict
                    intf_type = 'virtual_links'
                else:
                    # Set values for dict
                    intf_type = 'interfaces'
                    intf_name = interface

                continue
            
            # IP address 10.2.3.2/24
            m = p2_1.match(line)
            if m:
                ip_address = str(m.groupdict()['ip_address'])
                continue

            # IP address 192.168.246.1/24, Process ID 2 VRF default, area 0.0.0.1
            m = p2_2.match(line)
            if m:
                group = m.groupdict()
                vrf = str(group['vrf'])
                instance = str(group['pid'])
                ip_address = str(group['ip_address'])
                area = str(group['area'])

                if re.search('VL', interface):
                    intf_name = area + ' ' + router_id

                vrf_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {})
                af_dict = vrf_dict.setdefault('address_family', {}).\
                                   setdefault(af, {})
                instance_dict = af_dict.setdefault('instance', {}).\
                                        setdefault(instance, {})
                area_dict = instance_dict.setdefault('areas', {}).\
                                          setdefault(area, {})
                sub_dict = area_dict.setdefault(intf_type, {}).\
                                     setdefault(intf_name, {})

                # Set all other values
                sub_dict['bfd'] = {}
                sub_dict['bfd']['enable'] = False
                sub_dict['if_cfg'] = False

                try:
                    sub_dict['name'] = interface
                    del interface
                except Exception:
                    pass
                try:
                    sub_dict['enable'] = bool_dict[enable]
                except Exception:
                    pass
                try:
                    sub_dict['line_protocol'] = line_protocol
                    del line_protocol
                except Exception:
                    pass
                try:
                    sub_dict['ip_address'] = ip_address
                    del ip_address
                except Exception:
                    pass
                try:
                    sub_dict['backbone_area_id'] = backbone_area_id
                    del backbone_area_id
                except Exception:
                    pass
                continue

            # Process ID 1 VRF default, area 0.0.0.0
            # Process ID UNDERLAY VRF default, area 0.0.0.0
            m = p2_3.match(line)
            if m:
                instance = str(m.groupdict()['pid'])
                vrf = str(m.groupdict()['vrf'])
                area = str(m.groupdict()['area'])

                if re.search('VL', interface):
                    intf_name = area + ' ' + router_id

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
                if 'areas' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]:
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

                # Set all other values
                sub_dict['bfd'] = {}
                sub_dict['bfd']['enable'] = False
                sub_dict['if_cfg'] = False

                try:
                    sub_dict['name'] = interface
                    del interface
                except Exception:
                    pass
                try:
                    sub_dict['enable'] = bool_dict[enable]
                except Exception:
                    pass
                try:
                    sub_dict['line_protocol'] = line_protocol
                    del line_protocol
                except Exception:
                    pass
                try:
                    sub_dict['ip_address'] = ip_address
                    del ip_address
                except Exception:
                    pass
                try:
                    sub_dict['backbone_area_id'] = backbone_area_id
                    del backbone_area_id
                except Exception:
                    pass
                continue

            # Unnumbered interface using IP address of loopback1 (10.151.22.22)
            m = p3.match(line)
            if m:
                ip_address = str(m.groupdict()['ip_address'])
                continue

            # Enabled by interface configuration
            m = p4.match(line)
            if m:
                sub_dict['if_cfg'] = True
                continue

            # State BDR, Network type BROADCAST, cost 1
            m = p5.match(line)
            if m:
                sub_dict['state'] = str(m.groupdict()['state']).lower()
                sub_dict['interface_type'] = \
                    str(m.groupdict()['intf_type']).lower()
                sub_dict['cost'] = int(m.groupdict()['cost'])
                continue

            # Index 3, Transmit delay 1 sec, Router Priority 1
            m = p6_1.match(line)
            if m:
                sub_dict['index'] = int(m.groupdict()['index'])
                if m.groupdict()['transmit_delay']:
                    sub_dict['transmit_delay'] = \
                        int(m.groupdict()['transmit_delay'])
                    sub_dict['passive'] = False
                if m.groupdict()['priority']:
                    sub_dict['priority'] = int(m.groupdict()['priority'])
                continue

            # Index 2, Passive interface
            m = p6_2.match(line)
            if m:
                sub_dict['index'] = int(m.groupdict()['index'])
                sub_dict['passive'] = True
                continue

            # Designated Router ID: 10.36.3.3, address: 10.2.3.3
            m = p7_1.match(line)
            if m:
                sub_dict['dr_router_id'] = str(m.groupdict()['router_id'])
                sub_dict['dr_ip_addr'] = str(m.groupdict()['ip_addr'])
                continue

            # Backup Designated Router ID: 10.16.2.2, address: 10.2.3.2
            m = p7_2.match(line)
            if m:
                sub_dict['bdr_router_id'] = str(m.groupdict()['router_id'])
                sub_dict['bdr_ip_addr'] = str(m.groupdict()['ip_addr'])
                continue

            # 1 Neighbors, flooding to 1, adjacent with 1
            m = p8.match(line)
            if m:
                if 'statistics' not in sub_dict:
                    sub_dict['statistics'] = {}
                sub_dict['statistics']['total_neighbors'] = \
                    int(m.groupdict()['num_neighbors'])
                sub_dict['statistics']['num_nbrs_flooding'] = \
                    int(m.groupdict()['flooding'])
                sub_dict['statistics']['num_nbrs_adjacent'] = \
                    int(m.groupdict()['adjacent'])
                continue

            # Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
            m = p9.match(line)
            if m:
                sub_dict['hello_interval'] = int(m.groupdict()['hello'])
                sub_dict['dead_interval'] = int(m.groupdict()['dead'])
                sub_dict['retransmit_interval'] = \
                    int(m.groupdict()['retransmit'])
                sub_dict['wait_interval'] = int(m.groupdict()['wait'])
                continue

            # Hello timer due in 00:00:02
            m = p10.match(line)
            if m:
                sub_dict['hello_timer'] = str(m.groupdict()['hello'])
                continue

            # Simple authentication
            # Simple authentication, using keychain test (ready)
            # Simple authentication, using keychain test (not ready)
            m = p11_1.match(line)
            if m:
                if 'authentication' not in sub_dict:
                    sub_dict['authentication'] = {}
                if 'auth_trailer_key' not in sub_dict['authentication']:
                    sub_dict['authentication']['auth_trailer_key'] = {}
                    sub_dict['authentication']['auth_trailer_key']\
                        ['crypto_algorithm'] = 'Simple'
                # Set keychain
                if m.groupdict()['keychain']:
                    if 'auth_trailer_key_chain' not in sub_dict['authentication']:
                        sub_dict['authentication']['auth_trailer_key_chain'] = {}
                        sub_dict['authentication']['auth_trailer_key_chain']\
                            ['key_chain'] = str(m.groupdict()['keychain'])
                    continue

            # Message-digest authentication, using default key id 0
            m = p11_2.match(line)
            if m:
                if 'authentication' not in sub_dict:
                    sub_dict['authentication'] = {}
                if 'auth_trailer_key' not in sub_dict['authentication']:
                    sub_dict['authentication']['auth_trailer_key'] = {}
                    sub_dict['authentication']['auth_trailer_key']\
                        ['crypto_algorithm'] = 'Message-digest'
                if 'auth_trailer_key_chain' not in sub_dict['authentication']:
                    sub_dict['authentication']['auth_trailer_key_chain'] = {}
                    sub_dict['authentication']['auth_trailer_key_chain']\
                        ['key'] = str(m.groupdict()['key'])
                    continue

            # Number of opaque link LSAs: 0, checksum sum 0
            m = p12.match(line)
            if m:
                count = int(m.groupdict()['count'])
                checksum = int(m.groupdict()['checksum'])
                if 'statistics' not in sub_dict:
                    sub_dict['statistics'] = {}
                sub_dict['statistics']['link_scope_lsa_count'] = \
                    int(m.groupdict()['count'])
                sub_dict['statistics']['link_scope_lsa_cksum_sum'] = \
                    int(m.groupdict()['checksum'])
                continue

            # BFD is enabled
            m = p13.match(line)
            if m:
                sub_dict['bfd']['enable'] = True
                continue

        return ret_dict


# =======================================================
# Schema for 'show ip ospf neighbors detail [vrf <WORD>]'
# =======================================================
class ShowIpOspfNeighborDetailSchema(MetaParser):
    """Schema for:
        show ip ospf neighbors detail
        show ip ospf neighbors detail vrf <vrf>"""

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {'areas': 
                                    {Any(): 
                                        {'interfaces': 
                                            {Any(): 
                                                {'neighbors':
                                                     {Any(): 
                                                        {'neighbor_router_id': str,
                                                        'address': str,
                                                        'state': str,
                                                        'last_state_change': str,
                                                        Optional('priority'): int,
                                                        Optional('dr_ip_addr'): str,
                                                        Optional('bdr_ip_addr'): str,
                                                        Optional('dr_router_id'): str,
                                                        Optional('bdr_router_id'): str,
                                                        'hello_options': str,
                                                        'dbd_options': str,
                                                        'last_non_hello_packet_received': str,
                                                        'dead_timer': str,
                                                        Optional('statistics'): {
                                                            Optional('nbr_event_count'): int,
                                                            },
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
                                                        'state': str,
                                                        'last_state_change': str,
                                                        Optional('priority'): int,
                                                        Optional('dr_ip_addr'): str,
                                                        Optional('bdr_ip_addr'): str,
                                                        Optional('dr_router_id'): str,
                                                        Optional('bdr_router_id'): str,
                                                        'hello_options': str,
                                                        'dbd_options': str,
                                                        'last_non_hello_packet_received': str,
                                                        'dead_timer': str,
                                                        Optional('statistics'): {
                                                            Optional('nbr_event_count'): int,
                                                            },
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
                                                        'state': str,
                                                        'last_state_change': str,
                                                        Optional('priority'): int,
                                                        Optional('dr_ip_addr'): str,
                                                        Optional('bdr_ip_addr'): str,
                                                        Optional('dr_router_id'): str,
                                                        Optional('bdr_router_id'): str,
                                                        'hello_options': str,
                                                        'dbd_options': str,
                                                        'last_non_hello_packet_received': str,
                                                        'dead_timer': str,
                                                        Optional('statistics'): {
                                                            Optional('nbr_event_count'): int,
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


# =======================================================
# Parser for 'show ip ospf neighbors detail [vrf <WORD>]'
# =======================================================
class ShowIpOspfNeighborDetail(ShowIpOspfNeighborDetailSchema):
    """Parser for:
        show ip ospf neighbors detail
        show ip ospf neighbors <neighbor> detail
        show ip ospf neighbors detail vrf <vrf>
        show ip ospf neighbors <neighbor> detail vrf <vrf>"""

    cli_command = ['show ip ospf neighbors detail vrf {vrf}',
                   'show ip ospf neighbors {neighbor} detail vrf {vrf}',
                   'show ip ospf neighbors {neighbor} detail',
                   'show ip ospf neighbors detail']
    exclude = [
        'dead_timer',
        'last_non_hello_packet_received',
        'last_state_change',
        'bdr_ip_addr',
        'dr_ip_addr',
        'nbr_event_count']

    def cli(self, vrf='', neighbor='', output=None):
        if vrf:
            if neighbor:
                cmd = self.cli_command[1].format(vrf=vrf, neighbor=neighbor)
            else:
                cmd = self.cli_command[0].format(vrf=vrf)
        else:
            if neighbor:
                cmd = self.cli_command[2].format(neighbor=neighbor)
            else:
                cmd = self.cli_command[3]

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}
        af = 'ipv4'
        p1 = re.compile(r'^Neighbor +(?P<neighbor_router_id>(\S+)),'
                            ' +interface +address +(?P<address>(\S+))$')
        p2 = re.compile(r'^Process +ID +(?P<instance>(\S+)) +VRF'
                            ' +(?P<vrf>(\S+)), +in +area +(?P<area>(\S+))'
                            ' +via +interface +(?P<interface>(\S+))$')
        p3 = re.compile(r'^State +is +(?P<state>(\S+)),'
                            ' +(?P<changes>(\d+)) +state +changes,'
                            ' +last +change +(?P<last>(\S+))$')
        p4 = re.compile(r'^Neighbor +priority +is +(?P<priority>(\S+))$')
        p5 = re.compile(r'^DR +is +(?P<dr_ip>(\S+)) +BDR +is'
                            ' +(?P<bdr_ip>(\S+))$')
        p6 = re.compile(r'^Hello +options +(?P<hello_options>(\S+)),'
                            ' +dbd +options +(?P<dbd_options>(\S+))$')
        p7 = re.compile(r'^Last +non-hello +packet +received'
                            ' +(?P<non_hello>(\S+))$')
        p8 = re.compile(r'^Dead +timer +due +in +(?P<dead_timer>(\S+))$')

        for line in out.splitlines():
            line = line.strip()

            # Neighbor 10.36.3.3, interface address 10.2.3.3
            m = p1.match(line)
            if m:
                neighbor = str(m.groupdict()['neighbor_router_id'])
                address = str(m.groupdict()['address'])
                continue

            # Process ID 1 VRF default, in area 0.0.0.0 via interface Ethernet2/2
            # Process ID 1 VRF VRF1, in area 0.0.0.1 via interface SL1-0.0.0.0-10.151.22.22-10.229.11.11
            # Process ID 1 VRF default, in area 0.0.0.0 via interface VL1-0.0.0.1-10.64.4.4
            m = p2.match(line)
            if m:
                instance = str(m.groupdict()['instance'])
                vrf = str(m.groupdict()['vrf'])
                area = str(m.groupdict()['area'])
                interface = str(m.groupdict()['interface'])

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
                if 'areas' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area] = {}

                # Determine if 'interface' or 'sham_link' or 'virtual_link'
                if re.search('SL', interface):
                    pattern = '(?P<link>\w+)-(?P<area_id>[\w\.\:]+)-(?P<local>[\w\.\:]+)-(?P<remote>[\w\.\:]+)'
                    n = re.match(pattern, interface)
                    link = str(n.groupdict()['link'])
                    area_id = str(n.groupdict()['area_id'])
                    local = str(n.groupdict()['local'])
                    remote = str(n.groupdict()['remote'])
                    # Set values for dict
                    intf_type = 'sham_links'
                    intf_name = local + ' ' + remote

                elif re.search('VL', interface):
                    pattern = '(?P<link>\w+)-(?P<area_id>[\w\.\:]+)-(?P<router_id>[\w\.\:]+)'
                    n = re.match(pattern, interface)
                    link = str(n.groupdict()['link'])
                    area_id = str(n.groupdict()['area_id'])
                    router_id = str(n.groupdict()['router_id'])
                    # Set values for dict
                    intf_type = 'virtual_links'
                    intf_name = area_id + ' ' + router_id
                else:
                    # Set values for dict
                    intf_type = 'interfaces'
                    intf_name = interface

                # Set interface/sham_link/virtual_link dict
                if intf_type not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][intf_type] = {}
                if intf_name not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area][intf_type]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][intf_type][intf_name] = {}
                if 'neighbors' not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area]\
                        [intf_type][intf_name]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][intf_type][intf_name]\
                        ['neighbors'] = {}
                if neighbor not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area]\
                        [intf_type][intf_name]['neighbors']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][intf_type][intf_name]\
                        ['neighbors'][neighbor] = {}

                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]['areas'][area]\
                            [intf_type][intf_name]['neighbors'][neighbor]

                # Set previously parsed keys
                sub_dict['neighbor_router_id'] = neighbor
                sub_dict['address'] = address
                continue

            # State is FULL, 5 state changes, last change 08:38:40
            m = p3.match(line)
            if m:
                sub_dict['state'] = str(m.groupdict()['state']).lower()
                sub_dict['last_state_change'] = str(m.groupdict()['last'])
                if 'statistics' not in sub_dict:
                    sub_dict['statistics'] = {}
                    sub_dict['statistics']['nbr_event_count'] = int(m.groupdict()['changes'])
                    continue

            # Neighbor priority is 1
            m = p4.match(line)
            if m:
                sub_dict['priority'] = int(m.groupdict()['priority'])
                continue

            # DR is 10.2.3.3 BDR is 10.2.3.2
            m = p5.match(line)
            if m:
                sub_dict['dr_ip_addr'] = str(m.groupdict()['dr_ip'])
                sub_dict['bdr_ip_addr'] = str(m.groupdict()['bdr_ip'])
                continue

            # Hello options 0x12, dbd options 0x52
            m = p6.match(line)
            if m:
                sub_dict['hello_options'] = str(m.groupdict()['hello_options'])
                sub_dict['dbd_options']= str(m.groupdict()['dbd_options'])
                continue

            # Last non-hello packet received never
            m = p7.match(line)
            if m:
                sub_dict['last_non_hello_packet_received'] = \
                    str(m.groupdict()['non_hello'])
                continue

            # Dead timer due in 00:00:39
            m = p8.match(line)
            if m:
                sub_dict['dead_timer'] = str(m.groupdict()['dead_timer'])
                continue

        return ret_dict


# ===================================================================
# Super parser for 'show ip ospf database <WORD> detail [vrf <WORD>]'
# ===================================================================
class ShowIpOspfDatabaseDetailParser(MetaParser):
    """Parser for:
        show ip ospf database <db_type> detail
        show ip ospf database <db_type> detail vrf <vrf>"""

    def cli(self, cmd, db_type,output):

        assert db_type in ['external', 'network', 'summary', 'router',
                           'opaque']

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output
        
        # Init vars
        ret_dict = {}
        af = 'ipv4'
        mt_id = 0

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

        p1 = re.compile(r'^ *OSPF +Router +with +ID +\((?P<router_id>(\S+))\)'
                            ' +\(Process +ID +(?P<instance>(\S+))'
                            ' +VRF +(?P<vrf>(\S+))\)$')
        p2 = re.compile(r'^(?P<lsa_type_name>(.*)) +Link +States'
                            '(?: +\(Area +(?P<area>(\S+))\))?$')
        p3 = re.compile(r'^LS +age: +(?P<age>\d+)'
                            '(?P<dummy>\S+)?$')
        p4 = re.compile(r'^Options: +(?P<option>([a-zA-Z0-9]+))(?:'
                            ' *\((?P<option_desc>(.*))\))?$')
        p5 = re.compile(r'^LS +Type: +(?P<lsa_type>(.*))$')
        p36 = re.compile(r'^Link +State +ID: +(?P<lsa_id>(\S+))'
                            '(?: +\(.*\))?$')
        p6 = re.compile(r'^Advertising +Router: +(?P<adv_router>(\S+))$')
        p7 = re.compile(r'^LS +Seq +Number: +(?P<ls_seq_num>(\S+))$')
        p8 = re.compile(r'^Checksum: +(?P<checksum>(\S+))$')
        p9 = re.compile(r'^Length: +(?P<length>(\d+))$')
        p10 = re.compile(r'^Network +Mask: +\/(?P<net_mask>(\S+))$')
        p11 = re.compile(r'^Metric +Type: +2 +\(.*\)$')
        p12_1 = re.compile(r'^TOS: +(?P<tos>(\d+))$')
        p12_2 = re.compile(r'^TOS: +(?P<tos>(\d+)) +Metric: +(?P<metric>(\d+))$')
        p13 = re.compile(r'^Metric: +(?P<metric>(\d+))$')
        p14 = re.compile(r'^Forward +Address: +(?P<addr>(\S+))$')
        p15 = re.compile(r'^External +Route +Tag: +(?P<tag>(\S+))$')
        p16 = re.compile(r'^Attached +Router: +(?P<att_router>(\S+))$')
        p17 = re.compile(r'^Number +of +links: +(?P<num>(\d+))$')
        p18 = re.compile(r'^Link +connected +to: +a +(?P<type>(.*))$')
        p19_1 = re.compile(r'^\(Link +ID\) +Network\/Subnet +Number:'
                            ' +(?P<link_id>(\S+))$')
        p19_2 = re.compile(r'^\(Link +ID\) +Designated +Router +address:'
                            ' +(?P<link_id>(\S+))$')
        p19_3 = re.compile(r'^\(Link +ID\) +Neighboring +Router +ID:'
                            ' +(?P<link_id>(\S+))$')
        p20_1 = re.compile(r'^\(Link +Data\) +Network +Mask:'
                            ' +(?P<link_data>(\S+))$')
        p20_2 = re.compile(r'^\(Link +Data\) +Router +Interface +address:'
                            ' +(?P<link_data>(\S+))$')
        p21 = re.compile(r'^Number +of +TOS +metrics: +(?P<num>(\d+))$')
        p21_1 = re.compile(r'^TOS +(?P<tos>(\d+)) +Metric: +(?P<metric>(\d+))$')
        p22 = re.compile(r'^Opaque +Type: +(?P<type>(\d+))$')
        p23 = re.compile(r'^Opaque +ID: +(?P<id>(\d+))$')
        p24 = re.compile(r'^Fragment +number: +(?P<num>(\d+))$')
        p25 = re.compile(r'^MPLS +TE +router +ID *: +(?P<mpls>(\S+))$')
        p26 = re.compile(r'^Number +of +Links *: +(?P<links>(\d+))$')
        p27 = re.compile(r'^Link +connected +to +(?P<link>(.*))$')
        p28 = re.compile(r'^(?:Link-ID +:)? *(Link +ID|Link-ID) *:'
                            ' +(?P<id>(\S+))$')
        p29 = re.compile(r'^(?:Interface +Address +:)? *Interface'
                            ' +Address *: +(?P<addr>(\S+))$')
        p30 = re.compile(r'^Admin +Metric *: +(?P<te_metric>(\d+))$')
        p31 = re.compile(r'^Maximum +(B|b)andwidth *:'
                            ' +(?P<max_band>(\d+))$')
        p32 = re.compile(r'^Maximum +(R|r)eservable +(B|b)andwidth *:'
                            ' +(?P<max_res_band>(\d+))$')
        p33 = re.compile(r'^Affinity +Bit *: +(?P<admin_group>(\S+))$')
        p34 = re.compile(r'^Priority +(?P<num1>(\d+)) *:'
                            ' +(?P<band1>(\d+))(?: +Priority +(?P<num2>(\d+))'
                            ' *: +(?P<band2>(\d+)))?$')
        p35 = re.compile(r'^Unknown +Sub-TLV *: +Type += +(?P<type>(\d+)),'
                            ' +Length += +(?P<length>(\d+))'
                            ' +Value += +(?P<value>(.*))$')
        p40 = re.compile(r'^(?P<something>([0\s]+))$')
        for line in out.splitlines():
            line = line.strip()

            # OSPF Router with ID (10.16.2.2) (Process ID 1 VRF default)
            # OSPF Router with ID (10.151.22.22) (Process ID 1 VRF VRF1)
            # OSPF Router with ID (10.186.0.1) (Process ID UNDERLAY VRF default)
            m = p1.match(line)
            if m:
                router_id = str(m.groupdict()['router_id'])
                instance = str(m.groupdict()['instance'])
                vrf = str(m.groupdict()['vrf'])
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

            # Type-5 AS External Link States (Area 0.0.0.0)
            # Opaque Area Link States (Area 0.0.0.0)
            # Summary Network Link States (Area 0.0.0.0)
            # Network Link States (Area 0.0.0.0)
            m = p2.match(line)
            if m:
                lsa_type = lsa_type_mapping[db_type]
                
                # Set area
                if m.groupdict()['area']:
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

            # LS age: 1565
            # LS age: 3690(Maxage)
            m = p3.match(line)
            if m:
                age = int(m.groupdict()['age'])
                dummy = m.groupdict()['dummy']
                if dummy and "maxage" in dummy.lower():
                    maxage = True
                continue

            # Options: 0x20 (No TOS-capability, DC)
            m = p4.match(line)
            if m:
                option = str(m.groupdict()['option'])
                option_desc = str(m.groupdict()['option_desc'])
                continue

            # LS Type: Type-5 AS-External
            m = p5.match(line)
            if m:
                lsa_type = lsa_type_mapping[db_type]
                continue

            # Link State ID: 10.4.1.1
            # Link State ID: 10.94.44.44 (Network address)
            # Link State ID: 10.1.2.1 (Designated Router address)
            m = p36.match(line)
            if m:
                lsa_id = str(m.groupdict()['lsa_id'])
                continue

            # Advertising Router: 10.64.4.4
            m = p6.match(line)
            if m:
                adv_router = str(m.groupdict()['adv_router'])
                lsa = lsa_id + ' ' + adv_router
                
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
                    if mt_id not in db_dict['topologies']:
                        db_dict['topologies'][mt_id] = {}
                    db_topo_dict = db_dict['topologies'][mt_id]
                    db_topo_dict['mt_id'] = mt_id

                # Set header dict
                if 'header' not in sub_dict['lsas'][lsa]['ospfv2']:
                    sub_dict['lsas'][lsa]['ospfv2']['header'] = {}
                header_dict = sub_dict['lsas'][lsa]['ospfv2']['header']

                try:
                    # Set previously parsed values
                    header_dict['age'] = age
                    del age
                except Exception:
                    pass
                try:
                    # Set previously parsed values
                    header_dict['maxage'] = maxage
                    del maxage
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
            m = p7.match(line)
            if m:
                header_dict['seq_num'] = str(m.groupdict()['ls_seq_num'])
                continue

            # Checksum: 0x7d61
            m = p8.match(line)
            if m:
                header_dict['checksum'] = str(m.groupdict()['checksum'])
                continue

            # Length: 36
            m = p9.match(line)
            if m:
                header_dict['length'] = int(m.groupdict()['length'])
                continue

            # Network Mask: /32
            m = p10.match(line)
            if m:
                dummy = '{}/{}'.format('0.0.0.0', m.groupdict()['net_mask'])
                db_dict['network_mask'] = str(IPNetwork(dummy).netmask)
                continue

            # Metric Type: 2 (Larger than any link state path)
            m = p11.match(line)
            if m:
                db_topo_dict['flags'] = "E"
                continue

            # TOS: 0
            m = p12_1.match(line)
            if m:
                db_topo_dict['tos'] = int(m.groupdict()['tos'])
                continue

            # TOS: 0 Metric: 1
            m = p12_2.match(line)
            if m:
                db_topo_dict['tos'] = int(m.groupdict()['tos'])
                db_topo_dict['metric'] = int(m.groupdict()['metric'])
                continue

            # Metric: 20
            m = p13.match(line)
            if m:
                db_topo_dict['metric'] = int(m.groupdict()['metric'])
                continue

            # Forward Address: 0.0.0.0
            m = p14.match(line)
            if m:
                db_topo_dict['forwarding_address'] = str(m.groupdict()['addr'])
                continue

            # External Route Tag: 0
            m = p15.match(line)
            if m:
                db_topo_dict['external_route_tag'] = int(m.groupdict()['tag'])            
                continue

            # Attached Router: 10.84.66.66
            m = p16.match(line)
            if m:
                attached_router = str(m.groupdict()['att_router'])
                if 'attached_routers' not in db_dict:
                    db_dict['attached_routers'] = {}
                if attached_router not in db_dict['attached_routers']:
                    db_dict['attached_routers'][attached_router] = {}
                    continue

            # Number of links: 3
            m = p17.match(line)
            if m:
                db_dict['num_of_links'] = int(m.groupdict()['num'])
                continue

            # Link connected to: a Stub Network
            m = p18.match(line)
            if m:
                link_type = str(m.groupdict()['type']).lower()
                continue

            # (Link ID) Network/Subnet Number: 10.4.1.1
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
                    del link_type
                except Exception:
                    pass
                
                # Create topology dict under link_id
                if 'topologies' not in db_dict['links'][link_id]:
                    db_dict['links'][link_id]['topologies'] = {}
                if mt_id not in db_dict['links'][link_id]['topologies']:
                    db_dict['links'][link_id]['topologies'][mt_id] = {}
                db_dict['links'][link_id]['topologies'][mt_id]['mt_id'] = mt_id
                continue
                
            # (Link ID) Designated Router address: 10.166.7.6
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
                    del link_type
                except Exception:
                    pass
                
                # Create topology dict under link_id
                if 'topologies' not in db_dict['links'][link_id]:
                    db_dict['links'][link_id]['topologies'] = {}
                if mt_id not in db_dict['links'][link_id]['topologies']:
                    db_dict['links'][link_id]['topologies'][mt_id] = {}
                db_dict['links'][link_id]['topologies'][mt_id]['mt_id'] = mt_id
                continue

            # (Link ID) Neighboring Router ID: 10.151.22.22
            # (Link ID) Neighboring Router ID: 10.186.0.2
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
                    del link_type
                except Exception:
                    pass
                
                # Create topology dict under link_id
                if 'topologies' not in db_dict['links'][link_id]:
                    db_dict['links'][link_id]['topologies'] = {}
                if mt_id not in db_dict['links'][link_id]['topologies']:
                    db_dict['links'][link_id]['topologies'][mt_id] = {}
                db_dict['links'][link_id]['topologies'][mt_id]['mt_id'] = mt_id
                continue

            # (Link Data) Network Mask: 255.255.255.255
            m = p20_1.match(line)
            if m:
                db_dict['links'][link_id]['link_data'] = \
                    str(m.groupdict()['link_data'])
                continue

            # (Link Data) Router Interface address: 10.166.7.6
            m = p20_2.match(line)
            if m:
                db_dict['links'][link_id]['link_data'] = \
                    str(m.groupdict()['link_data'])
                continue

            # Number of TOS metrics: 0
            m = p21.match(line)
            if m:
                db_dict['links'][link_id]['num_tos_metrics'] = \
                    int(m.groupdict()['num'])
                continue

            # TOS   0 Metric: 1
            m = p21_1.match(line)
            if m:
                if db_type == 'router':
                    db_dict['links'][link_id]['topologies'][mt_id]['tos'] = int(m.groupdict()['tos'])
                    db_dict['links'][link_id]['topologies'][mt_id]['metric'] = int(m.groupdict()['metric'])
                continue

            # Opaque Type: 1
            m = p22.match(line)
            if m:
                opaque_type = int(m.groupdict()['type'])
                continue
            
            # Opaque ID: 38
            m = p23.match(line)
            if m:
                opaque_id = int(m.groupdict()['id'])
                continue

            # Fragment number: 0
            m = p24.match(line)
            if m:
                header_dict['fragment_number'] = int(m.groupdict()['num'])
                continue

            # MPLS TE router ID : 10.4.1.1
            m = p25.match(line)
            if m:
                header_dict['mpls_te_router_id'] = str(m.groupdict()['mpls'])
                continue

            # Number of Links : 0
            m = p26.match(line)
            if m:
                header_dict['num_links'] = int(m.groupdict()['links'])
                continue

            # Link connected to Broadcast network
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
            # Link-ID : 10.1.11.2
            # Link-ID :   Link ID : 192.168.106.2
            m = p28.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]['link_id'] = \
                    str(m.groupdict()['id'])
                continue

            # Interface Address : 10.1.4.1
            # Interface Address :   Interface Address : 192.168.106.2
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
            m = p30.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]['te_metric'] = \
                    int(m.groupdict()['te_metric'])
                continue

            # Maximum Bandwidth : 125000000
            m = p31.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]['max_bandwidth'] = \
                    int(m.groupdict()['max_band'])
                continue

            # Maximum reservable bandwidth : 93750000
            m = p32.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]\
                    ['max_reservable_bandwidth'] = \
                    int(m.groupdict()['max_res_band'])
                continue

            # Affinity Bit : 0x0
            m = p33.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]['admin_group'] = \
                    str(m.groupdict()['admin_group'])
                continue

            # Number of Priority : 8
            
            # Priority 0 : 93750000    Priority 1 : 93750000
            m = p34.match(line)
            if m:
                value1 = str(m.groupdict()['num1']) + ' ' + \
                         str(m.groupdict()['band1'])
                value2 = str(m.groupdict()['num2']) + ' ' + \
                         str(m.groupdict()['band2'])
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
            m = p35.match(line)
            if m:
                unknown_tlvs_counter += 1
                tlv_value = ''
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
                tlv_value += str(m.groupdict()['value'])
                db_dict['link_tlvs'][link_tlv_counter]['unknown_tlvs']\
                    [unknown_tlvs_counter]['value'] = tlv_value
                continue

            # 0 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            # 00 00 00 00 00 00 00 00 00 00 00 00 
            m = p40.match(line)
            if m:
                tlv_value = tlv_value + ' ' + line
                db_dict['link_tlvs'][link_tlv_counter]['unknown_tlvs']\
                    [unknown_tlvs_counter]['value'] = tlv_value
                continue

        return ret_dict


# ===============================================================
# Schema for 'show ip ospf database external detail [vrf <WORD>]'
# ===============================================================
class ShowIpOspfDatabaseExternalDetailSchema(MetaParser):
    """Schema for:
        show ip ospf database external detail
        show ip ospf database external detail vrf <vrf>"""

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
                                                                    Optional('maxage'): bool,
                                                                    'type': int,
                                                                    'adv_router': str,
                                                                    'seq_num': str,
                                                                    'checksum': str,
                                                                    'length': int},
                                                                'body': 
                                                                    {'external': 
                                                                        {'network_mask': str,
                                                                        'topologies': 
                                                                            {Any(): 
                                                                                {'mt_id': int,
                                                                                'tos': int,
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


# ===================================================================
# Super parser for 'show ip ospf database <WORD> detail [vrf <WORD>]'
# ===================================================================
class ShowIpOspfDatabaseExternalDetail(ShowIpOspfDatabaseExternalDetailSchema, ShowIpOspfDatabaseDetailParser):
    """Parser for:
        show ip ospf database external detail
        show ip ospf database external detail vrf <vrf>"""

    cli_command = ['show ip ospf database external detail vrf {vrf}', 'show ip ospf database external detail']
    exclude = [
        'age',
        'checksum',
        'seq_num']

    def cli(self, vrf='',output=None):
        # excute command to get output
        if vrf:
            cmd = self.cli_command[0].format(vrf=vrf)
        else:
            cmd = self.cli_command[1]

        return super().cli(cmd=cmd, db_type='external',output=output)


# ==============================================================
# Schema for 'show ip ospf database network detail [vrf <WORD>]'
# ==============================================================
class ShowIpOspfDatabaseNetworkDetailSchema(MetaParser):
    """Schema for:
        show ip ospf database network detail
        show ip ospf database network detail vrf <vrf>"""

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
                                                                    Optional('maxage'): bool,
                                                                    'type': int,
                                                                    'adv_router': str,
                                                                    'seq_num': str,
                                                                    'checksum': str,
                                                                    'length': int},
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


# ===============================================================
# Parser for 'show ip ospf database network detail [vrf <WORD>]'
# ===============================================================
class ShowIpOspfDatabaseNetworkDetail(ShowIpOspfDatabaseNetworkDetailSchema, ShowIpOspfDatabaseDetailParser):
    """Parser for:
        show ip ospf database network detail
        show ip ospf database network detail vrf <vrf>"""
    cli_command = ['show ip ospf database network detail vrf {vrf}', 'show ip ospf database network detail']
    exclude = [
        'age',
        'checksum',
        'seq_num',
        'lsas',
        'links']

    def cli(self, vrf='', output=None):
        # excute command to get output
        if vrf:
            cmd = self.cli_command[0].format(vrf=vrf)
        else:
            cmd = self.cli_command[1]

        return super().cli(cmd=cmd, db_type='network',output=output)


# ==============================================================
# Schema for 'show ip ospf database summary detail [vrf <WORD>]'
# ==============================================================
class ShowIpOspfDatabaseSummaryDetailSchema(MetaParser):

    """Schema for:
        show ip ospf database summary detail
        show ip ospf database summary detail vrf <vrf>"""

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
                                                                    Optional('maxage'): bool,
                                                                    'type': int,
                                                                    'adv_router': str,
                                                                    'seq_num': str,
                                                                    'checksum': str,
                                                                    'length': int},
                                                                'body': 
                                                                    {'summary': 
                                                                        {'network_mask': str,
                                                                        'topologies': 
                                                                            {Any(): 
                                                                                {'mt_id': int,
                                                                                'tos': int,
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


# ===============================================================
# Parser for 'show ip ospf database summary detail [vrf <WORD>]'
# ===============================================================
class ShowIpOspfDatabaseSummaryDetail(ShowIpOspfDatabaseSummaryDetailSchema, ShowIpOspfDatabaseDetailParser):
    """Parser for:
        show ip ospf database summary detail
        show ip ospf database summary detail vrf <vrf>"""

    cli_command = ['show ip ospf database summary detail vrf {vrf}', 'show ip ospf database summary detail']
    exclude = [
        'age',
        'checksum',
        'seq_num',
        'metric',
        'lsas']

    def cli(self, vrf='', output=None):
        # excute command to get output
        if vrf:
            cmd = self.cli_command[0].format(vrf=vrf)
        else:
            cmd = self.cli_command[1]

        return super().cli(cmd=cmd, db_type='summary',output=output)


# =============================================================
# Schema for 'show ip ospf database router detail [vrf <WORD>]'
# =============================================================
class ShowIpOspfDatabaseRouterDetailSchema(MetaParser):
    """Schema for:
        show ip ospf database router detail
        show ip ospf database router detail vrf <vrf>"""

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
                                                                    Optional('maxage'): bool,
                                                                    'type': int,
                                                                    'adv_router': str,
                                                                    'seq_num': str,
                                                                    'checksum': str,
                                                                    'length': int},
                                                                'body': 
                                                                    {'router': 
                                                                        {Optional('flags'): str,
                                                                        'num_of_links': int,
                                                                        'links':
                                                                            {Any(): 
                                                                                {'link_id': str,
                                                                                'link_data': str,
                                                                                'type': str,
                                                                                'num_tos_metrics': int,
                                                                                'topologies': 
                                                                                    {Any(): 
                                                                                        {'mt_id': int,
                                                                                        'metric': int,
                                                                                        'tos': int},
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


# ==============================================================
# Parser for 'show ip ospf database router detail [vrf <WORD>]'
# ==============================================================
class ShowIpOspfDatabaseRouterDetail(ShowIpOspfDatabaseRouterDetailSchema, ShowIpOspfDatabaseDetailParser):
    """Parser for:
        show ip ospf database router detail
        show ip ospf database router detail vrf <vrf>"""

    cli_command = ['show ip ospf database router detail vrf {vrf}', 'show ip ospf database router detail']
    exclude = [
        'age',
        'checksum',
        'seq_num',
        'links',
        'lsas']

    def cli(self, vrf='', output=None):
        # excute command to get output
        if vrf:
            cmd = self.cli_command[0].format(vrf=vrf)
        else:
            cmd = self.cli_command[1]

        return super().cli(cmd=cmd, db_type='router',output=output)


# =============================================================
# Schema for 'show ip ospf database opqaue-area detail [vrf <WORD>]'
# =============================================================
class ShowIpOspfDatabaseOpaqueAreaDetailSchema(MetaParser):
    """Schema for:
        show ip ospf database opaque-area detail
        show ip ospf database opaque-area detail vrf <vrf>"""

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
                                                                    Optional('maxage'): bool,
                                                                    'type': int,
                                                                    'adv_router': str,
                                                                    'seq_num': str,
                                                                    'checksum': str,
                                                                    'length': int,
                                                                    'opaque_type': int,
                                                                    'opaque_id': int,
                                                                    Optional('fragment_number'): int,
                                                                    Optional('mpls_te_router_id'): str,
                                                                    Optional('num_links'): int},
                                                                'body': 
                                                                    {'opaque': 
                                                                        {Optional('link_tlvs'): 
                                                                            {Any(): 
                                                                                {'link_type': int,
                                                                                'link_name': str,
                                                                                'link_id': str,
                                                                                'te_metric': int,
                                                                                'max_bandwidth': int,
                                                                                'max_reservable_bandwidth': int,
                                                                                'admin_group': str,
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


# ==================================================================
# Parser for 'show ip ospf database opaque-area detail [vrf <WORD>]'
# ==================================================================
class ShowIpOspfDatabaseOpaqueAreaDetail(ShowIpOspfDatabaseOpaqueAreaDetailSchema, ShowIpOspfDatabaseDetailParser):
    """Parser for:
        show ip ospf database opaque-area detail
        show ip ospf database opaque-area detail vrf <vrf>"""

    cli_command = ['show ip ospf database opaque-area detail vrf {vrf}', 'show ip ospf database opaque-area detail']
    exclude = [
        'age',
        'checksum',
        'seq_num',
        'lsas',
        'links']

    def cli(self, vrf='', output=None):
        # excute command to get output
        if vrf:
            cmd = self.cli_command[0].format(vrf=vrf)
        else:
            cmd = self.cli_command[1]

        return super().cli(cmd=cmd, db_type='opaque',output=output)
