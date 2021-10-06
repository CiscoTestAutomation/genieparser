""" show_isis.py

NXOS parsers for the following show commands:
    * show isis
    * show isis vrf {vrf}
    * show isis interface
    * show isis interface vrf {vrf}
    * show isis spf-log detail
    * show isis spf-log detail vrf {vrf}
    * show isis adjacency
    * show isis adjacency vrf {vrf}
    * show isis hostname
    * show isis hostname vrf {vrf}
    * show isis hostname detail
    * show isis hostname detail vrf {vrf}
    * show isis database detail
    * show isis database detail vrf {vrf}
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional
from genie.libs.parser.utils.common import Common


class ShowIsisSchema(MetaParser):
    """Schema for show isis"""

    schema = {
        'instance': {
            Any(): {
                'isis_process': str,
                'instance_number': int,
                'uuid': str,
                'process_id': int,
                'vrf': {
                    Any(): {
                        'vrf': str,
                        'system_id': str,
                        'is_type': str,
                        'sap': int,
                        'queue_handle': int,
                        'maximum_lsp_mtu': int,
                        'stateful_ha': str,
                        'graceful_restart': {
                            'enable': bool,
                            'state': str,
                            'last_gr_status': str,
                        },
                        'start_mode': str,
                        'bfd_ipv4': str,
                        'bfd_ipv6': str,
                        'topology_mode': str,
                        'metric_type': {
                            'advertise': list,
                            'accept': list,
                        },
                        'area_address': list,
                        'process': str,
                        'vrf_id': int,
                        'during_non_graceful_controlled_restart': str,
                        'resolution_of_l3_to_l2': str,
                        'sr_ipv4': str,
                        'sr_ipv6': str,
                        'supported_interfaces': list,
                        'topology': {
                            Any(): {
                                'address_family': {
                                    Optional('ipv4_unicast'): {
                                        'number_of_interface': int,
                                        'distance': int,
                                    },
                                    Optional('ipv6_unicast'): {
                                        'number_of_interface': int,
                                        'distance': int,
                                    },
                                },
                            },
                        },
                        'authentication': {
                            'level_1': {
                                Optional('authentication_type'): dict,
                                'auth_check': str,
                            },
                            'level_2': {
                                Optional('authentication_type'): dict,
                                'auth_check': str,
                            },
                        },
                        'l1_next_spf': str,
                        'l2_next_spf': str,
                    },
                },
            },
        },
    }


class ShowIsis(ShowIsisSchema):
    """Parser for show isis"""

    cli_command = ['show isis', 
                   'show isis vrf {vrf}']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]

            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        result_dict = {}

        # ISIS process : test
        p1 = re.compile(r'^ISIS +[Pp]rocess *: +(?P<isis_process>\S+)$')

        # Instance number :  1
        p2 = re.compile(r'^Instance +number *: +(?P<instance_number>\d+)$')

        # UUID: 1090519320
        p3 = re.compile(r'^UUID *: +(?P<uuid>\d+)$')

        # Process ID 1581
        p4 = re.compile(r'^Process +ID +(?P<process_id>\d+)$')

        # VRF: default
        p5 = re.compile(r'^VRF *: +(?P<vrf>\S+)$')

        # System ID : 3333.33ff.6666  IS-Type : L1-L2
        p6 = re.compile(r'^System +ID *: +(?P<sysid>[a-zA-Z\d\-\.]+) +IS-Type *: +(?P<is_type>\S+)$')

        # SAP : 412  Queue Handle : 15
        p7 = re.compile(r'^SAP *: +(?P<sap>\d+) +Queue +Handle *: +(?P<queue_handle>\d+)$')

        # Maximum LSP MTU: 1492
        p8 = re.compile(r'^Maximum +LSP +MTU *: +(?P<lsp_mtu>\d+)$')

        # Stateful HA enabled
        p9 = re.compile(r'^Stateful +HA +(?P<stateful_ha>\w+)$')

        # Graceful Restart enabled. State: Inactive
        p10 = re.compile(r'^Graceful +Restart +(?P<gr>\w+)\. +State *: +(?P<state>\w+)$')

        # Last graceful restart status : none
        p11 = re.compile(r'^Last +graceful +restart +status *: +(?P<last_gr_status>\w+)$')

        # Start-Mode Complete
        p12 = re.compile(r'^Start-Mode +(?P<start_mode>\w+)$')

        # BFD IPv4 is globally disabled for ISIS process: test
        p13 = re.compile(r'^BFD +IPv4 +is +(?P<bfd_ipv4>[\w\s]+) +for +ISIS +process: +(?P<name>.*)$')

        # BFD IPv6 is globally disabled for ISIS process: test
        p14 = re.compile(r'^BFD +IPv6 +is +(?P<bfd_ipv6>[\w\s]+) +for +ISIS +process: +(?P<name>.*)$')

        # Topology-mode is Multitopology
        p15 = re.compile(r'^Topology-mode +is +(?P<topology_mode>\w+)$')

        # Metric-style : advertise(wide), accept(narrow, wide)
        p16 = re.compile(r'^Metric-style *: +advertise\((?P<adv>.*)\), +accept\((?P<acc>.*)\)$')

        # Area address(es) :
        #     49.0001
        p17 = re.compile(r'^(?P<area>[\d\.]+)$')

        # Process is up and running
        p18 = re.compile(r'^Process +is +(?P<process>[\S\s]+)$')

        # VRF ID: 1
        p19 = re.compile(r'^VRF +ID *: +(?P<vrf_id>\d+)$')

        # Stale routes during non-graceful controlled restart
        # Flush Routes during non-graceful controlled restart
        p20 = re.compile(r'^(?P<route>[\w\s]+) +during +non-graceful +controlled +restart$')

        # Enable resolution of L3->L2 address for ISIS adjacency
        # Disable resolution of L3->L2 address for ISIS adjacency
        p21 = re.compile(r'^(?P<resolution>\w+) +resolution +of +L3->L2 +address +for +ISIS +adjacency$')

        # SR IPv4 is not configured and disabled for ISIS process: test
        p22 = re.compile(r'^SR +IPv4 +is +(?P<sr_ipv4>[\w\s]+) +for +ISIS +process: +(?P<name>.*)$')

        # SR IPv6 is not configured and disabled for ISIS process: test
        p23 = re.compile(r'^SR +IPv6 +is +(?P<sr_ipv6>[\w\s]+) +for +ISIS +process: +(?P<name>.*)$')

        # Interfaces supported by IS-IS :
        #     loopback0
        p24 = re.compile(r'^(?!Level)(?P<interface>[a-zA-Z][\S]+)$')

        # Topology : 0
        p25 = re.compile(r'^Topology *: +(?P<topology>\d+)$')

        # Address family IPv4 unicast :
        # Address family IPv6 unicast :
        p26 = re.compile(r'^Address +family +(?P<af>[\S\s]+?) *:$')

        #     Number of interface : 3
        p27 = re.compile(r'^Number +of +interface *: +(?P<num>\d+)$')

        #     Distance : 115
        p28 = re.compile(r'^Distance *: +(?P<distance>\d+)$')

        # Level1
        p29 = re.compile(r'^Level *(?P<level>\d+)$')

        # No auth type and keychain
        p30 = re.compile(r'^No auth type and keychain$')

        # Auth check set
        p31 = re.compile(r'^Auth +check +(?P<auth_check>\w+)$')

        # L1 Next SPF: 00:00:07
        p32 = re.compile(r'^L1 +Next +SPF *: +(?P<l1_next_spf>\S+)$')

        # L2 Next SPF: 00:00:04
        p33 = re.compile(r'^L2 +Next +SPF *: +(?P<l2_next_spf>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # ISIS process : test
            m = p1.match(line)
            if m:
                group = m.groupdict()
                isis_process = group['isis_process']
                pid_dict = result_dict.setdefault('instance', {}).setdefault(isis_process, {})
                pid_dict.update({'isis_process': isis_process})
                continue

            #  Instance number :  1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                instance_number = int(group['instance_number'])
                pid_dict.update({'instance_number': instance_number})
                continue

            #  UUID: 1090519320
            m = p3.match(line)
            if m:
                group = m.groupdict()
                uuid = group['uuid']
                pid_dict.update({'uuid': uuid})
                continue

            #  Process ID 1569
            m = p4.match(line)
            if m:
                group = m.groupdict()
                process_id = int(group['process_id'])
                pid_dict.update({'process_id': process_id})            
                continue

            # VRF: VRF1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                vrf = group['vrf']
                vrf_dict = pid_dict.setdefault('vrf', {}).setdefault(vrf, {})
                vrf_dict.update({'vrf': vrf})
                continue

            #   System ID : 3333.33ff.6666  IS-Type : L1-L2
            m = p6.match(line)
            if m:
                group = m.groupdict()
                sysid = group['sysid']
                is_type = group['is_type']
                vrf_dict.update({'system_id': sysid, 'is_type': is_type})
                continue

            #   SAP : 412  Queue Handle : 15
            m = p7.match(line)
            if m:
                group = m.groupdict()
                sap = int(group['sap'])
                queue_handle = int(group['queue_handle'])
                vrf_dict.update({'sap': sap, 'queue_handle': queue_handle})
                continue

            #   Maximum LSP MTU: 1492
            m = p8.match(line)
            if m:
                group = m.groupdict()
                lsp_mtu = int(group['lsp_mtu'])
                vrf_dict.update({'maximum_lsp_mtu': lsp_mtu})
                continue

            #   Stateful HA enabled
            m = p9.match(line)
            if m:
                group = m.groupdict()
                stateful_ha = group['stateful_ha']
                vrf_dict.update({'stateful_ha': stateful_ha})
                continue

            #   Graceful Restart enabled. State: Inactive
            m = p10.match(line)
            if m:
                group = m.groupdict()
                gr = group['gr']
                state = group['state']

                gr_dict = vrf_dict.setdefault('graceful_restart', {})
                if gr.lower() == 'enabled':
                    gr_dict.update({'enable': True})
                else:
                    gr_dict.update({'enable': False})

                gr_dict.update({'state': state})
                continue

            #   Last graceful restart status : none
            m = p11.match(line)
            if m:
                group = m.groupdict()
                last_gr_status = group['last_gr_status']
                gr_dict = vrf_dict.setdefault('graceful_restart', {})
                gr_dict.update({'last_gr_status': last_gr_status})
                continue

            #   Start-Mode Complete
            m = p12.match(line)
            if m:
                group = m.groupdict()
                start_mode = group['start_mode']
                vrf_dict.update({'start_mode': start_mode})
                continue

            #   BFD IPv4 is globally disabled for ISIS process: test
            m = p13.match(line)
            if m:
                group = m.groupdict()
                bfd_ipv4 = group['bfd_ipv4']
                vrf_dict.update({'bfd_ipv4': bfd_ipv4})
                continue

            #   BFD IPv6 is globally disabled for ISIS process: test
            m = p14.match(line)
            if m:
                group = m.groupdict()
                bfd_ipv6 = group['bfd_ipv6']
                vrf_dict.update({'bfd_ipv6': bfd_ipv6})
                continue

            #   Topology-mode is Multitopology
            m = p15.match(line)
            if m:
                group = m.groupdict()
                topology_mode = group['topology_mode']
                vrf_dict.update({'topology_mode': topology_mode})
                continue

            #   Metric-style : advertise(wide), accept(narrow, wide)
            m = p16.match(line)
            if m:
                group = m.groupdict()
                advertise = group['adv'].replace(' ', '').split(',')
                accept = group['acc'].replace(' ', '').split(',')

                metric_dict = vrf_dict.setdefault('metric_type', {})
                metric_dict.update({'advertise': advertise, 
                                    'accept': accept})
                continue

            #   Area address(es) :
            #     49.0001
            m = p17.match(line)
            if m:
                group = m.groupdict()
                area = group['area']
                area_address = vrf_dict.setdefault('area_address', [])
                area_address.append(area)
                continue

            #   Process is up and running
            m = p18.match(line)
            if m:
                group = m.groupdict()
                process = group['process']
                vrf_dict.update({'process': process})
                continue

            #   VRF ID: 3
            m = p19.match(line)
            if m:
                group = m.groupdict()
                vrf_id = int(group['vrf_id'])
                vrf_dict.update({'vrf_id': vrf_id})
                continue

            #   Stale routes during non-graceful controlled restart
            m = p20.match(line)
            if m:
                group = m.groupdict()
                route = group['route']
                vrf_dict.update({'during_non_graceful_controlled_restart': route})
                continue

            #   Enable resolution of L3->L2 address for ISIS adjacency
            m = p21.match(line)
            if m:
                group = m.groupdict()
                res = group['resolution']
                vrf_dict.update({'resolution_of_l3_to_l2': res})
                continue

            #   SR IPv4 is not configured and disabled for ISIS process: test
            m = p22.match(line)
            if m:
                group = m.groupdict()
                sr_ipv4 = group['sr_ipv4']
                vrf_dict.update({'sr_ipv4': sr_ipv4})
                continue

            #   SR IPv6 is not configured and disabled for ISIS process: test
            m = p23.match(line)
            if m:
                group = m.groupdict()
                sr_ipv6 = group['sr_ipv6']
                vrf_dict.update({'sr_ipv6': sr_ipv6})
                continue
            
            #   Interfaces supported by IS-IS :
            #     loopback300
            m = p24.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group['interface'])
                intf_list = vrf_dict.setdefault('supported_interfaces', [])
                intf_list.append(interface)
                continue

            #   Topology : 0
            m = p25.match(line)
            if m:
                group = m.groupdict()
                topology = int(group['topology'])
                topo_dict = vrf_dict.setdefault('topology', {}).setdefault(topology, {})
                continue

            #   Address family IPv4 unicast :
            m = p26.match(line)
            if m:
                group = m.groupdict()
                af = group['af'].replace(' ', '_').lower()
                af_dict = topo_dict.setdefault('address_family', {}).setdefault(af, {})
                continue

            #     Number of interface : 3
            m = p27.match(line)
            if m:
                group = m.groupdict()
                num = int(group['num'])
                af_dict.update({'number_of_interface': num})
                continue

            #     Distance : 115
            m = p28.match(line)
            if m:
                group = m.groupdict()
                distance = int(group['distance'])
                af_dict.update({'distance': distance})
                continue

            #   Level1
            m = p29.match(line)
            if m:
                group = m.groupdict()
                level = 'level_{}'.format(group['level'])
                level_dict = vrf_dict.setdefault('authentication', {}).setdefault(level, {})
                continue

            #   No auth type and keychain
            m = p30.match(line)
            if m:
                group = m.groupdict()
                continue

            #   Auth check set
            m = p31.match(line)
            if m:
                group = m.groupdict()
                auth_check = group['auth_check']
                level_dict.update({'auth_check': auth_check})
                continue

            #   L1 Next SPF: 00:00:02
            m = p32.match(line)
            if m:
                group = m.groupdict()
                l1_next_spf = group['l1_next_spf']
                vrf_dict.update({'l1_next_spf': l1_next_spf})
                continue

            #   L2 Next SPF: 0.123488
            m = p33.match(line)
            if m:
                group = m.groupdict()
                l2_next_spf = group['l2_next_spf']
                vrf_dict.update({'l2_next_spf': l2_next_spf})
                continue

        return result_dict


class ShowIsisInterfaceSchema(MetaParser):
    """Schema for show isis interface"""

    schema = {
        'instance': {
            Any(): { # process_id
                'vrf': {
                    Any(): {
                        'interfaces': {
                            Any(): {
                                'name': str,
                                'status': str,
                                Optional('ipv4'): str,
                                Optional('ipv4_subnet'): str,
                                Optional('ipv6'): {
                                    Any(): {
                                        'state': str,
                                    }
                                },
                                Optional('ipv6_subnet'): str,
                                Optional('ipv6_link_local_address'): str,
                                Optional('authentication'): {
                                    Any(): { # level_1 level_2
                                        Optional('authentication_type'): {
                                        },
                                        Optional('auth_check'): str,
                                    },
                                },
                                'index': str,
                                'local_circuit_id': str,
                                'circuit_type': str,
                                'bfd_ipv4': str,
                                'bfd_ipv6': str,
                                'mtr': str,
                                Optional('passive'): str,
                                Optional('mtu'): int,
                                Optional('lsp_interval_ms'): int,
                                'levels': {
                                    Any(): { # 1, 2
                                        Optional('metric'): str,
                                        Optional('designated_is'): str,
                                        Optional('metric_0'): str,
                                        Optional('metric_2'): str,
                                        Optional('csnp'): str,
                                        Optional('next_csnp'): str,
                                        Optional('hello'): str,
                                        Optional('multi'): str,
                                        Optional('next_iih'): str,
                                        Optional('adjs'): str,
                                        Optional('adjs_up'): str,
                                        Optional('pri'): str,
                                        Optional('circuit_id'): str,
                                        Optional('since'): str,
                                    },
                                },
                                'topologies': {
                                    Any(): { # mt
                                        'level': {
                                            Any(): { # 1, 2
                                                'metric': str,
                                                'metric_cfg': str,
                                                'fwdng': str,
                                                'ipv4_mt': str,
                                                'ipv4_cfg': str,
                                                'ipv6_mt': str,
                                                'ipv6_cfg': str,
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


class ShowIsisInterface(ShowIsisInterfaceSchema):
    """Parser for show isis interface"""

    cli_command = ['show isis interface', 
                   'show isis interface vrf {vrf}']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]

            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        result_dict = {}

        # IS-IS process: test VRF: default
        p1 = re.compile(r'^IS-IS +[Pp]rocess: +(?P<process_id>\S+) +VRF: +(?P<vrf>\S+)$')

        # loopback0, Interface status: protocol-up/link-up/admin-up
        p2 = re.compile(r'^(?P<interface>\S+), +Interface +status: +(?P<status>\S+)$')

        #   IP address: 10.36.3.3, IP subnet: 10.36.3.3/32
        p3 = re.compile(r'^IP +address: +(?P<ip>\S+), +IP +subnet: +(?P<subnet>\S+)$')

        #   IPv6 address:
        #     2001:3:3:3::3/128 [VALID]
        p4 = re.compile(r'^(?P<ipv6>\S+) +\[(?P<state>\S+)\]$')

        #   IPv6 subnet:  2001:3:3:3::3/128
        p5 = re.compile(r'^IPv6 +subnet: +(?P<subnet>\S+)$')

        #   IPv6 link-local address: fe80::5c00:80ff:fe02:0
        p6 = re.compile(r'^IPv6 +link-local +address: +(?P<link_address>\S+)$')

        #   Level1
        p7 = re.compile(r'^Level *(?P<level>\d+)$')

        #     No auth type and keychain
        p8 = re.compile(r'^No auth type and keychain$')

        #     Auth check set
        p9 = re.compile(r'^Auth +check +(?P<auth_check>\w+)$')

        #   Index: 0x0001, Local Circuit ID: 0x01, Circuit Type: L1-2
        p10 = re.compile(r'^Index: +(?P<index>\w+), +Local +Circuit +ID: '
                         r'+(?P<circuit_id>\w+), +Circuit +Type: +(?P<circuit_type>\S+)$')

        #   BFD IPv4 is locally disabled for Interface loopback0
        p11 = re.compile(r'^BFD +IPv4 +is +(?P<bfd_ipv4>[\s\w]+) +for +Interface +(?P<intf>.*)$')

        #   BFD IPv6 is locally disabled for Interface loopback0
        p12 = re.compile(r'^BFD +IPv6 +is +(?P<bfd_ipv6>[\s\w]+) +for +Interface +(?P<intf>.*)$')
        
        #   MTR is enabled
        p13 = re.compile(r'^MTR +is +(?P<mtr>\w+)$')

        #   Passive level: level-1-2
        p13_1 = re.compile(r'^Passive +level: +(?P<passive>\S+)$')

        #   Level      Metric
        #   1               1
        p14 = re.compile(r'^(?P<level>\d+) +(?P<metric>\d+)$')

        #   LSP interval: 33 ms, MTU: 1500
        p15 = re.compile(r'^LSP +interval: +(?P<lsp_interval>[\d]+) +ms, +MTU: +(?P<mtu>\d+)$')
        
        #   Level-1 Designated IS: R2_xr
        #   Level-2 Designated IS: R2_xr
        p16 = re.compile(r'^(?P<level>\S+) +Designated +IS: +(?P<designated_is>\S+)$')

        #   Level   Metric-0   Metric-2   CSNP  Next CSNP  Hello   Multi   Next IIH
        #   1              40     40     10 Inactive      10   3       00:00:04
        #   2              40     40     10 00:00:03      10   3       00:00:09
        p17 = re.compile(r'^(?P<level>\d+) +(?P<metric_0>\d+) +(?P<metric_2>\d+) '
                         r'+(?P<csnp>\d+) +(?P<next_csnp>[\w\:]+) +(?P<hello>\d+) '
                         r'+(?P<multi>\d+) +(?P<next_iih>[\w\:]+)$')

        #   Level  Adjs   AdjsUp Pri  Circuit ID         Since
        #   1         1        1  64  R2_xr.03           5d01h
        #   2         1        1  64  R2_xr.03           5d01h
        p18 = re.compile(r'^(?P<level>\d+) +(?P<adjs>\d+) +(?P<adjs_up>\d+) '
                         r'+(?P<pri>\d+) +(?P<circuit_id>\S+) +(?P<since>\w+)$')

        #   Topologies enabled:
        #     L  MT  Metric  MetricCfg  Fwdng IPV4-MT  IPV4Cfg  IPV6-MT  IPV6Cfg
        #     1  0        1       no   UP    UP       yes      DN       yes
        p19 = re.compile(r'^(?P<level>\d+) +(?P<mt>\d+) +(?P<metric>\d+) '
                         r'+(?P<metric_cfg>\w+) +(?P<fwdng>\w+) +(?P<ipv4_mt>\w+) '
                         r'+(?P<ipv4_cfg>\w+) +(?P<ipv6_mt>\w+) +(?P<ipv6_cfg>\w+)$')

        for line in out.splitlines():
            line = line.strip()

            # IS-IS process: test VRF: default
            m = p1.match(line)
            if m:
                group = m.groupdict()
                process_id = group['process_id']
                vrf = group['vrf']

                vrf_dict = result_dict.setdefault('instance', {}).\
                                       setdefault(process_id, {}).\
                                       setdefault('vrf', {}).\
                                       setdefault(vrf, {})
                continue

            # Ethernet1/2.115, Interface status: protocol-up/link-up/admin-up
            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                status = group['status']
                intf_dict = vrf_dict.setdefault('interfaces', {}).setdefault(interface, {})
                intf_dict.update({'name': interface, 'status': status})
                continue

            #  IP address: 10.36.3.3, IP subnet: 10.36.3.3/32
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ip = group['ip']
                subnet = group['subnet']
                intf_dict.update({'ipv4': ip, 'ipv4_subnet': subnet})
                continue

            #  2001:3:3:3::3/128 [VALID]
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ipv6 = group['ipv6']
                state = group['state']
                ipv6_dict = intf_dict.setdefault('ipv6', {}).setdefault(ipv6, {})
                ipv6_dict.update({'state': state})
                continue

            #  IPv6 subnet:  2001:3:3:3::3/128
            m = p5.match(line)
            if m:
                group = m.groupdict()
                subnet = group['subnet']
                intf_dict.update({'ipv6_subnet': subnet})
                continue

            #  IPv6 link-local address: fe80::5c00:80ff:fe02:0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                link_address = group['link_address']
                intf_dict.update({'ipv6_link_local_address': link_address})
                continue

            #   Level1
            m = p7.match(line)
            if m:
                group = m.groupdict()
                level = 'level_{}'.format(group['level'])
                level_dict = intf_dict.setdefault('authentication', {}).setdefault(level, {})
                continue

            #   No auth type and keychain
            m = p8.match(line)
            if m:
                group = m.groupdict()
                continue

            #   Auth check set
            m = p9.match(line)
            if m:
                group = m.groupdict()
                auth_check = group['auth_check']
                level_dict.update({'auth_check': auth_check})
                continue

            #   Index: 0x0001, Local Circuit ID: 0x01, Circuit Type: L1-2
            m = p10.match(line)
            if m:
                group = m.groupdict()
                index = group['index']
                circuit_id = group['circuit_id']
                circuit_type = group['circuit_type']

                intf_dict.update({'index': index,
                                  'local_circuit_id': circuit_id,
                                  'circuit_type': circuit_type})
                continue

            #   BFD IPv4 is locally disabled for Interface loopback0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                bfd_ipv4 = group['bfd_ipv4']
                intf_dict.update({'bfd_ipv4': bfd_ipv4})
                continue

            #   BFD IPv6 is locally disabled for Interface loopback0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                bfd_ipv6 = group['bfd_ipv6']
                intf_dict.update({'bfd_ipv6': bfd_ipv6})
                continue

            #   MTR is enabled
            m = p13.match(line)
            if m:
                group = m.groupdict()
                mtr = group['mtr']
                intf_dict.update({'mtr': mtr})
                continue

            #   Passive level: level-1-2
            m = p13_1.match(line)
            if m:
                group = m.groupdict()
                passive = group['passive']
                intf_dict.update({'passive': passive})
                continue

            #   Level      Metric
            #   1               1
            m = p14.match(line)
            if m:
                group = m.groupdict()
                level = group['level']
                metric = group['metric']
                lvl_dict = intf_dict.setdefault('levels', {}).setdefault(level, {})
                lvl_dict.update({'metric': metric})
                continue

            #   LSP interval: 33 ms, MTU: 1500
            m = p15.match(line)
            if m:
                group = m.groupdict()
                mtu = int(group['mtu'])
                lsp_interval = int(group['lsp_interval'])
                intf_dict.update({'mtu': mtu, 'lsp_interval_ms': lsp_interval})
                continue

            #   Level-1 Designated IS: R2_xr
            m = p16.match(line)
            if m:
                group = m.groupdict()
                level = group['level'].split('-')[-1]
                designated_is = group['designated_is']
                lvl_dict = intf_dict.setdefault('levels', {}).setdefault(level, {})
                lvl_dict.update({'designated_is': designated_is})
                continue

            #   Level   Metric-0   Metric-2   CSNP  Next CSNP  Hello   Multi   Next IIH
            #   1             40         40     10  00:00:06      10   3       00:00:04
            m = p17.match(line)
            if m:
                group = m.groupdict()
                level = group.pop('level')
                lvl_dict = intf_dict.setdefault('levels', {}).setdefault(level, {})
                lvl_dict.update({k: v for k, v in group.items()})
                continue

            #   Level  Adjs   AdjsUp Pri  Circuit ID         Since
            #   1         1        1  64  R2_xr.03           5d01h
            m = p18.match(line)
            if m:
                group = m.groupdict()
                level = group.pop('level')
                lvl_dict = intf_dict.setdefault('levels', {}).setdefault(level, {})
                lvl_dict.update({k: v for k, v in group.items()})
                continue

            #   Topologies enabled:
            #     L  MT  Metric  MetricCfg  Fwdng IPV4-MT  IPV4Cfg  IPV6-MT  IPV6Cfg
            #     1  0        1       no   UP    UP       yes      DN       yes
            m = p19.match(line)
            if m:
                group = m.groupdict()
                mt = group.pop('mt')
                level = group.pop('level')
                topo_dict = intf_dict.setdefault('topologies', {})
                sub_dict = topo_dict.setdefault(mt, {}).setdefault('level', {})\
                                    .setdefault(level, {})
                sub_dict.update({k: v for k, v in group.items()})
                continue

        return result_dict


class ShowIsisSpfLogDetailSchema(MetaParser):
    """Schema for show isis spf-log detail"""

    schema = {
        'instance': {
            Any(): { # process_id
                'vrf': {
                    Any(): {
                        'topology': {
                            Any(): {
                                'total_num_of_spf_calc': int,
                                'log_entry': {
                                    'current': int,
                                    'max': int,
                                },
                                'entrys': {
                                    Any(): {
                                        'ago': str,
                                        'date': str,
                                        'level': {
                                            Any(): {
                                                Optional('instance'): str,
                                                Optional('init'): float,
                                                Optional('spf'): float,
                                                Optional('is_update'): float,
                                                Optional('urib_update'): float,
                                                Optional('total'): float,
                                                Optional('node'): int,
                                                Optional('count'): int,
                                                Optional('changed'): int,
                                                Optional('reason'): str,
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


class ShowIsisSpfLogDetail(ShowIsisSpfLogDetailSchema):
    """Parser for show isis spf-log detail"""

    cli_command = ['show isis spf-log detail', 
                   'show isis spf-log detail vrf {vrf}']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]

            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        result_dict = {}

        # IS-IS Process: test SPF information VRF: default
        p1 = re.compile(r'^IS-IS +[Pp]rocess: +(?P<process_id>\S+) '
                        r'+SPF +information +VRF: +(?P<vrf>\S+)$')

        # SPF log for Topology 0
        p2 = re.compile(r'^SPF +log +for +Topology +(?P<topology>\d+)$')

        # Total number of SPF calculations: 225313
        p3 = re.compile(r'^Total +number +of +SPF +calculations: +(?P<total_num>\d+)$')

        # Log entry (current/max): 20/20
        p4 = re.compile(r'^Log +entry +\(current\/max\): +(?P<curr>\d+)\/(?P<max>\d+)$')

        # Log entry: 01, Ago: 00:01:26, Date: Tue Oct 15 21:53:39 2019
        # Log entry: 20, Ago: 0.800060, Date: Wed Nov 27 16:04:29 2019
        p5 = re.compile(r'^Log +entry: +(?P<entry>\d+), +Ago: +(?P<ago>[\d\.\:]+), '
                        r'+Date: +(?P<date>[\S\s]+)$')

        #   Level  Instance    Init      SPF       IS Update  URIB Update  Total
        #   2      0x0001B80B  0.000919  0.000896  0.000157   0.000439     0.002559
        p6 = re.compile(r'^(?P<level>\d+) +(?P<instance>\S+) +(?P<init>[\d\.]+) '
                        r'+(?P<spf>\S+) +(?P<is_update>\S+) '
                        r'+(?P<urib_update>\S+) +(?P<total>\S+)$')

        #   Level  Node Count   Changed  Reason
        #   2         4     7         0  New adj R2_xr on Ethernet1/1.115
        p7 = re.compile(r'^(?P<level>\d+) +(?P<node>\d+) +(?P<count>\d+) '
                        r'+(?P<changed>\d+) +(?P<reason>[\S\s]+)$')

        for line in out.splitlines():
            line = line.strip()

            # IS-IS Process: test SPF information VRF: default
            m = p1.match(line)
            if m:
                group = m.groupdict()
                process_id = group['process_id']
                vrf = group['vrf']

                vrf_dict = result_dict.setdefault('instance', {}).\
                                       setdefault(process_id, {}).\
                                       setdefault('vrf', {}).\
                                       setdefault(vrf, {})
                continue

            # SPF log for Topology 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                topo = group['topology']
                topo_dict = vrf_dict.setdefault('topology', {}).setdefault(topo, {})
                continue

            # Total number of SPF calculations: 225303
            m = p3.match(line)
            if m:
                group = m.groupdict()
                total_num = int(group['total_num'])
                topo_dict.update({'total_num_of_spf_calc': total_num})
                continue

            # Log entry (current/max): 20/20
            m = p4.match(line)
            if m:
                group = m.groupdict()
                curr = int(group['curr'])
                max = int(group['max'])
                log_dict = topo_dict.setdefault('log_entry', {})
                log_dict.update({'current': curr, 'max': max})
                continue

            # Log entry: 01, Ago: 00:01:25, Date: Tue Oct 15 21:52:57 2019
            m = p5.match(line)
            if m:
                group = m.groupdict()
                entry = group['entry']
                ago = group['ago']
                date = group['date']

                entry_dict = topo_dict.setdefault('entrys', {}).setdefault(entry, {})
                entry_dict.update({'ago': ago, 'date': date})
                continue

            #   Level  Instance    Init      SPF       IS Update  URIB Update  Total
            #   2      0x0001B80B  0.000919  0.000896  0.000157   0.000439     0.002559
            m = p6.match(line)
            if m:
                group = m.groupdict()
                level = int(group.pop('level'))
                lvl_dict = entry_dict.setdefault('level', {}).setdefault(level, {})
                lvl_dict.update({'instance': group.pop('instance')})
                lvl_dict.update({k: float(v) for k, v in group.items()})
                continue

            #   Level  Node Count   Changed  Reason
            #   2         4     6         0  New adj R1_xe on Ethernet1/2.115
            m = p7.match(line)
            if m:
                group = m.groupdict()
                level = int(group.pop('level'))
                lvl_dict = entry_dict.setdefault('level', {}).setdefault(level, {})
                lvl_dict.update({k: int(v) if v.isdigit() else v for k, v in group.items()})
                continue

        return result_dict


class ShowIsisAdjacencySchema(MetaParser):
    """Schema for show isis adjacency"""

    schema = {
        'instance': {
            Any(): {
                'vrf': {
                    Any(): {
                        'interfaces': {
                            Any(): {
                                'adjacencies': {
                                    Any(): {
                                        'neighbor_snpa': {
                                            Any(): {
                                                'level': {
                                                    Any(): {
                                                        'hold_time': str, 
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


class ShowIsisAdjacency(ShowIsisAdjacencySchema):
    """Parser for show isis adjacency"""

    cli_command = ['show isis adjacency', 
                   'show isis adjacency vrf {vrf}']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]

            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        result_dict = {}

        # IS-IS Process: test VRF: default
        p1 = re.compile(r'^IS-IS +[Pp]rocess: +(?P<process_id>\S+) +VRF: +(?P<vrf>\S+)$')

        # System ID       SNPA            Level  State  Hold Time  Interface
        # R2_xr           fa16.3eff.4abd  1      UP     00:00:09   Ethernet1/1.115
        # 2222.22ff.4444  fa16.3eff.4abd  1      INIT   00:00:32   Ethernet1/1.415
        # plum-fx-1       N/A             1-2    UP     00:00:30   Vlan100
        p2 = re.compile(r'^(?P<sysid>\S+) +(?P<snpa>[/\w\.]+) +(?P<level>[\d-]+) '
                        r'+(?P<state>\S+) +(?P<hold_time>[\d\:]+) +(?P<interface>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # IS-IS Process: test VRF: default
            m = p1.match(line)
            if m:
                group = m.groupdict()
                process_id = group['process_id']
                vrf = group['vrf']

                vrf_dict = result_dict.setdefault('instance', {}).\
                                       setdefault(process_id, {}).\
                                       setdefault('vrf', {}).\
                                       setdefault(vrf, {})
                continue

            # R2_xr           fa16.3eff.4abd  1      UP     00:00:09   Ethernet1/1.115
            m = p2.match(line)
            if m:
                group = m.groupdict()
                sysid = group['sysid']
                snpa = group['snpa']
                level = group['level']
                state = group['state']
                hold_time = group['hold_time']
                interface = Common.convert_intf_name(group['interface'])

                level_dict = vrf_dict.setdefault('interfaces', {}).setdefault(interface, {}).\
                                      setdefault('adjacencies', {}).setdefault(sysid, {}).\
                                      setdefault('neighbor_snpa', {}).setdefault(snpa, {}).\
                                      setdefault('level', {}).setdefault(level, {})

                level_dict.update({'hold_time': hold_time})
                level_dict.update({'state': state})

                continue

        return result_dict


class ShowIsisHostnameSchema(MetaParser):
    """Schema for show isis hostname"""

    schema = {
        'instance': {
            Any(): {
                'vrf': {
                    Any(): {
                        'hostname_db': {
                            'hostname': {
                                Any(): {
                                    'hostname': str,
                                    'level': list,
                                    Optional('local_router'): bool,
                                },
                            },
                        },
                    },
                },
            },
        },
    }


class ShowIsisHostname(ShowIsisHostnameSchema):
    """Parser for show isis hostname"""

    cli_command = ['show isis hostname', 
                   'show isis hostname vrf {vrf}']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]

            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        result_dict = {}

        # IS-IS Process: test dynamic hostname table VRF: default
        p1 = re.compile(r'^IS-IS +Process: +(?P<process_id>\S+) +dynamic '
                        r'+hostname +table +VRF: +(?P<vrf>\S+)$')

        #  Level  System ID       Dynamic hostname
        #  1      1111.11ff.2222  R1_ios
        #  1      3333.33ff.6666* R3_nx
        p2 = re.compile(r'^(?P<level>\d+) +(?P<system_id>[a-zA-Z\d\-\.]+)(?P<star>\*)? '
                        r'+(?P<dynamic_hostname>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            #  IS-IS Process: test dynamic hostname table VRF: default
            m = p1.match(line)
            if m:
                group = m.groupdict()
                process_id = group['process_id']
                vrf = group['vrf']

                vrf_dict = result_dict.setdefault('instance', {}).\
                                       setdefault(process_id, {}).\
                                       setdefault('vrf', {}).\
                                       setdefault(vrf, {})
                continue

            #  1      1111.11ff.2222  R1_ios
            #  1      3333.33ff.6666* R3_nx
            m = p2.match(line)
            if m:
                group = m.groupdict()
                hostname_dict = vrf_dict.setdefault('hostname_db', {}).\
                                         setdefault('hostname', {}).\
                                         setdefault(group['system_id'], {})

                hostname_dict.update({'hostname': group['dynamic_hostname']})
                level_list = hostname_dict.get('level', [])
                level = int(group['level'])
                if level not in level_list:
                    level_list.append(level)
                hostname_dict.update({'level': level_list})

                if group['star']:
                    hostname_dict.update({'local_router': True})
                continue

        return result_dict

class ShowIsisHostnameDetailSchema(MetaParser):
    """Schema for 
            * show isis hostname detail
            * show isis hostname detail vrf {vrf}"""

    schema = {
        'instance': {
            Any(): {
                'vrf': {
                    Any(): {
                        'hostname_db': {
                            'hostname': {
                                Any(): {
                                    'hostname': str,
                                    'level': list,
                                    Optional('local_router'): bool,
                                },
                            },
                        },
                    },
                },
            },
        },
    }

class ShowIsisHostnameDetail(ShowIsisHostnameDetailSchema):
    """Parser for 
            * show isis hostname detail
            * show isis hostname detail vrf {vrf}"""

    cli_command = ['show isis hostname detail', 
                   'show isis hostname detail vrf {vrf}']
    
    def cli(self, vrf=None, output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output
        
        # initial return dictionary
        result_dict = {}

        # IS-IS Process: test dynamic hostname table VRF: default
        p1 = re.compile(r'^IS-IS +Process: +(?P<process_id>\S+) +dynamic '
                        r'+hostname +table +VRF: +(?P<vrf>\S+)$')

        #  Level  LSP ID                Dynamic hostname
        #  1      7777.77ff.eeee.00-00* R7
        #  2      2222.22ff.4444.00-00  R2
        p2 = re.compile(r'^(?P<level>\d+) +(?P<lsp_id>[a-zA-Z\d\-\.]+)(?P<star>\*)? '
                        r'+(?P<dynamic_hostname>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            #  IS-IS Process: test dynamic hostname table VRF: default
            m = p1.match(line)
            if m:
                group = m.groupdict()
                process_id = group['process_id']
                vrf = group['vrf']

                vrf_dict = result_dict.setdefault('instance', {}).\
                                       setdefault(process_id, {}).\
                                       setdefault('vrf', {}).\
                                       setdefault(vrf, {})
                continue

            #  1      7777.77ff.eeee.00-00* R7
            #  2      2222.22ff.4444.00-00  R2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                hostname_dict = vrf_dict.setdefault('hostname_db', {}).\
                                         setdefault('hostname', {}).\
                                         setdefault(group['lsp_id'], {})

                hostname_dict.update({'hostname': group['dynamic_hostname']})
                level_list = hostname_dict.get('level', [])
                level = int(group['level'])
                if level not in level_list:
                    level_list.append(level)
                hostname_dict.update({'level': level_list})

                if group['star']:
                    hostname_dict.update({'local_router': True})
                continue
        
        return result_dict

class ShowIsisDatabaseDetailSchema(MetaParser):
    """Schema for show isis database detail"""

    schema = {
        'instance': {
            Any(): {
                'vrf': {
                    Any(): {
                        'level_db': {
                            Any(): { # level
                                Any(): { # lsp_id
                                    'lsp_id': str,
                                    'lsp_status': str,
                                    'sequence': str,
                                    'checksum': str,
                                    'lifetime': int,
                                    'attach_bit': int,
                                    'p_bit': int,
                                    'overload_bit': int,
                                    't_bit': int,
                                    'instance': str,
                                    Optional('area_address'): str,
                                    Optional('nlpid'): str,
                                    Optional('hostname'): str,
                                    Optional('router_id'): str,
                                    Optional('length'): int,
                                    Optional('mt_entries'): {
                                        Any(): {
                                            'att': int,
                                            'ol': int,
                                        }
                                    },
                                    Optional('extended_is_neighbor'): {
                                        Any(): {
                                            'neighbor_id': str,
                                            'metric': int,
                                        },
                                    },
                                    Optional('mt_is_neighbor'): {
                                        Any(): {
                                            'neighbor_id': str,
                                            'metric': int,
                                            'topo_id': int,
                                        },
                                    },
                                    Optional('ip_address'): str,
                                    Optional('extended_ip'): {
                                        Any(): {
                                            'metric': int,
                                            'up_down': str,
                                            Optional('sub_tlv_length'): int,
                                            Optional('sub_tlv_type'): int,
                                        },
                                    },
                                    Optional('ipv6_address'): str,
                                    Optional('mt_ipv6_prefix'): {
                                        Any(): {
                                            'metric': int,
                                            'topo_id': int,
                                            'up_down': str,
                                            'ext_origin': str,
                                            Optional('sub_tlv_length'): int,
                                            Optional('sub_tlv_type'): int,
                                        },
                                    },
                                    'digest_offset': int,
                                },
                            },
                        },
                    },
                },
            },
        },
    }


class ShowIsisDatabaseDetail(ShowIsisDatabaseDetailSchema):
    """Parser for show isis database detail"""

    cli_command = ['show isis database detail',
                   'show isis database detail vrf {vrf}']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]

            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        result_dict = {}

        # IS-IS Process: test dynamic hostname table VRF: default
        p1 = re.compile(r'^IS-IS +Process: +(?P<process_id>\S+) '
                        r'+LSP +database +VRF: +(?P<vrf>\S+)$')

        # IS-IS Level-1 Link State Database
        p2 = re.compile(r'^IS-IS +Level-(?P<level>\d+) +Link +State +Database(:)?$')

        # LSPID                 Seq Number   Checksum  Lifetime   A/P/O/T
        # R1_xe.00-00           0x000007CC   0xAF21    490        0/0/0/3
        # R3_nx.00-00         * 0x00000B05   0x7FA7    697        0/0/0/3
        p3 = re.compile(
            r'^(?P<lsp_id>\S+)(\s*(?P<lsp_status>[!*#?]+))? +(?P<sequence>\w+) +(?P<checksum>\w+) '
            r'+(?P<lifetime>[\d\*]+) +(?P<a>\d+)/(?P<p>\d+)/(?P<o>\d+)/(?P<t>\d+)$')

        #   Instance      :  0x000007C8
        p4 = re.compile(r'^Instance *: +(?P<instance>\w+)$')

        #   Area Address : 49.0001
        p5 = re.compile(r'^Area +Address *: +(?P<area_address>[\w\.]+)$')

        #   NLPID      :  0xCC 0x8E
        p6 = re.compile(r'^NLPID *: +(?P<nlp_id>[\w\s]+)$')

        #   MT TopoId     : TopoId:0 Att: 0 Ol: 0
        #                   TopoId:2 Att: 0 Ol: 0
        p7 = re.compile(r'^(MT TopoId *: +)?TopoId:(?P<topo_id>\d+) +Att: +(?P<att>\d+) +Ol: +(?P<ol>\d+)$')

        #   Hostname      :  R1_xe              Length : 5
        p8 = re.compile(r'^Hostname *: +(?P<hostname>\S+) +Length *: +(?P<length>\d+)$')

        #   Extended IS   :  R1_xe.02           Metric : 10
        p9 = re.compile(r'^Extended +IS *: +(?P<ext>\S+) +Metric *: +(?P<metric>\d+)$')
        
        #   TopoId: 2
        p10 = re.compile(r'^TopoId *: +(?P<topo_id>\d+)$')
        
        #   MtExtend IS   :  R1_xe.01           Metric : 10
        #                    R2_xr.03           Metric : 10
        p11 = re.compile(r'^(MtExtend +IS *: +)?(?P<mt_ext>\S+) +Metric *: +(?P<metric>\d+)$')

        #   IP Address    :  10.13.115.1
        p12 = re.compile(r'^IP +Address *: +(?P<ip_address>[\d\.]+)$')

        #   Extended IP   :     10.12.115.0/24  Metric : 10          (U)
        #   Extended IP   :     10.12.115.0/24  Metric : 10          (D)
        p13 = re.compile(r'^Extended +IP *: +(?P<ext_ip>\S+) +Metric *: +(?P<metric>\d+) +\((?P<up_down>\S+)\)$')

        #   IPv6 Address  :  2001:10:13:115::1
        p14 = re.compile(r'^IPv6 +Address *: +(?P<ip_address>\S+)$')

        #   Router ID     :  10.36.3.3
        p15 = re.compile(r'^Router +ID *: +(?P<router_id>\S+)$')

        #   MT-IPv6 Prefx :  TopoId : 2
        p16 = re.compile(r'^MT-IPv6 +Prefx *: +TopoId *: +(?P<topo_id>\d+)$')

        #   2001:10:12:115::/64  Metric : 10          (U/I)
        #   2001:10:12:115::/64  Metric : 10          (D/E)
        p17 = re.compile(r'^(?P<prefix>\S+) +Metric *: +(?P<metric>\d+) +\((?P<up_down>\w+)\/(?P<ext_origin>\w+)\)$')

        #   Unknown Sub-TLV      :  Length : 1  Type :   4
        p18 = re.compile(r'^Unknown +Sub-TLV *: +Length *: +(?P<length>\d+) +Type *: +(?P<type>\d+)$')

        #   Digest Offset :  0
        p19 = re.compile(r'^Digest +Offset *: +(?P<offset>\d+)$')

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue
            
            # IS-IS Process: test dynamic hostname table VRF: default
            m = p1.match(line)
            if m:
                group = m.groupdict()
                process_id = group['process_id']
                vrf = group['vrf']

                vrf_dict = result_dict.setdefault('instance', {}).\
                                       setdefault(process_id, {}).\
                                       setdefault('vrf', {}).\
                                       setdefault(vrf, {})
                continue

            # IS-IS Level-1 Link State Database
            m = p2.match(line)
            if m:
                group = m.groupdict()
                lvl = int(group['level'])
                lvl_dict = vrf_dict.setdefault('level_db', {}).setdefault(lvl, {})
                continue

            # LSPID                 Seq Number   Checksum  Lifetime   A/P/O/T
            # R1_xe.00-00           0x000007CC   0xAF21    490        0/0/0/3
            # R3_nx.00-00         * 0x00000B05   0x7FA7    697        0/0/0/3
            m = p3.match(line)
            if m:
                group = m.groupdict()
                lsp_id = group['lsp_id']
                sequence = group['sequence']
                checksum = group['checksum']
                lifetime = int(group['lifetime'])
                lsp_status = group['lsp_status']
                a = int(group['a'])
                p = int(group['p'])
                o = int(group['o'])
                t = int(group['t'])

                lsp_dict = lvl_dict.setdefault(lsp_id, {})
                lsp_dict['lsp_id'] = lsp_id
                lsp_dict['sequence'] = sequence
                lsp_dict['checksum'] = checksum
                lsp_dict['lifetime'] = lifetime
                lsp_dict['attach_bit'] = a
                lsp_dict['p_bit'] = p
                lsp_dict['overload_bit'] = o
                lsp_dict['t_bit'] = t
                lsp_dict['lsp_status'] = lsp_status or ''
                continue

            #   Instance      :  0x000007C8
            m = p4.match(line)
            if m:
                lsp_dict['instance'] = m.groupdict()['instance']
                continue

            #   Area Address : 49.0001
            m = p5.match(line)
            if m:
                lsp_dict['area_address'] = m.groupdict()['area_address']
                continue

            #   NLPID      :  0xCC 0x8E
            m = p6.match(line)
            if m:
                lsp_dict['nlpid'] = m.groupdict()['nlp_id']
                continue

            #   MT TopoId     : TopoId:0 Att: 0 Ol: 0
            #                   TopoId:2 Att: 0 Ol: 0
            m = p7.match(line)
            if m:
                topo_id = int(m.groupdict()['topo_id'])
                att = int(m.groupdict()['att'])
                ol = int(m.groupdict()['ol'])
                
                entry_dict = lsp_dict.setdefault('mt_entries', {}).setdefault(topo_id, {})
                entry_dict['att'] = att
                entry_dict['ol'] = ol
                continue

            #   Hostname      :  R1_xe              Length : 5
            m = p8.match(line)
            if m:
                lsp_dict['hostname'] = m.groupdict()['hostname']
                lsp_dict['length'] = int(m.groupdict()['length'])
                continue

            #   Extended IS   :  R1_xe.02           Metric : 10
            m = p9.match(line)
            if m:
                ext = m.groupdict()['ext']
                metric = int(m.groupdict()['metric'])

                ext_is_dict = lsp_dict.setdefault('extended_is_neighbor', {}).\
                                       setdefault(ext, {})
                ext_is_dict['neighbor_id'] = ext
                ext_is_dict['metric'] = metric
                continue
            
            #   TopoId: 2
            m = p10.match(line)
            if m:
                ipv4_topo_id = int(m.groupdict()['topo_id'])
                continue
            
            #   MtExtend IS   :  R1_xe.01           Metric : 10
            #                    R2_xr.03           Metric : 10
            m = p11.match(line)
            if m:
                mt_ext = m.groupdict()['mt_ext']
                metric = int(m.groupdict()['metric'])

                mt_ext_dict = lsp_dict.setdefault('mt_is_neighbor', {}).\
                                       setdefault(ext, {})
                mt_ext_dict['neighbor_id'] = mt_ext
                mt_ext_dict['metric'] = metric
                mt_ext_dict['topo_id'] = ipv4_topo_id
                continue

            #   IP Address    :  10.13.115.1
            m = p12.match(line)
            if m:
                lsp_dict['ip_address'] = m.groupdict()['ip_address']
                continue

            #   Extended IP   :     10.12.115.0/24  Metric : 10          (U)
            m = p13.match(line)
            if m:
                ip = m.groupdict()['ext_ip']
                metric = int(m.groupdict()['metric'])
                up_down = m.groupdict()['up_down']
                ip_dict = lsp_dict.setdefault('extended_ip', {}).setdefault(ip, {})

                ip_dict['metric'] = metric
                ip_dict['up_down'] = up_down
                continue

            #   IPv6 Address  :  2001:10:13:115::1
            m = p14.match(line)
            if m:
                lsp_dict['ipv6_address'] = m.groupdict()['ip_address']
                continue

            #   Router ID     :  10.36.3.3
            m = p15.match(line)
            if m:
                lsp_dict['router_id'] = m.groupdict()['router_id']
                continue

            #   MT-IPv6 Prefx :  TopoId : 2
            m = p16.match(line)
            if m:
                topo_id = int(m.groupdict()['topo_id'])
                ipv6_topo_id = topo_id
                continue

            #   2001:10:12:115::/64  Metric : 10          (U/I)
            m = p17.match(line)
            if m:
                prefix = m.groupdict()['prefix']
                metric = int(m.groupdict()['metric'])
                up_down = m.groupdict()['up_down']
                ext_origin = m.groupdict()['ext_origin']
                ip_dict = lsp_dict.setdefault('mt_ipv6_prefix', {}).setdefault(prefix, {})

                ip_dict['metric'] = metric
                ip_dict['topo_id'] = ipv6_topo_id
                ip_dict['up_down'] = up_down
                ip_dict['ext_origin'] = ext_origin
                continue

            #   Unknown Sub-TLV      :  Length : 1  Type :   4
            m = p18.match(line)
            if m:
                length = int(m.groupdict()['length'])
                stype = int(m.groupdict()['type'])

                ip_dict['sub_tlv_length'] = length
                ip_dict['sub_tlv_type'] = stype
                continue

            #   Digest Offset :  0
            m = p19.match(line)
            if m:
                lsp_dict['digest_offset'] = int(m.groupdict()['offset'])
                continue

        return result_dict
