"""  show_mfib.py
   supported commands:
        *  show ip mfib vrf <vrf> summary
        *  show ip mfib vrf <vrf> active | c HW Rate
        *  show ip mfib vrf <vrf> active
        *  show ip mfib summary
        *  show ipv6 mfib interface 
        *  show ipv6 mfib active
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or

class ShowIpMfibVrfSummarySchema(MetaParser):
    """Schema for:
        show ip mfib vrf {vrf} summary
    """
    schema = {
        'vrf': {
            Any():{
                'prefixes':{
                    'total':int,
                    'fwd':int,
                    'non_fwd':int,
                    'deleted':int
                },
                'ioitems':{
                    'total':int,
                    'fwd':int,
                    'non_fwd':int,
                    'deleted':int
                },
                'forwarding_prefixes':{
                    's_g':int,
                    'g':int,
                    'g_m':int
                },
                'table_id':str,
                'instance':str,
                'database':str
            },
        }
    }
    
class ShowIpMfibVrfSummary(ShowIpMfibVrfSummarySchema):
    """Parser for show ip mfib vrf {vrf} summary parameters"""

    cli_command = 'show ip mfib vrf {vrf} summary'

    def cli(self, vrf, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(vrf=vrf))
        else:
            out = output

        # initial return dictionary
        result_dict = {}
    
        ##VRF vrf3001
        p1=re.compile(r"^VRF (\S+)$")
        
        ##49 prefixes (49/0/0 fwd/non-fwd/deleted)
        ##98 ioitems (98/0/0 fwd/non-fwd/deleted)
        p2=re.compile(r"^(?P<total>\d+)\s+(?P<field>\S+) \((?P<fwd>\d+)\/(?P<non_fwd>\d+)\/(?P<deleted>\d+).*$")
        
        ##Forwarding prefixes: [20 (S,G), 27 (*,G), 2 (*,G/m)]
        p3=re.compile(r"^Forwarding prefixes:\s+\[(?P<s_g>\d+)[ \(A-z\,\)]+\,\s+(?P<g>\d+)[ \(\*\,A-Z\)]+\,\s+(?P<g_m>\d+).*$")
        
        ##Table id 0xB, instance 0x7FC5BE77F480
        p4=re.compile(r"^Table id (?P<table_id>\S+)\,\s+instance\s+(?P<instance>\S+)$")
        
        ##Database: epoch 0
        p5=re.compile(r"Database: ([a-z0-9 ]+)")
        
        for line in out.splitlines():
            line=line.strip()
            
            ##VRF vrf3001
            m=p1.match(line)
            if m:
               prefix_dict=result_dict.setdefault('vrf',{}).setdefault(m.groups()[0],{}) 
               continue
               
            ##49 prefixes (49/0/0 fwd/non-fwd/deleted)
            ##98 ioitems (98/0/0 fwd/non-fwd/deleted)
            m=p2.match(line)
            if m:
                r=m.groupdict()
                dict2=prefix_dict.setdefault(r['field'],{})
                r.pop('field')
                for key,value in r.items():
                    dict2.update({key:int(value)})
                continue
                
            ##Forwarding prefixes: [20 (S,G), 27 (*,G), 2 (*,G/m)]
            m=p3.match(line)
            if m:
                r=m.groupdict()
                dict3=prefix_dict.setdefault('forwarding_prefixes',{})
                for key,value in r.items():
                    dict3.update({key:int(value)})
                continue
                
            ##Table id 0xB, instance 0x7FC5BE77F480
            m=p4.match(line)
            if m:
                r=m.groupdict()
                for key,value in r.items():
                    prefix_dict.update({key:value})    
                continue
                
            ##Database: epoch 0
            m=p5.match(line)
            if m:
                prefix_dict.update({'database':m.groups()[0]}) 
                continue
        return result_dict
        
class ShowIpMfibVrfActiveHwRateSchema(MetaParser):
    """Schema for:
        show ip mfib vrf <vrf> active | c HW Rate
    """
    schema = {
        'mfib_group_count': {
            'matched_line':int
        }
    }
    
class ShowIpMfibVrfActiveHwRate(ShowIpMfibVrfActiveHwRateSchema):
    """Parser for show ip mfib vrf <vrf> active | c HW Rate"""

    cli_command = 'show ip mfib vrf {vrf} active | c HW Rate'

    def cli(self, vrf, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(vrf=vrf))
        else:
            out = output

        ret_dict={}

        # initial return dictionary        
        if not out.strip():
            return ret_dict
            
        out=out.strip()
        if out:
            ret_dict['mfib_group_count']={}
            ret_dict['mfib_group_count']['matched_line']=int(out.split("=")[1])
                
        return ret_dict
        
class ShowIpMfibVrfActiveSchema(MetaParser):
    """Schema for:
        show ip mfib vrf <vrf> active
    """
    schema = {
        'vrf': {
            Any():{
                'groups':{
                    Any():{
                        'source':str,
                        'sw_rate_details':{
                            'sw_rate_utilized':int,
                            'utilised_speed_type':str,
                            'max_sw_rate':int,
                            'max_sw_speed_type':str,
                            'duration':str,
                        },
                        'hw_rate_details':{
                            'hw_rate_utilized':int,
                            'utilised_speed_type':str,
                            'max_hw_rate':int,
                            'max_hw_speed_type':str,
                        },
                    },
                },
            },
        }
    }
    
class ShowIpMfibVrfActive(ShowIpMfibVrfActiveSchema):
    """Parser for show ip mfib vrf <vrf> active"""

    cli_command = 'show ip mfib vrf {vrf} active'

    def cli(self, vrf, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(vrf=vrf))
        else:
            out = output

        # initial return dictionary
        result_dict = {}
        
        if not out.strip():
            return result_dict
    
        ##VRF vrf3001
        p1=re.compile(r"^VRF (\S+)$")
        
        ##Group: 228.1.1.1
        p2=re.compile(r"^Group:\s+(\S+)$")
        
        ##Source: 161.1.1.2,
        ##RP-tree,
        p3=re.compile(r"(?:Source: +)?(\S+)\,$")
        
        ##SW Rate: 100 pps/0 kbps(1sec), 0 kbps(last 210 sec)
        p4=re.compile(r"^SW Rate: +(?P<sw_rate_utilized>\d+) +(?P<utilised_speed_type>\S+)\/"
                      r"(?P<max_sw_rate>\d+) +(?P<max_sw_speed_type>\S+)\(.*\(last +(?P<duration>.*)\)$")
                      
        ##HW Rate: 2000 pps/7750 kbps(1sec)
        p5=re.compile(r"^HW Rate: +(?P<hw_rate_utilized>\d+) +(?P<utilised_speed_type>\S+)\/"
                    r"(?P<max_hw_rate>\d+) +(?P<max_hw_speed_type>\S+)\(.*$")

        for line in out.splitlines():
            line = line.strip()
            
            ##VRF vrf3001
            m=p1.match(line)
            if m:
                main_dict=result_dict.setdefault("vrf",{}).setdefault(m.groups()[0],{})
                continue
                
            ##Group: 228.1.1.1
            m=p2.match(line)
            if m:
                group_dict=main_dict.setdefault('groups',{}).setdefault(m.groups()[0],{})
                continue
                
            ##Source: 161.1.1.2,
            m=p3.match(line)
            if m:
                group_dict['source']=m.groups()[0]
                continue
                
            ##SW Rate: 100 pps/0 kbps(1sec), 0 kbps(last 210 sec)
            m=p4.match(line)
            if m:
                r=m.groupdict()
                sw_details=group_dict.setdefault("sw_rate_details",{})
                for key,value in r.items():
                    sw_details[key]=int(value) if value.isdigit() else value.strip()
                continue
                
            ##HW Rate: 2000 pps/7750 kbps(1sec)
            m=p5.match(line)
            if m:
                r=m.groupdict()
                hw_details=group_dict.setdefault("hw_rate_details",{})
                for key,value in r.items():
                    hw_details[key]=int(value) if value.isdigit() else value.strip()
                continue
                
        return result_dict

        
# ======================================================
# Parser for 'show ip mfib summary '
# ======================================================

class ShowIpMfibSummarySchema(MetaParser):
    """Schema for show ip mfib summary"""

    schema = {
        's_g_entry': int,
        'star_g_entry': str,
        'star_g_m_entry': str,
    }

class ShowIpMfibSummary(ShowIpMfibSummarySchema):
    """Parser for show ip mfib summary"""

    cli_command = 'show ip mfib summary'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
            
        #  Forwarding prefixes: [0 (S,G), 5 (*,G), 3 (*,G/m)]
        p1 = re.compile(r"^Forwarding\s+prefixes:\s+\[(?P<s_g_entry>\d+)\s+\(S,G\),\s+(?P<star_g_entry>\d+)\s+\(\*,G\),\s+(?P<star_g_m_entry>\d+)\s+\(\*,G/m\)\]$")
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #  Forwarding prefixes: [0 (S,G), 5 (*,G), 3 (*,G/m)]
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['s_g_entry'] = int(dict_val['s_g_entry'])
                ret_dict['star_g_entry'] = dict_val['star_g_entry']
                ret_dict['star_g_m_entry'] = dict_val['star_g_m_entry']
                continue
        return ret_dict

# ======================================================
# Parser for 'show ipv6 mfib summary '
# ======================================================

class ShowIpv6MfibSummarySchema(MetaParser):
    """Schema for show ipv6 mfib summary"""

    schema = {
        's_g_entry': int,
        'star_g_entry': int,
        'star_g_m_entry': int,
    }

class ShowIpv6MfibSummary(ShowIpv6MfibSummarySchema):
    """Parser for show ipv6 mfib summary"""

    cli_command = 'show ipv6 mfib summary'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
            
        #  Forwarding prefixes: [0 (S,G), 5 (*,G), 3 (*,G/m)]
        p1 = re.compile(r"^Forwarding\s+prefixes:\s+\[(?P<s_g_entry>\d+)\s+\(S,G\),\s+(?P<star_g_entry>\d+)\s+\(\*,G\),\s+(?P<star_g_m_entry>\d+)\s+\(\*,G/m\)\]$")
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #  Forwarding prefixes: [0 (S,G), 5 (*,G), 3 (*,G/m)]
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['s_g_entry'] = int(dict_val['s_g_entry'])
                ret_dict['star_g_entry'] = int(dict_val['star_g_entry'])
                ret_dict['star_g_m_entry'] = int(dict_val['star_g_m_entry'])
                continue
        return ret_dict

# ======================================================
# Parser for 'show ip mfib | count <interface>'
# ======================================================

class ShowIpMfibCountSchema(MetaParser):
    """Schema for show ip mfib count"""

    schema = {
        'number_of_lines': int,
    }

class ShowIpMfibCount(ShowIpMfibCountSchema):
    """Parser for show ip mfib count"""

    cli_command = 'show ip mfib | count {interface}'

    def cli(self, interface, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))
            
        # Number of lines which match regexp = 6500
        p1 = re.compile(r"^Number of lines which match regexp\s+= (?P<number_of_lines>\S+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Number of lines which match regexp = 6500
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['number_of_lines'] = int(dict_val['number_of_lines'])
                continue

        return ret_dict

# ======================================================
# Parser for 'show ip mfib active'
# ======================================================
class ShowIpMfibActiveSchema(MetaParser):
    """Schema for:
        show ip mfib active
        show ip mfib vrf <vrf> active
    """
    schema = {
        'vrf': {
            Any():{
                'groups':{
                    Any():{
                        'source':str,
                        'sw_rate_details':{
                            'sw_rate_utilized':int,
                            'utilised_speed_type':str,
                            'max_sw_rate':int,
                            'max_sw_speed_type':str,
                            'duration':str,
                        },
                        'hw_rate_details':{
                            'hw_rate_utilized':int,
                            'utilised_speed_type':str,
                            'max_hw_rate':int,
                            'max_hw_speed_type':str,
                        },
                    },
                },
            },
        }
    }
    
class ShowIpMfibActive(ShowIpMfibActiveSchema):
    """Parser for 
    show ip mfib active
    """

    cli_command = 'show ip mfib active'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        result_dict = {}
        
        if not output.strip():
            return result_dict
        
        ##Group: 228.1.1.1
        p2=re.compile(r"^Group:\s+(\S+)$")
        
        ##Source: 161.1.1.2,
        ##RP-tree,
        p3=re.compile(r"(?:Source: +)?(\S+)\,$")
        
        ##SW Rate: 100 pps/0 kbps(1sec), 0 kbps(last 210 sec)
        p4=re.compile(r"^SW Rate: +(?P<sw_rate_utilized>\d+) +(?P<utilised_speed_type>\S+)\/"
                      r"(?P<max_sw_rate>\d+) +(?P<max_sw_speed_type>\S+)\(.*\(last +(?P<duration>.*)\)$")
                      
        ##HW Rate: 2000 pps/7750 kbps(1sec)
        p5=re.compile(r"^HW Rate: +(?P<hw_rate_utilized>\d+) +(?P<utilised_speed_type>\S+)\/"
                    r"(?P<max_hw_rate>\d+) +(?P<max_hw_speed_type>\S+)\(.*$")

        main_dict=result_dict.setdefault("vrf",{}).setdefault('Default',{})
        
        for line in output.splitlines():
            line = line.strip()
            
            ##Group: 228.1.1.1
            m=p2.match(line)
            if m:
                group_dict=main_dict.setdefault('groups',{}).setdefault(m.groups()[0],{})
                continue
                
            ##Source: 161.1.1.2,
            m=p3.match(line)
            if m:
                group_dict['source']=m.groups()[0]
                continue
                
            ##SW Rate: 100 pps/0 kbps(1sec), 0 kbps(last 210 sec)
            m=p4.match(line)
            if m:
                r=m.groupdict()
                sw_details=group_dict.setdefault("sw_rate_details",{})
                for key,value in r.items():
                    sw_details[key]=int(value) if value.isdigit() else value.strip()
                continue
                
            ##HW Rate: 2000 pps/7750 kbps(1sec)
            m=p5.match(line)
            if m:
                r=m.groupdict()
                hw_details=group_dict.setdefault("hw_rate_details",{})
                for key,value in r.items():
                    hw_details[key]=int(value) if value.isdigit() else value.strip()
                continue
                
        return result_dict
     

# ======================================================
# Parser for 'show ip mfib vrf <vrf> summary '
# ======================================================
class ShowIpv6MfibVrfSummarySchema(MetaParser):
    """Schema for:
        show ip mfib vrf {vrf} summary
    """
    schema = {
        'vrf': {
            Any():{
                'prefixes':{
                    'total':int,
                    'fwd':int,
                    'non_fwd':int,
                    'deleted':int
                },
                'ioitems':{
                    'total':int,
                    'fwd':int,
                    'non_fwd':int,
                    'deleted':int
                },
                'forwarding_prefixes':{
                    's_g':int,
                    'g':int,
                    'g_m':int
                },
                'table_id':str,
                'instance':str,
                'database':str
            },
        }
    }
    
class ShowIpv6MfibVrfSummary(ShowIpv6MfibVrfSummarySchema):
    """Parser for show ipv6 mfib vrf {vrf} summary"""

    cli_command = 'show ipv6 mfib vrf {vrf} summary'

    def cli(self, vrf, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(vrf=vrf))

        # initial return dictionary
        result_dict = {}
    
        ##VRF vrf3001
        p1=re.compile(r"^VRF (\S+)$")
        
        ##49 prefixes (49/0/0 fwd/non-fwd/deleted)
        ##98 ioitems (98/0/0 fwd/non-fwd/deleted)
        p2=re.compile(r"^(?P<total>\d+)\s+(?P<field>\S+) \((?P<fwd>\d+)\/(?P<non_fwd>\d+)\/(?P<deleted>\d+).*$")
        
        ##Forwarding prefixes: [20 (S,G), 27 (*,G), 2 (*,G/m)]
        p3=re.compile(r"^Forwarding prefixes:\s+\[(?P<s_g>\d+)[ \(A-z\,\)]+\,\s+(?P<g>\d+)[ \(\*\,A-Z\)]+\,\s+(?P<g_m>\d+).*$")
        
        ##Table id 0xB, instance 0x7FC5BE77F480
        p4=re.compile(r"^Table id (?P<table_id>\S+)\,\s+instance\s+(?P<instance>\S+)$")
        
        ##Database: epoch 0
        p5=re.compile(r"Database: ([a-z0-9 ]+)")
        
        for line in output.splitlines():
            line=line.strip()
            
            ##VRF vrf3001
            m=p1.match(line)
            if m:
               prefix_dict=result_dict.setdefault('vrf',{}).setdefault(m.groups()[0],{}) 
               continue
               
            ##49 prefixes (49/0/0 fwd/non-fwd/deleted)
            ##98 ioitems (98/0/0 fwd/non-fwd/deleted)
            m=p2.match(line)
            if m:
                r = m.groupdict()
                dict2=prefix_dict.setdefault(r['field'],{})
                r.pop('field')
                for key,value in r.items():
                    dict2.update({key:int(value)})
                continue
                
            ##Forwarding prefixes: [20 (S,G), 27 (*,G), 2 (*,G/m)]
            m=p3.match(line)
            if m:
                r = m.groupdict()
                dict3=prefix_dict.setdefault('forwarding_prefixes',{})
                for key,value in r.items():
                    dict3.update({key:int(value)})
                continue
                
            ##Table id 0xB, instance 0x7FC5BE77F480
            m=p4.match(line)
            if m:
                r = m.groupdict()
                for key,value in r.items():
                    prefix_dict.update({key:value})    
                continue
                
            ##Database: epoch 0
            m=p5.match(line)
            if m:
                prefix_dict.update({'database':m.groups()[0]}) 
                continue
        return result_dict

class ShowIpv6MfibInterfaceSchema(MetaParser):
    """Schema for show ipv6 mfib interface"""
    schema = {
        'configuration_status': str,
        'operational_status': str,
        'initialization_state': str,
        'total_signalling_packets_queued': int,
        'process_status': str,
        'tables': {
            'active': int,
            'mrib': int,
            'io': int
        },
        'interfaces': {
            str: {
                'status': str,
                'cef_based_output': {
                    'configured': str,
                    'available': str
                }
            }
        }
    }


class ShowIpv6MfibInterface(ShowIpv6MfibInterfaceSchema):
    """Parser for show ipv6 mfib interface"""

    cli_command = 'show ipv6 mfib interface'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize parsed data structure
        parsed_dict = {}

        # Regular expressions for parsing the output
        
        #Configuration Status: enabled
        p1 = re.compile(r'^Configuration +Status: +(?P<configuration_status>\S+)$')

        #Operational Status: running
        p2 = re.compile(r'^Operational +Status: +(?P<operational_status>\S+)$')

        #Initialization State: Running
        p3 = re.compile(r'^Initialization +State: +(?P<initialization_state>\S+)$')

        #Total signalling packets queued: 0
        p4 = re.compile(r'^Total +signalling +packets +queued: +(?P<total_signalling_packets_queued>\d+)$')
        
        #Process Status: may enable - 3 - pid 711
        p5 = re.compile(r'^Process +Status: +(?P<process_status>.+)$')

        #Tables 1/1/0 (active/mrib/io)
        p6 = re.compile(r'^Tables +(?P<active>\d+)/(?P<mrib>\d+)/(?P<io>\d+) +\(active/mrib/io\)$')

        #TenGigabitEthernet0/1/0    up     [yes       ,yes      ]
        p7 = re.compile(r'^(?P<interface>\S+) +(?P<status>\S+) +\[(?P<configured>\S+) +,(?P<available>\S+) +\]$')

        for line in output.splitlines():
            line = line.strip()

            # Match each line with the appropriate regex
            #Configuration Status: enabled
            m = p1.match(line)
            if m:
                parsed_dict['configuration_status'] = m.group('configuration_status')
                continue

            #Operational Status: running
            m = p2.match(line)
            if m:
                parsed_dict['operational_status'] = m.group('operational_status')
                continue

            #Initialization State: Running
            m = p3.match(line)
            if m:
                parsed_dict['initialization_state'] = m.group('initialization_state')
                continue

            #Total signalling packets queued: 0
            m = p4.match(line)
            if m:
                parsed_dict['total_signalling_packets_queued'] = int(m.group('total_signalling_packets_queued'))
                continue

            #Process Status: may enable - 3 - pid 711
            m = p5.match(line)
            if m:
                parsed_dict['process_status'] = m.group('process_status')
                continue

            #Tables 1/1/0 (active/mrib/io)
            m = p6.match(line)
            if m:
                tables_dict = parsed_dict.setdefault('tables', {})
                tables_dict['active'] = int(m.group('active'))
                tables_dict['mrib'] = int(m.group('mrib'))
                tables_dict['io'] = int(m.group('io'))
                continue

            #TenGigabitEthernet0/1/0    up     [yes       ,yes      ]
            m = p7.match(line)
            if m:
                interface = m.group('interface')
                interface_dict = parsed_dict.setdefault('interfaces', {}).setdefault(interface, {})
                interface_dict['status'] = m.group('status')
                cef_based_output_dict = interface_dict.setdefault('cef_based_output', {})
                cef_based_output_dict['configured'] = m.group('configured')
                cef_based_output_dict['available'] = m.group('available')
                continue

        return parsed_dict


# ===============================================
# Schema for:
#   * 'show ipv6 mfib active'
# ===============================================
class ShowIpv6MfibActiveSchema(MetaParser):
    """Schema for show ipv6 mfib active."""

    schema = {
        'active_multicast_sources': {
            'threshold': str,
            Optional('group'): str
        }
    }


# ===============================================
# Parser for:
#   * 'show ipv6 mfib active'
# ===============================================
class ShowIpv6MfibActive(ShowIpv6MfibActiveSchema):
    """Parser for show ipv6 mfib active."""

    cli_command = 'show ipv6 mfib active'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize return dictionary
        parsed_dict = {}

        # Active Multicast Sources - sending >= 4 kbps
        p1 = re.compile(r'^Active\s+Multicast\s+Sources\s+-\s+sending\s+>=\s+(?P<threshold>\S+\s+\S+)$')

        # Default
        p2 = re.compile(r'^(?P<vrf>\S+)$')

        current_vrf = None

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Active Multicast Sources - sending >= 4 kbps
            m = p1.match(line)
            if m:
                threshold = m.groupdict()['threshold']
                parsed_dict['active_multicast_sources'] = {
                    'threshold': threshold
                }
                continue

            # Default
            m = p2.match(line)
            if m:
                vrf_name = m.groupdict()['vrf']
                current_vrf = vrf_name
                
                parsed_dict['active_multicast_sources']['group'] = current_vrf
                continue

        return parsed_dict
