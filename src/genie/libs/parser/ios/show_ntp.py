"""show_ntp.py

IOS parsers for the following show commands:

    * show ntp associations
    * show ntp status
    * show ntp config

"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or
# import iosxe parser
from genie.libs.parser.iosxe.show_ntp import ShowNtpAssociationsDetail as ShowNtpAssociationsDetail_iosxe,\
                                             ShowNtpStatus as ShowNtpStatus_iosxe

# ==============================================
#  Schema for show ntp associations
# ==============================================
class ShowNtpAssociationsSchema(MetaParser):
    """Schema for show ntp associations"""

    schema = {
        'peer': {
            Any(): {
                'local_mode': {
                    Any(): {
                        'remote': str,
                        'configured': bool,
                        Optional('refid'): str,
                        Optional('local_mode'): str,
                        Optional('stratum'): int,
                        Optional('receive_time'): Or(str, int),
                        Optional('poll'): int,
                        Optional('reach'): int,
                        Optional('delay'): float,
                        Optional('offset'): float,
                        Optional('jitter'): float,
                        'mode': str,
                    },
                }
            },
        },
        'clock_state': {
            'system_status': {
                'clock_state': str,
                Optional('clock_stratum'): int,
                Optional('associations_address'): str,
                Optional('root_delay'): float,
                Optional('clock_offset'): float,
                Optional('clock_refid'): str,
                Optional('associations_local_mode'): str,
            }
        }
    }


# ==============================================
#  Parser for show ntp associations
# ==============================================
class ShowNtpAssociations(ShowNtpAssociationsSchema):
    """Parser for show ntp associations"""

    # * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
    MODE_MAP = {'*': 'synchronized',
                '#': 'selected',
                'x': 'falseticker',
                '+': 'candidate',
                '-': 'outlyer',
                None: 'unsynchronized'}

    cli_command = 'show ntp associations'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}

        #   address         ref clock       st   when   poll reach  delay  offset   disp
        # *~127.127.1.1     .LOCL.           0      6     16   377  0.000   0.000  1.204
        #  ~10.4.1.1        .INIT.          16      -   1024     0  0.000   0.000 15937.
        # +~10.16.2.2       127.127.1.1      8    137     64     1 15.917 556.786 7938.0
        p1 = re.compile(r'^(?P<mode_code>[x\*\#\+\- ])?(?P<configured>[\~])? *(?P<remote>[\w\.\:]+) +'
                        '(?P<refid>[\w\.]+) +(?P<stratum>\d+) +'
                        '(?P<receive_time>[\d\-]+) +(?P<poll>\d+) +'
                        '(?P<reach>\d+) +(?P<delay>[\d\.]+) +'
                        '(?P<offset>[\d\.\-]+) +(?P<disp>[\d\.\-]+)$')

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # *172.16.229.65     .GNSS.           1 -   59   64  377    1.436   73.819  10.905
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                peer = groups['remote']
                if '~' is groups['configured']:
                    configured = True
                else:
                    configured = False
                local_mode = 'client'
                mode = self.MODE_MAP.get(groups['mode_code'])
                try:
                    receive_time = int(groups['receive_time'])
                except:
                    receive_time = str(groups['receive_time'])

                peer_dict = ret_dict.setdefault('peer', {}).setdefault(peer, {})\
                    .setdefault('local_mode', {}).setdefault(local_mode, {})
                peer_dict.update({'remote': peer,
                                  'configured': configured,
                                  'refid': groups['refid'],
                                  'local_mode': local_mode,
                                  'mode': mode,
                                  'stratum': int(groups['stratum']),
                                  'receive_time': receive_time,
                                  'poll': int(groups['poll']),
                                  'reach': int(groups['reach']),
                                  'delay': float(groups['delay']),
                                  'offset': float(groups['offset']),
                                  'jitter': float(groups['disp'])})

                # ops clock_state structure
                if groups['mode_code']:
                    if '*' in groups['mode_code']:
                        clock_dict = ret_dict.setdefault('clock_state', {}).setdefault('system_status', {})
                        clock_dict['clock_state'] = mode
                        clock_dict['clock_stratum'] = int(groups['stratum'])
                        clock_dict['associations_address'] = peer
                        clock_dict['root_delay'] = float(groups['delay'])
                        clock_dict['clock_offset'] = float(groups['offset'])
                        clock_dict['clock_refid'] = groups['refid']
                        clock_dict['associations_local_mode'] = local_mode
                    else:
                        clock_dict = ret_dict.setdefault('clock_state', {}).setdefault('system_status', {})
                        clock_dict['clock_state'] = 'unsynchronized'

        # check if has synchronized peers, if no create unsynchronized entry
        if ret_dict and not ret_dict.get('clock_state'):
            ret_dict.setdefault('clock_state', {}).setdefault('system_status', {})\
                .setdefault('clock_state', 'unsynchronized')

        return ret_dict


# ==============================================
# Parser for 'show ntp status'
# ==============================================
class ShowNtpStatus(ShowNtpStatus_iosxe):
    """Parser for: show ntp status"""
    pass


# =========================================================
# Parser for 'show ntp config'
# =========================================================
class ShowNtpConfigSchema(MetaParser):
    """Schema for: show ntp config"""

    schema = {
        'vrf': {
            Any(): {
                'address': {
                    Any(): {
                        'type': {
                            Any(): {
                                'address': str,
                                'type': str,
                                'vrf': str,
                                Optional('source'): str,
                            }
                        },
                        'isconfigured': {
                            Any(): {
                                'address': str,
                                'isconfigured': bool,
                            }
                        }

                    }
                }
            }
        }
    }


class ShowNtpConfig(ShowNtpConfigSchema):
    """Parser for: show ntp config"""

    cli_command = 'show ntp config'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}

        # R1#show ntp config
        # ntp server 10.4.1.1
        # ntp server 10.16.2.2
        # ntp server vrf VRF1 10.64.4.4
        # ntp server 10.16.2.2 source Loopback0

        p1 = re.compile(r"^ntp +(?P<type>\w+)( +vrf +(?P<vrf>[\d\w]+))? "
                        "+(?P<address>[\w\.\:]+)( +source +(?P<source_interface>[\w]+))?$")

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            m = p1.match(line)
            if m:
                groups = m.groupdict()
                vrf = groups['vrf'] or 'default'
                ntp_type = groups['type']
                address = groups['address']
                source = groups['source_interface'] or ''
                isconfigured = True

                addr_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {})\
                    .setdefault('address', {}).setdefault(address, {})

                addr_dict.setdefault('type', {}).setdefault(ntp_type, {}).update({'address': address,
                                                                                  'type': ntp_type,
                                                                                  'vrf': vrf})
                if source:
                    addr_dict['type'][ntp_type]['source'] = source

                addr_dict.setdefault('isconfigured', {}).\
                    setdefault(str(isconfigured), {}).update({'address': address,
                                                              'isconfigured': isconfigured})

        return ret_dict


# ==============================================
#  Parser for show ntp associations detail
# ==============================================
class ShowNtpAssociationsDetail(ShowNtpAssociationsDetail_iosxe):
    """Parser for show ntp associations detail"""
    pass