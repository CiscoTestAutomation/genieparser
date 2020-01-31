""" show_system_ntp_all.py
    supports commands:
        * show system ntp all
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# =============================================
# Parser for 'show system ntp all'
# =============================================


class ShowSystemNtpAllSchema(MetaParser):
    """schema for show system ntp all"""

    schema = {
        'clock_state': {
            'system_status': {
                'configured': str,
                'admin_status': str,
                'server_enabled': str,
                'clock_source': str,
                'auth_check': str,
                'current_date_time': str,
                'stratum': int,
                'oper_status': str,
                'server_authenticate': str,
            }
        },
        Optional('peer'): {
            Any(): { # == group['remote']
                'local_mode': {
                    Any(): { # == 'client'
                        'state': str,
                        'refid': str,
                        'stratum': str,
                        'type': str,
                        'poll': int,
                        'reach': str,
                        'offset': float,
                        'a': str,
                        'router': str,
                        'remote': str,
                    }
                }
            }
        },
    }


class ShowSystemNtpAll(ShowSystemNtpAllSchema):
    """ Parser for show system ntp all"""

    cli_command = 'show system ntp all'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # ==============================================================
        # NTP Status
        # ==============================================================
        # Configured         : Yes                Stratum              : 3
        p0 = re.compile(r'Configured +: +(?P<configured>\S+) '
                        r'+Stratum +: +(?P<stratum>\d+)')
        # Admin Status       : up                 Oper Status          : up
        p1 = re.compile(r'Admin Status +: +(?P<admin_status>\S+) '
                        r'+Oper Status +: +(?P<oper_status>\S+)')
        # Server Enabled     : No                 Server Authenticate  : No
        p2 = re.compile(r'Server Enabled +: +(?P<server_enabled>\S+) '
                        r'+Server Authenticate +: +(?P<server_authenticate>\S+)')
        # Clock Source       : 192.168.132.170
        p3 = re.compile(r'Clock Source +: +(?P<clock_source>\S+)')
        # Auth Check         : No
        p4 = re.compile(r'Auth Check +: +(?P<auth_check>\S+)')
        # Current Date & Time: 2020/01/17 17:24:12 UTC
        p5 = re.compile(r'Current Date & Time: +(?P<current_date_time>[\s\S]+)')

        # ==============================================================
        # NTP Active Associations
        # ==============================================================
        # reject                    STEP            -  srvr  -  64   ........  0.000
        p6 = re.compile(r'(?P<state>\S+) +(?P<refid>\S+) '
                        r'+(?P<stratum>[-\d]) +(?P<type>\S+) '
                        r'+(?P<a>[-]) +(?P<poll>\d+) +(?P<reach>\S+) '
                        r'+(?P<offset>[-.\d]+)')
        # Base           172.16.189.64
        p7 = re.compile(r'(?P<router>\S+) +(?P<remote>[.\d]+)')

        for line in out.splitlines():
            line = line.strip()

            # ==============================================================
            # NTP Status
            # ==============================================================
            # Configured         : Yes                Stratum              : 3
            m = p0.match(line)
            if m:
                group = m.groupdict()
                system_status_dict = parsed_dict.setdefault('clock_state', {}).\
                                                 setdefault('system_status', {})
                system_status_dict['configured'] = group['configured']
                system_status_dict['stratum'] = int(group['stratum'])
                continue

            # Admin Status       : up                 Oper Status          : up
            # Server Enabled     : No                 Server Authenticate  : No
            # Clock Source       : 192.168.132.170
            # Auth Check         : No
            # Current Date & Time: 2020/01/17 17:24:12 UTC
            m = p1.match(line) or p2.match(line) or p3.match(line) or p4.match(line) or p5.match(line)

            if m:
                group = m.groupdict()
                for k in group.keys():
                    system_status_dict[k] = group[k]
                continue

            # ==============================================================
            # NTP Active Associations
            # ==============================================================
            # reject                    STEP            -  srvr  -  64   ........  0.000
            # candidate                 172.16.25.201  4  srvr  -  64   YYYYYYYY  -0.541
            m = p6.match(line)
            if m:

                group = m.groupdict()
                local_mode_dict = {'local_mode': {}}
                client_dict = local_mode_dict['local_mode'].setdefault('client', {})

                str_keys = ['state', 'refid', 'stratum',
                            'type', 'a', 'reach']
                for k in str_keys:
                    client_dict[k] = group[k]

                client_dict['poll'] = int(group['poll'])
                client_dict['offset'] = float(group['offset'])
                continue

            # Base           172.16.189.64
            m = p7.match(line)
            if m:
                group = m.groupdict()
                remote = group['remote']
                router = group['router']

                client_dict['router'] = router
                client_dict['remote'] = remote

                parsed_dict.setdefault('peer', {}).\
                            setdefault(remote, local_mode_dict)
                continue

        return parsed_dict




