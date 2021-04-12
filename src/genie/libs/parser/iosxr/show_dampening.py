""" show_dampening.py
    supports commands:
        * show im dampening
        * show im dampening {interface}
"""

# Python
import re
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common

# =============================================
# Parser for 'show im dampening'
# =============================================


class ShowImDampeningSchema(MetaParser):
    schema = {
        'interface': {
            Any(): {
                'index': {
                    Any(): {
                        Optional('capsulation'): str,
                        'penalty': int,
                        'suppressed': str,
                        Optional('protocol'): str,
                    }
                }
            }
        }
    }


class ShowImDampening(ShowImDampeningSchema):
    """ Parser for show im dampening"""

    cli_command = 'show im dampening'

    def cli(self, output=None):
        """parsing mechanism: cli
        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        """
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}
        index = 0
        interface = ""
        # GigabitEthernet0/0/0/1                                               2389 YES
        # POS0/2/0/0                  <base>             ppp                      0 NO
        p1 = re.compile(
            r'^(?P<interface>\S+) +(?P<prot>\S+)? +(?P<cap>\S+)? +(?P<pen>\d+) +(?P<sup>YES|NO)')

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            # GigabitEthernet0/0/0/1                                               2389 YES
            # POS0/2/0/0                  <base>             ppp                      0 NO

            m = p1.match(line)

            if m:
                group = m.groupdict()

                if interface == group['interface']:
                    interface = group['interface']
                    index = index+1
                else:
                    interface = group['interface']
                    index = 1
                protocol_dict = result_dict.setdefault('interface', {}).setdefault(
                    interface, {}).setdefault('index', {}).setdefault(index, {})
                protocol_dict.update({'penalty': int(group['pen'])})
                protocol_dict.update({'suppressed': group['sup']})
                if group['cap']:
                    protocol_dict.update({'capsulation': group['cap']})
                if group['prot']:
                    protocol_dict.update({'protocol': group['prot']})
                continue

        return result_dict


class ShowImDampeningIntfSchema(MetaParser):
    schema = {
        'interface': {
            Any(): {
                'dampening_status': str,
                Optional('interface_handler'): str,
                Optional('currently_suppressed'): str,
                Optional('half_life'): int,
                Optional('max_supress_time'): int,
                Optional('penalty'): int,
                Optional('reuse'): int,
                Optional('suppress'): int,
                Optional('suppressed_secs_remaining'): int,
                Optional('underlying_state'): str,
                Optional('index'):
                {Any():
                 {Optional('capsulation'): str,
                  Optional('penalty'): int,
                  Optional('suppression'): str,
                  Optional('suppression_remaining_sec'): int,
                  Optional('underlying_state'): str,
                  Optional('protocol'): str,
                  },
                 },
            }
        }
    }


class ShowImDampeningIntf(ShowImDampeningIntfSchema):
    """ Parser for show im dampening interface {interface} """

    cli_command = 'show im dampening interface {interface}'

    def cli(self, interface, output=None):
        """parsing mechanism: cli
        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        """
        if output is None:
            out = self.device.execute(
                self.cli_command.format(interface=interface))
        else:
            out = output

        result_dict = {}
        index = 0
        # TenGigE 0/1/0/0 (0x01180020)
        # GigabitEthernet0/2/0/0 (0x080002c0)
        p1 = re.compile(
            r'^(?P<interface>[a-zA-Z]+\s?[\/\d]+)( +\((?P<intf_hand>\S+)\))?$')

        # Dampening enabled: Penalty 1625, SUPPRESSED (42 secs remaining)
        p2 = re.compile(
            r'Dampening\s(?P<stat>\w+): +Penalty\s(?P<pen>\d+), +SUPPRESSED\s\((?P<sup>\d+)')

        # Dampening enabled: Penalty 0, not suppressed
        p3 = re.compile(
            r'Dampening\s(?P<stat_ns>\w+): +Penalty\s(?P<pen_ns>\d+), +not\ssupp.+')

        # underlying-state:  Up
        # Underlying state: Down
        p4 = re.compile(r'^[a-z-A-Z\s]+state:\s+(?P<und_stat>\S+)')

        #  half-life: 1        reuse:             1000
        p5 = re.compile(
            r'half-life:\s+(?P<half_life>\d+) +reuse:\s+(?P<reuse>\d+)')

        # suppress:  1500     max-suppress-time: 4
        p6 = re.compile(
            r'suppress:\s+(?P<suppress>\d+) +max-suppress-time:\s(?P<max_suppress>\d+)')

        # ipv6           ipv6               1625  YES    42s  remaining        Down
        p7 = re.compile(r'^(?P<prot>\S+)? +(?P<prot_cap>\S+)? +(?P<prot_pen>\d+) +(?P<prot_sup>YES|NO)'
                        ' +(?P<prot_sup_time>\d+). +remaining\s+(?P<prot_state>\S+)')

        # Dampening not enabled
        p8 = re.compile(r'^(?P<stat>Dampening not enabled)')

        for line in out.splitlines():

            if line:
                line = line.strip()

            else:
                continue

            # TenGigE 0/1/0/0 (0x01180020)
            # GigabitEthernet0/2/0/0 (0x080002c0)

            m = p1.match(line)

            if m:
                group = m.groupdict()
                result_dict.setdefault('interface', {})
                interface = group['interface']
                interface_dict = result_dict.setdefault(
                    'interface', {}).setdefault(interface, {})
                if group['intf_hand']:
                    interface_dict.update(
                        {'interface_handler': group['intf_hand']})
                continue

            # Dampening enabled: Penalty 1625, SUPPRESSED (42 secs remaining)

            m = p2.match(line)

            if m:
                group = m.groupdict()
                result_dict['interface'][interface].update(
                    {'dampening_status': group['stat']})
                result_dict['interface'][interface].update(
                    {'penalty': int(group['pen'])})
                result_dict['interface'][interface].update(
                    {'suppressed_secs_remaining': int(group['sup'])})
                result_dict['interface'][interface].update(
                    {'currently_suppressed': 'yes'})
                continue

            # Dampening enabled: Penalty 0, not suppressed

            m = p3.match(line)

            if m:
                group = m.groupdict()
                result_dict['interface'][interface].update(
                    {'dampening_status': group['stat_ns']})
                result_dict['interface'][interface].update(
                    {'penalty': int(group['pen_ns'])})
                result_dict['interface'][interface].update(
                    {'currently_suppressed': 'no'})
                continue

            # underlying-state:  Up
            # Underlying state: Down

            m = p4.match(line)

            if m:
                group = m.groupdict()
                result_dict['interface'][interface].update(
                    {'underlying_state': group['und_stat']})
                continue

            #  half-life: 1        reuse:             1000
            m = p5.match(line)

            if m:
                group = m.groupdict()
                result_dict['interface'][interface].update(
                    {'half_life': int(group['half_life'])})
                result_dict['interface'][interface].update(
                    {'reuse': int(group['reuse'])})
                continue

            # suppress:  1500     max-suppress-time: 4
            m = p6.match(line)

            if m:
                group = m.groupdict()
                result_dict['interface'][interface].update(
                    {'suppress': int(group['suppress'])})
                result_dict['interface'][interface].update(
                    {'max_supress_time': int(group['max_suppress'])})
                continue

            # ipv6           ipv6               1625  YES    42s  remaining        Down
            m = p7.match(line)

            if m:
                group = m.groupdict()
                index = index+1
                protocol_dict = result_dict.setdefault('interface', {}).setdefault(
                    interface, {}).setdefault('index', {}).setdefault(index, {})
                protocol_dict.update({'penalty': int(group['prot_pen'])})
                protocol_dict.update({'suppression': group['prot_sup']})
                protocol_dict.update(
                    {'suppression_remaining_sec': int(group['prot_sup_time'])})
                protocol_dict.update({'underlying_state': group['prot_state']})
                if group['prot']:
                    protocol_dict.update({'protocol': group['prot']})
                if group['prot_cap']:
                    protocol_dict.update({'capsulation': group['prot_cap']})
                continue

            # Dampening not enabled
            m = p8.match(line)

            if m:
                group = m.groupdict()
                result_dict.setdefault(
                    'interface', {}).setdefault(interface, {})
                result_dict['interface'][interface].update(
                    {'dampening_status': 'dampening_not_enabled'})
                continue

        return result_dict
