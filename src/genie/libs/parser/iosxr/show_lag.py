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
                'inter_chassis_link': str,
                'min_active_link': int,
                'min_active_bw_kbps': int,
                'max_active_link': int,
                'wait_while_timer_ms': int,
                'load_balance': {
                    'link_order_signaling': str,
                    'hash_type': str,
                    'locality_threshold': str,
                },
                'lacp': {
                    'lacp': str,
                    'flap_suppression_timer': str,
                    'cisco_extensions': str,
                    'non_revertive': str,
                },
                'mlacp': str,
                'ipv4_bfd': str,
                'ipv6_bfd': str,
                'port': {
                    Any(): {
                        'interface': str,
                        'device': str,
                        'state': str,
                        'port_id': str,
                        'bw_kbps': int,
                        'link_state': str,
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
        p1 = re.compile(r'^Bundle-Ether(?P<bundle_id>[\d]+)$')

        # Status:  Up
        p2 = re.compile(r'^Status: +(?P<oper_status>[\w]+)$')

        # Local links <active/standby/configured>:  2 / 0 / 2
        p3 = re.compile(r'^Local +links.*: *(?P<active>[\d]+)'
                        ' *\/ *(?P<standby>[\d]+) *\/ *(?P<configured>[\d]+)$')

        # Local bandwidth <effective/available>:  2000000 (2000000) kbps
        p4 = re.compile(r'^Local +bandwidth.*: *(?P<effective>[\d]+) *\((?P<available>[\d]+)\).*$')

        # MAC address (source):  001b.0c10.5a24 (Chassis pool)
        p5 = re.compile(r'^MAC address.*: *(?P<mac_address>[\w.-]+) +\((?P<mac_address_source>.*)\)$')

        # Inter-chassis link:  No
        p6 = re.compile(r'^Inter-chassis +link: *(?P<inter_chassis_link>[\w]+)$')

        # Minimum active links / bandwidth:  1 / 1 kbps
        p7 = re.compile(r'^Minimum +active +links.*: *(?P<min_active_link>[\d]+)'
                        ' *\/ *(?P<min_active_bw_kbps>[\d]+).*$')

        # Maximum active links:  8
        p8 = re.compile(r'^Maximum +active +links: *(?P<max_active_link>[\d]+)$')

        # Wait while timer:  2000 ms
        p9 = re.compile(r'^Wait +while +timer: *(?P<wait_while_timer_ms>[\d]+).*$')

        # Load balancing:
        # Link order signaling:  Not configured
        p10 = re.compile(r'^Link +order +signaling: *(?P<link_order_signaling>[\w\s]+)$')

        # Hash type:  Default
        p11 = re.compile(r'^Hash +type: *(?P<hash_type>[\w]+)$')

        # Locality threshold:  None
        p12 = re.compile(r'^Locality +threshold: *(?P<locality_threshold>[\w]+)$')

        # LACP:  Operational
        p13 = re.compile(r'^LACP: *(?P<lacp>[\w]+)$')

        # Flap suppression timer:  Off
        p14 = re.compile(r'^Flap +suppression +timer: *(?P<flap_suppression_timer>[\w]+)$')

        # Cisco extensions:  Disabled
        p15 = re.compile(r'^Cisco +extensions: *(?P<cisco_extensions>[\w]+)$')

        # Non-revertive:  Disabled
        p16 = re.compile(r'^Non-revertive: *(?P<non_revertive>[\w]+)$')

        # mLACP:  Not configured
        p17 = re.compile(r'^mLACP: *(?P<mlacp>[\w\s]+)$')

        # IPv4 BFD:  Not configured
        # IPv6 BFD:  Not configured
        p18 = re.compile(r'^(?P<type>[\w]+) +BFD: *(?P<ip_bfd>[\w\s]+)$')

        # Port                  Device           State        Port ID         B/W, kbps
        # Gi0/0/0/0             Local            Active       0x000a, 0x0001     1000000
        p19 = re.compile(r'^(?P<interface>[\S]+) +(?P<device>[\w]+) +(?P<state>[\w]+)'
                         ' +(?P<port_id>[\w]+, *[\w]+) +(?P<bw_kbps>[\d]+)')

        # Link is Active
        # Link is Standby due to maximum-active links configuration
        p20 = re.compile(r'^Link +is +(?P<link_state>[\S]+).*$')

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
                bundle_dict.update({'mac_address_source': group['mac_address_source']})
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
            # Link order signaling:  Not configured
            m = p10.match(line)
            if m:
                group = m.groupdict()
                lb_dict = bundle_dict.setdefault('load_balance', {})
                lb_dict.update({'link_order_signaling': group['link_order_signaling']})
                continue

            # Hash type:  Default
            m = p11.match(line)
            if m:
                group = m.groupdict()
                lb_dict.update({'hash_type': group['hash_type']})
                continue

            # Locality threshold:  None
            m = p12.match(line)
            if m:
                group = m.groupdict()
                lb_dict.update({'locality_threshold': group['locality_threshold']})
                continue

            # LACP:  Operational
            m = p13.match(line)
            if m:
                group = m.groupdict()
                lacp_dict = bundle_dict.setdefault('lacp', {})
                lacp_dict.update({'lacp': group['lacp']})
                continue

            # Flap suppression timer:  Off
            m = p14.match(line)
            if m:
                group = m.groupdict()
                lacp_dict.update({'flap_suppression_timer': group['flap_suppression_timer']})
                continue

            # Cisco extensions:  Disabled
            m = p15.match(line)
            if m:
                group = m.groupdict()
                lacp_dict.update({'cisco_extensions': group['cisco_extensions']})
                continue

            # Non-revertive:  Disabled
            m = p16.match(line)
            if m:
                group = m.groupdict()
                lacp_dict.update({'non_revertive': group['non_revertive']})
                continue

            # mLACP:  Not configured
            m = p17.match(line)
            if m:
                group = m.groupdict()
                bundle_dict.update({'mlacp': group['mlacp']})
                continue

            # IPv4 BFD:  Not configured
            # IPv6 BFD:  Not configured
            m = p18.match(line)
            if m:
                group = m.groupdict()
                bundle_dict.update({'ipv4_bfd': group['ip_bfd']})
                bundle_dict.update({'ipv6_bfd': group['ip_bfd']})
                continue

                


            # Port                  Device           State        Port ID         B/W, kbps
            # Gi0/0/0/0             Local            Active       0x000a, 0x0001     1000000
            m = p19.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group['interface'])
                port_dict = bundle_dict.setdefault('port', {}).setdefault(interface, {})
                port_dict.update({'interface': interface})
                port_dict.update({'device': group['device']})
                port_dict.update({'state': group['state']})
                port_dict.update({'port_id': group['port_id']})
                port_dict.update({'bw_kbps': int(group['bw_kbps'])})
                continue

            # Link is Active
            # Link is Standby due to maximum-active links configuration
            p20 = re.compile(r'^Link +is +(?P<link_state>[\S]+).*$')
            m = p20.match(line)
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
                'port': {
                    Any(): {
                        'interface': str,
                        'rate': int,
                        'state': str,
                        'port_id': str,
                        'key': int,
                        'system_id': str,
                        'synchronization': str,
                        'aggregatable': bool,
                        'collecting': bool,
                        'distributing': bool,
                        'partner': {
                            'rate': int,
                            'state': str,
                            'port_id': str,
                            'key': int,
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
                else:
                    sub_dict = bundle_dict.setdefault('port', {}).setdefault(interface, {}).setdefault('partner', {})
                sub_dict.update({'rate': int(group['rate'])})
                sub_dict.update({'state': state})
                sub_dict.update({'port_id': group['port_id']})
                sub_dict.update({'key': int(group['key'], 0)})
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
