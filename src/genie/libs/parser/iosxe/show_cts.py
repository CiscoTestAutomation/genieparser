import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional

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
