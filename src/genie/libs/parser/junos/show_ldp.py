"""show_ldp.py

JUNOS parsers for the following commands:
    * show ldp session
    * show ldp neighbor
    * show ldp database session {ipaddress}
    * show ldp overview
    * show ldp interface {interface}
    * show ldp interface {interface} detail
"""

import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import Any, Optional, Use, Schema, ListOf


class ShowLDPSessionSchema(MetaParser):
    """ Schema for
        * show ldp session
    """

    schema = {
        "ldp-session-information": {
            "ldp-session": ListOf({
                "ldp-neighbor-address": str,
                "ldp-session-state": str,
                "ldp-connection-state": str,
                "ldp-remaining-time": str,
                Optional("ldp-session-adv-mode"): str,
            })
        }
    }


class ShowLDPSession(ShowLDPSessionSchema):
    """ Parser for:
        * show ldp session
    """

    cli_command = 'show ldp session'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # 10.34.2.250                        Operational Open          26         DU
        p1 = re.compile(r'^(?P<ldp_neighbor_address>\S+) +'
                        r'(?P<ldp_session_state>\S+) +'
                        r'(?P<ldp_connection_state>\S+) +'
                        r'(?P<ldp_remaining_time>\d+)( +)?'
                        r'(?P<ldp_session_adv_mode>\S+)?$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                session_list = ret_dict.setdefault("ldp-session-information",
                                                   {}).setdefault(
                                                       "ldp-session", [])
                session_list.append({
                    k.replace('_', '-'): v
                    for k, v in group.items() if v is not None
                })

        return ret_dict


class ShowLdpNeighborSchema(MetaParser):
    """ Schema for:
            * show ldp neighbor
    """

    '''schema = {
    Optional("@xmlns:junos"): str,
    "ldp-neighbor-information": {
        Optional("@xmlns"): str,
        "ldp-neighbor": [
                {
            "interface-name": str,
            "ldp-label-space-id": str,
            "ldp-neighbor-address": str,
            "ldp-remaining-time": str
                }
            ]
        }
    }'''

    schema = {
        Optional("@xmlns:junos"): str,
        "ldp-neighbor-information": {
            Optional("@xmlns"): str,
            "ldp-neighbor": ListOf({
                "interface-name": str,
                "ldp-label-space-id": str,
                "ldp-neighbor-address": str,
                "ldp-remaining-time": str
            })
        }
    }


class ShowLdpNeighbor(ShowLdpNeighborSchema):
    """ Parser for:
            * show ldp neighbor
    """

    cli_command = 'show ldp neighbor'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # 10.169.14.158                      ge-0/0/0.0      10.34.2.250:0       14
        p1 = re.compile(
            r'^(?P<ldp_neighbor_address>\S+) '
            r'+(?P<interface_name>\S+) +(?P<ldp_label_space_id>\S+) '
            r'+(?P<ldp_remaining_time>\S+)$'
        )

        for line in out.splitlines():
            line = line.strip()

            # 10.169.14.158                      ge-0/0/0.0      10.34.2.250:0       14
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ldp_neighbor_list = ret_dict.setdefault('ldp-neighbor-information', {}).\
                    setdefault('ldp-neighbor', [])
                ldp_dict = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    ldp_dict[entry_key] = group_value

                ldp_neighbor_list.append(ldp_dict)
                continue

        return ret_dict


class ShowLdpDatabaseSessionIpaddressSchema(MetaParser):
    """ Schema for:
            * show ldp database session ipaddress
    """

    '''schema = {
    "ldp-database-information": {
        "ldp-database": [
            {
                "ldp-binding": [
                    {
                        "ldp-label": str,
                        "ldp-prefix": str
                    }
                ],
                "ldp-database-type": str,
                "ldp-label-received": str,
                "ldp-label-advertised": str,
                "ldp-session-id": str
            }
        ]
    }
}'''

    schema = {
        "ldp-database-information": {
            "ldp-database": ListOf({
                "ldp-binding": ListOf({
                    "ldp-label": str,
                    "ldp-prefix": str
                }),
                "ldp-database-type": str,
                Optional("ldp-label-received"): str,
                Optional("ldp-label-advertised"): str,
                "ldp-session-id": str
            })
        }
    }


class ShowLdpDatabaseSessionIpaddress(ShowLdpDatabaseSessionIpaddressSchema):
    """ Parser for:
            * show ldp database session ipaddress
    """

    cli_command = 'show ldp database session {ipaddress}'

    def cli(self, ipaddress=None, output=None):
        if not output:
            cmd = self.cli_command.format(ipaddress=ipaddress)
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        # Input label database, 10.169.14.240:0--10.34.2.250:0
        p1 = re.compile(
            r'^(?P<ldp_database_type>[\S\s]+), '
            r'+(?P<ldp_session_id>[\d\.\:\-]+)$'
        )

        # Labels received: 2
        p2 = re.compile(
            r'^Labels +(?P<label_type>\S+): +(?P<ldp_label_received>\d+)$'
        )

        # 3      10.34.2.250/32
        p3 = re.compile(
            r'^(?P<ldp_label>\d+) +(?P<ldp_prefix>[\d\.\/]+)$'
        )

        for line in out.splitlines():
            line = line.strip()

            # 10.169.14.158                      ge-0/0/0.0      10.34.2.250:0       14
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ldp_neighbor_list = ret_dict.setdefault('ldp-database-information', {}).\
                    setdefault('ldp-database', [])
                ldp_entry_dict = {}
                for group_key, group_value in group.items():
                    if(group_key != 'label_type'):
                        entry_key = group_key.replace('_', '-')
                        ldp_entry_dict[entry_key] = group_value

                ldp_binding_list = []
                ldp_entry_dict['ldp-binding'] = ldp_binding_list
                ldp_neighbor_list.append(ldp_entry_dict)
                continue

            # Labels received: 2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if group['label_type'] == 'advertised':
                    ldp_entry_dict['ldp-label-advertised'] = group['ldp_label_received']
                else:
                    ldp_entry_dict['ldp-label-received'] = group['ldp_label_received']
                continue

            # 3      10.34.2.250/32
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ldp_binding_dict = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    ldp_binding_dict[entry_key] = group_value

                ldp_binding_list.append(ldp_binding_dict)
                continue

        return ret_dict


class ShowLDPOverviewSchema(MetaParser):
    """ Schema for
        * show ldp overview
    """
    schema = {
        "ldp-overview-information": {
            "ldp-overview": {
                "ldp-instance-name": str,
                Optional("ldp-reference-count"): int,
                "ldp-router-id": str,
                Optional("ldp-inet"): str,
                Optional("ldp-transport-preference"): str,
                "ldp-message-id": int,
                "ldp-configuration-sequence": int,
                Optional("ldp-control-mode"): str,
                Optional("ldp-closing-mode"): str,
                "ldp-deaggregate": str,
                "ldp-explicit-null": str,
                "ldp-ipv6-tunneling": str,
                "ldp-strict-targeted-hellos": str,
                "ldp-loopback-if-added": str,
                "ldp-route-preference": int,
                "ldp-unicast-transit-lsp-chaining": str,
                "ldp-p2mp-transit-lsp-chaining": str,
                "ldp-transit-lsp-route-stats": str,
                Optional("ldp-retention-mode"): str,
                Optional("ldp-route-acknowledgement"): str,
                Optional("ldp-bgp-export"): str,
                Optional("ldp-mtu-discovery"): str,
                Optional("ldp-sr-mapping-client"): str,
                Optional("ldp-instance-capability"): {
                    "ldp-capability": str
                },
                Optional("ldp-instance-egress-fec-capability"): {
                    "ldp-egress-fec-capability": str
                },
                Optional("ldp-session-count"): {
                    Optional("ldp-session-operational"): int,
                    Optional("ldp-session-nonexistent"): int,
                    Optional("ldp-retention-mode"): str,
                    Optional("ldp-control-mode"): str,
                    Optional("ldp-session-connecting"): int
                },
                Optional("ldp-session-operational"): int,
                Optional("ldp-dod-session-count"): str,
                Optional("ldp-auto-targeted-session"): {
                    "ldp-auto-targeted-session-enabled": str,
                    "ldp-auto-targeted-dyn-tun-ses-count": int
                },
                Optional("ldp-p2mp"): {
                    "ldp-p2mp-recursive-route-enabled": str,
                    "ldp-p2mp-no-rsvp-tunneling-enabled": str
                },
                "ldp-timer-overview": {
                    "ldp-instance-keepalive-interval": int,
                    "ldp-instance-keepalive-timeout": int,
                    "ldp-instance-link-hello-interval": int,
                    "ldp-instance-link-hello-hold-time": int,
                    "ldp-instance-targeted-hello-interval": int,
                    "ldp-instance-targeted-hello-hold-time": int,
                    "ldp-instance-label-withdraw-delay": int,
                    Optional("ldp-instance-make-before-break-timeout"): int,
                    Optional("ldp-instance-make-before-break-switchover-delay"): int,
                    Optional("ldp-instance-link-protection-timeout"): int
                },
                "ldp-gr-overview": {
                    "ldp-gr-restart": str,
                    "ldp-gr-helper": str,
                    "ldp-gr-restarting": str,
                    "ldp-gr-reconnect-time": int,
                    "ldp-gr-max-neighbor-reconnect-time": int,
                    "ldp-gr-recovery-time": int,
                    "ldp-gr-max-neighbor-recovery-time": int
                },
                "ldp-te-overview": {
                    "ldp-te-bgp-igp": str,
                    "ldp-te-both-ribs": str,
                    "ldp-te-mpls-forwarding": str,
                    Optional("ldp-rib-group-change-pending"): str
                },
                "ldp-igp-overview": {
                    "ldp-tracking-igp-metric": str,
                    "ldp-igp-sync-session-up-delay": int
                },
                "ldp-session-protect-overview": {
                    "ldp-session-protect": str,
                    "ldp-session-protect-timeout": int
                },
                "ldp-interface-address": {
                    "interface-address": list
                },
                Optional("ldp-job-overview"): {
                    "ldp-read-job-time-quantum": int,
                    "ldp-write-job-time-quantum": int,
                    "ldp-read-job-loop-quantum": int,
                    "ldp-write-job-loop-quantum": int,
                    "ldp-inbound-read-job-time-quantum": int,
                    "ldp-outbound-read-job-time-quantum": int,
                    "ldp-inbound-read-job-loop-quantum": int,
                    "ldp-outbound-read-job-loop-quantum": int
                },
                Optional("ldp-label-allocation"): {
                    "ldp-label-current-allocs": int,
                    "ldp-label-total-allocs": int,
                    "ldp-label-total-frees": int,
                    "ldp-label-alloc-failure": int,
                    "ldp-global-label-current-allocs": int
                },
                Optional("ldp-protocol-modes"): {
                    Optional("ldp-distribution-mode"): str,
                    Optional("ldp-retention-mode"): str,
                    Optional("ldp-control-mode"): str,
                },
            }
        }
    }


class ShowLDPOverview(ShowLDPOverviewSchema):
    """ Parser for:
        * show ldp overview
    """

    cli_command = 'show ldp overview'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # variables initialize
        session_flag = False
        auto_targeted_flag = False
        p2mp_flag = False
        timers_flag = False
        grace_restart_flag = False
        traffic_engineering_flag = False
        igp_flag = False
        session_protection_flag = False
        ldp_job_flag = False
        label_alloc_flag = False
        protocol_mode_flag = False

        ret_dict = {}
        overview_dict = {}
        var_dict = {
            'Instance': ['ldp-instance-name', 'str'],
            'Protocol modes': ['ldp-protocol-modes', 'str'],
            'Distribution': ['ldp-distribution-mode', 'str'],
            'Reference count': ['ldp-reference-count', 'int'],
            'Connecting': ['ldp-session-connecting', 'int'],
            'Router ID': ['ldp-router-id', 'str'],
            'LDP inet': ['ldp-inet', 'str'],
            'Transport preference': ['ldp-transport-preference', 'str'],
            'Message id': ['ldp-message-id', 'int'],
            'Configuration sequence': ['ldp-configuration-sequence', 'int'],
            'Deaggregate': ['ldp-deaggregate', 'str'],
            'Explicit null': ['ldp-explicit-null', 'str'],
            'IPv6 tunneling': ['ldp-ipv6-tunneling', 'str'],
            'Strict targeted hellos': ['ldp-strict-targeted-hellos', 'str'],
            'Loopback if added': ['ldp-loopback-if-added', 'str'],
            'Route preference': ['ldp-route-preference', 'int'],
            'Unicast transit LSP chaining': ['ldp-unicast-transit-lsp-chaining', 'str'],
            'P2MP transit LSP chaining': ['ldp-p2mp-transit-lsp-chaining', 'str'],
            'Transit LSP statistics based on route statistics': ['ldp-transit-lsp-route-stats', 'str'],
            'LDP route acknowledgement': ['ldp-route-acknowledgement', 'str'],
            'BGP export': ['ldp-bgp-export', 'str'],
            'LDP mtu discovery': ['ldp-mtu-discovery', 'str'],
            'LDP SR Mapping Client': ['ldp-sr-mapping-client', 'str'],
            'Capabilities enabled': ['ldp-capability', 'str'],
            'Egress FEC capabilities enabled': ['ldp-egress-fec-capability', 'str'],
            # Downstream unsolicited sessions
            'Nonexistent': ['ldp-session-nonexistent', 'int'],
            'Operational': ['ldp-session-operational', 'int'],
            'Retention': ['ldp-retention-mode', 'str'],
            'Control': ['ldp-control-mode', 'str'],
            'Closing': ['ldp-closing-mode', 'str'],
            # Auto targeted sessions
            'Auto targeted': ['ldp-auto-targeted-session-enabled', 'str'],
            'Dynamic tunnel session count': ['ldp-auto-targeted-dyn-tun-ses-count', 'int'],
            # P2MP
            'Recursive route': ['ldp-p2mp-recursive-route-enabled', 'str'],
            'No rsvp tunneling': ['ldp-p2mp-no-rsvp-tunneling-enabled', 'str'],
            # Timers
            'Keepalive interval': ['ldp-instance-keepalive-interval', 'int'],
            'Keepalive timeout': ['ldp-instance-keepalive-timeout', 'int'],
            'Link hello interval': ['ldp-instance-link-hello-interval', 'int'],
            'Link hello hold time': ['ldp-instance-link-hello-hold-time', 'int'],
            'Targeted hello interval': ['ldp-instance-targeted-hello-interval', 'int'],
            'Targeted hello hold time': ['ldp-instance-targeted-hello-hold-time', 'int'],
            'Label withdraw delay': ['ldp-instance-label-withdraw-delay', 'int'],
            'Make before break timeout': ['ldp-instance-make-before-break-timeout', 'int'],
            'Make before break switchover delay': ['ldp-instance-make-before-break-switchover-delay', 'int'],
            'Link protection timeout': ['ldp-instance-link-protection-timeout', 'int'],
            # Graceful restart
            'Restart': ['ldp-gr-restart', 'str'],
            'Helper': ['ldp-gr-helper', 'str'],
            'Restart in process': ['ldp-gr-restarting', 'str'],
            'Reconnect time': ['ldp-gr-reconnect-time', 'int'],
            'Max neighbor reconnect time': ['ldp-gr-max-neighbor-reconnect-time', 'int'],
            'Recovery time': ['ldp-gr-recovery-time', 'int'],
            'Max neighbor recovery time': ['ldp-gr-max-neighbor-recovery-time', 'int'],
            # Traffic Engineering
            'Bgp igp': ['ldp-te-bgp-igp', 'str'],
            'Both ribs': ['ldp-te-both-ribs', 'str'],
            'Mpls forwarding': ['ldp-te-mpls-forwarding', 'str'],
            # IGP
            'Tracking igp metric': ['ldp-tracking-igp-metric', 'str'],
            'Sync session up delay': ['ldp-igp-sync-session-up-delay', 'int'],
            # Session protection
            'Session protection': ['ldp-session-protect', 'str'],
            'Session protection timeout': ['ldp-session-protect-timeout', 'int'],
            # LDP Job
            'Read job time quantum': ['ldp-read-job-time-quantum', 'int'],
            'Write job time quantum': ['ldp-write-job-time-quantum', 'int'],
            'Read job loop quantum': ['ldp-read-job-loop-quantum', 'int'],
            'Write job loop quantum': ['ldp-write-job-loop-quantum', 'int'],
            'Backup inbound read job time quantum': ['ldp-inbound-read-job-time-quantum', 'int'],
            'Backup outbound read job time quantum': ['ldp-outbound-read-job-time-quantum', 'int'],
            'Backup inbound read job loop quantum': ['ldp-inbound-read-job-loop-quantum', 'int'],
            'Backup outbound read job loop quantum': [
                'ldp-outbound-read-job-loop-quantum', 'int'],
            # Label allocation
            'Current number of LDP labels allocated': ['ldp-label-current-allocs', 'int'],
            'Total number of LDP labels allocated': ['ldp-label-total-allocs', 'int'],
            'Total number of LDP labels freed': ['ldp-label-total-frees', 'int'],
            'Total number of LDP label allocation failure': ['ldp-label-alloc-failure', 'int'],
            'Current number of labels allocated by all protocols': ['ldp-global-label-current-allocs', 'int'],
        }

        # Instance: master
        # Reconnect time: 60000, Max neighbor reconnect time: 120000
        # Restart: disabled, Helper: enabled, Restart in process: false
        p1 = re.compile(
            r'^(?P<var>[\w\s]+)\: +(?P<value>\S+)'
            r'(, +(?P<var2>[\w\s]+)\: +(?P<value2>\S+))?'
            r'(, +(?P<var3>[\w\s]+)\: +(?P<value3>\S+))?$')

        # Downstream unsolicited Sessions:
        p2 = re.compile(r'^Downstream +unsolicited +Sessions\:$')

        # Auto targeted sessions:
        p3 = re.compile(r'^Auto +targeted +sessions\:$')

        # P2MP:
        p4 = re.compile(r'^P2MP\:$')

        # Timers:
        p5 = re.compile(r'^Timers\:$')

        # Graceful restart:
        p6 = re.compile(r'^Graceful +restart\:$')

        # IGP:
        p7 = re.compile(r'^IGP\:$')

        # Session protection:
        p8 = re.compile(r'^Session +protection\:$')

        # Traffic Engineering:
        p9 = re.compile(r'^Traffic +Engineering\:$')

        # LDP Job:
        p10 = re.compile(r'^LDP +Job\:$')

        # Label allocation:
        p11 = re.compile(r'^Label +allocation\:$')

        # 10.1.2.2
        p12 = re.compile(r'^(?P<ip>[\d\.]+)$')

        # Protocol modes:
        p13 = re.compile(r'^Protocol +modes\:$')

        # Sessions:
        p14 = re.compile(r'Sessions\:$')

        for line in out.splitlines():
            line = line.strip()

            # Downstream unsolicited Sessions:
            m2 = p2.match(line)
            m13 = p13.match(line)
            m14 = p14.match(line)
            if m2 or m13 or m14:
                # Initialize sub dict
                if m2 or m14:
                    session_dict = overview_dict.setdefault(
                        "ldp-session-count", {})
                if m13:
                    session_dict = overview_dict.setdefault(
                        "ldp-protocol-modes", {})
                    protocol_mode_flag = True

                session_flag = True

            # Auto targeted sessions:
            m3 = p3.match(line)
            if m3:
                # if 'Auto targeted sessions' in line:
                # Initialize sub dict
                targeted_dict = overview_dict.setdefault(
                    'ldp-auto-targeted-session', {})
                auto_targeted_flag = True
                continue

            # P2MP:
            m4 = p4.match(line)
            if m4:
                # Initialize sub dict
                p2mp_dict = overview_dict.setdefault('ldp-p2mp', {})
                p2mp_flag = True
                continue

            # Timers:
            m5 = p5.match(line)
            if m5:
                # Initialize sub dict
                timers_dict = overview_dict.setdefault(
                    'ldp-timer-overview', {})
                timers_flag = True
                continue

            # Graceful restart:
            m6 = p6.match(line)
            if m6:
                # Initialize sub dict
                gr_dict = overview_dict.setdefault('ldp-gr-overview', {})
                grace_restart_flag = True
                continue

            # IGP:
            m7 = p7.match(line)
            if m7:
                # Initialize sub dict
                igp_dict = overview_dict.setdefault('ldp-igp-overview', {})
                igp_flag = True
                continue

            # Session protection:
            m8 = p8.match(line)
            if m8:
                # Initialize sub dict
                session_pr_dict = overview_dict.setdefault(
                    'ldp-session-protect-overview', {})
                session_protection_flag = True
                continue

            # Traffic Engineering:
            m9 = p9.match(line)
            if m9:
                # Initialize sub dict
                te_dict = overview_dict.setdefault('ldp-te-overview', {})
                traffic_engineering_flag = True
                continue

            # LDP Job:
            m10 = p10.match(line)
            if m10:
                # Initialize sub dict
                job_dict = overview_dict.setdefault('ldp-job-overview', {})
                ldp_job_flag = True
                continue

            # Label allocation:
            m11 = p11.match(line)
            if m11:
                # Initialize sub dict
                label_alloc_dict = overview_dict.setdefault(
                    'ldp-label-allocation', {})
                label_alloc_flag = True
                continue

            # Instance: master
            # Reconnect time: 60000, Max neighbor reconnect time: 120000
            # Restart: disabled, Helper: enabled, Restart in process: false
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                # Initialize dict structure
                overview_dict = ret_dict.setdefault(
                    "ldp-overview-information", {}).setdefault("ldp-overview", {})

                # Retrieve a list from predefined dict
                # handle misspell from the device
                # Session protecton timeout vs Session protection timeout
                if 'Session protecton timeout' in group['var']:
                    group['var'] = 'Session protection timeout'

                hold_list = var_dict.get(group['var'])

                # Get defined type for the data
                # convert to type if data is integer
                # else leave as string
                if 'int' in hold_list[1]:
                    defined_value = int(group['value'])
                else:
                    defined_value = group['value']

                if group['var2']:
                    hold_list_var2 = var_dict.get(group['var2'])

                    if 'int' in hold_list_var2[1]:
                        defined_value2 = int(group['value2'])
                    else:
                        defined_value2 = group['value2']

                if group['var3']:
                    hold_list_var3 = var_dict.get(group['var3'])

                    if 'int' in hold_list_var3[1]:
                        defined_value3 = int(group['value3'])
                    else:
                        defined_value3 = group['value3']

                if session_flag:
                    session_dict.update({hold_list[0]: defined_value})

                    if 'Control' in group['var']:
                        session_flag = False

                    if 'Operational' in group['var'] and protocol_mode_flag:
                        session_flag = False

                    if 'Connecting' in group['var'] and protocol_mode_flag:
                        session_flag = False

                elif 'Egress FEC capabilities enabled' in group['var']:
                    overview_dict.setdefault(
                        'ldp-instance-egress-fec-capability', {'ldp-egress-fec-capability': group['value']})

                elif 'Capabilities enabled' in group['var']:
                    overview_dict.setdefault(
                        'ldp-instance-capability', {'ldp-capability': group['value']})

                elif auto_targeted_flag:
                    targeted_dict.update({hold_list[0]: defined_value})

                    if 'Dynamic tunnel session count' in group['var']:
                        auto_targeted_flag = False
                elif p2mp_flag:
                    p2mp_dict.update({hold_list[0]: defined_value})

                    if 'No rsvp tunneling' in group['var']:
                        p2mp_flag = False
                elif timers_flag:
                    timers_dict.update({hold_list[0]: defined_value})
                    timers_dict.update({hold_list_var2[0]: defined_value2})

                    if 'Link protection timeout' in group['var']:
                        timers_flag = False

                    if 'Label withdraw delay' in group['var'] and not group['var2']:
                        timers_flag = False

                elif grace_restart_flag:
                    gr_dict.update({hold_list[0]: defined_value})
                    gr_dict.update({hold_list_var2[0]: defined_value2})

                    if group['var3']:
                        gr_dict.update({hold_list_var3[0]: defined_value3})

                    if 'Max neighbor recovery time' in group['var2']:
                        grace_restart_flag = False

                elif traffic_engineering_flag:
                    te_dict.update({hold_list[0]: defined_value})

                    if 'Mpls forwarding' in group['var']:
                        traffic_engineering_flag = False

                elif igp_flag:
                    igp_dict.update({hold_list[0]: defined_value})

                    if 'Sync session up delay' in group['var']:
                        igp_flag = False

                elif session_protection_flag:
                    session_pr_dict.update({hold_list[0]: defined_value})

                    if 'Session protection timeout' in group['var']:
                        session_protection_flag = False

                elif ldp_job_flag:
                    job_dict.update({hold_list[0]: defined_value})
                    job_dict.update({hold_list_var2[0]: defined_value2})

                    if 'Backup outbound read job loop quantum' in group['var2']:
                        ldp_job_flag = False

                elif label_alloc_flag:
                    label_alloc_dict.update({hold_list[0]: defined_value})

                    if 'Current number of labels allocated by all protocols' in group['var']:
                        label_alloc_flag = False

                else:
                    overview_dict.update({hold_list[0]: defined_value})

            m12 = p12.match(line)
            if m12:
                group = m12.groupdict()
                interface_dict = overview_dict.setdefault(
                    'ldp-interface-address', {}).setdefault('interface-address',[])
                interface_dict.append(group['ip'])
                
        return ret_dict


class ShowLDPInterfaceSchema(MetaParser):
    """ Schema for:
            * show ldp interface {interface}
    """
    schema = {
        Optional("@xmlns:junos"): str,
        "ldp-interface-information": {
            Optional("@xmlns"): str,
            "ldp-interface": {
                "interface-name": str,
                Optional("ldp-interface-local-address"): str,
                "ldp-label-space-id": str,
                "ldp-neighbor-count": str,
                "ldp-next-hello": str,
                Optional("ldp-holdtime"): str,
                Optional("ldp-hello-interval"): str,
                Optional("ldp-transport-address"): str,
            }
        }
    }


class ShowLDPInterface(ShowLDPInterfaceSchema):
    """ Parser for:
            * show ldp interface {interface}
    """
    cli_command = 'show ldp interface {interface}'

    def cli(self, interface, output=None):
        if not output:
            out = self.device.execute(self.cli_command.format(
                interface=interface
            ))
        else:
            out = output

        # ge-0/0/0.0         10.1.2.2                   10.204.14.100:0  1      3
        # et-0/0/0.0           10.4.14.240:0         1           3
        p1 = re.compile(r'^(?P<interface_name>\S+)( +(?P<local_address>\S+))? +'
                        r'(?P<space_id>\S+) +(?P<neighbor_count>\d+) +(?P<next_hello>\d+)$')

        # Hello interval: 5, Hold time: 15, Transport address: 10.204.14.100
        p2 = re.compile(r'^Hello +interval: +(?P<ldp_hello_interval>\d+), +'
                        r'Hold +time: +(?P<ldp_holdtime>\d+), +'
                        r'Transport +address: +(?P<ldp_transport_address>\S+)')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # ge-0/0/0.0         10.1.2.2                   10.204.14.100:0  1      3
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ldp_interface_info_dict = ret_dict.setdefault('ldp-interface-information', {}). \
                    setdefault('ldp-interface', {})
                ldp_interface_info_dict.update(
                    {'interface-name': group['interface_name']})

                if group['local_address']:
                    ldp_interface_info_dict.update(
                        {'ldp-interface-local-address': group['local_address']})
                        
                ldp_interface_info_dict.update(
                    {'ldp-label-space-id': group['space_id']})
                ldp_interface_info_dict.update(
                    {'ldp-neighbor-count': group['neighbor_count']})
                ldp_interface_info_dict.update(
                    {'ldp-next-hello': group['next_hello']})
                continue

            # Hello interval: 5, Hold time: 15, Transport address: 10.204.14.100
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ldp_interface_info_dict.update({k.replace('_', '-'): v for k, v in group.items()
                                                if v is not None})
                continue

        return ret_dict

class ShowLDPInterfaceDetail(ShowLDPInterface):
    cli_command = 'show ldp interface {interface} detail'
    def cli(self, interface, output=None):

        if not output:
            out = self.device.execute(self.cli_command.format(
                interface=interface
            ))
        else:
            out = output

        return super().cli(interface=interface, output=' ' if not out else out)


class ShowLdpSessionIpaddressDetailSchema(MetaParser):
    """ Schema for:
            * show ldp session ipaddress detail
    """

    schema = {
    "ldp-session-information": {
        "ldp-session": {
            "ldp-connection-state": str,
            "ldp-graceful-restart-local": str,
            Optional("ldp-graceful-restart-remote"): str,
            "ldp-holdtime": str,
            "ldp-keepalive-interval": str,
            Optional("ldp-keepalive-time"): str,
            Optional("ldp-local-address"): str,
            "ldp-local-helper-mode": str,
            "ldp-local-label-adv-mode": str,
            "ldp-local-maximum-reconnect": str,
            "ldp-local-maximum-recovery": str,
            "ldp-mtu-discovery": str,
            "ldp-neg-label-adv-mode": str,
            "ldp-neighbor-address": str,
            "ldp-neighbor-count": str,
            "ldp-neighbor-types": {
                "ldp-neighbor-type": str
            },
            "ldp-remaining-time": str,
            Optional("ldp-remote-address"): str,
            Optional("ldp-remote-helper-mode"): str,
            Optional("ldp-remote-label-adv-mode"): str,
            Optional("ldp-remote-reconnect-time"): str,
            "ldp-retry-interval": str,
            Optional("ldp-session-address"): {
                "interface-address": list
            },
            Optional("ldp-session-adv-mode"): str,
            "ldp-session-capabilities-advertised": {
                "ldp-capability": str
            },
            "ldp-session-capabilities-received": {
                "ldp-capability": str
            },
            "ldp-session-flags": {
                "ldp-session-flag": str
            },
            "ldp-session-id": str,
            "ldp-session-max-pdu": str,
            "ldp-session-nsr-state": str,
            "ldp-session-protection": {
                "ldp-session-protection-state": str
            },
            "ldp-session-role": str,
            "ldp-session-state": str,
            Optional("ldp-up-time"): str
        }
    }
}


class ShowLdpSessionIpaddressDetail(ShowLdpSessionIpaddressDetailSchema):
    """ Parser for:
            * show ldp session {ipaddress} detail
    """

    cli_command = 'show ldp session {ipaddress} detail'

    def cli(self, ipaddress, output=None):
        if not output:
            cmd = self.cli_command.format(ipaddress=ipaddress)
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        # Address: 10.169.14.240, State: Operational, Connection: Open, Hold time: 23
        p1 = re.compile(
            r'^Address: +(?P<ldp_neighbor_address>\S+), '
            r'+State: +(?P<ldp_session_state>\S+), '
            r'+Connection: +(?P<ldp_connection_state>\S+), '
            r'+Hold +time: +(?P<ldp_remaining_time>\S+)$'
        )

        # Session ID: 10.34.2.250:0--10.169.14.240:0
        p2 = re.compile(
            r'^Session ID: +(?P<ldp_session_id>\S+)$'
        )

        # Next keepalive in 3 seconds
        p3 = re.compile(
            r'^Next +keepalive +in +(?P<ldp_keepalive_time>\S+) +seconds$'
        )

        # Passive, Maximum PDU: 4096, Hold time: 30, Neighbor count: 1
        p4 = re.compile(
            r'^(?P<ldp_session_role>\S+), +Maximum +PDU: '
            r'+(?P<ldp_session_max_pdu>\d+), +Hold +time: '
            r'(?P<ldp_holdtime>\d+), Neighbor +count: (?P<ldp_neighbor_count>\d+)$'
        )

        # Neighbor types: discovered
        p5 = re.compile(
            r'^Neighbor +types: +(?P<ldp_neighbor_type>\S+)$'
        )

        # Keepalive interval: 10, Connect retry interval: 1
        p6 = re.compile(
            r'^Keepalive +interval: +(?P<ldp_keepalive_interval>\d+)+, '
            r'+Connect +retry +interval: (?P<ldp_retry_interval>\d+)$'
        )

        # Local address: 10.34.2.250, Remote address: 10.169.14.240
        p7 = re.compile(
            r'^Local +address: +(?P<ldp_local_address>\S+), '
            r'+Remote +address: +(?P<ldp_remote_address>\S+)$'
        )

        # Up for 00:00:47
        p8 = re.compile(
            r'^Up +for +(?P<ldp_up_time>\S+)$'
        )

        # Capabilities advertised: none
        p9 = re.compile(
            r'^Capabilities +advertised: +(?P<ldp_capability_advertised>\S+)$'
        )

        # Capabilities received: none
        p10 = re.compile(
            r'^Capabilities +received: +(?P<ldp_capability_received>\S+)$'
        )

        # Protection: disabled
        p11 = re.compile(
            r'^Protection: +(?P<ldp_session_protection_state>\S+)$'
        )

        # Session flags: none
        p12 = re.compile(
            r'^Session +flags: +(?P<ldp_session_flag>\S+)$'
        )

        # Local - Restart: disabled, Helper mode: enabled
        p13 = re.compile(
            r'^Local +- +Restart: +(?P<ldp_graceful_restart_local>\S+), '
            r'Helper +mode: +(?P<ldp_local_helper_mode>\S+)$'
        )

        # Remote - Restart: disabled, Helper mode: enabled
        # Remote - Restart: enabled, Helper mode: enabled, Reconnect time: 60000
        p14 = re.compile(
            r'^Remote +- +Restart: +(?P<ldp_graceful_restart_remote>\S+), '
            r'Helper +mode: +(?P<ldp_remote_helper_mode>\w+)(, +Reconnect +time: '
            r'+(?P<ldp_remote_reconnect_time>\S+))?$'
        )

        # Local maximum neighbor reconnect time: 120000 msec
        p15 = re.compile(
            r'^Local +maximum +neighbor +reconnect +time: '
            r'+(?P<ldp_local_maximum_reconnect>\S+) +msec$'
        )

        # Local maximum neighbor recovery time: 240000 msec
        p16 = re.compile(
            r'^Local +maximum +neighbor +recovery +time: '
            r'+(?P<ldp_local_maximum_recovery>\S+) +msec$'
        )

        # Local Label Advertisement mode: Downstream unsolicited
        p17 = re.compile(
            r'^Local +Label +Advertisement +mode: '
            r'+(?P<ldp_local_label_adv_mode>[\S\s]+)$'
        )

        # Remote Label Advertisement mode: Downstream unsolicited
        p18 = re.compile(
            r'^Remote +Label +Advertisement +mode: '
            r'+(?P<ldp_remote_label_adv_mode>[\S\s]+)$'
        )

        # Negotiated Label Advertisement mode: Downstream unsolicited
        p18_2 = re.compile(
            r'^Negotiated +Label +Advertisement +mode: '
            r'+(?P<ldp_neg_label_adv_mode>[\S\s]+)$'
        )

        # MTU discovery: disabled
        p19 = re.compile(r'^MTU +discovery: +(?P<ldp_mtu_discovery>\S+)$'
        )

        # Nonstop routing state: Not in sync
        p20 = re.compile(r'^Nonstop +routing +state: +(?P<ldp_session_nsr_state>[\S\s]+)$'
        )

        # Next-hop addresses received:
        p21 = re.compile(r'^(?P<next_hop_flag>Next-hop +addresses +received:)$'
        )

        # Next-hop addresses received:
        p22 = re.compile(r'^(?P<interface_address>[\d\.]+)$'
        )

        

        for line in out.splitlines():
            line = line.strip()

            # Address: 10.169.14.240, State: Operational, Connection: Open, Hold time: 23
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ldp_session_dict = ret_dict.setdefault('ldp-session-information', {}).\
                    setdefault('ldp-session', {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    ldp_session_dict[entry_key] = group_value
                continue

            # Session ID: 10.34.2.250:0--10.169.14.240:0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ldp_session_dict['ldp-session-id'] = group['ldp_session_id']
                continue

            # Next keepalive in 3 seconds
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ldp_session_dict['ldp-keepalive-time'] = group['ldp_keepalive_time']
                continue

            # Passive, Maximum PDU: 4096, Hold time: 30, Neighbor count: 1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    ldp_session_dict[entry_key] = group_value
                continue

            # Neighbor types: discovered
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ldp_neighbor_type_dict = {}
                ldp_neighbor_type_dict['ldp-neighbor-type'] = group['ldp_neighbor_type']
                ldp_session_dict['ldp-neighbor-types'] = ldp_neighbor_type_dict

            # Keepalive interval: 10, Connect retry interval: 1
            m = p6.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    ldp_session_dict[entry_key] = group_value
                continue

            # Local address: 10.34.2.250, Remote address: 10.169.14.240
            m = p7.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    ldp_session_dict[entry_key] = group_value
                continue

            # Up for 00:00:47
            m = p8.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    ldp_session_dict[entry_key] = group_value
                continue

            # Capabilities advertised: none
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ldp_capability_dict = {}
                ldp_capability_dict['ldp-capability'] = group['ldp_capability_advertised']
                ldp_session_dict['ldp-session-capabilities-advertised'] = ldp_capability_dict
                continue

            # Capabilities received: none
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ldp_capability_dict = {}
                ldp_capability_dict['ldp-capability'] = group['ldp_capability_received']
                ldp_session_dict['ldp-session-capabilities-received'] = ldp_capability_dict
                continue

            # Protection: disabled
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ldp_protection_dict = {}
                ldp_protection_dict['ldp-session-protection-state'] = group['ldp_session_protection_state']
                ldp_session_dict['ldp-session-protection'] = ldp_protection_dict
                continue

            # Session flags: none
            m = p12.match(line)
            if m:
                group = m.groupdict()
                ldp_session_protection_dict = {}
                ldp_session_protection_dict['ldp-session-flag'] = group['ldp_session_flag']
                ldp_session_dict['ldp-session-flags'] = ldp_session_protection_dict
                continue

            # Local - Restart: disabled, Helper mode: enabled
            m = p13.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    ldp_session_dict[entry_key] = group_value
                continue

            # Remote - Restart: disabled, Helper mode: enabled
            # Remote - Restart: enabled, Helper mode: enabled, Reconnect time: 60000
            m = p14.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in group.items():
                    if group_value != None:
                            entry_key = group_key.replace('_', '-')
                            ldp_session_dict[entry_key] = group_value
                continue

            # Local maximum neighbor reconnect time: 120000 msec
            m = p15.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    ldp_session_dict[entry_key] = group_value
                continue

            # Local maximum neighbor recovery time: 240000 msec
            m = p16.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    ldp_session_dict[entry_key] = group_value
                continue

            # Local Label Advertisement mode: Downstream unsolicited
            m = p17.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    ldp_session_dict[entry_key] = group_value
                continue

            # Remote Label Advertisement mode: Downstream unsolicited
            m = p18.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    ldp_session_dict[entry_key] = group_value
                continue

            # Negotiated Label Advertisement mode: Downstream unsolicited
            m = p18_2.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    ldp_session_dict[entry_key] = group_value
                continue

            # MTU discovery: disabled
            m = p19.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    ldp_session_dict[entry_key] = group_value
                continue
            
            # Nonstop routing state: Not in sync
            m = p20.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    ldp_session_dict[entry_key] = group_value
                continue

            # Next-hop addresses received:
            m = p21.match(line)
            if m:
                group = m.groupdict()
                if group['next_hop_flag']:
                    next_hop_flag = True
                    ldp_interface_address_list = []
                    ldp_inner_dict = {}
                    ldp_inner_list_dict = {}
                    ldp_inner_list_dict = ldp_interface_address_list
                    ldp_inner_dict['interface-address'] = ldp_inner_list_dict
                    ldp_session_dict['ldp-session-address'] = ldp_inner_dict
                continue

            # 10.169.14.157
            m = p22.match(line)
            if m:
                group = m.groupdict()
                if next_hop_flag:
                    ldp_interface_address_list.append(group['interface_address'])
                continue

        return ret_dict
