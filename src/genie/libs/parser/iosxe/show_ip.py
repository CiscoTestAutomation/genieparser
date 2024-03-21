'''
show_ip.py

IOSXE parsers for the following show commands:
    * show ip aliases
	* show ip aliases default-vrf
	* show ip aliases vrf {vrf}
    * show ip vrf
    * show ip vrf <vrf>
    * show ip vrf detail
    * show ip vrf detial <vrf>
    * show ip sla summary
    * show ip nbar classification socket-cache <number_of_sockets>
    * show ip nbar version
    * show ip nat translations
    * show ip nat translations total
    * show ip nat translations vrf {vrf} total    
    * show ip nat translations verbose
    * show ip nat statistics
    * show ip dhcp database
    * show ip dhcp snooping database
    * show ip dhcp snooping database detail
    * show ip dhcp snooping binding
    * show ip mfib
    * show ip mfib {group}
    * show ip mfib {group} {source}
    * show ip mfib verbose
    * show ip mfib {group} verbose
    * show ip mfib {group} {source} verbose
    * show ip mfib vrf {vrf}
    * show ip mfib vrf {vrf} {group}
    * show ip mfib vrf {vrf} {group} {source}
    * show ip mfib vrf {vrf} verbose
    * show ip mfib vrf {vrf} {group} verbose
    * show ip mfib vrf {vrf} {group} {source} verbose
    *  show ip mrib route
    * show ip mrib route {group}
    * show ip mrib route {group} {source}
    * show ip mrib route vrf {vrf}
    * show ip mrib route vrf {vrf} {group}
    * show ip mrib route vrf {vrf} {group} {source}
    * show ip sla statistics
    * show ip sla statistics {probe_id}
    * show ip sla statistics details
    * show ip sla statistics {probe_id} details
    * show ip sla statistics aggregated
    * show ip sla statistics aggregated {probe_id}
    * show ip sla responder
    * show ip nhrp traffic
    * show ip nhrp traffic interface {interface}
    * show ip nhrp traffic detail
    * show ip nhrp traffic interface {interface} detail
    * show ip nhrp stats
    * show ip nhrp stats {tunnel}
    * show ip nhrp stats detail
    * show ip nhrp stats {tunnel} detail
    * show ip nhrp
    * show ip nhrp detail
    * show ip nhrp nhs
    * show ip nhrp nhs {tunnel}
    * show nhrp stats
    * show nhrp stats {tunnel}
    * show nhrp stats detail
    * show nhrp stats {tunnel} detail
    * show ip dhcp binding
    * show ip dhcp binding vrf {vrf_name}
    * show ip dhcp binding | count Active
    * show ip nhrp summary
    * show ip dhcp snooping binding | include Total number of bindings
    * show ip dhcp snooping | include gleaning
    * show ip dns view
    * show ip admission cache
    * show ip igmp snooping detail
    * show ip verify source interface {interface}
    * show ip verify source
    * show ip dhcp excluded-addresses all
    * show ip dhcp excluded-addresses vrf {vrf}
    * show ip dhcp excluded-addresses pool {pool}
    * show ip http server all
    * show ip http server secure status
    * show ip dhcp snooping binding interface {interface}
    * show ip dhcp snooping binding {mac}
    * show ip name-servers
    * show ip name-servers vrf {vrf}
    '''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, ListOf, And,\
                                         Default, Use
# parser utils
from genie.libs.parser.utils.common import Common
from genie.libs.parser.iosxe.show_vrf import ShowVrfDetailSchema, ShowVrfDetailSuperParser

# ==============================
# Schema for 'show ip aliases', 'show ip aliases vrf {vrf}'
# ==============================
class ShowIPAliasSchema(MetaParser):
    '''
	Schema for:
	show ip aliases
	show ip aliases vrf {vrf}
	'''
    schema = {
        'vrf': {
            Any(): {
                'index': {
                    Any(): { # just incrementing 1, 2, 3, ... per entry
                        'address_type': str,
                        'ip_address': str,
                        Optional('port'): int,
                    },
                },
            },
        },
    }

# ==============================
# Parser for 'show ip aliases', 'show ip aliases vrf {vrf}'
# ==============================
class ShowIPAlias(ShowIPAliasSchema):
    '''
    Parser for:
    show ip aliases
    show ip aliases vrf {vrf}
    '''
    cli_command = ['show ip aliases',
        'show ip aliases vrf {vrf}']

    def cli(self, vrf = '', output = None):
        if output is None:
            if vrf:
                out = self.device.execute(self.cli_command[1].format(vrf = vrf))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Init vars
        parsed_dict = {}
        index = 1   # set a counter for the index

        # Address Type             IP Address      Port
        # Interface                10.169.197.94
        p1 = re.compile(r'(?P<address_type>(\S+)) +(?P<ip_address>(\S+))(?: +(?P<port>(\d+)))?$')
        # "?:" (for port) means optional

        for line in out.splitlines():
            line = line.strip()

            # Interface                10.169.197.94
            m = p1.match(line)
            if m:
                group = m.groupdict()
                if vrf:
                    vrf = vrf
                else:
                    vrf = 'default'
                vrf_dict = parsed_dict.setdefault('vrf', {}).\
                                       setdefault(vrf, {}).\
                                       setdefault('index', {}).\
                                       setdefault(index, {})
                vrf_dict['address_type'] = group['address_type']
                vrf_dict['ip_address'] = group['ip_address']
                if group['port']:
                    vrf_dict['port'] = int(group['port'])

                index += 1
                continue

        return parsed_dict

# ==============================
# Parser for show ip aliases default-vrf'
# ==============================
class ShowIPAliasDefaultVrf(ShowIPAlias):
    '''
    Parser for:
	show ip aliases default-vrf
	'''
    cli_command = 'show ip aliases default-vrf'

    def cli(self, output = None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output

        return super().cli(output = show_output)


class ShowIpVrfSchema(MetaParser):
    """Schema for
        * 'show ip vrf'
        * 'show ip vrf <vrf>'"""

    schema = {'vrf':
                {Any():
                    {Optional('route_distinguisher'): str,
                     'interfaces': list,
                    }
                },
            }


class ShowIpVrf(ShowIpVrfSchema):
    """Parser for:
        * 'show ip vrf'
        * 'show ip vrf <vrf>'"""

    cli_command = ['show ip vrf', 'show ip vrf {vrf}']
    def cli(self, vrf='', output=None):

        cmd = ""
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        #   Name                             Default RD            Interfaces
        #   Mgmt-intf                        <not set>             Gi1
        #   VRF1                             65000:1               Tu1
        #                                                          Lo300
        #                                                          Gi2.390
        p1 = re.compile(r'^(?P<vrf>[\S]+)\s+'
            '(?P<rd>([\d\:]+|(<not set>)))\s+'
            '(?P<interfaces>[\w\/\.\-]+)$')
        p2 = re.compile(r'(?P<interfaces>[\w\/\.\-]+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                groups = m.groupdict()
                vrf_dict = ret_dict.setdefault('vrf',{}).setdefault(groups['vrf'],{})
                if 'not' not in groups['rd']:
                    vrf_dict['route_distinguisher'] = str(groups['rd'])
                vrf_dict['interfaces'] = [Common.convert_intf_name(groups['interfaces'])]
                continue

            m = p2.match(line)
            if m:
                groups = m.groupdict()
                if 'interfaces' in vrf_dict:
                    vrf_dict.get('interfaces').append(Common.convert_intf_name(groups['interfaces']))

        return ret_dict


class ShowIpVrfDetail(ShowVrfDetailSuperParser):
    """Parser for
        * 'show ip vrf detail'
        * 'show ip vrf detail <vrf>'"""
    cli_command = ['show ip vrf detail' , 'show ip vrf detail {vrf}']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        return super().cli(output=show_output)


# ===============================
# Schema for 'show ip sla summary'
# ===============================
class ShowIpSlaSummarySchema(MetaParser):
    ''' Schema for "show ip sla summary" '''
    schema = {
        'ids': {
            Any(): {
                'state': str,
                'type': str,
                'destination': str,
                'rtt_stats': str,
                Optional('rtt_stats_msecs'): int,
                'return_code': str,
                'last_run': str,
            },
        }
    }


# ===============================
# Parser for 'show ip sla summary'
# ===============================
class ShowIpSlaSummary(ShowIpSlaSummarySchema):
    """Parser for:
    show ip sla summary
    """
    cli_command = 'show ip sla summary'

    def cli(self, output=None):

        parsed_dict = {}

        if output is None:
            output = self.device.execute(self.cli_command)

        # ID           Type        Destination       Stats       ReturnCode  LastRun
        # -----------------------------------------------------------------------
        # *1           tcp-connect 10.151.213.32     RTT=44      OK          21 seconds ago
        # *2           dns         10.84.2.123      -           Timeout     7 seconds ago
        # *3           udp-jitter  10.204.11.1       RTT=1       OK          54 seconds ago
        # *4           udp-jitter  10.145.33.3       RTT=1       OK          15 seconds ago
        # *5           udp-jitter  10.115.32.2       RTT=1       OK          8 seconds ago
        # *6           udp-jitter  11.311.31.2       RTT=1       OK          40 seconds ago
        # *7           icmp-echo   172.16.94.1       RTT=1       OK          2 seconds ago

        # ID       Type      Destination  State   Stats(ms)  ReturnCode  LastRun
        # ---      ----      -----------  -----   -------  ----------  -------
        # 100   icmp-jitter   192.0.2.2    Active   100      OK       22:49:53 PST Tue May 3 2011
        # 101   udp-jitter    192.0.2.2    Active   100      OK       22:49:53 PST Tue May 3 2011
        # 102   tcp-connect   192.0.2.2    Active    -      NoConnection  22:49:53 PST Tue May 3 2011
        # 103   video         1232:232  		 Active   100      OK       22:49:53 PST Tue May 3 2011
        #                       2001:db8::222
        # 104   video         1232:232  		 Active   100      OK       22:49:53 PST Tue May 3 2011
        #                       2001:db8::222

        p1 = re.compile(r'(?P<state_symbol>\*|\^|\~)?(?P<id>\d+) +'
            r'(?P<type>\S+) +(?P<destination>\S+)\s+(?P<state_word>\w+)?'
            r' +(?P<rtt_stats>\S+) +(?P<return_code>\w+) +'
            r'(?P<last_run>[\w\: ]+)')

        #                       2001:db8::222
        p2 = re.compile(r'(?P<extended_ip_address>[\d\:\.]+)')

        for line in output.splitlines():
            line = line.strip()

            #*1           tcp-connect 10.151.213.32     RTT=44      OK          21 seconds ago
            # 100   icmp-jitter   192.0.2.2    Active   100      OK       22:49:53 PST Tue May 3 2011
            m = p1.match(line)
            if m:
                group = m.groupdict()
                id = group['id']
                id_dict = parsed_dict.setdefault('ids', {}).setdefault(id, {})

                # State can be a *, ^, or ~ at front of line, or can be a word
                if group['state_symbol'] == '*':
                    id_dict['state'] = 'active'
                elif group['state_symbol'] == '^':
                    id_dict['state'] = 'inactive'
                elif group['state_symbol'] == '~':
                    id_dict['state'] = 'pending'
                else:
                    id_dict['state'] = group['state_word'].lower()

                id_dict['type'] = group['type']
                id_dict['destination'] = group['destination']
                id_dict['rtt_stats'] = group['rtt_stats']

                # Strip chars and convert 'rtt_stats' to an integer if possible
                rtt_stats_msecs = re.sub('[^0-9]', '', group['rtt_stats'])
                if rtt_stats_msecs != '':
                    id_dict['rtt_stats_msecs'] = int(rtt_stats_msecs)

                id_dict['return_code'] = group['return_code']
                id_dict['last_run'] = group['last_run']
                continue

            #                       2001:db8::222
            m = p2.match(line)
            if m:
                group = m.groupdict()
                id_dict['destination'] += group['extended_ip_address']
                continue

        return parsed_dict


class ShowIpNbarClassificationSocketSchema(MetaParser):
    """ Schema for the commands:
            * show ip nbar classification socket-cache <number_of_sockets>
    """

    schema = {
        'flow_cache': {
            Any():{
                'server_ip': str,
                'vrf': int,
                'port': int,
                'proto': str,
                'app_name': str,
                'is_valid': str,
                'is_black_list': str,
                'is_learn_ph': str,
                'expiry_time': int,
                'entry_type': str,
                'hit_count': int
            }
        }
    }


class ShowIpNbarClassificationSocket(ShowIpNbarClassificationSocketSchema):
    """
        * show ip nbar classification socket-cache <number_of_sockets>
    """

    cli_command = ['show ip nbar classification socket-cache {number_of_sockets}']

    def cli(self, number_of_sockets=None, output=None):
        if output is None:
            cmd = self.cli_command[0].format(number_of_sockets=number_of_sockets)
            out = self.device.execute(cmd)
        else:
            out = output

        # |10.169.188.209                          |    2|  443|TCP  |ssl                    |No   |No   |Yes  |633      |Infra|1      |
        p1 = re.compile(r'^\|(?P<server_ip>\S+)[\s|]+(?P<vrf>\d+)[\s|]+(?P<port>\d+)\|(?P<proto>\S+)[\s|]+(?P<app_name>\S+)[\s|]+(?P<is_valid>\w+)[\s|]+(?P<is_black_list>\w+)[\s|]+(?P<is_learn_ph>\w+)[\s|]+(?P<expiry_time>\d+)[\s|]+(?P<entry_type>\w+)\|(?P<hit_count>\d+)[\s|]+$')

        ret_dict = {}
        first_line = 1
        sess_num = 1
        for line in out.splitlines():
            line = line.strip()

            #zbfw zonepair-statistics ZP_lanZone_lanZone_Is_-902685811
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                if(first_line == 1):
                    first_line = first_line + 1
                    sess_dict = ret_dict.setdefault('flow_cache',{})

                feature_dict = sess_dict.setdefault(sess_num, {})
                feature_dict.update({'server_ip': groups['server_ip']})
                feature_dict.update({'vrf': int(groups['vrf'])})
                feature_dict.update({'port': int(groups['port'])})
                feature_dict.update({'proto': groups['proto']})
                feature_dict.update({'app_name': groups['app_name']})
                feature_dict.update({'is_valid': groups['is_valid']})
                feature_dict.update({'is_black_list': groups['is_black_list']})
                feature_dict.update({'is_learn_ph': groups['is_learn_ph']})
                feature_dict.update({'expiry_time': int(groups['expiry_time'])})
                feature_dict.update({'entry_type': groups['entry_type']})
                feature_dict.update({'hit_count': int(groups['hit_count'])})
                sess_num = sess_num + 1


        return(ret_dict)


# ==================================
# Schema for 'show ip nbar version'
# ==================================
class ShowIpNbarVersionSchema(MetaParser):
    '''Schema for:
        * show ip nbar version'''

    schema = {
        'nbar_software_version': str,
        'nbar_minimum_backward_compatible_version': str,
        'loaded_protocol_packs': {
            Any(): {
                'version': {
                    Any(): {
                        'file': str,
                        'publisher': str,
                        'creation_time': str,
                        'nbar_engine_version': str,
                        'state': str,
                    },
                },
            },
        },
    }

# ==================================
# Parser for 'show ip nbar version'
# ==================================
class ShowIpNbarVersion(ShowIpNbarVersionSchema):
    '''Parser for:
        * show ip nbar version'''

    cli_command = ['show ip nbar version']

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Initialize dictionaries
        parsed_dict = {}
        loaded_protocol_packs_dict = {}
        version_dict = {}

        # NBAR software version: 34
        p1 = re.compile('^NBAR software version:\s+(?P<nbar_software_version>.+)$')

        # NBAR minimum backward compatible version: 41
        p2 = re.compile('^NBAR minimum backward compatible version:\s+(?P<nbar_minimum_backward_compatible_version>.+)$')

        # Name: Advanced Protocol Pack
        p3 = re.compile('^Name:\s+(?P<name>.+)$')

        # Version: 41.0
        p4 = re.compile('^Version:\s+(?P<version>.+)$')

        # Publisher: Cisco Systems Inc.
        p5 = re.compile('^Publisher:\s+(?P<publisher>.+)$')

        # NBAR Engine Version: 31
        p6 = re.compile('^NBAR Engine Version:\s+(?P<nbar_engine_version>.+)$')

        # Creation time:  Mon Feb 11 09:42:11 UTC 2019
        p7 = re.compile('^Creation time:\s+(?P<creation_time>.+)$')

        # File: bootflash:sdavc/pp-adv-all-166.2-31-41.0.0.pack
        p8 = re.compile('^File:\s+(?P<file>.+)$')

        # State: Active
        p9 = re.compile('^State:\s+(?P<state>.+)$')

        for line in out.splitlines():
            line = line.strip()

            # NBAR software version: 34
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({'nbar_software_version': groups['nbar_software_version']})
                continue

            # NBAR minimum backward compatible version: 41
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({'nbar_minimum_backward_compatible_version': groups['nbar_minimum_backward_compatible_version']})
                continue

            # Name: Advanced Protocol Pack
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                loaded_protocol_packs_dict = parsed_dict.setdefault('loaded_protocol_packs',{}).setdefault(groups['name'],{})
                continue

            # Version: 41.0
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                version_dict = loaded_protocol_packs_dict.setdefault('version',{}).setdefault(groups['version'],{})
                continue

            # Publisher: Cisco Systems Inc.
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                version_dict.update({'publisher':groups['publisher']})
                continue

            # NBAR Engine Version: 31
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                version_dict.update({'nbar_engine_version':groups['nbar_engine_version']})
                continue

            # Creation time: Mon Feb 11 09:42:11 UTC 2019
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                version_dict.update({'creation_time':groups['creation_time']})
                continue

            # File: bootflash:sdavc/pp-adv-all-166.2-31-41.0.0.pack
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                version_dict.update({'file':groups['file']})
                continue

            # State: Active
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                version_dict.update({'state':groups['state']})
                continue

        return parsed_dict


class ShowIpNatTranslationsSchema(MetaParser):
    """ Schema for the commands:
            * show ip nat translations
            * show ip nat translations verbose
            * show ip nat translations vrf {vrf}
            * show ip nat translations vrf {vrf} verbose
    """

    schema = {
        'vrf': {
            Any(): {  # name of vrf
                'index': {
                    Any(): {  # 1, 2 ,3, ...
                        'protocol': str,
                        Optional('inside_global'): str,
                        Optional('inside_local'): str,
                        Optional('outside_local'): str,
                        Optional('outside_global'): str,
                        Optional('group_id'): int,
                        Optional('time_left'): str,
                        Optional('details'): {
                            'create': str,
                            'use': str,
                            'timeout': str,
                            'map_id_in': int,
                            'mac_address': str,
                            'input_idb': str,
                            'entry_id': str,
                            'use_count': int,
                        }
                    },
                },
            },
            Optional('number_of_translations'): int
        }
    }


class ShowIpNatTranslations(ShowIpNatTranslationsSchema):
    """
        * show ip nat translations
        * show ip nat translations verbose
        * show ip nat translations vrf {vrf}
        * show ip nat translations vrf {vrf} verbose
    """

    cli_command = ['show ip nat translations',
                   'show ip nat translations verbose',
                   'show ip nat translations vrf {vrf}',
                   'show ip nat translations vrf {vrf} verbose']

    def cli(self, vrf=None, option=None, output=None):
        if output is None:
            if option and vrf is None:
                cmd = self.cli_command[1].format(verbose=option)
            elif option and vrf:
                cmd = self.cli_command[3].format(vrf=vrf, verbose=option)
            elif vrf and option is None:
                cmd = self.cli_command[2].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]

            out = self.device.execute(cmd)
        else:
            out = output

        # udp  10.5.5.1:1025          192.0.2.1:4000 --- ---
        # udp  10.5.5.1:1024          192.0.2.3:4000 --- ---
        # udp  10.5.5.1:1026          192.0.2.2:4000 --- ---
        # --- 172.16.94.209     192.168.1.95 --- ---
        # --- 172.16.94.210     192.168.1.89 --- ---
        # udp 172.16.94.209:1220  192.168.1.95:1220  172.16.169.132:53    172.16.169.132:53
        # tcp 172.16.94.209:11012 192.168.1.89:11012 172.16.196.220:23    172.16.196.220:23
        # tcp 172.16.94.209:1067  192.168.1.95:1067  172.16.196.161:23    172.16.196.161:23
        # icmp 10.10.140.200:66      10.10.40.100:66       10.10.140.110:66      10.10.140.110:66
        # any ---                ---                10.1.0.2          10.144.0.2
        p1 = re.compile(r'^(?P<protocol>-+|udp|tcp|icmp|any) +(?P<inside_global>\S+) '
                        r'+(?P<inside_local>\S+) +(?P<outside_local>\S+) '
                        r'+(?P<outside_global>\S+)$')

        # create: 02/15/12 11:38:01, use: 02/15/12 11:39:02, timeout: 00:00:00
        # create 04/09/11 10:51:48, use 04/09/11 10:52:31, timeout: 00:01:00
        p2 = re.compile(r'^create(?:\:)? +(?P<create>[\S ]+), '
                        r'+use(?:\:)? +(?P<use>[\S ]+), +timeout(?:\:)? '
                        r'+(?P<timeout>\S+)$')

        # IOS-XE:
        # Map-Id(In): 1
        # IOS:
        # Map-Id(In):1, Mac-Address: 0000.0000.0000 Input-IDB: GigabitEthernet0/3/1
        p3 = re.compile(r'^Map\-Id\(In\)[\:|\s]+(?P<map_id_in>\d+)(?:[\,|\s]'
                        r'+Mac\-Address\: +(?P<mac_address>\S+) +Input\-IDB\: '
                        r'+(?P<input_idb>\S+))?$')

        # IOS-XE: Mac-Address: 0000.0000.0000    Input-IDB: TenGigabitEthernet1/1/0
        p4 = re.compile(r'^Mac-Address: +(?P<mac_address>\S+) +Input-IDB: '
                        r'+(?P<input_idb>\S+)$')

        # entry-id: 0x0, use_count:1
        p5 = re.compile(r'^entry-id: +(?P<entry_id>\S+), '
                        r'+use_count:+(?P<use_count>\d+)$')

        # Total number of translations: 3
        p6 = re.compile(r'^Total +number +of +translations: '
                        r'+(?P<number_of_translations>\d+)$')

        # Group_id:0   vrf: genie
        p7 = re.compile(r'^Group_id\:(?P<group_id>\d+) +vrf\: +(?P<vrf_name>\S+)$')

        # Format(H:M:S) Time-left :0:0:-1
        p8 = re.compile(r'^Format\S+ +Time\-left +\:(?P<time_left>\S+)$')

        # initialize variables
        ret_dict = {}
        index_dict = {}
        tmp_dict = {}
        index = 1
        m8_index = 1
        vrf_name = ''
        vrf_flag = False

        for line in out.splitlines():
            line = line.strip()

            # udp  10.5.5.1:1025          192.0.2.1:4000 --- ---
            # udp  10.5.5.1:1024          192.0.2.3:4000 --- ---
            # udp  10.5.5.1:1026          192.0.2.2:4000 --- ---
            # --- 172.16.94.209     192.168.1.95 --- ---
            # --- 172.16.94.210     192.168.1.89 --- ---
            # udp 172.16.94.209:1220  192.168.1.95:1220  172.16.169.132:53    172.16.169.132:53
            # tcp 172.16.94.209:11012 192.168.1.89:11012 172.16.196.220:23    172.16.196.220:23
            # tcp 172.16.94.209:1067  192.168.1.95:1067  172.16.196.161:23    172.16.196.161:23
            # any ---                ---                10.1.0.2          10.144.0.2
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                if 'vrf' in ret_dict:
                    if vrf_flag:
                        protocol_dict = index_dict.setdefault(index, {})
                        protocol_dict.update(group)

                    elif vrf_flag == False and index >= 2:
                        default_dict = vrf_dict.setdefault('default', {})
                        index_dict = default_dict.setdefault('index', {})
                        protocol_dict = index_dict.setdefault(index, {})
                        protocol_dict.update(group)

                        if tmp_dict:
                            default_dict = vrf_dict.setdefault('default', {})
                            index_dict = default_dict.setdefault('index', {})
                            protocol_dict = index_dict.setdefault(index, {})
                            vrf_dict['default']['index'].update(tmp_dict)
                            tmp_dict.clear()

                else:
                    vrf_dict = ret_dict.setdefault('vrf', {})

                    itemp_dict = tmp_dict.setdefault(index, {})

                    itemp_dict.update(group)
                    vrf_dict.setdefault('default', {}).setdefault('index', {}).update(tmp_dict)
                    protocol_dict = index_dict.setdefault(index, {})

                index += 1

                continue

            # create: 02/15/12 11:38:01, use: 02/15/12 11:39:02, timeout: 00:00:00
            # create 04/09/11 10:51:48, use 04/09/11 10:52:31, timeout: 00:01:00
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                if protocol_dict:
                    details_dict = protocol_dict.setdefault('details', {})
                    details_dict.update(group)

                else:
                    tmp_details_dict = tmp_dict[1].setdefault('details', {})
                    tmp_details_dict.update(group)

                continue

            # IOS-XE:
            # Map-Id(In): 1
            # IOS:
            # Map-Id(In):1, Mac-Address: 0000.0000.0000 Input-IDB: GigabitEthernet0/3/1
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()

                if protocol_dict:
                    details_dict.update({'map_id_in': int(group['map_id_in'])})

                    if group['mac_address']:
                        details_dict.update({'mac_address': group['mac_address']})

                    if group['input_idb']:
                        details_dict.update({'input_idb': group['input_idb']})

                else:
                    tmp_details_dict.update(
                        {'mac_address': group['mac_address']})
                    tmp_details_dict.update({'input_idb': group['input_idb']})
                    tmp_details_dict.update(
                        {'map_id_in': int(group['map_id_in'])})

                continue

            # IOS-XE:
            # Mac-Address: 0000.0000.0000    Input-IDB: TenGigabitEthernet1/1/0
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()

                if protocol_dict:
                    details_dict.update(group)
                else:
                    tmp_details_dict.update(group)

                continue

            # entry-id: 0x0, use_count:1
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                if protocol_dict:
                    details_dict.update({'entry_id': group['entry_id']})
                    details_dict.update({'use_count': int(group['use_count'])})

                else:
                    tmp_details_dict.update({'entry_id': group['entry_id']})
                    tmp_details_dict.update(
                        {'use_count': int(group['use_count'])})

                if tmp_dict:
                    default_dict = vrf_dict.setdefault('default', {})
                    index_dict = default_dict.setdefault('index', {})
                    protocol_dict = index_dict.setdefault(index, {})
                    vrf_dict['default']['index'].update(tmp_dict)
                    tmp_dict.clear()

                continue

            # Total number of translations: 3
            m6 = p6.match(line)
            if m6:

                anumber = int(m6.groupdict()['number_of_translations'])
                total_dict = ret_dict.setdefault('vrf', {})
                total_dict.update({'number_of_translations': anumber})

                continue

            # Group_id:0   vrf: genie
            m7 = p7.match(line)
            if m7:
                group = m7.groupdict()
                vrf_name = group['vrf_name']
                if tmp_dict:
                    vrf_name_dict = vrf_dict.setdefault(group['vrf_name'], {})
                    index_dict = vrf_name_dict.setdefault('index', {})
                    tmp_dict[1].update({'group_id': int(group['group_id'])})
                    del vrf_dict['default']
                    vrf_flag = True

                else:
                    protocol_dict.update({'group_id': int(group['group_id'])})

                continue

            # Format(H:M:S) Time-left :0:0:-1
            m8 = p8.match(line)
            if m8:
                time_left = m8.groupdict()['time_left']
                if tmp_dict:
                    m8_dict = vrf_name_dict.setdefault('index', {})
                    tmp_dict[1].update({'time_left': time_left})
                    vrf_dict[vrf_name]['index'].update(tmp_dict)
                    tmp_dict.clear()
                else:
                    protocol_dict.update({'time_left': time_left})

                continue

        return ret_dict


class ShowIpNatStatisticsSchema(MetaParser):
    """ Schema for command:
            * show ip nat statistics
    """

    schema = {
        'active_translations': {
            'total': int,
            'static': int,
            'dynamic': int,
            'extended': int,
        },
        'interfaces': {
            Optional('outside'): list,
            Optional('inside'): list,
        },
        'hits': int,
        'misses': int,
        Optional('dynamic_mappings'): {
            Any(): {  # 'Inside source'
                'id': {
                    Any(): {  # 0, 1, 2 or 1, 2, 3
                        Optional('match'): str,  # 'access-list 1 pool poo1'
                        Optional('access_list'): str,
                        Optional('route_map'): str,
                        Optional('refcount'): int,
                        Optional('interface'): str,
                        Optional('pool'): {
                            Any(): {  # mypool test-pool
                                'netmask': str,
                                'start': str,
                                'end': str,
                                'type': str,
                                'total_addresses': int,
                                'allocated': int,
                                'allocated_percentage': int,
                                'misses': int,
                                Optional('addr_hash'): int,
                                Optional('average_len'): int,
                                Optional('chains'): str,
                                Optional('id'): int,
                            }
                        }
                    }
                }
            }
        },
        Optional('nat_limit_statistics'): {
            'max_entry': {
                'max_allowed': int,
                'used': int,
                'missed': int,
            }
        },
        Optional('cef_translated_pkts'): int,
        Optional('in_to_out_drops'): int,
        Optional('out_to_in_drops'): int,
        Optional('cef_punted_pkts'): int,
        Optional('expired_translations'): int,
        Optional('pool_stats_drop'): int,
        Optional('mapping_stats_drop'): int,
        Optional('port_block_alloc_fail'): int,
        Optional('ip_alias_add_fail'): int,
        Optional('limit_entry_add_fail'): int,
        Optional('queued_pkts'): int,
        Optional('peak_translations'): int,
        Optional('occurred'): str,
        Optional('total_doors'): int,
        Optional('appl_doors'): int,
        Optional('normal_doors'): int,
    }


class ShowIpNatStatistics(ShowIpNatStatisticsSchema):
    """
        * show ip nat statistics
    """
    # Mapping for integers variables
    INT_MAPPING = {
        'Hits': 'hits',
        'Misses': 'misses',
        'CEF Translated packets': 'cef_translated_pkts',
        'Expired translations': 'expired_translations',
        'Pool stats drop': 'pool_stats_drop',
        'Port block alloc fail': 'port_block_alloc_fail',
        'IP alias add fail': 'ip_alias_add_fail',
        'Limit entry add fail': 'limit_entry_add_fail',
        'Queued Packets': 'queued_pkts',
        'Peak translations': 'peak_translations',
        'CEF Punted packets': 'cef_punted_pkts',
        'Mapping stats drop': 'mapping_stats_drop',
        'In-to-out drops': 'in_to_out_drops',
        'Out-to-in drops': 'out_to_in_drops',
        'Total doors': 'total_doors',
        'Appl doors': 'appl_doors',
        'Normal doors': 'normal_doors',
    }

    # Mapping for string variables
    STR_MAPPING = {
        'occurred': 'occurred',
    }

    cli_command = ['show ip nat statistics']

    def cli(self, output=None):

        out = output or self.device.execute(self.cli_command)

        # Total active translations: 0 (0 static, 0 dynamic 0 extended)
        # IOS
        # Total translations: 2 (0 static, 2 dynamic; 0 extended)
        p1 = re.compile(r'^Total(?: +active)? +translations: '
                        r'+(?P<total_translations>\d+) +\((?P<static>\d+) '
                        r'+static\, +(?P<dynamic>\d+) +dynamic\; '
                        r'+(?P<extended>\d+) +extended\)$')

        # Outside interfaces:
        # Inside interfaces:
        # IOS
        # Outside interfaces: Serial0
        # Inside interfaces: Ethernet1
        p2 = re.compile(r'^(?P<in_out_interfaces>Outside|Inside) '
                        r'+interfaces\:(?: +(?P<direction_interfaces>\S+))?$')

        # TenGigabitEthernet1/0/0, TenGigabitEthernet1/1/0, TenGigabitEthernet1/2/0, TenGigabitEthernet1/3/0
        # FastEthernet0/0
        p3 = re.compile(r'^(?P<direction_interfaces>[\w\d\/\d\/\d\,\s]+)$')

        # Hits: 59230465  Misses: 3
        # CEF Translated packets: 0, CEF Punted packets: 0
        # Expired translations: 0
        # Pool stats drop: 0  Mapping stats drop: 0
        # Port block alloc fail: 0
        # IP alias add fail: 0
        # Limit entry add fail: 0
        # Queued Packets: 0
        # Peak translations: 8114, occurred 18:35:17 ago
        # In-to-out drops: 0  Out-to-in drops: 0
        p4 = re.compile(r'^(?P<name_1>[\w|\s|\-]+)\: +(?P<number_1>\w+)'
                        r'(?:[\,|\s*]+(?P<name_2>[\w|\s|\-]+)(?:\:|\s*)? '
                        r'+(?P<number_2>\S+)(?: +ago)?)?$')
        
        # Dynamic mappings:
        p5 = re.compile(r'^(?P<dynamic>\w+) +mappings\:$')

        # -- Inside Source
        p6 = re.compile(r'^\-\- +(?P<source>\S+) +Source$')

        # [Id: 1] access-list 102 pool mypool refcount 3
        # access-list 1 pool net-208 refcount 2
        # [Id: 1] access-list 25 interface FastEthernet1/0 refcount 0
        # [Id: 3] access-list 99 interface Serial0/0 refcount 1
        # [Id: 1] access-list test-robot pool test-robot refcount 0
        # [Id: 3] access-list 99 interface Serial0/0 refcount 1
        # [Id: 1] route-map NAT-MAP pool inside-pool refcount 6
        # [Id: 0] route-map STATIC-MAP
        p7 = re.compile(r'^(?:\[Id\: +(?P<id>\d+)\] )?(?P<access_method>'
                        r'access\-+list|route\-map) +(?P<access_list>[\w\-]+)'
                        r'(?: +(?P<method>pool|interface) +(?P<pool>[\w\/-]+) '
                        r'+refcount +(?P<refcount>\d+))?$')

        # pool mypool: netmask 255.255.255.0
        # pool inside-pool: id 1, netmask 255.255.255.0
        p8 = re.compile(r'^pool +(?P<pool>\S+)\:(?: +(id +(?P<id>\d+))\,)?'
                        r'(?:( +netmask +(?P<netmask>[\d+\.]+))?)$')

        # start 10.5.5.1 end 10.5.5.5
        p9 = re.compile(r'^start +(?P<start>[\d\.]+) +end +(?P<end>[\d\.]+)$')

        # type generic, total addresses 5, allocated 1 (20%), misses 0
        # type generic, total addresses 1, allocated 0 (0%), misses 0
        p10 = re.compile(r'^type +(?P<type>\w+)\, +total +addresses '
                          r'+(?P<total_addresses>\d+)\, +allocated '
                          r'+(?P<allocated>\d+) +\((?P<allocated_percentage>\d+)'
                          r'+\%\)\, +misses +(?P<misses>\d+)$')

        # max entry: max allowed 2147483647, used 3, missed 0
        p11 = re.compile(r'^max +entry\: +max +allowed +(?P<max_allowed>\d+)\, '
                        r'+used +(?P<used>\d+)\, +missed +(?P<missed>\d+)$')

        # longest chain in pool: pool1's addr-hash: 0, average len 0,chains 0/256
        # longest chain in pool: test-pool1's addr-hash: 0, average len 0,chains 0/256
        p12 = re.compile(r'^longest +chain +in +pool\: +(?P<pool_name>\S+)\'s '
                        r'+addr\-hash\: +(?P<addr_hash>\d+)\, +average +len '
                        r'(?P<average_len>\d+)\,+chains +(?P<chains>\S+)$')

        parsed_dict = {}
        index = 1
        on_the_outside = False
        on_the_inside = False

        for line in out.splitlines():
            line = line.strip()

            # Total active translations: 0 (0 static, 0 dynamic 0 extended)
            # IOS
            # Total translations: 2 (0 static, 2 dynamic; 0 extended)
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                active_dict = parsed_dict.setdefault('active_translations', {})
                active_dict['total'] = int(group['total_translations'])
                active_dict['static'] = int(group['static'])
                active_dict['dynamic'] = int(group['dynamic'])
                active_dict['extended'] = int(group['extended'])

                continue

            # Outside interfaces:
            # Inside interfaces:
            # IOS
            # Outside interfaces: Serial0
            # Inside interfaces: Ethernet1
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                intf_dict = parsed_dict.setdefault('interfaces', {})
                if group['in_out_interfaces'] == 'Outside':
                    on_the_outside = True
                    on_the_inside = False

                    if group['direction_interfaces']:
                        outside_list = group['direction_interfaces'].split()
                        olist = []
                        for item in outside_list:
                            olist.append(item)

                        if 'outside' in intf_dict:
                            intf_dict['outside'] += olist
                        else:
                            intf_dict['outside'] = olist
                else:
                    on_the_inside = True
                    on_the_outside = False

                    if group['direction_interfaces']:
                        inside_list = group['direction_interfaces'].split()
                        ilist = []
                        for item in inside_list:
                            ilist.append(item)

                        if 'inside' in intf_dict:
                            intf_dict['inside'] += ilist
                        else:
                            intf_dict['inside'] = ilist
                continue

            # TenGigabitEthernet1/0/0, TenGigabitEthernet1/1/0, TenGigabitEthernet1/2/0, TenGigabitEthernet1/3/0
            # FastEthernet0/0
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()

                if on_the_outside:
                    outside_list = group['direction_interfaces'].split()
                    olist = []
                    for item in outside_list:
                        olist.append(item)

                    if 'outside' in intf_dict:
                        intf_dict['outside'] += olist
                    else:
                        intf_dict['outside'] = olist

                elif on_the_inside:
                    inside_list = group['direction_interfaces'].split()
                    ilist = []
                    for item in inside_list:
                        ilist.append(item)

                    if 'inside' in intf_dict:
                        intf_dict['inside'] += ilist
                    else:
                        intf_dict['inside'] = ilist

                continue

            # Hits: 59230465  Misses: 3
            # CEF Translated packets: 0, CEF Punted packets: 0
            # Expired translations: 0
            # Pool stats drop: 0  Mapping stats drop: 0
            # Port block alloc fail: 0
            # IP alias add fail: 0
            # Limit entry add fail: 0
            # Queued Packets: 0
            # Peak translations: 8114, occurred 18:35:17 ago
            # In-to-out drops: 0  Out-to-in drops: 0
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                
                if group['name_1']:
                    if self.INT_MAPPING.get(group['name_1']):
                        name_1 = self.INT_MAPPING.get(group['name_1'])
                        if name_1:
                            parsed_dict[name_1] = int(group['number_1'])
                    else:
                        name_1 = self.STR_MAPPING.get(group['name_1'])
                        if name_1:
                            parsed_dict[name_1] = int(group['number_1'])

                if group['name_2']:
                    if self.INT_MAPPING.get(group['name_2']):
                        name_2 = self.INT_MAPPING.get(group['name_2'])
                        if name_2:
                            parsed_dict[name_2] = int(group['number_2'])
                    else:
                        name_2 = self.STR_MAPPING.get(group['name_2'])
                        if name_2:
                            parsed_dict[name_2] = group['number_2']
                continue

            # Dynamic mappings:
            m5 = p5.match(line)
            if m5:
                dynamic_dict = parsed_dict.setdefault('dynamic_mappings', {})
                continue

            # -- Inside Source
            m6 = p6.match(line)
            if m6:
                source = m6.groupdict()['source'].lower() + '_source'
                source_dict = dynamic_dict.setdefault(source, {})
                continue

            # [Id: 1] access-list 102 pool mypool refcount 3
            # access-list 1 pool net-208 refcount 2
            # [Id: 1] access-list 25 interface FastEthernet1/0 refcount 0
            # [Id: 3] access-list 99 interface Serial0/0 refcount 1
            # [Id: 1] access-list test-robot pool test-robot refcount 0
            # [Id: 3] access-list 99 interface Serial0/0 refcount 1
            # [Id: 1] route-map NAT-MAP pool inside-pool refcount 6
            # [Id: 0] route-map STATIC-MAP
            m7 = p7.match(line)
            if m7:
                group = m7.groupdict()

                access_name1 = group['access_method'] + ' ' + group['access_list']

                if group['method'] and group['pool']:
                    access_name2 = group['method'] + ' ' + group['pool']
                    access_name = access_name1 + ' ' + access_name2
                else:
                    access_name = access_name1

                if group['id']:
                    id_dict = source_dict.setdefault('id', {})
                    name_dict = id_dict.setdefault(int(group['id']), {})
                else:
                    id_dict = source_dict.setdefault('id', {})
                    name_dict = id_dict.setdefault(index, {})
                    index += 1

                name_dict.update({'match': access_name})
                if 'access-list' == group['access_method']:
                    name_dict.update({'access_list': group['access_list']})

                elif 'route-map' == group['access_method']:
                    name_dict.update({'route_map': group['access_list']})

                if group['method'] == 'interface':
                    name_dict.update({'interface': group['pool']})

                elif group['method'] == 'pool':
                    pool_dict = name_dict.setdefault('pool', {})

                if group['refcount']:
                    name_dict.update({'refcount': int(group['refcount'])})

                continue

            # pool mypool: netmask 255.255.255.0
            # pool inside-pool: id 1, netmask 255.255.255.0
            m8 = p8.match(line)
            if m8:
                group = m8.groupdict()
                mypool_dict = pool_dict.setdefault(group['pool'], {})
                mypool_dict.update({'netmask': group['netmask']})

                if group['id']:
                    mypool_dict.update({'id': int(group['id'])})

                continue
            # start 10.5.5.1 end 10.5.5.5
            m9 = p9.match(line)

            if m9:
                group = m9.groupdict()

                mypool_dict.update({'start': group['start']})
                mypool_dict.update({'end': group['end']})

                continue

            # type generic, total addresses 5, allocated 1 (20 %), misses 0
            # type generic, total addresses 1, allocated 0 (0 % ), misses 0
            m10 = p10.match(line)

            if m10:
                group = m10.groupdict()
                mypool_dict.update({'type': group['type']})
                mypool_dict.update(
                    {'total_addresses': int(group['total_addresses'])})
                mypool_dict.update({'allocated': int(group['allocated'])})
                mypool_dict.update(
                    {'allocated_percentage': int(group['allocated_percentage'])})
                mypool_dict.update({'misses': int(group['misses'])})

                continue

            # max entry: max allowed 2147483647, used 3, missed 0
            m11 = p11.match(line)
            if m11:
                group = m11.groupdict()
                max_dict = parsed_dict.setdefault('nat_limit_statistics', {})
                nat_limit_dict = max_dict.setdefault('max_entry', {})
                nat_limit_dict.update({'max_allowed': int(group['max_allowed'])})
                nat_limit_dict.update({'used': int(group['used'])})
                nat_limit_dict.update({'missed': int(group['missed'])})

                continue

            # longest chain in pool: pool1's addr-hash: 0, average len 0,chains 0/256
            # longest chain in pool: test-pool1's addr-hash: 0, average len 0,chains 0/256
            m12 = p12.match(line)
            if m12:
                group = m12.groupdict()

                mypool_dict.update({'addr_hash': int(group['addr_hash'])})
                mypool_dict.update({'average_len': int(group['average_len'])})
                mypool_dict.update({'chains': group['chains']})
                
                continue

        return parsed_dict


# =======================================
# Schema for 'show ip dhcp database'
# =======================================
class ShowIpDhcpDatabaseSchema(MetaParser):
    """
    Schema for show ip dhcp database
    """

    schema = {
        'url': {
            str: {
                'read': str,
                'written': str,
                'status': str,
                'delay_in_secs': int,
                'timeout_in_secs': int,
                'failures': int,
                'successes': int
            }
        }
    }

# =======================================
# Parser for 'show ip dhcp database'
# =======================================
class ShowIpDhcpDatabase(ShowIpDhcpDatabaseSchema):
    """
    Parser for show ip dhcp database
    """
    cli_command = 'show ip dhcp database'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # URL       :    ftp://user:password@172.16.4.253/router-dhcp
        p1 = re.compile(r'^URL +: +(?P<url>(\S+))$')
        # Read      :    Dec 01 1997 12:01 AM
        p2 = re.compile(r'^Read +: +(?P<read>(.+))$')
        # Written   :    Never
        p3 = re.compile(r'^Written +: +(?P<written>(\S+))$')
        # Status    :    Last read succeeded. Bindings have been loaded in RAM.
        p4 = re.compile(r'^Status +: +(?P<status>(.+))$')
        # Delay     :    300 seconds
        p5 = re.compile(r'^Delay +: +(?P<delay>(\d+))')
        # Timeout   :    300 seconds
        p6 = re.compile(r'^Timeout +: +(?P<timeout>(\d+))')
        # Failures  :    0
        p7 = re.compile(r'^Failures +: +(?P<failures>(\d+))$')
        # Successes :    1
        p8 = re.compile(r'^Successes +: +(?P<successes>(\d+))$')

        ret_dict = {}
        for line in out.splitlines():
            line.strip()

            # URL       :    ftp://user:password@172.16.4.253/router-dhcp
            m = p1.match(line)
            if m:
                url_dict = ret_dict.setdefault('url', {}).setdefault(m.groupdict()['url'], {})
                # ret_dict.update({'url': m.groupdict()['url']})
                continue

            # Read      :    Dec 01 1997 12:01 AM
            m = p2.match(line)
            if m:
                url_dict.update({'read': m.groupdict()['read']})
                continue

            # Written   :    Never
            m = p3.match(line)
            if m:
                url_dict.update({'written': m.groupdict()['written']})
                continue

            # Status    :    Last read succeeded. Bindings have been loaded in RAM.
            m = p4.match(line)
            if m:
                url_dict.update({'status': m.groupdict()['status']})
                continue

            # Delay     :    300 seconds
            m = p5.match(line)
            if m:
                url_dict.update({'delay_in_secs': int(m.groupdict()['delay'])})
                continue

            # Timeout   :    300 seconds
            m = p6.match(line)
            if m:
                url_dict.update({'timeout_in_secs': int(m.groupdict()['timeout'])})
                continue

            # Failures  :    0
            m = p7.match(line)
            if m:
                url_dict.update({'failures': int(m.groupdict()['failures'])})
                continue

            # Successes :    1
            m = p8.match(line)
            if m:
                url_dict.update({'successes': int(m.groupdict()['successes'])})
                continue

        return ret_dict


# ===================================================
# Schema for 'show ip dhcp snooping database'
#            'show ip dhcp snooping database detail'
# ===================================================
class ShowIpDhcpSnoopingDatabaseSchema(MetaParser):
    """
    Schema for show ip dhcp snooping database
               show ip dhcp snooping database detail
    """

    schema = {
        'agent_url': str,
        'write_delay_secs': int,
        'abort_timer_secs': int,
        'agent_running': str,
        'delay_timer_expiry': str,
        'abort_timer_expiry': str,
        'last_succeeded_time': str,
        'last_failed_time': str,
        'last_failed_reason': str,
        'total_attempts': int,
        'startup_failures': int,
        'successful_transfers': int,
        'failed_transfers': int,
        'successful_reads': int,
        'failed_reads': int,
        'successful_writes': int,
        'failed_writes': int,
        'media_failures': int,
        Optional('detail'): {
            'first_successful_access': str,
            'last_ignored_bindings_counters': {
                'binding_collisions': int,
                'expired_leases': int,
                'invalid_interfaces': int,
                'unsupported_vlans': int,
                'parse_failures': int
            },
            'last_ignored_time': str,
            'total_ignored_bindings_counters': {
                'binding_collisions': int,
                'expired_leases': int,
                'invalid_interfaces': int,
                'unsupported_vlans': int,
                'parse_failures': int
            }
        }
    }

# ===================================================
# Parser for 'show ip dhcp snooping database'
# ===================================================
class ShowIpDhcpSnoopingDatabase(ShowIpDhcpSnoopingDatabaseSchema):
    """
    Parser for show ip dhcp snooping database
    """
    cli_command = 'show ip dhcp snooping database'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Initializes the Python dictionary variable
        ret_dict = {}

        # Agent URL :
        p1 = re.compile(r'^Agent URL +: +(?P<agent_url>\S*)$')

        # Write delay Timer : 300 seconds
        p2 = re.compile(r'^Write delay Timer +: +(?P<write_delay_secs>\d+) seconds$')

        # Abort Timer : 300 seconds
        p3 = re.compile(r'^Abort Timer +: +(?P<abort_timer_secs>\d+) seconds$')

        # Agent Running : No
        p4 = re.compile(r'^Agent Running +: +(?P<agent_running>\w+)$')

        # Delay Timer Expiry : Not Running
        p5 = re.compile(r'^Delay Timer Expiry +: +(?P<delay_timer_expiry>.+)$')

        # Abort Timer Expiry : Not Running
        p6 = re.compile(r'^Abort Timer Expiry +: +(?P<abort_timer_expiry>.+)$')

        # Last Succeded Time : None
        p7 = re.compile(r'^Last Succee?ded Time +: +(?P<last_succeeded_time>.+)$')

        # Last Failed Time : None
        p8 = re.compile(r'^Last Failed Time +: +(?P<last_failed_time>.+)$')

        # Last Failed Reason : No failure recorded.
        p9 = re.compile(r'^Last Failed Reason +: +(?P<last_failed_reason>[\w ]+)\.?$')

        # Total Attempts       :        0   Startup Failures :        0
        p10 = re.compile(r'^Total Attempts +: +(?P<total_attempts>\d+) +Startup Failures +: +(?P<startup_failures>\d+)$')

        # Successful Transfers :        0   Failed Transfers :        0
        p11 = re.compile(r'^Successful Transfers +: +(?P<successful_transfers>\d+) +Failed Transfers +: +(?P<failed_transfers>\d+)$')

        # Successful Reads     :        0   Failed Reads     :        0
        p12 = re.compile(r'^Successful Reads +: +(?P<successful_reads>\d+) +Failed Reads +: +(?P<failed_reads>\d+)$')

        # Successful Writes    :        0   Failed Writes    :        0
        p13 = re.compile(r'^Successful Writes +: +(?P<successful_writes>\d+) +Failed Writes +: +(?P<failed_writes>\d+)$')

        # Media Failures       :        0
        p14 = re.compile(r'^Media Failures +: +(?P<media_failures>\d+)$')

        # First successful access: Read
        p15 = re.compile(r'^First successful access *: +(?P<first_successful_access>\w+)$')

        # Last ignored bindings counters :
        p16 = re.compile(r'^Last ignored bindings counters *:$')

        # Binding Collisions    :        0   Expired leases    :        0
        p17 = re.compile(r'^Binding Collisions +: +(?P<binding_collisions>\d+) +Expired leases +: +(?P<expired_leases>\d+)$')

        # Invalid interfaces    :        0   Unsupported vlans :        0
        p18 = re.compile(r'^Invalid interfaces +: +(?P<invalid_interfaces>\d+) +Unsupported vlans : +(?P<unsupported_vlans>\d+)$')

        # Parse failures        :        0
        p19 = re.compile(r'^Parse failures +: +(?P<parse_failures>\d+)$')

        # Last Ignored Time : None
        p20 = re.compile(r'^Last Ignored Time +: +(?P<last_ignored_time>.+)$')

        # Total ignored bindings counters :
        p21 = re.compile(r'^Total ignored bindings counters *:$')

        # Processes the matched patterns
        for line in out.splitlines():
            line.strip()

            # Agent URL :
            m = p1.match(line)
            if m:
                ret_dict['agent_url'] = m.groupdict()['agent_url']
                continue

            # Write delay Timer : 300 seconds
            m = p2.match(line)
            if m:
                ret_dict['write_delay_secs'] = int(m.groupdict()['write_delay_secs'])
                continue

            # Abort Timer : 300 seconds
            m = p3.match(line)
            if m:
                ret_dict['abort_timer_secs'] = int(m.groupdict()['abort_timer_secs'])
                continue

            # Agent Running : No
            m = p4.match(line)
            if m:
                ret_dict['agent_running'] = m.groupdict()['agent_running']
                continue

            # Delay Timer Expiry : Not Running
            m = p5.match(line)
            if m:
                ret_dict['delay_timer_expiry'] = m.groupdict()['delay_timer_expiry']
                continue

            # Abort Timer Expiry : Not Running
            m = p6.match(line)
            if m:
                ret_dict['abort_timer_expiry'] = m.groupdict()['abort_timer_expiry']
                continue

            # Last Succeded Time : None
            m = p7.match(line)
            if m:
                ret_dict['last_succeeded_time'] = m.groupdict()['last_succeeded_time']
                continue

            # Last Failed Time : None
            m = p8.match(line)
            if m:
                ret_dict['last_failed_time'] = m.groupdict()['last_failed_time']
                continue

            # Last Failed Reason : No failure recorded.
            m = p9.match(line)
            if m:
                ret_dict['last_failed_reason'] = m.groupdict()['last_failed_reason']
                continue

            # Total Attempts       :        0   Startup Failures :        0
            m = p10.match(line)
            if m:
                ret_dict['total_attempts'] = int(m.groupdict()['total_attempts'])
                ret_dict['startup_failures'] = int(m.groupdict()['startup_failures'])
                continue

            # Successful Transfers :        0   Failed Transfers :        0
            m = p11.match(line)
            if m:
                ret_dict['successful_transfers'] = int(m.groupdict()['successful_transfers'])
                ret_dict['failed_transfers'] = int(m.groupdict()['failed_transfers'])
                continue

            # Successful Reads     :        0   Failed Reads     :        0
            m = p12.match(line)
            if m:
                ret_dict['successful_reads'] = int(m.groupdict()['successful_reads'])
                ret_dict['failed_reads'] = int(m.groupdict()['failed_reads'])
                continue

            # Successful Writes    :        0   Failed Writes    :        0
            m = p13.match(line)
            if m:
                ret_dict['successful_writes'] = int(m.groupdict()['successful_writes'])
                ret_dict['failed_writes'] = int(m.groupdict()['failed_writes'])
                continue

            # Media Failures       :        0
            m = p14.match(line)
            if m:
                ret_dict['media_failures'] = int(m.groupdict()['media_failures'])
                continue

            # First successful access: Read
            m = p15.match(line)
            if m:
                detail_dict = ret_dict.setdefault('detail', {})
                detail_dict['first_successful_access'] = m.groupdict()['first_successful_access']
                continue

            # Last ignored bindings counters :
            m = p16.match(line)
            if m:
                bindings_dict = detail_dict.setdefault('last_ignored_bindings_counters', {})
                continue

            # Binding Collisions    :        0   Expired leases    :        0
            m = p17.match(line)
            if m:
                bindings_dict['binding_collisions'] = int(m.groupdict()['binding_collisions'])
                bindings_dict['expired_leases'] = int(m.groupdict()['expired_leases'])
                continue

            # Invalid interfaces    :        0   Unsupported vlans :        0
            m = p18.match(line)
            if m:
                bindings_dict['invalid_interfaces'] = int(m.groupdict()['invalid_interfaces'])
                bindings_dict['unsupported_vlans'] = int(m.groupdict()['unsupported_vlans'])
                continue

            # Parse failures        :        0
            m = p19.match(line)
            if m:
                bindings_dict['parse_failures'] = int(m.groupdict()['parse_failures'])
                continue

            # Last Ignored Time : None
            m = p20.match(line)
            if m:
                detail_dict['last_ignored_time'] = m.groupdict()['last_ignored_time']
                continue

            # Total ignored bindings counters :
            m = p21.match(line)
            if m:
                bindings_dict = detail_dict.setdefault('total_ignored_bindings_counters', {})
                continue

        return ret_dict


# ===================================================
# Parser for 'show ip dhcp snooping database detail'
# ===================================================
class ShowIpDhcpSnoopingDatabaseDetail(ShowIpDhcpSnoopingDatabase):
    """
    Parser for show ip dhcp snooping database detail
    """
    cli_command = 'show ip dhcp snooping database detail'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        return super().cli(output=output)


# ===================================================
# Schema for 
#    * 'show ip dhcp snooping binding'
#    * 'show ip dhcp snooping binding interface {interface}'
#    * 'show ip dhcp snooping binding {mac}'
# ===================================================
class ShowIpDhcpSnoopingBindingSchema(MetaParser):
    ''' Schema for:
        * 'show ip dhcp snooping binding'
        * 'show ip dhcp snooping binding interface {interface}'
        * 'show ip dhcp snooping binding {mac}'
    '''

    schema = {
        'total_bindings': int,
        'interfaces': {
            Any(): {
                'vlan': {
                    Any(): {
                        'mac': str,
                        'ip': str,
                        'lease': int,
                        'type': str,
                    },
                },
            },
        },
    }


# ===========================
# Parser for:
#   * 'show show ip dhcp snooping binding'
#   * 'show ip dhcp snooping binding interface {interface}'
#   * 'show ip dhcp snooping binding {mac}'
# ===========================
class ShowIpDhcpSnoopingBinding(ShowIpDhcpSnoopingBindingSchema):
    ''' Parser for:
        * 'show ip dhcp snooping binding'
        * 'show ip dhcp snooping binding interface {interface}'
        * 'show ip dhcp snooping binding {mac}'
     '''

    cli_command = ['show ip dhcp snooping binding', 
                'show ip dhcp snooping binding interface {interface}',
                'show ip dhcp snooping binding {mac}']

    def cli(self, interface=None, mac=None, output=None):
        if output is None:
            if mac:
                cmd = self.cli_command[2].format(mac=mac)
            elif interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            
            output = self.device.execute(cmd)

        # Init vars
        ret_dict = {}

        # MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
        # ------------------  ---------------  ----------  -------------  ----  --------------------
        # 00:11:01:00:00:01   100.100.0.5      1124        dhcp-snooping   100   FiftyGigE6/0/25

        p1 = re.compile(r'^(?P<mac>\S+) +(?P<ip>\S+) +(?P<lease>\d+) +(?P<type>\S+) +(?P<vlan>\d+) +(?P<interface>\S+)$')

        # Total number of bindings: 1
        p2 = re.compile(r'^Total number of bindings: (?P<total_bindings>\d+)$')

        for line in output.splitlines():

            line = line.strip()
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vlan = group['vlan']
                interface = group['interface']

                # Build Dict

                intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(interface, {})
                vlan_dict = intf_dict.setdefault('vlan', {}).setdefault(vlan, {})

                # Set values
                vlan_dict.update({
                    'mac': group['mac'],
                    'ip': group['ip'],
                    'lease': int(group['lease']),
                    'type': group['type']
                })
                continue
            
            # Total number of bindings: 1
            m = p2.match(line)
            if m:
                ret_dict['total_bindings'] = int(m.groupdict()['total_bindings'])
                continue

        return ret_dict

# =====================================
# Schema for  show ip mfib
# Schema for  show ip mfib {group}
# Schema for  show ip mfib {group} {source}
# Schema for  show ip mfib verbose
# Schema for  show ip mfib {group} verbose
# Schema for  show ip mfib {group} {source} verbose
# Schema for  show ip mfib vrf {vrf}
# Schema for  show ip mfib vrf {vrf} {group}
# Schema for  show ip mfib vrf {vrf} {group} {source}
# Schema for  show ip mfib vrf {vrf} verbose
# Schema for  show ip mfib vrf {vrf} {group} verbose
# Schema for  show ip mfib vrf {vrf} {group} {source} verbose

# =====================================
class ShowIpMfibSchema(MetaParser):
    """Schema for:
      show ip mfib
      show ip mfib {group}
      show ip mfib {group} {source}
      show ip mfib verbose
      show ip mfib {group} verbose
      show ip mfib {group} {source} verbose
      show ip mfib vrf {vrf}
      show ip mfib vrf {vrf} {group}
      show ip mfib vrf {vrf} {group} {source}
      show ip mfib vrf {vrf} verbose
      show ip mfib vrf {vrf} {group} verbose
      show ip mfib vrf {vrf} {group} {source} verbose"""

    schema = {
        'vrf':
            {Any():
                {'address_family':
                    {Any():
                        {Optional('multicast_group'):
                            {Any():
                                {Optional('source_address'):
                                    {Any():
                                       {
                                            Optional('oif_ic_count'): Or(str,int),
                                            Optional('oif_a_count'): Or(str,int),
                                            Optional('flags'): str,
                                            Optional('sw_packet_count'): Or(str,int),
                                            Optional('sw_packets_per_second'): Or(str,int),
                                            Optional('sw_average_packet_size'): Or(str,int),
                                            Optional('sw_kbits_per_second'): Or(str,int),
                                            Optional('sw_total'): Or(str,int),
                                            Optional('sw_rpf_failed'): Or(str,int),
                                            Optional('sw_other_drops'): Or(str,int),
                                            Optional('hw_packet_count'): Or(str,int),
                                            Optional('hw_packets_per_second'): Or(str,int),
                                            Optional('hw_average_packet_size'): Or(str,int),
                                            Optional('hw_kbits_per_second'): Or(str,int),
                                            Optional('hw_total'): Or(str,int),
                                            Optional('hw_rpf_failed'): Or(str,int),
                                            Optional('hw_other_drops'): Or(str,int),
                                            Optional('incoming_interfaces'):
                                                {Any():
                                                    {
                                                     Optional('ingress_flags'): str,
                                                     Optional('ingress_vxlan_version'): str,
                                                     Optional('ingress_vxlan_cap'): str,
                                                     Optional('ingress_vxlan_vni'): str,
                                                     Optional('ingress_vxlan_nxthop'): str,
                                                    }
                                                },
                                            Optional('outgoing_interfaces'):
                                                {Any():
                                                    {
                                                     Optional('egress_flags'): str,
                                                     Optional('egress_rloc'): str,
                                                     Optional('egress_underlay_mcast'): str,
                                                     Optional('egress_adj_mac'): str,
                                                     Optional('egress_hw_pkt_count'): Or(str,int),
                                                     Optional('egress_fs_pkt_count'): Or(str,int),
                                                     Optional('egress_ps_pkt_count'): Or(str,int),
                                                     Optional('egress_pkt_rate'): Or(str,int),
                                                     Optional('egress_vxlan_version'): str,
                                                     Optional('egress_vxlan_cap'): str,
                                                     Optional('egress_vxlan_vni'): str,
                                                     Optional('egress_vxlan_nxthop'): str,
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    }
                },
            }

# =====================================
# Parser for  show ip mfib
# Parser for  show ip mfib {group}
# Parser for  show ip mfib {group} {source}
# Parser for  show ip mfib verbose
# Parser for  show ip mfib {group} verbose
# Parser for  show ip mfib {group} {source} verbose
# Parser for  show ip mfib vrf {vrf}
# Parser for  show ip mfib vrf {vrf} {group}
# Parser for  show ip mfib vrf {vrf} {group} {source}
# Parser for  show ip mfib vrf {vrf} verbose
# Parser for  show ip mfib vrf {vrf} {group} verbose
# Parser for  show ip mfib vrf {vrf} {group} {source} verbose

# =====================================
class ShowIpMfib(ShowIpMfibSchema):
    """Parser for:
      show ip mfib
      show ip mfib {group}
      show ip mfib {group} {source}
      show ip mfib verbose
      show ip mfib {group} verbose
      show ip mfib {group} {source} verbose
      show ip mfib vrf {vrf}
      show ip mfib vrf {vrf} {group}
      show ip mfib vrf {vrf} {group} {source}
      show ip mfib vrf {vrf} verbose
      show ip mfib vrf {vrf} {group} verbose
      show ip mfib vrf {vrf} {group} {source} verbose"""
    cli_command = ['show ip mfib',
                   'show ip mfib {group}',
                   'show ip mfib {group} {source}',
                   'show ip mfib {verbose}',
                   'show ip mfib {group} {verbose}',
                   'show ip mfib {group} {source} {verbose}',
                   'show ip mfib vrf {vrf}',
                   'show ip mfib vrf {vrf} {group}',
                   'show ip mfib vrf {vrf} {group} {source}',
                   'show ip mfib vrf {vrf} {verbose}',
                   'show ip mfib vrf {vrf} {group} {verbose}',
                   'show ip mfib vrf {vrf} {group} {source} {verbose}' ]


    def cli(self, vrf='Default',verbose='',group='',source='', address_family='ipv4',output=None):
        cmd="show ip mfib"
        if output is None:

            if vrf != 'Default':
                cmd += " vrf {vrf}".format(vrf=vrf)

            if group:
                cmd += " {group}".format(group=group)
            if source:
                cmd += " {source}".format(source=source)
            if verbose:
                cmd += " {verbose}".format(verbose=verbose)

            out = self.device.execute(cmd)
        else:
            out = output

        # initial variables

        mfib_dict = {}
        sub_dict = {}
        outgoing = False
        egress_data_update = False
        #Default
        #VRF vrf1
        p1 = re.compile(r'^(VRF\s+)?(?P<vrf>[\w]+)$')

        #  (*,225.1.1.1) Flags: C HW
        # (70.1.1.10,225.1.1.1) Flags: HW
        #  (*,FF05:1:1::1) Flags: C HW
        # (2001:70:1:1::10,FF05:1:1::1) Flags: HW
        p3 = re.compile(r'^\((?P<source_address>[\w\:\.\*\/]+)\,'
                     '(?P<multicast_group>[\w\:\.\/]+)\)'
                     '\s+Flags\:(?P<mfib_flags>[\s\w\s]+$|$)')
        #0x1AF0  OIF-IC count: 0, OIF-A count: 1
        p4 = re.compile(r'\w+ +OIF-IC count: +(?P<oif_ic_count>[\w]+)'
                   '\, +OIF-A count: +(?P<oif_a_count>[\w]+)$')
        # SW Forwarding: 0/0/0/0, Other: 0/0/0
        p5 = re.compile(r'SW Forwarding\:\s+(?P<sw_packet_count>[\w]+)\/'
                     r'(?P<sw_packets_per_second>[\w]+)\/'
                     r'(?P<sw_average_packet_size>[\w]+)\/'
                     r'(?P<sw_kbits_per_second>[\w]+)\,'
                     r'\s+Other\: +(?P<sw_total>[\w]+)\/'
                     r'(?P<sw_rpf_failed>[\w]+)\/'
                     r'(?P<sw_other_drops>[\w]+)$')
        #HW Forwarding:   222/0/204/0, Other: 0/0/0
        p6 = re.compile(r'^HW\s+Forwarding\:\s+(?P<hw_packet_count>[\w]+)\/'
                     r'(?P<hw_packets_per_second>[\w]+)\/'
                     r'(?P<hw_average_packet_size>[\w]+)\/'
                     r'(?P<hw_kbits_per_second>[\w]+)\,'
                     r'\s+Other\: +(?P<hw_total>[\w]+)\/'
                     r'(?P<hw_rpf_failed>[\w]+)\/'
                     r'(?P<hw_other_drops>[\w]+)$')
        # LISP0.1 Flags: A NS
        #  Null0 Flags: A
        #  GigabitEthernet1/0/1 Flags: A NS
        #Tunnel0, VXLAN Decap Flags: A
        #Vlan500, VXLAN v4 Encap (50000, 239.1.1.0) Flags: A
        #Vlan500, VXLAN v6 Encap (50000, FF13::1) Flags: A
        #Port-channel5 Flags: RA A MA

        p7 = re.compile(r'^(?P<ingress_if>[\w\/\.\-\:]+)'
                         '(\,\s+VXLAN +(?P<ingress_vxlan_version>[v0-9]+)?(\s+)?(?P<ingress_vxlan_cap>[\w]+)(\s+)?(\(?(?P<ingress_vxlan_vni>[0-9]+)(\,\s+)?(?P<ingress_vxlan_nxthop>[\w:./]+)?\)?)?)?'
                         ' +Flags\: +(?P<ingress_flags>A[\s\w]+|[\s\w]+ +A[\s\w]+|A$)')

        #Vlan2001 Flags: F NS
        #LISP0.1, (100.11.11.11, 235.1.3.167) Flags:
        #Tunnel0, VXLAN Decap Flags: F
        #Vlan500, VXLAN v4 Encap (50000, 239.1.1.0) Flags: F
        #Vlan500, VXLAN v6 Encap (50000, FF13::1) Flags: F
        #L2LISP0.699, L2LISP Decap Flags: F NS
        #Null0, LISPv4 Decap Flags: RF F NS
        #Port-channel5 Flags: RF F NS
        p8 = re.compile(r'^(?P<egress_if>[\w\/\.\-\:]+)'
                        '(\,\s+LISPv4\s*Decap\s*)?'
                        '(\,\s+L2LISP\s*Decap\s*)?'
                        '(\,\s+\(?(?P<egress_rloc>[\w\.]+)(\,\s+)?(?P<egress_underlay_mcast>[\w\.]+)?\)?)?'
                        '(\,\s+VXLAN +(?P<egress_vxlan_version>[v0-9]+)?(\s+)?(?P<egress_vxlan_cap>[\w]+)(\s+)?(\(?(?P<egress_vxlan_vni>[0-9]+)(\,\s+)?(?P<egress_vxlan_nxthop>[\w:./]+)?\)?)?)?'
						'\s+Flags\:\s?(?P<egress_flags>F[\s\w]+|[\s\w]+\s+F[\s\w]+|F$|[\s\w]+\s+F$|$)')

        #CEF: Adjacency with MAC: 01005E010101000A000120010800
        p9_1 = re.compile(r'^CEF\: +(?P<egress_adj_mac>[\w \:\(\)\.]+)$')
        #CEF: Special OCE (discard)
        p9_2 = re.compile(r'^CEF\: +(?P<egress_adj_mac>[\w \(\.\)]+)$')
        #Pkts: 0/0/2    Rate: 0 pps
        p10 = re.compile(r'^Pkts\:\s+(?P<egress_hw_pkt_count>[\w]+)\/'
                         '(?P<egress_fs_pkt_count>[\w]+)\/'
                         '(?P<egress_ps_pkt_count>[\w]+)'
                         '\s+Rate\:\s+(?P<egress_pkt_rate>[\w]+)\s+pps$')

        for line in out.splitlines():
            line = line.strip()

            mfib_dict.setdefault('vrf',{})
            #Default   (Would not be displayed in the output)
            #VRF vrf1
            m = p1.match(line)
            if m:
                vrf=m.groupdict()['vrf']
                continue

            mfib_data = mfib_dict['vrf'].setdefault(vrf,{}).setdefault('address_family',{}).setdefault(address_family,{})

            #  (*,225.1.1.1) Flags: C HW
            # (70.1.1.10,225.1.1.1) Flags: HW
            #  (*,FF05:1:1::1) Flags: C HW
            # (2001:70:1:1::10,FF05:1:1::1) Flags: HW
            m = p3.match(line)
            if m:
                group = m.groupdict()
                source_address = group['source_address']
                multicast_group = group['multicast_group']

                mfib_data.setdefault('multicast_group',{})
                sub_dict = mfib_data.setdefault('multicast_group',{}).setdefault(
                    multicast_group,{}).setdefault('source_address',
                    {}).setdefault(source_address,{})

                sub_dict['flags'] = group['mfib_flags'].strip()
                continue

            sw_data=sub_dict
            #0x1AF0  OIF-IC count: 0, OIF-A count: 1
            m=p4.match(line)
            if m:
                group = m.groupdict()
                sw_data['oif_ic_count'] = int(group['oif_ic_count'])
                sw_data['oif_a_count'] = int(group['oif_a_count'])
                continue

            # SW Forwarding: 0/0/0/0, Other: 0/0/0
            m = p5.match(line)
            if m:
                changedict={}
                for key in m.groupdict().keys():
                  changedict[key] = int(m.groupdict()[key])
                sw_data.update(changedict)
                continue

            #HW Forwarding:   222/0/204/0, Other: 0/0/0
            m=p6.match(line)
            if m:
                changedict={}
                for key in m.groupdict().keys():
                    if 'NA' in m.groupdict()[key]:
                        changedict[key] = (m.groupdict()[key])
                    else:
                        changedict[key] = int(m.groupdict()[key])
                sw_data.update(changedict)
                continue

            # LISP0.1 Flags: A NS
            #  Null0 Flags: A
            #  GigabitEthernet1/0/1 Flags: A NS
            #Tunnel0, VXLAN Decap Flags: A
            #Vlan500, VXLAN v4 Encap (50000, 239.1.1.0) Flags: A
            #Vlan500, VXLAN v6 Encap (50000, FF13::1) Flags: A
            m=p7.match(line)
            if m:
                group = m.groupdict()
                ingress_interface = group['ingress_if']
                ing_intf_dict = sw_data.setdefault('incoming_interfaces',{}).setdefault(ingress_interface,{})
                ing_intf_dict['ingress_flags'] = group['ingress_flags']
                if group['ingress_vxlan_cap']:
                    ing_intf_dict['ingress_vxlan_cap']=group['ingress_vxlan_cap']
                if group['ingress_vxlan_version']:
                    ing_intf_dict['ingress_vxlan_version']=group['ingress_vxlan_version']
                    ing_intf_dict['ingress_vxlan_vni']=group['ingress_vxlan_vni']
                    ing_intf_dict['ingress_vxlan_nxthop']=group['ingress_vxlan_nxthop']
                continue


            #Vlan2001 Flags: F NS
            #LISP0.1, (100.11.11.11, 235.1.3.167) Flags:
            #Tunnel0, VXLAN Decap Flags: F
            #Vlan500, VXLAN v4 Encap (50000, 239.1.1.0) Flags: F
            #Vlan500, VXLAN v6 Encap (50000, FF13::1) Flags: F
            #Null0, LISPv4 Decap Flags: RF F NS
            m=p8.match(line)

            if m:
                group = m.groupdict()
                outgoing_interface=group['egress_if']
                egress_data=sw_data.setdefault('outgoing_interfaces',{}).setdefault(outgoing_interface,{})
                egress_data_update = True
                if group['egress_rloc']:
                    egress_data['egress_rloc'] = group['egress_rloc']

                    #### adding this code for lisp and evpn interfaces with have unique
                    #### egress interface causing the last egress interface alone getting captured
                    #example below
                    # LISP0.1, 100.22.22.22 Flags: F
                    #Pkts: 0/0/1    Rate: 0 pps
                    #LISP0.1, 100.154.154.154 Flags: F
                    #Pkts: 0/0/1    Rate: 0 pps
                    #LISP0.1, 100.88.88.88 Flags: F
                    #Pkts: 0/0/1    Rate: 0 pps
                    #LISP0.1, 100.33.33.33 Flags: F

                    outgoing_interface='{},{}'.format(group['egress_if'], group['egress_rloc'])

                egress_data['egress_flags'] = group['egress_flags']
                if group['egress_underlay_mcast']:
                    egress_data['egress_underlay_mcast'] = group['egress_underlay_mcast']
                if group['egress_vxlan_cap']:
                    egress_data['egress_vxlan_cap']=group['egress_vxlan_cap']
                if group['egress_vxlan_version']:
                    egress_data['egress_vxlan_version']=group['egress_vxlan_version']
                if group['egress_vxlan_vni']:
                    egress_data['egress_vxlan_vni']=group['egress_vxlan_vni']
                if group['egress_vxlan_nxthop']:
                    egress_data['egress_vxlan_nxthop']=group['egress_vxlan_nxthop']

                continue
            #CEF: Adjacency with MAC: 01005E010101000A000120010800
            m=p9_1.match(line)
            if m and egress_data_update:
                group = m.groupdict()
                egress_data['egress_adj_mac'] = group['egress_adj_mac']
                continue
            #CEF: Special OCE (discard)
            m=p9_2.match(line)
            if m and egress_data_update:
                group = m.groupdict()
                egress_data['egress_adj_mac'] = group['egress_adj_mac']
                continue
            #Pkts: 0/0/2    Rate: 0 pps
            m=p10.match(line)
            if m and egress_data_update:
                changedict={}
                for key in m.groupdict().keys():
                  changedict[key] = int(m.groupdict()[key])
                egress_data.update(changedict)
                continue
        return mfib_dict

class ShowIpMribSchema(MetaParser):
    """Schema for:
       show ip mrib route
       show ip mrib route {group}
       show ip mrib route {group} {source}
       show ip mrib route vrf {vrf}
       show ip mrib route vrf {vrf} {group}
       show ip mrib route vrf {vrf} {group} {source}
    """

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'multicast_group': {
                            Any(): {
                                'source_address': {
                                    Any(): {
                                        'rpf_nbr': str,
                                        Optional('flags'): str,
                                        Optional('incoming_interface_list'): {
                                            Any(): {
                                                Optional('ingress_flags'): str,
                                            }
                                        },
                                        Optional('egress_interface_list'): {
                                            Any(): {
                                                Optional('egress_flags'): str,
                                                Optional('egress_next_hop'): str,
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

class ShowIpMrib(ShowIpMribSchema):
    """Parser for:
    show ip mrib route
    show ip mrib route {group}
    show ip mrib route {group} {source}
    show ip mrib route vrf {vrf}
    show ip mrib route vrf {vrf} {group}
    show ip mrib route vrf {vrf} {group} {source}"""

    cli_command = ['show ip mrib route',
                   'show ip mrib route {group}',
                   'show ip mrib route {group} {source}',
                   'show ip mrib vrf {vrf} route',
                   'show ip mrib vrf {vrf} route {group}',
                   'show ip mrib vrf {vrf} route {group} {source}']


    def cli(self, vrf='default', group='',source='',address_family='ipv4',output=None):
        cmd="show ip mrib "
        if output is None:

            if vrf != 'default':
                cmd += " vrf {vrf} ".format(vrf=vrf)
            cmd += "route"
            if group:
                cmd += " {group}".format(group=group)
            if source:
                cmd += " {source}".format(source=source)

            output = self.device.execute(cmd)

        # initial variables
        mrib_dict = {}
        sub_dict = {}
        outgoing = False

        # (*,225.1.1.1) RPF nbr: 10.10.10.1 Flags: C
        # (3.3.3.3,225.1.1.1) RPF nbr: 10.10.10.1 Flags:
        # (*,FF05:1:1::1) RPF nbr: 2001:150:1:1::1 Flags: C
        #(2001:192:168:7::11,FF05:1:1::1) RPF nbr: 2001:150:1:1::1 Flags: L C

        p1 = re.compile(r'^\((?P<source_address>[\w\:\.\*\/]+)\,'
                     '(?P<multicast_group>[\w\:\.\/]+)\)'
                     ' +RPF nbr: (?P<RPF_nbr>[\w\:\.\/]+)'
                     '\s+Flags\:(?P<mrib_flags>[\w\s]+|$)')

        # GigabitEthernet2/0/6 Flags: A NS
        # Tunnel1 Flags: A NS
        # Vlan500 Flags: A      VXLAN Encap/Decap       Next-hop: (0.0.0.0, 1.4.0.0)
        p2 = re.compile(r'^(?P<ingress_if>[\w\.\/\, ]+)'
                         '\s+Flags\: +(?P<ingress_flags>A[\sA-UW-Z0-9]+|[\s\w]+ +A[\sA-UW-Z0-9]+|A$)')

        #  LISP0.1 Flags: F NS  Next-hop: 100.154.154.154
        #  LISP0.1 Flags: F NS   Next-hop: (100.11.11.11, 235.1.3.167)
        #  Vlan500 Flags: F      VXLAN Encap/Decap       Next-hop: (239.1.1.0, 1.4.0.0)
        p3 = re.compile(r'^(?P<egress_if>[\w\.\/\,]+)'
                        '\s+Flags\:\s+(?P<egress_flags>F[\s\w]+)+((\s+)?VXLAN Encap\/Decap(\s+)?)?Next-hop\:\s+(?P<egress_next_hop>([\w\:\.\*\/]+)|(\([\w\:\.\*\/]+\, +[\w\:\.\*\/]+\)))$')

        #  Vlan2006 Flags: F LI NS
        p4=re.compile(r'^(?P<egress_if>[\w\.\/\, ]+)'
                        '\s+Flags\: +(?P<egress_flags>F[\s\w]+)')



        for line in output.splitlines():
            line=(line.strip()).replace('\t',' ')
            mrib_dict.setdefault('vrf',{})
            mrib_data = mrib_dict['vrf'].setdefault(vrf,{}).setdefault('address_family',{}).setdefault(address_family,{})
            #  (*,225.1.1.1) Flags: C HW
            # (70.1.1.10,225.1.1.1) Flags: HW
            #  (*,FF05:1:1::1) Flags: C HW
            # (2001:70:1:1::10,FF05:1:1::1) Flags: HW
            m = p1.match(line)
            if m:

                group = m.groupdict()
                source_address = group['source_address']
                multicast_group = group['multicast_group']

                mrib_data.setdefault('multicast_group',{})
                sub_dict = mrib_data['multicast_group']\
                    .setdefault(multicast_group,{})\
                    .setdefault('source_address',{})\
                    .setdefault(source_address,{})
                sub_dict['rpf_nbr'] = m.groupdict()['RPF_nbr']
                sub_dict['flags'] = m.groupdict()['mrib_flags']

                continue

            # GigabitEthernet2/0/6 Flags: A NS
            # Tunnel50 Flags: A
            sw_data=sub_dict
            m=p2.match(line)
            if m:
                group = m.groupdict()
                ingress_interface = group['ingress_if']
                ing_intf_dict=sw_data.setdefault('incoming_interface_list',{}).setdefault(ingress_interface,{})
                ing_intf_dict['ingress_flags'] = group['ingress_flags']
                continue


            #  LISP0.1 Flags: F NS  Next-hop: 100.154.154.154
            # LISP0.1 Flags: F NS	Next-hop: (100.11.11.11, 235.1.3.167)
            m=p3.match(line)
            if m:
                group = m.groupdict()
                egress_interface = group['egress_if']

                if group['egress_next_hop']:

                    egress_next_hop = group['egress_next_hop']
                    #Overlay interfaces have multiple egress interfaces with same  ID
                    #appending egress interface with nexthop to get complete data structure
                    # LISP0.1 Flags: F      Next-hop: 100.154.154.154
                    # LISP0.1 Flags: F      Next-hop: 100.33.33.33
                    # LISP0.1 Flags: F      Next-hop: 100.88.88.88

                    egress_interface = group['egress_if']+'-'+egress_next_hop

                egress_data=sw_data.setdefault('egress_interface_list',{}).setdefault(egress_interface,{})
                egress_data['egress_flags'] = group['egress_flags']
                egress_data['egress_next_hop'] =  group['egress_next_hop']

                continue

            # Vlan2001 Flags: F NS
            m=p4.match(line)
            if m:
                group = m.groupdict()
                egress_flags = group['egress_flags']
                egress_interface = group['egress_if']

                egress_data=sw_data.setdefault('egress_interface_list',{}).setdefault(egress_interface,{})
                egress_data['egress_flags'] = egress_flags

                continue

        return mrib_dict

# ===============================
# Schema for:
#    * 'show ip sla statistics'
#    * 'show ip sla statistics {probe_id}'
# ===============================
class ShowIpSlaStatisticsSchema(MetaParser):
    ''' Schema for:
        * "show ip sla statistics"
        * "show ip sla statistics {probe_id}"
    '''
    schema = {
        'ids': {
            Any(): {
                'probe_id': int,
                Optional('rtt_stats'): str,
                Optional('start_time'): str,
                Optional('return_code'): str,
                Optional('no_of_success'): int,
                Optional('no_of_failures'): int,
                Optional('ttl'): int,
                Optional('return_code'): str,
                Optional('oper_id'): int,
                Optional('no_of_failures'): int,
                Optional('delay'): str,
                Optional('destination'): str,
            },
        }
    }


# ===============================
# Parser for:
#    * 'show ip sla statistics'
#    * 'show ip sla statistics {probe_id}'
# ===============================
class ShowIpSlaStatistics(ShowIpSlaStatisticsSchema):
    '''Parser for:
       * "show ip sla statistics"
       * "show ip sla statistics {probe_id}"
    '''
    cli_command = ['show ip sla statistics','show ip sla statistics {probe_id}']

    def cli(self, probe_id='', output=None):

        if output is None:
            if probe_id:
                cmd = self.cli_command[1].format(probe_id=probe_id)
            else:
                cmd = self.cli_command[0]

            output = self.device.execute(cmd)

        # Initialize dictionary
        parsed_dict = {}

        # IPSLA operation id: 1
        p1 = re.compile(r'^IPSLA operation id: (?P<probe_id>\d+)$')

        # Latest RTT: NoConnection/Busy/Timeout
        p2 = re.compile(r'^Latest RTT: (?P<rtt_stats>.*).*$')

        # Latest operation start time: 00:33:01 PDT Mon Sep 20 2021
        p3 = re.compile(r'^Latest operation start time: (?P<start_time>.*)$')

        # Latest operation return code: Timeout
        p4 = re.compile(r'^Latest operation return code: (?P<return_code>\w+)')

        # Number of successes: 0
        p5 = re.compile(r'^Number of successes: (?P<no_of_success>\d+)$')

        # Number of failures: 1
        p6 = re.compile(r'^Number of failures: (?P<no_of_failures>\d+)$')

        # Operation time to live: 3569 sec
        p7 = re.compile(r'^Operation time to live: (?P<ttl>\d+).*$')

        # oper-id        status               lossSD       delay                  destination
        # 60988531       OK                   0            3220998/3222178/3222998             10.50.10.100
        p8 = re.compile(r'^(?P<oper_id>^\d+)\s+'
                r'(?P<return_code>\w+)\s+'
                r'(?P<no_of_failures>\d+)\s+'
                r'(?P<delay>\d+\/+\d+\/+\d+)\s+'
                r'(?P<destination>.*)$')

        for line in output.splitlines():
            line = line.strip()

            # IPSLA operation id: 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                id = group['probe_id']
                id_dict = parsed_dict.setdefault('ids', {}).setdefault(id, {})
                id_dict.update({'probe_id':int(group['probe_id'])})
                continue

            # Latest RTT: NoConnection/Busy/Timeout
            m = p2.match(line)
            if m:
                group = m.groupdict()
                id_dict.update({'rtt_stats':group['rtt_stats']})
                continue

            # Latest operation start time: 00:33:01 PDT Mon Sep 20 2021
            m = p3.match(line)
            if m:
                group = m.groupdict()
                id_dict.update({'start_time':group['start_time']})
                continue

            # Latest operation return code: Timeout
            m = p4.match(line)
            if m:
                group = m.groupdict()
                id_dict.update({'return_code':group['return_code']})
                continue

            # Number of successes: 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                id_dict.update({'no_of_success':int(group['no_of_success'])})
                continue

            # Number of failures: 1
            m = p6.match(line)
            if m:
                group = m.groupdict()
                id_dict.update({'no_of_failures':int(group['no_of_failures'])})
                continue

            # Operation time to live: 3569 sec
            m = p7.match(line)
            if m:
                group = m.groupdict()
                id_dict.update({'ttl':int(group['ttl'])})
                continue

            # oper-id        status               lossSD       delay                  destination
            # 60988531       OK                   0            3220998/3222178/3222998             10.50.10.100
            m = p8.match(line)
            if m:
                group = m.groupdict()
                id_dict.update({
                    'oper_id':int(group['oper_id']),
                    'return_code': group['return_code'],
                    'no_of_failures':int(group['no_of_failures']),
                    'delay': group['delay'],
                    'destination': group['destination']})
                continue

        return parsed_dict

# ===============================
# Schema for:
#    * 'show ip sla statistics details'
#    * 'show ip sla statistics {probe_id} details'
# ===============================

class ShowIpSlaStatisticsDetailsSchema(MetaParser):
    """ Schema for:
        * 'show ip sla statistics details'
        * 'show ip sla statistics {probe_id} details'
    """
    schema = {
        'ids': {
            Any(): {
                'probe_id': int,
                Optional('rtt_stats'): str,
                Optional('start_time'): str,
                Optional('return_code'): str,
                Optional('no_of_success'): int,
                Optional('no_of_failures'): int,
                Optional('ttl'): int,
                Optional('threshold_occurances'): str,
                'state_of_entry': str,
                'reset_time': str,
                Optional('type_of_operation'): str,
                Optional('delay'): str,
                Optional('destination'): str,
                Optional('oper_id'): int,
            },
        }
    }

# ===============================
# Parser for:
#    * 'show ip sla statistics details'
#    * 'show ip sla statistics {probe_id} details'
# ===============================

class ShowIpSlaStatisticsDetails(ShowIpSlaStatisticsDetailsSchema):
    """ Parser for:
        * 'show ip sla statistics details'
        * 'show ip sla statistics {probe_id} details'
    """

    cli_command = ['show ip sla statistics details', 'show ip sla statistics {probe_id} details']

    def cli(self, probe_id='', output=None):
        if output is None:
            if probe_id:
                cmd =  self.cli_command[1].format(probe_id=probe_id)
            else:
                cmd = self.cli_command[0]

            output = self.device.execute(cmd)
        # Initialize dictionary
        parsed_dict = {}

        # IPSLA operation id: 50
        p1 = re.compile(r'^IPSLA operation id: (?P<probe_id>\d+)$')

        # Latest RTT: 1 milliseconds
        p2 = re.compile(r'^Latest RTT: (?P<rtt_stats>.*).*$')

        # Latest operation start time: 05:47:54 UTC Tue Sep 28 2021
        p3 = re.compile(r'^Latest operation start time: (?P<start_time>.*)$')

        # Latest operation return code: OK
        p4 = re.compile(r'^Latest operation return code: (?P<return_code>\w+)$')

        # Number of successes: 48
        p5 = re.compile(r'^Number of successes: (?P<no_of_success>\d+)$')

        # Number of failures: 0
        p6 = re.compile(r'^Number of failures: (?P<no_of_failures>\d+)$')

        # Operation time to live: Forever
        p7 = re.compile(r'^Operation time to live: (?P<ttl>\d+).*$')

        # Over thresholds occurred: FALSE
        p8 = re.compile(r'^Over thresholds occurred: (?P<threshold_occurances>.*)$')

        # Operational state of entry: Active
        p9 = re.compile(r'^Operational state of entry: (?P<state_of_entry>.*)$')

        # Last time this entry was reset: Never
        p10 = re.compile(r'^Last time this entry was reset: (?P<reset_time>.*)$')

        # Type of operation: mcast
        p11 = re.compile(r'^Type of operation: (?P<type_of_operation>.*)$')

        # oper-id        status               lossSD       delay                  destination
        # 60988531       OK                   0            3220998/3222178/3222998             10.50.10.100
        p12 = re.compile(r'^(?P<oper_id>^\d+)\s+'
                r'(?P<return_code>\w+)\s+'
                r'(?P<no_of_failures>\d+)\s+'
                r'(?P<delay>\d+\/+\d+\/+\d+)\s+'
                r'(?P<destination>.*)$')

        for line in output.splitlines():
            line = line.strip()

            # IPSLA operation id: 50
            m = p1.match(line)
            if m:
                group = m.groupdict()
                id = group['probe_id']
                id_dict = parsed_dict.setdefault('ids', {}).setdefault(id, {})
                id_dict.update({'probe_id':int(group['probe_id'])})
                continue

            # Latest RTT: 1 milliseconds
            m = p2.match(line)
            if m:
                group = m.groupdict()
                id_dict.update({'rtt_stats':group['rtt_stats']})
                continue

            # Latest operation start time: 05:47:54 UTC Tue Sep 28 2021
            m = p3.match(line)
            if m:
                group = m.groupdict()
                id_dict.update({'start_time':group['start_time']})
                continue

            # Latest operation return code: OK
            m = p4.match(line)
            if m:
                group = m.groupdict()
                id_dict.update({'return_code':group['return_code']})
                continue

            # Number of successes: 48
            m = p5.match(line)
            if m:
                group = m.groupdict()
                id_dict.update({'no_of_success':int(group['no_of_success'])})
                continue

            # Number of failures: 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                id_dict.update({'no_of_failures':int(group['no_of_failures'])})
                continue

            # Operation time to live: Forever
            m = p7.match(line)
            if m:
                group = m.groupdict()
                id_dict.update({'ttl':int(group['ttl'])})
                continue

            # Over thresholds occurred: FALSE
            m = p8.match(line)
            if m:
                group = m.groupdict()
                id_dict.update({'threshold_occurances':group['threshold_occurances']})
                continue

            # Operational state of entry: Active
            m = p9.match(line)
            if m:
                group = m.groupdict()
                id_dict.update({'state_of_entry':group['state_of_entry']})
                continue

            # Last time this entry was reset: Never
            m = p10.match(line)
            if m:
                group = m.groupdict()
                id_dict.update({'reset_time':group['reset_time']})
                continue

            # Type of operation: mcast
            m = p11.match(line)
            if m:
                group = m.groupdict()
                id_dict.update({'type_of_operation':group['type_of_operation']})
                continue

            # oper-id        status               lossSD       delay                  destination
            # 60988531       OK                   0            3220998/3222178/3222998             10.50.10.100
            m = p12.match(line)
            if m:
                group = m.groupdict()
                id_dict.update({
                    'oper_id': int(group['oper_id']),
                    'return_code': group['return_code'],
                    'no_of_failures': int(group['no_of_failures']),
                    'delay': group['delay'],
                    'destination': group['destination']})
                continue

        return parsed_dict

# ===============================
# Schema for:
#    * 'show ip sla statistics aggregated'
#    * 'show ip sla statistics aggregated {probe_id}'
# ===============================

class ShowIpSlaStatisticsAggregatedSchema(MetaParser):
    """ Schema for:
        * 'show ip sla statistics aggregated'
        * 'show ip sla statistics aggregated {probe_id}'
    """

    schema = {
        'ids': {
            Any(): {
                Optional('probe_id'): int,
                Optional('type_of_operation'): str,
                # Optional('operation_status'): str,
                Optional('start_time'): {
                    Any(): {
                        Optional('no_of_success'): int,
                        Optional('no_of_failures'): int,
                        Optional('oper_id'): int,
                        Optional('status'): str,
                        Optional('loss_sd'): int,
                        Optional('delay'): str,
                        Optional('destination'): str,
                        Optional('dns_rtt'): int,
                        Optional('tcp_connection_rtt'): int,
                        Optional('http_transaction_rtt'): int,
                    }
                },
            }
        }
    }


# ===============================
# Parser for:
#    * 'show ip sla statistics aggregated'
#    * 'show ip sla statistics aggregated {probe_id}'
# ===============================

class ShowIpSlaStatisticsAggregated(ShowIpSlaStatisticsAggregatedSchema):
    '''Parser for:
            * 'show ip sla statistics aggregated'
            * 'show ip sla statistics aggregated {probe_id}'
    '''
    cli_command = ['show ip sla statistics aggregated', 'show ip sla statistics aggregated {probe_id}']

    def cli(self, probe_id='', output=None):
        if output is None:
            if probe_id:
                cmd =  self.cli_command[1].format(probe_id=probe_id)
            else:
                cmd = self.cli_command[0]

            output = self.device.execute(cmd)

        parsed_dict = {}

        # IPSLA operation id: 50
        p1 = re.compile(r'^IPSLA operation id: (?P<probe_id>\d+)$')

        # Type of operation: tcp-connect
        p2 = re.compile(r'^Type of operation: (?P<type_of_operation>.*)$')

        # Start Time Index: 13:48:19 UTC Thu Oct 21 2021
        p3 = re.compile(r'^Start Time Index: (?P<start_time>.*)$')

        # Number of successes: 60
        p4 = re.compile(r'^Number of successes: (?P<no_of_success>\d+)$')

        # Number of failures: 0
        p5 = re.compile(r'^Number of failures: (?P<no_of_failures>\d+)$')

        # oper-id        status               lossSD       delay                  destination
        # 60988531       OK                   0            985992/996505/1057999             10.50.10.100
        p6 = re.compile(r'^(?P<oper_id>^\d+)\s+'
                r'(?P<status>\w+)\s+'
                r'(?P<loss_sd>\d+)\s+'
                r'(?P<delay>\d+\/+\d+\/+\d+)\s+'
                r'(?P<destination>.*)$')

        # DNS RTT: 0
        p7 = re.compile(r'^DNS RTT: (?P<dns_rtt>\d+)$')

        # TCP Connection RTT: 56
        p8 = re.compile(r'^TCP Connection RTT: (?P<tcp_connection_rtt>\d+)$')

        # HTTP Transaction RTT: 360
        p9 = re.compile(r'^HTTP Transaction RTT: (?P<http_transaction_rtt>\d+)$')


        for line in output.splitlines():
            line = line.strip()

            # IPSLA operation id: 50
            m = p1.match(line)
            if m:
                group = m.groupdict()
                id = group['probe_id']
                id_dict = parsed_dict.setdefault('ids', {}).setdefault(id, {})
                id_dict.update({'probe_id':int(group['probe_id'])})
                continue

            # Type of operation: tcp-connect
            m = p2.match(line)
            if m:
                group = m.groupdict()
                id_dict.update({'type_of_operation':group['type_of_operation']})
                continue

            # Start Time Index: 13:48:19 UTC Thu Oct 21 2021
            m = p3.match(line)
            if m:
                group = m.groupdict()
                start_time_dict = id_dict.setdefault('start_time', {}).setdefault(group['start_time'], {})
                continue

            # Number of successes: 60
            m = p4.match(line)
            if m:
                group = m.groupdict()
                start_time_dict.update({'no_of_success':int(group['no_of_success'])})
                continue

            # Number of failures: 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                start_time_dict.update({'no_of_failures':int(group['no_of_failures'])})
                continue

            # oper-id        status               lossSD       delay                  destination
            # 60988531       OK                   0            985992/996505/1057999             10.50.10.100
            m = p6.match(line)
            if m:
                group = m.groupdict()
                start_time_dict.update({
                    'oper_id':int(group['oper_id']),
                    'status': group['status'],
                    'loss_sd':int(group['loss_sd']),
                    'delay': group['delay'],
                    'destination': group['destination']})
                continue

            # DNS RTT: 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                start_time_dict.update({'dns_rtt': int(group['dns_rtt'])})
                continue

            # TCP Connection RTT: 56
            m = p8.match(line)
            if m:
                group = m.groupdict()
                start_time_dict.update({'tcp_connection_rtt': int(group['tcp_connection_rtt'])})
                continue

            # HTTP Transaction RTT: 360
            m = p9.match(line)
            if m:
                group = m.groupdict()
                start_time_dict.update({'http_transaction_rtt': int(group['http_transaction_rtt'])})
                continue

        return parsed_dict


# ===============================
# Schema for 'show ip sla responder'
# ===============================
class ShowIpSlaResponderSchema(MetaParser):
    ''' Schema for "show ip sla responder" '''
    schema = {
        'ports': {
            Any(): {
                'control_port': int,
                'control_v2_port': int,
                'general_responder': str,
                'permanent_responder': str,
            },
        }
    }


# ===============================
# Parser for 'show ip sla responder'
# ===============================
class ShowIpSlaResponder(ShowIpSlaResponderSchema):
    """Parser for:
    show ip sla responder
    """
    cli_command = 'show ip sla responder'

    def cli(self, output=None):

        parsed_dict = {}

        if output is None:
            output = self.device.execute(self.cli_command)

        #General IP SLA Responder on Control port 1967
        p1 = re.compile(r'^General\s+IP\s+SLA\s+Responder\s+on\s+Control\s+port\s+(?P<control_port>\d+)$')

        #General IP SLA Responder on Control V2 port 1167
        p2 = re.compile(r'^General\s+IP\s+SLA\s+Responder\s+on\s+Control\s+V2\s+port\s+(?P<control_v2_port>\d+)$')

        #General IP SLA Responder is: Disabled
        p3 = re.compile(r'^General\s+IP\s+SLA\s+Responder\s+is:\s+(?P<general_responder>\w+)$')

        #Permanent Port IP SLA Responder is: Disabled
        p4 = re.compile(r'^Permanent\s+Port\s+IP\s+SLA\s+Responder\s+is:\s+(?P<permanent_responder>\w+)$')

        for line in output.splitlines():
            line = line.strip()

            #General IP SLA Responder on Control port 1967
            m = p1.match(line)
            if m:
                group = m.groupdict()
                control_port = group['control_port']
                id_dict = parsed_dict.setdefault('ports', {}).setdefault(control_port, {})
                id_dict.update({'control_port':int(group['control_port'])})
                continue


	        #General IP SLA Responder on Control V2 port 1167
            m = p2.match(line)
            if m:
                group = m.groupdict()
                control_v2_port = group['control_v2_port']
                id_dict = parsed_dict.setdefault('ports', {}).setdefault(control_port, {})
                id_dict.update({'control_v2_port':int(group['control_v2_port'])})
                continue

            #General IP SLA Responder is: Disabled
            m = p3.match(line)
            if m:
                group = m.groupdict()
                id_dict.update({'general_responder':group['general_responder']})
                continue


	        #Permanent Port IP SLA Responder is: Disabled
            m = p4.match(line)
            if m:
                group = m.groupdict()
                id_dict.update({'permanent_responder':group['permanent_responder']})
                continue

        return parsed_dict


class ShowIpDhcpBindingSchema(MetaParser):
    """
    Schema for show ip dhcp binding
               show ip dhcp binding vrf {vrf_name}
    """
    schema = {
        Optional('dhcp_binding'): {
            Any(): {
                Optional('ip_address'): str,
                Optional('client_id'): str,
                Optional('lease_expiration'): str,
                Optional('type'): str,
                Optional('state'): str,
                Optional('interface'):str
            }
        }
    }

class ShowIpDhcpBinding(ShowIpDhcpBindingSchema):

    ''' Parser for "show ip dhcp binding"
                   " show ip dhcp binding vrf {vrf_name}"
    '''
    cli_command = ['show ip dhcp binding', 'show ip dhcp binding vrf {vrf_name}']

    # Defines a function to run the cli_command
    def cli(self, vrf_name='', output=None):
        if output is None:
            if vrf_name:
                cmd = self.cli_command[1].format(vrf_name=vrf_name)
            else:
                cmd = self.cli_command[0]

            output = self.device.execute(cmd)

        parsed_dict = {}

        # for number of bindings
        var=1

        # IP address      Client-ID/ 		Lease expiration 	Type       State      Interface
        # 		Hardware address/
        # 		User name
        # 100.1.0.3       0100.1094.0000.01       Feb 08 2022 11:11 AM    Automatic  Active     TenGigabitEthernet1/0/2
        # 100.0.0.12      0010.9400.0004          May 13 2022 04:29 PM    Relay      Active     Port-channel40.2
        p1 = re.compile(r'^\s*(?P<ip_address>(\d+\.\d+\.\d+\.\d+))\s+(?P<client_id>([0-9a-f\.]+))\s+(?P<lease_expiration>([a-zA-Z]{3}\s\d{1,2}\s\d{4}\s\d{1,2}\:\d{1,2}\s[a-zA-Z]{2}|Infinite))\s+(?P<type>\w+)\s+(?P<state>\w+)\s+(?P<interface>[\w\.\-\/]+)\s*$')

        # Defines the "for" loop, to pattern match each line of output
        for line in output.splitlines():
            line = line.strip()

            # 100.1.0.3       0100.1094.0000.01       Feb 08 2022 11:11 AM    Automatic  Active     TenGigabitEthernet1/0/2
            m = p1.match(line)
            parsed_dict.setdefault('dhcp_binding', {})
            if m:
                parsed_dict['dhcp_binding'].setdefault(var, {})
                group = m.groupdict()
                parsed_dict['dhcp_binding'][var]['ip_address'] = str(group['ip_address'])
                parsed_dict['dhcp_binding'][var]['client_id'] = str(group['client_id'])
                parsed_dict['dhcp_binding'][var]['lease_expiration'] = str(group['lease_expiration'])
                parsed_dict['dhcp_binding'][var]['type'] = str(group['type'])
                parsed_dict['dhcp_binding'][var]['state'] = str(group['state'])
                parsed_dict['dhcp_binding'][var]['interface'] = str(group['interface'])
                var+=1
                continue

        return parsed_dict

# ==========================================
# Schema for 'show ip dhcp server statistics'
# ==========================================
class ShowIpDhcpServerStatisticsSchema(MetaParser):
    """
    Schema for show ip dhcp server statistics
    """
    schema = {
        'memory_usage': int,
        'address_pools': int,
        'database_agents': int,
        'automatic_bindings': int,
        'manual_bindings': int,
        'expired_bindings': int,
        'malformed_messages': int,
        'secure_arp_entries': int,
        'renew_messages': int,
        'workspace_timeouts': int,
        'static_routes': int,
        'relay_bindings': int,
        'relay_bindings_active': int,
        'relay_bindings_terminated': int,
        'relay_bindings_selecting': int,
        Optional('dhcp_relay_ack_drop') : int,
        Optional('dhcp_discovers_dropped') : int,
        'message_received': {
            'bootrequest': int,
            'dhcpdiscover': int,
            'dhcprequest': int,
            'dhcpdecline': int,
            'dhcprelease': int,
            'dhcpinform': int,
            'dhcpvendor': int,
            'bootreply': int,
            'dhcpoffer': int,
            'dhcpack': int,
            'dhcpnak': int
        },
        'message_sent':{
            'bootreply': int,
            'dhcpoffer': int,
            'dhcpack': int,
            'dhcpnak': int
        },
        'message_forwarded': {
            'bootrequest': int,
            'dhcpdiscover': int,
            'dhcprequest': int,
            'dhcpdecline': int,
            'dhcprelease': int,
            'dhcpinform': int,
            'dhcpvendor': int,
            'bootreply': int,
            'dhcpoffer': int,
            'dhcpack': int,
            'dhcpnak': int
        },
        'dhcp_dpm_statistics': {
            'offer_notifications_sent': int,
            'offer_callbacks_received': int,
            'classname_requests_sent': int,
            'classname_callbacks_received': int
        },
    }

# =======================================
# Parser for 'show ip dhcp binding'
# =======================================
class ShowIpDhcpServerStatistics(ShowIpDhcpServerStatisticsSchema):
    ''' Parser for "show ip dhcp server statistics"'''
    cli_command = 'show ip dhcp server statistics'

    # Defines a function to run the cli_command
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initializes the Python dictionary variable
        parsed_dict = {}

        # Memory usage         17342
        p1 = re.compile(r'^Memory\s+usage\s+(?P<memory_usage>\d+)\s*$')
        # Address pools        1
        p2 = re.compile(r'^Address\s+pools\s+(?P<address_pools>\d+)\s*$')
        # Database agents      0
        p3 = re.compile(r'^Database\s+agents\s+(?P<database_agents>\d+)\s*$')
        # Automatic bindings   0
        p4 = re.compile(r'^Automatic\s+bindings\s+(?P<automatic_bindings>\d+)\s*$')
        # Manual bindings      0
        p5 = re.compile(r'^Manual\s+bindings\s+(?P<manual_bindings>\d+)\s*$')
        # Expired bindings     0
        p6 = re.compile(r'^Expired\s+bindings\s+(?P<expired_bindings>\d+)\s*$')
        # Malformed messages   0
        p7 = re.compile(r'^Malformed\s+messages\s+(?P<malformed_messages>\d+)\s*$')
        # Secure arp entries   0
        p8 = re.compile(r'^Secure\s+arp\s+entries\s+(?P<secure_arp_entries>\d+)\s*$')
        # Renew messages       0
        p9 = re.compile(r'^Renew\s+messages\s+(?P<renew_messages>\d+)\s*$')
        # Workspace timeouts   0
        p10 = re.compile(r'^Workspace\s+timeouts\s+(?P<workspace_timeouts>\d+)\s*$')
        # Static routes        0
        p11 = re.compile(r'^Static\s+routes\s+(?P<static_routes>\d+)\s*$')
        # Relay bindings       0
        p12 = re.compile(r'^Relay\s+bindings\s+(?P<relay_bindings>\d+)\s*$')
        # Relay bindings active        0
        p13 = re.compile(r'^Relay\s+bindings\s+active\s+(?P<relay_bindings_active>\d+)\s*$')
        # Relay bindings terminated    0
        p14 = re.compile(r'^Relay\s+bindings\s+terminated\s+(?P<relay_bindings_terminated>\d+)\s*$')
        # Relay bindings selecting     0
        p15 = re.compile(r'^Relay\s+bindings\s+selecting\s+(?P<relay_bindings_selecting>\d+)\s*$')

        # Message              Received
        # BOOTREQUEST          0
        p16 = re.compile(r'^BOOTREQUEST\s+(?P<bootrequest>\d+)\s*$')
        # DHCPDISCOVER         0
        p17 = re.compile(r'^DHCPDISCOVER\s+(?P<dhcpdiscover>\d+)\s*')
        # DHCPREQUEST          0
        p18 = re.compile(r'^DHCPREQUEST\s+(?P<dhcprequest>\d+)\s*$')
        # DHCPDECLINE          0
        p19 = re.compile(r'^DHCPDECLINE\s+(?P<dhcpdecline>\d+)\s*$')
        # DHCPRELEASE          0
        p20 = re.compile(r'^DHCPRELEASE\s+(?P<dhcprelease>\d+)\s*$')
        # DHCPINFORM           0
        p21 = re.compile(r'^DHCPINFORM\s+(?P<dhcpinform>\d+)\s*$')
        # DHCPVENDOR           0
        p22 = re.compile(r'^DHCPVENDOR\s+(?P<dhcpvendor>\d+)\s*$')
        # BOOTREPLY            0
        p23 = re.compile(r'^BOOTREPLY\s+(?P<bootreply>\d+)\s*')
        # DHCPOFFER            0
        p24 = re.compile(r'^DHCPOFFER\s+(?P<dhcpoffer>\d+)\s*$')
        # DHCPACK              0
        p25 = re.compile(r'^DHCPACK\s+(?P<dhcpack>\d+)\s*$')
        # DHCPNAK              0
        p26 = re.compile(r'^DHCPNAK\s+(?P<dhcpnak>\d+)\s*$')

        # Offer notifications sent        0
        p27 = re.compile(r'^Offer\s+notifications\s+sent\s+(?P<offer_notifications_sent>\d+)\s*$')
        # Offer callbacks received        0
        p28 = re.compile(r'^Offer\s+callbacks\s+received\s+(?P<offer_callbacks_received>\d+)\s*$')
        # Classname requests sent         0
        p29 = re.compile(r'^Classname\s+requests\s+sent\s+(?P<classname_requests_sent>\d+)\s*$')
        # Classname callbacks received    0
        p30 = re.compile(r'^Classname\s+callbacks\s+received\s+(?P<classname_callbacks_received>\d+)\s*$')

        # message=['message_recieved','message_sent','message_forward']
        p31 = re.compile(r'^Message\s+(?P<state>(Received|Sent|Forwarded))\s*')

        # DHCP Relay ACK drop          0
        p32 = re.compile(r"^DHCP\s+Relay\s+ACK\s+drop\s+(?P<dhcp_relay_ack_drop>\d+)$")

        # DHCP Discovers dropped       15261506
        p33 = re.compile(r"^DHCP\s+Discovers\s+dropped\s+(?P<dhcp_discovers_dropped>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # message=['message_recieved','message_sent','message_forward']
            m = p31.match(line)
            if m:
                group = m.groupdict()
                message = "message_"+str(group['state'].lower())
                parsed_dict.setdefault(message, {})
                continue

            # Memory usage         17342
            m = p1.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['memory_usage'] = int(group['memory_usage'])
                continue

            # Address pools        1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['address_pools'] = int(group['address_pools'])
                continue

            # Database agents      0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['database_agents'] = int(group['database_agents'])
                continue

            # Automatic bindings   0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['automatic_bindings'] = int(group['automatic_bindings'])
                continue

            # Manual bindings      0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['manual_bindings'] = int(group['manual_bindings'])
                continue

            # Expired bindings     0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['expired_bindings'] = int(group['expired_bindings'])
                continue

            # Malformed messages   0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['malformed_messages'] = int(group['malformed_messages'])
                continue

            # Secure arp entries   0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['secure_arp_entries'] = int(group['secure_arp_entries'])
                continue

            # Renew messages       0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['renew_messages'] = int(group['renew_messages'])
                continue

            # Workspace timeouts   0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['workspace_timeouts'] = int(group['workspace_timeouts'])
                continue

            # Static routes        0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['static_routes'] = int(group['static_routes'])
                continue

            # Relay bindings       0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['relay_bindings'] = int(group['relay_bindings'])
                continue

            # Relay bindings active        0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['relay_bindings_active'] = int(group['relay_bindings_active'])
                continue

            # Relay bindings terminated    0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['relay_bindings_terminated'] = int(group['relay_bindings_terminated'])
                continue

            # Relay bindings selecting     0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['relay_bindings_selecting'] = int(group['relay_bindings_selecting'])
                continue

            # BOOTREQUEST          0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                parsed_dict[message]['bootrequest'] = int(group['bootrequest'])
                continue

            # DHCPDISCOVER         0
            m = p17.match(line)
            if m:
                group = m.groupdict()
                parsed_dict[message]['dhcpdiscover'] = int(group['dhcpdiscover'])
                continue

            # DHCPREQUEST          0
            m = p18.match(line)
            if m:
                group = m.groupdict()
                parsed_dict[message]['dhcprequest'] = int(group['dhcprequest'])
                continue

            # DHCPDECLINE          0
            m = p19.match(line)
            if m:
                group = m.groupdict()
                parsed_dict[message]['dhcpdecline'] = int(group['dhcpdecline'])
                continue

            # DHCPRELEASE          0
            m = p20.match(line)
            if m:
                group = m.groupdict()
                parsed_dict[message]['dhcprelease'] = int(group['dhcprelease'])
                continue

            # DHCPINFORM           0
            m = p21.match(line)
            if m:
                group = m.groupdict()
                parsed_dict[message]['dhcpinform'] = int(group['dhcpinform'])
                continue

            # DHCPVENDOR           0
            m = p22.match(line)
            if m:
                group = m.groupdict()
                parsed_dict[message]['dhcpvendor'] = int(group['dhcpvendor'])
                continue

            # BOOTREPLY            0
            m = p23.match(line)
            if m:
                group = m.groupdict()
                parsed_dict[message]['bootreply'] = int(group['bootreply'])
                continue

            # DHCPOFFER            0
            m = p24.match(line)
            if m:
                group = m.groupdict()
                parsed_dict[message]['dhcpoffer'] = int(group['dhcpoffer'])
                continue

            # DHCPACK              0
            m = p25.match(line)
            if m:
                group = m.groupdict()
                parsed_dict[message]['dhcpack'] = int(group['dhcpack'])
                continue

            # DHCPNAK              0
            m = p26.match(line)
            if m:
                group = m.groupdict()
                parsed_dict[message]['dhcpnak'] = int(group['dhcpnak'])
                continue

            parsed_dict.setdefault('dhcp_dpm_statistics', {})

            # Offer notifications sent        0
            m = p27.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['dhcp_dpm_statistics']['offer_notifications_sent'] = int(group['offer_notifications_sent'])
                continue

            # Offer callbacks received        0
            m = p28.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['dhcp_dpm_statistics']['offer_callbacks_received'] = int(group['offer_callbacks_received'])
                continue

            # Classname requests sent         0
            m = p29.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['dhcp_dpm_statistics']['classname_requests_sent'] = int(group['classname_requests_sent'])
                continue

            # Classname callbacks received    0
            m = p30.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['dhcp_dpm_statistics']['classname_callbacks_received'] = int(group['classname_callbacks_received'])
                continue

            # DHCP Relay ACK drop          0
            m = p32.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['dhcp_relay_ack_drop'] = int(group['dhcp_relay_ack_drop'])
                continue

            # DHCP Discovers dropped       15261506
            m = p33.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['dhcp_discovers_dropped'] = int(group['dhcp_discovers_dropped'])
                continue
        return parsed_dict

# ====================================================
# Parser for 'show ip nhrp traffic'
#            'show ip nhrp traffic interface {tunnel}'
# ====================================================

class ShowIpNhrpTrafficSchema(MetaParser):
    """Schema for show ip nhrp traffic
                  show ip nhrp traffic interface {tunnel}
    """
    schema = {
        'interface': {
            Any(): {
                'max_send_limit': str,
                'usage': str,
                Or('sent', 'rcvd'): {
                      'total': int,
                      'resolution_request': int,
                      'resolution_reply': int,
                      'registration_request': int,
                      'registration_reply': int,
                      'purge_request': int,
                      'purge_reply': int,
                      'error_indication': int,
                      'traffic_indication': int,
                      'redirect_supress': int
                },
            }
        }
    }

class ShowIpNhrpTraffic(ShowIpNhrpTrafficSchema):
    """Parser for 'show ip nhrp traffic'
                  'show ip nhrp traffic interface {interface}'
    """

    cli_command = ['show {ip_type} nhrp traffic', 'show {ip_type} nhrp traffic interface {interface}']
    def cli(self, ip_type= "ip", interface=None, output=None):

        if interface:
            cmd = self.cli_command[1].format(ip_type=ip_type,interface=interface)
        else:
            cmd = self.cli_command[0].format(ip_type=ip_type)

        if output is None:
            # get output from device
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # Tunnel100: Max-send limit:10000Pkts/10Sec, Usage:0%
        p1 = re.compile(r'^(?P<interface>[\w\/\.\-]+):\s+'
                        'Max-send limit:\s*(?P<max_send_limit>\d+[\w\/]+),\s+'
                        'Usage:(?P<usage>\d+%)$')

        # Sent: Total 4527
        p2 = re.compile(r'^Sent:\s+Total\s+(?P<total>\d+)$')

        # Rcvd: Total 4524
        p3 = re.compile(r'^Rcvd:\s+Total\s+(?P<total>\d+)$')

        # 73 Resolution Request  69 Resolution Reply  4344 Registration Request
        p4 = re.compile(r'^(?P<resolution_request>\d+)\s+Resolution\s+Request\s+'
                        '(?P<resolution_reply>\d+)\s+Resolution\s+Reply\s+'
                        '(?P<registration_request>\d+)\s+Registration\s+Request$')

        # 0 Registration Reply  41 Purge Request  0 Purge Reply
        p5 = re.compile(r'^(?P<registration_reply>\d+)\s+Registration\s+Reply\s+'
                        '(?P<purge_request>\d+)\s+Purge\s+Request\s+'
                        '(?P<purge_reply>\d+)\s+Purge\s+Reply$')

        # 0 Error Indication  41 Traffic Indication  0 Redirect Suppress
        p6 = re.compile(r'^(?P<error_indication>\d+)\s+Error\s+Indication\s+'
                        '(?P<traffic_indication>\d+)\s+Traffic\s+Indication\s+'
                        '(?P<redirect_supress>\d+)\s+Redirect\s+Suppress$')

        for line in output.splitlines():
            line = line.strip()

            # Tunnel100
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                interface_dict = ret_dict.setdefault('interface', {})
                tunnel_int_dict = interface_dict.setdefault(group['interface'], {})
                tunnel_int_dict.update({
                    'max_send_limit': group['max_send_limit'],
                    'usage': group['usage']
                })
                continue

            # Sent: Total 4527
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                attr_dict = tunnel_int_dict.setdefault('sent', {})
                attr_dict.update({
                    'total': int(group['total']),
                })
                continue

            # Rcvd: Total 4524
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                attr_dict = tunnel_int_dict.setdefault('rcvd', {})
                attr_dict.update({
                    'total': int(group['total'])
                })
                continue

            # 73 Resolution Request  69 Resolution Reply  4344 Registration Request
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                attr_dict.update({
                    'resolution_request': int(group['resolution_request']),
                    'resolution_reply': int(group['resolution_reply']),
                    'registration_request': int(group['registration_request'])
                })
                continue

            # 0 Registration Reply  41 Purge Request  0 Purge Reply
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                attr_dict.update({
                    'registration_reply': int(group['registration_reply']),
                    'purge_request': int(group['purge_request']),
                    'purge_reply': int(group['purge_reply'])
                })
                continue

            # 0 Error Indication  41 Traffic Indication  0 Redirect Suppress
            m6 = p6.match(line)
            if m6:
                group = m6.groupdict()
                attr_dict.update({
                    'error_indication': int(group['error_indication']),
                    'traffic_indication': int(group['traffic_indication']),
                    'redirect_supress': int(group['redirect_supress'])
                })
                continue

        return ret_dict

# ============================================================
# Parser for 'show ip nhrp traffic detail'
#            'show ip nhrp traffic interface {tunnel} detail'
# ============================================================

class ShowIpNhrpTrafficDetailSchema(MetaParser):
    """Schema for show ip nhrp traffic detail
                  show ip nhrp traffic interface {tunnel} detail
    """
    schema = {
        'statistics': {
            'global_statistics': {
                'packet': int,
                'queue': int,
                'size': int,
                Or('sent', 'rcvd'): {
                    'total': int,
                    'resolution_request': int,
                    'resolution_reply': int,
                    'registration_request': int,
                    'registration_reply': int,
                    'purge_request': int,
                    'purge_reply': int,
                    'error_indication': int,
                    'traffic_indication': int,
                    'redirect_supress': int
                }
            },
            Any(): {
                'max_send_limit': str,
                'usage': str,
                Or('sent', 'rcvd', 'fwd'): {
                    'total': int,
                    'resolution_request': int,
                    'resolution_reply': int,
                    'registration_request': int,
                    'registration_reply': int,
                    'purge_request': int,
                    'purge_reply': int,
                    'error_indication': int,
                    'traffic_indication': int,
                    'redirect_supress': int
                }
            }
        }
    }

class ShowIpNhrpTrafficDetail(ShowIpNhrpTrafficDetailSchema):
    """Parser for 'show ip nhrp traffic detail'
                  'show ip nhrp traffic interface {interface} detail'
    """

    cli_command = ['show {ip_type} nhrp traffic detail',
                   'show {ip_type} nhrp traffic interface {interface} detail']
    def cli(self, ip_type= "ip",interface=None, output=None):

        if interface:
            cmd = self.cli_command[1].format(ip_type=ip_type,interface=interface)
        else:
            cmd = self.cli_command[0].format(ip_type=ip_type)

        if output is None:
            # get output from device
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # Global statistics:
        p1 = re.compile('^Global statistics:$')

        # Packet Queue size: 0[0](1)
        p2 = re.compile(r'^Packet\s+Queue\s+size:\s+(?P<packet>\d+)'
                        '\[(?P<queue>\d+)\]\((?P<size>\d+)\)$')

        # Tunnel100: Max-send limit:10000Pkts/10Sec, Usage:0%
        p3 = re.compile(r'^(?P<interface>[\w\/\.\-]+):\s+'
                        'Max-send limit:\s*(?P<max_send_limit>\d+[\w\/]+),\s+'
                        'Usage:(?P<usage>\d+%)$')

        # Sent: Total 4527
        p4 = re.compile(r'^Sent:\s+Total\s+(?P<total>\d+)$')

        # Rcvd: Total 4524
        p5 = re.compile(r'^Rcvd:\s+Total\s+(?P<total>\d+)$')

        # Fwd: Total 0
        p6 = re.compile(r'^Fwd:\s+Total\s+(?P<total>\d+)$')

        # 73 Resolution Request  69 Resolution Reply  4344 Registration Request
        p7 = re.compile(r'^(?P<resolution_request>\d+)\s+Resolution\s+Request\s+'
                        '(?P<resolution_reply>\d+)\s+Resolution\s+Reply\s+'
                        '(?P<registration_request>\d+)\s+Registration\s+Request$')

        # 0 Registration Reply  41 Purge Request  0 Purge Reply
        p8 = re.compile(r'^(?P<registration_reply>\d+)\s+Registration\s+Reply\s+'
                        '(?P<purge_request>\d+)\s+Purge\s+Request\s+'
                        '(?P<purge_reply>\d+)\s+Purge\s+Reply$')

        # 0 Error Indication  41 Traffic Indication  0 Redirect Suppress
        p9 = re.compile(r'^(?P<error_indication>\d+)\s+Error\s+Indication\s+'
                        '(?P<traffic_indication>\d+)\s+Traffic\s+Indication\s+'
                        '(?P<redirect_supress>\d+)\s+Redirect\s+Suppress$')

        for line in output.splitlines():
            line = line.strip()

            # Global statistics:
            m1 = p1.match(line)
            if m1:
                statistics_dict = ret_dict.setdefault('statistics', {})
                tunnel_global_dict = statistics_dict.setdefault('global_statistics', {})
                continue

            # Packet Queue size: 0[0](1)
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                tunnel_global_dict.update({
                    'packet': int(group['packet']),
                    'queue': int(group['queue']),
                    'size': int(group['size'])
                })
                continue

            # Tunnel100
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                tunnel_global_dict = statistics_dict.setdefault(group['interface'], {})
                tunnel_global_dict.update({
                    'max_send_limit': group['max_send_limit'],
                    'usage': group['usage']
                })
                continue

            # Sent: Total 4527
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                attr_dict = tunnel_global_dict.setdefault('sent', {})
                attr_dict.update({
                    'total': int(group['total']),
                })
                continue

            # Rcvd: Total 4524
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                attr_dict = tunnel_global_dict.setdefault('rcvd', {})
                attr_dict.update({
                    'total': int(group['total'])
                })
                continue

            # Fwd: Total 0
            m6 = p6.match(line)
            if m6:
                group = m6.groupdict()
                attr_dict = tunnel_global_dict.setdefault('fwd', {})
                attr_dict.update({
                    'total': int(group['total'])
                })
                continue

            # 73 Resolution Request  69 Resolution Reply  4344 Registration Request
            m7 = p7.match(line)
            if m7:
                group = m7.groupdict()
                attr_dict.update({
                    'resolution_request': int(group['resolution_request']),
                    'resolution_reply': int(group['resolution_reply']),
                    'registration_request': int(group['registration_request'])
                })
                continue

            # 0 Registration Reply  41 Purge Request  0 Purge Reply
            m8 = p8.match(line)
            if m8:
                group = m8.groupdict()
                attr_dict.update({
                    'registration_reply': int(group['registration_reply']),
                    'purge_request': int(group['purge_request']),
                    'purge_reply': int(group['purge_reply'])
                })
                continue

            # 0 Error Indication  41 Traffic Indication  0 Redirect Suppress
            m9 = p9.match(line)
            if m9:
                group = m9.groupdict()
                attr_dict.update({
                    'error_indication': int(group['error_indication']),
                    'traffic_indication': int(group['traffic_indication']),
                    'redirect_supress': int(group['redirect_supress'])
                })
                continue

        return ret_dict

# ==============================================
# Parser for 'show ip nhrp stats'
#            'show ip nhrp stats {tunnel}'
#            'show nhrp stats {tunnel}',
#            'show ipv6 nhrp stats {tunnel}'
#            'show ipv6 nhrp stats'
#            'show nhrp stats'
# ==============================================

class ShowIpNhrpStatsSchema(MetaParser):
    """Schema for show ip nhrp stats
                  show ip nhrp stats {tunnel}
                  show nhrp stats {tunnel}
                  show ipv6 nhrp stats {tunnel}
                  show ipv6 nhrp stats
                  show nhrp stats

    """
    schema = {
        'interface': {
            Any(): {
                'interface_state_event_stats': {
                    'r_up': int,
                    'r_up_error': int,
                    'r_down': int,
                    'r_down_error': int,
                    'r_deleted': int,
                    'r_deleted_error': int
                },
                'tunnel_stats': {
                    's_endpoint_addition': int,
                    's_endpoint_addition_error': int,
                    's_endpoint_deletion': int,
                    's_endpoint_deletion_error': int
                },
                'tunnel_protection_stats': {
                    's_create_tp_socket': int,
                    's_create_tp_socket_error': int,
                    's_del_tp_socket': int,
                    's_del_tp_socket_error': int,
                    's_create_va': int,
                    's_create_va_error': int,
                    's_del_va': int,
                    's_del_va_error': int,
                    'r_up': int,
                    'r_up_error': int,
                    'r_down': int,
                    'r_down_error': int,
                    's_reset_socket': int,
                    's_reset_socket_error': int
                },
                'tunnel_qos_stats': {
                    's_qos_apply': int,
                    's_qos_apply_error': int,
                    's_qos_remove': int,
                    's_qos_remove_error': int
                },
                'rib_event_stats': {
                    's_add_route': int,
                    's_add_route_error': int,
                    's_del_route': int,
                    's_del_route_error': int,
                    's_add_nho': int,
                    's_add_nho_error': int,
                    's_del_nho': int,
                    's_del_nho_error': int,
                    's_rwatch_wo_route': int,
                    's_rwatch_wo_route_error': int,
                    'r_route_evicted': int,
                    'r_route_evicted_error': int
                },
                'mpls_stats': {
                    's_label_alloc': int,
                    's_label_alloc_error': int,
                    's_label_release': int,
                    's_label_release_error': int,
                    's_mpls_ip_key_bind': int,
                    's_mpls_ip_key_bind_error': int,
                    's_mpls_vpn_key_bind': int,
                    's_mpls_vpn_key_bind_error': int
                },
                'bfd_stats': {
                    's_client_create': int,
                    's_client_create_error': int,
                    's_client_destroy': int,
                    's_client_destroy_error': int,
                    'r_session_down': int,
                    'r_session_down_error': int,
                    'r_session_up': int,
                    'r_session_up_error': int
                },
                'bgp_stats': {
                    's_route_export': int,
                    's_route_export_error': int,
                    's_route_withdrawal': int,
                    's_route_withdrawal_error': int,
                    's_route_import': int,
                    's_route_import_error': int,
                    'r_imported_route_changed': int,
                    'r_imported_route_changed_error': int
                }
            }
        }
    }

class ShowIpNhrpStats(ShowIpNhrpStatsSchema):
    """Parser for 'show nhrp stats',
                  'show ip nhrp stats',
                  'show ipv6 nhrp stats',
                  'show nhrp stats {tunnel}',
                  'show ip nhrp stats {tunnel}',
                  'show ipv6 nhrp stats {tunnel}'
    """
    cli_command = ['show nhrp stats','show {ip_type} nhrp stats','show nhrp stats {tunnel}','show {ip_type} nhrp stats {tunnel}']
    def cli(self, tunnel= None, ip_type= None, output=None):
        if output is None:
            if tunnel is None and ip_type is None:
                cmd = self.cli_command[0]
            elif ip_type and tunnel is None:
                cmd = self.cli_command[1].format(ip_type=ip_type)
            elif ip_type is None and tunnel:
                cmd = self.cli_command[2].format(tunnel=tunnel)
            elif tunnel and ip_type:
                cmd = self.cli_command[3].format(ip_type=ip_type,tunnel=tunnel)

            # get output from device
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # Tunnel100
        p1 = re.compile(r'^(?P<interface>[\w\/\.\-\:]+)$')

        # Interface State Event Stats:
        p2 = re.compile('^Interface State Event Stats:$')

        # Tunnel Stats:
        p3 = re.compile('^Tunnel Stats:$')

        # Tunnel Protection Stats:
        p4 = re.compile('^Tunnel Protection Stats:$')

        # Tunnel QoS Stats:
        p5 = re.compile('^Tunnel QoS Stats:$')

        # RIB Events Stats:
        p6 = re.compile('^RIB Events Stats:$')

        # MPLS Stats:
        p7 = re.compile('^MPLS Stats:$')

        # BFD Stats:
        p8 = re.compile('^BFD Stats:$')

        # BGP Stats:
        p9 = re.compile('^BGP Stats:$')

        # [R]UP                         : 2[0]    [R]Down                       : 0[0]
        p10 = re.compile(r'^\[R\]UP +: +(?P<r_up>\d+)\[(?P<r_up_error>\d+)\]\s+'
                         '\[R\]Down +: +(?P<r_down>\d+)\[(?P<r_down_error>\d+)\]$')

        # [R]Deleted                    : 0[0]
        p11 = re.compile(r'^\[R\]Deleted +: +(?P<r_deleted>\d+)\[(?P<r_deleted_error>\d+)\]$')

        # [S]End Point Addition         : 200[0]  [S]End Point Deletion         : 120[0]
        p12 = re.compile(r'^\[S\]End +Point +Addition +: +(?P<s_endpoint_addition>\d+)'
                          '\[(?P<s_endpoint_addition_error>\d+)\]\s+'
                          '\[S\]End +Point +Deletion +: +(?P<s_endpoint_deletion>\d+)'
                          '\[(?P<s_endpoint_deletion_error>\d+)\]$')

        # [S]Create TP socket           : 0[0]    [S]Del TP socket              : 0[0]
        p13 = re.compile(r'^\[S\]Create +TP +socket +: +(?P<s_create_tp_socket>\d+)'
                         '\[(?P<s_create_tp_socket_error>\d+)\]\s+'
                         '\[S\]Del +TP +socket +: +(?P<s_del_tp_socket>\d+)'
                         '\[(?P<s_del_tp_socket_error>\d+)\]$')

        # [S]Create VA                  : 0[0]    [S]Del VA                     : 0[0]
        p14 = re.compile(r'^\[S\]Create +VA +: +(?P<s_create_va>\d+)'
                         '\[(?P<s_create_va_error>\d+)\]\s+'
                         '\[S\]Del +VA +: +(?P<s_del_va>\d+)'
                         '\[(?P<s_del_va_error>\d+)\]$')

        # [S]Reset Socket               : 0[0]
        p15 = re.compile(r'^\[S\]Reset +Socket +: +(?P<s_reset_socket>\d+)'
                         '\[(?P<s_reset_socket_error>\d+)\]$')

        # [S]QoS APPLY                  : 0[0]    [S]QoS Remove                 : 0[0]
        p16 = re.compile(r'^\[S\]QoS +APPLY +: +(?P<s_qos_apply>\d+)'
                         '\[(?P<s_qos_apply_error>\d+)\]\s+'
                         '\[S\]QoS +Remove +: +(?P<s_qos_remove>\d+)'
                         '\[(?P<s_qos_remove_error>\d+)\]$')

        # [S]Add Route                  : 60[0]   [S]Del Route                  : 60[0]
        p17 = re.compile(r'^\[S\]Add +Route +: +(?P<s_add_route>\d+)'
                         '\[(?P<s_add_route_error>\d+)\]\s+'
                         '\[S\]Del +Route +: +(?P<s_del_route>\d+)'
                         '\[(?P<s_del_route_error>\d+)\]$')

        # [S]Add NHO                    : 0[0]    [S]Del NHO                    : 0[0]
        p18 = re.compile(r'^\[S\]Add +NHO +: +(?P<s_add_nho>\d+)'
                         '\[(?P<s_add_nho_error>\d+)\]\s+'
                         '\[S\]Del +NHO +: +(?P<s_del_nho>\d+)'
                         '\[(?P<s_del_nho_error>\d+)\]$')

        # [S]Rwatch w/o route           : 0[0]    [R]Route Evicted              : 0[0]
        p19 = re.compile(r'^\[S\]Rwatch +w\/o +route +: +(?P<s_rwatch_wo_route>\d+)'
                         '\[(?P<s_rwatch_wo_route_error>\d+)\]\s+'
                         '\[R\]Route +Evicted +: +(?P<r_route_evicted>\d+)'
                         '\[(?P<r_route_evicted_error>\d+)\]$')

        # [S]Label Alloc                : 0[0]    [S]Label Release              : 0[0]
        p20 = re.compile(r'^\[S\]Label +Alloc +: +(?P<s_label_alloc>\d+)'
                         '\[(?P<s_label_alloc_error>\d+)\]\s+'
                         '\[S\]Label +Release +: +(?P<s_label_release>\d+)'
                         '\[(?P<s_label_release_error>\d+)\]$')

        # [S]MPLS IP Key Bind           : 0[0]    [S]MPLS VPN Key Bind          : 0[0]
        p21 = re.compile(r'^\[S\]MPLS +IP +Key +Bind +: +(?P<s_mpls_ip_key_bind>\d+)'
                         '\[(?P<s_mpls_ip_key_bind_error>\d+)\]\s+'
                         '\[S\]MPLS +VPN +Key +Bind +: +(?P<s_mpls_vpn_key_bind>\d+)'
                         '\[(?P<s_mpls_vpn_key_bind_error>\d+)\]$')

        # [S]Client Create              : 0[0]    [S]Client Destroy             : 0[0]
        p22 = re.compile(r'^\[S\]Client +Create +: +(?P<s_client_create>\d+)'
                         '\[(?P<s_client_create_error>\d+)\]\s+'
                         '\[S\]Client +Destroy +: +(?P<s_client_destroy>\d+)'
                         '\[(?P<s_client_destroy_error>\d+)\]$')

        # [R]Session Down               : 0[0]    [R]Session Up                 : 0[0]
        p23 = re.compile(r'^\[R\]Session +Down +: +(?P<r_session_down>\d+)'
                         '\[(?P<r_session_down_error>\d+)\]\s+'
                         '\[R\]Session +Up +: +(?P<r_session_up>\d+)'
                         '\[(?P<r_session_up_error>\d+)\]$')

        # [S]Route Export               : 0[0]    [S]Route Withdrawal           : 0[0]
        p24 = re.compile(r'^\[S\]Route +Export +: +(?P<s_route_export>\d+)'
                         '\[(?P<s_route_export_error>\d+)\]\s+'
                         '\[S\]Route +Withdrawal +: +(?P<s_route_withdrawal>\d+)'
                         '\[(?P<s_route_withdrawal_error>\d+)\]$')

        # [S]Route Import               : 0[0]    [R]Imported Route Changed     : 0[0]
        p25 = re.compile(r'^\[S\]Route +Import +: +(?P<s_route_import>\d+)'
                         '\[(?P<s_route_import_error>\d+)\]\s+'
                         '\[R\]Imported +Route +Changed +: +(?P<r_imported_route_changed>\d+)'
                         '\[(?P<r_imported_route_changed_error>\d+)\]$')

        for line in output.splitlines():
            interface_dict = ret_dict.setdefault('interface', {})
            line = line.strip()

            # Tunnel100
            if not tunnel :
                m1 = p1.match(line)
                if m1:
                    group = m1.groupdict()
                    tunnel_int_dict = interface_dict.setdefault(group['interface'], {})
                    continue
            else:
                tunnel_int_dict = interface_dict.setdefault(tunnel, {})

            # Interface State Event Stats:
            m2 = p2.match(line)
            if m2:
                attr_dict = tunnel_int_dict.setdefault('interface_state_event_stats', {})
                continue

            # Tunnel Stats:
            m3 = p3.match(line)
            if m3:
                attr_dict = tunnel_int_dict.setdefault('tunnel_stats', {})
                continue

            # Tunnel Protection Stats:
            m4 = p4.match(line)
            if m4:
                attr_dict = tunnel_int_dict.setdefault('tunnel_protection_stats', {})
                continue

            # Tunnel QoS Stats:
            m5 = p5.match(line)
            if m5:
                attr_dict = tunnel_int_dict.setdefault('tunnel_qos_stats', {})
                continue

            # RIB Events Stats:
            m6 = p6.match(line)
            if m6:
                attr_dict = tunnel_int_dict.setdefault('rib_event_stats', {})
                continue

            # MPLS Stats:
            m7 = p7.match(line)
            if m7:
                attr_dict = tunnel_int_dict.setdefault('mpls_stats', {})
                continue

            # BFD Stats:
            m8 = p8.match(line)
            if m8:
                attr_dict = tunnel_int_dict.setdefault('bfd_stats', {})
                continue

            # BGP Stats:
            m9 = p9.match(line)
            if m9:
                attr_dict = tunnel_int_dict.setdefault('bgp_stats', {})
                continue

            # [R]UP                         : 2[0]    [R]Down                       : 0[0]
            m10 = p10.match(line)
            if m10:
                group = m10.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [R]Deleted                    : 0[0]
            m11 = p11.match(line)
            if m11:
                group = m11.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]End Point Addition         : 200[0]  [S]End Point Deletion         : 120[0]
            m12 = p12.match(line)
            if m12:
                group = m12.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Create TP socket           : 0[0]    [S]Del TP socket              : 0[0]
            m13 = p13.match(line)
            if m13:
                group = m13.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Create VA                  : 0[0]    [S]Del VA                     : 0[0]
            m14 = p14.match(line)
            if m14:
                group = m14.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Reset Socket               : 0[0]
            m15 = p15.match(line)
            if m15:
                group = m15.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]QoS APPLY                  : 0[0]    [S]QoS Remove                 : 0[0]
            m16 = p16.match(line)
            if m16:
                group = m16.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Add Route                  : 60[0]   [S]Del Route                  : 60[0]
            m17 = p17.match(line)
            if m17:
                group = m17.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Add NHO                    : 0[0]    [S]Del NHO                    : 0[0]
            m18 = p18.match(line)
            if m18:
                group = m18.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Rwatch w/o route           : 0[0]    [R]Route Evicted              : 0[0]
            m19 = p19.match(line)
            if m19:
                group = m19.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Label Alloc                : 0[0]    [S]Label Release              : 0[0]
            m20 = p20.match(line)
            if m20:
                group = m20.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]MPLS IP Key Bind           : 0[0]    [S]MPLS VPN Key Bind          : 0[0]
            m21 = p21.match(line)
            if m21:
                group = m21.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Client Create              : 0[0]    [S]Client Destroy             : 0[0]
            m22 = p22.match(line)
            if m22:
                group = m22.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [R]Session Down               : 0[0]    [R]Session Up                 : 0[0]
            m23 = p23.match(line)
            if m23:
                group = m23.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Route Export               : 0[0]    [S]Route Withdrawal           : 0[0]
            m24 = p24.match(line)
            if m24:
                group = m24.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Route Import               : 0[0]    [R]Imported Route Changed     : 0[0]
            m25 = p25.match(line)
            if m25:
                group = m25.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

        return ret_dict

# ==============================================
# Parser for 'show ip nhrp stats detail'
#            'show ip nhrp stats {tunnel} detail'
# ==============================================

class ShowIpNhrpStatsDetailSchema(MetaParser):
    """Schema for show ip nhrp stats detail
                  show ip nhrp stats {tunnel} detail
    """
    schema = {
        'interface': {
            Any(): {
                'interface_state_event_stats': {
                    'r_up': int,
                    'r_up_error': int,
                    'r_down': int,
                    'r_down_error': int,
                    'r_admin_down': int,
                    'r_admin_down_error': int,
                    'r_deleted': int,
                    'r_deleted_error': int,
                    'r_addr_changed': int,
                    'r_addr_changed_error': int,
                    'r_vrf_changed': int,
                    'r_vrf_changed_error': int,
                    'r_packets_received': int,
                    'r_packets_received_error': int
                },
                'tunnel_stats': {
                    's_endpoint_addition': int,
                    's_endpoint_addition_error': int,
                    's_endpoint_deletion': int,
                    's_endpoint_deletion_error': int,
                    'r_o_ep_sb_created': int,
                    'r_o_ep_sb_created_error': int,
                    'r_t_ep_sb_created': int,
                    'r_t_ep_sb_created_error': int,
                    'r_to_ep_deleted': int,
                    'r_to_ep_deleted_error': int,
                    's_pre_delete': int,
                    's_pre_delete_error': int,
                    'r_src_change': int,
                    'r_src_change_error': int,
                    'r_mode_change': int,
                    'r_mode_change_error': int,
                    'r_leave_mode': int,
                    'r_leave_mode_error': int,
                    'r_decap_intercept': int,
                    'r_decap_intercept_error': int,
                    'r_delayed_event_unlink_ep': int,
                    'r_delayed_event_unlink_ep_error': int
                },
                'tunnel_protection_stats': {
                    's_create_tp_socket': int,
                    's_create_tp_socket_error': int,
                    's_del_tp_socket': int,
                    's_del_tp_socket_error': int,
                    's_create_va': int,
                    's_create_va_error': int,
                    's_del_va': int,
                    's_del_va_error': int,
                    'r_up': int,
                    'r_up_error': int,
                    'r_down': int,
                    'r_down_error': int,
                    's_reset_socket': int,
                    's_reset_socket_error': int,
                    'r_process_delayed_event': int,
                    'r_process_delayed_event_error': int,
                    'r_update_delayed_event': int,
                    'r_update_delayed_event_error': int
                },
                'tunnel_qos_stats': {
                    's_qos_apply': int,
                    's_qos_apply_error': int,
                    's_qos_remove': int,
                    's_qos_remove_error': int,
                    'r_qos_polocy_removed': int,
                    'r_qos_polocy_removed_error': int,
                    'r_cli_policy_map_deleted': int,
                    'r_cli_policy_map_deleted_error': int,
                    'r_cli_policy_map_rename': int,
                    'r_cli_policy_map_rename_error': int
                },
                'rib_event_stats': {
                    's_add_route': int,
                    's_add_route_error': int,
                    's_del_route': int,
                    's_del_route_error': int,
                    's_add_nho': int,
                    's_add_nho_error': int,
                    's_del_nho': int,
                    's_del_nho_error': int,
                    's_rwatch_wo_route': int,
                    's_rwatch_wo_route_error': int,
                    's_init_ipdb': int,
                    's_init_ipdb_error': int,
                    's_add_ipdb': int,
                    's_add_ipdb_error': int,
                    's_del_ipdb': int,
                    's_del_ipdb_error': int,
                    's_remove_ipdb': int,
                    's_remove_ipdb_error': int,
                    's_rt_revise': int,
                    's_rt_revise_error': int,
                    'r_redist_callback': int,
                    'r_redist_callback_error': int,
                    'r_route_add_callback': int,
                    'r_route_add_callback_error': int,
                    'r_route_evicted': int,
                    'r_route_evicted_error': int,
                    's_route_query': int,
                    's_route_query_error': int
                },
                'mpls_stats': {
                    's_label_alloc': int,
                    's_label_alloc_error': int,
                    's_label_release': int,
                    's_label_release_error': int,
                    's_mpls_ip_key_bind': int,
                    's_mpls_ip_key_bind_error': int,
                    's_mpls_vpn_key_bind': int,
                    's_mpls_vpn_key_bind_error': int,
                    's_inject_packet': int,
                    's_inject_packet_error': int,
                    'r_nhrp_mpls_mgmt_ch_cb': int,
                    'r_nhrp_mpls_mgmt_ch_cb_error': int,
                    'r_redirect': int,
                    'r_redirect_error': int,
                    's_label_oi_bind': int,
                    's_label_oi_bind_error': int,
                    's_register_mpls': int,
                    's_register_mpls_error': int,
                    's_unregister_mpls': int,
                    's_unregister_mpls_error': int
                },
                'bfd_stats': {
                    's_client_create': int,
                    's_client_create_error': int,
                    's_client_destroy': int,
                    's_client_destroy_error': int,
                    's_session_create': int,
                    's_session_create_error': int,
                    's_session_destroy': int,
                    's_session_destroy_error': int,
                    'r_callback': int,
                    'r_callback_error': int,
                    'r_session_down': int,
                    'r_session_down_error': int,
                    'r_session_up': int,
                    'r_session_up_error': int,
                    'r_session_default': int,
                    'r_session_default_error': int
                },
                'cef_stats': {
                    's_adjacency_used': int,
                    's_adjacency_used_error': int,
                    's_adjacency_mark_stale': int,
                    's_adjacency_mark_stale_error': int
                },
                'bgp_stats': {
                    's_route_export': int,
                    's_route_export_error': int,
                    's_route_withdrawal': int,
                    's_route_withdrawal_error': int,
                    's_route_import': int,
                    's_route_import_error': int,
                    'r_imported_route_changed': int,
                    'r_imported_route_changed_error': int,
                    's_route_marked': int,
                    's_route_marked_error': int,
                    's_route_unmarked': int,
                    's_route_unmarked_error': int,
                    'r_route_change_notification': int,
                    'r_route_change_notification_error': int,
                    'r_exported_route_deleted': int,
                    'r_exported_route_deleted_error': int,
                    'r_withdrawal_all_route': int,
                    'r_withdrawal_all_route_error': int
                },
                'platform_stats': {
                    'r_state_change': int,
                    'r_state_change_error': int,
                    'r_redirect_request': int,
                    'r_redirect_request_error': int,
                    's_enable': int,
                    's_enable_error': int,
                    's_disable': int,
                    's_disable_error': int
                }
            }
        }
    }

class ShowIpNhrpStatsDetail(ShowIpNhrpStatsDetailSchema):
    """Parser for 'show ip nhrp stats detail'
                  'show ip nhrp stats {tunnel} detail'
    """

    cli_command = ['show ip nhrp stats detail', 'show ip nhrp stats {tunnel} detail']
    def cli(self, tunnel=None, output=None):

        if output is None:
            if tunnel:
                cmd = self.cli_command[1].format(tunnel=tunnel)
            else:
                cmd = self.cli_command[0]
            # get output from device
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # Tunnel100
        p1 = re.compile(r'^(?P<interface>[\w\/\.\-\:]+)$')

        # Interface State Event Stats:
        p2 = re.compile('^Interface State Event Stats:$')

        # Tunnel Stats:
        p3 = re.compile('^Tunnel Stats:$')

        # Tunnel Protection Stats:
        p4 = re.compile('^Tunnel Protection Stats:$')

        # Tunnel QoS Stats:
        p5 = re.compile('^Tunnel QoS Stats:$')

        # RIB Events Stats:
        p6 = re.compile('^RIB Events Stats:$')

        # MPLS Stats:
        p7 = re.compile('^MPLS Stats:$')

        # BFD Stats:
        p8 = re.compile('^BFD Stats:$')

        # CEF Stats:
        p9 = re.compile('^CEF Stats:$')

        # BGP Stats:
        p10 = re.compile('^BGP Stats:$')

        # Platform Stats:
        p11 = re.compile('^Platform Stats:$')

        # [R]UP                         : 2[0]    [R]Down                       : 0[0]
        p12 = re.compile(r'^\[R\]UP +: +(?P<r_up>\d+)\[(?P<r_up_error>\d+)\]\s+'
                         r'\[R\]Down +: +(?P<r_down>\d+)\[(?P<r_down_error>\d+)\]$')

        # [R]Admin Down                 : 0[0]    [R]Deleted                    : 0[0]
        p13 = re.compile(r'^\[R\]Admin +Down +: +(?P<r_admin_down>\d+)'
                         '\[(?P<r_admin_down_error>\d+)\]\s+'
                         '\[R\]Deleted +: +(?P<r_deleted>\d+)'
                         '\[(?P<r_deleted_error>\d+)\]$')

        # [R]Addr Changed               : 0[0]    [R]VRF Changed                : 0[0]
        p14 = re.compile(r'^\[R\]Addr +Changed +: +(?P<r_addr_changed>\d+)'
                         '\[(?P<r_addr_changed_error>\d+)\]\s+'
                         '\[R\]VRF +Changed +: +(?P<r_vrf_changed>\d+)'
                         '\[(?P<r_vrf_changed_error>\d+)\]$')

        # [R]Packets received           : 2996[0]
        p15 = re.compile(r'^\[R\]Packets +received +: +(?P<r_packets_received>\d+)'
                         '\[(?P<r_packets_received_error>\d+)\]$')

        # [S]End Point Addition         : 200[0]  [S]End Point Deletion         : 120[0]
        p16 = re.compile(r'^\[S\]End +Point +Addition +: +(?P<s_endpoint_addition>\d+)'
                         '\[(?P<s_endpoint_addition_error>\d+)\]\s+'
                         '\[S\]End +Point +Deletion +: +(?P<s_endpoint_deletion>\d+)'
                         '\[(?P<s_endpoint_deletion_error>\d+)\]$')

        # [R]O EP SB Created            : 0[0]    [R]T EP SB Created
        p17 = re.compile(r'^\[R\]O +EP +SB +Created +: +(?P<r_o_ep_sb_created>\d+)'
                         '\[(?P<r_o_ep_sb_created_error>\d+)\]\s+'
                         '\[R\]T +EP +SB +Created +: +(?P<r_t_ep_sb_created>\d+)'
                         '\[(?P<r_t_ep_sb_created_error>\d+)\]$')

        # [R]T/O EP Deleted             : 0[0]    [S]Pre-Delete
        p18 = re.compile(r'^\[R\]T\/O +EP +Deleted +: +(?P<r_to_ep_deleted>\d+)'
                         '\[(?P<r_to_ep_deleted_error>\d+)\]\s+'
                         '\[S\]Pre-Delete +: +(?P<s_pre_delete>\d+)'
                         '\[(?P<s_pre_delete_error>\d+)\]$')

        # [R]SRC Change                 : 1[0]    [R]Mode Change
        p19 = re.compile(r'^\[R\]SRC +Change +: +(?P<r_src_change>\d+)'
                         '\[(?P<r_src_change_error>\d+)\]\s+'
                         '\[R\]Mode +Change +: +(?P<r_mode_change>\d+)'
                         '\[(?P<r_mode_change_error>\d+)\]$')

        # [R]Leave Mode                 : 2[0]    [R]Decap Intercept
        p20 = re.compile(r'^\[R\]Leave +Mode  +: +(?P<r_leave_mode>\d+)'
                         '\[(?P<r_leave_mode_error>\d+)\]\s+'
                         '\[R\]Decap +Intercept +: +(?P<r_decap_intercept>\d+)'
                         '\[(?P<r_decap_intercept_error>\d+)\]$')

        # [R]Delayed Event Unlink EP
        p21 = re.compile(r'^\[R\]Delayed +Event +Unlink +EP +: +(?P<r_delayed_event_unlink_ep>\d+)'
                         '\[(?P<r_delayed_event_unlink_ep_error>\d+)\]$')

        # [S]Create TP socket           : 0[0]    [S]Del TP socket              : 0[0]
        p22 = re.compile(r'^\[S\]Create +TP +socket +: +(?P<s_create_tp_socket>\d+)'
                         '\[(?P<s_create_tp_socket_error>\d+)\]\s+'
                         '\[S\]Del +TP +socket +: +(?P<s_del_tp_socket>\d+)'
                         '\[(?P<s_del_tp_socket_error>\d+)\]$')

        # [S]Create VA                  : 0[0]    [S]Del VA                     : 0[0]
        p23 = re.compile(r'^\[S\]Create +VA +: +(?P<s_create_va>\d+)'
                         '\[(?P<s_create_va_error>\d+)\]\s+'
                         '\[S\]Del +VA +: +(?P<s_del_va>\d+)'
                         '\[(?P<s_del_va_error>\d+)\]$')

        # [S]Reset Socket               : 0[0]    [R]Process Delayed Event
        p24 = re.compile(r'^\[S\]Reset +Socket +: +(?P<s_reset_socket>\d+)'
                         '\[(?P<s_reset_socket_error>\d+)\]\s+'
                         '\[R\]Process +Delayed +Event +: +(?P<r_process_delayed_event>\d+)'
                         '\[(?P<r_process_delayed_event_error>\d+)\]$')

        # [R]Update Delayed Event       : 0[0]
        p25 = re.compile(r'^\[R\]Update +Delayed +Event +: +(?P<r_update_delayed_event>\d+)'
                         '\[(?P<r_update_delayed_event_error>\d+)\]$')

        # [S]QoS APPLY                  : 0[0]    [S]QoS Remove                 : 0[0]
        p26 = re.compile(r'^\[S\]QoS +APPLY +: +(?P<s_qos_apply>\d+)'
                         '\[(?P<s_qos_apply_error>\d+)\]\s+'
                         '\[S\]QoS +Remove +: +(?P<s_qos_remove>\d+)'
                         '\[(?P<s_qos_remove_error>\d+)\]$')

        # [R]QoS Policy Removed         : 0[0]    [R]CLI-Policy Map Deleted     : 0[0]
        p27 = re.compile(r'^\[R\]QoS +Policy +Removed +: +(?P<r_qos_polocy_removed>\d+)'
                         '\[(?P<r_qos_polocy_removed_error>\d+)\]\s+'
                         '\[R\]CLI-Policy +Map +Deleted +: +(?P<r_cli_policy_map_deleted>\d+)'
                         '\[(?P<r_cli_policy_map_deleted_error>\d+)\]$')

        # [R]CLI-Policy Map Rename
        p28 = re.compile(r'^\[R\]CLI-Policy +Map +Rename +: +(?P<r_cli_policy_map_rename>\d+)'
                         '\[(?P<r_cli_policy_map_rename_error>\d+)\]$')

        # [S]Add Route                  : 60[0]   [S]Del Route                  : 60[0]
        p29 = re.compile(r'^\[S\]Add +Route +: +(?P<s_add_route>\d+)'
                         '\[(?P<s_add_route_error>\d+)\]\s+'
                         '\[S\]Del +Route +: +(?P<s_del_route>\d+)'
                         '\[(?P<s_del_route_error>\d+)\]$')

        # [S]Add NHO                    : 0[0]    [S]Del NHO                    : 0[0]
        p30 = re.compile(r'^\[S\]Add +NHO +: +(?P<s_add_nho>\d+)'
                         '\[(?P<s_add_nho_error>\d+)\]\s+'
                         '\[S\]Del +NHO +: +(?P<s_del_nho>\d+)'
                         '\[(?P<s_del_nho_error>\d+)\]$')

        # [S]Rwatch w/o route           : 0[0]    [S]Init IPDB                  : 0[0]
        p31 = re.compile(r'^\[S\]Rwatch +w\/o +route +: +(?P<s_rwatch_wo_route>\d+)'
                         '\[(?P<s_rwatch_wo_route_error>\d+)\]\s+'
                         '\[S\]Init +IPDB +: +(?P<s_init_ipdb>\d+)'
                         '\[(?P<s_init_ipdb_error>\d+)\]$')

        # [S]Add iPDB                   : 0[0]    [S]Del iPDB                   : 0[0]
        p32 = re.compile(r'^\[S\]Add +iPDB +: +(?P<s_add_ipdb>\d+)'
                         '\[(?P<s_add_ipdb_error>\d+)\]\s+'
                         '\[S\]Del +iPDB +: +(?P<s_del_ipdb>\d+)'
                         '\[(?P<s_del_ipdb_error>\d+)\]$')

        # [S]remove iPDB                : 0[0]    [S]RTrevise                   : 0[0]
        p33 = re.compile(r'^\[S\]remove +iPDB +: +(?P<s_remove_ipdb>\d+)'
                         '\[(?P<s_remove_ipdb_error>\d+)\]\s+'
                         '\[S\]RTrevise +: +(?P<s_rt_revise>\d+)'
                         '\[(?P<s_rt_revise_error>\d+)\]$')

        # [R]Redist Callback            : 0[0]    [R]Route Add Callback         : 0[0]
        p34 = re.compile(r'^\[R\]Redist +Callback +: +(?P<r_redist_callback>\d+)'
                         '\[(?P<r_redist_callback_error>\d+)\]\s+'
                         '\[R\]Route +Add +Callback +: +(?P<r_route_add_callback>\d+)'
                         '\[(?P<r_route_add_callback_error>\d+)\]$')

        # [R]Route Evicted              : 0[0]    [S]Route Query                : 0[0]
        p35 = re.compile(r'^\[R\]Route +Evicted +: +(?P<r_route_evicted>\d+)'
                         '\[(?P<r_route_evicted_error>\d+)\]\s+'
                         '\[S\]Route +Query +: +(?P<s_route_query>\d+)'
                         '\[(?P<s_route_query_error>\d+)\]$')

        # [S]Label Alloc                : 0[0]    [S]Label Release              : 0[0]
        p36 = re.compile(r'^\[S\]Label +Alloc +: +(?P<s_label_alloc>\d+)'
                         '\[(?P<s_label_alloc_error>\d+)\]\s+'
                         '\[S\]Label +Release +: +(?P<s_label_release>\d+)'
                         '\[(?P<s_label_release_error>\d+)\]$')

        # [S]MPLS IP Key Bind           : 0[0]    [S]MPLS VPN Key Bind          : 0[0]
        p37 = re.compile(r'^\[S\]MPLS +IP +Key +Bind +: +(?P<s_mpls_ip_key_bind>\d+)'
                         '\[(?P<s_mpls_ip_key_bind_error>\d+)\]\s+'
                         '\[S\]MPLS +VPN +Key +Bind +: +(?P<s_mpls_vpn_key_bind>\d+)'
                         '\[(?P<s_mpls_vpn_key_bind_error>\d+)\]$')

        # [S]Inject Packet              : 0[0]    [R]NHRP MPLS MGMT CH CB       : 0[0]
        p38 = re.compile(r'^\[S\]Inject +Packet +: +(?P<s_inject_packet>\d+)'
                         '\[(?P<s_inject_packet_error>\d+)\]\s+'
                         '\[R\]NHRP +MPLS +MGMT +CH +CB +: +(?P<r_nhrp_mpls_mgmt_ch_cb>\d+)'
                         '\[(?P<r_nhrp_mpls_mgmt_ch_cb_error>\d+)\]$')

        # [R]Redirect                   : 0[0]    [S]Label-OI Bind              : 0[0]
        p39 = re.compile(r'^\[R\]Redirect +: +(?P<r_redirect>\d+)'
                         '\[(?P<r_redirect_error>\d+)\]\s+'
                         '\[S\]Label-OI Bind +: +(?P<s_label_oi_bind>\d+)'
                         '\[(?P<s_label_oi_bind_error>\d+)\]$')

        # [S]Register MPLS              : 0[0]    [S]Unregister MPLS            : 0[0]
        p40 = re.compile(r'^\[S\]Register +MPLS +: +(?P<s_register_mpls>\d+)'
                         '\[(?P<s_register_mpls_error>\d+)\]\s+'
                         '\[S\]Unregister +MPLS +: +(?P<s_unregister_mpls>\d+)'
                         '\[(?P<s_unregister_mpls_error>\d+)\]$')

        # [S]Client Create              : 0[0]    [S]Client Destroy             : 0[0]
        p41 = re.compile(r'^\[S\]Client +Create +: +(?P<s_client_create>\d+)'
                         '\[(?P<s_client_create_error>\d+)\]\s+'
                         '\[S\]Client +Destroy +: +(?P<s_client_destroy>\d+)'
                         '\[(?P<s_client_destroy_error>\d+)\]$')

        # [S]Session Create             : 0[0]    [S]Session Destroy            : 0[0]
        p42 = re.compile(r'^\[S\]Session +Create +: +(?P<s_session_create>\d+)'
                         '\[(?P<s_session_create_error>\d+)\]\s+'
                         '\[S\]Session +Destroy +: +(?P<s_session_destroy>\d+)'
                         '\[(?P<s_session_destroy_error>\d+)\]$')

        # [R]Callback                   : 0[0]    [R]Session Down               : 0[0]
        p43 = re.compile(r'^\[R\]Callback +: +(?P<r_callback>\d+)'
                         '\[(?P<r_callback_error>\d+)\]\s+'
                         '\[R\]Session +Down +: +(?P<r_session_down>\d+)'
                         '\[(?P<r_session_down_error>\d+)\]$')

        # [R]Session Up                 : 0[0]    [R]Session Default            : 0[0]
        p44 = re.compile(r'^\[R\]Session +Up +: +(?P<r_session_up>\d+)'
                         '\[(?P<r_session_up_error>\d+)\]\s+'
                         '\[R\]Session +Default +: +(?P<r_session_default>\d+)'
                         '\[(?P<r_session_default_error>\d+)\]$')

        # [S]Adjacency Used             : 0[0]    [S]Adjacency Mark Stale       : 180[0]
        p45 = re.compile(r'^\[S\]Adjacency +Used +: +(?P<s_adjacency_used>\d+)'
                         '\[(?P<s_adjacency_used_error>\d+)\]\s+'
                         '\[S\]Adjacency +Mark +Stale +: +(?P<s_adjacency_mark_stale>\d+)'
                         '\[(?P<s_adjacency_mark_stale_error>\d+)\]$')

        # [S]Route Export               : 0[0]    [S]Route Withdrawal           : 0[0]
        p46 = re.compile(r'^\[S\]Route +Export +: +(?P<s_route_export>\d+)'
                         '\[(?P<s_route_export_error>\d+)\]\s+'
                         '\[S\]Route +Withdrawal +: +(?P<s_route_withdrawal>\d+)'
                         '\[(?P<s_route_withdrawal_error>\d+)\]$')

        # [S]Route Import               : 0[0]    [R]Imported Route Changed     : 0[0]
        p47 = re.compile(r'^\[S\]Route +Import +: +(?P<s_route_import>\d+)'
                         '\[(?P<s_route_import_error>\d+)\]\s+'
                         '\[R\]Imported +Route +Changed +: +(?P<r_imported_route_changed>\d+)'
                         '\[(?P<r_imported_route_changed_error>\d+)\]$')

        # [S]Route marked               : 0[0]    [S]Route unmarked             : 0[0]
        p48 = re.compile(r'^\[S\]Route +marked +: +(?P<s_route_marked>\d+)'
                         '\[(?P<s_route_marked_error>\d+)\]\s+'
                         '\[S\]Route +unmarked +: +(?P<s_route_unmarked>\d+)'
                         '\[(?P<s_route_unmarked_error>\d+)\]$')

        # [R]Route change notification  : 0[0]    [R]Exported Route Deleted     : 0[0]
        p49 = re.compile(r'^\[R\]Route +change +notification +: +(?P<r_route_change_notification>\d+)'
                         '\[(?P<r_route_change_notification_error>\d+)\]\s+'
                         '\[R\]Exported +Route +Deleted +: +(?P<r_exported_route_deleted>\d+)'
                         '\[(?P<r_exported_route_deleted_error>\d+)\]$')

        # [R]Withdraw All Routes        : 0[0]
        p50 = re.compile(r'^\[R\]Withdraw +All +Routes +: +(?P<r_withdrawal_all_route>\d+)'
                         '\[(?P<r_withdrawal_all_route_error>\d+)\]$')

        # [R]State Change               : 0[0]    [R]Redirect Request           : 0[0]
        p51 = re.compile(r'^\[R\]State +Change +: +(?P<r_state_change>\d+)'
                         '\[(?P<r_state_change_error>\d+)\]\s+'
                         '\[R\]Redirect +Request +: +(?P<r_redirect_request>\d+)'
                         '\[(?P<r_redirect_request_error>\d+)\]$')

        # [S]Enable                     : 0[0]    [S]Disable                    : 0[0]
        p52 = re.compile(r'^\[S\]Enable +: +(?P<s_enable>\d+)\[(?P<s_enable_error>\d+)\]\s+'
                         r'\[S\]Disable +: +(?P<s_disable>\d+)\[(?P<s_disable_error>\d+)\]$')

        for line in output.splitlines():
            interface_dict = ret_dict.setdefault('interface', {})
            line = line.strip()

            # Tunnel100
            if not tunnel:
                m1 = p1.match(line)
                if m1:
                    group = m1.groupdict()
                    tunnel_int_dict = interface_dict.setdefault(group['interface'], {})
                    continue
            else:
                tunnel_int_dict = interface_dict.setdefault(tunnel, {})

            # Interface State Event Stats:
            m2 = p2.match(line)
            if m2:
                attr_dict = tunnel_int_dict.setdefault('interface_state_event_stats', {})
                continue

            # Tunnel Stats:
            m3 = p3.match(line)
            if m3:
                attr_dict = tunnel_int_dict.setdefault('tunnel_stats', {})
                continue

            # Tunnel Protection Stats:
            m4 = p4.match(line)
            if m4:
                attr_dict = tunnel_int_dict.setdefault('tunnel_protection_stats', {})
                continue

            # Tunnel QoS Stats:
            m5 = p5.match(line)
            if m5:
                attr_dict = tunnel_int_dict.setdefault('tunnel_qos_stats', {})
                continue

            # RIB Events Stats:
            m6 = p6.match(line)
            if m6:
                attr_dict = tunnel_int_dict.setdefault('rib_event_stats', {})
                continue

            # MPLS Stats:
            m7 = p7.match(line)
            if m7:
                attr_dict = tunnel_int_dict.setdefault('mpls_stats', {})
                continue

            # BFD Stats:
            m8 = p8.match(line)
            if m8:
                attr_dict = tunnel_int_dict.setdefault('bfd_stats', {})
                continue

            # CEF Stats:
            m9 = p9.match(line)
            if m9:
                attr_dict = tunnel_int_dict.setdefault('cef_stats', {})
                continue

            # BGP Stats:
            m10 = p10.match(line)
            if m10:
                attr_dict = tunnel_int_dict.setdefault('bgp_stats', {})
                continue

            # Platform Stats:
            m11 = p11.match(line)
            if m11:
                attr_dict = tunnel_int_dict.setdefault('platform_stats', {})
                continue

            # [R]UP                         : 2[0]    [R]Down                       : 0[0]
            m12 = p12.match(line)
            if m12:
                group = m12.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [R]Admin Down                 : 0[0]    [R]Deleted                    : 0[0]
            m13 = p13.match(line)
            if m13:
                group = m13.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [R]Addr Changed               : 0[0]    [R]VRF Changed                : 0[0]
            m14 = p14.match(line)
            if m14:
                group = m14.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [R]Packets received           : 2996[0]
            m15 = p15.match(line)
            if m15:
                group = m15.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]End Point Addition         : 200[0]  [S]End Point Deletion         : 120[0]
            m16 = p16.match(line)
            if m16:
                group = m16.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [R]O EP SB Created            : 0[0]    [R]T EP SB Created
            m17 = p17.match(line)
            if m17:
                group = m17.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [R]T/O EP Deleted             : 0[0]    [S]Pre-Delete
            m18 = p18.match(line)
            if m18:
                group = m18.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [R]SRC Change                 : 1[0]    [R]Mode Change
            m19 = p19.match(line)
            if m19:
                group = m19.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [R]Leave Mode                 : 2[0]    [R]Decap Intercept
            m20 = p20.match(line)
            if m20:
                group = m20.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [R]Delayed Event Unlink EP
            m21 = p21.match(line)
            if m21:
                group = m21.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Create TP socket           : 0[0]    [S]Del TP socket              : 0[0]
            m22 = p22.match(line)
            if m22:
                group = m22.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Create VA                  : 0[0]    [S]Del VA                     : 0[0]
            m23 = p23.match(line)
            if m23:
                group = m23.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Reset Socket               : 0[0]    [R]Process Delayed Event
            m24 = p24.match(line)
            if m24:
                group = m24.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [R]Update Delayed Event       : 0[0]
            m25 = p25.match(line)
            if m25:
                group = m25.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]QoS APPLY                  : 0[0]    [S]QoS Remove                 : 0[0]
            m26 = p26.match(line)
            if m26:
                group = m26.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [R]QoS Policy Removed         : 0[0]    [R]CLI-Policy Map Deleted     : 0[0]
            m27 = p27.match(line)
            if m27:
                group = m27.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [R]CLI-Policy Map Rename
            m28 = p28.match(line)
            if m28:
                group = m28.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Add Route                  : 60[0]   [S]Del Route                  : 60[0]
            m29 = p29.match(line)
            if m29:
                group = m29.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Add NHO                    : 0[0]    [S]Del NHO                    : 0[0]
            m30 = p30.match(line)
            if m30:
                group = m30.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Rwatch w/o route           : 0[0]    [S]Init IPDB                  : 0[0]
            m31 = p31.match(line)
            if m31:
                group = m31.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Add iPDB                   : 0[0]    [S]Del iPDB                   : 0[0]
            m32 = p32.match(line)
            if m32:
                group = m32.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]remove iPDB                : 0[0]    [S]RTrevise                   : 0[0]
            m33 = p33.match(line)
            if m33:
                group = m33.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [R]Redist Callback            : 0[0]    [R]Route Add Callback         : 0[0]
            m34 = p34.match(line)
            if m34:
                group = m34.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [R]Route Evicted              : 0[0]    [S]Route Query                : 0[0]
            m35 = p35.match(line)
            if m35:
                group = m35.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Label Alloc                : 0[0]    [S]Label Release              : 0[0]
            m36 = p36.match(line)
            if m36:
                group = m36.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]MPLS IP Key Bind           : 0[0]    [S]MPLS VPN Key Bind          : 0[0]
            m37 = p37.match(line)
            if m37:
                group = m37.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Inject Packet              : 0[0]    [R]NHRP MPLS MGMT CH CB       : 0[0]
            m38 = p38.match(line)
            if m38:
                group = m38.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [R]Redirect                   : 0[0]    [S]Label-OI Bind              : 0[0]
            m39 = p39.match(line)
            if m39:
                group = m39.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Register MPLS              : 0[0]    [S]Unregister MPLS            : 0[0]
            m40 = p40.match(line)
            if m40:
                group = m40.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Client Create              : 0[0]    [S]Client Destroy             : 0[0]
            m41 = p41.match(line)
            if m41:
                group = m41.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Session Create             : 0[0]    [S]Session Destroy            : 0[0]
            m42 = p42.match(line)
            if m42:
                group = m42.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [R]Callback                   : 0[0]    [R]Session Down               : 0[0]
            m43 = p43.match(line)
            if m43:
                group = m43.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [R]Session Up                 : 0[0]    [R]Session Default            : 0[0]
            m44 = p44.match(line)
            if m44:
                group = m44.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Adjacency Used             : 0[0]    [S]Adjacency Mark Stale       : 180[0]
            m45 = p45.match(line)
            if m45:
                group = m45.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Route Export               : 0[0]    [S]Route Withdrawal           : 0[0]
            m46 = p46.match(line)
            if m46:
                group = m46.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Route Import               : 0[0]    [R]Imported Route Changed     : 0[0]
            m47 = p47.match(line)
            if m47:
                group = m47.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Route marked               : 0[0]    [S]Route unmarked             : 0[0]
            m48 = p48.match(line)
            if m48:
                group = m48.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [R]Route change notification  : 0[0]    [R]Exported Route Deleted     : 0[0]
            m49 = p49.match(line)
            if m49:
                group = m49.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [R]Withdraw All Routes        : 0[0]
            m50 = p50.match(line)
            if m50:
                group = m50.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [R]State Change               : 0[0]    [R]Redirect Request           : 0[0]
            m51 = p51.match(line)
            if m51:
                group = m51.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

            # [S]Enable                     : 0[0]    [S]Disable                    : 0[0]
            m52 = p52.match(line)
            if m52:
                group = m52.groupdict()
                attr_dict.update({k: int(v) for k, v in group.items()})
                continue

        return ret_dict

# ==============================================
# Parser for 'show ip nhrp'
# ==============================================

class ShowIpNhrpSchema(MetaParser):
    """Schema for show ip nhrp
    """
    schema = {
        Any(): {
            'via': {
                Any(): {
                    'tunnel': {
                        'tunnel_name': str,
                        'created': str,
                        'expire': str,
                    },
                    'type': str,
                    'flags': str,
                    'nbma_address': str,
                }
            }
        }
    }

class ShowIpNhrp(ShowIpNhrpSchema):
    """Parser for 'show ip nhrp'
    """

    cli_command = ['show ip nhrp']
    def cli(self, output=None):

        cmd = self.cli_command[0]

        if output is None:
            # get output from device
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # Matching patterns
        # 22.1.1.0/24 via 100.0.0.1
        p1 = re.compile(r'^(?P<target_network>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}) +'
                        'via +(?P<next_hop>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$')

        # Matching patterns
        # Tunnel100 created 00:00:13, expire 00:02:46
        p2 = re.compile(r'^(?P<tunnel>\S+) +'
                        'created +(?P<created>(\d+\w)+|never|[0-9\:]+), +'
                        '[expire ]*(?P<expire>(\d+\w)+|[0-9\:]+|never expire)$')

        # Matching patterns
        # Type: dynamic, Flags: router rib
        p3 = re.compile(r'^Type: +(?P<type>\S+), +'
                        'Flags: *(?P<flags>(.*))$')

        # Matching patterns
        # NBMA address: 101.1.1.1
        p4 = re.compile(r'^NBMA address: +(?P<nbma_address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$')

        for line in output.splitlines():
            line = line.strip()

            # 22.1.1.0/24 via 100.0.0.1
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                network_dict = ret_dict.setdefault(group['target_network'], {}).\
                                   setdefault('via', {}).\
                                   setdefault(group['next_hop'], {})
                continue

            # Tunnel100 created 00:00:13, expire 00:02:46
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                tunnel_dict = network_dict.setdefault('tunnel', {})
                tunnel_dict.update({
                    'tunnel_name': group['tunnel'],
                    'created': group['created'],
                    'expire': group['expire']
                })
                continue

            # Type: dynamic, Flags: router rib
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                network_dict.update({
                    'type': group['type'],
                    'flags': group['flags']
                })
                continue

            # NBMA address: 101.1.1.1
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                network_dict.update({
                    'nbma_address': group['nbma_address'],
                })
        return ret_dict


# ==============================================
# Parser for 'show ip nhrp detail'
# ==============================================

class ShowIpNhrpDetailSchema(MetaParser):
    """Schema for show ip nhrp detail
    """
    schema = {
        Any(): {
            'via': {
                Any(): {
                    'tunnel': {
                        'tunnel_name': str,
                        'created': str,
                        'expire': str,
                    },
                    'type': str,
                    'flags': str,
                    'nbma_address': str,
                    'preference': int,
                    Optional('requester'): str,
                    Optional('request_id'): str,
                }
            }
        }
    }


class ShowIpNhrpDetail(ShowIpNhrpDetailSchema):
    """Parser for 'show ip nhrp detail'
    """

    cli_command = ['show ip nhrp detail']
    def cli(self, output=None):

        cmd = self.cli_command[0]

        if output is None:
            # get output from device
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # 22.1.1.0/24 via 100.0.0.1
        p1 = re.compile(r'^(?P<target_network>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}) +'
                        'via +(?P<next_hop>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$')

        # Tunnel100 created 00:00:13, expire 00:02:46
        p2 = re.compile(r'^(?P<tunnel>\S+) +'
                        'created +(?P<created>(\d+\w)+|never|[0-9\:]+), +'
                        '[expire ]*(?P<expire>(\d+\w)+|[0-9\:]+|never expire)$')

        # Type: dynamic, Flags: router rib
        p3 = re.compile(r'^Type: +(?P<type>\S+), +'
                        'Flags: *(?P<flags>(.*))$')

        # NBMA address: 101.1.1.1
        p4 = re.compile(r'^NBMA address: +(?P<nbma_address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$')

        # Preference: 255
        p5 = re.compile(r'^Preference: +(?P<preference>\d+)$')

        # Requester: 100.0.0.1 Request ID: 9
        p6 = re.compile(r'^Requester: +(?P<requester>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) +'
                        'Request +ID: +(?P<request_id>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # 22.1.1.0/24 via 100.0.0.1
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                network_dict = ret_dict.setdefault(group['target_network'], {}).\
                                   setdefault('via', {}).\
                                   setdefault(group['next_hop'], {})
                continue

            # Tunnel100 created 00:00:13, expire 00:02:46
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                tunnel_dict = network_dict.setdefault('tunnel', {})
                tunnel_dict.update({
                    'tunnel_name': group['tunnel'],
                    'created': group['created'],
                    'expire': group['expire']
                })
                continue

            # Type: dynamic, Flags: router rib
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                network_dict.update({
                    'type': group['type'],
                    'flags': group['flags']
                })
                continue

            # NBMA address: 101.1.1.1
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                network_dict.update({
                    'nbma_address': group['nbma_address'],
                })
                continue

            # Preference: 255
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                network_dict.update({
                    'preference': int(group['preference'])
                })
                continue

            # Requester: 100.0.0.1 Request ID: 9
            m6 = p6.match(line)
            if m6:
                group = m6.groupdict()
                network_dict.update({
                    'requester': group['requester'],
                    'request_id': group['request_id']
                })
        return ret_dict

# ============================================================
# Parser for 'show ip nhrp nhs'
#            'show ip nhrp nhs {tunnel}'
# ============================================================

class ShowIpNhrpNhsSchema(MetaParser):
    """Schema for show ip nhrp nhs
                  show ip nhrp nhs {tunnel}
    """
    schema = {
        Any(): {
            'nhs_ip': {
                Any(): {
                    'nbma_address': str,
                    'priority': int,
                    'cluster': int,
                    'nhs_state': str
                }
            }
        }
    }

class ShowIpNhrpNhs(ShowIpNhrpNhsSchema):
    """Schema for show ip nhrp nhs
                  show ip nhrp nhs {tunnel}
    """

    cli_command = ['show ip nhrp nhs',
                   'show ip nhrp nhs {tunnel}']
    def cli(self, tunnel=None, output=None):

        if tunnel:
            cmd = self.cli_command[1].format(tunnel=tunnel)
        else:
            cmd = self.cli_command[0]

        if output is None:
            # get output from device
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # Tunnel100:
        p1 = re.compile(r'^(?P<interface>[\w\/\.\-]+):$')

        # 100.0.0.100  RE  NBMA Address: 101.1.1.1 priority = 0 cluster = 0
        p2 = re.compile(r'^(?P<nhs_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                        r'(?P<nhs_state>[E|R|W|D]+)\s+'
                        r'NBMA Address:\s+(?P<nbma_address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                        r'priority\s+=\s+(?P<priority>\d+)\s+cluster\s+=\s+(?P<cluster>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Tunnel100:
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                tunnel_dict = ret_dict.setdefault(group['interface'], {})
                continue

            # 100.0.0.100  RE  NBMA Address: 101.1.1.1 priority = 0 cluster = 0
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                attr_tunnel_dict = tunnel_dict.setdefault('nhs_ip', {}).\
                    setdefault(group['nhs_ip'], {})
                attr_tunnel_dict.update({
                    'nhs_state': group['nhs_state'],
                    'nbma_address': group['nbma_address'],
                    'priority': int(group['priority']),
                    'cluster': int(group['cluster'])
                })
                continue

        return ret_dict

# ============================================================
# Parser for 'show ip nhrp nhs detail'
#            'show ip nhrp nhs {tunnel} detail'
# ============================================================

class ShowIpNhrpNhsDetailSchema(MetaParser):
    """Schema for show ip nhrp nhs detail
                  show ip nhrp nhs {tunnel} detail
    """
    schema = {
        Any(): {
            'nhs_ip': {
                Any(): {
                    Optional('nbma_address'): str,
                    'priority': int,
                    'cluster': int,
                    'nhs_state': str,
                    'req_sent': int,
                    'req_failed': int,
                    'reply_recv': int,
                    Optional('receive_time'): str,
                    Optional('ack'): int,
                    Optional('current_request_id'): int,
                    Optional('protection_socket_requested'): str
                }
            }
        },
        Optional('pending_registration_requests'): {
            Optional('req_id'): {
                Any(): {
                    Optional('ret'): int,
                    Optional('nhs_ip'): str,
                    Optional('nhs_state'): str,
                    Optional('tunnel'): str
                }
            }
        }
    }

class ShowIpNhrpNhsDetail(ShowIpNhrpNhsDetailSchema):
    """Schema for show ip nhrp nhs detail
                  show ip nhrp nhs {tunnel} detail
    """

    cli_command = ['show ip nhrp nhs detail',
                   'show ip nhrp nhs {tunnel} detail']
    def cli(self, tunnel=None, output=None):

        if tunnel:
            cmd = self.cli_command[1].format(tunnel=tunnel)
        else:
            cmd = self.cli_command[0]

        if output is None:
            # get output from device
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # Tunnel100:
        p1 = re.compile(r'^(?P<interface>[\w\/\.\-]+):$')

        # Pending Registration Requests:
        p2 = re.compile('^Pending Registration Requests:$')

        # 100.0.0.100  RE  NBMA Address: 101.1.1.1 priority = 0 cluster = 0 \
        # req-sent 5685  req-failed 0  repl-recv 5675

        #10.0.0.1 RE priority = 0 cluster = 0 req-sent 34560 req-failed 0 repl-recv 26580 (00:03:14 ago)
        p3 = re.compile(r'^(?P<nhs_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                        r'(?P<nhs_state>[E|R|W|D]+)\s+'
                        r'(NBMA Address:\s+(?P<nbma_address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+)?'
                        r'priority\s+=\s+(?P<priority>\d+)\s+cluster\s+=\s+(?P<cluster>\d+)\s+'
                        r'req-sent\s+(?P<req_sent>\d+)\s+req-failed\s+(?P<req_failed>\d+)\s+'
                        r'repl-recv\s+(?P<reply_recv>\d+)$')

        # 100.0.0.100  RE  NBMA Address: 101.1.1.1 priority = 0 cluster = 0 \
        # req-sent 5685  req-failed 0  repl-recv 5675 (00:00:21 ago)

        #10.0.0.1 RE priority = 0 cluster = 0 req-sent 34560 req-failed 0 repl-recv 26580 (00:03:14 ago)
        p4 = re.compile(r'^(?P<nhs_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                        r'(?P<nhs_state>[E|R|W|D]+)\s+'
                        r'(NBMA Address:\s+(?P<nbma_address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+)?'
                        r'priority\s+=\s+(?P<priority>\d+)\s+cluster\s+=\s+(?P<cluster>\d+)\s+'
                        r'req-sent\s+(?P<req_sent>\d+)\s+req-failed\s+(?P<req_failed>\d+)\s+'
                        r'repl-recv\s+(?P<reply_recv>\d+)\s+'
                        r'\((?P<receive_time>\d{1,2}:\d{2}:\d{2})\s+\w+\)$')

        # Current Request ID: 11167
        p5 = re.compile(r'^Current +Request +ID:\s+(?P<current_request_id>\d+)$')

        # Current Request ID: 11167 (Ack: 11167)
        p6 = re.compile(r'^Current +Request +ID:\s+(?P<current_request_id>\d+)\s+'
                        r'\(Ack:\s+(?P<ack>\d+)\)$')

        # Protection Socket Requested: FALSE
        p7 = re.compile(r'^Protection +Socket +Requested:\s+'
                        r'(?P<protection_socket_requested>\w+)$')

        # Registration Request: Reqid 184, Ret 64  NHS 111.0.0.100 expired (Tu111)
        p8 = re.compile(r'^Registration +Request:\s+'
                        r'Reqid +(?P<req_id>\d+), +Ret +(?P<ret>\d+)\s+'
                        r'NHS +(?P<nhs_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                        r'(?P<nhs_state>\w+)\s+\((?P<tunnel>[\w\/\.\-]+)\)$')

        # Registration Request: Reqid 184, Ret 64  NHS 111.0.0.100 expired
        p9 = re.compile(r'^Registration +Request:\s+'
                        r'Reqid +(?P<req_id>\d+), +Ret +(?P<ret>\d+)\s+'
                        r'NHS +(?P<nhs_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                        r'(?P<nhs_state>\w+)$')

        for line in output.splitlines():
            line = line.strip()

            # Tunnel100:
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                tunnel_dict = ret_dict.setdefault(group['interface'], {})
                continue

            # Pending Registration Requests:
            m2 = p2.match(line)
            if m2:
                pending_dict = ret_dict.setdefault('pending_registration_requests', {})

            # 100.0.0.100  RE  NBMA Address: 101.1.1.1 priority = 0 cluster = 0 \
            # req-sent 5685  req-failed 0  repl-recv 5675
            #10.0.0.1 RE priority = 0 cluster = 0 req-sent 34560 req-failed 0 repl-recv 26580 (00:03:14 ago)
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                attr_tunnel_dict = tunnel_dict.setdefault('nhs_ip', {}).\
                    setdefault(group['nhs_ip'], {})
                attr_tunnel_dict.update({
                    'nhs_state': group['nhs_state'],
                    'priority': int(group['priority']),
                    'cluster': int(group['cluster']),
                    'req_sent': int(group['req_sent']),
                    'req_failed': int(group['req_failed']),
                    'reply_recv': int(group['reply_recv'])
                })
                if group['nbma_address']:
                    attr_tunnel_dict.update({'nbma_address': group['nbma_address']})
                continue

            # 100.0.0.100  RE  NBMA Address: 101.1.1.1 priority = 0 cluster = 0 \
            # req-sent 5685  req-failed 0  repl-recv 5675 (00:00:21 ago)
            #10.0.0.1 RE priority = 0 cluster = 0 req-sent 34560 req-failed 0 repl-recv 26580 (00:03:14 ago)
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                attr_tunnel_dict = tunnel_dict.setdefault('nhs_ip', {}).\
                    setdefault(group['nhs_ip'], {})
                attr_tunnel_dict.update({
                    'nhs_state': group['nhs_state'],
                    'priority': int(group['priority']),
                    'cluster': int(group['cluster']),
                    'req_sent': int(group['req_sent']),
                    'req_failed': int(group['req_failed']),
                    'reply_recv': int(group['reply_recv']),
                    'receive_time': group['receive_time']
                })
                if group['nbma_address']:
                    attr_tunnel_dict.update({'nbma_address': group['nbma_address']})
                continue

            # Current Request ID: 11167
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                attr_tunnel_dict.update({
                    'current_request_id': int(group['current_request_id'])
                })
                continue

            # Current Request ID: 11167 (Ack: 11167)
            m6 = p6.match(line)
            if m6:
                group = m6.groupdict()
                attr_tunnel_dict.update({
                    'current_request_id': int(group['current_request_id']),
                    'ack': int(group['ack'])
                })
                continue

            # Protection Socket Requested: FALSE
            m7= p7.match(line)
            if m7:
                group = m7.groupdict()
                attr_tunnel_dict.update({
                    'protection_socket_requested': group['protection_socket_requested']
                })
                continue

            # Registration Request: Reqid 184, Ret 64  NHS 111.0.0.100 expired (Tu111)
            m8 = p8.match(line)
            if m8:
                group = m8.groupdict()
                attr_dict = pending_dict.setdefault('req_id', {}).\
                    setdefault(group['req_id'], {})
                attr_dict.update({
                    'ret': int(group['ret']),
                    'nhs_ip': group['nhs_ip'],
                    'nhs_state': group['nhs_state'],
                    'tunnel': group['tunnel']
                })
                continue

            # Registration Request: Reqid 184, Ret 64  NHS 111.0.0.100 expired
            m9 = p9.match(line)
            if m9:
                group = m9.groupdict()
                attr_dict = pending_dict.setdefault('req_id', {}).\
                    setdefault(group['req_id'], {})
                attr_dict.update({
                    'ret': int(group['ret']),
                    'nhs_ip': group['nhs_ip'],
                    'nhs_state': group['nhs_state'],
                })
                continue

        return ret_dict

# ==============================================
# Parser for 'show nhrp stats'
#            'show nhrp stats {tunnel}'
# ==============================================
class ShowNhrpStats(ShowIpNhrpStats, ShowIpNhrpStatsSchema):
    """Parser for 'show nhrp stats'
                  'show nhrp stats {tunnel}'
    """

    cli_command = ['show nhrp stats', 'show nhrp stats {tunnel}']
    def cli(self, tunnel=None, output=None):

        if tunnel:
            cmd = self.cli_command[1].format(tunnel=tunnel)
        else:
            cmd = self.cli_command[0]

        if output is None:
            # get output from device
            output = self.device.execute(cmd)
        return super().cli(tunnel=tunnel, output=output)

# ==============================================
# Parser for 'show nhrp stats detail'
#            'show nhrp stats {tunnel} detail'
# ==============================================
class ShowNhrpStatsDetail(ShowIpNhrpStatsDetail, ShowIpNhrpStatsDetailSchema):
    """Parser for 'show nhrp stats detail'
                  'show nhrp stats {tunnel} detail'
    """

    cli_command = ['show nhrp stats detail', 'show nhrp stats {tunnel} detail']
    def cli(self, tunnel=None, output=None):

        if tunnel:
            cmd = self.cli_command[1].format(tunnel=tunnel)
        else:
            cmd = self.cli_command[0]

        if output is None:
            # get output from device
            output = self.device.execute(cmd)
        return super().cli(tunnel=tunnel, output=output)

# ================================================
# Schema for 'show ip dhcp binding | count Active'
# ================================================
class ShowIpDhcpBindingActiveCountSchema(MetaParser):
    """
    Schema for show ip dhcp binding
    """
    schema = {
        Optional('dhcp_binding'): {
            Optional('active_count'): str
        }
    }

class ShowIpDhcpBindingActiveCount(ShowIpDhcpBindingActiveCountSchema):

    ''' Parser for "show ip dhcp binding | count Active"'''
    cli_command = 'show ip dhcp binding | count Active'

    # Defines a function to run the cli_command
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}
        # Number of lines which match regexp = 0
        p1 = re.compile(r'^Number of lines which match regexp = (?P<active_count>(\d+))$')

        # Number of lines which match regexp = 0
        m = p1.match(output)

        parsed_dict.setdefault('dhcp_binding', {})
        if m:
            group = m.groupdict()
            parsed_dict['dhcp_binding']['active_count'] = str(group['active_count'])

        return parsed_dict

# ================================================
# Schema for 'show ip dhcp snooping binding | include Total number of bindings'
# ================================================
class ShowIpDhcpSnoopingBindingTotalNumberSchema(MetaParser):
    """
    Schema for show ip dhcp binding
    """
    schema = {
        'dhcp_snooping_binding': {
            'total_number': int
        }
    }

class ShowIpDhcpSnoopingBindingTotalNumber(ShowIpDhcpSnoopingBindingTotalNumberSchema):

    ''' Parser for "show ip dhcp binding | count Active"'''
    cli_command = 'show ip dhcp snooping binding | include Total number of bindings'

    # Defines a function to run the cli_command
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}
        # Number of lines which match regexp = 0
        p1 = re.compile(r'^Total number of bindings: (?P<total_number>(\d+))$')

        # Number of lines which match regexp = 0
        m = p1.match(output)

        if m:
            group = m.groupdict()
            parsed_dict.setdefault('dhcp_snooping_binding', {})
            parsed_dict['dhcp_snooping_binding']['total_number'] = int(group['total_number'])

        return parsed_dict

# ================================================
# Schema for 'show ip dhcp snooping | include gleaning'
# ================================================
class ShowIpDhcpSnoopingGleaningSchema(MetaParser):
    """
    Schema for show ip dhcp binding
    """
    schema = {
        'dhcp_snooping_gleaning_status': {
            'gleaning_status': str
        }
    }

class ShowIpDhcpSnoopingGleaning(ShowIpDhcpSnoopingGleaningSchema):

    ''' Parser for "show ip dhcp binding | count Active"
    Switch DHCP gleaning is enabled|disabled
    '''
    cli_command = 'show ip dhcp snooping | include gleaning'

    # Defines a function to run the cli_command
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}
        # Number of lines which match regexp = 0
        p1 = re.compile(r'^Switch DHCP gleaning is (?P<gleaning_status>(\S+))$')

        # Number of lines which match regexp = 0
        m = p1.match(output)

        if m:
            group = m.groupdict()
            parsed_dict.setdefault('dhcp_snooping_gleaning_status', {})
            parsed_dict['dhcp_snooping_gleaning_status']['gleaning_status'] = str(group['gleaning_status'])

        return parsed_dict

# =================================================
#  Schema for 'show ip nhrp summary'
# =================================================
class ShowIpNhrpSummarySchema(MetaParser):
    """schema for show ip nhrp summary"""
    schema = {
        'ip_nhrp': {
            "total": {
                'entries': int,
                'size': int,
                'static_entries': int,
                'dynamic_entries': int,
                'incomplete_entries': int
            },
            "remote": {
                'entries': int,
                'static_entries': int,
                'dynamic_entries': int,
                'incomplete_entries': int,
                'nhop': int,
                'bfd': int,
                'default': int,
                'temporary': int,
                'route': {
                    'entries': int,
                    'rib': int,
                    'h_rib': int,
                    'nho_rib': int,
                    'bgp': int
                },
                'lfib': int
            },
            "local": {
                'entries': int,
                'static_entries': int,
                'dynamic_entries': int,
                'incomplete_entries': int,
                'lfib': int
            }
        }
    }

# ===================================================
#  Parser for 'show ip nhrp summary'
# ===================================================
class ShowIpNhrpSummary(ShowIpNhrpSummarySchema):
    """Parser for show ip nhrp summary"""
    cli_command = 'show ip nhrp summary'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # IP NHRP cache 4 entries, 3072 bytes
        p1 = re.compile(r'^IP +NHRP +cache +(?P<nhrp_entries>[\d]+) +entries, +(?P<size>[\d]+) +bytes$')

        # 2 static 2 dynamic 0 incomplete
        p2 = re.compile(r'^(?P<total_static_entries>[\d]+) +static +(?P<total_dynamic_entries>[\d]+) +dynamic +(?P<total_incomplete_entries>[\d]+) +incomplete$')

        # 4 Remote
        p3 = re.compile(r'(?P<remote_entries>[\d]+) Remote$')

        # 1 nhop 3 bfd
        p4 = re.compile(r'(?P<nhop>[\d]+) +nhop +(?P<bfd>[\d]+) +bfd$')

        # 0 default 0 temporary
        p5 = re.compile(r'^(?P<default>[\d]+) +default +(?P<temporary>[\d]+) +temporary$')

        # 2 route
        p6 = re.compile(r'^(?P<total>[\d]+) +route$')

        # 2 rib (2 H 0 nho)
        p7 = re.compile(r'^(?P<rib>[\d]+) +rib +.(?P<h_rib>[\d]+) +H +(?P<nho_rib>[\d]+) +nho.$')

        # 0 bgp
        p8 = re.compile(r'^(?P<bgp>[\d]+) +bgp$')

        # 0 lfib
        p9 = re.compile(r'(?P<lfib>[\d]+) +lfib$')

        # 0 Local
        p10 = re.compile(r'^(?P<local>[\d]+) +Local$')

        # initial return dictionary

        ret_dict = {}

        for line in output.splitlines():
            line=line.strip()

            # IPv6 NHRP cache 4 entries, 3072 bytes
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ip_nhrp = ret_dict.setdefault('ip_nhrp', {})
                target_dict = ip_nhrp.setdefault('total',{})
                target_dict.update({
                    'entries': int(group['nhrp_entries']),
                    'size': int(group['size'])
                })
                continue

            # 2 static 2 dynamic 0 incomplete
            m = p2.match(line)
            if m:
                group = m.groupdict()
                target_dict.update({
                    'static_entries': int(group['total_static_entries']),
                    'dynamic_entries': int(group['total_dynamic_entries']),
                    'incomplete_entries': int(group['total_incomplete_entries'])
                })
                continue

            # 4 Remote
            m = p3.match(line)
            if m:
                group = m.groupdict()
                target_dict = ip_nhrp.setdefault('remote',{})
                target_dict.update({'entries': int(group['remote_entries'])})
                continue

            # 1 nhop 3 bfd
            m = p4.match(line)
            if m:
                group = m.groupdict()
                target_dict.update({'nhop': int(group['nhop']), 'bfd': int(group['bfd'])})
                continue

            # 0 default 0 temporary
            m = p5.match(line)
            if m:
                group = m.groupdict()
                target_dict.update({
                    'default': int(group['default']),
                    'temporary': int(group['temporary'])
                })
                continue

            # 2 route
            m = p6.match(line)
            if m:
                group = m.groupdict()
                route = target_dict.setdefault('route',{})
                route.update({'entries': int(group['total'])})
                continue

            # 2 rib (2 H 0 nho)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                route.update({
                    'rib': int(group['rib']),
                    'h_rib': int(group['h_rib']),
                    'nho_rib': int(group['nho_rib'])
                })
                continue

            # 0 bgp
            m = p8.match(line)
            if m:
                group = m.groupdict()
                route.update({'bgp': int(group['bgp'])})
                continue

            # 0 lfib
            m = p9.match(line)
            if m:
                group = m.groupdict()
                target_dict.update({'lfib': int(group['lfib'])})
                continue

            # 0 Local
            m = p10.match(line)
            if m:
                group = m.groupdict()
                target_dict = ip_nhrp.setdefault('local',{})
                target_dict.update({'entries': int(group['local'])})
                continue

        return ret_dict

# ====================================================
#  schema for show ip cef summary
# ====================================================
class ShowIpCefSummarySchema(MetaParser):
    """Schema for show ip cef summary"""
    schema = {
        'vrf':{
            Any():{
                'prefixes': {
                    'fwd': int,
                    'non_fwd': int,
                    'total_prefix': int
                },
                'table_id': str,
                'epoch': int
            }
        }
    }

# ====================================================
#  parser for show ip cef summary
# ====================================================
class ShowIpCefSummary(ShowIpCefSummarySchema):
    cli_command = 'show ip cef summary'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        # Vrf red
        p1 = re.compile(r'^VRF +(?P<vrf>\S+)$')

        # 4 prefixes (4/0 fwd/non-fwd)
        p2 = re.compile(r'^(?P<total_prefix>\d+) +prefixes +\((?P<fwd>\d+)\/(?P<non_fwd>\d+)+ fwd\/non-fwd\)$')

        # Table id 0x1E000001
        p3 = re.compile(r'^Table id (?P<table_id>\S+)$')

        #Database epoch:        0 (6 entries at this epoch)
        p4 = re.compile(r'^Database epoch: +(?P<epoch>\d+) +\(\d+ entries at this epoch\)$')


        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Vrf red
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                vrf_dict = ret_dict.setdefault('vrf',{}).setdefault(vrf, {})
                continue

            # 4 prefixes (4/0 fwd/non-fwd)
            m = p2.match(line)
            if m:
                prefix_dict = vrf_dict.setdefault('prefixes',{})
                group = m.groupdict()
                group = {k: int(v) for k, v in group.items() if v is not None}
                prefix_dict.update(group)
                continue

            # Table id 0x1E000001
            m = p3.match(line)
            if m:
                vrf_dict.update(m.groupdict())
                continue

            # Database epoch:        0 (6 entries at this epoch)
            m = p4.match(line)
            if m:
              vrf_dict.update({'epoch': int(m.groupdict()['epoch'])})
              continue

        return ret_dict


# =======================================================================
# Parser Schema for 'show ip dns view'
# =======================================================================

class ShowIpDnsViewSchema(MetaParser):

    """Schema for "show ip dns view" """

    schema = {
        "dns_parameters": {
            "vrf_id": {
                Any(): {
                    Optional("dns_lookup"): str,
                    Optional("domain_name"): str,
                    "dns_servers": list,
                }
            }
        }
    }


# ==============================================
# Parser for 'show ip dns view'
# ==============================================


class ShowIpDnsView(ShowIpDnsViewSchema):
    """parser for "show ip dns view" """

    cli_command = "show ip dns view"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # DNS View default vrf 65528 parameters:
        p1 = re.compile(
            r"^DNS+\s+View+\s+default+\s+vrf+\s+(?P<vrf_id>\d+)\s+parameters:+$"
        )

        # DNS View default parameters:
        p2 = re.compile(r"^DNS+\s+View+\s+default+\s+parameters:$")

        # Default domain name: pm9001_201_dhcp.intranet
        p3 = re.compile(r"^Default+\s+domain+\s+name:+\s+(?P<domain_name>\S+)$")

        # Domain lookup is enabled
        p4 = re.compile(r"^Domain+\s+lookup+\s+is+\s+enabled$")

        # Domain name-servers:
        p5 = re.compile(r"^Domain+\s+name-servers:$")

        # 10.10.201.144
        p6 = re.compile(r"^(?P<dns_server>^\d+[.]\d+[.]\d+[.]\d+)$")

        # 10.10.201.144 (vrf 65528)
        p7 = re.compile(
            r"^(?P<dns_server>^\d+[.]\d+[.]\d+[.]\d+)\s+[(]vrf+\s+(?P<vrf_id>\d+)[)]$"
        )

        parsed_dict = {}

        for line in output.splitlines():

            line = line.strip()

            dns_view_dict = parsed_dict.setdefault("dns_parameters", {}).setdefault(
                "vrf_id", {}
            )

            # DNS View default vrf 65528 parameters:
            m1 = p1.match(line)
            if m1:
                groups = m1.groupdict()
                specific_dns = dns_view_dict.setdefault(groups["vrf_id"], {})
                continue

            # DNS View default parameters:
            m2 = p2.match(line)
            if m2:
                specific_dns = dns_view_dict.setdefault("0", {})
                continue

            # Default domain name: pm9001_201_dhcp.intranet
            m3 = p3.match(line)
            if m3:
                groups = m3.groupdict()
                specific_dns.update({"domain_name": groups["domain_name"]})
                continue

            # Domain lookup is enabled
            m4 = p4.match(line)
            if m4:
                specific_dns.update({"dns_lookup": "enabled"})
                continue

            # Domain name-servers:
            m5 = p5.match(line)
            if m5:
                dns_servers = specific_dns.setdefault("dns_servers", [])
                continue

            # 10.10.201.144
            m6 = p6.match(line)
            if m6:
                groups = m6.groupdict()
                dns_servers.append(groups["dns_server"])
                continue
            # 10.10.201.144 (vrf 65528)
            m7 = p7.match(line)
            if m7:
                groups = m7.groupdict()
                dns_servers.append(groups["dns_server"])
                continue

        return parsed_dict


# ======================================================
# Schema for 'show ip admission cache '
# ======================================================

class ShowIpAdmissionCacheSchema(MetaParser):
    """Schema for show ip admission cache"""

    schema = {
        'admission_cache': {
            'total_session': int,
            'init_session': int,
        },
        'auth_proxy_cache': {
            Any(): {
                'client_mac': str,
                'client_ip': str,
                'state': str,
                'method': str,
                Optional('vrf'): str,
            },
        },
    }

# ======================================================
# Parser for 'show ip admission cache '
# ======================================================
class ShowIpAdmissionCache(ShowIpAdmissionCacheSchema):
    """Parser for show ip admission cache"""

    cli_command = 'show ip admission cache'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Total Sessions: 101 Init Sessions: 1
        p1 = re.compile(r"^Total\s+Sessions:\s+(?P<total_session>\d+)\s+Init\s+Sessions:\s+(?P<init_session>\d+)$")
        #  Client Mac 000a.aaaa.0001 Client IP 0.0.0.0 IPv6 , State INIT, Method Webauth
        #  Client Mac 000c.2911.69b9 Client IP 101.1.0.2 IPv6 ::, State AUTHC_FAIL, Method Webauth, VRF Global
        p2 = re.compile(r"^\s+Client\s+Mac\s+(?P<client_mac>\S+)\s+Client\s+IP\s+(?P<client_ip>(\d{1,3}\.){3}\d{1,3})\s+IPv6\s+(::)?,\s+State\s+(?P<state>\w+),\s+Method\s+(?P<method>\w+)(,\s+VRF+\s+(\w+))?$")

        ret_dict = {}

        for line in output.splitlines():

            # Total Sessions: 101 Init Sessions: 1
            match_obj = p1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if 'admission_cache' not in ret_dict:
                    admission_cache = ret_dict.setdefault('admission_cache', {})
                admission_cache['total_session'] = int(dict_val['total_session'])
                admission_cache['init_session'] = int(dict_val['init_session'])
                continue

            #  Client Mac 000a.aaaa.0001 Client IP 0.0.0.0 IPv6 , State INIT, Method Webauth
            match_obj = p2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                client_mac_var = dict_val['client_mac']
                if 'auth_proxy_cache' not in ret_dict:
                    auth_proxy_cache = ret_dict.setdefault('auth_proxy_cache', {})
                if client_mac_var not in ret_dict['auth_proxy_cache']:
                    client_mac_dict = ret_dict['auth_proxy_cache'].setdefault(client_mac_var, {})
                client_mac_dict['client_mac'] = dict_val['client_mac']
                client_mac_dict['client_ip'] = dict_val['client_ip']
                client_mac_dict['state'] = dict_val['state']
                client_mac_dict['method'] = dict_val['method']
                if 'vrf' in ret_dict:
                    client_mac_dict['vrf'] = dict_val['vrf']
                continue


        return ret_dict

# ======================================================
# Schema for 'show ip cef exact-route {source} {destination}'
# ======================================================

class showIpcefExactRouteSchema(MetaParser):
    """ Schema for the commands:
            * show ip cef exact-route {source} {destination}
    """

    schema = {
        "ip_adj": str,
        "ip_addr": str,
        "source": str,
        "destination": str
    }


class ShowIpcefExactRoute(showIpcefExactRouteSchema):
    """
        * show ip cef exact-route
    """

    cli_command = 'show ip cef exact-route {source} {destination}'

    def cli(self, source, destination, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(source=source, destination=destination))

        # 10.1.1.1 -> 20.1.1.1 =>IP adj out of Vlan13, addr 172.27.0.1
        p1 = re.compile(r'^(?P<source>\d+.\d+.\d+.\d+) +-> +(?P<destination>\d+.\d+.\d+.\d+) +=>IP adj +(?P<ip_adj>.*), +addr +(?P<ip_addr>\S+)$')


        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()
            # 10.1.1.1 -> 20.1.1.1 =>IP adj out of Vlan13, addr 172.27.0.1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['source'] = group['source']
                ret_dict['destination'] = group['destination']
                ret_dict['ip_adj'] = group['ip_adj']
                ret_dict['ip_addr'] = group['ip_addr']
                continue

        return ret_dict

class ShowIpIgmpSnoopingDetailSchema(MetaParser):
    """Schema for show ip igmp snooping detail"""
    schema = {
        'igmp_snooping': str,
        'global_pim_snooping': str,
        'igmpv3_snooping': str,
        'report_supression': str,
        'tcn_solicit_query': str,
        'tcn_flood_query_count': int,
        'robustness_variable': int,
        'last_member_query_count': int,
        'last_member_query_interval': int,
        'vlan': {
            Any(): {
                'igmp_snooping': str,
                'pim_snooping': str,
                'igmpv2_immediate_leave': str,
                'explicit_host_tracking': str,
                'multicast_router_learning_mode': str,
                Optional('cgmp_inter_mode'): str,
                'robustness_variable': int,
                'last_member_query_count': int,
                'last_member_query_interval': int,
                'topology_change_state': str,
            },
        }
    }

class ShowIpIgmpSnoopingDetail(ShowIpIgmpSnoopingDetailSchema):
    """Parser for show ip igmp snooping detail"""
    cli_command = 'show ip igmp snooping detail'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Vlan 10:
        p0 = re.compile(r"^Vlan\s+(?P<vlan>\d+):\s*$")

        # IGMP snooping : Enabled
        p1 = re.compile(r"^IGMP\s+snooping\s+:\s+(?P<igmp_snooping>\w+)$")

        # Global PIM Snooping : Disabled
        p2 = re.compile(r"^Global\s+PIM\s+Snooping\s+:\s+(?P<global_pim_snooping>\w+)$")

        # IGMPv3 snooping : Enabled
        p3 = re.compile(r"^IGMPv3\s+snooping\s+:\s+(?P<igmpv3_snooping>\w+)$")

        # Report suppression : Enabled
        p4 = re.compile(r"^Report\s+suppression\s+:\s+(?P<report_supression>\w+)$")

        # TCN solicit query : Disabled
        p5 = re.compile(r"^TCN\s+solicit\s+query\s+:\s+(?P<tcn_solicit_query>\w+)$")

        # TCN flood query count      : 2
        p6 = re.compile(r"^TCN\s+flood\s+query\s+count\s+:\s+(?P<tcn_flood_query_count>\d+)$")

        # Robustness variable : 2
        p7 = re.compile(r"^Robustness\s+variable\s+:\s+(?P<robustness_variable>\d+)$")

        # Last member query count  : 2
        p8 = re.compile(r"^Last\s+member\s+query\s+count\s+:\s+(?P<last_member_query_count>\d+)$")

        # Last member query interval   : 1000
        p9 = re.compile(r"^Last\s+member\s+query\s+interval\s+:\s+(?P<last_member_query_interval>\d+)$")

        # Pim Snooping                        : Disabled
        p10 = re.compile(r"^Pim\s+Snooping\s+:\s+(?P<pim_snooping>\w+)$")

        # IGMPv2 immediate leave              : Disabled
        p11 = re.compile(r"^IGMPv2\s+immediate\s+leave\s+:\s+(?P<igmpv2_immediate_leave>\w+)$")

        # Explicit host tracking              : Enabled
        p12 = re.compile(r"^Explicit\s+host\s+tracking\s+:\s+(?P<explicit_host_tracking>\w+)$")

        # Multicast router learning mode      : pim-dvmrp
        p13 = re.compile(r"^Multicast\s+router\s+learning\s+mode\s+:\s+(?P<multicast_router_learning_mode>\S+)$")

        # CGMP interoperability mode          : IGMP_ONLY
        p14 = re.compile(r"^CGMP\s+interoperability\s+mode\s+:\s+(?P<cgmp_inter_mode>\S+)$")

        # Topology change                     : No
        p15 = re.compile(r"^Topology\s+change\s+:\s+(?P<topology_change_state>\w+)$")

        vlan_dict = ret_dict
        for line in output.splitlines():
            line = line.strip()

            # Vlan 10:
            m = p0.match(line)
            if m:
                vlan_dict = ret_dict.setdefault('vlan', {}).setdefault(m.groupdict()['vlan'], {})

            # IGMP snooping : Enabled
            m = p1.match(line)
            if m:
                vlan_dict.update({
                    "igmp_snooping": m.groupdict()["igmp_snooping"]
                })
                continue

            # Global PIM Snooping : Disabled
            m = p2.match(line)
            if m:
                ret_dict["global_pim_snooping"] = m.groupdict()["global_pim_snooping"]
                continue

            # IGMPv3 snooping : Enabled
            m = p3.match(line)
            if m:
                ret_dict["igmpv3_snooping"] = m.groupdict()["igmpv3_snooping"]
                continue

            # Report suppression : Enabled
            m = p4.match(line)
            if m:
                ret_dict["report_supression"] = m.groupdict()["report_supression"]
                continue

            # TCN solicit query : Disabled
            m = p5.match(line)
            if m:
                ret_dict["tcn_solicit_query"] = m.groupdict()["tcn_solicit_query"]
                continue

            # TCN flood query count      : 2
            m = p6.match(line)
            if m:
                ret_dict["tcn_flood_query_count"] = int(m.groupdict()["tcn_flood_query_count"])
                continue

            # Robustness variable : 2
            m = p7.match(line)
            if m:
                vlan_dict.update({
                    "robustness_variable": int(m.groupdict()["robustness_variable"])
                })
                continue

            # Last member query count  : 2
            m = p8.match(line)
            if m:
                vlan_dict.update({
                    "last_member_query_count": int(m.groupdict()["last_member_query_count"])
                })
                continue

            # Last member query interval   : 1000
            m = p9.match(line)
            if m:
                vlan_dict.update({
                    "last_member_query_interval": int(m.groupdict()["last_member_query_interval"])
                })
                continue

            # Pim Snooping                        : Disabled
            m = p10.match(line)
            if m:
                vlan_dict.update(m.groupdict())
                continue

            # IGMPv2 immediate leave              : Disabled
            m = p11.match(line)
            if m:
                vlan_dict.update(m.groupdict())
                continue

            # Explicit host tracking              : Enabled
            m = p12.match(line)
            if m:
                vlan_dict.update(m.groupdict())
                continue

            # Multicast router learning mode      : pim-dvmrp
            m = p13.match(line)
            if m:
                vlan_dict.update(m.groupdict())
                continue

            # CGMP interoperability mode          : IGMP_ONLY
            m = p14.match(line)
            if m:
                vlan_dict.update(m.groupdict())
                continue

            # Topology change                     : No
            m = p15.match(line)
            if m:
                vlan_dict.update(m.groupdict())
                continue

        return ret_dict

# ======================================================
# Parser for 'show ip verify source'
# ======================================================

class ShowIpVerifySourceSchema(MetaParser):

    """Schema for show ip verify source"""

    schema = {
        'ip_address': {
            Any(): {
                'interface_name': str,
                'filter_type': str,
                'filter_mode': str,
                'vlan':str,
                Optional('mac_address'): str
            },
        },
    }

class ShowIpVerifySource(ShowIpVerifySourceSchema):
    """Parser for show ip verify source"""

    cli_command = ['show ip verify source', 'show ip verify source interface {interface_name}']

    def cli(self, interface_name=None, output=None):
        if output is None:
            if interface_name:
                output = self.device.execute(self.cli_command[1].format(interface_name=interface_name))
            else:
                output = self.device.execute(self.cli_command[0])

        # Gi1/0/3      ip trk       active       40.1.1.24                           10
        # Gi1/0/13   ip-mac       active       10.1.1.101       00:0A:00:0B:00:01  10
        p1 = re.compile(r"^(?P<interface_name>\S+)\s+(?P<filter_type>ip\s?\S+)\s+(?P<filter_mode>\S+)\s+(?P<ip_address>\S+)\s+(?P<mac_address>\S+)?\s+(?P<vlan>[\d,]*)$")

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()
            # Gi1/0/3      ip trk       active       40.1.1.24                           10
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                ip_dict = ret_dict.setdefault('ip_address', {}).setdefault(dict_val['ip_address'], {})
                ip_dict['interface_name'] = dict_val['interface_name']
                ip_dict['filter_type'] = dict_val['filter_type']
                ip_dict['filter_mode'] = dict_val['filter_mode']
                ip_dict['vlan'] = dict_val['vlan']
                if dict_val['mac_address']:
                    ip_dict['mac_address'] = dict_val['mac_address']
                continue

        return ret_dict

# ===================================================
# Schema for 'show ip dhcp excluded-addresses all'
#            'show ip dhcp excluded-addresses vrf {vrf}'
#            'show ip dhcp excluded-addresses pool {pool}'
# ===================================================


class ShowIpDhcpExcludedAddressesSchema(MetaParser):
    """
    Schema for
        show ip dhcp excluded-addresses all
        show ip dhcp excluded-addresses vrf {vrf}
        show ip dhcp excluded-addresses pool {pool}
    """
    schema = {
        Any(): {
            'start_ip': str,
            'end_ip': str,
            'num_of_ip': int,
            Optional('vrf'): Any()
        }
    }


# ===================================================
# Parser for 'show ip dhcp excluded-addresses all'
#            'show ip dhcp excluded-addresses vrf {vrf}'
#            'show ip dhcp excluded-addresses pool {pool}'
# ===================================================


class ShowIpDhcpExcludedAddresses(ShowIpDhcpExcludedAddressesSchema):

    ''' Parser for "show ip dhcp excluded-addresses all"'''
    cli_command = ['show ip dhcp excluded-addresses all',
                   'show ip dhcp excluded-addresses vrf {vrf}',
                   'show ip dhcp excluded-addresses pool {pool}']

    # Defines a function to run the cli_command
    def cli(self, vrf=None, pool=None, output=None):
        if output is None:
            if vrf:
                output = self.device.execute(self.cli_command[1].format(vrf=vrf))
            elif pool:
                output = self.device.execute(self.cli_command[2].format(pool=pool))
            else:
                output = self.device.execute(self.cli_command[0])

        parsed_dict = {}

        # for excluded-addresses list
        var = 1

        # Start IP        End IP          Number of IP's  VRF
        # ================================================================
        # 16.16.16.2      16.16.16.222    221
        # 20.0.0.1        20.0.0.1        1               my-dhcp-test-vrf

        p1 = re.compile(r'^\s*(?P<start_ip>\d+\.\d+\.\d+\.\d+)\s+(?P<end_ip>\d+\.\d+\.\d+\.\d+)\s+(?P<num_of_ip>\d+)(\s+(?P<vrf>\S+))?\s*$')

        for line in output.splitlines():
            line = line.strip()

            # 16.16.16.2      16.16.16.222    221
            # 20.0.0.1        20.0.0.1        1               my-dhcp-test-vrf
            m = p1.match(line)
            if m:
                parsed_dict.setdefault(var, {})
                group = m.groupdict()
                parsed_dict[var]['start_ip'] = group['start_ip']
                parsed_dict[var]['end_ip'] = group['end_ip']
                parsed_dict[var]['num_of_ip'] = int(group['num_of_ip'])
                parsed_dict[var]['vrf'] = group.get('vrf', None)
                var += 1
                continue

        return parsed_dict

class ShowIpIgmpSnoopingVlanSchema(MetaParser):
    """Schema for show ip igmp snooping vlan {vlan}"""
    schema = {
        'igmp_snooping': str,
        'global_pim_snooping': str,
        'igmpv3_snooping': str,
        'report_supression': str,
        'tcn_solicit_query': str,
        'tcn_flood_query_count': int,
        'robustness_variable': int,
        'last_member_query_count': int,
        'last_member_query_interval': int,
        'vlan': {
            Any(): {
                'igmp_snooping': str,
                'pim_snooping': str,
                'igmpv2_immediate_leave': str,
                'explicit_host_tracking': str,
                'multicast_router_learning_mode': str,
                Optional('cgmp_inter_mode'): str,
                'robustness_variable': int,
                'last_member_query_count': int,
                'last_member_query_interval': int,
                Optional('topology_change_state'): str,
            },
        }
    }

class ShowIpIgmpSnoopingVlan(ShowIpIgmpSnoopingVlanSchema):
    """Parser for show ip igmp snooping vlan {vlan}"""
    cli_command = 'show ip igmp snooping vlan {vlan}'

    def cli(self, vlan=None):
        cmd = self.cli_command.format(vlan = vlan)
        output = self.device.execute(cmd)

        ret_dict = {}

        # Vlan 10:
        p0 = re.compile(r"^Vlan\s+(?P<vlan>\d+):\s*$")
        
        # IGMP snooping : Enabled
        p1 = re.compile(r"^IGMP\s+snooping\s+:\s+(?P<igmp_snooping>\w+)$")

        # Global PIM Snooping : Disabled
        p2 = re.compile(r"^Global\s+PIM\s+Snooping\s+:\s+(?P<global_pim_snooping>\w+)$")

        # IGMPv3 snooping : Enabled
        p3 = re.compile(r"^IGMPv3\s+snooping\s+:\s+(?P<igmpv3_snooping>\w+)$")

        # Report suppression : Enabled
        p4 = re.compile(r"^Report\s+suppression\s+:\s+(?P<report_supression>\w+)$")

        # TCN solicit query : Disabled
        p5 = re.compile(r"^TCN\s+solicit\s+query\s+:\s+(?P<tcn_solicit_query>\w+)$")

        # TCN flood query count      : 2
        p6 = re.compile(r"^TCN\s+flood\s+query\s+count\s+:\s+(?P<tcn_flood_query_count>\d+)$")

        # Robustness variable : 2
        p7 = re.compile(r"^Robustness\s+variable\s+:\s+(?P<robustness_variable>\d+)$")

        # Last member query count  : 2
        p8 = re.compile(r"^Last\s+member\s+query\s+count\s+:\s+(?P<last_member_query_count>\d+)$")

        # Last member query interval   : 1000
        p9 = re.compile(r"^Last\s+member\s+query\s+interval\s+:\s+(?P<last_member_query_interval>\d+)$")

        # Pim Snooping                        : Disabled
        p10 = re.compile(r"^Pim\s+Snooping\s+:\s+(?P<pim_snooping>\w+)$")

        # IGMPv2 immediate leave              : Disabled
        p11 = re.compile(r"^IGMPv2\s+immediate\s+leave\s+:\s+(?P<igmpv2_immediate_leave>\w+)$")

        # Explicit host tracking              : Enabled
        p12 = re.compile(r"^Explicit\s+host\s+tracking\s+:\s+(?P<explicit_host_tracking>\w+)$")

        # Multicast router learning mode      : pim-dvmrp
        p13 = re.compile(r"^Multicast\s+router\s+learning\s+mode\s+:\s+(?P<multicast_router_learning_mode>\S+)$")

        # CGMP interoperability mode          : IGMP_ONLY
        p14 = re.compile(r"^CGMP\s+interoperability\s+mode\s+:\s+(?P<cgmp_inter_mode>\S+)$")

        # Topology change                     : No
        p15 = re.compile(r"^Topology\s+change\s+:\s+(?P<topology_change_state>\w+)$")

        vlan_dict = ret_dict
        for line in output.splitlines():
            line = line.strip()

            # Vlan 10:
            m = p0.match(line)
            if m:
                vlan_dict = ret_dict.setdefault('vlan', {}).setdefault(m.groupdict()['vlan'], {})
                continue

            # IGMP snooping : Enabled
            m = p1.match(line)
            if m:
                vlan_dict.update({
                    "igmp_snooping": m.groupdict()["igmp_snooping"]
                })
                continue
            
            # Global PIM Snooping : Disabled
            m = p2.match(line)
            if m:
                ret_dict["global_pim_snooping"] = m.groupdict()["global_pim_snooping"]
                continue

            # IGMPv3 snooping : Enabled
            m = p3.match(line)
            if m:
                ret_dict["igmpv3_snooping"] = m.groupdict()["igmpv3_snooping"]
                continue

            # Report suppression : Enabled
            m = p4.match(line)
            if m:
                ret_dict["report_supression"] = m.groupdict()["report_supression"]
                continue

            # TCN solicit query : Disabled
            m = p5.match(line)
            if m:
                ret_dict["tcn_solicit_query"] = m.groupdict()["tcn_solicit_query"]
                continue

            # TCN flood query count      : 2
            m = p6.match(line)
            if m:
                ret_dict["tcn_flood_query_count"] = int(m.groupdict()["tcn_flood_query_count"])
                continue

            # Robustness variable : 2
            m = p7.match(line)
            if m:
                vlan_dict.update({
                    "robustness_variable": int(m.groupdict()["robustness_variable"])
                })
                continue

            # Last member query count  : 2
            m = p8.match(line)
            if m:
                vlan_dict.update({
                    "last_member_query_count": int(m.groupdict()["last_member_query_count"])
                })
                continue

            # Last member query interval   : 1000
            m = p9.match(line)
            if m:
                vlan_dict.update({
                    "last_member_query_interval": int(m.groupdict()["last_member_query_interval"])
                })
                continue

            # Pim Snooping                        : Disabled
            m = p10.match(line)
            if m:
                vlan_dict.update(m.groupdict())
                continue

            # IGMPv2 immediate leave              : Disabled
            m = p11.match(line)
            if m:
                vlan_dict.update(m.groupdict())
                continue

            # Explicit host tracking              : Enabled
            m = p12.match(line)
            if m:
                vlan_dict.update(m.groupdict())
                continue

            # Multicast router learning mode      : pim-dvmrp
            m = p13.match(line)
            if m:
                vlan_dict.update(m.groupdict())
                continue

            # CGMP interoperability mode          : IGMP_ONLY
            m = p14.match(line)
            if m:
                vlan_dict.update(m.groupdict())
                continue

            # Topology change                     : No
            m = p15.match(line)
            if m:
                vlan_dict.update(m.groupdict())
                continue

        return ret_dict


class ShowIpHttpServerAllSchema(MetaParser):
    """
        Schema for show ip http server all
    """
    schema = {
        Optional('http_server'): {
            'status': str,
            'port': int,
            'supplementary_listener_ports': int,
            'authentication_method': str,
            'auth_retry': int,
            'time_window': int,
            'digest_algorithm': str,
            'access_class': str,
            'ipv4_access_class': str,
            'ipv6_access_class': str,
            Optional('base_path'): str,
            'file_upload_status': str,
            Optional('upload_path'): str,
            Optional('help_root'): str,
            'max_connections_allowed': int,
            'max_secondary_connections': int,
            'idle_timeout': int,
            'life_timeout': int,
            'session_idle_timeout': int,
            'max_requests_allowed': int,
            'linger_timeout': int,
            'active_session_modules': str,
            'application_session_modules': {
                Any(): {
                    'handle': int,
                    'status': str,
                    'secure_status': str,
                    'description': str
                }
            },
            'current_connections': {
                Any(): {
                    'remote_ipaddress_port': str,
                    'in_bytes': int,
                    'out_bytes': int
                }
            },
            'nginx_internal_counters': {
                'pool': int,
                'active_connection': int,
                'pool_available': int,
                'maximum_connection_hit': int
            },
            'statistics': {
                'accepted_connections': int,
                'server_accepts_handled_requests': str,
                'reading': int,
                'writing': int,
                'waiting': int
            },
            'history': {
                'index': {
                    Any(): {
                        'local_ip_address_port': str,
                        'remote_ip_address_port': str,
                        'in_bytes': int,
                        'out_bytes': int,
                        'end_time': str
                    }
                }
            },
            'conn_history_current_pos': int,
            Optional('help_path'): str
        },
        'http_secure_server': {
            Optional('capability'): str,
            'status': str,
            'port': int,
            'ciphersuite': list,
            'tls_version': list,
            'client_authentication': str,
            'piv_authentication': str,
            'piv_authorization': str,
            'trustpoint': str,
            Optional('peer_validation_trustpoint'): str,
            'ecdhe_curve': str,
            'active_session_modules': str
        }
    }


class ShowIpHttpServerAll(ShowIpHttpServerAllSchema):
    """
        Parser for show ip http server all
    """

    cli_command = 'show ip http server all'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        # HTTP server status: Enabled
        p0 = re.compile(r'^HTTP server status: (?P<status>\w+)$')

        # HTTP server port: 80
        p1 = re.compile(r'^HTTP server port: (?P<port>\d+)$')

        # HTTP server active supplementary listener ports: 21111
        p2 = re.compile(r'^HTTP server active supplementary listener ports: (?P<supplementary_listener_ports>\d+)$')

        # HTTP server authentication method: enable
        p3 = re.compile(r'^HTTP server authentication method: (?P<authentication_method>\w+)$')

        # HTTP server auth-retry 0 time-window 0
        p4 = re.compile(r'^HTTP server auth-retry (?P<auth_retry>\d+) time-window (?P<time_window>\d+)$')

        # HTTP server digest algorithm: md5
        p5 = re.compile(r'^HTTP server digest algorithm: (?P<digest_algorithm>\w+)$')

        # HTTP server access class: 0
        p6 = re.compile(r'^HTTP server access class: (?P<access_class>\d+)$')

        # HTTP server IPv4 access class: None
        p7 = re.compile(r'^HTTP server IPv4 access class: (?P<ipv4_access_class>\w+)$')

        # HTTP server IPv6 access class: None
        p8 = re.compile(r'^HTTP server IPv6 access class: (?P<ipv6_access_class>\w+)$')

        # HTTP server base path:
        p9 = re.compile(r'^HTTP server base path: (?P<base_path>\S+)$')

        # HTTP File Upload status: Disabled
        p10 = re.compile(r'^HTTP File Upload status: (?P<file_upload_status>\w+)$')

        # HTTP server upload path:
        p11 = re.compile(r'^HTTP server upload path: (?P<upload_path>\S+)$')

        # HTTP server help root:
        p12 = re.compile(r'^HTTP server help root: (?P<help_root>\w+)$')

        # Maximum number of concurrent server connections allowed: 300
        p13 = re.compile(r'^Maximum number of concurrent server connections allowed: (?P<max_connections_allowed>\d+)$')

        # Maximum number of secondary server connections allowed: 50
        p14 = re.compile(r'^Maximum number of secondary server connections allowed: (?P<max_secondary_connections>\d+)$')

        # Server idle time-out: 180 seconds
        p15 = re.compile(r'^Server idle time-out: (?P<idle_timeout>\d+) seconds$')

        # Server life time-out: 180 seconds
        p16 = re.compile(r'^Server life time-out: (?P<life_timeout>\d+) seconds$')

        # Server session idle time-out: 600 seconds
        p17 = re.compile(r'^Server session idle time-out: (?P<session_idle_timeout>\d+) seconds$')

        # Maximum number of requests allowed on a connection: 25
        p18 = re.compile(r'^Maximum number of requests allowed on a connection: (?P<max_requests_allowed>\d+)$')

        # Server linger time : 60 seconds
        p19 = re.compile(r'^Server linger time : (?P<linger_timeout>\d+) seconds$')

        # HTTP server active session modules: ALL
        p20 = re.compile(r'^HTTP server active session modules: (?P<active_session_modules>\w+)$')

        # HTTP secure server capability: Present
        p21 = re.compile(r'^HTTP secure server capability: (?P<capability>\w+)$')

        # HTTP secure server status: Enabled
        p21_1 = re.compile(r'^HTTP secure server status: (?P<status>\w+)$')

        # HTTP secure server port: 443
        p21_2 = re.compile(r'^HTTP secure server port: (?P<port>\d+)$')

        # HTTP secure server ciphersuite:  rsa-aes-cbc-sha2 rsa-aes-gcm-sha2
        p21_3 = re.compile(r'^HTTP secure server ciphersuite:\s+(?P<ciphersuite>.+)$')
        
        #         dhe-aes-cbc-sha2 dhe-aes-gcm-sha2 ecdhe-rsa-aes-cbc-sha2
        #         ecdhe-rsa-aes-gcm-sha2 ecdhe-ecdsa-aes-gcm-sha2 tls13-aes128-gcm-sha256
        #         tls13-aes256-gcm-sha384 tls13-chacha20-poly1305-sha256
        p21_4 = re.compile(r'^(?P<ciphersuite>(dhe|ecdhe|tls|rsa)[a-z\d\s\-]+)$')
        
        # HTTP secure server TLS version:  TLSv1.3 TLSv1.2
        p21_5 = re.compile(r'^HTTP secure server TLS version:\s+(?P<tls_version>.+)$')

        # HTTP secure server client authentication: Disabled
        p21_6 = re.compile(r'^HTTP secure server client authentication: (?P<client_authentication>\w+)$')

        # HTTP secure server PIV authentication: Disabled
        p21_7 = re.compile(r'^HTTP secure server PIV authentication: (?P<piv_authentication>\w+)$')

        # HTTP secure server PIV authorization only: Disabled
        p21_8 = re.compile(r'^HTTP secure server PIV authorization only: (?P<piv_authorization>\w+)$')

        # HTTP secure server trustpoint: INVALID_TP
        p21_9 = re.compile(r'^HTTP secure server trustpoint:\s+(?P<trustpoint>.+)$')

        # HTTP secure server peer validation trustpoint:
        p21_10 = re.compile(r'^HTTP secure server peer validation trustpoint: (?P<peer_validation_trustpoint>\w+)$')

        # HTTP secure server ECDHE curve: secp256r1
        p21_11 = re.compile(r'^HTTP secure server ECDHE curve: (?P<ecdhe_curve>\w+)$')

        # HTTP secure server active session modules: ALL
        p21_12 = re.compile(r'^HTTP secure server active session modules: (?P<active_session_modules>\w+)$')

        # HTTP server application session modules:
        p22 = re.compile(r'^HTTP server application session modules:$')

        # HTTP_IFS              1      Active   Active         HTTP based IOS File Server
        p22_1 = re.compile(r'^(?P<session_module_name>\S+)\s+(?P<handle>\d+)\s+(?P<status>[A-Za-z]+)\s+(?P<secure_status>[A-Za-z]+)\s+(?P<description>.+)$')

        # HTTP server current connections:
        p23 = re.compile(r'^HTTP server current connections:$')

        # local-ipaddress:port  remote-ipaddress:port  in-bytes  out-bytes
        # 127.0.0.1:21111  127.0.0.1:58764  0  0
        p23_1 = re.compile(r'^(?P<current_connection>\S+)\s+(?P<remote_ipaddress_port>\S+)\s+(?P<in_bytes>\d+)\s+(?P<out_bytes>\d+)$')

        # Nginx Internal Counters:
        p24 = re.compile(r'^Nginx Internal Counters:$')

        # Nginx pool = 915
        p24_1 = re.compile(r'^Nginx pool = (?P<pool>\d+)$')

        # Active connection = 1
        p24_2 = re.compile(r'^Active connection = (?P<active_connection>\d+)$')

        # Nginx pool available = 898
        p24_3 = re.compile(r'^Nginx pool available = (?P<pool_available>\d+)$')

        # Maxmum connection Hit = 0
        p24_4 = re.compile(r'^Maxmum connection Hit = (?P<maximum_connection_hit>\d+)$')

        # HTTP server statistics:
        p25 = re.compile(r'^HTTP server statistics:$')

        # Accepted connections total: 1
        p25_1 = re.compile(r'^Accepted connections total: (?P<accepted_connections>\d+)$')

        # 2 2 2
        p25_2 = re.compile(r'^(?P<server_accepts_handled_requests>[\d\s]+)$')

        # Reading: 0 Writing: 1 Waiting: 0
        p25_3 = re.compile(r'^Reading:\s+(?P<reading>\d+)\s+Writing:\s+(?P<writing>\d+)\s+Waiting:\s+(?P<waiting>\d+)$')

        # HTTP server history:
        p26 = re.compile(r'^HTTP server history:$')

        # local-ipaddress:port  remote-ipaddress:port  in-bytes  out-bytes  end-time
        # 127.0.0.1:21111  127.0.0.1:58764  0  404  11:56:11 17/03
        # 127.0.0.1:21111  127.0.0.1:58778  0  277  11:56:13 17/03
        p26_1 = re.compile(r'^(?P<local_ip_address_port>\S+)\s+(?P<remote_ip_address_port>\S+)\s+(?P<in_bytes>\d+)\s+(?P<out_bytes>\d+)\s+(?P<end_time>.+)$')

        # conn_history_current_pos: 2
        p27 = re.compile(r'^conn_history_current_pos: (?P<conn_history_current_pos>\d+)$')

        # HTTP server help path:
        p28 = re.compile(r'^HTTP server help path: (?P<help_path>\S+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # HTTP server status: Enabled
            m = p0.match(line)
            if m:
                http_server_dict = ret_dict.setdefault('http_server', {})
                http_server_dict['status'] = m.groupdict()['status']
                continue

            # HTTP server port: 80
            m = p1.match(line)
            if m:
                http_server_dict['port'] = int(m.groupdict()['port'])
                continue

            # HTTP server active supplementary listener ports: 21111
            m = p2.match(line)
            if m:
                http_server_dict['supplementary_listener_ports'] = int(m.groupdict()['supplementary_listener_ports'])
                continue

            # HTTP server authentication method: enable
            m = p3.match(line)
            if m:
                http_server_dict['authentication_method'] = m.groupdict()['authentication_method']
                continue

            # HTTP server auth-retry 0 time-window 0
            m = p4.match(line)
            if m:
                http_server_dict['auth_retry'] = int(m.groupdict()['auth_retry'])
                http_server_dict['time_window'] = int(m.groupdict()['time_window'])
                continue

            # HTTP server digest algorithm: md5
            m = p5.match(line)
            if m:
                http_server_dict['digest_algorithm'] = m.groupdict()['digest_algorithm']
                continue

            # HTTP server access class: 0
            m = p6.match(line)
            if m:
                http_server_dict['access_class'] = m.groupdict()['access_class']
                continue

            # HTTP server IPv4 access class: None
            m = p7.match(line)
            if m:
                http_server_dict['ipv4_access_class'] = m.groupdict()['ipv4_access_class']
                continue

            # HTTP server IPv6 access class: None
            m = p8.match(line)
            if m:
                http_server_dict['ipv6_access_class'] = m.groupdict()['ipv6_access_class']
                continue

            # HTTP server base path:
            m = p9.match(line)
            if m:
                http_server_dict['base_path'] = m.groupdict()['base_path']
                continue

            # HTTP File Upload status: Disabled
            m = p10.match(line)
            if m:
                http_server_dict['file_upload_status'] = m.groupdict()['file_upload_status']
                continue

            # HTTP server upload path:
            m = p11.match(line)
            if m:
                http_server_dict['upload_path'] = m.groupdict()['upload_path']
                continue

            # HTTP server help root:
            m = p12.match(line)
            if m:
                http_server_dict['help_root'] = m.groupdict()['help_root']
                continue

            # Maximum number of concurrent server connections allowed: 300
            m = p13.match(line)
            if m:
                http_server_dict['max_connections_allowed'] = int(m.groupdict()['max_connections_allowed'])
                continue

            # Maximum number of secondary server connections allowed: 50
            m = p14.match(line)
            if m:
                http_server_dict['max_secondary_connections'] = int(m.groupdict()['max_secondary_connections'])
                continue

            # Server idle time-out: 180 seconds
            m = p15.match(line)
            if m:
                http_server_dict['idle_timeout'] = int(m.groupdict()['idle_timeout'])
                continue

            # Server life time-out: 180 seconds
            m = p16.match(line)
            if m:
                http_server_dict['life_timeout'] = int(m.groupdict()['life_timeout'])
                continue

            # Server session idle time-out: 600 seconds
            m = p17.match(line)
            if m:
                http_server_dict['session_idle_timeout'] = int(m.groupdict()['session_idle_timeout'])
                continue

            # Maximum number of requests allowed on a connection: 25
            m = p18.match(line)
            if m:
                http_server_dict['max_requests_allowed'] = int(m.groupdict()['max_requests_allowed'])
                continue

            # Server linger time : 60 seconds
            m = p19.match(line)
            if m:
                http_server_dict['linger_timeout'] = int(m.groupdict()['linger_timeout'])
                continue

            # HTTP server active session modules: ALL
            m = p20.match(line)
            if m:
                http_server_dict['active_session_modules'] = m.groupdict()['active_session_modules']
                continue

            # HTTP secure server capability: Present
            m = p21.match(line)
            if m:
                secure_server_dict = ret_dict.setdefault('http_secure_server', {})
                secure_server_dict['capability'] = m.groupdict()['capability']
                continue

            # HTTP secure server status: Enabled
            m = p21_1.match(line)
            if m:
                secure_server_dict = ret_dict.setdefault('http_secure_server', {})
                secure_server_dict['status'] = m.groupdict()['status']
                continue

            # HTTP secure server port: 443
            m = p21_2.match(line)
            if m:
                secure_server_dict['port'] = int(m.groupdict()['port'])
                continue

            # HTTP secure server ciphersuite:  rsa-aes-cbc-sha2 rsa-aes-gcm-sha2
            m = p21_3.match(line)
            if m:
                secure_server_dict['ciphersuite'] = m.groupdict()['ciphersuite'].split()
                continue

            #         dhe-aes-cbc-sha2 dhe-aes-gcm-sha2 ecdhe-rsa-aes-cbc-sha2
            #         ecdhe-rsa-aes-gcm-sha2 ecdhe-ecdsa-aes-gcm-sha2 tls13-aes128-gcm-sha256
            #         tls13-aes256-gcm-sha384 tls13-chacha20-poly1305-sha256
            m = p21_4.match(line)
            if m:
                secure_server_dict['ciphersuite'].extend(m.groupdict()['ciphersuite'].split())
                continue

            # HTTP secure server TLS version:  TLSv1.3 TLSv1.2
            m = p21_5.match(line)
            if m:
                secure_server_dict['tls_version'] = m.groupdict()['tls_version'].split()
                continue

            # HTTP secure server client authentication: Disabled
            m = p21_6.match(line)
            if m:
                secure_server_dict['client_authentication'] = m.groupdict()['client_authentication']
                continue

            # HTTP secure server PIV authentication: Disabled
            m = p21_7.match(line)
            if m:
                secure_server_dict['piv_authentication'] = m.groupdict()['piv_authentication']
                continue

            # HTTP secure server PIV authorization only: Disabled
            m = p21_8.match(line)
            if m:
                secure_server_dict['piv_authorization'] = m.groupdict()['piv_authorization']
                continue

            # HTTP secure server trustpoint: INVALID_TP
            m = p21_9.match(line)
            if m:
                secure_server_dict['trustpoint'] = m.groupdict()['trustpoint']
                continue

            # HTTP secure server peer validation trustpoint:
            m = p21_10.match(line)
            if m:
                secure_server_dict['peer_validation_trustpoint'] = m.groupdict()['peer_validation_trustpoint']
                continue

            # HTTP secure server ECDHE curve: secp256r1
            m = p21_11.match(line)
            if m:
                secure_server_dict['ecdhe_curve'] = m.groupdict()['ecdhe_curve']
                continue

            # HTTP secure server active session modules: ALL
            m = p21_12.match(line)
            if m:
                secure_server_dict['active_session_modules'] = m.groupdict()['active_session_modules']
                continue

            # HTTP server application session modules:
            m = p22.match(line)
            if m:
                application_session_dict = http_server_dict.setdefault('application_session_modules', {})
                continue

            # HTTP_IFS              1      Active   Active         HTTP based IOS File Server
            m = p22_1.match(line)
            if m:
                group_dict = m.groupdict()
                session_module_dict = application_session_dict.setdefault(group_dict['session_module_name'].lower().replace('-', '_'), {})
                session_module_dict['handle'] = int(group_dict['handle'])
                session_module_dict['status'] = group_dict['status']
                session_module_dict['secure_status'] = group_dict['secure_status']
                session_module_dict['description'] = group_dict['description']
                continue

            # HTTP server current connections:
            m = p23.match(line)
            if m:
                current_connections_dict = http_server_dict.setdefault('current_connections', {})
                continue

            # local-ipaddress:port  remote-ipaddress:port  in-bytes  out-bytes
            # 127.0.0.1:21111  127.0.0.1:58764  0  0
            m = p23_1.match(line)
            if m:
                group_dict = m.groupdict()
                current_connection_dict = current_connections_dict.setdefault(group_dict['current_connection'], {})
                current_connection_dict['remote_ipaddress_port'] = group_dict['remote_ipaddress_port']
                current_connection_dict['in_bytes'] = int(group_dict['in_bytes'])
                current_connection_dict['out_bytes'] = int(group_dict['out_bytes'])
                continue

            # Nginx Internal Counters:
            m = p24.match(line)
            if m:
                nginx_counters_dict = http_server_dict.setdefault('nginx_internal_counters', {})
                continue

            # Nginx pool = 915
            m = p24_1.match(line)
            if m:
                nginx_counters_dict['pool'] = int(m.groupdict()['pool'])
                continue

            # Active connection = 1
            m = p24_2.match(line)
            if m:
                nginx_counters_dict['active_connection'] = int(m.groupdict()['active_connection'])
                continue

            # Nginx pool available = 898
            m = p24_3.match(line)
            if m:
                nginx_counters_dict['pool_available'] = int(m.groupdict()['pool_available'])
                continue

            # Maxmum connection Hit = 0
            m = p24_4.match(line)
            if m:
                nginx_counters_dict['maximum_connection_hit'] = int(m.groupdict()['maximum_connection_hit'])
                continue

            # HTTP server statistics:
            m = p25.match(line)
            if m:
                statistics_dict = http_server_dict.setdefault('statistics', {})
                continue

            # Accepted connections total: 1
            m = p25_1.match(line)
            if m:
                statistics_dict['accepted_connections'] = int(m.groupdict()['accepted_connections'])
                continue

            # 2 2 2
            m = p25_2.match(line)
            if m:
                statistics_dict['server_accepts_handled_requests'] = m.groupdict()['server_accepts_handled_requests']
                continue

            # Reading: 0 Writing: 1 Waiting: 0
            m = p25_3.match(line)
            if m:
                statistics_dict['reading'] = int(m.groupdict()['reading'])
                statistics_dict['writing'] = int(m.groupdict()['writing'])
                statistics_dict['waiting'] = int(m.groupdict()['waiting'])
                continue

            # HTTP server history:
            m = p26.match(line)
            if m:
                history_dict = http_server_dict.setdefault('history', {}).setdefault('index', {})
                continue

            # local-ipaddress:port  remote-ipaddress:port  in-bytes  out-bytes  end-time
            # 127.0.0.1:21111  127.0.0.1:58764  0  404  11:56:11 17/03
            # 127.0.0.1:21111  127.0.0.1:58778  0  277  11:56:13 17/03
            m = p26_1.match(line)
            if m:
                group_dict = m.groupdict()
                index = str(len(history_dict))
                each_history_dict = history_dict.setdefault(index, {})
                each_history_dict['local_ip_address_port'] = group_dict['local_ip_address_port']
                each_history_dict['remote_ip_address_port'] = group_dict['remote_ip_address_port']
                each_history_dict['in_bytes'] = int(group_dict['in_bytes'])
                each_history_dict['out_bytes'] = int(group_dict['out_bytes'])
                each_history_dict['end_time'] = group_dict['end_time']
                continue

            # conn_history_current_pos: 2
            m = p27.match(line)
            if m:
                http_server_dict['conn_history_current_pos'] = int(m.groupdict()['conn_history_current_pos'])
                continue

            # HTTP server help path:
            m = p28.match(line)
            if m:
                http_server_dict['help_path'] = m.groupdict()['help_path']
                continue
        
        return ret_dict


class ShowIpHttpServerSecureStatus(ShowIpHttpServerAll):
    """
        Parser for show ip http server secure status
    """

    cli_command = 'show ip http server secure status'

    def cli(self, output=None):
        return super().cli(output=output)

class ShowIpNatTranslationsTotalSchema(MetaParser):
    """ Schema for the commands:
            * show ip nat translations total
            * show ip nat translations vrf {vrf} total
    """
        
    schema = {
        'total_number_of_translations': int
    }
 
class ShowIpNatTranslationsTotal(ShowIpNatTranslationsTotalSchema):
    """
        * show ip nat translations total
        * show ip nat translations vrf {vrf} total
    """

    cli_command = ['show ip nat translations total', 'show ip nat translations vrf {vrf} total']
    def cli(self, vrf='', output=None):        
        cmd = ""
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output        

        # Total number of translations: 0
        p1 = re.compile(r'^\s*Total\s+number\s+of\s+translations:\s+(?P<number_of_translations>\d+)$')
 
        ret_dict = {}
        for line in out.splitlines():
            line = line.strip()


            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                ret_dict['total_number_of_translations'] = int(group['number_of_translations'])
       
        return ret_dict

# ==============================
# Schema for 'show ip name-servers', 'show ip name-servers vrf {vrf}'
# ==============================
class ShowIPNameServerSchema(MetaParser):
    '''
	Schema for:
	show ip name-servers
	show ip name-servers vrf {vrf}
	'''
    schema = {
        'vrf': {
             Any(): ListOf(str),
        },
    }


# ==============================
# Parser for 'show ip name-servers', 'show ip name-servers vrf {vrf}'
# ==============================
class ShowIPNameServer(ShowIPNameServerSchema):
    '''
    Parser for:
    show ip name-servers
    show ip name-servers vrf {vrf}
    '''
    cli_command = ['show ip name-servers',
        'show ip name-servers vrf {vrf}']
            
    def cli(self, vrf = '', output = None):
        if output is None:
            if vrf:
                out = self.device.execute(self.cli_command[1].format(vrf = vrf))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Init vars
        parsed_dict = {}
        # 255.255.255.255 matching ipv4 address
        p1 = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
        # ABCD:1234::1 matching ipv6 address
        p2 = re.compile(r"[a-fA-F\d\:]+")

        if not vrf:
            vrf = 'default'

        for line in out.splitlines():
            line = line.strip()

            # match the line with ipv4 address
            m1 = p1.match(line)      
            # match the line with ipv6 address
            m2 = p2.match(line)      
            if m1 or m2  :     
               ip_flow = parsed_dict.setdefault("vrf", {}).setdefault(
                    (vrf), []
               )
               ip_flow.append(line)
               continue
        return parsed_dict

class ShowIpSocketsSchema(MetaParser):
    """Schema for show ip sockets"""

    schema = {
        'index':{
            Any():{
                Optional('proto'): int,
                Optional('remote'): str,
                Optional('remote_port'): int,
                Optional('local'): str,
                Optional('local_port'): int,
                Optional('in'): int,
                Optional('out'): int,
                Optional('stat'): int,
                Optional('tty'): int,
                Optional('output_if'): Or(str, None)
            }
        }
    }

class ShowIpSockets(ShowIpSocketsSchema):
    """
    show ip sockets
    """

    cli_command = 'show ip sockets'
    
    def cli(self, output=None):
        
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        index = 1

        #Proto        Remote      Port      Local       Port  In Out  Stat TTY OutputIF
        #17           0.0.0.0      0       --any--      2228   0  0    211   0
        p1 = re.compile(r'^(?P<proto>[\d]+)\s+(?P<remote>[\d.]+)\s+(?P<remote_port>\d+)\s+(?P<local>\S+)\s+(?P<local_port>\d+)\s+(?P<in>\d+)\s+(?P<out>\d+)\s+(?P<stat>\d+)\s+(?P<tty>\d+)(\s+(?P<output_if>[\S]+))?$')

        
        for line in output.splitlines(): 
            line = line.strip()
            
            #Proto        Remote      Port      Local       Port  In Out  Stat TTY OutputIF
            #17           0.0.0.0      0       --any--      2228   0  0    211   0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                index_dict = ret_dict.setdefault('index', {}).setdefault(index,{})
                index_dict['proto'] = int(group['proto'])
                index_dict['remote'] = group['remote']
                index_dict['remote_port'] = int(group['remote_port'])
                index_dict['local'] = group['local']
                index_dict['local_port'] = int(group['local_port'])
                index_dict['in'] = int(group['in'])
                index_dict['out'] = int(group['out'])
                index_dict['stat'] = int(group['stat'])
                index_dict['tty'] = int(group['tty'])
                index_dict['output_if'] = group['output_if']
                index += 1
        return ret_dict
