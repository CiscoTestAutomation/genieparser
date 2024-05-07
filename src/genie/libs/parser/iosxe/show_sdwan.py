'''
* 'show sdwan appqoe aoim-statistics'
* 'show sdwan appqoe tcpopt status'
* 'show sdwan appqoe nat-statistics'
* 'show sdwan appqoe rm-resources'
* 'show sdwan appqoe flow all'
* 'show sdwan appqoe status'
* 'show sdwan appqoe service-chain status'
* 'show platform hardware qfp active feature sdwan datapath service-chain stats'
* 'show sdwan policy data-policy-filter'
* 'show sdwan bfd history'
* 'show sdwan bfd sessions'
* 'show sdwan bfd summary'
* 'show sdwan control summary'
* 'show sdwan control connections'
* 'show sdwan control local-properties'
* 'show sdwan ipsec inbound-connections'
* 'show sdwan ipsec outbound-connections'
* 'show sdwan ipsec local-sa <WORD>'
* 'show sdwan omp summary'
* 'show sdwan omp peers'
* 'show sdwan omp tlocs'
* 'show sdwan omp tloc-paths'
* 'show sdwan omp routes'
* 'show sdwan policy ipv6 access-list-associations'
* 'show sdwan policy access-list-associations'
* 'show sdwan policy access-list-counters'
* 'show sdwan policy ipv6 access-list-counters'
* 'show sdwan policy app-route-policy-filter'
* 'show sdwan policy from-vsmart'
* 'show sdwan reboot history'
* 'show sdwan software'
* 'show sdwan system status'
* 'show sdwan version'
* 'show sdwan zonebfwdp sessions'
* 'show sdwan zbfw zonepair-statistics'
* 'show sdwan tunnel sla index 0'
* 'show sdwan system on-demand'
* 'show sdwan system on-demand {remote_system}'
* 'show sdwan appqoe service-controllers'
* 'show sdwan app-fwd cflowd flow-count'
* 'show sdwan app-fwd cflowd statistics'
* 'show sdwan app-fwd dpi flows'
* 'show sdwan app-route sla-class'
* 'show sdwan app-route sla-class name <name>'
* 'show sdwan app-route stats local-color <color>'
* 'show sdwan app-route stats remote-color <color>'
* 'show sdwan app-route stats remote-system-ip <ip>'
* 'show sdwan tunnel sla'
* 'show sdwan tunnel sla index <index>'
* 'show sdwan tunnel sla name <name>'
* 'show sdwan tunnel statistics'
* 'show sdwan tunnel statistics bfd'
* 'show sdwan tunnel statistics fec'
* 'show sdwan tunnel statistics ipsec'
* 'show sdwan tunnel statistics pkt-dup'
* 'show sdwan tunnel statistics table'
* 'show sdwan utd dataplane config'
* 'show sdwan tenant {tenant} omp routes'
* 'show sdwan tenant {tenant} omp peers'
* 'show sdwan tenant-summary'
* 'show platform software sdwan multicast remote-nodes vrf {vrf ID}'
* 'show platform software sdwan multicast replicators vrf {vrf ID}'
* 'show sdwan security-info'
* 'show platform hardware qfp active feature sdwan client interface <interface name>'
* 'show sdwan omp multicast-routes'
* 'show sdwan omp multicast-auto-discover'
* 'show sdwan policy service-path vpn {vpn} interface {interface name} source-ip {source ip} dest-ip {destination ip} protocol {protocol}'
* 'show sdwan policy service-path vpn {vpn} interface {interface name} source-ip {source ip} dest-ip {destination ip} protocol {protocol} {all}'
* 'show sdwan appqoe dreopt statistics'
* 'show sdwan appqoe ad-statistics'
* 'show sdwan appqoe rm-statistics'
* 'show l2vpn sdwan all'
* 'show l2vpn sdwan all'
'''

# Python
import re
# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And, Default, Use, ListOf
import genie.parsergen as pg
from genie.libs.parser.viptela.show_bfd import ShowBfdSessions as ShowBfdSessions_viptela
from genie.libs.parser.viptela.show_bfd import ShowBfdSummary as ShowBfdSummary_viptela
from genie.libs.parser.viptela.show_control import ShowControlConnections as ShowControlConnections_viptela
from genie.libs.parser.viptela.show_control import ShowControlConnectionHistory as ShowControlConnectionHistory_viptela
from genie.libs.parser.viptela.show_control import ShowControlLocalProperties as ShowControlLocalProperties_viptela
from collections import OrderedDict
from genie.libs.parser.viptela.show_omp import ShowOmpSummary as ShowOmpSummary_viptela
from genie.libs.parser.viptela.show_omp import ShowOmpTlocs as ShowOmpTlocs_viptela
from genie.libs.parser.viptela.show_omp import ShowOmpPeers as ShowOmpPeers_viptela
from genie.libs.parser.viptela.show_omp import ShowOmpTlocPath as ShowOmpTlocPath_viptela
from genie.libs.parser.viptela.show_omp import ShowOmpRoutes as ShowOmpRoutes_viptela
from genie.libs.parser.viptela.show_reboot import ShowRebootHistory as ShowRebootHistory_viptela
from genie.libs.parser.viptela.show_software import ShowSoftwaretab as ShowSoftwaretab_viptela
from genie.libs.parser.viptela.show_system import ShowSystemStatus as ShowSystemStatus_viptela
from genie.libs.parser.viptela.show_version import ShowVersion as ShowVersion_viptela


class ShowSdwanAppqoeAoimStatisticsSchema(MetaParser):
    ''' Schema for show sdwan appqoe aoim-statistics'''
    schema = {
        "total_peer_syncs": int,
        "current_peer_syncs_in_progress": int,
        "Needed_peer_resyncs": int,
        "passthrough_connections_dueto_peer_version_mismatch": int,
        "aoim_db_size_in_bytes": int,
        "local_ao_stats":{
            "number_of_aos": int,
            "ao_name":{
                Any():
                {
                    "version" : str,
                    "registered": str
                },
            }
        },
        "peer_stats":{
            "number_of_peers": int,
            "peer_id":{
                Any():{
                    "number_of_peer_aos": int,
                    "ao_name":{
                        Any():
                        {
                            "version" : str,
                            "incompatible": str
                        },
                    }
                },
            }
        }
    }


class ShowSdwanAppqoeAoimStatistics(ShowSdwanAppqoeAoimStatisticsSchema):

    """ Parser for "show sdwan appqoe aoim-statistics" """

    cli_command = "show sdwan appqoe aoim-statistics"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #Total Number Of Peer Syncs      : 2
        p1=re.compile(r'\s*Total Number Of Peer Syncs+\s+\:+\s+(?P<total_peer_syncs>[\d]+)')

        #Current Number Of Peer Syncs in Progress      : 0
        p2=re.compile(r'\s*Current Number Of Peer Syncs in Progress+\s+\:+\s+(?P<current_peer_syncs>[\d]+)')

        #Number Of Peer Re-Syncs Needed      : 0
        p3=re.compile(r'\s*Number Of Peer Re-Syncs Needed+\s+\:+\s+(?P<peer_resyncs>[\d]+)')

        #Total Passthrough Connections Due to Peer Version Mismatch   : 0
        p4=re.compile(r'\s*Total Passthrough Connections Due to Peer Version Mismatch+\s+\:+\s+(?P<passthrough_connections>[\d]+)')

        #AOIM DB Size (Bytes): 4194304
        p5=re.compile(r'\s*AOIM DB Size +\(+Bytes+\)+\:+\s+(?P<aoim_db_size>\d+)')

        #LOCAL AO Statistics
        p6=re.compile(r'\s*LOCAL AO Statistics')

        #Number Of AOs      : 2
        p7=re.compile(r'\s*Number Of AOs +\s+\:+\s+(?P<ao_number>\d+)')

        #AO             Version   Registered
        #AO             Version   InCompatible
        p8=re.compile(r'\s*AO+\s+Version+\s+\w+')

        #SSL             1.2        N
        p9=re.compile(r'\s*(?P<ao_name>\w+)+\s+(?P<ao_version>[\d.]+)+\s+(?P<ao_status>\w+)')

        #PEER Statistics
        p10=re.compile(r'\s*PEER Statistics')

        #Number Of Peers      : 2
        p11=re.compile(r'\s*Number Of Peers+\s+\:+\s+(?P<peer_total>\d+)')

        #Peer ID: 10.220.100.214
        p12=re.compile(r'\s*Peer ID:+\s+(?P<peer_id>[\d.]+)')

        #Peer Num AOs      : 2
        p13=re.compile(r'\s*Peer Num AOs+\s+\:+\s+(?P<peer_ao_num>\d+)')

        parsed_dict={}
        check_flag=0

        for line in out.splitlines():
            m1= p1.match(line)
            if m1:
                #{'total_peer_syncs':'2'}
                groups=m1.groupdict()
                parsed_dict['total_peer_syncs']=int(groups['total_peer_syncs'])

            m2= p2.match(line)
            if m2:
                #{'current_peer_syncs':'0'}
                groups=m2.groupdict()
                parsed_dict['current_peer_syncs_in_progress']=int(groups['current_peer_syncs'])

            m3= p3.match(line)
            if m3:
                #{'peer_resyncs':'0'}
                groups=m3.groupdict()
                parsed_dict['Needed_peer_resyncs']=int(groups['peer_resyncs'])

            m4= p4.match(line)
            if m4:
                #{'passthrough_connections':'0'}
                groups=m4.groupdict()
                parsed_dict['passthrough_connections_dueto_peer_version_mismatch']=int(groups['passthrough_connections'])

            m5= p5.match(line)
            if m5:
                #{'aoim_db_size':'4194304'}
                groups=m5.groupdict()
                parsed_dict['aoim_db_size_in_bytes']=int(groups['aoim_db_size'])

            m6= p6.match(line)
            if m6:
                #LOCAL AO Statistics
                parsed_dict['local_ao_stats']={}
                cur_dict=parsed_dict['local_ao_stats']

            m7=p7.match(line)
            if m7:
                #{'ao_number':'2'}
                groups=m7.groupdict()
                cur_dict['number_of_aos']= int(groups['ao_number'])
                cur_dict['ao_name']={}
                cur_dict=cur_dict['ao_name']

            #AO             Version   Registered
            #AO             Version   InCompatible
            m8=p8.match(line)

            #SSL             1.2        N
            m9=p9.match(line)
            if m9 and not m8:
                #{'ao_name':'SSL','ao_version':'1.2','ao_status':'N'}
                groups=m9.groupdict()
                cur_dict[groups['ao_name']]={}
                cur_dict[groups['ao_name']]['version']=groups['ao_version']
                if check_flag==0:
                    cur_dict[groups['ao_name']]['registered']=groups['ao_status']
                else:
                    cur_dict[groups['ao_name']]['incompatible']=groups['ao_status']

            #PEER Statistics
            m10=p10.match(line)
            if m10:
                parsed_dict['peer_stats'] = {}
                cur_dict=parsed_dict['peer_stats']
                check_flag=1

            m11=p11.match(line)
            if m11:
                #{'peer_total':'2'}
                groups=m11.groupdict()
                cur_dict['number_of_peers']=int(groups['peer_total'])
                cur_dict['peer_id']={}
                cur_dict=cur_dict['peer_id']
                temp_dict=parsed_dict['peer_stats']['peer_id']

            m12=p12.match(line)
            if m12:
                #{'peer_id':'10.220.100.214'}
                groups=m12.groupdict()
                cur_dict=temp_dict
                cur_dict[groups['peer_id']]={}
                cur_dict=cur_dict[groups['peer_id']]


            m13=p13.match(line)
            if m13:
                #{'peer_ao_num':'2'}
                groups=m13.groupdict()
                cur_dict['number_of_peer_aos'] = int(groups['peer_ao_num'])
                cur_dict['ao_name']={}
                cur_dict=cur_dict['ao_name']

        return parsed_dict


class ShowSdwanAppqoeTcpoptStatusSchema(MetaParser):
    ''' Schema for show sdwan appqoe tcpopt status'''
    schema = {
        'status': {
            'tcp_opt_operational_state': str,
            'tcp_proxy_operational_state': str
            }
        }


class ShowSdwanAppqoeTcpoptStatus(ShowSdwanAppqoeTcpoptStatusSchema):

    """ Parser for "show sdwan appqoe tcpopt status" """

    cli_command = "show sdwan appqoe tcpopt status"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # Status
        p1 = re.compile(r'^Status$')

        # TCP OPT Operational State      : RUNNING
        # TCP Proxy Operational State    : RUNNING
        p2 = re.compile(r'^(?P<key>[\s\S]+\w) +: +(?P<value>[\s\S]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Status
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                tcpopt_status_dict = parsed_dict.setdefault('status', {})
                last_dict_ptr = tcpopt_status_dict
                continue

            # TCP OPT Operational State      : RUNNING
            # TCP Proxy Operational State    : RUNNING
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace(' ', '_').lower()
                value = groups['value']
                last_dict_ptr.update({key: value})

        return parsed_dict


class ShowSdwanAppqoeNatStatisticsSchema(MetaParser):
    ''' Schema for show sdwan appqoe nat-statistics'''
    schema = {
        'nat_statistics': {
            'insert_success': int,
            'delete_success': int,
            'duplicate_entries': int,
            'allocation_failures': int,
            'port_alloc_success': int,
            'port_alloc_failures': int,
            'port_free_success': int,
            'port_free_failures': int
        }
    }


class ShowSdwanAppqoeNatStatistics(ShowSdwanAppqoeNatStatisticsSchema):

    """ Parser for "show sdwan appqoe nat-statistics" """

    cli_command = "show sdwan appqoe nat-statistics"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # NAT Statistics
        p1 = re.compile(r'^NAT Statistics$')

        #  Insert Success      : 518181
        #  Delete Success      : 518181
        #  Duplicate Entries   : 5
        #  Allocation Failures : 0
        #  Port Alloc Success  : 0
        #  Port Alloc Failures : 0
        #  Port Free Success   : 0
        #  Port Free Failures  : 0
        p2 = re.compile(r'^(?P<key>[\s\S]+\w) +: +(?P<value>[\d]+)$')

        for line in out.splitlines():
            line = line.strip()

            # NAT Statistics
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                nat_statistics_dict = parsed_dict.setdefault('nat_statistics', {})
                last_dict_ptr = nat_statistics_dict
                continue

            #  Insert Success      : 518181
            #  Delete Success      : 518181
            #  Duplicate Entries   : 5
            #  Allocation Failures : 0
            #  Port Alloc Success  : 0
            #  Port Alloc Failures : 0
            #  Port Free Success   : 0
            #  Port Free Failures  : 0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace(' ', '_').lower()
                try:
                    value = int(groups['value'])
                except ValueError:
                    value = groups['value']
                last_dict_ptr.update({key: value})

        return parsed_dict


class ShowSdwanAppqoeRmResourcesSchema(MetaParser):
    ''' Schema for show sdwan appqoe rm-resources'''
    schema = {
        'rm_resources': {
            'rm_global_resources': {
                'max_services_memory_kb': int,
                'available_system_memory_kb': int,
                'used_services_memory_kb': int,
                'used_services_memory_percentage': int,
                'system_memory_status': str,
                'num_sessions_status': str,
                'overall_htx_health_status': str
                },
            'registered_service_resources': {
                'tcp_resources': {
                    'max_sessions': int,
                    'used_sessions': int,
                    'memory_per_session': int
                    },
                'ssl_resources': {
                    'max_sessions': int,
                    'used_sessions': int,
                    'memory_per_session': int
                    },
                Optional('dre_resources'): {
                    Optional('max_sessions'): int,
                    Optional('used_sessions'): int,
                    Optional('memory_per_session'): int
                    },
                Optional('http_resources'): {
                    Optional('max_sessions'): int,
                    Optional('used_sessions'): int,
                    Optional('memory_per_session'): int
                    }
                }
            }
        }


class ShowSdwanAppqoeRmResources(ShowSdwanAppqoeRmResourcesSchema):

    """ Parser for "show sdwan appqoe rm-resources" """

    cli_command = "show sdwan appqoe rm-resources"

    def cli(self, output=None):

        # if the user does not provide output to the parser
        # we need to get it from the device
        if not output:
            output = self.device.execute(self.cli_command)

        # RM Resources
        p1 = re.compile(r'^RM +Resources$')

        # RM Global Resources :
        p2 = re.compile(r'^RM +Global +Resources +:$')

        # Registered Service Resources :
        p3 = re.compile(r'^Registered +Service +Resources +:$')

        # TCP Resources:
        p4 = re.compile(r'^TCP +Resources:$')

        # SSL Resources:
        p5 = re.compile(r'^SSL +Resources:$')

        
        # Max Services Memory (KB)    : 6434914
        # Available System Memory(KB) : 12869828
        # Used Services Memory (KB)   : 0
        # Used Services Memory (%)    : 0
        # System Memory Status        : GREEN
        # Num sessions Status         : GREEN
        # Overall HTX health Status   : GREEN
        # Max Sessions                : 11000
        # Used Sessions               : 0
        # Memory Per Session          : 128
        p6 = re.compile(r'^(?P<key>[\s\S]+\S) +: +(?P<value>[\S]+)$')

        # DRE Resources:
        p7 = re.compile(r'^DRE +Resources:$')

        # HTTP Resources:
        p8 = re.compile(r'^HTTP +Resources:$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            # RM Resources
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                rm_resources_dict = ret_dict.setdefault('rm_resources', {})
                last_dict_ptr = rm_resources_dict
                continue

            # RM Global Resources :
            m = p2.match(line)
            if m:
                group = m.groupdict()
                rm_global_resources_dict = rm_resources_dict.setdefault('rm_global_resources', {})
                last_dict_ptr = rm_global_resources_dict
                continue

            # Registered Service Resources :
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                registered_service_resources_dict = rm_resources_dict.setdefault('registered_service_resources', {})
                last_dict_ptr = registered_service_resources_dict
                continue

            # TCP Resources:
            m = p4.match(line)
            if m:
                tcp_resources_dict = registered_service_resources_dict.setdefault('tcp_resources', {})
                last_dict_ptr = tcp_resources_dict
                continue

            # SSL Resources:
            m = p5.match(line)
            if m:
                ssl_resources_dict = registered_service_resources_dict.setdefault('ssl_resources', {})
                last_dict_ptr = ssl_resources_dict
                continue

            # DRE Resources:
            m = p7.match(line)
            if m:
                dre_resources_dict = registered_service_resources_dict.setdefault('dre_resources', {})
                last_dict_ptr = dre_resources_dict
                continue

            # HTTP Resources:
            m = p8.match(line)
            if m:
                http_resources_dict = registered_service_resources_dict.setdefault('http_resources', {})
                last_dict_ptr = http_resources_dict
                continue

            # Max Services Memory (KB)    : 6434914
            # Available System Memory(KB) : 12869828
            # Used Services Memory (KB)   : 0
            # Used Services Memory (%)    : 0
            # System Memory Status        : GREEN
            # Num sessions Status         : GREEN
            # Overall HTX health Status   : GREEN
            # Max Sessions                : 11000
            # Used Sessions               : 0
            # Memory Per Session          : 128
            m = p6.match(line)
            if  m:
                groups = m.groupdict()
                key = groups['key'].replace('(KB)', '_kb').replace('(%)', 'percentage').\
                    replace(' ', '_').replace('__', '_').lower()
                try:
                    value = int(groups['value'])
                except ValueError:
                    value = groups['value']
                last_dict_ptr.update({key: value})

        return ret_dict

class ShowSdwanAppqoeFlowAllSchema(MetaParser):
    ''' Schema for show sdwan appqoe flow all'''
    schema = {
        "active_flows": int,
        "vpn": {
            int: {
                "flow_id": {
                    int: {
                        "source_ip": str,
                        "source_port": int,
                        "destination_ip": str,
                        "destination_port": int,
                        "service": str,
                        }
                    },
                }
            },
        }

class ShowSdwanAppqoeFlowAll(ShowSdwanAppqoeFlowAllSchema):

    """ Parser for "show sdwan appqoe flow all" """

    cli_command = "show sdwan appqoe flow all"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}
        # Active Flows: 2139
        p1 = re.compile(r'^(?P<key>[\s\S]+\w):+\s+(?P<value>[\d]+)$')

        # Flow ID      VPN  Source IP:Port        Destination IP:Port   Service
        # 171064589     1    10.34.0.2:53350       10.36.211.203:443    TSU
        p2 = re.compile(
            r'^(?P<flow_id>[\d]+)[\s]+(?P<vpn>[\d]+)[\s]+(?P<source_ip>[\S]+\w)'
            r':(?P<source_port>[\d]+)[\s]+(?P<destination_ip>[\S]+\w)'
            r':(?P<destination_port>[\d]+)[\s]+(?P<service>[\s\S]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Active Flows: 2139
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace(' ', '_').lower()
                value = int(groups['value'])
                parsed_dict.update({key: value})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                vpn_dict = parsed_dict.setdefault(
                            'vpn', {}).setdefault(int(group['vpn']), {})
                flow_id_dict = vpn_dict.setdefault(
                            'flow_id', {}).setdefault(int(group['flow_id']), {})
                keys = ['source_ip', 'source_port', 'destination_ip',
                        'destination_port', 'service']
                for k in keys:
                    try:
                        flow_id_dict[k] = int(group[k])
                    except ValueError:
                        flow_id_dict[k] = group[k]
        return parsed_dict

# =================================================
#  Schema for 'show sdwan appqoe service-controllers'
# =================================================
class ShowSdwanAppqoeServiceControllersSchema(MetaParser):
    """Schema for show sdwan appqoe service-controllers"""
    schema = {
        Optional("service_health_status"): {
            Any(): { # Servvice Types TCP/SSL/DRE/HTTP
                "color": str,
                "percentage": int
            }
        },
        "service_controllers": {
            "lan_ip": {
                str: {
                    "system_ip": {
                        str: {
                            "site_id": int,
                            "sn_lan_ip": str
                        }
                    }
                }
            }
        }
    }

# ===================================================
#  Parser for 'show sdwan appqoe service-controllers'
# ===================================================
class ShowSdwanAppqoeServiceControllers(ShowSdwanAppqoeServiceControllersSchema):
    """Parser for show sdwan appqoe service-controllers"""

    cli_command = 'show sdwan appqoe service-controllers'
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # TCP : Red (0%)
        # SSL : Red (0%)
        # DRE : Green (37%)
        p1 = re.compile(r'^(?P<service>[\s\S]+)\s+:\s+(?P<service_color>[\s\S]+)\s+\((?P<percent>[\d]+)\%\)$')

        # 193.0.2.2        192.168.13.1            105  193.0.2.3
        p2 = re.compile(r'^(?P<lan_ip>[\d\.]+)\s+(?P<system_ip>[\d\.]+)\s+(?P<site_id>[\d]+)\s+(?P<sn_lan_ip>[\d\.]+)$')

        # Initialize Return Dictionary...
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                service = groups['service'].strip().replace('-', '_').replace(' ', '_').replace(':', '').lower()
                color = groups['service_color'].strip().replace('-', '_').replace(' ', '_').replace(':', '').lower()
                percentage = int(groups['percent'].strip().replace('-', '_').replace(' ', '_').replace(':', '').lower())
                svc_type_dict = ret_dict.setdefault('service_health_status', {}).setdefault(service, {})
                svc_type_dict.update({'color':color})
                svc_type_dict.update({'percentage':percentage})
                continue
            # 193.0.2.2        192.168.13.1            105  193.0.2.3
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                lan_ip = groups['lan_ip'].strip().replace('-', '_').replace(' ', '_').replace(':', '').lower()
                system_ip = groups['system_ip'].strip().replace('-', '_').replace(' ', '_').replace(':', '').lower()
                sys_ip_dict = ret_dict.setdefault('service_controllers',{}).\
                    setdefault('lan_ip', {}).setdefault(lan_ip, {}).\
                    setdefault('system_ip',{}).setdefault(system_ip, {})
                site_id = int(groups['site_id'].strip().replace('-', '_').replace(' ', '_').replace(':', '').lower())
                sn_lan_ip = groups['sn_lan_ip'].strip().replace('-', '_').replace(' ', '_').replace(':', '').lower()
                sys_ip_dict.update({'site_id':site_id,'sn_lan_ip':sn_lan_ip})
                continue

        return ret_dict

class ShowSdwanBfdHistorySchema(MetaParser):

    """schema for show sdwan bfd history"""

    schema={
        'site_id':
        {
            Any():
            {
                'system_ip':
                {
                    Any():
                    {
                        'dst_public_ip':
                        {
                            Any():
                            {
                                'time':
                                {
                                    Any():
                                    {
                                        'color': str,
                                        'state': str,
                                        'dst_public_port': str,
                                        'encap': str,
                                        'rx_pkts': str,
                                        'tx_pkts' : str,
                                        'del': str
                                    },
                                }
                            },
                        }
                    },
                }
            },
        }
    }

class ShowSdwanBfdHistory(ShowSdwanBfdHistorySchema):
    """parser for show sdwan bfd history"""

    cli_command= 'show sdwan bfd history'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #Removing unneccessary header
        try:
            strout= re.findall(r'\s+[DST PUBLIC \s]+RX+\s+TX+\s',out)
            out=out.replace(strout[0],"")
        except:
            out=out


        #parsed output using parsergen
        parsed_out = pg.oper_fill_tabular(device_output=out,
                                    header_fields=["SYSTEM IP", "SITE ID", "COLOR", "STATE", "IP", "PORT", "ENCAP","TIME","PKTS","PKTS","DEL"],
                                    label_fields=["system_ip", "site_id", "color", "state", "dst_public_ip", "dst_public_port","encap","time","rx_pkts","tx_pkts","del"],
                                    index= [1,0,4,7]
                                    )

        #creating a parsed dict using the output
        parsed_dict = parsed_out.entries

        #Parsing the dict according to the schema
        out_dict={}
        out_dict['site_id']={}
        cur_dict=out_dict['site_id']



        for key in parsed_dict.keys():
            cur_dict[key]={}
            cur_dict[key]['system_ip']={}
            for subkey in parsed_dict[key].keys():
                cur_dict[key]['system_ip'][subkey]={}
                cur_dict[key]['system_ip'][subkey]['dst_public_ip']={}
                for subsubkey in parsed_dict[key][subkey].keys():
                    cur_dict[key]['system_ip'][subkey]['dst_public_ip'][subsubkey]={}
                    cur_dict[key]['system_ip'][subkey]['dst_public_ip'][subsubkey]['time']={}
                    for subsubsubkey in parsed_dict[key][subkey][subsubkey].keys():
                        cur_dict[key]['system_ip'][subkey]['dst_public_ip'][subsubkey]['time'][subsubsubkey]={}
                        for valuekey in parsed_dict[key][subkey][subsubkey][subsubsubkey].keys():
                            if valuekey not in ['site_id','system_ip','dst_public_ip','time']:
                                cur_dict[key]['system_ip'][subkey]['dst_public_ip'][subsubkey]['time'][subsubsubkey][valuekey]=parsed_dict[key][subkey][subsubkey][subsubsubkey][valuekey]


        return out_dict

# =====================================
# Parser for 'show sdwan bfd sessions'
# =====================================
class ShowSdwanBfdSessions(ShowBfdSessions_viptela):

    """ Parser for "show sdwan bfd sessions" """
    cli_command = 'show sdwan bfd sessions'

    def cli(self, output = None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output

        return super().cli(output = show_output)

# ===============================================
# Parser for 'show sdwan bfd summary'
# ===============================================
class ShowSdwanBfdSummary(ShowBfdSummary_viptela):

    """ Parser for "show sdwan bfd summary" """
    cli_command = 'show sdwan bfd summary'

    def cli(self, output = None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output

        return super().cli(output = show_output)

# ===========================================
# Schema for 'show sdwan control summary'
# ===========================================
class ShowSdwanControlSummarySchema(MetaParser):

    """ Schema for "show sdwan control summary" """

    schema = {
        "summary": int,
        "vbond_counts": int,
        "vmanage_counts": int,
        "vsmart_counts": int,
    }

# ===========================================
# Parser for 'show sdwan control summary'
# ===========================================
class ShowSdwanControlSummary(ShowSdwanControlSummarySchema):

    """ Parser for "show sdwan control summary" """

    cli_command = 'show sdwan control summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # sh sdwan control summary
        #  control summary 0
        #   vbond_counts   0
        #   vmanage_counts 1
        #   vsmart_counts  6

        p1 = re.compile(r"(?P<key>\w+)\s+(?P<value>\d+)")

        for line in out.splitlines():
            line = line.strip()
            m = p1.search(line)
            if m:
                groups = m.groupdict()
                key = groups["key"].lower()
                value = int(groups["value"])

                parsed_dict.update({key: value})

        return parsed_dict

# ===========================================
# Parser for 'show sdwan control connections'
# ===========================================
class ShowSdwanControlConnections(ShowControlConnections_viptela):

    """ Parser for "show sdwan control connections" """
    cli_command = 'show sdwan control connections'

    def cli(self, output = None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output

        return super().cli(output = show_output)

# ===============================================
# Parser for 'show sdwan control local-properties'
# ===============================================
class ShowSdwanControlLocalProperties(ShowControlLocalProperties_viptela):

    """ Parser for "show sdwan control local-properties" """
    cli_command = 'show sdwan control local-properties'

    def cli(self, output = None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output

        return super().cli(output = show_output)

# =================================================
# Schema for 'show sdwan ipsec inbound-connections'
# =================================================
class ShowSdwanIpsecInboundConnectionsSchema(MetaParser):
    """ Schema for "show sdwan ipsec inbound-connections" command """

    schema = {
        "source_ip": {
            Any(): {
                'destination_ip': {
                    Any(): {
                        "local_tloc_color": str,
                        "destination_port": int,
                        "local_tloc": str,
                        "remote_tloc_color": str,
                        "remote_tloc": str,
                        "source_port": int,
                        "encryption_algorithm": str,
                        "tc_spi": int,
                    },
                },
            },
        },
    }

# =================================================
# Schema for 'show sdwan ipsec outbound-connections'
# =================================================
class ShowSdwanIpsecOutboundConnectionsSchema(MetaParser):
    """ Schema for "show sdwan ipsec outbound-connections" command """

    schema = {
        "source_ip": {
            Any(): {
                'destination_ip': {
                    Any(): {
                        "destination_port": int,
                        "authentication": str,
                        "remote_tloc_color": str,
                        "key_hash": str,
                        "spi": int,
                        "source_port": int,
                        "remote_tloc": str,
                        "encryption_algorithm": str,
                        "tunnel_mtu": int,
                        "tc_spi": int,
                    },
                },
            },
        },
    }

# =================================================
# Schema for 'show sdwan ipsec local-sa <WORD>'
# =================================================
class ShowSdwanIpsecLocalsaSchema(MetaParser):
    """ Schema for "show sdwan ipsec local-sa <WORD>" command """

    schema = {
        "local_sa": {
            'inbound': {
                'spi': int,
                'source_ipv4': str,
                'source_port': int,
                'source_ipv6': str,
                'tloc_color': str,
                'key_hash': str,
            },
            'outbound': {
                'spi': int,
                'source_ipv4': str,
                'source_port': int,
                'source_ipv6': str,
                'tloc_color': str,
                'key_hash': str,
            },
        },
    }

# =================================================
# Parser for 'show sdwan ipsec inbound-connections'
# =================================================
class ShowSdwanIpsecInboundConnections(ShowSdwanIpsecInboundConnectionsSchema):
    """ Parser for "show sdwan ipsec inbound-connections" """

    exclude = ['uptime']

    cli_command = "show sdwan ipsec inbound-connections"

    def cli(self, output=''):
        if not output:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        #10.106.2.2 12346   10.106.8.2 12406   10.111.0.6 biz-internet     10.111.0.9 biz-internet     AES-GCM-256           8
        p1 = re.compile(
            r"^(?P<source_ip>[\S]+) +(?P<source_port>[\d]+) +"
            r"(?P<destination_ip>[\S]+) +(?P<destination_port>[\d]+) +"
            r"(?P<remote_tloc>[\S]+) +(?P<remote_tloc_color>[\S]+) +"
            r"(?P<local_tloc>[\S]+) +(?P<local_tloc_color>[\S]+) +"
            r"(?P<encryption_algorithm>[\S]+) +(?P<tc_spi>[\d]+)$")

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                groups = m.groupdict()
                parameters_dict = {}
                source_ip = groups['source_ip']
                destination_ip = groups['destination_ip']
                parsed_dict.setdefault("source_ip",
                                       {}).setdefault(source_ip, {})
                destination_dict = parsed_dict["source_ip"][
                    source_ip].setdefault("destination_ip", {})
                parameters_dict.update({
                    'local_tloc_color':
                    groups['local_tloc_color'],
                    'destination_port':
                    int(groups['destination_port']),
                    'local_tloc':
                    groups['local_tloc'],
                    'remote_tloc_color':
                    groups['remote_tloc_color'],
                    'remote_tloc':
                    groups['remote_tloc'],
                    'source_port':
                    int(groups['source_port']),
                    'encryption_algorithm':
                    groups['encryption_algorithm'],
                    'tc_spi':
                    int(groups['tc_spi']),
                })
                ipsec_dict = destination_dict.setdefault(
                    destination_ip, parameters_dict)
                continue

        return parsed_dict

# =================================================
# Parser for 'show sdwan ipsec outbound-connections'
# =================================================
class ShowSdwanIpsecOutboundConnections(ShowSdwanIpsecOutboundConnectionsSchema
                                        ):
    """ Parser for "show sdwan ipsec outbound-connections" """

    exclude = ['uptime']

    cli_command = "show sdwan ipsec outbound-connections"

    def cli(self, output=''):
        if not output:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        #10.106.8.2                               12346   10.106.2.2                               12366   271     1438        10.111.0.6        biz-internet     AH_SHA1_HMAC   *****b384  AES-GCM-256           8
        p1 = re.compile(
            r"^(?P<source_ip>[\S]+) +(?P<source_port>[\d]+) +"
            r"(?P<destination_ip>[\S]+) +(?P<destination_port>[\d]+) +"
            r"(?P<spi>[\d]+) +(?P<tunnel_mtu>[\d]+) +"
            r"(?P<remote_tloc>[\S]+) +(?P<remote_tloc_color>[\S]+) +"
            r"(?P<authentication>[\S]+) +(?P<key_hash>[\S]+) +"
            r"(?P<encryption_algorithm>[\S]+) +(?P<tc_spi>[\d]+)$")

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                groups = m.groupdict()
                parameters_dict = {}
                source_ip = groups['source_ip']
                destination_ip = groups['destination_ip']
                parsed_dict.setdefault("source_ip",
                                       {}).setdefault(source_ip, {})
                destination_dict = parsed_dict["source_ip"][
                    source_ip].setdefault("destination_ip", {})
                parameters_dict.update({
                    'destination_port':
                    int(groups['destination_port']),
                    'authentication':
                    groups['authentication'],
                    'remote_tloc_color':
                    groups['remote_tloc_color'],
                    'key_hash':
                    groups['key_hash'],
                    'spi':
                    int(groups['spi']),
                    'source_port':
                    int(groups['source_port']),
                    'remote_tloc':
                    groups['remote_tloc'],
                    'encryption_algorithm':
                    groups['encryption_algorithm'],
                    'tunnel_mtu':
                    int(groups['tunnel_mtu']),
                    'tc_spi':
                    int(groups['tc_spi']),
                })
                ipsec_dict = destination_dict.setdefault(
                    destination_ip, parameters_dict)
                continue

        return parsed_dict

# =================================================
# Parser for 'show sdwan ipsec local-sa <WORD>'
# =================================================
class ShowSdwanIpsecLocalsa(ShowSdwanIpsecLocalsaSchema):
    """ Parser for "show sdwan ipsec local-sa <WORD>" """

    exclude = ['uptime']

    cli_command = "show sdwan ipsec local-sa {tloc_address}"

    def cli(self, tloc_address='', output=''):
        if not output:
            output = self.device.execute(self.cli_command.format(tloc_address=tloc_address))

        parsed_dict = {}

        #10.111.0.9        biz-internet     259     10.106.8.2        ::                                      12346   *****8d95
        #10.111.0.9        biz-internet     260     10.106.8.2        ::                                      12346   *****4447
        p1 = re.compile(
            r"^(?P<tloc_address>[\S]+) +(?P<tloc_color>[\S]+) +"
            r"(?P<spi>[\d]+) +(?P<source_ipv4>[\S]+) +"
            r"(?P<source_ipv6>[\S]+) +(?P<source_port>[\d]+) +(?P<key_hash>[\S]+)$"
        )

        count = 0
        for line in output.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                count += 1
                groups = m.groupdict()
                if count != 2:
                    spi_dict = parsed_dict.setdefault(
                        "local_sa",
                        OrderedDict()).setdefault("inbound", OrderedDict())
                else:
                    spi_dict = parsed_dict.setdefault(
                        "local_sa",
                        OrderedDict()).setdefault("outbound", OrderedDict())
                keys = [
                    "spi", "source_ipv4", "source_port", "source_ipv6",
                    "tloc_color", "key_hash"
                ]
                for k in keys:
                    spi_dict[k] = int(groups[k]) if k in [
                        "spi", "source_port"
                    ] else groups[k]
        return parsed_dict

# ===============================================
# Parser for 'show sdwan omp summary'
# ===============================================
class ShowSdwanOmpSummary(ShowOmpSummary_viptela):

    """ Parser for "show sdwan omp summary" """
    cli_command = 'show sdwan omp summary'

    def cli(self, output = None):
        if not output:
            show_output = self.device.execute(self.cli_command)

        return super().cli(output = show_output)

# ===============================================
# Parser for 'show sdwan omp peers'
# ===============================================
class ShowSdwanOmpPeers(ShowOmpPeers_viptela):

    """ Parser for "show sdwan omp peers" """
    cli_command = 'show sdwan omp peers'

    def cli(self, output = None):
        if not output:
            show_output = self.device.execute(self.cli_command)

        return super().cli(output = show_output)

# ===============================================
# Parser for 'show sdwan omp tlocs'
# ===============================================
class ShowSdwanOmpTlocs(ShowOmpTlocs_viptela):

    """ Parser for "show sdwan omp tlocs" """
    cli_command = 'show sdwan omp tlocs'

    def cli(self, output = None):
        if not output:
            show_output = self.device.execute(self.cli_command)

        return super().cli(output = show_output)

# ===============================================
# Parser for 'show sdwan omp tloc-paths'
# ===============================================
class ShowSdwanOmpTlocPath(ShowOmpTlocPath_viptela):

    """ Parser for "show sdwan omp tloc-paths" """
    cli_command = 'show sdwan omp tloc-paths'

    def cli(self, output = None):
        if not output:
            show_output = self.device.execute(self.cli_command)

        return super().cli(output = show_output)


# ===============================================
# Parser for 'show sdwan omp routes'
# ===============================================
class ShowSdwanOmpRoutes(ShowOmpRoutes_viptela):

    """ Parser for "show sdwan omp routes" """
    cli_command = ['show sdwan omp routes',
                  'show sdwan omp routes {prefix}',
                  'show sdwan omp routes vpn {vpn}',
                  'show sdwan omp routes {prefix} vpn {vpn}',
                  'show sdwan omp routes family {af} vpn {vpn}']

    def cli(self, prefix=None, vpn=None, af='ipv4', output=None):

        if output is None:
            if prefix and vpn:
                cmd = self.cli_command[3].format(prefix=prefix, vpn=vpn)
            elif af and vpn:
                cmd = self.cli_command[4].format(af=af, vpn=vpn)
            elif prefix:
                cmd = self.cli_command[1].format(prefix=prefix)
            elif vpn:
                cmd = self.cli_command[2].format(vpn=vpn)
            else:
                cmd = self.cli_command[0]
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        return super().cli(output=show_output, prefix=prefix, vpn=vpn)


class ShowSdwanPolicyIpv6AccessListAssociationsSchema(MetaParser):
    ''' Schema for show sdwan policy ipv6 access list associations'''
    schema = {
        'name': {
            Any(): {
                'interface_direction': {
                    Any(): {
                        'interface_name': list,
                    },
                }
            },
        }
    }

class ShowSdwanPolicyIpv6AccessListAssociations(ShowSdwanPolicyIpv6AccessListAssociationsSchema):

    """ Parser for "show sdwan policy ipv6 access list associations" """

    cli_command = "show sdwan policy ipv6 access-list-associations"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict={}
        return_dict = {}
        if out:
            outlist = out.splitlines()
            # acl-v6-apple  TenGigabitEthernet0/0/0.1002  in
            #               TenGigabitEthernet0/0/0.1002  out
            #               TenGigabitEthernet0/0/2.1002  in
            #               TenGigabitEthernet0/0/2.1002  out
            p1 = re.compile(r'^(?P<name>[\w\-\s]+) + (?P<interface_name>[\d\w/\.\-]+) + (?P<interface_direction>[\w]+)$')
            for line in outlist:
                m1 = p1.match(line)
                if m1:
                    groups = m1.groupdict()
                    if groups['name'].replace(' ', '') != '':
                        key = groups['name'].replace(' ', '')
                        return_dict[key] = {}
                        list_in = []
                        list_out = []
                        list_in.append(groups['interface_name'])
                        return_dict[key]['interface_direction'] = {}
                        return_dict[key]['interface_direction'][groups['interface_direction']] = {}
                        return_dict[key]['interface_direction']['in']['interface_name'] = list_in
                    else:
                        if groups['interface_direction'] == 'out':
                            list_out.append(groups['interface_name'])
                        elif groups['interface_direction'] == 'in':
                            list_in.append(groups['interface_name'])
                        return_dict[key]['interface_direction']['out'] = {}
                        return_dict[key]['interface_direction']['out']['interface_name'] = {}
                        return_dict[key]['interface_direction']['in']['interface_name'] = list_in
                        return_dict[key]['interface_direction']['out']['interface_name'] = list_out
            parsed_dict['name'] = return_dict
        return parsed_dict

class ShowSdwanPolicyAccessListAssociations(ShowSdwanPolicyIpv6AccessListAssociationsSchema):
    """ Parser for "show sdwan policy ipv6 access list associations" """

    cli_command = "show sdwan policy access-list-associations"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}
        return_dict = {}
        if out:
            outlist = out.splitlines()
            # acl-v4        TenGigabitEthernet0/0/2.1002  in
            #               TenGigabitEthernet0/0/2.1002  out
            # acl-v4-apple  TenGigabitEthernet0/0/0.1002  in
            #               TenGigabitEthernet0/0/0.1002  out
            p1 = re.compile(
                r'^(?P<name>[\w\-\s]+) + (?P<interface_name>[\d\w/\.\-]+) + (?P<interface_direction>[\w]+)$')
            for line in outlist:
                m1 = p1.match(line)
                if m1:
                    groups = m1.groupdict()
                    if groups['name'].replace(' ', '') != '':
                        key = groups['name'].replace(' ', '')
                        return_dict[key] = {}
                        list_in = []
                        list_out = []
                        list_in.append(groups['interface_name'])
                        return_dict[key]['interface_direction'] = {}
                        return_dict[key]['interface_direction'][groups['interface_direction']] = {}
                        return_dict[key]['interface_direction']['in']['interface_name'] = list_in
                    else:
                        if groups['interface_direction'] == 'out':
                            list_out.append(groups['interface_name'])
                        elif groups['interface_direction'] == 'in':
                            list_in.append(groups['interface_name'])
                        return_dict[key]['interface_direction']['out'] = {}
                        return_dict[key]['interface_direction']['out']['interface_name'] = {}
                        return_dict[key]['interface_direction']['in']['interface_name'] = list_in
                        return_dict[key]['interface_direction']['out']['interface_name'] = list_out
            parsed_dict['name'] = return_dict
        return parsed_dict

class ShowSdwanPolicyAccessListCountersSchema(MetaParser):
    ''' Schema for show sdwan policy access-list-counters'''
    schema = {
        'name': {
            Any(): {
                'counter_name': {
                    Any(): {
                        'bytes': int,
                        'packets': int
                    }
                }
            },
        }
    }

class ShowSdwanPolicyAccessListCounters(ShowSdwanPolicyAccessListCountersSchema):

    """ Parser for "show sdwan policy access-list-counters" """

    cli_command = "show sdwan policy access-list-counters" or "show sdwan policy ipv6 access-list-counters"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}
        return_dict={}
        if out:
            outlist=out.splitlines()
            for lines in range(len(outlist)):
                if len(outlist[lines].rstrip()) < 24:
                    local_list=outlist[lines-1].split()
                    local_list[0] = local_list[0]+ outlist[lines]
                    outlist[lines-1] = "  ".join(local_list)
            # acl-v4  count_seq_1                       0             0
            #         count_seq_2                       0             0
            #         count_seq_3                       0             0
            #         count_seq_4                       0             0
            #         count_seq_5                       0             0
            #         count_seq_7                       0             0
            #         count_seq_8                       0             0
            #         count_seq_9                       0             0
            #         count_seq_10                      0             0
            #         count_seq_11                      0             0
            #         count_seq_12                      0             0
            #         count_seq_13                      0             0
            #         count_seq_14                      0             0
            #         count_seq_15                      0             0
            #         count_seq_16                      0             0
            #         count_seq_17                      0             0
            #         count_seq_18                      0             0
            #         count_seq_19                      0             0
            #         count_seq_20                      0             0
            #         count_seq_21                      0             0
            #         count_seq_22                      0             0
            #         count_seq_23                      0             0
            #         count_seq_24                      0             0
            #         vpn1002-v4-traffic                9788308290    8520697223296
            #         default_action_count              0             0
            # acl-v4  acl_v4_40gig_counter              0             0
            # -40gig
            #         default_action_count              0             0
            # acl-v4  seq1                              8726713375    7977499318508
            # -apple
            #         default_action_count              246601717     239371283918
            p1=re.compile(r'^(?P<name>[\w\-\s]+) + (?P<counter_name>[\d\w/\.\-]+) + (?P<packets>[\d]+) +(?P<bytes>[\d]+)$')
            for line in outlist:
                m1=p1.match(line.rstrip())
                if m1:
                    groups = m1.groupdict()
                    local_dict = {}
                    local_dict['packets'] = int(groups['packets'])
                    local_dict['bytes'] = int(groups['bytes'])
                    if groups['name'].replace(' ', '') != '':
                        key = groups['name'].replace(' ', '')
                        return_dict[key] = {}
                        return_dict[key]['counter_name'] = {}
                        return_dict[key]['counter_name'][groups['counter_name']] = {}
                        return_dict[key]['counter_name'][groups['counter_name']] = local_dict
                    else:
                        return_dict[key]['counter_name'][groups['counter_name']] = local_dict
            parsed_dict['name'] = return_dict
        return parsed_dict

class ShowSdwanPolicyIpv6AccessListCounters(ShowSdwanPolicyAccessListCountersSchema):
    """ Parser for "show sdwan policy access-list-counters" """

    cli_command = "show sdwan policy ipv6 access-list-counters"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}
        return_dict = {}
        if out:
            outlist = out.splitlines()
            for lines in range(len(outlist)):
                if len(outlist[lines].rstrip()) < 24:
                    local_list = outlist[lines - 1].split()
                    local_list[0] = local_list[0] + outlist[lines]
                    outlist[lines - 1] = "  ".join(local_list)
            # acl-v6-apple  vpn1002-v6-traffic    3999853226  3260866067656
            #               default_action_count  248080      22356152
            p1 = re.compile(
                r'^(?P<name>[\w\-\s]+) + (?P<counter_name>[\d\w/\.\-]+) + (?P<packets>[\d]+) +(?P<bytes>[\d]+)$')
            for line in outlist:
                m1 = p1.match(line.rstrip())
                if m1:
                    groups = m1.groupdict()
                    local_dict = {}
                    local_dict['packets'] = int(groups['packets'])
                    local_dict['bytes'] = int(groups['bytes'])
                    if groups['name'].replace(' ', '') != '':
                        key = groups['name'].replace(' ', '')
                        return_dict[key] = {}
                        return_dict[key]['counter_name'] = {}
                        return_dict[key]['counter_name'][groups['counter_name']] = {}
                        return_dict[key]['counter_name'][groups['counter_name']] = local_dict
                    else:
                        return_dict[key]['counter_name'][groups['counter_name']] = local_dict
            parsed_dict['name'] = return_dict
        return parsed_dict

# =====================================
# Parser for 'show sdwan reboot history'
# =====================================
class ShowSdwanRebootHistory(ShowRebootHistory_viptela):

    """ Parser for "show sdwan reboot history" """
    cli_command = 'show sdwan reboot history'

    def cli(self, output = None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output
        return super().cli(output = show_output)

# =====================================
# Parser for 'show sdwan software'
# =====================================
class ShowSdwanSoftware(ShowSoftwaretab_viptela):

    """ Parser for "show sdwan software" """
    cli_command = 'show sdwan software'

    def cli(self, output = None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output
        if re.search('Total Space:',show_output):
            fin=re.search('Total Space:.*',show_output)
            show_output=show_output.replace(fin.group(0),' ')

        return super().cli(output = show_output)

# =====================================
# Parser for 'show sdwan system status'
# =====================================
class ShowSdwanSystemStatus(ShowSystemStatus_viptela):

    """ Parser for "show sdwan system status" """
    cli_command = 'show sdwan system status'

    def cli(self, output = None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output
        return super().cli(output = show_output)

# =====================================
# Parser for 'show sdwan version'
# =====================================
class ShowSdwanVersion(ShowVersion_viptela):

    """ Parser for "show sdwan version" """
    cli_command = 'show sdwan version'

    def cli(self, output = None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output
        return super().cli(output = show_output)

class ShowSdwanZonebfwdpSessionsSchema(MetaParser):
    schema = {
        'session_db': {
            Any(): {
                'session_id': int,
                'state': str,
                'src_ip': str,
                'dst_ip': str,
                'src_port': int,
                'dst_port': int,
                'protocol': str,
                'src_vrf': int,
                'dst_vrf': int,
                'src_vpn_id': int,
                'dst_vpn_id': int,
                'zp_name': str,
                'classmap_name': str,
                'nat_flags': str,
                'internal_flags': int,
                'total_initiator_bytes': int,
                'total_responder_bytes': int,
                Optional('application_type'): str
                }
         }
    }

class ShowSdwanZonebfwdpSessions(ShowSdwanZonebfwdpSessionsSchema):
    """Parser for show sdwan zonebfwdp sessions
    parser class - implements detail parsing mechanisms for cli output.
    """

    cli_command = 'show sdwan zonebfwdp sessions'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output


        #18005202  open    10.76.0.7  172.16.186.50    49873  443   PROTO_L7_HTTPS  2    2    1    0    ZP_lanZone_wanZone_I_-1639760094  Isn4451ZbfPolicy-seq-1-cm_  -      0         3684       67394
        p1 = re.compile(r'^(?P<sess_id>\d+)\s+(?P<state>\w+)\s+(?P<src_ip>\S+)\s+(?P<dst_ip>\S+)\s+(?P<src_port>\d+)\s+(?P<dst_port>\d+)\s+(?P<proto>\S+)\s+(?P<src_vrf>\d+)\s+(?P<dst_vrf>\d+)\s+(?P<src_vpn_id>\d+)\s+(?P<dst_vpn_id>\d+)\s+(?P<zp_name>\S+)\s+(?P<classmap_name>\S+)\s+(?P<nat_flags>\S+)\s+(?P<internal_flags>\d+)\s+(?P<tot_init_bytes>\d+)\s+(?P<tot_resp_bytes>\d+)$')

        #4583 open 10.225.18.63 10.196.18.63 1024 1024 PROTO_L4_UDP 3 3 20 20 ZP_LAN_ZONE_vpn20_LAN__968352866 ZBFW-seq-1-cm_ - 0 2435061651 2435062756 /statistical-p2p
        p2 = re.compile(r'^(?P<sess_id>\d+)\s+(?P<state>\w+)\s+(?P<src_ip>\S+)\s+(?P<dst_ip>\S+)\s+(?P<src_port>\d+)\s+(?P<dst_port>\d+)\s+(?P<proto>\S+)\s+(?P<src_vrf>\d+)\s+(?P<dst_vrf>\d+)\s+(?P<src_vpn_id>\d+)\s+(?P<dst_vpn_id>\d+)\s+(?P<zp_name>\S+)\s+(?P<classmap_name>\S+)\s+(?P<nat_flags>\S+)\s+(?P<internal_flags>\d+)\s+(?P<tot_init_bytes>\d+)\s+(?P<tot_resp_bytes>\d+)\s+(?P<app_type>\S+)$')


        ret_dict = {}
        sess_num = 0
        for line in out.splitlines():
            line = line.strip()

            ##18005202  open    10.76.0.7  172.16.186.50    49873  443   PROTO_L7_HTTPS  2    2    1    0    ZP_lanZone_wanZone_I_-1639760094  Isn4451ZbfPolicy-seq-1-cm_  -      0         3684       67394

            m = p1.match(line)
            if m:
                groups = m.groupdict()
                sess_dict = ret_dict.setdefault('session_db', {})
                feature_dict = sess_dict.setdefault(sess_num, {})
                feature_dict.update(({'session_id': int(groups['sess_id'])}))
                feature_dict.update(({'state': (groups['state'])}))
                feature_dict.update(({'src_ip': (groups['src_ip'])}))
                feature_dict.update(({'dst_ip': (groups['dst_ip'])}))
                feature_dict.update(({'src_port': int(groups['src_port'])}))
                feature_dict.update(({'dst_port': int(groups['dst_port'])}))
                feature_dict.update(({'protocol': (groups['proto'])}))
                feature_dict.update(({'src_vrf': int(groups['src_vrf'])}))
                feature_dict.update(({'dst_vrf': int(groups['dst_vrf'])}))
                feature_dict.update(({'src_vpn_id': int(groups['src_vpn_id'])}))
                feature_dict.update(({'dst_vpn_id': int(groups['dst_vpn_id'])}))
                feature_dict.update(({'zp_name': (groups['zp_name'])}))
                feature_dict.update(({'classmap_name': (groups['classmap_name'])}))
                feature_dict.update(({'nat_flags': (groups['nat_flags'])}))
                feature_dict.update(({'internal_flags': int(groups['internal_flags'])}))
                feature_dict.update(({'total_initiator_bytes': int(groups['tot_init_bytes'])}))
                feature_dict.update(({'total_responder_bytes': int(groups['tot_resp_bytes'])}))
                sess_num = sess_num + 1
                last_dict_ptr = feature_dict
                continue

            #4583 open 10.225.18.63 10.196.18.63 1024 1024 PROTO_L4_UDP 3 3 20 20 ZP_LAN_ZONE_vpn20_LAN__968352866 ZBFW-seq-1-cm_ - 0 2435061651 2435062756 /statistical-p2p
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                sess_dict = ret_dict.setdefault('session_db', {})
                feature_dict = sess_dict.setdefault(sess_num, {})
                feature_dict.update(({'session_id': int(groups['sess_id'])}))
                feature_dict.update(({'state': (groups['state'])}))
                feature_dict.update(({'src_ip': (groups['src_ip'])}))
                feature_dict.update(({'dst_ip': (groups['dst_ip'])}))
                feature_dict.update(({'src_port': int(groups['src_port'])}))
                feature_dict.update(({'dst_port': int(groups['dst_port'])}))
                feature_dict.update(({'protocol': (groups['proto'])}))
                feature_dict.update(({'src_vrf': int(groups['src_vrf'])}))
                feature_dict.update(({'dst_vrf': int(groups['dst_vrf'])}))
                feature_dict.update(({'src_vpn_id': int(groups['src_vpn_id'])}))
                feature_dict.update(({'dst_vpn_id': int(groups['dst_vpn_id'])}))
                feature_dict.update(({'zp_name': (groups['zp_name'])}))
                feature_dict.update(({'classmap_name': (groups['classmap_name'])}))
                feature_dict.update(({'nat_flags': (groups['nat_flags'])}))
                feature_dict.update(({'internal_flags': int(groups['internal_flags'])}))
                feature_dict.update(({'total_initiator_bytes': int(groups['tot_init_bytes'])}))
                feature_dict.update(({'total_responder_bytes': int(groups['tot_resp_bytes'])}))
                feature_dict.update(({'application_type': (groups['app_type'])}))
                sess_num = sess_num + 1
                last_dict_ptr = feature_dict
                continue

        return(ret_dict)

class ShowSdwanZbfwStatisticsSchema(MetaParser):
    schema = {
        'zonepair_name': {
            Any(): {
                'src_zone_name': str,
                'dst_zone_name': str,
                'policy_name': str,
                'class_entry': {
                    Any():{
                        'zonepair_name': str,
                        'class_action': str,
                        'pkts_counter': int,
                        'bytes_counter': int,
                        'attempted_conn': int,
                        'current_active_conn': int,
                        'max_active_conn': int,
                        'current_halfopen_conn': int,
                        'max_halfopen_conn': int,
                        'current_terminating_conn': int,
                        'max_terminating_conn': int,
                        'time_since_last_session_create': int,
                        Optional('match_entry'): {
                            Any(): {
                                'seq_num': int,
                                Optional('match_crit'): str,
                                'match_type': str
                            }
                        },
                        Optional('proto_entry'):{
                            int: {
                                'protocol_name': str,
                                'byte_counters': int,
                                'pkt_counters': int
                            }
                        },
                        'l7_policy_name': str
                    }
                },
                Optional('l7_class_entry'): {
                    Any(): {
                        'parent_class_name': str,
                        'child_class_action': str,
                        'pkts_counter': int,
                        'bytes_counter': int,
                        'attempted_conn': int,
                        'current_active_conn': int,
                        'max_active_conn': int,
                        'current_halfopen_conn': int,
                        'max_halfopen_conn': int,
                        'current_terminating_conn': int,
                        'max_terminating_conn': int,
                        'time_since_last_session_create': int,
                        Optional('l7_match_entry'): {
                            Any(): {
                                'byte_counters': int,
                                'pkt_counters': int
                            }
                        }
                    }
                }
            }
        }
    }

class ShowSdwanZbfwStatistics(ShowSdwanZbfwStatisticsSchema):
    """Parser for show sdwan zbfw zonepair-statistics
    parser class - implements detail parsing mechanisms for cli output.
    """

    cli_command = 'show sdwan zbfw zonepair-statistics'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #zbfw zonepair-statistics ZP_lanZone_lanZone_Is_-902685811
        #p1 = re.compile(r'^zbfw zonepair-statistics (?P<zp_name>\S+)$')
        p1 = re.compile(r'^zbfw\s+zonepair-statistics\s+(?P<zp_name>\S+)$')

        #fw-traffic-class-entry Isn4451ZbfPolicy-seq-1-cm_
        p2 = re.compile(r'^(?P<class_name>(fw-traffic-class-entry|fw-l7-traffic-class-entry)) (?P<class_entry>\S+)$')

        #fw-tc-match-entry "match-any Isn4451ZbfPolicy-svrf1-l4-cm_" 11
        #p3 = re.compile(r'^fw-tc-match-entry "(?P<match_crit>\S+)\s+(?P<tc_entry>[\w\d\s-]+)"\s(?P<tc_num>\S+)$')
        p3 = re.compile(r'^fw-tc-match-entry\s+"(?P<match_crit>\S+)\s+(?P<tc_entry>[\w\d\s-]+)"\s+(?P<tc_num>\S+)$')

        #fw-tc-match-entry Isn4451ZbfPolicy-seq-vrf5-acl_ 3
        #p4 = re.compile(r'^fw-tc-match-entry (?P<tc_entry>[\w\d\s-]+)\s(?P<tc_num>\S+)$')
        p4 = re.compile(r'^fw-tc-match-entry\s+(?P<tc_entry>[\w\d\s-]+)\s(?P<tc_num>\S+)$')

        #fw-tc-proto-entry 1
        #p5 = re.compile(r'^(?P<match_name>fw-tc-proto-entry|fw-l7-tc-match-app-entry)\s+(?P<entry_val>[\w\d\-]+)$')
        p5 = re.compile(r'^(?P<match_name>fw-tc-proto-entry|fw-l7-tc-match-app-entry)\s+(?P<entry_val>[\w\d\-]+)$')

        #l7-policy-name                 NONE
        p6 = re.compile(r'^(?P<entry_name>l7-policy-name)\s+(?P<entry_val>\S+)$')

        #src-zone-name lanZone
        #p5 = re.compile(r'^(?P<key>\S+)\s+(?P<value>\S+)$')
        p7 = re.compile(r'^(?P<key>\S+)\s+\"?(?P<value>[\w\s\d\-\_]+)\"?$')


        ret_dict = {}
        last_dict_ptr = {}
        for line in out.splitlines():
            line = line.strip()

            #zbfw zonepair-statistics ZP_lanZone_lanZone_Is_-902685811
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                feature_dict = ret_dict.setdefault('zonepair_name', {}).setdefault(groups['zp_name'], {})
                last_dict_ptr = feature_dict
                continue

            #fw-traffic-class-entry Isn4451ZbfPolicy-seq-1-cm_
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                if(groups['class_name'] == 'fw-l7-traffic-class-entry'):
                    class_dict = feature_dict.setdefault('l7_class_entry', {}).setdefault(groups['class_entry'], {})
                else:
                    class_dict = feature_dict.setdefault('class_entry', {}).setdefault(groups['class_entry'], {})
                last_dict_ptr = class_dict
                continue

            #fw-tc-match-entry "match-any Isn4451ZbfPolicy-svrf1-l4-cm_" 11
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                tc_dict = class_dict.setdefault('match_entry', {}).setdefault(groups['tc_entry'], {})
                tc_dict.update({'seq_num': int(groups['tc_num'])})
                tc_dict.update({'match_crit': (groups['match_crit'])})
                last_dict_ptr = tc_dict
                continue

            m = p4.match(line)
            if m:
                groups = m.groupdict()
                tc_dict = class_dict.setdefault('match_entry', {}).setdefault(groups['tc_entry'], {})
                tc_dict.update({'seq_num': int(groups['tc_num'])})
                last_dict_ptr = tc_dict
                continue

            m = p5.match(line)
            if m:
                groups = m.groupdict()
                if(groups['match_name'] == 'fw-l7-tc-match-app-entry'):
                    tc1_dict = class_dict.setdefault('l7_match_entry', {}).setdefault(groups['entry_val'], {})
                else:
                    tc1_dict = class_dict.setdefault('proto_entry', {}).setdefault(int(groups['entry_val']), {})

                    #tc1_dict = class_dict.setdefault(groups['entry_name'], {})
                    #tc1_dict.update({'seq_num': int(groups['tc_num'])})
                last_dict_ptr = tc1_dict
                continue

            m = p6.match(line)
            if m:
                groups = m.groupdict()
                class_dict.update({groups['entry_name'].replace('-', '_'): (groups['entry_val'])})
                continue

            #src-zone-name lanZone
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                if groups['key'].replace('-', '_').strip() in ['class_action','src_zone_name','dst_zone_name','policy_name','zonepair_name','class_action','protocol_name','match_type','parent_class_name','child_class_action']:
                    last_dict_ptr.update({groups['key'].replace('-', '_'): groups['value']})
                else:
                    last_dict_ptr.update({groups['key'].replace('-', '_'): int(groups['value'])})
                    continue

        return(ret_dict)

# ========================================================
# Schema for "show sdwan tunnel sla index 0"
# ========================================================
class ShowSdwanTunnelSlaIndex0Schema(MetaParser):
    schema = {
        "lines": {
            Any(): {
                "color": str,
                "loss": str,
                "latency": str,
                "jitter": str,
                "slaclass": str
            }
        }
    }

class ShowSdwanTunnelSlaIndex0(ShowSdwanTunnelSlaIndex0Schema):
    """
    Parser for show sdwan tunnel sla index 0 on ios-xe sdwan devices.
    parser class - implements detail parsing mechanisms for cli output.
    """
    cli_command = "show sdwan tunnel sla index 0"
    """
    tunnel sla-class 0
     sla-name    __all_tunnels__
     sla-loss    0
     sla-latency 0
     sla-jitter  0
                                        SRC    DST    REMOTE       T LOCAL   T REMOTE  MEAN  MEAN     MEAN    SLA CLASS
    PROTO  SRC IP        DST IP          PORT   PORT   SYSTEM IP    COLOR     COLOR     LOSS  LATENCY  JITTER  INDEX      SLA CLASS NAME
    ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    ipsec  10.91.243.31  10.91.254.211   12346  12346  10.91.252.6  private1  private1  0     29       1       0,1,2,3,4  __all_tunnels__, Bulk-Data, Scavenger, Transactional-Data, Voice
    ipsec  10.91.243.31  10.91.254.212   12346  12346  10.91.252.7  private1  private1  0     29       0       0,1,2,3,4  __all_tunnels__, Bulk-Data, Scavenger, Transactional-Data, Voice
    ipsec  10.91.243.31  10.91.254.227   12346  12346  10.91.252.8  private1  private1  0     23       0       0,1,2,3,4  __all_tunnels__, Bulk-Data, Scavenger, Transactional-Data, Voice
    ipsec  10.91.243.31  10.91.254.228   12346  12346  10.91.252.9  private1  private1  0     23       1       0,1,2,3,4  __all_tunnels__, Bulk-Data, Scavenger, Transactional-Data, Voice
    ipsec  192.168.1.2   10.55.14.29     12386  12406  10.91.252.6  3g        3g        0     35       5       0,1,2,3,4  __all_tunnels__, Bulk-Data, Scavenger, Transactional-Data, Voice
    ipsec  192.168.1.2   10.55.14.31     12386  12346  10.91.252.7  3g        3g        0     35       5       0,1,2,3,4  __all_tunnels__, Bulk-Data, Scavenger, Transactional-Data, Voice
    ipsec  192.168.1.2   10.228.123.61   12386  12366  10.91.252.8  3g        3g        0     37       6       0,1,2,3,4  __all_tunnels__, Bulk-Data, Scavenger, Transactional-Data, Voice
    ipsec  192.168.1.2   10.228.123.63   12386  12346  10.91.252.9  3g        3g        0     36       6       0,1,2,3,4  __all_tunnels__, Bulk-Data, Scavenger, Transactional-Data, Voice
    ipsec  192.168.2.2   10.55.14.28     12406  12406  10.91.252.6  lte       lte       0     36       7       0,1,2,3,4  __all_tunnels__, Bulk-Data, Scavenger, Transactional-Data, Voice
    ipsec  192.168.2.2   10.55.14.30     12406  12366  10.91.252.7  lte       lte       0     36       8       0,1,2,3,4  __all_tunnels__, Bulk-Data, Scavenger, Transactional-Data, Voice
    ipsec  192.168.2.2   10.228.123.60   12406  12366  10.91.252.8  lte       lte       100   0        0       0          __all_tunnels__
    ipsec  192.168.2.2   10.228.123.62   12406  12366  10.91.252.9  lte       lte       0     37       7       0,1,2,3,4  __all_tunnels__, Bulk-Data, Scavenger, Transactional-Data, Voice
    """

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        sla_dict = {}

        result_dict = {}

        p0 = re.compile(r"^(?P<proto>\w+)\s+(?P<srcip>\d+\.\d+\.\d+\.\d+)\s+(?P<destip>\d+\.\d+\.\d+\.\d+)\s+(?P<srcport>\d+)\s+(?P<destport>\d+)\s+(?P<remip>\d+\.\d+\.\d+\.\d+)\s+(?P<localcolor>\w+)\s+(?P<remotecolor>\w+)\s+(?P<loss>\d+)\s+(?P<latency>\d+)\s+(?P<jitter>\d+)\s+(?P<slaclass>\S+)\s+(?P<slaclassname>.*)\s+")

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if "lines" not in sla_dict:
                    result_dict = sla_dict.setdefault("lines",{})
                destip = m.groupdict()["destip"]
                color = m.groupdict()["localcolor"]
                loss = m.groupdict()["loss"]
                latency = m.groupdict()["latency"]
                jitter = m.groupdict()["jitter"]
                slaclass = m.groupdict()["slaclass"]
                result_dict[destip] = {}
                result_dict[destip]["color"] = color
                result_dict[destip]["loss"] = loss
                result_dict[destip]["latency"] = latency
                result_dict[destip]["jitter"] = jitter
                result_dict[destip]["slaclass"] = slaclass
                continue
        return sla_dict

class ShowSdwanSystemOnDemandSchema(MetaParser):
    schema = {
        'on_demand_tunnel': {
            Any(): {
                'system-ip': str,
                'on-demand': str,
                Optional('status'): str,
                Optional('timeout'): int
            }
        }
    }

class ShowSdwanSystemOnDemand(ShowSdwanSystemOnDemandSchema):
    """Parser for
                  'show sdwan system on-demand'
                  'show sdwan system on-demand remote-system'
                  'show sdwan system on-demand remote-system system-ip <ip>'
    """

    cli_command = ['show sdwan system on-demand',
                  'show sdwan system on-demand {remote_system}',
                  'show sdwan system on-demand {remote_system} system-ip {system_ip}']

    def cli(self, remote_system='', system_ip='',output=None):
        if output is None:
            if system_ip:
                remote_system = "remote-system"
                cmd = self.cli_command[2].format(remote_system=remote_system, system_ip=system_ip)
            elif remote_system:
                cmd = self.cli_command[1].format(remote_system=remote_system)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # Initialization return dictionary
        ret_dict = {}

        # 21       21.0.0.21          yes          active              6
        # 23       21.0.0.23          no             -                 -
        p1 = re.compile(r'^(?P<site_id>[\d]+)\s+(?P<system_ip>[0-9\.]+)\s+(?P<on_demand>[A-Za-z]+)\s+(?P<status>[\S]+)\s+(?P<timeout>[\S]+)')

        for line in output.splitlines():
            # ret_dict_ptr = ret_dict.setdefault('on_demand_tunnel',{})
            line = line.strip()
            # 21       21.0.0.21          yes          active              6
            # 23       21.0.0.23          no             -                 -
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                site_id = groups['site_id']
                site_dict = ret_dict.setdefault('on_demand_tunnel',{}).setdefault(site_id,{})
                last_dict_ptr = site_dict
                last_dict_ptr.update({'system-ip':groups['system_ip']})
                last_dict_ptr.update({'on-demand':groups['on_demand']})
                if re.match("yes", groups['on_demand'], re.I):
                    last_dict_ptr.update({'status':groups['status']})
                    if re.match("active", groups['status'], re.I):
                        last_dict_ptr.update({'timeout':int(groups['timeout'])})
                continue
        return ret_dict


# =======================================================================
# Parser Schema for 'show sdwan Tunnel statitics'                       #
# I have made most of the keys as optional as it is common schema for   #
# 3-4 CLI commands as listed below.                                     #
# =======================================================================
class ShowSdwanTunnelStatisticsSchema(MetaParser):
    schema = {
        'tunnel': {
            Any(): {  # Local TLOC IP
                'remote': {
                    Any(): {  # Remote TLOC IP
                        Optional('protocol'): str,
                        "src_port": int,
                        "dst_port": int,
                        Optional("remote_sys_ip"): str,
                        Optional("local_color"): str,
                        Optional("remote_color"): str,
                        Optional("tunnel_mtu"): int,
                        Optional("tcp_mss_adjust"): int,
                        Optional("tx"): {
                            "tx_pkts": int,
                            "tx_octets": int,
                            "tx_ipv4_mcast_pkts": int,
                            "tx_ipv4_mcast_octets": int
                        },
                        Optional("rx"): {
                            "rx_pkts": int,
                            "rx_octets": int,
                            "rx_ipv4_mcast_pkts": int,
                            "rx_ipv4_mcast_octets": int
                        },
                        Optional("ipv6_tx"): {
                            "ipv6_tx_pkts": int,
                            "ipv6_tx_octets": int
                        },
                        Optional("ipv6_rx"): {
                            "ipv6_rx_pkts": int,
                            "ipv6_rx_octets": int
                        },
                        Optional("bfd"): {
                            Optional("echo"): {
                                "bfd_echo_tx_pkts": int,
                                "bfd_echo_rx_pkts": int,
                                "bfd_echo_tx_octets": int,
                                "bfd_echo_rx_octets": int
                            },
                            Optional("pmtu"): {
                                "bfd_pmtu_tx_pkts": int,
                                "bfd_pmtu_rx_pkts": int,
                                "bfd_pmtu_tx_octets": int,
                                "bfd_pmtu_rx_octets": int
                            }
                        },
                        Optional("fec"): {
                            "fec_rx_data_pkts": int,
                            "fec_rx_parity_pkts": int,
                            "fec_tx_data_pkts": int,
                            "fec_tx_parity_pkts": int,
                            "fec_reconstruct_pkts": int,
                            "fec_capable": str,
                            "fec_dynamic": str,
                        },
                        Optional("ipsec"): {
                            "ipsec_decrypt_inbound": int,
                            "ipsec_rx_auth_failures": int,
                            "ipsec_rx_failures": int,
                            "ipsec_encrypt_outbound": int,
                            "ipsec_tx_auth_failures": int,
                            "ipsec_tx_failures": int
                        },
                        Optional("pktdup"): {
                            "pktdup_rx": int,
                            "pktdup_rx_other": int,
                            "pktdup_rx_this": int,
                            "pktdup_tx": int,
                            "pktdup_tx_other": int,
                            "pktdup_capable": str
                        }
                    }
                }
            }
        }
    }


# =======================================================================
# Parser for 'show sdwan tunnel statistics',                            #
# 'show sdwan tunnel statistics bfd',                                   #
# 'show sdwan tunnel statistics fec',                                   #
# 'show sdwan tunnel statistics ipsec',                                 #
# 'show sdwan tunnel statistics pkt-dup'                                #
# 'show sdwan tunnel statistics table'                                  #
# =======================================================================
class ShowSdwanTunnelStatistics(ShowSdwanTunnelStatisticsSchema):
    """Parser for
          'show sdwan tunnel statistics'
          'show sdwan tunnel statistics bfd'
          'show sdwan tunnel statistics fec'
          'show sdwan tunnel statistics ipsec'
          'show sdwan tunnel statistics pkt-dup'
          'show sdwan tunnel statistics table'
    """
    cli_command = ['show sdwan tunnel statistics', 'show sdwan tunnel statistics {stats_type}']

    def cli(self, stats_type='', output=None):
        # if the user does not provide output to the parser
        # we need to get it from the device
        if output is None:
            if stats_type:
                output = self.device.execute(self.cli_command[1].format(stats_type=stats_type))
            else:
                output = self.device.execute(self.cli_command[0])

        # tunnel stats ipsec 150.0.5.1 150.0.6.1 12346 12346
        # tunnel stats ipsec 150.0.5.1 150.0.7.1 12346 12346
        p1 = re.compile(
            r'^tunnel\s+stats\s+(ipsec|gre)\s+(?P<source>[\S]+)\s+(?P<destination>[\S]+)'
            r'\s+(?P<src_port>[\d]+)\s+(?P<dst_port>[\d]+)$')

        # fec-rx-data-pkts     0
        # fec-tx-data-pkts     0
        # fec-capable          true
        # fec-dynamic          false
        p2 = re.compile(r'^(?P<key>[a-zA-Z0-9\-\_]+)\s+(?P<value>[a-zA-Z0-9\-\_]+)$')

        # # ipsec     150.0.5.1  151.0.1.1   12346   12346  21.0.0.21    public-internet  lte             1438    4303977    494629034    8004520    8312606388    1358    0             0               0             0               0                   0                     0                   0
        # # ipsec     150.0.5.1  151.0.2.1   12346   12346  22.0.0.22    public-internet  private2        1438    324964     28472293     324963     39521236      1358    0             0               0             0               0                   0                     0                   0
        p3 = re.compile(r'^(?P<protocol>[a-z]+)\s+(?P<src_ip>[a-zA-Z0-9\.\:]+)\s+(?P<dest_ip>[a-zA-Z0-9\.\:]+)\s+'
                        r'(?P<src_port>[\d]+)\s+(?P<dst_port>[\d]+)\s+'
                        r'(?P<remote_sys_ip>[\S]+)\s+(?P<local_color>[0-9a-zA-Z\-\_]+)'
                        r'\s+(?P<remote_color>[0-9a-zA-Z\-\_]+)\s+(?P<tunnel_mtu>[\d]+)\s+'
                        r'(?P<tx_pkts>[\d]+)\s+(?P<tx_octets>[\d]+)\s+'
                        r'(?P<rx_pkts>[\d]+)\s+(?P<rx_octets>[\d]+)\s+(?P<tcp_mss_adjust>[\d]+)\s+'
                        r'(?P<ipv6_tx_pkts>[\d]+)\s+(?P<ipv6_tx_octets>[\d]+)'
                        r'\s+(?P<ipv6_rx_pkts>[\d]+)\s+(?P<ipv6_rx_octets>[\d]+)\s+'
                        r'(?P<tx_ipv4_mcast_pkts>[\d]+)\s+(?P<tx_ipv4_mcast_octets>[\d]+)'
                        r'\s+(?P<rx_ipv4_mcast_pkts>[\d]+)\s+(?P<rx_ipv4_mcast_octets>[\d]+)$')

        ret_dict = {}
        for line in output.splitlines():
            # tun_dict = ret_dict.setdefault("tunnel",{})
            # tunnel stats ipsec 150.0.5.1 150.0.6.1 12346 12346
            # tunnel stats ipsec 150.0.5.1 150.0.7.1 12346 12346
            line = line.strip()
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                dest_dict = ret_dict.setdefault("tunnel", {}). \
                    setdefault(groups['source'], {}). \
                    setdefault('remote', {}). \
                    setdefault(groups['destination'], {})
                dest_dict.update({
                    "src_port": int(groups['src_port']),
                    "dst_port": int(groups['dst_port'])
                })
                continue
            # fec-rx-data-pkts     0
            # fec-tx-data-pkts     0
            # fec-capable          true
            # fec-dynamic          false
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                value = groups['value']
                # Here I am checking this numeric as i am iterating through
                # different keys/values and needs to assign it accordingly.
                key = groups['key']
                if value.isnumeric():
                    value = int(value)
                # dest_dict.update({groups['key'].replace(' ','_').replace('-','_').lower():value})
                if re.search("pktdup", key):
                    key_dict = dest_dict.setdefault("pktdup",{})
                    lst_dict_ptr = key_dict
                    lst_dict_ptr.update({key.replace(' ','_').replace('-','_').lower():value})
                elif re.search("ipsec", key):
                    key_dict = dest_dict.setdefault("ipsec",{})
                    lst_dict_ptr = key_dict
                    lst_dict_ptr.update({key.replace(' ','_').replace('-','_').lower():value})
                elif re.search("fec", key):
                    key_dict = dest_dict.setdefault("fec",{})
                    lst_dict_ptr = key_dict
                    lst_dict_ptr.update({key.replace(' ','_').replace('-','_').lower():value})
                elif re.search("bfd", key):
                    if re.search("echo", key):
                        key_dict = dest_dict.setdefault("bfd",{}).setdefault("echo",{})
                    else:
                        key_dict = dest_dict.setdefault("bfd",{}).setdefault("pmtu",{})
                    lst_dict_ptr = key_dict
                    lst_dict_ptr.update({key.replace(' ','_').replace('-','_').lower():value})
                elif re.search("ipv6_tx", key):
                    key_dict = dest_dict.setdefault("ipv6_tx",{})
                    lst_dict_ptr = key_dict
                    lst_dict_ptr.update({key.replace(' ','_').replace('-','_').lower():value})
                elif re.search("ipv6_rx", key):
                    key_dict = dest_dict.setdefault("ipv6_rx",{})
                    lst_dict_ptr = key_dict
                    lst_dict_ptr.update({key.replace(' ','_').replace('-','_').lower():value})
                elif re.search("tx", key):
                    key_dict = dest_dict.setdefault("tx",{})
                    lst_dict_ptr = key_dict
                    lst_dict_ptr.update({key.replace(' ','_').replace('-','_').lower():value})
                elif re.search("rx", key):
                    key_dict = dest_dict.setdefault("rx",{})
                    lst_dict_ptr = key_dict
                    lst_dict_ptr.update({key.replace(' ','_').replace('-','_').lower():value})
                else:
                    dest_dict.update({key.replace(' ','_').replace('-','_').lower():value})
                continue

            # ipsec     150.0.5.1  151.0.1.1   12346   12346  21.0.0.21    public-internet  lte             1438    4303977    494629034    8004520    8312606388    1358    0             0               0             0               0                   0                     0                   0
            # ipsec     150.0.5.1  151.0.2.1   12346   12346  22.0.0.22    public-internet  private2        1438    324964     28472293     324963     39521236      1358    0             0               0             0               0                   0                     0                   0
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                dest_dict = ret_dict.setdefault("tunnel",{}).\
                    setdefault(groups['src_ip'],{}).\
                    setdefault('remote',{}).\
                    setdefault(groups['dest_ip'],{})
                del groups['src_ip']
                del groups['dest_ip']
                for key in groups.keys():
                    value = groups[key]
                    # Check is Mandatory as i am iteratig through different key/values pairs
                    # of different types.
                    if groups[key].isnumeric():
                        value = int(groups[key])
                    if re.search("pktdup", key):
                        key_dict = dest_dict.setdefault("pktdup",{})
                        lst_dict_ptr = key_dict
                        lst_dict_ptr.update({key.replace(' ','_').replace('-','_').lower():value})
                    elif re.search("ipsec", key):
                        key_dict = dest_dict.setdefault("ipsec",{})
                        lst_dict_ptr = key_dict
                        lst_dict_ptr.update({key.replace(' ','_').replace('-','_').lower():value})
                    elif re.search("fec", key):
                        key_dict = dest_dict.setdefault("fec",{})
                        lst_dict_ptr = key_dict
                        lst_dict_ptr.update({key.replace(' ','_').replace('-','_').lower():value})
                    elif re.search("bfd", key):
                        if re.search("echo", key):
                            key_dict = dest_dict.setdefault("bfd",{}).setdefault("echo",{})
                        else:
                            key_dict = dest_dict.setdefault("bfd",{}).setdefault("pmtu",{})
                        lst_dict_ptr = key_dict
                        lst_dict_ptr.update({key.replace(' ','_').replace('-','_').lower():value})
                    elif re.search("ipv6_tx", key):
                        key_dict = dest_dict.setdefault("ipv6_tx",{})
                        lst_dict_ptr = key_dict
                        lst_dict_ptr.update({key.replace(' ','_').replace('-','_').lower():value})
                    elif re.search("ipv6_rx", key):
                        key_dict = dest_dict.setdefault("ipv6_rx",{})
                        lst_dict_ptr = key_dict
                        lst_dict_ptr.update({key.replace(' ','_').replace('-','_').lower():value})
                    elif re.search("tx", key):
                        key_dict = dest_dict.setdefault("tx",{})
                        lst_dict_ptr = key_dict
                        lst_dict_ptr.update({key.replace(' ','_').replace('-','_').lower():value})
                    elif re.search("rx", key):
                        key_dict = dest_dict.setdefault("rx",{})
                        lst_dict_ptr = key_dict
                        lst_dict_ptr.update({key.replace(' ','_').replace('-','_').lower():value})
                    else:
                        dest_dict.update({key.replace(' ','_').replace('-','_').lower():value})
                continue

        return ret_dict


# =======================================================================
# Parser Schema for 'show sdwan Tunnel sla'                             #
# 'show sdwan tunnel sla index <index>',                                #
# 'show sdwan tunnel sla name <name>',                                  #
# 'show sdwan tunnel remote-system-ip <ip> sla                          #
# =======================================================================
class ShowSdwanTunnelSlaSchema(MetaParser):
    schema = {
        'tunnel_sla_class': {
            Any(): { # Tunnel SLA Class Index/Name/System IP value
                Optional("sla_name") : str,
                Optional("sla_loss"): int,
                Optional("sla_latency"): int,
                Optional("sla_jitter"): int,
                Optional("tunnel_count") : int,
                Any(): { # Local TLOC IP
                    'remote': {
                        Any(): { # Remote TLOC IP
                            Optional("index") : int,
                            "protocol" : str,
                            "src_ip" : str,
                            "dst_ip" : str,
                            Optional("src_port") : int,
                            Optional("dst_port") : int,
                            Optional("remote_system_ip") : str,
                            Optional("t_local_color") : str,
                            Optional("t_remote_color") : str,
                            Optional("local_color") : str,
                            Optional("remote_color") : str,
                            Optional("mean_loss") : int,
                            Optional("mean_latency") : int,
                            Optional("mean_jitter") : int,
                            Optional("sla_class_index") : str,
                            "sla_class_name" : str,
                            Optional("fallback_sla_class_index") : str
                        }
                    }
                }
            }
        }
    }


# =======================================================================
# Parser for 'show sdwan tunnel sla',                                   #
# 'show sdwan tunnel sla index <index>',                                #
# 'show sdwan tunnel sla name <name>',                                  #
# 'show sdwan tunnel remote-system-ip <ip> sla                          #
# =======================================================================
class ShowSdwanTunnelSla(ShowSdwanTunnelSlaSchema):
    """Parser for
           'show sdwan tunnel sla'
           'show sdwan tunnel sla index <index>'
           'show sdwan tunnel sla name <name>'
           'show sdwan tunnel remote-system-ip <ip> sla'
    """
    cli_command = ['show sdwan tunnel sla',
                'show sdwan tunnel sla index {index}',
                'show sdwan tunnel sla name {name}',
                'show sdwan tunnel remote-system-ip {system_ip} sla']
    def cli(self, index='', name="", system_ip= "", output=None):
        # if the user does not provide output to the parser
        # we need to get it from the device
        if output is None:
            if index:
                output = self.device.execute(self.cli_command[1].format(index=index))
            elif name:
                output = self.device.execute(self.cli_command[2].format(name=name))
            elif system_ip:
                output = self.device.execute(self.cli_command[3].format(system_ip=system_ip))
            else:
                output = self.device.execute(self.cli_command[0])

        ret_dict = {}
        # tunnel sla-class 1
        p1 = re.compile(r'^tunnel\s+sla-class\s+(?P<sla_index>[0-9]+)$')
        # tunnel system-ips 23.0.0.23
        p1_1 = re.compile(r'^tunnel\s+system-ips\s+(?P<tunnel_system_ips>[0-9\.]+)$')
        #  sla-name    aarSla
        p2 = re.compile(r'^sla-name\s+(?P<sla_name>[\S]+)$')
        # sla-loss    3
        # sla-latency 150
        # sla-jitter  50
        # tunnel-count 4
        p3 = re.compile(r'^(?P<sla_key>[\S]+)\s+(?P<sla_value>[\d]+)$')
        # ipsec  150.0.4.1  29.129.29.1   12346  12366  29.0.0.29    blue   metro-ethernet   0     0        0       0,1    __all_tunnels__, aarSla  None
        p4 = re.compile(r'(?P<protocol>[a-z]+)\s+(?P<src_ip>[a-zA-Z0-9\.\:]+)\s+(?P<dst_ip>[a-zA-Z0-9\.\:]+)\s+(?P<src_port>[\d]+)\s+'
        '(?P<dst_port>[\d]+)\s+(?P<remote_system_ip>[\S]+)\s+(?P<t_local_color>[0-9a-zA-Z\-\_]+)\s+(?P<t_remote_color>[0-9a-zA-Z\-\_]+)'
        '\s+(?P<mean_loss>[\d]+)\s+(?P<mean_latency>[\d]+)\s+(?P<mean_jitter>[\d]+)\s+(?P<sla_class_index>[\S]+)\s+(?P<sla_class_name>[\S\s]+)'
        '\s+(?P<fallback_sla_class_index>[\S]+)$')
        # 0  ipsec  150.0.2.1  150.0.3.1  private1  biz-internet  __all_tunnels__, aarSla
        p4_1 = re.compile(r'^(?P<index>[0-9]+)\s+(?P<protocol>[a-z]+)\s+(?P<src_ip>[a-zA-Z0-9\.\:]+)\s+(?P<dst_ip>[a-zA-Z0-9\.\:]+)\s+'
        '(?P<local_color>[0-9a-zA-Z\-\_]+)\s+(?P<remote_color>[0-9a-zA-Z\-\_]+)\s+(?P<sla_class_name>[\S\s]+)$')

        for line in output.splitlines():
            line = line.strip()
            # tunnel sla-class 1
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                sla_index_dict = ret_dict.setdefault('tunnel_sla_class', {}).\
                    setdefault(groups['sla_index'],{})
                continue

            # tunnel system-ips 23.0.0.23
            m = p1_1.match(line)
            if m:
                groups = m.groupdict()
                sla_index_dict = ret_dict.setdefault('tunnel_sla_class', {}).\
                    setdefault(groups['tunnel_system_ips'],{})
                continue

            #  sla-name    aarSla
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                sla_index_dict.update({'sla_name':groups['sla_name']})
                continue

            # sla-loss    3
            # sla-latency 150
            # sla-jitter  50
            # tunnel-count 4
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                key = groups['sla_key'].lower().replace("-","_").replace(" ","_")
                sla_index_dict.update({key:int(groups['sla_value'])})
                continue

            # ipsec  150.0.4.1  29.129.29.1   12346  12366  29.0.0.29    blue   metro-ethernet   0     0        0       0,1    __all_tunnels__, aarSla  None
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                sla_index_dst_dict = sla_index_dict.setdefault(groups['src_ip'],{}).\
                    setdefault('remote',{}).\
                    setdefault(groups['dst_ip'],{})
                for key in groups.keys():
                    value = groups[key]
                    # Check is Mandatory as i am iterations through different key/values pairs
                    # of different types.
                    if groups[key].isnumeric():
                        value = int(groups[key])
                    sla_index_dst_dict.update({key:value})
                continue

            # 0  ipsec  150.0.2.1  150.0.3.1  private1  biz-internet  __all_tunnels__, aarSla
            m = p4_1.match(line)
            if m:
                groups = m.groupdict()
                sla_index_dst_dict = sla_index_dict.setdefault(groups['src_ip'],{}).\
                    setdefault('remote',{}).\
                    setdefault(groups['dst_ip'],{})
                for key in groups.keys():
                    value = groups[key]
                    # Check is Mandatory as i am iterations through different key/values pairs
                    # of different types.
                    if groups[key].isnumeric():
                        value = int(groups[key])
                    sla_index_dst_dict.update({key:value})
                continue

        return(ret_dict)

# =======================================================================
# Parser Schema for 'show sdwan app-route statistics'                   #
# I have made most of the keys as optional as it is common schema for   #
# 3-4 CLI commands as  listed below.                                    #
# =======================================================================
class ShowSdwanAppRouteStatisticsSchema(MetaParser):
    schema = {
        'approute': {
            Optional(str): { # Local System IP
                str: { # Remote System IP
                    "protocol": str,
                    "src_port": int,
                    "dst_port": int,
                    "remote_system_ip": str,
                    "local_color": str,
                    "remote_color": str,
                    "sla_class_index": str,
                    "fall_back_sla_index": str,
                    "app_probe_class_list" : {
                        str: { # App Probe Class Name/Index
                            "mean_loss": int,
                            "mean_latency": int,
                            "mean_jitter": int,
                            "interval" : {
                                str: { # Interval Value
                                    "total_packets": int,
                                    "loss": int,
                                    "average_latency": int,
                                    "average_jitter": int,
                                    "tx_data_pkts": int,
                                    "rx_data_pkts": int,
                                    "ipv6_tx_data_pkts": int,
                                    "ipv6_rx_data_pkts": int
                                }
                            }
                        }
                    }
                }
            }
        }
    }

# =======================================================================
# Parser for                                                            #
# 'show sdwan app-route stats local-color <color>',                     #
# 'show sdwan app-route stats remote-color <color>',                    #
# 'show sdwan app-route stats remote-system-ip <ip>',                   #
# =======================================================================
class ShowSdwanAppRouteStatistics(ShowSdwanAppRouteStatisticsSchema):
    """Parser for
        'show sdwan app-route stats local-color <color>'
        'show sdwan app-route stats remote-color <color>'
        'show sdwan app-route stats remote-system-ip <ip>'
    """
    cli_command = ['show sdwan app-route stats {color_type} {color}',
            'show sdwan app-route stats remote-system-ip {system_ip}',
            'show sdwan app-route stats']
    def cli(self, color_type = "", color= "", system_ip= "", output=None):
        # if the user does not provide output to the parser
        # we need to get it from the device
        if output is None:
            if color_type and color:
                cmd = self.cli_command[0].format(color_type=color_type,color=color)
            elif system_ip:
                cmd = self.cli_command[1].format(system_ip=system_ip)
            else:
                cmd = self.cli_command[2]
            output = self.device.execute(cmd)

        # app-route statistics 150.0.5.1 150.0.6.1 12346 12346
        # app-route statistics 150.0.5.1 150.0.7.1 12346 12346
        p1 = re.compile(r'^app-route\s+statistics\s+(?P<source>[\S]+)\s+(?P<destination>[\S]+)\s+(?P<protocol>[a-zA-Z]+)\s+'
        '(?P<src_port>[\d]+)\s+(?P<dst_port>[\d]+)$')

        # app-probe-class-list None
        p1_1 = re.compile(r'^app-probe-class-list\s+(?P<app_probe_name>[\S]+)$')

        # interval 0
        # interval 1
        p1_2 = re.compile(r'^interval\s+(?P<interval>[0-9]+)$')

        #  remote-system-ip         20.0.0.20
        p2 = re.compile(r'^remote-system-ip\s+(?P<remote_system_ip>[\S]+)')

        #  local-color              blue
        p3 = re.compile(r'^local-color\s+(?P<local_color>[\S]+)$')

        #  remote-color             bronze
        p4 = re.compile(r'^remote-color\s+(?P<remote_color>[\S]+)$')

        #  sla-class-index          0,1
        p5 = re.compile(r'^sla-class-index\s+(?P<sla_class_index>[\S]+)$')

        #  fallback-sla-class-index None
        p6 = re.compile(r'^fallback-sla-class-index\s+(?P<fall_back_sla_index>[\S]+)$')

        #  total-packets     638
        #  loss              0
        #  average-latency   1
        #  average-jitter    1
        #  tx-data-pkts      0
        #  rx-data-pkts      0
        #  ipv6-tx-data-pkts 0
        #  ipv6-rx-data-pkts 0
        p7 = re.compile(r'^(?P<key>[\S]+)\s+(?P<value>[0-9]+)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()
            # app-route statistics 150.0.5.1 150.0.6.1 12346 12346
            # app-route statistics 150.0.5.1 150.0.7.1 12346 12346
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                dest_dict = ret_dict.setdefault("approute",{}).\
                    setdefault(groups['source'],{}).\
                    setdefault(groups['destination'],{})
                last_dict_ptr = dest_dict
                last_dict_ptr.update({"protocol":groups['protocol'],
                    "src_port":int(groups['src_port']),
                    "dst_port":int(groups['dst_port'])})
                continue

            # app-probe-class-list None
            m = p1_1.match(line)
            if m:
                groups = m.groupdict()
                app_probe_dict = dest_dict.setdefault("app_probe_class_list",{})
                app_probe_name_dict = app_probe_dict.setdefault(groups['app_probe_name'],{})
                last_dict_ptr  =  app_probe_name_dict
                continue

            # interval 0
            # interval 1
            m = p1_2.match(line)
            if m:
                groups = m.groupdict()
                interval_dict = app_probe_name_dict.setdefault("interval",{})
                interval_val_dict = interval_dict.setdefault(groups['interval'],{})
                last_dict_ptr  =  interval_val_dict
                continue

            #  remote-system-ip         20.0.0.20
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                for key in groups.keys():
                    key = key.replace(' ','_').replace('-','_').lower()
                value = groups[key]
                last_dict_ptr.update({key:value})
                continue

            #  local-color              blue
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                for key in groups.keys():
                    key = key.replace(' ','_').replace('-','_').lower()
                value = groups[key]
                last_dict_ptr.update({key:value})
                continue

            #  remote-color             bronze
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                for key in groups.keys():
                    key = key.replace(' ','_').replace('-','_').lower()
                value = groups[key]
                last_dict_ptr.update({key:value})
                continue

            #  sla-class-index          0,1
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                for key in groups.keys():
                    key = key.replace(' ','_').replace('-','_').lower()
                value = groups[key]
                last_dict_ptr.update({key:value})

            #  fallback-sla-class-index None
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                for key in groups.keys():
                    key = key.replace(' ','_').replace('-','_').lower()
                value = groups[key]
                last_dict_ptr.update({key:value})
                continue

            #  total-packets     638
            #  loss              0
            #  average-latency   1
            #  average-jitter    1
            #  tx-data-pkts      0
            #  rx-data-pkts      0
            #  ipv6-tx-data-pkts 0
            #  ipv6-rx-data-pkts 0
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                last_dict_ptr.update({groups['key'].replace(' ','_').replace('-','_').lower():int(groups['value'])})
                continue

        return ret_dict

# =======================================================================
# Parser Schema for 'show sdwan app-route sla-class'                    #
# Parser Schema for 'show sdwan app-route sla-class name <name>'        #
# I have made some of the keys as optional as it is common schema for   #
# both CLI commands as listed above.                                    #
# =======================================================================
class ShowSdwanAppRouteSlaClassSchema(MetaParser):
    schema = {
        'sla_class': {
            Any(): { # Sla Class Index/Name
                "name": str,
                "loss": int,
                "latency": int,
                "jitter": int,
                Optional("class_id"): int,
                Optional("app_probe_class"): str,
                Optional("app_probe_class_id"): int,
                Optional("app_probe_class"): str,
                "fallback_best_tunnel": str
            }
        }
    }

# =======================================================================
# Parser Schema for 'show sdwan app-route sla-class'                    #
# Parser Schema for 'show sdwan app-route sla-class name <name>'        #
# I have made some of the keys as optional as it is common schema for   #
# both CLI commands as listed above.                                    #
# =======================================================================
class ShowSdwanAppRouteSlaClass(ShowSdwanAppRouteSlaClassSchema):
    """Parser for
        'show sdwan app-route sla-class'
        'show sdwan app-route sla-class name <name>'
    """
    cli_command = ['show sdwan app-route sla-class', 'show sdwan app-route sla-class name {name}']
    def cli(self, name = "", output=None):
        # if the user does not provide output to the parser
        # we need to get it from the device
        if output is None:
            if name:
                output = self.device.execute(self.cli_command[1].format(name=name))
            else:
                output = self.device.execute(self.cli_command[0])

        # 0       __all_tunnels__       0     0        0        0          None                  None
        p1 = re.compile(r'^(?P<index>[0-9]+)\s+(?P<name>[\S]+)\s+(?P<loss>[\d]+)\s+(?P<latency>[\d]+)\s+(?P<jitter>[\d]+)'
        '\s+(?P<class_id>[\d]+)\s+(?P<app_probe_class>[\S]+)\s+(?P<fallback_best_tunnel>[\S]+)$')

        # app-route sla-class 1
        p2 = re.compile(r'^app-route\s+sla-class\s+(?P<index>[\d]+)$')

        #  name                 aarSla
        #  loss                 3
        #  latency              150
        #  jitter               50
        #  app-probe-class-id   0
        #  app-probe-class      None
        #  fallback-best-tunnel Latency
        p3 = re.compile(r'^(?P<key>[a-z\-]+)\s+(?P<value>[\S]+)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # 0       __all_tunnels__       0     0        0        0          None                  None
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                index = groups['index']
                index_dict = ret_dict.setdefault("sla_class",{}).setdefault(index,{})
                last_dict_ptr = index_dict
                del groups['index']
                for key in groups.keys():
                    value = groups[key]
                    key = key.lower().replace("-","_").replace(" ","_")
                    # Check is mandatory as i am iterating it through different keys/key-value pairs.
                    if value.isnumeric():
                        value = int(value)
                    last_dict_ptr.update({key:value})
                continue

            # app-route sla-class 1
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                index = groups['index']
                index_dict = ret_dict.setdefault("sla_class",{}).setdefault(index,{})
                last_dict_ptr = index_dict
                continue

            #  name                 aarSla
            #  loss                 3
            #  latency              150
            #  jitter               50
            #  app-probe-class-id   0
            #  app-probe-class      None
            #  fallback-best-tunnel Latency
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                value = groups['value']
                # Check is mandatory as i am iterating it through different keys/key-value pairs.
                if value.isnumeric():
                    value = int(value)
                last_dict_ptr.update({groups['key'].replace(' ','_').replace('-','_').lower():value})
                continue

        return(ret_dict)


# ===========================================
# Parser for 'show sdwan control connections history'
# ===========================================
class ShowSdwanControlConnectionHistory(ShowControlConnectionHistory_viptela):
    """ Parser for "show sdwan control connections history" """
    cli_command = 'show sdwan control connection-history'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        return super().cli(output=output)

# =======================================================================
# Parser Schema for 'show sdwan app-fwd dpi summary'
# =======================================================================
class ShowSdwanAppFwdDpiSummarySchema(MetaParser):
    """Schema for:
        show sdwan app-fwd dpi summary"""

    schema = {
        "name": {
            Any(): {
                "cache_size": int,
                "current_entries": int,
                "high_watermark": int,
                "flows_added": int,
                "flows_aged": int,
                "active_flows_timed_out": int,
                "inactive_flows_timed_out": int
            },
        },
    }

# =============================================
# Parser for 'show sdwan app-fwd dpi summary'
# =============================================

class ShowSdwanAppFwdDpiSummary(ShowSdwanAppFwdDpiSummarySchema):
    """parser for "show sdwan app-fwd dpi summary" """

    cli_command = "show sdwan app-fwd dpi summary"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        keys = ["cache_size", "current_entries", "high_watermark", "flows_added", "flows_aged",
                "active_flows_timed_out", "inactive_flows_timed_out"]

        #                                                             ACTIVE   INACTIVE
        #															  FLOWS    FLOWS
        #					 CACHE   CURRENT  HIGH       FLOWS  FLOWS  TIMED    TIMED
        # NAME                SIZE    ENTRIES  WATERMARK  ADDED  AGED   OUT      OUT
        # --------------------------------------------------------------------------------
        # sdwan_flow_monitor  512000   0        7          1590   1591   1355    236
        # sdwan_flow_monitor_2  5120   3        6          1570   1596   1358    2367

        p1 = re.compile(r"(?P<name>[a-z]+\S+)+\s+(?P<cache_size>\d+)+\s+(?P<current_entries>\d+)+\s+"
                        r"(?P<high_watermark>\d+)+\s+(?P<flows_added>\d+)+\s+(?P<flows_aged>\d+)+\s+"
                        r"(?P<active_flows_timed_out>\d+)+\s+(?P<inactive_flows_timed_out>\d+)")

        for line in output.splitlines():
            line = line.strip()

            # sdwan_flow_monitor  512000   0        7          1590   1591   1355    236
            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = group.pop("name")

                name_dict = parsed_dict.setdefault("name", {}). \
                    setdefault(name, {})

                name_dict.update({k: int(v) for k, v in group.items()})
        return parsed_dict

# =======================================================================
# Parser Schema for 'show sdwan app-fwd cflowd statistics'
# =======================================================================

class ShowSdwanAppfwdCflowdStatisticsSchema(MetaParser):

    """Schema for "show sdwan app-fwd cflowd statistics" """

    schema = {
            'data_packets': int,
            'template_packets': int,
            'total_packets': int,
            'flow_refresh': int,
            'flow_ageout': int,
            'flow_end_detected': int,
            'flow_end_forced': int,
            'flow_rate_limit_drop': int,
    }

# ==============================================
# Parser for 'show sdwan app-fwd cflowd statistics'
# ==============================================

class ShowSdwanAppfwdCflowdStatistics(ShowSdwanAppfwdCflowdStatisticsSchema):
    """ parser for "show sdwan app-fwd cflowd statistics" """

    cli_command = "show sdwan app-fwd cflowd statistics"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # data_packets             :      1371257
        p1 = re.compile(r'^data_packets\s+:+\s+(?P<data_packets>\d+)$')

        # template_packets         :      5345
        p2 = re.compile(r'^template_packets\s+:+\s+(?P<template_packets>\d+)$')

        # total-packets            :      57938
        p3 = re.compile(r'^total-packets\s+:+\s+(?P<total_packets>\d+)$')

        # flow-refresh             :      31713
        p4 = re.compile(r'^flow-refresh\s+:+\s+(?P<flow_refresh>\d+)$')

        # flow-ageout              :      18416
        p5 = re.compile(r'^flow-ageout\s+:+\s+(?P<flow_ageout>\d+)$')

        # flow-end-detected        :      0
        p6 = re.compile(r'^flow-end-detected\s+:+\s+(?P<flow_end_detected>\d+)$')

        # flow-end-forced          :      0
        p7 = re.compile(r'^flow-end-forced\s+:+\s+(?P<flow_end_forced>\d+)$')

        # flow-rate-limit-drop     :      0
        p8 = re.compile(r'^flow-rate-limit-drop\s+:+\s+(?P<flow_rate_limit_drop>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # data_packets             :      1371257
            m = p1.match(line)
            if m:
                group = m.groupdict()
                data_packets = int(group['data_packets'])
                ret_dict['data_packets'] = data_packets

            # template_packets         :      5345
            m = p2.match(line)
            if m:
                group = m.groupdict()
                template_packets = int(group['template_packets'])
                ret_dict['template_packets'] = template_packets

            # total-packets            :      57938
            m = p3.match(line)
            if m:
                group = m.groupdict()
                total_packets = int(group['total_packets'])
                ret_dict['total_packets'] = total_packets

            # flow-refresh             :      31713
            m = p4.match(line)
            if m:
                group = m.groupdict()
                flow_refresh = int(group['flow_refresh'])
                ret_dict['flow_refresh'] = flow_refresh

            # flow-ageout              :      18416
            m = p5.match(line)
            if m:
                group = m.groupdict()
                flow_ageout = int(group['flow_ageout'])
                ret_dict['flow_ageout'] = flow_ageout

            # flow-end-detected        :      0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                flow_end_detected = int(group['flow_end_detected'])
                ret_dict['flow_end_detected'] = flow_end_detected

            # flow-end-forced          :      0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                flow_end_forced = int(group['flow_end_forced'])
                ret_dict['flow_end_forced'] = flow_end_forced

            # flow-rate-limit-drop     :      0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                flow_rate_limit_drop = int(group['flow_rate_limit_drop'])
                ret_dict['flow_rate_limit_drop'] = flow_rate_limit_drop

        return ret_dict

# =============================================
# Parser Schema for 'show sdwan app-fwd cflowd flow-count'
# =============================================
class ShowSdwanAppfwdCflowdFlowCountSchema(MetaParser):
    """Schema for "show sdwan app-fwd cflowd flow-count" """

    schema = {
        "vpn": {
            Any(): {
                "count": int
            },
        },
    }

# ==============================================
# Parser for 'show sdwan app-fwd cflowd flow-count'
# ==============================================

class ShowSdwanAppfwdCflowdFlowCount(ShowSdwanAppfwdCflowdFlowCountSchema):
    """ parser for "show sdwan app-fwd cflowd flow-count" """

    cli_command = "show sdwan app-fwd cflowd flow-count"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        vpn_dict = {}

        # *    2
        p1 = re.compile(r'^(?P<vpn>.+?)\s+(?P<count>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # *    2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vpn = group['vpn']
                count = int(group['count'])
                name_dict = vpn_dict.setdefault('vpn', {}).setdefault(vpn, {})
                name_dict.update({'count': count})

        return vpn_dict

# =============================================
# Parser Schema for 'show sdwan app-hosting oper-data'
# =============================================
class ShowSdwanAppHostingOperDataSchema(MetaParser):
    """Schema for "show sdwan app-hosting oper-data" """

    schema = {
            'app_hosting_oper_data_app': {
                Any(): {
                    'state': str,
                    'pkg_info_name': str,
                    'pkg_info_path': str,
                    'app_name': str,
                    'pkg_version': str,
                    'pkg_desc_name': str,
                    'pkg_app_type': str,
                    'pkg_app_owner': str,
                    'app_act_allowed': str,
                    'pkg_app_author': str,
                    'pkg_info_key_type': str,
                    'pkg_info_method': str,
                    'pkg_lic_name': str,
                    'pkg_lic_version': str,
                    'processes_name': str,
                    'processes_status': str,
                    'processes_pid': str,
                    'processes_uptime': str,
                    'processes_memory': str,
                    'profile_name': str,
                    'disk': str,
                    'memory': str,
                    'cpu': str,
                    'vcpu': str,
                    'cpu_percent': str,
                    'guest_intf': str,
                    'res_add_state': str,
                    'res_add_disk_space': str,
                    'res_add_memory': str,
                    'res_add_cpu': str,
                    'res_add_vcpu': str,
                    'res_doc_run_opts': str,
                    'details_command': str,
                    'details_entry_point': str,
                    'details_health_stats': str,
                    'details_probe_error': str,
                    'details_probe_output': str,
                    'details_pkg_run_opt': str,
                    'ieobc_mac_address': str,
                    'utilization_name': str,
                    'req_app_util': str,
                    'actual_app_util': str,
                    'cpu_state': str,
                    'mem_allocation': str,
                    'mem_used': str
                }
            },
            'name': {
                Any(): {
                    'alias': str,
                    'rx_packets': str,
                    'rx_bytes': str,
                    'rx_errors': str,
                    'tx_packets': str,
                    'tx_bytes': str,
                    'tx_errors': str
                }
            },
            'storage_utils_storage_util_disk': {
                'alias': str,
                'rd_bytes': str,
                'rd_requests': str,
                'errors': str,
                'wr_bytes': str,
                'wr_requests': str,
                'capacity': str,
                'available': str,
                'used': str,
                'usage': str,
                'pkg_policy': str
            },
            'mac_address': {
                Any(): {
                    'attached_intf': str,
                    'ipv4_address': str,
                    'network_name': str,
                    'ipv6_address': str
                }
            },
            'app_hosting_oper_data_app_resources_global': {
                Any(): {
                    'quota': str,
                    'available': str,
                    Optional('quota_unit'): str,
                    Optional('available_unit'): str
                }
            },
            'app_notifications_event': {
                'timestamp': str,
                'severity_level': str,
                'host_name': str,
                'vrf_name': str,
                'app_id': str,
                'ev_type': str,
                'status': str,
                'app_state': str,
                'is_enabled': str
            }
        }

# ==============================================
# Parser for 'show sdwan app-hosting oper-data'
# ==============================================

class ShowSdwanAppHostingOperData(ShowSdwanAppHostingOperDataSchema):
    """ parser for "show sdwan app-hosting oper-data" """

    cli_command = "show sdwan app-hosting oper-data"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        oper_data_dict = {}
        # app-hosting-oper-data app utd
        p1 = re.compile(r'^app-hosting-oper-data\sapp\s(?P<app>\w+)$')

        #  details state            RUNNING
        p2 = re.compile(r'^details\sstate\s+(?P<state>\w+)$')

        #  details package-information name UTD-Snort-Feature
        p3 = re.compile(r'^details\spackage-information\sname\s+(?P<pkg_info_name>[A-Za-z-]+)$')

        #  details package-information path /bootflash/.UTD_IMAGES/iox-utd_1.0.4_SV2.9.16.1_XE17.7.tar
        p4 = re.compile(r'^details\spackage-information\spath\s+(?P<pkg_info_path>[A-Za-z0-9-\/._]+)$')

        # details package-information application name utd
        p5 = re.compile(r'^details\spackage-information\sapplication\sname\s+(?P<app_name>\w+)$')

        # details package-information application installed-version 1.0.4_SV2.9.16.1_XE17.7
        p6 = re.compile(
            r'^details\spackage-information\sapplication\sinstalled-version\s+(?P<pkg_version>[A-Z0-9._]+$)')

        #  details package-information application description "Unified Threat Defense"
        p7 = re.compile(r'^details\spackage-information\sapplication\sdescription\s+(?P<pkg_desc_name>\"[A-Za-z ]+\")$')

        # details package-information application type LXC
        p8 = re.compile(r'^details\spackage-information\sapplication\stype\s+(?P<pkg_app_type>\w+)$')

        #  details package-information application owner ioxm
        p9 = re.compile(r'^details\spackage-information\sapplication\sowner\s+(?P<pkg_app_owner>\w+)$')

        # details package-information application activation-allowed true
        p10 = re.compile(r'^details\spackage-information\sapplication\sactivation-allowed\s+(?P<app_act_allowed>\w+)$')

        # details package-information application author ""
        p11 = re.compile(r'^details\spackage-information\sapplication\sauthor\s+(?P<pkg_app_author>\S+)$')

        # details package-information signing key-type ""
        p12 = re.compile(r'^details\spackage-information\ssigning\skey-type\s+(?P<pkg_info_key_type>\S+)$')

        # details package-information signing method ""
        p13 = re.compile(r'^details\spackage-information\ssigning\smethod\s+(?P<pkg_info_method>\S+)$')

        # details package-information licensing name ""
        p14 = re.compile(r'^details\spackage-information\slicensing\sname\s+(?P<pkg_lic_name>\S+)$')

        # details package-information licensing version ""
        p15 = re.compile(r'^details\spackage-information\slicensing\sversion\s+(?P<pkg_lic_version>\S+)$')

        # details package-information url-path ""
        p16 = re.compile(r'^details\spackage-information\slurl-path\s+(?P<pkg_url_path>\S+)$')

        # details detailed-guest-status processes name ""
        p17 = re.compile(r'^details\sdetailed-guest-status\sprocesses\sname\s+(?P<processes_name>\S+)$')

        # details detailed-guest-status processes status ""
        p18 = re.compile(r'^details\sdetailed-guest-status\sprocesses\sstatus\s+(?P<processes_status>\S+)$')

        # details detailed-guest-status processes pid ""
        p19 = re.compile(r'^details\sdetailed-guest-status\sprocesses\spid\s+(?P<processes_pid>\S+)$')

        # details detailed-guest-status processes uptime ""
        p20 = re.compile(r'^details\sdetailed-guest-status\sprocesses\suptime\s+(?P<processes_uptime>\S+)$')

        # details detailed-guest-status processes memory ""
        p21 = re.compile(r'^details\sdetailed-guest-status\sprocesses\smemory\s+(?P<processes_memory>\S+)$')

        # details activated-profile-name cloud-medium
        p22 = re.compile(r'^details\sactivated-profile-name\s+(?P<profile_name>[a-z-]+)$')

        # details resource-reservation disk 1111
        p23 = re.compile(r'^details\sresource-reservation\sdisk\s+(?P<disk>\d+)$')

        # details resource-reservation memory 3072
        p24 = re.compile(r'^details\sresource-reservation\smemory\s+(?P<memory>\d+)$')

        # details resource-reservation cpu 0
        p25 = re.compile(r'^details\sresource-reservation\scpu\s+(?P<cpu>\d+)$')

        # details resource-reservation vcpu 0
        p26 = re.compile(r'^details\sresource-reservation\svcpu\s+(?P<vcpu>\d+)$')

        # details resource-reservation cpu-percent 50
        p27 = re.compile(r'^details\sresource-reservation\scpu-percent\s+(?P<cpu_percent>\d+)$')

        # details guest-interface  ""
        p28 = re.compile(r'^details\sguest-interface\s+(?P<guest_intf>\S+)$')

        # details resource-admission state ""
        p29 = re.compile(r'^details\sresource-admission\sstate\s+(?P<res_add_state>\S+)$')

        # details resource-admission disk-space ""
        p30 = re.compile(r'^details\sresource-admission\sdisk-space\s+(?P<res_add_disk_space>\S+)$')

        # details resource-admission memory ""
        p31 = re.compile(r'^details\sresource-admission\smemory\s+(?P<res_add_memory>\S+)$')

        # details resource-admission cpu 0
        p32 = re.compile(r'^details\sresource-admission\scpu\s+(?P<res_add_cpu>\S+)$')

        # details resource-admission vcpus ""
        p33 = re.compile(r'^details\sresource-admission\svcpus\s+(?P<res_add_vcpu>\S+)$')

        # details docker-run-opts  ""
        p34 = re.compile(r'^details\sdocker-run-opts\s+(?P<res_doc_run_opts>\S+)$')

        # details command          ""
        p35 = re.compile(r'^details\scommand\s+(?P<details_command>\S+)$')

        # details entry-point      ""
        p36 = re.compile(r'^details\sentry-point\s+(?P<details_entry_point>\S+)$')

        # details health-status    0
        p37 = re.compile(r'^details\shealth-status\s+(?P<details_health_stats>\S+)$')

        # details last-health-probe-error ""
        p38 = re.compile(r'^details\slast-health-probe-error\s+(?P<details_probe_error>\S+)$')

        # details last-health-probe-output ""
        p39 = re.compile(r'^details\slast-health-probe-output\s+(?P<details_probe_output>\S+)$')

        # details pkg-run-opt      ""
        p40 = re.compile(r'^details\spkg-run-opt\s+(?P<details_pkg_run_opt>\S+)$')

        # details ieobc-mac-addr   33:33:3a:33:33:3a
        p41 = re.compile(r'^details\sieobc-mac-addr\s+(?P<ieobc_mac_address>([0-9a-fA-F].?){12})$')

        # utilization name utd
        p42 = re.compile(r'^utilization\sname\s+(?P<utilization_name>\w+)$')

        # utilization cpu-util requested-application-util 0
        p43 = re.compile(r'^utilization\scpu-util\srequested-application-util\s+(?P<req_app_util>\w+)$')

        # utilization cpu-util actual-application-util 3
        p44 = re.compile(r'^utilization\scpu-util\sactual-application-util\s+(?P<actual_app_util>\w+)$')

        # utilization cpu-util cpu-state ""
        p45 = re.compile(r'^utilization\scpu-util\scpu-state\s+(?P<cpu_state>\S+)$')

        # utilization memory-util memory-allocation 3072
        p46 = re.compile(r'^utilization\smemory-util\smemory-allocation\s+(?P<mem_allocation>\S+)$')

        # utilization memory-util memory-used 335636
        p47 = re.compile(r'^utilization\smemory-util\smemory-used\s+(?P<mem_used>\S+)$')

        #                     RX       RX     RX      TX       TX     TX
        #   NAME     ALIAS  PACKETS  BYTES  ERRORS  PACKETS  BYTES  ERRORS
        #   ----------------------------------------------------------------
        #   dp_1_0   net2   0        0      0       30       1260   0
        #   dp_1_1   net3   0        0      0       0        0      0
        #   ieobc_1  ieobc  190      11175  0       190      12303  0

        p48 = re.compile(
            r'(?P<name>[a-z0-9_]+)+\s+(?P<alias>\w+)+\s+(?P<rx_packets>\d+)+\s+(?P<rx_bytes>\d+)+\s+(?P<rx_errors>\d+)+\s+(?P<tx_packets>\d+)+\s+(?P<tx_bytes>\d+)+\s+(?P<tx_errors>\d+)')

        # storage-utils storage-util disk
        p49 = re.compile(r'^storage-utils\sstorage-util\sdisk')

        # alias       ""
        p50 = re.compile(r'^alias\s+(?P<alias>\S+)$')

        #   rd-bytes    0
        p51 = re.compile(r'^rd-bytes\s+(?P<rd_bytes>\d+)$')

        #   rd-requests 0
        p52 = re.compile(r'^rd-requests\s+(?P<rd_requests>\d+)$')

        #   errors      0
        p53 = re.compile(r'^errors\s+(?P<errors>\d+)$')

        #   wr-bytes    0
        p54 = re.compile(r'^wr-bytes\s+(?P<wr_bytes>\d+)$')

        #   wr-requests 0
        p55 = re.compile(r'^wr-requests\s+(?P<wr_requests>\d+)$')

        #   capacity    1137664
        p56 = re.compile(r'^capacity\s+(?P<capacity>\d+)$')

        #   available   255382
        p57 = re.compile(r'^available\s+(?P<available>\d+)$')

        #   used        882282
        p58 = re.compile(r'^used\s+(?P<used>\d+)$')

        #   usage       ""
        p59 = re.compile(r'^usage\s+(?P<usage>\S+)$')

        #                ATTACHED   IPV4       NETWORK  IPV6
        # MAC ADDRESS        str     ERFACE  ADDRESS    NAME     ADDRESS
        # -----------------------------------------------------------
        # 54:0e:00:0b:0c:02  eth0       0.0.0.0    ieobc_1  ::
        # f8:6b:d9:c0:cc:5e  eth2       0.0.0.0    dp_1_0   ::
        # f8:6b:d9:c0:cc:5f  eth1       192.0.2.2  dp_1_1   ::

        p60 = re.compile(
            r'^(?P<mac_address>([0-9a-fA-F].?){12})+\s+(?P<attached_intf>\w+)+\s+(?P<ipv4_address>[0-9.]+)+\s+(?P<network_name>\w+)+\s+(?P<ipv6_address>\S+)$')

        # pkg-policy iox-pkg-policy-invalid
        p61 = re.compile(r'^pkg-policy\s+(?P<pkg_policy>\S+)$')

        # app-hosting-oper-data app-resources global
        p62 = re.compile(r'^app-hosting-oper-data\sapp-resources\sglobal')

        # cpu "system CPU"
        p63 = re.compile(r'^cpu\s+(?P<cpu>\"[A-Za-z ]+\")$')

        # quota          98
        p64 = re.compile(r'^quota\s+(?P<quota>\S+)$')

        # available      48
        p65 = re.compile(r'^available\s+(?P<available>\d+)$')

        # quota-unit     48608
        p66 = re.compile(r'^quota-unit\s+(?P<quota_unit>\S+)$')

        # available-unit 23808
        p67 = re.compile(r'^available-unit\s+(?P<available_unit>\S+)$')

        # memory memory
        p68 = re.compile(r'^memory\s+(?P<memory>\S+)$')

        # storage-device harddisk
        p69 = re.compile(r'^storage-device\s+(?P<storage_device>harddisk)$')

        # storage-device bootflash
        p70 = re.compile(r'^storage-device\s+(?P<storage_device>bootflash)$')

        # storage-device volume-group
        p71 = re.compile(r'^storage-device\s+(?P<storage_device>volume-group)$')

        # storage-device "CAF persist-disk"
        p72 = re.compile(r'^storage-device\s+(?P<storage_device>\"[A-Za-z -]+\")$')

        # timestamp      2022-04-25T18:08:36.189866+00:00
        p73 = re.compile(r'^timestamp\s+(?P<timestamp>\S+)$')

        # severity-level minor
        p74 = re.compile(r'^severity-level\s+(?P<severity_level>\w+)$')

        # host-name      pm9005
        p75 = re.compile(r'^host-name\s+(?P<host_name>\w+)$')

        # vrf-name       ""
        p76 = re.compile(r'^vrf-name\s+(?P<vrf_name>\S+)$')

        # app-id         utd
        p77 = re.compile(r'^app-id\s+(?P<app_id>\w+)$')

        # ev-type        im-iox-enable
        p78 = re.compile(r'^ev-type\s+(?P<ev_type>\S+)$')

        # status         im-app-pass
        p79 = re.compile(r'^status\s+(?P<status>\S+)$')

        # app-state      im-state-running
        p80 = re.compile(r'^app-state\s+(?P<app_state>[a-z-]+)$')

        # app-hosting-oper-data app-globals iox-enabled true
        p81 = re.compile(r'^app-hosting-oper-data\sapp-globals+\siox-enabled+\s+(?P<is_enabled>\w+)$')

        for line in output.splitlines():
            line = line.strip()

            # app-hosting-oper-data app utd
            m = p1.match(line)
            if m:
                group = m.groupdict()
                app = group['app']
                app_dict = oper_data_dict.setdefault('app_hosting_oper_data_app', {}).setdefault(app, {})
                continue

            # details state            RUNNING
            m = p2.match(line)
            if m:
                group = m.groupdict()
                state = group['state']
                app_dict['state'] = state
                continue

            # details package-information name UTD-Snort-Feature
            m = p3.match(line)
            if m:
                group = m.groupdict()
                pkg_info_name = group['pkg_info_name']
                app_dict['pkg_info_name'] = pkg_info_name
                continue

            # details package-information path /bootflash/.UTD_IMAGES/iox-utd_1.0.4_SV2.9.16.1_XE17.7.tar
            m = p4.match(line)
            if m:
                group = m.groupdict()
                pkg_info_path = group['pkg_info_path']
                app_dict['pkg_info_path'] = pkg_info_path
                continue

            # details package-information application name utd
            m = p5.match(line)
            if m:
                group = m.groupdict()
                app_name = group['app_name']
                app_dict['app_name'] = app_name
                continue

            # details package-information application installed-version 1.0.4_SV2.9.16.1_XE17.7
            m = p6.match(line)
            if m:
                group = m.groupdict()
                pkg_version = group['pkg_version']
                app_dict['pkg_version'] = pkg_version
                continue

            # details package-information application description "Unified Threat Defense"
            m = p7.match(line)
            if m:
                group = m.groupdict()
                pkg_desc_name = group['pkg_desc_name']
                app_dict['pkg_desc_name'] = pkg_desc_name
                continue

            # details package-information application type LXC
            m = p8.match(line)
            if m:
                group = m.groupdict()
                pkg_app_type = group['pkg_app_type']
                app_dict['pkg_app_type'] = pkg_app_type
                continue

            # details package-information application owner ioxm
            m = p9.match(line)
            if m:
                group = m.groupdict()
                pkg_app_owner = group['pkg_app_owner']
                app_dict['pkg_app_owner'] = pkg_app_owner
                continue

            # details package-information application activation-allowed true
            m = p10.match(line)
            if m:
                group = m.groupdict()
                app_act_allowed = group['app_act_allowed']
                app_dict['app_act_allowed'] = app_act_allowed
                continue

            # details package-information application author ""
            m = p11.match(line)
            if m:
                group = m.groupdict()
                pkg_app_author = group['pkg_app_author']
                app_dict['pkg_app_author'] = pkg_app_author
                continue

            # details package-information signing key-type ""
            m = p12.match(line)
            if m:
                group = m.groupdict()
                pkg_info_key_type = group['pkg_info_key_type']
                app_dict['pkg_info_key_type'] = pkg_info_key_type
                continue

            # details package-information signing method ""
            m = p13.match(line)
            if m:
                group = m.groupdict()
                pkg_info_method = group['pkg_info_method']
                app_dict['pkg_info_method'] = pkg_info_method
                continue

            # details package-information licensing name ""
            m = p14.match(line)
            if m:
                group = m.groupdict()
                pkg_lic_name = group['pkg_lic_name']
                app_dict['pkg_lic_name'] = pkg_lic_name
                continue

            # details package-information licensing version ""
            m = p15.match(line)
            if m:
                group = m.groupdict()
                pkg_lic_version = group['pkg_lic_version']
                app_dict['pkg_lic_version'] = pkg_lic_version
                continue

            # details package-information url-path ""
            m = p16.match(line)
            if m:
                group = m.groupdict()
                pkg_url_path = group['pkg_url_path']
                app_dict['pkg_url_path'] = pkg_url_path
                continue

            # details detailed-guest-status processes name ""
            m = p17.match(line)
            if m:
                group = m.groupdict()
                processes_name = group['processes_name']
                app_dict['processes_name'] = processes_name
                continue

            #  details detailed-guest-status processes status ""
            m = p18.match(line)
            if m:
                group = m.groupdict()
                processes_status = group['processes_status']
                app_dict['processes_status'] = processes_status
                continue

            #  details detailed-guest-status processes pid ""
            m = p19.match(line)
            if m:
                group = m.groupdict()
                processes_pid = group['processes_pid']
                app_dict['processes_pid'] = processes_pid
                continue

            #  details detailed-guest-status processes uptime ""
            m = p20.match(line)
            if m:
                group = m.groupdict()
                processes_uptime = group['processes_uptime']
                app_dict['processes_uptime'] = processes_uptime
                continue

            #  details detailed-guest-status processes memory ""
            m = p21.match(line)
            if m:
                group = m.groupdict()
                processes_memory = group['processes_memory']
                app_dict['processes_memory'] = processes_memory
                continue

            #  details activated-profile-name cloud-medium
            m = p22.match(line)
            if m:
                group = m.groupdict()
                profile_name = group['profile_name']
                app_dict['profile_name'] = profile_name
                continue

            #  details resource-reservation disk 1111
            m = p23.match(line)
            if m:
                group = m.groupdict()
                disk = group['disk']
                app_dict['disk'] = disk
                continue

            #  details resource-reservation memory 3072
            m = p24.match(line)
            if m:
                group = m.groupdict()
                memory = group['memory']
                app_dict['memory'] = memory
                continue

            #  details resource-reservation cpu 0
            m = p25.match(line)
            if m:
                group = m.groupdict()
                cpu = group['cpu']
                app_dict['cpu'] = cpu
                continue

            #  details resource-reservation vcpu 0
            m = p26.match(line)
            if m:
                group = m.groupdict()
                vcpu = group['vcpu']
                app_dict['vcpu'] = vcpu
                continue

            #  details resource-reservation cpu-percent 50
            m = p27.match(line)
            if m:
                group = m.groupdict()
                cpu_percent = group['cpu_percent']
                app_dict['cpu_percent'] = cpu_percent
                continue

            #  details guest-interface  ""
            m = p28.match(line)
            if m:
                group = m.groupdict()
                guest_intf = group['guest_intf']
                app_dict['guest_intf'] = guest_intf
                continue

            # details resource-admission state ""
            m = p29.match(line)
            if m:
                group = m.groupdict()
                res_add_state = group['res_add_state']
                app_dict['res_add_state'] = res_add_state
                continue

            # details resource-admission disk-space ""
            m = p30.match(line)
            if m:
                group = m.groupdict()
                res_add_disk_space = group['res_add_disk_space']
                app_dict['res_add_disk_space'] = res_add_disk_space
                continue

            # details resource-admission memory ""
            m = p31.match(line)
            if m:
                group = m.groupdict()
                res_add_memory = group['res_add_memory']
                app_dict['res_add_memory'] = res_add_memory
                continue

            # details resource-admission cpu 0
            m = p32.match(line)
            if m:
                group = m.groupdict()
                res_add_cpu = group['res_add_cpu']
                app_dict['res_add_cpu'] = res_add_cpu
                continue

            # details resource-admission vcpus ""
            m = p33.match(line)
            if m:
                group = m.groupdict()
                res_add_vcpu = group['res_add_vcpu']
                app_dict['res_add_vcpu'] = res_add_vcpu
                continue

            # details docker-run-opts  ""
            m = p34.match(line)
            if m:
                group = m.groupdict()
                res_doc_run_opts = group['res_doc_run_opts']
                app_dict['res_doc_run_opts'] = res_doc_run_opts
                continue

            # details command  ""
            m = p35.match(line)
            if m:
                group = m.groupdict()
                details_command = group['details_command']
                app_dict['details_command'] = details_command
                continue

            # details entry-postr  ""
            m = p36.match(line)
            if m:
                group = m.groupdict()
                details_entry_point = group['details_entry_point']
                app_dict['details_entry_point'] = details_entry_point
                continue

            # details health-status    0
            m = p37.match(line)
            if m:
                group = m.groupdict()
                details_health_stats = group['details_health_stats']
                app_dict['details_health_stats'] = details_health_stats
                continue

            # details last-health-probe-error ""
            m = p38.match(line)
            if m:
                group = m.groupdict()
                details_probe_error = group['details_probe_error']
                app_dict['details_probe_error'] = details_probe_error
                continue

            # details last-health-probe-output ""
            m = p39.match(line)
            if m:
                group = m.groupdict()
                details_probe_output = group['details_probe_output']
                app_dict['details_probe_output'] = details_probe_output
                continue

            # details pkg-run-opt      ""
            m = p40.match(line)
            if m:
                group = m.groupdict()
                details_pkg_run_opt = group['details_pkg_run_opt']
                app_dict['details_pkg_run_opt'] = details_pkg_run_opt
                continue

            # details ieobc-mac-addr   33:33:3a:33:33:3a
            m = p41.match(line)
            if m:
                group = m.groupdict()
                ieobc_mac_address = group['ieobc_mac_address']
                app_dict['ieobc_mac_address'] = ieobc_mac_address
                continue

            # utilization name utd
            m = p42.match(line)
            if m:
                group = m.groupdict()
                utilization_name = group['utilization_name']
                app_dict['utilization_name'] = utilization_name
                continue

            # utilization cpu-util requested-application-util 0
            m = p43.match(line)
            if m:
                group = m.groupdict()
                req_app_util = group['req_app_util']
                app_dict['req_app_util'] = req_app_util
                continue

            # utilization cpu-util actual-application-util 3
            m = p44.match(line)
            if m:
                group = m.groupdict()
                actual_app_util = group['actual_app_util']
                app_dict['actual_app_util'] = actual_app_util
                continue

            # utilization cpu-util cpu-state ""
            m = p45.match(line)
            if m:
                group = m.groupdict()
                cpu_state = group['cpu_state']
                app_dict['cpu_state'] = cpu_state
                continue

            # utilization memory-util memory-allocation 3072
            m = p46.match(line)
            if m:
                group = m.groupdict()
                mem_allocation = group['mem_allocation']
                app_dict['mem_allocation'] = mem_allocation
                continue

            #  utilization memory-util memory-used 335636
            m = p47.match(line)
            if m:
                group = m.groupdict()
                mem_used = group['mem_used']
                app_dict['mem_used'] = mem_used
                continue

            #                     RX       RX     RX      TX       TX     TX
            #   NAME     ALIAS  PACKETS  BYTES  ERRORS  PACKETS  BYTES  ERRORS
            #   ----------------------------------------------------------------
            #   dp_1_0   net2   0        0      0       30       1260   0
            #   dp_1_1   net3   0        0      0       0        0      0
            #   ieobc_1  ieobc  190      11175  0       190      12303  0
            m = p48.match(line)
            if m:
                group = m.groupdict()
                name = group.pop("name")

                name_dict = oper_data_dict.setdefault("name", {}). \
                    setdefault(name, {})

                name_dict.update({k: v for k, v in group.items()})
                continue

            # storage-utils storage-util disk
            if p49.match(line):
                resource = "storage_utils_storage_util_disk"
                storage_utils_storage_util_disk_dict = oper_data_dict.setdefault("storage_utils_storage_util_disk", {})
                storage_dict = storage_utils_storage_util_disk_dict
                continue

            # app-hosting-oper-data app-resources global
            if p62.match(line):
                resource = "app_hosting_oper_data_app_resources_global"
                app_resources_global_dict = oper_data_dict.setdefault("app_hosting_oper_data_app_resources_global", {})
                continue

            # available   255382
            if p57.match(line):
                m = p57.match(line)
                if m:
                    group = m.groupdict()
                    available = group['available']
                    storage_dict['available'] = available
                continue

            #  alias       ""
            m = p50.match(line)
            if m:
                group = m.groupdict()
                alias = group['alias']
                storage_utils_storage_util_disk_dict.setdefault("alias", alias)
                continue

            #  rd-bytes    0
            m = p51.match(line)
            if m:
                group = m.groupdict()
                rd_bytes = group['rd_bytes']
                storage_utils_storage_util_disk_dict['rd_bytes'] = rd_bytes
                continue

            #  rd-requests 0
            m = p52.match(line)
            if m:
                group = m.groupdict()
                rd_requests = group['rd_requests']
                storage_utils_storage_util_disk_dict['rd_requests'] = rd_requests
                continue

            #  errors      0
            m = p53.match(line)
            if m:
                group = m.groupdict()
                errors = group['errors']
                storage_utils_storage_util_disk_dict['errors'] = errors
                continue

            #  wr-bytes    0
            m = p54.match(line)
            if m:
                group = m.groupdict()
                wr_bytes = group['wr_bytes']
                storage_utils_storage_util_disk_dict['wr_bytes'] = wr_bytes
                continue

            #  wr-requests 0
            m = p55.match(line)
            if m:
                group = m.groupdict()
                wr_requests = group['wr_requests']
                storage_utils_storage_util_disk_dict['wr_requests'] = wr_requests
                continue

            #  capacity    1137664
            m = p56.match(line)
            if m:
                group = m.groupdict()
                capacity = group['capacity']
                storage_utils_storage_util_disk_dict['capacity'] = capacity
                continue

            #  used        882282
            m = p58.match(line)
            if m:
                group = m.groupdict()
                used = group['used']
                storage_utils_storage_util_disk_dict['used'] = used
                continue

            #   usage       ""
            m = p59.match(line)
            if m:
                group = m.groupdict()
                usage = group['usage']
                storage_utils_storage_util_disk_dict['usage'] = usage
                continue

            #                ATTACHED   IPV4       NETWORK  IPV6
            # MAC ADDRESS        str     ERFACE  ADDRESS    NAME     ADDRESS
            # -----------------------------------------------------------
            # 54:0e:00:0b:0c:02  eth0       0.0.0.0    ieobc_1  ::
            # f8:6b:d9:c0:cc:5e  eth2       0.0.0.0    dp_1_0   ::
            # f8:6b:d9:c0:cc:5f  eth1       192.0.2.2  dp_1_1   ::
            m = p60.match(line)
            if m:
                group = m.groupdict()
                mac_address = group.pop("mac_address")

                mac_add_dict = oper_data_dict.setdefault("mac_address", {}). \
                    setdefault(mac_address, {})

                mac_add_dict.update({k: v for k, v in group.items()})
                continue

            #   pkg-policy iox-pkg-policy-invalid
            m = p61.match(line)
            if m:
                group = m.groupdict()
                pkg_policy = group['pkg_policy']
                storage_utils_storage_util_disk_dict['pkg_policy'] = pkg_policy
                continue

            # cpu "system CPU"
            if p63.match(line):
                app_resource = "cpu"
                cpu_dict = app_resources_global_dict.setdefault("cpu_details", {})
                storage_dict = cpu_dict
                continue

            # memory memory
            elif p68.match(line):
                app_resource = "memory"
                memory_dict = app_resources_global_dict.setdefault("memory_details", {})
                storage_dict = memory_dict
                continue

            # storage-device harddisk
            elif p69.match(line):
                app_resource = "storage_device_harddisk"
                harddisk_dict = app_resources_global_dict.setdefault("storage_device_harddisk", {})
                storage_dict = harddisk_dict
                continue

            # storage-device bootflash
            elif p70.match(line):
                app_resource = "storage_device_bootflash"
                bootflash_dict = app_resources_global_dict.setdefault("storage_device_bootflash", {})
                storage_dict = bootflash_dict
                continue

            # storage-device volume-group
            elif p71.match(line):
                app_resource = "storage_device_volume_group"
                volume_group_dict = app_resources_global_dict.setdefault("storage_device_volume_group", {})
                storage_dict = volume_group_dict
                continue

            #  storage-device "CAF persist-disk"
            elif p72.match(line):
                app_resource = "storage_device_caf_persist_disk"
                caf_persist_disk_dict = app_resources_global_dict.setdefault("storage_device_caf_persist_disk", {})
                storage_dict = caf_persist_disk_dict
                continue

            # quota          98
            m = p64.match(line)
            if m:
                group = m.groupdict()
                quota = group['quota']
                storage_dict['quota'] = quota
                continue

            # quota-unit     48608
            m = p66.match(line)
            if m:
                group = m.groupdict()
                quota_unit = group['quota_unit']
                cpu_dict['quota_unit'] = quota_unit
                continue

            # available-unit 23808
            m = p67.match(line)
            if m:
                group = m.groupdict()
                available_unit = group['available_unit']
                cpu_dict['available_unit'] = available_unit
                continue

            # timestamp      2022-04-25T18:08:36.189866+00:00
            m = p73.match(line)
            if m:
                group = m.groupdict()
                timestamp = group['timestamp']
                app_notifications_event_dict = oper_data_dict.setdefault("app_notifications_event", {})
                app_notifications_event_dict['timestamp'] = timestamp
                continue

            # severity-level minor
            m = p74.match(line)
            if m:
                group = m.groupdict()
                severity_level = group['severity_level']
                app_notifications_event_dict['severity_level'] = severity_level
                continue

            # host-name      pm9005
            m = p75.match(line)
            if m:
                group = m.groupdict()
                host_name = group['host_name']
                app_notifications_event_dict['host_name'] = host_name
                continue

            # vrf-name       ""
            m = p76.match(line)
            if m:
                group = m.groupdict()
                vrf_name = group['vrf_name']
                app_notifications_event_dict['vrf_name'] = vrf_name
                continue

            # app-id         utd
            m = p77.match(line)
            if m:
                group = m.groupdict()
                app_id = group['app_id']
                app_notifications_event_dict['app_id'] = app_id
                continue

            # ev-type        im-iox-enable
            m = p78.match(line)
            if m:
                group = m.groupdict()
                ev_type = group['ev_type']
                app_notifications_event_dict['ev_type'] = ev_type
                continue

            # status         im-app-pass
            m = p79.match(line)
            if m:
                group = m.groupdict()
                status = group['status']
                app_notifications_event_dict['status'] = status
                continue

            # app-state      im-state-running
            m = p80.match(line)
            if m:
                group = m.groupdict()
                app_state = group['app_state']
                app_notifications_event_dict['app_state'] = app_state
                continue

            # app-hosting-oper-data app-globals iox-enabled true
            m = p81.match(line)
            if m:
                group = m.groupdict()
                is_enabled = group['is_enabled']
                app_notifications_event_dict['is_enabled'] = is_enabled
                continue

        return oper_data_dict


# ========================================================
# Schema for "show sdwan policy app-route-policy-filter"
# ========================================================

class ShowSdwanPolicyAppRoutePolicyFilterSchema(MetaParser):
    """Schema for 'show sdwan policy app-route-policy-filter' """

    schema = {
        "policy_name": {

            Any(): {
                "vpn_list": {

                    Any(): {
                        "counter_name": {

                            Any(): {
                                "packets": int,
                                "bytes": int
                            }
                        }
                    }
                }
            }
        }
    }

class ShowSdwanPolicyAppRoutePolicyFilter(ShowSdwanPolicyAppRoutePolicyFilterSchema):
    """
    Parser for 'show sdwan policy app-route-policy-filter' on ios-xe sdwan devices.
    parser class - implements detail parsing mechanisms for cli output.
    """
    cli_command = "show sdwan policy app-route-policy-filter"
    """
        # NAME            NAME  COUNTER NAME                      PACKETS       BYTES
        # ----------------------------------------------------------------------------------------
        # VPN_AAR_Policy  VPN1  default_action_count              0             0
        #                       AAR_APP_Email_963617983           0             0
        #                       AAR_APP_others_963617983          0             0
        #                       AAR_APP_Facebook_963617983        0             0
        #                       AAR_APP_Bit_Exchange_963617983    0             0
    """

    def cli(self, output: str = None) -> dict:
        if output is None:
            output = self.device.execute(self.cli_command)
        # VPN_AAR_Policy  VPN1  default_action_count              0             0
        p1 = re.compile(
            r"\s*(?P<policy_name>\S+)\s+(?P<vpn_name>\S+)\s+(?P<counter_name>\S+)\s+(?P<packets_counter>\d+)\s+(?P<bytes_counter>\d+)$"

        )

        # VPN1  default_action_count              0             0
        p2 = re.compile(
            r"^(?P<vpn_name>\S+)\s+(?P<counter_name>\S+)\s+(?P<packets_counter>\d+)\s+(?P<bytes_counter>\d+)$"

        )

        # AAR_APP_Facebook_963617983        0             0
        p3 = re.compile(
            r"^(?P<counter_name>\S+)\s+(?P<packets_counter>\d+)\s+(?P<bytes_counter>\d+)$"
        )

        parsed_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # VPN_AAR_Policy  VPN1  default_action_count              0             0
            m1 = p1.match(line)
            if m1:
                groups = m1.groupdict()
                policy_name = groups["policy_name"]
                vpn_name = groups["vpn_name"]
                counter_name = groups["counter_name"]
                packets_counter = int(groups["packets_counter"])
                bytes_counter = int(groups["bytes_counter"])
                policy_class_dict = parsed_dict.setdefault("policy_name", {}).setdefault(
                    policy_name, {}
                )
                vpn_class_dict = policy_class_dict.setdefault(
                    "vpn_list", {}
                ).setdefault(vpn_name, {})
                counter_dict = vpn_class_dict.setdefault("counter_name", {}).setdefault(
                    counter_name, {}
                )
                counter_dict["packets"] = packets_counter
                counter_dict["bytes"] = bytes_counter
                continue

            # VPN1  default_action_count              0             0
            m2 = p2.match(line)
            if m2:
                groups = m2.groupdict()
                vpn_name = groups["vpn_name"]
                counter_name = groups["counter_name"]
                packets_counter = int(groups["packets_counter"])
                bytes_counter = int(groups["bytes_counter"])
                vpn_class_dict = policy_class_dict.setdefault(
                    "vpn_list", {}
                ).setdefault(vpn_name, {})
                counter_dict = vpn_class_dict.setdefault("counter_name", {}).setdefault(
                    counter_name, {}
                )
                counter_dict["packets"] = packets_counter
                counter_dict["bytes"] = bytes_counter
                continue

            # AAR_APP_Facebook_963617983        0             0
            m3 = p3.match(line)
            if m3:
                groups = m3.groupdict()
                counter_name = groups["counter_name"]
                packets_counter = int(groups["packets_counter"])
                bytes_counter = int(groups["bytes_counter"])
                counter_dict = vpn_class_dict.setdefault("counter_name", {}).setdefault(
                    counter_name, {}
                )
                counter_dict["packets"] = packets_counter
                counter_dict["bytes"] = bytes_counter
                continue

        return parsed_dict

# ========================================================
# Schema for "show sdwan policy fromv-smart"
# ========================================================

class ShowSdwanPolicyFromVsmartSchema(MetaParser):
    """Schema for 'show sdwan policy from-vsmart'"""

    schema = {
        Optional("sla_class"): {
            Any(): {
                "loss": int,
                "latency": int,
                "jitter": int,
                Optional("fallback_best_tunnel"): {
                    "criteria": list,
                    "loss_variance": int,
                    "latency_variance": int,
                    "jitter_variance": int,
                },
            }
        },
        Optional("data_policy"): {
            Any(): {
                "direction": str,
                "vpn_list": {
                    Any(): {
                        "sequence": {
                            Any(): {
                                "match": {
                                    Optional("source_ip"): str,
                                    Optional("destination_ip"): str,
                                    Optional("dscp"): list,
                                    Optional("app_list"): str,
                                    Optional("source_data_prefix_list"): str,
                                    Optional("destination_data_prefix_list"): str,
                                    Optional("dns_app_list"): str,
                                    Optional("source_port"): int,
                                    Optional("destination_port"): int,
                                    Optional("protocol"): list,
                                    Optional("tcp"): str,
                                    Optional("plp"): str,
                                    Optional("traffic_to"): str,
                                    Optional("destination_region"): str,
                                    Optional("packet_length"): str,
                                    Optional("dns"): str,
                                },
                                "action": {
                                    Any(): {
                                        Optional("count"): str,
                                        Optional("nat"): {
                                            Optional("use_vpn"): int,
                                            Optional("fallback"): bool,
                                            Optional("pool"): str,
                                        },
                                        Optional("log"): bool,
                                        Optional("tcp_optimization"): bool,
                                        Optional("loss_protection"): {
                                            Optional("forward_error_correction"): str,
                                            Optional("packet_duplication"): bool,
                                        },
                                        Optional("cflowd"): bool,
                                        Optional("set"): {
                                            Optional("local_tloc_list"): {
                                                Optional("color"): list,
                                                Optional("encap"): str,
                                                Optional("restrict"): bool,
                                            },
                                            Optional("next_hop"): str,
                                            Optional("next_hop_loose"): bool,
                                            Optional("policer"): str,
                                            Optional("dscp"): list,
                                            Optional("forwarding_class"): str,
                                            Optional("vpn"): int,
                                            Optional("vip_tloc_pref_list"): {
                                                Any(): {
                                                    Optional("tloc"): {
                                                        Optional("label"): int,
                                                        Optional("ip"): str,
                                                        Optional("color"): str,
                                                        Optional("encap"): str,
                                                    }
                                                }
                                            },
                                            Optional("tloc_list"): list,
                                            Optional("service"): {
                                                Optional("name"): str,
                                                Optional("vpn"): int,
                                                Optional("tloc_list"): list,
                                                Optional("tloc"): {
                                                    Optional("ip"): str,
                                                    Optional("color"): list,
                                                    Optional("encap"): str,
                                                },
                                            },
                                        },
                                        Optional("redirect_dns"): str,
                                    }
                                },
                            }
                        },
                        Optional("default_action"): str,
                    }
                },
            }
        },
        Optional("cflowd_template"): {
            Any(): {
                "flow_active_timeout": int,
                "flow_inactive_timeout": int,
                "template_refresh": int,
                "flow_sampling_interval": int,
                "protocol": list,
                "customized_ipv4_record_fields": {
                    Optional("collect_tos"): bool,
                    Optional("collect_dscp_output"): bool,
                },
                "collector": {
                    "vpn": {
                        Any(): {
                            "address": str,
                            "port": int,
                            "transport": str,
                            "source_interface": str,
                        }
                    }
                },
            }
        },
        Optional("app_route_policy"): {
            Any(): {
                "vpn_list": {
                    Any(): {
                        "sequence": {
                            Any(): {
                                "match": {
                                    Optional("source_ip"): str,
                                    Optional("destination_ip"): str,
                                    Optional("dscp"): list,
                                    Optional("app_list"): str,
                                    Optional("source_data_prefix_list"): str,
                                    Optional("destination_data_prefix_list"): str,
                                    Optional("dns_app_list"): str,
                                    Optional("source_port"): int,
                                    Optional("destination_port"): int,
                                    Optional("protocol"): list,
                                    Optional("tcp"): str,
                                    Optional("plp"): str,
                                    Optional("traffic_to"): str,
                                    Optional("destination_region"): str,
                                    Optional("packet_length"): str,
                                    Optional("dns"): str,
                                    Optional("cloud_saas_app_list"): str,
                                },
                                "action": {
                                    Optional("count"): str,
                                    Optional("log"): bool,
                                    Optional("backup_sla_preferred_color"): str,
                                    Optional("sla_class"): {
                                        Optional("types"): list,
                                        Optional("preferred_color"): list,
                                    },
                                    Optional("cloud_saas"): str,
                                },
                            }
                        }
                    }
                }
            }
        },
        Optional("policer"): {
            Any(): {
                "rate": int,
                "burst": int,
                "exceed": str
            }
        },
        Optional("lists"): {
            Optional("vpn_list"): {
                Any(): {
                    "vpn": int
                }
            },
            Optional("app_list"): {
                Any(): {
                    Optional("app"): list,
                    Optional("app_family"): list
                }
            },
            Optional("data_prefix_list"): {
                Any(): {
                    "ip_prefix": str
                }
            },
            Optional("tloc_list"): {
                Any(): {
                    "tloc": {
                        Any(): {
                            "color": str,
                            "encap": str
                        }
                    }
                }
            },
            Optional("preferred_color_group"): {
                Any(): {
                    Any(): {
                        "color_preference": str,
                        Optional("path_preference"): str
                    }
                }
            },
        },
    }


class ShowSdwanPolicyFromVsmart(ShowSdwanPolicyFromVsmartSchema):
    """
    Parser for 'show sdwan policy from-vsmart' on ios-xe sdwan devices.
    parser class - implements detail parsing mechanisms for cli output.
    """

    cli_command = "show sdwan policy from-vsmart"

    def cli(self, output: str = None) -> dict:
        if output is None:
            output = self.device.execute(self.cli_command)

        # from-vsmart sla-class Realtime
        p1 = re.compile(r"^from-vsmart+\s+(?P<policy_type>\S+)\s+(?P<policy_type_name>\S+)$")

        # loss    21
        # latency 300
        # jitter  100
        p2 = re.compile(r"^(?P<stat_name>(loss|latency|jitter)+)\s+(?P<value>\d+)$")

        # criteria         loss latency jitter
        p3 = re.compile(r"^criteria+\s+(?P<fallback_criteria>[\s\S]+)$")

        # loss-variance    10
        # latency-variance 100
        # jitter-variance  200
        p4 = re.compile(
            r"^(?P<stat_name>(loss-variance|latency-variance|jitter-variance)+)\s+(?P<value>\d+)$"
        )

        # rate   3000000
        # burst  150000
        p5 = re.compile(r"^(?P<stat_name>(rate|burst)+)\s+(?P<value>\d+)$")

        # exceed drop
        p6 = re.compile(r"^exceed+\s+(?P<action>\S+)$")

        # direction from-service
        p7 = re.compile(r"^direction+\s+(?P<direction>\S+)$")

        # vpn-list VPN1
        p8 = re.compile(r"^vpn-list+\s+(?P<vpn_list_name>\S+)$")

        # sequence 51
        p9 = re.compile(r"^sequence+\s+(?P<sequence>\d+)$")

        # source-ip 0.0.0.0/0
        p10 = re.compile(r"^source-ip+\s+(?P<source_ip>\S+)$")

        # destination-ip     0.0.0.0/0
        p11 = re.compile(r"^destination-ip+\s+(?P<destination_ip>\S+)$")

        # dscp               15
        p12 = re.compile(r"^dscp+\s+(?P<dscp_list>[\s\d]+)$")

        # app-list Email
        p13 = re.compile(r"^app-list+\s+(?P<app_list>\S+)$")

        # source-data-prefix-list site1_vpn10_ipv4
        p14 = re.compile(r"^source-data-prefix-list+\s+(?P<sdata_prefix_list>\S+)$")

        # destination-data-prefix-list site6_service_ipv4_red
        p15 = re.compile(r"^destination-data-prefix-list+\s+(?P<ddata_prefix_list>\S+)$")

        # dns-app-list                 Microsoft_Apps
        p16 = re.compile(r"^dns-app-list+\s+(?P<dns_app_list>\S+)$")

        # source-port                  1024
        p17 = re.compile(r"^source-port+\s+(?P<source_port>\d+)$")

        # destination-port             8080
        p18 = re.compile(r"^destination-port+\s+(?P<destination_port>\d+)$")

        # protocol 1 2 3
        p19 = re.compile(r"^protocol+\s+(?P<protocol>[\s\S]+)$")

        # tcp                          syn
        p20 = re.compile(r"^tcp+\s+(?P<tcp_flag>\S+)$")

        # plp                          high
        p21 = re.compile(r"^plp+\s+(?P<plp>\S+)$")

        # traffic-to                   core
        p22 = re.compile(r"^traffic-to+\s+(?P<traffic_to>\S+)$")

        # destination-region           primary-region
        p23 = re.compile(r"^destination-region+\s+(?P<destination_region>\S+)$")

        # packet-length                1-4096
        p24 = re.compile(r"^packet-length+\s+(?P<packet_length>\S+)$")

        # dns                          request
        p25 = re.compile(r"^dns+\s+(?P<dns_query>\S+)$")

        # cloud-saas-app-list gotomeeting_apps
        p26 = re.compile(r"^cloud-saas-app-list+\s+(?P<cloud_saas_app_list>\S+)$")

        # action accept
        p27 = re.compile(r"^action+\s+(?P<action>\S+)$")

        # action
        p27_1 = re.compile(r"^action+$")

        # nat pool 11
        p28 = re.compile(r"^nat+\s+pool+\s+(?P<nat_pool_number>\d+)$")
        p28_1 = re.compile(r"^nat+\s+[\s\S]+")

        # nat use-vpn 0
        p29 = re.compile(r"^nat+\s+use-vpn+\s+(?P<use_vpn_number>\d+)$")

        # nat fallback
        p30 = re.compile(r"^nat+\s+fallback+$")

        # log
        p31 = re.compile(r"^log+$")

        # tcp-optimization
        p32 = re.compile(r"^tcp-optimization+$")

        # count  testing-counter_-2070586118
        p33 = re.compile(r"^count+\s+(?P<count_name>\S+)$")

        # set
        p34_1 = re.compile(r"^set+$")

        # local-tloc-list
        p34 = re.compile(r"^local-tloc-list+$")

        # restrict
        p35 = re.compile(r"^restrict+$")

        # color mpls public-internet
        p36 = re.compile(r"^color+\s+(?P<color_types>[\s\S]+)$")

        # encap ipsec
        p37 = re.compile(r"^encap+\s+(?P<encap_type>\S+)$")

        # next-hop         10.0.0.1
        p38 = re.compile(r"^next-hop+\s+(?P<next_hop>\S+)$")

        # next-hop-loose
        p39 = re.compile(r"^next-hop-loose+$")

        # policer          site6_policer
        p40 = re.compile(r"^policer+\s+(?P<policer>\S+)$")

        # forwarding-class Net-Mgmt
        p41 = re.compile(r"^forwarding-class+\s+(?P<forwarding_class>\S+)$")

        # vpn              10
        p42 = re.compile(r"^vpn+\s+(?P<vpn>\d+)$")

        # vip-tloc-pref-list 0
        p43 = re.compile(r"^vip-tloc-pref-list+\s+(?P<vip_tloc_pref_list>\d+)$")

        # tloc-label 1002
        # tloc-ip    8.8.8.1
        # tloc-color public-internet
        # tloc-encap ipsec
        p44 = re.compile(r"^tloc-+(?P<tloc_type>(?!list)\S+)\s+(?P<value>[\s\S]+)$")

        # tloc-list        HUB2
        p45 = re.compile(r"^tloc-list+\s+(?P<value>[\s\S]+)$")

        # service FW
        p46_1 = re.compile(r"^service+.+$")
        p46 = re.compile(r"^service+\s+(?P<service_type>\S+)$")

        # service vpn 23
        p47 = re.compile(r"^service+\s+vpn+\s(?P<service_vpn_number>\d+)$")

        # service tloc
        p48 = re.compile(r"^service+\s+tloc+\s+.+$")

        # service tloc-list HUB2
        p48_1 = re.compile(r"^service+\s+tloc-list+\s+(?P<tloc_list>\S+)$")

        # service tloc 10.101.7.2
        p48_2 = re.compile(r"^service+\s+tloc+\s+(?P<service_tloc_ip>\S+)$")

        # service tloc color public-internet
        p49 = re.compile(r"^service+\s+tloc+\s+color+\s+(?P<service_tloc_colors>[\S\s]+)$")

        # service tloc encap ipsec
        p50 = re.compile(r"^service+\s+tloc+\s+encap+\s+(?P<encap>\S+)$")

        # loss-protection forward-error-correction adaptive
        p51_1 = re.compile(r"^loss-protection+.+$")
        p51 = re.compile(
            r"^loss-protection+\s+forward-error-correction+\s+(?P<fw_error_correction_type>\S+)$"
        )

        # loss-protection packet-duplication
        p52 = re.compile(r"^loss-protection+\s+(?P<loss_prot_type>\S+)$")

        # redirect-dns host
        p53 = re.compile(r"^redirect-dns+\s+(?P<redirect_dns>\S+)$")

        # cflowd
        p54 = re.compile(r"^cflowd+$")

        # default-action accept
        p55 = re.compile(r"^default-action+\s+(?P<default_action>\S+)$")

        # flow-active-timeout    600
        # flow-inactive-timeout  60
        p57 = re.compile(r"^flow-+(?P<flow_type>\S+)-timeout+\s+(?P<timeout_value>\d+)$")

        # template-refresh       600
        p58 = re.compile(r"^template-refresh+\s+(?P<template_refresh_value>\d+)$")

        # flow-sampling-interval 1
        p59 = re.compile(r"^flow-sampling-interval+\s+(?P<sampling_interval>\d+)$")

        # customized-ipv4-record-fields
        p60 = re.compile(r"^customized-ipv4-record-fields+$")

        # collect-tos
        p61 = re.compile(r"^collect-tos+$")

        # no collect-dscp-output
        p62 = re.compile(r"^no+\s+collect-dscp-output+$")

        # collector vpn 10 address 10.0.0.1 port 1024 transport transport_udp
        p63 = re.compile(
            r"^collector+\s+vpn+\s+(?P<vpn_number>\d+)\s+address+\s+(?P<ip_address>\S+)\s+port+\s+(?P<port_number>\d+)\s+transport+\s+(?P<transport_type>\S+)$"
        )

        # source-interface GigabitEthernet0/0/0
        p64 = re.compile(r"^source-interface+\s+(?P<interface_name>\S+)$")

        # backup-sla-preferred-color bronze
        p65 = re.compile(r"^backup-sla-preferred-color+\s+(?P<color>\S+)$")

        # sla-class
        p66_1 = re.compile(r"^sla-class+.+$")

        # sla-class       raghav-test-Bulk-Data
        p66 = re.compile(r"^sla-class+\s+(?P<sla_class>\S+)$")

        # sla-class preferred-color biz-internet custom1
        p67 = re.compile(r"^sla-class+\s+preferred-color+\s+(?P<preferred_color>[\S\s]+)$")

        # cloud-saas allow-local
        p68 = re.compile(r"^cloud-saas+\s+(?P<cloud_saas>\S+)$")

        # from-vsmart lists vpn-list VPN1
        # from-vsmart lists app-list Email
        p69 = re.compile(r"^from-vsmart+\s+lists+\s+(?P<lists_type>\S+)+\s+(?P<list_name>\S+)$")

        # app cisco-jabber-im
        p70 = re.compile(r"^app+\s+(?P<app_type>\S+)$")

        # app-family app-fam-2
        p71 = re.compile(r"^app-family+\s+(?P<app_family_type>\S+)$")

        # ip-prefix 10.10.1.0/24
        p72 = re.compile(r"^ip-prefix+\s+(?P<ip_prefix>\S+)$")

        # tloc 8.8.8.1 color public-internet encap ipsec
        p73 = re.compile(
            r"^tloc+\s+(?P<tloc_ip>\S+)\s+color+\s+(?P<color>\S+)\s+encap+\s+(?P<encap>\S+)$"
        )

        # primary-preference
        # secondary-preference
        # tertiary-preference
        p74 = re.compile(r"^(?P<preference_order>\S+)-preference$")

        # color-preference biz-internet
        p75 = re.compile(r"^color-preference+\s+(?P<color_preference>\S+)$")

        # path-preference  direct-path
        p76 = re.compile(r"^path-preference+\s+(?P<path_preference>\S+)$")

        parser_location = None
        parsed_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # from-vsmart sla-class Realtime
            m1 = p1.match(line)
            if m1:
                groups = m1.groupdict()
                policy_type = groups["policy_type"]
                policy_type = policy_type.replace('-', '_')
                parser_location = policy_type
                policy_type_name = groups["policy_type_name"]
                policy_type_name = policy_type_name.replace('-', '_')
                policy_dict = parsed_dict.setdefault(policy_type, {}).setdefault(
                    policy_type_name, {}
                )
                continue

            # loss    21
            # latency 300
            # jitter  100
            m2 = p2.match(line)
            if m2:
                groups = m2.groupdict()
                stat_name = groups["stat_name"]
                stat_value = groups["value"]
                policy_dict[stat_name] = int(stat_value)
                continue

            # criteria         loss latency jitter
            m3 = p3.match(line)
            if m3:
                groups = m3.groupdict()
                criteria = groups["fallback_criteria"].split()
                fallback_policy_dict = policy_dict.setdefault("fallback_best_tunnel", {})
                fallback_policy_dict["criteria"] = criteria
                continue

            # loss-variance    10
            # latency-variance 100
            # jitter-variance  200
            m4 = p4.match(line)
            if m4:
                groups = m4.groupdict()
                stat_name = groups["stat_name"]
                stat_value = groups["value"]
                stat_name = stat_name.replace('-', '_')
                fallback_policy_dict[stat_name] = int(stat_value)
                continue

            # rate   3000000
            # burst  150000
            m5 = p5.match(line)
            if m5:
                groups = m5.groupdict()
                stat_name = groups["stat_name"]
                stat_value = groups["value"]
                policy_dict[stat_name] = int(stat_value)
                continue

            # exceed drop
            m6 = p6.match(line)
            if m6:
                groups = m6.groupdict()
                exceed_action = groups["action"]
                policy_dict["exceed"] = exceed_action
                continue

            # direction from-service
            m7 = p7.match(line)
            if m7:
                groups = m7.groupdict()
                direction = groups["direction"]
                policy_dict["direction"] = direction
                continue

            # vpn-list VPN1
            m8 = p8.match(line)
            if m8:
                groups = m8.groupdict()
                vpn_name = groups["vpn_list_name"]
                vpn_dict = policy_dict.setdefault("vpn_list", {}).setdefault(vpn_name, {})
                continue

            # sequence 51
            m9 = p9.match(line)
            if m9:
                groups = m9.groupdict()
                sequence = int(groups["sequence"])
                sequence_dict = vpn_dict.setdefault("sequence", {}).setdefault(sequence, {})
                sequence_current_dict = sequence_dict.setdefault("match", {})
                continue

            # source-ip 0.0.0.0/0
            m10 = p10.match(line)
            if m10:
                groups = m10.groupdict()
                source_ip = groups["source_ip"]
                sequence_current_dict["source_ip"] = source_ip
                continue

            # destination-ip     0.0.0.0/0
            m11 = p11.match(line)
            if m11:
                groups = m11.groupdict()
                destination_ip = groups["destination_ip"]
                sequence_current_dict["destination_ip"] = destination_ip
                continue

            # dscp               15
            m12 = p12.match(line)
            if m12:
                groups = m12.groupdict()
                dscp_list = groups["dscp_list"].split()
                dscp_numbers = []
                for dscp in dscp_list:
                    dscp_numbers.append(int(dscp))
                sequence_current_dict["dscp"] = dscp_numbers
                continue

            # app-list Email
            m13 = p13.match(line)
            if m13:
                groups = m13.groupdict()
                app_list = groups["app_list"]
                sequence_current_dict["app_list"] = app_list
                continue

            # source-data-prefix-list site1_vpn10_ipv4
            m14 = p14.match(line)
            if m14:
                groups = m14.groupdict()
                sdata_prefix_list = groups["sdata_prefix_list"]
                sequence_current_dict["source_data_prefix_list"] = sdata_prefix_list
                continue

            # destination-data-prefix-list site6_service_ipv4_red
            m15 = p15.match(line)
            if m15:
                groups = m15.groupdict()
                ddata_prefix_list = groups["ddata_prefix_list"]
                sequence_current_dict["destination_data_prefix_list"] = ddata_prefix_list
                continue

            # dns-app-list                 Microsoft_Apps
            m16 = p16.match(line)
            if m16:
                groups = m16.groupdict()
                dns_app_list = groups["dns_app_list"]
                sequence_current_dict["dns_app_list"] = dns_app_list
                continue

            # source-port                  1024
            m17 = p17.match(line)
            if m17:
                groups = m17.groupdict()
                source_port = groups["source_port"]
                sequence_current_dict["source_port"] = int(source_port)
                continue

            # destination-port             8080
            m18 = p18.match(line)
            if m18:
                groups = m18.groupdict()
                destination_port = groups["destination_port"]
                sequence_current_dict["destination_port"] = int(destination_port)
                continue

            # protocol 1 2 3
            m19 = p19.match(line)
            if m19:
                groups = m19.groupdict()
                protocols = groups["protocol"].split()
                if parser_location != "cflowd_template":
                    sequence_current_dict["protocol"] = protocols
                    continue
                policy_dict["protocol"] = protocols
                continue

            # tcp                          syn
            m20 = p20.match(line)
            if m20:
                groups = m20.groupdict()
                tcp_flag = groups["tcp_flag"]
                sequence_current_dict["tcp"] = tcp_flag
                continue

            # plp                          high
            m21 = p21.match(line)
            if m21:
                groups = m21.groupdict()
                plp = groups["plp"]
                sequence_current_dict["plp"] = plp
                continue

            # traffic-to                   core
            m22 = p22.match(line)
            if m22:
                groups = m22.groupdict()
                traffic_to = groups["traffic_to"]
                sequence_current_dict["traffic_to"] = traffic_to
                continue

            # destination-region           primary-region
            m23 = p23.match(line)
            if m23:
                groups = m23.groupdict()
                destination_region = groups["destination_region"]
                sequence_current_dict["destination_region"] = destination_region
                continue

            # packet-length                1-4096
            m24 = p24.match(line)
            if m24:
                groups = m24.groupdict()
                packet_length = groups["packet_length"]
                sequence_current_dict["packet_length"] = packet_length
                continue

            # dns                          request
            m25 = p25.match(line)
            if m25:
                groups = m25.groupdict()
                dns = groups["dns_query"]
                sequence_current_dict["dns"] = dns
                continue

            # cloud-saas-app-list gotomeeting_apps
            m26 = p26.match(line)
            if m26:
                groups = m26.groupdict()
                csaas_app_list = groups["cloud_saas_app_list"]
                sequence_current_dict["cloud_saas_app_list"] = csaas_app_list
                continue

            # action accept
            m27 = p27.match(line)
            if m27:
                groups = m27.groupdict()
                action = groups["action"]
                action_dict = sequence_dict.setdefault("action", {}).setdefault(action, {})

            # action
            m27_1 = p27_1.match(line)
            if m27_1:
                action_dict = sequence_dict.setdefault("action", {})

            # nat pool 11
            m28_1 = p28_1.match(line)
            if m28_1:
                nat_dict = action_dict.setdefault("nat", {})

                # nat pool 11
                m28 = p28.match(line)
                if m28:
                    groups = m28.groupdict()
                    nat_pool_number = groups["nat_pool_number"]
                    nat_dict["pool"] = nat_pool_number
                    continue

                # nat use-vpn 0
                m29 = p29.match(line)
                if m29:
                    groups = m29.groupdict()
                    vpn_number = groups["use_vpn_number"]
                    nat_dict["use_vpn"] = int(vpn_number)
                    continue

                # nat fallback
                m30 = p30.match(line)
                if m30:
                    nat_dict["fallback"] = True
                    continue

            # log
            m31 = p31.match(line)
            if m31:
                action_dict["log"] = True
                continue

            # tcp-optimization
            m32 = p32.match(line)
            if m32:
                action_dict["tcp_optimization"] = True
                continue

            # count  testing-counter_-2070586118
            m33 = p33.match(line)
            if m33:
                groups = m33.groupdict()
                count_name = groups["count_name"]
                action_dict["count"] = count_name
                continue

            # set
            m34_1 = p34_1.match(line)
            if m34_1:
                sequence_current_dict = action_dict.setdefault("set", {})
                continue

            # local-tloc-list
            m34 = p34.match(line)
            if m34:
                local_tloc_dict = sequence_current_dict.setdefault("local_tloc_list", {})
                continue

            # restrict
            m35 = p35.match(line)
            if m35:
                local_tloc_dict["restrict"] = True
                continue

            # color mpls public-internet
            m36 = p36.match(line)
            if m36:
                groups = m36.groupdict()
                color_types = groups["color_types"].split()
                local_tloc_dict["color"] = color_types
                continue

            # encap ipsec
            m37 = p37.match(line)
            if m37:
                groups = m37.groupdict()
                encap = groups["encap_type"]
                local_tloc_dict["encap"] = encap
                continue

            # next-hop         10.0.0.1
            m38 = p38.match(line)
            if m38:
                groups = m38.groupdict()
                next_hop = groups["next_hop"]
                sequence_current_dict["next_hop"] = next_hop
                continue

            # next-hop-loose
            m39 = p39.match(line)
            if m39:
                sequence_current_dict["next_hop_loose"] = True
                continue

            # policer          site6_policer
            m40 = p40.match(line)
            if m40:
                groups = m40.groupdict()
                policer = groups["policer"]
                sequence_current_dict["policer"] = policer
                continue

            # forwarding-class Net-Mgmt
            m41 = p41.match(line)
            if m41:
                groups = m41.groupdict()
                forwarding_class = groups["forwarding_class"]
                sequence_current_dict["forwarding_class"] = forwarding_class
                continue

            # vpn              10
            m42 = p42.match(line)
            if m42:
                groups = m42.groupdict()
                vpn = groups["vpn"]
                if parser_location != "lists":
                    sequence_current_dict["vpn"] = int(vpn)
                    continue
                policy_dict["vpn"] = int(vpn)
                continue

            # vip-tloc-pref-list 0
            m43 = p43.match(line)
            if m43:
                groups = m43.groupdict()
                vip_tloc_pref_list = groups["vip_tloc_pref_list"]
                vip_tloc_dict = (
                    sequence_current_dict.setdefault("vip_tloc_pref_list", {})
                    .setdefault(vip_tloc_pref_list, {})
                    .setdefault("tloc", {})
                )
                continue

            # tloc-label 1002
            # tloc-ip    8.8.8.1
            # tloc-color public-internet
            # tloc-encap ipsec
            m44 = p44.match(line)
            if m44:
                groups = m44.groupdict()
                tloc_type = groups["tloc_type"]
                value = groups["value"]
                if tloc_type == 'label':
                    value = int(value)
                vip_tloc_dict[tloc_type] = value
                continue

            # tloc-list        HUB2
            m45 = p45.match(line)
            if m45:
                groups = m45.groupdict()
                value = groups["value"].split()
                sequence_current_dict["tloc_list"] = value
                continue

            # service
            m46_1 = p46_1.match(line)
            if m46_1:
                service_dict = sequence_current_dict.setdefault("service", {})

            # service FW
            m46 = p46.match(line)
            if m46:
                groups = m46.groupdict()
                service_type = groups["service_type"]
                service_dict["name"] = service_type
                continue

            # service vpn 23
            m47 = p47.match(line)
            if m47:
                groups = m47.groupdict()
                service_vpn_number = groups["service_vpn_number"]
                service_dict["vpn"] = int(service_vpn_number)
                continue

            # service tloc
            m48 = p48.match(line)
            if m48:
                tloc_dict = service_dict.setdefault("tloc", {})

            # service tloc-list HUB2
            m48_1 = p48_1.match(line)
            if m48_1:
                groups = m48_1.groupdict()
                tloc_list = groups["tloc_list"]
                service_dict["tloc_list"] = tloc_list.split()
                continue

            # service tloc 10.101.7.2
            m48_2 = p48_2.match(line)
            if m48_2:
                groups = m48_2.groupdict()
                service_tloc_ip = groups["service_tloc_ip"]
                tloc_dict["ip"] = service_tloc_ip
                continue

            # service tloc color public-internet
            m49 = p49.match(line)
            if m49:
                groups = m49.groupdict()
                colors = groups["service_tloc_colors"].split()
                tloc_dict["color"] = colors
                continue

            # service tloc encap ipsec
            m50 = p50.match(line)
            if m50:
                groups = m50.groupdict()
                encap = groups["encap"]
                tloc_dict["encap"] = encap
                continue

            # loss-protection forward-error-correction adaptive
            m51_1 = p51_1.match(line)
            if m51_1:
                loss_prot_dict = action_dict.setdefault("loss_protection", {})

            m51 = p51.match(line)
            if m51:
                groups = m51.groupdict()
                correction_type = groups["fw_error_correction_type"]
                loss_prot_dict["forward_error_correction"] = correction_type
                continue

            # loss-protection packet-duplication
            m52 = p52.match(line)
            if m52:
                groups = m52.groupdict()
                loss_prot_type = groups["loss_prot_type"]
                loss_prot_type = loss_prot_type.replace('-', '_')
                loss_prot_dict[loss_prot_type] = True
                continue

            # redirect-dns host
            m53 = p53.match(line)
            if m53:
                groups = m53.groupdict()
                redirect_dns = groups["redirect_dns"]
                action_dict["redirect_dns"] = redirect_dns
                continue

            # cflowd
            m54 = p54.match(line)
            if m54:
                action_dict["cflowd"] = True
                continue

            # default-action accept
            m55 = p55.match(line)
            if m55:
                groups = m55.groupdict()
                default_action = groups["default_action"]
                vpn_dict["default_action"] = default_action
                continue

            # flow-active-timeout    600
            m57 = p57.match(line)
            if m57:
                groups = m57.groupdict()
                timeout_value = groups["timeout_value"]
                flow_type = groups["flow_type"]
                flow_type = f"flow_{flow_type}_timeout"
                policy_dict[flow_type] = int(timeout_value)
                continue

            # template-refresh       600
            m58 = p58.match(line)
            if m58:
                groups = m58.groupdict()
                template_refresh_value = groups["template_refresh_value"]
                policy_dict["template_refresh"] = int(template_refresh_value)
                continue

            # flow-sampling-interval 1
            m59 = p59.match(line)
            if m59:
                groups = m59.groupdict()
                samplig_interval = groups["sampling_interval"]
                policy_dict["flow_sampling_interval"] = int(samplig_interval)
                continue

            # customized-ipv4-record-fields
            m60 = p60.match(line)
            if m60:
                customized_ipv4_dict = policy_dict.setdefault("customized_ipv4_record_fields", {})
                continue

            # collect-tos
            m61 = p61.match(line)
            if m61:
                customized_ipv4_dict["collect_tos"] = True
                continue

            # no collect-dscp-output
            m62 = p62.match(line)
            if m62:
                customized_ipv4_dict["collect_dscp_output"] = False
                continue

            # collector vpn 10 address 10.0.0.1 port 1024 transport transport_udp
            m63 = p63.match(line)
            if m63:
                groups = m63.groupdict()
                vpn_number = groups["vpn_number"]
                ip_address = groups["ip_address"]
                port_number = groups["port_number"]
                transport_type = groups["transport_type"]
                collector_dict = (
                    policy_dict.setdefault("collector", {})
                    .setdefault("vpn", {})
                    .setdefault(vpn_number, {})
                )
                collector_dict["address"] = ip_address
                collector_dict["port"] = int(port_number)
                collector_dict["transport"] = transport_type
                continue

            # source-interface GigabitEthernet0/0/0
            m64 = p64.match(line)
            if m64:
                groups = m64.groupdict()
                source_interface = groups["interface_name"]
                collector_dict["source_interface"] = source_interface
                continue

            # backup-sla-preferred-color bronze
            m65 = p65.match(line)
            if m65:
                groups = m65.groupdict()
                color = groups["color"]
                action_dict["backup_sla_preferred_color"] = color
                continue

            # sla-class       raghav-test-Bulk-Data
            m66_1 = p66_1.match(line)
            if m66_1:
                sla_class_dict = action_dict.setdefault("sla_class", {})

            m66 = p66.match(line)
            if m66:
                groups = m66.groupdict()
                sla_class_type = groups["sla_class"]
                sla_class_type_list = sla_class_dict.setdefault("types", [])
                sla_class_type_list.append(sla_class_type)
                continue

            # sla-class preferred-color biz-internet custom1
            m67 = p67.match(line)
            if m67:
                groups = m67.groupdict()
                pref_color = groups["preferred_color"]
                sla_class_dict["preferred_color"] = pref_color.split()
                continue

            # cloud-saas allow-local
            m68 = p68.match(line)
            if m68:
                groups = m68.groupdict()
                cloud_saas = groups["cloud_saas"]
                action_dict["cloud_saas"] = cloud_saas
                continue

            # from-vsmart lists vpn-list VPN1
            # from-vsmart lists app-list Email
            m69 = p69.match(line)
            if m69:
                parser_location = "lists"
                groups = m69.groupdict()
                lists_type = groups["lists_type"]
                list_name = groups["list_name"]
                lists_type = lists_type.replace('-', '_')
                list_name = list_name.replace('-', '_')
                policy_dict = (
                    parsed_dict.setdefault("lists", {})
                    .setdefault(lists_type, {})
                    .setdefault(list_name, {})
                )
                continue

            # app cisco-jabber-im
            m70 = p70.match(line)
            if m70:
                groups = m70.groupdict()
                app_type = groups["app_type"]
                app_list = policy_dict.setdefault("app", [])
                app_list.append(app_type)
                continue

            # app-family app-fam-2
            m71 = p71.match(line)
            if m71:
                groups = m71.groupdict()
                app_family_type = groups["app_family_type"]
                app_family_list = policy_dict.setdefault("app_family", [])
                app_family_list.append(app_family_type)
                continue

            # ip-prefix 10.10.1.0/24
            m72 = p72.match(line)
            if m72:
                groups = m72.groupdict()
                ip_prefix = groups["ip_prefix"]
                policy_dict["ip_prefix"] = ip_prefix
                continue

            # tloc 8.8.8.1 color public-internet encap ipsec
            m73 = p73.match(line)
            if m73:
                groups = m73.groupdict()
                tloc_ip = groups["tloc_ip"]
                color = groups["color"]
                encap = groups["encap"]
                tloc_list_dict = policy_dict.setdefault("tloc", {}).setdefault(tloc_ip, {})
                tloc_list_dict["color"] = color
                tloc_list_dict["encap"] = encap
                continue

            # primary-preference
            # secondary-preference
            # tertiary-preference
            m74 = p74.match(line)
            if m74:
                groups = m74.groupdict()
                order = groups["preference_order"]
                order = f"{order}_preference"
                preference_dict = policy_dict.setdefault(order, {})
                continue

            # color-preference biz-internet
            m75 = p75.match(line)
            if m75:
                groups = m75.groupdict()
                color_preference = groups["color_preference"]
                preference_dict["color_preference"] = color_preference
                continue

            # path-preference  direct-path
            m76 = p76.match(line)
            if m76:
                groups = m76.groupdict()
                path_preference = groups["path_preference"]
                preference_dict["path_preference"] = path_preference
                continue

        return parsed_dict

# =======================================================================
# Parser Schema for 'show sdwan utd dataplane config'
# =======================================================================

class ShowSdwanUtdDataplaneConfigSchema(MetaParser):

    """Schema for "show sdwan utd dataplane config" """

    schema = {
        "utd_config_context": {
            int: {
                "context_flag": int,
                "engine": str,
                "state": str,
                "sn_redirect": str,
                "redirect_type": str,
                "threat_inspection": str,
                "defense_mode": str,
                "domain_filtering": str,
                "url_filtering": str,
                "all_interface": str,
                "file_inspection": str,
            }
        }
    }

# ==============================================
# Parser for 'show sdwan utd dataplane config'
# ==============================================

class ShowSdwanUtdDataplaneConfig(ShowSdwanUtdDataplaneConfigSchema):
    """parser for "show sdwan utd dataplane config" """

    cli_command = "show sdwan utd dataplane config"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # utd-dp config context 0
        p1 = re.compile(r"^utd-dp+\s+config+\s+context+\s+(?P<context_number>\d+)$")

        # context-flag      25493505
        p2 = re.compile(r"^context-flag+\s+(?P<context_flag>\d+)$")

        # engine            Standard
        # state             enabled
        # sn-redirect       fail-open
        # redirect-type     divert
        # threat-inspection not-enabled
        # defense-mode      not-enabled
        # domain-filtering  not-enabled
        # url-filtering     not-enabled
        # all-interface     enabled
        # file-inspection   enabled
        p3 = re.compile(r"^(?P<option_name>\S+)\s+(?P<option_value>\S+)$")

        parsed_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # utd-dp config context 0
            m1 = p1.match(line)
            if m1:
                groups = m1.groupdict()
                config_context = parsed_dict.setdefault(
                    "utd_config_context", {}
                ).setdefault(int(groups["context_number"]), {})
                continue

            # context-flag      25493505
            m2 = p2.match(line)
            if m2:
                groups = m2.groupdict()
                config_context.update({"context_flag": int(groups["context_flag"])})
                continue

            # engine            Standard
            # state             enabled
            # sn-redirect       fail-open
            # redirect-type     divert
            # threat-inspection not-enabled
            # defense-mode      not-enabled
            # domain-filtering  not-enabled
            # url-filtering     not-enabled
            # all-interface     enabled
            # file-inspection   enabled
            m3 = p3.match(line)
            if m3:
                groups = m3.groupdict()
                config_context.update(
                    {groups["option_name"].replace("-", "_"): groups["option_value"]}
                )
                continue

        return parsed_dict

# =======================================================================
# Parser Schema for 'show sdwan app-fwd dpi flows'
# =======================================================================


class ShowSdwanAppFwdDpiFlowsSchema(MetaParser):

    """Schema for "show sdwan app-fwd dpi flows" """

    schema = {
        "vpn_id": {
            Any(): ListOf(
                {
                    "source_ip": str,
                    "destination_ip": str,
                    "source_port": int,
                    "destination_port": int,
                    "dscp": int,
                    "ip_protocol": int,
                    "tcp_cntrl_bits": int,
                    "icmp_opcode": int,
                    "total_pkts": int,
                    "total_bytes": int,
                    "egress_intf_name": str,
                    "ingress_intf_name": str,
                    "application": str,
                    "family": str,
                    "drop_cause": str,
                    "drop_octets": int,
                    "drop_packets": int,
                    "sla_not_met": int,
                    "color_not_met": int,
                    "queue_id": int,
                    "tos": int,
                    "dscp_output": int,
                    "sampler_id": int,
                    "fec_d_pkts": int,
                    "fec_r_pkts": int,
                    "pkt_dup_d_pkts_orig": int,
                    "pkt_dup_d_pkts_dup": int,
                    "pkt_dup_r_pkts": int,
                    "pkt_cxp_d_pkts": int,
                    "traffic_category": int,
                    "service_area": int,
                    "ssl_read_bytes": int,
                    "ssl_written_bytes": int,
                    "ssl_en_read_bytes": int,
                    "ssl_en_written_bytes": int,
                    "ssl_de_read_bytes": int,
                    "ssl_de_written_bytes": int,
                    "ssl_service_type": int,
                    "ssl_traffic_type": int,
                    "ssl_policy_action": int,
                    "appqoe_action": int,
                    "appqoe_sn_ip": str,
                    "appqoe_pass_reason": int,
                    "appqoe_dre_input_bytes": int,
                    "appqoe_dre_input_packets": int,
                    "appqoe_flags": int,
                }
            )
        }
    }


# ==============================================
# Parser for 'show sdwan app-fwd dpi flows'
# ==============================================


class ShowSdwanAppFwdDpiFlows(ShowSdwanAppFwdDpiFlowsSchema):
    """parser for "show sdwan app-fwd dpi flows" """

    cli_command = "show sdwan app-fwd dpi flows"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # app-fwd cflowd flows vpn 100 src-ip 184.118.1.123 dest-ip 192.168.101.5 src-port 80 dest-port 1360 dscp 32 ip-proto 6
        p1 = re.compile(
            r"^app-fwd+\s+cflowd+\s+flows+\s+vpn+\s+(?P<vpn_id>\d+)\s+src-ip+\s+(?P<source_ip>\S+)"
            r"\s+dest-ip+\s+(?P<dest_ip>\S+)\s+src-port+\s+(?P<src_port>\d+)\s+dest-port+\s+"
            r"(?P<dest_port>\d+)\s+dscp+\s+(?P<dscp>\d+)\s+ip-proto+\s+(?P<ip_proto>\d+)$"
        )

        # tcp-cntrl-bits           18
        # icmp-opcode              0
        # total-pkts               8
        # total-bytes              448
        # start-time               "Thu Oct 20 08:52:40 2022"
        # egress-intf-name         Null
        # ingress-intf-name        GigabitEthernet2
        # application              unknown
        # family                   network-service
        # drop-cause               FirewallPolicy
        # drop-octets              448
        # drop-packets             8
        # sla-not-met              0
        # color-not-met            0
        # queue-id                 2
        # tos                      0
        # dscp-output              0
        # sampler-id               0
        # fec-d-pkts               0
        # fec-r-pkts               0
        # pkt-dup-d-pkts-orig      0
        # pkt-dup-d-pkts-dup       0
        # pkt-dup-r-pkts           0
        # pkt-cxp-d-pkts           0
        # traffic-category         0
        # service-area             0
        # ssl-read-bytes           0
        # ssl-written-bytes        0
        # ssl-en-read-bytes        0
        # ssl-en-written-bytes     0
        # ssl-de-read-bytes        0
        # ssl-de-written-bytes     0
        # ssl-service-type         0
        # ssl-traffic-type         0
        # ssl-policy-action        0
        # appqoe-action            0
        # appqoe-sn-ip             0.0.0.0
        # appqoe-pass-reason       0
        # appqoe-dre-input-bytes   0
        # appqoe-dre-input-packets 0
        # appqoe-flags             0
        p2 = re.compile(r"^(?P<name>\S+)\s+(?P<value>\S+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # app-fwd cflowd flows vpn 100 src-ip 184.118.1.123 dest-ip 192.168.101.5 src-port 80 dest-port 1360 dscp 32 ip-proto 6
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                vpn_flows = ret_dict.setdefault("vpn_id", {}).setdefault(
                    int(groups["vpn_id"]), []
                )
                flow = {
                    "source_ip": groups["source_ip"],
                    "destination_ip": groups["dest_ip"],
                    "source_port": int(groups["src_port"]),
                    "destination_port": int(groups["dest_port"]),
                    "dscp": int(groups["dscp"]),
                    "ip_protocol": int(groups["ip_proto"]),
                }
                vpn_flows.append(flow)
                continue

            # tcp-cntrl-bits           18
            # icmp-opcode              0
            # total-pkts               8
            # total-bytes              448
            # start-time               "Thu Oct 20 08:52:40 2022"
            # egress-intf-name         Null
            # ingress-intf-name        GigabitEthernet2
            # application              unknown
            # family                   network-service
            # drop-cause               FirewallPolicy
            # drop-octets              448
            # drop-packets             8
            # sla-not-met              0
            # color-not-met            0
            # queue-id                 2
            # tos                      0
            # dscp-output              0
            # sampler-id               0
            # fec-d-pkts               0
            # fec-r-pkts               0
            # pkt-dup-d-pkts-orig      0
            # pkt-dup-d-pkts-dup       0
            # pkt-dup-r-pkts           0
            # pkt-cxp-d-pkts           0
            # traffic-category         0
            # service-area             0
            # ssl-read-bytes           0
            # ssl-written-bytes        0
            # ssl-en-read-bytes        0
            # ssl-en-written-bytes     0
            # ssl-de-read-bytes        0
            # ssl-de-written-bytes     0
            # ssl-service-type         0
            # ssl-traffic-type         0
            # ssl-policy-action        0
            # appqoe-action            0
            # appqoe-sn-ip             0.0.0.0
            # appqoe-pass-reason       0
            # appqoe-dre-input-bytes   0
            # appqoe-dre-input-packets 0
            # appqoe-flags             0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                value = groups["value"]
                flow.update(
                    {
                        groups["name"].replace("-", "_"): int(value)
                        if value.isnumeric()
                        else value
                    }
                )
                continue

        return ret_dict

# =======================================================================
# Parser Schema for 'show sdwan appqoe status'
# =======================================================================

class ShowSdwanAppqoeStatusSchema(MetaParser):

    """Schema for "show sdwan appqoe status" """

    schema = {
        "appqoe_status": str,
        "sslproxy_status": str,
        "tcpproxy_status": str,
        "service_chain_status": str,
        "resource_mgr_status": str
    }

# ==============================================
# Parser for 'show sdwan appqoe status'
# ==============================================

class ShowSdwanAppqoeStatus(ShowSdwanAppqoeStatusSchema):
    """parser for "show sdwan appqoe status" """

    cli_command = "show sdwan appqoe status"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # APPQOE Status : YELLOW
        p1 = re.compile(r"^APPQOE\s+Status\s+:\s+(?P<appqoe_st>\S+)$")

        # SSLPROXY : YELLOW
        p2 = re.compile(r"^SSLPROXY\s+:\s+(?P<ssl_st>\S+)$")

        # TCPPROXY : GREEN
        p3 = re.compile(r"^TCPPROXY\s+:\s+(?P<tcp_st>\S+)$")

        # SERVICE CHAIN : GREEN
        p4 = re.compile(r"^SERVICE\s+CHAIN\s+:\s+(?P<sc_st>\S+)$")

        # RESOURCE MANAGER : GREEN
        p5 = re.compile(r"^RESOURCE\s+MANAGER\s+:\s+(?P<rm_st>\S+)$")


        parsed_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # APPQOE Status : YELLOW
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"appqoe_status": groups["appqoe_st"]})
                continue

            # SSLPROXY : YELLOW
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"sslproxy_status": groups["ssl_st"]})
                continue

            # TCPPROXY : GREEN
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"tcpproxy_status": groups["tcp_st"]})
                continue

            # SERVICE CHAIN : GREEN
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"service_chain_status": groups["sc_st"]})
                continue

            # RESOURCE MANAGER : GREEN
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"resource_mgr_status": groups["rm_st"]})
                continue
        return parsed_dict

# =======================================================================
# Parser Schema for 'show sdwan appqoe service-chain status'
# =======================================================================

class ShowSdwanAppqoeServiceChainStatusSchema(MetaParser):

    """Schema for "show sdwan appqoe service-chain status" """

    schema = {
        "snort_state": str,
        "dre_state": str,
        "httpopt_state": str
    }

# ==============================================
# Parser for 'show sdwan appqoe service-chain status'
# ==============================================

class ShowSdwanAppqoeServiceChainStatus(ShowSdwanAppqoeServiceChainStatusSchema):
    """parser for "show sdwan appqoe service-chain status" """

    cli_command = "show sdwan appqoe service-chain status"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # SNORT Connection          UP
        p1 = re.compile(r"^SNORT\s+Connection\s+(?P<snort_con_state>\S+)$")

        # DRE   Connection          UP
        p2 = re.compile(r"^DRE\s+Connection\s+(?P<dre_con_state>\S+)$")

        # HTTPOPT   Connection    DOWN
        p3 = re.compile(r"^HTTPOPT\s+Connection\s+(?P<httpopt_con_state>\S+)$")

        parsed_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # SNORT Connection          UP
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"snort_state": groups["snort_con_state"]})
                continue

            # DRE   Connection          UP
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"dre_state": groups["dre_con_state"]})
                continue

            # HTTPOPT   Connection    DOWN
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"httpopt_state": groups["httpopt_con_state"]})
                continue

        return parsed_dict

# =======================================================================
# Parser Schema for 'show sdwan appqoe dreopt status'
# =======================================================================

class ShowSdwanAppqoeDreoptStatusSchema(MetaParser):

    """Schema for "show sdwan appqoe dreopt status" """

    schema = {
        "dre_id": str,
        "dre_uptime": str,
        "health_status": str,
        "health_change_reason": str,
        "last_health_change_time": str,
        Optional("notification_send_time"): str,
        "dre_cache_status": str,
        "disk_cache_usage": str,
        "disk_latency": str,
        "profile_type": str,
        "max_connections": int,
        "max_fanout": int,
        "disk_size": str,
        "memory_size": str,
        "cpu_cores": int,
        "disk_encryption": str
    }

# ==============================================
# Parser for 'show sdwan appqoe dreopt status'
# ==============================================

class ShowSdwanAppqoeDreoptStatus(ShowSdwanAppqoeDreoptStatusSchema):
    """parser for "show sdwan appqoe dreopt status" """

    cli_command = "show sdwan appqoe dreopt status"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # DRE ID                                           : 52:54:dd:bd:23:b2-0184aba9c593-79a4a29c
        p1 = re.compile(r"^DRE\s+ID\s+:\s+(?P<id>\S+)$")

        # DRE uptime                                       : 07:10:46:10
        p2 = re.compile(r"^DRE\s+uptime\s+:\s+(?P<uptime>\S+)$")

        # Health status                                    : GREEN
        p3 = re.compile(r"^Health\s+status\s+:\s+(?P<status>\S+)$")

        # Health status change reason                      : None
        p4 = re.compile(r"^Health\s+status\s+change\s+reason\s+:\s+(?P<ch_reason>\S+)$")

        # Last health status change time                   : 07:10:46:10
        p5 = re.compile(r"^Last\s+health\s+status\s+change\s+time\s+:\s+(?P<ch_time>\S+)$")

        # Last health status notification sent time        : 1 second
        p6 = re.compile(r"^Last\s+health\s+status\s+notification\s+sent\s+time\s+:\s+(?P<send_time>\d+\s+\S+)$")

        # DRE cache status                                 : Active
        p7 = re.compile(r"^DRE\s+cache\s+status\s+:\s+(?P<cache_st>\S+)$")

        # Disk cache usage                                 : 0%
        p8 = re.compile(r"^Disk\s+cache\s+usage\s+:\s+(?P<cache_use>\d+%)$")

        # Disk latency                                     : 0 ms
        p9 = re.compile(r"^Disk\s+latency\s+:\s+(?P<latency>\d+\sms)$")

        # Profile type                               : S
        p10 = re.compile(r"^Profile type\s+:\s+(?P<type>\S+)$")

        # Maximum connections                        : 750
        p11 = re.compile(r"^Maximum\s+connections\s+:\s+(?P<connection>\d+)$")

        # Maximum fanout                             : 35
        p12 = re.compile(r"^Maximum\s+fanout\s+:\s+(?P<fanout>\d+)$")

        # Disk size                                  : 60 GB
        p13 = re.compile(r"^Disk\s+size\s+:\s+(?P<d_size>\d+\s\S+)$")

        # Memory size                                : 2048 MB
        p14 = re.compile(r"^Memory\s+size\s+:\s+(?P<m_size>\d+\s\S+)$")

        # CPU cores                                  : 1
        p15 = re.compile(r"^CPU\s+cores\s+:\s+(?P<cores>\d+)$")

        # Disk encryption                            : ON
        p16 = re.compile(r"^Disk\s+encryption\s+:\s+(?P<encr>\S+)$")

        parsed_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # DRE ID                                           : 52:54:dd:bd:23:b2-0184aba9c593-79a4a29c
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"dre_id": groups["id"]})
                continue

            # DRE   Connection          UP
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"dre_uptime": groups["uptime"]})
                continue

            # Health status                                    : GREEN
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"health_status": groups["status"]})
                continue

            # Health status change reason                      : None
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"health_change_reason": groups["ch_reason"]})
                continue

            # Last health status change time                   : 07:10:46:10
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"last_health_change_time": groups["ch_time"]})
                continue

            # Last health status notification sent time        : 1 second
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"notification_send_time": groups["send_time"]})
                continue

            # DRE cache status                                 : Active
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"dre_cache_status": groups["cache_st"]})
                continue

            # Disk cache usage                                 : 0%
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"disk_cache_usage": groups["cache_use"]})
                continue

            # Disk latency                                     : 0 ms
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"disk_latency": groups["latency"]})
                continue

            # Profile type                               : S
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"profile_type": groups["type"]})
                continue

            # Maximum connections                        : 750
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"max_connections": int(groups["connection"])})
                continue

            # Maximum fanout                             : 35
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"max_fanout": int(groups["fanout"])})
                continue

            # Disk size                                  : 60 GB
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"disk_size": groups["d_size"]})
                continue

            # Memory size                                : 2048 MB
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"memory_size": groups["m_size"]})
                continue

            # CPU cores                                  : 1
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"cpu_cores": int(groups["cores"])})
                continue

            # Disk encryption                            : ON
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"disk_encryption": groups["encr"]})
                continue

        return parsed_dict

# =======================================================================
# Parser Schema for 'show platform software sdwan service-chain database'
# =======================================================================

class ShowSdwanServiceChainDatabaseSchema(MetaParser):

    """Schema for "show platform software sdwan service-chain database" """

    schema = {
        "service_chain_db": {
            Any(): {
                "vrf": int,
                "label": str,
                "state": str,
                "services": {
                    Any(): {
                        "service_state": str,
                        "sequence": int,
                        Any():{
                            Any():{
                                Any():{
                                    'interface': str,
                                    'ip': str,
                                    'status': str
                                }
                            }
                        }
                    }
                }
            }
        }
    }
# =======================================================================
# Parser for 'show platform software sdwan service-chain database'
# =======================================================================
class ShowSdwanServiceChainDatabase(ShowSdwanServiceChainDatabaseSchema):
    """parser for "show platform software sdwan service-chain database" """

    cli_command = "show platform software sdwan service-chain database"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Chain-Name: SC3, VRF: 101, Label: 0x800409, State: Up
        p1 = re.compile(
            r"^Chain-Name:\s+(?P<sc>\S+),\s+VRF:\s+(?P<vrf>\d+),\s+"
            r"Label:\s+(?P<label>\S+),\s+State:\s+(?P<sc_status>\w+)$"
        )

        # Services:
        p2 = re.compile(r"^Services:$")

        # FW, State: Up
        p3 = re.compile(r"^(?P<service_name>(FW|IDS|IDP|SIG|NETSVC\d+)),\s+State:\s+(?P<ser_state>\S+)$")

        # Sequence   1
        p4 = re.compile(r"^Sequence\s+(?P<seq_no>\d+)$")

        # Transport HA pair-1:
        p5 = re.compile(r"^Transport\s+HA\s+pair-(?P<inst_num>\d+):$")

        # Active   Tx (GigabitEthernet3, 192.168.40.42  ): Up*
        p6 = re.compile(
            r"^(?P<inst_type>(Active|Backup))\s*Tx\s*\((?P<inst_tx_intf>\S+),\s*"
            r"(?P<inst_tx_ip>\S+)\s*\)\s*:\s*(?P<inst_tx_status>\w+)\*?$"
        )

        # Rx (GigabitEthernet3, 192.168.40.42  ): Up*
        p7 = re.compile(
            r"^Rx\s*\((?P<inst_rx_intf>\S+),\s*(?P<inst_rx_ip>\S+)\s*\)\s*:\s*(?P<inst_rx_status>\w+)\*?$"
        )
        services_db = {}
        for line in output.splitlines():
            line = line.strip()

            # Chain-Name: SC3, VRF: 101, Label: 0x800409, State: Up
            m = p1.match(line)
            if m:
                chain_dict = services_db.setdefault('service_chain_db', {})
                sc_name = m.groupdict()["sc"]
                sc_dict = chain_dict.setdefault(sc_name, {})
                sc_dict.update({"vrf": int(m.groupdict()["vrf"])})
                sc_dict.update({"label": m.groupdict()["label"]})
                sc_dict.update({"state": m.groupdict()["sc_status"]})
                continue

            # Services:
            m = p2.match(line)
            if m:
                ser_dict = sc_dict.setdefault("services", {})

            # FW, State: Up
            m = p3.match(line)
            if m:
                service_type = m.groupdict()["service_name"]
                type_dict = ser_dict.setdefault(service_type, {})
                type_dict.update({"service_state": m.groupdict()["ser_state"]})
                continue

            # Sequence   1
            m = p4.match(line)
            if m:
                type_dict.update({"sequence": int(m.groupdict()["seq_no"])})
                continue

            # Transport HA pair-1:
            m = p5.match(line)
            if m:
                ha_pair = m.groupdict()["inst_num"]
                ha_dict = type_dict.setdefault(ha_pair, {})
                continue

            # Active   Tx (GigabitEthernet3, 192.168.40.42  ): Up*
            m = p6.match(line)
            if m:
                ha_type = m.groupdict()["inst_type"]
                hatype_dict = ha_dict.setdefault(ha_type, {})
                dir_tx_dict = hatype_dict.setdefault('tx', {})
                dir_tx_dict.update({"interface": m.groupdict()["inst_tx_intf"]})
                dir_tx_dict.update({"ip": m.groupdict()["inst_tx_ip"]})
                dir_tx_dict.update({"status": m.groupdict()["inst_tx_status"]})
                continue

            # Rx (GigabitEthernet3, 192.168.40.42  ): Up*
            m = p7.match(line)
            if m:
                dir_rx_dict = hatype_dict.setdefault('rx', {})
                dir_rx_dict.update({"interface": m.groupdict()["inst_rx_intf"]})
                dir_rx_dict.update({"ip": m.groupdict()["inst_rx_ip"]})
                dir_rx_dict.update({"status": m.groupdict()["inst_rx_status"]})
                continue

        return services_db

# ================================================================================================
# Parser Schema for 'show platform hardware qfp active feature sdwan datapath service-chain stats'
# ================================================================================================

class ShowSdwanServiceChainStatsSchema(MetaParser):

    """Schema for "show platform hardware qfp active feature sdwan datapath service-chain stats" """

    schema = {
        "service_chain_stats": {
            Any(): {
                "global_stats": int,
                Any(): {
                    "tx_pkts": int,
                    "rx_pkts": int
                }
            }
        }
    }
# =========================================================================================
# Parser for 'show platform hardware qfp active feature sdwan datapath service-chain stats'
# =========================================================================================
class ShowSdwanServiceChainStats(ShowSdwanServiceChainStatsSchema):
    """parser for "show platform software sdwan service-chain database" """

    cli_command = "show platform hardware qfp active feature sdwan datapath service-chain stats"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Service-Chain ID: 4
        p1 = re.compile(r"^Service-Chain ID:\s+(?P<sc_id>\S+)$")

        # Global stats: 110167
        p2 = re.compile(r"^Global stats:\s+(?P<gbl_stats>\S+)$")

        # Service: Firewall
        p3 = re.compile(r"^Service:\s+(?P<srv_name>\S+)$")

        # Tx pkt: 110167
        p4 = re.compile(r"^Tx pkt:\s+(?P<tx_pkt>\S+)$")

        # Rx pkt: 110167
        p5 = re.compile(r"^Rx pkt:\s+(?P<rx_pkt>\S+)$")

        services_tr_stats = {}
        for line in output.splitlines():
            line = line.strip()

            # Service-Chain ID: 4
            m = p1.match(line)
            if m:
                services_stats = services_tr_stats.setdefault("service_chain_stats", {})
                sc = m.groupdict()["sc_id"]
                sc_dict = services_stats.setdefault("SC" + sc, {})
                continue

            # Global stats: 110167
            m = p2.match(line)
            if m:
                sc_dict.update({"global_stats": int(m.groupdict()["gbl_stats"])})
                continue

            # Service: Firewall
            m = p3.match(line)
            if m:
                srv_name = m.groupdict()["srv_name"]
                svr_dict = sc_dict.setdefault(srv_name, {})
                continue

            # Tx pkt: 110167
            m = p4.match(line)
            if m:
                svr_dict.update({"tx_pkts": int(m.groupdict()["tx_pkt"])})
                continue

            # Rx pkt: 110167
            m = p5.match(line)
            if m:
                svr_dict.update({"rx_pkts": int(m.groupdict()["rx_pkt"])})
                continue

        return services_tr_stats

# =======================================================================
# Parser Schema for 'show sdwan policy data-policy-filter'
# 'show sdwan policy data-policy-filter <policy>'
# =======================================================================
class ShowSdwanPolicyDataPolicyFilterSchema(MetaParser):

    """Schema for "show platform hardware qfp active feature sdwan datapath service-chain stats" """

    schema = {
        "data_policy_filter": {
            Any(): {
                Any():{
                    Any(): {
                        "packets": int,
                        "bytes": int
                    }
                }
            }
        }
    }
# =======================================================================
# Parser for 'show sdwan policy data-policy-filter',                    #
# 'show sdwan policy data-policy-filter <policy>'                       #
# =======================================================================
class ShowSdwanPolicyDataPolicyFilter(ShowSdwanPolicyDataPolicyFilterSchema):
    """Parser for
           'show sdwan policy data-policy-filter'
           'show sdwan policy data-policy-filter <policy>'
    """
    cli_command = ['show sdwan policy data-policy-filter',
                'show sdwan policy data-policy-filter {policy}']

    def cli(self, policy="", output=None):
        if output is None:
            if policy:
                output = self.device.execute(self.cli_command[1].format(policy=policy))
            else:
                output = self.device.execute(self.cli_command[0])

        ret_dict = {}
        # data-policy-filter DP_HUB_LOCAL_FROM_TUNNEL
        p1 = re.compile(r'^data-policy-filter\s+(?P<policy_name>\S+)$')

        # data-policy-vpnlist VPN1
        p2 = re.compile(r'^data-policy-vpnlist\s+(?P<vpn_name>\S+)$')

        # data-policy-counter default_action_count
        p3 = re.compile(r'^data-policy-counter\s+(?P<counter_name>\S+)$')

        # packets 0
        p4 = re.compile(r'^packets\s+(?P<pkts_count>\d+)$')

        # bytes   0
        p5 = re.compile(r'^bytes\s+(?P<bytes_count>\d+)$')

        policy_stats = {}
        for line in output.splitlines():
            line = line.strip()

            # data-policy-filter DP_HUB_LOCAL_FROM_TUNNEL
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                policy_dict = ret_dict.setdefault('data_policy_filter', {}).\
                    setdefault(groups['policy_name'],{})
                continue

            # data-policy-vpnlist VPN1
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                vpn_dict = policy_dict.setdefault(groups['vpn_name'], {})
                continue

            # data-policy-counter default_action_count
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                counter_dict = vpn_dict.setdefault(groups['counter_name'], {})
                continue

            # packets 0
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                counter_dict.update({"packets": int(m.groupdict()["pkts_count"])})
                continue

            # bytes   0
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                counter_dict.update({"bytes": int(m.groupdict()["bytes_count"])})
                continue

        return(ret_dict)


# =============================================================
# Parser for 'show sdwan tenant-summary'
# =============================================================

class ShowSdwanTenantSumarySchema(MetaParser):
    """Schema for: show sdwan tenant-summary"""

    schema = {
        "max_tenants": int,
        "active_tenants": int,
        Optional("org_name"): {
                    Any() :{
                        Optional("global_id"): int,
                        Optional("uuid"): str,
                    },
                },
            }

class ShowSdwanTenantSumary(ShowSdwanTenantSumarySchema):
    """Parser for: show sdwan tenant-summary"""

    cli_command = 'show sdwan tenant-summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}
        ret_dict ['org_name'] = {}

        #tenants-summary max-tenants 30
        p1 = re.compile(r'^\s*tenants\-summary max\-tenants\s*(?P<max_tenants>\d+)')

        #tenants-summary num-active-tenants 20
        p2 = re.compile(r'^\s*tenants\-summary num\-active\-tenants\s*(?P<active_tenants>\d+)')

        #mttedge-Tenant42   45187   0bf871da-c63c-4043-8f85-386c1f0db2b8
        p3 = re.compile(r'^\s*(?P<org_name>[\w\d\-]+)\s*(?P<global_id>\d+)\s*(?P<uuid>[\w\d\-]+)')

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            #tenants-summary max-tenants 30
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['max_tenants'] = int(groups['max_tenants'])
                continue

            #tenants-summary num-active-tenants 20
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['active_tenants'] = int(groups['active_tenants'])
                continue

            #mttedge-Tenant42   45187   0bf871da-c63c-4043-8f85-386c1f0db2b8
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                org_name = groups['org_name']
                ret_dict['org_name'][org_name]={}
                ret_dict['org_name'][org_name]['global_id'] = int(groups['global_id'])
                ret_dict['org_name'][org_name]['uuid'] = groups['uuid']
                continue

        return ret_dict

# =============================================================
# Parser for 'show sdwan tenant <tenant> omp peers'
# =============================================================

class ShowSdwanTenantOmpPeersSchema(MetaParser):
    """Schema for: show sdwan tenant {tenant} omp peers"""

    schema = {
        "tenant_id": int,
        "peer": {
                    Any() :{
                        "type": str,
                        "domain_id": int,
                        "overlay_id": int,
                        "site_id": int,
                        "region_id": str,
                        "state": str,
                        "uptime": str,
                        "r_i_s": str,
                    },
                },
            }

class ShowSdwanTenantOmpPeers(ShowSdwanTenantOmpPeersSchema):
    """Parser for: show sdwan tenant {tenant} omp peers"""

    cli_command = 'show sdwan tenant {tenant} omp peers'

    def cli(self, tenant="", output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(tenant=tenant))
        else:
            out = output

        # initial variables
        ret_dict = {}
        ret_dict ['peer'] = {}

        #17890     1.0.0.37         vsmart  1         1         37        None      up       1:04:13:23       65/13/25
        p1 = re.compile(r'^\s*(?P<tenant_id>\d+)\s*(?P<peer>[\d\.]+)\s*(?P<type>\w+)\s*(?P<domain_id>\d+)\s*(?P<overlay_id>\d+)\s*(?P<site_id>\d+)\s*(?P<region_id>\w+)\s*(?P<state>\w+)\s*(?P<uptime>[\d\:]+)\s*(?P<r_i_s>[\d\/]+)')

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            #17890     1.0.0.37         vsmart  1         1         37        None      up       1:04:13:23       65/13/25
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['tenant_id'] = int(groups['tenant_id'])
                peer = groups['peer']
                ret_dict['peer'][peer]={}
                ret_dict['peer'][peer]['type'] = (groups['type'])
                ret_dict['peer'][peer]['domain_id'] = int(groups['domain_id'])
                ret_dict['peer'][peer]['overlay_id'] = int(groups['overlay_id'])
                ret_dict['peer'][peer]['site_id'] = int(groups['site_id'])
                ret_dict['peer'][peer]['region_id'] = (groups['region_id'])
                ret_dict['peer'][peer]['state'] = (groups['state'])
                ret_dict['peer'][peer]['uptime'] = (groups['uptime'])
                ret_dict['peer'][peer]['r_i_s'] = (groups['r_i_s'])
                continue

        return ret_dict

# =============================================================
# Parser for 'show sdwan tenant <tenant> omp routes'
# =============================================================

class ShowSdwanTenantOmpRoutesSchema(MetaParser):
    """Schema for: show sdwan tenant {tenant} omp routes"""

    schema = {
        "tenant": int,
        "vpn": {
                Any():{
                    "prefix": {
                            Any():{
                                "path_id":{
                                    Any(): {
                                        "from_peer": str,
                                        "label": int,
                                        "status": str,
                                        "attribute_type": str,
                                        "tloc_ip": str,
                                        "color": str,
                                        "encap": str,
                                        "preference": str,
                                        "affinity_group_number": str,
                                        "region_id": str,
                                        "region_path": str,
                                    },
                                },
                             },
                        },
                     },
                },
            }

class ShowSdwanTenantOmpRoutes(ShowSdwanTenantOmpRoutesSchema):
    """Parser for: show sdwan tenant {tenant} omp routes"""

    cli_command = 'show sdwan tenant {tenant} omp routes'

    def cli(self, tenant="", output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(tenant=tenant))
        else:
            out = output

        # initial variables
        ret_dict = {}
        ret_dict ['vpn'] = {}
        vpn1 = "x"

        #17890     2      115.1.90.0/24       0.0.0.0          66     1091     C,Red,R   installed  2.0.150.6        mpls             ipsec  -           None        None        -
        p1 = re.compile(r'^\s*(?P<tenant>\d+)\s+(?P<vpn>\d+)\s+(?P<prefix>[\d\.\/]+)\s+(?P<from_peer>[\d\.]+)\s+(?P<path_id>\d+)\s+(?P<label>\d+)\s+(?P<status>[\w\,]+)\s+(?P<attribute_type>\w+)\s+(?P<tloc_ip>[\d\.]+)\s+(?P<color>\w+)\s+(?P<encap>\w+)\s+(?P<preference>\S+)\s+(?P<affinity_group_number>\w+)\s+(?P<region_id>\w+)\s+(?P<region_path>\S)')


        #0.0.0.0          70     1091     C,Red,R   installed  2.0.150.6        lte              ipsec  -           None        None        -
        p2 = re.compile(r'^\s*(?P<from_peer>[\d\.]+)\s+(?P<path_id>\d+)\s+(?P<label>\d+)\s+(?P<status>[\w\,]+)\s+(?P<attribute_type>\w+)\s+(?P<tloc_ip>[\d\.]+)\s+(?P<color>\w+)\s+(?P<encap>\w+)\s+(?P<preference>\S+)\s+(?P<affinity_group_number>\w+)\s+(?P<region_id>\w+)\s+(?P<region_path>\S)')

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            #17890     2      115.1.90.0/24       0.0.0.0          66     1091     C,Red,R   installed  2.0.150.6        mpls             ipsec  -           None        None        -
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['tenant'] = int(groups['tenant'])
                vpn = groups['vpn']
                path_id = groups['path_id']
                prefix = groups['prefix']
                if vpn != vpn1:
                    ret_dict['vpn'][vpn]={}
                    vpn1 = vpn
                    ret_dict['vpn'][vpn]['prefix']={}
                ret_dict['vpn'][vpn]['prefix'][prefix]={}
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id']={}
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]={}
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]['from_peer'] = groups['from_peer']
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]['label'] = int(groups['label'])
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]['status'] = groups['status']
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]['attribute_type'] = (groups['attribute_type'])
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]['tloc_ip'] = (groups['tloc_ip'])
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]['color'] = (groups['color'])
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]['encap'] = (groups['encap'])
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]['preference'] = (groups['preference'])
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]['affinity_group_number'] = (groups['affinity_group_number'])
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]['region_id'] = (groups['region_id'])
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]['region_path'] = (groups['region_path'])
                continue

            #0.0.0.0          70     1091     C,Red,R   installed  2.0.150.6        lte              ipsec  -           None        None        -
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                path_id = groups['path_id']
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]={}
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]['from_peer'] = groups['from_peer']
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]['label'] = int(groups['label'])
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]['status'] = groups['status']
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]['attribute_type'] = (groups['attribute_type'])
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]['tloc_ip'] = (groups['tloc_ip'])
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]['color'] = (groups['color'])
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]['encap'] = (groups['encap'])
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]['preference'] = (groups['preference'])
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]['affinity_group_number'] = (groups['affinity_group_number'])
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]['region_id'] = (groups['region_id'])
                ret_dict['vpn'][vpn]['prefix'][prefix]['path_id'][path_id]['region_path'] = (groups['region_path'])


        return ret_dict

class ShowSdwanMulticastRemoteNodesSchema(MetaParser):
    """Schema for 'show platform software sdwan multicast remote-nodes vrf {vrf ID}' """

    schema = {
        "system_ip": {
            Any(): {
                "replicator" : str,
                "spt_only_mode": str,
                "msdp_i_work": str,
                "label": str,
                "received_xg": str,
                "received_sg": str,
                "sent_xg": str,
                "sent_sg": str,
            },
        },
    }

# =======================================================================
# Parser for 'show platform software sdwan multicast remote-nodes vrf {vrf ID}'
# =======================================================================
class ShowSdwanMulticastRemoteNodes(ShowSdwanMulticastRemoteNodesSchema):
    """parser for 'show platform software sdwan multicast remote-nodes vrf {vrf ID}' """

    cli_command = "show platform software sdwan multicast remote-nodes vrf {vrf_ID}"

    def cli(self, vrf_ID='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(vrf_ID=vrf_ID))
        else:
            output = output

        ret_dict = {}
        mcast_dict = {}

        # 5.0.0.2         No       No     1004        0/0        0/0        0/0        0/0
        #*6.0.0.2         No       No     1006        0/0        0/0        0/0        0/0
        p1 = re.compile(r'^\s*(?P<system_ip>[\*\d\.]+)\s+(?P<spt_mode>\w+)\s+(?P<msdp>\w+)\s+(?P<label>\d+)\s+'
                        r'(?P<received_xg>\d+\/\d+)\s+(?P<received_sg>\d+\/\d+)\s+(?P<sent_xg>\d+\/\d+)\s+(?P<sent_sg>\d+\/\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # 5.0.0.2         No       No     1004        0/0        0/0        0/0        0/0
            #*6.0.0.2         No       No     1006        0/0        0/0        0/0        0/0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                mcast_dict = ret_dict.setdefault('system_ip', {})
                if '*' in groups['system_ip']:
                    system_ip = groups['system_ip'].lstrip('*')
                    mcast_dict[system_ip] = {}
                    mcast_dict[system_ip]['replicator'] = 'Yes'
                else:
                    system_ip = groups['system_ip']
                    mcast_dict[system_ip] = {}
                    mcast_dict[system_ip]['replicator'] = 'No'
                mcast_dict[system_ip]['spt_only_mode'] = groups['spt_mode']
                mcast_dict[system_ip]['msdp_i_work'] = groups['msdp']
                mcast_dict[system_ip]['label'] = groups['label']
                mcast_dict[system_ip]['received_xg'] = groups['received_xg']
                mcast_dict[system_ip]['received_sg'] = groups['received_sg']
                mcast_dict[system_ip]['sent_xg'] = groups['sent_xg']
                mcast_dict[system_ip]['sent_sg'] = groups['sent_sg']
                continue

        return ret_dict


class ShowSdwanMulticastReplicatorsSchema(MetaParser):
    """Schema for 'show platform software sdwan multicast replicators vrf {vrf ID}' """

    schema = {
        "system_ip": {
            Any(): {
                "selected" : str,
                "preference" : str,
                "route_count": str,
                "threshold": str,
                "distance": str,
            },
        },
    }

# =======================================================================
# Parser for 'show platform software sdwan multicast replicators vrf {vrf ID}'
# =======================================================================
class ShowSdwanMulticastReplicators(ShowSdwanMulticastReplicatorsSchema):
    """parser for 'show platform software sdwan multicast replicators vrf {vrf ID}' """

    cli_command = "show platform software sdwan multicast replicators vrf {vrf_ID}"

    def cli(self, vrf_ID='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(vrf_ID=vrf_ID))
        else:
            output = output

        ret_dict = {}
        mcast_dict = {}

        #  6.0.0.2                       0            1         500             489
        # >7.0.0.1                       0            2         100               0
        p1 = re.compile(r'^\s*(?P<system_ip>[\>\d\.]+)\s+(?P<preference>\d+)\s+(?P<route_count>\d+)\s+(?P<threshold>\d+)\s+(?P<distance>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            #  6.0.0.2                       0            1         500             489
            # >7.0.0.1                       0            2         100               0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                mcast_dict = ret_dict.setdefault('system_ip', {})
                if '>' in groups['system_ip']:
                    system_ip = groups['system_ip'].lstrip('>')
                    mcast_dict[system_ip] = {}
                    mcast_dict[system_ip]['selected'] = 'Yes'
                else:
                    system_ip = groups['system_ip']
                    mcast_dict[system_ip] = {}
                    mcast_dict[system_ip]['selected'] = 'No'
                mcast_dict[system_ip]['preference'] = groups['preference']
                mcast_dict[system_ip]['route_count'] = groups['route_count']
                mcast_dict[system_ip]['threshold'] = groups['threshold']
                mcast_dict[system_ip]['distance'] = groups['distance']
                continue

        return ret_dict


# ===========================================================================
# Schema Parser for 'show sdwan security-info'
# ===========================================================================
class ShowSdwanSecurityInfoSchema(MetaParser):
    """Schema for 'show sdwan security-info' """

    schema = {
        "authentication_type"  : str,
        "rekey"                : str,
        "replay_window"        : str,
        "encryption_supported" : str,
        "fips_mode"            : str,
        "pairwise_keying"      : str,
        "pwk_sym_rekey"        : str,
        "extended_ar_window"   : str,
        "integrity_type"       : str,
    }

# ============================================================================
# Parser for 'show sdwan security-info'
# ============================================================================
class ShowSdwanSecurityInfo(ShowSdwanSecurityInfoSchema):
    """parser for 'show sdwan security-info' """

    cli_command = "show sdwan security-info"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output = output

        ret_dict = {}

        #security-info authentication-type deprecated
        p1 = re.compile(r'^\s*security-info\s+authentication-type\s+(?P<authentication_type>\w+)$')

        #security-info rekey 86400
        p2 = re.compile(r'^\s*security-info\s+rekey\s+(?P<rekey>\d+)$')

        #security-info replay-window 512
        p3 = re.compile(r'^\s*security-info\s+replay-window\s+(?P<replay_window>\d+)$')

        #security-info encryption-supported "AES_GCM_256 (and AES_256_CBC for multicast)"
        p4 = re.compile(r'^\s*security-info\s+encryption-supported\s+(?P<encryption_supported>\w+)$')

        #security-info fips-mode Disabled
        p5 = re.compile(r'^\s*security-info\s+fips-mode\s+(?P<fips_mode>\w+)$')

        #security-info pairwise-keying Disabled
        p6 = re.compile(r'^\s*security-info\s+pairwise-keying\s+(?P<pairwise_keying>\w+)$')

        #security-info pwk-sym-rekey Enabled
        p7 = re.compile(r'^\s*security-info\s+pwk-sym-rekey\s+(?P<pwk_sym_rekey>\w+)$')

        #security-info extended-ar-window Disabled
        p8 = re.compile(r'^\s*security-info\s+extended-ar-window\s+(?P<extended_ar_window>\w+)$')

        #security-info integrity-type "ip-udp-esp esp"
        p9 = re.compile(r'^\s*security-info\s+integrity-type\s+"(?P<integrity_type>.*)"$')

        for line in output.splitlines():
            if not line:
                continue

            #security-info authentication-type deprecated
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['authentication_type'] = groups['authentication_type']
                continue

            #security-info rekey 86400
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['rekey'] = groups['rekey']
                continue

            #security-info replay-window 512
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['replay_window'] = groups['replay_window']
                continue

            #security-info encryption-supported "AES_GCM_256 (and AES_256_CBC for multicast)"
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['encryption_supported'] = groups['encryption_supported'].strip('"')
                continue

            #security-info fips-mode Disabled
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['fips_mode'] = groups['fips_mode']
                continue

            #security-info pairwise-keying Disabled
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['pairwise_keying'] = groups['pairwise_keying']
                continue

            #security-info pwk-sym-rekey Enabled
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['pwk_sym_rekey'] = groups['pwk_sym_rekey']
                continue

            #security-info extended-ar-window Disabled
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['extended_ar_window'] = groups['extended_ar_window']
                continue

            #security-info integrity-type "ip-udp-esp esp"
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['integrity_type'] = groups['integrity_type']
                continue

        return ret_dict


# =====================================================================================================
# Schema Parser for 'show platform hardware qfp active feature sdwan client interface <interface name>'
# =====================================================================================================
class ShowSdwanClientInterfaceSchema(MetaParser):
    """Schema for 'show platform hardware qfp active feature sdwan client interface <interface name>' """

    schema = {
        "tloc_extension_output_uidb"        : str,
        "interface_color"                   : str,
        "bfd_default_dscp"                  : str,
        "interface_class_exmem_address"     : str,
        "interface_rewrite_exmem_address"   : str,
        "explicit_input_acl_cfg"            : str,
        "wan_interface"                     : str,
        "sig_tun_src"                       : str,
        "standard_ipsec_tun_src"            : str,
        "standard_ipsec_tun_all"            : str,
        "standard_ssl_tun_all"              : str,
        "interface_ip"                      : str,
        "tloc_ext_gre_dst_ip"               : str,
        "path_monitor_send_num"             : str,
        "path_monitor_recv_num"             : str,
        "service" : {
            Any(): {
                "allowed"                   : str,
            },

        },
    }

# ==============================================================================================
# Parser for 'show platform hardware qfp active feature sdwan client interface <interface name>'
# ==============================================================================================
class ShowSdwanClientInterface(ShowSdwanClientInterfaceSchema):
    """parser for 'show platform hardware qfp active feature sdwan client interface <interface name>' """

    cli_command = "show platform hardware qfp active feature sdwan client interface {interface_name}"

    def cli(self, interface_name='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface_name=interface_name))
        else:
            output = output

        ret_dict = {}
        srv_dict = {}

        #Tloc extension output uidb  : 0xffffffff
        p1 = re.compile(r'^\s*Tloc\s+extension\s+output\s+uidb\s+:\s+(?P<tloc_extension_output_uidb>\w+)$')

        #Interface color        : private1
        p2 = re.compile(r'^\s*Interface\s+color\s+:\s+(?P<interface_color>(.*))$')

        #BFD Default DSCP       : 0x30
        p3 = re.compile(r'^\s*BFD\s+Default\s+DSCP\s+:\s+(?P<bfd_default_dscp>\w+)$')

        #Interface class exmem address   : 0x0
        p4 = re.compile(r'^\s*Interface\s+class\s+exmem\s+address\s+:\s+(?P<interface_class_exmem_address>\w+)$')

        #Interface rewrite exmem address   : 0x0
        p5 = re.compile(r'^\s*Interface\s+rewrite\s+exmem\s+address\s+:\s+(?P<interface_rewrite_exmem_address>\w+)$')

        #Explicit input ACL cfg :  Yes
        p6 = re.compile(r'^\s*Explicit\s+input\s+ACL\s+cfg\s+:\s+(?P<explicit_input_acl_cfg>\w+)$')

        #WAN interface          :  Yes
        p7 = re.compile(r'^\s*WAN\s+interface\s+:\s+(?P<wan_interface>\w+)$')

        #SIG Tun src            :  No
        p8 = re.compile(r'^\s*SIG\s+Tun\s+src\s+:\s+(?P<sig_tun_src>\w+)$')

        #Standard IPSec Tun src :  No
        p9 = re.compile(r'^\s*Standard\s+IPSec\s+Tun\s+src\s+:\s+(?P<standard_ipsec_tun_src>\w+)$')

        #Standard IPSec Tun all :  No
        p10 = re.compile(r'^\s*Standard\s+IPSec\s+Tun\s+all\s+:\s+(?P<standard_ipsec_tun_all>\w+)$')

        #Standard SSL Tun all   :  No
        p11 = re.compile(r'^\s*Standard\s+SSL\s+Tun\s+all\s+:\s+(?P<standard_ssl_tun_all>\w+)$')

        #Interface IP           : 0.0.0.0
        p12 = re.compile(r'^\s*Interface\s+IP\s+:\s+(?P<interface_ip>.*)$')

        #TLOC Ext GRE Dst IP    : 0.0.0.0
        p13 = re.compile(r'^\s*TLOC\s+Ext\s+GRE\s+Dst\s+IP\s+:\s+(?P<tloc_ext_gre_dst_ip>.*)$')

        #Path Monitor send num  : 0
        p14 = re.compile(r'^\s*Path\s+Monitor\s+send\s+num\s+:\s+(?P<path_monitor_send_num>\d+)$')

        #Path Monitor recv num  : 0
        p15 = re.compile(r'^\s*Path\s+Monitor\s+recv\s+num\s+:\s+(?P<path_monitor_recv_num>\d+)$')

        #all       :  Yes
        #bgp       :  No
        #dhcp      :  Yes
        p16 = re.compile(r'^\s*(?P<service_name>\w+)\s+:\s+(?P<allowed>\w+)$')

        for line in output.splitlines():
            if not line:
                continue

            #Tloc extension output uidb  : 0xffffffff
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['tloc_extension_output_uidb'] = groups['tloc_extension_output_uidb']
                continue

            #Interface color        : private1
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['interface_color'] = groups['interface_color']
                continue

            #BFD Default DSCP       : 0x30
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['bfd_default_dscp'] = groups['bfd_default_dscp']
                continue

            #Interface class exmem address   : 0x0
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['interface_class_exmem_address'] = groups['interface_class_exmem_address']
                continue

            #Interface rewrite exmem address   : 0x0
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['interface_rewrite_exmem_address'] = groups['interface_rewrite_exmem_address']
                continue

            #Explicit input ACL cfg :  Yes
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['explicit_input_acl_cfg'] = groups['explicit_input_acl_cfg']
                continue

            #WAN interface          :  Yes
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['wan_interface'] = groups['wan_interface']
                continue

            #SIG Tun src            :  No
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['sig_tun_src'] = groups['sig_tun_src']
                continue

            #Standard IPSec Tun src :  No
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['standard_ipsec_tun_src'] = groups['standard_ipsec_tun_src']
                continue

            #Standard IPSec Tun all :  No
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['standard_ipsec_tun_all'] = groups['standard_ipsec_tun_all']
                continue

            #Standard SSL Tun all   :  No
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['standard_ssl_tun_all'] = groups['standard_ssl_tun_all']
                continue

            #Interface IP           : 0.0.0.0
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['interface_ip'] = groups['interface_ip']
                continue

            #TLOC Ext GRE Dst IP    : 0.0.0.0
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['tloc_ext_gre_dst_ip'] = groups['tloc_ext_gre_dst_ip']
                continue

            #Path Monitor send num  : 0
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['path_monitor_send_num'] = groups['path_monitor_send_num']
                continue

            #Path Monitor recv num  : 0
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['path_monitor_recv_num'] = groups['path_monitor_recv_num']
                continue

            #all       :  Yes
            #bgp       :  No
            #dhcp      :  Yes
            p16 = re.compile(r'^\s*(?P<service_name>\w+)\s+:\s+(?P<allowed>\w+)$')
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                srv_dict = ret_dict.setdefault('service', {})
                service_name = groups['service_name']
                srv_dict[service_name] = {}
                srv_dict[service_name]['allowed'] = groups['allowed']
                continue

        return ret_dict


# ==============================================
# Schema for 'show sdwan omp multicast-routess'
# ==============================================
class ShowSdwanOmpMulticastRoutesSchema(MetaParser):

    """ Schema for "show sdwan omp multicast-routes" """

    schema = {
        'address-family': {
            Any(): {
                'vpn': {
                    Any(): {
                        'tenant': {
                            Any(): {
                                'originator' : {
                                    Any(): {
                                        'type' : str,
                                        'source_system_ip' : str,
                                        'destination_system_ip' : str,
                                        'group' : str,
                                        'source_mcast_ip' : str,
                                        'path_list': {
                                            Any(): {  # index
                                                'from_peer': str,
                                                'rp_address': str,
                                                'status': str,
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

# =============================================
# Parser for 'show sdwan omp multicast-routes'
# =============================================
class ShowSdwanOmpMulticastRoutes(ShowSdwanOmpMulticastRoutesSchema):

    """ Parser for "show sdwan omp multicast-routes" """

    cli_command = "show sdwan omp multicast-routes"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output = output

        ret_dict = {}

        #ipv4     0         (*,G)  2    7.0.0.4     5.0.0.6      225.0.0.1  100.200.2.1  1.0.0.17  100.200.2.1  C,R
        #         0         (*,G)  2    5.0.0.6     6.0.0.2      225.0.0.1  100.200.2.1  0.0.0.0   100.200.2.1  C,Red,R
        p1 = re.compile(r'^\s*(?P<af>\s+|\S+)\s+(?P<tenant>\d+)\s+(?P<type>\S+)\s+(?P<vpn>\d+)\s+(?P<src_orig>[\d\.]+)\s+(?P<dst>[\d\.]+)\s+'
                        r'(?P<group>[\d\.]+)\s+(?P<src_mcast>[\d\.]+)\s+(?P<peer>[\d\.]+)\s+(?P<rp>[\d\.]+|-)\s+(?P<status>[\w,]+)\s*$')

        #                                                                                1.0.0.18  100.200.2.1  C,R
        #                                                                                1.0.0.19  100.200.2.1  C,R
        #                                                                                1.0.0.20  100.200.2.1  C,I,R
        p2 = re.compile(r'^\s*(?P<peer>[\d\.]+)\s+(?P<rp>[\d\.]+|-)\s+(?P<status>[\w,]+)\s*$')

        for line in output.splitlines():

            #ipv4     0         (*,G)  2    7.0.0.4     5.0.0.6      225.0.0.1  100.200.2.1  1.0.0.17  100.200.2.1  C,R
            #         0         (*,G)  2    5.0.0.6     6.0.0.2      225.0.0.1  100.200.2.1  0.0.0.0   100.200.2.1  C,Red,R
            m = p1.match(line)
            if m:
                index = 1
                group = m.groupdict()
                if not re.match('^\s*$', group['af']):
                    af = group['af']
                vpn = group['vpn']
                tenant = group['tenant']
                originator = group['src_orig']
                af_dict = ret_dict.setdefault('address-family', {}).setdefault(af, {})
                vpn_dict = af_dict.setdefault('vpn', {}).setdefault(vpn, {})
                tenant_dict = vpn_dict.setdefault('tenant', {}).setdefault(tenant, {})
                route_info = tenant_dict.setdefault('originator', {}).setdefault(originator, {})
                route_info['type'] = group['type']
                route_info['source_system_ip'] = group['src_orig']
                route_info['destination_system_ip'] = group['dst']
                route_info['group'] = group['group']
                route_info['source_mcast_ip'] = group['src_mcast']
                path_dict = route_info.setdefault('path_list', {})
                path_dict[str(index)] = {}
                path_dict[str(index)]['from_peer'] = group['peer']
                path_dict[str(index)]['rp_address'] = group['rp']
                path_dict[str(index)]['status'] = group['status']
                index += 1

            #                                                                                1.0.0.18  100.200.2.1  C,R
            #                                                                                1.0.0.19  100.200.2.1  C,R
            #                                                                                1.0.0.20  100.200.2.1  C,I,R
            m = p2.match(line)
            if m:
                group = m.groupdict()
                path_dict[str(index)] = {}
                path_dict[str(index)]['from_peer'] = group['peer']
                path_dict[str(index)]['rp_address'] = group['rp']
                path_dict[str(index)]['status'] = group['status']
                index += 1

        return ret_dict


# ===================================================
# Schema for 'show sdwan omp multicast-auto-discover'
# ===================================================
class ShowSdwanOmpMulticastAutoDiscoverSchema(MetaParser):

    """ Schema for "show sdwan omp multicast-auto-discover" """

    schema = {
        'address-family': {
            Any(): {
                'vpn': {
                    Any(): {
                        'tenant': {
                            Any(): {
                                'originator' : {
                                    Any(): {
                                        'path_list': {
                                            Any(): {  # index
                                                'from_peer': str,
                                                'status': str,
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

# ===================================================
# Parser for 'show sdwan omp multicast-auto-discover'
# ===================================================
class ShowSdwanOmpMulticastAutoDiscover(ShowSdwanOmpMulticastAutoDiscoverSchema):

    """ Parser for "show sdwan omp multicast-auto-discover" """

    cli_command = "show sdwan omp multicast-auto-discover"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output = output

        ret_dict = {}

        #ipv4     0         2    5.0.0.2     1.0.0.17  C,R
        p1 = re.compile(r'^\s*(?P<af>\s+|\S+)\s+(?P<tenant>\d+)\s+(?P<vpn>\d+)\s+(?P<src_orig>[\d\.]+)\s+(?P<peer>[\d\.]+)\s+(?P<status>[\w,]+)\s*$')

        #                                    1.0.0.18  C,R
        p2 = re.compile(r'^\s*(?P<peer>[\d\.]+)\s+(?P<status>[\w,]+)\s*$')

        for line in output.splitlines():

            #ipv4     0         2    5.0.0.2     1.0.0.17  C,R
            m = p1.match(line)
            if m:
                index = 1
                group = m.groupdict()
                if not re.match('^\s*$', group['af']):
                    af = group['af']
                vpn = group['vpn']
                tenant = group['tenant']
                originator = group['src_orig']
                af_dict = ret_dict.setdefault('address-family', {}).setdefault(af, {})
                vpn_dict = af_dict.setdefault('vpn', {}).setdefault(vpn, {})
                tenant_dict = vpn_dict.setdefault('tenant', {}).setdefault(tenant, {})
                route_info = tenant_dict.setdefault('originator', {}).setdefault(originator, {})
                path_dict = route_info.setdefault('path_list', {})
                path_dict[str(index)] = {}
                path_dict[str(index)]['from_peer'] = group['peer']
                path_dict[str(index)]['status'] = group['status']
                index += 1

            #                                    1.0.0.18  C,R
            m = p2.match(line)
            if m:
                group = m.groupdict()
                path_dict[str(index)] = {}
                path_dict[str(index)]['from_peer'] = group['peer']
                path_dict[str(index)]['status'] = group['status']
                index += 1

        return ret_dict


# ==============================================================================================
#  Schema Parser for
# 'show sdwan policy service-path vpn {vpn} interface {interface} source-ip {source_ip} dest-ip {destination_ip} protocol {protocol}'
# 'show sdwan policy service-path vpn {vpn} interface {interface} source-ip {source_ip} dest-ip {destination_ip} protocol {protocol} {all}'
# ==============================================================================================
class ShowSdwanPolicyServicePathSchema(MetaParser):
    """Schema for
        'show sdwan policy service-path vpn {vpn} interface {interface} source-ip {source_ip} dest-ip {destination_ip} protocol {protocol}'
        'show sdwan policy service-path vpn {vpn} interface {interface} source-ip {source_ip} dest-ip {destination_ip} protocol {protocol} {all}'
   """

    schema = {
        "paths" : {
            Any(): { #index
                "next_hop_type"                   : str,
                Optional("source")                : str,
                Optional("source_port")           : int,
                Optional("destination")           : str,
                Optional("destination_port")      : int,
                Optional("local_color")           : str,
                Optional("remote_color")          : str,
                Optional("remote_system_ip")      : str,
                Optional("remote_ip")             : str,
                Optional("interface")             : str,
                Optional("index")                 : int,
            },
        },
        Optional("number_of_paths")               : int,
    }

# ==============================================================================================
# Parser for
# 'show sdwan policy service-path vpn {vpn} interface {interface} source-ip {source_ip} dest-ip {destination_ip} protocol {protocol}'
# 'show sdwan policy service-path vpn {vpn} interface {interface} source-ip {source_ip} dest-ip {destination_ip} protocol {protocol} {all}'
# ==============================================================================================
class ShowSdwanPolicyServicePath(ShowSdwanPolicyServicePathSchema):

    """Parser for
        'show sdwan policy service-path vpn {vpn} interface {interface} source-ip {source_ip} dest-ip {destination_ip} protocol {protocol}'
        'show sdwan policy service-path vpn {vpn} interface {interface} source-ip {source_ip} dest-ip {destination_ip} protocol {protocol} {all}'
    """

    cli_command = ['show sdwan policy service-path vpn {vpn} interface {interface} source-ip {source_ip} dest-ip {destination_ip} protocol {protocol}',
                   'show sdwan policy service-path vpn {vpn} interface {interface} source-ip {source_ip} dest-ip {destination_ip} protocol {protocol} {all}']

    def cli(self, vpn=None, interface=None, source_ip=None, destination_ip=None, protocol=None, all=None, output=None):
        if output is None:
            if not all:
                output = self.device.execute(self.cli_command[0].format(vpn=vpn,
                                                                        interface=interface,
                                                                        source_ip=source_ip,
                                                                        destination_ip=destination_ip,
                                                                        protocol=protocol))
            else:
                output = self.device.execute(self.cli_command[1].format(vpn=vpn,
                                                                        interface=interface,
                                                                        source_ip=source_ip,
                                                                        destination_ip=destination_ip,
                                                                        protocol=protocol,
                                                                        all=all))
        else:
            output = output

        ret_dict = {}
        index = 0

        #Number of possible next hops: 3
        p1 = re.compile(r'^\s*Number\s+of\s+possible\s+next\s+hops\s*:\s+(?P<number_of_paths>\d+)+$')

        #Next Hop: Remote
        p2 = re.compile(r'^\s*Next\s+Hop\s*:\s+(?P<next_hop_type>\w+)$')

        #Remote IP: 40.187.4.2, Interface TenGigabitEthernet1/0/6 Index: 14
        p3 = re.compile(r'^\s*Remote\s+IP\s*:\s+(?P<remote_ip>.*),\s+Interface\s+(?P<interface>.*)\s+Index\s*:\s+(?P<index>\d+)$')

        #Source: 40.185.4.1 12366 Destination: 40.185.20.1 12406 Local Color: blue Remote Color: blue Remote System IP: 6.0.0.2
        p4 = re.compile(r'^\s*Source\s*:\s+(?P<source>.*)\s+(?P<source_port>\d+)\s+Destination\s*:\s+(?P<destination>.*)\s+(?P<destination_port>\d+)\s+Local\s+Color\s*:\s+(?P<local_color>.*)\s+Remote\s+Color\s*:\s+(?P<remote_color>.*)\s+Remote\s+System\s+IP\s*:\s+(?P<remote_system_ip>.*)$')

        for line in output.splitlines():
            if not line:
                continue

            #Number of possible next hops: 3
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['number_of_paths'] = int(groups['number_of_paths'])
                continue

            #Next Hop: Remote
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                index += 1
                path_dict = ret_dict.setdefault('paths', {}).setdefault(index, {})
                path_dict['next_hop_type'] = groups['next_hop_type']
                continue

            #Remote IP: 40.187.4.2, Interface TenGigabitEthernet1/0/6 Index: 14
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                path_dict['remote_ip'] = groups['remote_ip']
                path_dict['interface'] = groups['interface']
                path_dict['index'] = int(groups['index'])
                continue

            #Source: 40.185.4.1 12366 Destination: 40.185.20.1 12406 Local Color: blue Remote Color: blue Remote System IP: 6.0.0.2
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                path_dict['source'] = groups['source']
                path_dict['source_port'] = int(groups['source_port'])
                path_dict['destination'] = groups['destination']
                path_dict['destination_port'] = int(groups['destination_port'])
                path_dict['local_color'] = groups['local_color']
                path_dict['remote_color'] = groups['remote_color']
                path_dict['remote_system_ip'] = groups['remote_system_ip']
                continue

        return ret_dict


    # =======================================================================
# Parser Schema for 'show sdwan appqoe dreopt statistics'
# =======================================================================


class ShowSdwanAppqoeDreoptStatisticsSchema(MetaParser):

    """Schema for "show sdwan appqoe dreopt statistics" """

    schema = {
        'total_connections': int,
        'max_concurrent_connections': int,
        'current_active_connections': int,
        'total_connection_resets': int,
        'total_original_bytes': str,
        'total_optimized_bytes': str,
        'overall_reduction_ratio': str,
        'disk_size_used': str,
        'cache_status': str,
        'cache_size': str,
        'cache_used': str,
        'oldest_data_in_cache': str,
        'replaced_last_hour_size': str,
        }

# ==============================================
# Parser for 'show sdwan appqoe dreopt statistics'
# ==============================================


class ShowSdwanAppqoeDreoptStatistics(ShowSdwanAppqoeDreoptStatisticsSchema):

    """ Parser for "show sdwan appqoe dreopt statistics" """

    cli_command = "show sdwan appqoe dreopt statistics"

    def cli(self, output=None):

        # if the user does not provide output to the parser
        # we need to get it from the device
        if not output:
            output = self.device.execute(self.cli_command)

        # Dreopt Statistics

        #Total connections                  : 15297
        p1 = re.compile(r"^Total\s+connections\s+:\s+(?P<total_connections>\S+)$")

        #Max concurrent connections         : 61
        p2 = re.compile(r"^Max\s+concurrent\s+connections\s+:\s+(?P<max_concurrent_connections>\S+)$")

        #Current active connections         : 36
        p3 = re.compile(r"^Current\s+active\s+connections\s+:\s+(?P<current_active_connections>\S+)$")

        #Total connection resets            : 0
        p4 = re.compile(r"^Total\s+connection\s+resets\s+:\s+(?P<total_connection_resets>\S+)$")

        #Total original bytes               : 56291 MB
        p5 = re.compile(r"^Total\s+original\s+bytes\s+:\s+(?P<total_original_bytes>\d+\s\S+)$")

        #Total optimized bytes              : 338 MB
        p6 = re.compile(r"^Total\s+optimized\s+bytes\s+:\s+(?P<total_optimized_bytes>\d+\s\S+)$")

        #Overall reduction ratio            : 99%
        p7 = re.compile(r"^Overall\s+reduction\s+ratio\s+:\s+(?P<overall_reduction_ratio>\S+)$")

        #Disk size used                     : 0%
        p8 = re.compile(r"^Disk\s+size\s+used\s+:\s+(?P<disk_size_used>\S+)$")

        #Cache status                       : Active
        p9 = re.compile(r"^Cache\s+status\s+:\s+(?P<cache_status>\S+)$")

        #Cache Size                         : 1191047 MB
        p10 = re.compile(r"^Cache\s+Size\s+:\s+(?P<cache_size>\d+\s\S+)$")

        #Cache used                         : 0%
        p11 = re.compile(r"^Cache\s+used\s+:\s+(?P<cache_used>\S+)$")

        #Oldest data in cache               : 86:08:46:46
        p12 = re.compile(r"^Oldest\s+data\s+in\s+cache\s+:\s+(?P<oldest_data_in_cache>\S+)$")

        #Replaced(last hour): size          : 0 MB
        p13 = re.compile(r"^Replaced\(last\s+hour\):\s+size\s+:\s+(?P<replaced_last_hour_size>\d+\s\S+)$")

        parsed_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #Total connections                  : 15297
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"total_connections": int(groups["total_connections"])})
                continue

            # Max concurrent connections         : 61
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"max_concurrent_connections": int(groups["max_concurrent_connections"])})
                continue

            # Current active connections         : 36
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"current_active_connections": int(groups["current_active_connections"])})
                continue

            # Total connection resets            : 0
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"total_connection_resets": int(groups["total_connection_resets"])})
                continue

            # Total original bytes               : 56291 MB
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"total_original_bytes": groups["total_original_bytes"]})
                continue

            # Total optimized bytes              : 338 MB
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"total_optimized_bytes": groups["total_optimized_bytes"]})
                continue

            # Overall reduction ratio            : 99%
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"overall_reduction_ratio": groups["overall_reduction_ratio"]})
                continue

            # Disk size used                     : 0%
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"disk_size_used": groups["disk_size_used"]})
                continue

            # Cache status                       : Active
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"cache_status": groups["cache_status"]})
                continue

            # Cache Size                         : 1191047 MB
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"cache_size": groups["cache_size"]})
                continue

            # Cache used                         : 78%
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"cache_used": groups["cache_used"]})
                continue

            # Oldest data in cache               : 86:08:46:46
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"oldest_data_in_cache": groups["oldest_data_in_cache"]})
                continue

            # Replaced(last hour): size          : 0 MB
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"replaced_last_hour_size": groups["replaced_last_hour_size"]})
                continue
        return parsed_dict

# =======================================================================
# Parser Schema for 'sh sdwan appqoe ad-statistics'
# =======================================================================

class ShSdwanAppqoeAdStatisticsSchema(MetaParser):

    """Schema for "sh sdwan appqoe ad-statistics" """

    schema = {
        'auto_discovery_option_length_mismatch': int,
        'auto_discovery_option_version_mismatch': int,
        'tcp_option_length_mismatch': int,
        'ad_role_set_to_none': int,
        'edge_ad_negotiation_start': int,
        'edge_ad_negotiation_done': int,
        'edge_rcvd_syn_ack_wo_ad_options': int,
        'edge_aoim_sync_needed': int,
        'core_ad_negotiation_start': int,
        'core_ad_negotiation_done': int,
        'core_rcvd_ack_wo_ad_options': int,
        'core_aoim_sync_needed': int,
        }

# ==============================================
# Parser for 'show sdwan appqoe dreopt statistics'
# ==============================================


class ShowSdwanAppqoeAdStatistics(ShSdwanAppqoeAdStatisticsSchema):

    """ Parser for "show sdwan appqoe ad-statistics" """

    cli_command = "show sdwan appqoe ad-statistics"

    def cli(self, output=None):

        # if the user does not provide output to the parser
        # we need to get it from the device
        if not output:
            output = self.device.execute(self.cli_command)

        # ad-statistics

        #Auto-Discovery Option Length Mismatch       : 0
        p1 = re.compile(r"^Auto-Discovery\s+Option\s+Length\s+Mismatch\s+:\s+(?P<auto_discovery_option_length>\S+)$")

        #Auto-Discovery Option Version Mismatch      : 0
        p2 = re.compile(r"^Auto-Discovery\s+Option\s+Version\s+Mismatch\s+:\s+(?P<auto_discovery_option_version>\S+)$")

        #Tcp Option Length Mismatch                  : 0
        p3 = re.compile(r"^Tcp\s+Option\s+Length\s+Mismatch\s+:\s+(?P<tcp_option_length_mismatch>\S+)$")

        #AD Role set to NONE                         : 0
        p4 = re.compile(r"^AD\s+Role\s+set\s+to\s+NONE\s+:\s+(?P<ad_role_set_to_none>\S+)$")

        #[Edge] AD Negotiation Start                 : 0
        p5 = re.compile(r"^.Edge.\s+AD\s+Negotiation\s+Start\s+:\s+(?P<edge_ad_negotiation_start>\S+)$")

        #[Edge] AD Negotiation Done                  : 0
        p6 = re.compile(r"^.Edge.\s+AD\s+Negotiation\s+Done\s+:\s+(?P<edge_ad_negotiation_done>\S+)$")

        #[Edge] Rcvd SYN-ACK w/o AD options          : 0
        p7 = re.compile(r"^.Edge.\s+Rcvd\s+SYN-ACK\s+w.o\s+AD\s+options\s+:\s+(?P<edge_rcvd_syn_ack_wo_ad_options>\S+)$")

        #[Edge] AOIM sync Needed                     : 0
        p8 = re.compile(r"^.Edge.\s+AOIM\s+sync\s+Needed\s+:\s+(?P<edge_aoim_sync_needed>\S+)$")

        #[Core] AD Negotiation Start                 : 0
        p9 = re.compile(r"^.Core.\s+AD\s+Negotiation\s+Start\s+:\s+(?P<core_ad_negotiation_start>\S+)$")

        #[Core] AD Negotiation Done                  : 0
        p10 = re.compile(r"^.Core.\s+AD\s+Negotiation\s+Done\s+:\s+(?P<core_ad_negotiation_done>\S+)$")

        #[Core] Rcvd ACK w/o AD options              : 0
        p11 = re.compile(r"^.Core.\s+Rcvd\s+ACK\s+w.o\s+AD\s+options\s+:\s+(?P<core_rcvd_ack_wo_ad_options>\S+)$")

        #[Core] AOIM sync Needed                     : 0
        p12 = re.compile(r"^.Core.\s+AOIM\s+sync\s+Needed\s+:\s+(?P<core_aoim_sync_needed>\S+)$")

        parsed_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #Auto-Discovery Option Length Mismatch       : 0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"auto_discovery_option_length_mismatch": int(groups["auto_discovery_option_length"])})
                continue

            #Auto-Discovery Option Version Mismatch      : 0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"auto_discovery_option_version_mismatch": int(groups["auto_discovery_option_version"])})
                continue

            #Tcp Option Length Mismatch                  : 0
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"tcp_option_length_mismatch": int(groups["tcp_option_length_mismatch"])})
                continue

            #AD Role set to NONE                         : 0
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"ad_role_set_to_none": int(groups["ad_role_set_to_none"])})
                continue

            #[Edge] AD Negotiation Start                 : 0
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"edge_ad_negotiation_start": int(groups["edge_ad_negotiation_start"])})
                continue

            #[Edge] AD Negotiation Done                  : 0
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"edge_ad_negotiation_done": int(groups["edge_ad_negotiation_done"])})
                continue

            #[Edge] Rcvd SYN-ACK w/o AD options          : 0
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"edge_rcvd_syn_ack_wo_ad_options": int(groups["edge_rcvd_syn_ack_wo_ad_options"])})
                continue

            #[Edge] AOIM sync Needed                     : 0
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"edge_aoim_sync_needed": int(groups["edge_aoim_sync_needed"])})
                continue

            #[Core] AD Negotiation Start                 : 0
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"core_ad_negotiation_start": int(groups["core_ad_negotiation_start"])})
                continue

            #[Core] AD Negotiation Done                  : 0
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"core_ad_negotiation_done": int(groups["core_ad_negotiation_done"])})
                continue

            #[Core] Rcvd ACK w/o AD options              : 0
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"core_rcvd_ack_wo_ad_options": int(groups["core_rcvd_ack_wo_ad_options"])})
                continue

            #[Core] AOIM sync Needed                     : 0
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"core_aoim_sync_needed": int(groups["core_aoim_sync_needed"])})
                continue

        return parsed_dict


# =======================================================================
# Parser Schema for 'show sdwan appqoe rm-statistics'
# =======================================================================

class ShowSdwanAppqoeRmStatisticsSchema(MetaParser):

    """Schema for "show sdwan appqoe rm-statistics" """

    schema = {
        'times_sessions_health_changed_yellow': int,
        'times_sessions_health_changed_green': int,
        'times_service_mem_health_changed_yellow': int,
        'times_service_mem_health_changed_green': int,
        'overall_health_changed_yellow': int,
        'overall_health_changed_green': int,
        'dre_reserve_failures_due_to_health_status': int,
        'client': {
            Any(): {
                'tcp_session_alloc': int,
                'tcp_session_free': int,
                'ssl_session_alloc': int,
                'ssl_session_free': int,
                'dre_session_alloc': int,
                'dre_session_free': int,
                'http_session_alloc': int,
                'http_session_free': int,
                },
            },
        }

# ==============================================
# Parser for 'show sdwan appqoe rm-statistics'
# ==============================================


class ShowSdwanAppqoeRmStatistics(ShowSdwanAppqoeRmStatisticsSchema):

    """ Parser for "show sdwan appqoe rm-statistics" """

    cli_command = "show sdwan appqoe rm-statistics"

    def cli(self, output=None):

        # if the user does not provide output to the parser
        # we need to get it from the device
        if not output:
            output = self.device.execute(self.cli_command)

        # rm-statistics

        #Times Sessions Health Changed Yellow      : 0
        p1 = re.compile(r"^Times\s+Sessions\s+Health\s+Changed\s+Yellow\s+:\s+(?P<session_yellow>\S+)$")

        #Times Sessions Health Changed Green       : 0
        p2 = re.compile(r"^Times\s+Sessions\s+Health\s+Changed\s+Green\s+:\s+(?P<session_green>\S+)$")

        #Times Service mem Health Changed Yellow   : 0
        p3 = re.compile(r"^Times\s+Service\s+mem\s+Health\s+Changed\s+Yellow\s+:\s+(?P<service_yellow>\S+)$")

        #Times Service mem Health Changed Green    : 0
        p4 = re.compile(r"^Times\s+Service\s+mem\s+Health\s+Changed\s+Green\s+:\s+(?P<service_green>\S+)$")

        #Overall Health Changed Yellow             : 0
        p5 = re.compile(r"^Overall\s+Health\s+Changed\s+Yellow\s+:\s+(?P<overall_health_changed_yellow>\S+)$")

        #Overall Health Changed Green              : 0
        p6 = re.compile(r"^Overall\s+Health\s+Changed\s+Green\s+:\s+(?P<overall_health_changed_green>\S+)$")

        #DRE Reserve Failures Due to Health Status : 34
        p7 = re.compile(r"^DRE\s+Reserve\s+Failures\s+Due\s+to\s+Health\s+Status\s+:\s+(?P<overall_health_yellow>\S+)$")

        #Client: TCP
        p8 = re.compile(r"^\s*Client:\s+(?P<client>\w+)\s*$")

        #TCP Session Alloc  : 8220905
        p9 = re.compile(r"^TCP\s+Session\s+Alloc\s+:\s+(?P<tcp_session_alloc>\S+)$")

        #TCP Session Free   : 8220552
        p10 = re.compile(r"^TCP\s+Session\s+Free\s+:\s+(?P<tcp_session_free>\S+)$")

        #SSL Session Alloc  : 0
        p11 = re.compile(r"^SSL\s+Session\s+Alloc\s+:\s+(?P<ssl_session_alloc>\S+)$")

        #SSL Session Free   : 0
        p12 = re.compile(r"^SSL\s+Session\s+Free\s+:\s+(?P<ssl_session_free>\S+)$")

        #DRE Session Alloc  : 0
        p13 = re.compile(r"^DRE\s+Session\s+Alloc\s+:\s+(?P<dre_session_alloc>\S+)$")

        #DRE Session Free   : 0
        p14 = re.compile(r"^DRE\s+Session\s+Free\s+:\s+(?P<dre_session_free>\S+)$")

        #HTTP Session Alloc  : 0
        p15 = re.compile(r"^HTTP\s+Session\s+Alloc\s+:\s+(?P<http_session_alloc>\S+)$")

        #HTTP Session Free   : 0
        p16 = re.compile(r"^HTTP\s+Session\s+Free\s+:\s+(?P<http_session_free>\S+)$")

        parsed_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #Times Sessions Health Changed Yellow      : 0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"times_sessions_health_changed_yellow": int(groups["session_yellow"])})
                continue

            #Times Sessions Health Changed Green       : 0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"times_sessions_health_changed_green": int(groups["session_green"])})
                continue

            #Times Service mem Health Changed Yellow   : 0
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"times_service_mem_health_changed_yellow": int(groups["service_yellow"])})
                continue

            #Times Service mem Health Changed Green    : 0
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"times_service_mem_health_changed_green": int(groups["service_green"])})
                continue

            #Overall Health Changed Yellow             : 0
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"overall_health_changed_yellow": int(groups["overall_health_changed_yellow"])})
                continue

            #Overall Health Changed Green              : 0
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"overall_health_changed_green": int(groups["overall_health_changed_green"])})
                continue

            #DRE Reserve Failures Due to Health Status : 34
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict.update({"dre_reserve_failures_due_to_health_status": int(groups["overall_health_yellow"])})
                continue

            #Client: TCP
            m = p8.match(line)
            if m:
                overall_client_dict= parsed_dict.setdefault("client", {})
                groups = m.groupdict()
                client_dict = overall_client_dict.setdefault(groups['client'], {})
                continue

            #TCP Session Alloc  : 8220905
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                client_dict.update({"tcp_session_alloc": int(groups["tcp_session_alloc"])})
                continue

            #TCP Session Free   : 8220552
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                client_dict.update({"tcp_session_free": int(groups["tcp_session_free"])})
                continue

            #SSL Session Alloc  : 0
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                client_dict.update({"ssl_session_alloc": int(groups["ssl_session_alloc"])})
                continue

            #SSL Session Free   : 0
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                client_dict.update({"ssl_session_free": int(groups["ssl_session_free"])})
                continue

            #DRE Session Alloc  : 0
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                client_dict.update({"dre_session_alloc": int(groups["dre_session_alloc"])})
                continue

            #DRE Session Free   : 0
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                client_dict.update({"dre_session_free": int(groups["dre_session_free"])})
                continue

            #HTTP Session Alloc  : 0
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                client_dict.update({"http_session_alloc": int(groups["http_session_alloc"])})
                continue

            #HTTP Session Free   : 0
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                client_dict.update({"http_session_free": int(groups["http_session_free"])})
                continue

        return parsed_dict

# =======================================================================
# Parser Schema for 'Show L2vpn Sdwan All'
# =======================================================================

class ShowL2vpnSdwanAllSchema(MetaParser):
    schema = {
        "l2vpn_sdwan_instance": {
            Any(): { #l2vpn sdwan instance
                "vpn_type": str,
                Optional("ip_local_learning")    : str,
                Optional("flooding_suppression") : str,
                "vc_id": int,
                "bridge_domain": int,
                "bridge_status": str,
                "local_l2vpn_status": str,
                "local_pseduoports": str,
                Optional("remote_sites"): {
                    Any() : { #remote site id
                        "remote_site" : str,
                        "l2_routes" : {
                            Any(): { #index
                                "system_ip": str,
                                "status": str,
                                "up_down_time": str,
                                "color": str,
                                "encap": str,
                                "label": int,
                                "df": str
                            }
                        }
                    }
                }
            }
        }
    }


# =======================================================================
# Parser for 'Show L2vpn Sdwan All'
# =======================================================================

class ShowL2vpnSdwanAll(ShowL2vpnSdwanAllSchema):

    """
    Parser for the output of "show l2vpn sdwan all"
    """

    cli_command = "show l2vpn sdwan all"

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)


        # L2VPN sdwan Instance : 1001
        p1 = re.compile(r'^L2VPN\s+sdwan\s+Instance\s+:\s+(?P<l2vpn_sdwan_instance>\d+)$')

        # VPN Type : point-to-point
        p2 = re.compile(r'^VPN\s+Type\s+:\s+(?P<vpn_type>\S+)$')

        #IP Local-learning    : Disabled
        p2_1 = re.compile(r'^IP\s+Local-learning\s+:\s+(?P<ip_local_learning>\S+)$')

        #Flooding Suppression : Disabled
        p2_2 = re.compile(r'^Flooding\s+Suppression\s+:\s+(?P<flooding_suppression>\S+)$')

        #   VC_ID: 1001 Bridge-domain: 1001 UP
        p3 = re.compile(r'^VC_ID:\s+(?P<vc_id>\d+)\s+Bridge-domain:\s+(?P<bridge_domain>\d+)\s+(?P<bridge_status>\S+)$')
        
        #    Local l2vpn status: UP
        p4 = re.compile(r'^Local\s+l2vpn\s+status:\s+(?P<local_l2vpn_status>\S+)$')
        
        #     Local Pseudoports: HundredGigE0/1/4 service instance 1001
        p5 = re.compile(r'^Local\s+Pseudoports:\s+(?P<local_pseduoports>.*)$')
        
        #    Remote Site: 603
        p6 = re.compile(r'^Remote\s+Site:\s+(?P<remote_site>\d+)$')

        #      6.0.0.3            UP           00:26:35   private1        ipsec    1036   N/A 
        p7 = re.compile(r'^(?P<system_ip>\d+.\d+.\d+.\d+)\s+(?P<status>\S+)\s+(?P<up_down_time>\S+)\s+(?P<color>\S+)\s+(?P<encap>\S+)\s+(?P<label>\d+)\s+(?P<df>\S+)')

    
        ret_dict = {}
        route_index = 1

        for line in output.splitlines():
            line = line.strip()

            # L2VPN sdwan Instance : 1001
            m = p1.match(line)
            if m:
                groups = m.groupdict() 
                l2vpn_sdwan_instance = int(groups['l2vpn_sdwan_instance'])
                l2vpn_sdwan_instance_dict = ret_dict.setdefault('l2vpn_sdwan_instance', {}).setdefault(l2vpn_sdwan_instance, {})
                continue

            # VPN Type : point-to-point
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                l2vpn_sdwan_instance_dict['vpn_type'] = groups['vpn_type']
                continue

            #IP Local-learning    : Disabled
            m = p2_1.match(line)
            if m:
                groups = m.groupdict()
                l2vpn_sdwan_instance_dict['ip_local_learning'] = groups['ip_local_learning']
                continue

            #Flooding Suppression : Disabled
            m = p2_2.match(line)
            if m:
                groups = m.groupdict()
                l2vpn_sdwan_instance_dict['flooding_suppression'] = groups['flooding_suppression']
                continue

            #   VC_ID: 1001 Bridge-domain: 1001 UP
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                l2vpn_sdwan_instance_dict['vc_id'] = int(groups['vc_id'])
                l2vpn_sdwan_instance_dict['bridge_domain'] = int(groups['bridge_domain'])
                l2vpn_sdwan_instance_dict['bridge_status'] = groups['bridge_status']
                continue

            #    Local l2vpn status: UP
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                l2vpn_sdwan_instance_dict['local_l2vpn_status'] = groups['local_l2vpn_status']
                continue

            #     Local Pseudoports: HundredGigE0/1/4 service instance 1001
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                l2vpn_sdwan_instance_dict['local_pseduoports'] = groups['local_pseduoports']
                continue

            #    Remote Site: 603
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                remote_site = groups['remote_site']
                remote_site_dict = l2vpn_sdwan_instance_dict.setdefault('remote_sites', {}).setdefault(remote_site,{})
                remote_site_dict['remote_site'] = remote_site
                route_index = 1
                continue

            #      6.0.0.3            UP           00:26:35   private1        ipsec    1036   N/A 
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                l2_route_dict = remote_site_dict.setdefault('l2_routes', {}).setdefault(route_index, {})
                l2_route_dict['system_ip'] = groups['system_ip']
                l2_route_dict['status'] = groups['status']
                l2_route_dict['up_down_time'] = groups['up_down_time']
                l2_route_dict['color'] = groups['color']
                l2_route_dict['encap'] = groups['encap']
                l2_route_dict['label'] = int(groups['label'])
                l2_route_dict['df'] = groups['df']
                route_index += 1
                continue

        return ret_dict
    
    
