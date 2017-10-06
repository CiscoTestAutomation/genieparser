''' show_mcast.py

IOSXE parsers for the following show commands:

    * show ipv6 pim interface
    * show ipv6 pim vrf <WROD> interface 

'''

# Python
import re

# Metaparser
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional


# =============================================
# Parser for 'show ipv6 pim interface'
# Parser for 'show ipv6 pim vrf <WROD> interface'
# =============================================

class ShowIpv6PimInterfaceSchema(MetaParser):

    # Schema for 'show ipv6 pim interface'
    # Schema for 'show ipv6 pim vrf <WROD> interface'

    schema = {'vrf': {
                Any(): {
                    'interface': {
                        Any() :{
                            'dr_priority': int,
                            'hello_interval': int,
                            'neighbor_count': int,
                            'pim_enabled': bool,
                            Optional('dr_address'): str,
                            Optional('address'): list,
                        },
                    }
                },
            }
        }


class ShowIpv6PimInterface(ShowIpv6PimInterfaceSchema):

    # Parser for 'show ipv6 pim interface'
    # Parser for 'show ipv6 pim vrf <WROD> interface'

    def cli(self, vrf=''):

        # set vrf infomation
        if vrf:
            cmd = 'show ipv6 pim vrf {} interface'.format(vrf)
        else:
            cmd = 'show ipv6 pim interface'
            vrf = 'default'

        # excute command to get output
        out = self.device.execute(cmd)

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet1   on    1     30     1
            p1 = re.compile(r'^(?P<intf>[\w\-\/\.]+) +(?P<status>(on|off))'
                             ' +(?P<nbr_count>\d+) +(?P<hello_int>\d+) +(?P<dr_pri>\d+)$')
            m = p1.match(line)
            if m:
                intf = m.groupdict()['intf']
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}

                if 'interface' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['interface'] = {}
                if intf not in ret_dict['vrf'][vrf]['interface']:
                    ret_dict['vrf'][vrf]['interface'][intf] = {}

                if m.groupdict()['status'].lower() == 'on':
                    ret_dict['vrf'][vrf]['interface'][intf]['pim_enabled'] = True
                else:
                    ret_dict['vrf'][vrf]['interface'][intf]['pim_enabled'] = False

                ret_dict['vrf'][vrf]['interface'][intf]['dr_priority'] = \
                    int(m.groupdict()['dr_pri'])

                ret_dict['vrf'][vrf]['interface'][intf]['hello_interval'] = \
                    int(m.groupdict()['hello_int'])

                ret_dict['vrf'][vrf]['interface'][intf]['neighbor_count'] = \
                    int(m.groupdict()['nbr_count'])
                continue

            # Address: FE80::5054:FF:FE2C:6CDF
            # Address: ::
            p2 = re.compile(r'^Address *: +(?P<address>[\s\w\:\.]+)$')
            m = p2.match(line)
            if m:
                address = m.groupdict()['address']
                if re.search('\w+', address):
                    ret_dict['vrf'][vrf]['interface'][intf]['address'] = address.split()
                continue

            # DR     : FE80::5054:FF:FEAC:64B3
            # DR     : not elected
            p3 = re.compile(r'^DR *: +(?P<dr_address>[\w\:\.]+)$')
            m = p3.match(line)
            if m:
                ret_dict['vrf'][vrf]['interface'][intf]['dr_address'] = \
                        m.groupdict()['dr_address']
                continue

        return ret_dict

# ==========================================================
# schema for parser : show ip pim interface
# schema for parser : show ip pim vrf <vrf_name> interface
# ==========================================================
class ShowIpPimInterfaceSchema(MetaParser):

    # Schema for 'show ip pim Interface'
    schema = {
        'vrf': {
            Any(): {
                'interfaces': {
                    Any(): {
                        'address_family': {
                            Any(): {
                                Optional('dr_priority'): int,
                                Optional('hello_interval'): int,
                                Optional('neighbor_count'): int,
                                Optional('version'): int,
                                Optional('mode'): str,
                                Optional('dr_address'): str,
                                Optional('address'): list,
                            },
                        },
                    },
                },
            },
        }
    }

# ==========================================================
# parser for  : show ip pim interface
# parser for  : show ip pim vrf <vrf_name> interface
# ==========================================================

class ShowIpPimInterface(ShowIpPimInterfaceSchema):

    # Parser for 'show ip pim Interface'
    # Parser for 'show ip pim vrf <vrf_name> interface'

    def cli(self, vrf=""):

        # find cmd
        if vrf:
            cmd = 'show ip pim vrf {} interface'.format(vrf)
        else:
            cmd = 'show ip pim interface'
            vrf = 'default'

        af_name = 'ipv4'

        # excute command to get output
        out = self.device.execute(cmd)

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()
            # Address          Interface                Ver/   Nbr    Query  DR         DR
            #                              Mode   Count  Intvl  Prior
            # 10.1.2.1         GigabitEthernet1         v2/S   1      30     1          10.1.2.2
            p1 = re.compile(r'^\s*(?P<address>[\w\:\.]+) +(?P<interface>[\w\d\S]+)'
                            ' +v(?P<version>[\d]+)\/(?P<mode>[\w]+)'
                            ' +(?P<nbr_count>[\d]+)'
                            ' +(?P<query_interval>[\d]+)'
                            ' +(?P<dr_priority>[\d]+)'
                            ' +(?P<dr_address>[\w\d\.\:]+)$')
            m = p1.match(line)
            if m:
                new_mode = ""
                address = m.groupdict()['address']
                intf_name = m.groupdict()['interface']
                nbr_count = int(m.groupdict()['nbr_count'])
                version = int(m.groupdict()['version'])
                mode = m.groupdict()['mode']
                query_interval = int(m.groupdict()['query_interval'])
                dr_priority = int(m.groupdict()['dr_priority'])
                dr_address = m.groupdict()['dr_address']

                if mode == 'S':
                    new_mode = 'sparse-mode'
                if mode == 'SD':
                    new_mode = 'sparse-dense-mode'
                if mode == 'D':
                    new_mode = 'dense-mode'

                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'interfaces' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['interfaces'] = {}
                if intf_name not in ret_dict['vrf'][vrf]['interfaces']:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]['interfaces'][intf_name]:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] = {}
                if intf_name not in ret_dict['vrf'][vrf]['interfaces'] \
                        [intf_name]['address_family']:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name] \
                        ['address_family'][af_name] = {}

                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name] \
                    ['address'] = address.split()
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name] \
                    ['neighbor_count'] = nbr_count
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name] \
                    ['version'] = version
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name] \
                    ['mode'] = new_mode
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name] \
                    ['hello_interval'] = query_interval
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name] \
                    ['dr_priority'] = dr_priority
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name] \
                    ['dr_address'] = dr_address
                continue

        return ret_dict

# =============================================================
# schema for : show ip pim interface detail
# schema for : show ip pim vrf <vrf_name> interface detail
# =============================================================
class ShowIpPimInterfaceDetailSchema(MetaParser):
     schema = {
         'vrf':{
             Any():{
                 'interfaces':{
                     Any():{
                         'address_family':{
                             Any():{
                                 'bfd':{
                                   Optional('enable'): bool,
                                 },
                                 Optional('hello_interval'): int,
                                 Optional('hello_packets_in'): int,
                                 Optional('hello_packets_out'): int,
                                 Optional('oper_status'): str,
                                 Optional('address'): list,
                                 Optional('multicast'):{
                                     Optional('switching'): str,
                                     Optional('packets_in'): int,
                                     Optional('packets_out'): int,
                                     Optional('ttl_threshold'): int,
                                     Optional('tag_switching'): str,
                                 },
                                 Optional('pim_status'): str,
                                 Optional('version'): int,
                                 Optional('mode'): str,
                                 Optional('dr_address'): str,
                                 Optional('neighbor_count'): int,
                                 Optional('jp_interval'): int,
                                 Optional('state_refresh_processing'): str,
                                 Optional('state_refresh_origination'): str,
                                 Optional('nbma_mode'): str,
                                 Optional('atm_multipoint_signalling'): str,
                                 Optional('domain_border'): str,
                                 Optional('neighbors_rpf_proxy_capable'): bool,
                                 Optional('none_dr_join'): bool,
                             },
                         },
                     },
                 },
             },
         },

     }

# =============================================================
# parser for : show ip pim interface detail
# parser for : show ip pim vrf <vrf_name> interface detail
# =============================================================
class ShowIpPimInterfaceDetail(ShowIpPimInterfaceDetailSchema):
    # Parser for 'show ip pim Interface detail'
    # Parser for 'show ip pim vrf <vrf_name> interface detail'

    def cli(self, vrf=""):

        # find cmd
        if vrf:
            cmd = 'show ip pim vrf {} interface detail'.format(vrf)
        else:
            cmd = 'show ip pim interface detail'
            vrf = 'default'

        af_name = 'ipv4'

        # initial variables
        ret_dict = {}
        intf_name = oper_status = nbr_count = nbma_mode = hello_packet_in = ""
        hello_interval = hello_packet_out= address = dr_address = multi_packet_in= ""
        multi_packet_out = mode = version = pim_status = state_refresh_origination = ""
        state_refresh_processing = multi_switching = tagswitching = atm_multipoint = ""
        jp_interval = neighbors_rpf_proxy_capable = domain_border = bfd = ttl_threshold = ""
        non_dr_join = ""
        # excute command to get output
        out = self.device.execute(cmd)


        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet3 is up, line protocol is up
            p1 = re.compile(r'^\s*(?P<intf_name>[\w\d\S]+) +is +up,'
                            ' +line +protocol +is +(?P<oper_status>\w+)$')
            m = p1.match(line)
            if m:
                intf_name = ""
                intf_name = m.groupdict()['intf_name']
                oper_status = m.groupdict()['oper_status']

            # Internet address is 10.1.2.1/24
            p2 = re.compile(r'^\s*Internet +address +is +(?P<address>[\w\d\S]+)$')
            m = p2.match(line)
            if m:
                address = m.groupdict()['address']

            # Multicast switching: fast
            p3 = re.compile(r'^\s*Multicast +switching: +(?P<multi_switching>\w+)$')
            m = p3.match(line)
            if m:
                multi_switching = m.groupdict()['multi_switching']

            # Multicast packets in/out: 5/0
            p4 = re.compile(r'^\s*Multicast +packets +in/out:'
                            ' +(?P<in>\d+)/(?P<out>\d+)$')
            m = p4.match(line)
            if m:
                multi_packet_in = int(m.groupdict()['in'])
                multi_packet_out = int(m.groupdict()['out'])

            # Multicast TTL threshold: 0
            p5 = re.compile(r'^\s*Multicast +TTL +threshold:'
                            ' +(?P<ttl_threshold>\d+)$')
            m = p5.match(line)
            if m:
                ttl_threshold = int(m.groupdict()['ttl_threshold'])

            # PIM: enabled
            p6 = re.compile(r'^\s*PIM:'
                            ' +(?P<status>\w+)$')
            m = p6.match(line)
            if m:
                pim_status = m.groupdict()['status']

            # PIM version: 2, mode: sparse
            p7 = re.compile(r'^\s*PIM +version:'
                            ' +(?P<version>\d+), +mode: +(?P<mode>\w+)$')
            m = p7.match(line)
            if m:
                version = int(m.groupdict()['version'])
                mode = m.groupdict()['mode']

            # PIM DR: 10.1.2.2
            # PIM DR: 1.1.1.1 (this system)
            p8 = re.compile(r'^\s*PIM +DR:'
                            ' +(?P<dr_address>[\w\d\S]+)(\s+(?P<info>[\w\S\s]+))?$')
            m = p8.match(line)
            if m:
                dr_address = m.groupdict()['dr_address']

            # PIM neighbor count: 1
            p9 = re.compile(r'^\s*PIM +neighbor +count:'
                            ' +(?P<nbr_count>\d+)$')
            m = p9.match(line)
            if m:
                nbr_count = int(m.groupdict()['nbr_count'])

            # PIM Hello/Query interval: 30 seconds
            p10 = re.compile(r'^\s*PIM +[h|H]ello/[q|Q]uery +interval:'
                            ' +(?P<hello_interval>\d+) +seconds$')
            m = p10.match(line)
            if m:
                hello_interval = int(m.groupdict()['hello_interval'])

            # PIM Hello packets in/out: 8/10
            p11 = re.compile(r'^\s*PIM +Hello +packets +in/out:'
                             ' +(?P<h_in>\d+)/(?P<h_out>\d+)$')
            m = p11.match(line)
            if m:
                hello_packet_in = int(m.groupdict()['h_in'])
                hello_packet_out = int(m.groupdict()['h_out'])

            # PIM J/P interval: 60 seconds
            p12 = re.compile(r'^\s*PIM +J/P +interval:'
                             ' +(?P<jp_interval>\d+) +seconds$')
            m = p12.match(line)
            if m:
                jp_interval = int(m.groupdict()['jp_interval'])

            # PIM State-Refresh processing: enabled
            p13 = re.compile(r'^\s*PIM +[s|S]tate-[r|R]efresh +processing:'
                             ' +(?P<state_refresh_processing>\w+)$')
            m = p13.match(line)
            if m:
                state_refresh_processing = m.groupdict()['state_refresh_processing']

            # PIM State-Refresh origination: disabled
            p14 = re.compile(r'^\s*PIM +[s|S]tate-[r|R]efresh +origination:'
                             ' +(?P<state_refresh_origination>\w+)$')
            m = p14.match(line)
            if m:
                state_refresh_origination = m.groupdict()['state_refresh_origination']

            # PIM NBMA mode: disabled
            p15 = re.compile(r'^\s*PIM +NBMA +mode:'
                             ' +(?P<nbma_mode>\w+)$')
            m = p15.match(line)
            if m:
                nbma_mode = m.groupdict()['nbma_mode']

            # PIM ATM multipoint signalling: disabled
            p16 = re.compile(r'^\s*PIM +ATM +multipoint +signalling:'
                             ' +(?P<atm_multipoint>\w+)$')
            m = p16.match(line)
            if m:
                atm_multipoint = m.groupdict()['atm_multipoint']

            # PIM domain border: disabled
            p17 = re.compile(r'^\s*PIM +domain +border:'
                             ' +(?P<domain_border>\w+)$')
            m = p17.match(line)
            if m:
                domain_border = m.groupdict()['domain_border']

            # PIM neighbors rpf proxy capable: TRUE
            p18 = re.compile(r'^\s*PIM +neighbors +rpf +proxy +capable:'
                             ' +(?P<neighbors_rpf_proxy_capable>\w+)$')
            m = p18.match(line)
            if m:
                neighbors_rpf_proxy_capable = m.groupdict()['neighbors_rpf_proxy_capable']

            # PIM BFD: disabled
            p19 = re.compile(r'^\s*PIM +BFD:'
                             ' +(?P<bfd>\w+)$')
            m = p19.match(line)
            if m:
                bfd = m.groupdict()['bfd']

            # PIM Non-DR-Join: FALSE
            p20 = re.compile(r'^\s*PIM +Non-DR-Join:'
                             ' +(?P<non_dr_join>\w+)$')
            m = p20.match(line)
            if m:
                non_dr_join = m.groupdict()['non_dr_join']

            # Multicast Tagswitching: disabled
            p21 = re.compile(r'^\s*Multicast +Tagswitching:'
                             ' +(?P<tagswitching>\w+)$')
            m = p21.match(line)
            if m:
                tagswitching = m.groupdict()['tagswitching']

            if intf_name:
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}

                if 'interfaces' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['interfaces'] = {}
                if intf_name not in ret_dict['vrf'][vrf]['interfaces']:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]['interfaces'][intf_name]:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] = {}
                if af_name not in ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name] = {}

                if bfd:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                        [af_name]['bfd'] ={}
                    if bfd.lower() == 'enabled':
                        enable = True
                    else:
                        enable = False
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                            [af_name]['bfd']['enable'] = enable

                if hello_interval is not None:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['hello_interval'] = hello_interval

                if hello_packet_in is not None:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['hello_packets_in'] = hello_packet_in

                if hello_packet_out is not None:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['hello_packets_out'] = hello_packet_out

                if oper_status:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['oper_status'] = oper_status
                if address:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['address'] = address.split()

                if multi_switching:
                    if 'multicast' not in ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                            [af_name]:
                        ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                            [af_name]['multicast'] = {}
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                            [af_name]['multicast']['switching'] = multi_switching

                if multi_packet_in is not None:
                    if 'multicast' not in ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                            [af_name]:
                        ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                            [af_name]['multicast'] = {}
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['multicast']['packets_in'] = multi_packet_in

                if multi_packet_out is not None:
                    if 'multicast' not in ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                            [af_name]:
                        ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                            [af_name]['multicast'] = {}
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['multicast']['packets_out'] = multi_packet_out

                if ttl_threshold is not None:
                    if 'multicast' not in ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                            [af_name]:
                        ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                            [af_name]['multicast'] = {}
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['multicast']['ttl_threshold'] = ttl_threshold

                if tagswitching:
                    if 'multicast' not in ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                            [af_name]:
                        ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                            [af_name]['multicast'] = {}
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['multicast']['tag_switching'] = tagswitching

                if pim_status:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['pim_status'] = pim_status

                if version is not None:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['version'] = version

                if mode is not None:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['mode'] = mode

                if dr_address:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['dr_address'] = dr_address
                if nbr_count is not None:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['neighbor_count'] = nbr_count

                if jp_interval is not None:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['jp_interval'] = jp_interval

                if  state_refresh_processing:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['state_refresh_processing'] = state_refresh_processing

                if state_refresh_origination:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['state_refresh_origination'] = state_refresh_origination

                if nbma_mode:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['nbma_mode'] = nbma_mode

                if atm_multipoint:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['atm_multipoint_signalling'] = atm_multipoint

                if  domain_border:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['domain_border'] = domain_border

                if neighbors_rpf_proxy_capable:
                    if neighbors_rpf_proxy_capable.lower() == 'true':
                        nbr_val = True
                    else:
                        nbr_val = False
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['neighbors_rpf_proxy_capable'] = nbr_val

                if non_dr_join:
                    if non_dr_join.lower() == 'true':
                        dr_join_val = True
                    else:
                        dr_join_val = False
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['none_dr_join'] = dr_join_val
                continue

        return ret_dict
