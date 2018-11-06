"""show_ntp.py

NXOS parsers for the following show commands:

    * show ntp peer-status
    * show ntp peers

"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# import parser utils
from genie.libs.parser.utils.common import Common


# ==============================================
#  Schema for show ntp peer-status
# ==============================================
class ShowNtpPeerStatusSchema(MetaParser):
    """Schema for show ntp peer-status"""

    schema = {
        'total_peers': int,
        'peer': {
            Any():{
                Optional('clock_state'): str,
                'mode': str,
                'remote': str,
                'local': str,
                'stratum': int,
                'poll': int,
                'reach': int,
                'delay': float,
                Optional('vrf'): str,
            }
        },
        'clock_state': {
            'system_status': {
                'clock_state': str,
                'clock_stratum': int,
                'associations_address': str,
                'associations_local_mode': str,
                'root_delay': float,
            }
        }
    }

# ==============================================
#  Parser for show ntp peer-status
# ==============================================
class ShowNtpPeerStatus(ShowNtpPeerStatusSchema):
    """Parser for show ntp peer-status"""

    MODE_MAP = {'*': 'synchronized',
                '+': 'active',
                '-': 'passive',
                '=': 'polled in client',
                None: 'unsynchronized'}

    def cli(self):

        # execute command to get output
        out = self.device.execute('show ntp peer-status')

        # initial variables
        ret_dict = {}

        # patterns

        # Total peers : 4
        p1 = re.compile(r'^Total +peers *: +(?P<total_peer>\d+)$')

        #     remote                                 local                                   st   poll   reach delay   vrf
        # *1.1.1.1                                  0.0.0.0                                   8   16     377   0.01311 default

        #    remote               local                 st   poll   reach delay   vrf
        # =127.127.1.0            10.100.100.1            8   64       0   0.00000
        p2 = re.compile(r'^(?P<mode_code>[\*\-\+\=]+)? *(?P<remote>[\w\.\:]+) +'
                         '(?P<local>[\w\.\:]+) +(?P<st>\d+) +'
                         '(?P<poll>\d+) +(?P<reach>\d+) +(?P<delay>[\w\.]+)'
                         '( *(?P<vrf>\S+))?$')


        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # Total peers : 4
            m = p1.match(line)
            if m:
                ret_dict['total_peers'] = int(m.groupdict()['total_peer'])

            # *1.1.1.1                                  0.0.0.0                                   8   16     377   0.01311 default
            # =127.127.1.0            10.100.100.1            8   64       0   0.00000
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                peer = groups['remote']
                peer_dict = ret_dict.setdefault('peer', {}).setdefault(peer, {})
                mode = self.MODE_MAP.get(groups['mode_code'])
                peer_dict['mode'] = mode
                peer_dict['remote'] = peer
                peer_dict['local'] = groups['local']
                peer_dict['stratum'] = int(groups['st'])
                peer_dict['poll'] = int(groups['poll'])
                peer_dict['reach'] = int(groups['reach'])
                peer_dict['delay'] = float(groups['delay'])
                if groups['vrf']:
                    peer_dict['vrf'] = groups['vrf']

                # ops clock_state structure
                if 'sync' in mode:
                    clock_dict = ret_dict.setdefault('clock_state', {}).setdefault('system_status', {})
                    clock_dict['clock_state'] = mode
                    clock_dict['clock_stratum'] = int(groups['st'])
                    clock_dict['associations_address'] = peer
                    clock_dict['associations_local_mode'] = mode
                    clock_dict['root_delay'] = float(groups['delay'])

        return ret_dict


# ==============================================
# Parser for 'show ntp peers'
# ==============================================

class ShowNtpPeersSchema(MetaParser):
    """Schema for: show ntp peers"""

    schema = {
        'peer': {
            Any():{
                'address': str,
                'type': str,
                'isconfigured': bool
            }
        }
    }

class ShowNtpPeers(ShowNtpPeersSchema):
    """Parser for: show ntp peers"""

    def cli(self):

        # excute command to get output
        out = self.device.execute('show ntp peers')

        # initial variables
        ret_dict = {}

        # 10.100.4.156                  Peer (configured)
        # 10.1.0.63                     Server (configured)
        p1 = re.compile(r'^(?P<peer>[\w\.\:]+) +(?P<type>\w+)( *\((?P<conf>configured)\))?$')

        for line in out.splitlines():
            line = line.strip()
            if not line: 
                continue

            m = p1.match(line)
            if m:
                groups = m.groupdict()
                address = groups['peer']
                peer_dict = ret_dict.setdefault('peer', {}).setdefault(address, {})
                peer_dict['address'] = address
                peer_dict['type'] = groups['type'].lower()
                peer_dict['isconfigured'] = 'configured' in str(groups['conf'])
                continue

        return ret_dict
