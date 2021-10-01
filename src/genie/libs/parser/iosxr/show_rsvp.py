"""show_rsvp.py

IOSXR parsers for the following commands:
    * show rsvp session
    * show rsvp session destination {ip_address}
    * show rsvp neighbors
    * show rsvp graceful-restart neighbors
    * show rsvp graceful-restart neighbors detail
    * show rsvp session detail
    * show rsvp session destination {ip_address} detail dst-port {tunnel_id}
"""
import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import Any, Optional, Use, Schema, ListOf
from genie.libs.parser.utils.common import Common


class ShowRSVPSessionSchema(MetaParser):
    """ Schema for:
        * show rsvp session
        * show rsvp session destination {ip_address}
    """

    schema = {
        "sessions": {
            "type": {
                Any(): {
                    "destination_address":{
                        Any(): {
                            "d_port": {
                                Any(): {
                                    "proto_exttun_id": str,
                                    "psb": int,
                                    "rsb": int,
                                    "req": int
                                }
                            }
                        }
                    }
                }
            }
        }
    }



class ShowRSVPSession(ShowRSVPSessionSchema):
    """ Parser for:
        * show rsvp session
        * show rsvp session destination {ip_address}
    """

    cli_command = ['show rsvp session', 'show rsvp session destination {ip_address}']

    def cli(self, output=None, ip_address=None):
        if not output and ip_address:
            out = self.device.execute(self.cli_command[1].format(ip_address=ip_address))
        elif not output:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}

        # LSP4     17.17.17.17 15060 141.141.141.141     1     1     1
        p1 = re.compile(r'^(?P<type>\S+)\s+(?P<destination_address>\d{1,3}\.\d{1,3}'
                        r'\.\d{1,3}\.\d{1,3})\s+(?P<d_port>\d+)\s+'
                        r'(?P<proto_exttun_id>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                        r'(?P<psb>\d+)\s+(?P<rsb>\d+)\s+(?P<req>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # LSP4     17.17.17.17 15060 141.141.141.141     1     1     1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                dport_dict = \
                    ret_dict.setdefault('sessions', {})\
                            .setdefault('type', {})\
                            .setdefault(group['type'], {})\
                            .setdefault('destination_address', {})\
                            .setdefault(group['destination_address'], {})\
                            .setdefault('d_port', {}) \
                            .setdefault(int(group['d_port']), {})

                dport_dict.update({
                    'proto_exttun_id': group['proto_exttun_id'],
                    'psb': int(group['psb']),
                    'rsb': int(group['rsb']),
                    'req': int(group['req'])
                })
                continue

        return ret_dict


class ShowRSVPNeighborSchema(MetaParser):
    """ Schema for:
        * show rsvp neighbors
    """

    schema = {
        "rsvp_neighbor_information": {
            "global_neighbor": {
                Any():{
                    "interface_neighbor": str,
                    "interface": str
                }
            }
        }
    }

class ShowRSVPNeighbor(ShowRSVPNeighborSchema):
    """ Parser for:
        * show rsvp neighbor
    """

    cli_command = 'show rsvp neighbor'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Global Neighbor: 106.106.106.106
        p1 = re.compile(r'^Global +Neighbor:\s+(?P<global_neighbor>.+)$')

        # 99.33.0.2            TenGigE0/2/0/0
        p2 = re.compile(r'^(?P<intf_neighbor>\d{1,3}\.\d{1,3}\.'
                        r'\d{1,3}\.\d{1,3})\s+(?P<interface>.+)$')


        for line in out.splitlines():
            line = line.strip()

            # Global Neighbor: 106.106.106.106
            m = p1.match(line)
            if m:
                group = m.groupdict()
                neighbor_information = ret_dict.setdefault('rsvp_neighbor_information', {}).\
                    setdefault('global_neighbor', {}).setdefault(group['global_neighbor'], {})
                continue

            # 99.33.0.2            TenGigE0/2/0/0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                # convert interface to full name
                interface = Common.convert_intf_name(group['interface'])
                neighbor_information.update({
                    'interface_neighbor': group['intf_neighbor'],
                    'interface': interface
                })
                continue

        return ret_dict


class ShowRSVPGracefulRestartNeighborsSchema(MetaParser):
    """ Schema for:
        * show rsvp graceful-restart neighbors
        * show rsvp graceful-restart neighbors detail
    """

    schema = {
        "rsvp_neighbor_information": {
            "neighbor": {
                Any():{
                    Optional("app"): str,
                    Optional("state"): str,
                    Optional("recovery"): str,
                    Optional("reason"): str,
                    Optional("since"): str,
                    Optional("lost_connection"): int,
                    Optional("source"): str,
                    Optional("protocol"): str,
                    Optional("recovery_state"): str,
                    Optional("interface_neighbors"): {
                        "number_of_interface": int,
                        "address": str
                    },
                    Optional("restart_time"): int,
                    Optional("restart_time_unit"): str,
                    Optional("recovery_time"): int,
                    Optional("recovery_time_unit"): str,
                    Optional("restart_timer"): str,
                    Optional("recovery_timer"): str,
                    Optional("hello_interval"): int,
                    Optional("hello_interval_unit"): str,
                    Optional("max_missed_hello_messages"): int,
                    Optional("pending_states"): int
                }
            }
        }
    }

class ShowRSVPGracefulRestartNeighbors(ShowRSVPGracefulRestartNeighborsSchema):
    """ Parser for:
       * show rsvp graceful-restart neighbors
    """

    cli_command = 'show rsvp graceful-restart neighbors'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # 106.106.106.106  MPLS    N/A     DONE          N/A                  N/A        0
        p1 = re.compile(r'^(?P<neighbor>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                        r'(?P<app>\w+)\s+(?P<state>\S+)\s+(?P<recovery>\w+)\s+'
                        r'(?P<reason>\S+)\s+(?P<since>\S+)\s+(?P<lost_cnt>\d+)$')


        for line in out.splitlines():
            line = line.strip()

            # 106.106.106.106  MPLS    N/A     DONE          N/A                  N/A        0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                neighbor_information = \
                    ret_dict.setdefault('rsvp_neighbor_information', {})\
                            .setdefault('neighbor', {})\
                            .setdefault(group['neighbor'], {})
                neighbor_information.update({
                    'app': group['app'],
                    'state': group['state'],
                    'recovery': group['recovery'],
                    'reason': group['reason'],
                    'since': group['since'],
                    'lost_connection': int(group['lost_cnt'])
                })
                continue

        return ret_dict

class ShowRSVPGracefulRestartNeighborsDetail(ShowRSVPGracefulRestartNeighborsSchema):
    """ Parser for:
       * show rsvp graceful-restart neighbors detail
    """

    cli_command = 'show rsvp graceful-restart neighbors detail'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)

        ret_dict = {}

        # Neighbor: 106.106.106.106 Source: 17.17.17.17 (MPLS)
        p1 = re.compile(r'^Neighbor:\s+(?P<neighbor>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                        r'\s+Source:\s+(?P<source>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                        r'\s+\((?P<protocol>\w+)\)$')

        # Recovery State: DONE
        p2 = re.compile(r'^Recovery +State:\s+(?P<recovery_state>\S+)$')

        # Number of Interface neighbors: 1
        p3 = re.compile(r'^Number +of +Interface +neighbors:\s+(?P<number_of_intf>\d+)$')

        # address: 99.33.0.2
        p4 =  re.compile(r'^address:\s+(?P<address>.+)$')

        # Restart time: 0 seconds  Recovery time: 0 seconds
        p5 = re.compile(r'^Restart +time:\s+(?P<restart_time>\d+) +(?P<restart_time_unit>\w+)'
                        r'\s+Recovery +time:\s+(?P<recovery_time>\d+) +(?P<recovery_time_unit>\w+)$')

        # Restart timer: Not running
        p6 = re.compile(r'^Restart +timer:\s+(?P<restart_time>.+)$')

        # Recovery timer: Not running
        p7 = re.compile(r'^Recovery +timer:\s+(?P<recovery_time>.+)$')

        # Hello interval: 5000 milliseconds  Maximum allowed missed Hello messages: 3
        p8 = re.compile('^Hello +interval:\s+(?P<hello_interval>\d+)\s+(?P<hello_interval_unit>\w+)'
                        '\s+Maximum +allowed +missed +Hello +messages:\s?(?P<max_allowed_msg>\d+)$')

        # Pending states: 0
        p9 = re.compile('^Pending +states:\s+(?P<pending_states>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Neighbor: 106.106.106.106 Source: 17.17.17.17 (MPLS)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                neighbor_information = ret_dict.setdefault('rsvp_neighbor_information', {}).\
                    setdefault('neighbor', {}).setdefault(group['neighbor'], {})
                neighbor_information.update({'source': group['source'],
                                             'protocol': group['protocol']})
                continue

            # Recovery State: DONE
            m = p2.match(line)
            if m:
                group = m.groupdict()
                neighbor_information.update({'recovery_state': group['recovery_state']})
                continue

            # Number of Interface neighbors: 1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                intf_neighbor_dict = neighbor_information.setdefault('interface_neighbors', {})
                intf_neighbor_dict.update({
                    'number_of_interface': int(group['number_of_intf'])
                })
                continue

            # address: 99.33.0.2
            m = p4.match(line)
            if m:
                group = m.groupdict()
                intf_neighbor_dict.update({
                    'address': group['address']
                })
                continue

            # Restart time: 0 seconds  Recovery time: 0 seconds
            m = p5.match(line)
            if m:
                group = m.groupdict()
                neighbor_information.update({
                    'restart_time': int(group['restart_time']),
                    'restart_time_unit': group['restart_time_unit'],
                    'recovery_time': int(group['recovery_time']),
                    'recovery_time_unit': group['recovery_time_unit']
                })
                continue

            # Restart timer: Not running
            m = p6.match(line)
            if m:
                group = m.groupdict()
                neighbor_information.update({
                    'restart_timer': group['restart_time']
                })
                continue

            # Recovery timer: Not running
            m = p7.match(line)
            if m:
                group = m.groupdict()
                neighbor_information.update({
                    'recovery_timer': group['recovery_time']
                })
                continue

            # Hello interval: 5000 milliseconds  Maximum allowed missed Hello messages: 3
            m = p8.match(line)
            if m:
                group = m.groupdict()
                neighbor_information.update({
                    'hello_interval': int(group['hello_interval']),
                    'hello_interval_unit': group['hello_interval_unit'],
                    'max_missed_hello_messages': int(group['max_allowed_msg'])
                })
                continue

            # Pending states: 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                neighbor_information.update({'pending_states': int(group['pending_states'])})
                continue

        return ret_dict


class ShowRSVPSessionDetailSchema(MetaParser):
    """ Schema for:
        * show rsvp session detail
        * show rsvp session destination {ip_address} detail dst-port {tunnel_id}
    """

    schema =  {
        "sessions": {
            Any(): {
                "address": {
                    Any(): {
                        "tun_id": {
                            Any(): {
                                "ext_id": {
                                    Any(): {
                                        "psbs": int,
                                        "rsbs": int,
                                        "requests": int,
                                        "lsp_id": int,
                                        "tunnel_name": {
                                            Any(): {
                                                "rsvp_path_info": {
                                                    "incoming_address": str,
                                                    Optional("record_route_state"): str,
                                                    Optional("record_route"): {
                                                        Optional(Any()):{
                                                            Optional('address'): str,
                                                            Optional('address_flag'): str,
                                                            Optional('label'): str,
                                                            Optional('label_flag'): str,
                                                        }
                                                    },
                                                    Optional("explicit_route_state"): str,
                                                    Optional("explicit_route"):  {
                                                        Optional(Any()):{
                                                            Optional('path_status'): str,
                                                            Optional('route_address'): str,
                                                        }
                                                    },
                                                    "inlabel": {
                                                        "interface": str,
                                                        "label": str,
                                                    },
                                                    "tspec": {
                                                        "avg_rate": int,
                                                        "burst": int,
                                                        "burst_unit": str,
                                                        "peak_rate": int,
                                                    },
                                                },
                                                "rsvp_resv_info": {
                                                    Optional("record_route_state"): str,
                                                    Optional("record_route"): {
                                                        Optional(Any()):{
                                                            Optional('address'): str,
                                                            Optional('address_flag'): str,
                                                            Optional('label'): str,
                                                            Optional('label_flag'): str,
                                                        }
                                                    },
                                                    "outlabel": {
                                                        "interface": str,
                                                        "label": str,
                                                    },
                                                    "frr_outlabel": {
                                                        "interface": str,
                                                        "label": str,
                                                    },
                                                    "fspec": {
                                                        "avg_rate": int,
                                                        "burst": int,
                                                        "burst_unit": str,
                                                        "peak_rate": int,
                                                    },
                                                },
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
    }


class ShowRSVPSessionDetail(ShowRSVPSessionDetailSchema):
    """ Parser for:
       * show rsvp session detail
       * show rsvp session destination {ip_address} detail dst-port {tunnel_id}
    """

    cli_command = [
        'show rsvp session detail',
        'show rsvp session destination {ip_address} detail dst-port {tunnel_id}'
        ]

    def cli(self, output=None, ip_address=None, tunnel_id=None):

        if ip_address and tunnel_id:
            out = self.device.execute(self.cli_command[1].format(ip_address=ip_address, tunnel_id=tunnel_id))
        elif not output:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}
        rsvp_flag_dict = {}

        # SESSION: IPv4-LSP Addr: 17.17.17.17, TunID: 15060, ExtID: 141.141.141.141
        p1 = re.compile(r'^SESSION:\s+(?P<session>\S+)\s+Addr:\s+(?P<address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}),'
                        r'\s+TunID:\s+(?P<tun_id>\d+),\s+ExtID:\s+(?P<ext_id>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$')

        # PSBs: 1, RSBs: 1, Requests: 1
        p2 = re.compile(r'^PSBs:\s+(?P<psbs>\d+),\s+RSBs:\s+(?P<rsbs>\d+),\s+Requests:\s+(?P<requests>\d+)$')

        # LSPId: 5
        p3 = re.compile(r'^LSPId:\s+(?P<lsp_id>\d+)$')

        # Tunnel Name: NHOP_15060_F141-ASR9912_Hu0000_F17-ASR922_Hu0000
        p4 = re.compile(r'^Tunnel +Name:\s+(?P<tunnel_name>.+)$')

        # RSVP Path Info
        p5 = re.compile(r'^RSVP Path Info:$')

        # InLabel: TenGigE0/2/0/0, 3
        p6 = re.compile(r'^InLabel:\s+(?P<interface>.+),\s+(?P<label>.+)$')

        # Incoming Address: 99.33.0.1
        p7 = re.compile(r'^Incoming Address:\s+(?P<incoming_address>.+)$')

        # Explicit Route: None
        p8 = re.compile(r'^Explicit Route:\s+(?P<explicit_route>.+)$')

        # Strict, 99.33.0.1/32
        p8_1 = re.compile(r'^(?P<path_status>\S+),\s+(?P<route_address>.+)')

        # Record Route: None
        p9 = re.compile(r'^Record Route:\s+(?P<record_route>.+)$')

        # IPv4 99.33.0.2, flags 0x0
        p9_1 = re.compile(r'^IPv4\s+(?P<address>.+),\s+flags\s+(?P<flag>.+)$')

        # Label 24023, flags 0x1
        p9_2 = re.compile(r'^Label\s+(?P<label>.+),\s+flags\s+(?P<flag>.+)$')

        # Tspec: avg rate=0, burst=1K, peak rate=0
        p10 = re.compile(r'^Tspec: +avg +rate=(?P<avg_rate>\d+),\s+burst=(?P<burst>\d+)'
                         r'(?P<burst_unit>\w+), +peak +rate=(?P<peak_rate>\d+)$')

        # RSVP Resv Info:
        p11 = re.compile(r'RSVP Resv Info:')

        # OutLabel: No intf, No label
        # OutLabel: HundredGigE0/0/0/0, 24023
        p12 = re.compile(r'^OutLabel:\s+(?P<interface>.+),\s+(?P<label>.+)$')

        # FRR OutLabel: tunnel-te53300, 3
        p13 = re.compile(r'^FRR +OutLabel:\s+(?P<interface>.+),\s+(?P<label>.+)$')

        # Fspec: avg rate=0, burst=1K, peak rate=0
        p14 = re.compile(r'^Fspec: +avg +rate=(?P<avg_rate>\d+),\s+burst=(?P<burst>\d+)'
                         r'(?P<burst_unit>\w+), +peak +rate=(?P<peak_rate>\d+)$')


        for line in out.splitlines():
            line = line.strip()

            # SESSION: IPv4-LSP Addr: 17.17.17.17, TunID: 15060, ExtID: 141.141.141.141
            m = p1.match(line)
            if m:
                group = m.groupdict()
                session_information = ret_dict.setdefault('sessions', {}).\
                    setdefault(group['session'], {}).\
                    setdefault('address', {}).setdefault(group['address'], {}).\
                    setdefault('tun_id', {}).setdefault(group['tun_id'], {}). \
                    setdefault('ext_id', {}).setdefault(group['ext_id'], {})
                continue

            # PSBs: 1, RSBs: 1, Requests: 1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                session_information.update({'psbs': int(group['psbs']),
                                          'rsbs': int(group['rsbs']),
                                          'requests': int(group['requests']),
                                          })
                continue

            # LSPId: 5
            m = p3.match(line)
            if m:
                group = m.groupdict()
                session_information.update({'lsp_id': int(group['lsp_id'])})
                continue


            # Tunnel Name: NHOP_15060_F141-ASR9912_Hu0000_F17-ASR922_Hu0000
            m = p4.match(line)
            if m:
                group = m.groupdict()
                tunnel_name_dict = session_information.setdefault('tunnel_name', {}).\
                    setdefault(group['tunnel_name'], {})
                continue

            # RSVP Path Info:
            m = p5.match(line)
            if m:
                group = m.group()
                if group=='RSVP Path Info:':
                    rsvp_path_dict = tunnel_name_dict.setdefault('rsvp_path_info', {})
                    rsvp_flag_dict = rsvp_path_dict
                continue

            # InLabel: TenGigE0/2/0/0, 3
            m = p6.match(line)
            if m:
                group = m.groupdict()
                inlabel_dict = rsvp_path_dict.setdefault('inlabel', {})
                interface = group['interface']
                interface = Common.convert_intf_name(interface)
                inlabel_dict.update({
                    'interface': interface,
                    'label': group['label']
                })
                continue

            # Incoming Address: 99.33.0.1
            m = p7.match(line)
            if m:
                group = m.groupdict()
                rsvp_path_dict.update({
                    'incoming_address': group['incoming_address']
                })
                continue

            # Explicit Route: None
            m = p8.match(line)
            if m:
                group = m.groupdict()
                rsvp_path_dict.update({
                    'explicit_route_state': group['explicit_route']
                })
                continue

            # Strict, 99.33.0.1/32
            m = p8_1.match(line)
            if m:
                group = m.groupdict()
                explicit_route_dict = rsvp_path_dict.setdefault('explicit_route', {})
                index = len(explicit_route_dict)
                index_dict = explicit_route_dict.setdefault(index, {})
                index_dict.update({
                    'path_status': group['path_status'],
                    'route_address': group['route_address']
                })
                continue

            # Record Route: None
            m = p9.match(line)
            if m:
                group = m.groupdict()
                rsvp_flag_dict.update({
                    'record_route_state': group['record_route']
                })
                continue

            # IPv4 141.141.141.141, flags 0x21
            m = p9_1.match(line)
            if m:
                group = m.groupdict()
                record_route_dict = rsvp_flag_dict.setdefault('record_route', {})
                index = len(record_route_dict)
                index_dict = record_route_dict.setdefault(index, {})
                index_dict.update({
                    'address': group['address'],
                    'address_flag': group['flag']
                })
                continue

            # Label 24023, flags 0x1
            m = p9_2.match(line)
            if m:
                group = m.groupdict()
                record_route_dict = rsvp_flag_dict.setdefault('record_route', {})
                index = len(record_route_dict)
                index_dict = record_route_dict.setdefault(index, {})
                index_dict.update({
                    'label': group['label'],
                    'label_flag': group['flag']
                })
                continue

            # Tspec: avg rate=0, burst=1K, peak rate=0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                tspec_dict = rsvp_path_dict.setdefault('tspec', {})
                tspec_dict.update({
                    'avg_rate': int(group['avg_rate']),
                    'burst': int(group['burst']),
                    'burst_unit': group['burst_unit'],
                    'peak_rate': int(group['peak_rate'])
                })
                continue


            # RSVP Resv Info:
            m = p11.match(line)
            if m:
                group = m.group()
                if group=='RSVP Resv Info:':
                    rsvp_resv_dict = tunnel_name_dict.setdefault('rsvp_resv_info', {})
                    rsvp_flag_dict = rsvp_resv_dict
                continue

            # OutLabel: No intf, No label
            # OutLabel: HundredGigE0/0/0/0, 24023
            m = p12.match(line)
            if m:
                group = m.groupdict()
                outlabel_dict = rsvp_resv_dict.setdefault('outlabel', {})
                interface = group['interface']
                interface = Common.convert_intf_name(interface)
                outlabel_dict.update({
                    'interface': interface,
                    'label': group['label']
                })
                continue

            # FRR OutLabel: tunnel-te53300, 3
            m = p13.match(line)
            if m:
                group = m.groupdict()
                outlabel_dict = rsvp_resv_dict.setdefault('frr_outlabel', {})
                interface = group['interface']
                interface = Common.convert_intf_name(interface)
                outlabel_dict.update({
                    'interface': interface,
                    'label': group['label']
                })
                continue

            # Fspec: avg rate=0, burst=1K, peak rate=0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                fspec_dict = rsvp_resv_dict.setdefault('fspec', {})
                fspec_dict.update({
                    'avg_rate': int(group['avg_rate']),
                    'burst': int(group['burst']),
                    'burst_unit': group['burst_unit'],
                    'peak_rate': int(group['peak_rate'])
                })
                continue

        return ret_dict
