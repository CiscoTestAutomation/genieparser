import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ===================================
# Schema for:
#  * 'show_cts_sxp_connections_brief'
# ===================================
class Show_Cts_Sxp_Connections_BriefSchema(MetaParser):
    """Schema for show_cts_sxp_connections_brief."""

    schema = {
    "sxp_connections": {
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
            "seq_export": str,
            "seq_import":str
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
#  * 'show_cts_sxp_connections_brief'
# ===================================
class Show_Cts_Sxp_Connections_Brief(Show_Cts_Sxp_Connections_BriefSchema):
    """Parser for show_cts_sxp_connections_brief"""

    cli_command = ['show cts sxp connections brief']

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

        p1 = re.compile(r"\s(?P<sxp_status>(Disabled|Enabled))", re.MULTILINE)
        p2 = re.compile(r"\s+(?P<highest_version>\d+)", re.MULTILINE)
        p3 = re.compile(r"\s+(?P<default_pw>(Not\s+Set|Set))", re.MULTILINE)
        p4 = re.compile(r"\s+(?P<key_chain>(Not\s+Set|Set))", re.MULTILINE)
        p5 = re.compile(r"\s+(?P<key_chain_name>(Not\s+Applicable|\S+))", re.MULTILINE)
        p6 = re.compile(r"\s+(?P<source_ip>(Not\s+Set|\d+\.\d+\.\d+\.\d+))", re.MULTILINE)
        p7 = re.compile(r"\s+(?P<conn_retry>\d+)", re.MULTILINE)
        p8 = re.compile(r"\s+(?P<reconcile_secs>\d+)", re.MULTILINE)
        p9 = re.compile(r"\s+(?P<seq_export>(Not\s+Set|\S+))", re.MULTILINE)
        p10 = re.compile(r"\s+(?P<seq_import>(Not\s+Set|\S+))", re.MULTILINE)
        p11 = re.compile(r"Retry\s+open\s+timer\s+is\s+(?P<retry_timer>(not\s+running|running))", re.MULTILINE)
        p12 = re.compile(
            r"(?P<peer_ip>\d+\.\d+\.\d+\.\d+)\s+(?P<source_ip>\d+\.\d+\.\d+\.\d+)\s+(?P<conn_status>\S+)\s+(?P<duration>\d+:\d+:\d+:\d+)",
            re.MULTILINE)

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
            if ": " in line:
                try:
                    data_type, value = line_strip.split(':', 1)
                    regex = regex_map.get(data_type.strip())
                except ValueError:
                    continue
            elif "Retry open" in line:
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
            else:
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
            if regex:
                match = regex.match((value))
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

