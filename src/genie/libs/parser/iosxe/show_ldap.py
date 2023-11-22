""" show_ldap.py
    supported commands:
        * Show ldap server all
        * Show ldap server {name} connections
        * Show ldap server {name} statistics
        * Show ldap server {name} summary
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# import parser utils
from genie.libs.parser.utils.common import Common

# ============================================
# Schema for:
#   * 'show ldap server all'
#   * 'show ldap server {name} summary'
# ============================================

class ShowLdapServerAllSchema(MetaParser):
    '''Schema for:
        * 'show ldap server all'
        * 'show ldap server {name} summary'
    '''
    schema = {
        'server': { 
            Any():{
                'server_address' : str,
                'server_listening_port' : int,
                'bind_rootdn' : str,
                'server_mode' : str,
                'cipher_suite' : str,
                'request_timeout' : int,
                'deadtime' : int,
                'state' : str,
                'no_of_active_connections' : int,
                Optional('total_messages') : {
                    'sent' : int,
                    'received' : int,
                },
                Optional('response_delay') : {
                    'average' : int,
                    'maximum' : int,
                },
                Optional('search') : {
                    'success' : int,
                    'failures' : int,
                },
                Optional('bind') : {
                    'success' : int,
                    'failures' : int,
                },
                Optional('connection'): {
                    'closes' : int,
                    'aborts' : int,
                    'fails' : int,
                    'timeouts' : int,
                },

            },
        },
    }

# ============================================
# Parser for:
#   * 'show ldap server all'
#   * 'show ldap server {name} summary'
# ============================================

class ShowLdapServerAll(ShowLdapServerAllSchema):
    '''Super parser for:
        * 'show ldap server all'
        * 'show ldap server {name} summary'
    '''

    cli_command = [
    'show ldap server all', 
    'show ldap server {name} summary'
    ]
    def cli(self, name=None, output=None):
        
        # Init vars
        if output is None:
            if name: 
                cmd = self.cli_command[1].format(name=name)
            else:
                cmd = self.cli_command[0]
            
            output = self.device.execute(cmd)
    
        #Server name :mgmt-ldap
        p1 = re.compile(r'^Server +name\s+:(?P<server_name>.*)$')
        
        #Server Address :10.106.26.254
        p2 = re.compile(r'^Server Address\s+:(?P<server_address>[\d\.]+)$')
        
        #Server listening Port :389
        p3 = re.compile(r'^Server listening Port\s+:(?P<server_listening_port>\d+)$')

        #Bind Root-dn :Administrator
        p4 = re.compile(r'^Bind Root-dn\s+:(?P<bind_rootdn>.*)$')
        
        #Server mode :Non-Secure
        p5 = re.compile(r'^Server mode\s+:(?P<server_mode>.*)$')

        #Cipher Suite :0x10
        p6 = re.compile(r'^Cipher Suite\s+:(?P<cipher_suite>.*)$')
        
        #Request timeout :20
        p7 = re.compile(r'^Request timeout\s+:(?P<request_timeout>\d+)$')
        
        #Deadtime in Mins :0
        p8 = re.compile(r'^Deadtime in Mins\s+:(?P<deadtime>\d+)$')
        
        #State :ALIVE
        p9 = re.compile(r'^State\s+:(?P<state>.*)$')
        
        #No. of active connections :0
        p10 = re.compile(r'^No. of active connections\s+:(?P<no_of_active_connections>\d+)$')

        #Total messages  [Sent:0, Received:0]
        p11 = re.compile(r'^Total messages\s+\[Sent:+(?P<sent>\d+)\, Received:+(?P<received>\d+)\]$')

        #Response delay(ms) [Average:0, Maximum:0]
        p12 = re.compile(r'^Response delay\(ms\) \[Average:+(?P<average>\d+)\, Maximum:+(?P<maximum>\d+)\]$')

        #Search [Success:0, Failures:0]
        p13 = re.compile(r'^Search\s+\[Success:+(?P<success>\d+)\, Failures:+(?P<failures>\d+)\]$')

        #Bind   [Success:0, Failures:0]
        p14 = re.compile(r'^Bind\s+\[Success:+(?P<success>\d+)\, Failures:+(?P<failures>\d+)\]$')

        #Connection   [Closes:0, Aborts:0, Fails:0, Timeouts:0]
        p15 = re.compile(r'^Connection\s+\[Closes:+(?P<closes>\d+)\, Aborts:+(?P<aborts>\d+)\, Fails:+(?P<fails>\d+)\, Timeouts:+(?P<timeouts>\d+)\]$')

        #Initial return dictionary
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            
            #Server name
            m = p1.match(line)
            if m:
                group = m.groupdict()
                server_name = group['server_name']
                server_dict = ret_dict.setdefault('server', {}).setdefault(server_name, {})
                continue
            
            #Server address
            m = p2.match(line)
            if m:
                group = m.groupdict()
                server_dict['server_address'] = group['server_address']
                continue
    
            #Server listening Port
            m = p3.match(line)
            if m:
                group = m.groupdict()
                server_dict['server_listening_port'] = int(group['server_listening_port'])
                continue

            #Bind Root-dn
            m = p4.match(line)
            if m:
                group = m.groupdict()
                server_dict['bind_rootdn'] = group['bind_rootdn']
                continue
                    
            #Server mode
            m = p5.match(line)
            if m:
                group = m.groupdict()
                server_dict['server_mode'] = group['server_mode']
                continue

            #Cipher Suite
            m  = p6.match(line)
            if m:
                group = m.groupdict()
                server_dict['cipher_suite'] = group['cipher_suite']
                continue
            
            #Request timeout
            m = p7.match(line)
            if m:
                group = m.groupdict()
                server_dict['request_timeout'] = int(group['request_timeout'])
                continue
                    
            #Deadtime
            m = p8.match(line)
            if m:
                group = m.groupdict()
                server_dict['deadtime'] = int(group['deadtime'])
                continue
    
            #State
            m = p9.match(line)
            if m:
                group = m.groupdict()
                server_dict['state'] = group['state']
                continue
            
            #No of active connections
            m = p10.match(line)
            if m:
                group = m.groupdict()
                server_dict['no_of_active_connections'] = int(group['no_of_active_connections'])
                continue
            
            #Total messages 
            m = p11.match(line)
            if m:
                group = m.groupdict()
                total_dict = server_dict.setdefault('total_messages',{})
                total_dict['sent'] = int(group['sent'])
                total_dict['received'] = int(group['received'])
                continue
            
            #Response delay(ms) [Average:0, Maximum:0]
            m = p12.match(line)
            if m:
                group = m.groupdict()
                total_dict = server_dict.setdefault('response_delay',{})
                total_dict['average'] = int(group['average'])
                total_dict['maximum'] = int(group['maximum'])
                continue
            
            ##Search [Success:0, Failures:0]
            m = p13.match(line)
            if m:
                group = m.groupdict()
                total_dict = server_dict.setdefault('search',{})
                total_dict['success'] = int(group['success'])
                total_dict['failures'] = int(group['failures'])
                continue
    
            #Bind   [Success:0, Failures:0]
            m = p14.match(line)
            if m:
                group = m.groupdict()
                total_dict = server_dict.setdefault('bind',{})
                total_dict['success'] = int(group['success'])
                total_dict['failures'] = int(group['failures'])
                continue

            #Connection   [Closes:0, Aborts:0, Fails:0, Timeouts:0]
            m = p15.match(line)
            if m:
                group = m.groupdict()
                total_dict = server_dict.setdefault('connection',{})
                total_dict['closes'] = int(group['closes'])
                total_dict['aborts'] = int(group['aborts'])
                total_dict['fails'] = int(group['fails'])
                total_dict['timeouts'] = int(group['timeouts'])
                continue
            
        return ret_dict

# ============================================
# Schema for:
#   * 'show ldap server {name} connections'
# ============================================

class ShowLdapServerConnectionsSchema(MetaParser):
    '''Schema for:
        * 'show ldap server {name} connections'
    '''
    schema = {
        'no_of_active_connections' : int,
    }

# ============================================
# Parser for:
#   * 'show ldap server {name} connections'
# ============================================

class ShowLdapServerConnections(ShowLdapServerConnectionsSchema):
    '''parser for:
        * 'show ldap server {name} connections'
    '''
    cli_command = 'show ldap server {name} connections'

    def cli(self, name=None, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(name=name))
       
        #Initial return dictionary
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            
            #No. of active connections :0
            p1 = re.compile(r'^No. of active connections\s+:(?P<no_of_active_connections>\d+)$')
            
            #No of active connections
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['no_of_active_connections'] = int(group['no_of_active_connections'])
                
        return ret_dict

# ============================================
# Schema for:
#   * 'show ldap server {name} statistics'
# ============================================

class ShowLdapServerStatisticsSchema(MetaParser):
    '''Schema for:
        * 'show ldap server {name} statistics'
    '''
    schema = {
        'total_messages' : {
            'sent' : int,
            'received' : int,
        },
        'response_delay' : {
            'average' : int,
            'maximum' : int,
        },
        'search' : {
            'success' : int,
            'failures' : int,
        },
        'bind' : {
            'success' : int,
            'failures' : int,
        },
        'connection' : {
            'closes' : int,
            'aborts' : int,
            'fails' : int,
            'timeouts' : int,
        },
    }

# ==================================================
# Parser for:
#   * 'show ldap server {name} statistics'
# ==================================================  
class ShowLdapServerStatistics(ShowLdapServerStatisticsSchema): 
    ''' Parser for:
        * 'show ldap server {name} statistics'
    '''
    cli_command = 'show ldap server {name} statistics'
    def cli(self, name="", output=None):
        if output is None:
            out  = self.device.execute(self.cli_command.format(name=name)) 
        else:
            out = output
        
        #Initial return dictionary
        ret_dict = {}
        
        for line in out.splitlines():
            line = line.strip()

            #Total messages  [Sent:0, Received:0]
            p1 = re.compile(r'^Total +messages\s+\[Sent:+(?P<sent>\d+)\, Received:+(?P<received>\d+)\]$')

            #Response delay(ms) [Average:0, Maximum:0]
            p2 = re.compile(r'^Response delay\(ms\) \[Average:+(?P<average>\d+)\, Maximum:+(?P<maximum>\d+)\]$')

            #Search [Success:0, Failures:0]
            p3 = re.compile(r'^Search\s+\[Success:+(?P<success>\d+)\, Failures:+(?P<failures>\d+)\]$')

            #Bind   [Success:0, Failures:0]
            p4 = re.compile(r'^Bind\s+\[Success:+(?P<success>\d+)\, Failures:+(?P<failures>\d+)\]$')

            #Connection   [Closes:0, Aborts:0, Fails:0, Timeouts:0]
            p5 = re.compile(r'^Connection\s+\[Closes:+(?P<closes>\d+)\, Aborts:+(?P<aborts>\d+)\, Fails:+(?P<fails>\d+)\, Timeouts:+(?P<timeouts>\d+)\]$')
   
            #Total messages 
            m = p1.match(line)
            if m:
                group = m.groupdict()
                total_dict = ret_dict.setdefault('total_messages',{})
                total_dict['sent'] = int(group['sent'])
                total_dict['received'] = int(group['received'])
            
            #Response delay(ms) [Average:0, Maximum:0]
            m = p2.match(line)
            if m:
                group = m.groupdict()
                total_dict = ret_dict.setdefault('response_delay',{})
                total_dict['average'] = int(group['average'])
                total_dict['maximum'] = int(group['maximum'])
            
            ##Search [Success:0, Failures:0]
            m = p3.match(line)
            if m:
                group = m.groupdict()
                total_dict = ret_dict.setdefault('search',{})
                total_dict['success'] = int(group['success'])
                total_dict['failures'] = int(group['failures'])
    
            #Bind   [Success:0, Failures:0]
            m = p4.match(line)
            if m:
                group = m.groupdict()
                total_dict = ret_dict.setdefault('bind',{})
                total_dict['success'] = int(group['success'])
                total_dict['failures'] = int(group['failures'])

            #Connection   [Closes:0, Aborts:0, Fails:0, Timeouts:0]
            m = p5.match(line)
            if m:
                group = m.groupdict()
                total_dict = ret_dict.setdefault('connection',{})
                total_dict['closes'] = int(group['closes'])
                total_dict['aborts'] = int(group['aborts'])
                total_dict['fails'] = int(group['fails'])
                total_dict['timeouts'] = int(group['timeouts'])

        return ret_dict