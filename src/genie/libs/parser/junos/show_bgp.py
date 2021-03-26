""" show_bgp.py

JunOs parsers for the following show commands:
    * show bgp group brief
    * show bgp group brief | no-more
    * show bgp group detail
    * show bgp group detail | no-more
    * show bgp group summary
    * show bgp summary
    * show bgp neighbor
    * show bgp neighbor {neighbor_address}
    * show bgp summary instance {instance}
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import (Any, Optional, Use, Schema, ListOf)


class ShowBgpGroupBriefSchema(MetaParser):
    """ Schema for:
            * show bgp group brief
            * show bgp group brief | no-more
            * show bgp group detail
            * show bgp group detail | no-more
    """
    """
     schema = {
        'bgp-group-information': {
            'bgp-group': ListOf({
                Optional('bgp-option-information'): {
                    'bgp-options': str,
                    'bgp-options-extended': str,
                    'export-policy': str,
                    'gshut-recv-local-preference': str,
                    'holdtime': str
                },
                Optional('bgp-rib'): ListOf({
                    'accepted-prefix-count': str,
                    'active-prefix-count': str,
                    'advertised-prefix-count': str,
                    'name': str,
                    'received-prefix-count': str,
                    Optional('suppressed-prefix-count'): str
                }),
                'established-count': str,
                'name': str,
                Optional('flap-count'): str,
                Optional('group-flags'): str,
                Optional('group-index'): str,
                Optional('local-as'): str,
                Optional('peer-address'): list,
                Optional('peer-as'): str,
                'peer-count': str,
                'type': str,
                Optional('route-queue'): {
                    'state': str,
                    'timer': str,
                }
            }),
            'bgp-information': {
                'bgp-rib': ListOf({
                    Optional("@junos:style"): str,
                    Optional("accepted-external-prefix-count"): str,
                    Optional("accepted-internal-prefix-count"): str,
                    Optional("accepted-prefix-count"): str,
                    Optional("active-external-prefix-count"): str,
                    Optional("active-internal-prefix-count"): str,
                    "active-prefix-count": str,
                    Optional("bgp-rib-state"): str,
                    Optional("damped-prefix-count"): str,
                    Optional("history-prefix-count"): str,
                    "name": str,
                    Optional("pending-prefix-count"): str,
                    Optional("received-prefix-count"): str,
                    Optional("suppressed-external-prefix-count"): str,
                    Optional("suppressed-internal-prefix-count"): str,
                    "suppressed-prefix-count": str,
                    Optional("total-external-prefix-count"): str,
                    Optional("total-internal-prefix-count"): str,
                    Optional("total-prefix-count"): str
                }),
                'down-peer-count': str,
                'external-peer-count': str,
                'group-count': str,
                'internal-peer-count': str,
                'peer-count': str,
                'flap-count': str,
            }
        }
    }
    """

    schema = {
        'bgp-group-information': {
            'bgp-group': ListOf({
                Optional('bgp-option-information'): {
                    'bgp-options': str,
                    'bgp-options-extended': str,
                    'export-policy': str,
                    'gshut-recv-local-preference': str,
                    'holdtime': str
                },
                Optional('bgp-rib'): ListOf({
                    'accepted-prefix-count': str,
                    'active-prefix-count': str,
                    'advertised-prefix-count': str,
                    'name': str,
                    'received-prefix-count': str,
                    Optional('suppressed-prefix-count'): str
                }),
                'established-count': str,
                'name': str,
                Optional('flap-count'): str,
                Optional('group-flags'): str,
                Optional('group-index'): str,
                Optional('local-as'): str,
                Optional('peer-address'): list,
                Optional('peer-as'): str,
                'peer-count': str,
                'type': str,
                Optional('route-queue'): {
                    'state': str,
                    'timer': str,
                }
            }),
            'bgp-information': {
                'bgp-rib': ListOf({
                    Optional("@junos:style"): str,
                    Optional("accepted-external-prefix-count"): str,
                    Optional("accepted-internal-prefix-count"): str,
                    Optional("accepted-prefix-count"): str,
                    Optional("active-external-prefix-count"): str,
                    Optional("active-internal-prefix-count"): str,
                    "active-prefix-count": str,
                    Optional("bgp-rib-state"): str,
                    Optional("damped-prefix-count"): str,
                    Optional("history-prefix-count"): str,
                    "name": str,
                    Optional("pending-prefix-count"): str,
                    Optional("received-prefix-count"): str,
                    Optional("suppressed-external-prefix-count"): str,
                    Optional("suppressed-internal-prefix-count"): str,
                    "suppressed-prefix-count": str,
                    Optional("total-external-prefix-count"): str,
                    Optional("total-internal-prefix-count"): str,
                    Optional("total-prefix-count"): str
                }),
                'down-peer-count': str,
                'external-peer-count': str,
                'group-count': str,
                'internal-peer-count': str,
                'peer-count': str,
                'flap-count': str,
            }
        }
    }


class ShowBgpGroupBrief(ShowBgpGroupBriefSchema):
    """ Parser for:
            * show bgp group brief
    """
    cli_command = 'show bgp group brief'

    exclude = ['peer-address']

    def cli(self, output=None):

        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        pevious_table_dict = {}
        table_found = None

        # Group Type: Internal    AS: 65171                  Local AS: 65171
        p1 = re.compile(
            r'^Group +Type: +(?P<type>\S+)( +AS: +(?P<peer_as>\d+))? +'
            r'Local +AS: +(?P<local_as>\d+)$')

        # Name: hktGCS002       Index: 0                   Flags: <Export Eval>
        p2 = re.compile(r'^Name: +(?P<name>\S+) +Index: +(?P<index>\d+) +'
                        r'Flags: +\<(?P<flags>[\S ]+)\>$')

        # Export: [ (v4_WATARI && NEXT-HOP-SELF) ]
        p3 = re.compile(r'^Export: +\[ +(?P<export>(\()?[\S ]+(\))?) +\]$')

        # Options: <Confed>
        p4 = re.compile(r'^Options: +\<(?P<options>Confed|'
                        r'Cluster +Confed|Multihop Confed)\>$')

        # Options: <GracefulShutdownRcv>
        p5 = re.compile(r'^Options: +\<(?P<options>GracefulShutdownRcv)\>$')

        # Holdtime: 0
        p6 = re.compile(r'^Holdtime: +(?P<holdtime>\d+)$')

        # Graceful Shutdown Receiver local-preference: 0
        p7 = re.compile(r'^Graceful +Shutdown +Receiver +local-preference: +'
                        r'(?P<gshut_recv_local_preference>\d+)$')

        # Total peers: 1        Established: 1
        p8 = re.compile(r'^Total +peers: +(?P<total_peers>\d+) +'
                        r'Established: +(?P<established>\d+)$')

        # inet6.0: 0/0/0/0
        # inet.0           : 0/682/682/0
        p9 = re.compile(
            r'^(?P<name>inet(\d+)?\.\d+) *: +(?P<active_prefix_count>\d+)'
            r'\/(?P<received_prefix_count>\d+)\/(?P<accepted_prefix_count>\d+)'
            r'\/(?P<advertised_prefix_count>\d+)$')

        # Groups: 14 Peers: 19   External: 6    Internal: 13   Down peers: 15  Flaps: 359
        p10 = re.compile(
            r'^Groups:\s+(?P<group_count>\d+)\s+Peers:\s+'
            r'(?P<peer_count>\d+)\s+External:\s+(?P<external_peer_count>\d+)'
            r'\s+Internal:\s+(?P<internal_peer_count>\d+)\s+Down\s+peers:\s+'
            r'(?P<down_peer_count>\d+)\s+Flaps:\s+(?P<flap_count>\d+)$')

        # 1366        682          0          0          0          0
        p11 = re.compile(
            r'^(?P<tot_paths>\d+) +(?P<act_paths>\d+) +'
            r'(?P<suppressed>\d+) +(?P<history>\d+) +(?P<damp_state>\d+) +'
            r'(?P<pending>\d+)$')

        # Table inet.0
        p12 = re.compile(r'^Table +(?P<name>\S+)$')

        # Active prefixes:              0
        p13 = re.compile(r'^Active +prefixes: +(?P<active_prefix_count>\d+)$')

        # Received prefixes:            682
        p14 = re.compile(
            r'^Received +prefixes: +(?P<received_prefix_count>\d+)$')

        # Accepted prefixes:            682
        p15 = re.compile(
            r'^Accepted +prefixes: +(?P<accepted_prefix_count>\d+)$')

        # Suppressed due to damping:    0
        p16 = re.compile(
            r'^Suppressed +due +to +damping: +(?P<suppressed_prefix_count>\d+)$'
        )

        # Advertised prefixes:          682
        p17 = re.compile(
            r'^Advertised +prefixes: +(?P<advertised_prefix_count>\d+)$')

        # Received external prefixes:   684
        p18 = re.compile(
            r'^Received +external +prefixes: +(?P<received_external_prefixes>\d+)$'
        )

        # Active external prefixes:     682
        p19 = re.compile(
            r'^Active +external +prefixes: +(?P<active_external_prefixes>\d+)$'
        )

        # Externals suppressed:         0
        p20 = re.compile(
            r'^Externals +suppressed: +(?P<externals_suppressed>\d+)$')

        # Received internal prefixes:   682
        p21 = re.compile(
            r'^Received +internal +prefixes: +(?P<received_internal_prefixes>\d+)$'
        )

        # Active internal prefixes:     0
        p22 = re.compile(
            r'^Active +internal +prefixes: +(?P<active_internal_prefixes>\d+)$'
        )

        # Internals suppressed:         0
        p23 = re.compile(
            r'^Internals +suppressed: +(?P<internal_suppressed>\d+)$')

        # RIB State: BGP restart is complete
        p24 = re.compile(r'^RIB +State: +(?P<rib_state>[\S\s]+)$')

        # Route Queue Timer: unset Route Queue: empty
        p25 = re.compile(
            r'^Route +Queue +Timer: +(?P<timer>\w+) +Route +Queue: +(?P<state>\w+)$'
        )

        # 10.189.5.253+179
        pIp = re.compile(r'^(?P<peer_address>\S+)$')

        # hktGCS002    Internal   1         1
        # v6_hktGCS002 Internal   1         1
        # sjkGDS221-EC11 External 1         1
        p26 = re.compile(r'^(?P<name>\S+) +(?P<type>Internal|External) '
                         r'+(?P<peer_count>\d+) +(?P<established_count>\d+)$')

        # inet.3           : 2/2/2/0 External: 2/2/2/0 Internal: 0/0/0/0
        p27 = re.compile(r'^(?P<name>inet(\d+)?\.\d+) *: '
                         r'+(?P<active_prefix_count>\d+)\/'
                         r'(?P<received_prefix_count>\d+)\/'
                         r'(?P<accepted_prefix_count>\d+)\/'
                         r'(?P<suppressed_prefix_count>\d+) '
                         r'+External: +(?P<active_external_prefix_count>\d+)\/'
                         r'(?P<total_external_prefix_count>\d+)\/'
                         r'(?P<accepted_external_prefix_count>\d+)\/'
                         r'(?P<suppressed_external_prefix_count>\d+) '
                         r'+Internal: +(?P<active_internal_prefix_count>\d+)\/'
                         r'(?P<total_internal_prefix_count>\d+)\/'
                         r'(?P<accepted_internal_prefix_count>\d+)\/'
                         r'(?P<suppressed_internal_prefix_count>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # hktGCS002    Internal   1         1
            # v6_hktGCS002 Internal   1         1
            # sjkGDS221-EC11 External 1         1
            m = p26.match(line)
            if m:
                group = m.groupdict()

                bgp_group_list = ret_dict.setdefault('bgp-group-information', {}). \
                                          setdefault('bgp-group', [])
                bgp_group_dict = {}
                bgp_group_list.append(bgp_group_dict)

                for k, v in group.items():
                    k = k.replace('_', '-')
                    bgp_group_dict[k] = v

                continue

            # Group Type: Internal    AS: 65171                  Local AS: 65171
            m = p1.match(line)
            if m:
                group = m.groupdict()
                bgp_group_list = ret_dict.setdefault('bgp-group-information', {}). \
                    setdefault('bgp-group', [])
                bgp_group_dict = {}
                bgp_group_list.append(bgp_group_dict)
                bgp_group_dict.update({'type': group['type']})
                peer_as = group['peer_as']
                if peer_as:
                    bgp_group_dict.update({'peer-as': peer_as})
                bgp_group_dict.update({'local-as': group['local_as']})
                continue

            # Name: hktGCS002       Index: 0                   Flags: <Export Eval>
            m = p2.match(line)
            if m:
                group = m.groupdict()
                bgp_group_dict.update({'name': group['name']})
                bgp_group_dict.update({'group-index': group['index']})
                bgp_group_dict.update({'group-flags': group['flags']})
                continue

            # Export: [ (v4_WATARI && NEXT-HOP-SELF) ]
            m = p3.match(line)
            if m:
                group = m.groupdict()
                bgp_option_information_dict = bgp_group_dict.setdefault(
                    'bgp-option-information', {})
                bgp_option_information_dict.update(
                    {'export-policy': group['export']})
                continue

            # Options: <Confed>
            m = p4.match(line)
            if m:
                group = m.groupdict()
                bgp_option_information_dict.update(
                    {'bgp-options': group['options']})
                continue

            # Options: <GracefulShutdownRcv>
            m = p5.match(line)
            if m:
                group = m.groupdict()
                bgp_option_information_dict.update(
                    {'bgp-options-extended': group['options']})
                continue

            # Holdtime: 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                bgp_option_information_dict.update(
                    {'holdtime': group['holdtime']})
                continue

            # Graceful Shutdown Receiver local-preference: 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                bgp_option_information_dict.update({
                    'gshut-recv-local-preference':
                    group['gshut_recv_local_preference']
                })
                continue

            # Total peers: 1        Established: 1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                bgp_group_dict.update({'peer-count': group['total_peers']})
                bgp_group_dict.update(
                    {'established-count': group['established']})
                continue

            # inet6.0: 0/0/0/0
            # inet.0           : 0/682/682/0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                bgp_rib_dict_list = bgp_group_dict.setdefault('bgp-rib', [])
                bgp_rib_dict = {}

                for k, v in group.items():
                    entry = k.replace('_', '-')
                    bgp_rib_dict.update({entry: v})

                pevious_table_dict.update({group['name']: bgp_rib_dict})
                bgp_rib_dict_list.append(bgp_rib_dict)
                continue

            # Groups: 14 Peers: 19   External: 6    Internal: 13   Down peers: 15  Flaps: 359
            m = p10.match(line)
            if m:
                table_found = True
                group = m.groupdict()
                bgp_information_dict = ret_dict.setdefault('bgp-group-information', {}). \
                    setdefault('bgp-information', {})

                for k, v in group.items():
                    entry = k.replace('_', '-')
                    bgp_information_dict.update({entry: v})
                continue

            # 1366        682          0          0          0          0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                bgp_info_rib_dict.update(
                    {'total-prefix-count': group['tot_paths']})
                bgp_info_rib_dict.update(
                    {'active-prefix-count': group['act_paths']})
                bgp_info_rib_dict.update(
                    {'suppressed-prefix-count': group['suppressed']})
                bgp_info_rib_dict.update(
                    {'history-prefix-count': group['history']})
                bgp_info_rib_dict.update(
                    {'damped-prefix-count': group['damp_state']})
                bgp_info_rib_dict.update(
                    {'pending-prefix-count': group['pending']})
                continue

            # Table inet.0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                bgp_rib_dict = {}
                bgp_info_rib_dict = {}
                sub_dict = {}
                if not table_found:
                    bgp_rib_dict_list = bgp_group_dict.setdefault(
                        'bgp-rib', [])
                    bgp_rib_dict.update({'name': group['name']})
                    pevious_table_dict.update({group['name']: bgp_rib_dict})
                    bgp_rib_dict_list.append(bgp_rib_dict)
                    sub_dict = bgp_rib_dict
                else:
                    bgp_info_rib_list = bgp_information_dict.setdefault(
                        'bgp-rib', [])
                    bgp_info_rib_dict.update({'name': group['name']})
                    bgp_info_rib_list.append(bgp_info_rib_dict)
                    sub_dict = bgp_info_rib_dict
                continue

            # inet.3           : 2/2/2/0 External: 2/2/2/0 Internal: 0/0/0/0
            m = p27.match(line)
            if m:
                group = m.groupdict()
                bgp_rib_dict = {}
                bgp_info_rib_dict = {}
                sub_dict = {}

                # if output has:
                #   Groups: 14 Peers: 19   External: 6    Internal: 13   Down peers: 15  Flaps: 359
                # table_found == True
                if not table_found:
                    bgp_rib_dict_list = bgp_group_dict.setdefault(
                        'bgp-rib', [])
                    bgp_rib_dict.update({'name': group['name']})
                    pevious_table_dict.update({group['name']: bgp_rib_dict})
                    bgp_rib_dict_list.append(bgp_rib_dict)
                    sub_dict = bgp_rib_dict
                else:
                    bgp_info_rib_list = bgp_information_dict.setdefault(
                        'bgp-rib', [])
                    bgp_info_rib_dict.update({'name': group['name']})
                    bgp_info_rib_list.append(bgp_info_rib_dict)
                    sub_dict = bgp_info_rib_dict

                for k, v in group.items():
                    entry = k.replace('_', '-')
                    sub_dict.update({entry: v})
                continue

            # Active prefixes:              0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update(
                    {'active-prefix-count': group['active_prefix_count']})
                continue

            # Received prefixes:            682
            m = p14.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update(
                    {'received-prefix-count': group['received_prefix_count']})
                continue

            # Accepted prefixes:            682
            m = p15.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update(
                    {'accepted-prefix-count': group['accepted_prefix_count']})
                continue

            # Suppressed due to damping:    0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({
                    'suppressed-prefix-count':
                    group['suppressed_prefix_count']
                })
                continue

            # Advertised prefixes:          682
            m = p17.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({
                    'advertised-prefix-count':
                    group['advertised_prefix_count']
                })
                continue

            # Received external prefixes:   684
            m = p18.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({
                    'total-external-prefix-count':
                    group['received_external_prefixes']
                })
                continue

            # Active external prefixes:     682
            m = p19.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({
                    'active-external-prefix-count':
                    group['active_external_prefixes']
                })
                continue

            # Externals suppressed:         0
            m = p20.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({
                    'suppressed-external-prefix-count':
                    group['externals_suppressed']
                })
                continue

            # Received internal prefixes:   682
            m = p21.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({
                    'total-internal-prefix-count':
                    group['received_internal_prefixes']
                })
                continue

            # Active internal prefixes:     0
            m = p22.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({
                    'active-internal-prefix-count':
                    group['active_internal_prefixes']
                })
                continue

            # Internals suppressed:         0
            m = p23.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({
                    'suppressed-internal-prefix-count':
                    group['internal_suppressed']
                })
                continue

            # RIB State: BGP restart is complete
            m = p24.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({'bgp-rib-state': group['rib_state']})
                continue

            # Route Queue Timer: unset Route Queue: empty
            m = p25.match(line)
            if m:
                group = m.groupdict()
                route_queue_dict = bgp_group_dict.setdefault('route-queue', {})
                route_queue_dict.update({'state': group['state']})
                route_queue_dict.update({'timer': group['timer']})
                continue

            # 10.189.5.253+179
            m = pIp.match(line)
            if m:
                group = m.groupdict()
                if not table_found:
                    peer_address_list = bgp_group_dict.get('peer-address', [])
                    peer_address_list.append(group['peer_address'])
                    bgp_group_dict.update({'peer-address': peer_address_list})
                else:
                    table_name = group['peer_address']
                    bgp_info_rib_list = bgp_information_dict.setdefault(
                        'bgp-rib', [])
                    bgp_info_rib_dict = {}
                    bgp_info_rib_dict.update({'name': table_name})
                    bgp_info_rib_list.append(bgp_info_rib_dict)
                continue
        return ret_dict


class ShowBgpGroupBriefNoMore(ShowBgpGroupBrief):
    """ Parser for:
            * show bgp group brief | no-more
    """
    cli_command = 'show bgp group brief | no-more'

    def cli(self, output=None):

        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return super().cli(output=out)


class ShowBgpGroupDetail(ShowBgpGroupBrief):
    """ Parser for:
            * show bgp group detail
            * show bgp group detail | no-more
    """
    cli_command = 'show bgp group detail'

    def cli(self, output=None):

        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return super().cli(output=out)


class ShowBgpGroupDetailNoMore(ShowBgpGroupDetail):
    """ Parser for:
            * show bgp group detail | no-more
    """
    cli_command = 'show bgp group detail | no-more'

    def cli(self, output=None):

        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return super().cli(output=out)


class ShowBgpGroupSummary(ShowBgpGroupBrief):
    """
    Parser for:
    * show bgp group summary
    """
    cli_command = 'show bgp group summary'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return super().cli(output=out)


class ShowBgpGroupSummaryNoMore(ShowBgpGroupSummary):
    """
    Parser for:
    * show bgp group summary | no-more
    """
    cli_command = 'show bgp group summary | no-more'

    def cli(self, output=None):

        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        return super().cli(output=out)



class ShowBgpSummarySchema(MetaParser):
    """
        schema = {
            "bgp-information": {
                "bgp-peer": [
                    {
                        "bgp-rib": [
                            {
                                "accepted-prefix-count": str,
                                "active-prefix-count": str,
                                "name": str,
                                "received-prefix-count": str,
                                "suppressed-prefix-count": str,
                            }
                        ],
                        "description": str,
                        "elapsed-time": {
                            "#text": str,
                            "@junos:seconds": str,
                        },
                        "flap-count": str,
                        "input-messages": str,
                        "output-messages": str,
                        "peer-address": str,
                        "peer-as": str,
                        "peer-state": str,
                        "route-queue-count": str,
                    }
                ],
                "bgp-rib": [
                    {
                    "accepted-external-prefix-count": str,
                    "accepted-internal-prefix-count": str,
                    "accepted-prefix-count": str,
                    "active-external-prefix-count": str,
                    "active-internal-prefix-count": str,
                    "active-prefix-count": str,
                    "bgp-rib-state": str,
                    "damped-prefix-count": str,
                    "history-prefix-count": str,
                    "name": str,
                    "pending-prefix-count": str,
                    "received-prefix-count": str,
                    "suppressed-external-prefix-count": str,
                    "suppressed-internal-prefix-count": str,
                    "suppressed-prefix-count": str,
                    "total-external-prefix-count": str,
                    "total-internal-prefix-count": str,
                    "total-prefix-count": str
                    }
                ],
                "bgp-thread-mode": str,
                "down-peer-count": str,
                "group-count": str,
                "peer-count": str,
            }
        }

    """

    # Main schema
    schema = {
        "bgp-information": {
            "bgp-peer": ListOf({
                Optional('bgp-rib'): ListOf({
                    'accepted-prefix-count': str,
                    'active-prefix-count': str,
                    'name': str,
                    'received-prefix-count': str,
                    'suppressed-prefix-count': str
                }),
                Optional("description"): str,
                "elapsed-time": {
                    "#text": str,
                    Optional("@junos:seconds"): str,
                },
                "flap-count": str,
                "input-messages": str,
                "output-messages": str,
                "peer-address": str,
                "peer-as": str,
                "peer-state": str,
                "route-queue-count": str,
            }),
            "bgp-rib": ListOf({
                Optional("accepted-external-prefix-count"): str,
                Optional("accepted-internal-prefix-count"): str,
                Optional("accepted-prefix-count"): str,
                Optional("active-external-prefix-count"): str,
                Optional("active-internal-prefix-count"): str,
                "active-prefix-count": str,
                Optional("bgp-rib-state"): str,
                "damped-prefix-count": str,
                "history-prefix-count": str,
                "name": str,
                "pending-prefix-count": str,
                Optional("received-prefix-count"): str,
                Optional("suppressed-external-prefix-count"): str,
                Optional("suppressed-internal-prefix-count"): str,
                "suppressed-prefix-count": str,
                Optional("total-external-prefix-count"): str,
                Optional("total-internal-prefix-count"): str,
                "total-prefix-count": str
            }),
            Optional("bgp-thread-mode"): str,
            "down-peer-count": str,
            "group-count": str,
            "peer-count": str,
        }
    }


class ShowBgpSummary(ShowBgpSummarySchema):
    """
    Parser for:
        * show bgp summary
    """
    cli_command = 'show bgp summary'

    def cli(self, output=None):

        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # ============================================================
        # Regex Patterns
        # ============================================================

        # ------------------------------------------------------------
        # p1, p2:
        # 'bgp-information' dict
        # ------------------------------------------------------------
        # Threading mode: BGP I/O
        p1 = re.compile(r'^Threading +mode: +(?P<bgp_thread_mode>[\S\s]+)$')

        # Groups: 14 Peers: 19 Down peers: 15
        p2 = re.compile(r'^Groups: +(?P<group_count>\d+) +Peers: '
                        r'+(?P<peer_count>\d+) +Down +peers: '
                        r'+(?P<down_peer_count>\d+)$')

        # ------------------------------------------------------------
        # p3, p4
        # 'bgp-information': {
        #       'bgp-rib': []
        # ------------------------------------------------------------
        # inet.0
        # inet6.0
        # VRF-TEST001.inet.0
        p3 = re.compile(r'.*(?P<name>(inet|mdt)(\d+)?.\d)$')

        # 1366        682          0          0          0          0
        p4 = re.compile(
            r'^(?P<total_prefix_count>\d+) +(?P<active_prefix_count>\d+) +'
            r'(?P<suppressed_prefix_count>\d+) +(?P<history_prefix_count>\d+) +'
            r'(?P<damped_prefix_count>\d+) +(?P<pending_prefix_count>\d+)$')

        # ------------------------------------------------------------
        # p5:
        # 'bgp-information': {
        #       'bgp-peer': []
        # ------------------------------------------------------------
        # 10.49.216.179           65171          0          0       0       0 29w5d 22:42:36 Connect
        # 2001:db8:eb18:ca45::11       65151          0          0       0       0 29w5d 22:42:36 Connect
        # 10.145.0.2                  3          2          3       0       1           9 0/0/0/0              0/0/0/0
        p5 = re.compile(
            r'^(?P<peer_address>[\d\w:.]+)\s+(?P<peer_as>\d+)\s+'
            r'(?P<input_messages>\d+)\s+(?P<output_messages>\d+)\s+'
            r'(?P<route_queue_count>\d+)\s+(?P<flap_count>\d+)\s+'
            r'(?P<text>[\S\s]+)\s+(?P<peer_state>Active|Connect|Establ|'
            r'([\d\/]+\s+[\d\/]+))$')

        # ------------------------------------------------------------
        # p6:
        # 'bgp-information': {
        #       'bgp-peer': [
        #           {'bgp-rib': {}}
        #       ]
        # ------------------------------------------------------------
        # inet.0: 682/684/684/0
        p6 = re.compile(
            r'^(?P<name>inet(\d+)?\.\d+) *: +(?P<active_prefix_count>\d+)'
            r'\/(?P<received_prefix_count>\d+)\/(?P<accepted_prefix_count>\d+)'
            r'\/(?P<suppressed_prefix_count>\d+)$')

        # ============================================================
        # Build Parsers
        # ============================================================

        parsed_dict = {}
        bgp_info_dict = {'bgp-information': {}}

        for line in out.splitlines():
            line = line.strip()

            # Threading mode: BGP I/O
            # Groups: 14 Peers: 19 Down peers: 15
            m = p1.match(line) or p2.match(line)
            if m:
                for group_key, group_value in m.groupdict().items():
                    entry_key = group_key.replace('_', '-')
                    bgp_info_dict['bgp-information'][entry_key] = group_value

                bgp_info_dict['bgp-information']['bgp-peer'] = []
                bgp_info_dict['bgp-information']['bgp-rib'] = []
                continue

            # ------------------------------------------------------------
            # Build
            #     "bgp-rib": [
            #         {
            #         "accepted-external-prefix-count": str,
            #         "accepted-internal-prefix-count": str,
            #         "accepted-prefix-count": str,
            #         "active-external-prefix-count": str,
            #         "active-internal-prefix-count": str,
            #         "active-prefix-count": str,
            #         "bgp-rib-state": str,
            #         "damped-prefix-count": str,
            #         "history-prefix-count": str,
            #         "name": str,
            #         "pending-prefix-count": str,
            #         "received-prefix-count": str,
            #         "suppressed-external-prefix-count": str,
            #         "suppressed-internal-prefix-count": str,
            #         "suppressed-prefix-count": str,
            #         "total-external-prefix-count": str,
            #         "total-internal-prefix-count": str,
            #         "total-prefix-count": str
            #         }
            #     ],
            # ------------------------------------------------------------

            # inet.0
            # inet6.0
            m = p3.match(line)
            if m:
                bgp_rib_dict = {}
                bgp_rib_dict['name'] = m.groupdict()['name']
                continue

            # 1366        682          0          0          0          0
            m = p4.match(line)
            if m:
                for key, value in m.groupdict().items():
                    key = key.replace('_', '-')
                    bgp_rib_dict[key] = value

                bgp_info_dict['bgp-information']['bgp-rib'].append(
                    bgp_rib_dict)
                continue

            # ------------------------------------------------------------
            # Build
            #       "bgp-peer": [
            #                     {
            #                         "bgp-rib": [
            #                             {
            #                                 "accepted-prefix-count": str,
            #                                 "active-prefix-count": str,
            #                                 "name": str,
            #                                 "received-prefix-count": str,
            #                                 "suppressed-prefix-count": str,
            #                             }
            #                         ],
            #                         "description": str,
            #                         "elapsed-time": {
            #                             "#text": str,
            #                             "@junos:seconds": str,
            #                         },
            #                         "flap-count": str,
            #                         "input-messages": str,
            #                         "output-messages": str,
            #                         "peer-address": str,
            #                         "peer-as": str,
            #                         "peer-state": str,
            #                         "route-queue-count": str,
            #                     }
            #                 ],
            # ------------------------------------------------------------

            # 10.49.216.179           65171          0          0       0       0 29w5d 22:42:36 Connect
            # 2001:db8:eb18:ca45::11       65151          0          0       0       0 29w5d 22:42:36 Connect
            # 10.145.0.2                  3          2          3       0       1           9 0/0/0/0              0/0/0/0
            # 10.64.4.4               65000         71         71       0       0       31:15 0/1/1/0              0/0/0/0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                bgp_peer_dict = {}

                special_case_state = re.compile(r'([\d\/]+\s+[\d\/]+)')

                for key, value in group.items():
                    if key == 'text':
                        bgp_peer_dict['elapsed-time'] = {'#text': value}
                        continue
                    key = key.replace('_', '-')

                    bgp_peer_dict[key] = value

                bgp_info_dict['bgp-information']['bgp-peer'].append(
                    bgp_peer_dict)
                continue

            # inet.0: 682/684/684/0
            m = p6.match(line)
            if m:
                if 'bgp-rib' not in bgp_peer_dict:
                    bgp_peer_dict['bgp-rib'] = []
                bgp_peer_rib_dict = {}

                for key, value in m.groupdict().items():
                    key = key.replace('_', '-')
                    bgp_peer_rib_dict[key] = value

                bgp_peer_dict['bgp-rib'].append(bgp_peer_rib_dict)
                continue

        # Handle the empty output
        if bool(bgp_info_dict['bgp-information']):
            parsed_dict.update(bgp_info_dict)

        return parsed_dict

class ShowBgpSummaryInstance(ShowBgpSummary):
    """
    Parser for:
        * show bgp summary instance {instance}
    """
    cli_command = 'show bgp summary instance {instance}'

    def cli(self, instance, output=None):

        if not output:
            out = self.device.execute(self.cli_command.format(
                instance=instance
            ))
        else:
            out = output

        return super().cli(output=out)


class ShowBgpNeighborSchema(MetaParser):
    """ Schema for:
            * show bgp neighbor
    """

    schema = {
        "bgp-information": {
                "bgp-peer": ListOf({
                    "bgp-option-information": {
                        "bgp-options": str,
                        Optional("bgp-options2"): bool,
                        Optional("bgp-options-extended"): str,
                        Optional("export-policy"): str,
                        Optional("gshut-recv-local-preference"): str,
                        Optional("holdtime"): str,
                        Optional("import-policy"): str,
                        Optional("local-address"): str,
                        Optional("preference"): str,
                        Optional("authentication-configured"): bool,
                        Optional("address-families"): str
                    },
                    Optional("description"): str,
                    Optional('active-holdtime'): str,
                    Optional('local-id'): str,
                    Optional('peer-id'): str,
                    "flap-count": str,
                    "last-error": str,
                    "last-event": str,
                    "last-state": str,
                    "local-as": str,
                    "peer-address": str,
                    "peer-as":str,
                    Optional("peer-cfg-rti"):str,
                    Optional("peer-fwd-rti"):str,
                    Optional("peer-group"):str,
                    "peer-state":str,
                    "peer-type":str,
                    'peer-flags':str,
                    'local-address':str,
                    Optional('route-reflector-client'):bool,
                    Optional("peer-index"):str,
                    Optional("last-flap-event"):str,
                    Optional("bgp-peer-iosession"): {
                        "iosession-thread-name": str,
                        "iosession-state": str
                    },
                    Optional("bgp-output-queue"):
                    ListOf({
                        "count": str,
                        "number": str,
                        "rib-adv-nlri": str,
                        "table-name": str
                    }),
                    Optional("peer-addpath-not-supported"):bool,
                    Optional("peer-no-llgr-restarter"):bool,
                    Optional("group-index"):str,
                    Optional("bgp-rib"):
                    ListOf({
                        "accepted-prefix-count": str,
                        "active-prefix-count": str,
                        "advertised-prefix-count": str,
                        "bgp-rib-state": str,
                        "name": str,
                        "received-prefix-count": str,
                        "rib-bit": str,
                        "send-state": str,
                        "suppressed-prefix-count": str
                    }),
                    Optional("bgp-bfd"): {
                        "bfd-configuration-state": str,
                        "bfd-operational-state": str
                    },
                    Optional("iosession-thread-name"):str,
                    Optional("bgp-error"):
                    ListOf({
                        "name": str,
                        "receive-count": str,
                        "send-count": str
                    }),
                    Optional("keepalive-interval"):str,
                    Optional("peer-no-restart"):bool,
                    Optional("iosession-state"):str,
                    Optional("entropy-label-info"): {
                        "entropy-label": str,
                        "entropy-label-capability": str,
                        "entropy-label-no-next-hop-validation": str,
                        "entropy-label-stitching-capability": str,
                        "nlri-type": str
                    },
                    Optional("last-checked"):str,
                    Optional("input-refreshes"):str,
                    Optional("input-messages"):str,
                    Optional("peer-stale-route-time-configured"):str,
                    Optional("nlri-type-session"):str,
                    Optional("nlri-type-peer"):str,
                    Optional("local-ext-nh-color-nlri"):str,
                    Optional("entropy-label-capability"):str,
                    Optional("output-octets"):str,
                    Optional("input-updates"):str,
                    Optional("peer-restart-flags-received"):str,
                    Optional("peer-end-of-rib-received"):str,
                    Optional("nlri-type"):str,
                    Optional("peer-end-of-rib-sent"):str,
                    Optional("output-updates"):str,
                    Optional("last-received"):str,
                    Optional("input-octets"):str,
                    Optional("peer-4byte-as-capability-advertised"):str,
                    Optional("peer-restart-nlri-configured"):str,
                    Optional("peer-restart-nlri-negotiated"):str,
                    Optional("output-messages"):str,
                    Optional("output-refreshes"):str,
                    Optional("entropy-label"):str,
                    Optional("peer-4byte-as-capability-advertised"):str,
                    Optional("peer-restart-nlri-configured"):str,
                    Optional("peer-restart-nlri-negotiated"):str,
                    Optional("output-messages"):str,
                    Optional("output-refreshes"):str,
                    Optional("entropy-label"):str,
                    Optional("entropy-label-no-next-hop-validation"):str,
                    Optional("last-sent"):str,
                    Optional("entropy-label-stitching-capability"):str,
                    Optional("peer-refresh-capability"):str,
                    Optional("snmp-index"):str,
                }),
                Optional('is-bgp-running'): bool
            }
        }


class ShowBgpNeighbor(ShowBgpNeighborSchema):
    """ Parser for:
            * show bgp neighbor
            * show bgp neighbor {neighbor_address}
    """
    cli_command = ['show bgp neighbor',
        'show bgp neighbor {neighbor_address}']

    def cli(self, neighbor_address=None, output=None):
        if not output:
            if neighbor_address:
                out = self.device.execute(self.cli_command[1].format(
                    neighbor_address=neighbor_address
                ))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Peer: 10.49.216.179 AS 65171   Local: 10.189.5.252 AS 65171
        p1 = re.compile(
            r'^Peer: +(?P<peer_address>\S+) +AS +(?P<peer_as>\d+) +Local: +(?P<local_address>\S+) +AS +(?P<local_as>\d+)$'
        )
        # Description: v4_pyats
        p2 = re.compile(r'^Description: +(?P<description>\S+)$')
        # Group: v4_pyats             Routing-Instance: master
        p3 = re.compile(
            r'^Group: +(?P<peer_group>\S+) +Routing-Instance: +(?P<peer_cfg_rti>\S+)$'
        )
        # Forwarding routing-instance: master
        p4 = re.compile(
            r'^Forwarding +routing-instance: +(?P<peer_fwd_rti>\S+)$')
        # Type: Internal    State: Active       (route reflector client)Flags: <>
        # Type: External    State: Established    Flags: <Sync InboundConvergencePending>
        p5 = re.compile(
            r'^Type: +(?P<peer_type>\S+) +State: +(?P<peer_state>\S+) +(?P<route_reflector>\(route +reflector +client\))?Flags: +<(?P<peer_flags>[\s\S]*)>$'
        )
        # Last State: Idle          Last Event: Start
        p6 = re.compile(
            r'^Last +State: +(?P<last_state>\S+) +Last +Event: +(?P<last_event>\S+)'
        )
        # Last Error: None
        p7 = re.compile(r'^Last +Error: +(?P<last_error>[\S\s]+)$')
        # Export: [ v4_pyats_NO-DEFAULT ] Import: [ 11 ]
        p8 = re.compile(
            r'^Export: +\[ +(?P<export_policy>\S+) +\] +Import: +\[ +(?P<import_policy>\S+) +\]$'
        )

        # Export: [ v4_pyats_NO-DEFAULT ]
        p8_1 = re.compile(
            r'^Export: +\[ +(?P<export_policy>\S+) +\]$'
        )

        # Import: [ as-path-limit ]
        p8_2 = re.compile(
            r'^Import: +\[ +(?P<import_policy>\S+) +\]$'
        )

        # Options: <Preference LocalAddress HoldTime LogUpDown Cluster PeerAS Refresh Confed>
        # Options: <GracefulShutdownRcv>
        p9 = re.compile(r'^Options: +<(?P<options>[\S\s]+)>$')

        # Holdtime: 30 Preference: 170
        # Local Address: 10.189.5.252 Holdtime: 720 Preference: 170
        p10 = re.compile(
            r'^(Local +Address: +(?P<local_address>\S+) +)?Holdtime: +(?P<holdtime>\S+) +Preference: +(?P<preference>\S+)$'
        )
        # Graceful Shutdown Receiver local-preference: 0
        p11 = re.compile(
            r'^Graceful +Shutdown +Receiver +local-preference: +(?P<gshut_recv_local_preference>\d+)$'
        )
        # Number of flaps: 0
        p12 = re.compile(r'^Number +of +flaps: +(?P<flap_count>\d+)$')
        # Authentication key is configured
        p13 = re.compile(r'^Authentication +key +is +configured$')
        # Export: [ ((LABELSTACK_O2B || HKG-EC_out) && (NEXT-HOP-SELF && HKG-EC_AddMED)) ]
        p14 = re.compile(r'^Export: +\[ +(?P<export_policy>[\s\S]+) +\]$')
        # Address families configured: inet-unicast inet-labeled-unicast
        p15 = re.compile(
            r'^Address +families +configured: +(?P<address_families>[\S\s]+)$')
        # Type: External    State: Established    Flags: <Sync>
        p16 = re.compile(
            r'^Type: +(?P<peer_type>\S+) +State: +(?P<peer_state>\S+) +Flags: +<(?P<peer_flags>\S*)>$'
        )
        # Last flap event: HoldTime
        p17 = re.compile(r'^Last +flap +event: +(?P<last_flap_event>\S+)')
        # Error: 'Hold Timer Expired Error' Sent: 27 Recv: 40
        p18 = re.compile(
            r'^Error: +\'(?P<name>[\S\s]+)\' +Sent: +(?P<send_count>\d+) +Recv: +(?P<receive_count>\d+)$'
        )
        # Peer ID: 10.169.14.240  Local ID: 10.189.5.252      Active Holdtime: 30
        p19 = re.compile(
            r'^Peer +ID: +(?P<peer_id>[\d\.]+) +Local +ID: +(?P<local_id>[\d\.]+) +Active +Holdtime: +(?P<active_holdtime>\d+)$'
        )
        # Keepalive Interval: 10         Group index: 10   Peer index: 0    SNMP index: 15
        p20 = re.compile(
            r'^Keepalive +Interval: +(?P<keepalive_interval>\d+) +Group +index: +(?P<group_index>\d+) +Peer +index: +(?P<peer_index>\d+) +SNMP +index: +(?P<snmp_index>\d+)$'
        )
        # I/O Session Thread: bgpio-0 State: Enabled
        p21 = re.compile(
            r'^I\/O +Session +Thread: +(?P<iosession_thread_name>\S+) +State: +(?P<iosession_state>\S+)$'
        )
        # BFD: disabled, down
        p22 = re.compile(
            r'^BFD: +(?P<bfd_configuration_state>\S+), +(?P<bfd_operational_state>\S+)$'
        )
        # NLRI for restart configured on peer: inet-unicast inet-labeled-unicast
        p23 = re.compile(
            r'^NLRI +for +restart +configured +on +peer: +(?P<peer_restart_nlri_configured>[\S\s]+)$'
        )
        # NLRI advertised by peer: inet-unicast inet-labeled-unicast
        p24 = re.compile(
            r'^NLRI +advertised +by +peer: +(?P<nlri_type_peer>[\s\S]+)$')
        # NLRI for this session: inet-unicast inet-labeled-unicast
        p25 = re.compile(
            r'^NLRI +for +this +session: +(?P<nlri_type_session>[\s\S]+)$')
        # Peer supports Refresh capability (2)
        p26 = re.compile(
            r'^Peer +supports +Refresh +capability +\((?P<peer_refresh_capability>\d+)\)$'
        )
        # Stale routes from peer are kept for: 300
        p27 = re.compile(
            r'^Stale +routes +from +peer +are +kept +for: +(?P<peer_stale_route_time_configured>\d+)$'
        )
        # Peer does not support Restarter functionality
        p28 = re.compile(
            r'^Peer +does +not +support +Restarter +functionality$')
        # Restart flag received from the peer: Notification
        # Restart flag received from the peer: Restarting Notification
        p29 = re.compile(
            r'^Restart +flag +received +from +the +peer: +(?P<peer_restart_flags_received>[\S\s]+)$'
        )
        # NLRI that restart is negotiated for: inet-unicast inet-labeled-unicast
        p30 = re.compile(
            r'^NLRI +that +restart +is +negotiated +for: +(?P<peer_restart_nlri_negotiated>[\S\s]+)$'
        )
        # NLRI of received end-of-rib markers: inet-unicast inet-labeled-unicast
        p31 = re.compile(
            r'^NLRI +of +received +end-of-rib +markers: +(?P<peer_end_of_rib_received>[\S\s]+)$'
        )
        # NLRI of all end-of-rib markers sent: inet-unicast inet-labeled-unicast
        p32 = re.compile(
            r'^NLRI +of +all +end-of-rib +markers +sent: +(?P<peer_end_of_rib_sent>[\S\s]+)$'
        )
        # Peer does not support LLGR Restarter functionality
        p33 = re.compile(
            r'^Peer +does +not +support +LLGR +Restarter +functionality$')
        # Peer supports 4 byte AS extension (peer-as 65151)
        p34 = re.compile(
            r'^Peer +supports +4 +byte +AS +extension +\(peer-as +(?P<peer_4byte_as_capability_advertised>\S+)\)$'
        )
        # Peer does not support Addpath
        p35 = re.compile(r'^Peer +does +not +support +Addpath$')
        # NLRI(s) enabled for color nexthop resolution: inet-unicast
        p36 = re.compile(
            r'^NLRI\(s\) +enabled +for +color +nexthop +resolution: +(?P<local_ext_nh_color_nlri>\S+)$'
        )
        # Entropy label NLRI: inet-labeled-unicast
        p37 = re.compile(r'^Entropy +label +NLRI: +(?P<nlri_type>[\S\s]+)$')
        #     Entropy label: No; next hop validation: Yes
        p38 = re.compile(
            r'^Entropy +label: +(?P<entropy_label>\S+); +next +hop +validation: +(?P<entropy_label_no_next_hop_validation>\S+)$'
        )
        #     Local entropy label capability: Yes; stitching capability: Yes
        p39 = re.compile(
            r'^Local +entropy +label +capability: +(?P<entropy_label_capability>\S+); +stitching +capability: +(?P<entropy_label_stitching_capability>\S+)$'
        )
        # Table inet.0 Bit: 20000
        p40 = re.compile(r'Table +(?P<name>\S+) +Bit: +(?P<rib_bit>\S+)')
        #     RIB State: BGP restart is complete
        p41 = re.compile(r'^RIB +State: +(?P<bgp_rib_state>[\S\s]+)$')
        #     Send state: in sync
        p42 = re.compile(r'^Send +state: +(?P<send_state>[\S\s]+)$')
        #     Active prefixes:              682
        p43 = re.compile(r'^Active +prefixes: +(?P<active_prefix_count>\d+)$')
        #     Received prefixes:            684
        p44 = re.compile(
            r'^Received +prefixes: +(?P<received_prefix_count>\d+)$')
        #     Accepted prefixes:            684
        p45 = re.compile(
            r'^Accepted +prefixes: +(?P<accepted_prefix_count>\d+)$')
        #     Suppressed due to damping:    0
        p46 = re.compile(
            r'^Suppressed +due +to +damping: +(?P<suppressed_prefix_count>\d+)$'
        )
        #     Advertised prefixes:          0
        p47 = re.compile(
            r'^Advertised +prefixes: +(?P<advertised_prefix_count>\d+)$')
        # Last traffic (seconds): Received 3    Sent 3    Checked 1999164
        p48 = re.compile(
            r'^Last +traffic +\(seconds\): +Received +(?P<last_received>\S+) +Sent +(?P<last_sent>\S+) +Checked +(?P<last_checked>\S+)$'
        )
        # Input messages:  Total 280022 Updates 61419   Refreshes 0     Octets 7137084
        p49 = re.compile(
            r'^Input +messages: +Total +(?P<input_messages>\S+) +Updates +(?P<input_updates>\S+) +Refreshes +(?P<input_refreshes>\S+) +Octets +(?P<input_octets>\S+)$'
        )
        # Output messages: Total 221176 Updates 0       Refreshes 0     Octets 4202359
        p50 = re.compile(
            r'^Output +messages: +Total +(?P<output_messages>\S+) +Updates +(?P<output_updates>\S+) +Refreshes +(?P<output_refreshes>\S+) +Octets +(?P<output_octets>\S+)$'
        )
        # Output Queue[1]: 0            (inet.0, inet-unicast)
        p51 = re.compile(
            r'^Output +Queue\[(?P<number>\d+)\]: +(?P<count>\d+) +\((?P<table_name>\S+), +(?P<rib_adv_nlri>\S+)\)$'
        )
        # BGP is not running
        p52 = re.compile(r'^BGP +is +not +running+$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Peer: 10.49.216.179 AS 65171   Local: 10.189.5.252 AS 65171
            m = p1.match(line)
            if m:
                group = m.groupdict()
                entry_list = ret_dict.setdefault("bgp-information",
                                                 {}).setdefault(
                                                     "bgp-peer", [])
                entry = {}
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                entry_list.append(entry)
                continue

            # Description: v4_pyats
            m = p2.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Group: v4_pyats             Routing-Instance: master
            m = p3.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Forwarding routing-instance: master
            m = p4.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Type: Internal    State: Active       (route reflector client)Flags: <>
            # Type: External    State: Established    Flags: <Sync  Sync>
            m = p5.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]

                entry['peer-type'] = group['peer_type']
                entry['peer-state'] = group['peer_state']
                entry['peer-flags'] = group['peer_flags']

                if group['route_reflector']:
                    entry['route-reflector-client'] = True
                continue

            # Last State: Idle          Last Event: Start
            m = p6.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Last Error: None
            m = p7.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Export: [ v4_pyats_NO-DEFAULT ] Import: [ 11 ]
            m = p8.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                entry = entry.setdefault("bgp-option-information", {})
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Export: [ v4_pyats_NO-DEFAULT ]
            m = p8_1.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                entry = entry.setdefault("bgp-option-information", {})
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Import: [ as-path-limit ]
            m = p8_2.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                entry = entry.setdefault("bgp-option-information", {})
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Options: <Preference LocalAddress HoldTime LogUpDown Cluster PeerAS Refresh Confed>
            # Options: <GracefulShutdownRcv>
            m = p9.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                entry = entry.setdefault("bgp-option-information", {})
                if "bgp-options" not in entry:
                    entry['bgp-options'] = group['options']
                else:
                    entry['bgp-options2'] = True
                    entry['bgp-options-extended'] = group['options']
                continue

            # Holdtime: 30 Preference: 170
            # Local Address: 10.189.5.252 Holdtime: 720 Preference: 170
            m = p10.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                entry = entry.setdefault("bgp-option-information", {})
                for key, value in group.items():
                    if group[key]:
                        key = key.replace('_', '-')
                        entry[key] = value
                continue

            # Graceful Shutdown Receiver local-preference: 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                entry = entry.setdefault("bgp-option-information", {})
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Number of flaps: 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Authentication key is configured
            m = p13.match(line)
            if m:
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                entry = entry.setdefault("bgp-option-information", {})
                entry['authentication-configured'] = True
                continue

            # Export: [ ((LABELSTACK_O2B || HKG-EC_out) && (NEXT-HOP-SELF && HKG-EC_AddMED)) ]
            m = p14.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                entry = entry.setdefault("bgp-option-information", {})
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Address families configured: inet-unicast inet-labeled-unicast
            m = p15.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                entry = entry.setdefault("bgp-option-information", {})
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Type: External    State: Established    Flags: <Sync>
            m = p16.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Last flap event: HoldTime
            m = p17.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Error: 'Hold Timer Expired Error' Sent: 27 Recv: 40
            m = p18.match(line)
            if m:
                group = m.groupdict()
                entry = {}
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                entry_location = ret_dict["bgp-information"]["bgp-peer"][-1]
                entry_location.setdefault("bgp-error", []).append(entry)
                continue

            # Peer ID: 10.169.14.240  Local ID: 10.189.5.252      Active Holdtime: 30
            m = p19.match(line)
            if m:
                group = m.groupdict()
                entry = {}
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                ret_dict["bgp-information"]["bgp-peer"][-1].update(entry)

                continue

            # Keepalive Interval: 10         Group index: 10   Peer index: 0    SNMP index: 15
            m = p20.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # I/O Session Thread: bgpio-0 State: Enabled
            m = p21.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                entry = entry.setdefault("bgp-peer-iosession", {})
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # BFD: disabled, down
            m = p22.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                entry = entry.setdefault("bgp-bfd", {})
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # NLRI for restart configured on peer: inet-unicast inet-labeled-unicast
            m = p23.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # NLRI advertised by peer: inet-unicast inet-labeled-unicast
            m = p24.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # NLRI for this session: inet-unicast inet-labeled-unicast
            m = p25.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Peer supports Refresh capability (2)
            m = p26.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Stale routes from peer are kept for: 300
            m = p27.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Peer does not support Restarter functionality
            m = p28.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                entry['peer-no-restart'] = True
                continue

            # Restart flag received from the peer: Notification
            m = p29.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # NLRI that restart is negotiated for: inet-unicast inet-labeled-unicast
            m = p30.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # NLRI of received end-of-rib markers: inet-unicast inet-labeled-unicast
            m = p31.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # NLRI of all end-of-rib markers sent: inet-unicast inet-labeled-unicast
            m = p32.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Peer does not support LLGR Restarter functionality
            m = p33.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                entry['peer-no-llgr-restarter'] = True
                continue

            # Peer supports 4 byte AS extension (peer-as 65151)
            m = p34.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Peer does not support Addpath
            m = p35.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                entry['peer-addpath-not-supported'] = True
                continue

            # NLRI(s) enabled for color nexthop resolution: inet-unicast
            m = p36.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Entropy label NLRI: inet-labeled-unicast
            m = p37.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            #     Entropy label: No; next hop validation: Yes
            m = p38.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            #     Local entropy label capability: Yes; stitching capability: Yes
            m = p39.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Table inet.0 Bit: 20000
            m = p40.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                entry_list = entry.setdefault("bgp-rib", [])
                entry = {}
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                entry_list.append(entry)
                continue

            #     RIB State: BGP restart is complete
            m = p41.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]["bgp-rib"][
                    -1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            #     Send state: in sync
            m = p42.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]["bgp-rib"][
                    -1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            #     Active prefixes:              682
            m = p43.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]["bgp-rib"][
                    -1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            #     Received prefixes:            684
            m = p44.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]["bgp-rib"][
                    -1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            #     Accepted prefixes:            684
            m = p45.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]["bgp-rib"][
                    -1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            #     Suppressed due to damping:    0
            m = p46.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]["bgp-rib"][
                    -1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            #     Advertised prefixes:          0
            m = p47.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]["bgp-rib"][
                    -1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Last traffic (seconds): Received 3    Sent 3    Checked 1999164
            m = p48.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Input messages:  Total 280022 Updates 61419   Refreshes 0     Octets 7137084
            m = p49.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Output messages: Total 221176 Updates 0       Refreshes 0     Octets 4202359
            m = p50.match(line)
            if m:
                group = m.groupdict()
                entry = ret_dict["bgp-information"]["bgp-peer"][-1]
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                continue

            # Output Queue[1]: 0            (inet.0, inet-unicast)
            m = p51.match(line)
            if m:
                group = m.groupdict()
                entry_list = ret_dict["bgp-information"]["bgp-peer"][-1]
                entry_list = entry_list.setdefault("bgp-output-queue", [])
                entry = {}
                for key, value in group.items():
                    key = key.replace('_', '-')
                    entry[key] = value
                entry_list.append(entry)
                continue

            # BGP is not running
            m = p52.match(line)
            if m:
                entry = ret_dict.setdefault('bgp-information', {})
                entry.setdefault('bgp-peer', [])
                entry['is-bgp-running'] = False
                continue

        return ret_dict
