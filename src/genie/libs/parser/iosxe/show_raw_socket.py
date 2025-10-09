####################################################################################
# show_raw_socket_tcp.py
#
# Copyright (c) 2024-2025 by cisco Systems, Inc.
# All rights reserved.
####################################################################################
""" show_raw_socket_tcp.py
   supported commands:
     * show raw-socket tcp sessions
     * show raw-socket tcp statistic
"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional, Any, ListOf
from genie.libs.parser.utils.common import Common
# ===========================================
# Parser for 'show raw-socket tcp sessions'
# ===========================================
class ShowRawSocketTcpSessionsSchema(MetaParser):
    """Schema for show raw-socket tcp sessions """
    schema = {
        'sockets': {
            int: {
                'interface': str,
                'tty': int,
                Optional('vrf'): str,
                'mode': str,
                'localip': str,
                'localport': int,
                'destip': str,
                'destport': Any(),
                'uptime': Any(),
                'idletime': Any(),
                'timeout_value': Any(),
                'timeout_units': str
            }
        }
    }
class ShowRawSocketTcpSessions(ShowRawSocketTcpSessionsSchema):

    """Parser for show raw-socket tcp sessions """

    cli_command = 'show raw-socket tcp sessions'
    
    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        ret_dict = {}
        # Pattern for parsing a valid ip address X.X.X.X (x in range of 0-255)
        ip_expression = r"((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"
        
        # Pattern for parsing raw socket tcp session
        # Interface   tty/(Idx)     vrf_name           socket   mode    local_ip_addr  local_port    dest_ip_addr  dest_port    up_time     idle_time/timeout
        # Se0/3/0      50                                 0    server        73.1.1.2     5000          listening     ----      -----            ----- 
        # 0/3/0        50                                 1    server        73.1.1.2     5000           73.1.1.1     4000     00:01:00      00:01:00/300sec
        p1 = re.compile(r'(?P<interface>(\S+))\s*\(?\s*?(?P<tty>(\d+))\)?\s+?(?P<vrf>(\w+|\d+|\S+))?\s+?(?P<socket_index>(\d+))\s*(?P<mode>(\S+))\s*(?P<localip>(%s))\s*(?P<localport>(\d+))\s*(?P<destip>(\S+|%s))\s*(?P<destport>(\d+|[-]+))\s*(?P<uptime>(\S+|[-]+))\s*(?P<idletime>(\S+|[-]+))'%(ip_expression,ip_expression))
        
        for line in out.splitlines():
            line = line.strip()
            # Matching line like 
            # 0/3/0        50                                 1    server        73.1.1.2     5000           73.1.1.1     4000     00:01:00      00:01:00/300sec
            m = p1.match(line)
            if m:
                group = m.groupdict()
                # Socket index
                socket_idx = int(group['socket_index'])
                # Create socket dictionary with index as the key
                socket_dict = ret_dict.setdefault('sockets',{}).setdefault(socket_idx,{})
                # Interface of the socket
                socket_dict['interface'] = group['interface']
                # Socket mode (server/client)
                socket_dict['mode'] = group['mode']
                # TTY number of socket
                socket_dict['tty'] = int(group['tty'])
                # Destination IP address of socket
                socket_dict['destip'] = group['destip']
                # Destination port of socket
                socket_dict['destport'] = group['destport']
                # Local IP address of socket
                socket_dict['localip'] = group['localip']
                # Local port of socket
                socket_dict['localport'] = int(group['localport'])
                # Uptime of socket
                socket_dict['uptime'] = group['uptime']
                # Idle time of socket
                socket_dict['idletime'] = str(group['idletime'])
                # If loop to check if idle time is represented as idle time/timeout 
                # If yes, then split the idle time and timeout value and units
                # This if block only populates the timeout value and continue is not
                # required in this block as the loop will skip next value. 
                if '/' in socket_dict['idletime']:
                    # Splitting the timeout value and units
                    timeouts = socket_dict['idletime'].split('/')
                    # idle timeout value after splitting
                    socket_dict['idletime'] = timeouts[0]
                    # parsing the idle timeout further to get the timeout value and units
                    timeoutresult=re.search(r'(\d+)(\S+)',timeouts[1])
                    # timeout value
                    socket_dict['timeout_value'] = int(timeoutresult.group(1))
                    # timeout units
                    socket_dict['timeout_units'] = timeoutresult.group(2)
                else:
                    # idle time is same as timeout value and units without any split
                    socket_dict['idletime'] = group['idletime']
                    # timeout value is same as idle time
                    socket_dict['timeout_value'] = group['idletime']
                    # timeout units is same as idle time
                    socket_dict['timeout_units'] = group['idletime']
                # If VRF is present, then add it to the socket dictionary.
                # This if block only populates the vrf value and continue is not
                # required in this block as the loop will skip next value.     
                if group['vrf']:
                    # VRF of the socket
                    socket_dict['vrf'] = group['vrf']
                continue
        return ret_dict
    
# ===========================================
# Parser for 'show raw-socket tcp statistic'
# ===========================================
class ShowRawSocketTcpStatisticSchema(MetaParser):
    """Schema for show raw-socket tcp statistic """
    schema = {
        'socketidx': {
            int: {
                'interface': str,
                Optional('vrf'): str,
                'sessions': int,
                'tcp_in_bytes': int,
                'tcp_out_bytes': int,
                'tcp_to_tty_frames': int,
                'tty_to_tcp_frames': int
            }
        }
    }
class ShowRawSocketTcpStatistic(ShowRawSocketTcpStatisticSchema):
    """Parser for show raw-socket tcp statistic """

    cli_command = 'show raw-socket tcp statistic'
    
    def cli(self, output=None):
        
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Pattern for parsing raw socket tcp statistics
        # Interface  idx             vrf_name             sessions      tcp_in_bytes         tcp_out_bytes   tcp_to_tty_frames    tty_to_tcp_frames
        # Lo1        35                                       1                 123                 3338                   5                   33 
        p1 = re.compile(r'(?P<interface>(\S+))\s*(?P<idx>(\d+))\s+(?P<vrf>(\S+))?\s+(?P<sessions>(\d+))\s+(?P<tcp_in_bytes>(\d+))\s+(?P<tcp_out_bytes>(\d+))\s+(?P<tcp_to_tty_frames>(\d+))\s+(?P<tty_to_tcp_frames>(\d+))')
        for line in out.splitlines():
             line = line.strip()
             # Match line like:
             #   Se0/3/0        35                                       1                 123                 3338                   5                   33 
             m = p1.match(line)
             if m:
                group = m.groupdict()
                # Socket index of the socket
                socket_idx = int(group['idx'])
                # Create socket dictionary with socket index as the key
                socket_dict = ret_dict.setdefault('socketidx',{}).setdefault(socket_idx,{})
                # Interface of the socket
                socket_dict['interface'] = group['interface']
                # Sessions of the socket
                socket_dict['sessions'] = int(group['sessions'])
                # TCP in bytes of the socket
                socket_dict['tcp_in_bytes'] = int(group['tcp_in_bytes'])
                # TCP out bytes of the socket
                socket_dict['tcp_out_bytes'] = int(group['tcp_out_bytes'])
                # TCP to tty frames of the socket
                socket_dict['tcp_to_tty_frames'] = int(group['tcp_to_tty_frames'])
                # TTY to TCP frames of the socket
                socket_dict['tty_to_tcp_frames'] = int(group['tty_to_tcp_frames'])
                # If VRF is present, then add it to the socket dictionary.
                # This if block only populates the vrf value and continue is not
                # required in this block as the loop will skip next value.
                if group['vrf']:
                    socket_dict['vrf'] = group['vrf']
                continue
        return ret_dict

# ===============================================
# Parser for 'show raw-socket tcp sessions local'
# ===============================================
class ShowRawSocketTcpSessionsLocalSchema(MetaParser):
    """Schema for show raw-socket tcp sessions local """
    schema = {
        'tty': {
            int:  ListOf (
                {
                    'interface': str,
                    'destip': str,
                    'destport': int,
                    'localip': str,
                    'localport': int,
                    'state': str
                }
            )
        }
    }
class ShowRawSocketTcpSessionsLocal(ShowRawSocketTcpSessionsLocalSchema):

    """Parser for show raw-socket tcp sessions local """

    cli_command = 'show raw-socket tcp sessions local'
    
    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        # Pattern for parsing a valid ip address X.X.X.X (x in range of 0-255)
        ip_expression = r"((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"
        
        # Pattern for parsing raw socket tcp session local
        # ------------------- Locally configured TCP client State --------------------
        #Interface  tty  dest_ip         dest_port  local_ip        local_port  state
        #Lo7        49   40.1.1.1          5000     50.1.1.1          4000      UP
        #Lo7        49   40.1.1.1          5001     50.1.1.1          4010      UP 
        p1 = re.compile(r'(?P<interface>(\S+))\s*(?P<tty>(\d+))\s*(?P<destip>(%s))\s*(?P<destport>(\d+))\s*(?P<localip>(%s))\s*(?P<localport>(\d+))\s*(?P<state>(\S+))'%(ip_expression,ip_expression))
        
        for line in out.splitlines():

            line = line.strip()
            # Matching line like 
            # Lo7        49   40.1.1.1          5000     50.1.1.1          4000      UP
            m = p1.match(line)
            if m:
                group = m.groupdict()
                # tty index
                tty_idx = int(group['tty'])
                # Create socket tty list with tty index as the key
                socket_dict = ret_dict.setdefault('tty',{}).setdefault(tty_idx,[])
                # Creating a tty dictionary 
                tty_dict = {}
                # Interface of the socket
                tty_dict['interface'] = group['interface']
                # Destination IP address of socket
                tty_dict['destip'] = group['destip']
                # Destination port of socket
                tty_dict['destport'] = int(group['destport'])
                # Local IP address of socket
                tty_dict['localip'] = group['localip']
                # Local port of socket
                tty_dict['localport'] = int(group['localport'])
                # Uptime of socket
                tty_dict['state'] = group['state']
                # updating the list to specific tty index
                socket_dict.append(tty_dict)
                continue

        return ret_dict
