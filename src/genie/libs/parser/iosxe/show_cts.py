import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional

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
          Optional("env_data_lifetime_secs"): str,
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
                # print(clean_line)
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
                    cts_env_dict['cts_env']['env_data_lifetime_secs'] = env_data_lifetime_secs
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
                full_date = f"{day}, {month}/{date}/{year}"
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
        "rbp_policies": {
            int: {
                Optional("policy_name"): str,
                "action_policy": str,
                "action_policy_group": str,
                Optional("src_grp_id"): int,
                Optional("src_grp_name"): str,
                Optional("unknown_group"): str,
                Optional("dst_group_id"): int,
                Optional("dst_group_name"): str,
                Optional("policy_groups"): {
                    Optional(int): {
                        Optional("policy_group"): str
                    }
                }
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

        remove_lines = ()

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
                if not cts_rb_permissions_dict.get('rbp_policies', {}):
                    cts_rb_permissions_dict['rbp_policies'] = {}
                continue
            # IPv4 Role-based permissions from group 42:Untrusted to group Unknown:
            elif rb_permissions_capture.match(line):
                policy_group_index = 1
                rb_permissions_match = rb_permissions_capture.match(line)
                groups = rb_permissions_match.groupdict()
                policy_data = {}
                if not cts_rb_permissions_dict.get('rbp_policies', {}):
                    cts_rb_permissions_dict['rbp_policies'] = {}
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
                if not policy_data.get('policy_groups', {}):
                    policy_data['policy_groups'] = {}
                if not policy_data['policy_groups'].get(policy_group_index, {}):
                    policy_data['policy_groups'][policy_group_index] = {}
                policy_data['policy_groups'][policy_group_index]['policy_group'] = policy_group
                policy_group_index = policy_group_index + 1
                continue
            #         Deny IP-00
            elif policy_action_capture.match(line):
                policy_action_match = policy_action_capture.match(line)
                groups = policy_action_match.groupdict()
                action_policy = groups['action_policy']
                action_policy_group = groups['action_policy_group']
                for k, v in groups.items():
                    policy_data.update({k: v})
                cts_rb_permissions_dict['rbp_policies'][policy_index] = policy_data
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
                cts_rb_permissions_dict['rbp_policies']['monitor_dynamic'] = monitor_dynamic
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
                cts_rb_permissions_dict['rbp_policies']['monitor_configured'] = monitor_configured
                continue

        return cts_rb_permissions_dict