from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

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
        Any(): {
            'type': str,
            'version': str
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
            'current': out.splitlines()[0].strip()
        }

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

        for line in out.splitlines():
            line = line.strip()

            p1 = re.compile(r'^(?P<ip_address>.*)\s+(?P<type>\w+)\s+(?P<version>\d)$')
            m = p1.match(line)
            if m:
                ip_address = m.groupdict()['ip_address'].strip()
                ret_dict[ip_address] = {'type':'', 'version':''}
                ret_dict[ip_address]['type'] = m.groupdict()['type']
                ret_dict[ip_address]['version'] = m.groupdict()['version']
                continue

        return ret_dict