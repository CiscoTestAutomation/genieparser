import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional, Any

# ===================================
# Schema for:
#  * 'show_cts_sxp_connections_brief'
# ===================================
class ShowCtsSxpConnectionsBriefSchema(MetaParser):
    """Schema for show_cts_sxp_connections_brief."""

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
                        if v.isdigit():
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
        "refresh_timer": str
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
                # print(clean_line)
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
                # print(clean_line)
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
                    Optional("idle_time"): str,
                    Optional("deadtime"): str
                }
            }
        },
        Optional("pac_valid_until"): str,
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
            Optional("retry_open_period"): str,
            Optional("reconcile_period"): str,
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
            }
        },
        Optional("cts_role_based_enforcement"): str,
        Optional("cts_role_based_vlan_enforcement"): str,
        Optional("number_trusted_links"): int,
        Optional("number_untrusted_links"): int
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
        r"^auto-test\s+=\s+(?P<test>[^,]+),\s+keywrap-enable\s+=\s+(?P<keywrap>[^,]+),\s+idle-time\s+=\s+(?P<idle>[^,]+),\s+deadtime\s+=\s+(?P<dead>[^,]+)$")

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
        p_sxp_retry = re.compile(r"^Connection\s+retry\s+open\s+period:\s+(?P<time>.*)$")

        # Reconcile period: 120 secs
        p_reconcile = re.compile(r"^Reconcile\s+period:\s+(?P<period>.*)$")

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
                                                                        "idle_time": group["idle"], "deadtime": group["dead"] })
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
                cts_dict.update({ "pac_valid_until": match.group("valid")})
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
                cts_dict["sxp_connections_summary"].update({ "retry_open_period": match.group("time") })
                continue
            # Reconcile period: 120 secs
            elif p_reconcile.match(line):
                match = p_reconcile.match(line)
                cts_dict["sxp_connections_summary"].update({ "reconcile_period": match.group("period") })
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
                cts_dict.update({ "cts_role_based_enforcement": match.group("value") })
                continue
            # CTS Role Based VLAN Enforcement: Enabled
            elif p_role_based_vlan.match(line):
                match = p_role_based_vlan.match(line)
                cts_dict.update({ "cts_role_based_vlan_enforcement": match.group("value") })
                continue
            # Trusted/Un-Trusted Links
            elif p_links_header.match(line):
                continue
            # Number of Trusted interfaces = 0
            elif p_trusted_links.match(line):
                match = p_trusted_links.match(line)
                cts_dict.update({ "number_trusted_links": int(match.group("count")) })
            # Number of Un-Trusted interfaces = 0
            elif p_untrusted_links.match(line):
                match = p_untrusted_links.match(line)
                cts_dict.update({ "number_untrusted_links": int(match.group("count")) })
                continue


        if not active_bindings:
            return cts_dict
        else:
            cts_dict = update_bindings(active_bindings, cts_dict)
            return cts_dict