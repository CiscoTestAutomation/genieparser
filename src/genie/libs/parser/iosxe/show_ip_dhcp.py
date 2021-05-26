"""
show ip dhcp database
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Schema, Any, Optional,
                                                Or, And, Default, Use)

# Parser Utils
from genie.libs.parser.utils.common import Common


class ShowIpDhcpDatabaseSchema(MetaParser):
    """
    Schema for show ip dhcp database
    """

    schema = {
        'url': str,
        'read': str,
        'written': str,
        'status': str,
        'delay_in_seconds': int,
        'timeout_in_seconds': int,
        'failures': int,
        'successes': int
    }


class ShowIpDhcpDatabase(ShowIpDhcpDatabaseSchema):
    """
    Parser for show ip dhcp database
    """
    cli_command = "show ip dhcp database"

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # URL       :    ftp://user:password@172.16.4.253/router-dhcp
        p1 = re.compile(r'^URL +: +(?P<url>(\S+))$')
        # Read      :    Dec 01 1997 12:01 AM
        p2 = re.compile(r'^Read +: +(?P<read>(.+))$')
        # Written   :    Never
        p3 = re.compile(r'^Written +: +(?P<written>(\S+))$')
        # Status    :    Last read succeeded. Bindings have been loaded in RAM.
        p4 = re.compile(r'^Status +: +(?P<status>(.+))$')
        # Delay     :    300 seconds
        p5 = re.compile(r'^Delay +: +(?P<delay>(\d+))')
        # Timeout   :    300 seconds
        p6 = re.compile(r'^Timeout +: +(?P<timeout>(\d+))')
        # Failures  :    0
        p7 = re.compile(r'^Failures +: +(?P<failures>(\d+))$')
        # Successes :    1
        p8 = re.compile(r'^Successes +: +(?P<successes>(\d+))$')

        ret_dict = {}
        for line in out.splitlines():
            line.strip()

            m = p1.match(line)
            if m:
                ret_dict.update({'url': m.groupdict()['url']})
                continue

            m = p2.match(line)
            if m:
                ret_dict.update({'read': m.groupdict()['read']})
                continue

            m = p3.match(line)
            if m:
                ret_dict.update({'written': m.groupdict()['written']})
                continue

            m = p4.match(line)
            if m:
                ret_dict.update({'status': m.groupdict()['status']})
                continue

            m = p5.match(line)
            if m:
                ret_dict.update({'delay_in_seconds': int(m.groupdict()['delay'])})
                continue

            m = p6.match(line)
            if m:
                ret_dict.update({'timeout_in_seconds': int(m.groupdict()['timeout'])})
                continue

            m = p7.match(line)
            if m:
                ret_dict.update({'failures': int(m.groupdict()['failures'])})
                continue

            m = p8.match(line)
            if m:
                ret_dict.update({'successes': int(m.groupdict()['successes'])})
                continue

        return ret_dict
