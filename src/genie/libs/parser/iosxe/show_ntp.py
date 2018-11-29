"""show_ntp.py

IOSXE parsers for the following show commands:

    * show ntp associations
    * show ntp status
    * show ntp config

"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or


# ==============================================
#  Schema for show ntp associations
# ==============================================
class ShowNtpAssociationsSchema(MetaParser):
    """Schema for show ntp associations"""

    schema = {
        'peer': {
            Any():{
                'local_mode': {
                    Any(): {
                        'remote': str,
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
    MODE_MAP = {'*': 'sys.peer',
                '#': 'selected',
                'x': 'falseticker',
                '+': 'candidate',
                '-': 'outlyer',
                '~': 'configured',
                '*~': 'synchronized',
                None: 'unsynchronized'}

    def cli(self):

        # execute command to get output
        out = self.device.execute('show ntp associations')

        # initial variables
        ret_dict = {}

        #   address         ref clock       st   when   poll reach  delay  offset   disp
        # *~127.127.1.1     .LOCL.           0      6     16   377  0.000   0.000  1.204
        # ~1.1.1.1         .INIT.          16      -   1024     0  0.000   0.000 15937.
        p1 = re.compile(r'^(?P<mode_code>[x\*\#\+\-\~]+)? *(?P<remote>[\w\.\:]+) +'
                         '(?P<refid>[\w\.]+) +(?P<stratum>\d+) +'
                         '(?P<receive_time>[\d\-]+) +(?P<poll>\d+) +'
                         '(?P<reach>\d+) +(?P<delay>[\d\.]+) +'
                         '(?P<offset>[\d\.\-]+) +(?P<disp>[\d\.\-]+)$')


        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # *171.68.38.65     .GNSS.           1 -   59   64  377    1.436   73.819  10.905
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                peer = groups['remote']
                local_mode = 'client'
                mode = self.MODE_MAP.get(groups['mode_code'])
                try:
                    receive_time = int(groups['receive_time'])
                except:
                    receive_time = str(groups['receive_time'])

                peer_dict = ret_dict.setdefault('peer', {}).setdefault(peer, {})\
                    .setdefault('local_mode', {}).setdefault(local_mode, {})
                peer_dict.update({'remote': peer,
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

class ShowNtpStatusSchema(MetaParser):
    """Schema for: show ntp status"""

    schema = {
        'clock_state': {
            'system_status': {
                'status': str,
                Optional('stratum'): int,
                Optional('refid'): str,
                Optional('nom_freq'): float,
                Optional('act_freq'): float,
                Optional('precision'): Or(int,str),
                Optional('uptime'): str,
                Optional('resolution'): int,
                Optional('reftime'): str,
                Optional('offset'): float,
                Optional('rootdelay'): float,
                Optional('rootdispersion'): float,
                Optional('peerdispersion'): float,
                Optional('leap_status'): str,
                Optional('drift'): str,
                Optional('poll'): int,
                Optional('last_update'): str,
            }
        }
    }


class ShowNtpStatus(ShowNtpStatusSchema):
    """Parser for: show ntp status"""

    def cli(self):

        # excute command to get output
        out = self.device.execute('show ntp status')

        # initial variables
        ret_dict = {}

        # Clock is synchronized, stratum 1, reference is .LOCL.
        p1 = re.compile(r'^Clock +is +(?P<clock_state>\w+), +stratum +(?P<stratum>\d+), +reference +is +(?P<refid>[\w\.]+)$')

        # Clock is unsynchronized, stratum 16, no reference clock
        p1_1 = re.compile(r'^Clock +is +(?P<clock_state>\w+), +stratum +(?P<stratum>\d+), +no +reference +clock$')

        # nominal freq is 250.0000 Hz, actual freq is 250.0000 Hz, precision is 2**10
        p2 = re.compile(r'^nominal +freq +is +(?P<nom_freq>[\d\.]+) +Hz, actual +freq +is +(?P<act_freq>[\d\.]+) +Hz, precision +is +(?P<precision>[\d\*]+)$')

        # ntp uptime is 1921500 (1/100 of seconds), resolution is 4000
        p3 = re.compile(r'^ntp +uptime +is +(?P<uptime>[\d\s\w\/\(\)]+), +resolution +is +(?P<resolution>[\d]+)$')

        # reference time is DF9FFBA0.8B020DC8 (15:43:28.543 UTC Wed Nov 21 2018)
        p4 = re.compile(r'^reference +time +is +(?P<reftime>[\w\s\.\:\(\)]+)$')

        # clock offset is 0.0000 msec, root delay is 0.00 msec
        p5 = re.compile(r'^clock +offset +is +(?P<offset>[\d\.]+) +msec, +root +delay +is +(?P<rootdelay>[\d\.]+) +msec$')

        # root dispersion is 2.31 msec, peer dispersion is 1.20 msec
        p6 = re.compile(r'^root +dispersion +is +(?P<rootdispersion>[\d\.]+) +msec, +peer +dispersion +is +(?P<peerdispersion>[\d\.]+) +msec$')

        # loopfilter state is 'CTRL' (Normal Controlled Loop), drift is 0.000000000 s/s
        p7 = re.compile(r'^loopfilter +state +is +(?P<leap_status>[\'\s\w\(\)]+), +drift +is +(?P<drift>[\d\.\s\w\/]+)$')

        # system poll interval is 16, last update was 9 sec ago.
        p8 = re.compile(r'^system +poll +interval +is +(?P<poll>\d+), +last +update +was +(?P<last_update>[\d\s\w]+).*$')

        for line in out.splitlines():
            line = line.strip()
            if not line: 
                continue

            m = p1.match(line)
            if m:
                groups = m.groupdict()
                clock_dict = ret_dict.setdefault('clock_state', {}).setdefault('system_status', {})
                clock_dict['status'] = groups['clock_state']
                clock_dict['stratum'] = int(groups['stratum'])
                clock_dict['refid'] = groups['refid']
                continue

            m = p1_1.match(line)
            if m:
                groups = m.groupdict()
                clock_dict = ret_dict.setdefault('clock_state', {}).setdefault('system_status', {})
                clock_dict['status'] = groups['clock_state']
                clock_dict['stratum'] = int(groups['stratum'])
                continue

            m = p2.match(line)
            if m:
                groups = m.groupdict()
                clock_dict = ret_dict.setdefault('clock_state', {}).setdefault('system_status', {})
                clock_dict['nom_freq'] = float(groups['nom_freq'])
                clock_dict['act_freq'] = float(groups['act_freq'])
                try:
                    clock_dict['precision'] = int(groups['precision'])
                except:
                    clock_dict['precision'] = str(groups['precision'])
                continue

            m = p3.match(line)
            if m:
                groups = m.groupdict()
                clock_dict = ret_dict.setdefault('clock_state', {}).setdefault('system_status', {})
                clock_dict['uptime'] = groups['uptime']
                clock_dict['resolution'] = int(groups['resolution'])
                continue

            m = p4.match(line)
            if m:
                groups = m.groupdict()
                clock_dict = ret_dict.setdefault('clock_state', {}).setdefault('system_status', {})
                clock_dict['reftime'] = groups['reftime']
                continue

            m = p5.match(line)
            if m:
                groups = m.groupdict()
                clock_dict = ret_dict.setdefault('clock_state', {}).setdefault('system_status', {})
                clock_dict['offset'] = float(groups['offset'])
                clock_dict['rootdelay'] = float(groups['rootdelay'])
                continue

            m = p6.match(line)
            if m:
                groups = m.groupdict()
                clock_dict = ret_dict.setdefault('clock_state', {}).setdefault('system_status', {})
                clock_dict['rootdispersion'] = float(groups['rootdispersion'])
                clock_dict['peerdispersion'] = float(groups['peerdispersion'])
                continue

            m = p7.match(line)
            if m:
                groups = m.groupdict()
                clock_dict = ret_dict.setdefault('clock_state', {}).setdefault('system_status', {})
                clock_dict['leap_status'] = groups['leap_status']
                clock_dict['drift'] = groups['drift']
                continue

            m = p8.match(line)
            if m:
                groups = m.groupdict()
                clock_dict = ret_dict.setdefault('clock_state', {}).setdefault('system_status', {})
                clock_dict['poll'] = int(groups['poll'])
                clock_dict['last_update'] = groups['last_update']
                continue

        return ret_dict


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

    def cli(self):

        # excute command to get output
        out = self.device.execute('show ntp config')

        # initial variables
        ret_dict = {}

        # R1#show ntp config
        # ntp server 1.1.1.1
        # ntp server 2.2.2.2
        # ntp server vrf VRF1 4.4.4.4
        # ntp server 2.2.2.2 source Loopback0

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
                    addr_dict['type'][ntp_type]['source']= source

                addr_dict.setdefault('isconfigured', {}).\
                    setdefault(str(isconfigured), {}).update({'address': address,
                                                              'isconfigured': isconfigured})

        return ret_dict