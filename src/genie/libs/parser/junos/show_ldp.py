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
        "ldp_overview_information": {
            "ldp_overview": {
                "ldp_instance_name": str,
                "ldp_reference_count": int,
                "ldp_router_id": str,
                "ldp_inet": str,
                "ldp_transport_preference": str,
                "ldp_message_id": int,
                "ldp_configuration_sequence": int,
                "ldp_deaggregate": str,
                "ldp_explicit_null": str,
                "ldp_ipv6_tunneling": str,
                "ldp_strict_targeted_hellos": str,
                "ldp_loopback_if_added": str,
                "ldp_route_preference": int,
                "ldp_unicast_transit_lsp_chaining": str,
                "ldp_p2mp_transit_lsp_chaining": str,
                "ldp_transit_lsp_route_stats": str,
                "ldp_route_acknowledgement": str,
                "ldp_bgp_export": str,
                "ldp_mtu_discovery": str,
                "ldp_sr_mapping_client": str,
                "ldp_instance_capability": {
                    "ldp_capability": str
                },
                "ldp_instance_egress_fec_capability": {
                    "ldp_egress_fec_capability": str
                },
                "ldp_session_count": {
                    "ldp_session_operational": int,
                    "ldp_retention_mode": str,
                    "ldp_control_mode": str
                },
                Optional("ldp_dod_session_count"): str,
                "ldp_auto_targeted_session": {
                    "ldp_auto_targeted_session_enabled": str,
                    "ldp_auto_targeted_dyn_tun_ses_count": int
                },
                "ldp_p2mp": {
                    "ldp_p2mp_recursive_route_enabled": str,
                    "ldp_p2mp_no_rsvp_tunneling_enabled": str
                },
                "ldp_timer_overview": {
                    "ldp_instance_keepalive_interval": int,
                    "ldp_instance_keepalive_timeout": int,
                    "ldp_instance_link_hello_interval": int,
                    "ldp_instance_link_hello_hold_time": int,
                    "ldp_instance_targeted_hello_interval": int,
                    "ldp_instance_targeted_hello_hold_time": int,
                    "ldp_instance_label_withdraw_delay": int,
                    "ldp_instance_make_before_break_timeout": int,
                    "ldp_instance_make_before_break_switchover_delay": int,
                    "ldp_instance_link_protection_timeout": int
                },
                "ldp_gr_overview": {
                    "ldp_gr_restart": str,
                    "ldp_gr_helper": str,
                    "ldp_gr_restarting": str,
                    "ldp_gr_reconnect_time": int,
                    "ldp_gr_max_neighbor_reconnect_time": int,
                    "ldp_gr_recovery_time": int,
                    "ldp_gr_max_neighbor_recovery_time": int
                },
                "ldp_te_overview": {
                    "ldp_te_bgp_igp": str,
                    "ldp_te_both_ribs": str,
                    "ldp_te_mpls_forwarding": str,
                    Optional("ldp_rib_group_change_pending"): str
                },
                "ldp_igp_overview": {
                    "ldp_tracking_igp_metric": str,
                    "ldp_igp_sync_session_up_delay": int
                },
                "ldp_session_protect_overview": {
                    "ldp_session_protect": str,
                    "ldp_session_protect_timeout": int
                },
                "ldp_interface_address": {
                    "interface_address": str
                },
                "ldp_job_overview": {
                    "ldp_read_job_time_quantum": int,
                    "ldp_write_job_time_quantum": int,
                    "ldp_read_job_loop_quantum": int,
                    "ldp_write_job_loop_quantum": int,
                    "ldp_inbound_read_job_time_quantum": int,
                    "ldp_outbound_read_job_time_quantum": int,
                    "ldp_inbound_read_job_loop_quantum": int,
                    "ldp_outbound_read_job_loop_quantum": int
                },
                "ldp_label_allocation": {
                    "ldp_label_current_allocs": int,
                    "ldp_label_total_allocs": int,
                    "ldp_label_total_frees": int,
                    "ldp_label_alloc_failure": int,
                    "ldp_global_label_current_allocs": int
                }
            }
        }
    }


class ShowLDPOverview(ShowLDPOverviewSchema):
    """ Parser for:
        * show ldp overview
    """

    cli_command = 'show ldp overview'

    # def insert_dict(a_dict, key, value):

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

        ret_dict = {}
        overview_dict = {}
        var_dict = {
            'Instance': ['ldp_instance_name', 'str'],
            'Reference count': ['ldp_reference_count', 'int'],
            'Router ID': ['ldp_router_id', 'str'],
            'LDP inet': ['ldp_inet', 'str'],
            'Transport preference': ['ldp_transport_preference', 'str'],
            'Message id': ['ldp_message_id', 'int'],
            'Configuration sequence': ['ldp_configuration_sequence', 'int'],
            'Deaggregate': ['ldp_deaggregate', 'str'],
            'Explicit null': ['ldp_explicit_null', 'str'],
            'IPv6 tunneling': ['ldp_ipv6_tunneling', 'str'],
            'Strict targeted hellos': ['ldp_strict_targeted_hellos', 'str'],
            'Loopback if added': ['ldp_loopback_if_added', 'str'],
            'Route preference': ['ldp_route_preference', 'int'],
            'Unicast transit LSP chaining': ['ldp_unicast_transit_lsp_chaining', 'str'],
            'P2MP transit LSP chaining': ['ldp_p2mp_transit_lsp_chaining', 'str'],
            'Transit LSP statistics based on route statistics': ['ldp_transit_lsp_route_stats', 'str'],
            'LDP route acknowledgement': ['ldp_route_acknowledgement', 'str'],
            'BGP export': ['ldp_bgp_export', 'str'],
            'LDP mtu discovery': ['ldp_mtu_discovery', 'str'],
            'LDP SR Mapping Client': ['ldp_sr_mapping_client', 'str'],
            'Capabilities enabled': ['ldp_capability', 'str'],
            'Egress FEC capabilities enabled': ['ldp_egress_fec_capability', 'str'],
            # Downstream unsolicited sessions
            'Operational': ['ldp_session_operational', 'int'],
            'Retention': ['ldp_retention_mode', 'str'],
            'Control': ['ldp_control_mode', 'str'],
            # Auto targeted sessions
            'Auto targeted': ['ldp_auto_targeted_session_enabled', 'str'],
            'Dynamic tunnel session count': ['ldp_auto_targeted_dyn_tun_ses_count', 'int'],
            # P2MP
            'Recursive route': ['ldp_p2mp_recursive_route_enabled', 'str'],
            'No rsvp tunneling': ['ldp_p2mp_no_rsvp_tunneling_enabled', 'str'],
            # Timers
            'Keepalive interval': ['ldp_instance_keepalive_interval', 'int'],
            'Keepalive timeout': ['ldp_instance_keepalive_timeout', 'int'],
            'Link hello interval': ['ldp_instance_link_hello_interval', 'int'],
            'Link hello hold time': ['ldp_instance_link_hello_hold_time', 'int'],
            'Targeted hello interval': ['ldp_instance_targeted_hello_interval', 'int'],
            'Targeted hello hold time': ['ldp_instance_targeted_hello_hold_time', 'int'],
            'Label withdraw delay': ['ldp_instance_label_withdraw_delay', 'int'],
            'Make before break timeout': ['ldp_instance_make_before_break_timeout', 'int'],
            'Make before break switchover delay': ['ldp_instance_make_before_break_switchover_delay', 'int'],
            'Link protection timeout': ['ldp_instance_link_protection_timeout', 'int'],
            # Graceful restart
            'Restart': ['ldp_gr_restart', 'str'],
            'Helper': ['ldp_gr_helper', 'str'],
            'Restart in process': ['ldp_gr_restarting', 'str'],
            'Reconnect time': ['ldp_gr_reconnect_time', 'int'],
            'Max neighbor reconnect time': ['ldp_gr_max_neighbor_reconnect_time', 'int'],
            'Recovery time': ['ldp_gr_recovery_time', 'int'],
            'Max neighbor recovery time': ['ldp_gr_max_neighbor_recovery_time', 'int'],
            # Traffic Engineering
            'Bgp igp': ['ldp_te_bgp_igp', 'str'],
            'Both ribs': ['ldp_te_both_ribs', 'str'],
            'Mpls forwarding': ['ldp_te_mpls_forwarding', 'str'],
            # IGP
            'Tracking igp metric': ['ldp_tracking_igp_metric', 'str'],
            'Sync session up delay': ['ldp_igp_sync_session_up_delay', 'int'],
            # Session protection
            'Session protection': ['ldp_session_protect', 'str'],
            'Session protection timeout': ['ldp_session_protect_timeout', 'int'],
            # LDP Job
            'Read job time quantum': ['ldp_read_job_time_quantum', 'int'],
            'Write job time quantum': ['ldp_write_job_time_quantum', 'int'],
            'Read job loop quantum': ['ldp_read_job_loop_quantum', 'int'],
            'Write job loop quantum': ['ldp_write_job_loop_quantum', 'int'],
            'Backup inbound read job time quantum': ['ldp_inbound_read_job_time_quantum', 'int'],
            'Backup outbound read job time quantum': ['ldp_outbound_read_job_time_quantum', 'int'],
            'Backup inbound read job loop quantum': ['ldp_inbound_read_job_loop_quantum', 'int'],
            'Backup outbound read job loop quantum': [
                'ldp_outbound_read_job_loop_quantum', 'int'],
            # Label allocation
            'Current number of LDP labels allocated': ['ldp_label_current_allocs', 'int'],
            'Total number of LDP labels allocated': ['ldp_label_total_allocs', 'int'],
            'Total number of LDP labels freed': ['ldp_label_total_frees', 'int'],
            'Total number of LDP label allocation failure': ['ldp_label_alloc_failure', 'int'],
            'Current number of labels allocated by all protocols': ['ldp_global_label_current_allocs', 'int'],
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

        for line in out.splitlines():
            line = line.strip()

            m1 = p1.match(line)
            m2 = p2.match(line)
            m3 = p3.match(line)
            m4 = p4.match(line)
            m5 = p5.match(line)
            m6 = p6.match(line)
            m7 = p7.match(line)
            m8 = p8.match(line)
            m9 = p9.match(line)
            m10 = p10.match(line)
            m11 = p11.match(line)

            if m2:
                # Initialize sub dict
                session_dict = overview_dict.setdefault(
                    "ldp_session_count", {})
                session_flag = True

            if m3:
                # Initialize sub dict
                targeted_dict = overview_dict.setdefault(
                    'ldp_auto_targeted_session', {})
                auto_targeted_flag = True

            if m4:
                # Initialize sub dict
                p2mp_dict = overview_dict.setdefault('ldp_p2mp', {})
                p2mp_flag = True

            if m5:
                # Initialize sub dict
                timers_dict = overview_dict.setdefault(
                    'ldp_timer_overview', {})
                timers_flag = True

            if m6:
                # Initialize sub dict
                gr_dict = overview_dict.setdefault('ldp_gr_overview', {})
                grace_restart_flag = True

            if m7:
                # Initialize sub dict
                igp_dict = overview_dict.setdefault('ldp_igp_overview', {})
                igp_flag = True

            if m8:
                # Initialize sub dict
                session_pr_dict = overview_dict.setdefault(
                    'ldp_session_protect_overview', {})
                session_protection_flag = True

            if m9:
                # Initialize sub dict
                te_dict = overview_dict.setdefault('ldp_te_overview', {})
                traffic_engineering_flag = True

            if m10:
                # Initialize sub dict
                job_dict = overview_dict.setdefault('ldp_job_overview', {})
                ldp_job_flag = True

            if m11:
                # Initialize sub dict
                label_alloc_dict = overview_dict.setdefault(
                    'ldp_label_allocation', {})
                label_alloc_flag = True

            if m1:
                group = m1.groupdict()
                # Initialize dict structure
                overview_dict = ret_dict.setdefault(
                    "ldp_overview_information", {}).setdefault("ldp_overview", {})

                # Retrieve a list from predefined dict
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
                elif 'Egress FEC capabilities enabled' in group['var']:
                    overview_dict.setdefault(
                        'ldp_instance_egress_fec_capability', {'ldp_egress_fec_capability': group['value']})

                elif 'Capabilities enabled' in group['var']:
                    overview_dict.setdefault(
                        'ldp_instance_capability', {'ldp_capability': group['value']})

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
                    'ldp_interface_address', {})
                interface_dict.update({'interface_address': group['ip']})

        return ret_dict
