'''show_netconf.py
IOSXE parsers for the following commands

    * 'show netconf session'
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional, Any, ListOf

class ShowNetconfSessionSchema(MetaParser):
    '''Schema for:
        * 'show netconf session'
    '''

    schema = {
        'open': int,
        'maximum': int,
    }

class ShowNetconfSession(ShowNetconfSessionSchema):
    '''Parser for:
        * 'show netconf session'
    '''

    cli_command = 'show netconf session'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(cli_command)
        else:
            out = output

        # Netconf Sessions: 0 open, maximum is 4
        p1 = re.compile(r'^Netconf +Sessions: +(?P<open>\d+) +open, +maximum +is +(?P<maximum>\d+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Netconf Sessions: 0 open, maximum is 4
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['open'] = int(group.get('open'))
                ret_dict['maximum'] = int(group.get('maximum'))
                continue

        return ret_dict


class ShowNetconfYangSessionsSchema(MetaParser):
    '''schema for:
        * show netconf-yang sessions
    '''

    schema = {
        'datastores': {
            Any(): {
                'lock': str,
                'name': str,
            }
        },
        'session-count': int,
        'sessions': ListOf({
            'session-id': int,
            'transport': str,
            'username': str,
            'source-host': str,
            'global-lock': str,
        })
    }

class ShowNetconfYangSessions(ShowNetconfYangSessionsSchema):
    '''parser for:
        * show netconf-yang sessions
    '''

    cli_command = 'show netconf-yang sessions'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # R: Global-lock on running datastore
        # C: Global-lock on candidate datastore
        # S: Global-lock on startup datastore
        p1 = re.compile(r'^(?P<char>\S+): +(?P<lock>\S+) +on +(?P<name>\S+) +datastore$')

        # Number of sessions : 1
        p2 = re.compile(r'^Number +of +sessions *: +(?P<session_count>\d+)$')

        # 24          netconf-ssh  admin                5.28.35.35             None
        p3 = re.compile(r'^(?P<session_id>\d+) +(?P<transport>\S+) +(?P<username>\S+) +'
                        r'(?P<source_host>\S+) +(?P<global_lock>\S+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # R: Global-lock on running datastore
            # C: Global-lock on candidate datastore
            # S: Global-lock on startup datastore
            m = p1.match(line)
            if m:
                group = m.groupdict()
                datastores = ret_dict.setdefault('datastores', {})
                char = datastores.setdefault(group.get('char'), {})
                char['lock'] = group.get('lock')
                char['name'] = group.get('name')

            # Number of sessions : 1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['session-count'] = group.get('session_count')

            # 24          netconf-ssh  admin                5.28.35.35             None
            m = p3.match(line)
            if m:
                group = m.groupdict()
                sessions_list = ret_dict.setdefault('sessions', [])
                session = dict()
                session.update({
                    'session-id': int(group['session_id']),
                    'transport': group['transport'],
                    'username': group['username'],
                    'source-host': group['source_host'],
                    'global-lock': group['global_lock'],
                })
                sessions_list.append(session)

        return ret_dict
