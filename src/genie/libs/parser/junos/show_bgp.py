""" show_bgp.py

JunOs parsers for the following show commands:
    * show bgp group brief | no-more
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
from genie.metaparser.util.schemaengine import (Any, 
        Optional, Use, SchemaTypeError, Schema)
        
class ShowBgpGroupBriefSchema(MetaParser):
    """ Schema for:
            * show bgp group brief | no-more
    """

    schema = {'bgp-group-information': {'bgp-group': [{'bgp-option-information': {'bgp-options': str,
                                                                     'bgp-options-extended': str,
                                                                     'export-policy': str,
                                                                     'gshut-recv-local-preference': str,
                                                                     'holdtime': str},
                                          'bgp-rib': {'accepted-prefix-count': str,
                                                      'active-prefix-count': str,
                                                      'advertised-prefix-count': str,
                                                      'name': str,
                                                      'received-prefix-count': str,
                                                      'suppressed-prefix-count': str},
                                          'established-count': str,
                                          'flap-count': str,
                                          'group-flags': str,
                                          'group-index': str,
                                          'local-as': str,
                                          'peer-address': str,
                                          'peer-as': str,
                                          'peer-count': str,
                                          'type': str}],
                           'bgp-information': {'bgp-rib': [{'accepted-external-prefix-count': str,
                                                            'accepted-internal-prefix-count': str,
                                                            'active-external-prefix-count': str,
                                                            'active-internal-prefix-count': str,
                                                            'bgp-rib-state': str,
                                                            'damped-prefix-count': str,
                                                            'history-prefix-count': str,
                                                            'pending-prefix-count': str,
                                                            'suppressed-external-prefix-count': str,
                                                            'suppressed-internal-prefix-count': str,
                                                            'total-external-prefix-count': str,
                                                            'total-internal-prefix-count': str,
                                                            'total-prefix-count': str}],
                                               'down-peer-count': str,
                                               'external-peer-count': str,
                                               'group-count': str,
                                               'internal-peer-count': str}}}

class ShowBgpGroupBrief(ShowBgpGroupBriefSchema):

    cli_command = ['show bgp group brief',
        'show bgp group brief | no-more']
    
    def cli(self, no_more=False, output=None):

        if not output:
            cmd = self.cli_command[1] if no_more else self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

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

        # 111.87.5.253+179
        p9 = re.compile(r'^(?P<peer_address>\S+)$')

        # inet6.0: 0/0/0/0
        p10 = re.compile(r'^(?P<name>inet(\d+)?\.\d+): +(?P<active_prefix_count>\d+)'
                r'\/(?P<received_prefix_count>\d+)\/(?P<accepted_prefix_count>\d+)'
                r'\/(?P<advertised_prefix_count>\d+)$')

        for line in out.splitlines():
            line = line.strip()
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

            # 111.87.5.253+179
            m = p9.match(line)
            if m:
                group = m.groupdict()
                bgp_group_dict.update({'peer-address': group['peer_address']})
                continue

            # inet6.0: 0/0/0/0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                bgp_rib_dict = bgp_group_dict.setdefault('bgp-rib', {})
                bgp_rib_dict.update({'name': group['name']})
                bgp_rib_dict.update({'active-prefix-count': group['active_prefix_count']})
                bgp_rib_dict.update({'received-prefix-count': group['received_prefix_count']})
                bgp_rib_dict.update({'accepted-prefix-count': group['accepted_prefix_count']})
                bgp_rib_dict.update({'advertised-prefix-count': group['advertised_prefix_count']})
                continue
        return ret_dict