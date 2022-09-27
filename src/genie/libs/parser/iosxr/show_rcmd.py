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



# ====================================================
#  schema for show rcmd isis {isis} event spf
# ====================================================

class ShowRcmdIsisEventSpfSchema(MetaParser):
    """Schema for show rcmd isis {isis} event spf"""
    schema = {
        Any(): {
            Any(): {
                'trigger_time': str,
                'duration_time': int,
                'type': str,
                'lsp': int,
                'total_prefixes_affected_critical': str,
                'time_taken_ip_critical': str,
                'time_taken_mpls_critical': str,
                'total_prefixes_affected_high': str,
                'time_taken_ip_high': str,
                'time_taken_mpls_high': str,
                'total_prefixes_affected_medium': str,
                'time_taken_ip_medium': str,
                'time_taken_mpls_medium': str,
                'total_prefixes_affected_low': str,
                'time_taken_ip_low': str,
                'time_taken_mpls_low': str
            }
        }
    }

# ====================================================
#  parser for show rcmd isis {isis} event spf
# ====================================================

class ShowRcmdIsisEventSpf(ShowRcmdIsisEventSpfSchema):
    """Parser for :
        show rcmd isis {isis} event spf
    """
    cli_command = 'show rcmd isis {isis} event spf'

    def cli(self, isis='', output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(isis=isis))

        rcmd_dict = {}

        # Reporting SPF Events for ISIS Instance : isis1
        p0 = re.compile(r'^\s*Reporting SPF Events for ISIS Instance.*: *(?P<isis_inst_id>.+) *')

        #  2        Aug  9 05:47:43.340     0     FULL    9              5 / - / -                     0 / - / -                     0 / - / -                     0 / - / -
        p1 = re.compile(r'^\s*(?P<spf>[~*#^\s]* *\d+) *(?P<trigger_time>\w+ *\d+ *[\d:.]+) *(?P<duration_time>\d+) *(?P<type>\w+) *(?P<lsp>\d+) *(?P<total_prefixes_affected_critical>[\d-]+) */ *(?P<time_taken_ip_critical>[\d-]+) */ *(?P<time_taken_mpls_critical>[\d-]+) *(?P<total_prefixes_affected_high>[\d-]+) */ *(?P<time_taken_ip_high>[\d-]+) */ *(?P<time_taken_mpls_high>[\d-]+) *(?P<total_prefixes_affected_medium>[\d-]+) */ *(?P<time_taken_ip_medium>[\d-]+) */ *(?P<time_taken_mpls_medium>[\d-]+) *(?P<total_prefixes_affected_low>[\d-]+) */ *(?P<time_taken_ip_low>[\d-]+) */ *(?P<time_taken_mpls_low>[\d-]+)')

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
                spf_name =  group['spf']
                result_dict = inter_dict.setdefault(spf_name, {})

                result_dict.update({
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
                continue

        return rcmd_dict




# ====================================================
#  schema for show rcmd isis {isis} event prefix
# ====================================================

class ShowRcmdIsisEventPrefixSchema(MetaParser):
    """Schema for show rcmd isis {isis} event prefix"""
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

# ====================================================
#  parser for show rcmd isis {isis} event prefix
# ====================================================

class ShowRcmdIsisEventPrefix(ShowRcmdIsisEventPrefixSchema):
    """Parser for :
        show rcmd isis {isis} event prefix
    """
    cli_command = 'show rcmd isis {isis} event prefix'

    def cli(self, isis='', output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(isis=isis))

        rcmd_dict = {}

        # ISIS process : isis1
        p0 = re.compile(r'^\s*ISIS process.*: *(?P<isis_inst_id>.+) *')

        #        1   4.4.4.4/32           Aug 11 07:53:16.105   Medium    Primary      Add         L1          40
        p1 = re.compile(r'^\s*(?P<event_id>[~*#^\s]* *\d+) *(?P<prefix>[\d\.\/]+) *(?P<trigger_time>\w+ *\d+ *[\d:.]+) *(?P<priority>\w+) *(?P<path_type>\w+) *(?P<change_type>\w+) *(?P<route>\w+) *(?P<cost>\d+) *')

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
                event_id =  group['event_id']
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
