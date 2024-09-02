"""show_lisp_session.py

    * show lisp session
    * show lisp session redundancy

"""


# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
                                                ListOf,
                                                Optional,
                                                Or)
from genie.libs.parser.utils.common import Common

from genie.libs.parser.iosxe.show_lisp_super import *

class ShowLispSession(ShowLispSessionSuperParser):

    ''' Parser for "show lisp session"'''

    cli_command = ['show lisp session',
                   'show lisp vrf {vrf} session']

    def cli(self, output=None, vrf=None):
        if output is None:
            if vrf:
                out = self.device.execute(self.cli_command[1].format(vrf=vrf))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output
        return super().cli(output=out)


class ShowLispSessionAll(ShowLispSessionSuperParser):

    ''' Parser for "show lisp session all"'''

    cli_command = ['show lisp session all',
                   'show lisp vrf {vrf} session all']

    def cli(self, output=None, vrf=None):
        if output is None:
            if vrf:
                out = self.device.execute(self.cli_command[1].format(vrf=vrf))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output
        return super().cli(output=out)


class ShowLispSessionEstablished(ShowLispSessionSuperParser):

    ''' Parser for "show lisp session established"'''

    cli_command = ['show lisp session established',
                   'show lisp vrf {vrf} session established']

    def cli(self, output=None, vrf=None):
        if output is None:
            if vrf:
                out = self.device.execute(self.cli_command[1].format(vrf=vrf))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output
        return super().cli(output=out)

# ==========================================
# Parser for: show lisp session redundancy
# ==========================================
class ShowLispSessionRedundancySchema(MetaParser):
    schema = {
        'passive_sessions': {
            'synced': int,
            'pending_tcp_action': int,
            'pending_checkpoints': int
        },
        'listeners': {
            'synced': int,
            'pending_tcp_action': int,
            'pending_checkpoints': int
        }
    }

class ShowLispSessionRedundancy(ShowLispSessionRedundancySchema):
    cli_command = 'show lisp session redundancy'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        lisp_dict = {}

        #  Passive sessions
        p1 = re.compile(r"^Passive sessions$")

        #  Listeners
        p2 = re.compile(r"^Listeners$")

        #    Synced/pending TCP action/pending checkpoint: 7/0/3
        p3 = re.compile(r"^Synced\/pending\sTCP\saction\/pending\scheckpoint:\s(?P<synced>\d+)\/(?P<pending_tcp_action>\d+)\/(?P<pending_checkpoints>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            #  Passive sessions
            m=p1.match(line)
            if m:
                currently_parsing_passive_session = True
                passive_sessions_dict = lisp_dict.setdefault('passive_sessions', {})
                continue

            #  Listeners
            m=p2.match(line)
            if m:
                currently_parsing_passive_session = False
                listeners_dict = lisp_dict.setdefault('listeners', {})
                continue

            #  Synced/pending TCP action/pending checkpoint: 7/0/3
            m=p3.match(line)
            if m:
                group = m.groupdict()
                if currently_parsing_passive_session:
                    passive_sessions_dict['synced'] = int(group['synced'])
                    passive_sessions_dict['pending_tcp_action'] = int(group['pending_tcp_action'])
                    passive_sessions_dict['pending_checkpoints'] = int(group['pending_checkpoints'])
                else:
                    listeners_dict['synced'] = int(group['synced'])
                    listeners_dict['pending_tcp_action'] = int(group['pending_tcp_action'])
                    listeners_dict['pending_checkpoints'] = int(group['pending_checkpoints'])
                continue

        return lisp_dict

class ShowLispSessionCapabilitySchema(MetaParser):

    ''' Schema for
        * show lisp vrf default session capability
        * show lisp vrf * session capability
    '''
    schema = {
        'vrf': {
            str: {
                'peer': {
                    str:
                        ListOf({
                            'port': int,
                            'tx_flags': str,
                            'rx_flags': str,
                            'rx_count': int,
                            'err_count': int
                        })
                    }
                }
            }
        }


class ShowLispSessionCapability(ShowLispSessionCapabilitySchema):
    """Parser for show lisp vrf {vrf} session capability"""
    cli_command = ['show lisp vrf {vrf} session capability']

    def cli(self, vrf=None, output=None):
        if output is None:
            if vrf:
                output = self.device.execute(self.cli_command[0].format(vrf=vrf))
        ret_dict = {}

        #Output for router lisp vrf red
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+vrf\s+(?P<vrf>\S+)$")

        #44.44.44.44:4342               0x1FF      0x1FF      1         0
        #44:44:44:44::.4342               0x1FF      0x1FF      1         0
        p2 = re.compile(r"^(?P<peer>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))(:|\.)(?P<port>\d+)"
                        r"\s+(?P<tx_flags>\S+)\s+(?P<rx_flags>\S+)\s+(?P<rx_count>\d+)"
                        r"\s+(?P<err_count>\d+)$")

        for line in output.splitlines():
            line = line.strip()
            #Output for router lisp vrf red
            m=p1.match(line)
            if m:
                groups = m.groupdict()
                vrf = groups['vrf']
                vrf_dict = ret_dict.setdefault('vrf',{})\
                                   .setdefault(vrf,{})
                continue

            #44.44.44.44:4342               0x1FF      0x1FF      1         0
            #44:44:44:44::.4342             0x1FF      0x1FF      1         0
            m=p2.match(line)
            if m:
                if "vrf" not in ret_dict:
                    vrf_dict = ret_dict.setdefault('vrf',{})\
                                       .setdefault(vrf,{})
                groups = m.groupdict()
                peer = groups['peer']
                port = int(groups['port'])
                tx_flags = groups['tx_flags']
                rx_flags = groups['rx_flags']
                rx_count = int(groups['rx_count'])
                err_count = int(groups['err_count'])
                peer_dict = vrf_dict.setdefault('peer',{})
                peer_list = peer_dict.setdefault(peer, [])
                session_dict = {}
                session_dict.update({
                    'port': port,
                    'tx_flags': tx_flags,
                    'rx_flags': rx_flags,
                    'rx_count': rx_count,
                    'err_count': err_count})
                peer_list.append(session_dict)
        return ret_dict

class ShowLispSessionCapabilityRLOCSchema(MetaParser):

    ''' Schema for
        * show lisp vrf {vrf} session capability {rloc}
    '''
    schema = {
        'vrf': {
            str: {
                'peer_address': str,
                'peer_port': int,
                'local_address': str,
                'local_port': int,
                'capability_exchange_complete': str,
                'capability_sent_bitmap': str,
                'capability_sent': ListOf(str),
                'capability_received_bitmap': str,
                'capability_received': ListOf(str),
                'rx_count': int,
                'err_count': int
                }
            }
        }


class ShowLispSessionCapabilityRLOC(ShowLispSessionCapabilityRLOCSchema):
    """Parser for show lisp vrf {vrf} session capability {rloc}"""
    cli_command = ['show lisp vrf {vrf} session capability {rloc}']

    def cli(self, vrf=None, rloc=None, output=None):
        if output is None:
            if vrf and rloc:
                output = self.device.execute(self.cli_command[0].format(vrf=vrf,rloc=rloc))
        ret_dict = {}

        # Output for router lisp vrf red
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+vrf\s+(?P<vrf>\S+)$")

        # Peer address:                 66.66.66.66:4342
        # Peer address:                 66:66:66:66::.4342
        p2 = re.compile(r"^Peer\s+address:\s+(?P<peer_address>((\d{1,3}\.\d{1,3}"
                        r"\.\d{1,3}\.\d{1,3}:)|([a-fA-F\d\:]+\.))(?P<peer_port>\d+))$")

        # Local address:                66.66.66.66:50383
        # Local address:                66:66:66:66::.50383
        p3 = re.compile(r"^Local\s+address:\s+(?P<local_address>((\d{1,3}\.\d{1,3}"
                        r"\.\d{1,3}\.\d{1,3}:)|([a-fA-F\d\:]+\.))(?P<local_port>\d+))$")

        # Capability Exchange Complete: Yes
        p4 = re.compile(r"^Capability\s+Exchange\s+Complete:\s+"
                        r"(?P<capability_exchange_complete>\S+)$")

        # Capability Sent:              0x000001FF
        p5 = re.compile(r"^Capability\s+Sent:\s+(?P<capability_sent_bitmap>\S+)$")

        # Publish-Subscribe Instance-ID
        p6 = re.compile(r"^(?P<capability_sent>Publish-Subscribe\s+Instance-ID)$")

        # Domain-Info
        p7 = re.compile(r"^(?P<Domain>Domain-Info)$")

        # Route-Tag
        p8 = re.compile(r"^(?P<route>Route-Tag)$")

        # SGT
        p9 = re.compile(r"^(?P<sgt>SGT)$")

        # Default-originate
        p10 = re.compile(r"^(?P<default>Default-originate)$")

        # Service-registration
        p11 = re.compile(r"^(?P<service>Service-registration)$")

        # Extranet-policy-propagation
        p12 = re.compile(r"^(?P<extranet>Extranet-policy-propagation)$")

        # Default-ETR Route-metric
        p13 = re.compile(r"^(?P<default_etr>Default-ETR Route-metric)$")

        # Unknown vendor type skip
        p14 = re.compile(r"^(?P<unknown>Unknown\s+vendor\s+type\s+skip)$")

        # Capability Received:              0x000001FF
        p15 = re.compile(r"^Capability\s+Received:\s+(?P<capability_received_bitmap>\S+)$")

        # Publish-Subscribe Instance-ID
        p16 = re.compile(r"^(?P<capability_received>Publish-Subscribe\s+Instance-ID)$")

        # Domain-Info
        p17 = re.compile(r"^(?P<Domain_received>Domain-Info)$")

        # Route-Tag
        p18 = re.compile(r"^(?P<route_received>Route-Tag)$")

        # SGT
        p19 = re.compile(r"^(?P<sgt_received>SGT)$")

        # Default-originate
        p20 = re.compile(r"^(?P<default_received>Default-originate)$")

        # Service-registration
        p21 = re.compile(r"^(?P<service_received>Service-registration)$")

        # Extranet-policy-propagation
        p22 = re.compile(r"^(?P<extranet_received>Extranet-policy-propagation)$")

        # Default-ETR Route-metric
        p23 = re.compile(r"^(?P<default_etr_received>Default-ETR Route-metric)$")

        # Unknown vendor type skip
        p24 = re.compile(r"^(?P<unknown_received>Unknown\s+vendor\s+type\s+skip)$")

        # Receive count:                1
        p25 = re.compile("^Receive\s+count:\s+(?P<rx_count>\d+)$")

        # Error count:                  0
        p26 = re.compile("^Error\s+count:\s+(?P<err_count>\d+)$")

        count1 = 0
        count2 = 0
        for line in output.splitlines():
            line = line.strip()

            # Output for router lisp vrf red
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                vrf = groups['vrf']
                vrf_dict = ret_dict.setdefault('vrf',{})\
                                   .setdefault(vrf,{})
                continue

            if not m and "vrf" not in ret_dict and vrf != "*":
                vrf = vrf
                vrf_dict = ret_dict.setdefault('vrf',{})\
                                   .setdefault(vrf,{})
                continue

            # Peer address:                 66.66.66.66:4342
            # Peer address:                 66:66:66:66::.4342
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                peer_address = groups['peer_address']
                peer_port = int(groups['peer_port'])
                vrf_dict.update({'peer_address':peer_address})
                vrf_dict.update({'peer_port':peer_port})
                continue

            # Local address:                66.66.66.66:50383
            # Local address:                66:66:66:66::.50383
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                local_address = groups['local_address']
                local_port = int(groups['local_port'])
                vrf_dict.update({'local_address':local_address})
                vrf_dict.update({'local_port':local_port})
                continue

            # Capability Exchange Complete: Yes
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                capability_exchange_complete = groups['capability_exchange_complete']
                vrf_dict.update({'capability_exchange_complete':capability_exchange_complete})
                continue

            # Capability Sent:              0x000001FF
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                capability_sent_bitmap = groups['capability_sent_bitmap']
                vrf_dict.update({'capability_sent_bitmap':capability_sent_bitmap})
                continue

            # Publish-Subscribe Instance-ID
            m = p6.match(line)
            if m and count1 <= count2:
                groups = m.groupdict()
                capability_sent = groups['capability_sent']
                capability_sent_list = vrf_dict.setdefault('capability_sent', [])
                capability_sent_list.append(capability_sent)
                continue

            # Domain-Info
            m = p7.match(line)
            if m and count1 <= count2:
                groups = m.groupdict()
                Domain = groups['Domain']
                capability_sent_list.append(Domain)
                continue

            # Route-Tag
            m = p8.match(line)
            if m and count1 <= count2:
                groups = m.groupdict()
                route = groups['route']
                capability_sent_list.append(route)
                continue

            # SGT
            m = p9.match(line)
            if m and count1 <= count2:
                groups = m.groupdict()
                sgt = groups['sgt']
                capability_sent_list.append(sgt)
                continue

            # Default-originate
            m = p10.match(line)
            if m and count1 <= count2:
                groups = m.groupdict()
                default = groups['default']
                capability_sent_list.append(default)
                continue

            # Service-registration
            m = p11.match(line)
            if m and count1 <= count2:
                groups = m.groupdict()
                service = groups['service']
                capability_sent_list.append(service)
                continue

            # Extranet-policy-propagation
            m = p12.match(line)
            if m and count1 <= count2:
                groups = m.groupdict()
                extranet = groups['extranet']
                capability_sent_list.append(extranet)
                continue

            # Default-ETR Route-metric
            m = p13.match(line)
            if m and count1 <= count2:
                groups = m.groupdict()
                default_etr = groups['default_etr']
                capability_sent_list.append(default_etr)
                continue

            # Unknown vendor type skip
            m = p14.match(line)
            if m and count1 <= count2:
                groups = m.groupdict()
                unknown = groups['unknown']
                capability_sent_list.append(unknown)
                count1 += 1
                continue

            # Capability Received:              0x000001FF
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                capability_received_bitmap = groups['capability_received_bitmap']
                vrf_dict.update({'capability_received_bitmap':capability_received_bitmap})
                continue

            # Publish-Subscribe Instance-ID
            m = p16.match(line)
            if m and count1 >= count2:
                groups = m.groupdict()
                capability_received = groups['capability_received']
                capability_received_list = vrf_dict.setdefault('capability_received', [])
                capability_received_list.append(capability_received)
                continue

            # Domain-Info
            m = p17.match(line)
            if m and count1 >= count2:
                groups = m.groupdict()
                Domain_received = groups['Domain_received']
                capability_received_list.append(Domain_received)
                continue

            # Route-Tag
            m = p18.match(line)
            if m and count1 >= count2:
                groups = m.groupdict()
                route_received = groups['route_received']
                capability_received_list.append(route_received)
                continue

            # SGT
            m = p19.match(line)
            if m and count1 >= count2:
                groups = m.groupdict()
                sgt_received = groups['sgt_received']
                capability_received_list.append(sgt_received)
                continue

            # Default-originate
            m = p20.match(line)
            if m and count1 >= count2:
                groups = m.groupdict()
                default_received = groups['default_received']
                capability_received_list.append(default_received)
                continue

            # Service-registration
            m = p21.match(line)
            if m and count1 >= count2:
                groups = m.groupdict()
                service_received = groups['service_received']
                capability_received_list.append(service_received)
                continue

            # Extranet-policy-propagation
            m = p22.match(line)
            if m and count1 >= count2:
                groups = m.groupdict()
                extranet_received = groups['extranet_received']
                capability_received_list.append(extranet_received)
                continue

            # Default-ETR Route-metric
            m = p23.match(line)
            if m and count1 >= count2:
                groups = m.groupdict()
                default_etr_received = groups['default_etr_received']
                capability_received_list.append(default_etr_received)
                continue

            # Unknown vendor type skip
            m = p24.match(line)
            if m and count1 >= count2:
                groups = m.groupdict()
                unknown_received = groups['unknown_received']
                capability_received_list.append(unknown_received)
                count2 += 1
                continue

            # Receive count:                1
            m = p25.match(line)
            if m:
                groups = m.groupdict()
                rx_count = int(groups['rx_count'])
                vrf_dict.update({'rx_count':rx_count})
                continue

            # Error count:                  0
            m = p26.match(line)
            if m:
                groups = m.groupdict()
                err_count = int(groups['err_count'])
                vrf_dict.update({'err_count':err_count})
                continue
        return ret_dict

class ShowLispSessionRLOCSchema(MetaParser):

    ''' Schema for
        * show lisp session {rloc}
        * show lisp {lisp_id} session {rloc}
        * show lisp locator-table {locator_table} session {rloc}
        * show lisp vrf {vrf} session {rloc}
    '''

    schema = {
        'lisp_id': {
            int: {
                'peer_addr': str,
                'peer_port': int,
                'local_address': str,
                Optional('local_port'): int,
                Optional('session_type'): str,
                Optional('session_state'): str,
                Optional('session_state_time'): str,
                Optional('session_rtt'): int,
                Optional('session_rtt_time'): str,
                'messages_in': int,
                'messages_out': int,
                'bytes_in': int,
                'bytes_out': int,
                'fatal_errors': int,
                'rcvd_unsupported': int,
                'rcvd_invalid_vrf': int,
                'rcvd_override':int,
                'rcvd_malformed':int,
                'sent_defferred': int,
                'ssd_redundancy': str,
                'auth_type': str,
                Optional('keychain_name'): str,
                'users': {
                    'count': int,
                    'type': {
                        str: {
                            'id': {
                                str: {
                                    'in': int,
                                    'out': int,
                                    'state': str
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }


class ShowLispSessionRLOC(ShowLispSessionRLOCSchema):

    ''' Parser for
        * show lisp session {rloc}
        * show lisp {lisp_id} session {rloc}
        * show lisp locator-table {locator_table} session {rloc}
        * show lisp vrf {vrf} session {rloc}
    '''
    cli_command = ['show lisp session {rloc}',
                   'show lisp {lisp_id} session {rloc}',
                   'show lisp locator-table {locator_table} session {rloc}',
                   'show lisp vrf {vrf} session {rloc}']

    def cli(self, output=None, lisp_id=None, rloc=None, locator_table=None, vrf=None):
        if output is None:
            if lisp_id and rloc:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id,rloc=rloc))
            elif locator_table and rloc:
                output = self.device.execute(self.cli_command[2].format(locator_table=locator_table,rloc=rloc))
            elif vrf and rloc:
                output = self.device.execute(self.cli_command[3].format(vrf=vrf,rloc=rloc))
            else:
                output = self.device.execute(self.cli_command[0].format(rloc=rloc))
        ret_dict = {}

        # Output for router lisp 0
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)$")

        # Peer address:     44.44.44.44:4342
        # Peer address:     44:44:44:44::.4342
        p2 = re.compile(r"^Peer\s+address:\s+(?P<peer_addr>(\d{1,3}\.\d{1,3}\."
                        r"\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))(:|\.)(?P<peer_port>\d+)$")

        # Local address:    11.11.11.11:61669
        # Local address:    11:11:11:11::.61669
        p3 = re.compile(r"^Local\s+address:\s+(?P<local_address>(\d{1,3}\.\d{1,3}\."
                        r"\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))(:|\.)(?P<local_port>\d+)$")

        # Session Type:     Active
        p4 = re.compile(r"^Session\s+Type:\s+(?P<session_type>\S+)$")

        # Session State:    Up (4d23h)
        p5 = re.compile(r"^Session\s+State:\s+(?P<session_state>\S+)\s+"
                        r"(?P<session_state_time>\S+)$")

        # Session RTT:      0 ms  (4d23h)
        p6 = re.compile(r"^Session\s+RTT:\s+(?P<session_rtt>\S+)\s+"
                        r"ms\s+(?P<session_rtt_time>\S+)$")

        # Messages in/out:  32/15
        p7 = re.compile(r"^Messages in\/out:\s+(?P<messages_in>\d+)"
                        r"\/(?P<messages_out>\d+)$")

        # Bytes in/out:     1606/1076
        p8 = re.compile(r"^Bytes in\/out:\s+(?P<bytes_in>\d+)"
                        r"\/(?P<bytes_out>\d+)$")

        # Fatal errors:     0
        p9 = re.compile(r"^Fatal\s+errors:\s+(?P<fatal_errors>\d+)$")

        # Rcvd unsupported: 0
        p10 = re.compile(r"^Rcvd\s+unsupported:\s+(?P<rcvd_unsupported>\d+)$")

        # Rcvd invalid VRF: 0
        p11 = re.compile(r"^Rcvd\s+invalid\s+VRF:\s+(?P<rcvd_invalid_vrf>\d+)$")

        # Rcvd override:    0
        p12 = re.compile(r"^Rcvd\s+override:\s+(?P<rcvd_override>\d+)$")

        # Rcvd malformed:   0
        p13 = re.compile(r"^Rcvd\s+malformed:\s+(?P<rcvd_malformed>\d+)$")

        # Sent deferred:    1
        p14 = re.compile(r"^Sent\s+deferred:\s+(?P<sent_defferred>\d+)$")

        # SSO redundancy:   N/A
        p15 = re.compile(r"^SSO\s+redundancy:\s+(?P<ssd_redundancy>\S+)$")

        #Auth Type:        TCP-Auth-Option, keychain:  kc1
        p16 = re.compile(r"^Auth\s+Type:\s+(?P<auth_type>\S+)"
                         r"(,\s+keychain:\s+(?P<keychain_name>\S+))?$")

        # Users:            14
        p17 = re.compile(r"^Users:\s+(?P<count>\S+)$")

        # Pubsub subscriber         lisp 0 IID 101 AFI MAC                   2/0      Off
        # Capability Exchange       N/A                                      1/1      Unsubscribe IID Sent
        p18 = re.compile(r"^(?P<type>[a-zA-Z]+(?:[\s.]+[a-zA-Z]+)*)\s+"
                         r"(?P<id>[a-zA-Z\/]+(?:[\s.]+[\da-zA-Z]+)*)\s+"
                         r"(?P<in>\d+)\/(?P<out>\d+)\s+(?P<state>[\S ]+)$")

        for line in output.splitlines():
            line = line.strip()

            # Output for router lisp 0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                continue

            # Peer address:     44.44.44.44:4342
            # Peer address:     44:44:44:44::.4342
            m = p2.match(line)
            if m:
                if lisp_id != "all":
                    lisp_id = int(lisp_id) if lisp_id else 0
                    lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                groups = m.groupdict()
                peer_addr = groups['peer_addr']
                peer_port = int(groups['peer_port'])
                lisp_id_dict.update({'peer_addr':peer_addr,
                                     'peer_port':peer_port})
                continue

            # Local address:    11.11.11.11:61669
            # Local address:    11:11:11:11::.61669
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                local_address = groups['local_address']
                local_port = int(groups['local_port'])
                lisp_id_dict.update({'local_address':local_address,
                                     'local_port':local_port})
                continue

            # Session Type:     Active
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                session_type = groups['session_type']
                lisp_id_dict.update({'session_type':session_type})
                continue

            # Session State:    Up (4d23h)
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                session_state = groups['session_state']
                session_state_time = groups['session_state_time']
                lisp_id_dict.update({'session_state':session_state,
                                     'session_state_time':session_state_time})
                continue

            # Session RTT:      0 ms  (4d23h)
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                session_rtt = int(groups['session_rtt'])
                session_rtt_time = groups['session_rtt_time']
                lisp_id_dict.update({'session_rtt':session_rtt,
                                     'session_rtt_time':session_rtt_time})
                continue

            # Messages in/out:  32/15
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                messages_in = int(groups['messages_in'])
                messages_out = int(groups['messages_out'])
                lisp_id_dict.update({'messages_in':messages_in,
                                     'messages_out':messages_out})
                continue

            # Bytes in/out:     1606/1076
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                bytes_in = int(groups['bytes_in'])
                bytes_out = int(groups['bytes_out'])
                lisp_id_dict.update({'bytes_in':bytes_in,
                                     'bytes_out':bytes_out})
                continue

            # Fatal errors:     0
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                fatal_errors = int(groups['fatal_errors'])
                lisp_id_dict.update({'fatal_errors':fatal_errors})
                continue

            # Rcvd unsupported: 0
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                rcvd_unsupported = int(groups['rcvd_unsupported'])
                lisp_id_dict.update({'rcvd_unsupported':rcvd_unsupported})
                continue

            # Rcvd invalid VRF: 0
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                rcvd_invalid_vrf = int(groups['rcvd_invalid_vrf'])
                lisp_id_dict.update({'rcvd_invalid_vrf':rcvd_invalid_vrf})
                continue

            # Rcvd override:    0
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                rcvd_override = int(groups['rcvd_override'])
                lisp_id_dict.update({'rcvd_override':rcvd_override})
                continue

            # Rcvd malformed:   0
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                rcvd_malformed = int(groups['rcvd_malformed'])
                lisp_id_dict.update({'rcvd_malformed':rcvd_malformed})
                continue

            # Sent deferred:    1
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                sent_defferred = int(groups['sent_defferred'])
                lisp_id_dict.update({'sent_defferred':sent_defferred})
                continue

            # SSO redundancy:   N/A
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                ssd_redundancy = groups['ssd_redundancy']
                lisp_id_dict.update({'ssd_redundancy':ssd_redundancy})
                continue

            #Auth Type:        TCP-Auth-Option, keychain:  kc1
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                auth_type = groups['auth_type']
                keychain_name = groups['keychain_name']
                if keychain_name:
                    lisp_id_dict.update({'auth_type':auth_type,
                                     'keychain_name':keychain_name})
                else:
                    lisp_id_dict.update({'auth_type':auth_type})
                continue

            # Users:            14
            m = p17.match(line)
            if m:
                groups = m.groupdict()
                count = int(groups['count'])
                count_dict = lisp_id_dict.setdefault('users',{})
                count_dict.update({'count':count})
                continue

            # Pubsub subscriber         lisp 0 IID 101 AFI MAC                   2/0      Off
            m = p18.match(line)
            if m:
                groups = m.groupdict()
                type = groups['type']
                id = groups['id']
                user_in = int(groups['in'])
                out = int(groups['out'])
                state = groups['state']
                type_dict = count_dict.setdefault('type',{}).setdefault(type,{})
                id_dict = type_dict.setdefault('id',{}).setdefault(id,{})
                id_dict.update({'in':user_in,
                                'out':out,
                                'state':state})
                continue
        return ret_dict

