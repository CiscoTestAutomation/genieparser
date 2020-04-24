""" show_bgp.py

JunOs parsers for the following show commands:
    * show bgp group brief
    * show bgp group brief | no-more
    * show bgp group detail
    * show bgp group detail | no-more
    * show bgp group summary
    * show bgp neighbor
    * show bgp neighbor {neighbor_address}
    * show bgp summary
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any, 
        Optional, Use, SchemaTypeError, Schema)


class ShowBgpGroupBriefSchema(MetaParser):
    """ Schema for:
            * show bgp group brief
            * show bgp group brief | no-more
            * show bgp group detail
            * show bgp group detail | no-more
    """
    """
        schema = {
            "bgp-group-information": {
                "bgp-group": [
                    {
                        {
                            'bgp-option-information': {
                            'bgp-options': str,
                            'bgp-options-extended': str,
                            'export-policy': str,
                            'gshut-recv-local-preference': str,
                            'holdtime': str
                        },
                        Optional('bgp-rib'): Use(validate_bgp_rib),
                        'established-count': str,
                        'name': str,
                        Optional('flap-count'): str,
                        'group-flags': str,
                        'group-index': str,
                        'local-as': str,
                        'peer-address': list,
                        Optional('peer-as'): str,
                        'peer-count': str,
                        'type': str,
                        Optional('route-queue'): {
                            'state': str,
                            'timer': str,
                        }
                    }
                ],
                "bgp-information": {
                    "bgp-rib": [
                        {
                            'active-prefix-count': str,
                            Optional('damped-prefix-count'): str,
                            Optional('history-prefix-count'): str,
                            'name': str,
                            Optional('pending-prefix-count'): str,
                            'suppressed-prefix-count': str,
                            Optional('total-prefix-count'): str,
                            Optional('active-external-prefix-count'): str,
                            Optional('active-internal-prefix-count'): str,
                            Optional('suppressed-external-prefix-count'): str,
                            Optional('accepted-prefix-count'): str,
                            Optional('total-internal-prefix-count'): str,
                            Optional('received-prefix-count'): str,
                            Optional('total-external-prefix-count'): str,
                            Optional('suppressed-internal-prefix-count'): str,
                            Optional('bgp-rib-state'): str,
                        }
                    ],
                    "down-peer-count": "str",
                    "external-peer-count": "str",
                    "group-count": "str",
                    "internal-peer-count": "str"
                }
            }
        }
    """
    def validate_bgp_group_list(value):
        if not isinstance(value, list):
            raise SchemaTypeError('bgp-rib is not a list')

        def validate_bgp_rib(value):
            if not isinstance(value, list):
                raise SchemaTypeError('bgp-rib is not a list')
            bgp_rib_schema = Schema(
                {
                    'accepted-prefix-count': str,
                    'active-prefix-count': str,
                    'advertised-prefix-count': str,
                    'name': str,
                    'received-prefix-count': str,
                    Optional('suppressed-prefix-count'): str
                })
            for item in value:
                bgp_rib_schema.validate(item)
            return value
        bgp_group_list_schema = Schema(
            {
                Optional('bgp-option-information'): {
                        'bgp-options': str,
                        'bgp-options-extended': str,
                        'export-policy': str,
                        'gshut-recv-local-preference': str,
                        'holdtime': str
                    },
                Optional('bgp-rib'): Use(validate_bgp_rib),
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
            })
        for item in value:
            bgp_group_list_schema.validate(item)
        return value
    
    def validate_bgp_info_bgp_rib_list(value):
        if not isinstance(value, list):
            raise SchemaTypeError('bgp-information bgp-rib is not a list')
        bgp_rib_list_schema = Schema(
            {
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
            })
        for item in value:
            bgp_rib_list_schema.validate(item)
        return value

    schema = {
        'bgp-group-information': {
            'bgp-group': Use(validate_bgp_group_list),
            'bgp-information': {
                'bgp-rib': Use(validate_bgp_info_bgp_rib_list),
                'down-peer-count': str,
                'external-peer-count': str,
                'group-count': str,
                'internal-peer-count': str,
                'peer-count': str,
                'flap-count': str,
                }}}


class ShowBgpGroupBrief(ShowBgpGroupBriefSchema):
    """ Parser for:
            * show bgp group brief
    """
    cli_command = 'show bgp group brief'
    
    exclude = [
        'peer-address'
    ]
    
    def cli(self, output=None):

        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        pevious_table_dict = {}
        table_found = None

        # Group Type: Internal    AS: 65171                  Local AS: 65171
        p1 = re.compile(r'^Group +Type: +(?P<type>\S+)( +AS: +(?P<peer_as>\d+))? +'
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
        p9 = re.compile(r'^(?P<name>inet(\d+)?\.\d+) *: +(?P<active_prefix_count>\d+)'
                        r'\/(?P<received_prefix_count>\d+)\/(?P<accepted_prefix_count>\d+)'
                        r'\/(?P<advertised_prefix_count>\d+)$')
        
        # Groups: 14 Peers: 19   External: 6    Internal: 13   Down peers: 15  Flaps: 359
        p10 = re.compile(r'^Groups:\s+(?P<group_count>\d+)\s+Peers:\s+'
                r'(?P<peer_count>\d+)\s+External:\s+(?P<external_peer_count>\d+)'
                r'\s+Internal:\s+(?P<internal_peer_count>\d+)\s+Down\s+peers:\s+'
                r'(?P<down_peer_count>\d+)\s+Flaps:\s+(?P<flap_count>\d+)$')
        
        # 1366        682          0          0          0          0
        p11 = re.compile(r'^(?P<tot_paths>\d+) +(?P<act_paths>\d+) +'
                r'(?P<suppressed>\d+) +(?P<history>\d+) +(?P<damp_state>\d+) +'
                r'(?P<pending>\d+)$')
        
        # Table inet.0
        p12 = re.compile(r'^Table +(?P<name>\S+)$')

        # Active prefixes:              0
        p13 = re.compile(r'^Active +prefixes: +(?P<active_prefix_count>\d+)$')

        # Received prefixes:            682
        p14 = re.compile(r'^Received +prefixes: +(?P<received_prefix_count>\d+)$')

        # Accepted prefixes:            682
        p15 = re.compile(r'^Accepted +prefixes: +(?P<accepted_prefix_count>\d+)$')

        # Suppressed due to damping:    0
        p16 = re.compile(r'^Suppressed +due +to +damping: +(?P<suppressed_prefix_count>\d+)$')

        # Advertised prefixes:          682
        p17 = re.compile(r'^Advertised +prefixes: +(?P<advertised_prefix_count>\d+)$')

        # Received external prefixes:   684
        p18 = re.compile(r'^Received +external +prefixes: +(?P<received_external_prefixes>\d+)$')

        # Active external prefixes:     682
        p19 = re.compile(r'^Active +external +prefixes: +(?P<active_external_prefixes>\d+)$')

        # Externals suppressed:         0
        p20 = re.compile(r'^Externals +suppressed: +(?P<externals_suppressed>\d+)$')

        # Received internal prefixes:   682
        p21 = re.compile(r'^Received +internal +prefixes: +(?P<received_internal_prefixes>\d+)$')

        # Active internal prefixes:     0
        p22 = re.compile(r'^Active +internal +prefixes: +(?P<active_internal_prefixes>\d+)$')

        # Internals suppressed:         0
        p23 = re.compile(r'^Internals +suppressed: +(?P<internal_suppressed>\d+)$')

        # RIB State: BGP restart is complete
        p24 = re.compile(r'^RIB +State: +(?P<rib_state>[\S\s]+)$')

        # Route Queue Timer: unset Route Queue: empty
        p25 = re.compile(r'^Route +Queue +Timer: +(?P<timer>\w+) +Route +Queue: +(?P<state>\w+)$')

        # 10.189.5.253+179
        pIp = re.compile(r'^(?P<peer_address>\S+)$')

        # hktGCS002    Internal   1         1
        # v6_hktGCS002 Internal   1         1
        # sjkGCS001-EC11 External 1         1
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
            # sjkGCS001-EC11 External 1         1
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
                bgp_option_information_dict = bgp_group_dict.setdefault('bgp-option-information', {})
                bgp_option_information_dict.update({'export-policy': group['export']})
                continue

            # Options: <Confed>
            m = p4.match(line)
            if m:
                group = m.groupdict()
                bgp_option_information_dict.update({'bgp-options': group['options']})
                continue

            # Options: <GracefulShutdownRcv>
            m = p5.match(line)
            if m:
                group = m.groupdict()
                bgp_option_information_dict.update({'bgp-options-extended': group['options']})
                continue

            # Holdtime: 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                bgp_option_information_dict.update({'holdtime': group['holdtime']})
                continue

            # Graceful Shutdown Receiver local-preference: 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                bgp_option_information_dict.update({'gshut-recv-local-preference': group['gshut_recv_local_preference']})
                continue

            # Total peers: 1        Established: 1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                bgp_group_dict.update({'peer-count': group['total_peers']})
                bgp_group_dict.update({'established-count': group['established']})
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
                bgp_info_rib_dict.update({'total-prefix-count': group['tot_paths']})
                bgp_info_rib_dict.update({'active-prefix-count': group['act_paths']})
                bgp_info_rib_dict.update({'suppressed-prefix-count': group['suppressed']})
                bgp_info_rib_dict.update({'history-prefix-count': group['history']})
                bgp_info_rib_dict.update({'damped-prefix-count': group['damp_state']})
                bgp_info_rib_dict.update({'pending-prefix-count': group['pending']})
                continue
            
            # Table inet.0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                bgp_rib_dict = {}
                bgp_info_rib_dict = {}
                sub_dict = {}
                if not table_found:
                    bgp_rib_dict_list = bgp_group_dict.setdefault('bgp-rib', [])
                    bgp_rib_dict.update({'name': group['name']})
                    pevious_table_dict.update({group['name']: bgp_rib_dict})
                    bgp_rib_dict_list.append(bgp_rib_dict)
                    sub_dict = bgp_rib_dict
                else:
                    bgp_info_rib_list = bgp_information_dict.setdefault('bgp-rib', [])
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
                    bgp_rib_dict_list = bgp_group_dict.setdefault('bgp-rib', [])
                    bgp_rib_dict.update({'name': group['name']})
                    pevious_table_dict.update({group['name']: bgp_rib_dict})
                    bgp_rib_dict_list.append(bgp_rib_dict)
                    sub_dict = bgp_rib_dict
                else:
                    bgp_info_rib_list = bgp_information_dict.setdefault('bgp-rib', [])
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
                sub_dict.update({'active-prefix-count': group['active_prefix_count']})
                continue

            # Received prefixes:            682
            m = p14.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({'received-prefix-count': group['received_prefix_count']})
                continue

            # Accepted prefixes:            682
            m = p15.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({'accepted-prefix-count': group['accepted_prefix_count']})
                continue

            # Suppressed due to damping:    0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({'suppressed-prefix-count': group['suppressed_prefix_count']})
                continue

            # Advertised prefixes:          682
            m = p17.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({'advertised-prefix-count': group['advertised_prefix_count']})
                continue
            
            # Received external prefixes:   684
            m = p18.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({'total-external-prefix-count': group['received_external_prefixes']})
                continue

            # Active external prefixes:     682
            m = p19.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({'active-external-prefix-count': group['active_external_prefixes']})
                continue

            # Externals suppressed:         0
            m = p20.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({'suppressed-external-prefix-count': group['externals_suppressed']})
                continue

            # Received internal prefixes:   682
            m = p21.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({'total-internal-prefix-count': group['received_internal_prefixes']})
                continue

            # Active internal prefixes:     0
            m = p22.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({'active-internal-prefix-count': group['active_internal_prefixes']})
                continue

            # Internals suppressed:         0
            m = p23.match(line)
            if m:
                group = m.groupdict()
                sub_dict.update({'suppressed-internal-prefix-count': group['internal_suppressed']})
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
                    bgp_info_rib_list = bgp_information_dict.setdefault('bgp-rib', [])
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
    def validate_bgp_rib_list(value):
        if not isinstance(value, list):
            raise SchemaTypeError('bgp-rib is not a list')
        bgp_rib_schema = Schema(
                {
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
                }
            )

        for item in value:
            bgp_rib_schema.validate(item)
        return value

    def validate_bgp_peer_list(value):
        if not isinstance(value, list):
            raise SchemaTypeError('bgp-peer is not a list')

        def validate_bgp_peer_rib_list(value):
            if not isinstance(value, list):
                raise SchemaTypeError('bgp-rib of bgp-peer is not a list')
            bgp_peer_rib_schema = Schema(
                {
                    'accepted-prefix-count': str,
                    'active-prefix-count': str,
                    'name': str,
                    'received-prefix-count': str,
                    'suppressed-prefix-count': str
                }
            )

            for item in value:
                bgp_peer_rib_schema.validate(item)
            return value

        bgp_peer_schema = Schema(
            {
                Optional('bgp-rib'): Use(validate_bgp_peer_rib_list),
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
            }
        )
        for item in value:
            bgp_peer_schema.validate(item)
        return value

    # Main schema
    schema = {
        "bgp-information": {
            "bgp-peer": Use(validate_bgp_peer_list),
            "bgp-rib": Use(validate_bgp_rib_list),
            "bgp-thread-mode": str,
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
        p3 = re.compile(r'^(?P<name>inet(\d+)?.\d)$')

        # 1366        682          0          0          0          0
        p4 = re.compile(r'^(?P<total_prefix_count>\d+) +(?P<active_prefix_count>\d+) +'
                        r'(?P<suppressed_prefix_count>\d+) +(?P<history_prefix_count>\d+) +'
                        r'(?P<damped_prefix_count>\d+) +(?P<pending_prefix_count>\d+)$')

        # ------------------------------------------------------------
        # p5:
        # 'bgp-information': {
        #       'bgp-peer': []
        # ------------------------------------------------------------
        # 10.49.216.179           65171          0          0       0       0 29w5d 22:42:36 Connect
        # 2001:db8:eb18:ca45::11       65151          0          0       0       0 29w5d 22:42:36 Connect
        p5 = re.compile(r'^(?P<peer_address>[\d\w:.]+) +(?P<peer_as>\d+) +'
                        r'(?P<input_messages>\d+) +(?P<output_messages>\d+) +'
                        r'(?P<route_queue_count>\d+) +(?P<flap_count>\d+) +'
                        r'(?P<text>[\S\s]+) +(?P<peer_state>Active|Connect|Establ)$')

        # ------------------------------------------------------------
        # p6:
        # 'bgp-information': {
        #       'bgp-peer': [
        #           {'bgp-rib': {}}
        #       ]
        # ------------------------------------------------------------
        # inet.0: 682/684/684/0
        p6 = re.compile(r'^(?P<name>inet(\d+)?\.\d+) *: +(?P<active_prefix_count>\d+)'
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

                bgp_info_dict['bgp-information']['bgp-rib'].append(bgp_rib_dict)
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
            m = p5.match(line)
            if m:
                group = m.groupdict()
                bgp_peer_dict = {}

                for key, value in group.items():
                    if key == 'text':
                        bgp_peer_dict['elapsed-time'] = {'#text': value}
                        continue
                    key = key.replace('_', '-')
                    bgp_peer_dict[key] = value

                bgp_info_dict['bgp-information']['bgp-peer'].append(bgp_peer_dict)
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




