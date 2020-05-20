from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any
import re


# =====================================
# Schema for 'show sdwan bfd sessions'
# =====================================
class ShowSdwanBfdSessionsSchema(MetaParser):

    """ Schema for "show sdwan bfd sessions """

    schema = {
        "system_ip": {
            Any(): {
                'source_tloc_color': {
                    Any(): {
                        "destination_public_ip": str,
                        "destination_public_port": str,
                        "detect_multiplier": str,
                        "encapsulation": str,
                        "site_id": str,
                        "source_ip": str,
                        "remote_tloc_color": str,
                        "state": str,
                        "transitions": str,
                        "tx_interval": str,
                        "uptime": str,
                    },
                },
            },
        },
    }


# =====================================
# Parser for 'show sdwan bfd sessions'
# =====================================
class ShowSdwanBfdSessions(ShowSdwanBfdSessionsSchema):

    """ Parser for "show sdwan bfd sessions" """
    exclude = ['uptime']
    
    cli_command = "show sdwan bfd sessions"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}


        p1 = re.compile(
            r"(?P<system_ip>\S+)\s+(?P<site_id>\d+)\s+(?P<state>\w+)\s+"
            r"(?P<source_tloc_color>\S+)\s+(?P<remote_tloc_color>\S+)\s+"
            r"(?P<source_ip>\S+)\s+(?P<destination_public_ip>\S+)\s+"
            r"(?P<destination_public_port>\d+)\s+(?P<encapsulation>\w+)\s+"
            r"(?P<detect_multiplier>\d+)\s+(?P<tx_interval>\d+)\s+"
            r"(?P<uptime>\S+)\s+(?P<transitions>\d+)"
        )

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                system_ip = group["system_ip"]
                parsed_dict.setdefault("system_ip", {}).setdefault(system_ip, {})
                session_dict = parsed_dict["system_ip"][system_ip].setdefault("source_tloc_color", {})
                ip_dict = session_dict.setdefault(group["source_tloc_color"], {})
                ip_dict["site_id"] = group["site_id"]
                ip_dict["state"] = group["state"]
                ip_dict["source_ip"] = group["source_ip"]
                ip_dict["remote_tloc_color"] = group["remote_tloc_color"]
                ip_dict["destination_public_ip"] = group["destination_public_ip"]
                ip_dict["destination_public_port"] = group["destination_public_port"]
                ip_dict["encapsulation"] = group["encapsulation"]
                ip_dict["detect_multiplier"] = group["detect_multiplier"]
                ip_dict["tx_interval"] = group["tx_interval"]
                ip_dict["uptime"] = group["uptime"]
                ip_dict["transitions"] = group["transitions"]

                continue

        return parsed_dict


# ===============================================
# Schema for 'show sdwan bfd summary'
# ===============================================
class ShowSdwanBfdSummarySchema(MetaParser):

    """ Schema for "show sdwan bfd summary" command """

    schema = {
        "sessions_total": int,
        "sessions_up": int,
        "sessions_max": int,
        "sessions_flap": int,
        "poll_interval": int,
    }


# ===============================================
# Parser for 'show sdwan bfd summary'
# ===============================================
class ShowSdwanBfdSummary(ShowSdwanBfdSummarySchema):

    """ Parser for "show sdwan bfd summary" """

    cli_command = "show sdwan bfd summary"
    exclude = []
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
    
        parsed_dict = {}

        # sessions-total         8
        p1 = re.compile(
            r"^sessions-total\s+(?P<sessions_total>\S+)"
        )

        # sessions-up            8
        p2 = re.compile(
            r"^sessions-up\s+(?P<sessions_up>\S+)"
        )

        # sessions-max           10
        p3 = re.compile(
            r"^sessions-max\s+(?P<sessions_max>\S+)"
        )

        # sessions-flap          121
        p4 = re.compile(
            r"^sessions-flap\s+(?P<sessions_flap>\S+)"
        )

        # poll-interval          120000
        p5 = re.compile(
            r"^poll-interval\s+(?P<poll_interval>\S+)"
        )

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                parsed_dict['sessions_total'] = m.groupdict()['sessions_total']
                continue

            m = p2.match(line)
            if m:
                parsed_dict['sessions_up'] = m.groupdict()['sessions_up']
                continue

            m = p3.match(line)
            if m:
                parsed_dict['sessions_max'] = m.groupdict()['sessions_max']
                continue

            m = p4.match(line)
            if m:
                parsed_dict['sessions_flap'] = m.groupdict()['sessions_flap']
                continue

            m = p5.match(line)
            if m:
                parsed_dict['poll_interval'] = m.groupdict()['poll_interval']
                continue

        return parsed_dict
