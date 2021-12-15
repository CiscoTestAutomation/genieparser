"""show_mldp.py

IOSXE parsers for the following show commands:

    * show mpls mldp count
    * show mpls mldp root
    * show mpls mldp neighbors
    * show mpls mldp database
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

class ShowMplsMldpCountSchema(MetaParser):
    """Schema for:
        show mpls mldp count
    """
    schema = {
        'mldp_count': {
            'mldp_database_summary': {
                'number_of_mp2mp_entries': int,
                'number_of_p2mp_entries': int,
                'total_number_of_entries': int,
            },
            'mldp_root_count':{
                'total_number_of_mldp_roots': int
            },
            'mldp_neighbor_count':{
                'total_number_of_mldp_neighbors': int
            },
        }
    }

class ShowMplsMldpCount(ShowMplsMldpCountSchema):
    """Parser for:
        show mpls mldp count
    """
    cli_command = 'show mpls mldp count'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        
        if not out.strip():
            return ret_dict
            
        ##MLDP Database Summary:
        ##MLDP Root Count:
        ##MLDP Neighbor Count:
        p1 = re.compile(r'^([a-zA-Z ]+):$')
        
        ##Number of MP2MP Entries : 1
        p2 = re.compile(r'^([a-zA-Z0-9 ]+)\s*: (\d+)$')
        
        for line in out.splitlines():
            line=line.strip()
            
            ##MLDP Database Summary:
            ##MLDP Root Count:
            ##MLDP Neighbor Count:
            m=re.match(p1,line)
            if m:
                key = m.groups()[0].strip().lower().replace(" ","_")
                new_dict = ret_dict.setdefault('mldp_count',{}).setdefault(key,{})
                
            ##Number of MP2MP Entries : 1
            m=re.match(p2,line)
            if m:
                res = m.groups()
                new_dict.update({res[0].strip().lower().replace(" ","_"):int(res[1])})
               
        return ret_dict
        
class ShowMplsMldpRootSchema(MetaParser):
    """Schema for:
        show mpls mldp root
    """
    schema = {
        'root_node': {
            Any(): {
                'metric': int,
                'distance': int,
                'interface': str,
                'learnet_via': str,
                'fec_count': int,
                'path_count': int,
                'ldp_neigh': str,
                'path':str
            },
        }
    }

class ShowMplsMldpRoot(ShowMplsMldpRootSchema):
    """Parser for:
        show mpls mldp root
    """
    cli_command = 'show mpls mldp root'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        
        if not out.strip():
            return ret_dict
            
        ##Path(s)     : 26.1.1.2         LDP nbr: 3.3.3.3:0         Port-channel30
        p1 = re.compile(r"^Path\(s\)\s+\:\s+(?P<path>\S+)\s+[a-zA-z ]+:\s+(?P<ldp_neigh>\S+)\s+(?P<interface>[a-zA-Z0-9\- ]+)$")
        
        ##Interface   : Port-channel30 (via unicast RT)
        p2 = re.compile(r"^Interface\s+\:\s+(?P<interface>\S+)\s+\(via\s+(?P<learnet_via>[a-zA-Z ]+)\)$")
        
        ## Root node    : 5.5.5.5  (we are the root)
        p3 = re.compile(r"^Root\s+node\s+:\s+(?P<root_node>\S+).*$")
        
        for line in out.splitlines():
            line=line.strip()
            if line:
                res=line.split(":")
                
                ##Root node    : 5.5.5.5
                m=p3.match(line)
                if m:
                    root_dict=ret_dict.setdefault("root_node",{}).setdefault(m.groupdict()['root_node'],{})
                    continue
                
                ##Path(s)     : 26.1.1.2         LDP nbr: 3.3.3.3:0         Port-channel30
                m=p1.match(line)
                if m:
                    group=m.groupdict()
                    root_dict.update(group)
                    continue
                
                ##Interface   : Port-channel30 (via unicast RT)
                m=p2.match(line)
                if m:
                    group=m.groupdict()
                    root_dict.update(group)
                    continue
                    
                ##Metric      : 4
                ##Distance    : 110
                ##FEC count   : 1
                ##Path count  : 1
                root_dict.update({res[0].strip().lower().replace(" ","_"):int(res[1].strip()) if res[1].strip().isdigit() else res[1].strip()})
               
        return ret_dict
        
class ShowMplsMldpNeighborsSchema(MetaParser):
    """Schema for:
        show mpls mldp neighbors
    """
    schema = {
        'mldp_peer': {
            Any(): {
                'uptime': str,
                'peer_state': str,
                'target_adj': str,
                'session_hndl': int,
                'upstream_count': int,
                'branch_count': int,
                'ldp_gr': {
                    'ldp_gr_state':str,
                    'reconnect_time':int,
                    Optional('reconnect_time_unit'):str,
                    'instance':int
                },
                'path_count':int,
                'path':str,
                'ldp_interface':str,
                'nhop_count':int,
                Optional('nhop_list'):str,
            },
        }
    }

class ShowMplsMldpNeighbors(ShowMplsMldpNeighborsSchema):
    """Parser for:
        show mpls mldp neighbors
    """
    cli_command = 'show mpls mldp neighbors'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        
        if not out.strip():
            return ret_dict
            
        ## MLDP peer ID    : 3.3.3.3:0, uptime 00:06:07 Up,
        p1 =re.compile(r"^MLDP peer ID\s+\:\s+(?P<mldp_peer>\S+)\,\s+uptime\s+(?P<uptime>\S+)\s+(?P<peer_state>\w+)\,$")
        
        ##LDP GR         : Enabled
        p2 = re.compile(r"^LDP GR\s+\:\s+(?P<ldp_gr_state>\S+)$")
        
        ##: Reconnect time: 120 Seconds
        ##: Instance: 2
        p3=re.compile(r"^:\s+(?P<key>[a-zA-z ]+)\:\s+(?P<value>\d+)\s*(?P<time_unit>\w+)?$")
        
        ## Path(s)        : 26.1.1.2          LDP Port-channel30
        p4=re.compile(r"^Path\(s\)\s+:\s+(?P<path>\S+)\s+LDP\s+(?P<ldp_interface>\S+)$")
        
        for line in out.splitlines():
            line=line.strip()
            
            ## MLDP peer ID    : 3.3.3.3:0, uptime 00:06:07 Up,            
            m=p1.match(line)
            if m:
                r1=m.groupdict()
                mldp_peer=ret_dict.setdefault('mldp_peer',{}).setdefault(r1['mldp_peer'],{})
                mldp_peer['uptime']=r1['uptime']
                mldp_peer['peer_state']=r1['peer_state']
                continue
            
            ##LDP GR         : Enabled
            m=p2.match(line)
            if m:
                ldp_gr_dict=mldp_peer.setdefault('ldp_gr',{})
                ldp_gr_dict.update({'ldp_gr_state':m.groups()[0]})
                continue

            ##: Reconnect time: 120 Seconds
            ##: Instance: 2            
            m=p3.match(line)
            if m:
                r3=m.groupdict()
                ldp_gr_dict.update({r3['key'].lower().replace(" ","_"):int(r3['value'])})
                if r3.get("time_unit",None):
                    ldp_gr_dict['reconnect_time_unit']=r3['time_unit'].lower()
                continue
                
            ## Path(s)        : 26.1.1.2          LDP Port-channel30
            m=p4.match(line)
            if m:
                r4=m.groupdict()
                for key,value in r4.items():
                    mldp_peer.update({key.lower():value})
                continue
            
            ##Target Adj     : No
            ##Session hndl   : 27
            ##Upstream count : 1
            ##Branch count   : 0
            ##Path count     : 1
            ##Nhop count     : 1
            ##Nhop list      : 26.1.1.2
            if line:
                res=line.split(":")
                mldp_peer.update({res[0].strip().lower().replace(" ","_"):int(res[1].strip()) if res[1].strip().isdigit() else res[1].strip()})
                continue
        return ret_dict
        
class ShowMplsMldpDatabaseSchema(MetaParser):
    """Schema for:
        show mpls mldp database
    """
    schema = {
        'lsm_id': {
            Any(): {
                'lsm_id': Any(),
                'type': str,
                'uptime': str,
                'fec_root': str,
                Optional('rnr_lsm_id'):Any(),
                'opaque_decoded': {
                    'type':str,
                    'rd':Any(),
                    'mdt_data':Any(),
                },
                'opaque_length':int,
                'opaque_length_type':str,
                'opaque_value':str,
                'upstream_client': {
                    Any():{
                        'expires':str,
                        'path_set_id':Any(),
                        Optional('state'):str,
                        Optional('uptime'):str,
                        Optional('out_label'):Any(),
                        Optional('interface'):str,
                        Optional('local_label'):Any(),
                        Optional('next_hop'):str,
                        Optional('rpf_id'):str,
                    },
                },
                'replication_client': {
                    Any():{
                        'path_set_id':Any(),
                        'uptime':str,
                        'interface':str,
                        Optional('out_label'):Any(),
                        Optional('rpf_id'):str,
                        Optional('local_label'):Any(),
                        Optional('next_hop'):str
                    },
                },
            },
        },
    }

class ShowMplsMldpDatabase(ShowMplsMldpDatabaseSchema):
    """Parser for:
        show mpls mldp database
    """
    cli_command = 'show mpls mldp database'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        
        if not out.strip():
            return ret_dict
 
        ##LSM ID : 100 (RNR LSM ID: 101)   Type: MP2MP   Uptime : 00:00:45
        p1=re.compile(r"^LSM ID : (?P<lsm_id>\S+)\s+(?:[\(A-Z: ]+\s+(?P<rnr_lsm_id>[0-9A-Z]+)\)?)*\s+Type: (?P<type>\S+)\s+Uptime : (?P<uptime>\S+)$")
       
        ##FEC Root           : 5.5.5.5     
        p2=re.compile(r"^FEC Root\s+\:\s+(?P<fec_root>[\d\.]+).*$")
        
        ##Opaque decoded     : [mdt 3001:1 0]
        p3=re.compile(r"^Opaque decoded\s+:\s+\[(?P<type>\S+)\s+(?P<rd>(\S+))\s+\(*(?P<mdt_data>[a-zA-Z0-9 ]+)\)*\]$")

        ##Opaque length      : 11 bytes       
        p4=re.compile(r"^Opaque length\s+:\s+(?P<opaque_length>\d+)\s+(?P<opaque_length_type>(\w+))$")

        ##Opaque value       : 02 000B 0030010000000100000000              
        p5=re.compile(r"Opaque value\s+:\s+([0-9A-Z ]+)$")
        
        ##Upstream client(s) :
        ##Replication client(s):
        p6=re.compile(r'^([a-zA-Z ]+)\S+\s*:$')
        
        ##2.2.2.2:0    [Active]
        ##None
        p7=re.compile(r"(?P<key>[\d+\.]+\:\d+)\s*\[*(?P<state>[a-zA-Z]+)*\]*|None")
        
        ##>MDT  (VRF vrf3001)
        p8=re.compile(r">*\s*MDT\s+\(VRF\s+(\S+)\)")

        ##Expires        : Never         Path Set ID  : 100
        ##Out Label (U)  : 26            Interface    : Port-channel20*
        ##Local Label (D): 45            Next Hop     : 104.1.1.2
        ##Uptime         : 00:00:45      Path Set ID  : 101
        ##Interface      : Lspvif9       RPF-ID       : *        
        p9=re.compile(r"([a-zA-Z\(\) ]+\s*\:\s+\S+)\s+([a-zA-Z\- ]+\:[a-zA-Z0-9\/\-\.\:\* ]+)")
        
        for line in out.splitlines():
            line=line.strip()
            
            ##LSM ID : 100 (RNR LSM ID: 101)   Type: MP2MP   Uptime : 00:00:45
            m=re.match(p1,line)
            if m:
                r1=m.groupdict()
                lsm_dict=ret_dict.setdefault('lsm_id',{}).setdefault(r1['lsm_id'],{})
                lsm_dict.update({key: int(value) if value.isdigit() else value for key,value in r1.items() if value})
                continue
                
            ##FEC Root           : 5.5.5.5 
            m=re.match(p2,line)
            if m:
                r2=m.groupdict()
                lsm_dict.update({'fec_root':r2['fec_root']})
                continue
            
            ##Opaque decoded     : [mdt 3001:1 0]
            m=re.match(p3,line)
            if m:
                r3=m.groupdict()
                opaque_dcit=lsm_dict.setdefault("opaque_decoded",{})
                opaque_dcit.update({key:int(value) if value.isdigit() else value for key,value in r3.items()})
                continue
        
            ##Opaque length      : 11 bytes 
            m=re.match(p4,line)
            if m:
                r4=m.groupdict()
                lsm_dict.update({key:int(value) if value.isdigit() else value for key,value in r4.items()})
                continue
        
            ##Opaque value       : 02 000B 0030010000000100000000 
            m=re.match(p5,line)
            if m:
                lsm_dict.update({'opaque_value':m.groups()[0]})
                continue
            
            ##Upstream client(s) :
            ##Replication client(s):
            m=re.match(p6,line)
            if m:
                client=lsm_dict.setdefault(m.groups()[0].lower().replace(" ","_"),{})
                continue
        
            ##2.2.2.2:0    [Active]
            ##None
            ##>MDT  (VRF vrf3001)
            m=re.match(p7,line) or re.match(p8,line)
            if m:
                client_info=client.setdefault(str(m.groups()[0]),{})
                if m.groupdict().get('state'):
                    client_info.update({'state':m.groupdict()['state']})
                continue
            
            ##Expires        : Never         Path Set ID  : 100
            ##Out Label (U)  : 26            Interface    : Port-channel20*
            ##Local Label (D): 45            Next Hop     : 104.1.1.2
            ##Uptime         : 00:00:45      Path Set ID  : 101
            ##Interface      : Lspvif9       RPF-ID       : *      
            m=re.match(p9,line)
            if m:
                for i in list(re.findall(p9,line)[0]):
                    res=i.split(":",1)
                    val=res[1].replace("*","") if res[0].strip()=="Interface" else res[1]
                    client_info.update({res[0].lower().strip().replace("-","_").replace(" ","_").replace("_(d)","").replace("_(u)",""):int(val) if val.strip().isdigit() else val.strip()})
                    continue
                    
        return ret_dict
