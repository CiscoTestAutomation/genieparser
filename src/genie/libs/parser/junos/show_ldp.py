"""show_ldp.py

JUNOS parsers for the following commands:
    * show ldp session
    * show ldp overview
"""

import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Use, Schema
from genie.metaparser.util.exceptions import SchemaTypeError


class ShowLDPSessionSchema(MetaParser):
    """ Schema for
        * show ldp session
    """
    def validate_ldp_session(value):
        if not isinstance(value, list):
            raise SchemaTypeError('LDP Session not a list')

        ldp_session = Schema({
            "ldp-neighbor-address": str,
            "ldp-session-state": str,
            "ldp-connection-state": str,
            "ldp-remaining-time": str,
            Optional("ldp-session-adv-mode"): str,
        })

        for item in value:
            ldp_session.validate(item)
        return value

    schema = {
        "ldp-session-information": {
            "ldp-session": Use(validate_ldp_session)
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

        # 59.128.2.250                        Operational Open          26         DU
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
                "ldp-deaggregate": str,
                "ldp-explicit-null": str,
                "ldp-ipv6-tunneling": str,
                "ldp-strict-targeted-hellos": str,
                "ldp-loopback-if-added": str,
                "ldp-route-preference": int,
                "ldp-unicast-transit-lsp-chaining": str,
                "ldp-p2mp-transit-lsp-chaining": str,
                "ldp-transit-lsp-route-stats": str,
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
                    Optional("ldp-retention-mode"): str,
                    Optional("ldp-control-mode"): str
                },
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
                    "interface-address": str
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
            'Operational': ['ldp-session-operational', 'int'],
            'Retention': ['ldp-retention-mode', 'str'],
            'Control': ['ldp-control-mode', 'str'],
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

        # 106.187.14.157
        p12 = re.compile(r'^(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$')

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
                    'ldp-interface-address', {})
                interface_dict.update({'interface-address': group['ip']})

        return ret_dict
