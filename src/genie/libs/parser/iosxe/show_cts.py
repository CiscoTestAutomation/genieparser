import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional, Any
from genie.parsergen import oper_fill_tabular

# ===================================
# Schema for:
#  * 'show cts sxp connections brief'
# ===================================
class ShowCtsSxpConnectionsBriefSchema(MetaParser):
    """Schema for show cts sxp connections brief."""

    schema = {
        "sxp_connections": {
            "total_sxp_connections": int,
            "status": {
                "sxp_status": str,
                "highest_version": int,
                "default_pw": str,
                Optional("key_chain"): str,
                Optional("key_chain_name"): str,
                "source_ip": str,
                "conn_retry": int,
                "reconcile_secs": int,
                "retry_timer": str,
                "peer_sequence_traverse_limit_for_export": str,
                "peer_sequence_traverse_limit_for_import":str
            },
            Optional("sxp_peers"): {
                str: {
                    "source_ip": str,
                    "conn_status": str,
                    "duration": str
                }
            }
        }
    }


# ===================================
# Parser for:
#  * 'show cts sxp connections brief'
#  * 'Parser for show cts sxp connections vrf {vrf} brief'
# ===================================
class ShowCtsSxpConnectionsBrief(ShowCtsSxpConnectionsBriefSchema):
    """Parser for show cts sxp connections brief"""
    """Parser for show cts sxp connections vrf {vrf} brief"""

    cli_command = ['show cts sxp connections brief', 'show cts sxp connections vrf {vrf} brief']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output
        sxp_dict = {}
        # There are no SXP Connections.
        #  SXP              : Enabled
        #  Highest Version Supported: 4
        #  Default Password : Set
        #  Default Key-Chain: Not Set
        #  Default Key-Chain Name: Not Applicable
        #  Default Source IP: 192.168.2.24
        # Connection retry open period: 120 secs
        # Reconcile period: 120 secs
        # Retry open timer is not running
        # Peer-Sequence traverse limit for export: Not Set
        # Peer-Sequence traverse limit for import: Not Set
        #
        # ----------------------------------------------------------------------------------------------------------------------------------
        # Peer_IP          Source_IP        Conn Status                                          Duration
        # ----------------------------------------------------------------------------------------------------------------------------------
        # 10.100.123.1    192.168.2.24   On                                                   44:19:54:52 (dd:hr:mm:sec)
        # 10.100.123.2    192.168.2.24   On                                                   44:19:54:52 (dd:hr:mm:sec)
        # 10.100.123.3    192.168.2.24   On                                                   44:19:54:52 (dd:hr:mm:sec)
        # 10.100.123.4    192.168.2.24   On                                                   44:19:54:52 (dd:hr:mm:sec)
        # 10.100.123.5    192.168.2.24   On                                                   44:18:58:47 (dd:hr:mm:sec)
        # 10.100.123.6    192.168.2.24   On                                                   20:12:53:40 (dd:hr:mm:sec)
        # 10.100.123.7    192.168.2.24   On                                                   44:18:58:47 (dd:hr:mm:sec)
        # 10.100.123.8    192.168.2.24   On                                                   20:12:40:41 (dd:hr:mm:sec)
        # 10.100.123.9    192.168.2.24   On                                                   44:18:58:47 (dd:hr:mm:sec)
        # 10.100.123.10   192.168.2.24   On                                                   44:18:58:47 (dd:hr:mm:sec)
        # 10.100.123.11   192.168.2.24   On                                                   44:22:21:10 (dd:hr:mm:sec)
        # 10.100.123.12   192.168.2.24   On                                                   44:18:58:47 (dd:hr:mm:sec)
        # 10.100.123.13   192.168.2.24   On                                                   45:08:24:37 (dd:hr:mm:sec)
        # 10.100.123.14   192.168.2.24   On                                                   45:08:24:37 (dd:hr:mm:sec)
        # 10.100.123.15   192.168.2.24   On                                                   36:11:31:08 (dd:hr:mm:sec)
        # 10.100.123.16   192.168.2.24   On                                                   36:12:13:50 (dd:hr:mm:sec)
        #
        # Total num of SXP Connections = 16

        #  SXP              : Enabled
        p1 = re.compile(r"\s(?P<sxp_status>(Disabled|Enabled))")
        #  Highest Version Supported: 4
        p2 = re.compile(r"\s+(?P<highest_version>\d+)")
        #  Default Password : Set
        p3 = re.compile(r"\s+(?P<default_pw>(Not\s+Set|Set))")
        #  Default Key-Chain: Not Set
        p4 = re.compile(r"\s+(?P<key_chain>(Not\s+Set|Set))")
        #  Default Source IP: 192.168.2.24
        p5 = re.compile(r"\s+(?P<key_chain_name>(Not\s+Applicable|\S+))")
        #  Default Source IP: 192.168.2.24
        p6 = re.compile(r"\s+(?P<source_ip>(Not\s+Set|\d+\.\d+\.\d+\.\d+))")
        # Connection retry open period: 120 secs
        p7 = re.compile(r"\s+(?P<conn_retry>\d+)")
        # Reconcile period: 120 secs
        p8 = re.compile(r"\s+(?P<reconcile_secs>\d+)")
        # Peer-Sequence traverse limit for export: Not Set
        p9 = re.compile(r"\s+(?P<peer_sequence_traverse_limit_for_export>(Not\s+Set|\S+))")
        # Peer-Sequence traverse limit for import: Not Set
        p10 = re.compile(r"\s+(?P<peer_sequence_traverse_limit_for_import>(Not\s+Set|\S+))")
        # Retry open timer is not running
        p11 = re.compile(r"Retry\s+open\s+timer\s+is\s+(?P<retry_timer>(not\s+running|running))")
        # 10.100.123.12   192.168.2.24   On                                                   44:18:58:47 (dd:hr:mm:sec)
        p12 = re.compile(
            r"(?P<peer_ip>\d+\.\d+\.\d+\.\d+)\s+(?P<source_ip>\d+\.\d+\.\d+\.\d+)\s+(?P<conn_status>\S+)\s+(?P<duration>\d+:\d+:\d+:\d+)")
        # Total num of SXP Connections = 16
        p13 = re.compile(r"^Total\s+num\s+of\s+SXP\s+Connections\s+=\s+(?P<total_sxp_connections>\d+)")

        # This regex map will be used to split the captured line using ':' as the delimeter
        # if it starts with this string, we will use this regex pattern.
        regex_map = {
            "SXP": p1,
            "Highest Version Supported": p2,
            "Default Password": p3,
            "Default Key-Chain": p4,
            "Default Key-Chain Name": p5,
            "Default Source IP": p6,
            "Connection retry open period": p7,
            "Reconcile period": p8,
            "Peer-Sequence traverse limit for export": p9,
            "Peer-Sequence traverse limit for import": p10,
            "Retry open timer is not running": p11,
        }

        # Remove lines with these leading strings
        remove_lines = ('---', 'Peer_IP')


        # Remove unwanted lines from raw text
        def filter_lines(raw_output, remove_lines):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            for clean_line in clean_lines:
                clean_line_strip = clean_line.strip()
                # Remove lines unwanted lines from list of "remove_lines"
                if clean_line_strip.startswith(remove_lines):
                    clean_lines.remove(clean_line)
            return clean_lines

        out = filter_lines(raw_output=out, remove_lines=remove_lines)

        for line in out:
            line_strip = line.strip()
            # ':' Will match lines with a colon and will use regex match and assign Key Value based on match.
            if ": " in line:
                try:
                    data_type, value = line_strip.split(':', 1)
                    regex = regex_map.get(data_type.strip())
                except ValueError:
                    continue
            # Retry open is a one off match that doesn't have a colon.
            elif "Retry open" in line:
                # Retry open timer is not running
                match = p11.match(line_strip)
                if match:
                    groups = match.groupdict()
                    retry_timer = groups['retry_timer']
                if not sxp_dict.get('sxp_connections'):
                    sxp_dict.update({"sxp_connections": {}})
                if not sxp_dict['sxp_connections'].get('status'):
                    sxp_dict['sxp_connections'].update({"status": {}})
                sxp_dict["sxp_connections"]['status'].update({'retry_timer': retry_timer})
                continue
            elif "Total num of SXP Connections" in line:
                # Total num of SXP Connections = 16
                match = p13.match(line_strip)
                if match:
                    groups = match.groupdict()
                    total_sxp_connections = int(groups['total_sxp_connections'])
                sxp_dict["sxp_connections"]['total_sxp_connections'] = total_sxp_connections
                continue
            # All other lines in the output should be p12 and captures peer_ip, source_ip, conn_status, and duration
            else:
                # 10.100.123.12   192.168.2.24   On                                                   44:18:58:47 (dd:hr:mm:sec)
                match = p12.match(line_strip)
                if match:
                    groups = match.groupdict()
                    peer_ip = groups['peer_ip']
                    source_ip = groups['source_ip']
                    conn_status = groups['conn_status']
                    duration = groups['duration']
                    if not sxp_dict.get('sxp_connections'):
                        sxp_dict.update({"sxp_connections": {}})
                    if not sxp_dict['sxp_connections'].get('sxp_peers'):
                        sxp_dict['sxp_connections'].update({"sxp_peers": {}})
                    sxp_dict['sxp_connections']['sxp_peers'].update({
                        peer_ip: {
                            'source_ip': source_ip,
                            'conn_status': conn_status,
                            'duration': duration
                        }})
                continue
            # After all captures are completed, if a regex match exists, assign a key/value to the root dict key.
            if regex:
                match = regex.match(value)
                if match:
                    groups = match.groupdict()
                    for k, v in groups.items():
                        if v is None:
                            continue
                        if v.isdigit() and 'peer_sequence_traverse_limit' not in k:
                            v = int(v)
                        if not sxp_dict.get('sxp_connections'):
                            sxp_dict.update({"sxp_connections": {}})
                        if not sxp_dict['sxp_connections'].get('status'):
                            sxp_dict['sxp_connections'].update({"status": {}})
                        sxp_dict['sxp_connections']['status'].update({k: v})
        if sxp_dict:
            return sxp_dict
        else:
            return {}


# ==================
# Schema for:
#  * 'show cts pacs'
# ==================
class ShowCtsPacsSchema(MetaParser):
    """Schema for show cts pacs."""

    schema = {
        "aid": str,
        "pac_info": {
            "aid": str,
            "pac_type": str,
            "i_id": str,
            "a_id_info": str,
            "credential_lifetime": str,
        },
        "pac_opaque": str,
        "refresh_timer": str,
    }


# ==================
# Parser for:
#  * 'show cts pacs'
# ==================
class ShowCtsPacs(ShowCtsPacsSchema):
    """Parser for show cts pacs"""

    cli_command = 'show cts pacs'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # AID: 1100E046659D4275B644BF946EFA49CD
        # PAC-Info:
        #   PAC-type = Cisco Trustsec
        #   AID: 1100E046659D4275B644BF946EFA49CD
        #   I-ID: gw1
        #   A-ID-Info: Identity Services Engine
        #   Credential Lifetime: 19:56:32 PDT Sun Sep 06 2020
        # PAC-Opaque: 000200B80003000100040010207FCE2A590A44BA0DE959740A348AF00006009C00030100F57E4D71BDE3BD2850B2B63C92E18122000000135EDA996F00093A805A004010F4EDAF81FB6900D03013E907ED81BFB83EE273B8E563BE48DC16B2E9164B1AA6711281937B734E8C449280FCEAF4BE668545B5A55BE20C6346C42AFFCA87FFDDA0AC6A480F9AEE147541EE51FB67CDE0580FD8A746978C78C2CB9E7855BB1667469896AB18902424344AC094B3162EF09488CDB0D6A95139
        # Refresh timer is set for 6w3d

        cts_pacs_dict = {}

        # AID: 1100E046659D4275B644BF946EFA49CD
        aid_capture = re.compile(r"^AID:\s+(?P<aid>\S+)")
        #   PAC-type = Cisco Trustsec
        pac_type_capture = re.compile(r"^PAC-type\s=\s(?P<pac_type>.*$)")
        #     I-ID: gw1
        iid_capture = re.compile(r"^I-ID:\s+(?P<iid>\S+)")
        #   A-ID-Info: Identity Services Engine
        aid_info_capture = re.compile(r"^A-ID-Info:\s+(?P<aid_info>.*$)")
        #   Credential Lifetime: 19:56:32 PDT Sun Sep 06 2020
        credential_lifetime_capture = re.compile(
            r"^Credential\s+Lifetime:\s+(?P<time>\d+:\d+:\d+)\s+(?P<time_zone>\S+)\s+(?P<day>\S+)\s+(?P<month>\S+)\s+(?P<date>\d+)\s+(?P<year>\d+)")
        # PAC - Opaque: 000200B80003000100040010207FCE2A590A44BA0DE959740A348AF00006009C00030100F57E4D71BDE3BD2850B2B63C92E18122000000135EDA996F00093A805A004010F4EDAF81FB6900D03013E907ED81BFB83EE273B8E563BE48DC16B2E9164B1AA6711281937B734E8C449280FCEAF4BE668545B5A55BE20C6346C42AFFCA87FFDDA0AC6A480F9AEE147541EE51FB67CDE0580FD8A746978C78C2CB9E7855BB1667469896AB18902424344AC094B3162EF09488CDB0D6A95139
        pac_opaque_capture = re.compile(r"^PAC-Opaque:\s+(?P<pac_opaque>.*$)")
        # Refresh timer is set for 6w3d
        refresh_timer_capture = re.compile(r"^Refresh\s+timer\s+is\s+set\s+for\s+(?P<refresh_timer>\S+)")

        remove_lines = ('PAC-Info:')

        # Remove unwanted lines from raw text
        def filter_lines(raw_output, remove_lines):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            rendered_lines = []
            for clean_line in clean_lines:
                clean_line_strip = clean_line.strip()
                # Remove lines unwanted lines from list of "remove_lines"
                if not clean_line_strip.startswith(remove_lines):
                    rendered_lines.append(clean_line_strip)
            return rendered_lines

        out = filter_lines(raw_output=out, remove_lines=remove_lines)

        for line in out:
            # AID: 1100E046659D4275B644BF946EFA49CD
            aid_match = aid_capture.match(line)
            if aid_match:
                groups = aid_match.groupdict()
                aid = groups['aid']
                if not cts_pacs_dict.get('aid', {}):
                    cts_pacs_dict['aid'] = aid
                if not cts_pacs_dict.get('pac_info', {}):
                    cts_pacs_dict['pac_info'] = {}
                    cts_pacs_dict['pac_info']['aid'] = aid
                continue
            #   PAC-type = Cisco Trustsec
            pac_type_match = pac_type_capture.match(line)
            if pac_type_match:
                groups = pac_type_match.groupdict()
                pac_type = groups['pac_type']
                if not cts_pacs_dict.get('pac_info', {}):
                    cts_pacs_dict['pac_info'] = {}
                cts_pacs_dict['pac_info']['pac_type'] = pac_type
                continue
            #     I-ID: gw1
            iid_match = iid_capture.match(line)
            if iid_match:
                groups = iid_match.groupdict()
                iid = groups['iid']
                cts_pacs_dict['pac_info']['i_id'] = iid
                continue
            #   A-ID-Info: Identity Services Engine
            aid_info_match = aid_info_capture.match(line)
            if aid_info_match:
                groups = aid_info_match.groupdict()
                aid_info = groups['aid_info']
                cts_pacs_dict['pac_info']['a_id_info'] = aid_info
                continue
            #   Credential Lifetime: 19:56:32 PDT Sun Sep 06 2020
            credential_lifetime_match = credential_lifetime_capture.match(line)
            if credential_lifetime_match:
                groups = credential_lifetime_match.groupdict()
                time = groups['time']
                time_zone = groups['time_zone']
                day = groups['day']
                month = groups['month']
                date = groups['date']
                year = groups['year']
                full_date = f"{day}, {month}/{date}/{year}"
                cts_pacs_dict['pac_info']['credential_lifetime'] = full_date
                continue
            # PAC - Opaque: 000200B80003000100040010207FCE2A590A44BA0DE959740A348AF00006009C00030100F57E4D71BDE3BD2850B2B63C92E18122000000135EDA996F00093A805A004010F4EDAF81FB6900D03013E907ED81BFB83EE273B8E563BE48DC16B2E9164B1AA6711281937B734E8C449280FCEAF4BE668545B5A55BE20C6346C42AFFCA87FFDDA0AC6A480F9AEE147541EE51FB67CDE0580FD8A746978C78C2CB9E7855BB1667469896AB18902424344AC094B3162EF09488CDB0D6A95139
            pac_opaque_match = pac_opaque_capture.match(line)
            if pac_opaque_match:
                groups = pac_opaque_match.groupdict()
                pac_opaque = groups['pac_opaque']
                cts_pacs_dict['pac_opaque'] = pac_opaque
                continue
            # Refresh timer is set for 6w3d
            refresh_timer_match = refresh_timer_capture.match(line)
            if refresh_timer_match:
                groups = refresh_timer_match.groupdict()
                refresh_timer = groups['refresh_timer']
                cts_pacs_dict['refresh_timer'] = refresh_timer
                continue

        return cts_pacs_dict


# =================================
# Schema for:
#  * 'show cts role-based counters'
# =================================
class ShowCtsRoleBasedCountersSchema(MetaParser):
    """Schema for show cts role-based counters."""

    schema = {
        "cts_rb_count": {
            int: {
                "src_group": str,
                "dst_group": str,
                "sw_denied_count": int,
                "hw_denied_count": int,
                "sw_permit_count": int,
                "hw_permit_count": int,
                "sw_monitor_count": int,
                "hw_monitor_count": int
            }
        }
    }


# =================================
# Parser for:
#  * 'show cts role-based counters'
# =================================
class ShowCtsRoleBasedCounters(ShowCtsRoleBasedCountersSchema):
    """Parser for show cts role-based counters"""

    cli_command = 'show cts role-based counters'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        cts_rb_count_dict = {}
        # Role-based IPv4 counters
        # From    To      SW-Denied  HW-Denied  SW-Permitt HW-Permitt SW-Monitor HW-Monitor
        # *       *       0          0          2          30802626587 0          0
        # 2       0       0          4794060    0          0          0          0
        # 7       0       0          0          0          0          0          0
        # 99      0       0          0          0          0          0          0

        rb_counters_capture = re.compile(r"^(?P<src_group>(\d+|\*))\s+(?P<dst_group>(\d+|\*))\s+"
                                         r"(?P<sw_denied_count>\d+)\s+(?P<hw_denied_count>\d+)\s+"
                                         r"(?P<sw_permit_count>\d+)\s+(?P<hw_permit_count>\d+)\s+"
                                         r"(?P<sw_monitor_count>\d+)\s+(?P<hw_monitor_count>\d+)")

        remove_lines = ('Role-based IPv4 counters', 'From')

        # Remove unwanted lines from raw text
        def filter_lines(raw_output, remove_lines):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            rendered_lines = []
            for clean_line in clean_lines:
                clean_line_strip = clean_line.strip()
                # Remove lines unwanted lines from list of "remove_lines"
                if not clean_line_strip.startswith(remove_lines):
                    rendered_lines.append(clean_line_strip)
            return rendered_lines

        out = filter_lines(raw_output=out, remove_lines=remove_lines)

        rb_count_index = 1
        rb_count_data = {}

        for line in out:
            # *       *       0          0          2          30802626587 0          0
            if rb_counters_capture.match(line):
                rb_counters_match = rb_counters_capture.match(line)
                groups = rb_counters_match.groupdict()
                if not cts_rb_count_dict.get('cts_rb_count', {}):
                    cts_rb_count_dict['cts_rb_count'] = {}
                if not cts_rb_count_dict['cts_rb_count'].get(rb_count_index, {}):
                    cts_rb_count_dict['cts_rb_count'][rb_count_index] = {}
                for k, v in groups.items():
                    if v.isdigit() and k not in ['src_group', 'dst_group']:
                        v = int(v)
                    rb_count_data.update({k: v})
                cts_rb_count_dict['cts_rb_count'][rb_count_index].update(rb_count_data)
                rb_count_index = rb_count_index + 1
                continue

        return cts_rb_count_dict



# =============
# Schema for:
#  * 'show cts'
# =============
class ShowCtsSchema(MetaParser):
    """Schema for show cts."""

    schema = {
        Optional("dot1x_feature"): str,
        "cts_device_identity": str,
        Optional("cts_sgt_caching"): str,
        Optional("cts_caching_support"): str,
        Optional("cts_ingress_sgt_caching"): str,
        Optional("cts_sg_epg_translation"): str,
        Optional("interfaces_in_dot1x_mode"): int,
        "interfaces_in_manual_mode": int,
        Optional("interfaces_in_l3_trustsec_mode"): int,
        "interfaces_in_ifc_states": {
            "init": int,
            "authenticating": int,
            "authorizing": int,
            "sap_negotiating": int,
            "open": int,
            "held": int,
            "disconnecting": int,
            "invalid": int
        },
        "cts_events_statistics": {
            "authentication_success": int,
            "authentication_reject": int,
            "authentication_failure": int,
            "authentication_logoff": int,
            "authentication_no_resp": int,
            "authorization_success": int,
            "authorization_failure": int,
            "sap_success": int,
            "sap_failure": int,
            "port_auth_fail": int
        },
        Optional("installed_list"): {
            Optional("name"): str,
            Optional("count"): int,
            Optional("server_ip"): {
                Optional(Any()) : {
                    Optional("port"): int,
                    Optional("a_id"): str,
                    Optional("status"): str,
                    Optional("auto_test"): str,
                    Optional("keywrap_enable"): str,
                    Optional("idle_time_mins"): int,
                    Optional("deadtime_secs"): int
                }
            }
        },
        Optional("pac_summary") : {
            Optional("pac_info"): {
                Optional("pac_valid_until"): str,
            }
        },
        Optional("environment_data_summary"): {
            Optional("data_last_recieved"): str,
            Optional("data_valid_until"): {
                Optional("value"): str,
                Optional("value_format"): str
            }
        },
        Optional("sxp_connections_summary"): {
            Optional("status"): str,
            Optional("highest_supported_version"): int,
            Optional("default_password"): str,
            Optional("default_key_chain"): str,
            Optional("default_key_chain_name"): str,
            Optional("default_source_ip"): str,
            Optional("retry_open_period_secs"): int,
            Optional("reconcile_period_secs"): int,
            Optional("retry_open_timer"): str,
            Optional("peer_sequence_limit_export"): str,
            Optional("peer_sequence_limit_import"): str,
            Optional("peer_ip"): {
                Optional(Any()): {
                    Optional("source_ip"): str,
                    Optional("conn_status"): str,
                    Optional("duration"): {
                        Optional("value"): str,
                        Optional("value_format"): str
                    }
                }
            },
            Optional("total_connections"): int
        },
        Optional("ip_sgt_bindings"): {
            Optional("ipv4"): {
                Optional("total_sxp_bindings"): int,
                Optional("total_active_bindings"): int
            },
            Optional("ipv6"): {
                Optional("total_sxp_bindings"): int,
                Optional("total_active_bindings"): int
            },
            Optional("cts_role_based_enforcement"): str,
            Optional("cts_role_based_vlan_enforcement"): str
        },
        Optional("trusted_untrusted_links"): {
            Optional("number_trusted_links"): int,
            Optional("number_untrusted_links"): int
        }
    }


# =============
# Parser for:
#  * 'show cts'
# =============
class ShowCts(ShowCtsSchema):
    """Parser for show cts"""

    cli_command = 'show cts'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output=output

        # CTS device identity: "SJC-ab-gw1"
        # CTS global sgt-caching: Disabled
        # CTS Ingress sgt-caching: Disabled
        # CTS sg-epg translation status: Disabled
        #
        # Number of CTS interfaces in MANUAL mode: 0
        #
        # Number of CTS interfaces in corresponding IFC state
        # INIT            state:  0
        # AUTHENTICATING  state:  0
        # AUTHORIZING     state:  0
        # SAP_NEGOTIATING state:  0
        # OPEN            state:  0
        # HELD            state:  0
        # DISCONNECTING   state:  0
        # INVALID         state:  0
        #
        # CTS events statistics:
        # authentication success: 0
        # authentication reject : 0
        # authentication failure: 0
        # authentication logoff : 0
        # authentication no resp: 0
        # authorization success : 0
        # authorization failure : 0
        # sap success           : 0
        # sap failure           : 0
        # port auth failure     : 0
        #
        # Installed list: CTSServerList1-0089, 7 server(s):
        # *Server: 10.100.123.1, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
        #         Status = ALIVE
        #         auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
        # *Server: 10.100.123.2, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
        #         Status = ALIVE
        #         auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
        # *Server: 10.100.123.3, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
        #         Status = ALIVE
        #         auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
        # *Server: 10.100.123.4, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
        #         Status = ALIVE
        #         auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
        # *Server: 10.100.123.5, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
        #         Status = ALIVE
        #         auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
        # *Server: 10.100.123.6, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
        #         Status = ALIVE
        #         auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
        # *Server: 10.100.123.7, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
        #         Status = ALIVE
        #         auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
        # ===================
        # CTS PAC Summary
        # =====================
        # PAC-Info:
        #     PAC Valid Until: 19:56:32 PDT Sep 6 2020
        #
        #
        # ============================
        # CTS Environment-Data Summary
        # ============================
        #
        # Environment Data Last Received: 20:04:41 PDT Mon Jul 13 2020
        #
        # Environment Data Valid Until: 0:09:35:43 (dd:hr:mm:sec)
        #
        # ===================================
        # SXP Connections Summary
        # ===================================
        # SXP              : Enabled
        # Highest Version Supported: 4
        # Default Password : Set
        # Default Key-Chain: Not Set
        # Default Key-Chain Name: Not Applicable
        # Default Source IP: 192.168.2.24
        # Connection retry open period: 120 secs
        # Reconcile period: 120 secs
        # Retry open timer is not running
        # Peer-Sequence traverse limit for export: Not Set
        # Peer-Sequence traverse limit for import: Not Set
        #
        # ----------------------------------------------------------------------------------------------------------------------------------
        # Peer_IP          Source_IP        Conn Status                                          Duration
        # ----------------------------------------------------------------------------------------------------------------------------------
        # 10.100.123.1     192.168.2.24   On                                                   44:19:54:57 (dd:hr:mm:sec)
        # 10.100.123.2     192.168.2.24   On                                                   44:19:54:57 (dd:hr:mm:sec)
        # 10.100.123.3     192.168.2.24   On                                                   44:19:54:57 (dd:hr:mm:sec)
        # 10.100.123.4     192.168.2.24   On                                                   44:19:54:57 (dd:hr:mm:sec)
        # 10.100.123.5     192.168.2.24   On                                                   44:18:58:51 (dd:hr:mm:sec)
        # 10.100.123.6     192.168.2.24   On                                                   20:12:53:44 (dd:hr:mm:sec)
        # 10.100.123.7     192.168.2.24   On                                                   44:18:58:51 (dd:hr:mm:sec)
        # 10.100.123.8     192.168.2.24   On                                                   20:12:40:45 (dd:hr:mm:sec)
        # 10.100.123.9     192.168.2.24   On                                                   44:18:58:51 (dd:hr:mm:sec)
        # 10.100.123.10    192.168.2.24   On                                                   44:18:58:51 (dd:hr:mm:sec)
        # 10.100.123.11    192.168.2.24   On                                                   44:22:21:14 (dd:hr:mm:sec)
        # 10.100.123.12    192.168.2.24   On                                                   44:18:58:51 (dd:hr:mm:sec)
        # 10.100.123.13    192.168.2.24   On                                                   45:08:24:42 (dd:hr:mm:sec)
        # 10.100.123.14    192.168.2.24   On                                                   45:08:24:42 (dd:hr:mm:sec)
        # 10.100.123.15    192.168.2.24   On                                                   36:11:31:13 (dd:hr:mm:sec)
        # 10.100.123.16    192.168.2.24   On                                                   36:12:13:54 (dd:hr:mm:sec)
        #
        # Total num of SXP Connections = 16
        # ===================
        #
        # ======================================
        # Summary of IPv4 & IPv6 IP-SGT bindings
        # ======================================
        #
        #
        #             -IPv4-
        #
        # IP-SGT Active Bindings Summary
        # ============================================
        # Total number of SXP      bindings = 3284
        # Total number of active   bindings = 3284
        #
        #
        #             -IPv6-
        #
        # IP-SGT Active Bindings Summary
        # ============================================
        # Total number of SXP      bindings = 111
        # Total number of active   bindings = 111
        #
        #
        # CTS Role Based Enforcement: Enabled
        # CTS Role Based VLAN Enforcement:Enabled
        #
        #
        # =================================
        # Trusted/Un-Trusted Links
        # ==================================
        # Number of Trusted interfaces = 0
        # Number of Un-Trusted interfaces = 0

        # Global Dot1x feature: Disabled
        p_dot1x = re.compile(r"^Global\s+Dot1x\s+feature:\s+(?P<dot1x>Enabled|Disabled)$")

        # CTS device identity: "AAA2220Q2DP"
        p_cts_device = re.compile(r"CTS\s+device\s+identity:\s+\"(?P<cts_identity>\S+)\"$")

        # CTS caching support: disabled
        p_cts_cache = re.compile(r"^CTS\s+caching\s+support:\s+(?P<cts_cache>enabled|disabled)$")

        # CTS sgt-caching global: Disabled
        p_cts_sgt = re.compile(r"^CTS\s+sgt-caching\s+global:\s+(?P<cts_sgt>Enabled|Disabled)$")

        # CTS global sgt-caching: Disabled
        p_cts_2_sgt = re.compile(r"^CTS\s+global\s+sgt-caching:\s+(?P<cts_2_sgt>Enabled|Disabled)$")

        # CTS Ingress sgt-caching: Disabled
        p_cts_ingress = re.compile(r"^CTS\s+Ingress\s+sgt-caching:\s+(?P<cts_ingress>Enabled|Disabled)")

        # CTS sg-epg translation status: Disabled
        p_cts_translation = re.compile(r"^CTS\s+sg-epg\s+translation\s+status:\s+(?P<cts_trans>Enabled|Disabled)")

        # Number of CTS interfaces in MANUAL mode: 0
        p_man_mode = re.compile(r"^Number\s+of\s+CTS\s+interfaces\s+in\s+MANUAL\s+mode:\s+(?P<man_mode>\d+)$")

        # Number of CTS interfaces in DOT1X mode:  0,    MANUAL mode: 0
        p_dot1x_man_mode = re.compile(
        r"^Number\s+of\s+CTS\s+interfaces\s+in\s+DOT1X\s+mode:\s+(?P<dot1x_mode>\d+),\s+MANUAL\s+mode:\s+(?P<man_mode>\d+)$")

        # Number of CTS interfaces in LAYER3 TrustSec mode: 0
        p_l3_mode = re.compile(r"^Number\s+of\s+CTS\s+interfaces\s+in\s+LAYER3\s+TrustSec\s+mode:\s+(?P<l3_mode>\d+)$")

        # Number of CTS interfaces in corresponding IFC state
        p_ifc_state = re.compile(r"^Number\s+of\s+CTS\s+interfaces\s+in\s+corresponding\s+IFC\s+state$")

        # INIT            state:  0
        p_init = re.compile(r"^INIT\s+state:\s+(?P<init>\d+)$")

        # AUTHENTICATING            state:  0
        p_authenticating = re.compile(r"^AUTHENTICATING\s+state:\s+(?P<auth>\d+)$")

        # AUTHORIZING            state:  0
        p_authorizing = re.compile(r"^AUTHORIZING\s+state:\s+(?P<authorizing>\d+)$")

        # SAP_NEGOTIATING            state:  0
        p_sap = re.compile(r"^SAP_NEGOTIATING\s+state:\s+(?P<sap>\d+)$")

        # OPEN            state:  0
        p_open = re.compile(r"^OPEN\s+state:\s+(?P<open>\d+)$")

        # HELD            state:  0
        p_held = re.compile(r"^HELD\s+state:\s+(?P<held>\d+)$")

        # DISCONNECTING            state:  0
        p_disconnect = re.compile(r"^DISCONNECTING\s+state:\s+(?P<disconnect>\d+)$")

        # INVALID            state:  0
        p_invalid = re.compile(r"^INVALID\s+state:\s+(?P<invalid>\d+)$")

        # CTS events statistics:
        p_cts_event = re.compile(r"^CTS\s+events\s+statistics:$")

        # authentication success: 0
        p_stat_authentication = re.compile(r"^authentication\s+success:\s+(?P<cts_authentication>\d+)$")

        # authentication reject: 0
        p_stat_reject = re.compile(r"^authentication\s+reject\s+:\s+(?P<cts_reject>\d+)$")

        # authentication failure: 0
        p_stat_failure = re.compile(r"^authentication\s+failure:\s+(?P<cts_failure>\d+)$")

        # authentication logoff: 0
        p_stat_logoff = re.compile(r"^authentication\s+logoff\s+:\s+(?P<cts_logoff>\d+)$")

        # authentication no resp: 0
        p_stat_noresp = re.compile(r"^authentication\s+no\s+resp:\s+(?P<cts_noresp>\d+)$")

        # authorization success: 0
        p_stat_authorization = re.compile(r"^authorization\s+success\s+:\s+(?P<cts_authorization>\d+)$")

        # authorization failure: 0
        p_stat_authorization_fail = re.compile(r"^authorization\s+failure\s+:\s+(?P<cts_authorization_fail>\d+)$")

        # sap success: 0
        p_stat_sap = re.compile(r"^sap\s+success\s+:\s+(?P<cts_sap>\d+)$")

        # sap failure: 0
        p_stat_sap_failure = re.compile(r"^sap\s+failure\s+:\s+(?P<cts_sap_failure>\d+)$")

        # port auth failure: 0
        p_port_fail = re.compile(r"^port\s+auth\s+failure\s+:\s+(?P<port_fail>\d+)$")

        # Installed list: CTSServerList1-0085, 1 server(s):
        p_installed_list = re.compile(r"^Installed\s+list:\s+(?P<serv_list_name>\S+),\s+(?P<serv_count>\d+)\s+server\(s\):$")

        # *Server: 10.100.123.1, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
        p_server_ast = re.compile(r"^\*Server:\s+(?P<serv_ip>[^,]+),\s+port\s+(?P<serv_port>\d+),\s+A-ID\s+(?P<serv_id>\S+)$")

        # Server: 10.100.123.1, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
        p_server = re.compile(r"^Server:\s+(?P<serv_ip>[^,]+),\s+port\s+(?P<serv_port>\d+),\s+A-ID\s+(?P<serv_id>\S+)$")

        # Status = ALIVE
        p_server_status = re.compile(r"^Status\s+=\s+(?P<serv_status>\S+)")

        # auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
        p_server_attributes = re.compile(
        r"^auto-test\s+=\s+(?P<test>[^,]+),\s+keywrap-enable\s+=\s+(?P<keywrap>[^,]+),\s+idle-time\s+=\s+(?P<idle>\d+)\s+mins,\s+deadtime\s+=\s+(?P<dead>\d+)\s+secs$")

        # ===================
        p_equal_header = re.compile(r"^=+")

        # CTS PAC Summary
        p_header_1 = re.compile(r"^CTS\s+PAc\s+Summary$")

        # PAC-Info:
        p_pac_header = re.compile(r"^PAC-Info:$")

        # PAC Valid Until: 09:24:04 UTC Oct 10 2020
        p_pac_valid = re.compile(r"^PAC\s+Valid\s+Until:\s+(?P<valid>.*)")

        # CTS Environment-Data Summary
        p_environment_header = re.compile(r"^CTS\s+Environment-Data\s+Summary$")

        # Environment Data Last Received: 09:26:17 UTC Tue Jul 14 2020
        p_env_last = re.compile(r"^Environment\s+Data\s+Last\s+Received:\s+(?P<last>.*)$")

        # Environment Data Valid Until: 0:16:13:37 (dd:hr:mm:sec)
        p_env_valid = re.compile(r"^Environment\s+Data\s+Valid\s+Until:\s+(?P<value>\S+)\s+\((?P<format>[^)]+)\)$")

        # SXP Connections Summary
        p_sxp_summary = re.compile(r"^SXP\s+Connections\s+Summary$")

        # SXP              : Enabled
        p_sxp_enabled = re.compile(r"SXP\s+:\s+(?P<status>Enabled|Disabled)$")

        # Highest Version Supported: 4
        p_sxp_version = re.compile(r"^Highest\s+Version\s+Supported:\s+(?P<version>\d+)")

        # Default Password : Set
        p_sxp_password = re.compile(r"^Default\s+Password\s+:\s+(?P<pass>.*)$")

        # Default Key-Chain: Not Set
        p_sxp_key_chain = re.compile(r"^Default\s+Key-Chain:\s+(?P<key>.*)$")

        # Default Key-Chain Name: Not Applicable
        p_sxp_key_chain_name = re.compile(r"^Default\s+Key-Chain\s+Name:\s+(?P<name>.*)$")

        # Default Source IP: Not Set
        p_sxp_source = re.compile(r"Default\s+Source\s+IP:\s+(?P<ip>.*)$")

        # Connection retry open period: 120 secs
        p_sxp_retry = re.compile(r"^Connection\s+retry\s+open\s+period:\s+(?P<time>\d+)\s+secs$")

        # Reconcile period: 120 secs
        p_reconcile = re.compile(r"^Reconcile\s+period:\s+(?P<period>\d+)\s+secs$")

        # Retry open timer is not running
        p_open_timer = re.compile(r"^Retry\s+open\s+timer\s+is\s+not\s+running$")

        # Peer-Sequence traverse limit for export: Not Set
        p_limit_export = re.compile(r"^Peer-Sequence\s+traverse\s+limit\s+for\s+export:\s+(?P<export>.*)$")

        # Peer-Sequence traverse limit for import: Not Set
        p_limit_import = re.compile(r"^Peer-Sequence\s+traverse\s+limit\s+for\s+import:\s+(?P<import>.*)$")

        # There are no SXP Connections.
        p_sxp_no_conn = re.compile(r"^There\s+are\s+no\s+SXP\s+Connections.$")

        # ----------------------------------------------------------------------------------------------------------------------------------
        p_hyphen_header = re.compile(r"^-+$")

        # Peer_IP          Source_IP        Conn Status                                          Duration
        p_sxp_conn_header = re.compile(r"^Peer_IP\s+Source_IP\s+\s+Conn\s+Status\s+Duration$")

        # 10.100.123.1     192.168.2.24   On                                                   44:19:54:57 (dd:hr:mm:sec)
        p_sxp_conn = re.compile(r"^(?P<peer_ip>\S+)\s+(?P<source_ip>\S+)\s+(?P<conn_status>\S+)\s+(?P<dur_val>\S+)\s+\((?P<dur_format>[^)]+)\)$")

        # Total num of SXP Connections = 16
        p_sxp_total = re.compile(r"^Total\s+num\s+of\s+SXP\s+Connections\s+=\s+(?P<total>\d+)$")

        # Summary of IPv4 & IPv6 IP-SGT bindings
        p_sum_ip_sgt = re.compile(r"^Summary\s+of\s+IPv4\s+&\s+IPv6\s+IP-SGT\s+bindings$")

        # -IPv4-
        p_ipv4_header = re.compile(r"^-IPv4-$")

        # IP-SGT Active Bindings Summary
        p_ip_sgt_active_header = re.compile(r"^IP-SGT\s+Active\s+Bindings\s+Summary$")

        # Total number of SXP      bindings = 3284
        p_total_sxp = re.compile(r"^Total\s+number\s+of\s+SXP\s+bindings\s+=\s+(?P<total>\d+)$")

        # Total number of active   bindings = 3284
        p_total_active_sxp = re.compile(r"^Total\s+number\s+of\s+active\s+bindings\s+=\s+(?P<active>\d+)$")

        # -IPv6-
        p_ipv6_header = re.compile(r"^-IPv6-$")

        # CTS Role Based Enforcement: Enabled
        p_role_based = re.compile(r"^CTS\s+Role\s+Based\s+Enforcement:\s+(?P<value>Enabled|Disabled)$")

        # CTS Role Based VLAN Enforcement:Enabled
        p_role_based_vlan = re.compile(r"^CTS\s+Role\s+Based\s+VLAN\s+Enforcement:(?P<value>Enabled|Disabled)$")

        # Trusted/Un-Trusted Links
        p_links_header = re.compile(r"^Trusted\/Un-Trusted\s+Links$")

        # Number of Trusted interfaces = 0
        p_trusted_links = re.compile(r"^Number\s+of\s+Trusted\s+interfaces\s+=\s+(?P<count>\d+)$")

        # Number of Un-Trusted interfaces = 0
        p_untrusted_links = re.compile(r"^Number\s+of\s+Un-Trusted\s+interfaces\s+=\s+(?P<count>\d+)$")

        def update_bindings(active_bindings, cts_dict):
            if len(active_bindings) == 2:
                cts_dict["ip_sgt_bindings"]["ipv4"].update({ "total_sxp_bindings": int(active_bindings[0]) })
                cts_dict["ip_sgt_bindings"]["ipv6"].update({ "total_sxp_bindings": int(active_bindings[1]) })
            else:
                # Update IPv4 binding count
                cts_dict["ip_sgt_bindings"]["ipv4"].update({ "total_sxp_bindings": int(active_bindings[0]) })
                cts_dict["ip_sgt_bindings"]["ipv4"].update({ "total_active_bindings": int(active_bindings[1]) })
                # Update IPv6 binding count
                cts_dict["ip_sgt_bindings"]["ipv6"].update({ "total_sxp_bindings": int(active_bindings[2]) })
                cts_dict["ip_sgt_bindings"]["ipv6"].update({ "total_active_bindings": int(active_bindings[3]) })

            return cts_dict


        cts_dict = {}
        active_bindings = []

        for line in output.splitlines():
            line = line.strip()
            # Global Dot1x feature: Disabled
            if p_dot1x.match(line):
                match = p_dot1x.match(line)
                cts_dict.update({ "dot1x_feature": match.group("dot1x") })
                continue
            # CTS device identity: "AAA2220Q2DP"
            elif p_cts_device.match(line):
                match = p_cts_device.match(line)
                cts_dict.update({ "cts_device_identity": match.group("cts_identity")})
                continue
            # CTS caching support: disabled
            elif p_cts_cache.match(line):
                match = p_cts_cache.match(line)
                cts_dict.update({ "cts_caching_support": match.group("cts_cache")})
                continue
            # CTS sgt-caching global: Disabled
            elif p_cts_sgt.match(line):
                match = p_cts_sgt.match(line)
                cts_dict.update({ "cts_sgt_caching": match.group("cts_sgt")})
                continue
            # CTS global sgt-caching: Disabled
            elif p_cts_2_sgt.match(line):
                match = p_cts_2_sgt.match(line)
                cts_dict.update({ "cts_sgt_caching": match.group("cts_2_sgt")})
                continue
            # CTS Ingress sgt-caching: Disabled
            elif p_cts_ingress.match(line):
                match = p_cts_ingress.match(line)
                cts_dict.update({ "cts_ingress_sgt_caching": match.group("cts_ingress") })
            # CTS sg-epg translation status: Disabled
            elif p_cts_translation.match(line):
                match = p_cts_translation.match(line)
                cts_dict.update({ "cts_sg_epg_translation": match.group("cts_trans") })
            # Number of CTS interfaces in DOT1X mode:  0,    MANUAL mode: 0
            elif p_dot1x_man_mode.match(line):
                match = p_dot1x_man_mode.match(line)
                cts_dict.update({ "interfaces_in_dot1x_mode": int(match.group("dot1x_mode")), "interfaces_in_manual_mode": int(match.group("man_mode")) })
                continue
            # Number of CTS interfaces in MANUAL mode: 0
            elif p_man_mode.match(line):
                match = p_man_mode.match(line)
                cts_dict.update({ "interfaces_in_manual_mode": int(match.group("man_mode")) })
                continue
            # Number of CTS interfaces in LAYER3 TrustSec mode: 0
            elif p_l3_mode.match(line):
                match = p_l3_mode.match(line)
                cts_dict.update({ "interfaces_in_l3_trustsec_mode": match.group("l3_mode")})
                continue
            # Number of CTS interfaces in corresponding IFC state
            elif p_ifc_state.match(line):
                if not cts_dict.get("interfaces_in_ifc_states"):
                    cts_dict.update({ "interfaces_in_ifc_states": {} })
                    continue
            # INIT            state:  0
            elif p_init.match(line):
                match = p_init.match(line)
                cts_dict["interfaces_in_ifc_states"].update({ "init" : int(match.group("init")) })
                continue
            # AUTHENTICATING           state:  0
            elif p_authenticating.match(line):
                match = p_authenticating.match(line)
                cts_dict["interfaces_in_ifc_states"].update({ "authenticating" : int(match.group("auth")) })
                continue
            # AUTHORIZING            state:  0
            elif p_authorizing.match(line):
                match = p_authorizing.match(line)
                cts_dict["interfaces_in_ifc_states"].update({ "authorizing" : int(match.group("authorizing")) })
                continue
            # SAP_NEGOTIATING            state:  0
            elif p_sap.match(line):
                match = p_sap.match(line)
                cts_dict["interfaces_in_ifc_states"].update({ "sap_negotiating" : int(match.group("sap")) })
                continue
            # OPEN            state:  0
            elif p_open.match(line):
                match = p_open.match(line)
                cts_dict["interfaces_in_ifc_states"].update({ "open" : int(match.group("open")) })
                continue
            # HELD            state:  0
            elif p_held.match(line):
                match = p_held.match(line)
                cts_dict["interfaces_in_ifc_states"].update({ "held" : int(match.group("held")) })
                continue
            # DISCONNECTING            state:  0
            elif p_disconnect.match(line):
                match = p_disconnect.match(line)
                cts_dict["interfaces_in_ifc_states"].update({ "disconnecting" : int(match.group("disconnect")) })
                continue
            # INVALID            state:  0
            elif p_invalid.match(line):
                match = p_invalid.match(line)
                cts_dict["interfaces_in_ifc_states"].update({ "invalid" : int(match.group("invalid")) })
                continue
            # CTS events statistics
            elif p_cts_event.match(line):
                if not cts_dict.get("cts_events_statistics"):
                    cts_dict.update({ "cts_events_statistics": {} })
                continue
            # authentication success: 0
            elif p_stat_authentication.match(line):
                match = p_stat_authentication.match(line)
                cts_dict["cts_events_statistics"].update({ "authentication_success": int(match.group("cts_authentication")) })
                continue
            # authentication reject: 0
            elif p_stat_reject.match(line):
                match = p_stat_reject.match(line)
                cts_dict["cts_events_statistics"].update({ "authentication_reject": int(match.group("cts_reject")) })
                continue
            # authentication failure: 0
            elif p_stat_failure.match(line):
                match = p_stat_failure.match(line)
                cts_dict["cts_events_statistics"].update({ "authentication_failure": int(match.group("cts_failure")) })
                continue
            # authentication logoff: 0
            elif p_stat_logoff.match(line):
                match = p_stat_logoff.match(line)
                cts_dict["cts_events_statistics"].update({ "authentication_logoff": int(match.group("cts_logoff")) })
                continue
            # authentication no resp: 0
            elif p_stat_noresp.match(line):
                match = p_stat_noresp.match(line)
                cts_dict["cts_events_statistics"].update({ "authentication_no_resp": int(match.group("cts_noresp")) })
                continue
            # authorization success: 0
            elif p_stat_authorization.match(line):
                match = p_stat_authorization.match(line)
                cts_dict["cts_events_statistics"].update({ "authorization_success": int(match.group("cts_authorization")) })
                continue
            # authorization failure: 0
            elif p_stat_authorization_fail.match(line):
                match = p_stat_authorization_fail.match(line)
                cts_dict["cts_events_statistics"].update({ "authorization_failure": int(match.group("cts_authorization_fail")) })
                continue
            # sap success: 0
            elif p_stat_sap.match(line):
                match = p_stat_sap.match(line)
                cts_dict["cts_events_statistics"].update({ "sap_success": int(match.group("cts_sap")) })
                continue
            # sap failure: 0
            elif p_stat_sap_failure.match(line):
                match = p_stat_sap_failure.match(line)
                cts_dict["cts_events_statistics"].update({ "sap_failure": int(match.group("cts_sap_failure")) })
                continue
            elif p_port_fail.match(line):
                match = p_port_fail.match(line)
                cts_dict["cts_events_statistics"].update({ "port_auth_fail": int(match.group("port_fail")) })
                continue
            # Installed list: CTSServerList1-0089, 7 server(s):
            elif p_installed_list.match(line):
                match = p_installed_list.match(line)
                group = match.groupdict()
                if not cts_dict.get("installed_list"):
                    cts_dict.update({ "installed_list" : {} })
                cts_dict["installed_list"].update({ "name" : group["serv_list_name"], "count": int(group["serv_count"]) })
                continue
            # *Server: 10.100.123.1, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
            elif p_server_ast.match(line):
                match = p_server_ast.match(line)
                group = match.groupdict()
                serv_ip = group["serv_ip"]
                if not cts_dict["installed_list"].get("server_ip"):
                    cts_dict["installed_list"].update({ "server_ip": {} })
                cts_dict["installed_list"]["server_ip"].update({ serv_ip: {} })
                cts_dict["installed_list"]["server_ip"][serv_ip].update({ "port": int(group["serv_port"]), "a_id": group["serv_id"]})
                continue
            # Server: 10.100.123.1, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
            elif p_server.match(line):
                match = p_server.match(line)
                group = match.groupdict()
                serv_ip = group["serv_ip"]
                if not cts_dict["installed_list"].get("server_ip"):
                    cts_dict["installed_list"].update({ "server_ip": {} })
                cts_dict["installed_list"]["server_ip"].update({ serv_ip: {} })
                cts_dict["installed_list"]["server_ip"][serv_ip].update({ "port": int(group["serv_port"]), "a_id": group["serv_id"]})
                continue
            # Status = ALIVE
            elif p_server_status.match(line):
                match = p_server_status.match(line)
                cts_dict["installed_list"]["server_ip"][serv_ip].update({ "status": match.group("serv_status") })
                continue
            # auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
            elif p_server_attributes.match(line):
                match = p_server_attributes.match(line)
                group = match.groupdict()
                cts_dict["installed_list"]["server_ip"][serv_ip].update({ "auto_test": group["test"], "keywrap_enable": group["keywrap"],
                                                                        "idle_time_mins": int(group["idle"]), "deadtime_secs": int(group["dead"]) })
                continue
            # Any number of '=' ex: "======" or "================================"
            elif p_equal_header.match(line):
                continue
            # CTS PAC Summary
            elif p_header_1.match(line):
                continue
            # PAC-info
            elif p_pac_header.match(line):
                continue
            # PAC Valid Until: 09:24:04 UTC Oct 10 2020
            elif p_pac_valid.match(line):
                match = p_pac_valid.match(line)
                cts_dict.update({ "pac_summary": { "pac_info": {} }})
                cts_dict["pac_summary"]["pac_info"].update({ "pac_valid_until": match.group("valid")})
                continue
            # CTS Environment-Data Summary
            elif p_environment_header.match(line):
                if not cts_dict.get("environemtn_data_summary"):
                    cts_dict.update({ "environment_data_summary": {} })
                continue
            # Environment Data Last Received: 09:26:17 UTC Tue Jul 14 2020
            elif p_env_last.match(line):
                match = p_env_last.match(line)
                cts_dict["environment_data_summary"].update({ "data_last_recieved": match.group("last") })
                continue
            # Environment Data Valid Until: 0:16:13:37 (dd:hr:mm:sec)
            elif p_env_valid.match(line):
                match = p_env_valid.match(line)
                group = match.groupdict()
                cts_dict["environment_data_summary"].update({ "data_valid_until": {} })
                cts_dict["environment_data_summary"]["data_valid_until"].update({ "value" : group["value"], "value_format": group["format"] })
                continue
            # SXP Connections Summary
            elif p_sxp_summary.match(line):
                if not cts_dict.get("sxp_connections_summary"):
                    cts_dict.update({ "sxp_connections_summary": {} })
                continue
            # SXP              : Enabled
            elif p_sxp_enabled.match(line):
                match = p_sxp_enabled.match(line)
                cts_dict["sxp_connections_summary"].update({ "status": match.group("status") })
                continue
            # Highest Version Supported: 4
            elif p_sxp_version.match(line):
                match = p_sxp_version.match(line)
                cts_dict["sxp_connections_summary"].update({ "highest_supported_version": int(match.group("version")) })
                continue
            # Default Password : Set
            elif p_sxp_password.match(line):
                match = p_sxp_password.match(line)
                cts_dict["sxp_connections_summary"].update({ "default_password": match.group("pass") })
                continue
            # Default Key-Chain: Not Set
            elif p_sxp_key_chain.match(line):
                match = p_sxp_key_chain.match(line)
                cts_dict["sxp_connections_summary"].update({ "default_key_chain": match.group("key") })
                continue
            # Default Key-Chain Name: Not Applicable
            elif p_sxp_key_chain_name.match(line):
                match = p_sxp_key_chain_name.match(line)
                cts_dict["sxp_connections_summary"].update({ "default_key_chain_name": match.group("name") })
                continue
            # Default Source IP: Not Set
            elif p_sxp_source.match(line):
                match = p_sxp_source.match(line)
                cts_dict["sxp_connections_summary"].update({ "default_source_ip": match.group("ip") })
                continue
            # Connection retry open period: 120 secs
            elif p_sxp_retry.match(line):
                match = p_sxp_retry.match(line)
                cts_dict["sxp_connections_summary"].update({ "retry_open_period_secs": int(match.group("time")) })
                continue
            # Reconcile period: 120 secs
            elif p_reconcile.match(line):
                match = p_reconcile.match(line)
                cts_dict["sxp_connections_summary"].update({ "reconcile_period_secs": int(match.group("period")) })
                continue
            # Retry open timer is not running
            elif p_open_timer.match(line):
                match = p_open_timer.match(line)
                cts_dict["sxp_connections_summary"].update({ "retry_open_timer": "disabled" })
                continue
            # Peer-Sequence traverse limit for export: Not Set
            elif p_limit_export.match(line):
                match = p_limit_export.match(line)
                cts_dict["sxp_connections_summary"].update({ "peer_sequence_limit_export": match.group("export")  })
                continue
            # Peer-Sequence traverse limit for import: Not Set
            elif p_limit_import.match(line):
                match = p_limit_import.match(line)
                cts_dict["sxp_connections_summary"].update({ "peer_sequence_limit_import": match.group("import")  })
                continue
            # There are no SXP Connections.
            elif p_sxp_no_conn.match(line):
                continue
            # ----------------------------------------------------------------------------------------------------------------------------------
            elif p_hyphen_header.match(line):
                continue
            # Peer_IP          Source_IP        Conn Status                                          Duration
            elif p_sxp_conn_header.match(line):
                continue
            # Total num of SXP Connections = 16
            elif p_sxp_total.match(line):
                match = p_sxp_total.match(line)
                cts_dict["sxp_connections_summary"].update({ "total_connections": int(match.group("total")) })
                continue
            # 10.100.123.1     192.168.2.24   On                                                   44:19:54:57 (dd:hr:mm:sec)
            elif p_sxp_conn.match(line):
                match = p_sxp_conn.match(line)
                group = match.groupdict()
                peer_ip = group["peer_ip"]
                if not cts_dict["sxp_connections_summary"].get("peer_ip"):
                    cts_dict["sxp_connections_summary"].update({ "peer_ip": {} })
                cts_dict["sxp_connections_summary"]["peer_ip"].update({ peer_ip: {} })
                cts_dict["sxp_connections_summary"]["peer_ip"][peer_ip].update({ "source_ip": group["source_ip"], "conn_status": group["conn_status"],
                                                                                "duration": {} })
                cts_dict["sxp_connections_summary"]["peer_ip"][peer_ip]["duration"].update({ "value": group["dur_val"], "value_format": group["dur_format"] })
                continue
            # Summary of IPv4 & IPv6 IP-SGT bindings
            elif p_sum_ip_sgt.match(line):
                if not cts_dict.get("ip_sgt_bindings"):
                    cts_dict.update({ "ip_sgt_bindings": {} })
                continue
            # -IPv4-
            elif p_ipv4_header.match(line):
                if not cts_dict["ip_sgt_bindings"].get("ipv4"):
                    cts_dict["ip_sgt_bindings"].update({ "ipv4": {} })
                continue
            # IP-SGT Active Bindings Summary
            elif p_ip_sgt_active_header.match(line):
                continue
            # Total number of SXP      bindings = 3284
            elif p_total_sxp.match(line):
                match = p_total_sxp.match(line)
                active_bindings.append(match.group("total"))
                # cts_dict["ip_sgt_bindings"]["ipv4"].update({ "total_sxp_bindings": match.group("total") })
                continue
            # Total number of active   bindings = 3284
            elif p_total_active_sxp.match(line):
                match = p_total_active_sxp.match(line)
                active_bindings.append(match.group("active"))
                # cts_dict["ip_sgt_bindings"]["ipv4"].update({ "total_active_bindings": match.group("active") })
                continue
            # -IPv6-
            elif p_ipv6_header.match(line):
                if not cts_dict["ip_sgt_bindings"].get("ipv6"):
                    cts_dict["ip_sgt_bindings"].update({ "ipv6": {} })
                continue
            # CTS Role Based Enforcement: Enabled
            elif p_role_based.match(line):
                match = p_role_based.match(line)
                cts_dict["ip_sgt_bindings"].update({ "cts_role_based_enforcement": match.group("value") })
                continue
            # CTS Role Based VLAN Enforcement: Enabled
            elif p_role_based_vlan.match(line):
                match = p_role_based_vlan.match(line)
                cts_dict["ip_sgt_bindings"].update({ "cts_role_based_vlan_enforcement": match.group("value") })
                continue
            # Trusted/Un-Trusted Links
            elif p_links_header.match(line):
                if not cts_dict.get("trusted_untrusted_links"):
                    cts_dict.update({ "trusted_untrusted_links" : {} })
                continue
            # Number of Trusted interfaces = 0
            elif p_trusted_links.match(line):
                match = p_trusted_links.match(line)
                cts_dict["trusted_untrusted_links"].update({ "number_trusted_links": int(match.group("count")) })
            # Number of Un-Trusted interfaces = 0
            elif p_untrusted_links.match(line):
                match = p_untrusted_links.match(line)
                cts_dict["trusted_untrusted_links"].update({ "number_untrusted_links": int(match.group("count")) })
                continue


        if not active_bindings:
            return cts_dict
        else:
            cts_dict = update_bindings(active_bindings, cts_dict)
            return cts_dict


# ==============================
# Schema for:
#  * 'show cts environment-data'
# ==============================
class ShowCtsEnvironmentDataSchema(MetaParser):
    """Schema for show cts environment-data."""

    schema = {
        "cts_env": {
            "current_state": str,
            "last_status": str,
            Optional("sgt_tags"): str,
            Optional("tag_status"): str,
            Optional("server_list_name"): str,
            Optional("server_count"): int,
            Optional("servers"): {
                Optional(int): {
                    Optional("server_ip"): str,
                    Optional("port"): int,
                    Optional("aid"): str,
                    Optional("server_status"): str,
                    Optional("auto_test"): str,
                    Optional("keywrap_enable"): str,
                    Optional("idle_time_mins"): int,
                    Optional("dead_time_secs"): int
                }
          },
            Optional("security_groups"): {
                Optional(int): {
                    Optional("sec_group"): str,
                    Optional("sec_group_name"): str
              }
          },
          Optional("env_data_lifetime_secs"): int,
          Optional("last_update"): {
                Optional("date"): str,
                Optional("time"): str,
                Optional("time_zone"): str
          },
          Optional("expiration"): str,
          Optional("refresh"): str,
          "state_machine_status": str,
          Optional("retry_timer_status"): str,
          Optional("cache_data_status"): str
        }
    }


# ==============================
# Parser for:
#  * 'show cts environment-data'
# ==============================
class ShowCtsEnvironmentData(ShowCtsEnvironmentDataSchema):
    """Parser for show cts environment-data"""

    cli_command = 'show cts environment-data'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        cts_env_dict = {}
        # CTS Environment Data
        # ====================
        # Current state = COMPLETE
        # Last status = Successful
        # Local Device SGT:
        #   SGT tag = 0-16:Unknown
        # Server List Info:
        # Installed list: CTSServerList1-0089, 4 server(s):
        #  *Server: 10.1.100.4, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
        #           Status = ALIVE
        #           auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
        #  *Server: 10.1.100.5, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
        #           Status = ALIVE
        #           auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
        #  *Server: 10.1.100.6, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
        #           Status = ALIVE
        #           auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
        #  *Server: 10.1.100.6, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
        #           Status = ALIVE
        #           auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
        # Security Group Name Table:
        #     0-15:Unit0
        #     2-12:Unit1
        #     3-10:Unit2
        #     4-11:Device11
        #     3215-08:K2
        #     9999-06:Q1
        #     68-10:North
        #     5016-00:Quarantine
        #     8000-00:TEST_8000
        # Environment Data Lifetime = 86400 secs
        # Last update time = 20:04:42 PDT Tue Jul 21 2020
        # Env-data expires in   0:00:46:51 (dd:hr:mm:sec)
        # Env-data refreshes in 0:00:46:51 (dd:hr:mm:sec)
        # Cache data applied           = NONE
        # State Machine is running

        # Current state = COMPLETE
        current_state_capture = re.compile(r"^Current\s+state\s+=\s+(?P<state>.*$)")
        # Last status = Successful
        last_status_capture = re.compile(r"^Last\s+status\s+=\s+(?P<last_status>.*$)")
        #   SGT tag = 0-16:Unknown
        tags_capture = re.compile(r"^SGT\s+tag\s+=\s+(?P<sgt_tags>\d+-\d+):(?P<tag_status>\w+)")
        # Installed list: CTSServerList1-0089, 4 server(s):
        server_list_capture = re.compile(
            r"^Installed\s+list:\s+(?P<server_list_name>\S+),\s+(?P<server_count>\d+)\s+server\(s\):", re.MULTILINE)
        #  *Server: 10.1.100.4, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
        servers_capture = re.compile(
            r"^(\*|)Server:\s+(?P<server_ip>\d+\.\d+\.\d+\.\d+),\s+port\s+(?P<port>\d+),\s+A-ID\s+(?P<aid>\S+)")
        #           Status = ALIVE
        server_status_capture = re.compile(r"^Status\s+=\s+(?P<server_status>\S+)")
        #           auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
        keywrap_capture = re.compile(
            r"^auto-test\s+=\s+(?P<auto_test>(TRUE|FALSE)),\s+keywrap-enable\s+=\s+(?P<keywrap_enable>(TRUE|FALSE)),\s+idle-time\s+=\s+(?P<idle_time_mins>\d+)\s+mins,\s+deadtime\s+=\s+(?P<dead_time_secs>\d+)\s+secs")
        #     0-15:Unit0
        sec_group_capture = re.compile(r"^(?P<sec_group>\S+):(?P<sec_group_name>\S+)")
        # Environment Data Lifetime = 86400 secs
        env_data_capture = re.compile(r"^Environment\s+Data\s+Lifetime\s+=\s+(?P<env_data_lifetime_secs>\d+)\s+secs")
        # Last update time = 20:04:42 PDT Tue Jul 21 2020
        last_update_capture = re.compile(
            r"^Last\s+update\s+time\s+=\s+(?P<time>\d+:\d+:\d+)\s+(?P<time_zone>\w+)\s+(?P<day>\S+)\s+(?P<month>\S+)\s+(?P<date>\d+)\s+(?P<year>\d+)")
        # Env-data expires in   0:00:46:51 (dd:hr:mm:sec)
        expiration_capture = re.compile(r"^Env-data\s+expires\s+in\s+(?P<expiration>\d+:\d+:\d+:\d+)\s+\S+")
        # Env-data refreshes in 0:00:46:51 (dd:hr:mm:sec)
        refresh_capture = re.compile(r"^Env-data\s+refreshes\s+in\s+(?P<refresh>\d+:\d+:\d+:\d+)\s+\S+")
        # Cache data applied           = NONE
        cache_data_capture = re.compile(r"^Cache\s+data\s+applied\s+=\s+(?P<cache_data_status>\S+)")
        # State Machine is running
        state_machine_capture = re.compile(r"^State\s+Machine\s+is\s+(?P<state_machine_status>\S+)")
        # Retry_timer (60 secs) is not running
        retry_capture = re.compile(
            r"^Retry_timer\s+\((?P<retry_timer_secs>\d+)\s+secs\)\s+is\s+(?P<retry_timer_status>.*$)")

        remove_lines = (
        'CTS Environment Data', '=========', 'Local Device SGT:', 'Server List Info:', 'Security Group Name Table:')

        # Remove unwanted lines from raw text
        def filter_lines(raw_output, remove_lines):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            rendered_lines = []
            for clean_line in clean_lines:
                clean_line_strip = clean_line.strip()
                # Remove lines unwanted lines from list of "remove_lines"
                if not clean_line_strip.startswith(remove_lines):
                    rendered_lines.append(clean_line_strip)
            return rendered_lines

        out = filter_lines(raw_output=out, remove_lines=remove_lines)

        server_data = {}
        security_groups = {}
        keywrap_index = 1
        sec_group_index = 1
        for line in out:
            # Current state = COMPLETE
            current_state_match = current_state_capture.match(line)
            if current_state_match:
                groups = current_state_match.groupdict()
                current_state = groups['state']
                if not cts_env_dict.get('cts_env', {}):
                    cts_env_dict['cts_env'] = {}
                cts_env_dict['cts_env']['current_state'] = current_state
                continue
            # Last status = Successful
            last_status_match = last_status_capture.match(line)
            if last_status_match:
                groups = last_status_match.groupdict()
                last_status = groups['last_status']
                cts_env_dict['cts_env']['last_status'] = last_status
                continue
            #   SGT tag = 0-16:Unknown
            tags_match = tags_capture.match(line)
            if tags_match:
                groups = tags_match.groupdict()
                sgt_tags = groups['sgt_tags']
                tag_status = groups['tag_status']
                cts_env_dict['cts_env']['sgt_tags'] = sgt_tags
                cts_env_dict['cts_env']['tag_status'] = tag_status
                continue
            # Installed list: CTSServerList1-0089, 4 server(s):
            server_list_match = server_list_capture.match(line)
            if server_list_match:
                groups = server_list_match.groupdict()
                server_list_name = groups['server_list_name']
                server_count = int(groups['server_count'])
                cts_env_dict['cts_env']['server_list_name'] = server_list_name
                cts_env_dict['cts_env']['server_count'] = server_count
                continue
            #  *Server: 10.1.100.4, port 1812, A-ID A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A
            servers_match = servers_capture.match(line)
            if servers_match:
                groups = servers_match.groupdict()
                server_ip = groups['server_ip']
                port = int(groups['port'])
                aid = groups['aid']
                server_data = {'server_ip': server_ip, 'port': port, 'aid': aid}
                continue
            #           Status = ALIVE
            server_status_match = server_status_capture.match(line)
            if server_status_match:
                groups = server_status_match.groupdict()
                server_status = groups['server_status']
                server_data.update({'server_status': server_status})
                if not cts_env_dict['cts_env'].get('servers', {}):
                    cts_env_dict['cts_env']['servers'] = []
                continue
            #           auto-test = FALSE, keywrap-enable = FALSE, idle-time = 60 mins, deadtime = 20 secs
            keywrap_match = keywrap_capture.match(line)
            if keywrap_match:
                groups = keywrap_match.groupdict()
                auto_test = groups['auto_test']
                keywrap_enable = groups['keywrap_enable']
                idle_time_mins = int(groups['idle_time_mins'])
                dead_time_secs = int(groups['dead_time_secs'])
                server_data.update(
                    {'auto_test': auto_test, 'keywrap_enable': keywrap_enable, 'idle_time_mins': idle_time_mins,
                     'dead_time_secs': dead_time_secs})
                if not cts_env_dict['cts_env'].get('servers', {}):
                    cts_env_dict['cts_env']['servers'] = {}
                if not cts_env_dict['cts_env']['servers'].get(keywrap_index, {}):
                    cts_env_dict['cts_env']['servers'][keywrap_index] = server_data
                keywrap_index = keywrap_index + 1
                continue
            #     0-15:Unit0
            sec_group_match = sec_group_capture.match(line)
            if sec_group_match:
                groups = sec_group_match.groupdict()
                sec_group = groups['sec_group']
                sec_group_name = groups['sec_group_name']
                sec_groups_data = {'sec_group': sec_group, 'sec_group_name': sec_group_name}
                if not cts_env_dict['cts_env'].get('security_groups', {}):
                    cts_env_dict['cts_env']['security_groups'] = {}
                if not cts_env_dict['cts_env']['security_groups'].get(sec_group_index, {}):
                    cts_env_dict['cts_env']['security_groups'][sec_group_index] = sec_groups_data
                sec_group_index = sec_group_index + 1
                continue
            # Environment Data Lifetime = 86400 secs
            env_data_match = env_data_capture.match(line)
            if env_data_match:
                groups = env_data_match.groupdict()
                if groups.get('env_empty', {}):
                    env_data = groups['env_empty']
                    cts_env_dict['cts_env']['env_data'] = env_data
                else:
                    env_data_lifetime_secs = groups['env_data_lifetime_secs']
                    cts_env_dict['cts_env']['env_data_lifetime_secs'] = int(env_data_lifetime_secs)
                continue
            # Last update time = 20:04:42 PDT Tue Jul 21 2020
            last_update_match = last_update_capture.match(line)
            if last_update_match:
                groups = last_update_match.groupdict()
                time = groups['time']
                time_zone = groups['time_zone']
                day = groups['day']
                month = groups['month']
                date = groups['date']
                year = groups['year']
                full_date = "{0}, {1}/{2}/{3}".format(day, month, date, year)
                cts_env_dict['cts_env'].update(
                    {'last_update': {'date': full_date, 'time': time, 'time_zone': time_zone}})
                continue
            # Env-data expires in   0:00:46:51 (dd:hr:mm:sec)
            expiration_match = expiration_capture.match(line)
            if expiration_match:
                groups = expiration_match.groupdict()
                expiration = groups['expiration']
                cts_env_dict['cts_env']['expiration'] = expiration
                continue
            # Env-data refreshes in 0:00:46:51 (dd:hr:mm:sec)
            refresh_match = refresh_capture.match(line)
            if refresh_match:
                groups = refresh_match.groupdict()
                refresh = groups['refresh']
                cts_env_dict['cts_env']['refresh'] = refresh
                continue
            # Cache data applied           = NONE
            cache_data_match = cache_data_capture.match(line)
            if cache_data_match:
                groups = cache_data_match.groupdict()
                cache_data_status = groups['cache_data_status']
                cts_env_dict['cts_env']['cache_data_status'] = cache_data_status
                continue
            # State Machine is running
            state_machine_match = state_machine_capture.match(line)
            if state_machine_match:
                groups = state_machine_match.groupdict()
                state_machine_status = groups['state_machine_status']
                cts_env_dict['cts_env']['state_machine_status'] = state_machine_status
                continue
            # Retry_timer (60 secs) is not running
            retry_match = retry_capture.match(line)
            if retry_match:
                groups = retry_match.groupdict()
                retry_timer_secs = int(groups['retry_timer_secs'])
                retry_timer_status = groups['retry_timer_status']
                cts_env_dict['cts_env']['state_machine_status'] = state_machine_status
                cts_env_dict['cts_env']['retry_timer_status'] = retry_timer_status
                continue

        return cts_env_dict

# ======================
# Schema for:
#  * 'show cts rbacl'
# ======================
class ShowCtsRbaclSchema(MetaParser):
    """Schema for show cts rbacl."""

    schema = {
        "cts_rbacl": {
            "ip_ver_support": str,
            "name": {
                str: {
                    "ip_protocol_version": str,
                    "refcnt": int,
                    "flag": str,
                    "stale": bool,
                    "aces": {
                        Optional(int): {
                            Optional("action"): str,
                            Optional("protocol"): str,
                            Optional("direction"): str,
                            Optional("port"): int
                        }
                    }
                }
            }
        }
    }


# ======================
# Parser for:
#  * 'show cts rbacl'
# ======================
class ShowCtsRbacl(ShowCtsRbaclSchema):
    """Parser for show cts rbacl"""

    cli_command = 'show cts rbacl'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        cts_rbacl_dict = {}
        # CTS RBACL Policy
        # ================
        # RBACL IP Version Supported: IPv4 & IPv6
        #   name   = TCP_51005-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 51005
        #
        #   name   = TCP_51060-02
        #   IP protocol version = IPV4
        #   refcnt = 4
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 51060
        #
        #   name   = TCP_51144-01
        #   IP protocol version = IPV4
        #   refcnt = 10
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 51144
        #
        #   name   = TCP_51009-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 51009



        # RBACL IP Version Supported: IPv4 & IPv6
        ip_ver_capture = re.compile(r"^RBACL\s+IP\s+Version\s+Supported:\s(?P<ip_ver_support>.*$)")
        #   name   = TCP_13131-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        rbacl_capture = re.compile(r"^(?P<rbacl_key>.*)(?==)=\s+(?P<rbacl_value>.*$)")
        #     permit tcp dst eq 13131
        rbacl_ace_capture = re.compile(
            r"^(?P<action>(permit|deny))\s+(?P<protocol>\S+)(\s+(?P<direction>dst|src)\s+((?P<port_condition>)\S+)\s+(?P<port>\d+)|)")

        remove_lines = ('CTS RBACL Policy', '================', 'RBACL ACEs:')

                # Remove unwanted lines from raw text
        def filter_lines(raw_output, remove_lines):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            rendered_lines = []
            for clean_line in clean_lines:
                clean_line_strip = clean_line.strip()
                if not clean_line_strip.startswith(remove_lines):
                    rendered_lines.append(clean_line_strip)
            return rendered_lines

        out = filter_lines(raw_output=out, remove_lines=remove_lines)
        rbacl_name = ''
        rbacl_ace_index = 1
        for line in out:
            # RBACL IP Version Supported: IPv4 & IPv6
            ip_ver_match = ip_ver_capture.match(line)
            if ip_ver_match:
                groups = ip_ver_match.groupdict()
                ip_ver_support = groups['ip_ver_support']
                if not cts_rbacl_dict.get('cts_rbacl', {}):
                    cts_rbacl_dict['cts_rbacl'] = {}
                    cts_rbacl_dict['cts_rbacl']['name'] = {}
                cts_rbacl_dict['cts_rbacl']['ip_ver_support'] = ip_ver_support
                continue
            #   name   = TCP_13131-01
            #   IP protocol version = IPV4
            #   refcnt = 2
            #   flag   = 0x41000000
            #   stale  = FALSE
            elif rbacl_capture.match(line):
                groups = rbacl_capture.match(line).groupdict()
                rbacl_key = groups['rbacl_key'].strip().lower().replace(' ', '_')
                rbacl_value = groups['rbacl_value']
                if rbacl_value.isdigit():
                    rbacl_value = int(rbacl_value)
                if rbacl_value == "TRUE" or rbacl_value == "FALSE":
                    if rbacl_value == "TRUE":
                        rbacl_value = True
                    else:
                        rbacl_value = False
                if not cts_rbacl_dict.get('cts_rbacl', {}):
                    cts_rbacl_dict['cts_rbacl'] = {}
                if rbacl_key == 'name':
                    rbacl_name = rbacl_value
                    cts_rbacl_dict['cts_rbacl']['name'][rbacl_name] = {}
                    rbacl_ace_index = 1
                else:
                    cts_rbacl_dict['cts_rbacl']['name'][rbacl_name].update({rbacl_key: rbacl_value})
                continue
            #     permit tcp dst eq 13131
            elif rbacl_ace_capture.match(line):
                groups = rbacl_ace_capture.match(line).groupdict()
                ace_group_dict = {}
                cts_rbacl_dict['cts_rbacl']['name'][rbacl_name]['aces'] = {}
                if groups['action']:
                    ace_group_dict.update({'action': groups['action']})
                if groups['protocol']:
                    ace_group_dict.update({'protocol': groups['protocol']})
                if groups['direction']:
                    ace_group_dict.update({'direction': groups['direction']})
                if groups['port_condition']:
                    ace_group_dict.update({'port_condition': groups['port_condition']})
                if groups['port']:
                    ace_group_dict.update({'port': int(groups['port'])})
                if not cts_rbacl_dict['cts_rbacl']['name'][rbacl_name]['aces'].get(rbacl_ace_index, {}):
                    cts_rbacl_dict['cts_rbacl']['name'][rbacl_name]['aces'][rbacl_ace_index] = ace_group_dict
                rbacl_ace_index = rbacl_ace_index + 1
                continue
        return cts_rbacl_dict


# ====================================
# Schema for:
#  * 'show cts role-based permissions'
# ====================================
class ShowCtsRoleBasedPermissionsSchema(MetaParser):
    """Schema for show cts role-based permissions."""

    schema = {
        "indexes": {
            int: {
                Optional("policy_name"): str,
                "action_policy": str,
                "action_policy_group": str,
                Optional("src_grp_id"): int,
                Optional("src_grp_name"): str,
                Optional("unknown_group"): str,
                Optional("dst_group_id"): int,
                Optional("dst_group_name"): str,
                Optional("policy_groups"): list
            },
            "monitor_dynamic": bool,
            "monitor_configured": bool
        }
    }



# ====================================
# Parser for:
#  * 'show cts role-based permissions'
# ====================================
class ShowCtsRoleBasedPermissions(ShowCtsRoleBasedPermissionsSchema):
    """Parser for show cts role-based permissions"""

    cli_command = 'show cts role-based permissions'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        cts_rb_permissions_dict = {}

        # IPv4 Role-based permissions default:
        rb_default_capture = re.compile(r"^IPv4\s+Role-based\s+permissions\s+(?P<default_group>default)")
        # IPv4 Role-based permissions from group 42:Untrusted to group Unknown:
        rb_permissions_capture = re.compile(
            r"^IPv4\s+Role-based\s+permissions\s+from\s+group\s+(?P<src_grp_id>\d+):(?P<src_grp_name>\S+)\s+to\s+group\s((?P<unknown_group>Unknown)|(?P<dst_group_id>\d+):(?P<dst_group_name>\S+)):")
        #         Deny IP-00
        policy_action_capture = re.compile(r"^(?P<action_policy>(Permit|Deny))\s+(?P<action_policy_group>\S+)")
        # ACCESS-01
        policy_group_capture = re.compile(r"^(?P<policy_group>\w+-\d+)")
        # RBACL Monitor All for Dynamic Policies : FALSE
        monitor_dynamic_capture = re.compile(
            r"^RBACL\s+Monitor\s+All\s+for\s+Dynamic\s+Policies\s+:\s+(?P<monitor_dynamic>(TRUE|FALSE))")
        #RBACL Monitor All for Configured Policies : FALSE
        monitor_configured_capture = re.compile(
            r"^RBACL\s+Monitor\s+All\s+for\s+Configured\s+Policies\s+:\s+(?P<monitor_configured>(TRUE|FALSE))")

        # Remove unwanted lines from raw text
        def filter_lines(raw_output):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            rendered_lines = []
            for clean_line in clean_lines:
                clean_line_strip = clean_line.strip()
                rendered_lines.append(clean_line_strip)
            return rendered_lines

        out = filter_lines(raw_output=out)

        # Index value for each policy which will increment as it matches a new policy
        policy_index = 1
        # Index value for each policy group which will increment as it matches a new policy group
        policy_group_index = 1
        # Used to populate data for each policy and the policy index will be used as the key.
        policy_data = {}

        for line in out:
            # IPv4 Role-based permissions default:
            if rb_default_capture.match(line):
                policy_group_index = 1
                rb_default_match = rb_default_capture.match(line)
                groups = rb_default_match.groupdict()
                default_group = groups['default_group']
                policy_data = {'policy_name': default_group}
                if not cts_rb_permissions_dict.get('indexes', {}):
                    cts_rb_permissions_dict['indexes'] = {}
                continue
            # IPv4 Role-based permissions from group 42:Untrusted to group Unknown:
            elif rb_permissions_capture.match(line):
                policy_group_index = 1
                rb_permissions_match = rb_permissions_capture.match(line)
                groups = rb_permissions_match.groupdict()
                policy_data = {}
                if not cts_rb_permissions_dict.get('indexes', {}):
                    cts_rb_permissions_dict['indexes'] = {}
                for k, v in groups.items():
                    if v:
                        if v.isdigit():
                            v = int(v)
                        policy_data.update({k: v})
                continue
            # ACCESS-01
            elif policy_group_capture.match(line):
                policy_group_match = policy_group_capture.match(line)
                groups = policy_group_match.groupdict()
                policy_group = groups['policy_group']
                if not policy_data.get('policy_groups', []):
                    policy_data['policy_groups'] = []
                policy_data['policy_groups'].append(policy_group)
                continue
            #         Deny IP-00
            elif policy_action_capture.match(line):
                policy_action_match = policy_action_capture.match(line)
                groups = policy_action_match.groupdict()
                action_policy = groups['action_policy']
                action_policy_group = groups['action_policy_group']
                for k, v in groups.items():
                    policy_data.update({k: v})
                cts_rb_permissions_dict['indexes'][policy_index] = policy_data
                policy_index = policy_index + 1
                continue
            # RBACL Monitor All for Dynamic Policies : FALSE
            elif monitor_dynamic_capture.match(line):
                monitor_dynamic_match = monitor_dynamic_capture.match(line)
                groups = monitor_dynamic_match.groupdict()
                monitor_dynamic = groups['monitor_dynamic']
                if monitor_dynamic == 'FALSE':
                    monitor_dynamic = False
                else:
                    monitor_dynamic = True
                cts_rb_permissions_dict['indexes']['monitor_dynamic'] = monitor_dynamic
                continue
            # RBACL Monitor All for Configured Policies : FALSE
            elif monitor_configured_capture.match(line):
                monitor_configured_match = monitor_configured_capture.match(line)
                groups = monitor_configured_match.groupdict()
                monitor_configured = groups['monitor_configured']
                if monitor_configured == 'FALSE':
                    monitor_configured = False
                else:
                    monitor_configured = True
                cts_rb_permissions_dict['indexes']['monitor_configured'] = monitor_configured
                continue

        return cts_rb_permissions_dict



# =====================================
# Schema for:
#  * 'show cts wireless profile policy {policy} '
# =====================================
class ShowCtsWirelessProfilePolicySchema(MetaParser):
    """Schema for show cts wireless profile policy {policy}."""

    schema = {
        "policy_name": {
            str: {
                "role_based_enforcement": str,
                "inline_tagging": str,
                "default_sgt": str
            }
        }
    }


# =====================================
# Parser for:
#  * 'show cts wireless profile policy {policy}'
# =====================================
class ShowCtsWirelessProfilePolicy(ShowCtsWirelessProfilePolicySchema):
    """Parser for show cts wireless profile policy {policy} """

    cli_command = 'show cts wireless profile policy {policy}'

    def cli(self, policy, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(policy=policy))
        else:
            output = output


        # Policy Profile Name         		: xyz-policy
        # CTS
        #   Role-based enforcement         : ENABLED
        #   Inline-tagging                 : ENABLED
        #   	Default SGT		 : 100
        #
        # Policy Profile Name          		: foo2
        # CTS
        #   Role-based enforcement         : DISABLED
        #   Inline-tagging                 : ENABLED
        #   Default SGT		         : NOT-DEFINED
        #
        # Policy Profile Name           	        : foo3
        # CTS
        #   Role-based enforcement         : DISABLED
        #   Inline-tagging                 : DISABLED
        #   Default SGT			 : 65001


        # Policy Profile Name         		: xyz-policy
        p_profile_name = re.compile(r"^Policy\s+Profile\s+Name\s+:\s+(?P<value>\S+)$")

        # CTS
        p_cts_section = re.compile(r"^CTS$")

        # Role-based enforcement         : ENABLED
        p_role_based = re.compile(r"^Role-based\s+enforcement\s+:\s+(?P<value>\S+)$")

        # Inline-tagging                 : DISABLED
        p_inline = re.compile(r"^Inline-tagging\s+:\s+(?P<value>\S+)$")

        # Default SGT		         : NOT-DEFINED
        p_sgt = re.compile(r"^Default\s+SGT\s+:\s+(?P<value>\S+)$")



        cts_ap_dict = {}
        current_policy = ""

        for line in output.splitlines():
            line = line.strip()
            m_profile_name = p_profile_name.match(line)
            if m_profile_name:
                # Policy Profile Name         		: xyz-policy
                current_policy = m_profile_name.group("value")
                cts_ap_dict.setdefault("policy_name", {} ).update({ current_policy: {} })
                continue
            m_cts_section = p_cts_section.match(line)
            if m_cts_section:
                # CTS
                continue
            m_role_based = p_role_based.match(line)
            if m_role_based:
                # Role-based enforcement         : ENABLED
                cts_ap_dict["policy_name"][current_policy].update({ "role_based_enforcement": m_role_based.group("value") })
                continue
            m_inline = p_inline.match(line)
            if m_inline:
                # Inline-tagging                 : DISABLED
                cts_ap_dict["policy_name"][current_policy].update({ "inline_tagging": m_inline.group("value") })
                continue
            m_sgt = p_sgt.match(line)
            if m_sgt:
                # Default SGT		         : NOT-DEFINED
                cts_ap_dict["policy_name"][current_policy].update({ "default_sgt": m_sgt.group("value") })
                continue

        return cts_ap_dict


# =========================
# Schema for:
#  * 'show cts ap sgt info {ap_name}'
# =========================
class ShowCtsApSgtInfoSchema(MetaParser):
    """Schema for show cts ap sgt info {ap_name}."""

    schema = {
        "ap": {
            Any(): {
                "number_of_sgts_referred_by_the_ap": int,
                Optional("sgts") : {
                    Optional(str) : {
                        Optional("policy_pushed_to_ap"): str,
                        Optional("no_of_clients"): int
                    }
                }
            }
        }
    }


# =========================
# Parser for:
#  * 'show cts ap sgt info {ap_name}'
# =========================
class ShowCtsApSgtInfo(ShowCtsApSgtInfoSchema):
    """Parser for show cts ap sgt info {ap_name}"""

    cli_command = 'show cts ap sgt info {ap_name}'

    def cli(self, ap_name="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(ap_name=ap_name))


        # Number of SGTs referred by the AP...............: 2
        #
        # SGT               PolicyPushedToAP       No.of Clients
        # ------------------------------------------------------------
        # UNKNOWN(0)        NO                     0
        # DEFAULT(65535)    NO                     0

        # Number of SGTs referred by the AP...............: 0
        p_number_sgts = re.compile(r"^Number\s+of\s+SGTs\s+referred\s+by\s+the\s+AP\.+:\s+(?P<value>\d+)$")

        # SGT               PolicyPushedToAP       No.of Clients
        p_sgt_header = re.compile(r"^SGT\s+PolicyPushedToAP\s+No.of\s+Clients$")

        # ------------------------------------------------------------
        p_sgt_delimiter = re.compile(r"^-+$")

        # 10                NO                     1
        p_sgt_row = re.compile(r"^(?P<sgt>\S+)\s+(?P<policy>\S+)\s+(?P<clients>\d+)$")

        cts_ap_dict = {}

        for line in output.splitlines():
            line = line.strip()
            m_number_sgts = p_number_sgts.match(line)
            if m_number_sgts:
                cts_ap_dict.setdefault("ap", {} ).setdefault(ap_name, {})
                cts_ap_dict["ap"][ap_name].update({ "number_of_sgts_referred_by_the_ap": int(m_number_sgts.group("value")) })
                continue
            m_sgt_header = p_sgt_header.match(line)
            if m_sgt_header:
                continue
            m_sgt_delimiter = p_sgt_delimiter.match(line)
            if m_sgt_delimiter:
                continue
            m_sgt_row = p_sgt_row.match(line)
            if m_sgt_row:
                group = m_sgt_row.groupdict()
                sgts_dict = cts_ap_dict["ap"][ap_name].setdefault("sgts", {})
                sgts_dict.update(
                            {
                                group["sgt"]: {
                                    "policy_pushed_to_ap": group["policy"],
                                    "no_of_clients": int(group["clients"])
                                }
                            }
                        )
                continue


        return cts_ap_dict


# =========================
# Schema for:
#  * 'show cts interface'
# =========================
class ShowCtsInterfaceSchema(MetaParser):
    """Schema for show cts interface'"""

    schema = {
        'global_dot1x_feature': str,
        'interfaces': {
            Any(): {
                'cts': {
                    'cts_status': str,
                    Optional('mode'): str
                },
                Optional('ifc_state'): str,
                Optional('intf_active_for'): str,
                Optional('authentication'): {
                    'status': str,
                    Optional('peer_identity'): str,
                    Optional('peer_advertised_capabilities'): str
                },
                Optional('authorization'): {
                    'status': str,
                    Optional('peer_sgt'): int,
                    Optional('peer_sgt_assignment'): str
                },
                Optional('sap_status'): str,
                Optional('propagate_sgt'): str,
                Optional('cache_info'): {
                    'expiration': str,
                    'cache_applied_to_link': str
                },
                Optional('statistics'): {
                    'authc_success': int,
                    'authc_reject': int,
                    'authc_failure': int,
                    'authc_no_response': int,
                    'authc_logoff': int,
                    'sap_success': int,
                    'sap_fail': int,
                    'authz_success': int,
                    'authz_fail': int,
                    'port_auth_fail': int
                },
                'l3_ipm': str
            },
        }
    }


# =========================
# Parser for:
#  * 'show cts interface'
# =========================
class ShowCtsInterface(ShowCtsInterfaceSchema):
    """Parser for show cts interface"""

    cli_command = 'show cts interface'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Global Dot1x feature is Disabled
        p1 = re.compile(r'^Global Dot1x feature is\s+(?P<global_dot1x_feature>\w+)')

        # TenGigabitEthernet1/0/6:
        p2 = re.compile(r'^Interface\s+(?P<interface>\S+\d+\/\d+\/\d+):')

        # CTS_status : enabled,mode: MANUAL
        p3 = re.compile(r'^CTS\s+is\s+(?P<cts_status>\S+),\s+mode:\s+(?P<mode>\S+)')

        # IFC state: OPEN
        p4 = re.compile(r'^IFC state:\s+(?P<ifc_state>\S+)')

        # Intf_active_for: 00:29:30.798
        p5 = re.compile(r'^Interface Active for\s+(?P<intf_active_for>\d+:\d+:\d+.\d+)')

        # Authentication Status:   NOT APPLICABLE
        p6 = re.compile(r'^Authentication Status:\s+(?P<status>\w+(?:\s+)?\w+)$')

        # Peer_identity:       "unknown"
        p7 = re.compile(r'^Peer identity:\s+\W(?P<peer_identity>(?:\w+)?)\W')

        # Peer's advertised capabilities: ""
        p8 = re.compile(r"^Peer's advertised capabilities:\s+\W(?P<peer_advertised_capabilities>(?:\w+)?)\W")

        # Authorization Status:    SUCCEEDED
        p9 = re.compile(r'^Authorization Status:\s+(?P<status>\w+(?:\s+)?\w+)$')

        # Peer_SGT:            2000
        p10 = re.compile(r'^Peer SGT:\s+(?P<peer_sgt>\d+)')

        # Peer SGT assignment: Trusted
        p11 = re.compile(r'^Peer SGT assignment:\s+(?P<peer_sgt_assignment>\w+)')

        # SAP Status:              NOT APPLICABLE
        p12 = re.compile(r'^SAP Status:\s+(?P<sap_status>\w+(?:\s+)?\w+)$')

        # Propagate_SGT: Enabled
        p13 = re.compile(r'^Propagate SGT:\s+(?P<propagate_sgt>\S+)')

        # Expiration            : N/A
        p14 = re.compile(r'^Expiration\s+:\s+(?P<expiration>\S+)')

        # Cache applied to link : NONE
        p15 = re.compile(r'Cache applied to link\s+:\s+(?P<cache_applied_to_link>\S+)')

        # authc success:              0
        p16 = re.compile(r'^authc success:\s+(?P<authc_success>\d+)')

        # authc reject:               0
        p17 = re.compile(r'^authc reject:\s+(?P<authc_reject>\d+)')

        # authc failure:              0
        p18 = re.compile(r'^authc failure:\s+(?P<authc_failure>\d+)')

        # authc no response:          0
        p19 = re.compile(r'^authc no response:\s+(?P<authc_no_response>\d+)')

        # authc logoff:               0
        p20 = re.compile(r'^authc logoff:\s+(?P<authc_logoff>\d+)')

        # sap success:                0
        p21 = re.compile(r'^sap success:\s+(?P<sap_success>\d+)')

        # sap fail:                   0
        p22 = re.compile(r'^sap fail:\s+(?P<sap_fail>\d+)')

        # authz success:              0
        p23 = re.compile(r'^authz success:\s+(?P<authz_success>\d+)')

        # authz fail:                 0
        p24 = re.compile(r'^authz fail:\s+(?P<authz_fail>\d+)')

        # port auth fail:             0
        p25 = re.compile(r'^port auth fail:\s+(?P<port_auth_fail>\d+)')

        # L3_IPM:   disabled.
        p26 = re.compile(r'^L3 IPM:\s+(?P<l3_ipm>\S+).')

        for line in out.splitlines():
            line = line.strip()

            # Global Dot1x feature is Disabled
            m = p1.match(line)
            if m:
                group = m.groupdict()
                global_dot1x_feature = group['global_dot1x_feature']
                ret_dict['global_dot1x_feature'] = global_dot1x_feature

            # TenGigabitEthernet1/0/6:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(interface, {})

            # CTS_status : enabled,mode: MANUAL
            m = p3.match(line)
            if m:
                group = m.groupdict()
                cts_status = group['cts_status']
                mode = group['mode']
                cts_dict = intf_dict.setdefault('cts', {})
                cts_dict['cts_status'] = cts_status
                cts_dict['mode'] = mode

            # IFC state: OPEN
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ifc_state = group['ifc_state']
                intf_dict['ifc_state'] = ifc_state

            # Intf_active_for: 00:29:30.798
            m = p5.match(line)
            if m:
                group = m.groupdict()
                intf_active_for = group['intf_active_for']
                intf_dict['intf_active_for'] = intf_active_for

            # Authentication Status:   NOT APPLICABLE
            m = p6.match(line)
            if m:
                group = m.groupdict()
                status = group['status']
                auth_dict = intf_dict.setdefault('authentication', {})
                auth_dict['status'] = status

            # Peer_identity:       "unknown"
            m = p7.match(line)
            if m:
                group = m.groupdict()
                peer_identity = group['peer_identity']
                auth_dict['peer_identity'] = str(peer_identity)

            # Peer's advertised capabilities: ""
            m = p8.match(line)
            if m:
                group = m.groupdict()
                peer_advertised_capabilities = group['peer_advertised_capabilities']
                auth_dict['peer_advertised_capabilities'] = str(peer_advertised_capabilities)

            # Authorization Status:    SUCCEEDED
            m = p9.match(line)
            if m:
                group = m.groupdict()
                status = group['status']
                authr_dict = intf_dict.setdefault('authorization', {})
                authr_dict['status'] = status

            # Peer_SGT:            2000
            m = p10.match(line)
            if m:
                group = m.groupdict()
                peer_sgt = int(group['peer_sgt'])
                authr_dict['peer_sgt'] = peer_sgt

            # Peer SGT assignment: Trusted
            m = p11.match(line)
            if m:
                group = m.groupdict()
                peer_sgt_assignment = group['peer_sgt_assignment']
                authr_dict['peer_sgt_assignment'] = peer_sgt_assignment

            # SAP Status:              NOT APPLICABLE
            m = p12.match(line)
            if m:
                group = m.groupdict()
                sap_status = group['sap_status']
                intf_dict['sap_status'] = sap_status

            # Propagate_SGT: Enabled
            m = p13.match(line)
            if m:
                group = m.groupdict()
                propagate_sgt = group['propagate_sgt']
                intf_dict['propagate_sgt'] = propagate_sgt

            # Expiration            : N/A
            m = p14.match(line)
            if m:
                group = m.groupdict()
                expiration = group['expiration']
                cache_dict = intf_dict.setdefault('cache_info', {})
                cache_dict['expiration'] = expiration

            # Cache applied to link : NONE
            m = p15.match(line)
            if m:
                group = m.groupdict()
                cache_applied_to_link = group['cache_applied_to_link']
                cache_dict['cache_applied_to_link'] = cache_applied_to_link

            # authc success:              0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                stat_dict = intf_dict.setdefault('statistics', {})
                stat_dict['authc_success'] = int(group['authc_success'])

            # authc reject:               0
            m = p17.match(line)
            if m:
                group = m.groupdict()
                stat_dict['authc_reject'] = int(group['authc_reject'])

            # authc failure:              0
            m = p18.match(line)
            if m:
                group = m.groupdict()
                stat_dict['authc_failure'] = int(group['authc_failure'])

            # authc no response:          0
            m = p19.match(line)
            if m:
                group = m.groupdict()
                stat_dict['authc_no_response'] = int(group['authc_no_response'])

            # authc logoff:               0
            m = p20.match(line)
            if m:
                group = m.groupdict()
                stat_dict['authc_logoff'] = int(group['authc_logoff'])

            # sap success:                0
            m = p21.match(line)
            if m:
                group = m.groupdict()
                stat_dict['sap_success'] = int(group['sap_success'])

            # sap fail:                   0
            m = p22.match(line)
            if m:
                group = m.groupdict()
                stat_dict['sap_fail'] = int(group['sap_fail'])

            # authz success:              0
            m = p23.match(line)
            if m:
                group = m.groupdict()
                stat_dict['authz_success'] = int(group['authz_success'])

            # authz fail:                 0
            m = p24.match(line)
            if m:
                group = m.groupdict()
                stat_dict['authz_fail'] = int(group['authz_fail'])

            # port auth fail:             0
            m = p25.match(line)
            if m:
                group = m.groupdict()
                stat_dict['port_auth_fail'] = int(group['port_auth_fail'])

            # L3_IPM:   disabled.
            m = p26.match(line)
            if m:
                group = m.groupdict()
                l3_ipm = group['l3_ipm']
                intf_dict['l3_ipm'] = l3_ipm

        return ret_dict

class ShowCtsRolebasedSgtMapIpSchema(MetaParser):

    ''' Schema for "show cts role-based sgt-map {ip}" '''

    schema = {
        Any(): {
            'ip': str,
            'sgt': str,
            'source': str,
        }
    }

class ShowCtsRolebasedSgtMapIp(ShowCtsRolebasedSgtMapIpSchema):
    """Schema for show cts role-based sgt-map {ip}"""

    cli_command = ['show cts role-based sgt-map {ip}',
                   'show cts role-based sgt-map vrf {vrf} {ip}']
    def cli(self, ip, vrf = None, output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf, ip=ip)
            else:
                cmd = self.cli_command[0].format(ip=ip)
            output = self.device.execute(cmd)
        return oper_fill_tabular(
            header_fields=['IP Address', 'SGT', 'Source'],
            label_fields= ['ip', 'sgt', 'source'],
            device_output=output,
            device_os='iosxe',
            index=[0]
        ).entries


class ShowCtsRoleBasedSgtMapAllSchema(MetaParser):
    """
        Schema for :
            show cts role-based sgt-map all
            show cts role-based sgt-map all vrf <vrf> all
    """
    schema = {
        Optional('ipv4_sgt_bindings'): {
            Any(): {
                'ip_address': str,
                'sgt': int,
                'source': str
            },
            Optional('total_active'): int,
            Optional('total_cli'): int,
            Optional('total_sxp'): int,
            Optional('total_internal'): int,
            Optional('total_local'): int
        },
        Optional('ipv6_sgt_bindings'): {
            Any(): {
                'ip_address': str,
                'sgt': int,
                'source': str
            },
            Optional('total_active'): int,
            Optional('total_cli'): int,
            Optional('total_sxp'): int,
            Optional('total_internal'): int,
            Optional('total_local'): int
        }
    }


class ShowCtsRoleBasedSgtMapAll(ShowCtsRoleBasedSgtMapAllSchema):
    """
        Parser for :
            show cts role-based sgt-map all
            show cts role-based sgt-map all vrf <vrf> all
    """

    cli_command = ['show cts role-based sgt-map all', 'show cts role-based sgt-map vrf {vrf} all']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # initial return dictionary
        result_dict = {}

        # Active IPv4-SGT Bindings Information
        # Active IPv6-SGT Bindings Information
        p0 = re.compile(r'^Active\s+(?P<sgt_type>([\w\-\s]+))\s+Information$')

        # 1.1.1.2 2 SXP
        # 1.1.1.3 3 SXP
        p1 = re.compile(r'^(?P<ip_address>(\S+))\s+(?P<sgt>(\d+))\s+(?P<source>(\w+))$')

        # Total number of SXP bindings = 51
        # Total number of active bindings = 51
        # Total number of SXP bindings = 2
        # Total number of active bindings = 2
        p2 = re.compile(r'^Total\s+number\s+of\s+(?P<binding_type>(\S+))\s+bindings\s+=\s+(?P<binding_count>(\d+))$')

        for line in output.splitlines():
            line = line.strip()

            # skip empty lines
            if not line:
                continue

            # Active IPv4-SGT Bindings Information
            # Active IPv6-SGT Bindings Information
            m0 = p0.match(line)
            if m0:
                group = m0.groupdict()
                group = group['sgt_type'].lower().replace('-', '_').replace(' ', '_')
                sgt_dict = result_dict.setdefault(group, {})
                continue

            # 1.1.1.2 2 SXP
            # 1.1.1.3 3 SXP
            m1 = p1.match(line)
            if m1:
                sgt_ip_group = m1.groupdict()
                sgt_ip_group['ip_address'] = sgt_ip_group['ip_address'].lower()
                sgt_ip_group['source'] = sgt_ip_group['source'].lower()
                sgt_ip_group['sgt'] = int(sgt_ip_group['sgt'])
                sgt_dict[sgt_ip_group['ip_address']] = sgt_ip_group
                continue

            # Total number of SXP bindings = 51
            # Total number of active bindings = 51
            # Total number of SXP bindings = 2
            # Total number of active bindings = 2
            m2 = p2.match(line)
            if m2:
                total_sgt_group = m2.groupdict()
                sgt_dict[f"total_{total_sgt_group['binding_type'].lower()}"] = \
                    int(total_sgt_group['binding_count'])

        return result_dict


class ShowCtsSxpConnectionsSchema(MetaParser):
    """
        Schema for:
            show cts sxp connections
            show cts sxp connections vrf <vrf>
    """
    schema = {
        Optional('total_sxp_connections'): int,
        'default_key_chain': str,
        'default_key_chain_name': str,
        'default_pwd': str,
        'default_source_ip': str,
        'export_traverse_limit': str,
        'highest_version': int,
        'import_traverse_limit': str,
        'reconcile_period': int,
        'retry_period': int,
        'retry_timer': str,
        'sxp_status': str,
        Any(): {
            Optional('conn_capability'): str,
            Optional('conn_hold_time'): int,
            Optional('speaker_conn_hold_time'): int,
            Optional('listener_conn_hold_time'): int,
            'conn_inst': int,
            'conn_status': str,
            'conn_version': int,
            'duration': str,
            'local_mode': str,
            'peer_ip': str,
            'source_ip': str,
            'tcp_conn_fd': str,
            'tcp_conn_pwd': str
        }
    }

class ShowCtsSxpConnections(ShowCtsSxpConnectionsSchema):
    """
        Parser for:
            show cts sxp connections
            show cts sxp connections vrf <vrf>
    """

    cli_command = ['show cts sxp connections', 'show cts sxp connections vrf {vrf}']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # initial return dictionary
        result_dict = {}

        #  SXP              : Enabled
        p1 = re.compile(r"^SXP\s+:\s+(?P<sxp_status>(Disabled|Enabled))$")
        #  Highest Version Supported: 4
        p2 = re.compile(r"^Highest\s+Version\s+Supported:\s+(?P<highest_version>\d+)$")
        #  Default Password : Set
        p3 = re.compile(r"^Default\s+Password\s+:\s+(?P<default_pwd>(Not\s+Set|Set))$")
        #  Default Key-Chain: Not Set
        p4 = re.compile(r"^Default\s+Key-Chain:\s+(?P<default_key_chain>(Not\s+Set|Set))$")
        #  Default Key-Chain Name: Not Applicable
        p5 = re.compile(r"^Default\s+Key-Chain\s+Name:\s+(?P<default_key_chain_name>(Not\s+Applicable|\S+))$")
        #  Default Source IP: 192.168.2.24
        p6 = re.compile(r"^Default\s+Source\s+IP:\s+(?P<default_source_ip>(Not\s+Set|[\d+\.]+))$")
        # Connection retry open period: 120 secs
        p7 = re.compile(r"^Connection\s+retry\s+open\s+period:\s+(?P<retry_period>\d+)\s+secs$")
        # Reconcile period: 120 secs
        p8 = re.compile(r"^Reconcile\s+period:\s+(?P<reconcile_period>\d+)\s+secs$")
        # Retry open timer is not running
        p9 = re.compile(r"^Retry\s+open\s+timer\s+is\s+(?P<retry_timer>(not\s+running|running))$")
        # Peer-Sequence traverse limit for export: Not Set
        p10 = re.compile(r"^Peer-Sequence\s+traverse\s+limit\s+for\s+export:\s+(?P<export_traverse_limit>(Not\s+Set|\S+))$")
        # Peer-Sequence traverse limit for import: Not Set
        p11 = re.compile(r"^Peer-Sequence\s+traverse\s+limit\s+for\s+import:\s+(?P<import_traverse_limit>(Not\s+Set|\S+))$")
        # Peer IP          : 10.1.1.2
        p12 = re.compile(r"^Peer\s+IP\s+:\s+(?P<peer_ip>[\d\.]+)$")
        # Source IP        : 10.1.1.1
        p13 = re.compile(r"^Source\s+IP\s+:\s+(?P<source_ip>[\d\.]+)$")
        # Conn status      : On
        p14 = re.compile(r"^Conn\s+status\s+:\s+(?P<conn_status>.*$)$")
        # Conn version     : 5
        p15 = re.compile(r"^Conn\s+version\s+:\s+(?P<conn_version>\d+)$")
        # Conn capability  : IPv4-IPv6-Subnet
        p16 = re.compile(r"^Conn\s+capability\s+:\s+(?P<conn_capability>\S+)$")
        # Conn hold time   : 120 seconds
        p17 = re.compile(r"^Conn\s+hold\s+time\s+:\s+(?P<conn_hold_time>\d+)\s+seconds$")
        # Local mode       : SXP Speaker
        p18 = re.compile(r"^Local\s+mode\s+:\s+(?P<local_mode>.*$)$")
        # Connection inst# : 1
        p19 = re.compile(r"^Connection\s+inst#\s+:\s+(?P<conn_inst>\d+)$")
        # TCP conn fd      : 1
        p20 = re.compile(r"^TCP\s+conn\s+fd\s+:\s+(?P<tcp_conn_fd>.*$)$")
        # TCP conn password: none
        p21 = re.compile(r"^TCP\s+conn\s+password:\s+(?P<tcp_conn_pwd>.*$)$")
        # Duration since last state change: 0:00:02:09 (dd:hr:mm:sec)
        p22 = re.compile(r"^Duration\s+since\s+last\s+state\s+change:\s+(?P<duration>.*)$")
        # Total num of SXP Connections = 2
        p23 = re.compile(r"^Total\s+num\s+of\s+SXP\s+Connections\s+=\s+(?P<total_sxp_connections>\d+)$")
        # Speaker Conn hold time   : 120 seconds
        p24 = re.compile(r"^Speaker\s+Conn\s+hold\s+time\s+:\s+(?P<speaker_conn_hold_time>\d+)\s+seconds$")
        # Listener Conn hold time   : 120 seconds
        p25 = re.compile(r"^Listener\s+Conn\s+hold\s+time\s+:\s+(?P<listener_conn_hold_time>\d+)\s+seconds$")

        for line in output.splitlines():
            line = line.strip()

            # skip empty lines
            if not line:
                continue

            #  SXP              : Enabled
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                result_dict.update(group)
                continue

            #  Highest Version Supported: 4
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                group['highest_version'] = int(group['highest_version'])
                result_dict.update(group)
                continue

            #  Default Password : Set
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                result_dict.update(group)
                continue

            #  Default Key-Chain: Not Set
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                result_dict.update(group)
                continue

            #  Default Key-Chain Name: Not Applicable
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                result_dict.update(group)
                continue

            #  Default Source IP: 192.168.2.24
            m6 = p6.match(line)
            if m6:
                group = m6.groupdict()
                result_dict.update(group)
                continue

            # Connection retry open period: 120 secs
            m7 = p7.match(line)
            if m7:
                group = m7.groupdict()
                group['retry_period'] = int(group['retry_period'])
                result_dict.update(group)
                continue

            # Reconcile period: 120 secs
            m8 = p8.match(line)
            if m8:
                group = m8.groupdict()
                group['reconcile_period'] = int(group['reconcile_period'])
                result_dict.update(group)
                continue

            # Retry open timer is not running
            m9 = p9.match(line)
            if m9:
                group = m9.groupdict()
                result_dict.update(group)
                continue

            # Peer-Sequence traverse limit for export: Not Set
            m10 = p10.match(line)
            if m10:
                group = m10.groupdict()
                result_dict.update(group)
                continue

            # Peer-Sequence traverse limit for import: Not Set
            m11 = p11.match(line)
            if m11:
                group = m11.groupdict()
                result_dict.update(group)
                continue

            # Peer IP          : 10.1.1.2
            m12 = p12.match(line)
            if m12:
                group = m12.groupdict()
                peer_dict = result_dict.setdefault(group['peer_ip'], group)
                continue

            # Source IP        : 10.1.1.1
            m13 = p13.match(line)
            if m13:
                group = m13.groupdict()
                peer_dict.update(group)
                continue

            # Conn status      : On
            # Conn status      : On (Speaker) :: On (Listener)
            m14 = p14.match(line)
            if m14:
                group = m14.groupdict()
                peer_dict.update(group)
                continue

            # Conn version     : 5
            m15 = p15.match(line)
            if m15:
                group = m15.groupdict()
                group['conn_version'] = int(group['conn_version'])
                peer_dict.update(group)
                continue

            # Conn capability  : IPv4-IPv6-Subnet
            m16 = p16.match(line)
            if m16:
                group = m16.groupdict()
                peer_dict.update(group)
                continue

            # Conn hold time   : 120 seconds
            m17 = p17.match(line)
            if m17:
                group = m17.groupdict()
                group['conn_hold_time'] = int(group['conn_hold_time'])
                peer_dict.update(group)
                continue

            # Local mode       : SXP Speaker
            # Local mode       : Both
            m18 = p18.match(line)
            if m18:
                group = m18.groupdict()
                peer_dict.update(group)
                continue

            # Connection inst# : 1
            m19 = p19.match(line)
            if m19:
                group = m19.groupdict()
                group['conn_inst'] = int(group['conn_inst'])
                peer_dict.update(group)
                continue

            # TCP conn fd      : 1
            # TCP conn fd      : 1(Speaker) 2(Listener)
            m20 = p20.match(line)
            if m20:
                group = m20.groupdict()
                group['tcp_conn_fd'] = group['tcp_conn_fd']
                peer_dict.update(group)
                continue

            # TCP conn password: none
            # TCP conn password: default SXP password
            m21 = p21.match(line)
            if m21:
                group = m21.groupdict()
                peer_dict.update(group)
                continue

            # Duration since last state change: 0:00:02:09 (dd:hr:mm:sec)
            m22 = p22.match(line)
            if m22:
                group = m22.groupdict()
                peer_dict.update(group)
                continue

            # Total num of SXP Connections = 2
            m23 = p23.match(line)
            if m23:
                group = m23.groupdict()
                group["total_sxp_connections"] = int(group["total_sxp_connections"])
                result_dict.update(group)
                continue

            # Speaker Conn hold time   : 120 seconds
            m24 = p24.match(line)
            if m24:
                group = m24.groupdict()
                group["speaker_conn_hold_time"] = int(group["speaker_conn_hold_time"])
                peer_dict.update(group)
                continue

            # Listener Conn hold time   : 120 seconds
            m25 = p25.match(line)
            if m25:
                group = m25.groupdict()
                group["listener_conn_hold_time"] = int(group["listener_conn_hold_time"])
                peer_dict.update(group)
                continue

        return result_dict


class ShowCtsSxpSgtMapBriefSchema(MetaParser):
    """
        Schema for:
            show cts sxp sgt-map brief
            show cts sxp sgt-map vrf <vrf> brief
    """
    schema = {
        'ip_sgt_mapping': {
            Optional('ipv4'): {
                Any(): int
            },
            Optional('ipv6'): {
                Any(): int
            },
            Optional('total_ip_sgt_mappings'): int
        }
    }

class ShowCtsSxpSgtMapBrief(ShowCtsSxpSgtMapBriefSchema):
    """
        Parser for:
            show cts sxp sgt-map brief
            show cts sxp sgt-map vrf <vrf> brief
    """

    cli_command = ['show cts sxp sgt-map brief', 'show cts sxp sgt-map vrf {vrf} brief']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # initial return dictionary
        result_dict = {}

        # IPv4,SGT: <10.1.1.8 , 5>
        # IPv4,SGT: <10.1.1.10 , 9>
        # IPv4,SGT: <10.1.1.11 , 89>
        # IPv4,SGT: <10.1.1.18 , 87>
        p0 = re.compile(r'^IPv4,SGT:\s+\<(?P<ip_address>[\d\.]+)\s+,\s+(?P<sgt>\d+)[:\w]*\>$')

        # IPv6,SGT: <2001::6 , 22>
        # IPv6,SGT: <2001::60 , 208>
        # IPv6,SGT: <2001::80 , 26>
        # IPv6,SGT: <2001::89 , 26>
        p1 = re.compile(r'^IPv6,SGT:\s+\<(?P<ip_address>[\w:]+)\s+,\s+(?P<sgt>\d+)[:\w]*\>$')

        # Total number of IP-SGT Mappings: 8
        p2 = re.compile(r'^Total\s+number\s+of\s+IP-SGT\s+Mappings:\s+(?P<total_ip_sgt_mappings>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # skip empty lines
            if not line:
                continue

            map_dict = result_dict.setdefault('ip_sgt_mapping', {})

            # IPv4,SGT: <10.1.1.8 , 5>
            # IPv4,SGT: <10.1.1.10 , 9:SGT_009>
            # IPv4,SGT: <10.1.1.11 , 89:SGT_089>
            # IPv4,SGT: <10.1.1.18 , 87>
            m0 = p0.match(line)
            if m0:
                ipv4_group = m0.groupdict()
                ipv4_group['sgt'] = int(ipv4_group['sgt'])
                v4_dict = map_dict.setdefault('ipv4', {})
                v4_dict[ipv4_group['ip_address']] = ipv4_group['sgt']
                continue

            # IPv6,SGT: <2001::6 , 22:SGT_022>
            # IPv6,SGT: <2001::60 , 208>
            # IPv6,SGT: <2001::80 , 26>
            # IPv6,SGT: <2001::89 , 26>
            m1 = p1.match(line)
            if m1:
                ipv6_group = m1.groupdict()
                ipv6_group['sgt'] = int(ipv6_group['sgt'])
                v6_dict = map_dict.setdefault('ipv6', {})
                v6_dict[ipv6_group['ip_address'].lower()] = ipv6_group['sgt']
                continue

            # Total number of IP-SGT Mappings: 8
            m2 = p2.match(line)
            if m2:
                total_group = m2.groupdict()
                total_group['total_ip_sgt_mappings'] = int(total_group['total_ip_sgt_mappings'])
                map_dict['total_ip_sgt_mappings'] = total_group['total_ip_sgt_mappings']

        return result_dict
