''' show_evpn.py

show evpn parser class

'''

from netaddr import EUI
from ipaddress import ip_address
import re

from metaparser import MetaParser
from metaparser.util.schemaengine import Any

from xbu_shared.parser.base import *

re_8bit_u = r'(?:' + r'|'.join([
    r'[0-9]',
    r'[1-9][0-9]',
    r'1[0-9][0-9]',
    r'2[0-4][0-9]',
    r'25[0-5]',
]) + r')'
re_8bit_x = r'(?:[A-Fa-f0-9]{1,2})'
re_8bit_02x = r'(?:[A-Fa-f0-9]{2})'
re_16bit_x = r'(?:[A-Fa-f0-9]{1,4})'
re_16bit_04x = r'(?:[A-Fa-f0-9]{4})'
re_mac = r'(?:' + r'|'.join([
    r'\.'.join([re_16bit_x] * 3),
    r':'.join([re_8bit_x] * 6),
    r'-'.join([re_8bit_x] * 6),
    r'\.'.join([re_8bit_x] * 6),
]) + r')'
re_ipv4 = r'(?:' + r'\.'.join([re_8bit_u] * 4) + r')'
re_ipv6 = r'(?:[A-Fa-f0-9:]*:[A-Fa-f0-9:]*(?::' + re_ipv4 + ')?)'
re_ip = r'(?:' + r'|'.join([re_ipv4, re_ipv6]) + ')'
re_label_str = r'(?:' + r'|'.join([
    r'[0-9]+',
    r'[A-Za-z0-9-]+',  # See mpls_label_strings @ mpls/base/include/mpls_label_defs_extra.h
]) + r')'


class ShowEvpnEvi(MetaParser):
    '''Parser class for 'show evpn evi' CLI.'''

    # TODO schema

    def cli(self):
        '''parsing mechanism: cli
        '''

        cmd = 'show evpn evi'

        tcl_package_require_caas_parsers()
        kl = tcl_invoke_caas_abstract_parser(
            device=self.device, exec=cmd)

        return kl


class ShowEvpnEviDetail(MetaParser):
    '''Parser class for 'show evpn evi detail' CLI.'''

    # TODO schema

    def cli(self):
        '''parsing mechanism: cli
        '''

        cmd = 'show evpn evi detail'

        tcl_package_require_caas_parsers()
        kl = tcl_invoke_caas_abstract_parser(
            device=self.device, exec=cmd)

        return kl


class ShowEvpnEviMac(MetaParser):
    '''Parser class for 'show evpn evi mac' CLI.'''

    # TODO schema

    def __init__(self, mac=None, **kwargs):
        self.mac = mac
        super().__init__(**kwargs)

    def cli(self):

        cmd = 'show evpn evi mac'.format()
        if self.mac:
            cmd += ' {mac}'.format(self.mac)

        out = self.device.execute(cmd)

        result = {
            'entries': [],
        }

        for line in out.splitlines():
            line = line.rstrip()

            # EVI        MAC address    IP address                               Nexthop                                 Label
            # ---------- -------------- ---------------------------------------- --------------------------------------- --------

            # 65535      02e5.7847.6000 ::                                       Local                                   0
            # 1          0000.0000.0001 ::                                       No remote pathlist
            m = re.match(r'^(?P<evi>[0-9]+)'
                         r' +(?P<mac>' + re_mac + ')'
                         r' +(?P<ip>' + re_ip + ')'
                         r'(?: +No remote pathlist|'
                         r' +(?P<next_hop>\S+)'
                         r' +(?:(?P<label_int>\d+)|(?P<label_str>' + re_label_str + '))'
                         r')'
                         r'$', line)
            if m:
                entry = {
                    'evi': int(m.group('evi')),
                    'mac': EUI(m.group('mac')),
                    'ip': ip_address(m.group('ip')),
                    'next_hop': m.group('next_hop'),
                    'label': m.group('label_str') \
                    or (m.group('label_int') and int(m.group('label_int'))),
                }
                try:
                    entry['next_hop'] = ip_address(entry['next_hop'])
                except (TypeError, ValueError):
                    pass
                result['entries'].append(entry)
                continue

            # OLD

            # MAC address    Nexthop                                 Label    vpn-id
            # -------------- --------------------------------------- -------- --------

            # 7777.7777.0002 N/A                                     24005    7
            m = re.match(r'^(?P<mac>' + re_mac + ')'
                         r' +(?:N/A|(?P<ip>' + re_ip + ')|(?P<next_hop>\S+))'
                         r' +(?:(?P<label_int>\d+)|(?P<label_str>' + re_label_str + '))'
                         r' +(?P<evi>[0-9]+)'
                         r'$', line)
            if m:
                entry = {
                    'mac': EUI(m.group('mac')),
                    'ip': m.group('ip') and ip_address(m.group('ip')),
                    'next_hop': m.group('next_hop'),
                    'label': m.group('label_str') or int(m.group('label_int')),
                    'evi': int(m.group('evi')),
                }
                try:
                    entry['label'] = int(entry['label'])
                except ValueError:
                    pass
                result['entries'].append(entry)
                continue

        return result


class ShowEvpnEthernetSegment(MetaParser):
    '''Parser class for 'show evpn ethernet-segment' CLI.'''

    # TODO schema

    def __init__(self, detail=False, private=False, carving=False, **kwargs):
        self.detail = detail
        self.private = private
        self.carving = carving
        super().__init__(**kwargs)

    def cli(self):
        '''parsing mechanism: cli
        '''

        cmd = 'show evpn ethernet-segment'
        if self.carving:
            cmd += ' carving'

        if self.private:
            cmd += ' private'
        elif self.detail:
            cmd += ' detail'

        tcl_package_require_caas_parsers()
        kl = tcl_invoke_caas_abstract_parser(
            device=self.device, exec=cmd)

        return kl

class ShowEvpnInternalLabelDetail(MetaParser):

    # TODO schema

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def cli(self):
        '''parsing mechanism: cli
        '''
        cmd = 'show evpn internal-label detail'

        out = self.device.execute(cmd)

        res = {
            'entries': [],
        }

        for line in out.splitlines():
            line = line.rstrip()

            # 5     0012.1200.0000.0000.0002                0        24114
            m = re.match(r'^\s*(?P<evi>\d+)\s+'
                          '(?P<esi>[\d.]+)\s+'
                          '(?P<eth_tag>\d+)\s+'
                          '(?P<internal_label>\w+)$',line)

            if m:
                # create new record
                record = { 'evi' : m.group('evi'),
                           'esi' : m.group('esi'),
                           'eth_tag' : m.group('eth_tag'),
                           'internal_label' : m.group('internal_label'),
                           'pathlists' : {
                                'mac' : [],
                                'es_ead' : [],
                                'evi_ead' : [],
                                'summary' : []
                            }
                         }

                res['entries'].append(record)

            # Multi-paths resolved: TRUE
            m = re.match(r'^\s+Multi-paths resolved: '
                          '(?P<mp_resolved>\w+)$',line)

            if m:
                res['entries'][-1]['mp_resolved'] = m.group('mp_resolved')


            # Multi-paths resolved: TRUE (Remote single-active)
            m = re.match(r'^\s+Multi-paths resolved: '
                          '(?P<mp_resolved>\w+) '
                          '\((?P<mp_single_active>.+)\)$',line)

            if m:
                res['entries'][-1]['mp_resolved'] = m.group('mp_resolved')
                res['entries'][-1]['mp_single_active'] = m.group('mp_single_active')

            # MAC     20.20.20.20                              24212
            m = re.match(r'^\s+MAC\s+'
                          '(?P<nexthop>[\d.]+)\s+'
                          '(?P<label>\d+)$',line)

            if m:
                mac_flag = True
                es_ead_flag = False
                evi_ead_flag = False
                summary_flag = False

                res['entries'][-1]['pathlists']['mac'].append(
                    {'nexthop' : m.group('nexthop'),
                     'label' : m.group('label')}
                )

            # EAD/ES  10.10.10.10                              0
            m = re.match(r'^\s+EAD/ES\s+'
                          '(?P<nexthop>[\d.]+)\s+'
                          '(?P<label>\d+)$',line)

            if m:
                mac_flag = False
                es_ead_flag = True
                evi_ead_flag = False
                summary_flag = False

                res['entries'][-1]['pathlists']['es_ead'].append(
                    {'nexthop' : m.group('nexthop'),
                     'label' : m.group('label')}
                )

            # EAD/EVI 10.10.10.10                              24012
            m = re.match(r'^\s+EAD/EVI\s+'
                          '(?P<nexthop>[\d.]+)\s+'
                          '(?P<label>\d+)$',line)

            if m:
                mac_flag = False
                es_ead_flag = False
                evi_ead_flag = True
                summary_flag = False

                res['entries'][-1]['pathlists']['evi_ead'].append(
                    {'nexthop' : m.group('nexthop'),
                     'label' : m.group('label')}
                )

            # Summary 20.20.20.20                              24212
            m = re.match(r'^\s+Summary\s+'
                          '(?P<nexthop>[\d.]+)\s+'
                          '(?P<label>\d+)$',line)

            if m:
                mac_flag = False
                es_ead_flag = False
                evi_ead_flag = False
                summary_flag = True

                res['entries'][-1]['pathlists']['summary'].append(
                    {'nexthop' : m.group('nexthop'),
                     'label' : m.group('label')}
                )

            #         20.20.20.20                              0
            m = re.match(r'^\s+'
                         '(?P<nexthop>[\d.]+)\s+'
                         '(?P<label>\d+)$',line)

            if m:
               if mac_flag:
                   res['entries'][-1]['pathlists']['mac'].append(
                       {'nexthop' : m.group('nexthop'),
                        'label' : m.group('label')}
                   )
               elif es_ead_flag:
                   res['entries'][-1]['pathlists']['es_ead'].append(
                       {'nexthop' : m.group('nexthop'),
                        'label' : m.group('label')}
                   )
               elif evi_ead_flag:
                   res['entries'][-1]['pathlists']['evi_ead'].append(
                       {'nexthop' : m.group('nexthop'),
                        'label' : m.group('label')}
                   )
               elif summary_flag:
                   res['entries'][-1]['pathlists']['summary'].append(
                       {'nexthop' : m.group('nexthop'),
                        'label' : m.group('label')}
                   )

            #         10.10.10.10 (B)                          24012
            m = re.match(r'^\s+'
                         '(?P<nexthop>[\d.]+)\s+'
                         '\((?P<flag>\w+)\)\s+'
                         '(?P<label>\d+)$',line)

            if m:
               res['entries'][-1]['pathlists']['summary'].append(
                   {'nexthop' : m.group('nexthop'),
                    'label' : m.group('label'),
                    'flag' : m.group('flag')}
               )

        return res

# vim: ft=python ts=8 sw=4 et
