"""show_lag.py
   supported commands:
     *  show lacp system-id
     *  show bundle 
     *  show lacp
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowLacpSystemIdSchema(MetaParser):
    """Schema for show lacp system-id"""

    schema = {
        'system_id_mac': str,
        'system_priority': int,
    }


class ShowLacpSystemId(ShowLacpSystemIdSchema):
    """Parser for show lacp system-id"""

    cli_command = 'show lacp system-id'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}
        # Priority  MAC Address
        # --------  -----------------
        #   0x0064  00-1b-0c-10-5a-26
        p1 = re.compile(r'^(?P<system_priority>[\w]+) +(?P<system_id_mac>[\w\.\-]+)$')

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                result_dict.update({'system_priority': int(group['system_priority'], 0)})
                result_dict.update({'system_id_mac': group['system_id_mac']})
                continue

        return result_dict


class ShowBundleSchema(MetaParser):
    """Schema for show bundle"""

    schema = {
        'interfaces': {
            Any(): {
                'name': str,
                'bundle_id': int,
                'oper_status': str,
                'local_links': {
                    'active': int,
                    'standby': int,
                    'configured': int,
                },
                'local_bandwidth_kbps': {
                    'effective': int,
                    'available': int,
                },
                'mac_address': str,
                'mac_address_source': str,
                Optional('inter_chassis_link'): str,
                'min_active_link': int,
                'min_active_bw_kbps': int,
                'max_active_link': int,
                'wait_while_timer_ms': int,
                Optional('load_balance'): {
                    Optional('load_balance'): str,
                    Optional('link_order_signaling'): str,
                    Optional('hash_type'): str,
                    Optional('locality_threshold'): str,
                },
                'lacp': {
                    'lacp': str,
                    Optional('flap_suppression_timer'): str,
                    Optional('cisco_extensions'): str,
                    Optional('non_revertive'): str,
                },
                'mlacp': {
                    'mlacp': str,
                    Optional('iccp_group'): str,
                    Optional('role'): str,
                    Optional('foreign_links_active'): int,
                    Optional('foreign_links_configured'): int,
                    Optional('switchover_type'): str,
                    Optional('recovery_delay'): str,
                    Optional('maximize_threshold'): str,
                },
                'ipv4_bfd': {
                    'ipv4_bfd': str,
                    Optional('state'): str,
                    Optional('fast_detect'): str,
                    Optional('start_timer'): str,
                    Optional('neighbor_unconfigured_timer'): str,
                    Optional('preferred_min_interval_ms'): int,
                    Optional('preferred_multiple'): int,
                    Optional('destination_address'): str,
                },
                Optional('ipv6_bfd'): {
                    Optional('ipv6_bfd'): str,
                    Optional('state'): str,
                    Optional('fast_detect'): str,
                    Optional('start_timer'): str,
                    Optional('neighbor_unconfigured_timer'): str,
                    Optional('preferred_min_interval_ms'): int,
                    Optional('preferred_multiple'): int,
                    Optional('destination_address'): str,
                },
                'port': {
                    Any(): {
                        'interface': str,
                        'device': str,
                        'state': str,
                        'port_id': str,
                        'bw_kbps': int,
                        Optional('link_state'): str,
                    },
                },
            },
        }
    }


class ShowBundle(ShowBundleSchema):
    """Parser for show bundle"""

    cli_command = 'show bundle'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}

        # Bundle-Ether1
        # Bundle-Ether 2
        p1 = re.compile(r'^Bundle-Ether *(?P<bundle_id>[\d]+)$')

        # Status:  Up
        # Status: mLACP hot standby
        p2 = re.compile(r'^Status: +(?P<oper_status>[\w\s]+)$')

        # Local links <active/standby/configured>:  2 / 0 / 2
        p3 = re.compile(r'^Local +links.*: *(?P<active>[\d]+)'
                         ' *\/ *(?P<standby>[\d]+) *\/ *(?P<configured>[\d]+)$')

        # Local bandwidth <effective/available>:  2000000 (2000000) kbps
        # Local bandwidth <effective/available>:  100000 / 100000 kbps
        p4 = re.compile(r'^Local +bandwidth.*: *(?P<effective>[\d]+) *(\/ *|\()(?P<available>[\d]+)\)?.*$')

        # MAC address (source):  001b.0c10.5a24 (Chassis pool)
        p5 = re.compile(r'^MAC address.*: *(?P<mac_address>[\w.-]+) +\((?P<mac_address_source>.*)\)$')

        # Inter-chassis link:  No
        p6 = re.compile(r'^Inter-chassis +link: *(?P<inter_chassis_link>[\w]+)$')

        # Minimum active links / bandwidth:  1 / 1 kbps
        p7 = re.compile(r'^Minimum +active +links.*: *(?P<min_active_link>[\d]+)'
                         ' *\/ *(?P<min_active_bw_kbps>[\d]+).*$')

        # Maximum active links:  8
        # Maximum active links:  32 (from partner)
        p8 = re.compile(r'^Maximum +active +links: *(?P<max_active_link>[\d]+).*$')

        # Wait while timer:  2000 ms
        # Wait-while timer:  2000 ms
        p9 = re.compile(r'^Wait( +|-)while +timer: *(?P<wait_while_timer_ms>[\d]+).*$')

        # Load balancing:
        # Load-balancing:  Default
        p10 = re.compile(r'^Load( +|-)balancing: *(?P<load_balance>[\w]+)$')

        # Link order signaling:  Not configured
        p10_1 = re.compile(r'^Link +order +signaling: *(?P<link_order_signaling>[\w\s]+)$')

        # Hash type:  Default
        # Hash type:  Src-IP
        p10_2 = re.compile(r'^Hash +type: *(?P<hash_type>[\S]+)$')

        # Locality threshold:  None
        p10_3 = re.compile(r'^Locality +threshold: *(?P<locality_threshold>[\w]+)$')

        # LACP:  Operational
        p11 = re.compile(r'^LACP: *(?P<lacp>[\w]+)$')

        # Flap suppression timer:  Off
        # Flap suppression timer:  2500 ms
        p11_1 = re.compile(r'^Flap +suppression +timer: *(?P<flap_suppression_timer>[\w\s]+)$')

        # Cisco extensions:  Disabled
        p11_2 = re.compile(r'^Cisco +extensions: *(?P<cisco_extensions>[\w]+)$')

        # Non-revertive:  Disabled
        p11_3 = re.compile(r'^Non-revertive: *(?P<non_revertive>[\w]+)$')

        # mLACP:  Not configured
        p12 = re.compile(r'^mLACP: *(?P<mlacp>[\w\s]+)$')

        # Interchassis group:  3
        # ICCP group:  1
        p12_1 = re.compile(r'^(Interchassis|ICCP) +group: *(?P<iccp_group>[\w\s]+)$')

        # Role: Active
        p12_2 = re.compile(r'^Role: *(?P<role>[\w]+)$')

        # Foreign links <active/configured>:  1 / 1
        p12_3 = re.compile(r'^Foreign +links.*: *(?P<foreign_links_active>[\d]+)'
                            ' *\/ *(?P<foreign_links_configured>[\d]+)$')

        # Switchover type:  Revertive
        p12_4 = re.compile(r'^Switchover +type: *(?P<switchover_type>[\w\s\-]+)$')

        # Recovery delay:  300 s
        p12_5 = re.compile(r'^Recovery delay: *(?P<recovery_delay>[\w\s]+)$')

        # Maximize threshold: 2 links
        p12_6 = re.compile(r'^Maximize +threshold: *(?P<maximize_threshold>[\w\s]+)$')

        # IPv4 BFD:  Not configured
        # IPv6 BFD:  Not configured
        p13 = re.compile(r'^(?P<type>[\w]+) +BFD: *(?P<ip_bfd>[\w\s]+)$')

        # State:   Off
        p13_1 = re.compile(r'^State: *(?P<state>[\w]+)$')

        # Fast detect:  Enabled
        p13_2 = re.compile(r'^Fast +detect: *(?P<fast_detect>[\w]+)$')

        # Start timer:  Off
        p13_3 = re.compile(r'^Start +timer: *(?P<start_timer>[\w\s]+)$')

        # Neighbor-unconfigured timer:   Off
        p13_4 = re.compile(r'^Neighbor-unconfigured +timer: *(?P<neighbor_unconfigured_timer>[\w\s]+)$')

        # Preferred min interval:    150 ms
        p13_5 = re.compile(r'^Preferred +min +interval: *(?P<preferred_min_interval_ms>[\d]+).*$')

        # Preferred multiple:   3
        p13_6 = re.compile(r'^Preferred +multiple: *(?P<preferred_multiple>[\d]+)$')

        # Destination address:  Not Configured
        p13_7 = re.compile(r'^Destination +address: *(?P<destination_address>[\w\s\.]+)$')

        # Port                  Device           State        Port ID         B/W, kbps
        # Gi0/0/0/0             Local            Active       0x000a, 0x0001     1000000
        p14 = re.compile(r'^(?P<interface>[\S]+) +(?P<device>[\S]+) +(?P<state>[\w]+)'
                          ' +(?P<port_id>[\w]+, *[\w]+) +(?P<bw_kbps>[\d]+)$')

        # Link is Active
        # Link is Standby due to maximum-active links configuration
        p15 = re.compile(r'^Link +is +(?P<link_state>.*)$')

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            # Bundle-Ether1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = m.group()
                bundle_dict = result_dict.setdefault('interfaces', {}).setdefault(name, {})
                bundle_dict.update({'name': name})
                bundle_dict.update({'bundle_id': int(group['bundle_id'])})
                continue

            # Status:  Up
            m = p2.match(line)
            if m:
                group = m.groupdict()
                bundle_dict.update({'oper_status': group['oper_status'].lower()})
                continue

            # Local links <active/standby/configured>:  2 / 0 / 2
            m = p3.match(line)
            if m:
                group = m.groupdict()
                local_dict = bundle_dict.setdefault('local_links', {})
                local_dict.update({k: int(v) for k, v in group.items()})
                continue

            # Local bandwidth <effective/available>:  2000000 (2000000) kbps
            m = p4.match(line)
            if m:
                group = m.groupdict()
                bw_dict = bundle_dict.setdefault('local_bandwidth_kbps', {})
                bw_dict.update({k: int(v) for k, v in group.items()})
                continue

            # MAC address (source):  001b.0c10.5a24 (Chassis pool)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                bundle_dict.update({'mac_address': group['mac_address']})
                bundle_dict.update({'mac_address_source': \
                        Common.convert_intf_name(group['mac_address_source'])})
                continue

            # Inter-chassis link:  No
            m = p6.match(line)
            if m:
                group = m.groupdict()
                bundle_dict.update({'inter_chassis_link': group['inter_chassis_link']})
                continue

            # Minimum active links / bandwidth:  1 / 1 kbps
            m = p7.match(line)
            if m:
                group = m.groupdict()
                bundle_dict.update({k: int(v) for k, v in group.items()})
                continue

            # Maximum active links:  8
            m = p8.match(line)
            if m:
                group = m.groupdict()
                bundle_dict.update({'max_active_link': int(group['max_active_link'])})
                continue

            # Wait while timer:  2000 ms
            m = p9.match(line)
            if m:
                group = m.groupdict()
                bundle_dict.update({'wait_while_timer_ms': int(group['wait_while_timer_ms'])})
                continue

            # Load balancing:
            # Load-balancing:  Default
            m = p10.match(line)
            if m:
                group = m.groupdict()
                lb_dict = bundle_dict.setdefault('load_balance', {})
                lb_dict.update({'load_balance': group['load_balance']})
                continue

            # Link order signaling:  Not configured
            m = p10_1.match(line)
            if m:
                group = m.groupdict()
                lb_dict = bundle_dict.setdefault('load_balance', {})
                lb_dict.update({'link_order_signaling': group['link_order_signaling']})
                continue

            # Hash type:  Default
            # Hash type:  Src-IP
            m = p10_2.match(line)
            if m:
                group = m.groupdict()
                lb_dict.update({'hash_type': group['hash_type']})
                continue

            # Locality threshold:  None
            m = p10_3.match(line)
            if m:
                group = m.groupdict()
                lb_dict.update({'locality_threshold': group['locality_threshold']})
                continue

            # LACP:  Operational
            m = p11.match(line)
            if m:
                group = m.groupdict()
                lacp_dict = bundle_dict.setdefault('lacp', {})
                lacp_dict.update({'lacp': group['lacp']})
                continue

            # Flap suppression timer:  Off
            m = p11_1.match(line)
            if m:
                group = m.groupdict()
                lacp_dict.update({'flap_suppression_timer': group['flap_suppression_timer']})
                continue

            # Cisco extensions:  Disabled
            m = p11_2.match(line)
            if m:
                group = m.groupdict()
                lacp_dict.update({'cisco_extensions': group['cisco_extensions']})
                continue

            # Non-revertive:  Disabled
            m = p11_3.match(line)
            if m:
                group = m.groupdict()
                lacp_dict.update({'non_revertive': group['non_revertive']})
                continue

            # mLACP:  Not configured
            m = p12.match(line)
            if m:
                group = m.groupdict()
                mlacp_dict = bundle_dict.setdefault('mlacp', {})
                mlacp_dict.update({'mlacp': group['mlacp']})
                continue

            # Interchassis group:  3
            # ICCP group:  1
            m = p12_1.match(line)
            if m:
                group = m.groupdict()
                mlacp_dict.update({'iccp_group': group['iccp_group']})
                continue

            # Role: Active
            m = p12_2.match(line)
            if m:
                group = m.groupdict()
                mlacp_dict.update({'role': group['role']})
                continue

            # Foreign links <active/configured>:  1 / 1
            m = p12_3.match(line)
            if m:
                group = m.groupdict()
                mlacp_dict.update({k : int(v) for k, v in group.items()})
                continue

            # Switchover type:  Revertive
            m = p12_4.match(line)
            if m:
                group = m.groupdict()
                mlacp_dict.update({'switchover_type': group['switchover_type']})
                continue

            # Recovery delay:  300 s
            m = p12_5.match(line)
            if m:
                group = m.groupdict()
                mlacp_dict.update({'recovery_delay': group['recovery_delay']})
                continue

            # Maximize threshold: 2 links
            m = p12_6.match(line)
            if m:
                group = m.groupdict()
                mlacp_dict.update({'maximize_threshold': group['maximize_threshold']})
                continue

            # IPv4 BFD:  Not configured
            # IPv6 BFD:  Not operational
            m = p13.match(line)
            if m:
                group = m.groupdict()
                bfd_type = group['type'].lower() + '_bfd'
                bfd_dict = bundle_dict.setdefault(bfd_type, {})
                bfd_dict.update({bfd_type: group['ip_bfd']})
                continue

            # State:   Off
            p13_1 = re.compile(r'^State: *(?P<state>[\w]+)$')
            m = p13_1.match(line)
            if m:
                group = m.groupdict()
                bfd_dict.update({'state': group['state']})
                continue

            # Fast detect:  Enabled
            p13_2 = re.compile(r'^Fast +detect: *(?P<fast_detect>[\w]+)$')
            m = p13_2.match(line)
            if m:
                group = m.groupdict()
                bfd_dict.update({'fast_detect': group['fast_detect']})
                continue

            # Start timer:  Off
            p13_3 = re.compile(r'^Start +timer: *(?P<start_timer>[\w\s]+)$')
            m = p13_3.match(line)
            if m:
                group = m.groupdict()
                bfd_dict.update({'start_timer': group['start_timer']})
                continue

            # Neighbor-unconfigured timer:   Off
            p13_4 = re.compile(r'^Neighbor-unconfigured +timer: *(?P<neighbor_unconfigured_timer>[\w\s]+)$')
            m = p13_4.match(line)
            if m:
                group = m.groupdict()
                bfd_dict.update({'neighbor_unconfigured_timer': group['neighbor_unconfigured_timer']})
                continue

            # Preferred min interval:    150 ms
            p13_5 = re.compile(r'^Preferred +min +interval: *(?P<preferred_min_interval_ms>[\d]+).*$')
            m = p13_5.match(line)
            if m:
                group = m.groupdict()
                bfd_dict.update({'preferred_min_interval_ms': int(group['preferred_min_interval_ms'])})
                continue

            # Preferred multiple:   3
            p13_6 = re.compile(r'^Preferred +multiple: *(?P<preferred_multiple>[\d]+)$')
            m = p13_6.match(line)
            if m:
                group = m.groupdict()
                bfd_dict.update({'preferred_multiple': int(group['preferred_multiple'])})
                continue

            # Destination address:  Not Configured
            p13_7 = re.compile(r'^Destination +address: *(?P<destination_address>[\w\s\.]+)$')
            m = p13_7.match(line)
            if m:
                group = m.groupdict()
                bfd_dict.update({'destination_address': group['destination_address']})
                continue

            # Port                  Device           State        Port ID         B/W, kbps
            # Gi0/0/0/0             Local            Active       0x000a, 0x0001     1000000
            m = p14.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group.pop('interface'))
                bw_kbps = int(group.pop('bw_kbps'))
                port_dict = bundle_dict.setdefault('port', {}).setdefault(interface, {})
                port_dict.update({'interface': interface})
                port_dict.update({'bw_kbps': bw_kbps})
                port_dict.update({k : v for k, v in group.items()})
                continue

            # Link is Active
            # Link is Standby due to maximum-active links configuration
            m = p15.match(line)
            if m:
                group = m.groupdict()
                port_dict.update({'link_state': group['link_state']})

        return result_dict


class ShowLacpSchema(MetaParser):
    """Schema for show lacp"""

    schema = {
        'interfaces': {
            Any(): {
                'name': str,
                'bundle_id': int,
                'lacp_mode': str,
                'port': {
                    Any(): {
                        'interface': str,
                        'bundle_id': int,
                        'rate': int,
                        'state': str,
                        'port_id': str,
                        'key': str,
                        'system_id': str,
                        'synchronization': str,
                        'aggregatable': bool,
                        'collecting': bool,
                        'distributing': bool,
                        'partner': {
                            'rate': int,
                            'state': str,
                            'port_id': str,
                            'key': str,
                            'system_id': str,
                            'synchronization': str,
                            'aggregatable': bool,
                            'collecting': bool,
                            'distributing': bool,
                        },
                        'receive': str,
                        'period': str,
                        'selection': str,
                        'mux': str,
                        'a_churn': str,
                        'p_churn': str,
                    },
                },
            },
        }
    }


class ShowLacp(ShowLacpSchema):
    """parser for show lacp"""

    cli_command = 'show lacp'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initialize result dict
        result_dict = {}

        # Bundle-Ether1
        p1 = re.compile(r'^Bundle-Ether(?P<bundle_id>[\d]+)$')

        #   Port          (rate)  State    Port ID       Key    System ID
        #   Gi0/0/0/0        30s  ascdA--- 0x000a,0x0001 0x0001 0x0064,00-1b-0c-10-5a-26
        #    Partner         30s  as--A--- 0x8000,0x0004 0x0002 0x8000,00-0c-86-5e-68-23
        p2 = re.compile(r'^(?P<interface>[\S]+) +(?P<rate>[\d]+)s +(?P<state>[\w-]+)'
                         ' +(?P<port_id>[\w, ]+) +(?P<key>[\w]+)'
                         ' +(?P<system_id>[\w\-, ]+)$')

        #   Port                  Receive    Period Selection  Mux       A Churn P Churn
        #   Gi0/0/0/0             Current    Slow   Selected   Distrib   None    None   
        p3 = re.compile(r'^(?P<interface>[\S]+) +(?P<receive>[\w]+) +(?P<period>[\w]+) +(?P<selection>[\w]+)'
                         ' +(?P<mux>[\w]+) +(?P<a_churn>[\w]+) +(?P<p_churn>[\w]+)$')

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            # Bundle-Ether1 
            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = m.group()
                bundle_dict = result_dict.setdefault('interfaces', {}).setdefault(name, {})
                bundle_dict.update({'name': name})
                bundle_dict.update({'bundle_id': int(group['bundle_id'])})
                continue

            #   Port          (rate)  State    Port ID       Key    System ID
            #   Gi0/0/0/0        30s  ascdA--- 0x000a,0x0001 0x0001 0x0064,00-1b-0c-10-5a-26
            #    Partner         30s  as--A--- 0x8000,0x0004 0x0002 0x8000,00-0c-86-5e-68-23
            m = p2.match(line)
            if m:
                group = m.groupdict()
                state = group['state']
                if not group['interface'] == 'Partner':
                    interface = Common.convert_intf_name(group['interface'])
                    sub_dict = bundle_dict.setdefault('port', {}).setdefault(interface, {})
                    sub_dict.update({'interface': interface})
                    sub_dict.update({'bundle_id': bundle_dict.get('bundle_id')})
                    bundle_dict.update({'lacp_mode': 'active' if "A" in state else 'passive'})
                else:
                    sub_dict = bundle_dict.setdefault('port', {}).setdefault(interface, {}).setdefault('partner', {})
                sub_dict.update({'rate': int(group['rate'])})
                sub_dict.update({'state': state})
                sub_dict.update({'port_id': group['port_id']})
                sub_dict.update({'key': group['key']})
                sub_dict.update({'system_id': group['system_id']})
                sub_dict.update({'aggregatable': True if 'a' in state else False})
                sub_dict.update({'synchronization': 'in_sync' if 's' in state else 'out_sync'})
                sub_dict.update({'collecting': True if 'c' in state else False})
                sub_dict.update({'distributing': True if 'd' in state else False})
                continue

            #   Port                  Receive    Period Selection  Mux       A Churn P Churn
            #   Gi0/0/0/0             Current    Slow   Selected   Distrib   None    None
            m = p3.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group['interface'])
                port_dict = bundle_dict.setdefault('port', {}).setdefault(interface, {})
                port_dict.update({'interface': interface})
                port_dict.update({'receive': group['receive']})
                port_dict.update({'period': group['period']})
                port_dict.update({'selection': group['selection']})
                port_dict.update({'mux': group['mux']})
                port_dict.update({'a_churn': group['a_churn']})
                port_dict.update({'p_churn': group['p_churn']})
                continue

        return result_dict

