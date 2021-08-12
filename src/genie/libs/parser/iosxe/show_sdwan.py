'''
* 'show sdwan appqoe aoim-statistics'
* 'show sdwan appqoe tcpopt status'
* 'show sdwan appqoe nat-statistics'
* 'show sdwan appqoe rm-resources'
* 'show sdwan appqoe flow all'
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
* 'show sdwan policy ipv6 access-list-associations'
* 'show sdwan policy access-list-associations'
* 'show sdwan policy access-list-counters'
* 'show sdwan policy ipv6 access-list-counters'
* 'show sdwan reboot history'
* 'show sdwan software'
* 'show sdwan system status'
* 'show sdwan version'
* 'show sdwan zonebfwdp sessions'
* 'show sdwan zbfw zonepair-statistics'
* 'show sdwan tunnel sla index 0'
'''

# Python
import re
# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And, Default, Use
import genie.parsergen as pg
from genie.libs.parser.viptela.show_bfd import ShowBfdSessions as ShowBfdSessions_viptela
from genie.libs.parser.viptela.show_bfd import ShowBfdSummary as ShowBfdSummary_viptela
from genie.libs.parser.viptela.show_control import ShowControlConnections as ShowControlConnections_viptela
from genie.libs.parser.viptela.show_control import ShowControlLocalProperties as ShowControlLocalProperties_viptela
from collections import OrderedDict
from genie.libs.parser.viptela.show_omp import ShowOmpSummary as ShowOmpSummary_viptela
from genie.libs.parser.viptela.show_omp import ShowOmpTlocs as ShowOmpTlocs_viptela
from genie.libs.parser.viptela.show_omp import ShowOmpPeers as ShowOmpPeers_viptela
from genie.libs.parser.viptela.show_omp import ShowOmpTlocPath as ShowOmpTlocPath_viptela
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
        p6 = re.compile(r'^(?P<key>[\s\S]+\S) +: +(?P<value>[\s\S]+)$')

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