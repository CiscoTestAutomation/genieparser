"""show_cef.py

IOSXE parsers for the following show commands:

    * show cef path set id <id> detail | in Replicate oce:
    * show cef uid
    * show cef path sets summary
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

class ShowCefPathSetIdDetailReplicateOceSchema(MetaParser):
    """Schema for:
        show cef path set id <id> detail | in Replicate oce:
    """
    schema = {
        'replicate_oce': {
             Any():{
                 'uid':int
             },
         },
    }

class ShowCefPathSetIdDetailReplicateOce(ShowCefPathSetIdDetailReplicateOceSchema):
    """Parser for:
        show cef path set id <id> detail | in Replicate oce:
        """
    cli_command = 'show cef path set id {cef_id} detail | in Replicate oce:'

    def cli(self, cef_id='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(cef_id=cef_id))

        ret_dict = {}
        
        ###Replicate oce: 0x7F9E40C59340 UID:6888
        p1=re.compile(r"^Replicate\s+oce:\s+(?P<replicate_oce>\S+)\s+UID:(?P<uid>\S+)$")

        for line in output.splitlines():
            line = line.strip()
            
            ##Replicate oce: 0x7F9E40C59340 UID:6888
            m1=p1.match(line)
            if m1:
                r=m1.groupdict()
                uid_dict=ret_dict.setdefault('replicate_oce',{}).setdefault(r['replicate_oce'],{})
                uid_dict['uid']=int(r['uid'])
        return ret_dict
        
class ShowCefUidSchema(MetaParser):
    """Schema for:
        show cef uid
    """
    schema = {
        'cef_unique_ids': {
            'cef_unique_ids_stats': list,
            'ids_maximum': int,
            'ids_free': int,
            'ids_active': int,
            'ids_pending_to_re_use': int,
            'ids_total_generated': int,
            'ids_total_reserved': int,
            'ids_total_deleted': int,
            'maximum_groups': int,
            'free_groups': int,
            'active_groups': int,
            'client_key': {
                'client_key_nodes': int,
                'uid_table_entries': int,
                'uid_table_config_size': int
            },
        },
    }

class ShowCefUid(ShowCefUidSchema):
    """Parser for:
        show cef uid
        """
    cli_command = 'show cef uid'

    def cli(self,output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
                
        ###CEF Unique IDs Stats: global space
        ###CEF Unique IDs Stats: platform space
        p1=re.compile(r"^CEF\s+Unique\s+IDs\s+Stats:\s+(?P<value>[a-zA-Z ]+)$")
        
        ###CEF UID Client Key Stats
        p2=re.compile(r"CEF\s+UID\s+Client\s+Key\s+Stats")
        
        ##IDs Maximum : 16777216
        p3=re.compile(r"^IDs\s+Maximum\s+:\s+(?P<ids_maximum>\d+)$")

        ##IDs Free : 16777212 
        p4=re.compile(r"^IDs\s+Free\s+:\s+(?P<ids_free>\d+)$")

        ##IDs Active : 4
        p5=re.compile(r"^IDs\s+Active\s+:\s+(?P<ids_active>\d+)$")

        ##IDs Pending re-use TO : 0
        p6=re.compile(r"^IDs\s+Pending\s+re\-use\s+TO\s+:\s+(?P<ids_pending_to_re_use>\d+)$")

        ##IDs Total Generated : 4
        p7=re.compile(r"^IDs\s+Total\s+Generated\s+:\s+(?P<ids_total_generated>\d+)$")

        ##IDs Total Reserved : 0
        p8=re.compile(r"^IDs\s+Total\s+Reserved\s+:\s+(?P<ids_total_reserved>\d+)$")

        ##IDs Total Reserved : 0
        p9=re.compile(r"^IDs\s+Total\s+Deleted\s+:\s+(?P<ids_total_deleted>\d+)$")
        
        ##Groups Maximum : 2048
        p10=re.compile(r"^Groups\s+Maximum\s+:\s+(?P<maximum_groups>\d+)$")

        ##Groups Free : 2047
        p11=re.compile(r"^Groups\s+Free\s+:\s+(?P<free_groups>\d+)$")

        ##Groups Active : 1
        p12=re.compile(r"^Groups\s+Active\s+:\s+(?P<active_groups>\d+)$")

        ##Client Key nodes : 4
        p13=re.compile(r"^Client\s+Key\s+nodes\s+:\s+(?P<client_key_nodes>\d+)$")

        ##UID Table Entries : 4
        p14=re.compile(r"^UID\s+Table\s+Entries\s+:\s+(?P<uid_table_entries>\d+)$")

        ##UID Table config size: 16777216
        p15=re.compile(r"^UID\s+Table\s+config\s+size:\s+(?P<uid_table_config_size>\d+)$")

        for line in output.splitlines():
            line = line.strip()
            
            ##CEF Unique IDs Stats: global space
            m = p1.match(line)
            if m:
                r = m.groupdict()
                cef_ids_dict=ret_dict.setdefault('cef_unique_ids',{})
                ids_stats_list = cef_ids_dict.setdefault('cef_unique_ids_stats', [])
                ids_stats_list.append(r['value'])
                continue
                
            ##CEF UID Client Key Stats
            m = p2.match(line)
            if m:
                client_key_dict=cef_ids_dict.setdefault('client_key',{})
                continue
             
            ##IDs Maximum : 16777216             
            m = p3.match(line)
            if m: 
                cef_ids_dict.update({'ids_maximum':int(m.groupdict()['ids_maximum'])})
                continue

            ##IDs Maximum : 16777216             
            m = p4.match(line)
            if m: 
                cef_ids_dict.update({'ids_free':int(m.groupdict()['ids_free'])})
                continue
                
            ##IDs Active : 4     
            m = p5.match(line)
            if m: 
                cef_ids_dict.update({'ids_active':int(m.groupdict()['ids_active'])})      
                continue

            ##IDs Pending re-use TO : 0 
            m = p6.match(line)
            if m: 
                cef_ids_dict.update({'ids_pending_to_re_use':int(m.groupdict()['ids_pending_to_re_use'])})
                continue
                
            ##IDs Total Generated : 4
            m = p7.match(line)
            if m: 
                cef_ids_dict.update({'ids_total_generated':int(m.groupdict()['ids_total_generated'])})
                continue

            ##IDs Total Generated : 4
            m = p8.match(line)
            if m: 
                cef_ids_dict.update({'ids_total_reserved':int(m.groupdict()['ids_total_reserved'])})
                continue
                
            ##IDs Total Deleted : 0
            m = p9.match(line)
            if m: 
                cef_ids_dict.update({'ids_total_deleted':int(m.groupdict()['ids_total_deleted'])})
                continue
       
            ##Groups Maximum : 2048
            m = p10.match(line)
            if m: 
                cef_ids_dict.update({'maximum_groups':int(m.groupdict()['maximum_groups'])}) 
                continue
   
            ##Groups Maximum : 2048
            m = p11.match(line)
            if m: 
                cef_ids_dict.update({'free_groups':int(m.groupdict()['free_groups'])})
                continue   
                
            ##Groups Active : 1
            m = p12.match(line)
            if m: 
                cef_ids_dict.update({'active_groups':int(m.groupdict()['active_groups'])})
                continue  

            ##Client Key nodes : 4
            m = p13.match(line)
            if m: 
                client_key_dict.update({'client_key_nodes':int(m.groupdict()['client_key_nodes'])})
                continue  

            ##UID Table Entries : 4
            m = p14.match(line)
            if m: 
                client_key_dict.update({'uid_table_entries':int(m.groupdict()['uid_table_entries'])}) 
                continue  

            ##UID Table config size
            m = p15.match(line)
            if m: 
                client_key_dict.update({'uid_table_config_size':int(m.groupdict()['uid_table_config_size'])})
                continue  
                
        return ret_dict

class ShowCefPathSetsSummarySchema(MetaParser):
    """Schema for:
        show cef path sets summary
    """
    schema = {
        'path_set_id': {
            Any():{
                'path_num': int,
            },
        },
    }

class ShowCefPathSetsSummary(ShowCefPathSetsSummarySchema):
    """Parser for:
        show cef path sets summary
        """
    cli_command = 'show cef path sets summary'

    def cli(self,output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        ##Path Set Id 0x00000002   Num Paths 1
        p1=re.compile(r"^Path\s+Set\s+Id\s+(?P<path_set_id>\S+)\s+Num\s+Paths\s+(?P<path_num>\d+)$")
        
        for line in output.splitlines():
            line=line.strip()
            m=p1.match(line)
            if m:
                r=m.groupdict()
                path_set_dict=ret_dict.setdefault('path_set_id',{}).setdefault(r['path_set_id'],{})
                path_set_dict['path_num']=int(r['path_num'])
            continue
            
        return ret_dict