"""show_mpls.py

JUNOS parsers for the following commands:
    * show mpls lsp name {name} detail
    * show mpls lsp name {name} extensive
    * show mpls ldp discovery detail
    * show mpls ldp parameters
"""

import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import Any, Optional, Use, Schema, ListOf


# ==============================================
#   Show mpls ldp discovery
# ==============================================
class ShowMplsLdpDiscoveryDetailSchema(MetaParser):
    """
    Schema for show mpls ldp discovery detail
    """
    schema = {
        'vrf': {
            Optional('local_ldp_identifier'): str,
            'vrfs': ListOf({
                'vrf_name': str,
                'interfaces': ListOf({
                    Optional('interface'): str,
                    Optional('vrf_hex'): str,
                    Optional('source_ip_addr'): str,
                    Optional('transport_ip_addr'): str,
                    Optional('xmit'): str,
                    Optional('recv'): str,
                    Optional('hello_interval_ms'): str,
                    Optional('hello_due_time_ms'): str,
                    Optional('quick_start'): str,
                    Optional('ldp_id'): {
                        Optional('network_addr'): str,
                        "ldp_entries": ListOf({
                            Optional('source_ip_addr'): str,
                            Optional('transport_ip_addr'): str,
                            Optional('holdtime_sec'): str,
                            Optional('proposed_local'): str,
                            Optional('proposed_peer'): str,
                            Optional('expiring_in'): str,
                            Optional('established_date'): str,
                            Optional('established_elapsed'): str,
                            Optional('last_session_connection_failures'): ListOf({
                                Optional('timestamp'): str,
                                Optional('reason'): str,
                                Optional('last_up_for'): str,
                            })
                        })
                    }
                })
            })
        }
    }


class ShowMplsLdpDiscoveryDetail(ShowMplsLdpDiscoveryDetailSchema):
    """
        Parser for show mpls ldp discovery detail
    """
    cli_command = 'show mpls ldp discovery detail'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        result_dict = {}
        discovery_flag = False

        # Local LDP Identifier: 10.94.1.1:0
        p1 = re.compile(r'^Local +LDP +Identifier: '
                        '(?P<local_ldp_identifier>[\d\.\:]+)$')

        # Discovery Sources:
        p2 = re.compile(r'^Discovery +Sources:$')

        # TenGigE0/3/0/0 (0xa0004c0) : xmit/recv
        # TenGigE0/3/0/26 (0xa000e00) : xmit/recv
        p3 = re.compile(r'^(?P<interface>\S+) \((?P<interface_hex>[\w]+)\)'
                        ' : (?P<xmit>xmit)?\/?(?P<recv>recv)?$')

        # VRF: 'default' (0x60000000)
        p4 = re.compile(r'^VRF: \'(?P<vrf>\S+)\' +\((?P<vrf_hex>[\w]+)\)$')

        # LDP Id: 10.144.96.96:0
        p5 = re.compile(r'^(?P<ldp_tdp>\w+) +Id:\s*(?P<ldp_tdp_id>[\S]+)$')

        # Source address: 10.120.0.1; Transport address: 10.94.1.1
        p6 = re.compile(r'^Source +address: +(?P<source_ip_addr>[\d\.]+);'
                        ' +Transport +address: +(?P<transport_ip_addr>[\d\.]+)$')

        # Hold time: 15 sec (local:15 sec, peer:45 sec)
        p7 = re.compile(r'^Hold +time: +(?P<holdtime_sec>\d+) +sec '
                        '\(local:(?P<proposed_local>\d+) +sec, '
                        'peer:(?P<proposed_peer>\d+) +sec\)$')

        # (expiring in 11 sec)
        # (expiring in 14.5 sec)
        p8 = re.compile(r'^\(expiring +in +(?P<expiring_in>\d.*) +sec\)$')

        # Established: Nov  6 14:39:26.164 (5w2d ago)
        p9 = re.compile(r'^Established: +(?P<established_date>\S.*) '
                        '+\((?P<established_elapsed>\S*) +ago\)$')

        # Hello interval: 5 sec (due in 563 msec)
        p10 = re.compile(r'^Hello +interval: +(?P<hello_interval>\d+) +sec'
                        ' +\(due +in +(?P<hello_due_time>\S+ +\S+)\)$')

        # Quick-start: Enabled
        p11 = re.compile(r'^Quick-start: +(?P<quick_start>\S+)$')

        # Last session connection failures:
        p12 = re.compile(r'^Last +session +connection +failures:$')

        #     Jan  4 05:20:34.814: User cleared session manually
        #     Jan  4 05:28:48.641: User cleared session manually
        p13 = re.compile(r'^(?P<timestamp>[A-Z][a-z]{2}\s+[0-9]{1,2}\s[0-9:.]+)'
                         ':\s+(?P<reason>[\w\s]+)$')

        #         (Last up for 00:06:56)
        #         (Last up for 00:08:05)
        p14 = re.compile(r'\(Last +up +for +(?P<last_up_for>[\d:]+)\)$')

        for line in out.splitlines():
            line = line.strip()

            # Local LDP Identifier: 10.94.1.1:0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ldp_dict = result_dict.setdefault('vrf', {})
                ldp_dict.update(
                    {'local_ldp_identifier': group['local_ldp_identifier']})
                continue

            # Discovery Sources:
            m = p2.match(line)
            if m:
                discovery_flag = True
                continue

            # TenGigE0/3/0/0 (0xa0004c0) : xmit/recv
            m = p3.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface'] if group['interface'] \
                    else "default"

                interface_dict = {'interface': interface}
                interface_dict.update(
                    {'xmit': 'True' if group['xmit'] else 'False'})
                interface_dict.update(
                    {'recv': 'True' if group['recv'] else 'False'})
                continue

            # VRF: 'default' (0x60000000)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                vrf_name = group['vrf'] if group['vrf'] else "default"
                vrf_list = result_dict.setdefault('vrf', {}).\
                    setdefault('vrfs', [])

                vrf = next(
                    (i for i in vrf_list if i['vrf_name'] == vrf_name), None)

                if vrf is None:
                    vrf = {'vrf_name': vrf_name, 'interfaces': []}
                    vrf_list.append(vrf)

                if interface:
                    vrf_hex = group['vrf_hex']
                    interface_dict.update({'vrf_hex': vrf_hex})
                    vrf['interfaces'].append(interface_dict)

                continue

            # LDP Id: 10.144.96.96:0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ldp_tdp = group['ldp_tdp'].lower()
                ldp_tdp_id = group['ldp_tdp_id']
                if discovery_flag:
                    ldp_dict = interface_dict.\
                        setdefault('{}_id'.format(ldp_tdp), {})

                    net_addr = next((i for i in ldp_dict
                                    if i['network_addr'] == ldp_tdp_id
                                    ), None)

                    if net_addr is None:
                        net_addr = {
                            'network_addr': ldp_tdp_id,
                            'ldp_entries': []
                        }
                        ldp_dict.update(net_addr)

                continue

            # Source address: 10.166.0.57; Transport address: 10.52.31.247
            m = p6.match(line)
            if m:
                group = m.groupdict()
                if 'source_ip_addr' in interface_dict.keys():
                    item_dict = {k: v for k, v in group.items() if v}
                    net_addr['ldp_entries'].append(item_dict)
                else:
                    interface_dict.update(
                        {k: v for k, v in group.items() if v})
                continue

            # Hold time: 15 sec (local:15 sec, peer:45 sec)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                item_dict.update(
                    {k: v for k, v in group.items() if v})
                continue

            # (expiring in 14.5 sec)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                item_dict.update(
                    {'expiring_in': group['expiring_in']})

            m = p9.match(line)
            if m:
                group = m.groupdict()
                item_dict.update({
                    'established_date': group['established_date'],
                    'established_elapsed': group['established_elapsed']
                })

            # Hello interval: 5 sec (due in 563 msec)
            m = p10.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'hello_interval_ms': str(
                    1000*int(group['hello_interval']))})
                if ' sec' in group['hello_due_time']:
                    hello_due_time_ms = str(
                        int(1000*float(group['hello_due_time'].split(' ')[0])))
                else:
                    hello_due_time_ms = str(
                        int(group['hello_due_time'].split(' ')[0]))
                interface_dict.update({'hello_due_time_ms': hello_due_time_ms})
                continue

            # Quick-start: Enabled
            m = p11.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update(
                    {'quick_start': group['quick_start'].lower()})
                continue

            # Last session connection failures:
            m = p12.match(line)
            if m:
                item_dict['last_session_connection_failures'] = []

            m = p13.match(line)
            if m:
                group = m.groupdict()
                connection_failure_dict = {
                    'timestamp': group['timestamp'],
                    'reason': group['reason']
                }

                item_dict['last_session_connection_failures'].append(
                    connection_failure_dict)
                continue

            m = p14.match(line)
            if m:
                group = m.groupdict()
                connection_failure_dict.update(
                    {'last_up_for': group['last_up_for']})

        return result_dict


class ShowMPLSLSPNameDetailSchema(MetaParser):
    """ Schema for
        * show mpls lsp name {name} detail
    """

    schema = {
        "mpls-lsp-information": {
            "rsvp-session-data": ListOf({
                "session-type": str,
                "count": str,
                Optional("rsvp-session"): {
                    "destination-address": str,
                    "source-address": str,
                    "lsp-state": str,
                    "route-count": str,
                    "name": str,
                    "lsp-path-type": str,
                    "suggested-label-in": str,
                    "suggested-label-out": str,
                    "recovery-label-in": str,
                    "recovery-label-out": str,
                    "rsb-count": str,
                    "resv-style": str,
                    "label-in": str,
                    "label-out": str,
                    "psb-lifetime": str,
                    "psb-creation-time": str,
                    "sender-tspec": str,
                    "lsp-id": str,
                    "tunnel-id": str,
                    "proto-id": str,
                    "packet-information": ListOf({
                        "heading": str,
                        Optional("next-hop"): str,
                        Optional("previous-hop"): str,
                        Optional("interface-name"): str,
                        Optional("count"): str,
                        Optional("entropy-label"): str,
                        Optional("in-epoch"): str,
                        Optional("in-message-handle"): str,
                        Optional("in-message-id"): str,
                        Optional("out-epoch"): str,
                        Optional("out-message-state"): str,
                        Optional("out-message-id"): str,
                    }),
                    "adspec": str,
                    "explicit-route": {
                        "explicit-route-element": ListOf({
                            "address": str,
                        })
                    },
                    "record-route": {
                        Optional("record-route-element"): ListOf({
                            "address": str,
                        }),
                        Optional("address"): list,
                    },
                    Optional("rsvp-lsp-enh-local-prot-downstream"): {
                        "rsvp-lsp-enh-local-prot-refresh-interval": str,
                        "rsvp-lsp-enh-lp-downstream-status": str
                    },
                    Optional("rsvp-lsp-enh-local-prot-upstream"): {
                        "rsvp-lsp-enh-local-prot-refresh-interval": str,
                        "rsvp-lsp-enh-lp-upstream-status": str
                    },
                },
                "display-count": str,
                "up-count": str,
                "down-count": str,
            })
        },
    }


class ShowMPLSLSPNameDetail(ShowMPLSLSPNameDetailSchema):
    """ Parser for:
        * show mpls lsp name {name} detail
    """

    cli_command = 'show mpls lsp name {name} detail'

    def cli(self, name, output=None):
        if not output:
            out = self.device.execute(self.cli_command.format(name=name))
        else:
            out = output

        ret_dict = {}

        # Ingress LSP: 0 sessions
        # Egress LSP: 0 sessions
        # Transit LSP: 30 sessions
        p1 = re.compile(
            r'^(?P<session_type>\S+) +LSP: +(?P<count>\d+) +sessions$')

        # Total 0 displayed, Up 0, Down 0
        p2 = re.compile(r'^Total (?P<display_count>\d+) +displayed, +Up +'
                        r'(?P<up_count>\d+), +Down +(?P<down_count>\d+)$')

        # 10.49.194.125
        p3 = re.compile(r'^[\d\.]+')

        # From: 10.49.194.127, LSPstate: Up, ActiveRoute: 0
        p4 = re.compile(r'^From: +(?P<source_address>[\d+\.]+), +LSPstate: +'
                        r'(?P<lsp_state>[^\s,]+), +ActiveRoute: +'
                        r'(?P<route_count>\d+)$')

        # LSPname: test_lsp_01, LSPpath: Primary
        p5 = re.compile(r'^LSPname: +(?P<name>[^\s,]+), +'
                        r'LSPpath: +(?P<lsp_path_type>\S+)$')

        # Suggested label received: -, Suggested label sent: -
        p6 = re.compile(
            r'^Suggested +label +received: +(?P<suggested_label_in>[^\s,]+), +'
            r'Suggested +label +sent: +(?P<suggested_label_out>\S+)$')

        # Recovery label received: -, Recovery label sent: 44
        p7 = re.compile(
            r'^Recovery +label +received: +(?P<recovery_label_in>[^\s,]+), +'
            r'Recovery +label +sent: +(?P<recovery_label_out>\S+)$')

        # Resv style: 1 FF, Label in: 46, Label out: 44
        p8 = re.compile(
            r'^Resv +style: +(?P<rsb_count>\d+) +(?P<resv_style>[^\s,]+), +'
            r'Label +in: +(?P<label_in>[^\s,]+), +'
            r'Label +out: +(?P<label_out>\S+)$')

        # Time left:  138, Since: Tue Jun 30 07:22:02 2020
        p9 = re.compile(r'^Time +left: +(?P<psb_lifetime>\d+), +'
                        r'Since: +(?P<psb_creation_time>.+)$')

        # Tspec: rate 0bps size 0bps peak Infbps m 20 M 1500
        p10 = re.compile(r'^Tspec: +(?P<sender_tspec>.+)$')

        # Port number: sender 1 receiver 50088 protocol 0
        p11 = re.compile(r'^Port +number: +sender +(?P<lsp_id>\d+) +'
                         r'receiver +(?P<tunnel_id>\d+) +'
                         r'protocol +(?P<proto_id>\d+)$')

        # PATH rcvfrom: 10.169.14.157 (ge-0/0/0.0) 1 pkts
        # PATH sentto: 192.168.145.218 (ge-0/0/1.1) 1 pkts
        # RESV rcvfrom: 192.168.145.218 (ge-0/0/1.1) 1 pkts, Entropy label: Yes
        p12 = re.compile(
            r'^(?P<heading>(PATH|RESV)) +'
            r'((rcvfrom: +(?P<previous_hop>\S+))|(sentto: +(?P<next_hop>\S+))) +'
            r'(?P<interface_name>\S+) +(?P<count>\d+) +pkts'
            r'(, +Entropy +label: +(?P<entropy_label>\S+))?$')

        # RESV
        p12_1 = re.compile(r'^(?P<heading>(PATH|RESV))$')

        # incoming message handle: P-8/1, Message ID: 23, Epoch: 385353
        p12_2 = re.compile(r'incoming +message +handle: +'
                           r'(?P<in_message_handle>\S+), +Message +ID: +'
                           r'(?P<in_message_id>\S+), +Epoch: +(?P<in_epoch>\S+)')

        # outgoing message state: refreshing, Message ID: 23, Epoch: 385318
        p12_3 = re.compile(r'outgoing +message +state: +'
                           r'(?P<out_message_state>\S+), +Message +ID: +'
                           r'(?P<out_message_id>\S+), +Epoch: +(?P<out_epoch>\S+)')

        # Adspec: received MTU 1500 sent MTU 1500
        p13 = re.compile(r'^Adspec: +(?P<adspec>.+)$')

        # Explct route: 192.168.145.218 10.49.194.65 10.49.194.66
        p14 = re.compile(r'^Explct +route: +(?P<addresses>.+)$')

        # Record route: 10.49.194.2 10.169.14.157 <self> 192.168.145.218
        p15 = re.compile(r'^Record +route: +(?P<addresses>.+)$')

        # Enhanced FRR: Disabled (Upstream), Reason: Compatibility, Refresh: 30 secs
        p16_1 = re.compile(r'Enhanced +FRR: (?P<rsvp_lsp_enh_lp_upstream_status>\S+)'
                           r' +\(Upstream\), +Reason: +Compatibility, +Refresh: '
                           r'+(?P<rsvp_lsp_enh_local_prot_refresh_interval>[\s\S]+)')

        # Enhanced FRR: Disabled (Downstream), Reason: Compatibility, Refresh: 30 secs
        p16_2 = re.compile(r'Enhanced +FRR: (?P<rsvp_lsp_enh_lp_downstream_status>\S+)'
                           r' +\(Downstream\), +Reason: +Compatibility, +Refresh: '
                           r'+(?P<rsvp_lsp_enh_local_prot_refresh_interval>[\s\S]+)')

        for line in out.splitlines():
            line = line.strip()

            # Ingress LSP: 0 sessions
            # Egress LSP: 0 sessions
            # Transit LSP: 30 sessions
            m = p1.match(line)
            if m:
                group = m.groupdict()
                session_data_list = ret_dict.setdefault('mpls-lsp-information', {}).\
                    setdefault('rsvp-session-data', [])
                session_data_dict = {}
                session_data_dict.update({
                    k.replace('_', '-'): v
                    for k, v in group.items() if v is not None
                })
                session_data_list.append(session_data_dict)
                continue

            # Total 0 displayed, Up 0, Down 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                session_data_dict.update({
                    k.replace('_', '-'): v
                    for k, v in group.items() if v is not None
                })
                continue

            # 10.49.194.125
            m = p3.match(line)
            if m:
                group = m.groupdict()
                rsvp_session = session_data_dict.setdefault('rsvp-session', {})
                if rsvp_session.get('record-route'):
                    record_route_element = rsvp_session.get('record-route').\
                        setdefault('record-route-element', [])
                    elements = re.findall(r'[\d\.]+', line)
                    for address in elements:
                        record_route_element.append({'address': address})
                elif rsvp_session.get('explicit-route'):
                    explicit_route_element = rsvp_session.get('explicit-route').\
                        setdefault('explicit-route-element', [])
                    elements = re.findall(r'[\d\.]+', line)
                    for address in elements:
                        explicit_route_element.append({'address': address})
                else:
                    rsvp_session.update({
                        'destination-address':
                        re.findall(r'[\d\.]+', line)[0]
                    })
                continue

            # From: 10.49.194.127, LSPstate: Up, ActiveRoute: 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                rsvp_session.update({
                    k.replace('_', '-'): v
                    for k, v in group.items() if v is not None
                })
                continue

            # LSPname: test_lsp_01, LSPpath: Primary
            m = p5.match(line)
            if m:
                group = m.groupdict()
                rsvp_session.update({
                    k.replace('_', '-'): v
                    for k, v in group.items() if v is not None
                })
                continue

            # Suggested label received: -, Suggested label sent: -
            m = p6.match(line)
            if m:
                group = m.groupdict()
                rsvp_session.update({
                    k.replace('_', '-'): v
                    for k, v in group.items() if v is not None
                })
                continue

            # Recovery label received: -, Recovery label sent: 44
            m = p7.match(line)
            if m:
                group = m.groupdict()
                rsvp_session.update({
                    k.replace('_', '-'): v
                    for k, v in group.items() if v is not None
                })
                continue

            # Resv style: 1 FF, Label in: 46, Label out: 44
            m = p8.match(line)
            if m:
                group = m.groupdict()
                rsvp_session.update({
                    k.replace('_', '-'): v
                    for k, v in group.items() if v is not None
                })
                continue

            # Time left:  138, Since: Tue Jun 30 07:22:02 2020
            m = p9.match(line)
            if m:
                group = m.groupdict()
                rsvp_session.update({
                    k.replace('_', '-'): v
                    for k, v in group.items() if v is not None
                })
                continue

            # Tspec: rate 0bps size 0bps peak Infbps m 20 M 1500
            m = p10.match(line)
            if m:
                group = m.groupdict()
                rsvp_session.update({
                    k.replace('_', '-'): v
                    for k, v in group.items() if v is not None
                })
                continue

            # Port number: sender 1 receiver 50088 protocol 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                rsvp_session.update({
                    k.replace('_', '-'): v
                    for k, v in group.items() if v is not None
                })
                continue

            # PATH rcvfrom: 10.169.14.157 (ge-0/0/0.0) 1 pkts
            # PATH sentto: 192.168.145.218 (ge-0/0/1.1) 1 pkts
            # RESV rcvfrom: 192.168.145.218 (ge-0/0/1.1) 1 pkts, Entropy label: Yes

            # RESV
            m = p12.match(line) or p12_1.match(line)
            if m:
                group = m.groupdict()

                if 'packet-information' not in rsvp_session:
                    packet_list = rsvp_session.setdefault('packet-information', [])

                packet_dict = {}

                # 'interface-name': '(ge-0/0/0.0)',
                if self.cli_command == 'show mpls lsp name {name} detail':
                    packet_dict.update({
                        k.replace('_', '-'): v
                        for k, v in group.items() if v is not None
                    })

                # 'interface-name': 'ge-0/0/0.0',
                elif self.cli_command == 'show mpls lsp name {name} extensive':
                    for k, v in group.items():
                        if v is not None:
                            if k == 'interface_name':
                                v = re.search('\((.+?)\)',v).group(1)
                                packet_dict[k.replace('_', '-')] = v
                            else:
                                packet_dict[k.replace('_', '-')] = v

                packet_list.append(packet_dict)
                continue

            # incoming message handle: P-8/1, Message ID: 23, Epoch: 385353
            # outgoing message state: refreshing, Message ID: 23, Epoch: 385318
            m = p12_2.match(line) or p12_3.match(line)
            if m:
                group = m.groupdict()

                packet_dict.update({
                    k.replace('_', '-'): v
                    for k, v in group.items() if v is not None
                })
                continue

            # Adspec: received MTU 1500 sent MTU 1500
            m = p13.match(line)
            if m:
                group = m.groupdict()
                rsvp_session.update({
                    k.replace('_', '-'): v
                    for k, v in group.items() if v is not None
                })
                continue

            # Explct route: 192.168.145.218 10.49.194.65 10.49.194.66
            m = p14.match(line)
            if m:
                group = m.groupdict()
                explicit_route_element = rsvp_session.setdefault('explicit-route', {}).\
                    setdefault('explicit-route-element', [])
                elements = group['addresses'].split(' ')
                for address in elements:
                    explicit_route_element.append({'address': address})
                continue

            # Record route: 10.49.194.2 10.169.14.157 <self> 192.168.145.218
            m = p15.match(line)
            if m:
                group = m.groupdict()

                #                     'record-route': {
                #                         'record-route-element': [{
                #                             'address': '10.49.194.2'
                #                         }, {
                #                             'address': '10.169.14.157'
                #                         }, {
                #                             'address': '10.64.64.64'
                #                         }]
                #                     }
                if self.cli_command == 'show mpls lsp name {name} detail':
                    record_route_element = rsvp_session.setdefault('record-route', {}).\
                        setdefault('record-route-element', [])
                    elements = group['addresses'].split(' ')
                    for address in elements:
                        record_route_element.append({'address': address})

                #                         "record-route": {
                #                             "address": [
                #                                 "10.49.194.2",
                #                                 "10.169.14.157",
                #                                 "192.168.145.218",
                #                             ],
                #                         },
                elif self.cli_command == 'show mpls lsp name {name} extensive':
                    record_route_address_list = rsvp_session.setdefault('record-route', {}).\
                                            setdefault('address', [])
                    elements = group['addresses'].split(' ')
                    for address in elements:
                        if address == '<self>':
                            continue
                        record_route_address_list.append(address)
                continue

            # Enhanced FRR: Disabled (Upstream), Reason: Compatibility, Refresh: 30 secs
            m = p16_1.match(line)
            if m:
                group = m.groupdict()
                upstream_dict = rsvp_session.setdefault("rsvp-lsp-enh-local-prot-upstream", {})

                for k, v in group.items():
                    upstream_dict[k.replace('_', '-')] = v

                continue

            # Enhanced FRR: Disabled (Downstream), Reason: Compatibility, Refresh: 30 secs
            m = p16_2.match(line)
            if m:
                group = m.groupdict()
                downstream_dict = rsvp_session.setdefault("rsvp-lsp-enh-local-prot-downstream", {})

                for k, v in group.items():
                    downstream_dict[k.replace('_', '-')] = v

                continue

        return ret_dict


class ShowMPLSLSPNameExtensive(ShowMPLSLSPNameDetail):
    """
    Parser for:
        * show mpls lsp name {name} extensive
    """

    cli_command = 'show mpls lsp name {name} extensive'

    def cli(self, name, output=None):

        if not output:
            cmd = self.cli_command.format(name=name)
            out = self.device.execute(cmd)
        else:
            out = output

        return super().cli(output=out, name=name)




# ==============================================
#  Schema for show mpls ldp parameters
# ==============================================

class ShowMplsLdpParametersSchema(MetaParser):
    """ Schema for
        * show mpls ldp parameters
    """
    schema = {
        "ldp-parameters": {
            "role": str,
            "protocol-version": str,
            "router-id": str,
            "null-label": {
                "null-label-ipv4-address": str
            },
            "session": {
                "session-holdtime-sec": str,
                "session-keepalive-interval-sec": str,
                "session-backoff": {
                    "backoff-initial-sec": str,
                    "backoff-maximum-sec": str
                },
                "global-md5-password": str
            },
            "discovery": {
                "discovery-link-hellos": {
                    "link-hellos-hold-time-sec": str,
                    "link-hellos-interval-sec": str
                },
                "discovery-target-hellos": {
                    "target-hellos-hold-time-sec": str,
                    "target-hellos-interval-sec": str
                },
                "discovery-quick-start": str,
                "discovery-transport-address": {
                    "transport-ipv4-address": str
                },
            },
            "graceful-restart": {
                "graceful-restart-status": str,
                "graceful-restart-reconnect-timeout": {
                    "reconnect-timeout-time-sec": str,
                    "reconnect-timeout-forward-state-holdtime-sec": str
                }
            },
            "nsr": {
                "nsr-status": str,
                Optional("nsr-sync-ed-status"): str
            },
            "timeouts": {
                "housekeeping-periodic-timer-timeouts-sec": str,
                "local-binding-timeouts-sec": str,
                "forward-state-lsd-timeouts-sec": str
            },
            "delay-af-bind-peer-sec": str,
            "max": {
                "interfaces": {
                    "max-interfaces-units": str,
                    Optional("attached-interfaces-units"): str,
                    Optional("te-tunnel-interfaces-units"): str
                },
                "max-peers-units": str
            },
            "oor-state": {
                "oor-memory": str
            },
        },
    }


# ==============================================
#  Parser for show mpls ldp parameters
# ==============================================

class ShowMplsLdpParameters(ShowMplsLdpParametersSchema):
    """ For Parsing
        * show mpls ldp parameters
    """

    cli_command = 'show mpls ldp parameters'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # LDP Parameters:
        p1 = re.compile(r'^LDP +Parameters:$')

        # Role: Active
        p2 = re.compile(r'^Role: +(?P<role_value>\w+)$')

        # Protocol Version: 1
        p3 = re.compile(r'^Protocol +Version: +(?P<protocol_version_number>\S+)$')

        # Router ID: 10.4.1.1
        p4 = re.compile(r'^Router +ID: +(?P<router_id_ip>[\d.]+)$')

        # Null Labels:
        p5 = re.compile(r'^Null +Label:$')

        # IPv4: Implicit
        p6 = re.compile(r'^IPv4: +(?P<null_labels_ipv4>\w+)$')

        # Session:
        p7 = re.compile(r'^Session:$')

        # Hold time: 180 sec
        p8 = re.compile(r'^Hold +time: +(?P<hold_time_seconds>\d+) +sec$')

        # Keepalive interval: 60 sec
        p9 = re.compile(r'^Keepalive +interval: +(?P<keepalive_interval_seconds>\d+) +sec$')

        # Backoff: Initial:15 sec, Maximum:120 sec
        p10 = re.compile(
            r'^Backoff: +Initial:(?P<initial_seconds>\d+) +sec'
            r', +Maximum:(?P<maximum_seconds>\d+) +sec$')

        # Global MD5 password: Disabled
        p11 = re.compile(
            r'^Global +MD5 +password: +(?P<global_md5_password>\w+)$')

        # Discovery:
        p12 = re.compile(r'^Discovery:$')

        # Link Hellos: Holdtime:15 sec, Interval:5 sec
        p13 = re.compile(
            r'^Link +Hellos: +Holdtime:(?P<link_hellos_hold_time_seconds>\d+) +sec,'
            r' +Interval:(?P<link_hellos_interval_seconds>\d+) +sec$')

        # Targeted Hellos: Holdtime:90 sec, Interval:10 sec
        p14 = re.compile(
            r'^Targeted +Hellos: +Holdtime:(?P<targeted_hellos_hold_time_seconds>\d+) +sec'
            r', +Interval:(?P<targeted_hellos_interval_seconds>\d+) +sec$')

        # Quick-start: Enabled (by default)
        p15 = re.compile(r'^Quick-start: +(?P<quick_start>.*)$')

        # Transport address:
        p16 = re.compile(r'^Transport +address:$')

        # IPv4: 10.4.1.1
        p17 = re.compile(r'^IPv4: +(?P<transport_address_ipv4_ip>[\d.]+)$')

        # Graceful Restart:
        p18 = re.compile(r'^Graceful +Restart:$')

        # Enabled
        p19 = re.compile(r'^(?P<graceful_restart_value>(Enabled|Disabled))$')

        # Reconnect Timeout:120 sec, Forwarding State Holdtime:180 sec
        p20 = re.compile(
            r'^Reconnect +Timeout:(?P<reconnect_timeout_seconds>\d+) +sec,'
            r' +Forwarding +State +Holdtime:(?P<forwarding_state_holdtime_seconds>\d+) +sec$')

        # NSR: Enabled, Sync-ed
        p21 = re.compile(r'^NSR: +(?P<nsr_value>\w+)(, +(?P<synced_value>Sync-ed))?$')

        # Timeouts:
        p22 = re.compile(r'^Timeouts:$')

        # Housekeeping periodic timer: 10 sec
        p23 = re.compile(
            r'^Housekeeping +periodic +timer: +(?P<housekeeping_periodic_timer_seconds>\d+) +sec$')

        # Local binding: 300 sec
        p24 = re.compile(r'^Local +binding: +(?P<local_binding_seconds>\d+) +sec$')

        # Forwarding state in LSD: 360 sec
        p25 = re.compile(
            r'^Forwarding +state +in +LSD: +(?P<forwarding_state_lsd_seconds>\d+) +sec$')

        # Delay in AF Binding withdrawl from peer: 180 sec
        p26 = re.compile(
            r'^Delay +in +AF +Binding +Withdrawl +from +peer:'
            r' +(?P<delay_af_binding_peer_seconds>\d+) +sec$')

        # Max:
        p27 = re.compile(r'^Max:$')

        # 5000 interfaces (4000 attached, 1000 TE tunnel), 2000 peers
        p28 = re.compile(
            r'^(?P<max_interface_number>\d+) +interfaces(,| )(\(| )'
            r'((?P<attached_interfaces_number>\d+) +attached(\)|,))?'
            r'((,| )*)?((?P<te_tunnel_number>\d+) +TE +tunnel\))?((,| )*)?((?P<peers_number>\d+) +peers)?')

        # OOR state
        p29 = re.compile(r'^OOR +state$')

        # Memory: Normal
        p30 = re.compile(
            r'^Memory: +(?P<oor_memory_value>(Normal|Major|Critical))$')

        # Looping through each line
        for line in out.splitlines():
            line = line.strip()

            # LDP Parameters:
            m = p1.match(line)
            if m:
                parameters_dict = ret_dict.setdefault('ldp-parameters', {})
                continue

            # Role: Active
            m = p2.match(line)
            if m:
                group = m.groupdict()
                parameters_dict['role'] = group['role_value']
                continue

            # Protocol Version: 1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                parameters_dict['protocol-version'] = group['protocol_version_number']
                continue

            # Router ID: 10.4.1.1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                parameters_dict['router-id'] = group['router_id_ip']
                continue

            # Null Label:
            m = p5.match(line)
            if m:
                null_label_dict = parameters_dict.setdefault('null-label', {})
                continue

            # ipv4: Implicit
            m = p6.match(line)
            if m:
                group = m.groupdict()
                null_label_dict['null-label-ipv4-address'] = group['null_labels_ipv4']
                continue

            # Session:
            m = p7.match(line)
            if m:
                session_dict = parameters_dict.setdefault('session', {})
                continue

            # Hold time: 180 sec
            m = p8.match(line)
            if m:
                group = m.groupdict()
                session_dict['session-holdtime-sec'] = group['hold_time_seconds']
                continue

            # Keepalive interval: 60 sec
            m = p9.match(line)
            if m:
                group = m.groupdict()
                session_dict['session-keepalive-interval-sec'] = group['keepalive_interval_seconds']
                continue

            # Backoff: Initial:15 sec, Maximum:120 sec
            m = p10.match(line)
            if m:
                group = m.groupdict()
                backoff_dict = session_dict.setdefault('session-backoff', {})
                backoff_dict['backoff-initial-sec'] = group['initial_seconds']
                backoff_dict['backoff-maximum-sec'] = group['maximum_seconds']
                continue

            # Global MD5 password: Disabled
            m = p11.match(line)
            if m:
                group = m.groupdict()
                session_dict['global-md5-password'] = group['global_md5_password']
                continue

            # Discovery:
            m = p12.match(line)
            if m:
                discovery_dict = parameters_dict.setdefault('discovery', {})
                continue

            # Link Hellos: Holdtime:15 sec, Interval:5 sec
            m = p13.match(line)
            if m:
                group = m.groupdict()
                link_hellos_dict = discovery_dict.setdefault('discovery-link-hellos', {})
                link_hellos_dict['link-hellos-hold-time-sec'] = group['link_hellos_hold_time_seconds']
                link_hellos_dict['link-hellos-interval-sec'] = group['link_hellos_interval_seconds']
                continue

            # Targeted Hellos: Holdtime:90 sec, Interval:10 sec
            m = p14.match(line)
            if m:
                group = m.groupdict()
                target_hellos_dict = discovery_dict.setdefault('discovery-target-hellos', {})
                target_hellos_dict['target-hellos-hold-time-sec'] = group['targeted_hellos_hold_time_seconds']
                target_hellos_dict['target-hellos-interval-sec'] = group['targeted_hellos_interval_seconds']
                continue

            # Quick-start: Enabled (by default)
            m = p15.match(line)
            if m:
                group = m.groupdict()
                discovery_dict['discovery-quick-start'] = group['quick_start']
                continue

            # Transport address:
            m = p16.match(line)
            if m:
                transport_address_dict = discovery_dict.setdefault('discovery-transport-address', {})
                continue

            # IPv4: 10.4.1.1
            m = p17.match(line)
            if m:
                group = m.groupdict()
                transport_address_dict['transport-ipv4-address'] = group['transport_address_ipv4_ip']
                continue

            # Graceful Restart:
            m = p18.match(line)
            if m:
                graceful_restart_dict = parameters_dict.setdefault('graceful-restart', {})
                continue

            # Enabled
            m = p19.match(line)
            if m:
                group = m.groupdict()
                graceful_restart_dict['graceful-restart-status'] = group['graceful_restart_value']
                continue

            # Reconnect Timeout:120 sec, Forwarding State Holdtime:180 sec
            m = p20.match(line)
            if m:
                group = m.groupdict()
                reconnect_timeout_dict = graceful_restart_dict.setdefault('graceful-restart-reconnect-timeout', {})
                reconnect_timeout_dict['reconnect-timeout-time-sec'] = group['reconnect_timeout_seconds']
                reconnect_timeout_dict['reconnect-timeout-forward-state-holdtime-sec'] = group['forwarding_state_holdtime_seconds']
                continue

            # NSR: Enabled, Sync-ed
            m = p21.match(line)
            if m:
                group = m.groupdict()
                nrs_dict = parameters_dict.setdefault('nsr', {})
                nrs_dict['nsr-status'] = group['nsr_value']

                if group['synced_value']:
                    nrs_dict['nsr-sync-ed-status'] = group['synced_value']
                continue

            # Timeouts:
            m = p22.match(line)
            if m:
                timeouts_dict = parameters_dict.setdefault('timeouts', {})
                continue

            # Housekeeping periodic timer: 10 sec
            m = p23.match(line)
            if m:
                group = m.groupdict()
                timeouts_dict['housekeeping-periodic-timer-timeouts-sec'] = group['housekeeping_periodic_timer_seconds']
                continue

            # Local binding: 300 sec
            m = p24.match(line)
            if m:
                group = m.groupdict()
                timeouts_dict['local-binding-timeouts-sec'] = group['local_binding_seconds']
                continue

            # Forwarding state in LSD: 360 sec
            m = p25.match(line)
            if m:
                group = m.groupdict()
                timeouts_dict['forward-state-lsd-timeouts-sec'] = group['forwarding_state_lsd_seconds']
                continue

            # Delay in AF Binding Withdrawl from peer: 180 sec
            m = p26.match(line)
            if m:
                group = m.groupdict()
                parameters_dict['delay-af-bind-peer-sec'] = group['delay_af_binding_peer_seconds']
                continue

            # Max:
            m = p27.match(line)
            if m:
                max_dict = parameters_dict.setdefault('max', {})
                continue

            # 5000 interfaces (4000 attached, 1000 TE tunnel), 2000 peers
            m = p28.match(line)
            if m:
                group = m.groupdict()

                max_interfaces_dict = max_dict.setdefault('interfaces', {})
                max_interfaces_dict['max-interfaces-units'] = group['max_interface_number']

                if group['attached_interfaces_number']:
                    max_interfaces_dict['attached-interfaces-units'] = group['attached_interfaces_number']

                if group['te_tunnel_number']:
                    max_interfaces_dict['te-tunnel-interfaces-units'] = group['te_tunnel_number']

                max_dict['max-peers-units'] = group['peers_number']
                continue

            # OOR state
            m = p29.match(line)
            if m:
                oor_state_dict = parameters_dict.setdefault('oor-state', {})
                continue

            # Memory: Normal
            m = p30.match(line)
            if m:
                group = m.groupdict()
                oor_state_dict['oor-memory'] = group['oor_memory_value']
                continue

        return ret_dict