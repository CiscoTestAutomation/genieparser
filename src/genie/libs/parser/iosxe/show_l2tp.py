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
        # 2311074340 2784131943 fsw-TSN-2     est    150.0.0.1       1      l2tp_default_class
        p2 = re.compile(r'^(?P<loc_tunnel_id>\d+)\s+(?P<rem_tunnel_id>\d+)\s+(?P<remote_name>\S+)\s+(?P<state>\S+)\s+(?P<remote_address>\d+\.\d+\.\d+\.\d+)\s+(?P<sessions>\d+)\s+(?P<l2tp_class>\S+)(?:\s*|$)')
        
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

# =======================================================
# Schema for 'show l2tp'
# =======================================================
class ShowL2tpSchema(MetaParser):
    """Schema for show l2tp"""

    schema = {
        'total_tunnels': int,
        'total_sessions': int,
        Optional('tunnels'): {
            Any(): {
                'loc_tunnel_id': int,
                'rem_tunnel_id': int,
                'remote_name': str,
                'state': str,
                'remote_address': str,
                'session_count': int,
                'l2tp_class_vpdn_group': str,
                Optional('sessions'): {
                    Any(): {
                        'loc_id': int,
                        'rem_id': int,
                        'tunnel_id': int,
                        'username': str,
                        'interface_vcid_circuit': str,
                        'state': str,
                        'last_change': str,
                        'unique_id': int,
                    }
                }
            }
        }
    }


# =======================================================
# Parser for 'show l2tp'
# =======================================================
class ShowL2tp(ShowL2tpSchema):
    """Parser for show l2tp"""

    cli_command = 'show l2tp'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize return dictionary
        ret_dict = {}

        # Regex patterns
        # L2TP Tunnel and Session Information Total tunnels 1 sessions 1
        p1 = re.compile(r'^L2TP Tunnel and Session Information Total tunnels (?P<total_tunnels>\d+) sessions (?P<total_sessions>\d+)$')

        # 3217474068 2611998623 fg4           est    100.3.1.1       1     l2tp_class_1
        p2 = re.compile(
            r'^(?P<loc_tunnel_id>\d+)\s+'
            r'(?P<rem_tunnel_id>\d+)\s+'
            r'(?P<remote_name>\S+)\s+'
            r'(?P<state>\S+)\s+'
            r'(?P<remote_address>\S+)\s+'
            r'(?P<session_count>\d+)\s+'
            r'(?P<l2tp_class_vpdn_group>\S+)$'
        )

        # 2409671146 3648835555 3217474068 101, Gi0/0/0         est    00:00:22 0
        p3 = re.compile(
            r'^(?P<loc_id>\d+)\s+'
            r'(?P<rem_id>\d+)\s+'
            r'(?P<tunnel_id>\d+)\s+'
            r'(?P<username>[^,]+),\s+'
            r'(?P<interface_vcid_circuit>\S+)\s+'
            r'(?P<state>\S+)\s+'
            r'(?P<last_change>\S+)\s+'
            r'(?P<unique_id>\d+)$'
        )

        current_tunnel_id = None
        session_counter = {}

        for line in output.splitlines():
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Parse total tunnels and sessions
            # L2TP Tunnel and Session Information Total tunnels 1 sessions 1
            m = p1.match(line)
            if m:
                ret_dict['total_tunnels'] = int(m.group('total_tunnels'))
                ret_dict['total_sessions'] = int(m.group('total_sessions'))
                continue

            # Parse tunnel information
            # 3217474068 2611998623 fg4           est    100.3.1.1       1     l2tp_class_1
            m = p2.match(line)
            if m:
                tunnel_id = m.group('loc_tunnel_id')
                current_tunnel_id = tunnel_id
                session_counter[tunnel_id] = 0
                
                tunnels_dict = ret_dict.setdefault('tunnels', {})
                tunnel_dict = tunnels_dict.setdefault(tunnel_id, {})
                
                tunnel_dict['loc_tunnel_id'] = int(m.group('loc_tunnel_id'))
                tunnel_dict['rem_tunnel_id'] = int(m.group('rem_tunnel_id'))
                tunnel_dict['remote_name'] = m.group('remote_name')
                tunnel_dict['state'] = m.group('state')
                tunnel_dict['remote_address'] = m.group('remote_address')
                tunnel_dict['session_count'] = int(m.group('session_count'))
                tunnel_dict['l2tp_class_vpdn_group'] = m.group('l2tp_class_vpdn_group')
                continue

            # Parse session information
            # 2409671146 3648835555 3217474068 101, Gi0/0/0         est    00:00:22 0
            m = p3.match(line)
            if m and current_tunnel_id:
                tunnel_id_from_session = m.group('tunnel_id')
                
                # Find the correct tunnel for this session
                tunnel_key = None
                for t_key, t_data in ret_dict.get('tunnels', {}).items():
                    if str(t_data['loc_tunnel_id']) == tunnel_id_from_session:
                        tunnel_key = t_key
                        break
                
                if tunnel_key:
                    session_counter.setdefault(tunnel_key, 0)
                    session_counter[tunnel_key] += 1
                    session_key = f"session_{session_counter[tunnel_key]}"
                    
                    sessions_dict = ret_dict['tunnels'][tunnel_key].setdefault('sessions', {})
                    session_dict = sessions_dict.setdefault(session_key, {})
                    
                    session_dict['loc_id'] = int(m.group('loc_id'))
                    session_dict['rem_id'] = int(m.group('rem_id'))
                    session_dict['tunnel_id'] = int(m.group('tunnel_id'))
                    session_dict['username'] = m.group('username').strip()
                    session_dict['interface_vcid_circuit'] = m.group('interface_vcid_circuit')
                    session_dict['state'] = m.group('state')
                    session_dict['last_change'] = m.group('last_change')
                    session_dict['unique_id'] = int(m.group('unique_id'))
                continue

        return ret_dict
