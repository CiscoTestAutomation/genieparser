'''show_bfd.py
NXOS parser for the following show commands
    * show bfd ipv4 neighbors
    * show bfd ipv4 neighbors vrf {vrf}
    * show bfd ipv4 {ipv4_address} neighbors vrf {vrf}
    * show bfd ipv6 neighbors
    * show bfd ipv6 neighbors vrf {vrf}
    * show bfd ipv6 {ipv6_address} neighbors vrf {vrf}
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Optional, Any

# parser utils
from genie.libs.parser.utils.common import Common


class ShowBfdSessionSchema(MetaParser):
    """
    Schema for the following show commands:
        * show bfd ipv4 neighbors
        * show bfd ipv4 neighbors vrf {vrf}
        * show bfd ipv4 {ipv4_address} neighbors vrf {vrf}
        * show bfd ipv6 neighbors
        * show bfd ipv6 neighbors vrf {vrf}
        * show bfd ipv6 {ipv6_address} neighbors vrf {vrf}
    """
    schema = {
        'vrf': {
            Any(): {
                'our_address': {
                    Any(): {
                        'neighbor_address': {
                            Any(): {
                                Optional('ld_rd'): str,
                                Optional('rh_rs'): str,
                                Optional('holdown_timer'): str,
                                Optional('holdown_timer_multiplier'): int,
                                Optional('state'): str,
                                Optional('interface'): str,
                                Optional('vrf'): str,
                                Optional('type'): str,
                            }
                        }
                    }
                }
            }
        }
    }

# ==============================================================
# Parser for the following show commands:
# 	* 'show bfd ipv4 neighbors'
# ==============================================================


class ShowBfdIpv4Session(ShowBfdSessionSchema):
    """ Parser for the following commands:
        * show bfd ipv4 neighbors
        * show bfd ipv4 neighbors vrf {vrf}
        * show bfd ipv4 {ipv4_address} neighbors vrf {vrf}

        OurAddr         NeighAddr       LD/RD                 RH/RS           Holdown(mult)     State       Int                   Vrf                              Type
        32.1.5.2        32.1.5.3        1090519042/1090519063 Up              4741(3)           Up          Po123.5               vxlan-1003                       SH
        32.1.6.2        32.1.6.3        1090519043/1090519064 Up              4741(3)           Up          Po123.6               vxlan-1003                       SH
        32.1.7.2        32.1.7.3        1090519044/1090519065 Up              4741(3)           Up          Po123.7               vxlan-1003                       SH
        11.11.2.1       11.11.5.1       1090519055/1090520660 Up              516(3)            Up          Lo13                  vxlan-1005                       MH
        11.11.2.1       11.11.6.1       1090519380/1090519696 Up              662(3)            Up          Lo12                  vxlan-1004                       MH
        node02#
    """

    cli_command = ['show bfd ipv4 neighbors',
                   'show bfd ipv4 neighbors vrf {vrf}',
                   'show bfd ipv4 {ipv4_address} neighbors vrf {vrf}']

    def cli(self, vrf='', ipv4_address=None, output=None):
        if output is None:
            # execute command to get output
            if vrf:
                if ipv4_address:
                    out = self.device.execute(self.cli_command[2].format(
                        vrf=vrf, ipv4_address=ipv4_address))
                else:
                    out = self.device.execute(
                        self.cli_command[1].format(vrf=vrf))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # initial variables
        ret_dict = {}

        # regex pattern for
        # 10.10.12.1      10.10.12.2      1090519053/1090519042 Up              6000(3)           Up          Eth1/35               default                          SH       N/A
        p1 = re.compile(
            r'^(?P<our_address>[\w\.\:]+)\s+'
            r'(?P<our_neighbor>[\w\.\:]+)\s+'
            r'(?P<ld_rd>\d+\/\d+)\s+(?P<rh_rs>\w+)\s+'
            r'(?P<holdown_timer>N\/A|\d+)\((?P<holdown_timer_multiplier>\d+)\)\s+'
            r'(?P<state>\S+)\s+(?P<interface>\S+)\s+(?P<vrf>\S+)\s+(?P<type>\S+).+?$')

        for line in out.splitlines():
            line = line.strip()

        # match line for p1
        # 10.10.12.1      10.10.12.2      1090519053/1090519042 Up              6000(3)           Up          Eth1/35               default                          SH       N/A
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf = ret_dict.setdefault('vrf', {}). \
                    setdefault(group['vrf'], {})
                our_address = vrf.setdefault(
                    'our_address', {}).setdefault(group['our_address'], {})
                our_neighbor = our_address.setdefault(
                    'neighbor_address', {}).setdefault(group['our_neighbor'], {})
                our_neighbor.update({'ld_rd': group['ld_rd'],
                                     'rh_rs': group['rh_rs'],
                                     'holdown_timer': group['holdown_timer'],
                                     'holdown_timer_multiplier': int(group['holdown_timer_multiplier']),
                                     'state': group['state'],
                                     'vrf': group['vrf'],
                                     'type': group['type'],
                                     'interface': Common.convert_intf_name(group['interface'])})
                continue
        return ret_dict


class ShowBfdIpv6Session(ShowBfdSessionSchema):
    """ Parser for the following commands:
        * show bfd ipv6 neighbors
        * show bfd ipv6 neighbors vrf {vrf}
        * show bfd ipv6 {ipv6_address} neighbors vrf {vrf}

        OurAddr                          NeighAddr
        LD/RD                 RH/RS           Holdown(mult)     State       Int                   Vrf                              Type
        32:1:7::2                        32:1:7::3
        1090519041/1090519061 Up              5917(3)           Up          Po123.7               vxlan-1003                       SH
        32:1:5::2                        32:1:5::3
        1090519045/1090519071 Up              5917(3)           Up          Po123.5               vxlan-1003                       SH
        32:1:6::2                        32:1:6::3
        1090519046/1090519078 Up              5917(3)           Up          Po123.6               vxlan-1003                       SH
        11:11:2::1                       11:11:6::1
        1090519053/1090519050 Up              648(3)            Up          Lo12                  vxlan-1004                       MH
        11:11:2::1                       11:11:5::1
        1090519056/1090520662 Up              523(3)            Up          Lo13                  vxlan-1005                       MH
        node02#
    """

    cli_command = ['show bfd ipv6 neighbors',
                   'show bfd ipv6 neighbors vrf {vrf}',
                   'show bfd ipv6 {ipv6_address} neighbors vrf {vrf}']

    def cli(self, vrf='', ipv6_address=None, output=None):
        if output is None:
            # execute command to get output
            if vrf:
                if ipv6_address:
                    out = self.device.execute(self.cli_command[2].format(
                        vrf=vrf, ipv6_address=ipv6_address))
                else:
                    out = self.device.execute(
                        self.cli_command[1].format(vrf=vrf))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # initial variables
        ret_dict = {}

        # regex pattern for
        # 2001:db8:12::1                   2001:db8:12::2
        p1 = re.compile(r'^(?P<our_address>[0-9A-Fa-f]+:[0-9A-Fa-f:]+)\s+(?P<our_neighbor>'
                        '[0-9A-Fa-f]+:[0-9A-Fa-f:]+)$')

        # 1090519054/1090519043 Up              6000(3)           Up          Eth1/35               default                          SH
        p2 = re.compile(r'^(?P<ld_rd>\d+\/\d+)\s+(?P<rh_rs>\w+)\s+(?P<holdown_timer>N\/A|\d+)\((?P<holdown_timer_multiplier>\d+)\)\s+(?P<state>\S+)\s+(?P<interface>\S+)\s+(?P<vrf>\S+)\s+(?P<type>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            # match line for p1
            # 2001:db8:12::1                   2001:db8:12::2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                our_address = group['our_address']
                our_neighbor = group['our_neighbor']
                continue
            # match line for p2
            # 1090519054/1090519043 Up              6000(3)           Up          Eth1/35               default
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if group['vrf']:
                    vrf = ret_dict.setdefault('vrf', {}). \
                        setdefault(group['vrf'], {})
                    our_address = vrf.setdefault(
                        'our_address', {}).setdefault(our_address, {})
                    our_neighbor = our_address.setdefault(
                        'neighbor_address', {}).setdefault(our_neighbor, {})
                    our_neighbor.update({'ld_rd': group['ld_rd'],
                                         'rh_rs': group['rh_rs'],
                                         'holdown_timer': group['holdown_timer'],
                                         'holdown_timer_multiplier': int(group['holdown_timer_multiplier']),
                                         'state': group['state'],
                                         'vrf': group['vrf'],
                                         'type': group['type'],
                                         'interface': Common.convert_intf_name(group['interface'])})
                continue
        return ret_dict
