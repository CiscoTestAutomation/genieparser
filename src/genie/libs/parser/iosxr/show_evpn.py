""" show_evpn.py

show evpn parser class
show evpn ethernet-segment
show evpn ethernet-segment detail
show evpn ethernet-segment private
show evpn ethernet-segment esi {esi} detail
"""

from ipaddress import ip_address
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

from genie.libs.parser.utils.common import Common

re_8bit_u = r'(?:' + r'|'.join([
    r'[0-9]',
    r'[1-9][0-9]',
    r'1[0-9][0-9]',
    r'2[0-4][0-9]',
    r'25[0-5]',
]) + r')'
re_8bit_x = r'(?:[A-Fa-f0-9]{1,2})'
re_8bit_02x = r'(?:[A-Fa-f0-9]{2})'
re_16bit_x = r'(?:[A-Fa-f0-9]{1,4})'
re_16bit_04x = r'(?:[A-Fa-f0-9]{4})'
re_mac = r'(?:' + r'|'.join([
    r'\.'.join([re_16bit_x] * 3),
    r':'.join([re_8bit_x] * 6),
    r'-'.join([re_8bit_x] * 6),
    r'\.'.join([re_8bit_x] * 6),
]) + r')'
re_ipv4 = r'(?:' + r'\.'.join([re_8bit_u] * 4) + r')'
re_ipv6 = r'(?:[A-Fa-f0-9:]*:[A-Fa-f0-9:]*(?::' + re_ipv4 + ')?)'
re_ip = r'(?:' + r'|'.join([re_ipv4, re_ipv6]) + ')'
re_label_str = r'(?:' + r'|'.join([
    r'[0-9]+',
    r'[A-Za-z0-9-]+',  # See mpls_label_strings @ mpls/base/include/mpls_label_defs_extra.h
]) + r')'


class ShowEvpnEviSchema(MetaParser):
    schema = {
        'evi': {
            Any(): {
                'bridge_domain': str,
                'type': str,
                Optional('route_target_in_use'): {
                    Any(): {
                        Any(): bool
                    }
                },
                Optional(Any()): str,
            }
        }
    }

class ShowEvpnEvi(ShowEvpnEviSchema):
    """Parser class for 'show evpn evi'"""

    cli_command = 'show evpn evi'
    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        ret_dict = {}
        # 1000  VPWS:1000       VPWS (vlan-unaware)
        # 2000  XC-POD1-EVPN    EVPN
        # 2001  XC-POD2-EVPN    EVPN
        p1 = re.compile(r'^(?P<evi>\d+) +(?P<bridge_domain>\S+) +(?P<type>.+)$')

        # 100:145                        Import 
        # 100:145                        Export 
        p2 = re.compile(r'^(?P<route_target_in_use>[\d+:\d+]+) +(?P<type>\S+)$')

        # ------------------------------ -------
        p3 = re.compile(r'(-+ *)+$')

        # Unicast Label  : 24001
        # Multicast Label: 16001
        # RD Auto  : (auto) 1.100.100.100:145
        p4 = re.compile(r'^(?P<key>[\S ]+) *: +(?P<value>[\S ]+)$')

        for line in out.splitlines():
            line = line.strip()

            # 1000  VPWS:1000       VPWS (vlan-unaware)
            # 2000  XC-POD1-EVPN    EVPN
            # 2001  XC-POD2-EVPN    EVPN
            m = p1.match(line)
            if m:
                group = m.groupdict()
                evi = int(group['evi'])
                bridge_domain = group['bridge_domain']
                evi_type = group['type']
                evi_dict = ret_dict.setdefault('evi', {}). \
                    setdefault(evi, {})
                evi_dict.update({'bridge_domain': bridge_domain})
                evi_dict.update({'type': evi_type})
                continue
            
            # 100:145                        Import 
            # 100:145                        Export 
            m = p2.match(line)
            if m:
                group = m.groupdict()
                route_target_in_use = group['route_target_in_use']
                route_type = group['type']
                type_dict = evi_dict.setdefault('route_target_in_use', {}). \
                    setdefault(route_target_in_use, {})
                type_dict.update({route_type.lower(): True})
                continue
            
            # ------------------------------ -------
            m = p3.match(line)
            if m:
                continue

            # Unicast Label  : 24001
            # Multicast Label: 16001
            # RD Auto  : (auto) 1.100.100.100:145
            m = p4.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].strip().lower().replace(' ', '_')
                value = group['value'].strip()
                evi_dict.update({key: value})
                continue
            
        return ret_dict

class ShowEvpnEviDetail(ShowEvpnEvi):
    """Parser class for 'show evpn evi detail' CLI."""

    cli_command = 'show evpn evi detail'
    def cli(self, output=None):
        """parsing mechanism: cli
        """
        
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        return super().cli(output=output)


class ShowEvpnEviMac(MetaParser):
    """Parser class for 'show evpn evi mac' CLI."""
    exclude = ['entries']

    # TODO schema

    def __init__(self, mac=None, vpn_id=None, private=False, **kwargs):
        self.mac = mac
        self.private = private
        self.vpn_id = vpn_id
        super().__init__(**kwargs)

    cli_command = ['show evpn evi vpn-id {vpn_id} mac','show evpn evi mac']
    def cli(self):

        if self.vpn_id is not None:
            cmd = self.cli_command[0].format(vpn_id=self.vpn_id)
        else:
            cmd = self.cli_command[1]

        if self.mac:
            cmd += ' {mac}'.format(self.mac)
        if self.private:
            cmd += ' private'.format()

        out = self.device.execute(cmd)

        result = {
            'entries': [],
        }

        entry = None
        for line in out.splitlines():
            line = line.rstrip()

            # EVI        MAC address    IP address                               Nexthop                                 Label
            # ---------- -------------- ---------------------------------------- --------------------------------------- --------

            # 65535      02e5.7847.6000 ::                                       Local                                   0
            # 1          0000.0000.0001 ::                                       No remote pathlist
            m = re.match(r'^(?P<evi>[0-9]+)'
                         r' +(?P<mac>' + re_mac + ')'
                         r' +(?P<ip>' + re_ip + ')'
                         r'(?: +No remote pathlist|'
                         r' +(?P<next_hop>\S+)'
                         r' +(?:(?P<label_int>\d+)|(?P<label_str>' + re_label_str + '))'
                         r')'
                         r'$', line)
            if m:
                entry = {
                    'evi': int(m.group('evi')),
                    'mac': m.group('mac'),
                    'ip': ip_address(m.group('ip')),
                    'next_hop': m.group('next_hop'),
                    'label': m.group('label_str') \
                    or (m.group('label_int') and int(m.group('label_int'))),
                }
                try:
                    entry['next_hop'] = ip_address(entry['next_hop'])
                except (TypeError, ValueError):
                    pass
                result['entries'].append(entry)
                continue

            # OLD

            # MAC address    Nexthop                                 Label    vpn-id
            # -------------- --------------------------------------- -------- --------

            # 7777.7777.0002 N/A                                     24005    7
            m = re.match(r'^(?P<mac>' + re_mac + ')'
                         r' +(?:N/A|(?P<ip>' + re_ip + ')|(?P<next_hop>\S+))'
                         r' +(?:(?P<label_int>\d+)|(?P<label_str>' + re_label_str + '))'
                         r' +(?P<evi>[0-9]+)'
                         r'$', line)
            if m:
                entry = {
                    'mac': m.group('mac'),
                    'ip': m.group('ip') and ip_address(m.group('ip')),
                    'next_hop': m.group('next_hop'),
                    'label': m.group('label_str') or int(m.group('label_int')),
                    'evi': int(m.group('evi')),
                }
                try:
                    entry['label'] = int(entry['label'])
                except ValueError:
                    pass
                result['entries'].append(entry)
                continue

            if entry and self.private:
                #EVI        MAC address    IP address                               Nexthop                                 Label
                #---------- -------------- ---------------------------------------- --------------------------------------- --------
                #1          fc00.0001.0002 ::                                       Bundle-Ether1.0                         28100
                #   Ethernet Tag                            : 0
                #   Multi-paths Resolved                    : False
                #   Static                                  : No
                #   Local Ethernet Segment                  : 0001.2222.2222.2200.000a
                #   Remote Ethernet Segment                 : 0000.0000.0000.0000.0000
                #   Local Sequence Number                   : 0
                #   Remote Sequence Number                  : 0
                #   Encapsulation                           : N/A
                #   ESI Port Key                            : 1
                #   Source                                  : Local
                #   Multi-paths Local Label                 : 0
                #   SOO Nexthop                             : ::
                #   BP IFH                                  : 0x152
                #   MAC State                               : Local
                #
                #   Object: EVPN MAC
                #   Base info: version=0xdbdb0008, flags=0x4100, type=8, reserved=0
                #   EVPN MAC event history  [Num events: 3]
                #   ----------------------------------------------------------------------------
                #     Time                Event                         Flags      Flags
                #     ====                =====                         =====      =====
                #     Dec  7 01:46:49.088 Create                        00000000, 00000000 -  -
                #     Dec  7 01:46:49.088 Advertise to BGP              00204110, 00000000 -  -
                #     Dec  7 01:46:49.088 Ignore BGP update             00000000, 00000000 -  -
                #   ----------------------------------------------------------------------------
                #65535      02a0.0964.e800 ::                                       Local                                   0
                #   Ethernet Tag                            : 0
                #   Multi-paths Resolved                    : False
                #   Static                                  : No
                #   Local Ethernet Segment                  : 0000.0000.0000.0000.0000
                #   Remote Ethernet Segment                 : 0000.0000.0000.0000.0000
                #   Local Sequence Number                   : 0
                #   Remote Sequence Number                  : 0
                #   Encapsulation                           : N/A
                #   ESI Port Key                            : 0
                #   Source                                  : Local
                #   Multi-paths Local Label                 : 0
                #   SOO Nexthop                             : ::
                #   BP IFH                                  : 0x0
                #   MAC State                               : Local
                #
                #   Object: EVPN MAC
                #   Base info: version=0xdbdb0008, flags=0xc100, type=8, reserved=0
                #   EVPN MAC event history  [Num events: 13]
                #   ----------------------------------------------------------------------------
                #     Time                Event                         Flags      Flags
                #     ====                =====                         =====      =====
                #     Dec  7 01:41:11.168 Create                        00000000, 00000000 -  -
                #     Dec  7 01:41:11.168 MAC advertise rejected        00000000, 00000000 -  -
                #     Dec  7 01:41:11.168 Withdraw from BGP;filtered    0000c000, 00000000 -  -
                #     Dec  7 01:41:11.168 Modify Redundant              00000000, 00000000 -  -
                #     Dec  7 01:45:25.632 Replay EVI to BGP             00000000, 00000000 -  -
                #     Dec  7 01:45:25.632 MAC advertise rejected        00000000, 00000000 -  -
                #     Dec  7 01:45:25.632 Withdraw from BGP;filtered    0000c100, 00000000 -  -
                #     Dec  7 01:45:25.632 Replay EVI to BGP             00000000, 00000000 -  -
                #     Dec  7 01:45:25.632 MAC advertise rejected        00000000, 00000000 -  -
                #     Dec  7 01:45:25.632 Withdraw from BGP             0040c110, 00000000 -  -
                #     Dec  7 01:46:04.032 Replay EVI to BGP             00000000, 00000000 -  -
                #     Dec  7 01:46:04.032 MAC advertise rejected        00000000, 00000000 -  -
                #     Dec  7 01:46:04.032 Withdraw from BGP             0040c110, 00000000 -  -
                #   ----------------------------------------------------------------------------

                m = re.match(r'^ +Ethernet Tag *: +(?P<eth_tag>[0-9]+)$|'
                             r'^ +Multi-paths Resolved *: +(?P<multipath_resolved>(True|False))$|'
                             r'^ +Static *: +(?P<is_static>(Yes|No))$|'
                             r'^ +Local Ethernet Segment *: +(?P<local_esi>[A-Za-z0-9]{4}\.[A-Za-z0-9]{4}\.[A-Za-z0-9]{4}\.[A-Za-z0-9]{4}\.[A-Za-z0-9]{4})$|'
                             r'^ +Remote Ethernet Segment *: +(?P<remote_esi>[A-Za-z0-9]{4}\.[A-Za-z0-9]{4}\.[A-Za-z0-9]{4}\.[A-Za-z0-9]{4}\.[A-Za-z0-9]{4})$|'
                             r'^ +Local Sequence Number *: +(?P<local_seq_no>[0-9]+)$|'
                             r'^ +Remote Sequence Number *: +(?P<remote_seq_no>[0-9]+)$|'
                             r'^ +Encapsulation *: +(?P<encapsulation>\S+)$|'
                             r'^ +Local Encapsulation *: +(?P<encapsulation_local>\S+)$|'
                             r'^ +Remote Encapsulation *: +(?P<encapsulation_remote>\S+)$|'
                             r'^ +ESI Port Key *: +(?P<esi_port_key>[0-9]+)$|'
                             r'^ +Source *: +(?P<source>\S+)$|'
                             r'^ +Multi-paths Local Label *: +(?P<multipath_label>[0-9]+)$|'
                             r'^ +SOO Nexthop *: +(?P<remote_soo>\S+)$|'
                             r'^ +BP XCID *: +(?P<bp_xcid>0x[A-fa-f0-9]+)$|'
                             r'^ +BP IFH *: +(?P<bp_ifh>0x[A-fa-f0-9]+)$|'
                             r'^ +MAC State *: +(?P<mac_state>\S+)$', line)

                if m:
                    if m.lastgroup != None:
                        if m.lastgroup == 'eth_tag':
                            entry[m.lastgroup] = int(m.group(m.lastgroup))
                        elif m.lastgroup == 'multipath_resolved':
                            if m.group(m.lastgroup) == 'True':
                                entry[m.lastgroup] = True
                            elif m.group(m.lastgroup) == 'False':
                                entry[m.lastgroup] = False
                        elif m.lastgroup == 'is_static':
                            if m.group(m.lastgroup) == 'Yes':
                                entry['is_static'] = True
                            elif m.group(m.lastgroup) == 'No':
                                entry['is_static'] = False
                        elif m.lastgroup == 'local_seq_no':
                            entry[m.lastgroup] = int(m.group(m.lastgroup))
                        elif m.lastgroup == 'remote_seq_no':
                            entry[m.lastgroup] = int(m.group(m.lastgroup))
                        elif m.lastgroup == 'esi_port_key':
                            entry[m.lastgroup] = int(m.group(m.lastgroup))
                        elif m.lastgroup == 'source':
                            if m.group(m.lastgroup) == 'Local':
                                entry['is_local'] = True
                                entry['is_remote'] = False
                            elif m.group(m.lastgroup) == 'Remote':
                                entry['is_remote'] = True
                                entry['is_local'] = False
                        elif m.lastgroup == 'multipath_label':
                            entry[m.lastgroup] = int(m.group(m.lastgroup))
                        elif m.lastgroup == 'remote_soo':
                            try:
                                entry[m.lastgroup] = ip_address(m.group(m.lastgroup))
                            except (TypeError, ValueError):
                                pass
                        else:
                            entry[m.lastgroup] = m.group(m.lastgroup)
                    continue

        # Search through the result entries and populate the duplicate macs
        # with our private data
        if self.private:
            for entry in result['entries']:
                if 'eth_tag' not in entry:
                    evi_entry = entry['evi']
                    mac_entry = entry['mac']
                    for copy_entry in result['entries']:
                        if 'eth_tag' in copy_entry and copy_entry['evi'] == evi_entry \
                                                   and copy_entry['mac'] == mac_entry:
                            # Need to copy entry['next'hop'] to set the correct
                            # value again after the update
                            next_hop_copy = entry['next_hop']
                            entry.update(copy_entry)
                            entry['next_hop'] = next_hop_copy
                            continue

        return result


class ShowEvpnEthernetSegment(MetaParser):
    """Parser class for 'show evpn ethernet-segment' CLI."""

    # TODO schema

    def __init__(self, detail=False, private=False, carving=False, esi=None, **kwargs):
        self.esi = esi
        self.detail = detail
        self.private = private
        self.carving = carving
        super().__init__(**kwargs)

    cli_command = ['show evpn ethernet-segment esi {esi}','show evpn ethernet-segment']
    def cli(self):
        """parsing mechanism: cli
        """

        if self.esi:
            cmd = self.cli_command[0].format(esi=self.esi)
        else:
            cmd = self.cli_command[1]

        if self.carving:
            cmd += ' carving'

        if self.private:
            cmd += ' private'
        elif self.detail:
            cmd += ' detail'

        tcl_package_require_caas_parsers()
        kl = tcl_invoke_caas_abstract_parser(
            device=self.device, exec=cmd)

        return kl


class ShowEvpnInternalLabelDetail(MetaParser):

    # TODO schema

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    cli_command = 'show evpn internal-label detail'

    def cli(self,output=None):
        """parsing mechanism: cli
        """
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        res = {
            'entries': [],
        }

        for line in out.splitlines():
            line = line.rstrip()

            # 5     0012.1200.0000.0000.0002                0        24114
            m = re.match(r'^\s*(?P<evi>\d+)\s+'
                          '(?P<esi>[\w.]+)\s+'
                          '(?P<eth_tag>\d+)\s+'
                          '(?P<internal_label>\w+)$',line)

            if m:
                # create new record
                record = { 'evi' : m.group('evi'),
                           'esi' : m.group('esi'),
                           'eth_tag' : m.group('eth_tag'),
                           'internal_label' : m.group('internal_label'),
                           'pathlists' : {
                                'mac' : [],
                                'es_ead' : [],
                                'evi_ead' : [],
                                'summary' : []
                            }
                         }

                res['entries'].append(record)

            # Multi-paths resolved: TRUE
            m = re.match(r'^\s+Multi-paths resolved: '
                          '(?P<mp_resolved>\w+)$',line)

            if m:
                res['entries'][-1]['mp_resolved'] = m.group('mp_resolved')


            # Multi-paths resolved: TRUE (Remote single-active)
            m = re.match(r'^\s+Multi-paths resolved: '
                          '(?P<mp_resolved>\w+) '
                          '\((?P<mp_single_active>.+)\)$',line)

            if m:
                res['entries'][-1]['mp_resolved'] = m.group('mp_resolved')
                res['entries'][-1]['mp_single_active'] = m.group('mp_single_active')

            # MAC     10.70.20.20                              24212
            m = re.match(r'^\s+MAC\s+'
                          '(?P<nexthop>[\d.]+)\s+'
                          '(?P<label>\d+)$',line)

            if m:
                mac_flag = True
                es_ead_flag = False
                evi_ead_flag = False
                summary_flag = False

                res['entries'][-1]['pathlists']['mac'].append(
                    {'nexthop' : m.group('nexthop'),
                     'label' : m.group('label')}
                )

            # EAD/ES  10.10.10.10                              0
            m = re.match(r'^\s+EAD/ES\s+'
                          '(?P<nexthop>[\d.]+)\s+'
                          '(?P<label>\d+)$',line)

            if m:
                mac_flag = False
                es_ead_flag = True
                evi_ead_flag = False
                summary_flag = False

                res['entries'][-1]['pathlists']['es_ead'].append(
                    {'nexthop' : m.group('nexthop'),
                     'label' : m.group('label')}
                )

            # EAD/EVI 10.10.10.10                              24012
            m = re.match(r'^\s+EAD/EVI\s+'
                          '(?P<nexthop>[\d.]+)\s+'
                          '(?P<label>\d+)$',line)

            if m:
                mac_flag = False
                es_ead_flag = False
                evi_ead_flag = True
                summary_flag = False

                res['entries'][-1]['pathlists']['evi_ead'].append(
                    {'nexthop' : m.group('nexthop'),
                     'label' : m.group('label')}
                )

            # Summary 10.70.20.20                              24212
            m = re.match(r'^\s+Summary\s+'
                          '(?P<nexthop>[\d.]+)\s+'
                          '(?P<label>\d+)$',line)

            if m:
                mac_flag = False
                es_ead_flag = False
                evi_ead_flag = False
                summary_flag = True

                res['entries'][-1]['pathlists']['summary'].append(
                    {'nexthop' : m.group('nexthop'),
                     'label' : m.group('label')}
                )

            #         10.70.20.20                              0
            m = re.match(r'^\s+'
                         '(?P<nexthop>[\d.]+)\s+'
                         '(?P<label>\d+)$',line)

            if m:
               if mac_flag:
                   res['entries'][-1]['pathlists']['mac'].append(
                       {'nexthop' : m.group('nexthop'),
                        'label' : m.group('label')}
                   )
               elif es_ead_flag:
                   res['entries'][-1]['pathlists']['es_ead'].append(
                       {'nexthop' : m.group('nexthop'),
                        'label' : m.group('label')}
                   )
               elif evi_ead_flag:
                   res['entries'][-1]['pathlists']['evi_ead'].append(
                       {'nexthop' : m.group('nexthop'),
                        'label' : m.group('label')}
                   )
               elif summary_flag:
                   res['entries'][-1]['pathlists']['summary'].append(
                       {'nexthop' : m.group('nexthop'),
                        'label' : m.group('label')}
                   )

            #         10.10.10.10 (B)                          24012
            m = re.match(r'^\s+'
                         '(?P<nexthop>[\d.]+)\s+'
                         '\((?P<flag>\w+)\)\s+'
                         '(?P<label>\d+)$',line)

            if m:
               res['entries'][-1]['pathlists']['summary'].append(
                   {'nexthop' : m.group('nexthop'),
                    'label' : m.group('label'),
                    'flag' : m.group('flag')}
               )

        return res

# vim: ft=python ts=8 sw=4 et

class ShowEvpnEthernetSegmentSchema(MetaParser):
    schema = {
        'segment_id': {
            Any(): {
                'interface': {
                    Any(): {
                        'next_hops': list,
                        Optional('es_to_bgp_gates'): str,
                        Optional('es_to_l2fib_gates'): str,
                        Optional('main_port'): {
                            'interface': str,
                            Optional('interface_mac'): str,
                            'if_handle': str,
                            'state': str,
                            'redundancy': str,
                        },
                        Optional('esi_type'): int,
                        Optional('value'): str,
                        Optional('es_import_rt'): str,
                        Optional('source_mac'): str,
                        Optional('topology'): {
                            'operational': str,
                            'configured': str,
                        },
                        Optional('primary_services'): str,
                        Optional('secondary_services'): str,
                        Optional('service_carving'): str,
                        Optional('peering_details'): str,
                        Optional('service_carving_results'): {
                            Optional('forwarders'): int,
                            Optional('permanent'): int,
                            Optional('bridge_ports'): {
                                'num_of_total': int,
                            },
                            'elected': {
                                'num_of_total': int,
                                Optional('i_sid_e'): list,
                            },
                            'not_elected': {
                                'num_of_total': int,
                                Optional('i_sid_ne'): list,
                            },
                        },
                        Optional('mac_flushing_mode'): str,
                        Optional('peering_timer'): str,
                        Optional('recovery_timer'): str,
                        Optional('carving_timer'): str,
                        Optional('local_shg_label'): int,
                        Optional('remote_shg_label'): int,
                        Optional('flush_again_timer'): str,
                        Optional('shg_label'): {
                            'num_of_label': int,
                            Any(): {
                                'next_hop': str
                            }
                        }
                    }
                }
            }
        }
    }

class ShowEvpnEthernetSegment(ShowEvpnEthernetSegmentSchema):
    """Parser class for 'show evpn ethernet-segment' CLI."""

    cli_command = 'show evpn ethernet-segment'
    def cli(self, output=None):
        """parsing mechanism: cli
        """
        
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        ret_dict = {}
        num_of_label = {}

        # 0210.0300.9e00.0210.0000 Gi0/3/0/0      1.100.100.100
        p1 = re.compile(r'^(?P<segment_id>\S+) +(?P<interface>\S+) +(?P<next_hop>[\d\.]+)$')

        # 2.100.100.100   
        p1_1 = re.compile(r'^(?P<next_hop>[\d\.]+)$')

        # ES to BGP Gates   : Ready
        p2 = re.compile(r'^ES +to +BGP +Gates +: +(?P<es_to_bgp_gates>\S+)$')

        # ES to L2FIB Gates : Ready
        p3 = re.compile(r'^ES +to +L2FIB +Gates +: +(?P<es_to_l2fib_gates>\S+)$')

        # Interface name : GigabitEthernet0/3/0/0
        p4 = re.compile(r'^Interface name +: +(?P<interface>\S+)$')

        # Interface MAC  : 008a.9644.d8dd
        p4_1 = re.compile(r'^Interface +MAC *: +(?P<interface_mac>[\S ]+)$')

        # IfHandle       : 0x1800300
        p5 = re.compile(r'^IfHandle +: +(?P<if_handle>\S+)$')

        # State          : Up
        p6 = re.compile(r'^State + : +(?P<state>\S+)$')

        # Redundancy     : Not Defined
        p7 = re.compile(r'^Redundancy +: +(?P<redundancy>[\S ]+)$')

        # Source MAC        : 0001.ed9e.0001 (PBB BSA)
        p8 = re.compile(r'^Source +MAC +: +(?P<source_mac>[\S ]+)$')

        # Operational    : MHN
        # Operational    : MH, All-active
        p9 = re.compile(r'^Operational +: +(?P<operational>[\S+ ]+)$')

        # Configured     : A/A per service (default)
        p10 = re.compile(r'^Configured +: +(?P<configured>[\S ]+)$')

        # Primary Services  : Auto-selection
        p11 = re.compile(r'^Primary +Services +: +(?P<primary_services>\S+)$')
        
        # Secondary Services: Auto-selection
        p12 = re.compile(r'^Secondary +Services *: +(?P<secondary_services>\S+)$')

        # Bridge ports   : 3
        p13 = re.compile(r'^Bridge +ports +: +(?P<bridge_ports>\d+)$')

        # Elected        : 0
        p14 = re.compile(r'^Elected +: +(?P<elected>\d+)$')

        # Not Elected    : 3
        p15 = re.compile(r'^Not +Elected +: +(?P<not_elected>\d+)$')

        # I-Sid E  :  1450101, 1650205, 1850309
        p16 = re.compile(r'^I-Sid +E +: +(?P<i_sid_e>[\S ]+)$')

        # I-Sid NE  :  1450101, 1650205, 1850309
        p16_1 = re.compile(r'^I-Sid +NE +: +(?P<i_sid_ne>[\S ]+)$')
        
        # MAC Flushing mode : STP-TCN
        p17 = re.compile(r'^MAC +Flushing +mode +: +(?P<mac_flushing_mode>\S+)$')

        # Peering timer     : 45 sec [not running]
        p18 = re.compile(r'^Peering +timer +: +(?P<peering_timer>[\S ]+)$')

        # Recovery timer    : 20 sec [not running]
        p19 = re.compile(r'^Recovery +timer +: +(?P<recovery_timer>[\S ]+)$')

        # Flushagain timer  : 60 sec
        p20 = re.compile(r'^Flushagain +timer +: +(?P<flush_again_timer>[\S ]+)$')

        # ESI type          : 0
        p21 = re.compile(r'^ESI +type *: +(?P<esi_type>\d+)$')

        # Value          : 36.3700.0000.0000.1100
        p22 = re.compile(r'^Value *: +(?P<value>[\S ]+)$')

        # ES Import RT      : 3637.0000.0000 (from ESI)
        p23 = re.compile(r'^ES +Import +RT *: +(?P<es_import_rt>[\S ]+)$')

        # Service Carving   : Auto-selection
        p24 = re.compile(r'^Service +Carving *: +(?P<service_carving>[\S ]+)$')

        # Peering Details   : 3.3.3.36[MOD:P:00] 3.3.3.37[MOD:P:00]
        p25 = re.compile(r'^Peering +Details *: +(?P<peering_details>[\S ]+)$')

        # Forwarders     : 1
        p26 = re.compile(r'^Forwarders *: +(?P<forwarders>\d+)$')

        # Permanent      : 0
        p27 = re.compile(r'^Permanent *: +(?P<permanent>\d+)$')

        # Carving timer     : 0 sec [not running]
        p28 = re.compile(r'^Carving +timer *: +(?P<carving_timer>[\S ]+)$')

        # Local SHG label   : 64005
        p29 = re.compile(r'^Local +SHG +label *: +(?P<local_shg_label>\d+)$')

        # Remote SHG labels : 1
        p30 = re.compile(r'^Remote +SHG +labels? *: +(?P<remote_shg_label>\d+)$')

        # 64005 : nexthop 3.3.3.37
        p31 = re.compile(r'^(?P<shg_label>\d+) *: +nexthop +(?P<next_hop>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            
            # ES to L2FIB Gates : Ready
            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # ES to L2FIB Gates : Ready
            m = p3.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # Interface name : GigabitEthernet0/3/0/0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                main_port_dict = interface_dict.setdefault('main_port', {})
                main_port_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # Interface MAC  : 008a.9644.d8dd
            m = p4_1.match(line)
            if m:
                group = m.groupdict()
                main_port_dict = interface_dict.setdefault('main_port', {})
                main_port_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # IfHandle       : 0x1800300
            m = p5.match(line)
            if m:
                group = m.groupdict()
                main_port_dict = interface_dict.setdefault('main_port', {})
                main_port_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # State          : Up
            m = p6.match(line)
            if m:
                group = m.groupdict()
                main_port_dict = interface_dict.setdefault('main_port', {})
                main_port_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # Redundancy     : Not Defined
            m = p7.match(line)
            if m:
                group = m.groupdict()
                main_port_dict = interface_dict.setdefault('main_port', {})
                main_port_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # Source MAC        : 0001.ed9e.0001 (PBB BSA)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # Operational    : MHN
            m = p9.match(line)
            if m:
                group = m.groupdict()
                topology_dict = interface_dict.setdefault('topology', {})
                topology_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # Configured     : A/A per service (default)
            m = p10.match(line)
            if m:
                group = m.groupdict()
                topology_dict = interface_dict.setdefault('topology', {})
                topology_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # Primary Services  : Auto-selection
            m = p11.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # Secondary Services: Auto-selection
            m = p12.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # Bridge ports   : 3
            m = p13.match(line)
            if m:
                group = m.groupdict()
                bridge_ports = int(group['bridge_ports'])
                bridge_ports_dict = interface_dict.setdefault('service_carving_results', {}). \
                    setdefault('bridge_ports', {})
                bridge_ports_dict.update({'num_of_total': bridge_ports})
                continue
            
            # Elected        : 0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                elected = int(group['elected'])
                elected_dict = interface_dict.setdefault('service_carving_results', {}). \
                    setdefault('elected', {})
                elected_dict.update({'num_of_total': elected})
                continue
            
            # Not Elected    : 3
            m = p15.match(line)
            if m:
                group = m.groupdict()
                not_elected = int(group['not_elected'])
                not_elected_dict = interface_dict.setdefault('service_carving_results', {}). \
                    setdefault('not_elected', {})
                not_elected_dict.update({'num_of_total': not_elected})
                continue

            # I-Sid E  :  1450101, 1650205, 1850309
            m = p16.match(line)
            if m:
                group = m.groupdict()
                i_sid_e = group['i_sid_e']
                elected_dict.update({'i_sid_e': i_sid_e.replace(' ', '').split(',')})
                continue

            # I-Sid NE  :  1450101, 1650205, 1850309
            m = p16_1.match(line)
            if m:
                group = m.groupdict()
                i_sid_ne = group['i_sid_ne']
                not_elected_dict.update({'i_sid_ne': i_sid_ne.replace(' ', '').split(',')})
                continue

            # MAC Flushing mode : STP-TCN
            m = p17.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # Peering timer     : 45 sec [not running]
            m = p18.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # Recovery timer    : 20 sec [not running]
            m = p19.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # Flushagain timer  : 60 sec
            m = p20.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # ESI type          : 0
            m = p21.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue

            # Value          : 36.3700.0000.0000.1100
            m = p22.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # ES Import RT      : 3637.0000.0000 (from ESI)
            m = p23.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # Service Carving   : Auto-selection
            m = p24.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # Peering Details   : 3.3.3.36[MOD:P:00] 3.3.3.37[MOD:P:00]
            m = p25.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # Forwarders     : 1
            m = p26.match(line)
            if m:
                group = m.groupdict()
                service_carving_results = interface_dict.setdefault('service_carving_results', {})
                service_carving_results.update({k:int(v) for k, v in group.items() if v is not None})
                continue

            # Permanent      : 0
            m = p27.match(line)
            if m:
                group = m.groupdict()
                service_carving_results = interface_dict.setdefault('service_carving_results', {})
                service_carving_results.update({k:int(v) for k, v in group.items() if v is not None})
                continue

            # Carving timer     : 0 sec [not running]
            m = p28.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # Local SHG label   : 64005
            m = p29.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue

            # Remote SHG labels : 1
            m = p30.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue

            # 64005 : nexthop 3.3.3.37
            m = p31.match(line)
            if m:
                group = m.groupdict()
                shg_label = int(group['shg_label'])
                next_hop = group['next_hop']
                next_hop_dict = interface_dict.setdefault('shg_label', {}). \
                    setdefault(shg_label, {})
                next_hop_dict.update({'next_hop': next_hop})
                label_index = num_of_label.get('num_of_label', 0) + 1
                interface_dict.setdefault('shg_label', {}). \
                    update({'num_of_label': label_index})
                continue

            # 0210.0300.9e00.0210.0000 Gi0/3/0/0      1.100.100.100
            m = p1.match(line)
            if m:
                group = m.groupdict()
                segment_id = group['segment_id']
                interface = Common.convert_intf_name(group['interface'])
                next_hop = group['next_hop']
                interface_dict = ret_dict.setdefault('segment_id', {}). \
                    setdefault(segment_id, {}). \
                    setdefault('interface', {}). \
                    setdefault(interface, {})
                next_hop_list = interface_dict.setdefault('next_hops', [next_hop])
                continue
            
            # 2.100.100.100
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                next_hop = group['next_hop']
                next_hop_list.append(next_hop)
                continue

        return ret_dict

class ShowEvpnEthernetSegmentDetail(ShowEvpnEthernetSegment):
    """Parser class for 'show evpn ethernet-segment detail' CLI."""

    cli_command = 'show evpn ethernet-segment detail'
    def cli(self, output=None):
        """parsing mechanism: cli
        """
        
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        return super().cli(output=out)

class ShowEvpnEthernetSegmentPrivate(ShowEvpnEthernetSegment):
    """Parser class for 'show evpn ethernet-segment private' CLI."""

    cli_command = 'show evpn ethernet-segment private'
    def cli(self, output=None):
        """parsing mechanism: cli
        """
        
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        return super().cli(output=out)

class ShowEvpnEthernetSegmentEsiDetail(ShowEvpnEthernetSegment):
    """Parser class for 'show evpn ethernet-segment esi {esi} detail' CLI."""

    cli_command = 'show evpn ethernet-segment esi {esi} detail'
    def cli(self, esi, output=None):
        """parsing mechanism: cli
        """
        
        if output is None:
            out = self.device.execute(self.cli_command.format(
                    esi=esi))
        else:
            out = output
        return super().cli(output=out)

class ABC(MetaParser):
    cli_command = 'abc'
    def cli(self, output=None):
         return {}