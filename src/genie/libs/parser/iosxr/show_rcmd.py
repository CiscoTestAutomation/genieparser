import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or


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


# ====================================================
#  schema for show rcmd server
# ====================================================

class ShowRcmdServerSchema(MetaParser):
    """Schema for show rcmd server"""
    schema = {
        'rcmd_server_info': {
            'host_name': str,
            'status': str,
            'max_events': int,
            'event_buffer': int,
            'monitoring_interval': int,
            'next_processing_due': int,
            'last_processing_started': str,
            'duration': int,
            'last_processing_status': str,
            'processing_cnt': int,
            'spf_processed_cnt': int,
            'rp_nodes_cnt': int,
            'lc_nodes_cnt': int,
            'diag_mode_nodes_cnt': int,
            'disabled_nodes_cnt': int,
            'inactive_nodes_cnt': int,
        },
        'archival_path_info': {
            'reports': str,
            'diagnostics': str,
            'arch_cnt': int,
            'last_arch_status': str,
            'last_arch_err': str,
            'last_arch_err_time': str,
        },
        'proto_conf': {
            Any(): {
                Any(): {
                    'threshold': int,
                    'disabled': str,
                }
            }
        }
    }


# ====================================================
#  parser for show rcmd server
# ====================================================

class ShowRcmdServer(ShowRcmdServerSchema):
    """Parser for :
        show rcmd server
    """
    cli_command = 'show rcmd server'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        rcmd_dict = {}

        # Routing Convergence Monitoring & Diagnostics (RCMD)
        p0 = re.compile(r'^.*RCMD.*')

        # HostName                 : hulk-asr9
        p1 = re.compile(r'^\s*HostName *: *(?P<host_name>\S+) *')

        # Status                   : Enable
        p2 = re.compile(r'^\s*Status *: *(?P<status>\S+) *')

        # Max Events Stored        : 500        Event Buffer Size        : 500
        p3 = re.compile(r'^\s*Max Events Stored *: *(?P<max_events>\d+) *Event Buffer Size *: *(?P<event_buffer>\d+) *')

        # Monitoring Interval(mins): 5          Next Processing due(secs): 8
        p4 = re.compile(r'^\s*Monitoring Interval.*?: *(?P<monitoring_interval>\d+) *Next Processing due.*: *(?P<next_processing_due>\d+) *')

        # Last Processing Started  : Jul 26 09:14:58.511
        p5 = re.compile(r'^\s*Last Processing Started *: *(?P<last_processing_started>[\w\s:.]+) *')

        # Duration(ms)             : 367        Last Processing Status   : Success
        p6 = re.compile(r'^\s*Duration.*?: *(?P<duration>\d+) *Last Processing Status.*: *(?P<last_processing_status>\w+) *')

        # Processing count         : 3474       SPF Processed count      : 0
        p7 = re.compile(r'^\s*Processing count.*?: *(?P<processing_cnt>\d+) *SPF Processed count.*: *(?P<spf_processed_cnt>\d+) *')

        # No. of RP Nodes          : 2          No. of LC Nodes          : 2
        p8 = re.compile(r'^\s*No. of RP Nodes.*?: *(?P<rp_nodes_cnt>\d+) *No. of LC Nodes.*: *(?P<lc_nodes_cnt>\d+) *')

        # Diag Mode Nodes          : 0          Disabled Nodes           : 0
        p9 = re.compile(r'^\s*Diag Mode Nodes.*?: *(?P<diag_mode_nodes_cnt>\d+) *Disabled Nodes.*: *(?P<disabled_nodes_cnt>\d+) *')

        # InActive Nodes           : 0
        p10 = re.compile(r'^\s*InActive Nodes.*?: *(?P<inactive_nodes_cnt>\d+) *')

        # Archival Path
        p11 = re.compile(r'^.*Archival Path.*')

        #   Reports                : Not-Configured
        p12 = re.compile(r'^\s*Reports.*?: *(?P<reports>.+) *')

        #   Diagnostics            : Not-Configured
        p13 = re.compile(r'^\s*Diagnostics.*?: *(?P<diagnostics>.+) *')

        # Archival count           : 0           Last Archival Status    : 'No error'
        p14 = re.compile(r'^\s*Archival count.*?: *(?P<arch_cnt>\d+) *Last Archival Status.*: *(?P<last_arch_status>.+) *')

        # Last Archival Error      : 'No error'
        p15 = re.compile(r'^\s*Last Archival Error\s+: *(?P<last_arch_err>.+) *')

        # Last Archival Error Time : '*'
        p16 = re.compile(r'^\s*Last Archival Error Time\s*: *(?P<last_arch_err_time>.+) *')

        # Protocol Configuration   :
        p17 = re.compile(r'^.*Protocol Configuration.*')

        #   OSPF:    Priority     Threshold    Disabled
        p18 = re.compile(r'^\s*OSPF\s*:')

        #             Critical          0        No
        p19 = re.compile(r'^\s*(?P<priority>\w+) *(?P<threshold>\d+) *(?P<disabled>\w+)')

        #   ISIS:    Priority     Threshold    Disabled
        p20 = re.compile(r'^\s*ISIS\s*:')

        for line in output.splitlines():
            line = line.strip()

            # Routing Convergence Monitoring & Diagnostics (RCMD)
            m = p0.match(line)
            if m:
                inter_dict = rcmd_dict.setdefault('rcmd_server_info', {})
                continue

            # HostName                 : hulk-asr9
            m = p1.match(line)
            if m:
                inter_dict['host_name'] = m.groupdict()['host_name']
                continue

            # Status                   : Enable
            m = p2.match(line)
            if m:
                inter_dict['status'] = m.groupdict()['status']
                continue

            # Max Events Stored        : 500        Event Buffer Size        : 500
            m = p3.match(line)
            if m:
                inter_dict['max_events'] = int(m.groupdict()['max_events'])
                inter_dict['event_buffer'] = int(m.groupdict()['event_buffer'])
                continue

            # Monitoring Interval(mins): 5          Next Processing due(secs): 8
            m = p4.match(line)
            if m:
                inter_dict['monitoring_interval'] = int(m.groupdict()['monitoring_interval'])
                inter_dict['next_processing_due'] = int(m.groupdict()['next_processing_due'])
                continue

            # Last Processing Started  : Jul 26 09:14:58.511
            m = p5.match(line)
            if m:
                inter_dict['last_processing_started'] = m.groupdict()['last_processing_started']
                continue

            # Duration(ms)             : 367        Last Processing Status   : Success
            m = p6.match(line)
            if m:
                inter_dict['duration'] = int(m.groupdict()['duration'])
                inter_dict['last_processing_status'] = m.groupdict()['last_processing_status']
                continue

            # Processing count         : 3474       SPF Processed count      : 0
            m = p7.match(line)
            if m:
                inter_dict['processing_cnt'] = int(m.groupdict()['processing_cnt'])
                inter_dict['spf_processed_cnt'] = int(m.groupdict()['spf_processed_cnt'])
                continue

            # No. of RP Nodes          : 2          No. of LC Nodes          : 2
            m = p8.match(line)
            if m:
                inter_dict['rp_nodes_cnt'] = int(m.groupdict()['rp_nodes_cnt'])
                inter_dict['lc_nodes_cnt'] = int(m.groupdict()['lc_nodes_cnt'])
                continue

            # Diag Mode Nodes          : 0          Disabled Nodes           : 0
            m = p9.match(line)
            if m:
                inter_dict['diag_mode_nodes_cnt'] = int(m.groupdict()['diag_mode_nodes_cnt'])
                inter_dict['disabled_nodes_cnt'] = int(m.groupdict()['disabled_nodes_cnt'])
                continue

            # InActive Nodes           : 0
            m = p10.match(line)
            if m:
                inter_dict['inactive_nodes_cnt'] = int(m.groupdict()['inactive_nodes_cnt'])
                continue

            # Archival Path
            m = p11.match(line)
            if m:
                inter_dict = rcmd_dict.setdefault('archival_path_info', {})
                continue

            #   Reports                : Not-Configured
            m = p12.match(line)
            if m:
                inter_dict['reports'] = m.groupdict()['reports']
                continue

            #   Diagnostics            : Not-Configured
            m = p13.match(line)
            if m:
                inter_dict['diagnostics'] = m.groupdict()['diagnostics']
                continue

            # Archival count           : 0           Last Archival Status    : 'No error'
            m = p14.match(line)
            if m:
                inter_dict['arch_cnt'] = int(m.groupdict()['arch_cnt'])
                inter_dict['last_arch_status'] = m.groupdict()['last_arch_status']
                continue

            # Last Archival Error      : 'No error'
            m = p15.match(line)
            if m:
                inter_dict['last_arch_err'] = m.groupdict()['last_arch_err']
                continue

            # Last Archival Error Time : '*'
            m = p16.match(line)
            if m:
                inter_dict['last_arch_err_time'] = m.groupdict()['last_arch_err_time']
                continue

            # Protocol Configuration   :
            m = p17.match(line)
            if m:
                inter_dict = rcmd_dict.setdefault('proto_conf', {})
                continue

            #   OSPF:    Priority     Threshold    Disabled
            m = p18.match(line)
            if m:
                result_dict = inter_dict.setdefault('ospf', {})
                continue

            #             Critical          0        No
            m = p19.match(line)
            if m:
                if 'isis' not in inter_dict:
                    priority_name =  m.groupdict()['priority']
                    result_dict2 = result_dict.setdefault(priority_name, {})

                    result_dict2['threshold'] = int(m.groupdict()['threshold'])
                    result_dict2['disabled'] = m.groupdict()['disabled']
                    continue

            #   ISIS:    Priority     Threshold    Disabled
            m = p20.match(line)
            if m:
                result_dict = inter_dict.setdefault('isis', {})
                continue

            #             Critical          0        No
            m = p19.match(line)
            if m:
                priority_name =  m.groupdict()['priority']
                result_dict2 = result_dict.setdefault(priority_name, {})

                result_dict2['threshold'] = int(m.groupdict()['threshold'])
                result_dict2['disabled'] = m.groupdict()['disabled']
                continue

        return rcmd_dict


# ========================================================
# Schema for:
#    * 'show rcmd isis {isis} event spf'
#    * 'show rcmd isis {isis} event spf {spf_run_no}'
# ========================================================

class ShowRcmdIsisEventSpfSchema(MetaParser):
    """ Schema for:
        * 'show rcmd isis {isis} event spf'
        * 'show rcmd isis {isis} event spf {spf_run_no}'
    """
    schema = {
        Any(): {
            Any(): {
                'trigger_time': str,
                'duration_time': int,
                'type': str,
                'lsp': int,
                Optional('total_prefixes_affected_critical'): int,
                Optional('time_taken_ip_critical'): int,
                Optional('time_taken_mpls_critical'): int,
                Optional('total_prefixes_affected_high'): int,
                Optional('time_taken_ip_high'): int,
                Optional('time_taken_mpls_high'): int,
                Optional('total_prefixes_affected_medium'): int,
                Optional('time_taken_ip_medium'): int,
                Optional('time_taken_mpls_medium'): int,
                Optional('total_prefixes_affected_low'): int,
                Optional('time_taken_ip_low'): int,
                Optional('time_taken_mpls_low'): int
            }
        }
    }

# ========================================================
# Parser for:
#    * 'show rcmd isis {isis} event spf'
#    * 'show rcmd isis {isis} event spf {spf_run_no}'
# ========================================================

class ShowRcmdIsisEventSpf(ShowRcmdIsisEventSpfSchema):
    """ Parser for:
        * 'show rcmd isis {isis} event spf'
        * 'show rcmd isis {isis} event spf {spf_run_no}'
    """
    cli_command = ['show rcmd isis {isis} event spf',
                   'show rcmd isis {isis} event spf {spf_run_no}']

    def cli(self, isis='', spf_run_no='', output=None):

        if output is None:
            if spf_run_no:
                output = self.device.execute(self.cli_command[1].format(isis=isis,spf_run_no=spf_run_no))
            else:
                output = self.device.execute(self.cli_command[0].format(isis=isis))

        rcmd_dict = {}

        # Reporting SPF Events for ISIS Instance : isis1
        p0 = re.compile(r'^\s*Reporting SPF Events for ISIS Instance.*: *(?P<isis_inst_id>.+) *$')

        #  2        Aug  9 05:47:43.340     0     FULL    9              5 / - / -                     0 / - / -                     0 / - / -                     0 / - / -
        p1 = re.compile(r'^\s*(?P<spf>[~*#^\s]* *\d+) *(?P<trigger_time>\w+ *\d+ *[\d:.]+) *(?P<duration_time>\d+) *(?P<type>\w+) *(?P<lsp>\d+) *(?P<total_prefixes_affected_critical>[\d-]+) */ *(?P<time_taken_ip_critical>[\d-]+) */ *(?P<time_taken_mpls_critical>[\d-]+) *(?P<total_prefixes_affected_high>[\d-]+) */ *(?P<time_taken_ip_high>[\d-]+) */ *(?P<time_taken_mpls_high>[\d-]+) *(?P<total_prefixes_affected_medium>[\d-]+) */ *(?P<time_taken_ip_medium>[\d-]+) */ *(?P<time_taken_mpls_medium>[\d-]+) *(?P<total_prefixes_affected_low>[\d-]+) */ *(?P<time_taken_ip_low>[\d-]+) */ *(?P<time_taken_mpls_low>[\d-]+) *$')

        for line in output.splitlines():
            line = line.strip()

            # Reporting SPF Events for ISIS Instance : isis1
            m = p0.match(line)
            if m:
                isis_inst_name =  m.groupdict()['isis_inst_id']
                inter_dict = rcmd_dict.setdefault(isis_inst_name, {})
                continue

            #  2        Aug  9 05:47:43.340     0     FULL    9              5 / - / -                     0 / - / -                     0 / - / -                     0 / - / -
            m = p1.match(line)
            if m:
                group = m.groupdict()
                spf_id_str =  group['spf']
                spf_id = int(spf_id_str.split()[-1])
                result_dict = inter_dict.setdefault(spf_id, {})

                temp_spf_dict = {}
                temp_spf_dict.update({
                    'trigger_time': group['trigger_time'],
                    'duration_time': int(group['duration_time']),
                    'type': group['type'],
                    'lsp': int(group['lsp']),
                    'total_prefixes_affected_critical': group['total_prefixes_affected_critical'],
                    'time_taken_ip_critical': group['time_taken_ip_critical'],
                    'time_taken_mpls_critical': group['time_taken_mpls_critical'],
                    'total_prefixes_affected_high': group['total_prefixes_affected_high'],
                    'time_taken_ip_high': group['time_taken_ip_high'],
                    'time_taken_mpls_high': group['time_taken_mpls_high'],
                    'total_prefixes_affected_medium': group['total_prefixes_affected_medium'],
                    'time_taken_ip_medium': group['time_taken_ip_medium'],
                    'time_taken_mpls_medium': group['time_taken_mpls_medium'],
                    'total_prefixes_affected_low': group['total_prefixes_affected_low'],
                    'time_taken_ip_low': group['time_taken_ip_low'],
                    'time_taken_mpls_low': group['time_taken_mpls_low']
                })

                for temp_key in temp_spf_dict:
                    if 'total_prefixes_affected_critical' in temp_key or 'time_taken_ip_critical' in temp_key or 'time_taken_mpls_critical' in temp_key or 'total_prefixes_affected_high' in temp_key or 'time_taken_ip_high' in temp_key or 'time_taken_mpls_high' in temp_key or 'total_prefixes_affected_medium' in temp_key or 'time_taken_ip_medium' in temp_key or 'time_taken_mpls_medium' in temp_key or 'total_prefixes_affected_low' in temp_key or 'time_taken_ip_low' in temp_key or 'time_taken_mpls_low' in temp_key:
                        if '-' in temp_spf_dict[temp_key]:
                            continue
                        else:
                            result_dict.update({temp_key:int(temp_spf_dict[temp_key])})
                    else:
                        result_dict.update({temp_key:temp_spf_dict[temp_key]})
                continue

        return rcmd_dict


# ========================================================
# Schema for:
#    * 'show rcmd isis {isis} event prefix'
#    * 'show rcmd isis {isis} event prefix {prefix_name}'
# ========================================================

class ShowRcmdIsisEventPrefixSchema(MetaParser):
    """ Schema for:
        * 'show rcmd isis {isis} event prefix'
        * 'show rcmd isis {isis} event prefix {prefix_name}'
    """
    schema = {
        Any(): {
            Any(): {
                'prefix': str,
                'trigger_time': str,
                'priority': str,
                'path_type': str,
                'change_type': str,
                'route': str,
                'cost': int
            }
        }
    }

# ========================================================
# Parser for:
#    * 'show rcmd isis {isis} event prefix'
#    * 'show rcmd isis {isis} event prefix {prefix_name}'
# ========================================================

class ShowRcmdIsisEventPrefix(ShowRcmdIsisEventPrefixSchema):
    """ Parser for:
        * 'show rcmd isis {isis} event prefix'
        * 'show rcmd isis {isis} event prefix {prefix_name}'
    """
    cli_command = ['show rcmd isis {isis} event prefix',
                   'show rcmd isis {isis} event prefix {prefix_name}']

    def cli(self, isis='', prefix_name='', output=None):

        if output is None:
            if prefix_name:
                output = self.device.execute(self.cli_command[1].format(isis=isis,prefix_name=prefix_name))
            else:
                output = self.device.execute(self.cli_command[0].format(isis=isis))

        rcmd_dict = {}

        # ISIS process : isis1
        p0 = re.compile(r'^\s*ISIS process.*: *(?P<isis_inst_id>.+) *')

        #        1   4.4.4.4/32           Aug 11 07:53:16.105   Medium    Primary      Add         L1          40
        p1 = re.compile(r'^\s*(?P<event_id>[~*#^\s]* *\d+) *(?P<prefix>[\d\.\/]+) *(?P<trigger_time>\w+ *\d+ *[\d:.]+) *(?P<priority>\w+) *(?P<path_type>\w+) *(?P<change_type>\w+) *(?P<route>\w+) *(?P<cost>\d+) *$')

        for line in output.splitlines():
            line = line.strip()

            # ISIS process : isis1
            m = p0.match(line)
            if m:
                isis_inst_name =  m.groupdict()['isis_inst_id']
                inter_dict = rcmd_dict.setdefault(isis_inst_name, {})
                continue

            #        1   4.4.4.4/32           Aug 11 07:53:16.105   Medium    Primary      Add         L1          40
            m = p1.match(line)
            if m:
                group = m.groupdict()
                event_id_str =  group['event_id']
                event_id = int(event_id_str.split()[-1])
                result_dict = inter_dict.setdefault(event_id, {})

                result_dict.update({
                    'prefix': group['prefix'],
                    'trigger_time': group['trigger_time'],
                    'priority': group['priority'],
                    'path_type': group['path_type'],
                    'change_type': group['change_type'],
                    'route': group['route'],
                    'cost': int(group['cost'])
                })
                continue

        return rcmd_dict



# ==========================================================
#  schema for show rcmd isis {isis} event statistics prefix
# ==========================================================

class ShowRcmdIsisEventStatisticsPrefixSchema(MetaParser):
    """Schema for show rcmd isis {isis} event statistics prefix"""
    schema = {
        Any(): {
            Any(): {
                'trigger_time': str,
                'events_added': int,
                'events_modified': int,
                'events_deleted': int,
                'events_processed_critical': int,
                'events_processed_high': int,
                'events_processed_medium': int,
                'events_processed_low': int,
                'route': str,
                'cost': int,
                'change_type': str,
                'priority': str
            }
        }
    }

# ==========================================================
#  parser for show rcmd isis {isis} event statistics prefix
# ==========================================================

class ShowRcmdIsisEventStatisticsPrefix(ShowRcmdIsisEventStatisticsPrefixSchema):
    """Parser for :
        show rcmd isis {isis} event statistics prefix
    """
    cli_command = 'show rcmd isis {isis} event statistics prefix'

    def cli(self, isis='', output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(isis=isis))

        rcmd_dict = {}

        # ISIS process : isis1
        p0 = re.compile(r'^\s*ISIS process.*: *(?P<isis_inst_id>.+) *')

        #  4.4.4.4/32          Aug 11 07:53:17.007       1/2/0          0/0/2/1          L1          30  Modify      Low
        p1 = re.compile(r'^\s*(?P<prefix>[\d\.\/]+) *(?P<trigger_time>\w+ *\d+ *[\d:.]+) *(?P<events_added>\d+)/(?P<events_modified>\d+)/(?P<events_deleted>\d+) *(?P<events_processed_critical>\d+)/(?P<events_processed_high>\d+)/(?P<events_processed_medium>\d+)/(?P<events_processed_low>\d+) *(?P<route>\S+) *(?P<cost>\d+) *(?P<change_type>\w+) *(?P<priority>\w+)')

        for line in output.splitlines():
            line = line.strip()

            # ISIS process : isis1
            m = p0.match(line)
            if m:
                isis_inst_name =  m.groupdict()['isis_inst_id']
                inter_dict = rcmd_dict.setdefault(isis_inst_name, {})
                continue

            #  4.4.4.4/32          Aug 11 07:53:17.007       1/2/0          0/0/2/1          L1          30  Modify      Low
            m = p1.match(line)
            if m:
                group = m.groupdict()
                prefix =  group['prefix']
                result_dict = inter_dict.setdefault(prefix, {})

                result_dict.update({
                    'trigger_time': group['trigger_time'],
                    'events_added': int(group['events_added']),
                    'events_modified': int(group['events_modified']),
                    'events_deleted': int(group['events_deleted']),
                    'events_processed_critical': int(group['events_processed_critical']),
                    'events_processed_high': int(group['events_processed_high']),
                    'events_processed_medium': int(group['events_processed_medium']),
                    'events_processed_low': int(group['events_processed_low']),
                    'route': group['route'],
                    'cost': int(group['cost']),
                    'change_type': group['change_type'],
                    'priority': group['priority']
                })
                continue

        return rcmd_dict



# ====================================================
#  schema for show rcmd isis {isis} event ip-frr
# ====================================================

class ShowRcmdIsisEventIpfrrSchema(MetaParser):
    """Schema for show rcmd isis {isis} event ip-frr"""
    schema = {
        Any(): {
            Any(): {
                'trigger_time': str,
                'spf': str,
                'nodes': str,
                'total': str,
                Optional('total_percent'): str,
                'critical': str,
                Optional('critical_percent'): str,
                'high': str,
                Optional('high_percent'): str,
                'medium': str,
                Optional('medium_percent'): str,
                'low': str,
                Optional('low_percent'): str
            }
        }
    }

# ====================================================
#  parser for show rcmd isis {isis} event ip-frr
# ====================================================

class ShowRcmdIsisEventIpfrr(ShowRcmdIsisEventIpfrrSchema):
    """Parser for :
        show rcmd isis {isis} event ip-frr
    """
    cli_command = 'show rcmd isis {isis} event ip-frr'

    def cli(self, isis='', output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(isis=isis))

        rcmd_dict = {}

        # Reporting IP-FRR Events for ISIS Instance: isis1
        p0 = re.compile(r'^\s*Reporting IP-FRR Events for ISIS Instance.*: *(?P<isis_inst_id>.+) *')

        #        1  Aug 11 07:52:07.820          2       0       5 ( 0%)               -               1 ( 0%)               -               4 ( 0%)
        p1 = re.compile(r'^\s*(?P<event_id>\d+) *(?P<trigger_time>\w+ *\d+ *[\d:.]+) *(?P<spf>\d+) *(?P<nodes>\d+) *(?P<total>\d+|-) *(\( *(?P<total_percent>\S+)%\))* *(?P<critical>\d+|-) *(\( *(?P<critical_percent>\S+)%\))* *(?P<high>\d+|-) *(\( *(?P<high_percent>\S+)%\))* *(?P<medium>\d+|-) *(\( *(?P<medium_percent>\S+)%\))* *(?P<low>\d+|-) *(\( *(?P<low_percent>\S+)%\))*')

        for line in output.splitlines():
            line = line.strip()

            # Reporting IP-FRR Events for ISIS Instance: isis1
            m = p0.match(line)
            if m:
                isis_inst_name =  m.groupdict()['isis_inst_id']
                inter_dict = rcmd_dict.setdefault(isis_inst_name, {})
                continue

            #        1  Aug 11 07:52:07.820          2       0       5 ( 0%)               -               1 ( 0%)               -               4 ( 0%)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                event_id =  group['event_id']
                result_dict = inter_dict.setdefault(event_id, {})

                result_dict.update({k: v for k, v in group.items() if 'event_id' not in k if v is not None})
                continue

        return rcmd_dict


# ====================================================
#  schema for show rcmd ldp event remote-lfa
# ====================================================

class ShowRcmdLdpEventRemotelfaSchema(MetaParser):
    """Schema for show rcmd ldp event remote-lfa"""
    schema = {
        Any(): {
            'snapshot_time': str,
            'total_nodes': int,
            'converged_nodes': int,
            'down_nodes': int,
            'prefixes': int,
            'paths': int,
            'labels': int,
            'coverage_percent': str
        }
    }

# ====================================================
#  parser for show rcmd ldp event remote-lfa
# ====================================================

class ShowRcmdLdpEventRemotelfa(ShowRcmdLdpEventRemotelfaSchema):
    """Parser for :
        show rcmd ldp event remote-lfa
    """
    cli_command = 'show rcmd ldp event remote-lfa'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        rcmd_dict = {}

        #        2   Aug 16 04:43:50.791        2 / 0 / 2                 3            3            0          0%
        p1 = re.compile(r'^\s*(?P<event_id>[*#\s]* *\d+) *(?P<snapshot_time>\w+ *\d+ *[\d:.]+) *(?P<total_nodes>\d+) *\/ *(?P<converged_nodes>\d+) *\/ *(?P<down_nodes>\d+) *(?P<prefixes>\d+) *(?P<paths>\d+) *(?P<labels>\d+) *(?P<coverage>\d+)%')

        for line in output.splitlines():
            line = line.strip()

            #        2   Aug 16 04:43:50.791        2 / 0 / 2                 3            3            0          0%
            m = p1.match(line)
            if m:
                group = m.groupdict()
                event_id =  group['event_id']
                result_dict = rcmd_dict.setdefault(event_id, {})

                result_dict.update({
                    'snapshot_time': group['snapshot_time'],
                    'total_nodes': int(group['total_nodes']),
                    'converged_nodes': int(group['converged_nodes']),
                    'down_nodes': int(group['down_nodes']),
                    'prefixes': int(group['prefixes']),
                    'paths': int(group['paths']),
                    'labels': int(group['labels']),
                    'coverage_percent': group['coverage']
                })
                continue

        return rcmd_dict


# ====================================================
#  schema for show rcmd ldp event session
# ====================================================

class ShowRcmdLdpEventSessionSchema(MetaParser):
    """Schema for show rcmd ldp event session"""
    schema = {
        Any(): {
            'session_time': str,
            'type': str,
            'lsr_id': str,
            'interface': str,
            'labels': str,
            'state': str
        }
    }

# ====================================================
#  parser for show rcmd ldp event session
# ====================================================

class ShowRcmdLdpEventSession(ShowRcmdLdpEventSessionSchema):
    """Parser for :
        show rcmd ldp event session
    """
    cli_command = 'show rcmd ldp event session'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        rcmd_dict = {}

        #     2      | Aug 16 04:42:32.269 |    Adjacency     |     5.5.5.5      |      HundredGigE0/0/0/1      |     10.5.1.2      |   Up
        p1 = re.compile(r'^\s*(?P<event_id>\d+) *?\| *(?P<session_time>\w+ *\d+ *[\d:.]+) *?\| *(?P<type>\S+) *?\| *(?P<lsr_id>\S+) *?\| *(?P<interface>\S+) *?\| *(?P<labels>\S+) *?\| *(?P<state>\S+)')

        for line in output.splitlines():
            line = line.strip()

            #     2      | Aug 16 04:42:32.269 |    Adjacency     |     5.5.5.5      |      HundredGigE0/0/0/1      |     10.5.1.2      |   Up
            m = p1.match(line)
            if m:
                group = m.groupdict()
                event_id =  group['event_id']
                result_dict = rcmd_dict.setdefault(event_id, {})

                result_dict.update({
                    'session_time': group['session_time'],
                    'type': group['type'],
                    'lsr_id': group['lsr_id'],
                    'interface': group['interface'],
                    'labels': group['labels'],
                    'state': group['state']
                })
                continue

        return rcmd_dict


# ==============================================================================
# Schema for:
#    * 'show rcmd isis {isis} event prefix {prefix_name} last {event_no} detail'
#    * 'show rcmd isis {isis} event prefix {prefix_name} detail'
# ==============================================================================

class ShowRcmdIsisEventPrefixLastDetailSchema(MetaParser):
    """ Schema for:
        * 'show rcmd isis {isis} event prefix {prefix_name} last {event_no} detail'
        * 'show rcmd isis {isis} event prefix {prefix_name} detail'
    """
    schema = {
        Any(): {
            Any(): {
                'prefix_name': str,
                'metric': int,
                'priority': str,
                'route_type': str,
                'path_type': str,
                'change_type': str,
                Optional('ip_frr_event_id'): int,
                Optional('spf_run_id'): int,
                Optional('paths'): {
                    Any(): {
                        Optional('ip_frr_path'): str,
                        'next_hop': str,
                        'metric': int,
                        'change_type': str,
                        Optional('remote_node'): str
                    }
                },
                'trigger_time': str,
                'summary': {
                    Optional('ip_time'): {
                        'min_time': int,
                        'min_node_id': str,
                        'max_time': int,
                        'max_node_id': str
                    },
                    Optional('mpls_time'): {
                        'min_time': int,
                        'min_node_id': str,
                        'max_time': int,
                        'max_node_id': str
                    }
                },
                'timeline': {
                    'details': {
                        Optional('isis'): int,
                        Optional('ribv4_enter'): int,
                        Optional('ribv4_exit'): int,
                        Optional('ribv4_redist'): int,
                        Optional('ldp_enter'): int,
                        Optional('ldp_exit'): int,
                        Optional('lsd_enter'): int,
                        Optional('lsd_exit'): int,
                        'lc': {
                            'ip': {
                                Optional(Any()): {
                                    Optional('path'): str,
                                    Optional('time'): int
                                }
                            },
                            'mpls': {
                                Optional(Any()): {
                                    Optional('path'): str,
                                    Optional('time'): int
                                }
                            }
                        }
                    }
                }
            }
        }
    }

# ===============================================================================
# Parser for:
#    * 'show rcmd isis {isis} event prefix {prefix_name} last {event_no} detail'
#    * 'show rcmd isis {isis} event prefix {prefix_name} detail'
# ===============================================================================

class ShowRcmdIsisEventPrefixLastDetail(ShowRcmdIsisEventPrefixLastDetailSchema):
    """ Parser for:
        * 'show rcmd isis {isis} event prefix {prefix_name} last {event_no} detail'
        * 'show rcmd isis {isis} event prefix {prefix_name} detail'
    """
    cli_command = ['show rcmd isis {isis} event prefix {prefix_name} last {event_no} detail',
                   'show rcmd isis {isis} event prefix {prefix_name} detail']

    def cli(self, isis='', prefix_name='', event_no='', output=None):

        if output is None:
            if event_no:
                output = self.device.execute(self.cli_command[0].format(isis=isis,prefix_name=prefix_name,event_no=event_no))
            else:
                output = self.device.execute(self.cli_command[1].format(isis=isis,prefix_name=prefix_name))

        rcmd_dict = {}

        #ISIS process: isis1
        p0 = re.compile(r'^ *ISIS process: *(?P<isis_id>\S+) *$')

        #Event: 6
        p1 = re.compile(r'^ *Event: *(?P<event_id>\d+) *$')

        #    Prefix: 5.5.5.5/32            Metric: 20          Priority: Low
        p2 = re.compile(r'^ *Prefix: *(?P<prefix_name>\S+) *Metric: *(?P<metric>\d+) *Priority: *(?P<priority>\w+) *$')

        #    Route Type: L1                Path-Type: Backup   Chg-Type: Modify    IP-FRR Event ID: 7
        #    Route Type: L1                Path-Type: Primary  Chg-Type: Modify    SPF Run: 8
        p3 = re.compile(r'^ *Route Type: *(?P<route_type>\S+) *Path-Type: *(?P<path_type>\w+) *Chg-Type: *(?P<change_type>\w+) *(IP-FRR Event ID: *(?P<ip_frr_event_id>\d+))*(SPF Run: *(?P<spf_run_id>\d+))* *$')

        #    Paths: HundredGigE0/0/0/1             NextHop: 10.5.1.2           Metric: 10     Chg-Type: NoChange
        p4 = re.compile(r'^ *Paths: *(?P<interface>\S+) *NextHop: *(?P<next_hop>\S+) *Metric: *(?P<metric>\d+) *Chg-Type: *(?P<change_type>\w+) *$')

        #           ^ HundredGigE0/0/0/0           NextHop: 10.1.1.2           Metric: 10     Chg-Type: Add         Remote-Node: 3.3.3.3
        #           * HundredGigE0/0/0/0           NextHop: 10.1.1.2           Metric: 10     Chg-Type: Add
        #           HundredGigE0/0/0/0             NextHop: 10.1.1.2           Metric: 10     Chg-Type: Delete
        p5 = re.compile(r'^ *((?P<ip_frr_path>[*^]))* *(?P<interface>\S+) *NextHop: *(?P<next_hop>\S+) *Metric: *(?P<metric>\d+) *Chg-Type: *(?P<change_type>\w+) *(Remote-Node: *(?P<remote_node>\S+))* *$')

        #    Trigger Time: Sep 14 09:00:36.587
        p6 = re.compile(r'^ *Trigger Time: *(?P<trigger_time>\w+ *\d+ *[\d:.]+) *$')

        #    Summary:
        p7 = re.compile(r'^ *Summary: *$')

        #        IP Route Program Time:        Min: 65(0/0/CPU0)             Max: 65(0/0/CPU0)
        p8 = re.compile(r'^ *IP Route Program Time: *Min: *(?P<min_time>\d+)\((?P<min_node_id>\S+)\) *Max: *(?P<max_time>\d+)\((?P<max_node_id>\S+)\) *$')

        #        MPLS Label Program Time:      Min: 70(0/0/CPU0)             Max: 70(0/0/CPU0)
        p9 = re.compile(r'^ *MPLS Label Program Time: *Min: *(?P<min_time>\d+)\((?P<min_node_id>\S+)\) *Max: *(?P<max_time>\d+)\((?P<max_node_id>\S+)\) *$')

        #    Timeline:
        p10 = re.compile(r'^ *Timeline: *$')

        #        Details:
        p11 = re.compile(r'^ *Details:.*$')

        #            ISIS:                0
        p12 = re.compile(r'^ *ISIS: *(?P<isis>\d+) *$')

        #            RIBv4-Enter:         2
        p13 = re.compile(r'^ *RIBv4-Enter: *(?P<ribv4_enter>\d+) *$')

        #            RIBv4-Exit:          5
        p14 = re.compile(r'^ *RIBv4-Exit: *(?P<ribv4_exit>\d+) *$')

        #            RIBv4-Redist:        5
        p15 = re.compile(r'^ *RIBv4-Redist: *(?P<ribv4_redist>\d+) *$')

        #            LDP Enter:           5
        p16 = re.compile(r'^ *LDP Enter: *(?P<ldp_enter>\d+) *$')

        #            LDP Exit:           11
        p17 = re.compile(r'^ *LDP Exit: *(?P<ldp_exit>\d+) *$')

        #            LSD Enter:          12
        p18 = re.compile(r'^ *LSD Enter: *(?P<lsd_enter>\d+) *$')

        #            LSD Exit:           14
        p19 = re.compile(r'^ *LSD Exit: *(?P<lsd_exit>\d+) *$')

        #            LC Details(IP Path):
        p20 = re.compile(r'^ *LC Details\(IP Path\):.*$')

        #              F  0/0/CPU0       65
        p21 = re.compile(r'^ *((?P<path>\w) +)?(?P<node_id>\S+) *(?P<time>\d+) *$')

        #            LC Details(MPLS Path):
        p22 = re.compile(r'^ *LC Details\(MPLS Path\):.*$')

        for line in output.splitlines():
            line = line.strip()

            #ISIS process: isis1
            m = p0.match(line)
            if m:
                isis_id = m.groupdict()['isis_id']
                isis_dict = rcmd_dict.setdefault(isis_id, {})
                continue

            #Event: 6
            m = p1.match(line)
            if m:
                event_id = int(m.groupdict()['event_id'])
                event_dict = isis_dict.setdefault(event_id, {})
                continue

            #    Prefix: 5.5.5.5/32            Metric: 20          Priority: Low
            m = p2.match(line)
            if m:
                group = m.groupdict()

                event_dict.update({
                    'prefix_name': group['prefix_name'],
                    'metric': int(group['metric']),
                    'priority': group['priority']
                })
                continue

            #    Route Type: L1                Path-Type: Backup   Chg-Type: Modify    IP-FRR Event ID: 7
            #    Route Type: L1                Path-Type: Primary  Chg-Type: Modify    SPF Run: 8
            m = p3.match(line)
            if m:
                group = m.groupdict()
                temp_route_dict = {}
                temp_route_dict.update({k: v for k, v in group.items() if v is not None})

                for temp_key in temp_route_dict:
                    if 'spf_run_id' in temp_key or 'ip_frr_event_id' in temp_key:
                        event_dict.update({temp_key:int(temp_route_dict[temp_key])})
                    else:
                        event_dict.update({temp_key:temp_route_dict[temp_key]})
                continue

            #    Paths: HundredGigE0/0/0/1             NextHop: 10.5.1.2           Metric: 10     Chg-Type: NoChange
            m = p4.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                path_dict = event_dict.setdefault('paths', {})
                interface_dict = path_dict.setdefault(interface, {})

                interface_dict.update({
                    'next_hop': group['next_hop'],
                    'metric': int(group['metric']),
                    'change_type': group['change_type']
                })
                continue

            #           ^ HundredGigE0/0/0/0           NextHop: 10.1.1.2           Metric: 10     Chg-Type: Add         Remote-Node: 3.3.3.3
            #           * HundredGigE0/0/0/0           NextHop: 10.1.1.2           Metric: 10     Chg-Type: Add
            #           HundredGigE0/0/0/0             NextHop: 10.1.1.2           Metric: 10     Chg-Type: Delete
            m = p5.match(line)
            if m:
                group = m.groupdict()
                interface2 = group['interface']
                interface2_dict = path_dict.setdefault(interface2, {})
                temp_interface_dict = {}
                temp_interface_dict.update({k: v for k, v in group.items() if 'interface' not in k if v is not None})

                for temp_key in temp_interface_dict:
                    if 'metric' in temp_key:
                        interface2_dict.update({temp_key:int(temp_interface_dict[temp_key])})
                    else:
                        interface2_dict.update({temp_key:temp_interface_dict[temp_key]})
                continue

            #    Trigger Time: Sep 14 09:00:36.587
            m = p6.match(line)
            if m:
                event_dict['trigger_time'] = m.groupdict()['trigger_time']
                continue

            #    Summary:
            m = p7.match(line)
            if m:
                summary_dict = event_dict.setdefault('summary', {})
                continue

            #        IP Route Program Time:        Min: 65(0/0/CPU0)             Max: 65(0/0/CPU0)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ip_dict = summary_dict.setdefault('ip_time', {})

                ip_dict.update({
                    'min_time': int(group['min_time']),
                    'min_node_id': group['min_node_id'],
                    'max_time': int(group['max_time']),
                    'max_node_id': group['max_node_id']
                })
                continue

            #        MPLS Label Program Time:      Min: 70(0/0/CPU0)             Max: 70(0/0/CPU0)
            m = p9.match(line)
            if m:
                group = m.groupdict()
                mpls_dict = summary_dict.setdefault('mpls_time', {})

                mpls_dict.update({
                    'min_time': int(group['min_time']),
                    'min_node_id': group['min_node_id'],
                    'max_time': int(group['max_time']),
                    'max_node_id': group['max_node_id']
                })
                continue

            #    Timeline:
            m = p10.match(line)
            if m:
                timeline_dict = event_dict.setdefault('timeline', {})
                continue

            #        Details:
            m = p11.match(line)
            if m:
                details_dict = timeline_dict.setdefault('details', {})
                continue

            #            ISIS:                0
            m = p12.match(line)
            if m:
                details_dict['isis'] = int(m.groupdict()['isis'])
                continue

            #            RIBv4-Enter:         2
            m = p13.match(line)
            if m:
                details_dict['ribv4_enter'] = int(m.groupdict()['ribv4_enter'])
                continue

            #            RIBv4-Exit:          5
            m = p14.match(line)
            if m:
                details_dict['ribv4_exit'] = int(m.groupdict()['ribv4_exit'])
                continue

            #            RIBv4-Redist:        5
            m = p15.match(line)
            if m:
                details_dict['ribv4_redist'] = int(m.groupdict()['ribv4_redist'])
                continue

            #            LDP Enter:           5
            m = p16.match(line)
            if m:
                details_dict['ldp_enter'] = int(m.groupdict()['ldp_enter'])
                continue

            #            LDP Exit:           11
            m = p17.match(line)
            if m:
                details_dict['ldp_exit'] = int(m.groupdict()['ldp_exit'])
                continue

            #            LSD Enter:          12
            m = p18.match(line)
            if m:
                details_dict['lsd_enter'] = int(m.groupdict()['lsd_enter'])
                continue

            #            LSD Exit:           14
            m = p19.match(line)
            if m:
                details_dict['lsd_exit'] = int(m.groupdict()['lsd_exit'])
                continue

            #            LC Details(IP Path):
            m = p20.match(line)
            if m:
                lc_dict = details_dict.setdefault('lc', {})
                ip_dict = lc_dict.setdefault('ip', {})
                continue

            #              F  0/0/CPU0       65
            m = p21.match(line)
            if m:
                if 'mpls' not in lc_dict:
                    group = m.groupdict()
                    node_name = group['node_id']
                    ip_node_dict = ip_dict.setdefault(node_name, {})
                    temp_lc_ip_dict = {}
                    temp_lc_ip_dict.update({k: v for k, v in group.items() if 'node_id' not in k if v is not None})

                    for temp_key in temp_lc_ip_dict:
                        if 'time' in temp_key:
                            ip_node_dict.update({temp_key:int(temp_lc_ip_dict[temp_key])})
                        else:
                            ip_node_dict.update({temp_key:temp_lc_ip_dict[temp_key]})
                    continue

            #            LC Details(MPLS Path):
            m = p22.match(line)
            if m:
                mpls_dict = lc_dict.setdefault('mpls', {})
                continue

            #              F  0/0/CPU0       65
            m = p21.match(line)
            if m:
                group = m.groupdict()
                node_name = group['node_id']
                mpls_node_dict = mpls_dict.setdefault(node_name, {})
                temp_lc_mpls_dict = {}
                temp_lc_mpls_dict.update({k: v for k, v in group.items() if 'node_id' not in k if v is not None})

                for temp_key in temp_lc_mpls_dict:
                    if 'time' in temp_key:
                        mpls_node_dict.update({temp_key:int(temp_lc_mpls_dict[temp_key])})
                    else:
                        mpls_node_dict.update({temp_key:temp_lc_mpls_dict[temp_key]})

        return rcmd_dict




# ==============================================================================
# Schema for:
#    * 'show rcmd isis {isis} event spf last {event_no} detail'
#    * 'show rcmd isis {isis} event spf {spf_run_no} detail'
# ==============================================================================

class ShowRcmdIsisEventSpfLastDetailSchema(MetaParser):
    """ Schema for:
        * 'show rcmd isis {isis} event spf last {event_no} detail'
        * 'show rcmd isis {isis} event spf {spf_run_no} detail'
    """
    schema = {
        Any(): {
            'spf_info': {
                Any(): {
                    Optional('run_event_status'): str,
                    'topology': int,
                    'level': str,
                    'type': str,
                    'trigger_time': str,
                    'trigger_values': str,
                    'wait': int,
                    'start': int,
                    'duration': int,
                    'trigger_lsp': str,
                    'seq': str,
                    'change_type': str,
                    'trigger_lsp_time': str,
                    'node_stats': {
                        'added': int,
                        'deleted': int,
                        'modified': int,
                        'reachable': int,
                        'unreachable': int,
                        'touched': int
                    },
                    'summary': {
                        Optional(Any()): {
                            'route_cnt': {
                                'added': int,
                                'deleted': int,
                                'modified': int
                            },
                            Optional('frr_coverage'): {
                                'total': int,
                                'full': int,
                                'partial': int,
                                'total_percent': str
                            },
                            Optional('ip_time'): {
                                'min_time': int,
                                'min_node_id': str,
                                'max_time': int,
                                'max_node_id': str
                            },
                            Optional('mpls_time'): {
                                'min_time': int,
                                'min_node_id': str,
                                'max_time': int,
                                'max_node_id': str
                            }
                        }
                    },
                    Optional(Any()): {
                       'route_cnt': {
                           'added': int,
                           'deleted': int,
                           'modified': int
                       },
                       Optional('ip_time'): {
                           'min_time': int,
                           'min_node_id': str,
                           'max_time': int,
                           'max_node_id': str
                       },
                       Optional('mpls_time'): {
                           'min_time': int,
                           'min_node_id': str,
                           'max_time': int,
                           'max_node_id': str
                       },
                       'details': {
                           Optional(Any()): {
                               'start': int,
                               'end': int,
                               'duration': int
                           },
                           'lc': {
                               'ip': {
                                   Optional(Any()): {
                                       Optional('path'): str,
                                       Optional('start'): int,
                                       Optional('end'): int,
                                       Optional('duration'): int
                                   }
                               },
                               Optional('mpls'): {
                                   Optional(Any()): {
                                       Optional('path'): str,
                                       Optional('start'): int,
                                       Optional('end'): int,
                                       Optional('duration'): int
                                   }
                               }
                           }
                       },
                       'leaf_nws_added': {
                           Optional('interface_ip'): str,
                           Optional('router_id'): str,
                        },
                       'leaf_nws_deleted': {
                           Optional('interface_ip'): str,
                           Optional('router_id'): str,
                        }
                    },
                    'lsp_processed': {
                        Optional(Any()): {
                            'seq': str,
                            'change_type': str,
                            'recv_time': str
                        }
                    },
                    'lsp_regenerated': {
                        Optional(Any()): {
                            'seq': str,
                            'change_type': str,
                            'recv_time': str
                        }
                    }
                }
            }
        }
    }

# ==============================================================================
# Parser for:
#    * 'show rcmd isis {isis} event spf last {event_no} detail'
#    * 'show rcmd isis {isis} event spf {spf_run_no} detail'
# ==============================================================================

class ShowRcmdIsisEventSpfLastDetail(ShowRcmdIsisEventSpfLastDetailSchema):
    """ Parser for:
        * 'show rcmd isis {isis} event spf last {event_no} detail'
        * 'show rcmd isis {isis} event spf {spf_run_no} detail'
    """
    cli_command = ['show rcmd isis {isis} event spf last {event_no} detail',
                   'show rcmd isis {isis} event spf {spf_run_no} detail']

    def cli(self, isis='', event_no='', spf_run_no='', output=None):

        if output is None:
            if spf_run_no:
                output = self.device.execute(self.cli_command[1].format(isis=isis,spf_run_no=spf_run_no))
            else:
                output = self.device.execute(self.cli_command[0].format(isis=isis,event_no=event_no))

        rcmd_dict = {}

        #ISIS process: isis1
        p0 = re.compile(r'^ *ISIS process: *(?P<isis_id>\S+) *$')

        #SPF Info:
        p1 = re.compile(r'^ *SPF Info: *$')

        #   Run: 459       Topology: 0              Level: L1                Type: Full
        #   ^Run: 459       Topology: 0              Level: L1                Type: Full
        p2 = re.compile(r'^ *((?P<run_event_status>[#^~*]))* *Run: *(?P<run_event_id>\d+) *Topology: *(?P<topology>\d+) *Level: *(?P<level>\S+) *Type: *(?P<type>\S+) *$')

        #    Trigger: Sep 19 18:11:17.193            Trigger:  lt lo lp
        p3 = re.compile(r'^ *Trigger: *(?P<trigger_time>\w+ *\d+ *[\d:.]+) *Trigger: *(?P<trigger_values>[\w ]*) *$')

        #                   Wait: 3981               Start: 3982              Duration: 0
        p4 = re.compile(r'^ *Wait: *(?P<wait>\d+) *Start: *(?P<start>\d+) *Duration: *(?P<duration>\d+) *$')

        #    Trigger LSP:   2037.0685.b002.00-00  Seq: b  Change-type: Modify  Time: Sep 19 18:11:17.193
        p5 = re.compile(r'^ *Trigger LSP: *(?P<trigger_lsp>\S+) *Seq: *(?P<seq>\w+) *Change-type: *(?P<change_type>\S+) *Time: *(?P<trigger_lsp_time>\w+ *\d+ *[\d:.]+) *$')

        #    Node Stats:    Added: 0                 Deleted: 0               Modified: 0
        p6 = re.compile(r'^ *Node Stats: *Added: *(?P<added>\d+) *Deleted: *(?P<deleted>\d+) *Modified: *(?P<modified>\d+) *$')

        #                   Reachable: 2             Unreachable: 0           Touched: 2
        p7 = re.compile(r'^ *Reachable: *(?P<reachable>\d+) *Unreachable: *(?P<unreachable>\d+) *Touched: *(?P<touched>\d+) *$')

        #    Summary:
        p8 = re.compile(r'^ *Summary: *$')

        #        Priority: Critical
        p9 = re.compile(r'.*Priority: *Critical *$')

        #            Route Count:                  Added: 0            Deleted: 0          Modified: 1
        p10 = re.compile(r'^ *Route Count: *Added: *(?P<added>\d+) *Deleted: *(?P<deleted>\d+) *Modified: *(?P<modified>\d+) *$')

        #            FRR Coverage:                 Total: 2            Full: 0             Partial: 0          Total:  0%
        p11 = re.compile(r'^ *FRR Coverage: *Total: *(?P<total>\d+) *Full: *(?P<full>\d+) *Partial: *(?P<partial>\d+) *Total: *(?P<total_percent>[\d.]*)% *$')

        #            IP Route Program Time:        Min: 3987(0/0/CPU0)           Max: 3987(0/0/CPU0)
        p12 = re.compile(r'^ *IP Route Program Time: *Min: *(?P<min_time>\d+)\((?P<min_node_id>\S+)\) *Max: *(?P<max_time>\d+)\((?P<max_node_id>\S+)\) *$')

        #            MPLS Label Program Time:      Min: 403(0/0/CPU0)            Max: 403(0/0/CPU0)
        p13 = re.compile(r'^ *MPLS Label Program Time: *Min: *(?P<min_time>\d+)\((?P<min_node_id>\S+)\) *Max: *(?P<max_time>\d+)\((?P<max_node_id>\S+)\) *$')

        #        Priority: High
        p14 = re.compile(r'.*Priority: *High *$')

        #        Priority: Medium
        p15 = re.compile(r'.*Priority: *Medium *$')

        #        Priority: Low
        p16 = re.compile(r'.*Priority: *Low *$')

        #        Details:                     Start               End          Duration
        p17 = re.compile(r'^ *Details: *Start *End *Duration *$')

        #              ISIS:                   3982              3982                 0
        p18 = re.compile(r'^ *ISIS: *(?P<start>\d+) *(?P<end>\d+) *(?P<duration>\d+) *$')

        #              RIBv4-Enter             3982              3982                 0
        p19 = re.compile(r'^ *RIBv4-Enter *(?P<start>\d+) *(?P<end>\d+) *(?P<duration>\d+) *$')

        #              RIBv4-Exit              3986              3986                 0
        p20 = re.compile(r'^ *RIBv4-Exit *(?P<start>\d+) *(?P<end>\d+) *(?P<duration>\d+) *$')

        #              RIBv4-Redist              3986              3986                 0
        p21 = re.compile(r'^ *RIBv4-Redist *(?P<start>\d+) *(?P<end>\d+) *(?P<duration>\d+) *$')

        #              LDP Enter              3986              3986                 0
        p22 = re.compile(r'^ *LDP Enter *(?P<start>\d+) *(?P<end>\d+) *(?P<duration>\d+) *$')

        #              LDP Exit              3986              3986                 0
        p23 = re.compile(r'^ *LDP Exit *(?P<start>\d+) *(?P<end>\d+) *(?P<duration>\d+) *$')

        #              LSD Enter              3986              3986                 0
        p24 = re.compile(r'^ *LSD Enter *(?P<start>\d+) *(?P<end>\d+) *(?P<duration>\d+) *$')

        #              LSD Exit              3986              3986                 0
        p25 = re.compile(r'^ *LSD Exit *(?P<start>\d+) *(?P<end>\d+) *(?P<duration>\d+) *$')

        #            LC Details(IP Path):
        p26 = re.compile(r'^ *LC Details\(IP Path\):.*$')

        #                F 0/0/CPU0            3987              3987                 0
        p27 = re.compile(r'^ *((?P<path>\w) +)?(?P<node_id>\S+) *(?P<start>\d+) *(?P<end>\d+) *(?P<duration>\d+) *$')

        #            LC Details(MPLS Path):
        p28 = re.compile(r'^ *LC Details\(MPLS Path\):.*$')

        #        Leaf Networks Added:
        p29 = re.compile(r'^ *Leaf Networks Added: *$')

        #            3.3.3.3/32                  10.3.1.0/24
        #            4.4.4.4/32
        p30 = re.compile(r'^ *(?P<interface_ip>[\d./]+) *((?P<router_id>\S+))* *$')

        #        Leaf Networks Deleted:
        p31 = re.compile(r'^ *Leaf Networks Deleted: *$')

        #    LSP Processed:
        p32 = re.compile(r'^ *LSP Processed: *$')

        #        Id: 2037.0685.b002.00-00  Seq: b  Change-type: Modify  Recv-Time: Sep 19 18:11:17.193
        p33 = re.compile(r'^ *Id: *(?P<id>\S+) *Seq: *(?P<seq>\w+) *Change-type: *(?P<change_type>\S+) *Recv-Time: *(?P<recv_time>\w+ *\d+ *[\d:.]+) *$')

        #    LSP Regenerated:
        p34 = re.compile(r'^ *LSP Regenerated: *$')

        for line in output.splitlines():
            line = line.strip()

            #ISIS process: isis1
            m = p0.match(line)
            if m:
                isis_id = m.groupdict()['isis_id']
                isis_id_dict = rcmd_dict.setdefault(isis_id, {})
                continue

            #SPF Info:
            m = p1.match(line)
            if m:
                spf_dict = isis_id_dict.setdefault('spf_info', {})
                continue

            #   Run: 459       Topology: 0              Level: L1                Type: Full
            #   ^Run: 459       Topology: 0              Level: L1                Type: Full
            m = p2.match(line)
            if m:
                group = m.groupdict()
                run_event_id = int(group['run_event_id'])
                run_event_dict = spf_dict.setdefault(run_event_id, {})
                temp_run_dict = {}
                temp_run_dict.update({k: v for k, v in group.items() if 'run_event_id' not in k if v is not None})

                for temp_key in temp_run_dict:
                    if 'topology' in temp_key:
                        run_event_dict.update({temp_key:int(temp_run_dict[temp_key])})
                    else:
                        run_event_dict.update({temp_key:temp_run_dict[temp_key]})
                continue

            #    Trigger: Sep 19 18:11:17.193            Trigger:  lt lo lp
            m = p3.match(line)
            if m:
                group = m.groupdict()

                run_event_dict.update({
                    'trigger_time': group['trigger_time'],
                    'trigger_values': group['trigger_values']
                })
                continue

            #                   Wait: 3981               Start: 3982              Duration: 0
            m = p4.match(line)
            if m:
                group = m.groupdict()

                run_event_dict.update({
                    'wait': int(group['wait']),
                    'start': int(group['start']),
                    'duration': int(group['duration'])
                })
                continue

            #    Trigger LSP:   2037.0685.b002.00-00  Seq: b  Change-type: Modify  Time: Sep 19 18:11:17.193
            m = p5.match(line)
            if m:
                group = m.groupdict()

                run_event_dict.update({
                    'trigger_lsp': group['trigger_lsp'],
                    'seq': group['seq'],
                    'change_type': group['change_type'],
                    'trigger_lsp_time': group['trigger_lsp_time']
                })
                continue

            #    Node Stats:    Added: 0                 Deleted: 0               Modified: 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                node_stats_dict = run_event_dict.setdefault('node_stats', {})

                node_stats_dict.update({
                    'added': int(group['added']),
                    'deleted': int(group['deleted']),
                    'modified': int(group['modified'])
                })
                continue

            #                   Reachable: 2             Unreachable: 0           Touched: 2
            m = p7.match(line)
            if m:
                group = m.groupdict()

                node_stats_dict.update({
                    'reachable': int(group['reachable']),
                    'unreachable': int(group['unreachable']),
                    'touched': int(group['touched'])
                })
                continue

            #    Summary:
            m = p8.match(line)
            if m:
                summary_dict = run_event_dict.setdefault('summary', {})
                continue

            #        Priority: Critical
            m = p9.match(line)
            if m:
                if 'critical' not in summary_dict:
                    critical_dict = summary_dict.setdefault('critical', {})
                    continue

            #            Route Count:                  Added: 0            Deleted: 0          Modified: 1
            m = p10.match(line)
            if m:
                if 'high' not in summary_dict and 'medium' not in summary_dict and 'low' not in summary_dict and 'critical' in summary_dict:
                    group = m.groupdict()
                    route_cnt_dict = critical_dict.setdefault('route_cnt', {})

                    route_cnt_dict.update({
                        'added': int(group['added']),
                        'deleted': int(group['deleted']),
                        'modified': int(group['modified'])
                    })
                    continue

            #            FRR Coverage:                 Total: 2            Full: 0             Partial: 0          Total:  0%
            m = p11.match(line)
            if m:
                if 'high' not in summary_dict and 'medium' not in summary_dict and 'low' not in summary_dict and 'critical' in summary_dict:
                    group = m.groupdict()
                    frr_coverage_dict = critical_dict.setdefault('frr_coverage', {})

                    frr_coverage_dict.update({
                        'total': int(group['total']),
                        'full': int(group['full']),
                        'partial': int(group['partial']),
                        'total_percent': group['total_percent']
                    })
                    continue

            #            IP Route Program Time:        Min: 3987(0/0/CPU0)           Max: 3987(0/0/CPU0)
            m = p12.match(line)
            if m:
                if 'high' not in summary_dict and 'medium' not in summary_dict and 'low' not in summary_dict and 'critical' in summary_dict:
                    group = m.groupdict()
                    ip_dict = critical_dict.setdefault('ip_time', {})

                    ip_dict.update({
                        'min_time': int(group['min_time']),
                        'min_node_id': group['min_node_id'],
                        'max_time': int(group['max_time']),
                        'max_node_id': group['max_node_id']
                    })
                    continue

            #            MPLS Label Program Time:      Min: 403(0/0/CPU0)            Max: 403(0/0/CPU0)
            m = p13.match(line)
            if m:
                if 'high' not in summary_dict and 'medium' not in summary_dict and 'low' not in summary_dict and 'critical' in summary_dict:
                    group = m.groupdict()
                    mpls_dict = critical_dict.setdefault('mpls_time', {})

                    mpls_dict.update({
                        'min_time': int(group['min_time']),
                        'min_node_id': group['min_node_id'],
                        'max_time': int(group['max_time']),
                        'max_node_id': group['max_node_id']
                    })
                    continue

            #        Priority: High
            m = p14.match(line)
            if m:
                if 'high' not in summary_dict:
                    high_dict = summary_dict.setdefault('high', {})
                    continue

            #            Route Count:                  Added: 0            Deleted: 0          Modified: 1
            m = p10.match(line)
            if m:
                if 'medium' not in summary_dict and 'low' not in summary_dict and 'high' in summary_dict:
                    group = m.groupdict()
                    route_cnt_dict = high_dict.setdefault('route_cnt', {})

                    route_cnt_dict.update({
                        'added': int(group['added']),
                        'deleted': int(group['deleted']),
                        'modified': int(group['modified'])
                    })
                    continue

            #            FRR Coverage:                 Total: 2            Full: 0             Partial: 0          Total:  0%
            m = p11.match(line)
            if m:
                if 'medium' not in summary_dict and 'low' not in summary_dict and 'high' in summary_dict:
                    group = m.groupdict()
                    frr_coverage_dict = high_dict.setdefault('frr_coverage', {})

                    frr_coverage_dict.update({
                        'total': int(group['total']),
                        'full': int(group['full']),
                        'partial': int(group['partial']),
                        'total_percent': group['total_percent']
                    })
                    continue

            #            IP Route Program Time:        Min: 3987(0/0/CPU0)           Max: 3987(0/0/CPU0)
            m = p12.match(line)
            if m:
                if 'medium' not in summary_dict and 'low' not in summary_dict and 'high' in summary_dict:
                    group = m.groupdict()
                    ip_dict = high_dict.setdefault('ip_time', {})

                    ip_dict.update({
                        'min_time': int(group['min_time']),
                        'min_node_id': group['min_node_id'],
                        'max_time': int(group['max_time']),
                        'max_node_id': group['max_node_id']
                    })
                    continue

            #            MPLS Label Program Time:      Min: 403(0/0/CPU0)            Max: 403(0/0/CPU0)
            m = p13.match(line)
            if m:
                if 'medium' not in summary_dict and 'low' not in summary_dict and 'high' in summary_dict:
                    group = m.groupdict()
                    mpls_dict = high_dict.setdefault('mpls_time', {})

                    mpls_dict.update({
                        'min_time': int(group['min_time']),
                        'min_node_id': group['min_node_id'],
                        'max_time': int(group['max_time']),
                        'max_node_id': group['max_node_id']
                    })
                    continue

            #        Priority: Medium
            m = p15.match(line)
            if m:
                if 'medium' not in summary_dict:
                    medium_dict = summary_dict.setdefault('medium', {})
                    continue

            #            Route Count:                  Added: 0            Deleted: 0          Modified: 1
            m = p10.match(line)
            if m:
                if 'low' not in summary_dict and 'medium' in summary_dict:
                    group = m.groupdict()
                    route_cnt_dict = medium_dict.setdefault('route_cnt', {})

                    route_cnt_dict.update({
                        'added': int(group['added']),
                        'deleted': int(group['deleted']),
                        'modified': int(group['modified'])
                    })
                    continue

            #            FRR Coverage:                 Total: 2            Full: 0             Partial: 0          Total:  0%
            m = p11.match(line)
            if m:
                if 'low' not in summary_dict and 'medium' in summary_dict:
                    group = m.groupdict()
                    frr_coverage_dict = medium_dict.setdefault('frr_coverage', {})

                    frr_coverage_dict.update({
                        'total': int(group['total']),
                        'full': int(group['full']),
                        'partial': int(group['partial']),
                        'total_percent': group['total_percent']
                    })
                    continue

            #            IP Route Program Time:        Min: 3987(0/0/CPU0)           Max: 3987(0/0/CPU0)
            m = p12.match(line)
            if m:
                if 'low' not in summary_dict and 'medium' in summary_dict:
                    group = m.groupdict()
                    ip_dict = medium_dict.setdefault('ip_time', {})

                    ip_dict.update({
                        'min_time': int(group['min_time']),
                        'min_node_id': group['min_node_id'],
                        'max_time': int(group['max_time']),
                        'max_node_id': group['max_node_id']
                    })
                    continue

            #            MPLS Label Program Time:      Min: 403(0/0/CPU0)            Max: 403(0/0/CPU0)
            m = p13.match(line)
            if m:
                if 'low' not in summary_dict and 'medium' in summary_dict:
                    group = m.groupdict()
                    mpls_dict = medium_dict.setdefault('mpls_time', {})

                    mpls_dict.update({
                        'min_time': int(group['min_time']),
                        'min_node_id': group['min_node_id'],
                        'max_time': int(group['max_time']),
                        'max_node_id': group['max_node_id']
                    })
                    continue

            #        Priority: Low
            m = p16.match(line)
            if m:
                if 'low' not in summary_dict:
                    low_dict = summary_dict.setdefault('low', {})
                    continue

            #            Route Count:                  Added: 0            Deleted: 0          Modified: 1
            m = p10.match(line)
            if m:
                if 'route_cnt' not in low_dict and 'low' in summary_dict:
                    group = m.groupdict()
                    route_cnt_dict = low_dict.setdefault('route_cnt', {})

                    route_cnt_dict.update({
                        'added': int(group['added']),
                        'deleted': int(group['deleted']),
                        'modified': int(group['modified'])
                    })
                    continue

            #            FRR Coverage:                 Total: 2            Full: 0             Partial: 0          Total:  0%
            m = p11.match(line)
            if m:
                if 'frr_coverage' not in low_dict and 'low' in summary_dict:
                    group = m.groupdict()
                    frr_coverage_dict = low_dict.setdefault('frr_coverage', {})

                    frr_coverage_dict.update({
                        'total': int(group['total']),
                        'full': int(group['full']),
                        'partial': int(group['partial']),
                        'total_percent': group['total_percent']
                    })
                    continue

            #            IP Route Program Time:        Min: 3987(0/0/CPU0)           Max: 3987(0/0/CPU0)
            m = p12.match(line)
            if m:
                if 'ip_time' not in low_dict and 'low' in summary_dict:
                    group = m.groupdict()
                    ip_dict = low_dict.setdefault('ip_time', {})

                    ip_dict.update({
                        'min_time': int(group['min_time']),
                        'min_node_id': group['min_node_id'],
                        'max_time': int(group['max_time']),
                        'max_node_id': group['max_node_id']
                    })
                    continue

            #            MPLS Label Program Time:      Min: 403(0/0/CPU0)            Max: 403(0/0/CPU0)
            m = p13.match(line)
            if m:
                if 'mpls_time' not in low_dict and 'low' in summary_dict:
                    group = m.groupdict()
                    mpls_dict = low_dict.setdefault('mpls_time', {})

                    mpls_dict.update({
                        'min_time': int(group['min_time']),
                        'min_node_id': group['min_node_id'],
                        'max_time': int(group['max_time']),
                        'max_node_id': group['max_node_id']
                    })
                    continue

            #        Priority: Critical
            m = p9.match(line)
            if m:
                run_event_critical_dict = run_event_dict.setdefault('critical', {})
                continue

            #            Route Count:                  Added: 0            Deleted: 0          Modified: 1
            m = p10.match(line)
            if m:
                if 'high' not in run_event_dict and 'medium' not in run_event_dict and 'low' not in run_event_dict and 'critical' in run_event_dict:
                    group = m.groupdict()
                    route_cnt_dict = run_event_critical_dict.setdefault('route_cnt', {})

                    route_cnt_dict.update({
                        'added': int(group['added']),
                        'deleted': int(group['deleted']),
                        'modified': int(group['modified'])
                    })
                    continue

            #            IP Route Program Time:        Min: 3987(0/0/CPU0)           Max: 3987(0/0/CPU0)
            m = p12.match(line)
            if m:
                if 'high' not in run_event_dict and 'medium' not in run_event_dict and 'low' not in run_event_dict and 'critical' in run_event_dict:
                    group = m.groupdict()
                    ip_dict = run_event_critical_dict.setdefault('ip_time', {})

                    ip_dict.update({
                        'min_time': int(group['min_time']),
                        'min_node_id': group['min_node_id'],
                        'max_time': int(group['max_time']),
                        'max_node_id': group['max_node_id']
                    })
                    continue

            #            MPLS Label Program Time:      Min: 403(0/0/CPU0)            Max: 403(0/0/CPU0)
            m = p13.match(line)
            if m:
                if 'high' not in run_event_dict and 'medium' not in run_event_dict and 'low' not in run_event_dict and 'critical' in run_event_dict:
                    group = m.groupdict()
                    mpls_dict = run_event_critical_dict.setdefault('mpls_time', {})

                    mpls_dict.update({
                        'min_time': int(group['min_time']),
                        'min_node_id': group['min_node_id'],
                        'max_time': int(group['max_time']),
                        'max_node_id': group['max_node_id']
                    })
                    continue

            #        Details:                     Start               End          Duration
            m = p17.match(line)
            if m:
                if 'high' not in run_event_dict and 'medium' not in run_event_dict and 'low' not in run_event_dict and 'critical' in run_event_dict:
                    run_event_critical_details_dict = run_event_critical_dict.setdefault('details', {})
                    continue

            #              ISIS:                   3982              3982                 0
            m = p18.match(line)
            if m:
                if 'high' not in run_event_dict and 'medium' not in run_event_dict and 'low' not in run_event_dict and 'critical' in run_event_dict:
                    group = m.groupdict()
                    isis_dict = run_event_critical_details_dict.setdefault('isis', {})

                    isis_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #              RIBv4-Enter             3982              3982                 0
            m = p19.match(line)
            if m:
                if 'high' not in run_event_dict and 'medium' not in run_event_dict and 'low' not in run_event_dict and 'critical' in run_event_dict:
                    group = m.groupdict()
                    ribv4_enter_dict = run_event_critical_details_dict.setdefault('ribv4_enter', {})

                    ribv4_enter_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #              RIBv4-Exit              3986              3986                 0
            m = p20.match(line)
            if m:
                if 'high' not in run_event_dict and 'medium' not in run_event_dict and 'low' not in run_event_dict and 'critical' in run_event_dict:
                    group = m.groupdict()
                    ribv4_exit_dict = run_event_critical_details_dict.setdefault('ribv4_exit', {})

                    ribv4_exit_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #              RIBv4-Redist              3986              3986                 0
            m = p21.match(line)
            if m:
                if 'high' not in run_event_dict and 'medium' not in run_event_dict and 'low' not in run_event_dict and 'critical' in run_event_dict:
                    group = m.groupdict()
                    ribv4_redist_dict = run_event_critical_details_dict.setdefault('ribv4_redist', {})

                    ribv4_redist_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #              LDP Enter              3986              3986                 0
            m = p22.match(line)
            if m:
                if 'high' not in run_event_dict and 'medium' not in run_event_dict and 'low' not in run_event_dict and 'critical' in run_event_dict:
                    group = m.groupdict()
                    ldp_enter_dict = run_event_critical_details_dict.setdefault('ldp_enter', {})

                    ldp_enter_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #              LDP Exit              3986              3986                 0
            m = p23.match(line)
            if m:
                if 'high' not in run_event_dict and 'medium' not in run_event_dict and 'low' not in run_event_dict and 'critical' in run_event_dict:
                    group = m.groupdict()
                    ldp_exit_dict = run_event_critical_details_dict.setdefault('ldp_exit', {})

                    ldp_exit_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #              LSD Enter              3986              3986                 0
            m = p24.match(line)
            if m:
                if 'high' not in run_event_dict and 'medium' not in run_event_dict and 'low' not in run_event_dict and 'critical' in run_event_dict:
                    group = m.groupdict()
                    lsd_enter_dict = run_event_critical_details_dict.setdefault('lsd_enter', {})

                    lsd_enter_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #              LSD Exit              3986              3986                 0
            m = p25.match(line)
            if m:
                if 'high' not in run_event_dict and 'medium' not in run_event_dict and 'low' not in run_event_dict and 'critical' in run_event_dict:
                    group = m.groupdict()
                    lsd_exit_dict = run_event_critical_details_dict.setdefault('lsd_exit', {})

                    lsd_exit_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #            LC Details(IP Path):
            m = p26.match(line)
            if m:
                if 'high' not in run_event_dict and 'medium' not in run_event_dict and 'low' not in run_event_dict and 'critical' in run_event_dict:
                    lc_dict = run_event_critical_details_dict.setdefault('lc', {})
                    ip_path_dict = lc_dict.setdefault('ip', {})
                    continue

            #                F 0/0/CPU0            3987              3987                 0
            m = p27.match(line)
            if m:
                if 'high' not in run_event_dict and 'medium' not in run_event_dict and 'low' not in run_event_dict and 'critical' in run_event_dict:
                    if 'mpls' not in lc_dict:
                        group = m.groupdict()
                        node_name = group['node_id']
                        ip_node_dict = ip_path_dict.setdefault(node_name, {})
                        temp_lc_ip_dict = {}
                        temp_lc_ip_dict.update({k: v for k, v in group.items() if 'node_id' not in k if v is not None})

                        for temp_key in temp_lc_ip_dict:
                            if 'start' in temp_key or 'end' in temp_key or 'duration' in temp_key:
                                ip_node_dict.update({temp_key:int(temp_lc_ip_dict[temp_key])})
                            else:
                                ip_node_dict.update({temp_key:temp_lc_ip_dict[temp_key]})
                        continue

            #            LC Details(MPLS Path):
            m = p28.match(line)
            if m:
                if 'high' not in run_event_dict and 'medium' not in run_event_dict and 'low' not in run_event_dict and 'critical' in run_event_dict:
                    mpls_path_dict = lc_dict.setdefault('mpls', {})
                    continue

            #                F 0/0/CPU0            3987              3987                 0
            m = p27.match(line)
            if m:
                if 'high' not in run_event_dict and 'medium' not in run_event_dict and 'low' not in run_event_dict and 'critical' in run_event_dict:
                    group = m.groupdict()
                    node_name = group['node_id']
                    mpls_node_dict = mpls_path_dict.setdefault(node_name, {})
                    temp_lc_mpls_dict = {}
                    temp_lc_mpls_dict.update({k: v for k, v in group.items() if 'node_id' not in k if v is not None})

                    for temp_key in temp_lc_mpls_dict:
                        if 'start' in temp_key or 'end' in temp_key or 'duration' in temp_key:
                            mpls_node_dict.update({temp_key:int(temp_lc_mpls_dict[temp_key])})
                        else:
                            mpls_node_dict.update({temp_key:temp_lc_mpls_dict[temp_key]})
                    continue

            #        Leaf Networks Added:
            m = p29.match(line)
            if m:
                if 'high' not in run_event_dict and 'medium' not in run_event_dict and 'low' not in run_event_dict and 'critical' in run_event_dict:
                    leaf_nws_add_dict = run_event_critical_dict.setdefault('leaf_nws_added', {})
                    continue

            #            3.3.3.3/32                  10.3.1.0/24
            #            4.4.4.4/32
            m = p30.match(line)
            if m:
                if 'high' not in run_event_dict and 'medium' not in run_event_dict and 'low' not in run_event_dict and 'critical' in run_event_dict:
                    if 'leaf_nws_deleted' not in run_event_critical_dict:
                        group = m.groupdict()

                        leaf_nws_add_dict.update({k: v for k, v in group.items() if v is not None})
                        continue

            #        Leaf Networks Deleted:
            m = p31.match(line)
            if m:
                if 'high' not in run_event_dict and 'medium' not in run_event_dict and 'low' not in run_event_dict and 'critical' in run_event_dict:
                    leaf_nws_delete_dict = run_event_critical_dict.setdefault('leaf_nws_deleted', {})
                    continue

            #            3.3.3.3/32                  10.3.1.0/24
            #            4.4.4.4/32
            m = p30.match(line)
            if m:
                if 'high' not in run_event_dict and 'medium' not in run_event_dict and 'low' not in run_event_dict and 'critical' in run_event_dict:
                    group = m.groupdict()

                    leaf_nws_delete_dict.update({k: v for k, v in group.items() if v is not None})
                    continue

            #        Priority: High
            m = p14.match(line)
            if m:
                run_event_high_dict = run_event_dict.setdefault('high', {})
                continue

            #            Route Count:                  Added: 0            Deleted: 0          Modified: 1
            m = p10.match(line)
            if m:
                if 'medium' not in run_event_dict and 'low' not in run_event_dict and 'high' in run_event_dict:
                    group = m.groupdict()
                    route_cnt_dict = run_event_high_dict.setdefault('route_cnt', {})

                    route_cnt_dict.update({
                        'added': int(group['added']),
                        'deleted': int(group['deleted']),
                        'modified': int(group['modified'])
                    })
                    continue

            #            IP Route Program Time:        Min: 3987(0/0/CPU0)           Max: 3987(0/0/CPU0)
            m = p12.match(line)
            if m:
                if 'medium' not in run_event_dict and 'low' not in run_event_dict and 'high' in run_event_dict:
                    group = m.groupdict()
                    ip_dict = run_event_high_dict.setdefault('ip_time', {})

                    ip_dict.update({
                        'min_time': int(group['min_time']),
                        'min_node_id': group['min_node_id'],
                        'max_time': int(group['max_time']),
                        'max_node_id': group['max_node_id']
                    })
                    continue

            #            MPLS Label Program Time:      Min: 403(0/0/CPU0)            Max: 403(0/0/CPU0)
            m = p13.match(line)
            if m:
                if 'medium' not in run_event_dict and 'low' not in run_event_dict and 'high' in run_event_dict:
                    group = m.groupdict()
                    mpls_dict = run_event_high_dict.setdefault('mpls_time', {})

                    mpls_dict.update({
                        'min_time': int(group['min_time']),
                        'min_node_id': group['min_node_id'],
                        'max_time': int(group['max_time']),
                        'max_node_id': group['max_node_id']
                    })
                    continue

            #        Details:                     Start               End          Duration
            m = p17.match(line)
            if m:
                if 'medium' not in run_event_dict and 'low' not in run_event_dict and 'high' in run_event_dict:
                    run_event_high_details_dict = run_event_high_dict.setdefault('details', {})
                    continue

            #              ISIS:                   3982              3982                 0
            m = p18.match(line)
            if m:
                if 'medium' not in run_event_dict and 'low' not in run_event_dict and 'high' in run_event_dict:
                    group = m.groupdict()
                    isis_dict = run_event_high_details_dict.setdefault('isis', {})

                    isis_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #              RIBv4-Enter             3982              3982                 0
            m = p19.match(line)
            if m:
                if 'medium' not in run_event_dict and 'low' not in run_event_dict and 'high' in run_event_dict:
                    group = m.groupdict()
                    ribv4_enter_dict = run_event_high_details_dict.setdefault('ribv4_enter', {})

                    ribv4_enter_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #              RIBv4-Exit              3986              3986                 0
            m = p20.match(line)
            if m:
                if 'medium' not in run_event_dict and 'low' not in run_event_dict and 'high' in run_event_dict:
                    group = m.groupdict()
                    ribv4_exit_dict = run_event_high_details_dict.setdefault('ribv4_exit', {})

                    ribv4_exit_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #              RIBv4-Redist              3986              3986                 0
            m = p21.match(line)
            if m:
                if 'medium' not in run_event_dict and 'low' not in run_event_dict and 'high' in run_event_dict:
                    group = m.groupdict()
                    ribv4_redist_dict = run_event_high_details_dict.setdefault('ribv4_redist', {})

                    ribv4_redist_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #              LDP Enter              3986              3986                 0
            m = p22.match(line)
            if m:
                if 'medium' not in run_event_dict and 'low' not in run_event_dict and 'high' in run_event_dict:
                    group = m.groupdict()
                    ldp_enter_dict = run_event_high_details_dict.setdefault('ldp_enter', {})

                    ldp_enter_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #              LDP Exit              3986              3986                 0
            m = p23.match(line)
            if m:
                if 'medium' not in run_event_dict and 'low' not in run_event_dict and 'high' in run_event_dict:
                    group = m.groupdict()
                    ldp_exit_dict = run_event_high_details_dict.setdefault('ldp_exit', {})

                    ldp_exit_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #              LSD Enter              3986              3986                 0
            m = p24.match(line)
            if m:
                if 'medium' not in run_event_dict and 'low' not in run_event_dict and 'high' in run_event_dict:
                    group = m.groupdict()
                    lsd_enter_dict = run_event_high_details_dict.setdefault('lsd_enter', {})

                    lsd_enter_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #              LSD Exit              3986              3986                 0
            m = p25.match(line)
            if m:
                if 'medium' not in run_event_dict and 'low' not in run_event_dict and 'high' in run_event_dict:
                    group = m.groupdict()
                    lsd_exit_dict = run_event_high_details_dict.setdefault('lsd_exit', {})

                    lsd_exit_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #            LC Details(IP Path):
            m = p26.match(line)
            if m:
                if 'medium' not in run_event_dict and 'low' not in run_event_dict and 'high' in run_event_dict:
                    lc_dict = run_event_high_details_dict.setdefault('lc', {})
                    ip_path_dict = lc_dict.setdefault('ip', {})
                    continue

            #                F 0/0/CPU0            3987              3987                 0
            m = p27.match(line)
            if m:
                if 'medium' not in run_event_dict and 'low' not in run_event_dict and 'high' in run_event_dict:
                    if 'mpls' not in lc_dict:
                        group = m.groupdict()
                        node_name = group['node_id']
                        ip_node_dict = ip_path_dict.setdefault(node_name, {})
                        temp_lc_ip_dict = {}
                        temp_lc_ip_dict.update({k: v for k, v in group.items() if 'node_id' not in k if v is not None})

                        for temp_key in temp_lc_ip_dict:
                            if 'start' in temp_key or 'end' in temp_key or 'duration' in temp_key:
                                ip_node_dict.update({temp_key:int(temp_lc_ip_dict[temp_key])})
                            else:
                                ip_node_dict.update({temp_key:temp_lc_ip_dict[temp_key]})
                        continue

            #            LC Details(MPLS Path):
            m = p28.match(line)
            if m:
                if 'medium' not in run_event_dict and 'low' not in run_event_dict and 'high' in run_event_dict:
                    mpls_path_dict = lc_dict.setdefault('mpls', {})
                    continue

            #                F 0/0/CPU0            3987              3987                 0
            m = p27.match(line)
            if m:
                if 'medium' not in run_event_dict and 'low' not in run_event_dict and 'high' in run_event_dict:
                    group = m.groupdict()
                    node_name = group['node_id']
                    mpls_node_dict = mpls_path_dict.setdefault(node_name, {})
                    temp_lc_mpls_dict = {}
                    temp_lc_mpls_dict.update({k: v for k, v in group.items() if 'node_id' not in k if v is not None})

                    for temp_key in temp_lc_mpls_dict:
                        if 'start' in temp_key or 'end' in temp_key or 'duration' in temp_key:
                            mpls_node_dict.update({temp_key:int(temp_lc_mpls_dict[temp_key])})
                        else:
                            mpls_node_dict.update({temp_key:temp_lc_mpls_dict[temp_key]})
                    continue

            #        Leaf Networks Added:
            m = p29.match(line)
            if m:
                if 'medium' not in run_event_dict and 'low' not in run_event_dict and 'high' in run_event_dict:
                    leaf_nws_add_dict = run_event_high_dict.setdefault('leaf_nws_added', {})
                    continue

            #            3.3.3.3/32                  10.3.1.0/24
            #            4.4.4.4/32
            m = p30.match(line)
            if m:
                if 'medium' not in run_event_dict and 'low' not in run_event_dict and 'high' in run_event_dict:
                    if 'leaf_nws_deleted' not in run_event_high_dict:
                        group = m.groupdict()

                        leaf_nws_add_dict.update({k: v for k, v in group.items() if v is not None})
                        continue

            #        Leaf Networks Deleted:
            m = p31.match(line)
            if m:
                if 'medium' not in run_event_dict and 'low' not in run_event_dict and 'high' in run_event_dict:
                    leaf_nws_delete_dict = run_event_high_dict.setdefault('leaf_nws_deleted', {})
                    continue

            #            3.3.3.3/32                  10.3.1.0/24
            #            4.4.4.4/32
            m = p30.match(line)
            if m:
                if 'medium' not in run_event_dict and 'low' not in run_event_dict and 'high' in run_event_dict:
                    group = m.groupdict()

                    leaf_nws_delete_dict.update({k: v for k, v in group.items() if v is not None})
                    continue

            #        Priority: Medium
            m = p15.match(line)
            if m:
                run_event_medium_dict = run_event_dict.setdefault('medium', {})
                continue

            #            Route Count:                  Added: 0            Deleted: 0          Modified: 1
            m = p10.match(line)
            if m:
                if 'low' not in run_event_dict and 'medium' in run_event_dict:
                    group = m.groupdict()
                    route_cnt_dict = run_event_medium_dict.setdefault('route_cnt', {})

                    route_cnt_dict.update({
                        'added': int(group['added']),
                        'deleted': int(group['deleted']),
                        'modified': int(group['modified'])
                    })
                    continue

            #            IP Route Program Time:        Min: 3987(0/0/CPU0)           Max: 3987(0/0/CPU0)
            m = p12.match(line)
            if m:
                if 'low' not in run_event_dict and 'medium' in run_event_dict:
                    group = m.groupdict()
                    ip_dict = run_event_medium_dict.setdefault('ip_time', {})

                    ip_dict.update({
                        'min_time': int(group['min_time']),
                        'min_node_id': group['min_node_id'],
                        'max_time': int(group['max_time']),
                        'max_node_id': group['max_node_id']
                    })
                    continue

            #            MPLS Label Program Time:      Min: 403(0/0/CPU0)            Max: 403(0/0/CPU0)
            m = p13.match(line)
            if m:
                if 'low' not in run_event_dict and 'medium' in run_event_dict:
                    group = m.groupdict()
                    mpls_dict = run_event_medium_dict.setdefault('mpls_time', {})

                    mpls_dict.update({
                        'min_time': int(group['min_time']),
                        'min_node_id': group['min_node_id'],
                        'max_time': int(group['max_time']),
                        'max_node_id': group['max_node_id']
                    })
                    continue

            #        Details:                     Start               End          Duration
            m = p17.match(line)
            if m:
                if 'low' not in run_event_dict and 'medium' in run_event_dict:
                    run_event_medium_details_dict = run_event_medium_dict.setdefault('details', {})
                    continue

            #              ISIS:                   3982              3982                 0
            m = p18.match(line)
            if m:
                if 'low' not in run_event_dict and 'medium' in run_event_dict:
                    group = m.groupdict()
                    isis_dict = run_event_medium_details_dict.setdefault('isis', {})

                    isis_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #              RIBv4-Enter             3982              3982                 0
            m = p19.match(line)
            if m:
                if 'low' not in run_event_dict and 'medium' in run_event_dict:
                    group = m.groupdict()
                    ribv4_enter_dict = run_event_medium_details_dict.setdefault('ribv4_enter', {})

                    ribv4_enter_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #              RIBv4-Exit              3986              3986                 0
            m = p20.match(line)
            if m:
                if 'low' not in run_event_dict and 'medium' in run_event_dict:
                    group = m.groupdict()
                    ribv4_exit_dict = run_event_medium_details_dict.setdefault('ribv4_exit', {})

                    ribv4_exit_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #              RIBv4-Redist              3986              3986                 0
            m = p21.match(line)
            if m:
                if 'low' not in run_event_dict and 'medium' in run_event_dict:
                    group = m.groupdict()
                    ribv4_redist_dict = run_event_medium_details_dict.setdefault('ribv4_redist', {})

                    ribv4_redist_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #              LDP Enter              3986              3986                 0
            m = p22.match(line)
            if m:
                if 'low' not in run_event_dict and 'medium' in run_event_dict:
                    group = m.groupdict()
                    ldp_enter_dict = run_event_medium_details_dict.setdefault('ldp_enter', {})

                    ldp_enter_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #              LDP Exit              3986              3986                 0
            m = p23.match(line)
            if m:
                if 'low' not in run_event_dict and 'medium' in run_event_dict:
                    group = m.groupdict()
                    ldp_exit_dict = run_event_medium_details_dict.setdefault('ldp_exit', {})

                    ldp_exit_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #              LSD Enter              3986              3986                 0
            m = p24.match(line)
            if m:
                if 'low' not in run_event_dict and 'medium' in run_event_dict:
                    group = m.groupdict()
                    lsd_enter_dict = run_event_medium_details_dict.setdefault('lsd_enter', {})

                    lsd_enter_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #              LSD Exit              3986              3986                 0
            m = p25.match(line)
            if m:
                if 'low' not in run_event_dict and 'medium' in run_event_dict:
                    group = m.groupdict()
                    lsd_exit_dict = run_event_medium_details_dict.setdefault('lsd_exit', {})

                    lsd_exit_dict.update({
                        'start': int(group['start']),
                        'end': int(group['end']),
                        'duration': int(group['duration'])
                    })
                    continue

            #            LC Details(IP Path):
            m = p26.match(line)
            if m:
                if 'low' not in run_event_dict and 'medium' in run_event_dict:
                    lc_dict = run_event_medium_details_dict.setdefault('lc', {})
                    ip_path_dict = lc_dict.setdefault('ip', {})
                    continue

            #                F 0/0/CPU0            3987              3987                 0
            m = p27.match(line)
            if m:
                if 'low' not in run_event_dict and 'medium' in run_event_dict:
                    if 'mpls' not in lc_dict:
                        group = m.groupdict()
                        node_name = group['node_id']
                        ip_node_dict = ip_path_dict.setdefault(node_name, {})
                        temp_lc_ip_dict = {}
                        temp_lc_ip_dict.update({k: v for k, v in group.items() if 'node_id' not in k if v is not None})

                        for temp_key in temp_lc_ip_dict:
                            if 'start' in temp_key or 'end' in temp_key or 'duration' in temp_key:
                                ip_node_dict.update({temp_key:int(temp_lc_ip_dict[temp_key])})
                            else:
                                ip_node_dict.update({temp_key:temp_lc_ip_dict[temp_key]})
                        continue

            #            LC Details(MPLS Path):
            m = p28.match(line)
            if m:
                if 'low' not in run_event_dict and 'medium' in run_event_dict:
                    mpls_path_dict = lc_dict.setdefault('mpls', {})
                    continue

            #                F 0/0/CPU0            3987              3987                 0
            m = p27.match(line)
            if m:
                if 'low' not in run_event_dict and 'medium' in run_event_dict:
                    group = m.groupdict()
                    node_name = group['node_id']
                    mpls_node_dict = mpls_path_dict.setdefault(node_name, {})
                    temp_lc_mpls_dict = {}
                    temp_lc_mpls_dict.update({k: v for k, v in group.items() if 'node_id' not in k if v is not None})

                    for temp_key in temp_lc_mpls_dict:
                        if 'start' in temp_key or 'end' in temp_key or 'duration' in temp_key:
                            mpls_node_dict.update({temp_key:int(temp_lc_mpls_dict[temp_key])})
                        else:
                            mpls_node_dict.update({temp_key:temp_lc_mpls_dict[temp_key]})
                    continue

            #        Leaf Networks Added:
            m = p29.match(line)
            if m:
                if 'low' not in run_event_dict and 'medium' in run_event_dict:
                    leaf_nws_add_dict = run_event_medium_dict.setdefault('leaf_nws_added', {})
                    continue

            #            3.3.3.3/32                  10.3.1.0/24
            #            4.4.4.4/32
            m = p30.match(line)
            if m:
                if 'low' not in run_event_dict and 'medium' in run_event_dict:
                    if 'leaf_nws_deleted' not in run_event_medium_dict:
                        group = m.groupdict()

                        leaf_nws_add_dict.update({k: v for k, v in group.items() if v is not None})
                        continue

            #        Leaf Networks Deleted:
            m = p31.match(line)
            if m:
                if 'low' not in run_event_dict and 'medium' in run_event_dict:
                    leaf_nws_delete_dict = run_event_medium_dict.setdefault('leaf_nws_deleted', {})
                    continue

            #            3.3.3.3/32                  10.3.1.0/24
            #            4.4.4.4/32
            m = p30.match(line)
            if m:
                if 'low' not in run_event_dict and 'medium' in run_event_dict:
                    group = m.groupdict()

                    leaf_nws_delete_dict.update({k: v for k, v in group.items() if v is not None})
                    continue

            #        Priority: Low
            m = p16.match(line)
            if m:
                run_event_low_dict = run_event_dict.setdefault('low', {})
                continue

            #            Route Count:                  Added: 0            Deleted: 0          Modified: 1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                route_cnt_dict = run_event_low_dict.setdefault('route_cnt', {})

                route_cnt_dict.update({
                    'added': int(group['added']),
                    'deleted': int(group['deleted']),
                    'modified': int(group['modified'])
                })
                continue

            #            IP Route Program Time:        Min: 3987(0/0/CPU0)           Max: 3987(0/0/CPU0)
            m = p12.match(line)
            if m:
                group = m.groupdict()
                ip_dict = run_event_low_dict.setdefault('ip_time', {})

                ip_dict.update({
                    'min_time': int(group['min_time']),
                    'min_node_id': group['min_node_id'],
                    'max_time': int(group['max_time']),
                    'max_node_id': group['max_node_id']
                })
                continue

            #            MPLS Label Program Time:      Min: 403(0/0/CPU0)            Max: 403(0/0/CPU0)
            m = p13.match(line)
            if m:
                group = m.groupdict()
                mpls_dict = run_event_low_dict.setdefault('mpls_time', {})

                mpls_dict.update({
                    'min_time': int(group['min_time']),
                    'min_node_id': group['min_node_id'],
                    'max_time': int(group['max_time']),
                    'max_node_id': group['max_node_id']
                })
                continue

            #        Details:                     Start               End          Duration
            m = p17.match(line)
            if m:
                run_event_low_details_dict = run_event_low_dict.setdefault('details', {})
                continue

            #              ISIS:                   3982              3982                 0
            m = p18.match(line)
            if m:
                group = m.groupdict()
                isis_dict = run_event_low_details_dict.setdefault('isis', {})

                isis_dict.update({
                    'start': int(group['start']),
                    'end': int(group['end']),
                    'duration': int(group['duration'])
                })
                continue

            #              RIBv4-Enter             3982              3982                 0
            m = p19.match(line)
            if m:
                group = m.groupdict()
                ribv4_enter_dict = run_event_low_details_dict.setdefault('ribv4_enter', {})

                ribv4_enter_dict.update({
                    'start': int(group['start']),
                    'end': int(group['end']),
                    'duration': int(group['duration'])
                })
                continue

            #              RIBv4-Exit              3986              3986                 0
            m = p20.match(line)
            if m:
                group = m.groupdict()
                ribv4_exit_dict = run_event_low_details_dict.setdefault('ribv4_exit', {})

                ribv4_exit_dict.update({
                    'start': int(group['start']),
                    'end': int(group['end']),
                    'duration': int(group['duration'])
                })
                continue

            #              RIBv4-Redist              3986              3986                 0
            m = p21.match(line)
            if m:
                group = m.groupdict()
                ribv4_redist_dict = run_event_low_details_dict.setdefault('ribv4_redist', {})

                ribv4_redist_dict.update({
                    'start': int(group['start']),
                    'end': int(group['end']),
                    'duration': int(group['duration'])
                })
                continue

            #              LDP Enter              3986              3986                 0
            m = p22.match(line)
            if m:
                group = m.groupdict()
                ldp_enter_dict = run_event_low_details_dict.setdefault('ldp_enter', {})

                ldp_enter_dict.update({
                    'start': int(group['start']),
                    'end': int(group['end']),
                    'duration': int(group['duration'])
                })
                continue

            #              LDP Exit              3986              3986                 0
            m = p23.match(line)
            if m:
                group = m.groupdict()
                ldp_exit_dict = run_event_low_details_dict.setdefault('ldp_exit', {})

                ldp_exit_dict.update({
                    'start': int(group['start']),
                    'end': int(group['end']),
                    'duration': int(group['duration'])
                })
                continue

            #              LSD Enter              3986              3986                 0
            m = p24.match(line)
            if m:
                group = m.groupdict()
                lsd_enter_dict = run_event_low_details_dict.setdefault('lsd_enter', {})

                lsd_enter_dict.update({
                    'start': int(group['start']),
                    'end': int(group['end']),
                    'duration': int(group['duration'])
                })
                continue

            #              LSD Exit              3986              3986                 0
            m = p25.match(line)
            if m:
                group = m.groupdict()
                lsd_exit_dict = run_event_low_details_dict.setdefault('lsd_exit', {})

                lsd_exit_dict.update({
                    'start': int(group['start']),
                    'end': int(group['end']),
                    'duration': int(group['duration'])
                })
                continue

            #            LC Details(IP Path):
            m = p26.match(line)
            if m:
                lc_dict = run_event_low_details_dict.setdefault('lc', {})
                ip_path_dict = lc_dict.setdefault('ip', {})
                continue

            #                F 0/0/CPU0            3987              3987                 0
            m = p27.match(line)
            if m:
                if 'mpls' not in lc_dict:
                    group = m.groupdict()
                    node_name = group['node_id']
                    ip_node_dict = ip_path_dict.setdefault(node_name, {})
                    temp_lc_ip_dict = {}
                    temp_lc_ip_dict.update({k: v for k, v in group.items() if 'node_id' not in k if v is not None})

                    for temp_key in temp_lc_ip_dict:
                        if 'start' in temp_key or 'end' in temp_key or 'duration' in temp_key:
                            ip_node_dict.update({temp_key:int(temp_lc_ip_dict[temp_key])})
                        else:
                            ip_node_dict.update({temp_key:temp_lc_ip_dict[temp_key]})
                    continue

            #            LC Details(MPLS Path):
            m = p28.match(line)
            if m:
                mpls_path_dict = lc_dict.setdefault('mpls', {})
                continue

            #                F 0/0/CPU0            3987              3987                 0
            m = p27.match(line)
            if m:
                group = m.groupdict()
                node_name = group['node_id']
                mpls_node_dict = mpls_path_dict.setdefault(node_name, {})
                temp_lc_mpls_dict = {}
                temp_lc_mpls_dict.update({k: v for k, v in group.items() if 'node_id' not in k if v is not None})

                for temp_key in temp_lc_mpls_dict:
                    if 'start' in temp_key or 'end' in temp_key or 'duration' in temp_key:
                        mpls_node_dict.update({temp_key:int(temp_lc_mpls_dict[temp_key])})
                    else:
                        mpls_node_dict.update({temp_key:temp_lc_mpls_dict[temp_key]})
                continue

            #        Leaf Networks Added:
            m = p29.match(line)
            if m:
                leaf_nws_add_dict = run_event_low_dict.setdefault('leaf_nws_added', {})
                continue

            #            3.3.3.3/32                  10.3.1.0/24
            #            4.4.4.4/32
            m = p30.match(line)
            if m:
                if 'leaf_nws_deleted' not in run_event_low_dict:
                    group = m.groupdict()

                    leaf_nws_add_dict.update({k: v for k, v in group.items() if v is not None})
                    continue

            #        Leaf Networks Deleted:
            m = p31.match(line)
            if m:
                leaf_nws_delete_dict = run_event_low_dict.setdefault('leaf_nws_deleted', {})
                continue

            #            3.3.3.3/32                  10.3.1.0/24
            #            4.4.4.4/32
            m = p30.match(line)
            if m:
                group = m.groupdict()

                leaf_nws_delete_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            #    LSP Processed:
            m = p32.match(line)
            if m:
                lsp_processed_dict = run_event_dict.setdefault('lsp_processed', {})
                continue

            #        Id: 2037.0685.b002.00-00  Seq: b  Change-type: Modify  Recv-Time: Sep 19 18:11:17.193
            m = p33.match(line)
            if m:
                if 'lsp_regenerated' not in run_event_dict:
                    group = m.groupdict()
                    lsp_id = group['id']
                    lsp_processed_id_dict = lsp_processed_dict.setdefault(lsp_id, {})

                    lsp_processed_id_dict.update({
                        'seq': group['seq'],
                        'change_type': group['change_type'],
                        'recv_time': group['recv_time']
                    })
                    continue

            #    LSP Regenerated:
            m = p34.match(line)
            if m:
                lsp_regenerated_dict = run_event_dict.setdefault('lsp_regenerated', {})
                continue

            #        Id: 2037.0685.b002.00-00  Seq: b  Change-type: Modify  Recv-Time: Sep 19 18:11:17.193
            m = p33.match(line)
            if m:
                group = m.groupdict()
                lsp_id = group['id']
                lsp_regenerated_id_dict = lsp_regenerated_dict.setdefault(lsp_id, {})

                lsp_regenerated_id_dict.update({
                    'seq': group['seq'],
                    'change_type': group['change_type'],
                    'recv_time': group['recv_time']
                })

        return rcmd_dict



# ========================================================
# Schema for:
#    * 'show rcmd process'
# ========================================================

class ShowRcmdProcessSchema(MetaParser):
    """ Schema for:
        * 'show rcmd process'
    """
    schema = {
        Optional('rcmd_process'): {
            Any(): {
                'protocol': str,
                'process': str,
                Optional('rcmd_instance'): {
                    Any(): {
                        'inst_name': str,
                        'upd_time': str,
                        Optional('spf_name'): {
                            'spf_name_t': int,
                            'spf_name_rc': int,
                            'spf_name_nr': int,
                            'spf_name_ni': int,
                            'lsp_c': int,
                            'lsp_l': int,
                            'arch_spf': int,
                            'arch_lsp': int,
                            Optional('inst_id'): {
                                Any(): {
                                    Optional('id'): int,
                                    Optional('upd_time_id'): str,
                                    Optional('state'): str,
                                    Optional('deleted'): str,
                                    Optional('fwdref'): str,
                                    Optional('spfoff'): int,
                                    Optional('spf_id'): {
                                        'spf_id_t': int,
                                        'spf_id_rc': int,
                                        'spf_id_nr': int,
                                        'spf_id_ni': int,
                                        'arch_cnt': int,
                                        'total_cnt': int
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

# ========================================================
# Parser for:
#    * 'show rcmd process'
# ========================================================

class ShowRcmdProcess(ShowRcmdProcessSchema):
    """ Parser for:
        * 'show rcmd process'
    """
    cli_command = 'show rcmd process'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        rcmd_dict = {}

        #Protocol: ISIS    Process Name: isis1
        p0 = re.compile(r'^(Protocol): +(?P<protocol>[\w+]+)\s+(Process +Name): +(?P<process>[\w+]+)$')

        #    Inst-Name: default:default:0 Upd-Time: Oct 17 11:52:13.768
        p1 = re.compile(r'^(Inst-Name): +(?P<inst_name>[\w:\-]+)\s+(Upd-Time): +(?P<upd_time>[a-zA-Z]+\s+\d{2}\s+\d{2}\:\d{2}\:\d{2}\.\d+)$')

        #      Spf(T/RC/NR/NI): 8/0/0/0 LSP(C/L): 0/11 Arch(Spf/Lsp): 0/0
        p2 = re.compile(r'^ *Spf\(T/RC/NR/NI\): *(?P<inst_name_spf>\S+) *LSP\(C/L\): *(?P<lsp_details>\S+) *Arch\(Spf/Lsp\): *(?P<arch_details>\S+) *$')

        #        Inst-Id: 213166328 Upd-Time: Oct 17 05:25:24.102 State: InActive Deleted: No FwdRef: No SpfOff: 0
        p3 = re.compile(r'^(Inst-Id):\s+(?P<id>\S+[\d]+)\s+(Upd-Time):\s+(?P<upd_time_id>\S+[a-zA-Z]+\s+\d{2}\s+\d{2}\:\d{2}\:\d{2}\.\d+)\s+(State):\s+(?P<state>\S+[\w]+)\s+(Deleted):\s+(?P<deleted>\S+[\w]+)\s+(FwdRef):\s+(?P<fwdref>\S+[\w]+)\s+(SpfOff):\s+(?P<spfoff>\S+)+$')

        #          Spf(T/RC/NR/NI): 6/4/2/0 Arch(Spf): 0 Total(Spt): 0
        p4 = re.compile(r'^ *Spf\(T/RC/NR/NI\): *(?P<inst_id_spf>\S+) *Arch\(Spf\): *(?P<arch_cnt>\S+) *Total\(Spt\): *(?P<total_cnt>\S+) *$')

        for line in output.splitlines():
            line = line.strip()

            #Protocol: ISIS    Process Name: isis1
            m = p0.match(line)
            if m:
                group = m.groupdict()
                inter_dict = rcmd_dict.setdefault('rcmd_process', {})
                process_name = group['process']
                process_dict = inter_dict.setdefault(process_name,{})

                process_dict.update({
                    'protocol': group['protocol'],
                    'process': group['process']
                })
                continue

            #    Inst-Name: default:default:0 Upd-Time: Oct 17 11:52:13.768
            m = p1.match(line)
            if m:
                group = m.groupdict()
                inter_dict = process_dict.setdefault('rcmd_instance',{})
                inst_name = group['inst_name']
                inst_dict = inter_dict.setdefault(inst_name, {})

                inst_dict.update({
                    'inst_name': group['inst_name'],
                    'upd_time': group['upd_time']
                })
                continue

            #      Spf(T/RC/NR/NI): 8/0/0/0 LSP(C/L): 0/11 Arch(Spf/Lsp): 0/0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                spf_name_dict = inst_dict.setdefault('spf_name',{})
                inst_name_spf = group['inst_name_spf'].split('/')
                lsp_details = group['lsp_details'].split('/')
                arch_details = group['arch_details'].split('/')

                spf_name_dict.update({
                    'spf_name_t': int(inst_name_spf[0]),
                    'spf_name_rc': int(inst_name_spf[1]),
                    'spf_name_nr': int(inst_name_spf[2]),
                    'spf_name_ni': int(inst_name_spf[3]),
                    'lsp_c': int(lsp_details[0]),
                    'lsp_l': int(lsp_details[1]),
                    'arch_spf': int(arch_details[0]),
                    'arch_lsp': int(arch_details[1])
                })
                continue

            #        Inst-Id: 213166328 Upd-Time: Oct 17 05:25:24.102 State: InActive Deleted: No FwdRef: No SpfOff: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                inter_dict = spf_name_dict.setdefault('inst_id', {})
                inst_id = int(group['id'])
                result_dict = inter_dict.setdefault(inst_id,{})

                result_dict.update({
                    'id': int(group['id']),
                    'upd_time_id': group['upd_time_id'],
                    'state': group['state'],
                    'deleted': group['deleted'],
                    'fwdref': group['fwdref'],
                    'spfoff': int(group['spfoff'])
                })
                continue

            #          Spf(T/RC/NR/NI): 6/4/2/0 Arch(Spf): 0 Total(Spt): 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                spf_id_dict = result_dict.setdefault('spf_id',{})
                inst_id_spf = group['inst_id_spf'].split('/')

                spf_id_dict.update({
                    'spf_id_t': int(inst_id_spf[0]),
                    'spf_id_rc': int(inst_id_spf[1]),
                    'spf_id_nr': int(inst_id_spf[2]),
                    'spf_id_ni': int(inst_id_spf[3]),
                    'arch_cnt': int(group['arch_cnt']),
                    'total_cnt': int(group['total_cnt'])
                })
                continue

        return rcmd_dict



# ========================================================
# Schema for:
#    * 'show rcmd interface event'
# ========================================================

class ShowRcmdInterfaceEventSchema(MetaParser):
    """ Schema for:
        * 'show rcmd interface event'
    """
    schema = {
        'sno': {
            Any(): {
                'protocol': str,
                'interface': str,
                'event_type': str,
                'time': str,
                'address': str,
            }
        }
    }

# ========================================================
# Parser for:
#    * 'show rcmd interface event'
# ========================================================

class ShowRcmdInterfaceEvent(ShowRcmdInterfaceEventSchema):
    """ Parser for:
        * 'show rcmd interface event'
    """
    cli_command = 'show rcmd interface event'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        rcmd_dict = {}

        #  4  |  ISIS  |     HundredGigE0/0/0/0     |     LinkUp     | Oct 17 05:25:25.109 |    10.1.1.1
        p0 = re.compile(r'^(?P<sno>\d+)\s+\|\s+(?P<protocol>\S+)\s+\|\s+(?P<interface>\S+)\s+\|\s+(?P<event_type>\S+)\s+\|\s+(?P<time>[a-zA-Z]+\s+\d{1,2}\s+\d{2}\:\d{2}\:\d{2}\.\d+)\s+\|\s+(?P<address>[\d\.\/]+)$')

        for line in output.splitlines():
            line = line.strip()

            #  4  |  ISIS  |     HundredGigE0/0/0/0     |     LinkUp     | Oct 17 05:25:25.109 |    10.1.1.1
            m = p0.match(line)
            if m:
                group = m.groupdict()
                s_no = int(group['sno'])
                result_dict = rcmd_dict.setdefault('sno', {}).setdefault(s_no, {})

                result_dict.update({
                    'protocol': group['protocol'],
                    'interface': group['interface'],
                    'event_type': group['event_type'],
                    'time': group['time'],
                    'address': group['address']
                })
                continue

        return rcmd_dict
