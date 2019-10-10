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
        Any(): {
            'process_id': str,
            'instance_number': int,
            'uuid': str,
            'pid': int,
            'vrf': {
                Any(): {
                    'vrf': str,
                    'system_id': str,
                    'is_type': str,
                    'sap': int,
                    'queue_handle': int,
                    'lsp_mtu': int,
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
                    'metric_type': str,
                    'area_address': list,
                    'enable': bool,
                    'vrf_id': int,
                    'sr_ipv4': str,
                    'sr_ipv6': str,
                    'supported_interfaces': list,
                    'topology': {
                        Any(): {
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
                    'authentication': {
                        'level_1': {
                            'authentication_type': dict,
                            'auth_check': str,
                        },
                        'level_2': {
                            'authentication_type': dict,
                            'auth_check': str,
                        },
                    },
                    'l1_next_spf': str,
                    'l2_next_spf': str,
                },
            },
        },
    }


class ShowIsis(ShowIsisSchema):
    """Parser for show isis"""

    cli_command = ['show isis', 'show isis vrf {vrf}']

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
        p1 = re.compile(r'^ISIS +[Pp]rocess *: +(?P<process_id>\S+)$')

        # Instance number :  1
        p2 = re.compile(r'^Instance +number *: +(?P<instance_number>\d+)$')

        # UUID: 1090519320
        p3 = re.compile(r'^UUID *: +(?P<uuid>\d+)$')

        # Process ID 1581
        p4 = re.compile(r'^Process +ID +(?P<pid>\d+)$')

        # VRF: default
        p5 = re.compile(r'^VRF *: +(?P<vrf>\S+)$')

        # System ID : 3333.3333.3333  IS-Type : L1-L2
        p6 = re.compile(r'^System +ID *: +(?P<sysid>[\d\.]+) +IS-Type *: +(?P<is_type>\S+)$')

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
        p13 = re.compile(r'^BFD +IPv4 +is +globally +(?P<bfd_ipv4>\w+) +for +ISIS +process: +(?P<name>.*)$')

        # BFD IPv6 is globally disabled for ISIS process: test
        p14 = re.compile(r'^BFD +IPv6 +is +globally +(?P<bfd_ipv6>\w+) +for +ISIS +process: +(?P<name>.*)$')

        # Topology-mode is Multitopology
        p15 = re.compile(r'^Topology-mode +is +(?P<topology_mode>\w+)$')

        # Metric-style : advertise(wide), accept(narrow, wide)
        p16 = re.compile(r'^Metric-style *: +(?P<metric_type>[\S\s]+)$')

        # Area address(es) :
        #     49.0001
        p17 = re.compile(r'^(?P<area>[\d\.]+)$')

        # Process is up and running
        p18 = re.compile(r'^Process +is +(?P<enable>[\S\s]+)$')

        # VRF ID: 1
        p19 = re.compile(r'^VRF +ID *: +(?P<vrf_id>\d+)$')

        # Stale routes during non-graceful controlled restart
        p20 = re.compile(r'^Stale routes during non-graceful controlled restart$')

        # Enable resolution of L3->L2 address for ISIS adjacency
        p21 = re.compile(r'^Enable resolution of L3->L2 address for ISIS adjacency$')

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
                process_id = group['process_id']
                pid_dict = result_dict.setdefault(process_id, {})
                pid_dict.update({'process_id': process_id})
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
                pid = int(group['pid'])
                pid_dict.update({'pid': pid})            
                continue

            # VRF: VRF1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                vrf = group['vrf']
                vrf_dict = pid_dict.setdefault('vrf', {}).setdefault(vrf, {})
                vrf_dict.update({'vrf': vrf})
                continue

            #   System ID : 3333.3333.3333  IS-Type : L1-L2
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
                vrf_dict.update({'lsp_mtu': lsp_mtu})
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
                metric_type = group['metric_type']
                vrf_dict.update({'metric_type': metric_type})
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
                enable = group['enable']
                if 'up' in enable.lower():
                    vrf_dict.update({'enable': True})
                else:
                    vrf_dict.update({'enable': False})
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
                continue

            #   Enable resolution of L3->L2 address for ISIS adjacency
            m = p21.match(line)
            if m:
                group = m.groupdict()
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
                af_dict = topo_dict.setdefault(af, {})
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
                level_dict.update({'authentication_type': {}})
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
        Any(): {
            Any(): Any(),
        },
    }
    # schema = {
    #     Any(): {
    #         'process_id': str,
    #         'instance_number': int,
    #         'uuid': str,
    #         'pid': int,
    #         'vrf': {
    #             Any(): {
    #                 'vrf': str,
    #                 'system_id': str,
    #                 'is_type': str,
    #                 'sap': int,
    #                 'queue_handle': int,
    #                 'lsp_mtu': int,
    #                 'stateful_ha': str,
    #                 'graceful_restart': {
    #                     'enable': bool,
    #                     'state': str,
    #                     'last_gr_status': str,
    #                 },
    #                 'start_mode': str,
    #                 'bfd_ipv4': str,
    #                 'bfd_ipv6': str,
    #                 'topology_mode': str,
    #                 'metric_type': str,
    #                 'area_address': list,
    #                 'enable': bool,
    #                 'vrf_id': int,
    #                 'sr_ipv4': str,
    #                 'sr_ipv6': str,
    #                 'supported_interfaces': list,
    #                 'topology': {
    #                     Any(): {
    #                         Optional('ipv4_unicast'): {
    #                             'number_of_interface': int,
    #                             'distance': int,
    #                         },
    #                         Optional('ipv6_unicast'): {
    #                             'number_of_interface': int,
    #                             'distance': int,
    #                         },
    #                     },
    #                 },
    #                 'authentication': {
    #                     'level_1': {
    #                         'authentication_type': dict,
    #                         'auth_check': str,
    #                     },
    #                     'level_2': {
    #                         'authentication_type': dict,
    #                         'auth_check': str,
    #                     },
    #                 },
    #                 'l1_next_spf': str,
    #                 'l2_next_spf': str,
    #             },
    #         },
    #     },
    # }


class ShowIsisInterface(ShowIsisInterfaceSchema):
    """Parser for show isis interface"""

    cli_command = ['show isis interface', 'show isis interface vrf {vrf}']

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

        #   IP address: 3.3.3.3, IP subnet: 3.3.3.3/32
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
                          '+(?P<circuit_id>\w+), +Circuit +Type: +(?P<circuit_type>\S+)$')

        #   BFD IPv4 is locally disabled for Interface loopback0
        p11 = re.compile(r'^BFD +IPv4 +is +locally +(?P<bfd_ipv4>\w+) +for +Interface +(?P<intf>.*)$')

        #   BFD IPv6 is locally disabled for Interface loopback0
        p12 = re.compile(r'^BFD +IPv6 +is +locally +(?P<bfd_ipv6>\w+) +for +Interface +(?P<intf>.*)$')
        
        #   MTR is enabled
        p13 = re.compile(r'^MTR +is +(?P<mtr>\w+)$')

        #   Level      Metric
        #   1               1
        p14 = re.compile(r'^(?P<level>\d+) +(?P<metric>\d+)$')

        #   LSP interval: 33 ms, MTU: 1500
        p15 = re.compile(r'^LSP +interval: +(?P<lsp_interval>[\w\s]+), +MTU: +(?P<mtu>\d+)$')
        
        #   Level-1 Designated IS: R2_xr
        #   Level-2 Designated IS: R2_xr
        p16 = re.compile(r'^(?P<level>\S+) +Designated +IS: +(?P<designated_is>\S+)$')

        #   Level   Metric-0   Metric-2   CSNP  Next CSNP  Hello   Multi   Next IIH
        #   1              40     40     10 00:00:06      10   3       00:00:04
        #   2              40     40     10 00:00:03      10   3       00:00:09
        p17 = re.compile(r'^(?P<level>\d+) +(?P<metric_0>\d+) +(?P<metric_2>\d+) '
                          '+(?P<csnp>\d+) +(?P<next_csnp>[\d\:]+) +(?P<hello>\d+) '
                          '+(?P<multi>\d+) +(?P<next_iih>[\d\:]+)$')

        #   Level  Adjs   AdjsUp Pri  Circuit ID         Since
        #   1         1        1  64  R2_xr.03           5d01h
        #   2         1        1  64  R2_xr.03           5d01h
        p18 = re.compile(r'^(?P<level>\d+) +(?P<adjs>\d+) +(?P<adjs_up>\d+) '
                          '+(?P<pri>\d+) +(?P<circuit_id>\S+) +(?P<since>\w+)$')

        #   Topologies enabled:
        #     L  MT  Metric  MetricCfg  Fwdng IPV4-MT  IPV4Cfg  IPV6-MT  IPV6Cfg
        #     1  0        1       no   UP    UP       yes      DN       yes
        p19 = re.compile(r'^(?P<level>\d+) +(?P<mt>\d+) +(?P<metric>\d+) '
                          '+(?P<metric_cfg>\w+) +(?P<fwdng>\w+) +(?P<ipv4_mt>\w+) '
                          '+(?P<ipv4_cfg>\w+) +(?P<ipv6_mt>\w+) +(?P<ipv6_cfg>\w+)$')

        for line in out.splitlines():
            line = line.strip()

            # IS-IS process: test VRF: default
            m = p1.match(line)
            if m:
                group = m.groupdict()
                process_id = group['process_id']
                vrf = group['vrf']

                vrf_dict = result_dict.setdefault(process_id, {}).\
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

            #  IP address: 3.3.3.3, IP subnet: 3.3.3.3/32
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
                intf_dict.update({'ipv6': ipv6, 'ipv6_state': state})
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
                intf_dict.update({'ipv6_link_address': link_address})
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
                level_dict.update({'authentication_type': {}})
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

            #   Level      Metric
            #   1               1
            m = p14.match(line)
            if m:
                group = m.groupdict()
                level = 'level_{}'.format(group['level'])
                metric = group['metric']
                lvl_dict = intf_dict.setdefault('levels', {}).setdefault(level, {})
                lvl_dict.update({'metric': metric})
                continue

            #   LSP interval: 33 ms, MTU: 1500
            m = p15.match(line)
            if m:
                group = m.groupdict()
                mtu = int(group['mtu'])
                lsp_interval = group['lsp_interval']
                intf_dict.update({'mtu': mtu, 'lsp_interval': lsp_interval})
                continue

            #   Level-1 Designated IS: R2_xr
            m = p16.match(line)
            if m:
                group = m.groupdict()
                level = group['level'].replace('-', '_').lower()
                designated_is = group['designated_is']
                lvl_dict = intf_dict.setdefault('levels', {}).setdefault(level, {})
                lvl_dict.update({'designated_is': designated_is})
                continue

            #   Level   Metric-0   Metric-2   CSNP  Next CSNP  Hello   Multi   Next IIH
            #   1              40     40     10 00:00:06      10   3       00:00:04
            m = p17.match(line)
            if m:
                group = m.groupdict()
                level = 'level_{}'.format(group.pop('level'))
                lvl_dict = intf_dict.setdefault('levels', {}).setdefault(level, {})
                lvl_dict.update({k: v for k, v in group.items()})
                continue

            #   Level  Adjs   AdjsUp Pri  Circuit ID         Since
            #   1         1        1  64  R2_xr.03           5d01h
            m = p18.match(line)
            if m:
                group = m.groupdict()
                level = 'level_{}'.format(group.pop('level'))
                lvl_dict = intf_dict.setdefault('levels', {}).setdefault(level, {})
                lvl_dict.update({k: v for k, v in group.items()})
                continue

            #   Topologies enabled:
            #     L  MT  Metric  MetricCfg  Fwdng IPV4-MT  IPV4Cfg  IPV6-MT  IPV6Cfg
            #     1  0        1       no   UP    UP       yes      DN       yes
            m = p19.match(line)
            if m:
                group = m.groupdict()
                topo_dict = intf_dict.setdefault('topologies', {})
                idx_dict = topo_dict.setdefault(len(topo_dict)+1, {})
                idx_dict.update({k: v for k, v in group.items()})
                continue

        return result_dict


class ShowIsisAdjacencySchema(MetaParser):
    """Schema for show isis adjacency"""

    schema = {
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
    }


class ShowIsisAdjacency(ShowIsisAdjacencySchema):
    """Parser for show isis adjacency"""

    cli_command = ['show isis adjacency', 'show isis adjacency vrf {vrf}']

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
        # R2_xr           fa16.3e44.0679  1      UP     00:00:09   Ethernet1/1.115
        # 2222.2222.2222  fa16.3e44.0679  1      INIT   00:00:32   Ethernet1/1.415
        p2 = re.compile(r'^(?P<sysid>\S+) +(?P<snpa>[\w\.]+) +(?P<level>\d+) '
                         '+(?P<state>\S+) +(?P<hold_time>[\d\:]+) +(?P<interface>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # IS-IS Process: test VRF: default
            m = p1.match(line)
            if m:
                group = m.groupdict()
                process_id = group['process_id']
                vrf = group['vrf']

                vrf_dict = result_dict.setdefault(process_id, {}).\
                                       setdefault('vrf', {}).\
                                       setdefault(vrf, {})
                continue

            # R2_xr           fa16.3e44.0679  1      UP     00:00:09   Ethernet1/1.115
            m = p2.match(line)
            if m:
                group = m.groupdict()
                sysid = group['sysid']
                snpa = group['snpa']
                level = int(group['level'])
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
        Any(): {
            'vrf': {
                Any(): {
                    'hostname_db': {
                        'hostname': {
                            Any(): {
                                'hostname': str,
                                'level': int,
                                Optional('local_router'): bool,
                            },
                        },
                    },
                },
            },
        },
    }


class ShowIsisHostname(ShowIsisHostnameSchema):
    """Parser for show isis hostname"""

    cli_command = ['show isis hostname', 'show isis hostname vrf {vrf}']

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
                         '+hostname +table +VRF: +(?P<vrf>\S+)$')

        #  Level  System ID       Dynamic hostname
        #  1      1111.1111.1111  R1_ios
        #  1      3333.3333.3333* R3_nx
        p2 = re.compile(r'^(?P<level>\d+) +(?P<system_id>[\d\.]+)(?P<star>\*)? '
                         '+(?P<dynamic_hostname>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            #  IS-IS Process: test dynamic hostname table VRF: default
            m = p1.match(line)
            if m:
                group = m.groupdict()
                process_id = group['process_id']
                vrf = group['vrf']

                vrf_dict = result_dict.setdefault(process_id, {}).\
                                       setdefault('vrf', {}).\
                                       setdefault(vrf, {})
                continue

            #  1      1111.1111.1111  R1_ios
            #  1      3333.3333.3333* R3_nx
            m = p2.match(line)
            if m:
                group = m.groupdict()
                hostname_dict = vrf_dict.setdefault('hostname_db', {}).\
                                         setdefault('hostname', {}).\
                                         setdefault(group['system_id'], {})

                hostname_dict.update({'hostname': group['dynamic_hostname']})
                hostname_dict.update({'level': int(group['level'])})

                if group['star']:
                    hostname_dict.update({'local_router': True})
                continue

        return result_dict






class ShowIsisDatabaseDetailSchema(MetaParser):
    """Schema for show isis database detail"""

    schema = {
        'tag': {
            Any(): {
                'level': {
                    Any(): {
                        Any(): {
                            'lsp_sequence_num': str,
                            'lsp_checksum': str,
                            Optional('local_router'): bool,
                            'lsp_holdtime': str,
                            Optional('lsp_rcvd'): str,
                            'attach_bit': int,
                            'p_bit': int,
                            'overload_bit': int,
                            Optional('area_address'): str,
                            Optional('router_id'): str,
                            Optional('nlpid'): str,
                            Optional('topology'): {
                                Any(): {
                                    'code': str,
                                },
                            },
                            Optional('hostname'): str,
                            Optional('ip_address'): str,
                            Optional('ipv6_address'): str,
                            Any(): {
                                Any(): {
                                    'metric': int,
                                    Optional('mt_ipv6'): bool,
                                },
                            },
                        },
                    }
                }
            }
        }
    }


class ShowIsisDatabaseDetail(ShowIsisDatabaseDetailSchema):
    """Parser for show isis database detail"""

    cli_command = 'show isis database detail'
    exclude = ['lsp_holdtime' , 'lsp_checksum', 'lsp_sequence_num']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        result_dict = {}
        tag = ""
        #  Tag VRF1:
        p1 = re.compile(r'^Tag +(?P<tag>\w+):$')

        # IS-IS Level-1 Link State Database:
        p2 = re.compile(r'^IS\-IS +Level\-(?P<level>\d+) +Link +State +Database(:)?$')

        # LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime/Rcvd      ATT/P/OL
        # R2.00-00            * 0x00000007   0x8A6D                 403/*         1/0/0
        p3 = re.compile(
            r'^(?P<lspid>[\w\-\.]+)(\s*(?P<star>\*))? +(?P<lsp_seq_num>\w+) +(?P<lsp_checksum>\w+)'
            ' +(?P<lsp_holdtime>[\d\*]+)(/(?P<lsp_rcvd>[\d\*]+))? +(?P<att>\d+)/(?P<p>\d+)/(?P<ol>\d+)$')
        #   Area Address: 49.0001
        p4 = re.compile(r'^Area +Address: +(?P<area_address>[\w\.]+)$')

        #   NLPID:        0xCC 0x8E
        p5 = re.compile(r'^NLPID: +(?P<nlp_id>[\w\s]+)$')

        #   Topology:     IPv4 (0x0)
        #                 IPv6 (0x4002 ATT)
        p6 = re.compile(r'^(Topology: +)?(?P<topology>(IP)+[\w]+) +\((?P<code>[\w\s]+)\)$')

        #   Hostname: R2
        p7 = re.compile(r'^Hostname: +(?P<hostname>\w+)$')
        #   IP Address:   10.84.66.66
        p8 = re.compile(r'^IP +Address: +(?P<ip_address>[\d\.]+)$')

        #   Metric: 10         IP 10.229.7.0/24
        p9 = re.compile(r'^Metric: +(?P<metric>\d+) +(?P<metric_topology>[\w\-]+)( +\((?P<mt_ipv6>[\w\-]+)\))? +(?P<ip>\S+)$')

        #   IPv6 Address: 2001:DB8:66:66:66::66
        p10 = re.compile(r'^IPv6 +Address: +(?P<ip_address>[\w\:]+)$')

        # Router ID:    10.1.77.77
        p11 = re.compile(r'^Router +ID: +(?P<router_id>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            #  Tag VRF1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tag = group['tag']
                continue

            # IS-IS Level-1 Link State Database:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                tag_dict = result_dict.setdefault('tag', {}). \
                                       setdefault(tag, {}). \
                                       setdefault('level', {}). \
                                       setdefault(int(group['level']), {})

                continue

            # LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime/Rcvd      ATT/P/OL
            # R2.00-00            * 0x00000007   0x8A6D                 403/*         1/0/0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                lsp_dict = tag_dict.setdefault(group['lspid'], {})
                if group['star']:
                    lsp_dict.update({'local_router': True})
                lsp_dict.update({'lsp_sequence_num': group['lsp_seq_num']})
                lsp_dict.update({'lsp_checksum': group['lsp_checksum']})
                lsp_dict.update({'lsp_holdtime': group['lsp_holdtime']})
                if group['lsp_rcvd']:
                    lsp_dict.update({'lsp_rcvd': group['lsp_rcvd']})
                lsp_dict.update({'attach_bit': int(group['att'])})
                lsp_dict.update({'p_bit': int(group['p'])})
                lsp_dict.update({'overload_bit': int(group['ol'])})
                continue

            #   Area Address: 49.0001
            m = p4.match(line)
            if m:
                group = m.groupdict()
                lsp_dict.update({"area_address": group['area_address']})
                continue

            #   NLPID:        0xCC 0x8E
            m = p5.match(line)
            if m:
                group = m.groupdict()
                lsp_dict.update({"nlpid": group['nlp_id']})
                continue

            #   Topology:     IPv4 (0x0)
            #                 IPv6 (0x4002 ATT)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                lsp_dict.setdefault('topology', {}).setdefault(group['topology'].lower(), {}).update({'code': group['code']})
                continue

            #   Hostname: R2
            m = p7.match(line)
            if m:
                group = m.groupdict()
                lsp_dict.update({'hostname': group['hostname']})
                continue

            #   IP Address:   10.84.66.66
            m = p8.match(line)
            if m:
                group = m.groupdict()
                lsp_dict.update({'ip_address': group['ip_address']})
                continue

            #  Metric: 10         IP 10.229.7.0/24
            #  Metric: 40         IS (MT-IPv6) R2.01
            #  Metric: 40         IS-Extended R2.01
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ip_dict = lsp_dict.setdefault(group['ip'], {}).setdefault(group['metric_topology'].lower(), {})
                ip_dict.update({'metric': int(group['metric'])})
                if group['mt_ipv6']:
                    ip_dict.update({'mt_ipv6': True})

                continue

            #   IPv6 Address: 2001:DB8:66:66:66::66
            m = p10.match(line)
            if m:
                group = m.groupdict()
                lsp_dict.update({'ipv6_address': group['ip_address']})
                continue

            #  Router ID:    10.1.77.77
            m = p11.match(line)
            if m:
                group = m.groupdict()
                lsp_dict.update({'router_id': group['router_id']})
                continue

        return result_dict
