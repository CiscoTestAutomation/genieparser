"""show_mpls.py

JUNOS parsers for the following commands:
    * show mpls lsp name {name} detail
    * show mpls lsp name {name} extensive
"""

import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import Any, Optional, Use, Schema


class ShowMPLSLSPNameDetailSchema(MetaParser):
    """ Schema for
        * show mpls lsp name {name} detail
    """
    def validate_rsvp_session_data(value):
        if not isinstance(value, list):
            raise SchemaError('RSVP session data is not a list')

        def validate_packet_information(value):
            if not isinstance(value, list):
                raise SchemaError('Packet information is not a list')

            packet_information = Schema({
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
            })

            for item in value:
                packet_information.validate(item)
            return value

        def validate_explicit_route(value):
            if not isinstance(value, list):
                raise SchemaError('Explicit route is not a list')

            explicit_route = Schema({
                "address": str,
            })

            for item in value:
                explicit_route.validate(item)
            return value

        def validate_record_route(value):
            if not isinstance(value, list):
                raise SchemaError('Record route is not a list')

            record_route = Schema({
                "address": str,
            })

            for item in value:
                record_route.validate(item)
            return value

        rsvp_session_data = Schema({
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
                "packet-information": Use(validate_packet_information),
                "adspec": str,
                "explicit-route": {
                    "explicit-route-element": Use(validate_explicit_route)
                },
                "record-route": {
                    Optional("record-route-element"): Use(validate_record_route),
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

        for item in value:
            rsvp_session_data.validate(item)
        return value

    schema = {
        "mpls-lsp-information": {
            "rsvp-session-data": Use(validate_rsvp_session_data)
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
