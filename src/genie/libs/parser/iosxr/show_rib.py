""" show_rib.py
    supports commands:
        * show rib tables
        * show rib tables summary
"""

# Python
import re
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common

# =============================================
# Parser for 'show rib table'
# =============================================

class ShowRibTablesSchema(MetaParser):
    schema = {'table_id':{
                    Any(): {
                        'prefix_count': int,
                        'prefix_limit': int,
                        'prefix_limit_notified': str,
                        'safi': str,
                        'table_deleted': str,
                        'table_id': str,
                        'table_name': str,
                        'table_reached_convergence': str,
                        'table_version': int,
                        'vrf_name': str,
                        'forward_referenced' : str,
                        }
                    }
                }
     

class ShowRibTables(ShowRibTablesSchema):
    """ Parser for show rib tables"""
    
    cli_command = 'show rib tables'

    def cli(self,output=None):
        """parsing mechanism: cli
        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        """
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
            
        result_dict = {}
        
        # <vrf>   / <table>    <safi>  <table_id>  <prefix_limit>  <prefix_count> <table_ver>
        # default/default        uni   0xe0000000  10000000            12              13  
        # Prefix Limit Notified Forward Referenced Table Deleted   Table Reached Convergence
        #         N                      N                N                 Y
        p1 = re.compile(r'^(?P<vrf>\S+)\/(?P<table>\w+) +(?P<safi>\w+)'
                        ' +(?P<table_id>\S+) +(?P<prfx_lmt>\d+) +(?P<prfx_cnt>\d+)'
                        ' +(?P<tbl_ver>\d+) +(?P<pfx_notif>\w) +(?P<forw_refe>\w)'
                        ' +(?P<tbl_del>\w) +(?P<tbl_conv>\w)')
        
        for line in out.splitlines():

            if line:
                line = line.strip()

            else:
                continue

            m = p1.match(line)
            
            if m:
                group = m.groupdict()
                result_dict.setdefault('table_id', {})
                table_id=group['table_id']
                result_dict['table_id'][table_id]={}
                result_dict['table_id'][table_id].update({'vrf_name': group['vrf']})
                result_dict['table_id'][table_id].update({'table_name': group['table']})
                result_dict['table_id'][table_id].update({'safi': group['safi']})
                result_dict['table_id'][table_id].update({'table_id': group['table_id']})
                result_dict['table_id'][table_id].update({'prefix_limit': int(group['prfx_lmt'])})
                result_dict['table_id'][table_id].update({'prefix_count': int(group['prfx_cnt'])})
                result_dict['table_id'][table_id].update({'table_version': int(group['tbl_ver'])})
                
                if group['pfx_notif']=='N':
                    result_dict['table_id'][table_id].update({'prefix_limit_notified': 'No'})
                elif group['pfx_notif']=='Y':
                    result_dict['table_id'][table_id].update({'prefix_limit_notified': 'Yes'})
                    
                if group['forw_refe']=='N':
                    result_dict['table_id'][table_id].update({'forward_referenced': 'No'})
                elif group['forw_refe']=='Y':
                    result_dict['table_id'][table_id].update({'forward_referenced': 'Yes'})
                    
                if group['tbl_del']=='N':
                    result_dict['table_id'][table_id].update({'table_deleted': 'No'})
                elif group['tbl_del']=='Y':
                    result_dict['table_id'][table_id].update({'table_deleted': 'Yes'})

                if group['tbl_conv']=='N':
                    result_dict['table_id'][table_id].update({'table_reached_convergence': 'No'})
                elif group['tbl_conv']=='Y':
                    result_dict['table_id'][table_id].update({'table_reached_convergence': 'Yes'})                                
        
        return result_dict


# =============================================
# Parser for 'show rib tables summary'
# =============================================

class ShowRibTablesSummarySchema(MetaParser):
    
    schema = {'rib_table':{
                       Any(): {
                            'num_unicast_tables': int,
                            'total_unicast_prefixes': int,
                            'num_multicast_tables': int,
                            'total_multicast_prefixes': int,
                        }
                    }
             }
                 



class ShowRibTablesSummary(ShowRibTablesSummarySchema):
    """ Parser for show rib tables summary"""

    cli_command = 'show rib tables summary'

    def cli(self,output=None):
        """parsing mechanism: cli
        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        """
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
            
        result_dict = {}
        
        result_dict.setdefault('rib_table', {})
        # Summary of number of tables and cumulative prefix counts in <IPv4> RIB:
        p1 = re.compile(r'^Summary\sof.+in +(?P<rib>\S+)')
        # Number of unicast tables:          <3>
        p2 = re.compile(r'^Number of unicast tables:\s+(?P<uni_tbl>\d+)')
        # Total number of unicast prefixes:         <4>
        p3 = re.compile(r'^Total number of unicast prefixes:\s+(?P<uni_pfx>\d+)')
        # Number of multicast tables:          <1>
        p4 = re.compile(r'^Number of multicast tables:\s+(?P<multi_tbl>\d+)')
        # Total number of multicast prefixes:          <0>
        p5 = re.compile(r'^Total number of multicast prefixes:\s+(?P<multi_pfx>\d+)')

        for line in out.splitlines():
    
            if line:
                line = line.strip()

            else:
                continue
                  
            m = p1.match(line)
            
            if m:
                group = m.groupdict()
                table_id=group['rib'].lower()
                result_dict['rib_table'][table_id]={}
        
            m = p2.match(line)
            
            if m:
                group = m.groupdict()
                result_dict['rib_table'][table_id].update({'num_unicast_tables': int(group['uni_tbl'])})

            m = p3.match(line)
            
            if m:
                group = m.groupdict()
                result_dict['rib_table'][table_id].update({'total_unicast_prefixes': int(group['uni_pfx'])})

            m = p4.match(line)
            
            if m:
                group = m.groupdict()
                result_dict['rib_table'][table_id].update({'num_multicast_tables': int(group['multi_tbl'])})
               
            m = p5.match(line)
            
            if m:
                group = m.groupdict()
                result_dict['rib_table'][table_id].update({'total_multicast_prefixes': int(group['multi_pfx'])})
        
        if result_dict == {'rib_table': {}}:
            result_dict = dict()
        return result_dict           