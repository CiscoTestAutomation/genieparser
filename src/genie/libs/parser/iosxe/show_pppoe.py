''' show_pppoe.py

IOSXE parsers for the following show commands:

    * 'show pppoe statistics'
'''
# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use

log = logging.getLogger(__name__)

# ==========================================
# Schema for
#   'show pppoe statistics'
# ===========================================
class ShowPppoeStatisticsSchema(MetaParser):
    """
    Schema for
        * 'show pppoe statistics'
    """

    schema = {
        'pppoe_events': {
            Any(): {
                'total': int,
                'since_cleared': int
            }
        },
        'pppoe_statistics': {
            Any(): {
                'total': int,
                'since_cleared': int
            }
        }
    }

class ShowPppoeStatistics(ShowPppoeStatisticsSchema):
    """
    Parser for
        * 'show pppoe statistics'
    """
    cli_command = ['show pppoe statistics']

    def cli(self, output=None):
        cmd = self.cli_command[0]

        if output is None:
            output = self.device.execute(self.cli_command[0])

        res_dict = {}
        # PPPoE Events                   TOTAL         SINCE CLEARED
        # PPPoE Statistics               TOTAL         SINCE CLEARED
        p1 = re.compile(r'^PPPoE\s+(?P<pppoe_type>\w+)\s+TOTAL\s+SINCE CLEARED$')

        # SSS Request                    146772        146772
        # Base VA Create Errors (sync)   0             0
        p2 = re.compile(r'^(?P<key>\D+[a-zA-Z)])\s+(?P<total>\d+)\s+(?P<since_cleared>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # PPPoE Events                   TOTAL         SINCE CLEARED
            # PPPoE Statistics               TOTAL         SINCE CLEARED
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                key = 'pppoe_{}'.format(groups['pppoe_type'].lower())
                res_dict.setdefault(key, {})

            # SSS Request                    146772        146772
            # Base VA Create Errors (sync)   0             0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                key1 = groups['key'].lower().replace(' ', '_').replace('(', '').replace(')', '').replace('-','_')
                res_dict.setdefault(key, {})
                res_dict[key].setdefault(key1, {})
                res_dict[key][key1]['total'] = int(groups['total'])
                res_dict[key][key1]['since_cleared'] = int(groups['since_cleared'])

        return res_dict

# =============================================
# Parser Schema for 'show pppoe session'
# =============================================


class ShowPppoeSessionSchema(MetaParser):
    """Schema for "show pppoe session" """

    schema = {
        "pppoe_id": {
            Any(): {
                "uniq_id": Or(int, str),
                "remote_mac": str,
                "local_mac": str,
                "port": str,
                "vt": Or(int, str),
                "va": str,
                Optional("va_st"): str,
                "state_type": str,
            },
        },
    }


# =============================================
# Parser for 'show pppoe session'
# =============================================

class ShowPppoeSession(ShowPppoeSessionSchema):
    """ parser for "show pppoe session" """

    cli_command = "show pppoe session"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        res_dict = {}

        # N/A      2  f80b.cb77.4409  Gi0/0/3               Di100 Vi2        UP
        # 639  17658  80b7.092d.32e6  Gi0/1/0                  4  N/A        LCP
        p1 = re.compile(
            r'^(?P<uniq_id>([A-Z/]+|\d+))+\s+(?P<pppoe_id>\d+)+\s+(?P<remote_mac>([0-9a-fA-F].?){12}\b)\s+'
            r'(?P<port>\w+[/]+\d[/]+\d+)\s+(?P<vt>\w+)\s+(?P<va>\w+|[A-Z/]+|[A-Za-z0-9.]+)\s+(?P<state_type>\w+)')

        #            4403.a743.55ed                              UP
        p2 = re.compile(r'^(?P<local_mac>([0-9a-fA-F].?){12}\b)+\s+(?P<va_st>\w+)$')

        #            bcd2.95c3.80c8
        p2_1 = re.compile(r'^(?P<local_mac>([0-9a-fA-F].?){12}$)')

        for line in output.splitlines():
            line = line.strip()

            # N/A      2  f80b.cb77.4409  Gi0/0/3               Di100 Vi2        UP
            # 639  17658  80b7.092d.32e6  Gi0/1/0                  4  N/A        LCP
            m = p1.match(line)
            if m:
                group = m.groupdict()
                pppoe_id = group.pop("pppoe_id")
                pppoe_id_dict = res_dict.setdefault("pppoe_id", {}). \
                        setdefault(pppoe_id, {})
                pppoe_id_dict.update({k: v for k, v in group.items()})

            # 4403.a743.55ed                              UP
            m1 = p2.match(line)
            if m1:
               group = m1.groupdict()
               pppoe_id_dict.update({k: v for k, v in group.items()})
               continue

            # bcd2.95c3.80c8
            m1 = p2_1.match(line)
            if m1:
               group = m1.groupdict()
               pppoe_id_dict.update({k: v for k, v in group.items()})
               continue

        return res_dict

# =============================================
# Parser Schema for 'show pppoe summary'
# =============================================


class ShowPppoeSummarySchema(MetaParser):
    """ Schema for 'show pppoe summary' """

    schema = {
        Optional('client_session'): int,
        Optional('total'): {
            Optional('total_count'): int,
            Optional('total_pta_count'): int,
            Optional('total_fwded_count'): int,
            Optional('total_trans_count'): int,
            Optional('interface'): {
                Optional(Any()): {
                    Optional('total'): int,
                    Optional('pta'): int,
                    Optional('fwded'): int,
                    Optional('trans'): int
                }
            }
        }
    }


# =============================================
# Parser for 'show pppoe summary'
# =============================================


class ShowPppoeSummary(ShowPppoeSummarySchema):
    """ parser for "show pppoe summary" """

    cli_command = "show pppoe summary"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        res_dict = {}

        # 1 client session
        p1 = re.compile(r'^(?P<client_session>\d+)')

        # TOTAL                               2       2       0       0
        p1_1 = re.compile(
            r'^(TOTAL\s+(?P<total_count>\d+)\s+(?P<total_pta_count>\d+)\s+(?P<total_fwded_count>\d+)+\s+'
            r'(?P<total_trans_count>\d+)$)')

        # GigabitEthernet0/1/0                1       1       0       0
        p2 = re.compile(
            r'^((?P<interface>\D+\d+((/\d+)+(\.\d+)?)?)\s+(?P<total>\d+)\s+(?P<pta>\d+)\s+(?P<fwded>\d+)+\s+'
            r'(?P<trans>\d+)$)')

        for line in output.splitlines():
            line = line.strip()

            # 1 client session
            m = p1.match(line)
            if m:
                group = m.groupdict()
                client_session = int(group['client_session'])
                res_dict.update({'client_session': client_session})
                continue

            # TOTAL   2       2       0       0
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                total_count_dict = res_dict.setdefault('total', {})
                total_count_dict.update({k: int(v) for k, v in group.items()})
                continue

            # GigabitEthernet0/1/0     1       1       0       0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface = group.pop('interface')
                interface_dict = total_count_dict.setdefault('interface', {}).setdefault(interface, {})
                interface_dict.update({k: int(v) for k, v in group.items()})
                continue

        return res_dict
