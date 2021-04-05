"""show_bfd.py

JUNOS parsers for the following commands:
    * show bfd session
"""

import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import Any, Optional, Use, Schema, ListOf


class ShowBFDSessionSchema(MetaParser):
    """ Schema for
        * show bfd session
    """

    schema = {
        "bfd-session-information": {
            Optional("bfd-session"): ListOf({
                    "session-neighbor": str,
                    "session-state": str,
                    Optional("session-interface"): str,
                    "session-detection-time": str,
                    "session-transmission-interval": str,
                    "session-adaptive-multiplier": str,
                }),
            "clients": str,
            "cumulative-reception-rate": str,
            "cumulative-transmission-rate": str,
            "sessions": str
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

        #     1 sessions, 1 clients
        p2 = re.compile(r'^(?P<sessions>\S+) +sessions, +(?P<clients>\S+) +clients$')

        #     Cumulative transmit rate 2.0 pps, cumulative receive rate 2.0 pps
        p3 = re.compile(r'^Cumulative transmit rate (?P<cumulative_reception_rate>\S+) pps, '
                        r'cumulative receive rate (?P<cumulative_transmission_rate>\S+) pps$')

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
                continue

            #     1 sessions, 1 clients
            #     Cumulative transmit rate 2.0 pps, cumulative receive rate 2.0 pps
            m = p2.match(line) or p3.match(line)
            if m:
                group = m.groupdict()

                for k, v in group.items():
                    ret_dict.setdefault('bfd-session-information', {})[k.replace('_', '-')] = v

                continue

        return ret_dict


class ShowBFDSessionDetailSchema(MetaParser):
    """
    Schema for:
        * show bfd session address {ipaddress} detail
    """

    schema = {
        "bfd-session-information": {
            Optional("bfd-session"): {
                Optional("bfd-client"): {
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
                Optional("session-up-time"): str,
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

    cli_command = 'show bfd session address {ipaddress} detail'

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
        #      Client LDP-OAM ipv4-unicast Area0.0.0.0, TX interval 0.050, RX interval 0.050
        p2 = re.compile(r'^Client +(?P<client_name>\S+)([\S\s]+)?, +TX +interval '
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
                if "bfd-session-information" not in ret_dict:
                    bfd_session = ret_dict.setdefault("bfd-session-information", {})
                for k, v in group.items():
                    ret_dict.setdefault('bfd-session-information', {})[k.replace('_', '-')] = v

                continue

        return ret_dict


class ShowBFDSessionAddressExtensiveSchema(MetaParser):
    """
    Schema for:
        * show bfd session address {ip_address} extensive
    """

    schema = {
    "bfd-session-information": {
        "bfd-session": {
            "adaptive-asynchronous-transmission-interval": str,
            "adaptive-reception-interval": str,
            "bfd-client": {
                "client-name": str,
                "client-reception-interval": str,
                "client-transmission-interval": str
            },
            "detection-multiplier": str,
            "echo-mode-desired": str,
            "echo-mode-state": str,
            "local-diagnostic": str,
            "local-discriminator": str,
            "minimum-asynchronous-interval": str,
            "minimum-reception-interval": str,
            "minimum-slow-interval": str,
            "minimum-transmission-interval": str,
            "neighbor-fate": str,
            "neighbor-minimum-reception-interval": str,
            "neighbor-minimum-transmission-interval": str,
            "neighbor-session-multiplier": str,
            "no-refresh": str,
            "remote-diagnostic": str,
            "remote-discriminator": str,
            "remote-state": str,
            "session-adaptive-multiplier": str,
            "session-detection-time": str,
            "session-interface": str,
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


class ShowBFDSessionAddressExtensive(ShowBFDSessionAddressExtensiveSchema):
    """
    Parser for:
        *show bfd session address {ip_address} extensive
    """

    cli_command = 'show bfd session address {ipaddress} extensive'

    def cli(self, ipaddress=None, output=None):
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
        p2 = re.compile(r'^Client +(?P<client_name>\S+)([\s\S]+)?, '
                        r'+TX +interval (?P<client_transmission_interval>\S+), '
                        r'+RX +interval (?P<client_reception_interval>\S+)$')

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


        # Min async interval 1.000, min slow interval 1.000
        p7 = re.compile(r'^Min +async +interval +(?P<minimum_asynchronous_interval>'
                        r'[\d\.]+), min +slow +interval +(?P<minimum_slow_interval>[\d\.]+)$')

        #Adaptive async TX interval 1.000, RX interval 1.000
        p8 = re.compile(r'^Adaptive +async +TX +interval +'
                        r'(?P<adap_transmission_interval>[\d\.]+), RX +interval '
                        r'+(?P<adap_reception_interval>[\d\.]+)$')

        #Local min TX interval 1.000, minimum RX interval 1.000, multiplier 3
        p9 = re.compile(r'^Local +min +TX +interval +(?P<minimum_transmission_interval>[\d\.]+), '
                        r'minimum +RX +interval +(?P<minimum_reception_interval>[\d\.]+), '
                        r'+multiplier +(?P<detection_multiplier>\d+)$')

        #Remote min TX interval 1.000, min RX interval 1.000, multiplier 3
        p10 = re.compile(r'^Remote +min +TX +interval +(?P<neighbor_min_trans_interval>[\d\.]+), '
                         r'min +RX +interval +(?P<neighbor_min_rec_interval>[\d\.]+), +multiplier '
                         r'+(?P<neighbor_session_multiplier>\d+)$')

        #Local discriminator 350, remote discriminator 772
        p11 = re.compile(r'^Local +discriminator +(?P<local_discriminator>\d+), '
                        r'remote +discriminator +(?P<remote_discriminator>\d+)$')

        #Echo mode disabled/inactive
        p12 = re.compile(r'^Echo +mode +(?P<echo_mode_desired>\S+)+\/+(?P<echo_mode_state>\S+)$')

        #Remote is control-plane independent
        p13 = re.compile(r'^(?P<neighbor_fate>Remote+ is+[\s\S]+)$')

        #Session ID: 0x1b3
        p14 = re.compile(r'^(?P<no_refresh>Session+ ID:+[\s\S]+)$')

        #     1 sessions, 1 clients
        p15 = re.compile(r'^(?P<sessions>\S+) +sessions, +(?P<clients>\S+) +clients$')

        #     Cumulative transmit rate 2.0 pps, cumulative receive rate 2.0 pps
        p16 = re.compile(r'^Cumulative transmit rate (?P<cumulative_reception_rate>\S+) pps, '
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

            #      Min async interval 1.000, min slow interval 1.000
            m = p7.match(line)
            if m:
                group = m.groupdict()

                for k, v in group.items():
                    bfd_session[k.replace('_', '-')] = v
                continue

            #      Adaptive async TX interval 1.000, RX interval 1.000
            m = p8.match(line)
            if m:
                group = m.groupdict()

                bfd_session['adaptive-asynchronous-transmission-interval'] = group['adap_transmission_interval']
                bfd_session['adaptive-reception-interval'] = group['adap_reception_interval']

                continue

            #      Local min TX interval 1.000, minimum RX interval 1.000, multiplier 3
            m = p9.match(line)
            if m:
                group = m.groupdict()

                for k, v in group.items():
                    bfd_session[k.replace('_', '-')] = v
                continue

            #      Remote min TX interval 1.000, min RX interval 1.000, multiplier 3
            m = p10.match(line)
            if m:
                group = m.groupdict()

                bfd_session['neighbor-minimum-reception-interval'] = group['neighbor_min_rec_interval']
                bfd_session['neighbor-minimum-transmission-interval'] = group['neighbor_min_trans_interval']
                bfd_session['neighbor-session-multiplier'] = group['neighbor_session_multiplier']
                continue

            #      Local discriminator 350, remote discriminator 772
            m = p11.match(line)
            if m:
                group = m.groupdict()

                for k, v in group.items():
                    bfd_session[k.replace('_', '-')] = v
                continue

            #      Echo mode disabled/inactive
            m = p12.match(line)
            if m:
                group = m.groupdict()

                for k, v in group.items():
                    bfd_session[k.replace('_', '-')] = v
                continue

            #      Remote is control-plane independent
            m = p13.match(line)
            if m:
                group = m.groupdict()

                for k, v in group.items():
                    bfd_session[k.replace('_', '-')] = v
                continue

            #      Session ID: 0x1b3
            m = p14.match(line)
            if m:
                group = m.groupdict()

                for k, v in group.items():
                    bfd_session[k.replace('_', '-')] = v
                continue

            #     1 sessions, 1 clients
            #     Cumulative transmit rate 2.0 pps, cumulative receive rate 2.0 pps
            m = p15.match(line) or p16.match(line)
            if m:
                group = m.groupdict()

                for k, v in group.items():
                    ret_dict['bfd-session-information'][k.replace('_', '-')] = v

                continue

        return ret_dict
