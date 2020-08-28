"""show_bfd.py

JUNOS parsers for the following commands:
    * show bfd session
"""

import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import Any, Optional, Use, Schema


class ShowBFDSessionSchema(MetaParser):
    """ Schema for
        * show bfd session
    """
    def validate_bfd_session(value):
        if not isinstance(value, list):
            raise SchemaError('BFD Session not a list')

        bfd_session = Schema({
            "session-neighbor": str,
            "session-state": str,
            Optional("session-interface"): str,
            "session-detection-time": str,
            "session-transmission-interval": str,
            "session-adaptive-multiplier": str,
        })

        for item in value:
            bfd_session.validate(item)
        return value

    schema = {
        "bfd-session-information": {
            "bfd-session": Use(validate_bfd_session)
        }
    }


class ShowBFDSession(ShowBFDSessionSchema):
    """ Parser for:
        * show bfd session
    """

    cli_command = 'show bfd session'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # 10.0.0.1                        Operational Open          26         DU
        # 10.0.0.2               Up        ge-0/0/0.0     1.500     0.500        3
        p1 = re.compile(r'^(?P<session_neighbor>\S+) +'
                        r'(?P<session_state>\S+)'
                        r'( +(?P<session_interface>\S+))? +'
                        r'(?P<session_detection_time>[\d\.]+) +'
                        r'(?P<session_transmission_interval>[\d\.]+) +'
                        r'(?P<session_adaptive_multiplier>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                session_list = ret_dict.setdefault("bfd-session-information", {}).\
                    setdefault("bfd-session", [])
                session_list.append({
                    k.replace('_', '-'): v
                    for k, v in group.items() if v is not None
                })

        return ret_dict


class ShowBFDSessionDetailSchema(MetaParser):
    """
    Schema for:
        * show bfd session address {ipaddress} detail
    """

    schema = {
        "bfd-session-information": {
            "bfd-session": {
                "bfd-client": {
                    "client-name": str,
                    "client-reception-interval": str,
                    "client-transmission-interval": str
                },
                "local-diagnostic": str,
                "remote-diagnostic": str,
                "remote-state": str,
                "session-adaptive-multiplier": str,
                "session-detection-time": str,
                Optional("session-interface"): str,
                "session-neighbor": str,
                "session-state": str,
                "session-transmission-interval": str,
                "session-type": str,
                "session-up-time": str,
                "session-version": str
            },
            "clients": str,
            "cumulative-reception-rate": str,
            "cumulative-transmission-rate": str,
            "sessions": str
        }
    }


class ShowBFDSessionDetail(ShowBFDSessionDetailSchema):
    """
    Parser for:
        *show bfd session address {ipaddress} detail
    """

    cli_command = 'show bfd session {ipaddress} detail'

    def cli(self, ipaddress, output=None):
        if not output:
            cmd = self.cli_command.format(ipaddress=ipaddress)
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        # ========================================================
        # Regex patterns
        # ========================================================
        #                                                       Detect   Transmit
        #     Address                  State     Interface      Time     Interval  Multiplier
        #     10.34.2.250             Up                       1.500     0.500        3
        p1 = re.compile(r'^(?P<session_neighbor>\S+) +'
                        r'(?P<session_state>\S+)'
                        r'( +(?P<session_interface>\S+))? +'
                        r'(?P<session_detection_time>[\d\.]+) +'
                        r'(?P<session_transmission_interval>[\d\.]+) +'
                        r'(?P<session_adaptive_multiplier>\S+)$')

        #      Client LDP-OAM, TX interval 0.050, RX interval 0.050
        p2 = re.compile(r'^Client +(?P<client_name>\S+), +TX +interval '
                        r'(?P<client_transmission_interval>\S+), +RX +interval '
                        r'(?P<client_reception_interval>\S+)$')

        #      Session up time 00:02:46
        p3 = re.compile(r'^Session +up +time +(?P<session_up_time>\S+)$')

        #      Local diagnostic None, remote diagnostic None
        p4 = re.compile(r'^Local +diagnostic +(?P<local_diagnostic>\S+), '
                        r'remote +diagnostic +(?P<remote_diagnostic>\S+)$')

        #      Remote state Up, version 1
        p5 = re.compile(r'^Remote +state +(?P<remote_state>\S+), '
                        r'+version +(?P<session_version>\S+)$')

        #      Session type: Multi hop BFD
        p6 = re.compile(r'^Session +type: +(?P<session_type>[\S\s]+)$')

        #     1 sessions, 1 clients
        p7 = re.compile(r'^(?P<sessions>\S+) +sessions, +(?P<clients>\S+) +clients$')

        #     Cumulative transmit rate 2.0 pps, cumulative receive rate 2.0 pps
        p8 = re.compile(r'^Cumulative transmit rate (?P<cumulative_reception_rate>\S+) pps, '
                        r'cumulative receive rate (?P<cumulative_transmission_rate>\S+) pps$')

        # ========================================================
        # Build output
        # ========================================================
        for line in out.splitlines():
            line = line.strip()

            #                                                       Detect   Transmit
            #     Address                  State     Interface      Time     Interval  Multiplier
            #     10.34.2.250             Up                       1.500     0.500        3
            #  ...
            #      Session up time 00:02:46
            #      Local diagnostic None, remote diagnostic None
            #      Remote state Up, version 1
            #      Session type: Multi hop BFD
            m = p1.match(line) or p3.match(line) or \
                p4.match(line) or p5.match(line) or \
                p6.match(line)
            if m:
                group = m.groupdict()

                if "bfd-session-information" not in ret_dict:
                    bfd_session = ret_dict.setdefault("bfd-session-information", {}).\
                        setdefault("bfd-session", {})

                for k, v in group.items():
                    if group[k]:
                        bfd_session[k.replace('_', '-')] = v

                continue

            #      Client LDP-OAM, TX interval 0.050, RX interval 0.050
            m = p2.match(line)
            if m:
                group = m.groupdict()

                bfd_client = bfd_session.setdefault("bfd-client", {})

                for k, v in group.items():
                    bfd_client[k.replace('_', '-')] = v

                continue

            #     1 sessions, 1 clients
            #     Cumulative transmit rate 2.0 pps, cumulative receive rate 2.0 pps
            m = p7.match(line) or p8.match(line)
            if m:
                group = m.groupdict()

                for k, v in group.items():
                    ret_dict['bfd-session-information'][k.replace('_', '-')] = v

                continue

        return ret_dict
