"""show_vrf.py

IOSXE parsers for the following show commands:
    * 'show vrf'
    * 'show vrf <vrf>'
    * 'show vrf detail'
    * 'show vrf detail <vrf>'
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


class ShowVrfSchema(MetaParser):
    ''' Schema for:
            show vrf
            show vrf {vrf}
    '''
    schema = {
        'vrf': {
            Any(): {
                Optional('route_distinguisher'): str,
                'protocols': list,
                Optional('interfaces'): list
            }
        }
    }


class ShowVrf(ShowVrfSchema):
    ''' Parser for:
            show vrf
            show vrf {vrf}
    '''
    cli_command = ['show vrf', 'show vrf {vrf}']

    def cli(self, vrf='', output=None):
        if vrf:
            cmd = self.cli_command[1].format(vrf=vrf)
        else:
            cmd = self.cli_command[0]

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        res_dict = {}

        # Mgmt-intf                        <not set>             ipv4,ipv6   Gi1
        # VRF1                             65000:1               ipv4,ipv6   Tu1
        # vpn4                           100:2          ipv4,ipv6
        # vpn4                             100:2                 ipv4,ipv6
        # rb-bcn-lab                       10.116.83.34:1        ipv4,ipv6   Lo9
        # test                             10.116.83.34:100      ipv4,ipv6   Lo100
        p1 = re.compile(r'^(?P<vrf>[\w\d\-\.]+)\s+(?P<rd>\<not +set\>|[\.\d\:]+)\s+'
                        r'(?P<protocols>[(?:ipv\d)\,]+)(?:\s+(?P<intf>[\S\s]+))?$')

        # Lo300
        # Gi2.390
        # Gi2.410
        # Te0/0/1
        p2 = re.compile(r'^(?P<intf>[\w\.\/]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Mgmt-intf                        <not set>             ipv4,ipv6   Gi1
            # VRF1                             65000:1               ipv4,ipv6   Tu1
            # vpn2                           100:3          ipv4              Lo23  AT3/0/0.1
            # vpn4                             100:2                 ipv4,ipv6
            # rb-bcn-lab                       10.116.83.34:1        ipv4,ipv6   Lo9
            #                                                                    Te0/0/1
            # test                             10.116.83.34:100      ipv4,ipv6   Lo100
            m = p1.match(line)
            if m:
                groups = m.groupdict()

                vrf = groups['vrf']
                vrf_dict = res_dict.setdefault('vrf', {}).setdefault(vrf, {})

                rd = groups['rd']
                if 'not set' not in rd:
                    vrf_dict.update({'route_distinguisher': rd})

                protocols = groups['protocols'].split(',')
                vrf_dict.update({'protocols': protocols})

                if groups['intf']:
                    intfs = groups['intf'].split()
                    intf_list = [Common.convert_intf_name(item) for item in intfs]
                    vrf_dict.update({'interfaces': intf_list})
                continue

            # Lo300
            # Gi2.390
            # Gi2.410
            # Te0/0/1
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                intf = Common.convert_intf_name(groups['intf'])
                vrf_dict.get('interfaces').append(intf)

        return res_dict


class ShowVrfDetailSchema(MetaParser):
    """Schema for
        * 'show vrf detail'
        * 'show vrf detail <vrf>'
        * 'show ip vrf detail'
        * 'show ip vrf detail <vrf>'"""

    schema = {
        Any(): {
            Optional('vrf_id'):  int,
            Optional('description'):  str,
            Optional('being_deleted'): bool,
            Optional('route_distinguisher'): str,
            Optional('vpn_id'): str,
            Optional('interfaces'): list,
            Optional('interface'): {Any(): {'vrf': str}},
            Optional('flags'):  str,
            Optional('cli_format'): str,
            Optional('support_af'): str,
            Optional('address_family'): {
                Any(): {
                    'table_id': str,
                    Optional('flags'):  str,
                    Optional('vrf_label'): {
                        Optional('distribution_protocol'): str,
                        Optional('allocation_mode'): str,
                        Optional('label'):int
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
                    Optional('import_route_map'): str,
                    Optional('export_route_map'): str,
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
                        }
                    }
                }
            }
        }
    }

class ShowVrfDetailSuperParser(ShowVrfDetailSchema):
    """Super Paser for:
        * show vrf detail
        * show vrf detail <vrf>
        * show ip vrf detail
        * show ip vrf detail <vrf>"""

    def cli(self, output=None):

        # Init vars
        result_dict = {}
        intf_conf = False
        rt_type = None
        af_flag = False

        # VRF VRF1 (VRF Id = 1); default RD 100:1; default VPNID <not set>
        # VRF Mgmt-vrf (VRF Id = 1); default RD <not set>; default VPNID <not set>
        # VRF vrf1; default RD 1:1; default VPNID <not set>
        # VRF Down; default RD 100:1; default VPNID <not set> VRF Table ID = 1
        # VRF 12349; default RD 10.4.1.1:20; default VPNID <not set>
        # VRF DEMO (VRF Id = 12); default RD 65001:1; default VPNID <not set>; being deleted
        p1 = re.compile(r'^VRF +(?P<vrf>[\S]+)( +\(VRF +Id +\= +'
                        r'(?P<vrf_id>\d+)\))?; +default +RD +'
                        r'(?P<rd>[\S\s]+); +default +VPNID +'
                        r'(?P<vpn_id>[\w\s\:\<\>]+)(?: +VRF +'
                        r'Table +ID +\= +(?P<alt_vrf_id>\d))?'
                        r'(?:(?P<being_deleted>; being deleted))?$')

        # New CLI format, supports multiple address-families
        p1_1 = re.compile(r'^(?P<cli_format>(New|Old)) +CLI +format,'
                          r' +supports +(?P<support_af>[\s\S]+)$')

        # Flags: 0x180C
        p2 = re.compile(r'^Flags: +(?P<flags>\w+)$')

        # Interfaces:
        p3 = re.compile(r'^Interfaces:$')

        #     Gi0/0
        p3_1 = re.compile(r'^(?P<intf>[\w\s\/\.\-]+)$')

        # Address family ipv4 unicast (Table ID = 0x1):
        # Address family ipv4 (Table ID = 2 (0x2)):
        p4 = re.compile(r'^Address +family +(?P<af>[\w\s]+) +'
                        r'\(Table +ID +\= +(?P<table_id>\w+)'
                        r'( *[\w\(\)]+)?\)(:|;)?(?: being deleted:)?$')

        # VRF Table ID = 2
        p5 = re.compile(r'^VRF +Table +ID += +(?P<table_id>\d+)$')

        # No Export VPN route-target communities
        # Export VPN route-target communities
        p6 = re.compile(r'^Export VPN route-target communities$')

        # No Import VPN route-target communities
        #Import VPN route-target communities
        p6_1 = re.compile(r'^Import VPN route-target communities$')

        #     RT:100:1                 RT:200:1
        p6_2 = re.compile(r'RT: *(?P<rt>[\w\:\.]+)')

        # No import route-map
        p7 = re.compile(r'^No import route-map$')

        # Import route-map for ipv4 unicast: import_from_global_map (prefix limit: 1000)
        p7_1 = re.compile(r'^Import +route-map +for +(?P<af>[\w\s]+): +'
                          r'(?P<import_map>[\w\-]+) +\(prefix +limit: (?P<limit>\d+)\)$')

        # Import route-map: import-test-map
        p7_2 = re.compile(r'^Import +route-map: +(?P<import_map>[\w\-]+)$')

        # No global export route-map
        # No export route-map
        p8 = re.compile(r'^No( *global)? export route-map$')

        # Global export route-map for ipv4 unicast: export_to_global_map (prefix limit: 1000)
        p8_1 = re.compile(r'^Global +export +route-map +for +(?P<af>[\w\s]+): +'
                          r'(?P<export_map>[\w\-]+) +\(prefix +limit: +(?P<limit>\d+)\)$')

        # Export route-map: export-test-map
        p8_2 = re.compile(r'^Export +route-map: +(?P<export_map>[\w\-]+)$')

        # Route warning limit 10000, current count 0
        # Route limit 10000, warning limit 70% (7000), current count 1
        p9 = re.compile(r'^Route( *limit +(?P<limit>\d+),)? +'
                        r'warning +limit +((?P<warning>\d+)|(?P<percent>\d+)'
                        r'\% *\((?P<warning_limit>[\d\%]+)\)), +'
                        r'current +count +(?P<count>\d+)$')

        # VRF label distribution protocol: not configured
        p10 = re.compile(r'^VRF +label +distribution +protocol: +(?P<vrf_label>[\w\s\-]+)$')

        # VRF label allocation mode: per-prefix
        p11 = re.compile(r'^VRF +label +allocation +mode: +(?P<mode>[\w\s\-]+)'
                         r'(?:\s*\(Label\s*(?P<label>\d+)\))?$')
        
        # Description: desc
        p12 = re.compile(r'^Description: +(?P<desc>[\S\s]+)$')
        
        for line in output.splitlines():
            line = line.strip()

            # VRF VRF1 (VRF Id = 1); default RD 100:1; default VPNID <not set>
            # VRF Mgmt-vrf (VRF Id = 1); default RD <not set>; default VPNID <not set>
            # VRF vrf1; default RD 1:1; default VPNID <not set>
            # VRF Down; default RD 100:1; default VPNID <not set> VRF Table ID = 1
            # VRF 12349; default RD 10.4.1.1:20; default VPNID <not set>
            # VRF DEMO (VRF Id = 12); default RD 65001:1; default VPNID <not set>; being deleted
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                vrf = groups['vrf']

                vrf_dict = result_dict.setdefault(vrf, {})

                if groups['being_deleted']:
                    vrf_dict.update({'being_deleted': True})

                if groups['vrf_id']:
                    vrf_dict.update({'vrf_id': int(groups['vrf_id'])})
                elif groups['alt_vrf_id']:
                    vrf_dict.update({'vrf_id': int(groups['alt_vrf_id'])})

                if 'not' not in groups['rd']:
                    vrf_dict.update({'route_distinguisher': groups['rd']})

                if 'not' not in groups['vpn_id']:
                    vrf_dict.update({'vpn_id': groups['vpn_id']})

                af_flag = False
                continue

            # New CLI format, supports multiple address-families
            m = p1_1.match(line)
            if m:
                groups = m.groupdict()
                vrf_dict.update({'cli_format':groups['cli_format']})
                vrf_dict.update({'support_af':groups['support_af']})
                continue

            # Flags: 0x180C
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                if not af_flag:
                    vrf_dict.update({'flags': groups['flags']})
                else:
                    af_dict = vrf_dict.setdefault('address_family', {}).setdefault(af, {})
                    af_dict.update({'flags': groups['flags']})
                continue

            # Interfaces:
            #     Gi0/0
            m = p3.match(line)
            if m:
                intf_conf = True
                continue

            p3_1 = re.compile(r'^(?P<intf>[\w\s\/\.\-]+)$')
            m = p3_1.match(line)
            if m and intf_conf:
                groups = m.groupdict()
                intfs = groups['intf'].split()
                intf_list = [Common.convert_intf_name(item) for item in intfs]
                if 'interfaces' in result_dict[vrf]:
                    vrf_dict.get('interfaces').extend(intf_list)
                else:
                    vrf_dict.update({'interfaces': intf_list})
                intf_dict = vrf_dict.setdefault('interface', {})
                [intf_dict.setdefault(intf, {}).update({'vrf': vrf}) for intf in intf_list]
                continue

            # Address family ipv4 unicast (Table ID = 0x1):
            # Address family ipv4 (Table ID = 2 (0x2)):
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                intf_conf = False
                af = groups['af'].lower()
                af_dict = vrf_dict.setdefault('address_family', {}).setdefault(af, {})
                af_dict.update({'table_id': groups['table_id']})
                af_flag = True
                continue

            # VRF Table ID = 2
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                intf_conf = False
                try:
                    af
                except Exception:
                    af = 'none'
                af_dict = vrf_dict.setdefault('address_family', {}).setdefault(af, {})
                af_dict.update({'table_id': groups['table_id']})
                af_flag = True
                continue

            # No Export VPN route-target communities
            # Export VPN route-target communities
            m = p6.match(line)
            if m:
                rt_type = 'export'
                rts_dict = af_dict.setdefault('route_targets', {})
                continue

            # No Import VPN route-target communities
            # Import VPN route-target communities
            m = p6_1.match(line)
            if m:
                rt_type = 'import'
                rts_dict = af_dict.setdefault('route_targets', {})
                continue

            #     RT:100:1                 RT:200:1
            m = p6_2.findall(line)
            if m and rt_type:
                for rt in m:
                    rt_dict = rts_dict.setdefault(rt, {})
                    rt_dict.update({'route_target': rt})
                    if 'rt_type' in rt_dict:
                        rt_dict.update({'rt_type': 'both'})
                    else:
                        rt_dict.update({'rt_type': rt_type.strip()})
                continue

            # No import route-map
            m = p7.match(line)
            if m:
                rt_type = None
                continue

            # Import route-map for ipv4 unicast: import_from_global_map (prefix limit: 1000)
            m = p7_1.match(line)
            if m:
                groups = m.groupdict()
                rt_type = None
                import_global_dict = af_dict.setdefault('import_from_global', {})
                import_global_dict.update({'import_from_global_map': groups['import_map']})
                import_global_dict.update({'prefix_limit': int(groups['limit'])})
                continue

            # Import route-map: import-test-map
            m = p7_2.match(line)
            if m:
                groups = m.groupdict()
                rt_type = None
                af_dict.update({'import_route_map': groups['import_map']})
                continue

            # No global export route-map
            # No export route-map
            m = p8.match(line)
            if m:
                rt_type = None
                continue

            # Global export route-map for ipv4 unicast: export_to_global_map (prefix limit: 1000)
            m = p8_1.match(line)
            if m:
                groups = m.groupdict()
                rt_type = None
                export_global_dict = af_dict.setdefault('export_to_global', {})
                export_global_dict.update({'export_to_global_map': groups['export_map']})
                export_global_dict.update({'prefix_limit': int(groups['limit'])})
                continue

            # Export route-map: export-test-map
            m = p8_2.match(line)
            if m:
                groups = m.groupdict()
                rt_type = None
                af_dict.update({'export_route_map': groups['export_map']})
                continue

            # Route warning limit 10000, current count 0
            # Route limit 10000, warning limit 70% (7000), current count 1
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                routing_table_limit_number = groups['limit']
                alert_value = groups['warning']
                alert_percent_value = groups['percent']
                alert_percent_warning = groups['warning_limit']
                count = int(groups['count'])

                rt_limit_dict = af_dict.setdefault('routing_table_limit', {})

                if routing_table_limit_number:
                    rt_limit_dict.update({'routing_table_limit_number': int(routing_table_limit_number)})

                rt_limit_action_dict = rt_limit_dict.setdefault('routing_table_limit_action', {})

                if alert_percent_value:
                    alert_percent_dict = rt_limit_action_dict.setdefault('enable_alert_percent', {})
                    alert_percent_dict.update({'alert_percent_value': int(alert_percent_value)})

                    if alert_percent_warning:
                        alert_limit_dict = rt_limit_action_dict.setdefault('enable_alert_limit_number', {})
                        alert_limit_dict.update({'alert_limit_number': int(alert_percent_warning)})

                if alert_value:
                    alert_limit_dict = rt_limit_action_dict.setdefault('enable_alert_limit_number', {})
                    alert_limit_dict.update({'alert_limit_number': int(alert_value)})
                continue

            # VRF label distribution protocol: not configured
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                if 'not' not in groups['vrf_label']:
                    vrf_label_dict = af_dict.setdefault('vrf_label', {})
                    vrf_label_dict.update({'distribution_protocol': groups['vrf_label']})
                continue

            # VRF label allocation mode: per-prefix
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                if 'not' not in groups['mode']:
                    vrf_label_dict = af_dict.setdefault('vrf_label', {})
                    vrf_label_dict.update({'allocation_mode': groups['mode'].strip()})
                    if groups['label']:
                        vrf_label_dict.update({'label': int(groups['label'])})
                continue

            # Description: desc
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                vrf_dict.update({'description': groups['desc']})
                continue
        return result_dict


class ShowVrfDetail(ShowVrfDetailSuperParser):
    """Parser for 
        * 'show vrf detail'
        * 'show vrf detail <vrf>'"""
    cli_command = ['show vrf detail' , 'show vrf detail {vrf}']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)

        else:
            out = output

        return super().cli(output=out)
# vim: ft=python et sw=4
