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

    def cli(self,output=None):
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

            # *172.16.229.65    .GNSS.           1 -   59   64  377    1.436   73.819  10.905
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                peer = groups['remote']
                if '~' == groups['configured']:
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

class ShowNtpStatusSchema(MetaParser):
    """Schema for: show ntp status"""

    schema = {
        'clock_state': {
            'system_status': {
                Optional('status'): str,
                Optional('stratum'): int,
                Optional('refid'): str,
                Optional('assoc_id'): int,
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
                Optional('leapsecond'): bool,
            }
        }
    }


class ShowNtpStatus(ShowNtpStatusSchema):
    """Parser for: show ntp status"""

    cli_command = 'show ntp status'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}

        # Clock is synchronized, stratum 1, reference is .LOCL.
        # Clock is synchronized, stratum 2, reference assoc id 1, reference is 192.0.2.1
        # Clock is synchronized (adding leap second), stratum 1, reference is 192.168.4.20
        p1 = re.compile(r'Clock +is +(?P<clock_state>\w+)(?P<leapsecond> +\(adding +leap +second\))?,'
            ' +stratum +(?P<stratum>\d+),(?: +reference +assoc +id +'
            '(?P<assoc_id>[\d]+),)? +reference +is +(?P<refid>[\w\.]+)$')

        # Clock is unsynchronized, stratum 16, no reference clock
        p1_1 = re.compile(r'^Clock +is +(?P<clock_state>\w+), +stratum +(?P<stratum>\d+), +no +reference +clock$')

        # nominal freq is 250.0000 Hz, actual freq is 250.0000 Hz, precision is 2**10
        p2 = re.compile(r'^nominal +freq +is +(?P<nom_freq>[\d\.]+) +Hz, actual +freq +is'
                         ' +(?P<act_freq>[\d\.]+) +Hz, precision +is +(?P<precision>[\d\*]+)$')

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
                if groups['assoc_id']:
                    clock_dict['assoc_id'] = int(groups['assoc_id'])
                if groups['leapsecond']:
                    clock_dict['leapsecond'] = True
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
                                Optional('preferred'): bool,
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
        # ntp server 10.3.254.100 prefer
        p1 = re.compile(r"^ntp +(?P<type>\w+)( +vrf +(?P<vrf>\S+))? "
                         "+(?P<address>[\w\.\:]+)( +source +"
                         "(?P<source_interface>[\w]+))?(?P<prefer> prefer)?$")

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
                prefer = groups['prefer']
                isconfigured = True

                addr_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {})\
                    .setdefault('address', {}).setdefault(address, {})

                addr_dict.setdefault('type', {}).setdefault(ntp_type, {}).update({'address': address,
                                                                                 'type': ntp_type,
                                                                                 'vrf': vrf})

                if prefer:
                    addr_dict['type'][ntp_type]['preferred'] = True

                if source:
                    addr_dict['type'][ntp_type]['source'] = source

                addr_dict.setdefault('isconfigured', {}).\
                    setdefault(str(isconfigured), {}).update({'address': address,
                                                              'isconfigured': isconfigured})



        return ret_dict

# ==============================================
#  Schema for show ntp associations detail
# ==============================================
class ShowNtpAssociationsDetailSchema(MetaParser):
    """Schema for show ntp associations detail"""

    schema = {
        'vrf': {
            Any(): {
                'associations': {
                    'address': {
                        Any(): {
                            'local_mode': {
                                Any(): {
                                    'isconfigured': {
                                        Any(): {
                                            'address': str,
                                            'local_mode': str,
                                            'isconfigured': bool,
                                            'stratum': int,
                                            'refid': str,
                                            Optional('authenticated'): bool,
                                            Optional('prefer'): str,
                                            'peer_interface': str,
                                            Optional('minpoll'): int,
                                            Optional('maxpoll'): int,
                                            Optional('port'): str,
                                            'version': int,
                                            'reach': str,
                                            Optional('unreach'): str,
                                            'poll': str,
                                            Optional('now'): str,
                                            'root_delay_msec': str,
                                            'root_disp': str,
                                            'offset_msec': str,
                                            'delay_msec': str,
                                            'dispersion': str,
                                            Optional('jitter_msec'): str,
                                            'originate_time': str,
                                            'receive_time': str,
                                            'transmit_time': str,
                                            'input_time': str,
                                            'vrf': str,
                                            Optional('ip_type'): str,
                                            'sane': bool,
                                            'valid': bool,
                                            Optional('master'): bool,
                                            Optional('selected'): bool,
                                            Optional('unsynced'): bool,
                                            'sync_dist': str,
                                            'precision': str,
                                            Optional('assoc_id'): int,
                                            Optional('assoc_name'): str,
                                            'filterror': str,
                                            'filtoffset': str,
                                            'filtdelay': str,
                                            Optional('ntp_statistics'): {
                                                'packet_sent': int,
                                                Optional('packet_sent_fail'): int,
                                                'packet_received': int,
                                                'packet_dropped': int,
                                            },
                                            'peer': {
                                                Any(): {
                                                    'local_mode': {
                                                        Any(): {
                                                            'local_mode': str,
                                                            'poll': int,
                                                        },
                                                    }
                                                },
                                            }
                                        }
                                    }
                                },
                            }
                        },
                    }
                }
            },
        },
    }

# ==============================================
#  Parser for show ntp associations detail
# ==============================================
class ShowNtpAssociationsDetail(ShowNtpAssociationsDetailSchema):
    """Parser for show ntp associations detail"""

    cli_command = 'show ntp associations detail'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}

        # 192.168.255.254 configured, ipv4, authenticated, insane, invalid, stratum 
        # 172.16.255.254 configured, ipv4, authenticated, our_master, sane, valid, stratum 2
        # 192.168.13.33 configured, ipv6, insane, invalid, unsynced, stratum 16
        # 172.31.32.2 configured, insane, invalid, stratum 5
        # 192.168.13.33 configured, selected, sane, valid, stratum 3
        # 192.168.13.57 configured, our_master, sane, valid, stratum 3
        # 192.168.255.254 configured, ipv4, authenticated (' ' reject), insane, invalid, stratum 3
        p1 = re.compile(r'^(?P<address>[\w\.\:]+) +(?P<configured>\w+),( +(?P<ip_type>ipv4|ipv6),)?'
                         '( +(?P<authenticated>authenticated)( +\(\'\W\' +\S+\))?,)?( +(?P<our_master>our_master),)?'
                         '( +(?P<selected>selected),)? +(?P<insane>\w+), +(?P<invalid>\w+),'
                         '( +(?P<unsynced>unsynced),)? +stratum +(?P<stratum>\d+)$')

        # ref ID 10.10.10.254      , time DBAB02D6.9E354130 (18:49:35.873 UTC Thu Jul 11 2019)
        # ref ID 172.16.255.254, time DBAB02D6.9E354130 (16:08:06.618 EST Fri Oct 14 2016)
        p2 = re.compile(r'^ref +ID +(?P<refid>[\w\.]+)( +)?, +time +(?P<input_time>[\w\:\s\(\)\.]+)$')

        # our mode client, peer mode server, our poll intvl 512, peer poll intvl 512
        # our mode client, peer mode server, our poll intvl 512, peer poll intvl 512
        p3 = re.compile(r'^our +mode +(?P<mode>\w+), +peer +mode +(?P<peer_mode>\w+),'
                         ' +our +poll +intvl +(?P<poll_intv>\d+),'
                         ' +peer +poll +intvl +(?P<peer_poll_intv>\d+)$')

        # root delay 0.00 msec, root disp 14.52, reach 377, sync dist 28.40
        p4 = re.compile(r'^root +delay +(?P<root_delay_msec>[\d\.]+) +msec, +root +disp +(?P<root_disp>[\d\.]+),'
                         ' +reach +(?P<reach>[\d\.]+),'
                         ' +sync +dist +(?P<sync_dist>[\d\.]+)$')

        # delay 0.00 msec, offset 0.0000 msec, dispersion 7.23, jitter 0.97 
        # delay 0.00 msec, offset -1.0000 msec, dispersion 5.64, jitter 0.97 msec
        # delay 7.86 msec, offset 11.176 msec, dispersion 3.62
        p5 = re.compile(r'^delay +(?P<delay_msec>[\d\.]+) +msec, +offset +(?P<offset_msec>[\d\.\-]+)'
                         ' +msec, +dispersion +(?P<dispersion>[\d\.]+)'
                         '(, +jitter +(?P<jitter_msec>[\d\.]+)( +msec)?)?$')

        # precision 2**10, version 4
        p6 = re.compile(r'^precision +(?P<precision>[\d\*]+), +version +(?P<version>\d+)$')

        # assoc id 62758, assoc name 192.168.255.254
        # assoc ID 2, assoc name myserver
        # assoc ID 1, assoc name 192.168.1.55,
        p7 = re.compile(r'^assoc +(id|ID) +(?P<assoc_id>\d+), +assoc +name +(?P<assoc_name>[\w\.]+),?$')

        # assoc in packets 27, assoc out packets 27, assoc error packets 0
        p8 = re.compile(r'^assoc +in +packets +(?P<assoc_in_packets>\d+),'
                         ' +assoc +out +packets +(?P<assoc_out_packets>\d+),'
                         ' +assoc +error +packets +(?P<assoc_error_packets>[\d\.]+)$')

        # org time 00000000.00000000 (09:00:00.000 EST Mon Jan 1 1900)
        p9 = re.compile(r'^org +time +(?P<org_time>[\w\:\s\(\)\.]+)$')

        # rec time DBAB046D.A8B43B28 (16:14:53.659 EST Fri Oct 14 2016)
        # rcv time AFE252E2.3D7E464D (00:12:34.240 PDT Mon Jan 1 1900)
        p10 = re.compile(r'^(rec|rcv) +time +(?P<rec_time>[\w\:\s\(\)\.]+)$')

        # xmt time DBAB046D.A8B43B28 (16:14:53.659 EST Fri Oct 14 2016)
        p11 = re.compile(r'^xmt +time +(?P<xmt_time>[\w\:\s\(\)\.]+)$')

        # filtdelay =     0.00    1.00    0.00    0.00    0.00    0.00    0.00    0.00
        p12 = re.compile(r'^filtdelay +\= +(?P<filtdelay>[\d\s\.]+)$')

        # filtoffset =    0.00    0.50    0.00    1.00    1.00    1.00    1.00    1.00
        p13 = re.compile(r'^filtoffset +\= +(?P<filtoffset>[\d\s\.\-]+)$')

        # filterror =     1.95    5.89    9.88   13.89   15.84   17.79   19.74   21.76
        p14 = re.compile(r'^filterror +\= +(?P<filterror>[\d\s\.]+)$')

        # minpoll = 6, maxpoll = 10
        p15 = re.compile(r'^minpoll +\= +(?P<minpoll>\d+), +maxpoll +\= +(?P<maxpoll>\d+)$')

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                address = group['address']
                ip_type = group['ip_type']
                stratum = int(group['stratum'])
                authenticated = True if group['authenticated'] else False
                isconfigured = True if group['configured'] else False
                sane = False if group['insane'] == 'insane' else True
                valid = False if group['invalid'] == 'invalid' else True
                master = True if group['our_master'] else False
                selected = True if group['selected'] else False
                unsynced = True if group['unsynced'] else False
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                refid = group['refid']
                input_time = group['input_time']
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                local_mode = group['mode']
                peer_mode = group['peer_mode']

                ret_dict.setdefault('vrf', {}).setdefault('default', {}).\
                    setdefault('associations', {}).setdefault('address', {}).\
                    setdefault(address, {}).setdefault('local_mode', {}).\
                    setdefault(local_mode, {}).setdefault('isconfigured', {}).\
                    setdefault(str(isconfigured), {})

                if ip_type:
                    ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['ip_type'] = ip_type

                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['selected'] = selected
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['unsynced'] = unsynced
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['address'] = address
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['isconfigured'] = isconfigured
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['authenticated'] = authenticated
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['sane'] = sane
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['valid'] = valid
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['master'] = master
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['stratum'] = stratum
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['refid'] = refid
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['input_time'] = input_time
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['peer_interface'] = refid
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['poll'] = group['poll_intv']
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['vrf'] = 'default'
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['local_mode'] = local_mode

                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)].setdefault('peer', {}).setdefault(refid, {}).\
                    setdefault('local_mode', {}).setdefault(peer_mode, {})

                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['peer'][refid]['local_mode']\
                    [peer_mode]['poll'] = int(group['peer_poll_intv'])
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['peer'][refid]['local_mode']\
                    [peer_mode]['local_mode'] = peer_mode
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                # ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                #     [local_mode]['isconfigured'][str(isconfigured)]['reach'] = group['root_delay_msec']
                # ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                #     [local_mode]['isconfigured'][str(isconfigured)]['sync_dist'] = group['root_disp']
                # ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                #     [local_mode]['isconfigured'][str(isconfigured)]['reach'] = group['reach']
                # ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                #     [local_mode]['isconfigured'][str(isconfigured)]['sync_dist'] = group['sync_dist']
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)].update({k:str(v) for k, v in group.items()})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict() 
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)].update({k:str(v) for k, v in group.items()})
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['precision'] = group['precision']
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['version'] = int(group['version'])
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['assoc_name'] = group['assoc_name']
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['assoc_id'] = int(group['assoc_id'])
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)].setdefault('ntp_statistics', {})
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['ntp_statistics']['packet_received'] = \
                    int(group['assoc_in_packets'])
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['ntp_statistics']['packet_sent'] = \
                    int(group['assoc_out_packets'])
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['ntp_statistics']['packet_dropped'] = \
                    int(group['assoc_error_packets'])
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['originate_time'] = group['org_time']
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['receive_time'] = group['rec_time']
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['transmit_time'] = group['xmt_time']
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['filtdelay'] = group['filtdelay']
                continue

            m = p13.match(line)
            if m:
                group = m.groupdict()
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['filtoffset'] = group['filtoffset']
                continue

            m = p14.match(line)
            if m:
                group = m.groupdict()
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['filterror'] = group['filterror']
                continue

            m = p15.match(line)
            if m:
                group = m.groupdict()
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['minpoll'] = int(group['minpoll'])
                ret_dict['vrf']['default']['associations']['address'][address]['local_mode']\
                    [local_mode]['isconfigured'][str(isconfigured)]['maxpoll'] = int(group['maxpoll'])

        return ret_dict