"""show_xconnect.py

show xsconnect parser class

  supported commands:
   *  show l2vpn xconnect
   
"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                               Any, \
                                               Optional, \
                                               Or, \
                                               And, \
                                               Default, \
                                               Use

from genie.libs.parser.base import *
from genie.libs.parser.utils.common import Common

# class ShowL2VpnXconnectSummary(MetaParser):
#     """Parser for show l2vpn xconnect summary"""
#     # parser class - implements detail parsing mechanisms for cli output.


#     #*************************
#     # schema - class variable
#     #
#     # Purpose is to make sure the parser always return the output
#     # (nested dict) that has the same data structure across all supported
#     # parsing mechanisms (cli(), yang(), xml()).
#     """
#     schema = {'TODO:': {
#                         'module': {
#                                  Any(): {
#                                          'bios_compile_time': str,
#                                          'bios_version': str,
#                                          'image_compile_time': str,
#                                          'image_version': str,
#                                          'status': str},}},
#               'hardware': {
#                         'bootflash': str,
#                         'chassis': str,
#                         'cpu': str,
#                         'device_name': str,
#                         'memory': str,
#                         'model': str,
#                         'processor_board_id': str,
#                         'slots': str,
#                         Any(): str,},
#               'kernel_uptime': {
#                         'days': str,
#                         'hours': str,
#                         'minutes': str,
#                         'seconds': str},
#               'reason': str,
#               'software': {
#                         'bios': str,
#                         'bios_compile_time': str,
#                         'kickstart': str,
#                         'kickstart_compile_time': str,
#                         'kickstart_image_file': str,
#                         'system': str,
#                         'system_compile_time': str,
#                         'system_image_file': str},
#               'system_version': str,
#               Any(): str,}
#     """
#     cli_command = 'show l2vpn xconnect summary'

#     def cli(self):
#         '''parsing mechanism: cli
#         '''

#         tcl_package_require_caas_parsers()
#         kl = tcl_invoke_caas_abstract_parser(
#             device=self.device, exec=self.cli_command)

#         return kl


# class ShowL2VpnXconnectBrief(MetaParser):
#     """Parser for show l2vpn xconnect brief"""
#     # parser class - implements detail parsing mechanisms for cli output.


#     #*************************
#     # schema - class variable
#     #
#     # Purpose is to make sure the parser always return the output
#     # (nested dict) that has the same data structure across all supported
#     # parsing mechanisms (cli(), yang(), xml()).
#     """
#     schema = {'TODO:': {
#                         'module': {
#                                  Any(): {
#                                          'bios_compile_time': str,
#                                          'bios_version': str,
#                                          'image_compile_time': str,
#                                          'image_version': str,
#                                          'status': str},}},
#               'hardware': {
#                         'bootflash': str,
#                         'chassis': str,
#                         'cpu': str,
#                         'device_name': str,
#                         'memory': str,
#                         'model': str,
#                         'processor_board_id': str,
#                         'slots': str,
#                         Any(): str,},
#               'kernel_uptime': {
#                         'days': str,
#                         'hours': str,
#                         'minutes': str,
#                         'seconds': str},
#               'reason': str,
#               'software': {
#                         'bios': str,
#                         'bios_compile_time': str,
#                         'kickstart': str,
#                         'kickstart_compile_time': str,
#                         'kickstart_image_file': str,
#                         'system': str,
#                         'system_compile_time': str,
#                         'system_image_file': str},
#               'system_version': str,
#               Any(): str,}
#     """
#     cli_command = 'show l2vpn xconnect brief'
#     def cli(self):
#         '''parsing mechanism: cli
#         '''

#         tcl_package_require_caas_parsers()
#         kl = tcl_invoke_caas_abstract_parser(
#             device=self.device, exec=self.cli_command)

#         return kl


# class ShowL2VpnXconnectDetail(MetaParser):
#     """Parser for show l2vpn xconnect detail"""
#     # parser class - implements detail parsing mechanisms for cli output.

#     #*************************
#     # schema - class variable
#     #
#     # Purpose is to make sure the parser always return the output
#     # (nested dict) that has the same data structure across all supported
#     # parsing mechanisms (cli(), yang(), xml()).
#     """
#     schema = {'cmp': {
#                         'module': {
#                                  Any(): {
#                                          'bios_compile_time': str,
#                                          'bios_version': str,
#                                          'image_compile_time': str,
#                                          'image_version': str,
#                                          'status': str},}},
#               'hardware': {
#                         'bootflash': str,
#                         'chassis': str,
#                         'cpu': str,
#                         'device_name': str,
#                         'memory': str,
#                         'model': str,
#                         'processor_board_id': str,
#                         'slots': str,
#                         Any(): str,},
#               'kernel_uptime': {
#                         'days': str,
#                         'hours': str,
#                         'minutes': str,
#                         'seconds': str},
#               'reason': str,
#               'software': {
#                         'bios': str,
#                         'bios_compile_time': str,
#                         'kickstart': str,
#                         'kickstart_compile_time': str,
#                         'kickstart_image_file': str,
#                         'system': str,
#                         'system_compile_time': str,
#                         'system_image_file': str},
#               'system_version': str,
#               Any(): str,}
#     """
#     cli_command = 'show l2vpn xconnect detail'

#     def cli(self):
#         '''parsing mechanism: cli
#         '''


#         tcl_package_require_caas_parsers()
#         kl = tcl_invoke_caas_abstract_parser(
#             device=self.device, exec=self.cli_command)

#         return kl


# class ShowL2VpnXconnectMp2mpDetail(MetaParser):
#     """Parser for show l2vpn xconnect mp2mp detail"""
#     # parser class - implements detail parsing mechanisms for cli output.

#     #*************************
#     # schema - class variable
#     #
#     # Purpose is to make sure the parser always return the output
#     # (nested dict) that has the same data structure across all supported
#     # parsing mechanisms (cli(), yang(), xml()).
#     """
#     schema = {'cmp': {
#                         'module': {
#                                  Any(): {
#                                          'bios_compile_time': str,
#                                          'bios_version': str,
#                                          'image_compile_time': str,
#                                          'image_version': str,
#                                          'status': str},}},
#               'hardware': {
#                         'bootflash': str,
#                         'chassis': str,
#                         'cpu': str,
#                         'device_name': str,
#                         'memory': str,
#                         'model': str,
#                         'processor_board_id': str,
#                         'slots': str,
#                         Any(): str,},
#               'kernel_uptime': {
#                         'days': str,
#                         'hours': str,
#                         'minutes': str,
#                         'seconds': str},
#               'reason': str,
#               'software': {
#                         'bios': str,
#                         'bios_compile_time': str,
#                         'kickstart': str,
#                         'kickstart_compile_time': str,
#                         'kickstart_image_file': str,
#                         'system': str,
#                         'system_compile_time': str,
#                         'system_image_file': str},
#               'system_version': str,
#               Any(): str,}
#     """
#     cli_command = 'show l2vpn xconnect mp2mp detail'

#     def cli(self):
#         '''parsing mechanism: cli
#         '''

#         tcl_package_require_caas_parsers()
#         kl = tcl_invoke_caas_abstract_parser(
#             device=self.device, exec=self.cli_command)

#         return kl

# # vim: ft=python ts=8 sw=4 et

class ShowL2vpnXconnectDetailSchema(MetaParser):
    schema = {
        'group': {
            Any(): {
                'xc': {
                    Any(): {
                        'state': str,
                        'interworking': str,
                        'monitor_session': {
                            Any(): {
                                'state': str
                            }
                        },
                        'ac':{
                            Any(): {
                                'state': str,
                                'type': str,
                                'mtu': int,
                                'xc_id': str,
                                'interworking': str,
                                'msti': int,
                                'statistics': {
                                    'packet_totals': {
                                        'send': int
                                    },
                                    'byte_totals': {
                                        'send': int
                                    }
                                }
                            }
                        },
                        'pw': {
                            'neighbor': str,
                            'id': int,
                            'state': str,
                            'class_set': bool,
                            'xc_id': str,
                            'encapsulation': str,
                            'protocol': str,
                            'type': str,
                            'control_word': str,
                            'interworking': str,
                            'backup_disable_delay': int,
                            'sequencing_set': bool,
                            'mpls': {
                                Any(): {
                                    'local': str,
                                    'remote': str
                                }
                            },
                            'create_time': str,
                            'last_time_status_changed': str,
                            'statistics': {
                                'packet_totals': {
                                    'receive': int
                                },
                                'byte_totals': {
                                    'receive': int
                                }
                            }
                        },
                        'backup_pw': {
                            'neighbor': str,
                            'id': int,
                            'state': str,
                            'class_set': bool,
                            'xc_id': str,
                            'encapsulation': str,
                            'protocol': str,
                            'type': str,
                            'control_word': str,
                            'interworking': str,
                            'backup_disable_delay': int,
                            'sequencing_set': bool,
                            'mpls': {
                                Any(): {
                                    'local': str,
                                    'remote': str
                                }
                            },
                            'create_time': str,
                            'last_time_status_changed': str,
                            'statistics': {
                                'packet_totals': {
                                    'receive': int
                                },
                                'byte_totals': {
                                    'receive': int
                                }
                            },
                        },
                    },
                },
            },
        },
    }

class ShowL2vpnXconnectDetail(ShowL2vpnXconnectDetailSchema):
    """Parser for show l2vpn xconnect detail"""

    cli_command = 'show l2vpn xconnect detail'
    def cli(self, output=None):
        out = output if output else self.device.execute(self.cli_command)
        ret_dict = {}
        current_dict = None
        pw_backup = False
        # Group siva_xc, XC siva_p2p, state is down; Interworking none
        p1 = re.compile(r'^Group +(?P<group>\S+), +XC +(?P<xc>\S+), +'
            'state +is +(?P<state>\S+); +Interworking +(?P<interworking>\S+)')

        # Monitor-Session: pw-span-test, state is configured
        p2 = re.compile(r'^Monitor\-Session: +(?P<monitor_session>\S+)'
            ', +state +is +(?P<state>\S+)$')

        # AC: GigabitEthernet0/4/0/1, state is up
        p3 = re.compile(r'^AC: +(?P<ac>\S+), +state +is +(?P<state>\S+)$')

        # Type Ethernet
        p4 = re.compile(r'^Type +(?P<type>\S+)$')

        # MTU 1500; XC ID 0x5000001; interworking none; MSTi 0
        p5 = re.compile(r'^MTU +(?P<mtu>\d+); +XC +ID +(?P<xc_id>\S+); '
            '+interworking +(?P<interworking>\S+); +MSTi +(?P<msti>\d+)$')

        # packet totals: send 98
        p6 = re.compile(r'^packet +totals: +send +(?P<send>\d+)$')
        
        # packet totals: receive 98
        p6_1 = re.compile(r'^packet +totals: +receive +(?P<receive>\d+)$')

        # byte totals: send 20798
        p7 = re.compile(r'^byte +totals: +send +(?P<send>\d+)$')

        # byte totals: send 20798
        p7_1 = re.compile(r'^byte +totals: +receive +(?P<receive>\d+)$')

        # PW: neighbor 10.1.1.1, PW ID 1, state is down ( local ready )
        p8 = re.compile(r'^PW: +neighbor +(?P<neighbor>\S+), +PW +ID +'
            '(?P<id>\d+), state +is +(?P<state>[\S ]+)$')
        
        # PW class not set, XC ID 0x5000001
        p9 = re.compile(r'^PW +class +not +set, +XC +ID +(?P<xc_id>\S+)$')

        # Encapsulation MPLS, protocol LDP
        p10 = re.compile(r'^Encapsulation +(?P<encapsulation>\S+), +protocol +(?P<protocol>\S+)$')

        # PW type Ethernet, control word enabled, interworking none
        p11 = re.compile(r'^PW +type +(?P<type>\S+), +control +word +(?P<control_word>\S+)'
            ', +interworking +(?P<interworking>\S+)$')

        # PW backup disable delay 0 sec
        p12 = re.compile(r'^PW +backup +disable +delay +(?P<backup_disable_delay>\d+) +sec$')

        # Sequencing not set
        p13 = re.compile(r'^Sequencing +not +set$')

        # MPLS         Local                          Remote
        p14 = re.compile(r'^MPLS +Local +Remote$')

        # Label        30005                          unknown
        # Group ID     0x5000300                      0x0
        # VCCV CV type 0x2                            0x0
        p15 = re.compile(r'^(?P<mpls>[\S ]+) +(?P<local>\S+) +(?P<remote>\S+)$')

        # Create time: 20/11/2007 21:45:06 (00:53:31 ago)
        p16 = re.compile(r'^Create +time: +(?P<create_time>[\S ]+)$')

        # Last time status changed: 20/11/2007 22:38:14 (00:00:23 ago)
        p17 = re.compile(r'^Last +time +status +changed: +(?P<last_time_status_changed>[\S ]+)$')

        # Backup PW:
        p18 = re.compile(r'^Backup +PW:$')

        # ------------ ------------------------------ -----------------------------
        p19 = re.compile(r'^-+ +-+ +-+$')

        # (control word)                 (control word)  
        p20 = re.compile(r'^\([\S ]+\)$')

        # Backup for neighbor 10.1.1.1 PW ID 1 ( active )
        p21 = re.compile(r'^Backup( +PW)? +for +neighbor +\S+ +PW +ID +\d+( +\( +\w+ +\))?$')


        for line in out.splitlines():
            line = line.strip()
            
            # Group siva_xc, XC siva_p2p, state is down; Interworking none
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_name = group['group']
                xc = group['xc']
                state = group['state']
                interworking = group['interworking']

                xc_dict = ret_dict.setdefault('group', {}). \
                    setdefault(group_name, {}). \
                    setdefault('xc', {}). \
                    setdefault(xc, {})

                xc_dict.update({'state': state})
                xc_dict.update({'interworking': interworking})
                continue
            
            # Monitor-Session: pw-span-test, state is configured
            m = p2.match(line)
            if m:
                group = m.groupdict()
                monitor_session = group['monitor_session']
                state = group['state']
                monitor_session_dict = xc_dict.setdefault('monitor_session', {}). \
                    setdefault(monitor_session, {})
                monitor_session_dict.update({'state': state})
                continue

            # AC: GigabitEthernet0/4/0/1, state is up 
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ac = group['ac']
                state = group['state']
                current_dict = xc_dict.setdefault('ac', {}). \
                    setdefault(ac, {})
                current_dict.update({'state': state})
                continue
            
            # Type Ethernet
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ac_type = group['type']
                current_dict.update({'type': ac_type})
                continue

            # MTU 1500; XC ID 0x5000001; interworking none; MSTi 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                mtu = int(group['mtu'])
                xc_id = group['xc_id']
                interworking = group['interworking']
                msti = int(group['msti'])
                current_dict.update({'mtu': mtu})
                current_dict.update({'xc_id': xc_id})
                current_dict.update({'interworking': interworking})
                current_dict.update({'msti': msti})
                continue
            
            # packet totals: send 98
            m = p6.match(line)
            if m:
                group = m.groupdict()
                send = int(group['send'])
                current_dict.setdefault('statistics', {}). \
                    setdefault('packet_totals', {}). \
                    update({'send': send})
                continue

            # packet totals: receive 98
            m = p6_1.match(line)
            if m:
                group = m.groupdict()
                receive = int(group['receive'])
                current_dict.setdefault('statistics', {}). \
                    setdefault('packet_totals', {}). \
                    update({'receive': receive})
                continue

            # byte totals: send 98
            m = p7.match(line)
            if m:
                group = m.groupdict()
                send = int(group['send'])
                current_dict.setdefault('statistics', {}). \
                    setdefault('byte_totals', {}). \
                    update({'send': send})
                continue
            
            # byte totals: receive 98
            m = p7_1.match(line)
            if m:
                group = m.groupdict()
                receive = int(group['receive'])
                current_dict.setdefault('statistics', {}). \
                    setdefault('byte_totals', {}). \
                    update({'receive': receive})
                continue

            # PW: neighbor 10.1.1.1, PW ID 1, state is down ( local ready )
            m = p8.match(line)
            if m:
                group = m.groupdict()
                neighbor = group['neighbor']
                pw_id = int(group['id'])
                state = group['state']
                if not pw_backup:
                    current_dict = xc_dict.setdefault('pw', {})
                current_dict.update({'neighbor': neighbor})
                current_dict.update({'id': pw_id})
                current_dict.update({'state': state})
                continue
            
            # PW class not set, XC ID 0x5000001
            m = p9.match(line)
            if m:
                group = m.groupdict()
                xc_id = group['xc_id']
                current_dict.update({'class_set': False})
                current_dict.update({'xc_id': xc_id})
                continue

            # Encapsulation MPLS, protocol LDP
            m = p10.match(line)
            if m:
                group = m.groupdict()
                encapsulation = group['encapsulation']
                protocol = group['protocol']
                current_dict.update({'encapsulation': encapsulation})
                current_dict.update({'protocol': protocol})
                continue
            
            # PW type Ethernet, control word enabled, interworking none
            m = p11.match(line)
            if m:
                group = m.groupdict()
                pw_type = group['type']
                control_word = group['control_word']
                interworking = group['interworking']
                current_dict.update({'type': pw_type})
                current_dict.update({'control_word': control_word})
                current_dict.update({'interworking': interworking})
                continue

            # PW backup disable delay 0 sec
            m = p12.match(line)
            if m:
                group = m.groupdict()
                backup_disable_delay = int(group['backup_disable_delay'])
                current_dict.update({'backup_disable_delay': backup_disable_delay})
                continue

            # Sequencing not set
            m = p13.match(line)
            if m:
                current_dict.update({'sequencing_set': False})
                continue

            # MPLS         Local                          Remote
            m = p14.match(line)
            if m:
                continue
            
            # Create time: 20/11/2007 21:45:06 (00:53:31 ago)
            m = p16.match(line)
            if m:
                group = m.groupdict()
                create_time = group['create_time']
                current_dict.update({'create_time': create_time})
                continue
            
            # Last time status changed: 20/11/2007 22:38:14 (00:00:23 ago)
            m = p17.match(line)
            if m:
                group = m.groupdict()
                last_time_status_changed = group['last_time_status_changed']
                current_dict.update({'last_time_status_changed': last_time_status_changed})
                continue
            
            # Backup PW:
            m = p18.match(line)
            if m:
                current_dict = xc_dict.setdefault('backup_pw', {})
                pw_backup = True
                continue
            
            # ------------ ------------------------------ -----------------------------
            m = p19.match(line)
            if m:
                continue
            
            # (control word)                 (control word)
            m = p20.match(line)
            if m:
                continue

            # Backup for neighbor 10.1.1.1 PW ID 1 ( active )
            m = p21.match(line)
            if m:
                continue

            # Label        30005                          unknown
            # Group ID     0x5000300                      0x0
            # VCCV CV type 0x2                            0x0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                mpls = group['mpls'].strip()
                local = group['local'].strip()
                remote = group['remote']
                mpls_dict = current_dict.setdefault('mpls', {}). \
                    setdefault(mpls, {})
                mpls_dict.update({'local': local})
                mpls_dict.update({'remote': remote})
                continue

        return ret_dict

class ShowL2vpnXconnectSchema(MetaParser):
    """Schema for show l2vpn xconnect"""
    schema = {
        'groups': {
            Any(): {
                'name': {
                    Any(): {
                        'status': str,
                        'segment1': {
                            Any(): {
                                'status': str,
                                'segment2': {
                                    Any(): {
                                        Optional('pw_id'): str,
                                        'status': str,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


class ShowL2vpnXconnect(ShowL2vpnXconnectSchema):
    """Parser for show l2vpn xconnect """

    cli_command = 'show l2vpn xconnect'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}
        flag_group = True

        # L2TPV3_V4_XC_GRP
        #           L2TPV3_P2P_1
        p1 = re.compile(r'^(?P<group>[\w]+)$')

        #               1000     DN   Gi0/0/0/5.1000    UP   10.4.1.206       1000   DN
        p2 = re.compile(r'^(?P<name>[a-zA-Z0-9]+) '
                        '+(?P<status_group>(UP|DN|AD|UR|SB|SR|\(PP\))) '
                        '+(?P<segment_1>.*?) ' 
                        '+(?P<status_seg1>(UP|DN|AD|UR|SB|SR|\(PP\))) '
                        '+(?P<segment_2>\S*) ' 
                        '+(?P<pw_id>\S*)? '
                        '+(?P<status_seg2>(UP|DN|AD|UR|SB|SR|\(PP\)))$')

        #                        UP   Gi0/2/0/1.2            UP       10.154.26.26     100    UP  
        p3 = re.compile(r'^(?P<status_group>(UP|DN|AD|UR|SB|SR|\(PP\))) '
                        '+(?P<segment_1>.*?) ' 
                        '+(?P<status_seg1>(UP|DN|AD|UR|SB|SR|\(PP\))) '
                        '+(?P<segment_2>\S*) ' 
                        '+(?P<pw_id>\S*)? '
                        '+(?P<status_seg2>(UP|DN|AD|UR|SB|SR|\(PP\)))$')

        for line in out.splitlines():
            line = line.strip()
            
            m = p1.match(line)
            if m:
                if flag_group:
                    group = m.groupdict()
                    group_dict = ret_dict.setdefault('groups', {}) \
                        .setdefault(str(group['group']), {})
                    flag_group = False
                    continue
                else:
                    group = m.groupdict()
                    name_dict = group_dict.setdefault('name', {}) \
                        .setdefault(str(group['group']), {})
                    flag_group = True
                    continue

            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                name_dict = group_dict.setdefault('name', {}) \
                    .setdefault(str(group['name']), {})
                flag_group = True
            
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()

            if m2 or m3:
                name_dict['status'] = str(group['status_group'])
                segment1_dict = name_dict.setdefault('segment1',{}) \
                    .setdefault(Common.convert_intf_name(group['segment_1']), {})
                segment1_dict['status'] = str(group['status_seg1'])
                segment2_dict = segment1_dict.setdefault('segment2', {}) \
                    .setdefault( str(group['segment_2']), {}) 
                segment2_dict['status'] = str(group['status_seg2'])
                if group['pw_id']:
                  segment2_dict['pw_id'] = str(group['pw_id'])

        return ret_dict