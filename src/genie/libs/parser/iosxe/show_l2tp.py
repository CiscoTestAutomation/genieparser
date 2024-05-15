"""
show_l2tp.py
"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional
# import parser utils
from genie.libs.parser.utils.common import Common

class ShowL2tpTunnelSchema(MetaParser):

    """Schema for show subscriber session"""

    schema = {
        Optional('total_tunnels'): int,
        Optional('sessions'): int,
        Optional('tunnels'): {
            Any(): {
                Optional('loc_tunnel_id'): int,
                Optional('rem_tunnel_id'): int,
                Optional('remote_name'): str,
                Optional('state'): str,
                Optional('remote_address'): str,
                Optional('l2tp_class'): str,
            },
        },
        Optional('no_active_tunnels'): str,
    }

# ==============================
# Parser for 'show l2tp tunnel'
# ==============================

# The parser class inherits from the schema class
class ShowL2tpTunnel(ShowL2tpTunnelSchema):

    ''' Parser for "show l2tp tunnel"'''
    cli_command = 'show l2tp tunnel'

    # Defines a function to run the cli_command
    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)


        # Initializes the Python dictionary variable
        parsed_dict = {}
        var=1

        # L2TP Tunnel Information Total tunnels 1 sessions 16
        p1 = re.compile(r'L2TP\s+Tunnel\s+Information\s+Total\s+tunnels\s+(?P<total_tunnels>\d+)\s+sessions\s+(?P<sessions>\d+)')

        # LocTunID   RemTunID   Remote Name   State  Remote Address  Sessn L2TP Class/
        # 11367      26859      LAC           est    99.1.1.1        16    airtel
        p2=re.compile(r'^(?P<loc_tunnel_id>\d+)\s+(?P<rem_tunnel_id>\d+)\s+(?P<remote_name>\w+)\s+(?P<state>\w+)\s+(?P<remote_address>\d+\.\d+\.\d+\.\d+)\s+\d+\s+(?P<l2tp_class>\w+)$')

        #%%No active L2TP tunnels
        p3=re.compile(r'^%%(?P<no_active_tunnels>(No\s+active\s+L2TP\s+tunnels))$')

        for line in output.splitlines():
            line = line.strip()

            # Processes the matched patterns for the first line of output
            m = p1.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['total_tunnels'] = int(group['total_tunnels'])
                parsed_dict['sessions'] = int(group['sessions'])
                continue

            m = p2.match(line)
            if m:
                parsed_dict.setdefault('tunnels', {})
                parsed_dict['tunnels'].setdefault(var, {})
                group = m.groupdict()
                parsed_dict['tunnels'][var]['loc_tunnel_id'] = int(group['loc_tunnel_id'])
                parsed_dict['tunnels'][var]['rem_tunnel_id'] = int(group['rem_tunnel_id'])
                parsed_dict['tunnels'][var]['remote_name'] = str(group['remote_name'])
                parsed_dict['tunnels'][var]['state'] = str(group['state'])
                parsed_dict['tunnels'][var]['remote_address'] = str(group['remote_address'])
                parsed_dict['tunnels'][var]['l2tp_class'] = str(group['l2tp_class'])
                var+=1
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['no_active_tunnels'] = str(group['no_active_tunnels'])

        return parsed_dict


class ShowL2tpSessionPacketsSchema(MetaParser):

    """Schema for show subscriber session"""

    schema = {
        Optional('total_tunnels'): int,
        Optional('total_sessions'): int,
        Optional('sessions'): {
            Any(): {
                Optional('loc_id'): int,
                Optional('rem_id'): int,
                Optional('tunnel_id'): int,
                Optional('packets_in'): int,
                Optional('packets_out'): int,
                Optional('bytes_in'): int,
                Optional('bytes_out'): int,
            },
        },
        Optional('no_active_tunnels'): str,
    }

# ==============================
# Super Parser for:
#   * 'show l2tp session packets',
#   * 'show l2tp session packets vcid',
# ==============================
class ShowL2tpSessionPacketsSuperParser(ShowL2tpSessionPacketsSchema):

    ''' Super Parser for
        * 'show l2tp session packets',
        * 'show l2tp session packets vcid',
    '''

    # Defines a function to run the cli_command
    def cli(self, vcid='', output=None):

        # Initializes the Python dictionary variable
        parsed_dict = {}
        index = 1

        # L2TP Session Information Total tunnels 8000 sessions 8000
        p1 = re.compile(r'L2TP\s+Session\s+Information\s+Total\s+tunnels\s+(?P<total_tunnels>\d+)\s+sessions\s+(?P<total_sessions>\d+)')

        # LocID      RemID      TunID      Pkts-In    Pkts-Out   Bytes-In   Bytes-Out
        # 507155526  4194000749 609164     182805     183322     181342560  182588712
        p2 = re.compile(r'^(?P<loc_id>\d+)\s+(?P<rem_id>\d+)\s+(?P<tunnel_id>\w+)\s+'
                        r'(?P<packets_in>\w+)\s+(?P<packets_out>\w+)\s+'
                        r'(?P<bytes_in>\w+)\s+(?P<bytes_out>\w+)$')

        #%%No active L2TP tunnels
        p3=re.compile(r'^%%(?P<no_active_tunnels>(No\s+active\s+L2TP\s+tunnels))$')

        for line in output.splitlines():
            line = line.strip()

            # L2TP Session Information Total tunnels 8000 sessions 8000
            m = p1.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['total_tunnels'] = int(group['total_tunnels'])
                parsed_dict['total_sessions'] = int(group['total_sessions'])
                continue

            # LocID      RemID      TunID      Pkts-In    Pkts-Out   Bytes-In   Bytes-Out
            # 507155526  4194000749 609164     182805     183322     181342560  182588712
            m = p2.match(line)
            if m:
                index_dict = parsed_dict.setdefault('sessions', {}).setdefault(index, {})
                group = m.groupdict()
                index_dict['loc_id'] = int(group['loc_id'])
                index_dict['rem_id'] = int(group['rem_id'])
                index_dict['tunnel_id'] = int(group['tunnel_id'])
                index_dict['packets_in'] = int(group['packets_in'])
                index_dict['packets_out'] = int(group['packets_out'])
                index_dict['bytes_in'] = int(group['bytes_in'])
                index_dict['bytes_out'] = int(group['bytes_out'])
                index += 1
                continue

            #%%No active L2TP tunnels
            m = p3.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['no_active_tunnels'] = str(group['no_active_tunnels'])

        return parsed_dict

# ===========================================
# Parser for:
#   * 'show l2tp session packets vcid {vcid}'
#   * 'show l2tp session packets'
# ===========================================
class ShowL2tpSessionPackets(ShowL2tpSessionPacketsSuperParser):

    ''' Parser for:
        * 'show l2tp session packets vcid {vcid}'
        * 'show l2tp session packets'
    '''

    cli_command = ['show l2tp session packets vcid {vcid}',
                   'show l2tp session packets',
                   ]

    def cli(self, vcid='', output=None):

        if output is None:
            # Build command
            if vcid:
                cmd = self.cli_command[0].format(vcid=vcid)
            else:
                cmd = self.cli_command[1]
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output)