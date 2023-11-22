'''show_netconf.py
IOSXE parsers for the following commands

    * 'show netconf session'
    * 'show netconf-yang datastores'
    * 'show netconf-yang sessions'
    * 'show netconf-yang sessions detail'
    * 'show netconf-yang status
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional, Any, Use, Schema, ListOf

# pyATS
from pyats.utils.exceptions import SchemaTypeError


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
            out = self.device.execute(self.cli_command)
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


class ShowNetconfYangDatastoresSchema(MetaParser):
    '''Schema for:
        * 'show netconf-yang datastores'
    '''

    schema = {
        'datastores': {
            'names': ListOf(str),
        }
    }

class ShowNetconfYangDatastores(ShowNetconfYangDatastoresSchema):
    '''Parser for:
        * 'show netconf-yang datastores'
    '''

    cli_command = 'show netconf-yang datastores'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Datastore Name             : running
        # Datastore Name             : candidate
        p1 = re.compile(r'^Datastore Name\s+:\s+(?P<datastore>\S+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Datastore Name             : running
            # Datastore Name             : candidate
            m = p1.match(line)
            if m:
                group = m.groupdict()
                datastore_list = ret_dict.setdefault("datastores", {}).setdefault("names", [])
                datastore_list.append(group['datastore'])
                continue

        return ret_dict


class ShowNetconfYangSessionsSchema(MetaParser):
    '''schema for:
        * show netconf-yang sessions
    '''

    schema = {
        'session_count': int,
        'session_id': {
            int: {
                'transport': str,
                'username': str,
                'source_host': str,
                'global_lock': str,
                Optional('login_time'): str,
                Optional('in_rpcs'): str,
                Optional('in_bad_rpcs'): str,
                Optional('out_rpc_errors'): str,
                Optional('out_notifications'): str,
            }
        }
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


        # Number of sessions : 1
        p1 = re.compile(r'^Number +of +sessions *: +(?P<session_count>\d+)$')

        # 24          netconf-ssh  admin                10.69.35.35             None
        p2 = re.compile(r'^(?P<session_id>\d+) +(?P<transport>\S+) +(?P<username>\S+) +'
                        r'(?P<source_host>\S+) +(?P<global_lock>\S+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            
            # Number of sessions : 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['session_count'] = int(group.get('session_count'))
                continue

            # 24          netconf-ssh  admin                10.69.35.35             None
            m = p2.match(line)
            if m:
                group = m.groupdict()
                session_ids = ret_dict.setdefault('session_id', {})
                session_id = session_ids.setdefault(int(group['session_id']), {})
                session_id.update({
                    'transport': group['transport'],
                    'username': group['username'],
                    'source_host': group['source_host'],
                    'global_lock': group['global_lock'],
                })
                continue

        return ret_dict

class ShowNetconfYangSessionsDetail(ShowNetconfYangSessionsSchema):
    '''parser for:
        * show netconf-yang sessions detail
    '''

    cli_command = 'show netconf-yang sessions detail'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output


        # Number of sessions : 1
        p1 = re.compile(r'^Number +of +sessions *: +(?P<session_count>\d+)$')

        # session-id             : 24
        p2 = re.compile(r'^session-id *: +(?P<session_id>\d+)$')

        # transport : netconf-ssh
        # username : admin
        # source-host : 10.69.35.35
        # login-time : 2020-09-29T15:19:54+00:00
        # in-rpcs : 1
        # in-bad-rpcs : 0
        # out-rpc-errors : 0
        # out-notifications : 0
        # global-lock : None  
        p3 = re.compile(r'^(?P<key>\S+) *: +(?P<data>\S+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()
            

            # Number of sessions : 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['session_count'] = int(group.get('session_count'))
                continue

            # session-id             : 24
            m = p2.match(line)
            if m:
                group = m.groupdict()
                session_ids = ret_dict.setdefault('session_id', {})
                session_id = session_ids.setdefault(int(group['session_id']), {})
                continue

            # transport : netconf-ssh
            # username : admin
            # source-host : 10.69.35.35
            # login-time : 2020-09-29T15:19:54+00:00
            # in-rpcs : 1
            # in-bad-rpcs : 0
            # out-rpc-errors : 0
            # out-notifications : 0
            # global-lock : None  
            m = p3.match(line)
            if m:
                group = m.groupdict()
                session_id.update({
                    group['key'].replace('-', '_'): group['data']
                })
                continue

        return ret_dict

class ShowNetconfYangSessionsDetail(ShowNetconfYangSessionsSchema):
    '''parser for:
        * show netconf-yang sessions detail
    '''

    cli_command = 'show netconf-yang sessions detail'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output


        # Number of sessions : 1
        p1 = re.compile(r'^Number +of +sessions *: +(?P<session_count>\d+)$')

        # session-id             : 24
        p2 = re.compile(r'^session-id *: +(?P<session_id>\d+)$')

        # transport : netconf-ssh
        # username : admin
        # source-host : 10.69.35.35
        # login-time : 2020-09-29T15:19:54+00:00
        # in-rpcs : 1
        # in-bad-rpcs : 0
        # out-rpc-errors : 0
        # out-notifications : 0
        # global-lock : None  
        p3 = re.compile(r'^(?P<key>\S+) *: +(?P<data>\S+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()
            

            # Number of sessions : 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['session_count'] = int(group.get('session_count'))
                continue

            # session-id             : 24
            m = p2.match(line)
            if m:
                group = m.groupdict()
                sessions = ret_dict.setdefault('session_id', {})
                session = sessions.setdefault(int(group['session_id']), {})
                continue

            # transport : netconf-ssh
            # username : admin
            # source-host : 10.69.35.35
            # login-time : 2020-09-29T15:19:54+00:00
            # in-rpcs : 1
            # in-bad-rpcs : 0
            # out-rpc-errors : 0
            # out-notifications : 0
            # global-lock : None  
            m = p3.match(line)
            if m:
                group = m.groupdict()
                session.update({
                    group['key'].replace('-', '_'): group['data']
                })
                continue

        return ret_dict


class ShowNetconfYangStatusSchema(MetaParser):
    '''Schema for:
        * 'show netconf-yang status'
    '''

    schema = {
        'status': str,
        'ssh_port': str,
        'candidate_datastore_status': str,
        Optional('side_effect_sync'): str,
        Optional('turbocli'): str,
        Optional('hostkey_algorithm'): ListOf(str),
        Optional('encryption_algorithm'): ListOf(str),
        Optional('mac_algorithm'): ListOf(str),
        Optional('kex_algorithm'): ListOf(str)
    }

class ShowNetconfYangStatus(ShowNetconfYangStatusSchema):
    '''Parser for:
        * 'show netconf-yang status'
    '''

    cli_command = 'show netconf-yang status'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # netconf-yang: enabled
        p1 = re.compile(r'^netconf-yang:\s+(?P<status>\S+)$')
        # netconf-yang ssh port: 830
        p2 = re.compile(r'^netconf-yang ssh port:\s+(?P<ssh_port>\d+)$')
        # netconf-yang candidate-datastore: enabled
        p3 = re.compile(r'^netconf-yang candidate-datastore:\s+(?P<candidate_datastore_status>\S+)$')
        # netconf-yang side-effect-sync: enabled
        p4 = re.compile(r'^netconf-yang side-effect-sync:\s+(?P<side_effect_sync>\S+)$')
        # netconf-yang turbocli: disabled
        p5 = re.compile(r'^netconf-yang turbocli:\s+(?P<turbocli>\S+)$')
        # netconf-yang ssh hostkey algorithms: rsa-sha2-256,rsa-sha2-512,ssh-rsa
        p6 = re.compile(r'^netconf-yang ssh hostkey algorithms:\s+(?P<hostkey_algorithm>\S+)$')
        # netconf-yang ssh encryption algorithms: aes128-ctr,aes192-ctr,aes256-ctr,aes128-cbc,aes256-cbc
        p7 = re.compile(r'^netconf-yang ssh encryption algorithms:\s+(?P<encryption_algorithm>\S+)$')
        # netconf-yang ssh MAC algorithms: hmac-sha2-256,hmac-sha2-512,hmac-sha1
        p8 = re.compile(r'^netconf-yang ssh MAC algorithms:\s+(?P<mac_algorithm>\S+)$')
        # netconf-yang ssh KEX algorithms: diffie-hellman-group14-sha1,diffie-hellman-group14-sha256,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group16-sha512
        p9 = re.compile(r'^netconf-yang ssh KEX algorithms:\s+(?P<kex_algorithm>\S+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # netconf-yang: enabled
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                ret_dict['status'] = group.pop('status')
            
            # netconf-yang ssh port: 830
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                ret_dict['ssh_port'] = group.pop('ssh_port')

            # netconf-yang candidate-datastore: enabled
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                ret_dict['candidate_datastore_status'] = group.pop('candidate_datastore_status')

            # netconf-yang side-effect-sync: enabled
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                ret_dict['side_effect_sync'] = group.pop('side_effect_sync')

            # netconf-yang turbocli: disabled
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                ret_dict['turbocli'] = group.pop('turbocli')

            # netconf-yang ssh hostkey algorithms: rsa-sha2-256,rsa-sha2-512,ssh-rsa
            m6 = p6.match(line)
            if m6:
                group = m6.groupdict()
                ret_dict['hostkey_algorithm'] = list(group.pop('hostkey_algorithm').strip().split(','))

            # netconf-yang ssh encryption algorithms: aes128-ctr,aes192-ctr,aes256-ctr,aes128-cbc,aes256-cbc
            m7 = p7.match(line)
            if m7:
                group = m7.groupdict()
                ret_dict['encryption_algorithm'] = list(group.pop('encryption_algorithm').strip().split(','))

            # netconf-yang ssh MAC algorithms: hmac-sha2-256,hmac-sha2-512,hmac-sha1
            m8 = p8.match(line)
            if m8:
                group = m8.groupdict()
                ret_dict['mac_algorithm'] = list(group.pop('mac_algorithm').strip().split(','))

            # netconf-yang ssh KEX algorithms: diffie-hellman-group14-sha1,diffie-hellman-group14-sha256,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group16-sha512
            m9 = p9.match(line)
            if m9:
                group = m9.groupdict()
                ret_dict['kex_algorithm'] = list(group.pop('kex_algorithm').strip().split(','))

        return ret_dict
