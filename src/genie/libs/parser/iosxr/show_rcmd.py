import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional


# ====================================================
#  schema for show rcmd node
# ====================================================

class ShowRcmdNodeSchema(MetaParser):
    """Schema for show rcmd node"""
    schema = {
        'rcmd_node':{
            Any(): {
                'node_id': int,
                'node_name': str,
                'node_type': str,
                'rcmd_state': str,
                'rcmd_oper_state': str,
                'node_upd_time': str,
                'node_status': str
            }
        }
    }

# ====================================================
#  parser for show rcmd node
# ====================================================

class ShowRcmdNode(ShowRcmdNodeSchema):
    """Parser for :
        show rcmd node
    """
    cli_command = 'show rcmd node'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        rcmd_dict = {}

        #1     | 0/RSP0/CPU0    | rp | Enbl/Yes| Jul 14 13:29:48.906 | No/6/0/0/1
        p0 = re.compile(r'^\s*(?P<node_id>\d+).*?\|\s*(?P<node_name>[a-zA-Z0-9/]+)\s*\|\s*(?P<node_type>\w+)\s*\|\s*(?P<rcmd_state>\w+)/(?P<rcmd_oper_state>\w+)\s*\|\s*(?P<last_upd_time>[\w\s\*:.]+)\s+\|\s*(?P<node_status>[\w/]+)')

        for line in output.splitlines():
            line = line.strip()

            #1     | 0/RSP0/CPU0    | rp | Enbl/Yes| Jul 14 13:29:48.906 | No/6/0/0/1
            m = p0.match(line)
            if m:
                group = m.groupdict()
                node_name = group ['node_name']
                node_dict = rcmd_dict.setdefault('rcmd_node', {}).setdefault(node_name, {})
                node_dict.update({
                    'node_id': int(group['node_id']),
                    'node_name': group['node_name'],
                    'node_type': group['node_type'],
                    'rcmd_state': group['rcmd_state'],
                    'rcmd_oper_state': group['rcmd_oper_state'],
                    'node_upd_time': group['last_upd_time'],
                    'node_status': group['node_status']
                })

        return rcmd_dict




# ====================================================
#  schema for show rcmd memory
# ====================================================

class ShowRcmdMemorySchema(MetaParser):
    """Schema for show rcmd memory"""
    schema = {
        'rcmd_struct':{
            Any(): {
                'curr_cnt': int,
                'alloc_fail_cnt': int,
                'alloc_cnt': int,
                'free_cnt': int,
            }
        },
        'rcmd_edm':{
            Any(): {
                'total': int,
                'success': int,
                'failure': int,
            }
        },
        'rcmd_str_len':{
            Any(): {
                'total': int,
                'success': int,
                'failure': int,
            }
        }
    }

# ====================================================
#  parser for show rcmd memory
# ====================================================

class ShowRcmdMemory(ShowRcmdMemorySchema):
    """Parser for :
        show rcmd memory
    """
    cli_command = 'show rcmd memory'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        rcmd_dict = {}

        #rcmd_server                 |          1 |          0 |          1 |          0
        p0 = re.compile(r'^\s*(?P<struct_name>\w+).*?\|\s*(?P<curr_cnt>\d+).*?\|\s*(?P<alloc_fail_cnt>\d+).*?\|\s*(?P<alloc_cnt>\d+).*?\|\s*(?P<free_cnt>\d+)')

        #RCMD EDM memory manager information
        p1 = re.compile(r'^RCMD EDM.*')
        
        #        64 |         12 |         11 |          1
        p2 = re.compile(r'^\s*(?P<size>\w+).*?\|\s*(?P<total>\d+).*?\|\s*(?P<success>\d+).*?\|\s*(?P<failure>\d+).*')

        #RCMD String memory manager information
        p3 = re.compile(r'^RCMD String.*')

        #        32 |        936 |        864 |       72
        p4 = re.compile(r'^\s*(?P<str_len>\w+).*?\|\s*(?P<total>\d+).*?\|\s*(?P<success>\d+).*?\|\s*(?P<failure>\d+).*')

        for line in output.splitlines():
            line = line.strip()

            #rcmd_server                 |          1 |          0 |          1 |          0
            m = p0.match(line)
            if m:
                inter_dict = rcmd_dict.setdefault('rcmd_struct',{})

                struct_name =  m.groupdict()['struct_name']
                result_dict = inter_dict.setdefault(struct_name,{})

                result_dict['curr_cnt'] = int(m.groupdict()['curr_cnt'])
                result_dict['alloc_fail_cnt'] = int(m.groupdict()['alloc_fail_cnt'])
                result_dict['alloc_cnt'] = int(m.groupdict()['alloc_cnt'])
                result_dict['free_cnt'] = int(m.groupdict()['free_cnt'])
                continue

            #RCMD EDM memory manager information
            m = p1.match(line)
            if m:
                inter_dict = rcmd_dict.setdefault('rcmd_edm',{})
                continue
            
            #        64 |         12 |         11 |          1
            m = p2.match(line)
            if m:
                if 'rcmd_str_len' not in rcmd_dict:
                    size_name =  m.groupdict()['size']
                    result_dict = inter_dict.setdefault(size_name,{})

                    result_dict['total'] = int(m.groupdict()['total'])
                    result_dict['success'] = int(m.groupdict()['success'])
                    result_dict['failure'] = int(m.groupdict()['failure'])
                    continue

            #RCMD String memory manager information
            m = p3.match(line)
            if m:
                inter_dict = rcmd_dict.setdefault('rcmd_str_len',{})
                continue

            #        32 |        936 |        864 |       72
            m = p4.match(line)
            if m:                
                str_len =  m.groupdict()['str_len']
                result_dict = inter_dict.setdefault(str_len,{})

                result_dict['total'] = int(m.groupdict()['total'])
                result_dict['success'] = int(m.groupdict()['success'])
                result_dict['failure'] = int(m.groupdict()['failure'])
                continue

        return rcmd_dict
