"""show_lag.py
    supported commands:
    * show feature
    * show lacp system-identifier
    * show lacp counters
    * show lacp neighbor
    * show port-channel summary
    * show port-channel database
"""

# Python
import re
import random

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
    Any, \
    Optional, \
    Or, \
    And, \
    Default, \
    Use

# import parser utils
from genie.libs.parser.utils.common import Common


# ============================
# parser for show feature
# ============================
class ShowFeatureSchema(MetaParser):
    """schema for: show feature"""
    schema = {
        'features': {
            Any(): {
                'instances': {
                    Any(): bool
                }
            }
        }
    }


class ShowFeature(ShowFeatureSchema):
    """parser for show feature"""
    cli_command = 'show feature'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # init dictionary
        parsed_dict = {}
        # bash-shell             1          disabled
        p1 = re.compile(
            r'^(?P<feature_name>[\w-]+)\s+(?P<instance>\d+)\s+(?P<state>('
            r'disabled|enabled))$')

        for line in out.splitlines():
            line = line.strip()
            # bash-shell             1          disabled
            m = p1.match(line)
            if m:
                group = m.groupdict()
                state = True if group['state'] == 'enabled' else False
                sub_dict = parsed_dict.setdefault('features', {}).setdefault(
                    group['feature_name'], {}).setdefault('instances', {})
                sub_dict[group['instance']] = state

                continue
        return parsed_dict


# ============================
# parser for show lacp system-identifier
# ============================
class ShowLacpSystemIdentifierSchema(MetaParser):
    """Schema for show lacp system-identifier"""
    schema = {
        'system_id_mac': str,
        'system_priority': int,
    }


class ShowLacpSystemIdentifier(ShowLacpSystemIdentifierSchema):
    """Parser for :
       show lacp sys-id"""

    cli_command = 'show lacp sys-id'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}
        # 32768,5e-2-0-1-0-7
        p1 = re.compile(r'^\s*(?P<system_priority>[\d]+), *(?P<system_id_mac>[\w\.\-]+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({'system_priority': int(group['system_priority'])})
                parsed_dict.update({'system_id_mac': group['system_id_mac']})
                continue

        return parsed_dict


# ============================
# schema for show lacp counters
# ============================
class ShowLacpCountersSchema(MetaParser):
    """schema for: show lcap counters"""
    schema = {
        'interfaces': {
            Any(): {
                'members': {
                    Any(): {
                        'interface': str,
                        'counters': {
                            'lacp_in_pkts': int,
                            'lacp_out_pkts': int,
                            'lacp_errors': int,
                            'marker_in_pkts': int,
                            'marker_out_pkts': int
                        },
                    },
                }
            },
        },
    }


# =============================
# parser for lacp counters
# ============================
class ShowLacpCounters(ShowLacpCountersSchema):
    """Parser for: show lacp counters"""

    cli_command = 'show lacp counters'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # init return dict
        parsed_dict = {}
        intf_dict = {}
        # port-channel1
        p1 = re.compile(r'^port-channel\d+$')
        # ------------------------------------------------------------------------------
        #                              LACPDUs                      Markers / Resp
        # LACPDUs
        # Port              Sent                Recv                  Recv
        # Sent  Pkts
        # Err
        # ------------------------------------------------------------------------------
        # port - channel1
        # Ethernet1 / 1        92                   85                     0      0   
        # 0      
        # Ethernet1 / 2        79                   87                     0      0   
        # 0      
        #
        # port - channel2
        # Ethernet1 / 3        136                  112                    0      0   
        # 0      
        # Ethernet1 / 4        95                   90                     0      0   
        # 0      
        # Ethernet1 / 5        118                  146                    0      0   
        # 0      
        p2 = re.compile(
            r'^(?P<interface>[\w\/]+) +(?P<lacp_out_pkts>[\d]+) +(?P<lacp_in_pkts>[\d]+)'
            ' +(?P<marker_in_pkts>[\d]+) +(?P<marker_out_pkts>[\d]+) +( +('
            '?P<lacp_pkts_errors>[\d]+))?$')

        for line in out.splitlines():
            if line:
                line = line.strip().replace('\xa0', ' ')
            else:
                continue

            # port-channel1
            m = p1.match(line)
            if m:
                intf_dict = parsed_dict.setdefault('interfaces', {}).setdefault(m.group(),
                                                                                {})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group["interface"])
                member_dict = intf_dict.setdefault('members', {}).setdefault(interface,
                                                                             {})
                member_dict.update({'interface': interface})
                counter_dict = member_dict.setdefault('counters', {})
                counter_dict.update({'lacp_in_pkts': int(group['lacp_in_pkts'])})
                counter_dict.update({'lacp_out_pkts': int(group['lacp_out_pkts'])})
                counter_dict.update({'marker_in_pkts': int(group['marker_in_pkts'])})
                counter_dict.update({'marker_out_pkts': int(group['marker_out_pkts'])})
                counter_dict.update({'lacp_errors': int(group['lacp_pkts_errors'])})
                continue

        return parsed_dict
