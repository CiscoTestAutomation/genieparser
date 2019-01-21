"""show_vrf.py

IOSXE parsers for the following show commands:
    * 'show vrf detail'
"""

# Python
import re
import xmltodict

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowVrfDetailSchema(MetaParser):
    """Schema for show vrf detail"""

    schema = {Any():
                {
                 Optional('vrf_id'):  int,
                 Optional('route_distinguisher'): str,
                 Optional('vpn_id'): str,
                 Optional('interfaces'):  list,
                 Optional('interface'):  {Any(): {'vrf': str}},
                 Optional('flags'):  str,
                 Optional('address_family'): {
                    Any(): {
                        'table_id': str,
                         Optional('flags'):  str,
                        Optional('vrf_label'): {
                            Optional('distribution_protocol'): str,
                            Optional('allocation_mode'): str
                        },
                        Optional('route_targets'): {
                            Any(): {
                                'route_target': str,
                                'rt_type': str,
                            },
                        },
                        Optional('import_from_global'): {
                            'import_from_global_map': str,
                            'prefix_limit': int
                        },
                        Optional('export_to_global'): {
                            'export_to_global_map': str,
                            'prefix_limit': int
                        },
                        Optional('routing_table_limit'): {
                            Optional('routing_table_limit_number'): int,
                            'routing_table_limit_action': {
                                Optional('enable_alert_percent'): {
                                    'alert_percent_value': int,
                                },
                                Optional('enable_alert_limit_number'): {
                                    'alert_limit_number': int,
                                },
                                Optional('enable_simple_alert'): {
                                    'simple_alert': bool,
                                }
                            },
                        },
                    },
                }
            },
        }

class ShowVrfDetail(ShowVrfDetailSchema):
    """Parser for show vrf detail"""
    cli_command = 'show vrf detail'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # Init vars
        vrf_dict = {}
        af_dict = {}
        intf_conf = False
        rt_type = None
        af_flag = False

        for line in out.splitlines():
            line = line.strip()

            # VRF VRF1 (VRF Id = 1); default RD 100:1; default VPNID <not set>
            # VRF Mgmt-vrf (VRF Id = 1); default RD <not set>; default VPNID <not set>
            # VRF vrf1; default RD 1:1; default VPNID <not set>
            p1 = re.compile(r'^VRF +(?P<vrf>[\w\-]+)( +'
                             '\(VRF +Id +\= +(?P<vrf_id>\d+)\))?; +'
                             'default +RD +(?P<rd>[\w\s\:\<\>]+); +'
                             'default +VPNID +(?P<vpn_id>[\w\s\:\<\>]+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                if vrf not in vrf_dict:
                    vrf_dict[vrf] = {}
                if m.groupdict()['vrf_id']:
                    vrf_dict[vrf]['vrf_id'] = int(m.groupdict()['vrf_id'])
                if 'not' not in m.groupdict()['rd']:
                    vrf_dict[vrf]['route_distinguisher'] = m.groupdict()['rd']
                if 'not' not in m.groupdict()['vpn_id']:
                    vrf_dict[vrf]['vpn_id'] = m.groupdict()['vpn_id']
                af_flag = False

                continue

            # New CLI format, supports multiple address-families

            # Flags: 0x180C
            p2 = re.compile(r'^Flags: +(?P<flags>\w+)$')
            m = p2.match(line)
            if m:
                if not af_flag:
                    vrf_dict[vrf]['flags'] = m.groupdict()['flags']
                else:
                    vrf_dict[vrf]["address_family"][af]['flags'] = \
                        m.groupdict()['flags']
                continue

            # Interfaces:
            #     Gi0/0
            p3 = re.compile(r'^Interfaces:$')
            m = p3.match(line)
            if m:
                intf_conf = True
                continue

            p3_1 = re.compile(r'^(?P<intf>[\w\s\/\.\-]+)$')
            m = p3_1.match(line)
            if m and intf_conf:
                intfs = m.groupdict()['intf'].split()
                intf_list = [Common.convert_intf_name(item) for item in intfs]
                vrf_dict[vrf]['interfaces'] = intf_list
                intf_dict = vrf_dict[vrf].setdefault('interface', {})
                [intf_dict.setdefault(intf, {}).update({'vrf':vrf}) for intf in intf_list]
                intf_conf = False
                continue

            # Address family ipv4 unicast (Table ID = 0x1):
            # Address family ipv4 (Table ID = 2 (0x2)):
            p4 = re.compile(r'^Address +family +(?P<af>[\w\s]+) +'
                             '\(Table +ID +\= +(?P<table_id>\w+)( *[\w\(\)]+)?\):$')
            m = p4.match(line)
            if m:
                af = m.groupdict()['af'].lower()
                if 'address_family' not in vrf_dict[vrf]:
                    vrf_dict[vrf]['address_family'] = {}
                if af not in vrf_dict[vrf]['address_family']:
                    vrf_dict[vrf]['address_family'][af] = {}

                af_dict = vrf_dict[vrf]['address_family'][af]

                af_dict['table_id'] = m.groupdict()['table_id']
                af_flag = True
                continue

            # No Export VPN route-target communities
            # Export VPN route-target communities
            p6 = re.compile(r'^Export VPN route-target communities$')
            m = p6.match(line)
            if m:
                rt_type = 'export'
                if 'route_targets' not in af_dict:
                    af_dict['route_targets'] = {}
                continue

            # No Import VPN route-target communities
            #Import VPN route-target communities
            p6_1 = re.compile(r'^Import VPN route-target communities$')
            m = p6_1.match(line)
            if m:
                rt_type = 'import'
                if 'route_targets' not in af_dict:
                    af_dict['route_targets'] = {}
                continue

            #     RT:100:1                 RT:200:1
            p6_1 = re.compile(r'RT: *(?P<rt>[\w\:\.]+)')
            m = p6_1.findall(line)
            if m and rt_type:
                for rt in m:
                    if rt not in af_dict['route_targets']:
                        af_dict['route_targets'][rt] = {}
                    af_dict['route_targets'][rt]['route_target'] = rt
                    if 'rt_type' in af_dict['route_targets'][rt]:
                        af_dict['route_targets'][rt]['rt_type'] = 'both'
                    else:
                        af_dict['route_targets'][rt]['rt_type'] = rt_type.strip()
                continue

            # No import route-map
            p7 = re.compile(r'^No import route-map$')
            m = p7.match(line)
            if m:
                rt_type = None
                continue

            # Import route-map for ipv4 unicast: import_from_global_map (prefix limit: 1000)
            p7_1 = re.compile(r'^Import +route-map +for +(?P<af>[\w\s]+): +'
                               '(?P<import_map>[\w\-]+) +\(prefix +limit: (?P<limit>\d+)\)$')
            m = p7_1.match(line)
            if m:
                rt_type = None
                if 'import_from_global' not in af_dict:
                    af_dict['import_from_global'] = {}
                af_dict['import_from_global']['import_from_global_map'] = m.groupdict()['import_map']
                af_dict['import_from_global']['prefix_limit'] = int(m.groupdict()['limit'])
                continue


            # No global export route-map
            # No export route-map
            p8 = re.compile(r'^No( *global)? export route-map$')
            m = p8.match(line)
            if m:
                rt_type = None
                continue

            # Global export route-map for ipv4 unicast: export_to_global_map (prefix limit: 1000)
            p8_1 = re.compile(r'^Global +export +route-map +for +(?P<af>[\w\s]+): +'
                               '(?P<import_map>[\w\-]+) +\(prefix +limit: +(?P<limit>\d+)\)$')
            m = p8_1.match(line)
            if m:
                rt_type = None
                if 'export_to_global' not in af_dict:
                    af_dict['export_to_global'] = {}
                af_dict['export_to_global']['export_to_global_map'] = m.groupdict()['import_map']
                af_dict['export_to_global']['prefix_limit'] = int(m.groupdict()['limit'])
                continue


            # Route warning limit 10000, current count 0
            # Route limit 10000, warning limit 70% (7000), current count 1
            p9 = re.compile(r'^Route( *limit +(?P<limit>\d+),)? +'
                             'warning +limit +((?P<warning>\d+)|(?P<percent>\d+)\% *\((?P<warning_limit>[\d\%]+)\)), +'
                             'current +count +(?P<count>\d+)$')
            m = p9.match(line)
            if m:
                routing_table_limit_number = m.groupdict()['limit']
                alert_value = m.groupdict()['warning']
                alert_percent_value = m.groupdict()['percent']
                alert_percent_warning = m.groupdict()['warning_limit']
                count = int(m.groupdict()['count'])

                if 'routing_table_limit' not in af_dict:
                    af_dict['routing_table_limit'] = {}

                if routing_table_limit_number:
                    af_dict['routing_table_limit']['routing_table_limit_number'] = \
                        int(routing_table_limit_number)

                if 'routing_table_limit_action' not in af_dict['routing_table_limit']:
                    af_dict['routing_table_limit']['routing_table_limit_action'] = {}

                if alert_percent_value:

                    if 'enable_alert_percent' not in af_dict['routing_table_limit']\
                        ['routing_table_limit_action']:
                        af_dict['routing_table_limit']['routing_table_limit_action']\
                            ['enable_alert_percent'] = {}
                            
                    af_dict['routing_table_limit']['routing_table_limit_action']\
                            ['enable_alert_percent']['alert_percent_value'] = int(alert_percent_value)

                    if alert_percent_warning:
                        if 'enable_alert_limit_number' not in af_dict['routing_table_limit']\
                            ['routing_table_limit_action']:
                            af_dict['routing_table_limit']['routing_table_limit_action']\
                                ['enable_alert_limit_number'] = {}
                        af_dict['routing_table_limit']['routing_table_limit_action']\
                            ['enable_alert_limit_number']['alert_limit_number'] = int(alert_percent_warning)

                if alert_value:
                    if 'enable_alert_limit_number' not in af_dict['routing_table_limit']\
                        ['routing_table_limit_action']:
                        af_dict['routing_table_limit']['routing_table_limit_action']\
                            ['enable_alert_limit_number'] = {}

                    af_dict['routing_table_limit']['routing_table_limit_action']\
                            ['enable_alert_limit_number']['alert_limit_number'] = int(alert_value)

                continue


            # VRF label distribution protocol: not configured
            p10 = re.compile(r'^VRF +label +distribution +protocol: +(?P<vrf_label>[\w\s\-]+)\)$')
            m = p10.match(line)
            if m:
                if 'not' not in m.groupdict()['vrf_label']:
                    if 'vrf_label' not in af_dict:
                        af_dict['vrf_label'] = {}
                    af_dict['vrf_label']['distribution_protocol'] = m.groupdict()['vrf_label']
                continue

            # VRF label allocation mode: per-prefix
            p11 = re.compile(r'^VRF +label +allocation +mode: +(?P<mode>[\w\s\-]+)$')
            m = p11.match(line)
            if m:
                if 'not' not in m.groupdict()['mode']:
                    if 'vrf_label' not in af_dict:
                        af_dict['vrf_label'] = {}
                    af_dict['vrf_label']['allocation_mode'] = m.groupdict()['mode']
                continue           

        return vrf_dict

# vim: ft=python et sw=4
