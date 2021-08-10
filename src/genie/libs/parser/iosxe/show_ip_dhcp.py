"""
show ip dhcp database
show ip dhcp snooping database
show ip dhcp snooping database detail
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Schema, Any, Optional,
                                                Or, And, Default, Use)

# Parser Utils
from genie.libs.parser.utils.common import Common

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