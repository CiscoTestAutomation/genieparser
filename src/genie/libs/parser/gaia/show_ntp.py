""" show_ntp.py

Check Point Gaia parsers for the following show commands:
    * show ntp active
    * show ntp current
    * show ntp servers

"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any


class ShowNtpActiveSchema(MetaParser):
    schema = {
        'active': str
    }

class ShowNtpCurrentSchema(MetaParser):
    schema = {
        'current': str
    }

class ShowNtpServersSchema(MetaParser):
    schema = {
        'ip_address': {
            Any(): {
                'type': str,
                'version': str
            }
        }
    }

class ShowNtpActive(ShowNtpActiveSchema):
    """ parser for show ntp active """

    cli_command = 'show ntp active'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        if len(out.splitlines()) != 1:
           # something is wrong
            return ret_dict

        ret_dict = {
            'active': out.splitlines()[0].strip()
        }

        return ret_dict

class ShowNtpCurrent(ShowNtpCurrentSchema):
    """ parser for show ntp current """

    cli_command = 'show ntp current'

    # Possible responses to this command are:
    #   'primary and secondary servers are not synchronized'
    #   'No server has yet to be synchronized' 
    #       - These occur when only a single ntp server is configured, or two are configured and are not synchronized
    #       - return value: {'current': 'unsynchronized'}
    #   'The NTP service is inactive'
    #       - This occurs if the command "set ntp service active on" is missing from the config
    #       - return value: {'current': 'inactive'}
    #   '<ip_address>'
    #       - The IP Address of the NTP server that the clock is currently synchronized to
    #       - return value: {'current': '{ip_address}'}

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        if len(out.splitlines()) != 1:
            # something is wrong
            return ret_dict

        p0  = re.compile(r'^The NTP service is inactive')
        p1  = re.compile(r'^primary and secondary servers are not synchronized')
        p2  = re.compile(r'^No server has yet to be synchronized') 
        p3  = re.compile(r'^(?P<ip_address>(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3})')

        for line in out.splitlines():
            
            # The NTP service is inactive
            m = p0.match(line)
            if m:
                ret_dict['current'] = 'inactive'
                continue
            
            # primary and secondary servers are not synchronized
            # no server has yet to be synchronized
            m = (p1.match(line) or p2.match(line))
            if m:
                ret_dict['current'] = 'unsynchronized'
                continue
            
            # <ip_address>
            m = p3.match(line)
            if m:
                ret_dict['current'] = m.groupdict()['ip_address']

        return ret_dict

class ShowNtpServers(ShowNtpServersSchema):
    """ parser for show ntp servers """

    cli_command = 'show ntp servers'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        ''' Sample Output
        gw-a> show ntp servers
        IP Address               Type              Version
        0.pool.ntp.org           Secondary         4
        172.16.121.123          Primary           4
        '''

        p1 = re.compile(r'^(?P<ip_address>.*)\s+(?P<type>\w+)\s+(?P<version>\d)$')

        for line in out.splitlines():
            if 'ip_address' not in ret_dict:
                ret_dict['ip_address']={}

            line = line.strip()

            # 172.16.121.123          Primary           4
            m = p1.match(line)
            if m:
                ip_address = m.groupdict()['ip_address'].strip()
                ret_dict['ip_address'][ip_address] = {'type':'', 'version':''}
                ret_dict['ip_address'][ip_address]['type'] = m.groupdict()['type']
                ret_dict['ip_address'][ip_address]['version'] = m.groupdict()['version']
                continue

        return ret_dict
