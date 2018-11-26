"""show_ntp.py

Junos parsers for the following show commands:

    * show ntp associations
    * show ntp status
    * show configuration system ntp | display set

"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


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
                        Optional('type'): str,
                        Optional('stratum'): int,
                        Optional('receive_time'): int,
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

    MODE_MAP = {'*': 'synchronized',
                'o': 'synchronized',
                'x': 'falseticker',
                '+': 'final selection set',
                '-': 'clustering',
                '=': 'client',
                None: 'unsynchronized'}

    TYPE_MAP = {'b': 'broadcast',
                'l': 'local',
                'm': 'multicast',
                'u': 'unicast',
                '-': 'active'}

    def cli(self):

        # execute command to get output
        out = self.device.execute('show ntp associations')

        # initial variables
        ret_dict = {}

        # for attributes details please refer to 
        # https://www.juniper.net/documentation/en_US/junos/topics/reference/command-summary/show-ntp-associations.html

        # remote         refid           st t when poll reach   delay   offset  jitter
        # ===============================================================================
        # x10.2.2.2         171.68.38.65     2 -   84  128  271    1.470  -46.760  52.506
        p1 = re.compile(r'^(?P<mode_code>[xo\*\-\+\=]+)? *(?P<remote>[\w\.\:]+) +'
                         '(?P<refid>[\w\.]+) +(?P<stratum>\d+) +(?P<type>[blmu\-]+) +'
                         '(?P<receive_time>\d+) +(?P<poll>\d+) +'
                         '(?P<reach>\d+) +(?P<delay>[\d\.]+) +'
                         '(?P<offset>[\d\.\-]+) +(?P<jitter>[\d\.\-]+)$')


        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # *171.68.38.65     .GNSS.           1 -   59   64  377    1.436   73.819  10.905
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                peer = groups['remote']
                local_mode = self.TYPE_MAP.get(groups['type'])
                mode = self.MODE_MAP.get(groups['mode_code'])

                peer_dict = ret_dict.setdefault('peer', {}).setdefault(peer, {})\
                    .setdefault('local_mode', {}).setdefault(local_mode, {})
                peer_dict.update({'remote': peer,
                                  'refid': groups['refid'],
                                  'type': local_mode,
                                  'mode': mode,
                                  'stratum': int(groups['stratum']),
                                  'receive_time': int(groups['receive_time']),
                                  'poll': int(groups['poll']),
                                  'reach': int(groups['reach']),
                                  'delay': float(groups['delay']),
                                  'offset': float(groups['offset']),
                                  'jitter': float(groups['jitter'])})

                # ops clock_state structure
                if 'sync' in mode:
                    clock_dict = ret_dict.setdefault('clock_state', {}).setdefault('system_status', {})
                    clock_dict['clock_state'] = mode
                    clock_dict['clock_stratum'] = int(groups['stratum'])
                    clock_dict['associations_address'] = peer
                    clock_dict['root_delay'] = float(groups['delay'])
                    clock_dict['clock_offset'] = float(groups['offset'])
                    clock_dict['clock_refid'] = groups['refid']
                    clock_dict['associations_local_mode'] = local_mode

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
                Optional('ass_id'): int,
                Optional('clock'): str,
                Optional('frequency'): float,
                Optional('jitter'): float,
                Optional('leap_status'): str,
                Optional('number_of_events'): int,
                Optional('offset'): float,
                Optional('peer'): int,
                Optional('poll'): int,
                Optional('precision'): float,
                Optional('processor'): str,
                Optional('recent_event'): str,
                Optional('refid'): str,
                Optional('reftime'): str,
                Optional('rootdelay'): float,
                Optional('rootdispersion'): float,
                Optional('stability'): float,
                Optional('state'): int,
                'status': str,
                Optional('stratum'): int,
                Optional('synch_source'): str,
                Optional('system'): str,
                Optional('version'): str
            }
        }
    }

class ShowNtpStatus(ShowNtpStatusSchema):
    """Parser for: show ntp status"""

    def cli(self):

        def _conver_val(value):
            if not value:
                return None

            if value.isdigit():
                return int(value)

            try:
                return float(value)
            except Exception:
                return value

        # excute command to get output
        out = self.device.execute('show ntp status')

        # initial variables
        ret_dict = {}

        # attributes details please refer to 
        # https://www.juniper.net/documentation/en_US/junos/topics/reference/command-summary/show-ntp-status.html

        # status=0644 leap_none, sync_ntp, 4 events, event_peer/strat_chg,
        # assID=0 status=0544 leap_none, sync_local_proto, 4 events, event_peer/strat_chg,
        p1 = re.compile(r'^(assID\=(?P<ass_id>\d+) *)?status\=(?P<status>\d+) *(?P<leap_status>\w+), +'
                         '(?P<synch_source>\w+), +(?P<number_of_events>\d+) +events, +(?P<recent_event>\S+),$')

        # reftime=df981acf.bfa97435  Thu, Nov 15 2018 11:18:23.748, poll=6,
        p2 = re.compile(r'^reftime\=(?P<reftime>[\w\s\,\.\:]+), +poll\=(?P<poll>\d+),$')

        # clock=df981ae8.eb6e7ee8  Thu, Nov 15 2018 11:18:48.919, state=4,
        p3 = re.compile(r'^clock\=(?P<clock>[\w\s\,\.\:]+), +state\=(?P<state>\d+),$')

        # version="ntpd 4.2.0-a Tue Dec 19 21:12:44  2017 (1)", processor="amd64",
        # system="FreeBSDJNPR-11.0-20171206.f4cad52_buil", leap=00, stratum=2,
        # precision=-23, rootdelay=1.434, rootdispersion=82.589, peer=22765,
        # refid=171.68.38.65,
        # offset=67.812, frequency=4.968, jitter=12.270, stability=0.890
        p4 = re.compile(r'(?P<key>\w+)\=\"?(?P<value>[\w\.\:\s\(\)\-\@\/\_]+)\"?')

        for line in out.splitlines():
            line = line.strip()
            if not line: 
                continue

            m = p1.match(line)
            if m:
                groups = m.groupdict()
                clock_dict = ret_dict.setdefault('clock_state', {}).setdefault('system_status', {})
                clock_dict['status'] = groups.pop('status')
                for k, v in groups.items():
                    v = _conver_val(v)
                    if v:
                        clock_dict[k] = v
                continue

            m = p2.match(line)
            if m:
                groups = m.groupdict()
                clock_dict = ret_dict.setdefault('clock_state', {}).setdefault('system_status', {})
                for k, v in groups.items():
                    v = _conver_val(v)
                    if v:
                        clock_dict[k] = v
                continue

            m = p3.match(line)
            if m:
                groups = m.groupdict()
                clock_dict = ret_dict.setdefault('clock_state', {}).setdefault('system_status', {})
                for k, v in groups.items():
                    v = _conver_val(v)
                    if v:
                        clock_dict[k] = v
                continue

            m = p4.findall(line)
            if m:
                clock_dict = ret_dict.setdefault('clock_state', {}).setdefault('system_status', {})
                for k, v in m:                
                    v = _conver_val(v)
                    if v:
                        clock_dict[k] = v
                continue

        return ret_dict


# =========================================================
# Parser for 'show configuration system ntp | display set '
# =========================================================

class ShowConfigurationSystemNtpSetSchema(MetaParser):
    """Schema for: show configuration system ntp | display set """

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

class ShowConfigurationSystemNtpSet(ShowConfigurationSystemNtpSetSchema):
    """Parser for: show configuration system ntp | display set """

    def cli(self):

        # excute command to get output
        out = self.device.execute('show configuration system ntp | display set')

        # initial variables
        ret_dict = {}

        # show configuration system ntp | display set 
        # set system ntp peer 10.2.2.2
        # set system ntp server 171.68.38.65 routing-instance mgmt_junos
        # set system ntp server 171.68.38.66 routing-instance mgmt_junos
        # set system ntp server 72.163.32.44 routing-instance mgmt_junos

        p1 = re.compile(r'^set +system +ntp +(?P<type>\w+) +(?P<address>[\w\.\:]+)'
                         '( *routing-instance +(?P<vrf>\S+))?$')

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
                isconfigured = True

                addr_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {})\
                    .setdefault('address', {}).setdefault(address, {})

                addr_dict.setdefault('type', {}).setdefault(ntp_type, {}).update({'address': address,
                                                                                 'type': ntp_type,
                                                                                 'vrf': vrf})

                addr_dict.setdefault('isconfigured', {}).\
                    setdefault(str(isconfigured), {}).update({'address': address,
                                                              'isconfigured': isconfigured})

        return ret_dict
