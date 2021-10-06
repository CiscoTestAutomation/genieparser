"""show_tacacs.py
   IOSXE parsers for the following show commands:
     *  show tacacs
     *  show tacacs private
     *  show tacacs public
"""
#python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema,Any,Optional,Or,And,Default,Use


# ==================================================
# Schema for 'show tacacs'
# ==================================================
class ShowTacacsSchema(MetaParser):
    """Schema for show tacacs
                  show tacacs private
                  show tacacs public"""
    schema = {
              'server': {
                  Any(): {
                    'continous_authc_fail_count': int,
                    'continous_authz_fail_count': int,
                    'failed_connect_attempts': int,
                    'server_status': str,
                    'socket_timeouts': int,
                    'socket_aborts': int,
                    'socket_closes': int,
                    'socket_errors': int,
                    'socket_opens': int,
                    'total_packets_recv': int,
                    'total_packets_sent': int,
                    'server_address': str,
                    'server_port': int,
                    'server_type': str
                  },
                },
            }

# ==================================================
# Parser for 'show tacacs'
# ==================================================
class ShowTacacs(ShowTacacsSchema):
    """Parser for show tacacs
                  show tacacs private
                  show tacacs public"""

    cli_command = ['show tacacs {modifier_type}', 'show tacacs']
    def cli(self, modifier_type = '', output = None):
        if output is None:
            if modifier_type:
                cmd = self.cli_command[0].format(modifier_type = modifier_type)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        servertype=''

        # initial dictionary
        resultdict = dict()
        serverdict = dict()

        # initial regexp patterns
        # Tacacs+ Server -  public  :
        p1 = re.compile(r'(Tacacs\+?)\s+(Server)\s+\-\s+(\w+)\s*\:')

        # Server name: ISE-TAC
        p2=re.compile(r'Server\s+name\:\s*(?P<server_name>(.*))')

        # Server address: 11.14.24.174
        p3=re.compile(r'Server\s+address\:\s*(?P<server_address>(.*))')

        # Server port: 49
        p4=re.compile(r'Server\s+port\:\s*(?P<server_port>(.*))')

        # Socket opens:          0
        p5= re.compile(r'Socket\s+opens\:\s*(?P<socket_opens>(\d+))')

        # Socket closes:          0
        p6= re.compile(r'Socket\s+closes\:\s*(?P<socket_closes>(\d+))')

        # Socket aborts:         0
        p7 = re.compile(r'Socket\s+aborts\:\s*(?P<socket_aborts>(\d+))')

        # Socket errors:         0
        p8 = re.compile(r'Socket\s+errors\:\s*(?P<socket_errors>(\d+))')

        # Socket Timeouts:       0
        p9 = re.compile(r'Socket\s+Timeouts\:\s*(?P<socket_timeouts>(\d+))')

        # Failed Connect Attempts:          0
        p10 = re.compile(r'\s*Failed\s+Connect\s+Attempts\:\s*(?P<failed_connect_attempts>(\d+))')

        # Total Packets Sent:          0
        p11 = re.compile(r'Total\s+Packets\s+Sent\:\s*(?P<total_packets_sent>(\d+))')

        # Total Packets Recv:          0
        p12 = re.compile(r'Total\s+Packets\s+Recv\:\s*(?P<total_packets_recv>(\d+))')

        # Server Status: Alive
        p13 = re.compile(r'Server\s+Status\:\s*(?P<server_status>(\w+))')

        # Continous Authc fail count:          0
        p14 = re.compile(r'Continous\s+Authc\s+fail\s+count\:\s*(?P<continous_authc_fail_count>(\d+))')

        # Continous Authz fail count:          0
        p15 = re.compile(r'Continous\s+Authz\s+fail\s+count\:\s*(?P<continous_authz_fail_count>(\d+))')

        for line in out.splitlines():
            line = line.strip()
            
            # Tacacs+ Server -  public  :
            res = p1.match(line)
            if res:
                servertype = res.group(3)
                continue

            # Server name: ISE-TAC
            res = p2.match(line)
            if res:
                group = res.groupdict()
                serverdict = resultdict.setdefault('server', {}).setdefault(group['server_name'], {})
                if servertype:
                    serverdict.update({'server_type': servertype})
                continue
            
            # Server address: 11.14.24.174
            res = p3.match(line)
            if res:
                group = res.groupdict()
                serverdict.update(group)
                continue

            # Server port: 49
            res = p4.match(line)
            if res:
                group = res.groupdict()
                serverdict.update({k: int(v) for k, v in group.items()})
                continue
            
            # Socket opens:          0
            res = p5.match(line)
            if res:
                group = res.groupdict()
                serverdict.update({k: int(v) for k, v in group.items()})
                continue

            # Socket closes:          0
            res = p6.match(line)
            if res:
                group = res.groupdict()
                serverdict.update({k: int(v) for k, v in group.items()})
                continue

            # Socket aborts:         0
            res = p7.match(line)
            if res:
                group = res.groupdict()
                serverdict.update({k: int(v) for k, v in group.items()})
                continue

            # Socket errors:         0
            res = p8.match(line)
            if res:
                group = res.groupdict()
                serverdict.update({k: int(v) for k, v in group.items()})
                continue
            
            # Socket Timeouts:       0
            res = p9.match(line)
            if res:
                group = res.groupdict()
                serverdict.update({k: int(v) for k, v in group.items()})
                continue

            # Failed Connect Attempts:          0
            res = p10.match(line)
            if res:
                group = res.groupdict()
                serverdict.update({k: int(v) for k, v in group.items()})
                continue

            # Total Packets Sent:          0
            res = p11.match(line)
            if res:
                group = res.groupdict()
                serverdict.update({k: int(v) for k, v in group.items()})
                continue
            
            # Total Packets Recv:          0
            res = p12.match(line)
            if res:
                group = res.groupdict()
                serverdict.update({k: int(v) for k, v in group.items()})
                continue

            # Server Status: Alive
            res = p13.match(line)
            if res:
                group = res.groupdict()
                serverdict.update(group)
                continue

            # Continous Authc fail count:          0
            res = p14.match(line)
            if res:
                group = res.groupdict()
                serverdict.update({k: int(v) for k, v in group.items()})
                continue

            # Continous Authz fail count:          0
            res = p15.match(line)
            if res:
                group = res.groupdict()
                serverdict.update({k: int(v) for k, v in group.items()})
                continue
        
        return resultdict
